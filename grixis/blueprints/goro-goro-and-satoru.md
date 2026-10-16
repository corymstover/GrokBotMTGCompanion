# Blueprint — Goro-Goro and Satoru

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/goro-goro-and-satoru.md), state `SOURCE_BASELINE`, list `lh1:dc88090cd00d2d0e…`). Machine-readable source: [`data/grixis/blueprints/goro-goro-and-satoru.json`](../../data/grixis/blueprints/goro-goro-and-satoru.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Goro-Goro and Satoru** — Legendary Creature — Goblin Human

> Whenever one or more creatures you control that entered this turn deal combat damage to a player, create a 5/5 red Dragon Spirit creature token with flying.  
> {1}{R}: Creatures you control gain haste until end of turn.

## Plan and commander role

- **Primary plan:** Fresh attackers every turn (hasty creatures, ninjutsu/sneak, attack-token makers) connect across several opponents so Goro-Goro makes a 5/5 flying Dragon per damaged player; the Dragon army wins in the air. *strategic_judgment · high*
- **Secondary:** Breath of Fury extra-combat loops (with Goro-Goro, Urabrask's Forge, Daring Piracy, Determined Iteration or Loyal Apprentice), extra combats (Karlach, Great Train Heist, Aggravated Assault) and Dragon damage (Terror of the Peaks, Dragon Tempest).
  - Evidence: [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md) · [goro-01](../interactions/goro-goro-and-satoru.md#goro-01-one-dragon-per-player-per-damage-step) · [goro-05](../interactions/goro-goro-and-satoru.md#goro-05-goro-goro--breath-of-fury-order-goro-goros-trigger-on-top)
- **Commander role: central.** Goro-Goro is the Dragon factory and the haste source the whole combat plan runs through. *strategic_judgment · high*
- ⚠️ **Honest note:** The trigger needs creatures that entered this turn to connect, so blockers and fogs hurt; his own haste only covers creatures already in play when it resolves (M1 goro-02). Breath of Fury goes infinite with four other cards without him.
  - Evidence: [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md) · [goro-02](../interactions/goro-goro-and-satoru.md#goro-02-the-haste-ability-only-covers-creatures-you-control-when-it-resolves)
- **Dependency level:** high *strategic_judgment · high* — [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Bracket 4 — Optimized (decisions natural ceiling).) | *fact · verified* | [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: explosive, deterministic combat loops, but combat- and setup-dependent; a generic Thoracle conversion would sideline the commander. Agrees with the source.) | *strategic_judgment · high* | [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md) · `spellbook:2237-3259` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Goro_Goro_and_Satoru` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 21, "2": 750, "3": 859, "4": 188, "5": 13}, "decks_with_bracket": 1831, "share_b4_plus": 0.11, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__goro-goro-and-satoru.json`

## Win conditions

- **dragon-army** (natural): Repeated 5/5 flying Dragons plus Terror of the Peaks/Dragon Tempest damage. Cards: Terror of the Peaks, Dragon Tempest, Samut, Hazoret's Champion. Enablers: Goro-Goro and Satoru. *strategic_judgment · high* — [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md) · [goro-08](../interactions/goro-goro-and-satoru.md#goro-08-dragon-payoffs-terror-of-the-peaks-and-dragon-tempest)
- **goro-breath** (combo): Goro-Goro + Breath of Fury: each new Dragon takes the Aura for another combat. Cards: Goro-Goro and Satoru, Breath of Fury. Enablers: Samut, Hazoret's Champion. *fact · verified* — `spellbook:2237-3259` · [goro-05](../interactions/goro-goro-and-satoru.md#goro-05-goro-goro--breath-of-fury-order-goro-goros-trigger-on-top)
- **breath-token-makers** (combo): Breath of Fury with a beginning-of-combat token maker loops combats without the commander. Cards: Breath of Fury, Urabrask's Forge, Daring Piracy, Determined Iteration, Loyal Apprentice. *fact · verified* — `spellbook:1347-3259` · `spellbook:1674-3259` · `spellbook:3259-3934` · `spellbook:33-3259` · [goro-06](../interactions/goro-goro-and-satoru.md#goro-06-breath-of-fury--a-beginning-of-combat-token-maker)

## Engines

- **fresh-attackers:** Goro-Goro and Satoru, Ninja of the Deep Hours, Mistblade Shinobi, Fallen Shinobi, Yuriko, the Tiger's Shadow, Satoru Umezawa, Raphael, the Nightwatcher, Phoenix Chick. Online when: Creatures that entered this turn connect. *fact · verified* — [goro-01](../interactions/goro-goro-and-satoru.md#goro-01-one-dragon-per-player-per-damage-step) · [goro-03](../interactions/goro-goro-and-satoru.md#goro-03-ninjutsu-sneak-and-enters-attacking-creatures-all-qualify) · [goro-04](../interactions/goro-goro-and-satoru.md#goro-04-raphaels-sneak-gives-double-strike-before-first-strike-damage)
- **dragon-payoffs:** Terror of the Peaks, Dragon Tempest, Waterbender Ascension, Enduring Curiosity. Online when: Dragons entering or creatures connecting. *fact · verified* — [goro-08](../interactions/goro-goro-and-satoru.md#goro-08-dragon-payoffs-terror-of-the-peaks-and-dragon-tempest) · [goro-09](../interactions/goro-goro-and-satoru.md#goro-09-waterbender-ascension-counts-each-creature)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:ninjutsu-entrants` | yes | 8 | Creatures that enter during combat and count as fresh. | 12: Ninja of the Deep Hours, Mistblade Shinobi, Fallen Shinobi, Moon-Circuit Hacker, Silver-Fur Master, Yuriko, the Tiger's Shadow, Satoru Umezawa, Satoru, the Infiltrator, Ingenious Infiltrator, Thousand-Faced Shadow, Raphael, the Nightwatcher, Nashi, Moon Sage's Scion | — | *strategic_judgment · high* | [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md) · [goro-03](../interactions/goro-goro-and-satoru.md#goro-03-ninjutsu-sneak-and-enters-attacking-creatures-all-qualify) |
| `pkg:extra-combat` | yes | 4 | More damage steps with fresh creatures. | 4: Breath of Fury, Karlach, Fury of Avernus, Great Train Heist, Aggravated Assault | — | *strategic_judgment · high* | [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:combat-token-makers` | yes | 4 | New creatures every combat. | 4: Urabrask's Forge, Daring Piracy, Determined Iteration, Loyal Apprentice | — | *strategic_judgment · high* | [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md) · [goro-06](../interactions/goro-goro-and-satoru.md#goro-06-breath-of-fury--a-beginning-of-combat-token-maker) |

## Key interactions

- **one-per-player:** One Dragon per damaged player per combat-damage step. (Goro-Goro and Satoru) *fact · verified* — [goro-01](../interactions/goro-goro-and-satoru.md#goro-01-one-dragon-per-player-per-damage-step)
- **haste-snapshot:** The {1}{R} haste covers only creatures you control on resolution. (Goro-Goro and Satoru, Samut, Hazoret's Champion) *fact · verified* — [goro-02](../interactions/goro-goro-and-satoru.md#goro-02-the-haste-ability-only-covers-creatures-you-control-when-it-resolves)
- **raphael-double:** Sneaked Raphael gives double strike: two triggers per player. (Raphael, the Nightwatcher) *fact · verified* — [goro-04](../interactions/goro-goro-and-satoru.md#goro-04-raphaels-sneak-gives-double-strike-before-first-strike-damage)
- **breath-order:** Put Goro-Goro's trigger on top so the Dragon exists for Breath of Fury. (Breath of Fury, Goro-Goro and Satoru) *fact · verified* — [goro-05](../interactions/goro-goro-and-satoru.md#goro-05-goro-goro--breath-of-fury-order-goro-goros-trigger-on-top)
- **still-fresh:** Creatures that entered this turn stay fresh in later combats. (Goro-Goro and Satoru) *fact · verified* — [goro-07](../interactions/goro-goro-and-satoru.md#goro-07-fresh-creatures-stay-fresh-through-extra-combats)

## Tutors and recursion

- Tutor target **Breath of Fury** via Demonic Tutor, Vampiric Tutor *strategic_judgment · high* — `spellbook:2237-3259`
- Recursion: Phoenix Chick, Jeska's Will *strategic_judgment · low* — [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Counters and cheap removal (Mana Drain, Counterspell, Swan Song, Terminate, Deadly Rollick, Toxic Deluge).
- **Protection:** Lightning Greaves, Fierce Guardianship, Deflecting Swat.
- **Mana:** Three-mana commander; Sol Ring, Ancient Tomb, Talismans, Treasure from combat.
- *strategic_judgment · moderate* — [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **blocked:** Flying blockers, fogs or wipes stop fresh creatures connecting. Mitigations: Evasive Ninjas; Rogue's Passage. *strategic_judgment · high* — [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md)
- **haste-gap:** New Dragons lack haste in later combats without Samut/Tempest or another activation. Mitigations: Samut, Hazoret's Champion; Dragon Tempest. *strategic_judgment · moderate* — [goro-02](../interactions/goro-goro-and-satoru.md#goro-02-the-haste-ability-only-covers-creatures-you-control-when-it-resolves)
- **commander-removed:** Without Goro-Goro, no Dragons. Mitigations: Commander-free Breath loops. *strategic_judgment · moderate* — [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md)

## Identity core

- **Goro-Goro and Satoru:** 5/5 Dragon whenever fresh creatures connect; team haste. *fact · verified* — `oracle:Goro-Goro and Satoru`
- **Breath of Fury:** Extra-combat engine with the commander's Dragons. *strategic_judgment · high* — [goro-05](../interactions/goro-goro-and-satoru.md#goro-05-goro-goro--breath-of-fury-order-goro-goros-trigger-on-top)
- **Samut, Hazoret's Champion:** Continuous haste for Dragons made mid-loop. *strategic_judgment · high* — [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md)
- **Raphael, the Nightwatcher:** Double strike doubles the triggers. *strategic_judgment · high* — [goro-04](../interactions/goro-goro-and-satoru.md#goro-04-raphaels-sneak-gives-double-strike-before-first-strike-damage)
- **Terror of the Peaks:** Each Dragon deals 5 on entry. *strategic_judgment · moderate* — [goro-08](../interactions/goro-goro-and-satoru.md#goro-08-dragon-payoffs-terror-of-the-peaks-and-dragon-tempest)

## Anti-goals and thematic constraints

- ✗ No generic Grixis Thoracle/Breach turbo conversion (decisions L24).
- ✗ Keep creatures that can enter and connect the same turn.
  - *strategic_judgment · high* — [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Ninjas, sneaky entrants and Dragon spirits (Kamigawa Goro-Goro and Satoru).
  - *strategic_judgment · moderate* — [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.49a:** Ninjutsu puts the creature onto the battlefield attacking. *fact · verified* — `cr:702.49a`
- **CR 508.4:** Creatures put onto the battlefield attacking never attacked for trigger purposes, but they count as entering this turn. *fact · verified* — `cr:508.4`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Dragon synergy", "Spirit synergy", "combat damage / attack triggers", "tokens"], "hooked_cards": 40, "role_counts": {"counter": 6, "draw": 11, "protection": 2, "ramp": 13, "removal": 8, "tutor": 2, "wipe": 1}, "lands": 33, "edhrec_pages": ["goro-goro-and-satoru"]}` *heuristic · low*

## Provenance

- Seeded from: [Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Goro_Goro_and_Satoru_Current_Cycle_Decisions_2026-10-14.md) · [Goro_Goro_and_Satoru_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Goro_Goro_and_Satoru_Approved_2026-10-14.md) · [Goro_Goro_and_Satoru_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Goro_Goro_and_Satoru_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
