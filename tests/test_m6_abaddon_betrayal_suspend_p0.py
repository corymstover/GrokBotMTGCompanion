"""P0-022: 7 registered physical Betrayal suspend/last-tick scenarios.

Uses the actual exact 100-card *alternative* source, with independent external
opponent library. No artificial card insertion into the 99 or win-rate claims.
"""
from __future__ import annotations
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest
from scripts.grixis_m7_decision_gate import parse_list

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/"data/grixis/m6/phase_b_plans/abaddon_p0_betrayal_suspend_20261022.json"
PLAN=json.loads(P.read_text())
BETRAYAL="Inevitable Betrayal"
LOST="The Lost and the Damned"
BASIC=("Island","Island","Swamp")
ZONES=("library","hand","field","exile","stack","graveyard")
OPPONENT=("Baleful Strix","Island","Swamp")


def counts(s):
    return sum((Counter(s[name]) for name in ZONES),Counter())


def move(s,card,a,b):
    if card not in s[a]:
        raise AssertionError("No physical card in source zone: "+card)
    s[a].remove(card)
    s[b].append(card)


def stage():
    path=ROOT/PLAN["variant"]
    if hashlib.sha256(path.read_bytes()).hexdigest()!=PLAN["variant_sha256"]:
        raise AssertionError("Canonical challenger SHA changed")
    cards,cmd,comp=parse_list(path)
    if len(cards)!=100 or len(set(cards))!=94 or cmd!=["Abaddon the Despoiler"] or comp:
        raise AssertionError("Not the registered genuine 100-card alternative")
    lib=cards[1:]
    if BETRAYAL not in lib:
        raise AssertionError("Cannot suspend cut card from preferred version")
    state={name:[] for name in ZONES}
    state["library"]=list(lib)
    state.update({"tapped":[],"time_counters":None,"upkeep_count":0,"cast_history":[],
                  "suspended":False,"total_spawn":0,"opp_library":list(OPPONENT),
                  "opp_gained":[],"resolution":None,"storm_count":0,"mana_pool_black":0,
                  "events":[]})
    move(state,BETRAYAL,"library","hand")
    move(state,LOST,"library","field")
    for name in BASIC:
        move(state,name,"library","field")
    assert counts(state)==Counter(lib)
    return state,Counter(lib)


def suspend(s,original,*,sorcery_window=True,already_cast_under_rule_of_law=False):
    """Tap source Island/Island/Swamp, pay 1UU as special action from hand."""
    if not sorcery_window or already_cast_under_rule_of_law:
        raise AssertionError("Prohibited suspend initiation timing")
    if s["tapped"] or Counter(s["field"])["Island"]<2 or "Swamp" not in s["field"]:
        raise AssertionError("Insufficient untapped U U and generic")
    if BETRAYAL not in s["hand"]:
        raise AssertionError("Inevitable Betrayal not physically in hand")
    s["tapped"].extend(BASIC) # two U and one B paying {1}; tapped NOW
    move(s,BETRAYAL,"hand","exile")
    s["time_counters"]=3
    s["suspended"]=True
    s["events"].append("special_action_suspend_from_hand_1UU_not_cast")
    assert not s["cast_history"] and s["storm_count"]==0 and s["total_spawn"]==0
    assert counts(s)==original


def upkeep(s,original,*,drannith=False,rule_of_law=False,
           earlier_spell_cast=False,decline_cast=False,counter_hit=False,
           choose_creature=True):
    """One upkeep: time counter trigger; last-counter optional free cast."""
    if BETRAYAL not in s["exile"] or not s["suspended"] or s["time_counters"]<=0:
        raise AssertionError("Not actually suspended")
    s["upkeep_count"]+=1
    s["time_counters"]-=1
    s["events"].append(("counter_removed",s["upkeep_count"],s["time_counters"]))
    if s["time_counters"]:
        assert counts(s)==original
        return "still_suspended"
    s["suspended"]=False  # zero counters => no future upkeep clock
    can_cast=not (drannith or (rule_of_law and earlier_spell_cast) or decline_cast)
    if not can_cast:
        s["resolution"]="stranded_exile_zero_counters"
        assert counts(s)==original
        return "stranded"
    # As suspend trigger resolves at upkeep, ignore sorcery-only timing;
    # spell is actually cast from exile for zero mana, MV 0, without
    # Abaddon-granted hand-only cascade.
    move(s,BETRAYAL,"exile","stack")
    s["cast_history"].append((BETRAYAL,0,"suspend_exile"))
    s["storm_count"]+=1
    s["total_spawn"]+=int(LOST in s["field"])
    s["events"].append("actual_nonhand_suspend_cast_no_abaddon_cascade")
    if counter_hit:
        move(s,BETRAYAL,"stack","graveyard")
        s["resolution"]="countered_after_cast"
    else:
        if choose_creature and "Baleful Strix" in s["opp_library"]:
            s["opp_library"].remove("Baleful Strix")
            s["opp_gained"].append("Baleful Strix")  # PUT, not cast
        move(s,BETRAYAL,"stack","graveyard")
        s["resolution"]="resolved_search_opponent_then_shuffle"
    assert counts(s)==original
    if Counter(s["opp_library"])+Counter(s["opp_gained"])!=Counter(OPPONENT):
        raise AssertionError("Opponent creature invented or omitted")
    return s["resolution"]


