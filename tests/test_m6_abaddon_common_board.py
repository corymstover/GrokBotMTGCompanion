"""Cycle110 common-board ledger denies mismatched causal value comparisons."""
import sys,unittest,copy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from grixis_m6_abaddon_common_board import candidate_leaf,blast_leaf,normalized_opening

def candidate(name="Heartless Hidetsugu"):
 loss=54 if name=="Heartless Hidetsugu" else 27
 value={"profile":"no_interference","activated":True,"resolved":True,
 "opponents_lost":loss,"pilot_damage":16 if name=="Heartless Hidetsugu" else 0,
 "abaddon_present":True,"followup_held_source_payable":"NO"}
 if name=="Tree of Perdition":value["target_life_after"]=13
 pre={"profile":"remove_source_before_first_activation",
     "activated":False,"resolved":False,"opponents_lost":0}
 post={"profile":"remove_source_after_ability_on_stack",
       "activated":True,"resolved":name=="Heartless Hidetsugu",
       "opponents_lost":loss if name=="Heartless Hidetsugu" else 0}
 return {"observations":{"slot_seen":True,"slot_held_and_mana_affordable":True,
  "slot_cast":True,"slot_cast_turn":5,"slot_activation_turn":6,
  "first_activation_profiles":[value,pre,post]}}
class LedgerTests(unittest.TestCase):
 def test_common_slot_only_opening_alignment(self):
  a={"opening":["Island","Bituminous Blast","Swamp"]}
  b={"opening":["Island","Heartless Hidetsugu","Swamp"]}
  c={"opening":["Island","Tree of Perdition","Swamp"]}
  self.assertEqual(normalized_opening(a),normalized_opening(b))
  self.assertEqual(normalized_opening(a),normalized_opening(c))
  c["opening"][2]="Mountain"
  self.assertNotEqual(normalized_opening(a),normalized_opening(c))
 def test_heartless_player_damage_does_not_remove_3_3(self):
  row=candidate_leaf(candidate(),"Heartless Hidetsugu")
  self.assertEqual(row["conditional_opponent_life_lost_on_tap"],54)
  self.assertGreater(row["conditional_controller_self_damage_on_tap"],0)
  self.assertTrue(row["opponent_3_3_alive_after_slot_outcome"])
  self.assertTrue(row["source_removed_after_ability_is_on_stack_still_resolves"])
  self.assertFalse(row["boltwave_or_flame_rift_source_payable_in_hand_at_tap"])
  self.assertEqual(row["candidate_followup_actual_cast_and_effect"],"UNMODELED")
 def test_tree_exchange_target_life_but_not_creature_or_source_removed(self):
  row=candidate_leaf(candidate("Tree of Perdition"),"Tree of Perdition")
  self.assertEqual(row["conditional_opponent_life_lost_on_tap"],27)
  self.assertEqual(row["conditional_controller_self_damage_on_tap"],0)
  self.assertFalse(row["source_removed_after_ability_is_on_stack_still_resolves"])
  self.assertTrue(row["opponent_3_3_alive_after_slot_outcome"])
 def test_illegal_haste_or_false_post_removal_events_rejected(self):
  row=candidate()
  row["observations"]["slot_activation_turn"]=5
  with self.assertRaisesRegex(ValueError,"Activation before"):candidate_leaf(row,"Heartless Hidetsugu")
  row=candidate("Tree of Perdition")
  row["observations"]["first_activation_profiles"][2]["resolved"]=True
  with self.assertRaisesRegex(ValueError,"Tree removed"):candidate_leaf(row,"Tree of Perdition")
 def test_blast_known_creature_removal_not_opponent_life_loss(self):
  trial={"seed":11,"opening":["Bituminous Blast","Island"],
   "blast_cast":True,"blast_resolution":"REMOVED_EXTERNAL_3_3_BY_FOUR_DAMAGE",
   "trigger_count":1,"triggers_resolved":1,"cascade_offers":[{"eligible_name":"Sol Ring"}],
   "executed_hit_spells":[{"name":"Sol Ring","resolved":True}],
   "declined_unknown_hits":[],"zone_counts":{"library":90,"graveyard":1,"battlefield":7,"hand":1,"command":1,"exile":0,"stack":0},
   "generated_rock_mana_not_spent_in_followup":2,"mana_vault_upkeeps_unresolved":0}
  prior={"seed":11,"opening":trial["opening"],"blast_cast":True}
  x=blast_leaf(trial,prior,"no_removal",True)
  self.assertTrue(x["opponent_3_3_removed_by_blast"])
  self.assertEqual(x["opponent_life_lost_from_blast_damage_to_creature"],0)
  self.assertEqual(x["rock_colorless_mana_generated_not_used_in_followup"],2)
  self.assertIsNone(x["cascade_card_quality_numeric_value"])
 def test_wrong_script_policy_and_nonconserved_ids_fail(self):
  trial={"seed":11,"opening":["Bituminous Blast"],"blast_cast":True,
   "blast_resolution":"REMOVED_EXTERNAL_3_3_BY_FOUR_DAMAGE","trigger_count":0,
   "triggers_resolved":0,"executed_hit_spells":[],"declined_unknown_hits":[],
   "cascade_offers":[],"zone_counts":{"library":1},"generated_rock_mana_not_spent_in_followup":0,
   "mana_vault_upkeeps_unresolved":0}
  prior={"seed":11,"opening":trial["opening"],"blast_cast":True}
  with self.assertRaises(ValueError):blast_leaf(trial,prior,"target_removed_after_cast",True)
  with self.assertRaises(ValueError):blast_leaf(trial,prior,"no_removal",True)
if __name__=="__main__":unittest.main()
