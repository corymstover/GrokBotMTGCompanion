"""P0-023: nine *preregistered* physical-source Underworld Breach combo cases.

Each of the 99 candidate cards resides in exactly one zone. All opponent
outcomes are conditional, and requested opponent mill != win/actual milling.
"""
from __future__ import annotations
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest
from scripts.grixis_m7_decision_gate import parse_list

ROOT = Path(__file__).resolve().parents[1]
PLAN = json.loads((ROOT/"data/grixis/m6/phase_b_plans/abaddon_p0_breach_led_freeze_20261022.json").read_text())
BREACH="Underworld Breach"
LED="Lion's Eye Diamond"
FREEZE="Brain Freeze"
FODDER=("Ancestral Vision","Brainstorm","Cabal Ritual","Dark Ritual",
        "Demonic Tutor","Flame Rift","Gamble","Jeska's Will",
        "Ponder","Rite of Flame","Swan Song","Vampiric Tutor")
INITIAL_HAND=("Arcane Signet","Flusterstorm")
ZONES=("library","hand","battlefield","graveyard","exile","stack")


def card_counter(state):
    return sum((Counter(state[n]) for n in ZONES),Counter())


def relocate(state,name,src,dst):
    if name not in state[src]:
        raise AssertionError("Physical card missing: "+name+" from "+src)
    state[src].remove(name)
    state[dst].append(name)


def conserved(state):
    if card_counter(state)!=state["original"]:
        raise AssertionError("Physical 99-card multiset drift: "+str(card_counter(state)-state["original"]))
    if state["stack"]:
        raise AssertionError("Unresolved original spell left on stack")


def setup():
    path=ROOT/PLAN["candidate_source"]
    if hashlib.sha256(path.read_bytes()).hexdigest()!=PLAN["candidate_sha256"]:
        raise AssertionError("Proposed whole-list physical SHA drift")
    cards,cmd,companions=parse_list(path)
    if len(cards)!=100 or len(set(cards))!=94 or cmd!=["Abaddon the Despoiler"] or companions:
        raise AssertionError("Wrong source list/commander/card count")
    library=cards[1:]
    state={name:[] for name in ZONES}
    state["library"]=list(library)
    state.update({"original":Counter(library),"tapped_lands":[],
                  "mana":{"U":0,"R":0}, "cast_history":[], "spell_copies":0,
                  "resolved_self_mill":0,"requested_opponent_mill":0,
                  "escape_fodder_exiled":[], "storm_copy_batches":[],
                  "virtual_lost_tokens":0, "breach_paid_source":None,
                  "activated_led_count":0,"ledger":[]})
    # Cast breach THIS turn; it must be sacrificed at beginning of this turn's
    # end step, so a prior-turn Breach setup would be false without replacement.
    relocate(state,"Mountain","library","battlefield")
    relocate(state,"Island","library","battlefield")
    state["tapped_lands"]=["Mountain","Island"]
    relocate(state,BREACH,"library","hand")
    relocate(state,BREACH,"hand","stack")
    state["cast_history"].append((BREACH,"hand",2))
    state["breach_paid_source"]=("{R} from Mountain","{1} from Island")
    relocate(state,BREACH,"stack","battlefield")
    relocate(state,LED,"library","graveyard")
    relocate(state,FREEZE,"library","graveyard")
    for name in FODDER: relocate(state,name,"library","graveyard")
    for name in INITIAL_HAND: relocate(state,name,"library","hand")
    conserved(state)
    return state


def permission(state,*,rule_of_law=False,drannith=False):
    # Rule of Law sees Breach cast this same turn as the first spell.
    if BREACH not in state["battlefield"]:
        raise ValueError("No escape permission: Breach removed")
    if drannith:
        raise ValueError("Drannith prevents graveyard casting")
    if rule_of_law and state["cast_history"]:
        raise ValueError("Rule of Law forbids another spell this turn")


