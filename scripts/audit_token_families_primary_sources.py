#!/usr/bin/env python3
"""Verify 34 named Wizards token-family source crosswalks in the frozen paper catalog."""
import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

DATA = Path(__file__).resolve().parent.parent / "data/set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREV = DATA / "art_series_primary_source_audit_2026-10-29.json"
LEDGER = DATA / "token_families_primary_sources_2023_2026.json"
OUTPUT = DATA / "token_families_primary_source_audit_2026-10-29.json"

EXPECTED_PARENTS = {
    "twoe":"woe", "twoc":"woc", "tlci":"lci", "tlcc":"lcc", "tmkm":"mkm", "tmkc":"mkc",
    "totj":"otj", "totc":"otc", "tbig":"big", "totp":"otp", "tmh3":"mh3", "tm3c":"m3c",
    "tblb":"blb", "tblc":"blc", "tdsk":"dsk", "tdsc":"dsc", "tfdn":"fdn", "tdft":"dft",
    "tdrc":"drc", "ttdm":"tdm", "ttdc":"tdc", "tfin":"fin", "tfic":"fic", "teoe":"eoe",
    "teoc":"eoc", "tspm":"spm", "tecl":"ecl", "tecc":"ecc", "ttmt":"tmt", "tsos":"sos",
    "tsoc":"soc", "tpip":"pip", "tfra":"fra", "tfrc":"frc"
}
SUPPLEMENTAL = {"tbig", "totp", "tpip"}
MAIN = {"twoe", "tlci", "tmkm", "totj", "tmh3", "tblb", "tdsk", "tfdn",
        "tdft", "ttdm", "tfin", "teoe", "tspm", "tecl", "ttmt", "tsos", "tfra"}
COMMANDER = set(EXPECTED_PARENTS) - MAIN - SUPPLEMENTAL


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def valid_wizards_token_page(url):
    parsed = urlparse(url)
    return (parsed.scheme == "https" and parsed.hostname == "magic.wizards.com" and
            parsed.path.startswith("/en/news/card-preview/") and
            ("tokens" in parsed.path or "token" in parsed.path))


