#!/usr/bin/env python3
"""Keep the current Multiverse checkpoint at the top of the legacy Progress Tracker.

Only the fenced checkpoint is generated; legacy project history below it is preserved.
Use --check in CI. A checked engineering item is never called approved/certified.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "Progress Tracker.md"
START = "<!-- MULTIVERSE-CURRENT:START -->"
END = "<!-- MULTIVERSE-CURRENT:END -->"


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def gate_triage() -> tuple[list[dict], dict[str, int]]:
    """Truthful four-state triage of release/Phase8 gates, not all checklist items.

    The source is the typed certification dry run, never inferred from a loose
    substring in a checklist item's prose or an arbitrary completion target.
    """
    from certification_dry_run import dry_run
    audit = dry_run()
    if audit['problems']:
        raise ValueError('invalid certification blocker audit: ' + str(audit['problems']))
    rows = []
    for r in audit['release_definition'] + audit['phase8']:
        kinds = sorted({b['kind'] for b in r['blockers']})
        if r['workflow_checked']:
            status = 'Completed'
        elif any(k in kinds for k in ('MISSING_SOURCE', 'ENGINEERING_OPEN')):
            status = 'Blocked'
        elif kinds:
            status = 'Under review'
        else:
            status = 'Not started'
        rows.append({'id': r.get('id') or r['item'], 'status': status, 'blocker_kinds': kinds})
    counts = Counter(r['status'] for r in rows)
    return rows, {k: counts[k] for k in ('Completed', 'Under review', 'Blocked', 'Not started')}


def build() -> str:
    workflow = (ROOT / "MTG_MULTIVERSE_MASTER_WORKFLOW.md").read_text(encoding="utf-8")
    version = re.search(r"\*\*Version:\*\* ([\d.]+)", workflow)
    if not version:
        raise ValueError("Master Workflow has no version")
    checks = re.findall(r"^- \[(x| )\] ", workflow, re.M)
    graph_data = load("data/multiverse_graph/multiverse_graph.json")
    graph = graph_data["stats"]
    named_people_factions = {n['id'] for n in graph_data['nodes']
                            if n['type'] in {'Character', 'Faction'}}
    nonstructural = {'cited_by', 'asserts', 'see_also_curated_entry', 'proposed_in'}
    directly_cited = {endpoint for e in graph_data['edges']
                      if e.get('claim') and e['relation'] not in nonstructural
                      for endpoint in (e['from'], e['to']) if endpoint in named_people_factions}
    # Do not use the archived Batch-14 recount for *current* claimed counts.
    # New source-graded claim packs may be appended after that dated report.
    coverage = load("data/lore_research/story_coverage_inventory_2026-10-30.json")["totals"]
    enrichment = load("data/card_enrichment.json")["cards"]
    readiness = load("data/release/readiness_2026-10-30.json")["verdict"]
    done = sum(x == "x" for x in checks)
    assert len(enrichment) == 5362, "unexpected priority-enrichment count; review the tracker generator"
    current_claims = sum(graph["claims_by_status"].values())
    assert coverage["claims"] == current_claims, "story inventory and graph claim counts diverged"
    gate_rows, gate_counts = gate_triage()
    gate_lines = [
        '| Gate | Triage | Remaining blocker types |',
        '| --- | --- | --- |',
    ]
    for row in gate_rows:
        title = row['id']
        if len(title) > 65:
            title = title[:62].rstrip() + '…'
        gate_lines.append(f'| {title} | {row["status"]} | {", ".join(row["blocker_kinds"]) or "none"} |')
    gate_report = '\n'.join(gate_lines)
    return f"""{START}
## MTG Multiverse Companion — current engineering checkpoint (2026-10-31)

**Live authority:** [Master Workflow v{version.group(1)}](MTG_MULTIVERSE_MASTER_WORKFLOW.md), the current
graph and dated recount. The older cycle-36/October-15 metrics **below this section are historical**;
they are not the active Phase 1–8 completion counters.

| Measure | Verified committed state | Important limitation |
| --- | ---: | --- |
| Master Workflow checklist | **{done}/{len(checks)} checked; {len(checks)-done} open** | Engineering verification, never owner approval. |
| Priority card enrichments | **{len(enrichment)}/5,362** | Enrichment does not imply every card has a sourced story. |
| Source-page inventory | **{coverage['cited_pages']} cited + {coverage['reviewed_no_claim_pages']} reviewed = {coverage['pages']} accounted for** | Current inventoried pages only, not all fiction ever published. |
| Cited lore claims | **{current_claims}** | Live graph/inventory concordance; claim packs remain preliminary research. |
| Cited graph | **{graph['nodes']} nodes / {graph['edges']} edges** | Unresolved orphan/variant and chronology work remains. |
| Registered people/factions with direct claims | **{len(directly_cited)}/{len(named_people_factions)}** | At least one cited relation per registered node, **not** a complete biography or census of all canon. |
| Exact printing-specific representations | **{graph.get('exact_art_printings', 0)}** | Frozen snapshot + official art-file label evidence, **not** canon scene depiction. |
| In-universe dated claim edges | **{graph['claim_edges_with_in_universe_date']}** | Most graph edges lack a verified in-world date. |
| Parked graph-built Commander pilots | **3 unapproved** | Preserved, not a knowledge-foundation release gate. |
| Foundation-release readiness | **{readiness}** | Research, exact-release CI and engineering remain; Cory's conditional acceptance is recorded but not yet effective. |
| Official source watch | **Weekly review-only workflow** | Story index, Scryfall metadata and rules PDF candidates; not automatic lore/rules updates. |

**First-release and Phase 8 gate triage (14 gates, separate from the 137-item engineering checklist):**
Completed **{gate_counts['Completed']}** · Under review **{gate_counts['Under review']}** ·
Blocked **{gate_counts['Blocked']}** · Not started **{gate_counts['Not started']}**.
"Under review" does **not** mean approved; it includes pending owner decisions,
exact-commit CI and ongoing maintenance. "Blocked" means a documented missing
source or remaining engineering work. The complete typed evidence is in
`data/release/certification_dry_run_2026-10-30.json`.

{gate_report}

**Priority next steps:** verify current-era Q&A answers; close only evidence-backed graph
identity and chronology gaps; expand comprehensive plane, character, faction and cross-plane
history; harden rules and difficult Q&A; preserve the newly recovered hash-verified October
historical Scryfall replay and retest release-time data freshness; pursue foundation-only certification. **Phase 6
deckbuilding and its three unapproved pilots are deferred until the knowledge foundation
is certified.** Do not modify any of the 62 finalized Grixis decks.
{END}"""


def current_block(text: str) -> str | None:
    if START not in text or END not in text:
        return None
    return text[text.index(START):text.index(END)+len(END)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if the generated checkpoint is stale")
    args = ap.parse_args()
    old = TRACKER.read_text(encoding="utf-8")
    new = build()
    if args.check:
        good = current_block(old) == new
        print("PASS current progress checkpoint" if good else "STALE progress checkpoint")
        return 0 if good else 1
    if current_block(old):
        text = old.replace(current_block(old), new)
    else:
        heading = "# Progress Tracker\n"
        if heading not in old:
            raise SystemExit("Progress Tracker top-level heading missing")
        text = old.replace(heading, heading + "\n" + new + "\n", 1)
    TRACKER.write_text(text, encoding="utf-8")
    print("Updated current checkpoint in Progress Tracker.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
