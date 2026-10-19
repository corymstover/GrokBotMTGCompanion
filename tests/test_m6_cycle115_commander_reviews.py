"""Cycle115 source-bound commander identity, adversarial and nonpromotion tests."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle115_commander_reviews as m
class Cycle115Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.result=m.run();cls.plan=m.read(m.PLAN);cls.review=m.read(m.REV)
  cls.registry=m.read(m.REG);cls.tri=m.read(m.TRIAGE)
 def test_three_real_decks_and_partners(self):
  d=self.result
  self.assertEqual(d["source_verified_deck_count"],3)
  a={x["deck_id"]:x for x in d["reviewed_decks"]}
  self.assertEqual(set(a),set(m.EXPECTED))
  self.assertEqual((a["RogSi"]["main_library_card_count"],a["RogSi"]["commander_count"]),(98,2))
  self.assertEqual((a["Nicol_Bolas"]["main_library_card_count"],a["Nicol_Bolas"]["commander_count"]),(99,1))
  self.assertEqual((a["Mai_and_Zuko"]["main_library_card_count"],a["Mai_and_Zuko"]["commander_count"]),(99,1))
  for x in a.values():
   self.assertTrue(x["candidate_add_absent"] and x["candidate_cut_present"])
   self.assertTrue(x["nonbasic_singleton_pass"] and x["source_blueprint_hash_match"] and x["m5_swap_id_match"])
 def test_oracle_semantic_coverage(self):
  o=self.result["oracle_checked"]
  for name in ("The Enigma Jewel // Locus of Enlightenment","Birgi, God of Storytelling // Harnfel, Horn of Bounty","Nicol Bolas","Volcano Hellion","Mai and Zuko","Basalt Monolith","Rings of Brighthearth"):
   self.assertIn(name,o)
   self.assertTrue(o[name]["frozen_archive_not_current_legality"])
 def test_adversarial_hash_and_commanders(self):
  item=copy.deepcopy(self.review["items"][0]);did=item["deck_id"];slug=m.EXPECTED[did][0]
  planned=next(v for v in self.plan["decks"] if v["id"]==did)
  meta=self.registry["decks"][did]
  blueprint=m.read(ROOT/"data/grixis/blueprints"/(slug+".json"))
  queue=next(v for v in self.tri["ordered_decks"] if v["deck_id"]==did)
  class Stub:
   commanders=[{"name":"Rograkh, Son of Rohgahh"},{"name":"Silas Renn, Seeker Adept"}]
   library=[{"name":"Birgi, God of Storytelling // Harnfel, Horn of Bounty"}]+[{"name":"other-"+str(i)} for i in range(97)]
  item["approved_raw_sha256"]="f"*64
  with self.assertRaises(ValueError):
   m.validate(item,planned,meta,blueprint,queue,Stub(),self.result["oracle_checked"])
  item=copy.deepcopy(self.review["items"][0]);item["cut"]="Mystic Remora"
  with self.assertRaises(ValueError):
   m.validate(item,planned,meta,blueprint,queue,Stub(),self.result["oracle_checked"])
  item=copy.deepcopy(self.review["items"][0])
  bad=copy.deepcopy(meta);bad["commanders"]=["Silas Renn, Seeker Adept"]
  with self.assertRaises(ValueError):
   m.validate(item,planned,bad,blueprint,queue,Stub(),self.result["oracle_checked"])
 def test_adversarial_false_independence(self):
  item=copy.deepcopy(self.review["items"][0]);item["independent_review"]=True
  did=item["deck_id"];slug=m.EXPECTED[did][0]
  plan=next(v for v in self.plan["decks"] if v["id"]==did)
  bp=m.read(ROOT/"data/grixis/blueprints"/(slug+".json"))
  queue=next(v for v in self.tri["ordered_decks"] if v["deck_id"]==did)
  class Stub:
   commanders=[{"name":"Rograkh, Son of Rohgahh"},{"name":"Silas Renn, Seeker Adept"}]
   library=[{"name":"Birgi, God of Storytelling // Harnfel, Horn of Bounty"}]+[{"name":"other-"+str(i)} for i in range(97)]
  with self.assertRaises(ValueError):
   m.validate(item,plan,self.registry["decks"][did],bp,queue,Stub(),self.result["oracle_checked"])
 def test_no_approval_or_false_certificates(self):
  for key in ("formal_independent_pass_c_count","full_effect_aware_phase_b_count","canonical_decks_modified","swaps_approved_or_applied"):
   self.assertEqual(self.result[key],0)
  for key in ("M6_accepted","whole_deck_legality_currently_verified","fresh_original_source_bytes_rehashed"):
   self.assertFalse(self.result[key])
  self.assertTrue(all(v is False for v in self.result["authority"].values()))
  self.assertTrue(all(not x["card_swap_applied"] and not x["formal_independent_pass_c"] for x in self.result["reviewed_decks"]))
if __name__=="__main__":unittest.main()
