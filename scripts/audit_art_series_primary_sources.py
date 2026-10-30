#!/usr/bin/env python3
"""Certify 38 first-party set-specific art-card component references, not legal game cards."""
import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

DATA = Path(__file__).resolve().parent.parent / "data/set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREV = DATA / "event_collab_promos_source_audit_2026-10-29.json"
LEDGER = DATA / "art_series_primary_sources_2019_2026.json"
OUTPUT = DATA / "art_series_primary_source_audit_2026-10-29.json"
EXPECTED_ART_CODES = {
    "amh1", "aznr", "akhm", "astx", "amh2", "aafr", "amid", "avow", "aneo",
    "asnc", "aclb", "admu", "abro", "aone", "amom", "altr", "acmm", "awoe",
    "alci", "amkm", "aotj", "amh3", "aacr", "ablb", "adsk", "afdn", "ainr",
    "adft", "atdm", "afin", "aeoe", "aspm", "aecl", "atmt", "asos", "amsh",
    "ahob", "afra"
}
UNSOURCED_SUBGROUPS = {"atla", "atle", "ahoc"}


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def is_wizards_art_source(url):
    p = urlparse(url)
    return (p.scheme == "https" and p.hostname in {"magic.wizards.com", "www.magic.wizards.com"}
            and p.path.startswith(("/en/news/card-image-gallery/", "/en/news/card-preview/",
                                   "/en/news/feature/", "/en/products/")))


