# ChatGPT foundation handoff — v2.92 (2026-11-01)

## Verified baseline

- Remote GitHub `main` before this batch: merge commit `3a1dde6b03671c77153007108358b4e575a37679` ([PR #961](https://github.com/corymstover/GrokBotMTGCompanion/pull/961)), with **23/23 exact-head** and **10/10 post-merge** checks green.
- Master Workflow v2.91: **93/137 checked, 44 open**, release not ready. Continue foundation-first policy and preserve the approved 62 Grixis decks; Phase 6 and its three unapproved pilots remain parked.

## v2.92 work

- Wrote deterministic, read-only `scripts/audit_entity_coverage.py` against the current registered graph, covering **839** World/Character/Faction/Object/Region nodes across five explicit types. All direct relationships require a registered Wizards source URL and valid grade; origins and card-name bridges do not count as story proof.
- Published a full per-entity JSON listing, human gap report and honest source-review priority: **4** registered nodes without a direct cited claim; **139** with only qualified direct claims. The priority order is *graph degree*, never a claim of actual canon importance.
- Added five tests for exact type totals, source citation integrity, no fabricated missing source, deterministic report and release/deckbuilding holds. Wired read-only build check into Phase 8 CI.
- Marked **K102** complete as an **audit of the registered corpus**, not an exhaustive census of all Magic canon or completion of biographies, cross-plane history or source gaps. Master Workflow v2.92 and current triage: **94 checked, 43 open** (26 under review, 17 blocked); `NOT_RELEASE_READY`.
- Evidence: `research/ENTITY_COVERAGE_AUDIT_2026-11-01.md`, `data/lore_research/entity_coverage_audit_2026-11-01.json`.

## Next actions and hard gates

- Rebuild the entity audit and full triage, re-check release evidence, run targeted local tests, exact-head GitHub CI, merge and post-merge verification. Do not call this integrated merely because local checks pass.
- Use source-poor entity IDs and the other open checklist items for further first-party story research, resolved chronology, and live Scryfall/CR verification. Owner foundation acceptance is conditional on the still-unpassed gates, never on a raw percentage. Leave 62 locked decks and three parked pilots unchanged.
