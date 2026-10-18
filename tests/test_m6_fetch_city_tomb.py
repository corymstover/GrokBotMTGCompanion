"""Cycle104 adversarial physical fetch, stack-trigger and utility mana tests."""
import sys,unittest,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from grixis_m6_fetch_city_tomb import PriorityFetchCityTomb,FETCHES,BlockedAction
from grixis_m6_transactional_stack import SUPPORTED
import grixis_sim
LANDS=set(FETCHES)|{"City of Brass","Ancient Tomb","Island","Swamp","Mountain",
 "Watery Grave","Steam Vents","Blood Crypt","Xander's Lounge","Command Tower"}

def make(name):
 if name in LANDS:return {"name":name,"land":True,"mv":0,
                         "cost":grixis_sim.parse_cost("")}
 return {"name":name,"land":False,"mv":2 if name=="Arcane Signet" else 1,
         "cost":grixis_sim.parse_cost(SUPPORTED[name]["cost"])}
def model(hand,rest=(),pilot=40):
 t=PriorityFetchCityTomb([make(x) for x in list(hand)+list(rest)],
                         [{"name":"Abaddon the Despoiler","land":False,"mv":5,
                           "cost":grixis_sim.parse_cost("{2}{U}{B}{R}")}],
                         seed=104,opponents=(40,39,31),pilot=pilot)
 for name in hand:
  uid=next(x for x in t.zones["library"] if t.cards[x]["name"]==name)
  t.transfer(uid,"library","hand")
 return t
def find(t,n,zone="hand"):
 return next(x for x in t.zones[zone] if t.cards[x]["name"]==n)

