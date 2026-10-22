"""Fail-closed Chaos Warp vs locked Abaddon stax opportunities (not gameplay)."""
import random
import unittest
from scripts.grixis_m6_abaddon_chaos_warp_stax import (
    COSTS, STAX, available_hand_answer, frozen_variants,
    response_window, trial,
)


class ChaosWarpStaxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan, cls.variants = frozen_variants()

    def test_precommitted_exact_100_card_one_slot_only(self):
        b=self.variants["baseline"]
        self.assertEqual(len(b),99)
        self.assertNotIn("Chaos Warp",b)
        self.assertEqual(len(self.variants),4)
        for name,library in self.variants.items():
            differences=[(i,x,y) for i,(x,y) in enumerate(zip(b,library)) if x!=y]
            self.assertEqual(len(differences),0 if name=="baseline" else 1)
            self.assertEqual(library.count("Chaos Warp"),int(name!="baseline"))

    def test_original_identity_cards_actually_have_low_printed_mv(self):
        x={r["card"]:r for r in self.plan["role_fixed_oracle"]}
        self.assertEqual(x["The Lost and the Damned"]["mana_value"],3)
        self.assertEqual(x["The Ruinous Powers"]["mana_value"],4)
        self.assertEqual(x["Chaos Warp"]["mana_cost"],"{2}{R}")
        self.assertIn("Commander",x["Chaos Warp"]["legality"])

    def test_rule_of_law_warp_first_spell_can_answer(self):
        r=response_window("Rule of Law","Chaos Warp")
        self.assertTrue(r["answer_action_allowed"])
        self.assertTrue(r["threat_removed_from_battlefield"])
        self.assertEqual(r["spell_count_after_action"],1)
        self.assertTrue(r["target_was_shuffled_then_random_replacement"])

    def test_rule_of_law_warp_second_spell_illegal(self):
        r=response_window("Rule of Law","Chaos Warp",spells_already_cast=1)
        self.assertFalse(r["answer_action_allowed"])
        self.assertFalse(r["answer_effective"])

    def test_otawara_channel_is_not_a_spell_and_ignores_spell_quota(self):
        r=response_window("Rule of Law","Otawara, Soaring City",spells_already_cast=1)
        self.assertTrue(r["answer_effective"])
        self.assertEqual(r["spell_count_after_action"],1)
        self.assertTrue(r["threat_can_be_recast_if_bounced"])

    def test_otawara_channel_from_hand_only(self):
        self.assertFalse(response_window("Rule of Law","Otawara, Soaring City",in_hand=False)["answer_action_allowed"])

    def test_warp_reveal_same_rule_of_law_is_not_a_guaranteed_out(self):
        r=response_window("Rule of Law","Chaos Warp",reveal="same_stax")
        self.assertTrue(r["target_was_shuffled_then_random_replacement"])
        self.assertFalse(r["answer_effective"])
        self.assertFalse(r["threat_removed_from_battlefield"])

    def test_warp_cascade_hit_blocked_by_still_active_rule_of_law(self):
        r=response_window("Rule of Law","Chaos Warp",abaddon_cascade_enabled=True)
        self.assertTrue(r["cascade_triggered_on_chaos_warp"])
        self.assertFalse(r["cascade_exiled_spell_cast_legal_before_warp_resolves"])

    def test_arcane_laboratory_equivalent_spelling(self):
        for name in ("Rule of Law","Arcane Laboratory"):
            r=response_window(name,"Chaos Warp",spells_already_cast=1)
            self.assertFalse(r["answer_action_allowed"])

    def test_swan_song_counters_enchantment_spell_but_not_resolved_permanent(self):
        self.assertTrue(response_window("Rule of Law","Swan Song",target_zone="stack")["threat_countered_on_stack"])
        self.assertFalse(response_window("Rule of Law","Swan Song")["answer_effective"])

    def test_force_of_negation_intercepts_null_rod_before_resolve(self):
        self.assertTrue(response_window("Null Rod","Force of Negation",target_zone="stack")["threat_countered_on_stack"])
        self.assertFalse(response_window("Null Rod","Force of Negation")["threat_removed_from_battlefield"])

    def test_existing_deadly_rollick_removes_creature_magistrate(self):
        self.assertTrue(response_window("Drannith Magistrate","Deadly Rollick")["threat_removed_from_battlefield"])
        self.assertFalse(response_window("Rule of Law","Deadly Rollick")["answer_effective"])

    def test_existing_pyroblast_not_answer_nonblue_resolved_stax(self):
        for name in STAX:
            self.assertFalse(response_window(name,"Pyroblast")["answer_effective"])

    def test_warp_can_answer_colorless_artifact_instead_of_spell_counter(self):
        self.assertTrue(response_window("Null Rod","Chaos Warp")["threat_removed_from_battlefield"])
        self.assertFalse(response_window("Null Rod","Swan Song")["answer_effective"])

    def test_rest_in_peace_exiled_cemetery_not_restored(self):
        r=response_window("Rest in Peace","Chaos Warp")
        self.assertTrue(r["threat_removed_from_battlefield"])
        self.assertFalse(r["already_exiled_graveyard_restored"])

    def test_warp_cannot_remove_an_on_stack_only_stax_spell(self):
        self.assertFalse(response_window("Rule of Law","Chaos Warp",target_zone="stack")["answer_effective"])

    def test_wrong_spell_count_and_unknown_stax_fail_closed(self):
        with self.assertRaises(ValueError):
            response_window("Unsupported Prison","Chaos Warp")
        with self.assertRaises(ValueError):
            response_window("Rule of Law","Chaos Warp",spells_already_cast=-1)

    def test_chaos_and_channel_costs_are_different_colors(self):
        self.assertEqual(COSTS["Chaos Warp"],(3,(0,0,1)))
        self.assertEqual(COSTS["Otawara, Soaring City"],(4,(1,0,0)))
        red=[("Mountain",False),("Ancient Tomb",False)]
        self.assertTrue(available_hand_answer(red,["Chaos Warp"],"Chaos Warp"))
        self.assertFalse(available_hand_answer(red,["Otawara, Soaring City"],"Otawara, Soaring City"))

    def test_channel_requires_otawara_still_in_hand_not_as_land(self):
        landfield=[("Otawara, Soaring City",False),("Island",False),
                   ("Swamp",False),("Mountain",False)]
        self.assertFalse(available_hand_answer(landfield,[],"Otawara, Soaring City"))

    def test_variant_seeded_access_reproducible(self):
        base=self.variants["warp_for_rakdos"]
        a=trial(base,621017,[4,6,8,10])
        b=trial(base,621017,[4,6,8,10])
        self.assertEqual(a,b)
        self.assertGreaterEqual(a[1],0)
        self.assertIn("chaos_warp_land_payable_as_first_spell",a[0][10])

    def test_no_challenger_changed_canonical_permissions(self):
        self.assertFalse(any(self.plan["authority"].values()))
        self.assertEqual(self.plan["matched_draw_source_opportunity"]["n_per_variant"],2000)


if __name__=="__main__":
    unittest.main()
