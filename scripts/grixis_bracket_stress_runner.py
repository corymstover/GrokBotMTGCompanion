#!/usr/bin/env python3
"""Step F batch 70.2: route each preregistered bracket stress item to existing evidence without fake simulation.

Cache-independent paths reuse committed M3 stress records and audit goldfish readiness. Step-E mechanic items are
resolved to actual module specifications but remain pending deck-level/local evaluation; judgment prompts stay pending
judgment. No priority weight is applied to an outcome and no aggregate deck/stress score is produced.
"""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
REG=ROOT/"data/grixis/registry.json"
SUITES=ROOT/"data/grixis/bracket_stress"
STRESS=ROOT/"data/grixis/stress"
AUDIT=ROOT/"data/grixis/audit"
MODULES=ROOT/"data/grixis/mechanics/modules.json"
OUT=ROOT/"data/grixis/bracket_stress_packets"
SCHEMA=ROOT/"data/grixis/schemas/bracket_stress_packet.schema.json"
VERSION=1

# 70.1 used this conceptual executor alias before the exact Step-E IDs were rechecked. Preserve the frozen suite string,
# but resolve it transparently here instead of silently pretending it is a module id.
MODULE_ALIASES={
 "counterspell_stack_protection":["counterspell_density","stack_protection"],
 "stax_tax":["stax_tax"],
}

def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def dump(p,o):
 p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")

def module_index(): return {m["id"]:m for m in load(MODULES)["modules"]}

def stress_record(slug,scenario):
 d=load(STRESS/f"{slug}.json")
 return next((r for r in d["records"] if r.get("scenario","").split("@")[0]==scenario),None)

def stress_evidence(slug,item):
 r=stress_record(slug,item["executor"])
 if r is None:
  return {"status":"missing_required_evidence","source":f"data/grixis/stress/{slug}.json","scenario":item["executor"]}
 metric=r["preregistered"]["metric"]
 primary=next((x for x in r["results"] if x["metric"]==metric),None)
 recovery=[x for x in r.get("scenario_metrics",[]) if x["metric"] in ("event_fired_share","commander_recast_share","recovery_turns","recovered_within_2_turns_share")]
 return {"status":"reused_existing_test_result","source":f"data/grixis/stress/{slug}.json#{r['id']}","record_id":r["id"],"scenario":r["scenario"],"legacy_preregistered":r["preregistered"],"legacy_verdict":r["verdict"],"primary_result":primary,"recovery_metrics":recovery,"evidence_class":"test_result","reuse_note":"Existing M3 paired stress evidence is reused under the Step-F bracket priority; its original preregistration, model and limitations are not rewritten."}

def turbo_evidence(slug):
 a=load(AUDIT/f"{slug}.json"); m=a["baseline_sim"]["metrics"]
 return {"status":"reused_goldfish_readiness","source":f"data/grixis/audit/{slug}.json#baseline_sim","evidence_class":"test_result","simulator":a["baseline_sim"]["simulator"],"samples":a["baseline_sim"]["samples"],"combo_assembled_by_turn":m.get("combo_assembled_by_turn",{}),"win_turn_proxy_by_turn":m.get("win_turn_proxy_by_turn",{}),"commander_cast_by_turn":m.get("commander_cast_by_turn",{}),"note":"These are one-player goldfish readiness/access proxies from the canonical baseline, never multiplayer win probability or a bracket pass/fail by themselves."}

def module_evidence(item,mods):
 requested=item["executor"]; ids=MODULE_ALIASES.get(requested,[requested]); found=[mods[x] for x in ids if x in mods]; missing=[x for x in ids if x not in mods]
 if missing:
  return {"status":"missing_module","requested_executor":requested,"resolved_module_ids":ids,"missing":missing}
 return {"status":"pending_deck_level_module_execution","requested_executor":requested,"resolved_module_ids":ids,"source":"data/grixis/mechanics/modules.json","evidence_class":"test_result","modules":[{"id":m["id"],"version":m["version"],"family":m["family"],"confidence":m["confidence"],"models":m["models"],"does_not_model":m["does_not_model"],"limitations":m["limitations"],"metrics":m["metrics"]} for m in found],"note":"Step-E modules exist and are routed, but no canonical-deck result is fabricated from swap-level/readiness machinery. Execute in the frozen local environment or consume a future deck-level result."}

def judgment_evidence(item):
 return {"status":"judgment_required","question":item["question"],"evidence_class":"strategic_judgment","automated_verdict":None,"note":"No automated substitute is allowed for this adversarial prompt."}

