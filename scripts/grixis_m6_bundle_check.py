#!/usr/bin/env python3
"""Fail-closed verifier for FINAL M6 J reproducibility bundles.

This script never creates receipts or certificates and never changes deck state.
Missing bundles are reported as pending; a missing bundle cannot be counted ready.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
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

# Strict Pass C non-independence disclosure (added for PR #653, Ashad): "technical(ly) independen(ce|t)"
# followed only by markdown/colon punctuation and then an explicit FALSE, or a NO that ends the clause
# (so "no longer ..." never matches). Any explicit TRUE/YES statement anywhere vetoes this path.
# The four legacy substrings below are kept unchanged so every receipt accepted before stays accepted.
_PASS_C_EXPLICIT_FALSE = re.compile(
    r"\btechnical(?:ly)?\s+independen(?:ce|t)[\s*:_`]*(?:false\b|no(?=[\s*_`]*(?:[.,;)]|$)))", re.I | re.M)
_PASS_C_EXPLICIT_TRUE = re.compile(r"\btechnical(?:ly)?\s+independen(?:ce|t)[\s*:_`]*(?:true|yes)\b", re.I)


# Strict parenthetical Pass C non-independence disclosure (added after PR #653 for Ashnod_the_Uncaring,
# whose preserved receipt reads "technical third-model independence (actual evaluator ...; independent=FALSE,
# owner-waived)"). Accepts only an explicit independent=FALSE inside the parenthetical that directly follows
# "technical third-model independence"; any independent=TRUE/YES or explicit TRUE/YES statement anywhere vetoes.
_PASS_C_PAREN_FALSE = re.compile(
    r"\btechnical\s+third-model\s+independence\s*\([^()]*?\bindependent\s*=\s*false\b[^()]*\)", re.I)
_PASS_C_PAREN_TRUE = re.compile(r"\bindependent\s*=\s*(?:true|yes)\b", re.I)


def pass_c_parenthetical_false_disclosure(text):
    """Fail closed: True only for the explicit parenthetical independent=FALSE form, with no
    independent=TRUE/YES and no explicit TRUE/YES technical-independence statement anywhere."""
    return (bool(_PASS_C_PAREN_FALSE.search(text)) and not _PASS_C_PAREN_TRUE.search(text)
            and not _PASS_C_EXPLICIT_TRUE.search(text))


def pass_c_explicit_false_disclosure(text):
    """Fail closed: True only for an explicit FALSE/NO technical-independence statement with no
    explicit TRUE/YES statement anywhere in the receipt. Absent or ambiguous wording returns False."""
    return bool(_PASS_C_EXPLICIT_FALSE.search(text)) and not _PASS_C_EXPLICIT_TRUE.search(text)


def _bare(h):
    return (h or "").removeprefix("sha256:")


# Legacy Stage A seal field names (added after PR #653 for Ashnod_the_Uncaring, whose preserved, immutable
# seal.json uses the "A_SEAL" schema). Only these exact one-to-one renames are mapped; values are never
# rewritten or inferred. Fail closed: a seal carrying both a canonical key and its legacy alias is rejected,
# and a seal that is not the complete A_SEAL legacy form is returned unchanged (so it fails as before).
_LEGACY_A_SEAL_ALIASES = {
    "canonical_input_sha256": "canonical_approved_sha256",
    "git_first_stage_commit_sha": "first_stage_git_commit_sha",
    "review_class_after_final": "formal_pass_c_classification",
    "technically_independent": "technical_independence",
    "actual_evaluator": "actual_model",
}


def normalize_legacy_stage_a_seal(seal):
    """Return seal with canonical field names for the exact legacy A_SEAL schema, else unchanged."""
    if any(c in seal and a in seal for c, a in _LEGACY_A_SEAL_ALIASES.items()):
        raise ValueError("Stage A seal carries both canonical and legacy field names")
    if (seal.get("stage") != "A_SEAL" or seal.get("owner_independence_waiver") is not True
            or any(c in seal for c in _LEGACY_A_SEAL_ALIASES)
            or not all(a in seal for a in _LEGACY_A_SEAL_ALIASES.values())):
        return seal
    out = {k: v for k, v in seal.items() if k not in _LEGACY_A_SEAL_ALIASES.values()}
    for c, a in _LEGACY_A_SEAL_ALIASES.items():
        out[c] = seal[a]
    return out


def registry_bound_digest_discrepancy(row, seal, deck_id):
    """Accept a progress-ledger/seal digest mismatch ONLY when it is the registry's own
    recorded historical-digest vs physical-raw discrepancy for this deck.

    Fail closed: the registry must say recorded_matches_raw is False, the ledger must
    carry exactly the registry's recorded (historical) digest, the Stage A seal must
    carry exactly the registry's physical raw SHA-256, and the two must differ. Nothing
    is rewritten; the historical value is preserved and merely reconciled.
    """
    deck = load(REGISTRY)["decks"].get(deck_id) or {}
    src = deck.get("source") or {}
    recorded, physical = _bare(src.get("recorded_sha256")), _bare(src.get("raw_sha256"))
    return (src.get("recorded_matches_raw") is False
            and bool(recorded) and bool(physical) and recorded != physical
            and _bare(row.get("canonical_approved_sha256")) == recorded
            and _bare(seal.get("canonical_input_sha256")) == physical)


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
    seal = normalize_legacy_stage_a_seal(load(safe_repo_file(expected["stage_a_seal_path"])))  # e.g. Ashnod_the_Uncaring
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
        or not (row.get("canonical_approved_sha256") == seal.get("canonical_input_sha256")
                or registry_bound_digest_discrepancy(row, seal, deck_id))
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
        or "**Technically independent:** NO." in final
        or "**Technically independent:** FALSE." in final  # Anhelo__the_Painter preserved wording
        or pass_c_explicit_false_disclosure(final)  # strict pattern, e.g. Ashad__the_Lone_Cyberman
        or pass_c_parenthetical_false_disclosure(final)  # strict parenthetical, e.g. Ashnod_the_Uncaring
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
