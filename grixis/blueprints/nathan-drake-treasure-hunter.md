# Blueprint — Nathan Drake, Treasure Hunter

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/nathan-drake-treasure-hunter.md), state `SOURCE_BASELINE`, list `lh1:ac167a53ea77215d…`). Machine-readable source: [`data/grixis/blueprints/nathan-drake-treasure-hunter.json`](../../data/grixis/blueprints/nathan-drake-treasure-hunter.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Nathan Drake, Treasure Hunter** — Legendary Creature — Human Rogue

> First strike  
> You may spend mana as though it were mana of any color to cast spells you don't own or to activate abilities of permanents you control but don't own.  
> Whenever Nathan Drake attacks, exile the top card of each player's library. You may cast a spell from among those cards.

## Plan and commander role

- **Primary plan:** Accelerate and protect a three-mana commander and attack with Nathan every turn. Each attack exiles the top card of every library and lets you cast one of them; trigger multipliers and extra combats (Roaming Throne, Firebender Ascension, Karlach, Fire Lord Azula) turn that into a repeatable heist. *strategic_judgment · high*
- **Secondary:** A theft suite (Gonti, Thief of Sanity, Tinybones, Hostage Taker, Opposition Agent, Notion Thief, Laughing Jasper Flint) turns stolen resources into card advantage; payoffs like Don Andres and Nalfeshnee monetize casting cards you don't own.
  - Evidence: [Nathan_Drake_Treasure_Hunter_v1.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) · [Nathan_Drake_Treasure_Hunter_v1.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)
- **Commander role: central.** Nathan is the main card-advantage engine and the reason the list values trigger copies and combat-time mana. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander Spellbook finds no combos in the list, and the source says the deck doesn't run a generic Oracle/Breach finish (blueprint L41). It wins by accumulated advantage and combat damage, so it's a low-to-mid Bracket 4 value deck. Nathan is central to the engine but provides no compact kill. No M1 interaction review exists yet for this deck.
  - Evidence: [Nathan_Drake_Treasure_Hunter_v1.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) · [Nathan_Drake_Treasure_Hunter_v1.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)
- **Dependency level:** high *strategic_judgment · high* — [Nathan_Drake_Treasure_Hunter_v1.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint v1).) | *fact · verified* | [Nathan_Drake_Treasure_Hunter_v1.md#L39](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling, low end: strong value engine and premium staples, but no compact win. Agrees with the source.) | *strategic_judgment · high* | [Nathan_Drake_Treasure_Hunter_v1.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Nathan_Drake__Treasure_Hunter` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 11, "2": 178, "3": 283, "4": 92, "5": 13}, "decks_with_bracket": 577, "share_b4_plus": 0.182, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__nathan-drake-treasure-hunter.json`

## Win conditions

- **advantage-combat** (natural): Out-value the table with stolen spells and win through combat with first strike, extra combats and stolen threats. Cards: Nathan Drake, Treasure Hunter, Karlach, Fury of Avernus, Fire Lord Azula, Etali, Primal Storm, Ragavan, Nimble Pilferer. Enablers: Roaming Throne, Firebender Ascension. *strategic_judgment · moderate* — [Nathan_Drake_Treasure_Hunter_v1.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)
- **stolen-wincons** (alternate): Whatever win condition the opponents' libraries provide; it can't be planned for. Cards: Nathan Drake, Treasure Hunter. Enablers: Gonti, Night Minister, Thief of Sanity, Tinybones, the Pickpocket. *strategic_judgment · moderate* — [Nathan_Drake_Treasure_Hunter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)

## Engines

- **nathan-heist:** Nathan Drake, Treasure Hunter, Roaming Throne, Firebender Ascension, Karlach, Fury of Avernus, Fire Lord Azula, Fire Nation Palace, Arena of Glory. Online when: Nathan attacks with mana available for the stolen spell. *fact · high* — `oracle:Nathan Drake, Treasure Hunter` · [Nathan_Drake_Treasure_Hunter_v1.md#L9](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)
- **theft-payoffs:** Don Andres, the Renegade, Passionate Archaeologist, Nalfeshnee, Prosper, Tome-Bound, Gonti, Night Minister, Thief of Sanity, Opposition Agent, Notion Thief. Online when: Casting cards you don't own. *strategic_judgment · high* — [Nathan_Drake_Treasure_Hunter_v1.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:trigger-scaling` | yes | 4 | More Nathan attack triggers per turn. | 4: Roaming Throne, Firebender Ascension, Karlach, Fury of Avernus, Fire Lord Azula | — | *strategic_judgment · high* | [Nathan_Drake_Treasure_Hunter_v1.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) · [Nathan_Drake_Treasure_Hunter_v1.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) · [Nathan_Drake_Treasure_Hunter_v1.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) · [Nathan_Drake_Treasure_Hunter_v1.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) |
| `pkg:haste-protection` | yes | 4 | Safe, immediate attacks. | 7: Lightning Greaves, Swiftfoot Boots, Arena of Glory, Fierce Guardianship, Deflecting Swat, Force of Negation, Swan Song | — | *strategic_judgment · high* | [Nathan_Drake_Treasure_Hunter_v1.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) · [Nathan_Drake_Treasure_Hunter_v1.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) |
| `pkg:theft` | yes | 8 | Steal opponents' resources. | 11: Gonti, Night Minister, Thief of Sanity, Tinybones, the Pickpocket, Hostage Taker, Opposition Agent, Notion Thief, Laughing Jasper Flint, Robber of the Rich, Black Cat, Cunning Thief, Stolen Strategy, Siphon Insight | — | *strategic_judgment · high* | [Nathan_Drake_Treasure_Hunter_v1.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) |

## Key interactions

- **attack-not-damage:** Nathan triggers when he's declared as an attacker, not on damage; evasion only matters to keep him alive. (Nathan Drake, Treasure Hunter) *fact · high* — `oracle:Nathan Drake, Treasure Hunter` · [Nathan_Drake_Treasure_Hunter_v1.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)
- **any-color-mana:** Mana spends as any color only for spells you don't own and abilities of permanents you don't own. (Nathan Drake, Treasure Hunter) *fact · high* — `oracle:Nathan Drake, Treasure Hunter`
- **firebending-window:** Fire Nation Palace's firebending makes mana before Nathan's trigger resolves, paying for the stolen spell. (Nathan Drake, Treasure Hunter, Fire Nation Palace) *fact · high* — [Nathan_Drake_Treasure_Hunter_v1.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) · `cr:702.189a`
- **roaming-throne-rogue:** Roaming Throne naming Rogue doubles Nathan's attack trigger. (Roaming Throne, Nathan Drake, Treasure Hunter) *fact · high* — [Nathan_Drake_Treasure_Hunter_v1.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)

## Tutors and recursion

- Tutor target **Roaming Throne** via Demonic Tutor, Vampiric Tutor, Praetor's Grasp *strategic_judgment · moderate* — [Nathan_Drake_Treasure_Hunter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)
- Recursion: Reanimate, Jeska's Will *strategic_judgment · moderate* — [Nathan_Drake_Treasure_Hunter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)

## Requirements

- **Interaction:** Mana Drain, Force of Negation, Swan Song, An Offer You Can't Refuse, Chaos Warp, Cyclonic Rift, Blasphemous Act.
- **Protection:** Boots, Greaves, Fierce Guardianship, Deflecting Swat.
- **Mana:** 34 lands, Sol Ring, Lotus Petal, Dark Ritual, Talismans.
- *strategic_judgment · moderate* — [Nathan_Drake_Treasure_Hunter_v1.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) · [Nathan_Drake_Treasure_Hunter_v1.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)

## Failure modes

- **nathan-dies-in-combat:** Nathan is a small attacker; blockers and removal shut off the engine. Mitigations: First strike; Protection. *strategic_judgment · high* — [Nathan_Drake_Treasure_Hunter_v1.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)
- **no-compact-kill:** No deterministic win, so long games against interaction-heavy tables. Mitigations: Theft of opponents' finishers. *strategic_judgment · high* — [Nathan_Drake_Treasure_Hunter_v1.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)
- **mana-in-combat:** Stolen spells need mana during combat. Mitigations: Firebending; Treasures. *strategic_judgment · moderate* — [Nathan_Drake_Treasure_Hunter_v1.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)

## Identity core

- **Nathan Drake, Treasure Hunter:** Attack-trigger heist engine. *fact · verified* — `oracle:Nathan Drake, Treasure Hunter`
- **Roaming Throne:** Doubles the trigger. *strategic_judgment · high* — [Nathan_Drake_Treasure_Hunter_v1.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)
- **Karlach, Fury of Avernus:** Extra combat and untap. *strategic_judgment · high* — [Nathan_Drake_Treasure_Hunter_v1.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)
- **Fire Lord Azula:** Combat mana and spell copy. *strategic_judgment · high* — [Nathan_Drake_Treasure_Hunter_v1.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)
- **Firebender Ascension:** Copies attack triggers. *strategic_judgment · moderate* — [Nathan_Drake_Treasure_Hunter_v1.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)

## Anti-goals and thematic constraints

- ✗ Don't add theft cards just for popularity (blueprint L51).
- ✗ Don't over-invest in damage-only evasion (blueprint L52).
  - *strategic_judgment · high* — [Nathan_Drake_Treasure_Hunter_v1.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) · [Nathan_Drake_Treasure_Hunter_v1.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)
- Theme: Treasure-hunter heists from every library.
  - *strategic_judgment · moderate* — [Nathan_Drake_Treasure_Hunter_v1.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 508.1:** Declare attackers; attack triggers. *fact · verified* — `cr:508.1`
- **CR 702.189a:** Firebending. *fact · verified* — `cr:702.189a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["combat damage / attack triggers", "playing cards from exile", "stealing / casting opponents' cards"], "hooked_cards": 36, "role_counts": {"counter": 5, "draw": 5, "protection": 3, "ramp": 21, "removal": 5, "tutor": 2, "wipe": 1}, "lands": 34, "edhrec_pages": ["nathan-drake-treasure-hunter"]}` *heuristic · low*

## Provenance

- Seeded from: [Nathan_Drake_Treasure_Hunter_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nathan_Drake_Treasure_Hunter_v1.md) · [Nathan_Drake_Treasure_Hunter_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Nathan_Drake_Treasure_Hunter_Candidate_Decisions_2026-10-15.md) · [Nathan_Drake_Treasure_Hunter_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Nathan_Drake_Treasure_Hunter_Approved_2026-10-15.md) · [Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nathan_Drake_Treasure_Hunter_Approval_Ready_Verification_2026-10-15.md) · [Nathan_Drake_Treasure_Hunter_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nathan_Drake_Treasure_Hunter_Whole_List_Audit_2026-10-15.md) · [Nathan_Drake_Treasure_Hunter_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Nathan_Drake_Treasure_Hunter_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
