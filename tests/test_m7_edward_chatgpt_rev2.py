"""Independent M7 Rev2 Edward Kenway exact-owner-review research checks.

This is NOT canonical owner approval. Oracle is the archived Oct23 live Scryfall
pool, not a live retest or gameplay win-rate simulation.
"""
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/grixis/m7/baseline_sources/Edward_Kenway_approved_source_2026-10-14.txt"
NEW = ROOT / "data/grixis/m7/candidate_lists/Edward_Kenway_ChatGPT_M7_Rev2_20261023.txt"
ORACLE = ROOT / "data/grixis/m7/decision_reviews/Edward_Kenway_ChatGPT_M7_Rev2_Oracle_Selected_20261023.json"
REVIEW = ROOT / "data/grixis/m7/decision_reviews/Edward_Kenway_ChatGPT_M7_Rev2_Independent_20261023.md"
EXPECTED = "8c01f2be6190be3e3af0fc5ba45eca16faa1b9346981f840811e4b63822c5ee1"
BASE_HASH = "a08d3bc9c283415f1579c493eccb3febd7d10dea3777bf3dc50cfbc0dbed4019"
COMMANDER = "Edward Kenway"
SWAPS = {
    "Mu Yanling, Wind Rider": "Breeches, Brazen Plunderer",
    "Brotherhood Vertibird": "Imposter Mech",
    "Mirkwood Bats": "Coastal Piracy",
    "Spectral Sailor": "Lotus Petal",
    "Malcolm, the Eyes": "Vaan, Street Thief",
}
KEEP = {"Fellwar Stone", "Captain Lannery Storm", "Fateful Discovery",
        "Imperial Seal", "Time Sieve", "Academy Manufactor", "The Indomitable",
        "Luxurious Locomotive", "Glint-Horn Buccaneer",
        "Malcolm, Keen-Eyed Navigator", "Roaming Throne"}
GAME_CHANGERS = {"Ancient Tomb", "Chrome Mox", "Cyclonic Rift",
                 "Fierce Guardianship", "Force of Will", "Imperial Seal",
                 "Jeska's Will", "Mana Vault", "Mox Diamond",
                 "Vampiric Tutor"}
ROCKS = {"Sol Ring", "Arcane Signet", "Fellwar Stone", "Mana Vault",
         "Talisman of Creativity", "Talisman of Dominance",
         "Talisman of Indulgence"}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    cards = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        assert m, (i+1, line)
        name, qty = m[2], int(m[1])
        if i == 0:
            assert (name, qty, bool(m[3])) == (COMMANDER, 1, True)
        else:
            assert m[3] is None
        cards[name] += qty
    return cards, lines

class EdwardRev2Research(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current, cls.lines = parse(NEW)
        cls.old, _ = parse(BASE)
        cls.oracle = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.evidence = {x["name"]: x for x in cls.oracle["cards"]}

    def test_source_raw_hashes_and_research_status(self):
        self.assertEqual(sha(NEW), EXPECTED)
        self.assertEqual(sha(BASE), BASE_HASH)
        self.assertEqual(self.oracle["candidate_raw_sha256"], EXPECTED)
        self.assertEqual(self.oracle["baseline_raw_sha256"], BASE_HASH)
        self.assertIn("NOT_OWNER_APPROVED", self.oracle["status"])
        self.assertIn(EXPECTED, REVIEW.read_text(encoding="utf-8"))

    def test_100_count_singleton_and_five_real_swaps(self):
        self.assertEqual(sum(self.current.values()), 100)
        self.assertEqual(len(self.current), 98)
        self.assertEqual(len(self.lines), 98)
        for name, n in self.current.items():
            expected = 2 if name in {"Island", "Swamp"} else 1
            self.assertEqual(n, expected, name)
        self.assertEqual(set(self.current)-set(self.old), set(SWAPS))
        self.assertEqual(set(self.old)-set(self.current), set(SWAPS.values()))
        self.assertTrue(KEEP <= self.current.keys())
        for name in KEEP:
            self.assertEqual(self.current[name], self.old[name])

    def test_all_98_oracle_identity_and_legality(self):
        self.assertEqual(set(self.current), set(self.evidence))
        self.assertEqual(sum(n for name,n in self.current.items()
                             if "Land" in self.evidence[name]["type_line"]), 35)
        self.assertEqual({name for name in self.current
                          if self.evidence[name].get("game_changer")}, GAME_CHANGERS)
        self.assertTrue(ROCKS <= self.current.keys())
        self.assertEqual(len(ROCKS), 7)
        vehicles = [n for n in self.current
                    if "Vehicle" in self.evidence[n]["type_line"]]
        qualifiers = [n for n in self.current
                      if "Creature" in self.evidence[n]["type_line"]
                      and ("Pirate" in self.evidence[n]["type_line"]
                           or "Assassin" in self.evidence[n]["type_line"])]
        self.assertEqual(len(vehicles), 13)
        self.assertEqual(len(qualifiers), 22)
        for name, qty in self.current.items():
            evidence=self.evidence[name]
            self.assertEqual(evidence["quantity"], qty)
            self.assertEqual(evidence["commander_legality"], "legal", name)
            self.assertTrue(set(evidence["color_identity"]) <= set("UBR"), name)
            self.assertTrue(evidence.get("oracle_id"), name)
        self.assertEqual(self.oracle["project_exceptions"], [])

    def test_theft_token_vehicle_oracle_mechanics(self):
        txt=lambda n:self.evidence[n]["oracle_text"]
        self.assertIn("At the beginning of your end step", txt(COMMANDER))
        self.assertIn("Whenever a Vehicle you control deals combat damage", txt(COMMANDER))
        self.assertIn("Vehicles you control have flying", txt("Mu Yanling, Wind Rider"))
        self.assertIn("Brotherhood Vertibird's power is equal", txt("Brotherhood Vertibird"))
        self.assertIn("Whenever you create or sacrifice a token", txt("Mirkwood Bats"))
        self.assertIn("{3}{U}: Draw a card", txt("Spectral Sailor"))
        self.assertIn("cast your second spell each turn", txt("Malcolm, the Eyes"))
        self.assertIn("Whenever Captain Lannery Storm attacks", txt("Captain Lannery Storm"))
        self.assertIn("Whenever an artifact you control enters, draw a card",
                      txt("Fateful Discovery"))

if __name__ == "__main__":
    unittest.main()
