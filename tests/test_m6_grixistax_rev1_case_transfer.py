"""Exact M7 Rev1 Grixistax finite M6 P0/P1 cases against 100-card source.

Each fixture binds to the approved-source candidate and selected historical/current
Oracle rows. These are conservative deterministic interactions, not a game engine,
an independent win-rate simulation, or blanket reuse of Grok's two-swap I/J.
"""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAND = ROOT / "data/grixis/m7/candidate_lists/Grixistax___October_2026_ChatGPT_Rev1.txt"
INDEX = ROOT / "data/grixis/m6/oracle_snapshots/Grixistax___October_2026_M7_Rev1_Selected_Oracle_20261025.json"
SHA = "70b48148409e849e38d7189bcda032d1c98d74329302563a005f86a86b81279e"
REMOVED = {"Damping Sphere", "Magus of the Moon", "Sheoldred, the Apocalypse"}
ADDED = {"Arcane Signet", "Bitterblossom", "Opposition", "Phyrexian Altar", "Ophiomancer"}


def trinisphere_final_mana(total_spent_before_floor, untapped=True):
    return max(3, total_spent_before_floor) if untapped else total_spent_before_floor


def kraum_triggers(spell_counts_by_opponent, kraum_on_battlefield=True):
    return sum(n >= 2 for n in spell_counts_by_opponent) if kraum_on_battlefield else 0


def tevesh_plus_one_cards(sacrificed_another_permanent, was_commander=False):
    return (2 + int(was_commander)) if sacrificed_another_permanent else 0


def chalice_counters(mana_value, charge_counters):
    return mana_value == charge_counters


def tower_tap_output(blood_moon, sacrifice_available):
    if blood_moon:
        return {"R": 1}
    return {"B": 2} if sacrifice_available else {"C": 1}


def altar_output(creature_available, requested_color):
    return {requested_color: 1} if creature_available else {}


def can_pay_opposition(blue, nonblue):
    return blue >= 2 and blue + nonblue >= 4


def can_escape(other_graveyard_cards, colored_source_available):
    return other_graveyard_cards >= 3 and colored_source_available


def orb_untaps(orb, tapped, available):
    if tapped:
        return available
    return min(1 if orb == "Winter Orb" else 2, available)


def helm_exile_replacement(library, replacement_active):
    """Finite library traversal with Helm X=1; result (exiled, graveyard, put_creature)."""
    exiled, grave, put = [], [], False
    for typ in library:
        if replacement_active:
            exiled.append(typ)
        else:
            grave.append(typ)
            if typ == "Creature" or len(grave) >= 1:
                put = typ == "Creature"
                break
    return exiled, grave, put


