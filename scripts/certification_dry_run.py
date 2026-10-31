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
KINDS = {"OWNER_APPROVAL", "OWNER_DECISION", "EXTERNAL_CI", "MISSING_SOURCE", "ENGINEERING_OPEN", "ONGOING"}


def B(kind, what, *evidence):
    return {"kind": kind, "what": what, "evidence": list(evidence)}


# Release-definition criteria (ids match release_readiness.CRITERIA, same order as the workflow list).
RELEASE_BLOCKERS = {
    "priority_enrichment": [
        B("OWNER_APPROVAL", "5,362/5,362 priority cards are enriched; the documented gaps (2,626 cards with no story lore "
          "yet, 1,304 of them Universes Beyond; 341 uncertain name-matched links) are listed, not resolved. Ticking the box "
          "means accepting that list as the documented exception set.",
          "data/card_enrichment.json", "data/lore_research/card_lore_links_2026-10-30.json"),
    ],
    "foundation_graph": [
        B("OWNER_APPROVAL", "Every claim pack, including foundational Packs A, B and C, is PRELIMINARY_RESEARCH; none is "
          "owner reviewed.", "data/multiverse_graph/manifest.json"),
        B("OWNER_DECISION", "Pack A genealogy disputes GD2-GD7 have no official statement that settles them; the owner "
          "decision cells are blank (GD1 has an official answer but is still unapplied).",
          "data/lore_research/pack_a_genealogy_disputes_2026-10-30.json"),
        B("MISSING_SOURCE", "L244 verified chronology is incomplete: story presents on different pages are unanchored, and "
          "Yawgmoth's end / Old Phyrexia's decimation have no official recap ordering (novel text is not ingested).",
          "data/lore_research/relative_chronology_2026-10-30.json"),
    ],
    "lookup_and_rules": [
        B("ENGINEERING_OPEN", "Bounded Phase 7 card/printing/set and published-rulings lookup is available, but "
          "undocumented interactions remain unmodelled (no game simulation) and later rules/ruling changes "
          "are not automatically reconciled.", "scripts/rules_interactions.py", "scripts/ask_rules_evidence.py",
          "scripts/ask_set_atlas.py"),
        B("EXTERNAL_CI", "'Current' Scryfall means a fresh snapshot at release time; the active snapshot is "
          "snap-20261029-40848334824-1 and the Oracle drift report must be re-run against the release snapshot.",
          "data/scryfall_snapshots"),
    ],
    "set_atlas": [
        B("ENGINEERING_OPEN", "Phase 1B QUALIFIED items: exact field parity between snapshots does not hold (342 prm release "
          "dates, 6 trk paper flags); Scryfall dates are not sourced street dates; the in-universe chronology is not linked "
          "to the release timeline.", "data/set_atlas/phase1b_snapshot_gates_2026-10-30.json"),
        B("OWNER_DECISION", "Whether the qualified gate (with its stated limitations and 555 optional source-pending records) "
          "is acceptable for the release.", "data/set_atlas/phase1b_qualified_functional_release_2026-10-29.json"),
    ],
    "knowledge_foundation": [
        B("EXTERNAL_CI", "The source-graded knowledge-foundation acceptance packet now exists with separate "
          "chronology ledgers, representative cited plane/character/faction/cross-plane evidence, explicit gaps and "
          "seventeen difficult Q&A cases. Its deterministic rebuild and representative rules/Q&A tests must still "
          "pass on the exact candidate foundation-release commit; it does not establish exhaustive knowledge.",
          "data/release/foundation_acceptance_packet_2026-10-30.json",
          "research/FOUNDATION_ACCEPTANCE_PACKET_2026-10-30.md"),
        B("OWNER_DECISION", "Cory reviews the actual knowledge-foundation scope and limitations after the "
          "engineering/CI evidence is complete. An owner-reviewed deck is NOT required.",
          "MTG_MULTIVERSE_MASTER_WORKFLOW.md"),
    ],
    "grixis_no_regression": [
        B("EXTERNAL_CI", "Focused Grixis mechanics validation must be green on the release commit, and the protected-path "
          "diff against dfc8891d must be empty.", ".github/workflows"),
    ],
    "ci_and_coverage": [
        B("EXTERNAL_CI", "All workflows green on the exact release commit.", ".github/workflows"),
        B("ONGOING", "Coverage report must be regenerated for the release batch (batch_recount).", "data/release"),
    ],
}

# Phase 8 items, in workflow order (matched by a leading phrase).
PHASE8_BLOCKERS = [
    ("Keep targeted CI checks", [
        B("OWNER_DECISION", "No documented set of required status checks protects main; choosing them is a repository "
          "setting only the owner can change.", ".github/workflows"),
    ]),
    ("Monitor new official stories", [
        B("ONGOING", "A read-only weekly workflow already checks Wizards story index, official rules/Commander page "
          "signals and Scryfall bulk timestamps, saving review artifacts without auto-ingesting changes. Its scope "
          "is deliberately not a complete story crawl or proof of rules changes; ongoing human review and release-time "
          "Oracle drift checks are still required.", ".github/workflows/multiverse-update-watch.yml",
          "scripts/monitor_multiverse_updates.py", "MTG_MULTIVERSE_MASTER_WORKFLOW.md"),
    ]),
    ("Rebuild and reconcile the Phase 1B set catalog", [
        B("ONGOING", "Triggered by new sets: the next is nau (Set API release 2027-02-05, no printings yet).",
          "data/set_atlas/phase1b_snapshot_gates_2026-10-30.json"),
    ]),
    ("Update snapshot manifests", [
        B("MISSING_SOURCE", "The 2026-10-28 data/printing_lore/manifest.json baseline has a hash but no byte count; L151's "
          "original file is unavailable.", "data/printing_lore/manifest.json", "scripts/audit_snapshot_manifests.py"),
    ]),
    ("Maintain an honest progress tracker", [
        B("ONGOING", "The current progress checkpoint now includes a generated completed / under review / blocked / "
          "not started triage for all 14 first-release and Phase 8 gates, with blocker types and an explicit "
          "distinction from the 137-item project checklist. It must keep regenerating as evidence changes.",
          "Progress Tracker.md", "scripts/update_multiverse_progress_tracker.py"),
    ]),
    ("Define an MTG Multiverse Companion milestone release", [
        B("OWNER_DECISION", "release_readiness.py now scores a knowledge-only foundation (verdict NOT_RELEASE_READY); "
          "the owner must review the documented foundation scope, not any pilot deck.",
          "scripts/release_readiness.py"),
    ]),
    ("Treat continual future MTG releases", [
        B("OWNER_DECISION", "A policy statement: checking it is the owner's call; the bot does not mark policy accepted.",
          "MTG_MULTIVERSE_MASTER_WORKFLOW.md"),
        B("ONGOING", "Maintenance track by design.", "MTG_MULTIVERSE_MASTER_WORKFLOW.md"),
    ]),
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
                                                  if r["blockers"] and all(b["kind"] in {"OWNER_APPROVAL", "OWNER_DECISION", "EXTERNAL_CI", "ONGOING"} for b in r["blockers"])],
            "problems": problems}


def to_md(d) -> str:
    L = ["# Certification checklist dry run (2026-10-30, Batch 14)", "",
         "Generated by `scripts/certification_dry_run.py` from `data/release/certification_dry_run_2026-10-30.json`. "
         "**This is a dry run, not certification.** It checks no box and approves nothing.", "",
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
