#!/usr/bin/env python3
"""Step F batch 70.1: pre-register bracket-specific stress suites before Birthday/M6 results exist.

Weights are *review-priority weights*, never outcome weights and never combined into a deck score. Each stress item
states whether it is executable by the legacy simulator, a Step-E mechanic module, a threshold readout, or requires
red-team judgment. Unsupported opponent-facing situations remain judgment prompts instead of fake simulations.
"""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
REG=ROOT/"data/grixis/registry.json"
OUT=ROOT/"data/grixis/bracket_stress"
SCHEMA=ROOT/"data/grixis/schemas/bracket_stress_suite.schema.json"
VERSION=1

B5=[
 ("turbo_clock","goldfish_threshold",0.20,"Pressure to present or meaningfully contest early wins; read existing goldfish/combo readiness, not a multiplayer win rate.",None),
 ("first_key_spell_countered","simulator_scenario",0.15,"First material setup/win spell is countered.","first_key_spell_countered"),
 ("graveyard_exiled","simulator_scenario",0.10,"Fast graveyard hate before or during setup.","graveyard_exiled"),
 ("commander_disruption","simulator_scenario",0.10,"Repeated commander disruption/tax pressure.","commander_removed_twice"),
 ("key_engine_exiled","simulator_scenario",0.10,"A central noncommander engine is exiled.","key_engine_exiled"),
 ("stack_protection","mechanic_module",0.15,"Can the list protect or force through a compact win under stack interaction?","counterspell_stack_protection"),
 ("stax_tax","mechanic_module",0.15,"Sensitivity to relevant stax/tax categories; categories remain separate.","stax_tax"),
 ("protected_win_red_team","judgment_prompt",0.05,"Adversarial reviewer asks whether primary wins remain executable through realistic protection/interaction windows.",None),
]
B4=[
 ("board_wipe","simulator_scenario",0.15,"Creature-board wipe and rebuilding pressure.","board_wipe"),
 ("artifact_wipe","simulator_scenario",0.10,"Artifact wipe / mana-engine disruption.","artifacts_wiped"),
 ("commander_disruption","simulator_scenario",0.15,"Repeated commander removal and tax recovery.","commander_removed_twice"),
 ("key_engine_exiled","simulator_scenario",0.10,"Central engine removal/exile.","key_engine_exiled"),
 ("mana_screw","simulator_scenario",0.10,"Missed land-drop recovery pressure.","mana_screw"),
 ("color_screw","simulator_scenario",0.05,"Temporary pressure on the commander's most-demanded color.","color_screw"),
 ("graveyard_exiled","simulator_scenario",0.05,"Graveyard hate/attrition where relevant.","graveyard_exiled"),
 ("repeated_removal_attrition","judgment_prompt",0.10,"Can the deck rebuild after repeated removal across multiple permanent types?",None),
 ("pillowfort","judgment_prompt",0.08,"Can combat/targeting-dependent routes function through pillowfort or must the deck pivot?",None),
 ("token_stall","judgment_prompt",0.06,"Can the deck progress through token stalls and clogged combat?",None),
 ("artifact_enchantment_interaction","judgment_prompt",0.06,"Does the deck have credible answers/recovery when key artifacts/enchantments are removed or opposing permanents must be answered?",None),
]
assert abs(sum(x[2] for x in B5)-1)<1e-9 and abs(sum(x[2] for x in B4)-1)<1e-9


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def dump(p,o):
 p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")

def ceiling(e):
 c=e.get("ceiling",{}); r=c.get("resolved_ceiling",{}).get("value")
 g=c.get("grok_estimated_ceiling",{}).get("value")
 s=c.get("source_ceiling",{}).get("value")
 v=r if r is not None else g if g is not None else s
 try: return int(v), ("resolved_ceiling" if r is not None else "grok_estimated_ceiling" if g is not None else "source_ceiling")
 except Exception: return 4,"fallback_B4_due_unresolved_ceiling"

