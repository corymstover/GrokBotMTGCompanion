#!/usr/bin/env python3
"""Eight source-verified priority/casting-restriction windows for Abaddon Ignus.

A pre-arranged, physically conserved 99-card opponent-counterfactual fixture,
not observed access probability. External hate cards belong to opponents.
Grinning Ignus's {R} return ability IS a mana ability, not stack-responsive.
"""
from __future__ import annotations
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from grixis_m6_abaddon_ignus_shared_effects import (
 ABADDON,BIRGI,IGNUS,ZERO,assert_conserved,create_state,effect_add,
 expected_physical,first_cascade,recast_ignus,source_cast,verify
)

ROOT=Path(__file__).resolve().parents[1]
PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_ignus_stack_windows_20261022.json"
LOYAL="Loyal Subordinate"
BURN="Boltwave"
FIRST_HIT="Sol Ring"
SEED=621017


def verify_study():
    p=json.loads(PLAN.read_text(encoding="utf-8"))
    prior,cards,decks=verify()
    a=p["baseline"]
    if a["canonical_raw_sha256"]!=prior["source"]["approved_raw_sha256"]:
        raise ValueError("Canonical approved SHA drift")
    if a["source_99_sha256"]!=prior["source"]["physical_baseline_sha256"]:
        raise ValueError("Physical 99 source drift")
    if a["variant"]!="ignus_for_rakdos":
        raise ValueError("Wrong physical challenger source")
    if len(decks[a["variant"]])!=99 or IGNUS not in decks[a["variant"]]:
        raise ValueError("Not a true hypothetical 100-card physical deck")
    ids={x["id"] for x in p["registered_states"]}
    expected={"uncontested","rule_of_law_boltwave_was_cast",
              "rule_of_law_first_ignus","drannith",
              "abaddon_removed_before_next_ignus",
              "birgi_removed_before_next_ignus",
              "ignus_countered_after_cast","ignus_entered_quiet_board"}
    if ids!=expected:raise ValueError("Counterfactual list drift")
    return p,prior,cards,decks[a["variant"]]


def relocate(state,name,target):
    """Move exactly one physical approved candidate card; never invent it."""
    if name in state["hand"]:
        state["hand"].remove(name)
    elif name in state["deck"]:
        state["deck"].remove(name)
    else:
        raise AssertionError("A physical card is absent or duplicated: "+name)
    if target=="hand":state["hand"].append(name)
    elif target=="field":state["field"].add(name)
    elif target=="graveyard":state["graveyard"].append(name)
    elif target=="top":state["deck"].insert(0,name)
    elif target=="land":state["lands"].append((name,True))
    else:raise ValueError("Invalid physical zone")
    

def fixture(library,*,ignus_field=False,life_source="loyal",
            birgi=True,abaddon=True):
    """Stage a *conditional* legal Grixis battlefield, not random full games.

    Loyal's combat-beginning trigger with Abaddon controlled has already dealt
    three to each of three opponents before our postcombat main. Alternatively
    the source-paid Boltwave is already resolved in grave this turn.
    """
    state=create_state(library,SEED)
    state["metrics"]["prearranged_not_observed"]=1
    relocate(state,BIRGI,"field" if birgi else "graveyard")
    relocate(state,IGNUS,"field" if ignus_field else "hand")
    if abaddon:state["field"].add(ABADDON)
    if life_source=="loyal":
        relocate(state,LOYAL,"field")
    elif life_source=="boltwave":
        relocate(state,BURN,"graveyard")
    else:raise ValueError("No grounded life-loss source")
    # Sole deterministic first cascade target, from the genuine 99-card list.
    relocate(state,FIRST_HIT,"top")
    if ignus_field:
        relocate(state,"Mountain","land")
        state["pool"]=(0,0,1,0)
    else:
        for basic in ("Island","Swamp","Mountain"):
            relocate(state,basic,"land")
        state["pool"]=(1,1,1,0)
    state["loss"]=9
    assert_conserved(state,expected_physical(library))
    return state


