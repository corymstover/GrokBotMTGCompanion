"""Batch 14: pack-cited official pages cached for chronology checks (metadata only in git)."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROV = ROOT / "data/lore_research/pack_source_cache_provenance_2026-10-30.json"
CHRONO = ROOT / "data/lore_research/relative_chronology_2026-10-30.json"
ALLOWED = {"url", "slug", "status", "title", "date", "words", "text_sha256", "cited_by", "error"}


class PackSourceCacheTest(unittest.TestCase):
    def setUp(self):
        self.prov = json.loads(PROV.read_text())

    def test_metadata_only_no_page_bodies(self):
        for p in self.prov["pages"]:
            self.assertLessEqual(set(p), ALLOWED, p.get("slug"))

    def test_official_wizards_urls_only(self):
        for p in self.prov["pages"]:
            self.assertTrue(p["url"].startswith("https://magic.wizards.com/"), p["url"])

    def test_all_pages_cached_and_cited(self):
        self.assertGreaterEqual(len(self.prov["pages"]), 10)
        for p in self.prov["pages"]:
            self.assertEqual(p["status"], "CACHED", p["slug"])
            self.assertTrue(p["cited_by"])

    def test_no_page_bodies_tracked(self):
        self.assertFalse((ROOT / "data/lore_research/sources").exists())

    def test_chronology_uses_new_pages_and_summaries(self):
        d = json.loads(CHRONO.read_text())
        urls = {e["source_url"].rstrip("/").split("/")[-1] for e in d["stated_edges"]}
        for slug in ("reforged-chain-2015-01-21", "the-brothers-war", "known-mutliverse-2008-03-19"):
            self.assertIn(slug, urls)
        # quotes stay short (no bulk page or novel text)
        for e in d["stated_edges"]:
            if e["quote"]:
                self.assertLess(len(e["quote"].split()), 45, e["quote"][:60])


if __name__ == "__main__":
    unittest.main()
