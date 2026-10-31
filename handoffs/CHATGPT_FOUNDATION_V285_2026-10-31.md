# Foundation continuation handoff — v2.85 (2026-10-31)

## Exact starting point

Read live GitHub main, not this handoff as a substitute. v2.84 was merged via
PR #953 at `c4041ec97ad06794e81d99776136e788b9a5fb8a`; its Master Workflow
and tracker were **89/137 checked, 48 open, NOT_RELEASE_READY**. The v2.85
bounded change protects Phase 7 Commander-answer confidence and invalid deck
configurations. It introduces no new canon claims, dates or Grixis changes.

## v2.85 implementation

- `scripts/commander_rules.py` checks the proposed leader(s) and partner
  mechanic before giving a candidate-card inclusion verdict. Invalid commander
  configurations return `allowed: false` and an explicit reason; empty and
  excessive leader lists do not produce false positive answers.
- Commander/inclusion answers using historical Scryfall card-shard legality
  and the dated 2026-09-25 CR excerpt are always `QUALIFIED` with
  `DATED_SCRYFALL_LEGALITY_NOT_LIVE` and a source date, rather than mistakenly
  claiming present-tense live legality.
- Four adversarial synthetic-fixture tests passed locally and were wired to
  `.github/workflows/phase7-companion-ask.yml`. The full real-card suite is
  a **GitHub CI gate**, not claimed to have been run in the local sparse clone.
- See `research/PHASE7_COMMANDER_QA_CURRENTNESS_2026-10-31.md` for the exact
  failure mode, test coverage and limitations.

## Next priorities

1. Verify v2.85 exact-head GitHub Actions and merge only after required checks.
2. Independently investigate hard two-card/game-state interactions and other
   currentness risks in card, rule and set lookups using current official
   sources; do not mark the broad Phase 7 integration task finished on this
   one bounded fix.
3. Expand source-quoted Amonkhet/War of the Spark, Thran/Weatherlight and
   Phyrexia histories with strictly supported cross-strand links.
4. Resolve documented graph, plane and printing categories only where primary
   evidence supports it. Reconcile pinned Scryfall bulks by their original
   hashes; owner release decisions and final certification remain hard gates.

**Foundation first:** no new decks, no pilot approvals, no Grixis modifications.
Maintain **89/137 checked, 48 open, NOT_RELEASE_READY** unless new evidence
actually closes a separate checklist item.
