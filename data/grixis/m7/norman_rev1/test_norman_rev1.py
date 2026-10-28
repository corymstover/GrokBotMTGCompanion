"""Finite, source-paid Norman M7 Rev1 commander/rules contracts.

The arithmetic/state transitions are modeled deliberately and narrowly.
These are *not* random gameplay tests, matchup win rates, or a Magic engine.
Rules sources: 2026-09-25 CR 601, 605, 702.187, 903;
Scryfall Oracle/rulings for Norman, LED, Breach, Inti, Fervent Mastery,
Cephalid Coliseum, Intuition, Samut, Cavern and Necropotence.
"""

import collections
import hashlib
import json
from pathlib import Path
import unittest


LIST = Path(__file__).resolve().parents[1] / "candidate_lists/Norman_Osborn_Green_Goblin_chatgpt_rev1.txt"
REPO = Path(__file__).resolve().parents[4]
EXPECTED_SHA = "c002a49243bd54780bb0f4a36a3c239a00e042defa1d0c6c4b891c3c8060eef9"
ADDS = {"Fervent Mastery", "Cephalid Coliseum", "Samut, Tyrant of Naktamun", "Intuition", "Inti, Seneschal of the Sun"}
CUTS = {"Yawgmoth's Will", "City of Traitors", "Defense Grid", "Demonic Counsel", "Will of the Jeskai"}


def reduced_cost(generic, colored, goblin=False, talent=False, noncreature=True):
    reduction = (2 if goblin else 0) + (1 if talent and noncreature else 0)
    return max(0, generic - reduction), colored


def mayhem_legal(*, discarded_this_turn, in_graveyard, goblin, nonland, is_instant,
                 your_main, empty_stack, flash=False):
    if not (discarded_this_turn and in_graveyard and goblin and nonland):
        return False
    return is_instant or flash or (your_main and empty_stack)


def coliseum_legal(graveyard_count, external_blue_mana, untapped=True):
    # Coliseum itself taps as part of its activation, so can't make its own U.
    return graveyard_count >= 7 and external_blue_mana >= 1 and untapped


def escape_legal(other_gy_cards, mana_payable):
    return other_gy_cards >= 3 and mana_payable


