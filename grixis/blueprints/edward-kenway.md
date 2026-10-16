# Blueprint — Edward Kenway

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/edward-kenway.md), state `SOURCE_BASELINE`, list `lh1:fe8bb5317dbf183c…`). Machine-readable source: [`data/grixis/blueprints/edward-kenway.json`](../../data/grixis/blueprints/edward-kenway.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Edward Kenway** — Legendary Creature — Human Assassin Pirate

> At the beginning of your end step, create a Treasure token for each tapped Assassin, Pirate, and/or Vehicle you control.  
> Whenever a Vehicle you control deals combat damage to a player, look at the top card of that player's library, then exile it face down. You may play that card for as long as it remains exiled.

## Plan and commander role

- **Primary plan:** Attack and crew with Assassins, Pirates and Vehicles so Edward's end step makes a Treasure per tapped one, and Vehicle hits exile cards to play; spend the Treasure on draw and compact artifact wins. *strategic_judgment · high*
- **Secondary:** Time Sieve extra-turn loops fed by Edward's Treasures (or Locomotive, Reaver Cleaver, Hoard Hauler), plus Malcolm + Glint-Horn Buccaneer as a second compact win.
  - Evidence: [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md) · [edward-01](../interactions/edward-kenway.md#edward-01-each-tapped-permanent-counts-once) · [edward-03](../interactions/edward-kenway.md#edward-03-edward--time-sieve-five-tapped-permanents--an-extra-turn)
- **Commander role: central.** Edward converts every tapped Assassin, Pirate and Vehicle into Treasure and is half of the Edward + Time Sieve extra-turn loop. *strategic_judgment · high*
- ⚠️ **Honest note:** Several of the deck's infinite lines (Reaver Cleaver, Luxurious Locomotive, Hoard Hauler + Time Sieve; Malcolm + Glint-Horn) work without Edward, and the ten-Game-Changer card pool does much of the lifting.
  - Evidence: [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md) · [edward-03](../interactions/edward-kenway.md#edward-03-edward--time-sieve-five-tapped-permanents--an-extra-turn) · [edward-05](../interactions/edward-kenway.md#edward-05-the-reaver-cleaver-and-hoard-hauler-extra-turn-lines) · [edward-06](../interactions/edward-kenway.md#edward-06-malcolm--glint-horn-buccaneer)
- **Dependency level:** medium *strategic_judgment · high* — [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md) · [edward-05](../interactions/edward-kenway.md#edward-05-the-reaver-cleaver-and-hoard-hauler-extra-turn-lines)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Bracket 4 — Optimized (decisions natural ceiling).) | *fact · verified* | [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: fast mana, free counters and four Time Sieve infinites make this the top of B4, but the Pirate/Vehicle commander engine is too slow and board-dependent for cEDH. Agrees with the source.) | *strategic_judgment · high* | [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md) · `spellbook:1558-5736` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Edward_Kenway` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 42, "2": 1409, "3": 1096, "4": 295, "5": 31}, "decks_with_bracket": 2873, "share_b4_plus": 0.113, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__edward-kenway.json`

## Win conditions

- **edward-time-sieve** (combo): Five tapped Assassins/Pirates/Vehicles each turn give five Treasures; Time Sieve turns them into extra turns. Cards: Edward Kenway, Time Sieve. Enablers: Academy Manufactor. *fact · verified* — `spellbook:1558-5736` · [edward-03](../interactions/edward-kenway.md#edward-03-edward--time-sieve-five-tapped-permanents--an-extra-turn)
- **other-time-sieve** (combo): Reaver Cleaver, Luxurious Locomotive or Hoard Hauler produce enough Treasure for Time Sieve without Edward. Cards: Time Sieve, The Reaver Cleaver, Luxurious Locomotive, Hoard Hauler. *fact · verified* — `spellbook:1558-5039` · `spellbook:1558-6307` · `spellbook:451-1558` · [edward-04](../interactions/edward-kenway.md#edward-04-luxurious-locomotive-over-crew-with-five-creatures) · [edward-05](../interactions/edward-kenway.md#edward-05-the-reaver-cleaver-and-hoard-hauler-extra-turn-lines)
- **malcolm-glint-horn** (combo): With two or more opponents, each discard pings everyone and Malcolm makes Treasure to repeat. Cards: Malcolm, Keen-Eyed Navigator, Glint-Horn Buccaneer. *fact · verified* — `spellbook:4508-4869` · [edward-06](../interactions/edward-kenway.md#edward-06-malcolm--glint-horn-buccaneer)

## Engines

- **end-step-treasure:** Edward Kenway, Academy Manufactor, Black Market Connections, Coastal Piracy. Online when: Tapped Assassins, Pirates or Vehicles at your end step. *fact · verified* — [edward-01](../interactions/edward-kenway.md#edward-01-each-tapped-permanent-counts-once) · [edward-07](../interactions/edward-kenway.md#edward-07-academy-manufactor-triples-treasure-output)
- **vehicle-theft:** Edward Kenway, Ramirez DePietro, Pillager, Don Andres, the Renegade, Smuggler's Copter, Jackdaw, The Indomitable. Online when: Vehicles connecting with players. *fact · verified* — [edward-02](../interactions/edward-kenway.md#edward-02-vehicle-damage-exiles-a-card-you-may-play-lands-included) · [edward-11](../interactions/edward-kenway.md#edward-11-ramirez-and-don-andres)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:pirates-assassins` | yes | 12 | Bodies that count for Edward and crew Vehicles. | 19: Adéwalé, Breaker of Chains, Basim Ibn Ishaq, Breeches, Brazen Plunderer, Breeches, Eager Pillager, Captain Lannery Storm, Captain Storm, Cosmium Raider, Deadeye Quartermaster, Fearless Swashbuckler, Gemcutter Buccaneer, Glint-Horn Buccaneer, Hostage Taker, Kitesail Larcenist, Malcolm, Keen-Eyed Navigator, Mary Read and Anne Bonny, Port Razer, Ragavan, Nimble Pilferer, Ramirez DePietro, Pillager, Siren Stormtamer, Admiral Brass, Unsinkable | — | *strategic_judgment · high* | [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:vehicles` | yes | 8 | Vehicles count when tapped and trigger Edward's combat theft. | 12: Smuggler's Copter, Jackdaw, Deluxe Dragster, Luxurious Locomotive, Skysovereign, Consul Flagship, Nautiloid Ship, Subterranean Schooner, The Indomitable, The Belligerent, RMS Titanic, Hoard Hauler, Imposter Mech | — | *strategic_judgment · high* | [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:time-sieve` | yes | 2 | The extra-turn win and its tutor support. | 4: Time Sieve, Academy Manufactor, Vampiric Tutor, Imperial Seal | — | *strategic_judgment · high* | `spellbook:1558-5736` |

## Key interactions

- **once-each:** Each tapped permanent counts once, whatever its types. (Edward Kenway) *fact · verified* — [edward-01](../interactions/edward-kenway.md#edward-01-each-tapped-permanent-counts-once)
- **play-lands:** Edward's exiled card may be played, lands included; Ramirez only casts. (Edward Kenway, Ramirez DePietro, Pillager) *fact · verified* — [edward-02](../interactions/edward-kenway.md#edward-02-vehicle-damage-exiles-a-card-you-may-play-lands-included)
- **manufactor:** Academy Manufactor turns each Treasure into a Treasure, Clue and Food. (Academy Manufactor) *fact · verified* — [edward-07](../interactions/edward-kenway.md#edward-07-academy-manufactor-triples-treasure-output)
- **fateful-deck-out:** Fateful Discovery's draws are mandatory and can deck you during a Time Sieve loop. (Fateful Discovery, Academy Manufactor) *fact · verified* — [edward-08](../interactions/edward-kenway.md#edward-08-fateful-discoverys-mandatory-draws-can-deck-you-during-an-extra-turn-lock)
- **titanic:** Edward's trigger still counts after RMS Titanic's sacrifice. (RMS Titanic, Edward Kenway) *fact · verified* — [edward-09](../interactions/edward-kenway.md#edward-09-rms-titanic-the-edward-trigger-survives-titanics-sacrifice)

## Tutors and recursion

- Tutor target **Time Sieve** via Vampiric Tutor, Imperial Seal, Urza's Saga *strategic_judgment · high* — `spellbook:1558-5736`
- Recursion: Admiral Brass, Unsinkable, Adéwalé, Breaker of Chains, The Indomitable *strategic_judgment · moderate* — [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Free and cheap counters (Force of Will, Fierce Guardianship, Mana Drain, Swan Song) and removal Vehicles.
- **Protection:** Deflecting Swat, Fierce Guardianship, Cavern of Souls for Pirates.
- **Mana:** Premium fast mana (Mana Vault, Chrome Mox, Mox Diamond, Mox Opal, Lotus Petal) and Edward's Treasures.
- *strategic_judgment · moderate* — [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **board-wipe:** A wipe takes out the creature/Vehicle board Edward counts. Mitigations: Admiral Brass recursion; Counters. *strategic_judgment · high* — [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md)
- **self-deck:** Mandatory draws during a loop can deck you. Mitigations: Watch library size; skip Fateful Discovery mid-loop. *strategic_judgment · moderate* — [edward-08](../interactions/edward-kenway.md#edward-08-fateful-discoverys-mandatory-draws-can-deck-you-during-an-extra-turn-lock)
- **crew-tension:** Creatures that crew can't also attack; Vehicles without crew are dead. Mitigations: Cheap crew bodies; Over-crew Locomotive. *strategic_judgment · moderate* — [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md)

## Identity core

- **Edward Kenway:** Treasure per tapped Assassin, Pirate or Vehicle, plus Vehicle-hit card theft. *fact · verified* — `oracle:Edward Kenway`
- **Time Sieve:** Turns Edward's Treasure into extra turns. *strategic_judgment · high* — `spellbook:1558-5736`
- **Academy Manufactor:** Triples Treasure output into artifacts and draw. *strategic_judgment · high* — [edward-07](../interactions/edward-kenway.md#edward-07-academy-manufactor-triples-treasure-output)
- **Luxurious Locomotive:** Over-crewed Vehicle that taps many creatures for Edward. *strategic_judgment · moderate* — [edward-04](../interactions/edward-kenway.md#edward-04-luxurious-locomotive-over-crew-with-five-creatures)
- **Ramirez DePietro, Pillager:** Pirate that also steals cards on combat hits. *strategic_judgment · moderate* — [edward-11](../interactions/edward-kenway.md#edward-11-ramirez-and-don-andres)

## Anti-goals and thematic constraints

- ✗ Generic cEDH staples are justified only where the source found them to beat commander-specific cards (decisions L13).
- ✗ Keep the creature/Vehicle balance: Vehicles without crew don't count.
  - *strategic_judgment · high* — [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Assassin's Creed IV pirate captain: Assassins, Pirates, ships and plunder.
  - *strategic_judgment · moderate* — [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 301.7:** Vehicles and crew. *fact · verified* — `cr:301.7`
- **CR 111.10a:** Treasure tokens. *fact · verified* — `cr:111.10a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Assassin synergy", "Pirate synergy", "Treasure", "combat damage / attack triggers", "tokens"], "hooked_cards": 39, "role_counts": {"counter": 6, "draw": 11, "protection": 1, "ramp": 30, "removal": 4, "tutor": 3, "wipe": 1}, "lands": 35, "edhrec_pages": ["edward-kenway"]}` *heuristic · low*

## Provenance

- Seeded from: [Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Edward_Kenway_Current_Cycle_Decisions_2026-10-14.md) · [Edward_Kenway_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Edward_Kenway_Approved_2026-10-14.md) · [Edward_Kenway_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Edward_Kenway_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
