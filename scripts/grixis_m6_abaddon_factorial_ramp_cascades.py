#!/usr/bin/env python3
"""Factorial physically shared Abaddon pilot: paid hand mana x other hand cascades.

The predecessor's THREE existing arms are called unchanged; only the fourth
combined arm actually runs both extensions on one mutable 99-card source.
All modes share identical seeded deck order and fixed casting policy.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from grixis_m6_abaddon_ignus_shared_effects import (
    ABADDON,assert_conserved,create_state,expected_physical,main_phase
)
from grixis_m6_abaddon_hand_acceleration_shared import (
    ACTIVATIONS,paid_accelerants_from_hand,start_turn,
    one_trial as hand_predecessor,verify as hand_verify
)
from grixis_m6_abaddon_other_hand_cascades import (
    one_trial as other_predecessor,verify as other_verify,
    snapshot as other_snapshot
)
from grixis_m6_abaddon_assault_access import play_land
from grixis_m6_fetch_city_tomb import FETCHES

ROOT=Path(__file__).resolve().parents[1]
PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_factorial_hand_ramp_cascades_20261022.json"


def verify():
    p=json.loads(PLAN.read_text(encoding="utf-8"))
    hp,old_h,cards_h,decks_h=hand_verify()
    op,old_o,cards_o,decks_o=other_verify()
    if old_h!=old_o or cards_h!=cards_o or decks_h!=decks_o:
        raise ValueError("Predecessor source 99/card graph mismatch")
    if (p["authority"]["approved_raw_sha256"]!=old_h["source"]["approved_raw_sha256"]
        or p["authority"]["physical_99_sha256"]!=old_h["source"]["physical_baseline_sha256"]):
        raise ValueError("Canonical source drift")
    e=p["experimental_design"]
    if (e["variants"]!=list(decks_h) or
        e["casting_orders"]!=old_h["policies"] or
        e["modes"]!=["neither","hand_ramp_only","core_other_cascade_only","both"] or
        e["checkpoint_own_turns"]!=old_h["sample"]["checkpoints"]):
        raise ValueError("Prerecorded four-arm physical pilot drift")
    if p["registered_hand_accelerants"]!=list(ACTIVATIONS):
        raise ValueError("Frozen hand mana spell order drift")
    if e["physical_trials"]!=e["paired_seeds_per_variant_order_mode"]*len(e["modes"])*len(e["variants"])*len(e["casting_orders"]):
        raise ValueError("Expected sample size inconsistent with registered four-arm design")
    return p,hp,op,old_h,cards_h,decks_h


def shared_metrics(state):
    """Only source-backed counters: cumulative events and per-seed booleans."""
    m=state["metrics"]
    return {
        "paid_initial_ignus_cast_seed":int(m["ignus_initial_paid_cast"]>0),
        "actual_ignus_cascade_seed":int(m["actual_paid_ignus_cascade"]>0),
        "actual_other_hand_cascade_seed":int(m["actual_other_hand_cascade"]>0),
        "actual_supported_effect_seed":int(m["actual_supported_hits_resolved"]>0),
        "actual_zero_mv_cascade_seed":int(m["zero_mv_hand_cascade_triggers"]>0),
        "hand_accelerant_cast_event_count":sum(m["hand_cast_"+x] for x in ACTIVATIONS),
        "hand_accelerant_cascade_events":m["hand_accelerant_cascade_triggers"],
        "zero_mv_cascade_events":m["zero_mv_hand_cascade_triggers"],
        "mana_vault_pilot_draw_damage":m["mana_vault_draw_damage"],
        "hand_red_mana_created":m["hand_red_mana"],
        "hand_black_mana_created":m["hand_black_mana"],
        "hand_colorless_mana_created":m["hand_colorless_mana"],
        "cascade_red_mana_created":m["hit_red_mana"],
        "cascade_black_mana_created":m["hit_black_mana"],
        "cascade_colorless_mana_created":m["hit_colorless_mana"],
        "cascade_cards_drawn":m["hit_cards_drawn"],
        "cascade_tutor_cards_to_hand_or_top":m["hit_tutored_hand"]+m["hit_tutored_top"],
        "cascade_opp_life_lost":m["hit_opponent_loss"],
        "cascade_ignus_events":m["actual_paid_ignus_cascade"],
        "cascade_other_hand_events":m["actual_other_hand_cascade"],
        "cascade_supported_effect_events":m["actual_supported_hits_resolved"],
    }


def shared_seeds(row,mode):
    """Only observably common per-SEED metrics from all three predecessors."""
    if mode=="neither" or mode=="core_other_cascade_only":
        return {
            "paid_initial_ignus_cast_seed":int(row["paid_initial_ignus_cast"]),
            "actual_ignus_cascade_seed":int(row["ignus_cascade_seed"]),
            "actual_other_hand_cascade_seed":int(row["other_hand_cascade_seed"]),
            "actual_supported_effect_seed":int(row["supported_hit_effect_seed"]),
            "actual_zero_mv_cascade_seed":0,
        }
    if mode=="hand_ramp_only":
        return {
            "paid_initial_ignus_cast_seed":int(row["paid_initial_ignus_cast"]),
            "actual_ignus_cascade_seed":int(row["actual_ignus_cascade_trigger"]),
            "actual_other_hand_cascade_seed":0,
            "actual_supported_effect_seed":int(row["actual_supported_effect_resolved"]),
            "actual_zero_mv_cascade_seed":0,
        }
    return {k:row[k] for k in ("paid_initial_ignus_cast_seed",
           "actual_ignus_cascade_seed","actual_other_hand_cascade_seed",
           "actual_supported_effect_seed","actual_zero_mv_cascade_seed")}


def one_trial(library,seed,policy,p,hp,op,old,cards,mode,*,checkpoints=None):
    cp=checkpoints or p["experimental_design"]["checkpoint_own_turns"]
    if mode=="neither":
        row,state=other_predecessor(library,seed,policy,op,old,cards,"original_ignus_only",checkpoints=cp)
        return {t:shared_seeds(x,mode) for t,x in row.items()},state
    if mode=="hand_ramp_only":
        row,state=hand_predecessor(library,seed,policy,hp,old,cards,"hand_acceleration",checkpoints=cp)
        return {t:shared_seeds(x,mode) for t,x in row.items()},state
    if mode=="core_other_cascade_only":
        row,state=other_predecessor(library,seed,policy,op,old,cards,
                "plus_other_qualified_hand_casts",checkpoints=cp)
        return {t:shared_seeds(x,mode) for t,x in row.items()},state
    if mode!="both":raise ValueError("Unregistered mode")
    state=create_state(library,seed)
    state["mana_vault_exhausted"]=False
    original=expected_physical(library)
    rows={}
    for turn in range(1,max(cp)+1):
        start_turn(state)
        if state["deck"]:
            state["hand"].append(state["deck"].pop(0))
        searches,land=play_land(state["hand"],state["deck"],state["lands"],seed,turn)
        if land in FETCHES:
            state["graveyard"].append(land)
        state["metrics"]["fetch_searches"]+=searches
        paid_accelerants_from_hand(state,hp,resolve_other_hand_cascades=True,
                cards=cards,prior=old,seed=seed,turn=turn)
        main_phase(state,cards,old,seed,turn,policy,other_hand_cascades=True)
        assert_conserved(state,original)
        if turn in cp:rows[str(turn)]=shared_metrics(state)
    return rows,state


def run(samples=None):
    p,hp,op,old,cards,decks=verify()
    e=p["experimental_design"]
    n=e["paired_seeds_per_variant_order_mode"] if samples is None else samples
    if n<1:raise ValueError("Sample count must be positive")
    result={}
    for mode in e["modes"]:
        result[mode]={}
        for policy in e["casting_orders"]:
            result[mode][policy]={}
            for variant,lib in decks.items():
                per_turn={str(t):Counter() for t in e["checkpoint_own_turns"]}
                examples=[]
                for i in range(n):
                    seed=e["seed"]+e["seed_step"]*i
                    receipts,state=one_trial(lib,seed,policy,p,hp,op,old,cards,mode)
                    for turn,data in receipts.items():
                        per_turn[turn].update(data)
                    if mode=="both" and len(examples)<3 and state["metrics"]["actual_other_hand_cascade"]:
                        examples.append({"seed":seed,"other_hand_cascade_events":state["metrics"]["actual_other_hand_cascade"],
                           "zero_mv_events":state["metrics"]["zero_mv_hand_cascade_triggers"],
                           "supported_hit_events":state["metrics"]["actual_supported_hits_resolved"],
                           "illustrative":state["examples"]})
                result[mode][policy][variant]={
                    "checkpoints":{t:dict(sorted(x.items())) for t,x in per_turn.items()},
                    "examples":examples}
    return {"schema_version":1,"preregistration":str(PLAN.relative_to(ROOT)),
            "canonical_approved_sha256":p["authority"]["approved_raw_sha256"],
            "samples_per_variant_policy_mode":n,
            "arms":result,"bounds":p["limits"],
            "comparison_constraint":"Per-seed indicators comparable across all modes; event counters only for both, never imputed for control modes."}


def main():
    a=argparse.ArgumentParser();a.add_argument("--samples",type=int);a.add_argument("--out")
    z=a.parse_args();r=run(z.samples)
    if z.out:
        Path(z.out).write_text(json.dumps(r,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    for mode,policies in r["arms"].items():
        for policy,variants in policies.items():
            for variant,d in variants.items():
                print(mode,policy,variant,"T10",json.dumps(d["checkpoints"]["10"],sort_keys=True))
    print("FOUR-ARM PHYSICAL STUDY, NOT 99-CARD GAME ENGINE OR WIN RATE.")

if __name__=="__main__":main()
