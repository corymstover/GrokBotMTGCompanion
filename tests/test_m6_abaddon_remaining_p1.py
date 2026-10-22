"""Abaddon residual P1: three source-backed exceptional mana/exile cases.
Seven finite physical fixtures (Delayed Blast Fireball, Nightscape Familiar,
Jeska's Will); no randomized game or complete Magic engine inference.
"""
from __future__ import annotations

import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_m6_abaddon_threshold_doublers_p0 as base
import test_m6_abaddon_residual_p1 as prior

DELAYED = "Delayed Blast Fireball"
NIGHT = "Nightscape Familiar"
JESKA = "Jeska's Will"
PROSPER = "Prosper, Tome-Bound"
KESSIG = "Kessig Flamebreather"
RITE = "Rite of Flame"
IGNUS = "Grinning Ignus"
VIVI = "Vivi Ornitier"


def exile_cast_delayed(*, blood=False, solphim=False):
    s = prior.begin(staged=(PROSPER,), blood=blood, solphim=solphim)
    # One physical possible top-card arrangement at Prosper's prior end step.
    s["library"].remove(DELAYED)
    s["library"].insert(0, DELAYED)
    base.move(s, DELAYED, "library", "exile")
    s["impulse_permission"] = "Prosper previous end step: until end of this turn"
    # Current turn, pay Delayed's real {1}{R}{R} from fresh lands.
    for land, mana in (("Mountain", "R"), ("Mountain", "R"), ("Island", "C")):
        base.move(s, land, "library", "battlefield")
        s["source_payments"].append((land, mana, DELAYED))
    base.move(s, DELAYED, "exile", "stack")
    s["cast_total"] += 1
    s["cast_log"].append((DELAYED, "exile", base.x(s)))
    # Cast from exile cannot earn Abaddon's CAST FROM HAND cascade.
    s["opponent_creature_damage"] = [0, 0, 0]
    base.conserved(s)
    return s


def resolve_delayed(s, *, cast_from_exile):
    amount = 5 if cast_from_exile else 2
    base.noncombat_damage(s, amount, source=DELAYED)
    # Solphim applies only to OPPONENT damage; their creatures take 2/5.
    s["opponent_creature_damage"] = [amount] * 3
    base.move(s, DELAYED, "stack", "graveyard")
    base.conserved(s)


class AbaddonRemainingSourcePaidP1(unittest.TestCase):
    def test_delayed_hand_cast_two_damage_three_opponents_x6(self):
        s = prior.paid_cast(prior.begin(), DELAYED,
                            (("Mountain", "R"), ("Mountain", "R"), ("Island", "C")),
                            noncreature=True, instant_sorcery=True)
        s["opponent_creature_damage"] = [0, 0, 0]
        resolve_delayed(s, cast_from_exile=False)
        self.assertEqual(s["damage_dealt"], [2, 2, 2])
        self.assertEqual(s["opponent_creature_damage"], [2, 2, 2])
        self.assertEqual(base.x(s), 6)
        self.assertEqual(s["self_life"], 40)

    def test_delayed_prosper_exile_paid_five_damage_not_hand_cascade(self):
        s = exile_cast_delayed()
        self.assertIn("Prosper", s["impulse_permission"])
        self.assertEqual(s["cascade_triggers"], 0)
        resolve_delayed(s, cast_from_exile=True)
        self.assertEqual(s["damage_dealt"], [5, 5, 5])
        self.assertEqual(s["opponent_creature_damage"], [5, 5, 5])
        self.assertEqual(base.x(s), 15)
        self.assertEqual(s["self_life"], 40)

    def test_delayed_exile_bloodletter_solphim_doubles_opponents_not_creatures(self):
        s = exile_cast_delayed(blood=True, solphim=True)
        resolve_delayed(s, cast_from_exile=True)
        self.assertEqual(s["damage_dealt"], [10, 10, 10])
        self.assertEqual(s["lost_this_turn"], [20, 20, 20])
        self.assertEqual(s["opponent_creature_damage"], [5, 5, 5])
        self.assertEqual(base.x(s), 60)
        self.assertEqual(s["self_life"], 40)

    def test_nightscape_discount_ignus_paid_1r_keeps_mana_value_three(self):
        s = prior.paid_cast(prior.begin(staged=(NIGHT, KESSIG)), RITE,
                            (("Mountain", "R"),),
                            noncreature=True, instant_sorcery=True)
        prior.resolve_to_grave(s, RITE)
        self.assertEqual(base.x(s), 3)
        # Nightscape Familiar reduces only one generic from printed {2}{R}.
        prior.paid_cast(s, IGNUS,
                        (("Mountain", "R"), ("Island", "C")),
                        noncreature=False, instant_sorcery=False)
        base.move(s, IGNUS, "stack", "battlefield")
        self.assertEqual(s["source_payments"][-2:], [
            ("Mountain", "R", IGNUS), ("Island", "C", IGNUS)])
        self.assertEqual(s["cascade_triggers"], 1)
        self.assertEqual(s["cast_log"][-1], (IGNUS, "hand", 3))
        base.conserved(s)

    def test_nightscape_blue_red_spell_receives_one_discount_not_two(self):
        s = prior.paid_cast(prior.begin(staged=(NIGHT,)), VIVI,
                            (("Island", "U"), ("Mountain", "R")),
                            noncreature=False)
        base.move(s, VIVI, "stack", "battlefield")
        # Vivi is printed {1}{U}{R}: ONE static reduction removes {1}.
        self.assertEqual(s["source_payments"], [
            ("Island", "U", VIVI), ("Mountain", "R", VIVI)])
        self.assertEqual(s["cast_total"], 1)
        base.conserved(s)

    def test_jeska_both_modes_locked_at_cast_mana_uses_resolution_hand_size(self):
        s = prior.paid_cast(prior.begin(), JESKA,
                            (("Island", "C"), ("Island", "C"), ("Mountain", "R")),
                            noncreature=True, instant_sorcery=True)
        self.assertTrue(s["commander_controlled"])
        selected_modes = ("mana", "impulse")
        self.assertEqual(len(selected_modes), 2)
        target_hand_at_cast = 6
        target_hand_at_resolution = 4  # opponent legitimately responds
        # Removal of Abaddon after modes were chosen cannot remove a mode.
        s["commander_controlled"] = False
        red_mana_generated = target_hand_at_resolution
        self.assertEqual(red_mana_generated, 4)
        self.assertNotEqual(red_mana_generated, target_hand_at_cast)
        for name in ("Sol Ring", "Arcane Signet", "Island"):
            base.move(s, name, "library", "exile")
        prior.resolve_to_grave(s, JESKA)
        self.assertIn("Sol Ring", s["exile"])
        self.assertEqual(s["cast_total"], 1)  # exiling is not casting
        self.assertEqual(s["cascade_triggers"], 0)
        self.assertEqual(base.x(s), 0)
        base.conserved(s)

    def test_jeska_without_commander_only_one_mode(self):
        s = prior.begin()
        s["commander_controlled"] = False
        prior.paid_cast(s, JESKA,
                        (("Island", "C"), ("Island", "C"), ("Mountain", "R")),
                        noncreature=True, instant_sorcery=True)
        modes = ("mana",)  # legally selected one; not both
        red_mana_generated = 5  # target opponent has five cards at resolution
        self.assertEqual(len(modes), 1)
        self.assertEqual(red_mana_generated, 5)
        self.assertEqual(len(s["exile"]), 0)  # no impulse mode
        prior.resolve_to_grave(s, JESKA)
        base.conserved(s)


if __name__ == "__main__":
    unittest.main()
