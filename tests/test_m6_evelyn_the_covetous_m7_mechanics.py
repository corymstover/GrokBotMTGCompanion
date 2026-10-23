"""Finite source-anchored rules/mana cases for the Evelyn, the Covetous M7 candidate.

No randomness. Evelyn is modelled exactly as printed (current Oracle in the M7 snapshot): flash; "Whenever Evelyn or
another Vampire you control enters, exile the top card of each player's library with a collection counter on it. Once
each turn, you may play a card from exile with a collection counter on it if it was exiled by an ability you
controlled, and you may spend mana as though it were mana of any color to cast it." Rules anchors: 603.6a (enters
triggers; Saw in Half tokens see each other), 406.6/607.2a (exiled-card linkage), 903.9a (commander zone choice on the
Worldgorger exile), 104.4b/732.4 (mandatory loops), 701.21a (sacrifice), 702.8a (flash), 704.5j/704.5d (legend rule,
tokens leaving the battlefield).

This is a bounded rules/qualification-count model over fixed, enumerated states, NOT a game engine, simulation or
win-rate measurement; it supports no improvement claim by itself. PassCBoundedMeasuredTests recomputes the bounded
finite version of the M6 Pass C #18 request (+Brainstorm / -Ripples of Undeath): exact hypergeometric castability,
fetch support, Evelyn castability and Ripples-mills-Worldgorger. Matched opening hands and games against opponents are
NOT modelled (no validated opponent model). Approximations disclosed: each fetch counts as a source of any one Grixis
colour; Gemstone Caverns and Exotic Orchard count as rainbow; fetch/shock life is ignored.
"""
from collections import Counter
from functools import lru_cache
import json
from math import comb
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Evelyn__the_Covetous"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RC = ROOT / "data/grixis/m7/research_challengers"
SPELLBOOK = RC / f"{D}_CommanderSpellbook_20261023.json"
MEASURED = RC / f"{D}_bounded_measured_tests_20261023.json"
ALT_PASSC = RC / f"{D}_PassC_baseline_plus_Brainstorm_minus_RipplesOfUndeath_20261023.txt"
EVELYN = "Evelyn, the Covetous"
ADDS = ["Brainstorm", "Burnt Offering", "Insolent Neonate", "Marsh Flats", "Verdant Catacombs"]
CUTS = ["Blazemire Verge", "Redirect Lightning", "Spellskite", "Thundering Falls", "Wan Shi Tong, Librarian"]
GAME_CHANGERS = ["Ad Nauseam", "Ancient Tomb", "Chrome Mox", "Demonic Tutor", "Force of Will", "Gamble",
                 "Imperial Seal", "Lion's Eye Diamond", "Mana Vault", "Mox Diamond", "Mystical Tutor", "Necropotence",
                 "Notion Thief", "Opposition Agent", "Orcish Bowmasters", "Rhystic Study", "Thassa's Oracle",
                 "Underworld Breach", "Vampiric Tutor"]
OWNER_REMOVED = ["Displacer Kitten", "Otawara, Soaring City", "Morphic Pool", "Talisman of Creativity",
                 "Wheel of Fortune", "The One Ring", "Dragon's Rage Channeler", "Cyclonic Rift", "Deflecting Swat",
                 "Into the Flood Maw", "Hoarding Broodlord", "Beseech the Mirror"]
OWNER_KEEPS = ["Vexing Bauble", "Ripples of Undeath", "Saw in Half", "Windfall", "Notion Thief", "Stifle",
               "Mistrise Village"]
FETCHES = {"Arid Mesa", "Bloodstained Mire", "Flooded Strand", "Marsh Flats", "Misty Rainforest", "Polluted Delta",
           "Scalding Tarn", "Verdant Catacombs", "Wooded Foothills"}
LAND_COLORS = {
    "Ancient Tomb": "", "City of Traitors": "", "Badlands": "BR", "Blood Crypt": "BR", "Blazemire Verge": "BR",
    "Mount Doom": "BR", "City of Brass": "UBR", "Command Tower": "UBR", "Exotic Orchard": "UBR",
    "Gemstone Caverns": "UBR", "Mana Confluence": "UBR", "Island": "U", "Mistrise Village": "U", "Swamp": "B",
    "Steam Vents": "UR", "Thundering Falls": "UR", "Volcanic Island": "UR", "Underground Sea": "UB",
    "Watery Grave": "UB", **{f: "UBR" for f in FETCHES}}
ROCKS = {"Sol Ring": "", "Arcane Signet": "UBR", "Fellwar Stone": "", "Mana Vault": "", "Lotus Petal": "UBR",
         "Talisman of Dominance": "UB", "Talisman of Indulgence": "BR", "Grim Monolith": ""}


