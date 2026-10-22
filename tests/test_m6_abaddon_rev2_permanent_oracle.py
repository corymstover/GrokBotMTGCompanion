"""Archived current 100-name Abaddon rev2 Oracle/identity source integrity.

Audits the exact new six-swap candidate rather than laundering the historical
two-swap I/J certificate or claiming full M6/M7 owner certification.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

from scripts.grixis_m6_abaddon_oracle_capture import logical_hash
from scripts.grixis_m7_abaddon_rev2_live_oracle import MANIFEST, validate_portfolio

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
EXPECTED = {
    "six_swap_selected_research": "lh1:853567925301becc5b646c193795a18871c269abce1368690cca5d9bda73a0b7",
    "five_swap_clone_focused_alternative": "lh1:c248964e93955e4b81b0e4de735d8dc66f6abfe29a580e39f0c164e59ee53654",
    "five_swap_combat_focused_alternative": "lh1:7be03e1b440689e3000d70fc447d97edea6f0200ce3941b2ffd9fc17b48aa4fd",
}
APPROVED = "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"


class PermanentAbaddonRev2Oracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.archive = json.loads(ARCHIVE.read_text(encoding="utf-8"))
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.variants, cls.source_hash = validate_portfolio(cls.manifest)
        cls.oracle = cls.archive["oracle_snapshot"]

    def test_exact_local_scryfall_capture_bytes_and_date(self):
        self.assertEqual(hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
                         "5ed756a9ba0f11b3994f6436ecab31a248a5bf491154c4d7e916c49610ac7ce5")
        self.assertEqual(self.archive["stage"],"LIVE_ORACLE_REVISED_ABADDON_RESEARCH_NOT_M6_M7_CERTIFICATION")
        self.assertEqual(self.archive["card_identity_count"],100)
        self.assertEqual(len(self.oracle),100)
        self.assertEqual(self.archive["source_approved_sha256"],APPROVED)
        self.assertTrue(self.archive["checked_at_utc"].startswith("2026-10-22"))
        self.assertEqual(self.archive["scryfall_endpoint"],"https://api.scryfall.com/cards/collection")

    def test_every_full_oracle_text_digest_and_grixis_legal_status(self):
        for name,card in self.oracle.items():
            with self.subTest(card=name):
                self.assertTrue(card["oracle_id"])
                self.assertEqual(card["commander_legality"],"legal")
                self.assertTrue(set(card["color_identity"]) <= {"B","U","R"})
                self.assertEqual(hashlib.sha256(card["oracle_text"].encode("utf-8")).hexdigest(),
                                 card["oracle_text_sha256"])
                self.assertTrue(card["scryfall_uri"].startswith("https://scryfall.com/"))

    def test_every_exact_physical_100_and_oracle_id_bound_logical_hash(self):
        self.assertEqual(self.source_hash,APPROVED)
        self.assertEqual(set(self.archive["physical_lists"]),set(self.variants))
        self.assertEqual(logical_hash(self.variants["baseline"],self.oracle),
                         "lh1:5a1e5e5bb86ba35d7dbf712fbc3a7d29c3e05a17569c05e8a11976321699b793")
        for v in self.manifest["comparisons"]:
            cards=self.variants[v["id"]]
            with self.subTest(variant=v["id"]):
                self.assertEqual(len(cards),100)
                self.assertEqual(self.archive["physical_lists"][v["id"]]["physical_sha256"],v["sha256"])
                self.assertTrue(set(cards) <= set(self.oracle))
                self.assertEqual(logical_hash(cards,self.oracle),EXPECTED[v["id"]])
        self.assertNotEqual(EXPECTED["six_swap_selected_research"],
                            "lh1:4bb15eb5acc051871e7d818890f71705eb74f1281e933e73b0e77ff770be1efc")

    def test_abaddon_specific_new_oracle_facts(self):
        expected=self.manifest["newly_checked_scryfall_oracle"]
        for name,item in expected.items():
            for k in ("oracle_id","mana_value","mana_cost","oracle_text","commander_legality","color_identity"):
                self.assertEqual(self.oracle[name][k],item[k])
        self.assertIn("isn't legendary",self.oracle["Spark Double"]["oracle_text"])
        self.assertEqual(self.oracle["Cyclonic Rift"]["mana_value"],2)

    def test_no_owner_approval_or_m6_i_j_fabricated(self):
        self.assertIs(self.archive["owner_m7_approval"],False)
        self.assertIs(self.archive["formal_m6_certificate"],False)
        self.assertIs(self.archive["old_two_swap_ij_not_rebound"],True)
        self.assertIs(self.manifest["m6_ij_recertified_for_revised_list"],False)


if __name__ == "__main__":
    unittest.main()
