#!/usr/bin/env python3
"""Source-aware lore lookup: official story citations + exact printed flavor mentions.

Usage (from repository root):
    python3 scripts/lore_evidence.py Urza --set atq --json
    python3 scripts/lore_evidence.py "Chain Veil" --json

This is a *retrieval tool*, not a factual relationship classifier. The Scryfall
flavor text proves a printing contains words, NOT that an event took place.
Official URLs are cited in the lore entry; they are not automatically asserted
as proof of every related card. Nothing edits the 62 Grixis decklists.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))


def printing_matches(term, archive, sets=(), limit=30, *, paper_english=True):
    """Stream compact committed printing shards; optional set narrows I/O."""
    if not term.strip():
        raise ValueError("search phrase is empty")
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    manifest = json.loads((archive / "manifest.json").read_text(encoding="utf-8"))
    set_map = manifest["sets"]
    unknown = sorted(set(sets) - set(set_map))
    if unknown:
        raise ValueError(f"unknown set codes: {', '.join(unknown)}")
    files = sorted({f for s in sets for f in set_map[s]["files"]}) if sets else sorted(manifest["shards"])
    rx = re.compile(r"(?<![\w])" + re.escape(term) + r"(?![\w])", re.IGNORECASE)
    found = []
    total = 0
    by_field = {"printed_flavor": 0, "saga_chapter_oracle": 0}
    for file in files:
        with (archive / file).open(encoding="utf-8") as handle:
            for line in handle:
                row = json.loads(line)
                if sets and row["s"] not in sets:
                    continue
                if paper_english and (row.get("l") != "en" or not row.get("p")):
                    continue
                for face_number, face in enumerate(row.get("faces", [])):
                    for key, label in (("f", "printed_flavor"), ("chapters", "saga_chapter_oracle")):
                        value = face.get(key, "")
                        if not rx.search(value):
                            continue
                        total += 1
                        by_field[label] += 1
                        if len(found) < limit:
                            found.append({
                                "printing_id": row["id"], "oracle_id": row.get("o"),
                                "card": row["n"], "face": face.get("n"), "face_index": face_number,
                                "set": row["s"], "collector_number": row["c"],
                                "released_at": row.get("r"), "source_url": row.get("url"),
                                "field": label, "verbatim": value,
                                "evidence": "literal_printing_text_match",
                                "interpretation": "textual mention only; lore relationship not independently confirmed",
                            })
    return {"total_matches": total, "matches_by_field": by_field, "shown": len(found),
            "truncated": total > len(found), "printings": found,
            "source": manifest.get("source"), "coverage": manifest.get("coverage")}


def lore_sources(term, entries):
    """Match named entities; preserve each entry's official URLs and caveats."""
    import lore_lib as L
    t = term.casefold()
    matched = [e for e in entries if e["name"].casefold() == t]
    if not matched:
        matched = [e for e in entries if t in e["name"].casefold()]
    result = []
    for entry in matched[:20]:
        urls = L.official_urls(entry["text"])
        result.append({
            "id": f"{entry['page']}#{entry['anchor']}", "kind": entry["kind"],
            "name": entry["name"], "official_citations": urls,
            "evidence": "official_urls_cited_in_entry",
            "interpretation": "citations document the entry; not necessarily each linked card",
            "uncertainty_markers": L.flags(entry["text"]),
        })
    return result


def graph_context(term, path, limit=25):
    """Navigate curated links, but keep their contextual evidence tier intact."""
    if not path.exists():
        return []
    graph = json.loads(path.read_text(encoding="utf-8"))
    nodes = {n["id"]: n for n in graph["nodes"]}
    matches = [n for n in nodes.values() if n["name"].casefold() == term.casefold()]
    if not matches:
        matches = [n for n in nodes.values() if term.casefold() in n["name"].casefold()]
    result = []
    for node in matches[:10]:
        edges = [e for e in graph["edges"] if e["from"] == node["id"] or e["to"] == node["id"]]
        links = []
        for edge in edges[:limit]:
            target = edge["to"] if edge["from"] == node["id"] else edge["from"]
            links.append({"name": nodes.get(target, {}).get("name", target), "id": target,
                          "relation": edge["relation"], "evidence": edge["evidence"]["tier"]})
        result.append({"node": node["id"], "total_connections": len(edges), "connections": links})
    return result


def lookup(term, archive, entries, sets=(), limit=30, graph_path=None):
    lore = lore_sources(term, entries)
    printings = printing_matches(term, archive, sets, limit)
    # Name-identical entities only: a broad partial text search is not
    # grounds for linking a particular printing to a particular lore person.
    exact = [e for e in lore if e["name"].casefold() == term.casefold()]
    mention_edges = [{
        "from": f"printing:{p['printing_id']}:{p['face_index']}:{p['field']}",
        "to": entity["id"], "relation": "literal_printed_name_mention",
        "evidence": {"tier": "literal_printing_text_match", "field": p["field"],
                     "printing_url": p["source_url"], "verbatim": p["verbatim"]},
        "qualification": "a printed name/phrase mention does not by itself establish a story relationship",
    } for entity in exact for p in printings["printings"]]
    return {"query": term, "lore_entries": lore,
            "graph_context": graph_context(term, graph_path or ROOT / "data" / "lore_graph.json"),
            "printing_text": printings, "printing_lore_edges": mention_edges}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("term", help="literal flavor-text phrase and entity name")
    parser.add_argument("--set", action="append", dest="sets", default=[],
                        help="optional set code (repeatable); e.g. --set atq")
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--archive", type=Path, default=ROOT / "data" / "printing_lore")
    parser.add_argument("--json", action="store_true", help="stable machine-readable output")
    args = parser.parse_args(argv)
    import lore_lib as L
    try:
        result = lookup(args.term, args.archive, L.all_entries(), args.sets, args.limit)
    except (OSError, ValueError) as e:
        parser.error(str(e))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    print(f"{args.term}: {len(result['lore_entries'])} lore entries; "
          f"{result['printing_text']['total_matches']} printing-text matches "
          f"({result['printing_text']['shown']} shown)")
    for context in result["graph_context"]:
        print(f"  Graph: {context['node']} — {context['total_connections']} contextual links")
        for link in context["connections"][:10]:
            print(f"    {link['name']} [{link['evidence']}]")
    for e in result["lore_entries"]:
        print(f"  {e['name']} [{e['kind']}] — {e['id']}")
        for url in e["official_citations"][:8]:
            print(f"    cited: {url}")
    for card in result["printing_text"]["printings"]:
        print(f"  {card['set'].upper()} #{card['collector_number']} {card['card']} "
              f"[{card['field']}] — {card['source_url']}")
        print(f"    {card['verbatim']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
