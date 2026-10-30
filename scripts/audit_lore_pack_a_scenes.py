#!/usr/bin/env python3
"""Verify Pack A3's primary story-art labels and exact historical card-name joins.

Official caption evidence is stronger than a thematic link, but an Oracle ID
does not prove a particular artwork was used on every printing variant.
"""
import argparse
import csv
import json
from pathlib import Path

import audit_lore_pack_a as A1
import audit_lore_pack_a_extension as A2

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "data/lore_research/pack_a_tarkir_card_scenes_2026-10-30.json"
OUTPUT = ROOT / "data/lore_research/pack_a_tarkir_card_scenes_audit_2026-10-30.json"
OFFICIAL_ARTICLES = {
    "https://magic.wizards.com/en/news/feature/reforged-chain-2015-01-21",
    "https://magic.wizards.com/en/news/magic-story/story-tarkir-block-2015-04-29",
    "https://magic.wizards.com/en/news/making-magic/prose-and-khans-part-2-2014-09-22",
    "https://magic.wizards.com/en/news/magic-story/chronicle-bolas-familiar-stranger-2018-08-01",
    "https://magic.wizards.com/en/news/feature/journey-nexus-2014-12-10",
    "https://magic.wizards.com/en/story/tarkir-plane",
}
TIERS = {"DIRECT_EVENT_SCENE_CAPTION", "OFFICIAL_STORY_DEVICE", "STORY_LOCATION_ART_CAPTION",
         "NAMED_CHARACTER_ART_IN_STORY"}


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def build():
    d = json.loads(INPUT.read_text(encoding="utf-8"))
    a1 = json.loads(A1.EVIDENCE.read_text(encoding="utf-8"))
    a2 = json.loads(A2.INPUT.read_text(encoding="utf-8"))
    if (d["extension_id"] != "PACK_A3_TARKIR_STORY_SCENES_AND_CARD_ART_CONTEXT"
            or d["evidence_cutoff"] != "2026-10-30"
            or d["extends"] != [A1.EVIDENCE.name, A2.INPUT.name]):
        raise ValueError("Pack A3 identity or dependency mismatch")
    sources = d["source_register"]
    urls = [A1.norm(s["url"]) for s in sources.values()]
    if len(urls) != 6 or set(urls) != OFFICIAL_ARTICLES:
        raise ValueError("Source register must be the six directly reviewed Wizards articles")
    if any(not s["title"] or not s["perspective"] for s in sources.values()):
        raise ValueError("All source-perspective labels are required")
    old_entities = {e["id"] for e in a1["entities"] + a2["entities"]}
    newer = [e["id"] for e in d["entities"]]
    if len(newer) != 7 or len(set(newer)) != 7 or old_entities.intersection(newer):
        raise ValueError("Missing or colliding new Pack A3 entities")
    all_entities = old_entities | set(newer)
    claims = d["claims"]
    if [c["id"] for c in claims] != [f"A{i:03d}" for i in range(25, 33)]:
        raise ValueError("Stable claim ID sequence must continue A025–A032")
    for c in claims:
        if (c["subject"] not in all_entities or c["object"] not in all_entities
                or c["grade"] not in A1.ALLOWED or not c["event_stage"] or not c["continuity"]
                or not c["summary"] or not c["limitation"] or not c["source_ids"]
                or any(s not in sources for s in c["source_ids"])):
            raise ValueError(f"Unsupported claim structure: {c['id']}")
    c = {x["id"]: x for x in claims}
    if (c["A028"]["continuity"] != "revised Tarkir timeline created by intervention"
            or c["A030"]["source_ids"] != ["reforged_chain"]):
        raise ValueError("Tarkir branch or direct story caption provenance downgraded")

    with A2.CARDS.open(encoding="utf-8", newline="") as f:
        indexed = {c["name"]: c for c in csv.DictReader(f)}
    mapped, oracles = [], set()
    for card in d["card_art_context"]:
        if (card["tier"] not in TIERS or card["event"] not in {"tarkir_duel", "pre_duel_time_travel", "ugin_grave_site"}
                or not card["caption_artist"] or not card["limit"]
                or not card["source_ids"] or any(s not in sources for s in card["source_ids"])):
            raise ValueError(f"Unqualified story card: {card['name']}")
        v = indexed.get(card["name"])
        if not v or v["oracle_id"] in oracles:
            raise ValueError(f"Missing or duplicate historical card name: {card['name']}")
        oid = v["oracle_id"]
        oracles.add(oid)
        prints = json.loads((ROOT / "data/set_atlas" / f"historical_cards_{oid[0]}.json").read_text(encoding="utf-8"))
        paper = [p for p in prints.get(oid, []) if p[2] == oid and p[6] == "en" and p[7] == 1]
        if not paper:
            raise ValueError(f"No English-paper printing rows for: {card['name']}")
        first = sorted(paper, key=lambda p: (p[5], p[0], p[4], p[1]))[0]
        mapped.append({"name": card["name"], "oracle_id": oid,
                       "color_identity_at_oct15_index": v["color_identity"],
                       "type_line_at_oct15_index": v["type_line"], "source_ids": card["source_ids"],
                       "art_context_tier": card["tier"], "source_caption_artist": card["caption_artist"],
                       "first_indexed_english_paper_printing": {
                           "set": first[0], "printing_id": first[1], "released_at": first[5], "collector_number": first[4]},
                       "historical_english_paper_printings": len(paper),
                       "specific_artist_to_printing_id_match_proven": False,
                       "limitation": card["limit"]})
    if len(mapped) != 6 or sum(x["art_context_tier"] == "DIRECT_EVENT_SCENE_CAPTION" for x in mapped) != 1:
        raise ValueError("Six distinct art contexts, including exactly one direct scene, required")
    crux = next(x for x in mapped if x["name"] == "Crux of Fate")
    if crux["art_context_tier"] != "DIRECT_EVENT_SCENE_CAPTION" or crux["source_ids"] != ["reforged_chain"]:
        raise ValueError("Crux of Fate direct story-scene caption source must remain exact")
    return {
        "schema": 1, "as_of": d["evidence_cutoff"], "result": "OFFICIAL_STORY_SCENE_AND_HISTORICAL_NAME_JOIN_PASS",
        "claims": len(claims), "entities": len(newer), "primary_sources": len(urls),
        "graded_art_context_cards": len(mapped), "direct_event_scene_caption_cards": 1,
        "all_six_historical_identity_colors_fit_grixis": all(set(x["color_identity_at_oct15_index"]) <= set("BRU")
                                                  or x["color_identity_at_oct15_index"] == "C" for x in mapped),
        "cards": mapped,
        "limitations": [
            "The captioned art is tied to an official story webpage, not to a verified Scryfall image/artist record for each printing ID.",
            "Only Crux of Fate is certified as a direct scene-context art caption here; character pictures and land locations have separate lower tiers.",
            "Historical color identity is not present-day Oracle/Commander legality and is not a decklist approval.",
            "A witness to the altered timeline is not proof that both mutually exclusive outcomes occurred in a single unchanged sequence."
        ]
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    report = build()
    payload = encode(report)
    if args.write:
        OUTPUT.write_bytes(payload)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != payload:
        raise ValueError("Pack A3 report drift")
    print(json.dumps({k: report[k] for k in
                      ("result", "claims", "entities", "primary_sources", "graded_art_context_cards",
                       "direct_event_scene_caption_cards", "all_six_historical_identity_colors_fit_grixis")}, sort_keys=True))


if __name__ == "__main__":
    main()
