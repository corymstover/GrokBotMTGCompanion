#!/usr/bin/env python3
"""Phase 1B exact set→card and card→set printing lookup over verified Scryfall.

Queries default to English paper printings released by --as-of; use --all
to print the entire result rather than the first 30 distinct cards/printings.
Future products and digital cards are excluded from this default display,
not deleted from the underlying snapshot or dated catalog.

Example:
  python3 scripts/set_atlas_lookup.py --snapshot PATH --snapshot-manifest MANIFEST \
    --as-of 2026-10-29 set lea --all
  python3 scripts/set_atlas_lookup.py --snapshot PATH --snapshot-manifest MANIFEST \
    --as-of 2026-10-29 card "Black Lotus"
"""

import argparse
import json
from collections import defaultdict
from datetime import date
from pathlib import Path

from audit_set_printing_atlas import source_rows, verify_source


def oracle_id(card):
    return card.get("oracle_id") or (card.get("card_faces") or [{}])[0].get("oracle_id")


def selected(card, cutoff, include_future=False, include_digital=False, include_foreign=False):
    if not include_foreign and card.get("lang") != "en":
        return False
    if not include_digital and "paper" not in card.get("games", []):
        return False
    # Never treat an unknown date as an earliest printing, even when the user
    # intentionally includes announced/future-dated records.
    try:
        day = date.fromisoformat(card.get("released_at") or "")
    except ValueError:
        return False
    if not include_future and day > cutoff:
        return False
    return True


def query(rows, cutoff, kind, target, *, include_future=False, include_digital=False,
          include_foreign=False, limit=30):
    target = target.casefold()
    first = {}
    first_sets = defaultdict(set)
    candidates = []
    for card in rows:
        if not selected(card, cutoff, include_future, include_digital, include_foreign):
            continue
        oid = oracle_id(card)
        if not oid:
            raise ValueError("selected printing lacks oracle_id")
        day = card.get("released_at") or ""
        if oid not in first or day < first[oid]:
            first[oid] = day
            first_sets[oid] = {card["set"]}
        elif day == first[oid]:
            first_sets[oid].add(card["set"])
        names = {card.get("name", "").casefold()}
        names.update(face.get("name", "").casefold() for face in card.get("card_faces", []))
        if (kind == "set" and card["set"].casefold() == target) or (kind == "card" and (target in names or target == oid.casefold())):
            candidates.append(card)

    if kind == "set":
        grouped = defaultdict(list)
        for card in candidates:
            grouped[oracle_id(card)].append(card)
        result = []
        for oid, printing in grouped.items():
            dates = [p.get("released_at", "") for p in printing]
            debuted = any(day == first[oid] for day in dates)
            result.append({"name": printing[0]["name"], "oracle_id": oid,
                           "printings_in_set": len(printing),
                           "first_printing_in_set": min(dates),
                           "classification": "same-day tied debut" if debuted and len(first_sets[oid]) > 1 else
                                             "debut" if debuted else "reprint",
                           "debut_set_codes": sorted(first_sets[oid]) if debuted else []})
        result.sort(key=lambda r: (r["name"].casefold(), r["oracle_id"]))
        return {"set_code": target, "distinct_oracle_ids": len(result),
                "printings": len(candidates), "items": result[:limit] if limit else result}
    result = [{"name": card["name"], "oracle_id": oracle_id(card),
               "printing_id": card["id"], "set": card["set"], "set_name": card["set_name"],
               "collector_number": card["collector_number"], "released_at": card.get("released_at"),
               "first_printed_in_sets": sorted(first_sets[oracle_id(card)])}
              for card in candidates]
    result.sort(key=lambda r: (r["released_at"] or "", r["set"], r["collector_number"]))
    return {"card": target, "printing_records": len(result),
            "set_codes": sorted({r["set"] for r in result}),
            "items": result[:limit] if limit else result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", required=True, type=Path)
    parser.add_argument("--snapshot-manifest", required=True, type=Path)
    parser.add_argument("--as-of", required=True, type=date.fromisoformat)
    parser.add_argument("--include-future", action="store_true")
    parser.add_argument("--include-digital", action="store_true")
    parser.add_argument("--include-foreign", action="store_true")
    parser.add_argument("--all", action="store_true", help="do not limit the printed items")
    subs = parser.add_subparsers(dest="kind", required=True)
    subs.add_parser("set").add_argument("target")
    subs.add_parser("card").add_argument("target")
    args = parser.parse_args()
    archive = verify_source(args.snapshot, args.snapshot_manifest)
    result = query(source_rows(args.snapshot), args.as_of, args.kind, args.target,
                   include_future=args.include_future, include_digital=args.include_digital,
                   include_foreign=args.include_foreign, limit=0 if args.all else 30)
    print(json.dumps({"snapshot_sha256": archive["sha256"], "as_of": args.as_of.isoformat(),
                      "filters": {"english_only": not args.include_foreign,
                                  "paper_only": not args.include_digital,
                                  "released_only": not args.include_future}, **result}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
