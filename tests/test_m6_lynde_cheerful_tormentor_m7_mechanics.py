"""Deck 31 Lynde__Cheerful_Tormentor (Lynde, Cheerful Tormentor) M7 research candidate: finite Oracle-anchored rules
checks and the bounded versions of the tests Pass C requested (1/2/3 self-Curse upkeep stacks, Braids / exile / DFC
return timing, extra-upkeep supply, Curse of Chaos versus Curse of Echoes and the author's Strionic Resonator and
Beseech the Mirror variants). Recomputes the exhaustive rules grids from the receipt's own embedded script and checks
the seeded goldfish cells for internal consistency. Not a game simulation or win rate; nothing here is owner approval."""
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
D = "Lynde__Cheerful_Tormentor"
LYNDE = "Lynde, Cheerful Tormentor"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
RULES = ROOT / f"data/grixis/m6/rules_snapshots/{D}_M7_20261023.md"
RC = ROOT / "data/grixis/m7/research_challengers"
MEAS = RC / f"{D}_bounded_measured_tests_20261023.json"
CSB = RC / f"{D}_CommanderSpellbook_20261023.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
ADDS = sorted(["Court of Vantress", "Extravagant Replication"])
CUTS = sorted(["Cruel Reality", "Curse of Death's Hold"])
GAME_CHANGERS = sorted(["Ancient Tomb", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship", "Imperial Seal",
                        "Jeska's Will", "Rhystic Study", "Vampiric Tutor"])


def library(path):
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"(\d+)x (.+?)( \[Commander\])?$", line.strip())
        if m and not m.group(3):
            out += [m.group(2)] * int(m.group(1))
    return out


