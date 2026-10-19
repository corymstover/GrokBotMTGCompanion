#!/usr/bin/env python3
"""Cycle124 generate three verdict-neutral independent critic intake packets.

Prepared by the original ChatGPT engineering author. No reviewer has been
assigned. The packets are neutral source material, NOT blinded execution,
independent strategic findings, Pass C certification, Phase B or user approval.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_authority as ga
import grixis_m6_cycle120_physical_access as c120
import grixis_m6_cycle117_independent_review_readiness as c117

PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle124_reviewer_ready_preregistered_01.json"
REG=ROOT/"data/grixis/registry.json"
TRACK=ROOT/"data/grixis/milestone_m6_m7_subtracker.json"
OUT=ROOT/"data/grixis/m6/independent_review_intake/cycle124_reviewer_ready_01.json"
AUTH_KEYS={"can_change_62_canonical_decks","can_approve_swaps",
 "can_self_certify_independent_pass_c","can_complete_phase_b","can_accept_m6_or_m7"}
RESERVED={"author_disposition","author_verdict","source_score","source_rank",
 "proxy_win_rate","recommended_swap","pass_c_completed","conclusion",
 "reviewer_id","reviewer_name","reviewer_signature"}
BASICS={"Plains","Island","Swamp","Mountain","Forest","Wastes"}
CASES={
 "Gwendlyn_Di_Corci":[
 "Explain Gwendlyn's activation turn restriction and when she and Alchemist may tap legally.",
 "Can Aphetto target Gwendlyn when she has Pemmin's Aura shroud? Distinguish aura state choices.",
 "How many *finite* discard activations are possible and what matters if opposing hands empty?",
 "What tutor-control windows and flash-counterplay are lost by cutting Opposition Agent?",
 "Evaluate actual deck-specific untap/haste/discard payoffs versus tutor-disruption needs.",
 "Describe missing source-paid opponent-state trials and a fair unfavorable candidate case."],
 "Nicol_Bolas__the_Ravager":[
 "Explain Ravager ETB, transform cost and sorcery-speed requirement from Oracle.",
 "Trace when Aetheric Amplifier can legally be cast and activate versus Mox Diamond deployment.",
 "Does counter doubling add loyalty abilities or automatically enable a -12 activation? Explain.",
 "Which protected plays require Mox Diamond fast/colored mana, including mandatory land discard?",
 "Assess printed physical-list Bolas/superfriends package dependence and competing speed priorities.",
 "Specify opposing removal/pressure conditions and matched full-game evidence that is absent."],
 "Mai_and_Zuko":[
 "Verify The Enigma Jewel front costs {U}, enters tapped and generates mana only for activated abilities.",
 "Trace one bounded Basalt Monolith/Rings/Jewel stack line without inferring an unbounded mana loop.",
 "Distinguish Mai/Zuko permitting artifact *casting* as flash from activating Jewel's craft.",
 "Explain An Offer's noncreature target legality, priority, two Treasure outcome and when it fizzles.",
 "Contrast immediate counterspell availability with artifact engine upside under the actual 31-land source list.",
 "What actual opponent-stack frequencies, card draw and independent full-effect game trials are missing?"]
}
def read(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(Path(p).read_bytes()).hexdigest()
def enc(o):return json.dumps(o,sort_keys=True,ensure_ascii=False,indent=2)+"\n"
def oracle_card(resolver,name):
 card,fuzzy=resolver.get(name)
 if card is None or fuzzy or card.get("name")!=name:
  raise ValueError("Missing, fuzzy or noncanonical frozen Oracle card: "+name)
 text=card.get("oracle_text") or "\n".join(face.get("oracle_text") or "" for face in card.get("card_faces",[]))
 mana=card.get("mana_cost") or " // ".join(face.get("mana_cost") or "" for face in card.get("card_faces",[]))
 if not text:raise ValueError("Frozen Oracle text unavailable: "+name)
 return {"name":name,"frozen_oracle_text":text,"printed_mana_cost":mana,
   "oracle_text_sha256":"sha256:"+hashlib.sha256(text.encode()).hexdigest(),
   "frozen_2026_10_16_not_current_legality_proof":True}
def blueprint(root,slug,expected):
 path=root/"data/grixis/blueprints"/(slug+".json")
 d=read(path)
 if (d["deck_id"]!=expected["deck_id"] or d["slug"]!=slug or
     d["canonical_hash"]!=expected["source_logical_hash"]):
   raise ValueError("Commander blueprint/logical hash mismatch: "+slug)
 return {"blueprint_sha256":sha(path),
    "commander_first_primary_plan":d["plan"]["value"]["primary"],
    "commander_first_secondary_plan":d["plan"]["value"]["secondary"],
    "source_required_interaction":d["requirements"]["value"]["interaction"],
    "source_anti_goals":d["anti_goals"]["value"],
    "known_project_natural_bracket":d["power"]["source_ceiling"]["value"]["value"]}
def validate_inputs(plan,reg,track,R):
 if (plan["cycle"]!=124 or plan["schema_version"]!=1 or
     plan["status"]!="PREREGISTERED_NO_CRITIC_ASSIGNED" or
     len(plan["cases"])!=3 or len(reg["decks"])!=62 or
     reg["program"]["milestones"]["M6"]["status"]!="in_progress" or
     reg["program"]["milestones"]["M7"]["status"]!="not_started" or
     track["display"]["m6_completed_gates"]!=3 or
     track["display"]["m7_completed_gates"]!=0 or
     track["m6"]["formal_m6_certified_decks"]!=0 or
     set(CASES)!={x["deck_id"] for x in plan["cases"]} or
     any(v is not None and v is not False for v in plan["critic_intake"].values()) or
     plan["reporting"]!={"prepared_cases":3,"formal_pass_c_complete":0,"phase_b_completed":0,
                          "canonical_decks_modified":0,"source_approved_swaps":0,
                          "m6_accepted":False,"m7_started":False}):
   raise ValueError("Source, authority or review-preparation boundary drift")
 authors={x["deck_id"]:x for x in c117.source_rows()}
 for case in plan["cases"]:
  did=case["deck_id"]
  src=reg["decks"][did]
  row=authors[did]
  if (case["slug"]!=src["slug"] or case["source_logical_hash"]!=src["current_canonical_hash"] or
      case["source_raw_sha256"]!=src["source"]["recorded_sha256"] or
      case["source_m5_swap_id"]!=row["swap_id"] or
      case["baseline"]!=row["cut"] or case["candidate"]!=row["add"] or
      case["source_author_cycle"]!=row["author_cycle"] or
      src["source"]["recorded_matches_raw"] is not True or
      ga.text_hash(ga.deck_block_text(src["slug"]),R)!=src["current_canonical_hash"]):
    raise ValueError("Named M5 review, source list or authority hash drift: "+did)

def source_packet(case,reg,R):
 did=case["deck_id"];src=reg["decks"][did];slug=case["slug"]
 text=ga.deck_block_text(slug)
 a,b,slot,original,flags=c120.verify_exact_pair({
   "slug":slug,"cut":case["baseline"],"add":case["candidate"],
   "commander":src["commanders"][0],"approved_logical_hash":case["source_logical_hash"],
   "opportunities":[]},R)
 if (len(a)!=99 or len(b)!=99 or sum(x!=y for x,y in zip(a,b))!=1):
  raise ValueError("Physical library not 99 main/one commander with one swap")
 if any(v>1 and k not in BASICS for k,v in Counter(a).items()):
  raise ValueError("Nonbasic singleton violation")
 anchor=blueprint(ROOT,slug,case)
 cards={name:oracle_card(R,name) for name in [*src["commanders"],case["baseline"],case["candidate"]]}
 return {"deck_id":did,"slug":slug,"commander":src["commanders"],
  "baseline_list_including_commander":[src["commanders"][0],*a],
  "candidate_list_including_commander":[src["commanders"][0],*b],
  "source_approved_raw_sha256_recorded":case["source_raw_sha256"],
  "source_approved_logical_hash":case["source_logical_hash"],
  "baseline_source_block_text_sha256":"sha256:"+hashlib.sha256(text.encode()).hexdigest(),
  "single_different_main_slot":slot,
  "named_m5_swap_id":case["source_m5_swap_id"],
  "option_approved_baseline":case["baseline"],
  "option_one_card_challenger":case["candidate"],
  "archived_oracle":cards,
  "commander_first_requirements_from_existing_blueprint":anchor,
  "six_unanswered_nonleading_review_questions":CASES[did],
  "card_count_each":100,"unchanged_card_slots":98,
  "prior_author_recommendation":None,
  "prior_author_outcome_not_disclosed":True,
  "earlier_simulation_effect_sizes_not_disclosed":True,
  "strict_blind_independent_execution_claimed":False}

def generate():
 plan,reg,tracker=map(read,(PLAN,REG,TRACK))
 R=ev.Resolver()
 validate_inputs(plan,reg,tracker,R)
 packets=[source_packet(x,reg,R) for x in plan["cases"]]
 if len({p["deck_id"] for p in packets})!=3:raise ValueError("Duplicate reviewer packet")
 for pkt in packets:
  if pkt["option_approved_baseline"] not in pkt["baseline_list_including_commander"] or (
      pkt["option_one_card_challenger"] not in pkt["candidate_list_including_commander"]):
    raise ValueError("Candidate source/card presence failure")
  if any(k in pkt for k in RESERVED):raise ValueError("Unqualified reviewer conclusion leaked")
  if any(word in enc(pkt).lower() for word in ["hold_existing_list_no_swap","swap_approved",
                                               "pass_c_complete"]):
    raise ValueError("Author disposition, or false certification leaked into neutral packet")
 return {"cycle":124,"schema_version":1,
   "stage":"M6_REVIEWER_READY_AUTHOR_PREPARED_NOT_INDEPENDENT_PASS_C",
   "preregistered_plan_sha256":sha(PLAN),
   "registry_sha256":sha(REG),"secondary_tracker_sha256":sha(TRACK),
   "archived_oracle_snapshot_sha256":"ea7abac9906633415553b585b32c4071c79d42ba23d7e3163a0c4e9c265a7483",
   "packet_count":3,"packets":packets,
   "critic_response_intake_template":plan["critic_intake"],
   "external_critic_assigned":False,"independence_verified":False,
   "external_critic_findings_observed":0,"formal_pass_c_completed":0,
   "effect_aware_phase_b_completed":0,"owner_approved_swaps":0,
   "canonical_decks_modified":0,"M6_accepted":False,"M7_started":False,
   "bounded_scope":["These source packets are prepared by the same ChatGPT author as Cycles112–123, therefore DO NOT qualify as independent Pass C.",
     "The candidate is plainly named and the repository is readable, so strict author-blindness/independence cannot be certified.",
     "No reviewer response, source-critical analysis, conflicts reconciliation or external reviewer evidence has been received.",
     "No full Phase B/stress multiplayer evaluations, legal-refresh or strategic optimization verdict were generated."]}
def main():
 a=argparse.ArgumentParser();a.add_argument("--build",action="store_true");a.add_argument("--check",action="store_true")
 v=a.parse_args()
 if not(v.build or v.check):a.error("use --build or --check")
 s=enc(generate())
 if v.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(s,encoding="utf-8")
 if v.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=s):
  raise ValueError("Cycle124 packet hash-replay differs")
 print("Cycle124: three source-locked reviewer packets prepared, NO assigned independent critic and NO Pass C.")
if __name__=="__main__":main()
