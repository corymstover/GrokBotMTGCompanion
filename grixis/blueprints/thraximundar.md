# Blueprint — Thraximundar

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/thraximundar.md), state `SOURCE_BASELINE`, list `lh1:6a7f264373b7f453…`). Machine-readable source: [`data/grixis/blueprints/thraximundar.json`](../../data/grixis/blueprints/thraximundar.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Thraximundar** — Legendary Creature — Zombie Assassin

> Haste  
> Whenever Thraximundar attacks, defending player sacrifices a creature of their choice.  
> Whenever a player sacrifices a creature, you may put a +1/+1 counter on Thraximundar.

## Plan and commander role

- **Primary plan:** Sacrifice aristocrats: edicts and forced sacrifices (Fleshbag, Plaguecrafter, Vona's Hunger, Flare of Malice, Call to the Grave, Grave Pact, Dictate of Erebos) shrink opposing boards while every sacrifice grows Thraximundar, and Cultist / Shizo make him an evasive commander-damage clock. *strategic_judgment · high*
- **Secondary:** Gravecrawler / Reassembling Skeleton loops with Phyrexian or Ashnod's Altar, Pitiless Plunderer, Rooftop Storm and drain payoffs (Blood Artist, Zulaport Cutthroat) for deterministic kills.
  - Evidence: [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L63](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L83](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L89](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)
- **Commander role: significant.** Thraximundar's attack is an edict, he grows from every sacrifice by any player, and he is a Zombie that enables Gravecrawler. *strategic_judgment · high*
- ⚠️ **Honest note:** Honest call: significant. None of the 17 Spellbook combos names him, though he can be Gravecrawler's 'another Zombie'. Without the loops he is a commander-damage clock. The approval uses the v2 decisions (approvals L14).
  - Evidence: [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Approved_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Thraximundar_Approved_2026-10-15.md) · `spellbook:2577-4050`
- **Dependency level:** medium *strategic_judgment · high* — `spellbook:2577-4050`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (approved v2 decisions).) | *fact · verified* | [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L106](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (High Bracket 4: 17 Spellbook loops and strong tutors, but thin protection and a seven-mana commander keep it short of cEDH. Agrees with the source.) | *strategic_judgment · high* | [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L78](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · `spellbook:2577-4050` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Thraximundar` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 16, "2": 206, "3": 223, "4": 90, "5": 4}, "decks_with_bracket": 539, "share_b4_plus": 0.174, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__thraximundar.json`

## Win conditions

- **zombie-loops** (combo): Gravecrawler + Phyrexian Altar (with another Zombie), Rooftop Storm lines, or Reassembling Skeleton + Pitiless Plunderer + an Altar, finishing with Blood Artist, Zulaport, Goblin Bombardment or Altar of Dementia. Cards: Gravecrawler, Phyrexian Altar, Rooftop Storm, Carrion Feeder, Pitiless Plunderer, Reassembling Skeleton, Ashnod's Altar, Blood Artist, Zulaport Cutthroat, Warren Soultrader. Enablers: Diabolic Intent, Demonic Tutor, Vampiric Tutor. *strategic_judgment · high* — `spellbook:2577-4050` · `spellbook:2577-2842-5670` · `spellbook:1580-4050-4871` · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L83](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L86](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L87](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)
- **commander-damage** (natural): A hasty, growing, evasive Thraximundar (Cultist of the Absolute, Shizo fear). Cards: Thraximundar, Cultist of the Absolute, Shizo, Death's Storehouse. Enablers: Accursed Marauder, Fleshbag Marauder, Innocent Blood, Plaguecrafter. *strategic_judgment · high* — [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L44](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)

## Engines

- **any-sacrifice-growth:** Thraximundar, Accursed Marauder, Fleshbag Marauder, Innocent Blood, Plaguecrafter, Sheoldred's Edict, Necrotic Hex. Online when: Any player sacrifices a creature. *fact · high* — `oracle:Thraximundar` · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L89](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)
- **pact-dictate:** Grave Pact, Dictate of Erebos, Mayhem Devil. Online when: Your own sacrifices. *strategic_judgment · high* — [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L63](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:edicts` | yes | 10 | Forced sacrifice. | 13: Accursed Marauder, Fleshbag Marauder, Innocent Blood, Plaguecrafter, Sheoldred's Edict, Necrotic Hex, Archfiend of Depravity, Vona's Hunger, Flare of Malice, Call to the Grave, Winter, Tormented Loner, Liliana, Dreadhorde General, Tergrid, God of Fright // Tergrid's Lantern | — | *strategic_judgment · high* | [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L63](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L69](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) |
| `pkg:outlets` | yes | 6 | Free sacrifice outlets. | 8: Phyrexian Altar, Ashnod's Altar, Altar of Dementia, Carrion Feeder, Goblin Bombardment, Yawgmoth, Thran Physician, Warren Soultrader, Phyrexian Tower | — | *strategic_judgment · high* | [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L83](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L87](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) |
| `pkg:loop-pieces` | yes | 5 | Recursive bodies and payoffs. | 7: Gravecrawler, Reassembling Skeleton, Pitiless Plunderer, Rooftop Storm, Blood Artist, Zulaport Cutthroat, Grimgrin, Corpse-Born | — | *strategic_judgment · high* | [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L83](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L86](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) |
| `pkg:commander-mana` | yes | 6 | Cast and recast an expensive commander. | 7: Mana Vault, Sol Ring, Ancient Tomb, Cabal Coffers, Command Beacon, Dark Ritual, Urborg, Tomb of Yawgmoth | — | *strategic_judgment · high* | [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) |

## Key interactions

- **any-player:** Thraximundar triggers on any player's creature sacrifice, including costs (Diabolic Intent, Flare of Malice, Yawgmoth). (Thraximundar, Diabolic Intent, Flare of Malice) *fact · high* — `oracle:Thraximundar` · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L89](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)
- **call-spares-zombies:** Call to the Grave spares Zombies, Thraximundar included. (Call to the Grave, Thraximundar) *fact · high* — [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)
- **skeleton-ashnod:** Skeleton + Plunderer + Ashnod's Altar nets one colorless mana per loop. (Reassembling Skeleton, Pitiless Plunderer, Ashnod's Altar) *fact · high* — [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L88](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)
- **gravecrawler-zombie:** Gravecrawler needs another Zombie to be cast from the graveyard; Thraximundar counts. (Gravecrawler, Thraximundar) *fact · high* — [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L83](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)
- **force-cut:** Force of Will was cut for Mana Vault because the blue pitch pool was too thin. (Mana Vault) *fact · high* — [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)

## Tutors and recursion

- Tutor target **Gravecrawler** via Diabolic Intent, Demonic Tutor, Vampiric Tutor *strategic_judgment · high* — `spellbook:2577-4050` · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L38](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)
- Recursion: Gravecrawler, Reassembling Skeleton, Reanimate, Victimize, Wilhelt, the Rotcleaver, Liliana, Dreadhorde General *strategic_judgment · high* — [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L63](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)

## Requirements

- **Interaction:** Mana Drain, Fierce Guardianship, Feed the Swarm, Toxic Deluge, Cyclonic Rift, Vandalblast, edict suite.
- **Protection:** Deflecting Swat, Lightning Greaves, Swiftfoot Boots, Fierce Guardianship.
- **Mana:** 36 lands with Cabal Coffers, Urborg and Command Beacon.
- *strategic_judgment · moderate* — [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)

## Failure modes

- **commander-removal:** Repeated removal taxes a seven-mana commander. Mitigations: Command Beacon; Swiftfoot Boots. *strategic_judgment · high* — [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)
- **thin-counters:** Few counterspells after Force of Will was cut. Mitigations: Mana Drain; Fierce Guardianship. *strategic_judgment · high* — [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)
- **graveyard-hate:** Graveyard hate stops Gravecrawler and Skeleton loops. Mitigations: Edict plan; Commander damage. *strategic_judgment · moderate* — `spellbook:2577-4050`

## Identity core

- **Thraximundar:** Attack edict and growth from every sacrifice. *fact · verified* — `oracle:Thraximundar`
- **Gravecrawler:** The core loop body. *strategic_judgment · high* — `spellbook:2577-4050`
- **Phyrexian Altar:** Pays for Gravecrawler. *strategic_judgment · high* — `spellbook:2577-4050`
- **Grave Pact:** Turns your sacrifices into edicts. *strategic_judgment · high* — [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L63](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)
- **Cultist of the Absolute:** Evasive, protected commander clock. *strategic_judgment · high* — [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No Thassa's Oracle / Consultation (v1 decisions L68; v2 L78).
- ✗ Zombie tribal stays secondary (v2 L77).
  - *strategic_judgment · high* — [Thraximundar_Candidate_Decisions_2026-10-15.md#L68](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L78](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_v2_2026-10-15.md#L77](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md)
- Theme: Sacrifice / Zombie aristocrats / commander damage (approvals L27).
  - *strategic_judgment · high* — [Thraximundar_Approved_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Thraximundar_Approved_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.21a:** Sacrifice. *fact · verified* — `cr:701.21a`
- **CR 903.10a:** Commander damage. *fact · verified* — `cr:903.10a`
- **CR 702.36a:** Fear. *fact · verified* — `cr:702.36a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["+1/+1 counters", "combat damage / attack triggers", "sacrifice"], "hooked_cards": 39, "role_counts": {"counter": 2, "draw": 7, "protection": 3, "ramp": 15, "removal": 7, "tutor": 3, "wipe": 1}, "lands": 36, "edhrec_pages": ["thraximundar"]}` *heuristic · low*

## Provenance

- Seeded from: [Thraximundar_Candidate_Decisions_v2_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_v2_2026-10-15.md) · [Thraximundar_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Thraximundar_Candidate_Decisions_2026-10-15.md) · [Thraximundar_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Thraximundar_Approved_2026-10-15.md) · [Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Thraximundar_Approval_Ready_Verification_v2_2026-10-15.md) · [Thraximundar_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Thraximundar_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
