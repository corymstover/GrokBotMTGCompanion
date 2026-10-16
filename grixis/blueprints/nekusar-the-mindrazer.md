# Blueprint — Nekusar, the Mindrazer

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/nekusar-the-mindrazer.md), state `SOURCE_BASELINE`, list `lh1:0b5079ca21d51e48…`). Machine-readable source: [`data/grixis/blueprints/nekusar-the-mindrazer.json`](../../data/grixis/blueprints/nekusar-the-mindrazer.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Nekusar, the Mindrazer** — Legendary Creature — Zombie Wizard

> At the beginning of each player's draw step, that player draws an additional card.  
> Whenever an opponent draws a card, Nekusar deals 1 damage to that player.

## Plan and commander role

- **Primary plan:** Wheels and draw punishment: force opponents to draw many cards (wheels, Peer into the Abyss, Winds of Change) with Nekusar and overlapping pingers out, so each draw deals damage. *strategic_judgment · high*
- **Secondary:** Multiply Nekusar's Wizard triggers (Harmonic Prodigy, Wizard's Staff, Krang), use Ghyrson for exact-1 damage events, and loop Underworld Breach + Wheel of Fortune + Jeska's Will.
  - Evidence: [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)
- **Commander role: significant.** Nekusar is the best punisher and his draw-step trigger gives every opponent an extra draw to punish. *strategic_judgment · high*
- ⚠️ **Honest note:** The source says outright that without Nekusar the deck still works as a wheel/group-slug deck (blueprint L55) and that the punishers were chosen so it isn't commander-or-bust (L29). Only 1 of 7 Spellbook combos needs him (Nekusar + Peer into the Abyss). He multiplies the plan rather than being required by it. The cycle 51 M1 review (nekusar-01..09) verifies the engines and flags Krang self-damage (nekusar-03).
  - Evidence: [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L55](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) · `spellbook:1561-1972`
- **Dependency level:** medium *strategic_judgment · high* — [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L55](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: fast mana, wheels and Peer/Breach kills, but a group-slug plan that the source deliberately keeps clear of Oracle shortcuts. Agrees with the source.) | *strategic_judgment · high* | [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Nekusar__the_Mindrazer` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 53, "2": 1374, "3": 2892, "4": 2610, "5": 291}, "decks_with_bracket": 7220, "share_b4_plus": 0.402, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__nekusar-the-mindrazer.json`

## Win conditions

- **peer-punish** (combo): Peer into the Abyss on an opponent with Nekusar, Sheoldred, Orcish Bowmasters, Razorkin Needlehead or Underworld Dreams out deals lethal draw damage. Cards: Peer into the Abyss, Nekusar, the Mindrazer, Sheoldred, the Apocalypse, Orcish Bowmasters, Razorkin Needlehead, Underworld Dreams. *fact · verified* — `spellbook:1561-1972` · `spellbook:1561-2498` · `spellbook:1561-3862` · `spellbook:1561-5919` · `spellbook:1561-2720`
- **breach-wheel** (combo): Underworld Breach + Wheel of Fortune + Jeska's Will: repeated wheels for punishment damage. Cards: Underworld Breach, Wheel of Fortune, Jeska's Will. Enablers: Fate Unraveler, Underworld Dreams, Sheoldred, the Apocalypse. *fact · verified* — `spellbook:1368-1878-2706`
- **curiosity-niv** (combo): Curiosity on Niv-Mizzet, Parun: an infinite draw/damage loop. Cards: Curiosity, Niv-Mizzet, Parun. *fact · verified* — `spellbook:1089-2353`
- **wheel-damage** (natural): Wheels with multiple punishers out deal table-wide damage over a few turns. Cards: Nekusar, the Mindrazer, Wheel of Fortune, Windfall, Wheel and Deal, Echo of Eons. Enablers: Fate Unraveler, Underworld Dreams, Sheoldred, the Apocalypse, Spiteful Visions, Phyrexian Tyranny, Kederekt Parasite, Razorkin Needlehead, Scrawling Crawler, Orcish Bowmasters, Ghyrson Starn, Kelermorph. *strategic_judgment · high* — [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)

## Engines

- **draw-punish:** Nekusar, the Mindrazer, Fate Unraveler, Underworld Dreams, Sheoldred, the Apocalypse, Spiteful Visions, Phyrexian Tyranny, Kederekt Parasite, Razorkin Needlehead, Scrawling Crawler, Orcish Bowmasters, Ghyrson Starn, Kelermorph. Online when: One or more punishers in play before the wheel. *fact · high* — `oracle:Nekusar, the Mindrazer` · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)
- **wizard-multipliers:** Nekusar, the Mindrazer, Harmonic Prodigy, Wizard's Staff, Krang, the All-Powerful. Online when: Nekusar in play. *fact · high* — [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:wheels` | yes | 8 | Force many real draws cheaply. | 12: Wheel of Fortune, Windfall, Wheel and Deal, Echo of Eons, Reforge the Soul, Magus of the Wheel, Wheel of Misfortune, Whispering Madness, Burning Inquiry, Winds of Change, Molten Psyche, Peer into the Abyss | — | *strategic_judgment · high* | [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) |
| `pkg:punishers` | yes | 8 | Redundant draw punishment so it isn't commander-or-bust. | 10: Fate Unraveler, Underworld Dreams, Sheoldred, the Apocalypse, Spiteful Visions, Phyrexian Tyranny, Kederekt Parasite, Razorkin Needlehead, Scrawling Crawler, Orcish Bowmasters, Ghyrson Starn, Kelermorph | — | *strategic_judgment · high* | [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) |
| `pkg:interaction` | yes | 6 | Cheap stack interaction and resets. | 9: Force of Will, Force of Negation, Fierce Guardianship, Mana Drain, Swan Song, Arcane Denial, Deflecting Swat, Toxic Deluge, Cyclonic Rift | — | *strategic_judgment · high* | [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) |

