"""Portable, read-only checks shared by the SEO workflow releases (stdlib only)."""
from __future__ import annotations
import hashlib
import html
import json
import re
import struct
import csv
import posixpath
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def local_file(root, value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Missing file path')
    root = Path(root).resolve()
    path = (root / value).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f'File escapes package: {value}')
    if not path.is_file() or not path.stat().st_size:
        raise ValueError(f'Missing or empty file: {value}')
    return path

def image_info(path):
    """Inspect actual raster headers; semantic/visual QA remains a separate review."""
    b = Path(path).read_bytes()
    if b.startswith(b'\x89PNG\r\n\x1a\n') and len(b) >= 33:
        width, height = struct.unpack('>II', b[16:24]); kind = 'png'
        if b[12:16] != b'IHDR' or b'IEND' not in b: raise ValueError('Incomplete PNG')
    elif b[:3] == b'\xff\xd8\xff' and b[-2:] == b'\xff\xd9':
        i = 2; width = height = 0; kind = 'jpeg'
        while i < len(b)-8:
            if b[i] != 255: i += 1; continue
            marker = b[i+1]; i += 2
            if marker in (0xd8, 0xd9) or 0xd0 <= marker <= 0xd7: continue
            size = int.from_bytes(b[i:i+2], 'big')
            if size < 2: raise ValueError('Invalid JPEG segment')
            if marker in (0xc0, 0xc1, 0xc2):
                height, width = struct.unpack('>HH', b[i+3:i+7]); break
            i += size
    elif b[:4] == b'RIFF' and b[8:12] == b'WEBP' and len(b) >= 30:
        if int.from_bytes(b[4:8], 'little') + 8 != len(b): raise ValueError('Incomplete WebP')
        chunk = b[12:16]; kind = 'webp'
        if chunk == b'VP8X':
            width = 1 + int.from_bytes(b[24:27], 'little'); height = 1 + int.from_bytes(b[27:30], 'little')
        elif chunk == b'VP8L' and b[20] == 0x2f:
            n = int.from_bytes(b[21:25], 'little'); width = (n & 0x3fff)+1; height = ((n >> 14) & 0x3fff)+1
        elif chunk == b'VP8 ' and b[23:26] == b'\x9d\x01\x2a':
            width = int.from_bytes(b[26:28], 'little') & 0x3fff; height = int.from_bytes(b[28:30], 'little') & 0x3fff
        else: raise ValueError('Unsupported WebP header')
    else: raise ValueError(f'Unsupported or invalid image: {path}')
    if width <= 0 or height <= 0: raise ValueError('Invalid image dimensions')
    return kind, width, height

def check_render(report, root, docx):
    errors = []
    try:
        if report.get('status', '').lower() != 'pass': raise ValueError('Render QA is not pass')
        if report.get('source_docx_sha256') != digest(docx): raise ValueError('Render belongs to a different DOCX')
        if not report.get('reviewed_by') or not report.get('inspection'): raise ValueError('Missing visual inspection record')
        if report.get('reviewer_type') not in {'ai', 'human'}: raise ValueError('Declare render reviewer_type: ai or human')
        pages = report.get('page_files', [])
        if not pages or len(pages) != report.get('page_count'): raise ValueError('Render page count mismatch')
        seen = set()
        for page in pages:
            path = local_file(root, page.get('path'))
            if path in seen: raise ValueError('Duplicate rendered page')
            seen.add(path)
            if digest(path) != page.get('sha256'): raise ValueError(f'Stale rendered page: {path.name}')
            image_info(path)
    except (ValueError, TypeError, KeyError, OSError) as exc: errors.append(str(exc))
    return errors

def docx_content(path):
    with zipfile.ZipFile(path) as z:
        if not {'[Content_Types].xml','_rels/.rels','word/document.xml'} <= set(z.namelist()):
            raise ValueError('Invalid DOCX package: missing required OPC parts')
        tree = ET.fromstring(z.read('word/document.xml'))
        body = tree.find(W+'body')
        paragraphs = []
        for node in body:
            if node.tag == W+'p': paragraphs.append(node)
            elif node.tag == W+'tbl': paragraphs.extend(node.iter(W+'p'))
        texts = [''.join(n.text or '' for n in p.iter(W+'t')) for p in paragraphs]
        headings = []
        for p, text in zip(paragraphs, texts):
            style = p.find('./'+W+'pPr/'+W+'pStyle')
            name = style.get(W+'val', '') if style is not None else ''
            m = re.fullmatch(r'Heading\s*([1-6])', name, re.I)
            if m: headings.append((int(m[1]), text.strip()))
        rels = {}
        if 'word/_rels/document.xml.rels' in z.namelist():
            rels = {x.get('Id'): x.get('Target') for x in ET.fromstring(z.read('word/_rels/document.xml.rels'))}
        links = [rels.get(x.get(R+'id')) for x in tree.iter(W+'hyperlink') if x.get(R+'id')]
        images = [x for x in tree.iter() if x.tag.endswith('}docPr')]
        media = {hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist() if n.startswith('word/media/')}
        hygiene = bool(list(tree.iter(W+'ins')) or list(tree.iter(W+'del')) or 'word/comments.xml' in z.namelist())
        yellow=[]
        for p in paragraphs:
            yellow.append(''.join(''.join(n.text or '' for n in run.iter(W+'t')) for run in p.iter(W+'r') if any(h.get(W+'val')=='yellow' for h in run.iter(W+'highlight'))))
        return {'text': '\n'.join(texts), 'headings': headings, 'links': links, 'images': images, 'media': media, 'hygiene': hygiene, 'table_count':len(body.findall(W+'tbl')), 'yellow_text':'\n'.join(yellow)}

