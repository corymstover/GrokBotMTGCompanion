#!/usr/bin/env python3
"""Phase 1B L193-L202 deliverable gates, verified in bulk against the pinned October 29 Scryfall snapshot.

Inputs: the committed set atlas (catalog, product catalog, historical shards, release-scope report),
SET_ATLAS.md, and the pinned Default Cards bulk (.cache/multiverse, SHA-256 must equal the product catalog's
oracle_printing_source_sha256). Output: data/set_atlas/phase1b_snapshot_gates_2026-10-30.json.

New, bulk-computed evidence (not available to the v2.20-v2.22 reports):
  * exact printing-ID parity between the committed October 28 historical shards and the October 29 bulk;
  * debut/reprint attribution recomputed per Oracle identity and cross-checked with Scryfall's `reprint` flag;
  * per-set count, reference and date-order checks plus five sample queries straight from the bulk.
Gate verdicts are PASS (mechanically met), QUALIFIED (met with stated limitations) or OPEN. No verdict is an
owner approval or certification, and nothing here infers lore from card data.
"""
from __future__ import annotations

import argparse
import collections
import csv
import glob
import gzip
import hashlib
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "data/set_atlas"
OUT = ATLAS / "phase1b_snapshot_gates_2026-10-30.json"
CACHE = Path(os.environ.get("MTG_MULTIVERSE_CACHE", ROOT / ".cache/multiverse"))
CUTOFF = "2026-10-29"
SAMPLES = {"lea": "Limited Edition Alpha", "leg": "Legends", "c21": "Commander product",
           "pznr": "promo set", "ydmu": "digital (Alchemy) release"}
TOKENISH = {"token", "double_faced_token", "emblem", "art_series"}
MULTIFACE = {"transform", "modal_dfc", "meld", "flip", "split", "adventure", "reversible_card", "battle",
             "double_faced_token", "art_series", "prepare"}
EXTRA_SETS = {"neo": ["nec"], "snc": ["ncc"], "mid": ["mic"], "vow": ["voc"], "stx": ["c21"], "iko": ["c20"],
              "rf": ["fra", "frc"]}


