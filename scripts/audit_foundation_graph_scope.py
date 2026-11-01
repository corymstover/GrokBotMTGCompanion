#!/usr/bin/env python3
"""Fail-closed audit of *bounded* Packs A/B/C graph acceptance, never global canon proof.

The five historical claim files remain PRELIMINARY_RESEARCH. A separate
conservative owner decision packet may accept their existing sourced, graded,
searchable connections with unresolved questions explicitly left UNKNOWN.

  python3 scripts/audit_foundation_graph_scope.py
  python3 scripts/audit_foundation_graph_scope.py --check
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/release/foundation_graph_scope_review_2026-11-01.json"
DISPOSITIONS = ROOT / "data/release/pack_a_genealogy_owner_dispositions_2026-11-01.json"
DISPUTES = ROOT / "data/lore_research/pack_a_genealogy_disputes_2026-10-30.json"
PACK_PREFIXES = ("pack_a_", "pack_b_", "pack_c_")
EXPECTED_DECISIONS = {
    "GD1": "RETAIN_CONFIRMED_TWINS_WITH_NARRATOR_DISSENT",
    "GD2": "UNKNOWN_TWINS_PARENTAGE",
    "GD3": "RETAIN_DISPUTED_SURVIVOR_ROSTER",
    "GD4": "RETAIN_LIMITED_RAIDER_DESCENDANT_CLAIM",
    "GD5": "RETAIN_CROSIS_ANCESTOR_GENERATION_UNKNOWN",
    "GD6": "RETAIN_DARIGAAZ_RITH_SIBLING_AS_RESEARCH_NOTE",
    "GD7": "CHROMIUM_FATES_UNORDERED",
}
GRADES = {"CANON_CONFIRMED", "CANON_IMPLIED", "CANON_DISPUTED", "OPEN_QUESTION", "ALTERNATE_CONTINUITY"}


def j(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(ok: bool, reason: str) -> None:
    if not ok:
        raise ValueError("foundation graph scope review: " + reason)


def build() -> dict:
    manifest = ROOT / "data/multiverse_graph/manifest.json"
    graph_file = ROOT / "data/multiverse_graph/multiverse_graph.json"
    coverage_file = ROOT / "data/lore_research/story_coverage_inventory_2026-10-30.json"
    chronology_file = ROOT / "data/lore_research/source_event_sequences_2026-10-30.json"
    graph, coverage, chronology = j(graph_file), j(coverage_file), j(chronology_file)
    dispositions, disputes = j(DISPOSITIONS), j(DISPUTES)
    expected = {x["id"]: x for x in disputes["disputes"]}
    decisions = {x["id"]: x["decision"] for x in dispositions["dispositions"]}
    require(len(dispositions["dispositions"]) == len(decisions) == 7 and set(decisions) == set(expected)
            and decisions == EXPECTED_DECISIONS, "missing or changed conservative genealogy decisions")
    require(dispositions["canon_claims_promoted"] == 0 and dispositions["deck_pilots_approved"] == 0
            and dispositions["overall_foundation_certified"] is False,
            "owner decisions promoted unsupported claims or deck approvals")

    paths = [ROOT / p for p in j(manifest)["claim_packs"]
             if Path(p).name.startswith(PACK_PREFIXES)]
    require(len(paths) == 5 and {p.name[:6] for p in paths} == {"pack_a", "pack_b", "pack_c"},
            "foundation packs missing or unexpected")
    raw = [j(p) for p in paths]
    sources = {}
    for pack in raw:
        for key, item in pack["source_register"].items():
            url = item.get("url", "")
            parts = urlsplit(url)
            require(parts.scheme == "https" and parts.hostname in ("magic.wizards.com", "www.magic.wizards.com"),
                    "non-Wizards foundation source: " + str(url))
            if key in sources:
                require(sources[key] == url, "source ID collision: " + key)
            sources[key] = url

    nodes = {n["id"]: n for n in graph["nodes"] if n["type"] == "Claim"}
    edges = {e["claim"] for e in graph["edges"] if e.get("claim")}
    seen, by_pack, graded = set(), Counter(), Counter()
    for path, pack in zip(paths, raw):
        part = path.name.split("_", 2)[1]
        for claim in pack["claims"]:
            ident, grade, used = claim["id"], claim["grade"], claim.get("source_ids", [])
            require(ident not in seen and grade in GRADES and used and all(s in sources for s in used),
                    "duplicate, uncited or ungraded claim: " + ident)
            require("claim:" + ident in nodes and nodes["claim:" + ident]["grade"] == grade and ident in edges,
                    "claim not represented with same grade in graph: " + ident)
            require(bool(claim.get("limitation")) if grade != "CANON_CONFIRMED" else True,
                    "uncertain claim without a limitation: " + ident)
            seen.add(ident)
            graded[grade] += 1
            by_pack[part] += 1
    require(len(seen) >= 78 and all(by_pack[p] >= n for p, n in (("a", 32), ("b", 18), ("c", 28))),
            "foundational cited claim coverage regressed")
    require(graph["stats"]["non_wizards_sources"] == 0 and graph["stats"]["claim_edges_with_in_universe_date"] > 0,
            "graph provenance or in-world time disappeared")
    totals, sequence = coverage["totals"], chronology["counts"]
    require(totals["cited_pages"] + totals["reviewed_no_claim_pages"] == totals["pages"] >= 626,
            "inventoried official story pages not all accounted for")
    require(sequence["events"] >= 155 and sequence["strict_edges"] >= 126 and
            sequence["ordered_pairs"] >= 525 and sequence["ordered_pairs"] < sequence["total_pairs"],
            "evidence-local chronology lost reachability or unknown pairs")

    audit = {"schema": "foundation-graph-scope-review/v1", "reviewed_on": "2026-11-01",
             "status": "BOUNDED_FOUNDATION_GRAPH_ACCEPTED_WITH_EXPLICIT_UNKNOWN_CANON",
             "scope": "SEARCHABLE_GRADED_PACK_A_B_C_CONNECTIONS_NOT_COMPLETE_GENEALOGY_OR_GLOBAL_CHRONOLOGY",
             "owner_decision": "APPROVED_AS_DOCUMENTED_UNDER_CORY_NOVEMBER_1_INSTRUCTION",
             "foundational_claims": len(seen), "claims_by_pack": dict(sorted(by_pack.items())),
             "claim_grades": dict(sorted(graded.items())), "distinct_official_source_ids": len(sources),
             "registered_graph_claims": sum(graph["stats"]["claims_by_status"].values()),
             "source_pages_accounted_for": totals["pages"],
             "source_local_events": sequence["events"], "source_local_proven_strict_pairs": sequence["ordered_pairs"],
             "source_local_total_pairs": sequence["total_pairs"],
             "conservative_genealogy_decisions": decisions,
             "input_sha256": {p.relative_to(ROOT).as_posix(): digest(p) for p in
                              [manifest, graph_file, coverage_file, chronology_file, DISPUTES, DISPOSITIONS, *paths]},
             "out_of_scope": ["Unproven twins' parentage, full Elder Dragon survivor count and all other GD2-GD7 assertions",
                              "Ordering Old Phyrexia's decimation against Yawgmoth's end without a direct source",
                              "A complete worldwide or cross-plane chronology, exhaustive canon, or present-day status",
                              "Any lore-deck, Commander-legal-list or Grixis deck approval"],
             "overall_foundation_certified": False}
    return audit


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true")
    a = p.parse_args()
    body = build()
    text = json.dumps(body, indent=2, ensure_ascii=False) + "\n"
    if a.check:
        require(OUT.is_file() and OUT.read_text(encoding="utf-8") == text, "committed scope review stale")
    else:
        OUT.write_text(text, encoding="utf-8")
    print(f"PASS bounded foundation graph review: {body['foundational_claims']} cited A/B/C claims; "
          f"{len(body['conservative_genealogy_decisions'])} conservative owner decisions; NOT CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
