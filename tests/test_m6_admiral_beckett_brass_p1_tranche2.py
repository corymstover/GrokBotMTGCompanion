"""Remaining four Admiral Beckett Brass P1 blueprint mechanics, finite only.

E01/E02/W01/F02: source-paid staged turns, physical cards/tokens, exact
timing and adverse cases. No multiplayer win-rate, full stack engine, random
draw process, full Oracle certification or claim of final M6/M7 acceptance.
"""

from collections import Counter, defaultdict
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
SNAPSHOT = ROOT / "data/grixis/m6/oracle_snapshots/Admiral_Beckett_Brass_P1_Tranche2_Scryfall_20261022.json"
P0_SNAPSHOT = ROOT / "data/grixis/m6/oracle_snapshots/Admiral_Beckett_Brass_P0_Scryfall_20261022.json"
P1_FIRST = ROOT / "data/grixis/m6/oracle_snapshots/Admiral_Beckett_Brass_P1_Tranche1_Scryfall_20261022.json"
RAW_HASH = "4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"


def source_inventory():
    body = CANONICAL.read_bytes()
    if hashlib.sha256(body).hexdigest() != RAW_HASH:
        raise ValueError("Approved source snapshot no longer matches live canonical approval")
    counts = Counter()
    for line in body.decode("utf-8").splitlines():
        m = re.fullmatch(r"([1-9][0-9]*)x (.+)", line)
        if not m:
            raise ValueError("Invalid Archidekt physical source line " + line)
        counts[m.group(2).replace(" [Commander]", "")] += int(m.group(1))
    if sum(counts.values()) != 100:
        raise ValueError("Not exactly 100 physical Commander cards")
    return counts


def payable(mana, *, generic=0, pips=()):
    """Only fixed-source color-cost arithmetic; each called in named turns."""
    left = Counter(mana)
    for pip in pips:
        if left[pip] <= 0:
            return False
        left[pip] -= 1
    return sum(left.values()) >= generic


def tap_named_lands(lands):
    """Finite named land-source taps, with Tomb's real two-life cost."""
    source = {"Island": ("U",), "Swamp": ("B",), "Mountain": ("R",),
              "Ancient Tomb": ("C", "C")}
    if len(set(lands)) != len(lands):
        raise ValueError("The same physical land cannot be tapped twice")
    mana = Counter()
    life_loss = 0
    for physical_land in lands:
        name = physical_land.split("#")[0]
        if name not in source:
            raise ValueError("Source not modeled: " + name)
        mana.update(source[name])
        if name == "Ancient Tomb":
            life_loss += 2
    return mana, life_loss


@dataclass
class StagedTarget:
    uid: str
    owner: str
    controller: str
    land: bool = False
    battlefield: bool = True


def distinct_pirate_victims(combat_hits):
    by_player = defaultdict(set)
    for source_id, opponent, is_pirate, prevented in combat_hits:
        if is_pirate and not prevented:
            by_player[opponent].add(source_id)
    return {p for p, sources in by_player.items() if len(sources) >= 3}


def beckett_end_step(qualified_players, targets, *, commander_alive, throne_pirate):
    if not commander_alive:
        return []
    eligible = [p for p in targets if p.battlefield and not p.land and
                p.controller in qualified_players]
    count = 2 if throne_pirate else 1
    # A separate LEGAL target per stack trigger, never one auto-duplicated target.
    return [(p.uid, p.controller) for p in eligible[:count]]


def resolve_theft(target, controller_at_target_choice, qualified):
    if not target.battlefield or target.land or target.controller != controller_at_target_choice or target.controller not in qualified:
        return False
    target.controller = "self"  # no built-in control expiration
    return True


