"""Pack A2 source uncertainty and full historical printing-ID join guard."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pack_a_extension as A2


class ElderDragonWarExtensionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.extension = json.loads(A2.INPUT.read_text(encoding="utf-8"))
        cls.report = A2.build()

    def test_exact_report_replay_and_scope(self):
        self.assertEqual(A2.REPORT.read_bytes(), A2.dump(self.report))
        self.assertEqual(self.report["result"],
                         "SOURCE_GRADED_ELDER_WAR_AND_HISTORICAL_CARD_NAME_JOIN_PASS")
        self.assertEqual((self.report["additional_claims"], self.report["additional_entities"],
                          self.report["first_party_source_urls"], self.report["card_name_anchors"]),
                         (12, 10, 8, 9))

    def test_piru_source_discrepancy_is_explicit(self):
        c = {x["id"]: x for x in self.extension["claims"]}
        self.assertIn("mh2_legends", c["A018"]["source_ids"])
        self.assertIn("perspectives", c["A018"]["source_ids"])
        self.assertIn("Piru", c["A018"]["summary"])
        self.assertIn("incomplete", c["A018"]["limitation"])
        self.assertEqual(c["A020"]["stage"], "post_war_corondor")
        self.assertEqual(c["A021"]["stage"], "post_war_corondor")

    def test_exact_card_names_are_provenances_not_battle_artwork(self):
        a = self.report["card_anchors"]
        self.assertEqual(len({c["oracle_id"] for c in a}), len(a))
        self.assertEqual({c["name"] for c in a},
                         {c["name"] for c in self.extension["card_anchors"]})
        self.assertTrue(all(c["first_indexed_english_paper_printing"]["printing_id"] for c in a))
        self.assertTrue(all(c["historical_english_paper_printings"] > 0 for c in a))
        self.assertTrue(all(c["representation"].startswith("NAMED_") for c in a))
        self.assertFalse(any("ARTWORK_DEPICTS" == c["representation"] for c in a))

    def test_first_party_only(self):
        self.assertTrue(all(A2.base.norm(s["url"]).startswith("https://magic.wizards.com/")
                            for s in self.extension["source_register"].values()))
        with self.assertRaises(ValueError):
            A2.base.norm("https://fan-wiki.example.com/unverified-family-tree")


if __name__ == "__main__":
    unittest.main()
