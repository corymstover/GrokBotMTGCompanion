"""Current-source lookup review cannot hide a source change or new CR uncertainty."""
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lookup_rules_scope as S  # noqa: E402
import release_readiness as R  # noqa: E402


class LookupRulesScopeTests(unittest.TestCase):
    def test_exact_saved_review_and_fail_closed_meld_behavior(self):
        saved = json.loads(S.OUT.read_text(encoding="utf-8"))
        self.assertEqual(saved, S.build())
        self.assertEqual(saved["indexed_oracle_ids_reconciled"], 33894)
        self.assertEqual(saved["indexed_november_oracle_text_or_identity_differences"], 0)
        self.assertEqual(saved["post_bulletin_rulebreaker_and_meld_current_verdict"],
                         "UNKNOWN_UNTIL_OFFICIAL_TEXT_RECONCILED")
        self.assertFalse(saved["full_foundation_release_certified"])
        self.assertEqual(R.c_lookup()[0], "MET")

    def test_new_indexed_oracle_text_drift_invalidates_scope(self):
        real = S.read
        def changed(rel):
            obj = real(rel)
            if rel.endswith("oct30_to_nov01_2200_release_delta_2026-11-01.json"):
                obj = dict(obj, delta={**obj["delta"], "oracle-cards": {
                    **obj["delta"]["oracle-cards"], "existing_ids_with_tracked_field_changes": 8}})
            return obj
        with patch.object(S, "read", side_effect=changed):
            with self.assertRaisesRegex(ValueError, "unreviewed current-source change"):
                S.build()

    def test_scope_review_removal_reverts_gate_to_partial(self):
        real = R._json
        with patch.object(R, "_json", side_effect=lambda rel: None if rel ==
                               "data/release/lookup_rules_scope_review_2026-11-01.json" else real(rel)):
            self.assertEqual(R.c_lookup()[0], "PARTIAL")


if __name__ == "__main__":
    unittest.main()
