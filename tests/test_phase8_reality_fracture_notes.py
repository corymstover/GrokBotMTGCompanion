"""Static, read-only checks for the bounded Phase 8 official-story note batch.

These notes are curated inputs, NOT a claim that generated card enrichment,
card shards, or the Phase 8 coverage counter have been updated yet.
"""

import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
STORY_URL = "https://magic.wizards.com/en/news/magic-story/the-legends-of-reality-fracture"
NEW_NOTES = {
    "Denzilore Fatehold", "Ingris Stingerquill", "Aerid Konstrari",
    "Kwia Vigorbloom", "Fblthp, Impossibly Lost", "Fblthp, Knows the Way",
    "Gallia, the Merrymaker", "Gallia, Tragic Host", "Ghalta the Unstoppable",
    "Marwyn, the Preserver", "Marwyn, the Clearcutter", "Yuriko, Blade of the Mighty",
}
ECHOVERSE_NOTES = {
    "Denzilore Fatehold", "Ingris Stingerquill", "Aerid Konstrari",
    "Kwia Vigorbloom", "Fblthp, Knows the Way", "Gallia, Tragic Host",
    "Marwyn, the Clearcutter", "Yuriko, Blade of the Mighty",
}


class RealityFractureLoreNotesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.notes = json.loads((ROOT / "data/card_lore_notes.json").read_text(encoding="utf-8"))

    def test_official_story_is_a_registered_primary_source(self):
        with (ROOT / "data/primary_sources.csv").open(encoding="utf-8", newline="") as f:
            sources = {r["url"] for r in csv.DictReader(f)}
        self.assertIn(STORY_URL, sources)

    def test_all_twelve_notes_match_exact_indexed_card_names(self):
        with (ROOT / "data/card_index.csv").open(encoding="utf-8", newline="") as f:
            cards = {r["name"] for r in csv.DictReader(f)}
        self.assertEqual(len(NEW_NOTES), 12)
        self.assertTrue(NEW_NOTES.issubset(cards))
        self.assertTrue(NEW_NOTES.issubset(self.notes))
        for name in NEW_NOTES:
            with self.subTest(name=name):
                note = self.notes[name]
                self.assertEqual(note["relation"], "depicts")
                self.assertEqual(note["sources"], [STORY_URL])
                self.assertTrue(note["text"].strip())
                # No verbatim passage is claimed without the original story cache.
                self.assertNotIn('"', note["text"])

    def test_echoverse_versions_are_explicitly_labeled(self):
        self.assertEqual(len(ECHOVERSE_NOTES), 8)
        for name in NEW_NOTES:
            note = self.notes[name]
            with self.subTest(name=name):
                if name in ECHOVERSE_NOTES:
                    self.assertTrue(note["text"].startswith("Echoverse continuity:"))
                    self.assertEqual(note.get("flag"), "⚠️")
                else:
                    self.assertNotIn("Echoverse continuity:", note["text"])
                    self.assertNotIn("flag", note)


if __name__ == "__main__":
    unittest.main()
