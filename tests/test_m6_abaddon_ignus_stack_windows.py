"""Official-Oracle Ignus mana ability and 8 physical, conditional stack windows."""
from collections import Counter
import unittest
from scripts.grixis_m6_abaddon_ignus_stack_windows import (
    IGNUS,BIRGI,ABADDON,FIRST_HIT,SEED,
    verify_study,fixture,legal_hand_ignus_and_first_cascade,
    one_window,run,
)
from scripts.grixis_m6_abaddon_ignus_shared_effects import (
    assert_conserved,expected_physical,first_cascade,recast_ignus
)

class IgnusTrueManaAbilityWindows(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan,cls.prior,cls.cards,cls.library=verify_study()
        cls.receipt=run()
        cls.cases=cls.receipt["cases"]

    def test_frozen_single_slot_challenger_100(self):
        self.assertEqual(len(self.library),99)
        self.assertEqual(len(set(self.library)),93)
        self.assertEqual(self.library.count(IGNUS),1)
        self.assertEqual(self.library.count("Island"),3)
        self.assertEqual(self.plan["baseline"]["canonical_raw_sha256"],
            "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf")

    def test_all_eight_preregistered_and_physically_conserved(self):
        self.assertEqual(len(self.cases),8)
        self.assertEqual(set(self.cases),set(x["id"] for x in self.plan["registered_states"]))
        for name,case in self.cases.items():
            with self.subTest(name=name):
                self.assertTrue(case["physical_zone_conservation"])
                self.assertTrue(case["prearranged_board_not_observed_access"])
                self.assertTrue(case["fixture_from_frozen_physical_99"])

    def test_mana_ability_has_no_stack_or_priority_response(self):
        c=self.cases["ignus_entered_quiet_board"]
        self.assertFalse(c["mana_ability_uses_stack"])
        self.assertFalse(c["ordinary_removal_can_respond_to_activation"])
        self.assertTrue(c["active_player_can_activate_before_opponent_priority"])
        self.assertEqual(c["additional_recasts"],5)
        self.assertEqual(c["final_ignus_zone"],"battlefield")

    def test_uncontested_birgi_abaddon_give_five_recasts_and_cascade(self):
        c=self.cases["uncontested"]
        self.assertEqual(c["additional_recasts"],5)
        self.assertEqual(c["additional_ignus_cascades"],5)
        self.assertEqual(c["actual_exiled_cascade_triggers"],5)

    def test_rule_of_law_after_boltwave_blocks_original_ignus(self):
        c=self.cases["rule_of_law_boltwave_was_cast"]
        self.assertFalse(c["initial_hand_cast"])
        self.assertFalse(c["trigger"])
        self.assertEqual(c["actual_exiled_cascade_triggers"],0)
        self.assertEqual(c["final_ignus_zone"],"hand")

    def test_rule_of_law_allows_first_ignus_but_not_free_cast_or_recast(self):
        c=self.cases["rule_of_law_first_ignus"]
        self.assertTrue(c["initial_hand_cast"])
        self.assertTrue(c["trigger"])
        self.assertFalse(c["cascade_free_cast"])
        self.assertEqual(c["first_hit"],FIRST_HIT)
        self.assertEqual(c["actual_exiled_cascade_triggers"],1)
        self.assertEqual(c["additional_recasts"],0)
        self.assertEqual(c["final_ignus_zone"],"battlefield")

    def test_drannith_prohibits_exile_hit_but_not_hand_recasts(self):
        c=self.cases["drannith"]
        self.assertTrue(c["initial_hand_cast"])
        self.assertTrue(c["trigger"])
        self.assertFalse(c["cascade_free_cast"])
        self.assertEqual(c["first_hit"],FIRST_HIT)
        self.assertEqual(c["additional_recasts"],5)
        self.assertEqual(c["actual_exiled_cascade_triggers"],6)
        self.assertEqual(c["cumulative_actual_supported_hit_effects"],0)

    def test_remove_abaddon_before_next_hand_cast_no_cascade(self):
        c=self.cases["abaddon_removed_before_next_ignus"]
        self.assertEqual(c["additional_recasts"],5)
        self.assertEqual(c["additional_ignus_cascades"],0)
        self.assertEqual(c["actual_exiled_cascade_triggers"],0)

    def test_remove_birgi_before_next_cast_no_repeat_red(self):
        c=self.cases["birgi_removed_before_next_ignus"]
        self.assertEqual(c["additional_recasts"],1)
        self.assertEqual(c["additional_ignus_cascades"],1)
        self.assertEqual(c["actual_exiled_cascade_triggers"],1)

    def test_counter_original_ignus_keeps_trigger_but_no_bounce(self):
        c=self.cases["ignus_countered_after_cast"]
        self.assertTrue(c["initial_hand_cast"])
        self.assertTrue(c["trigger"])
        self.assertTrue(c["cascade_free_cast"])
        self.assertEqual(c["first_hit"],FIRST_HIT)
        self.assertTrue(c["original_ignus_in_graveyard"])
        self.assertFalse(c["original_ignus_on_battlefield"])
        self.assertEqual(c["additional_recasts"],0)
        self.assertEqual(c["actual_exiled_cascade_triggers"],1)

    def test_direct_first_hit_under_rule_of_law_bottoms_real_card(self):
        state=fixture(self.library)
        src=expected_physical(self.library)
        receipt=first_cascade(state,self.cards,17,self.prior,rule_of_law=True)
        self.assertEqual(receipt["hit"],FIRST_HIT)
        self.assertFalse(receipt["cast_from_exile"])
        self.assertEqual(receipt["reason"],"spell_limit")
        self.assertNotIn(FIRST_HIT,state["field"])
        assert_conserved(state,src)

    def test_direct_first_hit_under_drannith_bottoms_real_card(self):
        state=fixture(self.library)
        src=expected_physical(self.library)
        receipt=first_cascade(state,self.cards,17,self.prior,drannith=True)
        self.assertEqual(receipt["hit"],FIRST_HIT)
        self.assertFalse(receipt["cast_from_exile"])
        self.assertEqual(receipt["reason"],"nonhand_spell_prohibited")
        assert_conserved(state,src)

    def test_no_hate_first_hit_retains_exact_predecessor_behavior(self):
        a=fixture(self.library);b=fixture(self.library)
        self.assertEqual(first_cascade(a,self.cards,17,self.prior),
                         first_cascade(b,self.cards,17,self.prior,
                            rule_of_law=False,drannith=False))
        self.assertEqual(a["field"],b["field"])
        self.assertEqual(a["graveyard"],b["graveyard"])
        self.assertEqual(a["deck"],b["deck"])

    def test_external_hate_does_not_invent_opponent_cards_in_our_library(self):
        p=self.plan["model_scope"]
        self.assertTrue(p["physical_99_zones_verified"])
        self.assertTrue(p["prearranged_board_fixture_not_physical_draw_probability"])
        self.assertFalse(p["real_external_opponent_spells_cast_or_drawn"])
        self.assertFalse(p["real_opponent_play_probability"])
        self.assertFalse(p["full_99_card_effects"])
        self.assertFalse(p["swap_superiority_proved"])
        self.assertFalse(p["canonical_changed"])
        self.assertIsNone(p["game_win_rate"])
        self.assertEqual(p["m6_certificates"],0)
        self.assertEqual(p["m7_owner_approvals"],0)

    def test_paid_cast_does_not_need_free_spell_as_a_prerequisite(self):
        s=fixture(self.library)
        r=legal_hand_ignus_and_first_cascade(s,self.cards,self.prior,
                       drannith=True)
        self.assertTrue(r["initial_hand_cast"])
        self.assertTrue(r["trigger"])
        self.assertFalse(r["cascade_free_cast"])
        assert_conserved(s,expected_physical(self.library))

if __name__=="__main__":
    unittest.main()
