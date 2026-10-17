"""I/J guard regression tests: positive receipt, adversarial mutation and authority failures."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_m6_ij as ij


class TestM6InputReceipt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        m5, summary, registry = ij.context()
        cls.original = ij.record(summary["decks"][0], registry[summary["decks"][0]["slug"]], m5, summary)

    def fresh(self):
        return json.loads(json.dumps(self.original))

    def test_complete_receipt(self):
        self.assertTrue(ij.validate_receipt(self.fresh()))
        self.assertFalse(self.original["authority"]["can_approve_or_lock"])
        self.assertFalse(self.original["reproduction"]["phase_b_replayed"])

    def test_forbid_false_shas(self):
        r = self.fresh()
        r["inputs"][0]["sha256"] = "sha256:" + "0" * 64
        with self.assertRaises(ValueError):
            ij.validate_receipt(r)

    def test_forbid_approval_claim(self):
        r = self.fresh()
        r["authority"]["can_approve_or_lock"] = True
        with self.assertRaises(ValueError):
            ij.validate_receipt(r)

    def test_forbid_positive_test_overclaim(self):
        r = self.fresh()
        r["reproduction"]["positive_simulator_verdicts_decisive"] = True
        with self.assertRaises(ValueError):
            ij.validate_receipt(r)

    def test_forbid_missing_roles(self):
        r = self.fresh()
        r["inputs"].pop()
        with self.assertRaises(ValueError):
            ij.validate_receipt(r)

    def test_forbid_unmet_gate_elision(self):
        r = self.fresh()
        r["required_next"].remove("phase_B_validated_evidence")
        with self.assertRaises(ValueError):
            ij.validate_receipt(r)

    def test_forbid_code_hash_drift(self):
        r = self.fresh()
        r["generator_sha256"] = "sha256:" + "0" * 64
        with self.assertRaises(ValueError):
            ij.validate_receipt(r)


if __name__ == "__main__":
    unittest.main()
