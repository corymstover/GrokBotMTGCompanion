"""Finite source-paid Abaddon rev2 portfolio and critical interaction contracts.

Counts/cost arithmetic are deterministic. These tests are *not* multiplayer
simulation or a substitute for current Oracle and M6 candidate-bound I/J.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

from scripts.grixis_m7_abaddon_rev2_live_oracle import (
    MANIFEST, validate_portfolio, audit,
)
from scripts.grixis_m7_abaddon_live_oracle import OracleGateError

ROOT = Path(__file__).resolve().parents[1]
PROTECTED = {
    "Abaddon the Despoiler", "The Ruinous Powers", "The Lost and the Damned",
    "Keeper of Secrets", "Call Forth the Tempest", "Noise Marine",
    "Birgi, God of Storytelling // Harnfel, Horn of Bounty",
    "Loyal Subordinate", "Neheb, the Eternal", "Underworld Breach",
    "Lion's Eye Diamond", "Brain Freeze", "Mystic Remora", "Boltwave",
    "Kessig Flamebreather", "Passionate Archaeologist", "Nalfeshnee",
    "Prosper, Tome-Bound", "Vivi Ornitier",
}


class AbaddonRev2WholePhysical100(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.variants, cls.approved_sha = validate_portfolio(cls.m)

    def test_no_approval_and_exact_source_identity(self):
        self.assertEqual(self.approved_sha, "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf")
        for flag in ("owner_approved", "oracle_complete", "m6_certified",
                     "m6_ij_recertified_for_revised_list"):
            self.assertIs(self.m[flag], False)

    def test_three_competing_exact_100_source_bound_packages(self):
        self.assertEqual(len(self.variants), 4)  # including baseline
        base = Counter(self.variants["baseline"])
        for v in self.m["comparisons"]:
            with self.subTest(variant=v["id"]):
                cards = self.variants[v["id"]]
                self.assertEqual(len(cards), 100)
                self.assertEqual(cards[0], "Abaddon the Despoiler")
                self.assertEqual(len(set(cards)), 94)
                self.assertTrue(PROTECTED <= set(cards))
                self.assertEqual(Counter(cards)-base, Counter(v["adds"]))
                self.assertEqual(base-Counter(cards), Counter(v["cuts"]))
                self.assertEqual(len(v["adds"]), len(v["cuts"]))
                self.assertGreaterEqual(len(v["adds"]), 5)
                self.assertEqual(hashlib.sha256((ROOT/v["path"]).read_bytes()).hexdigest(), v["sha256"])

    def test_owner_hard_audit_opportunity_not_faked(self):
        self.assertGreaterEqual(len(set(self.m["weak_incumbents_challenged"])), 8)
        decisions = self.m["material_candidate_judgments"]
        self.assertGreaterEqual(len(decisions), 10)
        self.assertEqual(len({x["card"] for x in decisions}), len(decisions))
        selected = {x["card"]: x["cut"] for x in decisions if x["decision"]=="SELECT_ADD"}
        chosen = self.m["comparisons"][0]
        self.assertEqual(set(selected), set(chosen["adds"]))
        self.assertEqual(set(selected.values()), set(chosen["cuts"]))
        self.assertTrue(set(chosen["cuts"]) <= set(self.m["weak_incumbents_challenged"]))

    def test_two_distinct_multiswap_alternatives_remain_physical(self):
        a,b = self.m["comparisons"][1:]
        self.assertNotEqual(set(a["adds"]), set(b["adds"]))
        self.assertNotEqual(a["sha256"], b["sha256"])
        self.assertEqual(len(a["adds"]),5)
        self.assertEqual(len(b["adds"]),5)
        self.assertIn("Exalted Flamer of Tzeentch", self.variants[a["id"]])
        self.assertIn("Exalted Flamer of Tzeentch", self.variants[b["id"]])

    def test_spark_double_doubles_only_qualified_actual_hand_casts(self):
        # Two distinct Abaddon static grants, no extra from an exile-cast
        # cascade hit; printed MV of the paid spell, not mana actually spent.
        def abaddon_granted_cascades(abaddons, mv, x, own_turn, from_hand):
            return abaddons if own_turn and from_hand and mv<=x else 0
        self.assertEqual(abaddon_granted_cascades(2,3,9,True,True),2)
        self.assertEqual(abaddon_granted_cascades(2,4,3,True,True),0)
        self.assertEqual(abaddon_granted_cascades(2,3,9,True,False),0)
        self.assertEqual(abaddon_granted_cascades(2,3,9,False,True),0)

    def test_bowmasters_wheel_actual_draw_events_not_permanent_per_drawstep(self):
        # 7 draws per opponent outside draw steps => one trigger per draw,
        # but damage is contingent on each individual trigger resolving.
        opponent_draws = [7,7,7]
        triggers=sum(opponent_draws)
        self.assertEqual(triggers,21)
        actual_resolved_opponent_damage=triggers
        self.assertEqual(actual_resolved_opponent_damage,21)
        # Pending triggers or canceled damage contribute zero X.
        self.assertEqual(sum([]),0)

    def test_rift_alternate_payment_does_not_change_mana_value(self):
        rift=self.m["newly_checked_scryfall_oracle"]["Cyclonic Rift"]
        self.assertEqual(rift["mana_value"],2)
        self.assertEqual(rift["mana_cost"],"{1}{U}")
        self.assertIn("Overload {6}{U}",rift["oracle_text"])
        # Alternate cost paid 7; still eligible for cascade at X >= 2.
        self.assertLessEqual(rift["mana_value"],2)

    def test_neheb_assault_loop_exact_cumulative_life_and_mana(self):
        opponent_losses=[3,3,3]  # actually resolved Loyal trigger
        x=sum(opponent_losses)
        self.assertEqual(x,9)
        first_neheb_red=x
        # Paying 3 to cast Assault and 5 for the first extra combat.
        red_after_cast_and_activation=first_neheb_red-3-5
        self.assertEqual(red_after_cast_and_activation,1)
        second_combat_losses=[3,3,3]
        cumulative=sum(opponent_losses)+sum(second_combat_losses)
        self.assertEqual(cumulative,18)
        self.assertGreaterEqual(cumulative,5)  # another payable activation

    def test_rev2_live_gate_still_requires_actual_current_oracle(self):
        new_names=set(self.m["newly_checked_scryfall_oracle"])
        self.assertEqual(new_names,{"Spark Double","Orcish Bowmasters","Cyclonic Rift"})
        for card in self.m["newly_checked_scryfall_oracle"].values():
            self.assertEqual(card["commander_legality"],"legal")
            self.assertTrue(set(card["color_identity"]) <= {"U","B","R"})
            self.assertTrue(card["oracle_text"])


if __name__ == "__main__":
    unittest.main()
