#!/usr/bin/env python3
"""Offline conservative evidence audit for Ugin/Bolas Pack A first claims.

Verify provenance and claim structure, not the truth of every natural-language
sentence. Human primary-source reading and context remain mandatory.
"""
import argparse
import csv
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = ROOT / "data/lore_research/pack_a_ugin_bolas_evidence_2026-10-30.json"
OUTPUT = ROOT / "data/lore_research/pack_a_evidence_audit_2026-10-30.json"
STORIES = ROOT / "data/story_index.csv"
ALLOWED = {"CANON_CONFIRMED", "CANON_IMPLIED", "CANON_DISPUTED",
           "ALTERNATE_CONTINUITY", "OPEN_QUESTION"}
# Direct Wizards sources checked during research but absent from the 660-story
# original inventory. This exception is a source-URL presence allowance, not
# independent verification of factual claims in the article.
CHECKED_OFFICIAL_SUPPLEMENTS = {
    "https://magic.wizards.com/en/news/magic-story/planeswalkers-guide-fate-reforged-2015-01-07",
    "https://magic.wizards.com/en/news/making-magic/even-more-war-games-2019-05-06",
}


def norm(url):
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in ("magic.wizards.com", "www.magic.wizards.com"):
        raise ValueError(f"Not a first-party Wizards HTTPS URL: {url}")
    return f"https://magic.wizards.com{parsed.path.rstrip('/')}"


def encode(data):
    return (json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def build():
    data = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    if data["pack_id"] != "PACK_A_UGIN_BOLAS_ELDER_DRAGONS" or data["evidence_cutoff"] != "2026-10-30":
        raise ValueError("Pack evidence identity or date changed")
    with STORIES.open(encoding="utf-8", newline="") as f:
        saved = {norm(r["url"]) for r in csv.DictReader(f)
                 if urlparse(r["url"]).hostname in ("magic.wizards.com", "www.magic.wizards.com")}
    sources = data["source_register"]
    if len(sources) < 9:
        raise ValueError("Minimum first-party primary-source register not maintained")
    indexed, manually_reviewed = [], []
    for key, source in sources.items():
        url = norm(source["url"])
        if url in saved:
            indexed.append(key)
        elif url in CHECKED_OFFICIAL_SUPPLEMENTS:
            manually_reviewed.append(key)
        else:
            raise ValueError(f"Unknown primary-source link in Pack A: {key}")
        if not source["title"] or not source["perspective"]:
            raise ValueError(f"No title or narrator perspective on source {key}")
    ids = [e["id"] for e in data["entities"]]
    if len(ids) != len(set(ids)) or len(ids) < 12:
        raise ValueError("Duplicate or missing stable entities")
    claims = data["claims"]
    if len(claims) != 12 or [c["id"] for c in claims] != [f"A{i:03d}" for i in range(1, 13)]:
        raise ValueError("Claim set or stable IDs changed without research review")
    for c in claims:
        if c["grade"] not in ALLOWED or not c["source_ids"] or not c["summary"] or not c["limitation"]:
            raise ValueError(f"Missing grade, citation, summary or limitation for {c['id']}")
        if c["subject"] not in ids:
            raise ValueError(f"Unknown subject {c['subject']}")
        if any(src not in sources for src in c["source_ids"]):
            raise ValueError(f"Broken source link for {c['id']}")
        if any(term in c["predicate"].lower() for term in ("depicted_by", "card_legality", "card_representation")):
            raise ValueError(f"Unverified card-to-story depiction claim in {c['id']}")
    byid = {c["id"]: c for c in claims}
    if (byid["A003"]["grade"] != "CANON_DISPUTED" or
            byid["A004"]["grade"] != "CANON_DISPUTED" or
            byid["A011"]["grade"] != "OPEN_QUESTION" or
            byid["A012"]["grade"] != "ALTERNATE_CONTINUITY"):
        raise ValueError("Narrator uncertainty or Echoverse separation was erased")
    if not all(byid[k]["continuity"] != byid["A006"]["continuity"] for k in ("A005", "A007")):
        raise ValueError("Original and altered Tarkir timelines were collapsed")
    return {
        "schema": 1, "as_of": data["evidence_cutoff"], "pack_id": data["pack_id"],
        "claims_checked": len(claims), "entities_checked": len(ids),
        "first_party_source_urls_checked": len(sources),
        "source_register_in_recovered_story_index": sorted(indexed),
        "source_register_externally_reviewed_official_pages": sorted(manually_reviewed),
        "grades": {grade: sum(c["grade"] == grade for c in claims) for grade in sorted(ALLOWED)},
        "deliberately_unverified_card_depictions": True,
        "result": "STRUCTURAL_PRIMARY_SOURCE_BOUNDARY_PASS",
        "limitations": [
            "Structural audit checks sources and conservative claim grades; source interpretation is human-reviewed, not machine-proven.",
            "The elder-war survivor list and spark awakening details are narrator claims; future history may clarify or retcon them.",
            "No card artwork/Oracle-level portrayal is automatically certified by this pack.",
            "Echoverse differs from prime continuity; a missing Echoverse Bolas cannot imply prime-universe erasure."
        ]
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    report = build()
    raw = encode(report)
    if args.write:
        OUTPUT.write_bytes(raw)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != raw:
        raise ValueError("Pack A source/claim audit diverges from published report")
    print(json.dumps({k: report[k] for k in
                      ("result", "claims_checked", "entities_checked", "first_party_source_urls_checked")}, sort_keys=True))


if __name__ == "__main__":
    main()
