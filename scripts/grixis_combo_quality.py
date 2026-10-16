#!/usr/bin/env python3
"""Step B: descriptive Combo Quality Model (ChatGPT cycle 67.1).

This layer does *not* turn combo quality into one synthetic power score and does not decide deck changes.  Commander
Spellbook supplies factual combo membership/output; the accepted M2 Blueprint and M4 graph add deck-specific strategic
context.  Unknown execution zones, exact mana, colored pips and interaction timing are recorded as unknown/deferred
rather than guessed.  Step C owns colored/source-aware mana; M6 judgment owns final primary/secondary/backup labels.

Usage:
  python3 scripts/grixis_combo_quality.py --build
  python3 scripts/grixis_combo_quality.py --check
  python3 scripts/grixis_combo_quality.py --summary
  python3 scripts/grixis_combo_quality.py --show abaddon-the-despoiler 1368-3518-4856
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "grixis" / "combo_quality"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "combo_quality.schema.json"
COMBOS = ROOT / "data" / "grixis_combos.json"
REGISTRY = ROOT / "data" / "grixis" / "registry.json"
SUMMARY = ROOT / "data" / "grixis_summary.json"
BP = ROOT / "data" / "grixis" / "blueprints"
GRAPH = ROOT / "data" / "grixis" / "graph"
VERSION = "1"


def load(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def dump(p: Path, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def axis(value, cls, confidence, evidence, note=None):
    out = {"value": value, "evidence_class": cls, "confidence": confidence, "evidence": sorted(set(evidence))}
    if note:
        out["note"] = note
    return out


def bp_commanders(bp):
    return [x["name"] for x in ((bp.get("commanders") or {}).get("value") or []) if x.get("name")]


def graph_cards(graph):
    return {n["name"]: n for n in graph.get("nodes", []) if n.get("kind") == "card" and n.get("name")}


def win_matches(bp, combo):
    cid = combo["id"]
    cc = set(combo["cards"])
    explicit, overlap = [], []
    for w in bp.get("win_conditions", []):
        if w.get("kind") != "combo":
            continue
        ev = set(w.get("evidence") or [])
        if f"spellbook:{cid}" in ev:
            explicit.append(w)
            continue
        wc = set(w.get("cards") or []) | set(w.get("enablers") or [])
        if cc and cc <= wc:
            overlap.append(w)
    return explicit or overlap


def noncombo_packages(node, bp):
    by_id = {p.get("id"): p for p in bp.get("packages", [])}
    out = []
    for pid in node.get("packages") or []:
        p = by_id.get(pid, {})
        blob = (str(pid) + " " + str(p.get("role") or "")).lower()
        if "combo" not in blob and "infinite" not in blob:
            out.append(pid)
    return sorted(out)


def piece_fact(name, nodes, bp):
    n = nodes.get(name)
    if not n:
        return {"name": name, "graph_present": False, "mv": None, "type_line": None, "roles": [], "packages": [],
                "identity_core": False, "tutor_target": False, "recursion": False, "independent_signal_count": 0}
    roles = sorted(n.get("roles") or [])
    packages = sorted(n.get("packages") or [])
    independent = len(roles) + len(noncombo_packages(n, bp)) + int(bool(n.get("identity_core"))) + int(bool(n.get("tutor_target"))) + int(bool(n.get("recursion")))
    return {"name": name, "graph_present": True, "mv": n.get("mv"), "type_line": n.get("type_line"),
            "roles": roles, "packages": packages, "identity_core": bool(n.get("identity_core")),
            "tutor_target": bool(n.get("tutor_target")), "recursion": bool(n.get("recursion")),
            "independent_signal_count": independent}


def type_buckets(pieces):
    out = {"instant": [], "sorcery": [], "permanent": [], "land": [], "unknown": []}
    for p in pieces:
        t = p.get("type_line") or ""
        n = p["name"]
        if not t:
            out["unknown"].append(n)
        elif "Land" in t:
            out["land"].append(n)
        elif "Instant" in t:
            out["instant"].append(n)
        elif "Sorcery" in t:
            out["sorcery"].append(n)
        else:
            out["permanent"].append(n)
    return {k: sorted(v) for k, v in out.items()}


def near_variants(combo, all_combos):
    a = set(combo["cards"])
    out = []
    for b in all_combos:
        if b["id"] == combo["id"]:
            continue
        bb = set(b["cards"])
        needed = max(1, min(len(a), len(bb)) - 1)
        if len(a & bb) >= needed:
            out.append(b["id"])
    return sorted(out)


def analyze_combo(slug, combo, all_combos, bp, graph):
    cid = combo["id"]
    cards = list(combo["cards"])
    nodes = graph_cards(graph)
    pieces = [piece_fact(n, nodes, bp) for n in cards]
    commanders = set(bp_commanders(bp))
    direct_commanders = sorted(commanders & set(cards))
    wins = win_matches(bp, combo)
    win_refs = [f"blueprint:data/grixis/blueprints/{slug}.json#win_conditions/{w.get('id')}" for w in wins]
    source_ref = f"spellbook:{cid}"
    graph_refs = [f"graph:data/grixis/graph/{slug}.json#card:{n}" for n in cards]

    external_enablers = sorted({x for w in wins for x in (w.get("enablers") or []) if x not in cards})
    commander_support = sorted({c for c in commanders for w in wins if c in set(w.get("cards") or []) | set(w.get("enablers") or [])} - set(direct_commanders))
    if direct_commanders:
        commander_mode = "direct_piece"
        structural = "commander_native_combo"
    elif commander_support:
        commander_mode = "blueprint_supports_line"
        structural = "commander_supported_combo"
    elif wins:
        commander_mode = "blueprint_line_has_no_commander_piece_or_enabler"
        structural = "commander_independent_power_package"
    else:
        commander_mode = "unlinked_to_blueprint_combo_win"
        structural = "unlinked_spellbook_combo"

    tutor = {t.get("target"): sorted(t.get("via") or []) for t in bp.get("tutor_targets", []) if t.get("target")}
    targeted = sorted(n for n in cards if n in tutor)
    recursion_value = set(((bp.get("recursion") or {}).get("value") or []))
    recurred = sorted(set(cards) & recursion_value)
    occ = Counter(n for c in all_combos for n in c.get("cards", []))
    variants = near_variants(combo, all_combos)
    types = type_buckets(pieces)
    exposed = sorted(set(types["instant"] + types["sorcery"] + types["permanent"]))
    mv_known = [p["mv"] for p in pieces if isinstance(p.get("mv"), (int, float))]
    low_signal = sorted(p["name"] for p in pieces if p["independent_signal_count"] == 0 and p["name"] not in commanders)
    independently_useful = {p["name"]: {"signal_count": p["independent_signal_count"], "roles": p["roles"],
                                         "noncombo_packages": noncombo_packages(nodes.get(p["name"], {}), bp),
                                         "identity_core": p["identity_core"], "tutor_target": p["tutor_target"],
                                         "recursion": p["recursion"]} for p in pieces}

    if wins and external_enablers:
        outcome = "blueprint_win_requires_external_payoff"
    elif wins:
        outcome = "blueprint_designated_win_line"
    elif combo.get("infinite"):
        outcome = "incidental_infinite_or_value_loop_requires_judgment"
    else:
        outcome = "noninfinite_combo_requires_judgment"

    class_refs = win_refs or [source_ref]
    axes = {
        "card_count": axis(len(cards), "fact", "verified", [source_ref], "Spellbook piece count; external payoff cards are reported separately."),
        "mana": axis({"mv_sum_proxy": sum(mv_known) if len(mv_known) == len(cards) else None,
                      "known_piece_mv_count": len(mv_known), "piece_count": len(cards),
                      "exact_startup_mana": "unresolved", "colored_mana": "deferred_to_step_C"},
                     "derived_metric", "moderate", graph_refs,
                     "Mana value sum is only a curve/setup proxy; alternate costs, rituals, activated costs and colors can make actual startup mana differ."),
        "zones": axis({"execution_zones": "unresolved_in_spellbook_snapshot", "card_type_buckets": types},
                      "fact", "low", [source_ref] + graph_refs,
                      "The cached Spellbook record lists pieces/requirements but not a normalized execution-zone requirement for every line."),
        "commander_requirement": axis({"direct_commander_pieces": direct_commanders, "blueprint_commander_support": commander_support,
                                       "mode": commander_mode},
                                      "derived_metric", "high" if wins or direct_commanders else "moderate",
                                      [source_ref] + win_refs + [f"blueprint:data/grixis/blueprints/{slug}.json#commander_role"]),
        "setup": axis({"spellbook_requires": combo.get("requires") or [], "blueprint_external_enablers": external_enablers},
                      "fact", "high" if wins else "moderate", [source_ref] + win_refs,
                      "This records declared requirements/enablers; it does not infer hidden sequencing costs."),
        "timing": axis({"piece_types": types, "exact_sequence_timing": "unresolved_without_step_or_oracle_timing_model"},
                       "heuristic", "low", graph_refs,
                       "Card types expose broad timing constraints only; exact combo timing remains unresolved."),
        "interaction_windows": axis({"cast_or_resolution_exposed_pieces": exposed, "count_proxy": len(exposed),
                                     "activated_or_triggered_windows": "unresolved"},
                                    "heuristic", "low", graph_refs,
                                    "This is deliberately not an interaction-resilience score; exact stack windows require line-specific rules analysis."),
        "tutor_accessibility": axis({"blueprint_targeted_pieces": targeted, "targeted_piece_count": len(targeted),
                                     "piece_count": len(cards), "via": {n: tutor[n] for n in targeted}},
                                    "strategic_judgment", "moderate", [f"blueprint:data/grixis/blueprints/{slug}.json#tutor_targets"],
                                    "Blueprint tutor targets are deck-specific strategic judgments, not an exhaustive tutor solver."),
        "redundancy": axis({"near_variant_ids": variants, "near_variant_count": len(variants),
                            "piece_spellbook_occurrences": {n: occ[n] for n in cards}},
                           "derived_metric", "high", [f"spellbook:data/grixis_combos.json#decks/{slug}"],
                           "Near variants share all but roughly one piece; occurrence counts are within this deck's cached Spellbook variants."),
        "dead_card_burden": axis({"low_independent_signal_pieces": low_signal, "count_proxy": len(low_signal)},
                                 "heuristic", "low", graph_refs,
                                 "Low-signal means no non-combo role/package, identity-core, tutor-target or recursion signal in the accepted graph/blueprint. It is not a claim that the card is literally dead."),
        "resilience": axis({"near_variant_count_proxy": len(variants),
                            "single_variant_pieces": sorted(n for n in cards if occ[n] == 1),
                            "protection_and_recovery_not_inferred": True},
                           "heuristic", "low", [source_ref] + graph_refs,
                           "Variant redundancy is only one resilience dimension; protection, graveyard hate and recovery are separate."),
        "recovery": axis({"blueprint_recursion_pieces": recurred, "count": len(recurred), "full_line_recovery": "unresolved"},
                         "strategic_judgment", "moderate", [f"blueprint:data/grixis/blueprints/{slug}.json#recursion"],
                         "Blueprint recursion coverage does not prove the whole combo can recover after disruption."),
        "immediate_win": axis({"status": "requires_external_payoff" if external_enablers else "unverified",
                               "blueprint_designated_win": bool(wins)},
                              "heuristic", "test_required", [source_ref] + win_refs,
                              "`infinite` is never treated as synonymous with immediate win. A judgment/rules review must resolve the endpoint."),
        "required_payoff": axis({"blueprint_external_payoffs_or_enablers": external_enablers,
                                 "status": "known_external_enabler" if external_enablers else "none_declared_but_not_proven_unnecessary"},
                                "strategic_judgment" if wins else "heuristic", "moderate" if wins else "low", [source_ref] + win_refs),
        "independent_usefulness": axis(independently_useful, "heuristic", "moderate", graph_refs,
                                      "Signals are structural evidence only; they do not substitute for card-by-card judgment."),
        "commander_contribution": axis({"mode": commander_mode, "direct_pieces": direct_commanders,
                                        "blueprint_support": commander_support, "commander_names": sorted(commanders)},
                                       "strategic_judgment" if wins else "derived_metric", "moderate", [source_ref] + win_refs + [f"blueprint:data/grixis/blueprints/{slug}.json#commander_role"]),
    }
    classification = {"structural_hint": structural, "outcome_hint": outcome,
                      "priority": "unresolved_requires_judgment", "status": "provisional_hint_not_decision",
                      "evidence_class": "heuristic", "confidence": "moderate" if wins else "low",
                      "evidence": sorted(set(class_refs))}
    return {
        "id": cid,
        "cards": cards,
        "spellbook": {"infinite": bool(combo.get("infinite")), "produces": combo.get("produces") or [],
                      "requires": combo.get("requires") or [], "csb_bracket_tag": combo.get("csb_bracket_tag"),
                      "evidence_class": "fact", "confidence": "verified", "evidence": [source_ref]},
        "piece_facts": pieces,
        "axes": axes,
        "classification": classification,
    }


def combo_entry_for(slug, deck_id, combos, summary):
    if deck_id in combos.get("decks", {}):
        return combos["decks"][deck_id]
    source_id = next((k for k, v in summary.items() if v.get("slug") == slug), None)
    if source_id and source_id in combos.get("decks", {}):
        return combos["decks"][source_id]
    return {"combos": []}


def build_one(deck_id, entry, combos, summary):
    slug = entry["slug"]
    bp_path, graph_path = BP / f"{slug}.json", GRAPH / f"{slug}.json"
    bp, graph = load(bp_path), load(graph_path)
    ce = combo_entry_for(slug, deck_id, combos, summary)
    all_combos = ce.get("combos") or []
    recs = [analyze_combo(slug, c, all_combos, bp, graph) for c in all_combos]
    s = {
        "combo_count": len(recs),
        "infinite_count": sum(1 for r in recs if r["spellbook"]["infinite"]),
        "commander_piece_count": sum(1 for r in recs if r["axes"]["commander_requirement"]["value"]["direct_commander_pieces"]),
        "blueprint_win_linked_count": sum(1 for r in recs if r["classification"]["outcome_hint"].startswith("blueprint_")),
        "commander_independent_win_hint_count": sum(1 for r in recs if r["classification"]["structural_hint"] == "commander_independent_power_package"),
        "unresolved_classification_count": len(recs),
    }
    return {
        "schema_version": 1, "deck_id": deck_id, "slug": slug,
        "canonical_hash": entry["canonical_project_list"]["hash"],
        "generated_by": f"scripts/grixis_combo_quality.py v{VERSION}", "status": "provisional_evidence",
        "authority": {"exploratory": True, "can_decide": False,
                      "note": "Step B evidence only. Structural/outcome labels are provisional hints; M6 judgment decides priority and deck changes."},
        "inputs": {"spellbook": "data/grixis_combos.json", "blueprint": f"data/grixis/blueprints/{slug}.json",
                   "graph": f"data/grixis/graph/{slug}.json", "registry": "data/grixis/registry.json"},
        "combos": recs, "summary": s,
    }


def build():
    reg, combos, summary = load(REGISTRY), load(COMBOS), load(SUMMARY)
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for did, e in sorted(reg["decks"].items(), key=lambda kv: kv[1]["slug"]):
        d = build_one(did, e, combos, summary)
        dump(OUT / f"{e['slug']}.json", d)
        rows.append({"deck_id": did, "slug": e["slug"], **d["summary"]})
    dump(OUT / "summary.json", {"schema_version": 1, "generated_by": f"scripts/grixis_combo_quality.py v{VERSION}",
                                "decks": rows,
                                "totals": {k: sum(r[k] for r in rows) for k in ("combo_count", "infinite_count", "commander_piece_count", "blueprint_win_linked_count", "commander_independent_win_hint_count", "unresolved_classification_count")}})
    print(f"combo-quality: built {len(rows)} decks, {sum(r['combo_count'] for r in rows)} Spellbook lines")


def check():
    try:
        import jsonschema
    except ImportError:
        print("combo-quality: jsonschema is required for --check")
        return 1
    schema = load(SCHEMA)
    resolver = jsonschema.RefResolver(base_uri=SCHEMA.resolve().as_uri(), referrer=schema)
    validator = jsonschema.Draft202012Validator(schema, resolver=resolver)
    reg, combos, summary = load(REGISTRY), load(COMBOS), load(SUMMARY)
    problems = []
    expected = {e["slug"] for e in reg["decks"].values()}
    present = {p.stem for p in OUT.glob("*.json") if p.name != "summary.json"}
    if present != expected:
        problems.append(f"deck file coverage mismatch: missing={sorted(expected-present)} extra={sorted(present-expected)}")
    for did, e in sorted(reg["decks"].items()):
        p = OUT / f"{e['slug']}.json"
        if not p.is_file():
            continue
        d = load(p)
        for err in validator.iter_errors(d):
            problems.append(f"{e['slug']}: schema {list(err.path)}: {err.message}")
        if d.get("canonical_hash") != e["canonical_project_list"]["hash"]:
            problems.append(f"{e['slug']}: canonical hash drift")
        source_ids = {c["id"] for c in (combo_entry_for(e["slug"], did, combos, summary).get("combos") or [])}
        built_ids = {c["id"] for c in d.get("combos", [])}
        if source_ids != built_ids:
            problems.append(f"{e['slug']}: Spellbook combo id drift")
        if any(c["classification"].get("priority") != "unresolved_requires_judgment" for c in d.get("combos", [])):
            problems.append(f"{e['slug']}: scripted combo classification attempted to resolve priority")
    print(f"combo-quality: {len(expected)} deck files, {len(problems)} problems")
    for p in problems[:40]:
        print("FAIL", p)
    return 1 if problems else 0


def summary_cmd():
    p = OUT / "summary.json"
    if not p.is_file():
        print("summary missing; run --build")
        return 1
    d = load(p)
    print(json.dumps(d["totals"], indent=2, sort_keys=True))
    return 0


def show(slug, combo_id):
    p = OUT / f"{slug}.json"
    if not p.is_file():
        print(f"unknown slug {slug}")
        return 1
    d = load(p)
    r = next((x for x in d["combos"] if x["id"] == combo_id), None)
    if not r:
        print(f"combo {combo_id} not found in {slug}")
        return 1
    print(json.dumps(r, indent=2, ensure_ascii=False, sort_keys=True))
    return 0


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--build", action="store_true")
    a.add_argument("--check", action="store_true")
    a.add_argument("--summary", action="store_true")
    a.add_argument("--show", nargs=2, metavar=("SLUG", "COMBO_ID"))
    x = a.parse_args(argv)
    rc = 0
    if x.build: build()
    if x.check: rc |= check()
    if x.summary: rc |= summary_cmd()
    if x.show: rc |= show(*x.show)
    if not (x.build or x.check or x.summary or x.show): a.print_help()
    return rc


if __name__ == "__main__":
    sys.exit(main())
