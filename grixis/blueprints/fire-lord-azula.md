# Blueprint — Fire Lord Azula

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/fire-lord-azula.md), state `SOURCE_BASELINE`, list `lh1:5647c4e9260c54e4…`). Machine-readable source: [`data/grixis/blueprints/fire-lord-azula.json`](../../data/grixis/blueprints/fire-lord-azula.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Fire Lord Azula** — Legendary Creature — Human Noble

> Firebending 2 (Whenever this creature attacks, add {R}{R}. This mana lasts until end of combat.)  
> Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell. You may choose new targets for the copy. (A copy of a permanent spell becomes a token.)

## Plan and commander role

- **Primary plan:** cEDH spell-copy: land Azula fast, attack, and cast rituals, untaps, draw and combo pieces while she's attacking so each resolves twice; win with Azula + Narset's Reversal/Underworld Breach + Frantic Search, Breach + LED/Petal + Brain Freeze, or Thassa's Oracle. *strategic_judgment · high*
- **Secondary:** Generic Grixis cEDH shell (fast mana, free counters, tutors, Necropotence/Ad Nauseam) wins without Azula when she can't attack.
  - Evidence: [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md) · [azula-05](../interactions/fire-lord-azula.md#azula-05-azula--narsets-reversal--frantic-search) · [azula-06](../interactions/fire-lord-azula.md#azula-06-azula--underworld-breach--frantic-search)
- **Commander role: significant.** Copies every spell cast while she attacks; two of the deck's infinites need her. *strategic_judgment · high*
- ⚠️ **Honest note:** Her copy only works during combat on an attack, so sorceries need flash enablers and she has to survive to attack. The Breach and Oracle lines (M1 azula-07, azula-08) win without her, and the list is built like a generic Grixis cEDH deck around her.
  - Evidence: [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md) · [azula-02](../interactions/fire-lord-azula.md#azula-02-while-attacking-means-during-combat-sorceries-need-a-flash-enabler) · [azula-07](../interactions/fire-lord-azula.md#azula-07-breach-lines-without-azula)
- **Dependency level:** medium *strategic_judgment · high* — [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md) · [azula-07](../interactions/fire-lord-azula.md#azula-07-breach-lines-without-azula)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (Power Bracket 5 — cEDH (decisions header).) | *fact · verified* | [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 5 (Bracket 5 ceiling: full cEDH shell with commander-dependent and commander-free infinites, backed by current tournament results per the source. Agrees with the source.) | *strategic_judgment · high* | [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md) · `spellbook:11-2196-7089` |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Fire_Lord_Azula` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 72, "2": 1265, "3": 3519, "4": 2030, "5": 562}, "decks_with_bracket": 7448, "share_b4_plus": 0.348, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__fire-lord-azula.json`

## Win conditions

- **azula-frantic** (combo): Attacking Azula copies Frantic Search alongside Narset's Reversal or Underworld Breach for unbounded untaps, draw and storm. Cards: Fire Lord Azula, Frantic Search, Narset's Reversal, Underworld Breach. Enablers: Arena of Glory, Borne Upon a Wind. *fact · verified* — `spellbook:11-2196-7089` · `spellbook:1368-2196-7089` · [azula-05](../interactions/fire-lord-azula.md#azula-05-azula--narsets-reversal--frantic-search) · [azula-06](../interactions/fire-lord-azula.md#azula-06-azula--underworld-breach--frantic-search)
- **breach** (combo): Underworld Breach with LED/Petal + Brain Freeze, Wheel of Fortune + Jeska's Will/LED, or Grinding Station. Cards: Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze, Wheel of Fortune, Jeska's Will, Grinding Station. *fact · verified* — `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856` · `spellbook:1368-1878-2706` · `spellbook:1368-2706-3518` · `spellbook:1368-3698--44` · [azula-07](../interactions/fire-lord-azula.md#azula-07-breach-lines-without-azula)
- **oracle** (combo): Thassa's Oracle with Demonic Consultation or Tainted Pact. Cards: Thassa's Oracle, Demonic Consultation, Tainted Pact. *fact · verified* — `spellbook:742-1295` · `spellbook:1295-3093` · [azula-08](../interactions/fire-lord-azula.md#azula-08-thassas-oracle--consultation--tainted-pact)

## Engines

- **attack-copy:** Fire Lord Azula, Big Score, Dark Ritual, Cabal Ritual, Snap, Frantic Search, Beseech the Mirror. Online when: Azula attacking. *fact · verified* — [azula-01](../interactions/fire-lord-azula.md#azula-01-the-copy-resolves-first-even-if-the-original-is-countered) · [azula-03](../interactions/fire-lord-azula.md#azula-03-additional-costs-are-paid-once-but-the-copy-counts-them-as-paid)
- **combat-timing:** Borne Upon a Wind, Quicken, Emergence Zone, Valley Floodcaller, Arena of Glory, Expedite. Online when: Flash or haste enabler available. *fact · verified* — [azula-02](../interactions/fire-lord-azula.md#azula-02-while-attacking-means-during-combat-sorceries-need-a-flash-enabler) · [azula-09](../interactions/fire-lord-azula.md#azula-09-arena-of-glory-gives-azula-haste)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:combat-timing` | yes | 5 | Move sorceries into combat and give Azula haste. | 7: Borne Upon a Wind, Quicken, Emergence Zone, Valley Floodcaller, Arena of Glory, Expedite, Birgi, God of Storytelling // Harnfel, Horn of Bounty | — | *strategic_judgment · high* | [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md) · [azula-02](../interactions/fire-lord-azula.md#azula-02-while-attacking-means-during-combat-sorceries-need-a-flash-enabler) |
| `pkg:free-interaction` | yes | 8 | Protect the combat turn. | 12: Force of Will, Force of Negation, Pact of Negation, Fierce Guardianship, Mental Misstep, Mindbreak Trap, Flusterstorm, Swan Song, Pyroblast, Red Elemental Blast, Deflecting Swat, An Offer You Can't Refuse | — | *strategic_judgment · high* | [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:copy-payoffs` | yes | 5 | Spells that double well under Azula. | 8: Big Score, Frantic Search, Snap, Dark Ritual, Cabal Ritual, Beseech the Mirror, Demand Answers, Redirect Lightning | — | *strategic_judgment · high* | [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md) |

## Key interactions

- **copy-first:** The copy resolves first and isn't cast: no storm, no cast triggers. (Fire Lord Azula) *fact · verified* — [azula-01](../interactions/fire-lord-azula.md#azula-01-the-copy-resolves-first-even-if-the-original-is-countered)
- **while-attacking:** Copies happen only during combat, so sorceries need flash enablers. (Fire Lord Azula, Borne Upon a Wind) *fact · verified* — [azula-02](../interactions/fire-lord-azula.md#azula-02-while-attacking-means-during-combat-sorceries-need-a-flash-enabler)
- **additional-costs:** Additional costs are paid once but count for the copy (Big Score: 4 cards + 4 Treasures). (Big Score) *fact · verified* — [azula-03](../interactions/fire-lord-azula.md#azula-03-additional-costs-are-paid-once-but-the-copy-counts-them-as-paid)
- **bargain-copy:** A bargained Beseech the Mirror copy is bargained too. (Beseech the Mirror) *fact · verified* — [azula-04](../interactions/fire-lord-azula.md#azula-04-a-bargained-beseech-the-mirror-copy-is-bargained-too)
- **permanent-copies:** Copied permanent spells become tokens without being 'created'. (Fire Lord Azula) *fact · verified* — [azula-10](../interactions/fire-lord-azula.md#azula-10-copied-permanent-spells-become-tokens-but-arent-created)

## Tutors and recursion

- Tutor target **Underworld Breach** via Demonic Tutor, Gamble, Imperial Seal *strategic_judgment · high* — `spellbook:1368-3518-4856`
- Tutor target **Thassa's Oracle** via Vampiric Tutor, Mystical Tutor, Wishclaw Talisman *strategic_judgment · high* — `spellbook:742-1295`
- Tutor target **Narset's Reversal** via Mystical Tutor *strategic_judgment · moderate* — `spellbook:11-2196-7089`
- Recursion: Underworld Breach, Jeska's Will *strategic_judgment · moderate* — [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Dense free counters and one-mana interaction.
- **Protection:** Deflecting Swat, Fierce Guardianship, Cavern of Souls.
- **Mana:** Fast mana and rituals; Azula must be cast and attack quickly.
- *strategic_judgment · high* — [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **no-combat:** Azula removed or unable to attack: no copies. Mitigations: Commander-free Breach/Oracle lines; Haste from Arena of Glory. *strategic_judgment · high* — [azula-02](../interactions/fire-lord-azula.md#azula-02-while-attacking-means-during-combat-sorceries-need-a-flash-enabler)
- **graveyard-hate:** Graveyard hate stops Breach. Mitigations: Thassa's Oracle + Consultation. *strategic_judgment · high* — [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md)
- **metalcraft:** Low artifact density can leave Mox Opal dead. Mitigations: Accepted by the source as a flex risk. *strategic_judgment · moderate* — [azula-11](../interactions/fire-lord-azula.md#azula-11-mox-opal-metalcraft-density)

## Identity core

- **Fire Lord Azula:** Copies each spell cast while she attacks. *fact · verified* — `oracle:Fire Lord Azula`
- **Narset's Reversal:** With Frantic Search under Azula, an infinite loop. *strategic_judgment · high* — [azula-05](../interactions/fire-lord-azula.md#azula-05-azula--narsets-reversal--frantic-search)
- **Frantic Search:** Free untap-draw spell that loops under Azula. *strategic_judgment · high* — [azula-05](../interactions/fire-lord-azula.md#azula-05-azula--narsets-reversal--frantic-search)
- **Borne Upon a Wind:** Flash so sorceries can be copied in combat. *strategic_judgment · high* — [azula-02](../interactions/fire-lord-azula.md#azula-02-while-attacking-means-during-combat-sorceries-need-a-flash-enabler)
- **Big Score:** One discard, double Treasure and cards. *strategic_judgment · moderate* — [azula-03](../interactions/fire-lord-azula.md#azula-03-additional-costs-are-paid-once-but-the-copy-counts-them-as-paid)

## Anti-goals and thematic constraints

- ✗ Thematic Fire Nation cards that lose to cEDH efficiency stay out (e.g. Fire Nation Palace, Fists of Flame; decisions L48, L51).
- ✗ Slow setup engines (Archmage Emeritus, Veyran) are cut.
  - *strategic_judgment · high* — [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Theme subordinate to cEDH; Avatar flavour comes mainly from the commander.
  - *strategic_judgment · moderate* — [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 707.10:** Copies of spells aren't cast. *fact · verified* — `cr:707.10`
- **CR 506.1:** The combat phase and its steps: Azula copies only during combat. *fact · verified* — `cr:506.1`

## Supporting features (heuristic, not identity)

- `{"hooks": ["combat damage / attack triggers", "copying"], "hooked_cards": 7, "role_counts": {"counter": 11, "draw": 14, "protection": 2, "ramp": 21, "removal": 7, "tutor": 7, "wipe": 1}, "lands": 26, "edhrec_pages": ["fire-lord-azula"]}` *heuristic · low*

## Provenance

- Seeded from: [Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Fire_Lord_Azula_Current_Cycle_Decisions_2026-10-14.md) · [Fire_Lord_Azula_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Fire_Lord_Azula_Approved_2026-10-14.md) · [Fire_Lord_Azula_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Fire_Lord_Azula_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
