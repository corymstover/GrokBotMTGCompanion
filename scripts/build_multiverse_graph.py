#!/usr/bin/env python3
"""Build the Phase 3 cited Multiverse relationship graph from research-pack JSON.

This script reads only committed research packs and lore-deck proposal evidence; it never
contacts the network.

Inputs are listed in data/multiverse_graph/manifest.json:
- ``claim_packs``: every Phase 4 pack that uses the
  ``entities`` / ``claims`` / ``source_register`` schema (A, A2, A3, ...). Any later pack in
  that shape, such as Pack B or C, joins the graph just by being added to the manifest.
- ``art_match_packs``: Pack A4-style exact art/printing matches.
- ``deck_evidence``: printing-evidence files for lore-deck proposals (unapproved). These
  produce ``proposed_in`` edges only and never canon assertions.
- ``story_caption_packs``: scripts/build_story_art_captions.py atlases. For pages that are
  already a registered graph Source, ``art_captioned_in_story`` edges link the Source to each
  captioned Card (navigation only, never canon assertions).
- ``curated_lore_graph``: data/lore_graph.json. Exact-name bridges to the curated wiki
  entries are labelled ``contextual_pointer`` (navigation only).

Output: data/multiverse_graph/multiverse_graph.json. The output is deterministic: sorted,
with no timestamps, and its content SHA-256 is embedded.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/multiverse_graph/manifest.json"
OUT = ROOT / "data/multiverse_graph/multiverse_graph.json"

# The canon-status vocabulary from Phase 3 of the master workflow, plus the
# OPEN_QUESTION grade already used in Pack A. Nothing outside this vocabulary is allowed.
CANON_STATUSES = {
    "CANON_CONFIRMED": "Stated by a cited Wizards primary source.",
    "CANON_IMPLIED": "Strongly implied by a cited primary source but not stated outright.",
    "CANON_DISPUTED": "Sources or in-story narrators conflict; both accounts are preserved.",
    "OPEN_QUESTION": "Primary sources leave the matter unresolved; do not assert either way.",
    "ALTERNATE_CONTINUITY": "True only inside a separate continuity (e.g. Echoverse).",
    "HYPOTHETICAL": "Creative or deckbuilding connection; never canon.",
}
GRADE_ALIASES = {"DISPUTED": "CANON_DISPUTED"}
NODE_TYPES = {"Character", "Event", "Plane", "Place", "Object", "Faction", "AlternateContinuity",
              "CardTheme", "Concept", "Card", "Source", "Claim", "DeckProposal", "Literal"}
TYPE_PREFIX = {"Character": "character", "Event": "event", "Plane": "plane", "Place": "place",
               "Object": "artifact", "Faction": "faction", "AlternateContinuity": "continuity",
               "CardTheme": "cardtheme", "Concept": "concept", "Card": "card", "Source": "source",
               "Claim": "claim", "DeckProposal": "deck", "Literal": "literal"}
OFFICIAL_HOSTS = ("https://magic.wizards.com/", "https://www.magic.wizards.com/", "https://media.wizards.com/", "https://www.wizards.com/",
                  "https://company.wizards.com/")
INVERSE = {"proposed_in": "proposes", "depicted_by": "depicts", "cited_by": "cites",
           "asserts": "asserted_by", "see_also_curated_entry": "see_also_from_curated_entry",
           "named_on_card": "names_entity"}


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


class Graph:
    def __init__(self) -> None:
        self.nodes: dict[str, dict] = {}
        self.edges: list[dict] = []
        self.local: dict[str, str] = {}   # pack-local entity id -> graph id
        self.problems: list[str] = []

    def add_node(self, gid: str, ntype: str, name: str, origin: str, **extra) -> str:
        if ntype not in NODE_TYPES:
            self.problems.append(f"unknown node type {ntype!r} for {gid}")
        node = self.nodes.get(gid)
        if node is None:
            node = {"id": gid, "type": ntype, "name": name, "origins": []}
            self.nodes[gid] = node
        elif node["type"] != ntype:
            self.problems.append(f"type conflict for {gid}: {node['type']} vs {ntype} ({origin})")
        if origin not in node["origins"]:
            node["origins"].append(origin)
        for k, v in extra.items():
            if v in (None, "", [], {}):
                continue
            if k in node and node[k] != v:
                if isinstance(node[k], list) and isinstance(v, list):
                    node[k] = sorted(set(node[k]) | set(v))
                    continue
                self.problems.append(f"attribute conflict {gid}.{k}: {node[k]!r} vs {v!r}")
            node[k] = v
        return gid

    def entity(self, local_id: str, ntype: str, name: str, origin: str) -> str:
        gid = f"{TYPE_PREFIX.get(ntype, 'entity')}:{local_id}"
        if local_id in self.local and self.local[local_id] != gid:
            self.problems.append(f"entity {local_id} typed inconsistently: {self.local[local_id]} vs {gid}")
        self.local[local_id] = gid
        return self.add_node(gid, ntype, name, origin)

    def resolve(self, token: str, origin: str) -> str:
        token = token.strip()
        if token in self.local:
            return self.local[token]
        by_name = {n["name"].lower(): n["id"] for n in self.nodes.values()
                   if n["type"] not in {"Claim", "Source", "Literal", "Card"}}
        if token.lower() in by_name:
            return by_name[token.lower()]
        # Free-text claim objects stay visible as Literal nodes. They are never silently
        # merged into an entity.
        return self.add_node(f"literal:{slug(token)}", "Literal", token, origin)

    def edge(self, src: str, rel: str, dst: str, **attrs) -> None:
        self.edges.append({"from": src, "relation": rel, "to": dst, **attrs})


def source_node(g: Graph, sid: str, meta: dict, origin: str) -> str:
    url = meta.get("url", "")
    official = url.startswith(OFFICIAL_HOSTS)
    return g.add_node(f"source:{sid}", "Source", meta.get("title", sid), origin, url=url,
                      source_class="WIZARDS_OFFICIAL" if official else "NON_WIZARDS_LABELLED",
                      kind=meta.get("kind", ""))


def ingest_claim_pack(g: Graph, rel: str) -> dict:
    d = load(rel)
    origin = Path(rel).name
    reg = d.get("source_register", {})
    for sid, meta in reg.items():
        source_node(g, sid, meta, origin)
    n_claims = 0
    for c in d.get("claims", []):
        n_claims += 1
        grade = GRADE_ALIASES.get(c["grade"], c["grade"])
        if grade not in CANON_STATUSES:
            g.problems.append(f"{origin} {c['id']}: unknown grade {c['grade']}")
        cid = g.add_node(f"claim:{c['id']}", "Claim", c.get("summary", c["id"]), origin,
                         grade=grade, predicate=c["predicate"],
                         stage=c.get("chronology_stage") or c.get("stage") or c.get("event_stage") or "",
                         continuity=c.get("continuity", ""), limitation=c.get("limitation", ""))
        if not c.get("source_ids"):
            g.problems.append(f"{origin} {c['id']}: claim has no source_ids")
        for sid in c.get("source_ids", []):
            if f"source:{sid}" not in g.nodes:
                g.problems.append(f"{origin} {c['id']}: unregistered source {sid}")
            g.edge(f"source:{sid}", "cited_by", cid)
        subj = g.resolve(c["subject"], origin)
        objs = [t for t in re.split(r";\s*", str(c["object"])) if t.strip()]
        g.edge(cid, "asserts", subj, role="subject")
        for tok in objs:
            obj = g.resolve(tok, origin)
            g.edge(cid, "asserts", obj, role="object")
            g.edge(subj, c["predicate"], obj, claim=c["id"], grade=grade,
                   sources=sorted(c.get("source_ids", [])))
    # Pack A2 card anchors and Pack A3 card-art contexts become Card nodes keyed by name.
    for a in d.get("card_anchors", []):
        card = g.add_node(f"card:{slug(a['name'])}", "Card", a["name"], origin)
        tgt = g.resolve(a["entity"], origin)
        g.edge(tgt, "depicted_by", card, tier=a["representation"], sources=sorted(a.get("source_ids", [])),
               limit=a.get("limit", ""))
    for a in d.get("card_art_context", []):
        card = g.add_node(f"card:{slug(a['name'])}", "Card", a["name"], origin)
        tgt = g.resolve(a["event"], origin) if a.get("event") else None
        if tgt:
            g.edge(tgt, "depicted_by", card, tier=a["tier"], sources=sorted(a.get("source_ids", [])),
                   limit=a.get("limit", ""))
    return {"file": rel, "claims": n_claims, "entities": len(d.get("entities", [])), "sources": len(reg)}


def ingest_art_pack(g: Graph, rel: str) -> dict:
    d = load(rel)
    origin = Path(rel).name
    for c in d.get("cards", []):
        card = g.add_node(f"card:{slug(c['name'])}", "Card", c["name"], origin, oracle_id=c.get("oracle_id"),
                          exact_story_art_printings=sorted(c.get("same_art_printing_ids", [])),
                          story_art_illustration_id=c.get("matched_illustration_id"))
        src = f"source:{c['source_id']}"
        if src not in g.nodes:
            g.problems.append(f"{origin} {c['name']}: unregistered source {c['source_id']}")
        g.edge(src, "exact_art_published_in_story", card, tier=c.get("context_tier", ""),
               printing=c.get("visually_reviewed_printing", {}).get("id", ""))
    return {"file": rel, "cards": len(d.get("cards", []))}


def ingest_deck(g: Graph, rel: str) -> dict:
    d = load(rel)
    origin = Path(rel).name
    deck_id = "deck:" + slug(Path(rel).name.replace("_printing_evidence.json", ""))
    status = str(d.get("status", ""))
    if "UNAPPROVED" not in status.upper():
        g.problems.append(f"{rel}: deck evidence claims approval; graph only ingests unapproved proposals")
    g.add_node(deck_id, "DeckProposal", d.get("theme", deck_id), origin, status=status,
               raw_sha256=d.get("raw_sha256", ""))
    count = 0
    for c in d.get("cards", []):
        if not c.get("tier"):
            continue
        p = c.get("printing", {})
        card = g.add_node(f"card:{slug(c['name'])}", "Card", c["name"], origin, oracle_id=p.get("oracle_id"))
        # Pilot 1 evidence names the key ``pack_a_claims``; spec-driven pilots use ``claims``.
        cited = c.get("pack_a_claims", c.get("claims", []))
        g.edge(card, "proposed_in", deck_id, tier=c["tier"], beat=c.get("beat", ""),
               printing=p.get("id", ""), claims=sorted(cited))
        for claim in cited:
            if f"claim:{claim}" not in g.nodes:
                g.problems.append(f"{rel} {c['name']}: cites unknown claim {claim}")
        count += 1
    return {"file": rel, "cards": count}


def ingest_name_anchors(g: Graph, rel: str) -> dict:
    """Card-name anchors (scripts/build_card_name_anchors.py): ``named_on_card`` edges from an
    entity to each printed card named for it. These are card-data navigation, never canon claims."""
    d = load(rel)
    origin = Path(rel).name
    src = d.get("card_data_source", {})
    n = 0
    for a in d.get("anchors", []):
        if a["entity"] not in g.local:
            g.problems.append(f"{origin}: anchor for unknown entity {a['entity']}")
            continue
        for c in a["cards"]:
            card = g.add_node(f"card:{slug(c['name'])}", "Card", c["name"], origin, oracle_id=c.get("oracle_id"))
            g.edge(g.local[a["entity"]], "named_on_card", card, tier=d.get("tier", "NAMED_CARD"),
                   card_data_source=f"{src.get('provider', '')} {src.get('snapshot', '')}".strip())
            n += 1
    return {"file": rel, "anchors": n}


def ingest_story_captions(g: Graph, rel: str) -> dict:
    d = load(rel)
    origin = Path(rel).name
    by_url = {n["url"]: n["id"] for n in g.nodes.values() if n["type"] == "Source" and n.get("url")}
    n = 0
    for page in d.get("pages", []):
        src = by_url.get(page["url"])
        if not src:
            continue
        artists: dict[str, set] = {}
        for c in page["captions"]:
            card = g.add_node(f"card:{slug(c['card'])}", "Card", c["card"], origin, oracle_id=c.get("oracle_id"))
            artists.setdefault(card, set()).add(c["artist"])
        for card in sorted(artists):
            g.edge(src, "art_captioned_in_story", card, tier=d.get("tier", ""), artists=sorted(artists[card]))
            n += 1
    return {"file": rel, "caption_edges": n}


def bridge_curated(g: Graph, rel: str) -> int:
    lg = load(rel)
    by_name: dict[str, list[str]] = {}
    for n in lg.get("nodes", []):
        if n.get("kind") in {"character", "plane", "item", "arc", "dossier"}:
            by_name.setdefault(n["name"].lower(), []).append(n["id"])
    hits = 0
    for node in list(g.nodes.values()):
        if node["type"] in {"Claim", "Source", "Literal", "DeckProposal", "Card"}:
            continue
        for target in sorted(by_name.get(node["name"].lower(), [])):
            tid = "curated:" + target
            g.add_node(tid, "Concept", target, Path(rel).name)
            g.edge(node["id"], "see_also_curated_entry", tid, tier="contextual_pointer")
            hits += 1
    return hits


def build(manifest_path: Path = MANIFEST) -> dict:
    m = json.loads(manifest_path.read_text(encoding="utf-8"))
    g = Graph()
    # Pass 1: register every pack's entities, so a claim in an earlier pack can name an entity
    # that a later pack introduces (for example, A003's survivor list and A2's entities).
    for rel in m["claim_packs"]:
        for ent in load(rel).get("entities", []):
            g.entity(ent["id"], ent["type"], ent["name"], Path(rel).name)
    inputs = {"claim_packs": [ingest_claim_pack(g, r) for r in m["claim_packs"]],
              "art_match_packs": [ingest_art_pack(g, r) for r in m.get("art_match_packs", [])],
              "deck_evidence": [ingest_deck(g, r) for r in m.get("deck_evidence", [])],
              "name_anchor_packs": [ingest_name_anchors(g, r) for r in m.get("name_anchor_packs", [])],
              "story_caption_packs": [ingest_story_captions(g, r) for r in m.get("story_caption_packs", [])]}
    bridges = bridge_curated(g, m["curated_lore_graph"]) if m.get("curated_lore_graph") else 0
    for rel in inputs:
        for item in inputs[rel]:
            item["sha256"] = hashlib.sha256((ROOT / item["file"]).read_bytes()).hexdigest()
    # Validation: broken links, duplicate edges, orphaned claims.
    seen = set()
    for e in g.edges:
        for end in ("from", "to"):
            if e[end] not in g.nodes:
                g.problems.append(f"broken edge endpoint {e[end]} in {e['relation']}")
        key = (e["from"], e["relation"], e["to"], e.get("claim"), e.get("role"), e.get("printing"))
        if key in seen:
            g.problems.append(f"duplicate edge {key}")
        seen.add(key)
    for n in g.nodes.values():
        n["origins"].sort()
        if n["type"] == "Claim" and not any(e["to"] == n["id"] and e["relation"] == "cited_by" for e in g.edges):
            g.problems.append(f"claim {n['id']} has no citing source")
    nodes = sorted(g.nodes.values(), key=lambda n: n["id"])
    edges = sorted(g.edges, key=lambda e: json.dumps(e, sort_keys=True))
    from collections import Counter
    stats = {"nodes": len(nodes), "edges": len(edges),
             "node_types": dict(sorted(Counter(n["type"] for n in nodes).items())),
             "claims_by_status": dict(sorted(Counter(n["grade"] for n in nodes if n["type"] == "Claim").items())),
             "relations": len({e["relation"] for e in edges}),
             "literal_objects": sum(1 for n in nodes if n["type"] == "Literal"),
             "curated_bridges": bridges,
             "wizards_official_sources": sum(1 for n in nodes if n.get("source_class") == "WIZARDS_OFFICIAL"),
             "non_wizards_sources": sum(1 for n in nodes if n.get("source_class") == "NON_WIZARDS_LABELLED")}
    body = {"schema": "multiverse-claim-graph/v1",
            "meaning": ("Directional, cited relationships compiled from committed research packs. A relationship "
                        "edge inherits its claim's canon status; deck-proposal and curated-bridge edges are "
                        "navigation, never canon assertions."),
            "canon_statuses": CANON_STATUSES, "inverse_relations": INVERSE,
            "inputs": inputs, "stats": stats, "problems": sorted(set(g.problems)),
            "nodes": nodes, "edges": edges}
    body["content_sha256"] = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
    return body


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="fail if the committed graph is stale or invalid")
    ap.add_argument("--out", type=Path, default=OUT)
    a = ap.parse_args()
    graph = build()
    text = json.dumps(graph, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    if graph["problems"]:
        print("GRAPH PROBLEMS:", *graph["problems"], sep="\n  ", file=sys.stderr)
    if a.check:
        current = a.out.read_text(encoding="utf-8") if a.out.exists() else ""
        if current != text:
            print("FAIL: committed multiverse_graph.json is stale; rerun build_multiverse_graph.py", file=sys.stderr)
            return 1
        print(f"PASS graph current: {graph['stats']}")
        return 1 if graph["problems"] else 0
    a.out.write_text(text, encoding="utf-8")
    print(json.dumps(graph["stats"], indent=1))
    return 1 if graph["problems"] else 0


if __name__ == "__main__":
    sys.exit(main())
