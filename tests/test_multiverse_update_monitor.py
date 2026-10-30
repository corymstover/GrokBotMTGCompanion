"""Deterministic fixtures for the read-only, source-safe Phase 8 update monitor."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import monitor_multiverse_updates as m


class SourceMonitorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline, cls.snapshot = m.baseline_data()

    def test_official_index_links_and_new_story_candidates(self):
        html = ('<a href="/en/news/magic-story/brand-new-chapter">Story</a>'
                '<a href="https://not-wizards.example/en/news/magic-story/fake">Fake</a>')
        result = m.story_signals(html, self.baseline["story_index_url"], m.known_story_urls(self.baseline))
        self.assertEqual(result["new_story_url_candidates"],
                         ["https://magic.wizards.com/en/news/magic-story/brand-new-chapter"])
        self.assertEqual(result["current_index_links"], 1)

    def test_existing_story_url_does_not_trigger(self):
        url = "https://magic.wizards.com/en/news/magic-story/reality-fracture-episode-10-happy-birthday"
        result = m.story_signals(f'<a href="{url}">Story</a>', self.baseline["story_index_url"],
                                 m.known_story_urls(self.baseline))
        self.assertEqual(result["new_story_url_candidates"], [])

    def test_scryfall_bulks_are_compared_by_real_timestamps(self):
        data = {"data": [{"type": "default_cards", "updated_at": "2026-10-30T09:05:46+00:00"},
                         {"type": "oracle_cards", "updated_at": "2026-10-29T09:02:02.225+00:00"},
                         {"type": "rulings", "updated_at": "invalid"}]}
        result = m.scryfall_signals(data, self.snapshot)
        self.assertEqual(result["default-cards"]["status"], "NEWER_BULK_AVAILABLE_REVIEW_FIRST")
        self.assertEqual(result["oracle-cards"]["status"], "NOT_NEWER")
        self.assertEqual(result["rulings"]["status"], "UNVERIFIABLE_METADATA")

    def test_rules_documents_not_dynamic_page_etag_are_alerts(self):
        rules = "<a href=\"https://media.wizards.com/2026/downloads/MagicCompRules 20261110.pdf\">new</a>"
        def fake(url, *, head=False):
            if url == self.baseline["story_index_url"]:
                return "", None
            if url == self.baseline["scryfall_bulk_metadata_url"]:
                return json.dumps({"data": []}), None
            return (rules if url.endswith("/rules") else "", "totally-different-etag")
        report = m.live_report(self.baseline, self.snapshot, fake)
        self.assertEqual(report["requires_review"],
                         ["https://media.wizards.com/2026/downloads/MagicCompRules 20261110.pdf"])
        self.assertEqual(report["sources"]["wizards_rules_pages"][1]["status"],
                         "ETAG_DIFFERENT_INFORMATIONAL_ONLY")

    def test_outage_preserves_unavailable_instead_of_fake_no_changes(self):
        def fails(url, *, head=False):
            raise OSError("offline")
        report = m.live_report(self.baseline, self.snapshot, fails)
        self.assertEqual(report["sources"]["official_stories"]["status"], "SOURCE_UNAVAILABLE")
        self.assertEqual(report["sources"]["scryfall"]["status"], "SOURCE_UNAVAILABLE")
        self.assertEqual(report["requires_review"], [])

    def test_active_snapshot_is_hash_pinned_and_owner_gates_untouched(self):
        self.assertEqual(self.snapshot["snapshot_id"], "snap-20261029-40848334824-1")
        self.assertEqual(len(self.snapshot["files"]["default-cards"]["sha256"]), 64)
        self.assertIn("Never auto-ingest", self.baseline["policy"])


if __name__ == "__main__":
    unittest.main()
