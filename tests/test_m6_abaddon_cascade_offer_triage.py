"""Cycle108 independent negative unit tests for non-promoted Oracle hit triage."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from grixis_m6_abaddon_cascade_offer_triage import oracle_classification,classify_card_specific_roles,ROLE_CHECKS

def offer(name="Lightning Bolt",mv=1):
 return {"eligible_name":name,"eligible_mv":mv,"eligible_uid":"m036"}
def card(name="Lightning Bolt",mv=1,typ="Instant",text="Lightning Bolt deals 3 damage to any target."):
 return {"name":name,"cmc":mv,"type_line":typ,"mana_cost":"{R}",
         "oracle_text":text,"layout":"normal"}
class GateTests(unittest.TestCase):
 def test_unknown_value_not_automatically_zero(self):
  x=oracle_classification(offer(),card(),{"Lightning Bolt"})
  self.assertEqual(x["effect_outcome"],"UNKNOWN_NOT_ZERO")
  self.assertEqual(x["comparative_deck_value"],"UNKNOWN_NOT_ZERO")
  self.assertFalse(x["controller_chose_cast"])
  self.assertEqual(x["priority_and_effect_resolution"],"NOT_EXECUTED")
  self.assertIn("LEGAL_TARGET_REQUIRES_STACK_OR_BOARD_CONTEXT",x["relevant_target_or_choice_flags"])
 def test_source_name_missing_or_false_mana_value_rejected(self):
  with self.assertRaises(ValueError):oracle_classification(offer(),card(name="Other"),{"Lightning Bolt"})
  with self.assertRaises(ValueError):oracle_classification(offer(mv=5),card(mv=5),{"Lightning Bolt"})
  with self.assertRaises(ValueError):oracle_classification(offer(),card(),{"Other"})
 def test_land_never_classifies_as_cascade_nonland(self):
  with self.assertRaises(ValueError):
   oracle_classification(offer("Island",0),card("Island",0,"Basic Land — Island","{T}: Add {U}."),{"Island"})
 def test_conditional_and_extra_cost_not_claimed_legal(self):
  x=oracle_classification(offer("Sample Spell",2),card("Sample Spell",2,"Sorcery",
             "As an additional cost to cast this spell, sacrifice a creature. Choose target player."),{"Sample Spell"})
  self.assertIn("ADDITIONAL_COST_NOT_MODELED",x["relevant_target_or_choice_flags"])
  self.assertIn("MODE_OR_CHOICE_NEEDS_CONTEXT",x["relevant_target_or_choice_flags"])
  self.assertEqual(x["spell_legality_if_chosen"],"UNVERIFIED_MAY_REQUIRE_CONTEXT")
 def test_known_named_direct_effect_is_not_executed(self):
  x=oracle_classification(offer("Boltwave",1),card("Boltwave",1,"Sorcery",
          "Boltwave deals 3 damage to each opponent."),{"Boltwave"})
  self.assertIn("3 damage",x["effect_text_known_but_NOT_observed"])
  self.assertEqual(x["effect_outcome"],"UNKNOWN_NOT_ZERO")
  self.assertTrue(x["no_numerical_value_assigned"])
 def test_complex_layout_fails_complete_legality_approval(self):
  x=oracle_classification(offer("Dual Form",2),dict(card("Dual Form",2),
          layout="modal_dfc"),{"Dual Form"})
  self.assertIn("ALTERNATE_CARD_FACE_OR_COMPLEX_LAYOUT",x["relevant_target_or_choice_flags"])
  self.assertEqual(x["spell_legality_if_chosen"],"UNVERIFIED_MAY_REQUIRE_CONTEXT")

class PostResultRoles(unittest.TestCase):
 def test_seven_exact_cards_are_qualitative_unknowns(self):
  sources={n:{"oracle_text":" and ".join(v["snippets"])}
    for n,v in ROLE_CHECKS.items()}
  classified=classify_card_specific_roles(sources,set(sources))
  self.assertEqual(len(classified),7)
  self.assertTrue(all(not x["was_cast_in_source_evidence"] and
    not x["realized_value_measured"] and x["relative_deck_value"]=="UNKNOWN_NOT_ZERO"
    for x in classified.values()))
 def test_missing_printed_mechanic_or_spurious_card_fails(self):
  sources={n:{"oracle_text":" and ".join(v["snippets"])}
    for n,v in ROLE_CHECKS.items()}
  sources["Chrome Mox"]["oracle_text"]="Artifact mana without imprint"
  with self.assertRaises(ValueError):classify_card_specific_roles(sources,set(sources))
  with self.assertRaises(ValueError):classify_card_specific_roles(sources,{"Sol Ring"})

if __name__=="__main__":unittest.main()
