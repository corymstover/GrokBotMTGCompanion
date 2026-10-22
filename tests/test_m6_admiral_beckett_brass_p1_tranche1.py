"""Four source-bound Admiral Beckett Brass P1 cases: K04/K05/W02/F03.

Finite, adversarial game-state assertions; NOT full Magic priority, paid
gameplay, multiplayer win-rate, aggregate M6 I/J or M7 certification.
Only the eight Scryfall cards in the committed 2026-10-22 P1 snapshot are
re-checked here; preexisting P0 assertions remain in the separate P0 suite.
"""

from collections import defaultdict
from dataclasses import dataclass, field
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "data/grixis/m6/oracle_snapshots/Admiral_Beckett_Brass_P1_Tranche1_Scryfall_20261022.json"
BASELINE_SHA = "4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"


def can_pay(pool, generic, colored=()):
    """Fixed-mana proof for these fixtures, not a mana-production engine."""
    unspent = dict(pool)
    for pip in colored:
        if unspent.get(pip, 0) < 1:
            return False
        unspent[pip] -= 1
    return sum(unspent.values()) >= generic


@dataclass
class Creature:
    uid: str
    creature_types: frozenset[str]
    controller: str
    owner: str
    toughness: int
    changeling: bool = False
    token: bool = False
    indestructible: bool = False
    damage: int = 0
    zone: str = "battlefield"

    def has_type(self, creature_type):
        return self.changeling or creature_type in self.creature_types


def cannonade(creatures):
    """Resolve 2 damage to EACH non-Pirate, then bounded SBA lethality."""
    for creature in creatures:
        if creature.zone != "battlefield" or creature.has_type("Pirate"):
            continue
        creature.damage += 2
        if creature.damage >= creature.toughness and not creature.indestructible:
            creature.zone = "ceased" if creature.token else "graveyard"


def palisade(creatures, chosen_type):
    """Each creature not of chosen type returns to OWNER (tokens cease)."""
    for creature in creatures:
        if creature.zone == "battlefield" and not creature.has_type(chosen_type):
            creature.zone = "ceased" if creature.token else "owner_hand"


@dataclass(frozen=True)
class CombatHit:
    physical_source_id: str
    damaged_player: str
    pirate_at_damage: bool
    prevented: bool = False


def beckett_qualified(history):
    per_player = defaultdict(set)
    for hit in history:
        if hit.pirate_at_damage and not hit.prevented:
            per_player[hit.damaged_player].add(hit.physical_source_id)
    return {player for player, sources in per_player.items() if len(sources) >= 3}


@dataclass
class PortRazerTurn:
    attacked_players: set[str] = field(default_factory=set)
    extra_combats: int = 0
    active_attack: str | None = None
    own_creatures_tapped: dict[str, bool] = field(default_factory=dict)
    other_creatures_tapped: dict[str, bool] = field(default_factory=dict)

    def declare_attack(self, player):
        if player in self.attacked_players or self.active_attack is not None:
            return False
        self.attacked_players.add(player)  # applies even if attack is blocked
        self.active_attack = player
        self.own_creatures_tapped["Port Razer"] = True
        return True

    def deal_combat_damage_to_player(self, *, prevented=False):
        if self.active_attack is None:
            return False
        self.active_attack = None
        if prevented:
            return False
        self.extra_combats += 1
        for uid in self.own_creatures_tapped:
            self.own_creatures_tapped[uid] = False
        return True


@dataclass
class TheftTarget:
    uid: str
    controller: str
    owner: str
    is_land: bool = False
    on_battlefield: bool = True


@dataclass
class EndStepTheftWindow:
    commander_present: bool
    combat_history: list[CombatHit]
    target: TheftTarget
    stack_target_controller: str | None = None

    def begin_end_step(self):
        qualified = beckett_qualified(self.combat_history)
        if (self.commander_present and self.target.on_battlefield and
                not self.target.is_land and self.target.controller in qualified):
            self.stack_target_controller = self.target.controller
            return True
        return False

    def remove_commander(self):
        self.commander_present = False

    def resolve_trigger(self):
        if (self.stack_target_controller is None or not self.target.on_battlefield or
                self.target.is_land or self.target.controller != self.stack_target_controller or
                self.stack_target_controller not in beckett_qualified(self.combat_history)):
            return False
        self.target.controller = "self"
        self.stack_target_controller = None
        return True


