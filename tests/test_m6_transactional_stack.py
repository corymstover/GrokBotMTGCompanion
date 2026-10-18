"""Cycle 101 bounded spell stack tests: physical IDs, payment, response and rollback."""
import sys,unittest,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from grixis_m6_transactional_stack import TransactionalLedger,BlockedAction,SUPPORTED
import grixis_sim

def card(name):
 info=SUPPORTED[name]
 return {"name":name,"land":False,"mv":{"Abaddon the Despoiler":5,"Kessig Flamebreather":2,
    "Dark Ritual":1,"Boltwave":1,"Flame Rift":2,"Arcane Signet":2}[name],
   "cost":grixis_sim.parse_cost(info["cost"])}

def state(names=("Kessig Flamebreather","Dark Ritual","Boltwave","Flame Rift","Arcane Signet")):
 t=TransactionalLedger([card(n) for n in names],[card("Abaddon the Despoiler")],seed=101)
 for id_ in list(t.zones["library"]):t.transfer(id_,"library","hand")
 return t

def uid(st,name,zone=None):
 return next(i for i in (st.zones[zone] if zone else st.cards) if st.cards[i]["name"]==name)

class TransactionalKernelTests(unittest.TestCase):
 def test_real_mana_cost_and_commander_tax(self):
  t=state()
  t.inject_mana({"U":2,"B":2,"R":2,"C":6})
  commander="c000"
  t.cast(commander,origin="command")
  self.assertEqual(t.zone_of(commander),"stack")
  t.resolve_all()
  self.assertEqual(t.zone_of(commander),"battlefield")
  t.commander_to_command(commander)
  t.cast(commander,origin="command")
  casts=[x for x in t.outcome_events if x["event"]=="supported_cast"]
  self.assertEqual([x["paid_tax"] for x in casts],[0,2])
  t.resolve_all()
  self.assertEqual(t.command_casts[commander],2)
  self.assertEqual(t.zone_of(commander),"battlefield")
  self.assertTrue(t.validate_stack())

 def test_color_restrictions_and_atomic_failed_cast(self):
  t=state()
  t.inject_mana({"C":10,"R":1})
  dark=uid(t,"Dark Ritual","hand")
  before=copy.deepcopy((t.zones,t.mana,t.outcome_events,t.frames,t.events))
  with self.assertRaises(BlockedAction):t.cast(dark)
  self.assertEqual((t.zones,t.mana,t.outcome_events,t.frames,t.events),before)
  t.inject_mana({"B":1})
  t.cast(dark)
  self.assertEqual(t.mana["B"],0)
  t.resolve_all()
  self.assertEqual(t.mana["B"],3)
  self.assertEqual(t.zone_of(dark),"graveyard")

 def test_kessig_trigger_survives_countered_dark_ritual(self):
  t=state()
  t.inject_mana({"R":2,"C":1,"B":1})
  k=uid(t,"Kessig Flamebreather","hand")
  d=uid(t,"Dark Ritual","hand")
  t.cast(k);t.resolve_all()
  t.cast(d)
  self.assertEqual(len(t.frames),2)
  self.assertEqual(t.frames[-1]["kind"],"trigger")
  t.scripted_counter_spell(d)
  self.assertEqual(t.zone_of(d),"graveyard")
  self.assertEqual(len(t.frames),1)
  t.resolve_all()
  self.assertEqual(t.opponents,[39,38,30])
  self.assertEqual(t.opponents_lost_this_turn,3)
  self.assertEqual(t.mana["B"],0)
  self.assertTrue(t.validate_stack())

 def test_kessig_trigger_survives_source_removal(self):
  t=state();t.inject_mana({"R":2,"B":1,"C":1})
  k=uid(t,"Kessig Flamebreather","hand")
  d=uid(t,"Dark Ritual","hand")
  t.cast(k);t.resolve_all()
  t.cast(d);t.scripted_remove_permanent(k)
  t.resolve_all()
  self.assertEqual(t.zone_of(k),"graveyard")
  self.assertEqual(t.opponents_lost_this_turn,3)
  self.assertEqual(t.mana["B"],3)

 def test_boltwave_flame_rift_actual_damage_and_zones(self):
  t=state();t.inject_mana({"R":3,"C":2})
  a=uid(t,"Boltwave","hand");b=uid(t,"Flame Rift","hand")
  t.cast(a);t.resolve_all()
  self.assertEqual(t.opponents,[37,36,28])
  self.assertEqual(t.opponents_lost_this_turn,9)
  t.cast(b);t.resolve_all()
  self.assertEqual(t.opponents,[33,32,24])
  self.assertEqual(t.opponents_lost_this_turn,21)
  self.assertEqual(t.pilot,36)
  self.assertEqual(t.zone_of(a),"graveyard")
  self.assertEqual(t.zone_of(b),"graveyard")

 def test_abaddon_granted_cascade_blocks_before_mana_or_zone(self):
  t=state();t.inject_mana({"U":2,"B":2,"R":4,"C":8})
  t.cast("c000",origin="command");t.resolve_all()
  bol=uid(t,"Boltwave","hand");flame=uid(t,"Flame Rift","hand")
  t.cast(bol);t.resolve_all()
  self.assertEqual(t.opponents_lost_this_turn,9)
  before=copy.deepcopy((t.zones,t.mana,t.frames,t.events,t.outcome_events))
  with self.assertRaisesRegex(BlockedAction,"cascade"):t.cast(flame)
  self.assertEqual((t.zones,t.mana,t.frames,t.events,t.outcome_events),before)
  self.assertEqual(t.zone_of(flame),"hand")

 def test_sorcery_priority_and_instant_response_window(self):
  t=state();t.inject_mana({"R":3,"C":3,"B":1})
  bol=uid(t,"Boltwave","hand");rit=uid(t,"Dark Ritual","hand")
  t.main_phase=False
  before=t.receipt()
  with self.assertRaises(BlockedAction):t.cast(bol)
  self.assertEqual(t.receipt(),before)
  t.main_phase=True
  t.cast(bol)
  with self.assertRaises(BlockedAction):t.cast(uid(t,"Flame Rift","hand"))
  t.cast(rit)   # instant, while another spell is pending
  t.resolve_all()
  self.assertEqual(t.mana["B"],3)
  self.assertEqual(t.opponents_lost_this_turn,9)
  self.assertTrue(t.validate_stack())

 def test_signet_mana_and_reset(self):
  t=state();t.inject_mana({"C":2})
  signet=uid(t,"Arcane Signet","hand")
  t.cast(signet);t.resolve_all()
  self.assertEqual(t.zone_of(signet),"battlefield")
  t.tap_signet(signet,"U")
  with self.assertRaises(BlockedAction):t.tap_signet(signet,"B")
  t.next_turn()
  self.assertEqual(t.mana["U"],0)
  self.assertEqual(t.tap_signet(signet,"B"),"B")

 def test_unsupported_rules_fail_closed_and_no_card_creation(self):
  t=state()
  ghost="m999"
  before=t.receipt()
  with self.assertRaises(BlockedAction):t.cast(ghost)
  with self.assertRaises(BlockedAction):t.scripted_counter_spell(ghost)
  with self.assertRaises(BlockedAction):t.scripted_remove_permanent("c000")
  self.assertEqual(t.receipt(),before)
  self.assertFalse(t.frames)
  self.assertTrue(t.check())

 def test_end_turn_forbids_pending_trigger(self):
  t=state();t.inject_mana({"R":2,"C":1,"B":1})
  k=uid(t,"Kessig Flamebreather","hand")
  t.cast(k);t.resolve_all()
  t.cast(uid(t,"Dark Ritual","hand"))
  with self.assertRaises(BlockedAction):t.next_turn()
  self.assertEqual(t.turn,1)

if __name__=="__main__":unittest.main()
