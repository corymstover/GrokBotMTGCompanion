#!/usr/bin/env python3
"""Step C integration/closure checker.

The cache-independent layers must all cover 62 canonical decks and remain non-deciding. Commander-mana (68.3) is a
separate local-cache closure item: zero generated deck records is an explicit pending state; 1..61 is an error; 62 is
validated normally. This lets CI enforce everything it can see without falsely claiming Step C complete.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
S=ROOT/"scripts"
CM=ROOT/"data/grixis/commander_mana"
REG=ROOT/"data/grixis/registry.json"

CACHE_INDEPENDENT=[
 ("mana-base","grixis_mana_base.py"),
 ("mana-timing","grixis_mana_timing.py"),
 ("mana-opportunity","grixis_mana_opportunity.py"),
 ("mana-resilience","grixis_mana_resilience.py"),
 ("mana-quality-gain","grixis_mana_quality_gain.py"),
]


def run_check(script):
    p=subprocess.run([sys.executable,str(S/script),"--check"],cwd=ROOT,capture_output=True,text=True)
    return p.returncode,(p.stdout+p.stderr).strip().splitlines()


def commander_state():
    expected=len(json.loads(REG.read_text(encoding="utf-8"))["decks"])
    files=[p for p in CM.glob("*.json") if p.name!="summary.json"] if CM.exists() else []
    n=len(files)
    if n==0:
        return "pending_local_cache_validation",0,expected,0,["commander-mana: 68.3 code/schema/tests exist; 62 outputs require the frozen local Scryfall cache"]
    if n!=expected:
        return "partial_invalid",n,expected,1,[f"commander-mana: partial generated population {n}/{expected}; expected either 0 pending or all {expected}"]
    rc,out=run_check("grixis_commander_mana.py")
    return ("validated" if rc==0 else "validation_failed"),n,expected,rc,out


def check():
    problems=[]; status=[]
    for name,script in CACHE_INDEPENDENT:
        rc,out=run_check(script)
        status.append((name,rc,out[-2:] if out else []))
        if rc: problems.append(f"{name} checker failed")
    cstate,n,expected,crc,cout=commander_state()
    if crc: problems.append("commander-mana closure state invalid")
    print("mana-step: cache-independent layers")
    for name,rc,out in status:
        print(f"  {name}: {'PASS' if rc==0 else 'FAIL'}")
        for line in out: print(f"    {line}")
    print(f"  commander-mana: {cstate} ({n}/{expected} generated deck records)")
    for line in cout[-3:]: print(f"    {line}")
    if cstate=="validated" and not problems:
        print("mana-step: Step C fully validated")
    elif cstate=="pending_local_cache_validation" and not problems:
        print("mana-step: code complete except declared 68.3 frozen-local-cache closure item")
    for p in problems: print("FAIL",p)
    return 1 if problems else 0


def main(argv=None):
    a=argparse.ArgumentParser(); a.add_argument("--check",action="store_true"); x=a.parse_args(argv)
    if x.check: return check()
    a.print_help(); return 0

if __name__=="__main__": sys.exit(main())
