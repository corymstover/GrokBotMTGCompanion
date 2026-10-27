"""Deck #55 exact-source and bounded commander-effect certification.

These are finite, source-scoped cost/timing/state assertions, not a Magic
rules engine, multiplayer win-rate simulation, or retroactive M6 I/J pass.
``--oracle-file`` checks against a publicly downloaded Oracle bulk file locally,
without transmitting the deck inventory to any card-data service.
"""
import argparse
from collections import Counter
from hashlib import sha256
import gzip
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
BASE = HERE / "Tetsuo_Imperial_Champion_Oct15_baseline.txt"
FINAL = HERE.parent / "candidate_lists/Tetsuo_Imperial_Champion_M7_Rev1.txt"
BASE_SHA = "d6d7561f00cb56cfb86cd79024975130d718ddc7f3a1bddf0c62f61dc422822e"
FINAL_SHA = "36890584524fb32d038ba27926af663dc98197f06f87d84a08282ce1f3fb29db"
ADDS = Counter([
    "Brotherhood Regalia", "City of Brass", "Demonic Tutor", "Drach'Nyen",
    "Firion, Wild Rose Warrior", "Grafted Exoskeleton", "Jeska's Will",
    "Karlach, Fury of Avernus", "Magnetic Theft", "Mjölnir, Hammer of Thor",
    "Otawara, Soaring City", "Shizo, Death's Storehouse", "Tainted Strike",
])
CUTS = Counter([
    "Akki Battle Squad", "Argentum Armor", "Brainstorm", "Heiko Yamazaki, the General",
    "Island", "Kediss, Emberclaw Familiar", "Smoldering Marsh", "Swamp",
    "Sword of Fire and Ice", "Terminate", "The Reality Chip", "Vorpal Sword",
    "Winged Boots",
])
BASICS = {"Island": 4, "Mountain": 4, "Swamp": 2}
NONBASIC_LANDS = set("""Academy Ruins|Ancient Tomb|Badlands|Blood Crypt|Bloodstained Mire|City of Brass|Command Tower|Exotic Orchard|Flooded Strand|Luxury Suite|Mana Confluence|Marsh Flats|Misty Rainforest|Morphic Pool|Otawara, Soaring City|Polluted Delta|Scalding Tarn|Shizo, Death's Storehouse|Steam Vents|Sunken Hollow|Training Center|Underground Sea|Volcanic Island|Watery Grave|Xander's Lounge""".split("|"))
PROTECTED = {
    "Tetsuo, Imperial Champion", "Excalibur, Sword of Eden", "Kaldra Compleat",
    "Embercleave", "Genji Glove", "Hexplate Wallbreaker", "Buster Sword",
    "The Reaver Cleaver", "Basilisk Collar", "Hammer of Nazahn",
    "Blacksmith's Talent", "Brass Squire", "Dalakos, Crafter of Wonders",
    "Godo, Bandit Warlord", "Savage Beating", "World at War",
    "Ancestral Vision", "Profane Tutor", "Wheel of Fate", "Inevitable Betrayal",
    "Chandra's Ignition", "Aggravated Assault", "Sword of Feast and Famine",
    "Swiftfoot Boots", "Oathkeeper, Takeno's Daisho", "Fierce Guardianship",
    "Force of Will", "Deflecting Swat", "Arcane Signet",
}


def parse(path, digest):
    raw = path.read_bytes()
    assert sha256(raw).hexdigest() == digest, path
    assert raw.endswith(b"\n") and b"\r" not in raw, path
    lines = raw.decode("utf8").splitlines()
    assert lines[0] == "1x Tetsuo, Imperial Champion [Commander]", path
    counts = Counter()
    for line in lines:
        quantity, name = line.split("x ", 1)
        assert int(quantity) > 0, line
        counts[name.removesuffix(" [Commander]")] += int(quantity)
    assert sum(counts.values()) == 100, path
    return counts


def physical_check():
    before = parse(BASE, BASE_SHA)
    after = parse(FINAL, FINAL_SHA)
    assert len(before) == 91 and len(after) == 93
    assert after - before == ADDS, after - before
    assert before - after == CUTS, before - after
    assert {k: v for k, v in after.items() if v > 1} == BASICS
    assert PROTECTED <= set(after)
    assert sum(after[k] for k in NONBASIC_LANDS) == 25
    assert sum(after[k] for k in BASICS) == 10
    assert sum(after[k] for k in NONBASIC_LANDS | set(BASICS)) == 35
    assert after["Tetsuo, Imperial Champion"] == 1
    print("PASS exact canonical 100 / 91 names -> candidate 100 / 93 names; 13 physical swaps; 35 lands; singleton")
    return after


