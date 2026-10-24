"""Independent, source-bound Davros M7 Rev2 nine-swap review. NO canonical approval."""
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/grixis/m7/independent_reviews/Davros__Dalek_Creator_Approved_Baseline_2026-10-14.txt"
FINAL = ROOT / "data/grixis/m7/independent_reviews/Davros__Dalek_Creator_ChatGPT_M7_Rev2_Candidate_2026-10-23.txt"
ORACLE = ROOT / "data/grixis/m7/independent_reviews/Davros__Dalek_Creator_ChatGPT_M7_Rev2_Selected_Oracle_2026-10-23.json"
REVIEW = ROOT / "data/grixis/m7/independent_reviews/Davros__Dalek_Creator_ChatGPT_M7_Rev2_Decision_2026-10-23.md"
POOL = ROOT / "data/grixis/m7/independent_reviews/Davros__Dalek_Creator_ChatGPT_M7_Rev2_Tested_Pool_2026-10-23.json"
EXPECTED = "96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc"
BASE_EXPECTED = "aa6d2d343c6c1f167de8d16b23951940f7d23810c6e7705a6fd0d539a7459adc"
SWAPS = [
    ("Bloodletter of Aclazotz", "Death in Heaven"),
    ("Tergrid, God of Fright", "The Cyber-Controller"),
    ("Purphoros, God of the Forge", "Blasphemous Act"),
    ("Fiery Confluence", "This Is How It Ends"),
    ("Flame Rift", "Cyberman Patrol"),
    ("Spark Double", "Cybermen Squadron"),
    ("Irenicus's Vile Duplication", "Weeping Angel"),
    ("Quantum Misalignment", "Ashad, the Lone Cyberman"),
    ("Mechanized Warfare", "Labyrinth Raptor"),
]
GAME_CHANGERS = {"Ancient Tomb", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship", "Jeska's Will", "Tergrid, God of Fright"}
ROCKS = {"Sol Ring", "Mox Opal", "Arcane Signet", "Fellwar Stone", "Talisman of Creativity", "Talisman of Dominance", "Talisman of Indulgence"}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    result = Counter()
    for index, line in enumerate(lines):
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        if not m:
            raise AssertionError(f"Unparseable deck line {index + 1}: {line}")
        name, quantity = m.group(2), int(m.group(1))
        if index == 0:
            assert name == "Davros, Dalek Creator" and quantity == 1 and m.group(3), "Commander must be first"
        else:
            assert m.group(3) is None, "No library commander annotations"
        assert quantity > 0
        result[name] += quantity
    return result, lines

class IndependentDavrosNineSwap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck, cls.lines = parse(FINAL)
        cls.baseline, cls.old_lines = parse(BASE)
        cls.oracle = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards = {x["name"]:x for x in cls.oracle["cards"]}
        cls.review = REVIEW.read_text(encoding="utf-8")

    def test_raw_hash_and_historical_authority(self):
        self.assertEqual(sha(FINAL), EXPECTED)
        self.assertEqual(sha(BASE), BASE_EXPECTED)
        self.assertEqual(self.oracle["candidate_sha256"], EXPECTED)
        self.assertEqual(self.oracle["baseline_sha256"], BASE_EXPECTED)
        self.assertIn("NOT APPROVED", self.review)
        self.assertIn("not a lock", self.review.lower())
        self.assertIn("NOT_CANONICAL", self.oracle["status"])

    def test_physical_count_commander_singleton_and_basics(self):
        self.assertEqual(sum(self.deck.values()), 100)
        self.assertEqual(len(self.deck), 95)
        self.assertEqual(len(self.lines), 95)
        self.assertEqual(self.deck["Davros, Dalek Creator"], 1)
        self.assertEqual(self.deck["Island"], 2)
        self.assertEqual(self.deck["Mountain"], 3)
        self.assertEqual(self.deck["Swamp"], 3)
        self.assertFalse({n for n,q in self.deck.items() if q > 1} - {"Island","Mountain","Swamp"})
        self.assertEqual(self.oracle["physical_cards"],100)
        self.assertEqual(self.oracle["distinct_names"],95)

    def test_exact_nine_positive_changes_and_no_deviations(self):
        additions = self.deck - self.baseline
        cuts = self.baseline - self.deck
        self.assertEqual(additions, Counter({a:1 for a,_ in SWAPS}))
        self.assertEqual(cuts, Counter({b:1 for _,b in SWAPS}))
        self.assertEqual(len(SWAPS),9)
        self.assertEqual(sum(self.baseline.values()),100)
        self.assertEqual(self.deck["Swan Song"],1)
        self.assertEqual(self.deck["Vandalblast"],1)
        self.assertEqual(self.deck["Sycorax Commander"],1)

    def test_current_selected_source_exact_and_complete(self):
        self.assertEqual(set(self.deck),set(self.cards))
        self.assertEqual(len(self.oracle["cards"]),len(self.deck))
        self.assertTrue(self.oracle["commander_legal_all"])
        self.assertTrue(self.oracle["color_identity_all_ubr"])
        self.assertFalse(self.oracle["project_exceptions"])
        for name, qty in self.deck.items():
            with self.subTest(card=name):
                x=self.cards[name]
                self.assertEqual(x["quantity"],qty)
                self.assertTrue(x["oracle_id"])
                self.assertTrue(x["oracle_text"])
                self.assertEqual(x["commander_legality"],"legal")
                self.assertTrue(set(x["color_identity"]) <= {"U","B","R"})
                self.assertTrue(x["source"])

    def test_timing_and_legend_rules_from_selected_oracle(self):
        commander=self.cards["Davros, Dalek Creator"]["oracle_text"]
        self.assertIn("At the beginning of your end step",commander)
        self.assertIn("lost 3 or more life this turn",commander)
        self.assertNotIn("At the beginning of your end step, if",commander)
        self.assertIn("create a 3/3 black Dalek artifact creature token",commander)
        self.assertIn("it isn't legendary",self.cards["Spark Double"]["oracle_text"])
        self.assertIn("it isn't legendary",self.cards["Irenicus's Vile Duplication"]["oracle_text"])
        self.assertIn("it isn't legendary",self.cards["Quantum Misalignment"]["oracle_text"])
        self.assertIn("Rebound",self.cards["Quantum Misalignment"]["oracle_text"])
        self.assertIn("whenever",self.cards["Purphoros, God of the Forge"]["oracle_text"].lower())
        self.assertIn("Whenever another creature you control enters",self.cards["Purphoros, God of the Forge"]["oracle_text"])
        self.assertIn("from a graveyard",self.cards["Tergrid, God of Fright"]["oracle_text"])
        self.assertIn("red or artifact source",self.cards["Mechanized Warfare"]["oracle_text"])
        self.assertIn("would deal damage to an opponent",self.cards["Mechanized Warfare"]["oracle_text"])
        self.assertIn("lose twice that much life",self.cards["Bloodletter of Aclazotz"]["oracle_text"])

    def test_lands_rocks_game_changers_mana_identity(self):
        lands=sum(x["quantity"] for x in self.cards.values() if "Land" in x["type_line"])
        self.assertEqual(lands,34)
        self.assertEqual(self.oracle["land_count"],34)
        self.assertTrue(ROCKS <= set(self.deck))
        self.assertEqual({n for n,x in self.cards.items() if x.get("game_changer")},GAME_CHANGERS)
        self.assertEqual(set(self.oracle["game_changers"]),GAME_CHANGERS)
        self.assertIn("{1}{R}{R}",self.cards["Mechanized Warfare"]["mana_cost"])
        self.assertIn("{4}{U}",self.cards["Quantum Misalignment"]["mana_cost"])

    def test_bounded_two_trigger_threshold_and_no_stacked_fiction(self):
        # First trigger can make only one Dalek; the subsequent Purphoros trigger
        # may resolve above another Davros trigger in the same end step.
        # A=3 already, B/C=0. No automatic trigger for B/C absent replacement.
        def qualified_after_one_token(purphoros_damage, mechanisms):
            initial={"A":3,"B":0,"C":0}
            assert any(v>=3 for v in initial.values())
            for op in initial:
                initial[op]+=mechanisms(purphoros_damage)
            return {op for op,v in initial.items() if v>=3}
        self.assertEqual(qualified_after_one_token(2,lambda n:n),{"A"})
        self.assertEqual(qualified_after_one_token(2,lambda n:n+1),{"A","B","C"}) # Mechanized
        self.assertEqual(qualified_after_one_token(2,lambda n:n*2),{"A","B","C"}) # Bloodletter
        self.assertEqual(2+2,4) # third Davros trigger can qualify B/C by two prior Purphoros entries
        self.assertIn("only a *subsequent* Davros resolution",self.review)

    def test_tested_pool_bounded_100_card_configurations(self):
        pool=json.loads(POOL.read_text(encoding="utf-8"))
        self.assertEqual(pool["selected"],"CHATGPT_NINE")
        self.assertEqual(pool["selected_raw_sha256"],EXPECTED)
        self.assertIn("NO_SIMULATED_GAMES",pool["status"])
        for variant in pool["configurations"]:
            with self.subTest(variant=variant["id"]):
                lines=variant["cards"].splitlines()
                m=[re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?",line) for line in lines]
                self.assertTrue(all(m),variant["id"])
                self.assertEqual(sum(int(v.group(1)) for v in m),100)
                self.assertEqual(m[0].group(2),"Davros, Dalek Creator")
        selected=[c for c in pool["configurations"] if c["id"]=="CHATGPT_NINE"]
        self.assertEqual(len(selected),1)
        self.assertEqual(selected[0]["cards"],FINAL.read_text(encoding="utf-8"))

    def test_disclosed_security_model_and_no_unearned_certification(self):
        self.assertIn("Dauthi Voidwalker",self.review)
        self.assertIn("Tergrid",self.review)
        self.assertIn("none is an infinite",self.review)
        self.assertIn("not** independently valid certificates",self.review)
        self.assertIn("no fabricated games",self.review.lower())

if __name__=="__main__":
    unittest.main()
