#!/usr/bin/env python3
"""Physically JOIN paid Abaddon/Birgi/Ignus casts with bounded cascade effects.

Unlike separate #520 and #522 snapshots, the SAME deck, hand, land taps,
mana pool, graveyard and battlefield mutate after each real paid Ignus cast.
Only the preregistered source-confirmed subset of cascade spells resolves.
This is deliberately NOT a complete 99-card game or an opponent/win model.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
import random
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from grixis_m6_abaddon_ignus_paid_chronology import (
    ABADDON,BIRGI,IGNUS,FAMILIAR,RAKDOS,ASSAULT,BURNS,ZERO,
    MV_AND_COLORS,source_cast,variants,
)
from grixis_m6_abaddon_ignus_cascade_first_hit import (
    inventory,legality_of_hit,is_land,
)
from grixis_m6_abaddon_assault_access import play_land,LANDS_KNOWN
from grixis_m6_fetch_city_tomb import FETCHES
from grixis_m6_abaddon_chronological_engine import pay_and_tap

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_ignus_shared_effects_20261022.json"
INSTANT_SORCERY={
    "Dark Ritual","Rite of Flame","Boltwave","Flame Rift",
    "Ancestral Vision","Profane Tutor","Demonic Tutor","Vampiric Tutor",
    "Imperial Seal","Gamble"
}
SUPPORTED=INSTANT_SORCERY|{"Sol Ring","Lotus Petal"}
TOP_TUTORS={"Vampiric Tutor","Imperial Seal"}
HAND_TUTORS={"Profane Tutor","Demonic Tutor","Gamble"}


def verify():
    p=json.loads(PLAN.read_text(encoding="utf-8"))
    old,decks=variants()
    prior,cards,again=inventory()
    if p["source"]["approved_raw_sha256"]!=old["authority"]["approved_raw_sha256"]:
        raise ValueError("Approved source mismatch")
    if p["source"]["physical_baseline_sha256"]!=prior["source_sha256"]:
        raise ValueError("Physical source mismatch")
    if p["variants"]!=list(decks) or list(decks)!=list(again):
        raise ValueError("Physical challenger order drift")
    if set(p["resolution_model"]["supported_effects"])!=SUPPORTED:
        raise ValueError("Preregistered effect subset changed")
    if p["policies"]!=["engine_first","burn_first"]:
        raise ValueError("Casting policies changed")
    return p,cards,decks


def expected_physical(library):
    return Counter(library)


def physical_zones(state):
    """Count exact named physical pieces; command-zone Abaddon is not library."""
    field=Counter(x for x in state["field"] if x!=ABADDON)
    return (Counter(state["deck"])+Counter(state["hand"]) +
            Counter(n for n,_ in state["lands"]) +
            Counter(state["graveyard"])+field)


def assert_conserved(state,original):
    now=physical_zones(state)
    if now!=original:
        raise AssertionError("A card was created, lost or doubled: "+
                             str((now-original,original-now)))


def tutor_target(deck,plan):
    for name in plan["resolution_model"]["tutor_priority"]:
        if name in deck:
            return name
    return min((x for x in deck if x not in LANDS_KNOWN),default=None)


def effect_add(pool,u=0,b=0,r=0,c=0):
    return pool[0]+u,pool[1]+b,pool[2]+r,pool[3]+c


def effect_resolve(name,state,seed,plan):
    """Resolve a cast *from exile*, with real physical zone and mana updates.

    Caller removed named hit from source deck and gave Birgi's triggered red
    before entering here. Caller owns allocation of the cast-spell zone.
    """
    red_before=state["pool"][2]
    extra={}
    if name=="Dark Ritual":
        state["pool"]=effect_add(state["pool"],b=3)
        state["metrics"]["hit_black_mana"]+=3
    elif name=="Rite of Flame":
        red=2+state["graveyard"].count("Rite of Flame")
        state["pool"]=effect_add(state["pool"],r=red)
        state["metrics"]["hit_red_mana"]+=red
    elif name=="Boltwave":
        state["loss"]+=9
        state["metrics"]["hit_opponent_loss"]+=9
    elif name=="Flame Rift":
        state["loss"]+=12
        state["pilot_life_damage"]+=4
        state["metrics"]["hit_opponent_loss"]+=12
        state["metrics"]["hit_pilot_damage"]+=4
    elif name=="Ancestral Vision":
        count=min(3,len(state["deck"]))
        for _ in range(count):
            state["hand"].append(state["deck"].pop(0))
        state["metrics"]["hit_cards_drawn"]+=count
        extra["physically_drawn"]=count
    elif name=="Sol Ring":
        # This is a noncreature artifact: its tap ability can be activated
        # the turn it enters. Fixed pilot taps it immediately exactly once.
        state["field"].add(name)
        state["rocks_tapped"]=True
        state["pool"]=effect_add(state["pool"],c=2)
        state["metrics"]["hit_colorless_mana"]+=2
    elif name=="Lotus Petal":
        # EtB, tap/sac for red, put in physical graveyard. Never re-tap.
        state["pool"]=effect_add(state["pool"],r=1)
        state["graveyard"].append(name)
        state["metrics"]["hit_red_mana"]+=1
    elif name in (HAND_TUTORS|TOP_TUTORS):
        target=tutor_target(state["deck"],plan)
        if target is not None:
            state["deck"].remove(target)
        # Tutor shuffles even when no useful card found. Target is physical.
        random.Random(seed ^ 0x70A70).shuffle(state["deck"])
        if name in TOP_TUTORS:
            if target is not None:
                state["deck"].insert(0,target)
                state["metrics"]["hit_tutored_top"]+=1
        else:
            if target is not None:
                state["hand"].append(target)
                state["metrics"]["hit_tutored_hand"]+=1
        if name in TOP_TUTORS:
            state["pilot_life_damage"]+=2
            state["metrics"]["hit_pilot_damage"]+=2
        if name=="Gamble" and state["hand"]:
            rng=random.Random(seed ^ 0x6A4B1E)
            discarded=state["hand"].pop(rng.randrange(len(state["hand"])))
            state["graveyard"].append(discarded)
            state["metrics"]["gamble_discarded"]+=1
            extra["discarded"]=discarded
        extra["physically_searched"]=target
    else:
        raise ValueError("Unregistered effect attempted: "+name)
    if name in INSTANT_SORCERY:
        state["graveyard"].append(name)
    # Lotus Petal was sacrificed; Sol Ring remains battlefield.
    state["metrics"]["actual_supported_hits_resolved"]+=1
    state["metrics"]["resolved_hit_"+name]+=1
    return extra


def first_cascade(state,cards,seed,plan,*,rule_of_law=False,drannith=False,trigger_mv=3,source_kind="ignus"):
    """One physical cascade trigger for source-paid hand spell; casting limits.

    Rule of Law assumes Ignus already consumed the turn's one spell.
    Drannith stops exile cast, not cascade triggering or physical exiling.
    Defaults reproduce PR524 exact no-hate source-state simulation.
    """
    if trigger_mv<0 or not isinstance(trigger_mv,int):
        raise ValueError("Cascade spell printed mana value must be nonnegative integer")
    if source_kind not in ("ignus","other_hand"):
        raise ValueError("Cascade source must be actual registered hand spell")
    d=state["deck"]
    before=Counter(d)
    exile=[]
    hit=None
    while d:
        name=d.pop(0)
        exile.append(name)
        if name not in cards:
            raise ValueError("Nonregistered card was exiled")
        if not is_land(cards[name]) and cards[name]["mv"]<trigger_mv:
            hit=name
            break
    legal=(legality_of_hit(hit,rule_of_law=rule_of_law,drannith=drannith) if hit else
           {"legal_to_cast":False,"chosen_cast":False,"reason":"empty"})
    supported=hit in SUPPORTED
    chosen=bool(supported and legal["chosen_cast"])
    to_bottom=list(exile)
    if chosen:
        to_bottom.remove(hit)
    random.Random(seed ^ 0xCA5CADE).shuffle(to_bottom)
    d.extend(to_bottom)
    if source_kind=="ignus":
        state["metrics"]["actual_paid_ignus_cascade"]+=1
    else:
        state["metrics"]["actual_other_hand_cascade"]+=1
    state["metrics"]["cascade_cards_exiled"]+=len(exile)
    state["metrics"]["first_hit_seen"]+=int(hit is not None)
    if chosen:
        # Birgi cast trigger for the EXILE-cast hit resolves before spell.
        if BIRGI in state["field"]:
            state["pool"]=effect_add(state["pool"],r=1)
            state["metrics"]["birgi_red_from_exile_hit"]+=1
        state["metrics"]["actual_supported_hit_cast"]+=1
        detail=effect_resolve(hit,state,seed,plan)
    else:
        state["metrics"]["unsupported_or_illegal_hit_declined"]+=int(hit is not None)
        state["metrics"]["declined_"+(hit or "no_hit")]+=1
        detail={}
    return {"hit":hit,"cast_from_exile":chosen,"source_kind":source_kind,
            "source_printed_mv":trigger_mv,
            "supported_and_effect_resolved":chosen,
            "reason":("supported" if chosen else legal["reason"] if not legal["chosen_cast"] else "unmodeled_effect_declined"),
            **detail}


def create_state(library,seed):
    if len(library)!=99:raise ValueError("Expected 99 physical library cards")
    deck=list(library)
    random.Random(seed).shuffle(deck)
    s={"deck":deck[7:],"hand":deck[:7],"field":set(),
       "lands":[],"graveyard":[],"pool":ZERO,"loss":0,
       "pilot_life_damage":0,"rocks_tapped":False,
       "metrics":Counter(),"examples":[]}
    assert_conserved(s,expected_physical(library))
    return s


def recast_ignus(state,cards,plan,seed,turn,*,rule_of_law=False,drannith=False):
    # Fixed conservative choice: don't pay bounce cost if Rule of Law
    # already prevents casting another hand spell this turn.
    if rule_of_law:
        return 0
    count=0
    for i in range(plan["sample"]["max_ignus_recasts_per_main"]):
        if IGNUS not in state["field"]:
            break
        # Bounce at sorcery speed; {R}, return Ignus -> {C}{C}{R}.
        bounce=pay_and_tap(state["lands"],state["pool"],IGNUS,
                           source_cost_override=(1,(0,0,1)))
        if bounce is None:break
        state["field"].remove(IGNUS)
        state["hand"].append(IGNUS)
        state["pool"]=effect_add(bounce,r=1,c=2)
        cast=source_cast(state["lands"],state["pool"],IGNUS,
                rakdos_controlled=RAKDOS in state["field"],
                familiar_controlled=FAMILIAR in state["field"],
                opponent_loss=state["loss"])
        if cast is None:
            raise AssertionError("Ignus activation made its own paid recast unaffordable")
        state["pool"]=cast
        state["hand"].remove(IGNUS)
        if BIRGI in state["field"]:
            state["pool"]=effect_add(state["pool"],r=1)
        if ABADDON in state["field"] and state["loss"]>=3:
            receipt=first_cascade(state,cards,seed^(turn*1301)^(i*53),plan,
                                  drannith=drannith)
            state["metrics"]["additional_cascade_from_paid_recast"]+=1
            if len(state["examples"])<3:
                state["examples"].append({"turn":turn,"recast":i+1,**receipt})
        state["field"].add(IGNUS) # now original Ignus spell resolves
        count+=1
    state["metrics"]["paid_ignus_additional_recasts"]+=count
    if count>=5 and state["loss"]>=3 and ABADDON in state["field"]:
        state["metrics"]["one_turn_5_recast_cascade_line"]+=1
    return count


def main_phase(state,cards,plan,seed,turn,policy,*,other_hand_cascades=False):
    if policy=="engine_first":
        order=[FAMILIAR,BIRGI,ABADDON,"Boltwave","Flame Rift",RAKDOS,IGNUS,ASSAULT]
    elif policy=="burn_first":
        order=["Boltwave","Flame Rift",FAMILIAR,BIRGI,ABADDON,RAKDOS,IGNUS,ASSAULT]
    else:raise ValueError("Unknown policy")
    ignus_cast_this_turn=False
    for name in order:
        if name in state["field"] or (name!=ABADDON and name not in state["hand"]):
            continue
        qualified_other=(name!=IGNUS and name!=ABADDON and
                 ABADDON in state["field"] and state["loss"]>=MV_AND_COLORS[name][0])
        cost=source_cast(state["lands"],state["pool"],name,
                    rakdos_controlled=RAKDOS in state["field"],
                    familiar_controlled=FAMILIAR in state["field"],
                    opponent_loss=state["loss"])
        if cost is None:continue
        state["pool"]=cost
        state["metrics"]["paid_hand_cast_"+name]+=1
        if name!=ABADDON:
            state["hand"].remove(name)
        if BIRGI in state["field"]:
            state["pool"]=effect_add(state["pool"],r=1)
        if qualified_other:
            if other_hand_cascades:
                source_mv=MV_AND_COLORS[name][0]
                if name in cards and cards[name]["mv"]!=source_mv:
                    raise ValueError("Printed MV for source hand spell changed: "+name)
                receipt=first_cascade(state,cards,seed^(turn*877)^(source_mv*739),
                                     plan,trigger_mv=source_mv,source_kind="other_hand")
                state["metrics"]["other_hand_cascade_triggers_resolved"]+=1
                if len(state["examples"])<3:
                    state["examples"].append({"turn":turn,"source_hand_cast":name,**receipt})
            else:
                state["metrics"]["other_hand_cascade_triggers_OMITTED"]+=1
        if name==IGNUS:
            ignus_cast_this_turn=True
            state["metrics"]["ignus_initial_paid_cast"]+=1
            if ABADDON in state["field"] and state["loss"]>=3:
                receipt=first_cascade(state,cards,seed^(turn*733),plan)
                state["metrics"]["first_ignus_cascade"]+=1
                if len(state["examples"])<3:
                    state["examples"].append({"turn":turn,"first_cast":True,**receipt})
        if name in BURNS:
            # Instants/sorceries resolve into the graveyard, never on board.
            state["loss"]+=9 if name=="Boltwave" else 12
            state["graveyard"].append(name)
            if name=="Flame Rift":
                state["pilot_life_damage"]+=4
        else:
            state["field"].add(name)
        if name==IGNUS:
            recast_ignus(state,cards,plan,seed,turn)
    if IGNUS in state["field"] and not ignus_cast_this_turn:
        recast_ignus(state,cards,plan,seed,turn)


def one_trial(library,seed,policy,plan,cards,*,checkpoints=None):
    checkpoints=checkpoints or plan["sample"]["checkpoints"]
    state=create_state(library,seed)
    original=expected_physical(library)
    snapshots={}
    for turn in range(1,max(checkpoints)+1):
        state["lands"]=[(n,False) for n,_ in state["lands"]]
        state["pool"]=ZERO
        state["loss"]=0
        state["rocks_tapped"]=False
        if "Sol Ring" in state["field"]:
            state["pool"]=effect_add(state["pool"],c=2)
            state["rocks_tapped"]=True
            state["metrics"]["existing_sol_ring_retap_mana"]+=2
        if state["deck"]:
            state["hand"].append(state["deck"].pop(0))
        searches,land=play_land(state["hand"],state["deck"],state["lands"],seed,turn)
        if land in FETCHES:
            state["graveyard"].append(land)
        state["metrics"]["fetch_searches"]+=searches
        main_phase(state,cards,plan,seed,turn,policy)
        assert_conserved(state,original)
        if turn in checkpoints:
            m=state["metrics"]
            snapshots[str(turn)]={
                "paid_initial_ignus_cast":m["ignus_initial_paid_cast"]>0,
                "actual_ignus_cascade_trigger":m["actual_paid_ignus_cascade"]>0,
                "actual_supported_hit_cast":m["actual_supported_hit_cast"]>0,
                "actual_supported_effect_resolved":m["actual_supported_hits_resolved"]>0,
                "cards_actually_drawn_by_hit":m["hit_cards_drawn"],
                "cards_physically_tutored_by_hit":m["hit_tutored_hand"]+m["hit_tutored_top"],
                "opponent_loss_from_cascade_hit":m["hit_opponent_loss"],
                "mana_from_cascade_hit":sum(m[k] for k in ("hit_red_mana","hit_black_mana","hit_colorless_mana")),
                "five_cascade_recasts":m["one_turn_5_recast_cascade_line"]>0,
                "ignored_other_hand_cascade":m["other_hand_cascade_triggers_OMITTED"],
                "unsupported_declined":m["unsupported_or_illegal_hit_declined"],
            }
    return snapshots,state


def run(samples=None):
    p,cards,decks=verify()
    n=p["sample"]["n_per_variant_policy"] if samples is None else samples
    if n<1:raise ValueError("Invalid sample count")
    evidence={}
    for policy in p["policies"]:
        evidence[policy]={}
        for variant,library in decks.items():
            total={str(t):Counter() for t in p["sample"]["checkpoints"]}
            examples=[]
            for i in range(n):
                seed=p["sample"]["seed"]+104729*i
                snapshots,final=one_trial(library,seed,policy,p,cards)
                for turn,row in snapshots.items():
                    for k,val in row.items():
                        total[turn][k]+=int(val)
                if final["metrics"]["actual_supported_hits_resolved"] and len(examples)<3:
                    examples.append({"seed":seed,"cascade_effects":dict(final["metrics"]),
                                     "illustrative_hit_traces":final["examples"]})
            evidence[policy][variant]={"checkpoints":{k:dict(sorted(v.items())) for k,v in total.items()},
                                       "supported_hit_examples":examples}
    return {"schema_version":1,"preregistration":str(PLAN.relative_to(ROOT)),
            "canonical_approved_sha256":p["source"]["approved_raw_sha256"],
            "samples_per_variant_policy":n,"policies":p["policies"],
            "variants":evidence,
            "bounds":p["limits"]}


def main():
    a=argparse.ArgumentParser()
    a.add_argument("--samples",type=int)
    a.add_argument("--out")
    args=a.parse_args()
    receipt=run(args.samples)
    if args.out:
        Path(args.out).write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    for policy,variants in receipt["variants"].items():
        for name,record in variants.items():
            print(policy,name,"T10",json.dumps(record["checkpoints"]["10"],sort_keys=True))
    print("TRUE physical paid Ignus cascade and restricted effects; NOT full games or wins.")


if __name__=="__main__":main()
