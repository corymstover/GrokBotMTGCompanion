"""Cycle113 adversarial source review and no-approval regression tests."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle113_commander_reviews as m

class Cycle113Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.reg=m.read(m.REG);cls.plan=m.read(m.PLAN);cls.review=m.read(m.REV)
  cls.actual=m.build()
 def test_three_approved_complete_source_lists(self):
  self.assertEqual(len(self.actual["new_source_verified_decks"]),3)
  self.assertEqual(set(x["deck_id"] for x in self.actual["new_source_verified_decks"]),set(m.EXPECTED))
  for x in self.actual["new_source_verified_decks"]:
   self.assertEqual(x["actual_main_cards"],99)
   self.assertEqual(x["actual_commanders"],1)
   self.assertTrue(x["proposed_cut_present"])
   self.assertTrue(x["proposed_add_absent"])
   self.assertTrue(x["commander_blueprint_required_core_preserved"])
 def test_no_independent_reviewer_or_decision_fabricated(self):
  for k in ("formal_independent_Pass_C_reviews_completed","effect_aware_balanced_phase_B_completed",
   "approved_decks_modified","new_owner_approvals"):
   self.assertEqual(self.actual[k],0)
  self.assertTrue(self.actual["real_independent_reviewers_not_claimed"])
  self.assertFalse(self.actual["official_current_legality_reverified"])
  self.assertFalse(self.actual["M6_accepted"])
  self.assertTrue(all(v is False for v in self.actual["authority"].values()))
 def test_original_identity_protected_and_nazgul_card_rule(self):
  row={x["deck_id"]:x for x in self.actual["new_source_verified_decks"]}
  self.assertEqual(len(row),3)
  self.assertIn("Sauron__Lord_of_the_Rings",row)
  self.assertIn("Nazgûl",m.ORACLE)
  self.assertIn("Godo, Bandit Warlord",m.ORACLE)
  self.assertTrue(all(x["source_P0_agreement_not_an_approval"] for x in row.values()))
 def test_author_retrospective_does_not_change_prior_approved_list(self):
  a=self.review["retrospective"]
  self.assertIn("Archaeomancer",a["Cormela"])
  self.assertIn("Dockside Chef",a["Ashnod"])
  self.assertIn("Illusionist's Bracers",a["Gwendlyn"])
  self.assertIn("unbounded untap",a["Gwendlyn"])
  self.assertTrue(self.actual["reviewed_holds_do_not_certify_all_candidate_pools"])
 def test_corrupted_approval_hash_m5_swap_and_candidate_are_rejected(self):
  r=copy.deepcopy(self.review["reviews"][0]);r["approved_raw_sha256"]="fake"
  did=r["deck_id"]
  class Deck:
   commanders=[{"name":m.EXPECTED[did][1]}]
   library=[{"name":m.EXPECTED[did][3]}]+[{"name":"other"+str(i)} for i in range(98)]
  reg=self.reg["decks"][did]
  bp=m.read(ROOT/"data/grixis/blueprints"/(reg["slug"]+".json"))
  triage=m.read(m.TRIAGE)
  x=next(x for x in triage["ordered_decks"] if x["deck_id"]==did)
  p=next(x for x in self.plan["new_reviews"] if x["deck_id"]==did)
  with self.assertRaises(ValueError):
   m.verify_deck(r,p,reg,bp,Deck(),x,self.actual["verified_frozen_oracle_records"])
  r=copy.deepcopy(self.review["reviews"][0])
  r["m5_swap_id"]="fabricated"
  with self.assertRaises(ValueError):
   m.verify_deck(r,p,reg,bp,Deck(),x,self.actual["verified_frozen_oracle_records"])
 def test_outcome_and_missing_opponent_play_explicit(self):
  for r in self.review["reviews"]:
   self.assertEqual(r["disposition"],"HOLD_EXISTING_LIST_NO_SWAP")
   self.assertFalse(r["proposed_change_approved"])
   self.assertGreaterEqual(len(r["rules"]),4)
  self.assertFalse(self.review["global_gates"]["M6_accepted"])
  self.assertEqual(self.review["global_gates"]["formal_phase_b_count"],0)

if __name__=="__main__":unittest.main()
