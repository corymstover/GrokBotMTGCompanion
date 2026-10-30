#!/usr/bin/env python3
"""Read-only Phase 1B release-gate audit of the published, immutable set/printing indexes.

This audit verifies released English-paper per-set count parity at the October 29
cutoff, 32 published index hashes, metadata partitions, and representative live
lookups. It does NOT claim a card-ID diff against missing newer bulk source bytes.
"""
import argparse
import hashlib
import json
from datetime import date
from pathlib import Path

from historical_set_lookup import card_query, set_query

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data/set_atlas"
CURRENT = DATA / "catalog_2026-10-29.json"
CURRENT_AUDIT = DATA / "audit_2026-10-29.json"
HISTORICAL = DATA / "historical_shard_audit_2026-10-29.json"
CATEGORY = DATA / "cross_category_audit_2026-10-29.json"
PRODUCT = DATA / "product_audit_2026-10-29.json"
FAMILY = DATA / "token_families_primary_source_audit_2026-10-29.json"
OUTPUT = DATA / "phase1b_fasttrack_readiness_2026-10-29.json"
CUTOFF = date(2026, 10, 29)

SMOKE_CODES = ("lea", "leg", "c21", "40k", "pznr", "tfin", "ydmu", "trk", "fbb")
EXPECTED_DELTAS = {
    "pf26": (2, 2), "pw26": (1, 1), "sds": (25, 25),
    "trc": (121, 121), "trk": (43, 49)
}


