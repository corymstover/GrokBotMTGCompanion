"""Final qualified Set Atlas release gate; no silent evidence upgrades."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_phase1b_functional_release as G


class QualifiedReleaseTests(unittest.TestCase):
    def test_replay_is_byte_exact_to_prior_published_evidence(self):
        self.assertEqual(G.OUTPUT.read_bytes(), G.encode(G.build()))

    def test_full_functional_scope_without_overclaiming(self):
        report = G.build()
        self.assertEqual(report["gate"], "QUALIFIED_OFFLINE_FUNCTIONAL_RELEASE_READY")
        coverage = report["verified_features"]
        self.assertEqual(coverage["all_set_codes_printings_and_unique_card_exports_pass"], 1062)
        self.assertEqual(coverage["historical_printing_ids_exactly_reverse_joined"], 119509)
        self.assertEqual(coverage["historical_stable_oracle_ids_reverse_joined"], 39099)
        self.assertEqual(coverage["released_english_paper_printing_rows"], 106855)
        self.assertEqual(coverage["curated_direct_wizards_story_series_links"], 12)
        self.assertEqual(sum(report["exclusive_set_code_scopes"].values()), 1062)
        self.assertEqual(report["optional_product_family_evidence"]["separately_preserved_source_pending_other_family_codes"], 555)
        self.assertFalse(report["optional_product_family_evidence"]["release_blocker"])

    def test_caveat_contract_is_explicit(self):
        caveats = " ".join(G.build()["release_limitations"]).lower()
        for phrase in ("exact id equality", "136", "555", "chronology", "repository-wide"):
            self.assertIn(phrase, caveats)
        self.assertNotIn("all time premier sets certified", G.build()["gate"].lower())


if __name__ == "__main__":
    unittest.main()
