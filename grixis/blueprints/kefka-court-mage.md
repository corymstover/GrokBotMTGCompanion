# Blueprint — Kefka, Court Mage // Kefka, Ruler of Ruin

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/kefka-court-mage.md), state `SOURCE_BASELINE`, list `lh1:a858b67801ed8c47…`). Machine-readable source: [`data/grixis/blueprints/kefka-court-mage.json`](../../data/grixis/blueprints/kefka-court-mage.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Kefka, Court Mage // Kefka, Ruler of Ruin** — Legendary Creature — Human Wizard // Legendary Creature — Avatar Wizard

> Whenever Kefka enters or attacks, each player discards a card. Then you draw a card for each card type among cards discarded this way.  
> {8}: Each opponent sacrifices a permanent of their choice. Transform Kefka. Activate only as a sorcery.  
> Flying  
> Whenever an opponent loses life during your turn, you draw that many cards.

## Plan and commander role

- **Primary plan:** cEDH hand attack: repeat Kefka's enter/attack trigger (haste via Anger or Arena of Glory, Harmonic Prodigy, blink, clones, Gogo, Saw in Half) so every player discards while you draw per card type, then win with Thassa's Oracle or Underworld Breach. *strategic_judgment · high*
- **Secondary:** Discard payoffs (Waste Not, Tinybones) and opposing life loss on your turn for the Ruler of Ruin face; Final Fortune for an extra Kefka turn.
  - Evidence: [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md) · [kefka-01](../interactions/kefka-court-mage.md#kefka-01-discard-trigger-counts-card-types-per-trigger) · [kefka-11](../interactions/kefka-court-mage.md#kefka-11-oracle-and-breach-finishes-protection-notes)
- **Commander role: central.** Haste, blink and copy slots all exist to make more Kefka triggers; his discard-draw is the deck's card-advantage and disruption engine. *strategic_judgment · high*
- ⚠️ **Honest note:** The kills (Oracle + Consultation/Pact, Breach lines) are generic and commander-independent. The {8} transform is rarely reached, and the back face is incidental (the source declined a Psychosis Crawler package).
  - Evidence: [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md) · [kefka-02](../interactions/kefka-court-mage.md#kefka-02-8-opponents-sacrifice-is-simultaneous-then-kefka-transforms) · [kefka-11](../interactions/kefka-court-mage.md#kefka-11-oracle-and-breach-finishes-protection-notes)
- **Dependency level:** medium *strategic_judgment · high* — [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (Power Bracket 5 — cEDH (decisions).) | *fact · verified* | [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 5 (Bracket 5 ceiling: genuine competitive commander with 2026 top cuts per the source and a full cEDH shell. Agrees with the source.) | *strategic_judgment · high* | [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md) · `spellbook:742-1295` |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Kefka__Court_Mage` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 45, "2": 680, "3": 2878, "4": 2401, "5": 2208}, "decks_with_bracket": 8212, "share_b4_plus": 0.561, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__kefka-court-mage.json`

## Win conditions

- **oracle** (combo): Thassa's Oracle with Demonic Consultation or Tainted Pact. Cards: Thassa's Oracle, Demonic Consultation, Tainted Pact. *fact · verified* — `spellbook:742-1295` · `spellbook:1295-3093` · [kefka-11](../interactions/kefka-court-mage.md#kefka-11-oracle-and-breach-finishes-protection-notes)
- **breach** (combo): Underworld Breach + LED/Petal + Brain Freeze, or Wheel of Fortune + Jeska's Will/LED. Cards: Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze, Wheel of Fortune, Jeska's Will. *fact · verified* — `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856` · `spellbook:1368-1878-2706` · `spellbook:1368-2706-3518` · [kefka-11](../interactions/kefka-court-mage.md#kefka-11-oracle-and-breach-finishes-protection-notes)
- **hand-lock-turns** (natural): Repeated Kefka triggers empty opposing hands; Final Fortune buys a protected combo turn. Cards: Final Fortune, Waste Not, Tinybones, Bauble Burglar. Enablers: Kefka, Court Mage // Kefka, Ruler of Ruin. *strategic_judgment · moderate* — [kefka-13](../interactions/kefka-court-mage.md#kefka-13-final-fortune-an-extra-kefka-turn-that-you-must-win)

## Engines

- **kefka-triggers:** Kefka, Court Mage // Kefka, Ruler of Ruin, Harmonic Prodigy, Anger, Arena of Glory. Online when: Kefka enters or attacks. *fact · verified* — [kefka-01](../interactions/kefka-court-mage.md#kefka-01-discard-trigger-counts-card-types-per-trigger) · [kefka-03](../interactions/kefka-court-mage.md#kefka-03-harmonic-prodigy-doubles-both-faces) · [kefka-04](../interactions/kefka-court-mage.md#kefka-04-haste-discard-anger-to-kefkas-own-trigger-or-use-arena-of-glory)
- **extra-kefkas:** Gogo, Mysterious Mime, Phantasmal Image, Phyrexian Metamorph, Molten Duplication, Saw in Half, Essence Flux, Displacer Kitten. Online when: Kefka in play to copy or blink. *fact · verified* — [kefka-05](../interactions/kefka-court-mage.md#kefka-05-gogo-copies-kefka-without-the-legend-rule) · [kefka-06](../interactions/kefka-court-mage.md#kefka-06-clones-of-kefka-image-and-metamorph-vs-molten-duplication) · [kefka-07](../interactions/kefka-court-mage.md#kefka-07-saw-in-half-on-your-commander-kefka) · [kefka-08](../interactions/kefka-court-mage.md#kefka-08-blink-re-triggers-essence-flux-and-displacer-kitten)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:copy-blink` | yes | 6 | More Kefka ETBs and attacks. | 8: Gogo, Mysterious Mime, Phantasmal Image, Phyrexian Metamorph, Molten Duplication, Saw in Half, Essence Flux, Displacer Kitten, Harmonic Prodigy | — | *strategic_judgment · high* | [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md) · [kefka-06](../interactions/kefka-court-mage.md#kefka-06-clones-of-kefka-image-and-metamorph-vs-molten-duplication) |
| `pkg:haste` | yes | 2 | Same-turn attack trigger. | 2: Anger, Arena of Glory | — | *strategic_judgment · high* | [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md) · [kefka-04](../interactions/kefka-court-mage.md#kefka-04-haste-discard-anger-to-kefkas-own-trigger-or-use-arena-of-glory) |
| `pkg:free-interaction` | yes | 8 | cEDH stack protection. | 12: Force of Will, Force of Negation, Pact of Negation, Fierce Guardianship, Mental Misstep, Mindbreak Trap, Flusterstorm, Swan Song, Pyroblast, Red Elemental Blast, Deflecting Swat, Into the Flood Maw | — | *strategic_judgment · high* | [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md) |

## Key interactions

- **card-types:** Draw equals the card types among that trigger's discards; supertypes don't count. (Kefka, Court Mage // Kefka, Ruler of Ruin) *fact · verified* — [kefka-01](../interactions/kefka-court-mage.md#kefka-01-discard-trigger-counts-card-types-per-trigger)
- **anger-haste:** Discard Anger to Kefka's own ETB and attack the same turn (needs a Mountain). (Anger, Kefka, Court Mage // Kefka, Ruler of Ruin) *fact · verified* — [kefka-04](../interactions/kefka-court-mage.md#kefka-04-haste-discard-anger-to-kefkas-own-trigger-or-use-arena-of-glory)
- **clones-transform:** Single-faced clones can't transform; Molten Duplication's token is double-faced. (Phantasmal Image, Phyrexian Metamorph, Molten Duplication) *fact · verified* — [kefka-06](../interactions/kefka-court-mage.md#kefka-06-clones-of-kefka-image-and-metamorph-vs-molten-duplication)
- **counsel-delirium:** Demonic Counsel is a full tutor only with delirium. (Demonic Counsel) *fact · verified* — [kefka-10](../interactions/kefka-court-mage.md#kefka-10-demonic-counsel-needs-delirium-to-be-a-full-tutor)
- **floodcaller:** Valley Floodcaller gives noncreature spells flash but doesn't untap Kefka. (Valley Floodcaller) *fact · verified* — [kefka-12](../interactions/kefka-court-mage.md#kefka-12-valley-floodcaller-flash-for-noncreature-spells-but-no-kefka-untap)

## Tutors and recursion

- Tutor target **Thassa's Oracle** via Vampiric Tutor, Imperial Seal, Mystical Tutor, Wishclaw Talisman *strategic_judgment · high* — `spellbook:742-1295`
- Tutor target **Underworld Breach** via Demonic Tutor, Gamble, Diabolic Intent *strategic_judgment · high* — `spellbook:1368-3518-4856`
- Recursion: Reanimate, Underworld Breach, Jeska's Will *strategic_judgment · moderate* — [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Free counters and one-mana interaction.
- **Protection:** Fierce Guardianship, Deflecting Swat, Cavern of Souls.
- **Mana:** Fast mana and rituals for a five-mana commander.
- *strategic_judgment · high* — [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **kefka-removed:** A five-mana commander removed before triggering much. Mitigations: Commander-free Oracle/Breach; Clones and Saw in Half. *strategic_judgment · high* — [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md)
- **low-diversity:** Opponents discarding one card type each draw you little. Mitigations: Repeat triggers; Discard payoffs. *strategic_judgment · moderate* — [kefka-01](../interactions/kefka-court-mage.md#kefka-01-discard-trigger-counts-card-types-per-trigger)
- **counsel-no-delirium:** Demonic Counsel without delirium only finds a Demon. Mitigations: Discard types into your yard first. *strategic_judgment · moderate* — [kefka-10](../interactions/kefka-court-mage.md#kefka-10-demonic-counsel-needs-delirium-to-be-a-full-tutor)

## Identity core

- **Kefka, Court Mage // Kefka, Ruler of Ruin:** Symmetric discard on enter/attack; you draw per card type. *fact · verified* — `oracle:Kefka, Court Mage // Kefka, Ruler of Ruin`
- **Harmonic Prodigy:** Doubles Kefka's Wizard triggers on both faces. *strategic_judgment · high* — [kefka-03](../interactions/kefka-court-mage.md#kefka-03-harmonic-prodigy-doubles-both-faces)
- **Anger:** Discarded to Kefka's own trigger for same-turn haste. *strategic_judgment · high* — [kefka-04](../interactions/kefka-court-mage.md#kefka-04-haste-discard-anger-to-kefkas-own-trigger-or-use-arena-of-glory)
- **Gogo, Mysterious Mime:** A Kefka copy without the legend rule; two attack triggers. *strategic_judgment · high* — [kefka-05](../interactions/kefka-court-mage.md#kefka-05-gogo-copies-kefka-without-the-legend-rule)
- **Displacer Kitten:** Each noncreature spell re-triggers Kefka's ETB. *strategic_judgment · moderate* — [kefka-08](../interactions/kefka-court-mage.md#kefka-08-blink-re-triggers-essence-flux-and-displacer-kitten)

## Anti-goals and thematic constraints

- ✗ No dedicated Psychosis Crawler/back-face package (decisions L60).
- ✗ Slow discard payoffs (Geth's Grimoire) cut at this ceiling (decisions L44).
  - *strategic_judgment · high* — [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Final Fantasy VI's mad court mage: ruin, discard and chaos.
  - *strategic_judgment · moderate* — [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.27c:** Single-faced permanents can't transform. *fact · verified* — `cr:701.27c`
- **CR 704.5j:** Legend rule after clone ETBs trigger. *fact · verified* — `cr:704.5j`

## Supporting features (heuristic, not identity)

- `{"hooks": ["combat damage / attack triggers", "discard", "sacrifice"], "hooked_cards": 23, "role_counts": {"counter": 10, "draw": 6, "protection": 1, "ramp": 20, "removal": 6, "tutor": 9, "wipe": 3}, "lands": 28, "edhrec_pages": ["kefka-court-mage"]}` *heuristic · low*

## Provenance

- Seeded from: [Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md) · [Kefka_Court_Mage_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Kefka_Court_Mage_Approved_2026-10-14.md) · [Kefka_Court_Mage_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Kefka_Court_Mage_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
