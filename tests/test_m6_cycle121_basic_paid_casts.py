"""Cycle121: positive and negative physical-source basic-land-only cast tests."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle121_basic_paid_casts as m

def scene(names,target):
 return m.Physical(names+[f"Filler {i}" for i in range(99-len(names))],target,list(range(99)))
class Cycle121Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.plan=m.read(m.PLAN);cls.reg=m.read(m.REG);cls.prior=m.read(m.PRIOR)
 def test_source_plan_and_no_deck_changes(self):
  self.assertEqual(len(self.plan["studies"]),3)
  self.assertEqual(self.plan["sample_count_per_deck"],1024)
  self.assertEqual(self.reg["program"]["milestones"]["M6"]["status"],"in_progress")
  self.assertTrue(all(v==0 or v is False for v in self.plan["approval"].values()))
 def test_missing_approved_hash_and_forged_milestone_rejected(self):
  import evaluate_decklist as ev
  R=ev.Resolver()
  p=copy.deepcopy(self.plan);p["studies"][0]["approved_logical_hash"]="lh1:wrong"
  with self.assertRaises(m.Blocked):m.verify_plan(p,self.reg,self.prior,R)
  p=copy.deepcopy(self.plan);p["approval"]["m6_accepted"]=True
  with self.assertRaises(m.Blocked):m.verify_plan(p,self.reg,self.prior,R)
 def test_exact_aligned_source_slot_same_seed(self):
  self.assertEqual(m.EXPECTED["Gwendlyn_Di_Corci"],("Opposition Agent","Aphetto Alchemist"))
  self.assertEqual(len(set(m.random.Random(m.sim.seed_for(120026,1)^0x5EED).sample(range(99),99))),99)
 def test_mox_rejects_missing_basic_without_modification(self):
  w=scene(["Mox Diamond","Command Tower"],"Mox Diamond");w.draw(7)
  old=m.encode(w.z)
  self.assertFalse(w.mox_entry());self.assertEqual(m.encode(w.z),old)
 def test_mox_replacement_discards_actual_physical_basic(self):
  w=scene(["Mox Diamond","Island"],"Mox Diamond");w.draw(7)
  self.assertTrue(w.mox_entry())
  self.assertIn(("m000","Mox Diamond"),w.z["battlefield"])
  self.assertIn(("m001","Island"),w.z["graveyard"])
  self.assertEqual(w.mana,{})
  self.assertEqual(w.mox_basic_discard,1);w.check()
 def test_alchemist_requires_blue_and_two_basic_mana(self):
  w=scene(["Aphetto Alchemist","Island","Swamp"],"Aphetto Alchemist");w.draw(7)
  w.turn=1;w.land_drop();w.tap_basics()
  self.assertFalse(w.paid_simple_cast())
  w.turn=2;w.mana={};w.tapped.clear();w.land_drop();w.tap_basics()
  self.assertTrue(w.paid_simple_cast());self.assertEqual(w.first_cast,2);w.check()
 def test_no_blue_does_not_cast_or_consume_card(self):
  w=scene(["Aphetto Alchemist","Swamp","Mountain"],"Aphetto Alchemist");w.draw(7)
  w.turn=1;w.land_drop();w.tap_basics()
  old=m.encode(w.z);self.assertFalse(w.paid_simple_cast())
  self.assertEqual(m.encode(w.z),old)
 def test_nonbasic_mana_is_unsupported_not_free(self):
  w=scene(["Aetheric Amplifier","Command Tower"],"Aetheric Amplifier");w.draw(7)
  w.turn=1;w.land_drop();w.tap_basics()
  self.assertEqual(len(w.z["battlefield"]),0)
  self.assertFalse(w.paid_simple_cast())
 def test_an_offer_without_opponent_spell_never_cast(self):
  w=scene(["An Offer You Can't Refuse","Island"],"An Offer You Can't Refuse")
  w.draw(7);w.turn=1;w.land_drop();w.tap_basics()
  self.assertFalse(w.paid_simple_cast())
  self.assertEqual(w.payable_no_opponent,1)
  self.assertIsNone(w.first_cast)
 def test_jewel_enters_tapped_and_restricted_mana_unmodeled(self):
  jewel="The Enigma Jewel // Locus of Enlightenment"
  w=scene([jewel,"Island"],jewel);w.draw(7)
  w.turn=1;w.land_drop();w.tap_basics()
  self.assertTrue(w.paid_simple_cast())
  self.assertIn("m000",w.tapped)
  self.assertEqual(sum(w.mana.values()),0)
  w.check()
 def test_jewel_requires_blue_not_just_any_basic_land(self):
  jewel="The Enigma Jewel // Locus of Enlightenment"
  w=scene([jewel,"Swamp","Mountain"],jewel);w.draw(7)
  w.turn=1;w.land_drop();w.tap_basics()
  self.assertFalse(w.paid_simple_cast())
  self.assertIsNone(w.first_cast)
  self.assertTrue(w.hand(jewel))
 def test_pay_rejects_colored_shortfall_atomically(self):
  pool={"U":2}
  self.assertIsNone(m.pay(pool,(2,{"B":1})))
  self.assertEqual(pool,{"U":2})
  self.assertEqual(sum(m.pay({"U":1,"B":1},(1,{"U":1})).values()),0)
 def test_reject_physical_card_conservation_failure(self):
  w=scene(["Island"],"Aphetto Alchemist")
  w.z["library"].pop()
  with self.assertRaises(AssertionError):w.check()
 def test_oracle_mox_and_jewel_supported_rules_are_gated(self):
  self.assertIn("Mox Diamond",m.EXPECTED["Nicol_Bolas__the_Ravager"])
  self.assertNotIn("Mox Diamond",m.COST)
  self.assertEqual(m.COST["The Enigma Jewel // Locus of Enlightenment"],(0,{"U":1}))
 def test_milestone_and_performance_never_certified(self):
  self.assertTrue(self.plan["no_mulligans"])
  self.assertEqual(self.reg["program"]["milestones"]["M6"]["status"],"in_progress")
  self.assertEqual(self.plan["approval"]["formal_independent_pass_c"],0)
  self.assertEqual(self.plan["approval"]["swaps_applied"],0)
if __name__=="__main__":unittest.main()
