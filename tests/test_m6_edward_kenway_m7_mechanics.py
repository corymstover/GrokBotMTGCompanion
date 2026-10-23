"""Finite source-anchored rules/mana cases for the Edward Kenway M7 candidate.

No randomness. Edward is modelled exactly as printed (current Oracle in the M7 snapshot): "At the beginning of your end
step, create a Treasure token for each tapped Assassin, Pirate, and/or Vehicle you control. Whenever a Vehicle you
control deals combat damage to a player, look at the top card of that player's library, then exile it face down. You
may play that card for as long as it remains exiled." Rules anchors: Edward ruling (a permanent with several listed
types counts once), CR 702.122a-c (crew; over-crew legal; crewing does not tap the Vehicle), 301.7a/b (Vehicle P/T
only while a creature; Brotherhood Vertibird counts itself), 702.9b (flying: Mu Yanling), 111.10a and 701.16a
(Treasure, Clue: artifact tokens), 603.2d (Roaming Throne: additional triggers), 704.5j (legend rule).

This is a bounded rules/qualification-count model over fixed, enumerated states, NOT a game engine, simulation or
win-rate measurement; it supports no improvement claim by itself. It contains the bounded finite version of the M6
Pass C #17 requests: (a) Mirkwood Bats vs Fateful Discovery castability (exact hypergeometric), (b) payoff plus
Academy Manufactor co-occurrence, (c) a deterministic end-step engine table (compulsory Fateful draws vs Bats drain,
with/without Manufactor and Time Sieve), (d) strict turn-5 Edward castability. Matched seven-card hands against opponent
interaction/blockers, lethal turn and crewing opportunity cost are NOT modelled (no validated opponent model).
Approximation disclosed: Cavern of Souls and Exotic Orchard are counted as U/B/R sources (true for Edward and Pirates
with Cavern naming Pirate; a small upward bias for Bats and Fateful, applied equally to both lists).
"""
from collections import Counter
from functools import lru_cache
import json
from math import comb
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Edward_Kenway"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RC = ROOT / "data/grixis/m7/research_challengers"
SPELLBOOK = RC / f"{D}_CommanderSpellbook_20261023.json"
MEASURED = RC / f"{D}_bounded_measured_tests_20261023.json"
ALT_FATEFUL = RC / f"{D}_PassC_MirkwoodBats_over_FatefulDiscovery_keep_Fellwar_20261023.txt"
ALT_ADRESTIA = RC / f"{D}_PassC_MirkwoodBats_over_Adrestia_keep_Fellwar_20261023.txt"
ALT_FOUR = RC / f"{D}_four_no_MirkwoodBats_keep_Fellwar_20261023.txt"
EDWARD = "Edward Kenway"
ADDS = ["Brotherhood Vertibird", "Malcolm, the Eyes", "Mirkwood Bats", "Mu Yanling, Wind Rider", "Spectral Sailor"]
CUTS = ["Breeches, Brazen Plunderer", "Captain Lannery Storm", "Fellwar Stone", "Imposter Mech", "Lotus Petal"]
GAME_CHANGERS = ["Ancient Tomb", "Chrome Mox", "Cyclonic Rift", "Fierce Guardianship", "Force of Will", "Imperial Seal",
                 "Jeska's Will", "Mana Vault", "Mox Diamond", "Vampiric Tutor"]
# Owner-removed (2026-10-14 revision) and owner-rejected cards/classes; none may come back.
OWNER_REMOVED_OR_REJECTED = [
    "Sulfur Falls", "Revel in Riches", "Mechanized Production", "Magmatic Galleon", "Admiral Beckett Brass",
    "Fell Flagship", "Corsair Captain", "Lifecraft Engine", "Malcolm, Alluring Scoundrel", "Blood Money",
    "Back in Town", "Pitiless Plunderer", "Storm the Vault", "Rain of Riches", "Treasure Map", "Mech Hangar",
    "Mobilizer Mech", "Reckoner Bankbuster", "Cargo Ship", "Careening Mine Cart", "The Thanos-Copter",
    "Overpowering Attack", "Unstoppable Plan", "Coercive Recruiter", "Great Gilded Boat", "Unwinding Clock",
    "Weatherlight", "Path of Ancestry"]
