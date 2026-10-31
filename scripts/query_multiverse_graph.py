#!/usr/bin/env python3
"""Query the Phase 3 cited Multiverse graph in both directions.

Examples:
  python3 scripts/query_multiverse_graph.py node "Nicol Bolas"
  python3 scripts/query_multiverse_graph.py neighbors ugin --status CANON_CONFIRMED
  python3 scripts/query_multiverse_graph.py card "Crux of Fate"
  python3 scripts/query_multiverse_graph.py printing blc 1
  python3 scripts/query_multiverse_graph.py path piru ugin
  python3 scripts/query_multiverse_graph.py path piru ugin --max-depth 1  # null; no truncated non-path
  python3 scripts/query_multiverse_graph.py path echoverse "Nicol Bolas" --include-qualified
  python3 scripts/query_multiverse_graph.py status CANON_DISPUTED
  python3 scripts/query_multiverse_graph.py search tarkir

Every relationship row includes its claim ID, canon status and source URLs. Rows for
proposals and curated bridges are labelled as navigation, not canon. Graph paths
default to CANON_CONFIRMED edges; disputed, implied, open and alternate-continuity
edges require explicit --include-qualified. Paths are undirected *navigation*,
not evidence of an ordered, causal or continuous historical journey.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import deque
from pathlib import Path

GRAPH = Path(__file__).resolve().parents[1] / "data/multiverse_graph/multiverse_graph.json"
STRUCTURAL = {"asserts", "cited_by"}


class MG:
    def __init__(self, path: Path = GRAPH):
        self.g = json.loads(path.read_text(encoding="utf-8"))
        self.nodes = {n["id"]: n for n in self.g["nodes"]}
        self.out: dict[str, list] = {}
        self.inc: dict[str, list] = {}
        for e in self.g["edges"]:
            self.out.setdefault(e["from"], []).append(e)
            self.inc.setdefault(e["to"], []).append(e)
        self.inverse = self.g.get("inverse_relations", {})

    def find(self, term: str, prefer: str | None = None) -> str:
        if term in self.nodes:
            return term
        t = term.lower().strip()
        key = "".join(c if c.isalnum() else "_" for c in t).strip("_")  # "Old Phyrexia" -> old_phyrexia
        exact = [i for i, n in self.nodes.items() if n["name"].lower() == t or i.split(":", 1)[-1] in (t, key)]
        if prefer is not None:
            preferred = sorted(i for i in exact if self.nodes[i]["type"] == prefer)
            if preferred:
                return preferred[0]
            recorded = sorted(i for i, n in self.nodes.items() if n["type"] == prefer and
                              t in {v.lower() for v in n.get("name_variants", [])})
            if len(recorded) == 1:
                return recorded[0]
            if len(recorded) > 1:
                raise KeyError(f"ambiguous recorded {prefer} name variant {term!r}; candidates: {recorded[:10]}")
        rank = {"Concept": 3, "Literal": 4, "Card": 2, "Source": 2, "Claim": 2, "DeckProposal": 2}
        pref = sorted(exact, key=lambda i: (0 if self.nodes[i]["type"] == prefer else 1 + rank.get(self.nodes[i]["type"], 0), i))
        if pref:
            return pref[0]
        # Alternate display names are imported only when multiple source packs
        # use different titles for the exact SAME ID. Ambiguous variants may not
        # be used to guess identity across distinct entities.
        variants = sorted(i for i, n in self.nodes.items() if t in
                          {v.lower() for v in n.get("name_variants", [])}
                          and (prefer is None or n["type"] == prefer))
        if len(variants) == 1:
            return variants[0]
        if len(variants) > 1:
            raise KeyError(f"ambiguous recorded name variant {term!r}; candidates: {variants[:10]}")
        part = sorted(i for i, n in self.nodes.items() if t in n["name"].lower() and n["type"] not in {"Claim"})
        if len(part) == 1:
            return part[0]
        raise KeyError(f"no unique node for {term!r}; candidates: {part[:10]}")

    def _sources(self, e: dict) -> list[str]:
        ids = e.get("sources", [])
        urls = [self.nodes[f"source:{s}"].get("url", "") for s in ids if f"source:{s}" in self.nodes]
        if e["relation"] == "art_file_used_on_official_page" and self.nodes[e["from"]]["type"] == "Source":
            urls.append(self.nodes[e["from"]].get("url", ""))
        return sorted(set(u for u in urls if u))

    def neighbors(self, term: str, status: str | None = None, include_structural=False) -> list[dict]:
        nid = self.find(term)
        rows = []
        for direction, edges in (("out", self.out.get(nid, [])), ("in", self.inc.get(nid, []))):
            for e in edges:
                if e["relation"] in STRUCTURAL and not include_structural:
                    continue
                if status and e.get("grade") != status:
                    continue
                other = e["to"] if direction == "out" else e["from"]
                rel = e["relation"] if direction == "out" else self.inverse.get(e["relation"], f"inverse_of:{e['relation']}")
                rows.append({"direction": direction, "relation": rel, "node": other,
                             "name": self.nodes[other]["name"], "type": self.nodes[other]["type"],
                             "claim": e.get("claim"), "status": e.get("grade") or ("NAVIGATION_ONLY" if e["relation"] in {"proposed_in", "see_also_curated_entry", "has_printing", "art_file_used_on_official_page"} else e.get("tier", "")),
                             "tier": e.get("tier"), "source_urls": self._sources(e)})
        return sorted(rows, key=lambda r: (r["direction"], r["relation"], r["node"]))

    def path(self, a: str, b: str, max_depth: int = 6, *, include_qualified: bool = False) -> list[dict] | None:
        """Find a fully connected, depth-bounded, sourced *navigation* path.

        The path traverses citation-bearing claim edges in either direction.
        It must never return a truncated prefix that fails to reach b, and
        must not silently use disputed or alternate-world claims as prime
        canon. Callers that explicitly inspect uncertainties can opt in.
        """
        if isinstance(max_depth, bool) or not isinstance(max_depth, int) or max_depth < 0:
            raise ValueError('max_depth must be a nonnegative integer')
        src, dst = self.find(a), self.find(b)
        prev: dict[str, tuple] = {src: None}
        depth: dict[str, int] = {src: 0}
        q = deque([src])
        while q:
            cur = q.popleft()
            if cur == dst:
                break
            if depth[cur] >= max_depth:
                continue
            steps = [(e, e["to"]) for e in self.out.get(cur, [])] + [(e, e["from"]) for e in self.inc.get(cur, [])]
            for e, nxt in steps:
                if (not e.get("claim") or nxt in prev or not self._sources(e)
                        or (not include_qualified and e.get("grade") != "CANON_CONFIRMED")):
                    continue
                prev[nxt] = (cur, e)
                depth[nxt] = depth[cur] + 1
                q.append(nxt)
        if dst not in prev:
            return None
        hops, cur = [], dst
        while prev[cur]:
            p, e = prev[cur]
            hops.append({"from": e["from"], "relation": e["relation"], "to": e["to"], "claim": e["claim"],
                         "status": e["grade"], "source_urls": self._sources(e),
                         "traversal_from": p, "traversal_to": cur,
                         "traversal_direction": "forward" if p == e["from"] else "reverse"})
            cur = p
        return list(reversed(hops))

    def card(self, term: str) -> dict:
        nid = self.find(term, prefer="Card")
        n = self.nodes[nid]
        return {"card": n, "relationships": self.neighbors(nid)}

    def printing(self, set_code: str, collector_number: str) -> list[dict]:
        code = set_code.lower().strip()
        number = collector_number.lower().strip()
        found = [n for n in self.g["nodes"] if n["type"] == "CardRepresentation"
                 and n["set"].lower() == code and n["collector_number"].lower() == number]
        return [{"printing": n, "relationships": self.neighbors(n["id"])} for n in found]

    def status(self, status: str) -> list[dict]:
        return [{"claim": n["id"], "summary": n["name"], "limitation": n.get("limitation", "")}
                for n in self.g["nodes"] if n["type"] == "Claim" and n.get("grade") == status]

    def search(self, term: str) -> list[dict]:
        t = term.lower()
        return [{"id": n["id"], "type": n["type"], "name": n["name"]} for n in self.g["nodes"]
                if t in n["name"].lower() or t in n["id"].lower() or
                any(t in v.lower() for v in n.get("name_variants", []))]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("node", "card", "search"):
        sub.add_parser(name).add_argument("term")
    nb = sub.add_parser("neighbors"); nb.add_argument("term"); nb.add_argument("--status"); nb.add_argument("--structural", action="store_true")
    pa = sub.add_parser("path"); pa.add_argument("a"); pa.add_argument("b")
    pa.add_argument("--max-depth", type=int, default=6)
    pa.add_argument("--include-qualified", action="store_true", help="also traverse disputed, open, implied and alternate-continuity claims")
    pr = sub.add_parser("printing"); pr.add_argument("set_code"); pr.add_argument("collector_number")
    st = sub.add_parser("status"); st.add_argument("status")
    a = ap.parse_args(argv)
    mg = MG()
    try:
        if a.cmd == "node":
            nid = mg.find(a.term); res = {"node": mg.nodes[nid], "relationships": mg.neighbors(nid)}
        elif a.cmd == "neighbors":
            res = mg.neighbors(a.term, a.status, a.structural)
        elif a.cmd == "card":
            res = mg.card(a.term)
        elif a.cmd == "printing":
            res = mg.printing(a.set_code, a.collector_number)
        elif a.cmd == "path":
            res = mg.path(a.a, a.b, max_depth=a.max_depth, include_qualified=a.include_qualified)
        elif a.cmd == "status":
            res = mg.status(a.status)
        else:
            res = mg.search(a.term)
    except KeyError as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
