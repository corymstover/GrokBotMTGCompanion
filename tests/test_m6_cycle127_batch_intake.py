"""Cycle127 positive/adversarial 62-deck batch review queue tests."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle127_batch_intake as m

class BatchIntake(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.plan,cls.reg,cls.tri,cls.track=map(m.read,(m.PLAN,m.REG,m.TRI,m.TRACK))
  cls.rows=m.verify_source(cls.plan,cls.reg,cls.tri,cls.track,m.prior.source_rows())
  cls.authors={x["deck_id"]:x for x in m.prior.source_rows()}
  cls.generated=m.generate()
 def test_all_62_nonduplicated_and_fully_source_bound(self):
  d=self.generated
  self.assertEqual((d["prepared_decks"],d["previous_authored_decks"],d["awaiting_authored_review"]),(62,15,47))
  self.assertEqual(len({x["deck_id"] for x in d["packets"]}),62)
  self.assertEqual(len({x["candidate_id"] for x in d["packets"]}),62)
  for x in d["packets"]:
   self.assertTrue(x["candidate_id"].startswith("swap:"+x["slug"]+":m5:"))
   self.assertTrue(x["challenger_add"] and x["baseline_cut"])
   self.assertEqual(x["historical_author_review_exists"],x["deck_id"] in self.authors)
   self.assertTrue(x["no_author_verdict_in_packet"])
   self.assertFalse(x["exception_treatment"]["current_official_legality_reverified"])
 def test_frozen_authority_and_no_fictional_pass_c(self):
  d=self.generated
  self.assertEqual(d["zero_authority_outcomes"],m.ZERO)
  self.assertTrue(d["CI_is_not_independent_review"])
  self.assertFalse(d["full_phase_b_or_m6_certificates_created"])
  self.assertFalse(any(v for v in self.plan["authority"].values()))
 def test_immutable_generated_bytes(self):
  self.assertEqual(m.encode(m.generate()),m.encode(self.generated))
 def test_reject_false_milestone_acceptance(self):
  reg=copy.deepcopy(self.reg);reg["program"]["milestones"]["M6"]["status"]="accepted"
  with self.assertRaises(ValueError):m.verify_source(self.plan,reg,self.tri,self.track,m.prior.source_rows())
 def test_reject_duplicate_source_deck(self):
  t=copy.deepcopy(self.tri);t["ordered_decks"][1]["deck_id"]=t["ordered_decks"][0]["deck_id"]
  with self.assertRaises(ValueError):m.verify_source(self.plan,self.reg,t,self.track,m.prior.source_rows())
 def test_reject_fabricated_authored_count(self):
  authors=m.prior.source_rows();authors[0]=copy.deepcopy(authors[1])
  with self.assertRaises(ValueError):m.verify_source(self.plan,self.reg,self.tri,self.track,authors)
 def test_reject_corrupt_blueprint_hash(self):
  q=copy.deepcopy(self.rows[0]);q["blueprint_sha256"]="sha256:"+"0"*64
  with self.assertRaises(ValueError):m.packet(q,self.reg,self.authors)
 def test_reject_swapped_candidate_not_in_M5_queue(self):
  q=copy.deepcopy(self.rows[0]);q["first_three_TO_REVIEW_NOT_TO_APPLY"][0]["swap_id"]="swap:bogus:m5:123"
  with self.assertRaises(ValueError):m.packet(q,self.reg,self.authors)
 def test_reject_unverified_author_staple_pair(self):
  q=next(copy.deepcopy(x) for x in self.rows if x["deck_id"] in self.authors)
  a=copy.deepcopy(self.authors)
  a[q["deck_id"]]["add"]="A fabricated replacement"
  with self.assertRaises(ValueError):m.packet(q,self.reg,a)
 def test_registered_exceptions_separate_from_official_status(self):
  for x in self.generated["packets"]:
   if x["exception_treatment"]["registered_project_exceptions"]:
    self.assertFalse(x["exception_treatment"]["current_official_legality_reverified"])
   self.assertFalse(x["no_current_oracle_or_gameplay_claim"] is False)
 def test_source_sha_mismatch_is_explicit_not_silently_cured(self):
  bad={x["deck_id"] for x in self.generated["packets"] if not x["historical_recorded_source_hash_matches_raw"]}
  self.assertEqual(bad,{"Admiral_Brass__Unsinkable","Anhelo__the_Painter"})
  self.assertTrue(all("not_rehashed" in x for x in [])) # No independent raw-rehash claim.
if __name__=="__main__":unittest.main()
