"""Source-paid deterministic Abaddon/Birgi/Ignus access safeguards."""
import unittest
from scripts.grixis_m6_abaddon_ignus_paid_chronology import (
    ABADDON, ASSAULT, BIRGI, BURNS, FAMILIAR, IGNUS, RAKDOS,
    ZERO, MV_AND_COLORS, cast_spells_one_main, finite_recasts,
    one_trial, response_windows, source_cast, variants,
)


class AbaddonPaidIgnusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan, cls.decks = variants()

    def test_frozen_physical_100_singleton_and_exact_swap_identity(self):
        from collections import Counter
        baseline=self.decks["approved"]
        self.assertEqual(set(self.decks),{"approved","ignus_for_rakdos",
             "ignus_for_nightscape_familiar","ignus_for_rite_of_flame",
             "assault_for_rakdos"})
        self.assertEqual(len(baseline),99)
        self.assertEqual(len(set(baseline)),93) # commander is the 94th name
        for q in self.plan["registered_variants"]:
            deck=self.decks[q["id"]]
            self.assertEqual(len(deck),99)
            diff=[(a,b) for a,b in zip(baseline,deck) if a!=b]
            self.assertEqual(len(diff),0 if q["cut"] is None else 1)
            if diff:
                self.assertEqual(diff[0],(q["cut"],q["add"]))
            self.assertEqual(set(n for n,c in Counter(deck).items() if c>1),
                             {"Island","Mountain","Swamp"})

    def test_printed_cascade_mv_unaffected_by_reductions(self):
        self.assertEqual(MV_AND_COLORS[IGNUS],(3,(0,0,1)))
        self.assertEqual(MV_AND_COLORS[ABADDON],(5,(1,1,1)))

    def test_rakdos_requires_a_life_loss_before_cast(self):
        four=[("Swamp",False),("Swamp",False),
              ("Mountain",False),("Mountain",False)]
        self.assertIsNone(source_cast(list(four),ZERO,RAKDOS,opponent_loss=0))
        field=list(four)
        self.assertIsNotNone(source_cast(field,ZERO,RAKDOS,opponent_loss=3))
        self.assertTrue(all(tapped for _,tapped in field))

    def test_nightscape_discount_is_one_not_two_on_multicolored_abaddon(self):
        four=[("Island",False),("Swamp",False),
              ("Mountain",False),("Mountain",False)]
        self.assertIsNone(source_cast(list(four),ZERO,ABADDON))
        field=list(four)
        self.assertIsNotNone(source_cast(field,ZERO,ABADDON,familiar_controlled=True))
        self.assertTrue(all(tapped for _,tapped in field))

    def test_nightscape_cast_is_1B_and_ignus_discount_only_generic(self):
        self.assertEqual(MV_AND_COLORS[FAMILIAR],(2,(0,1,0)))
        a=[("Swamp",False),("Island",False)]
        self.assertIsNotNone(source_cast(a,ZERO,FAMILIAR))
        self.assertIsNone(source_cast([("Mountain",False)],ZERO,IGNUS,
                                       familiar_controlled=True))
        self.assertIsNotNone(source_cast([("Mountain",False),("Island",False)],
                                         ZERO,IGNUS,familiar_controlled=True))

    def test_rakdos_discount_protects_only_generic_pips(self):
        self.assertIsNone(source_cast([("Island",False)],ZERO,IGNUS,
                                       rakdos_controlled=True,opponent_loss=9))
        self.assertIsNotNone(source_cast([("Mountain",False)],ZERO,IGNUS,
                                          rakdos_controlled=True,opponent_loss=9))
        self.assertIsNone(source_cast([("Mountain",False),("Mountain",False),
                                       ("Mountain",False)],ZERO,RAKDOS,opponent_loss=9))

    def test_no_birgi_single_red_allows_only_one_recast(self):
        field={IGNUS,ABADDON}
        n,c,pool=finite_recasts([], (0,0,1,0), field,9,limit=5)
        self.assertEqual((n,c,pool),(1,1,(0,0,0,0)))
        self.assertIn(IGNUS,field)

    def test_birgi_loop_five_recasts_source_paid_from_one_red(self):
        field={IGNUS,ABADDON,BIRGI}
        n,c,pool=finite_recasts([], (0,0,1,0),field,9,limit=5)
        self.assertEqual((n,c,pool),(5,5,(0,0,1,0)))

    def test_birgi_and_familiar_adds_colorless_without_excess_red(self):
        field={IGNUS,ABADDON,BIRGI,FAMILIAR}
        n,c,pool=finite_recasts([], (0,0,1,0),field,9,limit=5)
        self.assertEqual((n,c), (5,5))
        self.assertEqual(pool,(0,0,1,5))

    def test_abaddon_threshold_does_not_go_below_ignus_mana_value(self):
        for loss in (0,1,2):
            _,c,_=finite_recasts([], (0,0,1,0),
                                 {IGNUS,ABADDON,BIRGI},loss,limit=5)
            self.assertEqual(c,0)

    def test_paid_boltwave_builds_9_opp_loss_before_ignus_cast(self):
        # Start with a board legitimately established on previous turns.
        # These are enough physical untapped lands to pay {R} and {2}{R}.
        hand=["Boltwave",IGNUS]
        lands=[("Mountain",False),("Ancient Tomb",False),
               ("Swamp",False),("Mountain",False)]
        board={ABADDON,BIRGI}
        r=cast_spells_one_main(deck=[],hand=hand,lands=lands,pool=ZERO,
                               battlefield=board,policy="engine_first",
                               turn=7,first_cast_turn=None)
        self.assertEqual(r["opponent_loss_precombat_from_burn"],9)
        self.assertEqual(r["ignus_initial_cascade_triggers"],1)
        self.assertEqual(r["ignus_additional_paid_recasts"],5)
        self.assertEqual(r["ignus_additional_cascade_triggers"],5)
        self.assertIn(IGNUS,board)

    def test_absent_birgi_stops_burn_to_ignus_repeat_loop(self):
        hand=["Boltwave",IGNUS]
        lands=[("Mountain",False),("Ancient Tomb",False),
               ("Swamp",False),("Mountain",False)]
        board={ABADDON}
        r=cast_spells_one_main(deck=[],hand=hand,lands=lands,pool=ZERO,
                               battlefield=board,policy="engine_first",
                               turn=7,first_cast_turn=None)
        self.assertEqual(r["opponent_loss_precombat_from_burn"],9)
        self.assertEqual(r["ignus_initial_cascade_triggers"],1)
        self.assertLess(r["ignus_additional_paid_recasts"],5)

    def test_no_opponent_loss_even_abaddon_and_birgi_gives_zero_cascade(self):
        field={IGNUS,ABADDON,BIRGI}
        n,c,pool=finite_recasts([], (0,0,1,0),field,0,limit=5)
        self.assertEqual(n,5)
        self.assertEqual(c,0)

    def test_limited_nonignus_baseline_cannot_produce_ignus_cast(self):
        r,_=one_trial(self.decks["approved"],621017,"engine_first",[4,6,8,10])
        self.assertFalse(r[10]["ignus_initial_paid_cast"])
        self.assertFalse(r[10]["paid_5_repeat_ignus_cascades"])

    def test_real_draw_same_seed_same_paid_results(self):
        r=one_trial(self.decks["ignus_for_rakdos"],621017,"burn_first",[4,6,8,10])
        s=one_trial(self.decks["ignus_for_rakdos"],621017,"burn_first",[4,6,8,10])
        self.assertEqual(r,s)

    def test_response_removal_cascade_already_triggered_survives(self):
        cases=response_windows()
        self.assertTrue(cases["counter_ignus_initial_cast"]["abaddon_cascade_already_granted_if_qualified"])
        self.assertFalse(cases["counter_ignus_initial_cast"]["ignus_resolves_as_permanent"])
        self.assertTrue(cases["remove_abaddon_in_response_to_first_ignus"]["previously_triggered_cascade_kept"])
        self.assertFalse(cases["remove_abaddon_in_response_to_first_ignus"]["future_ignus_casts_gain_abaddon_cascade"])
        self.assertFalse(cases["rule_of_law_resolved"]["repeat_ignus_hand_casts_same_turn_legal"])
        self.assertTrue(cases["drannith_magistrate_resolved"]["casting_cascade_exiled_hit_prohibited"])

    def test_no_unauthorized_status_or_unregistered_policy(self):
        self.assertTrue(self.plan["authority"]["canonical_locked"])
        for name in ("can_change_canonical","can_issue_m6_certificate","can_approve_M7"):
            self.assertFalse(self.plan["authority"][name])
        with self.assertRaises(ValueError):
            one_trial(self.decks["approved"],1,"imagined_free_mana",[4])

if __name__=="__main__":
    unittest.main()
