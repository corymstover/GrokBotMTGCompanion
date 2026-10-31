"""Tentative card/art identity links never become canon through a name match."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_unresolved_lore_links as A  # noqa: E402


class UnresolvedLoreLinksTests(unittest.TestCase):
    def test_all_pending_links_and_art_mismatches_are_accounted_for(self):
        pending = A.pending()
        self.assertEqual(len(pending), 341)
        self.assertEqual(len({x["oracle_id"] for x in pending}), 209)
        art = A.art_unresolved()
        self.assertEqual(len(art), 7)
        self.assertEqual(sum(x["status"] == "NAME_MISMATCH" for x in art), 6)
        self.assertTrue(all(r["reason"] and r["source_url"].startswith("https://magic.wizards.com/") for r in art))

    def test_frozen_source_review_quarantines_all_tentative_links(self):
        report = A.check_saved()
        self.assertEqual(report["totals"]["pending_name_matches"], 341)
        self.assertEqual(report["totals"]["name_matches_by_status"],
                         {"EVIDENCE_LEAD_REVIEW_ONLY": 2, "UNRESOLVED_NAME_ONLY": 339})
        self.assertEqual(report["totals"]["candidate_evidence_types"], {"none": 339, "page": 2})
        self.assertTrue(all(row["canon_promotion"] is False for row in report["name_matches"]))
        self.assertFalse(report["approval_or_canon_changes"])

    def test_portable_check_rejects_silent_promotion(self):
        report = json.loads(A.OUT.read_text(encoding="utf-8"))
        report["name_matches"][0]["canon_promotion"] = True
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "tampered.json"
            target.write_text(json.dumps(report), encoding="utf-8")
            with patch.object(A, "OUT", target):
                with self.assertRaisesRegex(ValueError, "promotes tentative claims"):
                    A.check_saved()


if __name__ == "__main__":
    unittest.main()
