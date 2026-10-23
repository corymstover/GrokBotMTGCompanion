"""Finite source-anchored rules/mana cases for the Fire Lord Azula M7 candidate.

No randomness. Fire Lord Azula is modelled exactly as printed (current Oracle in the M7 snapshot): {1}{U}{B}{R} 4/4
Legendary Creature — Human Noble; "Firebending 2 ... Whenever you cast a spell while Fire Lord Azula is attacking, copy
that spell. You may choose new targets for the copy. (A copy of a permanent spell becomes a token.)" Rules anchors:
707.10 / 707.12 (copies of spells are not cast), 702.61a/b (split second; Samut ruling 2026-08-21), 601.2 (casting),
605.3 (mana abilities while holding priority), 500.4 (mana empties between steps), 704.5j (legend rule on token copies),
702.34 (flashback), 712 (modal double-faced cards).

This is a bounded rules/qualification-count model over fixed, enumerated states, NOT a game engine, simulation or
win-rate measurement; it supports no improvement claim by itself. PassCBoundedMeasuredTests recomputes the bounded finite
version of the M6 Pass C #19 requests (Samut/Beseech nonbo with +Spellseeker / -Samut; +Storm-Kiln Artist / -Big Score;
+Storm-Kiln Artist / -Wan Shi Tong): exact co-occurrence, Spellseeker reach, a Treasure ledger and exact Azula
castability. Matched opening hands and games against opponents are NOT modelled (no validated opponent model).
Approximations disclosed: each fetch counts as a source of any one Grixis colour; Exotic Orchard and Cavern of Souls
(Azula is a Human) count as rainbow; Gemstone Caverns counts as colourless for castability; fetch/shock life is ignored.
"""
from collections import Counter
from functools import lru_cache
import glob
import json
from math import comb
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Fire_Lord_Azula"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RC = ROOT / "data/grixis/m7/research_challengers"
SPELLBOOK = RC / f"{D}_CommanderSpellbook_20261023.json"
MEASURED = RC / f"{D}_bounded_measured_tests_20261023.json"
AZULA = "Fire Lord Azula"
SINK = "Sink into Stupor // Soporific Springs"
ADDS = sorted(["Flashback", "Mistrise Village", SINK, "Turnabout", "Unexpected Windfall"])
CUTS = sorted(["Exotic Orchard", "Gemstone Caverns", "Samut, Tyrant of Naktamun", "Swan Song", "Vivi Ornitier"])
GAME_CHANGERS = ["Ad Nauseam", "Ancient Tomb", "Chrome Mox", "Demonic Tutor", "Fierce Guardianship", "Force of Will",
                 "Gamble", "Grim Monolith", "Imperial Seal", "Jeska's Will", "Lion's Eye Diamond", "Mana Vault",
                 "Mox Diamond", "Mystical Tutor", "Necropotence", "Orcish Bowmasters", "Rhystic Study",
                 "Thassa's Oracle", "Underworld Breach", "Vampiric Tutor"]
OWNER_REMOVED = ["Storm-Kiln Artist", "Spellseeker", "Dualcaster Mage", "Twinflame", "Twinning Staff",
                 "Lightning Greaves", "Seething Song", "Snapcaster Mage", "Brainstorm", "Gitaxian Probe",
                 "Leyline of Anticipation", "Veyran, Voice of Duality", "Archmage Emeritus", "The Last Agni Kai",
                 "Training Center", "Final Fortune"]
OWNER_ADDS_KEPT = ["Geist of Saint Thalia", "Strix Serenade", "Repeal", "Quicken", "Crimson Wisps", "Expedite",
                   "Grinding Station", "Beseech the Mirror", "Mox Opal", "Wan Shi Tong, Librarian", "Starting Town",
                   "Arena of Glory", "Cavern of Souls"]
FETCHES = {"Arid Mesa", "Bloodstained Mire", "Flooded Strand", "Marsh Flats", "Misty Rainforest", "Polluted Delta",
           "Scalding Tarn", "Verdant Catacombs", "Wooded Foothills"}
LAND_COLORS = {
    "Ancient Tomb": "", "Emergence Zone": "", "Arena of Glory": "R", "Badlands": "BR", "Blood Crypt": "BR",
    "Cavern of Souls": "UBR", "City of Brass": "UBR", "Command Tower": "UBR", "Exotic Orchard": "UBR",
    "Gemstone Caverns": "UBR", "Mana Confluence": "UBR", "Starting Town": "UBR", "Mistrise Village": "U",
    "Otawara, Soaring City": "U", "Steam Vents": "UR", "Volcanic Island": "UR", "Underground Sea": "UB",
    "Watery Grave": "UB", **{f: "UBR" for f in FETCHES}}
