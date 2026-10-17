#!/usr/bin/env python3
"""Abaddon Cycle 83: bounded effect-aware Phase-B mechanics checks.

These exact deterministic scenarios do NOT estimate deck win rate, paired
commander optimization, or a complete executable combo. Source assumptions are
explicit and no result can authorize a card swap or approval.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_priority_01.json"
PACKET=ROOT/"data/grixis/m6/review_packets/abaddon-the-despoiler.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_01.json"
AUTH={"can_decide":False,"can_apply_swap":False,"can_approve_or_lock":False}
LIMITS=[
    "Exact conditional rules calculations only; no opponent-policy sampling or deck win-rate claim",
    "Does not simulate current 100-card mana curve, mulligans, real draw, combat blockers, priority, or opponent responses",
    "Every tapped ability assumes its source survived until legally usable; no haste supplied",
    "Grinding Station loop is limited by library/graveyard resources and has no demonstrated winner",
    "Follow-up Abaddon spells require commander present, hand origin, sufficient mana and a surviving game",
    "Phase-B completion requires independent current Oracle, full combo/resource audit, paired tests, colored-mana study and named Pass C judgment"
]


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def encode(o):
    return json.dumps(o,indent=1,ensure_ascii=False,sort_keys=True)+"\n"


def sha(path):
    return "sha256:"+hashlib.sha256(path.read_bytes()).hexdigest()


def cascade(mv,loss,origin="hand",your_turn=True,abaddon=True):
    return bool(abaddon and your_turn and origin=="hand" and mv>=0 and loss>=mv)


def tree(life,toughness,active=True,bloodletter=False):
    if not active:
        return {"resolved":False,"life_after":life,"life_lost":0,"damage":0}
    base=max(0,life-toughness)
    lost=base*(2 if bloodletter else 1)
    return {"resolved":True,"life_before":life,"toughness_before":toughness,
            "life_after":life-lost if life>=toughness else toughness,
            "life_lost":lost if life>=toughness else 0,
            "life_gained":max(0,toughness-life),"damage":0}


def heartless(lives=(40,39,31),pilot=40,solphim=False,bloodletter=False):
    opponents=[]
    for life in lives:
        damage=(life//2)*(2 if solphim else 1)
        loss=damage*(2 if bloodletter else 1)
        opponents.append({"life_before":life,"damage":damage,"life_lost":loss,
                          "life_after":life-loss,"defeated_after_SBA":life-loss<=0})
    self_damage=pilot//2
    return {"opponents":opponents,"pilot_damage":self_damage,
            "pilot_life_after":pilot-self_damage,
            "life_lost_to_opponents_in_damage_event":sum(o["life_lost"] for o in opponents)}


def kessig(spell_count,opponent_count=3):
    # Flamebreather triggers as each noncreature spell is CAST; its damage
    # cannot retroactively affect Abaddon's X for that same spell's casting.
    return {"first_spell_threshold_at_cast":0,
            "threshold_after_first_trigger":opponent_count,
            "threshold_after_all_triggers":spell_count*opponent_count}


def shredder(connect=(True,True,True),opponent_life=40):
    results=[]
    for hit in connect:
        # One original Shredder is declared attacking; two copies ENTER attacking,
        # so they DO NOT create further attack triggers.
        remaining=opponent_life-5 if hit else opponent_life
        later_loss=(remaining+1)//2 if hit and remaining>0 else 0
        results.append({"connect":hit,"damage":5 if hit else 0,
                        "triggered_life_loss":later_loss,
                        "total_life_lost":(5+later_loss) if hit else 0})
    return {"copies":max(0,len(connect)-1),"attack_triggers":1,
            "per_opponent":results,
            "table_life_lost":sum(x["total_life_lost"] for x in results)}


def station_loop(library_cards,other_graveyard_cards=0):
    # A single free artifact is sacrificed to tapped Grinding Station;
    # milling 3 replaces the 3 OTHER graveyard cards exiled to escape the
    # artifact; its entry untaps Station. This is NOT infinite.
    if library_cards<0 or other_graveyard_cards<0:
        raise ValueError("negative resource")
    cycles=0
    while library_cards>=3 and other_graveyard_cards>=0:
        library_cards-=3
        other_graveyard_cards+=3
        other_graveyard_cards-=3
        cycles+=1
    return {"completed_cycles":cycles,"remaining_library":library_cards,
            "net_mana_produced":0,"winner_proven":False,
            "repeatable_infinite":False,
            "requires_free_recastable_artifact":True,
            "requires_underworld_breach_and_station_untap":True}


def result():
    p=load(PLAN)
    packet=load(PACKET)
    swaps={x["swap_id"]:x for x in packet["items"]}
    ids=[sid for group in p["groups"] for sid in group["swap_ids"]]
    if (len(ids)!=7 or len(set(ids))!=7 or any(s not in swaps for s in ids)
            or p["base_hash"]!=packet["list_hash"]):
        raise ValueError("unregistered swap or baseline drift")
    a=heartless()
    b=heartless(solphim=True)
    blood=heartless(bloodletter=True)
    hypothetical=shredder()
    blocking=shredder((True,False,False))
    scenarios={
       "tree_life40_toughness13":tree(40,13),
       "tree_target_below_toughness":tree(8,13),
       "tree_removed_in_response":tree(40,13,active=False),
       "tree_bloodletter_life40":tree(40,13,bloodletter=True),
       "tree_followup_hand_mv5":cascade(5,27),
       "tree_followup_exile_mv5":cascade(5,27,origin="exile"),
       "tree_commander_absent_mv5":cascade(5,27,abaddon=False),
       "heartless_base":a,
       "heartless_with_solphim":b,
       "heartless_with_bloodletter":blood,
       "kessig_two_noncreature_spells":kessig(2),
       "shredder_all_three_connect":hypothetical,
       "shredder_one_connect":blocking,
       "grinding_station_free_artifact_90_library":station_loop(90),
       "grinding_station_free_artifact_2_library":station_loop(2),
       "cascade_resets_next_turn":cascade(5,0),
       "cascade_from_graveyard_after_large_loss":cascade(5,60,origin="graveyard"),
    }
    return {
      "schema_version":1,"stage":"M6_partial_bounded_mechanics",
      "deck_id":p["deck_id"],"slug":p["slug"],"base_hash":p["base_hash"],
      "preregistered_plan_sha256":sha(PLAN),"accepted_packet_sha256":sha(PACKET),
      "covered_swap_ids":ids,"covered_candidate_groups":[g["candidate"] for g in p["groups"]],
      "oracle_and_rules_refs":[
        "https://media.wizards.com/2024/downloads/INR_Release_Notes_hzvmSd7KJG/EN_MTGINR_ReleaseNotes_20240903.pdf",
        "https://media.wizards.com/2026/downloads/TMT_Release_Notes_eM8Yplm3UV/u17aHk8iV1_EN_MTGTMT_ReleaseNotes_20251001.pdf",
        "https://mtg.wtf/card/cmm/539/Heartless-Hidetsugu",
        "https://mtg.wtf/card/lci/92/Bloodletter-of-Aclazotz",
        "https://commanderspellbook.com/combo/1368-1414-4856/"
      ],
      "assumptions":[
        "Effects successfully resolve except explicit removal scenario; no prevention/replacement except named Solphim/Bloodletter",
        "Heartless values use floor(life/2) damage and double opponent noncombat damage with Solphim",
        "Bloodletter doubles life lost by opponent on your turn; its effect does not double damage",
        "Tree life exchange uses current unmodified toughness, includes life gain when life lower, and deals zero damage",
        "Shredder's original 5/5 and two nonlegendary token copies are assumed to have 5 power; tokens enter attacking without new attack triggers",
        "The artifact in Grinding Station scenario is free to escape, and sufficient other graveyard cards are milled in each iteration"
      ],
      "scenarios":scenarios,"limitations":LIMITS,
      "metrics":{"candidate_groups_examined":4,"swap_ids_addressed":7,
                 "bounded_scenario_checks":len(scenarios),
                 "effect_aware_deckwide_paired_tests":0,
                 "complete_phase_b_candidate_groups":0,
                 "approved_swaps":0},
      "status":"partial_rules_evidence_only",
      "phase_b_complete":False,
      "supports_improvement_claim":False,
      "authority":AUTH
    }


def check_result(data):
    d=data["scenarios"]
    assert d["tree_life40_toughness13"]["life_lost"]==27
    assert d["tree_life40_toughness13"]["damage"]==0
    assert d["tree_bloodletter_life40"]["life_lost"]==54
    assert d["tree_target_below_toughness"]["life_gained"]==5
    assert d["heartless_base"]["pilot_life_after"]==20
    assert [x["life_after"] for x in d["heartless_with_solphim"]["opponents"]]==[0,1,1]
    assert d["heartless_with_bloodletter"]["opponents"][0]["damage"]==20
    assert d["heartless_with_bloodletter"]["opponents"][0]["life_lost"]==40
    assert d["kessig_two_noncreature_spells"]["threshold_after_first_trigger"]==3
    assert d["kessig_two_noncreature_spells"]["threshold_after_all_triggers"]==6
    assert d["shredder_all_three_connect"]["table_life_lost"]==69
    assert d["shredder_one_connect"]["table_life_lost"]==23
    assert d["grinding_station_free_artifact_90_library"]["completed_cycles"]==30
    assert d["grinding_station_free_artifact_90_library"]["winner_proven"] is False
    for x in ("tree_followup_exile_mv5","tree_commander_absent_mv5","cascade_resets_next_turn",
              "cascade_from_graveyard_after_large_loss"):
        assert d[x] is False
    assert d["tree_followup_hand_mv5"] is True
    assert data["phase_b_complete"] is False and data["supports_improvement_claim"] is False
    assert not any(data["authority"].values())


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--build",action="store_true")
    parser.add_argument("--check",action="store_true")
    a=parser.parse_args()
    if not(a.build or a.check):parser.error("require --build/--check")
    data=result()
    check_result(data)
    if a.build:
        OUT.parent.mkdir(parents=True,exist_ok=True)
        OUT.write_text(encode(data),encoding="utf-8")
    if a.check and (not OUT.is_file() or OUT.read_text(encoding="utf-8")!=encode(data)):
        raise ValueError("bounded Phase-B record missing/stale")
    print("ABADDON BOUNDED PHASE-B",data["metrics"],": pass; zero improvement or approval claims")


if __name__=="__main__":main()
