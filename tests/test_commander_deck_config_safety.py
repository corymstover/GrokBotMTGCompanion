"""Adversarial Commander-Q&A tests using synthetic, non-canonical card records.

These tests run without the large card shards, and prove the answer envelope
does not certify a deck just because its colors fit an invalid commander.
"""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import commander_rules as cr  # noqa: E402
import mv_ask  # noqa: E402


def fixture(name, *, front_type="Legendary Creature", subtypes=(), identity="",
            legality="legal", partner=False):
    return {
        "name": name, "type_line": front_type, "front_type": front_type,
        "subtypes": list(subtypes), "identity": identity, "legality": legality,
        "abilities": {"partner": partner, "partner_with": set(), "partner_text": set(),
                      "background": False, "doctors_companion": False},
        "can_be_commander_text": False, "unmodelled": False, "pt": "2/2",
        "shard": "synthetic/card-shard#fixture",
    }


RECORDS = {
    "Sol Ring": fixture("Sol Ring", front_type="Artifact"),
    "Krark": fixture("Krark", identity="R", partner=True),
    "Sakashima": fixture("Sakashima", identity="U", partner=True),
    "Griselbrand": fixture("Griselbrand", identity="B", legality="banned"),
    "Llanowar Elves": fixture("Llanowar Elves", front_type="Creature", identity="G"),
}


class CommanderConfigurationSafety(unittest.TestCase):
    def setUp(self):
        # The record itself stands in for a parsed card shard, keeping every
        # test independent from downloaded Scryfall bulk or protected decks.
        self.resolve = patch.object(cr, "resolve", side_effect=RECORDS.get)
        self.facts = patch.object(cr, "facts", side_effect=lambda row: row)
        self.resolve.start()
        self.facts.start()
        self.addCleanup(self.resolve.stop)
        self.addCleanup(self.facts.stop)

    def test_single_commander_or_pair_must_be_eligible(self):
        for commanders in (["Griselbrand"], ["Llanowar Elves"], ["Krark", "Griselbrand"],
                           ["Krark", "Llanowar Elves"]):
            with self.subTest(commanders=commanders):
                out = cr.include("Sol Ring", commanders)
                self.assertFalse(out["result"]["allowed"])
                self.assertFalse(out["result"]["commander_configuration"]["allowed"])
                self.assertIn("INVALID_COMMANDER_CONFIGURATION", out["flags"])
                self.assertTrue(any("commander configuration" in r for r in out["result"]["reasons"]))
                self.assertEqual(out["confidence"], "QUALIFIED")

    def test_valid_commander_and_partner_pair_remain_usable(self):
        for commanders in (["Krark"], ["Krark", "Sakashima"]):
            with self.subTest(commanders=commanders):
                out = cr.include("Sol Ring", commanders)
                self.assertTrue(out["result"]["allowed"])
                self.assertTrue(out["result"]["commander_configuration"]["allowed"])
                self.assertNotIn("INVALID_COMMANDER_CONFIGURATION", out["flags"])
                self.assertIn(cr.HISTORICAL_LEGALITY_FLAG, out["flags"])
                self.assertEqual(out["confidence"], "QUALIFIED")
                self.assertEqual(out["card_data_as_of"], "2026-10-15")
                self.assertIn("Confirm current Oracle text", out["limitation"])

    def test_no_synthetic_configuration_is_automatically_live_verified(self):
        out = cr.commander(["Krark"])
        self.assertTrue(out["result"]["allowed"])
        self.assertEqual(out["confidence"], "QUALIFIED")
        self.assertIn(cr.HISTORICAL_LEGALITY_FLAG, out["flags"])
        routed = mv_ask.ask("Can Krark be my commander?")
        self.assertEqual(routed["route"], "ask->rules:single")
        self.assertEqual(routed["confidence"], "QUALIFIED")
        invalid = mv_ask.ask("Can Sol Ring go in a Griselbrand deck?")
        self.assertEqual(invalid["route"], "ask->rules:include")
        self.assertFalse(invalid["result"]["allowed"])
        self.assertIn("INVALID_COMMANDER_CONFIGURATION", invalid["flags"])

    def test_missing_or_excessive_commanders_do_not_produce_false_yes(self):
        for names in ([], ["Krark", "Sakashima", "Griselbrand"]):
            out = cr.include("Sol Ring", names)
            self.assertEqual(out["confidence"], "NOT_FOUND")
            self.assertIn("INVALID_COMMANDER_COUNT", out["flags"])
        self.assertEqual(cr.include("Sol Ring", ["Unknown"])["confidence"], "NOT_FOUND")


if __name__ == "__main__":
    unittest.main()
