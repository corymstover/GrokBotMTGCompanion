#!/usr/bin/env python3
"""Export compact, GitHub-readable set/printing/flavor shards from printing_lore.sqlite3.

The SQLite database is for fast full-text searches; this text export lets a
GitHub-only client answer set inventory and per-edition flavor questions by
reading one manifest and one or a few bounded shards, without a new download.

    python3 scripts/export_printing_lore.py build
    python3 scripts/export_printing_lore.py set lea --json --all
    python3 scripts/export_printing_lore.py flavor "Urza" --set atq --json
    python3 scripts/export_printing_lore.py check

Output is *not* the canonical card database. Keep the Grixis snapshot lock and
all old decks untouched. Source text comes from Scryfall default-cards; that
bulk covers English/default-language printings, not every translation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB = ROOT / ".cache" / "printing_lore.sqlite3"
DEFAULT_DIR = ROOT / "data" / "printing_lore"
SHARD_BYTES = 450_000  # keep individual files well below GitHub's 1 MiB contents API limit


def compact(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def record(conn, p):
    faces = []
    for f in conn.execute("SELECT name, type_line, oracle_text, flavor_text, flavor_name FROM faces "
                          "WHERE printing_id=? ORDER BY face_number", (p["id"],)):
        z = {"n": f["name"]}
        if f["flavor_text"]:
            z["f"] = f["flavor_text"]
        if f["flavor_name"]:
            z["fn"] = f["flavor_name"]
        # Sagawise rule chapters matter for narrative decks; other Oracle text is
        # already in the canonical card shards and is not duplicated here.
        if "Saga" in (f["type_line"] or ""):
            z["t"] = f["type_line"]
            z["chapters"] = f["oracle_text"] or ""
        faces.append(z)
    r = {"id": p["id"], "o": p["oracle_id"], "n": p["name"], "s": p["set_code"],
         "c": p["collector_number"], "l": p["lang"], "p": p["paper"], "r": p["released_at"]}
    if p["digital"]:
        r["d"] = 1
    if p["story_spotlight"]:
        r["spotlight"] = 1
    if p["scryfall_uri"]:
        r["url"] = p["scryfall_uri"]
    if faces:
        r["faces"] = faces
    return r


def export(db: Path, out: Path, max_bytes=SHARD_BYTES):
    if not db.is_file():
        raise FileNotFoundError(f"Missing {db}; build scripts/printing_lore_index.py first")
    out.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    meta = dict(conn.execute("SELECT key, value FROM meta"))
    manifest = {"schema": 1, "authority": meta["authority"], "coverage": meta.get("coverage", "default-cards snapshot"),
                "source": meta["source"], "source_sha256": meta["source_sha256"],
                "shard_bytes_max": max_bytes, "sets": {}, "shards": {}}
    # Rows are sorted by set so each set is found in one or a few shard files.
    rows = conn.execute("SELECT * FROM printings ORDER BY set_code, "
                        "CAST(collector_number AS INTEGER), collector_number, lang, id")
    current, lines, size, seq = None, [], 0, defaultdict(int)

    def flush():
        nonlocal lines, size, current
        if not lines:
            return
        prefix = current or "_"
        name = f"{prefix}-{seq[prefix]:03d}.jsonl"
        seq[prefix] += 1
        data = ("\n".join(lines) + "\n").encode("utf-8")
        (out / name).write_bytes(data)
        manifest["shards"][name] = {"bytes": len(data), "sha256": digest(data), "rows": len(lines)}
        for code in {json.loads(line)["s"] for line in lines}:
            if name not in manifest["sets"][code]["files"]:
                manifest["sets"][code]["files"].append(name)
        lines, size = [], 0

    for p in rows:
        code = p["set_code"]
        entry = manifest["sets"].setdefault(code, {"name": p["set_name"], "printings": 0,
                                                  "english_paper": 0, "files": []})
        entry["printings"] += 1
        entry["english_paper"] += int(p["paper"] and p["lang"] == "en")
        line = compact(record(conn, p))
        b = len(line.encode("utf-8")) + 1
        prefix = code[0] if code else "_"
        if lines and (prefix != current or size + b > max_bytes):
            flush()
        if b > max_bytes:
            raise ValueError(f"Single printing row {p['id']} exceeds shard byte cap")
        current = prefix
        lines.append(line)
        size += b
    flush()
    conn.close()
    manifest["total_printings"] = sum(x["printings"] for x in manifest["sets"].values())
    manifest["total_shards"] = len(manifest["shards"])
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def check(db: Path, out: Path) -> bool:
    if not (out / "manifest.json").is_file():
        return False
    expected = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="printing-export-check-") as tmp:
        actual = export(db, Path(tmp), expected["shard_bytes_max"])
        return expected == actual and all(digest((out / n).read_bytes()) == m["sha256"]
                                          for n, m in expected["shards"].items())


def lookup(out: Path, code: str, phrase: str | None, *, english_only=True, paper_only=True, limit=30):
    manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    code = code.lower()
    entry = manifest["sets"].get(code)
    if not entry:
        raise ValueError(f"Unknown set: {code}")
    count, names, ids, hits = 0, set(), set(), []
    for shard in entry["files"]:
        with (out / shard).open(encoding="utf-8") as fh:
            for line in fh:
                obj = json.loads(line)
                if obj["s"] != code or (english_only and obj["l"] != "en") or (paper_only and not obj["p"]):
                    continue
                if phrase is not None and not any(phrase.casefold() in f.get("f", "").casefold() for f in obj.get("faces", [])):
                    continue
                count += 1
                names.add(obj["n"])
                ids.add(obj.get("o") or obj["n"])
                if len(hits) < limit:
                    hits.append(obj)
    return {"set": code, "set_name": entry["name"], "matches": count, "distinct_names": len(names),
            "oracle_cards": len(ids), "items": hits,
            "snapshot": {"source": manifest["source"], "sha256": manifest["source_sha256"]},
            "note": "For all rows pass --all; matches count is unaffected by item display limit"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--dir", type=Path, default=DEFAULT_DIR)
    sub = parser.add_subparsers(dest="action", required=True)
    sub.add_parser("build")
    sub.add_parser("check")
    a = sub.add_parser("set")
    a.add_argument("code")
    b = sub.add_parser("flavor")
    b.add_argument("phrase")
    b.add_argument("--set", dest="code", required=True)
    for p in (a, b):
        p.add_argument("--all", action="store_true")
        p.add_argument("--limit", type=int, default=30)
        p.add_argument("--all-languages", action="store_true")
        p.add_argument("--include-digital", action="store_true")
        p.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.action == "build":
            m = export(args.db, args.dir)
            print(compact({"sets": len(m["sets"]), "shards": m["total_shards"], "printings": m["total_printings"]}))
        elif args.action == "check":
            ok = check(args.db, args.dir)
            print("printing shard export: " + ("current" if ok else "STALE"))
            return 0 if ok else 1
        else:
            r = lookup(args.dir, args.code, getattr(args, "phrase", None),
                       english_only=not args.all_languages, paper_only=not args.include_digital,
                       limit=10**9 if args.all else args.limit)
            print(json.dumps(r, ensure_ascii=False, indent=None if args.json else 2))
    except (OSError, ValueError, sqlite3.Error) as exc:
        print(f"export_printing_lore: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
