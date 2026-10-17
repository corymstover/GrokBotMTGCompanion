#!/usr/bin/env python3
"""Cycle 89: exact-seed 25-deck correction of Step C *no-fast-mana* proxy only.

Replays frozen old package counterfactual first and refuses corrections if it
doesn't match stored evidence. A corrected counterfactual additionally disables
imprint-conditional Chrome Mox. Never overwrites historical Step C, approved
deck data, or accepted M5. No win-rate inference is possible from these proxies.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_commander_mana as gm
import grixis_sim as sim

REG=ROOT/"data/grixis/registry.json"
STATIC=ROOT/"data/grixis/m6/mox_reconciliation/static_manifest.json"
BASE=ROOT/"data/grixis/commander_mana"
NEWSTATIC=ROOT/"data/grixis/m6/mox_reconciliation/static"
OUT=ROOT/"data/grixis/m6/mox_reconciliation/nofast"
MANIFEST=ROOT/"data/grixis/m6/mox_reconciliation/nofast_manifest.json"
AUTH={"can_decide":False,"can_apply_swap":False,"can_approve_or_lock":False}

def load(p):return json.loads(p.read_text(encoding="utf-8"))
def serialize(o):return json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n"
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()

def records():
    reg,manifest=load(REG),load(STATIC)
    if len(reg["decks"])!=62 or manifest["count"]!=25 or reg["program"]["milestones"]["M5"]["status"]!="accepted" or reg["program"]["milestones"]["M6"].get("accepted_by") is not None:
        raise ValueError("registry, M5/M6 or affected inventory mismatch")
    byslug={v["slug"]:(k,v) for k,v in reg["decks"].items()}
    out=[]
    for row in manifest["rows"]:
        slug=row["slug"]
        did,entry=byslug[slug]
        oldpath=BASE/(slug+".json")
        old=load(oldpath)
        stat=load(NEWSTATIC/(slug+".json"))
        if old["canonical_hash"]!=stat["canonical_hash"] or old["canonical_hash"]!=entry["canonical_project_list"]["hash"]:
            raise ValueError(slug+": stale canonical hash")
        if stat["fast_mana_cards"].count("Chrome Mox")!=1:
            raise ValueError(slug+": corrected fast mana not in source")
        if old["method"]["simulator_sha256"]!=sim.model_sha256() or old["method"]["samples"]!=gm.SAMPLES or old["method"]["seed"]!=gm.SEED or old["method"]["turns"]!=gm.TURNS:
            raise ValueError(slug+": historical simulator/seed mismatch")
        deck=sim.load_deck(slug)
        perms=gm.permutations(deck)
        old_comms={c["commander"]:c for c in old["commanders"]}
        results=[]
        for c in deck.commanders:
            name=c["name"]
            if name not in old_comms:raise ValueError(slug+": commander identity mismatch")
            orig=old_comms[name]
            historical_names=set(orig["fast_mana_inventory"])
            corrected_names=set(stat["fast_mana_cards"])
            if corrected_names!=historical_names|{"Chrome Mox"}:
                raise ValueError(slug+": unexpected package difference")
            d=gm.isolate_commander(deck,name)
            was=gm.run_scenario(gm.disable_fast_mana(d,historical_names),perms)
            old_replayed=gm.cast_summary(was)
            if old_replayed!=orig["no_fast_mana_counterfactual"]:
                raise ValueError(slug+": historical 500-seed no-fast result does not reproduce")
            now=gm.run_scenario(gm.disable_fast_mana(d,corrected_names),perms)
            corrected=gm.cast_summary(now)
            impact={str(turn):gm.paired_indicator_delta(was,now,
                lambda rec,turn=turn:rec["commander_turn"] is not None and rec["commander_turn"]<=turn)
                for turn in (2,3,4,5,6)}
            results.append({
                "commander":name,
                "historical_no_fast_sha256":"sha256:"+hashlib.sha256(serialize(old_replayed).encode()).hexdigest(),
                "historical_fast_cards":sorted(historical_names),
                "corrected_fast_cards":sorted(corrected_names),
                "old_no_fast_mana_counterfactual":old_replayed,
                "corrected_no_fast_mana_counterfactual":corrected,
                "additional_chrome_mox_disable_impact_old_minus_corrected_by_turn":impact,
                "baseline_commander_cast_probability_unchanged":orig["baseline"]["cast_by_turn"],
                "historical_fast_package_report_preserved":True,
            })
        obj={
            "schema_version":1,"stage":"M6_Chrome_Mox_corrected_paired_nofast_counterfactual",
            "deck_id":did,"slug":slug,"canonical_hash":old["canonical_hash"],
            "frozen_commander_mana_sha256":sha(oldpath),
            "corrected_static_sha256":sha(NEWSTATIC/(slug+".json")),
            "simulator_sha256":sim.model_sha256(),
            "method":{"samples":gm.SAMPLES,"seed":gm.SEED,"turns":gm.TURNS,
                      "comparator":"historical no-fast package vs same package PLUS Chrome Mox disabled",
                      "pairing":"same library permutations and seeded simulator v1.1"},
            "commanders":results,
            "status":"bounded_package_mana_evidence_no_deck_decision",
            "limitations":["This repairs a package proxy, NOT a one-card Chrome Mox replacement or multiplayer win rate",
                           "Goldfish engine simplifies imprint and availability; colored-source potential is not guaranteed",
                           "Baseline and removal/tax scenarios remain the historical unchanged reports",
                           "No model of opponents, actual stack decisions or full commander strategy",
                           "Full 62-deck research pipeline not rerun"],
            "authority":AUTH,
        }
        out.append(obj)
        print('checked historical no-fast and corrected Chrome Mox: '+slug, flush=True)
    if len(out)!=25 or len({x["slug"] for x in out})!=25:
        raise ValueError("25 deck audit incomplete")
    return out

def execute(build,check):
    all_rows=records()
    if build:OUT.mkdir(parents=True,exist_ok=True)
    brief=[]
    for obj in all_rows:
        slug=obj["slug"]
        body=serialize(obj)
        path=OUT/(slug+".json")
        if build:path.write_text(body,encoding="utf-8")
        if check and (not path.is_file() or path.read_text(encoding="utf-8")!=body):
            raise ValueError(slug+": absent or stale corrected no-fast receipt")
        brief.append({"slug":slug,"sha256":"sha256:"+hashlib.sha256(body.encode("utf-8")).hexdigest(),
                     "commander_count":len(obj["commanders"]),
                     "additional_fast_package_turn4_deltas":{
                         c["commander"]:c["additional_chrome_mox_disable_impact_old_minus_corrected_by_turn"]["4"]
                         for c in obj["commanders"]}})
    summary={
        "schema_version":1,"stage":"M6_25_deck_Chrome_Mox_corrected_nofast_manifest",
        "count":len(brief),"static_manifest_sha256":sha(STATIC),
        "simulator_sha256":sim.model_sha256(),
        "samples_per_commander":gm.SAMPLES,"seed":gm.SEED,"rows":brief,
        "original_commander_mana_artifacts_modified":False,
        "accepted_m5_or_canonical_state_modified":False,
        "scope":"Paired no-fast scenario difference from correcting Chrome Mox inventory; NOT a win-rate or approved swap",
        "authority":AUTH,
    }
    text=serialize(summary)
    if build:MANIFEST.write_text(text,encoding="utf-8")
    if check:
        if not MANIFEST.is_file() or MANIFEST.read_text(encoding="utf-8")!=text:
            raise ValueError("reproducibility manifest drift")
        if {p.stem for p in OUT.glob("*.json")}!={r["slug"] for r in brief}:
            raise ValueError("25 corrected no-fast files mismatch")
    print("corrected no-fast matched historical replay and produced",len(brief),
          "independent M6-only evidence artifacts; no approvals")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--build",action="store_true")
    ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    if not (args.build or args.check):ap.error("require --build/--check")
    execute(args.build,args.check)
