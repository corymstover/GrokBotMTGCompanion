import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from lore_query import card_printings, story_candidates, timeline_view


TIMELINE = """## A. In-universe eras
### Dated events (AR)
| Year | Event | Source |
|---|---|---|
| **4562 AR** | Frame story | [BRO](https://magic.wizards.com/en/news/magic-story/bro) |
| 28 AR | Siege | [BRO](https://magic.wizards.com/en/news/magic-story/bro2) |
### Post-Mending (Gatewatch era)
Ordered by story publication (⚠️ assumed in-world order).
| # | Arc | Event |
|---|---|---|
| 1 | First | Intro |
| 4a | Variant | Alters past |
### Phyrexian Invasion
| Order | Phase | Source |
|---|---|---|
| 1 | DMU | [Story](https://magic.wizards.com/en/news/magic-story/one) |
### Omenpath era (post-invasion)
| Relative marker (quoted) | Arc | Source |
|---|---|---|
| unplaced ⚠️ | Edge | [Story](https://magic.wizards.com/en/news/magic-story/two) |
| after TDM | Lorwyn | [Story](https://magic.wizards.com/en/news/magic-story/three) |
"""


class LoreQueryTests(unittest.TestCase):
    def test_ar_years_are_sorted_and_cited(self):
        result = timeline_view(TIMELINE, "ar")
        self.assertTrue(result["chronological"])
        self.assertEqual([r["verified_date"] for r in result["rows"]], [28, 4562])
        self.assertIn("https://magic.wizards.com/en/news/magic-story/bro2", result["rows"][0]["official_sources_on_row"])

    def test_publication_and_relative_markers_not_faked_as_absolute_dates(self):
        post = timeline_view(TIMELINE, "postmending")
        omen = timeline_view(TIMELINE, "omenpaths")
        self.assertFalse(post["chronological"])
        self.assertEqual([x["marker"] for x in post["rows"]], ["1", "4a"])
        self.assertFalse(omen["chronological"])
        self.assertEqual(omen["rows"][0]["marker"], "unplaced ⚠️")

    def test_card_editions_preserve_flavor_variants(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / "manifest.json").write_text(json.dumps({"source": "fixture", "coverage": "english",
                "shards": {"a-000.jsonl": {}}}), encoding="utf-8")
            with (p / "a-000.jsonl").open("w", encoding="utf-8") as fh:
                for i, phrase in enumerate(["Urza made it.", "Urza found it."]):
                    fh.write(json.dumps({"n": "Urza's Tome", "s": "atq", "c": str(i),
                        "l": "en", "p": 1, "faces": [{"n": "Urza's Tome", "f": phrase}]}) + "\n")
            result = card_printings("Urza's Tome", p, limit=1)
            self.assertEqual(result["printings"], 2)
            self.assertEqual(result["distinct_flavor_texts"], 2)
            self.assertEqual(result["shown"], 1)

    def test_candidates_retain_evidence_ranks(self):
        data = {"items": [{"name": "Karn", "page": "Characters Index.md", "anchor": "karn",
            "links": {"cards": ["cards/K/kar.md#karn"]}, "enriched_cards": ["Karn, Scion of Urza"]}]}
        evidence = {"printing_text": {"printings": [{"card": "Mysterious Artifact", "set": "atq",
            "collector_number": "2", "source_url": "https://scryfall.com/card/atq/2"}]}}
        result = story_candidates("Karn", data, evidence)
        self.assertEqual([x["rank"] for x in result["candidates"]], [1, 2, 3])
        self.assertIn("not a deck", result["warning"])


if __name__ == "__main__":
    unittest.main()
