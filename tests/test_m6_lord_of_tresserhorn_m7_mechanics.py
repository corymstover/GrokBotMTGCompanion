"""Deck 29 Lord_of_Tresserhorn (Lord of Tresserhorn) M7 review candidate: finite Oracle-anchored rules checks and the
bounded versions of the tests Pass C requested (Fierce Guardianship protection, Soul's Fire / Distortion Strike /
Aqueous Form conversion and evasion, Sheoldred's Edict interaction, and the Dress Down + Kediss + Phyresis layer-6
case). Uses Lord's actual Oracle text: enters -> you lose 2 life, sacrifice two creatures, target opponent draws two;
{B}: regenerate Lord. There is no opponent-regeneration clause. Recomputes the exhaustive rules grids from the receipt's
own embedded script and checks the seeded goldfish cells for internal consistency. Not a game simulation or win rate;
nothing here is owner approval."""
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
D = "Lord_of_Tresserhorn"
LORD = "Lord of Tresserhorn"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
RULES = ROOT / f"data/grixis/m6/rules_snapshots/{D}_M7_20261023.md"
RC = ROOT / "data/grixis/m7/research_challengers"
MEAS = RC / f"{D}_bounded_measured_tests_20261023.json"
CSB = RC / f"{D}_CommanderSpellbook_20261023.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
ADDS = ["Black Market Connections", "Consign to Memory", "Fierce Guardianship", "Ornithopter of Paradise", "Skullclamp"]
CUTS = ["Cover of Darkness", "Feed the Swarm", "Fellwar Stone", "Sheoldred's Edict", "Stubborn Denial"]


def library(path):
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"(\d+)x (.+?)( \[Commander\])?$", line.strip())
        if m and not m.group(3):
            out += [m.group(2)] * int(m.group(1))
    return out


def p_lands(lo, hi, lands=35, n=99, draw=7):
    return sum(math.comb(lands, k) * math.comb(n - lands, draw - k) for k in range(lo, hi + 1)) / math.comb(n, draw)


