#!/usr/bin/env python3
"""Replay conservative, source-graded set-to-Multiverse navigation (K055).

Only official story publications explicitly titled for a set are joined to
their cited graph claims. Their characters/planes/factions are *source-local
claim associations*, not assertions about every printing in that set.
Wizards mechanic features and Commander products are separately pinned to
first-party pages and cross-checked against frozen Scryfall product metadata.
Unsupported codes have an explicit unknown result, never a guessed lore join.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
BRIDGE = ROOT / "data/set_atlas/phase1b_release_scope_story_bridge_2026-10-29.json"
CATALOG = ROOT / "data/set_atlas/product_catalog_2026-10-29.json"
GRAPH = ROOT / "data/multiverse_graph/multiverse_graph.json"
SOURCES = ROOT / "data/set_atlas/set_context_primary_sources_2026-11-01.json"
OUT = ROOT / "data/release/set_multiverse_context_acceptance_2026-11-01.json"
OFFICIAL = {"magic.wizards.com", "www.magic.wizards.com"}
ENTITY_TYPES = {"Character", "Plane", "Faction"}
GRADES = {"CANON_CONFIRMED", "CANON_IMPLIED", "CANON_DISPUTED", "OPEN_QUESTION",
          "ALTERNATE_CONTINUITY", "HYPOTHETICAL"}
PINNED_MECHANICS = {
    "blb": ("bloomburrow-mechanics", {"Offspring", "Forage", "Valiant"}),
    "bro": ("the-brothers-war-mechanics", {"Prototype", "Powerstones"}),
    "tdm": ("tarkir-dragonstorm-mechanics", {"Endure", "Behold", "Mobilize", "Harmonize", "Omens"}),
}
PINNED_COMMANDER = ("tdm", "tdc", "tarkir-dragonstorm-commander-decklists")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def official(url: str) -> bool:
    p = urlparse(url)
    return p.scheme == "https" and p.hostname in OFFICIAL and not p.username and not p.password


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(bridge_path: Path = BRIDGE, catalog_path: Path = CATALOG,
          graph_path: Path = GRAPH, sources_path: Path = SOURCES) -> dict:
    b, c, g, s = map(load, (bridge_path, catalog_path, graph_path, sources_path))
    sets = c["sets"]
    if b.get("all_set_codes") != len(sets) or len(sets) != 1062:
        raise ValueError("Scryfall catalog and reviewed bridge code counts disagree")
    if s.get("schema") != "set-context-official-links/v1":
        raise ValueError("unreviewed official-links specification")
    nodes = {n["id"]: n for n in g["nodes"]}
    url_sources = defaultdict(list)
    for n in nodes.values():
        if n["type"] == "Source" and n.get("url") and official(n["url"]):
            url_sources[n["url"]].append(n["id"])
    source_claims = defaultdict(set)
    claim_entities = defaultdict(list)
    for e in g["edges"]:
        if e["relation"] == "cited_by" and e["from"] in nodes and e["to"] in nodes:
            source_claims[e["from"]].add(e["to"])
        if e["relation"] == "asserts" and e["from"] in nodes and e["to"] in nodes:
            n = nodes[e["to"]]
            if n["type"] in ENTITY_TYPES:
                claim_entities[e["from"]].append((n, e.get("role", "unknown")))

    mechanics = {}
    if set(x["set_code"] for x in s["mechanics"]) != set(PINNED_MECHANICS):
        raise ValueError("unexpected mechanics source coverage")
    for x in s["mechanics"]:
        code = x["set_code"]
        slug, names = PINNED_MECHANICS[code]
        if (code not in sets or sets[code]["scryfall_set_type"] != "expansion"
                or not official(x["source_url"]) or not x["source_url"].endswith("/" + slug)
                or set(x["mechanic_labels"]) != names
                or len(x["mechanic_labels"]) != len(names)):
            raise ValueError("unverified or inflated mechanics source: " + code)
        mechanics[code] = x

    commander = {}
    if len(s["commander_product_links"]) != 1:
        raise ValueError("unexpected Commander product sources")
    for x in s["commander_product_links"]:
        parent, child, slug = PINNED_COMMANDER
        if (x["parent_set_code"] != parent or x["commander_set_code"] != child
                or not official(x["source_url"]) or not x["source_url"].endswith("/" + slug)
                or sets[child]["parent_set_code"] != parent
                or sets[child]["scryfall_set_type"] != "commander"):
            raise ValueError("unverified Commander source or Scryfall parent link")
        commander[parent] = x

    scoped = {}
    entity_total, link_count = Counter(), 0
    for code, story in sorted(b["wizards_story_series_set_links"].items()):
        if code not in sets or story.get("official_story_count_in_recovered_index", 0) <= 0:
            raise ValueError("unreviewed story release code: " + code)
        sample = story["sample_first_party_story_sources"]
        if not sample or story["connection_scope"].find("no card-lore") < 0:
            raise ValueError("story publication scope must remain explicitly limited")
        associations, story_urls = [], set()
        for page in sample:
            url = page["url"]
            if not official(url) or url in story_urls or url not in url_sources:
                raise ValueError("missing, duplicated or nonofficial story citation: " + url)
            story_urls.add(url)
            for source_id in url_sources[url]:
                if nodes[source_id].get("source_class") != "WIZARDS_OFFICIAL":
                    raise ValueError("story source was not first-party graded")
                for claim_id in source_claims[source_id]:
                    claim = nodes[claim_id]
                    if claim["type"] != "Claim" or claim.get("grade") not in GRADES:
                        raise ValueError("ungraded graph claim cannot become set context")
                    for entity, role in claim_entities[claim_id]:
                        if role not in {"subject", "object"}:
                            raise ValueError("unreviewed claim-entity evidence role")
                        associations.append({
                            "entity_id": entity["id"], "entity_name": entity["name"],
                            "entity_type": entity["type"], "claim_id": claim_id,
                            "claim_grade": claim["grade"], "claim_summary": claim["name"],
                            "claim_role": role, "official_story_url": url,
                            "association_not_set_card_canon": True,
                        })
        associations.sort(key=lambda x: (x["entity_type"], x["entity_id"], x["claim_id"], x["official_story_url"]))
        for a in associations:
            entity_total[a["entity_type"]] += 1
        link_count += len(story_urls)
        scoped[code] = {
            "set_name": sets[code]["name"], "set_type": sets[code]["scryfall_set_type"],
            "official_publication_series": story["series_name_as_published"],
            "official_stories_in_recovered_index": story["official_story_count_in_recovered_index"],
            "sample_story_source_urls": sorted(story_urls),
            "source_claim_entity_associations": associations,
            "mechanics_official_feature": mechanics.get(code),
            "related_commander_product": commander.get(code),
            "unknowns": ["No inferred connections to individual cards, undocumented planes or other set codes.",
                         "Publication year and set release date are not in-universe event dates."],
        }
    if set(scoped) != {"blb", "bro", "dft", "eoe", "lci", "mat", "mkm", "mom", "one", "otj", "tdm", "woe"}:
        raise ValueError("story-series roster drifted without new source review")
    if link_count != 35 or not all(entity_total[k] for k in ENTITY_TYPES):
        raise ValueError("incomplete official page/typed entity association evidence")
    return {
        "schema": "set-multiverse-context-acceptance/v1", "as_of": "2026-11-01",
        "input_sha256": {p.name: sha(p) for p in (bridge_path, catalog_path, graph_path, sources_path)},
        "counts": {"all_scryfall_codes_queryable": len(sets), "official_story_series_sets": len(scoped),
                   "official_story_sample_pages": link_count,
                   "typed_claim_entity_associations": dict(sorted(entity_total.items())),
                   "sets_with_verified_mechanics_feature": len(mechanics),
                   "official_related_commander_product_links": len(commander)},
        "scope": "First-party publication and cited-claim navigation for 12 named releases; three mechanics features and one Commander product link; unknown elsewhere, not exhaustive set canon.",
        "sets_with_verified_context": scoped,
        "limitations": [
            "A Wizards story series named for a set identifies a publication relationship, not a claim about every card or a universal plane/faction roster.",
            "A graph entity appears only because a cited claim structurally references it; grade and source URL remain visible, including disputes and alternate continuity.",
            "Mechanics are attested on three named Wizards feature pages, not automatically assigned to every printing in the set.",
            "The Scryfall parent_set_code plus an official Wizards decklist page connects one Commander product; it does not approve the project's pilot decks.",
            "The other set codes are explicitly unknown for lore context; a shared name, release year, parent link or story-art filename is not proof of canon.",
        ],
    }


def query(code: str, report: dict | None = None, catalog_path: Path = CATALOG) -> dict:
    data = report if report is not None else build()
    sets = load(catalog_path)["sets"]
    code = code.strip().lower()
    if code not in sets:
        raise KeyError("unknown frozen Scryfall set code: " + code)
    context = data["sets_with_verified_context"].get(code)
    return {"code": code, "set_name": sets[code]["name"],
            "category": sets[code]["scryfall_set_type"],
            "parent_set_code": sets[code]["parent_set_code"],
            "evidence_status": "SOURCE_GRADED_PARTIAL_CONTEXT" if context else "NO_VERIFIED_STORY_CONTEXT_IN_THIS_SNAPSHOT",
            "context": context,
            "inferred_canon": False}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true")
    p.add_argument("--code", help="query a set code; unsupported contexts are explicitly unknown")
    args = p.parse_args(argv)
    data = build()
    if args.code:
        print(json.dumps(query(args.code, data), indent=2, ensure_ascii=False))
        return 0
    encoded = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != encoded:
            raise ValueError("set Multiverse context acceptance is stale")
        print("PASS first-party set-context: 12 story series, 35 pages, three mechanics features, one Commander product")
    else:
        OUT.write_text(encoded, encoding="utf-8")
        print("Wrote " + str(OUT.relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
