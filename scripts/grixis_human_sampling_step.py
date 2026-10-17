#!/usr/bin/env python3
"""Step H integration/closure checker.

Step H freezes sampling policy/formulas before M6, deterministically selects the static minimum review workload, and
freezes a non-deciding review-obligation manifest. Pending human/agent reviews are future M6 obligations, not failures.
"""
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
S=ROOT/"scripts"
POLICY=ROOT/"data/grixis/human_sampling_policy.json"
FREEZE=ROOT/"data/grixis/human_sampling_freeze.json"
SAMPLE=ROOT/"data/grixis/human_sampling_manifest.json"
REVIEW=ROOT/"data/grixis/human_review_manifest.json"
GAIN=ROOT/"data/grixis/human_sampling_gain.json"


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def run(script):
    p=subprocess.run([sys.executable,str(S/script),"--check"],cwd=ROOT,capture_output=True,text=True)
    return p.returncode,(p.stdout+p.stderr).strip().splitlines()


def check():
    probs=[]; checks=[]
    for name,script in (
        ("policy-freeze","grixis_human_sampling_policy.py"),
        ("sampler","grixis_human_sampling.py"),
        ("review-obligations","grixis_human_review_manifest.py"),
        ("gain","grixis_human_sampling_gain.py"),
    ):
        rc,out=run(script); checks.append((name,rc,out[-2:] if out else []))
        if rc: probs.append(f"{name} checker failed")
    required=(POLICY,FREEZE,SAMPLE,REVIEW,GAIN)
    for p in required:
        if not p.exists(): probs.append(f"missing {p.relative_to(ROOT)}")
    if not probs:
        freeze=load(FREEZE); sample=load(SAMPLE); review=load(REVIEW); gain=load(GAIN)
        if freeze.get("frozen_before_m6_outputs") is not True or freeze.get("m6_status_at_freeze")!="not_started":
            probs.append("sampling policy was not demonstrably frozen before M6")
        ph=freeze["policy_sha256"]
        if sample.get("policy_sha256")!=ph or review.get("policy_sha256")!=ph:
            probs.append("policy hash mismatch across Step H artifacts")
        expected=len(sample.get("deduped_static_workload",[]))
        actual=len(review.get("static_review_queue",[]))
        if actual!=expected or actual<=0: probs.append(f"static review queue {actual}, expected {expected}")
        if gain.get("after",{}).get("unique_static_decks_selected")!=actual:
            probs.append("gain proof unique workload disagrees with review queue")
        dyn=review.get("dynamic_review_queues",{})
        if set(dyn)!={"high_optimizer_disagreement","major_change"}:
            probs.append("dynamic review queue set mismatch")
        elif any(q.get("status")!="awaiting_future_inputs" or q.get("entries") for q in dyn.values()):
            probs.append("dynamic review queues populated before their M6-stage inputs")
        if review.get("authority",{}).get("can_decide") is not False or review.get("authority",{}).get("script_may_author_judgment") is not False:
            probs.append("review queue became decision/judgment capable")
        if gain.get("authority",{}).get("can_decide") is not False:
            probs.append("gain proof became decision-capable")
    print("human-sampling-step:")
    for name,rc,out in checks:
        print(f"  {name}: {'PASS' if rc==0 else 'FAIL'}")
        for line in out: print("   ",line)
    if not probs:
        print(f"  static minimum review workload: {len(load(REVIEW)['static_review_queue'])} unique decks")
        print("  dynamic strata: preregistered and intentionally awaiting M6-stage inputs")
        print("human-sampling-step: infrastructure complete; actual strategic reviews remain future non-scripted obligations")
    for p in probs: print("FAIL",p)
    return 1 if probs else 0


def main(argv=None):
    a=argparse.ArgumentParser(); a.add_argument("--check",action="store_true"); x=a.parse_args(argv)
    if x.check: return check()
    a.print_help(); return 0
if __name__=="__main__": sys.exit(main())
