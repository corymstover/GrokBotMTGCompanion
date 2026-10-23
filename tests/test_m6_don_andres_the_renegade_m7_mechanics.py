"""Finite source-anchored rules/mana cases for the Don Andres, the Renegade M7 candidate.

Seed 0, no randomness. Don Andres is modelled exactly as printed (current Oracle in the M7 snapshot): "Each creature
you control but don't own gets +2/+2, has menace and deathtouch, and is a Pirate in addition to its other types." and
"Whenever you cast a noncreature spell you don't own, create two tapped Treasure tokens." Ownership: CR 108.3 (card
owner = the player who started with it), 110.2 (permanent owner = card owner), 111.2 (token owner = its creator),
707.10 (a copy of a spell is not cast). Don's Treasures enter tapped, so they never pay for the spell that made them or
for anything else on the turn they are created unless something untaps them (Pass C #14 point kept).

This is a bounded rules/qualification-count model over fixed, enumerated states, NOT a game engine, simulation or
win-rate measurement; it supports no improvement claim by itself. It contains the bounded finite version of the two
M6 Pass C #14 requested tests: (a) Mob Rule vs Insurrection at 6/7/8 available mana over five fixed mixed-power
opponent tables, with Don on the battlefield or removed before combat; (b) Bribery vs the two named theft cuts
(Thieving Amalgam, Jhoira, Weatherlight Corsair) over five opponent creature densities, counting opponent-owned
permanents gained and the number of opponent turns before the first one arrives. Opponents' decisions, blocks, hand
contents, responses and matchups are not modelled; those remain explicit limitations.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Don_Andres__the_Renegade"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
SPELLBOOK = ROOT / f"data/grixis/m7/research_challengers/{D}_CommanderSpellbook_20261023.json"
DON = "Don Andres, the Renegade"
ADDS = ["Gríma, Saruman's Footman", "Fallen Shinobi", "Treachery", "Gloomlake Verge", "Blazemire Verge"]
CUTS = ["Professional Face-Breaker", "Seize the Spotlight", "Blasphemous Act", "Shipwreck Marsh", "Smoldering Marsh"]
CORE = ["Thieving Amalgam", "Jhoira, Weatherlight Corsair", "Roaming Throne", "Thieving Varmint", "Gonti, Night Minister",
        "Hostage Taker", "Gilded Drake", "Insurrection", "Coercive Recruiter", "Arcane Heist", "Dire Fleet Daredevil",
        "Siphon Insight", "Praetor's Grasp", "Opposition Agent", "Tasha, the Witch Queen", "Vaan, Street Thief"]
GAME_CHANGERS = ["Ancient Tomb", "Cyclonic Rift", "Fierce Guardianship", "Opposition Agent", "Vampiric Tutor"]
# Owner's 2026-10-14 approval removed these; none may come back unflagged.
OWNER_REMOVED = ["Buried Alive", "Living Death", "Victimize", "Cunning Rhetoric", "Share the Spoils",
                 "The Ruinous Powers", "Revel in Riches", "Gonti, Lord of Luxury", "Zara, Renegade Recruiter",
                 "Crumbling Necropolis", "Drowned Catacomb", "Haunted Ridge", "Stormcarved Coast"]

# Colours each land can produce (fetches: the colours of the typed lands they can find in this list; Exotic Orchard is
# opponent-dependent and counted colourless; Cavern of Souls' coloured mana only casts a creature of the chosen type, so
# it counts for Don (Vampire Pirate) but not for noncreature spells; the Verges' second colour needs an Island/Swamp or
# Swamp/Mountain, so they are counted at their unconditional colour only (conservative)).
LAND_COLORS = {
    "Ancient Tomb": "", "Badlands": "BR", "Blood Crypt": "BR", "Bloodstained Mire": "UBR", "Cavern of Souls": "UBR*",
    "City of Brass": "UBR", "Command Tower": "UBR", "Exotic Orchard": "", "Island": "U", "Luxury Suite": "BR",
    "Mana Confluence": "UBR", "Marsh Flats": "UBR", "Misty Rainforest": "UBR", "Morphic Pool": "UB", "Mountain": "R",
    "Otawara, Soaring City": "U", "Path of Ancestry": "UBR", "Polluted Delta": "UBR", "Scalding Tarn": "UBR",
    "Shipwreck Marsh": "UB", "Shivan Reef": "UR", "Smoldering Marsh": "BR", "Steam Vents": "UR", "Sulfur Falls": "UR",
    "Sulfurous Springs": "BR", "Swamp": "B", "Takenuma, Abandoned Mire": "B", "Training Center": "UR",
    "Underground River": "UB", "Underground Sea": "UB", "Verdant Catacombs": "UBR", "Volcanic Island": "UR",
    "Watery Grave": "UB", "Xander's Lounge": "UBR", "Gloomlake Verge": "U", "Blazemire Verge": "B"}
VERGE_FULL = {"Gloomlake Verge": "UB", "Blazemire Verge": "BR"}
# Lands that can enter untapped as the first or second land with no condition (multiplayer: Luxury Suite, Morphic Pool
# and Training Center are untapped with two or more opponents; shocks pay 2 life; fetches find an untapped dual).
CONDITIONAL_OR_TAPPED_EARLY = {"Path of Ancestry": "always tapped", "Xander's Lounge": "always tapped",
                               "Shipwreck Marsh": "tapped unless two other lands",
                               "Smoldering Marsh": "tapped unless two basic lands (list has four basics)",
                               "Sulfur Falls": "tapped unless an Island or a Mountain"}


def names(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split(" ", 1)
            out[raw.removesuffix(" [Commander]")] += int(q.rstrip("x"))
    return out


def oracle():
    out = {}
    for c in json.loads(SNAP.read_text())["cards"]:
        out[c["name"]] = out[c["name"].split(" // ")[0]] = c
    return out


def land_groups(deck, creature_spell, verge_full=False):
    g = Counter()
    for n, q in deck.items():
        if n not in LAND_COLORS:
            continue
        c = VERGE_FULL.get(n, LAND_COLORS[n]) if verge_full else LAND_COLORS[n]
        if c.endswith("*"):
            c = c[:-1] if creature_spell else ""
        g[c] += q
    return g


def _hall(counts, need):
    for r in range(1, len(need) + 1):
        for sub in combinations(need, r):
            if sum(k for cs, k in counts.items() if any(c in cs for c in sub)) < sum(need[c] for c in sub):
                return False
    return True


def colour_access(deck, seen, need, lands_needed, creature_spell, verge_full=False, size=99):
    """Exact multivariate-hypergeometric P(>= lands_needed lands among the top `seen` of the 99 AND distinct lands can
    pay the coloured pips in `need` (Hall's condition)). Lands only: rocks, Treasures and fetch shuffles excluded."""
    g = land_groups(deck, creature_spell, verge_full)
    keys = sorted(g)
    nonland = size - sum(g.values())
    tot, p = comb(size, seen), Fraction(0)
    for ks in product(*[range(min(g[k], seen) + 1) for k in keys]):
        s = sum(ks)
        if s > seen:
            continue
        counts = dict(zip(keys, ks))
        if s >= lands_needed and _hall(counts, need):
            w = 1
            for k, x in counts.items():
                w *= comb(g[k], x)
            p += Fraction(w * comb(nonland, seen - s), tot)
    return p


# ---- Pass C test (a): Mob Rule vs Insurrection ----
# Fixed mixed-power tables: opponents' untapped creature powers (printed power at resolution; CR 608.2h: Mob Rule's
# power check happens once, on resolution, before Don's +2/+2 applies to the stolen creatures).
TABLES = {"go_wide_small": [[1, 1, 1, 2, 2, 3], [1, 1], [2]],
          "big_stompy": [[5, 6, 4], [4], [7, 2]],
          "mixed": [[2, 4, 1, 5], [3, 6], [1]],
          "creature_light": [[1, 2], [], [3]],
          "one_big_threat": [[8], [1, 1], [2, 2]]}
COST = {"mob_rule": 6, "insurrection": 8}


def mass_steal(spell, table, mana, don_alive):
    """(castable, creatures stolen, stolen power after Don's static, opponents left with no untapped creature)."""
    if mana < COST[spell]:
        return (False, 0, 0, 0)
    allc = [p for opp in table for p in opp]
    if spell == "insurrection":
        took = [list(opp) for opp in table]
    else:
        big = [[p for p in opp if p >= 4] for opp in table]
        small = [[p for p in opp if p <= 3] for opp in table]
        pw = lambda t: sum(sum(o) for o in t) + (2 * sum(len(o) for o in t) if don_alive else 0)
        took = big if (pw(big), sum(map(len, big))) >= (pw(small), sum(map(len, small))) else small
    n = sum(map(len, took))
    power = sum(sum(o) for o in took) + (2 * n if don_alive else 0)
    left_empty = sum(1 for opp, t in zip(table, took) if len(opp) == len(t))
    assert n <= len(allc)
    return (True, n, power, left_empty)


def steal_grid():
    return {(s, t, m, a): mass_steal(s, TABLES[t], m, a)
            for s in COST for t in TABLES for m in (6, 7, 8) for a in (True, False)}


# ---- Pass C test (b): Bribery vs Thieving Amalgam / Jhoira ----
LIB = 85  # an opponent's library size in the bounded model (99-card deck after an opening hand and a few draws)


def bribery(creatures_in_library):
    """One opponent-owned creature immediately (the best one) iff the targeted library has a creature card."""
    hit = 1 if creatures_in_library > 0 else 0
    return dict(first_after_opp_turns=0 if hit else None, by_next_own_turn=hit, after_two_rounds=hit,
                don_triggers=0)  # Bribery is our own card: no Don trigger; the creature gets Don's static


def amalgam(creatures_in_library, opponents=3):
    """Manifests one card at each opponent's upkeep: each manifest is an opponent-owned 2/2 (4/4 menace deathtouch
    Pirate with Don). P(a manifest can be turned face up) = creature density (CR 701.40b; 701.40g for instants/sorceries)."""
    return dict(first_after_opp_turns=1, by_next_own_turn=opponents, after_two_rounds=2 * opponents,
                face_up_fraction=Fraction(creatures_in_library, LIB), don_triggers=0)


def jhoira(historic_in_library, attacks_survived=1):
    """ETB plus each attack: reveal until a historic permanent card; we get it and lose life equal to its mana value.
    Expected cards revealed per trigger = (N+1)/(h+1) (exact, sampling without replacement)."""
    hit = 1 if historic_in_library > 0 else 0
    return dict(first_after_opp_turns=0 if hit else None, by_next_own_turn=hit,
                after_two_rounds=hit * (1 + attacks_survived),
                expected_revealed=Fraction(LIB + 1, historic_in_library + 1) if hit else None, don_triggers=0)


DENSITIES = [0, 4, 8, 15, 25]


# ---- Commander-first payoff anchors ----
def shinobi_expected_don_triggers(noncreature_nonland, size=LIB):
    """Fallen Shinobi hit: the top two cards are exiled and may be played free this turn. Each noncreature spell we
    cast that way is opponent-owned: two tapped Treasures. Exact expectation over the two cards."""
    return 2 * Fraction(noncreature_nonland, size)


def treasure_chain(own_untapped_mana, stolen_noncreature_costs):
    """Don's Treasures enter tapped: they never pay for later spells in the same chain. Returns spells cast and
    tapped Treasures made (usable next turn)."""
    cast, tapped = 0, 0
    for c in stolen_noncreature_costs:
        if c > own_untapped_mana:
            break
        own_untapped_mana -= c
        cast += 1
        tapped += 2
    return cast, tapped


class DonOracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_commander_oracle(self):
        c = self.o[DON]
        t = c["oracle_text"]
        self.assertIn("Each creature you control but don't own gets +2/+2, has menace and deathtouch, and is a Pirate in "
                      "addition to its other types.", t)
        self.assertIn("Whenever you cast a noncreature spell you don't own, create two tapped Treasure tokens.", t)
        self.assertEqual(c["mana_cost"], "{1}{U}{B}{R}")
        self.assertIn("Vampire Pirate", c["type_line"])
        self.assertEqual(c["commander_legality"], "legal")

    def test_add_oracle_anchors(self):
        o = self.o
        g = o["Gríma, Saruman's Footman"]["oracle_text"]
        self.assertIn("can't be blocked", g)
        self.assertIn("exiles cards from the top of their library until they exile an instant or sorcery card. You may "
                      "cast that card without paying its mana cost", g)
        s = o["Fallen Shinobi"]["oracle_text"]
        self.assertIn("Ninjutsu {2}{U}{B}", s)
        self.assertIn("exiles the top two cards of their library. Until end of turn, you may play those cards without "
                      "paying their mana costs", s)
        t = o["Treachery"]["oracle_text"]
        self.assertIn("untap up to five lands", t)
        self.assertIn("You control enchanted creature.", t)
        self.assertIn("Activate only if you control an Island or a Swamp.", o["Gloomlake Verge"]["oracle_text"])
        self.assertIn("Activate only if you control a Swamp or a Mountain.", o["Blazemire Verge"]["oracle_text"])
        self.assertIn("enters tapped unless you control two or more other lands", o["Shipwreck Marsh"]["oracle_text"])
        self.assertIn("enters tapped unless you control two or more basic lands", o["Smoldering Marsh"]["oracle_text"])
        self.assertIn("deals 13 damage to each creature", o["Blasphemous Act"]["oracle_text"])
        self.assertIn("Each opponent chooses fame or fortune", o["Seize the Spotlight"]["oracle_text"])
        self.assertIn("Exile the top card of your library", o["Professional Face-Breaker"]["oracle_text"])

    def test_pass_c_card_anchors(self):
        o = self.o
        self.assertEqual(o["Mob Rule"]["mana_cost"], "{4}{R}{R}")
        self.assertIn("power 4 or greater", o["Mob Rule"]["oracle_text"])
        self.assertIn("power 3 or less", o["Mob Rule"]["oracle_text"])
        self.assertEqual(o["Insurrection"]["mana_cost"], "{5}{R}{R}{R}")
        self.assertIn("Untap all creatures and gain control of them until end of turn", o["Insurrection"]["oracle_text"])
        self.assertIn("Search target opponent's library for a creature card", o["Bribery"]["oracle_text"])
        self.assertIn("you manifest the top card of that player's library", o["Thieving Amalgam"]["oracle_text"])
        self.assertIn("until they reveal a historic permanent card", o["Jhoira, Weatherlight Corsair"]["oracle_text"])
        self.assertIn("triggers an additional time", o["Roaming Throne"]["oracle_text"])
        self.assertIn("Spend this mana only to cast spells you don't own", o["Thieving Varmint"]["oracle_text"])

    def test_swaps_identity_singleton_and_game_changers(self):
        self.assertEqual(sorted(set(self.cand) - set(self.base)), sorted(ADDS))
        self.assertEqual(sorted(set(self.base) - set(self.cand)), sorted(CUTS))
        self.assertEqual(sum(self.cand.values()), 100)
        self.assertEqual(sum(self.base.values()), 100)
        for n in CORE:
            self.assertIn(n, self.cand, n)
        for n, q in self.cand.items():
            c = self.o[n]
            self.assertTrue(set(c["color_identity"]) <= set("UBR"), n)
            self.assertEqual(c["commander_legality"], "legal", n)
            if q > 1:
                self.assertIn("Basic", c["type_line"], n)
        gc = lambda deck: sorted(n for n in deck if self.o[n]["game_changer"])
        self.assertEqual(gc(self.base), GAME_CHANGERS)
        self.assertEqual(gc(self.cand), GAME_CHANGERS)  # 5 Game Changers either way: Bracket 4 ceiling unchanged

    def test_owner_removed_classes_not_readded(self):
        for n in OWNER_REMOVED:
            self.assertNotIn(n, self.cand, n)

    def test_land_count_and_table_complete(self):
        lands = lambda deck: sum(q for n, q in deck.items() if "Land" in self.o[n]["type_line"].split(" // ")[0])
        self.assertEqual((lands(self.base), lands(self.cand)), (35, 35))
        for deck in (self.base, self.cand):
            self.assertEqual(sorted(n for n in deck if "Land" in self.o[n]["type_line"].split(" // ")[0]),
                             sorted(n for n in deck if n in LAND_COLORS))

    def test_early_conditional_or_tapped_lands(self):
        b = sorted(n for n in self.base if n in CONDITIONAL_OR_TAPPED_EARLY)
        c = sorted(n for n in self.cand if n in CONDITIONAL_OR_TAPPED_EARLY)
        self.assertEqual(len(b), 5)
        self.assertEqual(c, ["Path of Ancestry", "Sulfur Falls", "Xander's Lounge"])
        basics = sum(q for n, q in self.cand.items() if "Basic" in self.o[n]["type_line"])
        self.assertEqual(basics, 4)  # why Smoldering Marsh was usually tapped
        islands_swamps = [n for n in self.cand if any(t in self.o[n]["type_line"] for t in ("Island", "Swamp"))]
        swamps_mountains = [n for n in self.cand if any(t in self.o[n]["type_line"] for t in ("Swamp", "Mountain"))]
        self.assertEqual((len(islands_swamps), len(swamps_mountains)), (9, 9))  # names that switch on the Verges

    def test_spellbook_no_included_combo(self):
        s = json.loads(SPELLBOOK.read_text())
        self.assertEqual((s["baseline"]["included"], s["candidate"]["included"]), ([], []))


class PassCBoundedMeasuredTests(unittest.TestCase):
    """Pass C #14 requested tests, run as bounded finite versions."""

    # (a) Mob Rule vs Insurrection
    def test_castability_by_mana(self):
        g = steal_grid()
        self.assertEqual(len(g), 60)
        for t in TABLES:
            for a in (True, False):
                self.assertTrue(all(g[("mob_rule", t, m, a)][0] for m in (6, 7, 8)))
                self.assertEqual([g[("insurrection", t, m, a)][0] for m in (6, 7, 8)], [False, False, True])

    def test_insurrection_dominates_at_eight(self):
        g = steal_grid()
        for t in TABLES:
            for a in (True, False):
                i, m = g[("insurrection", t, 8, a)], g[("mob_rule", t, 8, a)]
                self.assertGreaterEqual(i[1], m[1])
                self.assertGreaterEqual(i[2], m[2])
        got = {t: (g[("mob_rule", t, 8, True)][1:3], g[("insurrection", t, 8, True)][1:3]) for t in TABLES}
        self.assertEqual(got, {"go_wide_small": ((9, 32), (9, 32)), "big_stompy": ((5, 36), (6, 40)),
                               "mixed": ((3, 21), (7, 36)), "creature_light": ((3, 12), (3, 12)),
                               "one_big_threat": ((4, 14), (5, 24))})
        self.assertEqual(sum(got[t][0] == got[t][1] for t in TABLES), 2)  # Mob Rule = Insurrection on 2/5 tables
        share = Fraction(sum(v[0][1] for v in got.values()), sum(v[1][1] for v in got.values()))
        self.assertEqual(share, Fraction(115, 144))  # Mob Rule keeps ~80% of Insurrection's stolen power at 8 mana

    def test_don_survival_changes_power_not_count(self):
        g = steal_grid()
        # don_alive=False means Don is not on the battlefield when the spell resolves or in combat.
        for t in TABLES:
            a, r = g[("insurrection", t, 8, True)], g[("insurrection", t, 8, False)]
            self.assertEqual(a[2] - r[2], 2 * a[1])  # Don's +2/+2 per stolen creature, same creatures
        self.assertEqual(g[("insurrection", "mixed", 8, False)][1:3], (7, 22))
        # Mob Rule's best mode depends on Don: one big threat, Don present -> take the four small creatures (14 power
        # after the buff); Don absent -> take the 8-power creature alone.
        self.assertEqual(g[("mob_rule", "one_big_threat", 8, True)][1:3], (4, 14))
        self.assertEqual(g[("mob_rule", "one_big_threat", 8, False)][1:3], (1, 8))
        flips = [t for t in TABLES if g[("mob_rule", t, 8, True)][1] != g[("mob_rule", t, 8, False)][1]]
        self.assertEqual(flips, ["one_big_threat"])
        # Don removed after resolution: the same creatures stay stolen until end of turn, minus 2 power each.
        no_don_power = sum(g[("insurrection", t, 8, False)][2] for t in TABLES)
        self.assertEqual(no_don_power, 84)

    def test_six_and_seven_mana_only_mob_rule(self):
        g = steal_grid()
        six = {t: g[("mob_rule", t, 6, True)][1:3] for t in TABLES}
        self.assertEqual(sum(v[1] for v in six.values()), 115)
        self.assertTrue(all(g[("insurrection", t, 7, True)] == (False, 0, 0, 0) for t in TABLES))

    # (b) Bribery vs Thieving Amalgam / Jhoira
    def test_bribery_vs_named_cuts(self):
        rows = {d: (bribery(d), amalgam(d), jhoira(d)) for d in DENSITIES}
        self.assertEqual(rows[0][0]["by_next_own_turn"], 0)  # Bribery whiffs on a creature-free library
        for d in DENSITIES:
            b, a, j = rows[d]
            self.assertEqual(a["by_next_own_turn"], 3)
            self.assertEqual(a["after_two_rounds"], 6)
            self.assertLessEqual(b["after_two_rounds"], 1)
            self.assertGreater(a["after_two_rounds"], b["after_two_rounds"])
            self.assertGreaterEqual(j["after_two_rounds"], b["after_two_rounds"])
            self.assertEqual((b["don_triggers"], a["don_triggers"], j["don_triggers"]), (0, 0, 0))
        self.assertEqual(rows[25][1]["face_up_fraction"], Fraction(5, 17))
        # turns-to-return: Bribery and Jhoira pay off on resolution; Amalgam's first body comes after one opponent upkeep
        self.assertEqual([rows[15][i]["first_after_opp_turns"] for i in range(3)], [0, 1, 0])
        self.assertEqual(jhoira(4)["expected_revealed"], Fraction(86, 5))
        self.assertEqual(jhoira(20)["expected_revealed"], Fraction(86, 21))

    # Commander-first payoff anchors for the adds
    def test_grima_and_shinobi_don_triggers(self):
        # Gríma: each connection casts one opponent-owned instant or sorcery free -> exactly 2 tapped Treasures if the
        # library holds one; Shinobi: exact expectation over two cards.
        self.assertEqual(shinobi_expected_don_triggers(30), Fraction(12, 17))
        self.assertEqual(shinobi_expected_don_triggers(0), 0)

    def test_tapped_treasures_never_fund_the_same_chain(self):
        self.assertEqual(treasure_chain(4, [2, 2, 2]), (2, 4))
        self.assertEqual(treasure_chain(0, [1]), (0, 0))

    def test_colour_access_exact(self):
        b, c = names(BASE), names(CAND)
        don = {"U": 1, "B": 1, "R": 1}
        r = lambda d, s, need, k, cr, v=False: round(float(colour_access(d, s, need, k, cr, v)), 4)
        # Don on turn 4 on the play (10 cards seen), four lands with U, B and R among them:
        self.assertEqual((r(b, 10, don, 4, True), r(c, 10, don, 4, True)), (0.4898, 0.4864))  # Verges counted 1 colour
        self.assertEqual(r(c, 10, don, 4, True, True), 0.4898)  # Verge condition met: identical colour groups
        # Three lands paying U, B and R by turn 3 (9 cards) for a noncreature spell (Cavern excluded):
        self.assertEqual((r(b, 9, don, 3, False), r(c, 9, don, 3, False), r(c, 9, don, 3, False, True)),
                         (0.5844, 0.574, 0.5844))
        # The swap's gain is tempo (two lands that never enter tapped), which this colour-only model does not count;
        # its cost is up to ~1 percentage point of colour access when a Verge's second colour is switched off.


if __name__ == "__main__":
    unittest.main()
