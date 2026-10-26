# Deck #41 — Nicol Bolas — M7 Rev1 approved candidate

Date: 2026-10-26. Status: OWNER APPROVED for exact M7 Rev1 SHA-256 a6079935a50b9469ca487e58e6bac159f8b777348b31585256b967f92c5d0df6. User replied **Approve** directly to the complete 100-card Archidekt-ready proposal after the verified 10 swaps were presented. This approval authorizes canonical replacement through a versioned PR, preserving the October 15 approved artifact.

Baseline authority: corymstover/grixis-commander-encyclopediaGPT/refinement/decklists/Nicol_Bolas_Approved_2026-10-15.txt; original raw SHA-256 e47fdd5c31dce2d5b05e8fa8c217fe94caa16ef150057f98748254fc3c841617.

Proposed artifact: data/grixis/m7/candidate_lists/Nicol_Bolas_chatgpt_rev1.txt; candidate raw SHA-256 a6079935a50b9469ca487e58e6bac159f8b777348b31585256b967f92c5d0df6 (exact bytes verified by SHA-bound GitHub Actions).

Scope: 10 exact 1:1 swaps, commander unchanged; 100 cards, 99 distinct card names, Island x2 only repeat, 37 lands, Grixis-only identity, no deliberate exception. Power Bracket 4 — Optimized. Archidekt tags Discard / Commander Damage / Control.

## Swaps

| Cut | Add | Strategy |
|---|---|---|
| Hypnotic Specter | Sarkhan, Soul Aflame | Dragon cost reduction and distinctly named Nicol copy when Dragon enters; own next upkeep avoids Nicol copy upkeep tax because copy lasts until end of turn. |
| Nightscape Familiar | Rivaz of the Claw | Dedicated two-color mana for Nicol Dragon spells; recast Nicol from graveyard if voluntarily left there after dying, with exile-on-dying granted to returned creature. |
| Oppression | Imperial Seal | Remove symmetric discard tax impeding our 8-mana setup; cheaply find Dragon Tempest, Ingris, or attack/ETB enabler. |
| Raiders' Wake | Ophidian Eye | Multiple draw triggers from Nicol dealing damage to multiple opponents; flash permits protection and timing flexibility; opponent life-loss payoff decreased. |
| No Mercy | Mithril Coat | Flash indestructible attachment to Nicol or another legend; shields commander against destroy-based effects and combat damage, but not exile, sacrifice or commander upkeep tax. |
| The Eldest Reborn | Reanimate | One-mana reanimation of Nicol if intentionally in graveyard, or another discarded creature; flexible lower-curve route, losing slower flavor saga. |
| Seething Song | Coalition Relic | Repeatable any-color acceleration and stored second color for hard UUBBRR + continuing UBR upkeep. |
| Shizo, Death's Storehouse | Minamo, School at Water's Edge | Untap Nicol for Quicksilver Dagger pings, and Rivaz to add more dragon mana; land changes B to U, loses fear evasion. |
| Bojuka Bog | Plaza of Heroes | Untapped commander-specific colored mana and legend protection; sacrifices graveyard-hate effect; track as meta risk. |
| Viridian Longbow | Dream Halls | Turn-five color-matching discard to cast an eight-mana Grixis commander from command zone; highly explosive, but symmetrical and potentially helps opposing interaction. Extra commander tax still applies. |

## Critical constraints / risks

- Original Nicol Bolas: whenever he deals damage to an opponent **for any reason**, that opponent discards their entire hand; not restricted to combat damage.
- Dragon Tempest / Ingris Stingerquill / Kediss / Chandra's Ignition / Pain for All / Quicksilver Dagger still make Bolas himself a damage source in their respective interactions.
- Sarkhan copies original Bolas except its own name; Sarkhan remains legendary, but the legend rule does not force an immediate sacrifice because the names differ. If Sarkhan entered that turn, copying does not grant haste.
- Dream Halls does not automatically protect the commander or pay commander tax/upkeep. Opponents can also cast spells with its replacement cost, so deployment timing matters.
- Plaza of Heroes's any-color restriction for a legendary spell applies when casting Bolas, but not necessarily to the upkeep payment unless its third mana mode can use the colors of a legend currently controlled.
- Reanimate doesn't reach the command zone; a dying Bolas must remain in its graveyard, not move to the command zone, for the line to work.
- Combo: Aggravated Assault + Sword of Feast and Famine still requires an equipped creature to deal combat damage to an opponent and enough untapped lands to generate five mana for the next Assault activation.
- Whole-deck 2026-10-15 Oracle/legality audit is baseline evidence. The 10 additions were separately publicly researched 2026-10-26, but a complete fresh per-name Scryfall check / engineering CI remains a certification gate before declaring approval-ready PASS.
- Historic approvals and frozen exports are NOT modified by this proposal.

Owner approval recorded once: **Approve**, October 26, 2026. No second approval is needed. Engineering GitHub Actions run 40411457402 completed SUCCESS at head e9855de13d49dad8ff01012cb3240e440e395548: 7/7 finite checks, live Scryfall 99/99 Commander legality and UBR identity, 14 Oracle witnesses PASS. Keep the historical October 15 artifact and lock only the verified Rev1 list; do not alter other locked decks.
