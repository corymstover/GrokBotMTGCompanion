"""Cycle120: source-locked physical access, paired positions and no false gameplay claims."""
import copy,random,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle120_physical_access as m
import grixis_sim as sim

class Cycle120SourceTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.p=m.load(m.PLAN);cls.reg=m.load(m.REG);cls.old=m.load(m.PRIOR);cls.proto=m.load(m.PROTO)
 def test_exact_registered_three_decks_and_nine_opportunities(self):
  m.verify_plan(self.p,self.reg,self.old,self.proto)
  self.assertEqual(len(self.p["studies"]),3)
  self.assertEqual(sum(len(s["opportunities"]) for s in self.p["studies"]),9)
  self.assertEqual(len(self.reg["decks"]),62)
 def test_false_approval_or_reported_phase_b_does_not_pass(self):
  p=copy.deepcopy(self.p);p["authority"]["can_certify_M6"]=True
  with self.assertRaises(ValueError):m.verify_plan(p,self.reg,self.old,self.proto)
  proto=copy.deepcopy(self.proto);proto["observed_game_results"]=[{"invented_win":1}]
  with self.assertRaises(ValueError):m.verify_plan(self.p,self.reg,self.old,proto)
  p=copy.deepcopy(self.p);p["sampling"]["allow_mulligans"]=True
  with self.assertRaises(ValueError):m.verify_plan(p,self.reg,self.old,self.proto)
 def test_changed_source_raw_sha_m5_candidate_and_unknown_opportunity(self):
  p=copy.deepcopy(self.p);p["studies"][0]["approved_raw_sha256"]="0"*64
  with self.assertRaises(ValueError):m.verify_plan(p,self.reg,self.old,self.proto)
  p=copy.deepcopy(self.p);p["studies"][1]["swap_id"]="swap:invented"
  with self.assertRaises(ValueError):m.verify_plan(p,self.reg,self.old,self.proto)
  p=copy.deepcopy(self.p);p["studies"][2]["opportunities"][0]["id"]="fraudulent win"
  with self.assertRaises(ValueError):m.verify_plan(p,self.reg,self.old,self.proto)
 def test_source_opportunity_requires_correct_arm_and_present_card(self):
  names=["Mox Diamond","Island","Counterspell","Forest","Black Lotus"]+["Filler "+str(i) for i in range(94)]
  perm=list(range(99))
  landflags=[False,True,False,True,False]+[False]*94
  op={"id":"a","arm":"baseline","required_main":["Mox Diamond"]}
  self.assertTrue(m.sampled(perm,names,op,4,landflags))
  op["required_main"]=["Aphetto Alchemist"]
  self.assertFalse(m.sampled(perm,names,op,8,landflags))
 def test_spare_land_in_opening_is_distinct_from_seen_after_draws(self):
  names=["Mox Diamond"]+["Filler "+str(i) for i in range(7)]+["Swamp"]+["Filler rest "+str(i) for i in range(90)]
  self.assertEqual(len(names),99)
  flags=[name=="Swamp" for name in names]
  perm=list(range(99))
  op={"required_main":["Mox Diamond"],"extra_requirement":"at_least_one_other_land_in_opening_seven"}
  self.assertFalse(m.sampled(perm,names,op,8,flags))
  op["extra_requirement"]="at_least_one_other_land_in_seen"
  self.assertTrue(m.sampled(perm,names,op,4,flags))
 def test_physical_uid_and_first_seen_are_not_casts(self):
  names=["Aphetto Alchemist"]+["Filler "+str(i) for i in range(98)]
  perm=list(range(99))
  op={"required_main":["Aphetto Alchemist"]}
  x=m.witness(perm,names,op,8,42,0)
  self.assertEqual(x["source_card_ids"][0]["physical_uid"],"m000")
  self.assertEqual(x["source_card_ids"][0]["first_seen_turn"],0)
  self.assertFalse(x["assumed_cast_and_mana_payments"])
 def test_one_slot_aligned_random_permutation_preserves_slot(self):
  a=["Filler "+str(i) for i in range(98)]+["Opposition Agent"]
  b=["Filler "+str(i) for i in range(98)]+["Aphetto Alchemist"]
  self.assertEqual(sum(x!=y for x,y in zip(a,b)),1)
  for i in range(50):
   perm=random.Random(sim.seed_for(120026,i)^0x5EED).sample(range(99),99)
   for t in [4,8]:
    sample=perm[:7+t]
    self.assertEqual("Opposition Agent" in {a[j] for j in sample},
         "Aphetto Alchemist" in {b[j] for j in sample})
 def test_analytical_singleton_access_bound(self):
  # A source singleton by T8 under the prereg 7+8 draws is exactly 15/99.
  p=self.p["sampling"]
  self.assertEqual(p["opening_hand"]+p["turns"]*p["draws_per_turn"],15)
  self.assertEqual(round(15/99,6),0.151515)
  self.assertEqual(sim.wilson(0,8192)[0],0)
  self.assertLess(sim.wilson(0,8192)[1][1],0.001)
 def test_source_opportunities_do_not_claim_legally_castable_bolas_or_jewel(self):
  for study in self.p["studies"]:
   for opportunity in study["opportunities"]:
    self.assertIn("meaning",opportunity)
    self.assertNotIn("actual_win_rate",opportunity)
  self.assertFalse(self.p["authority"]["can_claim_effect_aware_paired_gameplay"])
 def test_bad_unknown_land_gate_fails_closed(self):
  p=copy.deepcopy(self.p)
  p["studies"][1]["opportunities"][0]["extra_requirement"]="guarantee cast Bolas"
  with self.assertRaises(ValueError):m.verify_plan(p,self.reg,self.old,self.proto)
 def test_m6_remains_unaccepted_and_lock_preserved(self):
  self.assertEqual(self.reg["program"]["milestones"]["M6"]["status"],"in_progress")
  self.assertTrue(all(v is False for v in self.p["authority"].values()))
  self.assertEqual(self.p["sampling"]["samples_per_deck"],8192)
 def test_example_witness_rejects_missing_required_source_card(self):
  names=["Mox Diamond"]+["Filler "+str(i) for i in range(98)]
  perm=list(range(99))
  with self.assertRaises(ValueError):
   m.witness(perm,names,{"required_main":["Aphetto Alchemist"]},4,42,0)

if __name__=="__main__":unittest.main()
