"""Evidence-conservative Phase 1B all-set classifications and story bridges."""
import csv
import json
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_phase1b_release_scope as A


class ReleaseScopeAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads(A.OUTPUT.read_text(encoding="utf-8"))

    def test_complete_exclusive_1062_category_counts(self):
        counts = Counter(r["scope_label"] for r in self.report["set_scope_records"].values())
        self.assertEqual(len(self.report["set_scope_records"]), 1062)
        self.assertEqual(dict(counts), self.report["scope_counts_exclusive"])
        self.assertEqual([counts[c] for c in (
            "historical_regular_mainline", "documented_auxiliary_or_discarded",
            "localized_variant_provisional", "released_paper_other_category",
            "released_digital_only", "future_announced")], [136, 4, 2, 848, 62, 10])
        self.assertFalse(self.report["all_time_premier_set_count_certified"])

    def test_uncertainties_and_supplemental_codes_not_elevated(self):
        items = self.report["set_scope_records"]
        self.assertEqual(items["lea"]["scope_label"], "historical_regular_mainline")
        for code in ("mat", "big", "sum", "tsb"):
            self.assertEqual(items[code]["scope_label"], "documented_auxiliary_or_discarded")
        for code in ("fbb", "4bb"):
            self.assertEqual(items[code]["scope_label"], "localized_variant_provisional")
            self.assertIsNone(items[code]["wizards_release_source"])
        for code in ("c21", "40k", "brr"):
            self.assertEqual(items[code]["scope_label"], "released_paper_other_category")
        self.assertEqual(items["ydmu"]["scope_label"], "released_digital_only")
        self.assertEqual(items["trk"]["scope_label"], "future_announced")

    def test_twelve_curated_first_party_story_series_with_exact_titles(self):
        links = self.report["wizards_story_series_set_links"]
        self.assertEqual(set(links), set(A.STORY_SERIES))
        with A.STORIES.open(encoding="utf-8", newline="") as f:
            indexed = {(r["title"], r["url"]) for r in csv.DictReader(f)}
        for code, link in links.items():
            self.assertGreaterEqual(link["official_story_count_in_recovered_index"], 2)
            for item in link["sample_first_party_story_sources"]:
                self.assertIn((item["title"], item["url"]), indexed)
                self.assertTrue(item["title"].startswith(A.STORY_SERIES[code] + " | "))
                self.assertTrue(item["url"].startswith("https://magic.wizards.com/"))
        self.assertEqual(links["bro"]["official_story_count_in_recovered_index"], 10)
        self.assertEqual(links["mom"]["official_story_count_in_recovered_index"], 18)
        self.assertNotIn("pip", links)

    def test_full_report_replays_byte_exactly_from_frozen_sources(self):
        self.assertEqual(A.OUTPUT.read_bytes(), A.encode(A.build()))


if __name__ == "__main__":
    unittest.main()
