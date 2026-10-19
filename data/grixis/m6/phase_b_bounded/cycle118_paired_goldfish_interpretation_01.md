# Cycle 118 — Read-only source-locked paired goldfish evidence and limits

**Status:** 288 paired shuffles completed (96 per approved-deck vs one-card variant); 576 goldfish branches. Archived frozen Scryfall Oracle checksum verified. **This is NOT Phase B, a multiplayer game outcome, a final swap recommendation, or an independent Pass C review.**

## Experiment preregistration and evidence
- Registered before execution: `data/grixis/m6/phase_b_plans/cycle118_supported_paired_goldfish_preregistered_01.json`, commit `3fb1cb6f2c4e0d59008610094db01d7137ec69de`.
- Restricted-mana correction preregistered before execution: `data/grixis/m6/phase_b_plans/cycle118_simulator_coverage_guard_01.json`, commit `4d5555d0f7f6e0f9b5ec7919a8aefd485921a84e`.
- Exact reproducible GitHub Actions: [run 39188319574](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39188319574), commit `13be583758f1b20c6c36d5f55d816a2d2c0a9f2f`. The original run [39188205528](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39188205528) failed deterministic replay because a cross-process Python hash iteration seed was unpinned. Pinning `PYTHONHASHSEED=0` resolved the discrepancy and the second run passed both receipt build/check.
- Persisted GitHub Actions receipt: artifact `cycle118-source-locked-288-paired-goldfish-receipt`, ID `12158863317`; generated JSON `cycle118_supported_paired_goldfish_01.json`.

## Recorded pairs and development-only measurements

| Deck | Approved-list cut => candidate | Mana spent T1–T6 challenger − baseline (paired 95% CI) | Commander cast by T4 challenger − baseline (paired 95% CI) |
| --- | --- | --- | --- |
| Gwendlyn Di Corci | Opposition Agent => Aphetto Alchemist | +0.05208 [−0.02671, +0.13088] | 0 [0, 0] |
| Nicol Bolas, the Ravager | Mox Diamond => Aetheric Amplifier | +0.07292 [−0.30468, +0.45052] | +0.01042 [−0.01000, +0.03083] |
| Mai and Zuko | An Offer You Can't Refuse => The Enigma Jewel // Locus of Enlightenment | 0 [0, 0] | 0 [0, 0] |

No paired difference in the chosen M3 development proxies establishes an improvement. A zero result for the Jewel case especially says **nothing** about its activated-ability synergy; the relevant upside and counterspell loss are not supported by M3 v1.1.

## Modeling defect found and bounded
The existing `grixis_sim` v1.1 `source_spec()` falsely interprets The Enigma Jewel's {C}{C} **activation-only** mana as generic unrestricted permanent mana; the base `resolve()` treats nonland permanents as untapped. Both are incompatible with the card's front-face Oracle. The experiment **does not change the accepted simulator**: it neutralizes the Jewel card model as an inert castable artifact with no mana production and a tapped flag, and explicitly marks the real spell/activated-ability/flash value as unsupported. This is a conservative limitation, not a fix to the general simulator.

Gwendlyn's own-turn tap ability, Alchemist untap, the shroud issue and tutor disruption by Opposition Agent were **not** dynamically simulated. Nicol Bolas's transformation or planeswalker loyalty doubling were **not** dynamically simulated. Mai and Zuko's Firebending/flash, Jewel craft and activated-mana engine, and An Offer stack counters were **not** dynamically simulated. Prior local scripted six fixtures remain separate evidence, not full 99-card effect-aware trials.

## No new strategic certification
- Author HOLDs remain provisional; three promising candidates remain **unresolved**, with a need for genuinely independent source critique.
- Six Cycle117 effect-aware paired scenario types remain **unexecuted by a real turn/rules/opponent engine**.
- No current-date full-deck legality check, no M6 completion, no M8 certificate, no owner-approved swap.
- All 62 canonical records remain approved/locked with the same source hashes; zero decklist or exception changes from Cycle118.

**M6 next gate:** Scope *true effect-aware* tests to game states supported by real card effect execution (priority, tapped entry, mana-use restriction, commander interactions, opponent responses), then solicit reviewer independent from the original authored judgments. Do not extrapolate M3 goldfish to multiplayer win rates.
