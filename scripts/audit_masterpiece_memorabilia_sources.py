#!/usr/bin/env python3
"""Audit 17 specialty Scryfall masterpiece codes and two historical collectibles.

Source-backed *family* identification is not premier-release, printing-inventory,
card-legality, or even necessarily a one-code-to-one-sold-product certification.
"""
import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

DATA = Path(__file__).resolve().parent.parent / "data/set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREVIOUS = DATA / "inserts_clash_spellbook_source_audit_2026-10-29.json"
LEDGER = DATA / "masterpiece_memorabilia_sources_1993_2026.json"
OUTPUT = DATA / "masterpiece_memorabilia_source_audit_2026-10-29.json"
MASTERPIECE = {"brr", "eos", "exp", "fca", "mar", "med", "mp2", "mps",
               "mul", "otp", "puma", "pza", "soa", "spg", "sta", "wot", "zne"}
COLLECTIBLES = {"30a", "ced"}
REQUIRED = MASTERPIECE | COLLECTIBLES
EXPLICIT = {"brr", "eos", "fca", "mar", "mul", "otp", "pza", "soa", "spg", "sta", "wot", "zne"}


def encode(value):
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def official_url(url):
    parsed = urlparse(url)
    return (parsed.scheme == "https" and parsed.hostname in
            {"magic.wizards.com", "www.magic.wizards.com"} and
            (parsed.path.startswith("/en/news/") or parsed.path.startswith("/en/products/")))


