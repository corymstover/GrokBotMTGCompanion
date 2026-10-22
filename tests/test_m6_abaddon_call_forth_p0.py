"""P0-021 exact-99 physical source-paid Call Forth cascade stack tests.

Bounded conditional rules trace, NOT a full game/win-rate emulator.
Eight cases preregistered before implementation.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import unittest

from scripts.grixis_m7_decision_gate import parse_list

ROOT=Path(__file__).resolve().parents[1]
PLAN_PATH=ROOT/"data/grixis/m6/phase_b_plans/abaddon_p0_call_forth_20261022.json"
PLAN=json.loads(PLAN_PATH.read_text(encoding="utf-8"))
CALL="Call Forth the Tempest"
COMMANDER="Abaddon the Despoiler"
LOST="The Lost and the Damned"
KEEPER="Keeper of Secrets"
LOYAL="Loyal Subordinate"
HITS=(("Sol Ring",1),("Arcane Signet",2),("Talisman of Creativity",2))
HIT_MV=dict(HITS)
START_LANDS=["Mountain"]*3+["Island"]*3+["Swamp"]*2
ZONES=("library","hand","field","stack","graveyard","exile")


def physical_count(state):
    return sum((Counter(state[z]) for z in ZONES),Counter())


def move(state,card,source,target):
    if card not in state[source]:
        raise AssertionError(f"Physical {card} not present in {source}")
    state[source].remove(card)
    state[target].append(card)


def stage(*,life_source="loyal",previous_boltwave=False):
    """Only real cards from the preferred 99; opponent behavior is conditional."""
    path=ROOT/PLAN["candidate_path"]
    if hashlib.sha256(path.read_bytes()).hexdigest()!=PLAN["candidate_sha256"]:
        raise AssertionError("Exact contender SHA changed")
    cards,cmd,comp=parse_list(path)
    if len(cards)!=100 or cmd!=[COMMANDER] or comp:
        raise AssertionError("Wrong full contender list")
    original=Counter(cards[1:])
    s={z:[] for z in ZONES}
    s["library"]=list(cards[1:])
    s.update({"commander_controlled":True,"lands_tapped":[],"loss":0,
              "cast_history":[],"pending":[],"timeline":[],
              "lost_spawn":0,"keeper_targeted_damage":0,
              "opposing_creature_damage":None,"source_countered":False,
              "initial_cascade_count":None,"cascade_casts":[],"skipped_lands":[]})
    move(s,CALL,"library","hand")
    move(s,LOST,"library","field")
    for l in START_LANDS:
        move(s,l,"library","field")
        s["lands_tapped"].append(l)
    assert Counter(s["lands_tapped"])==Counter(START_LANDS)
    if previous_boltwave:
        move(s,"Boltwave","library","graveyard")
        s["cast_history"].append(("Boltwave",1,"hand"))
        s["loss"]=9  # actual Boltwave 3 damage to each of three opponents
    elif life_source=="loyal":
        move(s,LOYAL,"library","field")
        s["loss"]=9  # resolved lieutenant beginning-of-combat trigger 3 per opponent
    elif life_source=="keeper_plus_kessig":
        move(s,KEEPER,"library","field")
        move(s,"Kessig Flamebreather","library","field")
        s["loss"]=7  # stipulated unblocked 6 + 1 combat to same opponent
    elif life_source=="keeper_plus_storm":
        move(s,KEEPER,"library","field")
        move(s,"Storm-Kiln Artist","library","field")
        s["loss"]=8  # stipulated unblocked 6 + 2 combat to same opponent
    elif life_source=="none":
        s["loss"]=0
    else:
        raise AssertionError("Unregistered loss origin")
    # Deterministic opportunity only; use actual physical Swamp not spent as land.
    # First cascade exiles Swamp then Sol Ring; the following two hits each
    # must use a DIFFERENT actual physical card (Arcane Signet then Talisman).
    for name in reversed(("Swamp",)+tuple(n for n,_ in HITS)):
        move(s,name,"library","hand") # avoid synthetic card injection
        move(s,name,"hand","library")
        s["library"].remove(name)
        s["library"].insert(0,name)
    if physical_count(s)!=original:
        raise AssertionError("Fixture materialized or lost a source card")
    return s,original


def execute(s,original,*,drannith=False,rule_of_law=False,counter_source=False,copied_mvs=()):
    """Real paid MV8 hand spell; interleave each cascade and cast/hit resolution.

    Abaddon checks X once when Call is cast. A later Keeper trigger cannot
    retrospectively create a third instance of cascade.
    """
    if not (s["commander_controlled"] and
            Counter(s["lands_tapped"])==Counter(START_LANDS)):
        raise AssertionError("No 5 generic + 3 red physical sources")
    if s["loss"]<0:
        raise AssertionError("Negative threshold")
    at_cast=s["loss"]
    move(s,CALL,"hand","stack")
    s["cast_history"].append((CALL,8,"hand"))
    triggers=["printed_2","printed_1"]
    if at_cast>=8:
        triggers.insert(0,"Abaddon_granted")
    s["initial_cascade_count"]=len(triggers)
    s["pending"]=list(triggers)  # list tail is stack top; first printed ability top
    s["timeline"].append(("call_cast",at_cast,len(triggers)))
    if counter_source:
        move(s,CALL,"stack","graveyard")
        s["source_countered"]=True
        s["timeline"].append(("opponent_counter_call_before_cascade",))
    while s["pending"]:
        label=s["pending"].pop()
        s["timeline"].append(("resolve_cascade",label))
        exiled=[]
        hit=None
        while s["library"]:
            card=s["library"].pop(0)
            s["exile"].append(card)
            exiled.append(card)
            if card in HIT_MV:
                hit=card
                break
            # Prepared first skipped Swamp is the only intentional skip; fail
            # closed for other card effects instead of silently zeroing them.
            if card!="Swamp":
                raise AssertionError("Hit fixture drift (unmodeled card): "+card)
        if hit is None:
            raise AssertionError("Precommitted cascade failed to find real low-MV hit")
        if HIT_MV[hit]>=8:
            raise AssertionError("Cascade hit invalid MV")
        can_cast=not drannith and not rule_of_law
        s["timeline"].append(("exiled",label,tuple(exiled),can_cast))
        if can_cast:
            move(s,hit,"exile","stack")
            s["timeline"].append(("cast_free",hit,label))
            s["cast_history"].append((hit,HIT_MV[hit],"cascade_exile"))
            s["cascade_casts"].append(hit)
            s["lost_spawn"]+=int(LOST in s["field"])
            if KEEPER in s["field"]:
                # Trigger resolves before cascade-hit spell; one target opponent.
                s["keeper_targeted_damage"]+=HIT_MV[hit]
                s["loss"]+=HIT_MV[hit]
            move(s,hit,"stack","field")  # the three selected hits are artifacts
            s["timeline"].append(("resolve_hit",hit,label))
        bottom=[name for name in exiled if name in s["exile"]]
        random.Random(21021+len(s["cascade_casts"])*7+len(s["pending"])).shuffle(bottom)
        for name in bottom:
            move(s,name,"exile","library")
        if "Swamp" in bottom:
            s["skipped_lands"].append("Swamp")
    if not s["source_countered"]:
        # The eight-mana original source spell is NOT included in its own
        # damage. Spells countered after cast WOULD still count.
        s["opposing_creature_damage"]=sum(mv for n,mv,zone in s["cast_history"] if n!=CALL)
        move(s,CALL,"stack","graveyard")
        s["timeline"].append(("call_resolved",s["opposing_creature_damage"]))
    else:
        s["opposing_creature_damage"]=None
    # Copies were NOT cast: do not append copied_mvs to cast_history.
    if any(not isinstance(x,int) or x<0 for x in copied_mvs):
        raise AssertionError("Invalid copied mana values")
    if physical_count(s)!=original:
        raise AssertionError("Physical 99 cards drifted after all cascades")
    if s["exile"] or s["stack"] or s["pending"]:
        raise AssertionError("Temporary stack/exile zone not cleaned up")
    return s


class AbaddonCallForthP0021(unittest.TestCase):
    def test_call_x9_legal_three_separate(self):
        s,original=stage()
        execute(s,original)
        self.assertEqual(s["initial_cascade_count"],3)
        self.assertEqual(s["cascade_casts"],[x[0] for x in HITS])
        self.assertEqual(s["opposing_creature_damage"],5)
        self.assertEqual(s["lost_spawn"],3)
        self.assertEqual(s["skipped_lands"],["Swamp"])
        self.assertEqual([e[0] for e in s["timeline"] if e[0]=="resolve_cascade"],
                         ["resolve_cascade"]*3)
        self.assertEqual(len([e for e in s["timeline"] if e[0]=="resolve_hit"]),3)
        self.assertEqual(s["library"][-1],"Swamp")

    def test_call_x7_no_retroactive_grant(self):
        s,original=stage(life_source="keeper_plus_kessig")
        execute(s,original)
        self.assertEqual(s["initial_cascade_count"],2)
        self.assertEqual(s["cascade_casts"],["Sol Ring","Arcane Signet"])
        self.assertEqual(s["keeper_targeted_damage"],3)
        self.assertGreaterEqual(s["loss"],8)
        self.assertEqual(s["opposing_creature_damage"],3)
        self.assertEqual(s["lost_spawn"],2)

    def test_call_x8_grant_boundary(self):
        s,original=stage(life_source="keeper_plus_storm")
        execute(s,original)
        self.assertEqual(s["initial_cascade_count"],3)
        self.assertEqual(s["keeper_targeted_damage"],5)
        self.assertEqual(s["opposing_creature_damage"],5)

    def test_call_x0_printed_still_trigger(self):
        s,original=stage(life_source="none")
        execute(s,original)
        self.assertEqual(s["initial_cascade_count"],2)
        self.assertEqual(s["opposing_creature_damage"],3)
        self.assertEqual(s["lost_spawn"],2)

    def test_call_drannith_three_triggers_no_hits_cast(self):
        s,original=stage()
        execute(s,original,drannith=True)
        self.assertEqual(s["initial_cascade_count"],3)
        self.assertEqual(s["cascade_casts"],[])
        self.assertEqual(s["opposing_creature_damage"],0)
        self.assertEqual(s["lost_spawn"],0)
        self.assertNotIn("Sol Ring",s["field"])

    def test_call_rule_of_law_no_free_spells(self):
        s,original=stage()
        execute(s,original,rule_of_law=True)
        self.assertEqual(s["initial_cascade_count"],3)
        self.assertEqual(s["cascade_casts"],[])
        self.assertEqual(s["opposing_creature_damage"],0)
        self.assertEqual(s["lost_spawn"],0)

    def test_call_countered_source_independent_triggers(self):
        s,original=stage()
        execute(s,original,counter_source=True)
        self.assertTrue(s["source_countered"])
        self.assertEqual(s["initial_cascade_count"],3)
        self.assertEqual(s["cascade_casts"],[x[0] for x in HITS])
        self.assertIsNone(s["opposing_creature_damage"])
        self.assertEqual(s["lost_spawn"],3)
        self.assertIn(CALL,s["graveyard"])

    def test_call_casted_spells_before_resolve_not_copies(self):
        s,original=stage(previous_boltwave=True)
        execute(s,original,copied_mvs=(4,99))
        self.assertEqual(s["initial_cascade_count"],3)
        self.assertEqual(s["opposing_creature_damage"],6)
        self.assertEqual(s["loss"],9)
        self.assertEqual(s["cast_history"][0],("Boltwave",1,"hand"))
        self.assertEqual(len(s["cast_history"]),5)
        self.assertEqual(s["lost_spawn"],3)


if __name__=="__main__":
    unittest.main()
