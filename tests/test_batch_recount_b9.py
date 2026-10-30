"""Batch 9: per-batch recount and representative-query regression (Phase 1 line 65, Phase 7 line 279)."""
import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
os.environ.setdefault("MTG_SCRYFALL_MODE", "multiverse")
os.environ.setdefault("SCRYFALL_OFFLINE", "1")
import batch_recount  # noqa: E402
import mv_ask  # noqa: E402


class BatchRecount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rep = batch_recount.run()

    def test_every_representative_query_passes(self):
        bad = [q for q in self.rep["queries"] if not q["ok"]]
        self.assertEqual(bad, [])

    def test_recount_matches_inventory(self):
        c = self.rep["coverage"]
        self.assertEqual(c["pages"], 626)
        self.assertLessEqual(c["cited_pages"], c["pages"])
        self.assertEqual(self.rep["graph"]["stats"]["node_types"]["Claim"], c["claims"])
        self.assertEqual(self.rep["untagged"]["arc"], "(untagged)")


class EraAwareLeadership(unittest.TestCase):
    """A later-published page set in Tarkir's past must not be reported as the most recent leader."""

    def lead(self, q):
        env = mv_ask.ask(q)
        return env, env["result"]["leadership"]

    def test_past_era_khans_are_era_context(self):
        for q, present, past in [("Who leads the Temur?", "character:surrak", "character:yasova_dragonclaw"),
                                 ("Who leads the Sultai?", "character:sidisi", "character:tasigur"),
                                 ("Who leads the Mardu?", "character:zurgo", "character:alesha"),
                                 ("Who leads the Abzan?", "character:anafenza", "character:daghatar")]:
            env, lead = self.lead(q)
            self.assertEqual(lead["most_recent_cited"]["node"], present, q)
            self.assertIn("ERA_OR_TIMELINE_CONTEXT", env["flags"], q)
            self.assertIn("era_note", lead)
            row = next(x for x in lead["timeline"] if x["node"] == past)
            self.assertTrue(row["described_as_past_era"], q)

    def test_unlabelled_leaders_keep_publication_order(self):
        env, lead = self.lead("Who leads the Orzhov?")
        self.assertNotIn("ERA_OR_TIMELINE_CONTEXT", env["flags"])
        self.assertNotIn("era_note", lead)


if __name__ == "__main__":
    unittest.main()
