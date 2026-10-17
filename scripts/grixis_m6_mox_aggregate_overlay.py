#!/usr/bin/env python3
"""Cycle 91: aggregate overlay of corrected fast mana without editing historic summaries."""
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"data/grixis/mana_base/summary.json"
STATIC=ROOT/"data/grixis/m6/mox_reconciliation/static_manifest.json"
NOFAST=ROOT/"data/grixis/m6/mox_reconciliation/nofast_manifest.json"
PROOF=ROOT/"data/grixis/m6/mox_reconciliation/dependency_proof.json"
CMD=ROOT/"data/grixis/commander_mana/summary.json"
REG=ROOT/"data/grixis/registry.json"
OUT=ROOT/"data/grixis/m6/mox_reconciliation/aggregate_overlay.json"
def load(x):return json.loads(x.read_text(encoding="utf-8"))
def sha(x):return "sha256:"+hashlib.sha256(x.read_bytes()).hexdigest()
def fmt(o):return json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n"
def derive():
    a,s,n,p,c,r=map(load,(BASE,STATIC,NOFAST,PROOF,CMD,REG))
    if a["totals"]["decks"]!=62 or len(r["decks"])!=62 or s["count"]!=n["count"]!=p["decks"]!=25:
        raise ValueError("coverage drift")
    if p["verified_existing_outputs"]!=75 or c["totals"]["commander_records"]!=65:
        raise ValueError("dependency/commander baseline drift")
    if r["program"]["milestones"]["M5"]["status"]!="accepted" or r["program"]["milestones"]["M6"].get("accepted_by") is not None:
        raise ValueError("M5/M6 authority mismatch")
    byslug={v["slug"]:v for v in s["rows"]}
    deckrows=[]
    for row in a["decks"]:
        old=row["fast_mana"];delta=1 if row["slug"] in byslug else 0
        if delta and (byslug[row["slug"]]["old_fast_mana"]!=old or byslug[row["slug"]]["corrected_fast_mana"]!=old+1):
            raise ValueError("corrected row mismatch: "+row["slug"])
        deckrows.append({**row,"fast_mana":old+delta,"chrome_mox_conditional_inventory_delta":delta})
    if sum(x["chrome_mox_conditional_inventory_delta"] for x in deckrows)!=25:
        raise ValueError("25 Chrome Mox totals missing")
    newtot={**a["totals"],"fast_mana":sum(x["fast_mana"] for x in deckrows)}
    if newtot["fast_mana"]!=a["totals"]["fast_mana"]+25:
        raise ValueError("aggregate delta mismatch")
    for k in ("lands","flex_land_mdfcs","unresolved","decks"):
        if newtot[k]!=a["totals"][k]:
            raise ValueError("unexpected aggregate change")
    return {"schema_version":1,"stage":"M6_Chrome_Mox_correction_62_deck_aggregate_overlay",
        "inputs":{"historic_static_sha256":sha(BASE),"corrected_25_static_manifest_sha256":sha(STATIC),
                  "corrected_25_nofast_manifest_sha256":sha(NOFAST),
                  "unchanged_75_dependencies_sha256":sha(PROOF),
                  "historic_commander_summary_sha256":sha(CMD)},
        "original_totals":a["totals"],"corrected_totals":newtot,
        "deck_rows":deckrows,
        "existing_65_commander_cast_and_tax_summary_unchanged":True,
        "fast_package_proxies_corrected_separately_for_25_decks":True,
        "historical_evidence_overwritten":False,
        "color_source_count_is_potential_not_imprint_probability":True,
        "limits":["This overlay fixes only known Chrome Mox conditional-fast classification totals",
                  "Historic Step C summaries remain immutable evidence of their original analysis",
                  "These counts are not new cast-rate, mana-fixing reliability, or win-rate estimates",
                  "No M6 deck decisions, certificates or approvals follow from the counts"],
        "authority":{"can_decide":False,"can_apply_swap":False,"can_approve_or_lock":False}}
def main():
    a=argparse.ArgumentParser();a.add_argument("--build",action="store_true");a.add_argument("--check",action="store_true");c=a.parse_args()
    if not(c.build or c.check):a.error("require build or check")
    d=derive();body=fmt(d)
    if c.build:OUT.write_text(body,encoding="utf-8")
    if c.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=body):raise ValueError("aggregate overlay drift")
    print("corrected fast mana",d["original_totals"]["fast_mana"],"->",d["corrected_totals"]["fast_mana"],"; 62/62; 0 deck changes")
if __name__=="__main__":main()
