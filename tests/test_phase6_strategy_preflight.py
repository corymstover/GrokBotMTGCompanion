"""Fail-closed strategy evidence tests; never mutate preserved pilot proposals."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_phase6_strategy_preflight as audit


class Phase6StrategyPreflightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec = json.loads(audit.SPEC.read_text(encoding="utf-8"))

    def assert_rejected(self, alter, message):
        spec = copy.deepcopy(self.spec)
        alter(spec)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "strategy.json"
            path.write_text(json.dumps(spec), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, message):
                audit.build(path)

    def test_all_three_dated_curves_and_role_packs(self):
        result = audit.build()
        self.assertEqual(result["status"], "PRELIMINARY_MECHANICAL_STRATEGIES_K108_OPEN")
        self.assertEqual(len(result["pilots"]), 3)
        self.assertEqual({x["stem"]: x["mana_curve"]["lands_including_basics"]
                          for x in result["pilots"]}, {
            "ugin_bolas_elder_dragon_duality": 35,
            "original_primeval_dragons": 37,
            "ugins_allies_and_heroes": 36,
        })
        for pilot in result["pilots"]:
            curve = pilot["mana_curve"]
            self.assertEqual(curve["lands_including_basics"] + curve["nonlands_including_commander"], 100)
            self.assertTrue(pilot["status"].startswith("UNAPPROVED"))
            self.assertTrue(pilot["approval_flags_all_false"])
            self.assertEqual(set(pilot["verified_oracle_anchors"]), set(audit.ROLES))
            self.assertTrue(all(len(x) >= 2 for x in pilot["verified_oracle_anchors"].values()))
            self.assertIn("UNTESTED", pilot["power_hypothesis"])

    def test_invented_oracle_ability_cannot_prove_strategy(self):
        self.assert_rejected(lambda s: s["pilots"][0]["anchors"]["PAYOFF"][1].update(
            oracle_contains="Win the game as soon as Bolas enters"), "unproven PAYOFF Oracle anchor")

    def test_flavor_text_cannot_prove_a_mechanical_role(self):
        # This is printed as Bolas lore but does not appear in Oracle text.
        self.assert_rejected(lambda s: s["pilots"][0]["anchors"]["ACCELERATION"][0].update(
            oracle_contains="Dominaria's most ancient evil"), "unproven ACCELERATION Oracle anchor")

    def test_not_in_pilot_is_rejected_even_if_real_card(self):
        self.assert_rejected(lambda s: s["pilots"][0]["anchors"]["INTERACTION"][0].update(
            name="Swords to Plowshares"), "invalid or missing pilot anchor")

    def test_required_functional_role_cannot_be_omitted(self):
        self.assert_rejected(lambda s: s["pilots"][1]["anchors"].pop("INTERACTION"),
                             "every strategy needs all four")

    def test_unsupported_power_certificate_is_rejected(self):
        self.assert_rejected(lambda s: s["pilots"][2].update(power_hypothesis="BRACKET_5_CERTIFIED"),
                             "unjustifiably definitive")

    def test_spec_cannot_omit_pilot(self):
        self.assert_rejected(lambda s: s["pilots"].pop(), "exactly the three existing pilots")

    def test_check_detects_stale_artifact(self):
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder) / "review.json"
            dest.write_text("{}\n", encoding="utf-8")
            with patch.object(audit, "OUT", dest):
                with self.assertRaisesRegex(ValueError, "stale"):
                    audit.main(["--check"])


if __name__ == "__main__":
    unittest.main()
