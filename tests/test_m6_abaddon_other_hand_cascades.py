"""Abaddon static ability grants cascade to eligible OTHER hand spells, too."""
import unittest
from collections import Counter
from scripts.grixis_m6_abaddon_other_hand_cascades import (
    verify,one_trial,run
)
from scripts.grixis_m6_abaddon_ignus_shared_effects import (
    ABADDON,BIRGI,IGNUS,RAKDOS,ASSAULT,ZERO,
    first_cascade,main_phase,physical_zones,expected_physical
)
from scripts.grixis_m6_abaddon_ignus_paid_chronology import MV_AND_COLORS


def state(deck,*,hand=(),field=(ABADDON,),pool=ZERO,loss=9,lands=()):
    return {"deck":list(deck),"hand":list(hand),"field":set(field),
            "lands":list(lands),"graveyard":[],"pool":pool,"loss":loss,
            "pilot_life_damage":0,"rocks_tapped":False,
            "metrics":Counter(),"examples":[]}


class OtherSourcePaidHandCascades(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p,cls.old,cls.cards,cls.decks=verify()

    def test_printed_mvs_are_fixed_before_rakdos_familiar_discounts(self):
        for name,mv in self.p["scope"]["register_printed_mvs"].items():
            self.assertEqual(self.cards[name]["mv"],mv)
            self.assertEqual(MV_AND_COLORS[name][0],mv)
        self.assertEqual(len(self.decks),5)
        self.assertEqual(len(self.decks["approved"]),99)
        self.assertEqual(self.p["authority"]["canonical_approved_sha256"],
              "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf")

    def test_mv0_cascade_exiles_entire_library_without_a_spell_cast(self):
        d=["Island","Swamp","Dark Ritual","Sol Ring","Ancestral Vision"]
        s=state(d)
        orig=Counter(s["deck"])
        r=first_cascade(s,self.cards,173,self.old,
                        source_kind="other_hand",trigger_mv=0)
        self.assertIsNone(r["hit"])
        self.assertFalse(r["cast_from_exile"])
        self.assertEqual(r["source_printed_mv"],0)
        self.assertEqual(s["metrics"]["cascade_cards_exiled"],5)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],1)
        self.assertEqual(s["metrics"]["actual_paid_ignus_cascade"],0)
        self.assertEqual(Counter(s["deck"]),orig)
        self.assertEqual(len(s["deck"]),5)

    def test_mv1_can_hit_ancestral_but_not_ring_or_dark_ritual(self):
        s=state(["Sol Ring","Dark Ritual","Ancestral Vision","Mountain"])
        r=first_cascade(s,self.cards,77,self.old,trigger_mv=1,
                        source_kind="other_hand")
        self.assertEqual(r["hit"],"Ancestral Vision")
        self.assertTrue(r["cast_from_exile"])
        self.assertEqual(r["physically_drawn"],3)
        self.assertIn("Ancestral Vision",s["graveyard"])
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],1)

    def test_mv2_can_hit_mv1_but_not_mv2(self):
        s=state(["Cabal Ritual","Sol Ring","Mountain"])
        r=first_cascade(s,self.cards,77,self.old,trigger_mv=2,
                        source_kind="other_hand")
        self.assertEqual(r["hit"],"Sol Ring")
        self.assertTrue(r["cast_from_exile"])
        self.assertIn("Cabal Ritual",s["deck"])
        self.assertIn("Sol Ring",s["field"])

    def test_mv4_can_hit_mv3_but_unsupported_last_hit_is_not_skipped(self):
        s=state([IGNUS,"Dark Ritual"])
        r=first_cascade(s,self.cards,123,self.old,
                        trigger_mv=4,source_kind="other_hand")
        self.assertEqual(r["hit"],IGNUS)
        self.assertEqual(r["source_printed_mv"],4)
        self.assertFalse(r["cast_from_exile"])
        self.assertEqual(Counter(s["deck"]),Counter([IGNUS,"Dark Ritual"]))
        self.assertEqual(s["metrics"]["actual_paid_ignus_cascade"],0)

    def test_flame_rift_requires_prior_two_opponent_life_loss(self):
        for loss,expected in ((1,0),(2,1)):
            with self.subTest(loss=loss):
                s=state(["Sol Ring","Mountain"],hand=("Flame Rift",),
                        pool=(0,0,1,1),loss=loss)
                main_phase(s,self.cards,self.old,117,4,"engine_first",
                           other_hand_cascades=True)
                self.assertEqual(s["metrics"]["actual_other_hand_cascade"],expected)
                self.assertEqual(s["loss"],loss+12)
                self.assertIn("Flame Rift",s["graveyard"])

    def test_boltwave_own_damage_cannot_retroactively_cascade(self):
        s=state(["Ancestral Vision","Mountain"],hand=("Boltwave",),
                pool=(0,0,1,0),loss=0)
        main_phase(s,self.cards,self.old,10,4,"engine_first",
                   other_hand_cascades=True)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],0)
        self.assertEqual(s["loss"],9)
        self.assertIn("Boltwave",s["graveyard"])
        self.assertIn("Ancestral Vision",s["deck"])

    def test_boltwave_prior_life_loss_grants_cascade_before_burn_resolves(self):
        s=state(["Ancestral Vision","Island","Swamp","Mountain","Sol Ring"],
                hand=("Boltwave",),pool=(0,0,1,0),loss=1)
        main_phase(s,self.cards,self.old,10,4,"engine_first",
                   other_hand_cascades=True)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],1)
        self.assertEqual(s["metrics"]["hit_cards_drawn"],3)
        self.assertEqual(s["loss"],10)
        self.assertIn("Boltwave",s["graveyard"])
        self.assertIn("Ancestral Vision",s["graveyard"])

    def test_rakdos_mv4_source_paid_can_hit_mana_value_three_card(self):
        s=state(["Ancestral Vision","Mountain","Swamp","Island"],
                hand=(RAKDOS,),field=(ABADDON,),pool=(0,2,2,0),loss=9)
        main_phase(s,self.cards,self.old,37,8,"engine_first",
                   other_hand_cascades=True)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],1)
        self.assertIn(RAKDOS,s["field"])
        self.assertIn("Ancestral Vision",s["graveyard"])
        self.assertEqual(s["metrics"]["hit_cards_drawn"],3)

    def test_birgi_only_gives_red_when_already_controlled(self):
        s=state(["Ancestral Vision"],hand=("Boltwave",),
                field=(ABADDON,BIRGI),pool=(0,0,1,0),loss=9)
        main_phase(s,self.cards,self.old,7,3,"engine_first",
                   other_hand_cascades=True)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],1)
        self.assertGreaterEqual(s["pool"][2],1)
        self.assertNotIn(BIRGI,s["hand"])

    def test_abaddon_from_command_zone_cannot_cascade_itself(self):
        s=state(["Ancestral Vision"],hand=(),field=(),
                pool=(1,1,1,2),loss=9)
        main_phase(s,self.cards,self.old,7,5,"engine_first",
                   other_hand_cascades=True)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],0)
        self.assertIn(ABADDON,s["field"])

    def test_no_opponent_loss_abaddon_does_not_grant_mv1_spell(self):
        s=state(["Ancestral Vision"],hand=("Boltwave",),
                field=(ABADDON,),pool=(0,0,1,0),loss=0)
        main_phase(s,self.cards,self.old,7,5,"engine_first",
                   other_hand_cascades=True)
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],0)

    def test_default_exact_original_pilot_does_not_resolve_other_cascade(self):
        s=state(["Ancestral Vision"],hand=("Boltwave",),
                pool=(0,0,1,0),loss=9)
        main_phase(s,self.cards,self.old,7,5,"engine_first")
        self.assertEqual(s["metrics"]["actual_other_hand_cascade"],0)
        self.assertEqual(s["metrics"]["other_hand_cascade_triggers_OMITTED"],1)
        self.assertEqual(s["deck"],["Ancestral Vision"])

    def test_same_physical_seeds_control_against_predecessor(self):
        lib=self.decks["ignus_for_rakdos"]
        for policy in self.p["policies"]:
            a,b=one_trial(lib,621017,policy,self.p,self.old,self.cards,
                          "original_ignus_only")
            c,d=one_trial(lib,621017,policy,self.p,self.old,self.cards,
                          "plus_other_qualified_hand_casts")
            for t in ("4","6","8","10"):
                self.assertEqual(a[t]["other_hand_cascade_seed"],0)
                self.assertGreaterEqual(c[t]["other_hand_cascade_seed"],0)
            self.assertEqual(physical_zones(b),expected_physical(lib))
            self.assertEqual(physical_zones(d),expected_physical(lib))

    def test_bad_negative_mv_or_unregistered_source_fails_closed(self):
        s=state(["Sol Ring"])
        with self.assertRaises(ValueError):
            first_cascade(s,self.cards,3,self.old,
                          trigger_mv=-1,source_kind="other_hand")
        with self.assertRaises(ValueError):
            first_cascade(s,self.cards,3,self.old,
                          trigger_mv=3,source_kind="cast_from_exile")

    def test_boundaries_never_claim_wins_or_deck_authority(self):
        p=self.p["bounds"]
        self.assertFalse(p["canonical_changed"])
        self.assertFalse(p["full_99_card_effects"])
        self.assertFalse(p["all_hand_spell_cascade_triggers"])
        self.assertFalse(p["opponent_interaction_model"])
        self.assertFalse(p["superiority_proven"])
        self.assertIsNone(p["valid_multiplayer_win_rate"])
        self.assertEqual(p["m6_certificates"],0)
        self.assertEqual(p["m7_owner_approvals"],0)

if __name__=="__main__":
    unittest.main()