## Key interactions

- **krang-vs-draw-step:** Wizard's Staff/Harmonic Prodigy add instances of Nekusar's draw-step trigger; Krang doesn't, because a draw didn't cause that trigger. Krang adds damage-trigger instances only. (Nekusar, the Mindrazer, Krang, the All-Powerful, Harmonic Prodigy, Wizard's Staff) *fact · verified* — [nekusar-02](../interactions/nekusar-the-mindrazer.md#nekusar-02-wizards-staff--harmonic-prodigy--krang-additive-and-krang-skips-the-draw-step-trigger) · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)
- **ghyrson-exact-one:** Ghyrson Starn needs exactly 1 damage; damage-increasing replacement effects turn it off, so they were rejected. (Ghyrson Starn, Kelermorph, Nekusar, the Mindrazer) *fact · verified* — [nekusar-04](../interactions/nekusar-the-mindrazer.md#nekusar-04-ghyrson-starn-wants-exactly-1-damage-doublers-would-break-it) · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)
- **draw-step-extra:** Nekusar's extra draw is a triggered draw separate from the turn-based draw. (Nekusar, the Mindrazer) *fact · verified* — [nekusar-07](../interactions/nekusar-the-mindrazer.md#nekusar-07-draw-step-stack-normal-draw-then-order-nekusars-extra-draws-before-teferis-puzzle-box) · `cr:121.1` · `cr:504.1`
- **curiosity-nekusar:** Curiosity on Nekusar draws a card for each damage event. (Curiosity, Nekusar, the Mindrazer) *fact · verified* — [nekusar-06](../interactions/nekusar-the-mindrazer.md#nekusar-06-curiosity-on-niv-mizzet-loops-on-nekusar-its-value) · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)
- **krang-self-damage:** M1 flag: Krang also doubles Spiteful Visions and Phyrexian Tyranny on your own draws; wheel with care. (Krang, the All-Powerful, Spiteful Visions, Phyrexian Tyranny) *strategic_judgment · moderate* — [nekusar-03](../interactions/nekusar-the-mindrazer.md#nekusar-03-krang-also-doubles-spiteful-visions-and-phyrexian-tyranny-on-your-own-draws)
- **discard-vs-shuffle:** Waste Not and Liliana's Caress need discard wheels; shuffle wheels don't trigger them. Molten Psyche counts all draws. (Wheel of Fortune, Windfall, Waste Not, Liliana's Caress, Molten Psyche) *fact · verified* — [nekusar-08](../interactions/nekusar-the-mindrazer.md#nekusar-08-wheels-discard-vs-shuffle--waste-not-and-lilianas-caress-need-discard-molten-psyche-counts-all-draws)

## Tutors and recursion

- Tutor target **Peer into the Abyss** via Demonic Tutor, Vampiric Tutor, Mystical Tutor *strategic_judgment · high* — `spellbook:1561-1972`
- Tutor target **Underworld Breach** via Demonic Tutor, Mystical Tutor *strategic_judgment · moderate* — `spellbook:1368-1878-2706`
- Recursion: Underworld Breach, Jeska's Will, Echo of Eons *strategic_judgment · moderate* — [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)

## Requirements

- **Interaction:** Free and cheap counters, Toxic Deluge, Cyclonic Rift.
- **Protection:** Fierce Guardianship, Deflecting Swat.
- **Mana:** 35 lands, Mana Vault, Grim Monolith, Chrome Mox, Dark Ritual, Talismans; triple pips for Niv-Mizzet.
- *strategic_judgment · moderate* — [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)

## Failure modes

- **five-mana-setup:** A five-mana setup before the wheels; wheels without punishers refill opponents. Mitigations: Punisher redundancy. *strategic_judgment · high* — [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)
- **draw-locks:** Opposing Narset/Notion Thief turn the deck off. Mitigations: Removal; Counters. *strategic_judgment · high* — [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)
- **lifegain:** Lifegain blunts the slug damage. Mitigations: Compact Peer kills. *strategic_judgment · moderate* — [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)

## Identity core

- **Nekusar, the Mindrazer:** Extra draws plus a damage trigger. *fact · verified* — `oracle:Nekusar, the Mindrazer`
- **Peer into the Abyss:** The compact kill. *strategic_judgment · high* — `spellbook:1561-1972`
- **Wizard's Staff:** Doubles Nekusar's triggers. *strategic_judgment · high* — [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)
- **Wheel of Fortune:** Best wheel, and the Breach loop. *strategic_judgment · high* — `spellbook:1368-1878-2706`
- **Underworld Dreams:** Redundant punisher. *strategic_judgment · high* — [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No Narset/Notion Thief wheel locks (blueprint L59).
- ✗ No Thassa's Oracle package (L60), no infect shortcuts (L61), no Mindcrank package (L62).
  - *strategic_judgment · high* — [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) · [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L62](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)
- Theme: Wheels / draw punishment / group slug.
  - *strategic_judgment · high* — [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 121.1:** Drawing a card. *fact · verified* — `cr:121.1`
- **CR 504.1:** Draw step turn-based action. *fact · verified* — `cr:504.1`

## Supporting features (heuristic, not identity)

- `{"hooks": ["opponents drawing (wheels / punishers)"], "hooked_cards": 23, "role_counts": {"counter": 7, "draw": 32, "protection": 1, "ramp": 12, "removal": 4, "tutor": 3, "wipe": 1}, "lands": 35, "edhrec_pages": ["nekusar-the-mindrazer"]}` *heuristic · low*

## Provenance

- Seeded from: [Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nekusar_the_Mindrazer_Commander_Blueprint_2026-10-15.md) · [Nekusar_the_Mindrazer_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Nekusar_the_Mindrazer_Candidate_Decisions_2026-10-15.md) · [Nekusar_the_Mindrazer_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Nekusar_the_Mindrazer_Approved_2026-10-15.md) · [Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nekusar_the_Mindrazer_Approval_Ready_Verification_2026-10-15.md) · [Nekusar_the_Mindrazer_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nekusar_the_Mindrazer_Whole_List_Audit_2026-10-15.md) · [Nekusar_the_Mindrazer_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Nekusar_the_Mindrazer_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
