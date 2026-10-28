"""Deck 56 exact-M7-100 original P0 case transfer: finite event-state tests.

These cases examine the *causing spell/ability* of an event changed by a
replacement effect (CR 614.6). This is a deliberately bounded model, not a
Magic game engine, independent judge ruling or new M6 I/J certificate.
The initial 24-case review and its conservative K2 caveat remain archived.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import gzip
from hashlib import sha256
import json
from pathlib import Path
import unittest

from verify import physical, AUTHORIZED_FUTURE

PINNED_ORACLE_SHA256 = "2f8afacba1b8f5375723cdeec3bc00adb3c6b97d038acc6406fa774129d7cf0a"
REQUIRED_ORACLE = {
    "The Madcap Jester": ("whenever the madcap jester attacks", "spell or ability you control"),
    "Dauthi Voidwalker": ("would be put into an opponent's graveyard", "exile it with a void counter"),
    "Uba Mask": ("if a player would draw a card", "exiles that card face up instead"),
    "Brain Freeze": ("target player mills three cards", "storm"),
    "Wheel of Fortune": ("each player discards their hand", "draws seven cards"),
    "Opposition Agent": ("while they're searching", "they exile each card"),
    "Sire of Stagnation": ("whenever a land an opponent controls enters", "exiles the top two cards"),
}


@dataclass(frozen=True)
class LibraryEvent:
    """One replaced event; the original causing source stays identified."""

    source_controller: str | None
    source_kind: str  # spell, ability, or game_draw
    library_owner: str
    count: int
    original_destination: str
    replacement: str | None = None

    @property
    def resulting_destination(self) -> str:
        if self.replacement in {"dauthi", "uba_mask"}:
            return "exile"
        return self.original_destination

    @property
    def exile_count(self) -> int:
        return self.count if self.resulting_destination == "exile" else 0

    def jester_permission_triggers(self, jester_present: bool) -> bool:
        # CR 614.6: original event replaced; modified event happens instead.
        # The event's *causing spell/ability* remains the original source.
        return (jester_present and self.source_controller == "us"
                and self.source_kind in {"spell", "ability"}
                and self.library_owner != "us" and self.exile_count > 0)


def scan_oracle_bulk(path: Path):
    """Check 7 present/hypothetical cards by pinned exact Oracle bytes."""
    assert sha256(path.read_bytes()).hexdigest() == PINNED_ORACLE_SHA256, path
    found = {}
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            card = json.loads(line)
            name = card.get("name")
            if name in REQUIRED_ORACLE and name not in found:
                found[name] = card
    assert set(found) == set(REQUIRED_ORACLE), sorted(set(REQUIRED_ORACLE) - set(found))
    for name, snippets in REQUIRED_ORACLE.items():
        card = found[name]
        assert card.get("oracle_id"), name
        text = (card.get("oracle_text") or "").lower()
        for snippet in snippets:
            assert snippet in text, (name, snippet, text)
    assert found["The Madcap Jester"]["legalities"]["commander"] == "not_legal"
    assert found["Dauthi Voidwalker"]["legalities"]["commander"] == "legal"
    assert found["Opposition Agent"]["cmc"] == 3
    assert found["Sire of Stagnation"]["cmc"] == 6
    print("PASS pinned-current bulk SHA and seven named Oracle, UBR/exception checks")


class OriginalM6P0Followup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck = physical()

    def test_P0_C1_attack_trigger_and_live_source_window(self):
        # Three independent opponent top objects, each uniquely identified.
        exile = [LibraryEvent("us", "ability", o, 1, "exile")
                 for o in ("opponent_A", "opponent_B", "opponent_C")]
        self.assertEqual(sum(e.exile_count for e in exile), 3)
        self.assertTrue(all(e.jester_permission_triggers(True) for e in exile))
        self.assertFalse(any(e.jester_permission_triggers(False) for e in exile))
        self.assertEqual({e.library_owner for e in exile},
                         {"opponent_A", "opponent_B", "opponent_C"})

    def test_P0_K1_any_mana_type_does_not_waive_costs_or_timing(self):
        self.assertIn("The Madcap Jester", self.deck)
        stolen_spell_mana_value = 3  # Hypothetical off-color {2}{G} spell.
        mana_on_hand = {"R": 2, "C": 1, "G": 0}
        self.assertTrue(sum(mana_on_hand.values()) >= stolen_spell_mana_value)
        self.assertEqual(mana_on_hand["G"], 0)  # Jester permits R as green.
        self.assertFalse(2 >= stolen_spell_mana_value)  # Not free casting.
        regular_sorcery_window, unused_land_drop = False, False
        self.assertFalse(regular_sorcery_window)
        self.assertFalse(unused_land_drop)

    def test_P0_K2_dauthi_modified_mill_preserves_causing_spell_identity(self):
        self.assertIn("Dauthi Voidwalker", self.deck)
        self.assertIn("Brain Freeze", self.deck)
        brain_freeze_we_control = LibraryEvent("us", "spell", "opponent_A", 3,
                                             "graveyard", "dauthi")
        self.assertEqual(brain_freeze_we_control.resulting_destination, "exile")
        self.assertEqual(brain_freeze_we_control.exile_count, 3)
        self.assertTrue(brain_freeze_we_control.jester_permission_triggers(True))
        self.assertFalse(brain_freeze_we_control.jester_permission_triggers(False))
        # Dauthi's replacement being ours does NOT independently make an
        # opponent-controlled milling spell into a source we control.
        opposing_mill = LibraryEvent("opponent_A", "spell", "opponent_B", 3,
                                    "graveyard", "dauthi")
        self.assertEqual(opposing_mill.exile_count, 3)
        self.assertFalse(opposing_mill.jester_permission_triggers(True))
        self.assertEqual(LibraryEvent("us", "spell", "opponent_A", 3,
                                      "graveyard").exile_count, 0)

    def test_P0_K3_uba_mask_alone_is_not_controlled_cause(self):
        # The turn-based draw is a game action, not our spell or ability.
        # Uba Mask changes its destination but does not fabricate the source.
        self.assertNotIn("Uba Mask", self.deck)
        ordinary_opponent_draw = LibraryEvent(None, "game_draw", "opponent_A", 1,
                                              "hand", "uba_mask")
        self.assertEqual(ordinary_opponent_draw.exile_count, 1)
        self.assertFalse(ordinary_opponent_draw.jester_permission_triggers(True))
        our_wheel = LibraryEvent("us", "spell", "opponent_A", 7,
                                "hand", "uba_mask")
        self.assertTrue(our_wheel.jester_permission_triggers(True))
        opponent_wheel = LibraryEvent("opponent_B", "spell", "opponent_A", 7,
                                     "hand", "uba_mask")
        self.assertFalse(opponent_wheel.jester_permission_triggers(True))
        our_own_draw = LibraryEvent("us", "spell", "us", 7,
                                   "hand", "uba_mask")
        self.assertFalse(our_own_draw.jester_permission_triggers(True))

    def test_P0_F1_slow_sire_vs_agent_cost_response_and_not_auto_jester(self):
        self.assertIn("Opposition Agent", self.deck)
        self.assertNotIn("Sire of Stagnation", self.deck)
        agent_cost = {"B": 1, "generic": 2}
        sire_cost = {"B": 1, "U": 1, "generic": 4}
        self.assertEqual((sum(agent_cost.values()), sum(sire_cost.values())), (3, 6))
        opponent_searches, three_mana, six_mana = True, True, False
        self.assertTrue(opponent_searches and three_mana)
        self.assertFalse(six_mana)
        # Agent's search/exile does not turn every opponent search into a
        # credited spell/ability WE control for Jester; never count it free.
        opponent_search_event = LibraryEvent("opponent_A", "ability", "opponent_A",
                                            1, "exile")
        self.assertFalse(opponent_search_event.jester_permission_triggers(True))
        self.assertEqual(AUTHORIZED_FUTURE, {"The Madcap Jester", "Dragon's Smile"})


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--oracle-file", type=Path)
    args = parser.parse_args()
    physical()
    if args.oracle_file:
        scan_oracle_bulk(args.oracle_file)
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(OriginalM6P0Followup))
    raise SystemExit(0 if result.wasSuccessful() else 1)