def family(bracket): return "B5_competitive" if bracket>=5 else "B4_resilience"
def suite_rows(bracket): return B5 if bracket>=5 else B4

def build_one(did,e):
 b,src=ceiling(e); fam=family(b); rows=[]
 for i,(sid,kind,w,question,executor) in enumerate(suite_rows(b),1):
  rows.append({"order":i,"id":sid,"kind":kind,"priority_weight":w,"question":question,"executor":executor,"decision_authority":False})
 return {
  "schema_version":1,"deck_id":did,"slug":e["slug"],"canonical_hash":e["canonical_project_list"]["hash"],
  "status":"preregistered","evidence_class":"strategic_judgment","confidence":"high",
  "bracket":{"value":b,"source":src,"suite_family":fam},
  "weight_semantics":"review_priority_only_not_outcome_score",
  "authority":{"can_decide":False,"note":"Stress priority and test results inform later judgment; neither can decide a swap or approval alone."},
  "items":rows,
  "execution_policy":{"simulator_scenario":"paired deterministic perturbation against same-seed baseline","mechanic_module":"use the relevant Step-E bounded module; preserve its declared assumptions and category separation","goldfish_threshold":"read declared readiness metrics only; never relabel as multiplayer win probability","judgment_prompt":"requires later red-team/judgment review; no fake simulator substitute"},
  "limitations":["Priority weights allocate review/testing attention and are never multiplied by outcomes into a deck score.","B5 and B4 intentionally emphasize different failure modes.","Opponent-facing mechanics use only bounded Step-E proxies where implemented.","Judgment-only stresses remain judgment-only until a defensible model exists.","No stress result can approve a deck or independently decide a swap."]
 }

def build():
 reg=load(REG); OUT.mkdir(parents=True,exist_ok=True); rows=[]
 for did,e in sorted(reg["decks"].items(),key=lambda kv:kv[1]["slug"]):
  d=build_one(did,e); dump(OUT/f"{e['slug']}.json",d); rows.append({"deck_id":did,"slug":e["slug"],"bracket":d["bracket"]["value"],"suite_family":d["bracket"]["suite_family"],"items":len(d["items"])})
 dump(OUT/"summary.json",{"schema_version":1,"generated_by":f"scripts/grixis_bracket_stress.py v{VERSION}","decks":rows,"totals":{"decks":len(rows),"B5_competitive":sum(x["suite_family"]=="B5_competitive" for x in rows),"B4_resilience":sum(x["suite_family"]=="B4_resilience" for x in rows)}})
 print(f"bracket-stress: built {len(rows)} preregistered suites")

def check():
 try: import jsonschema
 except ImportError: print("bracket-stress: jsonschema required"); return 1
 reg=load(REG); expected={e["slug"] for e in reg["decks"].values()}; present={p.stem for p in OUT.glob("*.json") if p.name!="summary.json"} if OUT.exists() else set(); problems=[]
 if expected!=present: problems.append(f"coverage mismatch missing={sorted(expected-present)} extra={sorted(present-expected)}")
 schema=load(SCHEMA)
 for did,e in sorted(reg["decks"].items()):
  p=OUT/f"{e['slug']}.json"
  if not p.exists(): continue
  d=load(p)
  for er in jsonschema.Draft202012Validator(schema).iter_errors(d): problems.append(f"{e['slug']}: schema {list(er.path)}: {er.message}")
  if d["canonical_hash"]!=e["canonical_project_list"]["hash"]: problems.append(f"{e['slug']}: canonical hash drift")
  if abs(sum(x["priority_weight"] for x in d["items"])-1)>1e-9: problems.append(f"{e['slug']}: priority weights != 1")
  if any(x["decision_authority"] for x in d["items"]): problems.append(f"{e['slug']}: stress item became decision-capable")
  if d["weight_semantics"]!="review_priority_only_not_outcome_score": problems.append(f"{e['slug']}: weight semantics changed")
 print(f"bracket-stress: {len(present)}/62 suites, {len(problems)} problems")
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
