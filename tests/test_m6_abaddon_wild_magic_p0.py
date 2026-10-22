"""Abaddon P0-024: eight preregistered Wild-Magic Sorcerer on-cast tests.

Actual 99 named source cards are physically conserved across every trace.
Only known Oracle interactions are modeled, never arbitrary game outcomes.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

from scripts.grixis_m7_decision_gate import parse_list

ROOT = Path(__file__).resolve().parents[1]
PLAN = json.loads((ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_wild_magic_20261022.json").read_text())
CALL = "Call Forth the Tempest"
WILD = "Wild-Magic Sorcerer"
LOST = "The Lost and the Damned"
LOYAL = "Loyal Subordinate"
LANDS = ("Mountain",)*3 + ("Island",)*3 + ("Swamp",)*2
MV = {"Arcane Signet": 2, "Sol Ring": 1, "Talisman of Creativity": 2,
      "Lotus Petal": 0, WILD: 4}
ZONES = ("library", "hand", "field", "stack", "exile", "graveyard")


def current_multiset(s):
    return sum((Counter(s[z]) for z in ZONES), Counter())


def move(s, card, frm, to):
    if card not in s[frm]:
        raise AssertionError("Physical card not present: "+card+" in "+frm)
    s[frm].remove(card)
    s[to].append(card)


def stage(*, loss=9, wild_before=True, top=("Arcane Signet","Sol Ring",
             "Talisman of Creativity","Lotus Petal")):
    path = ROOT / PLAN["candidate_path"]
    if hashlib.sha256(path.read_bytes()).hexdigest()!=PLAN["candidate_sha256"]:
        raise AssertionError("Exact 100-card research challenger SHA changed")
    cards, commander, companions = parse_list(path)
    if len(cards)!=100 or len(set(cards))!=94 or commander!=["Abaddon the Despoiler"] or companions:
        raise AssertionError("Cannot source actual registered Abaddon 100")
    s={z: [] for z in ZONES}
    s["library"]=list(cards[1:])
    s.update({
        "original":Counter(cards[1:]),"loss":loss,"tapped":[],
        "cast_history":[],"exile_casts":[],"cascade_triggers":[],
        "cascade_scans":[],"stack_log":[],"nested_cascades":0,
        "nested_empty_cascades":0,"virtual_lost_spawns":0,
        "source_countered":False,"call_creature_damage":None,
        "wild_removed":False,"first_exile_spell":None,
        "opponent_effects_are_conditional":True})
    move(s,CALL,"library","hand")
    move(s,LOST,"library","field")
    if wild_before:
        move(s,WILD,"library","field")
    if loss==9:
        move(s,LOYAL,"library","field") # prior resolved combat trigger: 3 each
    elif loss!=0:
        raise AssertionError("Only two preregistered Abaddon loss preconditions")
    for land in LANDS:
        move(s,land,"library","field")
    # A chosen attainable top order; every named hit is taken from the same 99.
    for card in reversed(top):
        if card not in s["library"]:
            raise AssertionError("Chosen cascade hit absent from remaining source: "+card)
        s["library"].remove(card)
        s["library"].insert(0,card)
    assert current_multiset(s)==s["original"]
    return s


def scan(s, limit, *, zero_exhaustion=False):
    """Exile until strictly lower MV; virtual ability not a physical object."""
    exiled=[]
    hit=None
    while s["library"]:
        x=s["library"].pop(0)
        s["exile"].append(x)
        exiled.append(x)
        if limit==0:
            continue
        if x not in MV:
            raise AssertionError("Unregistered source was reached; do not invent its MV: "+x)
        if MV[x]<limit:
            hit=x
            break
    if zero_exhaustion:
        if limit!=0 or hit is not None or s["library"]:
            raise AssertionError("Zero-MV cascade must inspect entire remaining library")
        s["nested_empty_cascades"]+=1
    elif hit is None:
        raise AssertionError("Source-bounded physical hit unexpectedly absent")
    s["cascade_scans"].append((limit,tuple(exiled),hit))
    return exiled,hit


def bottom(s, exiled, *, put_first=()):
    """A specified *possible* random-bottom permutation; no odds implied."""
    remaining=[x for x in exiled if x in s["exile"]]
    order=list(put_first)
    for x in order:
        if x not in remaining:
            raise AssertionError("Chosen possible shuffle prefix absent from exile")
        remaining.remove(x)
    order+=remaining
    for x in order:
        move(s,x,"exile","library")
    s["stack_log"].append(("bottom",tuple(order[:5]),len(order)))


def cast_exile(s,card,*,counter_first=False,remove_wild_first=False):
    is_first = not s["exile_casts"]
    will_gain_wild = bool(is_first and WILD in s["field"])
    move(s,card,"exile","stack")
    s["exile_casts"].append(card)
    s["cast_history"].append((card,MV[card],"cascade_exile"))
    s["virtual_lost_spawns"]+=int(LOST in s["field"])
    s["stack_log"].append(("cast_exile",card,"wild_granted" if will_gain_wild else "ordinary"))
    if is_first:
        s["first_exile_spell"]=card
    if remove_wild_first:
        if not is_first or not will_gain_wild:
            raise AssertionError("Only registered first-spell Sorcerer removal")
        move(s,WILD,"field","graveyard")
        s["wild_removed"]=True
    if counter_first:
        if not is_first or not will_gain_wild:
            raise AssertionError("Only first granted exile spell may be countered")
        move(s,card,"stack","graveyard")
        s["stack_log"].append(("counter_after_cast",card))
    if will_gain_wild:
        # The granted triggered ability is on the stack even if Wild has left
        # or its original spell has been countered. Resolve it before the spell.
        s["nested_cascades"]+=1
        s["cascade_triggers"].append(("wild_nested",card))
        s["stack_log"].append(("wild_trigger",card))
        exiled, hit=scan(s,MV[card],zero_exhaustion=(MV[card]==0))
        if hit is not None:
            cast_exile(s,hit)
        # On an exhausted zero-MV cascade, a random-bottom permutation COULD
        # yield the next separately prearranged original-Call hit. This is a
        # conditional possible ordering, not a draw-probability sample.
        choose=("Arcane Signet","Talisman of Creativity") if MV[card]==0 else ()
        bottom(s,exiled,put_first=choose)
    if card in s["stack"]:
        move(s,card,"stack","field") # registered hits are artifacts/creature
        s["stack_log"].append(("resolve_exile_spell",card))
    else:
        s["stack_log"].append(("original_spell_countered_nested_still_resolved",card))


def run(s,*,drannith=False,rule_of_law=False,counter_call=False,
        counter_first=False,remove_wild_first=False):
    if s["tapped"] or any(Counter(s["field"])[n]<v for n,v in Counter(LANDS).items()):
        raise AssertionError("Cannot pay {5}{R}{R}{R} with actual untapped sources")
    # Tap the exact 3 red + five off-color generic source lands on cast.
    s["tapped"].extend(LANDS)
    move(s,CALL,"hand","stack")
    s["cast_history"].append((CALL,8,"hand"))
    count=2+int(s["loss"]>=8)
    s["cascade_triggers"].extend([("call_printed",1),("call_printed",2)])
    if count==3:
        s["cascade_triggers"].append(("abaddon_granted",3))
    s["stack_log"].append(("call_hand_cast",s["loss"],count))
    if counter_call:
        move(s,CALL,"stack","graveyard")
        s["source_countered"]=True
    for i in range(count):
        s["stack_log"].append(("resolve_outer_cascade",i+1))
        exiled,hit=scan(s,8)
        if hit and not (drannith or rule_of_law):
            cast_exile(s,hit,counter_first=counter_first and i==0,
                       remove_wild_first=remove_wild_first and i==0)
        bottom(s,exiled)
    if CALL in s["stack"]:
        s["call_creature_damage"]=sum(mv for name,mv,_ in s["cast_history"] if name!=CALL)
        move(s,CALL,"stack","graveyard")
    else:
        s["call_creature_damage"]=None
    if s["exile"] or s["stack"] or current_multiset(s)!=s["original"]:
        raise AssertionError("Original 99 card zones not conserved")
    return s


class AbaddonWildMagicP0024(unittest.TestCase):
    def test_wild_x9_first_nested_three_printed(self):
        s=run(stage())
        self.assertEqual(s["exile_casts"],
                         ["Arcane Signet","Sol Ring","Talisman of Creativity","Lotus Petal"])
        self.assertEqual(s["nested_cascades"],1)
        self.assertEqual(len([x for x in s["cascade_triggers"] if x[0].startswith("call_") or x[0]=="abaddon_granted"]),3)
        self.assertEqual(s["virtual_lost_spawns"],4)
        self.assertEqual(s["call_creature_damage"],5)
        self.assertEqual(s["first_exile_spell"],"Arcane Signet")

    def test_wild_x0_printed_nested_only(self):
        s=run(stage(loss=0))
        self.assertEqual(s["nested_cascades"],1)
        self.assertEqual(s["exile_casts"],["Arcane Signet","Sol Ring","Talisman of Creativity"])
        self.assertEqual(s["virtual_lost_spawns"],3)
        self.assertEqual(s["call_creature_damage"],5)

    def test_wild_first_mv0_zero_eligible(self):
        s=run(stage(top=("Lotus Petal","Arcane Signet","Talisman of Creativity")))
        self.assertEqual(s["first_exile_spell"],"Lotus Petal")
        self.assertEqual(s["nested_cascades"],1)
        self.assertEqual(s["nested_empty_cascades"],1)
        scans=[row for row in s["cascade_scans"] if row[0]==0]
        self.assertEqual(len(scans),1)
        self.assertIsNone(scans[0][2])
        # A zero-MV nested cascade exhausts all then returns actual cards:
        self.assertGreaterEqual(len(scans[0][1]),80)
        self.assertEqual(s["exile_casts"],["Lotus Petal","Arcane Signet","Talisman of Creativity"])

    def test_wild_arrives_after_first_exile_cast(self):
        s=run(stage(loss=0,wild_before=False,
                    top=(WILD,"Arcane Signet")))
        self.assertEqual(s["exile_casts"],[WILD,"Arcane Signet"])
        self.assertEqual(s["nested_cascades"],0)
        self.assertIn(WILD,s["field"])
        self.assertEqual(s["call_creature_damage"],6)

    def test_wild_removed_after_granted_cascade(self):
        s=run(stage(),remove_wild_first=True)
        self.assertEqual(s["nested_cascades"],1)
        self.assertEqual(s["exile_casts"][:2],["Arcane Signet","Sol Ring"])
        self.assertTrue(s["wild_removed"])
        self.assertIn(WILD,s["graveyard"])

    def test_wild_countered_original_call(self):
        s=run(stage(),counter_call=True)
        self.assertTrue(s["source_countered"])
        self.assertEqual(s["nested_cascades"],1)
        self.assertEqual(len(s["exile_casts"]),4)
        self.assertIsNone(s["call_creature_damage"])
        self.assertIn(CALL,s["graveyard"])

    def test_wild_drannith_and_rule_of_law(self):
        for policy in ("drannith","rule_of_law"):
            with self.subTest(policy=policy):
                s=run(stage(),**{policy:True})
                self.assertEqual(s["nested_cascades"],0)
                self.assertEqual(s["exile_casts"],[])
                self.assertEqual(s["virtual_lost_spawns"],0)
                self.assertEqual(s["call_creature_damage"],0)
                self.assertEqual(len(s["cascade_scans"]),3)

    def test_wild_countered_first_exile_spell(self):
        s=run(stage(),counter_first=True)
        self.assertEqual(s["nested_cascades"],1)
        self.assertIn("Arcane Signet",s["graveyard"])
        self.assertIn("Sol Ring",s["field"])
        self.assertEqual(s["exile_casts"][:2],["Arcane Signet","Sol Ring"])
        self.assertEqual(s["call_creature_damage"],5)


if __name__=="__main__":
    unittest.main()
