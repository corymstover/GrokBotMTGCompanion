#!/usr/bin/env python3
"""Cycle 88: rederive ONLY 25 affected Step C static mana files, in a separate M6 namespace.

Never rewrite historical Step C, M5 accepted evidence, or user-approved decks.
Conditional Chrome Mox counts potential mana colors, not assured availability.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_mana_base as mb

REG=ROOT/"data/grixis/registry.json"
AUDIT=ROOT/"data/grixis/m6/classifier_corrections/chrome_mox.json"
OUT=ROOT/"data/grixis/m6/mox_reconciliation/static"
MANIFEST=ROOT/"data/grixis/m6/mox_reconciliation/static_manifest.json"
AUTH={"can_decide":False,"can_apply_swap":False,"can_approve_or_lock":False}

def load(p):return json.loads(p.read_text(encoding="utf-8"))
def serialize(o):return json.dumps(o,indent=1,ensure_ascii=False,sort_keys=True)+"\n"
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()

def build_rows():
    reg,audit=load(REG),load(AUDIT)
    if len(reg["decks"])!=62 or audit["affected_count"]!=25:
        raise ValueError("registry/affected inventory drift")
    if reg["program"]["milestones"]["M5"]["status"]!="accepted" or reg["program"]["milestones"]["M6"].get("accepted_by") is not None:
        raise ValueError("M5/M6 authority mismatch")
    byslug={v["slug"]:(k,v) for k,v in reg["decks"].items()}
    db=mb.CardDB()
    rows=[]
    for item in sorted(audit["affected_decks"],key=lambda x:x["slug"]):
        slug=item["slug"]
        did,entry=byslug[slug]
        oldp=ROOT/"data/grixis/mana_base"/(slug+".json")
        frozen=load(oldp)
        corrected=mb.build_one(did,entry,db)
        if frozen["canonical_hash"]!=corrected["canonical_hash"]!=entry["canonical_project_list"]["hash"]:
            raise ValueError(slug+": canonical hash mismatch")
        if corrected["canonical_hash"]!=entry["canonical_project_list"]["hash"]:
            raise ValueError(slug+": current hash mismatch")
        if item["frozen_step_c_sha256"]!=sha(oldp):
            raise ValueError(slug+": frozen Step C checksum drift")
        if "Chrome Mox" in frozen["fast_mana_cards"] or corrected["fast_mana_cards"].count("Chrome Mox")!=1:
            raise ValueError(slug+": Chrome Mox classification not corrected")
        if corrected["counts"]["fast_mana"]!=frozen["counts"]["fast_mana"]+1:
            raise ValueError(slug+": unexpected fast-mana change")
        if corrected["counts"]["repeatable_nonland_sources"]!=frozen["counts"]["repeatable_nonland_sources"]+1:
            raise ValueError(slug+": unexpected repeatable-source change")
        if corrected["colored_sources"]["land_sources"]!=frozen["colored_sources"]["land_sources"]:
            raise ValueError(slug+": land-source drift")
        for color in "UBR":
            p0=frozen["colored_sources"]["land_plus_repeatable_nonland"][color]
            p1=corrected["colored_sources"]["land_plus_repeatable_nonland"][color]
            if p1!=p0+1:
                raise ValueError(slug+": unexpected potential "+color+" source change")
        # Only five values may change, as explicitly justified by Chrome Mox
        import copy
        normalized=copy.deepcopy(corrected)
        normalized["counts"]["fast_mana"]-=1
        normalized["counts"]["repeatable_nonland_sources"]-=1
        for c in "UBR":normalized["colored_sources"]["land_plus_repeatable_nonland"][c]-=1
        normalized["fast_mana_cards"].remove("Chrome Mox")
        if normalized!=frozen:
            def walk_diff(x,y,path=""):
                if isinstance(x,dict) and isinstance(y,dict):
                    keys=set(x)|set(y)
                    return [z for k in sorted(keys) for z in walk_diff(x.get(k),y.get(k),path+"."+k)]
                return [] if x==y else [path]
            raise ValueError(slug+": unintended fields differ: "+repr(walk_diff(normalized,frozen)[:12]))
        if corrected["authority"]["can_decide"] or corrected["unresolved_cards"]:
            raise ValueError(slug+": authority or unresolved drift")
        if corrected["counts"]["lands"]!=frozen["counts"]["lands"]:
            raise ValueError(slug+": land count drift")
        rows.append((slug,did,oldp,corrected,entry))
    return rows

def build(check,write):
    rows=build_rows()
    if write:OUT.mkdir(parents=True,exist_ok=True)
    summaries=[]
    for slug,did,oldp,corrected,entry in rows:
        out=OUT/(slug+".json")
        payload=serialize(corrected)
        if write:out.write_text(payload,encoding="utf-8")
        if check and (not out.is_file() or out.read_text(encoding="utf-8")!=payload):
            raise ValueError(slug+": missing or stale corrected static report")
        summaries.append({
            "deck_id":did,"slug":slug,"canonical_hash":corrected["canonical_hash"],
            "old_sha256":sha(oldp),
            "corrected_sha256":"sha256:"+hashlib.sha256(payload.encode("utf-8")).hexdigest(),
            "old_fast_mana":corrected["counts"]["fast_mana"]-1,
            "corrected_fast_mana":corrected["counts"]["fast_mana"],
            "new_source":"Chrome Mox; conditional imprint-dependent potential UBR",
            "simulator_impact":"requires separate sampled no-fast counterfactual; not measured here",
        })
    manifest={"schema_version":1,"stage":"M6_25_deck_conditional_mox_static_reconciliation",
        "registry_sha256":sha(REG),"audit_sha256":sha(AUDIT),
        "classifier_sha256":sha(ROOT/"scripts/grixis_mana_base.py"),
        "count":len(summaries),"rows":summaries,
        "expected_changes":"Each report differs from frozen Step C ONLY in fast-mana inventory +1, repeatable nonland count +1, and U/B/R potential source counts +1",
        "limitations":["Potential colored sources require valid Chrome Mox imprint and are not guaranteed color access",
            "Commander casting probabilities have not been recomputed",
            "Original Step C files and commander_mana artifacts remain frozen",
            "This reconciles structural classification only; it does not approve a deck swap or M6"],
        "authority":AUTH}
    if manifest["count"]!=25:raise ValueError("affected report count not 25")
    body=serialize(manifest)
    if write:MANIFEST.write_text(body,encoding="utf-8")
    if check and (not MANIFEST.is_file() or MANIFEST.read_text(encoding="utf-8")!=body):
        raise ValueError("static manifest drift")
    if check and {p.stem for p in OUT.glob("*.json")}!={s for s,*_ in rows}:
        raise ValueError("unexpected/missing static files")
    print("Cycle 88 corrected Step C static snapshots:",len(rows),"/25; commander-mana counterfactuals pending")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--build",action="store_true")
    ap.add_argument("--check",action="store_true")
    a=ap.parse_args()
    if not (a.build or a.check):ap.error("require --build or --check")
    build(a.check,a.build)
