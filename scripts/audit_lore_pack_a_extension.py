#!/usr/bin/env python3
"""Offline source-boundary and Phase 1B card-index join for Pack A2.

This checks reproducible links and declared limits, not the independent truth
of artwork interpretation or all lore prose.
"""
import argparse
import csv
import json
from pathlib import Path
from urllib.parse import urlparse

import audit_lore_pack_a as base

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "data/lore_research/pack_a_elder_dragon_war_extension_2026-10-30.json"
REPORT = ROOT / "data/lore_research/pack_a_elder_dragon_war_audit_2026-10-30.json"
CARDS = ROOT / "data/card_index.csv"
FIRST_PARTY_SOURCES = {
    "https://magic.wizards.com/en/news/feature/returning-legends-modern-horizons-2-2021-06-10",
    "https://magic.wizards.com/en/news/feature/legends-youll-find-dominaria-united-2022-09-01",
    "https://magic.wizards.com/en/news/feature/dominaria-united-release-notes-2022-08-26",
    "https://magic.wizards.com/en/news/feature/core-set-2019-release-notes-2018-06-22",
    "https://magic.wizards.com/en/news/making-magic/more-odds-ends-core-set-2019-2018-08-06",
}


def dump(data):
    return (json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode()


def build():
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    original = json.loads(base.EVIDENCE.read_text(encoding="utf-8"))
    if (data["extension_id"] != "PACK_A2_ELDER_DRAGON_WAR_AND_PRIMEVAL_LINEAGES"
            or data["extends"] != base.EVIDENCE.name
            or data["evidence_cutoff"] != "2026-10-30"):
        raise ValueError("Wrong source extension identity or checkpoint")
    source_urls = set()
    with base.STORIES.open(encoding="utf-8", newline="") as f:
        historical_story_urls = {base.norm(row["url"]) for row in csv.DictReader(f)
                                 if urlparse(row["url"]).hostname in
                                 ("magic.wizards.com", "www.magic.wizards.com")}
    for key, source in data["source_register"].items():
        url = base.norm(source["url"])
        if url not in historical_story_urls and url not in FIRST_PARTY_SOURCES:
            raise ValueError(f"Unknown first-party source: {key}")
        if not source.get("perspective") or not source.get("title") or url in source_urls:
            raise ValueError(f"Duplicate or missing source description: {key}")
        source_urls.add(url)

    prior_ids = {e["id"] for e in original["entities"]}
    entity_ids = [e["id"] for e in data["entities"]]
    if len(entity_ids) != 10 or len(set(entity_ids)) != 10 or prior_ids.intersection(entity_ids):
        raise ValueError("Pack A2 entity count, uniqueness or original identity regression")
    known_ids = prior_ids | set(entity_ids)
    claims = data["claims"]
    if [c["id"] for c in claims] != [f"A{i:03d}" for i in range(13, 25)]:
        raise ValueError("Stable add-on claim IDs must be A013–A024")
    for c in claims:
        if (c["grade"] not in base.ALLOWED or c["subject"] not in known_ids
                or any(k.strip() not in known_ids for k in c["object"].split(";"))
                or not c.get("stage") or not c.get("summary") or not c.get("limitation")
                or not c.get("source_ids")
                or any(s not in data["source_register"] for s in c["source_ids"])):
            raise ValueError(f"Broken or unqualified Pack A2 claim: {c['id']}")
    by_id = {c["id"]: c for c in claims}
    if (by_id["A018"]["source_ids"] != ["mh2_legends", "perspectives"]
            or by_id["A020"]["stage"] == "elder_dragon_wars"
            or by_id["A021"]["stage"] == "elder_dragon_wars"):
        raise ValueError("Survivor discrepancy and later Dakkon event must remain separate")

    with CARDS.open(encoding="utf-8", newline="") as f:
        index = {r["name"]: r for r in csv.DictReader(f)}
    anchors, oracle_ids = [], set()
    for a in data["card_anchors"]:
        if (a["representation"] not in {"NAMED_CHARACTER_CARD", "NAMED_EVENT_CARD"}
                or a["entity"] not in known_ids or not a["limit"]
                or not a["source_ids"]
                or any(s not in data["source_register"] for s in a["source_ids"])):
            raise ValueError(f"Unqualified card anchor: {a['name']}")
        row = index.get(a["name"])
        if not row or row["oracle_id"] in oracle_ids:
            raise ValueError(f"Anchor missing or repeated in fixed card index: {a['name']}")
        oid = row["oracle_id"]
        oracle_ids.add(oid)
        shard = ROOT / "data/set_atlas" / f"historical_cards_{oid[0]}.json"
        printing_index = json.loads(shard.read_text(encoding="utf-8"))
        printings = [p for p in printing_index.get(oid, []) if p[6] == "en" and p[7] == 1]
        if not printings or any(p[2] != oid for p in printings):
            raise ValueError(f"No exact-ID historical English-paper printing join for {a['name']}")
        earliest = sorted(printings, key=lambda p: (p[5], p[0], p[4], p[1]))[0]
        anchors.append({
            "name": a["name"], "oracle_id": oid, "color_identity_at_index": row["color_identity"],
            "type_line_at_index": row["type_line"],
            "first_indexed_english_paper_printing": {
                "set": earliest[0], "printing_id": earliest[1], "collector_number": earliest[4],
                "released_at": earliest[5]
            }, "historical_english_paper_printings": len(printings),
            "representation": a["representation"], "meaning_limit": a["limit"]
        })
    if len(anchors) != 9 or sum(a["representation"] == "NAMED_EVENT_CARD" for a in anchors) != 1:
        raise ValueError("Expected nine named card anchors including one named event")
    return {
        "schema": 1, "as_of": data["evidence_cutoff"], "extends": data["extends"],
        "result": "SOURCE_GRADED_ELDER_WAR_AND_HISTORICAL_CARD_NAME_JOIN_PASS",
        "additional_claims": len(claims), "additional_entities": len(entity_ids),
        "first_party_source_urls": len(source_urls), "card_name_anchors": len(anchors),
        "card_anchors": anchors,
        "limitations": [
            "Official named card identity and October 29-era historical printing data do not independently prove an artwork's event setting.",
            "Printed color identities and legalities are frozen historical index facts, not a present-day Commander certification.",
            "Bolas's four-name survivor account omitted Piru; source-perspective boundaries and later events must be kept distinct.",
            "This structural audit cannot machine-certify every in-universe assertion in a source biography."
        ]
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    report = build()
    payload = dump(report)
    if args.write:
        REPORT.write_bytes(payload)
    elif not REPORT.exists() or REPORT.read_bytes() != payload:
        raise ValueError("Pack A2 report mismatch: run with --write only after reviewing sources")
    print(json.dumps({k: report[k] for k in
                      ("result", "additional_claims", "additional_entities", "first_party_source_urls", "card_name_anchors")},
                     sort_keys=True))


if __name__ == "__main__":
    main()
