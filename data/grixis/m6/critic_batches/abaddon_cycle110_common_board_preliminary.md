# Cycle 110 — Abaddon three-slot common-board reconciliation: preliminary critique

**Status:** engineering author review only. Not formal independent Pass C/I/J, balanced end-to-end Phase B, a zero-improvement certificate, approved swap, or M6 acceptance.

## Source authority and precise method

- Preregistered Cycle 110 scope: data/grixis/m6/phase_b_plans/abaddon_common_board_01.json, committed first at d7bfc1f68be4b23ac994dd67fb33fe7faaaf3138.
- Derived full matched receipts: data/grixis/m6/phase_b_bounded/abaddon_common_board_01.json; reproducible summary: data/grixis/m6/phase_b_bounded/abaddon_common_board_summary_01.json.
- Same original 240 source seeds and 7-card opening hands except exact physically replaced Blast slot, approved 100-card deck raw SHA256 2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf.
- One common external opposing abilityless 3/3 and opponent life [40,39,31] at initial state for all three variants. This is NOT an actual 100-card opponent deck.
- The ledger reconciles accepted Cycle106 candidate access and conditional activation branches with Cycle107/109 actual original Blast cascade/resolution experiments. This does NOT independently re-simulate a full shared opponent-game timeline for all three variants. Post-cascade tutor/library changes may alter later draws.
- Source removal of candidates and target removal from Blast are DIFFERENT stress tests, not interchangeable resource investments by opponents; neither response frequencies nor matching legal opposing spells are modeled.

## Registered, conditional outcomes over 240 paired seeds

| Observation | Bituminous Blast | Heartless Hidetsugu | Tree of Perdition |
|---|---:|---:|---:|
| Slot actually cast with real supported mana | 7 | 7 | 19 |
| Tap ability hypothetically resolves on later turn with no response | N/A | 4 | 16 |
| Opposing 3/3 removed by the tested card | 7 | 0 | 0 |
| Physically resolved cascade-from-exile hit spells | 4 | N/A | N/A |
| Unresolved-but-offered cascade hits | 3 | N/A | N/A |
| Sum of conditional opponent life lost in tap branches | N/A | 216 | 432 |
| Sum of conditional pilot tap self-damage | N/A | 65 | 0 |
| Abaddon present at hypothetical tap activation | N/A | 4 | 4 |
| Source-payable Boltwave/Flame Rift in actual hand after conditional tap | N/A | 0 | 0 |

The 216 / 432 / 65 sums are outcomes *only if* a rare source-paid cast was followed by an unimpeded next-turn activation in that scripted branch. They are not observed actual losses from 240 realistic Commander games, nor equivalent utility scores. The baseline 3/3 removal and four genuinely resolved artifact/tutor cascade effects also have no independently valued payoff. The five generated colorless mana was unspent in modeled follow-up and the two Mana Vault upkeep events per policy remain unresolved. Unmodeled effects are unknown, never zero.

## Limits of comparison

- The initial board is held constant, but the tests do NOT have identical actual stack interaction, threat responses, four-player full board states, combat, mulligans, win conditions, legal followup across 99 cards, tutor-choice optimization, survival probabilities, or opponent-resource costs.
- Bituminous Blast's 3/3 removal is NOT numerically interchangeable with Heartless's player damage or Tree's opponent life exchange. A large Abaddon life-loss threshold is not equivalent to successfully casting valuable hand spells with cascading effects.
- The Abaddon commander-first engine remains underrepresented because the source plays almost no nonland cards except the tested slot and commander; candidate follow-up is limited to two spells, while other hand effects are unsupported.
- Exact original seed and 100-card pilot physical conservation, source hashes, and role receipts are defensible. Relative deck-power outcome remains CANNOT_EVALUATE, not improvement, tie, or tested-pool zero-improvement.

## Recommended project-level next work

Do not keep indefinitely expanding one Abaddon effect per engineering cycle. Commission a truly independent skeptical reviewer for this Abaddon hold judgment and begin commander-by-commander first-pass candidate reconciliation across all 62 source blueprints and verified approved lists. Only reopen costly full opponent-play modeling for a bounded pilot with a preregistered payoff objective, genuine opponent-response budget, measurable confidence, and a clear decision threshold.

**Decision:** preserve approved Bituminous Blast and all 62 canonically locked decks. No card swap, tested-pool certificate, Phase B/Pass C/I/J, or M6 acceptance issued.
