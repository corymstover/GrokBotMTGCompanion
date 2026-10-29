#!/usr/bin/env python3
"""Read-only Scryfall snapshot versus committed card/lore research inventory.

Produces a bounded evidence report. No card shards, enrichment records, lore
relations, 62-deck approvals, or historical development snapshots are edited.
The existing 2026-10-16 Oracle text is not generally archived in the index, so
this tool explicitly DOES NOT claim a complete historical Oracle-text diff.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scryfall_snapshot as snapshots  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def rows(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def sample(names, limit=30):
    return sorted(names, key=str.casefold)[:limit]


def reconcile(snapshot_dir: Path, repo_root: Path = ROOT) -> dict:
    manifest = snapshots.verify(snapshot_dir)
    files = manifest["files"]
    with (repo_root / "data/card_index.csv").open(encoding="utf-8", newline="") as f:
        index = {r["oracle_id"]: r for r in csv.DictReader(f)}
    enrichment = json.loads((repo_root / "data/card_enrichment.json").read_text(encoding="utf-8"))
    enriched = enrichment["cards"]
    printing_manifest = json.loads((repo_root / "data/printing_lore/manifest.json").read_text(encoding="utf-8"))

    new_oracles = {}
    for card in rows(snapshot_dir / files["oracle-cards"]["filename"]):
        if card.get("oracle_id"):
            new_oracles[card["oracle_id"]] = card

    old_ids, current_ids = set(index), set(new_oracles)
    additions = current_ids - old_ids
    missing = old_ids - current_ids
    type_changes, identity_changes, legality_changes, changer_changes = [], [], [], []
    rank_changes = 0
    for oid in old_ids & current_ids:
        old, new = index[oid], new_oracles[oid]
        label = f"{old['name']} → {new.get('name', old['name'])}" if old["name"] != new.get("name") else old["name"]
        if old["type_line"] != new.get("type_line", ""):
            type_changes.append(label)
        old_ci = set(old["color_identity"].replace("C", ""))
        if old_ci != set(new.get("color_identity") or []):
            identity_changes.append(label)
        if old["commander_legality"] != new.get("legalities", {}).get("commander", ""):
            legality_changes.append(label)
        if old["game_changer"] in ("1", "0") and (old["game_changer"] == "1") != bool(new.get("game_changer")):
            changer_changes.append(label)
        old_rank, new_rank = old.get("edhrec_rank", ""), new.get("edhrec_rank")
        if old_rank != ("" if new_rank is None else str(new_rank)):
            rank_changes += 1

    ruling_counts = Counter()
    for ruling in rows(snapshot_dir / files["rulings"]["filename"]):
        if ruling.get("oracle_id"):
            ruling_counts[ruling["oracle_id"]] += 1
    ruling_changes = []
    for oid, old in index.items():
        if old["rulings"].isdigit() and int(old["rulings"]) != ruling_counts.get(oid, 0):
            ruling_changes.append(old["name"])

    printing_counts = Counter()
    for printing in rows(snapshot_dir / files["default-cards"]["filename"]):
        printing_counts["all_default_records"] += 1
        if printing.get("digital"):
            continue
        printing_counts["paper_records"] += 1
        if printing.get("lang") == "en":
            printing_counts["english_paper_records"] += 1
        if printing.get("story_spotlight"):
            printing_counts["paper_story_spotlight"] += 1
        if printing.get("flavor_text") or any(f.get("flavor_text") for f in printing.get("card_faces") or []):
            printing_counts["paper_with_flavor_text"] += 1

    categories = {
        "previously_indexed_oracle_ids_missing_now": [index[oid]["name"] for oid in missing],
        "new_oracle_ids_not_in_committed_index": [new_oracles[oid]["name"] for oid in additions],
        "type_line_differences": type_changes,
        "color_identity_differences": identity_changes,
        "commander_legality_differences": legality_changes,
        "game_changer_differences": changer_changes,
        "indexed_ruling_count_differences": ruling_changes,
        "previously_enriched_oracle_ids_missing_now": [enriched[oid]["name"] for oid in set(enriched) - current_ids],
    }
    return {
        "schema_version": 1,
        "evidence_class": "read_only_reconciliation",
        "decision_authority": False,
        "snapshot_id": manifest["snapshot_id"],
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "compared_to": {
            "card_index_csv": "data/card_index.csv",
            "card_enrichment_json": "data/card_enrichment.json",
            "card_enrichment_prior_bulk": enrichment.get("bulk"),
            "printing_lore_prior_source": printing_manifest.get("source"),
            "printing_lore_prior_sha256": printing_manifest.get("source_sha256"),
        },
        "counts": {
            "prior_index_oracle_ids": len(index),
            "prior_enriched_oracle_ids": len(enriched),
            "current_oracle_ids": len(current_ids),
            "current_rulings": sum(ruling_counts.values()),
            **dict(printing_counts),
            "prior_printing_archive_english_paper": sum(s.get("english_paper", 0) for s in printing_manifest["sets"].values()),
            "edhrec_rank_differences": rank_changes,
        },
        "review_categories": {
            k: {"count": len(names), "first_30_names": sample(names)} for k, names in categories.items()
        },
        "limits": [
            "Legacy Oracle text was not stored in a directly comparable complete input archive; no Oracle-text delta claim is made.",
            "Printing archive aggregate and new Scryfall paper counts may differ by coverage, filtering and publication date.",
            "New IDs not in the committed index are discovery leads, not proof that all belong in a lore/Commander pool.",
            "No suggested deck swap, canon status, identity change, or legality conclusion is approved by this report.",
        ],
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--snapshot-dir", required=True, type=Path)
    p.add_argument("--repo-root", type=Path, default=ROOT)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    report = reconcile(args.snapshot_dir, args.repo_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("Read-only reconciliation:", report["snapshot_id"])
    for kind, details in report["review_categories"].items():
        print(f"  {kind}: {details['count']}")
    print("No canonical files changed.")


if __name__ == "__main__":
    main()
