#!/usr/bin/env python3
"""Read-only, dated classification of Scryfall Oracle IDs absent from the card index.

Use an archived, hash-verified Oracle Cards JSONL(.gz) snapshot; do not substitute
its contents for the locked historical Grixis snapshot or ingest future cards.

Example:
  python3 scripts/audit_oracle_index.py \
    --oracle .cache/multiverse/oracle-cards-20261029090202.jsonl.gz \
    --manifest .cache/multiverse/manifest.json --as-of 2026-10-29
"""

import argparse
import csv
import gzip
import hashlib
import json
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import ingest_scryfall as ing

ROOT = Path(__file__).resolve().parent.parent


def index_ids(path):
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    ids = [r["oracle_id"] for r in rows]
    if not all(ids) or len(set(ids)) != len(ids):
        raise ValueError("card index has empty or duplicate Oracle IDs")
    return set(ids)


def read_oracle(path):
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            try:
                card = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"bad Oracle JSON at line {number}") from exc
            yield card


def classify(cards, indexed, cutoff):
    """Exact categories with an explicit as-of date, never current wall-clock time."""
    counts = Counter()
    layouts = Counter()
    future_sets = Counter()
    future_dates = Counter()
    examples = defaultdict(list)
    seen = set()
    for card in cards:
        oid = card.get("oracle_id")
        if not isinstance(oid, str) or not oid or oid in seen:
            raise ValueError("Oracle snapshot contains a blank or repeated Oracle ID")
        seen.add(oid)
        layout = card.get("layout")
        eligible = layout not in ing.EXCLUDED_LAYOUTS and ing.in_universe(card)
        if oid in indexed:
            counts["indexed"] += 1
            if not eligible:
                counts["indexed_outside_policy"] += 1
            continue
        if layout in ing.EXCLUDED_LAYOUTS:
            category = "excluded_layout"
            layouts[layout] += 1
        elif not ing.in_universe(card):
            category = "nonpaper_noneternal"
        else:
            try:
                release = date.fromisoformat(card.get("released_at") or "")
            except ValueError:
                release = None
            if release is None:
                category = "eligible_undated_review"
            elif release > cutoff:
                category = "eligible_future_dated"
                future_sets[card.get("set") or "unknown"] += 1
                future_dates[release.isoformat()] += 1
            else:
                category = "eligible_released_missing"
        counts[category] += 1
        if len(examples[category]) < 8:
            examples[category].append({"name": card.get("name"), "oracle_id": oid,
                                       "set": card.get("set"), "released_at": card.get("released_at")})
    missing_from_snapshot = indexed - seen
    unindexed = len(seen - indexed)
    categories = ("excluded_layout", "nonpaper_noneternal", "eligible_future_dated",
                  "eligible_released_missing", "eligible_undated_review")
    if sum(counts[k] for k in categories) != unindexed:
        raise AssertionError("exclusion categories do not partition the unindexed records")
    return {
        "as_of": cutoff.isoformat(),
        "oracle_records": len(seen), "indexed_records": len(indexed),
        "indexed_present": counts["indexed"],
        "indexed_not_in_snapshot": len(missing_from_snapshot),
        "indexed_outside_policy": counts["indexed_outside_policy"],
        "unindexed_records": unindexed,
        "classifications": {key: counts[key] for key in categories},
        "excluded_layouts": dict(sorted(layouts.items())),
        "future_by_set": dict(sorted(future_sets.items())),
        "future_by_date": dict(sorted(future_dates.items())),
        "samples": {key: examples[key] for key in categories if examples[key]},
        "scope": "Scryfall Oracle Cards snapshot, paper/eternal index policy, dated release eligibility; not a printing census or legality ruling",
    }


def verify_archive(path, manifest):
    expected = manifest.get("files", {}).get("oracle-cards", {})
    if not expected.get("sha256") or not expected.get("records"):
        raise ValueError("manifest lacks Oracle hash or record count")
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    if digest.hexdigest() != expected["sha256"]:
        raise ValueError("Oracle snapshot SHA-256 does not match release manifest")
    if path.stat().st_size != expected.get("compressed_bytes"):
        raise ValueError("Oracle snapshot byte size does not match release manifest")
    return digest.hexdigest(), expected["records"]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--oracle", required=True, type=Path, help="archived Oracle JSONL or JSONL.gz")
    parser.add_argument("--index", default=ROOT / "data/card_index.csv", type=Path)
    parser.add_argument("--manifest", type=Path, help="snapshot manifest with compressed SHA-256 and record count")
    parser.add_argument("--as-of", required=True, type=date.fromisoformat, help="YYYY-MM-DD eligibility cutoff")
    args = parser.parse_args(argv)
    digest, records = (None, None)
    if args.manifest:
        digest, records = verify_archive(args.oracle, json.loads(args.manifest.read_text(encoding="utf-8")))
    report = classify(read_oracle(args.oracle), index_ids(args.index), args.as_of)
    if records is not None and report["oracle_records"] != records:
        parser.error("Oracle record count differs from verified release manifest")
    report["oracle_sha256"] = digest
    report["manifest_verified"] = bool(digest)
    print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
