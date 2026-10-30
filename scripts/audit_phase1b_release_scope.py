#!/usr/bin/env python3
"""Frozen Phase 1B release-scope census and official-story-series crosswalk.

The 136 historical regular/mainline items are NOT an all-time Wizards
"premier set" count. Scryfall codes are catalog objects, not product boxes.
Titles of first-party Magic story series establish only a set-to-story-series
publication relationship, not a particular card, plot detail or timeline.
"""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
FOLDER = ROOT / "data" / "set_atlas"
OUTPUT = FOLDER / "phase1b_release_scope_story_bridge_2026-10-29.json"
SETS = FOLDER / "product_catalog_2026-10-29.json"
EARLY = FOLDER / "wotc_early_release_audit_1993_2002.json"
MID = FOLDER / "wotc_mid_release_audit_2003_2022.json"
RECENT = FOLDER / "wotc_release_classification_2026-10-29.json"
CROSS = FOLDER / "cross_category_audit_2026-10-29.json"
STORIES = ROOT / "data" / "story_index.csv"
AS_OF = "2026-10-29"

# Curated titles as printed on official Wizards story pages. Do not infer the
# same link for supplemental products, Universes Beyond or similar card names.
STORY_SERIES = {
    "bro": "The Brothers' War",
    "one": "Phyrexia: All Will Be One",
    "mom": "March of the Machine",
    "mat": "March of the Machine: The Aftermath",
    "woe": "Wilds of Eldraine",
    "lci": "The Lost Caverns of Ixalan",
    "mkm": "Murders at Karlov Manor",
    "otj": "Outlaws of Thunder Junction",
    "blb": "Bloomburrow",
    "dft": "Aetherdrift",
    "tdm": "Tarkir: Dragonstorm",
    "eoe": "Edge of Eternities",
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build(folder=FOLDER, stories_file=STORIES):
    product = read_json(folder / SETS.name)
    early = read_json(folder / EARLY.name)
    mid = read_json(folder / MID.name)
    recent = read_json(folder / RECENT.name)
    cross = read_json(folder / CROSS.name)
    sets = product["sets"]
    if len(sets) != 1062 or any(x["as_of"] != AS_OF for x in (early, mid, recent)):
        raise ValueError("Set and classification sources drift from the dated atlas")
    reviewed = {}

    def register(code, kind, source, evidence):
        if code in reviewed:
            raise ValueError(f"Repeated candidate release classification: {code}")
        if not source.startswith("https://magic.wizards.com/") and not source.startswith("https://mtg-jp.com/"):
            raise ValueError(f"Candidate lacks primary Wizards evidence: {code}")
        reviewed[code] = {"scope": kind, "primary_release_source": source,
                          "evidence_granularity": evidence}

    for item in early["records"]:
        kind = item["classification"]
        scope = ("historical_regular_mainline" if kind == "historical_regular_expansion_or_core_release"
                 else "localized_variant_provisional" if kind == "localized_core_printing_variant_pending"
                 else "documented_auxiliary_or_discarded")
        # Border-language variants are NOT first-party certified as distinct products.
        if scope == "localized_variant_provisional":
            reviewed[item["code"]] = {"scope": scope, "primary_release_source": None,
                                      "evidence_granularity": "third_party_corroborated_only"}
        else:
            register(item["code"], scope, item["source_url"], "Wizards_release_enumeration")
    for item in mid["records"]:
        scope = ("historical_regular_mainline" if item["counted_as_historical_mainline"]
                 else "documented_auxiliary_or_discarded")
        register(item["code"], scope, item["source"], "Wizards_release_enumeration")
    for item in recent["reviewed"]:
        code = item["code"]
        if code not in sets or sets[code]["scryfall_set_type"] not in ("expansion", "core"):
            continue
        if sets[code]["digital_only"] or sets[code]["release_status_as_of_cutoff"] != "released_by_cutoff":
            continue
        scope = ("historical_regular_mainline" if item["count_as_reviewed_main_release_by_cutoff"]
                 else "documented_auxiliary_or_discarded")
        register(code, scope, item["source_url"], "Wizards_bounded_2023_2026_release_review")

    exact = {code for code, obj in sets.items()
             if obj["release_status_as_of_cutoff"] == "released_by_cutoff"
             and not obj["digital_only"] and obj["scryfall_set_type"] in ("expansion", "core")}
    if set(reviewed) != exact or len(exact) != 142:
        raise ValueError("142 reviewed expansion/core candidate codes not fully conserved")

    records, counts = {}, Counter()
    for code, item in sorted(sets.items()):
        if item["release_status_as_of_cutoff"] == "announced_future":
            scope, source, evidence = "future_announced", None, "Scryfall_metadata_only"
        elif item["digital_only"]:
            scope, source, evidence = "released_digital_only", None, "Scryfall_metadata_only"
        elif code in reviewed:
            review = reviewed[code]
            scope, source, evidence = (review["scope"], review["primary_release_source"],
                                       review["evidence_granularity"])
        else:
            scope, source, evidence = "released_paper_other_category", None, "Scryfall_metadata_only"
        counts[scope] += 1
        records[code] = {
            "name": item["name"], "scryfall_set_type": item["scryfall_set_type"],
            "released_at": item["released_at"], "scope_label": scope,
            "scope_evidence": evidence, "wizards_release_source": source,
            "parent_set_code": item["parent_set_code"],
        }
    expected = {"historical_regular_mainline": 136, "documented_auxiliary_or_discarded": 4,
                "localized_variant_provisional": 2, "released_paper_other_category": 848,
                "released_digital_only": 62, "future_announced": 10}
    if dict(counts) != expected or sum(counts.values()) != 1062:
        raise ValueError("Release-scope labels do not match the frozen 1062-code partition")
    source_expected = cross["all_code_census"]["status_exclusive_partitions"]
    if (source_expected["released_nondigital_expansion_core"] != 142 or
            source_expected["released_nondigital_other_categories"] != 848 or
            source_expected["digital_only_released"] != 62 or
            source_expected["future_announced"] != 10):
        raise ValueError("Scope disagrees with the independent cross-category audit")

    with stories_file.open(encoding="utf-8", newline="") as f:
        stories = list(csv.DictReader(f))
    if len(stories) < 600:
        raise ValueError("Recovered official story index looks incomplete")
    story_links = {}
    for code, title in STORY_SERIES.items():
        if code not in records or records[code]["scope_label"] not in (
                "historical_regular_mainline", "documented_auxiliary_or_discarded"):
            raise ValueError(f"Curated story set has an unexpected release scope: {code}")
        found = [s for s in stories if s["title"].startswith(title + " | ")
                 and s["source"] == "live"]
        if not found or any(urlparse(s["url"]).hostname != "magic.wizards.com" for s in found):
            raise ValueError(f"No directly named official story series: {code}")
        story_links[code] = {
            "series_name_as_published": title, "official_story_count_in_recovered_index": len(found),
            "sample_first_party_story_sources": [{"title": s["title"], "published_date": s["date"],
                                                   "url": s["url"]} for s in found[:3]],
            "connection_scope": "Wizards story publication titled for the named release; no card-lore, plot, or in-universe chronology inference",
        }
    return {
        "schema": 1, "as_of": AS_OF, "all_set_codes": 1062,
        "scope_counts_exclusive": expected, "all_142_released_paper_expansion_core_reviewed": True,
        "all_time_premier_set_count_certified": False,
        "wizards_story_series_set_links": story_links,
        "story_series_with_primary_title_links": len(story_links),
        "set_scope_records": records,
        "source_files": [str(x.relative_to(ROOT)) for x in
                         (SETS, EARLY, MID, RECENT, CROSS, STORIES)],
        "interpretation_boundaries": [
            "136 is the reviewed historical regular/mainline subset of 142 Scryfall expansion/core candidates, not an all-time Wizards premier-set total.",
            "848 other-category paper set codes include products, promos, bonus sheets and tokens; not 848 independent booster products.",
            "fbb and 4bb are provisional localized printing variants, not independently Wizards-source-certified distinct regular mainline sets.",
            "Lore bridges link exact Wizards-named story series only; they do not prove individual card associations or in-universe timelines.",
            "The 555 optional first-party source-pending other-category product records remain uncertified and nonblocking.",
            "Snapshot is fixed at October 29 2026; later live releases or rules are not reflected.",
        ],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true", help="Regenerate the fixed dated report")
    p.add_argument("--code", help="Inspect one Scryfall set-code classification and linked story series")
    args = p.parse_args()
    report = build()
    payload = encode(report)
    if args.write:
        OUTPUT.write_bytes(payload)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != payload:
        raise ValueError("Released scope and lore bridge report differs from source ledgers")
    if args.code:
        code = args.code.lower()
        if code not in report["set_scope_records"]:
            p.error(f"Unknown frozen set code: {code}")
        print(json.dumps({"code": code, "scope": report["set_scope_records"][code],
                          "stories": report["wizards_story_series_set_links"].get(code)}, indent=2))
    else:
        print(json.dumps({"all_set_codes": report["all_set_codes"],
                          "scope_counts": report["scope_counts_exclusive"],
                          "story_series_with_primary_title_links": report["story_series_with_primary_title_links"]},
                         sort_keys=True))


if __name__ == "__main__":
    main()
