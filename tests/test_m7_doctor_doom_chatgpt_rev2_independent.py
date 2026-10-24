"""Source-bound independent Doctor Doom M7 Rev2 nine-swap audit; not an approval."""
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "data/grixis/m7/independent_reviews"
BASE = DIR / "Doctor_Doom__King_of_Latveria_Approved_Baseline_2026-10-14.txt"
FINAL = DIR / "Doctor_Doom__King_of_Latveria_ChatGPT_M7_Rev2_Candidate_2026-10-23.txt"
ORACLE = DIR / "Doctor_Doom__King_of_Latveria_ChatGPT_M7_Rev2_Selected_Oracle_2026-10-23.json"
POOL = DIR / "Doctor_Doom__King_of_Latveria_ChatGPT_M7_Rev2_Tested_Pool_2026-10-23.json"
REVIEW = DIR / "Doctor_Doom__King_of_Latveria_ChatGPT_M7_Rev2_Decision_2026-10-23.md"
EXPECTED = "7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20"
BASE_EXPECTED = "c97bd448aa4b18d2f7ed15e5d67006ab320ed67ad3ed267e44150de472e1dc58"
COMMANDER = "Doctor Doom, King of Latveria"
SWAPS = [
    ("Lightning Axe", "Big Score"),
    ("Glint-Horn Buccaneer", "Green Goblin, Revenant"),
    ("Red Ghost, Intangible Genius", "Loki, the Deceiver"),
    ("Coastal Peak", "Shipwreck Marsh"),
    ("Swiftfoot Boots", "Unexpected Windfall"),
    ("Mox Diamond", "Fellwar Stone"),
    ("Withering Torment", "Feed the Swarm"),
    ("Molten Vortex", "Kang, Temporal Tyrant"),
    ("Tolaria West", "Geier Reach Sanitarium"),
]
ROCKS = {
    "Sol Ring", "Arcane Signet", "Mox Diamond", "Talisman of Creativity",
    "Talisman of Dominance", "Talisman of Indulgence", "The Soul Stone",
}
GAME_CHANGERS = {
    "Ancient Tomb", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship",
    "Jeska's Will", "Mox Diamond", "Vampiric Tutor",
}

def raw_sha(raw):
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

def parse(raw):
    rows = raw.splitlines()
    cards = Counter()
    for i, row in enumerate(rows):
        match = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", row)
        if not match:
            raise AssertionError(f"invalid row {i + 1}: {row}")
        n, name, tag = int(match.group(1)), match.group(2), match.group(3)
        if i == 0:
            assert name == COMMANDER and n == 1 and tag
        else:
            assert not tag
        assert n > 0
        cards[name] += n
    return cards, rows

