"""Cycle106 adversarial physical-card slot, typed mana and no-haste response tests."""
import sys,unittest,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_sim as sim
from grixis_m6_abaddon_physical_slot import SlotProbe,SLOTS,slot_in_hand,sources_can_pay,run_trial,compact
from grixis_m6_state_kernel import BlockedAction

def card(n):
 if n in ("Island","Swamp","Mountain","Command Tower","Blood Crypt","Volcanic Island","Ancient Tomb"):
  return {"name":n,"land":True,"mv":0,"cost":sim.parse_cost("")}
 if n in SLOTS:
  c,_,m=SLOTS[n]
  return {"name":n,"land":False,"mv":m,"cost":sim.parse_cost(c)}
 if n in ("Boltwave","Flame Rift"):
  return {"name":n,"land":False,"mv":1 if n=="Boltwave" else 2,
          "cost":sim.parse_cost("{R}" if n=="Boltwave" else "{1}{R}")}
 raise ValueError(n)
def fixture(slot,lands):
 cards=[card(n) for n in list(lands)+[slot,"Boltwave"]]
 commander={"name":"Abaddon the Despoiler","land":False,"mv":5,
           "cost":sim.parse_cost("{2}{U}{B}{R}")}
 t=SlotProbe(cards,[commander],slot=slot,seed=106)
 for uid in list(t.zones["library"]):t.transfer(uid,"library","hand")
 for n in lands:
  if t.land_played:t.next_turn()
  u=next(u for u in t.zones["hand"] if t.cards[u]["name"]==n)
  t.play_supported_land(u)
 return t

class PhysicalSlotTests(unittest.TestCase):
 def test_heartless_later_turn_and_three_removal_outcomes(self):
  t=fixture("Heartless Hidetsugu",["Mountain","Mountain","Island","Swamp","Command Tower"])
  uid=slot_in_hand(t)
  self.assertTrue(sources_can_pay(t,uid))
  paid=t.cast_with_land_sources(uid)
  self.assertGreaterEqual(len(paid),4)
  t.resolve_by_passes()
  self.assertEqual(t.zone_of(uid),"battlefield")
  with self.assertRaises(BlockedAction):t.activate_slot("no_interference")
  t.next_turn()
  expected=[]
  for mode in ("no_interference","remove_source_before_first_activation",
               "remove_source_after_ability_on_stack"):
   copy_state=copy.deepcopy(t)
   expected.append(copy_state.activate_slot(mode))
   self.assertTrue(copy_state.check())
  self.assertEqual([x["opponents_lost"] for x in expected],[54,0,54])
  self.assertEqual([x["pilot_damage"] for x in expected],[20,0,20])
  self.assertEqual(expected[0]["opponent_life_after"],[20,20,16])
  self.assertTrue(expected[2]["source_removed"])

 def test_tree_removed_after_activation_fails_exchange(self):
  t=fixture("Tree of Perdition",["Swamp","Island","Mountain","Command Tower"])
  uid=slot_in_hand(t);self.assertTrue(sources_can_pay(t,uid))
  t.cast_with_land_sources(uid);t.resolve_by_passes()
  t.next_turn()
  outcomes=[copy.deepcopy(t).activate_slot(mode) for mode in
    ("no_interference","remove_source_before_first_activation",
     "remove_source_after_ability_on_stack")]
  self.assertEqual([x["opponents_lost"] for x in outcomes],[27,0,0])
  self.assertEqual(outcomes[0]["target_life_after"],13)
  self.assertEqual(outcomes[0]["pilot_damage"],0)

 def test_blast_has_opportunity_but_no_fake_legal_target(self):
  t=fixture("Bituminous Blast",["Swamp","Mountain","Island","Command Tower","Mountain"])
  uid=slot_in_hand(t)
  self.assertTrue(sources_can_pay(t,uid))
  before=copy.deepcopy((t.zones,t.frames,t.tapped,t.mana,t.pilot))
  with self.assertRaisesRegex(BlockedAction,"target"):t.cast_with_land_sources(uid)
  self.assertEqual((t.zones,t.frames,t.tapped,t.mana,t.pilot),before)
  self.assertEqual(t.zone_of(uid),"hand")

 def test_wrong_colors_prevent_heartless(self):
  t=fixture("Heartless Hidetsugu",["Swamp","Swamp","Island","Island","Ancient Tomb"])
  uid=slot_in_hand(t)
  self.assertFalse(sources_can_pay(t,uid))
  before=copy.deepcopy((t.zones,t.tapped,t.mana,t.pilot))
  with self.assertRaises(BlockedAction):t.cast_with_land_sources(uid)
  self.assertEqual((t.zones,t.tapped,t.mana,t.pilot),before)

 def test_source_loss_and_priority_fail_closed(self):
  t=fixture("Tree of Perdition",["Swamp","Island","Mountain","Command Tower"])
  uid=slot_in_hand(t)
  t.cast_with_land_sources(uid);t.resolve_by_passes();t.next_turn()
  t.tapped.add(uid)
  with self.assertRaises(BlockedAction):t.activate_slot("no_interference")
  t.tapped.discard(uid);t.priority_seat=1
  with self.assertRaises(BlockedAction):t.cast_with_land_sources(uid)

 def test_source_role_matrix_never_proves_improvement(self):
  report={"cycle":106,"approved_raw_sha256":"test","samples_per_variant":240,
         "total_samples":720,"variants":{n:{"observed":{}} for n in SLOTS},
         "oracle_checks":{},"comparison_verdict":"CANNOT_EVALUATE_RELATIVE_DECK_STRENGTH",
         "reasons":["unknown"],"actual_game_win_rate":None}
  index=compact(report)
  self.assertFalse(index["new_card_approved"])
  self.assertFalse(index["M6_accepted"])
  self.assertIsNone(index["actual_game_win_rate"])

if __name__=="__main__":unittest.main()
