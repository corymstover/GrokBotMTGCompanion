# Deck #52 — Sol'kanar the Swamp King — M7 Rev1 final owner-review candidate

**Review only; not owner-approved.** Do not merge this PR or change the canonical approval state without Cory's exact SHA approval. Date: 2026-10-27.

- Canonical predecessor: `corymstover/grixis-commander-encyclopediaGPT/refinement/decklists/Solkanar_the_Swamp_King_Approved_2026-10-15.txt`
- Predecessor exact raw SHA: `7d39fff42b91263e83415feef1e69d048c54f8b4e2226b8430fb584076d19106`
- **Proposed six-swap M7 Rev1 raw SHA:** `2bd99c569df4a86897bca0164d2a1fa309b92f8b721e406b8394dfb04b1239e3`
- Exact candidate: `data/grixis/m7/candidate_lists/Sol_kanar_the_Swamp_King_M7_Rev1.txt`

## Commander necessity and rebuilt plan

Sol'kanar is a 5/5 Demon with swampwalk and a triggered gain of one life whenever *any player* casts a black spell (not when Sol'kanar itself is cast). It requires {2}{U}{B}{R}. This list wins from black-spell lifegain conversions, Painter's Servant naming black plus Demon's Horn, global Swamp conversion via Urborg/Blanket, Swamp-mana scaling via Coffers/Crypt Ghast, and its own unblockable combat. The 5MV commander provides a second gain trigger across the entire table and enables Hatred as a command-zone kill; removing him is materially worse despite independent backup engines.

## Six accepted commander-first swaps

| Cut | Add | Why; important downside |
|---|---|---|
| Alhammarret's Archive | Necropotence | 5MV delayed draw/life doubler becomes 3BBB black life-to-cards engine. Commander lifegain replenishes Necro payments. Necro skips draw step, exiles discarded cards, and provides purchased cards only at the next end step; no immediate draws. |
| Underworld Dreams | Orcish Bowmasters | BBB passive draw punishment becomes 1B black flash ETB/extra-draw interruption and scalable Army board. Wheel/Windfall hit many extra-draw events. Lose unconditional 1 life from every ordinary opponent draw. |
| Bontu's Monument | Rowan, Scion of War | Monument discounts only black creature spells and drains on creature casts, weaker in spell-heavy list. BR Rowan translates actual *life lost this turn* via Necro/K'rrik/pain lands/BMC into generic discounts for black/red spells including X drains. Needs untap and sorcery-speed activation; colored pips remain. |
| Bloodletter of Aclazotz | Hatred | Sacrifice turn-only loss multiplier for a black instant that uses Sol'kanar's 5-power swampwalk to deliver 21 commander damage by paying 16 life for +16 power when opponent controls a Swamp. Five mana and 16 life are at risk if target removed/countered; not guaranteed lethal. |
| Dimir Signet | Yawgmoth's Will | Replace persistent UB 2mana fixing with powerful 2B graveyard replay of cheap black spells, rituals, rocks, tutor and protection during one burst turn. Will creates exile replacement; lost UB ramp matters. |
| Talisman of Creativity | Bubbling Muck | Replace off-black UR ramp with one-B spell giving an extra B whenever any player taps a Swamp for mana this turn. 15 natural Swamp-typed land faces and Urborg/Blanket make big Exsanguinate/Torment turns. Temporary, symmetrical, and loses UR rock. |

**Structural:** exact 100 physical; 95 distinct; 1 commander; six Swamps only repeats. 35 front-face lands plus land-backed Fell Mire = 36 land-capable cards. 15 archived Game Changers, accepted in optimized Bracket 4. No project legality exceptions.

## Whole-99 review and final mana decision

The accompanying decision ledger adjudicates all 99 baseline noncommander physical slots: **93 KEEP / 6 CUT**. Compared high-impact challengers and original weak roles across ramp, lands, draw, black spell density, conversion, interaction, removal, tutor loops and Swamp access. Both broad EDHREC Top/High-Lift and archived M6 Pass C findings were treated as candidates, not automatic inclusions.

