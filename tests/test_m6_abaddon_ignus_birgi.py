"""Adversarial finite Grinning Ignus / Birgi / Abaddon conditional verification."""
import unittest
from scripts.grixis_m6_abaddon_ignus_birgi import (
    ignus_cycle,stormfist_upkeep,source_inventory,run
)


class AbaddonIgnusBirgi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan,cls.variants,cls.packet=source_inventory()

    def test_frozen_98_rows_63_unique_candidates(self):
        self.assertEqual(len(self.packet["items"]),98)
        self.assertEqual(len({i["add"] for i in self.packet["items"]}),63)
        self.assertEqual(set(self.variants),{"approved","ignus_for_rakdos",
            "ignus_for_nightscape_familiar","ignus_for_rite_of_flame"})

    def test_exact_100_and_immutable_physical_one_card_swaps(self):
        b=self.variants["approved"]
        self.assertEqual(len(b),99)
        self.assertNotIn("Grinning Ignus",b)
        for variant,library in self.variants.items():
            changes=[(x,y) for x,y in zip(b,library) if x!=y]
            self.assertEqual(len(changes),0 if variant=="approved" else 1)
            self.assertEqual(len(library),99)
            self.assertEqual(library.count("Grinning Ignus"),0 if variant=="approved" else 1)

    def test_core_birgi_retained_on_every_considered_physical_swap(self):
        for name,cards in self.variants.items():
            self.assertEqual(cards.count("Birgi, God of Storytelling // Harnfel, Horn of Bounty"),1,name)

    def test_five_finite_loops_are_mana_neutral_with_birgi(self):
        d=ignus_cycle(iterations=5)
        self.assertEqual(d["recasts"],5)
        self.assertEqual(d["birgi_red_triggers"],5)
        self.assertEqual(d["mana_pool_red"],1)
        self.assertEqual(d["mana_pool_colorless"],0)
        self.assertTrue(d["can_continue"])

    def test_abaddon_requires_opponent_life_loss_at_least_three(self):
        d=ignus_cycle(opponent_life_lost=2)
        self.assertEqual(d["recasts"],5)
        self.assertEqual(d["abaddon_cascade_triggers"],0)
        self.assertEqual(ignus_cycle(opponent_life_lost=3)["abaddon_cascade_triggers"],5)
        self.assertEqual(ignus_cycle(opponent_life_lost=0)["abaddon_cascade_triggers"],0)

    def test_commander_and_turn_bounded_hand_cast_requirement(self):
        self.assertEqual(ignus_cycle(abaddon_controlled=False)["abaddon_cascade_triggers"],0)
        other=ignus_cycle(ignus_from_hand=False,lost_present=True)
        self.assertEqual(other["abaddon_cascade_triggers"],0)
        self.assertEqual(other["lost_spawn_triggers"],1)
        self.assertFalse(other["can_continue"])

    def test_no_birgi_or_back_face_breaks_mana_neutrality(self):
        d=ignus_cycle(birgi_front=False)
        self.assertEqual(d["recasts"],1)
        self.assertEqual(d["mana_pool_red"],0)
        self.assertFalse(d["can_continue"])
        self.assertEqual(d["abaddon_cascade_triggers"],1)

    def test_rule_of_law_blocks_repeated_cascade(self):
        d=ignus_cycle(rule_of_law=True)
        self.assertEqual(d["recasts"],1)
        self.assertEqual(d["abaddon_cascade_triggers"],1)
        self.assertFalse(d["can_continue"])

    def test_nightscape_familiar_increases_colorless_not_red(self):
        d=ignus_cycle(familiar=True)
        self.assertEqual(d["recasts"],5)
        self.assertEqual(d["mana_pool_colorless"],5)
        self.assertEqual(d["mana_pool_red"],1)

    def test_no_initial_red_prevents_loop(self):
        d=ignus_cycle(initial_red=0)
        self.assertEqual(d["recasts"],0)
        self.assertEqual(d["abaddon_cascade_triggers"],0)

    def test_extra_life_loss_does_not_create_extra_ignus_cascade(self):
        self.assertEqual(ignus_cycle(opponent_life_lost=6)["abaddon_cascade_triggers"],5)
        self.assertEqual(ignus_cycle(opponent_life_lost=100)["abaddon_cascade_triggers"],5)

    def test_cascade_trigger_not_automatically_nonhand_cast_or_spawn(self):
        d=ignus_cycle(lost_present=True)
        self.assertEqual(d["abaddon_cascade_triggers"],5)
        self.assertEqual(d["lost_spawn_triggers"],0)

    def test_stormfist_three_opponents_funds_threshold_but_cards_given_away(self):
        d=stormfist_upkeep(opponents=3)
        self.assertEqual(d["opponent_life_lost"],3)
        self.assertTrue(d["enough_for_ignus_mv3_abaddon_cascade"])
        self.assertEqual(d["opponent_cards_drawn"],3)
        self.assertEqual(d["controller_cards_drawn"],1)
        self.assertTrue(d["cannot_be_treated_as_free_threshold"])

    def test_stormfist_two_opponents_not_enough_for_mv3_ignus(self):
        d=stormfist_upkeep(opponents=2)
        self.assertFalse(d["enough_for_ignus_mv3_abaddon_cascade"])

    def test_invalid_inputs_rejected(self):
        with self.assertRaises(ValueError): ignus_cycle(iterations=-1)
        with self.assertRaises(ValueError): ignus_cycle(opponent_life_lost=-1)
        with self.assertRaises(ValueError): stormfist_upkeep(opponents=0)

    def test_no_implicit_gameplay_or_approval(self):
        d=run()
        self.assertFalse(d["evidence_bounds"]["physical_100_card_gameplay_modeled"])
        self.assertFalse(d["evidence_bounds"]["net_improving_swap_proven"])
        self.assertIsNone(d["evidence_bounds"]["true_multiplayer_win_rate"])
        self.assertEqual(d["evidence_bounds"]["formal_M6_certificates"],0)
        self.assertEqual(d["evidence_bounds"]["M7_approved_decks"],0)
        self.assertFalse(d["evidence_bounds"]["canonical_changed"])
        self.assertFalse(any(self.plan["authority"].values()))


if __name__=="__main__":
    unittest.main()
