#!/usr/bin/env python3
"""Phase 1B: reproducible metadata-led product-family RESEARCH triage.

Maps every released non-digital Scryfall set code outside expansion/core
into an explicit source-type research queue. A cohort is NOT an officially
verified product family, independent booster, premier release, or legality
finding. Never silently promote unreviewed Scryfall type into Wizards canon.

Usage:
  python3 scripts/audit_product_family_triage.py --write   # explicit regeneration
  python3 scripts/audit_product_family_triage.py           # read-only reproducibility check
"""
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data/set_atlas"
CATALOG = DATA / "product_catalog_2026-10-29.json"
PREVIOUS = DATA / "cross_category_audit_2026-10-29.json"
OUT = DATA / "product_family_triage_2026-10-29.json"
CUTOFF = "2026-10-29"

# Explicit, *research-only* mapping of Scryfall's machine-readable set_type.
# Group names imply a search strategy, not an authoritative Wizards taxonomy.
COHORT_TYPES = {
    "promotional_and_record_extras": (
        "promo", "token", "memorabilia", "minigame", "vanguard",
        "treasure_chest", "masterpiece",
    ),
    "preconstructed_and_boxed": (
        "commander", "duel_deck", "premium_deck", "box", "arsenal",
        "planechase", "archenemy",
    ),
    "reprint_and_curated_products": (
        "masters", "from_the_vault", "spellbook",
    ),
    "draft_and_starter_variants": (
        "draft_innovation", "starter", "funny",
    ),
    "special_inserts_and_eternal_subsets": ("eternal",),
}
# High priority means the family may contain standalone booster products and
# should receive Wizards primary-source review first, NOT presumed premier.
COHORT_PRIORITY = {
    "draft_and_starter_variants": 1,
    "reprint_and_curated_products": 2,
    "special_inserts_and_eternal_subsets": 2,
    "preconstructed_and_boxed": 3,
    "promotional_and_record_extras": 4,
}
EXCEPTION_CODES = {
    "plst": "Scryfall Masters type includes The List; not proof of a standalone booster product.",
    "bchr": "Chronicles Foreign Black Border is a localized product variant; not proof of an independent Masters booster.",
    "ren": "Renaissance is categorized Masters; its exact distribution requires separate source review.",
    "rin": "Rinascimento is categorized Masters; its exact distribution requires separate source review.",
    "slx": "Universes Within is categorized Masters; not automatically an independent draftable set.",
    "ltr": "Wizards-reviewed Modern-legal full booster in draft_innovation, not Standard-premier in 2023.",
    "mh3": "Wizards-reviewed Modern Horizons product in draft_innovation, not Standard-premier.",
    "por": "Portal is tagged starter, a product to review on its own terms, not automatically promo.",
}


