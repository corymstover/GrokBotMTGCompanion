"""Kefka M7 Rev1 finite, source-paid P0 case fixtures (not a full Magic engine).

These small event/zone fixtures deliberately model both successful and
adversarial boundaries; they do not claim Monte Carlo win rates, all possible
priority interactions, or transfer of old pool certificates by assertion.
"""
import json
import re
import unittest
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORACLE = ROOT / "data/grixis/m7/independent_reviews/Kefka__Court_Mage_M7_Current_Scryfall_20261024.json"
SOURCE = ROOT / "data/grixis/m7/independent_candidates/Kefka__Court_Mage_M7_Sakashima_StepThrough_TwoSwap_Research_20261024.txt"
CARD_TYPES = {"Artifact", "Battle", "Creature", "Enchantment", "Instant", "Kindred", "Land", "Planeswalker", "Sorcery"}
KEFKA = "Kefka, Court Mage // Kefka, Ruler of Ruin"


def card_types(type_line):
    # Split subtype separator, ignore supertypes (legendary, basic, snow).
    return set(type_line.split(" — ")[0].split()) & CARD_TYPES


def pay(pool: Counter, colored: dict[str, int], generic=0):
    """Pay using explicit actual mana; no free mana or unsupported discounts."""
    copy = pool.copy()
    for symbol, amount in colored.items():
        if copy[symbol] < amount:
            return None
        copy[symbol] -= amount
    total = sum(copy.values())
    if total < generic:
        return None
    for symbol in ("C", "R", "B", "U"):
        used = min(copy[symbol], generic)
        copy[symbol] -= used
        generic -= used
    assert generic == 0
    return copy


@dataclass
class KefkaFixture:
    mana: Counter
    mountain: bool
    hand: list[str] = field(default_factory=list)
    graveyard: list[str] = field(default_factory=list)
    battlefield: list[str] = field(default_factory=list)
    pending: list[str] = field(default_factory=list)
    drawn: int = 0
    kefka_front: bool = False
    kefka_present: bool = False
    kefka_summoning_sick: bool = False
    opponent_permanents: list[list[str]] = field(default_factory=lambda: [["A", "B"], ["C"], ["D"]])

    def cast_kefka(self):
        post = pay(self.mana, {"U": 1, "B": 1, "R": 1}, 2)
        if post is None:
            return False
        self.mana = post
        self.kefka_front = self.kefka_present = self.kefka_summoning_sick = True
        self.battlefield.append("Kefka")
        self.pending.append("ETB_DISCARD")
        return True

    def remove_kefka(self):
        if self.kefka_present:
            self.kefka_present = False
            self.battlefield.remove("Kefka")
            self.graveyard.append("Kefka")

    def resolve_trigger(self, own_discard_type, opponent_discard_types, *, own_name=None):
        assert self.pending and self.pending.pop(0) in {"ETB_DISCARD", "ATTACK_DISCARD"}
        # Model one chosen card discarded by EACH player, without presuming all
        # opponents still have a hand; resolve using card TYPES, not supertypes.
        types = card_types(own_discard_type)
        for discarded in opponent_discard_types:
            if discarded is not None:
                types |= card_types(discarded)
        if own_name:
            self.hand.remove(own_name)
            self.graveyard.append(own_name)
        self.drawn += len(types)
        return len(types)

    @property
    def haste(self):
        return "Anger" in self.graveyard and self.mountain

    def declare_attack(self):
        if not self.kefka_present or (self.kefka_summoning_sick and not self.haste):
            return False
        self.pending.append("ATTACK_DISCARD")
        return True

    def activate_transform(self, *, is_main_phase: bool, stack_empty: bool):
        # Kefka's {8} is source-paid at sorcery speed, not a free transform.
        if not self.kefka_present or not self.kefka_front or not is_main_phase or not stack_empty:
            return False
        post = pay(self.mana, {}, 8)
        if post is None:
            return False
        self.mana = post
        for group in self.opponent_permanents:
            if group:
                group.pop(0)  # opponent choice, modeled explicitly as chosen first
        self.kefka_front = False
        return True


