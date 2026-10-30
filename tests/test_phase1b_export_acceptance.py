"""Full 1,062-set English printing/unique-card export readiness and filter policy."""
import csv
import io
import json
import sys
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_phase1b_export_acceptance as A
from export_phase1b_set_cards import export_set, format_export
from historical_set_lookup import card_query


class Phase1BExportAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs = [json.loads(path.read_text(encoding="utf-8"))
                      for path in (A.HIST, A.FAST, A.CURRENT)]

    def test_all_1062_sets_and_all_119509_printings_reverse_joined(self):
        report = json.loads(A.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(report["all_set_codes_full_export_checked"], 1062)
        self.assertEqual(report["historical_printing_ids_reverse_joined"], 119509)
        self.assertEqual(report["stable_oracle_ids_reverse_joined"], 39099)
        self.assertEqual(report["released_english_paper_printing_rows_exported"], 106855)
        self.assertEqual(report["set_codes_with_zero_default_released_paper_rows"], 105)
        self.assertEqual(report["all_1062_printing_and_unique_card_exports"], "PASS")

    def test_full_alpha_printings_and_unique_identity_csv_exports(self):
        prints = export_set("lea", mode="printings")
        unique = export_set("lea", mode="unique")
        self.assertEqual(prints["printing_records"], 295)
        self.assertEqual(len(prints["rows"]), 295)
        self.assertEqual(unique["distinct_identities_or_unresolved"], 290)
        self.assertEqual(sum(r["printings_in_set"] for r in unique["rows"]), 295)
        self.assertEqual(len(list(csv.DictReader(io.StringIO(format_export(prints, "csv"))))), 295)
        self.assertEqual(len(list(csv.DictReader(io.StringIO(format_export(unique, "csv"))))), 290)
        self.assertEqual(len(json.loads(format_export(prints, "json"))["rows"]), 295)
        lotus = next(r for r in unique["rows"] if r["name"] == "Black Lotus")
        self.assertEqual(lotus["debut_classification"], "debut")
        self.assertEqual(lotus["first_printing_in_set"], "1993-08-05")
        chronology = card_query("Black Lotus")
        self.assertEqual(chronology["matched_identities"], 1)
        self.assertEqual(chronology["cards"][0]["printings"][0]["set"], "lea")

    def test_future_digital_and_foreign_filters_require_opt_in(self):
        for code in ("trk", "ydmu", "fbb"):
            self.assertEqual(export_set(code)["printing_records"], 0)
        self.assertEqual(export_set("trk", future=True)["printing_records"], 481)
        self.assertEqual(export_set("ydmu", digital=True)["printing_records"], 39)
        self.assertEqual(export_set("fbb", foreign=True)["printing_records"], 307)
        self.assertEqual(export_set("lea", cutoff=date(1993, 8, 4))["printing_records"], 0)
        with self.assertRaises(KeyError):
            export_set("nonexistent-set-code")
        with self.assertRaises(ValueError):
            export_set("lea", mode="not-an-export-mode")

    def test_report_byte_exact_recomputed_from_committed_indexes(self):
        self.assertEqual(A.OUTPUT.read_bytes(), A.encode(A.build(*self.inputs)))


if __name__ == "__main__":
    unittest.main()
