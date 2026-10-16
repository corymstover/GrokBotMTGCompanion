# Blueprint — Don Andres, the Renegade

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/don-andres-the-renegade.md), state `SOURCE_BASELINE`, list `lh1:012d9c8c9f3127db…`). Machine-readable source: [`data/grixis/blueprints/don-andres-the-renegade.json`](../../data/grixis/blueprints/don-andres-the-renegade.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Don Andres, the Renegade** — Legendary Creature — Vampire Pirate

> Each creature you control but don't own gets +2/+2, has menace and deathtouch, and is a Pirate in addition to its other types.  
> Whenever you cast a noncreature spell you don't own, create two tapped Treasure tokens.

## Plan and commander role

- **Primary plan:** Play opponents' cards: steal creatures (they become +2/+2 menace deathtouch Pirates) and cast opponents' noncreature spells for two Treasures each, snowballing mana and board from Ragavan, Breeches, Grenzo, Thief of Sanity, Gonti, Hostage Taker and friends. *strategic_judgment · high*
- **Secondary:** Pirate payoffs for the stolen Pirates (Admiral Beckett Brass, Kindred Discovery, Malcolm, Coercive Recruiter) and Insurrection as the mass-theft finisher.
  - Evidence: [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md) · [donandres-01](../interactions/don-andres-the-renegade.md#donandres-01-ownership-not-control-decides-both-of-dons-abilities) · [donandres-02](../interactions/don-andres-the-renegade.md#donandres-02-the-treasure-trigger-needs-a-noncreature-spell-that-someone-else-owns)
- **Commander role: central.** Both theft axes pay off only through Don: stolen creatures become threats and stolen noncreature casts become Treasure. *strategic_judgment · high*
- ⚠️ **Honest note:** Power depends on what opponents play; casting from your own copies or putting cards onto the battlefield (Jhoira, Reanimate) gives no Treasure.
  - Evidence: [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md) · [donandres-03](../interactions/don-andres-the-renegade.md#donandres-03-copies-you-make-are-spells-you-own) · [donandres-04](../interactions/don-andres-the-renegade.md#donandres-04-putting-a-card-onto-the-battlefield-isnt-casting-it)
- **Dependency level:** high *strategic_judgment · high* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Bracket 4 — Optimized (current-cycle blueprint).) | *fact · verified* | [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Low-to-mid Bracket 4: strong theft value, no compact win, opponent-dependent. Agrees with the source.) | *strategic_judgment · high* | [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md) · [donandres-02](../interactions/don-andres-the-renegade.md#donandres-02-the-treasure-trigger-needs-a-noncreature-spell-that-someone-else-owns) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Don_Andres__the_Renegade` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 23, "2": 872, "3": 477, "4": 67, "5": 5}, "decks_with_bracket": 1444, "share_b4_plus": 0.05, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__don-andres-the-renegade.json`

## Win conditions

- **stolen-board** (natural): A board of opponents' creatures as 2/2-bigger menace deathtouch Pirates. Cards: Don Andres, the Renegade, Hostage Taker, Coercive Recruiter, Thieving Amalgam, Gonti, Night Minister. Enablers: Roaming Throne, Kindred Discovery. *strategic_judgment · high* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)
- **insurrection** (natural): Insurrection steals every creature for a lethal swing, all buffed by Don. Cards: Insurrection. Enablers: Don Andres, the Renegade. *strategic_judgment · high* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)
- **beckett-theft** (natural): Admiral Beckett Brass counts Don-made Pirates and permanently steals each end step. Cards: Admiral Beckett Brass. Enablers: Don Andres, the Renegade. *strategic_judgment · moderate* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md) · [donandres-10](../interactions/don-andres-the-renegade.md#donandres-10-don-makes-stolen-creatures-pirates-for-pirate-payoffs)

## Engines

- **stolen-spell-treasure:** Don Andres, the Renegade, Roaming Throne, Gonti, Night Minister, Tasha, the Witch Queen, Thief of Sanity, Grenzo, Havoc Raiser. Online when: Cast a noncreature spell you don't own. *fact · verified* — [donandres-02](../interactions/don-andres-the-renegade.md#donandres-02-the-treasure-trigger-needs-a-noncreature-spell-that-someone-else-owns) · [donandres-07](../interactions/don-andres-the-renegade.md#donandres-07-roaming-throne-on-pirate-doubles-the-treasure-trigger-not-the-static) · [donandres-11](../interactions/don-andres-the-renegade.md#donandres-11-cast-a-spell-you-dont-own-payoffs-stack-with-don)
- **stolen-creature-buff:** Don Andres, the Renegade, Thieving Amalgam, Hostage Taker, Gilded Drake. Online when: Control a creature you don't own. *fact · verified* — [donandres-01](../interactions/don-andres-the-renegade.md#donandres-01-ownership-not-control-decides-both-of-dons-abilities) · [donandres-05](../interactions/don-andres-the-renegade.md#donandres-05-manifested-opponent-cards-are-22s-that-get-the-bonus)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:card-theft` | yes | 10 | Access opponents' libraries, hands and graveyards. | 14: Ragavan, Nimble Pilferer, Breeches, Brazen Plunderer, Grenzo, Havoc Raiser, Vaan, Street Thief, Locke, Treasure Hunter, Thief of Sanity, Laughing Jasper Flint, Praetor's Grasp, Siphon Insight, Outrageous Robbery, Gonti, Night Minister, Court of Locthwain, Black Cat, Cunning Thief, Arcane Heist | — | *strategic_judgment · high* | [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md) |
| `pkg:creature-theft` | yes | 6 | Take creatures for Don's buff. | 7: Hostage Taker, Gilded Drake, Coercive Recruiter, Thieving Amalgam, Insurrection, Brainstealer Dragon, Seize the Spotlight | — | *strategic_judgment · high* | [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md) |
| `pkg:pirate-payoffs` | optional | 4 | Reward Don-made Pirates. | 6: Admiral Beckett Brass, Kindred Discovery, Malcolm, Keen-Eyed Navigator, Breeches, Eager Pillager, Ramirez DePietro, Pillager, Roaming Throne | — | *strategic_judgment · high* | [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md) |
| `pkg:interaction-protection` | yes | 8 | Interaction and commander protection. | 10: Fierce Guardianship, Deflecting Swat, Mana Drain, Chaos Warp, Deadly Rollick, Feed the Swarm, Toxic Deluge, Cyclonic Rift, Blasphemous Act, Lightning Greaves | — | *strategic_judgment · high* | [Don_Andres_the_Renegade_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Don_Andres_the_Renegade_Approved_2026-10-14.md) |

## Key interactions

- **ownership:** Ownership, not control, decides both abilities. (Don Andres, the Renegade) *fact · verified* — [donandres-01](../interactions/don-andres-the-renegade.md#donandres-01-ownership-not-control-decides-both-of-dons-abilities)
- **copies-and-put:** Copies you make are spells you own; putting onto the battlefield isn't casting. (Arcane Heist, Jhoira, Weatherlight Corsair, Reanimate, Animate Dead) *fact · verified* — [donandres-03](../interactions/don-andres-the-renegade.md#donandres-03-copies-you-make-are-spells-you-own) · [donandres-04](../interactions/don-andres-the-renegade.md#donandres-04-putting-a-card-onto-the-battlefield-isnt-casting-it)
- **amalgam-manifests:** Thieving Amalgam manifests are 4/4 menace deathtouch with Don. (Thieving Amalgam) *fact · verified* — [donandres-05](../interactions/don-andres-the-renegade.md#donandres-05-manifested-opponent-cards-are-22s-that-get-the-bonus)
- **voidwalker-nonbo:** Dauthi Voidwalker turns off Thieving Amalgam's drain. (Dauthi Voidwalker, Thieving Amalgam) *fact · verified* — [donandres-06](../interactions/don-andres-the-renegade.md#donandres-06-dauthi-voidwalker-turns-off-thieving-amalgams-drain)
- **throne:** Roaming Throne (Pirate) doubles the Treasure trigger, not the static. (Roaming Throne) *fact · verified* — [donandres-07](../interactions/don-andres-the-renegade.md#donandres-07-roaming-throne-on-pirate-doubles-the-treasure-trigger-not-the-static)

## Tutors and recursion

- Tutor target **Insurrection** via Vampiric Tutor *strategic_judgment · moderate* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)
- Tutor target **Roaming Throne** via Vampiric Tutor *strategic_judgment · moderate* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)
- Recursion: Animate Dead, Reanimate *strategic_judgment · moderate* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)

## Requirements

- **Interaction:** Moderate; theft doubles as removal.
- **Protection:** Greaves, free protection; Don's static vanishes with him.
- **Mana:** Treasure snowball plus rocks; ~33 lands.
- *strategic_judgment · moderate* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)

## Failure modes

- **weak-opponent-cards:** Opponents' cards are weak or off-color for what you need. Mitigations: Many theft angles. *strategic_judgment · high* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)
- **don-removed:** Without Don stolen creatures shrink and Treasures stop. Mitigations: Protection package. *strategic_judgment · high* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)
- **owner-leaves:** Stolen permanents leave when their owner leaves the game. Mitigations: —. *fact · verified* — [donandres-12](../interactions/don-andres-the-renegade.md#donandres-12-stolen-permanents-leave-with-their-owner)

## Identity core

- **Don Andres, the Renegade:** Turns stolen cards into Pirates and Treasure. *fact · verified* — `oracle:Don Andres, the Renegade`
- **Thief of Sanity:** Repeatable access to opponents' best spells for Treasure. *strategic_judgment · high* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)
- **Thieving Amalgam:** Every opponent's turn makes a Don-buffed manifest. *strategic_judgment · high* — [donandres-05](../interactions/don-andres-the-renegade.md#donandres-05-manifested-opponent-cards-are-22s-that-get-the-bonus)
- **Insurrection:** The dedicated mass-theft finisher. *strategic_judgment · high* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)
- **Gonti, Night Minister:** Another cast-what-you-don't-own engine that stacks with Don. *strategic_judgment · moderate* — [donandres-11](../interactions/don-andres-the-renegade.md#donandres-11-cast-a-spell-you-dont-own-payoffs-stack-with-don)

## Anti-goals and thematic constraints

- ✗ Don't drift into generic Treasure or self-recursion value.
- ✗ Don't rely on put-onto-battlefield effects for Treasure (they aren't casts).
  - *strategic_judgment · high* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)
- Theme: Thieves, pirates and heists.
  - *strategic_judgment · moderate* — [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 111.10a:** Treasure token definition. *fact · verified* — `cr:111.10a`
- **CR 707.10:** Copies you create are owned by you, so they don't trigger Don. *fact · verified* — `cr:707.10`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Pirate synergy", "Treasure", "instants and sorceries", "stealing / casting opponents' cards", "tokens"], "hooked_cards": 46, "role_counts": {"counter": 2, "draw": 4, "protection": 2, "ramp": 21, "removal": 8, "tutor": 1, "wipe": 2}, "lands": 35, "edhrec_pages": ["don-andres-the-renegade"]}` *heuristic · low*

## Provenance

- Seeded from: [Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Don_Andres_the_Renegade_Current_Cycle_Blueprint_2026-10-14.md) · [Don_Andres_the_Renegade_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Don_Andres_the_Renegade_Approved_2026-10-14.md) · [Don_Andres_the_Renegade_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Don_Andres_the_Renegade_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
