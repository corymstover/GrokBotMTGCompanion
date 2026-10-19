"""Cycle119 bounded effect witnesses: positive and adversarial rules/authority regression."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle119_bounded_effects as m

class Cycle119WitnessTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.plan=m.read(m.PLAN)
  cls.registry=m.read(m.SOURCE)
  cls.queue=m.read(m.QUEUE)
  cls.protocol=m.read(m.ORIG)
 def test_preregistered_source_authority(self):
  m.check_plan(self.plan,self.registry,self.queue,self.protocol)
  self.assertEqual(len(self.plan["studies"]),3)
  self.assertEqual({x["id"] for x in self.plan["scenarios"]},set(m.SCENARIOS))
  self.assertEqual(len(self.registry["decks"]),62)
 def test_six_bounded_world_scenarios_execute(self):
  for key,func in m.SCENARIOS.items():
   out=func()
   self.assertIn("baseline",out,key)
   self.assertIn("challenger",out,key)
  self.assertEqual(m.gw_legal()["challenger"]["gwendlyn_activations"],2)
  self.assertEqual(m.gw_adverse()["baseline"]["opponent_searches_controlled"],1)
  self.assertEqual(m.ravager_deploy()["baseline"]["ravager_cast_from_fixture"],True)
  self.assertEqual(m.ravager_loyalty()["challenger"]["loyalty"],10)
  self.assertEqual(m.mai_ability()["challenger"]["ordinary_C_after_one_cycle"],3)
  self.assertEqual(m.mai_counter()["baseline"]["opponent_treasures"],2)
 def test_gwendlyn_turn_restriction_and_sickness(self):
  w=m.World(["Gwendlyn Di Corci"],own_turn=False,controlled_since_turn=["Gwendlyn Di Corci"],target_hand=3)
  self.assertTrue(m.blocked_unchanged(w,lambda:m.gw_discard(w)))
  w=m.World(["Gwendlyn Di Corci"],own_turn=True,target_hand=3)
  self.assertTrue(m.blocked_unchanged(w,lambda:m.gw_discard(w)))
  w=m.World(["Gwendlyn Di Corci"],controlled_since_turn=["Gwendlyn Di Corci"],target_hand=0)
  self.assertTrue(m.blocked_unchanged(w,lambda:m.gw_discard(w)))
 def test_shroud_blocks_own_untap_and_sick_alchemist(self):
  w=m.World(["Aphetto Alchemist","Gwendlyn Di Corci"],
       controlled_since_turn=["Gwendlyn Di Corci"],shrouded=["Gwendlyn Di Corci"])
  w.tapped.add("Gwendlyn Di Corci")
  self.assertTrue(m.blocked_unchanged(w,lambda:m.gw_alchemist(w)))
  w.shrouded.clear()
  self.assertTrue(m.blocked_unchanged(w,lambda:m.gw_alchemist(w)))
 def test_mox_diamond_spare_land_precondition_and_no_phantom_ravager(self):
  w=m.World(["Mox Diamond"],mana={"C":1,"U":1,"B":1})
  self.assertTrue(m.blocked_unchanged(w,lambda:m.mox_diamond(w,False)))
  self.assertTrue(m.blocked_unchanged(w,lambda:m.cast_bolas_from_pool(w)))
 def test_amplifier_cannot_activate_at_opponent_priority_or_without_generic(self):
  w=m.World(["Aetheric Amplifier"],mana={"C":3})
  self.assertTrue(m.blocked_unchanged(w,lambda:m.amplifier_loyalty(w,5)))
  w=m.World(["Aetheric Amplifier"],mana={"C":5},own_turn=False)
  self.assertTrue(m.blocked_unchanged(w,lambda:m.amplifier_loyalty(w,5)))
  w=m.World(["Aetheric Amplifier"],mana={"C":5},main_phase=False)
  self.assertTrue(m.blocked_unchanged(w,lambda:m.amplifier_loyalty(w,5)))
  w=m.World(["Aetheric Amplifier"],mana={"C":5},stack_empty=False)
  self.assertTrue(m.blocked_unchanged(w,lambda:m.amplifier_loyalty(w,5)))
 def test_restricted_jewel_mana_never_casts_spells(self):
  jewel="The Enigma Jewel // Locus of Enlightenment"
  w=m.World([jewel],controlled_since_turn=[jewel])
  m.jewel_tap(w)
  self.assertEqual(w.restricted_C,2)
  self.assertTrue(m.blocked_unchanged(w,lambda:w.spend({"generic":1},restricted_allowed=False)))
  w.spend({"generic":2},restricted_allowed=True)
  self.assertEqual(w.restricted_C,0)
 def test_atomic_rejected_generic_cost_and_no_mana_invention(self):
  w=m.World(["Basalt Monolith"],mana={"C":2,"U":1})
  self.assertTrue(m.blocked_unchanged(w,lambda:w.spend({"B":1,"generic":2})))
  self.assertTrue(m.blocked_unchanged(w,lambda:w.spend({"generic":4})))
 def test_basalt_nonmana_activated_copy_one_finite_cycle(self):
  outcome=m.mai_ability()
  self.assertEqual(outcome["baseline"]["ordinary_C_after_one_cycle"],0)
  self.assertEqual(outcome["challenger"]["ordinary_C_after_one_cycle"],3)
  self.assertEqual(outcome["challenger"]["spent_restricted_C_on_rings_trigger"],2)
  self.assertEqual(outcome["challenger"]["untap_resolutions"],2)
  self.assertTrue(outcome["challenger"]["entered_tapped_blocked_tap"])
 def test_an_offer_cannot_counter_creatures(self):
  w=m.World(["An Offer You Can't Refuse"],mana={"U":1})
  self.assertTrue(m.blocked_unchanged(w,lambda:m.an_offer(w,noncreature=False)))
  self.assertFalse(m.mai_counter()["challenger"]["noncreature_spell_countered_by_jewel"])
 def test_adversarial_false_authority_and_source_m5_id_fails(self):
  fake=copy.deepcopy(self.plan);fake["authority"]["can_accept_m6"]=True
  with self.assertRaises(ValueError):
   m.check_plan(fake,self.registry,self.queue,self.protocol)
  fake=copy.deepcopy(self.plan);fake["studies"][0]["swap_id"]="invalid"
  with self.assertRaises(ValueError):
   m.check_plan(fake,self.registry,self.queue,self.protocol)
  fake=copy.deepcopy(self.plan);fake["studies"][1]["source_raw_sha256"]="0"*64
  with self.assertRaises(ValueError):
   m.check_plan(fake,self.registry,self.queue,self.protocol)
 def test_no_promotion_of_executed_fixtures_to_independent_pass_c(self):
  self.assertEqual(len(m.SCENARIOS),6)
  self.assertFalse(self.protocol["formal_independent_pass_c_completed"])
  self.assertEqual(self.protocol["observed_game_results"],[])
  self.assertFalse(self.protocol["phase_b_completed"])
  self.assertTrue(all(v is False for v in self.plan["authority"].values()))

if __name__=="__main__":unittest.main()
