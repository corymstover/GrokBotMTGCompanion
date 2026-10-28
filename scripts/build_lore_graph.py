#!/usr/bin/env python3
"""Build a conservative, provenance-preserving lore navigation graph.

Input is the already curated data/lore_entries.json. Its links are editorial
cross-references, NOT proof of a specific historical claim or chronology.
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path


def build(source):
    data = json.loads(Path(source).read_text(encoding="utf-8"))
    items = data["items"]
    nodes = {}
    for item in items:
        key = f"{item['page']}#{item['anchor']}"
        if key in nodes:
            raise ValueError(f"duplicate lore node: {key}")
        nodes[key] = {
            "id": key, "kind": item["kind"], "name": item["name"],
            "tags": item.get("tags", []), "flags": item.get("flags", {}),
            "citations_on_page": item.get("citations", 0),
        }

    edges = {}
    for item in items:
        source_id = f"{item['page']}#{item['anchor']}"
        for category, destinations in item.get("links", {}).items():
            for target_id in destinations:
                # A curated link is a navigational association. Even if a
                # page has citations, they do not automatically prove a link.
                kind = "entry_cross_reference" if target_id in nodes else "card_page_reference" if target_id.startswith("cards/") else "external_page_reference"
                key = (source_id, target_id, kind)
                edges[key] = {
                    "from": source_id, "to": target_id, "relation": kind,
                    "link_group": category,
                    "evidence": {"tier": "contextual_pointer", "source_entry": source_id,
                                 "verification": "linked_in_curated_lore_index"},
                }

    # Add browseable card nodes but never infer that they depict the event.
    for edge in edges.values():
        target = edge["to"]
        if target not in nodes:
            nodes[target] = {"id": target, "kind": "card_reference" if target.startswith("cards/") else "page_reference",
                             "name": target.rsplit("#", 1)[-1].replace("-", " "), "tags": [], "flags": {}, "citations_on_page": 0}
    return {
        "schema": "lore-evidence-graph/v1",
        "meaning": "Cross-references support navigation, not unqualified canon assertions.",
        "evidence_tiers": {"contextual_pointer": "Curated source links to target; relationship and chronology are not independently verified.",
                           "direct_official": "Reserved for an exact, independently verified official citation (not auto-assigned).",
                           "thematic_inference": "Reserved for explicitly labeled creative deckbuilding suggestions (not auto-assigned)."},
        "nodes": [nodes[k] for k in sorted(nodes)],
        "edges": [edges[k] for k in sorted(edges)],
        "stats": {"lore_entries": len(items), "total_nodes": len(nodes), "directed_edges": len(edges),
                  "card_references": sum(n["kind"] == "card_reference" for n in nodes.values())},
    }


def search(graph, term, limit):
    term = term.casefold()
    nodes = {n["id"]: n for n in graph["nodes"]}
    matched = [n for n in graph["nodes"] if term in n["name"].casefold() or term in n["id"].casefold()]
    result = []
    for node in matched[:limit]:
        edges = [e for e in graph["edges"] if e["from"] == node["id"] or e["to"] == node["id"]]
        neighbors = []
        for edge in edges[:50]:
            other = edge["to"] if edge["from"] == node["id"] else edge["from"]
            neighbors.append({"id": other, "name": nodes.get(other, {}).get("name", other),
                              "relation": edge["relation"], "evidence": edge["evidence"]["tier"]})
        result.append({"node": node, "connections": neighbors, "connection_count": len(edges)})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["build", "check", "search", "stats"])
    parser.add_argument("term", nargs="?", default="")
    parser.add_argument("--input", type=Path, default=Path("data/lore_entries.json"))
    parser.add_argument("--output", type=Path, default=Path("data/lore_graph.json"))
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    if args.command in ("build", "check"):
        graph = build(args.input)
        payload = json.dumps(graph, ensure_ascii=False, sort_keys=True, indent=1) + "\n"
        if args.command == "check":
            if not args.output.exists() or args.output.read_text(encoding="utf-8") != payload:
                parser.error("graph stale: run build")
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(payload, encoding="utf-8")
        print(json.dumps(graph["stats"], indent=2))
    else:
        graph = json.loads(args.output.read_text(encoding="utf-8"))
        print(json.dumps(graph["stats"] if args.command == "stats" else search(graph, args.term, args.limit), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
