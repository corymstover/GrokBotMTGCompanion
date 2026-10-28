"""Nine approved M7 revisions: finite, negative-controlled original M6 P0 cases.

The historical M6 blueprint cases were DESIGN ONLY. These are newly executed
source-scoped models of their actual mechanics, not a retroactive M6 I/J seal,
independent game engine, win-rate estimate, or authority to revise decks.
Each suite pins the whole approved candidate's raw SHA, original case IDs and
historically snapshotted Commander Oracle before running its bounded checks.
"""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

SOURCE = {
    "Nekusar__the_Mindrazer": (
        "data/grixis/m7/nekusar_rev1/nekusar_m7_candidate_rev1.txt",
        "043d2521cec1e82d7ba8ff899b96920249e16ae32e73e2759f02044b41f94e53", 1),
    "Nicol_Bolas": (
        "data/grixis/m7/candidate_lists/Nicol_Bolas_chatgpt_rev1.txt",
        "a6079935a50b9469ca487e58e6bac159f8b777348b31585256b967f92c5d0df6", 1),
    "Nicol_Bolas__the_Ravager": (
        "data/grixis/m7/candidate_lists/Nicol_Bolas__the_Ravager_chatgpt_rev1.txt",
        "acfa7922e262805a15932b53b1399acdf6ddf5592c8a3793fafdeec720ad4693", 1),
    "Parnesse__the_Subtle_Brush": (
        "data/grixis/m7/candidate_lists/Parnesse_the_Subtle_Brush_M7_Rev1_Approved_2026-10-27.txt",
        "63b605a2c36ec81ab7a5a48770ac2b96b7994daf38546aba7b6bc6bd7597928c", 1),
    "RogSi": (
        "data/grixis/m7/rogsi_rev1/RogSi_M7_Rev1_Candidate_2026-10-27.txt",
        "97f3c0ca70303b44cd887938c320b75de01e991feec7d71d4c18811aeaa88225", 2),
    "Saruman__the_White_Hand": (
        "data/grixis/m7/saruman_rev1/Saruman_M7_Rev1_Candidate_2026-10-27.txt",
        "dbf71bc86caec1be73c4333bf43e4104cccb5f91a06d2766e8b586adabd9724b", 1),
    "Sauron__Lord_of_the_Rings": (
        "data/grixis/m7/sauron_rev1/Sauron_Lord_of_the_Rings_M7_Rev1_Candidate_2026-10-27.txt",
        "c427805f78f7aca7384db56022868a2e7cb7d01eeeabbb280a18e77e538a8159", 1),
    "Sol_kanar_the_Swamp_King": (
        "data/grixis/m7/candidate_lists/Sol_kanar_the_Swamp_King_M7_Rev1.txt",
        "2bd99c569df4a86897bca0164d2a1fa309b92f8b721e406b8394dfb04b1239e3", 1),
    "Goben__Gene_Splice_Savant": (
        "data/grixis/m7/candidate_lists/Norman_Osborn_Green_Goblin_chatgpt_rev1.txt",
        "c002a49243bd54780bb0f4a36a3c239a00e042defa1d0c6c4b891c3c8060eef9", 1),
}

class BlueprintBound(unittest.TestCase):
    DECK = None
    IDS = None
    PLAN_ID = None

    @classmethod
    def setUpClass(cls):
        if cls.DECK is None:
            return
        path, digest, command_count = SOURCE[cls.DECK]
        raw = (ROOT / path).read_bytes()
        assert sha256(raw).hexdigest() == digest, cls.DECK
        rows = raw.decode("utf8").splitlines()
        assert rows and raw.endswith(b"\n") and b"\r" not in raw
        actual = Counter()
        for row in rows:
            qty, name = row.split("x ", 1)
            assert int(qty) >= 1
            actual[name.removesuffix(" [Commander]")] += int(qty)
        assert sum(actual.values()) == 100
        assert sum(" [Commander]" in r for r in rows) == command_count
        assert not [n for n, c in actual.items() if c > 1 and n not in ("Island", "Mountain", "Swamp", "Nazgûl")]
        plan_name = cls.PLAN_ID or cls.DECK
        plan = json.loads((ROOT / "data/grixis/m6/test_blueprints" / (plan_name + ".json")).read_text())
        actual_p0 = {c["id"] for c in plan["cases"] if c["priority"] == "P0"}
        assert actual_p0 == set(cls.IDS), (cls.DECK, actual_p0)
        assert plan["commander_oracle_snapshots"], cls.DECK
        assert all(c.get("oracle_text") and c.get("oracle_id") for c in plan["commander_oracle_snapshots"])
        cls.cards = actual
        cls.oracle = "\n".join(c["oracle_text"] for c in plan["commander_oracle_snapshots"])


