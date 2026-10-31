#!/usr/bin/env python3
"""Audit recovery of all 660 official Wizards source extracts without rehosting text.

Recover with scripts/fetch_story_pages.py; then run this file to write a small
metadata-only drift report. The original 2026-10-29 audit is immutable evidence,
not a guarantee that source HTML or extracted wording will never change.
The portable --check verifies the stored inventory/provenance; with a fully
available local cache it also recomputes every URL, word threshold and hash.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import story_cache_audit as A  # noqa: E402

ORIGINAL = ROOT / "data/story_cache_provenance_2026-10-29.json"
OUT = ROOT / "data/story_cache_recovery_2026-10-31.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def base() -> tuple[dict, dict]:
    historical = json.loads(ORIGINAL.read_text(encoding="utf-8"))
    inventory = A.inventory()
    key = lambda x: (x["kind"], x["url"])
    saved = {key(x): x for x in historical["records"]}
    if historical["total"] != 660 or len(saved) != 660 or len(inventory) != 660:
        raise ValueError("660-record original inventory or source metadata is incomplete")
    if set(map(key, inventory)) != set(saved) or historical["colliding_cache_paths"]:
        raise ValueError("official source URL inventory changed; re-review rather than silently replacing it")
    if any(x["status"] != "present" for x in saved.values()):
        raise ValueError("historical baseline was not strictly complete")
    return saved, {"original_sha256": sha(ORIGINAL), "inventory_total": len(inventory)}


def full_replay() -> dict:
    saved, prior = base()
    live = A.audit(A.inventory())
    if live["total"] != 660 or live["colliding_cache_paths"] or live["counts"] != {"present": 660}:
        raise ValueError(f"660-page source recovery incomplete: {live['counts']}")
    exact, changed = 0, []
    for x in live["records"]:
        old = saved[(x["kind"], x["url"])]
        if x["sha256"] == old["sha256"]:
            exact += 1
        else:
            changed.append({"kind": x["kind"], "url": x["url"], "old_sha256": old["sha256"],
                            "new_sha256": x["sha256"], "old_words": old["words"],
                            "new_words": x["words"], "old_title": old["title"],
                            "new_title": x["title"], "status": "EXTRACT_DRIFT_REVIEW_ONLY"})
    counts = Counter(r["kind"] for r in live["records"])
    return {"schema": "story-cache-provenance-replay/v1", "as_of": "2026-10-31",
            "original_metadata_sha256": prior["original_sha256"],
            "source_inventory": "data/primary_sources.csv + data/story_extra_sources.csv + fetch_story_pages.py ARTICLES",
            "total": 660, "strictly_present": 660, "exact_original_extraction_hashes": exact,
            "source_extract_drift": len(changed), "kind_totals": dict(sorted(counts.items())),
            "drift_review_queue": changed,
            "source_text_embedded": False,
            "result": "STRICT_SOURCE_URL_AND_LENGTH_AUDIT_PASSED; changed cached extracts require independent review",
            "limits": ["A matching extract hash is not proof that an article covers all relevant canon.",
                       "A changed extract is not automatically a lore correction or a new canon claim.",
                       "Article contents are copyrighted and remain outside Git; only metadata are committed."]}


def portable_check() -> dict:
    saved, orig = base()
    doc = json.loads(OUT.read_text(encoding="utf-8"))
    if doc["schema"] != "story-cache-provenance-replay/v1" or doc["total"] != 660 or \
       doc["strictly_present"] != 660 or doc["source_text_embedded"] is not False or \
       doc["original_metadata_sha256"] != orig["original_sha256"] or \
       doc["exact_original_extraction_hashes"] + doc["source_extract_drift"] != 660 or \
       doc["source_extract_drift"] != len(doc["drift_review_queue"]):
        raise ValueError("story recovery evidence report inconsistent with original inventory")
    if sum(doc["kind_totals"].values()) != 660 or any(v < 0 for v in doc["kind_totals"].values()):
        raise ValueError("story source kind totals inconsistent")
    if doc["source_inventory"] != "data/primary_sources.csv + data/story_extra_sources.csv + fetch_story_pages.py ARTICLES":
        raise ValueError("unexpected story source inventory provenance")
    seen = set()
    for row in doc["drift_review_queue"]:
        key = (row["kind"], row["url"])
        previous = saved.get(key)
        if key in seen or previous is None or row["old_sha256"] != previous["sha256"] or \
           row["old_words"] != previous["words"] or row["old_title"] != previous["title"] or \
           row["old_sha256"] == row["new_sha256"] or \
           not re.fullmatch(r"[0-9a-f]{64}", row["new_sha256"]) or \
           row["status"] != "EXTRACT_DRIFT_REVIEW_ONLY":
            raise ValueError("unverifiable or non-Wizards extract drift row")
        seen.add(key)
    return doc


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true")
    args = p.parse_args()
    if args.check:
        old = portable_check()
        # Rebuild fully only when the entire uncommitted cache is available.
        current = A.audit(A.inventory())
        if current["counts"] == {"present": 660} and full_replay() != old:
            raise ValueError("local source-cache drift differs from saved report")
        doc = old
    else:
        doc = full_replay()
        OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("PASS official source cache", doc["strictly_present"], "pages; exact cached hashes",
          doc["exact_original_extraction_hashes"], "drift for review", doc["source_extract_drift"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
