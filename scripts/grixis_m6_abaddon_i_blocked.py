#!/usr/bin/env python3
"""Generate a source-bound *BLOCKED*, not PASS, M6 I local-optimum receipt.

This is a truthful negative gate while a plausible commander-first two-swap
remains unapproved, partial effect tests remain, and four P0 cases are open.
It must never create a zero-improvement PASS or authorize deck changes.
"""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import jsonschema
from scripts.grixis_m6_abaddon_preflight import (
    ROOT, INVENTORY, DECISION, SNAPSHOT, PINNED, COVERAGE, sha, load
)
from scripts.grixis_m7_decision_gate import parse_list

SCHEMA=ROOT/"data/grixis/schemas/zero_improvement_certificate.schema.json"
SCOPE="Local optimum over the explicitly tested candidate pool only; not a mathematical or global proof of optimality."
M5_RECEIPT="data/grixis/m6/ij/input_receipts/abaddon-the-despoiler.json"
OPTIMIZER="data/grixis/m6/sealed/reconciliation_manifest.json"

class BlockedCertificateFailure(ValueError):
    pass


def build():
    inv=load(ROOT/INVENTORY)
    p=load(ROOT/DECISION)
    audit=load(ROOT/COVERAGE)
    if (len(inv["replay_cases"])!=44 or
        {x["id"] for x in inv["required_open"]}!={"P0-024","P0-025","P0-026","P0-027"} or
        len(audit["identified_unresolved"])!=4 or inv["authority"]["formal_m6_certified"]):
        raise BlockedCertificateFailure("Source completeness inventory must remain truthful")
    if sha(ROOT/SNAPSHOT)!=PINNED or p["canonical"]["approved_sha256"]!=PINNED:
        raise BlockedCertificateFailure("Canonical 100 deck SHA drift")
    for v in (p["proposed"],p["competing"]):
        if sha(ROOT/v["file"])!=v["physical_sha256"]:
            raise BlockedCertificateFailure("100-card staged pool SHA drift")
        cards,commands,comp=parse_list(ROOT/v["file"])
        if len(cards)!=100 or commands!=["Abaddon the Despoiler"] or comp:
            raise BlockedCertificateFailure("Invalid exact candidate")
    history=load(ROOT/M5_RECEIPT)
    if history["status"]!="inputs_attested_downstream_incomplete":
        raise BlockedCertificateFailure("Frozen M5 receipt falsely certifies Phase B")
    logical=history["list_hash"]
    if not logical.startswith("lh1:"):
        raise BlockedCertificateFailure("Missing canonical logical SHA")
    cases=sorted({x["test_file"] for x in inv["replay_cases"]})
    unresolved=[x["id"]+": "+x["topic"] for x in inv["required_open"]]
    unresolved.extend([
      "M7 preferred two-swap package versus the Keeper-cut alternative has not demonstrated comparable representative adversarial net-game superiority.",
      "The originally approved baseline cannot be declared a tested-pool local optimum while a plausible sourced commander-first two-swap improvement remains in review.",
    ])
    receipt={
      "schema_version":1,"deck_id":"Abaddon_the_Despoiler",
      "slug":"abaddon-the-despoiler",
      "generated_at":datetime.now(timezone.utc).isoformat(),
      "list_hash":logical,
      "candidate_pool":{"source_ref":DECISION,
          "source_sha256":"sha256:"+sha(ROOT/DECISION),
          "tested_pool_size":2},
      "optimizer_pass_ref":OPTIMIZER,
      "reconciliation_complete":False,
      "phase_b":{"all_required_tests_pass":False,"test_refs":cases},
      "unresolved_requires_human_judgment":unresolved,
      "receipt_refs":[M5_RECEIPT,INVENTORY,COVERAGE,
                     "data/grixis/m6/certification_preflight/Abaddon_the_Despoiler_M6_6_7_reconciliation_20261022.md"],
      "improving_substitution_found":False,
      "local_optimum_for_tested_pool":False,
      "certificate_status":"blocked",
      "blockers":[
         "Four source-identifiable P0 exile-cast core interactions remain unexecuted; 44 historic named P0 passing tests are not complete deckwide effect coverage.",
         "Two plausible exact 100-card challenger packages are not a closed effect-aware matched-game pool. The improving-substitution field is FALSE meaning not *proven*, not a proved absence of an improvement.",
         "Current baseline already has an authored plausible commander-first upgrade, so declaring zero improvement on it would be premature.",
         "Owner approval not given for current M7 proposed exact 100; do not conflate M6 evidence with M7 authority.",
      ],
      "scope_caveat":SCOPE,
      "authority":{"can_decide":False,"can_approve_or_lock":False,
                   "note":"Pure engineering BLOCKED finding; no swap, M6 acceptance, local-optimum PASS, or owner approval."}
    }
    check(receipt)
    return receipt


def check(d):
    errors=sorted(jsonschema.Draft202012Validator(load(SCHEMA)).iter_errors(d),
                  key=lambda x:tuple(str(i) for i in x.path))
    if errors:
        raise BlockedCertificateFailure("Invalid M6 I schema: "+str(errors[0].message))
    current=load(ROOT/DECISION)
    inv=load(ROOT/INVENTORY)
    if (d["certificate_status"]!="blocked" or d["local_optimum_for_tested_pool"] or
        d["reconciliation_complete"] or d["phase_b"]["all_required_tests_pass"] or
        d["authority"]["can_decide"] or d["authority"]["can_approve_or_lock"] or
        d["candidate_pool"]["source_ref"]!=DECISION or
        d["candidate_pool"]["source_sha256"]!="sha256:"+sha(ROOT/DECISION) or
        d["candidate_pool"]["tested_pool_size"]!=2 or
        set(d["phase_b"]["test_refs"])!={x["test_file"] for x in inv["replay_cases"]} or
        len(d["unresolved_requires_human_judgment"])!=6 or
        any(x["id"] not in "\n".join(d["unresolved_requires_human_judgment"]) for x in inv["required_open"]) or
        current["owner_approved"]):
        raise BlockedCertificateFailure("M6 I blocked receipt violates fixed source/authority gates")
    return True


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",required=True,type=Path)
    args=ap.parse_args()
    receipt=build()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(receipt,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf-8")
    check(load(args.out))
    print("ABADDON_M6_I_BLOCKED_SCHEMA_PASS",json.dumps({
        "status":receipt["certificate_status"],"open_mechanics":4,
        "tested_pool_size":2,"m6_i_certified":False,
        "file_sha256":sha(args.out),"path":str(args.out)},sort_keys=True))


if __name__=="__main__":
    main()
