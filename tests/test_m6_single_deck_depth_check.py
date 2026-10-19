"""Single-deck sequential depth-review tracker guards."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_single_deck_depth_check as c
class SequentialDepth(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.tracker=c.load(c.LEDGER)
  cls.registry=c.load(c.REG)
 def test_exact_62_verified_order_and_zero_deep_reviews(self):
  self.assertEqual(c.validate(self.tracker,self.registry),0)
  self.assertEqual(self.tracker["process"]["next_tracker_deck_id"],"Abaddon_the_Despoiler")
 def test_no_false_source_coverage_promotion(self):
  x=copy.deepcopy(self.tracker);x["process"]["deep_review_complete_count"]=62
  with self.assertRaises(AssertionError):c.validate(x,self.registry)
 def test_cannot_skip_deck_before_completing_first(self):
  x=copy.deepcopy(self.tracker);x["decks"][1]["status"]="IN_PROGRESS"
  x["process"]["active_tracker_deck_id"]=x["decks"][1]["tracker_deck_id"]
  with self.assertRaises(AssertionError):c.validate(x,self.registry)
 def test_missing_evidence_cannot_complete_first_deck(self):
  x=copy.deepcopy(self.tracker);x["decks"][0]["status"]="DEEP_REVIEW_COMPLETE"
  x["process"]["deep_review_complete_count"]=1
  x["process"]["next_tracker_deck_id"]=x["decks"][1]["tracker_deck_id"]
  with self.assertRaises(AssertionError):c.validate(x,self.registry)
 def test_hidden_canonical_hash_tampering_rejected(self):
  x=copy.deepcopy(self.tracker);x["decks"][0]["baseline_approved_sha256"]="0"*64
  with self.assertRaises(AssertionError):c.validate(x,self.registry)
 def test_goben_norman_conflict_cannot_be_silently_marked_alias_none(self):
  x=copy.deepcopy(self.tracker)
  t=next(z for z in x["decks"] if z["canonical_deck_id"]=="Goben__Gene_Splice_Savant")
  t["source_identity_discrepancy"]="NONE"
  with self.assertRaises(AssertionError):c.validate(x,self.registry)
 def test_canonical_swap_permission_mutation_rejected(self):
  x=copy.deepcopy(self.tracker);x["authority"]["canonical_deck_changes_allowed"]=True
  with self.assertRaises(AssertionError):c.validate(x,self.registry)
 def test_in_progress_requires_same_first_deck(self):
  x=copy.deepcopy(self.tracker);x["decks"][0]["status"]="IN_PROGRESS"
  x["process"]["active_tracker_deck_id"]="Abaddon_the_Despoiler"
  self.assertEqual(c.validate(x,self.registry),0)
 def test_blocked_requires_reason(self):
  x=copy.deepcopy(self.tracker);x["decks"][0]["status"]="BLOCKED"
  x["process"]["active_tracker_deck_id"]="Abaddon_the_Despoiler"
  with self.assertRaises(AssertionError):c.validate(x,self.registry)
if __name__=="__main__":unittest.main()
