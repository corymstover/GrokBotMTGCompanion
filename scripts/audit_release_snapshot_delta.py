#!/usr/bin/env python3
"""Read-only Oct 29 -> Oct 30 Scryfall Oracle, printing and rulings delta.

The two gzip inputs are intentionally not committed. The portable --check
validates the dated report against both manifest hashes in CI; optional archive
directory arguments also verify every byte/hash and replay all six JSONL files.
No story, card, protected Grixis deck, approval or rules artifact is mutated.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT / "data/scryfall_snapshots/snap-20261029-40848334824-1.manifest.json"
NEW = ROOT / "data/scryfall_snapshots/snap-20261030-live-20261031.manifest.json"
OUT = ROOT / "data/scryfall_snapshots/oct29_to_oct30_release_delta_2026-10-31.json"
KINDS = ("oracle-cards", "default-cards", "rulings")
ORACLE_FIELDS = ("name", "oracle_text_digest", "type_line", "color_identity", "commander_legality", "game_changer")
PRINT_FIELDS = ("oracle_id", "set", "collector_number", "lang", "digital", "released_at",
                "illustration_id", "image_status", "artist", "layout")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def manifest(path: Path) -> dict:
    doc = json.loads(path.read_text(encoding="utf-8"))
    if doc.get("schema_version") != 1 or set(doc.get("files", {})) != set(KINDS):
        raise ValueError("incomplete Scryfall bulk manifest")
    for kind, f in doc["files"].items():
        if not f["source_url"].startswith(f"https://data.scryfall.io/{kind}/{kind}-"):
            raise ValueError("unexpected bulk-data origin")
        if len(f["sha256"]) != 64 or f["compressed_bytes"] <= 0 or f["records"] <= 0:
            raise ValueError("invalid bulk-file hash/size/count")
    return doc


def source_file(meta: dict, directory: Path, kind: str) -> Path:
    item = meta["files"][kind]
    path = directory / item["filename"]
    if path.name != item["filename"] or path.stat().st_size != item["compressed_bytes"]:
        raise ValueError(f"missing/inaccurate {kind} source bytes in {directory}")
    sha = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            sha.update(block)
    if sha.hexdigest() != item["sha256"]:
        raise ValueError(f"{kind} archive SHA-256 differs from manifest")
    return path


def records(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                item = json.loads(line)
                if not isinstance(item, dict):
                    raise ValueError("JSONL row is not a Scryfall object")
                yield item


def oracle_features(c: dict) -> dict:
    faces = c.get("card_faces") or []
    text = "\n".join(f.get("oracle_text", "") for f in faces) if faces else c.get("oracle_text", "") or ""
    return {"name": c.get("name"), "oracle_text_digest": digest(text.encode("utf-8")),
            "type_line": c.get("type_line"), "color_identity": tuple(c.get("color_identity") or []),
            "commander_legality": c.get("legalities", {}).get("commander"),
            "game_changer": bool(c.get("game_changer"))}


def print_features(c: dict) -> dict:
    faces = c.get("card_faces") or []
    art = c.get("illustration_id") or tuple(f.get("illustration_id") for f in faces)
    return {"oracle_id": c.get("oracle_id"), "set": c.get("set"),
            "collector_number": c.get("collector_number"), "lang": c.get("lang"),
            "digital": bool(c.get("digital")), "released_at": c.get("released_at"),
            "illustration_id": art, "image_status": c.get("image_status"),
            "artist": c.get("artist"), "layout": c.get("layout")}


def indexed(path: Path, kind: str) -> tuple[dict, int]:
    key = "oracle_id" if kind == "oracle-cards" else "id"
    fn = oracle_features if kind == "oracle-cards" else print_features
    result, count = {}, 0
    for row in records(path):
        count += 1
        oid = row.get(key)
        if not oid or oid in result:
            raise ValueError(f"missing or duplicated {key} in {kind}")
        result[oid] = fn(row)
    return result, count


def compare(old: dict, new: dict, fields: tuple[str, ...]) -> dict:
    a, b = set(old), set(new)
    changes, examples = Counter(), []
    for ident in sorted(a & b):
        diff = [f for f in fields if old[ident][f] != new[ident][f]]
        if diff:
            changes.update(diff)
            if len(examples) < 30:
                examples.append({"id": ident, "name": new[ident].get("name", ""), "fields": diff})
    return {"baseline_records": len(old), "current_records": len(new),
            "added_ids": len(b - a), "removed_ids": len(a - b),
            "existing_ids_changed": sum(1 for ident in a & b if old[ident] != new[ident]),
            "changed_fields": {f: changes[f] for f in fields},
            "new_id_samples": sorted(b - a)[:30], "removed_id_samples": sorted(a - b)[:30],
            "changed_existing_samples": examples}


def ruling_multiset(path: Path) -> tuple[Counter, int]:
    hashes, n = Counter(), 0
    for item in records(path):
        n += 1
        # A comment's SHA is compared; the copyrighted full comment is not stored.
        ident = (item.get("oracle_id"), item.get("source"), item.get("published_at"),
                 digest((item.get("comment") or "").encode("utf-8")))
        hashes[ident] += 1
    return hashes, n


def build(old_dir: Path, new_dir: Path) -> dict:
    old, new = manifest(OLD), manifest(NEW)
    files = {kind: (source_file(old, old_dir, kind), source_file(new, new_dir, kind)) for kind in KINDS}
    checks = {}
    for kind in ("oracle-cards", "default-cards"):
        before, count_before = indexed(files[kind][0], kind)
        after, count_after = indexed(files[kind][1], kind)
        if (count_before, count_after) != (old["files"][kind]["records"], new["files"][kind]["records"]):
            raise ValueError(kind + " record counts disagree with pinned manifest")
        checks[kind] = compare(before, after, ORACLE_FIELDS if kind == "oracle-cards" else PRINT_FIELDS)
    before, bcount = ruling_multiset(files["rulings"][0])
    after, acount = ruling_multiset(files["rulings"][1])
    if (bcount, acount) != (old["files"]["rulings"]["records"], new["files"]["rulings"]["records"]):
        raise ValueError("ruling counts disagree with pinned manifest")
    checks["rulings"] = {"baseline_records": bcount, "current_records": acount,
                         "added": sum((after - before).values()), "removed": sum((before - after).values()),
                         "copyrighted_comments_embedded": False}
    return {"schema": "scryfall-release-snapshot-delta/v1", "as_of": "2026-10-31",
            "baseline_snapshot": old["snapshot_id"], "current_snapshot": new["snapshot_id"],
            "source_manifests": {"baseline_sha256": digest(OLD.read_bytes()),
                                 "current_sha256": digest(NEW.read_bytes())},
            "archives_strictly_verified": True, "delta": checks, "source_text_embedded": False,
            "limits": ["Source metadata are release-date snapshot comparisons, not official card street-release dates.",
                       "New Oracle IDs across bulk snapshots are not necessarily playable or eligible for the Companion's scoped card index.",
                       "Changed text hashes are review leads, not authority to rewrite cards, artwork or rules.",
                       "This evidence does not certify a completed MTG knowledge foundation or start deckbuilding."]}


def check_stored() -> dict:
    old, new = manifest(OLD), manifest(NEW)
    doc = json.loads(OUT.read_text(encoding="utf-8"))
    if doc.get("schema") != "scryfall-release-snapshot-delta/v1" or \
       doc.get("source_manifests") != {"baseline_sha256": digest(OLD.read_bytes()),
                                       "current_sha256": digest(NEW.read_bytes())} or \
       doc.get("baseline_snapshot") != old["snapshot_id"] or doc.get("current_snapshot") != new["snapshot_id"] or \
       doc.get("archives_strictly_verified") is not True or doc.get("source_text_embedded") is not False:
        raise ValueError("stored Scryfall release-freshness evidence not pinned to source manifests")
    for kind in KINDS:
        row = doc["delta"][kind]
        if (row["baseline_records"], row["current_records"]) != \
           (old["files"][kind]["records"], new["files"][kind]["records"]):
            raise ValueError("stored Scryfall delta no longer matches snapshot record counts")
        if kind != "rulings" and (row["added_ids"] < 0 or row["removed_ids"] < 0 or
                                  any(x < 0 for x in row["changed_fields"].values())):
            raise ValueError("invalid stored Scryfall delta fields")
    return doc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--baseline-dir", type=Path)
    ap.add_argument("--current-dir", type=Path)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if args.check:
        doc = check_stored()
        if args.baseline_dir and args.current_dir and build(args.baseline_dir, args.current_dir) != doc:
            raise ValueError("full bulk replay differs from stored delta")
    else:
        if not args.baseline_dir or not args.current_dir:
            ap.error("recording evidence requires both frozen source directories")
        doc = build(args.baseline_dir, args.current_dir)
        OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for kind, row in doc["delta"].items():
        print(kind, {k: v for k, v in row.items() if isinstance(v, int) and not isinstance(v, bool)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
