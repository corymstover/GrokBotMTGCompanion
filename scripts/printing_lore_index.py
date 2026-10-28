#!/usr/bin/env python3
"""Offline, printing-specific MTG set and flavor lookup.

Build once from GrokBot's existing Scryfall default-cards JSONL cache:
    python3 scripts/printing_lore_index.py build
    python3 scripts/printing_lore_index.py set lea --all --json
    python3 scripts/printing_lore_index.py flavor "Urza" --json
    python3 scripts/printing_lore_index.py card "Plains" --all
    python3 scripts/printing_lore_index.py saga --set neo

Unlike data/printings_summary.csv, this stores *individual editions*, faces,
flavor wording and the source Scryfall URL. It never edits the existing card
shards, curated lore evidence, approved decks, or canonical Grixis state.
The local SQLite index is a rebuildable cache, not a hand-maintained authority.
"""

from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
import sqlite3
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB = ROOT / ".cache" / "printing_lore.sqlite3"

SCHEMA = """
CREATE TABLE printings (
  id TEXT PRIMARY KEY, oracle_id TEXT, name TEXT NOT NULL,
  set_code TEXT NOT NULL, set_name TEXT NOT NULL, collector_number TEXT NOT NULL,
  released_at TEXT, lang TEXT NOT NULL, layout TEXT, set_type TEXT,
  paper INTEGER NOT NULL, digital INTEGER NOT NULL, promo INTEGER NOT NULL,
  story_spotlight INTEGER NOT NULL, scryfall_uri TEXT
);
CREATE TABLE faces (
  printing_id TEXT NOT NULL, face_number INTEGER NOT NULL, name TEXT NOT NULL,
  type_line TEXT, oracle_text TEXT, flavor_text TEXT, flavor_name TEXT,
  PRIMARY KEY (printing_id, face_number),
  FOREIGN KEY (printing_id) REFERENCES printings(id)
);
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE INDEX printing_set ON printings(set_code, lang, paper);
CREATE INDEX printing_name ON printings(name COLLATE NOCASE);
CREATE INDEX printing_oracle ON printings(oracle_id);
CREATE INDEX face_name ON faces(name COLLATE NOCASE);
"""


