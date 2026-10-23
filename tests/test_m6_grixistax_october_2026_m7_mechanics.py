"""Deck 27 Grixistax___October_2026 (Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools) M7: finite
Oracle-anchored checks and bounded Pass C tests.

Recomputes, from the frozen Oracle snapshot and the vendored baseline, the exact hypergeometric Force-pitch table in the
bounded measured-tests receipt, checks the seeded Monte Carlo rows (Pass C Talisman of Indulgence / Arcane Signet /
Overburden mana cells, token-engine and Opposition / Static Orb deployability) are internally consistent and pinned, and
pins the rules facts the two-swap research conclusion depends on. These are not win rates; nothing here is approval.
"""
import json
import re
import unittest
from collections import Counter
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = "Grixistax___October_2026"
KRAUM = "Kraum, Ludevic's Opus"
TEVESH = "Tevesh Szat, Doom of Fools"
RC = ROOT / "data/grixis/m7/research_challengers"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
MEAS = RC / f"{D}_bounded_measured_tests_20261023.json"
CSB = RC / f"{D}_CommanderSpellbook_20261023.json"
RULES = ROOT / f"data/grixis/m6/rules_snapshots/{D}_M7_20261023.md"
TURNS = [(t, 6 + t) for t in range(1, 7)]
LOCKS = ("no lock", "Contamination", "Blood Moon", "Back to Basics", "Artifact hate")


def library(path):
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"(\d+)x (.+?)( \[Commander\])?$", line.strip())
        if m and not m.group(3):
            out += [m.group(2)] * int(m.group(1))
    return out


def p_ge(k, n, N):
    return 1 - comb(N - k, n) / comb(N, n)


class GrixistaxMechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.m = json.loads(MEAS.read_text())
        cls.base, cls.cand = library(BASE), library(CAND)

    def text(self, n):
        return self.o[n]["oracle_text"]

    def ftype(self, n):
        return self.o[n]["type_line"].split(" // ")[0]

    def test_partner_commanders_oracle(self):
        self.assertIn("Whenever an opponent casts their second spell each turn, draw a card.", self.text(KRAUM))
        self.assertIn("Flying, haste", self.text(KRAUM))
        self.assertEqual(self.o[KRAUM]["mana_cost"], "{3}{U}{R}")
        t = self.text(TEVESH)
        self.assertIn("+2: Create two 0/1 black Thrull creature tokens.", t)
        self.assertIn("+1: You may sacrifice another creature or planeswalker. If you do, draw two cards, then draw "
                      "another card if the sacrificed permanent was a commander.", t)
        self.assertIn("can be your commander.", t)
        self.assertEqual(self.o[TEVESH]["mana_cost"], "{4}{B}")
        self.assertIn("Legendary Planeswalker", self.o[TEVESH]["type_line"])
        for n in (KRAUM, TEVESH):
            self.assertIn("Partner", self.text(n))
            self.assertEqual(self.o[n]["commander_legality"], "legal")
            self.assertIs(self.o[n]["game_changer"], False)

    def test_libraries_98_26_lands_and_exactly_two_swaps(self):
        for lib in (self.base, self.cand):
            self.assertEqual(len(lib), 98)
            self.assertEqual(sum(1 for n in lib if "Land" in self.ftype(n)), 26)
        self.assertEqual(sorted((Counter(self.cand) - Counter(self.base)).elements()), ["Arcane Signet", "Bitterblossom"])
        self.assertEqual(sorted((Counter(self.base) - Counter(self.cand)).elements()), ["Mox Amber", "Windfall"])
        counts = {k: sum(1 for n in self.cand if k in self.ftype(n) and "Land" not in self.ftype(n))
                  for k in ("Creature", "Planeswalker", "Artifact", "Enchantment", "Instant", "Sorcery")}
        self.assertEqual(counts, {"Creature": 7, "Planeswalker": 3, "Artifact": 22, "Enchantment": 10,
                                  "Instant": 22, "Sorcery": 8})

    def test_swap_cards_oracle_and_karn_does_not_enable_amber(self):
        self.assertEqual(self.text("Arcane Signet"), "{T}: Add one mana of any color in your commander's color identity.")
        self.assertEqual(self.o["Arcane Signet"]["mana_cost"], "{2}")
        self.assertEqual(self.text("Mox Amber"),
                         "{T}: Add one mana of any color among legendary creatures and planeswalkers you control.")
        self.assertIn("you lose 1 life and create a 1/1 black Faerie Rogue creature token with flying", self.text("Bitterblossom"))
        self.assertEqual(self.o["Bitterblossom"]["mana_cost"], "{1}{B}")
        self.assertIn("Each player discards their hand, then draws cards", self.text("Windfall"))
        self.assertEqual(self.o["Karn, the Great Creator"]["color_identity"], [])
        legends = [n for n in self.base if "Legendary" in self.o[n]["type_line"]
                   and ("Creature" in self.ftype(n) or "Planeswalker" in self.ftype(n))]
        coloured = [n for n in legends if self.o[n]["color_identity"]]
        self.assertNotIn("Karn, the Great Creator", coloured)
        for n in ("Arcane Signet", "Bitterblossom", "Mox Amber", "Windfall"):
            self.assertIs(self.o[n]["game_changer"], False, n)
        self.assertNotIn("Talisman of Indulgence", self.cand)
        self.assertNotIn("U", self.text("Talisman of Indulgence").split("Add {C}.")[1])

    def test_force_pitch_exact_hypergeometric(self):
        rec = self.m["force_pitch"]
        self.assertIn("Exact hypergeometric", rec["method"])
        self.assertEqual(rec["blue_nonland_cards_in_98"], {"baseline": 22, "candidate": 21})
        names = rec["blue_card_names"]
        self.assertEqual(sorted(set(names["baseline"]) - set(names["candidate"])), ["Windfall"])
        for k, lib in (("baseline", self.base), ("candidate", self.cand)):
            for n in names[k]:
                self.assertIn(n, lib)
                self.assertTrue("U" in (self.o[n]["mana_cost"] or "") or n == "Pact of Negation", n)
            for t, n in TURNS:
                self.assertEqual(rec["P_other_blue_card_available_to_pitch_given_Force_in_hand"][k][f"turn {t} (n={n})"],
                                 round(p_ge(len(names[k]) - 1, n - 1, 98), 4), (k, t))
        tab = rec["P_other_blue_card_available_to_pitch_given_Force_in_hand"]
        self.assertEqual((tab["baseline"]["turn 1 (n=7)"], tab["candidate"]["turn 1 (n=7)"]), (0.7748, 0.756))
        self.assertIn("If it's not your turn", self.text("Force of Negation"))

    def test_pass_c_mana_cells_consistent_and_pinned(self):
        r = self.m["mana"]["results"]
        self.assertEqual((self.m["mana"]["seed"], self.m["mana"]["games_per_cell"]), (27, 40000))
        for cfg in r:
            for lock in LOCKS:
                prev = -1
                for t in range(1, 5):
                    c = r[cfg][lock][f"turn {t}"]
                    self.assertGreaterEqual(c["mean_mana_sources_after_deploy"], prev)
                    prev = c["mean_mana_sources_after_deploy"]
                    self.assertLessEqual(c["P_UU_available"], c["P_U_available"])
        b, s, tal, ob = (r[k] for k in ("baseline", "plus_Arcane_Signet_minus_Mox_Amber",
                                        "plus_Talisman_of_Indulgence_minus_Mox_Amber",
                                        "plus_Arcane_Signet_minus_Overburden_keep_Amber"))
        self.assertEqual((b["no lock"]["turn 4"]["mean_mana_sources_after_deploy"],
                          s["no lock"]["turn 4"]["mean_mana_sources_after_deploy"]), (3.138, 3.193))
        self.assertEqual((b["no lock"]["turn 4"]["P_five_mana_with_B_for_Tevesh"],
                          s["no lock"]["turn 4"]["P_five_mana_with_B_for_Tevesh"]), (0.1526, 0.1657))
        self.assertEqual((b["Contamination"]["turn 4"]["P_U_available"], s["Contamination"]["turn 4"]["P_U_available"]),
                         (0.2788, 0.3299))
        self.assertEqual([b["no lock"][f"turn {t}"]["P_Mox_Amber_live_given_deployed"] for t in range(1, 5)][3], 0.2743)
        for lock in LOCKS:
            for t in range(1, 5):
                sc, tc = s[lock][f"turn {t}"], tal[lock][f"turn {t}"]
                self.assertEqual(sc["mean_mana_sources_after_deploy"], tc["mean_mana_sources_after_deploy"])
                self.assertGreaterEqual(sc["P_U_available"], tc["P_U_available"])
        self.assertGreater(s["Contamination"]["turn 4"]["P_U_available"], tal["Contamination"]["turn 4"]["P_U_available"])
        self.assertEqual(ob["no lock"]["turn 4"]["mean_mana_sources_after_deploy"], 3.225)
        self.assertIn("Seeded finite Monte Carlo goldfish", self.m["mana"]["method"])

    def test_token_engine_and_opposition_rows_consistent(self):
        tk = self.m["tokens"]
        seen = tk["P_specific_card_seen_by_turn"]
        for t in range(1, 5):
            self.assertEqual(seen[f"turn {t}"], round((6 + t) / 98, 4))
        for key in ("candidate", "staged_Opposition_alt"):
            for lock, rows in tk[key].items():
                for t in range(1, 5):
                    c = rows[f"turn {t}"]
                    self.assertLessEqual(c["P_token_engine_online_Tevesh_only"], c["P_token_engine_online_Tevesh_or_Bitterblossom"])
                    self.assertLessEqual(c["P_Opposition_seen_and_castable"], seen[f"turn {t}"] + 0.005)
        self.assertEqual(tk["candidate"]["no lock"]["turn 4"]["P_token_engine_online_Tevesh_or_Bitterblossom"], 0.2309)
        self.assertEqual(tk["baseline_P_token_engine_online_Tevesh_only"]["no lock"]["turn 4"], 0.1532)
        self.assertEqual(tk["candidate"]["Contamination"]["turn 4"]["P_token_engine_online_Tevesh_or_Bitterblossom"], 0.2019)
        self.assertEqual(tk["staged_Opposition_alt"]["no lock"]["turn 4"]["P_Opposition_seen_and_castable"], 0.0329)
        self.assertEqual(tk["staged_Opposition_alt"]["Contamination"]["turn 4"]["P_Opposition_seen_and_castable"], 0.0034)
        self.assertEqual(tk["baseline_P_Static_Orb_seen_and_castable"]["no lock"]["turn 4"], 0.0599)
        self.assertEqual(tk["baseline_P_Static_Orb_seen_and_castable"]["Contamination"]["turn 4"], 0.0584)
        self.assertGreater(tk["baseline_P_Static_Orb_seen_and_castable"]["Contamination"]["turn 4"],
                           tk["staged_Opposition_alt"]["Contamination"]["turn 4"]["P_Opposition_seen_and_castable"])

    def test_commander_spellbook_six_unchanged(self):
        c = json.loads(CSB.read_text())
        base = {x["id"] for x in c["baseline"]["included"]}
        self.assertEqual(base, {"1368-1414-4856", "1368-3518-4856", "1368-1878-2706", "1368-2706-3518",
                                "2581-5065", "2163-5065"})
        self.assertEqual({x["id"] for x in c["candidate"]["included"]}, base)
        for k, v in c["alternatives"].items():
            self.assertEqual({x["id"] for x in v["included"]}, base, k)

    def test_rules_snapshot_anchors(self):
        r = RULES.read_text()
        for s in ("702.124b", "702.124c", "903.8", "603.3b", "305.7", "502.3", "2024-04-12", "commander: legal",
                  "the \" // \" there only joins the pair", "no project exception applies to this deck",
                  "Not a {T} cost", "anti-synergistic"):
            self.assertIn(s, r)
        self.assertIn("Creatures entering don't cause abilities to trigger.", self.text("Torpor Orb"))
        self.assertIn("Whenever a player puts a nontoken creature onto the battlefield", self.text("Overburden"))
        self.assertIn("If a land is tapped for mana, it produces {B} instead of any other type and amount.",
                      self.text("Contamination"))
        self.assertIn("Tap an untapped creature you control: Tap target artifact, creature, or land.", self.text("Opposition"))

    def test_off_identity_excluded(self):
        live = {c["name"]: c for c in json.loads((RC / f"{D}_Scryfall_live_20261023.json").read_text())["cards"]}
        for n in ("Archon of Emeria", "Silence", "Orim's Chant", "Ethersworn Canonist"):
            self.assertIn("W", live[n]["color_identity"], n)
            self.assertNotIn(n, self.cand)

    def test_receipt_is_bounded_not_win_rate(self):
        self.assertIn("not a game simulation or win rate", self.m["purpose"])
        self.assertIn("no opponent model", self.m["scripts"]["mana"])


if __name__ == "__main__":
    unittest.main()