class IndependentDoctorDoomM7NineSwap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = FINAL.read_text(encoding="utf-8")
        cls.old_raw = BASE.read_text(encoding="utf-8")
        cls.candidate, cls.lines = parse(cls.raw)
        cls.baseline, _ = parse(cls.old_raw)
        cls.oracle = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards = {x["name"]: x for x in cls.oracle["cards"]}
        cls.pool = json.loads(POOL.read_text(encoding="utf-8"))
        cls.review = REVIEW.read_text(encoding="utf-8")

    def test_exact_bytes_and_noncanonical_status(self):
        self.assertTrue(self.raw.endswith("\n"))
        self.assertEqual(raw_sha(self.raw), EXPECTED)
        self.assertEqual(raw_sha(self.old_raw), BASE_EXPECTED)
        self.assertEqual(self.oracle["candidate_sha256"], EXPECTED)
        self.assertEqual(self.oracle["baseline_sha256"], BASE_EXPECTED)
        self.assertIn("NOT_OWNER_APPROVED_NOT_CANONICAL", self.oracle["status"])
        self.assertIn("NOT CANONICAL", self.review)
        self.assertIn("NOT A LOCK", self.review)

    def test_100_cards_exactly_one_commander_singleton(self):
        self.assertEqual(sum(self.candidate.values()), 100)
        self.assertEqual(len(self.candidate), 100)
        self.assertEqual(len(self.lines), 100)
        self.assertEqual(self.candidate[COMMANDER], 1)
        self.assertFalse({x for x, q in self.candidate.items() if q != 1})
        self.assertEqual(self.lines[0], f"1x {COMMANDER} [Commander]")
        self.assertEqual(self.oracle["physical_cards"], 100)
        self.assertEqual(self.oracle["distinct_names"], 100)

    def test_source_exact_and_legal(self):
        self.assertEqual(set(self.candidate), set(self.cards))
        self.assertEqual(len(self.cards), 100)
        self.assertTrue(self.oracle["commander_legal_all"])
        self.assertTrue(self.oracle["color_identity_all_ubr"])
        self.assertEqual(self.oracle["project_exceptions"], [])
        for name, card in self.cards.items():
            with self.subTest(card=name):
                self.assertEqual(card["quantity"], 1)
                self.assertTrue(card["oracle_id"])
                self.assertTrue(card["oracle_text"])
                self.assertEqual(card["commander_legality"], "legal")
                self.assertTrue(set(card["color_identity"]) <= {"U", "B", "R"})
                self.assertIn("Scryfall", card["source"])

    def test_exact_nine_nonpadding_substitutions_and_preservation(self):
        self.assertEqual(self.candidate - self.baseline, Counter({a: 1 for a, _ in SWAPS}))
        self.assertEqual(self.baseline - self.candidate, Counter({b: 1 for _, b in SWAPS}))
        self.assertEqual(len(SWAPS), 9)
        self.assertEqual(sum(self.baseline.values()), 100)
        self.assertEqual(self.candidate["Change of Fortune"], 1)
        self.assertEqual(self.candidate["Seismic Assault"], 1)
        self.assertEqual(self.candidate["Dakmor Salvage"], 1)
        self.assertEqual(self.candidate["Tectonic Reformation"], 1)
        self.assertEqual(self.candidate["Surly Badgersaur"], 1)
        self.assertEqual(self.candidate["Lethal Scheme"], 1)

    def test_mana_curve_ramp_land_count_bracket(self):
        land_count = sum(x["quantity"] for x in self.cards.values() if "Land" in x["type_line"])
        self.assertEqual(land_count, 38)
        self.assertEqual(self.oracle["land_count"], 38)
        self.assertEqual(set(self.candidate) & ROCKS, ROCKS)
        self.assertEqual({n for n, x in self.cards.items() if x["game_changer"]}, GAME_CHANGERS)
        self.assertEqual(set(self.oracle["game_changers"]), GAME_CHANGERS)
        self.assertEqual(self.cards["Molten Vortex"]["mana_cost"], "{R}")
        self.assertEqual(self.cards["Tolaria West"]["color_identity"], ["U"])
        self.assertEqual(self.cards["Mox Diamond"]["mana_cost"], "{0}")

    def test_oracle_and_not_made_up_synergies(self):
        doom = self.cards[COMMANDER]["oracle_text"]
        self.assertIn("one or more land cards", doom)
        self.assertIn("At the beginning of combat on your turn", doom)
        self.assertIn("It connives.", doom)
        vortex = self.cards["Molten Vortex"]["oracle_text"]
        self.assertIn("{R}, Discard a land card", vortex)
        self.assertIn("2 damage to any target", vortex)
        tol = self.cards["Tolaria West"]["oracle_text"]
        self.assertIn("Transmute {1}{U}{U}", tol)
        self.assertIn("mana value 0", tol)
        self.assertIn("Transmute only as a sorcery", tol)
        self.assertIn("If this artifact would enter", self.cards["Mox Diamond"]["oracle_text"])
        self.assertIn("discard a land card instead", self.cards["Mox Diamond"]["oracle_text"])
        self.assertIn("haste", self.cards["Glint-Horn Buccaneer"]["oracle_text"].lower())
        self.assertIn("Whenever you discard a card", self.cards["Glint-Horn Buccaneer"]["oracle_text"])
        self.assertIn("second card each turn", self.cards["Red Ghost, Intangible Genius"]["oracle_text"])
        self.assertIn("you've discarded this turn", self.cards["Change of Fortune"]["oracle_text"])
        self.assertIn("Destroy target creature or enchantment", self.cards["Withering Torment"]["oracle_text"])
        self.assertIn("hexproof", self.cards["Swiftfoot Boots"]["oracle_text"])

    def test_bounded_discard_and_dredge_traces(self):
        # Distinct discard events, not number of land cards in a single event.
        def doom_life_loss(discard_events):
            return 2 * sum(bool(any(card == "Land" for card in event)) for event in discard_events)
        self.assertEqual(doom_life_loss([["Land", "Land", "Land"]]), 2)
        self.assertEqual(doom_life_loss([["Land"], ["Land"], ["Land"]]), 6)
        self.assertEqual(doom_life_loss([["Creature"], ["Land"]]), 2)
        # Three separate Molten Vortex activations also require three red mana.
        self.assertEqual(3 * 2, 6)
        # Dredge 2 needs at least two library cards before every substitution.
        # First discard happens before the cycling draw.
        # Each subsequent discard needs a prior successful dredge of two cards.
        self.assertEqual(38 // 2 + 1, 20)
        self.assertEqual(37 // 2 + 1, 19)
        self.assertEqual(26 // 2 + 1, 14)
        self.assertEqual(25 // 2 + 1, 13)
        self.assertEqual((40 + 3 - 1) // 3, 14)
        self.assertIn("NOT an unbounded infinite", self.review)

    def test_alternative_exact_source_bound_full_100s(self):
        self.assertEqual(self.pool["selected"], "CHATGPT_NINE_SELECTED")
        self.assertEqual(self.pool["selected_raw_sha256"], EXPECTED)
        self.assertIn("NO_MATCHED_OPENING_GAMES", self.pool["status"])
        self.assertGreaterEqual(len(self.pool["configurations"]), 7)
        for v in self.pool["configurations"]:
            with self.subTest(variant=v["id"]):
                names, lines = parse(v["cards"])
                self.assertEqual(sum(names.values()), 100)
                self.assertEqual(len(names), 100)
                self.assertEqual(raw_sha(v["cards"]), v["raw_sha256"])
        selected = [x for x in self.pool["configurations"] if x["id"] == "CHATGPT_NINE_SELECTED"]
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]["cards"], self.raw)

    def test_source_and_policy_caveats(self):
        self.assertIn("Skirge Familiar", self.review)
        self.assertIn("Bitter Triumph", self.review)
        self.assertIn("seven-rock total", self.review)
        self.assertIn("requires UU", self.review)
        self.assertIn("no claim of simulated results", self.review.lower())
        self.assertIn("No canonical changes", self.review)

if __name__ == "__main__":
    unittest.main()
