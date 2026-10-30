#!/usr/bin/env python3
"""Keep the current Multiverse checkpoint at the top of the legacy Progress Tracker.

Only the fenced checkpoint is generated; legacy project history below it is preserved.
Use --check in CI. A checked engineering item is never called approved/certified.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "Progress Tracker.md"
START = "<!-- MULTIVERSE-CURRENT:START -->"
END = "<!-- MULTIVERSE-CURRENT:END -->"


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def build() -> str:
    workflow = (ROOT / "MTG_MULTIVERSE_MASTER_WORKFLOW.md").read_text(encoding="utf-8")
    version = re.search(r"\*\*Version:\*\* ([\d.]+)", workflow)
    if not version:
        raise ValueError("Master Workflow has no version")
    checks = re.findall(r"^- \[(x| )\] ", workflow, re.M)
    graph = load("data/multiverse_graph/multiverse_graph.json")["stats"]
    recount = load("data/release/batch_recount_2026-10-30_b14.json")["coverage"]
    enrichment = load("data/card_enrichment.json")["cards"]
    readiness = load("data/release/readiness_2026-10-30.json")["verdict"]
    done = sum(x == "x" for x in checks)
    assert len(enrichment) == 5362, "unexpected priority-enrichment count; review the tracker generator"
    return f"""{START}
## MTG Multiverse Companion — current engineering checkpoint (2026-10-30)

**Live authority:** [Master Workflow v{version.group(1)}](MTG_MULTIVERSE_MASTER_WORKFLOW.md), the current
graph and dated recount. The older cycle-36/October-15 metrics **below this section are historical**;
they are not the active Phase 1–8 completion counters.

| Measure | Verified committed state | Important limitation |
| --- | ---: | --- |
| Master Workflow checklist | **{done}/{len(checks)} checked; {len(checks)-done} open** | Engineering verification, never owner approval. |
| Priority card enrichments | **{len(enrichment)}/5,362** | Enrichment does not imply every card has a sourced story. |
| Source-page inventory | **{recount['cited_pages']} cited + {recount['reviewed_no_claim_pages']} reviewed = {recount['pages']} accounted for** | Current inventoried pages only, not all fiction ever published. |
| Cited lore claims | **{recount['claims']}** | Claim packs remain preliminary research. |
| Cited graph | **{graph['nodes']} nodes / {graph['edges']} edges** | Unresolved orphan/variant and chronology work remains. |
| In-universe dated claim edges | **{graph['claim_edges_with_in_universe_date']}** | Most graph edges lack a verified in-world date. |
| Unapproved graph-built Commander pilots | **3** | Cory has approved none of the three. |
| First-release readiness | **{readiness}** | Owner gates, external checks and ongoing engineering remain. |

**Priority next steps:** verify current-era Q&A answers; close only evidence-backed graph
identity and chronology gaps; expand comprehensive history and lore-first deck research;
restore the exact pinned Scryfall bulk when needed for source-level atlas replay; complete
owner review and release checks without modifying any of the 62 finalized Grixis decks.
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
