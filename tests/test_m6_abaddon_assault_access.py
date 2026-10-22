import random
import unittest
from fractions import Fraction
from scripts.grixis_m6_abaddon_assault_access import (
    BASICS, TARGETS, draw_only_probabilities, eligible_fetch_targets,
    frozen_source, land_colors, libraries, run, source_payable, trial,
)


class AbaddonAccessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan, cls.base = frozen_source()
        cls.libs = libraries(cls.base, cls.plan)

    def test_frozen_inventory_and_single_slot(self):
        self.assertEqual(len(self.base), 99)
        self.assertEqual(sum(n in BASICS for n in self.base), 9)
        self.assertEqual(len(self.libs), 3)
        for v, lib in self.libs.items():
            self.assertEqual(len(lib), 99)
            diff = [(a, b) for a, b in zip(self.base, lib) if a != b]
            self.assertEqual(len(diff), 0 if v == "baseline" else 1)
            self.assertEqual(lib.count("Aggravated Assault"), 0 if v == "baseline" else 1)

    def test_source_assignment_not_double_spent(self):
        self.assertFalse(source_payable([("Badlands", False), ("Volcanic Island", False),
                                         ("Underground Sea", False)], "Rakdos, Lord of Riots"))
        self.assertTrue(source_payable([("Badlands", False), ("Volcanic Island", False),
                                        ("Underground Sea", False), ("Mountain", False)],
                                       "Rakdos, Lord of Riots"))

    def test_ancient_tomb_two_generic_not_two_red(self):
        self.assertTrue(source_payable([("Ancient Tomb", False), ("Mountain", False)],
                                       "Aggravated Assault"))
        self.assertFalse(source_payable([("Ancient Tomb", False), ("Mountain", False),
                                         ("Mountain", False)], "Neheb, the Eternal"))

    def test_urborg_grants_alternative_black_not_bonus(self):
        self.assertEqual(set(land_colors("Ancient Tomb", True)), {("C", "C"), ("B",)})
        self.assertTrue(source_payable([("Urborg, Tomb of Yawgmoth", False),
                                        ("Island", False), ("Mountain", False),
                                        ("Ancient Tomb", False)], "Abaddon the Despoiler"))

    def test_tapped_land_not_used_on_its_arrival(self):
        self.assertFalse(source_payable([("Xander's Lounge", True),
                                         ("Island", False), ("Swamp", False),
                                         ("Ancient Tomb", False)],
                                        "Abaddon the Despoiler"))
        self.assertTrue(source_payable([("Xander's Lounge", False),
                                        ("Island", False), ("Swamp", False),
                                        ("Ancient Tomb", False)],
                                       "Abaddon the Despoiler"))

    def test_exotic_orchard_unknown_not_assumed_rainbow(self):
        self.assertEqual(land_colors("Exotic Orchard"), [])
        self.assertFalse(source_payable([("Exotic Orchard", False), ("Ancient Tomb", False)],
                                        "Aggravated Assault"))

    def test_fetch_targets_real_library_and_card_types(self):
        self.assertEqual(eligible_fetch_targets("Polluted Delta", ["Mountain"]), [])
        targets = eligible_fetch_targets("Polluted Delta", ["Island", "Underground Sea",
                                                           "Badlands", "Xander's Lounge"])
        self.assertEqual(targets[0], "Badlands")
        self.assertIn("Xander's Lounge", targets)

    def test_draw_only_exact_fraction(self):
        self.assertEqual(draw_only_probabilities(6)["one_named_singleton"], str(Fraction(13, 99)))
        self.assertEqual(draw_only_probabilities(10)["three_named_singletons"],
                         str(Fraction(17 * 16 * 15, 99 * 98 * 97)))

    def test_deterministic_trial_same_seed(self):
        a = trial(self.libs["assault_for_rakdos"], 621017, [4, 6, 8, 10])
        b = trial(self.libs["assault_for_rakdos"], 621017, [4, 6, 8, 10])
        self.assertEqual(a, b)
        self.assertGreaterEqual(a[1], 0)

    def test_paired_initial_index_mapping(self):
        seed = 621017
        ids = list(range(99))
        random.Random(seed).shuffle(ids)
        for variant, lib in self.libs.items():
            source_changes = [i for i in ids[:7] if self.base[i] != lib[i]]
            self.assertLessEqual(len(source_changes), 1)

    def test_report_is_never_certificate_or_win_rate(self):
        rec = run(12)
        self.assertEqual(rec["samples_per_variant"], 12)
        self.assertEqual(set(rec["observations"]), set(self.libs))
        self.assertIsNone(rec["limits"]["multiplayer_win_rate"])
        self.assertFalse(rec["limits"]["proves_swap_superiority"])
        self.assertFalse(rec["limits"]["has_actual_combo_assembly"])
        self.assertFalse(rec["limits"]["approved_deck_changed"])


if __name__ == "__main__":
    unittest.main()
