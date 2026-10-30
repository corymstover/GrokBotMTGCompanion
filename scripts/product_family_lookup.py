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
    data = json.loads(INDEX.read_text(encoding="utf-8"))
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
