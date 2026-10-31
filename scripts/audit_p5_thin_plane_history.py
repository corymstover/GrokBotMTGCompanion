#!/usr/bin/env python3
"""Audit four thin-plane expansions and optionally check quotes on official live HTML.

The offline gate verifies cited relation incidence and explicit historical
limitations. --live additionally checks quoted text at the original Wizards
URLs. Neither mode proves complete plane history or authorizes deckbuilding.
"""
import argparse
import hashlib
import html
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "data/lore_research/pack_p5_thin_plane_history_2026-10-31.json"
GRAPH = ROOT / "data/multiverse_graph/multiverse_graph.json"
DOSSIERS = ROOT / "data/lore_research/plane_history_dossiers_2026-10-30.json"
EXPECTED = {"Argentum": 5, "Eldraine": 5, "Ikoria": 6, "New Capenna": 5}
STRUCTURAL = {"cited_by", "asserts", "see_also_curated_entry", "proposed_in"}


class _Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def norm(value):
    return " ".join(html.unescape(value).split()).casefold()


def audit(html_by_source=None):
    pack = json.loads(PACK.read_text(encoding="utf-8"))
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    dossiers = json.loads(DOSSIERS.read_text(encoding="utf-8"))
    assert pack["status"] == "PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED"
    claims = pack["claims"]
    assert [c["id"] for c in claims] == [f"TPH{i:03d}" for i in range(1, 12)]
    assert len(pack["source_register"]) == 6
    source_hashes = []
    for claim in claims:
        assert claim["grade"] == "CANON_CONFIRMED" and len(claim["limitation"]) >= 40
        assert claim["source_excerpt"] and claim["source_ids"]
        for sid in claim["source_ids"]:
            url = pack["source_register"][sid]["url"]
            assert url.startswith("https://magic.wizards.com/")
        source_hashes.append({"claim": claim["id"], "sha256": hashlib.sha256(
            norm(claim["source_excerpt"]).encode()).hexdigest()})
        if html_by_source is not None:
            parser = _Text()
            parser.feed(html_by_source[claim["source_ids"][0]])
            if norm(claim["source_excerpt"]) not in norm(" ".join(parser.parts)):
                raise ValueError(f"Source excerpt absent on Wizards page for {claim['id']}")

    edges = [edge for edge in graph["edges"] if edge.get("claim") and
             edge["relation"] not in STRUCTURAL]
    for claim in claims:
        matches = [edge for edge in edges if edge["claim"] == claim["id"]]
        assert matches, f"No graph relation for {claim['id']}"
        assert all(edge["grade"] == claim["grade"] and
                   edge["sources"] == claim["source_ids"] for edge in matches)
        assert any(edge["from"] == f"plane:{claim['subject']}" for edge in matches)

    by_name = {plane["plane"]: plane for plane in dossiers["planes"]}
    counts = {name: by_name[name]["distinct_claims"] for name in EXPECTED}
    assert counts == EXPECTED, f"Four plane dossier counts changed: {counts}"
    assert dossiers["counts"]["thin_planes_fewer_than_five_claims"] == 8
    assert all(not by_name[name]["complete_history"] for name in EXPECTED if
               "complete_history" in by_name[name])
    assert "forgotten" in claims[6]["source_excerpt"]
    assert "NOT identify it as Phyrexia" in claims[6]["limitation"]
    return {"status": "PASS", "claims": len(claims), "source_pages": 6,
            "expanded_planes": counts, "remaining_thin_planes": 8,
            "source_hashes": source_hashes,
            "live_quote_checked": html_by_source is not None,
            "complete_histories": False, "owner_approved": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--live", action="store_true")
    args = parser.parse_args()
    pages = None
    if args.live:
        pack = json.loads(PACK.read_text(encoding="utf-8"))
        pages = {}
        for sid, source in pack["source_register"].items():
            req = Request(source["url"], headers={
                "User-Agent": "MTG-Multiverse-Companion-source-check/1.0"})
            with urlopen(req, timeout=30) as response:
                pages[sid] = response.read().decode("utf-8", errors="replace")
    print(json.dumps(audit(pages), indent=2))


if __name__ == "__main__":
    main()
