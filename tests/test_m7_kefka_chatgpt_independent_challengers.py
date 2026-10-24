"""Kefka independent 14 whole-100 research variants; no canonical owner approval."""
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "data/grixis/m7/independent_candidates"
INDEX = ROOT / "data/grixis/m7/independent_reviews/Kefka__Court_Mage_M7_Independent_Oracle_Index_20261024.json"
REPORT = ROOT / "data/grixis/m7/independent_reviews/Kefka__Court_Mage_ChatGPT_New_Challenger_Checkpoint_20261024.md"
BASE_SHA = "cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03"
STEM = "Kefka__Court_Mage_M7_"
PAIRS = {
    "Baseline": [],
    "Dualcaster_Over_Culling": [("Dualcaster Mage", "Culling the Weak")],
    "Chameleon_Over_DemonicCounsel": [("Chameleon, Master of Disguise", "Demonic Counsel")],
    "FleshDuplicate_Over_DemonicCounsel": [("Flesh Duplicate", "Demonic Counsel")],
    "GeneratorServant_Over_Culling": [("Generator Servant", "Culling the Weak")],
    "FireCovenant_Over_ToxicDeluge": [("Fire Covenant", "Toxic Deluge")],
    "Dualcaster_Chameleon_TwoSwap": [
        ("Dualcaster Mage", "Culling the Weak"), ("Chameleon, Master of Disguise", "Demonic Counsel")],
    "Dualcaster_FleshDuplicate_TwoSwap": [
        ("Dualcaster Mage", "Culling the Weak"), ("Flesh Duplicate", "Demonic Counsel")],
    "Generator_Chameleon_TwoSwap": [
        ("Generator Servant", "Culling the Weak"), ("Chameleon, Master of Disguise", "Demonic Counsel")],
    "Triple_With_FireCovenant_Stress": [
        ("Dualcaster Mage", "Culling the Weak"), ("Chameleon, Master of Disguise", "Demonic Counsel"),
        ("Fire Covenant", "Toxic Deluge")],
    "GlasspoolMimic_Over_DemonicCounsel": [
        ("Glasspool Mimic // Glasspool Shore", "Demonic Counsel")],
    "Naban_Over_DemonicCounsel": [("Naban, Dean of Iteration", "Demonic Counsel")],
    "Dualcaster_Glasspool_TwoSwap": [
        ("Dualcaster Mage", "Culling the Weak"), ("Glasspool Mimic // Glasspool Shore", "Demonic Counsel")],
    "Chameleon_Glasspool_TwoSwap": [
        ("Chameleon, Master of Disguise", "Culling the Weak"),
        ("Glasspool Mimic // Glasspool Shore", "Demonic Counsel")],
}


def read(key):
    suffix = "Baseline_Research_20261024.txt" if key == "Baseline" else key + "_Research_20261024.txt"
    raw = (DIR / (STEM + suffix)).read_bytes()
    assert raw.endswith(b"\n") and not raw.endswith(b"\n\n")
    lines = raw.decode("utf-8").splitlines()
    assert len(lines) == 100
    assert lines[0] == "1x Kefka, Court Mage // Kefka, Ruler of Ruin [Commander]"
    assert all(line.startswith("1x ") for line in lines)
    assert len(set(lines)) == 100
    return raw, [line.removeprefix("1x ").removesuffix(" [Commander]") for line in lines]


class KefkaIndependentChallengers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline_raw, cls.base = read("Baseline")
        cls.index = json.loads(INDEX.read_text(encoding="utf-8"))
        cls.report = REPORT.read_text(encoding="utf-8")

    def test_historical_baseline_raw_bytes_unchanged(self):
        self.assertEqual(hashlib.sha256(self.baseline_raw[:-1]).hexdigest(), BASE_SHA)
        self.assertEqual(len(self.base), 100)

    def test_all_fourteen_are_exact_full_100_with_only_staged_swaps(self):
        self.assertEqual(len(PAIRS), 14)
        base = Counter(self.base)
        for key, swaps in PAIRS.items():
            with self.subTest(configuration=key):
                raw, cards = read(key)
                self.assertEqual(len(cards), 100)
                expected = base.copy()
                for add, cut in swaps:
                    expected[cut] -= 1
                    expected[add] += 1
                    self.assertNotEqual(add, cut)
                self.assertEqual(Counter(cards), +expected)
                self.assertEqual(len(set(cards)), 100)
                self.assertEqual(cards.count("Kefka, Court Mage // Kefka, Ruler of Ruin"), 1)

    def test_source_bound_oracle_identity_and_legality(self):
        j = self.index
        self.assertEqual(j["source_date"], "2026-10-23")
        self.assertEqual(len(j["cards"]), 106)
        indexed = {c["name"]: c for c in j["cards"]}
        self.assertEqual(len(indexed), 106)
        external = j["external_card"]
        self.assertEqual(external["name"], "Chameleon, Master of Disguise")
        self.assertIn("gatherer.wizards.com", external["official_card_url"])
        for key in PAIRS:
            _, names = read(key)
            with self.subTest(configuration=key):
                self.assertEqual(set(names) - set(indexed), 
                                 {"Chameleon, Master of Disguise"} if external["name"] in names else set())
        for card in j["cards"] + [external]:
            with self.subTest(card=card["name"]):
                self.assertEqual(card["commander_legality"], "legal")
                self.assertTrue(set(card["color_identity"]) <= {"U", "B", "R"})
        _, base = read("Baseline")
        self.assertEqual(sum("Land" in indexed[n]["type_line"] for n in base), 28)
        self.assertEqual(sum(bool(indexed[n]["game_changer"]) for n in base), 20)

    def test_chameleon_mayhem_timing_and_name_caveat_reported(self):
        for term in ("Chameleon, Master of Disguise", "Mayhem", "eight mana", "own name",
                     "legend-rule", "regular creature casting timing", "not certified",
                     "no automatic acceptance", "only if discarded that turn"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), self.report.lower())

    def test_other_risks_and_competing_cut_slots_disclosed(self):
        for term in ("Flesh Duplicate", "vanishing 3", "double blue", "Glasspool",
                     "tapped-only blue", "Generator Servant", "Culling the Weak",
                     "Demonic Counsel", "Fire Covenant", "Toxic Deluge",
                     "Naban", "Harmonic Prodigy", "owner-direction"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), self.report.lower())

    def test_floor_and_preservation(self):
        self.assertIn("RESEARCH_ONLY", self.report)
        self.assertIn("No owner-presentable M7 list", self.report)
        self.assertIn("five-swap minimum", self.report)
        self.assertIn("canonical change", self.report)
        self.assertLess(max(len(s) for s in PAIRS.values()), 5)


if __name__ == "__main__":
    unittest.main()
