#!/usr/bin/env python3
"""Generate the two explicit larger portfolios and refresh a source-bound Scryfall snapshot.

Network use is limited to Scryfall's public exact-name batch endpoint.  This is
an evidence acquisition utility, not a game simulation or owner approval.
"""
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
CANDIDATES = HERE.parent / "candidate_lists"
MAIN = CANDIDATES / "The_Valeyard_M7_Rev1.txt"
ALT7 = CANDIDATES / "The_Valeyard_M7_Rev1_alt7.txt"
ALT8 = CANDIDATES / "The_Valeyard_M7_Rev1_alt8.txt"


def variant(source, swaps):
    lines = source.splitlines()
    for cut, add in swaps:
        old = "1x " + cut
        assert lines.count(old) == 1, (cut, lines.count(old))
        lines[lines.index(old)] = "1x " + add
    return "\n".join([lines[0], *sorted(lines[1:], key=str.casefold)]) + "\n"


def oracle_cards(names):
    out = {}
    all_names = sorted(set(names))
    for offset in range(0, len(all_names), 75):
        group = all_names[offset:offset + 75]
        payload = json.dumps({"identifiers": [{"name": x} for x in group]})
        raw = subprocess.check_output([
            "curl", "--fail", "-sS", "--retry", "3", "--max-time", "30",
            "-X", "POST", "-H", "Content-Type: application/json", "--data", payload,
            "https://api.scryfall.com/cards/collection",
        ], timeout=40)
        response = json.loads(raw)
        assert response.get("object") == "list" and not response.get("not_found"), response
        for card in response["data"]:
            key = card["name"]
            assert key in group and key not in out, key
            out[key] = {
                "oracle_id": card["oracle_id"],
                "oracle_text": card.get("oracle_text") or " // ".join(
                    f.get("oracle_text", "") for f in card.get("card_faces", [])),
                "color_identity": card["color_identity"],
                "commander_legality": card["legalities"]["commander"],
                "mana_cost": card.get("mana_cost", ""),
                "type_line": card["type_line"],
                "scryfall_uri": card["scryfall_uri"],
                "game_changer": card.get("game_changer", False),
            }
    if set(all_names) != set(out):
        raise AssertionError(f"Scryfall names differ: missing {set(all_names) - set(out)}; "
                             f"unexpected {set(out) - set(all_names)}")
    return dict(sorted(out.items()))


def main():
    main = MAIN.read_text(encoding="utf8")
    ALT7.write_text(variant(main, [("Fellwar Stone", "Mana Vault")]), encoding="utf8")
    ALT8.write_text(variant(main, [("Fellwar Stone", "Mana Vault"),
                                   ("Midnight Crusader Shuttle", "Helm of the Host")]), encoding="utf8")
    files = [HERE / "The_Valeyard_Oct15_baseline.txt", MAIN, ALT7, ALT8]
    names = {x.split("x ", 1)[1].replace(" [Commander]", "")
             for path in files for x in path.read_text().splitlines()}
    snapshot = {
        "source": "Scryfall public /cards/collection exact-name API",
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "deck_id": "The_Valeyard",
        "card_count_unique": len(names),
        "oracle_cards": oracle_cards(names),
    }
    target = HERE / "The_Valeyard_M7_Rev1_Scryfall_snapshot.json"
    target.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    print(f"Recorded {len(names)} resolved names in {target.name}")


if __name__ == "__main__":
    main()
