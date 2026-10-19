"""Cycle117 reviewer readiness: source invariants, false-certification resistance, adversarial outcomes."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle117_independent_review_readiness as m

class IndependentReadinessTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.receipt=m.audit()
  cls.protocols=m.read(m.PROTO)
  cls.rows=m.source_rows()
 def test_all_fifteen_source_bound_without_new_judgments(self):
  d=self.receipt
  self.assertEqual(d["author_review_count"],15)
  self.assertEqual(d["verified_distinct_decks"],15)
  self.assertEqual(d["dispositions"],{"held_exact_swap":12,"promising_unresolved":3})
  self.assertEqual(len({r["swap_id"] for r in d["author_rows"]}),15)
  for row in d["author_rows"]:
   self.assertEqual(len(row["approved_raw_sha256"]),64)
   self.assertTrue(row["source_sha256"].startswith("sha256:"))
 def test_three_falsifiable_experiments_and_two_scenario_types(self):
  d=self.receipt
  self.assertEqual(d["counterfactual_protocol_count"],3)
  self.assertEqual(d["counterfactual_scenario_count"],6)
  self.assertEqual(set(d["counterfactual_protocols"]),
    {"Gwendlyn_Di_Corci","Nicol_Bolas__the_Ravager","Mai_and_Zuko"})
  for p in self.protocols["protocols"]:
   self.assertEqual({s["kind"] for s in p["scenarios"]},
    {"favorable_candidate","adverse_candidate"})
   self.assertIsNone(p["same_seed_actual_results"])
 def test_authority_readiness_never_certification(self):
  d=self.receipt
  self.assertEqual(d["formal_independent_pass_c_count"],0)
  self.assertEqual(d["real_effect_aware_paired_result_count"],0)
  self.assertFalse(d["independent_reviewer_assigned"])
  self.assertEqual(d["owner_approvals_issued"],0)
  self.assertEqual(d["canonical_decks_modified"],0)
  self.assertFalse(d["M6_accepted"])
  self.assertIn("BLOCKED_PENDING_EXTERNAL_REVIEW",d["review_outcome_gate"])
  self.assertTrue(all(v is False for v in d["authority"].values()))
 def test_adversarial_faked_external_reviewer_or_measured_outcomes(self):
  fake=copy.deepcopy(self.protocols)
  fake["reviewer_independence_certified"]=True
  with self.assertRaises(ValueError):m.validate_protocols(fake,self.rows)
  fake=copy.deepcopy(self.protocols)
  fake["observed_game_results"]=[{"outcome":"invented"}]
  with self.assertRaises(ValueError):m.validate_protocols(fake,self.rows)
  fake=copy.deepcopy(self.protocols)
  fake["protocols"][0]["same_seed_actual_results"]=[1]
  with self.assertRaises(ValueError):m.validate_protocols(fake,self.rows)
 def test_adversarial_missing_comparator_and_m5_drift(self):
  fake=copy.deepcopy(self.protocols)
  fake["protocols"][0]["scenarios"][0]["compare_to_baseline"]=""
  with self.assertRaises(ValueError):m.validate_protocols(fake,self.rows)
  fake=copy.deepcopy(self.protocols)
  fake["protocols"][0]["source_swap_id"]="swap:wrong"
  with self.assertRaises(ValueError):m.validate_protocols(fake,self.rows)
  fake=copy.deepcopy(self.protocols)
  fake["protocols"][1]["scenarios"]=[fake["protocols"][1]["scenarios"][0]]
  with self.assertRaises(ValueError):m.validate_protocols(fake,self.rows)
 def test_adversarial_wrong_identity_or_performance_promotion(self):
  fake=copy.deepcopy(self.protocols)
  fake["protocols"][2]["candidate"]="Hullbreaker Horror"
  with self.assertRaises(ValueError):m.validate_protocols(fake,self.rows)
  fake=copy.deepcopy(self.protocols)
  fake["no_approval_authority"]["can_certify_pass_c"]=True
  with self.assertRaises(ValueError):m.validate_protocols(fake,self.rows)
  fake=copy.deepcopy(self.protocols)
  fake["protocols"][0]["minimum_real_observations_for_provisional_comparison"]=1
  with self.assertRaises(ValueError):m.validate_protocols(fake,self.rows)
 def test_gwendlyn_shroud_and_tutor_adversarial_setup_is_explicit(self):
  data=next(x for x in self.protocols["protocols"] if x["deck_id"]=="Gwendlyn_Di_Corci")
  adverse=next(s for s in data["scenarios"] if s["kind"]=="adverse_candidate")
  self.assertIn("shroud",adverse["setup"].lower())
  self.assertIn("tutor",adverse["setup"].lower())
 def test_no_probability_or_observed_game_claim_from_prompts(self):
  self.assertFalse(self.protocols["phase_b_completed"])
  self.assertFalse(self.protocols["formal_independent_pass_c_completed"])
  self.assertEqual(self.protocols["observed_game_results"],[])
if __name__=="__main__":unittest.main()
