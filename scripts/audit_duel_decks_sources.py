#!/usr/bin/env python3
"""Reproducible Wizards-source review of the historical Duel Decks product family.

Twenty-one original matchup boxes plus four Scryfall Anthology subcatalog codes
represent 22 sold products, not 25. This report overlays the earlier 86-code
audit and does not change either Scryfall snapshot or any Grixis records.
"""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREV = DATA / "boxed_precon_source_audit_2026-10-29.json"
LEDGER = DATA / "duel_decks_sources_2026-10-29.json"
OUT = DATA / "duel_decks_source_audit_2026-10-29.json"
COHORT = "preconstructed_and_boxed"
ORIGINAL_CODES = {
    "dd1", "dd2", "ddc", "ddd", "dde", "ddf", "ddg", "ddh", "ddi",
    "ddj", "ddk", "ddl", "ddm", "ddn", "ddo", "ddp", "ddq", "ddr",
    "dds", "ddt", "ddu",
}
ANTHOLOGY_COMPONENTS = {"dvd": "ddc", "evg": "dd1", "gvl": "ddd", "jvc": "dd2"}
REQUIRED = ORIGINAL_CODES | set(ANTHOLOGY_COMPONENTS)
OFFICIAL_ANTHOLOGY = "https://mtg-jp.com/products/0000095/"


