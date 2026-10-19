"""Cycle114 adversarial source and Oracle checks; no altered approved deck."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle114_commander_reviews as m

class Source114Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.plan=m.read(m.PLAN);cls.reviews=m.read(m.REV)
  cls.registry=m.read(m.REG);cls.triage=m.read(m.TRIAGE)
  cls.result=m.run()
 def test_three_original_99_plus_command(self):
  d=self.result
  self.assertEqual(d["source_verified_deck_count"],3)
  self.assertEqual(set(x["deck_id"] for x in d["reviewed_decks"]),set(m.EXP))
  for x in d["reviewed_decks"]:
   self.assertEqual(x["actual_main_library_cards"],99)
   self.assertEqual(x["commander_count"],1)
   self.assertTrue(x["approved_cut_present"] and x["candidate_add_absent"])
   self.assertTrue(x["source_blueprint_core_preserved"])
 def test_adversarial_prereg_and_approved_raw_mismatch(self):
  item=copy.deepcopy(self.reviews["reviews"][0])
  did=item["deck_id"]
  meta=self.registry["decks"][did]
  bp=m.read(ROOT/"data/grixis/blueprints"/(item["slug"]+".json"))
  q=next(x for x in self.triage["ordered_decks"] if x["deck_id"]==did)
  plan=next(x for x in self.plan["candidates"] if x["deck_id"]==did)
  class Stub:
   commanders=[{"name":"Inalla, Archmage Ritualist"}]
   library=[{"name":"Blood Pet"}]+[{"name":"other-"+str(i)} for i in range(98)]
  item["approved_sha256"]="wrong"
  with self.assertRaises(ValueError):
   m.validate(item,plan,meta,bp,q,Stub(),self.result["oracle_checked"])
  item=copy.deepcopy(self.reviews["reviews"][0]);item["cut"]="Spellseeker"
  with self.assertRaises(ValueError):
   m.validate(item,plan,meta,bp,q,Stub(),self.result["oracle_checked"])
 def test_archived_oracle_specific_ability_gates(self):
  self.assertGreaterEqual(len(self.result["oracle_checked"]),13)
  for card in ("Pitiless Plunderer","Drafna, Founder of Lat-Nam","Aetheric Amplifier",
               "Curse of Opulence","Mox Diamond","Nicol Bolas, the Ravager // Nicol Bolas, the Arisen"):
   self.assertIn(card,self.result["oracle_checked"])
   self.assertTrue(self.result["oracle_checked"][card]["frozen_snapshot_not_live_current_legality"])
 def test_candidate_specific_decisions_not_certificates(self):
  r={x["deck_id"]:x for x in self.reviews["reviews"]}
  self.assertEqual(r["Inalla__Archmage_Ritualist"]["disposition"],"HOLD_EXISTING_LIST_NO_SWAP")
  self.assertEqual(r["The_Rani"]["disposition"],"HOLD_EXISTING_LIST_NO_SWAP")
  self.assertEqual(r["Nicol_Bolas__the_Ravager"]["disposition"],"PROMISING_UNRESOLVED_DIFFERENT_CUT_NEEDED")
  for x in r.values():
   self.assertFalse(x["swap_applied"])
   self.assertFalse(x["full_phase_b_complete"])
   self.assertFalse(x["official_current_legality_certified"])
   self.assertGreaterEqual(len(x["rules"]),4)
 def test_no_autoswap_or_independence(self):
  for k in ("formal_independent_Pass_C_count","full_effect_aware_phase_B_count","canonical_decks_modified","swaps_approved_or_applied"):
   self.assertEqual(self.result[k],0)
  self.assertFalse(self.result["M6_accepted"])
  self.assertFalse(self.result["current_official_legality_reverified"])
  self.assertTrue(all(v is False for v in self.result["authority"].values()))
 def test_m5_testpass_does_not_decide(self):
  self.assertTrue(all(x["source_M5_test_pass_not_card_effect_test"] for x in self.result["reviewed_decks"]))
  self.assertTrue(all(not x["zero_improvement_certified"] for x in self.result["reviewed_decks"]))

if __name__=="__main__":unittest.main()
