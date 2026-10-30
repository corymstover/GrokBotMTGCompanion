#!/usr/bin/env python3
"""Offline Phase 1B Scryfall product-family research queue lookup.

Research cohort != Wizards-classified product or premier-set determination.
Examples:
  python3 scripts/product_family_lookup.py --summary
  python3 scripts/product_family_lookup.py --cohort draft_and_starter_variants
  python3 scripts/product_family_lookup.py --type masters --only-pending --all
  python3 scripts/product_family_lookup.py --parent afr --all
  python3 scripts/product_family_lookup.py --code ltr
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "data/set_atlas/product_family_triage_2026-10-29.json"
SOURCE_REVIEW = ROOT / "data/set_atlas/draft_starter_primary_audit_2026-10-29.json"
SECOND_SOURCE_REVIEW = ROOT / "data/set_atlas/draft_starter_batch2_audit_2026-10-29.json"
REPRINT_SOURCE_REVIEW = ROOT / "data/set_atlas/reprint_curated_source_audit_2026-10-29.json"


def apply_source_overlay(data, verified):
    """Use source-backed verified additions without rewriting the dated v2.1 triage."""
    if verified["snapshot_date"] != data["snapshot_date"]:
        raise ValueError("Product review overlay snapshot/date mismatch")
    updates = {x["code"]: x for x in verified["newly_wizards_reviewed"]}
    if len(updates) != verified["reviewed_batch_size"] or len(updates) != 23:
        raise ValueError("Incomplete duplicate or malformed source review overlay")
    entries = []
    patched = set()
    for entry in data["all_848_released_nondigital_other_type_records"]:
        new = dict(entry)
        src = updates.get(new["code"])
        if src is not None:
            if new["wizards_individual_source_review"] or src["scryfall_type"] != new["scryfall_set_type"]:
                raise ValueError(f"Source review overwrite or category mismatch: {new['code']}")
            new["wizards_individual_source_review"] = True
            new["review_status"] = "wizards_primary_source_batch_reviewed"
            new["wizards_primary_source"] = src["wizards_source_url"]
            new["wizards_review_product_group"] = src["wizards_product_group"]
            new["verified_evidence_note"] = src["evidence_note"]
            new["new_card_legality_date_claim"] = src.get("new_card_legality_date_claim")
            patched.add(new["code"])
        entries.append(new)
    if patched != set(updates):
        raise ValueError(f"Source overlay contains nonmatching codes: {sorted(set(updates) - patched)}")
    revised = dict(data)
    revised["all_848_released_nondigital_other_type_records"] = entries
    revised["wizards_reviewed_examples"] = verified["cumulative_wizards_source_reviewed_other_category_codes"]
    revised["metadata_only_pending_wizards_individual_review"] = verified["cumulative_source_pending_other_category_codes"]
    revised["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [x for x in entries
                   if x["metadata_cohort_not_official_classification"] == cohort]
        revised["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(x["wizards_individual_source_review"]) for x in members),
            "needs_individual_review": sum(not x["wizards_individual_source_review"] for x in members),
            "explicit_parent_links": sum(bool(x["parent_set_code_explicit_only"]) for x in members),
        }
    if len(entries) != 848 or len([x for x in entries if x["wizards_individual_source_review"]]) != 35:
        raise ValueError("Cumulative reviewed code conservation failed")
    return revised


def apply_second_source_overlay(data, verified):
    """Add eight graded product-family citations without changing prior snapshots."""
    if verified["cutoff"] != data["snapshot_date"]:
        raise ValueError("Review dates incompatible")
    updates = {x["code"]: x for x in verified["newly_sourced_family_evidence"]}
    if len(updates) != verified["new_wizards_family_evidence_count"] or len(updates) != 8:
        raise ValueError("New review contains duplicated or absent source codes")
    patched = set()
    result = []
    for item in data["all_848_released_nondigital_other_type_records"]:
        record = dict(item)
        src = updates.get(record["code"])
        if src:
            if record["wizards_individual_source_review"]:
                raise ValueError(f"Attempt to replace previous official review: {record['code']}")
            if src["scryfall_set_type"] != record["scryfall_set_type"]:
                raise ValueError(f"Official reviewed category drift for {record['code']}")
            record.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_family_source_with_evidence_grade",
                "wizards_primary_source": src["direct_official_article_url"],
                "wizards_review_product_group": src["product_family_wizards_supported"],
                "wizards_source_grade": src["wizards_family_evidence_grade"],
                "wizards_code_explicitly_confirmed": src["wizards_explicitly_printed_set_code"],
                "verified_evidence_note": src["wizards_article_supports"],
            })
            patched.add(record["code"])
        result.append(record)
    if patched != set(updates) or len(result) != 848:
        raise ValueError("Graded citations do not match existing Scryfall codes")
    current = dict(data)
    current["all_848_released_nondigital_other_type_records"] = result
    current["wizards_reviewed_examples"] = verified[
        "cumulative_outside_category_codes_with_wizards_source_family_evidence"]
    current["metadata_only_pending_wizards_individual_review"] = verified[
        "cumulative_outside_category_codes_individual_wizards_source_pending"]
    current["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [r for r in result if r["metadata_cohort_not_official_classification"] == cohort]
        current["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review": sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links": sum(bool(r["parent_set_code_explicit_only"]) for r in members),
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in result) != 43:
        raise ValueError("Cumulative official source records not 43")
    return current


def apply_reprint_source_overlay(data, report):
    """Only update the exact 28 new Wizards-family cited codes; preserve history."""
    if report["cutoff"] != data["snapshot_date"]:
        raise ValueError("Incompatible research snapshot")
    rows = {x["code"]:x for x in report["newly_sourced_family_evidence"]}
    if len(rows) != report["source_reviewed_this_batch"] or len(rows) != 28:
        raise ValueError("Unexpected duplicate/missing reprint source rows")
    result = []
    changed = set()
    for record in data["all_848_released_nondigital_other_type_records"]:
        item = dict(record)
        src = rows.get(item["code"])
        if src:
            if item["wizards_individual_source_review"]:
                raise ValueError(f"Cannot replace previously verified review: {item['code']}")
            if item["scryfall_set_type"] != src["scryfall_set_type"]:
                raise ValueError(f"Scryfall category changed for {item['code']}")
            item.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_reprint_curated_product_family_reviewed",
                "wizards_primary_source": src["wizards_source_url"],
                "wizards_review_product_group": src["wizards_product_family"],
                "wizards_source_grade": src["evidence_grade"],
                "wizards_code_explicitly_confirmed": src["wizards_explicit_scryfall_code"],
                "verified_evidence_note": src["source_note"],
                "wizards_premier_status_certified": False
            })
            changed.add(item["code"])
        result.append(item)
    if changed != set(rows) or len(result) != 848:
        raise ValueError("Review overlay failed total exact-code coverage")
    out = dict(data)
    out["all_848_released_nondigital_other_type_records"] = result
    out["wizards_reviewed_examples"] = report["cumulative_wizards_family_evidence_codes"]
    out["metadata_only_pending_wizards_individual_review"] = report["cumulative_pending_codes"]
    out["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [r for r in result if r["metadata_cohort_not_official_classification"] == cohort]
        out["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review": sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links": sum(bool(r["parent_set_code_explicit_only"]) for r in members)
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in result) != 71:
        raise ValueError("Review overlay conservation not 71")
    return out


def load_current_index():
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    if SOURCE_REVIEW.exists():
        verified = json.loads(SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_source_overlay(data, verified)
    if SECOND_SOURCE_REVIEW.exists():
        second = json.loads(SECOND_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_second_source_overlay(data, second)
    if REPRINT_SOURCE_REVIEW.exists():
        report = json.loads(REPRINT_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_reprint_source_overlay(data, report)
    return data


def select(data, code=None, cohort=None, set_type=None, parent=None,
           only_pending=False, priority=None):
    rows = []
    for item in data["all_848_released_nondigital_other_type_records"]:
        if code is not None and item["code"] != code.lower():
            continue
        if cohort is not None and item["metadata_cohort_not_official_classification"] != cohort:
            continue
        if set_type is not None and item["scryfall_set_type"] != set_type:
            continue
        if parent is not None and item["parent_set_code_explicit_only"] != parent.lower():
            continue
        if only_pending and item["wizards_individual_source_review"]:
            continue
        if priority is not None and item["research_priority_1_highest"] != priority:
            continue
        rows.append(item)
    return sorted(rows, key=lambda x: (
        x["research_priority_1_highest"], x["scryfall_set_type"],
        x["scryfall_release_or_first_card_date"] or "", x["code"]))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--summary", action="store_true")
    p.add_argument("--code")
    p.add_argument("--cohort")
    p.add_argument("--type", dest="set_type")
    p.add_argument("--parent")
    p.add_argument("--only-pending", action="store_true")
    p.add_argument("--priority", type=int, choices=(1, 2, 3, 4))
    p.add_argument("--all", action="store_true")
    args = p.parse_args()
    data = load_current_index()
    if args.summary:
        print(json.dumps({
            "snapshot": data["snapshot_date"],
            "metadata_research_cohorts": data["metadata_research_cohorts"],
            "cohort_review_progress": data["cohort_review_progress"],
            "reviewed": data["wizards_reviewed_examples"],
            "individual_source_review_pending": data["metadata_only_pending_wizards_individual_review"],
            "metadata_not_premier_status": True,
        }, indent=2, ensure_ascii=False))
        return
    results = select(
        data, code=args.code, cohort=args.cohort, set_type=args.set_type,
        parent=args.parent, only_pending=args.only_pending, priority=args.priority
    )
    print(json.dumps({
        "snapshot": data["snapshot_date"], "matches": len(results),
        "shown": len(results if args.all else results[:30]),
        "research_cohorts_not_official_classification": True,
        "results": results if args.all else results[:30],
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
