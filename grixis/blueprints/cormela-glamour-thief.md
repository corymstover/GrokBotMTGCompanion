# Blueprint — Cormela, Glamour Thief

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/cormela-glamour-thief.md), state `SOURCE_BASELINE`, list `lh1:545b22caf5c71e44…`). Machine-readable source: [`data/grixis/blueprints/cormela-glamour-thief.json`](../../data/grixis/blueprints/cormela-glamour-thief.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Cormela, Glamour Thief** — Legendary Creature — Vampire Rogue

> Haste  
> {1}, {T}: Add {U}{B}{R}. Spend this mana only to cast instant and/or sorcery spells.  
> When Cormela dies, return up to one target instant or sorcery card from your graveyard to your hand.

## Plan and commander role

- **Primary plan:** cEDH instant/sorcery combo: Cormela's hasty restricted UBR mana pays for spell chains, and her death trigger loops with sacrifice outlets plus reanimation/cloning (Saw in Half, Goryo's Vengeance, Shallow Grave, Demonic Gifts, Molten Duplication + Birgi). *strategic_judgment · high*
- **Secondary:** Commander-independent cEDH failovers: Thassa's Oracle + Demonic Consultation/Tainted Pact, Underworld Breach + LED/Petal + Brain Freeze or Wheel, Tendrils of Agony storm.
  - Evidence: [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md) · [Cormela_Glamour_Thief_Finalization_Certificate_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Glamour_Thief_Finalization_Certificate_2026-10-14.md) · [cormela-03](../interactions/cormela-glamour-thief.md#cormela-03) · [cormela-07](../interactions/cormela-glamour-thief.md#cormela-07)
- **Commander role: central.** Cormela is a ritual on a hasty body and the recursion piece of a dozen Spellbook loops; most of the deck's infinites name her. *strategic_judgment · high*
- ⚠️ **Honest note:** The compact Thassa's Oracle and Breach wins don't need her, which is correct for cEDH resilience; the ledger keeps them as failovers, not the identity.
  - Evidence: [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md) · [Cormela_Glamour_Thief_Finalization_Certificate_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Glamour_Thief_Finalization_Certificate_2026-10-14.md) · `spellbook:500-2701-4867`
- **Dependency level:** medium *strategic_judgment · high* — [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (cEDH — 'Cormela is treated at her natural cEDH ceiling' (optimization decision ledger).) | *fact · verified* | [Cormela_Optimization_Decision_Ledger.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md) |
| GrokBot estimated ceiling | 5 (cEDH (Bracket 5): Thassa's Oracle failover, Breach/LED, Necropotence/Ad Nauseam and 14 fast-mana pieces; the commander-specific loops are real. Agrees with the recovered source claim.) | *strategic_judgment · high* | [Cormela_Optimization_Decision_Ledger.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md) · [cormela-07](../interactions/cormela-glamour-thief.md#cormela-07) · `spellbook:742-1295` · [cormela-03](../interactions/cormela-glamour-thief.md#cormela-03) |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Cormela__Glamour_Thief` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 16, "2": 295, "3": 337, "4": 169, "5": 128}, "decks_with_bracket": 945, "share_b4_plus": 0.314, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__cormela-glamour-thief.json`

## Win conditions

- **saw-in-half** (combo): Saw in Half on Cormela with a mana-positive ritual or Jeska's Will: legend rule + death trigger loop. Cards: Cormela, Glamour Thief, Saw in Half, Dark Ritual, Cabal Ritual, Seething Song, Jeska's Will. Enablers: Tendrils of Agony. *fact · verified* — [cormela-03](../interactions/cormela-glamour-thief.md#cormela-03) · `spellbook:500-2701-4867` · `spellbook:500-1878-4867`
- **reanimate-altar** (combo): Cormela + Goryo's Vengeance or Shallow Grave + Ashnod's Altar or Phyrexian Altar. Cards: Cormela, Glamour Thief, Goryo's Vengeance, Shallow Grave, Ashnod's Altar, Phyrexian Altar. Enablers: Entomb. *fact · verified* — [cormela-04](../interactions/cormela-glamour-thief.md#cormela-04) · `spellbook:1893-2034-4867` · `spellbook:2034-3599-4867`
- **molten-duplication** (combo): Cormela + Birgi + Molten Duplication; Dualcaster Mage + Molten Duplication or Saw in Half. Cards: Molten Duplication, Birgi, God of Storytelling // Harnfel, Horn of Bounty, Dualcaster Mage. *fact · verified* — [cormela-06](../interactions/cormela-glamour-thief.md#cormela-06) · `spellbook:392-4867-5487` · `spellbook:147-5487`
- **thoracle** (combo): Thassa's Oracle + Demonic Consultation or Tainted Pact. Cards: Thassa's Oracle, Demonic Consultation, Tainted Pact. *fact · verified* — [cormela-07](../interactions/cormela-glamour-thief.md#cormela-07) · `spellbook:742-1295` · `spellbook:1295-3093`
- **breach** (combo): Underworld Breach + LED/Petal + Brain Freeze or Wheel of Fortune. Cards: Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze, Wheel of Fortune. *fact · verified* — [cormela-08](../interactions/cormela-glamour-thief.md#cormela-08) · `spellbook:1368-3518-4856`

## Engines

- **restricted-mana:** Cormela, Glamour Thief. Online when: {1},{T}: UBR for instants/sorceries; haste means it's usable the turn she lands. *fact · verified* — [cormela-01](../interactions/cormela-glamour-thief.md#cormela-01)
- **death-recursion:** Cormela, Glamour Thief, Ashnod's Altar, Phyrexian Altar, Phyrexian Tower, Demonic Gifts. Online when: Cormela dies: return an instant or sorcery; leave her in the graveyard for reanimation loops. *fact · verified* — [cormela-02](../interactions/cormela-glamour-thief.md#cormela-02) · [cormela-05](../interactions/cormela-glamour-thief.md#cormela-05)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:cormela-loops` | yes | 6 | Commander recursion loop pieces. | 9: Saw in Half, Goryo's Vengeance, Shallow Grave, Demonic Gifts, Molten Duplication, Ashnod's Altar, Phyrexian Altar, Phyrexian Tower, Birgi, God of Storytelling // Harnfel, Horn of Bounty | — | *strategic_judgment · high* | [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md) |
| `pkg:cedh-failover` | yes | 3 | Compact commander-independent wins. | 6: Thassa's Oracle, Demonic Consultation, Tainted Pact, Underworld Breach, Brain Freeze, Tendrils of Agony | — | *strategic_judgment · high* | [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md) |
| `pkg:fast-mana` | yes | 12 | cEDH-speed acceleration. | 14: Sol Ring, Mana Vault, Chrome Mox, Mox Diamond, Mox Opal, Lotus Petal, Lion's Eye Diamond, Dark Ritual, Cabal Ritual, Rite of Flame, Seething Song, Simian Spirit Guide, Ancient Tomb, Gemstone Caverns | — | *strategic_judgment · high* | [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md) |
| `pkg:stack-interaction` | yes | 10 | Win counter wars and protect the combo turn. | 12: Force of Will, Force of Negation, Fierce Guardianship, Pact of Negation, Mindbreak Trap, Flusterstorm, Swan Song, Mental Misstep, Pyroblast, Red Elemental Blast, Deflecting Swat, Orcish Bowmasters | — | *strategic_judgment · high* | [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md) |

## Key interactions

- **restricted-mana-death:** Hasty UBR for instants/sorceries; when she dies, return an instant or sorcery. (Cormela, Glamour Thief) *fact · verified* — [cormela-01](../interactions/cormela-glamour-thief.md#cormela-01)
- **decline-command-zone:** Decline the command-zone move to keep her in the graveyard for reanimation loops. (Cormela, Glamour Thief) *fact · verified* — [cormela-02](../interactions/cormela-glamour-thief.md#cormela-02)
- **saw-in-half-legend:** Saw in Half on Cormela: the legend rule gives a death trigger while one copy stays. (Saw in Half) *fact · verified* — [cormela-03](../interactions/cormela-glamour-thief.md#cormela-03)
- **bowmasters-wheels:** Orcish Bowmasters punishes your own wheels too. (Orcish Bowmasters, Wheel of Fortune, Windfall) *fact · verified* — [cormela-09](../interactions/cormela-glamour-thief.md#cormela-09)

## Tutors and recursion

- Tutor target **Thassa's Oracle** via Demonic Tutor, Vampiric Tutor, Imperial Seal, Wishclaw Talisman, Intuition *strategic_judgment · high* — [cormela-07](../interactions/cormela-glamour-thief.md#cormela-07)
- Tutor target **Saw in Half** via Mystical Tutor, Demonic Tutor, Gamble, Diabolic Intent *strategic_judgment · high* — [cormela-03](../interactions/cormela-glamour-thief.md#cormela-03)
- Tutor target **Underworld Breach** via Mystical Tutor, Gamble, Imperial Seal *strategic_judgment · high* — [cormela-08](../interactions/cormela-glamour-thief.md#cormela-08)
- Recursion: Underworld Breach, Reanimate, Goryo's Vengeance, Shallow Grave, Entomb *fact · verified* — [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md)

## Requirements

- **Interaction:** cEDH-level stack interaction (12+ free/cheap counters) plus Bowmasters.
- **Protection:** Counters protect the combo; Cormela is cheap to recast and can stay in the graveyard on purpose.
- **Mana:** 14+ fast-mana pieces, ~28 lands, untapped fetch/dual base (Xander's Lounge cut for Flooded Strand).
- *strategic_judgment · high* — [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md)

## Failure modes

- **stack-war-lost:** Losing the counter war on the combo turn. Mitigations: Free counters; Multiple distinct lines. *strategic_judgment · high* — [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md)
- **graveyard-hate:** Graveyard hate stops reanimation/Breach lines. Mitigations: Saw in Half and Thassa's Oracle don't use the graveyard. *strategic_judgment · moderate* — [cormela-02](../interactions/cormela-glamour-thief.md#cormela-02)
- **self-damage:** Ad Nauseam, Necropotence, City of Brass and Mana Confluence cost life. Mitigations: Fast kill. *strategic_judgment · moderate* — [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md)

## Identity core

- **Cormela, Glamour Thief:** Hasty spell ritual and the death-trigger half of most loops. *fact · verified* — `oracle:Cormela, Glamour Thief`
- **Saw in Half:** Two-card commander loop with any mana-positive ritual. *strategic_judgment · high* — [cormela-03](../interactions/cormela-glamour-thief.md#cormela-03)
- **Molten Duplication:** Copies Cormela for the Birgi loop and Dualcaster for the token loop. *strategic_judgment · high* — [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md)
- **Goryo's Vengeance:** Instant-speed reanimation half of the altar loop. *strategic_judgment · high* — [cormela-04](../interactions/cormela-glamour-thief.md#cormela-04)
- **Thassa's Oracle:** Compact failover that raises resilience. *strategic_judgment · high* — [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md)

## Anti-goals and thematic constraints

- ✗ Don't let the generic Grixis cEDH failovers replace the Cormela loops as the identity.
- ✗ Don't keep slow, exposed cost reducers (Electromancer, Storm-Kiln Artist cut in the ledger).
  - *strategic_judgment · high* — [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md) · [Cormela_Glamour_Thief_Finalization_Certificate_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Glamour_Thief_Finalization_Certificate_2026-10-14.md)
- Theme: Thief/glamour flavor is incidental; the identity is mechanical.
  - *strategic_judgment · low* — [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 903.9a:** Choosing not to move Cormela to the command zone keeps her in the graveyard for loops. *fact · verified* — `cr:903.9a`
- **CR 704.5j:** Saw in Half copies of Cormela hit the legend rule: one goes to the graveyard and triggers. *fact · verified* — `cr:704.5j`

## Supporting features (heuristic, not identity)

- `{"hooks": ["graveyard as a resource", "instants and sorceries"], "hooked_cards": 53, "role_counts": {"counter": 10, "draw": 11, "protection": 1, "ramp": 20, "removal": 5, "tutor": 8, "wipe": 1}, "lands": 30, "edhrec_pages": ["cormela-glamour-thief"]}` *heuristic · low*

## Provenance

- Seeded from: [Cormela_Glamour_Thief_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Cormela_Glamour_Thief_v1.md) · [Cormela_Optimization_Decision_Ledger.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md) · [Cormela_Glamour_Thief_Finalization_Certificate_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/cormela_2026-10-14/Cormela_Glamour_Thief_Finalization_Certificate_2026-10-14.md) · [Cormela_Glamour_Thief_Current_Cycle_Approval_Gate_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cormela_Glamour_Thief_Current_Cycle_Approval_Gate_2026-10-14.md)
- Reviewed by: — (not yet reviewed by Cory)
