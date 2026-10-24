# Anhelo, the Painter — ChatGPT independent M7 challenge #1 (2026-10-23)

**Status:** RESEARCH IN PROGRESS; **GrokBot five-swap candidate is NOT owner-ready and not approved**. This note preserves the independent second-pass discoveries and rejection/verification requirements; no canonical deck mutation authorized or performed. PR #652 head at intake: `a6798cf2ae19d39f7fc45726d2bc23e5fcb05a3a`.

## Verified source and initial source-bound recount

- Canonical 2026-10-13 approved-source file `refinement/decklists/Anhelo_the_Painter_Approval_Ready_2026-10-13.txt` is frozen, historical registry raw digest `d19d94b8a96fb27a760c7b7d9181221f74bd61642d1d1dd7644fc1c59c09839e` differs from physical raw `8d5f8a9bd4fcdcd164aab63150c14dc69a814a4d9fd764876de3214d3adf9972`. Keep both; do not fix silently.
- Scryfall-source quantity recount: original 100, **34 physical front-face lands and 9 two-mana/one-mana rocks**; Grok candidate 100, 33 front-face lands and 6 rocks. `Primal Amulet // Primal Wellspring` is front-face **Artifact**, not a present 35th land.
- Grok's cited probability of ≥3 static sources by top 9 falls `0.839→0.768`, and by top 8 `0.762→0.680`. This roughly 7–8.2 percentage point curve-time loss is material for a three-color {U}{B}{R} commander, a five-mana Reiterate/Geyser package, X finishers and copying on opponents' turns.
- `Fellwar Stone` is often colored fixing in multiplayer; calling it categorically unreliable because of opponent-land dependency is insufficient. The three original Talismans provide **untapped self-sufficient colored mana**, unlike Signets requiring a second input. Their color pairs overlapping Signets is not redundancy in timing/function.
- `Bedevil` requires **{B}{B}{R}**, a significant colored-load increase while candidate simultaneously removes two black-producing Talismans and Exotic Orchard. Grok's `Feed the Swarm` cut also eliminates the clean targeted enchantment answer. `Chaos Warp` is randomized replacement and `Cyclonic Rift` temporary bounce, not functionally identical. Challenge this cut; retain Feed in comparison builds.

## Newly identified off-ranking challenger — Forsaken Miner (high-priority P0)

`Forsaken Miner` costs **{B}**, is a **2/2**, can't block. From the graveyard, when you commit a crime you may pay **{B}** to return it **directly to battlefield**. Official Wizards Outlaws of Thunder Junction release notes expressly state that if a spell's **additional cost sacrifices Forsaken Miner**, its return ability still triggers **if that spell commits a crime**. This directly matches Anhelo's granted `casualty 2` additional sacrifice cost, provided the original spell targets an opponent, their permanent, spell, ability, or card in their graveyard. It can return on the *same spell cast*, even on an opponent's turn, for `{B}` and without spending another creature spell cast or waiting for landfall. This is qualitatively different from `Skyclave Shade` (own-turn landfall recast only), `Tenacious Underdog` (four-mana, two-life blitz after death), or `Sinister Concierge` (three upkeeps delayed).

**Primary source:** https://magic.wizards.com/en/news/feature/outlaws-of-thunder-junction-release-notes (Forsaken Miner card and two explicit rulings, passage around lines 891–901; crime timing rules around lines 151–173).

Needed P0 tests: (1) Anhelo on battlefield, Miner present, target opposing creature with `Bedevil` or `Chaos Warp`, pay casualty by sacrificing Miner, crime committed after additional cost, pay {B} and return Miner; (2) same first spell with a **non-targeting** spell such as `Frantic Search`, no crime and no Miner return; (3) graveyard-only ability, legal zone/timing, target and ability trigger order; (4) other-turn opponent targeting case; (5) graveyard hate response windows. **Do not assert every casualty spell recurs Miner**.

## Newly identified off-ranking challenger — Case of the Stashed Skeleton (high-priority P0)

