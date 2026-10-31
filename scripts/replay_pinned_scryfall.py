#!/usr/bin/env python3
"""Independently replay recovered historical Scryfall bytes; never update a deck.

Full proof (requires the seven named, SHA-pinned files):
  python3 scripts/replay_pinned_scryfall.py --dir /path/to/recovered

Portable CI check (does not pretend the uncommitted bulk files are present):
  python3 scripts/replay_pinned_scryfall.py --check

The full proof rebuilds October 28 SQLite + all printing-lore exports and compares
every generated file byte-for-byte with the committed 105 shards and manifest. It
also replays October 29's exact printing/illustration metadata against existing
Wizards art-label and six visually reviewed Pack A4 ledgers. Visual review itself
is not repeated; only the underlying Scryfall IDs and metadata are checked.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import export_printing_lore as E  # noqa: E402
import printing_lore_index as P  # noqa: E402

OUT = ROOT / "data/scryfall_snapshots/historical_bulk_replay_2026-10-31.json"
PRINT_MANIFEST = ROOT / "data/printing_lore/manifest.json"
ACTIVE_MANIFEST = ROOT / "data/scryfall_snapshots/snap-20261029-40848334824-1.manifest.json"
LOCK = ROOT / "data/grixis/dev_snapshot_lock.json"
LABELS = ROOT / "data/lore_research/story_image_label_printings_2026-10-30.json"
PACK_A4 = ROOT / "data/lore_research/pack_a4_printing_art_matches_2026-10-30.json"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def checksum(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def verify_file(folder: Path, filename: str, expected_sha: str, expected_bytes: int | None = None) -> dict:
    path = folder / filename
    if not path.is_file():
        raise ValueError(f"missing historical source: {path}")
    actual_bytes = path.stat().st_size
    actual_sha = checksum(path)
    if actual_sha != expected_sha or (expected_bytes is not None and actual_bytes != expected_bytes):
        raise ValueError(f"historical source mismatch: {filename} ({actual_bytes}, {actual_sha})")
    return {"file": filename, "sha256": actual_sha, "compressed_bytes": actual_bytes}


def scan_art(source: Path) -> dict:
    art = read_json(PACK_A4)["cards"]
    labels = [r for r in read_json(LABELS)["labels"] if r["status"] == "MATCHED"]
    needs = {r["printing"]["scryfall_id"] for r in labels}
    for card in art:
        needs.update(card["same_art_printing_ids"])
        needs.add(card["visually_reviewed_printing"]["id"])
        if card.get("known_different_art_first_indexed_promo"):
            needs.add(card["known_different_art_first_indexed_promo"]["id"])
    observed = {}
    with gzip.open(source, "rt", encoding="utf-8") as fh:
        for line in fh:
            record = json.loads(line)
            if record["id"] in needs:
                observed[record["id"]] = record
    errors = [f"missing printing {pid}" for pid in sorted(needs - set(observed))]
    for r in labels:
        p = r["printing"]
        raw = observed.get(p["scryfall_id"])
        if raw and any(raw.get(field) != p[dest] for field, dest in (
            ("name", "name"), ("set", "set"), ("collector_number", "collector_number"),
            ("artist", "artist"), ("released_at", "released_at")
        )):
            errors.append(f"story label printing fields differ: {p['scryfall_id']}")
    for card in art:
        rep = card["visually_reviewed_printing"]
        raw = observed.get(rep["id"])
        if raw and (raw.get("set") != rep["set"] or raw.get("collector_number") != rep["collector_number"]
                    or raw.get("artist") != card["artist"] or raw.get("oracle_id") != card["oracle_id"]
                    or raw.get("illustration_id") != card["matched_illustration_id"]):
            errors.append(f"reviewed art printing mismatch: {rep['id']}")
        for pid in card["same_art_printing_ids"]:
            same = observed.get(pid)
            if same and (same.get("oracle_id") != card["oracle_id"] or
                         same.get("illustration_id") != card["matched_illustration_id"]):
                errors.append(f"same-illustration claim mismatch: {pid}")
        other = card.get("known_different_art_first_indexed_promo")
        if other:
            observed_other = observed.get(other["id"])
            if observed_other and (observed_other.get("illustration_id") != other["illustration_id"]
                                   or observed_other.get("artist") != other["artist"]):
                errors.append(f"different-art exception mismatch: {other['id']}")
    if errors:
        raise ValueError("art metadata replay failed: " + "; ".join(errors[:15]))
    return {"official_story_labels_metadata_matched": len(labels),
            "visually_reviewed_pairs_metadata_matched": len(art),
            "listed_same_art_printings_metadata_matched": sum(len(c["same_art_printing_ids"]) for c in art),
            "unresolved_image_labels_unchanged": len(read_json(LABELS)["labels"]) - len(labels),
            "note": "Scryfall printing metadata only; no new visual comparison or event-depiction assertion."}


def full_replay(folder: Path) -> dict:
    hist, lock, active = read_json(PRINT_MANIFEST), read_json(LOCK), read_json(ACTIVE_MANIFEST)
    old = verify_file(folder, hist["source"], hist["source_sha256"])
    legacy = {}
    for kind, name in sorted(lock["files"].items()):
        legacy[kind] = verify_file(folder, name, lock["sha256"][kind].removeprefix("sha256:"))
    modern = {}
    for kind, meta in sorted(active["files"].items()):
        modern[kind] = verify_file(folder, meta["filename"], meta["sha256"], meta["compressed_bytes"])

    with tempfile.TemporaryDirectory(prefix="historical-printing-replay-") as tmp:
        tmpdir = Path(tmp)
        db = tmpdir / "printings.sqlite3"
        built = P.build(folder / hist["source"], db)
        generated = E.export(db, tmpdir / "shards")
        committed_dir = ROOT / "data/printing_lore"
        regenerated_dir = tmpdir / "shards"
        expected = set(hist["shards"]) | {"manifest.json"}
        actual = {p.name for p in regenerated_dir.iterdir() if p.is_file()}
        missing, extra = sorted(expected - actual), sorted(actual - expected)
        altered = sorted(name for name in expected & actual
                         if (committed_dir / name).read_bytes() != (regenerated_dir / name).read_bytes())
        if missing or extra or altered or generated != hist or int(built["printings"]) != hist["total_printings"]:
            raise ValueError(f"October 28 replay differs: missing={missing} extra={extra} altered={altered}")

    doc = {"schema": "historical-bulk-replay/v1", "recovered_on": "2026-10-31",
           "source_policy": "Exact recorded SHA-256 bytes only; original historical snapshots are never replaced by newer data.",
           "oct28": {**old, "source_url": "https://data.scryfall.io/default-cards/" + hist["source"],
                     "printing_records": hist["total_printings"], "set_codes": len(hist["sets"]),
                     "english_paper_printings": sum(x["english_paper"] for x in hist["sets"].values()),
                     "shards_rebuilt_byte_identical": len(hist["shards"]),
                     "export_manifest_byte_identical": True, "missing_shards": 0, "altered_shards": 0},
           "legacy_grixis": {"snapshot_id": lock["snapshot"], "files": legacy,
                             "lock_file_unchanged": True},
           "active_companion": {"snapshot_id": active["snapshot_id"], "files": modern,
                                "art_metadata": scan_art(folder / active["files"]["default-cards"]["filename"])},
           "scope": "Source-level printing and illustration metadata replay, not complete lore or foundation certification.",
           "protected_decks_modified": False}
    return doc


def portable_check() -> dict:
    """Check proof references and saved outputs; never claim a new bulk replay here."""
    doc = read_json(OUT)
    hist, lock, active = read_json(PRINT_MANIFEST), read_json(LOCK), read_json(ACTIVE_MANIFEST)
    assert doc["schema"] == "historical-bulk-replay/v1"
    assert doc["oct28"]["sha256"] == hist["source_sha256"]
    assert doc["oct28"]["shards_rebuilt_byte_identical"] == len(hist["shards"])
    assert doc["oct28"]["printing_records"] == hist["total_printings"]
    assert doc["oct28"]["export_manifest_byte_identical"] is True
    assert doc["legacy_grixis"]["snapshot_id"] == lock["snapshot"]
    assert doc["active_companion"]["snapshot_id"] == active["snapshot_id"]
    for kind, entry in doc["legacy_grixis"]["files"].items():
        assert entry["file"] == lock["files"][kind]
        assert entry["sha256"] == lock["sha256"][kind].removeprefix("sha256:")
    for kind, entry in doc["active_companion"]["files"].items():
        assert entry["sha256"] == active["files"][kind]["sha256"]
        assert entry["compressed_bytes"] == active["files"][kind]["compressed_bytes"]
    for name, meta in hist["shards"].items():
        p = ROOT / "data/printing_lore" / name
        assert p.stat().st_size == meta["bytes"] and checksum(p) == meta["sha256"], name
    return doc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dir", type=Path, help="directory with the seven recovered historical/modern bulk files")
    ap.add_argument("--check", action="store_true", help="portable evidence check without downloading source files")
    args = ap.parse_args()
    if not args.check and args.dir is None:
        ap.error("--dir required for a full replay")
    if args.check:
        doc = portable_check()
        if args.dir and doc != full_replay(args.dir):
            raise ValueError("recovered-source rerun disagrees with committed report")
    else:
        doc = full_replay(args.dir)
        OUT.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS historical Scryfall: {doc['oct28']['printing_records']:,} printings; "
          f"{doc['oct28']['shards_rebuilt_byte_identical']} identical shards; "
          f"{doc['active_companion']['art_metadata']['official_story_labels_metadata_matched']} art labels")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
