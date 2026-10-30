#!/usr/bin/env python3
"""Offline audit of the Pack A open-question review record.

Checks that the review targets real Pack A claims, that the retained grades match
the pack exactly (the review never silently changes a grade), that every evidence
id is a checked first-party Wizards source, that non-Wizards context is labelled
and never used as evidence, and that proposals are not already applied.
"""
import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
REVIEW = ROOT / "data/lore_research/pack_a_open_question_review_2026-10-30.json"
GRADES = {"CANON_CONFIRMED", "CANON_IMPLIED", "CANON_DISPUTED", "ALTERNATE_CONTINUITY", "OPEN_QUESTION"}
WIZ = {"magic.wizards.com", "www.magic.wizards.com"}
BANNED = ("APPROVED", "LOCKED", "CERTIFIED")


def audit(review: dict, pack: dict) -> list:
    errs = []
    if review.get("schema") != "pack-open-question-review/v1":
        errs.append("schema")
    if not str(review.get("status", "")).startswith("PRELIMINARY"):
        errs.append("status must stay PRELIMINARY")
    for w in BANNED:
        if w in str(review.get("status", "")).upper().replace("NOT CORY-REVIEWED", ""):
            errs.append(f"status uses {w}")
    src = review.get("sources_checked", {})
    for sid, s in src.items():
        host = urlparse(s.get("url", "")).hostname
        official = host in WIZ and s["url"].startswith("https://")
        if s.get("class") == "WIZARDS_OFFICIAL" and not official:
            errs.append(f"{sid}: labelled official but not a Wizards HTTPS URL")
        if s.get("class") != "WIZARDS_OFFICIAL" and (official or s.get("class") != "NON_WIZARDS_LABELLED"):
            errs.append(f"{sid}: bad class")
    claims = {c["id"]: c for c in pack["claims"]}
    seen = set()
    for r in review.get("reviews", []):
        cid = r["claim_id"]
        if cid in seen:
            errs.append(f"{cid}: duplicate review")
        seen.add(cid)
        if cid not in claims:
            errs.append(f"{cid}: not in pack")
            continue
        if r["grade_before"] != claims[cid]["grade"]:
            errs.append(f"{cid}: grade_before != pack grade")
        if r["decision"] not in ("RETAIN", "PROPOSE_CHANGE"):
            errs.append(f"{cid}: decision")
        if r["decision"] == "RETAIN" and r["grade_after"] != claims[cid]["grade"]:
            errs.append(f"{cid}: RETAIN but grade differs")
        if r["grade_after"] not in GRADES:
            errs.append(f"{cid}: grade_after")
        if not r.get("evidence") or not r.get("finding"):
            errs.append(f"{cid}: missing evidence/finding")
        for e in r.get("evidence", []):
            if src.get(e, {}).get("class") != "WIZARDS_OFFICIAL":
                errs.append(f"{cid}: evidence {e} is not a checked Wizards source")
        for e in r.get("context_non_wizards", []):
            if src.get(e, {}).get("class") != "NON_WIZARDS_LABELLED":
                errs.append(f"{cid}: context {e} not labelled")
    pack_keys = {(c["subject"], c["predicate"], str(c["object"])) for c in pack["claims"]}
    for p in review.get("proposed_claims_not_applied", []):
        if p["proposed_grade"] not in GRADES:
            errs.append(f"{p['proposal_id']}: grade")
        if p["proposal_id"] in claims:
            errs.append(f"{p['proposal_id']}: collides with pack id")
        if not p.get("limitation") or not p.get("source_ids"):
            errs.append(f"{p['proposal_id']}: limitation/sources")
        for s in p.get("source_ids", []):
            if src.get(s, {}).get("class") != "WIZARDS_OFFICIAL":
                errs.append(f"{p['proposal_id']}: source {s} not checked Wizards")
        key = (p["subject"], p["predicate"], p["object"])
        if key in pack_keys and "corroborat" not in p["summary"].lower():
            errs.append(f"{p['proposal_id']}: already in pack")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--review", default=str(REVIEW))
    a = ap.parse_args()
    review = json.loads(Path(a.review).read_text(encoding="utf-8"))
    pack = json.loads((ROOT / review["pack_file"]).read_text(encoding="utf-8"))
    errs = audit(review, pack)
    out = {"result": "FAIL" if errs else "PASS", "reviews": len(review["reviews"]),
           "decisions": {r["claim_id"]: f"{r['decision']} {r['grade_after']}" for r in review["reviews"]},
           "proposals_not_applied": len(review["proposed_claims_not_applied"]),
           "wizards_sources_checked": sum(s["class"] == "WIZARDS_OFFICIAL" for s in review["sources_checked"].values()),
           "errors": errs}
    print(json.dumps(out, indent=1))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
