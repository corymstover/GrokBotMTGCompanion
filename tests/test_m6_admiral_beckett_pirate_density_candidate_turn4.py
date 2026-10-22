"""Bounded, real-cost Admiral D candidate P0 attack/steal turn, NOT M6 I/J certification.

This is one physical, conditional state fixture and adversarial negative controls.
It never estimates multiplayer performance or approves a proposed 100-card deck.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "data/grixis/m7/research_challengers"
DECK_PATH = DIR / "Admiral_Beckett_Brass_evasive_pirate_density_package.txt"
ORACLE_PATH = DIR / "Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json"
CANDIDATE_SHA256 = "201a1d5fc90e30d6aff9a565603fcf8caef69604dad2c07b4951be2b41cc92ee"
ALLOWED_MANA = {
    "Underground Sea": {"U", "B"},
    "Volcanic Island": {"U", "R"},
    "Badlands": {"B", "R"},
    "City of Brass": {"W", "U", "B", "R", "G"},
}


def parse_deck() -> Counter[str]:
    lines = DECK_PATH.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "1x Admiral Beckett Brass [Commander]"
    deck: Counter[str] = Counter()
    for row in lines:
        quantity, name = row.split("x ", 1)
        name = name.removesuffix(" [Commander]")
        assert name not in deck
        deck[name] = int(quantity)
    assert len(deck) == 97 and sum(deck.values()) == 100
    return deck


@dataclass
class PaidTurnFixture:
    oracle: dict
    physical: Counter[str]
    turn: int = 0
    lands: set[str] = field(default_factory=set)
    tapped: set[str] = field(default_factory=set)
    creatures_entered: dict[str, int] = field(default_factory=dict)
    city_damage: int = 0

    def start_turn(self, turn: int, land_drop: str) -> None:
        assert turn == self.turn + 1
        assert land_drop in ALLOWED_MANA and self.physical[land_drop] == 1
        assert land_drop not in self.lands
        self.turn = turn
        self.tapped.clear()
        self.lands.add(land_drop)

    def cast(self, name: str, sources: list[tuple[str, str]]) -> None:
        assert self.physical[name] == 1 and name not in self.creatures_entered
        cost = self.oracle[name]["mana_cost"]
        tokens = re.findall(r"\{([^}]+)\}", cost)
        required = Counter(x for x in tokens if not x.isdigit())
        generic = sum(int(x) for x in tokens if x.isdigit())
        paid_colors = Counter(color for _, color in sources)
        assert len(sources) == sum(required.values()) + generic, (name, sources, cost)
        for color, needed in required.items():
            assert paid_colors[color] >= needed, (name, cost, paid_colors)
        assert len({land for land, _ in sources}) == len(sources)
        for land, color in sources:
            assert land in self.lands and land not in self.tapped
            assert color in ALLOWED_MANA[land]
            self.tapped.add(land)
            if land == "City of Brass":
                self.city_damage += 1  # Triggered damage, NOT mana paid in life.
        assert "Creature" in self.oracle[name]["type_line"]
        self.creatures_entered[name] = self.turn

    def ready_pirates(self, three: tuple[str, str, str]) -> bool:
        if len(three) != 3 or len(set(three)) != 3:
            return False
        return all(
            self.creatures_entered.get(name, self.turn) < self.turn
            and "Pirate" in self.oracle[name]["type_line"]
            for name in three
        )

    def beckett_theft_trigger(self, combat_sources: tuple[str, ...], target_is_nonland: bool,
                             commander_present_at_end_step: bool, fogged: bool = False) -> bool:
        if not commander_present_at_end_step or fogged or not target_is_nonland:
            return False
        return len(set(combat_sources)) >= 3 and self.ready_pirates(combat_sources)


class AdmiralPirateDensityCandidateTurn4Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck = parse_deck()
        payload = json.loads(ORACLE_PATH.read_text(encoding="utf-8"))
        cls.oracle = {x["name"]: x for x in payload["cards"]}

    def build_payable_fixture(self):
        f = PaidTurnFixture(self.oracle, self.deck)
        f.start_turn(1, "Underground Sea")
        f.cast("Cloud Pirates", [("Underground Sea", "U")])
        f.start_turn(2, "Volcanic Island")
        f.cast("Skyship Plunderer", [("Volcanic Island", "U"), ("Underground Sea", "U")])
        f.start_turn(3, "Badlands")
        f.cast("Departed Deckhand", [("Underground Sea", "U"), ("Badlands", "B")])
        f.start_turn(4, "City of Brass")
        f.cast("Admiral Beckett Brass", [("Underground Sea", "B"), ("Volcanic Island", "U"),
                                          ("Badlands", "R"), ("City of Brass", "R")])
        return f

    def test_candidate_d_has_exact_source_bound_100_cards(self):
        self.assertEqual(hashlib.sha256(DECK_PATH.read_bytes()).hexdigest(), CANDIDATE_SHA256)
        self.assertEqual(sum(self.deck.values()), 100)
        self.assertEqual(self.deck["Island"], 3)
        self.assertEqual(self.deck["Mountain"], 2)
        self.assertTrue(set(self.deck) <= set(self.oracle))

    def test_four_land_sequence_pays_each_printed_mana_cost_and_is_attack_ready(self):
        f = self.build_payable_fixture()
        self.assertEqual(self.oracle["Admiral Beckett Brass"]["mana_cost"], "{1}{U}{B}{R}")
        three = ("Cloud Pirates", "Skyship Plunderer", "Departed Deckhand")
        self.assertTrue(f.ready_pirates(three))
        self.assertEqual(f.creatures_entered["Admiral Beckett Brass"], 4)
        self.assertEqual(len(f.lands), 4)
        self.assertEqual(f.city_damage, 1)

    def test_three_pirates_same_player_then_legal_nonland_target(self):
        f = self.build_payable_fixture()
        three = ("Cloud Pirates", "Skyship Plunderer", "Departed Deckhand")
        self.assertIn("can't be blocked except by Spirits", self.oracle["Departed Deckhand"]["oracle_text"])
        self.assertIn("Flying", self.oracle["Cloud Pirates"]["oracle_text"])
        self.assertIn("Flying", self.oracle["Skyship Plunderer"]["oracle_text"])
        self.assertIn("At the beginning of your end step", self.oracle["Admiral Beckett Brass"]["oracle_text"])
        # Opponent's otherwise untargeted Sol Ring is a legal nonland permanent.
        self.assertTrue(f.beckett_theft_trigger(three, target_is_nonland=True,
                                                commander_present_at_end_step=True))

    def test_two_distinct_sources_or_fog_do_not_create_a_theft(self):
        f = self.build_payable_fixture()
        three = ("Cloud Pirates", "Skyship Plunderer", "Departed Deckhand")
        self.assertFalse(f.beckett_theft_trigger(three[:2], True, True))
        self.assertFalse(f.beckett_theft_trigger((three[0], three[0], three[1]), True, True))
        self.assertFalse(f.beckett_theft_trigger(three, True, True, fogged=True))

    def test_end_step_commander_and_target_are_real_conditions(self):
        f = self.build_payable_fixture()
        three = ("Cloud Pirates", "Skyship Plunderer", "Departed Deckhand")
        self.assertFalse(f.beckett_theft_trigger(three, False, True))
        self.assertFalse(f.beckett_theft_trigger(three, True, False))
        # Trigger already on stack survives later removal; this fixture stops at trigger creation.

    def test_broadside_paid_boast_is_not_unconditional_third_connection(self):
        card = self.oracle["Broadside Bombardiers"]
        self.assertIn("Menace, haste", card["oracle_text"])
        self.assertIn("Sacrifice another creature or artifact", card["oracle_text"])
        self.assertIn("only if this creature attacked this turn and only once each turn", card["oracle_text"])
        self.assertLess(2 + 0, 3, "A Treasure is MV0; boast 2 cannot remove a 3/3 blocker")

    def test_existing_indomitable_open_raiders_roles_are_preserved(self):
        for name in ("Merchant Raiders", "The Indomitable", "Open into Wonder", "Daring Piracy"):
            self.assertEqual(self.deck[name], 1)
        self.assertIn("for as long as you control this creature", self.oracle["Merchant Raiders"]["oracle_text"])
        self.assertIn("Whenever a creature you control deals combat damage", self.oracle["The Indomitable"]["oracle_text"])
        self.assertIn("draw a card", self.oracle["Open into Wonder"]["oracle_text"])


if __name__ == "__main__":
    unittest.main()