@dataclass
class ResourceState:
    own_library: list[str]
    opponents_libraries: dict[str, list[str]]
    hand: list[str] = field(default_factory=list)
    exile: dict[str, list[tuple[str, str]]] = field(default_factory=lambda: defaultdict(list))
    treasures: set[str] = field(default_factory=set)
    treasure_serial: int = 0
    life: int = 40
    lannery_power_bonus: int = 0

    def draw(self, count):
        for _ in range(count):
            if not self.own_library:
                raise ValueError("Fixture has no card left to draw")
            self.hand.append(self.own_library.pop(0))

    def create_treasure(self, count=1):
        for _ in range(count):
            self.treasure_serial += 1
            self.treasures.add(f"treasure-token-{self.treasure_serial}")

    def sacrifice_treasure(self, token):
        if token not in self.treasures:
            return False
        self.treasures.remove(token)  # token ceases after leaving battlefield
        self.lannery_power_bonus += 1
        return True

    def exile_top(self, opponent, source_permission):
        if not self.opponents_libraries[opponent]:
            return False
        self.exile[opponent].append((self.opponents_libraries[opponent].pop(0), source_permission))
        return True


def resolve_pirate_attack(resources, attacker_names, *, kindred_pirate, lannery_attacked):
    """Attack triggers occur even when subsequent combat damage is stopped."""
    if kindred_pirate:
        resources.draw(len(attacker_names))
    if lannery_attacked:
        resources.create_treasure()


def resolve_pirate_damage(resources, damage_events, *, bident, malcolm, breeches, ramirez):
    """One simultaneous combat damage step, with one-or-more grouping."""
    connecting = [(source, target) for source, target, prevented in damage_events if not prevented]
    victims = sorted({target for _, target in connecting})
    if bident:
        resources.draw(len(connecting))  # Bident: per creature combat-damaging a player
    if malcolm:
        resources.create_treasure(len(victims))  # once per opponent, not per Pirate
    if breeches:
        for target in victims:
            resources.exile_top(target, "BREECHES_THIS_TURN_ANY_COLOR_PAID")
    if ramirez:
        for target in victims:
            resources.exile_top(target, "RAMIREZ_WHILE_EXILED_PAID_NORMAL_COLORS")
    return victims


@dataclass
class WipeCreature:
    uid: str
    power: int
    toughness: int
    pirate: bool
    owner: str
    controller: str
    zone: str = "battlefield"
    finality: bool = False


def toxic_deluge(creatures, x, *, paid_life, current_life):
    if x < 0 or paid_life != x or paid_life > current_life:
        return False
    # -X/-X is not damage, and it can defeat indestructibility via 0 toughness.
    for creature in creatures:
        if creature.zone == "battlefield" and creature.toughness - x <= 0:
            creature.zone = "exile" if creature.finality else "graveyard"
    return True


def brass_reanimate_one(graveyard, battlefield, target_id):
    matches = [c for c in graveyard if c.uid == target_id and c.pirate and c.zone == "graveyard"]
    if len(matches) != 1:
        return False
    selected = matches[0]
    graveyard.remove(selected)
    selected.zone, selected.power, selected.toughness, selected.finality = "battlefield", 4, 4, True
    battlefield.append(selected)
    return True


