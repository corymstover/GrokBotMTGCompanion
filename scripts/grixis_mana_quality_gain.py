#!/usr/bin/env python3
"""Step C acceptance-standard proof: show real before/after mana decision-resolution gains.

This is a capability/evidence-resolution comparison, not a mana-base score and not a deck-change decision.
It consumes only committed Step C artifacts and deliberately leaves commander cast/tax outputs pending until the frozen
local Scryfall cache can build 68.3.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
BASE=ROOT/"data/grixis/mana_base"
TIMING=ROOT/"data/grixis/mana_timing"
OPP=ROOT/"data/grixis/mana_opportunity"
RES=ROOT/"data/grixis/mana_resilience"
OUT=ROOT/"data/grixis/mana_quality_gain.json"
SCHEMA=ROOT/"data/grixis/schemas/mana_quality_gain.schema.json"


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def dump(p,o): Path(p).write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")

def records(folder): return [load(p) for p in sorted(Path(folder).glob("*.json")) if p.name!="summary.json"]


def choose_timing_example():
    for d in records(TIMING):
        for t,row in sorted(d["turn_readiness"].items(),key=lambda kv:int(kv[0])):
            if row["potential_distinct_source_match_UBR"] != row["unconditional_distinct_source_match_UBR"] or row["potential_distinct_source_match_UBR"] != row["untapped_capable_distinct_source_match_UBR"]:
                return d,t,row
    raise RuntimeError("no real timing distinction found")


def choose_mdfc_example():
    for d in records(OPP):
        if d.get("mdfcs"):
            timing=load(TIMING/f"{d['slug']}.json")
            for t,row in sorted(timing["turn_readiness"].items(),key=lambda kv:int(kv[0])):
                if row["strict_land_drop_probability"] != row["flex_land_drop_probability"]:
                    return d,t,row
    raise RuntimeError("no real MDFC optionality example found")


def choose_utility_example():
    for d in records(OPP):
        for land in d.get("utility_lands",[]):
            if land.get("burden_flags") and land.get("support_flags"):
                return d,land
    raise RuntimeError("no utility land with both burden and support signals found")


def choose_resilience_example():
    for d in records(RES):
        if d["summary"].get("fetch_color_single_points",0)>0:
            fragile=[x for x in d["fetch_target_resilience"] if x["colors_with_only_one_target"]]
            if fragile:
                return d,fragile[0]
    # Structural one-source sensitivity is present for every normal deck; use it if fetch topology has no single point.
    for d in records(RES):
        r=d["turn_failure"]["3"]["one_strict_source_unavailable_UBR"]
        if r["worst_relative_delta"]>0:
            return d,{"structural_source_sensitivity":r}
    raise RuntimeError("no real resilience example found")


def build_record():
    bs=load(BASE/"summary.json")["totals"]; ts=load(TIMING/"summary.json")["totals"]
    os=load(OPP/"summary.json")["totals"]; rs=load(RES/"summary.json")["totals"]
    td,turn,tr=choose_timing_example(); md,mturn,mr=choose_mdfc_example(); ud,land=choose_utility_example(); rd,frag=choose_resilience_example()
    examples=[
      {
       "kind":"timing_and_condition_distinction","slug":td["slug"],
       "before":"Static source counts could say a land can make a color but could not separate conditional availability or untapped-capable timing in a distinct-source assignment.",
       "after":f"By turn {turn}, Step C records potential UBR match {tr['potential_distinct_source_match_UBR']}, unconditional UBR match {tr['unconditional_distinct_source_match_UBR']}, and untapped-capable UBR match {tr['untapped_capable_distinct_source_match_UBR']} as separate exact no-mulligan presence proxies.",
       "why_it_matters":"A nominal colored-source count can otherwise overstate what is available under its own condition or timing burden."
      },
      {
       "kind":"mdfc_optionality","slug":md["slug"],
       "cards":[x["card"] for x in md["mdfcs"]],
       "before":"Treating an MDFC as simply a land or simply a spell loses the option-value tradeoff.",
       "after":f"At turn {mturn}, the same deck has strict-land-drop probability {mr['strict_land_drop_probability']} and flex-land/MDFC probability {mr['flex_land_drop_probability']}; the MDFC stays an optional layer rather than silently inflating strict land count.",
       "why_it_matters":"Candidate review can see the resource benefit of the land face without pretending the spell slot has no opportunity cost."
      },
      {
       "kind":"utility_land_burden_vs_support","slug":ud["slug"],"card":land["card"],
       "before":"A generic utility-land heuristic can flag color/tapped burden or strategic text but has no reason to preserve the two dimensions separately.",
       "after":f"Step C records burdens {land['burden_flags']} and Commander-first/support signals {land['support_flags']} separately for {land['card']}, with `can_decide: false`.",
       "why_it_matters":"A land can be structurally expensive and strategically important at the same time; later judgment must compare both instead of auto-cutting it."
      },
      {
       "kind":"source_resilience","slug":rd["slug"],
       "before":"Raw source totals and fetch counts do not expose single-target color points or the marginal loss from one source becoming unavailable.",
       "after":f"Step C records bounded fetch/source resilience evidence for this real deck: {frag}.",
       "why_it_matters":"This identifies structural fragility without inventing opponent-removal frequency or a universal mana-quality score."
      }
    ]
    return {
      "schema_version":1,"status":"demonstrated_decision_quality_gain","evidence_class":"derived_metric",
      "authority":{"can_decide":False,"note":"This proof demonstrates added decision resolution only; it cannot decide a mana-base swap."},
      "before":{"model":"pre-Step-C general audit/candidate evidence","limitations":["No dedicated exact colored-source matching by turn.","No strict-land vs MDFC optional land-drop separation.","No fetch-target topology validation against actual typed lands.","No separate utility-land burden/support vector.","No one-source-unavailable structural sensitivity.","No dedicated commander cast/tax recovery layer."]},
      "after":{"model":"Step C batches 68.1/68.2/68.4/68.5 plus 68.3 code pending local-cache output","available_dimensions":["land/MDFC counts","colored pip demand","source-color inventory","distinct-source matching","conditional/unconditional/untapped-capable timing","fetch/typed-land target topology","utility-land burden and Commander-first support","MDFC option value","land-drop/source-access failure complements","one-source-unavailable structural sensitivity"],"pending":["68.3 actual commander casting, fast-mana delta and tax-recovery records require the frozen local Scryfall cache before Step C can be fully closed."]},
      "measured_deltas":{"mana_base_decks":bs["decks"],"mana_timing_decks":ts["decks"],"mana_opportunity_decks":os["decks"],"mana_resilience_decks":rs["decks"],"automatic_land_swap_decisions":0},
      "worked_examples":examples,
      "limitations":["This is a stated before/after capability comparison on real project decks, not blind benchmark accuracy.","No-mulligan presence and land-drop values are bounded resource-access proxies, not real-game loss or cast probabilities.","Conditional sources, sequencing, multiplayer interaction and strategic value still require later evidence/judgment.","68.3 commander casting/tax recovery remains explicitly pending local frozen-cache generation and validation.","No Step C artifact may by itself approve, cut, add or lock a card."],
      "conclusion":"Step C now resolves timing, MDFC optionality, fetch topology, utility-land tradeoffs and source fragility that static mana counts could not, while making zero automatic land-swap decisions; commander casting/tax evidence remains a declared local-cache closure item."
    }


def build():
    d=build_record(); dump(OUT,d); print(json.dumps(d["measured_deltas"],indent=2,sort_keys=True))

def check():
    try: import jsonschema
    except ImportError: print("mana-quality-gain: jsonschema required"); return 1
    problems=[]
    if not OUT.exists(): problems.append("mana_quality_gain.json missing; run --build")
    else:
        d=load(OUT); schema=load(SCHEMA)
        problems += [f"schema {list(e.path)}: {e.message}" for e in jsonschema.Draft202012Validator(schema).iter_errors(d)]
        try: expected=build_record()
        except Exception as e: problems.append(f"cannot rebuild gain proof: {type(e).__name__}: {e}"); expected=None
        if expected is not None and d!=expected: problems.append("mana_quality_gain.json is stale vs current Step C artifacts")
        if d.get("authority",{}).get("can_decide") is not False: problems.append("gain proof became decision-capable")
        m=d.get("measured_deltas",{})
        if any(m.get(k)!=62 for k in ("mana_base_decks","mana_timing_decks","mana_opportunity_decks","mana_resilience_decks")): problems.append("Step C cache-independent layers no longer cover all 62 decks")
        if m.get("automatic_land_swap_decisions")!=0: problems.append("Step C must not auto-decide land swaps")
    print(f"mana-quality-gain: {len(problems)} problems")
    for p in problems: print("FAIL",p)
    return 1 if problems else 0

def main(argv=None):
    a=argparse.ArgumentParser(); a.add_argument("--build",action="store_true"); a.add_argument("--check",action="store_true"); x=a.parse_args(argv); rc=0
    if x.build: build()
    if x.check: rc|=check()
    if not (x.build or x.check): a.print_help()
    return rc
if __name__=="__main__": sys.exit(main())
