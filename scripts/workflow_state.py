"""Record loaded rule versions and enforce ordered, artifact-backed workflow stages.

This records file loading and reviewer evidence, not proof of model comprehension.
It does not execute arbitrary commands supplied by task artifacts.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
from delivery_integrity import digest, local_file, read_json

def now(): return datetime.now(timezone.utc).isoformat()

def save(path, data):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name+'.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    temp.replace(path)

def snapshot(root, paths):
    return [{'path': str(Path(p).as_posix()), 'sha256': digest(local_file(root,p))} for p in paths]

def stale(root, entries):
    errors=[]
    for entry in entries:
        try:
            if digest(local_file(root,entry['path'])) != entry['sha256']: errors.append('Changed file: '+entry['path'])
        except (ValueError, OSError, KeyError) as exc: errors.append(str(exc))
    return errors

def validate(state, config, workflow_root, run_root, complete=True):
    errors=[]
    if state.get('workflow_version') != config['version'] or state.get('workflow_id') != config['workflow_id']:
        errors.append('Workflow identity/version mismatch; initialize a new run')
    if state.get('config_sha256') != digest(Path(workflow_root)/'workflow.json'): errors.append('Workflow configuration changed')
    expected_rules=set(config['bootstrap_files'])
    if {x['path'] for x in state.get('loaded_files',[])} != expected_rules: errors.append('Bootstrap file inventory differs')
    errors += stale(workflow_root,state.get('loaded_files',[]))
    errors += stale(run_root,state.get('inputs',[]))
    stages=state.get('stages',[])
    names=[s['id'] for s in config['stages']]
    if [s.get('id') for s in stages] != names[:len(stages)]: errors.append('Stage sequence is invalid')
    if complete and len(stages) != len(names): errors.append('Required workflow stages are incomplete')
    for stage in stages:
        errors += stale(run_root,stage.get('files',[]))
        if stage.get('status') != 'pass': errors.append('Stage did not pass: '+stage.get('id',''))
    if not state.get('inputs'): errors.append('No task input files recorded')
    if 'task-contract.json' not in {x.get('path') for x in state.get('inputs',[])}:
        errors.append('Frozen task contract is missing from recorded inputs')
    return errors

def advance(state, config, workflow_root, run_root, stage_id, report_path):
    errors=validate(state,config,workflow_root,run_root,complete=False)
    if errors: raise ValueError('; '.join(errors))
    i=len(state['stages'])
    if i >= len(config['stages']) or config['stages'][i]['id'] != stage_id:
        raise ValueError('Cannot skip, repeat, or reorder a stage; use invalidate for revisions')
    path=local_file(run_root,report_path); report=read_json(path)
    if report.get('run_id') != state['run_id'] or report.get('stage') != stage_id: raise ValueError('Report belongs to a different run/stage')
    if report.get('result') != 'pass': raise ValueError('Stage report must pass')
    checks=report.get('checks',[])
    if {x.get('id') for x in checks} != set(config['stages'][i]['checks']) or len(checks)!=len(config['stages'][i]['checks']):
        raise ValueError('Missing, extra, or duplicate stage checks')
    evidence=set()
    for check in checks:
        if check.get('result') != 'pass' or not check.get('reviewed_by') or check.get('reviewer_type') not in {'ai','human','automated'}:
            raise ValueError('Missing reviewer or unresolved stage check')
        if not check.get('evidence'): raise ValueError('Check has no artifact evidence')
        if not check.get('finding'): raise ValueError('Check needs a specific finding')
        evidence.update(check['evidence'])
    if report_path in evidence: raise ValueError('A report cannot be its own only evidence')
    files=snapshot(run_root, sorted(evidence | {report_path}))
    state['stages'].append({'id':stage_id,'status':'pass','completed_at':now(),'files':files})
    return state

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--workflow-root',type=Path,required=True)
    p.add_argument('--run-dir',type=Path,required=True)
    p.add_argument('command',choices=['init','advance','verify','invalidate'])
    p.add_argument('--run-id'); p.add_argument('--input',action='append',default=[])
    p.add_argument('--stage'); p.add_argument('--report')
    args=p.parse_args(); root=args.workflow_root.resolve(); run=args.run_dir.resolve()
    path=run/'workflow-state.json'; config=read_json(root/'workflow.json')
    try:
        if args.command=='init':
            if path.exists(): raise ValueError('Run already exists; resume it or choose a new run directory')
            if not args.run_id or not args.input: raise ValueError('init requires run ID and input files, including the task brief')
            contract=read_json(local_file(run,'task-contract.json'))
            for field in config['contract_fields']:
                if field not in contract: raise ValueError('Task contract lacks resolved scope: '+field)
            args.input=list(dict.fromkeys(args.input+['task-contract.json']))
            state={'schema_version':1,'workflow_id':config['workflow_id'],'workflow_version':config['version'],
                   'run_id':args.run_id,'created_at':now(),'config_sha256':digest(root/'workflow.json'),
                   'loaded_files':snapshot(root,config['bootstrap_files']),'inputs':snapshot(run,args.input),'stages':[]}
            save(path,state)
            print(json.dumps({'status':'initialized','loaded_files':state['loaded_files'],'next_stage':config['stages'][0]['id']},ensure_ascii=False,indent=2))
        elif args.command=='advance':
            state=advance(read_json(path),config,root,run,args.stage,args.report);save(path,state)
            print('PASS: stage '+args.stage)
        elif args.command=='invalidate':
            state=read_json(path); names=[x['id'] for x in config['stages']]
            if args.stage not in names: raise ValueError('Unknown stage')
            # Preserve history; do not silently bless changed inputs or workflow rules.
            state.setdefault('history',[]).append({'invalidated_at':now(),'from_stage':args.stage,'stages':state['stages']})
            state['stages']=state['stages'][:names.index(args.stage)];save(path,state)
            print('Invalidated requested stage and all dependent stages')
        else:
            errors=validate(read_json(path),config,root,run)
            print(json.dumps({'status':'fail' if errors else 'pass','errors':errors},ensure_ascii=False,indent=2))
            return 1 if errors else 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(json.dumps({'status':'fail','error':str(exc)},ensure_ascii=False));return 1
    return 0

if __name__=='__main__': raise SystemExit(main())
