"""Abaddon source-bound physically joined Ignus cascade-effect regression tests."""
import unittest
from collections import Counter
from scripts.grixis_m6_abaddon_ignus_shared_effects import (
    ABADDON,BIRGI,IGNUS,INSTANT_SORCERY,SUPPORTED,
    ZERO,verify,physical_zones,assert_conserved,
    first_cascade,create_state,recast_ignus,one_trial,expected_physical,
    effect_resolve,main_phase,run,
)

class SharedIgnusEffectCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan,cls.cards,cls.decks=verify()

    def state(self,deck,*,hand=(),field=(ABADDON,BIRGI),graveyard=(),pool=ZERO):
        return {"deck":list(deck),"hand":list(hand),"field":set(field),
                "lands":[],"graveyard":list(graveyard),"pool":pool,
                "loss":9,"pilot_life_damage":0,
                "rocks_tapped":False,"metrics":Counter(),"examples":[]}

    def test_preregistered_subset_and_source_sha_and_exact_100(self):
        self.assertEqual(len(SUPPORTED),12)
        self.assertEqual(set(SUPPORTED),set(self.plan["resolution_model"]["supported_effects"]))
        self.assertEqual(self.plan["source"]["approved_raw_sha256"],
                         "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf")
        self.assertEqual(len(self.decks),5)
        for name,cards in self.decks.items():
            self.assertEqual(len(cards),99)
            self.assertEqual(len(set(cards)),93)
        self.assertFalse(self.plan["limits"]["canonical_changed"])

    def test_conservation_99_from_physical_draw_and_play(self):
        library=self.decks["ignus_for_rakdos"]
        snap,state=one_trial(library,621017,"engine_first",self.plan,self.cards)
        self.assertEqual(set(snap),{"4","6","8","10"})
        self.assertEqual(physical_zones(state),expected_physical(library))

    def test_paid_hand_burn_goes_only_to_grave_not_battlefield(self):
        for burn,lands,loss in (
             ("Boltwave",[("Mountain",False)],9),
             ("Flame Rift",[("Mountain",False),("Island",False)],12)):
            with self.subTest(burn=burn):
                state=self.state([],hand=[burn],field=())
                state["lands"]=list(lands)
                original=physical_zones(state)
                main_phase(state,self.cards,self.plan,1701,3,"engine_first")
                self.assertEqual(state["loss"],9+loss)
                self.assertNotIn(burn,state["field"])
                self.assertIn(burn,state["graveyard"])
                self.assertEqual(physical_zones(state),original)

    def test_dark_ritual_adds_real_black_and_birgi_red_and_grave(self):
        state=self.state(["Dark Ritual","Island"],pool=(0,0,1,0))
        first=Counter(state["deck"])+Counter(state["graveyard"])
        receipt=first_cascade(state,self.cards,3,self.plan)
        self.assertEqual(receipt["hit"],"Dark Ritual")
        self.assertTrue(receipt["supported_and_effect_resolved"])
        self.assertEqual(state["pool"],(0,3,2,0))
        self.assertEqual(state["graveyard"],["Dark Ritual"])
        self.assertEqual(Counter(state["deck"])+Counter(state["graveyard"]),first)

    def test_rite_two_red_not_three_from_own_resolution(self):
        state=self.state(["Rite of Flame"],pool=ZERO)
        first_cascade(state,self.cards,3,self.plan)
        self.assertEqual(state["pool"],(0,0,3,0)) # Birgi 1 + Rite 2
        self.assertEqual(state["metrics"]["hit_red_mana"],2)
        self.assertEqual(state["graveyard"],["Rite of Flame"])

    def test_sol_ring_entry_taps_once_for_colorless(self):
        state=self.state(["Sol Ring"],pool=ZERO)
        first_cascade(state,self.cards,3,self.plan)
        self.assertIn("Sol Ring",state["field"])
        self.assertTrue(state["rocks_tapped"])
        self.assertEqual(state["pool"],(0,0,1,2))
        self.assertEqual(state["metrics"]["hit_colorless_mana"],2)
        self.assertEqual(state["graveyard"],[])

    def test_lotus_petal_funds_one_red_but_is_physically_sacrificed(self):
        state=self.state(["Lotus Petal"],pool=ZERO)
        first_cascade(state,self.cards,3,self.plan)
        self.assertEqual(state["pool"],(0,0,2,0)) # Birgi 1 + Petal R
        self.assertNotIn("Lotus Petal",state["field"])
        self.assertIn("Lotus Petal",state["graveyard"])

    def test_boltwave_resolves_to_9_real_opponent_loss(self):
        state=self.state(["Boltwave"],field=(ABADDON,))
        state["loss"]=3
        first_cascade(state,self.cards,3,self.plan)
        self.assertEqual(state["loss"],12)
        self.assertEqual(state["metrics"]["hit_opponent_loss"],9)
        self.assertEqual(state["pilot_life_damage"],0)

    def test_flame_rift_12_opponent_and_4_pilot_damage(self):
        state=self.state(["Flame Rift"],field=(ABADDON,))
        state["loss"]=3
        first_cascade(state,self.cards,3,self.plan)
        self.assertEqual(state["loss"],15)
        self.assertEqual(state["pilot_life_damage"],4)
        self.assertEqual(state["graveyard"],["Flame Rift"])

    def test_ancestral_vison_draws_three_from_shared_physical_deck(self):
        state=self.state(["Ancestral Vision","Mountain","Sol Ring","Swamp","Island"])
        original=Counter(state["deck"])
        receipt=first_cascade(state,self.cards,77,self.plan)
        self.assertEqual(receipt["physically_drawn"],3)
        self.assertEqual(state["hand"],["Mountain","Sol Ring","Swamp"])
        self.assertEqual(state["deck"],["Island"])
        self.assertEqual(state["graveyard"],["Ancestral Vision"])
        self.assertEqual(Counter(state["deck"]+state["graveyard"]+state["hand"]),original)

    def test_profane_tutor_removes_physical_burn_to_hand(self):
        state=self.state(["Profane Tutor","Island","Boltwave","Mountain"])
        original=Counter(state["deck"])
        rec=first_cascade(state,self.cards,33,self.plan)
        self.assertEqual(rec["physically_searched"],"Boltwave")
        self.assertIn("Boltwave",state["hand"])
        self.assertNotIn("Boltwave",state["deck"])
        self.assertIn("Profane Tutor",state["graveyard"])
        self.assertEqual(Counter(state["deck"]+state["hand"]+state["graveyard"]),original)

    def test_demonic_tutor_identical_physical_search(self):
        state=self.state(["Demonic Tutor","Dark Ritual","Island"])
        first_cascade(state,self.cards,17,self.plan)
        self.assertEqual(state["hand"],["Dark Ritual"])
        self.assertEqual(state["graveyard"],["Demonic Tutor"])

    def test_top_deck_tutors_do_not_give_immediate_hand_card(self):
        for name in ("Vampiric Tutor","Imperial Seal"):
            with self.subTest(name=name):
                state=self.state([name,"Mountain","Boltwave"])
                first_cascade(state,self.cards,50,self.plan)
                self.assertEqual(state["deck"][0],"Boltwave")
                self.assertEqual(state["hand"],[])
                self.assertEqual(state["pilot_life_damage"],2)
                self.assertEqual(state["metrics"]["hit_tutored_top"],1)

    def test_gamble_discard_is_real_and_retention_not_guaranteed(self):
        state=self.state(["Gamble","Boltwave"],hand=["Island"])
        orig=Counter(state["deck"]+state["hand"])
        r=first_cascade(state,self.cards,25,self.plan)
        self.assertEqual(state["metrics"]["gamble_discarded"],1)
        self.assertIn(r["discarded"],["Island","Boltwave"])
        self.assertEqual(Counter(state["deck"]+state["hand"]+state["graveyard"]),orig)

    def test_first_unsupported_hit_declined_not_skip_to_safe_one(self):
        state=self.state(["Arcane Signet","Dark Ritual"],pool=ZERO)
        original=Counter(state["deck"])
        rec=first_cascade(state,self.cards,9,self.plan)
        self.assertFalse(rec["cast_from_exile"])
        self.assertEqual(rec["hit"],"Arcane Signet")
        self.assertEqual(state["metrics"]["actual_supported_hits_resolved"],0)
        self.assertEqual(Counter(state["deck"]),original)

    def test_no_cascade_for_paid_loop_without_abaddon_or_loss(self):
        state=self.state([],field=(IGNUS,BIRGI),pool=(0,0,1,0))
        five=recast_ignus(state,self.cards,self.plan,17,7)
        self.assertEqual(five,5)
        self.assertEqual(state["metrics"]["actual_paid_ignus_cascade"],0)
        self.assertEqual(state["pool"][2],1)
        state2=self.state([],field=(IGNUS,BIRGI,ABADDON),pool=(0,0,1,0))
        state2["loss"]=2
        self.assertEqual(recast_ignus(state2,self.cards,self.plan,17,7),5)
        self.assertEqual(state2["metrics"]["actual_paid_ignus_cascade"],0)

    def test_paid_ignus_recast_mutates_shared_deck_and_mana_five_times(self):
        state=self.state(["Dark Ritual","Rite of Flame","Sol Ring","Lotus Petal","Ancestral Vision",
                          "Mountain","Swamp","Island","Boltwave","Flame Rift"],
                         field=(IGNUS,ABADDON,BIRGI),pool=(0,0,1,0))
        original=Counter(state["deck"])+Counter([IGNUS])
        count=recast_ignus(state,self.cards,self.plan,621017,7)
        self.assertEqual(count,5)
        self.assertEqual(state["metrics"]["actual_paid_ignus_cascade"],5)
        self.assertGreater(state["metrics"]["actual_supported_hits_resolved"],0)
        self.assertIn(IGNUS,state["field"])
        self.assertEqual(Counter(state["deck"]+state["graveyard"]+state["hand"]+
                                 [x for x in state["field"] if x not in (ABADDON,BIRGI)]),original)

    def test_tutored_top_card_changes_next_paid_cascade_eligible_hit(self):
        state=self.state(["Vampiric Tutor","Island","Boltwave","Swamp"],pool=(0,0,1,0))
        first_cascade(state,self.cards,12,self.plan)
        self.assertEqual(state["deck"][0],"Boltwave")
        before=state["loss"]
        rec=first_cascade(state,self.cards,13,self.plan)
        self.assertEqual(rec["hit"],"Boltwave")
        self.assertEqual(state["loss"]-before,9)

    def test_true_paid_casts_and_cascade_hits_from_same_library(self):
        lib=self.decks["ignus_for_rakdos"]
        a=one_trial(lib,621017,"engine_first",self.plan,self.cards)
        b=one_trial(lib,621017,"engine_first",self.plan,self.cards)
        self.assertEqual(a[0],b[0])
        self.assertEqual(a[1]["deck"],b[1]["deck"])
        self.assertEqual(a[1]["hand"],b[1]["hand"])
        self.assertEqual(a[1]["graveyard"],b[1]["graveyard"])

    def test_no_simulated_stealing_or_unbounded_outcome_claim(self):
        for k,v in self.plan["limits"].items():
            if k=="actual_game_win_rate":self.assertIsNone(v)
            elif k in ("m6_certificates","m7_decks_approved"):self.assertEqual(v,0)
            elif k=="land_only_setup_except_cascade_created_mana":self.assertTrue(v)
            else:self.assertFalse(v)
        self.assertIn("Inevitable Betrayal (opponent library unknown)",
                      self.plan["resolution_model"]["unsupported_or_declined"])

if __name__=="__main__": unittest.main()
