"""Cycle124 neutral independent critic intake: source correct, no synthetic Pass C."""
import copy,sys,unittest
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle124_reviewer_packets as m
import evaluate_decklist as ev
class ReviewerPacketTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.plan=m.read(m.PLAN);cls.reg=m.read(m.REG);cls.tracker=m.read(m.TRACK)
  cls.R=ev.Resolver()
 def test_preflight_approved_sources_and_no_promotions(self):
  m.validate_inputs(self.plan,self.reg,self.tracker,self.R)
  self.assertEqual(self.tracker["m6"]["formal_m6_certified_decks"],0)
  self.assertEqual(self.tracker["display"]["m7_completed_gates"],0)
 def test_three_registered_unique_exact_swap_sources(self):
  self.assertEqual({c["deck_id"] for c in self.plan["cases"]},set(m.CASES))
  self.assertEqual(len({c["source_m5_swap_id"] for c in self.plan["cases"]}),3)
  self.assertEqual(len(self.plan["cases"]),3)
 def test_packet_physical_100_one_card_only(self):
  for c in self.plan["cases"]:
   p=m.source_packet(c,self.reg,self.R)
   self.assertEqual(p["card_count_each"],100)
   self.assertEqual(len(p["baseline_list_including_commander"]),100)
   self.assertEqual(len(p["candidate_list_including_commander"]),100)
   self.assertEqual(sum(a!=b for a,b in zip(p["baseline_list_including_commander"],
                                          p["candidate_list_including_commander"])),1)
   self.assertEqual(p["unchanged_card_slots"],98)
 def test_personal_critic_identity_never_invented(self):
  receipt=m.generate()
  self.assertFalse(receipt["external_critic_assigned"])
  self.assertFalse(receipt["independence_verified"])
  self.assertEqual(receipt["formal_pass_c_completed"],0)
  self.assertEqual(receipt["external_critic_findings_observed"],0)
  self.assertTrue(all(x is None or x is False for x in
                      receipt["critic_response_intake_template"].values()))
 def test_packet_omits_author_verdict_and_proxy_win_rate(self):
  for pkt in m.generate()["packets"]:
   self.assertTrue(pkt["prior_author_outcome_not_disclosed"])
   self.assertIsNone(pkt["prior_author_recommendation"])
   self.assertFalse(pkt["strict_blind_independent_execution_claimed"])
   for forbidden in m.RESERVED:
    self.assertNotIn(forbidden,pkt)
 def test_each_packet_has_six_source_mechanic_questions(self):
  for p in m.generate()["packets"]:
   self.assertEqual(len(p["six_unanswered_nonleading_review_questions"]),6)
   self.assertEqual(len(p["archived_oracle"]),3)
   self.assertIn(p["option_approved_baseline"],p["archived_oracle"])
   self.assertIn(p["option_one_card_challenger"],p["archived_oracle"])
 def test_wrong_source_list_hash_rejected(self):
  p=copy.deepcopy(self.plan)
  p["cases"][0]["source_logical_hash"]="lh1:forged"
  with self.assertRaises(ValueError):
   m.validate_inputs(p,self.reg,self.tracker,self.R)
 def test_unknown_candidate_or_m5_swap_rejected(self):
  p=copy.deepcopy(self.plan)
  p["cases"][1]["candidate"]="Sol Ring"
  with self.assertRaises(ValueError):
   m.validate_inputs(p,self.reg,self.tracker,self.R)
  p=copy.deepcopy(self.plan);p["cases"][2]["source_m5_swap_id"]="swap:invented"
  with self.assertRaises(ValueError):
   m.validate_inputs(p,self.reg,self.tracker,self.R)
 def test_false_independent_reviewer_assignment_rejected(self):
  p=copy.deepcopy(self.plan);p["critic_intake"]["reviewer_id"]="invented reviewer"
  with self.assertRaises(ValueError):
   m.validate_inputs(p,self.reg,self.tracker,self.R)
 def test_m6_acceptance_and_proxy_phase_b_fake_rejected(self):
  p=copy.deepcopy(self.plan);p["reporting"]["formal_pass_c_complete"]=3
  with self.assertRaises(ValueError):
   m.validate_inputs(p,self.reg,self.tracker,self.R)
  r=copy.deepcopy(self.reg)
  r["program"]["milestones"]["M6"]["status"]="accepted"
  with self.assertRaises(ValueError):
   m.validate_inputs(self.plan,r,self.tracker,self.R)
 def test_tracker_not_marked_certified_by_packet_preparation(self):
  t=copy.deepcopy(self.tracker);t["display"]["m6_completed_gates"]=4
  with self.assertRaises(ValueError):
   m.validate_inputs(self.plan,self.reg,t,self.R)
 def test_enigma_oracle_blue_cost_and_commander_profile(self):
  p=next(x for x in m.generate()["packets"] if x["deck_id"]=="Mai_and_Zuko")
  self.assertEqual(p["archived_oracle"][m.JEWEL]["printed_mana_cost"].split(" // ")[0],"{U}") if hasattr(m,"JEWEL") else self.assertEqual(p["archived_oracle"]["The Enigma Jewel // Locus of Enlightenment"]["printed_mana_cost"].split(" // ")[0],"{U}")
  self.assertIn("artifact",p["commander_first_requirements_from_existing_blueprint"]["commander_first_primary_plan"].lower())
if __name__=="__main__":unittest.main()