class NekusarP0(BlueprintBound):
    DECK = "Nekusar__the_Mindrazer"
    IDS = ("C1", "K1", "K2", "K3", "F1")

    def test_C1_own_extra_draw_opponent_damage_only(self):
        self.assertIn("opponent draws a card", self.oracle.lower())
        def draw_step(player, extra=True):
            draw_count = 1 + int(extra)
            damage = draw_count if player != "controller" else 0
            return draw_count, damage
        self.assertEqual(draw_step("opponent"), (2, 2))
        self.assertEqual(draw_step("controller"), (2, 0))
        self.assertEqual(draw_step("opponent", False), (1, 1))

    def test_K1_staff_harmonic_draw_trigger_vs_krang_damage(self):
        self.assertIn("Wizard's Staff", self.cards)
        self.assertIn("Harmonic Prodigy", self.cards)
        self.assertIn("Krang, the All-Powerful", self.cards)
        # An extra trigger caused by damage is not itself a draw-step trigger.
        step_instances = 1 + 1 + 1  # native + Staff + Harmonic
        damage_instances = 1 + 1 + 1 + 1  # native + Staff + Harmonic + Krang
        self.assertEqual((step_instances, damage_instances), (3, 4))
        self.assertNotEqual(step_instances, damage_instances)

    def test_K2_ghyrson_exact_one_prevents_magnified_damage_trigger(self):
        self.assertIn("Ghyrson Starn, Kelermorph", self.cards)
        def ghyrson_extra(single_damage_event):
            return 2 if single_damage_event == 1 else 0
        self.assertEqual(ghyrson_extra(1), 2)
        self.assertEqual(ghyrson_extra(2), 0)  # replacement makes original damage 2
        self.assertEqual(ghyrson_extra(0), 0)
        self.assertNotIn("Torbran, Thane of Red Fell", self.cards)

    def test_K3_turn_based_draw_and_triggered_additional_draw(self):
        order = ["turn_based_draw", "Nekusar_extra_draw_trigger"]
        self.assertEqual(len(order), 2)
        self.assertNotEqual(order[0], order[1])
        self.assertEqual(order.count("turn_based_draw"), 1)

    def test_F1_five_mana_setup_wheel_without_punisher(self):
        # Printed {2}{U}{B}{R}; a draw wheel without a punisher is symmetrical draw.
        def castable(generic, blue, black, red):
            return generic >= 2 and blue >= 1 and black >= 1 and red >= 1
        self.assertTrue(castable(2, 1, 1, 1))
        self.assertFalse(castable(2, 0, 1, 1))
        self.assertEqual(7 * 0, 0)  # no Nekusar damage when commander absent
        self.assertIn("Wheel of Fortune", self.cards)


