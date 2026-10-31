#!/usr/bin/env python3
"""Offline/live official-source audit for v2.67's four additional plane dossiers."""
import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen

from audit_p5_thin_plane_history import _Text, norm

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "data/lore_research/pack_p5_four_more_plane_histories_2026-10-31.json"
GRAPH = ROOT / "data/multiverse_graph/multiverse_graph.json"
DOSSIERS = ROOT / "data/lore_research/plane_history_dossiers_2026-10-30.json"
EXPECTED = {"Fiora": 7, "Kaldheim": 7, "Lorwyn-Shadowmoor": 6, "Thunder Junction": 5}
SUBJECTS = {"fiora", "kaldheim", "lorwyn_shadowmoor", "thunder_junction"}
STRUCTURAL = {"cited_by", "asserts", "see_also_curated_entry", "proposed_in"}


def audit(html_by_source=None):
    pack = json.loads(PACK.read_text(encoding="utf-8"))
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    dossiers = json.loads(DOSSIERS.read_text(encoding="utf-8"))
    assert pack["status"] == "PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED"
    assert len(pack["source_register"]) == 7
    assert [c["id"] for c in pack["claims"]] == [f"FMP{i:03d}" for i in range(1, 13)]
    edges = [e for e in graph["edges"] if e.get("claim") and e["relation"] not in STRUCTURAL]
    for claim in pack["claims"]:
        assert claim["grade"] == "CANON_CONFIRMED" and claim["subject"] in SUBJECTS
        assert claim["source_excerpt"] and len(claim["limitation"]) >= 40
        assert claim["source_ids"]
        for sid in claim["source_ids"]:
            assert pack["source_register"][sid]["url"].startswith("https://magic.wizards.com/")
        if html_by_source is not None:
            parser = _Text()
            parser.feed(html_by_source[claim["source_ids"][0]])
            if norm(claim["source_excerpt"]) not in norm(" ".join(parser.parts)):
                raise ValueError(f"Source excerpt absent on Wizards page for {claim['id']}")
        relations = [e for e in edges if e["claim"] == claim["id"]]
        assert relations, f"No plane-incident relation for {claim['id']}"
        assert all(e["from"] == "plane:" + claim["subject"] and
                   e["grade"] == claim["grade"] and
                   e["sources"] == sorted(claim["source_ids"]) for e in relations)
    by_name = {p["plane"]: p for p in dossiers["planes"]}
    counts = {name: by_name[name]["distinct_claims"] for name in EXPECTED}
    assert counts == EXPECTED, f"Plane dossier drift: {counts}"
    assert dossiers["counts"]["thin_planes_fewer_than_five_claims"] <= 4
    assert all(not p.get("complete_history") for p in by_name.values())
    return {"status": "PASS", "claims": 12, "source_pages": 7,
            "expanded_planes": counts, "remaining_thin_planes": dossiers["counts"]["thin_planes_fewer_than_five_claims"],
            "live_quote_checked": html_by_source is not None,
            "complete_histories": False, "owner_approved": False}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--live", action="store_true")
    args = p.parse_args()
    pages = None
    if args.live:
        pack = json.loads(PACK.read_text(encoding="utf-8"))
        pages = {}
        for sid, source in pack["source_register"].items():
            req = Request(source["url"], headers={"User-Agent": "MTG-Multiverse-Companion-source-check/1.0"})
            with urlopen(req, timeout=30) as response:
                pages[sid] = response.read().decode("utf-8", errors="replace")
    print(json.dumps(audit(pages), indent=2))


if __name__ == "__main__":
    main()
