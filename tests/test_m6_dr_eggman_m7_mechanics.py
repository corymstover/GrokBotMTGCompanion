"""Finite source-anchored rules/mana cases for the Dr. Eggman M7 candidate.

Seed 0, no randomness. Dr. Eggman is modelled exactly as printed (current Oracle in the M7 snapshot): "At the beginning
of your end step, draw a card. Then each opponent faces a villainous choice — That player discards a card, or you may put
a Construct, Robot, or Vehicle card from your hand onto the battlefield." Rules anchors: CR 701.55a-d (villainous choice; additional times one at a time (55c, The Valeyard);
each opponent chooses one at a time in APNAP order (55d)), 701.55b (a player with no cards in hand can still choose to discard and discards
nothing, so no "whenever an opponent discards" trigger happens), 601.2 / 603.6a (a card put onto the battlefield is not
cast, so "when you cast" triggers do not happen, but enters-the-battlefield triggers do), 513.1 (end step triggers;
Eggman's trigger resolves before cleanup, 514.1 hand size 7), 500.9 / Y'shtola Rhul (additional end step), 301.7a / 702.122a (a Vehicle is a creature only once crewed).

This is a bounded rules/qualification-count model over fixed, enumerated states, NOT a game engine, simulation or
win-rate measurement; it supports no improvement claim by itself. It contains the bounded finite version of the two
M6 Pass C #15 requested tests: (a) +Goblin Welder / -Liliana's Caress over a fixed grid of opponent hand sizes, the
opponents' two extreme villainous-choice policies, our payloads in hand, The Valeyard on/off, and our own artifact
graveyard/fodder states; (b) 31 vs 32 vs 33 lands as exact multivariate-hypergeometric access to {2}{U}{B}{R} by
turn 5. Opponents' real decisions, responses, graveyard hate and matchups are not modelled; those remain limitations.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
from math import comb
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Dr__Eggman"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RC = ROOT / "data/grixis/m7/research_challengers"
LAND32 = RC / f"{D}_six_PassC_32lands_SilverbluffBridge_over_Thoughtcast_20261023.txt"
WELDER = RC / f"{D}_six_PassC_GoblinWelder_over_LilianasCaress_20261023.txt"
SPELLBOOK = RC / f"{D}_CommanderSpellbook_20261023.json"
EGGMAN = "Dr. Eggman"
ADDS = ["Behemoth of Vault 0", "Interceptor Mechan", "Possession Engine", "Skysovereign, Consul Flagship",
        "Su-Chi Cave Guard"]
CUTS = ["Blasphemous Act", "Cryptothrall", "Cybermen Squadron", "Foundry Inspector", "Unwinding Clock"]
GAME_CHANGERS = ["Ancient Tomb", "Cyclonic Rift", "Fierce Guardianship"]
# Owner's 2026-10-14 closeout removed or explicitly rejected these; none may come back unflagged.
OWNER_REMOVED = ["Megrim", "Great Intelligence's Plan", "Steel Overseer", "Efficient Construction",
                 "Mechanized Production", "Big Mother Mouser", "Reaver Titan", "Thopter Spy Network",
                 "Etherium Sculptor", "Dragonskull Summit", "Drowned Catacomb", "Sulfur Falls"]
OWNER_REJECTED = ["Ruin Grinder", "Mirrorworks", "Torrential Gearhulk", "Imposter Mech", "Scrawling Crawler",
                  "Pinnacle Emissary", "Damocles Base, Sword of Kang", "Chameleon, Master of Disguise", "Auton Soldier",
                  "Sakashima of a Thousand Faces", "Darksteel Forge", "Phyrexian Metamorph", "Chief of the Foundry",
                  "Raiders' Wake"]
DISCARD_PAYOFFS = ["Entropic Battlecruiser", "Geth's Grimoire", "Liliana's Caress", "Tinybones, Bauble Burglar",
                   "Waste Not"]
# Lands-only colours (fetches: the basic land types they can fetch; Exotic Orchard is opponent-dependent and is
# counted both as UBR (headline, four-player pods) and as colourless (conservative)). Rocks counted for metric B:
# Sol Ring, Fellwar Stone (colourless-conservative), Arcane Signet, three Talismans; Mox Opal excluded (metalcraft).
LAND_COLORS = {
    "Academy Ruins": "", "Ancient Tomb": "", "Badlands": "BR", "Blood Crypt": "BR", "Bloodstained Mire": "BR",
    "City of Brass": "UBR", "Command Tower": "UBR", "Exotic Orchard": "UBR", "Great Furnace": "R",
    "Inventors' Fair": "", "Island": "U", "Luxury Suite": "BR", "Mana Confluence": "UBR", "Morphic Pool": "UB",
    "Mountain": "R", "Polluted Delta": "UB", "Scalding Tarn": "UR", "Seat of the Synod": "U",
    "Silverbluff Bridge": "UR", "Spire of Industry": "UBR", "Steam Vents": "UR", "Swamp": "B", "Training Center": "UR",
    "Underground Sea": "UB", "Urza's Saga": "", "Vault of Whispers": "B", "Volcanic Island": "UR",
    "Watery Grave": "UB", "Xander's Lounge": "UBR"}
ROCKS = {"Sol Ring": "", "Fellwar Stone": "", "Arcane Signet": "UBR", "Talisman of Creativity": "UR",
         "Talisman of Dominance": "UB", "Talisman of Indulgence": "BR"}


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


def front_type(c):
    return c["type_line"].split(" // ")[0]


def is_payload(c):
    sub = front_type(c).split(" — ", 1)[1] if " — " in front_type(c) else ""
    return bool(re.search(r"\b(Construct|Robot|Vehicle)\b", sub))


def library(deck):
    lib = Counter(deck)
    lib[EGGMAN] -= 1
    return +lib


BIT = {"U": 1, "B": 2, "R": 4}


def eggman_access(deck, seen, orchard="UBR"):
    """Exact multivariate-hypergeometric DP over the 99. A: P(>=5 lands among `seen`). B: P(min(lands,5)+rocks >= 5,
    lands >= 3 and the distinct coloured sources seen cover U, B and R). Each land or rock is counted once."""
    cat = Counter()
    for n, q in library(deck).items():
        if n in LAND_COLORS:
            col = orchard if n == "Exotic Orchard" else LAND_COLORS[n]
            cat[("L", col)] += q
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
                key = (min(lands + (k if typ == "L" else 0), 6), min(rocks + (k if typ == "R" else 0), 6),
                       m | (sum(BIT[ch] for ch in col) if k and typ != "X" else 0))
                out[key] += v * comb(n, k)
        return dict(out)

    res, den = f(0, seen), comb(99, seen)
    a = Fraction(sum(v for (l, r, m), v in res.items() if l >= 5), den)
    b = Fraction(sum(v for (l, r, m), v in res.items() if min(l, 5) + r >= 5 and m == 7 and l >= 3), den)
    return a, b


def villainous(hands, payloads, valeyard, policy):
    """Three opponents in turn order face Eggman's choice once (twice with The Valeyard). policy 'discard' = an opponent
    discards whenever it has a card (it may still "discard" with an empty hand, 701.55b, which does nothing); 'put' = it
    always lets us put. We put whenever allowed and a payload is in hand (shared across opponents). Returns (cards
    actually discarded, payloads put, free no-op outs taken by opponents)."""
    hands, payloads = list(hands), payloads
    discarded = put = free = 0
    for i in range(len(hands)):
        for _ in range(2 if valeyard else 1):
            if policy == "discard":
                if hands[i] > 0:
                    hands[i] -= 1
                    discarded += 1
                else:
                    free += 1
            else:
                if payloads > 0:
                    payloads -= 1
                    put += 1
                else:
                    free += 1
    return discarded, put, free


def trigger_count(throne, spark, resonator, yshtola):
    """Eggman triggers in one of our turns. Roaming Throne naming Human (or Scientist) makes each Eggman-type creature's
    trigger happen twice; a nonlegendary Spark Double copy is a second Eggman; Strionic Resonator copies one trigger once
    per untap ({2},{T}); Y'shtola Rhul's first end step adds a second end step."""
    per_step = (1 + spark) * (2 if throne else 1)
    steps = 2 if yshtola else 1
    return per_step * steps + (1 if resonator else 0)


class EggmanOracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.base, cls.cand = names(BASE), names(CAND)

    def test_commander_oracle(self):
        c = self.o[EGGMAN]
        self.assertEqual(c["oracle_text"], "Flying\nAt the beginning of your end step, draw a card. Then each opponent "
                         "faces a villainous choice — That player discards a card, or you may put a Construct, Robot, or "
                         "Vehicle card from your hand onto the battlefield.")
        self.assertEqual((c["mana_cost"], c["type_line"]), ("{2}{U}{B}{R}", "Legendary Creature — Human Scientist"))
        self.assertEqual((c["power"], c["toughness"], c["commander_legality"], c["game_changer"]), ("3", "6", "legal", False))
        self.assertEqual((c["set"], c["released_at"]), ("sld", "2025-07-14"))

    def test_add_and_cut_oracle_anchors(self):
        o = self.o
        self.assertIn("When this Vehicle enters, gain control of target creature an opponent controls for as long as you "
                      "control this Vehicle", o["Possession Engine"]["oracle_text"])
        self.assertIn("Whenever Skysovereign enters or attacks, it deals 3 damage", o["Skysovereign, Consul Flagship"]["oracle_text"])
        self.assertIn("When this creature enters, return target artifact or creature card from your graveyard to your "
                      "hand", o["Interceptor Mechan"]["oracle_text"])
        self.assertIn("Ward {4}", o["Su-Chi Cave Guard"]["oracle_text"])
        self.assertIn("When this creature dies, add eight {C}", o["Su-Chi Cave Guard"]["oracle_text"])
        self.assertIn("When this creature enters, you get {E}{E}{E}{E}", o["Behemoth of Vault 0"]["oracle_text"])
        self.assertIn("destroy that permanent", o["Behemoth of Vault 0"]["oracle_text"])
        self.assertIn("deals 13 damage to each creature", o["Blasphemous Act"]["oracle_text"])
        self.assertIn("Nonlegendary artifact creatures you control have myriad", o["Cybermen Squadron"]["oracle_text"])
        self.assertIn("Other artifact creatures you control have hexproof", o["Cryptothrall"]["oracle_text"])
        self.assertIn("Untap all artifacts you control during each other player's untap step", o["Unwinding Clock"]["oracle_text"])
        self.assertEqual(o["Foundry Inspector"]["oracle_text"], "Artifact spells you cast cost {1} less to cast.")
        self.assertIn("they face that choice an additional time", o["The Valeyard"]["oracle_text"])
        self.assertIn("it triggers an additional time", o["Roaming Throne"]["oracle_text"])
        self.assertIn("there is an additional end step after this step", o["Y'shtola Rhul"]["oracle_text"])
        self.assertIn("When you cast this spell and whenever this creature attacks", o["Cityscape Leveler"]["oracle_text"])
        self.assertIn("that player loses 2 life", o["Liliana's Caress"]["oracle_text"])
        self.assertIn("that player simultaneously sacrifices the artifact and returns the artifact card to the battlefield",
                      o["Goblin Welder"]["oracle_text"])

    def test_swaps_identity_singleton_and_game_changers(self):
        self.assertEqual(sorted(set(self.cand) - set(self.base)), ADDS)
        self.assertEqual(sorted(set(self.base) - set(self.cand)), CUTS)
        self.assertEqual((sum(self.base.values()), sum(self.cand.values())), (100, 100))
        for n, q in self.cand.items():
            c = self.o[n]
            self.assertTrue(set(c["color_identity"]) <= set("UBR"), n)
            self.assertEqual(c["commander_legality"], "legal", n)
            if q > 1:
                self.assertIn("Basic", c["type_line"], n)
        gc = lambda d: sorted(n for n in d if self.o[n]["game_changer"])
        self.assertEqual(gc(self.base), GAME_CHANGERS)
        self.assertEqual(gc(self.cand), GAME_CHANGERS)
        self.assertFalse(self.o["Mox Opal"]["game_changer"])
        self.assertTrue(self.o["Tergrid, God of Fright"]["game_changer"])  # why the Tergrid alternative is GC #4

    def test_owner_removed_and_rejected_not_readded(self):
        for n in OWNER_REMOVED + OWNER_REJECTED:
            self.assertNotIn(n, self.cand, n)
        self.assertEqual(sorted(n for n in self.cand if n in DISCARD_PAYOFFS), DISCARD_PAYOFFS)  # no extra punisher
        self.assertFalse(any("anthem" in n.lower() for n in ADDS))
        for n in ADDS:
            self.assertNotIn("other artifact creatures you control get", self.o[n]["oracle_text"].lower(), n)

    def test_payload_density_and_cut_classification(self):
        pay = lambda d: sum(q for n, q in d.items() if n != EGGMAN and is_payload(self.o[n]))
        self.assertEqual((pay(self.base), pay(self.cand)), (28, 31))
        self.assertTrue(all(is_payload(self.o[n]) for n in ADDS))
        self.assertEqual([n for n in CUTS if is_payload(self.o[n])], ["Cryptothrall", "Foundry Inspector"])
        self.assertIn("Cyberman", self.o["Cybermen Squadron"]["type_line"])
        self.assertIn("Spacecraft", self.o["Entropic Battlecruiser"]["type_line"])
        self.assertFalse(is_payload(self.o["Entropic Battlecruiser"]))
        # exact P(no payload among the first n of the 99): opening 7 and 12 seen (turn 5 on the draw)
        p0 = lambda k, n: round(Fraction(comb(99 - k, n), comb(99, n)).__float__(), 4)
        self.assertEqual((p0(28, 7), p0(31, 7)), (0.0893, 0.0651))
        self.assertEqual((p0(28, 12), p0(31, 12)), (0.0139, 0.0079))
        self.assertEqual((Fraction(12 * 28, 99), Fraction(12 * 31, 99)), (Fraction(112, 33), Fraction(124, 33)))

    def test_cast_versus_put(self):
        cast_only = sorted(n for n in self.cand if is_payload(self.o[n]) and "When you cast" in self.o[n]["oracle_text"])
        self.assertEqual(cast_only, ["Cityscape Leveler"])
        for n in ADDS:  # every add's value is an ETB, attack or dies trigger or a static, all live when put
            self.assertNotIn("When you cast", self.o[n]["oracle_text"], n)
        etb = [n for n in ADDS if "enters" in self.o[n]["oracle_text"]]
        self.assertEqual(sorted(etb), ["Behemoth of Vault 0", "Interceptor Mechan", "Possession Engine",
                                       "Skysovereign, Consul Flagship"])
        self.assertIn("Artifact spells you cast", self.o["Foundry Inspector"]["oracle_text"])  # cast-only reducer

    def test_recursion_to_hand_feeding_eggman(self):
        to_hand = [n for n in self.cand if re.search(r"from your graveyard (to|on top of)", self.o[n]["oracle_text"])
                   or "card in your graveyard with lesser mana value" in self.o[n]["oracle_text"]]
        self.assertTrue({"Academy Ruins", "Golbez, Crystal Collector", "Interceptor Mechan", "Scrap Trawler",
                         "Tezzeret, Master of the Bridge"} <= set(to_hand), to_hand)
        self.assertNotIn("Interceptor Mechan", self.base)

    def test_spellbook_no_included_combo(self):
        s = json.loads(SPELLBOOK.read_text())
        self.assertEqual((len(s["baseline"]["included"]), len(s["candidate"]["included"])), (0, 0))


class PassCBoundedMeasuredTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base, cls.cand = names(BASE), names(CAND)

    def test_villainous_choice_grid(self):
        grid = {}
        for h, p, v, pol in product(range(4), range(4), (False, True), ("discard", "put")):
            grid[(h, p, v, pol)] = villainous((h, h, h), p, v, pol)
        self.assertEqual(len(grid), 64)
        # empty-handed opponents always have a free out under the discard branch (701.55b)
        for p, v in product(range(4), (False, True)):
            self.assertEqual(grid[(0, p, v, "discard")], (0, 0, 6 if v else 3))
        # with no payload in hand the put branch is free for every opponent
        for h, v in product(range(4), (False, True)):
            self.assertEqual(grid[(h, 0, v, "put")], (0, 0, 6 if v else 3))
        # The Valeyard doubles choices, not draws: 3 -> 6 decisions; payloads put capped by payloads in hand
        self.assertEqual(grid[(3, 3, True, "discard")], (6, 0, 0))
        self.assertEqual(grid[(3, 3, True, "put")], (0, 3, 3))
        self.assertEqual(grid[(3, 3, False, "put")], (0, 3, 0))
        free_cells = sum(1 for k, r in grid.items() if r[2] > 0)
        self.assertEqual(free_cells, 40)  # 40/64 cells give at least one opponent a no-cost answer

    def test_trigger_multipliers_are_finite(self):
        counts = {k: trigger_count(*k) for k in product((0, 1), repeat=4)}
        self.assertEqual(counts[(0, 0, 0, 0)], 1)
        self.assertEqual(counts[(1, 0, 0, 0)], 2)
        self.assertEqual(counts[(0, 0, 0, 1)], 2)
        self.assertEqual(counts[(1, 1, 1, 1)], 9)
        self.assertEqual(max(counts.values()), 9)  # bounded: 9 draws and, with The Valeyard, 18 choices per opponent

    def test_welder_versus_caress(self):
        """Finite grid: opponent hands 0..3 (all three equal), Valeyard off/on, payload in hand 0/1, opponent policy
        discard/put, our artifact cards in graveyard 0..2 and an artifact we would trade 0/1. Caress drains 2 per actual
        discard per Eggman trigger; Welder makes at most one exchange per turn cycle once it is untapped, putting the
        artifact straight onto the battlefield (not into hand, so it does not feed Eggman)."""
        caress_live = welder_live = cells = 0
        caress_life = Counter()
        for h, v, p, pol, g, a in product(range(4), (False, True), (0, 1), ("discard", "put"), range(3), (0, 1)):
            cells += 1
            d, _, _ = villainous((h, h, h), p, v, pol)
            caress_life[(h, v, pol)] = 2 * d
            caress_live += d > 0
            welder_live += g >= 1 and a >= 1
        self.assertEqual(cells, 192)
        self.assertEqual(caress_live, 72)   # live in 3/8 of cells: needs an opponent to choose to discard a real card
        self.assertEqual(welder_live, 64)   # live in 1/3 of cells: needs an artifact card already in our graveyard
        self.assertEqual(caress_life[(3, True, "discard")], 12)
        self.assertEqual(caress_life[(3, False, "discard")], 6)
        self.assertEqual(caress_life[(3, True, "put")], 0)
        # Caress is one of exactly five actual-discard payoffs; Welder would make it four. Neither changes the put branch.
        self.assertEqual(sum(1 for n in names(WELDER) if n in DISCARD_PAYOFFS), 4)
        self.assertEqual(sorted(set(names(WELDER)) - set(self.cand)), ["Goblin Welder"])

    def test_exact_land_access_31_32_33(self):
        land32 = names(LAND32)
        land33 = Counter(land32)
        land33["Thought Monitor"] -= 1
        land33 = +land33
        land33["Drossforge Bridge"] = 1
        LAND_COLORS["Drossforge Bridge"] = "BR"
        lands = lambda d: sum(q for n, q in d.items() if n in LAND_COLORS)
        self.assertEqual((lands(self.base), lands(self.cand), lands(land32), lands(land33)), (31, 31, 32, 33))
        got = {}
        for label, deck in (("base", self.base), ("cand", self.cand), ("32", land32), ("33", land33)):
            got[label] = [tuple(round(float(x), 4) for x in eggman_access(deck, n)) for n in (11, 12)]
        self.assertEqual(got["base"], [(0.2289, 0.3751), (0.3032, 0.4696)])
        self.assertEqual(got["cand"], got["base"])  # no mana change in the preferred five
        self.assertEqual(got["32"], [(0.2539, 0.404), (0.3328, 0.5009)])
        self.assertEqual(got["33"], [(0.2798, 0.4333), (0.3631, 0.532)])
        cons = [round(float(eggman_access(self.cand, n, orchard="")[1]), 4) for n in (11, 12)]
        self.assertTrue(all(c <= g for c, g in zip(cons, (0.3751, 0.4696))))


if __name__ == "__main__":
    unittest.main()
