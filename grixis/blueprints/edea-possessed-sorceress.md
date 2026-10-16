# Blueprint — Edea, Possessed Sorceress

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/edea-possessed-sorceress.md), state `SOURCE_BASELINE`, list `lh1:d6ca08555bc66faf…`). Machine-readable source: [`data/grixis/blueprints/edea-possessed-sorceress.json`](../../data/grixis/blueprints/edea-possessed-sorceress.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Edea, Possessed Sorceress** — Legendary Creature — Human Warlock

> Ward {2}  
> At the beginning of combat on your turn, gain control of target creature an opponent controls until end of turn. Untap that creature. It gains haste until end of turn.  
> Whenever a creature you control but don't own dies, return it to the battlefield under its owner's control and you draw a card.

## Plan and commander role

- **Primary plan:** Borrow an opponent's best creature every combat, swing with it, then sacrifice it before cleanup: Edea returns it to its owner and draws you a card while your sacrifice payoffs (Goblin Bombardment, Mayhem Devil, Grave Pact) fire. *strategic_judgment · high*
- **Secondary:** Multiply the theft (Mass Mutiny, Insurrection, Captivating Crew, extra combats, Edea copies) and convert temporary theft into permanent value (Thassa, Nightmare Shepherd, Black Crystal, Saw in Half, Impostor Syndrome).
  - Evidence: [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md#L10](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md) · [edea-02](../interactions/edea-possessed-sorceress.md#edea-02-a-borrowed-creature-that-dies-goes-back-to-its-owner-and-you-draw) · [edea-06](../interactions/edea-possessed-sorceress.md#edea-06-thassa-turns-a-temporary-steal-into-a-permanent-one)
- **Commander role: central.** Edea is the only repeatable source of free theft and the card-draw half of every sacrifice. *strategic_judgment · high*
- ⚠️ **Honest note:** She steals at beginning of combat on your turn only, needs a worthwhile target on an opposing board, and her draw clause needs the borrowed creature to die while you control it. Against creature-light tables the engine is weak.
  - Evidence: [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md) · [edea-01](../interactions/edea-possessed-sorceress.md#edea-01-the-combat-steal-is-targeted-arcane-lighthouse-handles-hexproof) · [edea-02](../interactions/edea-possessed-sorceress.md#edea-02-a-borrowed-creature-that-dies-goes-back-to-its-owner-and-you-draw)
- **Dependency level:** high *strategic_judgment · high* — [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Bracket 4 — Optimized (decisions natural ceiling).) | *fact · verified* | [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: strong multiplayer value and tempo engine with no compact two-card win; five-mana, board-dependent commander. Agrees with the source.) | *strategic_judgment · high* | [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md) · [edea-02](../interactions/edea-possessed-sorceress.md#edea-02-a-borrowed-creature-that-dies-goes-back-to-its-owner-and-you-draw) |
| Expected bracket (list as built) | 4 (computed floor 3) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Edea__Possessed_Sorceress` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 5, "2": 276, "3": 448, "4": 71, "5": 3}, "decks_with_bracket": 803, "share_b4_plus": 0.092, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__edea-possessed-sorceress.json`

## Win conditions

- **sac-drain** (natural): Sacrifice outlets plus damage payoffs turn every borrowed body, token and Treasure into damage while Edea refills. Cards: Goblin Bombardment, Mayhem Devil, Grave Pact, Pitiless Plunderer. Enablers: Edea, Possessed Sorceress, Viscera Seer, Phyrexian Altar, Ashnod's Altar. *strategic_judgment · high* — [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md)
- **mass-theft-swing** (natural): Mass theft (Insurrection, Mass Mutiny, Mob Rule) swings opposing boards at their owners, then everything is sacrificed for value. Cards: Insurrection, Mass Mutiny, Mob Rule, Seize the Spotlight. Enablers: Goblin Bombardment, Ashnod's Altar. *strategic_judgment · moderate* — [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md) · [edea-10](../interactions/edea-possessed-sorceress.md#edea-10-more-borrowing-mass-mutiny-and-captivating-crew)

## Engines

- **borrow-and-sacrifice:** Edea, Possessed Sorceress, Viscera Seer, Phyrexian Altar, Ashnod's Altar, Goblin Bombardment, Phyrexian Tower. Online when: Edea in play with an opposing creature to borrow and a sacrifice outlet. *fact · verified* — [edea-02](../interactions/edea-possessed-sorceress.md#edea-02-a-borrowed-creature-that-dies-goes-back-to-its-owner-and-you-draw) · [edea-03](../interactions/edea-possessed-sorceress.md#edea-03-extra-death-triggers-only-draw)
- **extra-steals:** Spark Double, Sakashima of a Thousand Faces, Irma, Part-Time Mutant, Karlach, Fury of Avernus, Full Throttle, Roaming Throne, Strionic Resonator. Online when: A copy of Edea, an extra combat, or a beginning-of-combat trigger copier. *fact · verified* — [edea-04](../interactions/edea-possessed-sorceress.md#edea-04-edea-copies-spark-double-sakashima-irma) · [edea-05](../interactions/edea-possessed-sorceress.md#edea-05-extra-combats-mean-extra-steals)
- **keep-the-steal:** Thassa, Deep-Dwelling, Chaos Shrine's Black Crystal, Nightmare Shepherd, Saw in Half, Impostor Syndrome. Online when: A borrowed creature in play when the retention effect resolves. *fact · verified* — [edea-06](../interactions/edea-possessed-sorceress.md#edea-06-thassa-turns-a-temporary-steal-into-a-permanent-one) · [edea-07](../interactions/edea-possessed-sorceress.md#edea-07-black-crystal-vs-edea-order-the-triggers-to-keep-the-card) · [edea-08](../interactions/edea-possessed-sorceress.md#edea-08-nightmare-shepherd-first-gives-you-a-11-copy) · [edea-09](../interactions/edea-possessed-sorceress.md#edea-09-saw-in-half-on-a-borrowed-creature)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:extra-theft` | yes | 6 | More non-owned bodies than Edea alone provides. | 7: Insurrection, Mass Mutiny, Mob Rule, Captivating Crew, Dominus of Fealty, Seize the Spotlight, Zara, Renegade Recruiter | — | *strategic_judgment · high* | [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md) · [edea-10](../interactions/edea-possessed-sorceress.md#edea-10-more-borrowing-mass-mutiny-and-captivating-crew) |
| `pkg:sac-outlets` | yes | 6 | Free or cheap sacrifice before cleanup returns the creature. | 10: Viscera Seer, Phyrexian Altar, Ashnod's Altar, Goblin Bombardment, Phyrexian Tower, Village Rites, Deadly Dispute, Warren Soultrader, Braids, Arisen Nightmare, Evereth, Viceroy of Plunder | — | *strategic_judgment · high* | [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:multipliers` | yes | 5 | Copies of Edea, her trigger, or extra combats. | 7: Spark Double, Sakashima of a Thousand Faces, Irma, Part-Time Mutant, Karlach, Fury of Avernus, Full Throttle, Roaming Throne, Strionic Resonator | — | *strategic_judgment · high* | [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md) · [edea-04](../interactions/edea-possessed-sorceress.md#edea-04-edea-copies-spark-double-sakashima-irma) · [edea-05](../interactions/edea-possessed-sorceress.md#edea-05-extra-combats-mean-extra-steals) |

## Key interactions

- **targeted-steal:** The steal targets; Arcane Lighthouse answers hexproof/shroud. (Edea, Possessed Sorceress, Arcane Lighthouse) *fact · verified* — [edea-01](../interactions/edea-possessed-sorceress.md#edea-01-the-combat-steal-is-targeted-arcane-lighthouse-handles-hexproof)
- **return-and-draw:** A borrowed creature dying returns to its owner and you draw; the owner gets its enter triggers. (Edea, Possessed Sorceress) *fact · verified* — [edea-02](../interactions/edea-possessed-sorceress.md#edea-02-a-borrowed-creature-that-dies-goes-back-to-its-owner-and-you-draw)
- **extra-triggers-draw:** Extra Edea death triggers only draw; just one return happens. (Spark Double, Sakashima of a Thousand Faces) *fact · verified* — [edea-03](../interactions/edea-possessed-sorceress.md#edea-03-extra-death-triggers-only-draw)
- **thassa-keep:** Thassa's end-step blink returns the borrowed creature under your control permanently. (Thassa, Deep-Dwelling) *fact · verified* — [edea-06](../interactions/edea-possessed-sorceress.md#edea-06-thassa-turns-a-temporary-steal-into-a-permanent-one)
- **black-crystal-order:** Order Black Crystal's trigger first to keep the stolen card; Edea still draws. (Chaos Shrine's Black Crystal, Edea, Possessed Sorceress) *fact · verified* — [edea-07](../interactions/edea-possessed-sorceress.md#edea-07-black-crystal-vs-edea-order-the-triggers-to-keep-the-card)

## Tutors and recursion

- Tutor target **Goblin Bombardment** via Demonic Tutor, Diabolic Intent *strategic_judgment · moderate* — [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md)
- Tutor target **Insurrection** via Demonic Tutor *strategic_judgment · moderate* — [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md)
- Recursion: Reanimate, Victimize, Nightmare Shepherd *strategic_judgment · moderate* — [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Counters (Mana Drain, Fierce Guardianship, Swan Song, Arcane Denial) and resets (Toxic Deluge, Blasphemous Act).
- **Protection:** Ward {2}, Lightning Greaves, Deflecting Swat, Fierce Guardianship.
- **Mana:** Five-mana commander: Sol Ring, Ancient Tomb, Talismans, Arcane Signet.
- *strategic_judgment · moderate* — [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **no-targets:** Creature-light opponents leave nothing worth stealing. Mitigations: Treasure/token sacrifice still feeds payoffs; Seize the Spotlight. *strategic_judgment · high* — [edea-01](../interactions/edea-possessed-sorceress.md#edea-01-the-combat-steal-is-targeted-arcane-lighthouse-handles-hexproof)
- **edea-removed:** Five-mana commander removed: theft and draw stop. Mitigations: Ward {2}; Greaves; Counters. *strategic_judgment · high* — [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md)
- **gift-etb:** Returning the creature gives its owner its enter triggers again. Mitigations: Choose targets without strong ETBs; Thassa/Black Crystal to keep instead. *strategic_judgment · moderate* — [edea-02](../interactions/edea-possessed-sorceress.md#edea-02-a-borrowed-creature-that-dies-goes-back-to-its-owner-and-you-draw)

## Identity core

- **Edea, Possessed Sorceress:** Free combat theft plus a card whenever the borrowed creature dies. *fact · verified* — `oracle:Edea, Possessed Sorceress`
- **Thassa, Deep-Dwelling:** Turns a one-turn steal into a permanent one. *strategic_judgment · high* — [edea-06](../interactions/edea-possessed-sorceress.md#edea-06-thassa-turns-a-temporary-steal-into-a-permanent-one)
- **Goblin Bombardment:** Free outlet that also turns each borrowed body into damage. *strategic_judgment · high* — [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md)
- **Mass Mutiny:** Steals one creature from every opponent at once. *strategic_judgment · high* — [edea-10](../interactions/edea-possessed-sorceress.md#edea-10-more-borrowing-mass-mutiny-and-captivating-crew)
- **Chaos Shrine's Black Crystal:** Keeps the stolen creature's card for later. *strategic_judgment · moderate* — [edea-07](../interactions/edea-possessed-sorceress.md#edea-07-black-crystal-vs-edea-order-the-triggers-to-keep-the-card)

## Anti-goals and thematic constraints

- ✗ Don't drift into a generic aristocrats deck that only sacrifices its own creatures (source).
- ✗ No compact cEDH combo package; the source sets a commander-first B4 shell.
  - *strategic_judgment · high* — [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Final Fantasy VIII sorceress possessing others: theft, control and sacrifice.
  - *strategic_judgment · moderate* — [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 108.3:** Owner versus controller: Edea's return goes to the owner. *fact · verified* — `cr:108.3`
- **CR 702.21a:** Ward {2}. *fact · verified* — `cr:702.21a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["graveyard as a resource", "stealing / casting opponents' cards"], "hooked_cards": 9, "role_counts": {"counter": 5, "draw": 9, "protection": 2, "ramp": 14, "removal": 6, "tutor": 2, "wipe": 2}, "lands": 35, "edhrec_pages": ["edea-possessed-sorceress"]}` *heuristic · low*

## Provenance

- Seeded from: [Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edea_Possessed_Sorceress_Current_Cycle_Decisions_2026-10-14.md) · [Edea_Possessed_Sorceress_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Edea_Possessed_Sorceress_Approved_2026-10-14.md) · [Edea_Possessed_Sorceress_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Edea_Possessed_Sorceress_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
