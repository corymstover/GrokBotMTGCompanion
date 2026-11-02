#!/usr/bin/env python3
"""Phase 8 certification-checklist DRY RUN (Batch 14).

Read-only. For every item in the workflow's "Definition of the first major Companion release" and every Phase 8
item, list exactly what blocks checking that box, typed by who/what can unblock it. It reuses
scripts/release_readiness.py for the machine status and reads checkbox state from MTG_MULTIVERSE_MASTER_WORKFLOW.md.

This tool never checks a box, approves, locks or certifies anything. A row with no blocker means "no mechanical
blocker found", which is still not owner sign-off.

Blocker kinds:
  OWNER_APPROVAL   Cory must review/approve an in-scope research artifact or evidence pack.
  OWNER_DECISION   Cory must decide a policy or a disputed question; the bot may not.
  OWNER_CONDITIONAL Cory's release-scope acceptance is already authorized, but not effective until every gate passes.
  EXTERNAL_CI      Must be shown green on GitHub for the exact release commit.
  MISSING_SOURCE   Needs a source the bot does not have (e.g. an unavailable original file, an official recap page).
  ENGINEERING_OPEN Non-owner work the bot can still do.
  ONGOING          Upkeep by design; the box describes a continuing practice.

  python3 scripts/certification_dry_run.py [--json] [--out data/release/certification_dry_run_2026-10-30.json] [--check]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
WORKFLOW = ROOT / "MTG_MULTIVERSE_MASTER_WORKFLOW.md"
OUT = ROOT / "data/release/certification_dry_run_2026-10-30.json"
KINDS = {"OWNER_APPROVAL", "OWNER_DECISION", "OWNER_CONDITIONAL", "EXTERNAL_CI", "MISSING_SOURCE", "ENGINEERING_OPEN", "ONGOING"}


def B(kind, what, *evidence):
    return {"kind": kind, "what": what, "evidence": list(evidence)}


# Release-definition criteria (ids match release_readiness.CRITERIA, same order as the workflow list).
RELEASE_BLOCKERS = {
    "priority_enrichment": [],  # v2.98 documented owner-accepted finite exception set, not canonical lore proof.
    "foundation_graph": [],  # Owner accepted limited *existing* primary-cited A/B/C connections; unknowns remain open research.
    "lookup_and_rules": [],  # Dated, fail-closed supported-source capability K133; no general simulator/current meld claim.
    "set_atlas": [],  # v2.98 qualified dated functional scope owner-accepted; optional source work remains open.
    "knowledge_foundation": [],  # Scoped research/Q&A accepted; exact release-commit CI separately K137.
    "grixis_no_regression": [],  # v3.00 immutable PR compare, protected hashes and focused-CI run evidence.
    "ci_and_coverage": [],  # v3.00 14/14 PR + 10/10 postmerge runs and hashed current batch recount.
}

# Phase 8 items, in workflow order (matched by a leading phrase).
PHASE8_BLOCKERS = [
    ("Keep targeted CI checks", []),  # v3.03 nine targeted PR CI domains accepted; branch protection is NOT asserted.
    ("Monitor new official stories", [
        B("ONGOING", "A read-only weekly workflow already checks Wizards story index, official rules/Commander page "
          "signals, official update-bulletin listing candidates and Scryfall bulk timestamps against the "
          "November 1 pinned manifest, saving review artifacts without auto-ingesting changes. Its scope "
          "is deliberately not a complete story crawl or proof of rules changes; ongoing human review and release-time "
          "Oracle drift checks are still required.", ".github/workflows/multiverse-update-watch.yml",
          "scripts/monitor_multiverse_updates.py", "data/maintenance/multiverse_update_monitor_baseline_2026-11-01.json"),
    ]),
    ("Rebuild and reconcile the Phase 1B set catalog", [
        B("ONGOING", "Triggered by new sets: the next is nau (Set API release 2027-02-05, no printings yet).",
          "data/set_atlas/phase1b_snapshot_gates_2026-10-30.json"),
    ]),
    ("Update snapshot manifests", []),  # Exact Oct 28/Oct 15–16 bytes recovered, hashed, independently replayed.
    ("Maintain an honest progress tracker", [
        B("ONGOING", "All 137 project tasks now have a deterministic Completed / Under review / Blocked / "
          "Not started audit and the 14 release/Phase 8 gates retain separate blocker triage. "
          "The engineering checkpoint is checked, but must keep regenerating as source evidence changes.",
          "Progress Tracker.md", "scripts/audit_full_checklist.py",
          "data/release/full_checklist_triage_2026-11-01.json"),
    ]),
    ("Define an MTG Multiverse Companion milestone release", []),  # Owner scope decision K129.
    ("Treat continual future MTG releases", []),  # Perpetual upkeep policy accepted; execution continues.
]


def section_items(heading_re):
    lines = WORKFLOW.read_text(encoding="utf-8").splitlines()
    out, on = [], False
    for ln in lines:
        if ln.startswith("## "):
            on = bool(re.match(heading_re, ln))
            continue
        m = re.match(r"- \[( |x)\] (.*)", ln) if on else None
        if m:
            out.append({"checked": m.group(1) == "x", "text": re.sub(r"\s*\*\(.*$", "", m.group(2)).strip()})
    return out


def _check_evidence(blockers, problems, where):
    for b in blockers:
        if b["kind"] not in KINDS:
            problems.append(f"{where}: bad kind {b['kind']}")
        for e in b["evidence"]:
            if not (ROOT / e).exists():
                problems.append(f"{where}: evidence path missing: {e}")


def dry_run() -> dict:
    import release_readiness as R
    rr = R.readiness()
    problems = []
    defs = section_items(r"## Definition of the first major Companion release")
    if len(defs) != len(R.CRITERIA):
        problems.append(f"workflow lists {len(defs)} release criteria, readiness scores {len(R.CRITERIA)}")
    release = []
    for (cid, text, _), row, item in zip(R.CRITERIA, rr["criteria"], defs):
        bl = RELEASE_BLOCKERS.get(cid, [])
        _check_evidence(bl, problems, cid)
        release.append({"id": cid, "criterion": item["text"], "workflow_checked": item["checked"],
                        "machine_status": row["status"], "machine_note": row["note"], "blockers": bl,
                        "blocked_by_owner": any(b["kind"].startswith("OWNER") for b in bl),
                        "bot_can_still_act": any(b["kind"] == "ENGINEERING_OPEN" for b in bl)})
    p8 = section_items(r"## Phase 8")
    phase8 = []
    for prefix, bl in PHASE8_BLOCKERS:
        hit = [i for i in p8 if i["text"].startswith(prefix)]
        if len(hit) != 1:
            problems.append(f"Phase 8 item not found exactly once: {prefix}")
            continue
        _check_evidence(bl, problems, prefix)
        phase8.append({"item": hit[0]["text"], "workflow_checked": hit[0]["checked"], "blockers": bl,
                       "blocked_by_owner": any(b["kind"].startswith("OWNER") for b in bl),
                       "bot_can_still_act": any(b["kind"] == "ENGINEERING_OPEN" for b in bl)})
    if len(phase8) != len(p8):
        problems.append(f"workflow has {len(p8)} Phase 8 items, dry run covers {len(phase8)}")
    tally = {}
    for r in release + phase8:
        for b in r["blockers"]:
            tally[b["kind"]] = tally.get(b["kind"], 0) + 1
    return {"schema": "certification_dry_run.v1", "status": "DRY_RUN_NOT_CERTIFICATION",
            "readiness_verdict": rr["verdict"], "readiness_tally": rr["tally"],
            "note": "Lists what blocks each box. Checks nothing, approves nothing, certifies nothing.",
            "release_definition": release, "phase8": phase8, "blocker_tally": dict(sorted(tally.items())),
            "items_blocked_only_by_owner_or_ci": [r.get("id") or r["item"] for r in release + phase8
                                                  if r["blockers"] and all(b["kind"] in {"OWNER_APPROVAL", "OWNER_DECISION", "OWNER_CONDITIONAL", "EXTERNAL_CI", "ONGOING"} for b in r["blockers"])],
            "problems": problems}


def to_md(d) -> str:
    L = ["# Certification checklist dry run (v3.00, revised 2026-11-01)", "",
         "Generated by `scripts/certification_dry_run.py` from `data/release/certification_dry_run_2026-10-30.json`. "
         "**This dry run is not the certificate.** All seven finite release gates have independently "
         "recorded evidence: five bounded source scopes plus two externally checked GitHub/protected-file "
         "gates in `data/release/foundation_milestone_certificate_2026-11-01.json`. The read-only "
         "machine evaluator continues to return EXTERNAL for GitHub results because offline reports "
         "cannot authenticate a future Actions run. Historical unknowns and future maintenance remain open.", "",
         f"Machine readiness verdict: **{d['readiness_verdict']}** ({d['readiness_tally']}). Blockers by kind: {d['blocker_tally']}.", ""]
    for title, rows, key in (("Definition of the first major Companion release", d["release_definition"], "criterion"),
                             ("Phase 8", d["phase8"], "item")):
        L += [f"## {title}", ""]
        for r in rows:
            box = "x" if r["workflow_checked"] else " "
            ms = f" (machine: {r['machine_status']})" if "machine_status" in r else ""
            L.append(f"- [{box}] **{r[key]}**{ms}")
            for b in r["blockers"]:
                L.append(f"  - `{b['kind']}`: {b['what']} Evidence: " + ", ".join(f"`{e}`" for e in b["evidence"]))
        L.append("")
    L += ["Items whose remaining blockers are only owner action, release-commit CI or ongoing upkeep: "
          + "; ".join(d["items_blocked_only_by_owner_or_ci"]) + ".", ""]
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--md", help="also write the Markdown summary here")
    ap.add_argument("--check", action="store_true", help="exit 1 if the committed dry run differs or has problems")
    a = ap.parse_args(argv)
    d = dry_run()
    text = json.dumps(d, indent=1, ensure_ascii=False) + "\n"
    if a.check:
        old = json.loads(OUT.read_text(encoding="utf-8")) if OUT.is_file() else None
        md = ROOT / "research/CERTIFICATION_DRY_RUN_2026-10-30.md"
        ok = not d["problems"] and old == d and md.is_file() and md.read_text(encoding="utf-8") == to_md(d)
        print("certification dry run:", "OK" if ok else "STALE_OR_PROBLEMS", d["problems"])
        return 0 if ok else 1
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    if a.md:
        Path(a.md).write_text(to_md(d), encoding="utf-8")
    if a.json or not a.out:
        print(text if a.json else f"{d['readiness_verdict']} {d['blocker_tally']} problems={d['problems']}")
    return 1 if d["problems"] else 0


if __name__ == "__main__":
    sys.exit(main())
