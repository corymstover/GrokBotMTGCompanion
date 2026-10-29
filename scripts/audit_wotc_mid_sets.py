#!/usr/bin/env python3
"""Reconcile every 2003–2022 Scryfall expansion/core candidate with Wizards.

Yearly Wizards retrospective lists are historical primary-source evidence
of randomized releases. This is NOT a claim that every release was marketed
as a "premier set" at its original date. The lone integrated bonus-sheet
exception, Time Spiral Timeshifted, is tracked as a separate Scryfall code.
"""
import argparse
import json
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data/set_atlas"
EVIDENCE = DATA / "wotc_mid_release_evidence_2003_2022.json"
CATALOG = DATA / "product_catalog_2026-10-29.json"
EARLY = DATA / "wotc_early_release_audit_1993_2002.json"
RECENT = DATA / "wotc_release_classification_2026-10-29.json"
OUT = DATA / "wotc_mid_release_audit_2003_2022.json"

AS_OF = date(2026, 10, 29)
REGULAR = "historical_regular_expansion_or_core_release"
BONUS = "integrated_bonus_sheet_not_an_independent_regular_release"
EXPECTED = {REGULAR: 80, BONUS: 1}
WOTC_SOURCES = {
    "https://magic.wizards.com/en/news/making-magic/looking-back-part-1",
    "https://magic.wizards.com/en/news/making-magic/looking-back-part-2",
    "https://magic.wizards.com/en/news/making-magic/trivial-pursuit-more-or-less",
}


