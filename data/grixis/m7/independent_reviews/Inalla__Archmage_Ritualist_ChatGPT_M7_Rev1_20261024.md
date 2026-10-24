# Inalla, Archmage Ritualist — ChatGPT M7 Rev1 proposal (2026-10-24)

**Status: INDEPENDENT FIVE-SWAP APPROVAL-CANDIDATE; OWNER APPROVAL PENDING. NOT CANONICAL.**

This is the third focused pass, **superseding the round-2 RESEARCH_ONLY conclusion for the proposed M7 quality floor**, not erasing the prior research-only artifacts or October 14 decisions. The earlier fifth-slot attempt (+Pyroblast/−Red Elemental Blast) is still rejected. This pass identified a materially more commander-specific fifth substitution: **Gifts Ungiven replacing Wheel of Fortune**. Six, seven, and further explored alternatives (Buried Alive, Rain of Filth, Phyrexian Tower, Jeweled Amulet, Daze, Mindbreak Trap, Pyroblast, Exhibition Tidecaller, Mistrise Village, Phantasmal Image, Snapback, Fire Magic) were not selected solely to increase count.

## Provenance

- Canonical repository and authority: `corymstover/grixis-commander-encyclopediaGPT` `main/state/current_deck_overrides.json`, `refinement/decklists/Inalla_Archmage_Ritualist_Approved_2026-10-14.txt`.
- Historical approved raw SHA-256: `81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3` (100 names, 27 lands, no final LF).
- Owner October 14 decision: `refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md`. This baseline already rebuilt 49 slots and retains the core Spellseeker/Scholar/Finale, Bloodline/Ruthless, and Breach/Oracle routes.
- New exact **LF-terminated** 100-card proposal: `data/grixis/m7/independent_candidates/Inalla__Archmage_Ritualist_M7_Rev1_Five_Swap_Gifts_20261024.txt`.
- Raw SHA-256 **`c9f35cac41a7717ef49b4dd3cb4f6031c2795a0082b31b54a13e645652df9b69`**.
- Bracket: **5 — cEDH**; Archidekt tags **Spellseeker Combo / Reanimator / Turbo**.
- No commander legality exceptions requested; Flashback 2026-04 print officially released and legal.

## Five specific additions and cuts with material losses

| Add | Cut | Why this helps *Inalla* | Material loss / uncertainty |
|---|---|---|---|
| **Flashback** | **Kefka, Court Mage // Kefka, Ruler of Ruin** | {R} Spellseeker-tutorable instant lets spent `Culling the Weak`, `Unearth`, `Burnt Offering`, `Entomb`, `Reanimate`, etc. be cast from graveyard by paying their costs; protects the signature Eminence chain from some interruptions, lowers mana curve. | Loses five-mana **Wizard** ETB mass discard/card draw and its repeatable attack value. The card to be cast via flashback will be exiled and ordinary mana/timing/target restrictions still apply. **Explicit reversal of Cory's Oct14 Kefka addition**, disclosed. |
| **Corpse Dance** | **Final Fortune** | Adds the documented `Scholar of the Ages` + `Burnt Offering` + **buyback Corpse Dance** infinite B/R mana, spell-return, ETB/storm loop using core Inalla pieces. Can instantly reanimate a Wizard and synergizes with Eminence. | Loses {R}{R} extra-turn closer, sometimes vital to turbo wins. Corpse Dance buyback costs {4}{B}, requires top creature of graveyard to be desired, and is fragile to instant-speed graveyard reorder/hate. **Explicit reversal of Oct14 Final Fortune addition.** |
| **Gifts Ungiven** | **Wheel of Fortune** | {3}{U} instant, at opponent end step, may present `Spellseeker`, `Step Through`, `Reanimate`, `Unearth`. **All six possible two-to-graveyard splits provide Spellseeker in hand or Spellseeker in graveyard with at least one reanimation spell in hand.** This makes an otherwise generic tutor deterministic access to *Inalla's one-card eminence win route*, subject to starting-card/interaction conditions. | Loses the immediate {2}{R} seven-card redraw, graveyard filling and potential turbo/Breach refill. Gifts costs **one more mana**, is a known Game Changer (increases archived set count **18→19**), exposes the line, and needs all four named cards in library to guarantee this particular pile. Strong but not strictly dominating Wheel. **Explicit reversal of Oct14 Wheel addition.** |
| **Forbidden Orchard** | **Exotic Orchard** | Untapped any-color mana independent of opposing land colors, improving early Spellseeker blue and black-ritual sequencing. | Gives an opponent a 1/1 blocker/sacrifice resource with each colored tap; can impede retained Ragavan. Exotic Orchard is often painless rainbow in multicolor tables. |
| **Starting Town** | **Island** | Untapped rainbow during turns 1–3 for one life, replacing a blue-only basic with early access to U/B/R. The deck retains basic `Swamp`, all other fetches/dual sources. | A newly played Town after turn 3 enters tapped; loses fetchable untapped basic Island and protection against nonbasic hate. Conditional land-tempo effect, **not** an unconditional strict upgrade. |

