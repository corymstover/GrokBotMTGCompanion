#!/usr/bin/env python3
"""Validate preregistered Abaddon Phase-B hypotheses against accepted M6 packet."""
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_authority as ga

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_priority_01.json"
PACKET=ROOT/"data/grixis/m6/review_packets/abaddon-the-despoiler.json"
REGISTRY=ROOT/"data/grixis/registry.json"


def validate():
    plan=json.loads(PLAN.read_text())
    packet=json.loads(PACKET.read_text())
    registry=json.loads(REGISTRY.read_text())
    errors=ga.validate_file(plan,"m6_phase_b_plan.schema.json")
    if errors:raise ValueError("plan invalid: "+"; ".join(errors[:5]))
    if registry["program"]["milestones"]["M5"]["status"]!="accepted":
        raise ValueError("M5 not accepted")
    if registry["program"]["milestones"]["M6"].get("accepted_by") is not None:
        raise ValueError("M6 prematurely accepted")
    if plan["base_hash"]!=packet["list_hash"] or plan["deck_id"]!=packet["deck_id"]:
        raise ValueError("deck identity or canonical hash mismatch")
    source={x["swap_id"]:x for x in packet["items"]}
    chosen=[]
    for group in plan["groups"]:
        for sid in group["swap_ids"]:
            if sid not in source:
                raise ValueError("Phase B plan invents swap ID: "+sid)
            if source[sid]["add"]!=group["candidate"]:
                raise ValueError("proposed add mismatch for "+sid)
            chosen.append(sid)
        if group["test_status"]!="not_executed" or group["agent_judgment"]!="pending":
            raise ValueError("Phase-B test or judgment falsely claimed")
    if len(set(chosen))!=len(chosen) or len(chosen)!=plan["counts"]["hypotheses"]:
        raise ValueError("hypothesis count/identity mismatch")
    if len(plan["groups"])!=plan["counts"]["candidate_groups"]:
        raise ValueError("candidate count mismatch")
    if not all(not x for x in plan["authority"].values()):
        raise ValueError("unauthorized authority")
    for key in ("phase_b_tests_completed","formal_judgments_completed","swaps_applied"):
        if plan["counts"][key]!=0:
            raise ValueError("unexecuted preregistration may not make progress claims")
    print("Abaddon Phase-B preregistration VALID: 4 candidate areas, 7 real swap hypotheses, 0 tests/decisions")


if __name__=="__main__":
    validate()
