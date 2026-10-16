# Blueprint — Bjorna, Nightfall Alchemist + Cecily, Haunted Mage

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/bjorna-nightfall-alchemist-cecily.md), state `SOURCE_BASELINE`, list `lh1:030933b552a9906f…`). Machine-readable source: [`data/grixis/blueprints/bjorna-nightfall-alchemist-cecily.json`](../../data/grixis/blueprints/bjorna-nightfall-alchemist-cecily.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Bjorna, Nightfall Alchemist** — Legendary Creature — Human

> {T}, Sacrifice an artifact: Bjorna, Nightfall Alchemist deals 1 damage to target creature. Goad that creature. (Until your next turn, that creature attacks each combat if able and attacks a player other than you if able.)  
> Partner—Friends forever (You can have two commanders if both have this ability.)

**Cecily, Haunted Mage** — Legendary Creature — Human Wizard

> Your maximum hand size is eleven.  
> Whenever Cecily, Haunted Mage attacks, you draw a card and you lose 1 life. Then if you have eleven or more cards in your hand, you may cast an instant or sorcery spell from your hand without paying its mana cost.  
> Partner—Friends forever (You can have two commanders if both have this ability.)

## Plan and commander role

- **Primary plan:** Big-hand spells: draw to eleven-plus cards with Rhystic Study, The One Ring, wheels and Trade Secrets/Yawgmoth's Bargain, attack with Cecily to draw and cast an instant or sorcery free, and win with draw-based combos (Peer into the Abyss + Psychosis Crawler or Teferi's Ageless Insight, Underworld Breach + Wheel of Fortune + Jeska's Will). *strategic_judgment · moderate*
- **Secondary:** Bjorna sacrifices spare artifacts (Treasures, Thopters, Clues) to ping and goad an opposing creature each turn, keeping attackers pointed away and clearing Cecily's way.
  - Evidence: [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md) · [bjorna-01](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-01-bjorna-sacrifice-an-artifact-ping-and-goad-a-creature) · [bjorna-02](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-02-cecily-draw-lose-1-then-check-eleven-cards) · [bjorna-05](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-05-peer-into-the-abyss--teferis-ageless-insight-an-odd-library-loses) · [bjorna-07](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-07-underworld-breach--wheel-of-fortune--jeskas-will)
- **Commander role: supporting.** Cecily turns attacks into a card and, with 11+ cards, a free spell; Bjorna is a small repeatable goad/ping that uses artifact tokens. Together they help, but the deck wins with draw-and-wheel combos that don't need either commander. *strategic_judgment · moderate*
- ⚠️ **Honest note:** The source blueprint misdescribes both commanders (Bjorna does not grant haste on noncreature spells; Cecily triggers on attacking, not combat damage; M1 bjorna-12). On current Oracle Bjorna is close to incidental and Cecily is a significant but combat-exposed engine. The approval dossier calls the pair the 'strategic center'; GrokBot's reading is that the draw/wheel/Peer package is.
  - Evidence: [bjorna-12](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-12-source-blueprint-misdescribes-both-commanders) · [bjorna-01](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-01-bjorna-sacrifice-an-artifact-ping-and-goad-a-creature) · [bjorna-02](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-02-cecily-draw-lose-1-then-check-eleven-cards) · [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md)
- **Dependency level:** low *strategic_judgment · moderate* — [bjorna-05](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-05-peer-into-the-abyss--teferis-ageless-insight-an-odd-library-loses) · [bjorna-07](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-07-underworld-breach--wheel-of-fortune--jeskas-will) · [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | — (none stated) (No source ceiling stated in the blueprint, approval or approval-gate dossier (checked Bot cycle 50).) | *fact · high* | [Cecily__Bjorna__Lutri_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Cecily__Bjorna__Lutri_v1.md) · [Cecily__Bjorna__Lutri_Approved_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Cecily__Bjorna__Lutri_Approved_2026-10-13.md) · [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 (project list with three banned-card exceptions): draw/wheel combo power, but the commanders add little speed; the official projection is weaker.) | *strategic_judgment · moderate* | [bjorna-05](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-05-peer-into-the-abyss--teferis-ageless-insight-an-odd-library-loses) · [bjorna-11](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-11-canonical-list-keeps-three-authorized-project-exceptions) · [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Cecily__Bjorna__Lutri` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | — (no source ceiling) | | |

- EDHREC: `{"bracket_counts": {"1": 1, "2": 8, "3": 10, "4": 4, "5": 3}, "decks_with_bracket": 26, "share_b4_plus": 0.269, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__bjorna-nightfall-alchemist-cecily-haunted-mage.json`

## Win conditions

- **peer-crawler** (combo): Peer into the Abyss on yourself with Psychosis Crawler out: each card drawn deals 1 to each opponent. Cards: Peer into the Abyss, Psychosis Crawler. Enablers: Cecily, Haunted Mage. *fact · verified* — [bjorna-06](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-06-peer-into-the-abyss--psychosis-crawler) · `spellbook:1561-2384`
- **peer-ageless-insight** (combo): Peer into the Abyss + Teferi's Ageless Insight: an odd library loses (flagged parity in M1). Cards: Peer into the Abyss, Teferi's Ageless Insight. *fact · moderate* — [bjorna-05](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-05-peer-into-the-abyss--teferis-ageless-insight-an-odd-library-loses) · `spellbook:1561-5042`
- **breach-wheel** (combo): Underworld Breach + Wheel of Fortune + Jeska's Will. Cards: Underworld Breach, Wheel of Fortune, Jeska's Will. *fact · moderate* — [bjorna-07](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-07-underworld-breach--wheel-of-fortune--jeskas-will) · `spellbook:1368-1878-2706`
- **wizard-damage** (natural): Niv-Mizzet, Parun and Psychosis Crawler punish the deck's huge draw volume. Cards: Niv-Mizzet, Parun, Psychosis Crawler. Enablers: Harmonic Prodigy. *strategic_judgment · moderate* — [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md)

## Engines

- **cecily-attack:** Cecily, Haunted Mage, Harmonic Prodigy, Robe of the Archmagi. Online when: Cecily attacks; with 11+ cards in hand after the draw, cast an instant or sorcery free. *fact · verified* — [bjorna-02](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-02-cecily-draw-lose-1-then-check-eleven-cards) · [bjorna-03](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-03-harmonic-prodigy-doubles-wizard-and-shaman-triggers) · [bjorna-04](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-04-robe-of-the-archmagi-draws-after-cecilys-trigger)
- **hand-size:** The One Ring, Rhystic Study, Mystic Remora, Trade Secrets, Yawgmoth's Bargain, Notion Thief. Online when: Draw engines running to reach eleven. *strategic_judgment · high* — [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:draw-engines` | yes | 6 | Reach and hold an eleven-card hand. | 8: The One Ring, Rhystic Study, Mystic Remora, Trade Secrets, Yawgmoth's Bargain, Archmage Emeritus, Niv-Mizzet, Parun, Robe of the Archmagi | — | *strategic_judgment · high* | [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md) |
| `pkg:wheels` | yes | 5 | Refill, fuel Peer/Breach lines, punish with Notion Thief. | 7: Wheel of Fortune, Wheel of Misfortune, Windfall, Echo of Eons, Reforge the Soul, Whispering Madness, Notion Thief | — | *strategic_judgment · high* | [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md) · [bjorna-08](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-08-wheels-with-notion-thief-and-teferis-ageless-insight) |
| `pkg:combo` | yes | 3 | Draw-based kills. | 5: Peer into the Abyss, Psychosis Crawler, Teferi's Ageless Insight, Underworld Breach, Jeska's Will | — | *fact · verified* | [bjorna-05](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-05-peer-into-the-abyss--teferis-ageless-insight-an-odd-library-loses) · [bjorna-06](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-06-peer-into-the-abyss--psychosis-crawler) · [bjorna-07](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-07-underworld-breach--wheel-of-fortune--jeskas-will) |
| `pkg:artifact-fodder` | optional | 4 | Artifacts and tokens for Bjorna to sacrifice. | 6: Big Score, Deadly Dispute, Sai, Master Thopterist, Ichor Wellspring, Academy Manufactor, Brass's Bounty | — | *strategic_judgment · moderate* | [bjorna-01](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-01-bjorna-sacrifice-an-artifact-ping-and-goad-a-creature) |

## Key interactions

- **bjorna-goad:** {T}, sacrifice an artifact: 1 damage to a creature and goad it. (Bjorna, Nightfall Alchemist) *fact · verified* — [bjorna-01](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-01-bjorna-sacrifice-an-artifact-ping-and-goad-a-creature)
- **cecily-order:** Draw and lose 1 first, then check eleven cards; free cast from hand. (Cecily, Haunted Mage) *fact · verified* — [bjorna-02](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-02-cecily-draw-lose-1-then-check-eleven-cards)
- **prodigy-doubles:** Harmonic Prodigy doubles Cecily, Niv-Mizzet and Archmage triggers. (Harmonic Prodigy) *fact · verified* — [bjorna-03](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-03-harmonic-prodigy-doubles-wizard-and-shaman-triggers)
- **triskaidekaphile:** Triskaidekaphile wins with exactly thirteen cards at upkeep. (Triskaidekaphile) *fact · verified* — [bjorna-09](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-09-triskaidekaphile-needs-exactly-thirteen-at-upkeep)
- **exceptions:** Lutri companion, Trade Secrets and Yawgmoth's Bargain are project exceptions, not Commander-legal. (Trade Secrets, Yawgmoth's Bargain, Lutri, the Spellchaser) *fact · verified* — [bjorna-11](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-11-canonical-list-keeps-three-authorized-project-exceptions)

## Tutors and recursion

- Tutor target **Peer into the Abyss** via Demonic Tutor, Vampiric Tutor, Mystical Tutor *strategic_judgment · high* — [bjorna-06](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-06-peer-into-the-abyss--psychosis-crawler)
- Tutor target **Psychosis Crawler** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [bjorna-06](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-06-peer-into-the-abyss--psychosis-crawler)
- Recursion: Underworld Breach, Kess, Dissident Mage, Emry, Lurker of the Loch, Goblin Engineer *strategic_judgment · moderate* — [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md)

## Requirements

- **Interaction:** Counters to protect combo turns; Toxic Deluge and Cyclonic Rift as resets.
- **Protection:** Lightning Greaves for Cecily's attack; Fierce Guardianship.
- **Mana:** Rituals (Seething Song, Mana Geyser, Jeska's Will) and rocks.
- *strategic_judgment · moderate* — [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md)

## Failure modes

- **cecily-cant-attack:** Cecily dies in combat or can't attack safely; free casts never happen. Mitigations: Bjorna goads blockers; Greaves. *strategic_judgment · high* — [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md)
- **wheel-shrinks-hand:** Wheels replace the hand and can drop below eleven. Mitigations: Sequence wheels before draw engines. *strategic_judgment · moderate* — [bjorna-08](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-08-wheels-with-notion-thief-and-teferis-ageless-insight)
- **legality:** Outside the project the list is not Commander-legal (three exceptions); the official projection swaps them out and loses power. Mitigations: Projection is labeled and never canonical. *strategic_judgment · high* — [bjorna-11](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-11-canonical-list-keeps-three-authorized-project-exceptions)

## Identity core

- **Cecily, Haunted Mage:** Attack draw and free spell at eleven cards: the pair's real engine. *fact · verified* — `oracle:Cecily, Haunted Mage`
- **Bjorna, Nightfall Alchemist:** Required commander; goads one blocker or attacker per turn using spare artifacts. *fact · verified* — `oracle:Bjorna, Nightfall Alchemist`
- **Peer into the Abyss:** Central combo piece and the biggest single hand-size swing. *strategic_judgment · high* — [bjorna-06](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-06-peer-into-the-abyss--psychosis-crawler)
- **The One Ring:** Protection plus escalating draw toward eleven. *strategic_judgment · high* — [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md)
- **Trade Secrets:** Project-authorized exception that fuels the hand-size plan. *approved_decision · verified* — [bjorna-11](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-11-canonical-list-keeps-three-authorized-project-exceptions) · [Cecily__Bjorna__Lutri_Approved_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Cecily__Bjorna__Lutri_Approved_2026-10-13.md)

## Anti-goals and thematic constraints

- ✗ Don't homogenize into generic Grixis storm (source guardrail).
- ✗ Don't claim the three exception cards are Commander-legal.
- ✗ Don't build around the misdescribed source text for Bjorna/Cecily.
  - *strategic_judgment · high* — [Cecily__Bjorna__Lutri_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Cecily__Bjorna__Lutri_v1.md) · [bjorna-12](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-12-source-blueprint-misdescribes-both-commanders)
- Theme: Friends forever pair; Lutri companion is a project exception kept from the source.
  - *approved_decision · verified* — [Cecily__Bjorna__Lutri_Approved_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Cecily__Bjorna__Lutri_Approved_2026-10-13.md)

## Project exceptions

Lutri, the Spellchaser, Trade Secrets, Yawgmoth's Bargain (🚩 NOT Commander-legal; registry `data/grixis/exceptions.json`)

## Construction-relevant rules

- **CR 702.124i:** Partner—Friends forever: both commanders' identities combine; each has its own tax. *fact · verified* — `cr:702.124i`
- **CR 702.139:** Companion rules; Lutri is banned as a companion in Commander and kept only as a project exception. *fact · verified* — `cr:702.139`

## Supporting features (heuristic, not identity)

- `{"hooks": ["artifacts", "card draw / hand size", "combat damage / attack triggers", "goad / forced attacks", "instants and sorceries", "sacrifice"], "hooked_cards": 64, "role_counts": {"counter": 2, "draw": 27, "protection": 1, "ramp": 18, "removal": 4, "tutor": 4, "wipe": 2}, "lands": 33, "edhrec_pages": ["bjorna-nightfall-alchemist-cecily-haunted-mage"]}` *heuristic · low*

## Provenance

- Seeded from: [Cecily__Bjorna__Lutri_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Cecily__Bjorna__Lutri_v1.md) · [Cecily__Bjorna__Lutri_Approved_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Cecily__Bjorna__Lutri_Approved_2026-10-13.md) · [Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md) · [Cecily__Bjorna__Lutri_Approved_2026-10-13.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Cecily__Bjorna__Lutri_Approved_2026-10-13.txt) · [bjorna-12](../interactions/bjorna-nightfall-alchemist-cecily.md#bjorna-12-source-blueprint-misdescribes-both-commanders)
- Reviewed by: — (not yet reviewed by Cory)
