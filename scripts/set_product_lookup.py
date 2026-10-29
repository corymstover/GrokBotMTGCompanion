#!/usr/bin/env python3
"""Read the dated Scryfall product catalog without contacting the live API.

Examples:
  python3 scripts/set_product_lookup.py --code lea
  python3 scripts/set_product_lookup.py --type expansion --year 1994
  python3 scripts/set_product_lookup.py --parent dmu
  python3 scripts/set_product_lookup.py --name "Commander" --include-future
"""
import argparse
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "data/set_atlas/product_catalog_2026-10-29.json"


def lookup(data, *, code=None, name=None, year=None, set_type=None, parent=None,
           include_future=False, earliest=None, latest=None):
    items = []
    for set_code, entry in data["sets"].items():
        if entry.get("scryfall_set_metadata_missing"):
            continue
        if code and set_code.casefold() != code.casefold():
            continue
        if name and name.casefold() not in entry["name"].casefold():
            continue
        if set_type and entry["scryfall_set_type"] != set_type:
            continue
        if parent and entry.get("parent_set_code") != parent:
            continue
        released = entry.get("released_at")
        if year is not None and (not released or int(released[:4]) != year):
            continue
        if earliest and (not released or released < earliest):
            continue
        if latest and (not released or released > latest):
            continue
        if not include_future and entry["release_status_as_of_cutoff"] == "announced_future":
            continue
        items.append({
            "code": set_code, "name": entry["name"], "set_type": entry["scryfall_set_type"],
            "release_date_or_first_printing": released, "digital_only": entry["digital_only"],
            "parent_set_code": entry.get("parent_set_code"),
            "oct29_printing_rows": entry["printing_records_in_oct29_default_cards"],
            "oct29_released_distinct_oracle_ids": entry["released_distinct_oracle_ids_in_oct29_default_cards"],
            "scryfall_uri": entry.get("scryfall_uri")
        })
    items.sort(key=lambda x: (x["release_date_or_first_printing"] or "", x["code"]))
    return items


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--code")
    p.add_argument("--name")
    p.add_argument("--year", type=int)
    p.add_argument("--type", dest="set_type")
    p.add_argument("--parent")
    p.add_argument("--from", dest="earliest")
    p.add_argument("--through", dest="latest")
    p.add_argument("--include-future", action="store_true")
    p.add_argument("--all", action="store_true")
    args = p.parse_args()
    for field in ("earliest", "latest"):
        v = getattr(args, field)
        if v is not None:
            date.fromisoformat(v)
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    results = lookup(catalog, code=args.code, name=args.name, year=args.year,
                     set_type=args.set_type, parent=args.parent,
                     earliest=args.earliest, latest=args.latest,
                     include_future=args.include_future)
    print(json.dumps({"snapshot": catalog["snapshot_date"], "matches": len(results),
                      "results": results if args.all else results[:30]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
