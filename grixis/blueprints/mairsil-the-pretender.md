# Blueprint — Mairsil, the Pretender

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/mairsil-the-pretender.md), state `SOURCE_BASELINE`, list `lh1:044e0d1ae699b318…`). Machine-readable source: [`data/grixis/blueprints/mairsil-the-pretender.json`](../../data/grixis/blueprints/mairsil-the-pretender.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Mairsil, the Pretender** — Legendary Creature — Human Wizard

> When Mairsil enters, you may exile an artifact or creature card from your hand or graveyard and put a cage counter on it.  
> Mairsil has all activated abilities of all cards you own in exile with cage counters on them. You may activate each of those abilities only once each turn.

## Plan and commander role

- **Primary plan:** Cage toolbox: put cards with strong activated abilities into hand or graveyard (Entomb, Buried Alive, Faithless Looting), re-enter, blink or copy Mairsil to cage more, use haste and untaps for repeated tap abilities, and close with Mairsil-dependent activated-ability loops. *strategic_judgment · high*
- **Secondary:** Exploit caged cards whose drawbacks aren't copied (Asmodeus draws seven cleanly) and grind with Arcanis, Pack Rat copies and Rings of Brighthearth.
  - Evidence: [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) · [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L56](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- **Commander role: central.** Mairsil is the engine: every caged ability lives on him, and five of the six Spellbook combos include him. *strategic_judgment · high*
- ⚠️ **Honest note:** Each acquired ability is once per turn per Mairsil object, so the loops need fresh objects (Quicksilver Elemental, blinks, copies). The deck is fragile to graveyard and exile hate on caged cards. This deck has no M1 interaction review yet (batch D is in progress), so the rules notes rest on the source's verification and Oracle text.
  - Evidence: [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) · [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- **Dependency level:** high *strategic_judgment · high* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions closeout).) | *fact · verified* | [Mairsil_the_Pretender_Current_Cycle_Decisions_2026-10-14.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mairsil_the_Pretender_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling, high end: lethal, tutor-dense, fast-mana combo toolbox, kept below cEDH to preserve the cage identity per the source. Agrees with the source.) | *strategic_judgment · high* | [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) · `spellbook:1369-2645-5112-5116` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Mairsil__the_Pretender` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 16, "2": 117, "3": 241, "4": 116, "5": 39}, "decks_with_bracket": 529, "share_b4_plus": 0.293, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__mairsil-the-pretender.json`

## Win conditions

- **quicksilver-lotus** (combo): Mairsil + Quicksilver Elemental + Gilded Lotus with Staff of Domination, Horseshoe Crab or Morphling: unbounded mana and activations. Cards: Mairsil, the Pretender, Quicksilver Elemental, Gilded Lotus, Staff of Domination, Horseshoe Crab, Morphling. Enablers: Walking Ballista. *fact · verified* — `spellbook:1369-2645-5112-5116` · `spellbook:1369-3995-5112-5116` · `spellbook:1369-5112-5116-5137` · [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- **rings-alchemist** (combo): Rings of Brighthearth + Aphetto Alchemist + Gilded Lotus: unbounded mana. Cards: Rings of Brighthearth, Aphetto Alchemist, Gilded Lotus. *fact · verified* — `spellbook:4091-4235-5116`
- **mairsil-lines** (combo): Mairsil + Hateflayer + Tree of Perdition, and Mairsil + Aetherling + Anger + Nevinyrral's Disk. Cards: Mairsil, the Pretender, Hateflayer, Tree of Perdition, Aetherling, Anger, Nevinyrral's Disk. *fact · verified* — `spellbook:2615-4449-5112` · `spellbook:1050-4068-4439-5112`

## Engines

- **re-cage:** Mairsil, the Pretender, Essence Flux, Displacer Kitten, Spark Double, Pack Rat, Rings of Brighthearth. Online when: Mairsil re-enters or is copied. *fact · high* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) · [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) · [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- **tap-payloads:** Arcanis the Omnipotent, Asmodeus the Archfiend, Minamo, School at Water's Edge, Patriar's Seal, Anger, Thousand-Year Elixir, Training Grounds. Online when: Payloads caged with haste/untap available. *fact · high* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) · [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L56](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) · [Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:cage-payloads` | yes | 10 | Activated abilities worth caging. | 14: Aetherling, Aphetto Alchemist, Arcanis the Omnipotent, Asmodeus the Archfiend, Cephalid Inkshrouder, Hateflayer, Horseshoe Crab, Morphling, Pack Rat, Quicksilver Elemental, Tree of Perdition, Staff of Domination, Walking Ballista, Torchling | — | *strategic_judgment · high* | [Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv) |
| `pkg:graveyard-setup` | yes | 5 | Put payloads where Mairsil can cage them. | 6: Entomb, Buried Alive, Faithless Looting, Frantic Search, Intuition, Unmarked Grave | — | *strategic_judgment · high* | [Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv) |
| `pkg:re-entry` | yes | 4 | Fresh Mairsil objects and more cage triggers. | 5: Essence Flux, Displacer Kitten, Spark Double, Marvin, Murderous Mimic, Pack Rat | — | *strategic_judgment · high* | [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) · [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) |

## Key interactions

- **once-per-object:** Each acquired ability once per turn per Mairsil object; blinks make a new object with fresh uses. (Mairsil, the Pretender, Essence Flux, Displacer Kitten) *fact · high* — `oracle:Mairsil, the Pretender` · [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- **asmodeus:** Mairsil gains Asmodeus's draw-seven but not its replacement effect. (Asmodeus the Archfiend) *fact · high* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L56](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- **rings-pack-rat:** Rings copies the caged Pack Rat activation without the discard cost: another Mairsil copy and cage trigger. (Rings of Brighthearth, Pack Rat) *fact · high* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L58](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- **marvin:** Marvin gains Mairsil's acquired activated abilities without the once-per-turn static. (Marvin, Murderous Mimic) *fact · high* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- **spark-double:** Spark Double copies Mairsil's printed cage ability and triggers its ETB. (Spark Double) *fact · high* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)

## Tutors and recursion

- Tutor target **Quicksilver Elemental** via Entomb, Buried Alive, Demonic Tutor *strategic_judgment · high* — `spellbook:1369-2645-5112-5116`
- Tutor target **Gilded Lotus** via Vampiric Tutor, Wishclaw Talisman *strategic_judgment · moderate* — `spellbook:1369-2645-5112-5116`
- Recursion: Essence Flux, Unmarked Grave, Mairsil, the Pretender *strategic_judgment · moderate* — [Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv)

## Requirements

- **Interaction:** Force of Will, Fierce Guardianship, Swan Song, An Offer You Can't Refuse, Deadly Rollick, Toxic Deluge, Cyclonic Rift.
- **Protection:** Lightning Greaves, Deflecting Swat, Aetherling and Cephalid Inkshrouder cages.
- **Mana:** 32 lands, Mana Vault, Chrome Mox, Mox Diamond, Lotus Petal, Gilded Lotus.
- *strategic_judgment · high* — [Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv)

## Failure modes

- **mairsil-removed:** Without Mairsil the caged abilities are inaccessible. Mitigations: Aetherling cage; Greaves; Counters. *strategic_judgment · high* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- **graveyard-hate:** Graveyard hate stops caging from the yard. Mitigations: Cage from hand. *strategic_judgment · high* — [Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv)
- **unsafe-lines:** Self-mill lines like Mirror-Mad Phantasm were cut as unsafe. Mitigations: Use the verified Quicksilver lines. *strategic_judgment · moderate* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)

## Identity core

- **Mairsil, the Pretender:** Gains the activated abilities of every caged card. *fact · verified* — `oracle:Mairsil, the Pretender`
- **Quicksilver Elemental:** Fresh ability instances for the infinite-mana lines. *strategic_judgment · high* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- **Asmodeus the Archfiend:** Draw seven without the drawback. *strategic_judgment · high* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L56](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- **Pack Rat:** Caged copy-maker for more cage triggers. *strategic_judgment · high* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L58](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- **Minamo, School at Water's Edge:** Untaps Mairsil for another tap ability. *strategic_judgment · moderate* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)

## Anti-goals and thematic constraints

- ✗ Don't replace the cage-toolbox identity with a tournament cEDH shell (verification L37).
- ✗ Avoid unsafe self-mill lines (verification L60).
  - *strategic_judgment · high* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)
- Theme: Mairsil the pretender: caged cards and borrowed powers.
  - *strategic_judgment · moderate* — [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 400.7:** A blinked Mairsil is a new object with fresh activation limits. *fact · verified* — `cr:400.7`
- **CR 602.5b:** Activation restrictions apply per object. *fact · verified* — `cr:602.5b`

## Supporting features (heuristic, not identity)

- `{"hooks": ["artifacts"], "hooked_cards": 25, "role_counts": {"counter": 4, "draw": 7, "protection": 4, "ramp": 17, "removal": 6, "tutor": 9, "wipe": 3}, "lands": 32, "edhrec_pages": ["mairsil-the-pretender"]}` *heuristic · low*

## Provenance

- Seeded from: [Mairsil_the_Pretender_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mairsil_the_Pretender_Current_Cycle_Decisions_2026-10-14.md) · [Mairsil_the_Pretender_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Mairsil_the_Pretender_Approved_2026-10-14.md) · [Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mairsil_the_Pretender_Whole_List_Audit_2026-10-14.csv) · [Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Mairsil_the_Pretender_Approval_Ready_Verification_2026-10-14.md) · [Mairsil_the_Pretender_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Mairsil_the_Pretender_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
