#!/usr/bin/env python3
"""A/B Abaddon physical hand-cascade extension, exact prior no-other control.

All restricted main-phase hand casts are actually paid. The physical library,
hand, battlefield, mana pool and graveyard are shared with Ignus's real
cascades. Printed MV, not reduced paid mana, controls lower-cost exiling.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from grixis_m6_abaddon_ignus_shared_effects import (
    ABADDON,ZERO,assert_conserved,create_state,effect_add,expected_physical,
    main_phase,one_trial as predecessor_one_trial,verify as predecessor_verify
)
from grixis_m6_abaddon_assault_access import play_land
from grixis_m6_fetch_city_tomb import FETCHES
from grixis_m6_abaddon_ignus_paid_chronology import MV_AND_COLORS

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_other_hand_cascades_20261022.json"


def verify():
    p=json.loads(PLAN.read_text(encoding="utf-8"))
    old,cards,decks=predecessor_verify()
    if p["authority"]["canonical_approved_sha256"]!=old["source"]["approved_raw_sha256"]:
        raise ValueError("Canonical frozen authority drift")
    if p["authority"]["frozen_physical_source_sha256"]!=old["source"]["physical_baseline_sha256"]:
        raise ValueError("Frozen 99 source drift")
    if p["physical_variants"]!=list(decks):
        raise ValueError("Five physical decks changed")
    if p["policies"]!=old["policies"]:
        raise ValueError("Predecessor pilot orders changed")
    if p["modes"]!=["original_ignus_only","plus_other_qualified_hand_casts"]:
        raise ValueError("Registered A/B modes changed")
    for name,mv in p["scope"]["register_printed_mvs"].items():
        if name not in MV_AND_COLORS or MV_AND_COLORS[name][0]!=mv:
            raise ValueError("Other hand source MV drift: "+name)
        if cards[name]["mv"]!=mv:
            raise ValueError("Graph physical card printed MV drift: "+name)
    return p,old,cards,decks


def snapshot(state):
    m=state["metrics"]
    return {
        "paid_initial_ignus_cast":int(m["ignus_initial_paid_cast"]>0),
        "ignus_cascade_seed":int(m["actual_paid_ignus_cascade"]>0),
        "other_hand_cascade_seed":int(m["actual_other_hand_cascade"]>0),
        "supported_hit_effect_seed":int(m["actual_supported_hits_resolved"]>0),
        "other_hand_cascade_triggers":m["actual_other_hand_cascade"],
        "other_hand_cascade_resolved":m["other_hand_cascade_triggers_resolved"],
        "ignus_cascade_triggers":m["actual_paid_ignus_cascade"],
        "supported_effects_resolved":m["actual_supported_hits_resolved"],
        "mana_from_cascade":sum(m[k] for k in ("hit_red_mana","hit_black_mana","hit_colorless_mana")),
        "cards_drawn_from_cascade":m["hit_cards_drawn"],
        "tutored_cards_to_hand_or_top":m["hit_tutored_hand"]+m["hit_tutored_top"],
        "opponent_loss_from_cascade":m["hit_opponent_loss"],
        "unsupported_hit_declines":m["unsupported_or_illegal_hit_declined"],
        "old_omitted_other_hand_triggers":m["other_hand_cascade_triggers_OMITTED"],
    }


def one_trial(library,seed,policy,p,old,cards,mode,*,checkpoints=None):
    cp=checkpoints or p["checkpoints"]
    if mode=="original_ignus_only":
        base,field=predecessor_one_trial(library,seed,policy,old,cards,checkpoints=cp)
        # The exact predecessor exposed correct checkpoint counters but not
        # separately named other-hand seed counters; reconstruct only known
        # zero or inherited fields. Never infer prior commander presence.
        snapshots={}
        for t,rec in base.items():
            snapshots[t]={
                "paid_initial_ignus_cast":int(rec["paid_initial_ignus_cast"]),
                "ignus_cascade_seed":int(rec["actual_ignus_cascade_trigger"]),
                "other_hand_cascade_seed":0,
                "supported_hit_effect_seed":int(rec["actual_supported_effect_resolved"]),
                "other_hand_cascade_triggers":0,
                "other_hand_cascade_resolved":0,
                # Original predecessor does not export Ignus event counts
                # at each checkpoint: seed-level only is available.
                "ignus_cascade_triggers":int(rec["actual_ignus_cascade_trigger"]),
                "supported_effects_resolved":int(rec["actual_supported_effect_resolved"]),
                "mana_from_cascade":rec["mana_from_cascade_hit"],
                "cards_drawn_from_cascade":rec["cards_actually_drawn_by_hit"],
                "tutored_cards_to_hand_or_top":rec["cards_physically_tutored_by_hit"],
                "opponent_loss_from_cascade":rec["opponent_loss_from_cascade_hit"],
                "unsupported_hit_declines":rec["unsupported_declined"],
                "old_omitted_other_hand_triggers":rec["ignored_other_hand_cascade"],
            }
        assert_conserved(field,expected_physical(library))
        return snapshots,field
    if mode!="plus_other_qualified_hand_casts":
        raise ValueError("Unregistered A/B policy")
    state=create_state(library,seed)
    original=expected_physical(library)
    output={}
    for turn in range(1,max(cp)+1):
        state["lands"]=[(name,False) for name,_ in state["lands"]]
        state["pool"]=ZERO
        state["loss"]=0
        state["rocks_tapped"]=False
        if "Sol Ring" in state["field"]:
            state["pool"]=effect_add(state["pool"],c=2)
            state["rocks_tapped"]=True
            state["metrics"]["existing_sol_ring_retap_mana"]+=2
        if state["deck"]:
            state["hand"].append(state["deck"].pop(0))
        searched,land=play_land(state["hand"],state["deck"],state["lands"],seed,turn)
        if land in FETCHES:
            state["graveyard"].append(land)
        state["metrics"]["fetch_searches"]+=searched
        main_phase(state,cards,old,seed,turn,policy,other_hand_cascades=True)
        assert_conserved(state,original)
        if turn in cp:
            output[str(turn)]=snapshot(state)
    return output,state


def run(samples=None):
    p,old,cards,decks=verify()
    n=p["paired_seeds_per_variant_policy_mode"] if samples is None else samples
    if n<1:raise ValueError("Invalid seed count")
    result={}
    for mode in p["modes"]:
        result[mode]={}
        for policy in p["policies"]:
            result[mode][policy]={}
            for variant,library in decks.items():
                sums={str(t):Counter() for t in p["checkpoints"]}
                examples=[]
                for i in range(n):
                    seed=p["seed"]+104729*i
                    rows,state=one_trial(library,seed,policy,p,old,cards,mode)
                    for t,row in rows.items():
                        sums[t].update(row)
                    if mode=="plus_other_qualified_hand_casts" and state["metrics"]["actual_other_hand_cascade"]>0 and len(examples)<3:
                        examples.append({"seed":seed,"physical_other_hand_cascades":state["metrics"]["actual_other_hand_cascade"],
                                         "actual_supported_hit_effects":state["metrics"]["actual_supported_hits_resolved"],
                                         "traces":state["examples"]})
                result[mode][policy][variant]={"checkpoints":{k:dict(sorted(v.items())) for k,v in sums.items()},"examples":examples}
    return {"schema_version":1,
            "preregistration":str(PLAN.relative_to(ROOT)),
            "canonical_sha256":p["authority"]["canonical_approved_sha256"],
            "samples_per_variant_policy_mode":n,
            "result":result,"bounds":p["bounds"]}


def main():
    a=argparse.ArgumentParser()
    a.add_argument("--samples",type=int)
    a.add_argument("--out")
    q=a.parse_args()
    receipt=run(q.samples)
    if q.out:
        Path(q.out).write_text(json.dumps(receipt,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    for mode,policies in receipt["result"].items():
        for policy,variants in policies.items():
            for variant,rec in variants.items():
                print(mode,policy,variant,"T10",json.dumps(rec["checkpoints"]["10"],sort_keys=True))
    print("Bounded paid other-hand cascades; no full 99-card game, counterplay or wins.")

if __name__=="__main__":
    main()