def serialize(obj):
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def build(current, current_audit, historical, category, product, family,
          index_folder=DATA, run_lookups=True):
    if (current["as_of"], current_audit["audit_date"], historical["cutoff"],
            category["snapshot_date"], family["cutoff"]) != (CUTOFF.isoformat(),) * 5:
        raise ValueError("Snapshot cutoffs differ; cannot fast-track without dated evidence")
    if current["source_sha256"] != current_audit["source"]["sha256"]:
        raise ValueError("Current catalog and verified bulk manifest SHA disagree")
    old, new = historical["per_set"], current["sets"]
    if set(old) != set(new) or len(old) != 1062:
        raise ValueError("All 1,062 historical and current set codes must match exactly")
    report_deltas = {}
    count_disagreements = []
    old_all = old_en = old_released = new_all = new_en = new_released = 0
    for code in sorted(new):
        prior, now = old[code], new[code]
        a, e, released = prior["all"], prior.get("english_paper", 0), prior.get("released_english_paper", 0)
        b, f, current_released = now["printings"], now["english_paper"], now["released_english_paper"]
        old_all += a; old_en += e; old_released += released
        new_all += b; new_en += f; new_released += current_released
        if released != current_released:
            count_disagreements.append({"code": code, "historical": released, "current": current_released})
        if (b - a, f - e) != (0, 0):
            report_deltas[code] = {"all_printing_delta": b - a, "english_paper_delta": f - e,
                                   "historical_released_english_paper": released,
                                   "current_released_english_paper": current_released}
    if count_disagreements:
        raise ValueError(f"Released per-set count differences require card-level reconciliation: {count_disagreements}")
    if ({k: (v["all_printing_delta"], v["english_paper_delta"]) for k, v in report_deltas.items()}
            != EXPECTED_DELTAS):
        raise ValueError("Unexpected changed set codes or preview deltas")
    if (old_all, old_en, old_released, new_all, new_en, new_released) != (
            119509, 107700, 106855, 119701, 107898, 106855):
        raise ValueError("Verified historical/current released total reconciliation failed")
    if current_audit["snapshot"]["released_english_paper"] != new_released:
        raise ValueError("Current audit and catalog released printing totals differ")
    if historical["released_english_paper"] != old_released:
        raise ValueError("Published historical audit released printing total differs")
    if ((new_en - new_released) - (old_en - old_released)) != 198:
        raise ValueError("New net English printings must be future-dated at cutoff")

    expected_hashes = historical["generated_file_sha256"]
    if len(expected_hashes) != 32:
        raise ValueError("Historical generated set/card index must contain 32 published shards")
    for name, checksum in expected_hashes.items():
        if not (name.startswith("historical_sets_") or name.startswith("historical_cards_")):
            raise ValueError("Unrecognized historical output filename")
        blob = (index_folder / name).read_bytes()
        if hashlib.sha256(blob).hexdigest() != checksum:
            raise ValueError(f"Historical published index was modified: {name}")

    census = category["all_code_census"]
    if census["total_all_scryfall_codes"] != 1062 or census["status_exclusive_partitions"] != {
            "digital_only_released": 62, "future_announced": 10,
            "released_nondigital_expansion_core": 142,
            "released_nondigital_other_categories": 848}:
        raise ValueError("Set status/category partitions are not a disjoint full 1,062 census")
    if (product["mapped_codes"], product["printing_atlas_codes"],
            product["api_set_codes_at_fetch"], product["counts"]["parent_links"]) != (1062, 1062, 1063, 560):
        raise ValueError("Product metadata/parent links do not reconcile with the 1,062 printing catalog codes")
    if product["warnings"]:
        raise ValueError("Unresolved product-set joins must not pass fast-track acceptance")
    if (family["cumulative_family_source_backed_codes"],
            family["cumulative_source_pending_codes"]) != (293, 555):
        raise ValueError("Individual product-source research queue checkpoint drift")
    if family["cumulative_family_source_backed_codes"] + family["cumulative_source_pending_codes"] != 848:
        raise ValueError("Other-category research queue must conserve 848 records")

    smoke = []
    if run_lookups:
        for code in SMOKE_CODES:
            result = set_query(code, folder=index_folder, cutoff=CUTOFF)
            prior = old[code].get("released_english_paper", 0)
            if result["printing_records"] != prior:
                raise ValueError(f"Historical live set lookup and audit disagree for {code}")
            smoke.append({"code": code, "released_english_paper": prior,
                          "distinct_identities": result["distinct_identities_or_unresolved"]})
        if set_query("trk", folder=index_folder, cutoff=CUTOFF, future=True)["printing_records"] <= 0:
            raise ValueError("Future Star Trek previews are not addressable with explicit opt-in")
        if set_query("ydmu", folder=index_folder, cutoff=CUTOFF, digital=True)["printing_records"] <= 0:
            raise ValueError("Digital-only entries are not addressable with explicit opt-in")
        if set_query("fbb", folder=index_folder, cutoff=CUTOFF, foreign=True)["printing_records"] <= 0:
            raise ValueError("Foreign printing variants are not addressable with explicit opt-in")
        lotus = card_query("Black Lotus", folder=index_folder, cutoff=CUTOFF)
        if lotus["matched_identities"] != 1 or "lea" not in {
                p["set"] for p in lotus["cards"][0]["printings"]}:
            raise ValueError("Bidirectional Black Lotus chronological printing lookup failed")
    return {
        "schema": 1, "as_of": CUTOFF.isoformat(),
        "policy": "Accelerated core acceptance: preserve individual Wizards family reviews as an optional separate research queue; never infer unsupported official classification",
        "source_provenance": {
            "historical_index": "105 October 28 printing shards; published 32 index files verified against committed generation hashes",
            "historical_source_bulk_bytes_reverified_now": False,
            "current_october29_bulk_reverified_now": False,
            "historical_original_bulk_sha256_recorded_only": historical["source_bulk_sha256_recorded_not_independently_rechecked"],
            "current_october29_bulk_sha256_from_prior_verified_audit": current["source_sha256"]
        },
        "all_codes": 1062, "published_index_files_hash_verified": 32,
        "historical_printing_records": old_all, "current_snapshot_printing_records": new_all,
        "historical_english_paper_printings": old_en,
        "current_snapshot_english_paper_printings": new_en,
        "released_english_paper_as_of_cutoff": old_released,
        "historical_future_english_paper": old_en - old_released,
        "current_future_english_paper": new_en - new_released,
        "net_printing_delta": new_all - old_all,
        "net_english_paper_delta": new_en - old_en,
        "released_english_paper_per_set_count_disagreements": count_disagreements,
        "changed_set_counts": report_deltas,
        "exclusive_status_partitions": census["status_exclusive_partitions"],
        "scryfall_product_metadata_codes_joined": product["mapped_codes"],
        "explicit_scryfall_parent_set_links": product["counts"]["parent_links"],
        "source_backed_other_category_families": 293,
        "non_blocking_other_category_family_research_pending": 555,
        "smoke_queries": smoke,
        "fasttrack_gate_status": {
            "released_english_paper_per_set_count_parity": "PASS",
            "32_git_published_index_hashes": "PASS",
            "category_partition_and_named_source_queue_preservation": "PASS",
            "complete_set_metadata_and_parent_link_join": "PASS",
            "nine_representative_set_lookups_and_black_lotus": "PASS" if run_lookups else "NOT_RUN",
            "exact_cross_snapshot_printing_ID_parity": "UNVERIFIED_requires_source_bytes_or_identified_delta",
            "newer_future_only_preview_rows_ingested": "NOT_REQUIRED_for_cutoff; current snapshot aggregates retained",
            "english_export_and_all_1062_set_query_acceptance": "PENDING",
            "premier_and_supplemental_set_category_count_release_labeling": "PENDING",
            "lore_to_publication_cross_reference": "PENDING"
        },
        "interpretation": [
            "All 1,062 set codes have equal released English-paper printing COUNTS at the dated cutoff; this is not a printing-ID equivalence certificate.",
            "The net 198 additional English-paper printing records belong wholly to future-dated COUNTS relative to the cutoff; all 1,062 released per-set counts are unchanged.",
            "The 293/848 first-party named-family source-review count measures optional provenance depth for other-category codes, NOT overall Phase 1B completion.",
            "Never treat 1,062 Scryfall codes or 293 sourced non-mainline product families as a count of regular historical expansion releases."
        ]
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    data = [load(p) for p in (CURRENT, CURRENT_AUDIT, HISTORICAL, CATEGORY, PRODUCT, FAMILY)]
    report = build(*data)
    payload = serialize(report)
    if args.write:
        OUTPUT.write_bytes(payload)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != payload:
        raise ValueError("Fast-track Phase 1B readiness report is not byte-exact reproducible")
    print(json.dumps({k: report[k] for k in (
        "all_codes", "released_english_paper_as_of_cutoff", "net_english_paper_delta",
        "published_index_files_hash_verified", "non_blocking_other_category_family_research_pending")}, sort_keys=True))


if __name__ == "__main__":
    main()
