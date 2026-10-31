#!/usr/bin/env python3
"""Fail-closed, read-only audit of all tentative card/name and art matches.

Replays the pinned Oct 30 Default Cards printing metadata and the 660-page
official Wizards cache. Candidate discoveries stay review-only: this tool
never writes card enrichment, claim packs, art tiers or approved decks.

  python3 scripts/audit_unresolved_lore_links.py --bulk /tmp/.../default-cards-*.jsonl.gz
  python3 scripts/audit_unresolved_lore_links.py --check
  python3 scripts/audit_unresolved_lore_links.py --check --bulk /tmp/.../default-cards-*.jsonl.gz
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from collections import Counter
from pathlib import Path

import build_card_enrichment as B
import story_cache_audit as S

ROOT = Path(__file__).resolve().parents[1]
ENRICHMENT = ROOT / "data/card_enrichment.json"
ART = ROOT / "data/lore_research/story_image_label_printings_2026-10-30.json"
STORY = ROOT / "data/story_cache_recovery_2026-10-31.json"
SNAP = ROOT / "data/scryfall_snapshots/snap-20261030-live-20261031.manifest.json"
OUT = ROOT / "data/lore_research/unresolved_printing_name_match_audit_2026-10-31.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pending() -> list[dict]:
    cards = json.loads(ENRICHMENT.read_text(encoding="utf-8"))["cards"]
    return sorted(({"oracle_id": oid, "card": c["name"], "entry": link["entry"],
                    "character": link["name"]}
                   for oid, c in cards.items() for link in c["lore"]["relations"]
                   if link["relation"] == "name-match"),
                  key=lambda r: (r["oracle_id"], r["entry"]))


def art_unresolved() -> list[dict]:
    images = json.loads(ART.read_text(encoding="utf-8"))
    counts = Counter(row["status"] for row in images["labels"])
    if dict(counts) != {k: v for k, v in images["counts"].items() if v}:
        raise ValueError("Wizards art-label statuses no longer agree with their source inventory")
    return [{"source_url": r["url"], "official_label": r["label"],
             "caption_name": r["caption_name"], "status": r["status"],
             "printing_name": (r.get("printing") or {}).get("name"),
             "reason": "CAPTION_PRINTING_NAME_DISAGREES" if r["status"] == "NAME_MISMATCH"
                       else "NO_EXACT_SET_COLLECTOR_PRINTING"}
            for r in images["labels"] if r["status"] != "MATCHED"]


def inputs() -> dict:
    meta = json.loads(SNAP.read_text(encoding="utf-8"))
    if meta.get("snapshot_id") != "snap-20261030-live-20261031":
        raise ValueError("current frozen printing source changed")
    return {"enrichment_sha256": digest(ENRICHMENT), "art_label_sha256": digest(ART),
            "story_recovery_sha256": digest(STORY), "scryfall_manifest_sha256": digest(SNAP),
            "printing_source_sha256": meta["files"]["default-cards"]["sha256"],
            "printing_source_file": meta["files"]["default-cards"]["filename"]}


def build(bulk: Path) -> dict:
    meta = inputs()
    if bulk.name != meta["printing_source_file"] or digest(bulk) != meta["printing_source_sha256"]:
        raise ValueError("local Scryfall file is not the exact pinned printing bulk")
    cache = S.audit(S.inventory())
    if cache["counts"] != {"present": 660} or cache["colliding_cache_paths"]:
        raise ValueError("660-page official source cache must be strictly complete")
    drift_urls = {r["url"] for r in json.loads(STORY.read_text(encoding="utf-8"))["drift_review_queue"]}
    rows = pending()
    # The read-only library scan selects this one exact current bulk file.
    old_mode, old_cache = os.environ.get("MTG_SCRYFALL_MODE"), os.environ.get("MTG_MULTIVERSE_CACHE")
    try:
        os.environ["MTG_SCRYFALL_MODE"] = "multiverse"
        os.environ["MTG_MULTIVERSE_CACHE"] = str(bulk.parent)
        prints = B.load_printings({r["oracle_id"] for r in rows})
    finally:
        if old_mode is None:
            os.environ.pop("MTG_SCRYFALL_MODE", None)
        else:
            os.environ["MTG_SCRYFALL_MODE"] = old_mode
        if old_cache is None:
            os.environ.pop("MTG_MULTIVERSE_CACHE", None)
        else:
            os.environ["MTG_MULTIVERSE_CACHE"] = old_cache
    stories, norm = B.story_norm()
    captions = B.art_captions()
    evidence_counts = Counter()
    evidence_rows = []
    for row in rows:
        x = {"entry": row["entry"], "name": row["character"], "relation": "name-match"}
        result = B.audit_name_match(x, {"name": row["card"]},
                                    {"name": row["character"], "text": ""},
                                    prints.get(row["oracle_id"], {"flavors": [], "artists": set(),
                                                                  "spotlight": [], "sets": [], "set_types": set()}),
                                    captions, stories, norm)
        lead = result.get("confirmed")
        source = (lead or {}).get("source")
        if source in drift_urls:
            status, reason = "SOURCE_DRIFT_REVIEW_ONLY", "OFFICIAL_TEXT_EXTRACTION_CHANGED_AFTER_BASELINE"
        elif lead:
            status, reason = "EVIDENCE_LEAD_REVIEW_ONLY", "CO_OCCURRENCE_OR_PRINTING_METADATA_IS_NOT_A_DEPICTION_APPROVAL"
        else:
            status, reason = "UNRESOLVED_NAME_ONLY", "NO_DIRECT_PRINTING_OR_OFFICIAL_PAGE_EVIDENCE"
        evidence_counts[(lead or {}).get("by", "none")] += 1
        evidence_rows.append({**row, "status": status, "reason": reason,
                              "lead_type": (lead or {}).get("by"), "source_url": source,
                              "paper_printing_found": bool(prints.get(row["oracle_id"], {}).get("sets")),
                              "canon_promotion": False})
    art_rows = art_unresolved()
    art_total = len(json.loads(ART.read_text(encoding="utf-8"))["labels"])
    return {"schema": "unresolved-lore-link-source-audit/v1", "as_of": "2026-10-31",
            "source_metadata": meta, "totals": {
                "pending_name_matches": len(rows),
                "pending_oracle_identities": len({r["oracle_id"] for r in rows}),
                "name_matches_by_status": dict(sorted(Counter(r["status"] for r in evidence_rows).items())),
                "candidate_evidence_types": dict(sorted(evidence_counts.items())),
                "story_image_labels_matched": art_total - len(art_rows),
                "unresolved_story_image_labels": len(art_rows),
            }, "name_matches": evidence_rows, "unresolved_story_images": art_rows,
            "source_text_embedded": False, "approval_or_canon_changes": False,
            "limitations": [
                "A same-page reference is a candidate, not proof a specific printing depicts a scene.",
                "Story Spotlight metadata names a story moment but does not by itself prove an exact character depiction.",
                "Absence in this bounded source corpus does not prove an MTG card has no lore anywhere.",
                "Unresolved name matches, title collisions and art label mismatches must remain explicitly unapproved.",
            ]}


def check_saved() -> dict:
    doc = json.loads(OUT.read_text(encoding="utf-8"))
    rows = pending()
    expected = {(r["oracle_id"], r["card"], r["entry"], r["character"]) for r in rows}
    actual = [(r["oracle_id"], r["card"], r["entry"], r["character"]) for r in doc["name_matches"]]
    art = art_unresolved()
    allowed = {"EVIDENCE_LEAD_REVIEW_ONLY", "SOURCE_DRIFT_REVIEW_ONLY", "UNRESOLVED_NAME_ONLY"}
    if doc.get("schema") != "unresolved-lore-link-source-audit/v1" or \
       doc.get("source_metadata") != inputs() or doc.get("source_text_embedded") is not False or \
       doc.get("approval_or_canon_changes") is not False or \
       doc["totals"]["pending_name_matches"] != len(rows) or \
       len(actual) != len(expected) or set(actual) != expected or \
       doc["totals"]["unresolved_story_image_labels"] != len(art) or \
       doc["totals"]["story_image_labels_matched"] + len(art) != \
           len(json.loads(ART.read_text(encoding="utf-8"))["labels"]) or \
       doc["unresolved_story_images"] != art or \
       any(r["canon_promotion"] is not False or not r["reason"] or r["status"] not in allowed or
           (r["status"] == "UNRESOLVED_NAME_ONLY" and r["source_url"] is not None)
           for r in doc["name_matches"]):
        raise ValueError("unsupported lore-link report is stale or promotes tentative claims")
    if doc["totals"]["name_matches_by_status"] != \
       dict(sorted(Counter(r["status"] for r in doc["name_matches"]).items())) or \
       doc["totals"]["candidate_evidence_types"] != \
       dict(sorted(Counter(r["lead_type"] or "none" for r in doc["name_matches"]).items())):
        raise ValueError("unsupported-lore-link status totals disagree")
    return doc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bulk", type=Path, help="exact local Default Cards archive for the full replay")
    ap.add_argument("--check", action="store_true", help="portable validation; fully replay when --bulk is set")
    args = ap.parse_args()
    if args.check:
        doc = check_saved()
        if args.bulk and build(args.bulk) != doc:
            raise ValueError("full printing/source replay differs from saved review-only report")
    else:
        if not args.bulk:
            ap.error("--bulk is required when creating the independent report")
        doc = build(args.bulk)
        OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("PASS unresolved review:", doc["totals"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
