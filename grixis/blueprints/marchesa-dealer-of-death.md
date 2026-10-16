# Blueprint — Marchesa, Dealer of Death

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/marchesa-dealer-of-death.md), state `SOURCE_BASELINE`, list `lh1:c37dda3aa8ad8964…`). Machine-readable source: [`data/grixis/blueprints/marchesa-dealer-of-death.json`](../../data/grixis/blueprints/marchesa-dealer-of-death.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Marchesa, Dealer of Death** — Legendary Creature — Human Rogue

> Whenever you commit a crime, you may pay {1}. If you do, look at the top two cards of your library. Put one of them into your hand and the other into your graveyard. (Targeting opponents, anything they control, and/or cards in their graveyards is a crime.)

## Plan and commander role

- **Primary plan:** cEDH: necessary targeted interaction doubles as crimes, so Marchesa turns each answer into {1} top-two card selection; fast mana and tutors race to Tainted Pact + Thassa's Oracle, Breach + LED/Petal + Brain Freeze, or Aphetto Alchemist + Hawkeye's Bow. *strategic_judgment · high*
- **Secondary:** Cheap repeatable crime sources (Spatial Binding, Hex Parasite, Spellskite, Tezzeret, Lapis Lazuli Talisman, Talon Gates) keep the selection engine running; Rhystic Study, Remora, Necropotence and Ad Nauseam refill.
  - Evidence: [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md) · [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)
- **Commander role: significant.** Marchesa converts the deck's interaction into card selection and graveyard setup. *strategic_judgment · high*
- ⚠️ **Honest note:** All three win packages work without her, and the list is the exact copy of a tournament-winning list (Takeda Ryuhei, 2026-10-11), a 48-card rebuild from the source baseline (decisions L10, L12). She is a selection engine in a generic Grixis cEDH shell, not a kill. No M1 interaction review exists yet for this deck.
  - Evidence: [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L10](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md) · [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)
- **Dependency level:** low *strategic_judgment · high* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (Power Bracket 5 — cEDH (approval).) | *fact · verified* | [Marchesa_Dealer_of_Death_Approved_2026-10-15.md#L6](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Marchesa_Dealer_of_Death_Approved_2026-10-15.md) |
| GrokBot estimated ceiling | 5 (Bracket 5 ceiling: an exact tournament-winning cEDH list with three compact wins. Agrees with the source.) | *strategic_judgment · high* | [Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md) · `spellbook:1295-3093` |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Marchesa__Dealer_of_Death` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 37, "2": 651, "3": 524, "4": 167, "5": 138}, "decks_with_bracket": 1517, "share_b4_plus": 0.201, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__marchesa-dealer-of-death.json`

## Win conditions

- **oracle-pact** (combo): Tainted Pact + Thassa's Oracle. Cards: Tainted Pact, Thassa's Oracle. *fact · verified* — `spellbook:1295-3093`
- **breach** (combo): Underworld Breach + LED/Lotus Petal + Brain Freeze. Cards: Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze. *fact · verified* — `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856`
- **bow-alchemist** (combo): Aphetto Alchemist + Hawkeye's Bow: deterministic damage loop. Cards: Aphetto Alchemist, Hawkeye's Bow. *fact · verified* — `spellbook:4091-7786` · [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)

## Engines

- **crime-selection:** Marchesa, Dealer of Death, Spatial Binding, Hex Parasite, Spellskite, Tezzeret, Cruel Captain, Lapis Lazuli Talisman, Talon Gates of Madara. Online when: Targeting an opponent or their stuff with {1} spare. *fact · high* — `oracle:Marchesa, Dealer of Death` · [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)
- **fast-mana-draw:** Mana Vault, Chrome Mox, Mox Diamond, Lotus Petal, Dark Ritual, Rhystic Study, Mystic Remora, Necropotence, Ad Nauseam. Online when: Opening hand. *strategic_judgment · high* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:crime-sources` | yes | 5 | Cheap repeatable targeting of opponents. | 7: Spatial Binding, Hex Parasite, Spellskite, Tezzeret, Cruel Captain, Lapis Lazuli Talisman, Talon Gates of Madara, Urborg | — | *strategic_judgment · high* | [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md) · [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md) |
| `pkg:free-interaction` | yes | 10 | cEDH interaction that is also a crime. | 16: Force of Will, Force of Negation, Pact of Negation, Fierce Guardianship, Mental Misstep, Minor Misstep, Mindbreak Trap, Flusterstorm, Swan Song, Pyroblast, Red Elemental Blast, Dispel, Stifle, Into the Flood Maw, Chain of Vapor, An Offer You Can't Refuse | — | *strategic_judgment · high* | [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md) · [Marchesa_Dealer_of_Death_Whole_List_Audit_2026-10-15.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Whole_List_Audit_2026-10-15.csv) |
| `pkg:tutors` | yes | 5 | Find a win package. | 6: Demonic Tutor, Vampiric Tutor, Imperial Seal, Mystical Tutor, Tainted Pact, Praetor's Grasp | — | *strategic_judgment · high* | [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md) |

## Key interactions

- **crime-definition:** Targeting an opponent, their permanents or their graveyard cards is a crime; Marchesa triggers once per crime. (Marchesa, Dealer of Death) *fact · high* — `oracle:Marchesa, Dealer of Death` · `cr:700.13`
- **hex-parasite-x0:** Hex Parasite at X=0 still targets, so it's a cheap repeatable crime. (Hex Parasite) *fact · high* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)
- **spatial-binding:** Spatial Binding targets for 1 life: a crime each activation. (Spatial Binding) *fact · high* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)
- **lapis:** Lapis Lazuli Talisman turns blue spells into targeted triggers and more crimes. (Lapis Lazuli Talisman) *fact · high* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)

## Tutors and recursion

- Tutor target **Thassa's Oracle** via Vampiric Tutor, Imperial Seal, Mystical Tutor *strategic_judgment · high* — `spellbook:1295-3093`
- Tutor target **Underworld Breach** via Demonic Tutor, Praetor's Grasp *strategic_judgment · high* — `spellbook:1368-3518-4856`
- Recursion: Underworld Breach, Jeska's Will *strategic_judgment · moderate* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Free and one-mana permission, bounce and removal.
- **Protection:** Fierce Guardianship, Deflecting Swat, Spellskite.
- **Mana:** 29 lands, zero/one-mana acceleration and rituals.
- *strategic_judgment · high* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)

## Failure modes

- **graveyard-hate:** Graveyard hate stops Breach. Mitigations: Oracle + Pact; Bow + Alchemist. *strategic_judgment · high* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)
- **marchesa-removed:** Without Marchesa, crimes give no selection. Mitigations: Commander-free wins. *strategic_judgment · moderate* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)
- **baseline-loss:** The 48-card rebuild abandons most of the source baseline's identity. Mitigations: Accepted by the source as the commander's real ceiling. *strategic_judgment · moderate* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)

## Identity core

- **Marchesa, Dealer of Death:** Crime trigger: pay {1} for top-two selection. *fact · verified* — `oracle:Marchesa, Dealer of Death`
- **Spatial Binding:** Repeatable 1-life crime. *strategic_judgment · high* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)
- **Hex Parasite:** X=0 crime activations. *strategic_judgment · high* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)
- **Hawkeye's Bow:** With Aphetto Alchemist, a compact damage win. *strategic_judgment · high* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)
- **Lapis Lazuli Talisman:** More crimes from blue spells. *strategic_judgment · moderate* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ Don't restore generic crime payoffs only for theme density (decisions L30).
- ✗ The source froze this exact list; revise only on explicit request (decisions closeout).
  - *strategic_judgment · high* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)
- Theme: Theme subordinate to cEDH: crimes come from interaction, not a crime-payoff theme.
  - *strategic_judgment · high* — [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 700.13:** Committing a crime. *fact · verified* — `cr:700.13`
- **CR 115.1:** Targets: what makes an action a crime. *fact · verified* — `cr:115.1`

## Supporting features (heuristic, not identity)

- `{"hooks": ["crimes (targeting opponents and their things)", "graveyard as a resource"], "hooked_cards": 37, "role_counts": {"counter": 15, "draw": 5, "protection": 2, "ramp": 22, "removal": 6, "tutor": 5}, "lands": 29, "edhrec_pages": ["marchesa-dealer-of-death"]}` *heuristic · low*

## Provenance

- Seeded from: [Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Current_Cycle_Decisions_2026-10-15.md) · [Marchesa_Dealer_of_Death_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Marchesa_Dealer_of_Death_Approved_2026-10-15.md) · [Marchesa_Dealer_of_Death_Whole_List_Audit_2026-10-15.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_Dealer_of_Death_Whole_List_Audit_2026-10-15.csv) · [Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Marchesa_Dealer_of_Death_Approval_Ready_Verification_2026-10-15.md) · [Marchesa_Dealer_of_Death_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Marchesa_Dealer_of_Death_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