No fifth filler: Pyroblast replacing REB is explicitly **not** in the candidate.

## Gifts pile mechanical proof, exact six cases

Cards revealed: `Spellseeker`, `Step Through`, `Reanimate`, `Unearth`, assuming all remain in library. The opponent puts any two in graveyard and the other two in hand. All six combinations:

| Opponent puts in graveyard | What the controller receives | Inalla access |
|---|---|---|
| Spellseeker + Step Through | Reanimate + Unearth | Reanimate Spellseeker directly |
| Spellseeker + Reanimate | Step Through + Unearth | Unearth Spellseeker directly |
| Spellseeker + Unearth | Step Through + Reanimate | Reanimate Spellseeker directly |
| Step Through + Reanimate | Spellseeker + Unearth | Cast Spellseeker |
| Step Through + Unearth | Spellseeker + Reanimate | Cast Spellseeker |
| Reanimate + Unearth | Spellseeker + Step Through | Cast Spellseeker |

A reanimated nontoken Spellseeker still enters as a Wizard, triggering **Inalla's Eminence**. `Reanimate` requires paying Spellseeker mana value 3 life. `Unearth` returns a mana value 3 or lower creature. To actually win, the owner also needs required colored mana, life, unblocked triggers/stack, necessary line cards in usable zones, and no relevant opponent hate. This table establishes **card access**, not a completed or interaction-proof combo or multiplayer win rate.

## Source-bound 100 verification protocol

- Candidate constructed from exact 100-card historical baseline by five one-for-one substitutions; commander first; 100 physical cards and 100 distinct names, no duplicated nonbasics, Tainted Pact singleton, 27 lands.
- Oracle archive `data/grixis/m6/oracle_snapshots/Inalla__Archmage_Ritualist_M7_Scryfall_20261023.json` contains all 99 candidate names other than Flashback, legal in Commander and U/B/R-or-colorless identity in the archived current Scryfall check; the archive was pulled October 23, not silently rewritten.
- Flashback is documented separately by [Wizards Gatherer SOS #115](https://gatherer.wizards.com/SOS/en-us/115/flashback), [Scryfall SOS #115](https://scryfall.com/card/sos/115/flashback), and [Wizards SOS set legality and flashback rules](https://magic.wizards.com/en/news/feature/secrets-of-strixhaven-release-notes).
- `Gifts Ungiven` is Scryfall-archived **official Commander legal**, U identity and Game Changer; `Wheel of Fortune` is archived legal. Other swaps are documented against exact Oracle text.
- Basic turn-3 conditional mana observations are transparent; no accurate multiplayer cast probability computed.
- Existing combo cores intact: `Spellseeker`/Scholar/Finale, Bloodline/Ruthless, Breach/LED/Brain Freeze, and Thassa's Oracle + Consultation/Pact.
- Focused test `tests/test_m7_inalla_five_swap_gifts_candidate.py` pins exact raw bytes, legality archive, source-bound new Flashback, source-combo tokens, all six Gifts splits, five adds/cuts, land count and owner gate.
- No real games, multiplayer win rates, third-model review, or fully exhaustive Magic rules-engine simulation claimed.

## Why five rather than a numerical cap

The project minimum is five **quality-positive hypotheses with clearly disclosed costs**, not a cap or automatic approval. The current five each address one of: commander-specific spell-reuse, commander-specific recursion combo, deterministic access to Spellseeker, early consistent Grixis source, and early first-three-turn color smoothing. The strongest remaining candidates have meaningful countervailing costs; see prior two adversarial review passes. This is a genuine proposal **for Cory to assess**, not a claim that any individual change dominates in every possible match.

### Stop line

**Await Cory's explicit approval of exactly SHA `c9f35cac41a7717ef49b4dd3cb4f6031c2795a0082b31b54a13e645652df9b69` after he sees the full 100-card list and tradeoffs.** Before that, no canonical PR/merge, no change to Inalla's October 14 APPROVED/LOCKED registry, no change to 22 previous new M7 locks.