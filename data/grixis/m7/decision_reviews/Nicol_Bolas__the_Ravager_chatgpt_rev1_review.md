# M7 Deck #42 — Nicol Bolas, the Ravager // Nicol Bolas, the Arisen — independent Rev1 proposal

Date: 2026-10-26. **OWNER REVIEW ONLY — NOT APPROVED, NOT LOCKED, NO CANONICAL MUTATION.** Reviewer: ChatGPT. Power Bracket: 4 — Optimized. Archidekt tags: Superfriends / Transform / Proliferate.

## Sources and provenance

- Current canonical approved source: `corymstover/grixis-commander-encyclopediaGPT/refinement/decklists/Nicol_Bolas_the_Ravager_Approved_2026-10-15.txt`, raw SHA-256 `5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e`; canonical current state APPROVED/LOCKED since 2026-10-15, unchanged by this proposal.
- Baseline whole-list audit: `refinement/verification/Nicol_Bolas_the_Ravager_Whole_List_Audit_2026-10-15.md`; 99 noncommander slots then adjudicated and source count/legality confirmed.
- Formal Pass C #42: engineering PR #458 (merged) remains NEEDS TESTING, comparing Aetheric Amplifier / The Eldest Reborn and Savor the Moment / Dreamtide Whale. This M7 proposal adjudicates rather than invents new test outcomes.
- EDHREC commander-specific optimized/proliferate evidence read 2026-10-26; source-bound popularity used only as challenger discovery, not automatic slot authority. Wizards current official Commander banned list reviewed 2026-10-26, Oct12 B&R pertains to Competitive Brawl.
- This candidate source: `data/grixis/m7/candidate_lists/Nicol_Bolas__the_Ravager_chatgpt_rev1.txt`. Exact raw SHA-256 `acfa7922e262805a15932b53b1399acdf6ddf5592c8a3793fafdeec720ad4693`.

## Six 1:1 swaps, all identity-driven

| CUT | ADD | Impact and deliberately accepted cost |
|---|---|---|
| The Eldest Reborn | Aetheric Amplifier | Converts five-mana three-chapter attrition into three-mana any-color rock and reusable {4},{T}, sorcery-speed loyalty doubler. Arisen enters seven loyalty; paying four and tapping an already-untapped Amplifier can raise it to 14, opening -12. Loses Saga edict/discard and reanimation; does not make the ultimate instantly lethal, and the rock cannot also tap for mana in the same turn without untap help. Resolves the prior Pass C high-priority dispute by favoring repeatable commander leverage; no fabricated measured win-rate claim. |
| Nicol Bolas, the Deceiver | Teferi's Talent | A five-mana blue aura puts a loyalty counter on the enchanted planeswalker whenever we draw a card; Arisen's +2 draw two creates two such triggers. Grants a -12 emblem to activate planeswalker loyalty abilities at instant timing on any player's turn subject to normal per-turn limits. Sacrifices an expensive flavorful Bolas walker and adds aura removal exposure; three other Bolas-named planeswalkers plus the Arisen remain. |
| Jaya's Phoenix | Experimental Augury | Five-mana recursively flying planeswalker payoff becomes two-mana instant card selection plus proliferate. Delivers an earlier loyalty boost or emergency countermagic search; loses recurring airborne pressure/blocking. |
| Tinybones, Bauble Burglar | Time Warp | Narrow single-discard payoff becomes a true additional turn with untap, draw, land drop and renewed loyalty activations across the existing walker board. Five mana and vulnerable to counters; distinct from Savor the Moment, which skips untap and was not selected. Loses discard exploitation, but Ravager's ETB discard remains valuable independently. |
| Tergrid, God of Fright // Tergrid's Lantern | Chandra, Torch of Defiance | Five-mana conditional opponent-discard theft becomes a four-mana planeswalker with +1 RR to support seven-mana transform, +1 impulsive card access and -3 creature removal. Sacrifices high-ceiling Tergrid theft when opponents discard permanents; no wheel engine remains to make that ceiling consistent. |
| Liliana's Talent | Vronos, Masked Inquisitor | Replaces five-mana vulnerable planeswalker aura/mass reanimation ultimate with five-mana planeswalker: +1 phases up to two *other* controlled walkers at the next end step, -2 bounces up to one nonland permanent per opponent. Protects the post-transform game against three opponents and adds multiplayer tempo; loses Liliana's mass resurrection route. |

