# Blueprint — Kess, Dissident Mage

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/kess-dissident-mage.md), state `SOURCE_BASELINE`, list `lh1:d89d5778424e5aa6…`). Machine-readable source: [`data/grixis/blueprints/kess-dissident-mage.json`](../../data/grixis/blueprints/kess-dissident-mage.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Kess, Dissident Mage** — Legendary Creature — Human Wizard

> Flying  
> Once during each of your turns, you may cast an instant or sorcery spell from your graveyard. If a spell cast this way would be put into your graveyard, exile it instead.

## Plan and commander role

- **Primary plan:** cEDH graveyard replay: Kess recasts one instant or sorcery from the graveyard each turn, so one Demonic Consultation or Tainted Pact finds Thassa's Oracle and is replayed to win, and Intuition/Gifts Ungiven piles win on any split. *strategic_judgment · high*
- **Secondary:** Underworld Breach finishes (Grinding Station with a zero-cost artifact, LED + Brain Freeze/Wheel), with loot and self-mill (Faithless Looting, Dragon's Rage Channeler, Entomb) stocking the yard.
  - Evidence: [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md) · [kess-03](../interactions/kess-dissident-mage.md#kess-03-kess-turns-one-tutor-into-both-halves-of-the-oracle-combo) · [kess-04](../interactions/kess-dissident-mage.md#kess-04-intuition-and-gifts-ungiven-piles-are-deterministic-with-kess)
- **Commander role: central.** Kess turns single tutors into complete Oracle wins and makes the Gifts/Intuition piles deterministic. *strategic_judgment · high*
- ⚠️ **Honest note:** Her permission is once per your own turn at normal timing (M1 kess-01), so it doesn't help on opponents' turns. Oracle + Consultation and the Breach lines still win without her, just less efficiently.
  - Evidence: [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md) · [kess-01](../interactions/kess-dissident-mage.md#kess-01-one-graveyard-cast-per-your-turn-at-normal-timing) · [kess-03](../interactions/kess-dissident-mage.md#kess-03-kess-turns-one-tutor-into-both-halves-of-the-oracle-combo)
- **Dependency level:** medium *strategic_judgment · high* — [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (Power Bracket 5 — fringe cEDH (decisions).) | *fact · verified* | [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 5 (Bracket 5 ceiling (fringe): genuine cEDH commander with 2026 results but lower conversion than leading commanders, per the source. Agrees with the source.) | *strategic_judgment · high* | [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md) · `spellbook:742-1295` |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Kess__Dissident_Mage` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 34, "2": 415, "3": 731, "4": 657, "5": 391}, "decks_with_bracket": 2228, "share_b4_plus": 0.47, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__kess-dissident-mage.json`

## Win conditions

- **kess-oracle** (combo): Consultation/Pact finds Oracle; Kess replays it from the graveyard to win. Intuition/Gifts piles are deterministic with her. Cards: Thassa's Oracle, Demonic Consultation, Tainted Pact, Intuition, Gifts Ungiven, Reanimate. Enablers: Kess, Dissident Mage. *fact · verified* — `spellbook:742-1295` · `spellbook:1295-3093` · [kess-03](../interactions/kess-dissident-mage.md#kess-03-kess-turns-one-tutor-into-both-halves-of-the-oracle-combo) · [kess-04](../interactions/kess-dissident-mage.md#kess-04-intuition-and-gifts-ungiven-piles-are-deterministic-with-kess)
- **breach-station** (combo): Underworld Breach + Grinding Station with Lotus Petal, Mox Opal or Chrome Mox: unbounded self-mill (Mox Diamond doesn't work). Cards: Underworld Breach, Grinding Station, Lotus Petal, Mox Opal, Chrome Mox. *fact · verified* — `spellbook:1368-3698--44` · [kess-06](../interactions/kess-dissident-mage.md#kess-06-underworld-breach--grinding-station-with-a-zero-cost-artifact)
- **breach-led** (combo): Breach + LED/Petal + Brain Freeze, or LED + Wheel of Fortune. Cards: Underworld Breach, Lion's Eye Diamond, Brain Freeze, Wheel of Fortune. *fact · verified* — `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856` · `spellbook:1368-2706-3518` · [kess-07](../interactions/kess-dissident-mage.md#kess-07-breach--led--brain-freeze-or-wheel)

## Engines

- **graveyard-replay:** Kess, Dissident Mage, Displacer Kitten, Snapcaster Mage, Entomb, Faithless Looting. Online when: Kess in play on your turn with a spell in the graveyard. *fact · verified* — [kess-01](../interactions/kess-dissident-mage.md#kess-01-one-graveyard-cast-per-your-turn-at-normal-timing) · [kess-02](../interactions/kess-dissident-mage.md#kess-02-a-new-kess-object-resets-the-permission-displacer-kitten) · [kess-05](../interactions/kess-dissident-mage.md#kess-05-entomb-and-snapcaster-as-graveyard-spell-access)
- **fast-mana-tutors:** Mana Vault, Grim Monolith, Chrome Mox, Mox Diamond, Lotus Petal, Dark Ritual, Demonic Tutor, Vampiric Tutor, Imperial Seal, Necropotence. Online when: Opening hand. *strategic_judgment · high* — [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:oracle-piles` | yes | 6 | Pieces that turn Kess into deterministic wins. | 6: Thassa's Oracle, Demonic Consultation, Tainted Pact, Intuition, Gifts Ungiven, Reanimate | — | *strategic_judgment · high* | [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md) · [kess-04](../interactions/kess-dissident-mage.md#kess-04-intuition-and-gifts-ungiven-piles-are-deterministic-with-kess) |
| `pkg:yard-stock` | yes | 5 | Fill the graveyard cheaply. | 7: Faithless Looting, Dragon's Rage Channeler, Ledger Shredder, Entomb, Gitaxian Probe, Brainstorm, Ponder | — | *strategic_judgment · high* | [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:free-interaction` | yes | 8 | cEDH stack protection. | 11: Force of Will, Force of Negation, Pact of Negation, Fierce Guardianship, Mental Misstep, Mindbreak Trap, Flusterstorm, Swan Song, Pyroblast, Red Elemental Blast, Into the Flood Maw | — | *strategic_judgment · high* | [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md) |

## Key interactions

- **once-own-turn:** One graveyard cast per your turn at normal timing; flashback doesn't use it. (Kess, Dissident Mage) *fact · verified* — [kess-01](../interactions/kess-dissident-mage.md#kess-01-one-graveyard-cast-per-your-turn-at-normal-timing)
- **kitten-reset:** Displacer Kitten's blink makes a new Kess with a fresh permission. (Displacer Kitten, Kess, Dissident Mage) *fact · verified* — [kess-02](../interactions/kess-dissident-mage.md#kess-02-a-new-kess-object-resets-the-permission-displacer-kitten)
- **station-moxen:** Grinding Station loops need a zero-cost artifact; Mox Diamond doesn't work. (Grinding Station, Mox Diamond) *fact · verified* — [kess-06](../interactions/kess-dissident-mage.md#kess-06-underworld-breach--grinding-station-with-a-zero-cost-artifact)
- **counsel-delirium:** Demonic Counsel is only a tutor with delirium. (Demonic Counsel) *fact · verified* — [kess-08](../interactions/kess-dissident-mage.md#kess-08-demonic-counsel-is-only-a-tutor-with-delirium)
- **beseech:** A bargained Beseech the Mirror casts the found card free. (Beseech the Mirror) *fact · verified* — [kess-09](../interactions/kess-dissident-mage.md#kess-09-bargained-beseech-the-mirror)

## Tutors and recursion

- Tutor target **Thassa's Oracle** via Demonic Consultation, Tainted Pact, Vampiric Tutor, Imperial Seal *strategic_judgment · high* — `spellbook:742-1295`
- Tutor target **Underworld Breach** via Demonic Tutor, Gamble, Personal Tutor *strategic_judgment · high* — `spellbook:1368-3698--44`
- Recursion: Kess, Dissident Mage, Snapcaster Mage, Reanimate, Underworld Breach *strategic_judgment · high* — [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Free counters and one-mana interaction.
- **Protection:** Fierce Guardianship, Deflecting Swat.
- **Mana:** Fast mana and rituals; 27 lands with no repeated names for Tainted Pact.
- *strategic_judgment · high* — [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **graveyard-hate:** Graveyard hate turns off Kess and Breach. Mitigations: Oracle + Consultation from hand. *strategic_judgment · high* — [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md)
- **own-turn-only:** Kess can't replay on opponents' turns. Mitigations: Snapcaster Mage; Flash protection. *strategic_judgment · moderate* — [kess-01](../interactions/kess-dissident-mage.md#kess-01-one-graveyard-cast-per-your-turn-at-normal-timing)
- **counsel:** Demonic Counsel without delirium only finds a Demon. Mitigations: Stock the yard first. *strategic_judgment · moderate* — [kess-08](../interactions/kess-dissident-mage.md#kess-08-demonic-counsel-is-only-a-tutor-with-delirium)

## Identity core

- **Kess, Dissident Mage:** Once-per-turn instant/sorcery replay from the graveyard. *fact · verified* — `oracle:Kess, Dissident Mage`
- **Demonic Consultation:** Cast twice with Kess: find Oracle, then win. *strategic_judgment · high* — [kess-03](../interactions/kess-dissident-mage.md#kess-03-kess-turns-one-tutor-into-both-halves-of-the-oracle-combo)
- **Intuition:** Deterministic Oracle pile with Kess. *strategic_judgment · high* — [kess-04](../interactions/kess-dissident-mage.md#kess-04-intuition-and-gifts-ungiven-piles-are-deterministic-with-kess)
- **Gifts Ungiven:** Every split wins with Kess's permission unused. *strategic_judgment · high* — [kess-04](../interactions/kess-dissident-mage.md#kess-04-intuition-and-gifts-ungiven-piles-are-deterministic-with-kess)
- **Displacer Kitten:** Resets Kess for another graveyard cast. *strategic_judgment · moderate* — [kess-02](../interactions/kess-dissident-mage.md#kess-02-a-new-kess-object-resets-the-permission-displacer-kitten)

## Anti-goals and thematic constraints

- ✗ Six-mana storm engines (Thousand-Year Storm) and storm payoffs (Talrand, Sky Summoner; Guttersnipe) rejected (decisions L137).
- ✗ Keep 100 distinct names so Tainted Pact never stops early.
  - *strategic_judgment · high* — [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md#L137](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Dissident Wizard: spells recast from the graveyard; theme subordinate to cEDH.
  - *strategic_judgment · moderate* — [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 400.7:** A blinked Kess is a new object with a fresh permission. *fact · verified* — `cr:400.7`
- **CR 601.2:** Casting from the graveyard follows normal timing. *fact · verified* — `cr:601.2`

## Supporting features (heuristic, not identity)

- `{"hooks": ["graveyard as a resource", "instants and sorceries"], "hooked_cards": 54, "role_counts": {"counter": 10, "draw": 10, "protection": 1, "ramp": 18, "removal": 6, "tutor": 11, "wipe": 2}, "lands": 27, "edhrec_pages": ["kess-dissident-mage"]}` *heuristic · low*

## Provenance

- Seeded from: [Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Current_Cycle_Decisions_2026-10-14.md) · [Kess_Dissident_Mage_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Kess_Dissident_Mage_Approved_2026-10-14.md) · [Kess_Dissident_Mage_Baseline_SHA_Correction_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Kess_Dissident_Mage_Baseline_SHA_Correction_2026-10-14.md) · [Kess_Dissident_Mage_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Kess_Dissident_Mage_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
- **Correction (Bot cycle 62):** retracted anti_goals[0] 'Six-mana storm engines and storm payoffs (Thousand-Year Storm, Talrand, Guttersnipe)', which read as calling all three six-mana → Only Thousand-Year Storm is mana value 6; Talrand, Sky Summoner is 4 and Guttersnipe 3 (cache). Wording split; found by the cycle-62 MV rule.
