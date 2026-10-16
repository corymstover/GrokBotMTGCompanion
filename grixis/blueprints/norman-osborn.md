# Blueprint — Norman Osborn // Green Goblin

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/norman-osborn.md), state `SOURCE_BASELINE`, list `lh1:9f7364522bbd7604…`). Machine-readable source: [`data/grixis/blueprints/norman-osborn.json`](../../data/grixis/blueprints/norman-osborn.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Norman Osborn // Green Goblin** — Legendary Creature — Human Scientist Villain // Legendary Creature — Goblin Human Villain

> Norman Osborn can't be blocked.  
> Whenever Norman Osborn deals combat damage to a player, he connives. (Draw a card, then discard a card. If you discarded a nonland card, put a +1/+1 counter on this creature.)  
> {1}{U}{B}{R}: Transform Norman Osborn. Activate only as a sorcery.  
> Flying, menace  
> Spells you cast from your graveyard cost {2} less to cast.  
> Goblin Formula — Each nonland card in your graveyard has mayhem. The mayhem cost is equal to its mana cost. (You may cast a card from your graveyard for its mayhem cost if you discarded it this turn. Timing rules still apply.)

## Plan and commander role

- **Primary plan:** Turbo combo: fast mana and tutors race to Thassa's Oracle + Demonic Consultation/Tainted Pact or Underworld Breach lines (LED + Brain Freeze, Wheel of Fortune + Jeska's Will, Grinding Station + Mox Amber). *strategic_judgment · high*
- **Secondary:** Commander-native mayhem: Norman connives unblockably, then Green Goblin makes every nonland card discarded this turn castable from the graveyard for {2} less, turning loot and discard outlets into card advantage.
  - Evidence: [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)
