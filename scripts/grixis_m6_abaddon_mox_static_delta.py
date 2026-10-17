#!/usr/bin/env python3
"""One-deck, read-only corrected Step C static classification delta."""
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_mana_base as mb
OUT=ROOT/"data/grixis/m6/classifier_corrections/abaddon_static_delta.json"
def load(p):return json.loads(p.read_text(encoding="utf-8"))
def hashp(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def enc(d):return json.dumps(d,indent=1,sort_keys=True,ensure_ascii=False)+"\n"
def derive():
    reg=load(ROOT/"data/grixis/registry.json")
    rid,entry=next((k,v) for k,v in reg["decks"].items() if v["slug"]=="abaddon-the-despoiler")
    oldpath=ROOT/"data/grixis/mana_base/abaddon-the-despoiler.json"
    old=load(oldpath)
    new=mb.build_one(rid,entry,mb.CardDB())
    assert old["canonical_hash"]==new["canonical_hash"]==entry["canonical_project_list"]["hash"]
    assert old["counts"]["lands"]==new["counts"]["lands"]==34
    assert new["counts"]["fast_mana"]==old["counts"]["fast_mana"]+1
    assert new["counts"]["repeatable_nonland_sources"]==old["counts"]["repeatable_nonland_sources"]+1
    assert "Chrome Mox" not in old["fast_mana_cards"] and "Chrome Mox" in new["fast_mana_cards"]
    assert new["colored_sources"]["land_sources"]==old["colored_sources"]["land_sources"]
    a=old["colored_sources"]["land_plus_repeatable_nonland"]
    b=new["colored_sources"]["land_plus_repeatable_nonland"]
    assert all(b[c]==a[c]+1 for c in "UBR")
    return {"schema_version":1,"stage":"M6_Abaddon_conditional_Chrome_Mox_static_delta",
      "deck_id":rid,"slug":entry["slug"],"list_hash":old["canonical_hash"],
      "frozen_step_c_sha256":hashp(oldpath),"corrected_classifier_sha256":hashp(ROOT/"scripts/grixis_mana_base.py"),
      "metrics":{"fast_mana_inventory":{"frozen":old["counts"]["fast_mana"],"corrected":new["counts"]["fast_mana"]},
         "repeatable_nonland_sources":{"frozen":old["counts"]["repeatable_nonland_sources"],"corrected":new["counts"]["repeatable_nonland_sources"]},
         "land_plus_repeatable_potential_colors":{"frozen":a,"corrected":b},
         "lands":{"frozen":old["counts"]["lands"],"corrected":new["counts"]["lands"]}},
      "newly_recognized":"Chrome Mox, conditional imprint-linked zero-mana artifact",
      "color_probability_claim":False,"commander_cast_probability_recomputed":False,
      "legacy_commander_mana_report_recomputed":False,
      "downstream_actions":["Do not infer an automatic one-turn improvement from inventory count changes",
         "Recompute conditional source availability with actual imprint resources before replacing historical commander mana records",
         "Retain Cycle 84 exact one-card paired Chrome Mox comparison as separate simulator evidence"],
      "status":"corrected_static_only_downstream_pending",
      "authority":{"can_decide":False,"can_apply_swap":False,"can_approve_or_lock":False}}
def main():
    p=argparse.ArgumentParser();p.add_argument("--build",action="store_true");p.add_argument("--check",action="store_true");a=p.parse_args()
    if not(a.build or a.check):p.error("need build or check")
    d=derive()
    if a.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(enc(d))
    if a.check and (not OUT.is_file() or OUT.read_text()!=enc(d)):raise ValueError("Abaddon static delta drift")
    print(json.dumps(d["metrics"],sort_keys=True))
if __name__=="__main__":main()
