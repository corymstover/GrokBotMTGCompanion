#!/usr/bin/env python3
"""Fail-closed triage of the finite Master Workflow checklist (134/134).

The original 137 historic item positions remain stable; three unbounded
maintenance duties are archived as non-checkbox markers, not falsely checked.
Each exact Phase 6 owner signoff remains independently SHA-verified.
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
import audit_lore_pilot_owner_approvals as approvals  # noqa: E402

WORKFLOW = ROOT / "MTG_MULTIVERSE_MASTER_WORKFLOW.md"
OUT = ROOT / "data/release/full_checklist_triage_2026-11-01.json"
MD = ROOT / "research/FULL_CHECKLIST_TRIAGE_2026-11-01.md"
STATES = ("Completed", "Under review", "Blocked", "Not started")

ARCHIVED = {"K105": "Maintain an explicit coverage/gaps inventory",
            "K125": "Monitor new official stories",
            "K126": "Rebuild and reconcile the Phase 1B"}
ARCHIVE = ROOT / "docs/archive/RECURRING_CHECKLIST_ITEMS_2026-11-02.md"

def items() -> list[dict]:
    result, section, ordinal, seen_archived = [], "", 0, set()
    archive_text = ARCHIVE.read_text(encoding="utf-8")
    for lineno, line in enumerate(WORKFLOW.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("## "):
            section = line[3:]
            continue
        archived = re.fullmatch(r"<!-- HISTORICAL-MAINTENANCE (K\d{3}): moved to docs/MAINTENANCE_POLICY.md on 2026-11-02; no active checkbox -->", line)
        if archived:
            ordinal += 1
            key = f"K{ordinal:03d}"
            if archived.group(1) != key or key not in ARCHIVED or key in seen_archived:
                raise ValueError(f"unexpected or misnumbered maintenance marker: {line}")
            if f"## {key}\n" not in archive_text or ARCHIVED[key] not in archive_text:
                raise ValueError(f"{key}: archived exact duty is missing")
            seen_archived.add(key)
            continue
        match = re.match(r"^- \[([ x])\] (.*)$", line)
        if match:
            ordinal += 1
            result.append({"id": f"K{ordinal:03d}", "line": lineno, "section": section,
                           "checked": match.group(1) == "x", "task": match.group(2)})
    if seen_archived != set(ARCHIVED) or ordinal != 137:
        raise ValueError(f"historical positions altered: {ordinal}; archived={seen_archived}")
    return result


def build() -> dict:
    rows = items()
    if len(rows) != 134 or any(not r["checked"] for r in rows):
        raise ValueError(f"expected 134 checked finite tasks; found {len(rows)} with {sum(not r['checked'] for r in rows)} open")
    audit = D.dry_run()
    if audit["problems"]:
        raise ValueError("certification release audit invalid: " + repr(audit["problems"]))
    # A checked K112-114 must have exact, still-matching owner decision bytes;
    # the old draft approval=false flags alone are not present-day authority.
    approved = approvals.check()["checklist_ids"]
    for key in approved:
        row = next((r for r in rows if r["id"] == key), None)
        if not row or not row["checked"] or not row["task"].startswith("Pilot "):
            raise ValueError(f"{key}: owner-approved pilot checklist checkbox is missing")
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
            if row["id"] in approvals.EXPECTED:
                status, kind, note = ("Completed", "EXACT_OWNER_APPROVAL",
                                      "Cory approved this exact original decklist by SHA-256 on 2026-11-02; no cards changed, current gameplay legality/power not certified.")
            else:
                status, kind, note = "Completed", None, "Checklist-verified engineering task; this is not owner approval."
        elif ref is not None:
            kinds = [b["kind"] for b in ref["blockers"]]
            status = ("Blocked" if any(x in kinds for x in ("MISSING_SOURCE", "ENGINEERING_OPEN"))
                      else "Under review" if kinds else "Not started")
            kind = ",".join(sorted(set(kinds))) or "GATE_REVIEW_NOT_STARTED"
            note = "; ".join(b["what"] for b in ref["blockers"]) or "No release-gate evidence reviewed yet."
        elif phase.startswith("Phase 6"):
            raise ValueError(f"{row['id']}: Phase 6 unchecked despite exact approved pilot register")
        else:
            raise ValueError(f"{row['id']}: new unchecked task in finite checklist")
        row.update({"status": status, "blocker_kind": kind, "reason": note})
        row.update({"completion_scope": "COMPLETED", "build_scope_reason": None})
    if p8_idx != len(audit["phase8"]) or release_idx != len(audit["release_definition"]):
        raise ValueError("release/Phase 8 audit and checklist item counts disagree")
    counts = collections.Counter(r["status"] for r in rows)
    scopes = collections.Counter(r["completion_scope"] for r in rows)
    if len(rows) != counts["Completed"] or scopes["COMPLETED"] != 134:
        raise ValueError("active checklist not completely finite/checked")
    phases = {}
    for phase in dict.fromkeys(r["section"] for r in rows):
        part = [r for r in rows if r["section"] == phase]
        phases[phase] = {"total": len(part), "checked": sum(r["checked"] for r in part),
                         "open": sum(not r["checked"] for r in part),
                         "active_build": sum(r["completion_scope"] == "ACTIVE_REPOSITORY_BUILD" for r in part),
                         "excluded_from_build": sum(r["completion_scope"] == "RECURRING_MAINTENANCE" for r in part)}
    return {"schema": "full-engineering-checklist-triage/v1", "as_of": "2026-11-02",
            "authority": "MTG_MULTIVERSE_MASTER_WORKFLOW.md",
            "disclaimer": "134 finite tasks; three historical recurring duties K105/K125/K126 are archived outside the checklist, never checked permanently. K112-K114 have separate exact owner pilot approvals; the numbered lore deck #9 approval is tracked separately. Checked engineering tasks do not imply live gameplay certification.",
            "totals": {"items": len(rows), "checked": counts["Completed"],
                       "open": len(rows) - counts["Completed"],
                       "historical_positions": 137, "archived_recurring_duties": 3,
                       "remaining_repository_build": scopes["ACTIVE_REPOSITORY_BUILD"],
                       "excluded_from_repository_build": scopes["RECURRING_MAINTENANCE"],
                       "post_build_pilot_reviews": scopes["POST_BUILD_PILOT_REVIEW"],
                       "recurring_maintenance": scopes["RECURRING_MAINTENANCE"],
                       "by_status": {k: counts[k] for k in STATES}},
            "by_phase": phases, "items": rows}


def markdown(data: dict) -> str:
    t = data["totals"]
    lines = ["# Complete Master Workflow checklist triage — 2026-11-02", "",
             f"**{t['checked']}/{t['items']} checked; {t['open']} open.** "
             + "; ".join(f"{k}: {v}" for k, v in t["by_status"].items()) + ".", "",
             f"**Repository finish line: {t['remaining_repository_build']} actionable build items remain.** "
             "Three unbounded maintenance duties were removed from the active checkbox list "
             "and preserved as K105/K125/K126 in `docs/archive/RECURRING_CHECKLIST_ITEMS_2026-11-02.md`; "
             "their work continues under `docs/MAINTENANCE_POLICY.md`.", "",
             "This checklist inventory alone is **not a foundation certificate**; the separate v3.00 SHA-pinned "
             "milestone certificate records external CI. Three exact original pilot decklists were subsequently "
             "owner-approved by SHA-256, without rebuilding, under the newer v3.11 decision; "
             "current Commander legality and gameplay power remain uncertified. Upkeep continues after release.", "",
             "The machine-readable JSON preserves the 134 active tasks with stable historical K-IDs. "
             "The three archived original duties remain available verbatim in the dated archive.", ""]
    for phase, counts in data["by_phase"].items():
        lines += [f"## {phase}", "", f"{counts['checked']}/{counts['total']} checked; "
                  f"{counts['active_build']} remaining build; {counts['excluded_from_build']} excluded from finish line.", ""]
        for item in (i for i in data["items"] if i["section"] == phase and i["completion_scope"] == "ACTIVE_REPOSITORY_BUILD"):
            clean = re.sub(r"\s*\*\(.*$", "", item["task"]).strip()
            lines.append(f"- **{item['id']} · {item['status']} · {item['blocker_kind']}** — {clean}")
            lines.append(f"  - {item['reason']}")
        lines.append("")
    lines += ["## Ongoing obligations (not checklist items)", "",
              "K105 coverage/gaps, K125 official source/rules watch, and K126 set/printing "
              "reconciliation are preserved in the linked maintenance policy, not left open forever.", ""]
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
            raise ValueError("full finite-checklist triage stale or missing")
    else:
        OUT.write_text(json_text, encoding="utf-8")
        MD.write_text(md_text, encoding="utf-8")
    print("PASS all-checklist triage", report["totals"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
