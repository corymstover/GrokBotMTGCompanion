# Abaddon — source correction, payoff-preserving alternatives, and bounded decision

**2026-10-22. Authored GPT-6, not a technically independent review. Status: M7 research only, NOT owner-ready.** Supersedes the *current recommendation* in the PR #542 file `Abaddon_the_Despoiler_opportunity_judgment_20261022.md`; retains the original PR #542 evidence unmodified for traceability. Physical comparison manifest is `Abaddon_the_Despoiler_portfolio_v2.json`, fact receipt `Abaddon_the_Despoiler_v2_oracle_erratum.json`.

## Two decision-changing errors in existing narrative

1. **The Lost and the Damned has mana cost {1}{U}{R}, mana value THREE.** Earlier deep review, PR #542 full-slot audit, and PR #542 variant descriptions repeatedly called it *five-mana* and thereby treated its loss as a tolerable high-cost-payoff cut. This is false. Its on-board ability says that whenever **you cast a spell from anywhere other than your hand** or a land you control enters from outside your hand, create a **3/3 red Spawn**. It is a cheap, distinctly Warhammer-engine card. Exact public card record: https://www.mtg.wtf/card/40k/129/The-Lost-and-the-Damned (2026-10-22 checked); canonical October 12 audit includes the same Oracle text. Not all Ignus casts create Spawn: the Ignus *hand* cast doesn't trigger Lost; an actual spell *cast off cascade from exile* does. A cascade hit that is declined, disallowed by Rule of Law/Drannith, or has no valid cast is not a cast and makes no token. A fetchland land entry from the **library** is a separate trigger, not a generic landfall.
2. **Call Forth the Tempest has {5}{R}{R}{R}, mana value EIGHT**, not eleven; and has **no mana-cost reduction** printed. It has *two* separate printed cascades even with Abaddon absent. Hand-casting during your turn with Abaddon gets a *third* if total current-turn opponents' life loss reaches **eight**. It sweeps opponents' creatures for the total mana value of **other spells cast earlier that turn**, including spells cast off its cascades; do not include mere spell copies. Original source: https://mtg.wtf/card/ltc/509/Call-Forth-the-Tempest and its 2023-11-03 card rulings (checked 2026-10-22). At eight mana, it remains a substantial top-end risk, but it is materially more realistically castable than the previously claimed MV11. Preserve it in the corrected research variants. Do not interpret an invalid earlier MV11 analysis as a sound cut criterion.

These are **material Oracle corrections**, not a claim that a new Scryfall all-100 card refresh ran, or that the existing sealed original reviews must be rewritten. Prior older review documents are provenance, *not current M7 factual authority* where contradicted.

## Corrected whole-deck direction

Abaddon needs same-turn life loss before a hand cast to gain cascade; subsequent exile casts build Spawn and other Warhammer engines. The now-corrected **three-mana Lost** and **eight-mana printed double-cascade Call Forth** jointly argue for *preserving*, not sacrificing, those two unique cards while strengthening the hand-cast engine and ability to answer hostile permanents.

The competitive incumbent to beat is still **100 physical cards** with 34 lands, 94 distinct names; current canon SHA `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`. Opponent life loss includes loss beyond damage. Ignus can be recast with source-paid Birgi but only on a quiet sorcery-speed mana-ability window; with Abaddon and X >= 3, *each Ignus spell actually cast from hand* qualifies for cascade. It has MV3, so a cascade from Ignus can only find a card of MV **strictly less than three**. Every correctly cast nonhand hit can trigger Lost, but triggers and storm copies are not themselves casts. Limits include colored red access, a finite physical library, turn priority, removal of Birgi/Abaddon, Rule of Law, Drannith, and tax/disruption. No real win-rate or matchup percentage inferred.

### Four exact 100-card research portfolios