def build(base, prev, ledger):
    if (base["snapshot_date"], prev["cutoff"], ledger["cutoff"]) != ("2026-10-29",) * 3:
        raise ValueError("Token source cutoff differs from the frozen paper catalog")
    if (prev["cumulative_family_source_backed_codes"], prev["cumulative_source_pending_codes"],
            prev["remaining_promo_record_extras"], prev["remaining_promo_parent_linked_explicit"],
            prev["remaining_promo_without_explicit_parent"]) != (259, 589, 565, 419, 146):
        raise ValueError("Prior art-series source review checkpoint drift")
    catalog = {r["code"]: r for r in base["all_848_released_nondigital_other_type_records"]}
    previous_pending = prev["remaining_source_pending_queue"]
    old_pending_codes = {r["code"] for r in previous_pending}
    if len(catalog) != 848 or len(previous_pending) != 589 or not set(EXPECTED_PARENTS) <= old_pending_codes:
        raise ValueError("Frozen 848-code catalog or token-pending membership drift")
    reviewed, seen = [], set()
    for source in ledger["records"]:
        code = source["code"]
        if code in seen or code not in EXPECTED_PARENTS:
            raise ValueError(f"Duplicate or unapproved token group {code}")
        seen.add(code)
        if not valid_wizards_token_page(source["official_url"]):
            raise ValueError(f"Missing direct first-party Wizards token article {code}")
        expected_context = ("main_booster" if code in MAIN else
                            "commander_decks" if code in COMMANDER else
                            "supplemental_product" if code == "tpip" else "supplemental_booster")
        if source["token_context"] != expected_context:
            raise ValueError(f"Wrong product context for distinct token family {code}")
        if len(source["named_product"]) < 17 or len(source["specific_source_note"]) < 78:
            raise ValueError(f"Token source lacks concrete family-specific evidence {code}")
        row = catalog[code]
        if (row["scryfall_set_type"] != "token" or
                row["metadata_cohort_not_official_classification"] != "promotional_and_record_extras" or
                row["parent_set_code_explicit_only"] != EXPECTED_PARENTS[code] or
                "Token" not in row["name"]):
            raise ValueError(f"Token type, parent link, or cohort mismatch for {code}")
        reviewed.append({
            "code": code,
            "name": row["name"],
            "scryfall_type": row["scryfall_set_type"],
            "scryfall_earliest_card_date": row["scryfall_release_or_first_card_date"],
            "scryfall_parent_set_code_explicit_only_unchanged": row["parent_set_code_explicit_only"],
            "official_source_url": source["official_url"],
            "officially_named_token_family": source["named_product"],
            "wizards_product_context": source["token_context"],
            "source_grade": "wizards_named_token_product_family_only",
            "source_note": source["specific_source_note"],
            "wizards_prints_exact_scryfall_token_code": False,
            "standalone_premier_expansion_certified": False,
            "individual_token_printing_inventory_certified": False,
            "new_playable_card_debut_count_certified": False,
            "current_format_legality_certified": False,
        })
    if seen != set(EXPECTED_PARENTS) or len(reviewed) != 34:
        raise ValueError(f"Incomplete token evidence cohort: {sorted(set(EXPECTED_PARENTS) - seen)}")
    pending = [r for r in previous_pending if r["code"] not in seen]
    promo = [r for r in pending if catalog[r["code"]]["metadata_cohort_not_official_classification"] == "promotional_and_record_extras"]
    linked = sum(bool(catalog[r["code"]]["parent_set_code_explicit_only"]) for r in promo)
    if (len(pending), len(promo), linked, len(promo) - linked) != (555, 531, 385, 146):
        raise ValueError("Token review would corrupt bounded other-category or parent-linked counts")
    return {
        "schema": 1, "cutoff": "2026-10-29", "previous_audit": PREV.name,
        "source_ledger": LEDGER.name, "new_source_backed_codes": 34,
        "new_named_family_wizards_crosswalks": 34, "new_exact_wizards_token_code_declarations": 0,
        "source_backed_token_families_this_batch": 34,
        "official_token_articles_cited": len({r["official_source_url"] for r in reviewed}),
        "cumulative_family_source_backed_codes": 293, "cumulative_source_pending_codes": 555,
        "remaining_promo_record_extras": len(promo),
        "remaining_promo_parent_linked_explicit": linked,
        "remaining_promo_without_explicit_parent": len(promo) - linked,
        "remaining_promo_types": dict(sorted(Counter(r["scryfall_type"] for r in promo).items())),
        "remaining_boxed_preconstructed": 11, "remaining_draft_starter": 11,
        "remaining_curated_reprints": 2,
        "reviewed_token_product_families": sorted(reviewed, key=lambda r: r["code"]),
        "remaining_source_pending_queue": pending,
        "caveats": ledger["caveats"] + [
            "Exactly 293 individually family-sourced plus 555 source-pending records conserve 848 non-digital English-paper other-category Scryfall codes from the frozen 2026-10-29 audit.",
            "All 34 token groups have explicit Scryfall parent codes, but Wizards did not declare those literal t-prefixed Scryfall catalog codes.",
            "Earlier 259 source reviews, Scryfall code dates, parent links, legal statuses, and all Grixis approved decks remain unchanged."
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = build(*(json.loads(path.read_text(encoding="utf-8")) for path in (BASE, PREV, LEDGER)))
    value = encode(report)
    if args.write:
        OUTPUT.write_bytes(value)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != value:
        raise ValueError("Token source-family report differs from deterministic recomputation")
    print(json.dumps({key: report[key] for key in (
        "new_source_backed_codes", "official_token_articles_cited", "cumulative_family_source_backed_codes",
        "cumulative_source_pending_codes", "remaining_promo_record_extras",
        "remaining_promo_parent_linked_explicit", "remaining_promo_without_explicit_parent")}, sort_keys=True))


if __name__ == "__main__":
    main()
