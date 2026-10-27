"""Local-only historical Oracle snapshot coverage checker for Norman M7.

Never transmits a decklist or card names. Historical snapshots are evidence,
not an assertion of live Scryfall verification or rules-engine correctness.
"""

import argparse
import collections
import hashlib
import json
import pathlib


def lookup():
    found = {}
    repo_root = pathlib.Path(__file__).resolve().parents[4]
    for folder in (repo_root / "data/grixis/m7/oracle_snapshots", repo_root / "data/grixis/m6/oracle_snapshots"):
        for path in folder.glob("*.json"):
            try:
                snapshot = json.loads(path.read_text())
            except (ValueError, UnicodeError):
                continue
            items = snapshot.get("cards", []) if isinstance(snapshot, dict) else []
            for card in items:
                if not isinstance(card, dict) or "name" not in card:
                    continue
                found.setdefault(card["name"].casefold(), (card, str(path.relative_to(repo_root))))
    return found


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("list_path", type=pathlib.Path)
    parser.add_argument("--detail", nargs="*", default=[])
    arguments = parser.parse_args()
    raw = arguments.list_path.read_bytes()
    lines = raw.decode("utf-8").splitlines()
    names = []
    for row in lines:
        if row.startswith("1x "):
            name = row[3:]
        elif row.startswith("1 "):
            name = row[2:]
        else:
            raise ValueError(f"Expected one-card row: {row!r}")
        names.append(name.replace(" [Commander]", ""))
    normalized = [name.casefold() for name in names]
    counts = collections.Counter(normalized)
    duplicates = {name: qty for name, qty in counts.items() if qty > 1}
    cards = lookup()
    invalid = []
    lands = []
    for name in names:
        hit = cards.get(name.casefold())
        card = hit[0] if hit else None
        if card is None:
            # Scryfall may return another canonical face/name for some alias prints.
            card = next((c for c, _ in cards.values() if c["name"].casefold() == name.casefold()), None)
        if card is None:
            invalid.append((name, "unresolved"))
            continue
        legality = card.get("commander_legality", card.get("legalities", {}).get("commander"))
        if legality != "legal":
            invalid.append((name, f"historical Commander status {legality}"))
        identity = set(card.get("color_identity", []))
        if not identity <= {"U", "B", "R"}:
            invalid.append((name, f"color identity {sorted(identity)}"))
        if "Land" in card.get("type_line", "").split(" // ")[0]:
            lands.append(name)
    for name in arguments.detail:
        hit = cards.get(name.casefold())
        if hit is not None:
            card, path = hit
            print(json.dumps({"snapshot": path, **{k: card.get(k) for k in ("name", "mana_cost", "oracle_text", "type_line", "color_identity", "commander_legality")}}, indent=2))
    print(json.dumps({
        "sha256_raw": hashlib.sha256(raw).hexdigest(),
        "count": len(lines), "unique": len(counts), "duplicates": duplicates,
        "lands": len(lands), "unresolved_or_illegal_in_local_snapshots": invalid,
        "covered_from_historical_snapshots": len(lines) - len(invalid),
        "source": "LOCAL_ARCHIVE_ONLY_NOT_LIVE_ORACLE_VERIFICATION",
    }, indent=2))
    if len(lines) != 100 or duplicates or not lines[0].endswith(" [Commander]"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
