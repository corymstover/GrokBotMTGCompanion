"""Deck 23 Inalla, Archmage Ritualist M7: finite exact (no RNG) Oracle-anchored checks and bounded Pass C tests.

Recomputes, from the frozen Oracle snapshot and the vendored baseline, the exact numbers recorded in the bounded
measured-tests receipt (lands-only castability, Spellseeker vs Micromancer reach, Thundertrap Trainer hit rate) and
pins the rules facts the research-only conclusion depends on. These are not win rates; nothing here is approval.
"""
import json
import re
import unittest
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = "Inalla__Archmage_Ritualist"
RC = ROOT / "data/grixis/m7/research_challengers"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
MEAS = RC / f"{D}_bounded_measured_tests_20261023.json"
CSB = RC / f"{D}_CommanderSpellbook_20261023.json"
RULES = ROOT / f"data/grixis/m6/rules_snapshots/{D}_M7_20261023.md"
KEFKA = "Kefka, Court Mage // Kefka, Ruler of Ruin"
FETCH = {"Arid Mesa", "Bloodstained Mire", "Flooded Strand", "Marsh Flats", "Misty Rainforest", "Polluted Delta",
         "Scalding Tarn", "Verdant Catacombs", "Wooded Foothills"}
ANY = {"Command Tower", "City of Brass", "Mana Confluence", "Exotic Orchard"}
U_L = {"Underground Sea", "Watery Grave", "Morphic Pool", "Volcanic Island", "Steam Vents", "Island",
       "Otawara, Soaring City"}
R_L = {"Badlands", "Blood Crypt", "Volcanic Island", "Steam Vents"}


def library(path):
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"(\d+)x (.+?)( \[Commander\])?$", line.strip())
        if m and not m.group(3):
            out += [m.group(2)] * int(m.group(1))
    return out


def p_joint(lands, special, n_deck, seen, need_lands, need_special):
    k, other = len(special), len(lands) - len(special)
    tot = 0
    for s in range(need_special, k + 1):
        for o in range(other + 1):
            if need_lands <= s + o <= seen:
                tot += comb(k, s) * comb(other, o) * comb(n_deck - len(lands), seen - s - o)
    return tot / comb(n_deck, seen)


