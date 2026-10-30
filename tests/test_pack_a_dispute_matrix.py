import hashlib, importlib.util, json, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "data/lore_research/pack_a_genealogy_disputes_2026-10-30.json"
spec = importlib.util.spec_from_file_location("bdm", ROOT / "scripts/build_pack_a_dispute_matrix.py")
bdm = importlib.util.module_from_spec(spec); spec.loader.exec_module(bdm)


def cache_pages():
    import sys
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_card_lore_links as b
    try:
        return b.load_pages()
    except SystemExit:
        return None


class PackADisputeMatrixTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(ART.read_text())

    def test_status_and_owner_fields_blank(self):
        self.assertEqual(self.d["status"], "PRELIMINARY_RESEARCH_FOR_OWNER")
        for r in self.d["disputes"] + self.d["other_pack_a_disputed_claims"]:
            self.assertEqual(r["owner_decision"], "")

    def test_quotes_official_and_hashed(self):
        for r in self.d["disputes"]:
            self.assertGreaterEqual(len(r["evidence"]), 2, r["id"])
            for e in r["evidence"]:
                self.assertTrue(e["source_url"].startswith("https://magic.wizards.com/"))
                self.assertIn(e["voice"], {"EDITORIAL", "NARRATOR_UGIN", "NARRATOR_BOLAS", "STORY_NARRATION", "CHARACTER_DIALOGUE"})
                self.assertIn(e["stance"], {"SUPPORTS", "CONTESTS", "QUALIFIES", "CONTEXT"})
                self.assertEqual(hashlib.sha256(bdm.norm(e["quote"]).encode()).hexdigest(), e["quote_sha256"])

    def test_resolution_only_with_official_source(self):
        for r in self.d["disputes"]:
            res = r["official_resolution"]
            if res is None:
                self.assertTrue(r["unresolved_because"])
            else:
                pages = {e["page"] for e in r["evidence"] if e["voice"] in ("EDITORIAL", "STORY_NARRATION")}
                self.assertTrue(set(res["source_pages"]) <= pages, r["id"])

    def test_grades_match_packs_unchanged(self):
        ci = bdm.claims_index()
        for r in self.d["disputes"]:
            for c, rec in r["claim_records"].items():
                self.assertEqual(rec["grade"], ci[c]["grade"])
        for c in self.d["other_pack_a_disputed_claims"]:
            self.assertEqual(c["grade"], ci[c["id"]]["grade"])
            self.assertNotEqual(c["grade"], "CANON_CONFIRMED")

    def test_roster_conflict_recorded_open(self):
        gd3 = next(r for r in self.d["disputes"] if r["id"] == "GD3")
        self.assertIsNone(gd3["official_resolution"])
        self.assertEqual(set(gd3["claims"]), {"A003", "A018"})

    def test_markdown_in_sync(self):
        self.assertEqual(bdm.MD.read_text(), bdm.render_md(self.d))

    def test_rebuild_matches_cache(self):
        pages = cache_pages()
        if pages is None:
            self.skipTest("story cache not present")
        self.assertEqual(bdm.build(pages), self.d)
        chron = [p for p in pages.values() if "chronicle-bolas" in p["url"]]
        self.assertEqual(len(chron), 8)
        self.assertFalse(any("Ur-Dragon" in p["text"] for p in chron))


if __name__ == "__main__":
    unittest.main()
