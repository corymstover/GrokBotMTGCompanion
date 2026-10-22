"""Progress sub-tracker: fail closed on unsupported promotion, not a new milestone authority."""
from pathlib import Path
import json,unittest
ROOT=Path(__file__).resolve().parents[1]
TRACKER=ROOT/"data/grixis/milestone_m6_m7_subtracker.json"
REG=ROOT/"data/grixis/registry.json"
PREF=ROOT/"data/grixis/m6/preflight.json"
SEAL=ROOT/"data/grixis/m6/sealed/reconciliation_manifest.json"
WAIVER=ROOT/"data/grixis/m6/governance/pass_c_owner_waiver_20261021.json"

def validate(t,r,p,s,w=None):
 if w is None:w=json.loads(WAIVER.read_text())
 assert w["decision_type"]=="OWNER_GOVERNANCE_WAIVER"
 assert w["owner"]=="Cory Stover" and w["recorded_local_date"]=="2026-10-21"
 assert "This is my formal waiver." in w["owner_verbatim_response"]
 assert "independent third-model Pass C requirement" in w["question_presented_to_owner"]
 assert w["decision"]=="AUTHORIZE_OWNER_EQUIVALENT_PASS_C_AS_REPLACEMENT_FOR_INDEPENDENT_THIRD_MODEL_REQUIREMENT_FOR_M6_GOVERNANCE"
 assert w["applies_to"]["gate"]=="M6.5" and w["applies_to"]["decks"]==62
 assert w["accepted_substitute"]["final_dispositions_complete"]==62
 assert not w["accepted_substitute"]["technically_independent"]
 assert w["accepted_substitute"]["genuinely_independent_third_model_reviews"]==0
 assert w["scope_and_effect"]["m6_5_governance_condition_satisfied"] is True
 assert not w["scope_and_effect"]["original_independent_review_performed"]
 assert w["scope_and_effect"]["other_m6_gates_remain_independently_required"] is True
 assert all(w["scope_and_effect"][x] is False for x in (
  "effect_aware_phase_b_or_gameplay_proved","m6_milestone_accepted",
  "m8_complete","canonical_decklist_change_authorized","owner_approval_of_any_candidate_swap"))
 assert w["scope_and_effect"]["m7_approved_decks"]==0
 assert t["schema_version"]==1
 assert len(r["decks"])==62 and t["accounting"]["canonical_total"]==62
 assert t["accounting"]["canonical_approved_locked"]==62
 assert t["accounting"]["m8_certified"]==0
 assert r["program"]["milestones"]["M6"]["status"]==t["m6"]["status"]=="in_progress"
 assert r["program"]["milestones"]["M7"]["status"]==t["m7"]["status"]=="not_started"
 assert r["program"]["milestones"]["M6"]["accepted_by"] is None
 assert r["program"]["milestones"]["M7"]["accepted_by"] is None
 assert len(t["m6"]["gates"])==10 and len(t["m7"]["gates"])==6
 assert len({a["id"] for a in t["m6"]["gates"]})==10
 assert len({a["id"] for a in t["m7"]["gates"]})==6
 assert t["display"]["m6_total_gates"]==10 and t["display"]["m7_total_gates"]==6
 assert t["display"]["m6_completed_gates"]==sum(a["status"]=="COMPLETE" for a in t["m6"]["gates"])
 assert t["display"]["m7_completed_gates"]==sum(a["status"]=="COMPLETE" for a in t["m7"]["gates"])
 assert t["display"]["m6_gate_completion_percent"]==100*t["display"]["m6_completed_gates"]/10
 assert t["display"]["m7_gate_completion_percent"]==100*t["display"]["m7_completed_gates"]/6
 assert t["display"]["m6_partial_gates"]==sum(a["status"]=="PARTIAL" for a in t["m6"]["gates"])
 assert t["display"]["m6_unfulfilled_gates"]==10-t["display"]["m6_completed_gates"]
 assert p["counts"]["accepted_m5_input_complete"]==62
 assert s["counts"]["decks"]==62
 assert s["counts"]["deep_review"]==8848
 assert s["pass_c"]["complete"] is False
 assert t["m6"]["gates"][3]["completed"]==62
 assert t["m6"]["gates"][3]["status"]=="COMPLETE"
 case=json.loads((ROOT/"data/grixis/m6/author_reviews/cycle128_six_commander_authored_judgments_01.json").read_text())
 assert case["review_count"]==6 and len(case["rows"])==6 and case["historical_authored_count_before"]==15
 assert case["authored_count_after_if_verified"]==21
 r129=json.loads((ROOT/"data/grixis/m6/author_reviews/cycle129_six_detailed_01.json").read_text())
 assert r129["review_count"]==len(r129["rows"])==6 and r129["authored_if_verified"]==27
 r130=json.loads((ROOT/"data/grixis/m6/author_reviews/cycle130_six_detailed_01.json").read_text())
 assert r130["review_count"]==len(r130["rows"])==6 and r130["authored_if_verified"]==33
 c131=[json.loads((ROOT/f"data/grixis/m6/author_reviews/cycle131_batch_{a}_01.json").read_text()) for a in "abcde"]
 new131=[x for b in c131 for x in b["rows"]]
 assert sum(b["count"] for b in c131)==29 and len(new131)==29
 assert len({x["deck_id"] for x in new131})==29
 assert all(batch["cycle"]==131 for batch in c131)
 assert all(x["approved_swaps"]==0 and not x["formal_pass_c"] and not x["full_phase_b"] for x in new131)
 assert t["display"]["m6_completed_gates"]==5 and t["display"]["m6_partial_gates"]==2
 assert t["m6"]["formal_m6_certified_decks"]==0

 assert len({x["deck_id"] for x in r130["rows"]})==6
 assert all(x["approved_swaps"]==0 and not x["independent_pass_c"] and not x["complete_phase_b"] for x in r130["rows"])
 assert len({x["deck_id"] for x in r129["rows"]})==6
 assert all(x["approved_swaps"]==0 and not x["independent_pass_c"] and not x["complete_phase_b"] for x in r129["rows"])
 assert len({x["deck_id"] for x in case["rows"]})==6
 assert all(x["disposition"]=="HOLD_EXISTING_LIST_NO_SWAP" and x["independent_pass_c_completed"] is False and x["approved_swaps"]==0 for x in case["rows"])
 assert t["m6"]["formal_m6_certified_decks"]==0
 assert t["m7"]["formal_m7_review_decisions"]==0
 assert t["m6"]["gates"][4]["status"]=="COMPLETE" and t["m6"]["gates"][4]["completed"]==62
 assert t["m6"]["gates"][4]["completion_basis"]=="OWNER_AUTHORIZED_NONINDEPENDENT_PASS_C_SUBSTITUTE"
 assert t["m6"]["gates"][4]["waiver_receipt"]==str(WAIVER.relative_to(ROOT))
 assert t["m6"]["gates"][4]["original_independent_requirement"]["technically_completed"]==0
 assert t["m6"]["gates"][4]["original_independent_requirement"]["waived_by_owner"] is True
 assert t["m6"]["gates"][5]["status"]=="PARTIAL" and t["m6"]["gates"][5]["completed"]==0
 assert t["m6"]["gates"][7]["completed"]==0 and t["m6"]["gates"][8]["completed"]==0
 assert t["m7"]["gates"][1]["completed"]==0
 assert len(t["m6"]["phase_b_additional_evidence"])==10
 assert {x["merged_pr"] for x in t["m6"]["phase_b_additional_evidence"]}=={511,512,514,516,518,520,522,524,526,528}
 assert all(x["deck_id"]=="Abaddon_the_Despoiler" and not x["full_multiplayer_gameplay"] and not x["superiority_proven"] for x in t["m6"]["phase_b_additional_evidence"])
 assert t["m6"]["phase_b_additional_evidence"][1]["turn_10"]["assault_for_rakdos"]["individually_payable_snapshots"]==2
 assert t["m6"]["gates"][6]["status"]=="PARTIAL" and t["m6"]["gates"][6]["completed"]==0
 assert t["update_contract"]["prefer_live_registry_and_evidence_over_this_snapshot"]
 assert t["update_contract"]["never_accept_a_milestone_or_modify_canonical_decks_from_tracker_update"]
 for milestone in ("m6","m7"):
  for gate in t[milestone]["gates"]:
   assert gate["status"] in ("COMPLETE","PARTIAL","BLOCKED","NOT_STARTED")
   assert isinstance(gate["title"],str) and gate["title"].strip()
   assert gate["evidence"]
   assert gate["completed"]>=0
   if gate["total"] is not None:assert gate["completed"]<=gate["total"]