class Cycle104Rules(unittest.TestCase):
 def test_fetch_cost_sacrifice_then_four_pass_resolution_and_shuffle(self):
  t=model(["Polluted Delta"],["Island","Watery Grave","Arcane Signet"])
  src=find(t,"Polluted Delta");t.play_supported_land(src)
  pre_life=t.pilot
  t.activate_fetch(src)
  self.assertEqual(t.zone_of(src),"graveyard")
  self.assertEqual(t.pilot,pre_life-1)
  self.assertEqual(len(t.frames),1)
  self.assertEqual(len(t.fetch_search_events),0)
  for _ in range(3):t.pass_priority()
  self.assertEqual(len(t.fetch_search_events),0)
  t.pass_priority()
  rec=t.fetch_search_events[-1]
  self.assertEqual(rec["selected"],"Watery Grave")
  self.assertTrue(rec["library_shuffled"])
  self.assertTrue(rec["shock_paid_2_life"])
  self.assertEqual(t.pilot,37)
  self.assertIn(rec["selected_uid"],t.zones["battlefield"])
  self.assertNotIn(rec["selected_uid"],t.tapped)
  self.assertTrue(t.check())

 def test_fetch_graveyard_cost_persists_after_opponent_passes(self):
  t=model(["Bloodstained Mire"],["Mountain"])
  u=find(t,"Bloodstained Mire");t.play_supported_land(u);t.activate_fetch(u)
  with self.assertRaises(BlockedAction):t.activate_fetch(u)
  t.resolve_by_passes()
  self.assertEqual(t.fetch_search_events[-1]["selected"],"Mountain")
  self.assertEqual(t.zone_of(u),"graveyard")
  self.assertEqual(t.land_played,True)

 def test_fetch_without_eligible_modeled_target_shuffles_anyway(self):
  t=model(["Misty Rainforest"],["Swamp"])
  u=find(t,"Misty Rainforest");t.play_supported_land(u);t.activate_fetch(u)
  t.resolve_by_passes()
  e=t.fetch_search_events[-1]
  self.assertIsNone(e["selected"])
  self.assertTrue(e["library_shuffled"])
  self.assertEqual(t.zone_of(find(t,"Swamp","library")),"library")

 def test_fetch_rejects_low_life_without_changing_zones(self):
  t=model(["Scalding Tarn"],["Island"],pilot=1)
  u=find(t,"Scalding Tarn");t.play_supported_land(u)
  old=(copy.deepcopy(t.zones),t.pilot,copy.deepcopy(t.frames))
  with self.assertRaises(BlockedAction):t.activate_fetch(u)
  self.assertEqual(old,(t.zones,t.pilot,t.frames))

 def test_ancient_tomb_two_colorless_and_immediate_damage(self):
  t=model(["Ancient Tomb","Arcane Signet"])
  u=find(t,"Ancient Tomb");t.play_supported_land(u)
  a=find(t,"Arcane Signet")
  source=t.cast_with_land_sources(a)
  self.assertEqual(source,[u])
  self.assertEqual(t.pilot,38)
  self.assertEqual(t.mana["C"],0)
  self.assertEqual(t.zone_of(a),"stack")
  self.assertEqual([f["kind"] for f in t.frames],["spell"])
  t.resolve_by_passes()
  self.assertEqual(t.zone_of(a),"battlefield")
  self.assertEqual(t.opponents_lost_this_turn,0)
  self.assertTrue(t.check())

 def test_city_mana_immediate_but_damage_on_separate_trigger(self):
  t=model(["City of Brass"])
  u=find(t,"City of Brass");t.play_supported_land(u)
  t.tap_land(u,"U")
  self.assertEqual(t.mana["U"],1)
  self.assertEqual(t.pilot,40)
  self.assertEqual(t.frames[-1]["name"],"City of Brass")
  for _ in range(3):t.pass_priority()
  self.assertEqual(t.pilot,40)
  t.pass_priority()
  self.assertEqual(t.pilot,39)
  self.assertEqual(t.opponents_lost_this_turn,0)

 def test_city_trigger_survives_losing_source(self):
  t=model(["City of Brass"])
  u=find(t,"City of Brass");t.play_supported_land(u);t.tap_land(u,"B")
  t.pass_priority()
  t.scripted_remove_permanent(u)
  self.assertEqual(t.zone_of(u),"graveyard")
  t.resolve_by_passes()
  self.assertEqual(t.pilot,39)

 def test_city_cast_spends_mana_and_stacks_damage_above_spell(self):
  t=model(["City of Brass","Island","Arcane Signet"])
  c=find(t,"City of Brass");t.play_supported_land(c)
  t.next_turn();t.play_supported_land(find(t,"Island"))
  a=find(t,"Arcane Signet")
  t.cast_with_land_sources(a)
  self.assertEqual(t.frames[0]["name"],"Arcane Signet")
  self.assertEqual(t.frames[-1]["name"],"City of Brass")
  self.assertEqual(t.pilot,40)
  for _ in range(4):t.pass_priority()
  self.assertEqual(t.pilot,39)
  self.assertEqual(t.zone_of(a),"stack")
  t.resolve_by_passes()
  self.assertEqual(t.zone_of(a),"battlefield")

 def test_shock_fetch_model_creates_no_new_card_id(self):
  t=model(["Bloodstained Mire"],["Blood Crypt","Mountain"])
  orig=t.initial_inventory_hash
  u=find(t,"Bloodstained Mire");t.play_supported_land(u);t.activate_fetch(u)
  t.resolve_by_passes()
  self.assertEqual(t.initial_inventory_hash,orig)
  self.assertEqual(sum(t.receipt()["zone_counts"].values()),4)
  self.assertTrue(t.validate_stack())

 def test_unsupported_and_color_rejections_are_atomic(self):
  t=model(["City of Brass","Arcane Signet"])
  u=find(t,"City of Brass");t.play_supported_land(u)
  old=(copy.deepcopy(t.zones),copy.deepcopy(t.mana),t.pilot,copy.deepcopy(t.frames))
  with self.assertRaises(BlockedAction):t.tap_land(u,"G")
  self.assertEqual((t.zones,t.mana,t.pilot,t.frames),old)
  with self.assertRaises(BlockedAction):t.cast_with_land_sources(find(t,"Arcane Signet"))
  self.assertEqual((t.zones,t.mana,t.pilot,t.frames),old)

 def test_life_near_death_fails_closed(self):
  t=model(["Ancient Tomb"],pilot=2);u=find(t,"Ancient Tomb");t.play_supported_land(u)
  with self.assertRaises(BlockedAction):t.tap_land(u,"C")
  self.assertEqual(t.pilot,2)
  c=model(["City of Brass"],pilot=1);v=find(c,"City of Brass")
  c.play_supported_land(v)
  with self.assertRaises(BlockedAction):c.tap_land(v,"B")
  self.assertEqual(c.pilot,1)

 def test_priority_required_for_fetch_and_city_ability(self):
  t=model(["Polluted Delta"],["Island"])
  u=find(t,"Polluted Delta");t.play_supported_land(u)
  t.priority_seat=2
  with self.assertRaises(BlockedAction):t.activate_fetch(u)
  self.assertEqual(t.pilot,40)
  self.assertEqual(t.zone_of(u),"battlefield")

if __name__=="__main__":unittest.main()
