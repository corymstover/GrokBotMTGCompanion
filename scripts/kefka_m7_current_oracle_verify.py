#!/usr/bin/env python3
"""Fetch current Scryfall identities for exact Kefka M7 Rev1 candidate.

This is independent of the older Grok 2026-10-23 snapshot. It verifies the
whole physical 100 but does not simulate Commander combat or approve a deck.
The tracked candidate source contains a final LF; canonical raw SHA is from
the identical 100 lines *without* that terminal LF.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/grixis/m7/independent_candidates/Kefka__Court_Mage_M7_Sakashima_StepThrough_TwoSwap_Research_20261024.txt"
EXPECTED_SHA = "14277f6e9774c5ef02b4f92332b52684794367007abf81bc2d84ef7ad7bcaa7d"
COMMANDER = "Kefka, Court Mage // Kefka, Ruler of Ruin"
URL = "https://api.scryfall.com/cards/collection"


def parse_source(data: bytes):
    raw = data.removesuffix(b"\n")
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA, "Unpinned candidate bytes"
    lines = raw.decode("utf-8").splitlines()
    assert len(lines) == 100
    cards = []
    for index, line in enumerate(lines):
        match = re.fullmatch(r"1x (.+?)( \[Commander\])?", line)
        assert match, f"Invalid physical deck row {index+1}"
        name, commander = match.groups()
        assert bool(commander) is (index == 0), "Commander line not unique or first"
        cards.append(name)
    assert cards[0] == COMMANDER and len(set(cards)) == 100
    return cards


def fetch_current(cards: list[str], endpoint=URL):
    found = []
    for start in range(0, len(cards), 70):
        # Scryfall's collection endpoint resolves the front-face name of a
        # transform card, then returns the authoritative full // display name.
        request_data = {"identifiers": [{"name": x.split(" // ")[0]}
                                        for x in cards[start:start+70]]}
        request = Request(endpoint, data=json.dumps(request_data).encode("utf-8"),
                          headers={"User-Agent": "GrixisEncyclopedia/1.0 Oracle source audit",
                                   "Accept": "application/json", "Content-Type": "application/json"},
                          method="POST")
        with urlopen(request, timeout=30) as response:
            page = json.load(response)
        assert not page.get("not_found"), f"Unresolved Scryfall card(s): {page['not_found']}"
        assert page.get("object") == "list", "Unexpected API response"
        found.extend(page["data"])
        if start + 70 < len(cards):
            time.sleep(0.18)  # Respect Scryfall's API pacing.
    return found


def verify(cards: list[str], fetched: list[dict]):
    by_name = {entry["name"]: entry for entry in fetched}
    assert len(by_name) == len(cards) and set(by_name) == set(cards), "Missing or aliased Oracle identities"
    archived = []
    for name in cards:
        c = by_name[name]
        assert c["legalities"]["commander"] == "legal", f"Not officially Commander-legal: {name}"
        assert set(c["color_identity"]) <= set("UBR"), f"Off-identity card: {name}"
        assert c.get("oracle_id"), f"Missing Oracle identity: {name}"
        faces = c.get("card_faces") or []
        texts = [face.get("oracle_text", "") for face in faces] or [c.get("oracle_text", "")]
        assert all(texts), f"Missing Oracle text: {name}"
        archived.append({
            "name": name, "oracle_id": c["oracle_id"], "legalities_commander": c["legalities"]["commander"],
            "color_identity": c["color_identity"], "mana_cost": c.get("mana_cost", ""),
            "type_line": c["type_line"], "layout": c["layout"],
            "game_changer": bool(c.get("game_changer", False)),
            "oracle_text": c.get("oracle_text") or "\n//\n".join(texts),
            "card_faces": [{"name": f.get("name"), "type_line": f.get("type_line"),
                            "mana_cost": f.get("mana_cost"), "oracle_text": f.get("oracle_text")}
                           for f in faces],
            "scryfall_uri": c["scryfall_uri"],
        })
    lands = [c["name"] for c in archived if "Land" in c["type_line"].split(" // ")[0].split(" — ")[0]]
    assert len(lands) == 28, f"Unexpected printed land count: {len(lands)}"
    assert set(by_name[COMMANDER]["color_identity"]) == set("UBR")
    assert "Sakashima of a Thousand Faces" in by_name and "Step Through" in by_name
    assert "Phyrexian Metamorph" not in by_name and "Demonic Counsel" not in by_name
    return {
        "contract": "KEFKA_M7_EXACT_100_CURRENT_SCRYFALL_ORACLE_V1",
        "verified_utc": datetime.now(timezone.utc).isoformat(),
        "source_api": URL, "raw_candidate_sha256_no_terminal_lf": EXPECTED_SHA,
        "count": len(archived), "distinct_count": len(by_name), "printed_lands": len(lands),
        "commander": COMMANDER, "commander_identity": ["B", "R", "U"],
        "official_commander_legal_all": True, "project_exceptions": [],
        "archived_game_changer_count": sum(c["game_changer"] for c in archived),
        "cards": archived, "mechanics_test_status": "SEPARATE_P0_P1_SCOPE_REQUIRED",
        "owner_approval_status": "NOT_APPROVED",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cards = parse_source(SOURCE.read_bytes())
    archive = verify(cards, fetch_current(cards))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(archive, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print({k: v for k, v in archive.items() if k not in {"cards"}})


if __name__ == "__main__":
    main()
