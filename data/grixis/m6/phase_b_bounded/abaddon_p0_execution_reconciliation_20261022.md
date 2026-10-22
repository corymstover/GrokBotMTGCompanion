# Abaddon — P0 real execution reconciliation (PR #547)

**Date:** 2026-10-22. **State:** 20/20 named registered cases executed and passed in exact-head GitHub Actions, **M6.6 still PARTIAL**, 3 mandatory P0 cases unexecuted. Reviewer GPT-6, owner-equivalent non-independent; canonical 62 decks unchanged.

## Grounded runtime receipt

- Actual CI run: https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39743082663
- Exact head at successful run: `de59f5610fcfc7d629b9fbe5d302d79eb2298d37`.
- Runner: `python -m scripts.grixis_m6_abaddon_p0_replay --out "$RUNNER_TEMP/abaddon-m6-p0-actual-replay.json"`.
- Machine-readable actual per-test status and test-file SHA checks: artifact **12409164361**, `abaddon-m6-p0-partial-de59f5610fcfc7d629b9fbe5d302d79eb2298d37`.
- P0 script emitted **20 executed, 20 PASS, 0 FAIL, 3 open, M6.6 not certified**. This is direct runtime output, not an unexecuted catalog count.
- New differential test: `tests/test_m6_abaddon_betrayal_keeper_p0.py` (6 original unit methods). Physically sources the actual alternate 100 with Betrayal and the preferred 100 with Keeper. External opponent card sources are explicit conditional fixtures; neither opponent draw probability nor win-rate is modeled.
- Reconciled named cases and open register: `data/grixis/m6/phase_b_plans/abaddon_p0_case_inventory_20261022.json`. Preregistered six-case plan was committed at `c6d1510207cd23e90e001969998938d0f15fcd0a` before implementation. Test runner fails on missing tests and unapproved changed IDs.
- Full card-name Oracle and official Commander legality across 5 full 100-card lists were re-checked live in the same CI run: **97 distinct identities**, artifact **12409228922**. Canonical TXT SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf` from pinned, connector-fetched authorized exact source bytes, **not** a live CI read of the separate private canonical repository.
- When this receipt file is added, CI must run **again on the final PR head**; only the successful last-head CI authorizes merger. The above earlier run is historic but remains directly verifiable.

## Exactly named unresolved mandatory P0

1. `P0-021` — **Call Forth the Tempest**, printed double cascade plus Abaddon's potentially granted third cascade at MV8; stack/cast-source/reveal-zone sequencing and conditional timing not demonstrated by a dedicated exact physical fixture.
2. `P0-022` — **Inevitable Betrayal suspend**, ordinary 1UU suspension and upkeep time-counter exile-cast timing, relevant to the alternative tested pool; the six executed tests cover cascade casting, not suspend clock.
3. `P0-023` — **Underworld Breach + Lion's Eye Diamond + Brain Freeze**, costs/exile/sacrifice/storm and adversarial timing in a physically conserved backed-up win line. The selected portfolio retains it; no completed exact-source P0 receipt is accepted here.

These are **known/reconciled open obligations**, not proof that no other future rules or Oracle problem can arise. P1 opponent metagame and Chaos Warp replacement frequencies remain explicitly deferred for nonprobabilistic strategic judgment. This 20-case registry is bounded coverage of known commander-critical effects, not exhaustive resolution of every spell in the deck.

## Governance

M6.5 = COMPLETE by formally owner-waived non-independent Pass C. M6.6 and M6.7 = PARTIAL. M6.8 tested-pool I, M6.9 J, M6.10 acceptance = BLOCKED. New M7 owner approvals = 0/62. Engineering branch cannot change the canonical 62 locked/approved decks. **Next executable action: implement P0-021 exact Call Forth phase/stack trace, then P0-022 and P0-023, reconcile qualified case receipts; do not issue I/J certificates beforehand.**