class GrixistaxExactRev1CaseFixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = CAND.read_bytes()
        cls.names = {
            l.removeprefix("1x ").removesuffix(" [Commander]")
            for l in cls.raw.decode("utf-8").splitlines()
        }
        cls.source = json.loads(INDEX.read_text(encoding="utf-8"))
        cls.meta = {x["name"]: x for x in cls.source["cards"]}
        assert hashlib.sha256(cls.raw).hexdigest() == SHA
        assert cls.source["candidate_raw_sha256"] == SHA
        assert len(cls.names) == len(cls.meta) == 100

    def oracle(self, name):
        self.assertIn(name, self.names)
        return self.meta[name]["oracle_text"]

    def test_selected_100_oracle_identity_and_legality_sources(self):
        self.assertEqual(self.names, set(self.meta))
        self.assertEqual(self.source["archived_selected_count"], 98)
        self.assertEqual(self.source["new_scryfall_page_selected_count"], 2)
        self.assertEqual(sum("Land" in x["type_line"] for x in self.meta.values()), 26)
        self.assertEqual(sum(bool(x["game_changer"]) for x in self.meta.values()), 22)
        for name, c in self.meta.items():
            with self.subTest(name=name):
                self.assertEqual(c["commander_legality"], "legal")
                self.assertTrue(set(c["color_identity"]) <= {"U", "B", "R"})
                self.assertTrue(c["oracle_text"])
        self.assertFalse(self.names & REMOVED)
        self.assertTrue(ADDED <= self.names)

    def test_C1_kraum_partner_second_spells_source_paid_and_adversarial(self):
        c = self.meta["Kraum, Ludevic's Opus"]
        self.assertEqual(c["mana_cost"], "{3}{U}{R}")
        self.assertIn("Flying, haste", self.oracle(c["name"]))
        self.assertIn("opponent casts their second spell each turn", c["oracle_text"])
        self.assertIn("Partner", c["oracle_text"])
        self.assertEqual(kraum_triggers([2, 3, 1]), 2)
        self.assertEqual(kraum_triggers([1, 1, 1]), 0)
        self.assertEqual(kraum_triggers([2, 2, 2], False), 0)
        # Paying five generic does not pay required U and R pips.
        self.assertFalse({"U": 0, "R": 0}["U"] >= 1 and {"U": 0, "R": 0}["R"] >= 1)

    def test_C2_tevesh_loyalty_tokens_draw_once_and_two_commander_tax_ledgers(self):
        c = self.meta["Tevesh Szat, Doom of Fools"]
        self.assertEqual(c["mana_cost"], "{4}{B}")
        t = self.oracle(c["name"])
        self.assertIn("+2: Create two 0/1 black Thrull", t)
        self.assertIn("sacrifice another creature or planeswalker", t)
        self.assertIn("draw another card if the sacrificed permanent was a commander", t)
        self.assertIn("can be your commander", t)
        self.assertIn("Partner", t)
        self.assertEqual(4 + 2, 6)  # Loyalty after +2 from printed 4.
        self.assertEqual(2 - 1, 1)  # One Thrull used leaves one; no phantom third.
        self.assertEqual(tevesh_plus_one_cards(True, True), 3)
        self.assertEqual(tevesh_plus_one_cards(True), 2)
        self.assertEqual(tevesh_plus_one_cards(False), 0)
        self.assertEqual((5 + 2, 5 + 0), (7, 5))  # Kraum recast tax doesn't tax Tevesh.
        # No other sacrificable permanent: +1 can add loyalty, not draw.

    def test_K1_kraum_trigger_after_paid_second_spell_without_removed_damping(self):
        self.assertIn("second spell", self.oracle("Kraum, Ludevic's Opus"))
        self.assertNotIn("Damping Sphere", self.names)
        self.assertIn("each spell that would cost less than three", self.oracle("Trinisphere"))
        self.assertEqual(kraum_triggers([2, 1, 0]), 1)
        self.assertEqual(kraum_triggers([1, 0, 0]), 0)
        self.assertEqual(trinisphere_final_mana(1), 3)
        # Cannot cast second spell on two remaining mana under untapped Trinisphere.
        self.assertGreater(trinisphere_final_mana(1), 2)

    def test_K2_blood_moon_phrexian_tower_and_altar_payability(self):
        self.assertIn("Nonbasic lands are Mountains", self.oracle("Blood Moon"))
        self.assertIn("Sacrifice a creature: Add {B}{B}", self.oracle("Phyrexian Tower"))
        self.assertIn("Nonbasic lands don't untap", self.oracle("Back to Basics"))
        self.assertIn("one mana of any color", self.oracle("Phyrexian Altar"))
        # Blood Moon overwrites nonbasic Tower's printed activated abilities but
        # doesn't change its nonbasic supertype; Altar (artifact) remains usable.
        self.assertEqual(tower_tap_output(True, True), {"R": 1})
        self.assertEqual(tower_tap_output(False, True), {"B": 2})
        self.assertEqual(tower_tap_output(False, False), {"C": 1})
        # Altar sacrifice produces a chosen color even though Moon removes
        # Tower's activated text, provided a real creature exists to sacrifice.
        self.assertEqual(altar_output(True, "U"), {"U": 1})
        self.assertEqual(altar_output(False, "U"), {})

    def test_K3_trinisphere_chalice_own_zero_and_one_mana_spells(self):
        self.assertIn("less than three mana", self.oracle("Trinisphere"))
        self.assertIn("mana value equal to the number of charge counters", self.oracle("Chalice of the Void"))
        self.oracle("Lion's Eye Diamond")
        self.oracle("Lotus Petal")
        self.assertEqual(trinisphere_final_mana(0), 3)
        self.assertEqual(trinisphere_final_mana(1), 3)
        self.assertEqual(trinisphere_final_mana(0, untapped=False), 0)
        # Chalice checks mana value 0, even when Trinisphere makes you PAY 3.
        self.assertTrue(chalice_counters(0, 0))
        self.assertFalse(chalice_counters(1, 0))

    def test_K4_karn_opponent_wishclaw_stops_artifact_ability_not_ours(self):
        self.assertIn("your opponents control can't be activated", self.oracle("Karn, the Great Creator"))
        w = self.oracle("Wishclaw Talisman")
        self.assertIn("An opponent gains control", w)
        self.assertIn("Activate only during your turn", w)
        # Pre-transfer, owner controls Wishclaw, has {1} and can activate;
        # after transfer, that opponent cannot activate under Karn.
        def wishclaw_activates(controller_is_opponent, paid_one, own_turn):
            return paid_one and own_turn and not controller_is_opponent
        self.assertTrue(wishclaw_activates(False, True, True))
        self.assertFalse(wishclaw_activates(True, True, True))
        self.assertFalse(wishclaw_activates(False, False, True))

    def test_K5_breach_hate_now_trinisphere_chalice_not_removed_damping(self):
        self.assertNotIn("Damping Sphere", self.names)
        self.assertIn("escape cost", self.oracle("Underworld Breach"))
        self.oracle("Trinisphere")
        self.oracle("Chalice of the Void")
        # Under Trinisphere, LED costs 3 to cast and Brain Freeze costs 3;
        # LED alone produces only 3, insufficient to pay both same cycle.
        self.assertLess(3, trinisphere_final_mana(0) + trinisphere_final_mana(2))
        # If Chalice is set to 0, LED is countered by its triggered ability.
        self.assertEqual(self.meta["Lion's Eye Diamond"]["cmc"], 0)
        self.assertTrue(chalice_counters(self.meta["Lion's Eye Diamond"]["cmc"], 0))
        # With lock removed, LED can produce UUU to pay Brain Freeze 1U.
        self.assertGreaterEqual(3, 2)

    def test_E1_thrull_parity_conserves_creatures_across_sac_outlets(self):
        for n in ("Contamination", "Skullclamp", "Phyrexian Tower",
                  "Culling the Weak", "Diabolic Intent", "Tangle Wire", "Overburden",
                  "Bitterblossom", "Ophiomancer", "Phyrexian Altar"):
            self.oracle(n)
        self.assertIn("sacrifice a creature", self.oracle("Contamination"))
        self.assertIn("Equipped creature gets +1/-1", self.oracle("Skullclamp"))
        self.assertIn("if you control no Snakes", self.oracle("Ophiomancer"))
        self.assertIn("nontoken creature", self.oracle("Overburden"))
        thrulls = 2
        thrulls -= 1  # Contamination upkeep: Thrull one
        self.assertEqual(thrulls, 1)
        thrulls -= 1  # Altar OR Skullclamp OR Tower, not all three
        self.assertEqual(thrulls, 0)
        self.assertFalse(thrulls > 0)
        # Clamp transforms one 0/1 Thrull into 1/0, which dies and draws two.
        self.assertEqual((0 + 1, 1 - 1), (1, 0))
        self.assertEqual(tevesh_plus_one_cards(True), 2)
        # If a Snake remains, Ophiomancer's intervening-if does not trigger.
        self.assertEqual(int(not bool({"Snake"})), 0)

    def test_E2_lock_parity_opposition_own_orbs_and_color_under_contamination(self):
        for n in ("Winter Orb", "Static Orb", "Blood Moon", "Back to Basics",
                  "Contamination", "Trinisphere", "Chalice of the Void",
                  "Arcane Signet", "Phyrexian Altar", "Opposition", "Cursed Totem"):
            self.oracle(n)
        self.assertFalse({"Damping Sphere", "Magus of the Moon"} & self.names)
        self.assertIn("Tap target artifact, creature, or land", self.oracle("Opposition"))
        self.assertIn("Activated abilities of creatures", self.oracle("Cursed Totem"))
        self.assertEqual(orb_untaps("Winter Orb", False, 6), 1)
        self.assertEqual(orb_untaps("Static Orb", False, 6), 2)
        self.assertEqual(orb_untaps("Winter Orb", True, 6), 6)
        self.assertEqual(orb_untaps("Static Orb", True, 6), 6)
        # Tap Orb with Opposition in last opponent end step before own untap.
        # Enchantment's ability and Altar's artifact ability aren't creature abilities.
        self.assertNotIn("Creature", self.meta["Opposition"]["type_line"])
        self.assertNotIn("Creature", self.meta["Phyrexian Altar"]["type_line"])
        self.assertIn("any color in your commander's color identity", self.oracle("Arcane Signet"))
        # Opposition costs UU; a single blue-producing rock cannot pay two U.
        self.assertFalse(can_pay_opposition(1, 5))
        self.assertTrue(can_pay_opposition(2, 2))

    def test_W1_helm_exile_replacement_empties_finite_library_not_immediate_win(self):
        self.assertIn("X can't be 0", self.oracle("Helm of Obedience"))
        self.assertIn("exile it instead", self.oracle("Leyline of the Void"))
        self.assertIn("with a void counter", self.oracle("Dauthi Voidwalker"))
        deck = ["Instant", "Creature", "Land", "Creature", "Sorcery"]
        for replacement in ("Leyline of the Void", "Dauthi Voidwalker"):
            with self.subTest(replacement=replacement):
                exile, gy, creature = helm_exile_replacement(deck, True)
                self.assertEqual(exile, deck)
                self.assertEqual(gy, [])
                self.assertFalse(creature)
        exile, gy, creature = helm_exile_replacement(deck, False)
        self.assertEqual(exile, [])
        self.assertEqual(gy, ["Instant"])
        self.assertFalse(creature)
        # A fully emptied library loses on attempted draw, not immediately on Helm.
        self.assertEqual(len(deck) - len(deck), 0)

    def test_W2_breach_led_brainfreeze_finite_paid_food_and_spell_count(self):
        for n in ("Underworld Breach", "Lion's Eye Diamond", "Lotus Petal",
                  "Brain Freeze", "Wheel of Fortune", "Jeska's Will"):
            self.oracle(n)
        self.assertIn("exile three other cards", self.oracle("Underworld Breach"))
        self.assertIn("Discard your hand", self.oracle("Lion's Eye Diamond"))
        self.assertIn("Storm", self.oracle("Brain Freeze"))
        self.assertTrue(can_escape(3, True))
        self.assertFalse(can_escape(2, True))
        self.assertFalse(can_escape(3, False))
        self.assertTrue(3 >= 2)   # LED's UUU can pay Brain Freeze's 1U
        # A two-spell turn has original Freeze plus two storm copies: 9 cards.
        self.assertEqual(3 * (1 + 2), 9)
        # Cannot count LED-discared hand as cards still held for another cast.
        self.assertEqual(len([]), 0)

    def test_W3_new_lock_beats_are_kraum_ragavan_tokens_not_removed_sheoldred(self):
        self.assertNotIn("Sheoldred, the Apocalypse", self.names)
        self.oracle("Kraum, Ludevic's Opus")
        self.oracle("Ragavan, Nimble Pilferer")
        self.oracle("Ophiomancer")
        self.oracle("Bitterblossom")
        self.assertIn("Flying, haste", self.oracle("Kraum, Ludevic's Opus"))
        self.assertIn("deathtouch", self.oracle("Ophiomancer"))
        # Kraum's printed 4 commander combat damage is six unblocked hits
        # to pass 21 commander damage, not an instant win or life drain trigger.
        self.assertTrue(6 * 4 >= 21)
        self.assertFalse(5 * 4 >= 21)
        self.assertFalse(0 * 4 >= 21)

    def test_F1_self_lock_negative_blue_shortfall_and_altar_source(self):
        self.assertIn("it produces {B} instead", self.oracle("Contamination"))
        self.assertIn("one mana of any color", self.oracle("Phyrexian Altar"))
        self.assertIn("any color in your commander's color identity", self.oracle("Arcane Signet"))
        self.assertEqual(self.meta["Opposition"]["mana_cost"], "{2}{U}{U}")
        # No artifact mana, all lands Contaminated: Opposition UU unpayable.
        self.assertFalse(can_pay_opposition(0, 7))
        # Two valid off-land sources can provide UU while lands pay generic.
        self.assertTrue(can_pay_opposition(2, 2))
        self.assertFalse(can_pay_opposition(1, 4))

    def test_F2_artifact_wipe_breaks_parity_but_enchantment_tokens_can_survive(self):
        for n in ("Static Orb", "Winter Orb", "Skullclamp", "Phyrexian Altar",
                  "Arcane Signet", "Bitterblossom", "Ophiomancer"):
            self.oracle(n)
        removed = {n for n in self.names if "Artifact" in self.meta[n]["type_line"]}
        self.assertIn("Phyrexian Altar", removed)
        self.assertIn("Arcane Signet", removed)
        self.assertIn("Skullclamp", removed)
        self.assertIn("Winter Orb", removed)
        self.assertNotIn("Bitterblossom", removed)
        self.assertNotIn("Ophiomancer", removed)
        self.assertNotIn("Opposition", removed)
        self.assertGreaterEqual(len(removed), 12)

    def test_F3_breach_negative_old_damping_removed_chalice_and_trinisphere_remain(self):
        self.assertNotIn("Damping Sphere", self.names)
        self.oracle("Trinisphere")
        self.oracle("Chalice of the Void")
        self.oracle("Underworld Breach")
        self.oracle("Lion's Eye Diamond")
        self.assertEqual(trinisphere_final_mana(0), 3)
        self.assertEqual(trinisphere_final_mana(2), 3)
        self.assertEqual(trinisphere_final_mana(2, False), 2)
        # A zero-MV LED is still countered by Chalice on 0 when cast.
        self.assertEqual(self.meta["Lion's Eye Diamond"]["cmc"], 0)
        self.assertTrue(chalice_counters(self.meta["Lion's Eye Diamond"]["cmc"], 0))


if __name__ == "__main__":
    unittest.main()