- **Commander role: significant.** Green Goblin's mayhem and cost reduction turn the loot/discard package into virtual card advantage. Norman is a blue legendary that turns on Mox Amber. *strategic_judgment · high*
- ⚠️ **Honest note:** All 7 Spellbook combos in the list are commander-free generic cEDH kills (Oracle, Breach). The source keeps them because the ceiling is genuinely cEDH and says they're not the deck's sole identity (verification L179). The mayhem engine needs a four-mana sorcery-speed transform. Good card selection, but the deck mostly wins without him. Registry quirk: this deck's registry id is the stale tracker id Goben__Gene_Splice_Savant, so the source files (Norman_Osborn_Green_Goblin_*) were cited by hand. No M1 interaction review exists yet for this deck.
  - Evidence: [Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md#L179](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L39](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)
- **Dependency level:** low *strategic_judgment · high* — [Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md#L179](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (Power Bracket 5 — cEDH (blueprint).) | *fact · verified* | [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L9](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 5 (Bracket 5 ceiling: tournament-backed turbo shell with Oracle and Breach lines. Agrees with the source.) | *strategic_judgment · high* | [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Goben__Gene_Splice_Savant` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 58, "2": 857, "3": 1622, "4": 681, "5": 788}, "decks_with_bracket": 4006, "share_b4_plus": 0.367, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__norman-osborn.json`

## Win conditions

- **oracle** (combo): Thassa's Oracle + Demonic Consultation or Tainted Pact. Cards: Thassa's Oracle, Demonic Consultation, Tainted Pact. *fact · verified* — `spellbook:1295-3093` · `spellbook:742-1295`
- **breach** (combo): Underworld Breach + LED/Lotus Petal + Brain Freeze, or + Wheel of Fortune (+ LED or Jeska's Will). Cards: Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze, Wheel of Fortune, Jeska's Will. *fact · verified* — `spellbook:1368-1414-4856` · `spellbook:1368-3518-4856` · `spellbook:1368-2706-3518` · `spellbook:1368-1878-2706`
- **breach-station** (combo): Underworld Breach + Grinding Station + Mox Amber: self-mill, storm and mana. With Norman out, Mox Amber makes blue. Cards: Underworld Breach, Grinding Station, Mox Amber. Enablers: Norman Osborn // Green Goblin, Brain Freeze, Thassa's Oracle. *fact · verified* — `spellbook:1368-3698--44` · [Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md#L193](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md#L195](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md)

## Engines

- **mayhem:** Norman Osborn // Green Goblin, Careful Study, Faithless Looting, Frantic Search, Psychic Frog, Shadow of the Goblin, Unstable Experiment, Big Score, Dark Deal. Online when: Green Goblin transformed ({1}{U}{B}{R}, sorcery speed) and a discard outlet. *fact · high* — `oracle:Norman Osborn // Green Goblin` · [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)
- **fast-mana:** Mana Vault, Grim Monolith, Chrome Mox, Mox Diamond, Mox Opal, Mox Amber, Lotus Petal, Dark Ritual, Cabal Ritual, Rite of Flame, Simian Spirit Guide, City of Traitors, Gemstone Caverns, Ancient Tomb. Online when: Opening hand. *strategic_judgment · high* — [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:discard-into-mayhem` | yes | 10 | Discard outlets that feed mayhem. | 15: Careful Study, Faithless Looting, Frantic Search, Psychic Frog, Shadow of the Goblin, Unstable Experiment, Big Score, Dark Deal, Attunement, Breakthrough, Ghostly Pilferer, Tolarian Winds, Artist's Talent, Gamble, Reckless Handling | — | *strategic_judgment · high* | [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md) |
| `pkg:timing` | optional | 2 | Flash timing for mayhem-cast noncreature spells. | 2: Borne Upon a Wind, Valley Floodcaller | — | *strategic_judgment · high* | [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md) |
| `pkg:tutors` | yes | 8 | Find the compact wins. | 10: Demonic Tutor, Vampiric Tutor, Imperial Seal, Mystical Tutor, Beseech the Mirror, Wishclaw Talisman, Reckless Handling, Gamble, Demonic Consultation, Tainted Pact | — | *strategic_judgment · high* | [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md) |
| `pkg:stack` | yes | 8 | cEDH stack interaction. | 13: Force of Will, Pact of Negation, Fierce Guardianship, Flusterstorm, Mental Misstep, Mindbreak Trap, Swan Song, Pyroblast, Red Elemental Blast, Deflecting Swat, Into the Flood Maw, Chain of Vapor, Defense Grid | — | *strategic_judgment · high* | [Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) |

## Key interactions

- **generic-only-reduction:** Green Goblin's {2} reduction only reduces generic mana. (Norman Osborn // Green Goblin) *fact · high* — `oracle:Norman Osborn // Green Goblin` · [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)
- **mayhem-timing:** Mayhem needs the card discarded this turn and follows normal timing rules; Borne Upon a Wind/Valley Floodcaller add flash. (Norman Osborn // Green Goblin, Borne Upon a Wind, Valley Floodcaller) *fact · high* — `oracle:Norman Osborn // Green Goblin` · [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)
- **no-necropotence:** Necropotence exiles discarded cards, which conflicts with mayhem, so it's deliberately excluded. (Norman Osborn // Green Goblin) *fact · high* — [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)
- **mox-amber-norman:** Norman is a blue legendary creature, so Mox Amber makes blue mana. (Mox Amber, Norman Osborn // Green Goblin) *fact · high* — [Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md#L195](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md)
- **connive:** Connive: draw, discard; a nonland discard adds a +1/+1 counter. (Norman Osborn // Green Goblin) *fact · high* — `cr:701.50a`

## Tutors and recursion

- Tutor target **Thassa's Oracle** via Demonic Tutor, Vampiric Tutor, Imperial Seal, Mystical Tutor *strategic_judgment · high* — `spellbook:1295-3093`
- Tutor target **Lion's Eye Diamond** via Beseech the Mirror, Wishclaw Talisman, Reckless Handling *strategic_judgment · high* — `spellbook:1368-3518-4856`
- Recursion: Norman Osborn // Green Goblin, Underworld Breach, Yawgmoth's Will, Jeska's Will *strategic_judgment · high* — [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)

## Requirements

- **Interaction:** Full cEDH free-counter suite.
- **Protection:** Fierce Guardianship, Deflecting Swat, Defense Grid, Cavern of Souls.
- **Mana:** 23 lands plus a dense fast-mana package.
- *strategic_judgment · high* — [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md#L239](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md)

## Failure modes

- **graveyard-hate:** Graveyard hate stops Breach and mayhem. Mitigations: Oracle lines. *strategic_judgment · high* — [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)
- **slow-transform:** Green Goblin needs a four-mana sorcery-speed transform. Mitigations: Generic combo without him. *strategic_judgment · moderate* — [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L38](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)
- **23-lands:** A 23-land turbo build can stumble without fast mana. Mitigations: Loot density. *strategic_judgment · moderate* — [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)

## Identity core

- **Norman Osborn // Green Goblin:** Unblockable connive, then mayhem and cost reduction. *fact · verified* — `oracle:Norman Osborn // Green Goblin`
- **Faithless Looting:** Cheap discard into mayhem. *strategic_judgment · high* — [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)
- **Borne Upon a Wind:** Flash for mayhem casts. *strategic_judgment · high* — [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)
- **Grinding Station:** Breach engine piece. *strategic_judgment · high* — [Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md#L193](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md)
- **Thassa's Oracle:** Compact win. *strategic_judgment · high* — `spellbook:1295-3093`

## Anti-goals and thematic constraints

- ✗ No Necropotence (blueprint L36).
- ✗ Don't cut commander-native discard engines for generic staples (L37).
- ✗ No five-mana discard payoffs or combat-only value (L38).
  - *strategic_judgment · high* — [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L38](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)
- Theme: Mayhem / graveyard casting / turbo combo (blueprint L11).
  - *strategic_judgment · high* — [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.50a:** Connive. *fact · verified* — `cr:701.50a`
- **CR 601.2f:** Cost reductions reduce generic mana. *fact · verified* — `cr:601.2f`
- **CR 702.187a:** Mayhem. *fact · verified* — `cr:702.187a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["+1/+1 counters", "combat damage / attack triggers", "connive / looting", "discard", "graveyard as a resource"], "hooked_cards": 24, "role_counts": {"counter": 8, "draw": 21, "protection": 1, "ramp": 22, "removal": 5, "tutor": 9, "wipe": 1}, "lands": 23, "edhrec_pages": ["norman-osborn"]}` *heuristic · low*

## Provenance

- Seeded from: [Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Norman_Osborn_Green_Goblin_Candidate_Decisions_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Norman_Osborn_Green_Goblin_Approved_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Approval_Ready_Verification_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Norman_Osborn_Green_Goblin_Whole_List_Audit_2026-10-15.md) · [Norman_Osborn_Green_Goblin_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Norman_Osborn_Green_Goblin_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
