"""Finite source-anchored rules/mana cases for the Cecily/Bjorna (companion Lutri) M7 candidate.

Seed 0, no randomness. Bounded rules model, NOT a game engine or win-rate measurement;
supports no improvement claim by itself.
"""
from collections import Counter
import json
from math import ceil
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Cecily__Bjorna__Lutri"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-13.txt"
SPELLBOOK = ROOT / f"data/grixis/m7/research_challengers/{D}_CommanderSpellbook_20261023.json"
CECILY, BJORNA, LUTRI = "Cecily, Haunted Mage", "Bjorna, Nightfall Alchemist", "Lutri, the Spellchaser"
SEA_GATE = "Sea Gate Restoration // Sea Gate, Reborn"
ADDS = ["Strionic Resonator", "Echo, Perceptive Prodigy", "Twenty-Toed Toad", SEA_GATE, "Deflecting Swat", "Mana Drain"]
CUTS = ["Emry, Lurker of the Loch", "Goblin Engineer", "Sai, Master Thopterist", "Dark Deal", "Mana Geyser", "Seething Song"]
ROCKS = {"Sol Ring", "Arcane Signet", "Dimir Signet", "Izzet Signet", "Rakdos Signet", "Talisman of Creativity",
         "Talisman of Dominance", "Talisman of Indulgence", "Thought Vessel"}
CORE = ["Robe of the Archmagi", "Harmonic Prodigy", "Thought Vessel", "In Garruk's Wake", "Apex of Power",
        "Mnemonic Deluge", "Peer into the Abyss", "Teferi's Ageless Insight", "Underworld Breach", "Wheel of Fortune",
        "Jeska's Will", "Psychosis Crawler", "Trade Secrets", "Yawgmoth's Bargain", "Wheel of Misfortune",
        "Lightning Greaves", "Archmage Emeritus", "Storm-Kiln Artist"]
EXCEPTIONS = {"Trade Secrets", "Yawgmoth's Bargain"}


def names(path, zones=("main", "commander")):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        q, raw = line.split(" ", 1)
        q = int(q.rstrip("x"))
        zone = "commander" if raw.endswith(" [Commander]") else "companion" if raw.endswith(" [Companion]") else "main"
        if zone in zones:
            out[raw.removesuffix(" [Commander]").removesuffix(" [Companion]")] += q
    return out


def cecily_attack(hand, copies=0, payloads=99):
    """Cecily's attack trigger plus `copies` copies (Resonator/Echo/Prodigy). Each resolution: draw 1, then if
    hand >= 11 may free-cast one instant/sorcery from hand (hand - 1). Checked on resolution (not intervening-if).
    Returns (free casts, final hand). Finite."""
    casts = 0
    for _ in range(1 + copies):
        hand += 1
        if hand >= 11 and casts < payloads:
            hand -= 1
            casts += 1
    return casts, hand


def toad_peer_win(hand_before_attack, library, copies=0):
    """Cecily + Twenty-Toed Toad attack together: Toad's two-attacker trigger draws 1; Cecily's trigger(s) draw and
    free-cast Peer into the Abyss on ourselves (draw half the library, rounded up); Toad's attack trigger resolves
    last and wins with 20+ cards in hand. Returns (wins, hand, library). Decking checked (104.3c)."""
    hand, lib = hand_before_attack + 1, library - 1
    hand += 1
    lib -= 1
    if hand < 11:
        return False, hand, lib
    hand -= 1
    draw = ceil(lib / 2)
    hand, lib = hand + draw, lib - draw
    return hand >= 20 and lib >= 0, hand, lib


