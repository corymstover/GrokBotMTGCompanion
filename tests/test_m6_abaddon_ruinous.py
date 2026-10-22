import unittest
from scripts.grixis_m6_abaddon_ruinous import ExiledCard, OutsideFixture, RuinousAbaddonTrace


class RuinousCascadeFixtureTests(unittest.TestCase):
    def test_opponent_owner_only_loses_life(self):
        s = RuinousAbaddonTrace((40, 39, 38))
        s.upkeep_exile(ExiledCard(owner=1, mana_value=5))
        self.assertEqual(s.play_exiled(), 5)
        self.assertEqual(s.life, [40, 34, 38])
        self.assertEqual(s.opponent_loss_this_turn, 5)

    def test_cast_trigger_on_cast_not_spell_resolution(self):
        s = RuinousAbaddonTrace()
        s.upkeep_exile(ExiledCard(0, 4))
        s.play_exiled()
        self.assertIn(("ruinous_life_loss_trigger_resolves", 0, 4), s.events)
        self.assertNotIn(("spell_resolved", 0, 4), s.events)

    def test_exile_cast_not_granted_cascade_even_after_loss(self):
        s = RuinousAbaddonTrace()
        s.upkeep_exile(ExiledCard(0, 6))
        s.play_exiled()
        self.assertFalse(s.exiled_spell_has_abaddon_cascade())
        self.assertTrue(s.cast_hand_spell(6))
        self.assertFalse(s.cast_hand_spell(7))

    def test_mana_value_zero_no_positive_loss(self):
        s = RuinousAbaddonTrace()
        s.upkeep_exile(ExiledCard(0, 0))
        self.assertEqual(s.play_exiled(), 0)
        self.assertEqual(s.opponent_loss_this_turn, 0)
        self.assertFalse(s.cast_hand_spell(1))

    def test_land_play_not_cast_no_life_loss(self):
        s = RuinousAbaddonTrace()
        s.upkeep_exile(ExiledCard(0, 0, "land"))
        self.assertEqual(s.play_exiled(), 0)
        self.assertEqual(s.opponent_loss_this_turn, 0)
        self.assertEqual(s.events[-1][0], "land_played_not_cast")

    def test_land_play_restriction(self):
        s = RuinousAbaddonTrace()
        s.upkeep_exile(ExiledCard(0, 0, "land"))
        with self.assertRaises(OutsideFixture):
            s.play_exiled(unused_land_play=False)

    def test_sorcery_cannot_cast_during_upkeep(self):
        s = RuinousAbaddonTrace()
        s.upkeep_exile(ExiledCard(0, 5, "sorcery"))
        with self.assertRaises(OutsideFixture):
            s.play_exiled(main_phase=False)
        self.assertEqual(s.opponent_loss_this_turn, 0)

    def test_instant_may_cast_in_upkeep(self):
        s = RuinousAbaddonTrace()
        s.upkeep_exile(ExiledCard(2, 2, "instant"))
        s.play_exiled(main_phase=False)
        self.assertEqual(s.opponent_loss_this_turn, 2)

    def test_mana_not_waived(self):
        s = RuinousAbaddonTrace()
        s.upkeep_exile(ExiledCard(1, 5))
        with self.assertRaises(OutsideFixture):
            s.play_exiled(mana_paid=False)
        self.assertEqual(s.life[1], 40)

    def test_cannot_recast_single_exile_permission(self):
        s = RuinousAbaddonTrace()
        s.upkeep_exile(ExiledCard(1, 2))
        s.play_exiled()
        with self.assertRaises(OutsideFixture):
            s.play_exiled()

    def test_without_commander_no_granted_cascade(self):
        s = RuinousAbaddonTrace(commander=False)
        s.upkeep_exile(ExiledCard(1, 8))
        s.play_exiled()
        self.assertFalse(s.cast_hand_spell(5))

    def test_next_turn_resets_opponent_loss(self):
        s = RuinousAbaddonTrace()
        s.upkeep_exile(ExiledCard(1, 7))
        s.play_exiled()
        self.assertTrue(s.cast_hand_spell(7))
        s.next_turn()
        self.assertFalse(s.cast_hand_spell(7))

    def test_owner_invalid_rejected(self):
        s = RuinousAbaddonTrace()
        with self.assertRaises(OutsideFixture):
            s.upkeep_exile(ExiledCard(3, 4))

    def test_permission_only_after_exiling(self):
        s = RuinousAbaddonTrace()
        with self.assertRaises(OutsideFixture):
            s.play_exiled()


if __name__ == "__main__":
    unittest.main()
