#!/usr/bin/env python3
"""L291 audit: snapshot manifests carry actual download bytes and stable hashes.

Cross-checks the committed copy of the active Companion snapshot manifest
(release snap-20261029-40848334824-1) against:
  * the GitHub release asset sizes (recorded at build time via `gh`),
  * local box copies of the bulk files when present (bytes + sha256),
  * every in-repo reference to a snapshot hash (printing_lore manifest,
    Phase 1B gates).
Read-only for all inputs; never touches data/grixis/ or the Grixis lock.

Usage: python3 scripts/audit_snapshot_manifests.py [--check]
"""
import hashlib, json, os, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAP = "snap-20261029-40848334824-1"
COPY = ROOT / f"data/scryfall_snapshots/{SNAP}.manifest.json"
OUT = ROOT / "data/scryfall_snapshots/manifest_audit_2026-10-30.json"
LOCAL_DIRS = [Path("/workspace/mv_cache/snap-20261029"), ROOT / ".cache/multiverse"]


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def release_sizes():
    try:
        out = subprocess.run(["gh", "release", "view", SNAP, "-R", "corymstover/GrokBotMTGCompanion",
                              "--json", "assets", "-q", '.assets[]|"\\(.name) \\(.size)"'],
                             capture_output=True, text=True, timeout=60, check=True).stdout
        return {n: int(s) for n, s in (l.split() for l in out.splitlines())}
    except Exception:
        return None


def build():
    m = json.loads(COPY.read_text())
    rel = release_sizes()
    if rel is None:
        raise SystemExit("gh release view unavailable; cannot rebuild (use --check)")
    files = []
    for kind, f in sorted(m["files"].items()):
        row = dict(kind=kind, filename=f["filename"], manifest_bytes=f["compressed_bytes"], manifest_sha256=f["sha256"],
                   records=f["records"], release_asset_bytes=rel.get(f["filename"]))
        row["release_bytes_match"] = row["release_asset_bytes"] == f["compressed_bytes"]
        for d in LOCAL_DIRS:
            p = d / f["filename"]
            if p.exists():
                row["local_check"] = dict(bytes=p.stat().st_size, sha256=sha(p))
                row["local_match"] = row["local_check"] == dict(bytes=f["compressed_bytes"], sha256=f["sha256"])
                break
        else:
            row["local_check"], row["local_match"] = None, None
        files.append(row)
    pl = json.loads((ROOT / "data/printing_lore/manifest.json").read_text())
    gates = json.loads((ROOT / "data/set_atlas/phase1b_snapshot_gates_2026-10-30.json").read_text())["bulk"]
    dc = m["files"]["default-cards"]
    refs = [
        dict(path="data/set_atlas/phase1b_snapshot_gates_2026-10-30.json", file=gates["file"], sha256=gates["sha256"],
             has_bytes=False, matches_active_manifest=(gates["file"] == dc["filename"] and gates["sha256"] == dc["sha256"]),
             note="Hash reference into the active manifest; bytes come from the manifest."),
        dict(path="data/printing_lore/manifest.json", file=pl["source"], sha256=pl["source_sha256"], has_bytes=False,
             matches_active_manifest=False,
             note="Historical 2026-10-28 shard baseline. The original bulk file is unavailable (workflow L151), so its download bytes cannot be measured; left unedited."),
    ]
    ok_active = all(r["release_bytes_match"] and r["local_match"] is not False for r in files)
    return {
        "schema": "snapshot-manifest-audit/v1", "as_of": "2026-10-30", "snapshot_id": SNAP,
        "manifest_copy": str(COPY.relative_to(ROOT)), "manifest_copy_sha256": sha(COPY),
        "files": files, "in_repo_references": refs,
        "l291": {"active_snapshot_ok": ok_active, "closes_l291": False,
                 "reason": "The active Companion manifest has measured bytes and SHA-256 for all 3 files, each matching the release asset size (and local copies where present). The 2026-10-28 printing_lore baseline has a hash but no bytes, and cannot get them while the original file is unavailable (L151)."},
    }


def main():
    if "--check" in sys.argv:
        doc = json.loads(OUT.read_text())
        assert sha(COPY) == doc["manifest_copy_sha256"], "manifest copy changed"
        m = json.loads(COPY.read_text())
        for r in doc["files"]:
            f = m["files"][r["kind"]]
            assert (r["manifest_bytes"], r["manifest_sha256"]) == (f["compressed_bytes"], f["sha256"])
            assert r["release_bytes_match"] and r["local_match"] is not False, r
            for d in LOCAL_DIRS:
                p = d / r["filename"]
                if p.exists() and os.environ.get("AUDIT_REHASH"):
                    assert (p.stat().st_size, sha(p)) == (f["compressed_bytes"], f["sha256"]), p
                    break
        print("snapshot manifest audit OK", doc["l291"]["active_snapshot_ok"])
        return
    doc = build()
    OUT.write_text(json.dumps(doc, indent=2) + "\n")
    print(json.dumps(doc["l291"]), [(r["kind"], r["release_bytes_match"], r["local_match"]) for r in doc["files"]])


if __name__ == "__main__":
    main()