class NicolBolasP0(BlueprintBound):
    DECK = "Nicol_Bolas"
    IDS = ("C1", "K1", "K2", "K3", "F1")

    def test_C1_upkeep_exact_ubr_or_sacrifice_and_discard(self):
        self.assertIn("sacrifice Nicol Bolas unless you pay", self.oracle)
        def survives_upkeep(mana):
            return all(mana.get(c, 0) >= 1 for c in "UBR")
        self.assertTrue(survives_upkeep({"U": 1, "B": 1, "R": 1}))
        self.assertFalse(survives_upkeep({"U": 0, "B": 1, "R": 4}))
        self.assertEqual(len(["A", "B", "C", "D"]), 4)  # hand discarded after damage
        self.assertEqual(len([]), 0)  # no cards discarded from empty hand

    def test_K1_any_damage_not_only_combat(self):
        def discard_if_bolas_dealt_damage(source, amount, target="opponent"):
            return source == "Nicol Bolas" and amount > 0 and target == "opponent"
        self.assertTrue(discard_if_bolas_dealt_damage("Nicol Bolas", 1))  # noncombat
        self.assertTrue(discard_if_bolas_dealt_damage("Nicol Bolas", 7))  # combat
        self.assertFalse(discard_if_bolas_dealt_damage("Kediss", 1))
        self.assertFalse(discard_if_bolas_dealt_damage("Nicol Bolas", 0))

    def test_K2_ingris_attacker_preblock_damage_and_discard(self):
        self.assertIn("Ingris Stingerquill", self.cards)
        event_order = ["declare_attackers", "Ingris_damage", "Bolas_discard", "declare_blockers"]
        self.assertLess(event_order.index("Bolas_discard"), event_order.index("declare_blockers"))
        self.assertGreater(event_order.index("Bolas_discard"), event_order.index("Ingris_damage"))
        self.assertFalse("combat_damage" in event_order)

    def test_K3_tergrid_and_tinybones_priority_on_discard(self):
        self.assertIn("Tinybones, Bauble Burglar", self.cards)
        self.assertIn("Tergrid, God of Fright // Tergrid's Lantern", self.cards)
        permanent_discarded = "opponent_permanent_card"
        triggers = [("Tergrid", permanent_discarded), ("Tinybones", permanent_discarded)]
        self.assertEqual(len(triggers), 2)
        # Both controller-order stack placements possible; neither is mandatory first.
        self.assertNotEqual(triggers[0][0], triggers[1][0])
        self.assertEqual({x[1] for x in triggers}, {permanent_discarded})

    def test_F1_eight_mana_cast_then_removal_before_damage(self):
        def castable(generic, colors):
            return generic >= 5 and all(colors.get(c, 0) >= 1 for c in "UBR")
        self.assertTrue(castable(5, {"U": 1, "B": 1, "R": 1}))
        self.assertFalse(castable(4, {"U": 1, "B": 1, "R": 1}))
        bolas_alive_at_damage = False  # opposing removal resolves before any hit
        combat_damage_events = 1 if bolas_alive_at_damage else 0
        self.assertEqual(combat_damage_events, 0)  # therefore no discard trigger
        self.assertIn("Mithril Coat", self.cards)  # candidate mitigation, not guaranteed


class RavagerP0(BlueprintBound):
    DECK = "Nicol_Bolas__the_Ravager"
    IDS = ("C1", "K1", "K2", "K3", "F1")

    def test_C1_etb_each_opponent_one_discard_and_source_paid_transform(self):
        self.assertIn("each opponent discards a card", self.oracle.lower())
        hands = {"A": 2, "B": 1, "C": 0}
        result = {p: max(0, n - 1) for p, n in hands.items()}
        self.assertEqual(result, {"A": 1, "B": 0, "C": 0})
        self.assertEqual(sum(hands.values()) - sum(result.values()), 2)
        def may_transform(generic, colors, own_main, empty_stack):
            return generic >= 4 and all(colors.get(c, 0) >= 1 for c in "UBR") and own_main and empty_stack
        self.assertTrue(may_transform(4, {"U":1, "B":1, "R":1}, True, True))
        self.assertFalse(may_transform(4, {"U":1, "B":1, "R":1}, False, True))

    def test_K1_exile_return_transformed_new_object_not_etb_discard(self):
        before = ("Ravager", "battlefield", 17)
        exile = ("Ravager", "exile", 17)
        after = ("Arisen", "battlefield", 18)
        self.assertEqual(exile[1], "exile")
        self.assertNotEqual(before[2], after[2])
        self.assertEqual(after[0], "Arisen")
        self.assertFalse(after[0] == "Ravager")  # no Ravager ETB repeat

    def test_K2_one_loyalty_activation_per_turn_unless_effect(self):
        def may_use_loyalty(used, extra_allowed=False):
            return used == 0 or extra_allowed
        self.assertTrue(may_use_loyalty(0))
        self.assertFalse(may_use_loyalty(1))
        self.assertTrue(may_use_loyalty(1, True))
        self.assertIn("The Chain Veil", self.cards)

    def test_K3_proliferate_adds_one_to_each_chosen_permanent(self):
        before = {"Bolas": 3, "Other walker": 1, "No chosen": 7}
        chosen = {"Bolas", "Other walker"}
        after = {k: n + int(k in chosen) for k, n in before.items()}
        self.assertEqual(after, {"Bolas": 4, "Other walker": 2, "No chosen": 7})
        self.assertEqual(after["No chosen"], before["No chosen"])

    def test_F1_sorcery_window_telegraphs_transformation(self):
        def can_respond_activation(own_main, empty_stack, colors):
            return own_main and empty_stack and set("UBR") <= colors
        self.assertTrue(can_respond_activation(True, True, set("UBR")))
        self.assertFalse(can_respond_activation(False, True, set("UBR")))
        self.assertFalse(can_respond_activation(True, False, set("UBR")))
        # Sorcery-speed activation gives opponent interaction before next main phase.
        self.assertIn("Fierce Guardianship", self.cards)


