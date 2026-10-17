"""Adversarial regression scenarios for bounded Abaddon effect-aware evidence."""
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_abaddon_bounded as b


class TestBoundedMechanics(unittest.TestCase):
    def test_oracle_calculations(self):
        v=b.result()
        b.check_result(v)
        self.assertEqual(v["metrics"]["complete_phase_b_candidate_groups"],0)
        self.assertEqual(len(v["covered_swap_ids"]),7)

    def test_tree_activation_protection(self):
        self.assertEqual(b.tree(40,13,active=False)["life_lost"],0)
        self.assertEqual(b.tree(40,13)["life_lost"],27)
        self.assertEqual(b.tree(8,13)["life_after"],13)
        self.assertEqual(b.tree(40,13,bloodletter=True)["life_after"],-14)

    def test_solphim_doubles_only_opponents(self):
        x=b.heartless((40,39),40,solphim=True)
        self.assertEqual([v["damage"] for v in x["opponents"]],[40,38])
        self.assertEqual(x["pilot_damage"],20)

    def test_bloodletter_doubles_life_loss_not_damage(self):
        x=b.heartless((40,),40,bloodletter=True)["opponents"][0]
        self.assertEqual(x["damage"],20)
        self.assertEqual(x["life_lost"],40)

    def test_cascade_hand_only_and_turn_local(self):
        self.assertTrue(b.cascade(5,27))
        self.assertFalse(b.cascade(5,27,origin="exile"))
        self.assertFalse(b.cascade(5,27,origin="graveyard"))
        self.assertFalse(b.cascade(5,27,origin="command"))
        self.assertFalse(b.cascade(5,27,your_turn=False))
        self.assertFalse(b.cascade(5,27,abaddon=False))
        self.assertFalse(b.cascade(5,0))
        self.assertFalse(b.cascade(5,4))
        self.assertTrue(b.cascade(0,0))

    def test_kessig_trigger_not_retroactive(self):
        self.assertEqual(b.kessig(2)["first_spell_threshold_at_cast"],0)
        self.assertEqual(b.kessig(2)["threshold_after_first_trigger"],3)

    def test_shredder_tokens_do_not_attack_trigger_again(self):
        a=b.shredder((True,True,True))
        self.assertEqual(a["attack_triggers"],1)
        self.assertEqual(a["copies"],2)
        self.assertEqual(a["table_life_lost"],69)
        self.assertEqual(b.shredder((False,False,False))["table_life_lost"],0)

    def test_station_does_not_prove_infinite_loop(self):
        self.assertEqual(b.station_loop(90)["completed_cycles"],30)
        self.assertFalse(b.station_loop(90)["repeatable_infinite"])
        self.assertFalse(b.station_loop(90)["winner_proven"])
        self.assertEqual(b.station_loop(2)["completed_cycles"],0)

    def test_approval_and_win_rate_not_reported(self):
        r=b.result()
        self.assertFalse(r["phase_b_complete"])
        self.assertFalse(r["supports_improvement_claim"])
        self.assertTrue(all(not v for v in r["authority"].values()))
        self.assertEqual(r["metrics"]["effect_aware_deckwide_paired_tests"],0)


if __name__=="__main__":
    unittest.main()
