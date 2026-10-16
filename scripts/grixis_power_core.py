#!/usr/bin/env python3
"""Step B / Cory D5: versioned post-M2 power_core correction overlay.

The accepted M2 Blueprint is immutable here.  This script only flags combo-quality records whose Blueprint-linked win
line is structurally commander-independent, because those packages are the highest-risk population for generic Grixis
power-core homogenization.  The overlay is evidence for later judgment, not a declaration that the package is bad.

Materiality gate: any *future* correction that proposes changing commander_role, dependency_level, power/ceiling,
anti_goals, packages/requirements, win_conditions or construction rules is material and requires targeted M2 review /
reopen for that deck.  A classification-only overlay touches none of those fields and therefore does not reopen M2.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CQ = ROOT / "data" / "grixis" / "combo_quality"
BP = ROOT / "data" / "grixis" / "blueprints"
OUT = ROOT / "data" / "grixis" / "power_core"
REGISTRY = ROOT / "data" / "grixis" / "registry.json"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "power_core_overlay.schema.json"
VERSION = 1
MATERIAL_FIELDS = [
    "commander_role",
    "dependency_level",
    "power",
    "anti_goals",
    "packages",
    "requirements",
    "win_conditions",
    "construction_rules",
]


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def dump(p, obj):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def material_fields_touched(proposed_changes):
    """Return material top-level Blueprint fields touched by hypothetical JSON-pointer-like change paths."""
    touched = set()
    for change in proposed_changes:
        path = str(change.get("path") if isinstance(change, dict) else change).lstrip("/")
        top = path.split("/", 1)[0] if path else ""
        if top in MATERIAL_FIELDS:
            touched.add(top)
    return sorted(touched)


def compactness(n):
    return "compact_2" if n <= 2 else "compact_3" if n == 3 else "extended_4_plus"


def candidate(combo):
    cl = combo["classification"]
    if cl["structural_hint"] != "commander_independent_power_package":
        return None
    cc = combo["axes"]["card_count"]["value"]
    reasons = [
        "Combo Quality Model links this Spellbook line to a Blueprint combo win.",
        "Neither a commander card nor a Blueprint commander enabler is part of the linked line.",
        "Commander-independent win packages require explicit identity scrutiny before M6, rather than automatic protection or removal.",
    ]
    if cc <= 3:
        reasons.append("The line is compact (three or fewer Spellbook pieces), increasing its generic-power-package relevance.")
    payoff = combo["axes"]["required_payoff"]["value"]["blueprint_external_payoffs_or_enablers"]
    if payoff:
        reasons.append("The Blueprint names external payoff/enabler cards; compactness alone therefore does not make the line self-contained.")
    return {
        "combo_id": combo["id"],
        "cards": combo["cards"],
        "classification": "power_core_review_candidate",
        "compactness": compactness(cc),
        "blueprint_win_linked": cl["outcome_hint"].startswith("blueprint_"),
        "commander_independent": True,
        "why_flagged": reasons,
        "evidence_class": "heuristic",
        "confidence": "moderate" if cl["outcome_hint"].startswith("blueprint_") else "low",
        "evidence": sorted(set(cl["evidence"] + combo["axes"]["commander_contribution"]["evidence"])),
        "materiality": {
            "current_overlay_changes_blueprint": False,
            "proposed_blueprint_changes": [],
            "material_fields_touched": [],
            "m2_action": "no_reopen_for_overlay_only; targeted review required before any material application",
        },
    }


def build_one(did, entry):
    slug = entry["slug"]
    cq = load(CQ / f"{slug}.json")
    bp = load(BP / f"{slug}.json")
    candidates = [x for x in (candidate(c) for c in cq["combos"]) if x]
    return {
        "schema_version": 1,
        "deck_id": did,
        "slug": slug,
        "canonical_hash": entry["canonical_project_list"]["hash"],
        "blueprint_version": int(bp.get("version") or 1),
        "status": "provisional_overlay",
        "authority": {"can_rewrite_blueprint": False, "can_reopen_m2": False, "can_decide_deck": False},
        "materiality_policy": {
            "material_fields": MATERIAL_FIELDS,
            "rule": "Classification-only overlays do not reopen M2. Any proposed correction touching a material field requires targeted Cory review/reopen before application; downstream artifacts regenerate either way.",
        },
        "candidates": candidates,
        "summary": {
            "candidate_count": len(candidates),
            "compact_candidate_count": sum(1 for x in candidates if x["compactness"] != "extended_4_plus"),
            "material_blueprint_changes_proposed": 0,
            "m2_reopen_requested": False,
        },
    }


def build():
    reg = load(REGISTRY)
    rows = []
    OUT.mkdir(parents=True, exist_ok=True)
    for did, e in sorted(reg["decks"].items(), key=lambda kv: kv[1]["slug"]):
        d = build_one(did, e)
        dump(OUT / f"{e['slug']}.json", d)
        rows.append({"deck_id": did, "slug": e["slug"], **d["summary"]})
    dump(OUT / "summary.json", {
        "schema_version": 1,
        "generated_by": f"scripts/grixis_power_core.py v{VERSION}",
        "decks": rows,
        "totals": {
            "candidate_count": sum(x["candidate_count"] for x in rows),
            "compact_candidate_count": sum(x["compact_candidate_count"] for x in rows),
            "material_blueprint_changes_proposed": 0,
            "m2_reopen_requested": False,
        },
    })
    print(f"power-core: built {len(rows)} overlays; {sum(x['candidate_count'] for x in rows)} review candidates")


def check():
    try:
        import jsonschema
    except ImportError:
        print("power-core: jsonschema required")
        return 1
    schema = load(SCHEMA)
    common = load(SCHEMA.parent / "common.schema.json")
    store = {schema["$id"]: schema, common["$id"]: common}
    resolver = jsonschema.RefResolver(base_uri=schema["$id"], referrer=schema, store=store)
    validator = jsonschema.Draft202012Validator(schema, resolver=resolver)
    reg = load(REGISTRY)
    problems = []
    expected = {e["slug"] for e in reg["decks"].values()}
    present = {p.stem for p in OUT.glob("*.json") if p.name != "summary.json"}
    if expected != present:
        problems.append(f"overlay coverage mismatch missing={sorted(expected-present)} extra={sorted(present-expected)}")
    for did, e in reg["decks"].items():
        p = OUT / f"{e['slug']}.json"
        if not p.exists():
            continue
        d = load(p)
        for err in validator.iter_errors(d):
            problems.append(f"{e['slug']}: schema {list(err.path)}: {err.message}")
        if d["canonical_hash"] != e["canonical_project_list"]["hash"]:
            problems.append(f"{e['slug']}: canonical hash drift")
        for c in d["candidates"]:
            if c["materiality"]["proposed_blueprint_changes"]:
                problems.append(f"{e['slug']} {c['combo_id']}: overlay attempted Blueprint mutation")
            if c["materiality"]["material_fields_touched"]:
                problems.append(f"{e['slug']} {c['combo_id']}: material overlay must trigger targeted review, not auto-apply")
    # Negative gate self-test: a hypothetical commander_role edit must be material; a label-only note must not.
    if material_fields_touched([{"path": "/commander_role/value/level"}]) != ["commander_role"]:
        problems.append("materiality gate failed commander_role negative test")
    if material_fields_touched([{"path": "/overlay_label"}]):
        problems.append("materiality gate wrongly marks overlay-only label as material")
    print(f"power-core: {len(expected)} overlays, {len(problems)} problems")
    for x in problems[:40]:
        print("FAIL", x)
    return 1 if problems else 0


def summary_cmd():
    d = load(OUT / "summary.json")
    print(json.dumps(d["totals"], indent=2, sort_keys=True))
    return 0


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--build", action="store_true")
    a.add_argument("--check", action="store_true")
    a.add_argument("--summary", action="store_true")
    x = a.parse_args(argv)
    rc = 0
    if x.build: build()
    if x.check: rc |= check()
    if x.summary: rc |= summary_cmd()
    if not (x.build or x.check or x.summary): a.print_help()
    return rc


if __name__ == "__main__":
    sys.exit(main())