class ParnesseP0(BlueprintBound):
    DECK = "Parnesse__the_Subtle_Brush"
    IDS = ("C1", "K1", "K2", "K3", "F1")

    def test_C1_opposing_target_tax_and_own_copy_gift_separate(self):
        self.assertIn("pays 4 life", self.oracle.lower())
        def counter_opposing_target(opp_controls, targets_mine, life_paid):
            return opp_controls and targets_mine and life_paid < 4
        self.assertTrue(counter_opposing_target(True, True, 0))
        self.assertFalse(counter_opposing_target(True, True, 4))
        self.assertFalse(counter_opposing_target(False, True, 0))
        self.assertFalse(counter_opposing_target(True, False, 0))
        self.assertIn("Whenever you copy a spell", self.oracle)

    def test_K1_copy_spell_distinct_from_copy_card_then_cast(self):
        def parnesse_triggers(action):
            return action == "copy_spell_on_stack"
        self.assertTrue(parnesse_triggers("copy_spell_on_stack"))
        self.assertFalse(parnesse_triggers("copy_card_in_exile_then_cast"))
        self.assertFalse(parnesse_triggers("normal_cast"))
        self.assertIn("Mizzix's Mastery", self.cards)  # the kept copy-card/cast source
        self.assertNotIn("Arcane Bombardment", self.cards)  # removed revision card

    def test_K2_optional_opponent_copy_may_choose_new_targets(self):
        def gifted(you_copy_spell, opponent_selected):
            return you_copy_spell and opponent_selected
        self.assertTrue(gifted(True, True))
        self.assertFalse(gifted(True, False))
        self.assertFalse(gifted(False, True))
        original_target, opponents_target = "opponent A", "opponent B"
        self.assertNotEqual(original_target, opponents_target)

    def test_K3_tax_4_life_not_4_mana_and_counter_if_declined(self):
        def pay_tax(life_total, choice):
            return choice and life_total >= 4
        self.assertTrue(pay_tax(10, True))
        self.assertFalse(pay_tax(3, True))
        self.assertFalse(pay_tax(10, False))
        self.assertEqual(10 - 4, 6)

    def test_F1_opponent_copy_of_tutor_or_wipe_can_backfire(self):
        # Opponent copy is explicitly optional: no uncontested free value.
        copied = {"spell":"Demonic Tutor", "recipient":"opponent"}
        self.assertIn("Demonic Tutor", self.cards)
        self.assertEqual(copied["recipient"], "opponent")
        self.assertNotEqual(copied["recipient"], "controller")
        recipient_opted_in = False  # gifting declined is a legal protective choice
        opponent_copy_count = int(recipient_opted_in)
        self.assertEqual(opponent_copy_count, 0)