def protection_can_answer(name, *, controls_commander, mana, threat_kind,
                          threat_targets_our_creature=False, alternative_target=False):
    """Finite response eligibility; no stack priority engine or target selection AI."""
    costs = {"Fierce Guardianship": (2, ("U",)),
             "Deflecting Swat": (2, ("R",)),
             "Siren Stormtamer": (0, ("U",))}
    generic, colors = costs[name]
    if name == "Fierce Guardianship":
        suitable = threat_kind == "noncreature_spell"
    elif name == "Deflecting Swat":
        suitable = threat_kind in {"targeted_spell", "targeted_ability"} and alternative_target
    else:
        suitable = threat_kind in {"targeted_spell", "targeted_ability"} and threat_targets_our_creature
    free = name in {"Fierce Guardianship", "Deflecting Swat"} and controls_commander
    return suitable and (free or can_pay(mana, generic, colors))


class AdmiralBeckettP1Tranche1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        cls.cards = cls.snapshot["cards"]

    def test_source_binding_and_eight_current_card_identities(self):
        self.assertEqual(self.snapshot["deck_id"], "Admiral_Beckett_Brass")
        self.assertEqual(self.snapshot["canonical_approved_sha256"], BASELINE_SHA)
        self.assertEqual(len(self.cards), 8)
        self.assertTrue(all(len(c["oracle_id"]) == 36 and
                            c["commander_legality"] == "legal" and
                            set(c["color_identity"]) <= set("UBR") and
                            c["api_uri"].startswith("https://api.scryfall.com/cards/")
                            for c in self.cards.values()))

    # K04: changeling is a Pirate in all zones and can connect unblocked.
    def test_k04_changeling_counts_and_different_sources(self):
        oracle = self.cards["Changeling Outcast"]
        self.assertEqual(oracle["mana_cost"], "{B}")
        self.assertIn("every creature type", oracle["oracle_text"])
        self.assertIn("can't block and can't be blocked", oracle["oracle_text"])
        outcast = Creature("outcast-physical-1", frozenset({"Shapeshifter"}),
                           "self", "self", 1, changeling=True)
        self.assertTrue(outcast.has_type("Pirate"))
        self.assertTrue(can_pay({"B": 1}, 0, ("B",)))
        self.assertFalse(can_pay({"C": 1}, 0, ("B",)))
        two_other_hits = [CombatHit("pirate-A", "enemy-A", True),
                          CombatHit("pirate-B", "enemy-A", True)]
        third = CombatHit(outcast.uid, "enemy-A", outcast.has_type("Pirate"))
        self.assertEqual(beckett_qualified(two_other_hits + [third]), {"enemy-A"})
        self.assertEqual(beckett_qualified(two_other_hits + [third, third]), {"enemy-A"})
        self.assertEqual(beckett_qualified(two_other_hits +
                         [CombatHit(outcast.uid, "enemy-B", True)]), set())

    def test_k04_blocked_or_prevented_outcast_no_false_threshold(self):
        allies = [CombatHit("pirate-A", "enemy-A", True),
                  CombatHit("pirate-B", "enemy-A", True)]
        self.assertEqual(beckett_qualified(allies), set())  # killed before damage
        self.assertEqual(beckett_qualified(allies +
                         [CombatHit("outcast", "enemy-A", True, prevented=True)]), set())
        # Ragavan Monkey with no type-changing effect cannot be substituted.
        self.assertEqual(beckett_qualified(allies +
                         [CombatHit("monkey", "enemy-A", False)]), set())

    # K05: BOTH one-sided sweepers require the actual type predicate.
    def test_k05_fiery_cannonade_saves_all_pirates_not_only_ours(self):
        oracle = self.cards["Fiery Cannonade"]
        self.assertEqual((oracle["mana_cost"], oracle["oracle_text"]),
                         ("{2}{R}", "Fiery Cannonade deals 2 damage to each non-Pirate creature."))
        self.assertTrue(can_pay({"R": 1, "C": 2}, 2, ("R",)))
        self.assertFalse(can_pay({"U": 1, "C": 2}, 2, ("R",)))
        own_pirate = Creature("own-P", frozenset({"Pirate"}), "self", "self", 1)
        enemy_pirate = Creature("enemy-P", frozenset({"Pirate"}), "enemy", "enemy", 1)
        changeling = Creature("outcast", frozenset({"Shapeshifter"}), "self", "self", 1, changeling=True)
        monkey = Creature("Ragavan-token", frozenset({"Monkey"}), "self", "self", 1, token=True)
        enemy = Creature("enemy-nonpirate", frozenset({"Wizard"}), "enemy", "enemy", 2)
        sturdy = Creature("enemy-sturdy", frozenset({"Human"}), "enemy", "enemy", 3)
        cannonade([own_pirate, enemy_pirate, changeling, monkey, enemy, sturdy])
        self.assertEqual([x.zone for x in (own_pirate, enemy_pirate, changeling)],
                         ["battlefield"] * 3)
        self.assertEqual((monkey.zone, enemy.zone), ("ceased", "graveyard"))
        self.assertEqual((sturdy.zone, sturdy.damage), ("battlefield", 2))

    def test_k05_palisade_returns_to_owners_and_affects_own_nonpirates(self):
        oracle = self.cards["Raise the Palisade"]
        self.assertEqual(oracle["mana_cost"], "{4}{U}")
        self.assertIn("Return all creatures that aren't of the chosen type", oracle["oracle_text"])
        self.assertTrue(can_pay({"U": 1, "C": 4}, 4, ("U",)))
        self.assertFalse(can_pay({"U": 1, "C": 3}, 4, ("U",)))
        own_pirate = Creature("pirate", frozenset({"Pirate"}), "self", "self", 2)
        enemy_pirate = Creature("enemy-pirate", frozenset({"Pirate"}), "enemy", "enemy", 2)
        outcast = Creature("outcast", frozenset({"Shapeshifter"}), "self", "self", 1, changeling=True)
        stolen = Creature("stolen", frozenset({"Wizard"}), "self", "enemy", 3)
        own_nonpirate = Creature("nonpirate", frozenset({"Human"}), "self", "self", 3)
        token = Creature("token", frozenset({"Goblin"}), "enemy", "enemy", 1, token=True)
        board = [own_pirate, enemy_pirate, outcast, stolen, own_nonpirate, token]
        palisade(board, "Pirate")
        self.assertEqual([x.zone for x in board],
                         ["battlefield", "battlefield", "battlefield", "owner_hand", "owner_hand", "ceased"])
        self.assertEqual(stolen.owner, "enemy")
        # It is not a targeted spell and does not spare our non-Pirates.
        self.assertEqual(oracle["oracle_text"].count("target"), 0)

    # W02: Port Razer's per-player restriction and cross-combat tally.
    def test_w02_port_razer_new_player_combat_only_and_own_untap(self):
        oracle = self.cards["Port Razer"]
        self.assertEqual(oracle["mana_cost"], "{3}{R}{R}")
        self.assertIn("can't attack a player it has already attacked this turn", oracle["oracle_text"])
        self.assertTrue(can_pay({"R": 2, "C": 3}, 3, ("R", "R")))
        self.assertFalse(can_pay({"R": 1, "C": 4}, 3, ("R", "R")))
        turn = PortRazerTurn(own_creatures_tapped={"Port Razer": False, "other Pirate": True},
                             other_creatures_tapped={"enemy-1": True})
        self.assertTrue(turn.declare_attack("enemy-A"))
        self.assertTrue(turn.deal_combat_damage_to_player())
        self.assertEqual(turn.extra_combats, 1)
        self.assertTrue(all(not v for v in turn.own_creatures_tapped.values()))
        self.assertTrue(turn.other_creatures_tapped["enemy-1"])
        self.assertFalse(turn.declare_attack("enemy-A"))
        self.assertTrue(turn.declare_attack("enemy-B"))
        self.assertTrue(turn.deal_combat_damage_to_player())
        self.assertEqual(turn.extra_combats, 2)
        self.assertFalse(turn.declare_attack("enemy-B"))

    def test_w02_no_hit_no_combat_and_distinct_sources_across_phases(self):
        turn = PortRazerTurn(own_creatures_tapped={"Port Razer": True})
        self.assertTrue(turn.declare_attack("enemy-A"))
        self.assertFalse(turn.deal_combat_damage_to_player(prevented=True))
        self.assertEqual(turn.extra_combats, 0)
        self.assertFalse(turn.declare_attack("enemy-A"))
        # Three distinct Pirates may damage enemy A in separate combats;
        # the same Port Razer hitting different players is never three sources.
        hits = [CombatHit("Port Razer", "enemy-A", True),
                CombatHit("Pirate-1", "enemy-A", True),
                CombatHit("Pirate-2", "enemy-A", True),
                CombatHit("Port Razer", "enemy-B", True)]
        self.assertEqual(beckett_qualified(hits), {"enemy-A"})
        self.assertEqual(beckett_qualified(hits[:1] * 3), set())

    # F03: command-zone tax, removal window, and protection's real targets.
    def test_f03_commander_removal_timing_and_source_paid_recast(self):
        self.assertTrue(can_pay({"U": 1, "B": 1, "R": 1, "C": 1}, 1, ("U", "B", "R")))
        self.assertFalse(can_pay({"U": 1, "B": 1, "R": 1, "C": 1}, 3, ("U", "B", "R")))
        self.assertTrue(can_pay({"U": 1, "B": 1, "R": 1, "C": 3}, 3, ("U", "B", "R")))
        self.assertEqual([4 + 2 * n for n in range(3)], [4, 6, 8])
        qualifying_sources = [CombatHit(str(i), "enemy-A", True) for i in range(3)]
        self.assertEqual(beckett_qualified(qualifying_sources), {"enemy-A"})
        # Pre-end-step removal prevents a trigger entirely.
        removed_before = EndStepTheftWindow(True, qualifying_sources,
                         TheftTarget("opponent-artifact", "enemy-A", "enemy-A"))
        removed_before.remove_commander()
        self.assertFalse(removed_before.begin_end_step())
        self.assertFalse(removed_before.resolve_trigger())
        # A triggered ability already on the stack is independent of Beckett's
        # later presence, but the opponent must still control its legal target.
        removed_after = EndStepTheftWindow(True, qualifying_sources,
                         TheftTarget("opponent-artifact", "enemy-A", "enemy-A"))
        self.assertTrue(removed_after.begin_end_step())
        removed_after.remove_commander()
        self.assertTrue(removed_after.resolve_trigger())
        self.assertEqual((removed_after.target.owner, removed_after.target.controller),
                         ("enemy-A", "self"))
        sacrificed = EndStepTheftWindow(True, qualifying_sources,
                      TheftTarget("opponent-artifact-2", "enemy-A", "enemy-A"))
        self.assertTrue(sacrificed.begin_end_step())
        sacrificed.target.on_battlefield = False
        self.assertFalse(sacrificed.resolve_trigger())

    def test_f03_swat_fierce_and_stormtamer_are_conditional(self):
        swat = self.cards["Deflecting Swat"]
        fierce = self.cards["Fierce Guardianship"]
        siren = self.cards["Siren Stormtamer"]
        self.assertIn("target spell or ability", swat["oracle_text"])
        self.assertIn("Counter target noncreature spell", fierce["oracle_text"])
        self.assertIn("{U}, Sacrifice this creature", siren["oracle_text"])
        self.assertTrue(can_pay({"R": 1, "C": 2}, 2, ("R",)))
        self.assertFalse(can_pay({"C": 3}, 2, ("R",)))
        self.assertTrue(can_pay({"U": 1, "C": 2}, 2, ("U",)))
        self.assertFalse(can_pay({"C": 3}, 2, ("U",)))
        # Free option for either spell requires controlling a commander;
        # Fierce's target is a noncreature SPELL, never a creature or ETB.
        self.assertTrue(protection_can_answer("Fierce Guardianship",
                 controls_commander=True, mana={}, threat_kind="noncreature_spell"))
        self.assertFalse(protection_can_answer("Fierce Guardianship",
                 controls_commander=False, mana={}, threat_kind="noncreature_spell"))
        self.assertTrue(protection_can_answer("Fierce Guardianship",
                 controls_commander=False, mana={"U": 1, "C": 2},
                 threat_kind="noncreature_spell"))
        self.assertFalse(protection_can_answer("Fierce Guardianship",
                 controls_commander=True, mana={}, threat_kind="creature_spell"))
        self.assertFalse(protection_can_answer("Fierce Guardianship",
                 controls_commander=True, mana={}, threat_kind="targeted_ability"))
        # Swat can target a spell with no targets, but changing none of them
        # cannot actually protect Beckett from an untargeted wrath.
        self.assertFalse(protection_can_answer("Deflecting Swat",
                 controls_commander=True, mana={}, threat_kind="noncreature_spell"))
        self.assertFalse(protection_can_answer("Deflecting Swat",
                 controls_commander=True, mana={}, threat_kind="targeted_spell",
                 alternative_target=False))
        self.assertTrue(protection_can_answer("Deflecting Swat",
                 controls_commander=True, mana={}, threat_kind="targeted_spell",
                 alternative_target=True))
        # Stormtamer counters only a spell/ability targeting self or an own
        # creature, consumes U and itself (one fewer attacker for threshold).
        self.assertTrue(protection_can_answer("Siren Stormtamer",
                 controls_commander=False, mana={"U": 1},
                 threat_kind="targeted_ability", threat_targets_our_creature=True))
        self.assertFalse(protection_can_answer("Siren Stormtamer",
                 controls_commander=True, mana={"C": 1},
                 threat_kind="targeted_ability", threat_targets_our_creature=True))
        self.assertFalse(protection_can_answer("Siren Stormtamer",
                 controls_commander=True, mana={"U": 1},
                 threat_kind="noncreature_spell", threat_targets_our_creature=False))
        damage_after_sacrifice = [CombatHit("pirate-A", "enemy-A", True),
                                  CombatHit("pirate-B", "enemy-A", True)]
        self.assertEqual(beckett_qualified(damage_after_sacrifice), set())

    def test_f03_greaves_shroud_requires_sorcery_speed_equip(self):
        oracle = self.cards["Lightning Greaves"]
        self.assertEqual(oracle["mana_cost"], "{2}")
        self.assertIn("haste and shroud", oracle["oracle_text"])
        self.assertIn("Equip {0}", oracle["oracle_text"])
        self.assertTrue(can_pay({"C": 2}, 2))
        greaves_pre_equipped = True
        beckett_legal_target_for_removal = not greaves_pre_equipped
        self.assertFalse(beckett_legal_target_for_removal)
        # Equip is sorcery speed; do not assert it can be moved during an
        # opponent's instant-speed removal response window.
        def can_equip(*, own_main, empty_stack, priority):
            return own_main and empty_stack and priority
        self.assertFalse(can_equip(own_main=False, empty_stack=False, priority=True))
        self.assertFalse(can_equip(own_main=True, empty_stack=False, priority=True))
        self.assertTrue(can_equip(own_main=True, empty_stack=True, priority=True))
        # Shroud blocks our own target spells/abilities as well as opponents'.
        self.assertFalse(beckett_legal_target_for_removal)


if __name__ == "__main__":
    unittest.main()
