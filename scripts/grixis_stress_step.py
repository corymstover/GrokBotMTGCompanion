#!/usr/bin/env python3
"""Step F integration/closure checker.

Infrastructure closure is cache-independent. Deck-level execution of Step-E mechanic items remains an explicit local
closure item, while red-team prompts intentionally remain pending for later real judgment and are not treated as test
failures. Partial/missing 62-deck infrastructure is always an error.
"""
from __future__ import annotations
import argparse,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent; S=ROOT/'scripts'; REG=ROOT/'data/grixis/registry.json'; SUITES=ROOT/'data/grixis/bracket_stress'; ROUTED=ROOT/'data/grixis/bracket_stress_packets'; RED=ROOT/'data/grixis/bracket_red_team'

def run(script):
 p=subprocess.run([sys.executable,str(S/script),'--check'],cwd=ROOT,capture_output=True,text=True)
 return p.returncode,(p.stdout+p.stderr).strip().splitlines()
def count(d): return len([p for p in Path(d).glob('*.json') if p.name!='summary.json']) if Path(d).exists() else 0

def check():
 expected=len(json.loads(REG.read_text(encoding='utf-8'))['decks']); probs=[]; checks=[]
 for name,script in (('suite','grixis_bracket_stress.py'),('routing','grixis_bracket_stress_runner.py'),('red-team','grixis_bracket_red_team.py'),('gain','grixis_bracket_stress_gain.py')):
  rc,out=run(script); checks.append((name,rc,out[-2:] if out else []));
  if rc: probs.append(f'{name} checker failed')
 for name,d in (('suite',SUITES),('routing',ROUTED),('red-team',RED)):
  n=count(d)
  if n!=expected: probs.append(f'{name} population {n}/{expected}')
 module_pending=judgment_pending=0
 if count(ROUTED)==expected:
  for p in [p for p in ROUTED.glob('*.json') if p.name!='summary.json']:
   d=json.loads(p.read_text())
   for x in d['items']:
    module_pending += x['evidence']['status']=='pending_deck_level_module_execution'
    judgment_pending += x['evidence']['status']=='judgment_required'
 print('bracket-stress-step:')
 for name,rc,out in checks:
  print(f"  {name}: {'PASS' if rc==0 else 'FAIL'}")
  for line in out: print('   ',line)
 print(f'  module items pending local deck-level execution: {module_pending}')
 print(f'  judgment items intentionally pending real review: {judgment_pending}')
 if not probs:
  if module_pending: print('bracket-stress-step: code/infrastructure complete; Step-E deck-level mechanic execution remains local closure item')
  else: print('bracket-stress-step: infrastructure and module execution routed with no pending module items')
 for p in probs: print('FAIL',p)
 return 1 if probs else 0

def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--check',action='store_true'); x=a.parse_args(argv)
 if x.check: return check()
 a.print_help(); return 0
if __name__=='__main__': sys.exit(main())
