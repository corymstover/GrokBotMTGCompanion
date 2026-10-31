#!/usr/bin/env python3
"""Audit v2.68's last four thin registered planes; optionally recheck live Wizards HTML."""
import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen

from audit_p5_thin_plane_history import _Text, norm

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "data/lore_research/pack_p5_last_four_thin_planes_2026-10-31.json"
GRAPH = ROOT / "data/multiverse_graph/multiverse_graph.json"
DOSSIERS = ROOT / "data/lore_research/plane_history_dossiers_2026-10-30.json"
EXPECTED = {"Bablovia": 5, "Meditation Realm": 5, "Muraganda": 5, "Skalla": 5}
SUBJECTS = {"bablovia", "meditation_realm", "muraganda", "skalla"}
STRUCTURAL = {"cited_by", "asserts", "see_also_curated_entry", "proposed_in"}


def text_on_page(html_body, quote):
    parser = _Text()
    parser.feed(html_body)
    return norm(quote) in norm(" ".join(parser.parts))


def audit(html_by_source=None):
    pack = json.loads(PACK.read_text(encoding="utf-8"))
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    dossiers = json.loads(DOSSIERS.read_text(encoding="utf-8"))
    assert pack["status"] == "PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED"
    assert len(pack["source_register"]) == 8
    assert [c["id"] for c in pack["claims"]] == [f"LFP{i:03d}" for i in range(1, 14)]
    assert "Un-set" in pack["scope"] and "SSX020" in pack["remaining"][1]
    edges = [e for e in graph["edges"] if e.get("claim") and e["relation"] not in STRUCTURAL]
    for i, claim in enumerate(pack["claims"]):
        assert claim["subject"] in SUBJECTS
        assert claim["grade"] == ("ALTERNATE_CONTINUITY" if i < 4 else "CANON_CONFIRMED")
        assert len(claim["limitation"]) >= 45 and claim["source_excerpt"]
        if i < 4:
            assert claim["continuity"] == "Unstable silver-border Un-set setting"
            assert any(term in claim["limitation"] for term in ("Unstable", "Un-set", "silver-border"))
        for sid in claim["source_ids"]:
            assert pack["source_register"][sid]["url"].startswith("https://magic.wizards.com/")
        if html_by_source is not None and not text_on_page(
                html_by_source[claim["source_ids"][0]], claim["source_excerpt"]):
            raise ValueError(f"Official source excerpt absent for {claim['id']}")
        relations = [e for e in edges if e["claim"] == claim["id"]]
        assert relations, f"Claim missing from graph: {claim['id']}"
        assert all(e["from"] == "plane:" + claim["subject"] and
                   e["grade"] == claim["grade"] and
                   e["sources"] == sorted(claim["source_ids"]) for e in relations)
    if html_by_source is not None and not text_on_page(
            html_by_source["lf_unset_boundary"], pack["continuity_boundary_excerpt"]):
        raise ValueError("Official Un-set continuity boundary excerpt absent")
    by_name = {p["plane"]: p for p in dossiers["planes"]}
    counts = {name: by_name[name]["distinct_claims"] for name in EXPECTED}
    assert counts == EXPECTED, f"Direct plane counts drifted: {counts}"
    assert sum(c["grade"] == "ALTERNATE_CONTINUITY" for c in by_name["Bablovia"]["facts"]) == 4
    assert dossiers["counts"]["thin_planes_fewer_than_five_claims"] == 0
    assert all(not p.get("complete_history") for p in by_name.values())
    return {"status": "PASS", "claims": 13, "official_pages": 8,
            "expanded_planes": counts, "registered_thin_planes": 0,
            "bablovia_unset_isolated": True, "complete_histories": False,
            "owner_approved": False, "live_quote_checked": html_by_source is not None}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--live", action="store_true")
    args = ap.parse_args()
    pages = None
    if args.live:
        pack = json.loads(PACK.read_text(encoding="utf-8"))
        pages = {}
        for sid, source in pack["source_register"].items():
            request = Request(source["url"], headers={
                "User-Agent": "MTG-Multiverse-Companion-source-check/1.0"})
            with urlopen(request, timeout=30) as response:
                pages[sid] = response.read().decode("utf-8", errors="replace")
    print(json.dumps(audit(pages), indent=2))


if __name__ == "__main__":
    main()
