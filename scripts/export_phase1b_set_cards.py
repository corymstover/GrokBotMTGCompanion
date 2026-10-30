#!/usr/bin/env python3
"""Export a full, dated set card list from committed Phase 1B historical shards.

Examples:
  python3 scripts/export_phase1b_set_cards.py lea --mode unique --format csv
  python3 scripts/export_phase1b_set_cards.py c21 --mode printings --format json
  python3 scripts/export_phase1b_set_cards.py trk --include-future --output star_trek.csv

Default: released English paper only as of 2026-10-29. Alternate-language,
digital, or future previews require explicit flags. Nothing is downloaded.
"""
import argparse
import csv
import hashlib
import io
import json
import sys
from datetime import date
from pathlib import Path

from historical_set_lookup import DATA, load, selected, set_query

PRINT_FIELDS = ("set_code", "name", "oracle_id", "printing_id", "collector_number",
                "released_at", "language", "paper", "debut_classification")
UNIQUE_FIELDS = ("set_code", "name", "oracle_id", "printings_in_set",
                 "first_printing_in_set", "debut_classification")


def export_set(code, *, mode="printings", cutoff=date(2026, 10, 29),
               future=False, digital=False, foreign=False, folder=DATA):
    if mode not in ("printings", "unique"):
        raise ValueError("Export mode must be printings or unique")
    code = code.lower()
    flags = {"future": future, "digital": digital, "foreign": foreign}
    snapshot = set_query(code, folder=folder, cutoff=cutoff, **flags)
    source = load(hashlib.sha256(code.encode()).hexdigest()[0], "sets", folder)[code]
    subset = [r for r in source if selected(r, cutoff, **flags)]
    classes = {(r["oracle_id"] or "unresolved:" + r["name"]): r["classification"]
               for r in snapshot["cards"]}
    if mode == "printings":
        rows = [{
            "set_code": code, "name": r[2], "oracle_id": r[1], "printing_id": r[0],
            "collector_number": r[3], "released_at": r[4], "language": r[5],
            "paper": bool(r[6]), "debut_classification": classes.get(r[1], "unresolved identity")
        } for r in subset]
        rows.sort(key=lambda x: (x["name"].casefold(), x["released_at"],
                                 x["collector_number"], x["printing_id"]))
    else:
        rows = []
        first_by_oracle = {}
        for printing in subset:
            oid = printing[1]
            first_by_oracle[oid] = min(first_by_oracle.get(oid, printing[4]), printing[4])
        for r in snapshot["cards"]:
            rows.append({
                "set_code": code, "name": r["name"], "oracle_id": r["oracle_id"],
                "printings_in_set": r["printings"],
                "first_printing_in_set": first_by_oracle.get(r["oracle_id"]),
                "debut_classification": r["classification"]
            })
    if mode == "printings" and len(rows) != snapshot["printing_records"]:
        raise ValueError("CSV/JSON printing export lost source records")
    if mode == "unique" and len(rows) != snapshot["distinct_identities_or_unresolved"]:
        raise ValueError("Unique identity export lost source records")
    return {
        "source": "2026-10-28 committed historical index",
        "as_of": cutoff.isoformat(), "filters": flags, "set_code": code,
        "mode": mode, "printing_records": snapshot["printing_records"],
        "distinct_identities_or_unresolved": snapshot["distinct_identities_or_unresolved"],
        "rows": rows
    }


def format_export(result, output_format):
    if output_format == "json":
        return json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if output_format != "csv":
        raise ValueError("Output format must be csv or json")
    fieldnames = PRINT_FIELDS if result["mode"] == "printings" else UNIQUE_FIELDS
    buf = io.StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(result["rows"])
    return buf.getvalue()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("code", help="Exact Scryfall set code")
    p.add_argument("--mode", choices=("printings", "unique"), default="printings")
    p.add_argument("--format", choices=("csv", "json"), default="csv")
    p.add_argument("--as-of", type=date.fromisoformat, default=date(2026, 10, 29))
    p.add_argument("--include-future", action="store_true")
    p.add_argument("--include-digital", action="store_true")
    p.add_argument("--include-foreign", action="store_true")
    p.add_argument("--output", type=Path, help="Write the export to this explicit file; otherwise stdout")
    args = p.parse_args()
    result = export_set(args.code, mode=args.mode, cutoff=args.as_of,
                        future=args.include_future, digital=args.include_digital,
                        foreign=args.include_foreign)
    content = format_export(result, args.format)
    if args.output:
        args.output.write_text(content, encoding="utf-8", newline="")
    else:
        sys.stdout.write(content)


if __name__ == "__main__":
    main()
