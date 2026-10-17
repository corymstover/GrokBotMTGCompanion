#!/usr/bin/env python3
"""Step H batch 71.3: immutable review-obligation manifest derived from the frozen sampler.

This is a queue contract, not a review author. Scripts may select work, but they may not write strategic judgment,
approve/reject swaps, or satisfy Cory-only approval. Actual review records are separate future artifacts.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
POLICY=ROOT/"data/grixis/human_sampling_policy.json"
FREEZE=ROOT/"data/grixis/human_sampling_freeze.json"
SAMPLE=ROOT/"data/grixis/human_sampling_manifest.json"
OUT=ROOT/"data/grixis/human_review_manifest.json"
SCHEMA=ROOT/"data/grixis/schemas/human_review_manifest.schema.json"
VERSION=1


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def dump(p,o): Path(p).write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")
def sha(p): return "sha256:"+hashlib.sha256(Path(p).read_bytes()).hexdigest()


def build_manifest():
    policy=load(POLICY); freeze=load(FREEZE); sample=load(SAMPLE)
    if sha(POLICY)!=freeze["policy_sha256"]: raise RuntimeError("sampling policy hash drift")
    if sample["policy_sha256"]!=freeze["policy_sha256"]: raise RuntimeError("sampling manifest policy hash mismatch")
    selected={}
    for st in sample["strata"]:
        if st["timing"]!="pre_m6_static": continue
        for row in st["selected"]:
            selected.setdefault(row["slug"],{})[st["id"]]=row["selection_inputs"]
    queue=[]
    for row in sample["deduped_static_workload"]:
        slug=row["slug"]; memberships=sorted(row["memberships"])
        if set(memberships)!=set(selected.get(slug,{})): raise RuntimeError(f"{slug}: membership/input mismatch")
        queue.append({
            "review_id":f"human-sample-v1:{slug}",
            "slug":slug,
            "memberships":memberships,
            "selection_inputs":{k:selected[slug][k] for k in memberships},
            "review_requirement":{
                "status":"pending",
                "allowed_methods":["human","agent_judgment"],
                "script_may_author":False,
                "requires_commander_first_context":True,
                "requires_evidence_classes":["fact","test_result","strategic_judgment"],
                "result_record":None
            }
        })
    dyn={}
    for sid in ("high_optimizer_disagreement","major_change"):
        hook=sample["dynamic_hooks"][sid]
        dyn[sid]={
            "status":"awaiting_future_inputs",
            "selector_function":hook["function"],
            "required_fields":hook["required_fields"],
            "entries":[]
        }
    return {
        "schema_version":1,
        "status":"pre_m6_review_obligations_frozen",
        "generated_by":f"scripts/grixis_human_review_manifest.py v{VERSION}",
        "policy_sha256":freeze["policy_sha256"],
        "sampling_manifest_sha256":sha(SAMPLE),
        "authority":{
            "can_decide":False,
            "script_may_author_judgment":False,
            "human_only_acceptance":True,
            "note":"This manifest creates review obligations only. It cannot approve, reject, lock, or decide a deck change."
        },
        "static_review_queue":queue,
        "dynamic_review_queues":dyn,
        "review_contract":{
            "sampling_is_minimum_not_maximum":True,
            "overlap_memberships_preserved":True,
            "unsampled_is_not_certified":True,
            "actual_review_record_is_separate":True
        },
        "limitations":[
            "Queue membership is not negative evidence about a deck.",
            "A pending queue item is not a failed review.",
            "Scripts may not fill strategic analysis or judgment fields on behalf of a reviewer.",
            "Dynamic queues stay empty until the pre-registered M6-stage inputs exist.",
            "Cory may require additional review beyond this minimum queue."
        ]
    }


def build():
    d=build_manifest(); dump(OUT,d)
    print(f"human-review-manifest: static={len(d['static_review_queue'])}; dynamic=0+0; policy={d['policy_sha256']}")


def check():
    try: import jsonschema
    except ImportError:
        print("human-review-manifest: jsonschema required"); return 1
    probs=[]
    if not OUT.exists(): probs.append("review manifest missing")
    else:
        d=load(OUT)
        for e in jsonschema.Draft202012Validator(load(SCHEMA)).iter_errors(d):
            probs.append(f"schema {list(e.path)}: {e.message}")
        try: expected=build_manifest()
        except Exception as e:
            probs.append(f"cannot replay review manifest: {type(e).__name__}: {e}"); expected=None
        if expected is not None and d!=expected: probs.append("review manifest differs from deterministic replay")
        slugs=[x["slug"] for x in d.get("static_review_queue",[])]
        if len(slugs)!=len(set(slugs)): probs.append("duplicate static review slug")
        for x in d.get("static_review_queue",[]):
            r=x["review_requirement"]
            if r["status"]!="pending" or r["script_may_author"] is not False or r["result_record"] is not None:
                probs.append(f"{x['slug']}: generated queue item became review-authored")
        for sid,q in d.get("dynamic_review_queues",{}).items():
            if q["status"]!="awaiting_future_inputs" or q["entries"]:
                probs.append(f"{sid}: dynamic queue populated before M6 inputs")
        if d.get("authority",{}).get("can_decide") is not False or d.get("authority",{}).get("script_may_author_judgment") is not False:
            probs.append("review manifest became decision/judgment capable")
    print(f"human-review-manifest: {len(probs)} problems")
    for p in probs: print("FAIL",p)
    return 1 if probs else 0


def main(argv=None):
    a=argparse.ArgumentParser(); a.add_argument("--build",action="store_true"); a.add_argument("--check",action="store_true")
    x=a.parse_args(argv); rc=0
    if x.build: build()
    if x.check: rc|=check()
    if not (x.build or x.check): a.print_help()
    return rc
if __name__=="__main__": sys.exit(main())