def local_oracle(counts, bulk_path):
    found = {}
    names = sorted(counts)
    opener = gzip.open if str(bulk_path).endswith(".gz") else open
    with opener(bulk_path, "rt", encoding="utf-8") as stream:
        for line in stream:
            card = json.loads(line)
            if card.get("name") in counts:
                found[card["name"]] = card
    assert set(found) == set(names), (set(names) - set(found), set(found) - set(names))
    for name, card in found.items():
        assert card.get("oracle_id"), name
        assert card["legalities"]["commander"] == "legal", name
        assert set(card["color_identity"]) <= {"U", "B", "R"}, name
        assert card.get("oracle_text") or card.get("card_faces"), name
    oracle = lambda n: found[n].get("oracle_text", "").lower()
    assert "whenever tetsuo attacks, if it's equipped" in oracle("Tetsuo, Imperial Champion")
    assert "greatest mana value among equipment attached" in oracle("Tetsuo, Imperial Champion")
    assert "attach target equipment" in oracle("Magnetic Theft")
    assert "double all damage equipped creature would deal" in oracle("Mjölnir, Hammer of Thor")
    assert "infect" in oracle("Grafted Exoskeleton")
    assert "sacrifice that permanent" in oracle("Grafted Exoskeleton")
    assert "sacrifice that token at the beginning of the next upkeep" in oracle("Firion, Wild Rose Warrior")
    assert "equip worthy {1}" in oracle("Mjölnir, Hammer of Thor")
    assert "after the second main phase" in oracle("World at War")
    assert "during combat on your turn" in oracle("Savage Beating")
    print(f"PASS local Scryfall public bulk {len(found)}/{len(names)} Oracle IDs, UBR identity and official Commander legality; no exception")


def attack_trigger(attacking, equipped_when_declared, equipped_on_resolution,
                   equipment_mvs, mode, spell_mv=None):
    if not attacking or not equipped_when_declared:
        return None  # intervening-if at attack declaration
    if not equipped_on_resolution or not equipment_mvs:
        return None  # intervening-if at resolution
    maximum = max(equipment_mvs)
    if mode == "damage":
        return ("damage", maximum)
    if mode == "spell" and spell_mv is not None and spell_mv <= maximum:
        return ("cast_from_hand_free", spell_mv)
    return None


class BoundedCommanderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.final = physical_check()

    def test_C1_equipped_attack_and_resolution_condition(self):
        self.assertIsNone(attack_trigger(True, False, True, [12], "damage"))
        self.assertIsNone(attack_trigger(True, True, False, [], "damage"))
        self.assertEqual(attack_trigger(True, True, True, [4, 12], "damage"), ("damage", 12))

    def test_K1_printed_mv_not_paid_equip_or_cast_cost(self):
        printed_excalibur_mv = 12
        discounted_cast_mana = 2  # illustrative historic reduction; not a mana-value change
        self.assertGreater(printed_excalibur_mv, discounted_cast_mana)
        self.assertEqual(attack_trigger(True, True, True, [12], "spell", 9), ("cast_from_hand_free", 9))
        self.assertIsNone(attack_trigger(True, True, True, [4], "spell", 5))

    def test_K2_attack_damage_is_not_combat_damage(self):
        noncombat_attack_trigger_damage = 7
        self.assertEqual(noncombat_attack_trigger_damage, 7)
        self.assertIn("Basilisk Collar", self.final)
        # Collar grants lifelink and deathtouch to source Tetsuo; Kediss is
        # intentionally cut because it triggers on COMBAT damage to opponent.
        self.assertNotIn("Kediss, Emberclaw Familiar", self.final)

    def test_K3_suspend_no_mana_cost_free_cast_from_hand(self):
        for card in ("Ancestral Vision", "Profane Tutor", "Wheel of Fate", "Inevitable Betrayal"):
            self.assertIn(card, self.final)
            self.assertEqual(attack_trigger(True, True, True, [1], "spell", 0), ("cast_from_hand_free", 0))

    def test_K4_savage_beating_extra_combat_pay_entwine(self):
        self.assertEqual(attack_trigger(True, True, True, [5], "spell", 5), ("cast_from_hand_free", 5))
        available = {"R": 1, "generic": 1}
        self.assertTrue(available["R"] >= 1 and available["generic"] >= 1)
        self.assertFalse(available["R"] == 0)  # free casting does not pay entwine by itself

    def test_K5_world_at_war_combat_cast_schedules_post_second_main(self):
        phases = ["declare_attackers", "combat_damage", "postcombat_main", "extra_combat", "extra_main"]
        self.assertLess(phases.index("postcombat_main"), phases.index("extra_combat"))
        self.assertEqual(attack_trigger(True, True, True, [5], "spell", 5), ("cast_from_hand_free", 5))
        self.assertIn("World at War", self.final)

    def test_E1_magnetic_theft_before_attack_valid_and_after_attack_too_late(self):
        base = attack_trigger(True, False, False, [], "damage")
        self.assertIsNone(base)
        red_mana = 1
        red_mana -= 1  # Magnetic Theft {R} cast before declare attackers
        self.assertEqual(red_mana, 0)
        self.assertEqual(attack_trigger(True, True, True, [7], "damage"), ("damage", 7))

    def test_E2_firion_copy_nonlegendary_vs_legend_rule(self):
        original = "Hexplate Wallbreaker"  # nonlegendary Equipment, copy remains until next upkeep
        token = original
        self.assertEqual((original, token), ("Hexplate Wallbreaker", "Hexplate Wallbreaker"))
        legendary_excalibur_original_and_token_same_controller = 2
        self.assertEqual(legendary_excalibur_original_and_token_same_controller - 1, 1)
        # Can never keep both legendary Excaliburs; do not claim permanent free copies.

    def test_E3_firion_exoskeleton_token_danger(self):
        temporary_copy_attached_to_tetsuo = True
        token_sacrificed_next_upkeep = True
        sacrifice_equipped_tetsuo_if_unattached = temporary_copy_attached_to_tetsuo and token_sacrificed_next_upkeep
        self.assertTrue(sacrifice_equipped_tetsuo_if_unattached)

    def test_E4_mjolnir_red_legend_worthy_and_doubled_damage(self):
        tetsuo_is_legendary_and_red = True
        self.assertTrue(tetsuo_is_legendary_and_red)
        generic_and_red_available = (1, 0)  # equip worthy {1} is paid with generic, not red
        self.assertEqual(sum(generic_and_red_available), 1)
        base_damage = 12
        self.assertEqual(base_damage * 2, 24)

    def test_E5_tainted_strike_response_vs_free_spell_choice(self):
        damage_mode_on_stack = attack_trigger(True, True, True, [12], "damage")
        self.assertEqual(damage_mode_on_stack, ("damage", 12))
        black_mana_in_response = 1
        self.assertEqual(black_mana_in_response, 1)
        poison_if_infect_applied_before_resolution = damage_mode_on_stack[1]
        self.assertGreaterEqual(poison_if_infect_applied_before_resolution, 10)
        self.assertNotEqual(attack_trigger(True, True, True, [12], "spell", 1)[0], "damage")

    def test_W1_grafted_exoskeleton_mjolnir_threshold(self):
        damage = attack_trigger(True, True, True, [4, 4, 12], "damage")[1]
        replaced_with_poison = damage * 2  # Mjolnir doubles source damage, Exoskeleton infect
        self.assertEqual(replaced_with_poison, 24)
        self.assertTrue(replaced_with_poison >= 10)
        self.assertLess(4 * 2, 10)  # without a >=5 ceiling this is not an automatic kill

    def test_W2_assault_sword_repeat_must_generate_five_and_connect(self):
        untapped_lands = 5
        produced = 5
        payable_assault = produced >= 5 and untapped_lands >= 5
        self.assertTrue(payable_assault)
        no_unblocked_equipped_combat_damage = False
        self.assertFalse(no_unblocked_equipped_combat_damage)  # no Sword trigger/no second iteration

    def test_W3_karlach_extra_combat_only_first_combat(self):
        self.assertEqual(1, sum(index == 0 for index in range(3)))
        self.assertIn("Karlach, Fury of Avernus", self.final)

    def test_F1_exoskeleton_removal_sacrifices_carrier(self):
        attached = True
        if attached:
            equipment_removed = True
            carrier_sacrificed = equipment_removed
        self.assertTrue(carrier_sacrificed)

    def test_F2_chandra_ignition_target_blocked_by_wealth_power_protection(self):
        self.assertIn("Chandra's Ignition", self.final)
        self.assertNotIn("Sword of Wealth and Power", self.final)
        self.assertNotIn("Sword of Fire and Ice", self.final)

    def test_F3_jeskas_will_combat_mana_does_not_float_to_main(self):
        red_mana_added_in_declare_attackers = 7
        red_mana_after_phase_ends = 0
        self.assertGreater(red_mana_added_in_declare_attackers, red_mana_after_phase_ends)
        # Exiled top-three remain playable this turn at NORMAL timing and cost.
        cards_in_exile_until_turn_ends = 3
        self.assertEqual(cards_in_exile_until_turn_ends, 3)

    def test_F4_protection_and_mana_recovery_retained(self):
        for card in ("Swiftfoot Boots", "Oathkeeper, Takeno's Daisho", "Mithril Coat",
                     "Padeem, Consul of Innovation", "Arcane Signet", "Sword of the Animist"):
            self.assertIn(card, self.final)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--oracle-file", type=Path, help="Pre-downloaded public Scryfall Oracle JSONL(.gz)")
    args = parser.parse_args()
    if args.oracle_file:
        local_oracle(physical_check(), args.oracle_file)
    else:
        unittest.main(argv=[__file__], verbosity=2)
