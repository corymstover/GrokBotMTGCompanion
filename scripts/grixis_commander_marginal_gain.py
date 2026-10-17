#!/usr/bin/env python3
"""Step D acceptance-standard proof: demonstrate decision-resolution gain without claiming dynamic closure early."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
STRUCT=ROOT/"data/grixis/commander_structure"; OUT=ROOT/"data/grixis/commander_marginal_gain.json"; SCHEMA=ROOT/"data/grixis/schemas/commander_marginal_gain.schema.json"

def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def dump(p,o): Path(p).write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")

def example(slug):
    d=load(STRUCT/f"{slug}.json"); s=d["summary"]
    return {"slug":slug,"accepted_role":d["accepted_blueprint_role"]["level"],"honest_note":d["accepted_blueprint_role"].get("honest_note"),"structural_counts":s,
            "resolution_gain":f"Separates {s['blueprint_wins_explicit_commander']} explicit commander win route(s) from {s['blueprint_wins_structurally_independent']} structurally independent Blueprint win route(s), and {s['combo_blueprint_supported']+s['combo_direct_commander_piece']} commander-linked Spellbook line(s) from {s['combo_commander_independent']} structurally independent line(s), without replacing the accepted role judgment."}

def build_record():
    summ=load(STRUCT/"summary.json")["decks"]
    central=next(x["slug"] for x in summ if x["role"]=="central" and x["blueprint_wins_explicit_commander"] and x["blueprint_wins_structurally_independent"])
    support=next((x["slug"] for x in summ if x["role"]=="supporting"),None)
    slugs=["kess-dissident-mage",central]+([support] if support and support not in ("kess-dissident-mage",central) else [])
    slugs=list(dict.fromkeys(slugs))
    totals=load(STRUCT/"summary.json")["totals"]
    return {
      "schema_version":1,"status":"demonstrated_partial_decision_resolution_gain","evidence_class":"derived_metric",
      "authority":{"can_decide":False,"note":"This proof shows added commander-dependence resolution, not commander-value truth or a deck decision."},
      "before":{"limitations":["Accepted Blueprint commander roles existed, but declared wins/engines/packages and Spellbook lines were not systematically partitioned by explicit commander dependence.","The prior simulator had no commander-unavailable or starting-tax counterfactual mode.","No single Step D record kept structural strategic routes and dynamic counterfactual dimensions in a common non-scoring evidence vector."]},
      "after":{"implemented":["62-deck structural route partition with accepted role preserved","paired normal/unavailable/+2-tax/removal-disruption simulator architecture with common seeds/permutations","non-collapsed integration vector for card economy, mana efficiency, key-set access, combo access, meaningful progress and recovery"],"pending":["Real 62-deck dynamic counterfactual outputs on frozen local Scryfall cache","Dynamic engine-online probability remains outside v1.1; structural engine dependence is retained instead"]},
      "measured":{"structural_decks":totals["decks"],"structural_spellbook_lines":totals["spellbook_lines"],"commander_direct_or_supported_lines":totals["combo_direct_commander_piece"]+totals["combo_blueprint_supported"],"commander_independent_lines":totals["combo_commander_independent"],"automatic_deck_decisions":0},
      "real_deck_examples":[example(s) for s in slugs],
      "limitations":["The demonstrated gain is structural/architectural until real dynamic outputs are generated locally.","Explicit commander-reference absence is not proof of zero commander value.","Counterfactual goldfish results will remain bounded test evidence, not multiplayer win rates.","Meaningful progress remains a vector; heterogeneous events are not summed into a synthetic score.","Accepted Blueprint commander-role judgments remain higher-value strategic context than these derived counts."],
      "conclusion":"Step D now distinguishes declared commander-linked strategic routes from independent routes and has a paired dynamic counterfactual architecture without collapsing either into a score; full dynamic closure remains an explicit frozen-local-cache item."
    }

def build(): d=build_record(); dump(OUT,d); print(json.dumps(d["measured"],indent=2,sort_keys=True))
def check():
    try: import jsonschema
    except ImportError: print("commander-marginal-gain: jsonschema required"); return 1
    problems=[]
    if not OUT.exists(): problems.append("gain record missing")
    else:
        d=load(OUT); s=load(SCHEMA)
        problems += [f"schema {list(e.path)}: {e.message}" for e in jsonschema.Draft202012Validator(s).iter_errors(d)]
        if d!=build_record(): problems.append("gain record stale")
        if d["authority"]["can_decide"] is not False: problems.append("gain record became decision-capable")
        if d["measured"]["structural_decks"]!=62: problems.append("structural coverage != 62")
        if d["measured"]["automatic_deck_decisions"]!=0: problems.append("automatic decisions != 0")
    print(f"commander-marginal-gain: {len(problems)} problems")
    for p in problems: print("FAIL",p)
    return 1 if problems else 0

def main(argv=None):
    a=argparse.ArgumentParser(); a.add_argument("--build",action="store_true"); a.add_argument("--check",action="store_true"); x=a.parse_args(argv); rc=0
    if x.build: build()
    if x.check: rc|=check()
    if not (x.build or x.check): a.print_help()
    return rc
if __name__=="__main__": sys.exit(main())