OWNER_KEEPS = ["Fateful Discovery", "Imperial Seal", "Time Sieve", "Academy Manufactor"]
LAND_COLORS = {
    "Ancient Tomb": "", "Arid Mesa": "UBR", "Badlands": "BR", "Blood Crypt": "BR", "Bloodstained Mire": "UBR",
    "Cavern of Souls": "UBR", "City of Brass": "UBR", "Command Tower": "UBR", "Exotic Orchard": "UBR",
    "Flooded Strand": "UBR", "Island": "U", "Luxury Suite": "BR", "Mana Confluence": "UBR", "Marsh Flats": "UBR",
    "Misty Rainforest": "UBR", "Morphic Pool": "UB", "Mountain": "R", "Otawara, Soaring City": "U",
    "Polluted Delta": "UBR", "Scalding Tarn": "UBR", "Shivan Reef": "UR", "Steam Vents": "UR",
    "Underground River": "UB", "Sulfurous Springs": "BR", "Swamp": "B", "Training Center": "UR",
    "Underground Sea": "UB", "Urza's Saga": "", "Verdant Catacombs": "UBR", "Volcanic Island": "UR",
    "Watery Grave": "UB", "Wooded Foothills": "UBR", "Xander's Lounge": "UBR"}
DURABLE_ROCKS = {"Sol Ring": "", "Arcane Signet": "UBR", "Fellwar Stone": "", "Mana Vault": "",
                 "Talisman of Creativity": "UR", "Talisman of Dominance": "UB", "Talisman of Indulgence": "BR"}
BIT = {"U": 1, "B": 2, "R": 4}