def build(base, prev, ledger):
    if (base["snapshot_date"], prev["cutoff"], ledger["cutoff"]) != ("2026-10-29",) * 3:
        raise ValueError("Frozen Scryfall / source cutoff mismatch")
    if (prev["cumulative_family_source_backed_codes"], prev["cumulative_source_pending_codes"],
            prev["remaining_promo_record_extras"], prev["remaining_promo_parent_linked_explicit"],
            prev["remaining_promo_without_explicit_parent"]) != (221, 627, 603, 457, 146):
        raise ValueError("Previous 221-code event/collaboration checkpoint drift")
    catalog = {row["code"]: row for row in base["all_848_released_nondigital_other_type_records"]}
    pending_rows = prev["remaining_source_pending_queue"]
    pending = {row["code"] for row in pending_rows}
    if len(catalog) != 848 or len(pending) != 627 or not EXPECTED_ART_CODES | UNSOURCED_SUBGROUPS <= pending:
        raise ValueError("Frozen 848-code paper catalog/pending membership drift")
    seen = set()
    sourced = []
    for item in ledger["records"]:
        code = item["code"]
        if code in seen or code not in EXPECTED_ART_CODES:
            raise ValueError(f"Duplicated or unapproved art-series source {code}")
        seen.add(code)
        if not is_wizards_art_source(item["official_url"]):
            raise ValueError(f"Art-card source not a direct official Wizards article {code}")
        expected_kind = ({"amh1": "wizards_release_notes_explicit_nonplayability",
                          "amid": "wizards_set_product_page_art_card_inclusion"}.get(code,
                                                                                     "wizards_dedicated_art_gallery"))
        if item["source_kind"] != expected_kind:
            raise ValueError(f"Unfounded or changed first-party art evidence grade {code}")
        if len(item["named_family"]) < 7 or len(item["source_note"]) < 95 or "art" not in item["source_note"].lower():
            raise ValueError(f"Insufficient concrete named art-series source evidence {code}")
        row = catalog[code]
        if (row["scryfall_set_type"] != "memorabilia" or
                row["metadata_cohort_not_official_classification"] != "promotional_and_record_extras" or
                "Art Series" not in row["name"] or row["parent_set_code_explicit_only"] is None):
            raise ValueError(f"Wrong Scryfall art-series category or explicit parent {code}")
        sourced.append({
            "code": code,
            "name": row["name"],
            "scryfall_type": "memorabilia",
            "scryfall_earliest_card_date": row["scryfall_release_or_first_card_date"],
            "scryfall_parent_set_code_explicit_only_unchanged": row["parent_set_code_explicit_only"],
            "official_source_url": item["official_url"],
            "officially_named_product_family": item["named_family"],
            "source_grade": item["source_kind"],
            "source_note": item["source_note"],
            "wizards_prints_exact_scryfall_art_series_code": False,
            "standalone_premier_expansion_certified": False,
            "individual_art_printing_inventory_certified": False,
            "new_playable_card_debut_count_certified": False,
            "current_format_legality_certified": False,
        })
    if seen != EXPECTED_ART_CODES or len(sourced) != 38:
        raise ValueError(f"Missing specifically sourced art-series pages: {sorted(EXPECTED_ART_CODES - seen)}")
    remainder = [r for r in pending_rows if r["code"] not in seen]
    promo_extras = [r for r in remainder if catalog[r["code"]]["metadata_cohort_not_official_classification"] == "promotional_and_record_extras"]
    parent_linked = sum(catalog[r["code"]]["parent_set_code_explicit_only"] is not None for r in promo_extras)
    art_pending = {r["code"] for r in remainder if "Art Series" in r["name"]}
    if (len(remainder), len(promo_extras), parent_linked, len(promo_extras) - parent_linked,
            art_pending) != (589, 565, 419, 146, UNSOURCED_SUBGROUPS):
        raise ValueError("Art-only source review corrupted promo / parent / unresolved series arithmetic")
    if 259 + len(remainder) != 848:
        raise ValueError("Full 848-code outside-category conservation failed")
    return {
        "schema": 1, "cutoff": "2026-10-29", "previous_audit": PREV.name,
        "source_ledger": LEDGER.name, "new_source_backed_codes": 38,
        "new_named_family_wizards_crosswalks": 38, "new_exact_wizards_code_declarations": 0,
        "cumulative_family_source_backed_codes": 259, "cumulative_source_pending_codes": 589,
        "source_backed_art_series_this_batch": 38,
        "remaining_unreviewed_art_series_codes": sorted(UNSOURCED_SUBGROUPS),
        "remaining_promo_record_extras": len(promo_extras),
        "remaining_promo_parent_linked_explicit": parent_linked,
        "remaining_promo_without_explicit_parent": len(promo_extras) - parent_linked,
        "remaining_promo_types": dict(sorted(Counter(r["scryfall_type"] for r in promo_extras).items())),
        "remaining_boxed_preconstructed": 11, "remaining_draft_starter": 11,
        "remaining_curated_reprints": 2,
        "reviewed_art_series_families": sorted(sourced, key=lambda r: r["code"]),
        "remaining_source_pending_queue": remainder,
        "caveats": ledger["caveats"] + [
            "259 individually reviewed first-party named-family records plus 589 source-pending entries conserve the frozen 848-paper-code other-category catalog.",
            "All 38 art sources substantiate real collectible illustration inserts or a dedicated art-card family for a named parent release, not a new playable-card expansion or Wizards-printed Scryfall Art Series code.",
            "All 38 explicit parent links come from the frozen Scryfall metadata. Official sources do not thereby independently confirm a Scryfall parent code or a playable printing inventory.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = build(*(json.loads(p.read_text(encoding="utf-8")) for p in (BASE, PREV, LEDGER)))
    value = encode(report)
    if args.write:
        OUTPUT.write_bytes(value)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != value:
        raise ValueError("Art-series primary source review not exactly reproducible")
    print(json.dumps({k: report[k] for k in (
        "new_source_backed_codes", "cumulative_family_source_backed_codes", "cumulative_source_pending_codes",
        "remaining_promo_record_extras", "remaining_promo_parent_linked_explicit",
        "remaining_promo_without_explicit_parent", "remaining_unreviewed_art_series_codes")}, sort_keys=True))


if __name__ == "__main__":
    main()