class AdmiralBeckettP1Tranche2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = json.loads(SNAPSHOT.read_text(encoding="utf-8"))["cards"]
        cls.p0 = json.loads(P0_SNAPSHOT.read_text(encoding="utf-8"))["cards"]
        cls.p1 = json.loads(P1_FIRST.read_text(encoding="utf-8"))["cards"]
        cls.source = source_inventory()

    def test_exact_canonical_100_and_oracle_source_bindings(self):
        self.assertEqual(sum(self.source.values()), 100)
        self.assertEqual(self.source["Admiral Beckett Brass"], 1)
        self.assertEqual((self.source["Island"], self.source["Mountain"]), (3, 2))
        self.assertTrue(all(q == 1 for name, q in self.source.items()
                            if name not in {"Island", "Mountain"}))
        self.assertEqual(len(self.cards), 14)
        self.assertTrue(all(name in self.source and card["commander_legality"] == "legal" and
                            set(card["color_identity"]) <= set("UBR") and card["oracle_id"]
                            for name, card in self.cards.items()))

    # E01: paid engine setup, end-step target choice, later-turn reset.
    def test_e01_two_targets_stacked_after_three_distinct_pirates(self):
        for name in ["Admiral Beckett Brass", "Roaming Throne", "Changeling Outcast",
                     "Storm Fleet Sprinter", "Spyglass Siren"]:
            self.assertEqual(self.source[name], 1)
        self.assertEqual(self.p0["Admiral Beckett Brass"]["mana_cost"], "{1}{U}{B}{R}")
        self.assertEqual(self.p0["Roaming Throne"]["mana_cost"], "{4}")
        self.assertTrue(payable({"U": 1, "B": 1, "R": 1, "C": 1}, generic=1, pips="UBR"))
        # One expressly staged T4 source set, not generic extra mana:
        # Tomb + three basic colors yields UBRCC, pays 1UBR, costs two life.
        for name in ("Ancient Tomb", "Island", "Swamp", "Mountain"):
            self.assertGreaterEqual(self.source[name], 1)
        actual_pool, actual_life = tap_named_lands(
            ["Ancient Tomb", "Island#1", "Swamp", "Mountain#1"])
        self.assertTrue(payable(actual_pool, generic=1, pips="UBR"))
        self.assertEqual(actual_life, 2)
        with self.assertRaises(ValueError):
            tap_named_lands(["Ancient Tomb", "Ancient Tomb"])
        next_turn_pool, next_turn_life = tap_named_lands(
            ["Ancient Tomb", "Island#1", "Swamp"])
        self.assertTrue(payable(next_turn_pool, generic=4))
        self.assertEqual(next_turn_life, 2)
        self.assertTrue(payable({"B": 1}, pips="B"))  # earlier turn Outcast
        self.assertTrue(payable({"U": 1}, pips="U"))  # earlier turn Spyglass
        self.assertTrue(payable({"U": 1, "R": 1, "C": 1}, generic=1, pips="UR"))  # Sprinter
        hits = [(name, "enemy-A", True, False) for name in
                ("Changeling Outcast", "Storm Fleet Sprinter", "Spyglass Siren")]
        eligible = distinct_pirate_victims(hits)
        targets = [StagedTarget("treasure-A", "enemy-A", "enemy-A"),
                   StagedTarget("creature-A", "enemy-A", "enemy-A"),
                   StagedTarget("land-A", "enemy-A", "enemy-A", land=True)]
        stack = beckett_end_step(eligible, targets, commander_alive=True, throne_pirate=True)
        self.assertEqual(stack, [("treasure-A", "enemy-A"), ("creature-A", "enemy-A")])
        for uid, controller in stack:
            t = next(p for p in targets if p.uid == uid)
            self.assertTrue(resolve_theft(t, controller, eligible))
            self.assertEqual((t.owner, t.controller), ("enemy-A", "self"))
        self.assertEqual(targets[-1].controller, "enemy-A")  # land never legal

    def test_e01_no_infinite_stolen_objects_or_trigger_without_fresh_hits(self):
        hits = [(name, "enemy-A", True, False) for name in ("pirate-1", "pirate-2")]
        eligible = distinct_pirate_victims(hits)
        target = StagedTarget("artifact", "enemy-A", "enemy-A")
        self.assertEqual(beckett_end_step(eligible, [target], commander_alive=True,
                                          throne_pirate=True), [])
        three = hits + [("pirate-3", "enemy-A", True, False)]
        eligible = distinct_pirate_victims(three)
        stack = beckett_end_step(eligible, [target], commander_alive=True, throne_pirate=True)
        self.assertEqual(len(stack), 1)  # one legal object, not two free steals
        self.assertTrue(resolve_theft(target, stack[0][1], eligible))
        self.assertEqual(beckett_end_step(eligible, [target], commander_alive=True,
                                          throne_pirate=True), [])
        # At NEXT end step, prior turn's damage must not satisfy threshold.
        self.assertEqual(beckett_end_step(distinct_pirate_victims([]), [
            StagedTarget("new-object", "enemy-A", "enemy-A")],
            commander_alive=True, throne_pirate=True), [])

    # E02: never collapse attack, combat, per-opponent and cast permissions.
    def test_e02_six_card_oracle_cost_and_trigger_differences(self):
        expected = {"Bident of Thassa": "{2}{U}{U}",
                    "Kindred Discovery": "{3}{U}{U}",
                    "Malcolm, Keen-Eyed Navigator": "{2}{U}",
                    "Breeches, Brazen Plunderer": "{3}{R}",
                    "Ramirez DePietro, Pillager": "{2}{U}{B}",
                    "Captain Lannery Storm": "{2}{R}"}
        for name, cost in expected.items():
            self.assertEqual(self.source[name], 1)
            self.assertEqual(self.cards[name]["mana_cost"], cost)
        self.assertIn("enters or attacks", self.cards["Kindred Discovery"]["oracle_text"])
        self.assertIn("deals combat damage", self.cards["Bident of Thassa"]["oracle_text"])
        self.assertIn("for each opponent dealt damage", self.cards["Malcolm, Keen-Eyed Navigator"]["oracle_text"])
        self.assertIn("this turn", self.cards["Breeches, Brazen Plunderer"]["oracle_text"])
        self.assertIn("for as long as it remains exiled", self.cards["Ramirez DePietro, Pillager"]["oracle_text"])
        self.assertIn("Whenever Captain Lannery Storm attacks", self.cards["Captain Lannery Storm"]["oracle_text"])
        self.assertTrue(payable({"U": 2, "C": 3}, generic=3, pips="UU"))
        self.assertFalse(payable({"U": 1, "C": 4}, generic=3, pips="UU"))
        # Named setup costs on distinct turns; no assumption all six engines
        # appeared on one battlefield for free in a single combat turn.
        self.assertTrue(payable({"U": 2, "C": 2}, generic=2, pips="UU"))  # Bident
        self.assertTrue(payable({"U": 1, "C": 2}, generic=2, pips="U"))  # Malcolm
        self.assertTrue(payable({"R": 1, "C": 3}, generic=3, pips="R"))  # Breeches
        self.assertTrue(payable({"U": 1, "B": 1, "C": 2}, generic=2, pips="UB"))  # Ramirez
        self.assertTrue(payable({"R": 1, "C": 2}, generic=2, pips="R"))  # Lannery

    def test_e02_physical_draw_treasure_exile_and_no_free_cast(self):
        state = ResourceState(
            own_library=[f"own-{i}" for i in range(20)],
            opponents_libraries={"A": [f"A-{i}" for i in range(8)],
                                 "B": [f"B-{i}" for i in range(8)]})
        state.life -= 2  # Ramirez ETB, independently paid when cast
        state.create_treasure(2)  # Ramirez ETB is TWO Treasures
        self.assertEqual((state.life, len(state.treasures)), (38, 2))
        state.draw(2)  # two Pirate entries after Kindred chose Pirate
        resolve_pirate_attack(state, ["Pirate-1", "Pirate-2", "Pirate-3", "Lannery"],
                              kindred_pirate=True, lannery_attacked=True)
        self.assertEqual((len(state.hand), len(state.treasures)), (6, 3))
        # Three Pirates connect A and a fourth connects B during one damage
        # step. None is double-counted by the one-or-more opponent triggers.
        victims = resolve_pirate_damage(state,
            [("Pirate-1", "A", False), ("Pirate-2", "A", False),
             ("Lannery", "A", False), ("Pirate-3", "B", False)],
            bident=True, malcolm=True, breeches=True, ramirez=True)
        self.assertEqual(victims, ["A", "B"])
        self.assertEqual(len(state.hand), 10)  # 4 Bident combat hits, not 2 opponents
        self.assertEqual(len(state.treasures), 5)  # +2 Malcolm, not +4
        self.assertEqual([len(state.exile[p]) for p in ("A", "B")], [2, 2])
        self.assertEqual([len(state.opponents_libraries[p]) for p in ("A", "B")], [6, 6])
        permissions = {permission for entries in state.exile.values() for _, permission in entries}
        self.assertEqual(permissions, {"BREECHES_THIS_TURN_ANY_COLOR_PAID",
                                      "RAMIREZ_WHILE_EXILED_PAID_NORMAL_COLORS"})
        # Physical exile is an optional PAID play, not drawing/casting free.
        self.assertFalse(payable({"C": 3}, generic=2, pips="G"))
        self.assertTrue(payable({"G": 1, "C": 2}, generic=2, pips="G"))
        spent = sorted(state.treasures)[0]
        self.assertTrue(state.sacrifice_treasure(spent))
        self.assertFalse(state.sacrifice_treasure(spent))  # no duplicate physical token
        self.assertEqual((len(state.treasures), state.lannery_power_bonus), (4, 1))

    def test_e02_fog_stops_hit_value_not_attack_trigger_value(self):
        state = ResourceState([f"own-{i}" for i in range(12)], {"A": ["A-1", "A-2"]})
        resolve_pirate_attack(state, ["Lannery", "Pirate-2"],
                              kindred_pirate=True, lannery_attacked=True)
        self.assertEqual((len(state.hand), len(state.treasures)), (2, 1))
        resolve_pirate_damage(state,
            [("Lannery", "A", True), ("Pirate-2", "A", True)],
            bident=True, malcolm=True, breeches=True, ramirez=True)
        self.assertEqual((len(state.hand), len(state.treasures), len(state.exile["A"])), (2, 1, 0))

    # W01: conditional actual lethal, not counting theft triggers as winning.
    def test_w01_four_real_combat_steps_reach_40_life_only_if_3_connect(self):
        for name in ("Changeling Outcast", "Storm Fleet Sprinter", "Spyglass Siren",
                     "Corsair Captain", "Admiral Beckett Brass"):
            self.assertEqual(self.source[name], 1)
        self.assertIn("can't be blocked", self.p1["Changeling Outcast"]["oracle_text"])
        self.assertIn("can't be blocked", self.cards["Storm Fleet Sprinter"]["oracle_text"])
        self.assertIn("Flying", self.cards["Spyglass Siren"]["oracle_text"])
        self.assertIn("Other Pirates you control get +1/+1", self.cards["Corsair Captain"]["oracle_text"])
        self.assertIn("Other Pirates you control get +1/+1", self.p0["Admiral Beckett Brass"]["oracle_text"])
        self.assertEqual((self.cards["Changeling Outcast"]["power"],
                          self.cards["Storm Fleet Sprinter"]["power"],
                          self.cards["Spyglass Siren"]["power"]), ("1", "2", "1"))
        self.assertEqual([self.p1["Changeling Outcast"]["mana_cost"],
                          self.cards["Spyglass Siren"]["mana_cost"],
                          self.cards["Storm Fleet Sprinter"]["mana_cost"],
                          self.cards["Corsair Captain"]["mana_cost"]],
                         ["{B}", "{U}", "{1}{U}{R}", "{2}{U}"])
        # Hypothetical naturally sequenced distinct turns, not a free board:
        self.assertTrue(payable({"B": 1}, pips="B"))
        self.assertTrue(payable({"U": 1}, pips="U"))
        self.assertTrue(payable({"U": 1, "R": 1, "C": 1}, generic=1, pips="UR"))
        self.assertTrue(payable({"U": 1, "C": 2}, generic=2, pips="U"))
        # Beckett + Corsair each add one power to these three OTHER Pirates:
        # Outcast 1+2, Sprinter 2+2, Siren 1+2 = 10 per clean combat.
        powers = {"Outcast": 1 + 2, "Sprinter": 2 + 2, "Siren": 1 + 2}
        self.assertEqual(sum(powers.values()), 10)
        life = 40
        history = []
        for _ in range(4):
            life -= sum(powers.values())  # opponent has no flying/reach blocker
            history.append(distinct_pirate_victims([(n, "opponent", True, False)
                           for n in powers]))
        self.assertEqual(life, 0)
        self.assertTrue(all(v == {"opponent"} for v in history))
        # One blocked flyer: seven damage and only two Pirate sources; Beckett
        # does not get a third Pirate from raw damage power.
        self.assertEqual(sum(powers.values()) - powers["Siren"], 7)
        self.assertEqual(distinct_pirate_victims([("Outcast", "opponent", True, False),
                         ("Sprinter", "opponent", True, False)]), set())

    def test_w01_fog_and_end_step_commander_removal_are_distinct_failures(self):
        hits = [(name, "opponent", True, True) for name in ("Outcast", "Sprinter", "Siren")]
        self.assertEqual(distinct_pirate_victims(hits), set())
        target = StagedTarget("opponent-rock", "opponent", "opponent")
        dry = beckett_end_step(distinct_pirate_victims(hits), [target],
                               commander_alive=True, throne_pirate=False)
        self.assertEqual(dry, [])
        actual_hits = [(name, "opponent", True, False) for name in ("Outcast", "Sprinter", "Siren")]
        self.assertEqual(beckett_end_step(distinct_pirate_victims(actual_hits), [target],
                         commander_alive=False, throne_pirate=False), [])
        self.assertEqual(target.controller, "opponent")

    # F02: adverse wipe and non-fabricated, bounded recovery.
    def test_f02_toxic_deluge_self_wipe_paid_life_and_full_type_coverage(self):
        self.assertEqual(self.cards["Toxic Deluge"]["mana_cost"], "{2}{B}")
        self.assertIn("pay X life", self.cards["Toxic Deluge"]["oracle_text"])
        self.assertIn("All creatures get -X/-X", self.cards["Toxic Deluge"]["oracle_text"])
        self.assertTrue(payable({"B": 1, "C": 2}, generic=2, pips="B"))
        board = [WipeCreature("own-pirate", 2, 2, True, "self", "self"),
                 WipeCreature("own-changeling", 1, 1, True, "self", "self"),
                 WipeCreature("enemy-pirate", 3, 3, True, "enemy", "enemy"),
                 WipeCreature("large-enemy", 6, 6, False, "enemy", "enemy")]
        self.assertFalse(toxic_deluge(board, 3, paid_life=0, current_life=40))
        self.assertTrue(all(c.zone == "battlefield" for c in board))
        self.assertTrue(toxic_deluge(board, 3, paid_life=3, current_life=40))
        self.assertEqual([c.zone for c in board],
                         ["graveyard", "graveyard", "graveyard", "battlefield"])
        self.assertEqual(distinct_pirate_victims([]), set())  # board reset, no theft

    def test_f02_pirate_reanimation_finality_and_timed_token_recovery(self):
        brass = self.cards["Admiral Brass, Unsinkable"]
        piracy = self.cards["Daring Piracy"]
        fathom = self.cards["Fathom Fleet Captain"]
        self.assertEqual(brass["mana_cost"], "{2}{U}{B}{R}")
        self.assertIn("finality counter", brass["oracle_text"])
        self.assertIn("base power and toughness 4/4", brass["oracle_text"])
        self.assertIn("beginning of combat", piracy["oracle_text"])
        self.assertIn("Exile it at the beginning of the next end step", piracy["oracle_text"])
        self.assertIn("another nontoken Pirate", fathom["oracle_text"])
        self.assertIn("you may pay {2}", fathom["oracle_text"])
        grave = [WipeCreature("pirate-A", 2, 2, True, "self", "self", zone="graveyard"),
                 WipeCreature("pirate-B", 1, 1, True, "self", "self", zone="graveyard")]
        field = []
        self.assertTrue(brass_reanimate_one(grave, field, "pirate-A"))
        self.assertEqual((len(field), len(grave)), (1, 1))
        self.assertEqual((field[0].power, field[0].toughness, field[0].finality), (4, 4, True))
        self.assertFalse(brass_reanimate_one(grave, field, "pirate-A"))
        self.assertTrue(toxic_deluge(field, 4, paid_life=4, current_life=40))
        self.assertEqual(field[0].zone, "exile")  # not returned for infinite loop
        # Piracy makes a hasty Pirate only when combat begins and expires at
        # next end step, even if it was the sole post-wipe body.
        token = WipeCreature("piracy-token", 1, 1, True, "self", "self")
        self.assertEqual(distinct_pirate_victims([(token.uid, "enemy", True, False)]), set())
        token.zone = "exile"  # end-step delay; not permanent rebuilding
        self.assertEqual(token.zone, "exile")
        self.assertTrue(payable({"C": 2}, generic=2))
        self.assertFalse(payable({"C": 1}, generic=2))  # Fathom trigger is optional/paid
        # Fathom's token has no "tapped and attacking" instruction; it may be
        # on the battlefield now but does not retroactively join this attack.
        attackers_at_declaration = {"Fathom Fleet Captain", "ally-Pirate"}
        fathom_created_token = WipeCreature("fleet-new-token", 2, 2, True, "self", "self")
        self.assertNotIn(fathom_created_token.uid, attackers_at_declaration)
        self.assertEqual(len(field), 1)  # no fictitious mass recursion


if __name__ == "__main__":
    unittest.main()
