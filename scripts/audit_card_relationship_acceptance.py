#!/usr/bin/env python3
"""Independent, bounded card/art and directional time-qualified graph acceptance.

K064 and K069 verify *available evidence*; they do not assert that every card
depicts a story scene or that an undated source implies a calendar year.
The existing graph, official quotes, exact printing UUIDs and flavor metadata
are checked independently; the query surface must keep those grades visible.

    python3 scripts/audit_card_relationship_acceptance.py
    python3 scripts/audit_card_relationship_acceptance.py --check
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from query_multiverse_graph import MG

OUT = ROOT / "data/release/card_relationship_acceptance_2026-11-01.json"
GRAPH = ROOT / "data/multiverse_graph/multiverse_graph.json"
MANIFEST = ROOT / "data/multiverse_graph/manifest.json"
ART = ROOT / "data/lore_research/pack_a4_printing_art_matches_2026-10-30.json"
IMAGE_LABELS = ROOT / "data/lore_research/story_image_label_printings_2026-10-30.json"
CARD_LINKS = ROOT / "data/lore_research/card_lore_links_2026-10-30.json"
OFFICIAL = ("https://magic.wizards.com/", "https://www.magic.wizards.com/")
UNCERTAINTY = {"CANON_IMPLIED", "CANON_DISPUTED", "OPEN_QUESTION", "ALTERNATE_CONTINUITY", "HYPOTHETICAL"}
DIRECT = {"DIRECT_EVENT_SCENE_CAPTION"}
NAVIGATION = {"named_on_card", "art_file_used_on_official_page", "has_printing", "art_captioned_in_story",
              "exact_art_published_in_story", "proposed_in"}


def load(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def require(value, message: str):
    if not value:
        raise ValueError("card/relationship acceptance: " + message)


def build(graph_path: Path = GRAPH) -> dict:
    graph = load(graph_path)
    m = load(MANIFEST)
    nodes = {n["id"]: n for n in graph["nodes"]}
    edges = graph["edges"]
    require(len(nodes) == len(graph["nodes"]) and not graph["problems"], "duplicate/broken graph nodes")
    sources = {k.split(":", 1)[1]: v for k, v in nodes.items() if k.startswith("source:")}
    claims = {c["id"]: c for p in m["claim_packs"] for c in load(ROOT / p)["claims"]}
    claim_nodes = {k.removeprefix("claim:"): v for k, v in nodes.items() if k.startswith("claim:")}
    require(len(claims) == len(claim_nodes), "claim research/graph count mismatch")

    # All claim relationships must retain direction, original grade and a
    # first-party source; uncertainty must not be upgraded during graph build.
    claim_edges = [e for e in edges if e.get("claim")]
    require(len(claim_edges) >= 1300, "sourced directional relations lost")
    dates, undated = [], 0
    for e in claim_edges:
        c = claims.get(e["claim"])
        require(c is not None and e["grade"] == claim_nodes[e["claim"]]["grade"], "missing or inflated claim grade")
        require(e["from"] in nodes and e["to"] in nodes and e["sources"], "unbound directed edge")
        for sid in e["sources"]:
            src = sources.get(sid)
            require(src and src["source_class"] == "WIZARDS_OFFICIAL"
                    and src["url"].startswith(OFFICIAL) and sid in c["source_ids"], "nonofficial or unrelated claim citation")
        t = e.get("in_universe_date")
        if not t:
            undated += 1
            continue
        require(set(t) == {"value", "quote", "source_id"} and t["source_id"] in e["sources"],
                "date missing explicit source/quote")
        require(t["value"] in t["quote"] and any(
            ev["source_id"] == t["source_id"] and ev["quote"] == t["quote"] for ev in c["evidence"]),
            "date phrase not verbatim in the claim's own official-source quotation")
        dates.append(e)
    require(len(dates) >= 36 and undated > 1000, "date scope unexpectedly changed without review")

    by_relation = Counter(e["relation"] for e in claim_edges)
    require({"allied_with", "created", "fought", "member_of"} <= set(by_relation),
            "representative relationship verbs absent")

    # Official image-file use is *printing-specific*, but never promotes an
    # illustrated scene to a canon event. Original label mismatches remain open.
    labels = load(IMAGE_LABELS)
    matched = [r for r in labels["labels"] if r["status"] == "MATCHED"]
    print_edges = [e for e in edges if e["relation"] == "has_printing"]
    art_edges = [e for e in edges if e["relation"] == "art_file_used_on_official_page"]
    require(len(matched) == len(art_edges) == 570 and len(print_edges) == 560,
            "exact label/printing atlas count drift")
    require(len({e["to"] for e in art_edges}) == len(print_edges), "unreconciled exact printing UUIDs")
    for e in art_edges:
        src, pr = nodes[e["from"]], nodes[e["to"]]
        require(src["type"] == "Source" and src.get("source_class") == "WIZARDS_OFFICIAL"
                and pr["type"] == "CardRepresentation" and pr["scryfall_id"] in e["to"],
                "art file not anchored to a first-party page and exact printing")
        require("not a statement" in e["limitation"], "image label cannot certify a depicted event")
    require(sum(r["status"] != "MATCHED" for r in labels["labels"]) == 7,
            "seven originally unresolved labels silently erased")

    name_edges = [e for e in edges if e["relation"] == "named_on_card"]
    captions = [e for e in edges if e["relation"] == "art_captioned_in_story"]
    require(len(name_edges) >= 701 and len(captions) >= 1025, "card/official-caption navigation missing")
    require(all(not e.get("grade") and e["relation"] in NAVIGATION for e in name_edges + captions + art_edges),
            "navigational card links must not be canon claims")

    depicted = [e for e in edges if e["relation"] == "depicted_by"]
    require(len(depicted) == 15 and sum(e.get("tier") in DIRECT for e in depicted) == 1,
            "direct scene caption must remain distinct from named art/character cards")
    for e in depicted:
        require(e.get("tier") and e.get("sources") and not e.get("grade"),
                "art grade inflated to narrative canon")
        require(all(s in sources and sources[s]["source_class"] == "WIZARDS_OFFICIAL" for s in e["sources"]),
                "art context lacks an official source")
    a4 = load(ART)
    story_art = [e for e in edges if e["relation"] == "exact_art_published_in_story"]
    require(len(a4["cards"]) == len(story_art) == 6, "six directly visually reviewed printings lost")
    for c in a4["cards"]:
        found = [e for e in story_art if e.get("printing") == c["visually_reviewed_printing"]["id"]]
        require(len(found) == 1 and found[0]["tier"] == c["context_tier"],
                "reviewed exact-art context cannot be inferred from a same-art reprint")

    links = load(CARD_LINKS)
    require(links["counts"]["LINKED"] >= 208 and links["counts"]["NO_LORE_YET"] >= 2626,
            "card-lore graded link limits lost")
    require(links["counts"]["tier:CLAIM_ANCHORED"] >= 132 and
            links["counts"]["tier:OFFICIAL_TEXT_NAMES_CARD"] >= 48,
            "claim and official named text routes missing")
    flavor = 0
    for rel in m["deck_evidence"]:
        ev = load(ROOT / rel)
        require(ev["status"].startswith("UNAPPROVED"), "deck narrative approval must remain deferred")
        flavor += sum(bool(c["printing"].get("printed_flavor")) for c in ev["cards"])
    require(flavor >= 20, "frozen printed flavor metadata missing")

    # An actual query must carry the exact quoted relative marker and return
    # UNKNOWN/NOT STATED for undated citations. No calendar date guessed.
    mg = MG(graph_path)
    qualified = mg.neighbors("Nicol Bolas", include_temporal=True)
    require(any(r["claim"] == "AKH017" and r["in_universe_date"]["value"] == "Several decades ago"
                and r["time_qualification"] == "QUOTED_SOURCE_LOCAL_SPAN" for r in qualified),
            "dated relationship hidden by public query")
    require(any(r["claim"] and r["time_qualification"] == "SOURCE_NOT_DATED" for r in qualified),
            "undated relationship lost its explicit unknown marker")
    crux = mg.card("Crux of Fate", include_temporal=True)
    require(any(r["tier"] == "DIRECT_EVENT_SCENE_CAPTION" for r in crux["relationships"]),
            "direct source caption missing in card query")
    require(any(r["tier"] == "OFFICIAL_IMAGE_LABEL_PRINTING_MATCH" for r in mg.printing("fra", "358")[0]["relationships"]),
            "exact indexed printing cannot navigate back to official art source")

    return {"schema": "card-relationship-evidence-acceptance/v1", "as_of": "2026-11-01",
            "scope": "Committed source-graded links and source-local dated graph relationships; not exhaustive canon or calendar chronology",
            "criteria": {
                "K064_card_story_art_flavor_links": "PASS_BOUNDED_EVIDENCE_TIERS_WITH_UNRESOLVED_LABELS_PRESERVED",
                "K069_directional_source_local_time": "PASS_DIRECTIONAL_OFFICIAL_CLAIMS_WITH_QUOTED_RELATIVE_SPANS_AND_UNKNOWN_UNDATED"},
            "counts": {"claim_relationship_edges": len(claim_edges), "dated_relationship_edges": len(dates),
                       "undated_relationship_edges": undated, "distinct_dated_claims": len({e["claim"] for e in dates}),
                       "direct_event_scene_caption_links": 1, "named_or_contextual_depicted_by_links": len(depicted) - 1,
                       "visually_reviewed_exact_art": len(story_art), "official_image_file_labels_matched": len(art_edges),
                       "distinct_exact_printings": len(print_edges), "unresolved_image_labels": 7,
                       "named_card_navigation_edges": len(name_edges), "official_story_art_caption_edges": len(captions),
                       "curated_card_lore_linked": links["counts"]["LINKED"],
                       "curated_card_without_lore_link": links["counts"]["NO_LORE_YET"],
                       "pilot_exact_printing_flavor_records": flavor},
            "non_date_relationship_verbs": dict(sorted(by_relation.items())),
            "input_sha256": {str(p.relative_to(ROOT)): sha(p) for p in (GRAPH, MANIFEST, ART, IMAGE_LABELS, CARD_LINKS)},
            "limitations": [
                "A named character card or art label is navigation, not a verified depiction of an in-story action.",
                "Only one directly captioned *event* scene is asserted; other 14 depicted_by links retain their non-event tiers.",
                "Printed flavor is a dated printing fact, not independent proof that its narration is canon truth.",
                "Thirty-six edges have attested relative phrases from 35 claims, not global calendar years or 1,306 fully dated relationships.",
                "A source-local phrase may describe a sentence's context rather than every clause; unquoted dates stay unknown.",
                "Most card records have no verified direct story link; seven unmatched historical image labels remain unresolved.",
                "The three lore decks remain UNAPPROVED and the protected 62 Grixis decks are not modified."]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    result = build()
    content = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if OUT.read_text(encoding="utf-8") != content:
            raise ValueError("card/relationship acceptance report stale")
        print("PASS bounded K064/K069 links: exact art/printings, grade, official source and explicit relative dates")
    else:
        OUT.write_text(content, encoding="utf-8")
        print("Wrote " + str(OUT.relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
