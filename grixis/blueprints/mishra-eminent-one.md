# Blueprint — Mishra, Eminent One

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/mishra-eminent-one.md), state `SOURCE_BASELINE`, list `lh1:6ac1d9c40c3c9286…`). Machine-readable source: [`data/grixis/blueprints/mishra-eminent-one.json`](../../data/grixis/blueprints/mishra-eminent-one.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Mishra, Eminent One** — Legendary Creature — Human Artificer

> At the beginning of combat on your turn, create a token that's a copy of target noncreature artifact you control, except its name is Mishra's Warform and it's a 4/4 Construct artifact creature in addition to its other types. It gains haste until end of turn. Sacrifice it at the beginning of the next end step.

## Plan and commander role

- **Primary plan:** Warform copies: at each combat Mishra copies a noncreature artifact as a hasty 4/4 token, which repeats ETB/LTB value (Ichor Wellspring, Cryogen Relic, Prized Statue, Lich's Relic, The Mightstone and Weakstone), feeds sacrifice and transmute effects, and closes with commander-native infinite turns or tokens. *strategic_judgment · high*
- **Secondary:** Secondary artifact combos (Top + Mystic Forge, KCI + Scrap Trawler + Myr Retriever) and Mindslaver control loops.
  - Evidence: [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)
- **Commander role: central.** Mishra is the copy engine and part of most of the deck's infinites. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native: 9 of the 19 Spellbook combos in the list include Mishra, including every infinite-turn line. The engine is a five-mana sorcery-speed combat trigger, which keeps the deck below cEDH speed; the source declined to swap in Oracle/Breach to force Bracket 5. The cycle 51 M1 review (mishraeo-01..09, all verified) confirms the Warform rules and combos.
  - Evidence: [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md) · `spellbook:2751-4636-5159`
- **Dependency level:** high *strategic_judgment · high* — `spellbook:2751-4636-5159`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions).) | *fact · verified* | [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling, high end: many commander-native infinites, but gated behind a five-mana sorcery-speed trigger. Agrees with the source.) | *strategic_judgment · high* | [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md) · `spellbook:2751-4636-5159` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Mishra__Eminent_One` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 17, "2": 859, "3": 1035, "4": 337, "5": 31}, "decks_with_bracket": 2279, "share_b4_plus": 0.161, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__mishra-eminent-one.json`

## Win conditions

- **aether-heart-turns** (combo): Mishra + Gonti's Aether Heart + Strionic Resonator, Lithoform Engine, Determined Iteration, Brudiclad or Worldwalker Helm: infinite turns. Cards: Mishra, Eminent One, Gonti's Aether Heart, Strionic Resonator, Lithoform Engine, Determined Iteration, Brudiclad, Telchor Engineer, Worldwalker Helm. *fact · verified* — `spellbook:2751-4636-5159` · `spellbook:3094-4636-5159` · `spellbook:3934-4636-5159` · `spellbook:1953-4636-5159` · `spellbook:4636-5159-5491`
- **urza-helm** (combo): Mishra + Urza, Lord High Artificer + Worldwalker Helm + Thousand-Year Elixir: infinite tokens and blue mana. Cards: Mishra, Eminent One, Urza, Lord High Artificer, Worldwalker Helm, Thousand-Year Elixir. *fact · verified* — `spellbook:457-5159-5295-5491`
- **reservoir-kci** (combo): Mishra + Aetherflux Reservoir; Mishra + KCI + Strionic Resonator or Lithoform Engine. Cards: Mishra, Eminent One, Aetherflux Reservoir, Krark-Clan Ironworks, Strionic Resonator, Lithoform Engine. *fact · verified* — `spellbook:4740-5159` · `spellbook:2751-4659-5159` · `spellbook:3094-4659-5159`
- **artifact-backups** (combo): Top + Mystic Forge + Etherium Sculptor or Enthusiastic Mechanaut; KCI + Scrap Trawler + Myr Retriever. Cards: Sensei's Divining Top, Mystic Forge, Etherium Sculptor, Enthusiastic Mechanaut, Krark-Clan Ironworks, Scrap Trawler, Myr Retriever. *fact · verified* — `spellbook:985-1976-5078` · `spellbook:985-4908-5078` · `spellbook:1020-1976-2866-4659` · `spellbook:1020-2866-4659-4908`

