# Blueprint — Marchesa, the Black Rose

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/marchesa-the-black-rose.md), state `SOURCE_BASELINE`, list `lh1:ff7464ce79627be5…`). Machine-readable source: [`data/grixis/blueprints/marchesa-the-black-rose.json`](../../data/grixis/blueprints/marchesa-the-black-rose.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Marchesa, the Black Rose** — Legendary Creature — Human Wizard

> Dethrone (Whenever this creature attacks the player with the most life or tied for most life, put a +1/+1 counter on it.)  
> Other creatures you control have dethrone.  
> Whenever a creature you control with a +1/+1 counter on it dies, return that card to the battlefield under your control at the beginning of the next end step.

## Plan and commander role

- **Primary plan:** +1/+1-counter aristocrats: put counters on creatures (dethrone, Thran Vigil, Metallic Mimic, Forge of Heroes), sacrifice them for mana, cards and damage, let Marchesa return countered creatures at end step, and use counters to reset persist creatures into sacrifice loops. *strategic_judgment · high*
- **Secondary:** Drain payoffs (Blood Artist, Mayhem Devil, Gray Merchant, Syr Konrad, Grave Pact) and Sneak Attack/Imperial Recruiter to find loop pieces.
  - Evidence: [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md)
- **Commander role: significant.** Marchesa gives the team dethrone and returns any countered creature that dies, which makes the sacrifice engine resilient. *strategic_judgment · high*
- ⚠️ **Honest note:** The source calls the closes 'commander-native loops' (decisions L16), but none of the 48 Spellbook infinites in the list needs Marchesa: they're persist/undying loops with Thran Vigil, Metallic Mimic, Gev, Uncivil Unrest or Mikaeus plus an outlet. She's a resilience engine, not the kill. No M1 interaction review exists yet for this deck.
  - Evidence: [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md) · `spellbook:2131-2292--5` · `spellbook:628-2034--5`
- **Dependency level:** low *strategic_judgment · high* — `spellbook:2131-2292--5`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions).) | *fact · verified* | [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling, high end: dozens of two- and three-card sacrifice infinites with tutors, but board-based and graveyard-reliant. Agrees with the source.) | *strategic_judgment · high* | [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md) · `spellbook:2131-2292--5` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Marchesa__the_Black_Rose` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 41, "2": 1491, "3": 1509, "4": 474, "5": 15}, "decks_with_bracket": 3530, "share_b4_plus": 0.139, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__marchesa-the-black-rose.json`

## Win conditions

- **persist-reset-loops** (combo): A persist creature plus a counter source (Thran Vigil, Metallic Mimic, Gev, Uncivil Unrest) and a sacrifice outlet loops for unbounded death triggers; Murderous Redcap or Goblin Bombardment kills. Cards: Thran Vigil, Metallic Mimic, Gev, Scaled Scorch, Uncivil Unrest, Murderous Redcap, Viscera Seer, Ashnod's Altar, Goblin Bombardment, Carrion Feeder, Altar of Dementia. *fact · verified* — `spellbook:2131-2292--5` · `spellbook:2034-2131--5` · `spellbook:345-2034--5` · `spellbook:345-1657` · `spellbook:1657-5805` · `spellbook:1657-5961` · `spellbook:2034-5805--5` · `spellbook:2034-5961--5` · `spellbook:5147-5805--5` · `spellbook:5147-5961--5`
- **mikaeus-loops** (combo): Mikaeus, the Unhallowed with a sacrifice outlet loops undying creatures; with Blood Artist/Warren Soultrader, Sage of Fables or Yawgmoth + Gray Merchant. Cards: Mikaeus, the Unhallowed, Ashnod's Altar, Viscera Seer, Goblin Bombardment, Blood Artist, Warren Soultrader, Sage of Fables, Gray Merchant of Asphodel. *fact · verified* — `spellbook:628-2034--5` · `spellbook:628-2292--5` · `spellbook:628-5147--5` · `spellbook:628-2842-5670--5` · `spellbook:628-2034-4866` · `spellbook:328-628-4279`
- **spark-double-loops** (combo): Spark Double copies of persist creatures, or Flayer of the Hatebound + Sage of Fables, with an Altar. Cards: Spark Double, Murderous Redcap, Glen Elendra Archmage, River Kelpie, Puppeteer Clique, Flayer of the Hatebound, Sage of Fables, Ashnod's Altar, Altar of Dementia. *fact · verified* — `spellbook:1657-2034-3908` · `spellbook:2034-2831-3908` · `spellbook:2034-3607-3908` · `spellbook:3020-3908-5256` · `spellbook:1123-2034-4866`

## Engines