def encode(data):
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build(base, previous, ledger):
    if any(x != "2026-10-29" for x in (
        base.get("snapshot_date"), previous.get("cutoff"), ledger.get("cutoff")
    )):
        raise ValueError("Mismatched historical October 29 cutoff")
    if previous.get("cumulative_family_source_backed_codes") != 86 or previous.get("cumulative_source_pending_codes") != 762:
        raise ValueError("Prior 86/762 checkpoint changed")
    if previous.get("boxed_source_pending_after_batch") != 95:
        raise ValueError("Prior boxed research backlog changed")
    if ledger.get("official_anthology_product") != OFFICIAL_ANTHOLOGY or ledger.get("official_anthology_product_code") != "DD3":
        raise ValueError("Official Anthology relationship not preserved")
    previous_queue = previous["remaining_source_pending_queue"]
    pending_codes = {r["code"] for r in previous_queue}
    if len(previous_queue) != len(pending_codes) or len(previous_queue) != 762:
        raise ValueError("Duplicate/missing prior pending entries")
    catalog = {r["code"]: r for r in base["all_848_released_nondigital_other_type_records"]}
    if len(catalog) != 848:
        raise ValueError("Original 848-code Scryfall catalog changed")

    rows = []
    seen = set()
    for evidence in ledger["records"]:
        code = evidence.get("code")
        if code in seen:
            raise ValueError(f"Duplicate Duel Decks evidence code: {code}")
        if code not in REQUIRED or code not in pending_codes:
            raise ValueError(f"Unexpected previously reviewed/non-Duel Decks code: {code}")
        source = evidence.get("official_product_url", "")
        parsed = urlparse(source)
        if parsed.scheme != "https" or parsed.hostname != "mtg-jp.com" or not parsed.path.startswith("/products/"):
            raise ValueError(f"Unapproved primary source host or route for {code}")
        original = code in ORIGINAL_CODES
        group = evidence.get("family")
        if original and (group != "individually_sold_duel_decks_box" or evidence.get("reprinted_original_product_scryfall_code")):
            raise ValueError(f"Original Duel Deck mislabeled: {code}")
        if not original and (
            group != "anthology_deck_subcatalog"
            or evidence.get("reprinted_original_product_scryfall_code") != ANTHOLOGY_COMPONENTS[code]
            or source != OFFICIAL_ANTHOLOGY
        ):
            raise ValueError(f"Anthology component incorrectly treated as independent product: {code}")
        card_data = catalog[code]
        if card_data["scryfall_set_type"] != "duel_deck" or card_data["metadata_cohort_not_official_classification"] != COHORT:
            raise ValueError(f"Wrong frozen Scryfall source type/cohort: {code}")
        # There is no explicit Scryfall parent for Anthology subcatalogs. The
        # Wizards relationship is an independent, separately attributed fact.
        if not original and card_data["parent_set_code_explicit_only"] is not None:
            raise ValueError(f"Scryfall anthology parent assertion changed: {code}")
        seen.add(code)
        rows.append({
            "code": code,
            "name": card_data["name"],
            "scryfall_set_type": card_data["scryfall_set_type"],
            "scryfall_release_or_first_card_date": card_data["scryfall_release_or_first_card_date"],
            "scryfall_explicit_parent_code_unchanged": card_data["parent_set_code_explicit_only"],
            "wizards_primary_url": source,
            "wizards_source_section": (
                "Official Duel Decks product detail page"
                if original else "Official Duel Decks: Anthology contents: the first four matchups / eight decks"
            ),
            "wizards_supported_family": group,
            "source_note": (
                "Wizards directly lists this named matchup as a historical Duel Decks product; "
                "Scryfall assigns its code independently. It is a preconstructed paired-deck box, not a premier booster expansion."
                if original else
                "Wizards confirms that Duel Decks: Anthology (DD3) contains all eight decks from the first four "
                "matchups. This is a catalog segment within that one box, not a new separately sold Duel Deck."
            ),
            "evidence_grade": "wizards_official_japanese_product_page_scryfall_code_crosswalk",
            "exact_scryfall_code_printed_by_wizards": False,
            "is_separately_sold_duel_decks_box": original,
            "anthology_component_of_one_2014_box": not original,
            "anthology_official_box_code_when_component": "DD3" if not original else None,
            "original_product_scryfall_code_when_anthology_component": (
                ANTHOLOGY_COMPONENTS.get(code)
            ),
            "wizards_product_relation_not_scryfall_parent": (
                "Duel Decks: Anthology" if not original else None
            ),
            "standalone_booster_expansion": False,
            "premier_set_status_certified": False,
            "card_format_legality_inferred": False
        })

    if seen != REQUIRED or len(rows) != 25:
        raise ValueError(f"Missing/unexpected Duel Decks codes: {sorted(REQUIRED - seen)}")
    pending = [r for r in previous_queue if r["code"] not in seen]
    if len(pending) != 737 or len(pending) + 86 + len(rows) != 848:
        raise ValueError("Full 848-code source-status conservation failed")
    prior_boxed = [
        r for r in previous_queue
        if catalog[r["code"]]["metadata_cohort_not_official_classification"] == COHORT
    ]
    remaining_boxed = [r for r in pending if catalog[r["code"]]["metadata_cohort_not_official_classification"] == COHORT]
    if len(prior_boxed) != 95 or len(remaining_boxed) != 70:
        raise ValueError("Boxed/preconstructed cohort conservation failed")
    return {
        "schema": 1,
        "cutoff": "2026-10-29",
        "prior_audit": PREV.name,
        "source": LEDGER.name,
        "new_source_backed_product_codes": 25,
        "new_individual_duel_deck_box_codes": 21,
        "new_anthology_deck_component_codes": 4,
        "distinct_sold_duel_decks_products_represented": 22,
        "cumulative_family_source_backed_codes": 111,
        "cumulative_source_pending_codes": 737,
        "previous_boxed_source_pending": 95,
        "boxed_source_pending_after_batch": 70,
        "reviewed_duel_decks_codes": sorted(rows, key=lambda x: x["code"]),
        "remaining_source_pending_queue": pending,
        "caveats": [
            "This sources 25 frozen Scryfall code records, but only 22 separately sold products: 21 original two-deck boxes and one 2014 eight-deck Anthology.",
            "The four Anthology components have no explicit Scryfall parent_set_code. Their shared actual boxed product is separately established by Wizards' official product page and is not imputed into Scryfall metadata.",
            "Wizards' official Japanese pages verify the product family and names; each exact Scryfall code and date remains an independently sourced Scryfall crosswalk.",
            "A preconstructed release does not confer new-set premier status or card format legality.",
            "111 source-backed records and 737 pending are October 29 research-state counts, not numbers of standalone products or original card sets."
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
        raise ValueError("Committed Duel Decks audit absent or not reproducible")
    print(json.dumps({
        k: result[k] for k in (
            "new_source_backed_product_codes", "new_anthology_deck_component_codes",
            "distinct_sold_duel_decks_products_represented", "cumulative_family_source_backed_codes",
            "cumulative_source_pending_codes", "boxed_source_pending_after_batch"
        )
    }, sort_keys=True))


if __name__ == "__main__":
    main()
