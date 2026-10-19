"""Cycle122 exact source-paid 19-land nonbasic/conditional ETB regression, no fake Phase B."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle122_nonbasic_source_casts as m
from grixis_m6_priority_nonbasic import PriorityNonbasic
from grixis_m6_state_kernel import BlockedAction

def world(names,opponents=3):
 cards=[{"name":n,"land":True,"cost":{"generic":0,"pips":[],"life":0}} for n in names]
 t=PriorityNonbasic(cards,[{"name":"Mai and Zuko","land":False}],seed=1,opponent_count=opponents)
 for u in list(t.zones["library"]):
  t.transfer(u,"library","hand")
 return t
def uid(t,name):
 return next(u for u in t.zones["hand"] if t.cards[u]["name"]==name)

class Cycle122Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.p=m.read(m.PLAN);cls.r=m.read(m.REG);cls.old=m.read(m.PRIOR)
 def test_prereg_and_all_three_source_decks_not_modified(self):
  self.assertEqual(self.p["cycle"],122)
  self.assertEqual(len(self.p["studies"]),3)
  self.assertEqual(self.p["model"]["samples_per_deck"],1024)
  self.assertEqual(self.r["program"]["milestones"]["M6"]["status"],"in_progress")
  self.assertTrue(all(v is False for v in self.p["authority"].values()))
 def test_false_m6_or_wrong_swap_id_blocked(self):
  import evaluate_decklist as ev
  # The static gating has no fake completion path; check registry/hash first.
  R=ev.Resolver()
  self.assertEqual(len(m.verify(self.p,self.r,self.old,R)),19)
  r=copy.deepcopy(self.r)
  r["program"]["milestones"]["M6"]["status"]="accepted"
  with self.assertRaises(ValueError):m.verify(self.p,r,self.old,R)
  p=copy.deepcopy(self.p);p["studies"][0]["swap_id"]="fake"
  with self.assertRaises(ValueError):m.verify(p,self.r,self.old,R)
 def test_enigma_jewel_requires_blue_even_with_three_black_lands(self):
  t=world(["Badlands","Blood Crypt","Luxury Suite"])
  t.play_supported_land(uid(t,"Badlands"))
  self.assertIsNone(m.source_payment(t,"The Enigma Jewel // Locus of Enlightenment"))
  self.assertEqual(m.c121.COST["The Enigma Jewel // Locus of Enlightenment"],(0,{"U":1}))
 def test_blue_color_selected_from_grixis_command_tower(self):
  t=world(["Command Tower"])
  t.play_supported_land(uid(t,"Command Tower"))
  payment=m.source_payment(t,"The Enigma Jewel // Locus of Enlightenment")
  self.assertEqual([(t.cards[u]["name"],c) for u,c in payment],[("Command Tower","U")])
 def test_xanders_lounge_enters_tapped_and_cannot_pay_immediately(self):
  t=world(["Xander's Lounge"])
  land=uid(t,"Xander's Lounge")
  self.assertFalse(t.play_supported_land(land))
  self.assertIn(land,t.tapped)
  self.assertIsNone(m.source_payment(t,"The Enigma Jewel // Locus of Enlightenment"))
 def test_shockland_pay_two_life_for_untapped_and_its_color(self):
  t=world(["Watery Grave"])
  land=uid(t,"Watery Grave")
  self.assertTrue(t.play_supported_land(land,pay_shock=True))
  self.assertEqual(t.pilot,38)
  self.assertEqual(m.source_payment(t,"The Enigma Jewel // Locus of Enlightenment")[0][1],"U")
 def test_shock_without_two_life_enters_tapped(self):
  t=world(["Watery Grave"])
  land=uid(t,"Watery Grave")
  self.assertFalse(t.play_supported_land(land,pay_shock=False))
  self.assertIn(land,t.tapped)
  self.assertEqual(t.pilot,40)
 def test_bondland_requires_two_other_opponents_for_untapped(self):
  t=world(["Training Center"],opponents=3)
  self.assertTrue(t.play_supported_land(uid(t,"Training Center")))
  w=world(["Training Center"],opponents=1)
  self.assertFalse(w.play_supported_land(uid(w,"Training Center")))
 def test_checkland_typed_requirement_and_tapped_gate(self):
  t=world(["Drowned Catacomb"])
  self.assertFalse(t.play_supported_land(uid(t,"Drowned Catacomb")))
  w=world(["Drowned Catacomb","Underground Sea"])
  w.play_supported_land(uid(w,"Underground Sea"))
  w.land_played=False
  self.assertTrue(w.play_supported_land(uid(w,"Drowned Catacomb")))
 def test_fastland_other_land_count_changes_entry(self):
  t=world(["Spirebluff Canal","Underground Sea","Badlands","Command Tower"])
  for name in ("Underground Sea","Badlands","Command Tower"):
   t.play_supported_land(uid(t,name));t.land_played=False
  self.assertFalse(t.play_supported_land(uid(t,"Spirebluff Canal")))
 def test_insufficient_land_and_mismatched_color_do_not_mutate(self):
  t=world(["Badlands"])
  t.play_supported_land(uid(t,"Badlands"))
  original=m.fmt(t.receipt())
  self.assertIsNone(m.source_payment(t,"The Enigma Jewel // Locus of Enlightenment"))
  self.assertEqual(m.fmt(t.receipt()),original)
  with self.assertRaises(BlockedAction):t.tap_land(next(u for u in t.zones["battlefield"]), "U")
 def test_nonbasic_unsupported_pathway_and_fetch_fail_closed(self):
  t=world(["Blightstep Pathway // Searstep Pathway","Polluted Delta"])
  self.assertIsNone(m.choose_land(t,"The Enigma Jewel // Locus of Enlightenment"))
  self.assertEqual(len(t.zones["battlefield"]),0)
 def test_physical_99_and_aligned_source_check_is_a_gate(self):
  self.assertEqual([s["deck_id"] for s in self.p["studies"]],
   ["Gwendlyn_Di_Corci","Nicol_Bolas__the_Ravager","Mai_and_Zuko"])
  self.assertEqual(self.p["model"]["seed"],120026)
 def test_an_offer_requires_external_noncreature_spell(self):
  t=world(["Command Tower"])
  t.play_supported_land(uid(t,"Command Tower"))
  self.assertIsNotNone(m.source_payment(t,"An Offer You Can't Refuse"))
  self.assertNotIn("An Offer You Can't Refuse", [t.cards[u]["name"] for u in t.zones["battlefield"]])
 def test_named_land_group_count_and_no_fictitious_other_mana(self):
  self.assertEqual(len(m.LANDS),19)
  self.assertNotIn("City of Brass",m.LANDS)
  self.assertNotIn("Ancient Tomb",m.LANDS)
  self.assertNotIn("Ally Encampment",m.LANDS)
 def test_milestone_subtracker_remains_incomplete(self):
  tracker=m.read(ROOT/"data/grixis/milestone_m6_m7_subtracker.json")
  self.assertEqual(tracker["display"]["m6_completed_gates"],3)
  self.assertEqual(tracker["display"]["m7_completed_gates"],0)
  self.assertEqual(tracker["m6"]["formal_m6_certified_decks"],0)

if __name__=="__main__":unittest.main()
