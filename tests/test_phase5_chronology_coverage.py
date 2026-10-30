"""Hard boundaries for partial historical order, plane inventory and pilot states."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import query_lore_chronology as q
import build_plane_history_priorities as coverage


class Phase5HistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chron = json.loads(q.DATA.read_text(encoding="utf-8"))

    def test_full_closure_and_primary_source_digests(self):
        self.assertEqual(q.check(self.chron)["result"], "PASS")

    def test_official_ancient_order(self):
        r = q.compare(self.chron, "A:elder_dragon_war", "A:primeval_rule")
        self.assertEqual(r["result"], "BEFORE")
        self.assertIn("magic.wizards.com", r["proof"][0]["source_url"])

    def test_printed_ar_dates_are_traced_back_to_stories(self):
        r = q.compare(self.chron, "B:kroog_siege", "B:trench_war")
        self.assertEqual(r["result"], "BEFORE")
        self.assertEqual({e["value"] for e in r["printed_ar_sources"]}, {"28", "44"})
        self.assertTrue(all(e["source_url"].startswith("https://magic.wizards.com/")
                            for e in r["printed_ar_sources"]))

    def test_unknown_not_reclassified_as_after_or_same(self):
        r = q.compare(self.chron, "C:josu_undead", "A:eldrazi_imprisoned")
        self.assertEqual(r["result"], "UNKNOWN")
        self.assertEqual(r["proof"], [])
        self.assertIn("UNKNOWN", r["limitation"])

    def test_original_tarkir_timeline_warns_about_continuity(self):
        r = q.compare(self.chron, "A:tarkir_duel", "A:tarkir_dragons_die_out")
        self.assertEqual(r["result"], "BEFORE")
        self.assertTrue(any("Original" in e.get("note", "") for e in r["proof"]))

    def test_unrecognized_event_does_not_become_evidence(self):
        with self.assertRaisesRegex(ValueError, "unknown chronology ID"):
            q.compare(self.chron, "fictional:unverified", "A:elder_dragon_war")

    def test_plane_report_and_all_three_unapproved_pilots(self):
        result = coverage.build()
        self.assertEqual(result["status"], "PRELIMINARY_RESEARCH")
        self.assertEqual(result["registered_planes"], 33)
        self.assertEqual(len(result["phase6_pilots"]), 3)
        self.assertTrue(all(p["status"] == "UNAPPROVED" for p in result["phase6_pilots"]))
        self.assertEqual(result["chronology"]["unresolved_pairs"], 2897)
        self.assertEqual(result["chronology"]["l244_complete"], False)


if __name__ == "__main__":
    unittest.main()
