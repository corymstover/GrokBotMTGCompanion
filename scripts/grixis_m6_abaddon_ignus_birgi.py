#!/usr/bin/env python3
"""Grinning Ignus + Birgi + Abaddon bounded, pre-registered source review.

No deck edits, multiplayer play or win-rate inference. The arithmetic models
only {R} Ignus bounce / {C}{C}{R} return, {2}{R} cast, Birgi {R} trigger;
Nightscape Familiar's one-generic reduction is a separate board assumption.
Cascade is a grant/trigger eligibility count, not real library resolution.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT / "scripts"))
from grixis_m6_abaddon_assault_access import frozen_source, LANDS_KNOWN

PLAN = ROOT / "data/grixis/m6/phase_b_plans/abaddon_ignus_birgi_20261021.json"


def source_inventory():
    p=json.loads(PLAN.read_text(encoding="utf-8"))
    raw=(ROOT/p["frozen_source_path"]).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=p["frozen_source_sha256"]:
        raise ValueError("Frozen source changed")
    prior,main=frozen_source()
    if prior["canonical_approved_raw_sha256"]!=p["canonical_approved_raw_sha256"]:
        raise ValueError("Canonical approved checksum mismatch")
    if len(main)!=99 or len(main)+1!=100:
        raise ValueError("Wrong physical inventory")
    if main.count("Birgi, God of Storytelling // Harnfel, Horn of Bounty")!=1:
        raise ValueError("Birgi double face absent in baseline")
    if "Grinning Ignus" in main:
        raise ValueError("Challenger already in canonical library")
    if any(main.count(name)!=1 for name in p["existing_support"] if name!="Abaddon the Despoiler"):
        raise ValueError("Physical baseline support drift")
    variants={}
    for variant in p["physical_variants"]:
        cards=list(main)
        if variant["cut"]:
            if cards.count(variant["cut"])!=1 or cards.count(variant["add"])!=0:
                raise ValueError("Bad one-card cut or add")
            cards[cards.index(variant["cut"])]=variant["add"]
        cnt=Counter(cards+["Abaddon the Despoiler"])
        if sum(cnt.values())!=100 or sum(n in LANDS_KNOWN for n in cards)!=34:
            raise ValueError("Wrong physical 100 or 34 lands")
        if {n for n,v in cnt.items() if v>1}!={"Island","Mountain","Swamp"}:
            raise ValueError("Singleton violation")
        variants[variant["id"]]=cards
    if len(variants)!=4:
        raise ValueError("Incomplete candidate cut variants")
    packet=json.loads((ROOT/p["candidate_packet"]).read_text(encoding="utf-8"))
    cards={x["add"] for x in packet["items"]}
    if (len(packet["items"])!=p["packet_expected"]["swap_records"] or
        len(cards)!=p["packet_expected"]["unique_candidate_cards"] or
        "Grinning Ignus" not in cards):
        raise ValueError("Screened candidate inventory drift")
    return p,variants,packet


def ignus_cycle(*, iterations=5, birgi_front=True,
                abaddon_controlled=True, opponent_life_lost=3,
                ignus_from_hand=True, rule_of_law=False,
                initial_red=1, familiar=False,
                lost_present=False):
    """Finite constructibility witness starting with Ignus already on battlefield.

    One Ignus bounce activation and recast for each counted iteration; Birgi
    refill is one red per cast. The bounced Ignus enters hand on each loop.
    A currently active Rule of Law permits only the first recast if no spell
    was cast earlier that turn. No pre-main permissions or opponents simulated.
    """
    if iterations<0 or opponent_life_lost<0 or initial_red<0:
        raise ValueError("Impossible fixture state")
    if not ignus_from_hand:
        # From outside the hand there is no repeatable bounce-to-same-zone
        # recast loop. A single exile cast still has Birgi/Lost triggers.
        return {"recasts":0,"abaddon_cascade_triggers":0,
                "birgi_red_triggers":int(birgi_front),
                "lost_spawn_triggers":int(lost_present),
                "mana_pool_red":initial_red,"mana_pool_colorless":0,
                "can_continue":False,"stopped_reason":"outside_hand_is_not_recursive_hand_loop",
                "proves_multiplayer_win":False}
    red=initial_red
    colorless=0
    casts=0
    cascades=0
    birgi_triggers=0
    reason="iteration_bound_reached"
    for _ in range(iterations):
        if rule_of_law and casts>=1:
            reason="rule_of_law_spell_limit"
            break
        if red<1:
            reason="ignus_bounce_requires_red"
            break
        # Cost: {R}, returning Ignus to hand; ability is a mana ability with
        # sorcery timing. Adds precisely {C}{C}{R} to the pool.
        red-=1
        colorless+=2
        red+=1
        generic_needed=1 if familiar else 2
        if colorless<generic_needed or red<1:
            raise AssertionError("Precommitted loop has impossible mana state")
        colorless-=generic_needed
        red-=1
        casts+=1
        if abaddon_controlled and opponent_life_lost>=3:
            cascades+=1
        if birgi_front:
            red+=1
            birgi_triggers+=1
        # Recast hand spell does NOT trigger Lost; cascade exile CAST may do
        # so, but hits and cast choices are NOT modeled here.
    can_continue=bool(not rule_of_law and red>=1)
    return {"recasts":casts,"abaddon_cascade_triggers":cascades,
            "birgi_red_triggers":birgi_triggers,
            "lost_spawn_triggers":0,"mana_pool_red":red,
            "mana_pool_colorless":colorless,"can_continue":can_continue,
            "stopped_reason":reason,"proves_multiplayer_win":False}


def stormfist_upkeep(*, opponents=3, active=True):
    if opponents<1:
        raise ValueError("Need an opponent")
    return {"opponent_life_lost":opponents if active else 0,
            "opponent_cards_drawn":opponents if active else 0,
            "controller_cards_drawn":1 if active else 0,
            "controller_life_lost":1 if active else 0,
            "enough_for_ignus_mv3_abaddon_cascade":bool(active and opponents>=3),
            "cannot_be_treated_as_free_threshold":True}


def run():
    p,variants,packet=source_inventory()
    cases={
        "neutral_birgi_ignus_with_abaddon_and_3_opponent_loss":ignus_cycle(),
        "abaddon_below_three_loss":ignus_cycle(opponent_life_lost=2),
        "commander_not_present":ignus_cycle(abaddon_controlled=False),
        "birgi_absent":ignus_cycle(birgi_front=False),
        "nightscape_present":ignus_cycle(familiar=True),
        "rule_of_law_present":ignus_cycle(rule_of_law=True),
        "exile_spell_not_recursive_hand_cast":ignus_cycle(ignus_from_hand=False,lost_present=True),
        "harnfel_back_face_not_birgi_front":ignus_cycle(birgi_front=False),
    }
    return {"schema_version":1,"stage":"M6_BOUNDED_RULE_AND_MANA_WITNESS_ONLY",
            "canonical_approved_sha256":p["canonical_approved_raw_sha256"],
            "physical_variants":{k:{"physical_library_cards":len(v),
                "creature_ignus_in_library":v.count("Grinning Ignus"),
                "birgi_double_face_retained":v.count("Birgi, God of Storytelling // Harnfel, Horn of Bounty")==1}
                for k,v in variants.items()},
            "candidate_source_inventory":{"screened_swap_records":len(packet["items"]),
                "distinct_added_names":len({x["add"] for x in packet["items"]})},
            "finite_conditional_traces":cases,
            "stormfist_upkeep_three_opponents":stormfist_upkeep(),
            "evidence_bounds":{"commander_first_repeated_cascade_if_3_life_lost":True,
                "actual_cascade_cards_cast_from_library":False,
                "physical_100_card_gameplay_modeled":False,
                "real_opening_hand_probability_measured":False,
                "net_improving_swap_proven":False,
                "true_multiplayer_win_rate":None,
                "formal_M6_certificates":0,
                "M7_approved_decks":0,
                "canonical_changed":False}}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out")
    arg=parser.parse_args()
    record=run()
    if arg.out:
        Path(arg.out).write_text(json.dumps(record,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    for name,row in record["finite_conditional_traces"].items():
        print(name, row)
    print("Rules witnesses, NOT game simulations or approval of any Ignus swap")


if __name__=="__main__":
    main()
