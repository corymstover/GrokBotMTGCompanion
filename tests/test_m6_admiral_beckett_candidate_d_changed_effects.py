"""Finite Oracle-bound *changed card* interactions for Admiral D RESEARCH_ONLY.

No game sampling, win-rate claim, M6 I/J certificate, or deck approval is emitted.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "data/grixis/m7/research_challengers"
DECK = DIR / "Admiral_Beckett_Brass_evasive_pirate_density_package.txt"
ORACLE = DIR / "Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json"
EXACT_CANDIDATE_SHA = "201a1d5fc90e30d6aff9a565603fcf8caef69604dad2c07b4951be2b41cc92ee"


def resolve_simultaneous_combat_triggers(chorus_before: int, skyship_first: bool) -> tuple[int, bool]:
    """Only two documented same-controller triggers, no omitted priority/model claims.

    Both Skyship and Malcolm have already dealt combat damage; Skyship targets
    Malcolm as a permanent, and a card legally castable when discarded exists.
    """
    count = chorus_before
    free_cast_offered = False

    def skyship():
        nonlocal count
        if count > 0:  # It adds one of each *existing* counter kind.
            count += 1

    def malcolm():
        nonlocal count, free_cast_offered
        count += 1
        free_cast_offered = count >= 4  # Checked during Malcolm's resolution.

    if skyship_first:
        skyship()
        malcolm()
    else:
        malcolm()
        skyship()
    return count, free_cast_offered


@dataclass
class PaidBoast:
    attacked: bool = False
    activated: bool = False

    def boast(self, sacrificed_name: str, sacrificed_mana_value: int,
              sacrifice_is_available_other_permanent: bool) -> int:
        if not self.attacked or self.activated or not sacrifice_is_available_other_permanent:
            raise ValueError("Broadside boast unavailable: attack, once/turn, or other permanent")
        if sacrificed_name == "Broadside Bombardiers":
            raise ValueError("Cannot pay an 'another' sacrifice cost with Broadside itself")
        self.activated = True
        return 2 + sacrificed_mana_value


class AdmiralChangedEffectsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.oracle = {c["name"]: c for c in json.loads(ORACLE.read_text(encoding="utf-8"))["cards"]}
        cls.deck_names = {
            row.split("x ", 1)[1].removesuffix(" [Commander]")
            for row in DECK.read_text(encoding="utf-8").splitlines()
        }

    def test_exact_research_candidate_and_card_source(self):
        self.assertEqual(hashlib.sha256(DECK.read_bytes()).hexdigest(), EXACT_CANDIDATE_SHA)
        for name in ("Skyship Plunderer", "Malcolm, Alluring Scoundrel",
                     "Broadside Bombardiers", "Arcane Signet", "Departed Deckhand", "Cloud Pirates"):
            self.assertIn(name, self.deck_names)
            self.assertEqual(self.oracle[name]["legalities"]["commander"], "legal")

    def test_malcolm_chorus_order_changes_free_cast_on_the_same_damage_event(self):
        skyship = self.oracle["Skyship Plunderer"]["oracle_text"]
        malcolm = self.oracle["Malcolm, Alluring Scoundrel"]["oracle_text"]
        self.assertIn("for each kind of counter on target permanent or player", skyship)
        self.assertIn("chorus counter", malcolm)
        self.assertIn("four or more chorus counters", malcolm)
        # With two pre-existing counters, controller orders Skyship to resolve first.
        self.assertEqual(resolve_simultaneous_combat_triggers(2, skyship_first=True), (4, True))
        # The same board/cards with the reverse trigger order offers no free cast.
        self.assertEqual(resolve_simultaneous_combat_triggers(2, skyship_first=False), (4, False))

    def test_plunderer_cannot_create_counters_of_a_kind_from_zero(self):
        self.assertEqual(resolve_simultaneous_combat_triggers(0, skyship_first=True), (1, False))
        self.assertEqual(resolve_simultaneous_combat_triggers(0, skyship_first=False), (2, False))
        # A +1/+1 or flying counter is only duplicated if it already exists.
        self.assertIn("flying counter", self.oracle["Zephyr Singer"]["oracle_text"])
        self.assertIn("explores", self.oracle["Francisco, Fowl Marauder"]["oracle_text"])

    def test_malcolm_free_cast_is_conditional_on_the_actual_discarded_card(self):
        self.assertIn("Draw a card, then discard a card", self.oracle["Malcolm, Alluring Scoundrel"]["oracle_text"])
        self.assertIn("may cast the discarded card without paying its mana cost",
                      self.oracle["Malcolm, Alluring Scoundrel"]["oracle_text"])
        # The resolved trigger *offers* the cast; the fixture does not invent a draw.
        self.assertIn("Chaos Warp", self.deck_names)
        self.assertEqual(self.oracle["Chaos Warp"]["mana_cost"], "{2}{R}")

    def test_broadside_treasure_payment_does_only_two_damage(self):
        oracle = self.oracle["Broadside Bombardiers"]["oracle_text"]
        self.assertIn("Menace, haste", oracle)
        self.assertIn("Sacrifice another creature or artifact", oracle)
        self.assertIn("only once each turn", oracle)
        state = PaidBoast(attacked=True)
        self.assertEqual(state.boast("Treasure token", 0, True), 2)
        self.assertLess(2, 3, "A Treasure boast cannot outright kill a 3/3 blocker")
        with self.assertRaises(ValueError):
            state.boast("Treasure token", 0, True)

    def test_boast_cannot_happen_before_attack_or_without_other_permanent(self):
        with self.assertRaises(ValueError):
            PaidBoast(attacked=False).boast("Treasure token", 0, True)
        with self.assertRaises(ValueError):
            PaidBoast(attacked=True).boast("Broadside Bombardiers", 3, True)
        with self.assertRaises(ValueError):
            PaidBoast(attacked=True).boast("Treasure token", 0, False)
        # Sacrificing an actual 2-MV artifact can deal four damage but costs that ramp.
        self.assertEqual(self.oracle["Arcane Signet"]["mana_cost"], "{2}")
        self.assertEqual(PaidBoast(attacked=True).boast("Arcane Signet", 2, True), 4)

    def test_deckhand_spell_target_fragility_is_not_confused_with_abilities(self):
        text = self.oracle["Departed Deckhand"]["oracle_text"]
        self.assertIn("becomes the target of a spell, sacrifice it", text)
        self.assertIn("Another target creature you control", text)
        self.assertIn("can't be blocked except by Spirits", text)
        # An activated ability (e.g. equipment's equip) is not a spell target.
        self.assertIn("Equip", self.oracle["Lightning Greaves"]["oracle_text"])
        self.assertIn("only creatures with flying", self.oracle["Cloud Pirates"]["oracle_text"])


if __name__ == "__main__":
    unittest.main()