class LyndeCheerfulTormentorM7Mechanics(unittest.TestCase):
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
        t = self.text(LYNDE)
        self.assertIn("Deathtouch", t)
        self.assertIn("Whenever a Curse is put into your graveyard from the battlefield, return it to the battlefield "
                      "attached to you at the beginning of the next end step.", t)
        self.assertIn("At the beginning of your upkeep, you may attach a Curse attached to you to one of your opponents. "
                      "If you do, draw two cards.", t)
        c = self.o[LYNDE]
        self.assertEqual(c["mana_cost"], "{1}{U}{B}{R}")
        self.assertEqual(c["type_line"], "Legendary Creature — Human Warlock")
        self.assertEqual((c["power"], c["toughness"]), ("2", "4"))
        self.assertEqual(c["commander_legality"], "legal")
        self.assertIs(c["game_changer"], False)
        self.assertEqual((c["set"], c["released_at"], c["oracle_id"]),
                         ("mic", "2021-09-24", "dc386f6c-bd4a-462a-8d42-0e7a552a4f17"))

    def test_libraries_99_35_lands_exactly_two_swaps(self):
        for lib in (self.base, self.cand):
            self.assertEqual(len(lib), 99)
            self.assertEqual(sum(1 for n in lib if "Land" in self.front(n)), 35)
            self.assertEqual((lib.count("Island"), lib.count("Mountain"), lib.count("Swamp")), (4, 3, 3))
        self.assertEqual(sorted((Counter(self.cand) - Counter(self.base)).elements()), ADDS)
        self.assertEqual(sorted((Counter(self.base) - Counter(self.cand)).elements()), CUTS)
        for n in set(self.cand) | {LYNDE}:
            self.assertEqual(self.o[n]["commander_legality"], "legal", n)
            self.assertTrue(set(self.o[n]["color_identity"]) <= {"U", "B", "R"}, n)
        for lib in (self.base, self.cand):
            self.assertEqual(sorted(n for n in set(lib) if self.o[n]["game_changer"]), GAME_CHANGERS)
        for n in ADDS:
            self.assertIs(self.o[n]["game_changer"], False, n)
        curses = [n for n in set(self.cand) if "Curse" in self.o[n]["type_line"]]
        self.assertEqual(len(curses), 19)  # 18 Curse cards plus Accursed Witch // Infectious Curse
        self.assertEqual(len([n for n in set(self.base) if "Curse" in self.o[n]["type_line"]]), 21)

    def test_swap_oracle(self):
        c = self.text("Court of Vantress")
        self.assertIn("When this enchantment enters, you become the monarch.", c)
        self.assertIn("If you're the monarch, you may create a token that's a copy of it.", c)
        self.assertIn("If you're not the monarch, you may have this enchantment become a copy of it", c)
        self.assertIn("create a token that's a copy of another target nonland permanent you control",
                      self.text("Extravagant Replication"))
        r = self.text("Cruel Reality")
        self.assertIn("At the beginning of enchanted player's upkeep, that player sacrifices a creature or planeswalker", r)
        self.assertIn("they lose 5 life", r)
        self.assertIn("Creatures enchanted player controls get -1/-1.", self.text("Curse of Death's Hold"))
        for n in ("Cruel Reality", "Curse of Death's Hold"):
            self.assertIn("Aura Curse", self.o[n]["type_line"], n)
        for n in ADDS:
            self.assertNotIn("Curse", self.o[n]["type_line"], n)  # adds are not Curses: Lynde does not return them

    def test_pass_c_and_staged_cards_oracle(self):
        self.assertIn("Destroy target permanent you own.", self.text("Staff of Compleation"))
        self.assertIn("Copy target triggered ability you control.", self.text("Strionic Resonator"))
        self.assertIn("Bargain", self.text("Beseech the Mirror"))
        self.assertIn("Whenever a player attacks enchanted player", self.text("Curse of Chaos"))
        self.assertIn("each other player may copy that spell", self.text("Curse of Echoes"))
        self.assertIn("Blue spells and red spells you cast cost {1} less to cast.", self.text("Nightscape Familiar"))
        self.assertNotIn("Curse", self.o["Grievous Wound"]["type_line"])  # rejected: not a Curse
        for n in ("The Unluckiest Planeswalker", "Jabs, Mistress of Mockery"):
            self.assertNotIn(n, self.o)  # excluded (not Commander-legal); never in any configuration

    def test_rules_grids_recomputed_from_receipt_script(self):
        src = self.m["scripts"]["meas"]
        part = src[src.index("# ---------------- Part B"):src.index('if __name__=="__main__":')]
        ns = {"itertools": itertools, "collections": collections}
        exec(part, ns)  # deterministic enumerated grids; no randomness, no I/O
        B = ns["gridB"]()
        self.assertEqual(B, self.m["results"]["B"])
        b1 = B["B1_self_curse_upkeep_stack_best_ordering"]
        self.assertEqual((b1["cells"], b1["cells_with_Cruel_Reality"], b1["Lynde_lost_with_Cruel_Reality"],
                          b1["Lynde_lost_without_Cruel_Reality"], b1["cells_with_Deaths_Hold"],
                          b1["X1_creature_killed_with_Deaths_Hold"], b1["X1_creature_killed_without_Deaths_Hold"],
                          b1["max_life_lost"], b1["Torment_cells"], b1["Torment_cells_zero_life"]),
                         (246, 96, 42, 0, 96, 32, 0, 2, 96, 72))
        self.assertEqual(len(B["B2_rules_cases"]["cases"]), 12)
        b3 = B["B3_extra_upkeep_and_copy_engine_supply"]
        self.assertEqual((b3["cells"], b3["draws_none"], b3["draws_Court_monarch"], b3["tokens_Court_monarch"],
                          b3["draws_Court_not_monarch"], b3["tokens_Court_not_monarch"],
                          b3["draws_Extravagant_Replication"], b3["tokens_Extravagant_Replication"],
                          b3["tokens_Court_monarch_plus_Replication"]),
                         (180, 82, 204, 102, 82, 0, 204, 102, 204))
        b4 = B["B4_removal_and_return_cut_versus_add"]
        self.assertEqual((b4["cells"], b4["Cruel_Reality_self_harm"], b4["Cruel_Reality_returns"],
                          b4["Curse_of_Deaths_Hold_self_harm"], b4["Curse_of_Deaths_Hold_returns"],
                          b4["Court_of_Vantress_returns"], b4["Extravagant_Replication_returns"]),
                         (72, 6, 6, 4, 6, 0, 0))

    def test_goldfish_cells_pinned_and_consistent(self):
        A = self.m["results"]["A"]
        self.assertEqual(len(A), 12)
        self.assertIn("seed 31", self.m["scripts"]["meas"])
        for cfg, rows in A.items():
            prev = {}
            for t in range(1, 8):
                c = rows[f"turn {t}"]
                for k, v in c.items():
                    self.assertLessEqual(v, c["P_Lynde_cast"] + 1e-9, (cfg, t, k))
                    self.assertGreaterEqual(v, prev.get(k, 0), (cfg, t, k))
                    prev[k] = v

        def at(cfg, t, k="P_Lynde_cast"):
            return A[cfg][f"turn {t}"][k]
        for cfg in ("baseline", "candidate"):
            self.assertEqual((at(cfg, 4), at(cfg, 7)), (0.629, 0.8681))
            self.assertEqual(at(cfg, 7, "P_Lynde_plus_repeatable_sacrifice_outlet"), 0.2716)
            self.assertEqual(at(cfg, 7, "P_Lynde_plus_extra_upkeep_source"), 0.2622)
        self.assertEqual(at("baseline", 7, "P_Lynde_plus_Court_or_Replication"), 0.0)
        self.assertEqual(at("candidate", 7, "P_Lynde_plus_Court_or_Replication"), 0.1381)
        self.assertEqual(at("baseline", 7, "P_Lynde_plus_Cruel_Reality_or_Deaths_Hold"), 0.1051)
        self.assertEqual(at("candidate", 7, "P_Lynde_plus_Cruel_Reality_or_Deaths_Hold"), 0.0)
        st = "on_candidate_staged_plus_Staff_of_Compleation_minus_Nightscape_Familiar"
        self.assertEqual((at(st, 4), at(st, 7), at(st, 7, "P_Lynde_plus_repeatable_sacrifice_outlet")),
                         (0.6179, 0.8601, 0.3379))
        self.assertEqual(at("on_candidate_PassC_plus_Strionic_Resonator_minus_Nightscape_Familiar", 7), 0.8601)
        for cfg in ("on_candidate_PassC_plus_Curse_of_Chaos_minus_Curse_of_Echoes",
                    "on_candidate_PassC_plus_Beseech_the_Mirror_minus_Curse_of_the_Restless_Dead"):
            self.assertEqual(A[cfg], A["candidate"], cfg)  # the deployment model does not score these Curses

    def test_land_count_hypergeometric(self):
        p = sum(math.comb(35, k) * math.comb(64, 7 - k) for k in range(2, 5)) / math.comb(99, 7)
        self.assertEqual(round(p, 4), 0.7306)

    def test_commander_spellbook_counts(self):
        c = json.loads(CSB.read_text())
        self.assertEqual(len(c["baseline"]["included"]), 0)
        self.assertEqual(len(c["candidate"]["included"]), 0)
        self.assertEqual((c["baseline"]["almost_included_count"], c["candidate"]["almost_included_count"]), (17, 22))
        self.assertEqual(len(c["alternatives"]), 10)
        for k, v in c["alternatives"].items():
            self.assertEqual(len(v["included"]), 0, k)

    def test_rules_snapshot_anchors(self):
        r = RULES.read_text()
        for s in ("CR 303.4f", "CR 303.4h", "CR 503.1a", "CR 603.7c", "CR 603.10a", "CR 704.5d", "CR 704.5m",
                  "CR 712.8a", "commander: legal", "not a Game Changer", "No preview caveat and no project exception",
                  "**no rulings**", "Jabs, Mistress of Mockery", "9b26aa28fc7e16f6652aaec292b4edf84e20db71"):
            self.assertIn(s, r)

    def test_receipt_is_bounded_not_win_rate(self):
        self.assertIn("Neither part is a win-rate simulation", self.m["scripts"]["meas"])
        self.assertIn("no opponent", self.m["scripts"]["meas"])


if __name__ == "__main__":
    unittest.main()
