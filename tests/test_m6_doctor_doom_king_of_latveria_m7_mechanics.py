"""Finite source-anchored rules/mana cases for the Doctor Doom, King of Latveria M7 candidate.

Seed 0, no randomness. Doom is modelled exactly as printed (current Oracle in the M7 snapshot): "Whenever you discard
one or more land cards, each opponent loses 2 life." (once per discard event, CR 603.2c) and "At the beginning of
combat on your turn, target Villain you control gains menace until end of turn. It connives." (CR 701.50a: a land
discarded to connive drains 2 but gives no +1/+1 counter).

This is a bounded rules/qualification-count model over fixed, enumerated states, NOT a game engine, simulation or
win-rate measurement; it supports no improvement claim by itself. It contains the bounded finite version of the three
M6 Pass C #13 requested tests: (a) the Dakmor Salvage + Tectonic Reformation + Surly Badgersaur loop as a finite,
library-bounded trace with the listed interruptions; (b) a matched Glint-Horn Buccaneer / Green Goblin, Revenant /
Magmakin Artillerist grid over five fixed turn patterns x attack possible/not x removal before attacks; (c) exact
hypergeometric colour access (lands only) for {1}{U}{B}{R} and Seismic Assault's {R}{R}{R}, baseline vs candidate, plus
a static count of graveyard-independent land-discard outlets. Opponents' decisions, blocks, hand contents beyond the
listed patterns, and matchups are not modelled; those remain explicit limitations.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Doctor_Doom__King_of_Latveria"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
SPELLBOOK = ROOT / f"data/grixis/m7/research_challengers/{D}_CommanderSpellbook_20261023.json"
DOOM = "Doctor Doom, King of Latveria"
ADDS = ["Lightning Axe", "Glint-Horn Buccaneer", "Red Ghost, Intangible Genius", "Coastal Peak", "Swiftfoot Boots",
        "Mox Diamond"]
CUTS = ["Feed the Swarm", "Change of Fortune", "Loki, the Deceiver", "Shipwreck Marsh", "Fellwar Stone",
        "Talisman of Creativity"]
CORE = ["Dakmor Salvage", "Tectonic Reformation", "Surly Badgersaur", "Seismic Assault", "Green Goblin, Nemesis",
        "Green Goblin, Revenant", "Monument to Endurance", "Cool but Rude", "Villainous Hideout", "Oscorp Industries",
        "Containment Construct", "Currency Converter", "Moonstone, Harsh Mistress", "Crucible of Worlds"]
GAME_CHANGERS_BASE = ["Ancient Tomb", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship", "Jeska's Will",
                      "Vampiric Tutor"]
GAME_CHANGERS_CAND = sorted(GAME_CHANGERS_BASE + ["Mox Diamond"])
# Owner's 10-14 approval removed opponent-discard punishers and Dark Deal; none may come back unflagged.
OWNER_REMOVED_CLASS = ["Tinybones, Trinket Thief", "Kefka, Court Mage", "Syphon Mind", "Dark Deal"]

# Colours each land can produce for a spell (fetches list the colours of the typed/basic lands they can find in this
# list; Exotic Orchard is opponent-dependent and counted as colourless; Villainous Hideout's coloured mana only pays
# for Villain spells/abilities of Villain sources, so it counts for casting Doom but not for Seismic Assault or for
# Tectonic Reformation's granted cycling cost). Oscorp Industries: "{T}: Add {U}, {B}, or {R}."
LAND_COLORS = {
    "Ancient Tomb": "", "Badlands": "BR", "Blood Crypt": "BR", "Bloodstained Mire": "UBR", "Canyon Slough": "BR",
    "City of Brass": "UBR", "Coastal Peak": "UR", "Command Tower": "UBR", "Dakmor Salvage": "B",
    "Desolate Lighthouse": "", "Drowned Catacomb": "UB", "Exotic Orchard": "", "Fabled Passage": "UBR",
    "Fetid Pools": "UB", "Geier Reach Sanitarium": "", "Haunted Ridge": "BR", "Island": "U", "Luxury Suite": "BR",
    "Mana Confluence": "UBR", "Morphic Pool": "UB", "Mountain": "R", "Oscorp Industries": "UBR",
    "Otawara, Soaring City": "U", "Polluted Delta": "UBR", "Scalding Tarn": "UBR", "Shipwreck Marsh": "UB",
    "Steam Vents": "UR", "Sulfur Falls": "UR", "Sulfurous Springs": "BR", "Sunken Hollow": "UB", "Swamp": "B",
    "Takenuma, Abandoned Mire": "B", "Training Center": "UR", "Underground River": "UB", "Underground Sea": "UB",
    "Villainous Hideout": "UBR*", "Volcanic Island": "UR", "Watery Grave": "UB", "Xander's Lounge": "UBR"}


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


def dakmor_loop(library, red=1, maker="badgersaur", buccaneer=False, cool_l2=False, monument=False,
                hate_on=None, exile_dakmor=False, opp_life=40, cap=1000):
    """Finite trace of: cycle Dakmor Salvage for {R} (Tectonic Reformation) -> discard triggers resolve first
    (CR 603.3b: Doom 2, Glint-Horn 1, Cool but Rude L2 2, Badgersaur untapped Treasure or Nemesis tapped Treasure,
    Monument one unused mode) -> the cycling draw is replaced by dredge 2 only if the library has >= 2 cards
    (CR 702.52b). `red` = external {R} available (Villainous Hideout cannot provide it). `hate_on` = graveyard exiled
    in response to the cycling draw of that iteration. `exile_dakmor` = a Containment Construct / Moonstone /
    Currency Converter "you may exile" choice taken on Dakmor (the loop ends; the model's default declines it)."""
    hand, gy, tre, lib, it, drain = True, False, 0, library, 0, 0
    modes, drawn, empty = [], 0, False
    while hand and it < cap:
        if red:
            red -= 1
        elif tre:
            tre -= 1
        else:
            break
        it += 1
        hand, gy = False, not exile_dakmor
        drain += 2 + (1 if buccaneer else 0) + (2 if cool_l2 else 0)
        if maker == "badgersaur":
            tre += 1  # Nemesis makes a *tapped* Treasure: it cannot pay this turn's next {R}
        chosen = None
        if monument and len(modes) < 3:
            chosen = ("treasure", "lose3", "draw")[len(modes)]
            modes.append(chosen)
            if chosen == "treasure":
                tre += 1
            elif chosen == "lose3":
                drain += 3
        if drain >= opp_life:
            break  # state-based actions: each opponent at 0
        if chosen == "draw":  # Monument's draw resolves first and is the one replaced by dredge
            if gy and lib >= 2:
                lib, gy, hand = lib - 2, False, True
            elif lib:
                lib, drawn = lib - 1, drawn + 1
        if hate_on == it:
            gy = False
        if gy and lib >= 2:
            lib, gy, hand = lib - 2, False, True
        elif lib:
            lib, drawn = lib - 1, drawn + 1
        else:
            empty = True
    return dict(iterations=it, drain_each=drain, library_left=lib, lethal=drain >= opp_life,
                monument_modes=len(modes), drawn=drawn, drew_from_empty=empty, dakmor_in_hand=hand)


# Pass C test (b): fixed turn patterns as lists of discard events (cards discarded, lands among them).
PATTERNS = {"cycling": [(1, 1), (1, 1), (1, 1)],  # connive a land + two Reformation land cycles
            "wheel": [(1, 1), (6, 2)],  # connive a land, then a 6-card wheel holding 2 lands
            "seismic": [(1, 1)] * 4,  # connive a land + three Seismic Assault activations
            "quiet": [(1, 0)],  # connive a nonland only
            "cast_this_turn": [(1, 1)]}  # payoff cast this main phase


def payoff(card, pattern, attack, removed_before_attack):
    """Return (damage to each opponent attributable to the payoff, cards it draws) on a fixed pattern."""
    ev = PATTERNS[pattern]
    sick = pattern == "cast_this_turn"
    discarded = sum(c for c, _ in ev)
    dmg = draw = 0
    if card in ("buccaneer", "artillerist"):
        dmg += discarded  # 1 per card (Buccaneer) == "that much damage" per event (Artillerist)
        if card == "buccaneer" and attack and not removed_before_attack:  # haste: one {1}{R} attack loot of a land
            dmg += 1 + 2  # its own ping + Doom's drain for the land
            draw += 1
    elif card == "revenant":
        if attack and not removed_before_attack and not sick:  # no haste
            dmg += 2  # the attack discard is a land: Doom drains 2
            draw += discarded + 1
    return dmg, draw


def grid(card):
    return {(p, a, r): payoff(card, p, a, r) for p in PATTERNS for a in (True, False) for r in (False, True)}


def land_groups(lands, villain_spell):
    g = Counter()
    for n in lands:
        c = LAND_COLORS[n]
        if c.endswith("*"):
            c = c[:-1] if villain_spell else ""
        g[c] += 1
    return g


def _hall(counts, need):
    for r in range(1, len(need) + 1):
        for sub in combinations(need, r):
            have = sum(k for cs, k in counts.items() if any(c in cs for c in sub))
            if have < sum(need[c] for c in sub):
                return False
    return True


def colour_access(lands, seen, need, lands_needed, villain_spell, deck=99):
    """Exact multivariate-hypergeometric P(at least `lands_needed` lands seen AND distinct lands can be assigned to the
    coloured pips in `need` (Hall's condition)) among the top `seen` cards of the 99. Lands only: rocks, Mox Diamond,
    Treasures and fetch shuffles are not counted (conservative)."""
    g = land_groups(lands, villain_spell)
    keys = sorted(g)
    nonland, tot, p = deck - len(lands), comb(deck, seen), Fraction(0)
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


class DoomOracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_commander_oracle(self):
        c = self.o[DOOM]
        t = c["oracle_text"]
        self.assertIn("Whenever you discard one or more land cards, each opponent loses 2 life.", t)
        self.assertIn("At the beginning of combat on your turn, target Villain you control gains menace until end of "
                      "turn. It connives.", t)
        self.assertEqual(c["mana_cost"], "{1}{U}{B}{R}")
        self.assertIn("Villain", c["type_line"])
        self.assertEqual(c["commander_legality"], "legal")

    def test_add_oracle_anchors(self):
        o = self.o
        self.assertIn("As an additional cost to cast this spell, discard a card or pay {5}", o["Lightning Axe"]["oracle_text"])
        self.assertIn("Whenever you discard a card, this creature deals 1 damage to each opponent",
                      o["Glint-Horn Buccaneer"]["oracle_text"])
        self.assertIn("Activate only if this creature is attacking", o["Glint-Horn Buccaneer"]["oracle_text"])
        self.assertEqual(o["Glint-Horn Buccaneer"]["mana_cost"], "{1}{R}{R}")
        rg = o["Red Ghost, Intangible Genius"]
        self.assertIn("Whenever you draw your second card each turn, create a 3/3 red Ape Villain creature token with haste",
                      rg["oracle_text"])
        self.assertIn("Villain", rg["type_line"])
        self.assertIn("Cycling {2}", o["Coastal Peak"]["oracle_text"])
        self.assertIn("Island Mountain", o["Coastal Peak"]["type_line"])
        self.assertIn("hexproof and haste", o["Swiftfoot Boots"]["oracle_text"])
        self.assertIn("shroud", o["Lightning Greaves"]["oracle_text"])  # why Boots, not Greaves (CR 702.18a)
        self.assertIn("you may discard a land card instead", o["Mox Diamond"]["oracle_text"])

    def test_loop_and_constraint_oracle_anchors(self):
        o = self.o
        self.assertIn("Each land card in your hand has cycling {R}", o["Tectonic Reformation"]["oracle_text"])
        self.assertIn("Dredge 2", o["Dakmor Salvage"]["oracle_text"])
        self.assertIn("Whenever you discard a land card, create a Treasure token", o["Surly Badgersaur"]["oracle_text"])
        self.assertIn("create a tapped Treasure token", o["Green Goblin, Nemesis"]["oracle_text"])
        self.assertIn("choose one that hasn't been chosen this turn", o["Monument to Endurance"]["oracle_text"])
        self.assertIn("Spend this mana only to cast a Villain spell or to activate an ability of a Villain source",
                      o["Villainous Hideout"]["oracle_text"])
        self.assertIn("{T}: Add {U}, {B}, or {R}.", o["Oscorp Industries"]["oracle_text"])
        self.assertEqual(o["Seismic Assault"]["mana_cost"], "{R}{R}{R}")
        self.assertIn("create a tapped and attacking token that's a copy", o["Loki, the Deceiver"]["oracle_text"])

    def test_swaps_identity_singleton_and_game_changers(self):
        added = sorted(set(self.cand) - set(self.base))
        cut = sorted(set(self.base) - set(self.cand))
        self.assertEqual(added, sorted(ADDS))
        self.assertEqual(cut, sorted(CUTS))
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
        self.assertEqual(gc(self.base), GAME_CHANGERS_BASE)
        self.assertEqual(gc(self.cand), GAME_CHANGERS_CAND)  # 7 Game Changers: Bracket 4 either way

    def test_owner_removed_class_not_readded(self):
        for n in OWNER_REMOVED_CLASS:
            self.assertNotIn(n, self.cand, n)

    def test_land_count_and_land_table_complete(self):
        lands = [n for n in self.cand if "Land" in self.o[n]["type_line"]]
        self.assertEqual(len(lands), 38)
        self.assertEqual(sorted(lands), sorted(n for n in self.cand if n in LAND_COLORS))
        self.assertEqual(len([n for n in self.base if n in LAND_COLORS]), 38)

    def test_spellbook_single_included_combo_is_the_finite_dakmor_loop(self):
        s = json.loads(SPELLBOOK.read_text())
        for k in ("baseline", "candidate"):
            inc = s[k]["included"]
            self.assertEqual(len(inc), 1)
            self.assertEqual(sorted(inc[0]["uses"]), ["Dakmor Salvage", "Surly Badgersaur", "Tectonic Reformation"])


class PassCBoundedMeasuredTests(unittest.TestCase):
    """Pass C #13 requested tests, run as bounded finite versions."""

    # (a) Dakmor loop
    def test_loop_is_library_bounded(self):
        r = dakmor_loop(40)
        self.assertEqual((r["iterations"], r["drain_each"], r["lethal"]), (20, 40, True))
        self.assertEqual(r["library_left"], 2)  # 19 dredges spent 38 cards
        self.assertEqual(dakmor_loop(38)["iterations"], 20)
        short = dakmor_loop(37)  # one card short: 18 dredges, the 19th draw is a normal draw
        self.assertEqual((short["iterations"], short["drain_each"], short["lethal"]), (19, 38, False))
        self.assertFalse(short["dakmor_in_hand"])

    def test_loop_with_damage_multipliers(self):
        r = dakmor_loop(40, buccaneer=True)
        self.assertEqual((r["iterations"], r["drain_each"], r["library_left"]), (14, 42, 14))
        self.assertTrue(dakmor_loop(26, buccaneer=True)["lethal"])
        self.assertFalse(dakmor_loop(25, buccaneer=True)["lethal"])
        r = dakmor_loop(40, buccaneer=True, cool_l2=True)
        self.assertEqual((r["iterations"], r["drain_each"]), (8, 40))

    def test_monument_adds_at_most_three_modes(self):
        r = dakmor_loop(40, monument=True)
        self.assertEqual(r["monument_modes"], 3)
        self.assertEqual((r["iterations"], r["drain_each"], r["lethal"]), (19, 41, True))

    def test_red_cost_and_treasure_constraints(self):
        self.assertEqual(dakmor_loop(40, red=0)["iterations"], 0)  # first {R} must be external
        n = dakmor_loop(40, maker="nemesis", red=3)  # Nemesis's Treasure enters tapped
        self.assertEqual((n["iterations"], n["drain_each"], n["lethal"]), (3, 6, False))
        g = land_groups(["Villainous Hideout"], villain_spell=False)
        self.assertEqual(dict(g), {"": 1})  # Hideout cannot pay the granted cycling {R}

    def test_interruptions_end_the_loop(self):
        h = dakmor_loop(40, hate_on=5)
        self.assertEqual((h["iterations"], h["drain_each"], h["lethal"]), (5, 10, False))
        x = dakmor_loop(40, exile_dakmor=True)  # taking the optional exile on Dakmor
        self.assertEqual((x["iterations"], x["drain_each"]), (1, 2))
        self.assertFalse(dakmor_loop(0)["dakmor_in_hand"])
        self.assertTrue(dakmor_loop(1, red=1)["drawn"] == 1)  # 1 card: dredge impossible, normal draw
        self.assertTrue(dakmor_loop(0, red=1)["drew_from_empty"])  # no replacement: an empty-library draw

    # (b) matched payoff grid
    def test_payoff_grid(self):
        gb, gr, ga = grid("buccaneer"), grid("revenant"), grid("artillerist")
        self.assertEqual(len(gb), 20)
        self.assertEqual((sum(v[0] for v in gb.values()), sum(v[1] for v in gb.values())), (79, 5))
        self.assertEqual((sum(v[0] for v in gr.values()), sum(v[1] for v in gr.values())), (8, 19))
        self.assertEqual((sum(v[0] for v in ga.values()), sum(v[1] for v in ga.values())), (64, 0))
        self.assertEqual(sum(gb[k][0] > gr[k][0] for k in gb), 20)
        self.assertEqual(sum(gr[k][1] > gb[k][1] for k in gb), 4)
        self.assertEqual(sum(gr[k] == (0, 0) for k in gr), 16)  # Revenant needs an attack, no haste
        self.assertTrue(all(gb[k][0] >= ga[k][0] and gb[k][1] >= ga[k][1] for k in gb))  # Buccaneer >= Artillerist
        self.assertEqual(gr[("wheel", True, False)], (2, 8))  # Revenant's ceiling: a refill

    # (c) exact colour access
    def test_colour_access_exact(self):
        b = [n for n in names(BASE) if n in LAND_COLORS]
        c = [n for n in names(CAND) if n in LAND_COLORS]
        doom = {"U": 1, "B": 1, "R": 1}
        r = lambda L, s, need, k, v: round(float(colour_access(L, s, need, k, v)), 4)
        self.assertEqual((r(b, 10, doom, 4, True), r(b, 11, doom, 4, True)), (0.555, 0.6477))
        self.assertEqual((r(c, 10, doom, 4, True), r(c, 11, doom, 4, True)), (0.557, 0.6498))
        rrr = {"R": 3}
        self.assertEqual((r(b, 11, rrr, 3, False), r(b, 12, rrr, 3, False)), (0.3895, 0.4529))
        self.assertEqual((r(c, 11, rrr, 3, False), r(c, 12, rrr, 3, False)), (0.4248, 0.4904))
        rr = {"R": 2}
        self.assertEqual((r(b, 9, rr, 3, False), r(c, 9, rr, 3, False)), (0.5318, 0.5573))

    def test_red_source_counts(self):
        red = lambda deck: sum(1 for n in deck if "R" in LAND_COLORS.get(n, "").rstrip("*")
                               and not LAND_COLORS[n].endswith("*"))
        self.assertEqual((red(names(BASE)), red(names(CAND))), (20, 21))  # Coastal Peak replaces UB Shipwreck Marsh

    # (d) graveyard dependence
    def test_graveyard_independent_outlets(self):
        cand = names(CAND)
        independent = ["Seismic Assault", "Tectonic Reformation", "Lightning Axe", "Mox Diamond", "Coastal Peak",
                       "Canyon Slough", "Fetid Pools", "Xander's Lounge", "Cool but Rude", "Glint-Horn Buccaneer"]
        dependent = ["Dakmor Salvage", "Crucible of Worlds", "Oscorp Industries"]
        for n in independent + dependent:
            self.assertIn(n, cand, n)
        self.assertGreater(len(independent), len(dependent))


if __name__ == "__main__":
    unittest.main()