## Commander-first strategy

1. Deploy Ravager on curve at {1}{U}{B}{R}; ETB every opponent discards one. Training Grounds reduces creature-side transform from {4}{U}{B}{R} to {2}{U}{B}{R}, not free and not to the back-face spell.
2. Transform into a new seven-loyalty Arisen. Amplifier / Deepglow Skate / proliferate / Rowan's Talent / Rings of Brighthearth / The Chain Veil escalate actual Arisen loyalty abilities, not generic Grixis turbo-combo lines.
3. Vronos and existing cheap interaction/sweepers shield walkers from multiplayer combat; Time Warp allows untap and another legal loyalty activation turn. Teferi's Talent tracks *each* card drawn to add counters to its enchanted walker.
4. Win through copied repeatable reanimation, damage to enemy planeswalkers/creatures, superfriends advantage, Vraska poison/proliferate pressure, and game-ending Chain Veil engines. Arisen -12 leaves one library card rather than directly killing a player; do not describe it as an immediate win.

## Structural check

- Exact SHA-256: `acfa7922e262805a15932b53b1399acdf6ddf5592c8a3793fafdeec720ad4693`.
- 100 physical cards, 98 printed list rows, 98 distinct names; basic Island x2 and Swamp x2 only repeats; 34 lands, unchanged; no nonbasic singleton violation; commander 1x on first line.
- Six exact named cuts plus six exact additions; no companion; U/B/R color identity, no project exception.
- Historic full approved-list per-name legality/identity evidence from Oct15 and reviewed latest official Commander banned list; all six new cards are existing regular non-banned U/B/R-or-colorless cards, verified by contemporary card texts. **No full fresh Scryfall 100-name live collection query, randomized multiplayer test, or M6 milestone certificate is claimed in this PR.** Those evidence limitations are disclosed for precise ownership certification.

## Challengers evaluated and declined

- Savor the Moment over Dreamtide Whale: despite cheap extra turn, no untap and the loss of Whale's repeated opponent-turn proliferate/7/5 blocker undercut its impact relative to Time Warp; KEEP Whale.
- Contagion Engine over Bolas's Citadel: repeated four-mana double proliferate is thematic, but six-mana deployment plus activation while removing Citadel's high-ceiling card velocity overtaxes the upper curve; KEEP Citadel.
- Silent Arbiter over Liliana's Talent: excellent global one-attacker restriction, but Vronos was chosen for per-opponent bounce, protection of up to two other walkers and synergy with Chain Veil/Talents.
- Blasphemous Act over Damnation, Toxic Deluge or another core slot: strong cheap board wipe, but two existing unconditional sweepers plus Vronos/Chandra/Ripples lower incremental need; retain identity slots.
- Savor, Thrummingbird, Contagion Clasp, Ugin, generic Oracle/Consultation, additional wheel locks: insufficient marginal commander-first power or redundant/off-plan.
- Keep Deepglow Skate, Flux Channeler, Dreamtide Whale, Inexorable Tide, Tekuthal, Ichormoon, Ripples, Sanctum Lurker, Rings, Tezzeret, The Chain Veil, all existing high-synergy Bolas/Teferi planeswalkers except expensive Deceiver, fast mana, and all 34 lands.

## Owner decision gate

This is a **complete proposed replacement**, not authorization to replace the SHA-bound October 15 list. A single Cory reply `Approve` to this exact Rev1 100-card proposal and raw SHA authorizes one versioned canonical approval/merge/post-merge lock, with exact-head source validation and GitHub checks. Preserve the original bytes and all other 61 decks.
