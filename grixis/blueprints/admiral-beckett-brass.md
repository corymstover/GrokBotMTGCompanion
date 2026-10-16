# Blueprint — Admiral Beckett Brass

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/admiral-beckett-brass.md), state `SOURCE_BASELINE`, list `lh1:38598ad4616bb802…`). Machine-readable source: [`data/grixis/blueprints/admiral-beckett-brass.json`](../../data/grixis/blueprints/admiral-beckett-brass.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Admiral Beckett Brass** — Legendary Creature — Human Pirate

> Other Pirates you control get +1/+1.  
> At the beginning of your end step, gain control of target nonland permanent controlled by a player who was dealt combat damage by three or more Pirates this turn.

## Plan and commander role

- **Primary plan:** Pirate aggro: develop several evasive Pirates and token makers, connect with three different Pirates against one opponent, and steal their best nonland permanent at every end step while Beckett's anthem grows the team. *strategic_judgment · high*
- **Secondary:** Combat-damage card draw and Treasure ramp (Malcolm, Breeches, Coastal-style draw) plus a creature-theft package (Hostage Taker, Coercive Recruiter, Don Andres) that turns stolen creatures into Pirates.
  - Evidence: [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [beckett-01](../interactions/admiral-beckett-brass.md#beckett-01) · [beckett-16](../interactions/admiral-beckett-brass.md#beckett-16)
- **Commander role: central.** Beckett is both the anthem and the theft engine; the deck's evasion, token and Pirate-density choices exist to meet his three-Pirate condition. *strategic_judgment · high*
- ⚠️ **Honest note:** The three-different-Pirates-to-the-same-player condition is genuinely hard to meet through blockers, and the payoff is one steal per end step (two with Roaming Throne). Without evasion the deck is ordinary tribal aggro.
  - Evidence: [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [beckett-01](../interactions/admiral-beckett-brass.md#beckett-01) · [beckett-02](../interactions/admiral-beckett-brass.md#beckett-02) · [beckett-11](../interactions/admiral-beckett-brass.md#beckett-11)
- **Dependency level:** high *strategic_judgment · high* — [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [beckett-16](../interactions/admiral-beckett-brass.md#beckett-16)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | — (none stated) (No source ceiling stated in the source blueprint, closeout or reconciliation records (checked Bot cycle 50).) | *fact · high* | [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [Admiral_Beckett_Brass_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Admiral_Beckett_Brass_Approval_Ready_Closeout_2026-10-13.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 by card pool (premium tutors, free counters, fast mana) around a fair, combat-dependent commander with no compact win; low-end B4.) | *strategic_judgment · moderate* | [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [beckett-16](../interactions/admiral-beckett-brass.md#beckett-16) · [deck page](../decks/admiral-beckett-brass.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Admiral_Beckett_Brass` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | — (no source ceiling) | | |

- EDHREC: `{"bracket_counts": {"1": 31, "2": 659, "3": 281, "4": 74, "5": 8}, "decks_with_bracket": 1053, "share_b4_plus": 0.078, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__admiral-beckett-brass.json`

## Win conditions

- **pirate-beats-and-theft** (natural): Wide evasive Pirate attacks pumped by lords and Beckett, stealing a blocker, rock or threat each end step until the table falls behind. Cards: Admiral Beckett Brass, Fathom Fleet Captain, Dire Fleet Captain, Corsair Captain, Port Razer. Enablers: Cover of Darkness, Open into Wonder, Siren Stormtamer. *strategic_judgment · high* — [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [beckett-01](../interactions/admiral-beckett-brass.md#beckett-01)
- **port-razer-combats** (natural): Port Razer's extra combats let the same Pirates connect again; Beckett's tally counts damage across all combats this turn. Cards: Port Razer. Enablers: Lightning Greaves. *strategic_judgment · moderate* — [beckett-10](../interactions/admiral-beckett-brass.md#beckett-10)

## Engines

- **end-step-theft:** Admiral Beckett Brass, Roaming Throne. Online when: Three or more different Pirates dealt combat damage to one player this turn. *fact · verified* — [beckett-01](../interactions/admiral-beckett-brass.md#beckett-01) · [beckett-02](../interactions/admiral-beckett-brass.md#beckett-02)
- **combat-draw-and-treasure:** Bident of Thassa, Kindred Discovery, Malcolm, Keen-Eyed Navigator, Breeches, Brazen Plunderer, Ramirez DePietro, Pillager, Captain Lannery Storm. Online when: Pirates connect. *strategic_judgment · high* — [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:evasion` | yes | 6 | Make three Pirates connect with the same opponent. | 10: Changeling Outcast, Cover of Darkness, Daring Saboteur, Siren Stormtamer, Storm Fleet Sprinter, Warkite Marauder, Open into Wonder, Spectral Sailor, Spyglass Siren, Kitesail Freebooter | Slippery Scoundrel | *strategic_judgment · high* | [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [beckett-11](../interactions/admiral-beckett-brass.md#beckett-11) |
| `pkg:pirate-bodies-and-tokens` | yes | 5 | Keep enough Pirates on board to re-trigger Beckett after removal. | 6: Fathom Fleet Captain, Daring Piracy, Kari Zev, Skyship Raider, Black Market Connections, Admiral Brass, Unsinkable, Merchant Raiders | — | *strategic_judgment · high* | [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) |
| `pkg:pirate-lords` | yes | 3 | Tribal pumps that win combats. | 4: Admiral Beckett Brass, Dire Fleet Captain, Corsair Captain, Francisco, Fowl Marauder | Fell Flagship | *strategic_judgment · high* | [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [beckett-14](../interactions/admiral-beckett-brass.md#beckett-14) |
| `pkg:creature-theft` | optional | 3 | Steal creatures and make them Pirates (they count for Beckett). | 4: Hostage Taker, Coercive Recruiter, Don Andres, the Renegade, Zara, Renegade Recruiter | — | *fact · verified* | [beckett-04](../interactions/admiral-beckett-brass.md#beckett-04) · [beckett-05](../interactions/admiral-beckett-brass.md#beckett-05) |
| `pkg:interaction-protection` | yes | 8 | Clear blockers, survive sweepers, protect the attack. | 11: Fierce Guardianship, Deflecting Swat, Counterspell, Mana Drain, Chaos Warp, Toxic Deluge, Cyclonic Rift, Fiery Cannonade, Raise the Palisade, Lightning Greaves, Feed the Swarm | — | *strategic_judgment · high* | [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [beckett-07](../interactions/admiral-beckett-brass.md#beckett-07) |

## Key interactions

- **three-pirates:** Three different Pirates must deal combat damage to the same player this turn; theft is permanent. (Admiral Beckett Brass) *fact · verified* — [beckett-01](../interactions/admiral-beckett-brass.md#beckett-01)
- **throne-doubles:** Roaming Throne naming Pirate doubles Beckett's end-step steal (separate targets). (Roaming Throne, Admiral Beckett Brass) *fact · verified* — [beckett-02](../interactions/admiral-beckett-brass.md#beckett-02) · [beckett-09](../interactions/admiral-beckett-brass.md#beckett-09)
- **kari-monkey:** Kari Zev's Ragavan token is a Monkey, not a Pirate: it doesn't count. (Kari Zev, Skyship Raider) *fact · verified* — [beckett-03](../interactions/admiral-beckett-brass.md#beckett-03)
- **changelings:** Changelings count as Pirates. (Changeling Outcast) *fact · verified* — [beckett-06](../interactions/admiral-beckett-brass.md#beckett-06)
- **one-sided-sweepers:** Fiery Cannonade spares Pirates; Raise the Palisade spares the chosen type. (Fiery Cannonade, Raise the Palisade) *fact · verified* — [beckett-07](../interactions/admiral-beckett-brass.md#beckett-07)

## Tutors and recursion

- Tutor target **Roaming Throne** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md)
- Tutor target **Open into Wonder** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md)
- Recursion: The Indomitable *fact · verified* — [beckett-12](../interactions/admiral-beckett-brass.md#beckett-12)

## Requirements

- **Interaction:** Blocker removal and one-sided sweepers matter more than counters; keep ~8-11 interaction pieces.
- **Protection:** Greaves plus free protection (Fierce Guardianship, Deflecting Swat); the anthem dies with Beckett.
- **Mana:** Four-mana commander; Treasure makers and rocks; 33 lands.
- *strategic_judgment · moderate* — [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [Admiral_Beckett_Brass_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Admiral_Beckett_Brass_Approval_Ready_Closeout_2026-10-13.md)

## Failure modes

- **blocked-out:** Blockers or fog effects stop the third Pirate from connecting, so no steal. Mitigations: Evasion package; Open into Wonder; Cyclonic Rift on a key turn. *strategic_judgment · high* — [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [beckett-01](../interactions/admiral-beckett-brass.md#beckett-01)
- **sweeper-reset:** A board wipe removes the Pirate density the condition needs. Mitigations: Token makers; Raise the Palisade/Cannonade are one-sided; Admiral Brass reanimates Pirates. *strategic_judgment · high* — [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md)
- **commander-removal:** Beckett removed repeatedly: the theft engine and anthem are gone. Mitigations: Lightning Greaves; Free protection. *strategic_judgment · moderate* — [beckett-15](../interactions/admiral-beckett-brass.md#beckett-15)

## Identity core

- **Admiral Beckett Brass:** Anthem plus the end-step theft that defines the deck. *fact · verified* — `oracle:Admiral Beckett Brass`
- **Roaming Throne:** Naming Pirate doubles both Beckett's theft and the Pirate ETB/attack triggers. *strategic_judgment · high* — [beckett-09](../interactions/admiral-beckett-brass.md#beckett-09)
- **Fathom Fleet Captain:** Each attack makes another Pirate token, refilling the three-Pirate count. *strategic_judgment · high* — [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md)
- **Cover of Darkness:** Naming Pirate gives the whole crew fear: the most direct answer to blockers. *strategic_judgment · high* — [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [beckett-11](../interactions/admiral-beckett-brass.md#beckett-11)
- **Coercive Recruiter:** Every Pirate ETB steals a creature and makes it a Pirate that can attack for the count. *fact · verified* — [beckett-04](../interactions/admiral-beckett-brass.md#beckett-04)

## Anti-goals and thematic constraints

- ✗ Don't dilute Pirate density for generic Grixis value creatures.
- ✗ Don't trim blocker removal/protection just to add more Pirates.
- ✗ Don't add one-shot effects unless they convert a key combat into theft or a kill.
  - *strategic_judgment · high* — [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md)
- Theme: Pirate tribal; non-Pirate creatures need a reason (theft, protection, draw).
  - *strategic_judgment · high* — [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 704.5j:** Double Down copies of legendary Pirates hit the legend rule; both ETBs still happen. *fact · verified* — `cr:704.5j` · [beckett-08](../interactions/admiral-beckett-brass.md#beckett-08)
- **CR 903.8:** Commander tax on a four-mana commander that is a removal magnet. *fact · verified* — `cr:903.8`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Pirate synergy", "combat damage / attack triggers", "stealing / casting opponents' cards"], "hooked_cards": 42, "role_counts": {"counter": 4, "draw": 8, "protection": 2, "ramp": 19, "removal": 4, "tutor": 3, "wipe": 2}, "lands": 35, "edhrec_pages": ["admiral-beckett-brass"]}` *heuristic · low*

## Provenance

- Seeded from: [Admiral_Beckett_Brass_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Admiral_Beckett_Brass_v1.md) · [Admiral_Beckett_Brass_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Admiral_Beckett_Brass_Approval_Ready_Closeout_2026-10-13.md) · [Admiral_Beckett_Brass_Approval_Ready_2026-10-13.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Admiral_Beckett_Brass_Approval_Ready_2026-10-13.txt) · [beckett-16](../interactions/admiral-beckett-brass.md#beckett-16)
- Reviewed by: — (not yet reviewed by Cory)
