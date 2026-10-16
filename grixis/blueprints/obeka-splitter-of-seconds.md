# Blueprint — Obeka, Splitter of Seconds

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/obeka-splitter-of-seconds.md), state `SOURCE_BASELINE`, list `lh1:95dc0a6026612942…`). Machine-readable source: [`data/grixis/blueprints/obeka-splitter-of-seconds.json`](../../data/grixis/blueprints/obeka-splitter-of-seconds.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Obeka, Splitter of Seconds** — Legendary Creature — Ogre Warlock

> Menace  
> Whenever Obeka deals combat damage to a player, you get that many additional upkeep steps after this phase.

## Plan and commander role

- **Primary plan:** Connect with Obeka (menace, evasion, protection), increase her damage or double her trigger, and turn the extra upkeep steps into cards, Treasures, Clues, tokens and counters through upkeep engines. *strategic_judgment · high*
- **Secondary:** Time Sieve plus upkeep-made artifacts gives repeatable extra turns; Darksteel Reactor and Mechanized Production give alternate wins.
  - Evidence: [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) · [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) · [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)
- **Commander role: central.** Obeka's combat-damage trigger is the deck's resource multiplier, and she's in all 5 Spellbook combos in the list. *strategic_judgment · high*
- ⚠️ **Honest note:** Strongly commander-native: every combo includes Obeka (Time Sieve + Court of Vantress/Thopter Spy Network/Replicating Ring/Smaug; Mechanized Production). She has to connect in combat first, so a 2/5 menace attacker is the bottleneck, and the extra upkeeps arrive after combat. No M1 interaction review exists yet for this deck.
  - Evidence: [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) · `spellbook:1558-5085-5471`
- **Dependency level:** high *strategic_judgment · high* — `spellbook:1558-5085-5471`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L9](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: commander-native infinite turns, but they need a combat connection first. Agrees with the source.) | *strategic_judgment · high* | [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) · `spellbook:1558-5085-5471` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Obeka__Splitter_of_Seconds` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 44, "2": 1838, "3": 1436, "4": 384, "5": 24}, "decks_with_bracket": 3726, "share_b4_plus": 0.11, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__obeka-splitter-of-seconds.json`

## Win conditions

- **time-sieve-turns** (combo): Obeka + Time Sieve + an upkeep artifact maker (Court of Vantress, Thopter Spy Network, Replicating Ring, Smaug): infinite turns. Cards: Obeka, Splitter of Seconds, Time Sieve, Court of Vantress, Thopter Spy Network, Replicating Ring, Smaug the Magnificent. Enablers: Mjölnir, Hammer of Thor, Roaming Throne. *fact · verified* — `spellbook:1469-1558-5471` · `spellbook:1558-5085-5471` · `spellbook:1558-5471-7348` · `spellbook:1558-5471-7651`
- **alt-wins** (alternate): Mechanized Production (eight same-name artifacts) or Darksteel Reactor (20 counters), both reached through extra upkeeps. Cards: Obeka, Splitter of Seconds, Mechanized Production, Darksteel Reactor. *fact · verified* — `spellbook:2047-5471` · [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)
- **advantage-combat** (natural): Out-value the table with extra-upkeep engines and win with combat or Smaug's Treasure damage. Cards: Obeka, Splitter of Seconds, Smaug the Magnificent. Enablers: Super Intelligence, Smaug the Magnificent, Tamiyo's Journal, Darksteel Reactor. *strategic_judgment · moderate* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)

## Engines

- **extra-upkeeps:** Obeka, Splitter of Seconds, Super Intelligence, Smaug the Magnificent, Tamiyo's Journal, Darksteel Reactor, Court of Ambition, Court of Cunning. Online when: Obeka deals combat damage to a player. *fact · high* — `oracle:Obeka, Splitter of Seconds` · [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) · `cr:500.9`
- **damage-multiplication:** Mjölnir, Hammer of Thor, Dragonfire Blade, Hatred, Roaming Throne, Wizard's Staff, Combat Research, Embercleave, Sword of Feast and Famine. Online when: Obeka equipped or pumped before damage. *strategic_judgment · high* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:damage-trigger-scaling` | yes | 5 | More damage or more triggers per connection. | 8: Mjölnir, Hammer of Thor, Dragonfire Blade, Hatred, Roaming Throne, Wizard's Staff, Combat Research, Embercleave, Sword of Feast and Famine | — | *strategic_judgment · high* | [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) |
| `pkg:upkeep-engines` | yes | 10 | Turn each extra upkeep into resources. | 15: Super Intelligence, Smaug the Magnificent, Tamiyo's Journal, Darksteel Reactor, Court of Ambition, Court of Cunning, Court of Embereth, Court of Ire, Court of Locthwain, Court of Vantress, As Foretold, Phyrexian Arena, Thopter Spy Network, Mechanized Production, Replicating Ring | — | *strategic_judgment · high* | [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) · [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L38](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) |
| `pkg:suspend` | optional | 4 | Time-counter cards sped up by upkeeps. | 6: Ancestral Vision, Inspiring Refrain, Jhoira of the Ghitu, Profane Tutor, Rousing Refrain, Suspended Sentence | — | *strategic_judgment · high* | [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) |
| `pkg:connection` | yes | 5 | Evasion and protection. | 8: Aqueous Form, Brotherhood Regalia, Silver Shroud Costume, Lightning Greaves, Swiftfoot Boots, Thassa, God of the Sea, Shizo, Death's Storehouse, Silent Arbiter | — | *strategic_judgment · high* | [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) |

