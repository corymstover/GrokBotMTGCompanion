#!/usr/bin/env python3
"""Cache official Wizards pages that claim packs cite but the story cache lacks (Batch 14).

Reads every claim pack in data/multiverse_graph/manifest.json, collects source_register URLs on official
Wizards hosts, and fetches any whose slug is not already in .cache/story/{text22,extra,articles} into the
gitignored .cache/story/sources/<slug>.txt (same text format as scripts/fetch_story_pages.py).
Full page text is never committed. A metadata-only provenance record (URL, status, title, date, word count,
sha256 of the cached text) is written to data/lore_research/pack_source_cache_provenance_2026-10-30.json.

  python3 scripts/fetch_pack_source_pages.py [--only SUBSTRING] [--delay 1.0] [--provenance-only]
"""
import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_story_pages import extract, get  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
STORY = ROOT / ".cache" / "story"
SOURCES = STORY / "sources"
OUT = ROOT / "data" / "lore_research" / "pack_source_cache_provenance_2026-10-30.json"
OFFICIAL = ("https://magic.wizards.com/", "https://media.wizards.com/", "https://www.wizards.com/", "https://company.wizards.com/")


def slug(url: str) -> str:
    return url.rstrip("/").split("/")[-1]


def cited_urls() -> dict:
    out = {}
    for rel in json.loads((ROOT / "data/multiverse_graph/manifest.json").read_text())["claim_packs"]:
        p = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        sr = p.get("source_register") or {}
        items = sr.items() if isinstance(sr, dict) else [(x.get("id") or x.get("source_id"), x) for x in sr]
        for sid, meta in items:
            url = meta.get("url") if isinstance(meta, dict) else None
            if url and url.startswith(OFFICIAL):
                out.setdefault(url, set()).add(f"{Path(rel).name}:{sid}")
    return out


def cached_elsewhere(s: str) -> bool:
    return any((STORY / d / f"{s}.txt").exists() for d in ("text22", "extra", "articles"))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--delay", type=float, default=1.0)
    ap.add_argument("--provenance-only", action="store_true")
    a = ap.parse_args(argv)
    SOURCES.mkdir(parents=True, exist_ok=True)
    rows = []
    for url, cites in sorted(cited_urls().items()):
        s = slug(url)
        if cached_elsewhere(s):
            continue
        f = SOURCES / f"{s}.txt"
        status = "CACHED"
        if not f.exists() and not a.provenance_only and a.only in url:
            html = get(url)
            time.sleep(a.delay)
            if html:
                f.write_text(extract(url, html), encoding="utf-8")
            else:
                status = "FETCH_FAILED"
        if not f.exists():
            rows.append({"url": url, "slug": s, "status": status if status != "CACHED" else "NOT_CACHED",
                         "cited_by": sorted(cites)})
            continue
        txt = f.read_text(encoding="utf-8")
        head = dict(line.split(": ", 1) for line in txt.split("\n\n", 1)[0].splitlines() if ": " in line)
        body = txt.split("\n\n", 1)[1] if "\n\n" in txt else ""
        rows.append({"url": url, "slug": s, "status": "CACHED" if len(body.split()) >= 50 else "CACHED_THIN",
                     "title": head.get("TITLE", ""), "date": head.get("DATE", ""), "words": len(body.split()),
                     "text_sha256": hashlib.sha256(txt.encode()).hexdigest(), "cited_by": sorted(cites)})
    doc = {"schema": "pack-source-cache-provenance/v1", "cache_dir": ".cache/story/sources (gitignored)",
           "meaning": "Metadata only; no page text is committed. Lists official pages cited by claim packs that were "
                      "missing from the main story cache.", "pages": rows}
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for r in rows:
        print(r["status"], r.get("words", ""), r["url"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
