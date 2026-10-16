# Blueprint — Mai and Zuko

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/mai-and-zuko.md), state `SOURCE_BASELINE`, list `lh1:7e44877d11198e9f…`). Machine-readable source: [`data/grixis/blueprints/mai-and-zuko.json`](../../data/grixis/blueprints/mai-and-zuko.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Mai and Zuko** — Legendary Creature — Human Noble Ally

> Firebending 3  
> You may cast Ally spells and artifact spells as though they had flash.

## Plan and commander role

- **Primary plan:** Artifact/Ally flash-combo: cast artifacts and Allies at instant speed (combat tricks, end-step development, interaction) and assemble compact artifact wins: Basalt Monolith + Rings of Brighthearth, Sensei's Divining Top with Bolas's Citadel + Aetherflux or Mystic Forge + a cost reducer. *strategic_judgment · high*
- **Secondary:** Firebending's combat mana pays for flashed artifacts and Allies; Breach + LED/Petal + Brain Freeze as a backup.
  - Evidence: [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md) · [maizuko-01](../interactions/mai-and-zuko.md#maizuko-01-flash-for-allies-and-artifacts-firebending-mana-lasts-through-combat) · [maizuko-08](../interactions/mai-and-zuko.md#maizuko-08-senseis-divining-top-loops-citadel--aetherflux-or-mystic-forge--a-cost-reducer)
- **Commander role: significant.** Flash for Allies and artifacts lets the combo and value pieces land on opponents' turns, and firebending adds combat mana. *strategic_judgment · high*
- ⚠️ **Honest note:** Every Spellbook infinite in the list (Monolith + Rings, the Top loops, Breach) works without Mai and Zuko; the commander adds speed and instant-speed safety, not the kill.
  - Evidence: [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md) · [maizuko-07](../interactions/mai-and-zuko.md#maizuko-07-basalt-monolith--rings-of-brighthearth--walking-ballista) · [maizuko-08](../interactions/mai-and-zuko.md#maizuko-08-senseis-divining-top-loops-citadel--aetherflux-or-mystic-forge--a-cost-reducer)
- **Dependency level:** low *strategic_judgment · high* — [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions).) | *fact · verified* | [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling, high end: fast mana and eight Spellbook infinites; the source rejects a Thoracle conversion to keep the commander relevant. Agrees with the source.) | *strategic_judgment · high* | [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md) · `spellbook:4131-4235` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Mai_and_Zuko` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 3, "2": 45, "3": 56, "4": 22, "5": 8}, "decks_with_bracket": 134, "share_b4_plus": 0.224, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__mai-and-zuko.json`

## Win conditions

- **monolith-rings** (combo): Basalt Monolith + Rings of Brighthearth: unbounded colorless mana into a mana sink. Cards: Basalt Monolith, Rings of Brighthearth. Enablers: Aetherflux Reservoir. *fact · verified* — `spellbook:4131-4235` · [maizuko-07](../interactions/mai-and-zuko.md#maizuko-07-basalt-monolith--rings-of-brighthearth--walking-ballista)
- **top-loops** (combo): Sensei's Divining Top with Bolas's Citadel + Aetherflux, or Mystic Forge + a cost reducer (Foundry Inspector, Etherium Sculptor, Enthusiastic Mechanaut, Longshot). Cards: Sensei's Divining Top, Bolas's Citadel, Aetherflux Reservoir, Mystic Forge, Foundry Inspector, Etherium Sculptor, Enthusiastic Mechanaut, Longshot, Rebel Bowman. Enablers: Mai and Zuko. *fact · verified* — `spellbook:2173-4740-5078` · `spellbook:777-985-5078` · `spellbook:985-1976-5078` · `spellbook:985-4908-5078` · `spellbook:985-5078-7356` · [maizuko-08](../interactions/mai-and-zuko.md#maizuko-08-senseis-divining-top-loops-citadel--aetherflux-or-mystic-forge--a-cost-reducer)
- **breach** (combo): Underworld Breach + LED/Lotus Petal + Brain Freeze. Cards: Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze. *fact · verified* — `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856` · [maizuko-09](../interactions/mai-and-zuko.md#maizuko-09-breach--led--brain-freeze)

## Engines

- **flash-artifacts:** Mai and Zuko, Tundra Tank, The Fire Nation Drill, Thought Monitor, Urza, Lord High Artificer, Sai, Master Thopterist. Online when: Mai and Zuko in play. *fact · verified* — [maizuko-01](../interactions/mai-and-zuko.md#maizuko-01-flash-for-allies-and-artifacts-firebending-mana-lasts-through-combat) · [maizuko-03](../interactions/mai-and-zuko.md#maizuko-03-flash-artifacts-as-interaction-tundra-tank-the-fire-nation-drill-thought-monitor)
- **combat-and-off-turn:** The Blue Spirit, Katara, Waterbending Master, Uthros Research Craft, Unwinding Clock, Boiling Rock Rioter, Ally Encampment. Online when: Casting on combat or opponents' turns. *fact · verified* — [maizuko-02](../interactions/mai-and-zuko.md#maizuko-02-combat-and-opponent-turn-payoffs-the-blue-spirit-katara-uthros-research-craft) · [maizuko-04](../interactions/mai-and-zuko.md#maizuko-04-unwinding-clock-untaps-mana-vault-and-basalt-monolith-on-others-turns) · [maizuko-06](../interactions/mai-and-zuko.md#maizuko-06-ally-support-boiling-rock-rioter-ally-encampment-roaming-throne)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:artifact-combo` | yes | 8 | Compact artifact wins. | 9: Basalt Monolith, Rings of Brighthearth, Sensei's Divining Top, Bolas's Citadel, Aetherflux Reservoir, Mystic Forge, Foundry Inspector, Etherium Sculptor, Enthusiastic Mechanaut | — | *strategic_judgment · high* | [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md) · [maizuko-08](../interactions/mai-and-zuko.md#maizuko-08-senseis-divining-top-loops-citadel--aetherflux-or-mystic-forge--a-cost-reducer) |
| `pkg:allies` | yes | 5 | Ally bodies that benefit from flash. | 6: The Blue Spirit, Katara, Waterbending Master, Sokka, Bold Boomeranger, Ty Lee, Chi Blocker, Boiling Rock Rioter, Avatar Roku, Firebender | — | *strategic_judgment · high* | [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md) · [maizuko-06](../interactions/mai-and-zuko.md#maizuko-06-ally-support-boiling-rock-rioter-ally-encampment-roaming-throne) |
| `pkg:fast-mana` | yes | 8 | Artifact mana for an artifact-combo deck. | 10: Sol Ring, Mana Vault, Basalt Monolith, Chrome Mox, Mox Diamond, Mox Opal, Lotus Petal, Arcane Signet, Fellwar Stone, Urza's Saga | — | *strategic_judgment · high* | [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md) |

## Key interactions

- **flash-firebend:** Flash for Allies/artifacts; firebending's RRR lasts all combat. (Mai and Zuko) *fact · verified* — [maizuko-01](../interactions/mai-and-zuko.md#maizuko-01-flash-for-allies-and-artifacts-firebending-mana-lasts-through-combat)
- **unwinding-clock:** Unwinding Clock untaps Mana Vault and Basalt Monolith on others' turns. (Unwinding Clock, Mana Vault, Basalt Monolith) *fact · verified* — [maizuko-04](../interactions/mai-and-zuko.md#maizuko-04-unwinding-clock-untaps-mana-vault-and-basalt-monolith-on-others-turns)
- **saga-cost:** Urza's Saga looks at mana cost {0}/{1}, not mana value. (Urza's Saga) *fact · verified* — [maizuko-05](../interactions/mai-and-zuko.md#maizuko-05-urzas-saga-finds-mana-cost-0-or-1-not-mana-value)
- **monolith-rings:** Monolith + Rings gives unbounded colorless mana. (Basalt Monolith, Rings of Brighthearth) *fact · verified* — [maizuko-07](../interactions/mai-and-zuko.md#maizuko-07-basalt-monolith--rings-of-brighthearth--walking-ballista)
- **top-flash:** Flash lets the Top loops run on opponents' turns. (Sensei's Divining Top, Mystic Forge) *fact · verified* — [maizuko-08](../interactions/mai-and-zuko.md#maizuko-08-senseis-divining-top-loops-citadel--aetherflux-or-mystic-forge--a-cost-reducer)

## Tutors and recursion

- Tutor target **Rings of Brighthearth** via Demonic Tutor, Vampiric Tutor *strategic_judgment · high* — `spellbook:4131-4235`
- Tutor target **Sensei's Divining Top** via Urza's Saga, Vampiric Tutor *strategic_judgment · moderate* — `spellbook:2173-4740-5078`
- Recursion: Underworld Breach, Emry, Lurker of the Loch *strategic_judgment · moderate* — [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Force of Will, Fierce Guardianship, Mana Drain, Swan Song, Toxic Deluge, Cyclonic Rift, flash artifacts.
- **Protection:** Lightning Greaves, Deflecting Swat, instant-speed deployment.
- **Mana:** 31 lands plus heavy artifact fast mana.
- *strategic_judgment · high* — [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **artifact-hate:** Artifact wipes and stax hit both mana and combos. Mitigations: Counters; Breach backup. *strategic_judgment · high* — [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md)
- **saga-misses:** Urza's Saga can't find {X} cards. Mitigations: Pick {0}/{1} targets. *strategic_judgment · moderate* — [maizuko-05](../interactions/mai-and-zuko.md#maizuko-05-urzas-saga-finds-mana-cost-0-or-1-not-mana-value)
- **commander-optional:** Without Mai and Zuko the deck loses flash speed, not its wins. Mitigations: Commander-free combos. *strategic_judgment · moderate* — [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md)

## Identity core

- **Mai and Zuko:** Flash for Allies and artifacts plus firebending 3. *fact · verified* — `oracle:Mai and Zuko`
- **Sensei's Divining Top:** Hub of the Citadel and Forge loops. *strategic_judgment · high* — [maizuko-08](../interactions/mai-and-zuko.md#maizuko-08-senseis-divining-top-loops-citadel--aetherflux-or-mystic-forge--a-cost-reducer)
- **Rings of Brighthearth:** With Basalt Monolith, unbounded mana. *strategic_judgment · high* — [maizuko-07](../interactions/mai-and-zuko.md#maizuko-07-basalt-monolith--rings-of-brighthearth--walking-ballista)
- **Tundra Tank:** Flashed artifact as an instant-speed trick. *strategic_judgment · high* — [maizuko-03](../interactions/mai-and-zuko.md#maizuko-03-flash-artifacts-as-interaction-tundra-tank-the-fire-nation-drill-thought-monitor)
- **The Blue Spirit:** Rewards creatures entering in combat. *strategic_judgment · moderate* — [maizuko-02](../interactions/mai-and-zuko.md#maizuko-02-combat-and-opponent-turn-payoffs-the-blue-spirit-katara-uthros-research-craft)

## Anti-goals and thematic constraints

- ✗ Generic Grixis Thoracle/Consultation conversion rejected (decisions L17).
- ✗ Keep cards that use flash or firebending mana over generic value.
  - *strategic_judgment · high* — [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Avatar: Mai and Zuko with Fire Nation machines and Allies.
  - *strategic_judgment · high* — [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.8a:** Flash. *fact · verified* — `cr:702.8a`
- **CR 106.4:** Mana empties between steps unless an effect says otherwise (firebending lasts through combat). *fact · verified* — `cr:106.4`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Ally synergy", "artifacts"], "hooked_cards": 48, "role_counts": {"counter": 5, "draw": 12, "protection": 3, "ramp": 15, "removal": 7, "tutor": 4, "wipe": 1}, "lands": 31, "edhrec_pages": ["mai-and-zuko"]}` *heuristic · low*

## Provenance

- Seeded from: [Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Current_Cycle_Decisions_2026-10-14.md) · [Mai_and_Zuko_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Mai_and_Zuko_Approved_2026-10-14.md) · [Mai_and_Zuko_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mai_and_Zuko_Whole_List_Audit_2026-10-14.csv) · [Mai_and_Zuko_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Mai_and_Zuko_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
