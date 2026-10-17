#!/usr/bin/env python3
"""Step F batch 70.3: frozen red-team/judgment packets for bracket-specific stresses.

The script *frames* adversarial questions and assembles evidence context; it never answers them. Every review starts
pending with null reviewer/verdict. Script-authored text cannot become a judgment review or a swap decision.
"""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
REG=ROOT/"data/grixis/registry.json"
PACKETS=ROOT/"data/grixis/bracket_stress_packets"
BP=ROOT/"data/grixis/blueprints"
AUDIT=ROOT/"data/grixis/audit"
STRUCT=ROOT/"data/grixis/commander_structure"
OUT=ROOT/"data/grixis/bracket_red_team"
SCHEMA=ROOT/"data/grixis/schemas/bracket_red_team.schema.json"
VERSION=1


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def dump(p,o):
 p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")

def audit_cards(a,disps,roles=()):
 rows=[]
 for s in a.get("slots",[]):
  if s.get("disposition") in disps or (roles and set(s.get("roles",[])) & set(roles)):
   rows.append({"card":s["card"],"disposition":s.get("disposition"),"roles":s.get("roles",[]),"structural_necessity":s.get("structural_necessity"),"decision_support":s.get("decision_support",{}).get("ok"),"graph_refs":s.get("graph_refs",[])[:3],"blueprint_refs":s.get("blueprint_refs",[])[:3]})
 return rows[:30]

def win_context(bp):
 return [{"id":w.get("id"),"kind":w.get("kind"),"cards":w.get("cards",[]),"enablers":w.get("enablers",[]),"evidence_class":w.get("evidence_class"),"confidence":w.get("confidence")} for w in bp.get("win_conditions",[])]

def failure_context(bp):
 return [{"id":x.get("id"),"description":x.get("description"),"mitigations":x.get("mitigations",[]),"evidence_class":x.get("evidence_class"),"confidence":x.get("confidence")} for x in bp.get("failure_modes",[])]

def requirements(bp):
 r=bp.get("requirements",{})
 return {"value":r.get("value",{}),"evidence_class":r.get("evidence_class"),"confidence":r.get("confidence")}

def anti_goals(bp):
 a=bp.get("anti_goals",{})
 return {"value":a.get("value",[]),"evidence_class":a.get("evidence_class"),"confidence":a.get("confidence")}

def prompt_focus(pid,a):
 if pid=="protected_win_red_team":
  return {"audit_roles":["counter","protection","tutor"],"audit_dispositions":["core","strong_retain","weak_retain"],"challenge":"Assume the primary win is identified and opponents hold relevant interaction. Determine whether the deck can assemble, protect, pivot, or recover without relying on generic power-core assumptions."}
 if pid=="repeated_removal_attrition":
  return {"audit_roles":["recursion","draw","ramp"],"audit_dispositions":["core","strong_retain","weak_retain","meta_dependent"],"challenge":"Assume multiple permanent types are answered over several turns. Identify which strategic routes actually rebuild and which collapse after repeated removal."}
 if pid=="pillowfort":
  return {"audit_roles":["removal","wipe"],"audit_dispositions":["core","strong_retain","weak_retain"],"challenge":"Assume combat or targeting is materially constrained. Identify noncombat pivots, answers, and any commander-native route that still functions."}
 if pid=="token_stall":
  return {"audit_roles":["wipe","removal"],"audit_dispositions":["core","strong_retain","weak_retain"],"challenge":"Assume combat lanes are clogged by expendable bodies. Determine whether the deck can progress without favorable combat and whether its removal/wipe plan preserves its own identity engine."}
 if pid=="artifact_enchantment_interaction":
  return {"audit_roles":["removal","counter","wipe"],"audit_dispositions":["core","strong_retain","meta_dependent","weak_retain"],"challenge":"Assume a key artifact/enchantment is removed and an opposing noncreature permanent must be answered. Verify actual answers, recursion/replacement lines, and package fragility."}
 return {"audit_roles":[],"audit_dispositions":["core","strong_retain","weak_retain"],"challenge":a}

def supporting_test_refs(packet):
 refs=[]
 for x in packet["items"]:
  ev=x["evidence"]
  if ev.get("status") in ("reused_existing_test_result","reused_goldfish_readiness"):
   refs.append({"stress_id":x["id"],"source":ev.get("source"),"status":ev.get("status"),"legacy_verdict":ev.get("legacy_verdict")})
 return refs

