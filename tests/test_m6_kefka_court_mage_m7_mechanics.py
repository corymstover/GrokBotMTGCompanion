"""Deck 25 Kefka, Court Mage M7: finite Oracle-anchored checks and bounded Pass C tests.

Recomputes, from the frozen Oracle snapshot and the vendored baseline, the exact hypergeometric numbers recorded in the
bounded measured-tests receipt (Mountain-subtype sources, Anger haste window with and without Entomb, Dualcaster Mage
partner access, early creatures for Culling the Weak), checks the seeded delirium proxy is internally consistent, and
pins the rules facts the one-swap research conclusion depends on. These are not win rates; nothing here is approval.
"""
import json
import re
import unittest
from collections import Counter
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = "Kefka__Court_Mage"
K = "Kefka, Court Mage // Kefka, Ruler of Ruin"
RC = ROOT / "data/grixis/m7/research_challengers"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
MEAS = RC / f"{D}_bounded_measured_tests_20261023.json"
CSB = RC / f"{D}_CommanderSpellbook_20261023.json"
RULES = ROOT / f"data/grixis/m6/rules_snapshots/{D}_M7_20261023.md"
TURNS = [(t, 6 + t) for t in range(1, 7)]
FETCHES = {"Arid Mesa", "Bloodstained Mire", "Scalding Tarn", "Wooded Foothills", "Flooded Strand", "Misty Rainforest",
           "Polluted Delta", "Marsh Flats", "Verdant Catacombs"}
EARLY = {"Ragavan, Nimble Pilferer", "Harmonic Prodigy", "Hexing Squelcher", "Tinybones, Bauble Burglar",
         "Orcish Bowmasters", "Phantasmal Image", "Thassa's Oracle"}
PARTNERS = {"Molten Duplication", "Saw in Half", "Essence Flux"}


def library(path):
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"(\d+)x (.+?)( \[Commander\])?$", line.strip())
        if m and not m.group(3):
            out += [m.group(2)] * int(m.group(1))
    return out


def p_ge1(k, n, N=99):
    return 1 - comb(N - k, n) / comb(N, n)


def p_both(k1, k2, n, N=99):
    tot = 0
    for i in range(1, min(k1, n) + 1):
        for j in range(1, min(k2, n - i) + 1):
            tot += comb(k1, i) * comb(k2, j) * comb(N - k1 - k2, n - i - j)
    return tot / comb(N, n)


class KefkaMechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        snap = json.loads(SNAP.read_text())
        cls.o = {c["name"]: c for c in snap["cards"]}
        cls.m = json.loads(MEAS.read_text())
        cls.base = library(BASE)
        cls.cand = library(CAND)

    def text(self, n):
        return self.o[n]["oracle_text"]

    def front_type(self, n):
        return self.o[n]["type_line"].split(" // ")[0]

    def test_commander_oracle_discard_draw_and_transform(self):
        t = self.text(K)
        self.assertIn("Whenever Kefka enters or attacks, each player discards a card. Then you draw a card for each "
                      "card type among cards discarded this way.", t)
        self.assertIn("{8}: Each opponent sacrifices a permanent of their choice. Transform Kefka. Activate only as a "
                      "sorcery.", t)
        self.assertIn("Whenever an opponent loses life during your turn", t)
        self.assertEqual(self.o[K]["mana_cost"].split(" // ")[0], "{2}{U}{B}{R}")
        self.assertIn("Wizard", self.o[K]["type_line"])
        self.assertIn("If a triggered ability of a Shaman or another Wizard you control triggers, that ability "
                      "triggers an additional time.", self.text("Harmonic Prodigy"))

    def test_libraries_are_99_singleton_28_lands_and_exactly_one_swap(self):
        for lib in (self.base, self.cand):
            self.assertEqual(len(lib), 99)
            self.assertEqual(len(set(lib)), 99)
            self.assertEqual(sum(1 for n in lib if "Land" in self.front_type(n)), 28)
        self.assertEqual(sorted((Counter(self.cand) - Counter(self.base)).elements()), ["Dualcaster Mage"])
        self.assertEqual(sorted((Counter(self.base) - Counter(self.cand)).elements()), ["Culling the Weak"])
        self.assertEqual(sum(1 for n in self.base if "Creature" in self.front_type(n)), 13)
        self.assertEqual(sum(1 for n in self.cand if "Creature" in self.front_type(n)), 14)

    def test_mountain_subtype_sources_recomputed(self):
        mtn = sorted(n for n in self.base if "Mountain" in self.front_type(n))
        self.assertEqual(mtn, ["Badlands", "Blood Crypt", "Steam Vents", "Volcanic Island"])
        self.assertEqual(mtn, self.m["mountain_subtype_lands_in_99"])
        self.assertEqual(set(self.m["fetchlands_that_find_one"]), FETCHES)
        self.assertTrue(FETCHES <= set(self.base))
        self.assertEqual(self.m["mountain_subtype_sources_total"], 13)
        for t, n in TURNS:
            self.assertEqual(self.m["mountain_source_by_turn"][f"turn {t} (n={n})"], round(p_ge1(13, n), 4))
        self.assertIn("you control a Mountain, creatures you control have haste", self.text("Anger"))

    def test_anger_haste_window_with_and_without_entomb_exact(self):
        rec = self.m["anger_haste_window"]["by_turn"]
        for t, n in TURNS:
            row = rec[f"turn {t} (n={n})"]
            self.assertEqual(row["baseline_Anger_seen_and_Mountain_source"], round(p_both(1, 13, n), 4))
            self.assertEqual(row["plusEntomb_Anger_or_Entomb_seen_and_Mountain_source"], round(p_both(2, 13, n), 4))
        self.assertEqual(rec["turn 1 (n=7)"]["baseline_Anger_seen_and_Mountain_source"], 0.0413)
        self.assertEqual(rec["turn 5 (n=11)"]["plusEntomb_Anger_or_Entomb_seen_and_Mountain_source"], 0.1642)
        self.assertIn("put that card into your graveyard", self.text("Entomb"))

    def test_demonic_counsel_has_no_demon_and_delirium_proxy_bounded(self):
        self.assertEqual([n for n in self.base if "Demon" in self.o[n]["type_line"]], [])
        self.assertEqual(self.m["demons_in_99"], [])
        self.assertIn("Delirium", self.text("Demonic Counsel"))
        self.assertIn("Search your library for a Demon card", self.text("Demonic Counsel"))
        rows = self.m["counsel_delirium_proxy"]["baseline"]
        prev = (0, 0)
        for t in range(2, 7):
            r = rows[f"turn {t} (n={6 + t})"]
            lo, hi = r["lower_no_extra_discard"], r["upper_with_one_free_typed_discard"]
            self.assertLessEqual(lo, hi)
            self.assertGreaterEqual((lo, hi), prev)
            prev = (lo, hi)
        self.assertEqual(rows["turn 4 (n=10)"], {"lower_no_extra_discard": 0.0659,
                                                  "upper_with_one_free_typed_discard": 0.4229})
        self.assertIn("seeded finite Monte Carlo (seed 25, N=200000)", self.m["method"])

    def test_dualcaster_rules_and_partner_access_exact(self):
        self.assertIn("Flash", self.text("Dualcaster Mage"))
        self.assertIn("copy target instant or sorcery spell", self.text("Dualcaster Mage"))
        self.assertIn("Wizard", self.o["Dualcaster Mage"]["type_line"])
        self.assertIn("It gains haste until end of turn", self.text("Molten Duplication"))
        self.assertIn("creates two tokens that are copies", self.text("Saw in Half"))
        self.assertIn("return that card to the battlefield", self.text("Essence Flux"))
        self.assertTrue(PARTNERS <= set(self.cand))
        d = self.m["dualcaster_mage_test"]
        self.assertIn("707.10", d["rules"])
        self.assertIn("147-5487", d["rules"])
        for t, n in TURNS:
            self.assertEqual(d["by_turn"][f"turn {t} (n={n})"]["P_Dualcaster_and_at_least_one_partner_seen"],
                             round(p_both(1, 3, n), 4))
        self.assertEqual(d["by_turn"]["turn 1 (n=7)"]["P_Dualcaster_and_at_least_one_partner_seen"], 0.0123)

    def test_culling_the_weak_needs_a_creature_exact(self):
        self.assertIn("As an additional cost to cast this spell, sacrifice a creature.", self.text("Culling the Weak"))
        self.assertTrue(EARLY <= set(self.base))
        for n in EARLY:
            self.assertIn("Creature", self.front_type(n))
            self.assertLessEqual(self.o[n]["cmc"], 2)
        rec = self.m["dualcaster_mage_test"]["early_creature_for_Culling"]
        for t, n in TURNS:
            self.assertEqual(rec[f"turn {t} (n={n})"], round(p_ge1(7, n), 4))
        self.assertEqual((rec["turn 1 (n=7)"], rec["turn 6 (n=12)"]), (0.4115, 0.6075))

    def test_commander_spellbook_deltas(self):
        c = json.loads(CSB.read_text())
        base = {x["id"] for x in c["baseline"]["included"]}
        self.assertEqual(len(base), 6)
        cand = {x["id"] for x in c["candidate"]["included"]}
        self.assertEqual(cand - base, {"147-5487", "147-500", "147-4598"})
        self.assertEqual(len(cand), 9)
        for k, v in c["alternatives"].items():
            extra = {x["id"] for x in v["included"]} - base
            if "DualcasterMage" in k:
                self.assertEqual(extra, {"147-5487", "147-500", "147-4598"}, k)
            else:
                self.assertEqual(extra, set(), k)
                self.assertEqual(len(v["included"]), 6, k)

    def test_rules_snapshot_anchors(self):
        r = RULES.read_text()
        for s in ("603.2d", "707.10", "707.10c", "903.8", "302.6", "702.10b", "205.2a", "712.8a"):
            self.assertIn(s, r)
        self.assertIn("If it's not your turn", self.text("Force of Negation"))

    def test_banned_and_off_identity_excluded(self):
        for n in ("Dockside Extortionist", "Jeweled Lotus", "Mana Crypt", "Manamorphose", "Culling the Weak"):
            self.assertNotIn(n, self.cand)
        live = {c["name"]: c for c in json.loads((RC / f"{D}_Scryfall_live_20261023.json").read_text())["cards"]}
        self.assertEqual(live["Dockside Extortionist"]["commander_legality"], "banned")
        self.assertIn("G", live["Manamorphose"]["color_identity"])
        self.assertEqual(self.o[K]["commander_legality"], "legal")
        self.assertIs(self.o[K]["game_changer"], False)
        self.assertIs(self.o["Dualcaster Mage"]["game_changer"], False)

    def colours(self, n, deck):
        t = self.text(n).split("\n//\n")[0]
        tl = self.front_type(n)
        out = {c for sub, c in (("Island", "U"), ("Swamp", "B"), ("Mountain", "R")) if sub in tl}
        for cl in re.findall(r"Add ([^.]*)\.", t):
            if "any color" in cl or "one mana of any" in cl:
                out |= set("UBR")
            out |= {c for c in "UBR" if "{" + c + "}" in cl}
        m = re.search(r"Search your library for an? (.+?) card", t)
        if m and "Land" in tl and "Sacrifice" in t:
            subs = [x for x in ("Island", "Swamp", "Mountain", "Plains", "Forest") if x in m.group(1)]
            for d in deck:
                if any(x in self.front_type(d) for x in subs):
                    out |= self.colours(d, [])
        return out

    def test_land_colour_sources_unchanged_21_20_20(self):
        for lib in (self.base, self.cand):
            lands = [n for n in lib if "Land" in self.front_type(n)]
            src = Counter(c for n in lands for c in self.colours(n, lib))
            self.assertEqual((src["U"], src["B"], src["R"]), (21, 20, 20))
        self.assertEqual(self.colours("Arena of Glory", self.base), {"R"})
        self.assertEqual(self.colours("Ancient Tomb", self.base), set())

    def test_receipt_is_bounded_not_win_rate(self):
        self.assertIn("exact hypergeometric", self.m["method"])
        self.assertIn("no claim of effect-aware game simulation", self.m["method"])
        self.assertIn("Not run as a separate measurement", self.m["DRC_vs_Tinybones"])


if __name__ == "__main__":
    unittest.main()
