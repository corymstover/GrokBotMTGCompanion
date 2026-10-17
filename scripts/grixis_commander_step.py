#!/usr/bin/env python3
"""Step D integration/closure checker with explicit frozen-local-cache pending semantics."""
from __future__ import annotations
import argparse,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent; S=ROOT/"scripts"; REG=ROOT/"data/grixis/registry.json"
CF=ROOT/"data/grixis/commander_counterfactual"; MARG=ROOT/"data/grixis/commander_marginal"

def run(script):
    p=subprocess.run([sys.executable,str(S/script),"--check"],cwd=ROOT,capture_output=True,text=True)
    return p.returncode,(p.stdout+p.stderr).strip().splitlines()
def count(folder): return len([p for p in folder.glob("*.json") if p.name!="summary.json"]) if folder.exists() else 0

def check():
    expected=len(json.loads(REG.read_text(encoding="utf-8"))["decks"]); problems=[]
    checks=[]
    for name,script in (("commander-structure","grixis_commander_structure.py"),("commander-counterfactual","grixis_commander_counterfactual.py"),("commander-marginal","grixis_commander_marginal.py"),("commander-marginal-gain","grixis_commander_marginal_gain.py")):
        rc,out=run(script); checks.append((name,rc,out[-2:] if out else []));
        if rc: problems.append(f"{name} checker failed")
    c=count(CF); m=count(MARG)
    if c not in (0,expected): problems.append(f"counterfactual partial population {c}/{expected}")
    if m not in (0,expected): problems.append(f"marginal partial population {m}/{expected}")
    if c==0 and m!=0: problems.append("marginal records exist before counterfactual population")
    if c==expected and m!=expected: problems.append("counterfactual population complete but marginal integration population missing")
    print("commander-step:")
    for name,rc,out in checks:
        print(f"  {name}: {'PASS' if rc==0 else 'FAIL'}")
        for line in out: print(f"    {line}")
    if not problems:
        if c==expected and m==expected: print("commander-step: Step D fully generated and validated")
        else: print("commander-step: code/structural layers validated; dynamic 62-deck generation remains a frozen-local-cache closure item")
    for p in problems: print("FAIL",p)
    return 1 if problems else 0

def main(argv=None):
    a=argparse.ArgumentParser(); a.add_argument("--check",action="store_true"); x=a.parse_args(argv)
    if x.check: return check()
    a.print_help(); return 0
if __name__=="__main__": sys.exit(main())
