#!/usr/bin/env python3
"""Cycle131 source-locked authorship census; never independent Pass C.

29 new authored cases; 33 prior source-backed author records. Verify frozen
Oracle identity, 100 card zones including partners, companion not counted as
main, exact M5 proposed swaps, hash consistency, known source exceptions.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_authority as ga
import grixis_m6_cycle117_independent_review_readiness as cycle117
import evaluate_decklist as ev

BATCHES={x:ROOT/f"data/grixis/m6/author_reviews/cycle131_batch_{x}_01.json" for x in "abcde"}
PREV=[
 ROOT/"data/grixis/m6/author_reviews/cycle128_six_commander_authored_judgments_01.json",
 ROOT/"data/grixis/m6/author_reviews/cycle129_six_detailed_01.json",
 ROOT/"data/grixis/m6/author_reviews/cycle130_six_detailed_01.json",
]
TRI=ROOT/"data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json"
REG=ROOT/"data/grixis/registry.json"
TRACK=ROOT/"data/grixis/milestone_m6_m7_subtracker.json"
PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle131_all_remaining_authored_preregistered_01.json"
OUT=ROOT/"data/grixis/m6/independent_review_intake/cycle131_all_62_authored_handoff_receipt_01.json"
BASICS={"Plains","Island","Swamp","Mountain","Forest","Wastes","Snow-Covered Island","Snow-Covered Swamp","Snow-Covered Mountain","Snow-Covered Forest","Snow-Covered Plains"}
KNOWN_RECORD_MISMATCH={"Admiral_Brass__Unsinkable","Anhelo__the_Painter"}
SPECIAL_COMPANION="Cecily__Bjorna__Lutri"
KNOWN_PROJECT_EXCEPTIONS={
 "Cecily__Bjorna__Lutri":3,
 "Tresserhorn_s_Lord__Returned":1,
}
def read(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def digest(p):return "sha256:"+hashlib.sha256(Path(p).read_bytes()).hexdigest()
def stable(obj):return json.dumps(obj,indent=2,sort_keys=True,ensure_ascii=False)+"\n"
def existing():
    source=cycle117.source_rows()
    ids=[r["deck_id"] for r in source]
    if len(ids)!=15:raise ValueError("Cycle112–116 source coverage drift")
    for path in PREV:
        j=read(path)
        rows=j.get("rows")
        if len(rows)!=6:raise ValueError("Prior six-case source batch changed "+str(path))
        ids.extend(x["deck_id"] for x in rows)
    if len(ids)!=33 or len(set(ids))!=33:
        raise ValueError("Earlier 33 author reviews not distinct")
    return ids
def validate_row(row,queue,meta,resolver):
    did=row["deck_id"]
    if (row["slug"]!=meta["slug"] or row["commander_names"]!=meta["commanders"] or
        queue["commanders"]!=meta["commanders"] or
        row["baseline_logical_hash"]!=meta["current_canonical_hash"] or
        queue["source_canonical_logical_hash"]!=meta["current_canonical_hash"] or
        row["source_recorded_sha"]!=meta["source"]["recorded_sha256"] or
        queue["recorded_source_approved_raw_sha256"]!=meta["source"]["recorded_sha256"] or
        row["source_raw_match_recorded"]!=meta["source"]["recorded_matches_raw"] or
        row["official_snapshot_status"]!=meta["official_commander_compliance"]["status"] or
        row["project_exception_refs"]!=meta["project_exceptions"]):
        raise ValueError("Commander/source/approval hash drift for "+did)
    c=queue["first_three_TO_REVIEW_NOT_TO_APPLY"][0]
    if (row["add"],row["cut"],row["m5_swap_id"])!=(c["add"],c["cut"],c["swap_id"]):
        raise ValueError("Authored exact candidate deviated from top M5 source "+did)
    if not c["swap_id"].startswith("swap:"+meta["slug"]+":m5:"):
        raise ValueError("M5 swap ID mismatched "+did)
    bp_path=ROOT/"data/grixis/blueprints"/(meta["slug"]+".json")
    bp=read(bp_path)
    if (bp["deck_id"]!=did or bp["canonical_hash"]!=meta["current_canonical_hash"] or
        digest(bp_path)!=queue["blueprint_sha256"] or
        row["protected_identity"]!=queue["blueprint_core"][:6]):
        raise ValueError("Commander blueprint/core does not match source "+did)
    if (not row["core"] or not row["positive"] or not row["cut_cost"] or
        not row["adverse"] or not row["followup"] or len(row["rules"])<5 or
        any(not isinstance(s,str) or len(s.strip())<30 for s in row["rules"]) or
        row["decision"] not in ("HOLD_EXACT_SWAP",
              "PROMISING_BUT_NO_CHANGE_PENDING_PAID_COMBAT_TEST",
              "PROMISING_BUT_NO_CHANGE_PENDING_ACTIVATION_TEST",
              "PROMISING_BUT_NO_CHANGE_PENDING_COLOR_TEST",
              "PROMISING_BUT_NO_CHANGE_PENDING_ARTIFACT_DENSITY_TEST",
              "PROMISING_BUT_NO_CHANGE_PENDING_COUNTER_TIMING_TEST",
              "PROMISING_BUT_NO_CHANGE_PENDING_FODDER_TEST",
              "PROMISING_BUT_NO_CHANGE_PENDING_HAND_SIZE_MANA_TEST") or
        row["approved_swaps"]!=0 or row["formal_pass_c"] or row["full_phase_b"] or
        row["current_full_legality_verification"]):
        raise ValueError("Review not decision-grade authored-only case "+did)
    text=ga.deck_block_text(meta["slug"])
    entries=ga.list_entries(text,resolver)
    if ga.text_hash(text,resolver)!=meta["current_canonical_hash"]:
        raise ValueError("Approved physical deck logical hash mismatch "+did)
    totals=Counter()
    counts=Counter()
    for z,oid,qty,name in entries:
        totals[z]+=qty
        if z in ("main","commander"):
            counts[name]+=qty
        if qty<1:raise ValueError("Bad physical quantity")
    if totals["main"]+totals["commander"]!=100 or totals["commander"]!=len(meta["commanders"]):
        raise ValueError("Wrong 100-card zone/commander count "+did+" "+str(totals))
    cmd_names=[name for z,oid,qty,name in entries if z=="commander" for _ in range(qty)]
    if cmd_names!=meta["commanders"]:
        raise ValueError("Physical source commanders/order changed "+did)
    if counts[row["cut"]]!=1 or counts[row["add"]]!=0:
        raise ValueError("Approved candidate swap cut/add presence mismatch "+did)
    if (totals["companion"]!=1 if did==SPECIAL_COMPANION else totals["companion"]!=0):
        raise ValueError("Companion handling mismatch "+did+" "+str(totals))
    companion_names=[name for z,oid,qty,name in entries if z=="companion"]
    if did==SPECIAL_COMPANION and companion_names!=["Lutri, the Spellchaser"]:
        raise ValueError("Explicit Lutri companion exception missing")
    # Source inventory does not silently repair recorded raw hash discrepancies.
    if (meta["source"]["recorded_matches_raw"] is False)!=(did in KNOWN_RECORD_MISMATCH):
        raise ValueError("Historical approved raw hash discrepancy changed "+did)
    if did in KNOWN_PROJECT_EXCEPTIONS:
        if len(meta["project_exceptions"])!=KNOWN_PROJECT_EXCEPTIONS[did]:
            raise ValueError("Deliberate project exception count changed "+did)
    elif meta["project_exceptions"]:
        raise ValueError("Undocumented new exception "+did)
    if did=="Tresserhorn_s_Lord__Returned" and meta["official_commander_compliance"]["status"]!="pending_release":
        raise ValueError("Future release misrepresented as officially legal")
    if did==SPECIAL_COMPANION and meta["official_commander_compliance"]["status"]!="not_compliant_project_exceptions":
        raise ValueError("Lutri / banned card exceptions misrepresented as officially legal")
    repeated={name:qty for name,qty in counts.items() if qty>1 and name not in BASICS}
    if repeated:
        # All 29 new cases are expected to be physically singleton besides basics.
        raise ValueError("Unexpected singleton/printed-copy exception "+did+" "+str(repeated))
    # Color identity: Grixis commander pair; recognize project-approved exceptions
    # separately from color identity. Do not treat frozen legality as current.
    commander_ci=set()
    for name in meta["commanders"]:
        obj,amb=resolver.get(name)
        if obj is None or amb or obj["name"]!=name:
            raise ValueError("Unknown frozen commander "+name)
        commander_ci.update(obj.get("color_identity") or [])
    if commander_ci!={"U","B","R"}:
        raise ValueError("Unexpected commander color identity "+did+" "+str(commander_ci))
    oracle={}
    for name in [*meta["commanders"],row["add"],row["cut"]]:
        card,amb=resolver.get(name)
        if card is None or amb or card["name"]!=name:
            raise ValueError("Frozen Oracle unrecognized exact card "+name)
        txt=card.get("oracle_text") or "\n".join(x.get("oracle_text") or "" for x in card.get("card_faces",[]))
        if not txt:raise ValueError("No text for card "+name)
        oracle[name]="sha256:"+hashlib.sha256(txt.encode()).hexdigest()
    for z,oid,qty,name in entries:
        if z not in ("commander","main","companion"):raise ValueError("Unknown zone "+z)
        card,amb=resolver.get(name)
        if not card or amb:raise ValueError("Unknown in-source Oracle card "+name)
        if not set(card.get("color_identity",[]))<=commander_ci:
            raise ValueError("Card outside commander CI "+did+" "+name)
    return {"deck_id":did,"commander_names":meta["commanders"],"source_path":meta["source"]["path"],
        "source_logical_sha":meta["current_canonical_hash"],
        "source_approved_recorded_raw_sha_not_rehashed":meta["source"]["recorded_sha256"],
        "recorded_raw_hash_matches_original_source":meta["source"]["recorded_matches_raw"],
        "source_blueprint_sha":digest(bp_path),"m5_swap_id":c["swap_id"],"add":row["add"],"cut":row["cut"],
        "source_cards_100":totals["main"]+totals["commander"],"commanders":totals["commander"],
        "companion_outside_100":totals["companion"],
        "official_status_at_frozen_snapshot":meta["official_commander_compliance"]["status"],
        "registered_project_exceptions":meta["project_exceptions"],
        "candidate_and_commander_oracle_sha":oracle,
        "authored_judgment":"PRESENT_SOURCE_ANCHORED_NOT_INDEPENDENT","formal_pass_c":False,
        "complete_phase_b":False,"owner_approved_swaps":0}
def audit():
    plan,reg,tri,track=map(read,(PLAN,REG,TRI,TRACK))
    if (plan["cycle"]!=131 or plan["status"]!="PREREGISTERED_BEFORE_AUTHOR_CONCLUSIONS" or
        len(reg["decks"])!=62 or track["m6"]["gates"][3]["completed"]!=33 or
        track["m6"]["formal_m6_certified_decks"]!=0 or
        reg["program"]["milestones"]["M6"]["status"]!="in_progress" or
        reg["program"]["milestones"]["M7"]["status"]!="not_started" or
        any(plan["authority"].values())):
        raise ValueError("Preregistration, current approval gates or review baseline drift")
    previous=existing()
    queue={x["deck_id"]:x for x in tri["ordered_decks"]}
    if len(queue)!=62 or set(queue)!=set(reg["decks"]):
        raise ValueError("Source 62 deck inventory changed")
    expected=set(queue)-set(previous)
    if len(expected)!=29:
        raise ValueError("Expected 29 missing authored decks, got "+str(len(expected)))
    new=[]
    for label,path in BATCHES.items():
        b=read(path)
        if b["cycle"]!=131 or b["batch"]!=label.upper() or b["source_kind"]!="authored_commander_first" or b["count"]!=len(b["rows"]):
            raise ValueError("Batch schema/provenance drift "+label)
        new.extend(b["rows"])
    ids=[x["deck_id"] for x in new]
    if len(ids)!=29 or len(set(ids))!=29 or set(ids)!=expected:
        raise ValueError("New authored cases don't exactly cover remaining 29: "+str(sorted(expected-set(ids))))
    # The outer author has authored all cases, but cannot self-identify as Pass C.
    if any(x["authored_by"]!="ChatGPT primary engineer; not independent" for x in new):
        raise ValueError("False separate reviewer")
    R=ev.Resolver()
    receipts=[validate_row(item,queue[item["deck_id"]],reg["decks"][item["deck_id"]],R) for item in new]
    if sum(not x["recorded_raw_hash_matches_original_source"] for x in receipts)!=2:
        raise ValueError("Two recorded raw source inconsistencies hidden")
    authors=[*previous,*ids]
    return {"schema_version":1,"cycle":131,"stage":"AUTHOR_REVIEWS_COMPLETE_AWAITING_INDEPENDENT_PASS_C",
        "approved_canonical_decks":62,"previous_authored":33,"new_authored":29,
        "total_authored":len(authors),"authored_deck_ids_in_triage_order":
          [x["deck_id"] for x in tri["ordered_decks"]],
        "new_reviews":receipts,"source_sha256":{"prereg":digest(PLAN),
          "registry":digest(REG),"triage":digest(TRI),"secondary_tracker_before":digest(TRACK),
          **{label:digest(path) for label,path in BATCHES.items()}},
        "formal_independent_pass_c_completed":0,"complete_effect_aware_phase_b_certified":0,
        "m6_certified_decks":0,"m6_accepted":False,"m7_started":False,
        "canonical_deck_changes":0,"owner_approved_swaps":0,
        "current_full_100_card_legality_reverified":False,
        "independence_note":"All 29 are ChatGPT original author reviews. GrokBot may perform future independent review only after qualification, disclosure of prior blueprint exposure and independent source/evidence analysis; neither this receipt nor CI certify Pass C.",
        "phase_b_note":"Author reviews include falsifiable scenarios, not measured multiplayer/effect-aware trials or tested-pool local certificates."}
def main():
    cli=argparse.ArgumentParser()
    cli.add_argument("--build",action="store_true")
    cli.add_argument("--check",action="store_true")
    a=cli.parse_args()
    if not(a.build or a.check):cli.error("Select --build and/or --check")
    doc=stable(audit())
    if a.build:
        OUT.parent.mkdir(parents=True,exist_ok=True)
        OUT.write_text(doc,encoding="utf-8")
    if a.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=doc):
        raise ValueError("Authorship census replay bytes differ")
    print("Cycle131 AUTHOR COMPLETE: 62 distinct source-anchored authored decks; 29 new. Formal Pass C 0/62, Phase B 0/62, canonical swaps 0.")
if __name__=="__main__":main()
