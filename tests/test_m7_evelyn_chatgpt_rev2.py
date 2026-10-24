"""Independent Evelyn cEDH M7 second-pass research confirmation (not approval).

Archived Oct23 live Scryfall evidence; deterministic singleton and Oracle gates.
No third-model independence, game simulation, or blanket full-suite pass claim.
"""
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/grixis/m7/baseline_sources/Evelyn__the_Covetous_approved_source_2026-10-14.txt"
NEW = ROOT / "data/grixis/m7/candidate_lists/Evelyn__the_Covetous_ChatGPT_M7_Rev2_Confirmed_20261023.txt"
ORACLE = ROOT / "data/grixis/m7/decision_reviews/Evelyn__the_Covetous_ChatGPT_M7_Rev2_Oracle_Selected_20261023.json"
REVIEW = ROOT / "data/grixis/m7/decision_reviews/Evelyn__the_Covetous_ChatGPT_M7_Rev2_Independent_20261023.md"
SHA = "c3f6862c6f4498778069f45e7a5e5bc7efe92d70158b5e9b3f438c8c861b89ac"
OLD = "1d602b5d9b2a370d3448816f593198212b2b83da74e92ccc3232798641b2588a"
SWAPS = {
    "Marsh Flats": "Thundering Falls",
    "Insolent Neonate": "Spellskite",
    "Brainstorm": "Redirect Lightning",
    "Burnt Offering": "Wan Shi Tong, Librarian",
    "Verdant Catacombs": "Blazemire Verge",
}
KEEP = {"Vexing Bauble", "Ripples of Undeath", "Saw in Half",
        "Windfall", "Notion Thief", "Stifle", "Mistrise Village",
        "Leyline of Anticipation", "Thassa's Oracle", "Underworld Breach",
        "Worldgorger Dragon", "Animate Dead", "Dance of the Dead", "Necromancy"}
GAME_CHANGERS = {
    "Ad Nauseam", "Ancient Tomb", "Chrome Mox", "Demonic Tutor",
    "Force of Will", "Gamble", "Imperial Seal", "Lion's Eye Diamond",
    "Mana Vault", "Mox Diamond", "Mystical Tutor", "Necropotence",
    "Notion Thief", "Opposition Agent", "Orcish Bowmasters",
    "Rhystic Study", "Thassa's Oracle", "Underworld Breach", "Vampiric Tutor"
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    cards = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        assert m, (i + 1, line)
        qty, name, marker = int(m[1]), m[2], m[3]
        if i == 0:
            assert (qty, name, bool(marker)) == (1, "Evelyn, the Covetous", True)
        else:
            assert marker is None
        cards[name] += qty
    return cards, lines

class EvelynM7IndependentConfirmation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards, cls.lines = parse(NEW)
        cls.old, _ = parse(BASE)
        cls.oracle = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.ev = {x["name"]: x for x in cls.oracle["cards"]}

    def test_source_and_candidate_raw_hashes(self):
        self.assertEqual(digest(BASE), OLD)
        self.assertEqual(digest(NEW), SHA)
        self.assertEqual(self.oracle["baseline_raw_sha256"], OLD)
        self.assertEqual(self.oracle["candidate_raw_sha256"], SHA)
        self.assertIn("NOT_OWNER_APPROVED", self.oracle["status"])
        self.assertIn(SHA, REVIEW.read_text(encoding="utf-8"))

    def test_exact_100_unique_and_five_swaps(self):
        self.assertEqual(len(self.lines), 100)
        self.assertEqual(sum(self.cards.values()), 100)
        self.assertEqual(len(self.cards), 100)
        self.assertTrue(all(qty == 1 for qty in self.cards.values()))
        self.assertEqual(set(self.cards) - set(self.old), set(SWAPS))
        self.assertEqual(set(self.old) - set(self.cards), set(SWAPS.values()))
        self.assertTrue(KEEP <= self.cards.keys())

    def test_scryfall_color_legality_lands_and_game_changers(self):
        self.assertEqual(set(self.cards), set(self.ev))
        self.assertEqual(sum(q for n, q in self.cards.items()
                             if "Land" in self.ev[n]["type_line"]), 26)
        self.assertEqual({n for n in self.cards
                          if self.ev[n].get("game_changer")}, GAME_CHANGERS)
        for name, qty in self.cards.items():
            c = self.ev[name]
            self.assertEqual(c["quantity"], qty)
            self.assertEqual(c["commander_legality"], "legal", name)
            self.assertTrue(set(c["color_identity"]) <= set("UBR"), name)
            self.assertTrue(c["oracle_id"], name)
        self.assertEqual(self.oracle["project_exceptions"], [])

    def test_evelyn_two_vampires_and_mechanics(self):
        vampire_names = [n for n in self.cards
                         if "Vampire" in self.ev[n]["type_line"]]
        self.assertEqual(set(vampire_names),
                         {"Evelyn, the Covetous", "Insolent Neonate"})
        txt = lambda n: self.ev[n]["oracle_text"]
        self.assertIn("Whenever Evelyn or another Vampire you control enters",
                      txt("Evelyn, the Covetous"))
        self.assertIn("Once each turn, you may play a card",
                      txt("Evelyn, the Covetous"))
        self.assertIn("Discard a card, Sacrifice this creature: Draw a card",
                      txt("Insolent Neonate"))
        self.assertIn("As an additional cost to cast this spell, sacrifice a creature",
                      txt("Burnt Offering"))
        self.assertIn("Draw three cards, then put two cards",
                      txt("Brainstorm"))
        self.assertIn("Search your library for a Plains or Swamp",
                      txt("Marsh Flats"))
        self.assertIn("Search your library for a Swamp or Forest",
                      txt("Verdant Catacombs"))

if __name__ == "__main__":
    unittest.main()
