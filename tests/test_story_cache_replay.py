"""Official source recovery is reproducible, but does not certify changed canon."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import replay_story_cache_provenance as R  # noqa: E402


class StoryCacheReplayTests(unittest.TestCase):
    def test_original_source_inventory_has_exactly_660_distinct_urls(self):
        saved, provenance = R.base()
        self.assertEqual(provenance["inventory_total"], 660)
        self.assertEqual(len(saved), 660)
        self.assertTrue(all(item["status"] == "present" for item in saved.values()))

    def test_replay_detects_and_quarantines_changed_extractions(self):
        saved, _ = R.base()
        records = [dict(v) for v in saved.values()]
        drift = records[0]
        drift["sha256"] = "a" * 64 if drift["sha256"] != "a" * 64 else "b" * 64
        drift["words"] += 7
        with patch.object(R.A, "audit", return_value={"total": 660, "counts": {"present": 660},
                                                     "colliding_cache_paths": [], "records": records}):
            replay = R.full_replay()
        self.assertEqual(replay["exact_original_extraction_hashes"], 659)
        self.assertEqual(replay["source_extract_drift"], 1)
        self.assertEqual(replay["drift_review_queue"][0]["status"], "EXTRACT_DRIFT_REVIEW_ONLY")
        self.assertFalse(replay["source_text_embedded"])

    def test_replay_rejects_incomplete_or_corrupt_cache(self):
        with patch.object(R.A, "audit", return_value={"total": 660, "counts": {"present": 659, "missing": 1},
                                                     "colliding_cache_paths": [], "records": []}):
            with self.assertRaisesRegex(ValueError, "incomplete"):
                R.full_replay()

    def test_committed_recovery_report_is_consistent_without_local_cache(self):
        if not R.OUT.is_file():
            self.skipTest("recovery report generated only after all 660 pages are recovered")
        report = R.portable_check()
        self.assertEqual(report["exact_original_extraction_hashes"] + report["source_extract_drift"], 660)


if __name__ == "__main__":
    unittest.main()
