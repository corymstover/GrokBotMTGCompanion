#!/usr/bin/env python3
"""Phase 1B: compare an existing printing manifest with a verified newer bulk.

This is a read-only analyzer unless --write is supplied. It never regenerates
historic printing shards, card pages, or protected Grixis data. Use a dated
Scryfall Default Cards archive plus the independent release manifest.

Example:
  python3 scripts/audit_set_printing_atlas.py \
    --baseline data/printing_lore/manifest.json \
    --snapshot .cache/multiverse/default-cards-YYYYMMDDHHMMSS.jsonl.gz \
    --snapshot-manifest .cache/multiverse/manifest.json \
    --as-of 2026-10-29 --write
"""

import argparse
import gzip
import hashlib
import json
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ATLAS = ROOT / "data" / "set_atlas"


def checksum(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_source(snapshot, release_manifest):
    source = json.loads(release_manifest.read_text(encoding="utf-8"))
    record = source.get("files", {}).get("default-cards", {})
    if record.get("filename") != snapshot.name:
        raise ValueError("snapshot filename differs from verified release manifest")
    if snapshot.stat().st_size != record.get("compressed_bytes"):
        raise ValueError("snapshot byte count differs from verified release manifest")
    digest = checksum(snapshot)
    if digest != record.get("sha256"):
        raise ValueError("snapshot SHA-256 differs from verified release manifest")
    if not isinstance(record.get("records"), int) or record["records"] <= 0:
        raise ValueError("release manifest lacks a valid default-cards record count")
    return {"filename": snapshot.name, "sha256": digest, "compressed_bytes": snapshot.stat().st_size,
            "manifest_records": record["records"]}


def validate_baseline(baseline):
    sets, shards = baseline["sets"], baseline["shards"]
    declared = baseline["total_printings"]
    if len(sets) == 0 or len(shards) != baseline["total_shards"]:
        raise ValueError("baseline manifest has missing sets or shards")
    if sum(v["printings"] for v in sets.values()) != declared:
        raise ValueError("baseline per-set totals do not match total printings")
    if sum(v["rows"] for v in shards.values()) != declared:
        raise ValueError("baseline per-shard totals do not match total printings")
    for code, entry in sets.items():
        if not code or not entry.get("files") or any(n not in shards for n in entry["files"]):
            raise ValueError(f"baseline set {code!r} references absent shard files")
        if not 0 <= entry["english_paper"] <= entry["printings"]:
            raise ValueError(f"baseline set {code} has invalid English paper totals")
    return {"source": baseline["source"], "source_sha256": baseline["source_sha256"],
            "set_codes": len(sets), "printing_records": declared,
            "english_paper_records": sum(v["english_paper"] for v in sets.values()),
            "shards": len(shards), "shard_rows": sum(v["rows"] for v in shards.values()),
            "shard_content_verified": False,
            "shard_content_caveat": "Manifest arithmetic and paths verified; archived shard bytes were not available for hashing in this audit."}


def source_rows(snapshot):
    opener = gzip.open if snapshot.suffix == ".gz" else open
    with opener(snapshot, "rt", encoding="utf-8") as stream:
        for number, line in enumerate(stream, 1):
            try:
                card = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"bad JSON at source line {number}") from exc
            if not isinstance(card, dict):
                raise ValueError(f"source line {number} is not a printing object")
            yield card


def analyze(rows, cutoff):
    counts = defaultdict(Counter)
    names, types = {}, {}
    first_printing, latest_printing = {}, {}
    oid_dates = defaultdict(dict)  # set -> oracle ID -> earliest released English paper date
    earliest = {}  # oracle ID -> earliest released English paper date anywhere in the snapshot
    seen_ids = set()
    all_oracle_ids = set()
    undated = 0
    total = 0
    for card in rows:
        total += 1
        pid, code = card.get("id"), card.get("set")
        if not pid or pid in seen_ids:
            raise ValueError("missing or repeated Scryfall printing ID")
        seen_ids.add(pid)
        if not code or not card.get("collector_number"):
            raise ValueError("printing lacks set code or collector number")
        name, kind = card.get("set_name"), card.get("set_type")
        if not name or not kind:
            raise ValueError(f"printing in {code} lacks set name/type")
        if code in names and (names[code] != name or types[code] != kind):
            raise ValueError(f"conflicting name or Scryfall set_type for {code}")
        names[code], types[code] = name, kind
        oid = card.get("oracle_id") or (card.get("card_faces") or [{}])[0].get("oracle_id")
        if not oid:
            raise ValueError(f"printing {pid} lacks an Oracle ID")
        all_oracle_ids.add(oid)
        raw_date = card.get("released_at")
        try:
            release = date.fromisoformat(raw_date or "")
        except ValueError:
            release = None
        if release is None:
            undated += 1
        else:
            first_printing[code] = min(release, first_printing.get(code, release))
            latest_printing[code] = max(release, latest_printing.get(code, release))
        english = card.get("lang") == "en"
        paper = "paper" in card.get("games", [])
        group = counts[code]
        group["printings"] += 1
        group["english_paper"] += int(english and paper)
        if release and release > cutoff:
            group["future_dated"] += 1
        if english and paper and release and release <= cutoff:
            group["released_english_paper"] += 1
            oid_dates[code][oid] = min(release, oid_dates[code].get(oid, release))
            earliest[oid] = min(release, earliest.get(oid, release))

    debut_sets = defaultdict(set)
    for code, dates in oid_dates.items():
        for oid, day in dates.items():
            if day == earliest[oid]:
                debut_sets[oid].add(code)
    catalog = {}
    for code in sorted(counts):
        group = counts[code]
        ods = oid_dates[code]
        single = sum(len(debut_sets[oid]) == 1 and code in debut_sets[oid] for oid in ods)
        tied = sum(len(debut_sets[oid]) > 1 and code in debut_sets[oid] for oid in ods)
        unique = len(ods)
        catalog[code] = {"name": names[code], "set_type": types[code],
                         "earliest_printing_date": first_printing.get(code).isoformat() if code in first_printing else None,
                         "latest_printing_date": latest_printing.get(code).isoformat() if code in latest_printing else None,
                         "printings": group["printings"], "english_paper": group["english_paper"],
                         "released_english_paper": group["released_english_paper"],
                         "released_distinct_oracle_ids": unique,
                         "single_set_debuts": single, "tied_same_day_debuts": tied,
                         "reprinted_oracle_ids": unique - single - tied,
                         "future_dated_printings": group["future_dated"]}
    return catalog, {"printings": total, "sets": len(catalog), "oracle_ids_all_languages_and_media": len(all_oracle_ids),
                     "english_paper": sum(v["english_paper"] for v in catalog.values()),
                     "released_english_paper": sum(v["released_english_paper"] for v in catalog.values()),
                     "future_dated_printings": sum(v["future_dated_printings"] for v in catalog.values()),
                     "undated_printings": undated,
                     "same_day_debut_identities": sum(len(sets) > 1 for sets in debut_sets.values())}


