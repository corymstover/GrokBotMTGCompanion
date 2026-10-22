#!/usr/bin/env python3
"""Read-only catalog of 61 UNIMPLEMENTED Commander effect-test design contracts.

This module NEVER imports or executes a designed test, simulator, mechanic
adapter, GitHub workflow, or deck mutation. It only reads and validates JSON.
Older authoring batches used three harmless metadata layouts; normalize their
plan entries into one immutable view without silently changing source claims.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=Path("data/grixis/m6/test_blueprints")
INDEX=BASE/"index.json"
ALLOWED_PRIORITIES={"P0","P1"}


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def plan_cases(document):
    candidates=document.get("tests",document.get("cases"))
    if not isinstance(candidates,list):
        raise ValueError("Missing deck-specific scenario list")
    result=[]
    for obj in candidates:
        if not isinstance(obj,dict):
            raise ValueError("Malformed effect case")
        case_id=obj.get("case_id",obj.get("id",obj.get("test_id")))
        anchor=obj.get("source_ref",obj.get("source",obj.get("source_anchor")))
        claim=obj.get("source_predicate_to_verify",obj.get("expected_claim_to_verify",
                    obj.get("oracle_or_blueprint_claim_pending_verification",
                    obj.get("expected_result_status",""))))
        if not case_id or not isinstance(anchor,str) or not anchor.startswith("blueprint:"):
            raise ValueError("Every effect case needs a unique ID and source anchor")
        if obj.get("priority") not in ALLOWED_PRIORITIES:
            raise ValueError("Unknown effect priority")
        statuses=(obj.get("implementation_status"),obj.get("implementation"),obj.get("status"),
                  obj.get("execution_status"),obj.get("execution"))
        if any(x and ("PASS" in str(x) or "EXECUTED" in str(x) and "NOT" not in str(x))
               for x in statuses):
            raise ValueError("Backlog cannot claim executable/passing cases")
        result.append({"id":case_id,"priority":obj["priority"],"source":anchor,
                       "scenario":obj.get("scenario",obj.get("title",case_id)),
                       "source_claim_to_verify":claim,
                       "kind":obj.get("kind",obj.get("contract","case")),
                       "cards":obj.get("fixture_named_cards",obj.get("cards",obj.get("associated_cards",[]))),
                       "status":"DESIGNED_NOT_IMPLEMENTED_NOT_RUN"})
    if len({x["id"] for x in result})!=len(result):
        raise ValueError("Duplicate effect case IDs")
    return result


def validate_catalog(root=ROOT):
    index=read(root/INDEX)
    scope=index["scope"]
    if scope["exclude"]!="Abaddon_the_Despoiler" or scope["roster_count"]!=61:
        raise ValueError("This is only the other 61 commander's backlog")
    entries=index["roster"]
    if len(entries)!=61 or len({x["deck_id"] for x in entries})!=61:
        raise ValueError("Missing/duplicate commander record")
    if any(v for v in [scope["executed"],scope["passed"],scope["implemented_effect_adapters"],
                       scope["completed_M6_decks_added"],scope["canonical_decks_modified"]]):
        raise ValueError("Designed-only backlog must never claim implementation or game approval")
    totals=Counter()
    decks=[]
    for expected in entries:
        deck_id=expected["deck_id"]
        if "/" in deck_id or "\\" in deck_id or deck_id.startswith("."):
            raise ValueError("Unsafe deck ID")
        file_path=root/BASE/(deck_id+".json")
        d=read(file_path)
        if d.get("deck_id")!=deck_id:
            raise ValueError("Mismatched deck ID "+deck_id)
        approved=(d.get("source_basis") or d.get("source_provenance") or d.get("source") or {})
        sha=(approved.get("registered_approved_sha256") or
             approved.get("canonical_approved_sha256") or
             approved.get("approved_sha256"))
        if sha!=expected["approved_source_sha256"]:
            raise ValueError("Registered approved SHA mismatch: "+deck_id)
        clauses=plan_cases(d)
        counts=Counter(x["priority"] for x in clauses)
        if (len(clauses)!=expected["designed_cases"] or counts["P0"]!=expected["P0"]
             or counts["P1"]!=expected["P1"]):
            raise ValueError("Index/case-count drift: "+deck_id)
        if expected["P0"]<1:
            raise ValueError("No commander-specific P0 test: "+deck_id)
        if not all(x["status"]=="DESIGNED_NOT_IMPLEMENTED_NOT_RUN" for x in clauses):
            raise ValueError("Unexpected test execution claim: "+deck_id)
        totals.update({"decks":1,"cases":len(clauses),"P0":counts["P0"],"P1":counts["P1"]})
        decks.append({"deck_id":deck_id,"position":expected["position"],
                      "designed_cases":len(clauses),"P0":counts["P0"],"P1":counts["P1"],
                      "path":expected["path"],"cases":clauses})
    if dict((k,totals[k]) for k in ("decks","cases","P0","P1")) != {
        "decks":61,"cases":882,"P0":308,"P1":574}:
        raise ValueError("Frozen design totals not independently reproduced")
    # Quantity-weighted 100-card audits come later. A TXT with 94 unique
    # line entries can contain 100 total cards because basic lands repeat.
    return {"status":"STATIC_DESIGN_CATALOG_VALID_ONLY","checks":"JSON_SHAPES_AND_INDEX_COUNTS_ONLY",
            "executes_tests":False,"oracle_freshness_verified":False,
            "approved_100_card_counts_verified":False,
            "total":dict(totals),"decks":decks}


def main():
    parser=argparse.ArgumentParser(description="Inspect, NEVER EXECUTE pending 61 Commander test plans")
    parser.add_argument("--deck-id",help="inspect a single pending commander")
    parser.add_argument("--priority",choices=["all","P0","P1"],default="all")
    parser.add_argument("--summary-only",action="store_true")
    parser.add_argument("--json-out",type=Path)
    opts=parser.parse_args()
    report=validate_catalog()
    if opts.deck_id:
        report["decks"]=[x for x in report["decks"] if x["deck_id"]==opts.deck_id]
        if not report["decks"]:
            parser.error("not part of the 61 deck backlog")
    if opts.priority!="all":
        for d in report["decks"]:
            d["cases"]=[x for x in d["cases"] if x["priority"]==opts.priority]
    if opts.summary_only:
        for d in report["decks"]:
            d.pop("cases")
    rendered=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if opts.json_out:
        opts.json_out.write_text(rendered,encoding="utf-8")
    print(rendered)


if __name__=="__main__":
    main()
