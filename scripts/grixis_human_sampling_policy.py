#!/usr/bin/env python3
"""Freeze/check the Step H human-quality sampling policy before any M6 outputs exist."""
from __future__ import annotations
import argparse,hashlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
POLICY=ROOT/'data/grixis/human_sampling_policy.json'; FREEZE=ROOT/'data/grixis/human_sampling_freeze.json'; P_SCHEMA=ROOT/'data/grixis/schemas/human_sampling_policy.schema.json'; F_SCHEMA=ROOT/'data/grixis/schemas/human_sampling_freeze.schema.json'; REG=ROOT/'data/grixis/registry.json'
IDS={'random','anomaly','exception','pending_release','cedh','low_commander_dependence','rules_sensitive','high_optimizer_disagreement','major_change'}

def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def digest(): return 'sha256:'+hashlib.sha256(POLICY.read_bytes()).hexdigest()
def m6_status(): return load(REG)['program']['milestones']['M6']['status']

def freeze(basis=None):
 if m6_status()!='not_started': raise SystemExit('refuse to freeze H policy after M6 started')
 p=load(POLICY); basis=basis or os.environ.get('GITHUB_SHA') or 'unknown-pre-M6-basis'
 d={'schema_version':1,'policy_path':'data/grixis/human_sampling_policy.json','policy_sha256':digest(),'seed':p['seed'],'frozen_before_m6_outputs':True,'m6_status_at_freeze':'not_started','basis_commit':basis,'authority':{'can_decide':False,'requires_cory_to_supersede':True},'note':'v1 policy hash frozen before M6 outputs. Later mutation requires an explicit superseding version approved by Cory; do not overwrite this record in place.'}
 FREEZE.write_text(json.dumps(d,indent=1,sort_keys=True)+'\n',encoding='utf-8'); print(d['policy_sha256'])

def check():
 try: import jsonschema
 except ImportError: print('human-sampling-policy: jsonschema required'); return 1
 probs=[]; p=load(POLICY)
 for e in jsonschema.Draft202012Validator(load(P_SCHEMA)).iter_errors(p): probs.append(f'policy schema {list(e.path)}: {e.message}')
 ids=[x['id'] for x in p['strata']]
 if set(ids)!=IDS or len(ids)!=len(set(ids)): probs.append(f'strata set/uniqueness invalid: {ids}')
 if not FREEZE.exists(): probs.append('freeze record missing')
 else:
  f=load(FREEZE)
  for e in jsonschema.Draft202012Validator(load(F_SCHEMA)).iter_errors(f): probs.append(f'freeze schema {list(e.path)}: {e.message}')
  if f.get('policy_sha256')!=digest(): probs.append(f"policy hash drift: freeze={f.get('policy_sha256')} actual={digest()}")
  if f.get('seed')!=p.get('seed'): probs.append('seed drift between policy and freeze')
 if p['authority']['can_decide'] is not False or p['review_output_requirement']['script_may_author_judgment'] is not False: probs.append('policy became decision/judgment capable')
 dyn={x['id']:x for x in p['strata'] if x['timing']!='pre_m6_static'}
 if set(dyn)!={'high_optimizer_disagreement','major_change'}: probs.append('future-result strata timing changed')
 print(f'human-sampling-policy: {len(probs)} problems; policy={digest()}')
 for x in probs: print('FAIL',x)
 return 1 if probs else 0

def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--freeze',action='store_true'); a.add_argument('--check',action='store_true'); a.add_argument('--basis-commit'); x=a.parse_args(argv); rc=0
 if x.freeze: freeze(x.basis_commit)
 if x.check: rc|=check()
 if not (x.freeze or x.check): a.print_help()
 return rc
if __name__=='__main__': sys.exit(main())
