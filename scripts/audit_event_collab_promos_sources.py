#!/usr/bin/env python3
"""Audit seven individually sourced 2022–2025 event/collaboration promo families."""
import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

DATA = Path(__file__).resolve().parent.parent / "data/set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREV = DATA / "apac_lunar_year_promos_source_audit_2026-10-29.json"
LEDGER = DATA / "event_collab_promos_sources_2022_2025.json"
OUTPUT = DATA / "event_collab_promos_source_audit_2026-10-29.json"
REQUIRED = {"gdy", "sch", "prcq", "pr23", "pmda", "pcbb", "pspl"}
PROGRAM_TERMS = {
    "gdy": ("Game Day", "2022"),
    "sch": ("Store Championship", "2022"),
    "prcq": ("Regional Championship Qualifier", "2022"),
    "pr23": ("Regional Championship Qualifier", "2023"),
    "pmda": ("Magic × Duel Masters", "2023"),
    "pcbb": ("Cowboy Bebop", "2024"),
    "pspl": ("Spotlight", "2025"),
}
EXPECTED_DATES = {
    "gdy": "2022-08-24", "sch": "2022-08-24", "prcq": "2022-03-31",
    "pr23": "2022-10-04", "pmda": "2023-08-10", "pcbb": "2024-04-22", "pspl": "2024-08-20"
}


def encode(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def wizards_url(url):
    p = urlparse(url)
    return (p.scheme == "https" and
            ((p.hostname == "wpn.wizards.com" and p.path.startswith("/en/news/")) or
             (p.hostname == "magic.wizards.com" and p.path.startswith("/en/news/")) or
             (p.hostname == "mtg-jp.com" and p.path.startswith("/reading/")) or
             (p.hostname in {"magic.gg", "www.magic.gg"} and p.path.startswith("/news/"))))


def build(base, previous, ledger):
    if (base["snapshot_date"], previous["cutoff"], ledger["cutoff"]) != ("2026-10-29",) * 3:
        raise ValueError("Frozen snapshot dates mismatch")
    if (previous["cumulative_family_source_backed_codes"],
            previous["cumulative_source_pending_codes"], previous["remaining_promo_record_extras"],
            previous["remaining_promo_parent_linked_explicit"],
            previous["remaining_promo_without_explicit_parent"]) != (214, 634, 610, 457, 153):
        raise ValueError("Lunar promo source checkpoint drift")
    catalog = {item["code"]: item for item in base["all_848_released_nondigital_other_type_records"]}
    queue = previous["remaining_source_pending_queue"]
    pending = {row["code"] for row in queue}
    if len(catalog) != 848 or len(pending) != 634 or not REQUIRED <= pending:
        raise ValueError("Whole frozen paper-set catalog drift")
    seen = set()
    review = []
    for item in ledger["records"]:
        code = item["code"]
        if code in seen or code not in REQUIRED:
            raise ValueError(f"Duplicate or unauthorized event/collab promo {code}")
        seen.add(code)
        if not wizards_url(item["official_url"]):
            raise ValueError(f"Source outside first-party Wizards publishers {code}")
        expected_grade = ("wizards_dated_program_family_regional_language" if code == "pmda"
                          else "wizards_dated_program_family")
        if item["evidence_grade"] != expected_grade or (code == "pmda") != (urlparse(item["official_url"]).hostname == "mtg-jp.com"):
            raise ValueError(f"Misgraded regional language/primary source {code}")
        program, year = PROGRAM_TERMS[code]
        if (item["official_publication_date"] != EXPECTED_DATES[code] or
                program not in item["official_section"] or year not in item["official_section"] or
                len(item["official_section"]) < 100 or len(item["source_caveat"]) < 85):
            raise ValueError(f"Missing dated named-program evidence and caveat {code}")
        row = catalog[code]
        if (row["scryfall_set_type"] != "promo" or
                row["metadata_cohort_not_official_classification"] != "promotional_and_record_extras" or
                row["parent_set_code_explicit_only"] is not None):
            raise ValueError(f"Unexpected frozen Scryfall classification or parent {code}")
        review.append({
            "code": code, "name": row["name"], "scryfall_type": "promo",
            "scryfall_earliest_card_date": row["scryfall_release_or_first_card_date"],
            "scryfall_parent_set_code_unchanged": None,
            "official_source_url": item["official_url"],
            "official_source_publication_date": item["official_publication_date"],
            "official_source_section": item["official_section"],
            "officially_supported_product_family": item["supported_family"],
            "source_grade": item["evidence_grade"],
            "source_caveat": item["source_caveat"],
            "wizards_prints_exact_scryfall_code": False,
            "standalone_premier_expansion_certified": False,
            "individual_card_printing_inventory_certified": False,
            "new_card_debut_count_certified": False,
            "current_format_legality_certified": False,
        })
    if seen != REQUIRED or len(review) != 7:
        raise ValueError(f"Missing event-program evidence {sorted(REQUIRED - seen)}")
    remainder = [row for row in queue if row["code"] not in seen]
    promos = [row for row in remainder if catalog[row["code"]]["metadata_cohort_not_official_classification"] == "promotional_and_record_extras"]
    linked = sum(catalog[row["code"]]["parent_set_code_explicit_only"] is not None for row in promos)
    if (len(remainder), len(promos), linked, len(promos) - linked) != (627, 603, 457, 146):
        raise ValueError("Unexpected cumulative event-promo arithmetic")
    if 221 + len(remainder) != 848:
        raise ValueError("Frozen 848 set-code conservation failed")
    return {
        "schema": 1, "cutoff": "2026-10-29", "previous_audit": PREV.name,
        "source_ledger": LEDGER.name, "new_source_backed_codes": 7,
        "new_named_family_wizards_crosswalks": 7, "new_exact_wizards_code_declarations": 0,
        "cumulative_family_source_backed_codes": 221, "cumulative_source_pending_codes": 627,
        "remaining_promo_record_extras": len(promos),
        "remaining_promo_parent_linked_explicit": linked,
        "remaining_promo_without_explicit_parent": len(promos) - linked,
        "remaining_promo_types": dict(sorted(Counter(row["scryfall_type"] for row in promos).items())),
        "remaining_boxed_preconstructed": 11, "remaining_draft_starter": 11,
        "remaining_curated_reprints": 2,
        "reviewed_event_collab_promo_families": sorted(review, key=lambda x: x["code"]),
        "remaining_source_pending_queue": remainder,
        "caveats": ledger["caveats"] + [
            "221 first-party named-family reviews plus 627 still-pending reviews exactly conserve the frozen 848 paper other-category set codes.",
            "Neither an event program name nor absence of an explicit Scryfall parent code means a newly released premier set.",
            "All seven official sources provide family/program-grade promotion evidence; none independently publishes the associated Scryfall catalog code.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    options = parser.parse_args()
    result = build(*(json.loads(p.read_text(encoding="utf-8")) for p in (BASE, PREV, LEDGER)))
    content = encode(result)
    if options.write:
        OUTPUT.write_bytes(content)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != content:
        raise ValueError("Event/collaboration source audit bytes are not reproducible")
    print(json.dumps({k: result[k] for k in (
        "new_source_backed_codes", "cumulative_family_source_backed_codes", "cumulative_source_pending_codes",
        "remaining_promo_record_extras", "remaining_promo_parent_linked_explicit",
        "remaining_promo_without_explicit_parent")}, sort_keys=True))


if __name__ == "__main__":
    main()
