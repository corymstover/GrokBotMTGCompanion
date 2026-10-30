#!/usr/bin/env python3
"""Reproduce ten individual official promotional/commemorative family citations.

Wizards product-family citations are not proof of official Scryfall catalog codes,
of exact card inventory, or of an additional premier expansion release.
"""
import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

DATA = Path(__file__).resolve().parent.parent / "data/set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREV = DATA / "masterpiece_memorabilia_source_audit_2026-10-29.json"
LEDGER = DATA / "historical_promo_series_sources_1997_2024.json"
OUTPUT = DATA / "historical_promo_series_source_audit_2026-10-29.json"
VANGUARD = {"pvan"}
WORLDS = {"wc97", "wc98", "wc99", "wc00", "wc04"}
LOCAL_STORE = {"plg20", "plg21", "plg22", "plg24"}
REQUIRED = VANGUARD | WORLDS | LOCAL_STORE


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def is_wizards_source(url):
    p = urlparse(url)
    return p.scheme == "https" and p.hostname in {
        "magic.wizards.com", "www.magic.wizards.com", "mtg-jp.com", "www.mtg-jp.com", "wpn.wizards.com"
    } and (p.path.startswith("/en/news/") or p.path.startswith("/reading/"))


def build(base, previous, ledger):
    if (base["snapshot_date"], previous["cutoff"], ledger["cutoff"]) != (
            "2026-10-29", "2026-10-29", "2026-10-29"):
        raise ValueError("Frozen source/date mismatch")
    if (previous["cumulative_family_source_backed_codes"],
            previous["cumulative_source_pending_codes"],
            previous["remaining_promo_record_extras"]) != (198, 650, 626):
        raise ValueError("Previous collectible evidence checkpoint drift")
    catalog = {r["code"]: r for r in base["all_848_released_nondigital_other_type_records"]}
    old = previous["remaining_source_pending_queue"]
    pending = {r["code"] for r in old}
    if len(catalog) != 848 or len(pending) != 650 or not REQUIRED <= pending:
        raise ValueError("Frozen 848-code catalog/pending list drift")
    seen = set()
    rows = []
    for item in ledger["records"]:
        code = item["code"]
        if code in seen or code not in REQUIRED:
            raise ValueError(f"Duplicate or unapproved family citation {code}")
        seen.add(code)
        if not is_wizards_source(item["official_url"]):
            raise ValueError(f"Not a first-party Wizards publication {code}")
        if item["evidence_grade"] not in {"wizards_contemporary_promotion", "wizards_official_named_retrospective"}:
            raise ValueError(f"Unsupported product-family evidence grade {code}")
        if len(item["official_section"]) < 70 or len(item["source_caveat"]) < 65:
            raise ValueError(f"Insufficient specific official evidence/caveat for {code}")
        meta = catalog[code]
        target_type = "vanguard" if code in VANGUARD else "memorabilia" if code in WORLDS else "promo"
        if (meta["scryfall_set_type"] != target_type or
                meta["metadata_cohort_not_official_classification"] != "promotional_and_record_extras" or
                meta["parent_set_code_explicit_only"] is not None):
            raise ValueError(f"Wrong Scryfall type, cohort or explicit parent {code}")
        if (code in WORLDS) != (item["evidence_grade"] == "wizards_official_named_retrospective"):
            raise ValueError(f"Historical product-year evidence grade misused {code}")
        if code in WORLDS and code[-2:] not in item["official_section"]:
            raise ValueError(f"Historical World Championship year not documented {code}")
        if code in LOCAL_STORE and "202" not in item["official_section"]:
            raise ValueError(f"Contemporary local game store promo year undocumented {code}")
        if code == "pvan" and "Vanguard" not in item["official_section"]:
            raise ValueError("Wizards Vanguard product family missing")
        rows.append({
            "code": code, "name": meta["name"], "scryfall_type": target_type,
            "scryfall_earliest_card_date": meta["scryfall_release_or_first_card_date"],
            "scryfall_parent_set_code_unchanged": None,
            "official_source_url": item["official_url"],
            "official_source_section": item["official_section"],
            "source_grade": item["evidence_grade"],
            "wizards_prints_exact_scryfall_code": False,
            "officially_supported_product_family": item["supported_family"],
            "source_caveat": item["source_caveat"],
            "standalone_premier_expansion_certified": False,
            "individual_card_printing_inventory_certified": False,
            "new_card_debut_count_certified": False,
            "current_format_legality_certified": False,
        })
    if seen != REQUIRED or len(rows) != 10:
        raise ValueError(f"Missing one of ten source records: {sorted(REQUIRED - seen)}")
    remainder = [r for r in old if r["code"] not in seen]
    promos = [r for r in remainder if catalog[r["code"]]["metadata_cohort_not_official_classification"] == "promotional_and_record_extras"]
    types = Counter(r["scryfall_type"] for r in promos)
    linked = sum(catalog[r["code"]]["parent_set_code_explicit_only"] is not None for r in promos)
    if (len(remainder), len(promos), linked, len(promos) - linked) != (640, 616, 457, 159):
        raise ValueError("Whole-catalog and unparented promo-series arithmetic drift")
    if 208 + len(remainder) != 848:
        raise ValueError("848-code total not conserved")
    return {
        "schema": 1, "cutoff": "2026-10-29", "previous_audit": PREV.name,
        "source_ledger": LEDGER.name, "new_source_backed_codes": 10,
        "new_exact_wizards_code_declarations": 0,
        "new_named_family_wizards_crosswalks": 10,
        "cumulative_family_source_backed_codes": 208,
        "cumulative_source_pending_codes": 640,
        "source_backed_world_championship_years_this_batch": 5,
        "source_backed_local_store_promotion_years_this_batch": 4,
        "source_backed_vanguard_codes_this_batch": 1,
        "remaining_promo_record_extras": len(promos),
        "remaining_promo_parent_linked_explicit": linked,
        "remaining_promo_without_explicit_parent": len(promos) - linked,
        "remaining_promo_types": dict(sorted(types.items())),
        "remaining_boxed_preconstructed": 11,
        "remaining_draft_starter": 11,
        "remaining_curated_reprints": 2,
        "reviewed_named_promo_families": sorted(rows, key=lambda r: r["code"]),
        "remaining_source_pending_queue": remainder,
        "caveats": ledger["caveats"] + [
            "208 Wizards family-backed plus 640 source-pending conserves the frozen 848 released nondigital other-category code records.",
            "None of these ten Wizards pages independently prints the Scryfall exact set code; family-year joins are frozen Scryfall crosswalks.",
            "The World Championship yearly product references are retrospective mentions, not reconstructed original box inventories or official code certification.",
            "Physical Vanguard supplements are distinct from regular legal deck cards and should never be counted as separate premier expansion sets.",
            "Explicit Scryfall parent relationships are metadata, not Wizards evidence or inferences about debut identity.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = build(*(json.loads(p.read_text(encoding="utf-8"))
                     for p in (BASE, PREV, LEDGER)))
    content = encode(report)
    if args.write:
        OUTPUT.write_bytes(content)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != content:
        raise ValueError("Historical promo series source audit is not reproducible")
    print(json.dumps({k: report[k] for k in (
        "new_source_backed_codes", "cumulative_family_source_backed_codes",
        "cumulative_source_pending_codes", "remaining_promo_record_extras",
        "remaining_promo_parent_linked_explicit", "remaining_promo_without_explicit_parent")}, sort_keys=True))


if __name__ == "__main__":
    main()
