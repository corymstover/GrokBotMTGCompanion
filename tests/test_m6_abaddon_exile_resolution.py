"""Cycle109 real cascade exile cast, tutor/rock resolver and anti-fabrication tests."""
import sys,unittest,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_sim as sim
from grixis_m6_abaddon_exile_resolution import ActualCascade,ROLE,TUTOR_ORDER
from grixis_m6_state_kernel import BlockedAction

COST={"Bituminous Blast":"{3}{B}{R}","Mana Vault":"{1}","Sol Ring":"{1}",
 "Demonic Tutor":"{1}{B}","Vampiric Tutor":"{B}",
 "Boltwave":"{R}","Flame Rift":"{1}{R}",
 "Chrome Mox":"{0}","Windfall":"{2}{U}","Deflecting Swat":"{2}{R}"}
def card(n):
 lands={"Mountain","Swamp","Island","Command Tower","Volcanic Island"}
 return {"name":n,"land":n in lands,"mv":{"Bituminous Blast":5,
 "Mana Vault":1,"Sol Ring":1,"Demonic Tutor":2,"Vampiric Tutor":1,
 "Chrome Mox":0,"Windfall":3,"Deflecting Swat":3,
 "Boltwave":1,"Flame Rift":2}.get(n,0),
 "cost":sim.parse_cost(COST.get(n,""))}
def fixture(hit):
 cards=[card(n) for n in ["Bituminous Blast","Mountain","Swamp","Island","Command Tower","Volcanic Island",
  hit,"Boltwave","Flame Rift"]]
 commander={"name":"Abaddon the Despoiler","land":False,"mv":5,
            "cost":sim.parse_cost("{2}{U}{B}{R}")}
 t=ActualCascade(cards,[commander],seed=109)
 blast=next(u for u in t.zones["library"] if t.cards[u]["name"]=="Bituminous Blast")
 t.transfer(blast,"library","hand")
 for n in ("Mountain","Swamp","Island","Command Tower","Volcanic Island"):
  u=next(u for u in t.zones["library"] if t.cards[u]["name"]==n)
  t.transfer(u,"library","battlefield")
  # no actual played-turn restriction for known battlefield setup
 offered=next(u for u in t.zones["library"] if t.cards[u]["name"]==hit)
 t.zones["library"].remove(offered);t.zones["library"].insert(0,offered)
 return t,blast,offered

class ExileCastTests(unittest.TestCase):
 def test_ring_resolves_without_mana_and_no_hand_cascade(self):
  t,b,u=fixture("Sol Ring")
  t.transfer("c000","command","battlefield")
  t.opponents_lost_this_turn=5
  t.cast_with_land_sources(b)
  self.assertEqual(t.cascade_triggers,2)
  t.resolve_by_passes()
  self.assertEqual(t.zone_of(b),"graveyard")
  self.assertEqual(t.zone_of(u),"battlefield")
  self.assertEqual(t.executed_hits[0]["offered_from"],"exile")
  self.assertEqual(t.executed_hits[0]["mana_paid"],0)
  self.assertEqual(t.executed_hits[0]["colorless_mana_generated"],2)
  self.assertEqual(t.hit_cascade_triggers_created,0)
  self.assertTrue(t.check())
  self.assertEqual(t.zones["exile"],[])
 def test_mana_vault_is_3_colorless_without_fake_spell_use(self):
  t,b,u=fixture("Mana Vault")
  t.cast_with_land_sources(b);t.resolve_by_passes()
  x=t.executed_hits[0]
  self.assertEqual(x["name"],"Mana Vault")
  self.assertEqual(x["colorless_mana_generated"],3)
  self.assertEqual(x["colorless_mana_consumed_in_a_followup_spell"],0)
  self.assertEqual(t.zone_of(u),"battlefield")
  self.assertIn(u,t.tapped)
  prior_life=t.pilot
  t.next_turn()
  self.assertIn(u,t.tapped) # Mana Vault never untaps naturally.
  self.assertEqual(t.pilot,prior_life) # Upkeep trigger deliberately unresolved.
  self.assertEqual(t.unmodeled_vault_upkeep_triggers,1)
  self.assertEqual(t.outcome_events[-1]["event"],"mana_vault_upkeep_not_modeled")
 def test_demonic_tutor_searches_real_library_to_hand(self):
  t,b,u=fixture("Demonic Tutor")
  t.cast_with_land_sources(b);t.resolve_by_passes()
  x=t.executed_hits[0]
  self.assertEqual(x["result"]["chosen_from_physical_library"],"Boltwave")
  self.assertEqual(x["result"]["destination"],"hand")
  self.assertEqual(t.zone_of(x["result"]["chosen_uid"]),"hand")
  self.assertEqual(t.zone_of(u),"graveyard")
  self.assertEqual(sum(t.receipt()["zone_counts"].values()),10)
 def test_vampiric_puts_target_top_and_pays_two_life(self):
  t,b,u=fixture("Vampiric Tutor")
  t.cast_with_land_sources(b);t.resolve_by_passes()
  x=t.executed_hits[0]
  self.assertEqual(x["result"]["destination"],"top_of_library")
  self.assertEqual(x["result"]["chosen_from_physical_library"],"Boltwave")
  self.assertEqual(t.zone_of(x["result"]["chosen_uid"]),"library")
  self.assertEqual(t.zones["library"][0],x["result"]["chosen_uid"])
  self.assertEqual(t.pilot,38)
  self.assertEqual(t.drawn_names(t.draw(1)),["Boltwave"])
 def test_unmodeled_hit_is_declined_not_assigned_zero(self):
  t,b,u=fixture("Chrome Mox")
  t.cast_with_land_sources(b);t.resolve_by_passes()
  self.assertEqual(len(t.executed_hits),0)
  self.assertEqual(len(t.unknown_hits),1)
  self.assertEqual(t.unknown_hits[0]["potential_value"],"UNKNOWN_NOT_ZERO")
  self.assertEqual(t.zone_of(u),"library")
  self.assertEqual(t.zone_of(b),"graveyard")
 def test_spell_target_removed_after_cast_does_not_stop_tutor(self):
  t,b,u=fixture("Demonic Tutor")
  t.cast_with_land_sources(b)
  t.pass_priority();t.externally_remove_target()
  t.resolve_by_passes()
  self.assertEqual(t.blast_resolution,"FAILED_TO_RESOLVE_TARGET_ILLEGAL")
  self.assertEqual(t.executed_hits[0]["result"]["chosen_from_physical_library"],"Boltwave")
  self.assertEqual(t.zone_of(u),"graveyard")
 def test_card_id_never_duplicated_or_exiled_after_resolve(self):
  for n in ROLE:
   t,b,u=fixture(n)
   t.cast_with_land_sources(b);t.resolve_by_passes()
   self.assertEqual(len({u for z in t.zones.values() for u in z}),10)
   self.assertEqual(sum(map(len,t.zones.values())),10)
   self.assertEqual(t.zones["exile"],[])
   self.assertEqual(t.zones["stack"],[])
   self.assertTrue(t.validate_stack())

if __name__=="__main__":unittest.main()
