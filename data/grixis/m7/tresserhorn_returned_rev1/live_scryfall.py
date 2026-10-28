#!/usr/bin/env python3
"""Consent-authorized Deck 60 full-100 Scryfall exact-name Oracle intake.

Submit only the unique card names in the exact proposed Deck #60 100-card
candidate, *not* the historical list or alternative 100s.
This discloses those names to api.scryfall.com, as Cory explicitly approved
on 2026-10-27 America/Chicago.  Never send credentials or unrelated files.
The output is source data, not a claim that a currently unreleased commander
is officially legal, and not a substitute for the M7 decision/IJ gates.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
PATHS = [
    ROOT / "data/grixis/m7/candidate_lists/Tresserhorn_s_Lord__Returned_M7_Rev1_RESEARCH.txt",
]
SNAPSHOT = ROOT / "data/grixis/m7/oracle_snapshots/Tresserhorn_Returned_M7_Rev1_Scryfall_20261027.json"
API = "https://api.scryfall.com/cards/collection"


def extract(path):
    raw = path.read_bytes()
    names = []
    for line in raw.decode("utf-8").splitlines():
        m = re.fullmatch(r"(\d+)x (.+)", line)
        assert m, (path, line)
        names.extend([m.group(2).removesuffix(" [Commander]")] * int(m.group(1)))
    assert len(names) == 100, (path, len(names))
    return names, hashlib.sha256(raw).hexdigest()


def main():
    source = [extract(path) for path in PATHS]
    unique = list(dict.fromkeys(name for deck, _ in source for name in deck))
    results = []
    not_found = []
    for offset in range(0, len(unique), 75):
        batch = unique[offset:offset + 75]
        # Scryfall collection exact-name matching expects a front-face name
        # for dual-faced cards; its response still gives the complete name.
        payload = json.dumps({"identifiers": [{"name": x.split(" // ")[0]}
                                               for x in batch]}).encode()
        request = urllib.request.Request(
            API, data=payload, method="POST",
            headers={"Content-Type": "application/json", "Accept": "application/json",
                     "User-Agent": "Cory-Grixis-M7-Deck60-Oracle-Verification/1.0"},
        )
        with urllib.request.urlopen(request, timeout=45) as response:
            parsed = json.loads(response.read().decode())
        assert parsed["object"] == "list"
        results.extend(parsed["data"])
        not_found.extend(parsed.get("not_found", []))
        if offset + 75 < len(unique):
            time.sleep(.25)
    if not_found:
        raise RuntimeError("Scryfall unresolved identifiers: " + json.dumps(not_found))
    by_name = {card["name"]: card for card in results}
    assert len(by_name) == len(unique), (len(by_name), len(unique))
    assert set(by_name) == set(unique), {"missing": sorted(set(unique) - set(by_name)),
                                       "extra": sorted(set(by_name) - set(unique))}
    cards = []
    for name in unique:
        item = by_name[name]
        cards.append({
            "name": item["name"],
            "oracle_id": item["oracle_id"],
            "type_line": item["type_line"],
            "mana_cost": item.get("mana_cost"),
            "oracle_text": item.get("oracle_text"),
            "color_identity": item["color_identity"],
            "commander_legality": item["legalities"]["commander"],
            "card_faces": [
                {key: face.get(key) for key in ("name", "mana_cost", "type_line", "oracle_text")}
                for face in item.get("card_faces", [])
            ],
        })
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    data = {
        "source": API,
        "retrieved_utc": stamp,
        "owner_consent_20261027": "Cory explicitly approved sharing exact card names with Scryfall for full-current Oracle verification",
        "source_100_hashes": {path.name: sha for path, (_, sha) in zip(PATHS, source)},
        "unique_identifiers": len(unique),
        "cards": cards,
    }
    SNAPSHOT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Live exact-name Scryfall snapshot:", SNAPSHOT)
    print("Unique card identities:", len(unique))
    print("Commander official legality:", by_name["Tresserhorn's Lord, Returned"]["legalities"]["commander"])
    print("SHA-256:", hashlib.sha256(SNAPSHOT.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
