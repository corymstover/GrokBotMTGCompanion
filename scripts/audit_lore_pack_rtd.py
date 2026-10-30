#!/usr/bin/env python3
"""Audit Pack C2 (Return to Dominaria episode extraction) against the official story cache.

What it checks:
- Schema: every claim has a known grade, a registered source, and at least one evidence
  quote. Every evidence source_id is one of the claim's source_ids.
- Sources: every registered source is an official magic.wizards.com Return to Dominaria
  episode listed in data/primary_sources.csv.
- Quotes: when the gitignored cache .cache/story/text22/<slug>.txt is present, every quote must
  be a verbatim substring of its episode text (whitespace is normalized, nothing else).
  The audit records each quote's sha256, so a cache-less ``--check`` can still confirm that
  the pack's quotes are the ones that were verified.

Writes data/lore_research/pack_c2_return_to_dominaria_audit_2026-10-30.json (deterministic,
self-hashed). ``--check`` re-runs the audit and fails on any difference. Without the cache,
it verifies the self-hash and quote hashes only.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "data/lore_research/pack_c2_return_to_dominaria_2026-10-30.json"
OUT = ROOT / "data/lore_research/pack_c2_return_to_dominaria_audit_2026-10-30.json"
CACHE = ROOT / ".cache/story/text22"
PRIMARY = ROOT / "data/primary_sources.csv"
GRADES = {"CANON_CONFIRMED", "CANON_IMPLIED", "CANON_DISPUTED", "OPEN_QUESTION", "ALTERNATE_CONTINUITY"}
URL_RE = re.compile(r"^https://magic\.wizards\.com/en/news/magic-story/return-dominaria-episode-\d+-\d{4}-\d{2}-\d{2}$")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def audit(pack: dict, cache: Path = CACHE) -> dict:
    problems: list[str] = []
    primary_urls = {r["url"] for r in csv.DictReader(PRIMARY.open(encoding="utf-8"))}
    reg = pack["source_register"]
    for sid, meta in sorted(reg.items()):
        if not URL_RE.match(meta.get("url", "")):
            problems.append(f"{sid}: not an official Return to Dominaria episode URL")
        if meta.get("url") not in primary_urls:
            problems.append(f"{sid}: URL missing from data/primary_sources.csv")
    ents = {e["id"] for e in pack["entities"]}
    texts: dict[str, str | None] = {}
    for sid, meta in reg.items():
        f = cache / (meta["url"].rstrip("/").split("/")[-1] + ".txt")
        texts[sid] = norm(f.read_text(encoding="utf-8")) if f.exists() else None
    cache_present = all(v is not None for v in texts.values())
    rows = []
    for c in pack["claims"]:
        if c["grade"] not in GRADES:
            problems.append(f"{c['id']}: unknown grade {c['grade']}")
        if c["subject"] not in ents:
            problems.append(f"{c['id']}: subject {c['subject']} is not a declared entity")
        if not c.get("evidence"):
            problems.append(f"{c['id']}: no evidence quotes")
        for sid in c["source_ids"]:
            if sid not in reg:
                problems.append(f"{c['id']}: unregistered source {sid}")
        for ev in c.get("evidence", []):
            if ev["source_id"] not in c["source_ids"]:
                problems.append(f"{c['id']}: evidence source {ev['source_id']} not in source_ids")
            q = norm(ev["quote"])
            status = "NOT_CHECKED_CACHE_ABSENT"
            text = texts.get(ev["source_id"])
            if text is not None:
                status = "VERBATIM" if q in text else "NOT_FOUND"
                if status == "NOT_FOUND":
                    problems.append(f"{c['id']}: quote not found verbatim in {ev['source_id']}: {q[:60]}")
            rows.append({"claim": c["id"], "source_id": ev["source_id"], "quote_sha256": sha(q), "status": status})
    grades: dict[str, int] = {}
    for c in pack["claims"]:
        grades[c["grade"]] = grades.get(c["grade"], 0) + 1
    out = {
        "schema": "pack-c2-rtd-audit/v1",
        "pack": str(PACK.relative_to(ROOT)),
        "pack_status": pack["status"],
        "claims": len(pack["claims"]),
        "entities": len(pack["entities"]),
        "sources": len(reg),
        "grades": dict(sorted(grades.items())),
        "quotes": len(rows),
        "quotes_verbatim": sum(r["status"] == "VERBATIM" for r in rows),
        "quote_rows": rows,
        "problems": problems,
        "note": "Verbatim-quote audit against the cached official episode text. This is research evidence, not owner approval or certification.",
    }
    out["content_sha256"] = sha(json.dumps(out, sort_keys=True, ensure_ascii=False))
    return out, cache_present


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    pack = json.loads(PACK.read_text(encoding="utf-8"))
    new, cache_present = audit(pack)
    if a.check:
        old = json.loads(OUT.read_text(encoding="utf-8"))
        body = {k: v for k, v in old.items() if k != "content_sha256"}
        if sha(json.dumps(body, sort_keys=True, ensure_ascii=False)) != old.get("content_sha256"):
            print("audit self-hash mismatch"); return 1
        if old["problems"]:
            print("committed audit lists problems"); return 1
        if old["quotes_verbatim"] != old["quotes"]:
            print("committed audit has unverified quotes"); return 1
        old_hashes = [(r["claim"], r["source_id"], r["quote_sha256"]) for r in old["quote_rows"]]
        new_hashes = [(r["claim"], r["source_id"], r["quote_sha256"]) for r in new["quote_rows"]]
        if old_hashes != new_hashes:
            print("pack quotes differ from the audited quotes; rerun the audit with the cache"); return 1
        if new["problems"] and cache_present:
            print("\n".join(new["problems"])); return 1
        schema_problems = [p for p in new["problems"] if "quote not found" not in p]
        if schema_problems:
            print("\n".join(schema_problems)); return 1
        if cache_present and new != old:
            print("audit differs from the cache-backed rerun"); return 1
        print(f"OK: {old['claims']} claims, {old['quotes_verbatim']}/{old['quotes']} quotes verbatim "
              f"({'re-verified against cache' if cache_present else 'cache absent: hashes verified'})")
        return 0
    if not cache_present:
        print("story cache missing; run scripts/fetch_story_pages.py first", file=sys.stderr); return 2
    OUT.write_text(json.dumps(new, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {new['claims']} claims, {new['quotes_verbatim']}/{new['quotes']} verbatim, problems={len(new['problems'])}")
    for p in new["problems"]:
        print(" -", p)
    return 1 if new["problems"] else 0


if __name__ == "__main__":
    sys.exit(main())
