#!/usr/bin/env python3
"""Capture and verify three immutable Scryfall bulk inputs for MTG Multiverse.

The files are deliberately NOT committed to git. A publishing workflow stores
the compressed bytes and this manifest together as durable GitHub release assets.
This tool never reads or changes data/grixis/dev_snapshot_lock.json.
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
import re
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

KINDS = ("oracle-cards", "default-cards", "rulings")
API = "https://api.scryfall.com/bulk-data"
HEADERS = {
    "User-Agent": "MTGMultiverseCompanion/1.0 (+https://github.com/corymstover/GrokBotMTGCompanion)",
    "Accept": "application/json;q=0.9,*/*;q=0.8",
}


def request(url: str):
    return urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=300)


def checksum(path: Path) -> tuple[int, str]:
    h = hashlib.sha256()
    n = 0
    with path.open("rb") as f:
        for buf in iter(lambda: f.read(1024 * 1024), b""):
            h.update(buf)
            n += len(buf)
    return n, h.hexdigest()


def jsonl_records(path: Path) -> int:
    n = 0
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                item = json.loads(line)
                if not isinstance(item, dict):
                    raise ValueError(f"non-object JSONL record in {path.name}")
                n += 1
    if n == 0:
        raise ValueError(f"empty Scryfall bulk: {path.name}")
    return n


def safe_name(url: str, kind: str) -> str:
    name = Path(urllib.parse.urlsplit(url).path).name
    if not re.fullmatch(r"[a-z0-9-]+-\d{14}\.jsonl\.gz", name) or not name.startswith(kind + "-"):
        raise ValueError(f"unexpected Scryfall JSONL download filename for {kind}: {name!r}")
    return name


def capture(folder: Path, snapshot_id: str) -> Path:
    if not re.fullmatch(r"snap-[a-zA-Z0-9_-]+", snapshot_id):
        raise ValueError("snapshot_id must be a simple snap-* identifier")
    folder.mkdir(parents=True, exist_ok=True)
    manifest_file = folder / "manifest.json"
    if manifest_file.exists():
        raise FileExistsError("snapshot already has a manifest; never replace an existing capture")
    files = {}
    for kind in KINDS:
        with request(f"{API}/{kind}") as resp:
            meta = json.load(resp)
        url = meta.get("jsonl_download_uri")
        if not url or urllib.parse.urlsplit(url).scheme != "https":
            raise ValueError(f"{kind} did not advertise an HTTPS jsonl_download_uri")
        name = safe_name(url, kind)
        dest = folder / name
        if not dest.exists():
            fd, part_name = tempfile.mkstemp(prefix=f".{name}.", suffix=".part", dir=folder)
            try:
                with os.fdopen(fd, "wb") as out, request(url) as inp:
                    for buf in iter(lambda: inp.read(1024 * 1024), b""):
                        out.write(buf)
                os.replace(part_name, dest)
            finally:
                if os.path.exists(part_name):
                    os.unlink(part_name)
        size, sha = checksum(dest)
        count = jsonl_records(dest)
        files[kind] = {
            "filename": name,
            "sha256": sha,
            "compressed_bytes": size,
            "records": count,
            "scryfall_updated_at": meta["updated_at"],
            "source_url": url,
        }
    manifest = {
        "schema_version": 1,
        "snapshot_id": snapshot_id,
        "captured_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "source": "Scryfall JSONL bulk API",
        "files": files,
        "legacy_grixis_snapshot_unchanged": "snap-20261016",
    }
    manifest_file.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    verify(folder)
    return manifest_file


def verify(folder: Path) -> dict:
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1 or set(manifest.get("files", {})) != set(KINDS):
        raise ValueError("manifest schema or bulk-kind set is invalid")
    for kind in KINDS:
        item = manifest["files"][kind]
        name = item["filename"]
        if Path(name).name != name or not name.startswith(kind + "-"):
            raise ValueError(f"invalid manifest path for {kind}")
        path = folder / name
        size, sha = checksum(path)
        if size != item["compressed_bytes"] or sha != item["sha256"]:
            raise ValueError(f"checksum/size mismatch for {kind}")
        if jsonl_records(path) != item["records"]:
            raise ValueError(f"record count mismatch for {kind}")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("capture", "verify"))
    parser.add_argument("--dir", required=True, type=Path, help="directory for bulk files and manifest")
    parser.add_argument("--snapshot-id", help="required for capture, e.g. snap-20261029-run123")
    args = parser.parse_args()
    if args.command == "capture":
        if not args.snapshot_id:
            parser.error("--snapshot-id is required for capture")
        capture(args.dir, args.snapshot_id)
    else:
        verify(args.dir)
    print(f"{args.command}: three bulk files independently checked in {args.dir}")


if __name__ == "__main__":
    main()
