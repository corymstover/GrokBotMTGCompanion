"""Cheap, physical 100-card source-bound checks; not Oracle or M6 certification."""
from __future__ import annotations
from collections import Counter
import json
from pathlib import Path
import tempfile
import unittest

from scripts.grixis_m7_decision_gate import parse_list, DecisionGateError

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_portfolio.json"
LAND_NAMES = set("""Ancient Tomb|Badlands|Blood Crypt|Bloodstained Mire|City of Brass|Command Tower|Exotic Orchard|Flooded Strand|Island|Luxury Suite|Mana Confluence|Marsh Flats|Misty Rainforest|Morphic Pool|Mountain|Otawara, Soaring City|Polluted Delta|Scalding Tarn|Steam Vents|Swamp|Takenuma, Abandoned Mire|Training Center|Underground Sea|Urborg, Tomb of Yawgmoth|Verdant Catacombs|Volcanic Island|Watery Grave|Xander's Lounge""".split("|"))
PROTECTED = {
    "Abaddon the Despoiler", "Birgi, God of Storytelling // Harnfel, Horn of Bounty",
    "Neheb, the Eternal", "Loyal Subordinate", "The Ruinous Powers",
    "Underworld Breach", "Lion's Eye Diamond", "Brain Freeze",
    "Mystic Remora", "Boltwave", "Kessig Flamebreather", "Passionate Archaeologist"
}


class AbaddonResearchPortfolio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.base, cls.commanders, _ = parse_list(ROOT / cls.manifest["baseline_source_path"])
        cls.base_counts = Counter(cls.base)

    def test_governance_explicitly_fail_closed(self):
        m = self.manifest
        self.assertEqual(m["stage"], "M7_RESEARCH_COMPARATIVE_NOT_OWNER_READY")
        self.assertEqual(m["canonical_baseline_raw_sha256"],
                         "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf")
        for key in ("owner_approved", "oracle_complete", "m6_certified"):
            self.assertIs(m[key], False)
        self.assertEqual(len(self.base), 100)
        self.assertEqual(len(self.commanders), 1)
        self.assertEqual(sum(c for n,c in self.base_counts.items() if n in LAND_NAMES), 34)

    def test_three_physical_100_card_alternatives_exactly_match_named_swaps(self):
        m = self.manifest
        self.assertEqual({p["id"] for p in m["comparisons"]},
                         {"engine_answer", "combat_answer", "triple_trial"})
        for variant in m["comparisons"]:
            with self.subTest(variant=variant["id"]):
                cards, commanders, companions = parse_list(ROOT / variant["path"])
                self.assertEqual(commanders, self.commanders)
                self.assertEqual(companions, [])
                self.assertEqual(len(cards), 100)
                self.assertEqual(len(set(cards)), 94)
                self.assertEqual(sum(n in LAND_NAMES for n in cards), m["baseline_lands"])
                self.assertTrue(PROTECTED <= set(cards))
                self.assertEqual(Counter(cards) - self.base_counts, Counter(variant["adds"]))
                self.assertEqual(self.base_counts - Counter(cards), Counter(variant["cuts"]))
                self.assertEqual(len(variant["adds"]), len(variant["cuts"]))
                self.assertTrue(set(variant["adds"]).isdisjoint(self.base_counts))

    def test_reject_illicit_nonbasic_duplicate_or_99_card_corruption(self):
        path = ROOT / self.manifest["comparisons"][0]["path"]
        original = path.read_text(encoding="utf-8")
        for corruption in (original.replace("1 Chaos Warp\n", "2 Chaos Warp\n"),
                           original.replace("1 Grinning Ignus\n", "")):
            with self.subTest(length=len(corruption)):
                with tempfile.TemporaryDirectory() as d:
                    temp=Path(d)/"invalid.txt"
                    temp.write_text(corruption,encoding="utf-8")
                    with self.assertRaises(DecisionGateError):
                        parse_list(temp)


if __name__ == "__main__":
    unittest.main()
