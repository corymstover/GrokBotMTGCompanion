#!/usr/bin/env python3
"""Story-art caption atlas: which printed cards' art appears, captioned, in official story pages.

Official magic.wizards.com story pages caption embedded card art as ``<Card Name> | Art by
<Artist>``. For every cached page listed in data/primary_sources.csv, this finds each caption
and keeps it only when both checks pass:

1. Card: the text before ``| Art by`` ends with an exact card name (front face, or a face
   name) from the manifest-verified Scryfall default-cards snapshot. The longest match wins.
2. Artist: the text after ``| Art by`` starts with an artist credited on some printing of
   that card in the same snapshot.

A kept caption means the official page shows that card's art. It is card and story
**navigation**, not a canon claim that the art depicts that scene. Pack A4-style exact
scene matches need visual review and stay separate.

    python3 scripts/build_story_art_captions.py          # needs .cache/story + .cache/multiverse
    python3 scripts/build_story_art_captions.py --check  # CI: self-hash and schema if caches absent
"""
from __future__ import annotations

import argparse
import csv
import glob
import gzip
import hashlib
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/story_atlas/story_art_captions_2026-10-30.json"
PRIMARY = ROOT / "data/primary_sources.csv"
STORY = ROOT / ".cache/story"
CACHE = Path(os.environ.get("MTG_MULTIVERSE_CACHE", ROOT / ".cache/multiverse"))
SNAPSHOT = "snap-20261029-40848334824-1"
DIRS = {"story": "text22", "article": "articles", "extra": "extra"}
CAP = re.compile(r"\|\s*Art by\s+")
OFFICIAL = re.compile(r"^https://magic\.wizards\.com/")


def norm(s: str) -> str:
    s = re.sub(r"\[/?autocard\]", "", s.replace("\u2019", "'"))
    return re.sub(r"\s+", " ", s).strip()


def fold(s: str) -> str:
    """Diacritic-insensitive form used only for the artist comparison (e.g. Ba\u01f5a == Baga)."""
    return "".join(ch for ch in unicodedata.normalize("NFKD", s) if not unicodedata.combining(ch))


def load_index():
    files = sorted(glob.glob(str(CACHE / "default-cards-*.jsonl.gz")))
    if not files:
        raise FileNotFoundError("default-cards snapshot missing from " + str(CACHE))
    names: dict[str, dict] = {}
    for line in gzip.open(files[0], "rt", encoding="utf-8"):
        c = json.loads(line)
        if c.get("layout") in {"token", "double_faced_token", "emblem", "art_series"}:
            continue
        faces = c.get("card_faces") or []
        keys = {norm(c["name"].split(" // ")[0])} | {norm(f.get("name", "")) for f in faces if f.get("name")}
        artists = {norm(a) for a in [c.get("artist", "")] + [f.get("artist", "") for f in faces] if a}
        for part in list(artists):
            artists |= {norm(x) for x in re.split(r"\s*&\s*", part)}
        for k in keys:
            e = names.setdefault(k, {"name": c["name"], "oracle_id": c.get("oracle_id"), "artists": set()})
            e["artists"] |= artists
    return names, Path(files[0]).name


def page_jobs():
    for r in csv.DictReader(PRIMARY.open(encoding="utf-8")):
        if r["kind"] in DIRS and OFFICIAL.match(r["url"]):
            yield r, STORY / DIRS[r["kind"]] / (r["url"].rstrip("/").split("/")[-1] + ".txt")


