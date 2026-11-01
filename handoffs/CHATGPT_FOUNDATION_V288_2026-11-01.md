# ChatGPT foundation handoff — v2.88 (2026-11-01)

## Verified starting point

- Remote `main` before this batch: `8954af942dadfa70b5087f2e3393d1fb6ad37fab` (merged v2.87 PR #957).
- Master Workflow v2.88 retains **137 numbered tasks, 89 checked, 48 open** and **`NOT_RELEASE_READY`**. The owner has conditionally accepted a foundation-only package, not yet eligible to execute.
- Preserve **62 approved Grixis decks**, historical snapshot locks and three parked pilots. Do **not** begin Phase 6 deckbuilding before foundation gates and the owner's release process.

## This batch — Phase 7 three-domain Q&A

- `mv_ask` now recognizes bounded questions about an exact card, a named lore subject and Commander eligibility together. Card facts resolve from the indexed Scryfall shard, eligibility from the dated Commander rule gate, and subject histories from exact-Oracle-UUID graph anchors with explicit `names_entity` edges.
- The graph name edge is **navigation only**: the answer never turns a card title into evidence that its art depicts a specific event. Duplicate graph Oracle anchors fail closed; absent named subjects stay absent.
- **Ugin, the Spirit Dragon** demonstrates a crucial distinction: format `legal` is not commander designation eligibility for a planeswalker without an exception. The unique `Nicol Bolas, the Ravager` front face resolves to its double-faced Oracle entry and reports disputed history instead of flattening grades. **Blackblade Reforged** does not acquire a fabricated named person.
- Every joined answer is `QUALIFIED`, distinguishes the archived Scryfall legality date (2026-10-15) from the official CR date (2026-09-25), caps claims at eight per subject, reports total/omitted counts and includes cited sampled claims. No live ban assertions, simulated interactions or deck recommendations.
- Six focused adversarial tests, Phase 7 CI route checks, and four additional acceptance Q&A cases bring the deterministic foundation packet to **83 representative cases, NOT CERTIFIED**.
- Evidence: `research/PHASE7_CARD_LORE_COMMANDER_EVIDENCE_2026-11-01.md`; generated packet: `research/FOUNDATION_ACCEPTANCE_PACKET_2026-10-30.md`.

## Remaining blockers and next work

- The broader Phase 7 integrated-research and difficult-Q&A boxes remain **open**; this is a bounded three-domain slice, not an unqualified completion claim. Live Oracle/ban freshness, broad source coverage, release quality and owner gates are pending.
- Re-run exact-head GitHub CI for the published PR and post-merge `main` before calling the batch complete. Continue sourced foundation work next, including unresolved chronology and source-grade lore gaps. Do not change approved deck collections or begin parked pilots.