def encode(document):
    return (json.dumps(document, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build(evidence, catalog, early, recent):
    if evidence.get("schema") != 1 or evidence.get("as_of") != AS_OF.isoformat():
        raise ValueError("Mid-history source date/schema mismatch")
    if catalog.get("snapshot_date") != AS_OF.isoformat() or early.get("as_of") != AS_OF.isoformat() or recent.get("as_of") != AS_OF.isoformat():
        raise ValueError("Historical audits have incompatible snapshot dates")

    candidates = {
        code for code, obj in catalog["sets"].items()
        if not obj.get("scryfall_set_metadata_missing")
        and obj["scryfall_set_type"] in ("expansion", "core")
        and obj["digital_only"] is False
        and obj["release_status_as_of_cutoff"] == "released_by_cutoff"
    }
    mid_candidates = {
        code for code in candidates if 2003 <= date.fromisoformat(catalog["sets"][code]["released_at"]).year <= 2022
    }
    seen = set()
    counts = Counter()
    rows = []
    for source_row in evidence.get("records", []):
        code = source_row["code"]
        if code in seen:
            raise ValueError(f"Duplicate reviewed Scryfall code: {code}")
        if code not in mid_candidates:
            raise ValueError(f"2003–2022 candidate missing or out of scope: {code}")
        source = source_row.get("source")
        if urlparse(source or "").hostname != "magic.wizards.com" or source not in WOTC_SOURCES:
            raise ValueError(f"Missing or unknown Wizards primary source: {code}")
        if not source_row.get("source_section") or not source_row.get("reason"):
            raise ValueError(f"No exact citation section for {code}")
        claim = source_row.get("claim")
        if claim not in EXPECTED:
            raise ValueError(f"Unrecognized early release relationship for {code}")
        item = catalog["sets"][code]
        year = date.fromisoformat(item["released_at"]).year
        if year != source_row.get("year"):
            raise ValueError(f"Year mismatch for {code}")
        if claim == REGULAR and source_row["evidence_level"] != "Wizards_primary_release_enumeration":
            raise ValueError(f"Unsupported mainline claim for {code}")
        if claim == BONUS:
            if code != "tsb" or source_row["evidence_level"] != "Wizards_explicit_bonus_sheet_description":
                raise ValueError("Integrated timeshifted sheet cannot be silently counted as a main release")
            if source != "https://magic.wizards.com/en/news/making-magic/looking-back-part-1":
                raise ValueError("Time Spiral bonus-sheet source must remain primary")
        elif code == "tsb":
            raise ValueError("Time Spiral Timeshifted must be classified as bonus sheet")

        seen.add(code)
        counts[claim] += 1
        rows.append({
            "code": code, "name": item["name"], "release_year": year,
            "scryfall_type": item["scryfall_set_type"], "released_at": item["released_at"],
            "classification": claim, "evidence_level": source_row["evidence_level"],
            "source": source, "source_section": source_row["source_section"],
            "reviewer_note": source_row["reason"],
            "counted_as_historical_mainline": claim == REGULAR
        })
    if mid_candidates != seen:
        raise ValueError(f"Unreviewed middle-era candidates: {sorted(mid_candidates - seen)}")
    if dict(counts) != EXPECTED:
        raise ValueError(f"Unexpected middle-era classifications: {dict(counts)}")
    earlier = early["combined_full_snapshot"]
    current = recent["summary"]
    if earlier["not_yet_reviewed_2003_2022"] != 81 or current["scryfall_released_nondigital_expansion_core_candidates_all_history"] != 142:
        raise ValueError("Historical baseline counts changed")
    mainline = earlier["reviewed_mainline_1993_2002_plus_2023_2026"] + counts[REGULAR]
    auxiliary = earlier["directly_documented_auxiliary_or_discarded"] + counts[BONUS]
    provisional = earlier["provisional_foreign_border_variants"]
    if (mainline, auxiliary, provisional) != (136, 4, 2) or mainline + auxiliary + provisional != 142:
        raise ValueError("End-to-end source-backed partition does not reconcile")
    return {
        "schema": 1, "as_of": AS_OF.isoformat(), "period": "2003-2022",
        "wizards_retroactive_marketing_caveat": "historical regular booster/core series is not the same as a contemporaneous premier-set designation",
        "period_candidates": len(mid_candidates),
        "period_reviewed_regular_expansion_core": counts[REGULAR],
        "period_integrated_bonus_sheets": counts[BONUS],
        "combined_candidate_classification": {
            "scryfall_released_nondigital_expansion_core": len(candidates),
            "wotc_supported_historical_regular_or_mainline_releases": mainline,
            "directly_sourced_auxiliary_discarded_or_integrated_sheets": auxiliary,
            "provisional_border_language_variants": provisional,
            "wholly_unreviewed_within_this_142_code_scope": 0,
            "all_time_premier_status_certified": False
        },
        "records": sorted(rows, key=lambda x: (x["released_at"], x["code"])),
        "caveats": [
            "This exhausts the 142-code Scryfall released nondigital expansion/core candidate denominator, not all Magic products and not the all-time count of modern premier products.",
            "FBB and 4BB remain provisional localized-printing cases and are not certified as separate premier/core editions.",
            "Wizards 'Looking Back' lists randomized booster releases, including nonpremier products; exact Scryfall expansion/core filtering and the separate complete core-edition list prevent such entries from silently joining this count.",
            "Time Spiral Timeshifted is an integrated bonus sheet, not a second independent expansion.",
            "Regular expansion/core releases from 1993-2022 predate or overlap changing Wizards terminology. Retroactive premier labels need separate period-specific criteria.",
            "The October 29 catalog uses Scryfall Set API data obtained later the same day as the archived card bulk; preserved snapshot dates do not prove original publication dates for every printing."
        ]
    }


def run(write=False):
    evidence = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    early = json.loads(EARLY.read_text(encoding="utf-8"))
    recent = json.loads(RECENT.read_text(encoding="utf-8"))
    serialized = encode(build(evidence, catalog, early, recent))
    if write:
        OUT.write_bytes(serialized)
    elif not OUT.exists() or OUT.read_bytes() != serialized:
        raise ValueError("Committed middle-era report is missing or not reproducible")
    print(json.dumps(json.loads(serialized)["combined_candidate_classification"], indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    run(parser.parse_args().write)