def names(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split(" ", 1)
            out[raw.removesuffix(" [Commander]").split(" // ")[0]] += int(q.rstrip("x"))
    return out


def oracle():
    out = {}
    for c in json.loads(SNAP.read_text())["cards"]:
        out[c["name"]] = out[c["name"].split(" // ")[0]] = c
    return out


def library(deck):
    lib = Counter(deck)
    lib[EDWARD] -= 1
    return +lib


def _dp(items, seen, key):
    @lru_cache(None)
    def f(i, left):
        if i == len(items):
            return {(0, 0, 0, 0): 1} if left == 0 else {}
        (typ, col), n = items[i]
        out = Counter()
        for k in range(0, min(n, left) + 1):
            for st, v in f(i + 1, left - k).items():
                out[key(st, typ, col, k)] += v * comb(n, k)
        return dict(out)
    return f(0, seen)


def categories(deck, rocks):
    cat = Counter()
    for n, q in library(deck).items():
        if n in LAND_COLORS:
            cat[("L", LAND_COLORS[n])] += q
        elif n in rocks:
            cat[("R", rocks[n])] += q
        else:
            cat[("X", "")] += q
    assert sum(cat.values()) == 99
    return sorted(cat.items())


def edward_t5(deck, seen):
    """P(>=5 lands among `seen`) and strict P(Edward castable by turn 5 from lands plus durable rocks: min(lands,5) +
    rocks >= 5, lands >= 3, and the sources seen cover U, B and R). Lotus Petal, moxen, Treasure excluded."""
    def key(st, typ, col, k):
        lands, rocks, m, _ = st
        return (min(lands + (k if typ == "L" else 0), 6), min(rocks + (k if typ == "R" else 0), 6),
                m | (sum(BIT[ch] for ch in col) if k and typ != "X" else 0), 0)
    res, den = _dp(tuple(categories(deck, DURABLE_ROCKS)), seen, key), comb(99, seen)
    a = sum(v for (l, r, m, _), v in res.items() if l >= 5) / den
    b = sum(v for (l, r, m, _), v in res.items() if min(l, 5) + r >= 5 and m == 7 and l >= 3) / den
    return round(a, 4), round(b, 4)


def bats_vs_fateful(deck, seen):
    """P(Mirkwood Bats {3}{B} castable) and P(Fateful Discovery {3}{U}{U} castable) from lands plus durable rocks."""
    def key(st, typ, col, k):
        s, u, b, _ = st
        src = typ != "X"
        return (min(s + (k if src else 0), 5), min(u + (k if src and "U" in col else 0), 2),
                min(b + (k if src and "B" in col else 0), 1), 0)
    res, den = _dp(tuple(categories(deck, DURABLE_ROCKS)), seen, key), comb(99, seen)
    bats = sum(v for (s, u, b, _), v in res.items() if s >= 4 and b >= 1) / den
    fate = sum(v for (s, u, b, _), v in res.items() if s >= 5 and u >= 2) / den
    return round(bats, 4), round(fate, 4)


def both_seen(seen, size=99):
    return round(comb(size - 2, seen - 2) / comb(size, seen), 4)


def end_step(tapped, manufactor=False, sieve=False):
    """Edward end step: one Treasure per tapped qualifier (each permanent once). Academy Manufactor replaces each
    Treasure creation with Clue + Food + Treasure. Fateful Discovery draws once per artifact entering (compulsory).
    Mirkwood Bats: each opponent loses 1 per token created and 1 per token sacrificed; a Time Sieve activation
    sacrifices five artifacts (counted only when five tokens exist). Returns (tokens, fateful_draws, bats_drain)."""
    tokens = tapped * (3 if manufactor else 1)
    sac = 5 if (sieve and tokens >= 5) else 0
    return tokens, tokens, tokens + sac


def edward_treasures(permanents):
    """permanents: list of type sets of TAPPED permanents. Each counts once if it has any listed type."""
    return sum(1 for types in permanents if types & {"Assassin", "Pirate", "Vehicle"})


class EdwardRulesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.cand = names(CAND)
        cls.base = names(BASE)

    def test_edward_oracle_and_legality(self):
        e = self.o[EDWARD]
        self.assertEqual(e["mana_cost"], "{2}{U}{B}{R}")
        self.assertIn("create a Treasure token for each tapped Assassin, Pirate, and/or Vehicle you control",
                      e["oracle_text"])
        self.assertIn("Whenever a Vehicle you control deals combat damage to a player", e["oracle_text"])
        self.assertIn("You may play that card for as long as it remains exiled", e["oracle_text"])
        self.assertEqual(e["commander_legality"], "legal")
        self.assertFalse(e["game_changer"])
        self.assertEqual((e["set"], e["released_at"]), ("acr", "2024-07-05"))

    def test_exact_delta_and_counts(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), ADDS)
        self.assertEqual(sorted((self.base - self.cand).elements()), CUTS)
        self.assertEqual(sum(self.cand.values()), 100)
        self.assertEqual(sum(q for n, q in self.cand.items() if n in LAND_COLORS), 35)
        self.assertEqual(sum(q for n, q in self.base.items() if n in LAND_COLORS), 35)
        self.assertEqual((self.cand["Island"], self.cand["Swamp"], self.cand["Mountain"]), (2, 2, 1))
        for n in self.cand:
            if "Land" in self.o[n]["type_line"].split(" // ")[0]:
                self.assertIn(n, LAND_COLORS)
        self.assertEqual(sorted(n for n in self.cand if self.o[n]["game_changer"]), GAME_CHANGERS)
        self.assertEqual(sorted(n for n in self.base if self.o[n]["game_changer"]), GAME_CHANGERS)

    def test_owner_removed_and_rejected_not_readded_and_keeps_kept(self):
        for n in OWNER_REMOVED_OR_REJECTED:
            self.assertNotIn(n, self.cand, n)
        for n in OWNER_KEEPS:
            self.assertIn(n, self.cand, n)

    def test_type_counts(self):
        def count(deck, pred):
            return sum(q for n, q in deck.items() if pred(self.o[n]["type_line"].split(" // ")[0]))
        veh = lambda t: "Vehicle" in t
        pa = lambda t: "Creature" in t and ("Pirate" in t or "Assassin" in t)
        cre = lambda t: "Creature" in t
        self.assertEqual((count(self.base, veh), count(self.cand, veh)), (13, 13))
        self.assertEqual((count(self.base, pa), count(self.cand, pa)), (21, 21))
        self.assertEqual((count(self.base, cre), count(self.cand, cre)), (24, 26))
        fly = lambda deck: sum(1 for n in deck if "Vehicle" in self.o[n]["type_line"]
                               and self.o[n]["oracle_text"].startswith("Flying"))
        self.assertEqual((fly(self.base), fly(self.cand)), (4, 5))

    def test_added_cards_oracle(self):
        self.assertIn("Vehicles you control have flying.", self.o["Mu Yanling, Wind Rider"]["oracle_text"])
        self.assertIn("3/2 colorless Vehicle artifact token with crew 1", self.o["Mu Yanling, Wind Rider"]["oracle_text"])
        self.assertIn("power is equal to the number of artifacts you control",
                      self.o["Brotherhood Vertibird"]["oracle_text"])
        self.assertIn("Whenever you create or sacrifice a token, each opponent loses 1 life.",
                      self.o["Mirkwood Bats"]["oracle_text"])
        self.assertIn("Pirate", self.o["Spectral Sailor"]["type_line"])
        self.assertIn("Flash", self.o["Spectral Sailor"]["oracle_text"])
        self.assertIn("Pirate", self.o["Malcolm, the Eyes"]["type_line"])
        self.assertIn("Whenever you cast your second spell each turn, investigate.",
                      self.o["Malcolm, the Eyes"]["oracle_text"])
        self.assertNotIn("Pirate", self.o["Mirkwood Bats"]["type_line"])  # disclosed: not an Edward qualifier

    def test_edward_counts_each_permanent_once(self):
        self.assertEqual(edward_treasures([{"Pirate", "Vehicle"}]), 1)
        self.assertEqual(edward_treasures([{"Human", "Assassin", "Pirate"}, {"Vehicle"}, {"Bat"}]), 2)
        self.assertEqual(edward_treasures([]), 0)

    def test_spellbook_same_six_complete_combos(self):
        d = json.loads(SPELLBOOK.read_text())
        ids = lambda k: sorted(c["id"] for c in d[k]["included"])
        self.assertEqual(ids("baseline"), ids("candidate"))
        self.assertEqual(len(d["candidate"]["included"]), 6)
        self.assertEqual((d["baseline"]["almost_included_count"], d["candidate"]["almost_included_count"]), (43, 45))
        sieve = [c for c in d["candidate"]["included"] if "Time Sieve" in c["uses"]]
        self.assertEqual(len(sieve), 5)
        for c in d["candidate"]["included"]:
            self.assertFalse(set(c["uses"]) & set(ADDS))  # no add is part of a complete combo