def build(base, previous, ledger):
    if (base["snapshot_date"], previous["cutoff"], ledger["cutoff"]) != (
            "2026-10-29", "2026-10-29", "2026-10-29"):
        raise ValueError("Source and Scryfall snapshot dates differ")
    if (previous["cumulative_family_source_backed_codes"],
            previous["cumulative_source_pending_codes"]) != (179, 669):
        raise ValueError("Prior 179/669 exact evidence checkpoint changed")
    catalog = {r["code"]: r for r in base["all_848_released_nondigital_other_type_records"]}
    prior = {r["code"] for r in previous["remaining_source_pending_queue"]}
    if len(catalog) != 848 or len(prior) != 669 or not REQUIRED <= prior:
        raise ValueError("Frozen 848-code census or preceding pending list changed")
    seen = set()
    entries = []
    for row in ledger["records"]:
        code = row["code"]
        if code in seen or code not in REQUIRED:
            raise ValueError(f"Duplicate or unsupported source code {code}")
        seen.add(code)
        if not official_url(row["official_url"]):
            raise ValueError(f"Non-Wizards source URL for {code}")
        if len(row["official_section"]) < 68 or len(row["evidence_caution"]) < 58:
            raise ValueError(f"Insufficient individually described official evidence for {code}")
        grade = row["evidence_grade"]
        if grade not in {"wizards_article_printed_exact_set_code", "wizards_named_product_family"}:
            raise ValueError(f"Unrecognized evidence grade {code}")
        if (grade == "wizards_article_printed_exact_set_code") != (code in EXPLICIT):
            raise ValueError(f"Incorrect exact-code assertion for {code}")
        if code in EXPLICIT and code.upper() not in row["official_section"]:
            raise ValueError(f"Missing official printed set code {code}")
        meta = catalog[code]
        expected_type = "masterpiece" if code in MASTERPIECE else "memorabilia"
        if (meta["scryfall_set_type"] != expected_type or
                meta["metadata_cohort_not_official_classification"] != "promotional_and_record_extras"):
            raise ValueError(f"Frozen product family type changed for {code}")
        if code in {"med", "mar", "spg"} and "multiple" not in row["evidence_caution"].lower():
            raise ValueError(f"Ongoing collection source boundary omitted for {code}")
        if code == "30a" and "not tournament legal" not in row["official_section"].lower() and "non-tournament-legal" not in row["official_section"].lower():
            raise ValueError("Commemorative 30th Anniversary product boundary missing")
        entries.append({
            "code": code, "name": meta["name"], "scryfall_type": expected_type,
            "scryfall_first_card_date": meta["scryfall_release_or_first_card_date"],
            "scryfall_parent_code_unchanged": meta["parent_set_code_explicit_only"],
            "wizards_primary_url": row["official_url"],
            "wizards_source_section": row["official_section"],
            "evidence_grade": grade,
            "wizards_exact_code_in_source": code in EXPLICIT,
            "wizards_family_context": row["product_relation"],
            "wizards_evidence_caution": row["evidence_caution"],
            "premier_set_certified": False, "one_code_one_sold_product_certified": False,
            "complete_printing_inventory_certified": False,
            "new_card_count_certified": False, "current_legality_certified": False,
        })
    if seen != REQUIRED:
        raise ValueError(f"Missing official records: {sorted(REQUIRED - seen)}")
    remaining = [r for r in previous["remaining_source_pending_queue"] if r["code"] not in seen]
    promo_pending = [r for r in remaining if catalog[r["code"]]["metadata_cohort_not_official_classification"] == "promotional_and_record_extras"]
    promo_types = Counter(catalog[r["code"]]["scryfall_set_type"] for r in promo_pending)
    parents = sum(bool(catalog[r["code"]]["parent_set_code_explicit_only"]) for r in promo_pending)
    if (len(remaining), len(promo_pending), parents, promo_types["masterpiece"]) != (650, 626, 457, 0):
        raise ValueError("Whole-catalog, parent-linked and masterpiece counts not conserved")
    if len(entries) != 19 or len(EXPLICIT) != 12 or 198 + len(remaining) != 848:
        raise ValueError("New official source census is incorrect")
    return {
        "schema": 1, "cutoff": "2026-10-29", "previous_audit": PREVIOUS.name,
        "source_ledger": LEDGER.name, "new_source_backed_codes": 19,
        "new_exact_code_wizards_confirmations": 12,
        "new_named_family_only_code_crosswalks": 7,
        "cumulative_family_source_backed_codes": 198,
        "cumulative_source_pending_codes": 650,
        "reviewed_masterpiece_records": 17,
        "remaining_masterpiece_records": 0,
        "reviewed_memorabilia_records": 2,
        "remaining_promo_record_extras": 626,
        "remaining_promo_record_types": dict(sorted(promo_types.items())),
        "remaining_promo_parent_links_explicit_in_scryfall": parents,
        "remaining_promo_no_explicit_parent": len(promo_pending) - parents,
        "remaining_boxed_preconstructed": 11,
        "remaining_draft_starter": 11,
        "remaining_curated_reprint": 2,
        "reviewed_source_records": sorted(entries, key=lambda r: r["code"]),
        "remaining_source_pending_queue": remaining,
        "caveats": ledger["caveats"] + [
            "198 first-party cited + 650 source-pending conserves the frozen 848 released nondigital other-category Scryfall codes.",
            "A masterpiece is a Scryfall set_type label for supplemental sheets/collectibles, not proof of a separately sold premier expansion.",
            "Exactly 12 Wizards pages explicitly print a code; the other seven support named products whose Scryfall codes remain a separate metadata crosswalk.",
            "Parent counts use only Scryfall's explicit parent_set_code, never thematic name or release-date guesses.",
            "Historic product-family evidence does not establish current legality, individually new designs, or the entire physical printing inventory.",
        ],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    report = build(*(json.loads(path.read_text(encoding="utf-8"))
                     for path in (BASE, PREVIOUS, LEDGER)))
    result = encode(report)
    if args.write:
        OUTPUT.write_bytes(result)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != result:
        raise ValueError("The nineteen-code collectible audit does not reproduce")
    print(json.dumps({k: report[k] for k in (
        "new_source_backed_codes", "new_exact_code_wizards_confirmations",
        "cumulative_family_source_backed_codes", "cumulative_source_pending_codes",
        "remaining_masterpiece_records", "remaining_promo_record_extras")}, sort_keys=True))


if __name__ == "__main__":
    main()
