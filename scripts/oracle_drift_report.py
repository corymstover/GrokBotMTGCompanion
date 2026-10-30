#!/usr/bin/env python3
"""Phase 1 card database: Oracle drift between committed card shards and a verified Scryfall snapshot.

Read-only. Compares, for every oracle_id in data/card_index.csv:
  * the Oracle text rendered in cards/**.md (flavor lines excluded) against the snapshot's oracle_text
  * index fields (name, type_line, color_identity, commander legality, game_changer) against the snapshot
and lists oracle_ids present only in the snapshot (new cards) or only in the index (removed / merged).

It edits no shard, enrichment, lore, deck, approval or Grixis file. The output is a bounded evidence report
used to plan a guarded shard refresh; it is not itself a refresh.

  python3 scripts/oracle_drift_report.py --oracle /path/oracle-cards-*.jsonl.gz [--out data/card_db/oracle_drift_<date>.json]
"""
from __future__ import annotations

import argparse
import csv
import gzip
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = 60
GC_FIELD = "game_changer"


def norm(text: str) -> str:
    text = unicodedata.normalize("NFC", text or "")
    text = text.replace("\u2014", "-").replace("\u2212", "-").replace("\u2019", "'")
    return re.sub(r"\s+", " ", text).strip()


NON_GAMEPLAY = {"art_series", "token", "double_faced_token", "emblem", "planar", "scheme", "vanguard", "front_card"}


def ci_set(code: str) -> set:
    return set(code) - {"C"}


def shard_texts(root: Path) -> dict[str, str]:
    """oracle_id -> Oracle text as rendered in the shards (all faces, flavor removed)."""
    out = {}
    for md in sorted((root / "cards").rglob("*.md")):
        for sec in re.split(r"^### ", md.read_text(encoding="utf-8"), flags=re.M)[1:]:
            oid = re.search(r"oracle_id `([0-9a-f-]{36})`", sec)
            if not oid:
                continue
            body = sec.split("- **Keywords", 1)[0].split("- **Commander notes", 1)[0]
            lines = []
            for l in re.findall(r"^\s+> (.*)$", body, re.M):
                if l.startswith("*"):
                    continue  # flavor text
                lines.append(l)
            out[oid.group(1)] = "\n".join(lines)
    return out


def snap_text(card: dict) -> str:
    if card.get("oracle_text") is not None and not card.get("card_faces"):
        return card["oracle_text"]
    faces = card.get("card_faces") or []
    return "\n".join(f.get("oracle_text", "") for f in faces if f.get("oracle_text"))


def snapshot_date(path: Path) -> str | None:
    m = re.search(r"(\d{4})(\d{2})(\d{2})\d{6}", path.name)
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else None


def report(oracle_path: Path, root: Path = ROOT) -> dict:
    with (root / "data/card_index.csv").open(encoding="utf-8", newline="") as fh:
        index = {r["oracle_id"]: r for r in csv.DictReader(fh)}
    shards = shard_texts(root)
    snap = {}
    with gzip.open(oracle_path, "rt", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                c = json.loads(line)
                if c.get("oracle_id"):
                    snap[c["oracle_id"]] = c
    changes = {k: [] for k in ("oracle_text", "name", "type_line", "color_identity", "commander_legality", GC_FIELD)}
    unparsed = []
    for oid, row in index.items():
        c = snap.get(oid)
        if not c:
            continue
        if oid in shards:
            if norm(shards[oid]) != norm(snap_text(c)):
                changes["oracle_text"].append(row["name"])
        else:
            unparsed.append(row["name"])
        if re.sub(r" \([A-Z0-9]+ #[^)]+\)$", "", row["name"]) != c["name"]:  # index disambiguates duplicate names
            changes["name"].append(f"{row['name']} -> {c['name']}")
        if norm(row["type_line"]) != norm(c.get("type_line", "")):
            changes["type_line"].append(row["name"])
        if ci_set(row["color_identity"]) != set(c.get("color_identity") or []):
            changes["color_identity"].append(row["name"])
        if row["commander_legality"] != c.get("legalities", {}).get("commander"):
            changes["commander_legality"].append(f"{row['name']}: {row['commander_legality']} -> {c.get('legalities', {}).get('commander')}")
        if (row[GC_FIELD] == "1") != bool(c.get(GC_FIELD)):
            changes[GC_FIELD].append(f"{row['name']}: {row[GC_FIELD]} -> {int(bool(c.get(GC_FIELD)))}")
    new = sorted((c["name"] for oid, c in snap.items() if oid not in index), key=str.casefold)
    gone = sorted((r["name"] for oid, r in index.items() if oid not in snap), key=str.casefold)
    new_ids = [oid for oid in snap if oid not in index]
    new_layouts = Counter(snap[oid].get("layout") for oid in new_ids)
    paper = [snap[o] for o in new_ids if not snap[o].get("digital") and snap[o].get("layout") not in NON_GAMEPLAY]
    paper_sets = Counter(f"{c.get('set')} ({c.get('set_type')}, {c.get('released_at')})" for c in paper)
    digital = sum(1 for o in new_ids if snap[o].get("digital"))
    return {
        "schema": "oracle-drift-report/v1",
        "status": "READ_ONLY_EVIDENCE (no shards refreshed)",
        "snapshot_file": oracle_path.name,
        "index_rows": len(index), "snapshot_oracle_ids": len(snap), "shard_sections_parsed": len(shards),
        "counts": {k: len(v) for k, v in changes.items()} | {"new_in_snapshot": len(new), "missing_from_snapshot": len(gone),
                                                             "shard_text_unparsed": len(unparsed)},
        "new_in_snapshot_layouts": dict(new_layouts.most_common()),
        "new_in_snapshot_breakdown": {"paper_gameplay": len(paper), "digital_only": digital,
                                      "non_gameplay_layouts": len(new_ids) - len(paper) - digital},
        "new_paper_gameplay_by_set": dict(paper_sets.most_common(40)),
        "new_paper_gameplay_sample": sorted((c["name"] for c in paper), key=str.casefold)[:SAMPLE],
        "snapshot_date": snapshot_date(oracle_path),
        "changed": changes,  # complete lists: the companion trusts a card only if it is absent from all of them
        "samples": {"new_in_snapshot": new[:SAMPLE],
                                                                 "missing_from_snapshot": gone[:SAMPLE],
                                                                 "shard_text_unparsed": unparsed[:SAMPLE]},
        "limitations": [
            "Text comparison normalizes whitespace, dashes and apostrophes; reminder-text or formatting-only edits still count as changes.",
            "Index fields are compared as stored in data/card_index.csv (2026-10-15 build); prices and EDHREC ranks are not compared.",
            "A change listed here is a refresh candidate, not proof of an errata announcement.",
        ],
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--oracle", required=True, type=Path)
    p.add_argument("--out", type=Path)
    a = p.parse_args(argv)
    r = report(a.oracle)
    txt = json.dumps(r, indent=1, ensure_ascii=False) + "\n"
    if a.out:
        a.out.write_text(txt, encoding="utf-8")
    print(json.dumps(r["counts"], indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
