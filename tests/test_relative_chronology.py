import hashlib, importlib.util, json, re, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "data/lore_research/relative_chronology_2026-10-30.json"
spec = importlib.util.spec_from_file_location("brc", ROOT / "scripts/build_relative_chronology.py")
brc = importlib.util.module_from_spec(spec); spec.loader.exec_module(brc)


class RelativeChronologyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(ART.read_text())
        cls.nodes = {n["id"]: n for n in cls.d["nodes"]}

    def test_status_and_l244_not_closed(self):
        self.assertEqual(self.d["status"], "PRELIMINARY_RESEARCH")
        self.assertFalse(self.d["l244_closure"]["closes_l244"])
        self.assertGreaterEqual(len(self.d["l244_closure"]["missing"]), 5)

    def test_acyclic(self):
        self.assertEqual(self.d["cycles"], [])
        for n, later in self.d["precedes"].items():
            self.assertNotIn(n, later)

    def test_stated_edges_cite_verbatim_official_quotes(self):
        for e in self.d["stated_edges"]:
            self.assertTrue(e["source_url"].startswith("https://magic.wizards.com/"), e)
            self.assertTrue(e["quote"])
            self.assertEqual(hashlib.sha256(brc.norm(e["quote"]).encode()).hexdigest(), e["quote_sha256"])

    def test_no_invented_years(self):
        for n in self.d["nodes"]:
            if n["kind"] != "PRINTED_AR_LABEL":
                self.assertNotIn("ar", n)
                self.assertIsNone(re.search(r"\b\d{2,5} AR\b", n["label"]), n)
        ar_edges = {e["later"]: e for e in self.d["stated_edges"] if e["kind"] == "PRINTED_AR"}
        for n in self.d["nodes"]:
            if n["kind"] == "PRINTED_AR_LABEL":
                self.assertIn(n["id"], ar_edges)  # every AR label comes from a printed header
                self.assertEqual(str(n["ar"]), ar_edges[n["id"]]["value"])
        for e in self.d["derived_edges"]:
            self.assertEqual(e["kind"], "DERIVED_FROM_PRINTED_AR")
            self.assertLess(self.nodes[e["earlier"]]["ar"], self.nodes[e["later"]]["ar"])

    def test_story_presents_never_merged(self):
        for e in self.d["stated_edges"]:
            self.assertFalse(e["earlier"].startswith("P:") and e["later"].startswith("P:"), e)
        for e in self.d["stated_edges"]:
            if e["kind"] == "SPAN_BEFORE_PRESENT":
                self.assertEqual(self.nodes[e["later"]]["kind"], "STORY_PRESENT")
                self.assertIn(e["value"].split()[-1].lower().strip("."), e["quote"].lower() + " years ago")

    def test_before_edges_in_closure(self):
        alias = {e["earlier"]: e["later"] for e in self.d["stated_edges"] if e["relation"] == "SAME_TIME_AS_LABEL"}
        for e in self.d["stated_edges"] + self.d["derived_edges"]:
            if e["relation"] == "BEFORE":
                a, b = alias.get(e["earlier"], e["earlier"]), alias.get(e["later"], e["later"])
                self.assertIn(b, self.d["precedes"][a])

    def test_claim_refs_exist(self):
        claims = brc.pack_claims()
        for n in self.d["nodes"]:
            for c in n.get("claims", []):
                self.assertIn(c["id"], claims)
                self.assertEqual(claims[c["id"]][2], c["grade"])

    def test_rebuild_matches_when_cache_present(self):
        try:
            pages = brc.load_pages()
        except SystemExit:
            self.skipTest("story cache absent")
        self.assertEqual(brc.build(pages), self.d)


if __name__ == "__main__":
    unittest.main()
