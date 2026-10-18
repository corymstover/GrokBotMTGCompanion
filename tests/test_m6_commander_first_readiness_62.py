"""Cycle111 adversarial 62-deck source and commander-identity triage tests."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_commander_first_readiness_62 as m

class Cycle111Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.registry=m.get(m.REG)
  cls.plan=m.get(m.PLAN)
  cls.deck=cls.registry["decks"]["Abaddon_the_Despoiler"]
  cls.packet=m.get(m.PACK/"abaddon-the-despoiler.json")
  cls.bp=m.get(m.BP/"abaddon-the-despoiler.json")
 def test_prereg_cannot_change_decks_or_decide(self):
  self.assertEqual(self.plan["cycle"],111)
  self.assertEqual(self.plan["roster_exact"],62)
  self.assertTrue(all(value is False for value in self.plan["authority"].values()))
 def test_approved_source_hash_cross_reference(self):
  c=m.checked_packet(self.packet,self.deck,self.bp)
  self.assertEqual(c["priority:P0_independent_agreement"],35)
  self.assertEqual(self.packet["counts"]["deep_review"],98)
  self.assertEqual(self.packet["list_hash"],self.bp["canonical_hash"])
 def test_tampered_packet_logical_hash_fails(self):
  bad=copy.deepcopy(self.packet)
  bad["list_hash"]="lh1:incorrect"
  with self.assertRaisesRegex(ValueError,"hash drift"):
   m.checked_packet(bad,self.deck,self.bp)
 def test_tampered_source_count_or_authority_fails(self):
  a=copy.deepcopy(self.packet)
  a["counts"]["deep_review"]+=1
  with self.assertRaises(ValueError):m.checked_packet(a,self.deck,self.bp)
  a=copy.deepcopy(self.packet)
  a["authority"]["can_decide"]=True
  with self.assertRaises(ValueError):m.checked_packet(a,self.deck,self.bp)
  a=copy.deepcopy(self.packet)
  a["items"][0]["candidate"]["screening_can_decide"]=True
  with self.assertRaises(ValueError):m.checked_packet(a,self.deck,self.bp)
 def test_protected_blueprint_identity_is_fatal_to_low_risk_label(self):
  x=copy.deepcopy(self.packet["items"][0])
  x["priority_class"]="P0_independent_agreement"
  x["flags"]=["test_pass"]
  identity=self.bp["identity_core"][0]["card"]
  x["cut"]=identity
  row=m.candidate_triage(x,self.bp)
  self.assertTrue(row["blueprint_identity_core_cut"])
  self.assertFalse(row["low_M5_triage_burden_only"])
  self.assertIn("CUTS_EXPLICIT_BLUEPRINT_IDENTITY_CORE",row["triage_caution_codes"])
 def test_designated_lutri_companion_only_registered_logical_hash_exception(self):
  deck=self.registry["decks"]["Cecily__Bjorna__Lutri"]
  packet=m.get(m.PACK/(deck["slug"]+".json"))
  bp=m.get(m.BP/(deck["slug"]+".json"))
  self.assertNotEqual(deck["baseline_hash"],deck["current_canonical_hash"])
  self.assertEqual(len(m.checked_packet(packet,deck,bp))>0,True)
  altered=copy.deepcopy(deck)
  altered["canonical_differs_from_source"]=[]
  with self.assertRaisesRegex(ValueError,"Unregistered baseline"):
   m.checked_packet(packet,altered,bp)
  altered=copy.deepcopy(deck)
  altered["deck_id"]="Other_Name"
  with self.assertRaises(ValueError):m.checked_packet(packet,altered,bp)
 def test_m5_pass_never_approves_or_establishes_performance(self):
  x=copy.deepcopy(self.packet["items"][0])
  x["priority_class"]="P0_independent_agreement"
  x["flags"]=["test_pass"]
  x["cut"]="hypothetical unprotected low-risk test slot"
  row=m.candidate_triage(x,self.bp)
  self.assertTrue(row["low_M5_triage_burden_only"])
  self.assertFalse(row["strategic_improvement_verified"])
  self.assertFalse(row["card_added_to_canonical_deck"])
  self.assertFalse(row["independent_commander_first_judgment_completed"])
 def test_stale_canonical_Goben_tracker_key_is_preserved_as_Norman_provenance(self):
  d=m.evaluate()
  n=next(x for x in d["ordered_decks"] if x["deck_id"]=="Norman_Osborn_Green_Goblin")
  self.assertEqual(n["source_canonical_legacy_deck_id_provenance"]["source_deck_id"],
                   "Goben__Gene_Splice_Savant")
  self.assertIn("Norman Osborn",n["commanders"][0])
 def test_62_inventory_no_invented_final_certifications(self):
  d=m.evaluate()
  self.assertEqual(d["deck_count"],62)
  self.assertEqual(d["blueprint_file_count"],62)
  self.assertEqual(d["packet_file_count"],62)
  self.assertEqual(len(d["ordered_decks"]),62)
  self.assertEqual(sum(d["aggregates"].get("deck_tier_"+x,0) for x in m.TIERS),62)
  self.assertFalse(d["M6_accepted"])
  self.assertFalse(d["can_issue_any_swap_recommendation"])
  self.assertFalse(d["all_62_actual_phase_b_and_independent_pass_c_completed"])
  self.assertFalse(d["current_official_legality_reverified"])
  for row in d["ordered_decks"]:
   self.assertFalse(row["any_swap_independently_approved_by_this_report"])
   self.assertFalse(row["named_independent_commander_judgment_completed"])
   self.assertFalse(row["formal_phase_b_ready_or_passed"])
   self.assertFalse(row["tested_pool_zero_improvement_certified"])
 def test_abaddon_specialized_hold_and_exception_preservation(self):
  d=m.evaluate()
  a=next(x for x in d["ordered_decks"] if x["deck_id"]=="Abaddon_the_Despoiler")
  self.assertEqual(a["Abaddon_prior_comparison"]["exact_comparative_conclusion"],"CANNOT_EVALUATE")
  b=next(x for x in d["ordered_decks"] if x["deck_id"]=="Cecily__Bjorna__Lutri")
  for card in ("Trade Secrets","Yawgmoth's Bargain","Lutri, the Spellchaser"):
   self.assertIn(card,b["intentional_project_exceptions"])
  self.assertTrue(any(x["intentional_future_release_exceptions"] for x in d["ordered_decks"]))
if __name__=="__main__":unittest.main()
