"""Cycle 102: four-player priority windows, basic-source payment and rollback."""
import sys,unittest,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from grixis_m6_priority_basics import PriorityBasics,BlockedAction
from grixis_m6_transactional_stack import SUPPORTED
import grixis_sim

def land(name):
 return {"name":name,"land":True,"cost":{"generic":0,"pips":[],"life":0},"mv":0}

def spell(name):
 return {"name":name,"land":False,"mv":{"Abaddon the Despoiler":5,"Kessig Flamebreather":2,
 "Dark Ritual":1,"Boltwave":1,"Flame Rift":2,"Arcane Signet":2}[name],
 "cost":grixis_sim.parse_cost(SUPPORTED[name]["cost"])}

def setup(items,command="Abaddon the Despoiler"):
 t=PriorityBasics([land(n) if n in ("Island","Swamp","Mountain") else spell(n)
                   for n in items],[spell(command)],seed=23)
 for u in list(t.zones["library"]):t.transfer(u,"library","hand")
 return t

def grab(t,name,zone="hand"):
 return next(u for u in t.zones[zone] if t.cards[u]["name"]==name)

class Cycle102Tests(unittest.TestCase):
 def test_four_passes_needed_to_resolve_spell(self):
  t=setup(["Swamp","Dark Ritual"])
  land_id=grab(t,"Swamp");t.play_basic(land_id)
  dark=grab(t,"Dark Ritual");t.cast_with_basic_sources(dark)
  self.assertEqual(t.zone_of(dark),"stack")
  for seat in range(3):
   self.assertEqual(t.priority_seat,seat)
   t.pass_priority()
   self.assertEqual(t.zone_of(dark),"stack")
  self.assertEqual(t.priority_seat,3)
  t.pass_priority()
  self.assertEqual(t.zone_of(dark),"graveyard")
  self.assertEqual(t.mana["B"],3)
  with self.assertRaises(BlockedAction):t.resolve_top()
  self.assertTrue(t.validate_stack())

 def test_insufficient_basic_sources_fail_before_tapping(self):
  t=setup(["Swamp","Arcane Signet"])
  s=grab(t,"Swamp");t.play_basic(s)
  a=grab(t,"Arcane Signet")
  state=copy.deepcopy((t.zones,t.tapped,t.mana,t.events,t.frames,t.priority_events))
  with self.assertRaises(BlockedAction):t.cast_with_basic_sources(a)
  self.assertEqual((t.zones,t.tapped,t.mana,t.events,t.frames,t.priority_events),state)
  self.assertEqual(t.zone_of(a),"hand")

 def test_two_actual_basics_pay_signet(self):
  t=setup(["Swamp","Island","Arcane Signet"])
  t.play_basic(grab(t,"Swamp"))
  t.next_turn()
  t.play_basic(grab(t,"Island"))
  a=grab(t,"Arcane Signet")
  paid=t.cast_with_basic_sources(a)
  self.assertEqual(len(paid),2)
  self.assertEqual(set(paid),set(t.tapped))
  self.assertEqual(t.mana["B"]+t.mana["U"],0)
  t.resolve_by_passes()
  self.assertEqual(t.zone_of(a),"battlefield")
  self.assertEqual(t.initial_card_count,4)
  self.assertTrue(t.check())

 def test_counter_only_during_opponent_priority(self):
  t=setup(["Swamp","Dark Ritual","Kessig Flamebreather","Mountain"])
  t.play_basic(grab(t,"Mountain"))
  t.next_turn()
  t.play_basic(grab(t,"Swamp"))
  k=grab(t,"Kessig Flamebreather")
  t.cast_with_basic_sources(k);t.resolve_by_passes()
  t.next_turn()
  r=grab(t,"Dark Ritual")
  t.cast_with_basic_sources(r)
  with self.assertRaises(BlockedAction):t.scripted_counter_spell(r)
  t.pass_priority() # seat 1 now has response window
  t.scripted_counter_spell(r)
  self.assertEqual(t.zone_of(r),"graveyard")
  self.assertEqual(t.priority_seat,0)
  t.resolve_by_passes()
  self.assertEqual(t.opponents_lost_this_turn,3)
  self.assertEqual(t.mana["B"],0)
  self.assertEqual(t.opponents,[39,38,30])
  self.assertTrue(t.check())

 def test_cascade_block_rolls_back_actual_land_taps(self):
  t=setup(["Mountain","Island","Swamp","Mountain","Mountain","Boltwave","Flame Rift"])
  # Fixture advances enough turns to establish Abaddon legally from five basics.
  for name in ("Mountain","Island","Swamp","Mountain","Mountain"):
   if t.land_played:t.next_turn()
   t.play_basic(grab(t,name))
  t.cast_with_basic_sources("c000",origin="command")
  t.resolve_by_passes()
  t.next_turn()
  bol=grab(t,"Boltwave");t.cast_with_basic_sources(bol);t.resolve_by_passes()
  f=grab(t,"Flame Rift")
  before=copy.deepcopy((t.zones,t.mana,t.tapped,t.frames,t.priority_events,t.events))
  with self.assertRaisesRegex(BlockedAction,"cascade"):t.cast_with_basic_sources(f)
  self.assertEqual((t.zones,t.mana,t.tapped,t.frames,t.priority_events,t.events),before)
  self.assertEqual(t.zone_of(f),"hand")

 def test_partial_priority_round_blocks_new_land_and_next_turn(self):
  t=setup(["Island","Swamp"])
  t.pass_priority()
  with self.assertRaises(BlockedAction):t.play_basic(grab(t,"Island"))
  with self.assertRaises(BlockedAction):t.next_turn()
  for _ in range(3):t.pass_priority()
  t.play_basic(grab(t,"Island"))
  self.assertEqual(t.turn,1)

 def test_basic_land_consumed_once_per_turn(self):
  t=setup(["Island","Swamp"])
  t.play_basic(grab(t,"Island"))
  with self.assertRaises(BlockedAction):t.play_basic(grab(t,"Swamp"))
  i=grab(t,"Island","battlefield")
  self.assertEqual(t.tap_basic(i),"U")
  with self.assertRaises(BlockedAction):t.tap_basic(i)
  t.next_turn()
  self.assertEqual(t.mana["U"],0)
  self.assertEqual(t.tap_basic(i),"U")

 def test_unsupported_and_wrong_priority_fail_without_mutation(self):
  t=setup(["Dark Ritual","Swamp"])
  t.play_basic(grab(t,"Swamp"))
  t.priority_seat=2
  before=copy.deepcopy((t.zones,t.mana,t.tapped,t.events,t.priority_events))
  with self.assertRaises(BlockedAction):t.cast_with_basic_sources(grab(t,"Dark Ritual"))
  self.assertEqual((t.zones,t.mana,t.tapped,t.events,t.priority_events),before)
  self.assertTrue(t.check())

if __name__=="__main__":unittest.main()
