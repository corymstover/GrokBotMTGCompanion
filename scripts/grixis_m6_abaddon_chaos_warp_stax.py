#!/usr/bin/env python3
"""Abaddon stax-answer windows + frozen 100-card matched answer access.

Source-bound deterministic rules assertions and land-only source-paid opportunity.
NOT multiplayer game simulation, odds of stax, deck superiority or owner approval.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from grixis_m6_abaddon_assault_access import frozen_source, play_land, LANDS_KNOWN
from grixis_m6_abaddon_chronological_engine import physical_payment

PLAN = ROOT / "data/grixis/m6/phase_b_plans/abaddon_chaos_warp_stax_20261021.json"
STAX = {
    "Rule of Law": {"zone_type":"enchantment","spell_limit":True,"from_exile_block":False},
    "Arcane Laboratory": {"zone_type":"enchantment","spell_limit":True,"from_exile_block":False},
    "Rest in Peace": {"zone_type":"enchantment","spell_limit":False,"from_exile_block":False},
    "Null Rod": {"zone_type":"artifact","spell_limit":False,"from_exile_block":False},
    "Drannith Magistrate": {"zone_type":"creature","spell_limit":False,"from_exile_block":True},
}
COSTS = {"Chaos Warp":(3,(0,0,1)), "Otawara, Soaring City":(4,(1,0,0))}
DISRUPTION_CLASSES = {
    "Chaos Warp":{"kind":"spell","target":"permanent","resolution":"shuffle_reveal"},
    "Otawara, Soaring City":{"kind":"activated_ability","target":"artifact_creature_enchantment_planeswalker","resolution":"bounce"},
    "Swan Song":{"kind":"spell","target":"enchantment_instant_sorcery_on_stack","resolution":"counter"},
    "Force of Negation":{"kind":"spell","target":"noncreature_spell_on_stack","resolution":"counter"},
    "Deadly Rollick":{"kind":"spell","target":"creature_permanent","resolution":"exile"},
    "Pyroblast":{"kind":"spell","target":"blue_spell_or_blue_permanent","resolution":"counter_or_destroy"},
}


def frozen_variants():
    p=json.loads(PLAN.read_text(encoding="utf-8"))
    prior, base = frozen_source()
    if p["source_sha256"] != prior["source_sha256"] or p["approved_raw_sha256"] != prior["canonical_approved_raw_sha256"]:
        raise ValueError("Canonical source or approved hash discrepancy")
    if len(base)!=99 or sum(n in LANDS_KNOWN for n in base)!=34:
        raise ValueError("Wrong physical frozen 99/34 inventory")
    alternatives={}
    for item in p["physical_variants"]:
        cards=list(base)
        if item["cut"]:
            if cards.count(item["cut"])!=1 or item["add"] in cards:
                raise ValueError("Candidate cut not an exact singleton")
            cards[cards.index(item["cut"])] = item["add"]
        from collections import Counter
        counts=Counter(cards+["Abaddon the Despoiler"])
        if sum(counts.values())!=100 or any(q>1 and n not in ("Island","Swamp","Mountain") for n,q in counts.items()):
            raise ValueError("Challenger violates 100-card singleton rule")
        if sum(n in LANDS_KNOWN for n in cards)!=34:
            raise ValueError("Land count changed")
        alternatives[item["id"]]=cards
    if set(alternatives)!={"baseline","warp_for_rakdos","warp_for_lost","warp_for_ruinous"}:
        raise ValueError("Variant coverage drift")
    return p,alternatives


def response_window(stax, answer, *,
                    target_zone="battlefield", spells_already_cast=0,
                    in_hand=True, reveal="different_permanent",
                    spell_limit_already_active=None,
                    abaddon_cascade_enabled=False):
    """Conservative boolean case truth for a single threat and response.

    Fixed legal timing, spell-limit and target-type windows ONLY, not actual
    stack priority/mana/opponent actions. Each answer assumes mana available.
    A channel activation is not a cast and only works with Otawara in hand.
    """
    if stax not in STAX or answer not in DISRUPTION_CLASSES:
        raise ValueError("Unknown verified fixture card")
    if target_zone not in ("battlefield","stack"):
        raise ValueError("Unknown target zone")
    if reveal not in ("different_permanent","same_stax","nonpermanent"):
        raise ValueError("Unregistered Warp reveal case")
    if not isinstance(spells_already_cast,int) or spells_already_cast<0:
        raise ValueError("Invalid spell count")
    if spell_limit_already_active is None:
        limited=target_zone=="battlefield" and STAX[stax]["spell_limit"]
    else:
        limited=bool(spell_limit_already_active)
    typ=STAX[stax]["zone_type"]
    kind=DISRUPTION_CLASSES[answer]["kind"]
    can_cast_or_activate=bool(in_hand) and not (kind=="spell" and limited and spells_already_cast>=1)
    eligible=(target_zone=="battlefield" and (
        answer=="Chaos Warp"
        or answer=="Otawara, Soaring City" and typ in ("artifact","creature","enchantment")
        or answer=="Deadly Rollick" and typ=="creature"
    )) or (target_zone=="stack" and (
        answer=="Swan Song" and typ=="enchantment"
        or answer=="Force of Negation" and typ!="creature"
    ))
    # All registered stax permanents are white or colorless; Pyroblast would
    # have no meaningful effect even if targetable via its conditional clause.
    effective=can_cast_or_activate and eligible
    if answer=="Chaos Warp" and effective and reveal=="same_stax":
        effective=False # A same-restrictor reveal is NOT a reliable out
    cascade_triggered=bool(answer=="Chaos Warp" and can_cast_or_activate
                            and abaddon_cascade_enabled)
    # Cascade trigger resolves before Warp; a second spell cannot be cast while
    # Rule of Law / Arcane Lab exists, even if Warp will later remove it.
    cascade_exiled_spell_cast_legal=(
        cascade_triggered and not (limited and spells_already_cast+1>=1)
        and not STAX[stax]["from_exile_block"]
    )
    stax_removed=effective and target_zone=="battlefield"
    # A counterspell answers the threatened spell before its permanent resolves.
    stax_countered=effective and target_zone=="stack"
    return {
        "answer_action_allowed":can_cast_or_activate,
        "answer_effective":effective,
        "threat_removed_from_battlefield":stax_removed,
        "threat_countered_on_stack":stax_countered,
        "spell_count_after_action":spells_already_cast+int(can_cast_or_activate and kind=="spell"),
        "cascade_triggered_on_chaos_warp":cascade_triggered,
        "cascade_exiled_spell_cast_legal_before_warp_resolves":cascade_exiled_spell_cast_legal,
        "already_exiled_graveyard_restored":False,
        "target_was_shuffled_then_random_replacement":answer=="Chaos Warp" and can_cast_or_activate and eligible,
        "threat_can_be_recast_if_bounced":answer=="Otawara, Soaring City" and effective,
        "multiplayer_win_rate":None,
    }


def available_hand_answer(landfield,hand,answer):
    if answer not in COSTS:
        raise ValueError("Invalid answer-cost fixture")
    if answer not in hand:
        return False
    # Otawara is a channel from HAND only. Do not count a land on battlefield.
    # Conservative: ZERO legendary creatures to discount {3}{U}.
    return physical_payment(landfield,(0,0,0,0),answer,
                            source_cost_override=COSTS[answer]) is not None


def trial(cards, seed,checkpoints):
    deck=list(cards)
    if len(deck)!=99:
        raise ValueError("Physical library count wrong")
    random.Random(seed).shuffle(deck)
    hand,deck=deck[:7],deck[7:]
    lands=[]
    result={}
    searches=0
    for turn in range(1,max(checkpoints)+1):
        lands=[(n,False) for n,_ in lands]
        hand.append(deck.pop(0))
        n,_=play_land(hand,deck,lands,seed,turn)
        searches+=n
        if turn not in checkpoints:
            continue
        warp_held="Chaos Warp" in hand
        channel_held="Otawara, Soaring City" in hand
        warp_payable=available_hand_answer(lands,hand,"Chaos Warp")
        channel_payable=available_hand_answer(lands,hand,"Otawara, Soaring City")
        result[turn]={
            "chaos_warp_held":warp_held,
            "chaos_warp_land_payable_as_first_spell":warp_payable,
            "otawara_channel_held":channel_held,
            "otawara_channel_land_payable":channel_payable,
            "at_least_one_payable_answer":warp_payable or channel_payable,
            "no_answer_held":not warp_held and not channel_held,
        }
    return result,searches


def run():
    plan,variants=frozen_variants()
    checks=plan["matched_draw_source_opportunity"]["checkpoints"]
    n=plan["matched_draw_source_opportunity"]["n_per_variant"]
    seen={name:{str(t):Counter() for t in checks} for name in variants}
    searches=Counter()
    for i in range(n):
        seed=plan["matched_draw_source_opportunity"]["seed"]+i*104729
        for name,cards in variants.items():
            r,s=trial(cards,seed,checks)
            searches[name]+=s
            for t,row in r.items():
                for key,value in row.items():
                    seen[name][str(t)][key]+=int(value)
    rules={
        "rol_warp_first_spell":response_window("Rule of Law","Chaos Warp"),
        "rol_warp_after_one_spell":response_window("Rule of Law","Chaos Warp",spells_already_cast=1),
        "rol_otawara_after_one_spell":response_window("Rule of Law","Otawara, Soaring City",spells_already_cast=1),
        "rol_warp_while_abaddon_cascade_enabled":response_window("Rule of Law","Chaos Warp",abaddon_cascade_enabled=True),
        "rol_warp_reveals_original_rule_again":response_window("Rule of Law","Chaos Warp",reveal="same_stax"),
        "rol_swan_song_before_resolution":response_window("Rule of Law","Swan Song",target_zone="stack"),
        "rol_swan_song_after_resolution":response_window("Rule of Law","Swan Song",target_zone="battlefield"),
        "rip_warp_after_exiling_grave":response_window("Rest in Peace","Chaos Warp"),
        "null_rod_warp_resolved":response_window("Null Rod","Chaos Warp"),
        "magistrate_deadly_rollick":response_window("Drannith Magistrate","Deadly Rollick"),
        "rol_pyroblast_resolved":response_window("Rule of Law","Pyroblast"),
    }
    return {
        "schema_version":1,
        "test_class":"frozen_physical_draw_land_source_opportunity_plus_deterministic_stax_counterfactuals",
        "preregistration":str(PLAN.relative_to(ROOT)),
        "approved_raw_sha256":plan["approved_raw_sha256"],
        "n_per_variant":n,
        "seed":plan["matched_draw_source_opportunity"]["seed"],
        "checkpoints":checks,
        "physical_variants":{name:{t:dict(sorted(counts.items())) for t,counts in turn.items()}
                             for name,turn in seen.items()},
        "search_shuffles":dict(searches),
        "scenario_outcomes":rules,
        "source_verified_errata":{
            "The Lost and the Damned":{"mana_cost":"{1}{U}{R}","mana_value":3,"baseline_cut_value_not_scored_zero":True},
            "The Ruinous Powers":{"mana_cost":"{2}{B}{R}","mana_value":4,"baseline_cut_value_not_scored_zero":True}},
        "limitations":{
            "opponent_stax_incidence_modeled":False,
            "has_actual_cast_spells":False,
            "has_actual_channel_activations":False,
            "effect_of_removed_incumbent_modeled":False,
            "stax_reveal_replacement_randomness_modeled":False,
            "actual_multiplayer_win_rate":None,
            "candidate_superiority_proven":False,
            "canonical_changed":False,
            "M6_6_complete":False,"M6_certificates":0,"M7_approved_decks":0,
        },
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out")
    args=parser.parse_args()
    d=run()
    if args.out:
        Path(args.out).write_text(json.dumps(d,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    for name,rec in d["physical_variants"].items():
        print(name, "T10", json.dumps(rec["10"],sort_keys=True))
    print("Neither metagame stax frequency nor deck win rates were measured.")
if __name__=="__main__":
    main()
