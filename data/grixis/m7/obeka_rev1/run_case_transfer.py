"""Execute the 15 Obeka C/K/E/W/F fixtures and seal exact-source transfer.

This is a deck-specific finite rules test record. It deliberately does not
invent historical I/J certificates or assert project-wide M6 certification.
"""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import unittest

from test_obeka_rev1 import ObekaBlueprintCases

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / "data/grixis/m6/test_blueprints/Obeka__Brute_Chronologist.json"
CAND = ROOT / "data/grixis/m7/candidate_lists/Obeka__Brute_Chronologist_chatgpt_rev1.txt"
ORACLE = ROOT / "data/grixis/m7/oracle_snapshots/Obeka__Brute_Chronologist_Rev1_Scryfall_20261027.json"
OUT = ROOT / "data/grixis/m7/verification/Obeka__Brute_Chronologist_Rev1_Scoped_M6_IJ_20261027.json"
CHANGED = {
    "K2": "Footsteps/Mimic Vat/Splinter Twin delayed next-end-step liabilities, source paid; early skip fails",
    "K3": "Delina removed because repeated regular end-combat exile; added Mimic Vat one-shot retains",
    "K6": "Removed historical Delina + Kiki condition, retained Dualcaster/Twinflame",
    "E2": "Added Footsteps/Mimic Vat/Splinter Twin one-shot token/creature persistence; 'until end' expires",
    "W2": "Removed Delina path; new nonlegend Zealous Conscripts + Kiki-Jiki and Twin loops traced",
    "F1": "Failure if Obeka removed while risky-turn lose trigger on stack",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    blueprint = json.loads(BASE.read_text())
    oracle = json.loads(ORACLE.read_text())
    assert oracle["candidate_sha256"] == sha(CAND)
    tests = unittest.defaultTestLoader.loadTestsFromTestCase(ObekaBlueprintCases)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    assert result.wasSuccessful() and result.testsRun == len(blueprint["cases"]) == 15
    methods = {x.replace("test_", "").split("_", 1)[0]: x
               for x in dir(ObekaBlueprintCases) if x.startswith("test_")}
    rows = []
    for item in blueprint["cases"]:
        case_id = item["id"]
        assert case_id in methods
        rows.append({
            "id": case_id,
            "priority": item["priority"],
            "contract": item["contract"],
            "historical_blueprint_status": item["status"],
            "scoped_execution": "PASS_FINITE_STATE_FIXTURE",
            "test_method": "ObekaBlueprintCases." + methods[case_id],
            "source": item["source"],
            "normal_and_adversarial": "Both payable/valid and negated prerequisite/timing cases are asserted where materially relevant; check test source for exact state.",
            "changed_card_scope": CHANGED.get(case_id, "Source-bound retained Obeka interaction; exact final 100 includes relevant cited cards where still applicable."),
            "limitations": "Not a full Comprehensive Rules engine or multiplayer win-rate benchmark; no automatic M6 certification.",
        })
    receipt = {
        "schema": "OBEKA_M7_REV1_SCOPED_CASE_TRANSFER",
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "deck_id": "Obeka__Brute_Chronologist",
        "canonical_2026_10_15_raw_sha256": "31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8",
        "candidate_raw_sha256": sha(CAND),
        "oracle_snapshot_sha256": sha(ORACLE),
        "oracle_retrieved_utc": oracle["retrieved_utc"],
        "planned_p0": 5,
        "executed_p0": 5,
        "passed_p0": 5,
        "planned_p1": 10,
        "executed_p1": 10,
        "passed_p1": 10,
        "deferred": 0,
        "assertions": rows,
        "reproduce": [
            "python data/grixis/m7/obeka_rev1/verify_obeka_rev1.py",
            "python data/grixis/m7/obeka_rev1/test_obeka_rev1.py",
            "python data/grixis/m7/obeka_rev1/run_case_transfer.py",
        ],
        "formal_m6_or_project_ij_certification": "NOT_INFERRED; legacy full-project transfer chain remains independent.",
        "win_rate_claim": "NONE; finite deterministic stack/timing/cost assertions only.",
        "canonical_mutation": False,
    }
    OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(f"PASS 15/15 (P0 5/5, P1 10/10); scoped transfer receipt {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
