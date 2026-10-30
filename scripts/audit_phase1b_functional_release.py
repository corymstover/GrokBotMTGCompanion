#!/usr/bin/env python3
"""Reproducible, explicitly qualified Phase 1B Set Atlas release coverage.

Certifies the committed historical English-paper offline query/export surface.
It must never imply full cross-snapshot ID equality, official all-time premier
counts, complete story/card lore relationships or 555 optional source reviews.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ATLAS = ROOT / "data" / "set_atlas"
FAST = ATLAS / "phase1b_fasttrack_readiness_2026-10-29.json"
EXPORT = ATLAS / "phase1b_export_acceptance_2026-10-29.json"
SCOPE = ATLAS / "phase1b_release_scope_story_bridge_2026-10-29.json"
CROSS = ATLAS / "cross_category_audit_2026-10-29.json"
HIST = ATLAS / "historical_shard_audit_2026-10-29.json"
OUTPUT = ATLAS / "phase1b_qualified_functional_release_2026-10-29.json"


def encode(result):
    return (json.dumps(result, sort_keys=True, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def build():
    fast, export, scope, cross, hist = [json.loads(path.read_text(encoding="utf-8"))
                                      for path in (FAST, EXPORT, SCOPE, CROSS, HIST)]
    if [r["as_of"] for r in (fast, export, scope)] != ["2026-10-29"] * 3:
        raise ValueError("Fast track, exports and category sources have conflicting dates")
    if (fast["all_codes"], scope["all_set_codes"],
            export["all_set_codes_full_export_checked"],
            cross["all_code_census"]["total_all_scryfall_codes"]) != (1062,) * 4:
        raise ValueError("1,062-set catalog scope is not conserved")
    if (fast["released_english_paper_as_of_cutoff"],
            export["released_english_paper_printing_rows_exported"],
            hist["released_english_paper"]) != (106855,) * 3:
        raise ValueError("Default released English printing surface changed")
    if export["historical_printing_ids_reverse_joined"] != hist["printing_ids"] or hist["printing_ids"] != 119509:
        raise ValueError("Published historical printing join is incomplete")
    if export["stable_oracle_ids_reverse_joined"] != hist["stable_oracle_ids_indexed"] or hist["stable_oracle_ids_indexed"] != 39099:
        raise ValueError("Published historical Oracle identity index drift")
    if (fast["published_index_files_hash_verified"],
            fast["scryfall_product_metadata_codes_joined"],
            scope["story_series_with_primary_title_links"]) != (32, 1062, 12):
        raise ValueError("Index hashes, set metadata or limited story bridge is incomplete")
    if (fast["non_blocking_other_category_family_research_pending"] != 555 or
            fast["source_backed_other_category_families"] != 293):
        raise ValueError("Previously documented optional product-family research is not preserved")
    required = {"historical_regular_mainline": 136, "documented_auxiliary_or_discarded": 4,
                "localized_variant_provisional": 2, "released_paper_other_category": 848,
                "released_digital_only": 62, "future_announced": 10}
    if (scope["scope_counts_exclusive"] != required or
            scope["all_time_premier_set_count_certified"] is not False or
            len(scope["set_scope_records"]) != 1062):
        raise ValueError("Release scope categories have been silently recast")
    if export["all_1062_printing_and_unique_card_exports"] != "PASS":
        raise ValueError("Whole catalog export audit not accepted")
    return {
        "schema": 1,
        "release_name": "Phase 1B Set & Printing Atlas — qualified functional checkpoint",
        "as_of": "2026-10-29", "artifact_scope": "GitHub committed October 28 historical indexes with October 29 released cutoff",
        "gate": "QUALIFIED_OFFLINE_FUNCTIONAL_RELEASE_READY",
        "verified_features": {
            "all_set_codes_categorized_and_queryable": 1062,
            "all_set_codes_printings_and_unique_card_exports_pass": 1062,
            "historical_printing_ids_exactly_reverse_joined": 119509,
            "historical_stable_oracle_ids_reverse_joined": 39099,
            "released_english_paper_printing_rows": 106855,
            "default_filter_zero_row_but_valid_set_codes": 105,
            "historical_lookup_index_hashes_verified": 32,
            "set_codes_joined_to_scryfall_metadata": 1062,
            "curated_direct_wizards_story_series_links": 12,
        },
        "exclusive_set_code_scopes": required,
        "optional_product_family_evidence": {
            "wizards_primary_sourced_other_family_codes": 293,
            "separately_preserved_source_pending_other_family_codes": 555,
            "release_blocker": False,
        },
        "release_limitations": [
            "The original October 28 bulk source bytes are not present; committed historical shards and their lookup indexes are audited, not a reconstructed original bulk.",
            "October 29 new-bulk and October 28 historical released English-paper per-set counts agree; exact ID equality between different dated bulk snapshots is unproven.",
            "The 136 reviewed expansion/core regular/mainline classification is not a universal Wizards all-time premier-set total.",
            "Other released paper codes include tokens, promos, alternate printings and product components; they are not separate physical expansion boxes.",
            "The 12 story links reflect title-matched official story publication series, not individual card canon or in-universe event chronology.",
            "555 optional promo/other product-family primary-source reviews remain open and cannot be described as officially certified.",
            "This release is snapshot-dated and does not make claims about later MTG products, bans, rules or releases.",
            "Repository-wide tests can require unrelated Grixis data fixtures, optional pytest installation and private/full snapshot inputs; this gate uses relevant Phase 1B and GitHub Grixis CI.",
        ],
        "acceptance_commands": [
            "python3 scripts/audit_phase1b_fasttrack.py",
            "python3 scripts/audit_phase1b_export_acceptance.py",
            "python3 scripts/audit_phase1b_release_scope.py",
            "python3 scripts/audit_phase1b_functional_release.py",
            "python3 -m unittest discover -s tests -p 'test_*set*.py' -q",
            "python3 -m unittest discover -s tests -p 'test_*sources.py' -q",
            "python3 -m unittest discover -s tests -p 'test_phase1b*.py' -q",
            "python3 scripts/audit_set_product_links.py --check",
            "GitHub focused Grixis mechanics validation (separate exact-head CI)",
        ],
        "release_policy": "Functional Set Atlas lookup/export coverage is available with stated limits. Do not upgrade exact cross-snapshot-ID, global premier-set, independent product or lore/canon completeness claims without new evidence.",
        "source_reports": [str(p.relative_to(ROOT)) for p in (FAST, EXPORT, SCOPE, CROSS, HIST)],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    report = build()
    raw = encode(report)
    if args.write:
        OUTPUT.write_bytes(raw)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != raw:
        raise ValueError("Qualified release checkpoint not reproducible from committed audits")
    print(json.dumps({"gate": report["gate"],
                      "all_set_codes": report["verified_features"]["all_set_codes_categorized_and_queryable"],
                      "open_optional_product_research": report["optional_product_family_evidence"]["separately_preserved_source_pending_other_family_codes"]},
                     sort_keys=True))


if __name__ == "__main__":
    main()
