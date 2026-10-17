#!/usr/bin/env python3
"""Step F integration/closure checker.

True closure requires complete 62-deck bracket suites/routing/red-team artifacts plus executed canonical-deck Step-E
mechanic evidence for every preregistered mechanic item. Judgment prompts intentionally remain pending real review and
are not treated as automated failures. Partial/missing infrastructure or pending mechanic execution is an error.
"""
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
S = ROOT / "scripts"
REG = ROOT / "data/grixis/registry.json"
SUITES = ROOT / "data/grixis/bracket_stress"
MECH = ROOT / "data/grixis/bracket_stress_mechanics"
ROUTED = ROOT / "data/grixis/bracket_stress_packets"
RED = ROOT / "data/grixis/bracket_red_team"


def run(script):
    p = subprocess.run([sys.executable, str(S / script), "--check"], cwd=ROOT, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip().splitlines()


def count(d):
    return len([p for p in Path(d).glob("*.json") if p.name != "summary.json"]) if Path(d).exists() else 0


def expected_b5():
    n = 0
    for p in SUITES.glob("*.json"):
        if p.name == "summary.json":
            continue
        if json.loads(p.read_text(encoding="utf-8"))["bracket"]["suite_family"] == "B5_competitive":
            n += 1
    return n


def check():
    expected = len(json.loads(REG.read_text(encoding="utf-8"))["decks"])
    probs = []
    checks = []
    for name, script in (
        ("suite", "grixis_bracket_stress.py"),
        ("mechanics", "grixis_bracket_mechanics.py"),
        ("routing", "grixis_bracket_stress_runner.py"),
        ("red-team", "grixis_bracket_red_team.py"),
        ("gain", "grixis_bracket_stress_gain.py"),
    ):
        rc, out = run(script)
        checks.append((name, rc, out[-2:] if out else []))
        if rc:
            probs.append(f"{name} checker failed")
    for name, d, n_expected in (
        ("suite", SUITES, expected),
        ("mechanics", MECH, expected_b5()),
        ("routing", ROUTED, expected),
        ("red-team", RED, expected),
    ):
        n = count(d)
        if n != n_expected:
            probs.append(f"{name} population {n}/{n_expected}")

    module_pending = module_executed = judgment_pending = 0
    if count(ROUTED) == expected:
        for p in [p for p in ROUTED.glob("*.json") if p.name != "summary.json"]:
            d = json.loads(p.read_text(encoding="utf-8"))
            for x in d["items"]:
                st = x["evidence"]["status"]
                module_pending += st == "pending_deck_level_module_execution"
                module_executed += st == "executed_deck_level_module_result"
                judgment_pending += st == "judgment_required"
                if x["kind"] == "mechanic_module" and st != "executed_deck_level_module_result":
                    probs.append(f"{d['slug']}:{x['id']}: mechanic item not executed ({st})")

    if module_pending:
        probs.append(f"{module_pending} mechanic item(s) still pending deck-level execution")

    print("bracket-stress-step:")
    for name, rc, out in checks:
        print(f"  {name}: {'PASS' if rc == 0 else 'FAIL'}")
        for line in out:
            print("   ", line)
    print(f"  mechanic items executed on frozen canonical decks: {module_executed}")
    print(f"  mechanic items pending local deck-level execution: {module_pending}")
    print(f"  judgment items intentionally pending real review: {judgment_pending}")
    if not probs:
        print("bracket-stress-step: COMPLETE — infrastructure and required bounded mechanic execution closed; judgment remains human-only")
    for p in probs[:100]:
        print("FAIL", p)
    return 1 if probs else 0


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--check", action="store_true")
    x = a.parse_args(argv)
    if x.check:
        return check()
    a.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
