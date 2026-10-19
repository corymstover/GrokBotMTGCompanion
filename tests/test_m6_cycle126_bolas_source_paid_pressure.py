"""Cycle126: physical Bolas Mox/Amplifier tempo, action/tap exclusivity and loyalty pressure."""
import copy,json,random,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle126_bolas_source_paid_pressure as m
from grixis_m6_priority_nonbasic import PriorityNonbasic
from grixis_m6_state_kernel import BlockedAction
import evaluate_decklist as ev

def fixture(names=(),hand=(),battlefield=(),opponent_count=3):
 n=list(names)
 main=[{"name":x,"land":x in m.BASIC_MANA or x in m.LANDS} for x in n]
 t=PriorityNonbasic(main,[{"name":m.BOLAS,"land":False}],seed=7,opponent_count=opponent_count)
 for name in hand:
  uid=next(i for i in t.zones["library"] if t.cards[i]["name"]==name)
  t.transfer(uid,"library","hand")
 for name in battlefield:
  uid=next(i for i in t.zones["library"] if t.cards[i]["name"]==name)
  t.transfer(uid,"library","battlefield")
 return t
class BolasSourceTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.p=m.read(m.PLAN);cls.r=m.read(m.SOURCE);cls.prior=m.read(m.PARENT)
 def test_preregister_and_source_approved_cards_oracle_gated(self):
  R=ev.Resolver()
  proof=m.verify(self.p,self.r,self.prior,R)
  self.assertEqual(set(proof),{m.AMP,m.MOX,m.BOLAS})
  self.assertEqual(self.p["study"]["cut"],m.MOX)
  self.assertEqual(self.p["study"]["add"],m.AMP)
 def test_source_rejects_wrong_candidate_and_false_acceptance(self):
  R=ev.Resolver()
  p=copy.deepcopy(self.p);p["study"]["add"]="Black Lotus"
  with self.assertRaises(ValueError):m.verify(p,self.r,self.prior,R)
  p=copy.deepcopy(self.p);p["authority"]["accept_m6"]=True
  with self.assertRaises(ValueError):m.verify(p,self.r,self.prior,R)
 def test_mox_without_physical_land_fails_unchanged(self):
  t=fixture([m.MOX],hand=[m.MOX])
  before=m.enc(t.receipt())
  self.assertIsNone(m.physical_mox_entry(t))
  self.assertEqual(m.enc(t.receipt()),before)
 def test_mox_entry_discards_only_real_land_from_hand(self):
  t=fixture([m.MOX,"Island"],hand=[m.MOX,"Island"])
  x=m.physical_mox_entry(t)
  self.assertIsNotNone(x)
  self.assertEqual(t.zone_of(x["mox_uid"]),"battlefield")
  self.assertEqual(t.zone_of(x["discard_uid"]),"graveyard")
  self.assertEqual(x["discard_name"],"Island")
  self.assertFalse(t.land_played)
  self.assertEqual(sum(t.mana.values()),0)
 def test_mox_produces_one_mana_any_color_same_entry_turn(self):
  t=fixture([m.MOX,"Island"],hand=[m.MOX,"Island"])
  x=m.physical_mox_entry(t)
  self.assertIsNotNone(x)
  assigned=m.planned_payment(t,(0,("R",)))
  self.assertEqual(assigned,[(x["mox_uid"],"R")])
  m.pay_physical(t,assigned,"unit_test_mox_red")
  self.assertIn(x["mox_uid"],t.tapped)
  self.assertIsNone(m.planned_payment(t,(0,("B",))))
 def test_amplifier_cost_three_not_free_and_does_not_invent_mana(self):
  t=fixture([m.AMP,"Island","Swamp"],hand=[m.AMP],battlefield=["Island","Swamp"])
  before=m.enc(t.receipt())
  self.assertIsNone(m.paid_amplifier_cast(t))
  self.assertEqual(m.enc(t.receipt()),before)
  self.assertEqual(sum(t.mana.values()),0)
 def test_amplifier_paid_three_and_taps_for_mana_on_cast_turn(self):
  t=fixture([m.AMP,"Island","Swamp","Mountain"],hand=[m.AMP],battlefield=["Island","Swamp","Mountain"])
  v=m.paid_amplifier_cast(t)
  self.assertEqual(v["turn"],1)
  self.assertEqual(len(v["sources"]),3)
  self.assertIn(m.AMP,[t.cards[i]["name"] for i in t.zones["battlefield"]])
  self.assertIsNotNone(m.planned_payment(t,(0,("U",))))
  m.pay_physical(t,m.planned_payment(t,(0,("U",))),"one_amp_mana")
  self.assertIsNone(m.planned_payment(t,(0,("U",))))
 def test_same_amp_cannot_tap_for_mana_and_double_in_turn(self):
  t=fixture([m.AMP,"Island","Swamp","Mountain","Command Tower"],
    battlefield=[m.AMP,"Island","Swamp","Mountain","Command Tower"])
  uid=next(i for i in t.zones["battlefield"] if t.cards[i]["name"]==m.AMP)
  m.pay_physical(t,[(uid,"U")],"use_amp_as_mana_source")
  self.assertIsNone(m.source_double(t,7))
  self.assertIn(uid,t.tapped)
 def test_amp_double_requires_other_four_source_payment(self):
  t=fixture([m.AMP,"Island","Swamp","Mountain"],battlefield=[m.AMP,"Island","Swamp","Mountain"])
  self.assertIsNone(m.source_double(t,7))
  self.assertEqual(sum(t.mana.values()),0)
 def test_double_seven_to_fourteen_no_loyalty_activation(self):
  t=fixture([m.AMP,"Island","Swamp","Mountain","Command Tower"],
    battlefield=[m.AMP,"Island","Swamp","Mountain","Command Tower"])
  x=m.source_double(t,7)
  self.assertEqual(x["before"],7);self.assertEqual(x["after"],14)
  self.assertEqual(len(x["sources"]),4)
  self.assertIsNone(m.source_double(t,14))
  self.assertEqual(sum(t.mana.values()),0)
 def test_double_rejects_outside_main_and_nonempty_stack(self):
  t=fixture([m.AMP,"Island","Swamp","Mountain","Command Tower"],
    battlefield=[m.AMP,"Island","Swamp","Mountain","Command Tower"])
  before=m.enc(t.receipt())
  self.assertIsNone(m.source_double(t,7,own_main=False))
  self.assertIsNone(m.source_double(t,7,stack_empty=False))
  self.assertEqual(m.enc(t.receipt()),before)
 def test_commander_exact_ubr_requires_four_actual_untapped_sources(self):
  t=fixture(["Island","Swamp","Mountain"],battlefield=["Island","Swamp","Mountain"])
  self.assertIsNone(m.pay_and_place_commander(t))
  self.assertIn("c000",t.zones["command"])
  t=fixture(["Island","Swamp","Mountain","Command Tower"],
    battlefield=["Island","Swamp","Mountain","Command Tower"])
  cast=m.pay_and_place_commander(t)
  self.assertEqual(len(cast["sources"]),4)
  self.assertIn("c000",t.zones["battlefield"])
  self.assertEqual(sum(t.mana.values()),0)
 def test_transform_requires_seven_and_starts_at_7_not_5(self):
  names=["Island","Swamp","Mountain","Command Tower","Underground Sea","Badlands","Volcanic Island"]
  t=fixture(names,battlefield=names)
  t.transfer("c000","command","battlefield")
  x=m.source_transform(t)
  self.assertIsNotNone(x)
  self.assertEqual(x["initial_loyalty"],7)
  self.assertEqual(len(x["sources"]),7)
  self.assertIn("c000",t.zones["battlefield"])
  self.assertEqual(sum(t.mana.values()),0)
 def test_pressure_damage_is_only_threshold_not_real_enemy_action(self):
  p=m.pressure_thresholds(7)
  self.assertTrue(p["3"]["survives"])
  self.assertFalse(p["8"]["survives"])
  q=m.pressure_thresholds(14)
  self.assertTrue(q["13"]["survives"])
  self.assertFalse(q["13"]["remaining"]==0)
  self.assertIsNone(m.pressure_thresholds(None))
 def test_no_unregistered_mana_from_unsupported_fetch_or_rock(self):
  t=fixture(["Polluted Delta","Island"],battlefield=["Polluted Delta","Island"])
  self.assertIsNone(m.planned_payment(t,(1,("U",))))
  self.assertNotIn(("m000","U"),m.planned_payment(t,(0,("U",))))
 def test_accepted_locks_and_subtrackers_unchanged(self):
  tr=m.read(ROOT/"data/grixis/milestone_m6_m7_subtracker.json")
  self.assertEqual(tr["display"]["m6_completed_gates"],3)
  self.assertEqual(tr["display"]["m7_completed_gates"],0)
  self.assertEqual(tr["m6"]["formal_m6_certified_decks"],0)
  self.assertTrue(all(value is False for value in self.p["authority"].values()))
if __name__=="__main__":unittest.main()
