"""Batch 4 (2026-10-30): extra official-story lore evidence for enrichment records.

- `named_on`: only for a record with no other lore evidence. The card's full front-face name (two or more words)
  appears case-sensitively in the prose of a cached Magic Story episode or Planeswalker's Guide.
- `art_on` from the Phase 1B caption atlas: only when the CSV captions give the card no art, and only with a matching artist.
The story cache is gitignored, so the prose checks are skipped when it is absent; the stored-data checks always run.
"""
import csv
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_card_enrichment as B  # noqa: E402

CARDS = json.loads((ROOT / "data" / "card_enrichment.json").read_text(encoding="utf-8"))["cards"]
EVIDENCE = ("relations", "spotlight", "flavor_on", "art_on", "presented_on")


class NamedOnTests(unittest.TestCase):
    def test_counts_floor(self):
        named = [v for v in CARDS.values() if v["lore"].get("named_on")]
        self.assertGreaterEqual(len(named), 120)
        self.assertEqual(len(CARDS), 5362)

    def test_named_on_is_fallback_only_and_story_urls(self):
        for v in CARDS.values():
            lo = v["lore"]
            if not lo.get("named_on"):
                continue
            self.assertFalse(any(lo.get(f) for f in EVIDENCE) or lo.get("note"), v["name"])
            self.assertLessEqual(len(lo["named_on"]), 3)
            fr = B.front(v["name"])
            self.assertGreaterEqual(len(fr.split()), 2, v["name"])
            self.assertNotIn(fr, B.NAMED_ON_REJECT)
            for t, u in lo["named_on"]:
                self.assertRegex(u, B.STORY_URL, v["name"])
            self.assertIn("Named verbatim in official story text", v["lines"][0])
            self.assertNotIn(B.NO_LORE, v["lines"][0])

    def test_reject_list(self):
        self.assertEqual(B.named_on("The Thing"), [])
        self.assertEqual(B.named_on("Dungeon Master"), [])
        self.assertEqual(B.named_on("Yargle"), [])  # one word: never

    def test_story_url_filter(self):
        ok = ["https://magic.wizards.com/en/news/magic-story/favor-2017-07-05",
              "https://magic.wizards.com/en/news/feature/planeswalkers-guide-to-the-lost-caverns-of-ixalan",
              "https://magic.wizards.com/en/news/feature/a-planeswalkers-guide-to-zendikar"]
        no = ["https://magic.wizards.com/en/news/announcements/a-first-look-at-outlaws-of-thunder-junction",
              "https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19"]
        for u in ok:
            self.assertRegex(u, B.STORY_URL)
        for u in no:
            self.assertNotRegex(u, B.STORY_URL)

    @unittest.skipUnless(any((ROOT / ".cache" / "story" / "text22").glob("*.txt")) if (ROOT / ".cache" / "story" / "text22").exists() else False,
                         "story cache absent (gitignored)")
    def test_prose_contains_name(self):
        prose = B.story_prose()
        for v in CARDS.values():
            for t, u in v["lore"].get("named_on", []):
                fr = B.front(v["name"]).replace("\u2019", "'")
                self.assertRegex(prose[u][1], r"(?<![\w-])" + re.escape(fr) + r"(?![\w-])", v["name"])


class AtlasArtTests(unittest.TestCase):
    def test_atlas_art_is_documented_and_artist_matched(self):
        csv_urls = {}
        for r in csv.DictReader((ROOT / "data" / "story_art_captions.csv").open(encoding="utf-8")):
            csv_urls.setdefault(r["caption_name"], set()).add(r["url"])
        atlas = B.atlas_captions()
        n_atlas = 0
        for v in CARDS.values():
            for t, u in v["lore"].get("art_on", []):
                names = {v["name"], B.front(v["name"])}
                if any(u in csv_urls.get(n, ()) for n in names):
                    continue
                n_atlas += 1
                self.assertTrue(any(u == x[1] for n in names for x in atlas.get(n, [])), (v["name"], u))
        self.assertGreaterEqual(n_atlas, 20)

    def test_atlas_pages_official(self):
        for v in B.atlas_captions().values():
            for t, u, a in v:
                self.assertTrue(u.startswith("https://magic.wizards.com/en/"))
                self.assertTrue(a)


if __name__ == "__main__":
    unittest.main()
