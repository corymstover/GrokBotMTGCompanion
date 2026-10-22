#!/usr/bin/env python3
"""Source-paid six-card HAND acceleration extension of PR524's physical Ignus model.

Mode OFF delegates to original PR524 one_trial without changes. Mode ON casts
six actual physical singleton hand-held mana accelerants before fixed core
sequence. Neither model is a complete Grixis game or a deck win-rate estimate.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from grixis_m6_abaddon_ignus_shared_effects import (
    ABADDON,BIRGI,IGNUS,FAMILIAR,RAKDOS,ZERO,
    assert_conserved,create_state,effect_add,expected_physical,main_phase,
    one_trial as predecessor_one_trial,verify as predecessor_verify
)
from grixis_m6_abaddon_assault_access import play_land
from grixis_m6_fetch_city_tomb import FETCHES
from grixis_m6_abaddon_chronological_engine import pay_and_tap

ROOT=Path(__file__).resolve().parents[1]
PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_hand_acceleration_shared_20261022.json"
ACTIVATIONS=("Lotus Petal","Sol Ring","Mana Vault",
             "Dark Ritual","Cabal Ritual","Rite of Flame")
HAND_RITUALS={"Dark Ritual","Cabal Ritual","Rite of Flame"}


def verify():
    p=json.loads(PLAN.read_text(encoding="utf-8"))
    prior,cards,decks=predecessor_verify()
    a=p["authority"]
    if (a["canonical_approved_sha256"]!=prior["source"]["approved_raw_sha256"] or
        a["frozen_99_card_source_sha256"]!=prior["source"]["physical_baseline_sha256"]):
        raise ValueError("Canonical or baseline snapshot changed")
    if (p["experiment"]["variants"]!=list(decks) or
        p["experiment"]["policies"]!=prior["policies"] or
        p["experiment"]["pre_main_fixed_acceleration_order"]!=list(ACTIVATIONS)):
        raise ValueError("Predeclared variants/cast policy drift")
    if set(p["verified_hand_accelerants"])!=set(ACTIVATIONS):
        raise ValueError("Hand accelerant card subset drift")
    if p["experiment"]["control_modes"]!=["no_hand_acceleration","hand_acceleration"]:
        raise ValueError("Control policy drift")
    expected={"Lotus Petal":(0,(0,0,0)),"Sol Ring":(1,(0,0,0)),
       "Mana Vault":(1,(0,0,0)),"Dark Ritual":(1,(0,1,0)),
       "Cabal Ritual":(2,(0,1,0)),"Rite of Flame":(1,(0,0,1))}
    for name,cost in expected.items():
        item=p["verified_hand_accelerants"][name]
        if (item["cost"][0],tuple(item["cost"][1]))!=cost:
            raise ValueError("Frozen exact Oracle cost drift: "+name)
        if cards[name]["mv"]!=cost[0]:
            raise ValueError("Printed MV graph mismatch: "+name)
    return p,prior,cards,decks


def paid_accelerants_from_hand(state,plan):
    """One registered pre-main source-paid pass; new rocks tap/sac once.

    Cards are not cast if source payment fails; no phantom hand-to-board move.
    Nightscape cannot discount any generic portion of a mono-B/mono-R ritual.
    """
    for name in ACTIVATIONS:
        if name not in state["hand"]: continue
        if name in ("Sol Ring","Mana Vault") and name in state["field"]:
            raise AssertionError("A singleton artifact is simultaneously held and controlled")
        unit=plan["verified_hand_accelerants"][name]["cost"]
        printed=(unit[0],tuple(unit[1]))
        paid=pay_and_tap(state["lands"],state["pool"],name,
                         source_cost_override=printed)
        if paid is None:continue
        state["pool"]=paid
        state["hand"].remove(name)
        state["metrics"]["hand_cast_"+name]+=1
        if BIRGI in state["field"]:
            state["pool"]=effect_add(state["pool"],r=1)
            state["metrics"]["birgi_red_from_hand_accelerant"]+=1
        if name=="Lotus Petal":
            # Zero-mana permanent, immediate tap and sacrifice for fixed R.
            state["graveyard"].append(name)
            state["pool"]=effect_add(state["pool"],r=1)
            state["metrics"]["hand_red_mana"]+=1
        elif name=="Sol Ring":
            state["field"].add(name)
            state["rocks_tapped"]=True
            state["pool"]=effect_add(state["pool"],c=2)
            state["metrics"]["hand_colorless_mana"]+=2
        elif name=="Mana Vault":
            state["field"].add(name)
            state["mana_vault_exhausted"]=True
            state["pool"]=effect_add(state["pool"],c=3)
            state["metrics"]["hand_colorless_mana"]+=3
        elif name=="Dark Ritual":
            state["pool"]=effect_add(state["pool"],b=3)
            state["metrics"]["hand_black_mana"]+=3
            state["graveyard"].append(name)
        elif name=="Cabal Ritual":
            threshold=len(state["graveyard"])>=7
            produced=5 if threshold else 3
            state["pool"]=effect_add(state["pool"],b=produced)
            state["metrics"]["hand_black_mana"]+=produced
            state["metrics"]["cabal_threshold_paid"]+=int(threshold)
            state["graveyard"].append(name)
        elif name=="Rite of Flame":
            # Original card is still on the stack for this computation.
            produced=2+state["graveyard"].count("Rite of Flame")
            state["pool"]=effect_add(state["pool"],r=produced)
            state["metrics"]["hand_red_mana"]+=produced
            state["graveyard"].append(name)
    # Sources just produced reside in the actual shared U/B/R/C pool.


def metrics_snapshot(state):
    m=state["metrics"]
    return {
        "paid_initial_ignus_cast":int(m["ignus_initial_paid_cast"]>0),
        "actual_ignus_cascade_trigger":int(m["actual_paid_ignus_cascade"]>0),
        "actual_supported_effect_resolved":int(m["actual_supported_hits_resolved"]>0),
        "five_cascade_recasts":int(m["one_turn_5_recast_cascade_line"]>0),
        "paid_commander_access":int(ABADDON in state["field"]),
        "hand_accelerants_cast":sum(m["hand_cast_"+x] for x in ACTIVATIONS),
        "hand_black_mana":m["hand_black_mana"],
        "hand_red_mana":m["hand_red_mana"],
        "hand_colorless_mana":m["hand_colorless_mana"],
        "hand_mana_vault_damage":m["mana_vault_draw_damage"],
        "hand_cabal_threshold_casts":m["cabal_threshold_paid"],
        "unsupported_or_illegal_hits_declined":m["unsupported_or_illegal_hit_declined"],
        "other_hand_cascades_omitted":m["other_hand_cascade_triggers_OMITTED"],
        **{"hand_cast_"+x:m["hand_cast_"+x] for x in ACTIVATIONS},
    }


def one_trial(library,seed,policy,plan,prior,cards,mode,*,checkpoints=None):
    cp=checkpoints or plan["experiment"]["checkpoint_own_turns"]
    if mode=="no_hand_acceleration":
        # Pure compatibility control: the exact predecessor implementation.
        old,field=predecessor_one_trial(library,seed,policy,prior,cards,
                                        checkpoints=cp)
        samples={}
        for t in cp:
            prev=old[str(t)]
            samples[str(t)]={
                "paid_initial_ignus_cast":int(prev["paid_initial_ignus_cast"]),
                "actual_ignus_cascade_trigger":int(prev["actual_ignus_cascade_trigger"]),
                "actual_supported_effect_resolved":int(prev["actual_supported_effect_resolved"]),
                "five_cascade_recasts":int(prev["five_cascade_recasts"]),
                "paid_commander_access":int(ABADDON in field["field"]),
                "hand_accelerants_cast":0,"hand_black_mana":0,
                "hand_red_mana":0,"hand_colorless_mana":0,
                "hand_mana_vault_damage":0,"hand_cabal_threshold_casts":0,
                "unsupported_or_illegal_hits_declined":prev["unsupported_declined"],
                "other_hand_cascades_omitted":prev["ignored_other_hand_cascade"],
                **{"hand_cast_"+x:0 for x in ACTIVATIONS}
            }
        assert_conserved(field,expected_physical(library))
        return samples,field
    if mode!="hand_acceleration":
        raise ValueError("Unknown mode")
    if len(library)!=99:raise ValueError("Only physical 99 source")
    state=create_state(library,seed)
    original=expected_physical(library)
    snapshots={}
    state["mana_vault_exhausted"]=False
    for turn in range(1,max(cp)+1):
        state["lands"]=[(n,False) for n,_ in state["lands"]]
        state["pool"]=ZERO
        state["loss"]=0
        state["rocks_tapped"]=False
        if "Sol Ring" in state["field"]:
            state["pool"]=effect_add(state["pool"],c=2)
            state["rocks_tapped"]=True
            state["metrics"]["existing_sol_ring_retap_mana"]+=2
        # Mana Vault normally does NOT untap. Its {4} optional paid-upkeep
        # untap is intentionally excluded, and so is its reuse.
        if state["mana_vault_exhausted"]:
            if "Mana Vault" not in state["field"]:
                raise AssertionError("Mana Vault tap flag has no physical card")
            state["pilot_life_damage"]+=1 # beginning of draw step
            state["metrics"]["mana_vault_draw_damage"]+=1
        if state["deck"]:
            state["hand"].append(state["deck"].pop(0))
        searched,land=play_land(state["hand"],state["deck"],
                               state["lands"],seed,turn)
        if land in FETCHES:
            state["graveyard"].append(land)
        state["metrics"]["fetch_searches"]+=searched
        paid_accelerants_from_hand(state,plan)
        main_phase(state,cards,prior,seed,turn,policy)
        assert_conserved(state,original)
        if turn in cp:
            snapshots[str(turn)]=metrics_snapshot(state)
    return snapshots,state


def run(samples=None):
    p,prior,cards,decks=verify()
    n=p["experiment"]["paired_seeds_per_variant_policy"] if samples is None else samples
    if n<1:raise ValueError("Sample count must be positive")
    observations={}
    for mode in p["experiment"]["control_modes"]:
        observations[mode]={}
        for policy in p["experiment"]["policies"]:
            observations[mode][policy]={}
            for variant,library in decks.items():
                agg={str(t):Counter() for t in p["experiment"]["checkpoint_own_turns"]}
                examples=[]
                for i in range(n):
                    seed=p["experiment"]["fixed_seed"]+104729*i
                    rows,state=one_trial(library,seed,policy,p,prior,cards,mode)
                    for t,v in rows.items():
                        for name,val in v.items():
                            agg[t][name]+=int(val)
                    if len(examples)<3 and state["metrics"]["actual_supported_hits_resolved"]>0:
                        examples.append({"seed":seed,
                          "supported_effect_resolutions":state["metrics"]["actual_supported_hits_resolved"],
                          "source_paid_hand_acceleration_casts":sum(state["metrics"]["hand_cast_"+x] for x in ACTIVATIONS)})
                observations[mode][policy][variant]={
                    "checkpoints":{t:dict(sorted(row.items())) for t,row in agg.items()},
                    "examples":examples}
    return {"schema_version":1,"stage":"PAIRED_SAME_PHYSICAL_LIBRARY_HAND_ACCELERANTS_VS_ORIGINAL_SOURCE_BOUNDED_IGNUS",
            "preregistration":str(PLAN.relative_to(ROOT)),
            "canonical_sha256":p["authority"]["canonical_approved_sha256"],
            "samples_per_variant_policy_mode":n,"results":observations,
            "bounds":p["limits"]}


def main():
    a=argparse.ArgumentParser()
    a.add_argument("--samples",type=int)
    a.add_argument("--out")
    z=a.parse_args()
    receipt=run(z.samples)
    if z.out:
        Path(z.out).write_text(json.dumps(receipt,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    for mode,policies in receipt["results"].items():
        for policy,variants in policies.items():
            for variant,obs in variants.items():
                print(mode,policy,variant,"T10",json.dumps(obs["checkpoints"]["10"],sort_keys=True))
    print("NO multiplayer win-rate, no opponent interaction, no approved deck modifications.")

if __name__=="__main__":main()
