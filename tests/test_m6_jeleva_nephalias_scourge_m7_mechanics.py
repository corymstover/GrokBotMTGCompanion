"""Deck 24 Jeleva, Nephalia's Scourge M7: finite exact (no RNG) Oracle-anchored checks and bounded Pass C tests.

Recomputes, from the frozen Oracle snapshot and the vendored baseline, the exact numbers recorded in the bounded
measured-tests receipt (stager access with and without Intuition, haste/flash enabler access with Borne Upon a Wind vs
Galvanic Iteration, Mox Opal metalcraft, Spellseeker reach, land colour sources, Commander Spellbook deltas) and pins
the rules facts the research-only conclusion depends on. These are not win rates; nothing here is approval.
"""
import json
import re
import unittest
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = "Jeleva__Nephalia_s_Scourge"
J = "Jeleva, Nephalia's Scourge"
RC = ROOT / "data/grixis/m7/research_challengers"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
MEAS = RC / f"{D}_bounded_measured_tests_20261023.json"
CSB = RC / f"{D}_CommanderSpellbook_20261023.json"
RULES = ROOT / f"data/grixis/m6/rules_snapshots/{D}_M7_20261023.md"
STAGERS = {"Mystical Tutor", "Vampiric Tutor", "Imperial Seal", "Personal Tutor", "Scheming Symmetry", "Long-Term Plans",
           "Lim-D\u00fbl's Vault", "Brainstorm", "Scroll Rack", "Sensei's Divining Top", "Ponder"}
ENABLERS = {"Torch Courier", "Lightning Greaves", "Arena of Glory", "Borne Upon a Wind"}
WINDOWS = {7: "opening 7", 8: "turn 1 on the draw / turn 2 on the play (8)", 9: "turn 3 on the play (9)",
           10: "turn 3 on the draw / turn 4 on the play (10)"}


def library(path):
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"(\d+)x (.+?)( \[Commander\])?$", line.strip())
        if m and not m.group(3):
            out += [m.group(2)] * int(m.group(1))
    return out


def p_ge1(k, seen, n=99):
    return round(1 - comb(n - k, seen) / comb(n, seen), 4)


class JelevaMechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        snap = json.loads(SNAP.read_text())
        cls.o = {c["name"]: c for c in snap["cards"]}
        cls.snap = snap
        cls.m = json.loads(MEAS.read_text())
        cls.lib = library(BASE)
        cls.lands = [n for n in cls.lib if "Land" in cls.o[n]["type_line"]]

    def text(self, n):
        return self.o[n]["oracle_text"]

    def test_commander_oracle_x_exile_and_free_cast_on_attack(self):
        t = self.text(J)
        self.assertIn("When Jeleva enters, each player exiles the top X cards of their library, where X is the amount "
                      "of mana spent to cast Jeleva.", t)
        self.assertIn("Whenever Jeleva attacks, you may cast an instant or sorcery spell from among cards exiled with "
                      "Jeleva without paying its mana cost.", t)
        self.assertEqual(self.o[J]["mana_cost"], "{1}{U}{B}{R}")
        self.assertIn("Wizard", self.o[J]["type_line"])
        self.assertIn("that ability triggers an additional time", self.text("Harmonic Prodigy"))

    def test_library_is_99_with_27_lands_and_singleton(self):
        self.assertEqual(len(self.lib), 99)
        self.assertEqual(len(set(self.lib)), 99)
        self.assertEqual(len(self.lands), 27)

    def test_t1_stager_access_recomputed_exactly(self):
        st = [n for n in self.lib if n in STAGERS]
        self.assertEqual(len(st), 11)
        self.assertEqual(self.m["T1_stagers"]["count_in_baseline"], 11)
        self.assertEqual(set(self.m["T1_stagers"]["cards"]), STAGERS)
        self.assertIn("third from the top", self.text("Long-Term Plans"))
        self.assertIn("puts that card on top", self.text("Scheming Symmetry"))
        self.assertIn("the rest into your graveyard", self.text("Intuition"))
        self.assertNotIn("on top", self.text("Intuition"))
        rec = self.m["T1_stager_access_exact"]
        for seen, key in WINDOWS.items():
            row = rec[key]
            self.assertEqual(row["baseline_P_ge1_stager"], p_ge1(11, seen))
            minus = [v for k, v in row.items() if k.startswith("minus_one_stager (")][0]
            self.assertEqual(minus, p_ge1(10, seen))
            self.assertLess(minus, row["baseline_P_ge1_stager"])
        self.assertEqual([p_ge1(11, s) for s in WINDOWS], [0.5736, 0.6246, 0.6699, 0.7103])
        self.assertIn("'waits two draws' is false", self.m["T1_rules"])

    def test_t2_intuition_hostile_piles_enumerated(self):
        piles = [tuple(x["pile"]) for x in self.m["T2_Intuition_hostile_enumeration"]]
        self.assertIn(("Underworld Breach", "Lion's Eye Diamond", "Brain Freeze"), piles)
        self.assertGreaterEqual(len(piles), 3)
        for x in self.m["T2_Intuition_hostile_enumeration"]:
            self.assertIn("hostile_result", x["opponent_choice_outcomes"], x["pile"])
        self.assertIn("Intuition never beats Long-Term Plans or Scheming Symmetry", self.m["T2_conclusion"])
        self.assertIn("115.3", self.m["T2_conclusion"])

    def test_t3_galvanic_vs_borne_enablers_exact(self):
        en = [n for n in self.lib if n in ENABLERS]
        self.assertEqual(len(en), 4)
        g = self.m["T3_Galvanic_vs_Borne"]
        self.assertEqual(set(g["haste_or_flash_enablers_baseline"]), ENABLERS)
        self.assertEqual(g["instants_and_sorceries_in_99"],
                         sum(1 for n in self.lib if any(t in self.o[n]["type_line"] for t in ("Instant", "Sorcery"))))
        self.assertEqual(sorted(g["copy_no_value_or_harmful"]),
                         ["Demonic Consultation", "Doomsday", "Final Fortune", "Mnemonic Betrayal",
                          "Peer into the Abyss", "Tainted Pact", "Toxic Deluge", "Yawgmoth's Will"])
        self.assertIn("707.10", g["rules"])
        self.assertIn("copy that spell", self.text("Galvanic Iteration"))
        self.assertIn("as though they had flash", self.text("Borne Upon a Wind"))
        rec = self.m["T3_enabler_access_exact"]
        for seen, key in WINDOWS.items():
            self.assertEqual(rec[key]["baseline (4 enablers)"], p_ge1(4, seen))
            self.assertEqual(rec[key]["Galvanic replacing Borne (3 enablers)"], p_ge1(3, seen))
        self.assertEqual((p_ge1(4, 7), p_ge1(4, 10), p_ge1(3, 7), p_ge1(3, 10)), (0.2577, 0.3514, 0.1994, 0.276))

    def test_t4_mox_opal_metalcraft_exact(self):
        art = sorted(n for n in self.lib if "Artifact" in self.o[n]["type_line"])
        self.assertEqual(len(art), 16)
        self.assertEqual(art, sorted(self.m["T4_Mox_Opal"]["artifacts_in_99"]))
        got = {}
        for k in (6, 7, 8, 9):
            p = 1 - sum(comb(15, i) * comb(83, k - i) for i in (0, 1)) / comb(98, k)
            got[f"{k} other cards"] = round(p, 4)
        self.assertEqual(got, self.m["T4_Mox_Opal"]["P_ge2_other_artifacts_given_Opal_in_hand"])
        self.assertEqual(list(got.values()), [0.2277, 0.2906, 0.3536, 0.4152])

    def test_t5_spellseeker_reach(self):
        isp = sorted(n for n in self.lib if any(t in self.o[n]["type_line"] for t in ("Instant", "Sorcery"))
                     and self.o[n]["cmc"] <= 2)
        self.assertEqual(len(isp), 29)
        self.assertEqual(isp, sorted(self.m["T5_Spellseeker_reach"]["MV_le_2_instants_sorceries"]))
        self.assertIn("mana value 2 or less", self.text("Spellseeker"))

    def test_t6_land_colour_sources(self):
        per = self.m["T6_land_colour_sources"]["per_land"]
        self.assertEqual(sorted(per), sorted(self.lands))
        cnt = {c: sum(1 for v in per.values() if c in v) for c in "UBR"}
        self.assertEqual(cnt, {"U": 21, "B": 20, "R": 19})
        self.assertEqual(self.m["T6_land_colour_sources"]["U_B_R"], cnt)
        self.assertIn("{T}: Add {C}.", self.text("Hanweir Battlements"))
        self.assertIn("target opponent creates a 1/1", self.text("Forbidden Orchard"))
        self.assertIn("Add {R}{R}. If any of that mana is spent on a creature spell, it gains haste", self.text("Arena of Glory"))

    def test_commander_spellbook_deltas(self):
        c = json.loads(CSB.read_text())
        base = {x["id"] for x in c["baseline"]["included"]}
        self.assertEqual(len(base), 7)
        for k, v in c["alternatives"].items():
            extra = {x["id"] for x in v["included"]} - base
            if "DramaticReversal" in k:
                self.assertEqual(len(extra), 1, k)
                self.assertEqual(len(v["included"]), 8)
            else:
                self.assertEqual(extra, set(), k)
                self.assertEqual(len(v["included"]), 7, k)

    def test_rules_snapshot_anchors(self):
        r = RULES.read_text()
        for s in ("607.2a", "603.2d", "707.10", "903.8", "302.6", "115.3", "702.10b"):
            self.assertIn(s, r)
        self.assertIn("If it's not your turn", self.text("Force of Negation"))
        self.assertIn("lose the game", self.text("Final Fortune"))
        self.assertIn("haste and shroud", self.text("Lightning Greaves"))
        self.assertIn("Haste", self.text("Torch Courier"))

    def test_banned_and_off_identity_excluded(self):
        for n in ("Dockside Extortionist", "Jeweled Lotus", "Mana Crypt", "Manamorphose"):
            self.assertNotIn(n, self.lib)
        live = {c["name"]: c for c in json.loads((RC / f"{D}_Scryfall_live_20261023.json").read_text())["cards"]}
        self.assertEqual(live["Dockside Extortionist"]["commander_legality"], "banned")
        self.assertIn("G", live["Manamorphose"]["color_identity"])
        self.assertEqual(self.o[J]["commander_legality"], "legal")
        self.assertIs(self.o[J]["game_changer"], False)

    def test_receipt_is_bounded_not_win_rate(self):
        self.assertIn("exact hypergeometric", self.m["method"])
        self.assertIn("no sampling", self.m["method"])
        self.assertTrue(self.m["not_run_and_why"])


if __name__ == "__main__":
    unittest.main()