class TestMilestoneSubtracker(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.t=json.loads(TRACKER.read_text())
  cls.r=json.loads(REG.read_text())
  cls.p=json.loads(PREF.read_text())
  cls.s=json.loads(SEAL.read_text())
 def test_snapshot_matches_current_engineering_milestones(self):
  validate(self.t,self.r,self.p,self.s)
 def test_false_M6_acceptance_is_rejected(self):
  import copy
  d=copy.deepcopy(self.r)
  d["program"]["milestones"]["M6"]["status"]="accepted"
  with self.assertRaises(AssertionError):validate(self.t,d,self.p,self.s)
 def test_false_independent_pass_c_is_rejected(self):
  import copy
  d=copy.deepcopy(self.s);d["pass_c"]["complete"]=True
  with self.assertRaises(AssertionError):validate(self.t,self.r,self.p,d)
 def test_false_percentage_is_rejected(self):
  import copy
  t=copy.deepcopy(self.t);t["display"]["m6_gate_completion_percent"]=90
  with self.assertRaises(AssertionError):validate(t,self.r,self.p,self.s)
 def test_premature_cycle2_review_claim_is_rejected(self):
  import copy
  t=copy.deepcopy(self.t);t["m7"]["formal_m7_review_decisions"]=62
  with self.assertRaises(AssertionError):validate(t,self.r,self.p,self.s)
 def test_owner_equivalent_pass_c_counts_and_provenance(self):
  source=json.loads((ROOT/"data/grixis/m6/owner_pass_c_substitute/progress.json").read_text())
  record=self.t["m6"]["owner_equivalent_pass_c"]
  self.assertEqual((source["stage_a_complete"],source["stage_b_complete"],source["final_complete"]),(62,62,62))
  self.assertEqual((record["completed"],record["total"]),(62,62))
  self.assertFalse(record["technically_independent"])
  self.assertEqual(record["genuinely_independent_third_model_reviews"],0)
  self.assertFalse(source["technically_independent"])
  self.assertEqual(source["next_pending_deck"],None)
  self.assertEqual(len(source["decks"]),62)
  self.assertTrue(all(x["stage_a_complete"] and x["stage_b_complete"] and x["final_complete"] and x["canonical_unchanged"] for x in source["decks"]))
  self.assertTrue(all(x["owner_swap_approved"] is False for x in source["decks"]))
  observed={"needs_testing":0,"propose_upgrade":0,"keep":0}
  for x in source["decks"]:
   observed[{"NEEDS TESTING":"needs_testing","PROPOSE UPGRADE":"propose_upgrade","KEEP":"keep"}[x["final_disposition"]]]+=1
  self.assertEqual(record["dispositions"],observed)
  self.assertEqual(self.t["m6"]["gates"][4]["status"],"COMPLETE")
  self.assertEqual(self.t["m6"]["gates"][4]["completed"],62)
  self.assertTrue(self.t["m6"]["owner_equivalent_pass_c"]["original_independent_gate_waived_for_m6_governance"])
  self.assertEqual(self.t["m6"]["formal_m6_certified_decks"],0)
  self.assertEqual(self.t["m7"]["formal_m7_review_decisions"],0)
 def test_formal_owner_waiver_is_recorded_without_fake_independence(self):
  w=json.loads(WAIVER.read_text())
  self.assertEqual(w["accepted_substitute"]["stage_a_complete"],62)
  self.assertEqual(w["accepted_substitute"]["stage_b_complete"],62)
  self.assertEqual(w["accepted_substitute"]["final_dispositions_complete"],62)
  self.assertFalse(w["accepted_substitute"]["technically_independent"])
  self.assertEqual(w["accepted_substitute"]["genuinely_independent_third_model_reviews"],0)
  self.assertEqual(self.t["m6"]["gates"][4]["completion_basis"],"OWNER_AUTHORIZED_NONINDEPENDENT_PASS_C_SUBSTITUTE")
  self.assertEqual(self.t["m6"]["gates"][4]["completed"],62)
  self.assertEqual(self.t["m6"]["formal_m6_certified_decks"],0)
 def test_forged_or_overbroad_waiver_is_rejected(self):
  import copy
  w=json.loads(WAIVER.read_text())
  for key,value in (("owner_verbatim_response","No, I reject"),("decision","UNAUTHORIZED")):
   d=copy.deepcopy(w);d[key]=value
   with self.assertRaises(AssertionError):validate(self.t,self.r,self.p,self.s,d)
  for key,value in (("technically_independent",True),("genuinely_independent_third_model_reviews",62)):
   d=copy.deepcopy(w);d["accepted_substitute"][key]=value
   with self.assertRaises(AssertionError):validate(self.t,self.r,self.p,self.s,d)
  d=copy.deepcopy(w);d["scope_and_effect"]["m6_milestone_accepted"]=True
  with self.assertRaises(AssertionError):validate(self.t,self.r,self.p,self.s,d)
 def test_falsifying_original_independence_count_is_rejected(self):
  import copy
  t=copy.deepcopy(self.t)
  t["m6"]["gates"][4]["original_independent_requirement"]["technically_completed"]=62
  with self.assertRaises(AssertionError):validate(t,self.r,self.p,self.s)
 def test_targeted_phase_b_receipt_is_not_certification(self):
  receipt=self.t["m6"]["phase_b_targeted_evidence"]
  self.assertEqual(receipt["deck_id"],"Abaddon_the_Despoiler")
  self.assertEqual(receipt["merged_evidence_pr"],504)
  self.assertTrue((ROOT/receipt["evidence"]).exists())
  self.assertTrue(receipt["real_effects_modeled"])
  self.assertFalse(receipt["is_full_deck_paired_gameplay"])
  self.assertFalse(receipt["proves_swap_superiority"])
  self.assertEqual(receipt["deck_level_phase_b_certificates_issued"],0)
  self.assertEqual((self.t["m6"]["gates"][5]["status"],self.t["m6"]["gates"][5]["completed"]),("PARTIAL",0))
 def test_abaddon_agent_judgments_only_partially_advance_m6_7(self):
  path=ROOT/"data/grixis/m6/judgment_reviews/abaddon_phase_b_decisions_20261021.json"
  d=json.loads(path.read_text())
  self.assertEqual(d["deck_id"],"Abaddon_the_Despoiler")
  self.assertEqual(len(d["candidates"]),4)
  self.assertTrue(all(not c["approved_swap"] for c in d["candidates"]))
  self.assertTrue(all(v is False for v in d["authority"].values()))
  gate=self.t["m6"]["gates"][6]
  self.assertEqual((gate["status"],gate["completed"]),("PARTIAL",0))
  self.assertTrue(any("abaddon_phase_b_decisions_20261021.json" in x for x in gate["evidence"]))
  self.assertEqual(self.t["display"]["m6_partial_gates"],2)
  self.assertEqual(self.t["m6"]["formal_m6_certified_decks"],0)
 def test_new_ruinous_and_assault_land_only_receipts_remain_bounded(self):
  records=self.t["m6"]["phase_b_additional_evidence"]
  r,a,chron,warp,ignus,paid,hit,shared,hand,stack=records
  self.assertEqual((r["merged_pr"],a["merged_pr"],chron["merged_pr"],warp["merged_pr"],ignus["merged_pr"],paid["merged_pr"],hit["merged_pr"],shared["merged_pr"],hand["merged_pr"],stack["merged_pr"]),(511,512,514,516,518,520,522,524,526,528))
  self.assertEqual(r["deterministic_tests"],14)
  self.assertEqual(a["unit_tests"],11)
  self.assertEqual(chron["unit_tests"],15)
  self.assertEqual(chron["samples_per_variant"],2000)
  self.assertFalse(chron["full_multiplayer_gameplay"])
  self.assertFalse(chron["superiority_proven"])
  self.assertFalse(chron["net_deck_performance_comparison"])
  self.assertTrue(chron["physical_tap_costs_paid"])
  self.assertIsNone(chron["true_game_win_rate"])
  self.assertEqual(chron["turn_10"]["assault_for_rakdos"]["first_assault_activation_paid"],1)
  self.assertEqual(chron["turn_10"]["assault_for_lost"]["first_assault_activation_paid"],4)
  self.assertTrue((ROOT/chron["evidence"]).is_file())
  self.assertTrue((ROOT/chron["preregistration"]).is_file())
  self.assertEqual(stack["new_unit_tests"],15)
  self.assertEqual(stack["predecessor_regression_tests"],20)
  self.assertEqual(stack["conditional_opponent_windows"],8)
  self.assertTrue(stack["witnesses"]["quiet_board_ignus_return_is_no_stack_mana_ability"])
  self.assertFalse(stack["witnesses"]["can_respond_to_ignus_bounce_activation"])
  self.assertEqual(stack["witnesses"]["uncontested_paid_recasts"],5)
  self.assertEqual(stack["witnesses"]["uncontested_abaddon_cascades"],5)
  self.assertFalse(stack["witnesses"]["rule_of_law_after_prior_spell_initial_cast"])
  self.assertFalse(stack["witnesses"]["rule_of_law_first_ignus_free_cascade_cast"])
  self.assertFalse(stack["witnesses"]["drannith_free_cascade_cast"])
  self.assertEqual(stack["witnesses"]["drannith_ignus_paid_hand_recasts"],5)
  self.assertEqual(stack["witnesses"]["abaddon_removed_next_cascades"],0)
  self.assertEqual(stack["witnesses"]["birgi_removed_next_recasts"],1)
  self.assertTrue(stack["witnesses"]["countered_initial_ignus_cascade_persists"])
  self.assertFalse(stack["witnesses"]["countered_original_ignus_does_not_enter"])
  self.assertTrue(stack["prearranged_board_not_empirical_probability"])
  self.assertFalse(stack["actual_opp_spell_simulation"])
  self.assertFalse(stack["full_multiplayer_gameplay"])
  self.assertFalse(stack["superiority_proven"])
  self.assertIsNone(stack["measured_win_rate"])
  self.assertFalse(stack["canonical_changed"])
  for key in ("preregistration","evidence"):
   self.assertTrue((ROOT/stack[key]).is_file())
  self.assertEqual(hand["unit_tests"],15)
  self.assertEqual(hand["physical_variants"],5)
  self.assertEqual(hand["policies"],2)
  self.assertEqual(hand["control_modes"],2)
  self.assertEqual(hand["samples_per_variant_policy_mode"],1000)
  self.assertEqual(hand["total_paired_trajectories"],20000)
  self.assertEqual(hand["modeled_hand_accelerants"],6)
  self.assertEqual(hand["turn10_engine_first"]["ignus_for_rakdos"]["no_hand_acceleration"]["any_real_cascade"],4)
  self.assertEqual(hand["turn10_engine_first"]["ignus_for_rakdos"]["hand_acceleration"]["any_real_cascade"],5)
  self.assertEqual(hand["turn10_engine_first"]["ignus_for_nightscape_familiar"]["hand_acceleration"]["any_supported_effect"],1)
  self.assertEqual(hand["turn10_engine_first"]["ignus_for_rite_of_flame"]["hand_acceleration"]["any_supported_effect"],4)
  self.assertTrue(hand["no_hand_acceleration_reuses_prior_exact"])
  for flag in ("full_99_effects","full_multiplayer_gameplay","opponent_policy_modelled",
               "other_commander_granted_cascades_modelled","superiority_proven","canonical_changed"):
   self.assertFalse(hand[flag])
  self.assertIsNone(hand["measured_win_rate"])
  for key in ("preregistration","evidence"):
   self.assertTrue((ROOT/hand[key]).is_file())
  self.assertEqual(shared["unit_tests"],20)
  self.assertEqual(shared["physical_variants"],5)
  self.assertEqual(shared["policies"],2)
  self.assertEqual(shared["samples_per_variant_policy"],2000)
  self.assertEqual(shared["total_trajectories"],20000)
  self.assertEqual(shared["supported_cascade_effect_names"],12)
  self.assertEqual(shared["turn10_engine_first"]["ignus_for_rakdos"]["any_real_ignus_cascade_trajectory"],12)
  self.assertEqual(shared["turn10_engine_first"]["ignus_for_rakdos"]["any_supported_hit_effect_trajectory"],7)
  self.assertEqual(shared["turn10_engine_first"]["ignus_for_rakdos"]["mana_units_from_hits"],13)
  self.assertEqual(shared["turn10_engine_first"]["ignus_for_nightscape_familiar"]["any_real_ignus_cascade_trajectory"],13)
  self.assertEqual(shared["turn10_engine_first"]["ignus_for_rite_of_flame"]["any_supported_hit_effect_trajectory"],9)
  self.assertTrue(shared["actual_shared_cascade_hit_effects_in_paid_trajectories"])
  self.assertFalse(shared["all_99_effects_implemented"])
  self.assertFalse(shared["full_multiplayer_gameplay"])
  self.assertFalse(shared["superiority_proven"])
  self.assertFalse(shared["opponent_policy_modeled"])
  self.assertFalse(shared["other_commander_granted_hand_cascades_modeled"])
  self.assertFalse(shared["canonical_changed"])
  for key in ("preregistration","evidence"):
   self.assertTrue((ROOT/shared[key]).is_file())
  self.assertEqual(hit["unit_tests"],18)
  self.assertEqual(hit["physical_variants"],5)
  self.assertEqual(hit["samples_per_variant"],2000)
  self.assertEqual(hit["physical_target_pool"],{"nonland_lt3":35,"mv0":7,"mv1":15,"mv2":13})
  self.assertEqual(hit["conditional_turn10"]["approved"]["safe_policy_cast_offer"],1822)
  self.assertEqual(hit["conditional_turn10"]["approved"]["artifact_mana_hit"],530)
  self.assertEqual(hit["conditional_turn10"]["approved"]["tutor_hit"],329)
  self.assertEqual(hit["conditional_turn10"]["ignus_for_nightscape"]["safe_policy_cast_offer"],1818)
  self.assertEqual(hit["conditional_turn10"]["ignus_for_rite"]["safe_policy_cast_offer"],1821)
  self.assertFalse(hit["actual_engine_assembly_at_snapshot"])
  self.assertFalse(hit["effects_of_cascade_hits_resolved"])
  self.assertFalse(hit["full_multiplayer_gameplay"])
  self.assertFalse(hit["superiority_proven"])
  self.assertFalse(hit["canonical_changed"])
  for key in ("preregistration","evidence"):
   self.assertTrue((ROOT/hit[key]).is_file())
  self.assertEqual(paid["unit_tests"],17)
  self.assertEqual(paid["physical_variants"],5)
  self.assertEqual(paid["policies"],2)
  self.assertEqual(paid["samples_per_variant_per_policy"],2000)
  self.assertEqual(paid["total_seeded_closed_trajectories"],20000)
  self.assertTrue(paid["models_paid_named_casts"])
  self.assertFalse(paid["models_actual_cascade_exile_casts"])
  self.assertFalse(paid["full_multiplayer_gameplay"])
  self.assertFalse(paid["superiority_proven"])
  self.assertFalse(paid["canonical_changed"])
  self.assertFalse(paid["real_opponent_response_probability"])
  self.assertEqual(paid["turn10"]["engine_first"]["ignus_for_rakdos"]["paid_five_extra_cascades"],3)
  self.assertEqual(paid["turn10"]["engine_first"]["ignus_for_nightscape"]["paid_five_extra_cascades"],1)
  self.assertEqual(paid["turn10"]["engine_first"]["ignus_for_rite"]["paid_five_extra_cascades"],4)
  self.assertEqual(paid["turn10"]["burn_first"]["ignus_for_rakdos"]["paid_five_extra_cascades"],2)
  self.assertEqual(paid["turn10"]["engine_first"]["approved_commander_cast"],1525)
  for key in ("evidence","preregistration"):
   self.assertTrue((ROOT/paid[key]).is_file())
  self.assertEqual(ignus["unit_tests"],16)
  self.assertEqual(ignus["source_m5_swap_records"],98)
  self.assertEqual(ignus["distinct_candidate_adds"],63)
  self.assertEqual(ignus["unapplied_100_card_variants"],4)
  self.assertEqual(ignus["conditional_finite_trace"]["cascade_triggers_with_birgi_and_abaddon_and_three_life_lost"],5)
  self.assertEqual(ignus["conditional_finite_trace"]["cascade_triggers_below_three_life_lost"],0)
  self.assertFalse(ignus["full_multiplayer_gameplay"])
  self.assertFalse(ignus["superiority_proven"])
  self.assertFalse(ignus["actual_cascade_library_casts_measured"])
  self.assertFalse(ignus["canonical_changed"])
  for key in ("evidence","pre_registration"):
   self.assertTrue((ROOT/ignus[key]).is_file())
  self.assertEqual(warp["unit_tests"],27)
  self.assertEqual(warp["samples_per_variant_per_policy"],2000)
  self.assertEqual(warp["physical_variants"],4)
  self.assertEqual(warp["policies"],2)
  self.assertEqual(warp["turn_10_reserved_channel_policy"]["baseline_any_held_payable_answer"],282)
  self.assertEqual(warp["turn_10_reserved_channel_policy"]["warp_for_rakdos_any"],577)
  self.assertEqual(warp["turn_10_reserved_channel_policy"]["warp_for_lost_any"],584)
  self.assertEqual(warp["turn_10_reserved_channel_policy"]["warp_for_ruinous_any"],557)
  self.assertEqual(warp["turn_10_reserved_channel_policy"]["reserved_otawara_land_drops_skipped_across_2000_samples"],1297)
  self.assertEqual(warp["corrected_mana_values"],{"The Lost and the Damned":3,"The Ruinous Powers":4})
  self.assertEqual(warp["verified_fetchlands_in_baseline"],7)
  self.assertFalse(warp["full_multiplayer_gameplay"])
  self.assertFalse(warp["superiority_proven"])
  self.assertFalse(warp["actual_stax_distribution_measured"])
  self.assertFalse(warp["canonical_changed"])
  for name in ("evidence","preregistration","reserve_policy_preregistration","lost_oracle_preregistration"):
   self.assertTrue((ROOT/warp[name]).is_file(),name)
  self.assertEqual(a["samples_per_variant"],2000)
  self.assertTrue((ROOT/r["evidence"]).is_file())
  self.assertTrue((ROOT/a["evidence"]).is_file())
  self.assertTrue((ROOT/a["preregistration"]).is_file())
  self.assertFalse(r["full_multiplayer_gameplay"])
  self.assertFalse(a["real_combo_casting"])
  self.assertFalse(a["superiority_proven"])
  self.assertEqual(a["turn_10"]["baseline_rakdos"]["individual_land_payable"],254)
  self.assertEqual(a["turn_10"]["assault_for_rakdos"]["individual_land_payable"],336)
  self.assertEqual(a["turn_10"]["assault_for_lost"]["individual_land_payable"],348)
  self.assertEqual(self.t["m6"]["formal_m6_certified_decks"],0)
  self.assertEqual(self.t["m7"]["formal_m7_review_decisions"],0)
  d=json.loads((ROOT/"data/grixis/m6/judgment_reviews/abaddon_phase_b_decisions_20261021.json").read_text())
  ab=next(x for x in d["candidates"] if x["card"]=="Aggravated Assault")
  self.assertFalse(ab["approved_swap"])
  self.assertEqual(ab["access_observation"]["verdict"],"EASIER_ASSAULT_CAST_SOURCE_AVAILABILITY_OBSERVED_BUT_COMBO_VALUE_AND_BEST_CUT_UNPROVEN")
  self.assertIsNone(ab["access_observation"]["gameplay_win_rate"])
  self.assertEqual(ab["chronological_observation"]["n_per_variant"],2000)
  self.assertFalse(ab["chronological_observation"]["superiority_proven"])
  self.assertFalse(ab["chronological_observation"]["canonical_swap_authorized"])
  ignus_case=next(x for x in d["candidates"] if x["card"]=="Grinning Ignus")
  self.assertEqual(ignus_case["interim_decision"],"HOLD_PRIORITY_TEST_CHALLENGER_NO_APPROVED_SWAP")
  self.assertEqual(ignus_case["rule_witness"]["recasts_with_birgi"],5)
  self.assertEqual(ignus_case["paid_assembly_observation"]["engine_first_turn10"]["ignus_for_rakdos"]["five_paid_granted_cascades"],3)
  self.assertEqual(ignus_case["paid_assembly_observation"]["engine_first_turn10"]["ignus_for_nightscape"]["abaddon_cast"],1478)
  self.assertFalse(ignus_case["paid_assembly_observation"]["proves_challenger_superiority"])
  self.assertEqual(ignus_case["cascade_first_hit_observation"]["subthree_pool"]["total"],35)
  self.assertEqual(ignus_case["cascade_first_hit_observation"]["t10_per2000"]["approved_safe_cast_offers"],1822)
  self.assertFalse(ignus_case["cascade_first_hit_observation"]["ramp_or_tutor_effects_resolved"])
  self.assertFalse(ignus_case["cascade_first_hit_observation"]["net_superiority_proven"])
  o=ignus_case["disruption_oracle_correction"]
  self.assertEqual(o["registered_windows"],8)
  self.assertEqual(o["tests_targeted"],15)
  self.assertEqual(o["tests_predecessor"],20)
  self.assertEqual(o["witnesses"]["uncontested_paid_recasts"],5)
  self.assertFalse(o["witnesses"]["rule_of_law_first_ignus_free_cascade_legal"])
  self.assertFalse(o["witnesses"]["drannith_cascade_free_cast_legal"])
  self.assertFalse(o["witnesses"]["original_ignus_countered_enters_battlefield"])
  self.assertFalse(o["actual_opponent_response_probability"])
  self.assertFalse(o["swap_superiority_proven"])
  self.assertIsNone(o["win_rate"])
  mana=ignus_case["hand_acceleration_observation"]
  self.assertTrue(mana["actual_non_cascade_hand_ramp_paid"])
  self.assertEqual(mana["engine_first_turn10_per1000"]["ignus_for_rakdos"]["no_hand_acceleration"]["actual_ignus_cascade"],4)
  self.assertEqual(mana["engine_first_turn10_per1000"]["ignus_for_rakdos"]["hand_acceleration"]["actual_ignus_cascade"],5)
  self.assertFalse(mana["other_abaddon_hand_cast_cascades"])
  self.assertFalse(mana["net_superiority_proven"])
  self.assertIsNone(mana["measured_multiplayer_win_rate"])
  joined=ignus_case["shared_paid_effects_observation"]
  self.assertTrue(joined["actual_paid_shared_cascade_effects"])
  self.assertEqual(joined["engine_first_turn10_per2000"]["ignus_for_rakdos"]["any_actual_ignus_cascade"],12)
  self.assertEqual(joined["engine_first_turn10_per2000"]["ignus_for_rakdos"]["any_source_verified_hit_effect_resolved"],7)
  self.assertFalse(joined["all_99_effects_modeled"])
  self.assertFalse(joined["other_qualifying_hand_cascades_modeled"])
  self.assertFalse(joined["swap_superiority_proven"])
  self.assertIsNone(joined["measured_multiplayer_win_rate"])
  self.assertIsNone(ignus_case["paid_assembly_observation"]["true_game_win_rate"])
  self.assertFalse(ignus_case["approved_swap"])
  chaos=next(x for x in d["candidates"] if x["card"]=="Chaos Warp")
  self.assertFalse(chaos["approved_swap"])
  self.assertEqual(chaos["stax_answer_observation"]["turn_10_reserve_policy"]["approved_baseline_otawara_payable"],282)
  self.assertFalse(chaos["stax_answer_observation"]["approved_swap"])
  self.assertIsNone(chaos["stax_answer_observation"]["actual_multiplayer_win_rate"])
  role=d["other_pool_resolution"]["protected_engine_oracle_errata"]
  self.assertEqual(role["lost"]["mana_value"],3)
  self.assertEqual(role["ruinous"]["mana_value"],4)
  self.assertIn("seven",role["lost"]["trigger"])
  self.assertEqual(self.t["m6"]["gates"][5]["status"],"PARTIAL")
  self.assertEqual(self.t["m6"]["gates"][6]["status"],"PARTIAL")
 def test_no_canonical_reapproval_claim(self):
  self.assertIn("do not count",self.t["accounting"]["warning"].lower())
  self.assertEqual(self.t["accounting"]["canonical_approved_locked"],62)
  self.assertEqual(self.t["m6"]["formal_m6_certified_decks"],0)
  self.assertEqual(self.t["m7"]["formal_m7_review_decisions"],0)
if __name__=="__main__":unittest.main()
