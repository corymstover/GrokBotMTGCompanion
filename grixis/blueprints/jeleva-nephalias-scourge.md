# Blueprint — Jeleva, Nephalia's Scourge

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/jeleva-nephalias-scourge.md), state `SOURCE_BASELINE`, list `lh1:21c3ebbd08ef90b8…`). Machine-readable source: [`data/grixis/blueprints/jeleva-nephalias-scourge.json`](../../data/grixis/blueprints/jeleva-nephalias-scourge.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Jeleva, Nephalia's Scourge** — Legendary Creature — Vampire Wizard

> Flying  
> When Jeleva enters, each player exiles the top X cards of their library, where X is the amount of mana spent to cast Jeleva.  
> Whenever Jeleva attacks, you may cast an instant or sorcery spell from among cards exiled with Jeleva without paying its mana cost.

## Plan and commander role

- **Primary plan:** Stage a big instant or sorcery on top (Mystical/Vampiric Tutor, Imperial Seal, Personal Tutor, Scheming Symmetry, Long-Term Plans), cast Jeleva to exile it, give her haste and attack to cast it free: Mind's Desire, Peer into the Abyss, Mnemonic Betrayal, Doomsday, Yawgmoth's Will. *strategic_judgment · high*
- **Secondary:** Fringe-cEDH turbo backups: Thassa's Oracle + Consultation/Tainted Pact/Doomsday, Underworld Breach + LED/Petal + Brain Freeze or Wheel + Jeska's Will.
  - Evidence: [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md) · [jeleva-05](../interactions/jeleva-nephalias-scourge.md#jeleva-05-staging-the-top-of-the-library-for-jelevas-exile) · [jeleva-07](../interactions/jeleva-nephalias-scourge.md#jeleva-07-free-cast-payoffs-minds-desire-storm-final-fortune-peer-into-the-abyss)
- **Commander role: significant.** Jeleva is the spell-cheating card-advantage engine the top-deck setup is built for. *strategic_judgment · high*
- ⚠️ **Honest note:** She has to resolve, gain haste and survive to attack before she does anything, and all the compact wins (Oracle, Doomsday, Breach) are commander-independent. She's a strong value engine, not the deck's kill.
  - Evidence: [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md) · [jeleva-03](../interactions/jeleva-nephalias-scourge.md#jeleva-03-the-attack-trigger-cast-happens-during-resolution-before-blockers) · [jeleva-08](../interactions/jeleva-nephalias-scourge.md#jeleva-08-oracle-lines-and-doomsday-dont-cast-jeleva-onto-your-own-pile)
- **Dependency level:** medium *strategic_judgment · high* — [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (Power Bracket 5 — fringe cEDH (decisions).) | *fact · verified* | [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 5 (Bracket 5 ceiling (fringe): full cEDH turbo shell; the commander converts less well than top shells per the source's tournament note. Agrees with the source.) | *strategic_judgment · high* | [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md) · `spellbook:1295-3189` |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Jeleva__Nephalia_s_Scourge` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 19, "2": 259, "3": 282, "4": 114, "5": 29}, "decks_with_bracket": 703, "share_b4_plus": 0.203, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__jeleva-nephalias-scourge.json`

## Win conditions

- **oracle-doomsday** (combo): Thassa's Oracle with Demonic Consultation, Tainted Pact or Doomsday; don't cast Jeleva onto your own Doomsday pile. Cards: Thassa's Oracle, Demonic Consultation, Tainted Pact, Doomsday. *fact · verified* — `spellbook:742-1295` · `spellbook:1295-3093` · `spellbook:1295-3189` · [jeleva-08](../interactions/jeleva-nephalias-scourge.md#jeleva-08-oracle-lines-and-doomsday-dont-cast-jeleva-onto-your-own-pile)
- **breach** (combo): Underworld Breach + LED/Petal + Brain Freeze, or Wheel of Fortune + Jeska's Will/LED. Cards: Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze, Wheel of Fortune, Jeska's Will. *fact · verified* — `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856` · `spellbook:1368-1878-2706` · `spellbook:1368-2706-3518` · [jeleva-09](../interactions/jeleva-nephalias-scourge.md#jeleva-09-breach-lines-led--brain-freeze-wheel--jeskas-will)
- **free-haymaker** (natural): A free Mind's Desire or Peer into the Abyss off Jeleva's attack snowballs into a combo turn. Cards: Mind's Desire, Peer into the Abyss, Mnemonic Betrayal, Yawgmoth's Will, Final Fortune. Enablers: Jeleva, Nephalia's Scourge. *strategic_judgment · moderate* — [jeleva-07](../interactions/jeleva-nephalias-scourge.md#jeleva-07-free-cast-payoffs-minds-desire-storm-final-fortune-peer-into-the-abyss)

## Engines

- **exile-and-cast:** Jeleva, Nephalia's Scourge, Harmonic Prodigy, Lightning Greaves, Torch Courier, Arena of Glory. Online when: Jeleva enters with a staged spell in range and attacks. *fact · verified* — [jeleva-01](../interactions/jeleva-nephalias-scourge.md#jeleva-01-x-counts-the-mana-actually-spent-including-commander-tax) · [jeleva-03](../interactions/jeleva-nephalias-scourge.md#jeleva-03-the-attack-trigger-cast-happens-during-resolution-before-blockers) · [jeleva-04](../interactions/jeleva-nephalias-scourge.md#jeleva-04-harmonic-prodigy-doubles-both-jeleva-triggers)
- **top-staging:** Mystical Tutor, Vampiric Tutor, Imperial Seal, Personal Tutor, Scheming Symmetry, Long-Term Plans, Brainstorm, Scroll Rack, Sensei's Divining Top. Online when: Before casting Jeleva. *fact · verified* — [jeleva-05](../interactions/jeleva-nephalias-scourge.md#jeleva-05-staging-the-top-of-the-library-for-jelevas-exile)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:top-tutors` | yes | 6 | Put the target where Jeleva exiles it. | 9: Mystical Tutor, Vampiric Tutor, Imperial Seal, Personal Tutor, Scheming Symmetry, Long-Term Plans, Scroll Rack, Sensei's Divining Top, Brainstorm | — | *strategic_judgment · high* | [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md) · [jeleva-05](../interactions/jeleva-nephalias-scourge.md#jeleva-05-staging-the-top-of-the-library-for-jelevas-exile) |
| `pkg:haste` | yes | 3 | Attack the turn she lands. | 3: Lightning Greaves, Torch Courier, Arena of Glory | — | *strategic_judgment · high* | [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md) · [jeleva-06](../interactions/jeleva-nephalias-scourge.md#jeleva-06-haste-package-greaves-shroud-blocks-torch-courier) |
| `pkg:free-cast-targets` | yes | 5 | High-leverage spells worth casting free. | 6: Mind's Desire, Peer into the Abyss, Mnemonic Betrayal, Doomsday, Yawgmoth's Will, Final Fortune | — | *strategic_judgment · high* | [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md) · [jeleva-07](../interactions/jeleva-nephalias-scourge.md#jeleva-07-free-cast-payoffs-minds-desire-storm-final-fortune-peer-into-the-abyss) |

## Key interactions

- **x-includes-tax:** X is the mana actually spent, commander tax included; not cast means X = 0. (Jeleva, Nephalia's Scourge) *fact · verified* — [jeleva-01](../interactions/jeleva-nephalias-scourge.md#jeleva-01-x-counts-the-mana-actually-spent-including-commander-tax)
- **own-exile:** Each Jeleva object only knows the cards it exiled. (Jeleva, Nephalia's Scourge) *fact · verified* — [jeleva-02](../interactions/jeleva-nephalias-scourge.md#jeleva-02-each-jeleva-object-only-knows-its-own-exiled-cards)
- **prodigy:** Harmonic Prodigy doubles both triggers: two exiles, two free casts. (Harmonic Prodigy) *fact · verified* — [jeleva-04](../interactions/jeleva-nephalias-scourge.md#jeleva-04-harmonic-prodigy-doubles-both-jeleva-triggers)
- **greaves-courier:** Greaves' shroud blocks Torch Courier's targeting. (Lightning Greaves, Torch Courier) *fact · verified* — [jeleva-06](../interactions/jeleva-nephalias-scourge.md#jeleva-06-haste-package-greaves-shroud-blocks-torch-courier)
- **doomsday-pile:** Don't cast Jeleva onto your own Doomsday pile. (Doomsday, Jeleva, Nephalia's Scourge) *fact · verified* — [jeleva-08](../interactions/jeleva-nephalias-scourge.md#jeleva-08-oracle-lines-and-doomsday-dont-cast-jeleva-onto-your-own-pile)

## Tutors and recursion

- Tutor target **Thassa's Oracle** via Vampiric Tutor, Imperial Seal, Wishclaw Talisman *strategic_judgment · high* — `spellbook:742-1295`
- Tutor target **Mind's Desire** via Mystical Tutor, Personal Tutor *strategic_judgment · high* — [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md)
- Recursion: Yawgmoth's Will, Underworld Breach, Jeska's Will *strategic_judgment · moderate* — [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Free counters and one-mana interaction; Toxic Deluge.
- **Protection:** Fierce Guardianship, Deflecting Swat, haste to minimise exposure.
- **Mana:** Fast mana and rituals to raise Jeleva's X.
- *strategic_judgment · high* — [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **no-attack:** Jeleva removed before attacking: no free cast. Mitigations: Haste package; Commander-free Oracle/Breach. *strategic_judgment · high* — [jeleva-03](../interactions/jeleva-nephalias-scourge.md#jeleva-03-the-attack-trigger-cast-happens-during-resolution-before-blockers)
- **top-disrupted:** Top-of-library changes before the ETB miss the staged card. Mitigations: Cast Jeleva in response windows. *strategic_judgment · moderate* — [jeleva-05](../interactions/jeleva-nephalias-scourge.md#jeleva-05-staging-the-top-of-the-library-for-jelevas-exile)
- **graveyard-hate:** Graveyard hate stops Breach and Yawgmoth's Will. Mitigations: Oracle/Doomsday lines. *strategic_judgment · moderate* — [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md)

## Identity core

- **Jeleva, Nephalia's Scourge:** Exiles the top X of every library and casts an instant or sorcery free on attack. *fact · verified* — `oracle:Jeleva, Nephalia's Scourge`
- **Harmonic Prodigy:** Doubles both Jeleva triggers. *strategic_judgment · high* — [jeleva-04](../interactions/jeleva-nephalias-scourge.md#jeleva-04-harmonic-prodigy-doubles-both-jeleva-triggers)
- **Scheming Symmetry:** Two staged cards for one Jeleva exile. *strategic_judgment · high* — [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md)
- **Mind's Desire:** Premier free-cast target. *strategic_judgment · high* — [jeleva-07](../interactions/jeleva-nephalias-scourge.md#jeleva-07-free-cast-payoffs-minds-desire-storm-final-fortune-peer-into-the-abyss)
- **Torch Courier:** Cheap haste for the same-turn attack. *strategic_judgment · moderate* — [jeleva-06](../interactions/jeleva-nephalias-scourge.md#jeleva-06-haste-package-greaves-shroud-blocks-torch-courier)

## Anti-goals and thematic constraints

- ✗ The 7–10-mana battlecruiser exile-value shell was retired as too slow (decisions).
- ✗ Generic slow value (The One Ring, Roaming Throne, Strionic Resonator) rejected (decisions L69, L73).
  - *strategic_judgment · high* — [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md#L69](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Vampire Wizard pirate of Nephalia: plundering libraries; theme subordinate to cEDH.
  - *strategic_judgment · moderate* — [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 107.3m:** X determined by mana spent on an ETB-referencing permanent. *fact · verified* — `cr:107.3m`
- **CR 903.8:** Commander tax. *fact · verified* — `cr:903.8`

## Supporting features (heuristic, not identity)

- `{"hooks": ["combat damage / attack triggers", "instants and sorceries"], "hooked_cards": 50, "role_counts": {"counter": 10, "draw": 11, "protection": 2, "ramp": 18, "removal": 4, "tutor": 8, "wipe": 3}, "lands": 27, "edhrec_pages": ["jeleva-nephalias-scourge"]}` *heuristic · low*

## Provenance

- Seeded from: [Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Jeleva_Nephalia_s_Scourge_Current_Cycle_Decisions_2026-10-14.md) · [Jeleva_Nephalia_s_Scourge_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Jeleva_Nephalia_s_Scourge_Approved_2026-10-14.md) · [Jeleva_Nephalia_s_Scourge_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Jeleva_Nephalia_s_Scourge_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
