"""Deck 28 Loki__the_Deceiver (Loki, the Deceiver) M7 research candidate: finite Oracle-anchored rules checks and the
bounded versions of the tests Pass C requested (+Strionic Resonator -Swiftfoot Boots; +Seize the Day -Black Market
Connections). Recomputes the exhaustive rules grid from the receipt's own embedded script and checks the seeded goldfish
cells for internal consistency. Not a game simulation or win rate; nothing here is owner approval."""
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
D = "Loki__the_Deceiver"
LOKI = "Loki, the Deceiver"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
RULES = ROOT / f"data/grixis/m6/rules_snapshots/{D}_M7_20261023.md"
RC = ROOT / "data/grixis/m7/research_challengers"
MEAS = RC / f"{D}_bounded_measured_tests_20261023.json"
CSB = RC / f"{D}_CommanderSpellbook_20261023.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
ADDS = ["Elektra, Daughter of the Hand", "Ultimo, Civilization's End"]
CUTS = ["Crimson Cowl, Master of Evil", "Killmonger, Ruthless Usurper"]
CONFIGS = ("baseline", "plus_Strionic_Resonator_minus_Swiftfoot_Boots", "plus_Seize_the_Day_minus_Black_Market_Connections",
           "plus_Ultimo_minus_Crimson_Cowl", "plus_Elektra_minus_Killmonger", "candidate_Ultimo_and_Elektra",
           "candidate_plus_Secluded_Courtyard_minus_Path_of_Ancestry",
           "candidate_plus_Strionic_Resonator_minus_Swiftfoot_Boots")


def library(path):
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"(\d+)x (.+?)( \[Commander\])?$", line.strip())
        if m and not m.group(3):
            out += [m.group(2)] * int(m.group(1))
    return out


def p_ge1(k, n, N):
    return 1 - math.comb(N - k, n) / math.comb(N, n)


