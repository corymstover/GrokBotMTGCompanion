"""Deck 30 Lord_Xander__the_Collector (Lord Xander, the Collector) M7 research candidate: finite Oracle-anchored rules
checks and the bounded versions of the tests Pass C requested (+Necromancy -Persist versus two-mana nonlegendary Auton
recursion and the two-mana Goryo's Vengeance haste burst; Seize the Day). Recomputes the exhaustive rules grids from the
receipt's own embedded script and checks the seeded goldfish cells for internal consistency. Not a game simulation or
win rate; nothing here is owner approval."""
from __future__ import annotations
import collections
import itertools
import json
import math
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = "Lord_Xander__the_Collector"
XANDER = "Lord Xander, the Collector"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
RULES = ROOT / f"data/grixis/m6/rules_snapshots/{D}_M7_20261023.md"
RC = ROOT / "data/grixis/m7/research_challengers"
MEAS = RC / f"{D}_bounded_measured_tests_20261023.json"
CSB = RC / f"{D}_CommanderSpellbook_20261023.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
ADDS = sorted(["Necromancy", "Swiftfoot Boots", "Malakir Rebirth // Malakir Mire"])
CUTS = sorted(["Persist", "Lightning Greaves", "Bojuka Bog"])


def library(path):
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"(\d+)x (.+?)( \[Commander\])?$", line.strip())
        if m and not m.group(3):
            out += [m.group(2)] * int(m.group(1))
    return out


