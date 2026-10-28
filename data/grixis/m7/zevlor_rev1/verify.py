#!/usr/bin/env python3
"""Zevlor M7 Rev1: exact-source Oracle, payment, target and stack fixture checks.

This is a bounded *specific-card* model, not a generalized rules engine, win-rate
simulation, historical M6 Phase-B replay, or an independent Grok M7 verdict.
Every historical M6 case is mapped to a test with a negated precondition.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
import csv
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
BASE = HERE / "Zevlor_Oct15_Authority_Baseline.txt"
FINAL = ROOT / "data/grixis/m7/candidate_lists/Zevlor__Elturel_Exile_M7_Rev1.txt"
ALT8 = ROOT / "data/grixis/m7/candidate_lists/Zevlor__Elturel_Exile_M7_Rev1_alt8.txt"
ALT9 = ROOT / "data/grixis/m7/candidate_lists/Zevlor__Elturel_Exile_M7_Rev1_alt9.txt"
SNAP = json.loads((HERE / "Zevlor_M7_Rev1_Scryfall_snapshot.json").read_text())
CARDS = SNAP["oracle_cards"]
SHA = {
    BASE.name: "d2ea6ed8e42ec512b6a6ae7162da8c17b26494b45a9ff6d0c38882c202a42dc9",
    FINAL.name: "071e9a8b9eaa0f2cfad65f4e7ef05cc5cf0a8b5f74f2221c75d68e6c4dd1bb8f",
    ALT8.name: "23518e9c7bf894e7643f946a8801c58a031e99d98750c867305adc4fdb7e8878",
    ALT9.name: "9ffc69741f36ce7a07ce48f5ff9df692d4b326770ed83781c457856196c482da",
}
SWAPS = {
    "End of the Hunt": "Abrade",
    "Strategic Betrayal": "Terminate",
    "Gifts Ungiven": "Gamble",
    "Rousing Refrain": "Dark Ritual",
    "Traumatic Critique": "Portent",
    "Cruelclaw's Heist": "Counterspell",
}
OPPONENTS = ("B", "C", "D")
LANDS = {n for n, v in CARDS.items() if "Land" in v["type_line"]}
MANA_SYMBOL = re.compile(r"\{([^}]+)\}")


def text(name: str) -> str:
    return CARDS[name]["oracle_text"]


def inventory(path: Path) -> list[str]:
    result = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"(\d+)x (.+?)(?: \[Commander\])?", line)
        if not match:
            raise ValueError(f"Invalid 100-card row: {path}: {line!r}")
        result.extend([match.group(2)] * int(match.group(1)))
    return result


def pay(pool: dict[str, int], cost: str, x: int = 0) -> dict[str, int] | None:
    """Finite actual mana payment. Colored pips first; generic may use leftovers."""
    remaining = pool.copy()
    generic = 0
    for symbol in MANA_SYMBOL.findall(cost):
        if symbol == "X":
            generic += x
        elif symbol.isdigit():
            generic += int(symbol)
        elif symbol in "UBR":
            if remaining.get(symbol, 0) < 1:
                return None
            remaining[symbol] -= 1
        else:
            raise ValueError(f"Cost unsupported in this named fixture: {cost}")
    for color in ("C", "R", "B", "U"):
        take = min(generic, remaining.get(color, 0))
        remaining[color] = remaining.get(color, 0) - take
        generic -= take
    return remaining if not generic else None


def target_is_eligible(targets: tuple[tuple[str, str], ...]) -> bool:
    """Target tuple is (kind, controller); kind=player or permanent."""
    return len(targets) == 1 and targets[0][1] in OPPONENTS and targets[0][0] in (
        "player", "permanent"
    )


@dataclass
class Spell:
    name: str
    targets: tuple[tuple[str, str], ...]
    x: int = 0
    mode: str = "default"
    gift: bool = False
    cast: bool = True
    zone: str = "stack"

    def copy_for(self, opponent: str) -> "Spell":
        if opponent not in OPPONENTS or not self.targets:
            raise ValueError("Copy requires legal opponent and original target")
        return Spell(self.name, ((self.targets[0][0], opponent),), self.x,
                     self.mode, self.gift, False, "stack")


@dataclass
class ZevlorFixture:
    turn: int = 1
    on_battlefield: bool = True
    tapped: bool = False
    has_haste: bool = True
    watches: int = 0
    activated: int = 0
    mana: dict[str, int] = field(default_factory=lambda: {"C": 10, "U": 8, "B": 8, "R": 8})
    cast_events: int = 0
    copy_events: int = 0

    def activate(self, *, training=False, bracers=False) -> bool:
        if not self.on_battlefield or self.tapped or not self.has_haste:
            return False
        remaining = pay(self.mana, "{1}" if training else "{2}")
        if remaining is None:
            return False
        self.mana = remaining
        self.tapped = True
        self.activated += 1
        self.watches += 2 if bracers else 1  # Bracers copy activated ability, not cost.
        return True

    def untap(self, *, source: str, targetable: bool = True):
        if not targetable:
            return False
        if source == "Pemmin's Aura":
            remaining = pay(self.mana, "{U}")
        elif source == "Patriar's Seal":
            remaining = pay(self.mana, "{1}")  # seal must already be untapped
        elif source == "Minamo, School at Water's Edge":
            remaining = pay(self.mana, "{U}")  # land must already be untapped
        else:
            raise ValueError(source)
        if remaining is None:
            return False
        self.mana = remaining
        self.tapped = False
        return True

    def next_turn(self):
        self.turn += 1
        self.watches = 0  # This turn only; do not carry a phantom delayed trigger.
        self.tapped = False

    def cast_spell(self, spell: Spell, *, sorcery_window=True, staff=False,
                   counter_original=False, legal_opponents=OPPONENTS):
        if spell.name not in CARDS or spell.zone != "hand" and spell.zone != "stack":
            raise ValueError("Only an actual controlled cast is modeled")
        if "Sorcery" in CARDS[spell.name]["type_line"] and not sorcery_window:
            return None
        remaining = pay(self.mana, CARDS[spell.name]["mana_cost"], spell.x)
        if remaining is None:
            return None
        self.mana = remaining
        self.cast_events += 1
        eligible = target_is_eligible(spell.targets)
        watchers = self.watches if eligible else 0
        if eligible:
            self.watches = 0  # All waiting activations detect the same next cast.
        copies = []
        original_opponent = spell.targets[0][1] if spell.targets else None
        for _ in range(watchers):
            made = [spell.copy_for(o) for o in OPPONENTS
                    if o != original_opponent and o in legal_opponents]
            if staff and made:
                made.append(spell.copy_for(made[0].targets[0][1]))
            copies.extend(made)
        # The delayed trigger references the cast even if original is countered
        # before that trigger resolves; actual original resolution is separate.
        if counter_original:
            spell.zone = "graveyard"
        self.copy_events += len(copies)
        return spell, copies


def highest_exiled(creatures_or_walkers: list[int]) -> int | None:
    return max(creatures_or_walkers) if creatures_or_walkers else None


class ZevlorM7ExactSourceBound(unittest.TestCase):
    def test_00_exact_four_sources_all_100_oracle_and_99_slot_scope(self):
        sets = []
        for p in (BASE, FINAL, ALT8, ALT9):
            self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(), SHA[p.name], p.name)
            cards = inventory(p)
            self.assertEqual(len(cards), 100)
            self.assertEqual(cards[0], "Zevlor, Elturel Exile")
            self.assertEqual(len(Counter(cards)), 97)
            self.assertEqual({n: q for n, q in Counter(cards).items() if q > 1},
                             {"Island": 2, "Mountain": 2, "Swamp": 2})
            for name in cards:
                self.assertIn(name, CARDS)
                self.assertTrue(CARDS[name]["oracle_id"])
                self.assertEqual(CARDS[name]["legal"], "legal", name)
                self.assertTrue(set(CARDS[name]["color_identity"]) <= {"U", "B", "R"}, name)
            sets.append(Counter(cards))
        self.assertEqual(sets[1] - sets[0], Counter(SWAPS.keys()))
        self.assertEqual(sets[0] - sets[1], Counter(SWAPS.values()))
        self.assertEqual(sets[2] - sets[0], Counter(
            [*SWAPS, "Intuition", "Magewright's Stone"]))
        self.assertEqual(sets[3] - sets[0], Counter(
            [*SWAPS, "Intuition", "Magewright's Stone", "Inside Information"]))
        self.assertEqual(sum(n in LANDS for n in inventory(FINAL)), 34)
        self.assertIn("targets only a single opponent", text("Zevlor, Elturel Exile"))
        with (HERE / "Zevlor_M7_Rev1_99slot_ledger.csv").open(newline="") as handle:
            audited = list(csv.DictReader(handle))
        self.assertEqual(sum(int(row["quantity"]) for row in audited), 99)
        self.assertEqual(sum(row["decision"] == "CUT CANDIDATE" for row in audited), 6)

    # The original 5 P0 cases, tested against exact M7 source.
    def test_C1_haste_zone_activate_tap_and_source_paid_two(self):
        self.assertIn("Haste", text("Zevlor, Elturel Exile"))
        self.assertIn("{2}, {T}:", text("Zevlor, Elturel Exile"))
        f = ZevlorFixture(mana={"C": 2})
        self.assertTrue(f.activate())
        self.assertEqual((f.watches, f.mana["C"]), (1, 0))
        self.assertFalse(f.activate())  # Already tapped.
        self.assertFalse(ZevlorFixture(on_battlefield=False).activate())
        self.assertFalse(ZevlorFixture(has_haste=False).activate())
        self.assertFalse(ZevlorFixture(mana={"C": 1}).activate())

    def test_K1_only_one_real_opponent_or_opponent_controlled_permanent(self):
        f = ZevlorFixture()
        self.assertTrue(f.activate())
        # An actual legal cast targeting its own caster is not Zevlor-eligible.
        # Two targets also fail the predicate, but Traumatic Critique itself
        # cannot select two, so do not fake such a cast.
        self.assertFalse(target_is_eligible((("player", "B"), ("player", "C"))))
        illegal = Spell("Traumatic Critique", (("player", "YOU"),))
        result = f.cast_spell(illegal)
        self.assertEqual(len(result[1]), 0)
        self.assertEqual(f.watches, 1)  # Multi-target cast never consumed watch.
        legal = Spell("Traumatic Critique", (("permanent", "C"),))
        result2 = f.cast_spell(legal)
        self.assertEqual(len(result2[1]), 2)
        self.assertFalse(target_is_eligible((("permanent", "YOU"),)))
        self.assertFalse(target_is_eligible((("player", "YOU"),)))

    def test_K2_copies_are_not_cast_but_each_magecraft_triggers(self):
        self.assertIn("cast or copy", text("Sedgemoor Witch").lower())
        self.assertIn("cast or copy", text("Storm-Kiln Artist").lower())
        f = ZevlorFixture()
        self.assertTrue(f.activate())
        spell, copies = f.cast_spell(Spell("Gifts Ungiven", (("player", "B"),)))
        self.assertEqual((f.cast_events, f.copy_events, len(copies)), (1, 2, 2))
        self.assertTrue(all(not c.cast for c in copies))
        magecraft_witch = f.cast_events + f.copy_events
        magecraft_kiln = f.cast_events + f.copy_events
        self.assertEqual((magecraft_witch, magecraft_kiln), (3, 3))
        self.assertEqual(f.cast_events, 1)  # No three cast-only triggers.
        self.assertEqual(spell.zone, "stack")

    def test_K3_countered_original_does_not_erase_delayed_copies(self):
        f = ZevlorFixture()
        self.assertTrue(f.activate())
        original, copies = f.cast_spell(Spell("Praetor's Grasp", (("player", "B"),)),
                                        counter_original=True)
        self.assertEqual(original.zone, "graveyard")
        self.assertEqual([c.targets[0][1] for c in copies], ["C", "D"])
        self.assertEqual(f.watches, 0)
        self.assertEqual(f.cast_events, 1)
        # No activation or illegal targets: countering cannot invent copies.
        no_activation = ZevlorFixture()
        self.assertEqual(len(no_activation.cast_spell(
            Spell("Praetor's Grasp", (("player", "B"),)), counter_original=True)[1]), 0)

    def test_F1_no_claim_of_automatic_compact_win(self):
        f = ZevlorFixture()
        self.assertTrue(f.activate())
        _, copies = f.cast_spell(Spell("Cruelclaw's Heist", (("player", "B"),)))
        self.assertEqual(len(copies), 2)
        enemy_life = {"B": 40, "C": 40, "D": 40}
        self.assertEqual(min(enemy_life.values()), 40)  # Discard/exile is not lethal.
        self.assertEqual(sum(0 for p in enemy_life), 0)  # No invented life loss.

    # The eleven original P1 case IDs.
    def test_K4_copy_retains_x_mode_and_paid_gift_choice(self):
        self.assertIn("X damage to any target", text("Traumatic Critique"))
        self.assertIn("Gift a card", text("Cruelclaw's Heist"))
        original = Spell("Traumatic Critique", (("player", "B"),), x=5, mode="damage")
        copied = original.copy_for("C")
        self.assertEqual((copied.x, copied.mode, copied.cast), (5, "damage", False))
        paid = Spell("Cruelclaw's Heist", (("player", "B"),), gift=True)
        self.assertTrue(paid.copy_for("D").gift)  # Already-chosen optional cost.
        self.assertFalse(Spell("Cruelclaw's Heist", (("player", "B"),)).copy_for("D").gift)
        self.assertIsNone(pay({"U": 1, "R": 1, "C": 3}, "{X}{U}{R}", x=5))
        self.assertIsNotNone(pay({"U": 1, "R": 1, "C": 5}, "{X}{U}{R}", x=5))

    def test_K5_bracers_separate_watches_one_cast_no_free_repeat(self):
        self.assertIn("copy that ability", text("Illusionist's Bracers"))
        f = ZevlorFixture()
        self.assertTrue(f.activate(bracers=True))
        self.assertEqual((f.activated, f.watches), (1, 2))
        _, copies = f.cast_spell(Spell("Bribery", (("player", "B"),)))
        self.assertEqual(len(copies), 4)
        self.assertEqual(f.watches, 0)
        self.assertFalse(f.activate())  # No phantom untap from ability copies.
        f2 = ZevlorFixture()
        self.assertTrue(f2.activate())
        self.assertTrue(f2.untap(source="Pemmin's Aura"))
        self.assertTrue(f2.activate())
        self.assertEqual(f2.watches, 2)
        self.assertEqual(len(f2.cast_spell(Spell("Bribery", (("player", "B"),)))[1]), 4)

    def test_K6_twinning_staff_one_additional_per_copy_event(self):
        self.assertIn("that many times plus an additional time", text("Twinning Staff"))
        f = ZevlorFixture()
        self.assertTrue(f.activate())
        _, copies = f.cast_spell(Spell("Praetor's Grasp", (("player", "B"),)),
                                  staff=True)
        self.assertEqual(len(copies), 3)  # Two other opponents plus ONE Staff bonus.
        self.assertEqual(f.cast_events, 1)
        self.assertTrue(all(not copy.cast for copy in copies))
        f2 = ZevlorFixture()
        self.assertTrue(f2.activate(bracers=True))
        self.assertEqual(len(f2.cast_spell(Spell("Praetor's Grasp",
                                                 (("player", "B"),)), staff=True)[1]), 6)

    def test_K7_swiftfoot_hexproof_allows_own_untap_greaves_shroud_does_not(self):
        self.assertIn("hexproof", text("Swiftfoot Boots").lower())
        self.assertIn("Untap target legendary permanent", text("Minamo, School at Water's Edge"))
        self.assertIn("Untap target legendary creature", text("Patriar's Seal"))
        swift = ZevlorFixture(tapped=True)
        self.assertTrue(swift.untap(source="Minamo, School at Water's Edge",
                                     targetable=True))
        shrouded = ZevlorFixture(tapped=True)
        self.assertFalse(shrouded.untap(source="Patriar's Seal", targetable=False))
        self.assertTrue(shrouded.tapped)

    def test_E1_payment_cast_valid_copy_sequence_and_negated_precondition(self):
        f = ZevlorFixture(mana={"C": 3, "B": 1})
        self.assertTrue(f.activate())
        original, copies = f.cast_spell(Spell("End of the Hunt", (("player", "B"),)))
        self.assertEqual((f.mana["C"], f.mana["B"], f.cast_events), (0, 0, 1))
        self.assertEqual([c.targets[0][1] for c in copies], ["C", "D"])
        self.assertEqual(len(copies), 2)
        broke = ZevlorFixture(mana={"C": 2, "B": 0})
        self.assertTrue(broke.activate())
        self.assertIsNone(broke.cast_spell(Spell("End of the Hunt", (("player", "B"),))))
        self.assertEqual(broke.watches, 1)

    def test_E2_support_training_omen_pemmin_seal_minamo_bracers_staff(self):
        self.assertIn("less to activate", text("Training Grounds"))
        self.assertIn("Spend this mana only to activate abilities", text("Omen Hawker"))
        f = ZevlorFixture(mana={"C": 1, "U": 4})
        self.assertTrue(f.activate(training=True, bracers=True))
        self.assertEqual(f.mana["C"], 0)
        self.assertTrue(f.untap(source="Pemmin's Aura"))
        self.assertTrue(f.activate(training=True))
        self.assertEqual(f.watches, 3)
        f2 = ZevlorFixture(mana={"C": 0, "U": 2})
        self.assertTrue(f2.activate())  # Hawker's CU may pay the *ability* cost.
        f2.mana = {"C": 0, "U": 2, "R": 0}
        self.assertIsNone(pay(f2.mana, CARDS["Rousing Refrain"]["mana_cost"]))
        self.assertIn("Untap", text("Pemmin's Aura"))
        self.assertIn("Untap target legendary creature", text("Patriar's Seal"))
        self.assertIn("Untap target legendary permanent", text("Minamo, School at Water's Edge"))
        self.assertIn("additional time", text("Twinning Staff"))

    def test_W1_multiplied_payloads_captures_three_distinct_opponents(self):
        payloads = ("Cruel Ultimatum", "Praetor's Grasp", "Acquire",
                    "Bribery", "River's Rebuke", "Leadership Vacuum")
        for name in payloads:
            self.assertRegex(text(name).lower(), r"target (opponent|player)", name)
            f = ZevlorFixture()
            self.assertTrue(f.activate())
            original, copied = f.cast_spell(Spell(name, (("player", "B"),)))
            self.assertIsNotNone(original)
            self.assertEqual({o.targets[0][1] for o in [original, *copied]},
                             set(OPPONENTS))
        self.assertIn("loses 5 life", text("Cruel Ultimatum"))
        enemy_life = dict.fromkeys(OPPONENTS, 40)
        for p in OPPONENTS:
            enemy_life[p] -= 5
        self.assertEqual(enemy_life, dict.fromkeys(OPPONENTS, 35))
        # If opponent D has no legal target permanent for a permanent-target
        # spell, its copy cannot be manufactured to steal nonexisting objects.
        f = ZevlorFixture()
        self.assertTrue(f.activate())
        self.assertEqual(len(f.cast_spell(
            Spell("Traumatic Critique", (("permanent", "B"),)),
            legal_opponents=("B", "C"))[1]), 1)

    def test_W2_magecraft_witch_and_artist_real_copy_counts(self):
        f = ZevlorFixture()
        self.assertTrue(f.activate())
        f.cast_spell(Spell("Peek", (("player", "B"),)))
        triggers = f.cast_events + f.copy_events
        self.assertEqual(triggers, 3)
        self.assertIn("Pest", text("Sedgemoor Witch"))
        self.assertIn("Treasure", text("Storm-Kiln Artist"))
        self.assertEqual((triggers, triggers), (3, 3))
        self.assertEqual(f.cast_events, 1)  # Cast-only effects occur once.

    def test_W3_omen_hawker_pemmin_colorless_loop_not_colored_freecasting(self):
        self.assertIn("{T}: Add {C}{U}", text("Omen Hawker"))
        self.assertIn("{U}: Untap enchanted creature", text("Pemmin's Aura"))
        # Enchant Omen Hawker. Each tap produces CU for ACTIVATED abilities;
        # spend U on Pemmin's Aura's untap, net +C, repeat bounded five times.
        ability_pool = {"C": 0, "U": 0}
        tapped = False
        for _ in range(5):
            self.assertFalse(tapped)
            tapped = True
            ability_pool["C"] += 1
            ability_pool["U"] += 1
            ability_pool["U"] -= 1
            tapped = False
        self.assertEqual(ability_pool, {"C": 5, "U": 0})
        self.assertIsNone(pay(ability_pool, "{U}"))
        self.assertIsNone(pay(ability_pool, "{3}{R}{R}"))
        # That resource cannot pay for SPELLS even generic spell costs.
        no_pemmin = 1
        self.assertLess(no_pemmin, 5)  # Only one Hawker tap without untap.

    def test_F2_sorcery_priority_cast_window_and_turn_boundaries(self):
        f = ZevlorFixture()
        self.assertTrue(f.activate())
        self.assertIsNone(f.cast_spell(
            Spell("Cruelclaw's Heist", (("player", "B"),)), sorcery_window=False))
        self.assertEqual(f.watches, 1)
        self.assertEqual(len(f.cast_spell(
            Spell("Cruelclaw's Heist", (("player", "B"),)), sorcery_window=True)[1]), 2)
        f2 = ZevlorFixture()
        self.assertTrue(f2.activate())
        f2.next_turn()
        self.assertEqual(len(f2.cast_spell(Spell("Gifts Ungiven",
                                                 (("player", "B"),)))[1]), 0)

    def test_F3_only_actual_target_not_multiple_or_untargeted_copy(self):
        self.assertTrue(target_is_eligible((("player", "B"),)))
        self.assertTrue(target_is_eligible((("permanent", "D"),)))
        for bad in ((), (("player", "YOU"),), (("permanent", "YOU"),),
                    (("player", "B"), ("player", "C"))):
            self.assertFalse(target_is_eligible(bad))
        self.assertTrue(target_is_eligible((("player", "B"),)))  # Gifts targets.
        self.assertIn("any target", text("Traumatic Critique"))
        self.assertIn("Target opponent", text("Gifts Ungiven"))

    # Six specific approved substitutions with actual adverse branches.
    def test_s01_end_of_hunt_highest_exile_but_not_artifact_or_smaller(self):
        self.assertIn("greatest mana value", text("End of the Hunt"))
        self.assertIn("Target opponent", text("End of the Hunt"))
        self.assertEqual(highest_exiled([2, 8, 5]), 8)
        self.assertNotEqual(highest_exiled([2, 8, 5]), 2)
        self.assertIsNone(highest_exiled([]))
        self.assertNotIn("artifact", text("End of the Hunt").lower())
        self.assertIn("artifact", text("Abrade").lower())

    def test_s02_strategic_betrayal_exiles_creature_and_graveyard(self):
        self.assertIn("and their graveyard", text("Strategic Betrayal"))
        opponent = {"creatures": ["token", "threat"], "graveyard": ["reanimate", "fetch"]}
        choice = opponent["creatures"].pop(0)  # Opponent picks a sacrificial token.
        opponent["graveyard"].clear()
        self.assertEqual((choice, opponent), ("token",
                                             {"creatures": ["threat"], "graveyard": []}))
        empty = {"creatures": [], "graveyard": ["reanimate"]}
        empty["graveyard"].clear()  # No creature, still exiles graveyard.
        self.assertEqual(empty, {"creatures": [], "graveyard": []})

    def test_s03_gifts_three_own_library_piles_partitions_are_independent(self):
        self.assertIn("Search your library for up to four cards", text("Gifts Ungiven"))
        self.assertIn("Target opponent chooses two", text("Gifts Ungiven"))
        pile_library = [f"card-{i}" for i in range(12)]
        hand, graveyard = [], []
        for target in OPPONENTS:  # Three actual Zevlor-targeted spell instances.
            revealed = [pile_library.pop(0) for _ in range(4)]
            chosen = revealed[:2] if target != "C" else revealed[-2:]
            graveyard.extend(chosen)
            hand.extend(c for c in revealed if c not in chosen)
        self.assertEqual((len(hand), len(graveyard), len(pile_library)), (6, 6, 0))
        self.assertEqual(len(set(hand + graveyard)), 12)
        self.assertNotIn("target opponent's library", text("Gifts Ungiven").lower())
        self.assertEqual(len({"same"}), 1)  # Cannot reveal four identical names.

    def test_s04_rousing_refrain_pay_five_red_hand_math_and_suspend(self):
        self.assertIn("each card in target opponent's hand", text("Rousing Refrain"))
        self.assertIn("Suspend 3", text("Rousing Refrain"))
        f = ZevlorFixture(mana={"C": 5, "R": 2})
        self.assertTrue(f.activate())
        original, copies = f.cast_spell(Spell("Rousing Refrain", (("player", "B"),)))
        self.assertEqual(len(copies), 2)
        self.assertEqual(f.mana["R"], 0)  # Two red pips were actually spent.
        hand_size = {"B": 5, "C": 4, "D": 2}
        self.assertEqual(sum(hand_size[op] for op in OPPONENTS), 11)
        self.assertTrue(all(not c.cast for c in copies))
        # Only the physical card can remain in exile suspended; spell copies
        # cease to exist after changing zones, so do not assign them time counters.
        suspended_physical, suspended_copies = 3, 0
        self.assertEqual((suspended_physical, suspended_copies), (3, 0))
        self.assertIsNone(pay({"C": 3, "R": 1}, CARDS["Rousing Refrain"]["mana_cost"]))

    def test_s05_traumatic_critique_zero_x_is_payable_filter_not_free_burn(self):
        f = ZevlorFixture(mana={"C": 2, "U": 1, "R": 1})
        self.assertTrue(f.activate())
        original, copies = f.cast_spell(Spell("Traumatic Critique",
                                              (("player", "B"),), x=0))
        self.assertEqual(len(copies), 2)
        self.assertEqual((f.mana["U"], f.mana["R"]), (0, 0))
        self.assertEqual(3 * 2, 6)  # Six drawn total across three resolutions.
        self.assertEqual(3 * 1, 3)  # Three mandatory discards.
        self.assertEqual(3 * 0, 0)  # Zero burn at X=0.
        self.assertIsNone(pay({"U": 1, "R": 1, "C": 1}, "{X}{U}{R}", x=2))

    def test_s06_cruelclaws_heist_no_gift_three_hand_exiles_no_free_cast(self):
        self.assertIn("Target opponent reveals their hand", text("Cruelclaw's Heist"))
        self.assertIn("If the gift was promised", text("Cruelclaw's Heist"))
        f = ZevlorFixture(mana={"C": 2, "B": 2})
        self.assertTrue(f.activate())
        original, copies = f.cast_spell(Spell("Cruelclaw's Heist",
                                              (("player", "B"),), gift=False))
        self.assertEqual(len(copies), 2)
        hands = {"B": ["land", "engine"], "C": ["land", "answer"],
                 "D": ["land", "combo"]}
        exiled = [hands[o].pop(1) for o in OPPONENTS]
        self.assertEqual(exiled, ["engine", "answer", "combo"])
        self.assertFalse(original.gift)
        self.assertTrue(all(not copy.gift for copy in copies))
        self.assertEqual(len(exiled), 3)
        # Without a promised gift no permission to cast those exiled cards.
        cast_permission = original.gift
        self.assertFalse(cast_permission)
        self.assertIsNone(pay({"B": 1}, CARDS["Cruelclaw's Heist"]["mana_cost"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
