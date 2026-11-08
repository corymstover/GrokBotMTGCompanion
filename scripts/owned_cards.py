#!/usr/bin/env python3
"""Offline owned-card lookup: Oracle, mana, identity, rarities, Pauper, rulings.

Read a dated, separately sourced personal catalogue; never treat it as a
replacement for the repository's historical canonical Oracle snapshots.
"""

import argparse
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATADIR = ROOT / "data" / "physical_collection" / "owned_cards" / "2026-11-08"
MANIFEST = DATADIR / "manifest.json"


class OwnedCards:
    def __init__(self):
        self.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.names = {name.casefold(): name for name in self.manifest["name_to_shard"]}
        self._shards = {}

    def get(self, name):
        actual = self.names.get(name.strip().casefold())
        if not actual:
            return None
        filename = self.manifest["name_to_shard"][actual]
        if filename not in self._shards:
            self._shards[filename] = json.loads((DATADIR / filename).read_text(encoding="utf-8"))["cards"]
        return self._shards[filename][actual]

    def records(self):
        for name in sorted(self.manifest["name_to_shard"], key=str.casefold):
            yield self.get(name)


def eligible(card, available, colors, pauper, type_filter, needle):
    if available and card["copies_available"] < 1:
        return False
    if colors is not None and not set(card["color_identity"]).issubset(set(colors)):
        return False
    if pauper and card["legalities"].get("pauper") != "legal":
        return False
    if type_filter and type_filter.casefold() not in card["type_line"].casefold():
        return False
    haystack = " ".join([card["name"], card.get("oracle_text") or "",
                         card.get("type_line") or "", *card.get("keywords", []),
                         *(f.get("oracle_text") or "" for f in card["card_faces"])])
    return needle.casefold() in haystack.casefold()


def short_line(card):
    cost = card.get("mana_cost") or "/".join(f.get("mana_cost", "") for f in card["card_faces"])
    identity = "".join(card["color_identity"]) or "C"
    return (f"{card['name']} | {cost or '—'} | MV {card['mana_value']} | "
            f"identity {identity} | owned {card['copies_owned']} / free {card['copies_available']} | "
            f"Pauper {card['legalities'].get('pauper')}" +
            (" | PRE-RELEASE" if card["future_only"] else ""))


def detail(card, as_of):
    print(short_line(card))
    print(f"Type: {card['type_line']} | colors: {','.join(card['colors']) or 'colorless'}")
    print(f"Oracle ID: {card['oracle_id']}")
    if card["card_faces"]:
        for i, face in enumerate(card["card_faces"], 1):
            print(f"Face {i}: {face['name']} ({face.get('mana_cost', '')}) · {face.get('type_line', '')}")
            print(face.get("oracle_text", "(no rules text)"))
    else:
        print("Oracle text:\n" + (card.get("oracle_text") or "(no rules text)"))
    print("Keywords: " + (", ".join(card["keywords"]) or "none listed"))
    print(f"Printings examined: {card['printings_count']}; observed rarities: "
          + ", ".join(card["all_recorded_rarities"]))
    print(f"Representative printing ({card['representative_set']}): "
          f"{card['representative_printing_rarity']}; your owned printing is NOT identified")
    if card["regular_common_printings"]:
        sample = card["regular_common_printings"][0]
        print(f"Historical regular common example: {sample['set'].upper()} #{sample['collector_number']}")
    print(f"Pauper as of {as_of}: {card['legalities'].get('pauper')} "
          f"(not inferred from one printing's rarity)")
    print(f"Commander as of {as_of}: {card['legalities'].get('commander')}")
    if card["future_only"]:
        print("CAUTION: No generally released printing by the snapshot date; "
              "prerelease ownership is not proof of constructed legality.")
    if "published_rulings" in card:
        print(f"Cached newer published rulings: {len(card['published_rulings'])}")
        for ruling in card["published_rulings"]:
            print(f"- {ruling['published_at']}: {ruling['comment']}")
    else:
        print(f"Rulings in older repository shard: {card.get('original_ruling_count', 'not indexed')}")
    print("Current rulings: " + (card.get("rulings_uri") or "not supplied"))
    print("All printing details: " + (card.get("prints_search_uri") or "not supplied"))
    if card.get("original_shard"):
        print("Original repository card shard: " + card["original_shard"])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    pcard = sub.add_parser("card", help="Look up one owned card's complete details")
    pcard.add_argument("name")
    pcard.add_argument("--json", action="store_true")
    for cmd in ("find", "pauper"):
        p = sub.add_parser(cmd, help="Search owned Oracle text/names or list Pauper-legal cards")
        if cmd == "find":
            p.add_argument("text", help="Substring to search across Oracle text, types and names")
        p.add_argument("--available", action="store_true", help="Exclude cards reserved in Xander or Dihada")
        p.add_argument("--colors", help="Filter cards usable in a color identity, e.g. WB or GUR")
        p.add_argument("--type", help="Filter printed type line, e.g. Creature or Instant")
        p.add_argument("--pauper", action="store_true", help="Limit to currently Pauper-legal cards")
        p.add_argument("--limit", type=int, default=40)
    sub.add_parser("stats", help="Summarize coverage and supported availability")
    args = ap.parse_args()
    db = OwnedCards()
    if args.cmd == "card":
        card = db.get(args.name)
        if not card:
            ap.error(f"Not owned or not in this dated snapshot: {args.name}")
        if args.json:
            print(json.dumps(card, indent=2, ensure_ascii=False))
        else:
            detail(card, db.manifest["as_of_date"])
        return
    if args.cmd == "stats":
        all_cards = list(db.records())
        print(f"Snapshot: {db.manifest['as_of_date']}; "
              f"owned {sum(c['copies_owned'] for c in all_cards)} copies / {len(all_cards)} names")
        print(f"Available: {sum(c['copies_available'] for c in all_cards)} copies / "
              f"{sum(bool(c['copies_available']) for c in all_cards)} names")
        print(f"Pauper legal now: {sum(c['legalities']['pauper']=='legal' for c in all_cards)} names; "
              f"available: {sum(c['legalities']['pauper']=='legal' and c['copies_available']>0 for c in all_cards)}")
        print(f"Not released generally by snapshot date: {sum(c['future_only'] for c in all_cards)} names")
        print(f"Index gaps covered by this catalogue: {db.manifest['index_coverage']['missing']}")
        print("Representative-printing rarity distribution: " +
              str(dict(Counter(c['representative_printing_rarity'] for c in all_cards))))
        return
    colors = args.colors.upper() if args.colors else None
    if colors is not None and set(colors) - set("WUBRG"):
        ap.error("--colors must use only W U B R G color-identity letters")
    if args.limit < 1:
        ap.error("--limit must be at least 1")
    matching = [c for c in db.records() if eligible(
        c, args.available, colors, args.pauper or args.cmd == "pauper",
        args.type, args.text if args.cmd == "find" else "")]
    print(f"{len(matching)} matching owned names (showing {min(args.limit, len(matching))})")
    for card in matching[:args.limit]:
        print(short_line(card))


if __name__ == "__main__":
    main()
