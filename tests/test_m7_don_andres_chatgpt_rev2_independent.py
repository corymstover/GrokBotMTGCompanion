"""Independent source-bound Don Andres M7 Rev2 seven-swap research, NOT an owner approval."""
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "data/grixis/m7/independent_reviews"
BASE = DIR / "Don_Andres__the_Renegade_Approved_Baseline_2026-10-14.txt"
FINAL = DIR / "Don_Andres__the_Renegade_ChatGPT_M7_Rev2_Candidate_2026-10-23.txt"
ORACLE = DIR / "Don_Andres__the_Renegade_ChatGPT_M7_Rev2_Selected_Oracle_2026-10-23.json"
REVIEW = DIR / "Don_Andres__the_Renegade_ChatGPT_M7_Rev2_Decision_2026-10-23.md"
POOL = DIR / "Don_Andres__the_Renegade_ChatGPT_M7_Rev2_Tested_Pool_2026-10-23.json"
EXACT = "59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f"
HISTORIC = "a6022fddd295d7c671690fbce5e25dc6fed47ca7fa77bf1d8a86ebadb2d927bb"
COMMANDER = "Don Andres, the Renegade"
SWAPS = [
    ("Gríma, Saruman's Footman", "Professional Face-Breaker"),
    ("Fallen Shinobi", "Seize the Spotlight"),
    ("Treachery", "Blasphemous Act"),
    ("Gloomlake Verge", "Shipwreck Marsh"),
    ("Blazemire Verge", "Smoldering Marsh"),
    ("Mind's Dilation", "Stolen Strategy"),
    ("Passionate Archaeologist", "Breeches, Eager Pillager"),
]
ROCKS = {"Arcane Signet", "Dimir Signet", "Fellwar Stone", "Izzet Signet",
         "Rakdos Signet", "Sol Ring", "Talisman of Creativity",
         "Talisman of Dominance", "Talisman of Indulgence"}
GAME_CHANGERS = {"Ancient Tomb", "Cyclonic Rift", "Fierce Guardianship",
                 "Opposition Agent", "Vampiric Tutor"}

def sha(content):
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

def parse(content):
    cards = Counter()
    lines = content.splitlines()
    for i, l in enumerate(lines):
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", l)
        if not m: raise AssertionError("Bad line %s: %s" % (i+1,l))
        quantity,name,tag=int(m.group(1)),m.group(2),m.group(3)
        if i == 0:
            assert name == COMMANDER and quantity == 1 and tag
        else:
            assert tag is None
        assert quantity >= 1
        cards[name] += quantity
    return cards, lines

