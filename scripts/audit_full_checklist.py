#!/usr/bin/env python3
"""Deterministic, honest four-state triage of every Master Workflow checkbox.

Unlike the separate seven-criterion release-readiness test, this inventory covers
all 137 engineering tasks, including optional research, continuing maintenance,
and the ten Phase 6 items explicitly deferred until foundation certification.
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
OUT = ROOT / "data/release/full_checklist_triage_2026-10-31.json"
MD = ROOT / "research/FULL_CHECKLIST_TRIAGE_2026-10-31.md"
STATES = ("Completed", "Under review", "Blocked", "Not started")

# Explicitly classified open engineering work OUTSIDE the separate release/
# Phase 8 gates and Cory's protected post-foundation deckbuilding phase.
# The first match is not used: all keys must match exactly one open item.
OPEN = {
    "Independently corroborate `fbb` and `4bb`": ("Blocked", "MISSING_PRIMARY_SOURCE", "Wizards evidence for two foreign-border printing variants is still unverified."),
    "Resolve the remaining **2** curated/reprint": ("Blocked", "MISSING_PRIMARY_SOURCE", "Thirteen named catalog exceptions lack individual Wizards product evidence."),
    "Research the remaining **11** older boxed": ("Blocked", "MISSING_PRIMARY_SOURCE", "Older preconstructed/regional box codes need first-party product citations."),
    "Publish reproducible totals for **all Scryfall set codes**": ("Under review", "QUALIFIED_SCOPE", "All 1,062 categories are counted; an all-time first-party premier-set count is not certified."),
    "Verify debut/reprint attribution using dated": ("Under review", "QUALIFIED_DATES", "Stable printing IDs are audited, but Scryfall first-card dates are not verified product street dates."),
    "Maintain two separately labeled timelines": ("Under review", "CHRONOLOGY_GAPS", "Real-world release dates and in-world events remain separate; cited bridges are incomplete."),
    "Connect sets to supported planes": ("Under review", "SOURCE_GRADING", "Existing cited story-series joins are not exhaustive set-to-canon relationships."),
    "Link direct printed depictions": ("Under review", "SOURCE_GRADING", "Proof tiers and 570 printing labels exist, but direct depiction evidence remains incomplete."),
    "Expand the primary-source inventory": ("Under review", "ONGOING_SOURCE_RESEARCH", "The source roster and quotation audits require continued expansion/review."),
    "Record directional, dated, cited relationships": ("Under review", "CHRONOLOGY_GAPS", "Only a subset of graph relations carry source-quoted in-universe time phrases."),
    "**Pack A: Ugin, Nicol Bolas": ("Under review", "PRELIMINARY_LORE", "Elder Dragon War history and genealogy are researched but not exhaustively settled."),
    "Finish Pack A's disputed Elder Dragon War": ("Blocked", "OWNER_AND_SOURCE_DECISION", "Several conflicting genealogies require citations or explicit decisions; pilots remain parked."),
    "**Pack B: Thran civilization": ("Under review", "PRELIMINARY_LORE", "Source-local chronology and biographies do not yet constitute a complete Thran/Brothers' War history."),
    "**Pack C: Dominaria": ("Under review", "PRELIMINARY_LORE", "The cited Weatherlight/Invasion sequence is only a bounded history, not the full Legacy account."),
    "For each pack, publish a verified chronology": ("Under review", "CHRONOLOGY_GAPS", "Cross-ledger bridges, provenance limits and unresolved ordering still need synthesis."),
    "Expand the Mending, major planeswalkers": ("Under review", "COVERAGE_GAPS", "Mending and Gatewatch biographies/events are not comprehensively source-audited."),
    "Expand Bolas's schemes": ("Under review", "COVERAGE_GAPS", "War of the Spark sources are only partially extracted."),
    "Expand Mirrodin/New Phyrexia": ("Under review", "COVERAGE_GAPS", "Main-story claim packs do not exhaust side stories or consequences."),
    "Expand Omenpaths": ("Under review", "COVERAGE_GAPS", "Newer stories and continuity changes require further cited claims."),
    "Audit major planes, regions": ("Under review", "COVERAGE_GAPS", "A registered 33-plane inventory is not a complete canon census or biography set."),
    "Connect cross-plane histories": ("Under review", "CHRONOLOGY_GAPS", "Explicit SAME_EVENT bridges exist, but most cross-plane order/retcon claims are unresolved."),
    "Use the Phase 1B Set & Printing Atlas": ("Under review", "SOURCE_GRADING", "Atlas-to-story and era joins are incomplete; publication must not imply in-world time."),
    "Maintain an explicit coverage/gaps inventory": ("Under review", "ONGOING_SOURCE_TRIAGE", "Dated coverage inventory exists, but future sources and gap reports remain ongoing."),
    "Answer obscure lore and chronology": ("Under review", "QA_COVERAGE", "Cited Q&A works on bounded claims; unsupported questions remain UNKNOWN."),
    "Integrate card, lore and rules search": ("Under review", "QA_COVERAGE", "Cross-domain answer routes and current rules edges need further breadth."),
    "Test difficult representative queries": ("Under review", "QA_COVERAGE", "49 representative acceptance questions are a regression sample, not exhaustive interaction coverage."),
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
            status, kind = "Blocked", "POST_FOUNDATION_DEFERRED"
            note = "Cory deferred all Phase 6 deckbuilding/pilots until the knowledge foundation is certified."
        else:
            matches = [key for key in OPEN if row["task"].startswith(key)]
            if len(matches) != 1:
                raise ValueError(f"{row['id']}: unchecked task must have exactly one curated triage entry: {row['task'][:90]}")
            key = matches[0]
            manual_found[key] += 1
            status, kind, note = OPEN[key]
        row.update({"status": status, "blocker_kind": kind, "reason": note})
    if set(manual_found) != set(OPEN) or any(x != 1 for x in manual_found.values()):
        raise ValueError("curated triage map has unused/duplicate prefixes: " + repr(manual_found))
    if p8_idx != len(audit["phase8"]) or release_idx != len(audit["release_definition"]):
        raise ValueError("release/Phase 8 audit and checklist item counts disagree")
    counts = collections.Counter(r["status"] for r in rows)
    phases = {}
    for phase in dict.fromkeys(r["section"] for r in rows):
        part = [r for r in rows if r["section"] == phase]
        phases[phase] = {"total": len(part), "checked": sum(r["checked"] for r in part),
                         "open": sum(not r["checked"] for r in part)}
    return {"schema": "full-engineering-checklist-triage/v1", "as_of": "2026-10-31",
            "authority": "MTG_MULTIVERSE_MASTER_WORKFLOW.md",
            "disclaimer": "All 137 tasks, not the seven foundation-release criteria; completed means a checked engineering task, not certified lore or deck approval.",
            "totals": {"items": len(rows), "checked": counts["Completed"],
                       "open": len(rows) - counts["Completed"],
                       "by_status": {k: counts[k] for k in STATES}},
            "by_phase": phases, "items": rows}


def markdown(data: dict) -> str:
    t = data["totals"]
    lines = ["# Complete Master Workflow checklist triage — 2026-10-31", "",
             f"**{t['checked']}/{t['items']} checked; {t['open']} open.** "
             + "; ".join(f"{k}: {v}" for k, v in t["by_status"].items()) + ".", "",
             "This inventory is **not foundation certification**. Deferred Phase 6 tasks remain deliberately blocked, "
             "not silently completed; ongoing maintenance and source gaps are included.", "",
             "The machine-readable JSON records every task, its original workflow line, triage, blocker kind and reason.", ""]
    for phase, counts in data["by_phase"].items():
        lines += [f"## {phase}", "", f"{counts['checked']}/{counts['total']} checked; {counts['open']} open.", ""]
        for item in (i for i in data["items"] if i["section"] == phase and not i["checked"]):
            clean = re.sub(r"\s*\*\(.*$", "", item["task"]).strip()
            lines.append(f"- **{item['id']} · {item['status']} · {item['blocker_kind']}** — {clean}")
            lines.append(f"  - {item['reason']}")
        lines.append("")
    return "\n".join(lines)


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
