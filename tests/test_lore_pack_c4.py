import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pack_c4 as C4  # noqa: E402
import audit_lore_pack_rtd as E  # noqa: E402


class MarchOfTheMachinePackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pack = json.loads(C4.PACK.read_text(encoding="utf-8"))
        cls.audit = json.loads(C4.OUT.read_text(encoding="utf-8"))
        cls.claims = {c["id"]: c for c in cls.pack["claims"]}

    def test_research_status_only(self):
        self.assertTrue(self.pack["status"].startswith("PRELIMINARY_RESEARCH"))
        self.assertIn("not owner approved", self.pack["status"])

    def test_audit_clean(self):
        self.assertEqual(self.audit["problems"], [])
        self.assertEqual(self.audit["quotes_verbatim"], self.audit["quotes"])
        self.assertGreaterEqual(self.audit["claims"], 20)
        self.assertEqual(E.main(["--check"], C4.PACK, C4.OUT, C4.URL_RE, C4.SCHEMA), 0)

    def test_ten_official_episodes_only(self):
        self.assertEqual(len(self.pack["source_register"]), 10)
        for meta in self.pack["source_register"].values():
            self.assertRegex(meta["url"], C4.URL_RE)
        # The allow-list is exact: another set's "episode-1-..." slug is rejected.
        self.assertIsNone(C4.URL_RE.match("https://magic.wizards.com/en/news/magic-story/episode-1-an-offer-of-revenge"))
        for c in self.pack["claims"]:
            self.assertTrue(c["evidence"], c["id"])

    def test_every_episode_cited(self):
        cited = {s for c in self.pack["claims"] for s in c["source_ids"]}
        self.assertEqual(cited, set(self.pack["source_register"]))

    def test_inferences_are_graded_and_limited(self):
        # Attributions the quotes do not state in one sentence stay CANON_IMPLIED with a limitation.
        for cid in ("MOM002", "MOM006", "MOM015", "MOM021"):
            self.assertEqual(self.claims[cid]["grade"], "CANON_IMPLIED", cid)
            self.assertTrue(self.claims[cid]["limitation"], cid)
        self.assertIn("Wrenn's death is not asserted", self.claims["MOM015"]["limitation"])
        self.assertFalse(any(c["predicate"] == "died" for c in self.pack["claims"]))

    def test_claims_in_graph_with_era(self):
        g = json.loads((ROOT / "data/multiverse_graph/multiverse_graph.json").read_text(encoding="utf-8"))
        edges = [e for e in g["edges"] if str(e.get("claim", "")).startswith("MOM")]
        self.assertEqual({e["claim"] for e in edges}, set(self.claims))
        self.assertTrue(all(e.get("era") == "mom_invasion_2023" for e in edges))
        ids = {n["id"] for n in g["nodes"]}
        # Shared entities merge with earlier packs rather than duplicating.
        for nid in ("character:elesh_norn", "character:karn", "place:zhalfir", "plane:zendikar"):
            self.assertIn(nid, ids)

    def test_mutation_non_wizards_source_caught(self):
        p = copy.deepcopy(self.pack)
        first = sorted(p["source_register"])[0]
        p["source_register"][first]["url"] = "https://example.com/fan-wiki/march-of-the-machine"
        out, _ = E.audit(p, E.CACHE, C4.URL_RE, C4.PACK, C4.SCHEMA)
        self.assertTrue(any("not an allowed" in x for x in out["problems"]))

    def test_mutation_altered_quote_caught_when_cache_present(self):
        p = copy.deepcopy(self.pack)
        p["claims"][0]["evidence"][0]["quote"] += " (paraphrase)"
        out, present = E.audit(p, E.CACHE, C4.URL_RE, C4.PACK, C4.SCHEMA)
        if not present:
            self.skipTest("official story cache absent (CI); hashes are checked by test_audit_clean")
        self.assertTrue(any("quote not found verbatim" in x for x in out["problems"]))


if __name__ == "__main__":
    unittest.main()
