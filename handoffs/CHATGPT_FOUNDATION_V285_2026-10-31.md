# Foundation continuation handoff — v2.85 (2026-10-31)

## Verified live state after publishing

Read live GitHub main, not this handoff as a substitute. The v2.85 bounded
change was merged via [PR #954](https://github.com/corymstover/GrokBotMTGCompanion/pull/954)
on 2026-10-31 at `33a8c2d312b0e225960810d1267ed4782b5eb2a9`.
Its **22/22 exact-head PR checks and 10/10 post-merge checks all passed**.
The Master Workflow and tracker remain **89/137 checked, 48 open,
NOT_RELEASE_READY**. It introduces no new canon claims, dates or Grixis
changes; the 62 protected deck paths are absent from the PR diff.

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
- The first PR CI run detected a stale foundation Q&A-packet expectation
  (`VERIFIED` → `QUALIFIED`) and shifted task-line metadata in the 137-item
  triage. The packet/generator were updated, and the workflow addendum was
  moved after the checklist so its recorded task lines remain unchanged.
  The corrected exact-head run must verify both generated artifacts.
- See `research/PHASE7_COMMANDER_QA_CURRENTNESS_2026-10-31.md` for the exact
  failure mode, test coverage and limitations.

## Next priorities

1. Independently investigate hard two-card/game-state interactions and other
   currentness risks in card, rule and set lookups using current official
   sources; do not mark the broad Phase 7 integration task finished on this
   one bounded fix.
2. Expand source-quoted Amonkhet/War of the Spark, Thran/Weatherlight and
   Phyrexia histories with strictly supported cross-strand links.
3. Resolve documented graph, plane and printing categories only where primary
   evidence supports it. Reconcile pinned Scryfall bulks by their original
   hashes; owner release decisions and final certification remain hard gates.

**Foundation first:** no new decks, no pilot approvals, no Grixis modifications.
Maintain **89/137 checked, 48 open, NOT_RELEASE_READY** unless new evidence
actually closes a separate checklist item.