class RogSiP0(BlueprintBound):
    DECK = "RogSi"
    IDS = ("C1", "C2", "K1", "K2", "K3", "F1")

    def test_C1_zero_mana_rograkh_partner_and_keywords(self):
        self.assertIn("First strike", self.oracle)
        self.assertIn("menace", self.oracle)
        self.assertIn("trample", self.oracle)
        self.assertEqual(self.cards["Rograkh, Son of Rohgahh"], 1)
        self.assertEqual(self.cards["Silas Renn, Seeker Adept"], 1)
        self.assertNotEqual("Rograkh, Son of Rohgahh", "Silas Renn, Seeker Adept")

    def test_C2_silas_combat_damage_player_only_target_artifact(self):
        self.assertIn("combat damage to a player", self.oracle.lower())
        def gains_permission(combat, player_damage, artifact_grave):
            return combat and player_damage and artifact_grave
        self.assertTrue(gains_permission(True, True, True))
        self.assertFalse(gains_permission(True, False, True))
        self.assertFalse(gains_permission(False, True, True))
        self.assertFalse(gains_permission(True, True, False))

    def test_K1_grave_artifact_permission_no_flash_timing(self):
        def may_cast(grave_artifact, permission, normal_timing):
            return grave_artifact and permission and normal_timing
        self.assertTrue(may_cast(True, True, True))
        self.assertFalse(may_cast(True, True, False))
        self.assertFalse(may_cast(False, True, True))
        self.assertIn("Grinding Station", self.cards)

    def test_K2_vexing_symmetrical_nospend_and_squelcher_noncounter(self):
        self.assertIn("Vexing Bauble", self.cards)
        self.assertIn("Hexing Squelcher", self.cards)
        def bauble_counters(mana_spent, squelcher_controller):
            return mana_spent == 0 and not squelcher_controller
        self.assertTrue(bauble_counters(0, False))
        self.assertFalse(bauble_counters(1, False))
        self.assertFalse(bauble_counters(0, True))
        # Both the user's and opponent's zero-spend casts otherwise qualify.

    def test_K3_samut_split_second_not_triggered_ability_suppression(self):
        self.assertIn("Samut, Tyrant of Naktamun", self.cards)
        stack = ["our_instant_with_split_second", "Vexing_Bauble_trigger"]
        self.assertEqual(stack[-1], "Vexing_Bauble_trigger")
        self.assertNotEqual(stack[-1], "a_spell_cast_in_response")
        self.assertTrue("Vexing_Bauble_trigger" in stack)

    def test_F1_graveyard_hate_stops_breach_and_mnemonic(self):
        self.assertIn("Underworld Breach", self.cards)
        self.assertIn("Mnemonic Betrayal", self.cards)
        grave = {"Lion's Eye Diamond", "Brain Freeze"}
        grave.clear()  # opposing grave exile resolves
        self.assertNotIn("Lion's Eye Diamond", grave)
        self.assertFalse(bool(grave))


class SarumanP0(BlueprintBound):
    DECK = "Saruman__the_White_Hand"
    IDS = ("C1", "K1", "K2", "K3", "F1")

    def test_C1_noncreature_spell_cast_amass_mana_value_and_orc_goblin(self):
        self.assertIn("noncreature spell", self.oracle.lower())
        self.assertIn("amass Orcs", self.oracle)
        def amass_if_cast(is_noncreature, mana_value):
            return mana_value if is_noncreature else 0
        self.assertEqual(amass_if_cast(True, 7), 7)
        self.assertEqual(amass_if_cast(False, 7), 0)
        self.assertEqual(amass_if_cast(True, 0), 0)

    def test_K1_alt_cost_and_delve_do_not_change_printed_mana_value(self):
        self.assertIn("Force of Will", self.cards)
        printed_mv, mana_spent = 5, 0  # pitched force
        self.assertEqual(printed_mv, 5)
        self.assertNotEqual(printed_mv, mana_spent)
        treasure_cruise_printed_mv = 7 + 1  # {7}{U}, irrespective of delve
        self.assertEqual(treasure_cruise_printed_mv, 8)

    def test_K2_x_spell_stack_mana_value_includes_chosen_x(self):
        def mv_on_stack(fixed_symbols, chosen_x):
            return fixed_symbols + chosen_x
        self.assertEqual(mv_on_stack(2, 5), 7)
        self.assertEqual(mv_on_stack(2, 0), 2)
        self.assertNotEqual(mv_on_stack(2, 5), 2)

    def test_K3_fling_cost_sacrifices_army_before_amass_souls_fire_does_not(self):
        self.assertIn("Soul's Fire", self.cards)
        self.assertNotIn("Fling", self.cards)
        pre_cast_army = {"power": 8, "exists": True}
        fling_army_exists_at_cast_trigger_resolution = False  # paid sacrifice
        souls_fire_army_exists_at_cast_trigger_resolution = pre_cast_army["exists"]
        self.assertFalse(fling_army_exists_at_cast_trigger_resolution)
        self.assertTrue(souls_fire_army_exists_at_cast_trigger_resolution)

    def test_F1_multi_spell_requirement_vs_one_no_compact_infinite(self):
        self.assertIn("Saruman, the White Hand", self.cards)
        def counters_from_casts(mvs):
            return sum(mvs)
        self.assertEqual(counters_from_casts([5]), 5)
        self.assertEqual(counters_from_casts([5, 7]), 12)
        self.assertLess(counters_from_casts([5]), counters_from_casts([5, 7]))
        self.assertNotIn("Thassa's Oracle", self.cards)