def build_one(did,e):
 slug=e["slug"]; p=load(PACKETS/f"{slug}.json"); bp=load(BP/f"{slug}.json"); a=load(AUDIT/f"{slug}.json"); st=load(STRUCT/f"{slug}.json")
 judgments=[x for x in p["items"] if x["evidence"]["status"]=="judgment_required"]
 reviews=[]
 for x in judgments:
  f=prompt_focus(x["id"],x["question"])
  reviews.append({
   "id":x["id"],"priority_weight":x["priority_weight"],"question":x["question"],"adversarial_challenge":f["challenge"],
   "evidence_context":{
    "blueprint_failure_modes":failure_context(bp),"blueprint_anti_goals":anti_goals(bp),"blueprint_requirements":requirements(bp),"blueprint_win_conditions":win_context(bp),
    "audit_focus":audit_cards(a,set(f["audit_dispositions"]),set(f["audit_roles"])),
    "commander_structure":{"accepted_role":st["accepted_blueprint_role"],"summary":st["summary"]},
    "supporting_test_refs":supporting_test_refs(p)
   },
   "review_contract":{"required_review_method":"human_or_agent_judgment_not_script","acceptable_evidence_classes":["fact","test_result","strategic_judgment"],"heuristic_only_sufficient":False,"must_address_commander_identity":True,"must_address_bracket_context":True,"may_decide_swap":False},
   "review_status":"pending","reviewer":None,"analysis":None,"verdict":None,"uncertainties":[],"can_decide":False
  })
 return {
  "schema_version":1,"deck_id":did,"slug":slug,"canonical_hash":e["canonical_project_list"]["hash"],"suite_family":p["suite_family"],"bracket":p["bracket"],"status":"red_team_pending","evidence_class":"strategic_judgment","authority":{"can_decide":False,"note":"This packet frames required adversarial reviews; script generation never answers or decides them."},"source_packet":f"data/grixis/bracket_stress_packets/{slug}.json","reviews":reviews,"packet_context":{"failure_modes":len(bp.get("failure_modes",[])),"audit_slots":len(a.get("slots",[])),"commander_role":st["accepted_blueprint_role"]["level"]},"limitations":["Evidence context is assembled mechanically and may include irrelevant rows; the reviewer must judge relevance.","A pending red-team prompt is not a judgment_review and cannot support an M6 decision.","No script-authored verdict or recommendation is permitted.","Priority weights allocate review attention only.","Later judgment must preserve Commander-first identity and bracket-specific context."]
 }

def build():
 reg=load(REG); OUT.mkdir(parents=True,exist_ok=True); rows=[]
 for did,e in sorted(reg["decks"].items(),key=lambda kv:kv[1]["slug"]):
  d=build_one(did,e); dump(OUT/f"{e['slug']}.json",d); rows.append({"deck_id":did,"slug":e["slug"],"suite_family":d["suite_family"],"pending_reviews":len(d["reviews"])})
 dump(OUT/"summary.json",{"schema_version":1,"generated_by":f"scripts/grixis_bracket_red_team.py v{VERSION}","decks":rows,"totals":{"decks":len(rows),"pending_reviews":sum(x["pending_reviews"] for x in rows),"B5_reviews":sum(x["pending_reviews"] for x in rows if x["suite_family"]=="B5_competitive"),"B4_reviews":sum(x["pending_reviews"] for x in rows if x["suite_family"]=="B4_resilience")}})
 print(f"bracket-red-team: built {len(rows)} packets")

def check():
 try: import jsonschema
 except ImportError: print("bracket-red-team: jsonschema required"); return 1
 reg=load(REG); schema=load(SCHEMA); expected={e["slug"] for e in reg["decks"].values()}; present={p.stem for p in OUT.glob("*.json") if p.name!="summary.json"} if OUT.exists() else set(); problems=[]
 if present!=expected: problems.append(f"coverage mismatch missing={sorted(expected-present)} extra={sorted(present-expected)}")
 for did,e in sorted(reg["decks"].items()):
  p=OUT/f"{e['slug']}.json"
  if not p.exists(): continue
  d=load(p)
  for er in jsonschema.Draft202012Validator(schema).iter_errors(d): problems.append(f"{e['slug']}: schema {list(er.path)}: {er.message}")
  if d["canonical_hash"]!=e["canonical_project_list"]["hash"]: problems.append(f"{e['slug']}: canonical hash drift")
  if d["authority"]["can_decide"] is not False: problems.append(f"{e['slug']}: packet became decision-capable")
  for r in d["reviews"]:
   if r["review_status"]!="pending" or r["reviewer"] is not None or r["analysis"] is not None or r["verdict"] is not None: problems.append(f"{e['slug']}:{r['id']}: script pre-answered judgment")
   if r["can_decide"] is not False or r["review_contract"]["may_decide_swap"] is not False: problems.append(f"{e['slug']}:{r['id']}: review packet became decision-capable")
 print(f"bracket-red-team: {len(present)}/62 packets, {len(problems)} problems")
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
