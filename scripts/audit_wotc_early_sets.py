#!/usr/bin/env python3
"""Verify a bounded Wizards-sourced 1993-2002 set-release evidence census.

Historical "mainline release" means a regular expansion/core edition described
in Wizards' year-by-year retrospective or explicit core set enumeration.
It does not assert the modern marketing term "premier" was used before 2020.
Foreign-border edition variants remain provisional, not proven excluded.
"""
import argparse
import json
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data/set_atlas"
SOURCE = DATA / "wotc_early_release_evidence_1993_2002.json"
ATLAS = DATA / "product_catalog_2026-10-29.json"
PREVIOUS = DATA / "wotc_release_classification_2026-10-29.json"
REPORT = DATA / "wotc_early_release_audit_1993_2002.json"
CUTOFF = date(2026, 10, 29)
GROUPS = {
    "historical_regular_expansion_or_core_release": 35,
    "discarded_print_run": 1,
    "localized_core_printing_variant_pending": 2,
}


def encode(doc):
    return (json.dumps(doc, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build(source, atlas, earlier):
    if source.get("schema") != 1 or source.get("as_of") != CUTOFF.isoformat():
        raise ValueError("Evidence date/schema mismatch")
    if atlas.get("snapshot_date") != CUTOFF.isoformat() or earlier.get("as_of") != CUTOFF.isoformat():
        raise ValueError("Incompatible catalog/classification cutoffs")

    candidates = {
        code for code, v in atlas["sets"].items()
        if not v.get("scryfall_set_metadata_missing")
        and v["scryfall_set_type"] in ("core", "expansion")
        and v["digital_only"] is False
        and v["release_status_as_of_cutoff"] == "released_by_cutoff"
    }
    early_candidates = {
        code for code in candidates if date.fromisoformat(atlas["sets"][code]["released_at"]).year <= 2002
    }
    seen = set()
    counts = Counter()
    result = []
    for row in source.get("records", []):
        code = row.get("code")
        if code in seen:
            raise ValueError(f"Duplicate early record: {code}")
        if code not in early_candidates:
            raise ValueError(f"Not a 1993–2002 expansion/core candidate: {code}")
        claim = row.get("claim")
        if claim not in GROUPS:
            raise ValueError(f"Unrecognized release claim for {code}: {claim}")
        primary = row.get("source")
        if urlparse(primary or "").hostname not in ("magic.wizards.com", "www.magic.wizards.com"):
            raise ValueError(f"Unverified source domain for {code}")
        if not row.get("section") or not row.get("classification_note"):
            raise ValueError(f"Missing citation section or review note for {code}")
        s = atlas["sets"][code]
        year = date.fromisoformat(s["released_at"]).year
        if year != row.get("year"):
            raise ValueError(f"Incorrect release year for {code}")
        if claim == "historical_regular_expansion_or_core_release" and row["evidence_level"] != "primary_Wizards_enumeration":
            raise ValueError(f"Unconfirmed mainline classification for {code}")
        if claim == "discarded_print_run":
            if code != "sum" or row["evidence_level"] != "explicit_Wizards_exclusion":
                raise ValueError("Discarded-print-run exception lacks direct source")
        if claim == "localized_core_printing_variant_pending":
            if code not in {"fbb", "4bb"} or row["evidence_level"] != "provisional_structural_inference":
                raise ValueError("Foreign-border variant incorrectly promoted to certainty")
        counts[claim] += 1
        seen.add(code)
        result.append({
            "code": code, "name": s["name"], "release_year": year,
            "scryfall_type": s["scryfall_set_type"], "released_at": s["released_at"],
            "classification": claim, "review_status": row["evidence_level"],
            "source_url": primary, "source_section": row["section"],
            "secondary_source_url": row.get("auxiliary_source"),
            "reason": row["classification_note"],
            "included_in_historical_regular_release_count":
                claim == "historical_regular_expansion_or_core_release"
        })

    if seen != early_candidates:
        raise ValueError(f"Unclassified early candidate codes: {sorted(early_candidates - seen)}")
    if dict(counts) != GROUPS:
        raise ValueError(f"Historical categorization no longer matches evidence: {dict(counts)}")
    prev = earlier["summary"]
    if prev["scryfall_released_nondigital_expansion_core_candidates_all_history"] != 142:
        raise ValueError("Earlier candidate total changed")
    if prev["wotc_reviewed_released_main_set_codes_2023_2026"] != 21:
        raise ValueError("Earlier reviewed main total changed")
    if prev["reviewed_expansion_core_auxiliary_not_a_main_release"] != 2:
        raise ValueError("Earlier reviewed auxiliary total changed")
    remaining_after = prev["unreviewed_released_nondigital_expansion_core_candidates"] - len(seen)
    if remaining_after != 81:
        raise ValueError("Expected remaining 2003–2022 candidate total changed")
    known_main = 21 + counts["historical_regular_expansion_or_core_release"]
    documented_others = 2 + counts["discarded_print_run"]
    provisional = counts["localized_core_printing_variant_pending"]
    candidate_undetermined = remaining_after + provisional
    if known_main + documented_others + candidate_undetermined != 142:
        raise ValueError("Candidate partition does not reconcile")
    report = {
        "schema": 1, "as_of": CUTOFF.isoformat(),
        "definition": "Historical regular expansion/core releases documented by Wizards; not retroactive marketing claims about the term premier.",
        "source_files": [SOURCE.name, ATLAS.name, PREVIOUS.name],
        "period": "1993-2002",
        "period_candidate_count": len(early_candidates),
        "period_evidence_counts": dict(sorted(counts.items())),
        "period_reviewed_regular_mainline": counts["historical_regular_expansion_or_core_release"],
        "period_confirmed_not_independent_mainline": counts["discarded_print_run"],
        "period_provisional_variants": provisional,
        "combined_full_snapshot": {
            "candidate_expansion_core_total": 142,
            "reviewed_mainline_1993_2002_plus_2023_2026": known_main,
            "directly_documented_auxiliary_or_discarded": documented_others,
            "provisional_foreign_border_variants": provisional,
            "not_yet_reviewed_2003_2022": remaining_after,
            "candidate_unresolved_including_two_provisionals": candidate_undetermined,
            "all_time_mainline_total_certified": False,
        },
        "records": sorted(result, key=lambda x: (x["released_at"], x["code"])),
        "caveats": [
            "Wizards' year-by-year randomized booster article is a retrospective, not a formal modern premier-set designation.",
            "Scryfall expanded/core categorizations are independent of Wizards' terminology.",
            "The Foreign Black Border and Fourth Edition Foreign Black Border codes are provisional variants pending direct primary-source review.",
            "Summer Magic is a scrapped Revised printing with accidental limited distribution, not a regular independent core release.",
            "Chronicles, Renaissance, Portal and Unglued are outside the Scryfall expansion/core candidate denominator; that does not mean they were never products.",
            "The 81 remaining 2003–2022 candidates require separate reviewed sources before an all-time mainline count."
        ],
    }
    return report


def run(write=False):
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    atlas = json.loads(ATLAS.read_text(encoding="utf-8"))
    earlier = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    out = encode(build(source, atlas, earlier))
    if write:
        REPORT.write_bytes(out)
    elif not REPORT.exists() or REPORT.read_bytes() != out:
        raise ValueError("Saved early-release census does not match the evidence inputs")
    print(json.dumps(json.loads(out)["combined_full_snapshot"], indent=2, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    run(parser.parse_args().write)