def inline_markdown(text):
    text = re.sub(r'!\[[^\]]*\]\([^\n]*?\)', '', text)
    text = re.sub(r'\[([^\]]+)\]\((?:[^()]|\([^()]*\))*\)', r'\1', text)
    text = re.sub(r'<(https?://[^>]+)>', r'\1', text)
    text = re.sub(r'</?(?:strong|em|b|i|mark|span)(?:\s[^>]*)?>', '', text)
    return html.unescape(text.replace('**','').replace('__','').replace('`','').replace('\\|','|'))

def markdown_text(text):
    lines = []
    if re.search(r'^\[.*\]:|^\[\^|<table\b', text, re.M | re.I):
        raise ValueError('Reference links/footnotes/HTML tables need an explicit canonical export before parity checking')
    for line in text.splitlines():
        if re.match(r'^\s*(```|~~~)', line): continue
        if re.match(r'^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$', line): continue
        line = re.sub(r'^\s{0,3}#{1,6}\s+', '', line)
        line = re.sub(r'^\s*(?:[-*+] |\d+[.)] |>)\s*', '', line)
        if line.strip().startswith('|'): line = ' '.join(line.strip().strip('|').split('|'))
        lines.append(inline_markdown(line))
    return '\n'.join(lines)

def text_tokens(text):
    # Ignore presentation punctuation/whitespace, retain words and numeric data.
    return re.findall(r'\w+', text.casefold(), re.UNICODE)

def check_docx_parity(markdown, docx):
    errors = []
    try:
        data = docx_content(docx)
        if text_tokens(markdown_text(markdown)) != text_tokens(data['text']): errors.append('DOCX/Markdown body or table text differs')
        table_count=len(re.findall(r'^\s*\|?\s*:?-{3,}:?\s*\|(?:\s*:?-{3,}:?\s*\|?)+\s*$',markdown,re.M))
        if data['table_count']<table_count: errors.append('Markdown table was flattened instead of preserved as a Word table')
        headings = [(len(m[1]), inline_markdown(m[2]).strip()) for m in re.finditer(r'^(#{1,6})\s+(.+)$', markdown, re.M)]
        if headings != data['headings']: errors.append('DOCX/Markdown semantic heading sequence differs')
        if sum(level == 1 for level, _ in headings) != 1: errors.append('Exactly one H1 is required')
        if any(b[0] > a[0]+1 for a,b in zip(headings,headings[1:])): errors.append('Heading level skipped')
        md_links = re.findall(r'(?<!!)\[[^\]]*\]\((https?://[^\s)]+)(?:\s+"[^"]*")?\)', markdown)
        if sorted(md_links) != sorted(x for x in data['links'] if x and x.startswith(('http://','https://'))): errors.append('DOCX/Markdown hyperlink targets differ')
        if data['hygiene']: errors.append('Release DOCX contains tracked changes or comments')
        if any(not x.get('descr','').strip() for x in data['images']): errors.append('DOCX image lacks Alt text')
    except (ValueError, OSError, zipfile.BadZipFile, ET.ParseError) as exc: errors.append(str(exc))
    return errors

def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def check_contract(cfg, root, fields):
    contract=read_json(local_file(root,'task-contract.json'))
    return ['Release changed frozen task scope: '+field for field in fields if field not in contract or cfg.get(field)!=contract[field]]

def xlsx_sheets(path):
    ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(path) as z:
        if not {'[Content_Types].xml','_rels/.rels','xl/workbook.xml'} <= set(z.namelist()):
            raise ValueError('Invalid XLSX package: missing required OPC parts')
        workbook=ET.fromstring(z.read('xl/workbook.xml'))
        rels={n.get('Id'):n.get('Target') for n in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        shared=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            shared=[''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        result={}
        for sheet in workbook.find('s:sheets',ns):
            target=rels[sheet.get(R+'id')]
            target=target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/'+target)
            rows=[]
            for row in ET.fromstring(z.read(target)).findall('.//s:sheetData/s:row',ns):
                cells=[]
                for cell in row:
                    index=0
                    for c in re.match(r'[A-Z]+',cell.get('r'))[0]: index=index*26+ord(c)-64
                    while len(cells)<index: cells.append('')
                    value=cell.find('s:v',ns)
                    if cell.get('t')=='e': raise ValueError(f'Workbook formula error in {sheet.get("name")} {cell.get("r")}')
                    if cell.find('s:f',ns) is not None and value is None: raise ValueError('Formula has no recalculated cached result')
                    v=value.text if value is not None else ''
                    if cell.get('t')=='s': v=shared[int(v)]
                    elif cell.get('t')=='inlineStr': v=''.join(n.text or '' for n in cell.findall('.//s:t',ns))
                    cells[index-1]=v or ''
                rows.append(cells)
            result[sheet.get('name')]=rows
        return result

def check_csv_sheet(path, rows):
    with Path(path).open(encoding='utf-8-sig',newline='') as f: expected=list(csv.reader(f))
    def cleaned(table):
        result=[]
        for row in table:
            values=[str(v or '').strip() for v in row]
            while values and not values[-1]: values.pop()
            result.append(values)
        while result and not result[-1]: result.pop()
        return result
    return cleaned(expected)==cleaned(rows)
