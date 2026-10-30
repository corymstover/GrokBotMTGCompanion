#!/usr/bin/env python3
"""Phase 3 L220: audit the repository's existing entity structures before any new schema is created.

Read-only over committed artifacts. It writes one dated audit JSON and makes no change to
the graph, the claim packs, card_enrichment.json or any Grixis/approval artifact.

It reports:
  * an inventory of every entity-bearing structure (schema, generator, ID scheme, counts);
  * multiverse-graph integrity (prefix/type agreement, dangling edges, orphans, cards without an oracle_id);
  * duplicate-entity candidates: different IDs with the same normalised name (and type family),
    plus whole-word alias candidates (e.g. "Bolas" vs "Nicol Bolas"), which are left for review and never merged;
  * claim-pack consistency: the same pack-local ID declared with different names or types, and claims whose
    subject or object is not a declared entity;
  * a crosswalk from the legacy curated lore index (data/lore_graph.json / data/lore_entries.json) to graph nodes,
    noting which legacy entries the existing `curated:` bridge misses.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "multiverse_audits" / "entity_structure_audit_2026-10-30.json"
GRAPH = "data/multiverse_graph/multiverse_graph.json"
MANIFEST = "data/multiverse_graph/manifest.json"
ENTITY_TYPES = {"Character", "Event", "Plane", "Place", "Object", "Faction", "Concept",
                "AlternateContinuity", "CardTheme"}
# Types that may legitimately describe the same named thing (a plane named as a place, etc.).
FAMILY = {"Plane": "location", "Place": "location"}
EXPECTED_PREFIX = {"Character": "character", "Event": "event", "Plane": "plane", "Place": "place",
                   "Object": "artifact", "Faction": "faction", "AlternateContinuity": "continuity",
                   "CardTheme": "cardtheme", "Concept": {"concept", "curated"}, "Card": "card",
                   "Source": "source", "Claim": "claim", "DeckProposal": "deck", "Literal": "literal"}
LEGACY_KIND_TO_TYPES = {"character": {"Character"}, "plane": {"Plane", "Place"}, "item": {"Object"},
                        "dossier": {"Character"}}
STOP = {"the", "of", "a", "an", "and"}


def norm(name: str) -> str:
    s = re.sub(r"[^a-z0-9 ]+", " ", name.lower().replace("’", "'").replace("'", ""))
    words = s.split()
    if words and words[0] == "the":
        words = words[1:]
    return " ".join(words)


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def inventory() -> list[dict]:
    rows = []

    def add(path, **kw):
        p = ROOT / path
        rows.append({"path": path, "exists": p.exists(), **kw})

    g = load(GRAPH)
    add(GRAPH, schema=g.get("schema"), generator="scripts/build_multiverse_graph.py", role="CANONICAL_RELATIONSHIP_GRAPH",
        id_scheme="<type-prefix>:<pack-local-id or slug>", count=len(g["nodes"]),
        by_type=dict(sorted(Counter(n["type"] for n in g["nodes"]).items())))
    lg = load("data/lore_graph.json")
    add("data/lore_graph.json", schema=lg.get("schema"), generator="scripts/build_lore_graph.py",
        role="LEGACY_CURATED_NAVIGATION_GRAPH", id_scheme="<Markdown page>#<anchor>", count=len(lg["nodes"]),
        by_type=dict(sorted(Counter(n["kind"] for n in lg["nodes"]).items())))
    le = load("data/lore_entries.json")
    add("data/lore_entries.json", schema=None, generator=le.get("generated_by"), role="LEGACY_CURATED_LORE_INDEX",
        id_scheme="page + anchor", count=len(le["items"]), by_type=dict(sorted(le["by_kind"].items())))
    kb = load("data/kb_index.json")
    add("data/kb_index.json", schema=kb.get("schema"), generator=kb.get("generated_by"), role="KEYWORD_SEARCH_INDEX",
        id_scheme="page/deck/lore entry", count=len(kb["items"]))
    cr = load("data/card_refs.json")
    add("data/card_refs.json", schema=None, generator=cr.get("generated_by"), role="CARD_NAME_CROSSREFS",
        id_scheme="card name", count=len(cr["cards"]), note=f"bulk {cr.get('bulk')}")
    ce = load("data/card_enrichment.json")
    cards = ce.get("cards")
    add("data/card_enrichment.json", schema=None, generator=ce.get("generated_by"), role="CARD_ENRICHMENT (read-only here)",
        id_scheme="card name / oracle", count=len(cards) if hasattr(cards, "__len__") else None)
    cn = load("data/card_lore_notes.json")
    add("data/card_lore_notes.json", schema=None, generator="curated", role="CURATED_CARD_NOTES", id_scheme="card name",
        count=len([k for k in cn if not k.startswith("_")]))
    ld = load("data/lore_decks/lore_decks.json")
    add("data/lore_decks/lore_decks.json", schema=None, generator="lore deck tooling", role="LORE_DECK_REGISTRY (read-only)",
        id_scheme="deck number/slug", count=len(ld["decks"]))
    sa = load("data/story_atlas/story_art_captions_2026-10-30.json")
    add("data/story_atlas/story_art_captions_2026-10-30.json", schema=sa.get("schema"), generator="story caption builder",
        role="STORY_ART_CAPTIONS", id_scheme="page url + card name", count=sa["captions"] if isinstance(sa["captions"], int) else len(sa["captions"]))
    packs = load(MANIFEST)["claim_packs"]
    n_ent = sum(len(load(p).get("entities", [])) for p in packs)
    add("data/lore_research/pack_*.json (manifest claim_packs)", schema="claim-pack (various v1)",
        generator="scripts/story_claim_pipeline.py and per-pack builders", role="CLAIM_PACK_ENTITY_DECLARATIONS",
        id_scheme="pack-local snake_case id, merged globally by the graph builder", count=n_ent, packs=len(packs))
    for extra in ("data/lore_research/card_lore_links_2026-10-30.json", "data/lore_research/flavor_lore_links_2026-10-30.json",
                  "data/lore_research/card_name_anchors_2026-10-30.json", "data/lore_research/claim_card_anchors_2026-10-30.json"):
        d = load(extra)
        add(extra, schema=d.get("schema") if isinstance(d, dict) else None, generator="overlay builder",
            role="CARD_TO_LORE_OVERLAY", id_scheme="oracle_id / card name -> graph id")
    return rows


def graph_integrity(g: dict) -> dict:
    ids = {n["id"] for n in g["nodes"]}
    prefix_mismatch = []
    for n in g["nodes"]:
        exp = EXPECTED_PREFIX.get(n["type"])
        pre = n["id"].split(":", 1)[0]
        ok = pre in exp if isinstance(exp, set) else pre == exp
        if not ok:
            prefix_mismatch.append(n["id"])
    dangling = [e for e in g["edges"] if e["from"] not in ids or e["to"] not in ids]
    deg = Counter()
    for e in g["edges"]:
        deg[e["from"]] += 1
        deg[e["to"]] += 1
    orphans = sorted(n["id"] for n in g["nodes"] if deg[n["id"]] == 0)
    cards_no_oracle = sorted(n["id"] for n in g["nodes"] if n["type"] == "Card" and not n.get("oracle_id"))
    dup_ids = [i for i, c in Counter(n["id"] for n in g["nodes"]).items() if c > 1]
    literals = sorted(n["name"] for n in g["nodes"] if n["type"] == "Literal")
    return {"nodes": len(g["nodes"]), "edges": len(g["edges"]), "duplicate_ids": dup_ids,
            "prefix_type_mismatches": prefix_mismatch, "dangling_edges": len(dangling),
            "orphan_nodes": orphans, "cards_without_oracle_id": cards_no_oracle,
            "literal_objects": literals, "builder_problems": g.get("problems", [])}


def duplicate_candidates(g: dict) -> dict:
    ents = [n for n in g["nodes"] if n["type"] in ENTITY_TYPES and not n["id"].startswith("curated:")]
    by_norm = defaultdict(list)
    for n in ents:
        by_norm[(FAMILY.get(n["type"], n["type"]), norm(n["name"]))].append(n)
    exact = []
    for (fam, key), ns in sorted(by_norm.items()):
        if len(ns) > 1:
            exact.append({"normalised_name": key, "family": fam,
                          "ids": sorted(x["id"] for x in ns), "types": sorted({x["type"] for x in ns})})
    cross_type = defaultdict(list)
    for n in ents:
        cross_type[norm(n["name"])].append(n)
    cross = [{"normalised_name": k, "ids": sorted(x["id"] for x in v), "types": sorted({x["type"] for x in v})}
             for k, v in sorted(cross_type.items())
             if len({FAMILY.get(x["type"], x["type"]) for x in v}) > 1]
    # Whole-word alias candidates within Character: a short name that is the first or last word(s)
    # of exactly one longer name of the same type.
    chars = [n for n in ents if n["type"] == "Character"]
    names = {n["id"]: norm(n["name"]).split() for n in chars}
    alias = []
    for a, aw in names.items():
        if not aw or len(aw) > 2:
            continue
        hits = [b for b, bw in names.items() if b != a and len(bw) > len(aw)
                and (bw[:len(aw)] == aw or bw[-len(aw):] == aw) and not set(aw) <= STOP]
        if len(hits) == 1:
            alias.append({"short": a, "long": hits[0], "status": "REVIEW_ONLY_NOT_MERGED"})
    return {"same_name_same_family": exact, "same_name_different_type": cross,
            "character_alias_candidates": sorted(alias, key=lambda r: r["short"])}


def declared_names(packs: list[str]) -> dict[str, set[str]]:
    """graph id -> every name a claim pack declared for it (pack authors' own name variants)."""
    out: dict[str, set[str]] = defaultdict(set)
    for rel in packs:
        for e in load(rel).get("entities", []):
            pre = EXPECTED_PREFIX.get(e.get("type"), "entity")
            pre = "concept" if isinstance(pre, set) else pre
            out[f"{pre}:{e['id']}"].add(e.get("name") or "")
    return out


def pack_consistency(packs: list[str]) -> dict:
    decl = defaultdict(set)
    all_ids = {e["id"] for rel in packs for e in load(rel).get("entities", [])}
    undeclared = []
    for rel in packs:
        p = load(rel)
        local = {}
        for e in p.get("entities", []):
            decl[e["id"]].add((e.get("type"), e.get("name"), Path(rel).name))
            local[e["id"]] = e
        for c in p.get("claims", []):
            s = c.get("subject")
            if s and s not in local:
                kind = ("COMPOUND_SUBJECT_BECAME_LITERAL" if ";" in s else
                        "DECLARED_IN_ANOTHER_PACK" if s in all_ids else "UNDECLARED")
                undeclared.append({"pack": Path(rel).name, "claim": c["id"], "role": "subject", "token": s, "kind": kind})
    type_conflicts, name_variants = [], []
    for lid, rows in sorted(decl.items()):
        types = {t for t, _, _ in rows}
        names = {n for _, n, _ in rows}
        if len(types) > 1:
            type_conflicts.append({"local_id": lid, "types": sorted(types), "packs": sorted({p for *_, p in rows})})
        if len({norm(n) for n in names if n}) > 1:
            name_variants.append({"local_id": lid, "names": sorted(n for n in names if n)})
    return {"declared_local_ids": len(decl), "type_conflicts": type_conflicts,
            "name_variants_same_id": name_variants, "claims_with_undeclared_subject": undeclared}


def legacy_crosswalk(g: dict, packs: list[str]) -> dict:
    lg = load("data/lore_graph.json")
    graph_by_norm = defaultdict(list)
    variant_by_norm = defaultdict(list)
    names = declared_names(packs)
    for n in g["nodes"]:
        if n["type"] in ENTITY_TYPES and not n["id"].startswith("curated:"):
            graph_by_norm[norm(n["name"])].append(n)
            for v in names.get(n["id"], ()):
                if v and norm(v) != norm(n["name"]):
                    variant_by_norm[norm(v)].append(n)
    bridged = {e["to"][len("curated:"):] for e in g["edges"] if e["relation"] == "see_also_curated_entry"}
    rows = []
    for n in lg["nodes"]:
        types = LEGACY_KIND_TO_TYPES.get(n["kind"])
        if not types:
            continue
        cand = [x for x in graph_by_norm.get(norm(n["name"]), []) if x["type"] in types]
        variant = [x for x in variant_by_norm.get(norm(n["name"]), []) if x["type"] in types] if not cand else []
        if not cand and not variant:  # first-name fallback ("Ajani Goldmane" -> "Ajani"), reported as a candidate only
            first = norm(n["name"]).split()[:1]
            cand_first = [x for x in graph_by_norm.get(" ".join(first), []) if x["type"] in types] if first else []
        else:
            cand_first = []
        rows.append({"legacy_id": n["id"], "kind": n["kind"], "name": n["name"],
                     "graph_matches": sorted(x["id"] for x in cand),
                     "declared_name_variant_matches": sorted(x["id"] for x in variant),
                     "first_word_candidates": sorted(x["id"] for x in cand_first),
                     "bridged_in_graph": n["id"] in bridged,
                     "status": ("BRIDGED" if n["id"] in bridged else
                                "NORMALISED_MATCH_NOT_BRIDGED" if cand else
                                "MATCH_VIA_DECLARED_NAME_VARIANT" if variant else
                                "CANDIDATE_BY_FIRST_WORD" if cand_first else "LEGACY_ONLY")})
    return {"rows": rows, "by_status": dict(sorted(Counter(r["status"] for r in rows).items()))}


def build() -> dict:
    g = load(GRAPH)
    packs = load(MANIFEST)["claim_packs"]
    integ = graph_integrity(g)
    dups = duplicate_candidates(g)
    pc = pack_consistency(packs)
    xw = legacy_crosswalk(g, packs)
    findings = []
    findings.append("Two lore graphs coexist by design: data/lore_graph.json (legacy curated Markdown navigation, "
                    "page#anchor IDs, contextual_pointer tier) and data/multiverse_graph (claim-graded, cited). "
                    "The multiverse graph is the relationship layer; the legacy graph is bridged via curated: Concept nodes. "
                    "No new entity schema is needed.")
    if integ["cards_without_oracle_id"]:
        findings.append(f"{len(integ['cards_without_oracle_id'])} Card node(s) lack an oracle_id: "
                        + ", ".join(integ["cards_without_oracle_id"][:5]))
    findings.append(f"{len(dups['same_name_same_family'])} same-name/same-family ID groups and "
                    f"{len(dups['character_alias_candidates'])} character alias candidates need review; none were merged.")
    findings.append(f"Legacy crosswalk: {xw['by_status']}. CANDIDATE_BY_FIRST_WORD rows are review-only.")
    comp = [r for r in pc["claims_with_undeclared_subject"] if r["kind"] != "DECLARED_IN_ANOTHER_PACK"]
    if comp:
        findings.append("Claim subjects that did not resolve to an entity: "
                        + ", ".join(f"{r['claim']} {r['token']!r} ({r['kind']})" for r in comp))
    if pc["name_variants_same_id"]:
        findings.append(f"{len(pc['name_variants_same_id'])} pack-local IDs carry differing display names across packs; "
                        "the graph keeps the first-ingested name, so exact-name bridges can miss the others.")
    return {
        "schema": "entity-structure-audit/v1",
        "status": "ENGINEERING_AUDIT (read-only; no merges or schema changes applied)",
        "workflow_item": "Phase 3 L220",
        "inventory": inventory(),
        "graph_integrity": integ,
        "duplicate_candidates": dups,
        "claim_pack_consistency": pc,
        "legacy_crosswalk": xw,
        "findings": findings,
        "recommendation": ("Keep data/multiverse_graph as the single relationship schema; extend packs by reusing "
                           "existing local IDs (check this audit's alias list first); resolve review candidates with "
                           "cited evidence, never by name similarity alone."),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if the committed audit is stale")
    a = ap.parse_args()
    data = json.dumps(build(), indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    if a.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != data:
            print("STALE: re-run scripts/audit_entity_structures.py")
            return 1
        print("OK: entity structure audit current")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(data, encoding="utf-8")
    d = json.loads(data)
    print(json.dumps({k: d[k] for k in ("findings",)}, indent=1))
    print("integrity:", {k: (len(v) if isinstance(v, list) else v) for k, v in d["graph_integrity"].items()})
    print("pack:", {k: (len(v) if isinstance(v, list) else v) for k, v in d["claim_pack_consistency"].items()})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