- **dethrone-return:** Marchesa, the Black Rose, Thran Vigil, Metallic Mimic, Forge of Heroes, The Ozolith. Online when: Countered creatures dying with Marchesa in play. *fact · high* — `oracle:Marchesa, the Black Rose` · [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md)
- **sac-value:** Phyrexian Altar, Ashnod's Altar, Goblin Bombardment, Viscera Seer, Carrion Feeder, Altar of Dementia, Skullclamp, Pitiless Plunderer, Grim Haruspex. Online when: Sacrifice outlet and fodder. *strategic_judgment · high* — [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:sac-outlets` | yes | 7 | Free or cheap outlets for the loops. | 8: Phyrexian Altar, Ashnod's Altar, Goblin Bombardment, Viscera Seer, Carrion Feeder, Altar of Dementia, Phyrexian Tower, Yahenni, Undying Partisan | — | *strategic_judgment · high* | [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md) |
| `pkg:persist-undying` | yes | 5 | Creatures that come back with counters. | 6: Murderous Redcap, Glen Elendra Archmage, River Kelpie, Puppeteer Clique, Flayer of the Hatebound, Twilight Diviner | — | *strategic_judgment · high* | `spellbook:2131-2292--5` |
| `pkg:drain-payoffs` | yes | 5 | Turn deaths into damage and value. | 6: Blood Artist, Mayhem Devil, Gray Merchant of Asphodel, Syr Konrad, the Grim, Grave Pact, Warren Soultrader | — | *strategic_judgment · high* | [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md) |

## Key interactions

- **counter-return:** Only creatures with a +1/+1 counter return, at the next end step, under your control. (Marchesa, the Black Rose) *fact · high* — `oracle:Marchesa, the Black Rose`
- **dethrone-team:** Dethrone on the team only triggers attacking the player with the most life. (Marchesa, the Black Rose) *fact · high* — `oracle:Marchesa, the Black Rose` · `cr:702.105a`
- **persist-reset:** A +1/+1 counter cancels a -1/-1 counter, so persist can trigger again. (Thran Vigil, Metallic Mimic, Murderous Redcap) *fact · high* — `cr:702.79a` · `spellbook:2131-2292--5`
- **yawgmoth-gary:** Mikaeus + Yawgmoth + Gray Merchant is an infinite drain. (Mikaeus, the Unhallowed, Gray Merchant of Asphodel) *fact · high* — `spellbook:328-628-4279`

## Tutors and recursion

- Tutor target **Thran Vigil** via Demonic Tutor, Vampiric Tutor, Diabolic Intent *strategic_judgment · high* — `spellbook:2131-2292--5`
- Tutor target **Murderous Redcap** via Imperial Recruiter *strategic_judgment · moderate* — `spellbook:1657-5805`
- Recursion: Marchesa, the Black Rose, Reanimate, Victimize, Sneak Attack *strategic_judgment · moderate* — [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Fierce Guardianship, Flare of Denial, An Offer You Can't Refuse, Toxic Deluge, Blasphemous Act, Cyclonic Rift.
- **Protection:** Lightning Greaves, counters.
- **Mana:** Sol Ring, Ancient Tomb, Talismans, sacrifice mana.
- *strategic_judgment · moderate* — [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md)

## Failure modes

- **graveyard-exile:** Exile removal and graveyard hate stop persist and Marchesa returns. Mitigations: Many redundant loops. *strategic_judgment · high* — [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md)
- **marchesa-removed:** Losing Marchesa removes dethrone and recursion. Mitigations: Commander-free loops. *strategic_judgment · moderate* — `oracle:Marchesa, the Black Rose`
- **counter-hate:** Counter removal or -1/-1 effects disrupt the resets. Mitigations: Multiple counter sources. *strategic_judgment · moderate* — [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md)

## Identity core

- **Marchesa, the Black Rose:** Team dethrone and end-step return for countered creatures. *fact · verified* — `oracle:Marchesa, the Black Rose`
- **Thran Vigil:** Counter source that turns persist creatures into loops. *strategic_judgment · high* — `spellbook:2131-2292--5`
- **Murderous Redcap:** Persist damage creature at the centre of the kills. *strategic_judgment · high* — `spellbook:1657-5805`
- **Mikaeus, the Unhallowed:** Undying for the team. *strategic_judgment · high* — `spellbook:628-2034--5`
- **Phyrexian Altar:** Free outlet that makes mana. *strategic_judgment · moderate* — [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No generic Grixis combo shell; close through counter/sacrifice loops (decisions L16).
- ✗ Cut Village Rites, Black Market Connections and others for loop and tutor density (decisions swaps).
  - *strategic_judgment · high* — [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md)
- Theme: The Black Rose's dethrone and death-and-return aristocrats.
  - *strategic_judgment · moderate* — [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.79a:** Persist. *fact · verified* — `cr:702.79a`
- **CR 704.5q:** +1/+1 and -1/-1 counters annihilate. *fact · verified* — `cr:704.5q`

## Supporting features (heuristic, not identity)

- `{"hooks": ["+1/+1 counters", "combat damage / attack triggers", "graveyard as a resource"], "hooked_cards": 24, "role_counts": {"counter": 4, "draw": 11, "protection": 1, "ramp": 11, "removal": 5, "tutor": 4, "wipe": 2}, "lands": 34, "edhrec_pages": ["marchesa-the-black-rose"]}` *heuristic · low*

## Provenance

- Seeded from: [Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Current_Cycle_Decisions_2026-10-15.md) · [Marchesa_the_Black_Rose_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Marchesa_the_Black_Rose_Approved_2026-10-15.md) · [Marchesa_the_Black_Rose_Whole_List_Audit_2026-10-15.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Marchesa_the_Black_Rose_Whole_List_Audit_2026-10-15.csv) · [Marchesa_the_Black_Rose_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Marchesa_the_Black_Rose_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
