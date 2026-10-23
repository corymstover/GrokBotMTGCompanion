"""Deck 26 Kess, Dissident Mage M7: finite Oracle-anchored checks and bounded Pass C tests.

Recomputes, from the frozen Oracle snapshot and the vendored baseline, the exact hypergeometric numbers recorded in the
bounded measured-tests receipt (blue Force-pitch availability for +Jeska's Will -Ledger Shredder, the Jeska's Will
hand-size table, colour sources), checks that the seeded Monte Carlo rows (Kess colours by turn, Frantic Search three-land
access, Demonic Counsel delirium proxy) are internally consistent, and pins the rules facts the one-swap research
conclusion depends on. These are not win rates; nothing here is approval.
"""
import json
import re
import unittest
from collections import Counter
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = "Kess__Dissident_Mage"
K = "Kess, Dissident Mage"
RC = ROOT / "data/grixis/m7/research_challengers"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
WILL = RC / f"{D}_PassC_plus_JeskasWill_minus_LedgerShredder_20261023.txt"
MEAS = RC / f"{D}_bounded_measured_tests_20261023.json"
CSB = RC / f"{D}_CommanderSpellbook_20261023.json"
RULES = ROOT / f"data/grixis/m6/rules_snapshots/{D}_M7_20261023.md"
TURNS = [(t, 6 + t) for t in range(1, 7)]


def library(path):
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"(\d+)x (.+?)( \[Commander\])?$", line.strip())
        if m and not m.group(3):
            out += [m.group(2)] * int(m.group(1))
    return out


def p_ge(k, n, N):
    return 1 - comb(N - k, n) / comb(N, n)


class KessMechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.m = json.loads(MEAS.read_text())
        cls.base, cls.cand, cls.will = library(BASE), library(CAND), library(WILL)

    def text(self, n):
        return self.o[n]["oracle_text"]

    def ftype(self, n):
        return self.o[n]["type_line"].split(" // ")[0]

    def test_commander_oracle_graveyard_permission(self):
        t = self.text(K)
        self.assertIn("Once during each of your turns, you may cast an instant or sorcery spell from your graveyard. "
                      "If a spell cast this way would be put into your graveyard, exile it instead.", t)
        self.assertIn("Flying", t)
        self.assertEqual(self.o[K]["mana_cost"], "{1}{U}{B}{R}")
        self.assertIn("Legendary Creature", self.o[K]["type_line"])
        self.assertEqual(self.o[K]["commander_legality"], "legal")
        self.assertIs(self.o[K]["game_changer"], False)
        self.assertIn("exile up to one target nonland permanent you control, then return that card",
                      self.text("Displacer Kitten"))

    def test_libraries_99_singleton_27_lands_and_exactly_one_swap(self):
        for lib in (self.base, self.cand):
            self.assertEqual(len(lib), 99)
            self.assertEqual(len(set(lib)), 99)
            self.assertEqual(sum(1 for n in lib if "Land" in self.ftype(n)), 27)
            self.assertFalse(any(n in lib for n in ("Island", "Swamp", "Mountain")))
        self.assertEqual(sorted((Counter(self.cand) - Counter(self.base)).elements()), ["Mana Drain"])
        self.assertEqual(sorted((Counter(self.base) - Counter(self.cand)).elements()), ["Personal Tutor"])
        self.assertEqual(sum(1 for n in self.cand if "Instant" in self.ftype(n)), 30)
        self.assertEqual(sum(1 for n in self.cand if "Sorcery" in self.ftype(n)), 13)
        self.assertEqual(sum(1 for n in self.cand if "Creature" in self.ftype(n)), 10)

    def test_mana_drain_and_personal_tutor_oracle(self):
        self.assertIn("Counter target spell. At the beginning of your next main phase, add an amount of {C} equal to "
                      "that spell's mana value.", self.text("Mana Drain"))
        self.assertEqual(self.o["Mana Drain"]["mana_cost"], "{U}{U}")
        self.assertIn("Instant", self.o["Mana Drain"]["type_line"])
        self.assertIn("Search your library for a sorcery card, reveal it, then shuffle and put that card on top.",
                      self.text("Personal Tutor"))
        self.assertIn("Sorcery", self.o["Personal Tutor"]["type_line"])
        for n in ("Demonic Consultation", "Tainted Pact", "Brain Freeze"):
            self.assertIn("Instant", self.ftype(n), n)
        for n in ("Mana Drain", "Personal Tutor"):
            self.assertIs(self.o[n]["game_changer"], False, n)

    def test_blue_pitch_cards_exact_hypergeometric(self):
        def blue(lib):
            return [n for n in lib if "{U}" in (self.o[n]["mana_cost"] or "") and "Land" not in self.ftype(n)]
        rec = self.m["passC_jeskas_will_vs_ledger_shredder"]
        counts = rec["blue_cards_in_99"]
        self.assertEqual((len(blue(self.base)), len(blue(self.will)), len(blue(self.cand))), (26, 25, 26))
        self.assertEqual((counts["baseline"], counts["plus_Jeskas_Will_minus_Ledger_Shredder"],
                          counts["candidate_plus_Mana_Drain_minus_Personal_Tutor"]), (26, 25, 26))
        tab = rec["P_other_blue_card_available_to_pitch_given_Force_in_hand"]
        for key, lib in (("baseline", self.base), ("plus_Will_minus_Shredder", self.will), ("candidate", self.cand)):
            k = len(blue(lib)) - 1
            for t, n in TURNS:
                self.assertEqual(tab[key][f"turn {t} (n={n})"], round(p_ge(k, n - 1, 98), 4), (key, t))
        self.assertEqual(tab["baseline"]["turn 1 (n=7)"], 0.8383)
        self.assertEqual(tab["plus_Will_minus_Shredder"]["turn 1 (n=7)"], 0.824)

    def test_jeskas_will_hand_size_table_exact(self):
        t = self.text("Jeska's Will")
        self.assertIn("If you control a commander as you cast this spell, you may choose both instead.", t)
        self.assertIn("Add {R} for each card in target opponent's hand.", t)
        self.assertEqual(self.o["Jeska's Will"]["mana_cost"], "{2}{R}")
        tab = self.m["passC_jeskas_will_vs_ledger_shredder"]["will_mana_by_opponent_hand_size"]
        self.assertEqual(sorted(tab, key=int), [str(h) for h in range(8)])
        for h, row in tab.items():
            self.assertEqual(row["red_mana_added"], int(h))
            self.assertEqual(row["net_after_paying_{2}{R}"], int(h) - 3)
        self.assertNotIn("Jeska's Will", self.cand)
        self.assertIn("Whenever a player casts their second spell each turn, this creature connives.",
                      self.text("Ledger Shredder"))

    def test_frantic_search_three_land_rows_consistent(self):
        self.assertIn("Untap up to three lands.", self.text("Frantic Search"))
        rows = self.m["passC_frantic_search_vs_personal_tutor"]["lands_in_play_by_turn"]
        prev = -1
        for t, n in TURNS:
            r = rows[f"turn {t} (n={n})"]
            self.assertGreaterEqual(r["P_three_lands_in_play"], prev)
            prev = r["P_three_lands_in_play"]
            self.assertLessEqual(r["mean_lands_in_play"], t)
            # Monte Carlo row must not exceed the exact P(at least three lands seen)
            self.assertLessEqual(r["P_three_lands_in_play"], round(p_three(n), 4) + 0.005)
        self.assertEqual(rows["turn 1 (n=7)"]["P_three_lands_in_play"], 0.0)
        self.assertEqual(rows["turn 2 (n=8)"]["P_three_lands_in_play"], 0.0)
        self.assertEqual(rows["turn 6 (n=12)"]["P_three_lands_in_play"], 0.6912)
        self.assertNotIn("Frantic Search", self.cand)

    def test_demonic_counsel_no_demon_and_delirium_proxy_bounded(self):
        self.assertEqual([n for n in self.base if "Demon" in self.o[n]["type_line"]], [])
        self.assertIn("Delirium", self.text("Demonic Counsel"))
        self.assertIn("Search your library for a Demon card", self.text("Demonic Counsel"))
        rec = self.m["demonic_counsel_delirium_proxy"]
        for key in ("baseline", "candidate", "plus_Frantic_minus_Personal"):
            prev = (0, 0)
            for t in range(2, 7):
                r = rec[key][f"turn {t} (n={6 + t})"]
                lo, hi = r["lower_no_discard"], r["upper_one_typed_discard_if_outlet_seen"]
                self.assertLessEqual(lo, hi)
                self.assertGreaterEqual((lo, hi), prev)
                prev = (lo, hi)
        b6, c6 = rec["baseline"]["turn 6 (n=12)"], rec["candidate"]["turn 6 (n=12)"]
        self.assertEqual((b6["upper_one_typed_discard_if_outlet_seen"], c6["upper_one_typed_discard_if_outlet_seen"]),
                         (0.401, 0.3858))
        self.assertLessEqual(b6["upper_one_typed_discard_if_outlet_seen"] - c6["upper_one_typed_discard_if_outlet_seen"], 0.016)
        self.assertIn("seeded finite Monte Carlo (seed 26, N=200000)", self.m["method"])

    def test_kess_colour_rows_consistent_and_conservative(self):
        rows = self.m["kess_colored_mana_by_turn"]["baseline_and_candidate_identical_mana"]
        prev = {"UU": 0, "UBR": 0, "Kess_4_with_UBR": 0}
        for t, n in TURNS:
            r = rows[f"turn {t} (n={n})"]
            self.assertLessEqual(r["Kess_4_with_UBR"], r["UBR"])
            for k in prev:
                self.assertGreaterEqual(r[k], prev[k])
            prev = r
        self.assertEqual(rows["turn 1 (n=7)"], {"UU": 0.0, "UBR": 0.0, "Kess_4_with_UBR": 0.0})
        self.assertEqual(rows["turn 6 (n=12)"]["Kess_4_with_UBR"], 0.5328)
        self.assertIn("conservative lower bounds", self.m["kess_colored_mana_by_turn"]["assumptions"])

    def colours(self, n, deck):
        t = self.text(n)
        tl = self.ftype(n)
        out = {c for sub, c in (("Island", "U"), ("Swamp", "B"), ("Mountain", "R")) if sub in tl}
        for cl in re.findall(r"Add ([^.]*)\.", t):
            if "any color" in cl or "one mana of any" in cl:
                out |= set("UBR")
            out |= {c for c in "UBR" if "{" + c + "}" in cl}
        m = re.search(r"Search your library for an? (.+?) card", t)
        if m and "Land" in tl and "Sacrifice" in t:
            subs = [x for x in ("Island", "Swamp", "Mountain", "Plains", "Forest") if x in m.group(1)]
            for d in deck:
                if any(x in self.ftype(d) for x in subs):
                    out |= self.colours(d, [])
        return out

    def test_land_colour_sources_unchanged_21_18_19(self):
        for lib in (self.base, self.cand):
            lands = [n for n in lib if "Land" in self.ftype(n)]
            src = Counter(c for n in lands for c in self.colours(n, lib))
            self.assertEqual((src["U"], src["B"], src["R"]), (21, 18, 19))
            self.assertEqual(sorted(n for n in lands if not self.colours(n, lib)),
                             ["Ancient Tomb", "City of Traitors", "Gemstone Caverns"])
        c = self.m["colored_land_sources"]
        self.assertEqual((c["blue"], c["black"], c["red"]), (21, 18, 19))
        self.assertEqual(self.m["lands_in_99"], 27)

    def test_commander_spellbook_deltas(self):
        c = json.loads(CSB.read_text())
        base = {x["id"] for x in c["baseline"]["included"]}
        self.assertEqual(len(base), 6)
        self.assertEqual({x["id"] for x in c["candidate"]["included"]}, base)
        for k, v in c["alternatives"].items():
            extra = {x["id"] for x in v["included"]} - base
            if "JeskasWill" in k:
                self.assertEqual(extra, {"1368-1878-2706"}, k)
            elif "FranticSearch" in k:
                self.assertEqual(extra, {"1368-2196-3766"}, k)
            else:
                self.assertEqual(extra, set(), k)
        self.assertIn("742-1295", base)
        self.assertIn("1295-3093", base)

    def test_rules_snapshot_anchors(self):
        r = RULES.read_text()
        for s in ("117.1a", "118.9", "400.7", "505.1", "106.4", "608.2n", "903.8",
                  "postcombat main phase", "**no** permission on opponents' turns", "commander: legal"):
            self.assertIn(s, r)
        self.assertIn("If it's not your turn", self.text("Force of Negation"))
        self.assertIn("If you control a commander, you may cast this spell without paying its mana cost.",
                      self.text("Deadly Rollick"))

    def test_off_identity_excluded(self):
        live = {c["name"]: c for c in json.loads((RC / f"{D}_Scryfall_live_20261023.json").read_text())["cards"]}
        self.assertIn("G", live["Manamorphose"]["color_identity"])
        self.assertIn("W", live["Silence"]["color_identity"])
        for n in ("Manamorphose", "Silence", "Orim's Chant", "Sea of Clouds", "Personal Tutor"):
            self.assertNotIn(n, self.cand)

    def test_receipt_is_bounded_not_win_rate(self):
        self.assertIn("exact hypergeometric", self.m["method"])
        self.assertIn("no effect-aware game simulation", self.m["method"])
        self.assertIn("No hand-size logs exist in the repo",
                      self.m["passC_jeskas_will_vs_ledger_shredder"]["opponent_hand_size_note"])


def p_three(n, lands=27, N=99):
    return sum(comb(lands, i) * comb(N - lands, n - i) for i in range(3, min(lands, n) + 1)) / comb(N, n)


if __name__ == "__main__":
    unittest.main()
