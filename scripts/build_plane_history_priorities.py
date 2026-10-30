#!/usr/bin/env python3
"""Deterministic, conservative Phase 2/5/6 coverage and research queue.

Counts ONLY claims explicitly attached to a Plane node in the cited graph.
Missing direct edges are research gaps, not evidence that a plane lacks history.
Three registered Phase 6 pilots stay UNAPPROVED. Use --check in CI.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "data/multiverse_graph/multiverse_graph.json"
CHRON = ROOT / "data/lore_research/relative_chronology_2026-10-30.json"
SPECS = ROOT / "data/lore_decks/specs"
OUT = ROOT / "data/lore_research/plane_history_priorities_2026-10-30.json"


def build():
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    chron = json.loads(CHRON.read_text(encoding="utf-8"))
    planes = {n["id"]: n for n in graph["nodes"] if n["type"] == "Plane"}
    claim_edges = {p: [] for p in planes}
    for e in graph["edges"]:
        if not e.get("claim"):
            continue
        targets = {e["from"], e["to"]} & planes.keys()
        for p in targets:
            claim_edges[p].append(e)
    plane_rows = []
    for id_, node in sorted(planes.items(), key=lambda kv: kv[1]["name"].casefold()):
        edges = claim_edges[id_]
        citations = sorted({s for e in edges for s in e.get("sources", [])})
        claims = sorted({e["claim"] for e in edges})
        grades = sorted({e.get("grade", "UNKNOWN") for e in edges})
        plane_rows.append({"id": id_, "name": node["name"], "claim_edges": len(edges),
                           "distinct_claims": len(claims), "claims": claims,
                           "official_source_ids": citations, "grades_present": grades,
                           "research_priority": "NO_DIRECT_CLAIM" if not claims else
                           "THIN_DIRECT_EVIDENCE" if len(claims) < 5 else "EXPAND_NARRATIVE_DEPTH",
                           "limitation": "Direct graph edges only; not the complete plane history or a canon completeness score."})
    pilots = []
    for path in sorted(SPECS.glob("pilot[123]_*.json")):
        spec = json.loads(path.read_text(encoding="utf-8"))
        stem = spec["stem"]
        proposal = json.loads((ROOT / "data/lore_decks/drafts" / (stem + "_proposal.json")).read_text(encoding="utf-8"))
        if not spec["status"].startswith("UNAPPROVED") or any(proposal["approval"][flag] for flag in ("approved", "locked", "certified")):
            raise ValueError("pilot research must never change approval state: " + stem)
        pilots.append({"name": spec["theme"], "stem": stem,
                       "status": "UNAPPROVED", "commander": spec["commander"]["name"],
                       "tiers": proposal["counts"]["tiers"],
                       "missing_owner_gate": "exact decklist and lore-representation approval by Cory",
                       "research_caution": "Mechanics, printed-card names, and official artwork mentions do not prove a direct scene depiction."})
    no_direct = sum(r["distinct_claims"] == 0 for r in plane_rows)
    return {"schema": "plane-history-priorities/v1", "as_of": "2026-10-30",
            "status": "PRELIMINARY_RESEARCH", "coverage_basis": "Only registered Plane nodes and direct cited claim edges in the committed graph. MTG's complete list of planes is larger and not enumerated here.",
            "registered_planes": len(plane_rows), "without_direct_claims": no_direct,
            "with_direct_claims": len(plane_rows) - no_direct,
            "chronology": {"event_nodes": chron["counts"]["event_nodes"],
                           "comparable_pairs": chron["counts"]["comparable_pairs"],
                           "unresolved_pairs": chron["counts"]["total_pairs"] - chron["counts"]["comparable_pairs"],
                           "disconnected_components": chron["counts"]["components"],
                           "l244_complete": chron["l244_closure"]["closes_l244"]},
            "phase6_pilots": pilots, "planes": plane_rows,
            "next_research": [
                "For no-direct-claim planes, locate official Wizards story/plane primers; only then add cited claims.",
                "For thinly linked planes, build participant/conflict/event/aftermath dossiers with explicit uncertainty.",
                "Place chronology edges only with verbatim primary-source orderings or printed in-world dates; do not infer from set release order.",
                "Review three pilot decks with Cory before any owner-approval or certification flag changes."]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    value = build()
    result = json.dumps(value, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if OUT.read_text(encoding="utf-8") != result:
            raise SystemExit("FAIL plane-history research priorities stale")
        print(f"PASS {value['registered_planes']} planes, {value['without_direct_claims']} lacking direct cited claims; three unapproved pilots")
    else:
        OUT.write_text(result, encoding="utf-8")
        print(f"Updated {OUT}")


if __name__ == "__main__":
    main()
