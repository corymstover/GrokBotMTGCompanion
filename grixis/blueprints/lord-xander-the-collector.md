# Blueprint — Lord Xander, the Collector

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/lord-xander-the-collector.md), state `SOURCE_BASELINE`, list `lh1:84233c9153b8b1c8…`). Machine-readable source: [`data/grixis/blueprints/lord-xander-the-collector.json`](../../data/grixis/blueprints/lord-xander-the-collector.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Lord Xander, the Collector** — Legendary Creature — Vampire Demon Noble

> When Lord Xander enters, target opponent discards half the cards in their hand, rounded down.  
> Whenever Lord Xander attacks, defending player mills half their library, rounded down.  
> When Lord Xander dies, target opponent sacrifices half the nonland permanents they control of their choice, rounded down.

## Plan and commander role

- **Primary plan:** Xander trigger multiplication: reanimate or cheat out a seven-mana commander (Entomb + Reanimate/Animate Dead/Persist/Feign Death), copy him (Phantasmal Image, Spark Double, Sakashima, Blade of Selves, Helm of the Host, Hall of Echoes, Auton Soldier) and stack his discard-half, mill-half and sacrifice-half triggers. *strategic_judgment · high*
- **Secondary:** Finish the mill with Bruvac, Riverchurn Monument, Fraying Sanity or Maddening Cacophony; compact backups are Duskmantle Guildmage + Mindcrank, Sword of Feast and Famine + Aggravated Assault, and Breach lines.
  - Evidence: [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md) · [xander-01](../interactions/lord-xander-the-collector.md#xander-01-three-separate-triggers-enter-attack-dies) · [xander-05](../interactions/lord-xander-the-collector.md#xander-05-finishing-the-mill-bruvac-riverchurn-monument-fraying-sanity-maddening-cacophony)
- **Commander role: central.** Every copy, reanimation and mill-doubler exists to multiply Xander's three triggers, and his attack is half of two Spellbook infinites. *strategic_judgment · high*
- ⚠️ **Honest note:** Seven mana, so the deck relies on reanimation and clones to make him realistic. Halving rounds down, so an odd library leaves one card (M1 xander-05). Guildmage + Mindcrank, Monument/Bruvac + Cacophony, Sword + Assault and Breach all win without him.
  - Evidence: [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md) · [xander-05](../interactions/lord-xander-the-collector.md#xander-05-finishing-the-mill-bruvac-riverchurn-monument-fraying-sanity-maddening-cacophony) · [xander-11](../interactions/lord-xander-the-collector.md#xander-11-duskmantle-guildmage--mindcrank-and-the-breach-line)
- **Dependency level:** medium *strategic_judgment · high* — [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions).) | *fact · verified* | [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling, high end: premium fast mana and free counters with compact mill infinites, but a seven-mana commander and little cEDH evidence per the source. Agrees with the source.) | *strategic_judgment · high* | [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md) · `spellbook:95-1022` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Lord_Xander__the_Collector` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 8, "2": 200, "3": 253, "4": 185, "5": 14}, "decks_with_bracket": 660, "share_b4_plus": 0.302, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__lord-xander-the-collector.json`

## Win conditions

- **xander-mill** (combo): Xander's half-library mill with Bruvac or Riverchurn Monument (or Fraying Sanity) mills a player out. Cards: Lord Xander, the Collector, Bruvac the Grandiloquent, Riverchurn Monument, Fraying Sanity. Enablers: Hall of Echoes, Roaming Throne. *fact · verified* — `spellbook:95-1022` · `spellbook:1022-6285` · [xander-05](../interactions/lord-xander-the-collector.md#xander-05-finishing-the-mill-bruvac-riverchurn-monument-fraying-sanity-maddening-cacophony)
- **mill-combos** (combo): Duskmantle Guildmage + Mindcrank or Maddening Cacophony; Monument/Bruvac + Cacophony. Cards: Duskmantle Guildmage, Mindcrank, Maddening Cacophony, Riverchurn Monument, Bruvac the Grandiloquent. *fact · verified* — `spellbook:936-5069` · `spellbook:5069-5080` · `spellbook:5080-6285` · `spellbook:95-5080` · [xander-11](../interactions/lord-xander-the-collector.md#xander-11-duskmantle-guildmage--mindcrank-and-the-breach-line)
- **assault-breach** (combo): Sword of Feast and Famine + Aggravated Assault (each combat another Xander mill), or Breach lines. Cards: Sword of Feast and Famine, Aggravated Assault, Underworld Breach, Lion's Eye Diamond, Brain Freeze, Wheel of Fortune. Enablers: Lord Xander, the Collector. *fact · verified* — `spellbook:900-3750` · `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856` · `spellbook:1368-1878-2706` · `spellbook:1368-2706-3518` · [xander-10](../interactions/lord-xander-the-collector.md#xander-10-sword-of-feast-and-famine--aggravated-assault-extra-combats-extra-xander-mills) · [xander-11](../interactions/lord-xander-the-collector.md#xander-11-duskmantle-guildmage--mindcrank-and-the-breach-line)

## Engines

- **xander-copies:** Phantasmal Image, Spark Double, Sakashima of a Thousand Faces, Molten Duplication, Saw in Half, Blade of Selves, Helm of the Host, Hall of Echoes, Auton Soldier, Roaming Throne, Strionic Resonator. Online when: Xander in play or a copy target available. *fact · verified* — [xander-02](../interactions/lord-xander-the-collector.md#xander-02-clones-and-the-legend-rule-phantasmal-image-molten-duplication-saw-in-half) · [xander-03](../interactions/lord-xander-the-collector.md#xander-03-myriad-copies-blade-of-selves-vs-auton-soldier) · [xander-04](../interactions/lord-xander-the-collector.md#xander-04-hall-of-echoes-and-helm-of-the-host) · [xander-07](../interactions/lord-xander-the-collector.md#xander-07-roaming-throne-and-strionic-resonator)
- **reanimation:** Entomb, Reanimate, Animate Dead, Persist, Feign Death. Online when: Xander in the graveyard. *fact · verified* — [xander-08](../interactions/lord-xander-the-collector.md#xander-08-feign-death-on-your-commander-leave-it-in-the-graveyard)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:copy-trigger` | yes | 8 | Multiply Xander's own triggers. | 11: Phantasmal Image, Spark Double, Sakashima of a Thousand Faces, Molten Duplication, Saw in Half, Blade of Selves, Helm of the Host, Hall of Echoes, Auton Soldier, Roaming Throne, Strionic Resonator | — | *strategic_judgment · high* | [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:reanimation` | yes | 4 | Make a seven-mana commander realistic. | 5: Entomb, Reanimate, Animate Dead, Persist, Feign Death | — | *strategic_judgment · high* | [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md) · [xander-08](../interactions/lord-xander-the-collector.md#xander-08-feign-death-on-your-commander-leave-it-in-the-graveyard) |
| `pkg:mill-finish` | yes | 3 | Turn half a library into all of it. | 5: Bruvac the Grandiloquent, Riverchurn Monument, Fraying Sanity, Maddening Cacophony, Cruel Calculations | — | *strategic_judgment · high* | [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md) · [xander-05](../interactions/lord-xander-the-collector.md#xander-05-finishing-the-mill-bruvac-riverchurn-monument-fraying-sanity-maddening-cacophony) |

## Key interactions

- **three-triggers:** Enter: discard half; attack: mill half; dies: sacrifice half (all rounded down). (Lord Xander, the Collector) *fact · verified* — [xander-01](../interactions/lord-xander-the-collector.md#xander-01-three-separate-triggers-enter-attack-dies)
- **legend-rule-deaths:** Each legendary Xander copy gives an enter trigger and a dies trigger via the legend rule. (Phantasmal Image, Molten Duplication, Saw in Half) *fact · verified* — [xander-02](../interactions/lord-xander-the-collector.md#xander-02-clones-and-the-legend-rule-phantasmal-image-molten-duplication-saw-in-half)
- **blade-vs-auton:** Blade of Selves tokens give ETB + dies; Auton Soldier tokens only ETB. (Blade of Selves, Auton Soldier) *fact · verified* — [xander-03](../interactions/lord-xander-the-collector.md#xander-03-myriad-copies-blade-of-selves-vs-auton-soldier)
- **feign-death:** Feign Death only works if Xander stays in the graveyard. (Feign Death, Lord Xander, the Collector) *fact · verified* — [xander-08](../interactions/lord-xander-the-collector.md#xander-08-feign-death-on-your-commander-leave-it-in-the-graveyard)
- **tergrid:** Tergrid steals Xander's discarded and sacrificed permanents. (Tergrid, God of Fright // Tergrid's Lantern) *fact · verified* — [xander-09](../interactions/lord-xander-the-collector.md#xander-09-tergrid-steals-xanders-discards-and-sacrifices)

## Tutors and recursion

- Tutor target **Lord Xander, the Collector** via Entomb, Gamble *strategic_judgment · high* — [xander-08](../interactions/lord-xander-the-collector.md#xander-08-feign-death-on-your-commander-leave-it-in-the-graveyard)
- Tutor target **Bruvac the Grandiloquent** via Demonic Tutor, Vampiric Tutor, Imperial Seal *strategic_judgment · high* — `spellbook:95-1022`
- Recursion: Reanimate, Animate Dead, Persist, Feign Death, Underworld Breach *strategic_judgment · high* — [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Free counters (Force of Will, Force of Negation, Pact of Negation, Fierce Guardianship), Mana Drain, Toxic Deluge, Cyclonic Rift.
- **Protection:** Lightning Greaves, Deflecting Swat.
- **Mana:** Fast mana (Mana Vault, Grim Monolith, Ancient Tomb, Lotus Petal, Dark Ritual) or the reanimation route.
- *strategic_judgment · high* — [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **graveyard-hate:** Graveyard hate stops the reanimation route to a seven-mana commander. Mitigations: Clones; Fast mana hard-cast. *strategic_judgment · high* — [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md)
- **odd-library:** Rounding down can leave a card in a library. Mitigations: Bruvac/Monument; Second mill source. *strategic_judgment · moderate* — [xander-05](../interactions/lord-xander-the-collector.md#xander-05-finishing-the-mill-bruvac-riverchurn-monument-fraying-sanity-maddening-cacophony)
- **xander-removed:** Removal before attacking costs the mill trigger (though the dies trigger still hurts). Mitigations: Copies; Protection. *strategic_judgment · moderate* — [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md)

## Identity core

- **Lord Xander, the Collector:** Discard half, mill half, sacrifice half. *fact · verified* — `oracle:Lord Xander, the Collector`
- **Bruvac the Grandiloquent:** Doubles Xander's mill into a full library. *strategic_judgment · high* — [xander-05](../interactions/lord-xander-the-collector.md#xander-05-finishing-the-mill-bruvac-riverchurn-monument-fraying-sanity-maddening-cacophony)
- **Phantasmal Image:** Two-mana Xander copy: ETB plus a legend-rule death. *strategic_judgment · high* — [xander-02](../interactions/lord-xander-the-collector.md#xander-02-clones-and-the-legend-rule-phantasmal-image-molten-duplication-saw-in-half)
- **Blade of Selves:** Myriad Xander tokens: enter and dies triggers per opponent. *strategic_judgment · high* — [xander-03](../interactions/lord-xander-the-collector.md#xander-03-myriad-copies-blade-of-selves-vs-auton-soldier)
- **Cruel Calculations:** Draws off the cards Xander milled. *strategic_judgment · moderate* — [xander-06](../interactions/lord-xander-the-collector.md#xander-06-cruel-calculations-counts-the-mill)

## Anti-goals and thematic constraints

- ✗ Commander-independent mill (Painter's Servant/Grindstone) cut for Xander copies (decisions).
- ✗ No generic Grixis cEDH replacement of the commander-first shell (decisions L17).
  - *strategic_judgment · high* — [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Vampire Demon collector of Fiora: discard, mill and sacrifice, halving everything.
  - *strategic_judgment · moderate* — [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.116a:** Myriad. *fact · verified* — `cr:702.116a`
- **CR 704.5j:** Legend rule puts copies into the graveyard (dies triggers). *fact · verified* — `cr:704.5j`

## Supporting features (heuristic, not identity)

- `{"hooks": ["combat damage / attack triggers", "discard", "graveyard as a resource", "sacrifice"], "hooked_cards": 27, "role_counts": {"counter": 7, "draw": 8, "protection": 3, "ramp": 11, "removal": 6, "tutor": 6, "wipe": 1}, "lands": 33, "edhrec_pages": ["lord-xander-the-collector"]}` *heuristic · low*

## Provenance

- Seeded from: [Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Current_Cycle_Decisions_2026-10-14.md) · [Lord_Xander_the_Collector_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Lord_Xander_the_Collector_Approved_2026-10-14.md) · [Lord_Xander_the_Collector_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_Xander_the_Collector_Whole_List_Audit_2026-10-14.csv) · [Lord_Xander_the_Collector_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Lord_Xander_the_Collector_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
