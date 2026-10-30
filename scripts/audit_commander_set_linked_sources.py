#!/usr/bin/env python3
"""Reproduce twelve source-backed 2020–2022 Commander precon family reviews."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREV = DATA / "commander_series_source_audit_2026-10-29.json"
LEDGER = DATA / "commander_set_linked_sources_2020_2022.json"
OUT = DATA / "commander_set_linked_source_audit_2026-10-29.json"
REQUIRED = {"znc", "khc", "c21", "afc", "mic", "voc", "nec", "ncc", "dmc", "40k", "brc", "scd"}
COHORT = "preconstructed_and_boxed"


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build(base, previous, ledger):
    if any(x != "2026-10-29" for x in (
        base.get("snapshot_date"), previous.get("cutoff"), ledger.get("cutoff")
    )):
        raise ValueError("Mismatched historical snapshot cutoff")
    if (previous.get("cumulative_family_source_backed_codes"),
            previous.get("cumulative_source_pending_codes"),
            previous.get("boxed_source_pending_after_batch")) != (120, 728, 61):
        raise ValueError("Previous Commander series checkpoint changed")
    old = previous["remaining_source_pending_queue"]
    pending_codes = {r["code"] for r in old}
    if len(old) != 728 or len(pending_codes) != len(old):
        raise ValueError("Original source-pending rows missing or duplicated")
    catalog = {r["code"]: r for r in base["all_848_released_nondigital_other_type_records"]}
    if len(catalog) != 848:
        raise ValueError("Frozen Scryfall source catalog changed")

    verified = []
    seen = set()
    seen_urls = set()
    for evidence in ledger["records"]:
        code = evidence.get("code")
        if code in seen:
            raise ValueError(f"Duplicate product code: {code}")
        if code not in REQUIRED or code not in pending_codes:
            raise ValueError(f"Unsupported or already-reviewed code: {code}")
        url = evidence.get("official_url", "")
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.hostname not in ("magic.wizards.com", "www.magic.wizards.com") or not parsed.path.startswith("/en/news/"):
            raise ValueError(f"Not a direct Wizards article: {code}")
        if url in seen_urls:
            raise ValueError(f"Duplicate URL improperly reused for distinct product: {code}")
        section = evidence.get("source_section", "")
        if "Commander" not in section or len(section) < 25:
            raise ValueError(f"Missing precise product/decklist citation: {code}")
        meta = catalog[code]
        if meta["metadata_cohort_not_official_classification"] != COHORT or meta["scryfall_set_type"] != "commander":
            raise ValueError(f"Wrong Scryfall category or research cohort: {code}")
        seen.add(code)
        seen_urls.add(url)
        verified.append({
            "code": code,
            "name": meta["name"],
            "scryfall_type": meta["scryfall_set_type"],
            "scryfall_release_or_first_card_date": meta["scryfall_release_or_first_card_date"],
            "scryfall_explicit_parent_code_unchanged": meta["parent_set_code_explicit_only"],
            "wizards_primary_url": url,
            "wizards_article_section": section,
            "product_family_wizards_supported": "set_linked_or_starter_commander_preconstructed_release",
            "wizards_source_note": (
                "Wizards' own release announcement or decklist article identifies the named Commander "
                "preconstructed product line. The exact Scryfall set code/date and printing index are separate "
                "metadata; interactive Gatherer decklists may display later card printings."
            ),
            "evidence_grade": "wizards_direct_commander_product_or_decklist_scryfall_code_crosswalk",
            "wizards_exact_scryfall_code_confirmed": False,
            "decklist_exact_card_printing_inventory_certified": False,
            "new_card_count_certified": False,
            "card_legality_inferred": False,
            "premier_set_certified": False,
        })
    if seen != REQUIRED or len(verified) != 12:
        raise ValueError(f"Missing or extra Commander set-linked code: {sorted(REQUIRED-seen)}")
    remaining = [r for r in old if r["code"] not in seen]
    boxed = [r for r in remaining if catalog[r["code"]]["metadata_cohort_not_official_classification"] == COHORT]
    if len(remaining) != 716 or len(boxed) != 49 or 132 + len(remaining) != 848:
        raise ValueError("Full 848-code partition or boxed cohort conservation failed")
    return {
        "schema": 1,
        "cutoff": "2026-10-29",
        "prior_audit": PREV.name,
        "source": LEDGER.name,
        "new_source_backed_commander_release_codes": 12,
        "cumulative_family_source_backed_codes": 132,
        "cumulative_source_pending_codes": 716,
        "previous_boxed_source_pending": 61,
        "boxed_source_pending_after_batch": 49,
        "reviewed_commander_set_linked_codes": sorted(verified, key=lambda x: x["code"]),
        "remaining_source_pending_queue": remaining,
        "caveats": [
            "The twelve 2020–2022 Commander product-family records are not twelve single decks or premier expansion sets.",
            "Wizards article text establishes the marketed products; the precise Scryfall code, first-card date and parent_set_code are sourced independently from the frozen October 29 metadata.",
            "Wizards explicitly warns that interactive Gatherer decklists can show later printings of cards. Source-family validation is not a card-by-card box-printing certification.",
            "No claims are inferred about new card counts, Commander legality of every printing or the Standard/Modern legality of cards in these supplemental products.",
            "132 backed plus 716 pending conserves all 848 non-expansion/core released paper Scryfall codes."
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = build(*(json.loads(p.read_text(encoding="utf-8")) for p in (BASE, PREV, LEDGER)))
    blob = encode(report)
    if args.write:
        OUT.write_bytes(blob)
    elif not OUT.exists() or OUT.read_bytes() != blob:
        raise ValueError("Committed 2020–2022 Commander source audit is not reproducible")
    print(json.dumps({
        k: report[k] for k in (
            "new_source_backed_commander_release_codes", "cumulative_family_source_backed_codes",
            "cumulative_source_pending_codes", "boxed_source_pending_after_batch"
        )
    }, sort_keys=True))


if __name__ == "__main__":
    main()
