"""Cycle123 conditional opponent-event effects are source-paid, not claimed games."""
import copy,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle123_conditional_offer_stack as m
import evaluate_decklist as ev
import grixis_sim as sim
from grixis_m6_priority_nonbasic import PriorityNonbasic
from grixis_m6_state_kernel import BlockedAction

def fixture(land="Command Tower",include_offer=True,land_tapped=False):
 names=[land]+([m.OFFER] if include_offer else [])+["Test inert card "+str(i) for i in range(99-1-int(include_offer))]
 cards=[{"name":s,"land":s==land,"cost":sim.parse_cost("{U}" if s==m.OFFER else "")} for s in names]
 w=PriorityNonbasic(cards,[{"name":"Mai and Zuko","land":False}],seed=2,opponent_count=3)
 land_id=next(i for i,c in w.cards.items() if c["name"]==land)
 w.transfer(land_id,"library","hand")
 if include_offer:
  offer_id=next(i for i,c in w.cards.items() if c["name"]==m.OFFER)
  w.transfer(offer_id,"library","hand")
 w.play_supported_land(land_id,pay_shock=True if land=="Watery Grave" else None)
 if land_tapped:w.tapped.add(land_id)
 return w

class ConditionalOfferTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.plan=m.read(m.PLAN)
  cls.parent=m.read(m.PARENT)
  cls.registry=m.read(m.REG)
 def test_registered_approved_mai_source_and_frozen_oracle(self):
  checked=m.verify(self.plan,self.parent,self.registry,ev.Resolver())
  self.assertIn("offer_oracle_text_sha256",checked)
  self.assertTrue(checked["nineteen_frozen_oracle_nonbasic_land_gates"])
 def test_valid_physical_offer_counter_and_treasures(self):
  t=fixture()
  r=m.source_paid_offer_fixture(t)
  self.assertEqual(r["final_zone"],"graveyard")
  self.assertEqual(r["countered"],1)
  self.assertEqual(r["opponent_virtual_treasures"],2)
  self.assertEqual(r["four_stipulated_passes"],4)
  self.assertEqual(r["physical_card_total"],100)
  self.assertEqual(t.mana["U"],0)
  self.assertEqual(t.frames,[])
  self.assertTrue(t.validate_stack())
 def test_uncounterable_target_still_gives_two_treasures(self):
  t=fixture()
  r=m.source_paid_offer_fixture(t,counterable=False)
  self.assertEqual(r["countered"],0)
  self.assertTrue(r["resolved"])
  self.assertEqual(r["opponent_virtual_treasures"],2)
 def test_becomes_illegal_after_cast_fizzles_no_treasures(self):
  t=fixture()
  r=m.source_paid_offer_fixture(t,removed_after_cast=True)
  self.assertEqual(r["final_zone"],"graveyard")
  self.assertFalse(r["resolved"])
  self.assertEqual(r["countered"],0)
  self.assertEqual(r["opponent_virtual_treasures"],0)
 def assertBlockedUnchanged(self,t,**kwargs):
  before=m.fmt(t.receipt())
  with self.assertRaises(BlockedAction):
   m.source_paid_offer_fixture(t,**kwargs)
  self.assertEqual(m.fmt(t.receipt()),before)
  self.assertEqual(len(t.frames),0)
 def test_illegal_creature_target_rejected_before_payment(self):
  self.assertBlockedUnchanged(fixture(),kind="creature")
 def test_no_opponent_spell_prevents_cast_or_ghost_target(self):
  self.assertBlockedUnchanged(fixture(),spell_present=False)
 def test_missing_controller_priority_cannot_invent_response(self):
  self.assertBlockedUnchanged(fixture(),pilot_priority=False)
 def test_no_offer_in_hand_not_created(self):
  self.assertBlockedUnchanged(fixture(include_offer=False))
 def test_watery_grave_untapped_life_cost_is_source_paid(self):
  t=fixture("Watery Grave")
  self.assertEqual(t.pilot,38)
  r=m.source_paid_offer_fixture(t)
  self.assertEqual(r["countered"],1)
  self.assertEqual(r["source_payment"][0]["name"],"Watery Grave")
 def test_mana_confluence_pays_one_life_when_tapped(self):
  t=fixture("Mana Confluence")
  r=m.source_paid_offer_fixture(t)
  self.assertEqual(r["source_life_paid"],1)
  self.assertEqual(t.pilot,39)
 def test_badlands_cannot_pay_blue_and_no_mutation(self):
  self.assertBlockedUnchanged(fixture("Badlands"))
 def test_tapped_xanders_lounge_cannot_pay_at_entry(self):
  t=fixture("Xander's Lounge")
  self.assertBlockedUnchanged(t)
 def test_jewel_has_blue_cost_and_does_not_counter_by_itself(self):
  self.assertEqual(m.c121.COST[m.JEWEL],(0,{"U":1}))
  self.assertEqual(m.OFFER,"An Offer You Can't Refuse")
  self.assertEqual(self.plan["deck"]["cut"],m.OFFER)
  self.assertEqual(self.plan["deck"]["add"],m.JEWEL)
 def test_false_source_swap_or_milestone_status_cannot_pass(self):
  p=copy.deepcopy(self.plan)
  p["deck"]["add"]="Demonic Tutor"
  with self.assertRaises(ValueError):
   m.verify(p,self.parent,self.registry,ev.Resolver())
  p=copy.deepcopy(self.plan);p["authority"]["can_apply_candidate"]=True
  with self.assertRaises(ValueError):
   m.verify(p,self.parent,self.registry,ev.Resolver())
 def test_secondary_m6_m7_tracker_stays_unpromoted(self):
  tr=m.read(ROOT/"data/grixis/milestone_m6_m7_subtracker.json")
  self.assertEqual(tr["display"]["m6_completed_gates"],3)
  self.assertEqual(tr["display"]["m7_completed_gates"],0)
  self.assertEqual(tr["m6"]["formal_m6_certified_decks"],0)
  self.assertEqual(self.registry["program"]["milestones"]["M6"]["status"],"in_progress")
if __name__=="__main__":unittest.main()
