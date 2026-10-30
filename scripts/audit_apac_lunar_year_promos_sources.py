#!/usr/bin/env python3
"""Certify six dated Wizards Lunar New Year *family* crosswalks, not exact set codes."""
import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

DATA = Path(__file__).resolve().parent.parent / "data/set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREV = DATA / "historical_promo_series_source_audit_2026-10-29.json"
LEDGER = DATA / "apac_lunar_year_promos_sources_2021_2026.json"
OUTPUT = DATA / "apac_lunar_year_promos_source_audit_2026-10-29.json"
REQUIRED = {f"pl{year:02}" for year in range(21, 27)}
ANIMALS = {"pl21": "Ox", "pl22": "Tiger", "pl23": "Rabbit", "pl24": "Dragon", "pl25": "Snake", "pl26": "Horse"}


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def is_first_party(url):
    p = urlparse(url)
    return (p.scheme == "https" and p.hostname in {
        "magic.wizards.com", "www.magic.gg", "magic.gg"
    } and (p.path.startswith("/en/news/") or
           p.path.startswith("/zh-Hant/news/") or
           (p.hostname in {"www.magic.gg", "magic.gg"} and p.path.startswith("/news/"))))


def build(base, previous, ledger):
    if (base["snapshot_date"], previous["cutoff"], ledger["cutoff"]) != ("2026-10-29",) * 3:
        raise ValueError("Snapshot/date mismatch")
    if (previous["cumulative_family_source_backed_codes"],
            previous["cumulative_source_pending_codes"],
            previous["remaining_promo_record_extras"],
            previous["remaining_promo_parent_linked_explicit"],
            previous["remaining_promo_without_explicit_parent"]) != (208, 640, 616, 457, 159):
        raise ValueError("Historical annual promo source checkpoint drift")
    catalog = {item["code"]: item for item in base["all_848_released_nondigital_other_type_records"]}
    pending_rows = previous["remaining_source_pending_queue"]
    pending = {item["code"] for item in pending_rows}
    if len(catalog) != 848 or len(pending) != 640 or not REQUIRED <= pending:
        raise ValueError("Frozen 848 paper catalog/pending membership drift")

    observed = set()
    reviewed = []
    for item in ledger["records"]:
        code = item["code"]
        if code in observed or code not in REQUIRED:
            raise ValueError(f"Duplicated or unauthorized annual promo source {code}")
        observed.add(code)
        if not is_first_party(item["official_url"]):
            raise ValueError(f"Not an approved first-party Wizards annual promo source {code}")
        grade = item["evidence_grade"]
        if (code == "pl26") != (grade == "wizards_contemporary_promotion_regional_language") or grade not in {
            "wizards_contemporary_promotion", "wizards_contemporary_promotion_regional_language"
        }:
            raise ValueError(f"Annual promo source grade/language mismatch {code}")
        if (code == "pl26") != (urlparse(item["official_url"]).path.startswith("/zh-Hant/")):
            raise ValueError(f"Regional evidence URL mismatch {code}")
        if (ANIMALS[code] not in item["official_section"] or
                str(2000 + int(code[2:])) not in item["official_section"] or
                len(item["official_section"]) < 95 or len(item["source_caveat"]) < 85):
            raise ValueError(f"Missing dated, named Wizards evidence/caveat {code}")
        if item["source_publication_date"][:4] not in {str(2000 + int(code[2:])), "2023" if code == "pl24" else ""}:
            raise ValueError(f"Annual promo source publication date mismatch {code}")
        meta = catalog[code]
        if (meta["scryfall_set_type"] != "promo" or
                meta["metadata_cohort_not_official_classification"] != "promotional_and_record_extras" or
                meta["parent_set_code_explicit_only"] is not None):
            raise ValueError(f"Unanticipated set classification or parent for {code}")
        reviewed.append({
            "code": code,
            "name": meta["name"],
            "scryfall_type": "promo",
            "scryfall_earliest_card_date": meta["scryfall_release_or_first_card_date"],
            "scryfall_parent_set_code_unchanged": None,
            "official_source_url": item["official_url"],
            "official_source_publication_date": item["source_publication_date"],
            "official_source_section": item["official_section"],
            "source_grade": grade,
            "wizards_prints_exact_scryfall_code": False,
            "officially_supported_product_family": item["supported_family"],
            "source_caveat": item["source_caveat"],
            "standalone_premier_expansion_certified": False,
            "individual_card_printing_inventory_certified": False,
            "new_card_debut_count_certified": False,
            "current_format_legality_certified": False,
        })
    if observed != REQUIRED or len(reviewed) != 6:
        raise ValueError(f"Incomplete annual promo family evidence: {sorted(REQUIRED - observed)}")
    remaining = [item for item in pending_rows if item["code"] not in observed]
    promos = [item for item in remaining if catalog[item["code"]]["metadata_cohort_not_official_classification"] == "promotional_and_record_extras"]
    linked = sum(catalog[item["code"]]["parent_set_code_explicit_only"] is not None for item in promos)
    if (len(remaining), len(promos), linked, len(promos) - linked) != (634, 610, 457, 153):
        raise ValueError("Six annual promos did not preserve frozen code arithmetic")
    if 214 + len(remaining) != 848:
        raise ValueError("848-code catalog conservation failed")
    return {
        "schema": 1,
        "cutoff": "2026-10-29",
        "previous_audit": PREV.name,
        "source_ledger": LEDGER.name,
        "new_source_backed_codes": 6,
        "new_exact_wizards_code_declarations": 0,
        "new_named_family_wizards_crosswalks": 6,
        "cumulative_family_source_backed_codes": 214,
        "cumulative_source_pending_codes": 634,
        "remaining_promo_record_extras": len(promos),
        "remaining_promo_parent_linked_explicit": linked,
        "remaining_promo_without_explicit_parent": len(promos) - linked,
        "remaining_promo_types": dict(sorted(Counter(item["scryfall_type"] for item in promos).items())),
        "remaining_boxed_preconstructed": 11,
        "remaining_draft_starter": 11,
        "remaining_curated_reprints": 2,
        "reviewed_apac_lunar_year_promo_families": sorted(reviewed, key=lambda item: item["code"]),
        "remaining_source_pending_queue": remaining,
        "caveats": ledger["caveats"] + [
            "The six dated official annual program pages support PL21 through PL26 family names and years, not exact Wizards-printed Scryfall codes.",
            "214 source-backed and 634 source-pending conserves the frozen 848 released nondigital other-category paper codes.",
            "Only explicit Scryfall parent links are counted as such; these six annual groupings have none and are not six premier sets.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = build(*(json.loads(p.read_text(encoding="utf-8")) for p in (BASE, PREV, LEDGER)))
    payload = encode(report)
    if args.write:
        OUTPUT.write_bytes(payload)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != payload:
        raise ValueError("APAC Lunar New Year source audit is not reproducible")
    print(json.dumps({k: report[k] for k in (
        "new_source_backed_codes", "cumulative_family_source_backed_codes", "cumulative_source_pending_codes",
        "remaining_promo_record_extras", "remaining_promo_parent_linked_explicit",
        "remaining_promo_without_explicit_parent")}, sort_keys=True))


if __name__ == "__main__":
    main()