class CecilyM7Mechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_commander_and_companion_oracle(self):
        c = self.cards[CECILY]
        self.assertIn("Your maximum hand size is eleven.", c["oracle_text"])
        self.assertIn("Then if you have eleven or more cards in your hand, you may cast an instant or sorcery spell "
                      "from your hand without paying its mana cost", c["oracle_text"])
        self.assertEqual((c["power"], c["toughness"], c["cmc"]), ("3", "5", 4.0))
        self.assertIn("Wizard", c["type_line"])
        self.assertIn("Sacrifice an artifact", self.cards[BJORNA]["oracle_text"])
        self.assertIn("if you cast it, copy target instant or sorcery spell you control", self.cards[LUTRI]["oracle_text"])

    def test_cecily_trigger_copies_finite(self):
        self.assertEqual(cecily_attack(9), (0, 10))
        self.assertEqual(cecily_attack(10), (1, 10))
        self.assertEqual(cecily_attack(10, copies=1), (2, 10))
        self.assertEqual(cecily_attack(9, copies=1), (1, 10))
        self.assertEqual(cecily_attack(10, copies=3), (4, 10))
        self.assertEqual(cecily_attack(10, copies=3, payloads=1), (1, 13))

    def test_copier_oracle(self):
        self.assertIn("Copy target triggered ability you control", self.cards["Strionic Resonator"]["oracle_text"])
        self.assertIn("from a creature source", self.cards["Echo, Perceptive Prodigy"]["oracle_text"])
        self.assertIn("Vigilance", self.cards["Echo, Perceptive Prodigy"]["oracle_text"])
        self.assertIn("Wizard", self.cards["Twenty-Toed Toad"]["type_line"])
        self.assertNotIn("Wizard", self.cards["Echo, Perceptive Prodigy"]["type_line"])

    def test_twenty_toed_toad_peer_line(self):
        t = self.cards["Twenty-Toed Toad"]["oracle_text"]
        self.assertIn("Your maximum hand size is twenty.", t)
        self.assertIn("you win the game if there are twenty or more counters on it or you have twenty or more cards in hand", t)
        self.assertIn("draws cards equal to half the number of cards in their library", self.cards["Peer into the Abyss"]["oracle_text"])
        self.assertEqual(toad_peer_win(10, 60), (True, 40, 29))
        self.assertEqual(toad_peer_win(8, 60)[0], False)
        self.assertEqual(toad_peer_win(10, 20), (True, 20, 9))
        self.assertEqual(toad_peer_win(10, 16)[0], False)

    def test_sea_gate_and_cut_rationale_text(self):
        s = self.cards[SEA_GATE]
        self.assertIn("Draw cards equal to the number of cards in your hand plus one. You have no maximum hand size", s["oracle_text"])
        self.assertIn("Land", s["type_line"].split("//")[1])
        self.assertIn("Each player discards all the cards in their hand, then draws that many cards minus one",
                      self.cards["Dark Deal"]["oracle_text"])
        self.assertIn("for each tapped land your opponents control", self.cards["Mana Geyser"]["oracle_text"])
        self.assertIn("If you control a commander, you may cast this spell without paying its mana cost",
                      self.cards["Deflecting Swat"]["oracle_text"])
        self.assertIn("equal to that spell's mana value", self.cards["Mana Drain"]["oracle_text"])

    def test_breach_escape_exiles_three_finite(self):
        self.assertIn("exile three other cards from your graveyard", self.cards["Underworld Breach"]["oracle_text"])

    def test_spellbook_combos(self):
        sb = json.loads(SPELLBOOK.read_text())
        ids = lambda k: {x["id"] for x in sb[k]["included"]}
        self.assertEqual(ids("baseline"), {"1368-1878-2706", "1561-2384", "1561-5042"})
        self.assertEqual(ids("candidate"), ids("baseline") | {"1561-5850"})
        toad = [x for x in sb["candidate"]["included"] if x["id"] == "1561-5850"][0]
        self.assertEqual(sorted(toad["uses"]), ["Peer into the Abyss", "Twenty-Toed Toad"])

    def test_exact_swaps_core_and_companion_outside_100(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), sorted(ADDS))
        self.assertEqual(sorted((self.base - self.cand).elements()), sorted(CUTS))
        for n in CORE + [CECILY, BJORNA]:
            self.assertEqual(self.cand[n], 1, n)
        self.assertEqual(names(CAND, zones=("companion",)), Counter({LUTRI: 1}))
        self.assertNotIn(LUTRI, self.cand)

    def test_quantity_counted_lands_rocks(self):
        land = lambda d: sum(q for n, q in d.items() if "Land" in self.cards[n]["type_line"].split("//")[0])
        self.assertEqual((land(self.base), land(self.cand)), (33, 33))
        self.assertEqual(sum(q for n, q in self.cand.items() if n in ROCKS), 9)
        self.assertEqual(sum(q for n, q in self.base.items() if n in ROCKS), 9)
        self.assertEqual(self.cand["Island"], 2)
        self.assertEqual(sum(self.cand.values()), 100)
        self.assertEqual(sum(self.base.values()), 100)

    def test_legality_identity_singleton_game_changers_exceptions(self):
        for n, q in self.cand.items():
            c = self.cards[n]
            self.assertEqual(c["commander_legality"], "banned" if n in EXCEPTIONS else "legal", n)
            self.assertTrue(set(c["color_identity"]) <= {"U", "B", "R"}, n)
            if n != "Island":
                self.assertEqual(q, 1, n)
        # Scryfall does not encode the Commander companion ban: project exception, never officially legal.
        self.assertEqual(self.cards[LUTRI]["commander_legality"], "legal")
        gc = lambda d: sorted(n for n in d if self.cards[n]["game_changer"])
        self.assertEqual(gc(self.cand), gc(self.base))
        self.assertEqual(gc(self.cand), ["Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship", "Jeska's Will",
                                         "Mystical Tutor", "Notion Thief", "Rhystic Study", "The One Ring",
                                         "Underworld Breach", "Vampiric Tutor"])


if __name__ == "__main__":
    unittest.main()