def names(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split(" ", 1)
            out[raw.removesuffix(" [Commander]").split(" // ")[0]] += int(q.rstrip("x"))
    return out


def oracle():
    return {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}


def categories(deck):
    lib = Counter(deck)
    lib[EVELYN] -= 1
    cat = Counter()
    for n, q in (+lib).items():
        if n in LAND_COLORS:
            col = LAND_COLORS[n]
            k = ("L", "U" in col, "B" in col, bool(col), n in FETCHES)
        elif n in ROCKS:
            col = ROCKS[n]
            k = ("R", "U" in col, "B" in col, bool(col), False)
        else:
            k = ("X", False, False, False, False)
        cat[k] += q
    assert sum(cat.values()) == 99
    return sorted(cat.items())


def prob(deck, seen, cond):
    items = categories(deck)

    @lru_cache(None)
    def f(i, left, L, R, U, B, C, F):
        if i == len(items):
            return {(L, R, U, B, C, F): 1} if left == 0 else {}
        (t, u, b, col, fe), n = items[i]
        out = Counter()
        for k in range(0, min(n, left) + 1):
            st = (min(L + (k if t == "L" else 0), 6), min(R + (k if t == "R" else 0), 6), min(U + (k if u else 0), 2),
                  min(B + (k if b else 0), 2), min(C + (k if col else 0), 3), min(F + (k if fe else 0), 1))
            for s, v in f(i + 1, left - k, *st).items():
                out[s] += v * comb(n, k)
        return dict(out)
    r = f(0, seen, 0, 0, 0, 0, 0, 0)
    return round(sum(v for s, v in r.items() if cond(*s)) / comb(99, seen), 4)


def measured(deck):
    o = {}
    for play, off in (("play", 0), ("draw", 1)):
        o[play] = dict(
            brainstorm_U_source_T1=prob(deck, 7 + off, lambda L, R, U, B, C, F: U >= 1),
            brainstorm_U_source_T2=prob(deck, 8 + off, lambda L, R, U, B, C, F: U >= 1),
            ripples_castable_T2=prob(deck, 8 + off, lambda L, R, U, B, C, F: min(L, 2) + R >= 2 and B >= 1),
            ripples_castable_T3=prob(deck, 9 + off, lambda L, R, U, B, C, F: min(L, 3) + R >= 2 and B >= 1),
            fetch_in_first_N={str(N): prob(deck, N + off, lambda L, R, U, B, C, F: F >= 1) for N in (7, 8, 9, 10)},
            evelyn_castable={str(T): prob(deck, 7 + T - 1 + off,
                                          lambda L, R, U, B, C, F, T=T: min(L, T) + R >= 5 and B >= 1 and C >= 3)
                             for T in (3, 4, 5, 6)})
    return o


def ripples_wgd(off):
    rows = []
    for k in (1, 2, 3):
        lib = 99 - (7 + 2 + off)
        miss, lk = 1.0, lib
        for _ in range(k):
            miss *= (lk - 3) / lk
            lk -= 4
        rows.append(round(1 - miss, 4))
    return lib, rows


class EvelynOracleAndDeltaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.base = names(BASE)
        cls.cand = names(CAND)

    def test_commander_oracle_is_vampire_only_and_flash(self):
        ev = self.o[EVELYN]
        self.assertEqual(ev["mana_cost"], "{2}{U/B}{B}{B/R}")
        self.assertEqual(ev["type_line"], "Legendary Creature — Vampire Rogue")
        self.assertIn("Flash", ev["oracle_text"])
        self.assertIn("Whenever Evelyn or another Vampire you control enters", ev["oracle_text"])
        self.assertIn("exile the top card of each player's library with a collection counter", ev["oracle_text"])
        self.assertIn("Once each turn", ev["oracle_text"])
        self.assertIn("spend mana as though it were mana of any color", ev["oracle_text"])
        self.assertEqual((ev["power"], ev["toughness"]), ("2", "5"))

    def test_add_oracles_support_the_stated_roles(self):
        self.assertEqual(self.o["Insolent Neonate"]["type_line"], "Creature — Vampire")
        self.assertIn("Discard a card, Sacrifice this creature: Draw a card.", self.o["Insolent Neonate"]["oracle_text"])
        self.assertIn("sacrifice a creature", self.o["Burnt Offering"]["oracle_text"])
        self.assertIn("Add X mana in any combination of {B} and/or {R}", self.o["Burnt Offering"]["oracle_text"])
        self.assertEqual(self.o["Brainstorm"]["mana_cost"], "{U}")
        self.assertIn("Swamp", self.o["Marsh Flats"]["oracle_text"])
        self.assertIn("Swamp", self.o["Verdant Catacombs"]["oracle_text"])
        # Burnt Offering sacrificing Evelyn yields 5, Worldgorger Dragon 6 (mana value of the sacrificed creature).
        self.assertEqual((self.o[EVELYN]["cmc"], self.o["Worldgorger Dragon"]["cmc"]), (5.0, 6.0))

    def test_vampire_count_and_free_spells_versus_vexing_bauble(self):
        vamps = sorted(n for n in self.cand if "Vampire" in self.o[n]["type_line"])
        self.assertEqual(vamps, [EVELYN, "Insolent Neonate"])
        self.assertEqual(sorted(n for n in self.base if "Vampire" in self.o[n]["type_line"]), [EVELYN])
        self.assertIn("if no mana was spent to cast it, counter that spell", self.o["Vexing Bauble"]["oracle_text"])
        for add in ADDS:
            if "Land" not in self.o[add]["type_line"]:
                self.assertNotEqual(self.o[add]["mana_cost"], "", add)

    def test_exact_delta_counts_and_singleton(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), ADDS)
        self.assertEqual(sorted((self.base - self.cand).elements()), CUTS)
        self.assertEqual(sum(self.cand.values()), 100)
        self.assertTrue(all(q == 1 for q in self.cand.values()))
        lands = lambda d: sum(q for n, q in d.items() if "Land" in self.o[n]["type_line"].split(" // ")[0])
        self.assertEqual((lands(self.base), lands(self.cand)), (26, 26))
        self.assertEqual((sum(n in FETCHES for n in self.base), sum(n in FETCHES for n in self.cand)), (7, 9))
        creatures = lambda d: sum(1 for n in d if n != EVELYN and "Creature" in self.o[n]["type_line"])  # library only
        self.assertEqual((creatures(self.base), creatures(self.cand)), (14, 13))

    def test_game_changers_unchanged_and_all_legal(self):
        for d in (self.base, self.cand):
            self.assertEqual(sorted(n for n in d if self.o[n]["game_changer"]), sorted(GAME_CHANGERS))
            for n in d:
                self.assertEqual(self.o[n]["commander_legality"], "legal", n)
                self.assertTrue(set(self.o[n]["color_identity"]) <= set("UBR"), n)

    def test_spellbook_same_seven_combos(self):
        s = json.loads(SPELLBOOK.read_text())
        ids = lambda k: sorted(c["id"] for c in s[k]["included"])
        expected = sorted(["742-1295", "1295-3093", "1368-1414-4856", "1368-3518-4856", "4812-4846", "2896-4846",
                           "3605-4846"])
        self.assertEqual(ids("baseline"), expected)
        self.assertEqual(ids("candidate"), expected)
        self.assertEqual((s["baseline"]["almost_included_count"], s["candidate"]["almost_included_count"]), (103, 117))

    def test_owner_direction(self):
        for card in OWNER_REMOVED:
            self.assertEqual(self.cand[card], 0, card)
        for keep in OWNER_KEEPS:
            self.assertEqual(self.cand[keep], 1, keep)

    def test_saw_in_half_trigger_count_finite(self):
        # 603.6a: two Vampire tokens enter simultaneously; each triggers for itself and for the other.
        tokens = 2
        triggers = tokens * tokens
        self.assertEqual(triggers, 4)
        self.assertEqual(triggers * 4, 16)  # four-player pod: each trigger exiles one card from each library
        # 704.5j then keeps one token; the triggers are already on the stack and still resolve.


class PassCBoundedMeasuredTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rec = json.loads(MEASURED.read_text())

    def test_recompute_baseline_candidate_and_passc_alternative(self):
        for key, path in (("base.txt", BASE), ("cand.txt", CAND), (ALT_PASSC.name, ALT_PASSC)):
            self.assertEqual(measured(names(path)), self.rec["decks"][key], key)

    def test_headline_numbers(self):
        b, c = measured(names(BASE)), measured(names(CAND))
        self.assertEqual((b["play"]["brainstorm_U_source_T1"], c["play"]["brainstorm_U_source_T1"]), (0.8385, 0.8531))
        self.assertEqual((b["draw"]["brainstorm_U_source_T1"], c["draw"]["brainstorm_U_source_T1"]), (0.8771, 0.8899))
        self.assertEqual(b["play"]["ripples_castable_T2"], 0.7852)
        self.assertEqual((b["play"]["fetch_in_first_N"]["7"], c["play"]["fetch_in_first_N"]["7"]), (0.4115, 0.4981))
        self.assertEqual((b["play"]["evelyn_castable"]["4"], c["play"]["evelyn_castable"]["4"]), (0.1491, 0.1491))

    def test_ripples_mills_worldgorger(self):
        self.assertEqual(ripples_wgd(0), (90, [0.0333, 0.0671, 0.1012]))
        self.assertEqual(ripples_wgd(1), (89, [0.0337, 0.0678, 0.1023]))


if __name__ == "__main__":
    unittest.main()
