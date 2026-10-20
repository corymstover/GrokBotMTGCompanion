#!/usr/bin/env python3
"""Read-only scope/source guards for M6 reconciliation evidence PRs.

This is an evidence-preservation check, NOT an independent card-rules certification.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE_BRANCH = "chatgpt-cycle76-m6-refinement"
ALLOWED_PATHS = {
    ".github/workflows/m6-evidence-reconciliation.yml",
    "scripts/grixis_m6_evidence_only_check.py",
    "tests/test_m6_evidence_only_check.py",
}
ALLOWED_PREFIXES = (
    "data/grixis/m6/two_model_reconciliation/",
    "data/grixis/m6/owner_pass_c_substitute/",
)


def changed_paths() -> list[str]:
    base = os.environ.get("GITHUB_BASE_REF") or BASE_BRANCH
    subprocess.run(
        ["git", "fetch", "--no-tags", "origin", base],
        check=True, cwd=ROOT, capture_output=True, text=True,
    )
    mergebase = subprocess.check_output(
        ["git", "merge-base", "HEAD", f"origin/{base}"],
        cwd=ROOT, text=True,
    ).strip()
    changed = subprocess.check_output(
        ["git", "diff", "--name-only", mergebase, "HEAD"],
        cwd=ROOT, text=True,
    )
    return [x for x in changed.splitlines() if x]


def allowed_path(path: str) -> bool:
    return path in ALLOWED_PATHS or path.startswith(ALLOWED_PREFIXES)


def check_reconciliation(path: Path) -> list[str]:
    errors = []
    body = path.read_text(encoding="utf-8")
    txt = body.lower()
    if not re.search(r"\b[a-f0-9]{64}\b", body):
        errors.append(f"{path}: missing full canonical SHA-256 receipt")
    for name, test in [
        ("GitHub model comparison", "grokbot" in txt and "chatgpt" in txt),
        ("owner approval/lock context", "approved" in txt and "lock" in txt),
        ("clear independence disclaimer", bool(re.search(r"\bnot\s+(?:formally\s+)?independent\b", txt))),
        ("reconciliation disposition", any(k in txt for k in ("keep", "reject", "propose", "needs testing", "blocker"))),
    ]:
        if not test:
            errors.append(f"{path}: missing {name}")
    return errors


def check_protocol(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8").lower()
    checks = {
        "actual reviewer identity": "chatgpt" in text,
        "no true-independence impersonation": "not formally independent" in text or "not independent" in text,
        "immutable first-pass seal": "seal.json" in text and "stage_a.md" in text,
        "owner gate": "owner" in text and "approval" in text,
    }
    return [f"{path}: missing {label}" for label, good in checks.items() if not good]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", required=True)
    args = parser.parse_args()
    paths = changed_paths()
    if not paths:
        print("FAIL: no changed paths against integration", file=sys.stderr)
        return 1
    errors = []
    for item in paths:
        if not allowed_path(item):
            errors.append(f"Scope violation: {item}")
            continue
        path = ROOT / item
        if not path.is_file():
            errors.append(f"Evidence file missing or deleted: {item}")
            continue
        if item.startswith("data/grixis/m6/two_model_reconciliation/") and item.endswith(".md"):
            errors.extend(check_reconciliation(path))
        if item.endswith("PROTOCOL_JOSH_LEE_KWAI.md"):
            errors.extend(check_protocol(path))
    if errors:
        print("\n".join("FAIL: " + e for e in errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(paths)} changed evidence-only paths; no canonical, tracker, deep-review or GrokBot source changes. This is NOT independent Pass C.")
    for item in paths:
        print("  " + item)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
