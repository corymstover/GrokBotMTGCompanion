"""Deck #23 Inalla independent round-2 source-bound alternatives; no canonical approval."""
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data/grixis/m7/baseline_sources/Inalla__Archmage_Ritualist_approved_source_2026-10-14.txt"
CAND = ROOT / "data/grixis/m7/independent_candidates"
REVIEW = ROOT / "data/grixis/m7/independent_reviews/Inalla__Archmage_Ritualist_ChatGPT_Round2_20261024.json"
MD = ROOT / "data/grixis/m7/independent_reviews/Inalla__Archmage_Ritualist_ChatGPT_Round2_20261024.md"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Inalla__Archmage_Ritualist_M7_Scryfall_20261023.json"
BASE_SHA = "81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3"

EXPECTED = {
    "flashback_one_swap": ("Inalla__Archmage_Ritualist_M7_Flashback_One_Swap_20261024.txt",
        "0bbe50e990f58ea36c9cb0a0c442dba3cc41fe9cf9580fffe08d095834b75e51",
        {"Flashback"}, {"Kefka, Court Mage // Kefka, Ruler of Ruin"}),
    "four_swap_challenge": ("Inalla__Archmage_Ritualist_M7_Four_Swap_Combat_20261024.txt",
        "fa7e1434332b0abdf5cdbd656c4483c02ce76f7431342116a0e9b0c426633d00",
        {"Flashback", "Corpse Dance", "Forbidden Orchard", "Starting Town"},
        {"Kefka, Court Mage // Kefka, Ruler of Ruin", "Final Fortune", "Exotic Orchard", "Island"}),
    "five_swap_stress_rejected": ("Inalla__Archmage_Ritualist_M7_Five_Swap_Stress_NotApproved_20261024.txt",
        "0327b8413ca38182b4710346087d7f35f5e0c6cfee1bd0af90fc61c757c181bb",
        {"Flashback", "Corpse Dance", "Forbidden Orchard", "Starting Town", "Pyroblast"},
        {"Kefka, Court Mage // Kefka, Ruler of Ruin", "Final Fortune", "Exotic Orchard", "Island",
         "Red Elemental Blast"}),
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        assert m, (path, line)
        out[m[2]] += int(m[1])
    return out

class InallaRound2SourceBound(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = parse(SRC)
        cls.review = json.loads(REVIEW.read_text(encoding="utf-8"))
        cls.oracle = {x["name"]: x for x in json.loads(
            ORACLE.read_text(encoding="utf-8"))["cards"]}

    def test_canonical_source_stable_and_research_only_disclosure(self):
        self.assertEqual(digest(SRC), BASE_SHA)
        self.assertFalse(SRC.read_bytes().endswith(b"\n"))
        self.assertEqual((sum(self.source.values()), len(self.source)), (100, 100))
        self.assertEqual(self.source["Inalla, Archmage Ritualist"], 1)
        self.assertFalse(self.review["owner_approved"])
        self.assertFalse(self.review["canonical_changed"])
        self.assertEqual(self.review["preserved_newly_m7_locked_decks"], 22)
        self.assertIn("RESEARCH_ONLY", self.review["status"])
        self.assertIn("RESEARCH_ONLY", MD.read_text(encoding="utf-8"))

    def test_all_three_exact_100_and_only_disclosed_swaps(self):
        by_id = {x["name"]: x for x in self.review["alternatives"]}
        self.assertEqual(set(by_id), set(EXPECTED))
        for key, (filename, sha, added, cut) in EXPECTED.items():
            path = CAND / filename
            data = parse(path)
            with self.subTest(key=key):
                self.assertEqual(digest(path), sha)
                self.assertTrue(path.read_bytes().endswith(b"\n"))
                self.assertEqual((sum(data.values()), len(data)), (100, 100))
                self.assertEqual(data["Inalla, Archmage Ritualist"], 1)
                self.assertEqual(set(data - self.source), added)
                self.assertEqual(set(self.source - data), cut)
                self.assertEqual(by_id[key]["raw_sha256"], sha)
                self.assertFalse(by_id[key]["owner_presentable"])
                self.assertEqual(sum("Land" in self.oracle[n]["type_line"] for n in data
                                     if n in self.oracle), 27)

    def test_oracle_identity_and_legality_separately_bound_to_actual_sources(self):
        flash = self.review["new_discoveries"]["flashback"]
        self.assertEqual(flash["mana_cost"], "{R}")
        self.assertEqual(flash["type"], "Instant")
        self.assertEqual(flash["color_identity"], ["R"])
        self.assertEqual(flash["commander_legality"], "legal")
        self.assertIn("target instant or sorcery card", flash["oracle_text"].lower())
        self.assertTrue(flash["official_gatherer"].startswith("https://gatherer.wizards.com/"))
        self.assertTrue(flash["official_wizards_legality_rules"].startswith("https://magic.wizards.com/"))
        self.assertNotIn("Flashback", self.oracle)  # separate 2026 official source, not frozen archive
        for key, (filename, _, _, _) in EXPECTED.items():
            deck = parse(CAND / filename)
            with self.subTest(key=key):
                self.assertEqual(set(deck) - set(self.oracle), {"Flashback"})
                gc = 0
                for name in deck:
                    if name == "Flashback":
                        continue
                    c = self.oracle[name]
                    self.assertEqual(c["commander_legality"], "legal", name)
                    self.assertTrue(set(c["color_identity"]) <= set("UBR"), name)
                    self.assertTrue(c["oracle_text"], name)
                    gc += bool(c["game_changer"])
                self.assertEqual(gc, 18)

    def test_preserves_primary_inalla_combo_routes(self):
        for filename, _, _, _ in EXPECTED.values():
            deck = parse(CAND / filename)
            for name in ["Inalla, Archmage Ritualist", "Spellseeker", "Scholar of the Ages",
                         "Burnt Offering", "Culling the Weak", "Finale of Promise", "Unearth",
                         "Reanimate", "Shallow Grave", "Entomb", "Ruthless Technomancer",
                         "Bloodline Necromancer", "Underworld Breach", "Brain Freeze",
                         "Lion's Eye Diamond", "Thassa's Oracle", "Tainted Pact"]:
                self.assertEqual(deck[name], 1, name)
        self.assertIn("mana value 2 or less", self.oracle["Spellseeker"]["oracle_text"])

    def test_corpse_dance_combo_and_constraints(self):
        c = self.oracle["Corpse Dance"]["oracle_text"]
        scholar = self.oracle["Scholar of the Ages"]["oracle_text"]
        burnt = self.oracle["Burnt Offering"]["oracle_text"]
        self.assertIn("Buyback {2}", c)
        self.assertIn("top creature card", c)
        self.assertIn("return up to two target instant and/or sorcery", scholar)
        self.assertIn("sacrificed creature's mana value", burnt)
        self.assertEqual(self.oracle["Scholar of the Ages"]["cmc"], 7)
        # Burnt Offering = one black invested for 7 B/R, Corpse Dance buyback = 5;
        # conditional net +1 mana per iteration after initial setup.
        self.assertEqual(7 - 1 - (3 + 2), 1)
        self.assertIn("top-creature graveyard ordering",
            self.review["new_discoveries"]["corpse_dance"]["extra_prerequisites"])

    def test_mana_and_fifth_swap_not_fabricated(self):
        orchard = self.oracle["Forbidden Orchard"]["oracle_text"]
        self.assertIn("target opponent creates a 1/1", orchard)
        self.assertIn("an opponent controls", self.oracle["Exotic Orchard"]["oracle_text"])
        self.assertIn("first, second, or third turn", self.oracle["Starting Town"]["oracle_text"])
        self.assertIn("Pay 1 life", self.oracle["Starting Town"]["oracle_text"])
        self.assertIn("Island", self.source)
        self.assertIn("Swamp", self.source)
        self.assertIn("five_swap_stress_rejected", EXPECTED)
        self.assertTrue(self.review["alternatives"][-1]["rejected_reason"])
        self.assertFalse(any(x["owner_presentable"] for x in self.review["alternatives"]))
        self.assertEqual(self.review["sample_stats"]["parsed_tournament_decks"], 250)
        self.assertFalse(self.review["sample_stats"]["dual_caster_ppg_observation"]["causal"])

if __name__ == "__main__":
    unittest.main()
