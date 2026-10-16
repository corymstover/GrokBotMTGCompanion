# Blueprint — Davros, Dalek Creator

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/davros-dalek-creator.md), state `SOURCE_BASELINE`, list `lh1:ef9b2bd79878dfd9…`). Machine-readable source: [`data/grixis/blueprints/davros-dalek-creator.json`](../../data/grixis/blueprints/davros-dalek-creator.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Davros, Dalek Creator** — Legendary Artifact Creature — Alien Scientist

> Menace  
> At the beginning of your end step, create a 3/3 black Dalek artifact creature token with menace if an opponent lost 3 or more life this turn. Then each opponent who lost 3 or more life this turn faces a villainous choice — You draw a card, or that player discards a card.

## Plan and commander role

- **Primary plan:** Make every opponent lose 3+ life on your turn (Maestros Charm, Boltwave, Court of Ambition, Loyal Subordinate, Torment of Hailfire), so Davros's end-step trigger makes a 3/3 menace Dalek and forces a draw-or-discard villainous choice on each of them; multiply the trigger with Auton Soldier, Strionic Resonator, Scientist Supreme and The Valeyard. *strategic_judgment · high*
- **Secondary:** Punish the discard branch (Entropic Battlecruiser, Waste Not, Tinybones) and turn menace Daleks into a clock with Labyrinth Raptor and Dalek lords.
  - Evidence: [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md) · [davros-01](../interactions/davros-dalek-creator.md#davros-01-the-3-life-check-is-on-resolution-not-an-intervening-if) · [davros-05](../interactions/davros-dalek-creator.md#davros-05-the-valeyard-doubles-every-villainous-choice)
- **Commander role: central.** Davros is the repeatable value engine: Dalek every turn plus a card or a discard per qualifying opponent. *strategic_judgment · high*
- ⚠️ **Honest note:** Value-only engine with delayed payoff and opponent choice; no Spellbook combos. The deck is Bracket 4 mainly because of its Game Changers and premium interaction, not because Davros threatens fast wins.
  - Evidence: [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md) · [davros-01](../interactions/davros-dalek-creator.md#davros-01-the-3-life-check-is-on-resolution-not-an-intervening-if) · [davros-02](../interactions/davros-dalek-creator.md#davros-02-villainous-choices-resolve-player-by-player)
- **Dependency level:** high *strategic_judgment · high* — [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Bracket 4 — Optimized (current-cycle decisions).) | *fact · verified* | [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md) · [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md#L94](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Low-end Bracket 4: forced there by Game Changers and premium interaction; the engine itself is fair value with no combo. Agrees with the source.) | *strategic_judgment · moderate* | [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md) · [davros-01](../interactions/davros-dalek-creator.md#davros-01-the-3-life-check-is-on-resolution-not-an-intervening-if) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Davros__Dalek_Creator` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 22, "2": 818, "3": 611, "4": 100, "5": 9}, "decks_with_bracket": 1560, "share_b4_plus": 0.07, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__davros-dalek-creator.json`

## Win conditions

- **dalek-army** (natural): Menace Dalek tokens every turn, pumped and protected, with Labyrinth Raptor forcing bad blocks. Cards: Davros, Dalek Creator, Labyrinth Raptor, The Dalek Emperor, Genesis of the Daleks, Dalek Squadron. Enablers: Loyal Subordinate. *strategic_judgment · high* — [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md)
- **drain-and-discard** (natural): Entropic Battlecruiser and Court of Ambition make each discard cost 3 life; Torment of Hailfire and Exterminate! close. Cards: Entropic Battlecruiser, Court of Ambition, Torment of Hailfire, Exterminate!, Wound Reflection. Enablers: Geier Reach Sanitarium. *strategic_judgment · moderate* — [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md) · [davros-06](../interactions/davros-dalek-creator.md#davros-06-entropic-battlecruiser-at-station-1-punishes-discards)

## Engines

- **end-step-davros:** Davros, Dalek Creator, Auton Soldier, Strionic Resonator, Scientist Supreme of A.I.M., Roaming Throne, The Valeyard. Online when: At least one opponent lost 3+ life this turn when the trigger resolves. *fact · verified* — [davros-01](../interactions/davros-dalek-creator.md#davros-01-the-3-life-check-is-on-resolution-not-an-intervening-if) · [davros-04](../interactions/davros-dalek-creator.md#davros-04-copying-and-doubling-davros) · [davros-05](../interactions/davros-dalek-creator.md#davros-05-the-valeyard-doubles-every-villainous-choice)
- **three-life-enablers:** Maestros Charm, Boltwave, Court of Ambition, Loyal Subordinate, Sygg, River Cutthroat. Online when: Fixed 3-life loss to each opponent during your turn. *fact · verified* — [davros-07](../interactions/davros-dalek-creator.md#davros-07-fixed-3-life-enablers)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:three-life-enablers` | yes | 6 | Turn on Davros for the whole table. | 8: Maestros Charm, Boltwave, Court of Ambition, Loyal Subordinate, Torment of Hailfire, Exterminate!, Perforating Artist, Wound Reflection | — | *strategic_judgment · high* | [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md) · [davros-07](../interactions/davros-dalek-creator.md#davros-07-fixed-3-life-enablers) |
| `pkg:trigger-multipliers` | yes | 4 | More Davros triggers or choices. | 5: Auton Soldier, Strionic Resonator, Scientist Supreme of A.I.M., Roaming Throne, The Valeyard | — | *strategic_judgment · high* | [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md) · [davros-04](../interactions/davros-dalek-creator.md#davros-04-copying-and-doubling-davros) |
| `pkg:discard-punishers` | yes | 3 | Make the discard branch hurt. | 5: Entropic Battlecruiser, Waste Not, Tinybones, Trinket Thief, Geth's Grimoire, Sycorax Commander | — | *strategic_judgment · high* | [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:interaction-protection` | yes | 10 | Bracket 4 interaction and commander protection. | 13: Counterspell, Mana Drain, Swan Song, Fierce Guardianship, Deflecting Swat, Snuff Out, Deadly Rollick, Delete, Toxic Deluge, Cyclonic Rift, Lightning Greaves, Swiftfoot Boots, Padeem, Consul of Innovation | — | *strategic_judgment · high* | [Davros_Dalek_Creator_Whole_List_Audit_Closeout_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Whole_List_Audit_Closeout_2026-10-14.md) |

## Key interactions

- **check-on-resolution:** Always triggers; the 3-life check is on resolution, not an intervening if. (Davros, Dalek Creator) *fact · verified* — [davros-01](../interactions/davros-dalek-creator.md#davros-01-the-3-life-check-is-on-resolution-not-an-intervening-if)
- **order-drains:** Put Davros's trigger on the stack first so end-step drains resolve before it. (Davros, Dalek Creator) *fact · verified* — [davros-03](../interactions/davros-dalek-creator.md#davros-03-order-end-step-drains-above-davros)
- **valeyard:** The Valeyard doubles every villainous choice. (The Valeyard) *fact · verified* — [davros-05](../interactions/davros-dalek-creator.md#davros-05-the-valeyard-doubles-every-villainous-choice)
- **battlecruiser:** Entropic Battlecruiser at station 1+ makes each discard cost 3 life. (Entropic Battlecruiser) *fact · verified* — [davros-06](../interactions/davros-dalek-creator.md#davros-06-entropic-battlecruiser-at-station-1-punishes-discards)
- **raptor:** Labyrinth Raptor punishes blocks on menace Daleks. (Labyrinth Raptor) *fact · verified* — [davros-08](../interactions/davros-dalek-creator.md#davros-08-labyrinth-raptor-and-menace-daleks)

## Tutors and recursion

- Tutor target **The Valeyard** via Demonic Tutor *strategic_judgment · moderate* — [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md)
- Tutor target **Entropic Battlecruiser** via Demonic Tutor *strategic_judgment · moderate* — [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md)
- Recursion: Geth's Grimoire *strategic_judgment · low* — [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Strong: 13 interaction pieces including free counters and sweepers.
- **Protection:** Greaves, Boots, Padeem (artifact), Plaza of Heroes.
- **Mana:** Four-mana commander; fixing upgrades (City of Brass, Mana Confluence).
- *strategic_judgment · moderate* — [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md) · [Davros_Dalek_Creator_Whole_List_Audit_Closeout_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Whole_List_Audit_Closeout_2026-10-14.md)

## Failure modes

- **threshold-missed:** No opponent at 3 life lost this turn: the trigger does nothing. Mitigations: Fixed 3-life enablers. *strategic_judgment · high* — [davros-01](../interactions/davros-dalek-creator.md#davros-01-the-3-life-check-is-on-resolution-not-an-intervening-if)
- **opponents-choose:** Opponents pick the cheaper branch every time. Mitigations: Discard punishers make both branches cost something. *strategic_judgment · moderate* — [davros-02](../interactions/davros-dalek-creator.md#davros-02-villainous-choices-resolve-player-by-player)
- **slow-clock:** Value without a kill: games go long. Mitigations: Torment of Hailfire; Labyrinth Raptor. *strategic_judgment · moderate* — [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md)

## Identity core

- **Davros, Dalek Creator:** Dalek and villainous choice every end step. *fact · verified* — `oracle:Davros, Dalek Creator`
- **Maestros Charm:** Instant 3 life from every opponent: turns Davros on for the full table. *strategic_judgment · high* — [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md)
- **Court of Ambition:** Upkeep 3-life-or-discard for each opponent; both branches feed Davros. *strategic_judgment · high* — [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md)
- **Entropic Battlecruiser:** Converts discard choices into 3-life losses. *strategic_judgment · high* — [davros-06](../interactions/davros-dalek-creator.md#davros-06-entropic-battlecruiser-at-station-1-punishes-discards)
- **The Valeyard:** Doubles every villainous choice. *strategic_judgment · moderate* — [davros-05](../interactions/davros-dalek-creator.md#davros-05-the-valeyard-doubles-every-villainous-choice)

## Anti-goals and thematic constraints

- ✗ Don't drift into generic Grixis artifacts or generic discard.
- ✗ Don't add opponent-upkeep effects (The Rack, Bottomless Pit) that don't help on your turn (source cuts).
  - *strategic_judgment · high* — [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Doctor Who Daleks.
  - *strategic_judgment · high* — [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.55a:** Villainous choice: the opponent chooses, then all of that option happens. *fact · verified* — `cr:701.55a`
- **CR 603.4:** Davros has no intervening if: it always triggers and checks on resolution. *fact · verified* — `cr:603.4`

## Supporting features (heuristic, not identity)

- `{"hooks": ["artifacts", "discard", "opponents losing life", "tokens", "villainous choices / voting"], "hooked_cards": 50, "role_counts": {"counter": 4, "draw": 8, "protection": 4, "ramp": 9, "removal": 8, "tutor": 1, "wipe": 4}, "lands": 34, "edhrec_pages": ["davros-dalek-creator"]}` *heuristic · low*

## Provenance

- Seeded from: [Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Davros_Dalek_Creator_Current_Cycle_Decisions_2026-10-14.md) · [Davros_Dalek_Creator_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Davros_Dalek_Creator_Approved_2026-10-14.md) · [Davros_Dalek_Creator_Whole_List_Audit_Closeout_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/davros_dalek_creator_2026-10-14/Davros_Dalek_Creator_Whole_List_Audit_Closeout_2026-10-14.md) · [Davros_Dalek_Creator_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Davros_Dalek_Creator_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
