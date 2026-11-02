# MTG Companion — current agent entry point

**Current baseline (2026-11-02):** Master Workflow **v3.12** retains v3.09's
owner-selected **bounded repository construction acceptance**, plus the new
explicit owner approval of the three exact original Phase 6 pilot hashes.
**134/134 finite checklist items are checked; 0 are open.** Historical
K105/K125/K126 moved to [continuing maintenance](docs/MAINTENANCE_POLICY.md),
not falsely completed forever. This is not universal lore, live
rules/ban, or empirical Commander power certification. See
[`MTG_MULTIVERSE_MASTER_WORKFLOW.md`](MTG_MULTIVERSE_MASTER_WORKFLOW.md),
[`data/release/bounded_repository_completion_2026-11-02.json`](data/release/bounded_repository_completion_2026-11-02.json),
and [`Progress Tracker.md`](Progress%20Tracker.md) for authoritative history.

**Repository visibility:** Cory explicitly chose to keep
`corymstover/GrokBotMTGCompanion` **public** on 2026-11-02. Do not change its
visibility without a later owner direction.

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
registry. All ten lore decks **#1–#10**, including the exact Ugin #9 historical
list with its banned Emrakul Rule 0 exception, are indexed in
[`docs/LORE_DECK_APPROVAL_INDEX.md`](docs/LORE_DECK_APPROVAL_INDEX.md), with
exact owner approval receipts in [`data/lore_decks/approvals/`](data/lore_decks/approvals/), and must remain
unchanged, with [#9's SHA-bound owner receipt](data/lore_decks/owner_decisions/2026-11-02_cory_approved_lore_deck_9_ugin.md).
The three graph-built foundation pilots are now **OWNER APPROVED
AS EXACT HISTORICAL OCTOBER 29 LISTS**, according to
[`data/lore_decks/owner_decisions/2026-11-02_cory_approved_phase6_pilots.md`](data/lore_decks/owner_decisions/2026-11-02_cory_approved_phase6_pilots.md).
Their unmodified source specs and proposal JSON retain their *older*
`UNAPPROVED` labels solely as historical metadata; the later hash-bound owner
receipt governs present acceptance. No list was rebuilt/optimized/changed, and
no live legality, bracket, power or playtesting certificate is implied. Later
revisions require new exact approvals. Verify the overlay with
`python3 scripts/audit_lore_pilot_owner_approvals.py --check`.

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

The Grixis instructions above apply only to explicit Grixis finalization and must never be silently applied to a new lore-deck request. For knowledge queries, use [`LORE_QUERY_QUICKSTART.md`](LORE_QUERY_QUICKSTART.md), `scripts/lore_query.py`, `scripts/mv_ask.py`, and the cited graph, timeline and Q&A tools. [`LORE_DECKBUILDING_READY.md`](LORE_DECKBUILDING_READY.md), `scripts/story_deck_planner.py` and `scripts/evaluate_decklist.py` are available for a **new explicit** deckbuilding request. Separate printed facts, official story claims, contextual links, and creative flavor. An old draft's "awaiting approval" line does not override a later exact owner approval receipt; all ten numbered lore deck specifications and three newly approved historical pilot hashes are protected. No draft becomes approved merely by an engineering merge without an explicit owner record.
