# Blueprint — Ashnod the Uncaring

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/ashnod-the-uncaring.md), state `SOURCE_BASELINE`, list `lh1:539266aa61af3923…`). Machine-readable source: [`data/grixis/blueprints/ashnod-the-uncaring.json`](../../data/grixis/blueprints/ashnod-the-uncaring.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Ashnod the Uncaring** — Legendary Creature — Human Artificer

> Deathtouch  
> Whenever you activate an ability of an artifact or creature that isn't a mana ability, if one or more permanents were sacrificed to activate it, you may copy that ability. You may choose new targets for the copy. (Sacrificing an artifact for mana to activate an ability doesn't count.)

## Plan and commander role

- **Primary plan:** Artifact-sacrifice engine: activate abilities whose costs sacrifice artifacts or creatures (Spellbombs, Station effects, Trading Post, Time Sieve, altars-as-costs) and copy every one of them with Ashnod, recurring the fodder with Trawler/Retriever/Welder loops. *strategic_judgment · high*
- **Secondary:** Spellbook infinites around Myr Retriever + Scrap Trawler + altar/KCI + cost reducer, Nim Deathmantle loops and Dross Scorpion + Retrofitter Foundry, with drain payoffs (Disciple, Mayhem Devil, Reckless Fireweaver).
  - Evidence: [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md) · [ashnod-01](../interactions/ashnod-the-uncaring.md#ashnod-01-current-oracle-no-once-per-turn-limit-tokens-count) · [ashnod-03](../interactions/ashnod-the-uncaring.md#ashnod-03-sacrifice-cost-artifacts-become-two-for-one) · [Ashnod_Oracle_Correction_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Ashnod_Oracle_Correction_2026-10-14.md)
- **Commander role: central.** Ashnod doubles every non-mana ability that sacrificed something to activate: copied Time Sieve is two extra turns, copied Trading Post is two cards or two artifacts back. *strategic_judgment · high*
- ⚠️ **Honest note:** The source blueprint describes an older 'once each turn, nontoken' Ashnod; current Oracle has no turn limit and tokens count (M1 ashnod-01). The deck is stronger than the source text implies, and its infinites run without Ashnod.
  - Evidence: [ashnod-01](../interactions/ashnod-the-uncaring.md#ashnod-01-current-oracle-no-once-per-turn-limit-tokens-count) · [Ashnod_Oracle_Correction_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Ashnod_Oracle_Correction_2026-10-14.md) · [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md) · [ashnod-03](../interactions/ashnod-the-uncaring.md#ashnod-03-sacrifice-cost-artifacts-become-two-for-one)
- **Dependency level:** medium *strategic_judgment · moderate* — [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md) · [ashnod-08](../interactions/ashnod-the-uncaring.md#ashnod-08-scrap-trawler--myr-retriever--altar-or-kci--a-cost-reducer)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Proposed natural ceiling: optimized/high-power Bracket 4, not claimed established cEDH (approval gate dossier).) | *fact · verified* | [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md) |
| GrokBot estimated ceiling | 4 (High Bracket 4: 15 Spellbook infinites (3-4 pieces) and a stronger current Oracle than the source assumed, but a five-mana commander and no compact cEDH win. Agrees with the recovered source claim.) | *strategic_judgment · high* | [ashnod-01](../interactions/ashnod-the-uncaring.md#ashnod-01-current-oracle-no-once-per-turn-limit-tokens-count) · [ashnod-08](../interactions/ashnod-the-uncaring.md#ashnod-08-scrap-trawler--myr-retriever--altar-or-kci--a-cost-reducer) · `spellbook:1020-1976-2034-2866` · [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Ashnod_the_Uncaring` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 5, "2": 219, "3": 319, "4": 81, "5": 16}, "decks_with_bracket": 640, "share_b4_plus": 0.152, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__ashnod-the-uncaring.json`

## Win conditions

- **trawler-retriever-loop** (combo): Scrap Trawler + Myr Retriever + Ashnod's Altar or KCI + a cost reducer (Etherium Sculptor, Foundry Inspector, Enthusiastic Mechanaut): infinite death/ETB triggers for Disciple/Mayhem Devil drain. Cards: Scrap Trawler, Myr Retriever, Ashnod's Altar, Krark-Clan Ironworks, Etherium Sculptor. Enablers: Disciple of the Vault, Mayhem Devil. *fact · verified* — [ashnod-08](../interactions/ashnod-the-uncaring.md#ashnod-08-scrap-trawler--myr-retriever--altar-or-kci--a-cost-reducer) · `spellbook:1020-1976-2034-2866`
- **deathmantle-loop** (combo): Nim Deathmantle + Ashnod's Altar or KCI with Marionette Apprentice, Urza or Farid. Cards: Nim Deathmantle, Ashnod's Altar, Marionette Apprentice, Urza, Lord High Artificer, Farid, Enterprising Salvager. *fact · verified* — [ashnod-09](../interactions/ashnod-the-uncaring.md#ashnod-09-nim-deathmantle-loops-apprentice-urza-farid) · `spellbook:2034-5003-6199`
- **scorpion-foundry** (combo): Dross Scorpion + Retrofitter Foundry + Ashnod's Altar or KCI. Cards: Dross Scorpion, Retrofitter Foundry, Ashnod's Altar. Enablers: Mayhem Devil. *fact · verified* — [ashnod-10](../interactions/ashnod-the-uncaring.md#ashnod-10-dross-scorpion--retrofitter-foundry--altar-or-kci) · `spellbook:2034-2797-4853`
- **copied-time-sieve** (natural): Time Sieve copied by Ashnod: two extra turns per activation. Cards: Time Sieve, Ashnod the Uncaring. Enablers: Sai, Master Thopterist. *fact · verified* — [ashnod-04](../interactions/ashnod-the-uncaring.md#ashnod-04-time-sieve-copied-two-extra-turns)

## Engines

- **copy-sac-abilities:** Ashnod the Uncaring, Rings of Brighthearth, Trading Post, Pyrite Spellbomb, Executioner's Capsule, Mishra's Bauble, Wayfarer's Bauble. Online when: Ashnod in play; a non-mana activated ability with a sacrifice in its cost. *fact · verified* — [ashnod-01](../interactions/ashnod-the-uncaring.md#ashnod-01-current-oracle-no-once-per-turn-limit-tokens-count) · [ashnod-03](../interactions/ashnod-the-uncaring.md#ashnod-03-sacrifice-cost-artifacts-become-two-for-one)
- **leave-play-payoffs:** Disciple of the Vault, Mayhem Devil, Reckless Fireweaver, Marionette Apprentice. Online when: Artifacts/permanents being sacrificed. *fact · verified* — [ashnod-11](../interactions/ashnod-the-uncaring.md#ashnod-11-leave-the-battlefield-payoffs)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:sac-cost-artifacts` | yes | 8 | Artifacts whose own abilities sacrifice, so Ashnod copies them. | 10: Pyrite Spellbomb, Executioner's Capsule, Mishra's Bauble, Wayfarer's Bauble, Dross Skullbomb, Mnemonic Sphere, Moonsilver Key, Time Sieve, Trading Post, Blasting Station | — | *strategic_judgment · high* | [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md) · [ashnod-03](../interactions/ashnod-the-uncaring.md#ashnod-03-sacrifice-cost-artifacts-become-two-for-one) |
| `pkg:sac-outlets` | yes | 5 | Free or mana-positive sacrifice outlets. | 6: Ashnod's Altar, Krark-Clan Ironworks, Altar of Dementia, Arcbound Ravager, Grinding Station, Krark-Clan Shaman | — | *strategic_judgment · high* | [Ashnod_the_Uncaring_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Ashnod_the_Uncaring_v1.md) |
| `pkg:artifact-recursion` | yes | 6 | Bring fodder back for the next copy. | 10: Scrap Trawler, Myr Retriever, Emry, Lurker of the Loch, Goblin Welder, Goblin Engineer, Scrap Welder, Academy Ruins, Buried Ruin, Nim Deathmantle, Farid, Enterprising Salvager | — | *strategic_judgment · high* | [Ashnod_the_Uncaring_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Ashnod_the_Uncaring_v1.md) |
| `pkg:drain-payoffs` | yes | 3 | Turn loops into a kill. | 5: Disciple of the Vault, Mayhem Devil, Reckless Fireweaver, Marionette Apprentice, Walking Ballista | — | *strategic_judgment · high* | [Ashnod_the_Uncaring_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Ashnod_the_Uncaring_v1.md) |

## Key interactions

- **current-oracle:** No once-per-turn limit; tokens count; copies every qualifying ability. (Ashnod the Uncaring) *fact · verified* — [ashnod-01](../interactions/ashnod-the-uncaring.md#ashnod-01-current-oracle-no-once-per-turn-limit-tokens-count) · [Ashnod_Oracle_Correction_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Ashnod_Oracle_Correction_2026-10-14.md)
- **mana-abilities-excluded:** Mana abilities and resolution-time sacrifices don't count. (Ashnod's Altar, Krark-Clan Ironworks) *fact · verified* — [ashnod-02](../interactions/ashnod-the-uncaring.md#ashnod-02-mana-abilities-and-resolution-time-sacrifices-dont-count)
- **time-sieve:** Copied Time Sieve: two extra turns. (Time Sieve) *fact · verified* — [ashnod-04](../interactions/ashnod-the-uncaring.md#ashnod-04-time-sieve-copied-two-extra-turns)
- **rings-and-ashnod:** Rings of Brighthearth and Ashnod both copy the same activation. (Rings of Brighthearth) *fact · verified* — [ashnod-06](../interactions/ashnod-the-uncaring.md#ashnod-06-rings-of-brighthearth-and-ashnod-both-copy)
- **copy-lki:** Copies use the original's sacrificed-object information. (Altar of Dementia, Blasting Station) *fact · verified* — [ashnod-05](../interactions/ashnod-the-uncaring.md#ashnod-05-copies-use-the-originals-sacrificed-object-information)

## Tutors and recursion

- Tutor target **Scrap Trawler** via Demonic Tutor, Vampiric Tutor *strategic_judgment · high* — [ashnod-08](../interactions/ashnod-the-uncaring.md#ashnod-08-scrap-trawler--myr-retriever--altar-or-kci--a-cost-reducer)
- Tutor target **Nim Deathmantle** via Demonic Tutor, Vampiric Tutor *strategic_judgment · high* — [ashnod-09](../interactions/ashnod-the-uncaring.md#ashnod-09-nim-deathmantle-loops-apprentice-urza-farid)
- Tutor target **Time Sieve** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md)
- Recursion: Scrap Trawler, Myr Retriever, Emry, Lurker of the Loch, Goblin Welder, Scrap Welder, Academy Ruins, Buried Ruin, Nim Deathmantle, Farid, Enterprising Salvager *fact · verified* — [Ashnod_the_Uncaring_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Ashnod_the_Uncaring_v1.md)

## Requirements

- **Interaction:** Light: Mana Drain, Fierce Guardianship, Deflecting Swat, a few removal spells; artifact hate must be answered on the stack.
- **Protection:** Free counters; Ashnod is five mana so recasting hurts.
- **Mana:** Artifact fast mana (Mox Opal, Lotus Petal, Sol Ring, Urza's Saga) and 33 lands (lean; the dossier accepts the risk).
- *strategic_judgment · moderate* — [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md)

## Failure modes

- **artifact-hate:** Vandalblast-style wipes or Stony Silence-type locks shut off the engine. Mitigations: Recursion package; Counters. *strategic_judgment · high* — [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md)
- **slow-commander:** Five-mana commander; 33 lands is lean. Mitigations: Artifact fast mana. *strategic_judgment · moderate* — [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md)
- **citadel-needs-board:** Bolas's Citadel and Time Sieve need a big board to fire. Mitigations: Token makers (Sai, Urza's Saga). *strategic_judgment · moderate* — [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md)

## Identity core

- **Ashnod the Uncaring:** Copies every sacrifice-cost ability; nothing else in the deck doubles activations. *fact · verified* — `oracle:Ashnod the Uncaring`
- **Trading Post:** Approved swap: four sacrifice modes, each doubled by Ashnod. *strategic_judgment · high* — [Ashnod_the_Uncaring_Approved_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Ashnod_the_Uncaring_Approved_2026-10-13.md)
- **Time Sieve:** Copied, it is two extra turns per activation. *strategic_judgment · high* — [ashnod-04](../interactions/ashnod-the-uncaring.md#ashnod-04-time-sieve-copied-two-extra-turns)
- **Scrap Trawler:** Recursion hub of the Retriever loop. *strategic_judgment · high* — [ashnod-08](../interactions/ashnod-the-uncaring.md#ashnod-08-scrap-trawler--myr-retriever--altar-or-kci--a-cost-reducer)
- **Rings of Brighthearth:** A second copy layer on the same activation. *strategic_judgment · moderate* — [ashnod-06](../interactions/ashnod-the-uncaring.md#ashnod-06-rings-of-brighthearth-and-ashnod-both-copy)

## Anti-goals and thematic constraints

- ✗ Don't drift into generic artifact combo that ignores sacrifice-cost abilities.
- ✗ Don't build to the outdated once-per-turn/nontoken reading of Ashnod.
  - *strategic_judgment · high* — [Ashnod_Oracle_Correction_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Ashnod_Oracle_Correction_2026-10-14.md) · [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md)
- Theme: Artificer / Brothers' War artifact flavor.
  - *strategic_judgment · low* — [Ashnod_the_Uncaring_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Ashnod_the_Uncaring_v1.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 605.1a:** Mana abilities are excluded from Ashnod's copy. *fact · verified* — `cr:605.1a`
- **CR 707.10:** A copied activated ability doesn't repay its costs. *fact · verified* — `cr:707.10`

## Supporting features (heuristic, not identity)

- `{"hooks": ["activated abilities", "artifacts", "copying", "sacrifice"], "hooked_cards": 58, "role_counts": {"counter": 3, "draw": 12, "protection": 1, "ramp": 15, "removal": 8, "tutor": 5, "wipe": 2}, "lands": 33, "edhrec_pages": ["ashnod-the-uncaring"]}` *heuristic · low*

## Provenance

- Seeded from: [Ashnod_the_Uncaring_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Ashnod_the_Uncaring_v1.md) · [Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Ashnod_the_Uncaring_Approval_Gate_Dossier_2026-10-13.md) · [Ashnod_the_Uncaring_Approved_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Ashnod_the_Uncaring_Approved_2026-10-13.md) · [Ashnod_Oracle_Correction_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/retrospective_1_to_8/Ashnod_Oracle_Correction_2026-10-14.md) · [Ashnod_the_Uncaring_Approved_2026-10-13.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Ashnod_the_Uncaring_Approved_2026-10-13.txt)
- Reviewed by: — (not yet reviewed by Cory)
