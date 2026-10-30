"""First-party lore research pack A provenance and canon boundaries."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pack_a as A


class PackATests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(A.EVIDENCE.read_text(encoding="utf-8"))

    def test_exact_replay_and_complete_source_register(self):
        report = A.build()
        self.assertEqual(A.OUTPUT.read_bytes(), A.encode(report))
        self.assertEqual(report["claims_checked"], 12)
        self.assertEqual(report["entities_checked"], 13)
        self.assertEqual(report["first_party_source_urls_checked"], 10)
        self.assertEqual(report["result"], "STRUCTURAL_PRIMARY_SOURCE_BOUNDARY_PASS")

    def test_source_ids_and_claims_are_reviewable(self):
        claims = self.data["claims"]
        self.assertEqual(len({c["id"] for c in claims}), 12)
        for claim in claims:
            self.assertTrue(claim["summary"])
            self.assertTrue(claim["limitation"])
            self.assertTrue(claim["source_ids"])
            self.assertTrue(all(k in self.data["source_register"] for k in claim["source_ids"]))

    def test_continuity_and_narrator_caveats_preserved(self):
        claims = {c["id"]: c for c in self.data["claims"]}
        self.assertEqual(claims["A003"]["grade"], "CANON_DISPUTED")
        self.assertEqual(claims["A004"]["grade"], "CANON_DISPUTED")
        self.assertEqual(claims["A011"]["grade"], "OPEN_QUESTION")
        self.assertEqual(claims["A012"]["grade"], "ALTERNATE_CONTINUITY")
        self.assertNotEqual(claims["A005"]["continuity"], claims["A006"]["continuity"])
        self.assertNotIn("depicted_by", {c["predicate"] for c in self.data["claims"]})

    def test_wizards_source_host_boundary(self):
        self.assertEqual(A.norm("https://www.magic.wizards.com/en/news/x"),
                         "https://magic.wizards.com/en/news/x")
        with self.assertRaises(ValueError):
            A.norm("https://example.org/story/the-twins")
        with self.assertRaises(ValueError):
            A.norm("http://magic.wizards.com/en/news/story")


if __name__ == "__main__":
    unittest.main()