def source_rows(path: Path):
    """Existing ingest_scryfall.py cache format: one card JSON object per line."""
    op = gzip.open if path.suffix == ".gz" else open
    with op(path, "rt", encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.strip()
            if not line or line in ("[", "]"):
                continue
            try:
                obj = json.loads(line.rstrip(","))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{n}: expected JSONL (run existing Scryfall cache ingest first)") from exc
            if not isinstance(obj, dict):
                raise ValueError(f"{path}:{n}: expected one card object per line")
            yield obj


def latest_source() -> Path:
    matches = sorted((ROOT / ".cache").glob("default-cards-*.jsonl.gz"))
    if not matches:
        raise FileNotFoundError("No .cache/default-cards-*.jsonl.gz; populate the existing Scryfall cache first")
    return matches[-1]


def card_faces(obj):
    faces = obj.get("card_faces") or [obj]
    for i, face in enumerate(faces):
        yield (obj["id"], i, face.get("name") or obj.get("name", ""),
               face.get("type_line") or obj.get("type_line", ""),
               face.get("oracle_text") or (obj.get("oracle_text", "") if len(faces) == 1 else ""),
               face.get("flavor_text") or (obj.get("flavor_text", "") if len(faces) == 1 else ""),
               face.get("flavor_name") or (obj.get("flavor_name", "") if len(faces) == 1 else ""))
    # Preserve unusual top-level text on a multiface layout as its own searchable record.
    if len(faces) > 1 and obj.get("flavor_text") and not any(f.get("flavor_text") == obj["flavor_text"] for f in faces):
        yield (obj["id"], len(faces), obj.get("name", ""), obj.get("type_line", ""),
               obj.get("oracle_text", ""), obj["flavor_text"], obj.get("flavor_name", ""))


def build(source: Path, destination: Path) -> dict:
    if not source.is_file():
        raise FileNotFoundError(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix="printing-lore-", suffix=".sqlite3", dir=destination.parent)
    os.close(fd)
    conn = None
    count = 0
    try:
        conn = sqlite3.connect(temp)
        conn.executescript(SCHEMA)
        conn.execute("PRAGMA synchronous=OFF")
        insert_p = "INSERT OR REPLACE INTO printings VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        insert_f = "INSERT OR REPLACE INTO faces VALUES (?,?,?,?,?,?,?)"
        for c in source_rows(source):
            if not c.get("id") or not c.get("set") or not c.get("collector_number"):
                raise ValueError(f"Incomplete printing identity at source record {count + 1}")
            row = (c["id"], c.get("oracle_id") or (c.get("card_faces") or [{}])[0].get("oracle_id"),
                   c.get("name", ""), c["set"].lower(), c.get("set_name", ""), c["collector_number"],
                   c.get("released_at"), c.get("lang", "en"), c.get("layout"), c.get("set_type"),
                   int("paper" in c.get("games", [])), int(bool(c.get("digital"))),
                   int(bool(c.get("promo"))), int(bool(c.get("story_spotlight"))), c.get("scryfall_uri"))
            conn.execute(insert_p, row)
            conn.executemany(insert_f, card_faces(c))
            count += 1
            if count % 10000 == 0:
                conn.commit()
        conn.execute("CREATE VIRTUAL TABLE flavor_fts USING fts5(flavor_text, content='faces', content_rowid='rowid')")
        conn.execute("INSERT INTO flavor_fts(flavor_fts) VALUES ('rebuild')")
        sha = hashlib.sha256()
        with source.open("rb") as fh:
            for block in iter(lambda: fh.read(1024 * 1024), b""):
                sha.update(block)
        meta = {"schema": "1", "built_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                "source": source.name, "source_sha256": sha.hexdigest(), "printings": str(count),
                "authority": "Scryfall default-cards printing data (local snapshot)"}
        conn.executemany("INSERT INTO meta VALUES (?,?)", meta.items())
        conn.commit()
        conn.close()
        conn = None
        os.replace(temp, destination)
        return meta
    finally:
        if conn is not None:
            conn.close()
        if os.path.exists(temp):
            os.unlink(temp)


def filters(args, alias="p"):
    clauses, vals = [], []
    if not args.all_languages:
        clauses.append(f"{alias}.lang = 'en'")
    if not args.include_digital:
        clauses.append(f"{alias}.paper = 1")
    if getattr(args, "set_code", None):
        clauses.append(f"{alias}.set_code = ?")
        vals.append(args.set_code.lower())
    return (" AND ".join(clauses) or "1=1"), vals


def query(conn: sqlite3.Connection, args) -> dict:
    meta = dict(conn.execute("SELECT key, value FROM meta"))
    where, vals = filters(args)
    limit = "" if args.all else " LIMIT ?"
    if not args.all:
        vals.append(args.limit)
    if args.action == "stats":
        rows = conn.execute(f"SELECT COUNT(*) AS printings, COUNT(DISTINCT set_code) AS sets, "
                            f"COUNT(DISTINCT COALESCE(oracle_id, name)) AS oracle_cards FROM printings p WHERE {where}",
                            vals[:len(vals) - (0 if args.all else 1)]).fetchone()
        result = {"counts": dict(rows)}
    elif args.action == "set":
        counts = conn.execute(f"SELECT COUNT(*) AS printings, COUNT(DISTINCT name) AS distinct_names, "
                              f"COUNT(DISTINCT COALESCE(oracle_id, name)) AS oracle_cards "
                              f"FROM printings p WHERE {where}", vals[:len(vals) - (0 if args.all else 1)]).fetchone()
        rows = conn.execute(f"SELECT p.* FROM printings p WHERE {where} "
                            f"ORDER BY CAST(p.collector_number AS INTEGER), p.collector_number, p.lang{limit}", vals)
        result = {"set_code": args.set_code.lower(), "counts": dict(counts), "items": [dict(r) for r in rows]}
    elif args.action == "card":
        pred = "(p.name = ? COLLATE NOCASE OR EXISTS "
        pred += "(SELECT 1 FROM faces f WHERE f.printing_id = p.id AND f.name = ? COLLATE NOCASE))"
        terms = vals[:len(vals) - (0 if args.all else 1)] + [args.name, args.name]
        if not args.all:
            terms.append(args.limit)
        rows = conn.execute(f"SELECT p.* FROM printings p WHERE {where} AND {pred} "
                            f"ORDER BY p.released_at, p.set_code, p.collector_number{limit}", terms)
        result = {"card": args.name, "items": [with_faces(conn, dict(r)) for r in rows]}
    elif args.action == "flavor":
        # FTS5 phrase matching is indexed and treats punctuation as word separators.
        phrase = '"' + args.phrase.replace('"', '""') + '"'
        params = [phrase] + vals
        rows = conn.execute(f"SELECT p.*, f.face_number, f.name AS face_name, f.flavor_text "
                            f"FROM flavor_fts JOIN faces f ON flavor_fts.rowid = f.rowid "
                            f"JOIN printings p ON p.id = f.printing_id "
                            f"WHERE flavor_fts MATCH ? AND {where} "
                            f"ORDER BY p.released_at, p.set_code, p.collector_number{limit}", params)
        result = {"flavor_phrase": args.phrase, "items": [dict(r) for r in rows]}
    elif args.action == "saga":
        rows = conn.execute(f"SELECT DISTINCT p.* FROM printings p JOIN faces f ON f.printing_id=p.id "
                            f"WHERE {where} AND f.type_line LIKE '%Saga%' "
                            f"ORDER BY p.released_at, p.set_code, p.collector_number{limit}", vals)
        result = {"items": [with_faces(conn, dict(r)) for r in rows]}
    else:
        raise ValueError(args.action)
    return {"snapshot": meta, "filters": {"english_only": not args.all_languages,
                                          "paper_only": not args.include_digital}, **result}


def with_faces(conn, printing):
    printing["faces"] = [dict(r) for r in conn.execute(
        "SELECT face_number, name, type_line, oracle_text, flavor_text, flavor_name FROM faces "
        "WHERE printing_id=? ORDER BY face_number", (printing["id"],))]
    return printing


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="SQLite index path")
    sub = parser.add_subparsers(dest="action", required=True)
    build_p = sub.add_parser("build", help="build from existing Scryfall JSONL cache")
    build_p.add_argument("--source", type=Path, help="explicit .jsonl/.jsonl.gz input for reproducibility")
    for action in ("stats", "set", "card", "flavor", "saga"):
        p = sub.add_parser(action)
        if action == "set":
            p.add_argument("set_code", help="Scryfall set code, e.g. lea = Alpha")
        if action == "card":
            p.add_argument("name")
        if action == "flavor":
            p.add_argument("phrase", help="exact sequence of words in printing flavor")
        if action in ("stats", "card", "flavor", "saga"):
            p.add_argument("--set", dest="set_code", help="limit to a Scryfall set code")
        p.add_argument("--all", action="store_true", help="do not limit result count")
        p.add_argument("--limit", type=int, default=30)
        p.add_argument("--all-languages", action="store_true")
        p.add_argument("--include-digital", action="store_true")
        p.add_argument("--json", action="store_true", help="compact machine-readable output")
    args = parser.parse_args(argv)
    try:
        if args.action == "build":
            result = build(args.source or latest_source(), args.db)
        else:
            if not args.db.is_file():
                raise FileNotFoundError(f"Index missing: {args.db}; run the build command first")
            conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
            conn.row_factory = sqlite3.Row
            result = query(conn, args)
            conn.close()
        print(json.dumps(result, ensure_ascii=False, indent=None if getattr(args, "json", False) else 2))
    except (OSError, ValueError, sqlite3.Error) as exc:
        print(f"printing_lore_index: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