def build_one(did,e,mods=None):
 slug=e["slug"]; suite=load(SUITES/f"{slug}.json"); mods=mods or module_index(); rows=[]
 for item in suite["items"]:
  if item["kind"]=="simulator_scenario": ev=stress_evidence(slug,item)
  elif item["kind"]=="goldfish_threshold": ev=turbo_evidence(slug)
  elif item["kind"]=="mechanic_module": ev=module_evidence(item,mods)
  elif item["kind"]=="judgment_prompt": ev=judgment_evidence(item)
  else: ev={"status":"unsupported_executor_kind"}
  rows.append({"id":item["id"],"kind":item["kind"],"priority_weight":item["priority_weight"],"question":item["question"],"preregistered_executor":item["executor"],"evidence":ev,"decision_authority":False})
 return {"schema_version":1,"deck_id":did,"slug":slug,"canonical_hash":e["canonical_project_list"]["hash"],"suite_family":suite["bracket"]["suite_family"],"bracket":suite["bracket"],"suite_source":f"data/grixis/bracket_stress/{slug}.json","status":"evidence_routed","evidence_class":"derived_metric","authority":{"can_decide":False,"note":"The packet routes preregistered stresses to evidence or pending review; it never aggregates outcomes or decides swaps."},"weight_semantics":suite["weight_semantics"],"items":rows,"aggregate_score":None,"limitations":["Existing M3 stress records are reused rather than silently rerun under new thresholds.","Goldfish readiness is not multiplayer win probability.","Step-E mechanic modules remain bounded/readiness proxies and may require local deck-level execution.","Judgment prompts remain unanswered by automation.","Priority weights allocate attention only and are not outcome weights."]}

def build():
 reg=load(REG); mods=module_index(); OUT.mkdir(parents=True,exist_ok=True); rows=[]
 for did,e in sorted(reg["decks"].items(),key=lambda kv:kv[1]["slug"]):
  d=build_one(did,e,mods); dump(OUT/f"{e['slug']}.json",d)
  counts={}
  for x in d["items"]: counts[x["evidence"]["status"]]=counts.get(x["evidence"]["status"],0)+1
  rows.append({"deck_id":did,"slug":e["slug"],"suite_family":d["suite_family"],"statuses":counts})
 dump(OUT/"summary.json",{"schema_version":1,"generated_by":f"scripts/grixis_bracket_stress_runner.py v{VERSION}","decks":rows,"totals":{"decks":len(rows)}})
 print(f"bracket-stress-runner: built {len(rows)} routed packets")

def check():
 try: import jsonschema
 except ImportError: print("bracket-stress-runner: jsonschema required"); return 1
 reg=load(REG); schema=load(SCHEMA); mods=module_index(); expected={e["slug"] for e in reg["decks"].values()}; present={p.stem for p in OUT.glob("*.json") if p.name!="summary.json"} if OUT.exists() else set(); problems=[]
 if present!=expected: problems.append(f"coverage mismatch missing={sorted(expected-present)} extra={sorted(present-expected)}")
 for did,e in sorted(reg["decks"].items()):
  p=OUT/f"{e['slug']}.json"
  if not p.exists(): continue
  d=load(p)
  for er in jsonschema.Draft202012Validator(schema).iter_errors(d): problems.append(f"{e['slug']}: schema {list(er.path)}: {er.message}")
  if d["canonical_hash"]!=e["canonical_project_list"]["hash"]: problems.append(f"{e['slug']}: canonical hash drift")
  if d["authority"]["can_decide"] is not False: problems.append(f"{e['slug']}: packet became decision-capable")
  if d.get("aggregate_score") is not None: problems.append(f"{e['slug']}: aggregate stress score forbidden")
  if abs(sum(x["priority_weight"] for x in d["items"])-1)>1e-9: problems.append(f"{e['slug']}: weights drifted")
  for x in d["items"]:
   st=x["evidence"]["status"]
   if st in ("missing_required_evidence","missing_module","unsupported_executor_kind"): problems.append(f"{e['slug']}:{x['id']}: {st}")
   if x["kind"]=="judgment_prompt" and st!="judgment_required": problems.append(f"{e['slug']}:{x['id']}: judgment prompt auto-resolved")
   if x["kind"]=="mechanic_module" and st!="pending_deck_level_module_execution": problems.append(f"{e['slug']}:{x['id']}: module route status {st}")
 print(f"bracket-stress-runner: {len(present)}/62 packets, {len(problems)} problems")
 for p in problems[:50]: print("FAIL",p)
 return 1 if problems else 0

def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument("--build",action="store_true"); a.add_argument("--check",action="store_true"); a.add_argument("--deck"); x=a.parse_args(argv); rc=0
 if x.deck:
  reg=load(REG); did,e=next((did,e) for did,e in reg["decks"].items() if e["slug"]==x.deck); print(json.dumps(build_one(did,e),indent=2,sort_keys=True))
 if x.build: build()
 if x.check: rc|=check()
 if not (x.deck or x.build or x.check): a.print_help()
 return rc
if __name__=="__main__": sys.exit(main())
