"""Rules-source response-order check against independent conditional scenarios."""
import unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_abaddon_interaction_grid as m

class TestResponseGrid(unittest.TestCase):
    def test_tree_fails_if_removed_after_activation(self):
        self.assertEqual(m.tree(source_removed_before_resolution=True)["life_lost"],0)
        self.assertEqual(m.tree()["life_lost"],27)
        self.assertEqual(m.tree(solphim=True)["life_lost"],27)
    def test_source_removal_distinguishes_heartless(self):
        self.assertEqual(m.heartless(source_removed_before_resolution=True)["total_opponent_life_lost"],54)
        self.assertEqual(m.tree(source_removed_before_resolution=True)["life_lost"],0)
    def test_support_removal_does_not_retain_multiplier(self):
        self.assertEqual(m.heartless(solphim=True)["total_opponent_life_lost"],108)
        self.assertEqual(m.heartless(solphim=True,solphim_removed_before_resolution=True)["total_opponent_life_lost"],54)
        self.assertEqual(m.heartless(bloodletter=True,bloodletter_removed_before_resolution=True)["total_opponent_life_lost"],54)
    def test_prevention_can_invalidate_high_threshold(self):
        d=m.heartless(solphim=True,bloodletter=True,prevent_opponents=(0,1,2))
        self.assertEqual(d["total_opponent_life_lost"],0)
        self.assertEqual(d["pilot_after"],20)
    def test_summoning_sickness_and_hand_cast(self):
        self.assertFalse(m.active_tap_cast(4,4))
        self.assertTrue(m.active_tap_cast(4,5))
        self.assertTrue(m.active_tap_cast(4,4,haste=True))
        self.assertFalse(m.hand_cascade(27,origin="exile"))
        self.assertFalse(m.hand_cascade(27,commander=False))
    def test_no_false_improvement_promotion(self):
        e=m.make()
        self.assertEqual(len(e["examples"]),29)
        self.assertFalse(e["phase_b_complete"])
        self.assertFalse(e["supports_improvement_claim"])
        self.assertFalse(any(e["authority"].values()))

if __name__=="__main__":unittest.main()
