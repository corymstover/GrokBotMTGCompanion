"""Live Scryfall /cards/collection check for the exact Nekusar M7 Rev1 97 names.

The GitHub Actions runner supplies outbound internet access; no keys required.
Failure is a hard CI failure, not a reason to claim verified-by-inference.
"""
import json
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from time import sleep
from test_nekusar_m7_rev1 import CANDIDATE, CAND_SHA, parse, sha256

SOURCE = "https://api.scryfall.com/cards/collection"
IDENTITY = {"U", "B", "R"}
CRITICAL_ORACLE_PHRASES = {
    "Nekusar, the Mindrazer": ["Whenever an opponent draws a card", "At the beginning of each player's draw step"],
    "Roaming Throne": ["triggered ability of another creature you control of the chosen type", "additional time"],
    "Spark Double": ["isn't legendary"],
    "Bloodletter of Aclazotz": ["If an opponent would lose life during your turn", "twice"],
    "Glint-Horn Buccaneer": ["Whenever you discard a card", "1 damage to each opponent"],
    "Faerie Mastermind": ["Whenever an opponent draws their second card each turn"],
    "Sigil of Sleep": ["Whenever enchanted creature deals damage to a player"],
    "Cavern of Souls": ["creature spell of the chosen type", "can't be countered"],
}


def fetch_group(names):
    body = json.dumps({"identifiers": [{"name": name} for name in names]}).encode()
    req = Request(SOURCE, data=body, method="POST", headers={
        "User-Agent": "GrixisCommanderEncyclopedia-M7-Nekusar/1.0",
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json"
    })
    for attempt in range(3):
        try:
            with urlopen(req, timeout=25) as resp:
                return json.load(resp)
        except HTTPError as exc:
            if exc.code in (429, 500, 502, 503, 504) and attempt < 2:
                sleep(2 * (attempt + 1))
                continue
            raise


def main():
    cards, _ = parse(CANDIDATE)
    assert sha256(CANDIDATE.read_bytes()).hexdigest() == CAND_SHA
    names = list(cards.keys())
    records = {}
    for i in range(0, len(names), 70):
        result = fetch_group(names[i:i + 70])
        assert result.get("not_found") in (None, []), result.get("not_found")
        for item in result["data"]:
            # Scryfall reports transforming/modal cards as "front // back".
            front_name = item["name"].split(" // ")[0]
            records[front_name] = item
        sleep(0.15)

    errors = []
    if set(records) != set(names):
        errors.append(f"Resolution mismatch missing={set(names)-set(records)} extra={set(records)-set(names)}")
    for name in names:
        c = records.get(name)
        if not c:
            continue
        if c["legalities"]["commander"] != "legal":
            errors.append(f"{name}: not Commander legal: {c['legalities']['commander']}")
        if not set(c["color_identity"]) <= IDENTITY:
            errors.append(f"{name}: forbidden color identity {c['color_identity']}")
    for name, phrases in CRITICAL_ORACLE_PHRASES.items():
        c = records.get(name)
        if not c:
            continue
        oracle = c.get("oracle_text", "")
        for phrase in phrases:
            if phrase.lower() not in oracle.lower():
                errors.append(f"{name}: Oracle text missing required phrase {phrase!r}")
    # Card identity names are all exact English front names in this deck.
    if errors:
        raise AssertionError("\n".join(errors))

    print(f"PASS live Scryfall /cards/collection resolved {len(records)}/{len(names)} exact names;")
    print("PASS each Commander legal and Grixis UBR/colorless; new material Oracle witnesses PASS;")
    print(f"PASS exact candidate raw SHA-256 {CAND_SHA}")
    print("API records are current point-in-time checks, not a measured gameplay win rate.")


if __name__ == "__main__":
    main()
