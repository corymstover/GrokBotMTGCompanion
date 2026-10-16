# Blueprint — Evelyn, the Covetous

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/evelyn-the-covetous.md), state `SOURCE_BASELINE`, list `lh1:94c3b2c4114887f0…`). Machine-readable source: [`data/grixis/blueprints/evelyn-the-covetous.json`](../../data/grixis/blueprints/evelyn-the-covetous.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Evelyn, the Covetous** — Legendary Creature — Vampire Rogue

> Flash  
> Whenever Evelyn or another Vampire you control enters, exile the top card of each player's library with a collection counter on it.  
> Once each turn, you may play a card from exile with a collection counter on it if it was exiled by an ability you controlled, and you may spend mana as though it were mana of any color to cast it.

## Plan and commander role

- **Primary plan:** cEDH turbo/midrange: fast mana, tutors and dense free interaction toward Worldgorger Dragon + a reanimation Aura (unbounded mana, repeated Evelyn exile triggers), Thassa's Oracle + Consultation/Tainted Pact, or Underworld Breach + LED/Petal + Brain Freeze. *strategic_judgment · high*
- **Secondary:** Evelyn as a flash value engine: each entry exiles the top card of every library and she plays one per turn, with Leyline of Anticipation and Valley Floodcaller letting her work on opponents' turns.
  - Evidence: [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md) · [evelyn-03](../interactions/evelyn-the-covetous.md#evelyn-03-worldgorger-dragon--animate-dead--dance-of-the-dead--necromancy) · [evelyn-06](../interactions/evelyn-the-covetous.md#evelyn-06-thassas-oracle--demonic-consultation-or-tainted-pact) · [evelyn-07](../interactions/evelyn-the-covetous.md#evelyn-07-underworld-breach--lions-eye-diamond--lotus-petal--brain-freeze)
- **Commander role: significant.** Flash card advantage, and a Worldgorger loop that repeatedly re-triggers her exile. *strategic_judgment · high*
- ⚠️ **Honest note:** All three proven win lines (Worldgorger + Aura for mana, Oracle + Consultation/Pact, Breach + LED + Brain Freeze) work without Evelyn; the Evelyn-specific Worldgorger-into-Oracle line is rated uncertain in M1 (evelyn-05). Evelyn is the only Vampire left, so her 'another Vampire' clause is dead text: the source traded the Vampire identity for a generic Grixis cEDH shell.
  - Evidence: [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md) · [evelyn-05](../interactions/evelyn-the-covetous.md#evelyn-05-worldgorger--evelyn--thassas-oracle) · [evelyn-03](../interactions/evelyn-the-covetous.md#evelyn-03-worldgorger-dragon--animate-dead--dance-of-the-dead--necromancy)
- **Dependency level:** low *strategic_judgment · high* — [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md) · [evelyn-03](../interactions/evelyn-the-covetous.md#evelyn-03-worldgorger-dragon--animate-dead--dance-of-the-dead--necromancy)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (Bracket 5 — cEDH / fringe-competitive (decisions §2).) | *fact · verified* | [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 5 (Bracket 5 ceiling: proven cEDH win packages and tournament results (48 entries, 10 top cuts per the source). Agrees with the source; note the power comes mostly from generic packages, not from Evelyn.) | *strategic_judgment · high* | [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md) · `spellbook:4812-4846` |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Evelyn__the_Covetous` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 20, "2": 522, "3": 305, "4": 108, "5": 100}, "decks_with_bracket": 1055, "share_b4_plus": 0.197, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__evelyn-the-covetous.json`

## Win conditions

- **worldgorger** (combo): Worldgorger Dragon + Animate Dead/Dance of the Dead/Necromancy: unbounded mana, with a creature in a graveyard as the exit into a win. Cards: Worldgorger Dragon, Animate Dead, Dance of the Dead, Necromancy. Enablers: Entomb, Unmarked Grave, Faithless Looting, Evelyn, the Covetous. *fact · verified* — `spellbook:4812-4846` · `spellbook:3605-4846` · `spellbook:2896-4846` · [evelyn-03](../interactions/evelyn-the-covetous.md#evelyn-03-worldgorger-dragon--animate-dead--dance-of-the-dead--necromancy) · [evelyn-04](../interactions/evelyn-the-covetous.md#evelyn-04-the-worldgorger-loop-is-mandatory-have-a-way-out)
- **oracle** (combo): Thassa's Oracle with Demonic Consultation or Tainted Pact. Cards: Thassa's Oracle, Demonic Consultation, Tainted Pact. *fact · verified* — `spellbook:742-1295` · `spellbook:1295-3093` · [evelyn-06](../interactions/evelyn-the-covetous.md#evelyn-06-thassas-oracle--demonic-consultation-or-tainted-pact)
- **breach-brain-freeze** (combo): Underworld Breach with Lion's Eye Diamond or Lotus Petal loops Brain Freeze to mill the table. Cards: Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze. *fact · verified* — `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856` · [evelyn-07](../interactions/evelyn-the-covetous.md#evelyn-07-underworld-breach--lions-eye-diamond--lotus-petal--brain-freeze)

## Engines

- **collection-exile:** Evelyn, the Covetous, Leyline of Anticipation, Valley Floodcaller, Party Thrasher. Online when: Evelyn enters; one play from exile each turn. *fact · verified* — [evelyn-01](../interactions/evelyn-the-covetous.md#evelyn-01-one-play-per-turn-from-any-evelyns-exile) · [evelyn-02](../interactions/evelyn-the-covetous.md#evelyn-02-flash-enablers-use-evelyn-on-opponents-turns)
- **fast-mana-tutors:** Mana Vault, Chrome Mox, Mox Diamond, Lotus Petal, Dark Ritual, Demonic Tutor, Vampiric Tutor, Imperial Seal, Necropotence, Ad Nauseam. Online when: Opening hand. *strategic_judgment · high* — [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:worldgorger` | yes | 5 | Dragon, Auras and discard/entomb setup. | 7: Worldgorger Dragon, Animate Dead, Dance of the Dead, Necromancy, Entomb, Unmarked Grave, Faithless Looting | — | *strategic_judgment · high* | [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md) · [evelyn-03](../interactions/evelyn-the-covetous.md#evelyn-03-worldgorger-dragon--animate-dead--dance-of-the-dead--necromancy) |
| `pkg:free-interaction` | yes | 8 | Stack protection at cEDH speed. | 11: Force of Will, Force of Negation, Pact of Negation, Mental Misstep, Mindbreak Trap, Flusterstorm, Swan Song, An Offer You Can't Refuse, Pyroblast, Red Elemental Blast, Stifle | — | *strategic_judgment · high* | [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:tutors` | yes | 6 | Find a combo half. | 8: Demonic Tutor, Vampiric Tutor, Imperial Seal, Mystical Tutor, Wishclaw Talisman, Gamble, Demonic Consultation, Tainted Pact | — | *strategic_judgment · high* | [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md) |

## Key interactions

- **one-play:** One collection-counter play per turn across all Evelyns. (Evelyn, the Covetous) *fact · verified* — [evelyn-01](../interactions/evelyn-the-covetous.md#evelyn-01-one-play-per-turn-from-any-evelyns-exile)
- **mandatory-loop:** The Worldgorger loop is mandatory: without an exit it's a draw. (Worldgorger Dragon) *fact · verified* — [evelyn-04](../interactions/evelyn-the-covetous.md#evelyn-04-the-worldgorger-loop-is-mandatory-have-a-way-out)
- **evelyn-oracle:** Worldgorger + Evelyn into Thassa's Oracle from exile is plausible but rated uncertain. (Worldgorger Dragon, Evelyn, the Covetous, Thassa's Oracle) *fact · verified* — [evelyn-05](../interactions/evelyn-the-covetous.md#evelyn-05-worldgorger--evelyn--thassas-oracle)
- **bauble-self:** Vexing Bauble also counters your own free LED/Petal escapes. (Vexing Bauble, Lion's Eye Diamond) *fact · verified* — [evelyn-08](../interactions/evelyn-the-covetous.md#evelyn-08-vexing-bauble-counters-your-own-free-spells-including-escaped-led-and-petal)
- **saw-commander:** Saw in Half on Evelyn: she dies, you get two token copies and their triggers. (Saw in Half, Evelyn, the Covetous) *fact · verified* — [evelyn-09](../interactions/evelyn-the-covetous.md#evelyn-09-saw-in-half-on-evelyn-the-commander-rule-no-longer-prevents-dying)

## Tutors and recursion

- Tutor target **Worldgorger Dragon** via Entomb, Demonic Tutor *strategic_judgment · high* — `spellbook:4812-4846`
- Tutor target **Thassa's Oracle** via Demonic Tutor, Vampiric Tutor, Imperial Seal *strategic_judgment · high* — `spellbook:742-1295`
- Tutor target **Underworld Breach** via Demonic Tutor, Gamble *strategic_judgment · moderate* — `spellbook:1368-3518-4856`
- Recursion: Animate Dead, Necromancy, Dance of the Dead, Reanimate, Underworld Breach *strategic_judgment · high* — [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Free counters and one-mana stack interaction.
- **Protection:** Defense Grid, Spellskite, the counter suite.
- **Mana:** Premium fast mana and rituals; 5-mana flash commander.
- *strategic_judgment · high* — [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **no-exit:** Worldgorger loop with no creature to break it is a forced draw. Mitigations: Keep a second creature in the yard; Thassa's Oracle exit. *strategic_judgment · high* — [evelyn-04](../interactions/evelyn-the-covetous.md#evelyn-04-the-worldgorger-loop-is-mandatory-have-a-way-out)
- **graveyard-hate:** Graveyard hate stops Worldgorger and Breach. Mitigations: Thassa's Oracle + Consultation; Bounce/remove hate. *strategic_judgment · high* — [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md)
- **own-bauble:** Your own Vexing Bauble blocks free combo spells. Mitigations: Crack it first. *strategic_judgment · moderate* — [evelyn-08](../interactions/evelyn-the-covetous.md#evelyn-08-vexing-bauble-counters-your-own-free-spells-including-escaped-led-and-petal)

## Identity core

- **Evelyn, the Covetous:** Flash exile engine with one play per turn. *fact · verified* — `oracle:Evelyn, the Covetous`
- **Worldgorger Dragon:** The commander-flavoured combo: loops re-trigger Evelyn. *strategic_judgment · high* — [evelyn-03](../interactions/evelyn-the-covetous.md#evelyn-03-worldgorger-dragon--animate-dead--dance-of-the-dead--necromancy)
- **Leyline of Anticipation:** Flash for everything, so Evelyn plays on opponents' turns. *strategic_judgment · high* — [evelyn-02](../interactions/evelyn-the-covetous.md#evelyn-02-flash-enablers-use-evelyn-on-opponents-turns)
- **Saw in Half:** Kills Evelyn into two token copies and four triggers. *strategic_judgment · high* — [evelyn-09](../interactions/evelyn-the-covetous.md#evelyn-09-saw-in-half-on-evelyn-the-commander-rule-no-longer-prevents-dying)
- **Party Thrasher:** Gives Evelyn's casts convoke and loots. *strategic_judgment · moderate* — [evelyn-10](../interactions/evelyn-the-covetous.md#evelyn-10-party-thrasher-gives-evelyn-casts-convoke)

## Anti-goals and thematic constraints

- ✗ Don't rebuild the Vampire/ETB value shell; the source judged it below the commander's ceiling (decisions §2).
- ✗ Keep combo exits in the list: the Worldgorger loop can't be left unbroken.
  - *strategic_judgment · high* — [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Theme subordinate to cEDH: the Vampire identity is gone (Evelyn is the only Vampire).
  - *strategic_judgment · high* — [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 104.4b:** An unbreakable mandatory loop is a draw. *fact · verified* — `cr:104.4b`
- **CR 702.8a:** Flash. *fact · verified* — `cr:702.8a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Vampire synergy", "enters triggers", "playing cards from exile"], "hooked_cards": 10, "role_counts": {"counter": 11, "draw": 11, "protection": 1, "ramp": 17, "removal": 5, "tutor": 8, "wipe": 2}, "lands": 26, "edhrec_pages": ["evelyn-the-covetous"]}` *heuristic · low*

## Provenance

- Seeded from: [Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Evelyn_the_Covetous_Current_Cycle_Decisions_2026-10-14.md) · [Evelyn_the_Covetous_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Evelyn_the_Covetous_Approved_2026-10-14.md) · [Evelyn_the_Covetous_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Evelyn_the_Covetous_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