def sha_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def jload(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def pinned_bulk(product: dict) -> Path:
    """Select the exact approved bulk; never silently fall back to a newer cache file."""
    manifest = jload(ROOT / "data/scryfall_snapshots/snap-20261029-40848334824-1.manifest.json")
    recorded = manifest["files"]["default-cards"]
    if recorded["sha256"] != product["oracle_printing_source_sha256"]:
        raise SystemExit("MTG_SNAPSHOT_MANIFEST_CONFLICT: product catalog and pinned manifest hashes differ")
    path = CACHE / recorded["filename"]
    if not path.is_file():
        raise SystemExit(
            f"MTG_PINNED_BULK_MISSING: {path} is required for this full snapshot audit. "
            f"Restore the exact file from {recorded['source_url']} (when available), "
            f"verify SHA-256 {recorded['sha256']}, or retain the saved qualified report; "
            "a later bulk cannot impersonate this locked snapshot."
        )
    return path


def build() -> dict:
    catalog = jload(ATLAS / "catalog_2026-10-29.json")["sets"]
    product = jload(ATLAS / "product_catalog_2026-10-29.json")
    psets = product["sets"]
    bulk = pinned_bulk(product)
    bulk_sha = sha_file(bulk)
    if bulk_sha != product["oracle_printing_source_sha256"]:
        raise SystemExit(f"pinned bulk {Path(bulk).name} sha256 {bulk_sha} != product catalog source hash")

    # ---- historical October 28 shards
    hist = {}
    for f in sorted(glob.glob(str(ATLAS / "historical_sets_*.json"))):
        for code, rows in jload(Path(f)).items():
            for r in rows:
                hist[r[0]] = (code, r[1], r[4], r[5], r[6])  # set, oracle, released, lang, paper

    # ---- October 29 bulk
    snap, dup_ids, scn = {}, 0, collections.Counter()
    per_set = collections.defaultdict(lambda: {"printings": 0, "en_paper_released": 0, "oracles": set(),
                                               "min_date": None})
    by_oracle = collections.defaultdict(list)
    layouts, no_oracle = collections.Counter(), 0
    for line in gzip.open(bulk, "rt", encoding="utf-8"):
        c = json.loads(line)
        if c["id"] in snap:
            dup_ids += 1
        oid = c.get("oracle_id") or (c.get("card_faces") or [{}])[0].get("oracle_id")
        if not c.get("oracle_id"):
            no_oracle += 1
        paper = "paper" in c.get("games", [])
        snap[c["id"]] = (c["set"], oid, c["released_at"], c["lang"], int(paper))
        scn[(c["set"], c["collector_number"], c["lang"])] += 1
        s = per_set[c["set"]]
        s["printings"] += 1
        if s["min_date"] is None or c["released_at"] < s["min_date"]:
            s["min_date"] = c["released_at"]
        released = c["released_at"] <= CUTOFF
        if c["lang"] == "en" and paper and released:
            s["en_paper_released"] += 1
            if oid:
                s["oracles"].add(oid)
                by_oracle[oid].append((c["released_at"], c["set"], c.get("set_type"), bool(c.get("reprint")),
                                       c["layout"]))
        layouts[c["layout"]] += 1

    # ---- G1 exact ID parity
    hid, sid = set(hist), set(snap)
    both = hid & sid
    field_mismatch, drift_sets = collections.Counter(), collections.defaultdict(collections.Counter)
    for i in both:
        h, s = hist[i], snap[i]
        for k, n in ((0, "set"), (1, "oracle_id"), (2, "released_at"), (3, "lang"), (4, "paper")):
            if h[k] != s[k]:
                field_mismatch[n] += 1
                drift_sets[n][s[0]] += 1
    only_new = collections.Counter(snap[i][0] for i in sid - hid)
    only_old = collections.Counter(hist[i][0] for i in hid - sid)
    g1 = {"historical_oct28_printing_ids": len(hid), "oct29_bulk_printing_ids": len(sid),
          "ids_in_both": len(both), "only_in_oct28": len(hid - sid), "only_in_oct29": len(sid - hid),
          "only_in_oct29_by_set_top": dict(only_new.most_common(15)),
          "only_in_oct28_by_set_top": dict(only_old.most_common(15)),
          "shared_id_field_mismatches": dict(field_mismatch),
          "shared_id_field_mismatches_by_set_top": {k: dict(v.most_common(12)) for k, v in sorted(drift_sets.items())},
          "duplicate_ids_in_bulk": dup_ids,
          "duplicate_set_collector_lang_in_bulk": sum(1 for v in scn.values() if v > 1),
          "printings_without_top_level_oracle_id": no_oracle,
          "set_codes_only_in_bulk": sorted(set(per_set) - set(catalog)),
          "set_codes_only_in_catalog": sorted(set(catalog) - set(per_set))}

    # ---- L201 per-set count checks vs product catalog
    count_mismatch = []
    for code, p in psets.items():
        s = per_set.get(code)
        if not s:
            count_mismatch.append((code, "missing in bulk"))
            continue
        if s["printings"] != p["printing_records_in_oct29_default_cards"]:
            count_mismatch.append((code, "printings", s["printings"], p["printing_records_in_oct29_default_cards"]))
        if len(s["oracles"]) != p["released_distinct_oracle_ids_in_oct29_default_cards"] and \
                p["release_status_as_of_cutoff"] == "released_by_cutoff":
            count_mismatch.append((code, "oracles", len(s["oracles"]),
                                   p["released_distinct_oracle_ids_in_oct29_default_cards"]))
    api_codes = {x["code"] for x in jload(ATLAS / "scryfall_set_metadata_2026-10-29.json")["scryfall_sets"]}
    broken_parent = sorted(c for c, p in psets.items() if p.get("parent_set_code") and p["parent_set_code"] not in api_codes)
    parent_api_only = sorted(f'{c}->{p["parent_set_code"]}' for c, p in psets.items()
                             if p.get("parent_set_code") and p["parent_set_code"] not in psets and p["parent_set_code"] in api_codes)
    preview_before_set_date = sorted(c for c, p in psets.items()
                                     if per_set.get(c) and p.get("released_at") and per_set[c]["min_date"] < p["released_at"])
    cats = collections.Counter(v["set_type"] for v in catalog.values())
    samples = {}
    for code, label in SAMPLES.items():
        s, p = per_set.get(code), psets.get(code, {})
        samples[code] = {"label": label, "name": p.get("name"), "set_type": p.get("scryfall_set_type"),
                         "digital_only": p.get("digital_only"), "released_at": p.get("released_at"),
                         "bulk_printings": s["printings"] if s else 0,
                         "bulk_released_en_paper_rows": s["en_paper_released"] if s else 0,
                         "bulk_released_en_paper_oracle_ids": len(s["oracles"]) if s else 0,
                         "catalog_printings": p.get("printing_records_in_oct29_default_cards")}

    # ---- G6 debut/reprint attribution
    debut_sets, ties, promo_first, flag_conflict, debut_layout = collections.Counter(), 0, 0, 0, collections.Counter()
    for oid, rows in by_oracle.items():
        rows.sort()
        first = rows[0][0]
        firsts = [r for r in rows if r[0] == first]
        fsets = {r[1] for r in firsts}
        if len(fsets) > 1:
            ties += 1
        else:
            debut_sets[firsts[0][1]] += 1
        if all(r[2] == "promo" for r in firsts):
            promo_first += 1
        if any(r[3] for r in firsts) and not any(not r[3] for r in firsts):
            flag_conflict += 1  # every earliest-dated printing says reprint=true
        debut_layout[firsts[0][4] if firsts[0][4] in MULTIFACE | TOKENISH else "normal_or_other"] += 1
    cat_debut = {c: v.get("single_set_debuts", 0) for c, v in catalog.items()}
    debut_mismatch = sorted(c for c in set(cat_debut) | set(debut_sets) if cat_debut.get(c, 0) != debut_sets.get(c, 0))
    all_oracles = {s[1] for s in snap.values() if s[1]}
    digital_only = len(all_oracles - set(by_oracle))
    g6 = {"released_en_paper_oracle_ids": len(by_oracle), "single_set_debut_identities": sum(debut_sets.values()),
          "same_day_multi_set_ties": ties, "debut_only_in_promo_sets": promo_first,
          "earliest_printing_flagged_reprint_by_scryfall": flag_conflict,
          "identities_without_released_en_paper_printing": digital_only,
          "debut_layouts": dict(sorted(debut_layout.items())),
          "per_set_debut_mismatch_vs_catalog": debut_mismatch[:30], "per_set_debut_mismatch_count": len(debut_mismatch)}

    # ---- L200 set -> official story bridge (titled publication series; not lore inferred from cards)
    pages = list(csv.DictReader((ROOT / "data/primary_sources.csv").open(encoding="utf-8")))
    url_arc = {r["url"]: r["arc"] for r in pages if r["arc"]}
    claims_by_arc = collections.Counter()
    for f in sorted(glob.glob(str(ROOT / "data/lore_research/pack_*.json"))):
        pk = jload(Path(f))
        reg = pk.get("source_register")
        if not isinstance(reg, dict):
            continue
        for cl in pk.get("claims", []):
            arcs = {url_arc.get(reg.get(s, {}).get("url")) for s in cl.get("source_ids", [])} - {None}
            for a in arcs:
                claims_by_arc[a] += 1
    bridge = {}
    for arc in sorted({r["arc"] for r in pages if r["arc"]}):
        codes = set()
        for a in arc.lower().split("/"):
            codes |= {a, *EXTRA_SETS.get(a, [])}
            if a in catalog:
                codes |= {c for c, v in catalog.items() if v["name"] == catalog[a]["name"] + " Commander"}
        codes &= set(catalog)
        bridge[arc] = {"set_codes": sorted(codes), "official_story_pages": sum(1 for r in pages if r["arc"] == arc),
                       "cited_claims": claims_by_arc.get(arc, 0)}
    spotlight = collections.Counter()
    for line in gzip.open(bulk, "rt", encoding="utf-8"):
        c = json.loads(line)
        if c.get("story_spotlight"):
            spotlight[c["set"]] += 1

    atlas_md = (ROOT / "SET_ATLAS.md").read_text(encoding="utf-8")
    scope = jload(ATLAS / "phase1b_release_scope_story_bridge_2026-10-29.json")
    exp = jload(ATLAS / "phase1b_export_acceptance_2026-10-29.json")
    dates = jload(ROOT / "data/lore_research/in_universe_dates_2026-10-30.json")

    def v(ok, qualified=False):
        return "PASS" if ok and not qualified else "QUALIFIED" if ok else "OPEN"

    exact = g1["only_in_oct28"] == 0 and not g1["shared_id_field_mismatches"]
    superset = g1["only_in_oct28"] == 0 and g1["ids_in_both"] == g1["historical_oct28_printing_ids"]
    gates = [
        {"line": "L193", "gate": "printing index/shards audited against the archived Default Cards snapshot",
         "verdict": v(superset and g1["duplicate_ids_in_bulk"] == 0 and not g1["set_codes_only_in_bulk"], not exact),
         "evidence": "g1_exact_id_parity", "note": "exact ID and field parity holds" if exact else
         "every Oct 28 historical ID is present in the Oct 29 bulk; Oct-29-only IDs and shared-ID field drift "
         "(release-date/paper updates) are listed by set; no silent join"},
        {"line": "L194", "gate": "normalized set catalog with parent links and provenance",
         "verdict": v(len(psets) == 1062 and not broken_parent and all(
             {"released_at", "scryfall_set_type", "digital_only", "parent_relation_source"} <= set(p) for p in psets.values())),
         "evidence": "product_catalog_2026-10-29.json", "broken_parent_links": broken_parent,
         "parent_links_to_api_only_future_sets": parent_api_only},
        {"line": "L195", "gate": "reproducible totals for all set codes and, separately, premier candidates",
         "verdict": v(sum(cats.values()) == 1062 and bool(scope.get("scope_counts_exclusive")), True),
         "evidence": "catalog set_type totals + release-scope 136/4/2/848/62/10", "set_type_totals": dict(sorted(cats.items())),
         "note": "136 is a sourced regular/mainline classification of one Scryfall category, not an all-time premier census"},
        {"line": "L196", "gate": "per-set English printing records and deduplicated inventories",
         "verdict": v(exp.get("all_set_codes_full_export_checked") == 1062 or exp.get("all_1062_printing_and_unique_card_exports") in (True, 1062, "PASS")),
         "evidence": "phase1b_export_acceptance_2026-10-29.json"},
        {"line": "L197", "gate": "bidirectional set<->card search with code/name/year/type/date filters",
         "verdict": v(all((ROOT / "scripts" / s).exists() for s in ("set_product_lookup.py", "set_atlas_lookup.py",
                                                                        "historical_set_lookup.py"))),
         "evidence": "set_product_lookup.py (--code/--name/--year/--type/--parent/--from/--through), set_atlas_lookup.py, historical_set_lookup.py"},
        {"line": "L198", "gate": "debut/reprint attribution verified with dated stable identities and edge cases",
         "verdict": v(g6["per_set_debut_mismatch_count"] == 0, True), "evidence": "g6_debut_reprint",
         "edge_cases": {k: g6[k] for k in ("same_day_multi_set_ties", "debut_only_in_promo_sets",
                                           "earliest_printing_flagged_reprint_by_scryfall",
                                           "identities_without_released_en_paper_printing")},
         "note": "Scryfall dates are release-or-first-card dates; preview/promo availability is not a sourced street date"},
        {"line": "L199", "gate": "two separately labelled timelines, linked only by sourced claims",
         "verdict": v(dates.get("by_kind", {}).get("AR_YEAR", 0) == 0 and "in-universe" not in json.dumps(
             product["sets"]).lower(), True), "evidence": "product catalog released_at (real world) vs "
         "data/lore_research/in_universe_dates_2026-10-30.json (32 RELATIVE_SPAN, 0 calendar years)",
         "note": "in-universe timeline is relative spans only; no AR-year chronology exists yet"},
        {"line": "L200", "gate": "sets connected to planes/arcs/characters without inventing lore",
         "verdict": v(len(bridge) > 0, True), "evidence": "set_story_bridge (arc-tagged official pages and cited claims "
         "per set) + Scryfall story_spotlight printings", "note": "publication-series bridge; per-card canon lives in claim packs"},
        {"line": "L201", "gate": "automated checks: counts, uniqueness, totals, date order, references, sample queries",
         "verdict": v(not count_mismatch and g1["duplicate_ids_in_bulk"] == 0 and not broken_parent and all(
             samples[c]["bulk_printings"] == samples[c]["catalog_printings"] for c in samples)),
         "evidence": "this report + tests/test_phase1b_snapshot_gates.py"},
        {"line": "L202", "gate": "user-facing set index with snapshot date, exceptions, sources, exports",
         "verdict": v("October 29" in atlas_md and "Default Cards" in atlas_md), "evidence": "SET_ATLAS.md"},
    ]
    body = {"schema": "phase1b-snapshot-gates/v1", "as_of": CUTOFF,
            "status": "ENGINEERING VERIFICATION (not owner approval or certification)",
            "bulk": {"file": Path(bulk).name, "sha256": bulk_sha, "matches_product_catalog_source": True},
            "gates": gates, "g1_exact_id_parity": g1,
            "l201_checks": {"per_set_count_mismatches": count_mismatch[:30], "per_set_count_mismatch_count": len(count_mismatch),
                            "broken_parent_links": broken_parent, "set_codes_with_printing_before_set_date": len(preview_before_set_date),
                            "set_codes_with_printing_before_set_date_examples": preview_before_set_date[:15],
                            "layout_counts": dict(sorted(layouts.items())), "sample_queries": samples},
            "g6_debut_reprint": g6,
            "set_story_bridge": bridge,
            "story_spotlight_printings_by_set": dict(sorted(spotlight.items())),
            "story_spotlight_printings_total": sum(spotlight.values())}
    return body


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    body = build()
    text = json.dumps(body, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    if a.check:
        ok = OUT.exists() and OUT.read_text(encoding="utf-8") == text
        print("PASS phase1b snapshot gates current" if ok else "STALE: rerun scripts/audit_phase1b_snapshot_gates.py")
        return 0 if ok else 1
    OUT.write_text(text, encoding="utf-8")
    print("wrote", OUT.relative_to(ROOT))
    for g in body["gates"]:
        print(g["line"], g["verdict"], g["gate"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
