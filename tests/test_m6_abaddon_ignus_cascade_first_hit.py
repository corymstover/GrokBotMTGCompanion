"""Frozen 35-card subthree cascade: physical exile, legal casting and fail closed."""
import unittest
from collections import Counter

from scripts.grixis_m6_abaddon_ignus_cascade_first_hit import (
    inventory, legality_of_hit, resolve_cascade, trial
)

class AbaddonFirstCascade(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan,cls.cards,cls.decks=inventory()

    def test_exact_frozen_graph_and_99_variants(self):
        self.assertEqual(len(self.decks),5)
        base=self.decks["approved"]
        self.assertEqual(len(base),99)
        for name,cards in self.decks.items():
            self.assertEqual(len(cards),99)
            self.assertEqual(Counter(cards)["Island"],3)
            self.assertEqual(Counter(cards)["Swamp"],3)
            self.assertEqual(Counter(cards)["Mountain"],3)

    def test_challenger_cards_absent_from_baseline_graph_have_verified_mv3(self):
        self.assertEqual(self.cards["Grinning Ignus"]["mv"],3)
        self.assertEqual(self.cards["Aggravated Assault"]["mv"],3)
        self.assertEqual(self.cards["Grinning Ignus"]["type_line"],"Creature — Elemental")
        self.assertEqual(self.cards["Aggravated Assault"]["type_line"],"Enchantment")
        for n in ("Grinning Ignus","Aggravated Assault"):
            d=[n,"Sol Ring"]
            rec=resolve_cascade(d,self.cards,seed=4)
            self.assertEqual(rec["first_hit"],"Sol Ring")
            self.assertEqual(rec["exiled_count"],2)

    def test_physical_subthree_pool_and_roles(self):
        p=self.plan
        self.assertEqual(p["baseline_nonland_lt3"],{
            "total_unique_physical":35,"mv0":7,"mv1":15,"mv2":13})
        self.assertEqual(len(p["roles"]["zero_cost_suspend_can_cast"]),3)
        self.assertEqual(len(p["roles"]["artifact_mana"]),9)
        self.assertEqual(len(p["roles"]["ritual_mana"]),3)
        self.assertEqual(len(p["roles"]["tutors"]),6)

    def test_ignus_mv3_skips_equal_or_greater(self):
        deck=["Nightscape Familiar","Grinning Ignus","Birgi, God of Storytelling // Harnfel, Horn of Bounty","Sol Ring"]
        r=resolve_cascade(deck,self.cards,seed=4)
        self.assertEqual(r["first_hit"],"Nightscape Familiar")
        self.assertEqual(r["hit_mana_value"],2)
        self.assertTrue(r["chosen_cast_from_exile"])

    def test_lands_and_mv3_skipped_and_bottomed(self):
        deck=["Island","Ancient Tomb","Birgi, God of Storytelling // Harnfel, Horn of Bounty","Sol Ring"]
        r=resolve_cascade(deck,self.cards,seed=4)
        self.assertEqual(r["first_hit"],"Sol Ring")
        self.assertEqual(r["exiled_count"],4)
        self.assertEqual(r["library_after"],3)
        self.assertEqual(Counter(deck),Counter(["Island","Ancient Tomb",
                 "Birgi, God of Storytelling // Harnfel, Horn of Bounty"]))

    def test_suspend_no_mana_cost_spells_can_cascade_cast(self):
        for n in self.plan["roles"]["zero_cost_suspend_can_cast"]:
            with self.subTest(n=n):
                deck=[n]
                r=resolve_cascade(deck,self.cards,seed=4)
                self.assertEqual(r["hit_mana_value"],0)
                self.assertTrue(r["legal_to_cast"])
                self.assertTrue(r["chosen_cast_from_exile"])
                self.assertEqual(deck,[])

    def test_flusterstorm_cannot_target_original_creature(self):
        d=["Flusterstorm"]
        r=resolve_cascade(d,self.cards,seed=4)
        self.assertFalse(r["legal_to_cast"])
        self.assertFalse(r["chosen_cast_from_exile"])
        self.assertEqual(d,["Flusterstorm"])

    def test_swan_song_cannot_target_original_creature(self):
        d=["Swan Song"]
        r=resolve_cascade(d,self.cards,seed=4)
        self.assertFalse(r["legal_to_cast"])
        self.assertEqual(d,["Swan Song"])

    def test_pact_can_self_counter_but_safe_policy_declines(self):
        d=["Pact of Negation"]
        r=resolve_cascade(d,self.cards,seed=4)
        self.assertTrue(r["legal_to_cast"])
        self.assertFalse(r["chosen_cast_from_exile"])
        self.assertEqual(r["reason"],"decline_self_counter_original_ignus")
        self.assertEqual(d,["Pact of Negation"])

    def test_pyroblast_target_red_ignus_cast_legal_but_not_blue_effect(self):
        d=["Pyroblast"]
        r=resolve_cascade(d,self.cards,seed=4)
        self.assertTrue(r["legal_to_cast"])
        self.assertTrue(r["chosen_cast_from_exile"])
        self.assertEqual(r["reason"],"legal_red_ignus_target_no_blue_effect")
        self.assertEqual(d,[])

    def test_rule_of_law_cascade_hit_cannot_cast(self):
        d=["Sol Ring"]
        r=resolve_cascade(d,self.cards,seed=4,rule_of_law=True)
        self.assertFalse(r["chosen_cast_from_exile"])
        self.assertEqual(r["reason"],"spell_limit")
        self.assertEqual(d,["Sol Ring"])

    def test_drannith_cascade_hit_cannot_cast(self):
        d=["Sol Ring"]
        r=resolve_cascade(d,self.cards,seed=4,drannith=True)
        self.assertFalse(r["chosen_cast_from_exile"])
        self.assertEqual(r["reason"],"nonhand_spell_prohibited")
        self.assertEqual(d,["Sol Ring"])

    def test_stack_with_legal_instant_target_can_make_swan_song_legal(self):
        d=["Swan Song"]
        r=resolve_cascade(d,self.cards,seed=4,only_original_ignus_on_stack=False)
        self.assertTrue(r["legal_to_cast"])
        self.assertTrue(r["chosen_cast_from_exile"])

    def test_physical_shuffle_keeps_multiplicity_in_duplicate_basics(self):
        original=["Island","Swamp","Mountain","Island","Mountain","Sol Ring"]
        a=list(original);b=list(original)
        ra=resolve_cascade(a,self.cards,seed=715)
        rb=resolve_cascade(b,self.cards,seed=715)
        self.assertEqual((ra,a),(rb,b))
        self.assertEqual(len(a),len(original)-1)
        self.assertEqual(Counter(a),Counter(["Island","Swamp","Mountain","Island","Mountain"]))

    def test_all_exiled_when_no_low_value_nonland(self):
        original=["Island","Grinning Ignus","Bituminous Blast"]
        d=list(original)
        r=resolve_cascade(d,self.cards,seed=43)
        self.assertIsNone(r["first_hit"])
        self.assertFalse(r["chosen_cast_from_exile"])
        self.assertEqual(Counter(d),Counter(original))

    def test_mana_payment_does_not_change_trigger_mana_value(self):
        # Cost reductions from Rakdos/Familiar do not change an MV3 trigger.
        deck=["Ancestral Vision","Nightscape Familiar"]
        r=resolve_cascade(deck,self.cards,seed=4,trigger_mv=3)
        self.assertEqual(r["first_hit"],"Ancestral Vision")
        self.assertFalse(r["abaddon_granted_cascade_to_exile_hit"])

    def test_checkpoint_sampling_is_independent_hypothetical_trigger(self):
        lib=self.decks["ignus_for_rakdos"]
        first=trial(self.cards,lib,621017,[4,6,8,10],self.plan)
        second=trial(self.cards,lib,621017,[4,6,8,10],self.plan)
        self.assertEqual(first,second)
        self.assertTrue(all(x["physically_eligible_snapshot_only"] for x in first.values()))
        self.assertTrue(all(not x["actual_hit_effect_resolved"] for x in first.values()))

    def test_source_and_owner_authority_is_not_upgraded(self):
        b=self.plan["bounds"]
        self.assertFalse(any(x for k,x in b.items() if isinstance(x,bool)))
        self.assertIsNone(b["actual_win_rate"])
        self.assertEqual(b["m6_certificates"],0)
        self.assertEqual(b["m7_owner_approvals"],0)

if __name__=="__main__":
    unittest.main()
