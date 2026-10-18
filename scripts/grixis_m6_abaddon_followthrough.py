#!/usr/bin/env python3
"""Cycle 94: conditional Abaddon follow-through. NOT a win-rate simulator."""
from __future__ import annotations
import argparse,hashlib,itertools,json
from pathlib import Path
from grixis_m6_abaddon_interaction_grid import active_tap_cast,heartless,tree
ROOT=Path(__file__).resolve().parents[1]
PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_followthrough_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
PRIOR=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_interaction_grid_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_followthrough_01.json"
AUTH={"can_decide":False,"can_apply_swap":False,"can_change_canonical_list":False,"can_approve_or_lock":False}

def read(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def enc(d):return json.dumps(d,indent=2,sort_keys=True,ensure_ascii=False)+"\n"

def legal_payments(pool,cost):
    """Enumerate all legal colored+generic payments; NO abilities, reducers or taxes."""
    remaining={c:int(pool.get(c,0)) for c in "UBRC"}
    for c in "UBR":
        n=int(cost.get(c,0))
        if remaining[c]<n:return []
        remaining[c]-=n
    options=[]
    for amounts in itertools.product(*(range(remaining[c]+1) for c in "CUBR")):
        if sum(amounts)!=int(cost.get("generic",0)):continue
        paid=dict(remaining)
        for c,n in zip("CUBR",amounts):paid[c]-=n
        options.append(paid)
    return options

def followup_after_commander(pool,already_present,commander_cost,followup_cost):
    possibilities=[dict(pool)] if already_present else legal_payments(pool,commander_cost)
    return any(legal_payments(p,followup_cost) for p in possibilities)

def cascade_triggers(card,lost,origin="hand",own_turn=True,commander=True):
    """Counts cascade abilities at cast only; does not resolve spells or hits."""
    printed=int(card=="Bituminous Blast")
    mv={"Bituminous Blast":5,"followup_mv3":3}.get(card,99)
    granted=int(bool(commander and own_turn and origin=="hand" and lost>=mv))
    return {"printed":printed,"granted_by_abaddon":granted,"total_on_cast":printed+granted}

def board_result(board,opponents,pilot):
    active=active_tap_cast(board["turn_cast"],board["activation_turn"],board["haste"],board["source_survives"])
    if not active:return {"activation_legal":False,"total_opponent_life_lost":0,"pilot_damage":0,"opponents_defeated":0,"game_continues":True}
    removed=board.get("response_remove_source",False)
    if board["source"]=="Heartless Hidetsugu":
        r=heartless(opp=tuple(opponents),pilot=pilot,source_removed_before_resolution=removed)
        n=sum(x["life_after"]<=0 for x in r["opponents"])
        return {"activation_legal":True,"total_opponent_life_lost":r["total_opponent_life_lost"],
                "pilot_damage":r["pilot_damage"],"opponents_defeated":n,"game_continues":n<len(opponents)}
    if board["source"]=="Tree of Perdition":
        r=tree(life=opponents[0],source_removed_before_resolution=removed)
        n=int(r["target_after"]<=0)
        return {"activation_legal":True,"exchange_resolved":r["exchanged"],
                "total_opponent_life_lost":r["life_lost"],"pilot_damage":0,
                "opponents_defeated":n,"game_continues":n<len(opponents)}
    raise ValueError("Unregistered source")

def run():
    p,prior=read(PLAN),read(PRIOR)
    if (p["cycle"]!=94 or p["status"]!="registered_before_test" or p["authority"]!=AUTH or
        any(prior["authority"].values()) or prior["phase_b_complete"] or prior["supports_improvement_claim"]):
        raise ValueError("Preregistration/authority drift")
    if sha(SOURCE)!=p["baseline_sha256"] or "1 Abaddon the Despoiler [Commander]" not in SOURCE.read_text():
        raise ValueError("Approved Abaddon source drift")
    costs=p["nominal_costs"]
    boards=[]
    for board in p["preregistered_board_states"]:
        result=board_result(board,p["opponent_life"],p["pilot_life"])
        lost=result["total_opponent_life_lost"]
        mana=[]
        for row in p["mana_pools"]:
            possible=(result["game_continues"] and followup_after_commander(
                row["pool"],row["commander_already_present"],costs["abaddon"],costs["followup_mv3"]))
            mana.append({"pool_id":row["id"],"nominal_colored_followup_castable":bool(possible),
                         "granted_cascade_on_followup":bool(possible and cascade_triggers("followup_mv3",lost)["granted_by_abaddon"])})
        boards.append({"id":board["id"],"source":board["source"],"observed":result,"mana_followup":mana})
    printed=[]
    for lost in p["threshold_inputs"]:
        for origin,own_turn,commander in [("hand",True,True),("hand",True,False),("exile",True,True),("hand",False,True)]:
            printed.append({"opponent_life_lost":lost,"spell_origin":origin,"own_turn":own_turn,
               "commander_present":commander,
               "bituminous_blast":cascade_triggers("Bituminous Blast",lost,origin,own_turn,commander),
               "plain_mv3":cascade_triggers("followup_mv3",lost,origin,own_turn,commander)})
    kessig={"opponents":3,"spells_cast":2,"threshold_at_each_mv3_cast":[0,3],
            "grant_cascade_on_each_cast":[False,True],"threshold_after_both_trigger_resolutions":6,
            "requires_opponents_taking_unprevented_damage":True}
    birgi={"spells_cast":2,"red_mana_from_cast_triggers_if_resolved":2,
           "available_to_pay_same_spells_that_triggered":False,
           "available_to_pay_subsequent_spells_while_unspent":True,"harnfel_effect_modeled":False}
    assert [r["observed"]["total_opponent_life_lost"] for r in boards]==[0,54,0,54,0,27,0,0]
    assert cascade_triggers("Bituminous Blast",5)["total_on_cast"]==2
    assert cascade_triggers("Bituminous Blast",0,commander=False)["total_on_cast"]==1
    expected=[False,True,True,False]
    assert [followup_after_commander(m["pool"],m["commander_already_present"],
          costs["abaddon"],costs["followup_mv3"]) for m in p["mana_pools"]]==expected
    return {"schema_version":1,"stage":"M6_Abaddon_bounded_effect_aware_followthrough",
        "deck_id":p["deck_id"],"slug":p["slug"],"canonical_hash":p["canonical_hash"],
        "approved_list_sha256":p["approved_list_sha256"],"preregistration_sha256":"sha256:"+sha(PLAN),
        "source_baseline_sha256":"sha256:"+sha(SOURCE),"prior_rule_grid_sha256":"sha256:"+sha(PRIOR),
        "board_results":boards,"printed_cascade_cases":printed,
        "retained_engine_witnesses":{"Kessig Flamebreather":kessig,"Birgi, God of Storytelling":birgi},
        "blocked_ranking":"No win rate, upgrade preference, draw/mulligan/answer probability or deckwide pair comparison",
        "limitations":[
          "Eight conditional board states; not a sampled 99-card deck, paired Phase-B or multiplayer policy",
          "Specified prepaid mana pools only; no taxes, alternative costs, draw, counters or protection",
          "Kessig/Birgi witnesses require source survival and resolving triggers; Harnfel unmodeled",
          "Printed cascade instance counts do not simulate hits or downstream performance",
          "Opponent removal and survival scenarios have no estimated frequencies",
          "No Phase-B, Pass C, I, J, M6, swap or winner certification"],
        "effect_aware_deckwide_paired_test_executed":False,
        "full_phase_b_complete":False,"supports_improvement_claim":False,"authority":AUTH}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--build",action="store_true");ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    if not(args.build or args.check):ap.error("use --build or --check")
    output=enc(run())
    if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(output,encoding="utf-8")
    if args.check and (not OUT.is_file() or OUT.read_text(encoding="utf-8")!=output):
        raise ValueError("Cycle 94 evidence drift")
    print("Cycle 94: 8 conditional board cases, 24 cascade cases, 0 deck authority")
if __name__=="__main__":main()
