"""Tests for scripts/release_readiness.py: it reads committed evidence and never claims approval."""
import json
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import release_readiness as R  # noqa: E402

STATUSES = {"MET", "PARTIAL", "NOT_MET", "EXTERNAL"}


class ReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = R.readiness()

    def test_every_written_criterion_is_evaluated(self):
        self.assertEqual(len(self.r["criteria"]), 7)
        self.assertTrue(all(c["status"] in STATUSES and c["note"] for c in self.r["criteria"]))
        ids = {c["id"] for c in self.r["criteria"]}
        self.assertIn("knowledge_foundation", ids)
        self.assertNotIn("reviewed_graph_deck", ids)

    def test_never_claims_approval_or_certification(self):
        forbidden = {"APPROVED", "LOCKED", "CERTIFIED", "CANONICAL_LOCKED"}
        self.assertNotIn(self.r["verdict"], forbidden)
        self.assertIn(self.r["verdict"], {"NOT_RELEASE_READY", "READY_FOR_OWNER_REVIEW"})
        self.assertTrue(all(c["status"] not in forbidden for c in self.r["criteria"]))
        self.assertIn("Never an approval", self.r["note"])

    def test_verdict_not_ready_while_anything_partial(self):
        if self.r["tally"]["PARTIAL"] or self.r["tally"]["NOT_MET"]:
            self.assertEqual(self.r["verdict"], "NOT_RELEASE_READY")

    def test_enrichment_counts_come_from_artifact(self):
        c = next(c for c in self.r["criteria"] if c["id"] == "priority_enrichment")
        ev = c["evidence"]
        self.assertEqual(ev["enriched"] + ev["remaining"], ev["total"])
        if ev["remaining"]:
            self.assertEqual(c["status"], "PARTIAL")

    def test_preliminary_packs_cannot_be_met(self):
        c = next(c for c in self.r["criteria"] if c["id"] == "foundation_graph")
        if any("PRELIMINARY" in s for s in c["evidence"].get("pack_statuses", [])):
            self.assertNotEqual(c["status"], "MET")

    def test_missing_pack_is_not_met(self):
        real = R._json

        def fake(rel):
            d = real(rel)
            if rel == "data/multiverse_graph/manifest.json":
                d = dict(d, claim_packs=[p for p in d["claim_packs"] if "pack_c_" not in p])
            return d
        with mock.patch.object(R, "_json", side_effect=fake):
            self.assertEqual(R.c_graph()[0], "NOT_MET")

    def test_protected_digests_are_read_only_hashes(self):
        c = next(c for c in self.r["criteria"] if c["id"] == "grixis_no_regression")
        d = c["evidence"]["protected_path_digests"]
        self.assertIn("state/current_deck_overrides.json", d)
        self.assertTrue(all(v["sha256"] is None or len(v["sha256"]) == 64 for v in d.values()))

    def test_foundation_gate_does_not_require_lore_deck_approval(self):
        c = next(c for c in self.r["criteria"] if c["id"] == "knowledge_foundation")
        self.assertIs(c["evidence"]["deck_pilots_required"], False)
        self.assertNotIn("deck approval", c["note"].lower())

    def test_foundation_acceptance_requires_explicit_scope_and_three_reviews(self):
        review = {"status": "OWNER_ACCEPTED", "scope": "KNOWLEDGE_FOUNDATION_ONLY",
                  "chronology_reviewed": True, "history_coverage_reviewed": True,
                  "qa_regressions_passed": True}
        real = R._json
        with mock.patch.object(R, "_json", side_effect=lambda rel: review if rel ==
                               "data/release/knowledge_foundation_acceptance.json" else real(rel)):
            self.assertEqual(R.c_knowledge_foundation()[0], "MET")
        review["qa_regressions_passed"] = False
        with mock.patch.object(R, "_json", side_effect=lambda rel: review if rel ==
                               "data/release/knowledge_foundation_acceptance.json" else real(rel)):
            self.assertEqual(R.c_knowledge_foundation()[0], "PARTIAL")


if __name__ == "__main__":
    unittest.main()
