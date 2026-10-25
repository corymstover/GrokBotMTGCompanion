"""Deck #27 Grixistax M7 Rev1 source-bound, offline structural checks.

These tests deliberately do not claim to simulate gameplay, resolve rules, or
replace a current live Oracle/legality check.
"""

import hashlib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/grixis/m7/baseline_sources/Grixistax___October_2026_approved_source_2026-10-14.txt"
CANDIDATE = ROOT / "data/grixis/m7/candidate_lists/Grixistax___October_2026_ChatGPT_Rev1.txt"
BASE_SHA = "f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c"
CAND_SHA = "70b48148409e849e38d7189bcda032d1c98d74329302563a005f86a86b81279e"
ADDS = {
    "Arcane Signet", "Bitterblossom", "Opposition",
    "Phyrexian Altar", "Ophiomancer",
}
CUTS = {
    "Mox Amber", "Magus of the Moon", "Ashiok, Dream Render",
    "Damping Sphere", "Sheoldred, the Apocalypse",
}
COMMANDERS = {
    "Kraum, Ludevic's Opus", "Tevesh Szat, Doom of Fools",
}
LANDS = {
    "Ancient Tomb", "Arid Mesa", "Badlands", "Blood Crypt",
    "Bloodstained Mire", "City of Brass", "Command Tower",
    "Flooded Strand", "Gemstone Caverns", "Island",
    "Mana Confluence", "Marsh Flats", "Misty Rainforest",
    "Morphic Pool", "Mountain", "Otawara, Soaring City",
    "Phyrexian Tower", "Polluted Delta", "Scalding Tarn",
    "Steam Vents", "Swamp", "Underground Sea",
    "Verdant Catacombs", "Volcanic Island", "Watery Grave",
    "Wooded Foothills",
}
PRESERVED = {
    "Contamination", "Skullclamp", "Winter Orb", "Static Orb",
    "Tangle Wire", "Blood Moon", "Back to Basics", "Trinisphere",
    "Chalice of the Void", "Cursed Totem", "Torpor Orb", "Overburden",
    "Karn, the Great Creator", "Helm of Obedience", "Leyline of the Void",
    "Dauthi Voidwalker", "Underworld Breach", "Lion's Eye Diamond",
    "Brain Freeze", "Wheel of Fortune", "Windfall",
    "Narset, Parter of Veils", "Notion Thief",
    "Opposition Agent", "Necropotence", "Rhystic Study",
    "Mystic Remora", "Phyrexian Tower", "Diabolic Intent",
    "Culling the Weak", "Force of Will", "Force of Negation",
    "Mindbreak Trap", "Tainted Pact",
}


def parse(path):
    rows = path.read_text(encoding="utf-8").splitlines()
    result = []
    for row in rows:
        assert row.startswith("1x "), f"bad format {row!r}"
        name = row[3:].replace(" [Commander]", "")
        result.append((name, row.endswith(" [Commander]")))
    return result


class GrixistaxRev1Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = parse(BASE)
        cls.after = parse(CANDIDATE)
        cls.bnames = {name for name, _ in cls.before}
        cls.anames = {name for name, _ in cls.after}

    def test_exact_raw_hashes(self):
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), BASE_SHA)
        self.assertEqual(hashlib.sha256(CANDIDATE.read_bytes()).hexdigest(), CAND_SHA)
        self.assertTrue(CANDIDATE.read_bytes().endswith(b"\n"))

    def test_exact_100_singleton_and_pair(self):
        for rows in (self.before, self.after):
            self.assertEqual(len(rows), 100)
            self.assertEqual(len({name for name, _ in rows}), 100)
            self.assertEqual({name for name, commander in rows if commander}, COMMANDERS)
            self.assertEqual([commander for _, commander in rows[:2]], [True, True])
            self.assertEqual(sum(commander for _, commander in rows), 2)
            self.assertTrue(all(not commander for _, commander in rows[2:]))

    def test_exact_five_one_for_one_swaps(self):
        self.assertEqual(self.anames - self.bnames, ADDS)
        self.assertEqual(self.bnames - self.anames, CUTS)
        self.assertEqual(len(self.anames & self.bnames), 95)

    def test_land_count_and_same_mana_base(self):
        self.assertEqual(len(LANDS), 26)
        self.assertEqual(self.anames & LANDS, LANDS)
        self.assertEqual(self.bnames & LANDS, LANDS)
        self.assertEqual((self.anames - self.bnames) & LANDS, set())
        self.assertEqual((self.bnames - self.anames) & LANDS, set())

    def test_identity_wheels_prison_and_win_packages_preserved(self):
        self.assertTrue(PRESERVED.issubset(self.anames))
        self.assertTrue(COMMANDERS.issubset(self.anames))
        self.assertNotIn("Thassa's Oracle", self.anames)
        self.assertNotIn("Demonic Consultation", self.anames)
        self.assertNotIn("Urza, Lord High Artificer", self.anames)

    def test_no_unintended_special_rules(self):
        self.assertNotIn("Lutri, the Spellchaser", self.anames)
        self.assertNotIn("Trade Secrets", self.anames)
        self.assertNotIn("Yawgmoth's Bargain", self.anames)


if __name__ == "__main__":
    unittest.main()
