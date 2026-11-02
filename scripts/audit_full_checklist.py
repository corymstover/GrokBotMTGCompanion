#!/usr/bin/env python3
"""Deterministic, honest four-state triage of every Master Workflow checkbox.

Unlike the separate seven-criterion release-readiness test, this inventory covers
all 137 engineering tasks, including optional research, continuing maintenance,
and the Phase 6 items resumed after independently certified foundation.
No item is marked complete by this tool and none of these statuses is approval.
Each unchecked non-release item has a manually curated, fail-closed blocker
classification; additions must be reviewed before this report can regenerate.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import certification_dry_run as D  # noqa: E402

WORKFLOW = ROOT / "MTG_MULTIVERSE_MASTER_WORKFLOW.md"
OUT = ROOT / "data/release/full_checklist_triage_2026-11-01.json"
MD = ROOT / "research/FULL_CHECKLIST_TRIAGE_2026-11-01.md"
STATES = ("Completed", "Under review", "Blocked", "Not started")

# v3.05 owner-defined repository finish line: these unchecked historical
# checklist entries are real records, but are NOT unfinished repository-build
# work. They must never be auto-checked or used to approve a preserved pilot.
# Revalidate the task wording so future numbering edits cannot silently move
# an exclusion to an unrelated engineering gate.
EXCLUDED_FROM_BUILD = {
    "K105": ("RECURRING_MAINTENANCE", "Maintain an explicit coverage/gaps inventory", "Future source/coverage watch continues after a finished repository release."),
    "K112": ("POST_BUILD_PILOT_REVIEW", "Pilot 1:", "Cory will rebuild and individually review this pilot after repository development is finished."),
    "K113": ("POST_BUILD_PILOT_REVIEW", "Pilot 2:", "Cory will rebuild and individually review this pilot after repository development is finished."),
    "K114": ("POST_BUILD_PILOT_REVIEW", "Pilot 3:", "Cory will rebuild and individually review this pilot after repository development is finished."),
    "K125": ("RECURRING_MAINTENANCE", "Monitor new official stories", "Future story, rules, Oracle and release monitoring continues after the build finish line."),
    "K126": ("RECURRING_MAINTENANCE", "Rebuild and reconcile the Phase 1B", "Future-set re-ingestion is event-triggered upkeep, not unfinished initial construction."),
}

# Explicitly classified open engineering work OUTSIDE the separate release/
# Phase 8 gates and Cory's protected post-foundation deckbuilding phase.
# The first match is not used: all keys must match exactly one open item.
OPEN = {
    "Maintain an explicit coverage/gaps inventory": ("Under review", "ONGOING_SOURCE_TRIAGE", "Dated coverage inventory exists, but future sources and gap reports remain ongoing."),
}

# The v3.00 certified foundation lifted the prerequisite. The v3.02 bounded
# engine audit completes K106/K109/K111/K115, but unreviewed gameplay and
# individually unapproved pilot proposals are not inferred complete.
PHASE6_OPEN = {
    "Pilot 1:": ("Blocked", "INDIVIDUAL_PILOT_APPROVAL_PENDING", "Ugin/Bolas proposal is UNAPPROVED and requires explicit individual deck review."),
    "Pilot 2:": ("Blocked", "INDIVIDUAL_PILOT_APPROVAL_PENDING", "Primeval Dragons proposal is UNAPPROVED and requires explicit individual deck review."),
    "Pilot 3:": ("Blocked", "INDIVIDUAL_PILOT_APPROVAL_PENDING", "Ugin Allies proposal is UNAPPROVED and requires explicit individual deck review."),
}


def items() -> list[dict]:
    result, section = [], ""
    for lineno, line in enumerate(WORKFLOW.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("## "):
            section = line[3:]
            continue
        match = re.match(r"^- \[([ x])\] (.*)$", line)
        if match:
            result.append({"id": f"K{len(result)+1:03d}", "line": lineno, "section": section,
                           "checked": match.group(1) == "x", "task": match.group(2)})
    return result


def build() -> dict:
    rows = items()
    if len(rows) != 137:
        raise ValueError(f"expected all 137 project tasks; found {len(rows)}")
    audit = D.dry_run()
    if audit["problems"]:
        raise ValueError("certification release audit invalid: " + repr(audit["problems"]))
    manual_found = collections.Counter()
    p8_idx = release_idx = 0
    for row in rows:
        phase = row["section"]
        if phase.startswith("Phase 8"):
            ref = audit["phase8"][p8_idx]
            p8_idx += 1
        elif phase.startswith("Definition of the first major"):
            ref = audit["release_definition"][release_idx]
            release_idx += 1
        else:
            ref = None
        if row["checked"]:
            status, kind, note = "Completed", None, "Checklist-verified engineering task; this is not owner approval."
        elif ref is not None:
            kinds = [b["kind"] for b in ref["blockers"]]
            status = ("Blocked" if any(x in kinds for x in ("MISSING_SOURCE", "ENGINEERING_OPEN"))
                      else "Under review" if kinds else "Not started")
            kind = ",".join(sorted(set(kinds))) or "GATE_REVIEW_NOT_STARTED"
            note = "; ".join(b["what"] for b in ref["blockers"]) or "No release-gate evidence reviewed yet."
        elif phase.startswith("Phase 6"):
            matches = [key for key in PHASE6_OPEN if row["task"].startswith(key)]
            if len(matches) != 1:
                raise ValueError(f"{row['id']}: open post-foundation Phase 6 task not classified")
            status, kind, note = PHASE6_OPEN[matches[0]]
        else:
            matches = [key for key in OPEN if row["task"].startswith(key)]
            if len(matches) != 1:
                raise ValueError(f"{row['id']}: unchecked task must have exactly one curated triage entry: {row['task'][:90]}")
            key = matches[0]
            manual_found[key] += 1
            status, kind, note = OPEN[key]
        row.update({"status": status, "blocker_kind": kind, "reason": note})
        exclusion = EXCLUDED_FROM_BUILD.get(row["id"])
        if exclusion:
            scope, expected_prefix, explanation = exclusion
            if row["checked"] or not row["task"].startswith(expected_prefix):
                raise ValueError(f"{row['id']}: stale owner-defined finish-line exclusion")
            row.update({"completion_scope": scope, "build_scope_reason": explanation})
        else:
            row.update({"completion_scope": "COMPLETED" if row["checked"] else "ACTIVE_REPOSITORY_BUILD",
                        "build_scope_reason": None})
    if set(manual_found) != set(OPEN) or any(x != 1 for x in manual_found.values()):
        raise ValueError("curated triage map has unused/duplicate prefixes: " + repr(manual_found))
    if p8_idx != len(audit["phase8"]) or release_idx != len(audit["release_definition"]):
        raise ValueError("release/Phase 8 audit and checklist item counts disagree")
    counts = collections.Counter(r["status"] for r in rows)
    scopes = collections.Counter(r["completion_scope"] for r in rows)
    if (scopes["ACTIVE_REPOSITORY_BUILD"] + scopes["POST_BUILD_PILOT_REVIEW"]
            + scopes["RECURRING_MAINTENANCE"] != len(rows) - counts["Completed"]
            or scopes["POST_BUILD_PILOT_REVIEW"] != 3
            or scopes["RECURRING_MAINTENANCE"] != 3):
        raise ValueError("owner-defined build scope does not reconcile with 137 historical tasks")
    phases = {}
    for phase in dict.fromkeys(r["section"] for r in rows):
        part = [r for r in rows if r["section"] == phase]
        phases[phase] = {"total": len(part), "checked": sum(r["checked"] for r in part),
                         "open": sum(not r["checked"] for r in part),
                         "active_build": sum(r["completion_scope"] == "ACTIVE_REPOSITORY_BUILD" for r in part),
                         "excluded_from_build": sum(r["completion_scope"] in (
                             "POST_BUILD_PILOT_REVIEW", "RECURRING_MAINTENANCE") for r in part)}
    return {"schema": "full-engineering-checklist-triage/v1", "as_of": "2026-11-01",
            "authority": "MTG_MULTIVERSE_MASTER_WORKFLOW.md",
            "disclaimer": "All 137 tasks, not the seven foundation-release criteria; completed means a checked engineering task, not certified lore or deck approval.",
            "totals": {"items": len(rows), "checked": counts["Completed"],
                       "open": len(rows) - counts["Completed"],
                       "remaining_repository_build": scopes["ACTIVE_REPOSITORY_BUILD"],
                       "excluded_from_repository_build": scopes["POST_BUILD_PILOT_REVIEW"] + scopes["RECURRING_MAINTENANCE"],
                       "post_build_pilot_reviews": scopes["POST_BUILD_PILOT_REVIEW"],
                       "recurring_maintenance": scopes["RECURRING_MAINTENANCE"],
                       "by_status": {k: counts[k] for k in STATES}},
            "by_phase": phases, "items": rows}


def markdown(data: dict) -> str:
    t = data["totals"]
    lines = ["# Complete Master Workflow checklist triage — 2026-11-01", "",
             f"**{t['checked']}/{t['items']} checked; {t['open']} open.** "
             + "; ".join(f"{k}: {v}" for k, v in t["by_status"].items()) + ".", "",
             f"**Repository finish line: {t['remaining_repository_build']} actionable build items remain.** "
             f"{t['excluded_from_repository_build']} unchecked historical items are excluded: "
             f"{t['post_build_pilot_reviews']} post-build pilot reviews and "
             f"{t['recurring_maintenance']} recurring upkeep tasks. None is treated as finished or as a release blocker.", "",
             "This checklist inventory alone is **not a foundation certificate**; the separate v3.00 SHA-pinned "
             "milestone certificate records external CI. Pilot reviews are deferred until decks are rebuilt "
             "using the completed repository data; upkeep continues after release.", "",
             "The machine-readable JSON preserves all 137 original tasks with their build-scope classification.", ""]
    for phase, counts in data["by_phase"].items():
        lines += [f"## {phase}", "", f"{counts['checked']}/{counts['total']} checked; "
                  f"{counts['active_build']} remaining build; {counts['excluded_from_build']} excluded from finish line.", ""]
        for item in (i for i in data["items"] if i["section"] == phase and i["completion_scope"] == "ACTIVE_REPOSITORY_BUILD"):
            clean = re.sub(r"\s*\*\(.*$", "", item["task"]).strip()
            lines.append(f"- **{item['id']} · {item['status']} · {item['blocker_kind']}** — {clean}")
            lines.append(f"  - {item['reason']}")
        lines.append("")
    lines += ["## Outside repository-build completion (not remaining work)", "",
              "These stay unchecked in the archival 137-task record. They are not counted in the repository finish line.", ""]
    for item in (i for i in data["items"] if i["completion_scope"] in (
            "POST_BUILD_PILOT_REVIEW", "RECURRING_MAINTENANCE")):
        clean = re.sub(r"\s*\*\(.*$", "", item["task"]).strip()
        lines.append(f"- **{item['id']} · {item['completion_scope']}** — {clean}")
        lines.append(f"  - {item['build_scope_reason']}")
    lines.append("")
    return "\n".join(lines).rstrip("\n") + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    report = build()
    json_text = json.dumps(report, indent=1, ensure_ascii=False) + "\n"
    md_text = markdown(report)
    if args.check:
        if not OUT.is_file() or OUT.read_text(encoding="utf-8") != json_text or not MD.is_file() or MD.read_text(encoding="utf-8") != md_text:
            raise ValueError("full 137-task checklist triage stale or missing")
    else:
        OUT.write_text(json_text, encoding="utf-8")
        MD.write_text(md_text, encoding="utf-8")
    print("PASS all-checklist triage", report["totals"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