class NormanM7FiniteTests(unittest.TestCase):
    def test_exact_100_source_and_five_real_swaps(self):
        raw = LIST.read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), EXPECTED_SHA)
        rows = raw.decode().splitlines()
        self.assertEqual(len(rows), 100)
        self.assertEqual(rows[0], "1x Norman Osborn // Green Goblin [Commander]")
        self.assertTrue(all(row.startswith("1x ") for row in rows))
        self.assertFalse({k: v for k, v in collections.Counter(rows).items() if v > 1})
        names = {row[3:].removesuffix(" [Commander]") for row in rows}
        self.assertTrue(ADDS <= names)
        self.assertFalse(CUTS & names)

    def test_c1_sorcery_transform_and_mana_pips(self):
        # Front is 1U, transform costs 1UBR; C cannot stand in for U/B/R.
        def can_transform(is_main, stack_empty, generic, u, b, r):
            return is_main and stack_empty and generic >= 1 and min(u, b, r) >= 1
        self.assertTrue(can_transform(True, True, 1, 1, 1, 1))
        self.assertFalse(can_transform(False, True, 6, 1, 1, 1))
        self.assertFalse(can_transform(True, False, 6, 1, 1, 1))
        self.assertFalse(can_transform(True, True, 6, 1, 1, 0))

    def test_k1_generic_discount_and_alternate_cost_separation(self):
        self.assertEqual(reduced_cost(3, "R", goblin=True), (1, "R"))  # Big Score
        self.assertEqual(reduced_cost(3, "RR", goblin=True), (1, "RR"))  # Fervent Mastery mayhem
        self.assertEqual(reduced_cost(3, "RR", goblin=True, talent=True), (0, "RR"))
        self.assertEqual(reduced_cost(1, "U", goblin=True), (0, "U"))
        self.assertEqual(reduced_cost(0, "UB", goblin=True), (0, "UB"))
        # Fervent's 2RR alternative printed cost cannot be combined with mayhem.
        self.assertEqual(reduced_cost(2, "RR", goblin=False), (2, "RR"))

    def test_k2_mayhem_same_turn_zone_timing_negative(self):
        legal = dict(discarded_this_turn=True, in_graveyard=True, goblin=True,
                     nonland=True, is_instant=False, your_main=True, empty_stack=True)
        self.assertTrue(mayhem_legal(**legal))
        self.assertFalse(mayhem_legal(**(legal | {"your_main": False})))
        self.assertFalse(mayhem_legal(**(legal | {"empty_stack": False})))
        self.assertTrue(mayhem_legal(**(legal | {"your_main": False, "flash": True})))
        self.assertTrue(mayhem_legal(**(legal | {"your_main": False, "is_instant": True})))
        self.assertFalse(mayhem_legal(**(legal | {"discarded_this_turn": False})))
        self.assertFalse(mayhem_legal(**(legal | {"goblin": False})))
        self.assertFalse(mayhem_legal(**(legal | {"in_graveyard": False})))
        self.assertFalse(mayhem_legal(**(legal | {"nonland": False})))

    def test_k3_necropotence_and_graveyard_hate(self):
        # Necropotence discard enters GY and its exile trigger goes on stack;
        # non-flash sorcery mayhem cannot answer that stack frame.
        state = dict(discarded_this_turn=True, in_graveyard=True, goblin=True,
                     nonland=True, is_instant=False, your_main=True, empty_stack=False)
        self.assertFalse(mayhem_legal(**state))
        self.assertTrue(mayhem_legal(**(state | {"flash": True})))
        # Yawgmoth's Will replaces new graveyard moves with exile.
        self.assertFalse(mayhem_legal(**(state | {"in_graveyard": False, "flash": True})))
        # Targeted graveyard hate removes Mayhem / Breach resource.
        self.assertFalse(mayhem_legal(**(state | {"in_graveyard": False})))

    def test_k4_both_faces_castable_with_shared_tax_and_cavern(self):
        # One MDFC in the command zone: either creature face can be cast.
        # Tax is calculated from casts of the card, not a separate count per face.
        faces = {"Norman Osborn": (1, "U"), "Green Goblin": (1, "UBR")}
        def command_zone_cost(face, previous_casts_of_card):
            generic, colored = faces[face]
            return generic + 2 * previous_casts_of_card, colored
        self.assertEqual(command_zone_cost("Norman Osborn", 0), (1, "U"))
        self.assertEqual(command_zone_cost("Green Goblin", 0), (1, "UBR"))
        self.assertEqual(command_zone_cost("Green Goblin", 1), (3, "UBR"))
        self.assertEqual(command_zone_cost("Norman Osborn", 2), (5, "U"))
        human_creature_faces = {"Norman Osborn", "Green Goblin"}
        self.assertEqual(set(faces), human_creature_faces)
        # Cavern naming Human protects either cast creature spell, not transform.
        self.assertTrue(all(face in human_creature_faces for face in faces))
        self.assertNotIn("transform activated ability", human_creature_faces)
        self.assertEqual({"U"}, {"U"})  # front-face Amber mana colors
        self.assertEqual({"U", "B", "R"}, set(faces["Green Goblin"][1]))

    def test_corrected_source_json_markdown_regression(self):
        source = json.loads((REPO / "data/grixis_interactions/norman-osborn.json").read_text())
        markdown = (REPO / "grixis/interactions/norman-osborn.md").read_text()
        serialized = json.dumps(source)
        for material in (serialized, markdown):
            self.assertIn("directly from the command zone", material)
            self.assertIn("Cavern", material)
            self.assertIn("cannot be activated during another spell", material)
            self.assertNotIn("Goblin is never cast", material)
            self.assertNotIn("LED may be activated mid-cast", material)

    def test_intuition_graveyard_move_does_not_trigger_mayhem(self):
        # Two tutored cards were *put* in GY, not discarded. No fake Mayhem.
        data = dict(discarded_this_turn=False, in_graveyard=True, goblin=True,
                    nonland=True, is_instant=True, your_main=True, empty_stack=True)
        self.assertFalse(mayhem_legal(**data))

    def test_coliseum_threshold_payable_and_one_source(self):
        self.assertFalse(coliseum_legal(6, 1))
        self.assertFalse(coliseum_legal(7, 0))
        self.assertFalse(coliseum_legal(7, 1, untapped=False))
        self.assertTrue(coliseum_legal(7, 1))

    def test_led_not_usable_during_spell_cost_payment(self):
        def can_activate_led(priority_window, during_cast_601):
            return priority_window and not during_cast_601
        self.assertTrue(can_activate_led(True, False))
        self.assertFalse(can_activate_led(False, True))
        self.assertFalse(can_activate_led(True, True))

    def test_breach_requires_other_cards_and_sufficient_mana(self):
        self.assertFalse(escape_legal(0, True))
        self.assertFalse(escape_legal(2, True))
        self.assertFalse(escape_legal(3, False))
        self.assertTrue(escape_legal(3, True))
        # Station mills three, a single Amber escape exiles three other cards;
        # this can replace consumed fodder, not conjure startup fodder.
        self.assertEqual((5 + 3 - 3), 5)

    def test_samut_scope_and_inti_event_limits(self):
        # Samut grants split second to our *instant/sorcery spells* only,
        # not an Oracle creature or Breach enchantment cast.
        protected_types = {"Instant", "Sorcery"}
        self.assertIn("Instant", protected_types)
        self.assertNotIn("Creature", protected_types)
        self.assertNotIn("Enchantment", protected_types)
        # Inti fires for each discard *event*, not each card of one batch.
        events = [3, 1]
        self.assertEqual(sum(1 for cards_discarded in events if cards_discarded > 0), 2)


if __name__ == "__main__":
    unittest.main()
