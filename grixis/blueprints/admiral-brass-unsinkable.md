# Blueprint — Admiral Brass, Unsinkable

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/admiral-brass-unsinkable.md), state `SOURCE_BASELINE`, list `lh1:3ff7f503d029554c…`). Machine-readable source: [`data/grixis/blueprints/admiral-brass-unsinkable.json`](../../data/grixis/blueprints/admiral-brass-unsinkable.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Admiral Brass, Unsinkable** — Legendary Creature — Human Pirate

> When Admiral Brass enters, mill four cards.  
> At the beginning of combat on your turn, you may return target Pirate creature card from your graveyard to the battlefield with a finality counter on it. It has base power and toughness 4/4. It gains haste until end of turn. (If a creature with a finality counter on it would die, exile it instead.)

## Plan and commander role

- **Primary plan:** Pirate reanimator: fill the graveyard with high-impact Pirates (ETB mill, Entomb, Buried Alive, looting), return one each beginning of combat as a hasty 4/4 with a finality counter, and attack with ETB/attack value. *strategic_judgment · high*
- **Secondary:** Tribal mass reanimation (Living Death, Patriarch's Bidding, Victimize) as recovery and finish; finality-counter removal (Power Conduit) to make reanimation repeatable.
  - Evidence: [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md) · [brass-01](../interactions/admiral-brass-unsinkable.md#brass-01-the-combat-reanimation-pirate-creature-card-finality-counter-base-44-haste) · [brass-15](../interactions/admiral-brass-unsinkable.md#brass-15-what-the-list-depends-on)
- **Commander role: central.** Brass's combat trigger is a free Pirate reanimation every turn; the self-mill and Pirate-ETB choices exist for it. *strategic_judgment · high*
- ⚠️ **Honest note:** Finality counters exile the returned Pirate when it would die, so each card is usually a one-shot unless Power Conduit removes the counter; the engine slowly consumes the graveyard.
  - Evidence: [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md) · [brass-01](../interactions/admiral-brass-unsinkable.md#brass-01-the-combat-reanimation-pirate-creature-card-finality-counter-base-44-haste) · [brass-02](../interactions/admiral-brass-unsinkable.md#brass-02-finality-counters-mean-exile-not-death) · [brass-03](../interactions/admiral-brass-unsinkable.md#brass-03-power-conduit-removes-the-finality-counter)
- **Dependency level:** high *strategic_judgment · high* — [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md) · [brass-15](../interactions/admiral-brass-unsinkable.md#brass-15-what-the-list-depends-on)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | — (none stated) (No source ceiling stated in the source blueprint or its evidence (checked Bot cycle 50).) | *fact · high* | [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 by card pool (Entomb/Reanimate, premium tutors and free counters), fair combat engine without a compact win; low-to-mid B4.) | *strategic_judgment · moderate* | [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md) · [brass-15](../interactions/admiral-brass-unsinkable.md#brass-15-what-the-list-depends-on) · [deck page](../decks/admiral-brass-unsinkable.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Admiral_Brass__Unsinkable` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | — (no source ceiling) | | |

- EDHREC: `{"bracket_counts": {"1": 26, "2": 1049, "3": 772, "4": 174, "5": 7}, "decks_with_bracket": 2028, "share_b4_plus": 0.089, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__admiral-brass-unsinkable.json`

## Win conditions

- **reanimated-pirate-beats** (natural): A new hasty 4/4 Pirate with ETB value every combat, pumped by Shared Animosity and lords, plus Port Razer combats. Cards: Admiral Brass, Unsinkable, Shared Animosity, Port Razer, Angrath's Marauders. Enablers: Entomb, Buried Alive. *strategic_judgment · high* — [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md)
- **mass-reanimation** (natural): Living Death or Patriarch's Bidding returns a whole Pirate board for a lethal swing. Cards: Living Death, Patriarch's Bidding. Enablers: Faithless Looting. *fact · moderate* — [brass-10](../interactions/admiral-brass-unsinkable.md#brass-10-mass-reanimation-patriarchs-bidding-and-living-death-are-symmetric) · [brass-12](../interactions/admiral-brass-unsinkable.md#brass-12-angraths-marauders-doubles-all-your-damage)

## Engines

- **combat-reanimation:** Admiral Brass, Unsinkable, Roaming Throne. Online when: A Pirate creature card in your graveyard at your beginning of combat. *fact · verified* — [brass-01](../interactions/admiral-brass-unsinkable.md#brass-01-the-combat-reanimation-pirate-creature-card-finality-counter-base-44-haste)
- **pirate-etb-value:** Skeleton Crew, Gemcutter Buccaneer, Coercive Recruiter, Hostage Taker, Zara, Renegade Recruiter. Online when: Pirates entering (reanimated or cast). *fact · verified* — [brass-07](../interactions/admiral-brass-unsinkable.md#brass-07-skeleton-crew-triggers-on-every-reanimation-and-encore) · [brass-13](../interactions/admiral-brass-unsinkable.md#brass-13-gemcutter-buccaneer-turns-treasures-into-pirate-equipment)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:graveyard-setup` | yes | 4 | Put the right Pirate in the graveyard before combat. | 4: Entomb, Buried Alive, Faithless Looting, Brass's Tunnel-Grinder // Tecutlan, the Searing Rift | — | *strategic_judgment · high* | [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md) |
| `pkg:reanimation` | yes | 4 | Backup and mass reanimation beyond the commander. | 5: Animate Dead, Reanimate, Victimize, Living Death, Patriarch's Bidding | Back in Town | *strategic_judgment · high* | [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md) |
| `pkg:high-impact-pirates` | yes | 8 | Pirates worth reanimating for ETB/attack value. | 10: Amphin Mutineer, Angrath's Marauders, Broadside Bombardiers, Coercive Recruiter, Hostage Taker, Port Razer, Zara, Renegade Recruiter, Mary Read and Anne Bonny, Pitiless Plunderer, Gemcutter Buccaneer | Warkite Marauder, Kitesail Larcenist | *strategic_judgment · high* | [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md) |
| `pkg:finality-removal` | optional | 1 | Remove finality counters so reanimated Pirates can die normally and return again. | 1: Power Conduit | Soul Diviner | *fact · verified* | [brass-03](../interactions/admiral-brass-unsinkable.md#brass-03-power-conduit-removes-the-finality-counter) |
| `pkg:interaction-protection` | yes | 8 | Stack and board interaction plus commander protection. | 11: Counterspell, Mana Drain, Fierce Guardianship, Deflecting Swat, Siren Stormtamer, Lightning Greaves, Chaos Warp, Toxic Deluge, Cyclonic Rift, Deadly Rollick, Feed the Swarm | — | *strategic_judgment · high* | [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md) |

## Key interactions

- **combat-trigger:** Beginning of combat: return a Pirate creature card with a finality counter; base 4/4, haste. (Admiral Brass, Unsinkable) *fact · verified* — [brass-01](../interactions/admiral-brass-unsinkable.md#brass-01-the-combat-reanimation-pirate-creature-card-finality-counter-base-44-haste)
- **finality-exile:** Finality creatures are exiled instead of dying: no death triggers or Plunderer Treasure. (Pitiless Plunderer) *fact · verified* — [brass-02](../interactions/admiral-brass-unsinkable.md#brass-02-finality-counters-mean-exile-not-death)
- **power-conduit:** Power Conduit removes the finality counter; the base 4/4 stays. (Power Conduit) *fact · verified* — [brass-03](../interactions/admiral-brass-unsinkable.md#brass-03-power-conduit-removes-the-finality-counter)
- **changeling-and-wonder:** Changeling cards are Pirate creature cards in the graveyard; Wonder in the graveyard gives flying. (Changeling Outcast, Wonder) *fact · verified* — [brass-05](../interactions/admiral-brass-unsinkable.md#brass-05-changeling-cards-are-pirate-creature-cards-in-the-graveyard) · [brass-09](../interactions/admiral-brass-unsinkable.md#brass-09-wonder-in-the-graveyard-gives-your-team-flying)
- **symmetric-mass-reanimation:** Living Death and Patriarch's Bidding are symmetric; check opponents' graveyards first. (Living Death, Patriarch's Bidding) *fact · moderate* — [brass-10](../interactions/admiral-brass-unsinkable.md#brass-10-mass-reanimation-patriarchs-bidding-and-living-death-are-symmetric)

## Tutors and recursion

- Tutor target **Port Razer** via Entomb, Buried Alive *strategic_judgment · high* — [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md)
- Tutor target **Living Death** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md)
- Recursion: Animate Dead, Reanimate, Victimize, Living Death, Patriarch's Bidding *fact · verified* — [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md)

## Requirements

- **Interaction:** Graveyard hate is the main threat; keep stack interaction to protect the reanimation turn.
- **Protection:** Greaves, Stormtamer and free protection for the commander.
- **Mana:** Four-mana commander; 34 lands plus rocks.
- *strategic_judgment · moderate* — [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md)

## Failure modes

- **graveyard-hate:** Graveyard exile (Bojuka Bog, Rest in Peace) shuts off the commander and mass reanimation. Mitigations: Hard-cast Pirates still work; Hold reanimation until needed. *strategic_judgment · high* — [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md)
- **one-shot-reanimation:** Finality counters mean each reanimated Pirate is usually exiled the next time it would die. Mitigations: Power Conduit. *fact · verified* — [brass-02](../interactions/admiral-brass-unsinkable.md#brass-02-finality-counters-mean-exile-not-death)
- **bad-mill:** Commander ETB mill and self-mill may hit lands or non-Pirates. Mitigations: Entomb/Buried Alive choose the card. *strategic_judgment · moderate* — [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md)

## Identity core

- **Admiral Brass, Unsinkable:** Every-turn Pirate reanimation at no card or mana cost. *fact · verified* — `oracle:Admiral Brass, Unsinkable`
- **Power Conduit:** The only card that makes the finality counter go away, turning one-shots into a loop. *strategic_judgment · high* — [brass-03](../interactions/admiral-brass-unsinkable.md#brass-03-power-conduit-removes-the-finality-counter)
- **Entomb:** One-mana setup of the exact Pirate the next combat returns. *strategic_judgment · high* — [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md)
- **Skeleton Crew:** Pays off each reanimation and encore with extra value. *strategic_judgment · high* — [brass-07](../interactions/admiral-brass-unsinkable.md#brass-07-skeleton-crew-triggers-on-every-reanimation-and-encore)
- **Roaming Throne:** Naming Pirate doubles the combat reanimation trigger. *strategic_judgment · moderate* — [brass-04](../interactions/admiral-brass-unsinkable.md#brass-04-roaming-throne-pirate-doubles-the-reanimation)

## Anti-goals and thematic constraints

- ✗ Don't become generic Grixis reanimator: the targets should be Pirates the commander can return.
- ✗ Don't self-mill as an end in itself.
- ✗ Revel in Riches-style off-plan alternate wins were cut for commander synergy (source decision).
  - *strategic_judgment · high* — [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md)
- Theme: Pirate tribal reanimator; nonPirate threats need a role.
  - *strategic_judgment · high* — [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 122.1h:** Finality counter: if the permanent would go to the graveyard, it's exiled instead. *fact · verified* — `cr:122.1h`
- **CR 903.9a:** Commander-zone choice matters for a graveyard deck that may want Brass to stay in the graveyard. *fact · verified* — `cr:903.9a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Pirate synergy", "graveyard as a resource"], "hooked_cards": 33, "role_counts": {"counter": 4, "draw": 7, "protection": 2, "ramp": 21, "removal": 7, "tutor": 5, "wipe": 1}, "lands": 34, "edhrec_pages": ["admiral-brass-unsinkable"]}` *heuristic · low*

## Provenance

- Seeded from: [Admiral_Brass_Unsinkable_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Brass_Unsinkable_v1.md) · [Admiral_Brass_Unsinkable_Deck_Quality_v3.json](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Admiral_Brass_Unsinkable_Deck_Quality_v3.json) · [brass-15](../interactions/admiral-brass-unsinkable.md#brass-15-what-the-list-depends-on)
- Reviewed by: — (not yet reviewed by Cory)
