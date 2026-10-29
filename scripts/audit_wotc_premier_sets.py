#!/usr/bin/env python3
"""Rebuild the bounded, Wizards-evidenced MTG release classification.

This is a reviewed 2023-2026 sample, not a full historical premier count.
It never infers Premier from Scryfall's expansion/core set_type alone.
"""
import argparse
import json
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "set_atlas"
EVIDENCE = DATA / "wotc_reviewed_release_evidence_2026-10-29.json"
CATALOG = DATA / "product_catalog_2026-10-29.json"
OUT = DATA / "wotc_release_classification_2026-10-29.json"
AS_OF = date(2026, 10, 29)

MAIN = {"official_main_set_release", "official_universes_beyond_main_release", "official_2023_main_set"}
NON_MAIN = {"official_epilogue_micro_set", "official_main_set_subset",
            "official_digital_universes_within_counterpart", "official_special_product"}
FUTURE = {"official_upcoming_main_release"}
ALL = MAIN | NON_MAIN | FUTURE
EXPECTED = {"official_main_set_release": 13, "official_universes_beyond_main_release": 6,
            "official_2023_main_set": 2, "official_epilogue_micro_set": 1,
            "official_main_set_subset": 1, "official_digital_universes_within_counterpart": 1,
            "official_special_product": 4, "official_upcoming_main_release": 2}


def encoding(value):
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build(evidence, catalog):
    if evidence.get("schema") != 1 or evidence.get("as_of") != AS_OF.isoformat():
        raise ValueError("Incorrect date or schema for reviewed WotC records")
    if catalog.get("snapshot_date") != AS_OF.isoformat():
        raise ValueError("Underlying dated product catalog is not the reviewed snapshot")
    groups = Counter()
    used = set()
    results = []
    for item in evidence["records"]:
        code = item["code"]
        group = item["group"]
        if code in used:
            raise ValueError(f"Duplicate reviewed set code: {code}")
        if group not in ALL:
            raise ValueError(f"Unknown release group: {group}")
        if code not in catalog["sets"]:
            raise ValueError(f"Reviewed code {code} absent in Scryfall printings catalog")
        uri = item.get("source")
        domain = urlparse(uri or "").hostname
        if domain not in ("magic.wizards.com", "www.magic.wizards.com"):
            raise ValueError(f"Non-Wizards source for {code}: {uri}")
        if not item.get("source_section"):
            raise ValueError(f"No official-source section for {code}")
        s = catalog["sets"][code]
        if s.get("scryfall_set_metadata_missing"):
            raise ValueError(f"No independent Set API metadata for {code}")
        released = s["release_status_as_of_cutoff"] == "released_by_cutoff"
        kind = s["scryfall_set_type"]
        if group in MAIN and (not released or s["digital_only"] or kind not in ("expansion", "core")):
            raise ValueError(f"Main release has inconsistent date/media/type: {code}")
        if group in FUTURE and released:
            raise ValueError(f"Upcoming set is already released by cutoff: {code}")
        if group == "official_digital_universes_within_counterpart" and not s["digital_only"]:
            raise ValueError(f"Digital counterpart is not digital: {code}")
        if group == "official_main_set_subset" and kind not in ("expansion", "core"):
            raise ValueError(f"Subdivision is not Scryfall expansion/core: {code}")
        if group == "official_epilogue_micro_set" and kind not in ("expansion", "core"):
            raise ValueError(f"Epilogue is not Scryfall expansion/core: {code}")
        used.add(code)
        groups[group] += 1
        results.append({
            "code": code, "name": s["name"], "official_product_group": group,
            "scryfall_type": kind, "scryfall_released_at": s["released_at"],
            "scryfall_digital": s["digital_only"],
            "publication_status": "released" if released else "future",
            "source_url": uri, "source_section": item["source_section"],
            "evidence_note": item.get("reason"),
            "count_as_reviewed_main_release_by_cutoff": group in MAIN,
            "note": "reviewed historical scope only; no universal premier census"
        })
    if dict(groups) != EXPECTED:
        raise ValueError(f"Reviewed source coverage changed: {dict(groups)}")
    base_candidates = {
        code for code, item in catalog["sets"].items()
        if not item.get("scryfall_set_metadata_missing")
        and item["scryfall_set_type"] in ("expansion", "core")
        and not item["digital_only"]
        and item["release_status_as_of_cutoff"] == "released_by_cutoff"
    }
    main_codes = {x["code"] for x in results if x["official_product_group"] in MAIN}
    nonmain_expansion = {x["code"] for x in results if x["official_product_group"] in (
        "official_main_set_subset", "official_epilogue_micro_set")}
    if len(base_candidates) != 142 or len(main_codes) != 21 or len(nonmain_expansion) != 2:
        raise ValueError("Expected curated baseline no longer matches frozen Scryfall data")
    if not main_codes <= base_candidates or not nonmain_expansion <= base_candidates:
        raise ValueError("Curated code absent from frozen eligible expansion/core subset")
    classified = {x["code"]: x for x in results}
    data = {
        "schema": 1, "as_of": AS_OF.isoformat(),
        "authority": "Wizards primary release/product pages; Scryfall source data for code, type, date, printings",
        "scope": "Reviewed 2023-2026 official release-family batch; earlier 1993-2022 product history not yet certified",
        "summary": {
            "all_scryfall_set_codes": len(catalog["sets"]),
            "wotc_reviewed_codes": len(used),
            "wotc_reviewed_released_main_set_codes_2023_2026": len(main_codes),
            "wotc_reviewed_2026_upcoming_main_codes": groups["official_upcoming_main_release"],
            "scryfall_released_nondigital_expansion_core_candidates_all_history": len(base_candidates),
            "reviewed_expansion_core_auxiliary_not_a_main_release": len(nonmain_expansion),
            "unreviewed_released_nondigital_expansion_core_candidates": len(base_candidates - main_codes - nonmain_expansion),
            "all_set_codes_not_curated_in_this_batch": len(catalog["sets"]) - len(used),
            "official_groups": dict(sorted(groups.items()))
        },
        "reviewed": sorted(results, key=lambda x: (x["scryfall_released_at"] or "", x["code"])),
        "unreviewed_released_nondigital_expansion_core_codes": sorted(base_candidates - main_codes - nonmain_expansion),
        "caveats": [
            "The reviewed 21 codes are a bounded 2023-2026 official-main-release inventory, not the all-time premier set count.",
            "A Standard-legal epilogue or subset is not thereby a separate regularly scheduled main release.",
            "The 142 Scryfall expansion/core candidates are not automatically all Wizards premier products.",
            "Scryfall's /sets data was fetched later on the same date than Default Cards; dates and fields remain source-separated.",
            "All unreviewed codes remain unclassified, not silently presumed standard or supplemental.",
            "Future products are excluded from 2026 released counts; lore chronology is not determined from publication order."
        ]
    }
    return data


def run(write=False):
    evidence = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    atlas = json.loads(CATALOG.read_text(encoding="utf-8"))
    result = build(evidence, atlas)
    output = encoding(result)
    if write:
        OUT.write_bytes(output)
    elif not OUT.exists() or OUT.read_bytes() != output:
        raise ValueError("Committed release classification does not match the reviewed evidence")
    print(json.dumps(result["summary"], indent=2, sort_keys=True))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    run(p.parse_args().write)
