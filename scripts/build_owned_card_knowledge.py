#!/usr/bin/env python3
"""Build a small, source-provenanced catalogue of *only* Cory's owned cards.

Read Scryfall's official compressed `default-cards` JSONL bulk export locally.
Never overwrite the repository-wide pinned Oracle shards or download a bulk
file implicitly. The source gzip is an input, not a repository artifact.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COLLECTION = ROOT / "data" / "physical_collection"
SNAP = COLLECTION / "2026-11-08"
OUTDIR = COLLECTION / "owned_cards" / "2026-11-08"
MANIFEST = OUTDIR / "manifest.json"
RULINGS_CACHE = OUTDIR / "recent_rulings.json"
INDEX = ROOT / "data" / "card_index.csv"


def read_counts(path: Path) -> dict[str, int]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return {r["Name"]: int(r["Quantity"]) for r in csv.DictReader(f)}


def file_hash(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def _section(shard_path: Path, name: str) -> str | None:
    content = shard_path.read_text(encoding="utf-8")
    match = re.search(r"^### " + re.escape(name) + r"\s*$(.*?)(?=^### |\Z)",
                      content, re.M | re.S)
    return match.group(1) if match else None


def _oracle_from_shard(section: str, is_multiface: bool) -> str | None:
    if is_multiface:
        # Face text is arranged in separate Markdown entries; parsing must not
        # silently flatten their separate costs and characteristics.
        return None
    match = re.search(r"^- \*\*Oracle text:\*\*\s*$\n((?:\s+>.*\n?)*)", section, re.M)
    if not match:
        return None
    result = "\n".join(line.strip()[2:].strip() for line in match.group(1).splitlines()
                       if line.strip().startswith("> "))
    return "" if result == "*(no rules text)*" else result


def _face_summary(face: dict) -> dict:
    return {key: face[key] for key in (
        "name", "mana_cost", "type_line", "oracle_text", "colors", "power",
        "toughness", "loyalty", "defense", "flavor_text") if key in face}


def build(bulk_path: Path, updated_at: str, as_of: str) -> dict:
    owned = read_counts(SNAP / "master_inventory.csv")
    free = read_counts(COLLECTION / "current_available.csv")
    with INDEX.open(encoding="utf-8", newline="") as f:
        old = {r["name"]: r for r in csv.DictReader(f) if r["name"] in owned}
    if len(owned) != 751 or sum(owned.values()) != 1332 or sum(free.values()) != 1131:
        raise ValueError("Source inventory no longer matches verified November 8 snapshot")
    if set(free) - set(owned):
        raise ValueError("Available pool contains a card not in the master inventory")

    matched: dict[str, list[dict]] = defaultdict(list)
    total_rows = 0
    with gzip.open(bulk_path, "rt", encoding="utf-8") as f:
        for line in f:
            total_rows += 1
            card = json.loads(line)
            name = card.get("name", "")
            if name in owned and card.get("lang") == "en":
                matched[name].append(card)
    missing = sorted(set(owned) - set(matched))
    if missing:
        raise ValueError("Some owned cards could not be identified in the chosen Scryfall bulk: "
                         + ", ".join(missing))

    records = {}
    drift = defaultdict(list)
    excluded_memorabilia_names = []
    shards: dict[str, str] = {}
    today = date.fromisoformat(as_of)
    for name in sorted(owned, key=str.casefold):
        # Promotional theme cards and non-playable 30th Anniversary facsimiles
        # cannot independently confer Pauper legality by being marked common.
        candidates = [c for c in matched[name] if c.get("set_type") != "memorabilia"
                      and c.get("type_line") != "Card" and c.get("oracle_id")]
        if not candidates:
            raise ValueError(f"No regular playable printing for owned name: {name}")
        source_id = old.get(name, {}).get("oracle_id")
        group_sizes = Counter(c["oracle_id"] for c in candidates if "paper" in c.get("games", []))
        group_sizes += Counter(c["oracle_id"] for c in candidates)
        oracle_id = source_id if source_id in group_sizes else group_sizes.most_common(1)[0][0]
        valid = [c for c in candidates if c["oracle_id"] == oracle_id]
        releases = [c for c in valid if c.get("released_at", "9999") <= as_of]
        available_prints = [c for c in releases if "paper" in c.get("games", [])]
        pool = available_prints or releases or valid
        representative = max(pool, key=lambda c: (c.get("released_at", ""),
                                                   "paper" in c.get("games", []),
                                                   c.get("id", "")))
        future_only = not releases
        printings = sorted(({key: c[key] for key in (
            "set", "collector_number", "released_at", "rarity", "games") if key in c}
                            for c in valid), key=lambda c: (
                                c.get("released_at", ""), c.get("set", ""),
                                c.get("collector_number", "")))
        common_examples = [p for p in printings if p["rarity"] == "common"
                           and (set(p.get("games", [])) & {"paper", "mtgo"})]
        c = representative
        record = {
            "name": name,
            "copies_owned": owned[name],
            "copies_available": free.get(name, 0),
            "copies_reserved": owned[name] - free.get(name, 0),
            "oracle_id": oracle_id,
            "representative_printing_id": c["id"],
            "representative_set": c.get("set"),
            "representative_printing_rarity": c.get("rarity"),
            "representative_release_date": c.get("released_at"),
            "future_only": future_only,
            "layout": c.get("layout"),
            "mana_cost": c.get("mana_cost", ""),
            "mana_value": c.get("cmc"),
            "colors": c.get("colors", []),
            "color_identity": c.get("color_identity", []),
            "type_line": c.get("type_line"),
            "oracle_text": c.get("oracle_text"),
            "card_faces": [_face_summary(f) for f in c.get("card_faces", [])],
            "keywords": c.get("keywords", []),
            "produced_mana": c.get("produced_mana", []),
            "power": c.get("power"),
            "toughness": c.get("toughness"),
            "loyalty": c.get("loyalty"),
            "defense": c.get("defense"),
            "legalities": c.get("legalities", {}),
            "game_changer": bool(c.get("game_changer", False)),
            "all_recorded_rarities": sorted({p["rarity"] for p in printings}),
            "has_regular_common_printing": bool(common_examples),
            "regular_common_printings": [
                {k: p[k] for k in ("set", "collector_number", "released_at", "games")}
                for p in common_examples[:8]],
            "printings_count": len(printings),
            "printings_by_rarity": dict(Counter(p["rarity"] for p in printings)),
            "prints_search_uri": c.get("prints_search_uri"),
            "rulings_uri": c.get("rulings_uri"),
            "scryfall_uri": c.get("scryfall_uri"),
        }
        if name in old:
            row = old[name]
            record["original_shard"] = f"{row['shard']}#{row['anchor']}"
            if row["oracle_id"] != oracle_id:
                drift["oracle_id"].append(name)
            if row["type_line"] != record["type_line"]:
                drift["type_line"].append(name)
            original_identity = [] if row["color_identity"] == "C" else sorted(row["color_identity"])
            if original_identity != sorted(record["color_identity"]):
                drift["color_identity"].append(name)
            if row["commander_legality"] != record["legalities"].get("commander"):
                drift["commander_legality"].append(name)
            shard_path = ROOT / row["shard"]
            if row["shard"] not in shards:
                shards[row["shard"]] = shard_path.read_text(encoding="utf-8")
            match = re.search(r"^### " + re.escape(name) + r"\s*$(.*?)(?=^### |\Z)",
                              shards[row["shard"]], re.M | re.S)
            if not match:
                drift["missing_shard_section"].append(name)
            else:
                record["original_ruling_count"] = int(re.search(r"- \*\*Rulings\*\* \((\d+)\)", match.group(1)).group(1)) \
                    if re.search(r"- \*\*Rulings\*\* \((\d+)\)", match.group(1)) else 0
                shard_oracle = _oracle_from_shard(match.group(1), bool(record["card_faces"]))
                if (shard_oracle or record["oracle_text"]) and shard_oracle != record["oracle_text"]:
                    drift["oracle_text"].append(name)
        else:
            drift["missing_canonical_index"].append(name)
        # Printings from separately named, non-playable products are *not* a
        # substitute for the official format legality Scryfall reports.
        if len(candidates) != len(matched[name]):
            excluded_memorabilia_names.append(name)
        records[name] = record

    if RULINGS_CACHE.exists():
        cache = json.loads(RULINGS_CACHE.read_text(encoding="utf-8"))
        for name, ruling_list in cache.get("cards", {}).items():
            if name not in records or not isinstance(ruling_list, list):
                raise ValueError(f"Invalid targeted rulings cache entry: {name}")
            records[name]["published_rulings"] = ruling_list

    result = {
        "schema": "mtg-owned-card-knowledge/v1",
        "as_of_date": as_of,
        "source": {
            "authority": "Scryfall default-cards compressed JSONL bulk, not live card API lookups",
            "type": "default_cards",
            "bulk_updated_at": updated_at,
            "bulk_filename": bulk_path.name,
            "bulk_sha256": file_hash(bulk_path),
            "total_printing_rows_scanned": total_rows,
            "source_url": "https://api.scryfall.com/bulk-data/default-cards",
        },
        "inventory": {"owned_names": len(owned), "owned_copies": sum(owned.values()),
                      "available_names": len(free), "available_copies": sum(free.values())},
        "index_coverage": {"present": len(old), "missing": len(owned) - len(old)},
        "drift": {k: sorted(v) for k, v in sorted(drift.items())},
        "memorabilia_or_nonplayable_printing_names_ignored": sorted(excluded_memorabilia_names),
        "caveats": [
            "Physical CSVs list card names and quantities, not owned printing/set/foil/condition.",
            "A card's representative printing rarity is not necessarily the rarity of Cory's copy.",
            "Use current Pauper legality and historical regular common-printing evidence together; special memorabilia does not confer eligibility.",
            "Future-only cards may be available at a prerelease but lack general constructed legality until their release; do not infer permanent bans.",
            "Card-specific rulings and interactions are not exhausted by Oracle text; source rulings links and current CR remain authoritative.",
        ],
        "cards": records,
    }
    return result


def check(data: dict) -> None:
    master = read_counts(SNAP / "master_inventory.csv")
    free = read_counts(COLLECTION / "current_available.csv")
    if set(data["cards"]) != set(master):
        raise ValueError("Owned knowledge coverage does not equal the full master collection")
    for name, card in data["cards"].items():
        if (card["copies_owned"] != master[name]
                or card["copies_available"] != free.get(name, 0)
                or card["copies_reserved"] != master[name] - free.get(name, 0)):
            raise ValueError(f"Owned/current allocation mismatch: {name}")
        if not card["type_line"] or card["mana_value"] is None or not card["oracle_id"]:
            raise ValueError(f"Incomplete structural card identity: {name}")
        if card["oracle_text"] is None and not card["card_faces"] and "Land" not in card["type_line"]:
            raise ValueError(f"No Oracle text or faces for nonland card: {name}")
        if card["printings_count"] < 1 or not card["legalities"].get("pauper"):
            raise ValueError(f"Missing printings or current format status: {name}")
    print(json.dumps({
        "result": "verified", "card_names": len(master),
        "physical_copies": sum(master.values()), "available_copies": sum(free.values()),
        "original_index_missing": data["index_coverage"]["missing"],
        "oracle_drift_candidates": len(data["drift"].get("oracle_text", [])),
        "currently_pauper_legal_names": sum(c["legalities"]["pauper"] == "legal"
                                             for c in data["cards"].values()),
    }))


def save_shards(data: dict) -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    cards = data.pop("cards")
    names = sorted(cards, key=str.casefold)
    listings: dict[str, str] = {}
    shards = []
    for start in range(0, len(names), 20):
        group = names[start:start + 20]
        filename = f"part-{start // 20 + 1:03d}.json"
        payload = {"schema": "mtg-owned-card-shard/v1", "as_of_date": data["as_of_date"],
                   "cards": {name: cards[name] for name in group}}
        blob = (json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
        (OUTDIR / filename).write_bytes(blob)
        listings.update({name: filename for name in group})
        shards.append({"file": filename, "names": len(group),
                       "sha256": hashlib.sha256(blob).hexdigest()})
    data["shards"] = shards
    data["name_to_shard"] = listings
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def load_shards() -> dict:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    cards = {}
    for shard in data["shards"]:
        blob = (OUTDIR / shard["file"]).read_bytes()
        if hashlib.sha256(blob).hexdigest() != shard["sha256"]:
            raise ValueError(f"Modified owned card data shard: {shard['file']}")
        partial = json.loads(blob)
        if len(partial["cards"]) != shard["names"]:
            raise ValueError(f"Shard entry count mismatch: {shard['file']}")
        cards.update(partial["cards"])
    if set(cards) != set(data["name_to_shard"]):
        raise ValueError("Manifest does not index the complete owned card catalogue")
    data["cards"] = cards
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    builder = sub.add_parser("build", help="Generate from a locally downloaded Scryfall gzip")
    builder.add_argument("--bulk", required=True, type=Path)
    builder.add_argument("--updated-at", required=True)
    builder.add_argument("--as-of", default="2026-11-08")
    sub.add_parser("check", help="Verify existing catalogue against owned/current quantities")
    options = parser.parse_args()
    if options.command == "build":
        result = build(options.bulk, options.updated_at, options.as_of)
        check(result)
        save_shards(result)
        check(load_shards())
        print(f"Wrote {MANIFEST.relative_to(ROOT)} and its card shards")
    else:
        check(load_shards())


if __name__ == "__main__":
    main()
