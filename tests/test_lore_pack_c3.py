import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pack_c3 as C3  # noqa: E402
import audit_lore_pack_rtd as E  # noqa: E402


class AssaultOnNewPhyrexiaPackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pack = json.loads(C3.PACK.read_text(encoding="utf-8"))
        cls.audit = json.loads(C3.OUT.read_text(encoding="utf-8"))

    def test_research_status_only(self):
        self.assertTrue(self.pack["status"].startswith("PRELIMINARY_RESEARCH"))
        self.assertIn("not owner approved", self.pack["status"])

    def test_audit_clean(self):
        self.assertEqual(self.audit["problems"], [])
        self.assertEqual(self.audit["quotes_verbatim"], self.audit["quotes"])
        self.assertEqual(E.main(["--check"], C3.PACK, C3.OUT, C3.URL_RE, C3.SCHEMA), 0)

    def test_five_official_episodes_only(self):
        self.assertEqual(len(self.pack["source_register"]), 5)
        for meta in self.pack["source_register"].values():
            self.assertRegex(meta["url"], C3.URL_RE)
        for c in self.pack["claims"]:
            self.assertTrue(c["evidence"], c["id"])

    def test_no_death_or_fate_asserted_beyond_text(self):
        c = {x["id"]: x for x in self.pack["claims"]}
        self.assertEqual(c["ONE012"]["predicate"], "fought")
        self.assertIn("does not explicitly state that Tibalt died", c["ONE012"]["limitation"])
        self.assertIn("unknown", c["ONE014"]["limitation"])
        self.assertFalse(any(x["predicate"] in {"killed", "died"} for x in self.pack["claims"]))

    def test_claims_in_graph_with_era(self):
        g = json.loads((ROOT / "data/multiverse_graph/multiverse_graph.json").read_text(encoding="utf-8"))
        edges = [e for e in g["edges"] if str(e.get("claim", "")).startswith("ONE")]
        self.assertEqual({e["claim"] for e in edges}, {x["id"] for x in self.pack["claims"]})
        self.assertTrue(all(e.get("era") == "one_strike_2023" for e in edges))

    def test_mutation_non_wizards_source_caught(self):
        p = copy.deepcopy(self.pack)
        first = sorted(p["source_register"])[0]
        p["source_register"][first]["url"] = "https://example.com/fan-wiki/new-phyrexia"
        out, _ = E.audit(p, E.CACHE, C3.URL_RE, C3.PACK, C3.SCHEMA)
        self.assertTrue(any("not an allowed" in x for x in out["problems"]))


if __name__ == "__main__":
    unittest.main()
