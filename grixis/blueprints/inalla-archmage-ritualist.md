# Blueprint — Inalla, Archmage Ritualist

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/inalla-archmage-ritualist.md), state `SOURCE_BASELINE`, list `lh1:c3f633472c2acd8e…`). Machine-readable source: [`data/grixis/blueprints/inalla-archmage-ritualist.json`](../../data/grixis/blueprints/inalla-archmage-ritualist.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Inalla, Archmage Ritualist** — Legendary Creature — Human Wizard

> Eminence — Whenever another nontoken Wizard you control enters, if Inalla is in the command zone or on the battlefield, you may pay {1}. If you do, create a token that's a copy of that Wizard. The token gains haste. Exile it at the beginning of the next end step.  
> Tap five untapped Wizards you control: Target player loses 7 life.

## Plan and commander role

- **Primary plan:** cEDH Wizard combo from the command zone: Inalla's Eminence copies each Wizard ETB (Spellseeker, Scholar of the Ages, Bloodline Necromancer, Ruthless Technomancer) for {1}, turning tutors and reanimation into Scholar sacrifice loops or the Bloodline/Technomancer loop for unbounded mana and Wizards. *strategic_judgment · high*
- **Secondary:** Commander-free backups: Thassa's Oracle + Consultation/Tainted Pact and Underworld Breach + LED + Brain Freeze/Wheel of Fortune.
  - Evidence: [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md) · [inalla-01](../interactions/inalla-archmage-ritualist.md#inalla-01-eminence-works-from-the-command-zone-once-per-trigger) · [inalla-03](../interactions/inalla-archmage-ritualist.md#inalla-03-inalla--bloodline-necromancer--ruthless-technomancer)
- **Commander role: central.** Eminence doubles every Wizard ETB without Inalla being cast; she's needed for the Bloodline + Technomancer loop and her five-Wizard tap closes it. *strategic_judgment · high*
- ⚠️ **Honest note:** The deck mostly doesn't cast her (decisions L16). The nine Scholar + sacrifice-ritual loops, Oracle and Breach all win without Inalla, and the one-card Spellseeker line is rated uncertain in M1 (inalla-06).
  - Evidence: [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md) · [inalla-06](../interactions/inalla-archmage-ritualist.md#inalla-06-spellseeker-one-card-line) · [inalla-04](../interactions/inalla-archmage-ritualist.md#inalla-04-scholar-of-the-ages--a-sacrifice-ritual--shallow-grave-or-persist)
- **Dependency level:** medium *strategic_judgment · high* — [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md) · [inalla-04](../interactions/inalla-archmage-ritualist.md#inalla-04-scholar-of-the-ages--a-sacrifice-ritual--shallow-grave-or-persist)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (Power Bracket 5 — cEDH (decisions).) | *fact · verified* | [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md#L103](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 5 (Bracket 5 ceiling: dense cEDH combo with 15 Spellbook infinites/compact wins and current tournament top cuts per the source. Agrees with the source.) | *strategic_judgment · high* | [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md) · `spellbook:1869-2721-3719` |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Inalla__Archmage_Ritualist` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 26, "2": 582, "3": 1036, "4": 832, "5": 815}, "decks_with_bracket": 3291, "share_b4_plus": 0.5, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__inalla-archmage-ritualist.json`

## Win conditions

- **bloodline-technomancer** (combo): Inalla + Bloodline Necromancer + Ruthless Technomancer: unbounded Treasures and Wizards, then Inalla's five-Wizard tap drains 7 at a time. Cards: Inalla, Archmage Ritualist, Bloodline Necromancer, Ruthless Technomancer. Enablers: Apprentice Necromancer. *fact · verified* — `spellbook:1869-2721-3719` · [inalla-03](../interactions/inalla-archmage-ritualist.md#inalla-03-inalla--bloodline-necromancer--ruthless-technomancer)
- **scholar-loops** (combo): Scholar of the Ages + Sacrifice/Burnt Offering/Culling the Weak + Persist, Shallow Grave or Saw in Half: unbounded mana. Cards: Scholar of the Ages, Sacrifice, Burnt Offering, Culling the Weak, Persist, Shallow Grave, Saw in Half. Enablers: Spellseeker, Inalla, Archmage Ritualist. *fact · verified* — `spellbook:813-1181-2171` · `spellbook:813-1181-1893` · `spellbook:813-1777-2171` · `spellbook:813-1777-1893` · `spellbook:813-2081-2171` · `spellbook:813-1893-2081` · `spellbook:500-813-1181` · `spellbook:500-813-1777` · `spellbook:500-813-2081` · [inalla-04](../interactions/inalla-archmage-ritualist.md#inalla-04-scholar-of-the-ages--a-sacrifice-ritual--shallow-grave-or-persist) · [inalla-05](../interactions/inalla-archmage-ritualist.md#inalla-05-saw-in-half--scholar-the-tokens-keep-mana-value-7)
- **oracle-breach** (combo): Thassa's Oracle + Consultation/Tainted Pact, or Breach + LED/Petal + Brain Freeze/Wheel. Cards: Thassa's Oracle, Demonic Consultation, Tainted Pact, Underworld Breach, Lion's Eye Diamond, Brain Freeze. *fact · verified* — `spellbook:742-1295` · `spellbook:1295-3093` · `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856` · `spellbook:1368-2706-3518` · [inalla-09](../interactions/inalla-archmage-ritualist.md#inalla-09-thassas-oracle-and-breach-lines)

## Engines

- **eminence-copies:** Inalla, Archmage Ritualist, Spellseeker, Thundertrap Trainer, Apprentice Necromancer, Vedalken Aethermage, Scholar of the Ages. Online when: A nontoken Wizard enters and you have {1}. *fact · verified* — [inalla-01](../interactions/inalla-archmage-ritualist.md#inalla-01-eminence-works-from-the-command-zone-once-per-trigger) · [inalla-08](../interactions/inalla-archmage-ritualist.md#inalla-08-hasty-wizard-copies-apprentice-necromancer-and-thundertrap-trainer)
- **fast-mana-tutors:** Mana Vault, Grim Monolith, Chrome Mox, Mox Diamond, Lotus Petal, Dark Ritual, Demonic Tutor, Vampiric Tutor, Imperial Seal, Entomb. Online when: Opening hand. *strategic_judgment · high* — [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:wizards` | yes | 8 | Wizards whose ETBs Inalla copies. | 8: Spellseeker, Scholar of the Ages, Bloodline Necromancer, Ruthless Technomancer, Apprentice Necromancer, Thundertrap Trainer, Vedalken Aethermage, Kefka, Court Mage // Kefka, Ruler of Ruin | — | *strategic_judgment · high* | [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:sac-reanimate` | yes | 8 | Sacrifice rituals and reanimation for Scholar loops. | 11: Sacrifice, Burnt Offering, Culling the Weak, Persist, Shallow Grave, Saw in Half, Reanimate, Animate Dead, Unearth, Entomb, Lively Dirge | — | *strategic_judgment · high* | [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md) · [inalla-04](../interactions/inalla-archmage-ritualist.md#inalla-04-scholar-of-the-ages--a-sacrifice-ritual--shallow-grave-or-persist) |
| `pkg:interaction` | yes | 6 | cEDH stack protection. | 7: Force of Will, Pact of Negation, Mental Misstep, Flusterstorm, Swan Song, Red Elemental Blast, An Offer You Can't Refuse | — | *strategic_judgment · high* | [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md) |

## Key interactions

- **eminence:** Eminence works from the command zone, one {1} per trigger; a zone change mid-trigger fizzles the copy. (Inalla, Archmage Ritualist) *fact · verified* — [inalla-01](../interactions/inalla-archmage-ritualist.md#inalla-01-eminence-works-from-the-command-zone-once-per-trigger)
- **tap-sick:** Tapping five Wizards ignores summoning sickness. (Inalla, Archmage Ritualist) *fact · verified* — [inalla-02](../interactions/inalla-archmage-ritualist.md#inalla-02-the-five-wizard-tap-ignores-summoning-sickness)
- **saw-scholar:** Saw in Half's Scholar tokens keep mana value 7. (Saw in Half, Scholar of the Ages) *fact · verified* — [inalla-05](../interactions/inalla-archmage-ritualist.md#inalla-05-saw-in-half--scholar-the-tokens-keep-mana-value-7)
- **spellseeker-uncertain:** The one-card Spellseeker line is uncertain; don't rely on it as deterministic. (Spellseeker) *fact · verified* — [inalla-06](../interactions/inalla-archmage-ritualist.md#inalla-06-spellseeker-one-card-line)
- **finale-timing:** Finale of Promise and Beseech cast during resolution; split second stops them. (Finale of Promise, Beseech the Mirror) *fact · verified* — [inalla-07](../interactions/inalla-archmage-ritualist.md#inalla-07-finale-and-beseech-cast-during-resolution-split-second-would-stop-them)

## Tutors and recursion

- Tutor target **Bloodline Necromancer** via Spellseeker, Vedalken Aethermage, Step Through *strategic_judgment · high* — `spellbook:1869-2721-3719`
- Tutor target **Scholar of the Ages** via Entomb, Demonic Tutor, Intuition *strategic_judgment · high* — `spellbook:813-1181-2171`
- Tutor target **Thassa's Oracle** via Vampiric Tutor, Mystical Tutor, Wishclaw Talisman *strategic_judgment · high* — `spellbook:742-1295`
- Recursion: Reanimate, Animate Dead, Unearth, Shallow Grave, Persist, Underworld Breach, Apprentice Necromancer *strategic_judgment · high* — [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Free counters and one-mana stack interaction.
- **Protection:** Cavern of Souls, counters.
- **Mana:** Fast mana and rituals; {1} spare per Eminence copy.
- *strategic_judgment · high* — [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **graveyard-hate:** Graveyard hate cuts Scholar loops and Breach. Mitigations: Bloodline/Technomancer loop; Oracle + Consultation. *strategic_judgment · high* — [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md)
- **eminence-fizzle:** A Wizard leaving mid-trigger stops the copy. Mitigations: Protect key ETBs. *strategic_judgment · moderate* — [inalla-01](../interactions/inalla-archmage-ritualist.md#inalla-01-eminence-works-from-the-command-zone-once-per-trigger)
- **split-second:** Split second stops Finale/Beseech casts mid-resolution. Mitigations: Alternate tutors. *strategic_judgment · moderate* — [inalla-07](../interactions/inalla-archmage-ritualist.md#inalla-07-finale-and-beseech-cast-during-resolution-split-second-would-stop-them)

## Identity core

- **Inalla, Archmage Ritualist:** Eminence copies of every Wizard ETB, plus a 7-life five-Wizard tap. *fact · verified* — `oracle:Inalla, Archmage Ritualist`
- **Scholar of the Ages:** Mana-value-7 Wizard at the centre of the sacrifice loops. *strategic_judgment · high* — [inalla-04](../interactions/inalla-archmage-ritualist.md#inalla-04-scholar-of-the-ages--a-sacrifice-ritual--shallow-grave-or-persist)
- **Bloodline Necromancer:** Half of the commander loop and Wizard reanimation. *strategic_judgment · high* — [inalla-03](../interactions/inalla-archmage-ritualist.md#inalla-03-inalla--bloodline-necromancer--ruthless-technomancer)
- **Spellseeker:** Wizard tutor for the combo instants and sorceries, doubled by Eminence. *strategic_judgment · high* — [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md)
- **Apprentice Necromancer:** Hasty token copy reanimates immediately. *strategic_judgment · moderate* — [inalla-08](../interactions/inalla-archmage-ritualist.md#inalla-08-hasty-wizard-copies-apprentice-necromancer-and-thundertrap-trainer)

## Anti-goals and thematic constraints

- ✗ Generic cEDH staples that don't exploit Inalla (e.g. Orcish Bowmasters) were rejected (decisions L77).
- ✗ Don't build around casting Inalla routinely; she works from the command zone.
  - *strategic_judgment · high* — [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md#L77](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Wizard ritualists; theme follows the Eminence engine.
  - *strategic_judgment · moderate* — [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.79a:** Persist. *fact · verified* — `cr:702.79a`
- **CR 702.10c:** Haste lets token copies use tap abilities immediately (Apprentice Necromancer). *fact · verified* — `cr:702.10c`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Wizard synergy", "copying", "enters triggers", "tokens"], "hooked_cards": 25, "role_counts": {"counter": 7, "draw": 5, "ramp": 20, "removal": 4, "tutor": 12, "wipe": 1}, "lands": 27, "edhrec_pages": ["inalla-archmage-ritualist"]}` *heuristic · low*

## Provenance

- Seeded from: [Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Inalla_Archmage_Ritualist_Current_Cycle_Decisions_2026-10-14.md) · [Inalla_Archmage_Ritualist_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Inalla_Archmage_Ritualist_Approved_2026-10-14.md) · [Inalla_Archmage_Ritualist_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Inalla_Archmage_Ritualist_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