class IndependentDonAndresM7Rev2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = FINAL.read_text(encoding="utf-8")
        cls.old_raw = BASE.read_text(encoding="utf-8")
        cls.deck, cls.lines = parse(cls.raw)
        cls.old, _ = parse(cls.old_raw)
        cls.oracle = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards = {x["name"]:x for x in cls.oracle["cards"]}
        cls.old_oracle = {x["name"]:x for x in cls.oracle["adversarial_source_cards"]}
        cls.pool = json.loads(POOL.read_text(encoding="utf-8"))
        cls.review = REVIEW.read_text(encoding="utf-8")

    def test_raw_hash_immutability_and_status(self):
        self.assertEqual(sha(self.raw), EXACT)
        self.assertEqual(sha(self.old_raw), HISTORIC)
        self.assertTrue(self.raw.endswith("\n"))
        self.assertEqual(self.oracle["candidate_sha256"], EXACT)
        self.assertEqual(self.oracle["baseline_sha256"], HISTORIC)
        self.assertIn("NOT_OWNER_APPROVED_NOT_CANONICAL", self.oracle["status"])
        self.assertIn("NOT APPROVED", self.review)
        self.assertIn("NOT CANONICAL", self.review)

    def test_100_physical_and_only_island_repeated(self):
        self.assertEqual(sum(self.deck.values()), 100)
        self.assertEqual(len(self.lines), 99)
        self.assertEqual(len(self.deck), 99)
        self.assertEqual(self.deck[COMMANDER], 1)
        self.assertEqual({n:q for n,q in self.deck.items() if q > 1}, {"Island": 2})
        self.assertEqual(self.oracle["physical_cards"], 100)
        self.assertEqual(self.oracle["distinct_names"], 99)
        self.assertEqual(sum(self.old.values()),100)

    def test_seven_positive_swaps_not_cap_and_retained_core(self):
        self.assertEqual(len(SWAPS),7)
        self.assertEqual(self.deck-self.old, Counter({a:1 for a,_ in SWAPS}))
        self.assertEqual(self.old-self.deck, Counter({b:1 for _,b in SWAPS}))
        for n in ("Thieving Amalgam", "Jhoira, Weatherlight Corsair",
                  "Insurrection", "Gonti, Night Minister", "Roaming Throne",
                  "Wand of Wonder", "Kindred Discovery"):
            self.assertEqual(self.deck[n],1)

    def test_card_sources_legal_color_and_actual_game_changers(self):
        self.assertEqual(set(self.deck),set(self.cards))
        self.assertEqual(len(self.cards),99)
        self.assertTrue(self.oracle["commander_legal_all"])
        self.assertTrue(self.oracle["color_identity_all_ubr"])
        self.assertEqual(self.oracle["project_exceptions"],[])
        for n,q in self.deck.items():
            with self.subTest(card=n):
                x=self.cards[n]
                self.assertEqual(x["quantity"],q)
                self.assertEqual(x["commander_legality"],"legal")
                self.assertTrue(x["oracle_id"] and x["oracle_text"])
                self.assertTrue(set(x["color_identity"]) <= {"U","B","R"})
                self.assertIn("Scryfall",x["source"])
        self.assertEqual({n for n,c in self.cards.items() if c["game_changer"]}, GAME_CHANGERS)
        self.assertEqual(set(self.oracle["game_changers"]), GAME_CHANGERS)

    def test_35_lands_nine_rocks_and_color_payability(self):
        lands = sum(x["quantity"] for x in self.cards.values() if "Land" in x["type_line"])
        self.assertEqual(lands,35)
        self.assertEqual(self.oracle["land_count"],35)
        self.assertEqual(set(self.deck) & ROCKS, ROCKS)
        self.assertEqual(set(self.oracle["mana_rocks"]), ROCKS)
        self.assertEqual(self.cards["Blazemire Verge"]["color_identity"],["B","R"])
        self.assertEqual(self.cards["Gloomlake Verge"]["color_identity"],["B","U"])

    def test_corrected_shipwreck_other_lands_not_basics(self):
        shipwreck=self.old_oracle["Shipwreck Marsh"]["oracle_text"]
        self.assertIn("two or more other lands",shipwreck)
        self.assertNotIn("two or more basic lands",shipwreck)
        self.assertIn("two or more basic lands",self.old_oracle["Smoldering Marsh"]["oracle_text"])
        self.assertIn("control an Island or a Swamp",self.cards["Gloomlake Verge"]["oracle_text"])
        self.assertIn("control a Swamp or a Mountain",self.cards["Blazemire Verge"]["oracle_text"])
        self.assertIn("Shipwreck Marsh needs two BASIC lands is false",self.review)
        self.assertIn("Gloomlake Verge",self.review)

    def test_owner_cast_and_background_actual_mechanics(self):
        don=self.cards[COMMANDER]["oracle_text"]
        self.assertIn("creature you control but don't own",don)
        self.assertIn("a noncreature spell you don't own",don)
        self.assertIn("two tapped Treasure tokens",don)
        archaeologist=self.cards["Passionate Archaeologist"]["oracle_text"]
        self.assertIn("Commander creatures you own",archaeologist)
        self.assertIn("Whenever you cast a spell from exile",archaeologist)
        self.assertIn("mana value to target opponent",archaeologist)
        self.assertIn("Legendary Enchantment",self.cards["Passionate Archaeologist"]["type_line"])
        self.assertIn("their first spell each turn",self.cards["Mind's Dilation"]["oracle_text"])
        self.assertIn("without paying its mana cost",self.cards["Mind's Dilation"]["oracle_text"])
        self.assertIn("Gríma can't be blocked",self.cards["Gríma, Saruman's Footman"]["oracle_text"])
        self.assertIn("Ninjutsu",self.cards["Fallen Shinobi"]["oracle_text"])
        self.assertIn("untap up to five lands",self.cards["Treachery"]["oracle_text"])
        self.assertIn("triggers an additional time",self.cards["Roaming Throne"]["oracle_text"])

    def test_bounded_case_three_opponent_stolen_spells(self):
        # This is a conditional trace, not a predicted encounter or win rate.
        def resulting_value(casts):
            # Each input is (owner, kind, mana value, cast from exile)
            tapped_treasures=sum(2 for owner,kind,cmc,exile in casts
                                 if owner == "opponent" and kind != "Creature")
            archaeologist_damage=sum(cmc for _,_,cmc,exile in casts if exile)
            return tapped_treasures,archaeologist_damage
        cases=[("opponent","Sorcery",2,True),
               ("opponent","Creature",4,True),
               ("opponent","Instant",6,True)]
        self.assertEqual(resulting_value(cases),(4,12))
        self.assertEqual(resulting_value([]),(0,0))
        # Copying a spell without casting doesn't appear in the cast list.
        self.assertEqual(resulting_value([("self","Sorcery",4,True)]),(0,4))
        self.assertIn("tapped",self.review.lower())
        self.assertIn("No matched-opening multiplayer sample",self.review)

    def test_complete_100_counterfactuals_no_fabricated_simulations(self):
        self.assertEqual(self.pool["selected"],"CHATGPT_SEVEN_SELECTED")
        self.assertEqual(self.pool["selected_raw_sha256"],EXACT)
        self.assertIn("NO_MATCHED_OPENING_GAMES",self.pool["status"])
        self.assertGreaterEqual(len(self.pool["configurations"]),9)
        for v in self.pool["configurations"]:
            with self.subTest(variant=v["id"]):
                parsed,lines=parse(v["cards"])
                self.assertEqual(sum(parsed.values()),100)
                self.assertEqual(len(parsed),99)
                self.assertEqual(sha(v["cards"]),v["raw_sha256"])
        self.assertEqual([v["cards"] for v in self.pool["configurations"]
                          if v["id"]=="CHATGPT_SEVEN_SELECTED"],[self.raw])

    def test_owner_rejected_classes_and_research_gate(self):
        for name in ("Bribery", "Agent of Treachery", "Zara, Renegade Recruiter",
                     "Memory Plunder", "Cunning Rhetoric", "The Ruinous Powers"):
            self.assertNotIn(name,self.deck)
        self.assertIn("owner",self.review.lower())
        self.assertIn("No newly independent third-model Pass C",self.review)

if __name__ == "__main__":
    unittest.main()
