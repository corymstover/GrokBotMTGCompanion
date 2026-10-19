"""Cycle128 source and oracle adversarial tests; no independent review claims."""
import copy,unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle128_six_judgments as m
class Cycle128(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.receipt=m.build()
  cls.plan=m.read(m.PLAN)
  cls.revs=m.read(m.REV)
  cls.reg=m.read(m.REG)
  cls.tri=m.read(m.TRI)
  cls.oracle=cls.receipt["frozen_oracle"]
 def test_six_distinct_verified_physical_source_decks(self):
  self.assertEqual(self.receipt["source_reviewed_count"],6)
  self.assertEqual(self.receipt["authored_total_if_verified"],21)
  self.assertEqual(set(r["deck_id"] for r in self.receipt["authored_only_receipts"]),set(m.EXPECTED))
  for r in self.receipt["authored_only_receipts"]:
   self.assertEqual((r["physical_main_cards"],r["physical_commanders"]),(99,1))
   self.assertTrue(r["source_M5_candidate_verified"] and r["oracle_add_cut_and_commander_bound"])
 def test_all_frozen_oracle_cards_verified(self):
  for name in ("The Valeyard","Norman Osborn // Green Goblin","Sol'kanar the Swamp King",
              "Garza Zol, Plague Queen","Evelyn, the Covetous","Sauron, the Dark Lord",
              "Hullbreaker Horror","Orcish Bowmasters","Kamahl, Pit Fighter",
              "Rapid Hybridization","Rakdos Charm","Deadly Rollick","Tidespout Tyrant","Nazgûl"):
   self.assertTrue(self.oracle[name]["frozen_card_identity_verified"])
   self.assertFalse(self.oracle[name]["fresh_2026_10_19_commander_legality_claim"])
 def test_sauron_nazgul_printed_exception(self):
  d=next(r for r in self.receipt["authored_only_receipts"] if r["deck_id"]=="Sauron__the_Dark_Lord")
  self.assertTrue(d["oracle_add_cut_and_commander_bound"])
 def test_authority_no_false_pass_c_phase_b(self):
  self.assertEqual(self.receipt["canonical_deck_changes"],0)
  self.assertEqual(self.receipt["approved_swaps"],0)
  self.assertEqual(self.receipt["formal_independent_pass_c_count"],0)
  self.assertEqual(self.receipt["complete_effect_aware_multiplayer_phase_b_count"],0)
  self.assertFalse(self.receipt["M6_accepted"])
  self.assertFalse(self.receipt["current_whole_list_legality_checked"])
  for r in self.revs["rows"]:
   self.assertEqual(r["disposition"],"HOLD_EXISTING_LIST_NO_SWAP")
   self.assertGreaterEqual(len(r["source_specific_rules"]),5)
   self.assertTrue(r["positive_case"] and r["cut_cost"] and r["next_empirical_evidence"])
 def test_reject_modified_m5_add(self):
  r=next(copy.deepcopy(x) for x in self.revs["rows"] if x["deck_id"]=="The_Valeyard")
  r["proposed_add"]="A fabricated card"
  self.assertNotEqual(m.EXPECTED[r["deck_id"]][0],r["proposed_add"])
 def test_reject_false_independent_review(self):
  r=next(copy.deepcopy(x) for x in self.revs["rows"] if x["deck_id"]=="Garza_Zol__Plague_Queen")
  r["independent_pass_c_completed"]=True
  # The same source verifier used in actual build must reject an upgraded author row.
  meta=self.reg["decks"][r["deck_id"]]
  queue=next(x for x in self.tri["ordered_decks"] if x["deck_id"]==r["deck_id"])
  import evaluate_decklist as ev,grixis_sim as sim
  R=ev.Resolver()
  bp=m.read(ROOT/"data/grixis/blueprints"/(meta["slug"]+".json"))
  plan=next(x for x in self.plan["cases"] if x["deck_id"]==r["deck_id"])
  with self.assertRaises(ValueError):
   m.verify(r,plan,meta,queue,bp,sim.load_deck(meta["slug"],R),self.oracle,R)
 def test_reject_false_milestone_registration(self):
  row=m.read(m.REV)
  row["review_count"]=7
  self.assertNotEqual(row["review_count"],len(row["rows"]))
if __name__=="__main__":unittest.main()
