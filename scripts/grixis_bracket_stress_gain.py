#!/usr/bin/env python3
"""Step F gain proof: generic M3 stress coverage -> bracket-specific routed/adversarial review resolution.

This measures evidence/task resolution, not deck quality. No stress outcome is weighted into a score.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "data/grixis/registry.json"
SUITES = ROOT / "data/grixis/bracket_stress"
ROUTED = ROOT / "data/grixis/bracket_stress_packets"
RED = ROOT / "data/grixis/bracket_red_team"
STRESS = ROOT / "data/grixis/stress"
OUT = ROOT / "data/grixis/bracket_stress_gain.json"
SCHEMA = ROOT / "data/grixis/schemas/bracket_stress_gain.schema.json"


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def dump(p, o):
    Path(p).write_text(json.dumps(o, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def files(d):
    return [p for p in sorted(Path(d).glob("*.json")) if p.name != "summary.json"]


def example(slug):
    s = load(SUITES / f"{slug}.json")
    p = load(ROUTED / f"{slug}.json")
    r = load(RED / f"{slug}.json")
    return {
        "slug": slug,
        "suite_family": s["bracket"]["suite_family"],
        "bracket": s["bracket"]["value"],
        "stress_ids": [x["id"] for x in s["items"]],
        "routed_statuses": {x["id"]: x["evidence"]["status"] for x in p["items"]},
        "judgment_prompts": [x["id"] for x in r["reviews"]],
        "resolution_gain": (
            "Generic M3 scenarios are now placed in a bracket-specific workload together with executed bounded "
            "Step-E canonical-deck evidence and mandatory adversarial prompts; no outcome is aggregated."
        ),
    }


def build_record():
    reg = load(REG)
    suite_files = files(SUITES)
    packet_files = files(ROUTED)
    red_files = files(RED)
    families = {"B5_competitive": 0, "B4_resilience": 0}
    module_executed = judgment = legacy = goldfish = 0
    b5 = None
    b4 = None
    for p in suite_files:
        s = load(p)
        fam = s["bracket"]["suite_family"]
        families[fam] += 1
        if fam == "B5_competitive" and b5 is None:
            b5 = s["slug"]
        if fam == "B4_resilience" and b4 is None:
            b4 = s["slug"]
    for p in packet_files:
        d = load(p)
        for x in d["items"]:
            st = x["evidence"]["status"]
            module_executed += st == "executed_deck_level_module_result"
            judgment += st == "judgment_required"
            legacy += st == "reused_existing_test_result"
            goldfish += st == "reused_goldfish_readiness"
    generic = set()
    if files(STRESS):
        for r in load(files(STRESS)[0])["records"]:
            generic.add(r["scenario"].split("@")[0])
    return {
        "schema_version": 1,
        "status": "demonstrated_decision_resolution_gain",
        "evidence_class": "derived_metric",
        "authority": {
            "can_decide": False,
            "note": "This proof compares stress evidence/review resolution only; it cannot rank decks or decide swaps.",
        },
        "before": {
            "model": "M3 generic stress suite",
            "decks": 62,
            "scenario_families": sorted(generic),
            "scenario_count": len(generic),
            "limitation": (
                "Every deck received the same generic scenario set; opponent-facing stack/stax and bracket-specific "
                "adversarial questions were not assigned as distinct workloads."
            ),
        },
        "after": {
            "model": "Step F bracket-specific stress architecture",
            "decks": len(suite_files),
            "suite_family_counts": families,
            "routed_packets": len(packet_files),
            "red_team_packets": len(red_files),
            "legacy_test_items_reused": legacy,
            "goldfish_readiness_items_reused": goldfish,
            "module_items_executed_deck_level": module_executed,
            "judgment_items_pending_real_review": judgment,
            "aggregate_outcome_scores": 0,
        },
        "real_deck_examples": [example(b5), example(b4)],
        "limitations": [
            "This is a before/after evidence-resolution comparison, not benchmark accuracy or deck power measurement.",
            "Existing M3 outcomes are reused under their original preregistration; Step F does not retroactively change thresholds.",
            "Step-E deck-level module execution is bounded availability/friction evidence from the frozen development snapshot, not multiplayer outcome simulation.",
            "Red-team prompts remain pending judgment and are not counted as passed/failed stresses.",
            "Priority weights are workload allocation only and never outcome weights.",
        ],
        "conclusion": (
            "Step F resolves the prior one-size-fits-all stress layer into distinct B5/B4 workloads, exact evidence "
            "routing, executed bounded mechanic evidence and mandatory adversarial review prompts without producing "
            "a composite stress score."
        ),
    }


def build():
    dump(OUT, build_record())
    print(json.dumps(build_record()["after"], indent=2, sort_keys=True))


def check():
    try:
        import jsonschema
    except ImportError:
        print("bracket-stress-gain: jsonschema required")
        return 1
    probs = []
    if not OUT.exists():
        probs.append("gain record missing")
    else:
        d = load(OUT)
        s = load(SCHEMA)
        probs += [f"schema {list(e.path)}: {e.message}" for e in jsonschema.Draft202012Validator(s).iter_errors(d)]
        if d != build_record():
            probs.append("gain record stale")
        if d["authority"]["can_decide"] is not False:
            probs.append("gain proof became decision-capable")
        if d["after"]["aggregate_outcome_scores"] != 0:
            probs.append("aggregate outcome score introduced")
        if set(d["after"]["suite_family_counts"]) != {"B5_competitive", "B4_resilience"}:
            probs.append("suite family split missing")
        if d["after"]["module_items_executed_deck_level"] <= 0:
            probs.append("no executed deck-level mechanic items recorded")
    print(f"bracket-stress-gain: {len(probs)} problems")
    for x in probs:
        print("FAIL", x)
    return 1 if probs else 0


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--build", action="store_true")
    a.add_argument("--check", action="store_true")
    x = a.parse_args(argv)
    rc = 0
    if x.build:
        build()
    if x.check:
        rc |= check()
    if not (x.build or x.check):
        a.print_help()
    return rc


if __name__ == "__main__":
    sys.exit(main())
