#!/usr/bin/env python3
"""Audit five historically isolated character/faction endpoints, optionally against live Wizards HTML.

The offline check proves graph identity, direct-edge provenance and explicit
currentness limits. Only --live verifies exact source excerpts on the official
pages; neither mode approves claims, certifies completeness or updates decks.
"""
import argparse
import hashlib
import html
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "data/lore_research/pack_p5_isolated_entity_history_2026-10-31.json"
GRAPH = ROOT / "data/multiverse_graph/multiverse_graph.json"
EXPECTED = {"character:eric_kenrith", "character:hazel_kenrith",
            "character:lyra_dawnbringer", "character:valentin", "faction:cabaretti"}
STRUCTURAL = {"cited_by", "asserts", "see_also_curated_entry", "proposed_in"}


class _Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def norm(text):
    return " ".join(html.unescape(text).split()).casefold()


def audit(html_by_source=None):
    pack = json.loads(PACK.read_text(encoding="utf-8"))
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    assert pack["status"] == "PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED"
    claims = pack["claims"]
    assert [c["id"] for c in claims] == [f"IEH{i:03d}" for i in range(1, 6)]
    assert len(pack["source_register"]) == 4
    source_hashes = []
    for c in claims:
        assert c["grade"] == "CANON_CONFIRMED" and c["limitation"]
        assert len(c["source_ids"]) == 1 and len(c["source_excerpt"]) >= 25
        sid = c["source_ids"][0]
        url = pack["source_register"][sid]["url"]
        assert url.startswith("https://magic.wizards.com/")
        source_hashes.append({"claim": c["id"], "source_id": sid,
                              "quote_sha256": hashlib.sha256(norm(c["source_excerpt"]).encode()).hexdigest()})
        if html_by_source is not None:
            reader = _Text()
            reader.feed(html_by_source[sid])
            if norm(c["source_excerpt"]) not in norm(" ".join(reader.parts)):
                raise ValueError(f"Official source excerpt missing for {c['id']}")
    assert "Eric" in claims[1]["source_excerpt"]
    assert "Erec" in claims[1]["limitation"]  # no unsupported spelling merge
    assert all(any(word in c["limitation"].lower() for word in ("current", "later", "present"))
               for c in claims)
    ids = {n["id"] for n in graph["nodes"]}
    assert EXPECTED <= ids
    edges = [e for e in graph["edges"] if e.get("claim") and e["relation"] not in STRUCTURAL]
    direct = {nid for edge in edges for nid in (edge["from"], edge["to"])}
    assert EXPECTED <= direct
    for c in claims:
        matches = [e for e in edges if e["claim"] == c["id"]]
        assert matches and all(e["grade"] == "CANON_CONFIRMED" and
                               e["sources"] == c["source_ids"] for e in matches)
    registered = {n["id"] for n in graph["nodes"] if n["type"] in ("Character", "Faction")}
    uncovered = sorted(registered - direct)
    assert not uncovered, f"Registered character/faction without direct cited claim: {uncovered}"
    return {"status": "PASS", "verified_claims": len(claims),
            "registered_character_faction_entities": len(registered),
            "entities_with_direct_cited_claims": len(registered), "uncovered": uncovered,
            "source_pages": len(pack["source_register"]), "quote_hashes": source_hashes,
            "live_source_quote_check": html_by_source is not None,
            "owner_approved": False, "complete_histories": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--live", action="store_true")
    args = parser.parse_args()
    page_html = None
    if args.live:
        pack = json.loads(PACK.read_text(encoding="utf-8"))
        page_html = {}
        for sid, source in pack["source_register"].items():
            request = Request(source["url"], headers={"User-Agent": "MTG-Multiverse-Companion-source-check/1.0"})
            with urlopen(request, timeout=30) as response:
                page_html[sid] = response.read().decode("utf-8", errors="replace")
    print(json.dumps(audit(page_html), indent=2))


if __name__ == "__main__":
    main()