| Variant | Adds | Exact cuts | Strategic opportunity |
| --- | --- | --- | --- |
| **V2 engine-only** | Ignus | Rakdos | Retains 3-MV Lost, 8-MV Call, 6-MV Keeper and the zero-MV Betrayal hit, but leaves the resolved nonblue-permanent answer gap |
| **V2 engine + Warp for Keeper — provisional lead** | Ignus; Chaos Warp | Rakdos; Keeper of Secrets | Gains combo/cascade and instant answer while keeping the most efficient exile Spawn payoff; loses Keeper's six-mana Warhammer damage-from-nonhand-casts finisher and haste body, an actual damage conversion cost |
| **V2 engine + Warp for Betrayal** | Ignus; Chaos Warp | Rakdos; Inevitable Betrayal | Keeps Keeper finish but trades an especially good MV0 cascade hit that steals a creature from an opponent's library; weaker low-MV cascade target pool and reduced free-value potential |
| **V2 combat + Warp for Keeper** | Aggravated Assault; Chaos Warp | Rakdos; Keeper of Secrets | With Neheb and Loyal, has a finite conditional extra-combat drain finish, but is less directly linked to Abaddon's hand-cast cascade and can be crippled by removing Neheb or the lieutenant |

All exact lists are in this directory as `Abaddon_the_Despoiler_v2_<variant>.txt`. They all retain The Lost and the Damned, Call Forth, The Ruinous Powers, Birgi, Neheb and Loyal Subordinate, keep 34 original lands, and leave the approved source untouched. Their physical add/cut and singleton properties are executable checks, **not** comprehensive Oracle approvals.

### Candidate dispositions after source correction (research only)

- **Grinning Ignus: provisional SELECT** versus Rakdos's restricted BBRR four-drop creature-only discounts. In a spell-first deck, additional on-commander hand casts and cascade access create a role Rakdos does not, but Birgi is a fragile prerequisite for no-net-red repeats. This is qualitative, not a proven increase in win rate.
- **Chaos Warp: provisional SELECT** when substituting six-mana Keeper, **not** three-mana Lost. Removal of resolved Rule of Law / Rest in Peace / nonblue enchantment remains uniquely useful, although Chaos Warp can reveal a replacement permanent and Rule of Law can prevent casting it later in that turn. At full multiplayer tables the high-curve Keeper's target-opponent damage is a real late-game finisher. The comparative choice can reverse under midrange games where Keeper survives and converts MV4–8 nonhand casts into lethal damage.
- **Aggravated Assault: RETAIN_ALTERNATIVE**, not "HOLD equals KEEP". Pays `{3}{R}{R}` during a main phase, requires source-generated Neheb mana from opponent life lost in postcombat main; with ≥5 loss it can enable repeat combat/main phases, but requires separate damage/drain output to win. Retaining Lost improves later spell chains regardless of whether this combo assembles.
- **Inevitable Betrayal: protect unless a package advantage compensates.** Zero-mana-value suspend spell is a premium legal free cascade hit, and may provide a creature swing; cutting it is a real cascade-density loss.
- **The Lost and the Damned and Call Forth the Tempest: RETAIN.** Both are original approved core and were incorrectly characterized in the previous analysis. New facts support retention; they are not newly added candidate cards.

### Adversarial decision tests left open (no simulation treadmill)

1. Against a control/hate pod, is one `Chaos Warp` more practical as a postresolution answer than six-MV Keeper's damage output under the same mana and priority windows? Estimate via actual source/Oracle-targeted deterministic cases before any bounded gameplay modeling; also weigh the chance Warp replaces a threat.
2. Under creature removal, can Ignus/Abaddon repeat when Birgi trigger remains on the stack or Birgi dies? Existing PR #528 fixtures cover multiple cases. Don't rerun them just to find a favourable result.
3. Does three-MV Lost make nonhand cascading reliably convert into tokens in the relevant real states? It creates **zero tokens** when no free spell is actually cast. Retain precise distinction in regression tests.
4. Are the existing counterspell hit odds and zero-MV suspend access more costly to lose than Keeper's six-MV recurring damage? If changing the selected cut, compare physical complete lists, *not isolated extra cards*.

**Gate boundary:** This is *not* an M7 final packet. Full current Oracle/legality of all 100, effect-aware missing mandatory P0, original/source+challenger cryptographic hashes, M6.8 I and M6.9 J receipts, and final exact owner approval are still open. Bracket 4 unchanged. The owner-authorized 62/62 non-independent Pass C waiver remains accurate, technically independent reviews 0/62.
