import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pack_a5 as A5  # noqa: E402
import audit_lore_pack_rtd as E  # noqa: E402


class UginAlliesPackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pack = json.loads(A5.PACK.read_text(encoding="utf-8"))
        cls.audit = json.loads(A5.OUT.read_text(encoding="utf-8"))

    def test_research_status_only(self):
        self.assertTrue(self.pack["status"].startswith("PRELIMINARY_RESEARCH"))
        self.assertIn("not owner approved", self.pack["status"])

    def test_audit_clean(self):
        self.assertEqual(self.audit["problems"], [])
        self.assertEqual(self.audit["quotes_verbatim"], self.audit["quotes"])
        self.assertEqual(E.main(["--check"], A5.PACK, A5.OUT, A5.URL_RE, A5.SCHEMA), 0)

    def test_every_claim_quoted_from_official_story(self):
        for c in self.pack["claims"]:
            self.assertTrue(c["evidence"], c["id"])
        for meta in self.pack["source_register"].values():
            self.assertRegex(meta["url"], A5.URL_RE)

    def test_inferred_claim_not_upgraded(self):
        g = {c["id"]: c["grade"] for c in self.pack["claims"]}
        self.assertEqual(g["U016"], "CANON_IMPLIED")

    def test_mutation_non_wizards_source_caught(self):
        p = copy.deepcopy(self.pack)
        first = sorted(p["source_register"])[0]
        p["source_register"][first]["url"] = "https://example.com/fan-wiki/ugin"
        out, _ = E.audit(p, E.CACHE, A5.URL_RE, A5.PACK, A5.SCHEMA)
        self.assertTrue(any("not an allowed" in x for x in out["problems"]))


if __name__ == "__main__":
    unittest.main()
