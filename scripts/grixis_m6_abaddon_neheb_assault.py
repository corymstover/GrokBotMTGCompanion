#!/usr/bin/env python3
"""Bounded deterministic rules fixture: Abaddon/Neheb/Assault/Loyal Subordinate.

Models only the listed live effects, exact red mana, phase starts, and fixed
response windows. No opening-hand probabilities, opponent AI, full rules engine,
multiplayer win rate, comparative deck performance, or approval authority.
"""
from __future__ import annotations

class OutsideFixture(Exception):
    """Valid Magic lines can be outside this explicitly limited postcombat policy."""

class AssaultCombatTrace:
    def __init__(self, opponents=(40, 40, 40), *,
                 commander=True, loyal=True, neheb=True, assault=True,
                 damage_prevented=False):
        self.opponents = list(opponents)
        self.commander = commander
        self.loyal = loyal
        self.neheb = neheb
        self.assault = assault
        self.damage_prevented = damage_prevented
        self.phase = "precombat_main"
        self.pending_extras = 0
        self.stack = []
        self.life_lost = 0
        self.red = 0
        self.combats = 0
        self.activations = 0
        self.over = False
        self.events = []

    def remove(self, permanent):
        if permanent not in ("commander", "loyal", "neheb", "assault"):
            raise OutsideFixture("Unsupported removal target")
        if not getattr(self, permanent):
            raise ValueError("Permanent absent")
        setattr(self, permanent, False)
        self.events.append(("remove", permanent))

    def scripted_external_loss(self, amounts):
        """Explicit setup only, not an estimated occurrence in a real deck."""
        if self.over or len(amounts) != len(self.opponents):
            raise ValueError("Invalid life-loss setup")
        if any(a < 0 for a in amounts):
            raise ValueError("Life loss cannot be negative")
        for i, amount in enumerate(amounts):
            if self.opponents[i] > 0:
                self.opponents[i] -= amount
                self.life_lost += amount
        self.over = all(x <= 0 for x in self.opponents)
        self.events.append(("scripted_loss", tuple(amounts)))

    def begin_combat(self, *, extra=False):
        if self.over or self.stack:
            raise ValueError("Game over or unresolved stack")
        if extra:
            if self.phase != "postcombat_main" or self.pending_extras < 1:
                raise ValueError("No scheduled extra combat")
            self.pending_extras -= 1
        elif self.phase != "precombat_main":
            raise ValueError("Regular combat only follows precombat main")
        self.red = 0  # Mana from the preceding phase does not carry into combat.
        self.phase = "combat"
        self.combats += 1
        if self.commander and self.loyal:
            self.stack.append("loyal")
        self.events.append(("begin_combat", extra, self.combats))

    def begin_postcombat_main(self):
        if self.phase != "combat" or self.stack:
            raise ValueError("Resolve combat triggers before postcombat main")
        self.red = 0
        self.phase = "postcombat_main"
        # Snapshot trigger existence at phase start. Removal afterward cannot
        # undo a Neheb trigger already put on the stack.
        if self.neheb:
            self.stack.append("neheb")
        self.events.append(("begin_postcombat_main", self.combats))

    def activate_assault(self):
        # Aggravated Assault is also legally activatable in other sorcery
        # windows; those lines are OUTSIDE this postcombat-only experiment.
        if self.phase != "postcombat_main":
            raise OutsideFixture("Only postcombat-main activations modeled")
        if self.over or self.stack or self.pending_extras:
            raise ValueError("Sorcery window/one activation per main required")
        if not self.assault:
            raise ValueError("Aggravated Assault absent")
        if self.red < 5:
            raise ValueError("Cannot pay exact {3}{R}{R} using modeled red")
        self.red -= 5
        self.stack.append("assault")
        self.events.append(("pay_assault", 5, self.red))

    def resolve_top(self):
        if not self.stack:
            raise ValueError("No stack object")
        item = self.stack.pop()
        if item == "loyal":
            # Intervening-if commander clause is rechecked on resolution.
            # The triggered ability persists after its source leaves play.
            if self.commander:
                for i, life in enumerate(self.opponents):
                    if life > 0:
                        self.opponents[i] = life - 3
                        self.life_lost += 3
                self.over = all(x <= 0 for x in self.opponents)
                self.events.append(("loyal_resolved", self.life_lost))
            else:
                self.events.append(("loyal_if_failed", self.life_lost))
        elif item == "neheb":
            self.red += self.life_lost  # Cumulative actual loss as it resolves.
            self.events.append(("neheb_resolved", self.red))
        elif item == "assault":
            # Destroying Assault after activation does not counter the ability.
            self.pending_extras += 1
            self.activations += 1
            self.events.append(("extra_combat_created", self.pending_extras))
        else:
            raise OutsideFixture("Unexpected effect")
        return item

    def next_turn(self):
        if self.stack or self.pending_extras or self.phase != "postcombat_main":
            raise ValueError("Finish pending phases before ending the turn")
        self.life_lost = 0
        self.red = 0
        self.phase = "precombat_main"
        self.events.append(("next_turn", 0))

def complete_four_piece_example():
    """One conditional legal trace, NOT an observed game or likely outcome."""
    s = AssaultCombatTrace()
    s.begin_combat()
    s.resolve_top()
    s.begin_postcombat_main()
    s.resolve_top()
    while not s.over and s.combats < 14:
        s.activate_assault()
        s.resolve_top()
        s.begin_combat(extra=True)
        s.resolve_top()
        if not s.over:
            s.begin_postcombat_main()
            s.resolve_top()
    return s