def escape_source(state,name,*,rule_of_law=False,drannith=False):
    """Pay Breach alternate cost from *current* own graveyard and eligible mana.

    Exiling three OTHER cards is a cost; NEVER exile the escaping card itself.
    This policy protects the other combo card as necessary for continuation.
    """
    if name not in (LED,FREEZE):
        raise ValueError("unsupported escape target")
    permission(state,rule_of_law=rule_of_law,drannith=drannith)
    if name not in state["graveyard"]:
        raise ValueError("not in graveyard")
    if name==FREEZE and state["mana"]["U"]<2:
        raise ValueError("Cannot pay Brain Freeze {1}{U} with present mana")
    choices=[x for x in state["graveyard"] if x not in (LED,FREEZE)]
    if len(choices)<3:
        raise ValueError("Cannot pay escape's three other graveyard cards")
    fodder=choices[:3]
    for x in fodder:
        relocate(state,x,"graveyard","exile")
    state["escape_fodder_exiled"].extend(fodder)
    if name==FREEZE: state["mana"]["U"]-=2
    storm_prior=len(state["cast_history"]) if name==FREEZE else None
    relocate(state,name,"graveyard","stack")
    state["cast_history"].append((name,"escaped_graveyard",0 if name==LED else 2))
    state["ledger"].append(("cast_escape",name,tuple(fodder),storm_prior))
    return storm_prior


def resolve_led(state,*,counter_led=False):
    if LED not in state["stack"]: raise AssertionError("No LED spell")
    relocate(state,LED,"stack","graveyard" if counter_led else "battlefield")
    conserved(state)


def activate_led(state,*,color="U"):
    if LED not in state["battlefield"]: raise ValueError("LED not on battlefield")
    if color not in ("U","R","B"): raise ValueError("unsupported demonstration mana")
    # Casting is finished. Only in eligible priority window can the LED
    # instant-timing mana ability be activated: no stack and no response to
    # the activation itself; discarding ALL cards and sacrifice are costs.
    hand=list(state["hand"])
    for card in hand: relocate(state,card,"hand","graveyard")
    relocate(state,LED,"battlefield","graveyard")
    state["mana"][color]+=3
    state["activated_led_count"]+=1
    state["ledger"].append(("led_mana_ability",color,tuple(hand),"no_stack"))
    conserved(state)
    return hand


def freeze_resolution(state,storm_prior,*,self_copies=1,counter_original=False):
    if FREEZE not in state["stack"]: raise AssertionError("No actual Freeze spell")
    if not isinstance(storm_prior,int) or not 0<=self_copies<=storm_prior:
        raise AssertionError("Invalid storm target distribution")
    # Copies are virtual stack objects and NOT additional casts. One self
    # copy gives 3 *actual named cards* from the 99 to the graveyard.
    state["storm_copy_batches"].append(storm_prior)
    state["spell_copies"]+=storm_prior
    for _ in range(self_copies*3):
        if not state["library"]:
            raise ValueError("Own library empty during self-targeted mill")
        card=state["library"].pop(0)
        state["graveyard"].append(card)
        state["resolved_self_mill"]+=1
    # Other copies (and uncoun tered original) request opponent to mill 3;
    # opponent library physically unspecified: no invented victory claim.
    opponent_instances=storm_prior-self_copies + (0 if counter_original else 1)
    state["requested_opponent_mill"]+=3*opponent_instances
    relocate(state,FREEZE,"stack","graveyard")
    state["ledger"].append(("storm_resolved",storm_prior,self_copies,
                            opponent_instances,counter_original))
    conserved(state)


def one_cycle(state,*,color="U",counter_original=False):
    escape_source(state,LED)
    resolve_led(state)
    activate_led(state,color=color)
    prior=escape_source(state,FREEZE)
    freeze_resolution(state,prior,self_copies=1,counter_original=counter_original)
    conserved(state)
    return prior


