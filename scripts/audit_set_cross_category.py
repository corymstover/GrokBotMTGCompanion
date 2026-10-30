#!/usr/bin/env python3
"""Phase 1B: reproducible cross-category product audit (October 29, 2026).

The Scryfall set_type field is not a Wizards "premier" classifier.
This report summarizes ALL source-category codes and separately classifies
only a small set of official-evidence-backed non-expansion/core products.
Foreign-border variants remain provisional: third-party documentation alone
does not close a primary-source certification gate.
"""
import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
ATLAS = ROOT / "data/set_atlas"
CATALOG = ATLAS / "product_catalog_2026-10-29.json"
EVIDENCE = ATLAS / "cross_category_evidence_2026-10-29.json"
EARLY = ATLAS / "wotc_early_release_audit_1993_2002.json"
MID = ATLAS / "wotc_mid_release_audit_2003_2022.json"
REPORT = ATLAS / "cross_category_audit_2026-10-29.json"
REQUIRED_CODES = {"ltr", "ltc", "acr", "mh1", "mh2", "mh3", "cmm",
                  "rvr", "inr", "j22", "pip", "cmr"}
GROUPS = {
    "modern_legal_full_booster_not_2023_standard_premier",
    "modern_legal_nonstandard_universes_beyond",
    "modern_horizons_supplemental",
    "masters_reprint_product",
    "remastered_reprint_product",
    "jumpstart_special_product",
    "universes_beyond_commander_product",
    "commander_draft_product"
}


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build(catalog, evidence, early, mid):
    if (catalog["snapshot_date"] != "2026-10-29"
            or evidence["as_of"] != "2026-10-29"
            or mid["as_of"] != "2026-10-29"):
        raise ValueError("Cross-category source date mismatch")
    if (early["combined_full_snapshot"]["candidate_expansion_core_total"] != 142
            or mid["combined_candidate_classification"]["scryfall_released_nondigital_expansion_core"] != 142):
        raise ValueError("Existing category census drifted")
    if mid["combined_candidate_classification"]["wotc_supported_historical_regular_or_mainline_releases"] != 136:
        raise ValueError("Existing vetted historical subset changed")

    policy = evidence["premier_reference"]
    if urlparse(policy["source"]).hostname != "magic.wizards.com" or urlparse(policy["policy_update"]).hostname != "magic.wizards.com":
        raise ValueError("Official premier definition and policy source missing")
    total = len(catalog["sets"])
    partitions = Counter()
    category_breakdown = Counter()
    category_examples = {}
    for code, v in sorted(catalog["sets"].items()):
        if v.get("scryfall_set_metadata_missing"):
            raise ValueError(f"Missing Scryfall set metadata for {code}")
        category = v["scryfall_set_type"]
        category_breakdown[category] += 1
        if category not in category_examples:
            category_examples[category] = {"code": code, "name": v["name"]}
        if v["release_status_as_of_cutoff"] == "announced_future":
            partitions["future_announced"] += 1
        elif v["digital_only"]:
            partitions["digital_only_released"] += 1
        elif category in ("expansion", "core"):
            partitions["released_nondigital_expansion_core"] += 1
        else:
            partitions["released_nondigital_other_categories"] += 1
    if total != 1062 or sum(partitions.values()) != total:
        raise ValueError("Set status/category buckets fail whole-archive conservation")
    if partitions["released_nondigital_expansion_core"] != 142:
        raise ValueError("Incorrect previously certified category denominator")
    # All other paper set codes are a discovery pool, NOT 848 premier products.
    if partitions["released_nondigital_other_categories"] != 848:
        raise ValueError("Cross-category dated paper products count changed")

    reviewed = []
    seen = set()
    for item in evidence["records"]:
        code = item["code"]
        if code in seen or code not in REQUIRED_CODES:
            raise ValueError(f"Duplicate or unsupported code in official evidence: {code}")
        s = catalog["sets"].get(code)
        if s is None or s["scryfall_set_type"] in ("expansion", "core"):
            raise ValueError(f"Not an outside-expansion/core set: {code}")
        if s["digital_only"] or s["release_status_as_of_cutoff"] != "released_by_cutoff":
            raise ValueError(f"Unreleased or digital reviewed set: {code}")
        if item["group"] not in GROUPS or not item["section"] or not item["evidence_note"]:
            raise ValueError(f"Missing bounded review evidence: {code}")
        if urlparse(item["source"]).hostname != "magic.wizards.com":
            raise ValueError(f"Source is not Wizards for {code}")
        seen.add(code)
        reviewed.append({
            "code": code, "name": s["name"],
            "scryfall_set_type": s["scryfall_set_type"],
            "release_date": s["released_at"],
            "product_group": item["group"], "source_url": item["source"],
            "source_section": item["section"], "note": item["evidence_note"],
            "premier_inference": "not_a_2023_2024_standard_main_release",
        })
    if seen != REQUIRED_CODES:
        raise ValueError(f"Missing official-source reviews: {sorted(REQUIRED_CODES - seen)}")
    leads = evidence["localized_printing_leads"]
    if {x["code"] for x in leads} != {"fbb", "4bb"} or len(leads) != 2:
        raise ValueError("Historical localized variants missing or duplicated")
    for item in leads:
        if (item["status"] != "external_corroboration_only_primary_source_pending"
                or item["source_type"] != "third_party_specialist"
                or urlparse(item["source"]).hostname == "magic.wizards.com"):
            raise ValueError("Localized variant was silently promoted to Wizards-certified")
    if mid["combined_candidate_classification"]["provisional_border_language_variants"] != 2:
        raise ValueError("Conflicting status for localized printing variants")

    return {
        "schema": 1, "snapshot_date": "2026-10-29",
        "purpose": "Audit officially sourced non-premier full products outside the Scryfall expansion/core set type, while keeping a complete categorical census",
        "source_catalog": CATALOG.name, "primary_evidence": EVIDENCE.name,
        "premier_policy": policy,
        "all_code_census": {
            "total_all_scryfall_codes": total,
            "status_exclusive_partitions": dict(sorted(partitions.items())),
            "scryfall_category_totals_including_digital_and_future": dict(sorted(category_breakdown.items())),
            "category_representative_examples": dict(sorted(category_examples.items())),
        },
        "reviewed_non_expansion_core_products": sorted(reviewed, key=lambda x: x["code"]),
        "reviewed_count": len(reviewed),
        "unreviewed_released_nondigital_other_category_codes": partitions["released_nondigital_other_categories"] - len(reviewed),
        "localized_printing_variants": leads,
        "caveats": [
            "The 848 released paper set codes outside expansion/core include supplemental, tokens, promos and numerous non-premier product families; they are not 848 standalone booster sets.",
            "The 12 reviewed outside-category records are bounded examples, not a certification of every code in the 848-code discovery pool.",
            "The 136 reviewed expansion/core regular/mainline codes remain a category-specific count, not a universal 1993–2026 premier census.",
            "Wizards' 2022 premier/Standard definition and 2025 forward-only Universes Beyond policy must both be applied with dated context.",
            "Neither Scryfall set_type nor mere Modern legality proves an item to be a premier release.",
            "Specialist sources corroborate FBB/4BB localized edition relationships but the project still lacks direct Wizards verification; those statuses remain provisional.",
            "This is a dated October 29, 2026 catalog, not a current live legality or product count."
        ]
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    inputs = [json.loads(path.read_text(encoding="utf-8")) for path in (CATALOG, EVIDENCE, EARLY, MID)]
    result = build(*inputs)
    raw = encode(result)
    if args.write:
        REPORT.write_bytes(raw)
    elif not REPORT.exists() or REPORT.read_bytes() != raw:
        raise ValueError("Committed cross-category report is not reproducible")
    print(json.dumps({**result["all_code_census"]["status_exclusive_partitions"],
                      "reviewed_examples": result["reviewed_count"],
                      "unreviewed_other_category_codes": result["unreviewed_released_nondigital_other_category_codes"]}, indent=2))


if __name__ == "__main__":
    main()
