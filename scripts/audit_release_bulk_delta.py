#!/usr/bin/env python3
"""Reproducible, read-only field audit between SHA-pinned Scryfall bulk snapshots.

Keep the original bulk bytes outside git. Never update card shards, approved decks,
or historical snapshots from this audit. Both manifests must be accompanied by all
three original compressed files; counts, byte lengths, and SHA-256 are checked.

Example:
  python3 scripts/audit_release_bulk_delta.py \
    --old-manifest data/scryfall_snapshots/snap-20261030-live-20261031.manifest.json \
    --new-manifest data/scryfall_snapshots/snap-20261101-live-20261101.manifest.json \
    --old-dir /tmp/old-scryfall --new-dir /tmp/new-scryfall \
    --output data/scryfall_snapshots/oct30_to_nov01_release_delta_2026-11-01.json
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KINDS = ("oracle-cards", "default-cards", "rulings")
ORACLE_FIELDS = ("name", "type_line", "color_identity", "commander_legality",
                 "game_changer", "oracle_text_digest", "layout", "keywords")
PRINT_FIELDS = ("oracle_id", "set", "collector_number", "lang", "digital",
                "released_at", "illustration_id", "image_status", "artist", "layout")


def sha_bytes(path: Path) -> tuple[int, str]:
    h, size = hashlib.sha256(), 0
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            size += len(chunk)
            h.update(chunk)
    return size, h.hexdigest()


def raw_records(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                item = json.loads(line)
                if not isinstance(item, dict):
                    raise ValueError(f"not a JSON object: {path}")
                yield item


def text_digest(card: dict) -> str:
    text = [card.get("oracle_text"), [f.get("oracle_text") for f in card.get("card_faces", [])]]
    return hashlib.sha256(json.dumps(text, ensure_ascii=False).encode()).hexdigest()


def fields(item: dict, kind: str) -> dict:
    if kind == "oracle-cards":
        return {"name": item.get("name"), "type_line": item.get("type_line"),
                "color_identity": item.get("color_identity"),
                "commander_legality": item.get("legalities", {}).get("commander"),
                "game_changer": item.get("game_changer"),
                "oracle_text_digest": text_digest(item), "layout": item.get("layout"),
                # Scryfall may reorder a keyword array without changing the
                # card's abilities. Treat only membership changes as drift.
                "keywords": sorted(item.get("keywords") or [])}
    if kind == "default-cards":
        return {k: item.get(k) for k in PRINT_FIELDS}
    raise ValueError(kind)


def load_snapshot(manifest: dict, directory: Path) -> dict:
    if manifest.get("schema_version") != 1 or set(manifest.get("files", {})) != set(KINDS):
        raise ValueError("unexpected Scryfall manifest structure")
    out = {}
    for kind in KINDS:
        meta = manifest["files"][kind]
        path = directory / meta["filename"]
        size, checksum = sha_bytes(path)
        if (size, checksum) != (meta["compressed_bytes"], meta["sha256"]):
            raise ValueError(f"unverified source bytes: {path}")
        if kind == "rulings":
            values = Counter()
            for item in raw_records(path):
                values[json.dumps(item, sort_keys=True, ensure_ascii=False)] += 1
            count = sum(values.values())
        else:
            values = {}
            for item in raw_records(path):
                # An oracle-cards record has a *printing* id as well as the
                # stable oracle_id. Reprinting must not look like a new card.
                ident = item["oracle_id"] if kind == "oracle-cards" else item["id"]
                if ident in values:
                    raise ValueError(f"duplicate {kind} id: {ident}")
                selected = fields(item, kind)
                signature = hashlib.sha256(json.dumps(item, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
                values[ident] = (selected, signature)
            count = len(values)
        if count != meta["records"]:
            raise ValueError(f"source record count differs from manifest: {kind}")
        out[kind] = values
    return out


def summarize_changes(old: dict, new: dict, kind: str) -> dict:
    before, after = set(old), set(new)
    common = before & after
    keys = ORACLE_FIELDS if kind == "oracle-cards" else PRINT_FIELDS
    names = Counter()
    changes = []
    other = 0
    for ident in common:
        a, ah = old[ident]
        b, bh = new[ident]
        if ah == bh:
            continue
        changed = [key for key in keys if a[key] != b[key]]
        names.update(changed)
        if not changed:
            other += 1
            continue
        changes.append({"id": ident, "name": b.get("name") if kind == "oracle-cards" else None,
                        "fields": changed})
    return {"baseline_records": len(old), "current_records": len(new),
            "added_ids": len(after - before), "removed_ids": len(before - after),
            "existing_ids_with_tracked_field_changes": len(changes),
            "changed_fields": {key: names[key] for key in keys},
            "other_untracked_metadata_changed": other,
            "new_id_samples": sorted(after - before)[:20],
            "removed_id_samples": sorted(before - after)[:20],
            "changed_existing_samples": sorted(changes, key=lambda c: c["id"])[:25]}


def index_drift(oracle: dict, index_path: Path) -> dict:
    with index_path.open(newline="", encoding="utf-8") as f:
        indexed = {r["oracle_id"]: r for r in csv.DictReader(f)}
    missing = set(indexed) - set(oracle)
    added = set(oracle) - set(indexed)
    changes = defaultdict(list)
    for ident in indexed.keys() & oracle.keys():
        old, now = indexed[ident], oracle[ident][0]
        compares = {
            "name": (old["name"], now["name"]),
            "type_line": (old["type_line"], now["type_line"]),
            "color_identity": (set(old["color_identity"].replace("C", "")), set(now["color_identity"] or [])),
            "commander_legality": (old["commander_legality"], now["commander_legality"]),
            "game_changer": (old["game_changer"] == "1", bool(now["game_changer"])),
        }
        for field, (before, after) in compares.items():
            if before != after:
                changes[field].append(old["name"])
    return {"indexed_ids": len(indexed), "current_ids": len(oracle),
            "missing_indexed_ids": len(missing), "new_ids_not_in_index": len(added),
            "new_ids_samples": sorted(oracle[oid][0]["name"] for oid in added)[:20],
            "field_differences": {key: {"count": len(changes[key]), "first_20_names": sorted(changes[key])[:20]}
                                  for key in ("name", "type_line", "color_identity", "commander_legality", "game_changer")}}


def protected_art_metadata_parity(old_printings: dict, new_printings: dict, repo: Path) -> dict:
    """Independently check prior exact-art references, without revising visual evidence."""
    pack = json.loads((repo / "data/lore_research/pack_a4_printing_art_matches_2026-10-30.json").read_text())
    labels = json.loads((repo / "data/lore_research/story_image_label_printings_2026-10-30.json").read_text())
    ids = set()
    for row in pack["cards"]:
        ids.add(row["visually_reviewed_printing"]["id"])
        ids.update(row["same_art_printing_ids"])
        if row.get("known_different_art_first_indexed_promo"):
            ids.add(row["known_different_art_first_indexed_promo"]["id"])
    ids.update(row["printing"]["scryfall_id"] for row in labels["labels"] if row["status"] == "MATCHED")
    missing = sorted(ids - set(new_printings))
    changed = sorted(ident for ident in ids & set(old_printings) & set(new_printings)
                     if any(old_printings[ident][0][field] != new_printings[ident][0][field]
                            for field in ("oracle_id", "set", "collector_number", "illustration_id", "artist")))
    return {"checked_specific_printings": len(ids), "missing_from_new_bulk": missing,
            "material_art_identity_changes": changed,
            "limitation": "Source metadata parity only; prior human visual matches were not repeated."}


def audit(old_manifest: dict, new_manifest: dict, old_dir: Path, new_dir: Path,
          index_path: Path | None = None) -> dict:
    old, new = load_snapshot(old_manifest, old_dir), load_snapshot(new_manifest, new_dir)
    rulings_unchanged = old["rulings"] == new["rulings"]
    removed = old["rulings"] - new["rulings"]
    added = new["rulings"] - old["rulings"]
    report = {
        "schema": "release-bulk-field-delta/v1", "status": "SOURCE_DRIFT_AUDIT_NOT_AUTO_INGESTION",
        "baseline_snapshot": old_manifest["snapshot_id"], "current_snapshot": new_manifest["snapshot_id"],
        "baseline_manifest_files": old_manifest["files"], "current_manifest_files": new_manifest["files"],
        "source_bytes_sha256_and_counts_verified": True,
        "delta": {
            "oracle-cards": summarize_changes(old["oracle-cards"], new["oracle-cards"], "oracle-cards"),
            "default-cards": summarize_changes(old["default-cards"], new["default-cards"], "default-cards"),
            "rulings": {"baseline_records": sum(old["rulings"].values()),
                        "current_records": sum(new["rulings"].values()),
                        "identical_record_multiset": rulings_unchanged,
                        "removed_records": sum(removed.values()), "added_records": sum(added.values())},
        },
        "limits": ["Field-level differences require explicit review; this is not a live legality guarantee.",
                   "No card shards, historical snapshots, approved decks or lore claims were changed.",
                   "The current Scryfall bulk files must be re-checked against API metadata at release time."]}
    if index_path:
        report["indexed_card_parity"] = index_drift(new["oracle-cards"], index_path)
        report["prior_art_source_integrity"] = protected_art_metadata_parity(
            old["default-cards"], new["default-cards"], index_path.parents[1])
    return report


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("old-manifest", "new-manifest", "old-dir", "new-dir", "output"):
        p.add_argument("--" + name, type=Path, required=True)
    p.add_argument("--card-index", type=Path, default=ROOT / "data/card_index.csv")
    a = p.parse_args()
    old = json.loads(a.old_manifest.read_text(encoding="utf-8"))
    new = json.loads(a.new_manifest.read_text(encoding="utf-8"))
    report = audit(old, new, a.old_dir, a.new_dir, a.card_index)
    a.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS verified {old['snapshot_id']} → {new['snapshot_id']}")
    for key, value in report["delta"].items():
        print(f"  {key}: {value.get('existing_ids_with_tracked_field_changes', value.get('added_records'))} tracked-field changes / "
              f"{value.get('added_ids', 0)} new IDs")
    print("  index drift:", {k: v["count"] for k, v in report["indexed_card_parity"]["field_differences"].items()})


if __name__ == "__main__":
    main()
