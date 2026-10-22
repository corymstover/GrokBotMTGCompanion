#!/usr/bin/env python3
"""Bounded rules fixture: The Ruinous Powers and Abaddon, not game simulation.

The fixture explicitly models owner/controller, zone, normal spell-casting
permission, the delayed Ruinous Powers cast trigger and Abaddon's hand-only
cascade grant. It does not model a full stack, paid mana, opponents' decks,
random targeting, cascade resolution, or game/win rates.
"""
from dataclasses import dataclass


class OutsideFixture(ValueError):
    pass


@dataclass(frozen=True)
class ExiledCard:
    owner: int
    mana_value: int
    kind: str = "sorcery"  # instant, sorcery, creature, or land


class RuinousAbaddonTrace:
    def __init__(self, life=(40, 40, 40), commander=True):
        self.life = list(life)
        self.commander = commander
        self.opponent_loss_this_turn = 0
        self.exiled = None
        self.cast = False
        self.turn = 1
        self.events = []

    def upkeep_exile(self, card):
        if self.exiled is not None:
            raise OutsideFixture("Only one upkeep trigger/card modeled")
        if card.owner not in range(len(self.life)) or card.mana_value < 0:
            raise OutsideFixture("Card owner must be an opponent; MV nonnegative")
        if card.kind not in ("instant", "sorcery", "creature", "land"):
            raise OutsideFixture("Unsupported card type")
        self.exiled = card
        self.cast = False
        self.events.append(("exile_opponent_top", card.owner, card.kind))

    def play_exiled(self, *, main_phase=True, empty_stack=True,
                   mana_paid=True, unused_land_play=True):
        if self.exiled is None or self.cast:
            raise OutsideFixture("No available exiled card")
        c = self.exiled
        if c.kind != "instant" and not (main_phase and empty_stack):
            raise OutsideFixture("Normal timing rules apply to exile permission")
        if c.kind == "land":
            if not unused_land_play:
                raise OutsideFixture("Land play exhausted")
            self.cast = True
            self.events.append(("land_played_not_cast", c.owner))
            return 0
        if not mana_paid:
            raise OutsideFixture("Mana costs still payable; colored mana flexible")
        self.cast = True
        # The trigger occurs on CAST, not on spell resolution. It is shown as
        # resolved in a no-response window, separate from the spell itself.
        self.events.append(("cast_from_exile", c.owner, c.mana_value))
        self.life[c.owner] -= c.mana_value
        self.opponent_loss_this_turn += c.mana_value
        self.events.append(("ruinous_life_loss_trigger_resolves", c.owner, c.mana_value))
        return c.mana_value

    def cast_hand_spell(self, mana_value):
        if mana_value < 0:
            raise OutsideFixture("Negative MV")
        granted = bool(self.commander and mana_value <= self.opponent_loss_this_turn)
        self.events.append(("hand_cast_cascade_grant", mana_value, granted))
        return granted

    def exiled_spell_has_abaddon_cascade(self):
        # Even after Ruinous loss, a spell cast from exile is not from hand.
        return False

    def next_turn(self):
        self.turn += 1
        self.opponent_loss_this_turn = 0
        self.exiled = None
        self.cast = False
        self.events.append(("next_turn_loss_reset", self.turn))
