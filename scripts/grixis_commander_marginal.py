#!/usr/bin/env python3
"""Step D batch 69.3: integrate structural and paired dynamic commander-marginality evidence.

No scalar commander-value score is produced. Instead each record keeps the requested dimensions separate: structural
routes/engines, card economy, mana utilization, first package/key access, combo assembly, a meaningful-progress vector,
and disruption recovery. Real records are built only after 69.2 counterfactual outputs exist on the frozen local cache.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
REG=ROOT/"data/grixis/registry.json"
STRUCT=ROOT/"data/grixis/commander_structure"
CF=ROOT/"data/grixis/commander_counterfactual"
OUT=ROOT/"data/grixis/commander_marginal"
SCHEMA=ROOT/"data/grixis/schemas/commander_marginal.schema.json"
VERSION=1


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def dump(p,o):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")

def ratio(a,b): return None if a is None or b in (None,0) else round(a/b,6)

def mode_vector(m):
    key=m.get("first_key_set_access_by_turn4",{})
    return {
      "card_economy":{"extra_cards_drawn_mean":m.get("extra_cards_drawn_mean"),"tutors_resolved_mean":m.get("tutors_resolved_mean")},
      "mana_efficiency":{"mana_spent_t1_6_mean":m.get("mana_spent_t1_6_mean"),"mana_available_t1_6_mean":m.get("mana_available_t1_6_mean"),"spent_over_available_proxy":ratio(m.get("mana_spent_t1_6_mean"),m.get("mana_available_t1_6_mean"))},
      "package_access":{"first_key_set_access_by_turn4":key,"expected_key_sets_first_accessed_by_turn4":round(sum(key.values()),6)},
      "combo_access":{"combo_assembled_by_turn6":m.get("combo_assembled_by_turn6"),"win_proxy_by_turn6":m.get("win_proxy_by_turn6")},
      "meaningful_progress_vector":{"commander_cast_by_turn6":m.get("commander_cast_by_turn6"),"extra_cards_drawn_mean":m.get("extra_cards_drawn_mean"),"tutors_resolved_mean":m.get("tutors_resolved_mean"),"expected_key_sets_first_accessed_by_turn4":round(sum(key.values()),6),"combo_assembled_by_turn6":m.get("combo_assembled_by_turn6")},
      "recovery":m.get("disruption_recovery")
    }

def vector_delta(normal,other):
    def sub(a,b): return None if a is None or b is None else round(a-b,6)
    out={}
    for section in ("card_economy","mana_efficiency","package_access","combo_access","meaningful_progress_vector"):
        out[section]={}
        for k,av in normal[section].items():
            bv=other[section].get(k)
            if isinstance(av,(int,float)) or av is None:
                out[section][k]=sub(av,bv)
    return out


def build_one(slug):
    reg=load(REG); did,e=next((did,e) for did,e in reg["decks"].items() if e["slug"]==slug)
    st=load(STRUCT/f"{slug}.json"); cf=load(CF/f"{slug}.json")
    vectors={m:mode_vector(cf["metrics"][m]) for m in ("normal","unavailable","taxed","disrupted")}
    return {
      "schema_version":1,"deck_id":did,"slug":slug,"canonical_hash":e["canonical_project_list"]["hash"],
      "status":"provisional_marginal_value_evidence","evidence_class":"test_result","confidence":"low",
      "authority":{"can_decide":False,"note":"Commander marginal-value vectors remain evidence; no scalar score or deck decision is emitted."},
      "accepted_blueprint_role":st["accepted_blueprint_role"],
      "structural_routes":{"summary":st["summary"],"wins":st["blueprint_routes"]["wins"],"engines":st["blueprint_routes"]["engines"],"combo_routes":st["combo_routes"]},
      "dynamic_vectors":vectors,
      "normal_minus_counterfactual":{m:vector_delta(vectors["normal"],vectors[m]) for m in ("unavailable","taxed","disrupted")},
      "dimension_status":{
        "engines":"structural explicit-dependence evidence available; engine-online probability not modeled by v1.1",
        "package_access":"dynamic first-member access only; not package completion",
        "card_economy":"extra draws and tutors modeled by v1.1 only",
        "combo_assembly":"dynamic assembly/win proxies plus structural route dependence",
        "meaningful_actions":"reported as a non-collapsed meaningful-progress vector; no heterogeneous events are summed into one score",
        "mana_efficiency":"spent/available resource proxy through turn 6",
        "recovery":"bounded commander-removal/recast proxy",
        "strategic_routes":"accepted Blueprint + Step-B structural route evidence"
      },
      "limitations":["No dimension is converted into a universal commander-value score.","Dynamic results inherit every grixis_sim v1.1 limitation and are not multiplayer win rates.","Meaningful progress is a vector of separately interpretable components, not a count of heterogeneous actions.","Package access is first access to any key-set member, not completion or engine-online probability.","Commander-native triggered/activated abilities missing from v1.1 can make dynamic deltas understate real commander value; structural Blueprint evidence remains mandatory context.","Partner-pair disruption remains a bounded one-at-a-time legacy stress proxy."]
    }


def build_all():
    reg=load(REG); OUT.mkdir(parents=True,exist_ok=True); rows=[]
    for did,e in sorted(reg["decks"].items(),key=lambda kv:kv[1]["slug"]):
        d=build_one(e["slug"]); dump(OUT/f"{e['slug']}.json",d); rows.append({"deck_id":did,"slug":e["slug"],"role":d["accepted_blueprint_role"]["level"]})
    dump(OUT/"summary.json",{"schema_version":1,"generated_by":f"scripts/grixis_commander_marginal.py v{VERSION}","decks":rows,"totals":{"decks":len(rows)}})
    print(f"commander-marginal: built {len(rows)} decks")

def check():
    try: import jsonschema
    except ImportError: print("commander-marginal: jsonschema required"); return 1
    reg=load(REG); expected={e["slug"] for e in reg["decks"].values()}; present={p.stem for p in OUT.glob("*.json") if p.name!="summary.json"} if OUT.exists() else set(); problems=[]
    if not present:
        print("commander-marginal: 0/62 records; pending frozen-local-cache counterfactual outputs")
        return 0
    if present!=expected: problems.append(f"partial population missing={sorted(expected-present)} extra={sorted(present-expected)}")
    schema=load(SCHEMA)
    for did,e in sorted(reg["decks"].items()):
        p=OUT/f"{e['slug']}.json"
        if not p.exists(): continue
        d=load(p)
        for err in jsonschema.Draft202012Validator(schema).iter_errors(d): problems.append(f"{e['slug']}: schema {list(err.path)}: {err.message}")
        if d["canonical_hash"]!=e["canonical_project_list"]["hash"]: problems.append(f"{e['slug']}: canonical hash drift")
        if d["authority"]["can_decide"] is not False: problems.append(f"{e['slug']}: record became decision-capable")
    print(f"commander-marginal: {len(present)}/62 records, {len(problems)} problems")
    for p in problems[:40]: print("FAIL",p)
    return 1 if problems else 0

def main(argv=None):
    a=argparse.ArgumentParser(); a.add_argument("--build",action="store_true"); a.add_argument("--check",action="store_true"); a.add_argument("--deck"); x=a.parse_args(argv); rc=0
    if x.deck: print(json.dumps(build_one(x.deck),indent=2,sort_keys=True))
    if x.build: build_all()
    if x.check: rc|=check()
    if not (x.deck or x.build or x.check): a.print_help()
    return rc
if __name__=="__main__": sys.exit(main())