## Engines

- **warform-value:** Mishra, Eminent One, Ichor Wellspring, Cryogen Relic, Prized Statue, Lich's Relic, The Mightstone and Weakstone, Coveted Jewel. Online when: Mishra survives to combat with a good noncreature artifact. *fact · high* — `oracle:Mishra, Eminent One` · [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md) · [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)
- **warform-conversion:** Master Transmuter, Transmute Artifact, Repurposing Bay, Krark-Clan Ironworks, Smelting Vat. Online when: Temporary Warforms are turned into real artifacts or mana. *strategic_judgment · high* — [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L47](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md) · [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md) · [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:extra-turn-pieces` | yes | 4 | Pieces that finish the Aether Heart infinite-turn loops. | 6: Gonti's Aether Heart, Strionic Resonator, Lithoform Engine, Determined Iteration, Worldwalker Helm, Brudiclad, Telchor Engineer | — | *strategic_judgment · high* | [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md) |
| `pkg:etb-ltb-artifacts` | yes | 5 | Good Warform copy targets. | 8: Ichor Wellspring, Cryogen Relic, Prized Statue, Lich's Relic, Nihil Spellbomb, The Mightstone and Weakstone, Mindslaver, Coveted Jewel | — | *strategic_judgment · high* | [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md) |
| `pkg:artifact-tutors` | yes | 5 | Find combo pieces. | 9: Whir of Invention, Transmute Artifact, Goblin Engineer, Demonic Tutor, Vampiric Tutor, Imperial Seal, Gamble, Urza's Saga, Inventors' Fair | — | *strategic_judgment · high* | [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md) |

## Key interactions

- **iteration-ordering:** Order the beginning-of-combat triggers so Mishra resolves first; Determined Iteration can then populate the new Warform. (Mishra, Eminent One, Determined Iteration) *fact · verified* — [mishraeo-02](../interactions/mishra-eminent-one.md#mishraeo-02-gontis-aether-heart-infinite-turns-determined-iteration--strionic-resonator--lithoform-engine--worldwalker-helm--brudiclad) · `oracle:Mishra, Eminent One` · [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L44](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)
- **warform-mv:** The Warform keeps the copied artifact's mana value and survives until the end step, so Repurposing Bay or Transmute effects can cash it in first. (Mishra, Eminent One, Repurposing Bay, Transmute Artifact) *fact · verified* — [mishraeo-07](../interactions/mishra-eminent-one.md#mishraeo-07-sorcery-speed-sinks-repurposing-bay-uthros-station-esoteric-duplicator-at-end-step) · `oracle:Mishra, Eminent One` · [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)
- **copiable-values:** Copying an Effigy-modified artifact keeps its copiable modifications (decisions L45). (Mishra, Eminent One, Machine God's Effigy) *fact · verified* — [mishraeo-08](../interactions/mishra-eminent-one.md#mishraeo-08-machine-gods-effigy-turns-creatures-into-warform-targets) · `cr:707.2`
- **slaver-control:** Mindslaver + Resonator or Lithoform with Mishra is a repeatable opponent-turn control structure, not a win. (Mishra, Eminent One, Mindslaver, Strionic Resonator, Lithoform Engine) *fact · verified* — [mishraeo-04](../interactions/mishra-eminent-one.md#mishraeo-04-mindslaver-warforms-strionic--lithoform-esoteric-duplicator-emry-academy-ruins) · [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L63](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)
- **warform-basics:** The Warform is a hasty 4/4 copy of a noncreature artifact, sacrificed at the next end step. (Mishra, Eminent One) *fact · verified* — [mishraeo-01](../interactions/mishra-eminent-one.md#mishraeo-01-mishras-warform-a-hasty-44-copy-of-a-noncreature-artifact-sacrificed-at-end-step)
- **helm-urza:** Worldwalker Helm + Urza + Thousand-Year Elixir: infinite Warforms, Maps and {U}. (Mishra, Eminent One, Worldwalker Helm, Urza, Lord High Artificer, Thousand-Year Elixir) *fact · verified* — [mishraeo-03](../interactions/mishra-eminent-one.md#mishraeo-03-worldwalker-helm--urza--thousand-year-elixir-infinite-warforms-maps-and-u)

## Tutors and recursion

- Tutor target **Gonti's Aether Heart** via Whir of Invention, Transmute Artifact, Goblin Engineer, Demonic Tutor *strategic_judgment · high* — `spellbook:2751-4636-5159`
- Tutor target **Strionic Resonator** via Whir of Invention, Urza's Saga *strategic_judgment · moderate* — `spellbook:2751-4636-5159`
- Recursion: Academy Ruins, Goblin Welder, Emry, Lurker of the Loch, Scrap Trawler, Myr Retriever, Portal to Phyrexia *strategic_judgment · moderate* — [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Mana Drain, An Offer You Can't Refuse, Chaos Warp, Cyclonic Rift, Toxic Deluge.
- **Protection:** Fierce Guardianship, Deflecting Swat.
- **Mana:** Workshop, Moxen, Talismans, Coveted Jewel.
- *strategic_judgment · moderate* — [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)

## Failure modes

- **mishra-removed:** Mishra must survive to your own combat; sorcery-speed removal or a board wipe resets the engine. Mitigations: Fierce Guardianship; Deflecting Swat. *strategic_judgment · high* — `oracle:Mishra, Eminent One`
- **artifact-hate:** Artifact hate stops copy targets and combos. Mitigations: Recursion. *strategic_judgment · high* — [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)
- **speed:** A five-mana commander that triggers at combat is slow against cEDH tables. Mitigations: Fast artifact mana. *strategic_judgment · moderate* — [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)

## Identity core

- **Mishra, Eminent One:** Warform copy engine. *fact · verified* — `oracle:Mishra, Eminent One`
- **Gonti's Aether Heart:** Infinite-turn hub. *strategic_judgment · high* — `spellbook:2751-4636-5159`
- **Strionic Resonator:** Copies triggers for the turn loop. *strategic_judgment · high* — `spellbook:2751-4636-5159`
- **Lithoform Engine:** Redundant copier. *strategic_judgment · high* — `spellbook:3094-4636-5159`
- **Ichor Wellspring:** Card draw on Warform ETB and death. *strategic_judgment · high* — [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ Don't force Bracket 5 with a generic Grixis Oracle/Breach shell (decisions L18).
- ✗ Underworld Breach and Brain Freeze were cut for identity, not because they don't work (decisions L70).
  - *strategic_judgment · high* — [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)
- Theme: Artifact-copy Warforms; combat-step artifact value.
  - *strategic_judgment · high* — [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 707.2:** Copiable values. *fact · verified* — `cr:707.2`
- **CR 603.3b:** Ordering beginning-of-combat triggers. *fact · verified* — `cr:603.3b`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Construct synergy", "artifacts", "copying", "sacrifice", "tokens"], "hooked_cards": 53, "role_counts": {"counter": 4, "draw": 12, "protection": 2, "ramp": 17, "removal": 5, "tutor": 8, "wipe": 1}, "lands": 34, "edhrec_pages": ["mishra-eminent-one"]}` *heuristic · low*

## Provenance

- Seeded from: [Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Current_Cycle_Decisions_2026-10-15.md) · [Mishra_Eminent_One_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Mishra_Eminent_One_Approved_2026-10-15.md) · [Mishra_Eminent_One_Whole_List_Audit_2026-10-15.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Eminent_One_Whole_List_Audit_2026-10-15.csv) · [Mishra_Eminent_One_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Mishra_Eminent_One_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
