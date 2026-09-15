"""Behavioral regressions for stage order, stale evidence and actual artifacts."""
import csv
import importlib.util
import json
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import unittest
import zipfile
import zlib
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parents[1]
WF=ROOT if (ROOT/'workflow.json').exists() else ROOT/'skill/optimize-page-seo-copy-v3'
SCRIPTS=WF/('tools' if (WF/'tools').exists() else 'scripts')
sys.path.insert(0,str(SCRIPTS))
from delivery_integrity import digest, check_render, check_docx_parity, image_info
from workflow_state import read_json, save, snapshot, advance, validate, now

def png(path,width=8,height=4):
    def chunk(kind,data): return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data)&0xffffffff)
    data=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',width,height,8,2,0,0,0))+chunk(b'IDAT',zlib.compress((b'\0'+b'\xff\xff\xff'*width)*height))+chunk(b'IEND',b'')
    Path(path).write_bytes(data)

def docx(path,blocks,links=(),highlight=False):
    paragraphs=[]
    for level,text in blocks:
        style=f'<w:pPr><w:pStyle w:val="Heading{level}"/></w:pPr>' if level else ''
        rpr='<w:rPr><w:highlight w:val="yellow"/></w:rPr>' if highlight else ''
        paragraphs.append(f'<w:p>{style}<w:r>{rpr}<w:t>{escape(text)}</w:t></w:r></w:p>')
    for i,(label,url) in enumerate(links): paragraphs.append(f'<w:p><w:hyperlink r:id="r{i}"><w:r><w:t>{escape(label)}</w:t></w:r></w:hyperlink></w:p>')
    with zipfile.ZipFile(path,'w') as z:
        z.writestr('[Content_Types].xml','<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>')
        z.writestr('_rels/.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rDoc" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>')
        z.writestr('word/document.xml','<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>'+''.join(paragraphs)+'</w:body></w:document>')
        z.writestr('word/_rels/document.xml.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'+''.join(f'<Relationship Id="r{i}" Target="{escape(url)}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" TargetMode="External"/>' for i,(_,url) in enumerate(links))+'</Relationships>')

