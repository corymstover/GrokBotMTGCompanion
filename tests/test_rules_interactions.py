"""Tests for the Phase 7 gameplay rules-interaction checks (scripts/rules_interactions.py)."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_cr_keyword_excerpt as X  # noqa: E402
import rules_interactions as R  # noqa: E402


class KeywordExcerptTests(unittest.TestCase):
    def test_self_hash_and_known_rules(self):
        self.assertEqual(X.main(["--check"]), 0)
        self.assertEqual(R.CR["sections"]["702.19"], "Trample")
        self.assertEqual(R.CR["sections"]["702.2"], "Deathtouch")
        self.assertIn("can’t be destroyed", R.CR["rules"]["702.12b"])
        self.assertEqual(R.CR["source_sha256"][:8], "8d860e45")

    def test_keyword_citation(self):
        c = R.cite_keyword("Deathtouch")
        self.assertEqual(c["rule"], "702.2")
        self.assertTrue(c["text"] and c["text"][0]["rule"] == "702.2a")
        self.assertEqual(R.cite_keyword("Swampwalk")["rule"], "702.14")
        self.assertIsNone(R.cite_keyword("Not A Keyword")["rule"])


class PairTests(unittest.TestCase):
    def test_direct_ruling_verified(self):
        d = R.pair("Urza's Saga", "Urza's Tower")
        self.assertEqual(d["confidence"], "VERIFIED")
        self.assertTrue(any("doesn't interact" in r["text"] for r in d["result"]["direct_rulings"]))

    def test_own_short_name_is_not_a_link(self):
        d = R.pair("Nicol Bolas, God-Pharaoh", "Nicol Bolas")
        self.assertFalse([r for r in d["result"]["direct_rulings"] if r["ruling_of"] == "Nicol Bolas, God-Pharaoh"])

    def test_set_name_is_not_a_link(self):
        d = R.pair("Hall of Tagsin", "The Brothers' War")
        self.assertEqual(d["result"]["direct_rulings"], [])
        self.assertIn("NO_DIRECT_RULING", d["flags"])
        self.assertEqual(d["confidence"], "QUALIFIED")

    def test_keyword_rules_cited(self):
        d = R.pair("Questing Beast", "Gisela, Blade of Goldnight")
        rules = {k["rule"] for k in d["result"]["keyword_rules"]}
        self.assertTrue({"702.2", "702.7", "702.9"} <= rules)

    def test_unknown_card(self):
        self.assertEqual(R.main(["pair", "No Such Card Zzz", "Island"]), 3)


class AuditTests(unittest.TestCase):
    def test_audit_current_and_grounded(self):
        self.assertEqual(R.main(["audit", "--check"]), 0)
        d = json.loads(R.AUDIT.read_text(encoding="utf-8"))
        self.assertEqual(d["totals"]["unresolved_cards"], 0)
        self.assertIn("not a rules certification", d["status"])
        for deck in d["decks"]:
            for l in deck["direct_ruling_links"]:
                rec = R.record(l["ruling_of"])
                self.assertIn({"date": l["date"], "text": l["text"]}, rec["rulings"])
                self.assertTrue(R._mentions(l["text"], l["names"]) or R._mentions(l["text"], l["names"].split(" // ")[0]))

    def test_decklist_parser_strips_set_and_number(self):
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("1x Ugin, the Spirit Dragon (frf) 1\n1 Island\n1x Karn Liberated [Commander]\n")
        self.assertEqual(R.parse_decklist(Path(f.name)), ["Ugin, the Spirit Dragon", "Island", "Karn Liberated"])


if __name__ == "__main__":
    unittest.main()
