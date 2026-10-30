"""Core Phase 1B readiness checks without promoting the 555 optional source reviews."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_phase1b_fasttrack as A


class Phase1BFasttrackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs = [json.loads(path.read_text(encoding="utf-8"))
                      for path in (A.CURRENT, A.CURRENT_AUDIT, A.HISTORICAL,
                                   A.CATEGORY, A.PRODUCT, A.FAMILY)]

    def build(self, overrides=None, lookups=False):
        args = copy.deepcopy(self.inputs)
        if overrides:
            for index, replacement in overrides.items():
                args[index] = replacement
        return A.build(*args, run_lookups=lookups)

    def test_released_english_paper_counts_match_for_all_1062_codes(self):
        report = self.build()
        self.assertEqual(report["all_codes"], 1062)
        self.assertEqual(report["released_english_paper_as_of_cutoff"], 106855)
        self.assertEqual(report["released_english_paper_per_set_count_disagreements"], [])
        self.assertEqual(report["net_printing_delta"], 192)
        self.assertEqual(report["net_english_paper_delta"], 198)
        self.assertEqual(report["historical_future_english_paper"], 845)
        self.assertEqual(report["current_future_english_paper"], 1043)
        self.assertEqual(set(report["changed_set_counts"]), set(A.EXPECTED_DELTAS))

    def test_all_32_published_indexes_and_representative_live_queries(self):
        report = self.build(lookups=True)
        self.assertEqual(report["published_index_files_hash_verified"], 32)
        self.assertEqual([x["code"] for x in report["smoke_queries"]], list(A.SMOKE_CODES))
        self.assertEqual(report["fasttrack_gate_status"]["nine_representative_set_lookups_and_black_lotus"], "PASS")
        self.assertFalse(report["source_provenance"]["current_october29_bulk_reverified_now"])
        self.assertEqual(report["fasttrack_gate_status"]["exact_cross_snapshot_printing_ID_parity"],
                         "UNVERIFIED_requires_source_bytes_or_identified_delta")

    def test_555_source_reviews_remain_optional_and_metadata_joins_still_pass(self):
        report = self.build()
        self.assertEqual(report["scryfall_product_metadata_codes_joined"], 1062)
        self.assertEqual(report["explicit_scryfall_parent_set_links"], 560)
        self.assertEqual(report["non_blocking_other_category_family_research_pending"], 555)
        self.assertEqual(sum(report["exclusive_status_partitions"].values()), 1062)
        self.assertEqual(report["source_backed_other_category_families"], 293)

    def test_detects_released_date_drift_metadata_conflict_and_wrong_hash(self):
        current = copy.deepcopy(self.inputs[0])
        current["sets"]["lea"]["released_english_paper"] -= 1
        with self.assertRaisesRegex(ValueError, "Released per-set count differences"):
            self.build({0: current})
        products = copy.deepcopy(self.inputs[4]); products["warnings"] = ["new unmatched set"]
        with self.assertRaisesRegex(ValueError, "Unresolved product-set joins"):
            self.build({4: products})
        historical = copy.deepcopy(self.inputs[2]); historical["generated_file_sha256"]["historical_cards_0.json"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "Historical published index was modified"):
            self.build({2: historical})

    def test_report_is_byte_exact_reproducible(self):
        self.assertEqual(A.OUTPUT.read_bytes(), A.serialize(self.build(lookups=True)))


if __name__ == "__main__":
    unittest.main()
