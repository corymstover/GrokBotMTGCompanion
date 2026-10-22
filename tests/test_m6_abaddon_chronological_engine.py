import unittest
from scripts.grixis_m6_abaddon_chronological_engine import (
    ENGINE, ZERO, _pay_from_pool, one_physical_trial, pay_and_tap,
    physical_payment, postcombat_window,
)
from scripts.grixis_m6_abaddon_assault_access import frozen_source, libraries


class ChronologicalAbaddonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan, cls.base = frozen_source()
        cls.variants = libraries(cls.base, cls.plan)

    def test_actual_colored_pips_need_three_colors_and_five_mana(self):
        lands = [("Island", False), ("Swamp", False), ("Mountain", False),
                 ("Ancient Tomb", False)]
        self.assertIsNotNone(physical_payment(lands, ZERO, "Abaddon the Despoiler"))
        self.assertIsNone(physical_payment(lands[:3], ZERO, "Abaddon the Despoiler"))

    def test_ancient_tomb_surplus_floats_and_cannot_double_tap(self):
        lands = [("Ancient Tomb", False)]
        left = pay_and_tap(lands, ZERO, "Aggravated Assault",
                           source_cost_override=(1, (0, 0, 0)))
        self.assertEqual(left, (0, 0, 0, 1))
        self.assertTrue(lands[0][1])
        self.assertEqual(pay_and_tap(lands, left, "Aggravated Assault",
                                     source_cost_override=(1, (0, 0, 0))), ZERO)
        self.assertIsNone(pay_and_tap(lands, ZERO, "Aggravated Assault",
                                      source_cost_override=(1, (0, 0, 0))))

    def test_one_real_source_cannot_pay_two_separate_spells(self):
        lands = [("Command Tower", False), ("Underground Sea", False),
                 ("Badlands", False), ("Ancient Tomb", False)]
        remaining = pay_and_tap(lands, ZERO, "Abaddon the Despoiler")
        self.assertIsNotNone(remaining)
        self.assertIsNone(pay_and_tap(lands, remaining, "Loyal Subordinate"))

    def test_urborg_creates_alternative_tap_ability_not_bonus_mana(self):
        lands = [("Urborg, Tomb of Yawgmoth", False),
                 ("Island", False), ("Mountain", False), ("Ancient Tomb", False)]
        result = physical_payment(lands, ZERO, "Abaddon the Despoiler")
        self.assertIsNotNone(result)
        self.assertEqual(len(result[0]), 4)
        # Tomb must use two generic mana to reach five units: Urborg itself
        # supplies B and other colored lands supply U/R.
        self.assertIn(3, result[0])

    def test_tapped_land_unavailable_for_paid_cast(self):
        lands = [("Xander's Lounge", True), ("Island", False),
                 ("Swamp", False), ("Mountain", False)]
        self.assertIsNone(physical_payment(lands, ZERO, "Abaddon the Despoiler"))

    def test_no_implicit_orchard_colors(self):
        lands = [("Exotic Orchard", False), ("Mountain", False),
                 ("Ancient Tomb", False)]
        self.assertIsNotNone(physical_payment(lands, ZERO, "Aggravated Assault"))
        self.assertIsNone(physical_payment(lands, ZERO, "Abaddon the Despoiler"))

    def test_generic_remainder_respects_selected_colored_pips(self):
        self.assertIsNone(_pay_from_pool((2, 0, 2, 0), (5, (1, 1, 1))))
        self.assertEqual(_pay_from_pool((1, 1, 1, 2), (5, (1, 1, 1))), ZERO)
        self.assertEqual(_pay_from_pool((0, 0, 3, 3), (3, (0, 0, 1))),
                         (0, 0, 0, 3))

    def test_loyal_no_tap_and_all_three_opponents_lose_three(self):
        loss = postcombat_window(set(ENGINE))
        self.assertEqual(loss["opponents_lost"], 9)
        self.assertEqual(loss["neheb_red"], 9)
        self.assertTrue(loss["assault_first_postcombat_activation"])
        self.assertEqual(loss["assault_red_spent"], 5)
        self.assertFalse(loss["extra_combat_win_proved"])

    def test_commander_removed_before_combat_blocks_drain(self):
        out = postcombat_window(set(ENGINE), commander_removed_before_combat=True)
        self.assertEqual(out["opponents_lost"], 0)
        self.assertEqual(out["neheb_red"], 0)
        self.assertFalse(out["assault_first_postcombat_activation"])

    def test_neheb_or_loyal_absent_stops_neheb_funded_activation(self):
        for gone in ("Neheb, the Eternal", "Loyal Subordinate"):
            with self.subTest(gone=gone):
                result = postcombat_window(set(ENGINE) - {gone})
                self.assertFalse(result["assault_first_postcombat_activation"])

    def test_assault_presence_does_not_itself_win(self):
        result = postcombat_window({"Aggravated Assault", "Neheb, the Eternal"})
        self.assertFalse(result["assault_first_postcombat_activation"])
        self.assertFalse(result["extra_combat_win_proved"])

    def test_paid_setup_can_complete_across_distinct_turns(self):
        lands = [("Island", False), ("Swamp", False), ("Mountain", False),
                 ("Ancient Tomb", False), ("Badlands", False)]
        battlefield = set()
        for name in ENGINE:
            lands = [(land, False) for land, _ in lands]  # Next own turn, untap
            rest = pay_and_tap(lands, ZERO, name)
            self.assertIsNotNone(rest, name)
            battlefield.add(name)
        self.assertTrue(postcombat_window(battlefield)["assault_first_postcombat_activation"])

    def test_actual_physical_library_trial_reproduces(self):
        lib = self.variants["assault_for_rakdos"]
        a = one_physical_trial(lib, 621017, horizon=10)
        b = one_physical_trial(lib, 621017, horizon=10)
        self.assertEqual(a, b)
        self.assertTrue(a["actual_modeled_land_payments"])
        self.assertIsNone(a["actual_multiplayer_game_win"])
        self.assertTrue(all(1 <= turn <= 10 for turn in a["cast_turns"].values()))

    def test_baseline_cannot_create_assault_from_empty_slot(self):
        r = one_physical_trial(self.variants["baseline"], 621017, horizon=10)
        self.assertNotIn("Aggravated Assault", r["cast_turns"])
        self.assertIsNone(r["first_payable_postcombat_assault_activation_turn"])

    def test_no_phantom_four_piece_if_assault_only_drawn(self):
        r = postcombat_window({"Aggravated Assault", "Abaddon the Despoiler"})
        self.assertFalse(r["assault_first_postcombat_activation"])


if __name__ == "__main__":
    unittest.main()