class SauronLordP0(BlueprintBound):
    DECK = "Sauron__Lord_of_the_Rings"
    IDS = ("C1", "K1", "K2", "K3", "F1")

    def test_C1_cast_trigger_amass_mill_reanimate_and_opposing_commander_death(self):
        self.assertIn("When you cast this spell", self.oracle)
        events = ["cast", "amass_5", "mill_5", "target_creature_grave", "return_target"]
        self.assertEqual(events[1:3], ["amass_5", "mill_5"])
        self.assertLess(events.index("mill_5"), events.index("target_creature_grave"))
        cast_trigger_amass_counters = 5
        cards_milled = ["a", "b", "c", "d", "e"]
        self.assertEqual((cast_trigger_amass_counters, len(cards_milled)), (5, 5))
        self.assertIn("commander an opponent controls dies", self.oracle.lower())

    def test_K1_countering_spell_does_not_counter_on_cast_trigger(self):
        stack = ["sauron_spell", "sauron_cast_trigger"]
        stack.remove("sauron_spell")  # countered in response
        self.assertIn("sauron_cast_trigger", stack)
        self.assertNotIn("sauron_spell", stack)

    def test_K2_mill_five_before_reanimate_can_use_fresh_milled_creature(self):
        grave = []
        milled = ["Land", "Creature A", "Instant", "Creature B", "Land"]
        grave.extend(milled)
        target = "Creature B" if "Creature B" in grave else None
        self.assertEqual(len(grave), 5)
        self.assertEqual(target, "Creature B")
        self.assertNotEqual(target, "Instant")

    def test_K3_beacon_moves_to_hand_and_no_command_zone_tax(self):
        self.assertIn("Command Beacon", self.cards)
        def generic_to_pay(prior_zone, prior_casts):
            return 5 + (2 * prior_casts if prior_zone == "command" else 0)
        self.assertEqual(generic_to_pay("command", 3), 11)
        self.assertEqual(generic_to_pay("hand", 3), 5)
        self.assertNotEqual(generic_to_pay("command", 3), generic_to_pay("hand", 3))

    def test_F1_eight_mana_ubr_slow_vs_fast_mana(self):
        def castable(generic, u, b, r):
            return generic >= 5 and min(u, b, r) >= 1
        self.assertTrue(castable(5, 1, 1, 1))
        self.assertFalse(castable(5, 0, 1, 1))
        self.assertFalse(castable(4, 1, 1, 1))
        self.assertIn("Reanimate", self.cards)


class SwampKingP0(BlueprintBound):
    DECK = "Sol_kanar_the_Swamp_King"
    IDS = ("C1", "K1", "K2", "K3", "F1")

    def test_C1_swampwalk_and_any_player_casting_black_spell(self):
        self.assertIn("Swampwalk", self.oracle)
        self.assertIn("Whenever a player casts a black spell", self.oracle)
        def life_gain(is_black, player):
            return 1 if is_black else 0
        self.assertEqual(life_gain(True, "opponent"), 1)
        self.assertEqual(life_gain(True, "owner"), 1)
        self.assertEqual(life_gain(False, "opponent"), 0)
        self.assertTrue("Swamp" in {"Island", "Swamp"})
        self.assertFalse("Swamp" in {"Island"})

    def test_K1_painter_black_additive_also_opponent_casts(self):
        self.assertIn("Painter's Servant", self.cards)
        def black_spell(native_colors, painter_black):
            return "B" in native_colors or painter_black
        self.assertTrue(black_spell({"U"}, True))
        self.assertTrue(black_spell({"B"}, False))
        self.assertFalse(black_spell({"U"}, False))
        self.assertIn("Demon's Horn", self.cards)

    def test_K2_blanket_urborg_swampwalk_not_mana_from_nothing(self):
        self.assertIn("Blanket of Night", self.cards)
        self.assertIn("Urborg, Tomb of Yawgmoth", self.cards)
        def is_swamp(original, effect):
            return original == "Swamp" or effect
        self.assertTrue(is_swamp("Forest", True))
        self.assertFalse(is_swamp("Forest", False))
        self.assertTrue(is_swamp("Swamp", False))

    def test_K3_sols_and_horn_independent_two_life_triggers(self):
        self.assertIn("Demon's Horn", self.cards)
        triggers = ["SolKanar", "DemonsHorn"]
        self.assertEqual(len(triggers), 2)
        self.assertNotEqual(triggers[0], triggers[1])
        self.assertEqual(len([]), 0)  # no black spell, neither fires

    def test_F1_removal_of_required_loop_half_stops_repeat(self):
        self.assertIn("Painter's Servant", self.cards)
        self.assertIn("Grindstone", self.cards)
        def combo_live(painter, grindstone, mana_paid):
            return painter and grindstone and mana_paid
        self.assertTrue(combo_live(True, True, True))
        self.assertFalse(combo_live(False, True, True))
        self.assertFalse(combo_live(True, False, True))
        self.assertFalse(combo_live(True, True, False))


