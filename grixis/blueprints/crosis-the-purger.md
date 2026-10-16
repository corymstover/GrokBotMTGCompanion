# Blueprint — Crosis, the Purger

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/crosis-the-purger.md), state `SOURCE_BASELINE`, list `lh1:0cbe60a05298b70d…`). Machine-readable source: [`data/grixis/blueprints/crosis-the-purger.json`](../../data/grixis/blueprints/crosis-the-purger.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Crosis, the Purger** — Legendary Creature — Dragon

> Flying  
> Whenever Crosis deals combat damage to a player, you may pay {2}{B}. If you do, choose a color, then that player reveals their hand and discards all cards of that color.

## Plan and commander role

- **Primary plan:** Discard control: make Crosis connect (evasion, haste, protection), pay {2}{B} to strip a color from the hand, and with Painter's Servant strip the whole hand; punish and harvest discards with Liliana's Caress, Waste Not, Tinybones, Bandit's Talent and Geth's Grimoire. *strategic_judgment · high*
- **Secondary:** Symmetric hand attack (Mind Twist, Hymn to Tourach, wheels under Notion Thief) and the Notion Thief + Teferi's Puzzle Box lock.
  - Evidence: [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md) · [crosis-01](../interactions/crosis-the-purger.md#crosis-01-pay-2b-on-resolution-then-choose-the-color) · [crosis-02](../interactions/crosis-the-purger.md#crosis-02-painters-servant-makes-crosis-a-full-hand-discard)
- **Commander role: central.** Crosis's combat trigger is the deck's largest discard event; equipment, Painter and haste pieces exist to make it land. *strategic_judgment · high*
- ⚠️ **Honest note:** Six mana, needs combat damage and another {2}{B}; the deck has no compact kill. It wins by attrition, discard punishment and combat, so the B4 rating comes more from the card pool (fast mana, Force of Will, Mind Twist) than from a fast win.
  - Evidence: [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md) · [crosis-01](../interactions/crosis-the-purger.md#crosis-01-pay-2b-on-resolution-then-choose-the-color) · [crosis-11](../interactions/crosis-the-purger.md#crosis-11-commander-tax-at-six-mana)
- **Dependency level:** high *strategic_judgment · high* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Bracket 4 — Optimized, not cEDH (current-cycle decisions).) | *fact · verified* | [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md) · [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md#L47](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Low-end Bracket 4: premium card pool, slow six-mana combat engine, no compact win. Agrees with the source.) | *strategic_judgment · high* | [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md) · [crosis-11](../interactions/crosis-the-purger.md#crosis-11-commander-tax-at-six-mana) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Crosis__the_Purger` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 6, "2": 90, "3": 77, "4": 23, "5": 1}, "decks_with_bracket": 197, "share_b4_plus": 0.122, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__crosis-the-purger.json`

## Win conditions

- **discard-punishment** (natural): Empty hands under Liliana's Caress, Bottomless Pit, Bandit's Talent and Tinybones drain plus Specter/Kroxa beats. Cards: Liliana's Caress, Bottomless Pit, Bandit's Talent, Tinybones, Trinket Thief, Kroxa, Titan of Death's Hunger. Enablers: Crosis, the Purger, Painter's Servant. *strategic_judgment · high* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)
- **commander-damage** (natural): Crosis with Sword of Feast and Famine / Brotherhood Regalia as a flying commander-damage clock against a discarded-out table. Cards: Crosis, the Purger, Sword of Feast and Famine, Brotherhood Regalia. Enablers: Swiftfoot Boots, Lightning Greaves. *strategic_judgment · moderate* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)
- **notion-puzzle-lock** (combo): Notion Thief + Teferi's Puzzle Box: opponents' draws become yours (a lock, not a kill). Cards: Notion Thief, Teferi's Puzzle Box. *fact · verified* — [crosis-07](../interactions/crosis-the-purger.md#crosis-07-notion-thief--teferis-puzzle-box-lock) · `spellbook:2286-3221`

## Engines

- **purge:** Crosis, the Purger, Painter's Servant, Brotherhood Regalia, Shizo, Death's Storehouse. Online when: Crosis deals combat damage and {2}{B} is available on resolution. *fact · verified* — [crosis-01](../interactions/crosis-the-purger.md#crosis-01-pay-2b-on-resolution-then-choose-the-color) · [crosis-02](../interactions/crosis-the-purger.md#crosis-02-painters-servant-makes-crosis-a-full-hand-discard)
- **discard-harvest:** Waste Not, Tinybones, Bauble Burglar, Geth's Grimoire, Tergrid, God of Fright // Tergrid's Lantern, Liliana's Caress. Online when: Opponents discard. *strategic_judgment · high* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:connect` | yes | 6 | Haste, evasion and protection so Crosis connects. | 9: Brotherhood Regalia, Sword of Feast and Famine, Swiftfoot Boots, Lightning Greaves, Shizo, Death's Storehouse, Plaza of Heroes, Cavern of Souls, Deflecting Swat, Fierce Guardianship | — | *strategic_judgment · high* | [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:discard-payoffs` | yes | 6 | Make discards hurt or pay. | 9: Liliana's Caress, Waste Not, Bottomless Pit, Bandit's Talent, Tinybones, Bauble Burglar, Tinybones, Trinket Thief, Tinybones, Pocket Nuisance, Geth's Grimoire, Tergrid, God of Fright // Tergrid's Lantern | — | *strategic_judgment · high* | [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:discard-sources` | yes | 8 | Additional discard so the payoffs fire without Crosis. | 10: Hymn to Tourach, Mind Twist, Blizzard Specter, Sedraxis Specter, Fell Specter, Tourach, Dread Cantor, The Raven Man, Oppression, Syphon Mind, Kroxa, Titan of Death's Hunger | — | *strategic_judgment · high* | [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:notion-wheels` | optional | 3 | One-sided wheels and the Puzzle Box lock. | 4: Notion Thief, Teferi's Puzzle Box, Wheel of Fortune, Windfall | — | *fact · verified* | [crosis-07](../interactions/crosis-the-purger.md#crosis-07-notion-thief--teferis-puzzle-box-lock) · [crosis-08](../interactions/crosis-the-purger.md#crosis-08-notion-thief-turns-wheels-one-sided) |

## Key interactions

- **pay-on-resolution:** Pay {2}{B} on resolution, then choose the color. (Crosis, the Purger) *fact · verified* — [crosis-01](../interactions/crosis-the-purger.md#crosis-01-pay-2b-on-resolution-then-choose-the-color)
- **painter:** Painter's Servant: name its color with Crosis for a full-hand discard. (Painter's Servant) *fact · verified* — [crosis-02](../interactions/crosis-the-purger.md#crosis-02-painters-servant-makes-crosis-a-full-hand-discard)
- **sword-painter:** Sword trigger above Crosis untaps lands for the payment; Painter's color can knock the Sword's protection off. (Sword of Feast and Famine, Painter's Servant) *fact · verified* — [crosis-03](../interactions/crosis-the-purger.md#crosis-03-painters-color-can-knock-sword-of-feast-and-famine-off-crosis) · [crosis-04](../interactions/crosis-the-purger.md#crosis-04-sword-of-feast-and-famine-above-crosis-untapped-lands-pay-2b)
- **tergrid-order:** Order Tergrid's trigger on top of Tinybones'. (Tergrid, God of Fright // Tergrid's Lantern, Tinybones, Trinket Thief) *fact · verified* — [crosis-06](../interactions/crosis-the-purger.md#crosis-06-tergrid-and-tinybones-order-tergrid-on-top)
- **oppression-symmetric:** Oppression is symmetric. (Oppression) *fact · moderate* — [crosis-10](../interactions/crosis-the-purger.md#crosis-10-oppression-is-symmetric)

## Tutors and recursion

- Tutor target **Painter's Servant** via Demonic Tutor, Vampiric Tutor, Gamble *strategic_judgment · high* — [crosis-02](../interactions/crosis-the-purger.md#crosis-02-painters-servant-makes-crosis-a-full-hand-discard)
- Tutor target **Brotherhood Regalia** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)
- Recursion: Reanimate, Dream Salvage, Kroxa, Titan of Death's Hunger *strategic_judgment · moderate* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md) · [crosis-09](../interactions/crosis-the-purger.md#crosis-09-recoil-and-dream-salvage)

## Requirements

- **Interaction:** Counters (Force of Will, Mana Drain, Swan Song) plus Toxic Deluge/Damnation for blockers.
- **Protection:** Two haste/protection equipment, Plaza, Regalia ward, free protection.
- **Mana:** Fast mana (Mana Vault, Chrome Mox, Mox Diamond, Dark Ritual) to land a six-drop early.
- *strategic_judgment · high* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **no-connection:** Crosis can't connect (flying blockers, removal). Mitigations: Regalia unblockable; Shizo fear; Sword pro-black/green. *strategic_judgment · high* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)
- **tapped-out:** No {2}{B} on resolution: the trigger does nothing. Mitigations: Sword untaps lands. *strategic_judgment · moderate* — [crosis-01](../interactions/crosis-the-purger.md#crosis-01-pay-2b-on-resolution-then-choose-the-color)
- **no-finisher:** Opponents stuck on empty hands but the deck lacks a fast kill. Mitigations: Bottomless Pit/Caress drain; Commander damage. *strategic_judgment · moderate* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)

## Identity core

- **Crosis, the Purger:** Combat-triggered color purge: the deck's defining discard event. *fact · verified* — `oracle:Crosis, the Purger`
- **Painter's Servant:** Makes every purge a full-hand discard. *strategic_judgment · high* — [crosis-02](../interactions/crosis-the-purger.md#crosis-02-painters-servant-makes-crosis-a-full-hand-discard)
- **Brotherhood Regalia:** Unblockable for {1} plus ward: the most direct connect enabler. *strategic_judgment · high* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)
- **Tinybones, Bauble Burglar:** Turns discarded cards into stolen plays. *strategic_judgment · high* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)
- **Waste Not:** Every discard type pays you mana, cards or Zombies. *strategic_judgment · moderate* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)

## Anti-goals and thematic constraints

- ✗ Don't add generic cEDH win packages or Painter + Grindstone combos (source decision).
- ✗ Don't drop the connect/protection count for more discard.
  - *strategic_judgment · high* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Dragon-legend control; Specters and discard creatures fit the theme.
  - *strategic_judgment · moderate* — [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.9:** Discard rules; Painter's color-setting makes all cards one color. *fact · verified* — `cr:701.9`
- **CR 903.8:** Commander tax on a six-drop that must survive combat. *fact · verified* — `cr:903.8`

## Supporting features (heuristic, not identity)

- `{"hooks": ["combat damage / attack triggers", "discard"], "hooked_cards": 30, "role_counts": {"counter": 5, "draw": 12, "protection": 4, "ramp": 15, "removal": 6, "tutor": 4, "wipe": 2}, "lands": 36, "edhrec_pages": ["crosis-the-purger"]}` *heuristic · low*

## Provenance

- Seeded from: [Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md) · [Crosis_the_Purger_Approval_Candidate_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Crosis_the_Purger_Approval_Candidate_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
