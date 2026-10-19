"""Cycle116 deterministic adversarial commander-first checks (no canonical mutations)."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle116_commander_reviews as m

class Cycle116Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.out=m.run()
  cls.plan=m.read(m.PLAN)
  cls.reviews=m.read(m.REV)
  cls.reg=m.read(m.REG)
  cls.tri=m.read(m.TRIAGE)
 def test_approved_sources_are_exact_three_commander_first_100(self):
  self.assertEqual(self.out["review_count"],3)
  self.assertEqual(set(x["deck_id"] for x in self.out["reviewed"]),set(m.EXPECTED))
  for row in self.out["reviewed"]:
   self.assertEqual(row["source_main_count"],99)
   self.assertEqual(row["commander_count"],1)
   self.assertTrue(row["nonbasic_singleton_checked"])
   self.assertTrue(row["add_absent_cut_present"])
   self.assertFalse(row["canonical_deck_modified"])
 def test_frozen_oracle_positive_mechanics(self):
  seen=self.out["frozen_oracle"]
  for card in ("Kess, Dissident Mage","Edea, Possessed Sorceress","Lynde, Cheerful Tormentor",
        "Hullbreaker Horror","Orcish Bowmasters","Tidespout Tyrant","Deadly Rollick",
        "Withering Torment","Despotic Scepter"):
   self.assertIn(card,seen)
   self.assertTrue(seen[card]["frozen_source_only_not_live_current_legality"])
 def _row_inputs(self,did):
  row=next(x for x in self.reviews["reviews"] if x["deck_id"]==did)
  plan=next(x for x in self.plan["decks"] if x["deck_id"]==did)
  reg=self.reg["decks"][did]
  bp=m.read(ROOT/"data/grixis/blueprints"/(row["slug"]+".json"))
  tri=next(x for x in self.tri["ordered_decks"] if x["deck_id"]==did)
  class Stub:
   commanders=[{"name":row["commander"]}]
   library=[{"name":row["proposed_cut"]}]+[{"name":"filler-"+str(i)} for i in range(98)]
  return row,plan,reg,bp,tri,Stub()
 def test_adversarial_approval_sha_mismatch(self):
  x=self._row_inputs("Kess__Dissident_Mage")
  row=copy.deepcopy(x[0]);row["approved_raw_sha256"]="0"*64
  with self.assertRaises(ValueError):
   m.validate(row,x[1],x[2],x[3],x[4],x[5],self.out["frozen_oracle"])
 def test_adversarial_candidate_replacement_and_false_certificate(self):
  x=self._row_inputs("Lynde__Cheerful_Tormentor")
  row=copy.deepcopy(x[0]);row["proposed_cut"]="Curse of Bloodletting"
  with self.assertRaises(ValueError):
   m.validate(row,x[1],x[2],x[3],x[4],x[5],self.out["frozen_oracle"])
  row=copy.deepcopy(x[0]);row["independent_pass_c_completed"]=True
  with self.assertRaises(ValueError):
   m.validate(row,x[1],x[2],x[3],x[4],x[5],self.out["frozen_oracle"])
 def test_adversarial_wrong_oracle_source(self):
  x=self._row_inputs("Edea__Possessed_Sorceress")
  row=copy.deepcopy(x[0]);bad=copy.deepcopy(self.out["frozen_oracle"])
  bad.pop("Tidespout Tyrant")
  with self.assertRaises(ValueError):
   m.validate(row,x[1],x[2],x[3],x[4],x[5],bad)
 def test_no_false_upgrade_or_independent_review(self):
  for key in ("canonical_decks_modified","swaps_approved_or_applied",
        "formal_independent_pass_c_count","effect_aware_multiplayer_phase_b_count"):
   self.assertEqual(self.out[key],0)
  self.assertFalse(self.out["M6_accepted"])
  self.assertFalse(self.out["entire_deck_current_official_legality_certified"])
  self.assertFalse(self.out["source_bytes_independently_rehashed"])
  self.assertTrue(all(v is False for v in self.out["authority"].values()))
  for row in self.reviews["reviews"]:
   self.assertEqual(row["disposition"],"HOLD_EXISTING_LIST_NO_SWAP")
   self.assertEqual(row["approved_swaps"],0)
   self.assertTrue(row["cut_cost"] and row["next_evidence"])

if __name__=="__main__":unittest.main()
