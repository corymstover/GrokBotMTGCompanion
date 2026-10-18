#!/usr/bin/env python3
"""Cycle110 paired source-derived causal ledger for three Abaddon slot candidates.

This is a COMMON INITIAL BOARD overlay on exact Cycle106/109 matched seeds.
It is not a new full balanced opponent-game simulator. No scalar utility
or end-to-end card strength inference can be drawn from dissimilar effects.
"""
from __future__ import annotations
import argparse,hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_common_board_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
REG=ROOT/"data/grixis/registry.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_common_board_01.json"
SMALL=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_common_board_summary_01.json"
SLOTS=("Bituminous Blast","Heartless Hidetsugu","Tree of Perdition")
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,
      "can_decide":False,"can_certify_M6":False}
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def digest(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def fmt(a):return json.dumps(a,sort_keys=True,ensure_ascii=False,indent=2)+"\n"
def normalized_opening(rec):
 return ["__PAIRED_SLOT__" if name in SLOTS else name for name in rec["opening"]]
def candidate_leaf(row,name):
 o=row["observations"]
 profiles=o.get("first_activation_profiles")
 if o["slot_cast"]!=bool(o["slot_cast_turn"]):
  raise ValueError("Candidate source-cast contradictory "+name)
 if profiles is None and o["slot_activation_turn"] is not None:
  raise ValueError("Activation turn without branch receipts")
 if profiles is not None:
  if len(profiles)!=3 or [q["profile"] for q in profiles]!=[
     "no_interference","remove_source_before_first_activation",
     "remove_source_after_ability_on_stack"]:
   raise ValueError("Conditional opponent policy labels changed")
  if not o["slot_cast"] or o["slot_activation_turn"]<=o["slot_cast_turn"]:
   raise ValueError("Activation before legally cast no-haste creature")
  keep,pre,post=profiles
  if not keep["activated"] or not keep["resolved"]:
   raise ValueError("No-response candidate branch cannot resolve")
  if pre["activated"] or pre["resolved"] or pre["opponents_lost"]!=0:
   raise ValueError("Source removed before tap illegally activated")
  if name=="Heartless Hidetsugu":
   if keep["opponents_lost"]!=sum([40//2,39//2,31//2]):
    raise ValueError("Heartless fixture opponent damage drift")
   if not post["resolved"] or post["opponents_lost"]!=keep["opponents_lost"]:
    raise ValueError("Heartless ability must survive source removal on stack")
   if keep["pilot_damage"]<=0:raise ValueError("Self damage excluded")
  elif name=="Tree of Perdition":
   if keep["opponents_lost"]!=27 or keep["target_life_after"]!=13:
    raise ValueError("Tree fixture opponent life-exchange drift")
   if post["resolved"] or post["opponents_lost"]!=0:
    raise ValueError("Tree removed before exchange must fail")
  if keep["followup_held_source_payable"] not in (
      "NO","YES_but_granted_cascade_unknown"):
   raise ValueError("Unmodeled candidate followup promoted")
 else:
  keep=pre=post=None
 return {
  "slot_seen":bool(o["slot_seen"]),
  "source_payable_held":bool(o["slot_held_and_mana_affordable"]),
  "source_paid_creature_cast":bool(o["slot_cast"]),
  "cast_turn":o["slot_cast_turn"],
  "conditional_no_haste_tap_turn":o["slot_activation_turn"],
  "conditional_no_response_tap_resolved":bool(keep and keep["resolved"]),
  "opponent_3_3_alive_after_slot_outcome":True,
  "conditional_opponent_life_lost_on_tap":keep["opponents_lost"] if keep else 0,
  "conditional_controller_self_damage_on_tap":keep["pilot_damage"] if keep else 0,
  "abaddon_on_board_at_conditional_tap":bool(keep and keep["abaddon_present"]),
  "boltwave_or_flame_rift_source_payable_in_hand_at_tap":bool(
     keep and keep["followup_held_source_payable"]=="YES_but_granted_cascade_unknown"),
  "source_removed_before_tap_prevents_activation":bool(pre and not pre["activated"]),
  "source_removed_after_ability_is_on_stack_still_resolves":bool(post and post["resolved"]),
  "source_removed_after_ability_conditional_opponent_loss":post["opponents_lost"] if post else None,
  "candidate_followup_actual_cast_and_effect":"UNMODELED",
  "three_other_opponent_decisions_or_full_board":"UNMODELED"}

def blast_leaf(replay,prior,policy):
 if replay["seed"]!=prior["seed"] or replay["opening"]!=prior["opening"]:
  raise ValueError("Original Blast sampled hand or seed drift")
 if replay["blast_cast"]!=prior["blast_cast"]:
  raise ValueError("Original physical Blast cast changed")
 if replay["trigger_count"]!=replay["triggers_resolved"]:
  raise ValueError("Unresolved source cascade frame")
 effects=replay["executed_hit_spells"]
 unknown=replay["declined_unknown_hits"]
 offers=replay["cascade_offers"]
 if len(effects)+len(unknown)!=len(offers) or any(not x["resolved"] for x in effects):
  raise ValueError("Offered physical cascade spell effect accounting drift")
 death=replay["blast_resolution"]=="REMOVED_EXTERNAL_3_3_BY_FOUR_DAMAGE"
 failed=replay["blast_resolution"]=="FAILED_TO_RESOLVE_TARGET_ILLEGAL"
 if policy=="no_removal" and failed or policy=="target_removed_after_cast" and death:
  raise ValueError("Opponent target policy changed")
 if replay["blast_cast"] and not (death or failed):
  raise ValueError("Blast cast had no valid modeled final resolution")
 if not replay["blast_cast"] and (death or failed or effects or offers):
  raise ValueError("Spell effects appeared with Blast absent")
 if sum(replay["zone_counts"].values())!=100:
  raise ValueError("Baseline physical card IDs not conserved")
 return {
  "slot_seen":bool(prior["offers"] or prior["blast_cast"]), # not universal drawn-in-hand measure
  "source_paid_blast_cast":bool(replay["blast_cast"]),
  "opponent_3_3_alive_after_slot_outcome":not death,
  "opponent_3_3_removed_by_blast":death,
  "scripted_target_removed_before_blast_resolution":failed,
  "cascade_printed_offers":len(offers),
  "actual_cascade_exile_spells_cast_and_resolved":len(effects),
  "actual_cascade_effect_names":[x["name"] for x in effects],
  "unresolved_offered_spell_names":[x["name"] for x in unknown],
  "real_tutor_to_hand_count":sum(x["name"]=="Demonic Tutor" for x in effects),
  "real_tutor_to_top_count":sum(x["name"]=="Vampiric Tutor" for x in effects),
  "real_artifacts_battlefield_count":sum(x["name"] in ("Sol Ring","Mana Vault") for x in effects),
  "rock_colorless_mana_generated_not_used_in_followup":replay["generated_rock_mana_not_spent_in_followup"],
  "mana_vault_upkeep_triggers_not_resolved":replay["mana_vault_upkeeps_unresolved"],
  "actual_followup_spell_from_tutor_or_rock":"NOT_VERIFIED",
  "opponent_life_lost_from_blast_damage_to_creature":0,
  "cascade_card_quality_numeric_value":None}

def compare_one(blast106,heart,tree,blast107,blast109,blast109removed,idx):
 rows=(blast106,heart,tree)
 seeds={r["seed"] for r in rows}|{blast107["seed"],blast109["seed"],blast109removed["seed"]}
 if len(seeds)!=1:raise ValueError("Unpaired seed "+str(idx))
 starts=[normalized_opening(r) for r in rows]+[
  normalized_opening(blast109),normalized_opening(blast109removed)]
 if any(x!=starts[0] for x in starts[1:]):
  raise ValueError("Only the exact replaced slot may differ in opening "+str(idx))
 if blast109["initial_inventory"]!=blast106["physical_inventory"]:
  raise ValueError("Canonical baseline physical inventory mismatch")
 if blast109removed["initial_inventory"]!=blast106["physical_inventory"]:
  raise ValueError("Target removal changed pilot 100 card source")
 if len(blast107["offers"])!=len(blast109["cascade_offers"]):
  raise ValueError("Physical eligible offer count changed")
 for x,y in zip(blast107["offers"],blast109["cascade_offers"]):
  if x["eligible_uid"]!=y["eligible_uid"] or x["eligible_name"]!=y["eligible_name"]:
   raise ValueError("Different physical offer cards after source-controlled replay")
 if blast109["executed_hit_spells"]!=blast109removed["executed_hit_spells"]:
  raise ValueError("Removing creature target altered independent cascade spell outcomes")
 result={"seed":blast106["seed"],"same_initial_7_except_one_slot":True,
  "external_first_opponent_creature":"3/3 abilityless, not a pilot physical card",
  "common_initial_opponent_life":[40,39,31],
  "no_response":{
   "Bituminous Blast":blast_leaf(blast109,blast107,"no_removal"),
   "Heartless Hidetsugu":candidate_leaf(heart,"Heartless Hidetsugu"),
   "Tree of Perdition":candidate_leaf(tree,"Tree of Perdition")},
  "noncomparable_scripted_stress":{
   "Blast_target_3_3_removed_after_cast":blast_leaf(
      blast109removed,blast107 if not blast107["blast_cast"] else {
       **blast107,"blast_cast":blast109removed["blast_cast"],
       "seed":blast107["seed"],"opening":blast107["opening"]}, "target_removed_after_cast"),
   "Heartless_source_removed_before_activation":bool(
     heart["observations"]["first_activation_profiles"] and not heart["observations"]["first_activation_profiles"][1]["activated"]),
   "Tree_source_removed_after_activation_fails_exchange":bool(
     tree["observations"]["first_activation_profiles"] and not tree["observations"]["first_activation_profiles"][2]["resolved"])},
  "comparable_win_outcome":None,"unmodeled_card_utility_not_zero":True}
 # Different-target response scripts are stress tests only, NEVER paired
 # opponent policy probabilities. Their source costs are not modeled.
 return result

def run():
 p=read(PLAN);r=read(REG)
 c106=read(ROOT/p["source_cycle106"])
 c107=read(ROOT/p["source_cycle107"])
 c109=read(ROOT/p["source_cycle109"])
 c105=read(ROOT/p["source_cycle105"])
 if (p["cycle"]!=110 or p["status"]!="preregistered_before_implementation"
  or p["authority"]!=AUTH or p["samples"]!=240
  or p["slots"]!=list(SLOTS) or p["seed"]!=106017
  or digest(SOURCE)!="sha256:"+p["approved_source_txt_sha256"]
  or c106["approved_raw_sha256"]!=p["approved_raw_sha256"]
  or c109["approved_raw_sha256"]!=p["approved_raw_sha256"]
  or c105["ready_for_any_card_swap"] or len(r["decks"])!=62
  or r["program"]["milestones"]["M6"]["status"]!="in_progress"):
  raise ValueError("Cycle110 plan, provenance or authority drift")
 b=c106["variants"]["Bituminous Blast"]["trials"]
 h=c106["variants"]["Heartless Hidetsugu"]["trials"]
 t=c106["variants"]["Tree of Perdition"]["trials"]
 seven=c107["policies"]["no_removal"]["trials"]
 base=c109["two_target_response_policies"]["no_removal"]["samples"]
 removed=c109["two_target_response_policies"]["target_removed_after_cast"]["samples"]
 if any(len(a)!=240 for a in (b,h,t,seven,base,removed)):
  raise ValueError("One of the 240 paired cohorts missing")
 records=[];tot=Counter();held=Counter();seeds=set()
 for i in range(240):
  q=compare_one(b[i],h[i],t[i],seven[i],base[i],removed[i],i)
  if q["seed"] in seeds:raise ValueError("Duplicate paired seed")
  seeds.add(q["seed"])
  records.append(q)
  for name,details in q["no_response"].items():
   if name=="Bituminous Blast":
    tot["blast_casts"]+=int(details["source_paid_blast_cast"])
    tot["baseline_threat_3_3_removed"]+=int(details["opponent_3_3_removed_by_blast"])
    tot["baseline_real_cascade_spell_resolutions"]+=details["actual_cascade_exile_spells_cast_and_resolved"]
    tot["baseline_unknown_hit_offers"]+=len(details["unresolved_offered_spell_names"])
    tot["baseline_mana_generated_not_spent"]+=details["rock_colorless_mana_generated_not_used_in_followup"]
    tot["baseline_unresolved_mana_vault_upkeeps"]+=details["mana_vault_upkeep_triggers_not_resolved"]
   else:
    token="heartless" if name=="Heartless Hidetsugu" else "tree"
    tot[token+"_cast"]+=int(details["source_paid_creature_cast"])
    tot[token+"_conditional_tap"]+=int(details["conditional_no_response_tap_resolved"])
    tot[token+"_tap_abaddon_on_board"]+=int(details["conditional_no_response_tap_resolved"] and details["abaddon_on_board_at_conditional_tap"])
    tot[token+"_activation_opponent_life_lost_conditional"]+=details["conditional_opponent_life_lost_on_tap"]
    tot[token+"_self_damage_conditional"]+=details["conditional_controller_self_damage_on_tap"]
    tot[token+"_followup_source_payable"]+=int(details["boltwave_or_flame_rift_source_payable_in_hand_at_tap"])
    if details["opponent_3_3_alive_after_slot_outcome"] is not True:
     raise ValueError("Candidate ability incorrectly removed shared external creature")
 if not (tot["blast_casts"]==7 and tot["baseline_threat_3_3_removed"]==7
         and tot["baseline_real_cascade_spell_resolutions"]==4
         and tot["baseline_unknown_hit_offers"]==3
         and tot["heartless_cast"]==7 and tot["heartless_conditional_tap"]==4
         and tot["tree_cast"]==19 and tot["tree_conditional_tap"]==16):
  raise ValueError("C106/C109 accepted bounded evidence unexpectedly drifted")
 return {"schema_version":1,"cycle":110,
   "stage":"M6_Abaddon_matched_common_board_role_vector_reconciliation",
   "plan_sha256":digest(PLAN),"source_approved_hash":p["approved_raw_sha256"],
   "source_C106_sha256":digest(ROOT/p["source_cycle106"]),
   "source_C107_sha256":digest(ROOT/p["source_cycle107"]),
   "source_C109_sha256":digest(ROOT/p["source_cycle109"]),
   "common_initial_opponent_board":{
      "creature":"one abilityless opposing 3/3 under first opponent control",
      "opponent_life":[40,39,31]},
   "comparison_type":"SAME_SEED_INITIAL_HAND_AND_BOARD_SOURCE_RECONCILIATION_NOT_FULL_BALANCED_EFFECT_PLAY",
   "paired_seeds":240,"cohort_count":3,"aggregate_conditioned_role_vectors":dict(sorted(tot.items())),
   "paired_records":records,
   "stress_responses_are_not_equal_opponent_actions":True,
   "relative_deck_strength":"CANNOT_EVALUATE",
   "could_approve_any_swap":False,"could_certify_zero_improvement":False,
   "phase_b_complete":False,"formal_independent_review_complete":False,
   "M6_accepted":False,
   "blockers":["No shared opponent response spell costs, threat priorities or realistic timing; stress policies have different targets",
      "No value scale for 3/3 removal and four resolved cascade effects against life-loss/tap effect and pilot self damage",
      "Only Boltwave or Flame Rift supported for candidate follow-up, none source-payable at tested activation; other hand effects unmodeled",
      "No actual post-tutor spell cast or rock-generated mana spent, plus three unknown cascade offered effects",
      "Different post-cascade tutor library states preclude matching identical later card draws, though starting seeds/hands are preserved",
      "No full deck multiplayer pressure or relative win/power metric"],
   "next_M6_execution_priority":"Independent skeptical reviewer on Abaddon no-improvement/hold decision; then broaden first-pass 62-deck commander-specific candidate review rather than infinite one-commander card-effect patches",
   "authority":AUTH}
def compact(j):
 return {"cycle":j["cycle"],"paired_seeds":j["paired_seeds"],
  "role_vector":j["aggregate_conditioned_role_vectors"],
  "relative_deck_strength":j["relative_deck_strength"],
  "comparison_type":j["comparison_type"],
  "stronger_deck_demonstrated":False,"M6_accepted":False}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--build",action="store_true");ap.add_argument("--check",action="store_true")
 a=ap.parse_args()
 if not(a.build or a.check):ap.error("require --build or --check")
 x=run();full=fmt(x);sm=fmt(compact(x))
 if a.build:
  OUT.parent.mkdir(parents=True,exist_ok=True)
  OUT.write_text(full,encoding="utf-8");SMALL.write_text(sm,encoding="utf-8")
 if a.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=full or not SMALL.exists() or SMALL.read_text(encoding="utf-8")!=sm):
  raise ValueError("C110 240 common board pairs cannot be reproduced")
 print("Cycle110 same 240 starting states; common 3/3 fate and conditional role vectors; NO relative strength verdict",flush=True)
if __name__=="__main__":main()
