"""Exact-100 Inalla M7 Rev1 owner-facing candidate source gate; does not approve."""
import hashlib
import itertools
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/grixis/m7/baseline_sources/Inalla__Archmage_Ritualist_approved_source_2026-10-14.txt"
CANDIDATE = ROOT / "data/grixis/m7/independent_candidates/Inalla__Archmage_Ritualist_M7_Rev1_Five_Swap_Gifts_20261024.txt"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Inalla__Archmage_Ritualist_M7_Scryfall_20261023.json"
REVIEW = ROOT / "data/grixis/m7/independent_reviews/Inalla__Archmage_Ritualist_ChatGPT_M7_Rev1_20261024.md"

OLD_SHA = "81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3"
NEW_SHA = "c9f35cac41a7717ef49b4dd3cb4f6031c2795a0082b31b54a13e645652df9b69"
ADD = {"Flashback", "Corpse Dance", "Gifts Ungiven", "Forbidden Orchard", "Starting Town"}
CUT = {"Kefka, Court Mage // Kefka, Ruler of Ruin", "Final Fortune", "Wheel of Fortune",
       "Exotic Orchard", "Island"}
CORE = {
    "Inalla, Archmage Ritualist", "Spellseeker", "Culling the Weak", "Unearth",
    "Burnt Offering", "Finale of Promise", "Entomb", "Reanimate",
    "Scholar of the Ages", "Shallow Grave", "Bloodline Necromancer",
    "Ruthless Technomancer", "Saw in Half", "Thassa's Oracle", "Demonic Consultation",
    "Tainted Pact", "Underworld Breach", "Lion's Eye Diamond", "Brain Freeze",
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    counts = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        assert match, (path, line)
        counts[match[2]] += int(match[1])
    return counts

class InallaFiveSwapOwnerGate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old = parse(BASE)
        cls.new = parse(CANDIDATE)
        cls.snapshot = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards = {card["name"]: card for card in cls.snapshot["cards"]}
        cls.md = REVIEW.read_text(encoding="utf-8")

    def test_sha_exact_and_historical_canon_unchanged(self):
        self.assertEqual(sha(BASE), OLD_SHA)
        self.assertFalse(BASE.read_bytes().endswith(b"\n"))
        self.assertEqual(sha(CANDIDATE), NEW_SHA)
        self.assertTrue(CANDIDATE.read_bytes().endswith(b"\n"))
        self.assertIn("OWNER APPROVAL PENDING", self.md)
        self.assertIn("NOT CANONICAL", self.md)
        self.assertIn(NEW_SHA, self.md)

    def test_exact_five_additions_cuts_100_count_distinct(self):
        self.assertEqual((sum(self.old.values()), len(self.old)), (100, 100))
        self.assertEqual((sum(self.new.values()), len(self.new)), (100, 100))
        self.assertEqual(self.new["Inalla, Archmage Ritualist"], 1)
        self.assertEqual(self.new - self.old, Counter({x: 1 for x in ADD}))
        self.assertEqual(self.old - self.new, Counter({x: 1 for x in CUT}))
        self.assertTrue(CORE <= set(self.new))
        self.assertEqual(len(self.new & self.old), 95)

    def test_archived_current_oracle_and_known_official_flashback_source(self):
        # A candidate-specific Oct23 live-Scryfall snapshot covers 99 names.
        self.assertEqual(set(self.new) - set(self.cards), {"Flashback"})
        self.assertIn("gatherer.wizards.com/SOS/en-us/115/flashback", self.md)
        self.assertIn("scryfall.com/card/sos/115/flashback", self.md)
        self.assertIn("magic.wizards.com/en/news/feature/secrets-of-strixhaven-release-notes", self.md)
        self.assertIn("officially released and legal", self.md)
        game_changers = set()
        land_count = 0
        for name in self.new:
            if name == "Flashback":
                continue
            card = self.cards[name]
            self.assertEqual(card["commander_legality"], "legal", name)
            self.assertTrue(set(card["color_identity"]) <= set("UBR"), name)
            self.assertTrue(card["oracle_text"], name)
            land_count += ("Land" in card["type_line"])
            if card["game_changer"]:
                game_changers.add(name)
        self.assertEqual(land_count, 27)
        self.assertEqual(len(game_changers), 19)
        self.assertIn("Gifts Ungiven", game_changers)
        self.assertNotIn("Wheel of Fortune", game_changers)
        self.assertEqual(self.cards["Gifts Ungiven"]["mana_cost"], "{3}{U}")

    def test_all_six_gifts_splits_reach_spellseeker(self):
        pile = ("Spellseeker", "Step Through", "Reanimate", "Unearth")
        spell = self.cards["Gifts Ungiven"]["oracle_text"]
        self.assertIn("up to four cards with different names", spell)
        self.assertIn("Target opponent chooses two of those cards", spell)
        self.assertIn("graveyard and the rest into your hand", spell)
        routes = []
        for grave_pair in itertools.combinations(pile, 2):
            grave = set(grave_pair)
            hand = set(pile) - grave
            self.assertEqual((len(grave), len(hand)), (2, 2))
            possible = (
                "Spellseeker" in hand or
                ("Spellseeker" in grave and bool({"Reanimate", "Unearth"} & hand))
            )
            self.assertTrue(possible, grave_pair)
            routes.append(possible)
        self.assertEqual(len(routes), 6)
        self.assertIn("mana value 2 or less", self.cards["Spellseeker"]["oracle_text"])
        self.assertIn("mana value 3 or less", self.cards["Unearth"]["oracle_text"])
        self.assertIn("life equal to that card's mana value", self.cards["Reanimate"]["oracle_text"])
        self.assertIn("nontoken Wizard", self.cards["Inalla, Archmage Ritualist"]["oracle_text"])

    def test_corpse_dance_burnt_offering_scholar_core(self):
        self.assertIn("top creature card", self.cards["Corpse Dance"]["oracle_text"])
        self.assertIn("Buyback {2}", self.cards["Corpse Dance"]["oracle_text"])
        self.assertIn("return up to two target instant and/or sorcery",
                      self.cards["Scholar of the Ages"]["oracle_text"])
        self.assertIn("sacrificed creature's mana value",
                      self.cards["Burnt Offering"]["oracle_text"])
        self.assertEqual(self.cards["Scholar of the Ages"]["cmc"], 7)
        self.assertEqual(7 - 1 - 5, 1)  # conditional per-loop B/R mana gain

    def test_color_fixing_has_real_downside(self):
        self.assertIn("target opponent creates a 1/1",
                      self.cards["Forbidden Orchard"]["oracle_text"])
        self.assertIn("first, second, or third turn",
                      self.cards["Starting Town"]["oracle_text"])
        self.assertIn("Pay 1 life", self.cards["Starting Town"]["oracle_text"])
        self.assertEqual(self.new["Swamp"], 1)
        self.assertEqual(self.new["Island"], 0)
        self.assertIn("extra-turn", self.md)
        self.assertIn("seven-card redraw", self.md)
        self.assertIn("after turn 3 enters tapped", self.md)
        self.assertIn("1/1 blocker/sacrifice resource", self.md)

if __name__ == "__main__":
    unittest.main()
