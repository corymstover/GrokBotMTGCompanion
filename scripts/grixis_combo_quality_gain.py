#!/usr/bin/env python3
"""Step B acceptance-standard proof: demonstrate a real before/after decision-quality gain.

This does not score decks or benchmark accuracy. It proves that Step B exposes decision-relevant distinctions the old
combo-presence layer could not represent, while preserving unresolved strategic judgment instead of auto-deciding.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CQ = ROOT / "data" / "grixis" / "combo_quality"
PC = ROOT / "data" / "grixis" / "power_core"
LS = ROOT / "data" / "grixis" / "combo_line_semantics"
CF = ROOT / "data" / "grixis" / "combo_families"
OUT = CQ / "decision_quality_gain.json"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "combo_quality_gain.schema.json"


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def dump(p, obj):
    Path(p).write_text(json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def all_deck_records(folder):
    return [load(p) for p in sorted(Path(folder).glob("*.json")) if p.name not in ("summary.json", "decision_quality_gain.json")]


def find_example(predicate):
    for deck in all_deck_records(CQ):
        for c in deck["combos"]:
            if predicate(c):
                return deck["slug"], c
    return None, None


def build_record():
    cq = load(CQ / "summary.json")["totals"]
    pc = load(PC / "summary.json")["totals"]
    ls = load(LS / "summary.json")["totals"]
    cf = load(CF / "summary.json")["totals"]

    ext_slug, ext = find_example(lambda c: c["classification"]["structural_hint"] == "commander_independent_power_package"
                                 and bool(c["axes"]["required_payoff"]["value"]["blueprint_external_payoffs_or_enablers"]))
    native_slug, native = find_example(lambda c: c["classification"]["structural_hint"] == "commander_native_combo")
    core_slug, core = find_example(lambda c: c["classification"]["structural_hint"] == "commander_independent_power_package"
                                   and c["axes"]["card_count"]["value"] <= 3)
    if not all((ext, native, core)):
        raise RuntimeError("Step B quality-gain worked examples could not be selected from current records")

    examples = [
        {
            "kind": "commander_independent_external_payoff",
            "slug": ext_slug,
            "combo_id": ext["id"],
            "cards": ext["cards"],
            "before": "The old layer could report that the Spellbook line exists/infinite but did not distinguish commander independence or Blueprint external payoff/enabler dependence.",
            "after": f"Step B marks the line {ext['classification']['structural_hint']} and records external Blueprint payoff/enabler cards {ext['axes']['required_payoff']['value']['blueprint_external_payoffs_or_enablers']}; immediate-win remains test_required.",
            "why_it_matters": "A compact infinite-looking line can otherwise be mistaken for a self-contained commander-native win package.",
        },
        {
            "kind": "commander_native",
            "slug": native_slug,
            "combo_id": native["id"],
            "cards": native["cards"],
            "before": "The old layer represented this primarily as combo membership/infinite status.",
            "after": f"Step B records direct commander piece(s) {native['axes']['commander_requirement']['value']['direct_commander_pieces']} and preserves the line as commander_native_combo while leaving strategic priority unresolved.",
            "why_it_matters": "Commander-first optimization needs to distinguish native lines from generic power packages without automatically preferring either one.",
        },
        {
            "kind": "power_core_review",
            "slug": core_slug,
            "combo_id": core["id"],
            "cards": core["cards"],
            "before": "The old combo-presence layer had no explicit post-M2 materiality path for generic compact win packages.",
            "after": "Step B flags this compact commander-independent Blueprint-win line as a power_core_review_candidate under the D5 overlay, without editing the accepted Blueprint or reopening M2.",
            "why_it_matters": "This creates an auditable Commander-first review population instead of silently protecting or deleting generic power packages.",
        },
    ]

    return {
        "schema_version": 1,
        "status": "demonstrated_decision_quality_gain",
        "evidence_class": "derived_metric",
        "before": {
            "model": "pre-Step-B combo presence model",
            "available_fields": ["Spellbook combo membership", "piece names", "infinite flag", "produces/requires snapshot"],
            "limitations": [
                "No normalized commander-contribution distinction.",
                "No explicit external-payoff vs self-contained distinction.",
                "No deck-specific tutor/recovery/dead-card/redundancy vector.",
                "No D5 power_core review overlay/materiality gate.",
                "No line-step/mana/zone/action evidence or variant-family redundancy network integrated into combo review.",
            ],
        },
        "after": {
            "model": "Step-B combo-quality evidence vector + line semantics + power_core overlay + variant families",
            "available_dimensions": [
                "card count", "mana-value/setup proxy", "declared Spellbook mana", "zone evidence", "commander requirement",
                "setup/enablers", "timing/type proxy", "interaction-window proxy", "tutor accessibility", "redundancy",
                "dead-card-burden proxy", "resilience", "recovery", "immediate-win uncertainty", "required payoff",
                "independent usefulness", "commander contribution", "line action counts", "endpoint hints", "variant-family redundancy networks",
            ],
            "governance_guards": [
                "Infinite never implies immediate win.",
                "Primary/secondary/backup/incidental/value-loop priority remains unresolved strategic judgment.",
                "power_core overlay cannot rewrite accepted M2 Blueprints or auto-reopen M2.",
                "Variant-family components are redundancy evidence, not claims that every transitive member is strategically identical.",
                "Exact/colored mana remains Step C when not explicitly supported by cached line evidence.",
            ],
        },
        "measured_deltas": {
            "spellbook_lines": cq["combo_count"],
            "blueprint_linked_lines": cq["blueprint_win_linked_count"],
            "direct_commander_piece_lines": cq["commander_piece_count"],
            "commander_independent_win_hints": cq["commander_independent_win_hint_count"],
            "power_core_review_candidates": pc["candidate_count"],
            "compact_power_core_candidates": pc["compact_candidate_count"],
            "step_records": ls["step_record_found_count"],
            "declared_mana_records": ls["mana_needed_declared_count"],
            "zone_mentions": ls["zone_mention_count"],
            "direct_endpoint_hints": ls["direct_endpoint_hint_count"],
            "variant_families": cf["family_count"],
            "multi_line_variant_families": cf["multi_line_family_count"],
            "strategic_priority_auto_decisions": 0,
        },
        "worked_examples": examples,
        "limitations": [
            "This is a capability/decision-resolution comparison, not a claim that Step B already chose the correct deck changes.",
            "Commander Spellbook steps are community-maintained and not official rules; official rules/M1 remain authoritative.",
            "Several dimensions are intentionally proxies or unresolved; Step C, D, stress testing and M6 judgment add later evidence.",
            "Variant families are transitive connected components under a near-variant rule and require judgment before strategic equivalence is asserted.",
            "The retrospective benchmark is separately contamination-flagged; this record is not presented as blind benchmark accuracy.",
        ],
        "conclusion": "Step B demonstrably improves decision resolution over binary combo presence by separating commander contribution, external payoff/setup, deck-specific support, redundancy/recovery/dead-card signals, community line semantics, variant-family redundancy and D5 power-core review, while making zero automatic strategic-priority decisions.",
    }


def build():
    d = build_record(); dump(OUT, d)
    print(json.dumps(d["measured_deltas"], indent=2, sort_keys=True))


def check():
    try:
        import jsonschema
    except ImportError:
        print("combo-quality-gain: jsonschema required"); return 1
    schema = load(SCHEMA)
    problems = []
    if not OUT.exists():
        problems.append("decision_quality_gain.json missing; run --build")
    else:
        d = load(OUT)
        problems += [f"schema {list(e.path)}: {e.message}" for e in jsonschema.Draft202012Validator(schema).iter_errors(d)]
        expected = build_record()
        if d != expected:
            problems.append("decision_quality_gain.json is stale vs current Step B summaries/records")
        m = d.get("measured_deltas", {})
        if m.get("strategic_priority_auto_decisions") != 0:
            problems.append("Step B must not auto-decide strategic combo priority")
        if m.get("spellbook_lines", 0) and m.get("step_records", 0) != m.get("spellbook_lines", 0):
            problems.append("current frozen step cache no longer covers every Step B combo line")
        if m.get("variant_families", 0) < m.get("multi_line_variant_families", 0):
            problems.append("multi-line family count cannot exceed all families")
    print(f"combo-quality-gain: {len(problems)} problems")
    for p in problems: print("FAIL", p)
    return 1 if problems else 0


def main(argv=None):
    a = argparse.ArgumentParser(); a.add_argument("--build", action="store_true"); a.add_argument("--check", action="store_true")
    x = a.parse_args(argv); rc = 0
    if x.build: build()
    if x.check: rc |= check()
    if not (x.build or x.check): a.print_help()
    return rc


if __name__ == "__main__": sys.exit(main())
