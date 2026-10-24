"""Source-bound Jeleva M7 Rev1 owner-ready checks; not an approval or rules engine."""
import hashlib
import json
from pathlib import Path
import unittest

from tests.test_m7_jeleva_chatgpt_adversarial import (HASTE_ENABLERS, TOP_STAGERS,
                                                    read_cards)

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "data/grixis/m7"
CANDIDATE = PREFIX / "independent_candidates/Jeleva__Nephalia_s_Scourge_M7_Rev1_OwnerReady_20261024.txt"
INDEX = PREFIX / "independent_reviews/Jeleva__Nephalia_s_Scourge_M7_Rev1_Oracle_Identity_Index_20261024.json"
PACKET = PREFIX / "independent_reviews/Jeleva__Nephalia_s_Scourge_M7_Rev1_Owner_Packet_20261024.md"
WAIVER = PREFIX / "governance/Jeleva__Nephalia_s_Scourge_Single_Deck_Swap_Floor_Exception_20261024.md"
EXPECTED_SHA = "6f2cdafa089c3e923104429f764bed66e500fe20cafb3b00dd4d29488bd52cac"
EXPECTED_BASE_SHA = "00e3f52118f5944684ebc49a5398acf8184f7ca878e861221e4c99931191bc2f"


class JelevaRev1OwnerReady(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = CANDIDATE.read_bytes()
        cls.lines = cls.raw.decode("utf-8").splitlines()
        cls.names = [line[3:] for line in cls.lines]
        cls.baseline, cls.baseline_raw = read_cards("baseline")
        cls.index = json.loads(INDEX.read_text(encoding="utf-8"))
        cls.packet = PACKET.read_text(encoding="utf-8")
        cls.waiver = WAIVER.read_text(encoding="utf-8")

    def test_exact_sha_and_bytes(self):
        self.assertEqual(len(self.raw), 1807)
        self.assertTrue(self.raw.endswith(b"\n"))
        self.assertFalse(self.raw.endswith(b"\n\n"))
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), EXPECTED_SHA)
        self.assertEqual(hashlib.sha256(self.baseline_raw[:-1]).hexdigest(), EXPECTED_BASE_SHA)

    def test_100_card_singleton_commander_first_and_exact_two_swaps(self):
        self.assertEqual(len(self.lines), 100)
        self.assertEqual(self.lines[0], "1x Jeleva, Nephalia's Scourge [Commander]")
        self.assertTrue(all(l.startswith("1x ") and l == l.strip() for l in self.lines))
        self.assertEqual(len(set(self.names)), 100)
        self.assertEqual(set(self.names) - set(self.baseline), {
            "Jeleva, Nephalia's Scourge [Commander]", "Cavern of Souls", "Fire Covenant"})
        self.assertEqual(set(self.baseline) - set(self.names), {"City of Traitors", "Toxic Deluge"})
        self.assertEqual(TOP_STAGERS & set(self.names), TOP_STAGERS)
        self.assertEqual(HASTE_ENABLERS & set(self.names), HASTE_ENABLERS)

    def test_source_bound_card_legality_and_color_identity(self):
        index = self.index
        self.assertEqual(index["candidate_raw_sha256"], EXPECTED_SHA)
        self.assertEqual(index["source_date"], "2026-10-23")
        self.assertEqual(index["external_card"]["name"], "Cavern of Souls")
        self.assertEqual(index["external_card"]["commander_legality"], "legal")
        self.assertEqual(len(index["cards"]), 99)
        by_name = {entry["name"]: entry for entry in index["cards"]}
        self.assertEqual(len(by_name), 99)
        actual = {self.lines[0][3:].removesuffix(" [Commander]")} | set(self.names[1:])
        self.assertEqual(actual - set(by_name), {"Cavern of Souls"})
        for entry in index["cards"] + [index["external_card"]]:
            with self.subTest(card=entry["name"]):
                self.assertEqual(entry["commander_legality"], "legal")
                self.assertTrue(set(entry["color_identity"]) <= {"B", "R", "U"})
        lands = [c for c in index["cards"] if "Land" in c["type_line"]]
        self.assertEqual(len(lands) + 1, 27)
        spells = [c for c in index["cards"] if "Instant" in c["type_line"] or "Sorcery" in c["type_line"]]
        self.assertEqual(len(spells), 45)
        self.assertEqual(sum(bool(c["game_changer"]) for c in index["cards"]), 20)

    def test_waiver_is_jeleva_only_and_canonical_pending(self):
        self.assertIn("Jeleva", self.waiver)
        self.assertIn("five-swap", self.waiver)
        self.assertIn("two", self.waiver.lower())
        self.assertIn("does not constitute approval", self.waiver.lower())
        self.assertIn(EXPECTED_SHA, self.waiver)
        self.assertIn(EXPECTED_SHA, self.packet)
        self.assertIn("NOT APPROVED", self.packet)
        self.assertIn("CANONICAL MAIN NOT CHANGED", self.packet)
        self.assertIn("City of Traitors", self.packet)
        self.assertIn("Toxic Deluge", self.packet)
        self.assertIn("additional cost", self.packet)


if __name__ == "__main__":
    unittest.main()
