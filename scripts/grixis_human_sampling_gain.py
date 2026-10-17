#!/usr/bin/env python3
"""Step H batch 71.3: before/after human-oversight gain proof.

This measures review-coverage and preregistration gain, not deck strength or model accuracy.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
SAMPLE=ROOT/"data/grixis/human_sampling_manifest.json"
REVIEW=ROOT/"data/grixis/human_review_manifest.json"
OUT=ROOT/"data/grixis/human_sampling_gain.json"
SCHEMA=ROOT/"data/grixis/schemas/human_sampling_gain.schema.json"
VERSION=1


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def dump(p,o): Path(p).write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")


def build_gain():
    s=load(SAMPLE); r=load(REVIEW)
    per={x["id"]:x["selected_count"] for x in s["strata"]}
    examples=sorted(r["static_review_queue"],key=lambda x:(-len(x["memberships"]),x["slug"]))[:8]
    return {
      "schema_version":1,
      "generated_by":f"scripts/grixis_human_sampling_gain.py v{VERSION}",
      "evidence_class":"derived_metric",
      "authority":{"can_decide":False,"note":"Oversight-coverage gain is not a deck-quality score and cannot decide a swap."},
      "baseline":{
        "stage":"before Step H",
        "deterministic_policy_frozen":False,
        "minimum_static_review_workload":0,
        "result_dependent_formulas_preregistered":False,
        "all_project_exceptions_mandatory":False,
        "all_pending_release_mandatory":False
      },
      "after":{
        "policy_frozen_before_m6":True,
        "static_strata":7,
        "dynamic_strata_preregistered":2,
        "unique_static_decks_selected":len(r["static_review_queue"]),
        "per_stratum_selected":per,
        "all_exception_eligible_selected":per.get("exception",0),
        "all_pending_release_eligible_selected":per.get("pending_release",0),
        "review_queue_items_pending":sum(x["review_requirement"]["status"]=="pending" for x in r["static_review_queue"]),
        "scripts_can_author_judgment":False
      },
      "real_deck_examples":[{"slug":x["slug"],"memberships":x["memberships"]} for x in examples],
      "gain_claims":[
        f"Pre-M6 oversight changes from no preregistered minimum sample to {len(r['static_review_queue'])} unique static deck reviews across seven frozen strata.",
        f"All {per.get('exception',0)} project-exception/authorization decks and all {per.get('pending_release',0)} pending-release decks are mandatory rather than sampled away.",
        "Random sampling supplies an unbiased defect-detection stratum while anomaly, cEDH, commander-dependence and rules-sensitive strata target known risk classes.",
        "Optimizer-disagreement and major-change selection formulas are executable and frozen before those results exist, preventing result-aware cherry-picking."
      ],
      "limitations":[
        "More review coverage is not proof that deck decisions are correct.",
        "Overlap means per-stratum counts must not be summed as unique decks.",
        "Dynamic strata have no selected decks until their M6-stage inputs exist.",
        "Unsampled decks are not certified by omission.",
        "The gain proof measures process/oversight improvement, not multiplayer win rate or power."
      ]
    }


def build():
    d=build_gain(); dump(OUT,d)
    print(f"human-sampling-gain: unique={d['after']['unique_static_decks_selected']}; dynamic_preregistered={d['after']['dynamic_strata_preregistered']}")


def check():
    try: import jsonschema
    except ImportError: print("human-sampling-gain: jsonschema required"); return 1
    probs=[]
    if not OUT.exists(): probs.append("gain proof missing")
    else:
        d=load(OUT)
        for e in jsonschema.Draft202012Validator(load(SCHEMA)).iter_errors(d): probs.append(f"schema {list(e.path)}: {e.message}")
        try: expected=build_gain()
        except Exception as e: probs.append(f"cannot replay gain proof: {type(e).__name__}: {e}"); expected=None
        if expected is not None and d!=expected: probs.append("gain proof differs from deterministic replay")
        if d.get("authority",{}).get("can_decide") is not False: probs.append("gain proof became decision-capable")
        if d.get("after",{}).get("scripts_can_author_judgment") is not False: probs.append("gain proof says scripts may author judgment")
        if d.get("after",{}).get("unique_static_decks_selected",0)<=0: probs.append("no demonstrated static oversight gain")
    print(f"human-sampling-gain: {len(probs)} problems")
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
