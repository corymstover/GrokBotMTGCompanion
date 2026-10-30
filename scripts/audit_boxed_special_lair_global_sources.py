#!/usr/bin/env python3
"""Audit five Wizards-documented Secret Lair and Global Series product families."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

DATA = Path(__file__).resolve().parent.parent / "data" / "set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREV = DATA / "boxed_specialty_source_audit_2026-10-29.json"
LEDGER = DATA / "boxed_special_lair_global_sources_2018_2026.json"
OUT = DATA / "boxed_special_lair_global_audit_2026-10-29.json"
REQUIRED = {"gs1", "sld", "slu", "slc", "slz"}
COHORT = "preconstructed_and_boxed"


def encode(obj):
    return (json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def build(base, previous, ledger):
    if (base.get("snapshot_date"), previous.get("cutoff"), ledger.get("cutoff")) != (
            "2026-10-29", "2026-10-29", "2026-10-29"):
        raise ValueError("Historical source cutoff drift")
    if (previous.get("cumulative_family_source_backed_codes"),
            previous.get("cumulative_source_pending_codes"),
            previous.get("boxed_source_pending_after_batch")) != (165, 683, 16):
        raise ValueError("Prior boxed specialty review count changed")
    old = previous["remaining_source_pending_queue"]
    codes = {r["code"] for r in old}
    catalog = {r["code"]: r for r in base["all_848_released_nondigital_other_type_records"]}
    if len(old) != 683 or len(codes) != 683 or len(catalog) != 848:
        raise ValueError("Source-pending queue or frozen catalog corrupted")
    seen = set()
    urls = set()
    verified = []
    for rec in ledger["records"]:
        code = rec.get("code")
        if code in seen:
            raise ValueError(f"Duplicate Secret Lair/Global Series source: {code}")
        if code not in REQUIRED or code not in codes:
            raise ValueError(f"Unsupported or previously reviewed code: {code}")
        url = rec.get("official_url", "")
        parts = urlparse(url)
        if (parts.scheme != "https" or parts.hostname not in
                ("magic.wizards.com", "www.magic.wizards.com", "mtg-jp.com") or
                not (parts.path.startswith("/en/news/") or parts.path.startswith("/products/"))):
            raise ValueError(f"Not a direct official Wizards source: {code}")
        if url in urls:
            raise ValueError(f"Official product article reused: {code}")
        section = rec.get("source_section", "")
        if len(section) < 50:
            raise ValueError(f"Missing product-specific section: {code}")
        note = rec.get("relationship_note", "")
        if len(note) < 60:
            raise ValueError(f"Insufficient product-relation caveat: {code}")
        grade = rec.get("evidence_grade")
        if grade not in ("official_product_code_and_release", "named_product_family_crosswalk"):
            raise ValueError(f"Unsupported direct-source grade: {code}")
        explicit = code == "gs1"
        if (grade == "official_product_code_and_release") != explicit:
            raise ValueError(f"Incorrect official printed-code claim: {code}")
        if explicit and (parts.hostname != "mtg-jp.com" or "GS1" not in section):
            raise ValueError("GS1 lacks exact Japanese Wizards product-code evidence")
        meta = catalog[code]
        if (meta["metadata_cohort_not_official_classification"] != COHORT or
                meta["scryfall_set_type"] != ("duel_deck" if explicit else "box")):
            raise ValueError(f"Unexpected Scryfall metadata cohort/type: {code}")
        seen.add(code)
        urls.add(url)
        verified.append({
            "code": code,
            "name": meta["name"],
            "scryfall_type": meta["scryfall_set_type"],
            "scryfall_release_or_first_card_date": meta["scryfall_release_or_first_card_date"],
            "scryfall_explicit_parent_code_unchanged": meta["parent_set_code_explicit_only"],
            "wizards_primary_url": url,
            "wizards_product_section": section,
            "wizards_supported_relationship_note": note,
            "evidence_grade": grade,
            "wizards_exact_scryfall_code_explicit": explicit,
            "product_family_wizards_supported": "secret_lair_collection_or_global_series_introductory_decks",
            "exact_deck_or_card_printing_inventory_certified": False,
            "current_format_legality_certified": False,
            "premier_set_certified": False,
            "new_card_count_certified": False,
        })
    if seen != REQUIRED or len(verified) != 5:
        raise ValueError(f"Missing five source-backed products: {sorted(REQUIRED-seen)}")
    remaining = [r for r in old if r["code"] not in seen]
    boxed = [r for r in remaining if catalog[r["code"]]["metadata_cohort_not_official_classification"] == COHORT]
    if len(remaining) != 678 or len(boxed) != 11 or 170 + len(remaining) != 848:
        raise ValueError("Outside-category and boxed cohort totals fail conservation")
    return {
        "schema": 1, "cutoff": "2026-10-29",
        "prior_audit": PREV.name, "source": LEDGER.name,
        "new_source_backed_product_family_codes": 5,
        "cumulative_family_source_backed_codes": 170,
        "cumulative_source_pending_codes": 678,
        "previous_boxed_source_pending": 16,
        "boxed_source_pending_after_batch": 11,
        "wizards_explicit_codes_this_batch": ["gs1"],
        "reviewed_secret_lair_global_codes": sorted(verified, key=lambda x: x["code"]),
        "remaining_source_pending_queue": remaining,
        "caveats": ledger["caveats"] + [
            "170 source-backed plus 678 source-pending conserves all 848 released nondigital other-category paper codes.",
            "No product-family evidence is treated as an exact printing census, current legality record or premiere-set certification.",
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
        raise ValueError("Secret Lair/Global Series primary-source report is not reproducible")
    print(json.dumps({k: report[k] for k in (
        "new_source_backed_product_family_codes", "cumulative_family_source_backed_codes",
        "cumulative_source_pending_codes", "boxed_source_pending_after_batch")}, sort_keys=True))


if __name__ == "__main__":
    main()
