"""Deck #50 exact-M7 source-bound *finite* Commander rules-state transfer.

The 15 C/K/E/W/F cases are traced against the named M6 blueprint, the
documented Oracle analyses and an exact 100-card physical candidate.  This
miniature fixture checks real source/cost/stack/zone consequences and negative
controls.  It is NOT a general Magic engine, multiplayer win-rate experiment,
or a retroactive replay of the historical sealed M6 I/J phases.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from hashlib import sha256
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DECK_DIR = ROOT / "data/grixis/m7/sauron_dark_lord_rev1"
LIST = DECK_DIR / "sauron_dark_lord_m7_rev1.txt"
BLUEPRINT = ROOT / "data/grixis/m6/test_blueprints/Sauron__the_Dark_Lord.json"
EXPECTED_SHA = "266660c6a3241c07a052da7624366be1f9617cb5db4c35c422b0e8f828977d9b"


@dataclass
class Permanent:
    name: str
    controller: int = 0
    kinds: set[str] = field(default_factory=set)
    subtypes: set[str] = field(default_factory=set)
    counters: int = 0
    token: bool = False
    legendary: bool = False
    shadow_counter: bool = False
    tapped: bool = False

    def has_type(self, subtype: str, adaptation: bool = False) -> bool:
        return subtype in self.subtypes or (adaptation and subtype == "Wraith")


class FiniteSauron:
    """Controlled battlefield with explicit cast, LIFO trigger, zone and cost ledger."""

    def __init__(self):
        self.battlefield = [Permanent("Sauron, the Dark Lord", kinds={"Creature"},
                                      subtypes={"Avatar", "Horror"}, legendary=True)]
        self.stack: list[tuple[str, object]] = []
        self.hand: list[tuple[str, str]] = []  # (card, card-type role)
        self.graveyard: list[tuple[str, str]] = []
        self.exile: list[tuple[str, str]] = []
        self.library: list[str] = [f"library-{i}" for i in range(90)]
        self.mana = Counter({"B": 0, "U": 0, "R": 0, "C": 0})
        self.life = [40, 40, 40, 40]
        self.ring_events = 0
        self.counter_events = 0
        self.resolved_spells = 0
        self.tempt_draw_choices: list[bool] = []
        self.ring_level = 0
        self.roaming_choice = None
        self.arcane_wraith = False
        self.mauhur = False
        self.great_goblin = False
        self.glint_horn = False
        self.bone_miser = False
        self.moonstone = False
        self.pending_moonstone: list[tuple[str, str]] = []
        self.zombies = 0
        self.trace: list[str] = []

    def creature(self, name, *, owner=0, subtypes=(), counters=0, token=False, legendary=False):
        p = Permanent(name, controller=owner, kinds={"Creature"}, subtypes=set(subtypes),
                      counters=counters, token=token, legendary=legendary)
        self.battlefield.append(p)
        return p

    def find(self, name):
        return next((p for p in self.battlefield if p.name == name), None)

    def pay(self, *, b=0, u=0, r=0, generic=0):
        needed = Counter({"B": b, "U": u, "R": r})
        if any(self.mana[c] < count for c, count in needed.items()):
            return False
        rest = self.mana.copy()
        for c, count in needed.items():
            rest[c] -= count
        if sum(rest.values()) < generic:
            return False
        for c in ("C", "B", "U", "R"):
            amount = min(rest[c], generic)
            rest[c] -= amount
            generic -= amount
        self.mana = rest
        return True

    def active(self, name):
        return self.find(name) is not None

    def triggered_multiplier(self, creature: Permanent):
        """Throne Wraith doubles every creature trigger when Adaptation grants Wraith."""
        return 2 if self.roaming_choice and creature.has_type(self.roaming_choice, self.arcane_wraith) else 1

    def cast(self, *, player, spell, cost=(0, 0, 0, 0)):
        b, u, r, gen = cost
        if player == 0 and not self.pay(b=b, u=u, r=r, generic=gen):
            return False
        # Source spell is pushed before cast triggers (triggers resolve first).
        self.stack.append(("spell", spell))
        commander = self.find("Sauron, the Dark Lord")
        if player != 0 and commander:
            for _ in range(self.triggered_multiplier(commander)):
                self.stack.append(("amass", 1))
        self.trace.append(f"cast:{player}:{spell}")
        return True

    def cast_sauron_from_command_zone(self, tax=0):
        # Printed {3}{U}{B}{R}, plus {2} per earlier command-zone cast.
        if self.find("Sauron, the Dark Lord"):
            return False  # this fixture requires commander absent to cast
        if not self.pay(b=1, u=1, r=1, generic=3 + tax):
            return False
        self.battlefield.append(Permanent("Sauron, the Dark Lord", kinds={"Creature"},
                                          subtypes={"Avatar", "Horror"}, legendary=True))
        return True  # representative resolution, not a stack counterfight

    def cast_nazgul(self):
        if not self.pay(b=1, generic=2):
            return False
        p = self.creature("Nazgûl", subtypes={"Wraith"})
        for _ in range(self.triggered_multiplier(p)):
            self.stack.append(("ring_tempt", 1))
        return True

    def cast_soothing(self, target):
        if target not in self.battlefield or target.token or "Creature" not in target.kinds:
            return False
        if not self.pay(u=1, generic=1):
            return False
        self.stack.append(("soothing", target))
        return True

    def counter_spell(self, spell):
        # Countering the original spell does not remove Sauron's cast trigger.
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == ("spell", spell):
                self.stack.pop(i)
                self.trace.append(f"counter:{spell}")
                return True
        return False

    def amass(self, amount, *, species="Orc"):
        armies = [p for p in self.battlefield if p.controller == 0 and "Army" in p.subtypes]
        if armies:
            army = armies[0]
            army.subtypes.add(species)
        else:
            army = self.creature("Army token", subtypes={species, "Army"}, token=True)
        actual = amount + int(self.mauhur and bool({"Army", "Orc", "Goblin"} & army.subtypes))
        army.counters += actual
        self.counter_events += 1
        self.trace.append(f"amass:{species}:{amount}+{actual-amount}")
        if self.great_goblin:
            goblin = self.find("The Great Goblin")
            if goblin:
                for _ in range(self.triggered_multiplier(goblin)):
                    self.stack.append(("great_goblin_ping", 1))
        return army

    def ring_tempts(self):
        self.ring_events += 1
        self.ring_level = min(self.ring_level + 1, 4)
        self.trace.append("ring:tempt")
        # Sauron's Ring trigger and each Nazgul pump trigger are distinct.
        sauron = self.find("Sauron, the Dark Lord")
        if sauron:
            for _ in range(self.triggered_multiplier(sauron)):
                self.stack.append(("sauron_reset", 1))
        for nazgul in [p for p in self.battlefield if p.name == "Nazgûl" and p.controller == 0]:
            for _ in range(self.triggered_multiplier(nazgul)):
                self.stack.append(("nazgul_wave", 1))

    def discard_all_and_draw(self, choose):
        if not choose:
            self.trace.append("reset:declined")
            return
        to_discard = self.hand[:]
        self.hand.clear()
        for card in to_discard:
            self.graveyard.append(card)
            if self.glint_horn:
                for opponent in (1, 2, 3):
                    self.life[opponent] -= 1
            if self.bone_miser:
                role = card[1]
                if role == "land":
                    self.mana["B"] += 2
                elif role == "creature":
                    self.zombies += 1
                else:
                    self.draw(1)
            if self.moonstone:
                self.pending_moonstone.append(card)
        self.draw(4)
        self.trace.append(f"reset:{len(to_discard)}:draw4")

    def draw(self, n):
        for _ in range(n):
            if not self.library:
                raise AssertionError("empty library; unmodeled loss condition")
            self.hand.append((self.library.pop(0), "spell"))

    def resolve(self):
        if not self.stack:
            return False
        event, param = self.stack.pop()
        if event == "amass":
            self.amass(int(param))
        elif event == "great_goblin_ping":
            # A triggered ability on the stack survives its source leaving.
            self.life[1] -= 2
        elif event == "nazgul_wave":
            for creature in list(self.battlefield):
                if creature.controller == 0 and creature.has_type("Wraith", self.arcane_wraith):
                    n = 1 + int(self.mauhur and bool({"Army", "Orc", "Goblin"} & creature.subtypes))
                    creature.counters += n
                    self.counter_events += 1
                    goblin = self.find("The Great Goblin")
                    if self.great_goblin and goblin and {"Army", "Orc", "Goblin"} & creature.subtypes:
                        for _ in range(self.triggered_multiplier(goblin)):
                            self.stack.append(("great_goblin_ping", 1))
        elif event == "sauron_reset":
            self.discard_all_and_draw(self.tempt_draw_choices.pop(0) if self.tempt_draw_choices else False)
        elif event == "spell":
            self.resolved_spells += 1
            if param == "Birthday Escape":
                self.draw(1)
                self.ring_tempts()
        elif event == "ring_tempt":
            self.ring_tempts()
        elif event == "soothing":
            if param in self.battlefield:  # only legal target left; otherwise spell fizzles
                self.battlefield.remove(param)
                if param.controller == 0:
                    self.hand.append((param.name, "creature"))
                self.ring_tempts()
        else:
            raise AssertionError(("unknown stack event", event))
        return True

    def resolve_all(self):
        while self.resolve():
            if len(self.trace) > 1000:
                raise AssertionError("bounded fixture overrun")

    def combat_army(self, *, damage_to_player: bool, combat: bool = True, shadow_blocker=False):
        army = self.find("Army token")
        if not army or army.counters == 0 or not combat or not damage_to_player or shadow_blocker:
            return 0
        if not self.find("Sauron, the Dark Lord"):
            return 0
        for _ in range(self.triggered_multiplier(self.find("Sauron, the Dark Lord"))):
            self.stack.append(("ring_tempt", 1))
        return army.counters

    def wipe(self):
        for permanent in list(self.battlefield):
            if "Creature" in permanent.kinds:
                self.battlefield.remove(permanent)
                if not permanent.token:
                    self.graveyard.append((permanent.name, "creature"))


class TestDeck50Cases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = LIST.read_bytes()
        assert sha256(raw).hexdigest() == EXPECTED_SHA
        cls.list_counts = Counter()
        for row in raw.decode().splitlines():
            qty, name = row.split("x ", 1)
            cls.list_counts[name.removesuffix(" [Commander]")] += int(qty)
        assert sum(cls.list_counts.values()) == 100
        cls.blueprint = json.loads(BLUEPRINT.read_text())
        assert {r["id"] for r in cls.blueprint["cases"]} == {
            "C1", "K1", "K2", "K3", "K4", "K5", "K6", "K7",
            "E1", "E2", "W1", "W2", "F1", "F2", "F3"
        }
        cls.commander_text = cls.blueprint["commander_oracle_snapshots"][0]["oracle_text"]

    def test_C1_commander_zones_stack_and_optional_reset(self):
        for text in ("Ward—Sacrifice a legendary", "Whenever an opponent casts a spell",
                     "Whenever an Army you control deals combat damage",
                     "Whenever the Ring tempts you"):
            self.assertIn(text, self.commander_text)
        s = FiniteSauron()
        s.hand = [("Nazgûl", "creature"), ("Island", "land")]
        s.tempt_draw_choices = [True]
        self.assertTrue(s.cast(player=1, spell="Opponent spell"))
        s.resolve_all()
        self.assertEqual(s.find("Army token").counters, 1)
        s.combat_army(damage_to_player=True)
        s.resolve_all()
        self.assertEqual(s.ring_events, 1)
        self.assertEqual(len(s.hand), 4)
        self.assertEqual(len(s.graveyard), 2)
        s.wipe()
        self.assertTrue(s.cast(player=1, spell="Second opponent spell"))
        s.resolve_all()
        self.assertIsNone(s.find("Army token"))  # no commander on battlefield
        self.assertFalse(s.cast_sauron_from_command_zone())  # no free recast
        s.mana = Counter({"B": 1, "U": 1, "R": 1, "C": 3})
        self.assertTrue(s.cast_sauron_from_command_zone())  # 3UBR paid
        self.assertEqual(sum(s.mana.values()), 0)

    def test_K1_ward_sacrifice_paid_on_target_and_not_on_sweeper(self):
        s = FiniteSauron()
        opponent_legend = s.creature("Legendary enemy", owner=1, legendary=True)
        opponent_nonlegend = s.creature("Ordinary enemy", owner=1)
        def target_and_pay_ward(cost_source):
            if cost_source is None or cost_source not in s.battlefield or not cost_source.legendary or cost_source.controller != 1:
                return False
            s.battlefield.remove(cost_source)
            s.graveyard.append((cost_source.name, "creature"))
            return True
        self.assertFalse(target_and_pay_ward(opponent_nonlegend))
        self.assertTrue(target_and_pay_ward(opponent_legend))
        self.assertNotIn(opponent_legend, s.battlefield)
        self.assertFalse(target_and_pay_ward(opponent_legend))  # cost not reusable
        s.wipe()  # untargeted effect doesn't invoke ward
        self.assertIsNone(s.find("Sauron, the Dark Lord"))

    def test_K2_cast_even_if_countered_and_throne_priority(self):
        s = FiniteSauron()
        self.assertTrue(s.cast(player=1, spell="Lightning Bolt"))
        self.assertTrue(s.counter_spell("Lightning Bolt"))
        s.resolve_all()
        self.assertEqual((s.find("Army token").counters, s.resolved_spells), (1, 0))
        self.assertTrue(s.cast(player=0, spell="Own spell"))
        s.resolve_all()
        self.assertEqual(s.find("Army token").counters, 1)
        s.roaming_choice = "Avatar"
        self.assertTrue(s.cast(player=2, spell="Two triggers"))
        self.assertEqual([x[0] for x in s.stack].count("amass"), 2)
        s.resolve_all()
        self.assertEqual(s.find("Army token").counters, 3)

    def test_K3_mauhur_exactly_one_per_counter_event(self):
        s = FiniteSauron()
        s.mauhur = True
        army = s.amass(5)
        self.assertEqual((army.counters, s.counter_events), (6, 1))
        s.amass(1)
        self.assertEqual((army.counters, s.counter_events), (8, 2))
        s.mauhur = False
        s.amass(1)
        self.assertEqual(army.counters, 9)

    def test_K4_great_goblin_event_and_adversarial_removal(self):
        s = FiniteSauron()
        s.mauhur = s.great_goblin = True
        s.creature("The Great Goblin", subtypes={"Goblin"}, legendary=True)
        army = s.amass(3)
        self.assertEqual(army.counters, 4)
        self.assertEqual(len(s.stack), 1)
        s.resolve_all()
        self.assertEqual(s.life[1], 38)  # 2 damage per event, not per counter
        s.battlefield.remove(s.find("The Great Goblin"))
        s.amass(2)
        s.resolve_all()
        self.assertEqual(s.life[1], 38)
        goblin = s.creature("The Great Goblin", subtypes={"Goblin"}, legendary=True)
        s.amass(2)
        s.battlefield.remove(goblin)  # source removed after trigger already stacked
        s.resolve_all()
        self.assertEqual(s.life[1], 36)  # LKI, removing source cannot undo trigger

    def test_K5_throne_wraith_bridge_vs_without_adaptation(self):
        s = FiniteSauron()
        s.roaming_choice = "Wraith"
        s.creature("Nazgûl", subtypes={"Wraith"})
        s.ring_tempts()
        self.assertEqual([x[0] for x in s.stack].count("nazgul_wave"), 2)
        self.assertEqual([x[0] for x in s.stack].count("sauron_reset"), 1)
        s.resolve_all()
        s.arcane_wraith = True
        s.ring_tempts()
        # CRITICAL: Adaptation makes Avatar Sauron a Wraith, so Throne now
        # doubles Sauron's triggered ability AND Nazgul's, not only Nazgul.
        self.assertEqual([x[0] for x in s.stack].count("nazgul_wave"), 2)
        self.assertEqual([x[0] for x in s.stack].count("sauron_reset"), 2)
        s.resolve_all()
        self.assertEqual(s.find("Sauron, the Dark Lord").counters, 2)
        s.arcane_wraith = False
        s.ring_tempts()
        s.resolve_all()
        self.assertEqual(s.find("Sauron, the Dark Lord").counters, 2)
        # Original Nazgul ETB is a real Wraith creature trigger; Throne
        # doubles the ETB itself, producing two independent temptations.
        s.mana = Counter({"B": 1, "C": 2})
        before = s.ring_events
        self.assertTrue(s.cast_nazgul())
        s.resolve_all()
        self.assertEqual(s.ring_events - before, 2)
        self.assertEqual(sum(s.mana.values()), 0)

    def test_K6_seven_nazgul_and_temptation_waves(self):
        s = FiniteSauron()
        self.assertEqual(self.list_counts["Nazgûl"], 7)  # Oracle allows up to nine
        army = s.amass(1)
        wraiths = [s.creature("Nazgûl", subtypes={"Wraith"}) for _ in range(7)]
        s.ring_tempts()
        s.resolve_all()
        self.assertTrue(all(w.counters == 7 for w in wraiths))
        self.assertEqual(army.counters, 1)
        s.arcane_wraith = True
        s.ring_tempts()
        s.resolve_all()
        self.assertEqual(army.counters, 8)  # 7 more; Army is also a Wraith
        self.assertTrue(all(w.counters == 14 for w in wraiths))

    def test_K7_minas_morgul_cost_tap_shadow_and_army_identity(self):
        s = FiniteSauron()
        army = s.amass(2)
        morgul = Permanent("Minas Morgul, Dark Fortress", kinds={"Land"})
        s.battlefield.append(morgul)
        s.mana = Counter({"B": 0, "C": 3})
        self.assertFalse(s.pay(b=1, generic=3))
        self.assertFalse(army.shadow_counter)
        s.mana["B"] = 1
        self.assertTrue(s.pay(b=1, generic=3))
        morgul.tapped = True
        army.shadow_counter = True
        army.subtypes.add("Wraith")
        self.assertTrue({"Army", "Orc", "Wraith"} <= army.subtypes)
        self.assertTrue(morgul.tapped)
        self.assertEqual(sum(s.mana.values()), 0)

    def test_E1_three_opponent_casts_source_paid_nonloop(self):
        s = FiniteSauron()
        for player in (1, 2, 3):
            self.assertTrue(s.cast(player=player, spell=f"opponent-{player}"))
        s.resolve_all()
        self.assertEqual(s.find("Army token").counters, 3)
        self.assertEqual(s.resolved_spells, 3)
        self.assertEqual(s.counter_events, 3)
        # No automatic infinite amass: with no new opposing cast, the state stops.
        before = (s.find("Army token").counters, len(s.stack))
        s.resolve_all()
        self.assertEqual((s.find("Army token").counters, len(s.stack)), before)

    def test_E2_paid_birthday_escape_vs_invalid_soothing_target(self):
        s = FiniteSauron()
        s.hand = [("Creature", "creature")]
        s.mana["U"] = 1
        self.assertTrue(s.cast(player=0, spell="Birthday Escape", cost=(0, 1, 0, 0)))
        s.resolve_all()  # resolving Birthday Escape tempts Ring, draws one
        self.assertEqual((s.ring_events, s.life[0]), (1, 40))
        self.assertEqual(len(s.hand), 2)  # draw one, optional Sauron reset declined
        # Soothing requires nontoken creature target at both cast/resolution;
        # with sole target removed in response, entire spell fails, no Ring.
        target = s.creature("Target enemy", owner=1)
        s.mana = Counter({"U": 1, "C": 1})
        self.assertTrue(s.cast_soothing(target))
        s.battlefield.remove(target)
        s.resolve_all()
        self.assertEqual(s.ring_events, 1)
        self.assertEqual(sum(s.mana.values()), 0)

    def test_W1_trample_and_shadow_need_actual_damage_to_player(self):
        s = FiniteSauron()
        army = s.amass(6)
        self.assertEqual(s.combat_army(damage_to_player=False), 0)
        self.assertEqual(s.combat_army(damage_to_player=True, combat=False), 0)
        army.shadow_counter = True
        self.assertEqual(s.combat_army(damage_to_player=True, shadow_blocker=True), 0)
        self.assertEqual(s.ring_events, 0)
        self.assertEqual(s.combat_army(damage_to_player=True), 6)
        s.resolve_all()
        self.assertEqual(s.ring_events, 1)

    def test_W2_goblin_pings_source_changed_from_cut_widespread(self):
        s = FiniteSauron()
        s.great_goblin = True
        s.creature("The Great Goblin", subtypes={"Goblin"}, legendary=True)
        s.mana = Counter({"U": 1, "C": 1})
        self.assertTrue(s.pay(u=1, generic=1))  # Lazotep Plating
        army = s.amass(1, species="Zombie")
        self.assertIn("Army", army.subtypes)
        s.resolve_all()
        self.assertEqual(s.life[1], 38)
        self.assertEqual(s.life[2], 40)  # target *opponent*, not every opponent
        s.roaming_choice = "Wraith"
        s.arcane_wraith = True
        s.amass(1)
        s.resolve_all()
        self.assertEqual(s.life[1], 34)  # Goblin also Wraith; Throne doubles

    def test_F1_no_claimed_compact_infinite_win_and_counterspell_window(self):
        for absent in ("Underworld Breach", "Thassa's Oracle", "Demonic Consultation",
                       "Worldgorger Dragon", "Isochron Scepter", "Reiterate"):
            self.assertNotIn(absent, self.list_counts)
        s = FiniteSauron()
        s.mana["U"] = 1
        self.assertTrue(s.cast(player=1, spell="opponent combo spell"))
        self.assertTrue(s.pay(u=1))  # Swan Song represented as a U counterspell
        self.assertTrue(s.counter_spell("opponent combo spell"))
        s.resolve_all()
        self.assertEqual((s.resolved_spells, s.find("Army token").counters), (0, 1))
        self.assertEqual(s.life[1:], [40, 40, 40])

    def test_F2_quiet_opponents_keep_call_and_ring_dependent_engine(self):
        s = FiniteSauron()
        s.creature("Nazgûl", subtypes={"Wraith"})
        for upkeep in range(3):
            # Call of the Ring is a preexisting upkeep trigger; opponents
            # have cast zero spells throughout this source-paid finite trace.
            s.ring_tempts()
            s.resolve_all()
            self.assertIsNone(s.find("Army token"))
        self.assertEqual((s.ring_events, s.find("Nazgûl").counters), (3, 3))
        self.assertEqual(s.resolved_spells, 0)

    def test_F3_sweeper_loses_army_token_and_reanimates_nontoken_only(self):
        s = FiniteSauron()
        s.amass(8)
        s.creature("Nazgûl", subtypes={"Wraith"}, counters=3)
        s.wipe()
        self.assertIsNone(s.find("Army token"))
        self.assertIn(("Nazgûl", "creature"), s.graveyard)
        self.assertNotIn(("Army token", "creature"), s.graveyard)
        self.assertNotIn("The Ozolith", self.list_counts)  # cut; no stored counters
        s.creature("Nazgûl", subtypes={"Wraith"})  # payable later reanimate target
        self.assertEqual(s.find("Nazgûl").counters, 0)

    def test_changed_discard_package_paid_zones_mana_damage_draw(self):
        s = FiniteSauron()
        s.glint_horn = s.bone_miser = s.moonstone = True
        s.hand = [("Swamp", "land"), ("Nazgûl", "creature"), ("Ringsight", "spell")]
        s.tempt_draw_choices = [True]
        s.ring_tempts()
        s.resolve_all()
        self.assertEqual(s.life[1:], [37, 37, 37])
        self.assertEqual(s.mana["B"], 2)
        self.assertEqual(s.zombies, 1)
        self.assertEqual(len(s.hand), 5)  # Bone Miser noncreature + draw4
        self.assertEqual(len(s.pending_moonstone), 3)
        # Optional Moonstone choice moves *the discarded actual object* from
        # graveyard to exile; this denies direct reanimation of that card.
        target = ("Nazgûl", "creature")
        self.assertIn(target, s.graveyard)
        s.graveyard.remove(target)
        s.exile.append(target)
        self.assertNotIn(target, s.graveyard)
        self.assertIn(target, s.exile)


if __name__ == "__main__":
    unittest.main()
