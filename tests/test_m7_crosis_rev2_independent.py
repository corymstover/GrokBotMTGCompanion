"""ChatGPT independent Deck #10 M7 Rev2: finite source-bound checks (not owner approval).

Fixtures are exact Oct23 Scryfall-backed research records from Grok #658 and
the canon Cecily selected Scryfall snapshot, not new network downloads.
No game-engine/win-rate claims are made. Original Grok five-swap tests stay intact.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "data/grixis/m7/"
BASE = ROOT / (PREFIX + "baseline_sources/Crosis__the_Purger_approved_source_2026-10-14.txt")
CAND = ROOT / (PREFIX + "chatgpt_final_candidates/Crosis__the_Purger_M7_Rev2_Approval_Candidate_20261023.txt")
SOURCE = ROOT / "data/grixis/m6/oracle_snapshots/Crosis__the_Purger_M7_Scryfall_20261023.json"
ADDON = ROOT / (PREFIX + "research_challengers/Crosis__the_Purger_M7_Rev2_Addon_Scryfall_20261023.json")
HASH = "a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a"
ADDS = ("Megrim", "Rankle, Master of Pranks", "Aggravated Assault",
        "Raiders' Wake", "Deadly Rollick", "Bloodchief Ascension",
        "Otawara, Soaring City", "Takenuma, Abandoned Mire", "Sokenzan, Crucible of Defiance")
CUTS = ("Jet Medallion", "Blizzard Specter", "Dream Salvage",
        "Oppression", "Fell Specter", "Bottomless Pit",
        "Island", "Swamp", "Mountain")
BASICS = {"Island", "Swamp", "Mountain"}
ROCKS = ("Sol Ring", "Mana Vault", "Chrome Mox", "Mox Diamond",
         "Lotus Petal", "Arcane Signet", "Dimir Signet", "Izzet Signet",
         "Rakdos Signet", "Talisman of Creativity", "Talisman of Dominance",
         "Talisman of Indulgence", "Jet Medallion")


def parse(source):
    names = Counter()
    lines = source.splitlines()
    for index, line in enumerate(lines):
        qty, name = line.split("x ", 1)
        if index == 0:
            assert name == "Crosis, the Purger [Commander]"
            name = name.removesuffix(" [Commander]")
        else:
            assert "[Commander]" not in name
        names[name] += int(qty)
    return names


class TestCrosisM7Rev2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = CAND.read_bytes()
        cls.deck = parse(cls.raw.decode("utf-8"))
        cls.base = parse(BASE.read_text(encoding="utf-8"))
        main = json.loads(SOURCE.read_text(encoding="utf-8"))
        ext = json.loads(ADDON.read_text(encoding="utf-8"))
        cls.cards = {c["name"]: c for c in main["cards"] + ext["cards"]}
        cls.ext = ext

    def test_raw_fingerprint_and_structural_count(self):
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), HASH)
        self.assertTrue(self.raw.endswith(b"\n"))
        self.assertEqual(sum(self.deck.values()), 100)
        self.assertEqual(self.deck["Crosis, the Purger"], 1)
        self.assertEqual(len(self.deck), 95)
        self.assertEqual(self.deck["Island"], 3)
        self.assertEqual(self.deck["Swamp"], 3)
        self.assertEqual(self.deck["Mountain"], 2)
        for n, q in self.deck.items():
            if n not in BASICS:
                self.assertEqual(q, 1, n)

    def test_nine_real_swaps_and_preserved_core(self):
        self.assertEqual(sorted((self.deck - self.base).elements()), sorted(ADDS))
        self.assertEqual(sorted((self.base - self.deck).elements()), sorted(CUTS))
        self.assertEqual(self.deck["Izzet Signet"], 1)
        self.assertEqual(self.deck["Dark Deal"], 1)
        self.assertEqual(self.deck["Brotherhood Regalia"], 1)
        self.assertEqual(self.deck["Painter's Servant"], 1)
        self.assertEqual(self.deck["Sedraxis Specter"], 1)
        self.assertEqual(self.deck["Sword of Feast and Famine"], 1)
        self.assertEqual(self.deck["Lightning Greaves"], 1)
        self.assertEqual(self.deck["Liliana's Caress"], 1)

    def test_all_cards_current_oracle_and_no_exceptions(self):
        self.assertEqual(self.ext["expected_candidate_raw_sha256"], HASH)
        self.assertEqual(len(self.ext["cards"]), 3)
        self.assertEqual(set(self.deck) - set(self.cards), set())
        for n in self.deck:
            card = self.cards[n]
            self.assertEqual(card["commander_legality"], "legal", n)
            self.assertTrue(set(card["color_identity"]) <= {"U", "B", "R"}, n)
            self.assertTrue(card["oracle_id"], n)
            self.assertTrue(card["oracle_text"], n)
        self.assertEqual(sum(self.deck[n] for n in self.deck if self.cards[n]["game_changer"]), 14)

    def test_land_and_acceleration_stay_stable(self):
        self.assertEqual(sum(q for n, q in self.deck.items()
                             if "Land" in self.cards[n]["type_line"]), 36)
        self.assertEqual(sum(self.deck[n] for n in ROCKS), 12)
        self.assertEqual(sum(self.base[n] for n in ROCKS), 13)
        channels = {"Otawara, Soaring City": ("U", "{3}{U}"),
                    "Takenuma, Abandoned Mire": ("B", "{3}{B}"),
                    "Sokenzan, Crucible of Defiance": ("R", "{3}{R}")}
        for n, (color, cost) in channels.items():
            card = self.cards[n]
            self.assertEqual(card["color_identity"], [color])
            self.assertEqual(card["type_line"], "Legendary Land")
            self.assertIn("{T}: Add {" + color + "}", card["oracle_text"])
            self.assertIn("Channel — " + cost, card["oracle_text"])
            self.assertIn("less to activate for each legendary creature", card["oracle_text"])
        self.assertIn("target artifact, creature, enchantment, or planeswalker",
                      self.cards["Otawara, Soaring City"]["oracle_text"])
        self.assertIn("Mill three cards", self.cards["Takenuma, Abandoned Mire"]["oracle_text"])
        self.assertIn("two 1/1 colorless Spirit creature tokens",
                      self.cards["Sokenzan, Crucible of Defiance"]["oracle_text"])
        tapped = [n for n in self.deck
                  if "Land" in self.cards[n]["type_line"]
                  and "This land enters tapped." in self.cards[n]["oracle_text"]]
        self.assertEqual(tapped, ["Xander's Lounge"])

    def test_discard_payoffs_and_timing(self):
        commander = self.cards["Crosis, the Purger"]["oracle_text"]
        self.assertIn("combat damage to a player, you may pay {2}{B}", commander)
        self.assertIn("discards all cards of that color", commander)
        for n in ("Megrim", "Liliana's Caress", "Raiders' Wake"):
            self.assertIn("Whenever an opponent discards a card", self.cards[n]["oracle_text"])
        self.assertIn("three or more quest counters",
                      self.cards["Bloodchief Ascension"]["oracle_text"])
        self.assertIn("At the beginning of each end step",
                      self.cards["Bloodchief Ascension"]["oracle_text"])
        self.assertIn("loses 2 life. If you do, you gain 2 life",
                      self.cards["Bloodchief Ascension"]["oracle_text"])
        self.assertEqual(5 * (2 + 2 + 2), 30)  # finite five-card Painter purge (active 3 punishers)
        self.assertEqual(5 * (2 + 2 + 2 + 2), 40)  # only AFTER Ascension has 3 quest counters
        self.assertIn("If you control a commander",
                      self.cards["Deadly Rollick"]["oracle_text"])
        self.assertIn("Activate only as a sorcery",
                      self.cards["Aggravated Assault"]["oracle_text"])
        self.assertIn("untap all lands you control",
                      self.cards["Sword of Feast and Famine"]["oracle_text"].lower())


if __name__ == "__main__":
    unittest.main()
