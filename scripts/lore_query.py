#!/usr/bin/env python3
"""One small command interface for the repo's lore-first retrieval tools.

Examples (from repository root):
  python3 scripts/lore_query.py set lea --limit 5
  python3 scripts/lore_query.py card "Urza's Saga" --limit 5
  python3 scripts/lore_query.py flavor "Urza" --set atq --limit 5
  python3 scripts/lore_query.py lore "Karn" --limit 5
  python3 scripts/lore_query.py timeline ar
  python3 scripts/lore_query.py timeline omenpaths
  python3 scripts/lore_query.py candidates "Urza" --limit 30

JSON is the default for ChatGPT scripts; --human gives a concise readable view.
Scryfall export covers English/default-language printings, not all translations.
Contextual links and literal flavor mentions are not proof of a story event.
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import export_printing_lore as P
import lore_evidence as E

TIMELINE_SECTIONS = {
    "ar": "Dated events (AR)",
    "postmending": "Post-Mending (Gatewatch era)",
    "invasion": "Phyrexian Invasion",
    "omenpaths": "Omenpath era (post-invasion)",
}
TIMELINE_METHODS = {
    "ar": "explicit_AR_years_as_printed_in_cited_official_stories",
    "postmending": "editorial_publication_order_not_guaranteed_in_world",
    "invasion": "editorial_phase_sequence_with_story_sources",
    "omenpaths": "relative_markers_only_not_a_total_order",
}
URL_RX = re.compile(r"https://magic\.wizards\.com/[^\s)]+")


def timeline_view(markdown, scope):
    """Extract existing, source-labeled timeline rows without inventing dates."""
    if scope not in TIMELINE_SECTIONS:
        raise ValueError(f"unknown timeline scope: {scope}")
    heading = TIMELINE_SECTIONS[scope]
    marker = f"### {heading}\n"
    start = markdown.find(marker)
    if start < 0:
        raise ValueError(f"missing timeline section: {heading}")
    tail = markdown[start + len(marker):]
    end = re.search(r"^#{2,3} ", tail, re.M)
    section = tail[:end.start()] if end else tail
    rows = []
    for line in section.splitlines():
        if not line.startswith("|") or re.match(r"^\|\s*:?[-]+", line):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 3:
            continue
        first = cols[0].replace("**", "")
        if scope == "ar":
            match = re.fullmatch(r"(\d+) AR", first)
            if not match:
                continue
            sort_key = int(match.group(1))
        elif scope in ("postmending", "invasion"):
            if not re.fullmatch(r"\d+[a-z]?", first):
                continue
            sort_key = first
        else:
            if first.casefold().startswith("relative marker"):
                continue
            sort_key = None
        source_urls = sorted(set(u.rstrip(".,;") for u in URL_RX.findall(line)))
        rows.append({"marker": first, "cells_markdown": cols[1:],
                     "official_sources_on_row": source_urls,
                     "source_anchor": "Master Timeline.md#" + re.sub(r"[^a-z0-9 -]", "", heading.casefold()).replace(" ", "-"),
                     "verified_date": sort_key if scope == "ar" else None,
                     "qualification": "Row is transcribed from curated timeline; the cited official source must be checked for disputed details."})
    if scope == "ar":
        rows.sort(key=lambda r: r["verified_date"])
    return {"scope": scope, "ordering_rule": TIMELINE_METHODS[scope],
            "chronological": scope == "ar", "rows": rows, "count": len(rows)}


def card_printings(name, archive, limit=30):
    """Find every edition of a named card, preserving distinct flavor variants."""
    if not name.strip():
        raise ValueError("card name is empty")
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    manifest = json.loads((archive / "manifest.json").read_text(encoding="utf-8"))
    total = 0
    distinct_flavors = set()
    out = []
    for shard in sorted(manifest["shards"]):
        with (archive / shard).open(encoding="utf-8") as handle:
            for line in handle:
                row = json.loads(line)
                if row.get("l") != "en" or not row.get("p"):
                    continue
                if name.casefold() not in (row["n"].casefold(), *[f["n"].casefold() for f in row.get("faces", [])]):
                    continue
                total += 1
                distinct_flavors.update(f["f"] for f in row.get("faces", []) if f.get("f"))
                if len(out) < limit:
                    out.append(row)
    return {"query": name, "printings": total, "distinct_flavor_texts": len(distinct_flavors),
            "flavor_variants": sorted(distinct_flavors), "shown": len(out), "items": out,
            "source": manifest.get("source"), "coverage": manifest.get("coverage")}


def story_candidates(term, data, evidence, limit=30):
    """Retrieval-only candidate pool. No card is called canon-depicting by default."""
    matched = [e for e in data["items"] if e["name"].casefold() == term.casefold()]
    if not matched:
        matched = [e for e in data["items"] if term.casefold() in e["name"].casefold()]
    by_card = defaultdict(lambda: {"evidence": [], "sources": set(), "rank": 9})
    for entry in matched:
        source = f"{entry['page']}#{entry['anchor']}"
        for name in entry.get("enriched_cards", []):
            record = by_card[name]
            record["rank"] = min(record["rank"], 2)
            record["evidence"].append("curated_enrichment_contextual_not_depiction_proof")
            record["sources"].add(source)
        for card_path in entry.get("links", {}).get("cards", []):
            record = by_card[card_path]
            record["rank"] = 1
            record["evidence"].append("explicit_card_page_link_in_lore_entry")
            record["sources"].add(source)
    for printing in evidence["printing_text"]["printings"]:
        name = printing["card"]
        record = by_card[name]
        record["rank"] = min(record["rank"], 3)
        record["evidence"].append("literal_printed_flavor_or_chapter_mention")
        record["sources"].add(printing.get("source_url") or f"{printing['set']}#{printing['collector_number']}")
    cards = [{"card_or_reference": name, "rank": item["rank"],
              "evidence": sorted(set(item["evidence"])), "sources": sorted(item["sources"])}
             for name, item in by_card.items()]
    cards.sort(key=lambda x: (x["rank"], x["card_or_reference"].casefold()))
    return {"theme": term, "total_candidates_in_sample": len(cards), "candidates": cards[:limit],
            "ranking": "explicit link > curated enrichment > literal text mention; not deck-power ranking",
            "warning": "Candidate list is not a deck and makes no unverified chronology or legality claims."}


def run(args):
    archive = args.archive
    if args.action == "set":
        return P.lookup(archive, args.term, None, limit=args.limit)
    if args.action == "card":
        return card_printings(args.term, archive, args.limit)
    if args.action == "flavor":
        return E.printing_matches(args.term, archive, args.sets, args.limit)
    if args.action == "timeline":
        return timeline_view(args.timeline.read_text(encoding="utf-8"), args.scope)
    if args.action in ("lore", "candidates"):
        import lore_lib as L
        evidence = E.lookup(args.term, archive, L.all_entries(), args.sets, args.limit)
        if args.action == "lore":
            return evidence
        data = json.loads((ROOT / "data" / "lore_entries.json").read_text(encoding="utf-8"))
        return story_candidates(args.term, data, evidence, args.limit)
    raise ValueError(f"unsupported action {args.action}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=ROOT / "data" / "printing_lore")
    parser.add_argument("--timeline", type=Path, default=ROOT / "Master Timeline.md")
    parser.add_argument("--human", action="store_true")
    sub = parser.add_subparsers(dest="action", required=True)
    for action in ("set", "card", "flavor", "lore", "candidates"):
        p = sub.add_parser(action)
        p.add_argument("term")
        p.add_argument("--limit", type=int, default=30)
        if action in ("flavor", "lore", "candidates"):
            p.add_argument("--set", dest="sets", action="append", default=[])
    t = sub.add_parser("timeline")
    t.add_argument("scope", choices=list(TIMELINE_SECTIONS))
    args = parser.parse_args(argv)
    try:
        result = run(args)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    if args.human:
        if args.action == "timeline":
            print(f"{args.scope}: {result['count']} source-labeled events ({result['ordering_rule']})")
            for row in result["rows"]:
                print(f"  {row['marker']}: {row['cells_markdown'][0]}")
        elif args.action == "candidates":
            for row in result["candidates"]:
                print(f"  {row['rank']}. {row['card_or_reference']} [{', '.join(row['evidence'])}]")
        else:
            print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
