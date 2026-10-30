#!/usr/bin/env python3
"""Second bounded Wizards-backed draft/starter review, preserving prior snapshots.

Review levels distinguish exact Wizards code evidence from Wizards product-family
evidence crosswalked to a Scryfall set code. This does NOT certify every
historic Magic release or a product's format legality.
"""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
ATLAS = ROOT / "data/set_atlas"
OLDER = ATLAS / "draft_starter_primary_audit_2026-10-29.json"
EVIDENCE = ATLAS / "draft_starter_evidence_batch2_2026-10-29.json"
BASE = ATLAS / "product_family_triage_2026-10-29.json"
OUT = ATLAS / "draft_starter_batch2_audit_2026-10-29.json"
KNOWN = {"h17", "h1r", "h2r", "hho", "ptg", "ulst", "unk", "w17"}
ALLOWED_GRADES = {
    "exact_code_and_group_primary",
    "exact_product_primary",
    "product_family_primary_code_crosswalk_scryfall",
}


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build(previous, evidence, base):
    if evidence.get("schema") != 1 or evidence.get("cutoff") != "2026-10-29":
        raise ValueError("Unsupported evidence snapshot")
    if previous.get("snapshot_date") != evidence["cutoff"] or base.get("snapshot_date") != evidence["cutoff"]:
        raise ValueError("Incompatible prior source dates")
    if (previous["cumulative_wizards_source_reviewed_other_category_codes"],
        previous["cumulative_source_pending_other_category_codes"],
        previous["draft_starter_pending_after_batch"]) != (35, 813, 21):
        raise ValueError("Prior 23-code review was mutated")
    pending = set(previous["draft_starter_pending_codes"])
    older_all_pending = {r["code"]: r for r in previous["remaining_source_pending_queue_all_other_categories"]}
    base_index = {r["code"]: r for r in base["all_848_released_nondigital_other_type_records"]}
    if len(older_all_pending) != 813 or len(base_index) != 848:
        raise ValueError("Prior queue or complete Scryfall index has duplicates/omissions")
    seen = set()
    reviewed = []
    for row in evidence.get("records", []):
        code = row.get("code")
        if code in seen:
            raise ValueError(f"Duplicated set code in primary ledger: {code}")
        if code not in pending or code not in older_all_pending:
            raise ValueError(f"Not a pending reviewed draft/starter code: {code}")
        if row.get("grade") not in ALLOWED_GRADES:
            raise ValueError(f"Unrecognized evidence level: {code}")
        parsed = urlparse(row.get("url", ""))
        if parsed.scheme != "https" or parsed.hostname not in ("magic.wizards.com", "www.magic.wizards.com"):
            raise ValueError(f"Not a direct Wizards article: {code}")
        if not row.get("section") or len(row.get("detail", "")) < 40:
            raise ValueError(f"Insufficient source context: {code}")
        if not row.get("group"):
            raise ValueError(f"Missing specific product group: {code}")
        s = base_index[code]
        if s["wizards_individual_source_review"] or s["metadata_cohort_not_official_classification"] != "draft_and_starter_variants":
            raise ValueError(f"Previously approved code or wrong cohort: {code}")
        if s["scryfall_release_or_first_card_date"] > evidence["cutoff"]:
            raise ValueError(f"Premature future-date review: {code}")
        seen.add(code)
        reviewed.append({
            "code": code, "name": s["name"],
            "scryfall_set_type": s["scryfall_set_type"],
            "wizards_family_evidence_grade": row["grade"],
            "product_family_wizards_supported": row["group"],
            "direct_official_article_url": row["url"],
            "direct_official_article_section": row["section"],
            "wizards_article_supports": row["detail"],
            "date_origin": "Scryfall /sets released_at from earlier snapshot",
            "scryfall_date": s["scryfall_release_or_first_card_date"],
            "scryfall_parent_set_code": s["parent_set_code_explicit_only"],
            "wizards_explicitly_printed_set_code": row["grade"] == "exact_code_and_group_primary",
            "independent_premier_status_verified": False,
            "individual_card_legality_date_verified": False,
        })
    if seen != KNOWN or len(reviewed) != 8:
        raise ValueError(f"Batch must contain exactly eight bounded codes; missing {sorted(KNOWN-seen)}")
    remaining = sorted(pending-seen)
    if len(remaining) != 13:
        raise ValueError("Draft/starter source backlog wrong")
    pending_queue = [row for row in previous["remaining_source_pending_queue_all_other_categories"]
                     if row["code"] not in seen]
    if len(pending_queue) != 805:
        raise ValueError("Cumulative outside-category source queue wrong")
    if len(reviewed) + previous["cumulative_wizards_source_reviewed_other_category_codes"] + len(pending_queue) != 848:
        raise ValueError("Lost or duplicated Scryfall code")
    return {
        "schema": 1, "cutoff": evidence["cutoff"], "source_evidence": EVIDENCE.name,
        "previous_report": OLDER.name,
        "new_wizards_family_evidence_count": len(seen),
        "new_exact_code_printed_by_wizards": sum(r["wizards_explicitly_printed_set_code"] for r in reviewed),
        "new_wizards_family_evidence_with_scryfall_crosswalk":
            len(seen)-sum(r["wizards_explicitly_printed_set_code"] for r in reviewed),
        "all_outside_category_codes": 848,
        "cumulative_outside_category_codes_with_wizards_source_family_evidence": 43,
        "cumulative_outside_category_codes_individual_wizards_source_pending": 805,
        "draft_starter_codes_source_pending": remaining,
        "draft_starter_source_pending_count": 13,
        "newly_sourced_family_evidence": sorted(reviewed, key=lambda x: x["code"]),
        "still_source_pending_queue": pending_queue,
        "caveats": [
            "This evidence batch establishes product families; only sources that explicitly state a Scryfall code receive exact-code Wizards provenance.",
            "A Wizards family explanation plus a Scryfall code crosswalk is not the same as Wizards independently printing/confirming that code.",
            "43 cumulative outside-category code reviews means documented Wizards product-family support, NOT 43 premier releases or individual card legalities.",
            "The remaining 13 draft/starter codes and 805 all-category codes remain pending official primary-source checks.",
            "The original 12-source and 23-source evidence snapshots remain unchanged; only derived offline read layers incorporate this batch.",
            "All source and cutoff dates are as-of October 29, 2026 and are not silently updated.",
        ],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    obj = build(*(json.loads(path.read_text(encoding="utf-8")) for path in (OLDER, EVIDENCE, BASE)))
    b = encode(obj)
    if args.write:
        OUT.write_bytes(b)
    elif not OUT.exists() or OUT.read_bytes() != b:
        raise ValueError("Saved second batch differs from reproducible code/evidence audit")
    print(json.dumps({
        "new": obj["new_wizards_family_evidence_count"],
        "with_explicit_wizards_set_code": obj["new_exact_code_printed_by_wizards"],
        "cumulative_reviewed": obj["cumulative_outside_category_codes_with_wizards_source_family_evidence"],
        "source_pending": obj["cumulative_outside_category_codes_individual_wizards_source_pending"],
        "draft_pending": obj["draft_starter_codes_source_pending"],
    }, indent=2))


if __name__ == "__main__":
    main()
