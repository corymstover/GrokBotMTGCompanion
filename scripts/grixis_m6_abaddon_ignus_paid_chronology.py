#!/usr/bin/env python3
"""Source-paid, PHYSICAL 100-card Abaddon/Ignus pilot under two fixed cast policies.

Not a complete multiplayer engine. Does not resolve cascade, attacks, opposing
actions, tutors, fast mana, other draw, combat/Neheb/Assault activations or wins.
Uses frozen SHA-linked 99 library and source-consuming mana selection from prior
M6 access work. See preregistered JSON for scope and critical biases.
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
from grixis_m6_abaddon_ignus_birgi import source_inventory
from grixis_m6_abaddon_assault_access import play_land
from grixis_m6_abaddon_chronological_engine import ZERO, pay_and_tap

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_ignus_paid_chronology_20261021.json"
BIRGI="Birgi, God of Storytelling // Harnfel, Horn of Bounty"
ABADDON="Abaddon the Despoiler"
IGNUS="Grinning Ignus"
FAMILIAR="Nightscape Familiar"
RAKDOS="Rakdos, Lord of Riots"
ASSAULT="Aggravated Assault"
BURNS=("Boltwave","Flame Rift")
MV_AND_COLORS={
    ABADDON:(5,(1,1,1)),
    BIRGI:(3,(0,0,1)),
    FAMILIAR:(2,(0,1,0)),
    IGNUS:(3,(0,0,1)),
    RAKDOS:(4,(0,2,2)),
    ASSAULT:(3,(0,0,1)),
    "Boltwave":(1,(0,0,1)),
    "Flame Rift":(2,(0,0,1))
}


def variants():
    plan=json.loads(PLAN.read_text(encoding="utf-8"))
    old,base,_packet=source_inventory()
    if plan["authority"]["approved_raw_sha256"]!=old["canonical_approved_raw_sha256"]:
        raise ValueError("Approved baseline SHA drift")
    if plan["authority"]["engineering_source_sha256"]!=old["frozen_source_sha256"]:
        raise ValueError("Frozen source hash mismatch")
    decks=dict(base)
    approved=list(base["approved"])
    if approved.count(RAKDOS)!=1 or approved.count(IGNUS)!=0:
        raise ValueError("Incumbent identity changed")
    deck=list(approved)
    deck[deck.index(RAKDOS)]=ASSAULT
    if ASSAULT in approved or len(deck)!=99:
        raise ValueError("Assault challenger slot invalid")
    decks["assault_for_rakdos"]=deck
    if set(decks)!={q["id"] for q in plan["registered_variants"]}:
        raise ValueError("Preregistered candidate variants drift")
    for q in plan["registered_variants"]:
        a=approved
        b=decks[q["id"]]
        difference=[i for i,(x,y) in enumerate(zip(a,b)) if x!=y]
        if len(difference)!=int(q["cut"] is not None):
            raise ValueError("Physical 99 swap size invalid")
        if q["cut"] and (a[difference[0]]!=q["cut"] or b[difference[0]]!=q["add"]):
            raise ValueError("Wrong one-card substitution")
    return plan,decks


def source_cast(lands,pool,name, *, rakdos_controlled=False,
                familiar_controlled=False,opponent_loss=0):
    """Mana source paid, proper printed MV preserved for separate cascade.

    Nightscape reduces generic cost exactly once for any U and/or R spell,
    never colored pips. Rakdos reduces generic on a creature if opponents
    lost life that turn. Reduction is additive but never below colored cost.
    """
    total,pips=MV_AND_COLORS[name]
    if name==RAKDOS and opponent_loss<=0:
        return None
    generic=total-sum(pips)
    discount=int(familiar_controlled and name in
          (ABADDON,BIRGI,IGNUS,RAKDOS,ASSAULT,"Boltwave","Flame Rift"))
    if rakdos_controlled and opponent_loss>0 and name in
        (ABADDON,BIRGI,FAMILIAR,IGNUS,RAKDOS):
        discount+=opponent_loss
    new_total=sum(pips)+max(0,generic-discount)
    return pay_and_tap(lands,pool,name,source_cost_override=(new_total,pips))


def cast_spells_one_main(*,deck,hand,lands,pool,battlefield,policy,turn,first_cast_turn):
    """Fixed named-spell policy, one legal precombat main; no responsive opponents.

    The first source-paid Ignus cast is followed by up to five further finite
    bounce/recasts in the same main, with physical costs and optional Rakdos
    creature-generic discounts. No opponent life-loss or mana from cascade.
    """
    loss=0
    paid=[]
    ignus_initial_cascade=0
    extra_ignus_cascades=0
    extra_recasts=0
    threshold_source=0
    if policy=="engine_first":
        sequence=[FAMILIAR,BIRGI,ABADDON,*BURNS,RAKDOS,IGNUS,ASSAULT]
    elif policy=="burn_first":
        sequence=[*BURNS,FAMILIAR,BIRGI,ABADDON,RAKDOS,IGNUS,ASSAULT]
    else:
        raise ValueError("Unknown preregistered pilot policy")
    for name in sequence:
        if name in battlefield or name!=ABADDON and name not in hand:
            continue
        cancascade=ABADDON in battlefield and loss>=MV_AND_COLORS[name][0]
        newpool=source_cast(lands,pool,name,rakdos_controlled=(RAKDOS in battlefield),
                            familiar_controlled=(FAMILIAR in battlefield),
                            opponent_loss=loss)
        if newpool is None:
            continue
        pool=newpool
        paid.append(name)
        if name==IGNUS and cancascade:
            ignus_initial_cascade+=1
        # Birgi must have been controlled on *casting* the spell, so casting
        # Birgi itself does not generate mana; its trigger resolves before
        # the modeled next main-phase action.
        if BIRGI in battlefield:
            pool=(pool[0],pool[1],pool[2]+1,pool[3])
        battlefield.add(name)
        if name!=ABADDON:
            hand.remove(name)
        if name in BURNS:
            # Source-paid, uncountered, unprevented damage assumption. Birgi
            # triggers before spell resolves; no cascade hit cast is modeled.
            new_loss=9 if name=="Boltwave" else 12
            loss+=new_loss
            threshold_source+=new_loss
        if name==IGNUS:
            # Does not require summoning sickness to have worn off: activated
            # bounce has no tap symbol and sorcery timing is in our main.
            count,cascades,pool=finite_recasts(
                lands,pool,battlefield,loss, limit=5)
            extra_recasts+=count
            extra_ignus_cascades+=cascades
    # A cast Ignus remains on battlefield in this closed fixture. At a later
    # turn, it can activate its legal main-phase bounce even without recasting
    # initially that turn, provided it is still alive in this no-removal run.
    if IGNUS in battlefield and IGNUS not in paid:
        count,cascades,pool=finite_recasts(
            lands,pool,battlefield,loss, limit=5)
        extra_recasts+=count
        extra_ignus_cascades+=cascades
    return {
        "cast_names":paid,
        "opponent_loss_precombat_from_burn":loss,
        "threshold_from_paid_burn":threshold_source,
        "ignus_initial_cascade_triggers":ignus_initial_cascade,
        "ignus_additional_paid_recasts":extra_recasts,
        "ignus_additional_cascade_triggers":extra_ignus_cascades,
        "five_recasts_same_main":extra_recasts>=5,
    }


def finite_recasts(lands,pool,battlefield,loss,*,limit=5):
    casts=0
    cascades=0
    for _ in range(limit):
        if IGNUS not in battlefield:
            raise AssertionError("Ignoring physical zone of Ignus")
        # If red cannot be supplied, don't return Ignus to hand: it is safer
        # to leave it on battlefield and cannot claim a cast.
        bounce=pay_and_tap(lands,pool,IGNUS,source_cost_override=(1,(0,0,1)))
        if bounce is None:
            break
        # Activated ability {R}, return Ignus to hand: produce {C}{C}{R}.
        # To avoid an artificial rollback of landed taps we can spend
        # 2C+R only after verifying the next cast is itself affordable.
        newpool=(bounce[0],bounce[1],bounce[2]+1,bounce[3]+2)
        trial_lands=list(lands)
        # pay_and_tap runs on a COPY of lands to ensure a safe candidate
        # before recording any further taps, and never creates mana.
        recast=source_cast(trial_lands,newpool,IGNUS,
                            rakdos_controlled=RAKDOS in battlefield,
                            familiar_controlled=FAMILIAR in battlefield,
                            opponent_loss=loss)
        if recast is None:
            # Ignus always generates two colorless plus one red when bounced,
            # covering its full {2}{R} recast even with zero reduction. A
            # failed payment here means a bug in the closed source subset.
            raise AssertionError("Ignus bounce generated insufficient recast mana")
        lands[:]=trial_lands
        pool=recast
        # The new hand-cast Ignus has cascade ONLY if Abaddon was already
        # controlled AND loss threshold >= Ignus's unmodified MV3.
        if ABADDON in battlefield and loss>=3:
            cascades+=1
        # Birgi's triggered red is available after it resolves; not a mana
        # ability and it can be countered, which is separately tested.
        if BIRGI in battlefield:
            pool=(pool[0],pool[1],pool[2]+1,pool[3])
        casts+=1
    return casts,cascades,pool


def one_trial(lib,seed,policy,checkpoints):
    if len(lib)!=99:
        raise ValueError("Frozen 99-card physical library required")
    rng=random.Random(seed)
    cards=list(lib);rng.shuffle(cards)
    hand,cards=cards[:7],cards[7:]
    field=set()
    lands=[]
    results={}
    first_paid_loop_turn=None
    all_paid_casts=[]
    initial_ignus_cascade_seen=False
    for turn in range(1,max(checkpoints)+1):
        lands=[(name,False) for name,_ in lands]
        # All floating mana, including Birgi, is cleared between TURNS.
        pool=ZERO
        hand.append(cards.pop(0))
        play_land(hand,cards,lands,seed,turn)
        r=cast_spells_one_main(deck=lib,hand=hand,lands=lands,pool=pool,
                             battlefield=field,policy=policy,turn=turn,
                             first_cast_turn=None)
        all_paid_casts.extend(r["cast_names"])
        initial_ignus_cascade_seen|=bool(r["ignus_initial_cascade_triggers"])
        if (r["five_recasts_same_main"] and
                r["ignus_additional_cascade_triggers"]>=5 and
                first_paid_loop_turn is None):
            first_paid_loop_turn=turn
        if turn in checkpoints:
            results[turn]={
                "abaddon_cast":ABADDON in field,
                "birgi_cast":BIRGI in field,
                "familiar_cast":FAMILIAR in field,
                "rakdos_cast":RAKDOS in field,
                "ignus_initial_paid_cast":IGNUS in all_paid_casts,
                "ignus_ever_granted_initial_cascade":initial_ignus_cascade_seen,
                "paid_5_repeat_ignus_cascades":first_paid_loop_turn is not None,
                "assault_cast":ASSAULT in field,
                "burn_spells_paid_resolved_count":sum(x in BURNS for x in all_paid_casts),
                "paid_named_spells":len(all_paid_casts)
            }
    return results,first_paid_loop_turn


def response_windows():
    """Only independent stack-rule case truths; no opponent policy or rates."""
    return {
      "counter_ignus_initial_cast":{"birgi_cast_trigger_still_exists":True,
         "abaddon_cascade_already_granted_if_qualified":True,
         "ignus_resolves_as_permanent":False,
         "recast_loop_resumes_without_another_ignus":False},
      "remove_abaddon_in_response_to_first_ignus":{
         "previously_triggered_cascade_kept":True,
         "future_ignus_casts_gain_abaddon_cascade":False},
      "remove_birgi_with_first_cast_trigger_on_stack":{
         "existing_birgi_red_trigger_kept":True,
         "future_birgi_red_triggers":False,
         "extra_mana_could_fund_another_recast":True},
      "rule_of_law_resolved":{
         "at_most_one_spell_that_turn":True,
         "ignus_bounce_is_not_a_spell":True,
         "repeat_ignus_hand_casts_same_turn_legal":False,
         "cascade_trigger_may_exist_without_legal_exile_cast":True},
      "drannith_magistrate_resolved":{
         "ignus_cast_from_hand_prohibited":False,
         "abaddon_cascade_trigger_happens_if_qualified":True,
         "casting_cascade_exiled_hit_prohibited":True},
    }


def run(samples=None):
    p,decks=variants()
    samples=p["samples_per_variant_policy"] if samples is None else samples
    if samples<1:
        raise ValueError("No sample count")
    obs={}
    for policy in p["policies"]:
        obs[policy]={}
        for vid,lib in decks.items():
            aggregate={t:Counter() for t in p["checkpoints"]}
            first=[]
            for i in range(samples):
                seed=p["seed"]+104729*i
                row,first_turn=one_trial(lib,seed,policy,p["checkpoints"])
                for t,metrics in row.items():
                    for k,v in metrics.items():
                        aggregate[t][k]+=int(v)
                if first_turn is not None and len(first)<5:
                    first.append({"seed":seed,"turn":first_turn})
            obs[policy][vid]={"observations":{str(t):dict(sorted(counter.items()))
                                                for t,counter in aggregate.items()},
                              "first_legal_five_recast_seeds":first}
    return {"schema_version":1,
      "stage":"BOUNDED_PHYSICAL_PAID_NAMED_SPELL_SOURCE_ACCESS",
      "preregistration":str(PLAN.relative_to(ROOT)),
      "canonical_raw_sha256":p["authority"]["approved_raw_sha256"],
      "n_per_variant_per_policy":samples,
      "paired_seed":p["seed"],"policies":p["policies"],
      "variants":obs,"response_windows":response_windows(),
      "not_modeled":{
          "actual_cascade_hits_cast":False,
          "fast_mana_rocks_rituals_tutors_draw_engines":False,
          "opponent_responses_in_simulated_trajectories":False,
          "combat_neheb_loyal_assault_activation":False,
          "creature_damage_or_incumbent_role_value":False,
          "full_multiplayer_gameplay":False,
          "true_game_win_rate":None,
          "swap_superiority_proved":False,
          "m6_completed":False,
          "m6_certificates":0,"m7_approvals":0,
          "canonical_changed":False}
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--samples",type=int,default=None)
    parser.add_argument("--out")
    args=parser.parse_args()
    result=run(args.samples)
    if args.out:
        Path(args.out).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",
                                  encoding="utf-8")
    for policy,data in result["variants"].items():
        for variant,counts in data.items():
            print(policy,variant,"T10",
                  json.dumps(counts["observations"]["10"],sort_keys=True))
    print("NO actual game win rate, full cascade resolutions or swap authority.")


if __name__=="__main__":
    main()
