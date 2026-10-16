# Blueprint — Dr. Eggman

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/dr-eggman.md), state `SOURCE_BASELINE`, list `lh1:04e4d973c9055eda…`). Machine-readable source: [`data/grixis/blueprints/dr-eggman.json`](../../data/grixis/blueprints/dr-eggman.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Dr. Eggman** — Legendary Creature — Human Scientist

> Flying  
> At the beginning of your end step, draw a card. Then each opponent faces a villainous choice — That player discards a card, or you may put a Construct, Robot, or Vehicle card from your hand onto the battlefield.

## Plan and commander role

- **Primary plan:** Villainous-choice artifact cheat: hold big Constructs, Robots and Vehicles so each opponent either discards or lets you put one onto the battlefield free at your end step; punish discards and multiply Eggman's trigger. *strategic_judgment · high*
- **Secondary:** Artifact ETB payoffs over cast payoffs (Eggman doesn't cast), Gearhulks and Myr Battlesphere, discard punishers (Liliana's Caress, Waste Not, Tinybones) and The Valeyard/Y'shtola extra choices.
  - Evidence: [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md) · [eggman-01](../interactions/dr-eggman.md#eggman-01-opponents-choose-one-at-a-time-in-turn-order) · [eggman-03](../interactions/dr-eggman.md#eggman-03-eggmans-placement-isnt-a-cast)
- **Commander role: central.** Eggman draws every end step and forces a discard or a free deployment from each opponent. *strategic_judgment · high*
- ⚠️ **Honest note:** Opponents choose: an empty-handed opponent can 'discard' for free, and late in the game the choice gets cheap. The deck needs a dense hand of real threats to make the fork bite.
  - Evidence: [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md) · [eggman-01](../interactions/dr-eggman.md#eggman-01-opponents-choose-one-at-a-time-in-turn-order) · [eggman-02](../interactions/dr-eggman.md#eggman-02-an-empty-handed-opponent-can-choose-to-discard-and-lose-nothing)
- **Dependency level:** high *strategic_judgment · high* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Bracket 4 — Optimized (current-cycle blueprint).) | *fact · verified* | [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: strong free-deployment value with trigger multipliers; no compact win; the list sits at its computed floor of 3. Agrees with the source ceiling.) | *strategic_judgment · high* | [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md) · [eggman-05](../interactions/dr-eggman.md#eggman-05-extra-eggman-triggers-roaming-throne-spark-double-strionic-resonator) |
| Expected bracket (list as built) | 3 (computed floor 3) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Dr__Eggman` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 30, "2": 756, "3": 1047, "4": 255, "5": 15}, "decks_with_bracket": 2103, "share_b4_plus": 0.128, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__dr-eggman.json`

## Win conditions

- **free-artifact-army** (natural): Repeated free Gearhulks, Myr Battlesphere, Metalwork Colossus and Vehicles overwhelm the table. Cards: Myr Battlesphere, Metalwork Colossus, Noxious Gearhulk, Combustible Gearhulk, Cityscape Leveler, Thunderhawk Gunship. Enablers: Dr. Eggman. *strategic_judgment · high* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)
- **discard-attrition** (natural): Discard punishers turn the discard branch into damage and value. Cards: Liliana's Caress, Waste Not, Tinybones, Bauble Burglar, Geth's Grimoire, Withering Torment. Enablers: The Valeyard. *strategic_judgment · moderate* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)

## Engines

- **end-step-fork:** Dr. Eggman, The Valeyard, Roaming Throne, Strionic Resonator, Spark Double, Y'shtola Rhul. Online when: Your end step with Eggman in play. *fact · verified* — [eggman-01](../interactions/dr-eggman.md#eggman-01-opponents-choose-one-at-a-time-in-turn-order) · [eggman-04](../interactions/dr-eggman.md#eggman-04-the-valeyard-makes-each-opponent-choose-twice) · [eggman-05](../interactions/dr-eggman.md#eggman-05-extra-eggman-triggers-roaming-throne-spark-double-strionic-resonator) · [eggman-06](../interactions/dr-eggman.md#eggman-06-yshtola-rhuls-extra-end-step-retriggers-eggman)
- **robot-construct-supply:** Master Transmuter, Mechan Assembler, Simulacrum Synthesizer, One with the Machine, Scrap Trawler. Online when: Artifacts entering. *fact · verified* — [eggman-09](../interactions/dr-eggman.md#eggman-09-construct-robot-and-vehicle-supply) · [eggman-10](../interactions/dr-eggman.md#eggman-10-one-with-the-machine-counts-on-resolution)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:eggman-targets` | yes | 20 | Construct/Robot/Vehicle cards worth putting in free (the source counts 28). | 22: Myr Battlesphere, Metalwork Colossus, Noxious Gearhulk, Combustible Gearhulk, Coalstoke Gearhulk, Oildeep Gearhulk, Cityscape Leveler, Thunderhawk Gunship, Depthshaker Titan, Krang, Utrom Warlord, Vision, Spectral Synthezoid, Ultron, Machine Overlord, Ultron, Artificial Malevolence, Blitzwing, Cruel Tormentor // Blitzwing, Adaptive Assailant, Cyberdrive Awakener, Scrap Trawler, Foundry Inspector, Thought Monitor, Scrapyard Recombiner, The Regalia, Nautiloid Ship, Curie, Emergent Intelligence | — | *strategic_judgment · high* | [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md) · [eggman-09](../interactions/dr-eggman.md#eggman-09-construct-robot-and-vehicle-supply) |
| `pkg:trigger-multipliers` | yes | 4 | More Eggman triggers or end steps. | 5: The Valeyard, Roaming Throne, Strionic Resonator, Spark Double, Y'shtola Rhul | — | *strategic_judgment · high* | [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md) |
| `pkg:discard-punishers` | yes | 4 | Make the discard branch costly. | 5: Liliana's Caress, Waste Not, Tinybones, Bauble Burglar, Geth's Grimoire, Entropic Battlecruiser | — | *strategic_judgment · high* | [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md) |

## Key interactions

- **turn-order:** Draw, then each opponent chooses in turn order. (Dr. Eggman) *fact · verified* — [eggman-01](../interactions/dr-eggman.md#eggman-01-opponents-choose-one-at-a-time-in-turn-order)
- **empty-hand:** An empty-handed opponent can choose discard and lose nothing. (Dr. Eggman) *fact · verified* — [eggman-02](../interactions/dr-eggman.md#eggman-02-an-empty-handed-opponent-can-choose-to-discard-and-lose-nothing)
- **not-cast:** Eggman's placement isn't a cast: ETB triggers yes, cast triggers no. (Dr. Eggman, Vision, Spectral Synthezoid) *fact · verified* — [eggman-03](../interactions/dr-eggman.md#eggman-03-eggmans-placement-isnt-a-cast)
- **valeyard:** The Valeyard makes each opponent choose twice. (The Valeyard) *fact · verified* — [eggman-04](../interactions/dr-eggman.md#eggman-04-the-valeyard-makes-each-opponent-choose-twice)
- **yshtola:** Y'shtola Rhul's extra end step retriggers Eggman. (Y'shtola Rhul) *fact · verified* — [eggman-06](../interactions/dr-eggman.md#eggman-06-yshtola-rhuls-extra-end-step-retriggers-eggman)

## Tutors and recursion

- Tutor target **Myr Battlesphere** via Fabricate *strategic_judgment · moderate* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)
- Tutor target **Roaming Throne** via Fabricate *strategic_judgment · moderate* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)
- Recursion: Academy Ruins, Scrap Trawler, Scrapyard Recombiner *strategic_judgment · moderate* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)

## Requirements

- **Interaction:** Direct interaction for when Eggman is removed (Toxic Deluge, Blasphemous Act, Cyclonic Rift, counters).
- **Protection:** Greaves, Padeem, Cryptothrall, free protection.
- **Mana:** Five-mana commander; artifact mana (Mox Opal, Sol Ring, Urza's Saga).
- *strategic_judgment · moderate* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)

## Failure modes

- **cheap-choice:** Opponents with empty hands choose discard for free. Mitigations: Discard punishers still trigger only on real discards; Valeyard. *strategic_judgment · high* — [eggman-02](../interactions/dr-eggman.md#eggman-02-an-empty-handed-opponent-can-choose-to-discard-and-lose-nothing)
- **eggman-removed:** Five-mana commander removed: no fork. Mitigations: Protection; Artifact infrastructure works alone. *strategic_judgment · high* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)
- **empty-own-hand:** No good targets in hand makes the deployment branch harmless. Mitigations: Eggman's own draw; Keep threats in hand. *strategic_judgment · moderate* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)

## Identity core

- **Dr. Eggman:** End-step draw and the discard-or-deploy fork. *fact · verified* — `oracle:Dr. Eggman`
- **The Valeyard:** Doubles every opponent's villainous choice. *strategic_judgment · high* — [eggman-04](../interactions/dr-eggman.md#eggman-04-the-valeyard-makes-each-opponent-choose-twice)
- **Y'shtola Rhul:** Extra end step: another full Eggman trigger. *strategic_judgment · high* — [eggman-06](../interactions/dr-eggman.md#eggman-06-yshtola-rhuls-extra-end-step-retriggers-eggman)
- **Myr Battlesphere:** Premium free Construct deployment. *strategic_judgment · high* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)
- **Liliana's Caress:** Each discard costs 2 life, so the discard branch hurts. *strategic_judgment · moderate* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)

## Anti-goals and thematic constraints

- ✗ Don't force a cEDH shell that makes Eggman incidental (source).
- ✗ Prefer artifact-enter payoffs over cast-only payoffs.
  - *strategic_judgment · high* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)
- Theme: Sonic villain building robots: Constructs, Robots and Vehicles.
  - *strategic_judgment · high* — [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.55b:** A player may choose an impossible option (discard with no cards). *fact · verified* — `cr:701.55b`
- **CR 702.184:** Station on Entropic Battlecruiser. *fact · verified* — `cr:702.184`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Construct synergy", "Robot synergy", "discard", "villainous choices / voting"], "hooked_cards": 31, "role_counts": {"counter": 2, "draw": 10, "protection": 4, "ramp": 8, "removal": 8, "tutor": 3, "wipe": 3}, "lands": 31, "edhrec_pages": ["dr-eggman"]}` *heuristic · low*

## Provenance

- Seeded from: [Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Dr_Eggman_Current_Cycle_Blueprint_2026-10-14.md) · [Dr_Eggman_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Dr_Eggman_Approved_2026-10-14.md) · [Dr_Eggman_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Dr_Eggman_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
