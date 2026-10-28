"""Parnesse current-SHA original P1 K5/K6/K7/E1/F3 bounded stack models.

Exactly five previously DESIGN_ONLY case groups, each with normal and negated
preconditions. This is not a complete multiplayer Magic rules engine or a
win-rate estimate. The original K7 infinite claim is necessarily conditional:
Reiterate buyback must be payable repeatedly and its target ritual copy must
generate *more than six red mana* for strictly increasing mana without other
resources.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "data/grixis/m7/candidate_lists/Parnesse_the_Subtle_Brush_M7_Rev1_Approved_2026-10-27.txt"
PLAN = ROOT / "data/grixis/m6/test_blueprints/Parnesse__the_Subtle_Brush.json"
SHA = "63b605a2c36ec81ab7a5a48770ac2b96b7994daf38546aba7b6bc6bd7597928c"
CASES = {
    "K5": {"Parnesse, the Subtle Brush", "Chaos Warp"},
    "K6": {"Parnesse, the Subtle Brush", "Bonus Round", "Chaos Warp", "Reverberate"},
    "K7": {"Reiterate", "Mana Geyser", "Jeska's Will", "Grapeshot"},
    "E1": {"Parnesse, the Subtle Brush", "Harmonic Prodigy", "Veyran, Voice of Duality", "Wizard's Staff", "Reverberate"},
    "F3": {"Flusterstorm", "Reiterate", "Mana Geyser", "Fierce Guardianship", "Parnesse, the Subtle Brush"},
}


def opponent_target_tax(copy_controller, target_controller, life_paid, parnesse_present=True):
    """Independent Parnesse tax per opposing spell/copy's new target."""
    targeted_by_opponent = parnesse_present and copy_controller == "opponent" and target_controller == "you"
    return "countered" if targeted_by_opponent and life_paid < 4 else "not_countered_by_parnesse"


def bonus_round_cast_copies(spell_controller, bonus_resolved):
    """Resolved Bonus Round lets *each* player copy their own later I/S cast."""
    return {"copy_count": int(bonus_resolved), "copy_controller": spell_controller}


def iterate_ritual(mana_available, ritual_red_output, target_on_stack=True,
                   buyback=True, red_sources_available=True):
    """One Reiterate buyback copy: cost 1RR+3=4RR (6), returns card to hand."""
    if not target_on_stack or not buyback or not red_sources_available or mana_available < 6:
        return None
    return mana_available - 6 + ritual_red_output


def parnesse_gift_triggers(copied_spell_type, staff_equipped, harmonic, veyran):
    """Additional trigger clauses add once each; they do not multiply 2^n."""
    native = 1
    if copied_spell_type == "none":
        return 0
    return native + int(staff_equipped) + int(harmonic) + int(
        veyran and copied_spell_type in ("instant", "sorcery"))


def protected_loop_target(target_spell_is_still_on_stack, answer_countered,
                          sufficient_mana):
    """Original ritual must still be a valid target and resistance overcome."""
    return target_spell_is_still_on_stack and answer_countered and sufficient_mana