class AbaddonBetrayalSuspendP0022(unittest.TestCase):
    def test_suspend_paid_three_upkeeps(self):
        s,original=stage()
        suspend(s,original)
        self.assertEqual(Counter(s["tapped"]),Counter(BASIC))
        self.assertEqual(upkeep(s,original),"still_suspended")
        self.assertEqual(upkeep(s,original),"still_suspended")
        self.assertEqual(upkeep(s,original),"resolved_search_opponent_then_shuffle")
        self.assertEqual(s["time_counters"],0)
        self.assertEqual(s["cast_history"],[(BETRAYAL,0,"suspend_exile")])
        self.assertEqual(s["total_spawn"],1)
        self.assertEqual(s["opp_gained"],["Baleful Strix"])
        self.assertIn(BETRAYAL,s["graveyard"])
        self.assertEqual(s["storm_count"],1)

    def test_suspend_no_creature_fail_to_find(self):
        s,original=stage()
        suspend(s,original)
        upkeep(s,original);upkeep(s,original)
        upkeep(s,original,choose_creature=False)
        self.assertEqual(s["total_spawn"],1)
        self.assertEqual(s["opp_gained"],[])
        self.assertEqual(s["resolution"],"resolved_search_opponent_then_shuffle")

    def test_suspend_drannith_last_tick_stranded(self):
        s,original=stage()
        suspend(s,original)
        upkeep(s,original);upkeep(s,original)
        self.assertEqual(upkeep(s,original,drannith=True),"stranded")
        self.assertEqual(s["total_spawn"],0)
        self.assertIn(BETRAYAL,s["exile"])
        self.assertFalse(s["suspended"])
        self.assertEqual(s["time_counters"],0)
        with self.assertRaises(AssertionError):
            upkeep(s,original)

    def test_suspend_rule_of_law_prev_spell_blocks(self):
        s,original=stage()
        suspend(s,original)
        upkeep(s,original);upkeep(s,original)
        # One legal previous upkeep cast: a physically sourced Dark Ritual,
        # paid by a refreshed Swamp, black mana can be left floating.
        move(s,"Dark Ritual","library","graveyard")
        s["cast_history"].append(("Dark Ritual",1,"hand"))
        s["storm_count"]=1
        s["mana_pool_black"]=3
        self.assertEqual(upkeep(s,original,rule_of_law=True,earlier_spell_cast=True),"stranded")
        self.assertEqual(s["cast_history"],[("Dark Ritual",1,"hand")])
        self.assertEqual(s["total_spawn"],0)
        self.assertIn(BETRAYAL,s["exile"])

    def test_suspend_owner_declines_free_cast(self):
        s,original=stage()
        suspend(s,original)
        upkeep(s,original);upkeep(s,original)
        self.assertEqual(upkeep(s,original,decline_cast=True),"stranded")
        self.assertEqual(s["storm_count"],0)
        self.assertIn(BETRAYAL,s["exile"])

    def test_suspend_countered_after_cast(self):
        s,original=stage()
        suspend(s,original)
        upkeep(s,original);upkeep(s,original)
        self.assertEqual(upkeep(s,original,counter_hit=True),"countered_after_cast")
        self.assertEqual(s["storm_count"],1)
        self.assertEqual(s["total_spawn"],1)
        self.assertEqual(s["opp_gained"],[])
        self.assertIn(BETRAYAL,s["graveyard"])

    def test_suspend_not_hardcast_and_late_legal_first_spell(self):
        s,original=stage()
        self.assertIsNone(s["time_counters"])
        # Printed mana cost is absent, so a standard hand casting action has
        # no payable mana cost. Suspend special action is the legal substitute.
        self.assertEqual(PLAN["cost_budget"]["registered_case_count"],7)
        suspend(s,original)
        self.assertEqual(s["storm_count"],0)
        self.assertEqual(s["total_spawn"],0)
        upkeep(s,original);upkeep(s,original)
        self.assertEqual(upkeep(s,original,rule_of_law=True,earlier_spell_cast=False),
                         "resolved_search_opponent_then_shuffle")
        self.assertEqual(s["cast_history"],[(BETRAYAL,0,"suspend_exile")])
        self.assertEqual(s["storm_count"],1)
        self.assertEqual(s["total_spawn"],1)


if __name__=="__main__":
    unittest.main()
