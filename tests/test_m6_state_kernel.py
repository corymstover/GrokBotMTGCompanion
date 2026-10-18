"""Cycle 100: adversarial all-commander physical-card state invariants."""
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from grixis_m6_state_kernel import Ledger,BlockedAction,fingerprint
import grixis_m6_state_kernel_62 as runner

def card(name,land=False,cost=None):
 return {"name":name,"land":land,"cost":cost or {"generic":1,"pips":[],"life":0}}

class StateKernelTests(unittest.TestCase):
 def setup_state(self):
  return Ledger([card("Island",True),card("Island",True),card("Swamp",True),
                card("Sol Ring",False,{"generic":1,"pips":[],"life":0})],
                [card("Abaddon the Despoiler")],seed=51)

 def test_unique_id_cards_and_repeated_basics(self):
  s=self.setup_state()
  self.assertEqual(s.initial_card_count,5)
  self.assertEqual(len(set(s.cards)),5)
  self.assertEqual(len([v for v in s.original.values() if v=="Island"]),2)
  self.assertEqual(len(s.zones["command"]),1)
  self.assertTrue(s.check())

 def test_deterministic_seed_and_zone_conservation(self):
  x=self.setup_state();y=self.setup_state()
  self.assertEqual(x.zones,y.zones)
  xa=x.draw(3);ya=y.draw(3)
  self.assertEqual(xa,ya)
  self.assertEqual(x.receipt(),y.receipt())
  self.assertTrue(all(c in x.zones["hand"] for c in xa))
  self.assertEqual(len(x.zones["library"])+len(x.zones["hand"])+len(x.zones["command"]),5)

 def test_draw_overflow_fails_without_partial_state_mutation(self):
  s=self.setup_state();before=s.receipt()
  with self.assertRaises(BlockedAction):s.draw(5)
  self.assertEqual(before,s.receipt())
  with self.assertRaises(BlockedAction):s.draw(-1)

 def test_zone_transfer_abuse_fails_closed(self):
  s=self.setup_state();s.draw(2)
  before=s.receipt()
  for args in [("m000","graveyard","hand"),("ghost","library","hand"),
               ("m000","hand","hand"),("m000","hand","not_a_zone")]:
   with self.assertRaises(BlockedAction):s.transfer(*args)
  self.assertEqual(s.receipt(),before)
  uid=s.zones["hand"][0]
  s.transfer(uid,"hand","exile")
  self.assertEqual(s.zone_of(uid),"exile")
  with self.assertRaises(BlockedAction):s.transfer(uid,"hand","graveyard")
  self.assertTrue(s.check())

 def test_basic_land_play_and_mana_exhaustion(self):
  s=self.setup_state();s.draw(4)
  basic=next(i for i in s.zones["hand"] if s.cards[i]["name"]=="Island")
  s.play_basic(basic)
  self.assertEqual(s.tap_basic(basic),"U")
  self.assertEqual(s.mana["U"],1)
  with self.assertRaises(BlockedAction):s.tap_basic(basic)
  other=next(i for i in s.zones["hand"] if s.cards[i]["name"]=="Swamp")
  with self.assertRaises(BlockedAction):s.play_basic(other)
  s.next_turn()
  self.assertEqual(s.mana["U"],0)
  self.assertEqual(s.tap_basic(basic),"U")
  self.assertEqual(s.mana["U"],1)
  s.play_basic(other)
  self.assertEqual(s.tap_basic(other),"B")
  self.assertTrue(s.check())

 def test_land_timing_and_nonbasics_blocked(self):
  s=self.setup_state();s.draw(4)
  island=next(i for i in s.zones["hand"] if s.cards[i]["name"]=="Island")
  before=s.receipt()
  for kws in ({"own_turn":False},{"main_phase":False},{"stack_empty":False}):
   with self.assertRaises(BlockedAction):s.play_basic(island,**kws)
   self.assertEqual(s.receipt(),before)
  t=Ledger([card("Command Tower",True)],[card("Abaddon the Despoiler")])
  land=t.draw(1)[0]
  with self.assertRaises(BlockedAction):t.play_basic(land)
  self.assertEqual(t.zone_of(land),"hand")

 def test_unmodeled_effect_never_moves_card(self):
  s=self.setup_state();uid=s.draw(4)[0];before=s.receipt()
  block=s.refuse_effect(uid,"no oracle handler")
  self.assertEqual(block["status"],"blocked_unmodeled_effect")
  self.assertEqual(before["zone_fingerprint"],s.receipt()["zone_fingerprint"])
  self.assertEqual(s.receipt()["unmodeled_effects"],1)

 def test_printed_mana_preflight_cannot_cast_spell(self):
  s=Ledger([card("Test Spell",False,{"generic":1,"pips":[frozenset({"U"})],"life":0}),
            card("Island",True)],[card("Test Commander")])
  uid=s.draw(2)[0]
  spell=next(i for i in s.zones["hand"] if s.cards[i]["name"]=="Test Spell")
  info=s.printed_cost_probe(spell)
  self.assertEqual(info["status"],"printed_mana_only_unaffordable")
  self.assertFalse(info["legal_cast"])
  before=s.receipt()
  s.mana["U"]=1
  s.mana["C"]=1
  info=s.printed_cost_probe(spell)
  self.assertEqual(info["status"],"printed_mana_only_affordable")
  self.assertFalse(info["legal_cast"])
  self.assertEqual(s.zone_of(spell),"hand")
  self.assertTrue(s.check())
  s.mana["C"]=-1
  with self.assertRaises(AssertionError):s.check()

 def test_stack_priority_boundary(self):
  s=self.setup_state();s.draw(1)
  i=s.zones["hand"][0]
  s.transfer(i,"hand","stack")
  with self.assertRaises(BlockedAction):s.next_turn()
  self.assertEqual(s.turn,1)
  s.transfer(i,"stack","graveyard")
  s.next_turn()
  self.assertEqual(s.turn,2)

 def test_global_preregistration_exact_read_only_scope(self):
  p=runner.data(runner.PLAN)
  self.assertEqual(p["coverage"]["roster_decks"],62)
  self.assertEqual(p["coverage"]["samples_per_deck"],4)
  self.assertEqual(p["coverage"]["seed"],100017)
  self.assertFalse(any(p["protected"].values()))
  self.assertEqual(p["preregistration_status"],"registered_before_implementation")

if __name__=="__main__":unittest.main()