class ParnesseCurrentOriginalP1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = DECK.read_bytes()
        if sha256(raw).hexdigest() != SHA:
            raise AssertionError("owner-approved current 100 drifted")
        lines = raw.decode("utf-8").splitlines()
        if not lines or lines[0] != "1x Parnesse, the Subtle Brush [Commander]":
            raise AssertionError("current commander or first line changed")
        cls.cards = Counter()
        for line in lines:
            quantity, name = line.split("x ", 1)
            cls.cards[name.removesuffix(" [Commander]")] += int(quantity)
        if sum(cls.cards.values()) != 100 or any(
            qty != 1 for name, qty in cls.cards.items() if name not in {"Island", "Mountain", "Swamp"}
        ):
            raise AssertionError("exact-current physical roster invalid")
        blueprint = json.loads(PLAN.read_text())
        by_id = {case["id"]: case for case in blueprint["cases"]}
        p1 = {case["id"] for case in blueprint["cases"] if case["priority"] == "P1"}
        if len(p1) != 11 or not set(CASES).issubset(p1):
            raise AssertionError("original P1 blueprint drifted")
        for case_id, necessary in CASES.items():
            if by_id[case_id]["priority"] != "P1" or not all(cls.cards[n] == 1 for n in necessary):
                raise AssertionError(f"original P1 {case_id} or source card missing")
        cls.oracle = blueprint["commander_oracle_snapshots"][0]["oracle_text"]
        assert "counter that spell or ability unless that player pays 4 life" in cls.oracle
        assert "Whenever you copy a spell" in cls.oracle

    def test_K5_gifted_copy_is_opponent_controlled_and_taxed_only_when_targeting_mine(self):
        # I copied a valid on-stack Chaos Warp; Parnesse offered an opponent a
        # separate copy and they chose my permanent as its new target.
        self.assertEqual(opponent_target_tax("opponent", "you", 0), "countered")
        self.assertEqual(opponent_target_tax("opponent", "you", 3), "countered")
        self.assertEqual(opponent_target_tax("opponent", "you", 4), "not_countered_by_parnesse")
        self.assertEqual(opponent_target_tax("opponent", "opponent", 0), "not_countered_by_parnesse")
        self.assertEqual(opponent_target_tax("you", "you", 0), "not_countered_by_parnesse")
        self.assertEqual(opponent_target_tax("opponent", "you", 0, False), "not_countered_by_parnesse")

    def test_K6_bonus_round_symmetry_and_own_copy_trigger_boundary(self):
        # Pay {1}{R}{R} for Bonus Round, then its symmetric effect starts only
        # after it resolves, and creates a copy controlled by the original caster.
        self.assertEqual(bonus_round_cast_copies("you", True), {"copy_count": 1, "copy_controller": "you"})
        self.assertEqual(bonus_round_cast_copies("opponent", True),
                         {"copy_count": 1, "copy_controller": "opponent"})
        self.assertEqual(bonus_round_cast_copies("you", False)["copy_count"], 0)
        self.assertFalse(bonus_round_cast_copies("opponent", True)["copy_controller"] == "you")
        # The opponent's bonus copy is not a copy *you* made, so doesn't gift
        # again under your Parnesse. The opponent's targeted copy can be taxed.
        self.assertEqual(opponent_target_tax("opponent", "you", 0), "countered")
        self.assertEqual(opponent_target_tax("opponent", "you", 4), "not_countered_by_parnesse")

    def test_K7_reiterate_infinite_red_needs_real_buyback_and_net_positive_ritual(self):
        # Mana Geyser creates R equal to *tapped lands opponents control*.
        # Jeska's Will's selected mana mode creates R equal to selected
        # opponent's *hand size*. Neither resource threshold is guaranteed.
        self.assertEqual(iterate_ritual(6, 7), 7)  # +1, repeatable, unbounded with live target
        self.assertEqual(iterate_ritual(6, 6), 6)  # no net mana; possible storm, not infinite mana
        self.assertEqual(iterate_ritual(6, 5), 5)  # loses one mana each paid repetition
        self.assertIsNone(iterate_ritual(5, 10))  # cannot pay 4RR in the first place
        self.assertIsNone(iterate_ritual(6, 10, target_on_stack=False))
        self.assertIsNone(iterate_ritual(6, 10, buyback=False))
        self.assertIsNone(iterate_ritual(6, 10, red_sources_available=False))
        self.assertEqual(iterate_ritual(8, 8), 10)
        self.assertIn("Grapeshot", self.cards)  # finish exists, but only after actual spell chain

    def test_E1_copy_politics_additional_triggers_are_optional_not_exponential(self):
        self.assertEqual(parnesse_gift_triggers("instant", False, False, False), 1)
        self.assertEqual(parnesse_gift_triggers("instant", True, True, True), 4)
        self.assertEqual(parnesse_gift_triggers("sorcery", True, False, True), 3)
        # Veyran's extra-trigger clause requires casting/copying an I/S spell;
        # a copied non-I/S spell still triggers Parnesse itself but not Veyran.
        self.assertEqual(parnesse_gift_triggers("creature", True, True, True), 3)
        self.assertEqual(parnesse_gift_triggers("none", True, True, True), 0)
        # Each trigger offers up to one target opponent a copy. You may decline.
        available = parnesse_gift_triggers("instant", True, True, True)
        self.assertEqual(sum([False] * available), 0)
        self.assertEqual(sum([True, False, False, False]), 1)

    def test_F3_counterspell_on_original_or_copy_disrupts_unprotected_engine(self):
        # Flusterstorm can target Reiterate (an instant) unless a payable tax
        # is met. Fierce Guardianship needs a legal spell and a commander for
        # the free alternative; it does not magically pre-exist in hand.
        self.assertTrue(protected_loop_target(True, True, True))
        self.assertFalse(protected_loop_target(False, True, True))  # original ritual countered
        self.assertFalse(protected_loop_target(True, False, True))  # response was not answered
        self.assertFalse(protected_loop_target(True, True, False))  # cannot pay required 4RR
        self.assertEqual(self.cards["Mana Drain"], 1)
        self.assertEqual(self.cards["Fierce Guardianship"], 1)


if __name__ == "__main__":
    unittest.main()
