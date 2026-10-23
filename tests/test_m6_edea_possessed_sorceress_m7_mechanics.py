"""Finite source-anchored rules/mana cases for the Edea, Possessed Sorceress M7 candidate.

Seed 0, no randomness. Edea is modelled exactly as printed (current Oracle in the M7 snapshot): "Ward {2}. At the
beginning of combat on your turn, gain control of target creature an opponent controls until end of turn. Untap that
creature. It gains haste until end of turn. Whenever a creature you control but don't own dies, return it to the
battlefield under its owner's control and you draw a card." Rules anchors: CR 500.8 / 506.1 (each additional combat
phase has its own beginning of combat step, so Edea triggers again), 603.2b (an "at the beginning of" ability triggers
only if the permanent has it when the step begins: Irma's timing caveat), 603.2d (Roaming Throne: additional triggers,
not copies), 603.3b (we order our simultaneous death triggers: Kaya's Ghostform before Edea), 400.7 and 609.3 (once
Ghostform has returned the card, Edea's return does as much as possible: no return, but the draw still happens),
707.2 (Hall of Echoes / Irma copy Edea's printed abilities), 704.5j (legend rule, switched off by Hall of Echoes).

This is a bounded rules/qualification-count model over fixed, enumerated states, NOT a game engine, simulation or
win-rate measurement; it supports no improvement claim by itself. It contains the bounded finite version of every
M6 Pass C #16 requested test: (a) Conjurer's Closet vs Irma, (b) Closet vs Impostor Syndrome, (c) Closet vs
Industrial Advancement, (d) Combat Celebrant vs Grim Haruspex (deferred in Pass C), (e) mana on turns 3-7 as exact
multivariate-hypergeometric access, (f) the Irma/Edea beginning-of-combat timing. Opponents' responses, removal,
blockers and matchups are not modelled; those remain limitations.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
from math import comb
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Edea__Possessed_Sorceress"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RC = ROOT / "data/grixis/m7/research_challengers"
SPELLBOOK = RC / f"{D}_CommanderSpellbook_20261023.json"
EDEA = "Edea, Possessed Sorceress"
ADDS = ["Aggravated Assault", "Combat Celebrant", "Hall of Echoes", "Kaya's Ghostform", "Lithoform Engine"]
CUTS = ["Ayara, Widow of the Realm", "Evereth, Viceroy of Plunder", "High Market", "Seize the Spotlight",
        "Zara, Renegade Recruiter"]
GAME_CHANGERS = ["Ancient Tomb", "Demonic Tutor", "Fierce Guardianship"]
# Owner's 2026-10-14 revision removed these nine; owner rejected the rest. None may come back.
OWNER_REMOVED = ["Garland, Royal Kidnapper", "Beast Within", "Coercive Recruiter", "Morbid Opportunist",
                 "Dictate of Erebos", "Reliquary Tower", "Dragonskull Summit", "Drowned Catacomb", "Sulfur Falls"]
OWNER_REJECTED = ["Marchesa, the Black Rose", "Domineering Will", "Nasty End", "Cunning Rhetoric", "Conjurer's Closet",
                  "Chameleon, Master of Disguise", "Quantum Misalignment", "Helm of Possession", "Altar of Dementia",
                  "Yawgmoth, Thran Physician", "Carrion Feeder", "Come Back Wrong", "Rhystic Study",
                  "Vampiric Tutor", "Force of Will", "The One Ring", "Breath of Fury", "Sakashima the Impostor"]
LAND_COLORS = {
    "Ancient Tomb": "", "Arcane Lighthouse": "", "Badlands": "BR", "Blood Crypt": "BR", "Bloodstained Mire": "BR",
    "City of Brass": "UBR", "Command Tower": "UBR", "Exotic Orchard": "UBR", "Hall of Echoes": "", "High Market": "",
    "Haunted Ridge": "BR", "Island": "U", "Luxury Suite": "BR", "Mana Confluence": "UBR", "Morphic Pool": "UB",
    "Mountain": "R", "Otawara, Soaring City": "U", "Phyrexian Tower": "", "Polluted Delta": "UB",
    "Scalding Tarn": "UR", "Shipwreck Marsh": "UB", "Steam Vents": "UR", "Stormcarved Coast": "UR", "Swamp": "B",
    "Training Center": "UR", "Underground Sea": "UB", "Urborg, Tomb of Yawgmoth": "B", "Volcanic Island": "UR",
    "Watery Grave": "UB", "Xander's Lounge": "UBR"}
ROCKS = {"Sol Ring": "", "Fellwar Stone": "", "Arcane Signet": "UBR", "Talisman of Creativity": "UR",
         "Talisman of Dominance": "UB", "Talisman of Indulgence": "BR"}
# Repeatable sacrifice outlets usable at will (no once-per-end-step restriction).
OUTLETS = ["Ashnod's Altar", "Ayara, Widow of the Realm", "Evereth, Viceroy of Plunder", "Goblin Bombardment",
           "High Market", "Illuminor Szeras", "Phyrexian Altar", "Phyrexian Tower", "Viscera Seer",
           "Warren Soultrader"]
EXTRA_COMBAT = ["Aggravated Assault", "Combat Celebrant", "Full Throttle", "Karlach, Fury of Avernus"]
TRIGGER_MULT = ["Gogo, Master of Mimicry", "Hall of Echoes", "Irma, Part-Time Mutant", "Lithoform Engine",
                "Roaming Throne", "Sakashima of a Thousand Faces", "Spark Double", "Strionic Resonator"]


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
    lib[EDEA] -= 1
    return +lib


BIT = {"U": 1, "B": 2, "R": 4}


def mana_access(deck, turn, on_draw=False):
    """Exact multivariate-hypergeometric DP over the 99 for seen = 7 + (turn - 1) (+1 on the draw).
    A: P(lands >= turn) (a land drop every turn up to `turn`). B: P(Edea castable by `turn`: min(lands, turn) + rocks
    >= 5, lands >= 3, and the distinct coloured sources seen cover U, B and R). Each land or rock counted once."""
    seen = 7 + (turn - 1) + (1 if on_draw else 0)
    cat = Counter()
    for n, q in library(deck).items():
        if n in LAND_COLORS:
            cat[("L", LAND_COLORS[n])] += q
        elif n in ROCKS:
            cat[("R", ROCKS[n])] += q
        else:
            cat[("X", "")] += q
    items, total = sorted(cat.items()), sum(cat.values())
    assert total == 99

    @lru_cache(None)
    def f(i, left):
        if i == len(items):
            return {(0, 0, 0): 1} if left == 0 else {}
        (typ, col), n = items[i]
        out = Counter()
        for k in range(0, min(n, left) + 1):
            for (lands, rocks, m), v in f(i + 1, left - k).items():
                key = (min(lands + (k if typ == "L" else 0), 8), min(rocks + (k if typ == "R" else 0), 6),
                       m | (sum(BIT[ch] for ch in col) if k and typ != "X" else 0))
                out[key] += v * comb(n, k)
        return dict(out)

    res, den = f(0, seen), comb(99, seen)
    a = Fraction(sum(v for (l, r, m), v in res.items() if l >= turn), den)
    b = Fraction(sum(v for (l, r, m), v in res.items() if min(l, turn) + r >= 5 and m == 7 and l >= 3), den)
    return a, b


def p_at_least_one(hits, seen, size=99):
    return 1 - Fraction(comb(size - hits, seen), comb(size, seen))


# ---- (a) Conjurer's Closet vs Irma ------------------------------------------------------------------------------
def closet_vs_irma_grid():
    """Cells: combats this turn c in 1..4 (1 none; 2 Karlach/Celebrant/one Assault activation; 3 Full Throttle;
    4 Full Throttle + Celebrant), Roaming Throne naming Human or Warlock t in {0,1}, Thassa in {0,1}, Irma already
    an Edea copy from an earlier turn in {0,1}. Irma (Edea mode): copies Edea at beginning of combat; by 603.2b the
    copied Edea trigger is missing in the combat where the copy first happens, then she is a second Edea for every
    later combat (her copy has no duration). Closet: one extra end-step blink keeping one stolen creature (Thassa
    already does this). Returns per-cell (irma_steals, irma_keeps, closet_steals, closet_keeps)."""
    cells = []
    for c, t, thassa, ready in product(range(1, 5), (0, 1), (0, 1), (0, 1)):
        edea = c * (1 + t)
        irma_extra = (c if ready else c - 1) * (1 + t)
        cells.append(dict(c=c, t=t, thassa=thassa, ready=ready, irma_steals=edea + irma_extra, irma_keeps=thassa,
                          closet_steals=edea, closet_keeps=thassa + 1))
    return cells


# ---- (b) Closet vs Impostor Syndrome ----------------------------------------------------------------------------
def closet_vs_impostor_grid():
    """Cells: stolen nontoken creatures that connect with a player this turn k in 0..3 (summed over all combats),
    Thassa in {0,1}. Impostor Syndrome: one permanent token copy we own per connecting nontoken creature (Edea never
    returns tokens: we own them). Closet: one kept stolen creature at end step. Returns (impostor_keeps,
    closet_keeps)."""
    return [dict(k=k, thassa=th, impostor=k + th, closet=1 + th) for k, th in product(range(4), (0, 1))]


# ---- (c) Closet vs Industrial Advancement -----------------------------------------------------------------------
def advancement_hit(x, library_size, creatures):
    """Exact P(at least one creature card among the top x of the library)."""
    return 1 - Fraction(comb(library_size - creatures, x), comb(library_size, x))


def closet_vs_advancement_grid():
    """Industrial Advancement sacrifices the stolen creature at our end step: Edea returns it to its owner and we draw
    (one card), and with probability P(hit in top MV) a creature from our library enters. Closet instead keeps the
    stolen creature. Cells: stolen creature MV x in 2..8, library 70/80 cards with 14/18 creature cards."""
    out = []
    for x, size, cr in product(range(2, 9), (70, 80), (14, 18)):
        out.append(dict(mv=x, library=size, creatures=cr, p_hit=advancement_hit(x, size, cr)))
    return out


# ---- (d) Combat Celebrant vs Grim Haruspex / Seize the Spotlight ------------------------------------------------
def celebrant_grid():
    """Over a three-turn window: Celebrant (survives, attacks) gives one extra combat per turn, so one extra Edea
    steal per turn (two with Roaming Throne naming Warlock or Human). Grim Haruspex draws one card per nontoken
    creature we control that dies, stolen ones included (on top of Edea's draw). Seize the Spotlight is a one-shot:
    each opponent chooses; at most three steals or three draws+Treasures once. Cells: deaths per turn d in 0..3,
    Throne t in {0,1}, Celebrant turns alive a in 0..3."""
    out = []
    for d, t, a in product(range(4), (0, 1), range(4)):
        out.append(dict(d=d, t=t, alive=a, celebrant_steals=a * (1 + t), haruspex_draws=3 * d,
                        spotlight_best_steals=3, spotlight_worst_steals=0))
    return out


def assault_extra_combats(mana, red):
    """Aggravated Assault {3}{R}{R}, sorcery speed in each additional main phase: activations = min(mana//5, red//2)."""
    return min(mana // 5, red // 2)


def edea_triggers(combats, throne=0, edea_copies=0, lithoform=0):
    """Edea combat triggers this turn: one per combat per Edea instance (Edea + Hall/Irma/clone copies), doubled by
    each Roaming Throne naming Human or Warlock (603.2d), plus Lithoform Engine copies ({2},{T}: once per untap)."""
    return combats * (1 + edea_copies) * (1 + throne) + lithoform


def death_draws(ghostform_first):
    """A stolen creature enchanted with Kaya's Ghostform dies. We order the two triggers (603.3b). Returns
    (controller of the returned card, cards Edea draws)."""
    if ghostform_first:
        return ("us", 1)   # Ghostform returns it under our control; Edea's return then finds a new object (400.7),
                           # does as much as possible (609.3): no return, but the draw still happens.
    return ("owner", 1)    # Edea returns it first; Ghostform then finds nothing (ruling 2019-05-03).


class EdeaRulesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.cand = names(CAND)
        cls.base = names(BASE)

    def test_edea_oracle_and_legality(self):
        e = self.o[EDEA]
        self.assertEqual(e["mana_cost"], "{2}{U}{B}{R}")
        self.assertIn("At the beginning of combat on your turn, gain control of target creature an opponent controls",
                      e["oracle_text"])
        self.assertIn("return it to the battlefield under its owner's control and you draw a card", e["oracle_text"])
        self.assertEqual(e["commander_legality"], "legal")
        self.assertFalse(e["game_changer"])
        self.assertEqual((e["set"], e["released_at"]), ("fic", "2025-12-05"))

    def test_exact_delta_and_counts(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), ADDS)
        self.assertEqual(sorted((self.base - self.cand).elements()), CUTS)
        self.assertEqual(sum(self.cand.values()), 100)
        lands = sum(q for n, q in self.cand.items() if n in LAND_COLORS)
        self.assertEqual(lands, 35)
        self.assertEqual(sorted(n for n in self.cand if self.o[n]["game_changer"]), GAME_CHANGERS)

    def test_owner_removed_and_rejected_not_readded(self):
        for n in OWNER_REMOVED + OWNER_REJECTED:
            self.assertNotIn(n, self.cand, n)

    def test_added_cards_oracle(self):
        self.assertIn("{3}{R}{R}: Untap all creatures you control. After this main phase, there is an additional combat phase",
                      self.o["Aggravated Assault"]["oracle_text"])
        self.assertIn("return that card to the battlefield under your control", self.o["Kaya's Ghostform"]["oracle_text"])
        self.assertIn("The \"legend rule\" doesn't apply", self.o["Hall of Echoes"]["oracle_text"])
        self.assertIn("Copy target activated or triggered ability you control", self.o["Lithoform Engine"]["oracle_text"])
        self.assertIn("there is an additional combat phase", self.o["Combat Celebrant"]["oracle_text"])
        self.assertIn("Human", self.o["Combat Celebrant"]["type_line"])

    def test_trigger_counts(self):
        self.assertEqual(edea_triggers(1), 1)
        self.assertEqual(edea_triggers(2), 2)                     # Celebrant / Karlach / one Assault activation
        self.assertEqual(edea_triggers(1, edea_copies=1), 2)       # Hall of Echoes activated before combat
        self.assertEqual(edea_triggers(2, throne=1, edea_copies=1), 8)
        self.assertEqual(edea_triggers(1, lithoform=1), 2)
        self.assertEqual(assault_extra_combats(10, 4), 2)
        self.assertEqual(assault_extra_combats(10, 3), 1)
        self.assertEqual(assault_extra_combats(4, 4), 0)

    def test_ghostform_ordering(self):
        self.assertEqual(death_draws(True), ("us", 1))
        self.assertEqual(death_draws(False), ("owner", 1))

    def test_irma_timing_caveat(self):
        # 603.2b: in the combat where Irma first becomes an Edea copy, the copy has no trigger for that step.
        cells = {(x["c"], x["t"], x["thassa"], x["ready"]): x for x in closet_vs_irma_grid()}
        self.assertEqual(cells[(1, 0, 0, 0)]["irma_steals"], 1)
        self.assertEqual(cells[(1, 0, 0, 1)]["irma_steals"], 2)
        self.assertEqual(cells[(2, 0, 0, 0)]["irma_steals"], 3)

    def test_no_complete_spellbook_combo(self):
        d = json.loads(SPELLBOOK.read_text())
        self.assertEqual(d["baseline"]["included"], [])
        self.assertEqual(d["candidate"]["included"], [])


class PassCBoundedMeasuredTests(unittest.TestCase):
    """Bounded finite versions of every M6 Pass C #16 request (exact counts/fractions; seed 0)."""

    @classmethod
    def setUpClass(cls):
        cls.cand = names(CAND)
        cls.base = names(BASE)

    def test_a_closet_vs_irma(self):
        g = closet_vs_irma_grid()
        self.assertEqual(len(g), 32)
        steals_irma = sum(x["irma_steals"] for x in g)
        steals_closet = sum(x["closet_steals"] for x in g)
        keeps_irma = sum(x["irma_keeps"] for x in g)
        keeps_closet = sum(x["closet_keeps"] for x in g)
        self.assertEqual((steals_irma, steals_closet, keeps_irma, keeps_closet), (216, 120, 16, 48))
        self.assertEqual(sum(1 for x in g if x["irma_steals"] > x["closet_steals"]), 28)
        # Keep Irma (Pass C KEEP): +96 steal triggers (each also a potential Edea draw) vs +32 end-step keeps,
        # and Thassa already supplies the end-step keep in half the cells.

    def test_b_closet_vs_impostor(self):
        g = closet_vs_impostor_grid()
        self.assertEqual(len(g), 8)
        self.assertEqual(sum(1 for x in g if x["impostor"] >= x["closet"]), 6)
        self.assertEqual(sum(1 for x in g if x["impostor"] > x["closet"]), 4)

    def test_c_closet_vs_advancement(self):
        g = {(x["mv"], x["library"], x["creatures"]): x["p_hit"] for x in closet_vs_advancement_grid()}
        self.assertEqual(len(g), 28)
        self.assertEqual(round(float(g[(5, 80, 18)]), 4), 0.7308)
        self.assertEqual(round(float(g[(3, 70, 14)]), 4), 0.4936)
        self.assertEqual(round(float(g[(8, 80, 18)]), 4), 0.8834)
        # Advancement: one Edea draw plus a free creature at these hit rates, every end step; Closet: keep one
        # stolen creature (a role Thassa already fills). Keep Industrial Advancement.

    def test_d_celebrant_vs_haruspex(self):
        g = celebrant_grid()
        self.assertEqual(len(g), 32)
        self.assertEqual(sum(x["celebrant_steals"] for x in g), 72)
        self.assertEqual(sum(x["haruspex_draws"] for x in g), 144)
        # Both stay: Celebrant replaces Seize the Spotlight, not Grim Haruspex (Pass C DEFER honoured).
        self.assertIn("Grim Haruspex", self.cand)
        self.assertIn("Combat Celebrant", self.cand)

    def test_e_mana_turns_3_to_7(self):
        expected = {}
        for t in range(3, 8):
            a_b, b_b = mana_access(self.base, t)
            a_c, b_c = mana_access(self.cand, t)
            self.assertEqual((a_b, b_b), (a_c, b_c))  # Hall of Echoes replaces High Market: both colourless lands
            expected[t] = (round(float(a_c), 4), round(float(b_c), 4))
        self.assertEqual(expected, MANA_EXPECTED)

    def test_f_outlet_density_cost(self):
        base_n = sum(self.base[n] for n in OUTLETS)
        cand_n = sum(self.cand[n] for n in OUTLETS)
        self.assertEqual((base_n, cand_n), (10, 7))
        self.assertEqual(round(float(p_at_least_one(base_n, 12)), 4), 0.7432)
        self.assertEqual(round(float(p_at_least_one(cand_n, 12)), 4), 0.6075)
        ex_b = sum(self.base[n] for n in EXTRA_COMBAT)
        ex_c = sum(self.cand[n] for n in EXTRA_COMBAT)
        mult_b = sum(self.base[n] for n in TRIGGER_MULT)
        mult_c = sum(self.cand[n] for n in TRIGGER_MULT)
        self.assertEqual((ex_b, ex_c, mult_b, mult_c), (2, 4, 6, 8))


MANA_EXPECTED = {3: (0.6811, 0.0456), 4: (0.4984, 0.2304), 5: (0.3342, 0.4878), 6: (0.2069, 0.588), 7: (0.1191, 0.6772)}

if __name__ == "__main__":
    unittest.main()
