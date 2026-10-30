import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pack_rtd as A  # noqa: E402


class RtdPackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pack = json.loads(A.PACK.read_text(encoding="utf-8"))
        cls.audit = json.loads(A.OUT.read_text(encoding="utf-8"))

    def test_status_is_research_not_approval(self):
        s = self.pack["status"]
        self.assertIn("PRELIMINARY_RESEARCH", s)
        for word in ("APPROVED", "LOCKED", "CERTIFIED"):
            self.assertNotIn(word, s.replace("not owner approved", "").replace("not certified", ""))

    def test_twelve_official_episodes(self):
        reg = self.pack["source_register"]
        self.assertEqual(len(reg), 12)
        for meta in reg.values():
            self.assertRegex(meta["url"], A.URL_RE)

    def test_committed_audit_clean_and_hashed(self):
        self.assertEqual(self.audit["problems"], [])
        self.assertEqual(self.audit["quotes_verbatim"], self.audit["quotes"])
        self.assertEqual(self.audit["claims"], len(self.pack["claims"]))
        self.assertEqual(A.main(["--check"]), 0)

    def test_disputed_claims_kept_disputed(self):
        g = {c["id"]: c["grade"] for c in self.pack["claims"]}
        for cid in ("RTD006", "RTD021", "RTD033"):
            self.assertEqual(g[cid], "CANON_DISPUTED")

    def test_mutation_unregistered_source_caught(self):
        p = copy.deepcopy(self.pack)
        p["claims"][0]["source_ids"].append("not_a_source")
        out, _ = A.audit(p)
        self.assertTrue(any("unregistered source" in x for x in out["problems"]))

    def test_mutation_bad_grade_caught(self):
        p = copy.deepcopy(self.pack)
        p["claims"][0]["grade"] = "APPROVED"
        out, _ = A.audit(p)
        self.assertTrue(any("unknown grade" in x for x in out["problems"]))

    def test_mutation_altered_quote_changes_hash(self):
        p = copy.deepcopy(self.pack)
        p["claims"][0]["evidence"][0]["quote"] += " (invented)"
        out, cache_present = A.audit(p)
        self.assertNotEqual(out["quote_rows"][0]["quote_sha256"], self.audit["quote_rows"][0]["quote_sha256"])
        if cache_present:
            self.assertTrue(any("quote not found" in x for x in out["problems"]))


if __name__ == "__main__":
    unittest.main()
