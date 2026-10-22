"""P0-030: source-paid conditional Abaddon life-loss / damage replacement proofs.

Nine deterministic fixtures, no randomized wins. The real chosen 100-card
list supplies every tracked physical card; Abaddon sits outside the 99.
Bloodletter replaces life LOSS, Solphim replaces noncombat DAMAGE. No copy
or cascade trigger is invented from these replacement effects.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import hashlib
import json
import unittest

from scripts.grixis_m7_decision_gate import parse_list

ROOT = Path(__file__).resolve().parents[1]
PLAN = json.loads((ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_threshold_doublers_20261022.json").read_text(encoding="utf-8"))
ZONES = ("library", "hand", "battlefield", "stack", "graveyard", "exile")
BLOOD = "Bloodletter of Aclazotz"
SOLPHIM = "Solphim, Mayhem Dominus"
BOLT = "Boltwave"
IGNUS = "Grinning Ignus"
LOYAL = "Loyal Subordinate"
THERMO = "Thermo-Alchemist"


def move(s, name, source, target):
    if name not in s[source]:
        raise AssertionError("Physical card not in expected zone: " + name + " in " + source)
    s[source].remove(name)
    s[target].append(name)


def conserved(s):
    actual = sum((Counter(s[z]) for z in ZONES), Counter())
    if actual != s["original_99"]:
        raise AssertionError("Source-99 physical card multiset drift")


def initial(*, blood=False, solphim=False, loyal=False, thermo=False, own_turn=True):
    path = ROOT / PLAN["candidate_path"]
    if hashlib.sha256(path.read_bytes()).hexdigest() != PLAN["candidate_sha256"]:
        raise AssertionError("Exact chosen M7 100-card source changed")
    cards, commanders, companions = parse_list(path)
    if len(cards) != 100 or commanders != ["Abaddon the Despoiler"] or companions:
        raise AssertionError("Not the staged complete Abaddon 100")
    s = {z: [] for z in ZONES}
    s["library"] = list(cards[1:])
    s.update(original_99=Counter(cards[1:]), opponent_lives=[40, 40, 40],
             lost_this_turn=[0, 0, 0], damage_dealt=[0, 0, 0],
             source_payments=[], own_turn=own_turn, commander_controlled=True,
             cast_log=[], cascade_triggers=0, prevented=set(), stack_events=[])
    for flag, name in ((blood, BLOOD), (solphim, SOLPHIM),
                       (loyal, LOYAL), (thermo, THERMO)):
        if flag:
            move(s, name, "library", "battlefield")
    conserved(s)
    return s


def life_loss(s, amount, index):
    if amount < 0:
        raise AssertionError("Negative life loss unsupported")
    # Bloodletter applies once to the life-loss event, NOT to damage dealt,
    # and only during Bloodletter's controller's turn.
    actual = amount * (2 if s["own_turn"] and BLOOD in s["battlefield"] else 1)
    s["opponent_lives"][index] -= actual
    s["lost_this_turn"][index] += actual
    return actual


def noncombat_damage(s, amount, *, source, prevention=()):
    if source not in s["battlefield"] and source not in s["stack"]:
        raise AssertionError("Damage source not in real physical zone")
    for i in range(3):
        # Solphim changes damage amount, not the amount lost directly.
        damage = amount * (2 if SOLPHIM in s["battlefield"] else 1)
        if i in prevention:
            damage = 0
        s["damage_dealt"][i] += damage
        life_loss(s, damage, i)


def x(s):
    return sum(s["lost_this_turn"])


def cast_paid_boltwave(s, *, countered=False, prevent=()):
    if not s["own_turn"]:
        raise AssertionError("Boltwave is a sorcery: cannot hand cast on opponents' turn here")
    # One of three actual source Mountains pays {R}; no repeated mana credit.
    move(s, "Mountain", "library", "battlefield")
    s["source_payments"].append(("Mountain", "R", BOLT))
    move(s, BOLT, "library", "hand")
    move(s, BOLT, "hand", "stack")
    s["cast_log"].append((BOLT, "hand", x(s)))
    s["cascade_triggers"] += int(s["commander_controlled"] and x(s) >= 1)
    if countered:
        move(s, BOLT, "stack", "graveyard")
        s["stack_events"].append("countered_before_resolution")
    else:
        noncombat_damage(s, 3, source=BOLT, prevention=prevent)
        move(s, BOLT, "stack", "graveyard")
    conserved(s)
    return s


def cast_paid_ignus(s):
    # After the one Mountain paid for Boltwave, the two OTHER Mountains
    # and one Island from the exact 99 pay {2}{R}; no tapped-land reuse.
    if not s["own_turn"]:
        raise AssertionError("Ignus sorcery-speed hand cast not legal in this state")
    for land, mana in (("Mountain", "R"), ("Mountain", "C"), ("Island", "C")):
        move(s, land, "library", "battlefield")
        s["source_payments"].append((land, mana, IGNUS))
    move(s, IGNUS, "library", "hand")
    threshold = x(s)
    move(s, IGNUS, "hand", "stack")
    s["cast_log"].append((IGNUS, "hand", threshold))
    has_cascade = bool(s["commander_controlled"] and threshold >= 3)
    s["cascade_triggers"] += int(has_cascade)
    move(s, IGNUS, "stack", "battlefield")
    conserved(s)
    return has_cascade


class AbaddonThresholdDoublersP0030(unittest.TestCase):
    def test_plain_paid_boltwave_x9(self):
        s = cast_paid_boltwave(initial())
        self.assertEqual(s["damage_dealt"], [3, 3, 3])
        self.assertEqual(s["lost_this_turn"], [3, 3, 3])
        self.assertEqual(x(s), 9)
        self.assertEqual(s["source_payments"], [("Mountain", "R", BOLT)])

    def test_solphim_doubles_damage_x18(self):
        s = cast_paid_boltwave(initial(solphim=True))
        self.assertEqual(s["damage_dealt"], [6, 6, 6])
        self.assertEqual(s["lost_this_turn"], [6, 6, 6])
        self.assertEqual(x(s), 18)

    def test_bloodletter_doubles_loss_not_damage(self):
        s = cast_paid_boltwave(initial(blood=True))
        self.assertEqual(s["damage_dealt"], [3, 3, 3])
        self.assertEqual(s["lost_this_turn"], [6, 6, 6])
        self.assertEqual(x(s), 18)

    def test_both_replacements_x36_once(self):
        s = cast_paid_boltwave(initial(blood=True, solphim=True))
        self.assertEqual(s["damage_dealt"], [6, 6, 6])
        self.assertEqual(s["lost_this_turn"], [12, 12, 12])
        self.assertEqual(s["opponent_lives"], [28, 28, 28])
        self.assertEqual(x(s), 36)

    def test_loyal_loss_only_bloodletter(self):
        s = initial(blood=True, solphim=True, loyal=True)
        self.assertTrue(s["commander_controlled"])
        # Beginning of combat: Loyal's direct life loss is not damage.
        for i in range(3):
            life_loss(s, 3, i)
        self.assertEqual(s["damage_dealt"], [0, 0, 0])
        self.assertEqual(s["lost_this_turn"], [6, 6, 6])
        self.assertEqual(x(s), 18)
        conserved(s)

    def test_prevent_one_opponent_damage(self):
        s = cast_paid_boltwave(initial(blood=True, solphim=True), prevent=(1,))
        self.assertEqual(s["damage_dealt"], [6, 0, 6])
        self.assertEqual(s["lost_this_turn"], [12, 0, 12])
        self.assertEqual(x(s), 24)
        conserved(s)

    def test_countered_boltwave_no_resolved_damage(self):
        s = cast_paid_boltwave(initial(blood=True, solphim=True), countered=True)
        self.assertIn(BOLT, s["graveyard"])
        self.assertEqual(s["damage_dealt"], [0, 0, 0])
        self.assertEqual(s["lost_this_turn"], [0, 0, 0])
        self.assertEqual(s["cascade_triggers"], 0)
        conserved(s)

    def test_opponent_turn_solphim_only(self):
        s = initial(blood=True, solphim=True, thermo=True, own_turn=False)
        # Thermo-Alchemist was controlled since before this turn and untapped.
        noncombat_damage(s, 1, source=THERMO)
        self.assertEqual(s["damage_dealt"], [2, 2, 2])
        self.assertEqual(s["lost_this_turn"], [2, 2, 2])
        self.assertEqual(x(s), 6)
        # Abaddon grants cascade only DURING its controller's own turn.
        self.assertFalse(s["own_turn"])
        self.assertEqual(s["cascade_triggers"], 0)
        conserved(s)

    def test_paid_ignus_after_x36_cascade_snapshot(self):
        s = cast_paid_boltwave(initial(blood=True, solphim=True))
        self.assertEqual(x(s), 36)
        self.assertTrue(cast_paid_ignus(s))
        self.assertEqual(s["cascade_triggers"], 1)
        self.assertEqual(s["cast_log"][-1], (IGNUS, "hand", 36))
        self.assertEqual(len(s["source_payments"]), 4)
        move(s, BLOOD, "battlefield", "graveyard")
        self.assertEqual(x(s), 36)  # historic opponent loss is not undone
        self.assertEqual(s["cascade_triggers"], 1)  # already created on cast
        conserved(s)


if __name__ == "__main__":
    unittest.main()
