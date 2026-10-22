#!/usr/bin/env python3
"""Bounded first Ignus cascade hit on the frozen physical Abaddon 99 cards.

The cascade trigger is HYPOTHETICAL at each checkpoint; neither casting
Ignus nor the prerequisite commander/life-loss setup is constructed here.
The exile -> optional no-cost spell cast -> random-bottom process is real
source-bound deck manipulation. Spell effects / game wins are NOT simulated.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from grixis_m6_abaddon_assault_access import frozen_source, play_land
from grixis_m6_abaddon_ignus_paid_chronology import variants as physical_variants

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_ignus_cascade_first_hit_20261021.json"
NO_TARGET={"Flusterstorm","Swan Song"}
SELF_COUNTER={"Pact of Negation"}
LEGAL_NO_EFFECT={"Pyroblast"}


def inventory():
    p=json.loads(PLAN.read_text(encoding="utf-8"))
    prior,baseline=frozen_source()
    if p["canonical_raw_sha256"]!=prior["canonical_approved_raw_sha256"] or p["source_sha256"]!=prior["source_sha256"]:
        raise ValueError("Frozen approved or source hash drift")
    raw=(ROOT/p["graph_path"]).read_bytes()
    blob=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
    if blob!=p["graph_git_blob_sha"]:
        raise ValueError("Frozen generated card-mana graph blob changed")
    graph=json.loads(raw)
    cards={x["name"]:x for x in graph["nodes"] if x.get("kind")=="card" and x.get("zone") in ("main","command")}
    # The frozen card graph rightly contains only the approved list; two
    # proposed additions have their OWN preregistered source-verified costs.
    # Never classify a physical challenger from a guessed missing graph node.
    ignus=json.loads((ROOT/"data/grixis/m6/phase_b_plans/abaddon_ignus_birgi_20261021.json").read_text())
    byname={r["card"]:r for r in ignus["source_verification"]}
    if byname["Grinning Ignus"]["cost"]!="{2}{R}":
        raise ValueError("Grinning Ignus registered printed cost drift")
    assault=json.loads((ROOT/"data/grixis/m6/phase_b_plans/abaddon_chronological_engine_20261021.json").read_text())
    if "Aggravated Assault" not in str(assault):
        raise ValueError("Assault preresolved challenger role absent")
    from grixis_m6_abaddon_assault_access import SPELL_COST
    if SPELL_COST["Aggravated Assault"]!=(3,(0,0,1)):
        raise ValueError("Aggravated Assault source cost changed")
    cards["Grinning Ignus"]={"name":"Grinning Ignus","mv":3,"type_line":"Creature — Elemental","source":"PR518 source-verification"}
    cards["Aggravated Assault"]={"name":"Aggravated Assault","mv":3,"type_line":"Enchantment","source":"PR514 frozen source-paid cost fixture"}
    if not all(name in cards for name in set(baseline)):
        raise ValueError("Source physical cards missing from graph")
    under=[name for name in baseline if not is_land(cards[name])
           and int(cards[name]["mv"])<3]
    bymv=Counter(int(cards[name]["mv"]) for name in under)
    expected=p["baseline_nonland_lt3"]
    if len(under)!=expected["total_unique_physical"] or any(bymv[i]!=expected["mv"+str(i)] for i in (0,1,2)):
        raise ValueError("Wrong sub-three source card pool or graph Oracle metadata")
    # Every named role must be a true physical card with appropriate mana value.
    for role,names in p["roles"].items():
        for name in names:
            if name not in under:
                raise ValueError("Registered role absent from lower MV physical pool: "+name)
    q,deck_variants=physical_variants()
    if set(deck_variants)!={r["id"] for r in p["candidate_physical_variants"]}:
        raise ValueError("Variant identity drift")
    for row in p["candidate_physical_variants"]:
        old=list(baseline);new=deck_variants[row["id"]]
        differences=[(a,b) for a,b in zip(old,new) if a!=b]
        if differences!=([] if row["cut"] is None else [(row["cut"],row["add"])]):
            raise ValueError("Physical challenger has unexpected modifications")
    return p,cards,deck_variants


def is_land(card):
    return "Land" in card["type_line"]


def role_tags(name,plan):
    return tuple(key for key,names in plan["roles"].items() if name in names)


def legality_of_hit(name,*,rule_of_law=False,drannith=False,
                    only_original_ignus_on_stack=True):
    if rule_of_law or drannith:
        return {"legal_to_cast":False,"chosen_cast":False,
                "reason":"spell_limit" if rule_of_law else "nonhand_spell_prohibited"}
    if only_original_ignus_on_stack and name in NO_TARGET:
        return {"legal_to_cast":False,"chosen_cast":False,"reason":"no_target_other_spell_type"}
    if only_original_ignus_on_stack and name in SELF_COUNTER:
        return {"legal_to_cast":True,"chosen_cast":False,"reason":"decline_self_counter_original_ignus"}
    if only_original_ignus_on_stack and name in LEGAL_NO_EFFECT:
        return {"legal_to_cast":True,"chosen_cast":True,"reason":"legal_red_ignus_target_no_blue_effect"}
    return {"legal_to_cast":True,"chosen_cast":True,"reason":"permissible_under_fixed_stack"}


def resolve_cascade(deck,cards,*,seed,trigger_mv=3,rule_of_law=False,
                    drannith=False,only_original_ignus_on_stack=True):
    """Mutate deck physically and return bounded cast-permission trace.

    All cards (including unchosen last hit) are put back on the bottom in a
    random order, except an actually cast last hit. A cascade hit itself is
    a spell cast FROM EXILE, never from hand; no added Abaddon cascade.
    """
    if trigger_mv<1:
        raise ValueError("No valid cascade hit has MV below a <=0 spell")
    initial=Counter(deck)
    exiled=[]
    hit=None
    while deck:
        name=deck.pop(0)
        exiled.append(name)
        if name not in cards:
            raise ValueError("Graph missing physical exiled card")
        card=cards[name]
        if not is_land(card) and int(card["mv"])<trigger_mv:
            hit=name
            break
    check=(legality_of_hit(hit,rule_of_law=rule_of_law,drannith=drannith,
                            only_original_ignus_on_stack=only_original_ignus_on_stack)
           if hit is not None else
           {"legal_to_cast":False,"chosen_cast":False,"reason":"no_eligible_nonland_remaining"})
    returned=list(exiled)
    if hit is not None and check["chosen_cast"]:
        returned.remove(hit)
    random.Random(seed ^ 0xC45CADE).shuffle(returned)
    deck.extend(returned)
    expected=initial.copy()
    if hit is not None and check["chosen_cast"]:
        expected[hit]-=1
        if expected[hit]==0:
            del expected[hit]
    if Counter(deck)!=expected:
        raise AssertionError("Cascade lost or duplicated a physical library card")
    return {
        "first_hit":hit,
        "hit_mana_value":None if hit is None else int(cards[hit]["mv"]),
        "exiled_count":len(exiled),
        "chosen_cast_from_exile":bool(check["chosen_cast"]),
        "legal_to_cast":bool(check["legal_to_cast"]),
        "reason":check["reason"],
        "uncast_bottom_count":len(returned),
        "library_after":len(deck),
        "abaddon_granted_cascade_to_exile_hit":False,
        "actual_hit_effect_resolved":False,
    }


def trial(cards,library,seed,checkpoints,plan):
    # Snapshot each turn's surviving real cards, not a made-up second deck;
    # cascade is independent at each checkpoint and does not change the next
    # turn's shared physical progression.
    deck=list(library)
    random.Random(seed).shuffle(deck)
    hand,deck=deck[:7],deck[7:]
    lands=[]
    rows={}
    for turn in range(1,max(checkpoints)+1):
        lands=[(n,False) for n,_ in lands]
        hand.append(deck.pop(0))
        play_land(hand,deck,lands,seed,turn)
        if turn in checkpoints:
            cloned=list(deck)
            event=resolve_cascade(cloned,cards,seed=seed ^ (turn*919),trigger_mv=3)
            roles=role_tags(event["first_hit"],plan) if event["first_hit"] else ()
            event["hit_roles"]=roles
            event["physically_eligible_snapshot_only"]=True
            rows[turn]=event
    return rows


def run(samples=None):
    p,cards,variants=inventory()
    samples=p["simulation"]["samples_per_variant"] if samples is None else samples
    if samples<=0:
        raise ValueError("Nonpositive experiment count")
    checkpoints=p["simulation"]["checkpoints"]
    counts={}
    for name,library in variants.items():
        at={str(t):Counter() for t in checkpoints}
        hit_counts={str(t):Counter() for t in checkpoints}
        example={}
        for i in range(samples):
            seed=p["simulation"]["seed"]+i*104729
            records=trial(cards,library,seed,checkpoints,p)
            for turn,event in records.items():
                key=str(turn)
                at[key]["conditional_eligible_hit"]+=int(event["first_hit"] is not None)
                at[key]["free_cast_legal"]+=int(event["legal_to_cast"])
                at[key]["free_cast_chosen_under_safe_policy"]+=int(event["chosen_cast_from_exile"])
                at[key]["no_cast_or_declined"]+=int(not event["chosen_cast_from_exile"])
                at[key]["cards_exiled_total"]+=event["exiled_count"]
                at[key]["hit_mv_"+str(event["hit_mana_value"])]+=int(event["first_hit"] is not None)
                for tag in event["hit_roles"]:
                    at[key]["hit_role_"+tag]+=1
                at[key]["reason_"+event["reason"]]+=1
                if event["first_hit"]:
                    hit_counts[key][event["first_hit"]]+=1
                if event["reason"] not in example:
                    example[event["reason"]]={"seed":seed,"turn":turn,"hit":event["first_hit"]}
        counts[name]={"checkpoints":{k:dict(sorted(x.items())) for k,x in at.items()},
                      "hit_names":{k:dict(sorted(x.items())) for k,x in hit_counts.items()},
                      "examples":example}
    # These fail-closed adversarial response cases are NOT sampled into the
    # physical cascade-hit histogram or treated as opponent frequencies.
    rules={
      "suspend_ancestral":resolve_cascade(["Ancestral Vision"],cards,seed=3),
      "suspend_inevitable":resolve_cascade(["Inevitable Betrayal"],cards,seed=3),
      "suspend_profane":resolve_cascade(["Profane Tutor"],cards,seed=3),
      "rule_of_law":resolve_cascade(["Sol Ring"],cards,seed=3,rule_of_law=True),
      "drannith":resolve_cascade(["Sol Ring"],cards,seed=3,drannith=True),
      "flusterstorm_only_ignus":resolve_cascade(["Flusterstorm"],cards,seed=3),
      "swan_song_only_ignus":resolve_cascade(["Swan Song"],cards,seed=3),
      "pact_of_negation_only_ignus":resolve_cascade(["Pact of Negation"],cards,seed=3),
      "pyroblast_only_ignus":resolve_cascade(["Pyroblast"],cards,seed=3),
      "cascade_does_not_cast_land":resolve_cascade(["Island","Ancient Tomb","Sol Ring"],cards,seed=3)
    }
    return {
       "schema_version":1,"stage":"CONDITIONAL_FIRST_EXILE_CASCADE_HIT_CAST_PERMISSION_ONLY",
       "preregistration":str(PLAN.relative_to(ROOT)),
       "canonical_approved_sha256":p["canonical_raw_sha256"],
       "samples_per_physical_variant":samples,
       "variants":counts,
       "conditional_rules":rules,
       "physical_lower_mv_pool":{"count":35,"mv0":7,"mv1":15,"mv2":13},
       "bounds":{
         "paid_abaddon_birgi_ignus_assembly":False,
         "full_cascade_hit_spell_effects_resolved":False,
         "fast_mana_and_tutor_spell_effects_resolved":False,
         "opponent_actions_or_stack_sampling":False,
         "observed_real_deck_cascade_win_rate":None,
         "net_swap_superiority":False,
         "canonical_modified":False,
         "m6_completed":False,
         "m6_certificates":0,
         "m7_owner_approvals":0,
       }
    }


def main():
    a=argparse.ArgumentParser()
    a.add_argument("--samples",type=int,default=None)
    a.add_argument("--out")
    args=a.parse_args()
    result=run(samples=args.samples)
    if args.out:
        Path(args.out).write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    for name,v in result["variants"].items():
        print(name,"T10",json.dumps(v["checkpoints"]["10"],sort_keys=True))
    print("Cascade first-hit opportunity only: no effects, opponents, full-game strength or win rate.")


if __name__=="__main__":
    main()