class PassCBoundedMeasuredTests(unittest.TestCase):
    """Bounded finite versions of the M6 Pass C #17 requests (exact hypergeometric; no RNG)."""

    @classmethod
    def setUpClass(cls):
        cls.cand = names(CAND)
        cls.base = names(BASE)
        cls.m = json.loads(MEASURED.read_text())

    def test_a_bats_vs_fateful_castability(self):
        got_b = [bats_vs_fateful(self.base, n) for n in (10, 11, 12)]
        got_c = [bats_vs_fateful(self.cand, n) for n in (10, 11, 12)]
        self.assertEqual(got_b, [(0.6839, 0.4191), (0.7694, 0.5296), (0.8364, 0.6307)])
        self.assertEqual(got_c, [(0.6597, 0.3937), (0.7477, 0.5024), (0.8179, 0.6037)])
        rec = {k.split(" ")[0]: v for k, v in self.m["pass_c_bounded_test"]["castability"].items()}
        self.assertEqual([(r["P_bats_castable"], r["P_fateful_castable"]) for r in rec["BASELINE"]], got_b)
        self.assertEqual([(r["P_bats_castable"], r["P_fateful_castable"]) for r in rec["PREFERRED_FIVE"]], got_c)
        self.assertEqual([bats_vs_fateful(names(ALT_FATEFUL), n) for n in (10, 11, 12)], got_b)

    def test_b_payoff_and_manufactor_both_seen(self):
        self.assertEqual([both_seen(n) for n in (10, 11, 12, 15)], [0.0093, 0.0113, 0.0136, 0.0216])
        self.assertEqual(self.cand["Academy Manufactor"], 1)

    def test_c_end_step_engine_table(self):
        self.assertEqual(end_step(2), (2, 2, 2))
        self.assertEqual(end_step(2, manufactor=True), (6, 6, 6))
        self.assertEqual(end_step(2, manufactor=True, sieve=True), (6, 6, 11))
        self.assertEqual(end_step(4, manufactor=True), (12, 12, 12))
        self.assertEqual(end_step(4, manufactor=True, sieve=True), (12, 12, 17))
        self.assertEqual(end_step(4, sieve=True), (4, 4, 4))  # Sieve needs five artifacts: intended duplicate row
        rows = self.m["pass_c_bounded_test"]["engine"]
        self.assertEqual(len(rows), 24)
        for r in rows:
            t, d, b = end_step(r["tapped_qualifiers"], r["manufactor"], r["time_sieve_sacrifices_5_tokens"] or False)
            self.assertEqual((r["tokens_created"], r["fateful_compulsory_draws"], r["bats_life_loss_each_opponent"]),
                             (t, d, b))
            self.assertEqual(r["end_steps_of_bats_alone_to_kill_3_opponents_from_40"], -(-40 // b))

    def test_d_edward_turn5_castability_petal_excluded(self):
        self.assertEqual((edward_t5(self.base, 11), edward_t5(self.base, 12)), ((0.3342, 0.5283), (0.4251, 0.6295)))
        self.assertEqual((edward_t5(self.cand, 11), edward_t5(self.cand, 12)), ((0.3342, 0.5025), (0.4251, 0.6038)))
        for alt in (ALT_FATEFUL, ALT_ADRESTIA, ALT_FOUR):
            self.assertEqual((edward_t5(names(alt), 11), edward_t5(names(alt), 12)),
                             ((0.3342, 0.5283), (0.4251, 0.6295)))
        rec = self.m["mana_test_petal_excluded"]["results"]
        cand = [v for k, v in rec.items() if k.startswith("PREFERRED_FIVE")][0]
        self.assertEqual([x["P_castable_T5_lands_plus_rocks"] for x in cand], [0.5025, 0.6038])

    def test_e_opening_hand_lands(self):
        p = sum(comb(35, k) * comb(64, 7 - k) for k in range(2, 6)) / comb(99, 7)
        self.assertEqual(round(p, 4), 0.7746)


if __name__ == "__main__":
    unittest.main()