## Key interactions

- **upkeep-phases:** The additional upkeeps come in extra beginning phases whose untap and draw steps are skipped. (Obeka, Splitter of Seconds) *fact · high* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) · `cr:500.9`
- **mjolnir-worthy:** Mjölnir doubles Obeka's damage, and she's worthy, so equip costs {1}. (Mjölnir, Hammer of Thor, Obeka, Splitter of Seconds) *fact · high* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)
- **staff-not-wizard:** Wizard's Staff doubles her triggers, but she's a Warlock, so equip is the normal {3}. (Wizard's Staff, Obeka, Splitter of Seconds) *fact · high* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)
- **throne-ogre:** Roaming Throne naming Ogre or Warlock doubles the trigger. (Roaming Throne, Obeka, Splitter of Seconds) *fact · high* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)

## Tutors and recursion

- Tutor target **Time Sieve** via Demonic Tutor, Vampiric Tutor, Profane Tutor *strategic_judgment · high* — `spellbook:1558-5085-5471`
- Recursion: Shizo, Death's Storehouse *strategic_judgment · low* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)

## Requirements

- **Interaction:** Mana Drain, Swan Song, An Offer You Can't Refuse, Deadly Rollick, Cyclonic Rift, Toxic Deluge.
- **Protection:** Fierce Guardianship, Deflecting Swat, Greaves, Boots, Dragonfire Blade.
- **Mana:** 35 lands (blueprint L52).
- *strategic_judgment · moderate* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)

## Failure modes

- **no-connection:** Blockers, fogs and removal stop the engine. Mitigations: Menace; Evasion package. *strategic_judgment · high* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)
- **artifact-hate:** Artifact removal answers Time Sieve. Mitigations: Upkeep value even without the combo. *strategic_judgment · moderate* — `spellbook:1558-5085-5471`
- **four-to-six-drops:** Many upkeep engines cost four to six mana. Mitigations: 35 lands. *strategic_judgment · moderate* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)

## Identity core

- **Obeka, Splitter of Seconds:** Extra upkeeps from combat damage. *fact · verified* — `oracle:Obeka, Splitter of Seconds`
- **Time Sieve:** Turns upkeep artifacts into extra turns. *strategic_judgment · high* — `spellbook:1558-5085-5471`
- **Mjölnir, Hammer of Thor:** Doubles her damage. *strategic_judgment · high* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)
- **Smaug the Magnificent:** Treasure each upkeep, and a combo piece. *strategic_judgment · high* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)
- **Super Intelligence:** One mana: a card each upkeep. *strategic_judgment · high* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ Not generic Grixis cEDH (blueprint L48); no generic extra turns or Oracle/Breach (L49).
- ✗ No more evasion slots (L50).
  - *strategic_judgment · high* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) · [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) · [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)
- Theme: Extra upkeeps / combat damage / upkeep triggers (blueprint L11).
  - *strategic_judgment · high* — [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 500.9:** Adding steps. *fact · verified* — `cr:500.9`
- **CR 503.1:** Upkeep step. *fact · verified* — `cr:503.1`

## Supporting features (heuristic, not identity)

- `{"hooks": ["combat damage / attack triggers"], "hooked_cards": 12, "role_counts": {"counter": 4, "draw": 7, "protection": 7, "ramp": 11, "removal": 4, "tutor": 4, "wipe": 2}, "lands": 35, "edhrec_pages": ["obeka-splitter-of-seconds"]}` *heuristic · low*

## Provenance

- Seeded from: [Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md) · [Obeka_Splitter_of_Seconds_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Obeka_Splitter_of_Seconds_Candidate_Decisions_2026-10-15.md) · [Obeka_Splitter_of_Seconds_Final_Challenger_Red_Team_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Obeka_Splitter_of_Seconds_Final_Challenger_Red_Team_2026-10-15.md) · [Obeka_Splitter_of_Seconds_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Obeka_Splitter_of_Seconds_Approved_2026-10-15.md) · [Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md) · [Obeka_Splitter_of_Seconds_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Splitter_of_Seconds_Whole_List_Audit_2026-10-15.md) · [Obeka_Splitter_of_Seconds_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Obeka_Splitter_of_Seconds_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
