"""Fetch a dated Scryfall Oracle collection for Nathan's current deck and challengers.

This is source acquisition, not a rules engine or an approval gate.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError


ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "data/grixis/m7/baseline_sources/Nathan_Drake_Treasure_Hunter_Approved_2026-10-15.txt"
DEST = ROOT / "data/grixis/m7/oracle_snapshots/Nathan_Drake_M7_Research_Scryfall_20261026.json"
CHALLENGERS = [
    "Mana Vault", "Grim Monolith", "Chrome Mox", "Mox Diamond", "Mox Amber",
    "Captain Lannery Storm", "Goldspan Dragon", "Curse of Opulence",
    "Combat Celebrant", "Seize the Day", "Port Razer", "Relentless Assault",
    "Dolmen Gate", "Cover of Darkness", "Thieves' Tools", "Security Bypass",
    "Strionic Resonator", "Spark Double", "Sakashima of a Thousand Faces",
    "Toxic Deluge", "Force of Will", "Cavern of Souls", "City of Traitors",
    "Spider-Verse", "Memory Worm", "Mari, the Killing Quill",
    "Azula, Cunning Usurper", "Gonti, Canny Acquisitor", "Breeches, Brazen Plunderer",
    "Anowon, the Ruin Thief", "Gonti, Lord of Luxury", "Grim Hireling",
    "Zuko, Firebending Master", "Firebender Roku", "Ragavan and Kari Zev",
    "Lightning Bolt", "Malakir Rebirth", "Fell the Profane", "Sink into Stupor",
]


def names_from_deck(raw: bytes) -> list[str]:
    result = []
    for row in raw.decode("utf-8").splitlines():
        qty, name = row.split("x ", 1)
        assert qty.isdigit()
        result.append(name.removesuffix(" [Commander]"))
    return list(dict.fromkeys(result))


def fetch_group(names: list[str]) -> tuple[list[dict], list[dict]]:
    payload = json.dumps({"identifiers": [{"name": name} for name in names]}).encode()
    req = Request(
        "https://api.scryfall.com/cards/collection",
        data=payload,
        method="POST",
        headers={"Content-Type": "application/json", "Accept": "application/json",
                 "User-Agent": "GrixisEncyclopediaDeck39/1.0 (deck source validation)"},
    )
    try:
        with urlopen(req, timeout=30) as stream:
            data = json.load(stream)
    except HTTPError as exc:
        raise RuntimeError(f"Scryfall HTTP {exc.code}: {exc.read().decode('utf-8', errors='replace')}") from exc
    return data["data"], data.get("not_found", [])


def main() -> None:
    raw = BASELINE.read_bytes()
    baseline_names = names_from_deck(raw)
    all_names = list(dict.fromkeys(baseline_names + CHALLENGERS))
    cards = []
    missed = []
    for i in range(0, len(all_names), 75):
        new_cards, not_found = fetch_group(all_names[i:i+75])
        for card in new_cards:
            faces = card.get("card_faces", [])
            cards.append({
                "name": card["name"], "oracle_id": card.get("oracle_id"),
                "oracle_text": card.get("oracle_text", ""),
                "mana_cost": card.get("mana_cost", ""),
                "cmc": card.get("cmc"), "type_line": card.get("type_line"),
                "color_identity": card["color_identity"],
                "commander_legality": card["legalities"]["commander"],
                "released_at": card.get("released_at"),
                "faces": [{"name": f.get("name"), "oracle_text": f.get("oracle_text", ""),
                           "type_line": f.get("type_line", "")} for f in faces],
            })
        missed.extend(not_found)
    by_name = {c["name"]: c for c in cards}
    # Print diagnostics without equating a name match with a deeper rules proof.
    summary = {
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "source": "https://api.scryfall.com/cards/collection",
        "baseline_path": str(BASELINE.relative_to(ROOT)),
        "baseline_sha256": hashlib.sha256(raw).hexdigest(),
        "baseline_card_names": baseline_names,
        "challenger_names": CHALLENGERS,
        "missing_baseline": sorted(set(baseline_names) - set(by_name)),
        "not_found": missed,
        "cards": sorted(cards, key=lambda c: c["name"]),
    }
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Oracle source", DEST)
    print("baseline card names", len(baseline_names), "total retrieved", len(cards))
    print("missing baseline", summary["missing_baseline"], "not found", missed)
    print("baseline SHA", summary["baseline_sha256"])


if __name__ == "__main__":
    main()
