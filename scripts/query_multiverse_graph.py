#!/usr/bin/env python3
"""Query the Phase 3 cited Multiverse graph in both directions.

Examples:
  python3 scripts/query_multiverse_graph.py node "Nicol Bolas"
  python3 scripts/query_multiverse_graph.py neighbors ugin --status CANON_CONFIRMED
  python3 scripts/query_multiverse_graph.py card "Crux of Fate"
  python3 scripts/query_multiverse_graph.py path piru ugin
  python3 scripts/query_multiverse_graph.py status CANON_DISPUTED
  python3 scripts/query_multiverse_graph.py search tarkir

Every relationship row includes its claim ID, canon status and source URLs. Rows for
proposals and curated bridges are labelled as navigation, not canon.
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
        rank = {"Concept": 3, "Literal": 4, "Card": 2, "Source": 2, "Claim": 2, "DeckProposal": 2}
        pref = sorted(exact, key=lambda i: (0 if self.nodes[i]["type"] == prefer else 1 + rank.get(self.nodes[i]["type"], 0), i))
        if pref:
            return pref[0]
        part = sorted(i for i, n in self.nodes.items() if t in n["name"].lower() and n["type"] not in {"Claim"})
        if len(part) == 1:
            return part[0]
        raise KeyError(f"no unique node for {term!r}; candidates: {part[:10]}")

    def _sources(self, e: dict) -> list[str]:
        ids = e.get("sources", [])
        return [self.nodes[f"source:{s}"].get("url", "") for s in ids if f"source:{s}" in self.nodes]

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
                             "claim": e.get("claim"), "status": e.get("grade") or ("NAVIGATION_ONLY" if e["relation"] in {"proposed_in", "see_also_curated_entry"} else e.get("tier", "")),
                             "tier": e.get("tier"), "source_urls": self._sources(e)})
        return sorted(rows, key=lambda r: (r["direction"], r["relation"], r["node"]))

    def path(self, a: str, b: str, max_depth: int = 6) -> list[dict] | None:
        src, dst = self.find(a), self.find(b)
        prev: dict[str, tuple] = {src: None}
        q = deque([src])
        while q:
            cur = q.popleft()
            if cur == dst:
                break
            steps = [(e, e["to"]) for e in self.out.get(cur, [])] + [(e, e["from"]) for e in self.inc.get(cur, [])]
            for e, nxt in steps:
                # Paths only travel through cited canon relationships between entities.
                if "claim" not in e or nxt in prev:
                    continue
                prev[nxt] = (cur, e)
                q.append(nxt)
        if dst not in prev:
            return None
        hops, cur = [], dst
        while prev[cur]:
            p, e = prev[cur]
            hops.append({"from": e["from"], "relation": e["relation"], "to": e["to"], "claim": e["claim"],
                         "status": e["grade"], "source_urls": self._sources(e)})
            cur = p
        return list(reversed(hops))[:max_depth]

    def card(self, term: str) -> dict:
        nid = self.find(term, prefer="Card")
        n = self.nodes[nid]
        return {"card": n, "relationships": self.neighbors(nid)}

    def status(self, status: str) -> list[dict]:
        return [{"claim": n["id"], "summary": n["name"], "limitation": n.get("limitation", "")}
                for n in self.g["nodes"] if n["type"] == "Claim" and n.get("grade") == status]

    def search(self, term: str) -> list[dict]:
        t = term.lower()
        return [{"id": n["id"], "type": n["type"], "name": n["name"]} for n in self.g["nodes"]
                if t in n["name"].lower() or t in n["id"].lower()]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("node", "card", "search"):
        sub.add_parser(name).add_argument("term")
    nb = sub.add_parser("neighbors"); nb.add_argument("term"); nb.add_argument("--status"); nb.add_argument("--structural", action="store_true")
    pa = sub.add_parser("path"); pa.add_argument("a"); pa.add_argument("b")
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
        elif a.cmd == "path":
            res = mg.path(a.a, a.b)
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
