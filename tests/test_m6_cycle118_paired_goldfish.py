"""Cycle118 exact source, linked prereg and fail-closed M3 goldfish limitations tests."""
import copy, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle118_paired_goldfish as m

class Cycle118SourceBoundTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.plan=m.read(m.PLAN)
  cls.guard=m.read(m.GUARD)
  cls.proto=m.read(m.PROTO)
  cls.reg=m.read(m.REG)
  cls.queue=m.read(m.QUEUE)
 def test_three_accepted_m5_sources_have_exact_ids(self):
  m.verify_inputs(self.plan,self.guard,self.proto,self.reg,self.queue)
  self.assertEqual({x["deck_id"] for x in self.plan["benchmarks"]},set(m.NAMES))
  self.assertTrue(all(len(x["approved_raw_sha256"])==64 for x in self.plan["benchmarks"]))
 def test_must_reject_false_independent_phase_b_promotion(self):
  p=copy.deepcopy(self.plan);p["authority"]["can_certify_M6"]=True
  with self.assertRaises(ValueError):
   m.verify_inputs(p,self.guard,self.proto,self.reg,self.queue)
  pr=copy.deepcopy(self.proto);pr["phase_b_completed"]=True
  with self.assertRaises(ValueError):
   m.verify_inputs(self.plan,self.guard,pr,self.reg,self.queue)
 def test_must_reject_fake_source_swap_and_missing_deck(self):
  p=copy.deepcopy(self.plan)
  p["benchmarks"][0]["add"]="Demonic Tutor"
  with self.assertRaises(ValueError):
   m.verify_inputs(p,self.guard,self.proto,self.reg,self.queue)
  p=copy.deepcopy(self.plan);p["benchmarks"].pop()
  with self.assertRaises(ValueError):
   m.verify_inputs(p,self.guard,self.proto,self.reg,self.queue)
 def test_false_good_jewel_source_override_is_rejected(self):
  bad=copy.deepcopy(self.guard)
  bad["policy"]["apply_to_challenger_card_model"]["source"]=["C",2]
  with self.assertRaises(ValueError):
   m.verify_inputs(self.plan,bad,self.proto,self.reg,self.queue)
 def test_physical_exact_cut_only(self):
  a="1x Boss [Commander]\n1x Opposition Agent\n1x Swamp\n"
  out=m.replace_exact_slot(a,"Opposition Agent","Aphetto Alchemist")
  self.assertIn("1x Boss [Commander]",out)
  self.assertIn("1x Aphetto Alchemist",out)
  self.assertNotIn("Opposition Agent",out)
  with self.assertRaises(ValueError):
   m.replace_exact_slot(a,"Not in deck","Aphetto Alchemist")
  with self.assertRaises(ValueError):
   m.replace_exact_slot(a+"1x Opposition Agent\n","Opposition Agent","Aphetto Alchemist")
 def test_jewel_mana_cannot_be_spent_as_general_mana(self):
  source={"name":"The Enigma Jewel // Locus of Enlightenment","source":(frozenset("C"),2),
     "tapped":False,"v11":{"tutor":{"types":[]}}}
  class Deck:
   library=[source]
  before=m.model_capability_guard(Deck(),Deck(),source["name"])
  self.assertIsNone(source["source"])
  self.assertTrue(source["tapped"])
  self.assertEqual(source["v11"],{})
  self.assertEqual(before["applied_guard"],"Jewel inert castable artifact, does not provide general mana")
 def test_cycle117_scenarios_remain_unrun(self):
  self.assertFalse(self.proto["phase_b_completed"])
  self.assertEqual(self.proto["observed_game_results"],[])
  self.assertFalse(self.proto["formal_independent_pass_c_completed"])
 def test_model_is_goldfish_and_keeps_lock(self):
  self.assertEqual(self.plan["engine"]["model_version"],"1.1")
  self.assertEqual(self.plan["engine"]["samples_per_pair"],96)
  self.assertEqual(self.plan["engine"]["fixed_seed"],118026)
  self.assertTrue(all(not v for v in self.plan["authority"].values()))
  self.assertEqual(self.reg["program"]["milestones"]["M6"]["status"],"in_progress")

if __name__=="__main__":unittest.main()
