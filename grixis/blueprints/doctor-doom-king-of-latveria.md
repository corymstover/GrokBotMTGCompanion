# Blueprint — Doctor Doom, King of Latveria

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/doctor-doom-king-of-latveria.md), state `SOURCE_BASELINE`, list `lh1:bdc7cc1f7dc0eeb6…`). Machine-readable source: [`data/grixis/blueprints/doctor-doom-king-of-latveria.json`](../../data/grixis/blueprints/doctor-doom-king-of-latveria.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Doctor Doom, King of Latveria** — Legendary Creature — Human Noble Villain

> Whenever you discard one or more land cards, each opponent loses 2 life.  
> At the beginning of combat on your turn, target Villain you control gains menace until end of turn. It connives. (Draw a card, then discard a card. If you discarded a nonland card, put a +1/+1 counter on that creature.)

## Plan and commander role

- **Primary plan:** Lands as discard ammunition: discard land cards in separate events (cycling, Trade Routes, Seismic Assault, Psychic Frog, rummaging) so each event drains every opponent for 2, then recover the lands (Crucible, Moonstone, Containment Construct) and repeat. *strategic_judgment · high*
- **Secondary:** Villain/connive shell: Doom's combat connive on a Villain plus Lethal Scheme, Kang, Ultron, Glorious Purpose; Doom trigger copies (Chameleon, Spark Double, Roaming Throne) and the Tectonic Reformation + Surly Badgersaur + Dakmor Salvage infinite.
  - Evidence: [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md) · [doom-01](../interactions/doctor-doom-king-of-latveria.md#doom-01) · [doom-08](../interactions/doctor-doom-king-of-latveria.md#doom-08)
- **Commander role: central.** Doom is the drain: every separate land-discard event is 2 from each opponent, and his combat connive filters toward more lands and Villain value. *strategic_judgment · high*
- ⚠️ **Honest note:** One trigger per discard event, not per land: mass discards (wheels) give one trigger. The kill is multi-piece and resource-dependent.
  - Evidence: [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md) · [doom-01](../interactions/doctor-doom-king-of-latveria.md#doom-01) · [doom-02](../interactions/doctor-doom-king-of-latveria.md#doom-02)
- **Dependency level:** high *strategic_judgment · high* — [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Bracket 4 — Optimized (current-cycle blueprint).) | *fact · verified* | [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: one three-card infinite and repeatable table drain; multi-piece, resource-dependent kill. Agrees with the source.) | *strategic_judgment · high* | [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md) · [doom-08](../interactions/doctor-doom-king-of-latveria.md#doom-08) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Doctor_Doom__King_of_Latveria` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 16, "2": 751, "3": 912, "4": 210, "5": 23}, "decks_with_bracket": 1912, "share_b4_plus": 0.122, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__doctor-doom-king-of-latveria.json`

## Win conditions

- **badgersaur-reformation-dakmor** (combo): Tectonic Reformation + Surly Badgersaur + Dakmor Salvage: cycle Dakmor for {R}, Badgersaur makes Treasure, dredge it back; each cycle is a Doom drain. Cards: Tectonic Reformation, Surly Badgersaur, Dakmor Salvage. Enablers: Doctor Doom, King of Latveria. *fact · verified* — [doom-08](../interactions/doctor-doom-king-of-latveria.md#doom-08) · `spellbook:779-2546-4467`
- **trade-routes-engine** (natural): Trade Routes + Bone Miser or Badgersaur + Dakmor: repeated land discards fund the next activation. Cards: Trade Routes, Bone Miser, Surly Badgersaur, Dakmor Salvage. *fact · moderate* — [doom-09](../interactions/doctor-doom-king-of-latveria.md#doom-09)
- **repeated-drain** (natural): Seismic Assault, Psychic Frog and cycling lands drain 2 per event; Archfiend of Ifnir and Cool but Rude add more. Cards: Seismic Assault, Psychic Frog, Archfiend of Ifnir, Cool but Rude, Monument to Endurance. Enablers: Crucible of Worlds. *strategic_judgment · high* — [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md)

## Engines

- **land-discard-drain:** Doctor Doom, King of Latveria, Psychic Frog, Seismic Assault, Trade Routes, Archfiend of Ifnir. Online when: Separate land-discard events. *fact · verified* — [doom-01](../interactions/doctor-doom-king-of-latveria.md#doom-01) · [doom-06](../interactions/doctor-doom-king-of-latveria.md#doom-06) · [doom-11](../interactions/doctor-doom-king-of-latveria.md#doom-11)
- **land-recursion:** Crucible of Worlds, Moonstone, Harsh Mistress, Containment Construct, Shadow of the Grave, Dakmor Salvage. Online when: Lands in the graveyard to replay or redraw. *fact · verified* — [doom-07](../interactions/doctor-doom-king-of-latveria.md#doom-07) · [doom-10](../interactions/doctor-doom-king-of-latveria.md#doom-10)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:land-discard-outlets` | yes | 6 | Discard lands one event at a time. | 8: Psychic Frog, Seismic Assault, Trade Routes, Faithless Looting, Frantic Search, Tectonic Reformation, Desolate Lighthouse, Geier Reach Sanitarium | — | *strategic_judgment · high* | [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md) |
| `pkg:land-recursion` | yes | 4 | Recover discarded lands. | 5: Crucible of Worlds, Moonstone, Harsh Mistress, Containment Construct, Shadow of the Grave, Dakmor Salvage | — | *strategic_judgment · high* | [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md) |
| `pkg:doom-copies` | yes | 3 | Copy Doom's triggers. | 3: Chameleon, Master of Disguise, Spark Double, Roaming Throne | — | *strategic_judgment · high* | [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md) · [doom-03](../interactions/doctor-doom-king-of-latveria.md#doom-03) · [doom-04](../interactions/doctor-doom-king-of-latveria.md#doom-04) |
| `pkg:villains-connive` | optional | 6 | Villains for the combat connive and connive payoffs. | 9: Lethal Scheme, Kang, Temporal Tyrant, Ultron, Unlimited, Villainous Hideout, Glorious Purpose, Norman Osborn // Green Goblin, Prowler, Clawed Thief, Tombstone, Career Criminal, Leader, Super-Genius | — | *strategic_judgment · high* | [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md) |

## Key interactions

- **per-event:** One Doom trigger per discard event, not per land; Cool but Rude counts per card. (Doctor Doom, King of Latveria, Cool but Rude) *fact · verified* — [doom-01](../interactions/doctor-doom-king-of-latveria.md#doom-01)
- **connive-target:** The combat connive targets a Villain; with no legal target, no connive. (Doctor Doom, King of Latveria) *fact · verified* — [doom-02](../interactions/doctor-doom-king-of-latveria.md#doom-02)
- **chameleon:** Chameleon copy keeps its own name: no legend rule. (Chameleon, Master of Disguise) *fact · verified* — [doom-03](../interactions/doctor-doom-king-of-latveria.md#doom-03)
- **dakmor:** Dakmor Salvage dredge is renewable, bounded by library size. (Dakmor Salvage) *fact · verified* — [doom-07](../interactions/doctor-doom-king-of-latveria.md#doom-07)
- **crucible-cycling:** Crucible doesn't let you cycle lands from the graveyard. (Crucible of Worlds) *fact · verified* — [doom-10](../interactions/doctor-doom-king-of-latveria.md#doom-10)

## Tutors and recursion

- Tutor target **Tectonic Reformation** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [doom-08](../interactions/doctor-doom-king-of-latveria.md#doom-08)
- Tutor target **Seismic Assault** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md)
- Recursion: Crucible of Worlds, Moonstone, Harsh Mistress, Containment Construct, Shadow of the Grave, Reanimate *fact · verified* — [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md)

## Requirements

- **Interaction:** Counters (Swan Song, Fierce Guardianship) and removal; graveyard hate is a real threat.
- **Protection:** Free protection; Doom is four mana.
- **Mana:** Many lands (fuel and mana); Treasure from Badgersaur/Bone Miser.
- *strategic_judgment · moderate* — [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md)

## Failure modes

- **mass-discard:** Discarding many lands at once is only one trigger. Mitigations: Prefer per-card outlets (Frog, cycling). *strategic_judgment · high* — [doom-01](../interactions/doctor-doom-king-of-latveria.md#doom-01)
- **graveyard-hate:** Graveyard exile stops land recursion and Dakmor. Mitigations: Crucible still replays from hand discard cycles. *strategic_judgment · moderate* — [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md)
- **no-villain:** No Villain on board: no combat connive. Mitigations: Villain density. *strategic_judgment · moderate* — [doom-02](../interactions/doctor-doom-king-of-latveria.md#doom-02)

## Identity core

- **Doctor Doom, King of Latveria:** 2-life table drain per land-discard event. *fact · verified* — `oracle:Doctor Doom, King of Latveria`
- **Psychic Frog:** Free, repeatable land-discard outlet: one Doom trigger per activation. *strategic_judgment · high* — [doom-06](../interactions/doctor-doom-king-of-latveria.md#doom-06)
- **Seismic Assault:** Each land discard is a separate event: Doom drain plus 2 damage. *strategic_judgment · high* — [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md)
- **Crucible of Worlds:** Replays discarded lands so the ammunition doesn't run out. *strategic_judgment · high* — [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md)
- **Dakmor Salvage:** Renewable land to discard; centre of the infinite. *strategic_judgment · moderate* — [doom-08](../interactions/doctor-doom-king-of-latveria.md#doom-08)

## Anti-goals and thematic constraints

- ✗ Don't add generic Thassa's Oracle/Consultation cEDH packages (source blueprint).
- ✗ Don't treat it as generic Villain tribal or generic discard.
  - *strategic_judgment · high* — [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md)
- Theme: Marvel villains.
  - *strategic_judgment · moderate* — [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.50a:** Connive: draw, then discard; a nonland discard adds a +1/+1 counter. *fact · verified* — `cr:701.50a`
- **CR 702.52:** Dredge replaces a draw (Dakmor Salvage). *fact · verified* — `cr:702.52`

## Supporting features (heuristic, not identity)

- `{"hooks": ["+1/+1 counters", "Villain synergy", "connive / looting", "discard", "opponents losing life"], "hooked_cards": 41, "role_counts": {"counter": 2, "draw": 19, "protection": 1, "ramp": 16, "removal": 6, "tutor": 3, "wipe": 1}, "lands": 38, "edhrec_pages": ["doctor-doom-king-of-latveria"]}` *heuristic · low*

## Provenance

- Seeded from: [Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Doctor_Doom_King_of_Latveria_Current_Cycle_Blueprint_2026-10-14.md) · [Doctor_Doom_King_of_Latveria_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Doctor_Doom_King_of_Latveria_Approved_2026-10-14.md) · [Doctor_Doom_King_of_Latveria_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Doctor_Doom_King_of_Latveria_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
