# MTG Companion — current agent entry point

**Current baseline (2026-11-02):** Master Workflow **v3.09** records owner-selected
**bounded repository construction acceptance**: 131/137 historical boxes checked,
zero active build requirements, and six deliberately open items (three pilot
reviews and three perpetual upkeep duties). This is not universal lore, live
rules/ban, or empirical Commander power certification. See
[`MTG_MULTIVERSE_MASTER_WORKFLOW.md`](MTG_MULTIVERSE_MASTER_WORKFLOW.md),
[`data/release/bounded_repository_completion_2026-11-02.json`](data/release/bounded_repository_completion_2026-11-02.json),
and [`Progress Tracker.md`](Progress%20Tracker.md) for authoritative history.

**Current owner directive (v3.10 hardening):** Improve reliability and everyday
use: run the full offline test suite, fix failures and unsafe network fallback,
add natural-language card/rules regression cases, keep the entry-point docs
current, and carefully reconcile stale PRs and redundant CI. Do not rewrite
historical v3.09 acceptance, invent new approvals, or weaken source/confidence
labels. Any unresolved lore/rules question remains explicitly UNKNOWN.

**Protected owner decisions:** The 62 Grixis decks are governed by the separate
[`corymstover/grixis-commander-encyclopediaGPT`](https://github.com/corymstover/grixis-commander-encyclopediaGPT)
canonical approval registry (`state/current_deck_overrides.json` in **that
repository**, not at this repository root). This repo also contains an archived
Grixis source copy and local audit digests; neither supersedes the canonical
registry. All nine lore decks **#1–8 and #10** have owner approval receipts in
[`data/lore_decks/approvals/`](data/lore_decks/approvals/) and must remain
unchanged. The three graph-built foundation pilots remain **UNAPPROVED** and
are to be rebuilt/reviewed only on Cory's later explicit request.

**Testing:** Prefer reproducible tests with `SCRYFALL_OFFLINE=1` and
`MTG_SCRYFALL_MODE=multiverse`; a requested live update is separate and must
not silently alter snapshot locks. Treat red tests, cache-conditional tests,
and stale documentation as genuine maintenance work, not reason to revoke a
qualified historical certificate without evidence.

## Archived Grixis Encyclopedia one-command workflow (explicit requests only)

This entry-point supplements, never replaces, the existing M6/M6.x, I/J, M7 and GrokBot processes preserved in `chatgpt-cycle76-m6-refinement` (especially its `AGENTS.md`, `grixis/M6 Commander-First Single-Deck Review Standard.md`, `grixis/Commander-First Decisive Optimization and Test Economy Standard.md`, `data/grixis/m6/test_blueprints/`, and scoped M6/IJ evidence). The authoritative approval source remains canonical `corymstover/grixis-commander-encyclopediaGPT/main`.

**Required for any Grixis deck-finalization turn:** read [`grixis/M7 ONE_COMMAND FINISH.md`](grixis/M7%20ONE_COMMAND%20FINISH.md) fully. Cory's instruction “Finish Deck #N” authorizes complete bounded reuse, commander-first research, testing and a single exact 100-card approval packet without repeated “Proceed” prompts. Five honest swaps is the ordinary minimum, never a cap or quality target. Never fabricate changes or claim unsatisfied M6 P0/IJ verification passed.

The one-click `M7 One-Command Evidence Intake` Action is read-only evidence recovery and does **not** independently finish a deck, select swaps, approve it, modify canonical records or engage paid Grok. Exact owner SHA approval remains indispensable, followed by the canonical exact-head merge/postmerge lock protocol.

## Other MTG lore and creative decks (tools ready; explicit requests only)

The Grixis instructions above apply only to explicit Grixis finalization and must never be silently applied to a new lore-deck request. For knowledge queries, use [`LORE_QUERY_QUICKSTART.md`](LORE_QUERY_QUICKSTART.md), `scripts/lore_query.py`, `scripts/mv_ask.py`, and the cited graph, timeline and Q&A tools. [`LORE_DECKBUILDING_READY.md`](LORE_DECKBUILDING_READY.md), `scripts/story_deck_planner.py` and `scripts/evaluate_decklist.py` are available for a **new explicit** deckbuilding request. Separate printed facts, official story claims, contextual links, and creative flavor. An old draft's "awaiting approval" line does not override a later exact owner approval receipt; the nine approved lore deck specifications are protected. No unapproved pilot becomes locked by an engineering merge.
