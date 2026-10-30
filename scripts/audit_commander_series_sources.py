#!/usr/bin/env python3
"""Conserve nine source-backed historical annual Commander product-family codes."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREV = DATA / "duel_decks_source_audit_2026-10-29.json"
LEDGER = DATA / "commander_series_sources_2011_2020.json"
OUT = DATA / "commander_series_source_audit_2026-10-29.json"
EXPECTED = {"cmd": 2011, **{f"c{year % 100:02d}": year for year in range(2013, 2021)}}
COHORT = "preconstructed_and_boxed"


def encode(data):
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build(base, previous, ledger):
    if any(x != "2026-10-29" for x in (
        base.get("snapshot_date"), previous.get("cutoff"), ledger.get("cutoff")
    )):
        raise ValueError("Historical snapshot cutoff mismatch")
    if (previous.get("cumulative_family_source_backed_codes"),
            previous.get("cumulative_source_pending_codes"),
            previous.get("boxed_source_pending_after_batch")) != (111, 737, 70):
        raise ValueError("Previous Duel Decks 111/737/70 checkpoint changed")
    old = previous["remaining_source_pending_queue"]
    pending = {r["code"] for r in old}
    if len(pending) != len(old) or len(pending) != 737:
        raise ValueError("Missing/duplicated previous pending codes")
    catalog = {r["code"]: r for r in base["all_848_released_nondigital_other_type_records"]}
    if len(catalog) != 848:
        raise ValueError("Frozen 848-code catalog changed")

    seen = set()
    reviewed = []
    for evidence in ledger["records"]:
        code = evidence.get("code")
        if code in seen:
            raise ValueError(f"Duplicate Commander evidence: {code}")
        year = evidence.get("year")
        if code not in EXPECTED or year != EXPECTED[code] or code not in pending:
            raise ValueError(f"Unexpected Commander annual family: {code}/{year}")
        url = evidence.get("official_product_url", "")
        u = urlparse(url)
        if u.scheme != "https" or u.hostname != "mtg-jp.com" or not u.path.startswith("/products/"):
            raise ValueError(f"Commander family needs direct official product page: {code}")
        meta = catalog[code]
        if meta["scryfall_set_type"] != "commander" or meta["metadata_cohort_not_official_classification"] != COHORT:
            raise ValueError(f"Commander catalog type/cohort mismatch: {code}")
        if str(year) not in meta["name"]:
            raise ValueError(f"Commander product year/name mismatch: {code}")
        seen.add(code)
        reviewed.append({
            "code": code,
            "name": meta["name"],
            "source_year": year,
            "scryfall_set_type": meta["scryfall_set_type"],
            "scryfall_release_or_first_card_date": meta["scryfall_release_or_first_card_date"],
            "scryfall_parent_set_code_unchanged": meta["parent_set_code_explicit_only"],
            "wizards_primary_url": url,
            "wizards_source_section": f"Official Commander ({year} edition) product page",
            "wizards_supported_family": "annual_commander_preconstructed_deck_release_family",
            "source_note": (
                f"Wizards' official product archive lists the {year} Commander preconstructed release; "
                "the exact Scryfall code and first-card date are independent catalog metadata. "
                "This source certifies a product family, not a single boxed deck or premier booster expansion."
            ),
            "evidence_grade": "wizards_official_japanese_product_page_scryfall_code_crosswalk",
            "scryfall_code_explicitly_confirmed_by_wizards": False,
            "individually_packaged_deck_count_certified": False,
            "standalone_booster_expansion": False,
            "premier_set_status_certified": False,
            "card_format_legality_inferred": False
        })
    if seen != set(EXPECTED) or len(reviewed) != 9:
        raise ValueError(f"Missing Commander annual release(s): {sorted(set(EXPECTED)-seen)}")
    remaining = [r for r in old if r["code"] not in seen]
    boxed_pending = [
        r for r in remaining
        if catalog[r["code"]]["metadata_cohort_not_official_classification"] == COHORT
    ]
    if len(remaining) != 728 or len(boxed_pending) != 61 or 120 + len(remaining) != 848:
        raise ValueError("Commander annual research cohort count conservation failed")
    return {
        "schema": 1,
        "cutoff": "2026-10-29",
        "prior_audit": PREV.name,
        "source": LEDGER.name,
        "new_source_backed_commander_product_family_codes": 9,
        "new_annual_commander_release_families": 9,
        "individual_preconstructed_deck_box_count_not_certified": True,
        "cumulative_family_source_backed_codes": 120,
        "cumulative_source_pending_codes": 728,
        "previous_boxed_source_pending": 70,
        "boxed_source_pending_after_batch": 61,
        "reviewed_commander_codes": sorted(reviewed, key=lambda x: x["code"]),
        "remaining_source_pending_queue": remaining,
        "caveats": [
            "Nine annual Commander product-family codes are sourced; no claim is made that each code represents exactly one deck box or one new-card set.",
            "Wizards product pages establish Commander preconstructed releases; exact codes, parent links and set-release dates are from the frozen Scryfall catalog.",
            "The original 2011 and 2013–2020 annual families are the only scope of this review. Later set-linked Commander releases remain pending.",
            "A Commander deck reprint does not expand Standard/Modern legality by itself; no new format-legality or premier-set status is inferred.",
            "120 source-backed and 728 source-pending count Scryfall records, not numbers of separately packaged products or original card designs."
        ]
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = build(*(json.loads(p.read_text(encoding="utf-8")) for p in (BASE, PREV, LEDGER)))
    blob = encode(result)
    if args.write:
        OUT.write_bytes(blob)
    elif not OUT.exists() or OUT.read_bytes() != blob:
        raise ValueError("Committed Commander 2011–2020 audit not reproducible")
    print(json.dumps({
        k: result[k] for k in (
            "new_source_backed_commander_product_family_codes", "cumulative_family_source_backed_codes",
            "cumulative_source_pending_codes", "boxed_source_pending_after_batch"
        )
    }, sort_keys=True))


if __name__ == "__main__":
    main()