For **{1}{B}**, this enchantment creates a **2/1 suspected Skeleton** (menace, can't block): valid pre-existing Anhelo casualty fodder. After the token is sacrificed and no suspected Skeletons remain under our control, the Case solves at the beginning of *our* end step; its solved activated ability then permits paying **{1}{B}**, sacrificing Case and searching for **any card** at **sorcery speed**. Thus a naturally commander-fueled 2/1 body becomes a delayed, paid universal tutor, not simply generic tutor goodstuff. Four total mana spread over turns; timing/only-one-body/condition are real costs. Compare to `Dogged Detective`, `Sinister Concierge` and expensive duplicate recursion engines before adding.

Oracle: https://scryfall.com/card/pmkm/80s/case-of-the-stashed-skeleton; Wizards case rules: https://magic.wizards.com/en/news/feature/murders-at-karlov-manor-release-notes. P0 test: casualty token sacrifice, solve at own end step, activate only after solved at sorcery timing and pay both additional costs; no immediate tutor during casualty resolution.

## Off-ranking engine contender — Fable of the Mirror-Breaker (high priority)

For **{2}{R}**, Saga chapter I creates an immediate **2/2** mana-Treasure-on-attack Shaman, chapter II rummages up to two cards, and transformed `Reflection of Kiki-Jiki` is itself a **2/2**, can pay {1}, tap to create a hasty token copy of another nonlegendary creature for Anhelo's casualty. It produces commander-legal bodies **without consuming a nonland mana source slot** and filters combo draws. Note three-turn transformation delay, token expiry and Reflection summoning sickness. Compare to `Primal Amulet`, `Maestros Ascendancy`, `Deekah` and other expensive setup cards with full 100-card alternatives.

**Primary source:** https://magic.wizards.com/en/news/feature/kamigawa-neon-dynasty-release-notes-2022-02-09 (official exact printed mechanics).

## Additional challenger — Deadly Dispute (research only)

Instant **{1}{B}**, additionally sacrifice artifact/creature, draw two and create Treasure; with Anhelo can copy the draw-and-Treasure effects when also sacrificing power-2+ casualty fodder. Multiple additional sacrifice costs may require **two separate resources**, unless Dispute's cost sacrifices a Treasure and casualty another creature. Not yet selected; compare extra-sacrifice burden against `Big Score`, `Startle`, and any non-core draw spell. Must source-bind Oracle and test the two cost payments independently.

## Research decision boundary before final candidate

1. Preserve baseline's enchantment-answer role, and test 34-land/8–9-rock, 34-land/7-rock and Grok's 33/6 full-100 candidate configurations, not just match its five swap count.
2. Individually test `Forsaken Miner`, `Case`, `Fable` (plus any further challengers) against **actual weaker incumbent roles** instead of automatically cutting 4 mana sources.
3. Specifically compare `Tenacious Underdog`'s four-mana/graveyard-life engine with `Forsaken Miner`'s one-black interaction-based return. Test `Skyclave Shade` landfall, `Dogged Detective` opponent second draw and `Sinister Concierge` delayed suspend on actual opponent-turn casualty patterns.
4. Preserve combo core: `Twinflame`/`Dualcaster Mage`, `Reiterate` + `Mana Geyser`, `Twinning Staff`, `Narset's Reversal`, `Underworld Breach`, `Storm-Kiln Artist`, `Ral, Storm Conduit` and useful 2/2 token generators.
5. Recheck exact 100, singleton, live Scryfall Oracle/UBR/official legality (esp. new challenger names), cash/colored payment, bounded board-state tests and raw SHA. No fictitious win rate or complete M6 I/J certificate inferred from the old Grok candidate.
6. Five is **minimum presentation floor only**. Explore 6/7/8+ quality-positive changes, but do not pad. Present to Cory only a fully checked exact 100-card best candidate and explicit approval request.

**Decision as of this note:** Hold Grok #652 preferred list as **RESEARCH ONLY**, not final; material overlooked on-theme cards and mana/enchantment coverage require reassessment. No approval for Anhelo M7 implied.
