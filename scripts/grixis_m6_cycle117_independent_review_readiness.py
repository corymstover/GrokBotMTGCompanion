#!/usr/bin/env python3
"""Cycle117: audit 15 authored reviews and prepare three falsifiable independent-review packets.

No external reviewer was recruited; no games simulated; never certifies Pass C or M6.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG=ROOT/"data/grixis/registry.json"
READINESS=ROOT/"data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json"
PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle117_independent_review_readiness_01.json"
PROTO=ROOT/"data/grixis/m6/independent_review_intake/cycle117_counterfactual_protocols_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle117_review_readiness_receipt_01.json"
SOURCES={
 112:"data/grixis/m6/author_reviews/cycle112_three_commander_authored_judgments_01.json",
 113:"data/grixis/m6/author_reviews/cycle113_three_commander_review_01.json",
 114:"data/grixis/m6/author_reviews/cycle114_three_commander_reviews_01.json",
 115:"data/grixis/m6/author_reviews/cycle115_three_commander_reviews_01.json",
 116:"data/grixis/m6/author_reviews/cycle116_commander_first_reviews_01.json",
}
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,"can_certify_M6":False,
      "can_issue_independent_pass_c":False,"can_claim_phase_b_performance":False}
SHA64=lambda s:isinstance(s,str) and len(s)==64 and all(c in "0123456789abcdef" for c in s)
def read(path):return json.loads(Path(path).read_text(encoding="utf-8"))
def digest(path):return "sha256:"+hashlib.sha256(Path(path).read_bytes()).hexdigest()
def serialized(d):return json.dumps(d,sort_keys=True,ensure_ascii=False,indent=2)+"\n"
def source_rows():
 rows=[]
 for n,path in SOURCES.items():
  file=ROOT/path
  d=read(file)
  if d["cycle"]!=n:raise ValueError("Wrong original author cycle "+str(n))
  a=d.get("reviews",d.get("items"))
  if not isinstance(a,list) or len(a)!=3:raise ValueError("Author batch count drift "+str(n))
  for item in a:
   row={
    "deck_id":item["deck_id"],
    "author_cycle":n,
    "source_path":path,
    "source_sha256":digest(file),
    "commander":item["commander"],
    "approved_raw_sha256":item.get("approved_raw_sha256",item.get("approved_sha256")),
    "swap_id":item.get("m5_swap_id",item.get("swap_id",item.get("source_swap_id"))),
    "add":item.get("add",item.get("proposed_add")),
    "cut":item.get("cut",item.get("proposed_cut")),
    "author_disposition":item.get("disposition",item.get("verdict")),
   }
   if any(row[k] is None for k in ("deck_id","commander","approved_raw_sha256","swap_id","add","cut","author_disposition")):
    raise ValueError("Incomplete original author record: "+row["deck_id"])
   if not SHA64(row["approved_raw_sha256"]):
    raise ValueError("Missing SHA256 for original author record")
   # A false direct independent claim is not allowed in these author-only sources.
   for key in ("independent_review","independent_pass_c_completed","formal_pass_c"):
    if item.get(key) not in (None,False,0):
     raise ValueError("Original author review is misrepresented as independent")
   for key in ("swap_applied","list_modified","proposed_change_approved","performance_modeling_completed"):
    if item.get(key) not in (None,False,0):
     raise ValueError("Author record falsely claims deck change or measured performance")
   if item.get("approved_swaps",0)!=0:
    raise ValueError("Author review claims owner-authorized card change")
   rows.append(row)
 return rows

def validate_protocols(obj,rows):
 if (obj["schema_version"]!=1 or obj["cycle"]!=117 or
     obj["status"]!="PREREGISTERED_NO_RESULTS" or
     obj["independent_reviewer_assignment"] is not None or
     obj["reviewer_independence_certified"] is not False or
     obj["observed_game_results"]!=[] or
     obj["phase_b_completed"] or obj["formal_independent_pass_c_completed"]):
  raise ValueError("Counterfactual protocols cannot masquerade as completed independent review")
 claims=obj["no_approval_authority"]
 if set(claims)!={"can_apply_card_swap","can_accept_M6","can_certify_pass_c"} or any(claims.values()):
  raise ValueError("No authority may be conferred by scenario packets")
 by_id={r["deck_id"]:r for r in rows}
 spec={}
 for item in obj["protocols"]:
  did=item["deck_id"]
  if did in spec or did not in by_id or item["source_cycle"]!=by_id[did]["author_cycle"]:
   raise ValueError("Counterfactual protocol not backed by a distinct author review")
  if (item["source_swap_id"]!=by_id[did]["swap_id"] or
      item["baseline"]!=by_id[did]["cut"] or item["candidate"]!=by_id[did]["add"]):
   raise ValueError("Counterfactual protocol source candidate did not match")
  if (item["effect_aware_engine_proven"] or item["same_seed_actual_results"] is not None or
      item["minimum_real_observations_for_provisional_comparison"]!=0):
   raise ValueError("Hypothetical scenarios falsely counted as observed game evidence")
  sc=item["scenarios"]
  if (len(sc)!=2 or {s["kind"] for s in sc}!={"favorable_candidate","adverse_candidate"}
      or len({s["id"] for s in sc})!=2):
   raise ValueError("Must prereg one favorable and one adverse scenario per candidate")
  for s in sc:
   if (not s["setup"] or not s["actions_to_trace"] or not s["compare_to_baseline"] or
       not s["hard_checks"] or len(s["outcome_fields"])<3):
    raise ValueError("Missing falsifiable scenario and paired baseline")
  spec[did]=len(sc)
 wanted={"Gwendlyn_Di_Corci","Nicol_Bolas__the_Ravager","Mai_and_Zuko"}
 if set(spec)!=wanted or sum(spec.values())!=6:
  raise ValueError("Three established promising cases / six paired scenarios required")
 if any(v is not None for v in obj["required_reviewer_response"].values()):
  raise ValueError("No independent reviewer has completed this protocol")
 return spec

def audit():
 p=read(PLAN);proto=read(PROTO);registry=read(REG);tri=read(READINESS)
 if (p["cycle"]!=117 or p["status"]!="preregistered_before_engineering_or_evaluation" or
     p["authority"]!=AUTH or p["scope"]["author_review_cycles"]!=list(SOURCES) or
     p["scope"]["expected_reviews"]!=15 or len(registry["decks"])!=62 or
     registry["program"]["milestones"]["M6"]["status"]!="in_progress" or
     registry["program"]["milestones"]["M6"]["accepted_by"] is not None or
     not all(registry["program"]["milestones"][f"M{i}"]["status"]=="accepted" for i in range(6))):
  raise ValueError("Independent gate prereg, authority or baseline drift")
 rows=source_rows()
 if len(rows)!=15 or len({r["deck_id"] for r in rows})!=15:
  raise ValueError("Original 15 distinct named source authors not present")
 tmap={d["deck_id"]:d for d in tri["ordered_decks"]}
 for r in rows:
  did=r["deck_id"]
  if did not in tmap or did not in registry["decks"]:
   raise ValueError("Source deck missing from 62-deck roster")
  meta=registry["decks"][did];q=tmap[did]
  if (meta["source"]["recorded_sha256"]!=r["approved_raw_sha256"] or
      meta["source"]["recorded_matches_raw"] is not True or
      meta["current_canonical_hash"]!=q["source_canonical_logical_hash"]):
   raise ValueError("Original candidate does not match source approved hash and M6 queue: "+did)
  hits=[c for c in q["first_three_TO_REVIEW_NOT_TO_APPLY"] if c["swap_id"]==r["swap_id"]]
  if len(hits)!=1 or (hits[0]["add"],hits[0]["cut"])!=(r["add"],r["cut"]):
   raise ValueError("M5 source candidate drift: "+did)
  if not ("test_pass" in hits[0]["M5_flags"]):
   raise ValueError("M5 test-pass source provenance missing")
 counts={"held_exact_swap":sum(r["author_disposition"]=="HOLD_EXISTING_LIST_NO_SWAP" for r in rows),
         "promising_unresolved":sum(r["author_disposition"]!="HOLD_EXISTING_LIST_NO_SWAP" for r in rows)}
 if counts!={"held_exact_swap":12,"promising_unresolved":3}:
  raise ValueError("Unexpected author disposition distribution")
 experiments=validate_protocols(proto,rows)
 if {(t["deck_id"],t["source_swap_id"]) for t in p["scope"]["target_candidate_experiments"]}!={(d, next(r["swap_id"] for r in rows if r["deck_id"]==d)) for d in experiments}:
  raise ValueError("Experiment registration mismatches source provenance")
 for item in p["scope"]["target_candidate_experiments"]:
  r=next(x for x in rows if x["deck_id"]==item["deck_id"])
  if (item["candidate"]!=r["add"] or item["baseline"]!=r["cut"]):
   raise ValueError("Registered experiment baseline/candidate mismatch")
 return {"schema_version":1,"cycle":117,"stage":"M6_INDEPENDENT_REVIEW_INTAKE_PREPARATION",
   "sources":{str(k):{"path":v,"sha256":digest(ROOT/v)} for k,v in SOURCES.items()},
   "author_review_count":len(rows),"verified_distinct_decks":len({r["deck_id"] for r in rows}),
   "dispositions":counts,"author_rows":rows,
   "counterfactual_protocol_count":len(experiments),"counterfactual_scenario_count":sum(experiments.values()),
   "counterfactual_protocols":experiments,
   "formal_independent_pass_c_count":0,"real_effect_aware_paired_result_count":0,
   "source_current_100_card_legality_recognition_not_recategorized":True,
   "independent_reviewer_assigned":False,"owner_approvals_issued":0,"canonical_decks_modified":0,
   "zero_improvement_certificates_issued":0,"M6_accepted":False,
   "review_outcome_gate":"BLOCKED_PENDING_EXTERNAL_REVIEW_AND_ACTUAL_EFFECT_AWARE_PAIRED_EVIDENCE",
   "first_next_action":"Obtain named reviewer separate from authored judgments, then measured favorable/adverse paired scenario runs; reconcile disagreement before proposing any swap.",
   "registry_sha256":digest(REG),"M6_triage_sha256":digest(READINESS),
   "plan_sha256":digest(PLAN),"protocol_sha256":digest(PROTO),"authority":AUTH}

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("--build",action="store_true");parser.add_argument("--check",action="store_true")
 args=parser.parse_args()
 if not(args.build or args.check):parser.error("Use --build or --check")
 txt=serialized(audit())
 if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(txt,encoding="utf-8")
 if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=txt):
  raise ValueError("Cycle117 evidence contract did not reproduce")
 print("Cycle117: 15 source-locked authors / 3 promising hypotheses / 6 unrun scenarios; NO independent Pass C, Phase B or M6 certification")
if __name__=="__main__":main()
