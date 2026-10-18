"""Cycle105 source-auditable decision readiness regressions."""
import sys,unittest,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_abaddon_decision_readiness as m

class DecisionReadinessTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.report=m.verify()
  cls.plan=m.read(m.PLAN)
 def test_all_98_packet_items_provisional(self):
  r=self.report
  self.assertEqual(r["packet_screening_rows"],98)
  self.assertEqual(len(r["screening_queue"]),98)
  self.assertEqual([a["row"] for a in r["screening_queue"]],list(range(1,99)))
  self.assertTrue(all(not a["candidate_swap_approved"] for a in r["screening_queue"]))
  self.assertTrue(all(a["requires_independent_commander_first_review"] for a in r["screening_queue"]))
 def test_six_exact_matched_core_and_alt_cut_pairs(self):
  f=self.report["deep_focus_comparisons"]
  self.assertEqual(len(f),6)
  adds=self.plan["focus"]["adds"];cuts=self.plan["focus"]["cuts"]
  self.assertEqual({(x["add"],x["cut"]) for x in f},
                   {(a,c) for a in adds for c in cuts})
  self.assertEqual(sum(x["registry"]["source"]=="M5_review_packet" for x in f),4)
  self.assertEqual(sum(x["registry"]["source"].startswith("M6_") for x in f),2)
 def test_protected_core_has_no_fake_measured_power(self):
  for item in self.report["deep_focus_comparisons"]:
   if item["cut"]=="Bituminous Blast":
    self.assertEqual(item["registry"]["source"],"M6_independently_proposed_alt_cut_not_in_98_M5_rows")
    self.assertTrue(item["protected_role_loss"]["printed_cascade_plus_instant_speed_creature_removal"])
    self.assertIsNotNone(item["finite_cascade_offer_coverage"])
    self.assertIsNotNone(item["paired_development_proxy"])
    self.assertTrue(item["paired_development_proxy"]["NOT_effect_aware_or_a_win_metric"])
   else:
    self.assertEqual(item["preliminary_strategic_status"],"DISFAVOR_PROTECTED_ENGINE_CUT")
    self.assertIsNone(item["finite_cascade_offer_coverage"])
    self.assertIsNone(item["paired_development_proxy"])
    self.assertTrue(any(v for k,v in item["protected_role_loss"].items() if k!="requires_explicit_alternative_role_compensation"))
 def test_all_relevant_decision_gates_fail(self):
  self.assertFalse(self.report["ready_for_any_card_swap"])
  self.assertFalse(self.report["tested_pool_zero_improvement_certified"])
  self.assertFalse(self.report["independent_phase_b_completed"])
  self.assertFalse(self.report["independent_pass_c_completed"])
  self.assertFalse(self.report["true_gameplay_win_rate_available"])
  self.assertFalse(self.report["M6_accepted"])
  self.assertTrue(all(not any(x["hard_gates"].values()) for x in self.report["deep_focus_comparisons"]))
  self.assertTrue(all(not x["approved_swap"] and not x["zero_improvement_proven"]
                      for x in self.report["deep_focus_comparisons"]))
 def test_frozen_source_and_exact_verified_canonical_card_count(self):
  self.assertEqual(len(m.list_cards()),100)
  self.assertEqual(m.list_cards()[0],"Abaddon the Despoiler")
  self.assertEqual(self.report["source_approved_list_sha256"],self.plan["frozen"]["approved_list_sha256"])
  self.assertEqual(self.report["source_list_sha256"],
                   "sha256:"+self.plan["frozen"]["baseline_export_sha256"])
  self.assertTrue(all(v is False for v in self.report["authority"].values()))
 def test_m5_screening_drift_fails_closed(self):
  packet=m.read(m.ROOT/self.plan["frozen"]["source_packet"])
  good=m.screening(packet)
  item=copy.deepcopy(packet);item["items"][0]["authority"]["can_decide"]=True
  with self.assertRaises(ValueError):m.screening(item)
  self.assertEqual(len(good),98)
 def test_manifest_declares_discriminating_next_experiment(self):
  next_=self.report["next_discriminating_experiment"]
  self.assertGreaterEqual(len(next_["preregister_requirements"]),6)
  self.assertTrue(next_["unsupported_effects_are_not_zero_value"])
  self.assertIn("Bituminous Blast",next_["name"])

if __name__=="__main__":unittest.main()
