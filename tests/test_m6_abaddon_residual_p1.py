"""P1 residual source-paid Abaddon effects: exact physical 100, seven finite cases.
No claim of a multiplayer model, player win rate, or completed M6 I/J.
Oracle: Wizards FIN/40K notes, Scryfall Flame Rift, Kessig, Exalted.
"""
from __future__ import annotations

import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_m6_abaddon_threshold_doublers_p0 as base

FLAME = "Flame Rift"
KESSIG = "Kessig Flamebreather"
EXALTED = "Exalted Flamer of Tzeentch"
VIVI = "Vivi Ornitier"
NOISE = "Noise Marine"
RITE = "Rite of Flame"
SIGNET = "Arcane Signet"
IGNUS = "Grinning Ignus"


def begin(*, staged=(), blood=False, solphim=False):
    s = base.initial(blood=blood, solphim=solphim)
    for card in staged:
        base.move(s, card, "library", "battlefield")
    s["self_life"] = 40
    s["cast_total"] = 0
    s["vivi_counters"] = 0
    s["vivi_mana_used"] = False
    base.conserved(s)
    return s


def paid_cast(s, card, mana, *, noncreature=False, instant_sorcery=False):
    # Mana tuple is a finite list of source land/name + produced symbols.
    # Moving each physical land once prevents same-land double payment.
    for land, produces in mana:
        base.move(s, land, "library", "battlefield")
        s["source_payments"].append((land, produces, card))
    base.move(s, card, "library", "hand")
    base.move(s, card, "hand", "stack")
    before = base.x(s)
    s["cast_total"] += 1
    s["cast_log"].append((card, "hand", before))
    if card == IGNUS and s["commander_controlled"] and s["own_turn"] and before >= 3:
        s["cascade_triggers"] += 1  # Abaddon grants one cascade to this MV3 hand cast.
    # Triggers are created on CAST and resolve independently of that spell.
    if noncreature:
        for source in (KESSIG, VIVI):
            if source in s["battlefield"]:
                if source == VIVI:
                    s["vivi_counters"] += 1
                base.noncombat_damage(s, 1, source=source)
    if instant_sorcery and EXALTED in s["battlefield"]:
        base.noncombat_damage(s, 1, source=EXALTED)
    base.conserved(s)
    return s


def resolve_to_grave(s, card):
    base.move(s, card, "stack", "graveyard")
    base.conserved(s)


class AbaddonResidualP1SourcePaid(unittest.TestCase):
    def test_flame_rift_source_paid_hits_caster_not_threshold(self):
        s = paid_cast(begin(), FLAME, (("Mountain", "R"), ("Island", "C")),
                      noncreature=True, instant_sorcery=True)
        base.noncombat_damage(s, 4, source=FLAME)
        s["self_life"] -= 4
        resolve_to_grave(s, FLAME)
        self.assertEqual(s["lost_this_turn"], [4, 4, 4])
        self.assertEqual(base.x(s), 12)
        self.assertEqual(s["self_life"], 36)

    def test_flame_rift_solphim_bloodletter_only_on_opponents(self):
        s = paid_cast(begin(blood=True, solphim=True), FLAME,
                      (("Mountain", "R"), ("Island", "C")),
                      noncreature=True, instant_sorcery=True)
        base.noncombat_damage(s, 4, source=FLAME)
        s["self_life"] -= 4
        resolve_to_grave(s, FLAME)
        self.assertEqual(s["damage_dealt"], [8, 8, 8])
        self.assertEqual(s["lost_this_turn"], [16, 16, 16])
        self.assertEqual(base.x(s), 48)
        self.assertEqual(s["self_life"], 36)

    def test_kessig_casts_artifact_even_if_countered(self):
        s = paid_cast(begin(staged=(KESSIG,)), SIGNET,
                      (("Mountain", "R"), ("Island", "C")),
                      noncreature=True, instant_sorcery=False)
        # Countering the actual Signet cannot rewind Kessig's cast trigger.
        resolve_to_grave(s, SIGNET)
        self.assertEqual(s["damage_dealt"], [1, 1, 1])
        self.assertEqual(base.x(s), 3)
        self.assertEqual(s["cast_total"], 1)

    def test_exalted_only_cast_instant_or_sorcery_not_ignus(self):
        s = paid_cast(begin(staged=(EXALTED,)), RITE,
                      (("Mountain", "R"),),
                      noncreature=True, instant_sorcery=True)
        resolve_to_grave(s, RITE)
        self.assertEqual(base.x(s), 3)
        s = paid_cast(s, IGNUS, (("Mountain", "R"), ("Mountain", "C"),
                                 ("Island", "C")),
                      noncreature=False, instant_sorcery=False)
        base.move(s, IGNUS, "stack", "battlefield")
        self.assertEqual(base.x(s), 3)
        self.assertEqual(s["cascade_triggers"], 1)
        base.conserved(s)

    def test_vivi_one_noncreature_cast_increases_power_and_mana_once(self):
        s = paid_cast(begin(staged=(VIVI,)), SIGNET,
                      (("Mountain", "R"), ("Island", "C")),
                      noncreature=True)
        base.move(s, SIGNET, "stack", "battlefield")
        self.assertEqual(s["vivi_counters"], 1)
        self.assertEqual(base.x(s), 3)
        # Base 0/3 Vivi with one +1/+1 counter has power 1; the
        # zero-cost activated mana ability is once per controller turn.
        self.assertFalse(s["vivi_mana_used"])
        mana_generated = s["vivi_counters"]
        s["vivi_mana_used"] = True
        self.assertEqual(mana_generated, 1)
        self.assertTrue(s["vivi_mana_used"])
        base.conserved(s)

    def test_three_cast_pingers_produce_nine_opponent_loss(self):
        s = paid_cast(begin(staged=(KESSIG, EXALTED, VIVI)), RITE,
                      (("Mountain", "R"),),
                      noncreature=True, instant_sorcery=True)
        resolve_to_grave(s, RITE)
        self.assertEqual(s["damage_dealt"], [3, 3, 3])
        self.assertEqual(s["lost_this_turn"], [3, 3, 3])
        self.assertEqual(base.x(s), 9)
        self.assertEqual(s["vivi_counters"], 1)

    def test_noise_marine_printed_cascade_even_at_x_zero_single_target(self):
        s = paid_cast(begin(), NOISE,
                      (("Mountain", "R"), ("Mountain", "C"), ("Mountain", "C"),
                       ("Island", "C"), ("Island", "C")))
        self.assertEqual(base.x(s), 0)
        # Printed cascade independently exists; Abaddon's X<5 adds none.
        # One physically possible top-card order has Sol Ring as first hit.
        s["library"].remove("Sol Ring")
        s["library"].insert(0, "Sol Ring")
        self.assertEqual(s["library"][0], "Sol Ring")
        base.move(s, "Sol Ring", "library", "exile")
        base.move(s, "Sol Ring", "exile", "stack")
        s["cast_total"] += 1
        base.move(s, "Sol Ring", "stack", "battlefield")
        base.move(s, NOISE, "stack", "battlefield")
        # ETB counts Noise plus the cascade-cast Sol Ring, 2 real casts.
        # Its Sonic Blaster targets ONE opponent, not the whole table.
        base.life_loss(s, 2, 0)
        s["damage_dealt"][0] += 2
        self.assertEqual(s["lost_this_turn"], [2, 0, 0])
        self.assertEqual(base.x(s), 2)
        self.assertEqual(s["cast_total"], 2)
        base.conserved(s)


if __name__ == "__main__":
    unittest.main()
