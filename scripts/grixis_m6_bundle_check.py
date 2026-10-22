#!/usr/bin/env python3
"""Fail-closed verifier for FINAL M6 J reproducibility bundles.

This script never creates receipts or certificates and never changes deck state.
Missing bundles are reported as pending; a missing bundle cannot be counted ready.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga

BUNDLES = ROOT / "data/grixis/m6/bundles"
REGISTRY = ROOT / "data/grixis/registry.json"
SEALS = ROOT / "data/grixis/m6/sealed/reconciliation_manifest.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def safe_repo_file(name):
    path = Path(name)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("unsafe artifact path")
    full = (ROOT / path).resolve()
    if not full.is_relative_to(ROOT.resolve()) or not full.is_file():
        raise ValueError("missing/outside-repo artifact: " + name)
    return full


def content_hash(name):
    return "sha256:" + hashlib.sha256(safe_repo_file(name).read_bytes()).hexdigest()


def bind(name, h):
    if content_hash(name) != h:
        raise ValueError("SHA-256 drift: " + name)


OWNER_EQUIVALENT = "FORMAL_PASS_C_OWNER_EQUIVALENT"
OWNER_WAIVER = "data/grixis/m6/governance/pass_c_owner_waiver_20261021.json"
OWNER_PROGRESS = "data/grixis/m6/owner_pass_c_substitute/progress.json"


def validate_pass_c(judgment, deck_id):
    """Validate either original independent reviewer receipt or owner's exact waiver.

    The waived mode is explicitly NON-INDEPENDENT, with the real owner decision,
    the 62/62 progress ledger, this deck's sealed Stage A and final disposition
    bound to immutable SHA-256 references. This never waives Phase B or M6 J.
    """
    bind(judgment["judgment_receipt_path"], judgment["judgment_receipt_sha256"])
    if judgment.get("review_class") != OWNER_EQUIVALENT:
        reviewer = load(safe_repo_file(judgment["judgment_receipt_path"]))
        if reviewer.get("reviewer") != judgment["reviewer"] or reviewer.get("status") != "critical_review_complete":
            raise ValueError("Pass C reviewer receipt not complete/identified")
        if reviewer.get("can_approve_or_lock") is not False:
            raise ValueError("Pass C reviewer attempted approval")
        return True

    directory = f"data/grixis/m6/owner_pass_c_substitute/{deck_id}"
    expected = {
        "judgment_receipt_path": f"{directory}/final_disposition.md",
        "waiver_receipt_path": OWNER_WAIVER,
        "progress_receipt_path": OWNER_PROGRESS,
        "stage_a_seal_path": f"{directory}/seal.json",
    }
    for key, path in expected.items():
        if judgment.get(key) != path:
            raise ValueError("Wrong owner-equivalent Pass C source: " + key)
    for key in ("waiver_receipt", "progress_receipt", "stage_a_seal"):
        bind(judgment[key + "_path"], judgment[key + "_sha256"])
    waiver = load(safe_repo_file(OWNER_WAIVER))
    progress = load(safe_repo_file(OWNER_PROGRESS))
    seal = load(safe_repo_file(expected["stage_a_seal_path"]))
    if (judgment.get("technically_independent") is not False
        or progress.get("technically_independent") is not False
        or progress.get("genuinely_independent_third_model_reviews") != 0
        or progress.get("review_class") != OWNER_EQUIVALENT
        or progress.get("actual_model") != "ChatGPT/OpenAI GPT-6"
        or judgment.get("reviewer") != progress["actual_model"]
        or progress.get("formal_pass_c_owner_equivalent_completed") != 62
        or progress.get("final_complete") != 62
        or waiver.get("decision") != "AUTHORIZE_OWNER_EQUIVALENT_PASS_C_AS_REPLACEMENT_FOR_INDEPENDENT_THIRD_MODEL_REQUIREMENT_FOR_M6_GOVERNANCE"
        or waiver.get("applies_to", {}).get("gate") != "M6.5"
        or waiver.get("scope_and_effect", {}).get("m6_5_governance_condition_satisfied") is not True
        or waiver.get("accepted_substitute", {}).get("technically_independent") is not False
        or waiver.get("accepted_substitute", {}).get("genuinely_independent_third_model_reviews") != 0
        or waiver.get("scope_and_effect", {}).get("other_m6_gates_remain_independently_required") is not True):
        raise ValueError("Owner-equivalent Pass C provenance/waiver not valid")
    rows = [x for x in progress.get("decks", []) if x.get("deck_id") == deck_id]
    if len(rows) != 1:
        raise ValueError("Missing or duplicated owner-equivalent deck review")
    row = rows[0]
    if (row.get("stage_status") != "FINAL_EVIDENCE_MERGED"
        or not all(row.get(k) is True for k in ("stage_a_complete", "stage_b_complete", "final_complete", "canonical_unchanged"))
        or row.get("owner_swap_approved") is not False
        or row.get("final_evidence_path") != expected["judgment_receipt_path"]
        or row.get("canonical_approved_sha256") != seal.get("canonical_input_sha256")
        or row.get("first_stage_commit_sha") != seal.get("git_first_stage_commit_sha")
        or seal.get("deck_id") != deck_id
        or seal.get("review_class_after_final") != OWNER_EQUIVALENT
        or seal.get("technically_independent") is not False
        or seal.get("actual_evaluator") != progress["actual_model"]):
        raise ValueError("Owner-equivalent deck/Stage A seal provenance mismatch")
    for ext in ("md", "json"):
        if content_hash(seal["stage_a_" + ext + "_path"]) != "sha256:" + seal["stage_a_" + ext + "_sha256"]:
            raise ValueError("Stage A source diverged from separately sealed byte commitment")
    final = safe_repo_file(judgment["judgment_receipt_path"]).read_text(encoding="utf-8")
    # Historical owner-equivalent reviews used two explicit negative-independence labels.
    # Accept the actual preserved wordings, never an absent or implied disclosure.
    disclosed_nonindependence = (
        "Technically independent third model" in final
        or "**actual technical independence:** false" in final
    )
    if ("ChatGPT/OpenAI GPT-6" not in final
        or not disclosed_nonindependence
        or row["final_disposition"] not in final):
        raise ValueError("Owner-equivalent final review missing provenance/disposition")
    return True


def validate_bundle(b, registry, seals):
    errors = ga.validate_file(b, "m6_reproducibility_bundle.schema.json")
    if errors:
        raise ValueError("invalid J bundle schema: " + "; ".join(errors[:8]))
    deck = registry["decks"].get(b["deck_id"])
    if not deck or b["slug"] != deck["slug"] or b["baseline_hash"] != deck["current_canonical_hash"]:
        raise ValueError("bundle baseline is not the preserved canonical hash")
    if b["snapshot"]["birthday_id"] != load(ROOT / "data/grixis/birthday_m5/summary.json")["birthday_authority_snapshot"]:
        raise ValueError("bundle Birthday snapshot mismatch")
    for item in b["inputs"]:
        bind(item["path"], item["sha256"])
    if b["sealed_passes"]["a_commit"] != seals["pass_a_commit"] or b["sealed_passes"]["b_commit"] != seals["pass_b_commit"]:
        raise ValueError("A/B committed hashes mismatch")
    bind("data/grixis/m6/sealed/reconciliation_manifest.json",
         b["sealed_passes"]["reconciliation_manifest_sha256"])
    slug = b["slug"]
    for side in ("a", "b"):
        name = b["sealed_passes"][side + "_output_ref"]
        expected = f"data/grixis/m6/sealed/{side.upper()}/{slug}.json"
        if name != expected:
            raise ValueError("sealed pass path mismatch")
        sealed = load(safe_repo_file(name))
        if sealed["pass"]["list_hash"] != b["baseline_hash"]:
            raise ValueError("sealed pass list hash mismatch")
    judgment = b["pass_c"]
    validate_pass_c(judgment, b["deck_id"])
    for t in b["phase_b"]["tests"]:
        bind(t["test_ref"], t["source_sha256"])
        if t["supports_improvement_claim"] and (t["effect_coverage"] != "fully_modeled" or t["verdict"] != "pass"):
            raise ValueError("unmodeled or failing test was promoted as improvement proof")
    for key in ("red_team", "mana_analysis"):
        bind(b[key]["report_path"], b[key]["sha256"])
    for key in ("oracle_ref", "rules_ref", "legality_ref"):
        safe_repo_file(b["snapshot"][key])
    if b["authority"]["can_approve_or_lock"] or b["authority"]["can_decide"]:
        raise ValueError("bundle illegally contains human approval")
    return True


def check():
    reg = load(REGISTRY)
    if len(reg["decks"]) != 62 or reg["program"]["milestones"]["M5"]["status"] != "accepted":
        raise ValueError("M5 authority incomplete")
    seals = load(SEALS)
    if seals["pass_c"]["complete"] is not False:
        raise ValueError("reconciliation manifest may not self-certify Pass C")
    expected = {x["slug"] for x in reg["decks"].values()}
    files = sorted(BUNDLES.glob("*.json")) if BUNDLES.exists() else []
    if len(files) > 62:
        raise ValueError("more than 62 bundles")
    seen = set()
    for p in files:
        bundle = load(p)
        if p.stem != bundle.get("slug") or p.stem not in expected or p.stem in seen:
            raise ValueError("unknown/duplicated final bundle: " + p.name)
        seen.add(p.stem)
        validate_bundle(bundle, reg, seals)
    print(f"M6 J final bundle verification: {len(seen)}/62 valid; {62-len(seen)} pending; no approval authority")
    return len(seen)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", required=True)
    ap.add_argument("--require-complete", action="store_true")
    args = ap.parse_args()
    count = check()
    if args.require_complete and count != 62:
        raise SystemExit("not enough complete bundles for M6 closure")
