# Blueprint — Anhelo, the Painter

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/anhelo-the-painter.md), state `SOURCE_BASELINE`, list `lh1:627cae661f5af180…`). Machine-readable source: [`data/grixis/blueprints/anhelo-the-painter.json`](../../data/grixis/blueprints/anhelo-the-painter.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Anhelo, the Painter** — Legendary Creature — Vampire Assassin

> Deathtouch  
> The first instant or sorcery spell you cast each turn has casualty 2. (As you cast that spell, you may sacrifice a creature with power 2 or greater. When you do, copy the spell and you may choose new targets for the copy.)

## Plan and commander role

- **Primary plan:** Spell-copy spellslinger: keep cheap power-2+ bodies around to pay casualty 2 on the first instant or sorcery each turn (on every player's turn), copying tutors, removal, extra turns and finishers. *strategic_judgment · high*
- **Secondary:** Commander-independent spell-copy infinites (Twinning Staff or Reiterate + Narset's Reversal, Dualcaster Mage + Twinflame, Reiterate + Mana Geyser/Jeska's Will, Primal Wellspring + Frantic Search).
  - Evidence: [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md) · [anhelo-01](../interactions/anhelo-the-painter.md#anhelo-01) · [anhelo-07](../interactions/anhelo-the-painter.md#anhelo-07) · [anhelo-09](../interactions/anhelo-the-painter.md#anhelo-09)
- **Commander role: significant.** Anhelo turns one spell per turn into two and makes token makers double as copy fuel; his deathtouch body also blocks. *strategic_judgment · moderate*
- ⚠️ **Honest note:** The deck's kills are mostly two-card spell-copy infinites that do not need Anhelo; he is a value engine (one casualty per turn), not the win condition. Calling him 'central' would overstate it.
  - Evidence: [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md) · [anhelo-01](../interactions/anhelo-the-painter.md#anhelo-01) · [anhelo-07](../interactions/anhelo-the-painter.md#anhelo-07) · [anhelo-09](../interactions/anhelo-the-painter.md#anhelo-09) · [anhelo-14](../interactions/anhelo-the-painter.md#anhelo-14)
- **Dependency level:** medium *strategic_judgment · moderate* — [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md) · [anhelo-07](../interactions/anhelo-the-painter.md#anhelo-07) · [anhelo-09](../interactions/anhelo-the-painter.md#anhelo-09)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | — (none stated) (No source ceiling stated in the source blueprint, slot audit or closeout (checked Bot cycle 50).) | *fact · high* | [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md) · [Anhelo_the_Painter_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Anhelo_the_Painter_Approval_Ready_Closeout_2026-10-13.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: eight Spellbook infinites, several of them two-card, with tutors and free counters; the commander is a value engine, not cEDH-speed.) | *strategic_judgment · high* | [anhelo-07](../interactions/anhelo-the-painter.md#anhelo-07) · [anhelo-09](../interactions/anhelo-the-painter.md#anhelo-09) · `spellbook:11-2539` · `spellbook:147-1235` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Anhelo__the_Painter` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | — (no source ceiling) | | |

- EDHREC: `{"bracket_counts": {"1": 24, "2": 649, "3": 553, "4": 171, "5": 30}, "decks_with_bracket": 1427, "share_b4_plus": 0.141, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__anhelo-the-painter.json`

## Win conditions

- **narset-reversal-loop** (combo): Narset's Reversal copying itself with Twinning Staff or Reiterate: arbitrary copies of the target spell (storm/magecraft payoffs or copied Crackle/Torment). Cards: Narset's Reversal, Twinning Staff, Reiterate. Enablers: Archmage Emeritus, Talrand, Sky Summoner. *fact · verified* — [anhelo-07](../interactions/anhelo-the-painter.md#anhelo-07) · `spellbook:11-2539` · `spellbook:11-3368`
- **dualcaster-twinflame** (combo): Dualcaster Mage + Twinflame: arbitrarily many hasty Dualcaster tokens. Cards: Dualcaster Mage, Twinflame. *fact · verified* — [anhelo-09](../interactions/anhelo-the-painter.md#anhelo-09) · `spellbook:147-1235`
- **reiterate-mana** (combo): Reiterate with buyback on Mana Geyser or Jeska's Will for infinite mana into a big X spell. Cards: Reiterate, Mana Geyser, Jeska's Will. Enablers: Crackle with Power, Torment of Hailfire. *fact · verified* — [anhelo-08](../interactions/anhelo-the-painter.md#anhelo-08) · `spellbook:2091-3368` · `spellbook:1878-3368`
- **copied-extra-turns** (natural): Casualty-copied Time Warp and big spells grind out a value win. Cards: Time Warp, Army of the Damned, Crackle with Power. Enablers: Anhelo, the Painter. *strategic_judgment · moderate* — [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md)

## Engines

- **casualty-copy:** Anhelo, the Painter, Archmage Emeritus, Talrand, Sky Summoner, Veyran, Voice of Duality, Storm-Kiln Artist. Online when: A creature with power 2+ to sacrifice when casting the first instant/sorcery of a turn. *fact · verified* — [anhelo-01](../interactions/anhelo-the-painter.md#anhelo-01) · [anhelo-04](../interactions/anhelo-the-painter.md#anhelo-04)
- **spell-recursion:** Kess, Dissident Mage, Maestros Ascendancy, Underworld Breach, Snapcaster Mage. Online when: Key spells in the graveyard. *fact · verified* — [anhelo-12](../interactions/anhelo-the-painter.md#anhelo-12)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:casualty-fodder` | yes | 8 | Bodies or token makers with power 2+ that are fine to sacrifice. | 10: Bloodghast, Army of the Damned, Ghoulish Procession, Jadar, Ghoulcaller of Nephalia, Poppet Stitcher // Poppet Factory, Lagomos, Hand of Hatred, Baral and Kari Zev, Startle, Judith, Carnage Connoisseur, Snapcaster Mage | — | *strategic_judgment · high* | [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md) · [Anhelo_the_Painter_99_Slot_Audit_Working_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Anhelo_the_Painter_99_Slot_Audit_Working_2026-10-13.md) |
| `pkg:copy-multipliers` | yes | 4 | Copy effects that stack with casualty. | 6: Twinning Staff, Reiterate, Narset's Reversal, Galvanic Iteration, Twinflame, Ral, Storm Conduit | — | *fact · verified* | [anhelo-06](../interactions/anhelo-the-painter.md#anhelo-06) · [anhelo-07](../interactions/anhelo-the-painter.md#anhelo-07) |
| `pkg:copy-worthy-spells` | yes | 6 | Spells that are much better copied. | 8: Demonic Tutor, Vampiric Tutor, Time Warp, Crackle with Power, Torment of Hailfire, Dig Through Time, An Offer You Can't Refuse, A Little Chat | — | *strategic_judgment · high* | [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md) |
| `pkg:interaction` | yes | 8 | Counters and removal, many cheap enough to be the 'first' spell on opponents' turns. | 10: Counterspell, Mana Drain, Fierce Guardianship, Deflecting Swat, Narset's Reversal, Chaos Warp, Deadly Rollick, Feed the Swarm, Toxic Deluge, Cyclonic Rift | — | *strategic_judgment · high* | [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md) |

## Key interactions

- **casualty-2:** First instant/sorcery each turn: optionally sacrifice a power-2+ creature to copy it. (Anhelo, the Painter) *fact · verified* — [anhelo-01](../interactions/anhelo-the-painter.md#anhelo-01)
- **first-spell-tracking:** Spells cast before Anhelo arrived still count as the turn's first. (Anhelo, the Painter) *fact · moderate* — [anhelo-02](../interactions/anhelo-the-painter.md#anhelo-02)
- **copy-vs-cast:** Copies trigger magecraft (cast or copy) but not 'whenever you cast' payoffs. (Archmage Emeritus, Storm-Kiln Artist, Talrand, Sky Summoner) *fact · verified* — [anhelo-04](../interactions/anhelo-the-painter.md#anhelo-04)
- **twinning-staff:** Twinning Staff adds one to every copy event, including casualty. (Twinning Staff) *fact · verified* — [anhelo-06](../interactions/anhelo-the-painter.md#anhelo-06)
- **double-casualty:** Granted casualty stacks with A Little Chat's own casualty. (A Little Chat) *fact · verified* — [anhelo-03](../interactions/anhelo-the-painter.md#anhelo-03)

## Tutors and recursion

- Tutor target **Narset's Reversal** via Mystical Tutor, Demonic Tutor, Vampiric Tutor *strategic_judgment · high* — [anhelo-07](../interactions/anhelo-the-painter.md#anhelo-07)
- Tutor target **Twinflame** via Mystical Tutor, Demonic Tutor *strategic_judgment · high* — [anhelo-09](../interactions/anhelo-the-painter.md#anhelo-09)
- Tutor target **Twinning Staff** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [anhelo-07](../interactions/anhelo-the-painter.md#anhelo-07)
- Recursion: Kess, Dissident Mage, Maestros Ascendancy, Underworld Breach, Snapcaster Mage, Bloodghast *fact · verified* — [anhelo-12](../interactions/anhelo-the-painter.md#anhelo-12) · [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md)

## Requirements

- **Interaction:** Cheap instant-speed interaction that doubles as the turn's casualty spell.
- **Protection:** Free counters protect combo turns; Anhelo himself is cheap to recast.
- **Mana:** Rituals, rocks and Storm-Kiln Treasures; 31 lands.
- *strategic_judgment · moderate* — [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md) · [Anhelo_the_Painter_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Anhelo_the_Painter_Approval_Ready_Closeout_2026-10-13.md)

## Failure modes

- **no-fodder:** No power-2+ creature when the important spell is cast: no copy. Mitigations: Token makers; Bloodghast recursion. *strategic_judgment · high* — [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md) · [Anhelo_the_Painter_99_Slot_Audit_Working_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Anhelo_the_Painter_99_Slot_Audit_Working_2026-10-13.md)
- **fodder-is-engine:** Sacrificing an engine creature (Talrand, Archmage) to casualty trades away the value engine. Mitigations: Prioritize token fodder. *strategic_judgment · moderate* — [anhelo-14](../interactions/anhelo-the-painter.md#anhelo-14)
- **combo-disrupted:** Graveyard hate and stack interaction stop the copy loops. Mitigations: Multiple distinct infinites; Free counters. *strategic_judgment · moderate* — [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md)

## Identity core

- **Anhelo, the Painter:** Grants casualty 2 every turn: the one effect no other card in the deck provides. *fact · verified* — `oracle:Anhelo, the Painter`
- **Twinning Staff:** Adds a copy to every casualty copy and loops Narset's Reversal. *strategic_judgment · high* — [anhelo-06](../interactions/anhelo-the-painter.md#anhelo-06)
- **Ghoulish Procession:** Steady supply of sacrificial bodies that turns the casualty cost into value. *strategic_judgment · high* — [Anhelo_the_Painter_99_Slot_Audit_Working_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Anhelo_the_Painter_99_Slot_Audit_Working_2026-10-13.md)
- **Narset's Reversal:** Cheap interaction that is also the core copy-loop piece. *strategic_judgment · high* — [anhelo-07](../interactions/anhelo-the-painter.md#anhelo-07)
- **Archmage Emeritus:** Magecraft draws on copies, so every casualty copy cantrips. *strategic_judgment · moderate* — [anhelo-04](../interactions/anhelo-the-painter.md#anhelo-04)

## Anti-goals and thematic constraints

- ✗ Don't homogenize into generic Grixis storm that ignores casualty fodder.
- ✗ Don't cut the power-2+ body count below what casualty needs.
  - *strategic_judgment · high* — [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md)
- Theme: Spell copying as artistry ('the Painter'): copies over raw storm count.
  - *strategic_judgment · low* — [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.153a:** Casualty is an additional cost paid while casting; the copy is made by a reflexive trigger. *fact · verified* — `cr:702.153a`
- **CR 707.10:** Copies are not cast: no cast triggers, but magecraft sees them. *fact · verified* — `cr:707.10`

## Supporting features (heuristic, not identity)

- `{"hooks": ["casualty / power 2 or greater", "copying", "instants and sorceries", "sacrifice"], "hooked_cards": 55, "role_counts": {"counter": 4, "draw": 6, "protection": 1, "ramp": 18, "removal": 5, "tutor": 4, "wipe": 1}, "lands": 34, "edhrec_pages": ["anhelo-the-painter"]}` *heuristic · low*

## Provenance

- Seeded from: [Anhelo_the_Painter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Anhelo_the_Painter_v1.md) · [Anhelo_the_Painter_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Anhelo_the_Painter_Approval_Ready_Closeout_2026-10-13.md) · [Anhelo_the_Painter_99_Slot_Audit_Working_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Anhelo_the_Painter_99_Slot_Audit_Working_2026-10-13.md) · [Anhelo_the_Painter_Approval_Ready_2026-10-13.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Anhelo_the_Painter_Approval_Ready_2026-10-13.txt)
- Reviewed by: — (not yet reviewed by Cory)