class LokiM7Mechanics(unittest.TestCase):
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
        t = self.text(LOKI)
        self.assertIn("Whenever Loki attacks, create a tapped and attacking token that's a copy of another target Villain "
                      "you control, except it isn't legendary and it's an Illusion in addition to its other types.", t)
        self.assertIn("Sacrifice that token at the beginning of the next end step.", t)
        self.assertIn("Whenever one or more Villains you control deal combat damage to a player, draw a card.", t)
        c = self.o[LOKI]
        self.assertEqual(c["mana_cost"], "{1}{U}{B}{R}")
        self.assertIn("Villain", c["type_line"])
        self.assertEqual(c["commander_legality"], "legal")
        self.assertIs(c["game_changer"], False)
        self.assertEqual((c["set"], c["released_at"]), ("msc", "2026-06-26"))
        self.assertLessEqual(c["released_at"], "2026-10-23")

    def test_libraries_99_34_lands_exactly_two_swaps(self):
        for lib in (self.base, self.cand):
            self.assertEqual(len(lib), 99)
            self.assertEqual(sum(1 for n in lib if "Land" in self.front(n)), 34)
        self.assertEqual(sorted((Counter(self.cand) - Counter(self.base)).elements()), ADDS)
        self.assertEqual(sorted((Counter(self.base) - Counter(self.cand)).elements()), CUTS)
        for n in set(self.cand) | {LOKI}:
            self.assertEqual(self.o[n]["commander_legality"], "legal", n)
            self.assertTrue(set(self.o[n]["color_identity"]) <= {"U", "B", "R"}, n)
        gcs = sorted(n for n in set(self.cand) if self.o[n]["game_changer"])
        self.assertEqual(gcs, ["Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship", "Jeska's Will", "Rhystic Study"])

    def test_swap_oracle_enters_vs_attack_triggers(self):
        # Adds: enters triggers (work on a Loki token copy, CR 603.6a)
        self.assertIn("When Ultimo enters, each opponent sacrifices a creature of their choice.",
                      self.text("Ultimo, Civilization's End"))
        self.assertIn("When Elektra enters, destroy target creature an opponent controls with power 3 or less.",
                      self.text("Elektra, Daughter of the Hand"))
        self.assertIn("Sneak {1}{B}{B}", self.text("Elektra, Daughter of the Hand"))
        for n in ADDS:
            self.assertIn("Villain", self.o[n]["type_line"])
            self.assertIs(self.o[n]["game_changer"], False)
        # Cuts: attack / nontoken-attack triggers (do not fire on a token put onto the battlefield attacking, CR 508.4)
        self.assertIn("Whenever one or more nontoken Villains you control attack a player",
                      self.text("Crimson Cowl, Master of Evil"))
        k = self.text("Killmonger, Ruthless Usurper")
        self.assertIn("Whenever Killmonger attacks, he gets +1/+0", k)
        self.assertIn("Whenever Killmonger deals combat damage to a player, that player sacrifices an artifact", k)

    def test_pass_c_cards_oracle(self):
        self.assertIn("{2}, {T}: Copy target triggered ability you control.", self.text("Strionic Resonator"))
        self.assertIn("After this main phase, there is an additional combat phase", self.text("Seize the Day"))
        self.assertIn("hexproof and haste", self.text("Swiftfoot Boots"))
        self.assertIn("haste and shroud", self.text("Lightning Greaves"))
        self.assertIn("Triggered abilities you control can't cause you to sacrifice or exile creature tokens you control.",
                      self.text("The Master, Multiplied"))
        self.assertIn("it triggers an additional time", self.text("Roaming Throne"))

    def test_rules_grid_recomputed_from_receipt_script(self):
        src = self.m["scripts"]["meas"]
        part = src[src.index("# ---- Part B"):src.index("out={")]
        ns = {"itertools": itertools, "collections": collections}
        exec(part, ns)  # deterministic enumerated grid; no randomness, no I/O
        res = self.m["results"]
        self.assertEqual(ns["Bres"], res["partB_results"])
        self.assertEqual(dict(cells=ns["np_"], **ns["pair"]), res["partB_paired_cells_excluding_Boots"])
        self.assertEqual(dict(ns["bo"]), res["partB_Boots_marginal_cells_baseline_with_no_other_equipment"])
        pc = res["partB_paired_cells_excluding_Boots"]
        self.assertEqual((pc["cells"], pc["strionic_more_copies"], pc["seize_more_copies"], pc["seize_fewer_draws_incl_BMC"],
                          pc["seize_more_draws_incl_BMC"]), (756, 80, 42, 630, 0))
        bo = res["partB_Boots_marginal_cells_baseline_with_no_other_equipment"]
        self.assertEqual((bo["cells"], bo["Boots_adds_a_combat_vs_no_equipment"], bo["Boots_adds_copies_vs_no_equipment"]),
                         (342, 144, 48))
        scen = ns["scen"]
        # Rules branches: fizzle on removed target (608.2b); Greaves/Boots haste; Master keeps the token.
        self.assertEqual(scen("baseline", "ready", "target_removed_in_response", "none", "none", 0, False)["copies"], 0)
        self.assertEqual(scen("baseline", "sick", "valid", "none", "none", 3, False)["combats"], 0)
        self.assertEqual(scen("baseline", "sick", "valid", "Greaves", "none", 3, False)["copies"], 1)
        self.assertEqual(scen("strionic", "ready", "valid", "none", "none", 2, True)["token_kept"], 2)
        self.assertIsNone(scen("strionic", "ready", "valid", "Boots", "none", 2, False))
        self.assertEqual(scen("seize", "ready", "valid", "none", "none", 4, False)["combats"], 2)
        self.assertEqual(scen("seize", "ready", "valid", "none", "after_combat1", 6, False)["combats"], 1)

    def test_goldfish_cells_pinned_and_consistent(self):
        res = self.m["results"]
        self.assertEqual((res["seed"], res["games_per_config"], res["turns"]), (28, 20000, 7))
        A = res["partA_results"]
        self.assertEqual(set(A), set(CONFIGS))
        for cfg, rows in A.items():
            prev = {}
            for t in range(1, 8):
                c = rows[f"turn {t}"]
                self.assertLessEqual(c["P_Loki_attacks_with_valid_other_Villain_target"], c["P_Loki_on_battlefield"] + 1e-9)
                for k in ("P_Loki_on_battlefield", "P_cheap_Villain_MV3_or_less_deployed"):
                    self.assertGreaterEqual(c[k], prev.get(k, 0), (cfg, t, k))
                    prev[k] = c[k]
            if "Strionic" not in cfg:
                self.assertEqual(rows["turn 7"]["P_Strionic_activation_payable_on_attack"], 0, cfg)
            if "Seize" not in cfg:
                self.assertEqual(rows["turn 7"]["P_Seize_the_Day_castable_postcombat_on_attack"], 0, cfg)

        def att(cfg):
            return [A[cfg][f"turn {t}"]["P_Loki_attacks_with_valid_other_Villain_target"] for t in (4, 5, 6)]
        self.assertEqual(att("baseline"), [0.1803, 0.5849, 0.7069])
        self.assertEqual(att("plus_Strionic_Resonator_minus_Swiftfoot_Boots"), [0.1801, 0.5867, 0.7082])
        self.assertEqual(att("plus_Seize_the_Day_minus_Black_Market_Connections"), [0.1772, 0.5764, 0.7044])
        self.assertEqual(att("candidate_Ultimo_and_Elektra"), [0.1682, 0.5696, 0.7003])
        self.assertEqual(att("plus_Ultimo_minus_Crimson_Cowl")[0], 0.1746)
        self.assertEqual(att("plus_Elektra_minus_Killmonger")[0], 0.1763)
        s = A["plus_Strionic_Resonator_minus_Swiftfoot_Boots"]
        self.assertEqual([s[f"turn {t}"]["P_Strionic_activation_payable_on_attack"] for t in (5, 6, 7)], [0.0164, 0.0393, 0.0599])
        z = A["plus_Seize_the_Day_minus_Black_Market_Connections"]
        self.assertEqual([z[f"turn {t}"]["P_Seize_the_Day_castable_postcombat_on_attack"] for t in (4, 5, 6)],
                         [0.0006, 0.0066, 0.0219])
        cheap = [A["baseline"]["turn 3"]["P_cheap_Villain_MV3_or_less_deployed"],
                 A["plus_Ultimo_minus_Crimson_Cowl"]["turn 3"]["P_cheap_Villain_MV3_or_less_deployed"],
                 A["candidate_Ultimo_and_Elektra"]["turn 3"]["P_cheap_Villain_MV3_or_less_deployed"]]
        self.assertEqual(cheap, [0.3005, 0.2834, 0.2567])
        self.assertIn("Seeded finite Monte Carlo goldfish", res["partA_method"])
        self.assertIn("not win rates", res["partB_method"])

    def test_land_count_hypergeometric(self):
        # 34 lands in 99, opening seven: exact hypergeometric for 2-4 lands
        p = sum(math.comb(34, k) * math.comb(65, 7 - k) for k in range(2, 5)) / math.comb(99, 7)
        self.assertEqual(round(p, 4), 0.7195)

    def test_commander_spellbook_zero_included(self):
        c = json.loads(CSB.read_text())
        self.assertEqual(c["baseline"]["included"], [])
        self.assertEqual(c["candidate"]["included"], [])
        self.assertEqual(len(c["alternatives"]), 8)
        for k, v in c["alternatives"].items():
            self.assertEqual(v["included"], [], k)

    def test_rules_snapshot_anchors(self):
        r = RULES.read_text()
        for s in ("CR 508.4", "CR 603.6a", "CR 608.2b", "CR 702.18a", "CR 702.11b", "CR 707.2", "CR 107.3m",
                  "commander: legal", "not a Game Changer", "no project exception applies",
                  "Hela, Mistress of Darkness (release 2027-04-09)", "Mirror Universe Intrusion (release 2026-11-13)",
                  "**not** called legal"):
            self.assertIn(s, r)

    def test_unreleased_and_banned_excluded(self):
        live = {c["name"]: c for c in json.loads((RC / f"{D}_Scryfall_live_20261023.json").read_text())["cards"]}
        for n in ("Hela, Mistress of Darkness // Dark Tutor", "Mirror Universe Intrusion"):
            self.assertEqual(live[n]["commander_legality"], "not_legal", n)
            self.assertGreater(live[n]["released_at"], "2026-10-23", n)
        for n in ("Dockside Extortionist", "Jeweled Lotus"):
            self.assertEqual(live[n]["commander_legality"], "banned", n)
        for n in live:
            if live[n]["commander_legality"] != "legal":
                self.assertNotIn(n, self.cand)

    def test_receipt_is_bounded_not_win_rate(self):
        self.assertIn("not a win rate", self.m["purpose"])
        self.assertIn("no opponent", self.m["scripts"]["meas"])


if __name__ == "__main__":
    unittest.main()
