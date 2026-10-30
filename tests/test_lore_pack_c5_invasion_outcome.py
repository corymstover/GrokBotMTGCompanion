"""One source establishes two outcomes, not their relative ordering."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_lore_pack_c5 import audit
from query_multiverse_graph import MG


class InvasionOutcomeTests(unittest.TestCase):
    def test_two_separate_editorial_claims(self):
        result = audit()
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["outcome_order"], "UNESTABLISHED")

    def test_official_excerpt_checks_and_negative_control(self):
        body = "<p>crew of the Weatherlight used the artifacts of the Legacy to destroy Yawgmoth himself</p>"
        body += "<p>decimated Phyrexia itself using eldritch 'soul bombs,'</p>"
        self.assertTrue(audit(body)["live_quote_check"])
        with self.assertRaisesRegex(ValueError, "missing from live"):
            audit("<p>not the official source quotations</p>")

    def test_graph_claims_preserve_attribution_and_caveats(self):
        mg = MG()
        claims = {n["id"]: n for n in mg.g["nodes"] if n["type"] == "Claim"}
        for cid in ("claim:C501", "claim:C502"):
            self.assertEqual(claims[cid]["grade"], "CANON_CONFIRMED")
            self.assertTrue(claims[cid]["limitation"])
        edges = [e for e in mg.g["edges"] if e.get("claim") in {"C501", "C502"}]
        self.assertEqual(len(edges), 2)
        self.assertTrue(all(e["sources"] == ["km"] for e in edges))
        self.assertEqual(mg.nodes["source:km"]["url"],
                         "https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19")


if __name__ == "__main__":
    unittest.main()