class LordXanderM7Mechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.base, cls.cand = library(BASE), library(CAND)
        cls.m = json.loads(MEAS.read_text())

    def text(self, n):
        return self.o[n]["oracle_text"]

    def front(self, n):
        return self.o[n]["type_line"].split(" // ")[0]

    def test_commander_oracle_legality_and_release(self):
        t = self.text(XANDER)
        self.assertIn("When Lord Xander enters, target opponent discards half the cards in their hand, rounded down.", t)
        self.assertIn("Whenever Lord Xander attacks, defending player mills half their library, rounded down.", t)
        self.assertIn("When Lord Xander dies, target opponent sacrifices half the nonland permanents they control of their "
                      "choice, rounded down.", t)
        c = self.o[XANDER]
        self.assertEqual(c["mana_cost"], "{4}{U}{B}{R}")
        self.assertTrue(c["type_line"].startswith("Legendary Creature"))
        self.assertEqual(c["commander_legality"], "legal")
        self.assertIs(c["game_changer"], False)
        self.assertEqual((c["set"], c["released_at"], c["oracle_id"]),
                         ("snc", "2022-04-29", "d17bfa94-5046-46ae-80af-be5d1d35af13"))

    def test_libraries_99_33_land_slots_exactly_three_swaps(self):
        for lib in (self.base, self.cand):
            self.assertEqual(len(lib), 99)
        self.assertEqual(sum(1 for n in self.base if "Land" in self.front(n)), 33)
        self.assertEqual(sum(1 for n in self.cand if "Land" in self.front(n)), 32)
        self.assertEqual(sum(1 for n in self.cand if "Land" in self.o[n]["type_line"]), 33)  # + Malakir MDFC
        self.assertEqual(sorted((Counter(self.cand) - Counter(self.base)).elements()), ADDS)
        self.assertEqual(sorted((Counter(self.base) - Counter(self.cand)).elements()), CUTS)
        for n in set(self.cand) | {XANDER}:
            self.assertEqual(self.o[n]["commander_legality"], "legal", n)
            self.assertTrue(set(self.o[n]["color_identity"]) <= {"U", "B", "R"}, n)
        gcs = [n for n in set(self.cand) if self.o[n]["game_changer"]]
        self.assertEqual(len(gcs), 20)
        self.assertEqual(sorted(gcs), sorted(n for n in set(self.base) if self.o[n]["game_changer"]))
        for n in ADDS:
            self.assertIs(self.o[n]["game_changer"], False, n)

    def test_swap_oracle(self):
        self.assertIn("Return target nonlegendary creature card from your graveyard", self.text("Persist"))
        n = self.text("Necromancy")
        self.assertIn("as though it had flash", n)
        self.assertIn("sacrifices it at the beginning of the next cleanup step", n)
        self.assertIn("Put target creature card from a graveyard onto the battlefield", n)
        self.assertIn("When this enchantment leaves the battlefield, that creature's controller sacrifices it.", n)
        self.assertIn("haste and shroud", self.text("Lightning Greaves"))
        self.assertIn("Equip {0}", self.text("Lightning Greaves"))
        self.assertIn("hexproof and haste", self.text("Swiftfoot Boots"))
        self.assertIn("Equip {1}", self.text("Swiftfoot Boots"))
        self.assertIn("exile target player's graveyard", self.text("Bojuka Bog"))
        m = self.text("Malakir Rebirth // Malakir Mire")
        self.assertIn("When this creature dies, return it to the battlefield tapped under its owner's control.", m)
        self.assertIn("This land enters tapped.", m)

    def test_pass_c_cards_oracle(self):
        g = self.text("Goryo's Vengeance")
        self.assertIn("Return target legendary creature card from your graveyard", g)
        self.assertIn("Exile it at the beginning of the next end step.", g)
        self.assertIn("there is an additional combat phase", self.text("Seize the Day"))
        self.assertIn("copy of target nonlegendary creature you control", self.text("Kiki-Jiki, Mirror Breaker"))

    def test_rules_grids_recomputed_from_receipt_script(self):
        src = self.m["scripts"]["meas"]
        part = src[src.index("# ---------------- Part B"):src.index('if __name__=="__main__":')]
        ns = {"itertools": itertools, "collections": collections}
        exec(part, ns)  # deterministic enumerated grids; no randomness, no I/O
        B = ns["gridB"]()
        self.assertEqual(B, self.m["results"]["B"])
        b1 = B["B1_recursion_Persist_vs_Necromancy_vs_Goryos"]
        self.assertEqual((b1["cells"], b1["Necromancy_returns"], b1["Persist_returns"], b1["Goryos_Vengeance_returns"],
                          b1["Necromancy_returns_Persist_does_not"], b1["Persist_returns_Necromancy_does_not"],
                          b1["Necromancy_extra_dies_trigger"], b1["Goryos_Vengeance_attack_trigger_this_turn"]),
                         (36, 12, 4, 8, 10, 2, 1, 2))
        for row in b1["rows"]:
            if row["target"] == "Lord_Xander_own_graveyard":
                self.assertFalse(row["Persist"]["returns"])  # Persist: nonlegendary only
        b2 = B["B2_haste_equipment_Greaves_vs_Boots"]
        self.assertEqual((b2["cells"], b2["Boots_action_ok"], b2["Greaves_action_ok"], b2["Boots_ok_Greaves_blocked"],
                          b2["Greaves_ok_Boots_blocked"], b2["Greaves_haste"], b2["Boots_haste"]),
                         (44, 44, 30, 14, 0, 44, 22))
        b3 = B["B3_land_slot_Bojuka_Bog_vs_Malakir_Rebirth"]
        self.assertEqual((b3["cells"], b3["Bog_answers"], b3["Malakir_answers"], b3["Malakir_only"], b3["Bog_only"]),
                         (16, 6, 6, 4, 4))

    def test_goldfish_cells_pinned_and_consistent(self):
        A = self.m["results"]["A"]
        self.assertEqual(len(A), 13)
        self.assertIn("seed 30", self.m["scripts"]["meas"])
        for cfg, rows in A.items():
            prev = {}
            for t in range(1, 8):
                c = rows[f"turn {t}"]
                self.assertLessEqual(c["P_Xander_attack_trigger_declared"], c["P_Xander_cast"] + 1e-9, (cfg, t))
                for k in ("P_Xander_cast", "P_Xander_attack_trigger_declared"):
                    self.assertGreaterEqual(c[k], prev.get(k, 0), (cfg, t, k))
                    prev[k] = c[k]

        def at(cfg, t, k="P_Xander_attack_trigger_declared"):
            return A[cfg][f"turn {t}"][k]
        self.assertEqual((at("baseline", 6), at("baseline", 7)), (0.1924, 0.2978))
        self.assertEqual((at("candidate", 6), at("candidate", 7)), (0.1857, 0.2897))
        self.assertEqual(at("candidate", 7), at("single_plus_Swiftfoot_Boots_minus_Lightning_Greaves", 7))
        for cfg in ("single_plus_Necromancy_minus_Persist", "single_plus_Malakir_Rebirth_minus_Bojuka_Bog",
                    "PassC_single_plus_Goryos_Vengeance_minus_Persist_on_baseline"):
            self.assertEqual(A[cfg], A["baseline"], cfg)
        for cfg in ("baseline", "candidate"):
            self.assertEqual(at(cfg, 7, "P_Xander_cast"), 0.3779)
        self.assertEqual(at("probe_on_candidate_plus_Chrome_Mox_minus_Talisman_of_Creativity", 7, "P_Xander_cast"), 0.3808)
        self.assertEqual(at("probe_on_candidate_plus_Command_Beacon_minus_Xanders_Lounge", 7, "P_Xander_cast"), 0.3786)
        self.assertEqual(at("probe_on_candidate_plus_Glasspool_Mimic_minus_Training_Center", 7, "P_Xander_cast"), 0.3749)

    def test_land_count_hypergeometric(self):
        p = sum(math.comb(33, k) * math.comb(66, 7 - k) for k in range(2, 5)) / math.comb(99, 7)
        self.assertEqual(round(p, 4), 0.7069)

    def test_commander_spellbook_counts(self):
        c = json.loads(CSB.read_text())
        self.assertEqual(len(c["baseline"]["included"]), 11)
        self.assertEqual(len(c["candidate"]["included"]), 11)
        self.assertEqual((c["baseline"]["almost_included_count"], c["candidate"]["almost_included_count"]), (132, 131))
        self.assertEqual(len(c["alternatives"]), 8)
        for k, v in c["alternatives"].items():
            self.assertEqual(len(v["included"]), 14 if "KikiJiki" in k else 11, k)

    def test_rules_snapshot_anchors(self):
        r = RULES.read_text()
        for s in ("CR 514.3a", "CR 700.4", "CR 702.11b", "CR 702.18a", "CR 702.6a", "commander: legal",
                  "not a Game Changer", "no project exception applies", "**no rulings**", "Sorin of House Markov"):
            self.assertIn(s, r)

    def test_receipt_is_bounded_not_win_rate(self):
        self.assertIn("Neither part is a win-rate simulation", self.m["scripts"]["meas"])
        self.assertIn("no opponent", self.m["scripts"]["meas"])


if __name__ == "__main__":
    unittest.main()
