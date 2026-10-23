"""Finite source-anchored rules/mana cases for the Crosis, the Purger M7 candidate.

Seed 0, no randomness. A bounded rules model, NOT a game engine or win-rate measurement;
it supports no improvement claim by itself.
"""
from collections import Counter
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Crosis__the_Purger"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
SPELLBOOK = ROOT / f"data/grixis/m7/research_challengers/{D}_CommanderSpellbook_20261023.json"
CROSIS = "Crosis, the Purger"
TERGRID = "Tergrid, God of Fright // Tergrid's Lantern"
ADDS = ["Megrim", "Rankle, Master of Pranks", "Aggravated Assault", "Raiders' Wake", "Deadly Rollick"]
CUTS = ["Jet Medallion", "Blizzard Specter", "Dream Salvage", "Oppression", "Izzet Signet"]
CORE = ["Painter's Servant", "Liliana's Caress", "Waste Not", "Sword of Feast and Famine", "Brotherhood Regalia",
        "Lightning Greaves", "Cavern of Souls", "Sedraxis Specter", TERGRID, "Notion Thief", "Teferi's Puzzle Box",
        "Wheel of Fortune", "Windfall", "Dark Deal", "Bottomless Pit", "Mind Twist", "Dark Ritual"]
GAME_CHANGERS = ["Ancient Tomb", "Chrome Mox", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship", "Force of Will",
                 "Gamble", "Mana Vault", "Mox Diamond", "Mystical Tutor", "Notion Thief", "Orcish Bowmasters",
                 TERGRID, "Vampiric Tutor"]
ROCKS_BASE = ["Sol Ring", "Mana Vault", "Chrome Mox", "Mox Diamond", "Lotus Petal", "Arcane Signet", "Dimir Signet",
              "Izzet Signet", "Rakdos Signet", "Talisman of Creativity", "Talisman of Dominance",
              "Talisman of Indulgence", "Jet Medallion"]
FETCH = {"Bloodstained Mire": ("Swamp", "Mountain"), "Marsh Flats": ("Plains", "Swamp"),
         "Misty Rainforest": ("Forest", "Island"), "Polluted Delta": ("Island", "Swamp"),
         "Scalding Tarn": ("Island", "Mountain"), "Verdant Catacombs": ("Swamp", "Forest")}
PUNISHERS = {"Megrim": 2, "Liliana's Caress": 2, "Raiders' Wake": 2}


