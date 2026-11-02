#!/usr/bin/env python3
"""Independently certify qualified, separately labelled set totals (K050).

This is a *dated set-code census*, not a Wizards all-time premier-set census.
The two counts must never be conflated.  All 1,062 Scryfall codes are assigned
exactly one scope class; the 136 primary-supported regular/mainline releases
are a subset of 142 nondigital expansion/core candidates at the cutoff.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SCOPE = ROOT / "data/set_atlas/phase1b_release_scope_story_bridge_2026-10-29.json"
CATALOG = ROOT / "data/set_atlas/product_catalog_2026-10-29.json"
GATES = ROOT / "data/set_atlas/phase1b_snapshot_gates_2026-10-30.json"
OUT = ROOT / "data/release/set_totals_acceptance_2026-11-01.json"
EXPECTED_SCOPE = {
    "historical_regular_mainline": 136,
    "documented_auxiliary_or_discarded": 4,
    "localized_variant_provisional": 2,
    "released_paper_other_category": 848,
    "released_digital_only": 62,
    "future_announced": 10,
}


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def wotc_url(url: str | None) -> bool:
    if not url:
        return False
    p = urlparse(url)
    return p.scheme == "https" and p.hostname in {"magic.wizards.com", "www.magic.wizards.com"}


def build(scope_path: Path = SCOPE, catalog_path: Path = CATALOG,
          gates_path: Path = GATES) -> dict:
    scope, catalog, gates = read(scope_path), read(catalog_path), read(gates_path)
    records, products = scope["set_scope_records"], catalog["sets"]
    if scope.get("all_time_premier_set_count_certified") is not False:
        raise ValueError("an unverified all-time Wizards premier count was promoted")
    if scope.get("as_of") != catalog.get("snapshot_date") or scope["as_of"] != "2026-10-29":
        raise ValueError("cross-snapshot set counts are not comparable")
    if set(records) != set(products) or len(records) != 1062 or scope.get("all_set_codes") != 1062:
        raise ValueError("set-code census is not exhaustive and bijective")
    cats = Counter(row["scope_label"] for row in records.values())
    if dict(cats) != EXPECTED_SCOPE or scope.get("scope_counts_exclusive") != EXPECTED_SCOPE:
        raise ValueError("the exclusive six-way scope partition is not reproducible")
    types = Counter(row["scryfall_set_type"] for row in products.values())
    gate_rows = [g for g in gates["gates"] if g["gate"].startswith("reproducible totals for all set codes")]
    if len(gate_rows) != 1 or types != gate_rows[0]["set_type_totals"]:
        raise ValueError("independently published per-type Scryfall totals disagree")
    if sum(types.values()) != 1062 or (types["expansion"], types["core"]) != (120, 25):
        raise ValueError("expansion/core category totals do not sum to frozen catalog")

    candidates = {code for code, p in products.items()
                  if p["scryfall_set_type"] in ("expansion", "core")
                  and not p["digital_only"] and p["release_status_as_of_cutoff"] == "released_by_cutoff"}
    qualified = {code for code, row in records.items()
                 if row["scope_label"] in ("historical_regular_mainline",
                                            "documented_auxiliary_or_discarded",
                                            "localized_variant_provisional")}
    if candidates != qualified or len(candidates) != 142:
        raise ValueError("released nondigital expansion/core candidate roster drifted")

    official_codes = []
    for code, row in sorted(records.items()):
        p = products[code]
        if (row["scryfall_set_type"] != p["scryfall_set_type"]
                or row["parent_set_code"] != p["parent_set_code"]
                or row["released_at"] != p["released_at"]):
            raise ValueError("set scope disagrees with frozen product metadata: " + code)
        label = row["scope_label"]
        if label in {"historical_regular_mainline", "documented_auxiliary_or_discarded"}:
            if (not wotc_url(row.get("wizards_release_source")) or row.get("scope_evidence") not in
                    {"Wizards_release_enumeration", "Wizards_bounded_2023_2026_release_review"}):
                raise ValueError("primary-supported release has no Wizards evidence: " + code)
            official_codes.append(code)
        elif label == "localized_variant_provisional":
            if (code not in {"4bb", "fbb"} or row.get("scope_evidence") != "third_party_corroborated_only"
                    or row.get("wizards_release_source") is not None):
                raise ValueError("localized border variant was promoted without Wizards source")
        elif row.get("wizards_release_source") is not None:
            raise ValueError("non-reviewed category was silently given official provenance: " + code)

    return {
        "schema": "set-totals-acceptance/v1", "snapshot_date": "2026-10-29",
        "input_sha256": {p.name: sha(p) for p in (scope_path, catalog_path, gates_path)},
        "source": "Scryfall /sets frozen metadata plus 140 individually Wizards-cited scoped releases",
        "counts": {
            "all_scryfall_set_codes": 1062,
            "scryfall_set_types": dict(sorted(types.items())),
            "scryfall_expansion_or_core_category_all_dates": 145,
            "released_nondigital_expansion_or_core_candidates_at_cutoff": 142,
            "wizards_sourced_historical_regular_mainline_subset": 136,
            "wizards_sourced_documented_auxiliary_not_regular_mainline": 4,
            "provisional_foreign_border_variants_without_primary_confirmation": 2,
            "released_paper_other_category_codes": 848,
            "released_digital_only_codes": 62,
            "future_announced_codes": 10,
        },
        "first_party_source_cited_codes": official_codes,
        "all_time_wizards_premier_census_certified": False,
        "qualified_acceptance": "K050 publishes exact dated all-code, product-category, expansion/core candidate and primary-supported regular/mainline totals without conflating them.",
        "limitations": [
            "1062 counts Scryfall set-code catalog objects, not 1062 physical products or premier expansions.",
            "145 expansion/core are Scryfall set-type codes across dates and media; 142 are released nondigital candidates at the 2026-10-29 cutoff.",
            "136 is the Wizards-source-reviewed historical regular/mainline subset of those 142 candidates, not an all-time Wizards certified premier census.",
            "Four auxiliary/discarded and two provisional foreign-border variants are explicitly excluded from the 136, not silently treated as new premier releases.",
            "848 other-category paper codes include commander products, bonus sheets, tokens, promo and other metadata records; not all are separate sold products.",
            "The snapshot is frozen; later live additions belong to recurring upkeep and cannot change these historical totals without a new dated source.",
        ],
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    rendered = json.dumps(build(), indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != rendered:
            raise ValueError("qualified set totals acceptance report is stale")
        print("PASS qualified set totals: 1062 code categories; 142 released paper candidates; 136 first-party reviewed mainline")
    else:
        OUT.write_text(rendered, encoding="utf-8")
        print("Wrote " + str(OUT.relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
