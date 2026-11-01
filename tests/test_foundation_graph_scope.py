"""Bounded owner review retains genuine uncertainties and fails closed on stale provenance."""
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_foundation_graph_scope as S  # noqa: E402


class FoundationGraphScopeTests(unittest.TestCase):
    def test_exact_source_graded_review_is_reproducible(self):
        saved = json.loads(S.OUT.read_text(encoding="utf-8"))
        self.assertEqual(saved, S.build())
        self.assertEqual(saved["foundational_claims"], 78)
        self.assertEqual(saved["claims_by_pack"], {"a": 32, "b": 18, "c": 28})
        self.assertEqual(saved["conservative_genealogy_decisions"], S.EXPECTED_DECISIONS)
        self.assertFalse(saved["overall_foundation_certified"])
        self.assertTrue(any("decimation" in x for x in saved["out_of_scope"]))

    def test_dispute_resolution_cannot_promote_unproven_parentage(self):
        real = S.j
        def changed(path):
            value = real(path)
            if path == S.DISPOSITIONS:
                value = dict(value, dispositions=[dict(x) for x in value["dispositions"]])
                value["dispositions"][1]["decision"] = "UR_DRAGON_PARENT_CONFIRMED"
            return value
        with patch.object(S, "j", side_effect=changed):
            with self.assertRaisesRegex(ValueError, "conservative genealogy decisions"):
                S.build()


if __name__ == "__main__":
    unittest.main()