A seven-swap alternative added Mindcrank over Rakdos Signet for a Bloodchief Ascension combo; **rejected** in final red team. It removed *three* persistent colored 2MV rocks. Among the 99 available card positions, probability of seeing ≥1 of the original seven named 2MV colored sources in first ten is 53.7%, but only 35.1% with four; retaining Rakdos Signet restores five sources (roughly 42%). This does not predict actual games, but it exposes a material early U/B/R-acceleration cost. Mindcrank additionally pulls toward a generic two-piece milling kill. The six-swap variant better preserves casting Sol'kanar with colored pips.

Other researched and **rejected**:
- Well of Lost Dreams over Witch of the Moors: redundant paid-draw package costs repeatable opponent sacrifice plus creature recursion, which already triggers from commander gain events.
- Lake of the Dead over Bojuka Bog: costs Swamp(s) on entry/activation and loses unconditional graveyard exile; evaluated against high B burst.
- Sanguine Bond over Demon's Horn: fifth expensive gain-to-loss converter displaces an independent cheap black-spell gain event.
- Sorin of House Markov: **not Commander-legal in Grixis**: Sorin, Ravenous Neonate back face is white/black color-indicated. Do not treat reminder-text extort as the cause; the back-face indicator is decisive.
- Roaming Throne: expensive colorless four-mana commander-dependent additional trigger; wrong weakest-slot trade.
- Generic Thoracle/Breach cEDH conversion, additional irrelevant opponents' spells, and any move that removes Painter/Grindstone, Witch or typed Swamp infrastructure.

## Source-bound certification and limitations

- Raw candidate independently SHA-256 hashed, structural recount to 100/95, singleton Swamp only, archived identity legality complete on **all 95 distinct names**, no exceptions.
- Source: `data/card_index.csv` blob `c84463e9fa4708165027404dca54af5dcf5774b`, generated from Scryfall Oracle bulk 2026-10-15, with exact 95 Oracle IDs, identities, legality in `data/grixis/m7/oracle_snapshots/Sol_kanar_the_Swamp_King_M7_Rev1_2026-10-15.json`. Targeted official Oracle research checked new effects and a new illegal-card candidate; **not a fresh all-95 live October 27 API sweep**.
- Source-bound interaction checks: Sol and Horn create separate gains on black spell; Painter converts opponent spells; Hatred life paid as cost and swampwalk condition; Necro end-step delay; Rowan generic-only cost reduction and gross life lost; Bubbling Muck symmetric Swamps; Will graveyard-replay/exile timing; Exquisite Blood feedback triggers. No random multiplayer games or numerical win-rate claims.
- Official current Commander ban list and Wizards rules referenced, EDHREC Sol'kanar base/lifegain/optimized compared. Prior engineering comprehensive/reconciliation/formal owner-equivalent Pass C evidence PRs #315, #364, #479 preserve independent historical findings, including Necropotence unresolved prior to this focused M7 choice.
- Existing B4 package of K'rrik, Bolas's Citadel, Top, Aetherflux, Vito, Enduring Tenacity, Starscape Cleric, Marauding Blight-Priest, Exquisite Blood, Bloodthirsty Conqueror, Bloodchief Ascension, Demon's Horn, Painter/Grindstone, Witch of the Moors, Urborg, Blanket, typed Swamps, Cabal Coffers, Crypt Ghast, Gray Merchant, Exsanguinate/Torment, relevant hard counters, Bojuka Bog and Rakdos Charm stays intact.

Owner approval boundary: exact list hash `2bd99c569df4a86897bca0164d2a1fa309b92f8b721e406b8394dfb04b1239e3`. Preserve Oct15 Sol'kanar approved predecessor and other canonical locks. No global M6/M7/M8 milestones inferred.
