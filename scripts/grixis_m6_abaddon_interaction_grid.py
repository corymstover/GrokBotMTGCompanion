#!/usr/bin/env python3
"""Cycle 93: bounded, explicit adversarial response-window grid for Abaddon.

A small conditional rules harness, not a stack simulator, randomized opponent
model, paired win-rate experiment, final Pass C verdict, or commander approval.
Mechanics reference current Oracle/Wizards release notes and CR 113.7a.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
PRIOR=ROOT/"data/grixis/m6/phase_b_plans/abaddon_priority_01.json"
PAIRED=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_threshold_access_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_interaction_grid_01.json"
AUTH={"can_decide":False,"can_apply_swap":False,"can_approve_or_lock":False}

def read(x):return json.loads(x.read_text(encoding="utf-8"))
def sha(x):return "sha256:"+hashlib.sha256(x.read_bytes()).hexdigest()
def enc(x):return json.dumps(x,indent=1,ensure_ascii=False,sort_keys=True)+"\n"

def active_tap_cast(turn_cast,turn_of_activation,haste=False,source_survived=True):
    return source_survived and (turn_of_activation>turn_cast or
        (haste and turn_of_activation==turn_cast))

def tree(life=40,toughness=13,source_removed_before_resolution=False,target_legal=True,
         bloodletter=False,solphim=False):
    # CR exchange needs TWO values still existing; special card ruling overrides
    # generic last-known information in case Tree leaves before resolution.
    if source_removed_before_resolution or not target_legal:
        return {"target_before":life,"target_after":life,"life_lost":0,"life_gained":0,
                "damage":0,"exchanged":False,"source_fails_in_response":source_removed_before_resolution}
    change=life-toughness
    lost=max(0,change)*(2 if bloodletter else 1)
    gained=max(0,-change)
    return {"target_before":life,"target_after":life-lost if change>=0 else life+gained,
            "life_lost":lost,"life_gained":gained,"damage":0,"exchanged":True,
            "source_fails_in_response":False}

def heartless(opp=(40,39,31),pilot=40,activated=True,
             source_removed_before_resolution=False,solphim=False,
             solphim_removed_before_resolution=False,bloodletter=False,
             bloodletter_removed_before_resolution=False,prevent_opponents=()):
    # After activation, source destruction does not remove its ability from stack.
    # If Solphim/Bloodletter leave before resolution, their replacements don't apply.
    # Prevention applies to DAMAGE, before Bloodletter changes the life lost.
    if not activated:
        return {"opponents":[{"life_before":x,"damage":0,"life_lost":0,"life_after":x}
                              for x in opp],"pilot_damage":0,"pilot_after":pilot,
                "ability_resolved":False,"source_removed_after_activation":source_removed_before_resolution,
                "total_opponent_life_lost":0}
    multiplied_damage=solphim and not solphim_removed_before_resolution
    multiplied_loss=bloodletter and not bloodletter_removed_before_resolution
    rows=[]
    for i,life in enumerate(opp):
        normal=life//2
        damage=(normal*(2 if multiplied_damage else 1)) if i not in prevent_opponents else 0
        life_lost=damage*(2 if multiplied_loss else 1)
        rows.append({"life_before":life,"damage":damage,"life_lost":life_lost,
                     "life_after":life-life_lost})
    self_damage=pilot//2
    return {"opponents":rows,"pilot_damage":self_damage,"pilot_after":pilot-self_damage,
            "ability_resolved":True,"source_removed_after_activation":source_removed_before_resolution,
            "total_opponent_life_lost":sum(x["life_lost"] for x in rows)}

def hand_cascade(opp_lost,mv=5,origin="hand",own_turn=True,commander=True):
    return bool(own_turn and commander and origin=="hand" and opp_lost>=mv)

def mana_followup(available_now,abaddon_already_on_field,spell_mv=3):
    # Restrictive nominal cost illustration: not claiming available mana
    # can pay required colors, free alternative costs or mana-generation effects.
    requirement=spell_mv+(0 if abaddon_already_on_field else 5)
    return {"nominal_total_mana":available_now,
            "required_nominal_mana":requirement,
            "nominal_budget_sufficient":available_now>=requirement,
            "colored_pips_checked":False,
            "hand_spell_available_checked":False}

def make():
    source=SOURCE.read_text(encoding="utf-8")
    if "1 Abaddon the Despoiler [Commander]" not in source or "1 Kessig Flamebreather" not in source:
        raise ValueError("canonical source drift")
    plan=read(PRIOR); paired=read(PAIRED)
    if plan["base_hash"]!=paired["canonical_hash"] or paired["full_phase_b_complete"]:
        raise ValueError("incorrect accepted deck or prematurely complete evidence")
    examples={
        "tree_same_turn_without_haste_active":active_tap_cast(4,4,False,True),
        "tree_first_next_turn_active":active_tap_cast(4,5,False,True),
        "tree_removed_before_first_untap_active":active_tap_cast(4,5,False,False),
        "heartless_same_turn_without_haste_active":active_tap_cast(5,5,False,True),
        "heartless_first_next_turn_active":active_tap_cast(5,6,False,True),
        "tree_40_unmodified":tree(),
        "tree_40_removed_after_activation":tree(source_removed_before_resolution=True),
        "tree_40_illegal_target":tree(target_legal=False),
        "tree_40_bloodletter":tree(bloodletter=True),
        "tree_40_solphim":tree(solphim=True),
        "tree_40_low_toughness_4":tree(toughness=4),
        "tree_opponent_at_8_life":tree(life=8),
        "heartless_40_39_31_base":heartless(),
        "heartless_source_removed_after_activation":heartless(source_removed_before_resolution=True),
        "heartless_40_39_31_solphim":heartless(solphim=True),
        "heartless_solphim_removed_in_response":heartless(solphim=True,solphim_removed_before_resolution=True),
        "heartless_40_39_31_bloodletter":heartless(bloodletter=True),
        "heartless_bloodletter_removed_in_response":heartless(bloodletter=True,bloodletter_removed_before_resolution=True),
        "heartless_both_multipliers":heartless(solphim=True,bloodletter=True),
        "heartless_one_opponent_prevents_damage":heartless(solphim=True,bloodletter=True,prevent_opponents=(0,)),
        "heartless_all_opponents_prevent_damage":heartless(solphim=True,bloodletter=True,prevent_opponents=(0,1,2)),
        "heartless_no_legal_activation":heartless(activated=False),
        "tree_followup_hand_cascade_after_27_lost":hand_cascade(27),
        "tree_followup_graveyard_not_eligible":hand_cascade(27,origin="graveyard"),
        "tree_followup_other_players_turn_not_eligible":hand_cascade(27,own_turn=False),
        "tree_five_mana_new_abaddon_no_mana_left_for_mv3":{"example":mana_followup(5,False,3)},
        "tree_eight_mana_new_abaddon_and_mv3":{"example":mana_followup(8,False,3)},
        "tree_mana_if_commander_preexisting_and_3_available":{"example":mana_followup(3,True,3)},
        "cascade_reset_next_turn":hand_cascade(0),
    }
    assert not examples["tree_same_turn_without_haste_active"]
    assert examples["tree_first_next_turn_active"]
    assert not examples["heartless_same_turn_without_haste_active"]
    assert examples["heartless_first_next_turn_active"]
    assert examples["tree_40_unmodified"]["life_lost"]==27
    assert examples["tree_40_bloodletter"]["life_lost"]==54
    assert examples["tree_40_solphim"]["life_lost"]==27
    assert examples["tree_40_low_toughness_4"]["life_lost"]==36
    assert examples["tree_40_removed_after_activation"]["life_lost"]==0
    assert examples["heartless_source_removed_after_activation"]["total_opponent_life_lost"]==54
    assert examples["heartless_40_39_31_base"]["total_opponent_life_lost"]==54
    assert examples["heartless_40_39_31_solphim"]["total_opponent_life_lost"]==108
    assert examples["heartless_solphim_removed_in_response"]["total_opponent_life_lost"]==54
    assert examples["heartless_40_39_31_bloodletter"]["total_opponent_life_lost"]==108
    assert examples["heartless_bloodletter_removed_in_response"]["total_opponent_life_lost"]==54
    assert examples["heartless_both_multipliers"]["total_opponent_life_lost"]==216
    assert examples["heartless_all_opponents_prevent_damage"]["total_opponent_life_lost"]==0
    assert examples["heartless_all_opponents_prevent_damage"]["pilot_after"]==20
    assert not examples["tree_followup_graveyard_not_eligible"]
    assert not examples["cascade_reset_next_turn"]
    return {"schema_version":1,"stage":"M6_Abaddon_bounded_opponent_response_and_turn_timing",
        "source_baseline_sha256":sha(SOURCE),"preregistered_plan_sha256":sha(PRIOR),
        "paired_mana_only_sha256":sha(PAIRED),
        "deck_id":plan["deck_id"],"slug":plan["slug"],"canonical_hash":plan["base_hash"],
        "examples":examples,
        "sourced_rules":[
          "https://magic.wizards.com/en/news/feature/eldritch-moon-release-notes-2016-07-08",
          "https://mtg.wtf/help/rules#113.7a",
          "https://magic.wizards.com/en/news/feature/the-lost-caverns-of-ixalan-release-notes",
          "https://mtg.wtf/card/cmm/539/Heartless-Hidetsugu",
          "https://mtg.wtf/card/40k/171/Abaddon-the-Despoiler"
        ],
        "sensitivity_dimensions":[
          "Tree must be on battlefield when exchange resolves; removal counters its effect",
          "Heartless activated damage ability persists even if source leaves; Solphim/Bloodletter replacements require those permanents present at resolution",
          "A same-turn tap activation requires haste or prior-turn control; neither proposed creature has intrinsic haste",
          "Damage prevention blocks Heartless life-loss; Tree life exchange is non-damage and ignores Solphim",
          "Heartless damages controller, Tree normally does not; multiplayer victims versus one Tree target",
          "Cascade is hand-cast, during controller turn, commander-present and life-loss threshold at casting time",
          "Nominal follow-through requires mana after Abaddon cast and sufficient colored pips; resources not modeled here"
        ],
        "limitations":[
          "Manually encoded finite cases, NOT a comprehensive Magic rules engine or Phase-B multiplayer simulator",
          "Assumes abilities are legally activated and on stack when labeled; omitted mana/targeting/protection other than explicit case",
          "Does not assign probabilities to opponents responding, source surviving, haste, or prevention",
          "Does not estimate actual win rate or likelihood of drawing cards together",
          "Earlier 600-seed mana comparisons still ignore both added and removed abilities",
          "Named final Pass C, complete J bundles and explicit user approval still required"
        ],
        "phase_b_complete":False,"supports_improvement_claim":False,"authority":AUTH}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--build",action="store_true");ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    if not(args.build or args.check):ap.error("require --build or --check")
    d=make();text=enc(d)
    if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(text,encoding="utf-8")
    if args.check and (not OUT.is_file() or OUT.read_text(encoding="utf-8")!=text):raise ValueError("response grid drift")
    print("Abaddon Cycle 93",len(d["examples"]),"conditional response/turn cases; zero full Phase-B or swap authority")
if __name__=="__main__":main()