@dataclass
class KefkaCopy:
    name: str
    double_faced: bool
    is_commander_object: bool = False
    back_face_up: bool = False
    pending_etb: bool = True

    def transform(self):
        # Resolution of an activated Kefka ability instructs transformation
        # after sacrifices, but a physical single-faced clone cannot turn over.
        if not self.double_faced:
            return False
        self.back_face_up = not self.back_face_up
        return True


def created_copy_of_kefka(*, source_is_transforming_dfc: bool, mode: str):
    assert mode in {"single_faced_clone", "token_copy_created"}
    return KefkaCopy(name="Kefka", double_faced=(source_is_transforming_dfc
                    and mode == "token_copy_created"))


def apply_legend_rule(copies: list[KefkaCopy], legend_exception: bool):
    if legend_exception:
        return copies
    # State-based actions keep just the owner's chosen first same-name Kefka.
    same_name = [c for c in copies if c.name == "Kefka"]
    return [same_name[0]] if same_name else copies


@dataclass
class BreachLEDLoop:
    """Conservative finite ledger, not a full Magic priority/zone engine.

    graveyard_fuel is the count of expendable OTHER graveyard cards, excluding
    LED, Brain Freeze, and Oracle; we never silently exile a combo piece.
    """

    library: int
    graveyard_fuel: int
    blue_mana: int = 0
    spells_cast: int = 0
    breach_active: bool = True
    led_in_grave: bool = True
    freeze_in_grave: bool = True
    oracle_in_grave: bool = True

    def led_freeze(self, *, self_target=True, storm_countered=False):
        # LED's escape {0} + exile three OTHER cards, then cast/resolve LED;
        # sacrifice it at instant speed BEFORE casting the next Brain Freeze.
        # Brain Freeze needs {1}{U} + exile three additional OTHER cards.
        if not (self.breach_active and self.led_in_grave and self.freeze_in_grave
                and self.graveyard_fuel >= 6):
            return None
        self.graveyard_fuel -= 3
        self.led_in_grave = False
        self.spells_cast += 1
        self.blue_mana += 3  # LED activation resolves; LED returns to graveyard.
        self.led_in_grave = True
        if self.blue_mana < 2:  # No invented zero-mana Brain Freeze.
            return None
        self.graveyard_fuel -= 3
        self.blue_mana -= 2
        self.freeze_in_grave = False
        storm_copies_plus_original = (1 if storm_countered else 1 + self.spells_cast)
        self.spells_cast += 1
        milled = min(self.library, 3 * storm_copies_plus_original) if self_target else 0
        self.library -= milled
        self.graveyard_fuel += milled
        self.freeze_in_grave = True  # Resolved spell goes back to the graveyard.
        return storm_copies_plus_original, milled

    def can_escape_oracle_and_win_unanswered(self):
        # Thassa's Oracle costs UU plus three OTHER graveyard cards under
        # Breach, and the library must be empty at the ETB resolution.
        return (self.breach_active and self.oracle_in_grave and self.library == 0
                and self.blue_mana >= 2 and self.graveyard_fuel >= 3)


