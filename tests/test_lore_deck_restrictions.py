"""Phase 6 release-era / chosen edition / true Oracle-debut filters."""
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import historical_set_lookup as H
import lore_deck_restrictions as R


class LoreDeckRestrictions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ring = next(c for c in H.card_query("Sol Ring")["cards"]
                        if c["oracle_id"] == "6ad8011d-3471-4369-9d68-b264cc027487")

    @staticmethod
    def card(identity, row):
        return {"name": "Sol Ring", "printing": {
            "oracle_id": identity, "id": row["printing_id"], "set": row["set"],
            "collector_number": row["collector_number"], "released_at": row["released_at"]}}

    def test_first_print_is_not_selected_reprint(self):
        entries = self.ring["printings"]
        self.assertEqual(entries[0]["set"], "lea")
        reprint = next(row for row in entries if row["set"] == "c21")
        c = self.card(self.ring["oracle_id"], reprint)
        ok = R.Restriction(chosen_sets=frozenset({"c21"}), first_sets=frozenset({"lea"}))
        self.assertEqual(R.check_printing(c, ok)["status"], "ALLOWED")
        bad = R.Restriction(first_sets=frozenset({"c21"}))
        self.assertEqual(R.check_printing(c, bad)["reasons"], ["FIRST_RECORDED_SET_NOT_ALLOWED"])
        wrong_edition = R.Restriction(chosen_sets=frozenset({"lea"}))
        self.assertEqual(R.check_printing(c, wrong_edition)["reasons"], ["SELECTED_SET_NOT_ALLOWED"])

    def test_real_world_publication_era_not_story_era(self):
        row = self.ring["printings"][0]
        card = self.card(self.ring["oracle_id"], row)
        self.assertEqual(R.check_printing(card, R.Restriction(release_from=date(1993, 1, 1),
                                                            release_through=date(1993, 12, 31)))["status"], "ALLOWED")
        self.assertEqual(R.check_printing(card, R.Restriction(release_from=date(2001, 1, 1)))["reasons"],
                         ["SELECTED_PRINTING_BEFORE_PUBLICATION_ERA"])

    def test_tied_debut_retains_multiple_sets(self):
        oid = "bbbbbbbb-0000-4000-8000-000000000001"
        rows = [["lea", "aaaaaaaa-0000-4000-8000-000000000001", oid, "Test", "1", "1993-08-05", "en", 1],
                ["leb", "aaaaaaaa-0000-4000-8000-000000000002", oid, "Test", "2", "1993-08-05", "en", 1],
                ["2ed", "aaaaaaaa-0000-4000-8000-000000000003", oid, "Test", "3", "1993-12-01", "en", 1],
                ["tmp", "aaaaaaaa-0000-4000-8000-000000000004", oid, "Test", "4", "2027-01-01", "en", 1],
                ["prm", "aaaaaaaa-0000-4000-8000-000000000005", oid, "Test", "5", "1990-01-01", "fr", 1],
                ["prm", "aaaaaaaa-0000-4000-8000-000000000006", oid, "Test", "6", "1990-01-01", "en", 0]]
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            (folder / "historical_cards_b.json").write_text(json.dumps({oid: rows}))
            card = {"name": "Test", "printing": {"oracle_id": oid, "id": rows[2][1], "set": "2ed",
                                                  "collector_number": "3", "released_at": "1993-12-01"}}
            rule = R.Restriction(first_sets=frozenset({"leb"}))
            result = R.check_printing(card, rule, folder)
            self.assertEqual(result["status"], "ALLOWED")
            self.assertEqual(result["first_recorded_sets"], ["lea", "leb"])

    def test_unknown_printing_and_mismatch_fail_closed(self):
        row = self.ring["printings"][0]
        card = self.card(self.ring["oracle_id"], row)
        rule = R.Restriction(chosen_sets=frozenset({"lea"}))
        card["printing"]["id"] = "ffffffff-ffff-4fff-8fff-ffffffffffff"
        self.assertEqual(R.check_printing(card, rule)["status"], "UNKNOWN")
        card["printing"]["id"] = row["printing_id"]
        card["printing"]["released_at"] = "1999-01-01"
        self.assertEqual(R.check_printing(card, rule)["reasons"], ["CHOSEN_PRINTING_METADATA_MISMATCH"])
        card["printing"]["oracle_id"] = None
        self.assertEqual(R.check_printing(card, rule)["reasons"], ["MISSING_STABLE_ORACLE_OR_PRINTING_ID"])

    def test_invalid_restriction_and_beyond_cutoff(self):
        for rule in (R.Restriction(), R.Restriction(chosen_sets=frozenset({"does-not-exist"})),
                     R.Restriction(release_from=date(2026, 10, 30), release_through=date(2000, 1, 1)),
                     R.Restriction(chosen_sets=frozenset({"lea"}), as_of=date(2027, 1, 1))):
            with self.assertRaises(ValueError):
                rule.validate()

    def test_cli_real_pilot_remains_unapproved(self):
        run = subprocess.run([sys.executable, "scripts/lore_deck_restrictions.py", "--stem",
                              "original_primeval_dragons", "--first-printed-in", "lea"],
                             cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        report = json.loads(run.stdout)
        self.assertEqual(sum(report["totals"].values()), 85)
        self.assertEqual(report["totals"]["UNKNOWN"], 0)
        self.assertGreater(report["totals"]["EXCLUDED"], 0)
        rejected = subprocess.run([sys.executable, "scripts/lore_deck_restrictions.py", "--stem",
                                   "original_primeval_dragons", "--first-printed-in", "lea", "--require-all"],
                                  cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(rejected.returncode, 1)


if __name__ == "__main__":
    unittest.main()