def names(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split(" ", 1)
            out[raw.removesuffix(" [Commander]")] += int(q.rstrip("x"))
    return out


def per_opponent_loss(discarded, punishers):
    """CR 603.2c: each punisher triggers once per card an opponent discards, including every card of one
    multi-card discard (Crosis purge, wheel). Finite sum; no prevention assumed."""
    return discarded * sum(PUNISHERS[p] for p in punishers)


def crosis_purge(hand_colors, chosen, painter=None):
    """Crosis's paid trigger: discard all cards of the chosen color. With Painter's Servant naming the chosen
    color, every card in hand is that color (Painter Oracle), so the hand is emptied."""
    if painter == chosen:
        return len(hand_colors)
    return sum(1 for colors in hand_colors if chosen in colors)


def sword_assault_loop(lands, combats, connect, crosis_pay=True):
    """Sword of Feast and Famine on Crosis + Aggravated Assault ({3}{R}{R}). Per combat: on combat damage, put the
    Crosis trigger on the stack first and the Sword trigger last (CR 603.3b, we choose order) so Sword resolves
    first and untaps all lands; then pay {2}{B} for Crosis, then {3}{R}{R} in the following main phase (CR 500.8).
    Returns (crosis purges paid, extra combats activated). Finite: bounded by `combats`."""
    purges = extra = 0
    available = lands  # all lands tapped earlier for the first Assault activation are untapped by Sword
    for i in range(combats):
        if not connect[i]:
            break
        available = lands  # Sword untaps all lands
        if crosis_pay and available >= 3 + 5:
            available -= 3
            purges += 1
        if available >= 5:
            available -= 5
            extra += 1
        else:
            break
    return purges, extra


class CrosisM7Mechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_commander_oracle_and_identity(self):
        c = self.cards[CROSIS]
        self.assertEqual(c["mana_cost"], "{3}{U}{B}{R}")
        self.assertIn("Dragon", c["type_line"])
        self.assertIn("Flying", c["oracle_text"])
        self.assertIn("deals combat damage to a player, you may pay {2}{B}", c["oracle_text"])
        self.assertIn("discards all cards of that color", c["oracle_text"])
        self.assertIn("All cards that aren't on the battlefield", self.cards["Painter's Servant"]["oracle_text"])
        hand = [{"U"}, {"B"}, {"R"}, {"U", "R"}, set()]   # five cards, one colorless
        self.assertEqual(crosis_purge(hand, "U"), 2)
        self.assertEqual(crosis_purge(hand, "U", painter="U"), 5)

    def test_punisher_per_card_damage_is_finite_and_opponent_only(self):
        for n in PUNISHERS:
            self.assertIn("Whenever an opponent discards a card", self.cards[n]["oracle_text"])
            self.assertIn("2", self.cards[n]["oracle_text"])
        self.assertIn("deals 2 damage", self.cards["Megrim"]["oracle_text"])
        self.assertIn("loses 2 life", self.cards["Raiders' Wake"]["oracle_text"])
        self.assertEqual(per_opponent_loss(5, ["Liliana's Caress"]), 10)        # baseline Painter purge
        self.assertEqual(per_opponent_loss(5, list(PUNISHERS)), 30)             # candidate Painter purge
        self.assertEqual(per_opponent_loss(7, list(PUNISHERS)), 42)             # wheel on 7 cards
        self.assertEqual(per_opponent_loss(6, ["Megrim"]), 12)                  # Pass C's own example
        self.assertEqual(per_opponent_loss(0, list(PUNISHERS)), 0)              # empty hand: inert

    def test_sword_assault_stack_order_and_mana(self):
        self.assertIn("you untap all lands you control", self.cards["Sword of Feast and Famine"]["oracle_text"])
        a = self.cards["Aggravated Assault"]["oracle_text"]
        self.assertIn("{3}{R}{R}: Untap all creatures you control", a)
        self.assertIn("additional combat phase followed by an additional main phase", a)
        self.assertIn("Activate only as a sorcery", a)
        self.assertEqual(sword_assault_loop(8, 4, [True] * 4), (4, 4))
        self.assertEqual(sword_assault_loop(7, 4, [True] * 4), (0, 4))         # 7 lands: Assault only, no purge
        self.assertEqual(sword_assault_loop(4, 4, [True] * 4), (0, 0))         # cannot pay {3}{R}{R}
        self.assertEqual(sword_assault_loop(8, 4, [True, True, False, True]), (2, 2))  # ends when blocked/prevented

    def test_rankle_and_rollick_oracle(self):
        r = self.cards["Rankle, Master of Pranks"]["oracle_text"]
        self.assertIn("Flying, haste", r)
        self.assertIn("Each player discards a card", r)
        self.assertNotIn("haste", self.cards["Blizzard Specter"]["oracle_text"].lower())
        self.assertIn("If you control a commander, you may cast this spell without paying its mana cost",
                      self.cards["Deadly Rollick"]["oracle_text"])
        self.assertIn("Exile target creature", self.cards["Deadly Rollick"]["oracle_text"])

    def test_spellbook_combos_baseline_one_candidate_two(self):
        s = json.loads(SPELLBOOK.read_text())
        base = {c["id"] for c in s["baseline"]["included"]}
        cand = {c["id"]: c for c in s["candidate"]["included"]}
        self.assertEqual(base, {"2286-3221"})
        self.assertEqual(set(cand), {"2286-3221", "900-3750"})
        self.assertEqual(sorted(cand["900-3750"]["uses"]), ["Aggravated Assault", "Sword of Feast and Famine"])
        for c in s["candidate"]["included"]:
            for n in c["uses"]:
                self.assertGreaterEqual(self.cand[n], 1, n)

    def test_exact_swaps_and_core_preserved(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), sorted(ADDS))
        self.assertEqual(sorted((self.base - self.cand).elements()), sorted(CUTS))
        for n in CORE + [CROSIS]:
            self.assertEqual(self.cand[n], 1, n)

    def test_lands_rocks_and_fetch_reach(self):
        def lands(lst):
            return sum(q for n, q in lst.items() if "Land" in self.cards[n]["type_line"].split(" // ")[0])
        self.assertEqual(lands(self.base), 36)
        self.assertEqual(lands(self.cand), 36)
        self.assertEqual(sum(self.base[n] for n in ROCKS_BASE), 13)
        self.assertEqual(sum(self.cand[n] for n in ROCKS_BASE), 11)
        tapped = [n for n in self.cand if "Land" in self.cards[n]["type_line"]
                  and "This land enters tapped." in self.cards[n]["oracle_text"]]
        self.assertEqual(tapped, ["Xander's Lounge"])
        lounge = self.cards["Xander's Lounge"]["type_line"]
        for f, types in FETCH.items():
            self.assertEqual(self.cand[f], 1, f)
            self.assertTrue(any(t in lounge for t in types), f)
        self.assertEqual(len([n for n in self.cand if "Sacrifice this land: Search" in self.cards[n]["oracle_text"]]), 6)

    def test_legality_identity_singleton_game_changers(self):
        self.assertEqual(sum(self.cand.values()), 100)
        basics = {"Island", "Swamp", "Mountain"}
        for n, q in self.cand.items():
            c = self.cards[n]
            self.assertEqual(c["commander_legality"], "legal", n)
            self.assertTrue(set(c["color_identity"]) <= {"U", "B", "R"}, n)
            if n not in basics:
                self.assertEqual(q, 1, n)
        self.assertEqual(sorted(n for n in self.cand if self.cards[n]["game_changer"]), sorted(GAME_CHANGERS))
        self.assertEqual(sorted(n for n in self.base if self.cards[n]["game_changer"]), sorted(GAME_CHANGERS))
        for n in ADDS:
            self.assertFalse(self.cards[n]["game_changer"], n)


if __name__ == "__main__":
    unittest.main()
