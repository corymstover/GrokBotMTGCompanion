#!/usr/bin/env python3
"""Registered Abaddon Chrome Mox vs Grinding Station M3 mana test. Not deck approval."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_authority as ga
import grixis_paired as pair
import grixis_sim as sim
import evaluate_decklist as ev

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_chrome_mox_pair_01.json"
PACKET=ROOT/"data/grixis/m6/review_packets/abaddon-the-despoiler.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_mana_pair_chrome_mox.json"

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

def sha(p):
    return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()

def encode(obj):
    return json.dumps(obj,sort_keys=True,indent=1,ensure_ascii=False)+"\n"

def build_record():
    p=load(PLAN);packet=load(PACKET);reg=load(ga.REGISTRY)
    assert p["status"]=="registered_not_run" and p["model"]==sim.VERSION=="1.1"
    assert packet["list_hash"]==p["baseline_hash"]
    assert reg["program"]["milestones"]["M5"]["status"]=="accepted"
    assert reg["program"]["milestones"]["M6"]["accepted_by"] is None
    hits=[x for x in packet["items"] if x["swap_id"]==p["swap_id"]]
    assert len(hits)==1 and (hits[0]["cut"],hits[0]["add"])==(p["cut"],p["add"])
    lines=ga.deck_block_text(p["slug"]).splitlines()
    idx=[i for i,l in enumerate(lines) if l.split(" ",1)[-1].split(" [")[0].strip()==p["cut"]]
    assert len(idx)==1
    lines[idx[0]]="1 "+p["add"]
    R=ev.Resolver()
    a=sim.load_deck(p["slug"],R)
    b=sim.load_deck(p["slug"],R,text="\n".join(lines)+"\n")
    assert a.N==b.N==99
    scores,pairs=pair.paired(a,b,p["samples"],p["seed"],turns=p["turns"],
                            pairs=[(p["cut"],p["add"])],model=p["model"])
    assert pairs==[(p["cut"],p["add"])]
    selected=[next(r for r in scores if r["metric"]==metric) for metric in p["endpoints"]]
    coverage=pair.coverage(a,b,pairs,p["model"])
    assert "Grinding Station [no effect modelled beyond being a castable card]" in coverage[0]
    return {"schema_version":1,"stage":"M6_partial_mana_paired_test",
       "deck_id":p["deck_id"],"slug":p["slug"],"base_hash":p["baseline_hash"],
       "preregistration_sha256":sha(PLAN),"m5_packet_sha256":sha(PACKET),
       "swap_id":p["swap_id"],"cut":p["cut"],"add":p["add"],
       "samples":p["samples"],"seed":p["seed"],"model":p["model"],
       "model_sha256":sim.model_sha256(),"results":selected,
       "coverage":coverage,"limitations":p["coverage_omissions"],
       "supports_improvement_claim":False,"phase_b_complete":False,
       "authority":{"can_decide":False,"can_apply_swap":False,"can_approve_or_lock":False}}

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--build",action="store_true")
    ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    if not(args.build or args.check):ap.error("choose --build/--check")
    r=build_record()
    if args.build:
        OUT.parent.mkdir(parents=True,exist_ok=True)
        OUT.write_text(encode(r),encoding="utf-8")
    if args.check and OUT.read_text(encoding="utf-8")!=encode(r):
        raise ValueError("mana result drift")
    print(encode({"samples":r["samples"],"results":r["results"],
                  "supports_improvement_claim":False,"phase_b_complete":False}))