class InallaMechanics(unittest.TestCase):
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

    def test_commander_oracle_eminence_and_tap_five(self):
        t = self.text("Inalla, Archmage Ritualist")
        self.assertIn("Eminence \u2014 Whenever another nontoken Wizard you control enters, if Inalla is in the command zone "
                      "or on the battlefield, you may pay {1}", t)
        self.assertIn("create a token that's a copy of that Wizard. The token gains haste.", t)
        self.assertIn("Tap five untapped Wizards you control: Target player loses 7 life.", t)
        self.assertNotIn("{T}:", t)  # no tap symbol, so summoning-sick Wizards and hasty tokens can pay (CR 302.6)
        self.assertEqual(self.o["Inalla, Archmage Ritualist"]["mana_cost"], "{2}{U}{B}{R}")

    def test_library_is_99_with_27_lands(self):
        self.assertEqual(len(self.lib), 99)
        self.assertEqual(len(self.lands), 27)
        self.assertEqual(self.m["deck_stats"]["base.txt"]["lands"], 27)

    def test_t1_lands_only_castability_recomputed_exactly(self):
        R = [n for n in self.lands if n in FETCH | ANY | R_L | {"Cavern of Souls"}]
        U = [n for n in self.lands if n in FETCH | ANY | U_L | {"Cavern of Souls"}]
        tbl = self.m["T1_castability"]["results"]
        row = tbl["turn 3 on the draw / turn 4 on the play (7+3)"]
        n = 99
        dual = round(p_joint(self.lands, R, n, 10, 3, 2), 4)
        kefka = round(sum(comb(27, i) * comb(72, 10 - i) for i in range(5, 11)) / comb(99, 10), 4)
        micro = round(p_joint(self.lands, U, n, 10, 4, 1), 4)
        snap = round(p_joint(self.lands, U, n, 10, 2, 1), 4)
        self.assertEqual((dual, kefka, micro, snap), (0.4605, 0.0958, 0.2717, 0.8045))
        vals = sorted(row.values())
        for v in (dual, kefka, micro, snap):
            self.assertIn(v, vals)

    def test_t2_spellseeker_vs_micromancer_reach(self):
        isp = [n for n in self.lib if any(t in self.o[n]["type_line"] for t in ("Instant", "Sorcery"))]
        seeker = sorted(n for n in isp if self.o[n]["cmc"] <= 2)
        micro = sorted(n for n in isp if self.o[n]["cmc"] == 1)
        self.assertEqual((len(seeker), len(micro), len(set(seeker) - set(micro))), (33, 20, 13))
        rec = self.m["T2_tutor_reach"]
        self.assertEqual(rec["Spellseeker_MV_le_2_instant_sorcery"], seeker)
        self.assertEqual(rec["Micromancer_MV_eq_1_instant_sorcery"], micro)
        self.assertIn("mana value 1,", self.text("Micromancer"))
        self.assertIn("mana value 2 or less", self.text("Spellseeker"))
        for must in ("Demonic Tutor", "Pact of Negation", "Tainted Pact", "Finale of Promise", "Brain Freeze"):
            self.assertIn(must, set(seeker) - set(micro))

    def test_t4_thundertrap_trainer_exact(self):
        nn = [n for n in self.lib if not any(t in self.o[n]["type_line"] for t in ("Creature", "Land"))]
        self.assertEqual(len(nn), 58)
        self.assertEqual(round(1 - comb(41, 4) / comb(99, 4), 6), 0.973098)
        self.assertEqual(round(1 - comb(41, 8) / comb(99, 8), 6), 0.999442)
        rec = self.m["T4_thundertrap_trainer"]
        self.assertEqual((rec["P_at_least_one_hit_in_top4"], rec["with_Eminence_copy_top8_disjoint"]), (0.973098, 0.999442))
        self.assertIn("Wizard", self.o["Thundertrap Trainer"]["type_line"])

    def test_t3_combo_delta_dualcaster_only(self):
        c = json.loads(CSB.read_text())
        base = {x["id"] for x in c["baseline"]["included"]}
        self.assertEqual(len(base), 16)
        dual = {x["id"] for x in c["alternatives"][f"{D}_PassC_plus_DualcasterMage_minus_Kefka_20261023.txt"]["included"]}
        self.assertEqual(dual - base, {"147-500", "147-4598"})
        for k, v in c["alternatives"].items():
            if "Dualcaster" not in k:
                self.assertLessEqual({x["id"] for x in v["included"]} - base, set(), k)

    def test_rules_facts_behind_rejections(self):
        self.assertIn("Human Wizard", self.o["Dualcaster Mage"]["type_line"])
        self.assertIn("copy target instant or sorcery spell", self.text("Dualcaster Mage"))
        self.assertIn("two tokens that are copies", self.text("Saw in Half"))
        self.assertIn("then return that card to the battlefield", self.text("Essence Flux"))
        self.assertIn("split second", self.text("Samut, Tyrant of Naktamun"))
        self.assertIn("create a token that's a copy", self.text("Twinflame"))  # tokens: no Eminence (nontoken clause)
        self.assertIn("except during its controller's turn", self.text("Defense Grid"))
        self.assertIn("Wizard", self.o[KEFKA]["type_line"])
        self.assertNotIn("Wizard", self.o["Hexing Squelcher"]["type_line"])
        self.assertEqual(self.o["Hoarding Broodlord"]["cmc"], 8)
        r = RULES.read_text()
        for s in ("603.4", "302.6", "702.61a", "601.2f", "147-500", "147-4598"):
            self.assertIn(s, r)

    def test_banned_and_off_identity_excluded(self):
        for n in ("Dockside Extortionist", "Jeweled Lotus", "Mana Crypt"):
            self.assertNotIn(n, self.lib)
        live = {c["name"]: c for c in json.loads((RC / f"{D}_Scryfall_live_20261023.json").read_text())["cards"]}
        self.assertEqual(live["Dockside Extortionist"]["commander_legality"], "banned")
        self.assertIn("G", live["Culling Ritual"]["color_identity"])
        self.assertEqual(self.o["Inalla, Archmage Ritualist"]["commander_legality"], "legal")
        self.assertIs(self.o["Inalla, Archmage Ritualist"]["game_changer"], False)

    def test_receipt_is_bounded_not_win_rate(self):
        self.assertEqual(self.m["status"], "BOUNDED_FINITE_EXACT_TESTS_NOT_EMPIRICAL_WIN_RATE")
        self.assertIn("No seeded multiplayer game simulation", self.m["what_was_not_run"])
        self.assertIn("OWNER_DECISION", self.m["verdict"]["PASS_C_DUALCASTER_OVER_KEFKA"])


if __name__ == "__main__":
    unittest.main()
