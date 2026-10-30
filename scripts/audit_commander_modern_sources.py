#!/usr/bin/env python3
"""Reproduce nineteen Wizards-backed 2023–2026 Commander family reviews."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREV = DATA / "commander_set_linked_source_audit_2026-10-29.json"
LEDGER = DATA / "commander_modern_sources_2023_2026.json"
OUT = DATA / "commander_modern_source_audit_2026-10-29.json"
REQUIRED = {
    "onc", "moc", "woc", "who", "lcc", "mkc", "otc", "m3c", "blc", "dsc",
    "fdc", "drc", "tdc", "fic", "eoc", "ecc", "soc", "msc", "frc",
}
COHORT = "preconstructed_and_boxed"


def encode(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def build(base, previous, ledger):
    if (base.get("snapshot_date"), previous.get("cutoff"), ledger.get("cutoff")) != (
            "2026-10-29", "2026-10-29", "2026-10-29"):
        raise ValueError("Historical snapshot/date mismatch")
    if (previous.get("cumulative_family_source_backed_codes"),
            previous.get("cumulative_source_pending_codes"),
            previous.get("boxed_source_pending_after_batch")) != (132, 716, 49):
        raise ValueError("Prior twelve Commander records were changed")
    old = previous["remaining_source_pending_queue"]
    pending = {r["code"] for r in old}
    catalog = {r["code"]: r for r in base["all_848_released_nondigital_other_type_records"]}
    if len(old) != 716 or len(pending) != 716 or len(catalog) != 848:
        raise ValueError("Original metadata source-pending queue changed")
    seen = set()
    urls = set()
    verified = []
    for evidence in ledger["records"]:
        code = evidence.get("code")
        if code in seen:
            raise ValueError(f"Duplicate Commander source code: {code}")
        if code not in REQUIRED or code not in pending:
            raise ValueError(f"Unsupported or already reviewed Commander code: {code}")
        url = evidence.get("official_url", "")
        parsed = urlparse(url)
        if (parsed.scheme != "https" or parsed.hostname not in
                ("magic.wizards.com", "www.magic.wizards.com") or
                not parsed.path.startswith("/en/news/")):
            raise ValueError(f"Not a direct Wizards source for {code}")
        if url in urls:
            raise ValueError(f"Duplicate official page reused for distinct Commander release: {code}")
        section = evidence.get("source_section", "")
        if "Commander" not in section or len(section) < 28:
            raise ValueError(f"Missing exact Commander product section: {code}")
        meta = catalog[code]
        if meta["metadata_cohort_not_official_classification"] != COHORT or meta["scryfall_set_type"] != "commander":
            raise ValueError(f"Unexpected type or cohort for Commander {code}")
        if code == "fdc":
            difference = evidence.get("date_relationship", "")
            if not all(x in difference for x in ("2026", "2024", "October 2", "November 15")):
                raise ValueError("FDC cross-year product/date caveat must be retained")
            if meta["scryfall_release_or_first_card_date"] != "2024-11-15":
                raise ValueError("FDC earliest-card source metadata changed")
        elif evidence.get("date_relationship"):
            raise ValueError(f"Unexpected temporal-source note for {code}")
        verified.append({
            "code": code,
            "name": meta["name"],
            "scryfall_type": meta["scryfall_set_type"],
            "scryfall_release_or_first_card_date": meta["scryfall_release_or_first_card_date"],
            "scryfall_explicit_parent_code_unchanged": meta["parent_set_code_explicit_only"],
            "wizards_primary_url": url,
            "wizards_article_section": section,
            "wizards_product_family_supported": "commander_preconstructed_product_line",
            "wizards_source_note": (
                "The official page identifies this marketed Commander deck product family. "
                "The Scryfall code, first-card date and parent link come independently from the frozen "
                "October 29 snapshot. Wizards page evidence is not a card-by-card printing or legality audit."
            ),
            "wizards_versus_scryfall_date_relationship": evidence.get("date_relationship"),
            "wizards_exact_scryfall_code_confirmed": False,
            "exact_deck_printing_inventory_certified": False,
            "new_card_count_certified": False,
            "card_legality_inferred": False,
            "premier_set_certified": False,
            "evidence_grade": "wizards_direct_commander_decklist_scryfall_family_crosswalk",
        })
        seen.add(code)
        urls.add(url)
    if seen != REQUIRED or len(verified) != 19:
        raise ValueError(f"Modern Commander source audit missing codes: {sorted(REQUIRED-seen)}")
    remaining = [r for r in old if r["code"] not in seen]
    boxed = [r for r in remaining if catalog[r["code"]]["metadata_cohort_not_official_classification"] == COHORT]
    commander_remaining = [r for r in remaining if catalog[r["code"]]["scryfall_set_type"] == "commander"]
    if len(remaining) != 697 or len(boxed) != 30 or commander_remaining or 151 + len(remaining) != 848:
        raise ValueError("All 848 records, boxed queue or Commander-type queue conservation failed")
    return {
        "schema": 1,
        "cutoff": "2026-10-29",
        "prior_audit": PREV.name,
        "source": LEDGER.name,
        "new_source_backed_commander_product_family_codes": 19,
        "cumulative_family_source_backed_codes": 151,
        "cumulative_source_pending_codes": 697,
        "previous_boxed_source_pending": 49,
        "boxed_source_pending_after_batch": 30,
        "remaining_commander_type_source_pending": 0,
        "reviewed_commander_modern_codes": sorted(verified, key=lambda x: x["code"]),
        "remaining_source_pending_queue": remaining,
        "caveats": [
            "Nineteen Scryfall commander-type codes are not nineteen individual decks, nineteen premier sets or nineteen certified product print inventories.",
            "FDC Scryfall earliest-card metadata says 2024-11-15, while Wizards' five Foundations Commander boxed decks went on sale 2026-10-02. This is an intentionally preserved cross-year distinction, not evidence of 2024 boxed deck sales.",
            "All official product-family links and Scryfall metadata remain independent: Wizards sources do not necessarily print Scryfall's three-letter code.",
            "Legality, decklist printing versions, debut counts, and precise set-level first printings remain separately uncertified.",
            "151 source-backed plus 697 source-pending conserves all 848 frozen non-expansion/core released paper codes.",
        ],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    report = build(*(json.loads(path.read_text(encoding="utf-8")) for path in (BASE, PREV, LEDGER)))
    payload = encode(report)
    if args.write:
        OUT.write_bytes(payload)
    elif not OUT.exists() or OUT.read_bytes() != payload:
        raise ValueError("Committed 2023–2026 Commander source report is not reproducible")
    print(json.dumps({key: report[key] for key in (
        "new_source_backed_commander_product_family_codes", "cumulative_family_source_backed_codes",
        "cumulative_source_pending_codes", "boxed_source_pending_after_batch",
        "remaining_commander_type_source_pending")}, sort_keys=True))


if __name__ == "__main__":
    main()