class AbaddonBreachLEDFreezeP0023(unittest.TestCase):
    def test_breach_two_cycles_source_paid(self):
        s=setup()
        self.assertEqual(s["breach_paid_source"],
                         ("{R} from Mountain","{1} from Island"))
        self.assertEqual(one_cycle(s),2)  # earlier Breach + LED
        self.assertEqual(one_cycle(s),4)  # Breach LED Freeze LED
        self.assertEqual(s["storm_copy_batches"],[2,4])
        self.assertEqual(len(s["cast_history"]),5)
        self.assertEqual(s["spell_copies"],6)
        self.assertEqual(s["resolved_self_mill"],6)
        self.assertEqual(s["requested_opponent_mill"],18)
        self.assertEqual(len(s["escape_fodder_exiled"]),12)
        self.assertEqual(s["mana"]["U"],2)
        self.assertIn(LED,s["graveyard"]); self.assertIn(FREEZE,s["graveyard"])
        self.assertIn(BREACH,s["battlefield"])
        conserved(s)

    def test_breach_exile_three_other_each_cast(self):
        s=setup()
        one_cycle(s);one_cycle(s)
        cost_receipts=[event for event in s["ledger"] if event[0]=="cast_escape"]
        self.assertEqual(len(cost_receipts),4)
        self.assertEqual([x[1] for x in cost_receipts],[LED,FREEZE,LED,FREEZE])
        self.assertTrue(all(len(x[2])==3 and x[1] not in x[2] for x in cost_receipts))
        self.assertEqual(len(s["exile"]),12)
        self.assertEqual(len(set(s["exile"])),12)
        self.assertEqual(Counter(s["escape_fodder_exiled"]),Counter(s["exile"]))
        conserved(s)

    def test_breach_insufficient_escape_fodder(self):
        s=setup()
        for name in FODDER[1:]:
            relocate(s,name,"graveyard","library")
        # Grave holds LED, Freeze and one fodder. Only two other cards:
        # cannot pay {0}+exile THREE other cards.
        with self.assertRaisesRegex(ValueError,"three other"):
            escape_source(s,LED)
        self.assertEqual(len(s["exile"]),0)
        self.assertIn(LED,s["graveyard"])
        conserved(s)

    def test_breach_led_discards_hand_on_activation(self):
        s=setup()
        self.assertEqual(tuple(s["hand"]),INITIAL_HAND)
        self.assertEqual(len(s["cast_history"]),1)  # Breach already cast/paid
        escape_source(s,LED);resolve_led(s)
        discarded=activate_led(s)
        self.assertEqual(tuple(discarded),INITIAL_HAND)
        self.assertEqual(s["hand"],[])
        self.assertEqual(s["activated_led_count"],1)
        self.assertEqual(s["mana"],{"U":3,"R":0})
        self.assertEqual(s["cast_history"][0],(BREACH,"hand",2))
        self.assertEqual(s["ledger"][-1][-1],"no_stack")
        conserved(s)

    def test_breach_no_blue_mana_cannot_cast_freeze(self):
        s=setup()
        escape_source(s,LED);resolve_led(s)
        activate_led(s,color="R")
        with self.assertRaisesRegex(ValueError,"Cannot pay Brain Freeze"):
            escape_source(s,FREEZE)
        self.assertEqual(s["mana"],{"U":0,"R":3})
        self.assertIn(FREEZE,s["graveyard"])
        conserved(s)

    def test_breach_rule_of_law_after_breach(self):
        s=setup()
        with self.assertRaisesRegex(ValueError,"Rule of Law"):
            escape_source(s,LED,rule_of_law=True)
        self.assertEqual(len(s["cast_history"]),1)
        self.assertEqual(len(s["exile"]),0)
        conserved(s)

    def test_breach_drannith_graveyard_cast_forbidden(self):
        s=setup()
        with self.assertRaisesRegex(ValueError,"Drannith"):
            escape_source(s,LED,drannith=True)
        self.assertEqual(len(s["cast_history"]),1)
        self.assertEqual(len(s["exile"]),0)
        conserved(s)

    def test_breach_removal_response_window(self):
        s=setup()
        escape_source(s,LED);resolve_led(s);activate_led(s)
        self.assertEqual(s["mana"]["U"],3)
        # Opponent has priority before next spell cast, and destroys Breach.
        relocate(s,BREACH,"battlefield","graveyard")
        with self.assertRaisesRegex(ValueError,"Breach removed"):
            escape_source(s,FREEZE)
        self.assertEqual(s["mana"]["U"],3)
        self.assertIn(FREEZE,s["graveyard"])
        conserved(s)

    def test_breach_countered_brain_freeze_storm_survives(self):
        s=setup()
        prior=one_cycle(s,counter_original=True)
        self.assertEqual(prior,2)
        self.assertEqual(s["resolved_self_mill"],3)
        # One of two copies also targets an opponent; original countered
        # AFTER trigger/copies created, so no original mill event.
        self.assertEqual(s["requested_opponent_mill"],3)
        self.assertEqual(s["spell_copies"],2)
        self.assertEqual(len(s["cast_history"]),3)
        self.assertIn(FREEZE,s["graveyard"])
        conserved(s)


if __name__=="__main__":
    unittest.main()
