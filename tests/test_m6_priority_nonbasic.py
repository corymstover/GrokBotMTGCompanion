"""Cycle103: adversarial Oracle-modeled land entry, real source payment and fail-closed."""
import sys,unittest,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from grixis_m6_priority_nonbasic import PriorityNonbasic,LANDS,BlockedAction
import grixis_sim

def land(n):return {"name":n,"land":True,"cost":grixis_sim.parse_cost(""),"mv":0}
def spell(n):return {"name":n,"land":False,"cost":grixis_sim.parse_cost("{2}"),"mv":2}
def fixture(names,opponents=3):
 t=PriorityNonbasic([land(n) if n!="Arcane Signet" else spell(n) for n in names],
       [{"name":"Abaddon the Despoiler","land":False,"mv":5,
         "cost":grixis_sim.parse_cost("{2}{U}{B}{R}")}],
       seed=103,opponents=tuple([40]*opponents),opponent_count=opponents)
 for uid in list(t.zones["library"]):t.transfer(uid,"library","hand")
 return t
def find(t,name,zone="hand"):
 return next(i for i in t.zones[zone] if t.cards[i]["name"]==name)
def advance(t):t.next_turn()

class LandsTests(unittest.TestCase):
 def test_shock_enters_untapped_with_exact_two_life(self):
  t=fixture(["Watery Grave"])
  uid=find(t,"Watery Grave")
  self.assertTrue(t.play_supported_land(uid,pay_shock=True))
  self.assertEqual(t.pilot,38)
  self.assertNotIn(uid,t.tapped)
  self.assertEqual(t.tap_land(uid,"B"),"B")
  self.assertEqual(t.mana["B"],1)
  self.assertEqual(t.opponents_lost_this_turn,0)

 def test_shock_declines_life_enters_tapped_until_next_turn(self):
  t=fixture(["Steam Vents"])
  uid=find(t,"Steam Vents")
  self.assertFalse(t.play_supported_land(uid,pay_shock=False))
  self.assertIn(uid,t.tapped)
  with self.assertRaises(BlockedAction):t.tap_land(uid,"R")
  advance(t)
  self.assertEqual(t.tap_land(uid,"U"),"U")
  self.assertEqual(t.pilot,40)

 def test_typed_check_respects_dual_subtypes_even_when_tapped(self):
  t=fixture(["Watery Grave","Drowned Catacomb"])
  t.play_supported_land(find(t,"Watery Grave"),pay_shock=False)
  advance(t)
  uid=find(t,"Drowned Catacomb")
  self.assertTrue(t.play_supported_land(uid))
  self.assertNotIn(uid,t.tapped)
  self.assertEqual(t.tap_land(uid,"U"),"U")
  self.assertTrue(t.check())

 def test_typed_check_enters_tapped_without_enabler(self):
  t=fixture(["Dragonskull Summit"])
  uid=find(t,"Dragonskull Summit")
  self.assertFalse(t.play_supported_land(uid))
  self.assertIn(uid,t.tapped)

 def test_fastland_threshold(self):
  a=fixture(["Spirebluff Canal","Island","Swamp","Mountain","Command Tower"])
  a.play_supported_land(find(a,"Island"))
  advance(a);a.play_supported_land(find(a,"Swamp"))
  advance(a)
  fast=find(a,"Spirebluff Canal")
  self.assertTrue(a.play_supported_land(fast))
  b=fixture(["Spirebluff Canal","Island","Swamp","Mountain","Command Tower"])
  for n in ("Island","Swamp","Mountain"):
   b.play_supported_land(find(b,n));advance(b)
  fast2=find(b,"Spirebluff Canal")
  self.assertFalse(b.play_supported_land(fast2))
  self.assertIn(fast2,b.tapped)

 def test_bond_land_opponent_count(self):
  a=fixture(["Morphic Pool"],opponents=3)
  self.assertTrue(a.play_supported_land(find(a,"Morphic Pool")))
  b=fixture(["Morphic Pool"],opponents=1)
  self.assertFalse(b.play_supported_land(find(b,"Morphic Pool")))

 def test_triland_enters_tapped_and_produces_correct_colors(self):
  t=fixture(["Xander's Lounge"])
  uid=find(t,"Xander's Lounge")
  self.assertFalse(t.play_supported_land(uid))
  advance(t)
  self.assertEqual(t.tap_land(uid,"R"),"R")
  with self.assertRaises(BlockedAction):t.tap_land(uid,"U")
  self.assertEqual(t.mana["R"],1)

 def test_mana_confluence_exact_life_paid_controller_only(self):
  t=fixture(["Mana Confluence"])
  uid=find(t,"Mana Confluence")
  t.play_supported_land(uid)
  self.assertEqual(t.tap_land(uid,"B"),"B")
  self.assertEqual(t.pilot,39)
  self.assertEqual(t.opponents_lost_this_turn,0)
  self.assertEqual(t.opponents,[40,40,40])

 def test_real_dual_sources_cast_signet(self):
  t=fixture(["Watery Grave","Command Tower","Arcane Signet"])
  t.play_supported_land(find(t,"Watery Grave"),pay_shock=True)
  advance(t);t.play_supported_land(find(t,"Command Tower"))
  uid=find(t,"Arcane Signet")
  sources=t.cast_with_land_sources(uid)
  self.assertEqual(len(sources),2)
  self.assertEqual(set(sources),t.tapped)
  t.resolve_by_passes()
  self.assertEqual(t.zone_of(uid),"battlefield")
  self.assertEqual(t.pilot,38)
  self.assertEqual(sum(t.receipt()["zone_counts"].values()),4)

 def test_failed_cast_preserves_source_taps_and_life(self):
  t=fixture(["Mana Confluence","Arcane Signet"])
  t.play_supported_land(find(t,"Mana Confluence"))
  uid=find(t,"Arcane Signet")
  old=copy.deepcopy((t.zones,t.tapped,t.mana,t.pilot,t.priority_events,t.outcome_events))
  with self.assertRaises(BlockedAction):t.cast_with_land_sources(uid)
  self.assertEqual((t.zones,t.tapped,t.mana,t.pilot,t.priority_events,t.outcome_events),old)

 def test_unsupported_land_and_wrong_color_do_not_mutate(self):
  t=fixture(["City of Brass","Command Tower"])
  uid=find(t,"City of Brass")
  old=t.receipt()
  with self.assertRaises(BlockedAction):t.play_supported_land(uid)
  self.assertEqual(t.receipt(),old)
  c=find(t,"Command Tower")
  t.play_supported_land(c)
  with self.assertRaises(BlockedAction):t.tap_land(c,"G")
  self.assertEqual(t.mana["G"],0)
  self.assertNotIn(c,t.tapped)

 def test_life_ending_payments_fail_closed(self):
  t=fixture(["Mana Confluence"])
  uid=find(t,"Mana Confluence");t.play_supported_land(uid)
  t.pilot=1
  before=t.receipt()
  with self.assertRaises(BlockedAction):t.tap_land(uid,"U")
  self.assertEqual(t.receipt(),before)
  s=fixture(["Blood Crypt"]);s.pilot=2
  with self.assertRaises(BlockedAction):s.play_supported_land(find(s,"Blood Crypt"),pay_shock=True)
  self.assertEqual(s.zone_of(find(s,"Blood Crypt")),"hand")

if __name__=="__main__":unittest.main()
