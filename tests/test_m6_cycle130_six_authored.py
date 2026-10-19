"""Cycle130 positive and hostile data integrity tests."""
import unittest,sys,copy
from unittest.mock import patch
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle130_validate as v
class Reviews(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.d=v.validate()
 def test_six_distinct(self):
  self.assertEqual(len(cls_set:={x["deck_id"] for x in self.d["checks"]}),6)
  self.assertEqual(self.d["authored_total"],33)
 def test_no_independent_or_canonical_promotion(self):
  self.assertEqual(self.d["independent_pass_c"],0)
  self.assertEqual(self.d["canonical_edits"],0)
  self.assertTrue(all(not x["independent_pass_c"] for x in self.d["checks"]))
 def test_exact_oracle_card_names(self):
  for row in self.d["checks"]:
   self.assertEqual(len(row["oracle_text_hashes"]),3)
   self.assertTrue(all(len(sha)==64 for sha in row["oracle_text_hashes"].values()))
 def test_no_new_project_exceptions(self):
  self.assertTrue(all(not x["exceptions"] for x in self.d["checks"]))
 def test_untrusted_swap_rejected(self):
  x=v.load("data/grixis/m6/author_reviews/cycle130_six_detailed_01.json")
  q=v.load("data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json")
  row=x["rows"][0];pair=next(c for c in q["ordered_decks"] if c["deck_id"]==row["deck_id"])
  self.assertEqual(row["add"],pair["first_three_TO_REVIEW_NOT_TO_APPLY"][0]["add"])
  self.assertNotEqual("Fake Addition",pair["first_three_TO_REVIEW_NOT_TO_APPLY"][0]["add"])
 def test_tampered_candidate_fails_real_validator(self):
  original=v.load
  target="data/grixis/m6/author_reviews/cycle130_six_detailed_01.json"
  def modified(path):
   x=original(path)
   if str(path)==target:
    x=copy.deepcopy(x);x["rows"][0]["add"]="Fake Addition"
   return x
  with patch.object(v,"load",side_effect=modified):
   with self.assertRaises(AssertionError):v.validate()
 def test_false_milestone_fails_real_validator(self):
  original=v.load
  def modified(path):
   x=original(path)
   if str(path)=="data/grixis/milestone_m6_m7_subtracker.json":
    x=copy.deepcopy(x);x["m6"]["gates"][3]["completed"]=62
   return x
  with patch.object(v,"load",side_effect=modified):
   with self.assertRaises(AssertionError):v.validate()
 def test_missing_review_rules_fails_real_validator(self):
  original=v.load
  target="data/grixis/m6/author_reviews/cycle130_six_detailed_01.json"
  def modified(path):
   x=original(path)
   if str(path)==target:
    x=copy.deepcopy(x);x["rows"][1]["rules"]=[]
   return x
  with patch.object(v,"load",side_effect=modified):
   with self.assertRaises(AssertionError):v.validate()
if __name__=="__main__":unittest.main()
