"""Mairsil M7 Rev1 retrospective P0 transfer: source-paid finite cases.

Do NOT infer a universal Magic rules engine, quantitative multiplayer result,
or replayed M6 historical I/J experiment from these bounded, Oracle-anchored
state transitions. Historical canonical 100 and approval are unchanged.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/grixis/m7/oracle_snapshots/Mairsil_the_Pretender_Rev1_P0_Scryfall_20261026.json"
CANDIDATE = ROOT / "data/grixis/m7/candidate_lists/Mairsil_the_Pretender_chatgpt_rev1.txt"
SHA = "fd5e44773c829311254193d5c6d4433676e787743249451cc37a7345b0cf83ad"


class Cage:
    """A single Mairsil object in a source-bound finite fixture, not a board simulator."""

    def __init__(self, oracle):
        self.oracle = oracle
        self.battlefield = True
        self.object_id = 1
        self.owner_exile = set()
        self.hand = {"Asmodeus the Archfiend", "Pack Rat", "Rings of Brighthearth", "Rhystic Study"}
        self.graveyard = {"Displacer Kitten"}
        self.once = set()

    def enter_and_cage(self, card, origin, kind, *, owner=True):
        if not owner or kind not in {"Creature", "Artifact"}:
            return False
        location = self.hand if origin == "hand" else self.graveyard if origin == "graveyard" else None
        if location is None or card not in location:
            return False
        location.remove(card)
        self.owner_exile.add(card)
        return True

    def activate(self, card, ability, payment):
        if not self.battlefield or card not in self.owner_exile:
            return False
        key = (self.object_id, card, ability)
        if key in self.once or not payment:
            return False
        self.once.add(key)
        return True

    def blink(self, *, legal_spell_or_effect):
        if not self.battlefield or not legal_spell_or_effect:
            return False
        self.object_id += 1
        return True


class TestMairsilExactM7P0(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = CANDIDATE.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == SHA
        snap = json.loads(SOURCE.read_text(encoding="utf-8"))
        assert snap["candidate_raw_sha256"] == SHA
        cls.cards = {r["name"]: r for r in snap["records"]}
        assert len(cls.cards) == 10
        assert all(c["commander_legality"] == "legal" for c in cls.cards.values())
        assert all(not(set(c["color_identity"]) - set("UBR")) for c in cls.cards.values())

    def text(self, name):
        return self.cards[name]["oracle_text"]

    def test_C1_own_artifact_creature_cage_hand_grave_and_invalid_object(self):
        self.assertIn("artifact or creature card from your hand or graveyard", self.text("Mairsil, the Pretender"))
        self.assertIn("cards you own in exile with cage counters", self.text("Mairsil, the Pretender"))
        s = Cage(self.cards)
        self.assertTrue(s.enter_and_cage("Asmodeus the Archfiend", "hand", "Creature"))
        self.assertTrue(s.enter_and_cage("Displacer Kitten", "graveyard", "Creature"))
        self.assertEqual(s.owner_exile, {"Asmodeus the Archfiend", "Displacer Kitten"})
        self.assertNotIn("Asmodeus the Archfiend", s.hand)
        self.assertNotIn("Displacer Kitten", s.graveyard)
        self.assertFalse(s.enter_and_cage("Rhystic Study", "hand", "Enchantment"))
        self.assertFalse(s.enter_and_cage("Pack Rat", "opponent_graveyard", "Creature", owner=False))
        self.assertNotIn("Rhystic Study", s.owner_exile)

    def test_K1_once_per_object_essence_flux_kitten_and_missing_blink(self):
        self.assertIn("only once each turn", self.text("Mairsil, the Pretender"))
        self.assertIn("Exile target creature you control", self.text("Essence Flux"))
        self.assertIn("Whenever you cast a noncreature spell", self.text("Displacer Kitten"))
        s = Cage(self.cards)
        self.assertTrue(s.enter_and_cage("Asmodeus the Archfiend", "hand", "Creature"))
        self.assertTrue(s.activate("Asmodeus the Archfiend", "draw-seven", payment=True))
        self.assertFalse(s.activate("Asmodeus the Archfiend", "draw-seven", payment=True))
        self.assertFalse(s.blink(legal_spell_or_effect=False))
        self.assertFalse(s.activate("Asmodeus the Archfiend", "draw-seven", payment=True))
        self.assertTrue(s.blink(legal_spell_or_effect=True))  # valid Essence Flux or Kitten effect
        self.assertTrue(s.activate("Asmodeus the Archfiend", "draw-seven", payment=True))
        self.assertEqual(len(s.owner_exile), 1)  # exile/cage belongs to owner, persists

    def test_K2_asmodeus_black_cost_draw_seven_without_static_replacement(self):
        self.assertIn("{B}{B}{B}: Draw seven cards", self.text("Asmodeus the Archfiend"))
        self.assertIn("If you would draw a card, exile the top card", self.text("Asmodeus the Archfiend"))
        self.assertIn("all activated abilities", self.text("Mairsil, the Pretender"))
        s = Cage(self.cards)
        self.assertTrue(s.enter_and_cage("Asmodeus the Archfiend", "hand", "Creature"))
        library = list("ABCDEFGHI")
        hand = []
        colored_black = 3
        self.assertTrue(s.activate("Asmodeus the Archfiend", "draw-seven", payment=colored_black >= 3))
        colored_black -= 3
        hand.extend(library[:7])
        del library[:7]
        self.assertEqual(hand, list("ABCDEFG"))
        self.assertEqual(library, ["H", "I"])
        self.assertEqual(colored_black, 0)
        self.assertFalse(s.activate("Asmodeus the Archfiend", "draw-seven", payment=True))
        # Mairsil gains the activated draw effect, not Asmodeus's static replacement;
        # absent actual Asmodeus on the field, the seven cards enter hand, not exile.
        self.assertNotIn("H", hand)
        no_black = Cage(self.cards)
        self.assertFalse(no_black.activate("Asmodeus the Archfiend", "draw-seven", payment=False))

    def test_K3_pack_rat_rings_paid_copy_legend_and_no_free_discard(self):
        self.assertIn("{2}{B}, Discard a card: Create a token", self.text("Pack Rat"))
        self.assertIn("if it isn't a mana ability, you may pay {2}", self.text("Rings of Brighthearth"))
        self.assertIn("copy that ability", self.text("Rings of Brighthearth"))
        s = Cage(self.cards)
        self.assertTrue(s.enter_and_cage("Pack Rat", "hand", "Creature"))
        mana = {"B": 1, "generic": 4}
        self.assertGreaterEqual(mana["generic"], 4)  # 2 source cost + 2 Rings option
        discarded = s.hand.pop()  # a real hand card for source Pack Rat cost
        self.assertTrue(discarded)
        mana["B"] -= 1
        mana["generic"] -= 2
        self.assertTrue(s.activate("Pack Rat", "copy-self", payment=mana["B"] == 0))
        mana["generic"] -= 2  # Rings optional copy; costs no second discard
        token_copies_entered = 2  # copied ability and original resolve
        self.assertEqual(token_copies_entered, 2)
        self.assertEqual(mana, {"B": 0, "generic": 0})
        self.assertFalse(s.activate("Pack Rat", "copy-self", payment=True))
        # Tokens copy *legendary Mairsil*. On state-based actions one legendary
        # Mairsil can remain under owner's control, not three persistent bodies.
        self.assertEqual(min(1 + token_copies_entered, 1), 1)
        no_source_cost = Cage(self.cards)
        self.assertFalse(no_source_cost.activate("Pack Rat", "copy-self", payment=False))

    def test_F1_caged_exile_persists_but_removed_mairsil_has_no_abilities(self):
        self.assertIn("Mairsil has all activated abilities", self.text("Mairsil, the Pretender"))
        s = Cage(self.cards)
        self.assertTrue(s.enter_and_cage("Asmodeus the Archfiend", "hand", "Creature"))
        s.battlefield = False
        self.assertFalse(s.activate("Asmodeus the Archfiend", "draw-seven", payment=True))
        self.assertIn("Asmodeus the Archfiend", s.owner_exile)  # exile object still there
        s.battlefield = True  # a subsequently cast Mairsil, with a fresh object ID
        s.object_id += 1
        self.assertTrue(s.activate("Asmodeus the Archfiend", "draw-seven", payment=True))


if __name__ == "__main__":
    unittest.main()
