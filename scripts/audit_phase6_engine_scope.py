#!/usr/bin/env python3
"""Rebuild/check a finite four-capability Phase 6 infrastructure acceptance.

No lore pilot is approved. No live legality, bracket, unknown lore or Grixis
approval is asserted. This certifies the *reusable bounded operations* behind
K106/K109/K111/K115, not remaining research or owner review tasks.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_foundation_milestone_certificate as foundation
import audit_lore_pilot as pilots
import lore_deck_candidates as candidates
import lore_deck_restrictions as restrictions
import release_readiness as readiness

OUT = ROOT / "data/release/phase6_engine_scope_review_2026-11-01.json"


def build():
    cert = foundation.check()
    if cert["status"] != "CERTIFIED_BOUNDED_KNOWLEDGE_FOUNDATION_MILESTONE":
        raise ValueError("Phase 6 foundation prerequisite not certified")
    digests = readiness.tree_digest(readiness.PROTECTED)
    if {path: row["sha256"] for path, row in digests.items()} != cert["external_verification"]["protected_path_sha256"]:
        raise ValueError("protected Grixis approval/state paths changed since certified foundation baseline")
    specs = sorted(pilots.SPECS.glob("*.json"))
    if len(specs) != 3:
        raise ValueError("expected exactly three preserved UNAPPROVED pilots")
    results, grades_total = [], {g: 0 for g in pilots.TIERS}
    for specpath in specs:
        spec = json.loads(specpath.read_text(encoding="utf-8"))
        proof = pilots.audit(specpath)
        if proof["status"] != spec["status"] or not proof["status"].startswith("UNAPPROVED"):
            raise ValueError("pilot status drift")
        found = candidates.retrieve(spec["stem"])
        if found["status"] != proof["status"] or found["count"] != proof["named"]:
            raise ValueError("graded candidate retrieval drift")
        grades = {g: len(candidates.retrieve(spec["stem"], g)["cards"]) for g in pilots.TIERS}
        if grades != proof["tiers"]:
            raise ValueError("graded retrieval no longer mirrors exact printing evidence")
        for grade, count in grades.items():
            grades_total[grade] += count
        if not all(row["oracle_id"] and row["printing_id"] and row["source"] for row in found["cards"]):
            raise ValueError("graded retrieval lost identity/printing/source provenance")
        # A restrictive first-print/debut filter should explain both eligible
        # and ineligible cards, while never silently allowing missing data.
        evidence = json.loads(pilots.files(spec)["printing_evidence.json"].read_text(encoding="utf-8"))
        filtered = restrictions.evaluate(evidence["cards"], restrictions.Restriction(first_sets=frozenset({"lea"})))
        if filtered["totals"]["UNKNOWN"] or not filtered["totals"]["EXCLUDED"]:
            raise ValueError("Phase 1B debut filter did not fail closed or exercise exclusions")
        props = json.loads(pilots.files(spec)["proposal.json"].read_text(encoding="utf-8"))
        if any(props["approval"][key] for key in ("approved", "locked", "certified")):
            raise ValueError("unexpected lore pilot approval or lock")
        if len(props["archidekt_tags"]) != 3 or len(set(props["archidekt_tags"])) != 3:
            raise ValueError("Archidekt tag count/uniqueness drift")
        results.append({"stem": spec["stem"], "status": proof["status"], "snapshot": proof["snapshot"],
                        "total_cards": proof["total"], "graded_nonbasic_candidates": found["count"],
                        "graded_retrieval": grades, "three_archidekt_tags": props["archidekt_tags"],
                        "commander_first_exact_import": True, "pilot_approval_flags_all_false": True,
                        "first_printed_in_lea_example": filtered["totals"],
                        "spec_sha256": hashlib.sha256(specpath.read_bytes()).hexdigest(),
                        "evidence_sha256": hashlib.sha256(pilots.files(spec)["printing_evidence.json"].read_bytes()).hexdigest()})
    if not all(grades_total.values()):
        raise ValueError("all four curated retrieval tiers must be represented")
    return {"schema": "phase6-engine-scope-acceptance/v1", "as_of": "2026-11-01",
            "scope": "Four bounded existing/incremental Phase 6 engine capabilities, not pilot approval or whole-project certification",
            "foundation_certificate": "data/release/foundation_milestone_certificate_2026-11-01.json",
            "criteria": {"K106_curator_graded_lore_card_retrieval": "PASS_BOUNDED_TO_EXISTING_CURATED_POOL",
                         "K109_printing_set_publication_era_oracle_debut_filters": "PASS_DATED_PHASE1B_ENGLISH_PAPER",
                         "K111_three_tags_exact_commander_first_import": "PASS_ALL_THREE_UNAPPROVED_PILOTS",
                         "K115_protected_Grixis_baseline": "PASS_UNCHANGED_CERTIFIED_PROTECTED_DIGESTS"},
            "grade_totals": grades_total, "pilots": results,
            "protected_baseline_sha256": {k: v["sha256"] for k, v in digests.items()},
            "limitations": ["Graded candidates are already curated, not autonomous canon classification for arbitrary prompts.",
                            "Printing-era dates are publication history, not in-world story eras.",
                            "First-recorded debut is Oracle-ID-specific English paper as of October 29, not an absolute cross-language/world first.",
                            "Commander choice comparison, realistic deck strategy, live rules/legality/bracket and three explicit owner pilot approvals remain open.",
                            "Existing 62 Grixis canonical deck approvals/lists and all three unapproved pilot proposals were not modified."]}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true")
    args = p.parse_args(argv)
    result = build()
    content = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if OUT.read_text(encoding="utf-8") != content:
            raise ValueError("Phase 6 acceptance artifact stale")
    else:
        OUT.write_text(content, encoding="utf-8")
    print("PASS Phase 6 engine scoped acceptance; all pilots UNAPPROVED; Grixis protected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
