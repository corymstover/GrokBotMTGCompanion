#!/usr/bin/env python3
"""Step D batch 69.1: structural commander-marginality evidence across all 62 decks.

This layer asks a narrow counterfactual question before simulation: which *declared* Blueprint routes, engines, packages
and Step-B combo lines explicitly require or are supported by the commander, and which remain structurally independent?
It does not turn those counts into a commander-value score and does not infer that an unmentioned commander interaction
has zero value. Dynamic action/economy/recovery deltas are later Step D batches.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
REG=ROOT/"data/grixis/registry.json"
BP=ROOT/"data/grixis/blueprints"
CQ=ROOT/"data/grixis/combo_quality"
OUT=ROOT/"data/grixis/commander_structure"
SCHEMA=ROOT/"data/grixis/schemas/commander_structure.schema.json"
VERSION=1


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def dump(p,o):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")

def names(bp): return [x["name"] for x in bp["commanders"]["value"]]
def hits(items,cmds): return sorted(set(items or []) & set(cmds))


def route_rows(bp,cmds):
    wins=[]
    for w in bp.get("win_conditions",[]):
        direct=hits(list(w.get("cards",[]))+list(w.get("enablers",[])),cmds)
        wins.append({"id":w["id"],"kind":w.get("kind"),"commander_refs":direct,"commander_explicit":bool(direct),"evidence_class":w.get("evidence_class","strategic_judgment"),"confidence":w.get("confidence","moderate")})
    engines=[]
    for e in bp.get("engines",[]):
        direct=hits(e.get("cards",[]),cmds)
        engines.append({"id":e["id"],"commander_refs":direct,"commander_explicit":bool(direct),"online_condition_mentions_commander":any(n.lower() in (e.get("online_condition") or "").lower() for n in cmds)})
    packages=[]
    for p in bp.get("packages",[]):
        direct=hits(p.get("cards",[]),cmds)
        packages.append({"id":p["id"],"required":bool(p.get("required")),"min_count":p.get("min_count"),"commander_refs":direct,"commander_explicit":bool(direct)})
    return wins,engines,packages


def combo_rows(cq,cmds):
    rows=[]
    for c in cq.get("combos",[]):
        v=c["axes"]["commander_requirement"]["value"]
        direct=sorted(set(v.get("direct_commander_pieces",[])) & set(cmds))
        support=sorted(set(v.get("blueprint_commander_support",[])) & set(cmds))
        mode="direct_commander_piece" if direct else "blueprint_supported" if support else "commander_independent"
        rows.append({"id":c["id"],"cards":c["cards"],"mode":mode,"direct_commander_pieces":direct,"blueprint_commander_support":support,"structural_hint":c.get("classification",{}).get("structural_hint")})
    return rows


def build_one(did,e):
    slug=e["slug"]; bp=load(BP/f"{slug}.json"); cq=load(CQ/f"{slug}.json"); cmds=names(bp)
    wins,engines,packages=route_rows(bp,cmds); combos=combo_rows(cq,cmds)
    level=bp["commander_role"]["value"]["level"]
    summary={
      "blueprint_wins":len(wins),"blueprint_wins_explicit_commander":sum(x["commander_explicit"] for x in wins),"blueprint_wins_structurally_independent":sum(not x["commander_explicit"] for x in wins),
      "engines":len(engines),"engines_explicit_commander":sum(x["commander_explicit"] or x["online_condition_mentions_commander"] for x in engines),
      "required_packages":sum(x["required"] for x in packages),"required_packages_explicit_commander":sum(x["required"] and x["commander_explicit"] for x in packages),
      "spellbook_lines":len(combos),"combo_direct_commander_piece":sum(x["mode"]=="direct_commander_piece" for x in combos),"combo_blueprint_supported":sum(x["mode"]=="blueprint_supported" for x in combos),"combo_commander_independent":sum(x["mode"]=="commander_independent" for x in combos)
    }
    return {
      "schema_version":1,"deck_id":did,"slug":slug,"canonical_hash":e["canonical_project_list"]["hash"],
      "status":"provisional_evidence","evidence_class":"derived_metric","confidence":"moderate",
      "authority":{"can_decide":False,"note":"Structural commander-reference counts are a counterfactual prior only; they cannot decide deck changes or commander value."},
      "commanders":cmds,
      "accepted_blueprint_role":{"level":level,"advances_plan":bp["commander_role"]["value"].get("advances_plan"),"honest_note":bp["commander_role"]["value"].get("honest_note"),"evidence_class":bp["commander_role"].get("evidence_class"),"confidence":bp["commander_role"].get("confidence")},
      "blueprint_routes":{"wins":wins,"engines":engines,"packages":packages},
      "combo_routes":combos,"summary":summary,
      "counterfactual_questions":["Which declared wins disappear or change when the commander is unavailable?","Which declared engines/packages explicitly require the commander?","Which Spellbook lines remain structurally independent?","How much dynamic card economy, action efficiency, assembly speed and recovery actually changes? (deferred to later Step D batches)"],
      "limitations":["Exact-name/Blueprint support is structural evidence, not a complete rules-interaction detector.","A route without an explicit commander reference may still gain substantial value from the commander in play.","A route with an explicit commander reference may have redundant alternate routes not captured by a single Blueprint field.","Counts are intentionally not combined into a synthetic commander-value score.","Dynamic effects on cards drawn, meaningful actions, mana spent, combo timing and recovery require the Step D counterfactual simulator layer."]
    }


def build():
    reg=load(REG); rows=[]; OUT.mkdir(parents=True,exist_ok=True)
    for did,e in sorted(reg["decks"].items(),key=lambda kv:kv[1]["slug"]):
        d=build_one(did,e); dump(OUT/f"{e['slug']}.json",d); rows.append({"deck_id":did,"slug":e["slug"],"role":d["accepted_blueprint_role"]["level"],**d["summary"]})
    dump(OUT/"summary.json",{"schema_version":1,"generated_by":f"scripts/grixis_commander_structure.py v{VERSION}","decks":rows,"totals":{"decks":len(rows),"blueprint_wins":sum(x["blueprint_wins"] for x in rows),"blueprint_wins_explicit_commander":sum(x["blueprint_wins_explicit_commander"] for x in rows),"engines_explicit_commander":sum(x["engines_explicit_commander"] for x in rows),"spellbook_lines":sum(x["spellbook_lines"] for x in rows),"combo_direct_commander_piece":sum(x["combo_direct_commander_piece"] for x in rows),"combo_blueprint_supported":sum(x["combo_blueprint_supported"] for x in rows),"combo_commander_independent":sum(x["combo_commander_independent"] for x in rows)}})
    print(f"commander-structure: built {len(rows)} decks")


def check():
    try: import jsonschema
    except ImportError: print("commander-structure: jsonschema required"); return 1
    reg=load(REG); schema=load(SCHEMA); problems=[]; expected={e["slug"] for e in reg["decks"].values()}; present={p.stem for p in OUT.glob("*.json") if p.name!="summary.json"}
    if expected!=present: problems.append(f"coverage mismatch missing={sorted(expected-present)} extra={sorted(present-expected)}")
    for did,e in sorted(reg["decks"].items()):
        p=OUT/f"{e['slug']}.json"
        if not p.exists(): continue
        d=load(p)
        for err in jsonschema.Draft202012Validator(schema).iter_errors(d): problems.append(f"{e['slug']}: schema {list(err.path)}: {err.message}")
        if d["canonical_hash"]!=e["canonical_project_list"]["hash"]: problems.append(f"{e['slug']}: canonical hash drift")
        if d["authority"]["can_decide"] is not False: problems.append(f"{e['slug']}: record became decision-capable")
        s=d["summary"]
        if s["spellbook_lines"] != s["combo_direct_commander_piece"]+s["combo_blueprint_supported"]+s["combo_commander_independent"]: problems.append(f"{e['slug']}: combo route partition mismatch")
        if s["blueprint_wins"] != s["blueprint_wins_explicit_commander"]+s["blueprint_wins_structurally_independent"]: problems.append(f"{e['slug']}: win route partition mismatch")
    print(f"commander-structure: {len(expected)} deck files, {len(problems)} problems")
    for p in problems[:50]: print("FAIL",p)
    return 1 if problems else 0


def main(argv=None):
    a=argparse.ArgumentParser(); a.add_argument("--build",action="store_true"); a.add_argument("--check",action="store_true"); a.add_argument("--summary",action="store_true"); x=a.parse_args(argv); rc=0
    if x.build: build()
    if x.check: rc|=check()
    if x.summary: print(json.dumps(load(OUT/"summary.json"),indent=2,sort_keys=True))
    if not (x.build or x.check or x.summary): a.print_help()
    return rc
if __name__=="__main__": sys.exit(main())
