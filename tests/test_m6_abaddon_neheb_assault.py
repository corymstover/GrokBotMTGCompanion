"""Abaddon Phase B: exact-payability finite rules traces, not matchup statistics."""
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from grixis_m6_abaddon_neheb_assault import AssaultCombatTrace, OutsideFixture, complete_four_piece_example

class NehebAssaultPhaseB(unittest.TestCase):
    def test_four_piece_earliest_phases_and_14_combat_kill_trace(self):
        s=AssaultCombatTrace()
        s.begin_combat()
        s.resolve_top()
        self.assertEqual((s.opponents,s.life_lost),([37,37,37],9))
        s.begin_postcombat_main()
        s.resolve_top()
        self.assertEqual(s.red,9)
        s.activate_assault()
        self.assertEqual(s.red,4)
        s.resolve_top()
        s.begin_combat(extra=True)
        self.assertEqual(s.red,0) # unused mana emptied on phase change
        s.resolve_top()
        self.assertEqual((s.opponents,s.life_lost),([34,34,34],18))
        s.begin_postcombat_main()
        s.resolve_top()
        self.assertEqual(s.red,18)
        full=complete_four_piece_example()
        self.assertTrue(full.over)
        self.assertEqual(full.combats,14)
        self.assertEqual(full.activations,13)
        self.assertEqual(full.opponents,[-2,-2,-2])
        self.assertEqual(full.life_lost,126)

    def test_five_red_floor_allows_extra_combats_but_not_a_win(self):
        s=AssaultCombatTrace(loyal=False,commander=False)
        s.scripted_external_loss([5,0,0])
        s.begin_combat()
        s.begin_postcombat_main()
        s.resolve_top()
        for i in range(3):
            self.assertEqual(s.red,5)
            s.activate_assault()
            s.resolve_top()
            s.begin_combat(extra=True)
            s.begin_postcombat_main()
            s.resolve_top()
        self.assertEqual(s.combats,4)
        self.assertEqual(s.activations,3)
        self.assertEqual(s.life_lost,5)
        self.assertEqual(s.opponents,[35,40,40])
        self.assertFalse(s.over) # extra combats are not themselves damage

    def test_commander_if_condition_checked_at_start_and_resolution(self):
        no_commander=AssaultCombatTrace(commander=False)
        no_commander.begin_combat()
        self.assertEqual(no_commander.stack,[])
        no_commander.begin_postcombat_main()
        no_commander.resolve_top()
        self.assertEqual(no_commander.red,0)

        responded=AssaultCombatTrace()
        responded.begin_combat()
        self.assertEqual(responded.stack,["loyal"])
        responded.remove("commander")
        responded.resolve_top()
        responded.begin_postcombat_main()
        responded.resolve_top()
        self.assertEqual((responded.life_lost,responded.red),(0,0))
        with self.assertRaises(ValueError):responded.activate_assault()

    def test_lieutenant_trigger_survives_subordinate_removal(self):
        s=AssaultCombatTrace()
        s.begin_combat()
        s.remove("loyal")
        s.resolve_top()
        self.assertEqual(s.life_lost,9)
        s.begin_postcombat_main()
        s.resolve_top()
        self.assertEqual(s.red,9)

    def test_neheb_before_and_after_start_of_postcombat(self):
        before=AssaultCombatTrace()
        before.begin_combat()
        before.resolve_top()
        before.remove("neheb")
        before.begin_postcombat_main()
        self.assertEqual(before.stack,[])
        self.assertEqual(before.red,0)
        with self.assertRaises(ValueError):before.activate_assault()

        after=AssaultCombatTrace()
        after.begin_combat()
        after.resolve_top()
        after.begin_postcombat_main()
        self.assertEqual(after.stack,["neheb"])
        after.remove("neheb")
        after.resolve_top()
        self.assertEqual(after.red,9)
        after.activate_assault()
        after.resolve_top()
        after.begin_combat(extra=True)
        after.resolve_top()
        after.begin_postcombat_main()
        self.assertEqual(after.stack,[]) # no Neheb future postcombat trigger
        self.assertEqual(after.red,0)

    def test_assault_activation_resolves_after_enchantment_removed(self):
        s=AssaultCombatTrace()
        s.begin_combat()
        s.resolve_top()
        s.begin_postcombat_main()
        s.resolve_top()
        s.activate_assault()
        s.remove("assault")
        s.resolve_top()
        self.assertEqual(s.pending_extras,1)
        s.begin_combat(extra=True)
        s.resolve_top()
        s.begin_postcombat_main()
        s.resolve_top()
        with self.assertRaises(ValueError):s.activate_assault()

    def test_sorcery_timing_payment_and_pending_stack(self):
        s=AssaultCombatTrace()
        with self.assertRaises(OutsideFixture):
            s.activate_assault() # precombat activation is legal in MTG but OUT of this policy
        s.begin_combat()
        with self.assertRaises(OutsideFixture):s.activate_assault()
        s.resolve_top()
        s.begin_postcombat_main()
        with self.assertRaises(ValueError):s.activate_assault() # Neheb trigger still on stack
        s.resolve_top()
        s.red=4
        with self.assertRaises(ValueError):s.activate_assault()
        s.red=5
        s.activate_assault()
        with self.assertRaises(ValueError):s.activate_assault()
        s.resolve_top()
        with self.assertRaises(ValueError):s.activate_assault() # one per postcombat policy

    def test_damage_fog_does_not_prevent_nondamage_life_loss(self):
        s=AssaultCombatTrace(damage_prevented=True)
        s.begin_combat()
        s.resolve_top()
        self.assertEqual((s.opponents,s.life_lost),([37,37,37],9))

    def test_next_turn_resets_loss_and_red(self):
        s=AssaultCombatTrace()
        s.begin_combat()
        s.resolve_top()
        s.begin_postcombat_main()
        s.resolve_top()
        s.next_turn()
        self.assertEqual((s.life_lost,s.red,s.phase),(0,0,"precombat_main"))
        s.begin_combat()
        s.resolve_top()
        s.begin_postcombat_main()
        s.resolve_top()
        self.assertEqual(s.red,9)

    def test_bounded_authority_and_exact_plan(self):
        import json
        plan=json.loads((ROOT/"data/grixis/m6/phase_b_plans/abaddon_neheb_assault_20261021.json").read_text())
        self.assertEqual(plan["baseline_canonical_sha256"],"2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf")
        self.assertEqual(plan["exact_challenger"],{"add":"Aggravated Assault","cut":"Rakdos, Lord of Riots"})
        self.assertFalse(any(plan["authority"].values()))
        self.assertIn("Measured multiplayer win rates",plan["not_claimed"])
        self.assertEqual(len(plan["deterministic_case_ids"]),9)

if __name__=="__main__":
    unittest.main()
