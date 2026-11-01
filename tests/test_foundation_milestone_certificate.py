"""A foundation certificate must retain source limits, immutable evidence and 7 gates."""
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_foundation_milestone_certificate as C


class CertificateTests(unittest.TestCase):
    def test_exact_bounded_certificate(self):
        d = C.check()
        self.assertEqual(len(d["foundation_gates"]), 7)
        self.assertIn("NOT all MTG canon", d["scope"])
        self.assertEqual(len(d["external_verification"]["candidate_pr_workflows"]["run_ids"]), 14)
        self.assertEqual(len(d["external_verification"]["merged_main_workflows"]["run_ids"]), 10)

    def test_missing_workflow_result_invalidates_certificate(self):
        original = json.loads(C.CERT.read_text())
        compromised = json.loads(json.dumps(original))
        compromised["external_verification"]["merged_main_workflows"]["run_ids"].pop()
        with patch.object(C, "CERT", Mock(read_text=lambda **kw: json.dumps(compromised))):
            with self.assertRaises(AssertionError):
                C.check()


if __name__ == "__main__":
    unittest.main()