class LordOfTresserhornM7Mechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.base, cls.cand = library(BASE), library(CAND)
        cls.m = json.loads(MEAS.read_text())

    def text(self, n):
        return self.o[n]["oracle_text"]

    def front(self, n):
        return self.o[n]["type_line"].split(" // ")[0]

    def test_commander_actual_oracle_no_opponent_regeneration(self):
        t = self.text(LORD)
        self.assertEqual(t, "When Lord of Tresserhorn enters, you lose 2 life, you sacrifice two creatures, and target "
                            "opponent draws two cards.\n{B}: Regenerate Lord of Tresserhorn.")
        self.assertNotIn("opponent regenerat", t.lower())
        self.assertEqual(t.count("Regenerate"), 1)
        c = self.o[LORD]
        self.assertEqual(c["mana_cost"], "{1}{U}{B}{R}")
        self.assertEqual((c["power"], c["toughness"]), ("10", "4"))
        self.assertIn("Zombie", c["type_line"])
        self.assertEqual(c["commander_legality"], "legal")
        self.assertIs(c["game_changer"], False)
        self.assertEqual((c["set"], c["released_at"]), ("me1", "2007-09-10"))

    def test_libraries_99_35_lands_exactly_five_swaps(self):
        for lib in (self.base, self.cand):
            self.assertEqual(len(lib), 99)
            self.assertEqual(sum(1 for n in lib if "Land" in self.front(n)), 35)
        self.assertEqual(sorted((Counter(self.cand) - Counter(self.base)).elements()), ADDS)
        self.assertEqual(sorted((Counter(self.base) - Counter(self.cand)).elements()), CUTS)
        for n in set(self.cand) | {LORD}:
            self.assertEqual(self.o[n]["commander_legality"], "legal", n)
            self.assertTrue(set(self.o[n]["color_identity"]) <= {"U", "B", "R"}, n)
        gcs = sorted(n for n in set(self.cand) if self.o[n]["game_changer"])
        self.assertEqual(gcs, ["Demonic Tutor", "Fierce Guardianship", "Vampiric Tutor"])
        self.assertEqual(sorted(n for n in set(self.base) if self.o[n]["game_changer"]), ["Demonic Tutor", "Vampiric Tutor"])

    def test_swap_oracle_anchors(self):
        self.assertIn("If you control a commander, you may cast this spell without paying its mana cost.",
                      self.text("Fierce Guardianship"))
        self.assertIn("Ferocious — If you control a creature with power 4 or greater, counter that spell instead.",
                      self.text("Stubborn Denial"))
        self.assertIn("Counter target triggered ability or colorless spell.", self.text("Consign to Memory"))
        self.assertIn("Destroy target creature or enchantment an opponent controls.", self.text("Feed the Swarm"))
        self.assertIn("Create a 3/2 colorless Shapeshifter creature token with changeling.",
                      self.text("Black Market Connections"))
        self.assertIn("Creatures of the chosen type have fear.", self.text("Cover of Darkness"))
        self.assertIn("{T}: Add one mana of any color.", self.text("Ornithopter of Paradise"))
        self.assertIn("Artifact Creature", self.o["Ornithopter of Paradise"]["type_line"])
        self.assertNotIn("Creature", self.o["Fellwar Stone"]["type_line"])
        self.assertIn("Whenever equipped creature dies, draw two cards.", self.text("Skullclamp"))
        self.assertIn("Each opponent sacrifices a nontoken creature of their choice.", self.text("Sheoldred's Edict"))
        self.assertIn("Creatures lose all abilities.", self.text("Dress Down"))
        self.assertIn("Counter target activated or triggered ability.", self.text("Stifle"))

    def test_rules_grid_recomputed_from_receipt_script(self):
        src = self.m["scripts"]["meas"]
        part = src[src.index("# ---------------- Part B"):src.index("out={")]
        ns = {"itertools": itertools, "collections": collections}
        exec(part, ns)  # deterministic enumerated grids; no randomness, no I/O
        B = self.m["results"]["partB_results"]
        self.assertEqual(ns["B"], B)

        def pick(k, *f):
            return tuple(B[k][x] for x in f)
        self.assertEqual(pick("B1_evasion_Cover_vs_Aqueous", "cells", "Cover_connects", "AqueousForm_connects"), (24, 12, 15))
        self.assertEqual(pick("B2_conversion_Pain_vs_TBR_vs_SoulsFire", "cells", "Pain_for_All_kills",
                              "Temur_Battle_Rage_kills", "Souls_Fire_kills", "Pain_kills_SoulsFire_does_not"),
                         (972, 108, 174, 216, 0))
        self.assertEqual(pick("B3_interaction_Edict_vs_kept_suite_and_SoulsFire", "cells", "Edict_answers",
                              "SoulsFire_answers", "Edict_answers_and_no_kept_spot_removal_does",
                              "Edict_answers_and_no_kept_removal_incl_sweepers_does"), (14, 10, 4, 2, 0))
        self.assertEqual(pick("B4_protection_StubbornDenial_vs_FierceGuardianship", "cells", "FG_answers",
                              "Denial_answers", "FG_only", "Denial_only"), (40, 17, 9, 8, 0))
        self.assertEqual(pick("B6_Consign_to_Memory_vs_Feed_the_Swarm", "cells", "Consign_only", "Feed_only"), (8, 5, 2))
        # CR 903.3d: Lord on the stack is not a controlled commander, so FG is a {2}{U} hard cast there.
        fg, sd = ns["fg"], ns["sd"]
        self.assertFalse(fg("counterspell_on_Lord_cast", 2, "Lord_controlled"))
        self.assertTrue(fg("counterspell_on_Lord_cast", 3, "Lord_not_controlled"))
        self.assertTrue(fg("noncreature_wrath", 0, "Lord_controlled"))
        self.assertFalse(fg("creature_spell_threat", 3, "Lord_controlled"))
        self.assertFalse(sd("counterspell_on_Lord_cast", 3, "Lord_controlled"))  # ferocious off while Lord is on the stack
        self.assertTrue(sd("noncreature_wrath", 1, "Lord_controlled"))

    def test_dress_down_layer6_truth_table(self):
        b5 = self.m["results"]["partB_results"]["B5_Dress_Down_layer6_truth_table"]
        rows = b5["rows"]
        self.assertEqual(b5["cells"], 24)
        self.assertEqual(len(rows), 24)
        keys = {(r["phyresis"], r["haste_source"], r["tainted"]) for r in rows}
        self.assertEqual(len(keys), 24)
        for r in rows:
            # CR 613.1f / 613.7: later-timestamp grants survive Dress Down, earlier ones do not.
            self.assertEqual(r["Lord_has_infect"], r["phyresis"] == "after_Dress_Down" or r["tainted"] != "none", r)
            self.assertEqual(r["Lord_has_haste"], r["haste_source"] == "Greaves_reequipped_after_Dress_Down", r)
            self.assertIs(r["Kediss_trigger_live"], False)  # Kediss is a creature; its ability is gone too
            self.assertIs(r["regenerate_available"], False)  # Lord's own {B} regeneration is lost that turn
            self.assertIs(r["Lord_ETB_suppressed_if_Dress_Down_resolved_before_Lord_enters"], True)
        self.assertEqual(sum(r["Lord_has_infect"] for r in rows), 16)
        self.assertEqual(sum(r["Lord_has_haste"] for r in rows), 6)
        self.assertIn("CR 613.7", b5["notes"])
        self.assertIn("Lord's own {B} regeneration is also gone that turn", b5["notes"])

    def test_goldfish_cells_pinned_and_consistent(self):
        res = self.m["results"]
        self.assertEqual((res["seed"], res["games_per_config"], res["turns"]), (29, 20000, 7))
        A = res["partA_results"]
        self.assertEqual(len(A), 30)
        for cfg, rows in A.items():
            prev = {}
            for t in range(1, 8):
                c = rows[f"turn {t}"]
                self.assertLessEqual(c["P_Lord_attack_ready_with_conversion_card"], c["P_Lord_attack_ready"] + 1e-9)
                self.assertLessEqual(c["P_Lord_attack_ready"], c["P_Lord_on_battlefield"] + 1e-9)
                self.assertLessEqual(c["P_Lord_out_with_free_protection_in_hand"],
                                     c["P_Lord_out_with_any_counter_or_protection_in_hand"] + 1e-9)
                self.assertLessEqual(c["P_Lord_on_battlefield_without_paying_ETB"], c["P_Lord_on_battlefield"] + 1e-9)
                for k in ("P_Lord_on_battlefield", "mean_cards_seen"):
                    self.assertGreaterEqual(c[k], prev.get(k, 0), (cfg, t, k))
                    prev[k] = c[k]
            if "Skullclamp" not in cfg and cfg not in ("candidate",) and not cfg.startswith(("alt_B", "alt_C", "alt_D", "alt_E",
                                                                                            "alt_F", "alt_G")):
                self.assertEqual(rows["turn 7"]["mean_Skullclamp_draws"], 0, cfg)

        def dep(cfg):
            return [A[cfg][f"turn {t}"]["P_Lord_on_battlefield"] for t in (4, 5, 6)]
        self.assertEqual(dep("baseline"), [0.2717, 0.4783, 0.6121])
        self.assertEqual(dep("candidate"), [0.3068, 0.529, 0.6613])
        self.assertEqual(dep("alt_A_four_swaps_keep_Sheoldreds_Edict_no_Skullclamp")[2], 0.6563)
        self.assertEqual(dep("alt_B_Skullclamp_minus_Muddle_the_Mixture_keep_Edict")[2], 0.6672)
        self.assertEqual(dep("alt_C_Skullclamp_minus_Nightscape_Familiar")[2], 0.6438)
        self.assertEqual(dep("alt_D_candidate_plus_Aqueous_Form_minus_Muddle_the_Mixture")[2], 0.6637)
        self.assertEqual(dep("alt_E_candidate_plus_Distortion_Strike_minus_Rogues_Passage_34_lands")[2], 0.649)
        self.assertEqual(dep("alt_G_prior_draft_TBR_minus_Pain_for_All_instead_of_Consign")[2], 0.6538)
        self.assertEqual(dep("alt_F_original_tentative_plan")[2], 0.5674)
        self.assertEqual(dep("probe_single_plus_Fierce_Guardianship_minus_Nightscape_Familiar")[2], 0.5856)
        self.assertEqual(dep("probe_single_plus_Souls_Fire_minus_Sheoldreds_Edict")[2], 0.6107)
        self.assertEqual(dep("single_plus_Black_Market_Connections_minus_Cover_of_Darkness")[2], 0.6381)
        self.assertEqual(dep("single_plus_Ornithopter_of_Paradise_minus_Fellwar_Stone")[0], 0.2879)
        t6 = {k: A[k]["turn 6"] for k in ("baseline", "candidate")}
        self.assertEqual((t6["baseline"]["P_Lord_out_with_free_protection_in_hand"],
                          t6["candidate"]["P_Lord_out_with_free_protection_in_hand"]), (0.1208, 0.1969))
        self.assertEqual((t6["baseline"]["P_Lord_attack_ready_with_conversion_card"],
                          t6["candidate"]["P_Lord_attack_ready_with_conversion_card"]), (0.2352, 0.2683))
        self.assertEqual(t6["candidate"]["mean_Skullclamp_draws"], 0.26)
        self.assertIn("Seeded finite Monte Carlo goldfish", res["partA_method"])
        self.assertIn("not win rates", res["partB_method"])
        self.assertIn("B4 protection (Stubborn Denial vs Fierce Guardianship", res["partB_method"])

    def test_land_count_hypergeometric(self):
        # 35 lands in 99, opening seven: exact hypergeometric (unchanged by the swaps)
        self.assertEqual(round(p_lands(2, 4), 4), 0.7306)
        self.assertEqual(round(p_lands(1, 3), 4), 0.7603)
        self.assertEqual(round(p_lands(1, 4), 4), 0.9069)

    def test_commander_spellbook_included_unchanged(self):
        c = json.loads(CSB.read_text())
        self.assertEqual(len(c["baseline"]["included"]), 19)
        self.assertEqual(sorted(map(json.dumps, c["candidate"]["included"])), sorted(map(json.dumps, c["baseline"]["included"])))
        self.assertEqual((c["baseline"]["almost_included_count"], c["candidate"]["almost_included_count"]), (283, 289))
        self.assertEqual(len(c["alternatives"]), 9)
        for k, v in c["alternatives"].items():
            self.assertEqual(len(v["included"]), 19, k)

    def test_rules_snapshot_anchors(self):
        r = RULES.read_text()
        for s in ("no opponent-regeneration clause", "CR 701.19a", "CR 701.21a", "CR 903.3d", "CR 613.1f", "CR 613.7",
                  "CR 704.5f", "CR 903.10a", "CR 702.90", "commander: legal", "not a Game Changer",
                  "no preview caveat or project exception applies", "Live data was not written into the frozen cache"):
            self.assertIn(s, r)

    def test_off_identity_excluded_and_candidate_legal(self):
        live = json.loads((RC / f"{D}_Scryfall_live_20261023.json").read_text())
        self.assertIn("frozen cache untouched", live["purpose"])
        cards = {c["name"]: c for c in live["cards"]}
        for n in set(self.cand) & set(cards):
            self.assertEqual(cards[n]["commander_legality"], "legal", n)
        for n in live["excluded_off_identity_or_illegal"]:
            self.assertNotIn(n, self.cand)

    def test_receipt_is_bounded_not_win_rate(self):
        self.assertIn("not a win rate", self.m["purpose"])
        self.assertIn("no opponent", self.m["scripts"]["meas"])


if __name__ == "__main__":
    unittest.main()
