#!/usr/bin/env python3
"""Replay Pack A4's frozen, human-reviewed official-art-to-printing ledger.

This offline check validates traceability and non-conflation. It does not re-fetch
Scryfall or classify pixels; the dated visual review is documented in the ledger.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "data/lore_research/pack_a4_printing_art_matches_2026-10-30.json"
A3 = ROOT / "data/lore_research/pack_a_tarkir_card_scenes_2026-10-30.json"
UUID = re.compile(r"^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$")


def build():
    record = json.loads(LEDGER.read_text(encoding="utf-8"))
    earlier = json.loads(A3.read_text(encoding="utf-8"))
    if (record["schema"], record["pack_id"], record["extends"]) != (
        1, "PACK_A4_SIX_EXACT_TARKIR_STORY_ART_PRINTING_MATCHES", A3.name
    ):
        raise ValueError("Unexpected Pack A4 schema or parent")
    cards = record["cards"]
    prior = {c["name"]: c for c in earlier["card_art_context"]}
    sources = earlier["source_register"]
    if len(cards) != len(prior) or {c["name"] for c in cards} != set(prior):
        raise ValueError("A4 must cover exactly the six original A3 names")

    seen_ids, seen_art = set(), set()
    matched_ids = 0
    for card in cards:
        name = card["name"]
        if card["context_tier"] != prior[name]["tier"]:
            raise ValueError("A3 story-context grade changed: " + name)
        if card["source_id"] not in prior[name]["source_ids"]:
            raise ValueError("Source is not an A3 caption source: " + name)
        if not (sources[card["source_id"]]["url"].startswith("https://magic.wizards.com/")
                and card["source_art_url"].startswith("https://media.wizards.com/")):
            raise ValueError("Unrecognized first-party provenance: " + name)
        if not all(UUID.fullmatch(card[key]) for key in ("oracle_id", "matched_illustration_id")):
            raise ValueError("Malformed stable Oracle or illustration identity: " + name)
        art = (card["oracle_id"], card["matched_illustration_id"])
        if art in seen_art:
            raise ValueError("Duplicate card/illustration combination")
        seen_art.add(art)
        if not card["artist"] or card["commander_legal_at_review"] is not True:
            raise ValueError("Unreviewed artist/current-legal snapshot: " + name)
        representative = card["visually_reviewed_printing"]
        if not (UUID.fullmatch(representative["id"]) and representative["set"]
                and representative["collector_number"]):
            raise ValueError("Invalid independently compared printing")
        variants = card["same_art_printing_ids"]
        if not variants or representative["id"] not in variants or len(variants) != len(set(variants)):
            raise ValueError("Representative missing or repeated among same-art variants")
        if any(not UUID.fullmatch(pid) or pid in seen_ids for pid in variants):
            raise ValueError("Invalid or cross-card duplicated printing UUID")
        seen_ids.update(variants)
        matched_ids += len(variants)

    if matched_ids != 20:
        raise ValueError("Expected 20 exactly identified same-illustration printing IDs")
    ugin = next(c for c in cards if c["name"] == "Ugin, the Spirit Dragon")
    wrong_art = ugin["known_different_art_first_indexed_promo"]
    if not (ugin["artist"] == "Raymond Swanland" and
            ugin["visually_reviewed_printing"]["set"] == "frf" and
            ugin["visually_reviewed_printing"]["collector_number"] == "1" and
            wrong_art["set"] == "ugin" and wrong_art["artist"] == "Chris Rahn" and
            wrong_art["id"] not in ugin["same_art_printing_ids"] and
            wrong_art["illustration_id"] != ugin["matched_illustration_id"]):
        raise ValueError("Ugin's promo-vs-story illustration correction was lost")
    if sum(c["context_tier"] == "DIRECT_EVENT_SCENE_CAPTION" for c in cards) != 1:
        raise ValueError("Only Crux of Fate has a direct witnessed duel caption")

    return {"status": "PASS_FROZEN_ART_LEDGER_REPLAY", "reviewed_at": record["reviewed_at"],
            "visually_reviewed_source_to_printing_pairs": len(cards),
            "same_illustration_printing_ids": matched_ids,
            "distinct_illustration_ids": len(seen_art),
            "all_six_commander_legal_at_review": True,
            "realtime_image_or_legality_fetch": False}


if __name__ == "__main__":
    print(json.dumps(build(), sort_keys=True))
