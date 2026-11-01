"""Bounded Phase 6 engine acceptance without deck approvals or live legality claims."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pilot as A
import audit_phase6_engine_scope as S
import lore_deck_candidates as C


class Phase6EngineScopeTests(unittest.TestCase):
    def test_grades_all_four_curator_tiers_and_source_provenance(self):
        name = "ugin_bolas_elder_dragon_duality"
        all_cards = C.retrieve(name)
        self.assertEqual(all_cards["count"], 83)
        self.assertTrue(all_cards["status"].startswith("UNAPPROVED"))
        self.assertEqual({grade: C.retrieve(name, grade)["count"] for grade in A.TIERS},
                         {"DIRECT_DEPICTION": 6, "CANON_REFERENCE": 54,
                          "LORE_INSPIRED": 8, "MECHANICAL_SYMBOL": 15})
        self.assertTrue(all(row["source"] and row["printing_id"] and row["oracle_id"]
                            for row in all_cards["cards"]))
        self.assertEqual(C.retrieve(name, name="Nicol")["count"] > 0, True)
        with self.assertRaises(ValueError):
            C.retrieve(name, "CANON_BUT_UNVERIFIED")
        with self.assertRaises(ValueError):
            C.retrieve("nonexistent_pilot")

    def test_archidekt_import_audit_catches_middle_row_tampering(self):
        specpath = next(A.SPECS.glob("pilot2_*.json"))
        spec = json.loads(specpath.read_text(encoding="utf-8"))
        real = A.files(spec)
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "tampered_archidekt_import.txt"
            rows = real["archidekt_import.txt"].read_text(encoding="utf-8").splitlines()
            rows[10] = "1x Incorrect Card"
            bad.write_text("\n".join(rows) + "\n", encoding="utf-8")
            fake = {**real, "archidekt_import.txt": bad}
            with mock.patch.object(A, "files", return_value=fake):
                with self.assertRaisesRegex(ValueError, "match every decklist"):
                    A.audit(specpath)

    def test_frozen_report_replays_and_preserves_approvals(self):
        expected = json.loads(S.OUT.read_text(encoding="utf-8"))
        live = S.build()
        self.assertEqual(live, expected)
        self.assertEqual(len(live["pilots"]), 3)
        self.assertTrue(all(row["pilot_approval_flags_all_false"] for row in live["pilots"]))
        self.assertTrue(all(row["first_printed_in_lea_example"]["UNKNOWN"] == 0
                            for row in live["pilots"]))
        self.assertTrue(all(row["status"].startswith("UNAPPROVED") for row in live["pilots"]))


if __name__ == "__main__":
    unittest.main()