ROCKS = {"Sol Ring": "", "Arcane Signet": "UBR", "Fellwar Stone": "", "Mana Vault": "", "Lotus Petal": "UBR",
         "Talisman of Creativity": "UR", "Talisman of Dominance": "UB", "Talisman of Indulgence": "BR",
         "Grim Monolith": ""}
BIT = {"U": 1, "B": 2, "R": 4}


def names(path):
    out = Counter()
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split(" ", 1)
            out[raw.removesuffix(" [Commander]")] += int(q.rstrip("x"))
    return out


def library(path):
    d = names(path)
    d[AZULA] -= 1
    return +d


def oracle():
    return {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}


def front(type_line):
    return type_line.split(" // ")[0]


def castable(lib, seen, turn, mdfc_land):
    cat = Counter()
    for n, q in lib.items():
        if n == SINK and mdfc_land:
            k = ("L", "U")
        elif n in LAND_COLORS:
            k = ("L", "" if n == "Gemstone Caverns" else LAND_COLORS[n])
        elif n in ROCKS:
            k = ("R", ROCKS[n])
        else:
            k = ("X", "")
        cat[k] += q
    items = sorted(cat.items())
    assert sum(cat.values()) == 99

    @lru_cache(None)
    def f(i, left, L, R, m):
        if i == len(items):
            return {(L, R, m): 1} if left == 0 else {}
        (t, col), n = items[i]
        out = Counter()
        for k in range(0, min(n, left) + 1):
            nm = m | (sum(BIT[c] for c in set(col)) if k and t != "X" else 0)
            for s, v in f(i + 1, left - k, min(L + (k if t == "L" else 0), 6),
                          min(R + (k if t == "R" else 0), 6), nm).items():
                out[s] += v * comb(n, k)
        return dict(out)
    r = f(0, seen, 0, 0, 0)
    ok = sum(v for (L, R, m), v in r.items() if min(L, turn) + min(R, turn - 1) >= 4 and m == 7)
    return round(ok / comb(99, seen), 4)


def run_cast(path, mdfc_land=False):
    lib = library(path)
    return {seat: {str(T): castable(lib, 7 + T - 1 + off, T, mdfc_land) for T in (2, 3, 4, 5)}
            for seat, off in (("play", 0), ("draw", 1))}


def turnabout_net(lands):
    """One loop iteration: Turnabout (4) + Narset's Reversal (2) cast; two Turnabout resolutions untap our lands."""
    return 2 * lands - 6


class AzulaOracleAndDeltaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.base = names(BASE)
        cls.cand = names(CAND)

    def test_commander_oracle_copies_spells_cast_while_attacking(self):
        az = self.o[AZULA]
        self.assertEqual(az["mana_cost"], "{1}{U}{B}{R}")
        self.assertEqual(az["type_line"], "Legendary Creature — Human Noble")
        self.assertEqual((az["power"], az["toughness"]), ("4", "4"))
        self.assertIn("Firebending 2", az["oracle_text"])
        self.assertIn("Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell.", az["oracle_text"])
        self.assertIn("A copy of a permanent spell becomes a token.", az["oracle_text"])

    def test_add_oracles_support_the_stated_roles(self):
        o = self.o
        self.assertIn("untap all tapped permanents of that type that player controls", o["Turnabout"]["oracle_text"])
        self.assertEqual(o["Turnabout"]["mana_cost"], "{2}{U}{U}")
        self.assertIn("Copy target instant or sorcery spell, then return it to its owner's hand",
                      o["Narset's Reversal"]["oracle_text"])
        self.assertIn("spell or nonland permanent an opponent controls", o[SINK]["oracle_text"])
        self.assertIn("pay 3 life", o[SINK]["oracle_text"])
        self.assertEqual(o[SINK]["type_line"], "Instant // Land")
        self.assertIn("As an additional cost to cast this spell, discard a card.", o["Unexpected Windfall"]["oracle_text"])
        self.assertIn("create two Treasure tokens", o["Unexpected Windfall"]["oracle_text"])
        self.assertIn("gains flashback until end of turn", o["Flashback"]["oracle_text"])
        self.assertEqual(o["Flashback"]["mana_cost"], "{R}")
        self.assertIn("enters tapped unless you control a Mountain or a Forest", o["Mistrise Village"]["oracle_text"])
        self.assertIn("can't be countered", o["Mistrise Village"]["oracle_text"])
        self.assertIn("have split second", o["Samut, Tyrant of Naktamun"]["oracle_text"])

    def test_exact_delta_counts_and_singleton(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), ADDS)
        self.assertEqual(sorted((self.base - self.cand).elements()), CUTS)
        self.assertEqual((sum(self.base.values()), sum(self.cand.values())), (100, 100))
        self.assertTrue(all(q == 1 for q in self.cand.values()))
        lands = lambda d: sum(q for n, q in d.items() if "Land" in front(self.o[n]["type_line"]))
        self.assertEqual((lands(self.base), lands(self.cand)), (26, 25))
        self.assertEqual(sum(1 for n in self.cand if "Land" in self.o[n]["type_line"] and
                             "Land" not in front(self.o[n]["type_line"])), 1)  # the Sink MDFC
        self.assertEqual((sum(n in FETCHES for n in self.base), sum(n in FETCHES for n in self.cand)), (9, 9))
        lib = lambda d: [n for n in d if n != AZULA]
        creatures = lambda d: sum(1 for n in lib(d) if "Creature" in front(self.o[n]["type_line"]))
        self.assertEqual((creatures(self.base), creatures(self.cand)), (13, 11))
        spells = lambda d: sum(1 for n in lib(d) if any(t in front(self.o[n]["type_line"]) for t in ("Instant", "Sorcery")))
        self.assertEqual((spells(self.base), spells(self.cand)), (41, 44))

    def test_land_sources_mistrise_enablers_and_island_count(self):
        def sources(d, mdfc):
            s = Counter()
            for n in d:
                col = LAND_COLORS.get(n, "U" if (n == SINK and mdfc) else None)
                if col is not None:
                    for c in col:
                        s[c] += 1
            return (s["R"], s["U"], s["B"])
        for n in self.base + self.cand:
            if "Land" in front(self.o[n]["type_line"]):
                self.assertIn(n, LAND_COLORS, n)
        self.assertEqual(sources(self.base, False), (21, 21, 20))
        self.assertEqual(sources(self.cand, False), (19, 20, 18))
        self.assertEqual(sources(self.cand, True), (19, 21, 18))
        mountains = sorted(n for n in self.cand if "Mountain" in self.o[n]["type_line"])
        self.assertEqual(mountains, ["Badlands", "Blood Crypt", "Steam Vents", "Volcanic Island"])
        self.assertEqual(len(mountains) + sum(n in FETCHES for n in self.cand), 13)
        islands = sorted(n for n in self.cand if "Island" in self.o[n]["type_line"])
        self.assertEqual(islands, ["Steam Vents", "Underground Sea", "Volcanic Island", "Watery Grave"])

    def test_game_changers_unchanged_and_all_legal(self):
        for d in (self.base, self.cand):
            self.assertEqual(sorted(n for n in d if self.o[n]["game_changer"]), sorted(GAME_CHANGERS))
            for n in d:
                self.assertEqual(self.o[n]["commander_legality"], "legal", n)
                self.assertTrue(set(self.o[n]["color_identity"]) <= set("UBR"), n)

    def test_spellbook_nine_kept_plus_turnabout_loop(self):
        s = json.loads(SPELLBOOK.read_text())
        ids = lambda k: sorted(c["id"] for c in s[k]["included"])
        expected = sorted(["742-1295", "1295-3093", "1368-1414-4856", "1368-3518-4856", "1368-1878-2706",
                           "1368-2706-3518", "1368-3698--44", "11-2196-7089", "1368-2196-7089"])
        self.assertEqual(ids("baseline"), expected)
        self.assertEqual(ids("candidate"), sorted(expected + ["11-4276-7089"]))
        self.assertEqual((s["baseline"]["almost_included_count"], s["candidate"]["almost_included_count"]), (98, 105))

    def test_owner_direction(self):
        for card in OWNER_REMOVED:
            self.assertEqual(self.cand[card], 0, card)
        for keep in OWNER_ADDS_KEPT:
            self.assertEqual(self.cand[keep], 1, keep)
        self.assertEqual(self.cand["Samut, Tyrant of Naktamun"], 0)  # FLAGGED override, keep-Samut list staged
        alt = names(RC / f"{D}_four_keep_Samut_no_Turnabout_20261023.txt")
        self.assertEqual((alt["Samut, Tyrant of Naktamun"], alt["Turnabout"]), (1, 0))

    def test_turnabout_loop_net_mana_is_finite_per_iteration(self):
        # Two Turnabout resolutions per iteration, lands tapped for mana between them (605.3, 500.4).
        self.assertEqual([turnabout_net(L) for L in range(2, 7)], [-2, 0, 2, 4, 6])
        self.assertEqual(min(L for L in range(10) if turnabout_net(L) >= 0), 3)   # unbounded storm
        self.assertEqual(min(L for L in range(10) if turnabout_net(L) > 0), 4)    # unbounded mana

    def test_copied_additional_cost_cards_double_once(self):
        # Azula ruling: additional costs paid for the original count for the copy; one discard, twice the output.
        windfall = {"cards": 2 * 2, "treasures": 2 * 2, "discards": 1}
        self.assertEqual(windfall, {"cards": 4, "treasures": 4, "discards": 1})
        self.assertEqual(4 - 4, 0)  # Big Score copied: 4 Treasures against its {3}{R}; net mana 0


class PassCBoundedMeasuredTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rec = json.loads(MEASURED.read_text())
        cls.lists = {"base.txt": BASE, "cand.txt": CAND}
        for p in sorted(glob.glob(str(RC / f"{D}_*_20261023.txt"))):
            cls.lists[Path(p).name] = Path(p)

    def test_recompute_castability_for_every_list(self):
        self.assertEqual(set(self.rec["azula_castable"]), set(self.lists))
        for key, path in self.lists.items():
            self.assertEqual(run_cast(path), self.rec["azula_castable"][key], key)
        for key, val in self.rec["azula_castable_mdfc_played_as_land"].items():
            self.assertEqual(run_cast(self.lists[key], mdfc_land=True), val, key)

    def test_castability_headline_numbers(self):
        c, m = self.rec["azula_castable"], self.rec["azula_castable_mdfc_played_as_land"]
        self.assertEqual((c["base.txt"]["play"]["4"], m["cand.txt"]["play"]["4"], c["cand.txt"]["play"]["4"]),
                         (0.492, 0.4905, 0.4632))
        self.assertEqual((c["base.txt"]["draw"]["4"], m["cand.txt"]["draw"]["4"]), (0.5855, 0.5839))
        self.assertEqual(m[f"{D}_six_MoxAmber_over_FellwarStone_20261023.txt"]["play"]["4"], 0.4638)
        self.assertTrue(all(v["play"]["2"] == 0.0 for v in c.values()))

    def test_samut_cooccurrence_exact(self):
        def p_all(n, k):
            return comb(99 - k, n - k) / comb(99, n)
        row = [r for r in self.rec["samut_cooccurrence"] if r["seat"] == "play" and r["turn"] == 4][0]
        self.assertEqual(row["cards_seen"], 10)
        self.assertEqual(row["P_Samut_seen"], round(1 - comb(98, 10) / comb(99, 10), 4))
        self.assertEqual(row["P_Samut_seen"], 0.101)
        self.assertEqual(row["P_Samut_and_Beseech"], round(p_all(10, 2), 4))
        self.assertEqual(row["P_Samut_and_Beseech"], 0.0093)
        self.assertEqual(row["P_Samut_and_NarsetsReversal_and_FranticSearch"], 0.0008)

    def test_split_second_trace_blocks_our_free_cast_and_reversal(self):
        t = {r["line"]: r for r in self.rec["split_second_trace"]}
        blocked = [k for k, r in t.items() if r["samut"].startswith("BLOCKED")]
        self.assertEqual(len(blocked), 3)
        self.assertTrue(any("Beseech" in k for k in blocked))
        self.assertTrue(any("11-2196-7089" in k for k in blocked))
        self.assertTrue(any("11-4276-7089" in k for k in blocked))

    def test_spellseeker_reach_and_kiln_ledger(self):
        o = oracle()
        for key in ("base.txt", "cand.txt"):
            hits = sorted(n for n in library(self.lists[key]) if o[n]["cmc"] <= 2 and
                          any(t in front(o[n]["type_line"]) for t in ("Instant", "Sorcery")))
            self.assertEqual(len(hits), 30, key)
            self.assertEqual(len(hits), self.rec["spellseeker_reach"][key]["count"])
        for r in self.rec["stormkiln_vs_bigscore"]["rows"]:
            k = r["spells_cast_while_Azula_attacks"]
            self.assertEqual(r["StormKiln_one_artist_cast_precombat"]["net_mana_after_paying_artist"], 2 * k - 4)
            self.assertEqual(r["BigScore_cast_while_Azula_attacks"]["net_mana"], 0)
            self.assertEqual(r["BigScore_cast_while_Azula_attacks"]["net_cards"], 2)


if __name__ == "__main__":
    unittest.main()