def legal_hand_ignus_and_first_cascade(state,cards,prior,*,rule_of_law=False,
                                       drannith=False,already_cast_this_turn=False,
                                       counter_original=False):
    """One SOURCE-PAID Ignus cast on a controlled battlefield and stack window."""
    if rule_of_law and already_cast_this_turn:
        return {"initial_hand_cast":False,"trigger":False,"cascade_free_cast":False,
                "reason":"Rule of Law blocks original second spell","additional_recasts":0}
    cost=source_cast(state["lands"],state["pool"],IGNUS,
                     familiar_controlled=False,rakdos_controlled=False,
                     opponent_loss=state["loss"])
    if cost is None:raise AssertionError("Conditional source-paid hand Ignus cannot be cast")
    state["pool"]=cost
    state["hand"].remove(IGNUS)
    state["metrics"]["hand_ignus_paid"]+=1
    birgi_trigger=BIRGI in state["field"]
    if birgi_trigger:
        # Spell-cast triggered ability resolves; this is NOT the Ignus mana
        # ability (which has a different no-stack rule).
        state["pool"]=effect_add(state["pool"],r=1)
        state["metrics"]["birgi_red_on_cast"]+=1
    cascade=ABADDON in state["field"] and state["loss"]>=3
    if counter_original:
        # Opponent counters creature SPELL, not Ignus's no-stack mana ability.
        # Existing cast triggers stay on stack and resolve independently.
        state["graveyard"].append(IGNUS)
    receipt=(first_cascade(state,cards,19,prior,
             rule_of_law=rule_of_law,drannith=drannith) if cascade else None)
    if not counter_original:
        state["field"].add(IGNUS)
    return {"initial_hand_cast":True,"trigger":cascade,
            "cascade_free_cast":bool(receipt and receipt["cast_from_exile"]),
            "first_hit":receipt["hit"] if receipt else None,
            "counter_original":counter_original,
            "original_ignus_in_graveyard":IGNUS in state["graveyard"],
            "original_ignus_on_battlefield":IGNUS in state["field"],
            "birgi_cast_red_trigger":birgi_trigger,
            "additional_recasts":0,"reason":"original countered" if counter_original else
                     "legal cast, triggered abilities and priority recorded"}


def one_window(name,p,prior,cards,library):
    if name=="rule_of_law_boltwave_was_cast":
        state=fixture(library,life_source="boltwave")
        original=tuple(state["pool"])
        result=legal_hand_ignus_and_first_cascade(
           state,cards,prior,rule_of_law=True,already_cast_this_turn=True)
        if state["pool"]!=original:raise AssertionError("No forbidden mana should be spent")
    elif name=="rule_of_law_first_ignus":
        state=fixture(library)
        result=legal_hand_ignus_and_first_cascade(
            state,cards,prior,rule_of_law=True)
        result["additional_recasts"]=recast_ignus(
            state,cards,prior,22,7,rule_of_law=True)
    elif name=="drannith":
        state=fixture(library)
        result=legal_hand_ignus_and_first_cascade(
            state,cards,prior,drannith=True)
        result["additional_recasts"]=recast_ignus(
            state,cards,prior,22,7,drannith=True)
    elif name=="ignus_countered_after_cast":
        state=fixture(library)
        result=legal_hand_ignus_and_first_cascade(
            state,cards,prior,counter_original=True)
        result["additional_recasts"]=recast_ignus(
            state,cards,prior,22,7)  # no creature to bounce
    elif name in ("uncontested","ignus_entered_quiet_board",
                  "abaddon_removed_before_next_ignus",
                  "birgi_removed_before_next_ignus"):
        state=fixture(library,ignus_field=True,
            birgi=name!="birgi_removed_before_next_ignus",
            abaddon=name!="abaddon_removed_before_next_ignus")
        if name=="ignus_entered_quiet_board":
            # Ignus mana ability (source-paid) is immediately activatable
            # under active player's priority and *cannot be responded to*.
            result={"mana_ability_uses_stack":False,
                     "ordinary_removal_can_respond_to_activation":False,
                     "active_player_can_activate_before_opponent_priority":True}
        else:result={}
        before=state["metrics"]["actual_paid_ignus_cascade"]
        result["additional_recasts"]=recast_ignus(state,cards,prior,22,7)
        result["additional_ignus_cascades"]=(
            state["metrics"]["actual_paid_ignus_cascade"]-before)
    else:raise ValueError("Nonregistered disruption: "+name)
    assert_conserved(state,expected_physical(library))
    result.update({"fixture_from_frozen_physical_99":True,
        "prearranged_board_not_observed_access":True,
        "physical_zone_conservation":True,
        "final_ignus_zone":"battlefield" if IGNUS in state["field"] else
                  "graveyard" if IGNUS in state["graveyard"] else
                  "hand" if IGNUS in state["hand"] else "other",
        "cumulative_actual_supported_hit_effects":
            state["metrics"]["actual_supported_hits_resolved"],
        "actual_exiled_cascade_triggers":
            state["metrics"]["actual_paid_ignus_cascade"]})
    return result


def run():
    p,prior,cards,library=verify_study()
    outputs={entry["id"]:one_window(entry["id"],p,prior,cards,library)
             for entry in p["registered_states"]}
    return {"schema_version":1,"stage":"CONDITIONAL_PHYSICAL_RESPONSE_WINDOWS_NO_OPPONENT_FREQUENCY",
       "canonical_sha256":p["baseline"]["canonical_raw_sha256"],
       "study_plan":str(PLAN.relative_to(ROOT)),"cases":outputs,
       "bounds":p["model_scope"]}


def main():
    import argparse
    a=argparse.ArgumentParser();a.add_argument("--out")
    args=a.parse_args();report=run()
    if args.out:Path(args.out).write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    for k,v in report["cases"].items():
        print(k,json.dumps(v,sort_keys=True))
    print("Conditional eight physical stack windows; not sampled meta or deck win rate.")


if __name__=="__main__":main()
