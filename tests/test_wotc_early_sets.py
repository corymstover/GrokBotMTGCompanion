"""Offline regression tests for the Wizards-backed 1993–2002 release census."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_wotc_early_sets as E


class EarlySetsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = json.loads(E.SOURCE.read_text(encoding="utf-8"))
        cls.atlas = json.loads(E.ATLAS.read_text(encoding="utf-8"))
        cls.previous = json.loads(E.PREVIOUS.read_text(encoding="utf-8"))

    def test_count_reconciles_without_claiming_all_time_premier_total(self):
        audit = E.build(self.sources, self.atlas, self.previous)
        self.assertEqual(audit["period_candidate_count"], 38)
        self.assertEqual(audit["period_reviewed_regular_mainline"], 35)
        self.assertEqual(audit["period_confirmed_not_independent_mainline"], 1)
        self.assertEqual(audit["period_provisional_variants"], 2)
        c = audit["combined_full_snapshot"]
        self.assertEqual(c["candidate_expansion_core_total"], 142)
        self.assertEqual(c["reviewed_mainline_1993_2002_plus_2023_2026"], 56)
        self.assertEqual(c["directly_documented_auxiliary_or_discarded"], 3)
        self.assertEqual(c["not_yet_reviewed_2003_2022"], 81)
        self.assertEqual(c["candidate_unresolved_including_two_provisionals"], 83)
        self.assertFalse(c["all_time_mainline_total_certified"])

    def test_unresolved_foreign_border_and_summer_magic_exception(self):
        result = {x["code"]: x for x in E.build(self.sources, self.atlas, self.previous)["records"]}
        for code in ("fbb", "4bb"):
            self.assertEqual(result[code]["review_status"], "provisional_structural_inference")
            self.assertFalse(result[code]["included_in_historical_regular_release_count"])
        self.assertEqual(result["sum"]["classification"], "discarded_print_run")
        self.assertEqual(result["sum"]["review_status"], "explicit_Wizards_exclusion")
        for code in ("lea", "leb", "2ed", "arn", "ice", "ons"):
            self.assertTrue(result[code]["included_in_historical_regular_release_count"])

    def test_missing_duplicate_and_inferred_sources_fail(self):
        source = copy.deepcopy(self.sources)
        source["records"].append(copy.deepcopy(source["records"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            E.build(source, self.atlas, self.previous)
        source = copy.deepcopy(self.sources)
        source["records"][0]["source"] = "https://example.com/unofficial"
        with self.assertRaisesRegex(ValueError, "Unverified source"):
            E.build(source, self.atlas, self.previous)
        source = copy.deepcopy(self.sources)
        foreign = next(x for x in source["records"] if x["code"] == "fbb")
        foreign["claim"] = "historical_regular_expansion_or_core_release"
        with self.assertRaisesRegex(ValueError, "Unconfirmed mainline"):
            E.build(source, self.atlas, self.previous)

    def test_deterministic_bytes(self):
        once = E.encode(E.build(self.sources, self.atlas, self.previous))
        twice = E.encode(E.build(self.sources, self.atlas, self.previous))
        self.assertEqual(once, twice)


if __name__ == "__main__":
    unittest.main()
