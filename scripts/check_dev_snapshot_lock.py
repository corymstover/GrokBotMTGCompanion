#!/usr/bin/env python3
"""validate_all step dev-snapshot-lock (Bot cycle 66.3b): the shared cache's active bulk must be the locked dev snapshot.

For every kind in data/grixis/dev_snapshot_lock.json the newest cached `<kind>-*.json*` file (what every script that
globs the cache picks) must be the locked file, with the locked sha256. A newer or missing bulk fails."""
import hashlib, json, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / "data" / "grixis" / "dev_snapshot_lock.json"
CACHE = Path(os.environ.get("SCRYFALL_CACHE", ROOT / ".cache"))


def problems(lock_path=LOCK, cache=CACHE, hashes=True):
    if not lock_path.is_file():
        return []
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    p = []
    for kind, name in sorted(lock["files"].items()):
        cached = sorted(f.name for f in cache.glob(f"{kind}-*.json*") if not f.name.endswith(".part"))
        if name not in cached:
            p.append(f"{kind}: locked bulk {name} missing from the cache")
            continue
        if cached[-1] != name:
            p.append(f"{kind}: active (newest) cached bulk is {cached[-1]}, not the locked {name}")
        if hashes and "sha256:" + hashlib.sha256((cache / name).read_bytes()).hexdigest() != lock["sha256"][kind]:
            p.append(f"{kind}: {name} sha256 differs from the lock")
    return p


if __name__ == "__main__":
    p = problems()
    for e in p:
        print("FAIL", e)
    print(f"dev-snapshot-lock: {len(json.loads(LOCK.read_text())['files']) if LOCK.is_file() else 0} locked bulk(s), {len(p)} problem(s)")
    sys.exit(1 if p else 0)