def xlsx(path,sheets):
    with zipfile.ZipFile(path,'w') as z:
        z.writestr('[Content_Types].xml','<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'+''.join(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' for i in range(1,len(sheets)+1))+'</Types>')
        z.writestr('_rels/.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rBook" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr('xl/workbook.xml','<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>'+''.join(f'<sheet name="{escape(name)}" sheetId="{i}" r:id="r{i}"/>' for i,name in enumerate(sheets,1))+'</sheets></workbook>')
        z.writestr('xl/_rels/workbook.xml.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'+''.join(f'<Relationship Id="r{i}" Target="worksheets/sheet{i}.xml"/>' for i,_ in enumerate(sheets,1))+'</Relationships>')
        for i,rows in enumerate(sheets.values(),1):
            xml=[]
            for ri,row in enumerate(rows,1):
                cells=[]
                for ci,value in enumerate(row,1):
                    n=ci;col=''
                    while n:n,r=divmod(n-1,26);col=chr(65+r)+col
                    cells.append(f'<c r="{col}{ri}" t="inlineStr"><is><t>{escape(str(value))}</t></is></c>')
                xml.append('<row>'+''.join(cells)+'</row>')
            z.writestr(f'xl/worksheets/sheet{i}.xml','<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>'+''.join(xml)+'</sheetData></worksheet>')

def init_state(run):
    (run/'task-brief.md').write_text('Synthetic regression fixture; no live research or publication. No images requested.')
    if not (run/'task-contract.json').exists():
        defaults={'human_approval_required':False,'article_type':'vs','mode':'new_article','images_required':False,'visual_scope':'NAMED_SECTIONS','required_visual_sections':[],'visuals_not_required':True,'required_copy_locations':['H1'],'required_visual_modules':[],'keyword_visibility':'not_requested'}
        config=read_json(WF/'workflow.json');save(run/'task-contract.json',{key:defaults[key] for key in config['contract_fields']})
    result=subprocess.run([sys.executable,str(SCRIPTS/'workflow_state.py'),'--workflow-root',str(WF),'--run-dir',str(run),'init','--run-id','TEST','--input','task-brief.md'],capture_output=True,text=True)
    if result.returncode: raise AssertionError(result.stdout+result.stderr)
    return read_json(run/'workflow-state.json')

def complete_stages(run,evidence='task-brief.md'):
    config=read_json(WF/'workflow.json');state=init_state(run)
    (run/'records').mkdir(exist_ok=True)
    for stage in config['stages']:
        report={'run_id':'TEST','stage':stage['id'],'result':'pass','checks':[{'id':name,'result':'pass','reviewer_type':'automated','reviewed_by':'regression fixture','finding':'Synthetic artifact available for execution test','evidence':[evidence]} for name in stage['checks']]}
        relative='records/'+stage['id']+'.json';save(run/relative,report)
        state=advance(state,config,WF,run,stage['id'],relative);save(run/'workflow-state.json',state)
    return state

class ExecutionTests(unittest.TestCase):
    def setUp(self): self.temp=tempfile.TemporaryDirectory();self.run=Path(self.temp.name)
    def tearDown(self): self.temp.cleanup()
    def test_real_image_dimensions(self):
        p=self.run/'image.png';png(p,13,7);self.assertEqual(image_info(p),('png',13,7))
    def test_fake_image_rejected(self):
        p=self.run/'image.webp';p.write_text('not an image')
        with self.assertRaises(ValueError):image_info(p)
    def test_complete_stages(self):
        state=complete_stages(self.run);self.assertEqual(validate(state,read_json(WF/'workflow.json'),WF,self.run),[])
    def test_skipped_stage_rejected(self):
        state=init_state(self.run);config=read_json(WF/'workflow.json')
        with self.assertRaises(ValueError):advance(state,config,WF,self.run,config['stages'][1]['id'],'missing.json')
    def test_unfinished_stages_block_release(self):
        self.assertTrue(validate(init_state(self.run),read_json(WF/'workflow.json'),WF,self.run))
    def test_changed_input_rejected(self):
        state=complete_stages(self.run);(self.run/'task-brief.md').write_text('new scope')
        self.assertTrue(validate(state,read_json(WF/'workflow.json'),WF,self.run))
    def test_changed_stage_evidence_rejected(self):
        (self.run/'evidence.md').write_text('original');state=complete_stages(self.run,'evidence.md')
        (self.run/'evidence.md').write_text('changed')
        self.assertTrue(validate(state,read_json(WF/'workflow.json'),WF,self.run))
    def test_render_current_and_stale(self):
        d=self.run/'article.docx';docx(d,[(1,'Topic'),(0,'Complete text')]);png(self.run/'page.png')
        report={'status':'pass','source_docx_sha256':digest(d),'reviewer_type':'ai','reviewed_by':'Test reviewer','inspection':'Synthetic page inspected','page_count':1,'page_files':[{'path':'page.png','sha256':digest(self.run/'page.png')}]}
        self.assertEqual(check_render(report,self.run,d),[])
        docx(d,[(1,'Topic'),(0,'Changed text')]);self.assertTrue(check_render(report,self.run,d))
    def test_render_missing_page(self):
        d=self.run/'article.docx';docx(d,[(1,'Topic')])
        report={'status':'pass','source_docx_sha256':digest(d),'reviewer_type':'ai','reviewed_by':'Test','inspection':'fixture','page_count':1,'page_files':[{'path':'missing.png','sha256':'x'}]}
        self.assertTrue(check_render(report,self.run,d))
    def test_body_loss_rejected(self):
        d=self.run/'article.docx';docx(d,[(1,'Topic'),(0,'First paragraph'),(0,'Second paragraph')])
        md='# Topic\n\nFirst paragraph\n\nSecond paragraph';self.assertEqual(check_docx_parity(md,d),[])
        docx(d,[(1,'Topic'),(0,'First paragraph')]);self.assertTrue(check_docx_parity(md,d))
    def test_wrong_hyperlink_rejected(self):
        d=self.run/'article.docx';docx(d,[(1,'Topic')],[('Source','https://wrong.example')])
        self.assertTrue(check_docx_parity('# Topic\n\n[Source](https://correct.example)',d))
    def test_reference_markup_fails_explicitly(self):
        d=self.run/'article.docx';docx(d,[(1,'Topic')])
        self.assertTrue(check_docx_parity('# Topic\n[a]: https://example.com',d))

if __name__=='__main__':unittest.main()
