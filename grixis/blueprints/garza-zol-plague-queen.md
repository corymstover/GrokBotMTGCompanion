# Blueprint — Garza Zol, Plague Queen

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/garza-zol-plague-queen.md), state `SOURCE_BASELINE`, list `lh1:f5190339a7e9ccc3…`). Machine-readable source: [`data/grixis/blueprints/garza-zol-plague-queen.json`](../../data/grixis/blueprints/garza-zol-plague-queen.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Garza Zol, Plague Queen** — Legendary Creature — Vampire Noble

> Flying, haste  
> Whenever a creature dealt damage by Garza Zol this turn dies, put a +1/+1 counter on Garza Zol.  
> Whenever Garza Zol deals combat damage to a player, you may draw a card.

## Plan and commander role

- **Primary plan:** Voltron with Garza as the damage source: ramp out a seven-mana commander, make her damage lethal (Basilisk Collar, Quietus Spike, Thornbite Staff, Chandra's Ignition, Nova Flame) so each kill grows her, and close with commander damage, infect or extra combats. *strategic_judgment · high*
- **Secondary:** Equipment card flow (Robe of the Archmagi, Mask of Memory, Sword of Fire and Ice, Curiosity) and compact closers: Kediss + Grafted Exoskeleton, Hatred, Jeska tripling power, Sword of Feast and Famine or Reaver Cleaver + Aggravated Assault.
  - Evidence: [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md) · [garza-02](../interactions/garza-zol-plague-queen.md#garza-02-basilisk-collar--thornbite-staff-a-repeatable-deathtouch-ping) · [garza-05](../interactions/garza-zol-plague-queen.md#garza-05-kediss--grafted-exoskeleton-one-hit-poisons-every-opponent)
- **Commander role: central.** Garza is the only real threat: her damage triggers the growth, her hits draw, and every closer is aimed at her. *strategic_judgment · high*
- ⚠️ **Honest note:** Seven mana with a rising commander tax, and every plan runs through one creature: removal or a chump-proof blocker stalls the deck (source: blueprint L44). Her draw clause is a 'may' that only works on player hits.
  - Evidence: [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md#L44](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md) · [garza-01](../interactions/garza-zol-plague-queen.md#garza-01-any-damage-from-garza-counts-and-the-death-can-come-later)
- **Dependency level:** high *strategic_judgment · high* — [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint target).) | *fact · verified* | [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md#L6](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: optimized Voltron with compact closers, capped by a seven-mana combat commander. Agrees with the source.) | *strategic_judgment · high* | [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md#L44](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md) · `spellbook:2822-3681` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Garza_Zol__Plague_Queen` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 5, "2": 22, "3": 9, "4": 6}, "decks_with_bracket": 42, "share_b4_plus": 0.143, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__garza-zol-plague-queen.json`

## Win conditions

- **commander-damage** (natural): Grown, evasive Garza with equipment, Hatred or Jeska kills through commander damage. Cards: Hatred, Jeska, Thrice Reborn, Blackblade Reforged, Blade of the Bloodchief, Tarrian's Soulcleaver. Enablers: Garza Zol, Plague Queen, Rogue's Passage, Brotherhood Regalia. *strategic_judgment · high* — [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md) · [garza-07](../interactions/garza-zol-plague-queen.md#garza-07-damage-multipliers-for-commander-damage-and-poison)
- **kediss-infect** (combo): Infect Garza at 10+ power with Kediss: one hit gives every opponent 10 poison. Cards: Kediss, Emberclaw Familiar, Grafted Exoskeleton. Enablers: Garza Zol, Plague Queen, Psychotic Fury, Inquisitor's Flail. *fact · verified* — `spellbook:2822-3681` · [garza-05](../interactions/garza-zol-plague-queen.md#garza-05-kediss--grafted-exoskeleton-one-hit-poisons-every-opponent)
- **extra-combats** (combo): Sword of Feast and Famine or The Reaver Cleaver + Aggravated Assault: unbounded combats. Cards: Aggravated Assault, Sword of Feast and Famine, The Reaver Cleaver. Enablers: Garza Zol, Plague Queen. *fact · verified* — `spellbook:900-3750` · `spellbook:3750-5039` · [garza-09](../interactions/garza-zol-plague-queen.md#garza-09-sword-of-feast-and-famine-or-reaver-cleaver--aggravated-assault)

## Engines

- **deathtouch-growth:** Garza Zol, Plague Queen, Basilisk Collar, Quietus Spike, Thornbite Staff, Chandra's Ignition, Nova Flame, Fall of the Hammer, Soul's Fire. Online when: Garza in play with a deathtouch source or a damage effect sourced from her. *fact · verified* — [garza-02](../interactions/garza-zol-plague-queen.md#garza-02-basilisk-collar--thornbite-staff-a-repeatable-deathtouch-ping) · [garza-03](../interactions/garza-zol-plague-queen.md#garza-03-chandras-ignition-and-nova-flame-garza-is-the-source)
- **combat-draw:** Garza Zol, Plague Queen, Robe of the Archmagi, Curiosity, Mask of Memory, Sword of Fire and Ice. Online when: Garza connects with a player. *fact · verified* — [garza-10](../interactions/garza-zol-plague-queen.md#garza-10-robe-of-the-archmagi-and-curiosity-draws)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:evasion-protection` | yes | 8 | Make the one threat connect and survive. | 11: Brotherhood Regalia, Trailblazer's Boots, Rogue's Passage, Shizo, Death's Storehouse, Swiftfoot Boots, Mithril Coat, Commander's Plate, Shadowspear, Slip Out the Back, Deflecting Swat, Fierce Guardianship | — | *strategic_judgment · high* | [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md) |
| `pkg:deathtouch-damage` | yes | 5 | Turn Garza's damage into kills that grow her. | 7: Basilisk Collar, Quietus Spike, Thornbite Staff, Chandra's Ignition, Nova Flame, Fall of the Hammer, Soul's Fire | — | *strategic_judgment · high* | [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md) · [garza-02](../interactions/garza-zol-plague-queen.md#garza-02-basilisk-collar--thornbite-staff-a-repeatable-deathtouch-ping) |
| `pkg:fast-mana` | yes | 6 | Pay for a seven-mana commander and its tax. | 10: Sol Ring, Mana Vault, Grim Monolith, Ancient Tomb, Arcane Signet, Fellwar Stone, Command Beacon, Talisman of Creativity, Talisman of Dominance, Talisman of Indulgence | — | *strategic_judgment · high* | [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md) |

## Key interactions

- **any-damage:** Any damage Garza dealt this turn counts; the death can come later in the turn. (Garza Zol, Plague Queen) *fact · verified* — [garza-01](../interactions/garza-zol-plague-queen.md#garza-01-any-damage-from-garza-counts-and-the-death-can-come-later)
- **garza-source:** Chandra's Ignition and Nova Flame make Garza the source, so deathtouch wipes boards and each death grows her. (Chandra's Ignition, Nova Flame) *fact · verified* — [garza-03](../interactions/garza-zol-plague-queen.md#garza-03-chandras-ignition-and-nova-flame-garza-is-the-source)
- **exoskeleton-sac:** Unattaching Grafted Exoskeleton sacrifices Garza. (Grafted Exoskeleton) *fact · verified* — [garza-06](../interactions/garza-zol-plague-queen.md#garza-06-grafted-exoskeleton-unattaching-it-sacrifices-garza)
- **jeska-cz:** Jeska dies on entry unless Garza has been cast from the command zone; Command Beacon casts don't count. (Jeska, Thrice Reborn, Command Beacon) *fact · verified* — [garza-08](../interactions/garza-zol-plague-queen.md#garza-08-jeska-needs-garza-cast-from-the-command-zone-first)
- **ozolith:** The Ozolith keeps Garza's counters when she leaves. (The Ozolith) *fact · verified* — [garza-11](../interactions/garza-zol-plague-queen.md#garza-11-the-ozolith-keeps-garzas-counters)

## Tutors and recursion

- Tutor target **Basilisk Collar** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md)
- Tutor target **Aggravated Assault** via Demonic Tutor *strategic_judgment · moderate* — `spellbook:900-3750`
- Recursion: Command Beacon, The Ozolith *strategic_judgment · low* — [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md)

## Requirements

- **Interaction:** Cheap removal and counters (Mana Drain, Counterspell, Terminate, Deadly Rollick, Pongify, Toxic Deluge, Cyclonic Rift).
- **Protection:** Equipment protection, boots, Fierce Guardianship, Deflecting Swat.
- **Mana:** 38 lands plus Sol Ring, Mana Vault, Grim Monolith, Ancient Tomb, Command Beacon.
- *strategic_judgment · high* — [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md)

## Failure modes

- **tax:** Repeated removal makes a seven-mana commander uncastable. Mitigations: Command Beacon; Protection suite. *strategic_judgment · high* — [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md#L44](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md)
- **single-threat:** One-threat Voltron loses to edicts and chump-blocking. Mitigations: Flying, Rogue's Passage, Shizo; Kediss infect closer. *strategic_judgment · high* — [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md)
- **jeska-dead:** Jeska dies if Garza hasn't been cast from the command zone. Mitigations: Cast Garza first. *strategic_judgment · moderate* — [garza-08](../interactions/garza-zol-plague-queen.md#garza-08-jeska-needs-garza-cast-from-the-command-zone-first)

## Identity core

- **Garza Zol, Plague Queen:** Grows from creatures she damaged dying; draws on player hits. *fact · verified* — `oracle:Garza Zol, Plague Queen`
- **Basilisk Collar:** Deathtouch turns every Garza ping into a kill. *strategic_judgment · high* — [garza-02](../interactions/garza-zol-plague-queen.md#garza-02-basilisk-collar--thornbite-staff-a-repeatable-deathtouch-ping)
- **Thornbite Staff:** Repeatable ping that untaps Garza on each death. *strategic_judgment · high* — [garza-02](../interactions/garza-zol-plague-queen.md#garza-02-basilisk-collar--thornbite-staff-a-repeatable-deathtouch-ping)
- **Kediss, Emberclaw Familiar:** With an infect Garza, poisons every opponent at once. *strategic_judgment · high* — [garza-05](../interactions/garza-zol-plague-queen.md#garza-05-kediss--grafted-exoskeleton-one-hit-poisons-every-opponent)
- **Chandra's Ignition:** Garza-sourced board wipe that grows her. *strategic_judgment · moderate* — [garza-03](../interactions/garza-zol-plague-queen.md#garza-03-chandras-ignition-and-nova-flame-garza-is-the-source)

## Anti-goals and thematic constraints

- ✗ Generic cEDH packages (Chrome Mox, Mox Diamond, rituals, Thassa's Oracle) were deliberately not added (blueprint L48).
- ✗ Don't treat Garza as an incidental body in a value shell.
  - *strategic_judgment · high* — [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md)
- Theme: Vampire plague queen: deathtouch, plague and a single growing threat.
  - *strategic_judgment · moderate* — [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.2b:** Deathtouch: any damage is lethal. *fact · verified* — `cr:702.2b`
- **CR 903.10a:** 21 combat damage from one commander. *fact · verified* — `cr:903.10a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["+1/+1 counters", "combat damage / attack triggers", "graveyard as a resource"], "hooked_cards": 16, "role_counts": {"counter": 4, "draw": 6, "protection": 6, "ramp": 14, "removal": 9, "tutor": 2, "wipe": 1}, "lands": 38, "edhrec_pages": ["garza-zol-plague-queen"]}` *heuristic · low*

## Provenance

- Seeded from: [Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Garza_Zol_Plague_Queen_Current_Cycle_Blueprint_2026-10-14.md) · [Garza_Zol_Plague_Queen_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Garza_Zol_Plague_Queen_Current_Cycle_Decisions_2026-10-14.md) · [Garza_Zol_Plague_Queen_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Garza_Zol_Plague_Queen_Approved_2026-10-14.md) · [Garza_Zol_Plague_Queen_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Garza_Zol_Plague_Queen_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