def encode(document):
    return (json.dumps(document, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def build(catalog, prior):
    if catalog.get("snapshot_date") != CUTOFF or prior.get("snapshot_date") != CUTOFF:
        raise ValueError("Snapshot dates mismatch")
    base = prior["all_code_census"]["status_exclusive_partitions"]
    if base != {
        "digital_only_released": 62, "future_announced": 10,
        "released_nondigital_expansion_core": 142,
        "released_nondigital_other_categories": 848,
    }:
        raise ValueError("Baseline status buckets do not match frozen snapshot")
    reviewed = {
        r["code"]: r for r in prior["reviewed_non_expansion_core_products"]
    }
    if len(reviewed) != prior["reviewed_count"] or len(reviewed) != 12:
        raise ValueError("Official-source review ledger has changed")
    lookup = {}
    for cohort, types in COHORT_TYPES.items():
        for category in types:
            if category in lookup:
                raise ValueError(f"Ambiguous cohort mapping for {category}")
            lookup[category] = cohort
    if len(catalog["sets"]) != 1062:
        raise ValueError("Frozen set-code count mismatch")

    records, counts, types, status_counts = [], Counter(), Counter(), Counter()
    by_type = defaultdict(Counter)
    by_cohort = defaultdict(Counter)
    reviewed_seen = set()
    for code, s in sorted(catalog["sets"].items()):
        if s.get("scryfall_set_metadata_missing"):
            raise ValueError(f"Set API record missing for {code}")
        if s["release_status_as_of_cutoff"] == "announced_future":
            status_counts["future_announced"] += 1
            continue
        if s["digital_only"]:
            status_counts["digital_only_released"] += 1
            continue
        kind = s["scryfall_set_type"]
        if kind in ("core", "expansion"):
            status_counts["released_nondigital_expansion_core"] += 1
            continue
        if kind not in lookup:
            raise ValueError(f"Unknown released non-digital Scryfall set_type {kind!r}, code={code}")
        cohort = lookup[kind]
        reviewed_record = reviewed.get(code)
        if reviewed_record:
            reviewed_seen.add(code)
            if reviewed_record["scryfall_set_type"] != kind:
                raise ValueError(f"Wizards-reviewed Scryfall category mismatch: {code}")
        official_review = bool(reviewed_record)
        entry = {
            "code": code,
            "name": s["name"],
            "scryfall_set_type": kind,
            "metadata_cohort_not_official_classification": cohort,
            "research_priority_1_highest": COHORT_PRIORITY[cohort],
            "scryfall_release_or_first_card_date": s["released_at"],
            "parent_set_code_explicit_only": s.get("parent_set_code"),
            "parent_association_status": (
                "scryfall_explicit_parent" if s.get("parent_set_code")
                else "not_given_does_not_prove_standalone"
            ),
            "oct29_default_cards_printings": s["printing_records_in_oct29_default_cards"],
            "oct29_released_distinct_oracle_ids": s["released_distinct_oracle_ids_in_oct29_default_cards"],
            "wizards_individual_source_review": official_review,
            "review_status": (
                "wizards_primary_source_example_reviewed" if official_review
                else "metadata_only_individual_wizards_source_review_pending"
            ),
            "premier_release_status": "not_inferred_from_set_type",
            "wizards_primary_source": reviewed_record["source_url"] if official_review else None,
            "wizards_review_product_group": reviewed_record["product_group"] if official_review else None,
            "known_historical_or_classification_caution": EXCEPTION_CODES.get(code),
            "scryfall_source": s.get("scryfall_uri"),
        }
        records.append(entry)
        counts[cohort] += 1
        types[kind] += 1
        status_counts["released_nondigital_other_categories"] += 1
        by_type[kind]["codes"] += 1
        by_cohort[cohort]["codes"] += 1
        if official_review:
            by_type[kind]["wizards_reviewed"] += 1
            by_cohort[cohort]["wizards_reviewed"] += 1
        else:
            by_type[kind]["needs_individual_review"] += 1
            by_cohort[cohort]["needs_individual_review"] += 1
        if s.get("parent_set_code"):
            by_type[kind]["explicit_parent_links"] += 1
            by_cohort[cohort]["explicit_parent_links"] += 1

    if dict(status_counts) != base:
        raise ValueError(f"Unreconciled set census: {dict(status_counts)} != {base}")
    if len(records) != 848 or sum(counts.values()) != 848:
        raise ValueError("Outside-category cohort total not exhaustive")
    if reviewed_seen != set(reviewed):
        raise ValueError(f"Previously reviewed examples lost: {sorted(set(reviewed)-reviewed_seen)}")
    pending = [r for r in records if not r["wizards_individual_source_review"]]
    if len(pending) != 836:
        raise ValueError(f"Incorrect metadata-only pending count: {len(pending)}")

    # No individual set receives two cohorts; parentless is NOT equal to standalone.
    queue = [
        {"code": r["code"], "name": r["name"], "scryfall_set_type": r["scryfall_set_type"],
         "metadata_cohort": r["metadata_cohort_not_official_classification"],
         "priority": r["research_priority_1_highest"],
         "parent": r["parent_set_code_explicit_only"], "release": r["scryfall_release_or_first_card_date"]}
        for r in pending
    ]
    queue.sort(key=lambda x: (x["priority"], x["scryfall_set_type"], x["release"] or "", x["code"]))
    return {
        "schema": 1,
        "snapshot_date": CUTOFF,
        "provenance": {
            "scryfall_snapshot": CATALOG.name,
            "wizards_review_ledger": PREVIOUS.name,
            "cohorts": "local research triage derived solely from frozen Scryfall set_type",
        },
        "source_total_set_codes": 1062,
        "exclusive_whole_corpus_counts": dict(sorted(status_counts.items())),
        "released_nondigital_other_type_codes": 848,
        "wizards_reviewed_examples": len(reviewed_seen),
        "metadata_only_pending_wizards_individual_review": len(pending),
        "metadata_research_cohorts": dict(sorted(counts.items())),
        "scryfall_categories": {t: dict(sorted(c.items())) for t, c in sorted(by_type.items())},
        "cohort_review_progress": {t: dict(sorted(c.items())) for t, c in sorted(by_cohort.items())},
        "all_848_released_nondigital_other_type_records": records,
        "pending_836_individual_source_review_queue": queue,
        "limitations": [
            "Cohorts and priorities are a research queue derived from Scryfall set_type, NOT Wizards product-family certification.",
            "Only 12 exact codes have individual Wizards primary-source review; the other 836 remain source-pending.",
            "A nonempty parent_set_code is a direct Scryfall association; a missing parent does not establish a standalone release.",
            "The printed counts are from the Oct 29 Default Cards catalog and are not a guarantee of distinct physical printed cards or sealed products.",
            "A token, promo, memorabilia, or funny Scryfall type is not itself proof of premier status, game legality or standalone booster availability.",
            "Do not add these 848 to the 136 previously reviewed expansion/core mainline count to obtain an all-time premier-set figure.",
            "All dates and review flags describe the frozen 2026-10-29 snapshot, not current live data.",
        ],
    }


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--write", action="store_true")
    write = args.parse_args().write
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    prior = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    output = build(catalog, prior)
    raw = encode(output)
    if write:
        OUT.write_bytes(raw)
    elif not OUT.exists() or OUT.read_bytes() != raw:
        raise ValueError("Saved product family research triage differs from deterministic snapshot output")
    print(json.dumps({
        "all_set_codes": output["source_total_set_codes"],
        "cohorts": output["metadata_research_cohorts"],
        "wizards_reviewed_examples": output["wizards_reviewed_examples"],
        "wizards_source_pending": output["metadata_only_pending_wizards_individual_review"],
        "queue_top_10": output["pending_836_individual_source_review_queue"][:10],
    }, indent=2))


if __name__ == "__main__":
    main()