def scan(text: str, names: dict, maxlen: int, rejected: dict | None = None) -> list[dict]:
    out = []
    rejected = rejected if rejected is not None else {}
    for m in CAP.finditer(text):
        before = text[max(0, m.start() - 120):m.start()].rstrip()
        words = before.split(" ")
        hit = None
        for k in range(min(len(words), maxlen), 0, -1):
            cand = " ".join(words[-k:]).lstrip("\"“(")
            if cand in names:
                hit = cand
                break
        if not hit:
            rejected["no_exact_card_name"] = rejected.get("no_exact_card_name", 0) + 1
            continue
        after = fold(text[m.end():m.end() + 80])
        art = next((a for a in sorted(names[hit]["artists"], key=len, reverse=True) if after.startswith(fold(a))), None)
        if not art:
            rejected["artist_not_credited_in_snapshot"] = rejected.get("artist_not_credited_in_snapshot", 0) + 1
            continue
        out.append({"card": names[hit]["name"], "oracle_id": names[hit]["oracle_id"], "caption_name": hit, "artist": art})
    return out


def build() -> dict:
    names, snap_file = load_index()
    maxlen = max(len(k.split(" ")) for k in names)
    pages, missing, rejected = [], 0, {}
    for r, path in page_jobs():
        if not path.exists():
            missing += 1
            continue
        caps = scan(norm(path.read_text(encoding="utf-8")), names, maxlen, rejected)
        seen, uniq = set(), []
        for c in caps:
            key = (c["oracle_id"], c["artist"])
            if key not in seen:
                seen.add(key)
                uniq.append(c)
        if uniq:
            pages.append({"url": r["url"], "title": r["title"], "date": r["date"], "kind": r["kind"], "captions": uniq})
    pages.sort(key=lambda p: (p["date"], p["url"]))
    cards = {c["oracle_id"] for p in pages for c in p["captions"]}
    out = {
        "schema": "story-art-captions/v1",
        "tier": "ART_CAPTIONED_IN_OFFICIAL_STORY",
        "meaning": "The official Wizards page displays this card's art with a '<card> | Art by <artist>' caption. Navigation only: not a claim that the art depicts the scene.",
        "card_data_source": {"provider": "Scryfall", "snapshot": SNAPSHOT, "file": snap_file},
        "story_source": "Cached official magic.wizards.com pages inventoried in data/primary_sources.csv",
        "pages_scanned_missing": missing,
        "pages_with_captions": len(pages),
        "captions": sum(len(p["captions"]) for p in pages),
        "distinct_cards": len(cards),
        "rejected_captions": dict(sorted(rejected.items())),
        "rejection_note": "Captions are dropped (not guessed) when the card name is not exact or the credited artist does not match the snapshot, e.g. typos such as 'Michael Kormarck'.",
        "pages": pages,
    }
    out["content_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    return out


def self_hash_ok(d: dict) -> bool:
    body = {k: v for k, v in d.items() if k != "content_sha256"}
    return hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest() == d.get("content_sha256")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    caches = bool(glob.glob(str(CACHE / "default-cards-*.jsonl.gz"))) and (STORY / "text22").is_dir()
    if a.check:
        old = json.loads(OUT.read_text(encoding="utf-8"))
        if not self_hash_ok(old) or old.get("schema") != "story-art-captions/v1":
            print("FAIL: story art captions self-hash or schema mismatch"); return 1
        if any(not OFFICIAL.match(p["url"]) for p in old["pages"]):
            print("FAIL: non-Wizards page in atlas"); return 1
        if not caches:
            print(f"OK (caches absent: self-hash verified): {old['captions']} captions, {old['distinct_cards']} cards, {old['pages_with_captions']} pages")
            return 0
        if build() != old:
            print("FAIL: story art captions are stale; rerun scripts/build_story_art_captions.py"); return 1
        print(f"OK (rebuilt from caches): {old['captions']} captions, {old['distinct_cards']} cards, {old['pages_with_captions']} pages")
        return 0
    if not caches:
        print("caches missing (.cache/story and the Scryfall default-cards snapshot)", file=sys.stderr); return 2
    out = build()
    if out["pages_scanned_missing"]:
        print(f"note: {out['pages_scanned_missing']} inventoried pages not cached", file=sys.stderr)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {out['captions']} captions, {out['distinct_cards']} cards, {out['pages_with_captions']} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