def audit(baseline, catalog, summary, source, cutoff):
    previous = baseline["sets"]
    new_codes = sorted(set(catalog) - set(previous))
    missing_codes = sorted(set(previous) - set(catalog))
    changes = {}
    for code in sorted(set(catalog) & set(previous)):
        a, b = previous[code], catalog[code]
        d = {k: b[k] - a[k] for k in ("printings", "english_paper") if b[k] != a[k]}
        if d:
            changes[code] = d
    breakdown = defaultdict(lambda: {"set_codes": 0, "printing_records": 0, "english_paper": 0})
    for entry in catalog.values():
        cat = breakdown[entry["set_type"]]
        cat["set_codes"] += 1
        cat["printing_records"] += entry["printings"]
        cat["english_paper"] += entry["english_paper"]
    return {"schema": 1, "audit_date": cutoff.isoformat(), "source": source,
            "baseline": validate_baseline(baseline), "snapshot": summary,
            "comparison": {"new_set_codes": new_codes, "absent_set_codes": missing_codes,
                           "changed_sets": changes, "changed_set_count": len(changes),
                           "net_printing_delta": summary["printings"] - baseline["total_printings"],
                           "net_english_paper_delta": summary["english_paper"] - sum(x["english_paper"] for x in previous.values())},
            "scryfall_set_types": dict(sorted(breakdown.items())),
            "interpretation": [
                "Scryfall set_type describes its source category; expansion/core is not a certified list of premier releases.",
                "Printing count is distinct Scryfall printing ID in Default Cards, including variants, promos and future-dated previews.",
                "Debuts use each Oracle ID's earliest available released English paper printing through the audit date; same-day cross-set ties are tracked separately.",
                "Earliest/latest printing dates are not independently verified product release dates.",
                "The historical shard bytes were not audited here; only the baseline manifest's internal totals and references were checked."
            ]}


def generate(baseline, snapshot, release_manifest, cutoff):
    source = verify_source(snapshot, release_manifest)
    previous = json.loads(baseline.read_text(encoding="utf-8"))
    validate_baseline(previous)
    catalog, summary = analyze(source_rows(snapshot), cutoff)
    if summary["printings"] != source["manifest_records"]:
        raise ValueError("source row count differs from verified release manifest")
    report = audit(previous, catalog, summary, source, cutoff)
    return report, {"schema": 1, "as_of": cutoff.isoformat(), "source_sha256": source["sha256"],
                    "count_policy": "Distinct Scryfall printing ID; English paper debut/reprint counts are as-of the cutoff",
                    "sets": catalog}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, default=ROOT / "data/printing_lore/manifest.json")
    parser.add_argument("--snapshot", required=True, type=Path)
    parser.add_argument("--snapshot-manifest", required=True, type=Path)
    parser.add_argument("--as-of", required=True, type=date.fromisoformat)
    parser.add_argument("--write", action="store_true", help="publish only Phase 1B audit/catalog artifacts")
    args = parser.parse_args()
    report, catalog = generate(args.baseline, args.snapshot, args.snapshot_manifest, args.as_of)
    if args.write:
        ATLAS.mkdir(parents=True, exist_ok=True)
        (ATLAS / f"audit_{args.as_of}.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        (ATLAS / f"catalog_{args.as_of}.json").write_text(json.dumps(catalog, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"as_of": args.as_of.isoformat(), "write": args.write,
                      "sets": report["snapshot"]["sets"], "printings": report["snapshot"]["printings"],
                      "english_paper": report["snapshot"]["english_paper"],
                      "future_printings": report["snapshot"]["future_dated_printings"],
                      "changed_sets": report["comparison"]["changed_sets"],
                      "same_day_debut_identities": report["snapshot"]["same_day_debut_identities"]}, indent=2))


if __name__ == "__main__":
    main()
