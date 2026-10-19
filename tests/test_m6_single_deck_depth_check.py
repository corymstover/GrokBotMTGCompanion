"""Sequential M6 deep-review guards at any legitimate completion count.

These tests must not assume the initial 0/62 seed after the first real
source-bound review completes. The zero baseline is an explicit test fixture.
"""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_m6_single_deck_depth_check as check


class SequentialDepth(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tracker = check.load(check.LEDGER)
        cls.registry = check.load(check.REG)

    def clone(self):
        return copy.deepcopy(self.tracker)

    def zero_state(self):
        """Build an intentionally empty 62-deck queue for tampering tests."""
        x = self.clone()
        for d in x["decks"]:
            d["status"] = "PENDING"
            d["deep_review_evidence_path"] = None
            d["completed_at_commit"] = None
            d["ci_run_url"] = None
            d["blocker"] = None
        p = x["process"]
        p["deep_review_complete_count"] = 0
        p["active_tracker_deck_id"] = None
        p["next_tracker_deck_id"] = x["decks"][0]["tracker_deck_id"]
        p["ready_for_grokbot_pass_c"] = False
        return x

    def test_exact_62_verified_order_and_live_progress(self):
        self.assertEqual(len(self.tracker["decks"]), 62)
        expected = sum(d["status"] == "DEEP_REVIEW_COMPLETE" for d in self.tracker["decks"])
        self.assertEqual(check.validate(self.tracker, self.registry), expected)
        self.assertEqual(self.tracker["process"]["deep_review_complete_count"], expected)
        self.assertEqual(self.tracker["authority"]["historical_m6_4_authored_source_reviews"], 62)

    def test_valid_zero_state_fixture(self):
        self.assertEqual(check.validate(self.zero_state(), self.registry), 0)

    def test_no_false_source_coverage_promotion(self):
        x = self.clone()
        x["process"]["deep_review_complete_count"] = 62 if x["process"]["deep_review_complete_count"] != 62 else 0
        with self.assertRaises(AssertionError):
            check.validate(x, self.registry)

    def test_cannot_skip_deck_before_completing_first(self):
        x = self.zero_state()
        x["decks"][1]["status"] = "IN_PROGRESS"
        x["process"]["active_tracker_deck_id"] = x["decks"][1]["tracker_deck_id"]
        with self.assertRaises(AssertionError):
            check.validate(x, self.registry)

    def test_missing_evidence_cannot_complete_first_deck(self):
        x = self.zero_state()
        x["decks"][0]["status"] = "DEEP_REVIEW_COMPLETE"
        x["process"]["deep_review_complete_count"] = 1
        x["process"]["next_tracker_deck_id"] = x["decks"][1]["tracker_deck_id"]
        with self.assertRaises(AssertionError):
            check.validate(x, self.registry)

    def test_completed_entry_must_retain_source_evidence(self):
        x = self.clone()
        done = next((d for d in x["decks"] if d["status"] == "DEEP_REVIEW_COMPLETE"), None)
        if done is None:
            self.skipTest("No completed source-bound review in this snapshot")
        done["deep_review_evidence_path"] = None
        with self.assertRaises(AssertionError):
            check.validate(x, self.registry)

    def test_completed_entry_requires_real_ci_url(self):
        x = self.clone()
        done = next((d for d in x["decks"] if d["status"] == "DEEP_REVIEW_COMPLETE"), None)
        if done is None:
            self.skipTest("No completed source-bound review in this snapshot")
        done["ci_run_url"] = "https://example.invalid/fake"
        with self.assertRaises(AssertionError):
            check.validate(x, self.registry)

    def test_completed_entry_requires_exact_commit_sha(self):
        x = self.clone()
        done = next((d for d in x["decks"] if d["status"] == "DEEP_REVIEW_COMPLETE"), None)
        if done is None:
            self.skipTest("No completed source-bound review in this snapshot")
        done["completed_at_commit"] = "unverified"
        with self.assertRaises(AssertionError):
            check.validate(x, self.registry)

    def test_hidden_canonical_hash_tampering_rejected(self):
        x = self.clone()
        x["decks"][0]["baseline_approved_sha256"] = "0" * 64
        with self.assertRaises(AssertionError):
            check.validate(x, self.registry)

    def test_goben_norman_conflict_cannot_be_silently_marked_alias_none(self):
        x = self.clone()
        target = next(d for d in x["decks"] if d["canonical_deck_id"] == "Goben__Gene_Splice_Savant")
        target["source_identity_discrepancy"] = "NONE"
        with self.assertRaises(AssertionError):
            check.validate(x, self.registry)

    def test_canonical_swap_permission_mutation_rejected(self):
        x = self.clone()
        x["authority"]["canonical_deck_changes_allowed"] = True
        with self.assertRaises(AssertionError):
            check.validate(x, self.registry)

    def test_in_progress_requires_same_first_deck(self):
        x = self.zero_state()
        x["decks"][0]["status"] = "IN_PROGRESS"
        x["process"]["active_tracker_deck_id"] = "Abaddon_the_Despoiler"
        self.assertEqual(check.validate(x, self.registry), 0)

    def test_blocked_requires_reason(self):
        x = self.zero_state()
        x["decks"][0]["status"] = "BLOCKED"
        x["process"]["active_tracker_deck_id"] = "Abaddon_the_Despoiler"
        with self.assertRaises(AssertionError):
            check.validate(x, self.registry)

    def test_bad_next_tracker_pointer_rejected(self):
        x = self.zero_state()
        x["process"]["next_tracker_deck_id"] = x["decks"][1]["tracker_deck_id"]
        with self.assertRaises(AssertionError):
            check.validate(x, self.registry)


if __name__ == "__main__":
    unittest.main()
