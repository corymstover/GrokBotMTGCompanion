#!/usr/bin/env python3
"""Rebuild fourteen historical specialty-box and premium-deck source reviews."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

DATA = Path(__file__).resolve().parent.parent / "data" / "set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREV = DATA / "commander_modern_source_audit_2026-10-29.json"
LEDGER = DATA / "boxed_specialty_sources_2006_2022.json"
OUT = DATA / "boxed_specialty_source_audit_2026-10-29.json"
REQUIRED = {"cst", "h09", "pd2", "pd3", "md1", "e02", "gk1", "g18", "gnt",
            "gk2", "gn2", "q06", "q07", "gn3"}
EXPLICIT_WIZARDS_CODES = {"h09", "pd2", "pd3", "md1"}
EXPECTED_SHARED_URL = {"g18", "gnt"}
COHORT = "preconstructed_and_boxed"


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build(base, previous, evidence):
    if (base.get("snapshot_date"), previous.get("cutoff"), evidence.get("cutoff")) != (
            "2026-10-29", "2026-10-29", "2026-10-29"):
        raise ValueError("Incompatible source/metadata snapshot")
    if (previous.get("cumulative_family_source_backed_codes"),
            previous.get("cumulative_source_pending_codes"),
            previous.get("boxed_source_pending_after_batch")) != (151, 697, 30):
        raise ValueError("Modern Commander prior source audit changed")
    pending = previous["remaining_source_pending_queue"]
    pending_codes = {r["code"] for r in pending}
    catalog = {r["code"]: r for r in base["all_848_released_nondigital_other_type_records"]}
    if len(pending) != 697 or len(pending_codes) != 697 or len(catalog) != 848:
        raise ValueError("Catalog or research queue lost records")
    reviewed = []
    seen = set()
    url_codes = {}
    for source in evidence["records"]:
        code = source.get("code")
        if code in seen:
            raise ValueError("Duplicate specialty box source record")
        if code not in REQUIRED or code not in pending_codes:
            raise ValueError(f"Unsupported or previously sourced specialty code: {code}")
        url = source.get("official_url", "")
        parts = urlparse(url)
        if (parts.scheme != "https" or parts.hostname not in
                ("magic.wizards.com", "www.magic.wizards.com", "mtg-jp.com") or
                not (parts.path.startswith("/en/news/") or parts.path.startswith("/products/"))):
            raise ValueError(f"Not an approved direct official product/article URL: {code}")
        codes_for_url = url_codes.setdefault(url, set())
        codes_for_url.add(code)
        section = source.get("source_section", "")
        if len(section) < 34:
            raise ValueError(f"Official section insufficiently specific for {code}")
        grade = source.get("source_grade")
        if grade not in ("named_product_family_crosswalk", "official_product_code_and_release"):
            raise ValueError(f"Unsupported evidence grade for {code}")
        if (grade == "official_product_code_and_release") != (code in EXPLICIT_WIZARDS_CODES):
            raise ValueError(f"Unsupported printed-code evidence assertion: {code}")
        if code in EXPLICIT_WIZARDS_CODES and (code.upper() not in section or parts.hostname != "mtg-jp.com"):
            raise ValueError(f"Official three-letter code not supported: {code}")
        metadata = catalog[code]
        if metadata["metadata_cohort_not_official_classification"] != COHORT or metadata["scryfall_set_type"] not in ("box", "premium_deck"):
            raise ValueError(f"Unexpected research cohort/type: {code}")
        reviewed.append({
            "code": code,
            "name": metadata["name"],
            "scryfall_type": metadata["scryfall_set_type"],
            "scryfall_release_or_first_card_date": metadata["scryfall_release_or_first_card_date"],
            "scryfall_explicit_parent_code_unchanged": metadata["parent_set_code_explicit_only"],
            "wizards_primary_url": url,
            "wizards_product_section": section,
            "evidence_grade": grade,
            "wizards_exact_scryfall_code_explicit": code in EXPLICIT_WIZARDS_CODES,
            "product_family_wizards_supported": "specialty_box_or_preconstructed_deck_product",
            "wizards_source_note": "Official product documentation supports this product family. Scryfall set dates and parent metadata remain separately frozen; no physical card-level printing census or format legality inference is asserted.",
            "exact_deck_printing_inventory_certified": False,
            "individual_card_legality_certified": False,
            "new_card_count_certified": False,
            "premier_set_certified": False,
        })
        seen.add(code)
    if seen != REQUIRED or len(reviewed) != 14:
        raise ValueError(f"Missing specialty box source codes: {sorted(REQUIRED-seen)}")
    for url, codes in url_codes.items():
        if len(codes) > 1 and codes != EXPECTED_SHARED_URL:
            raise ValueError(f"Official source improperly reused: {url}")
    if not any(codes == EXPECTED_SHARED_URL for codes in url_codes.values()):
        raise ValueError("2018 Game Night versus Gift Pack shared-article boundary lost")
    remaining = [r for r in pending if r["code"] not in seen]
    boxed = [r for r in remaining if catalog[r["code"]]["metadata_cohort_not_official_classification"] == COHORT]
    if len(remaining) != 683 or len(boxed) != 16 or 165 + len(remaining) != 848:
        raise ValueError("Outside-category corpus / boxed queue conservation failed")
    return {
        "schema": 1, "cutoff": "2026-10-29", "prior_audit": PREV.name,
        "source": LEDGER.name, "source_reviewed_this_batch": 14,
        "cumulative_family_source_backed_codes": 165,
        "cumulative_source_pending_codes": 683,
        "previous_boxed_source_pending": 30,
        "boxed_source_pending_after_batch": 16,
        "wizards_explicit_set_codes_this_batch": sorted(EXPLICIT_WIZARDS_CODES),
        "reviewed_boxed_specialty_codes": sorted(reviewed, key=lambda x: x["code"]),
        "remaining_source_pending_queue": remaining,
        "caveats": evidence["source_caveats"] + [
            "A boxed product may contain multiple decks/boosters; fourteen codes are not fourteen premier expansion sets.",
            "165 reviewed plus 683 pending conserves all 848 original non-expansion/core released paper codes.",
            "No frozen October 29 Scryfall set metadata, printing inventory, rules or Grixis approvals changed.",
        ],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    report = build(*(json.loads(p.read_text(encoding="utf-8")) for p in (BASE, PREV, LEDGER)))
    content = encode(report)
    if args.write:
        OUT.write_bytes(content)
    elif not OUT.exists() or OUT.read_bytes() != content:
        raise ValueError("Specialty boxed source audit not reproducible")
    print(json.dumps({k: report[k] for k in (
        "source_reviewed_this_batch", "cumulative_family_source_backed_codes",
        "cumulative_source_pending_codes", "boxed_source_pending_after_batch")}, sort_keys=True))


if __name__ == "__main__":
    main()
