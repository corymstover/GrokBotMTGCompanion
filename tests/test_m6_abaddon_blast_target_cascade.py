"""Cycle107 tests: source-backed legal Blast, physical cascade and target responses."""
import sys,unittest,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_sim as sim
from grixis_m6_abaddon_blast_target_cascade import BlastCascade
from grixis_m6_state_kernel import BlockedAction

def model(name):
 costs={"Bituminous Blast":"{3}{B}{R}","Arcane Signet":"{2}",
        "Boltwave":"{R}","Flame Rift":"{1}{R}"}
 lands={"Mountain","Swamp","Island","Command Tower","Volcanic Island"}
 mv={"Bituminous Blast":5,"Arcane Signet":2,"Boltwave":1,"Flame Rift":2}
 return {"name":name,"land":name in lands,"mv":mv.get(name,0),
         "cost":sim.parse_cost(costs.get(name,""))}
def state(threshold=0,commander=False):
 names=["Bituminous Blast","Mountain","Swamp","Island","Command Tower",
        "Volcanic Island","Arcane Signet","Boltwave","Flame Rift"]
 cmd={"name":"Abaddon the Despoiler","land":False,"mv":5,
      "cost":sim.parse_cost("{2}{U}{B}{R}")}
 t=BlastCascade([model(x) for x in names],[cmd],seed=707)
 blast=next(uid for uid in t.zones["library"] if t.cards[uid]["name"]=="Bituminous Blast")
 t.transfer(blast,"library","hand")
 for name in ("Mountain","Swamp","Island","Command Tower","Volcanic Island"):
  uid=next(uid for uid in t.zones["library"] if t.cards[uid]["name"]==name)
  t.transfer(uid,"library","battlefield")
 if commander:t.transfer("c000","command","battlefield")
 t.opponents_lost_this_turn=threshold
 if threshold:t.opponents[0]-=threshold
 return t,blast
class PhysicalBlastTests(unittest.TestCase):
 def test_one_printed_cascade_without_commander(self):
  t,u=state()
  paid=t.cast_with_land_sources(u)
  self.assertEqual(len(paid),5)
  self.assertEqual(t.cascade_triggers,1)
  self.assertEqual(t.zone_of(u),"stack")
  t.resolve_by_passes()
  self.assertEqual(t.cascade_resolved,1)
  self.assertEqual(t.blast_resolution,"REMOVED_EXTERNAL_3_3_BY_FOUR_DAMAGE")
  self.assertEqual(t.target_damage,4)
  self.assertEqual(t.zone_of(u),"graveyard")
  self.assertEqual(t.zones["exile"],[])
  self.assertEqual(len(t.cascade_offers),1)
  self.assertTrue(t.check())
 def test_two_independent_cascades_threshold_at_cast(self):
  t,u=state(threshold=5,commander=True)
  t.cast_with_land_sources(u)
  self.assertEqual(t.cascade_triggers,2)
  t.resolve_by_passes()
  self.assertEqual(t.cascade_resolved,2)
  self.assertEqual(len(t.cascade_offers),2)
  self.assertEqual({x["trigger"] for x in t.cascade_offers},{"printed","Abaddon_granted"})
  for row in t.cascade_offers:
   if row["eligible_uid"]:
    self.assertLess(row["eligible_mv"],5)
    self.assertEqual(row["possible_effect_value"],"UNKNOWN_NOT_ZERO")
    self.assertEqual(row["controller_choice"],"decline_optional_cast")
  self.assertEqual(t.zones["exile"],[])
  self.assertTrue(t.check())
 def test_target_removed_after_cast_cascade_still_resolves(self):
  t,u=state()
  t.cast_with_land_sources(u)
  with self.assertRaises(BlockedAction):t.externally_remove_target()
  t.pass_priority()
  t.externally_remove_target()
  t.resolve_by_passes()
  self.assertEqual(t.blast_resolution,"FAILED_TO_RESOLVE_TARGET_ILLEGAL")
  self.assertEqual(t.target_damage,0)
  self.assertEqual(t.cascade_resolved,1)
  self.assertEqual(t.zone_of(u),"graveyard")
  self.assertTrue(t.check())
 def test_target_absent_at_cast_does_not_spend_mana(self):
  t,u=state();t.target_alive=False
  old=copy.deepcopy((t.zones,t.tapped,t.mana,t.frames,t.events,t.priority_events))
  with self.assertRaises(BlockedAction):t.cast_with_land_sources(u)
  self.assertEqual((t.zones,t.tapped,t.mana,t.frames,t.events,t.priority_events),old)
  self.assertEqual(t.zone_of(u),"hand")
 def test_cast_trigger_order_no_fictitious_granted_cascade(self):
  t,u=state(threshold=0,commander=True)
  t.cast_with_land_sources(u)
  self.assertEqual(t.cascade_triggers,1)
  self.assertEqual(t.frames[-1]["why"],"printed")
  t.resolve_by_passes()
  self.assertTrue(t.check())
 def test_cascade_reveals_first_eligible_nonland_and_uses_real_ids(self):
  t,u=state()
  ids=t.zones["library"]
  land=next(x for x in ids if t.cards[x]["name"]=="Arcane Signet")
  # Make Arcane Signet top of current physical library, then other spell.
  t.zones["library"].remove(land);t.zones["library"].insert(0,land)
  t.cast_with_land_sources(u);t.resolve_by_passes()
  x=t.cascade_offers[0]
  self.assertEqual(x["eligible_name"],"Arcane Signet")
  self.assertEqual(x["eligible_uid"],land)
  self.assertEqual(x["number_of_revealed"],1)
  self.assertEqual(t.zone_of(land),"library")
  self.assertTrue(t.check())

if __name__=="__main__":unittest.main()
