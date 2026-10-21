"""Focused Abaddon Rakdos opportunity-cost regressions; no empirical win rates."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from grixis_m6_abaddon_rakdos_role import (
    assault_activation_cost, baseline_creature_inventory, payment, report,
)


class RakdosCostRegression(unittest.TestCase):
    def test_approved_full_deck_creature_inventory(self):
        inventory = baseline_creature_inventory()
        self.assertEqual((inventory["cards"], inventory["distinct"]), (100, 94))
        self.assertEqual(inventory["potential_discountable_creature_names"], 17)
        self.assertIn("Abaddon the Despoiler", inventory["potential_beneficiaries"])
        self.assertNotIn("Rakdos, Lord of Riots", inventory["potential_beneficiaries"])

    def test_multiopponent_life_loss_reduces_generic_to_zero(self):
        loss = 3 + 3 + 3  # Loyal Subordinate with three opponents, conditional
        self.assertEqual(payment("Neheb, the Eternal", loss, rakdos_present=True)["generic_due"], 0)
        self.assertEqual(payment("Loyal Subordinate", loss, rakdos_present=True)["generic_due"], 0)
        self.assertEqual(payment("Prosper, Tome-Bound", loss, rakdos_present=True)["generic_due"], 0)

    def test_colored_pips_unchanged(self):
        p = payment("Abaddon the Despoiler", 9, rakdos_present=True)
        self.assertEqual(p["colored_due"], {"U": 1, "B": 1, "R": 1})
        self.assertEqual(p["generic_due"], 0)

    def test_commander_tax_added_before_reduction(self):
        p = payment("Abaddon the Despoiler", 9, rakdos_present=True, commander_tax=4)
        self.assertEqual((p["generic_due"], p["discount"], p["mana_value"]), (0, 6, 5))

    def test_discount_does_not_change_printed_mana_value(self):
        self.assertEqual(payment("Neheb, the Eternal", 9, rakdos_present=True)["mana_value"], 5)

    def test_no_rakdos_or_new_turn_means_no_discount(self):
        self.assertEqual(payment("Neheb, the Eternal", 9, rakdos_present=False)["generic_due"], 3)
        self.assertEqual(payment("Neheb, the Eternal", 0, rakdos_present=True)["generic_due"], 3)

    def test_life_gain_back_does_not_cancel_that_turns_loss(self):
        loss_before_gain, subsequent_life_gain = 5, 20
        self.assertGreater(subsequent_life_gain, loss_before_gain)
        self.assertEqual(payment("Neheb, the Eternal", loss_before_gain,
                                 rakdos_present=True)["generic_due"], 0)

    def test_rakdos_never_reduces_its_own_initial_cost(self):
        p = payment("Rakdos, Lord of Riots", 9, rakdos_present=True)
        self.assertEqual((p["discount"], p["colored_due"]), (0, {"B": 2, "R": 2}))

    def test_assault_is_not_a_creature_spell_and_its_activation_is_not_discounted(self):
        self.assertEqual(payment("Aggravated Assault", 9, rakdos_present=True)["generic_due"], 2)
        self.assertEqual(assault_activation_cost(9, rakdos_present=True),
                         {"generic_due": 3, "colored_due": {"R": 2}, "rakdos_applies": False})

    def test_capped_reduction_and_invalid_cases(self):
        self.assertEqual(payment("Loyal Subordinate", 9, rakdos_present=True)["discount"], 2)
        with self.assertRaises(ValueError):
            payment("Loyal Subordinate", -1, rakdos_present=True)
        with self.assertRaises(ValueError):
            payment("Neheb, the Eternal", 9, rakdos_present=True, commander_tax=2)

    def test_report_is_explicitly_non_decisional(self):
        r = report()
        self.assertTrue(r["no_measured_gameplay_or_challenger_superiority"])
        self.assertFalse(any(r["authority"].values()))


if __name__ == "__main__":
    unittest.main()
