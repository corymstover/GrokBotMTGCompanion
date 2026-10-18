"""Cycle112 negative verification: no source drift or unauthorized cards/approval."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle112_commander_reviews as m

class ThreeCommanderReviews(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.reg=m.read(m.REG)
  cls.plan=m.read(m.PLAN)
  cls.review=m.read(m.REVIEWS)
  cls.verified=m.run() # Requires CI-restored pinned Scryfall archive.
 def test_exact_3_source_bound_real_card_decklists(self):
  x=self.verified
  self.assertEqual(len(x["reviewed_decks"]),3)
  self.assertEqual(x["source_conservation"]["full_approved_lists_read"],3)
  self.assertEqual(x["source_conservation"]["reviewed_additions_applied"],0)
  self.assertTrue(all(v["original_99_card_main_verified"] and
    v["commander_on_100th_slot_verified"] for v in x["reviewed_decks"]))
 def test_author_judgment_cannot_pose_as_independent(self):
  x=self.verified
  self.assertEqual(x["independent_Pass_C_reviews_completed"],0)
  self.assertEqual(x["full_effect_aware_M6_Phase_B_reviews_completed"],0)
  self.assertEqual(x["approvals_or_certifications_issued"],0)
  self.assertFalse(x["M6_accepted"])
  self.assertTrue(all(v is False for v in x["authority"].values()))
  self.assertTrue(all(not row["swap_applied_or_approved"] and
     not row["named_independent_Pass_C_complete"] and
     not row["proposed_card_legality_rechecked_at_decision_time"]
     for row in x["reviewed_decks"]))
 def test_all_three_outcomes_are_explicit(self):
  self.assertEqual(self.verified["dispositions"],{
    "Cormela, Glamour Thief":"HOLD_EXISTING_LIST_NO_SWAP",
    "Ashnod the Uncaring":"HOLD_EXISTING_LIST_NO_SWAP",
    "Gwendlyn Di Corci":"PROMISING_UNRESOLVED_REQUIRES_TARGETED_EVIDENCE"})
 def test_false_source_binding_rejected(self):
  sample=self.review["reviews"][0]
  d=self.reg["decks"][sample["deck_id"]]
  b=m.read(ROOT/"data/grixis/blueprints"/(sample["slug"]+".json"))
  p=m.read(ROOT/"data/grixis/m6/review_packets"/(sample["slug"]+".json"))
  class Fake:
   commanders=[{"name":"Cormela, Glamour Thief"}]
   library=[{"name":n} for n in ["Faithless Looting"]+["unrelated_"+str(x) for x in range(98)]]
  bad=copy.deepcopy(sample)
  bad["approved_raw_sha256"]="invalid"
  with self.assertRaisesRegex(ValueError,"Approved deck source"):
   m.validate_review(bad,self.plan["first_batch"][0],d,b,p,Fake(),self.verified["frozen_oracle_checks"])
  bad=copy.deepcopy(sample)
  bad["cut"]="Saw in Half"
  with self.assertRaises(ValueError):
   m.validate_review(bad,self.plan["first_batch"][0],d,b,p,Fake(),self.verified["frozen_oracle_checks"])
 def test_reject_fabricated_selected_candidate_or_m5_auto_approve(self):
  d=self.reg["decks"]["Ashnod_the_Uncaring"]
  b=m.read(ROOT/"data/grixis/blueprints"/(d["slug"]+".json"))
  p=m.read(ROOT/"data/grixis/m6/review_packets"/(d["slug"]+".json"))
  fake=copy.deepcopy(p)
  matches=[x for x in fake["items"] if x["swap_id"]==
    "swap:ashnod-the-uncaring:m5:0298cc8543cb"]
  self.assertEqual(len(matches),1)
  matches[0]["candidate"]["screening_can_decide"]=True
  with self.assertRaises(ValueError):
   m.validate_review(self.review["reviews"][1],self.plan["first_batch"][1],d,b,fake,
                     type("Model",(),{"library":[{"name":"Dockside Chef"}]*99,
                       "commanders":[{"name":"Ashnod the Uncaring"}]})(),
                     self.verified["frozen_oracle_checks"])
 def test_rules_gates_encoded_in_reviews(self):
  r={x["deck_id"]:x for x in self.review["reviews"]}
  self.assertIn("cannot cast Archaeomancer", " ".join(r["Cormela__Glamour_Thief"]["commander_specific_rules"]))
  a=" ".join(r["Ashnod_the_Uncaring"]["commander_specific_rules"])
  self.assertIn("Chef",a)
  self.assertIn("Clues",a)
  g=" ".join(r["Gwendlyn_Di_Corci"]["commander_specific_rules"])
  self.assertIn("Bracers",g)
  self.assertIn("shroud",g)
  self.assertIn("own-turn",g)
  for k in r:
   self.assertGreaterEqual(len(r[k]["missing_evidence"]),3)

if __name__=="__main__":unittest.main()
