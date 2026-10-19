"""Cycle129 positive and hostile data integrity tests."""
import unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle129_validate as v
class Reviews(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.d=v.validate()
 def test_six_distinct(self):
  self.assertEqual(len(cls_set:={x["deck_id"] for x in self.d["checks"]}),6)
  self.assertEqual(self.d["authored_total"],27)
 def test_no_independent_or_canonical_promotion(self):
  self.assertEqual(self.d["independent_pass_c"],0)
  self.assertEqual(self.d["canonical_edits"],0)
  self.assertTrue(all(not x["independent_pass_c"] for x in self.d["checks"]))
 def test_exact_oracle_card_names(self):
  for row in self.d["checks"]:
   self.assertEqual(len(row["oracle_text_hashes"]),3)
   self.assertTrue(all(len(sha)==64 for sha in row["oracle_text_hashes"].values()))
 def test_future_release_not_official(self):
  j=next(x for x in self.d["checks"] if x["deck_id"]=="The_Madcap_Jester")
  self.assertEqual(j["official_snapshot_status"],"pending_release")
  self.assertEqual(len(j["exceptions"]),2)
 def test_untrusted_swap_rejected(self):
  x=v.load("data/grixis/m6/author_reviews/cycle129_six_detailed_01.json")
  q=v.load("data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json")
  row=x["rows"][0];pair=next(c for c in q["ordered_decks"] if c["deck_id"]==row["deck_id"])
  self.assertEqual(row["add"],pair["first_three_TO_REVIEW_NOT_TO_APPLY"][0]["add"])
  self.assertNotEqual("Fake Addition",pair["first_three_TO_REVIEW_NOT_TO_APPLY"][0]["add"])
if __name__=="__main__":unittest.main()