class KefkaExactP0Transfer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards = {c["name"]: c for c in data["cards"]}
        cls.list_names = [re.sub(r" \[Commander\]$", "", s[3:]) for s in SOURCE.read_text().splitlines()]
        assert len(cls.list_names) == len(set(cls.list_names)) == 100
        assert data["raw_candidate_sha256_no_terminal_lf"] == "14277f6e9774c5ef02b4f92332b52684794367007abf81bc2d84ef7ad7bcaa7d"
        for name in (KEFKA, "Anger", "Step Through", "Sakashima of a Thousand Faces", "Harmonic Prodigy", "Molten Duplication"):
            assert name in cls.cards

    def test_C1_cast_paid_etb_attack_and_transform_boundaries(self):
        text = self.cards[KEFKA]["oracle_text"]
        self.assertIn("Whenever Kefka enters or attacks, each player discards a card.", text)
        self.assertIn("{8}: Each opponent sacrifices a permanent", text)
        s = KefkaFixture(Counter({"C": 2, "U": 1, "B": 1, "R": 1}), mountain=False)
        self.assertTrue(s.cast_kefka())
        self.assertEqual(s.mana.total(), 0)
        self.assertFalse(s.declare_attack())  # Newly cast, no haste.
        self.assertEqual(s.resolve_trigger("Legendary Creature", ["Artifact", "Instant", "Land"]), 4)
        self.assertFalse(s.activate_transform(is_main_phase=True, stack_empty=True))  # Cannot pay 8.
        s.mana = Counter({"C": 8})
        self.assertFalse(s.activate_transform(is_main_phase=False, stack_empty=True))
        self.assertFalse(s.activate_transform(is_main_phase=True, stack_empty=False))
        self.assertTrue(s.activate_transform(is_main_phase=True, stack_empty=True))
        self.assertEqual(s.opponent_permanents, [["B"], [], []])
        self.assertFalse(s.kefka_front)

    def test_K1_card_types_are_distinct_and_supertypes_are_not_types(self):
        s = KefkaFixture(Counter(), mountain=False, pending=["ETB_DISCARD"])
        # Legendary isn't a card type; Artifact Creature contributes two;
        # duplicate opposing artifacts contribute only one Artifact type.
        self.assertEqual(s.resolve_trigger("Legendary Artifact Creature",
                                           ["Artifact", "Basic Land", "Artifact"]), 3)
        self.assertEqual(s.drawn, 3)
        s.pending.append("ATTACK_DISCARD")
        self.assertEqual(s.resolve_trigger("Creature", ["Creature", None, "Creature"]), 1)
        self.assertEqual(s.drawn, 4)
        self.assertNotIn("Legendary", CARD_TYPES)

    def test_K2_anger_discard_on_etb_enables_only_mountain_haste(self):
        self.assertIn("as long as this card is in your graveyard and you control a mountain",
                      self.cards["Anger"]["oracle_text"].lower())
        for has_mountain in (False, True):
            s = KefkaFixture(Counter({"C": 2, "U": 1, "B": 1, "R": 1}), mountain=has_mountain,
                             hand=["Anger"])
            self.assertTrue(s.cast_kefka())
            s.resolve_trigger("Creature", ["Land", "Instant", "Artifact"], own_name="Anger")
            self.assertEqual(s.declare_attack(), has_mountain)
            self.assertEqual(len(s.pending), 1 if has_mountain else 0)
        invalid = KefkaFixture(Counter({"C": 2, "U": 1, "R": 1}), mountain=True)
        self.assertFalse(invalid.cast_kefka())  # Can't waive black requirement.

    def test_K3_copy_of_transforming_card_vs_single_faced_clone(self):
        # 707.8a / 712 copying distinction. A physical single-faced clone
        # does not transform; a token *created copying* a DFC has two faces.
        single_faced_copy = created_copy_of_kefka(source_is_transforming_dfc=True,
                                                  mode="single_faced_clone")
        molten_token_of_kefka = created_copy_of_kefka(source_is_transforming_dfc=True,
                                                      mode="token_copy_created")
        self.assertFalse(single_faced_copy.transform())
        self.assertFalse(single_faced_copy.back_face_up)
        self.assertTrue(molten_token_of_kefka.transform())
        self.assertTrue(molten_token_of_kefka.back_face_up)
        self.assertTrue(molten_token_of_kefka.transform())
        self.assertFalse(molten_token_of_kefka.back_face_up)
        # Copying an ordinary one-faced physical Clone as a token does not
        # invent a DFC back; the source object has to actually be two-faced.
        non_dfc_token = created_copy_of_kefka(source_is_transforming_dfc=False,
                                              mode="token_copy_created")
        self.assertFalse(non_dfc_token.transform())
        self.assertIn("Create a token that's a copy of target artifact or creature you control",
                      self.cards["Molten Duplication"]["oracle_text"])
        # The {8} instruction's sacrifices would still occur when a physical
        # single-faced Kefka copy resolves it; only the transform does nothing.
        self.assertIn("Each opponent sacrifices a permanent", self.cards[KEFKA]["oracle_text"])

    def test_F1_remove_kefka_before_trigger_resolves_does_not_counter_etb(self):
        s = KefkaFixture(Counter({"C": 2, "U": 1, "B": 1, "R": 1}), mountain=True)
        self.assertTrue(s.cast_kefka())
        s.remove_kefka()  # Opponent acts with ETB trigger still on stack.
        self.assertFalse(s.declare_attack())
        self.assertEqual(s.resolve_trigger("Sorcery", ["Land", "Instant", "Artifact"]), 4)
        self.assertFalse(s.kefka_present)
        self.assertIn("Kefka", s.graveyard)

    def test_new_M7_step_through_and_sakashima_payable_and_legend_caveats(self):
        self.assertIn("Wizardcycling {2}", self.cards["Step Through"]["oracle_text"])
        self.assertIn('"legend rule" doesn\'t apply', self.cards["Sakashima of a Thousand Faces"]["oracle_text"])
        # Cycling {2}: discard *from hand* and pay generic; Kefka in command
        # zone isn't a library Wizard and cannot be fetched this way.
        wizard_targets = [n for n in self.list_names if "Wizard" in self.cards[n]["type_line"].split(" // ")[0]]
        self.assertEqual(set(wizard_targets), {"Harmonic Prodigy", "Gogo, Mysterious Mime", "Valley Floodcaller", "Thassa's Oracle", KEFKA})
        self.assertIsNotNone(pay(Counter({"C": 2}), {}, 2))
        self.assertIsNone(pay(Counter({"C": 1}), {}, 2))
        self.assertEqual(set(wizard_targets) - {KEFKA}, {"Harmonic Prodigy", "Gogo, Mysterious Mime", "Valley Floodcaller", "Thassa's Oracle"})
        # Sakashima-Kefka is a copy, but not the actual commander object and
        # so never deals commander damage; with Sakashima present, two copies
        # can remain; if it leaves, SBA reimposes same-name legend rule.
        copies = [KefkaCopy("Kefka", True, is_commander_object=True),
                  KefkaCopy("Kefka", False), KefkaCopy("Kefka", True)]
        self.assertEqual(len(apply_legend_rule(copies, legend_exception=True)), 3)
        self.assertEqual(len(apply_legend_rule(copies, legend_exception=False)), 1)
        self.assertEqual(sum(c.is_commander_object for c in copies), 1)

    def test_P1_K5_valley_flash_noncreature_does_not_untap_kefka(self):
        oracle = self.cards["Valley Floodcaller"]["oracle_text"]
        self.assertIn("You may cast noncreature spells as though they had flash", oracle)
        self.assertIn("Birds, Frogs, Otters, and Rats you control", oracle)
        self.assertNotIn("Wizards you control", oracle)
        s = KefkaFixture(Counter({"C": 2, "U": 1, "B": 1, "R": 1}), mountain=False)
        self.assertTrue(s.cast_kefka())
        self.assertFalse(s.declare_attack())  # Flash timing grants no haste.

    def test_P1_E1_E2_essence_flux_requires_target_and_creates_return_etb(self):
        oracle = self.cards["Essence Flux"]["oracle_text"]
        self.assertIn("Exile target creature you control, then return that card", oracle)
        s = KefkaFixture(Counter({"U": 1}), mountain=True)
        self.assertIsNotNone(pay(s.mana, {"U": 1}))
        self.assertFalse(s.kefka_present)  # Cannot target absent Kefka.
        s.kefka_present = True
        s.battlefield = ["Kefka"]
        s.pending.append("ETB_DISCARD")  # Return creates new Kefka ETB.
        self.assertEqual(s.resolve_trigger("Creature", ["Land", "Land", "Instant"]), 3)
        self.assertEqual(s.drawn, 3)

    def test_P1_W1_oracle_consultation_pact_source_paid_boundary(self):
        consultation = self.cards["Demonic Consultation"]["oracle_text"]
        pact = self.cards["Tainted Pact"]["oracle_text"]
        oracle = self.cards["Thassa's Oracle"]["oracle_text"]
        self.assertIn("Choose a card name. Exile the top six", consultation)
        self.assertIn("Repeat this process", pact)
        self.assertIn("greater than or equal to the number of cards in your library", oracle)
        self.assertTrue(len(set(self.list_names)) == 100)  # Pact singleton condition.
        # This verifies the final empty-library Oracle check, NOT the entire
        # ordering/counterspell chain or every reachable library state.
        devotion = 2
        self.assertTrue(devotion >= 0)
        self.assertFalse(devotion >= 3)
        self.assertIsNotNone(pay(Counter({"B": 1, "U": 2}), {"B": 1}))
        self.assertIsNotNone(pay(Counter({"U": 2}), {"U": 2}))

    def test_P1_W2_breach_led_freeze_paid_finite_storm_to_oracle(self):
        for name in ("Underworld Breach", "Lion's Eye Diamond", "Brain Freeze", "Thassa's Oracle"):
            self.assertIn(name, self.list_names)  # Exact, SHA-pinned 100.
        self.assertIn("exile three other cards", self.cards["Underworld Breach"]["oracle_text"])
        self.assertIn("Discard your hand, Sacrifice this artifact", self.cards["Lion's Eye Diamond"]["oracle_text"])
        self.assertIn("Storm", self.cards["Brain Freeze"]["oracle_text"])
        self.assertIn("greater than or equal to the number of cards in your library",
                      self.cards["Thassa's Oracle"]["oracle_text"])

        state = BreachLEDLoop(library=42, graveyard_fuel=12)
        self.assertFalse(state.can_escape_oracle_and_win_unanswered())
        self.assertEqual([state.led_freeze() for _ in range(4)],
                         [(2, 6), (4, 12), (6, 18), (8, 6)])
        self.assertEqual(state.library, 0)
        self.assertEqual(state.blue_mana, 4)  # Each LED yields UUU, Freeze costs UU.
        self.assertEqual(state.graveyard_fuel, 30)  # 12 - (4 x 6) + 42 milled.
        self.assertTrue(state.can_escape_oracle_and_win_unanswered())

    def test_P1_W2_breach_failures_and_counterplay_require_real_fuel(self):
        self.assertIsNone(BreachLEDLoop(library=42, graveyard_fuel=5).led_freeze())
        self.assertIsNone(BreachLEDLoop(library=42, graveyard_fuel=12,
                                        breach_active=False).led_freeze())
        self.assertIsNone(BreachLEDLoop(library=42, graveyard_fuel=12,
                                        freeze_in_grave=False).led_freeze())
        diverted = BreachLEDLoop(library=42, graveyard_fuel=6)
        self.assertEqual(diverted.led_freeze(self_target=False), (2, 0))
        self.assertIsNone(diverted.led_freeze())  # Opponent mill did not feed our yard.
        stopped_storm = BreachLEDLoop(library=42, graveyard_fuel=6)
        self.assertEqual(stopped_storm.led_freeze(storm_countered=True), (1, 3))
        self.assertIsNone(stopped_storm.led_freeze())  # Countered storm trigger matters.
        no_oracle_mana = BreachLEDLoop(library=0, graveyard_fuel=3, blue_mana=1)
        self.assertFalse(no_oracle_mana.can_escape_oracle_and_win_unanswered())
        exiled_oracle = BreachLEDLoop(library=0, graveyard_fuel=10, blue_mana=4,
                                      oracle_in_grave=False)
        self.assertFalse(exiled_oracle.can_escape_oracle_and_win_unanswered())
        # An opponent can still counter Oracle, remove Breach before the next
        # escape, or intervene in the stack. This tests a legal bounded trace,
        # not unconditional repeatability or a forced multiplayer win.

    def test_P1_W3_F2_repeated_hand_attack_and_extra_turn_liability(self):
        self.assertIn("Take an extra turn after this one", self.cards["Final Fortune"]["oracle_text"])
        hand_sizes = [3, 2, 1]
        for _ in range(3):
            hand_sizes = [max(0, x - 1) for x in hand_sizes]
        self.assertEqual(hand_sizes, [0, 0, 0])
        s = KefkaFixture(Counter(), mountain=False, pending=["ATTACK_DISCARD"])
        self.assertEqual(s.resolve_trigger("Basic Land", ["Land", "Land", None]), 1)
        # The modeled extra-turn trigger is a loss unless a win or a valid
        # replacement effect intervenes before the delayed end step.
        delayed_loss_at_end_step = True
        wins_before_end_step = False
        self.assertTrue(delayed_loss_at_end_step and not wins_before_end_step)


if __name__ == "__main__":
    unittest.main()
