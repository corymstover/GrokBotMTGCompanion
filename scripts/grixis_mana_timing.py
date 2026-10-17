#!/usr/bin/env python3
"""Step C batch 68.2: source reliability, ETB timing, fetch-target validation, and distinct-source color readiness.

The model stays deliberately bounded. It uses the frozen card pages and canonical lists; it does not refresh external data,
sequence spells, assign context-dependent source reliability percentages, or decide land swaps. Probability outputs are exact
no-mulligan *draw/presence* calculations under declared source sets. They are not cast probabilities or win rates.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_mana_base as mb

REGISTRY = ROOT / "data" / "grixis" / "registry.json"
BASE = ROOT / "data" / "grixis" / "mana_base"
OUT = ROOT / "data" / "grixis" / "mana_timing"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "mana_timing.schema.json"
VERSION = 1
ORDER = "UBR"


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def dump(p, obj):
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def norm_mask(colors):
    s = set(colors or "")
    return "".join(c for c in ORDER if c in s)


def _advance(reachable, mask, copies, req):
    """All capped colored-pip fulfillment states reachable by assigning `copies` distinct sources of `mask`."""
    cur = set(reachable)
    for _ in range(copies):
        nxt = set(cur)
        for st in cur:
            for i, c in enumerate(ORDER):
                if c not in mask or st[i] >= req[i]:
                    continue
                x = list(st); x[i] += 1; nxt.add(tuple(x))
        cur = nxt
    return frozenset(cur)


def distinct_source_match_probability(masks, n, requirements):
    """Exact P(drawn cards contain distinct source cards assignable to the colored requirements).

    Each card can satisfy at most one colored pip. Flexible masks (e.g. UBR) therefore cannot pay multiple pips by
    themselves. Non-sources are represented by the empty mask. This is source-presence only: it does not prove the
    source can be deployed/activated on that turn.
    """
    N = len(masks); n = min(max(0, n), N)
    req = tuple(int(requirements.get(c, 0)) for c in ORDER)
    if not any(req): return 1.0
    if sum(req) > n: return 0.0
    cats = sorted(Counter(norm_mask(x) for x in masks).items())
    initial = frozenset({(0, 0, 0)})
    # DP stores combinatorial counts, not floating transition probabilities.
    dp = {(0, initial): 1}
    for mask, count in cats:
        nd = defaultdict(int)
        for (drawn, state), ways in dp.items():
            top = min(count, n - drawn)
            for x in range(top + 1):
                st2 = _advance(state, mask, x, req) if mask else state
                nd[(drawn + x, st2)] += ways * comb(count, x)
        dp = nd
    target = req
    success = sum(ways for (drawn, state), ways in dp.items() if drawn == n and target in state)
    return success / comb(N, n)


def direct_mask(card, deck_ci):
    """Colors the object itself can directly produce, excluding fetch-search virtual access."""
    colors, _, _ = mb._add_clause_colors(card["oracle"], deck_ci)
    colors |= {mb.BASIC_TYPE_COLOR[t] for t in mb.BASIC_TYPE_COLOR if t in card["type_line"]}
    colors = {c for c in colors if c in deck_ci}
    return norm_mask(colors)


def fetch_targets(source_name, source, lands):
    """Validate a fetch against actual targetable lands in the current 99.

    Returns targets using basic land types from the frozen type line. `basic_fetch` requires the Basic supertype. This is
    deck-start target availability only; depletion after earlier fetches is intentionally not simulated here.
    """
    if not (source.get("fetch_types") or source.get("basic_fetch")):
        return []
    out = []
    wanted = set(source.get("fetch_types") or [])
    for name, target in lands:
        if name == source_name:
            continue
        if source.get("basic_fetch"):
            legal = "Basic Land" in target["type_line"]
        else:
            legal = bool(wanted & set(target.get("basic_types") or []))
        if not legal:
            continue
        dm = target.get("direct_mask", "")
        out.append({
            "card": name,
            "basic_types": target.get("basic_types") or [],
            "direct_colors": dm,
            "entry_timing": entry_timing(target),
        })
    return sorted(out, key=lambda x: x["card"])


def entry_timing(card):
    if card.get("tapped_unconditional"):
        return "always_tapped"
    if card.get("tapped_conditional"):
        return "conditional_untapped"
    return "untapped_by_default"


def color_union(rows, predicate=lambda r: True):
    s = set()
    for r in rows:
        if predicate(r): s |= set(r.get("direct_colors", ""))
    return norm_mask(s)


def source_record(name, card, actual_fetch_targets):
    fetch = bool(card.get("fetch_types") or card.get("basic_fetch"))
    if fetch:
        potential = color_union(actual_fetch_targets)
        untapped_capable = color_union(actual_fetch_targets, lambda x: x["entry_timing"] != "always_tapped")
        guaranteed_untapped = color_union(actual_fetch_targets, lambda x: x["entry_timing"] == "untapped_by_default")
        # A fetch's color choice is functional if a target exists; target ETB timing is kept separate.
        unconditional = potential if actual_fetch_targets else ""
    else:
        potential = card.get("direct_mask", "")
        unconditional = "" if card.get("conditional_source") else potential
        untapped_capable = "" if card.get("tapped_unconditional") else potential
        guaranteed_untapped = potential if entry_timing(card) == "untapped_by_default" else ""
    return {
        "card": name,
        "kind": "fetch" if fetch else ("mdfc_land_face" if card.get("flex_land") else "direct_land"),
        "potential_colors": potential,
        "unconditional_colors": unconditional,
        "untapped_capable_colors": untapped_capable,
        "guaranteed_untapped_colors": guaranteed_untapped,
        "entry_timing": entry_timing(card),
        "conditional_mana_ability": bool(card.get("conditional_source")),
        "fetch_target_count": len(actual_fetch_targets),
    }


def deck_cards(entry, db):
    ents = mb.parse_export(ROOT / entry["canonical_project_list"]["export"])
    raw_cmd = [db.get(n) for z, q, n in ents if z == "commander"]
    deck_ci = set().union(*(set(c["color_identity"]) & set(mb.COLORS) for c in raw_cmd))
    rows = []
    for z, q, n in ents:
        if z != "main": continue
        c = mb.classify(db.get(n), deck_ci)
        c["direct_mask"] = direct_mask(c, deck_ci)
        for _ in range(q): rows.append((n, c))
    return deck_ci, rows


def full_masks(N, rows, field):
    """One mask per library card; source rows already include strict lands or MDFCs selected by the caller."""
    masks = [r.get(field, "") for r in rows]
    if len(masks) > N: raise ValueError("source-mask rows exceed library size")
    return masks + [""] * (N - len(masks))


def build_one(did, entry, db):
    baseline = load(BASE / f"{entry['slug']}.json")
    deck_ci, library = deck_cards(entry, db)
    N = baseline["counts"]["library_cards"]
    lands = [(n, c) for n, c in library if c["land"]]
    mdfcs = [(n, c) for n, c in library if c["flex_land"]]

    fetch_map = {}
    source_rows = []
    for name, card in lands:
        targets = fetch_targets(name, card, lands)
        if card.get("fetch_types") or card.get("basic_fetch"):
            fetch_map[name] = targets
        source_rows.append(source_record(name, card, targets))
    flex_rows = [source_record(name, card, []) for name, card in mdfcs]

    strict_potential = full_masks(N, source_rows, "potential_colors")
    strict_unconditional = full_masks(N, source_rows, "unconditional_colors")
    strict_untapped = full_masks(N, source_rows, "untapped_capable_colors")
    flex_potential = full_masks(N, source_rows + flex_rows, "potential_colors")

    turn = {}
    for t in (2, 3, 4, 5):
        seen = min(N, 7 + t)
        turn[str(t)] = {
            "cards_seen_no_mulligan": seen,
            "potential_distinct_source_match_UBR": round(distinct_source_match_probability(strict_potential, seen, {"U":1,"B":1,"R":1}), 6),
            "unconditional_distinct_source_match_UBR": round(distinct_source_match_probability(strict_unconditional, seen, {"U":1,"B":1,"R":1}), 6),
            "untapped_capable_distinct_source_match_UBR": round(distinct_source_match_probability(strict_untapped, seen, {"U":1,"B":1,"R":1}), 6),
            "flex_land_potential_distinct_source_match_UBR": round(distinct_source_match_probability(flex_potential, seen, {"U":1,"B":1,"R":1}), 6),
            "strict_land_drop_probability": baseline["turn_access_proxies"][str(t)]["strict_land_drop_probability"],
            "flex_land_drop_probability": baseline["turn_access_proxies"][str(t)]["flex_land_drop_probability"],
        }

    commander = []
    for cmd in baseline["commander_casting"]:
        req = cmd["colored_requirements"]
        seen = min(N, 7 + cmd["base_resource_target"])
        commander.append({
            "name": cmd["name"],
            "colored_requirements": req,
            "cards_seen_by_base_resource_turn": seen,
            "potential_distinct_source_match": round(distinct_source_match_probability(strict_potential, seen, req), 6),
            "unconditional_distinct_source_match": round(distinct_source_match_probability(strict_unconditional, seen, req), 6),
            "untapped_capable_distinct_source_match": round(distinct_source_match_probability(strict_untapped, seen, req), 6),
            "note": "Colored-source assignment only; generic mana, sequencing, rocks, rituals and commander tax are handled separately/later.",
        })

    fetch_records = []
    for name, card in lands:
        if name not in fetch_map: continue
        targets = fetch_map[name]
        by_color = {c: [x["card"] for x in targets if c in x["direct_colors"]] for c in ORDER}
        untapped_by_color = {c: [x["card"] for x in targets if c in x["direct_colors"] and x["entry_timing"] != "always_tapped"] for c in ORDER}
        fetch_records.append({
            "card": name,
            "search_types": card.get("fetch_types") or [],
            "basic_only": bool(card.get("basic_fetch")),
            "target_count": len(targets),
            "actual_target_colors": color_union(targets),
            "untapped_capable_target_colors": color_union(targets, lambda x: x["entry_timing"] != "always_tapped"),
            "targets_by_color": by_color,
            "untapped_capable_targets_by_color": untapped_by_color,
            "targets": targets,
        })

    categories = Counter()
    for r in source_rows:
        if r["kind"] == "fetch" and r["fetch_target_count"] == 0: categories["stranded_fetch"] += 1
        if r["conditional_mana_ability"]: categories["conditional_mana_ability"] += 1
        categories[r["entry_timing"]] += 1
        if not r["potential_colors"]: categories["no_usable_grixis_color"] += 1

    return {
        "schema_version": 1,
        "deck_id": did,
        "slug": entry["slug"],
        "canonical_hash": entry["canonical_project_list"]["hash"],
        "status": "provisional_evidence",
        "evidence_class": "derived_metric",
        "confidence": "moderate",
        "authority": {"can_decide": False, "note": "Timing/reliability diagnostics cannot decide mana-base swaps."},
        "inputs": {"mana_baseline": f"data/grixis/mana_base/{entry['slug']}.json", "canonical_export": entry["canonical_project_list"]["export"], "frozen_card_pages": "data/card_index.csv + cards/**"},
        "source_categories": dict(sorted(categories.items())),
        "strict_land_sources": source_rows,
        "mdfc_optional_sources": flex_rows,
        "fetch_validation": fetch_records,
        "stranded_fetches": [x["card"] for x in fetch_records if x["target_count"] == 0],
        "turn_readiness": turn,
        "commander_colored_readiness": commander,
        "limitations": [
            "No source receives an invented real-game reliability percentage; context-dependent and ETB conditions remain categorical.",
            "Distinct-source matching is exact for cards seen but does not prove those cards were deployed, survived, or can activate in sequence.",
            "Fetch validation uses targets present at deck start and does not model target depletion after earlier fetches.",
            "Untapped-capable includes conditional-untapped targets such as shock/check-style lands; guaranteed-untapped is retained separately at the source level.",
            "MDFC land faces are an optional-source layer and do not silently increase the strict land count.",
            "Rocks, rituals, one-shot mana, generic costs, commander tax and spell sequencing are not folded into these colored-land probabilities.",
        ],
    }


def build():
    reg = load(REGISTRY); db = mb.CardDB(); rows = []
    OUT.mkdir(parents=True, exist_ok=True)
    for did, entry in sorted(reg["decks"].items(), key=lambda kv: kv[1]["slug"]):
        d = build_one(did, entry, db); dump(OUT / f"{entry['slug']}.json", d)
        rows.append({"deck_id": did, "slug": entry["slug"], "fetches": len(d["fetch_validation"]), "stranded_fetches": len(d["stranded_fetches"]), "conditional_sources": d["source_categories"].get("conditional_mana_ability", 0)})
    dump(OUT / "summary.json", {"schema_version": 1, "generated_by": f"scripts/grixis_mana_timing.py v{VERSION}", "decks": rows, "totals": {"decks": len(rows), "fetches": sum(x["fetches"] for x in rows), "stranded_fetches": sum(x["stranded_fetches"] for x in rows), "conditional_sources": sum(x["conditional_sources"] for x in rows)}})
    print(f"mana-timing: built {len(rows)} decks; fetches={sum(x['fetches'] for x in rows)} stranded={sum(x['stranded_fetches'] for x in rows)}")


def check():
    try: import jsonschema
    except ImportError: print("mana-timing: jsonschema required"); return 1
    schema = load(SCHEMA); reg = load(REGISTRY); problems = []
    expected = {e["slug"] for e in reg["decks"].values()}; present = {p.stem for p in OUT.glob("*.json") if p.name != "summary.json"}
    if expected != present: problems.append(f"coverage mismatch missing={sorted(expected-present)} extra={sorted(present-expected)}")
    for did, entry in sorted(reg["decks"].items()):
        p = OUT / f"{entry['slug']}.json"
        if not p.exists(): continue
        d = load(p)
        for err in jsonschema.Draft202012Validator(schema).iter_errors(d): problems.append(f"{entry['slug']}: schema {list(err.path)}: {err.message}")
        if d["canonical_hash"] != entry["canonical_project_list"]["hash"]: problems.append(f"{entry['slug']}: canonical hash drift")
        if d["authority"]["can_decide"] is not False: problems.append(f"{entry['slug']}: timing record became decision-capable")
        if d["stranded_fetches"]: problems.append(f"{entry['slug']}: stranded fetches require review: {d['stranded_fetches']}")
        for f in d["fetch_validation"]:
            if f["target_count"] != len(f["targets"]): problems.append(f"{entry['slug']}: {f['card']} target count drift")
        for t, row in d["turn_readiness"].items():
            for k, v in row.items():
                if k.endswith("probability") or "match_UBR" in k:
                    if not 0 <= v <= 1: problems.append(f"{entry['slug']}: {t}.{k} out of bounds")
    print(f"mana-timing: {len(expected)} deck files, {len(problems)} problems")
    for p in problems[:50]: print("FAIL", p)
    return 1 if problems else 0


def main(argv=None):
    a = argparse.ArgumentParser(); a.add_argument("--build", action="store_true"); a.add_argument("--check", action="store_true"); a.add_argument("--summary", action="store_true")
    x = a.parse_args(argv); rc = 0
    if x.build: build()
    if x.check: rc |= check()
    if x.summary: print(json.dumps(load(OUT / "summary.json"), indent=2, sort_keys=True))
    if not (x.build or x.check or x.summary): a.print_help()
    return rc


if __name__ == "__main__": sys.exit(main())
