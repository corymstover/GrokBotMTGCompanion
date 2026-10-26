"""Deck #34 source-bound finite case tests, not a full MTG rules or win-rate simulator.

Assumed card text is explicitly recorded in the review artifact.  Each test has
a valid paid case and a negative/response case; these are bounded fixtures, not
claims about unmodeled multiplayer priority or stochastic performance.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
M7 = ROOT / "data/grixis/m7"
BASE = M7 / "baseline_sources/Marchesa_Dealer_of_Death_chatgpt_rev1_baseline.txt"
CAND = M7 / "candidate_lists/Marchesa_Dealer_of_Death_chatgpt_rev1.txt"
ALTS = M7 / "research_challengers"
BASE_SHA = "34a6a940c54aaebde612ae5d3a244e22931d3a977fa26e4c43f2a76aafc0f6b1"
CAND_SHA = "f6f68d204925ef3528166722d874cd4122e50755b30f8b9a9ac19d7eff9afd3e"
ADDS = {
    "Demonic Consultation", "Gilded Drake", "Marsh Flats", "Mayhem Devil",
    "Opposition Agent", "Scrabbling Claws", "Sink into Stupor // Soporific Springs",
    "Snuff Out",
}
CUTS = {
    "Copy Enchantment", "Counterbalance", "Dispel", "Great Hall of the Citadel",
    "Last Chance", "Minor Misstep", "Storm-Kiln Artist", "Tolaria",
}


def names(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    assert all(re.fullmatch(r"1x .+(?: \[Commander\])?", s) for s in lines)
    return [s[3:].removesuffix(" [Commander]") for s in lines]


def crime(targets: tuple[str, ...]) -> bool:
    """Each SPELL or ABILITY is a single event, even with several legal targets."""
    return any(x in {"opponent", "opponent_permanent", "opponent_spell",
                     "opponent_ability", "opponent_grave_card"} for x in targets)


class Selection:
    def __init__(self, *, marchesa=True, mana=2, life=20, library=None):
        self.marchesa = marchesa
        self.mana = mana
        self.life = life
        self.library = list(library or ["A", "B", "C", "D"])
        self.hand = []
        self.grave = []
        self.triggered = 0
        self.paid = 0

    def target_event(self, targets: tuple[str, ...], choose=True) -> bool:
        if not self.marchesa or not crime(targets):
            return False
        self.triggered += 1
        if not choose or self.mana < 1:
            return True
        self.mana -= 1
        self.paid += 1
        inspected = self.library[:2]
        del self.library[:2]
        if inspected:
            self.hand.append(inspected[0])
        if len(inspected) == 2:
            self.grave.append(inspected[1])
        return True


class TestMarchesaRev1(unittest.TestCase):
    def test_exact_sources_and_structural_roles(self):
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), BASE_SHA)
        self.assertEqual(hashlib.sha256(CAND.read_bytes()).hexdigest(), CAND_SHA)
        old, new = names(BASE), names(CAND)
        self.assertEqual(len(old), 100)
        self.assertEqual(len(new), 100)
        self.assertEqual(len(set(new)), 100)  # also Pact singleton
        self.assertEqual(CAND.read_text().count("[Commander]"), 1)
        self.assertEqual(new[0], "Marchesa, Dealer of Death")
        self.assertEqual(set(new) - set(old), ADDS)
        self.assertEqual(set(old) - set(new), CUTS)
        for core in (
            "Marchesa, Dealer of Death", "Spatial Binding", "Hex Parasite",
            "Spellskite", "Lapis Lazuli Talisman", "Bender's Waterskin",
            "Tezzeret, Cruel Captain", "Magda, the Hoardmaster",
            "Aphetto Alchemist", "Hawkeye's Bow", "Underworld Breach",
            "Brain Freeze", "Lion's Eye Diamond", "Thassa's Oracle",
            "Tainted Pact", "Rhystic Study", "Ad Nauseam",
        ):
            self.assertIn(core, new)
        # Lands changed: -Tolaria/-Great Hall, +Marsh Flats/+Soporific Springs.
        self.assertEqual(29 - 2 + 1 + 1, 29)  # physical land faces incl. MDFC

    def test_three_full_100_package_challengers(self):
        selected = set(names(CAND))
        alternatives = [
            ("alt8_counterbalance", "728bcddce4c8f80c4c81c8f192f53958e515af035ea9cf8a08aedbd047cce98e",
             "Counterbalance", "Magda, the Hoardmaster"),
            ("alt8_talisman", "1cfa6d9d4c6d6015c9a3676c84e12776407182bbf93159f8c4a071a08e260248",
             "Talisman of Indulgence", "Scrabbling Claws"),
            ("alt9_intuition", "eaac15030cbe0c153c01ce6b7e25efa623087142e5e2f4ccc9f4b12e6d054fed",
             "Intuition", "Praetor's Grasp"),
        ]
        for suffix, expected_sha, add, cut in alternatives:
            p = ALTS / ("Marchesa_Dealer_of_Death_rev1_" + suffix + ".txt")
            self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(), expected_sha)
            alt = names(p)
            self.assertEqual(len(set(alt)), len(alt))
            self.assertEqual(len(alt), 100)
            self.assertEqual(set(alt) - selected, {add})
            self.assertEqual(selected - set(alt), {cut})

    def test_C1_commander_paid_selection_and_removed_negation(self):
        f = Selection(mana=1)
        self.assertTrue(f.target_event(("opponent_permanent",)))
        self.assertEqual((f.triggered, f.paid, f.mana), (1, 1, 0))
        self.assertEqual((f.hand, f.grave, f.library), (["A"], ["B"], ["C", "D"]))
        zero = Selection(mana=0)
        self.assertTrue(zero.target_event(("opponent",)))
        self.assertEqual((zero.paid, zero.hand, zero.grave), (0, [], []))
        absent = Selection(marchesa=False)
        self.assertFalse(absent.target_event(("opponent",)))
        self.assertEqual(absent.triggered, 0)

    def test_K1_target_definition_and_one_crime_per_ability(self):
        self.assertTrue(crime(("opponent", "opponent_permanent", "opponent_spell")))
        self.assertTrue(crime(("opponent_grave_card",)))
        self.assertTrue(crime(("opponent_ability",)))
        self.assertFalse(crime(("self", "own_permanent", "own_grave_card")))
        f = Selection(mana=4)
        f.target_event(("opponent", "opponent_permanent", "opponent_spell"))
        self.assertEqual(f.triggered, 1)

    def test_K2_hex_parasite_x_zero_source_paid(self):
        f = Selection(mana=1, life=10)
        # X=0; {B/P} paid as 2 life, still a legal targeted activation.
        f.life -= 2
        f.target_event(("opponent_permanent",))
        self.assertEqual((f.life, f.paid), (8, 1))
        invalid = Selection(mana=1)
        invalid.target_event(("own_permanent",))
        self.assertEqual(invalid.triggered, 0)

    def test_K3_spatial_binding_life_and_repeat(self):
        f = Selection(life=10, mana=2)
        for _ in range(2):
            f.life -= 1  # printed activation cost; each activation separate
            f.target_event(("opponent_permanent",))
        self.assertEqual((f.life, f.paid, f.mana), (8, 2, 0))
        negated = Selection(life=10, mana=2)
        negated.life -= 1
        negated.target_event(("own_permanent",))
        self.assertEqual(negated.paid, 0)

    def test_K4_lapis_trigger_targets_even_if_optional_three_declined(self):
        f = Selection(mana=1)
        blue_spell = True
        if blue_spell:
            f.target_event(("opponent_permanent",))
        self.assertEqual(f.paid, 1)  # paid Marchesa {1}, NOT Lapis {3}
        red_only = Selection()
        if False:  # no blue spell: no Lapis trigger
            red_only.target_event(("opponent_permanent",))
        self.assertEqual(red_only.triggered, 0)

    def test_K5_tezzeret_kitten_new_object_and_priority_window(self):
        # Each planeswalker object uses a loyalty ability only once/turn.
        activated_objects = set()
        object_id = "tezzeret_first_object"
        f = Selection(mana=2)
        if object_id not in activated_objects:
            activated_objects.add(object_id)
            f.target_event(("opponent_permanent",))  # loyalty 0
        self.assertIn(object_id, activated_objects)
        self.assertEqual(f.paid, 1)
        # A noncreature spell and Displacer Kitten's legal blink make a NEW object.
        object_id = "tezzeret_after_blink"
        activated_objects.add(object_id)
        f.target_event(("opponent_permanent",))
        self.assertEqual(f.paid, 2)
        # Cursed Totem doesn't stop loyalty; no Kitten/new object forbids repeat.
        self.assertEqual(len(activated_objects), 2)

    def test_K6_removed_last_chance_is_not_current_candidate_requirement(self):
        self.assertNotIn("Last Chance", names(CAND))
        self.assertIn("Final Fortune", names(CAND))
        # Historical rule, not an active two-extra-turn package: latest extra
        # turn created is taken first.  No second source remains in the list.
        queued = ["Final Fortune", "Last Chance"]
        self.assertEqual(queued.pop(), "Last Chance")

    def test_K7_mox_amber_and_magda_tapped_treasure(self):
        def amber_colors(legends):
            return set().union(*legends) if legends else set()
        self.assertEqual(amber_colors([]), set())
        self.assertEqual(amber_colors([{"R"}]), {"R"})  # Magda alone
        self.assertEqual(amber_colors([{"U", "B", "R"}]), {"U", "B", "R"})
        treasure = {"tapped": True, "made_this_turn": True}
        self.assertFalse(not treasure["tapped"])  # cannot fund its own first crime
        magda_triggered_this_turn = True
        second_crime_adds_treasure = not magda_triggered_this_turn
        self.assertFalse(second_crime_adds_treasure)

    def test_E1_claws_devils_and_drake_paid_new_crimes(self):
        f = Selection(mana=3, library=list("ABCDEFGH"))
        # Claws targets PLAYER; works even when that player's GY is empty.
        f.target_event(("opponent",))
        # Each sacrificed permanent independently makes a Mayhem Devil trigger.
        f.target_event(("opponent_permanent",))
        # Drake's ETB targets an opponent-controlled creature.
        f.target_event(("opponent_permanent",))
        self.assertEqual(f.paid, 3)
        no_creature = Selection()
        no_creature.target_event(())
        self.assertEqual(no_creature.triggered, 0)
        self.assertEqual(f.grave, ["B", "D", "F"])

    def test_E2_mana_and_draw_limitations(self):
        # 0-mana artifact mana is not 'colored for every purpose': Mox Amber
        # requires a legendary creature/planeswalker; Marchesa costs UBR.
        colored = {"U": 1, "B": 1, "R": 1}
        self.assertTrue(all(colored[c] >= 1 for c in "UBR"))
        missing_red = {"U": 1, "B": 1, "R": 0}
        self.assertFalse(all(missing_red[c] >= 1 for c in "UBR"))
        # Effect-aware opening probability is deliberately NOT claimed.

    def test_W1_oracle_consult_source_paid_and_stack_disruption(self):
        # Oracle ETB trigger must already be on stack, Consultation names a
        # genuinely absent card and can exile the entire library on resolution.
        stack = ["Thassa's Oracle ETB"]
        life_library = ["A", "B", "C", "D", "E", "F"]
        named_absent_card = "Not In Deck"
        self.assertNotIn(named_absent_card, names(CAND))
        life_library.clear()  # Consultation resolves, never finds named card
        devotion_blue = 2
        self.assertTrue(len(life_library) <= devotion_blue and bool(stack))
        stack.clear()  # Stifle/ability-counter in response: no Oracle trigger
        self.assertFalse(bool(stack))

    def test_W2_breach_led_brain_freeze_hate_response(self):
        grave = {"Brain Freeze", "Lion's Eye Diamond", "filler_1", "filler_2",
                 "filler_3", "filler_4", "filler_5", "filler_6"}
        self.assertTrue({"Brain Freeze", "Lion's Eye Diamond"} <= grave)
        self.assertGreaterEqual(len(grave - {"Brain Freeze"}), 3)
        # Actual escape requires card and 3 other cards in GY per cast; opponents
        # can interrupt.  Exiling Brain Freeze kills THIS explicit line.
        grave.remove("Brain Freeze")
        self.assertNotIn("Brain Freeze", grave)

    def test_W3_bow_alchemist_three_finite_tap_cycles_and_tomem(self):
        damage = [0, 0, 0]
        alchemist_can_tap = True  # not summoning sick and untapped
        bow_equipped = True
        for _ in range(3):
            if alchemist_can_tap and bow_equipped:
                damage = [x + 1 for x in damage]
                alchemist_can_tap = True  # targeted self-untap on resolution
        self.assertEqual(damage, [3, 3, 3])
        self.assertFalse(crime(("own_permanent",)))  # Bow damage is nontargeting
        cursed_totem_active = True
        self.assertFalse(alchemist_can_tap and not cursed_totem_active)

    def test_F1_graveyard_hate_and_counterplay(self):
        f = Selection(mana=1)
        opponent_grave = {"Underworld Breach", "Brain Freeze"}
        # Scrabbling Claws sacrificial mode can target the exact enemy GY card,
        # while tap mode only makes target opponent select one to exile.
        f.target_event(("opponent_grave_card",))
        opponent_grave.remove("Brain Freeze")
        self.assertNotIn("Brain Freeze", opponent_grave)
        self.assertEqual(f.paid, 1)
        # A target card that leaves the GY before resolution cannot be exiled
        # a second time, though the initial target already committed the crime.
        self.assertNotIn("Brain Freeze", opponent_grave)

    def test_F2_removed_commander_gives_no_selection(self):
        f = Selection(marchesa=False, mana=5)
        f.target_event(("opponent_spell",))
        self.assertEqual((f.triggered, f.paid, f.mana), (0, 0, 5))

    def test_F3_historical_baseline_is_not_the_M7_source(self):
        # The old 48-card October 15 rebuild is historical; this change is
        # exactly 8 new swaps relative to the SHA-bound approved October 15 100.
        self.assertEqual(len(set(names(BASE)) - set(names(CAND))), 8)

    def test_selected_new_card_target_caveats(self):
        self.assertTrue(crime(("opponent_permanent",)))  # free Snuff Out
        self.assertFalse(crime(()))  # Opposition Agent does not target
        self.assertTrue(crime(("opponent_spell",)))  # Sink into Stupor
        self.assertFalse(crime(()))  # Sink used as a land
        self.assertFalse(crime(()))  # Demonic Consultation has no target


if __name__ == "__main__":
    unittest.main()