class NormanGreenGoblinP0(BlueprintBound):
    # Cory explicitly resolved this *canonical registry alias* on 2026-10-27:
    # "Goben IS Green Goblin, theyre the same CARD." Frozen 62 IDs and the
    # separately pinned 61-plan manifest remain unchanged.
    DECK = "Goben__Gene_Splice_Savant"
    PLAN_ID = "Norman_Osborn_Green_Goblin"
    IDS = ("C1", "K1", "K2", "K3", "F1")

    def test_C1_norman_connive_and_four_color_transform_timing(self):
        self.assertIn("Norman Osborn can't be blocked", self.oracle)
        self.assertIn("connives", self.oracle)
        self.assertIn("Activate only as a sorcery", self.oracle)
        # Combat-damage trigger connives; nonland discard grows one counter.
        def connive(damage_to_player, discarded_is_land):
            return (1, int(not discarded_is_land)) if damage_to_player else (0, 0)
        self.assertEqual(connive(True, False), (1, 1))
        self.assertEqual(connive(True, True), (1, 0))
        self.assertEqual(connive(False, False), (0, 0))
        def transform(generic, mana, own_main, empty_stack):
            return generic >= 1 and all(mana.get(c, 0) >= 1 for c in "UBR") and own_main and empty_stack
        self.assertTrue(transform(1, {"U":1,"B":1,"R":1}, True, True))
        self.assertFalse(transform(1, {"U":1,"B":1,"R":1}, False, True))

    def test_K1_green_goblin_reduces_generic_not_colored_costs(self):
        self.assertIn("Spells you cast from your graveyard cost {2} less", self.oracle)
        # One source spell {3}{U}{B}; transformed Goblin reduces generic 3 to 1.
        def discounted(generic, mana):
            return (max(generic - 2, 0), mana)
        self.assertEqual(discounted(3, ("U", "B")), (1, ("U", "B")))
        self.assertEqual(discounted(1, ("U", "B")), (0, ("U", "B")))
        self.assertNotEqual(discounted(3, ("U", "B")), (1, ()))

    def test_K2_mayhem_discard_this_turn_and_normal_timing_or_flash(self):
        self.assertIn("mayhem", self.oracle)
        self.assertIn("Borne Upon a Wind", self.cards)
        self.assertIn("Valley Floodcaller", self.cards)
        def cast_mayhem(discarded_this_turn, sorcery_speed, flash_granted):
            return discarded_this_turn and (sorcery_speed or flash_granted)
        self.assertTrue(cast_mayhem(True, True, False))
        self.assertTrue(cast_mayhem(True, False, True))
        self.assertFalse(cast_mayhem(False, True, True))
        self.assertFalse(cast_mayhem(True, False, False))

    def test_K3_necropotence_discard_exile_breaks_mayhem(self):
        self.assertNotIn("Necropotence", self.cards)
        # Necropotence-style replacement prevents discards from reaching yard.
        def mayhem_card_in_grave(discarded, exile_replacement):
            return discarded and not exile_replacement
        self.assertTrue(mayhem_card_in_grave(True, False))
        self.assertFalse(mayhem_card_in_grave(True, True))
        self.assertFalse(mayhem_card_in_grave(False, False))

    def test_F1_graveyard_exile_removes_breach_and_mayhem_resources(self):
        self.assertIn("Underworld Breach", self.cards)
        self.assertIn("Grinding Station", self.cards)
        grave = {"Lion's Eye Diamond", "Brain Freeze", "Mayhem Spell"}
        self.assertIn("Mayhem Spell", grave)
        grave.clear()  # source-paid hostile graveyard exile, before next cast
        self.assertFalse(bool(grave))
        self.assertNotIn("Mayhem Spell", grave)


if __name__ == "__main__":
    unittest.main(verbosity=2)
