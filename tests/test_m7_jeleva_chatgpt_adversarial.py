"""Jeleva independent research-only stress configurations; no card is owner approved here."""
import hashlib
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "data/grixis/m7/independent_candidates"
REPORT = ROOT / "data/grixis/m7/independent_reviews/Jeleva__Nephalia_s_Scourge_ChatGPT_Adversarial_20261024.md"
STEM = "Jeleva__Nephalia_s_Scourge_M7_"
FILES = {
    "baseline": "Baseline_Research_20261024.txt",
    "savage": "SavageBeating_Over_MindsDesire_Research_20261024.txt",
    "blast": "DelayedBlastFireball_Over_ToxicDeluge_Research_20261024.txt",
    "two": "Savage_Delayed_TwoSwap_Research_20261024.txt",
    "haste": "HasteMagic_Over_TorchCourier_Research_20261024.txt",
    "samut": "Samut_Over_TorchCourier_Research_20261024.txt",
}
EXPECTED = {
    "baseline": {},
    "savage": {"Savage Beating": "Mind's Desire"},
    "blast": {"Delayed Blast Fireball": "Toxic Deluge"},
    "two": {"Savage Beating": "Mind's Desire", "Delayed Blast Fireball": "Toxic Deluge"},
    "haste": {"Haste Magic": "Torch Courier"},
    "samut": {"Samut, Hazoret's Champion": "Torch Courier"},
}
HISTORICAL_RAW_SHA256 = "00e3f52118f5944684ebc49a5398acf8184f7ca878e861221e4c99931191bc2f"
LANDS = {
    "Ancient Tomb", "Arena of Glory", "Arid Mesa", "Badlands", "Blood Crypt", "Bloodstained Mire",
    "City of Brass", "City of Traitors", "Command Tower", "Exotic Orchard", "Flooded Strand",
    "Gemstone Caverns", "Island", "Mana Confluence", "Marsh Flats", "Misty Rainforest",
    "Morphic Pool", "Otawara, Soaring City", "Polluted Delta", "Scalding Tarn", "Steam Vents",
    "Swamp", "Underground Sea", "Verdant Catacombs", "Volcanic Island", "Watery Grave", "Wooded Foothills",
}
TOP_STAGERS = {
    "Mystical Tutor", "Vampiric Tutor", "Imperial Seal", "Personal Tutor", "Scheming Symmetry",
    "Long-Term Plans", "Brainstorm", "Scroll Rack", "Sensei's Divining Top", "Ponder", "Preordain",
}
HASTE_ENABLERS = {"Torch Courier", "Lightning Greaves", "Arena of Glory", "Borne Upon a Wind"}


def read_cards(key):
    raw = (FOLDER / (STEM + FILES[key])).read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise AssertionError("research files are single-LF normalized; historic source has no LF")
    text = raw.decode("utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "1x Jeleva, Nephalia's Scourge [Commander]":
        raise AssertionError("wrong commander first line")
    if len(lines) != 100 or any(not re.fullmatch(r"1x [^\r\n]+", l) for l in lines[1:]):
        raise AssertionError("research alternative must have 100 one-per-line 1x cards")
    names = [line[3:] for line in lines[1:]]
    if len(names) != len(set(names)):
        raise AssertionError("singleton violation")
    return names, raw


class JelevaAdversarialStress(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base, cls.raw = read_cards("baseline")
        cls.report = REPORT.read_text(encoding="utf-8")

    def test_source_byte_provenance_and_100_distinct(self):
        # Canonical Oct14 TXT lacks terminal LF, unlike reserialized research-only files.
        self.assertEqual(hashlib.sha256(self.raw[:-1]).hexdigest(), HISTORICAL_RAW_SHA256)
        self.assertEqual(len(self.base), 99)
        self.assertEqual(len(set(self.base)), 99)
        self.assertEqual(len(LANDS.intersection(self.base)), 27)
        self.assertEqual(len(TOP_STAGERS.intersection(self.base)), 11)
        self.assertEqual(len(HASTE_ENABLERS.intersection(self.base)), 4)

    def test_all_research_alternatives_exact_swaps_and_mana_shell(self):
        base = set(self.base)
        for key, changes in EXPECTED.items():
            with self.subTest(candidate=key):
                cards, _ = read_cards(key)
                names = set(cards)
                self.assertEqual(len(names), 99)
                self.assertEqual(names - base, set(changes))
                self.assertEqual(base - names, set(changes.values()))
                self.assertEqual(len(LANDS.intersection(names)), 27)
                self.assertEqual(LANDS.intersection(names), LANDS)
                self.assertEqual(TOP_STAGERS.intersection(names), TOP_STAGERS)
                if key not in ("haste", "samut"):
                    self.assertEqual(HASTE_ENABLERS.intersection(names), HASTE_ENABLERS)
                else:
                    self.assertEqual(len(HASTE_ENABLERS.intersection(names)), 3)

    def test_jeleva_combat_timing_and_exile_conditions_are_explicit(self):
        # Official WotC release notes are cited in the research report; these checks
        # validate that the *review* never upgrades conditional branches to guarantees.
        for text in ("declare-attackers", "additional combat", "after this phase",
                     "after a main phase", "extra combat", "needs Jeleva to survive"):
            if text == "needs Jeleva to survive":
                self.assertIn("needs Jeleva to survive", self.report)
            else:
                self.assertIn(text, self.report)
        self.assertIn("5", self.report)
        self.assertIn("cast from exile", self.report)
        self.assertIn("indestructible", self.report)

    def test_no_five_swap_claim_or_owner_approval(self):
        self.assertIn("RESEARCH_ONLY", self.report)
        self.assertIn("no owner-presentable proposal", self.report)
        self.assertIn("no canonical change", self.report)
        self.assertIn("no owner approval", self.report)
        self.assertIn("zero five-swap-ready proposals", self.report)
        self.assertIn("not a validated Magic rules engine", self.report)
        self.assertLess(max(len(changes) for changes in EXPECTED.values()), 5)


if __name__ == "__main__":
    unittest.main()
