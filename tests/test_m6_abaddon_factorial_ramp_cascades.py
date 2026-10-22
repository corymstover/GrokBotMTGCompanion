"""Adversarial four-arm paid acceleration x other Abaddon hand-cascade tests."""
import unittest
from collections import Counter
from scripts.grixis_m6_abaddon_factorial_ramp_cascades import (
    verify,one_trial,shared_metrics,shared_seeds,run
)
from scripts.grixis_m6_abaddon_hand_acceleration_shared import (
    paid_accelerants_from_hand,one_trial as hand_predecessor
)
from scripts.grixis_m6_abaddon_other_hand_cascades import (
    one_trial as other_predecessor
)
from scripts.grixis_m6_abaddon_ignus_shared_effects import (
    ABADDON,BIRGI,IGNUS,ZERO,physical_zones,expected_physical,
    first_cascade,main_phase
)


def minimal(deck,hand,*,field=(ABADDON,),lands=(),pool=ZERO,loss=0,graveyard=()):
    return {"deck":list(deck),"hand":list(hand),"field":set(field),
            "lands":list(lands),"graveyard":list(graveyard),"pool":pool,
            "loss":loss,"pilot_life_damage":0,"rocks_tapped":False,
            "metrics":Counter(),"examples":[],"mana_vault_exhausted":False}


class FactorialAbaddonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p,cls.hp,cls.op,cls.old,cls.cards,cls.decks=verify()

    def test_frozen_100_card_five_variants_and_four_arms(self):
        e=self.p["experimental_design"]
        self.assertEqual(len(self.decks),5)
        self.assertEqual(e["modes"],["neither","hand_ramp_only",
                         "core_other_cascade_only","both"])
        self.assertEqual(e["physical_trials"],20000)
        self.assertEqual(e["paired_seeds_per_variant_order_mode"],500)
        self.assertEqual(len(e["casting_orders"]),2)
        for name,library in self.decks.items():
            self.assertEqual(len(library),99)
            self.assertEqual(len(set(library)),93)
            self.assertEqual(library.count("Island"),3)
            self.assertEqual(library.count("Mountain"),3)
            self.assertEqual(library.count("Swamp"),3)
        self.assertEqual(self.p["authority"]["approved_raw_sha256"],
                "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf")

    def test_zero_mv_lotus_real_hand_cast_cascades_at_X_zero(self):
        s=minimal(["Mountain","Island","Swamp","Dark Ritual","Sol Ring"],
                  ["Lotus Petal"],field=(ABADDON,),loss=0)
        original=physical_zones(s)
        paid_accelerants_from_hand(s,self.hp,resolve_other_hand_cascades=True,
                    cards=self.cards,prior=self.old,seed=87,turn=3)
        self.assertEqual(s["metrics"]["zero_mv_hand_cascade_triggers"],1)
        self.assertEqual(s["metrics"]["hand_accelerant_cascade_triggers"],1)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],1)
        self.assertEqual(s["metrics"]["cascade_cards_exiled"],5)
        self.assertEqual(s["metrics"]["actual_supported_hits_resolved"],0)
        self.assertEqual(s["metrics"]["hand_cast_Lotus Petal"],1)
        self.assertEqual(s["pool"],(0,0,1,0))
        self.assertIn("Lotus Petal",s["graveyard"])
        self.assertNotIn("Lotus Petal",s["field"])
        self.assertEqual(physical_zones(s),original)

    def test_zero_mv_cascade_not_generated_without_commander(self):
        s=minimal(["Island","Ancestral Vision"],["Lotus Petal"],field=(),loss=0)
        paid_accelerants_from_hand(s,self.hp,resolve_other_hand_cascades=True,
                    cards=self.cards,prior=self.old,seed=87,turn=3)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],0)
        self.assertEqual(s["deck"],["Island","Ancestral Vision"])
        self.assertEqual(s["pool"],(0,0,1,0))

    def test_rite_of_flame_cascade_draws_before_rite_effect(self):
        s=minimal(["Ancestral Vision","Mountain","Island","Swamp","Sol Ring"],
                  ["Rite of Flame"],field=(ABADDON,BIRGI),
                  lands=[("Mountain",False)],loss=1)
        original=physical_zones(s)
        paid_accelerants_from_hand(s,self.hp,resolve_other_hand_cascades=True,
                    cards=self.cards,prior=self.old,seed=9,turn=5)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],1)
        self.assertEqual(s["metrics"]["actual_supported_hits_resolved"],1)
        self.assertEqual(s["metrics"]["hit_cards_drawn"],3)
        self.assertEqual(s["metrics"]["hand_red_mana"],2)
        self.assertEqual(s["pool"][2],4) # Rite R2 + Birgi R1 for Rite and R1 for cascade-cast Vision
        self.assertEqual(s["graveyard"],["Ancestral Vision","Rite of Flame"])
        self.assertEqual(physical_zones(s),original)

    def test_dark_ritual_can_cascade_zero_mv_before_three_black(self):
        s=minimal(["Ancestral Vision","Island","Swamp","Mountain"],
                  ["Dark Ritual"],field=(ABADDON,),
                  lands=[("Swamp",False)],loss=1)
        original=physical_zones(s)
        paid_accelerants_from_hand(s,self.hp,resolve_other_hand_cascades=True,
                    cards=self.cards,prior=self.old,seed=17,turn=5)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],1)
        self.assertEqual(s["metrics"]["hit_cards_drawn"],3)
        self.assertEqual(s["metrics"]["hand_black_mana"],3)
        self.assertEqual(s["pool"],(0,3,0,0))
        self.assertEqual(physical_zones(s),original)

    def test_cabal_ritual_mana_value_two_strictly_less_hit(self):
        s=minimal(["Cabal Ritual","Sol Ring","Mountain"],
                  ["Cabal Ritual"],field=(ABADDON,),
                  lands=[("Swamp",False),("Island",False)],loss=2)
        # Mini-fixture may duplicate source by name; collapse physical as
        # a distinct face to avoid claiming this is a complete 99-card source.
        s["deck"].remove("Cabal Ritual")
        original=physical_zones(s)
        paid_accelerants_from_hand(s,self.hp,resolve_other_hand_cascades=True,
                    cards=self.cards,prior=self.old,seed=17,turn=5)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],1)
        self.assertIn("Sol Ring",s["field"])
        self.assertEqual(s["metrics"]["hand_black_mana"],3)
        self.assertEqual(s["metrics"]["hit_colorless_mana"],2)
        self.assertEqual(physical_zones(s),original)

    def test_unsupported_already_cast_from_exile_does_not_recurse(self):
        s=minimal(["Ancestral Vision","Mountain","Swamp","Island"],
                  ["Sol Ring"],field=(ABADDON,BIRGI),
                  lands=[("Mountain",False)],loss=1)
        paid_accelerants_from_hand(s,self.hp,resolve_other_hand_cascades=True,
                    cards=self.cards,prior=self.old,seed=17,turn=3)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],1)
        self.assertEqual(s["metrics"]["hit_cards_drawn"],3)
        self.assertEqual(s["metrics"]["actual_paid_ignus_cascade"],0)
        self.assertIn("Sol Ring",s["field"])

    def test_default_hand_helper_still_ignores_other_cascade(self):
        s=minimal(["Ancestral Vision","Island"],["Sol Ring"],
                  field=(ABADDON,),lands=[("Mountain",False)],loss=1)
        paid_accelerants_from_hand(s,self.hp)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],0)
        self.assertEqual(s["deck"],["Ancestral Vision","Island"])
        self.assertIn("Sol Ring",s["field"])

    def test_combined_requires_graph_and_predecessor_for_cascade(self):
        s=minimal(["Mountain"],["Lotus Petal"],field=(ABADDON,))
        with self.assertRaises(ValueError):
            paid_accelerants_from_hand(s,self.hp,
                resolve_other_hand_cascades=True)

    def test_hand_cast_boltwave_does_not_grant_own_cascade_retroactively(self):
        s=minimal(["Ancestral Vision"],["Boltwave"],field=(ABADDON,),
                  pool=(0,0,1,0),loss=0)
        main_phase(s,self.cards,self.old,9,4,"engine_first",
                   other_hand_cascades=True)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],0)
        self.assertEqual(s["loss"],9)

    def test_all_four_arms_run_exact_matched_source_without_duplicate_cards(self):
        lib=self.decks["ignus_for_rakdos"]
        for mode in self.p["experimental_design"]["modes"]:
            with self.subTest(mode=mode):
                snapshots,field=one_trial(lib,621017,"engine_first",
                    self.p,self.hp,self.op,self.old,self.cards,mode)
                self.assertEqual(set(snapshots),{"4","6","8","10"})
                self.assertEqual(physical_zones(field),expected_physical(lib))
                self.assertLessEqual(snapshots["10"]["actual_other_hand_cascade_seed"],1)
                self.assertLessEqual(snapshots["10"]["actual_supported_effect_seed"],1)

    def test_each_delegated_arm_matches_existent_predecessor_exactly(self):
        lib=self.decks["ignus_for_rite_of_flame"]
        for policy in self.p["experimental_design"]["casting_orders"]:
            for mode in ("neither","hand_ramp_only","core_other_cascade_only"):
                with self.subTest(mode=mode,policy=policy):
                    a,field=one_trial(lib,621017,policy,
                      self.p,self.hp,self.op,self.old,self.cards,mode)
                    if mode=="neither":
                        b,prior=other_predecessor(lib,621017,policy,
                           self.op,self.old,self.cards,"original_ignus_only")
                    elif mode=="hand_ramp_only":
                        b,prior=hand_predecessor(lib,621017,policy,
                           self.hp,self.old,self.cards,"hand_acceleration")
                    else:
                        b,prior=other_predecessor(lib,621017,policy,
                           self.op,self.old,self.cards,"plus_other_qualified_hand_casts")
                    self.assertEqual(field["deck"],prior["deck"])
                    self.assertEqual(field["hand"],prior["hand"])
                    self.assertEqual(field["graveyard"],prior["graveyard"])
                    self.assertEqual(field["pool"],prior["pool"])
                    self.assertEqual(a["10"]["paid_initial_ignus_cast_seed"],int(
                         b["10"]["paid_initial_ignus_cast"]))

    def test_same_seed_combined_is_reproducible(self):
        lib=self.decks["ignus_for_nightscape_familiar"]
        a,x=one_trial(lib,621017,"burn_first",self.p,self.hp,self.op,
                      self.old,self.cards,"both")
        b,y=one_trial(lib,621017,"burn_first",self.p,self.hp,self.op,
                      self.old,self.cards,"both")
        self.assertEqual(a,b)
        self.assertEqual(x["deck"],y["deck"])
        self.assertEqual(x["graveyard"],y["graveyard"])

    def test_bad_mode_and_frozen_scope_rejects_wins(self):
        lib=self.decks["approved"]
        with self.assertRaises(ValueError):
            one_trial(lib,2,"engine_first",self.p,self.hp,self.op,
                      self.old,self.cards,"forced_win")
        for k,v in self.p["limits"].items():
            if k=="actual_multiplayer_wins":self.assertIsNone(v)
            elif k in ("m6_certificates","m7_approval_records"):self.assertEqual(v,0)
            else:self.assertFalse(v)

    def test_small_sample_schema_all_combinations(self):
        r=run(2)
        self.assertEqual(r["samples_per_variant_policy_mode"],2)
        self.assertEqual(set(r["arms"]),set(self.p["experimental_design"]["modes"]))
        for mode,policies in r["arms"].items():
            self.assertEqual(set(policies),set(self.p["experimental_design"]["casting_orders"]))
            for _,variants in policies.items():
                self.assertEqual(set(variants),set(self.decks))
                for _,v in variants.items():
                    d=v["checkpoints"]["10"]
                    self.assertLessEqual(d["actual_other_hand_cascade_seed"],2)
                    self.assertLessEqual(d["actual_supported_effect_seed"],2)
                    self.assertLessEqual(d["actual_zero_mv_cascade_seed"],2)

if __name__=="__main__":unittest.main()
