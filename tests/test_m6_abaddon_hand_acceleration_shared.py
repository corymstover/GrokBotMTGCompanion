"""Frozen six actual hand mana acceleration policies added to physical Abaddon pilot."""
from collections import Counter
import unittest

from scripts.grixis_m6_abaddon_hand_acceleration_shared import (
    ABADDON,BIRGI,ACTIVATIONS,ZERO,verify,paid_accelerants_from_hand,
    start_turn,one_trial,expected_physical
)
from scripts.grixis_m6_abaddon_ignus_shared_effects import (
    main_phase,physical_zones,one_trial as predecessor_trial
)


def state(*,hand=(),lands=(),field=(),pool=ZERO,graveyard=()):
    return {"deck":[],"hand":list(hand),"field":set(field),"lands":list(lands),
        "graveyard":list(graveyard),"pool":pool,"loss":0,
        "pilot_life_damage":0,"rocks_tapped":False,
        "mana_vault_exhausted":False,"metrics":Counter(),"examples":[]}


class AbaddonHandAccelerantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan,cls.predecessor,cls.graph,cls.variants=verify()

    def test_source_scope_and_100_card_physical_variants(self):
        self.assertEqual(len(ACTIVATIONS),6)
        self.assertEqual(len(self.variants),5)
        for lib in self.variants.values():
            self.assertEqual(len(lib),99)
            self.assertEqual(len(set(lib)),93)
            self.assertEqual(Counter(lib)["Mountain"],3)
            self.assertEqual(Counter(lib)["Island"],3)
            self.assertEqual(Counter(lib)["Swamp"],3)
        self.assertEqual(self.plan["authority"]["canonical_approved_sha256"],
                         "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf")

    def test_no_held_accelerants_means_no_new_mana(self):
        s=state(hand=("Demonic Tutor",),lands=(("Mountain",False),))
        paid_accelerants_from_hand(s,self.plan)
        self.assertEqual(s["pool"],ZERO)
        self.assertEqual(s["hand"],["Demonic Tutor"])
        self.assertEqual(s["lands"],[("Mountain",False)])

    def test_lotus_petal_0_into_ring_1_exact_generic_and_mana_color(self):
        s=state(hand=("Lotus Petal","Sol Ring"))
        original=Counter(s["hand"])
        paid_accelerants_from_hand(s,self.plan)
        self.assertEqual(s["pool"],(0,0,0,2))
        self.assertEqual(s["metrics"]["hand_cast_Lotus Petal"],1)
        self.assertEqual(s["metrics"]["hand_cast_Sol Ring"],1)
        self.assertIn("Sol Ring",s["field"])
        self.assertEqual(s["graveyard"],["Lotus Petal"])
        self.assertEqual(physical_zones(s),original)

    def test_no_mana_generated_before_sol_ring_paid(self):
        s=state(hand=("Sol Ring",))
        paid_accelerants_from_hand(s,self.plan)
        self.assertEqual(s["pool"],ZERO)
        self.assertIn("Sol Ring",s["hand"])
        self.assertFalse(s["metrics"]["hand_cast_Sol Ring"])

    def test_mana_vault_source_paid_1_and_taps_to_3_c_once(self):
        s=state(hand=("Mana Vault",),lands=(("Mountain",False),))
        original=physical_zones(s)
        paid_accelerants_from_hand(s,self.plan)
        self.assertEqual(s["pool"],(0,0,0,3))
        self.assertTrue(s["mana_vault_exhausted"])
        self.assertIn("Mana Vault",s["field"])
        self.assertEqual(physical_zones(s),original)

    def test_mana_vault_does_not_untap_and_loses_life_each_draw_step(self):
        s=state(field=("Mana Vault","Sol Ring"),lands=(("Swamp",True),))
        s["mana_vault_exhausted"]=True
        start_turn(s)
        self.assertEqual(s["pool"],(0,0,0,2))
        self.assertEqual(s["pilot_life_damage"],1)
        self.assertTrue(s["mana_vault_exhausted"])
        start_turn(s)
        self.assertEqual(s["pool"],(0,0,0,2))
        self.assertEqual(s["pilot_life_damage"],2)
        self.assertEqual(s["metrics"]["mana_vault_draw_damage"],2)
        self.assertFalse(s["lands"][0][1])

    def test_dark_ritual_paid_black_creates_three_black(self):
        s=state(hand=("Dark Ritual",),lands=(("Swamp",False),))
        original=physical_zones(s)
        paid_accelerants_from_hand(s,self.plan)
        self.assertEqual(s["pool"],(0,3,0,0))
        self.assertEqual(s["graveyard"],["Dark Ritual"])
        self.assertEqual(physical_zones(s),original)

    def test_cabal_ritual_unthresholded_exact_1B_into_BBB(self):
        s=state(hand=("Cabal Ritual",),
                lands=(("Swamp",False),("Island",False)))
        paid_accelerants_from_hand(s,self.plan)
        self.assertEqual(s["pool"],(0,3,0,0))
        self.assertEqual(s["metrics"]["cabal_threshold_paid"],0)
        self.assertEqual(s["graveyard"],["Cabal Ritual"])

    def test_cabal_threshold_counts_graveyard_at_resolution_only(self):
        prior=["Island","Swamp","Mountain","Flooded Strand","Misty Rainforest",
               "Polluted Delta","Lotus Petal"]
        s=state(hand=("Cabal Ritual",),
                graveyard=prior,lands=(("Swamp",False),("Island",False)))
        original=physical_zones(s)
        paid_accelerants_from_hand(s,self.plan)
        self.assertEqual(s["pool"],(0,5,0,0))
        self.assertEqual(s["metrics"]["cabal_threshold_paid"],1)
        self.assertEqual(len(s["graveyard"]),8)
        self.assertEqual(physical_zones(s),original)

    def test_rite_only_two_red_and_into_grave(self):
        s=state(hand=("Rite of Flame",),lands=(("Mountain",False),))
        paid_accelerants_from_hand(s,self.plan)
        self.assertEqual(s["pool"],(0,0,2,0))
        self.assertEqual(s["graveyard"],["Rite of Flame"])

    def test_birgi_mana_on_cast_of_hand_ritual_not_cast_birgi_itself(self):
        s=state(hand=("Rite of Flame",),lands=(("Mountain",False),),
                field=(BIRGI,))
        paid_accelerants_from_hand(s,self.plan)
        self.assertEqual(s["pool"],(0,0,3,0))
        self.assertEqual(s["metrics"]["birgi_red_from_hand_accelerant"],1)

    def test_cast_sol_ring_enables_actual_5_mana_commander_from_colored_lands(self):
        s=state(hand=("Sol Ring",),
          lands=(("Mountain",False),("Island",False),
                 ("Swamp",False),("Mountain",False)))
        no_ramp=state(hand=(),
          lands=(("Mountain",False),("Island",False),
                 ("Swamp",False),("Mountain",False)))
        main_phase(no_ramp,self.graph,self.predecessor,21,5,"engine_first")
        self.assertNotIn(ABADDON,no_ramp["field"])
        paid_accelerants_from_hand(s,self.plan)
        main_phase(s,self.graph,self.predecessor,21,5,"engine_first")
        self.assertIn(ABADDON,s["field"])
        self.assertIn("Sol Ring",s["field"])
        self.assertEqual(s["metrics"]["hand_cast_Sol Ring"],1)

    def test_no_mode_exactly_reproduces_parent_ignus_source_access(self):
        lib=self.variants["ignus_for_rakdos"]
        for seed,policy in ((621017,"engine_first"),(725746,"burn_first")):
            prior,prior_state=predecessor_trial(lib,seed,policy,
                self.predecessor,self.graph)
            rows,field=one_trial(lib,seed,policy,self.plan,
                self.predecessor,self.graph,"no_hand_acceleration")
            for t,rec in prior.items():
                self.assertEqual(rows[t]["paid_initial_ignus_cast"],
                                 int(rec["paid_initial_ignus_cast"]))
                self.assertEqual(rows[t]["actual_ignus_cascade_trigger"],
                                 int(rec["actual_ignus_cascade_trigger"]))
                self.assertEqual(rows[t]["actual_supported_effect_resolved"],
                                 int(rec["actual_supported_effect_resolved"]))
            for key in ("deck","hand","lands","graveyard","pool","field"):
                self.assertEqual(prior_state[key],field[key])

    def test_both_modes_are_deterministic_and_conserve_source(self):
        lib=self.variants["ignus_for_rite_of_flame"]
        for mode in self.plan["experiment"]["control_modes"]:
            a=one_trial(lib,621017,"engine_first",self.plan,self.predecessor,self.graph,mode)
            b=one_trial(lib,621017,"engine_first",self.plan,self.predecessor,self.graph,mode)
            self.assertEqual(a[0],b[0])
            self.assertEqual(physical_zones(a[1]),expected_physical(lib))
            self.assertEqual(a[1]["deck"],b[1]["deck"])
            self.assertEqual(a[1]["hand"],b[1]["hand"])

    def test_negative_wrong_policy_and_limits(self):
        lib=self.variants["approved"]
        with self.assertRaises(ValueError):
            one_trial(lib,621017,"engine_first",self.plan,
                self.predecessor,self.graph,"free_mana")
        for k,v in self.plan["limits"].items():
            if k=="measured_win_rate":self.assertIsNone(v)
            elif k in ("m6_certification_issued","m7_new_owner_approvals"):self.assertEqual(v,0)
            else:self.assertFalse(v)

if __name__=="__main__":unittest.main()
