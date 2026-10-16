# Blueprint — Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/grixistax-october-2026.md), state `SOURCE_BASELINE`, list `lh1:f56e9d1dfe623d6a…`). Machine-readable source: [`data/grixis/blueprints/grixistax-october-2026.json`](../../data/grixis/blueprints/grixistax-october-2026.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Kraum, Ludevic's Opus** — Legendary Creature — Zombie Horror

> Flying, haste  
> Whenever an opponent casts their second spell each turn, draw a card.  
> Partner (You can have two commanders if both have partner.)

**Tevesh Szat, Doom of Fools** — Legendary Planeswalker — Szat

> +2: Create two 0/1 black Thrull creature tokens.  
> +1: You may sacrifice another creature or planeswalker. If you do, draw two cards, then draw another card if the sacrificed permanent was a commander.  
> −10: Gain control of all commanders. Put all commanders from the command zone onto the battlefield under your control.  
> Tevesh Szat, Doom of Fools can be your commander.  
> Partner

## Plan and commander role

- **Primary plan:** Grixis stax: constrict mana, untaps, searches and graveyards (Winter Orb, Static Orb, Blood Moon, Back to Basics, Contamination, Tangle Wire, Trinisphere) while artifact mana and Tevesh's Thrulls break parity, then win with Helm of Obedience + Leyline of the Void/Dauthi Voidwalker or an Underworld Breach finish. *strategic_judgment · high*
- **Secondary:** Taxes over hard one-spell caps keep Kraum's second-spell draw live; Necropotence, Rhystic Study and Mystic Remora refill under the lock.
  - Evidence: [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md) · [grixistax-03](../interactions/grixistax-october-2026.md#grixistax-03-tevesh-thrulls-feed-every-sacrifice-outlet) · [grixistax-09](../interactions/grixistax-october-2026.md#grixistax-09-helm-of-obedience--leyline-of-the-void-or-dauthi-voidwalker)
- **Commander role: significant.** Tevesh Szat is the parity engine (Thrulls pay Contamination, feed Skullclamp, Phyrexian Tower and Culling the Weak); Kraum is evasive pressure and a draw trigger. *strategic_judgment · high*
- ⚠️ **Honest note:** Both win lines (Helm + Leyline/Dauthi, Breach) are commander-independent, and Kraum is close to incidental: he only draws when an opponent casts a second spell, which this deck's own taxes suppress. The pair is chosen for parity breaking, not as an engine the deck can't run without (source: decisions L28).
  - Evidence: [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md) · [grixistax-01](../interactions/grixistax-october-2026.md#grixistax-01-partners-kraum--tevesh-szat) · [grixistax-02](../interactions/grixistax-october-2026.md#grixistax-02-kraum-once-per-opponent-per-turn-under-damping-sphere-too)
- **Dependency level:** medium *strategic_judgment · high* — [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (Power Bracket 5 — fringe / rogue cEDH (decisions).) | *fact · verified* | [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 5 (Bracket 5 ceiling (fringe): full cEDH interaction, tutors and fast mana with compact wins; the pair converts less than leading partner shells, per the source. Agrees with the source.) | *strategic_judgment · high* | [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md) · `spellbook:2163-5065` |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Grixistax___October_2026` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 2, "2": 15, "3": 19, "4": 19, "5": 80}, "decks_with_bracket": 135, "share_b4_plus": 0.733, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__kraum-ludevics-opus-tevesh-szat-doom-of-fools.json`

## Win conditions

- **helm-leyline** (combo): Helm of Obedience with Leyline of the Void or Dauthi Voidwalker exiles an opponent's whole library for {1}. Cards: Helm of Obedience, Leyline of the Void, Dauthi Voidwalker. *fact · verified* — `spellbook:2163-5065` · `spellbook:2581-5065` · [grixistax-09](../interactions/grixistax-october-2026.md#grixistax-09-helm-of-obedience--leyline-of-the-void-or-dauthi-voidwalker)
- **breach** (combo): Underworld Breach with LED/Petal + Brain Freeze or Wheel of Fortune + Jeska's Will/LED; needs your own prison pieces out of the way. Cards: Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze, Wheel of Fortune, Jeska's Will. *fact · verified* — `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856` · `spellbook:1368-1878-2706` · `spellbook:1368-2706-3518` · [grixistax-10](../interactions/grixistax-october-2026.md#grixistax-10-the-breach-finish-needs-your-own-prison-pieces-gone)
- **lock-beatdown** (natural): Under a full lock, Kraum, Sheoldred and Ragavan attack opponents who can't develop. Cards: Sheoldred, the Apocalypse, Ragavan, Nimble Pilferer. Enablers: Kraum, Ludevic's Opus. *strategic_judgment · moderate* — [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md)

## Engines

- **thrull-parity:** Tevesh Szat, Doom of Fools, Contamination, Skullclamp, Phyrexian Tower, Culling the Weak, Diabolic Intent, Tangle Wire, Overburden. Online when: Tevesh in play making Thrulls. *fact · verified* — [grixistax-03](../interactions/grixistax-october-2026.md#grixistax-03-tevesh-thrulls-feed-every-sacrifice-outlet) · [grixistax-06](../interactions/grixistax-october-2026.md#grixistax-06-overburden-and-tangle-wire-with-thrull-tokens)
- **mana-lock:** Winter Orb, Static Orb, Blood Moon, Magus of the Moon, Back to Basics, Contamination, Damping Sphere, Trinisphere, Chalice of the Void. Online when: Artifact mana and Thrulls deployed before the lock. *fact · verified* — [grixistax-04](../interactions/grixistax-october-2026.md#grixistax-04-contamination-damping-sphere-and-blood-moon-on-the-same-land) · [grixistax-07](../interactions/grixistax-october-2026.md#grixistax-07-trinisphere-and-chalice-tax-your-own-free-spells)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:prison` | yes | 12 | Resource denial pieces. | 18: Winter Orb, Static Orb, Blood Moon, Magus of the Moon, Back to Basics, Contamination, Damping Sphere, Trinisphere, Chalice of the Void, Tangle Wire, Torpor Orb, Cursed Totem, Overburden, Narset, Parter of Veils, Ashiok, Dream Render, Notion Thief, Opposition Agent, Leyline of the Void | — | *strategic_judgment · high* | [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:artifact-mana` | yes | 8 | Parity breakers that ignore land locks. | 11: Sol Ring, Mana Vault, Grim Monolith, Chrome Mox, Mox Diamond, Mox Opal, Mox Amber, Lotus Petal, Lion's Eye Diamond, Talisman of Creativity, Talisman of Dominance | — | *strategic_judgment · high* | [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:free-interaction` | yes | 8 | Protect the lock and the win. | 12: Force of Will, Force of Negation, Pact of Negation, Fierce Guardianship, Mental Misstep, Mindbreak Trap, Flusterstorm, Swan Song, Pyroblast, Red Elemental Blast, An Offer You Can't Refuse, Deflecting Swat | — | *strategic_judgment · high* | [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md) |

## Key interactions

- **kraum-trigger:** Kraum draws once per opponent per turn, still under Damping Sphere. (Kraum, Ludevic's Opus, Damping Sphere) *fact · verified* — [grixistax-02](../interactions/grixistax-october-2026.md#grixistax-02-kraum-once-per-opponent-per-turn-under-damping-sphere-too)
- **blood-moon-self:** Blood Moon turns your own Phyrexian Tower into a Mountain. (Blood Moon, Phyrexian Tower, Back to Basics) *fact · verified* — [grixistax-05](../interactions/grixistax-october-2026.md#grixistax-05-blood-moon-strips-your-own-utility-lands-back-to-basics-still-locks-them)
- **self-tax:** Trinisphere and Chalice tax your own free spells and fast mana. (Trinisphere, Chalice of the Void) *fact · verified* — [grixistax-07](../interactions/grixistax-october-2026.md#grixistax-07-trinisphere-and-chalice-tax-your-own-free-spells)
- **karn-wishclaw:** Karn turns off the Wishclaw you hand an opponent. (Karn, the Great Creator, Wishclaw Talisman) *fact · verified* — [grixistax-08](../interactions/grixistax-october-2026.md#grixistax-08-karn-locks-the-wishclaw-you-hand-over)
- **breach-needs-clear:** The Breach finish needs your own prison pieces gone. (Underworld Breach, Damping Sphere) *fact · verified* — [grixistax-10](../interactions/grixistax-october-2026.md#grixistax-10-the-breach-finish-needs-your-own-prison-pieces-gone)

## Tutors and recursion

- Tutor target **Helm of Obedience** via Demonic Tutor, Vampiric Tutor, Imperial Seal, Tainted Pact *strategic_judgment · high* — `spellbook:2163-5065`
- Tutor target **Winter Orb** via Karn, the Great Creator, Diabolic Intent *strategic_judgment · moderate* — [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md)
- Recursion: Underworld Breach, Jeska's Will *strategic_judgment · low* — [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Free counters, Toxic Deluge, Cyclonic Rift, Deadly Rollick.
- **Protection:** Fierce Guardianship, Deflecting Swat, counters.
- **Mana:** Heavy artifact fast mana to break the land locks; 26 lands.
- *strategic_judgment · high* — [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **self-lock:** The prison suite taxes your own mana, spells and utility lands. Mitigations: Sequence artifact mana first; Thrulls for Contamination. *strategic_judgment · high* — [grixistax-07](../interactions/grixistax-october-2026.md#grixistax-07-trinisphere-and-chalice-tax-your-own-free-spells) · [grixistax-05](../interactions/grixistax-october-2026.md#grixistax-05-blood-moon-strips-your-own-utility-lands-back-to-basics-still-locks-them)
- **artifact-removal:** Artifact wipes break parity against you. Mitigations: Counters; Land-based enchantment locks. *strategic_judgment · high* — [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md)
- **breach-blocked:** Your own Damping Sphere/Trinisphere stop the Breach finish. Mitigations: Helm win; Remove own pieces first. *strategic_judgment · moderate* — [grixistax-10](../interactions/grixistax-october-2026.md#grixistax-10-the-breach-finish-needs-your-own-prison-pieces-gone)

## Identity core

- **Tevesh Szat, Doom of Fools:** Thrulls and card draw that break the deck's own parity. *fact · verified* — `oracle:Tevesh Szat, Doom of Fools`
- **Kraum, Ludevic's Opus:** Hasty flier and a draw when opponents cast a second spell. *fact · verified* — `oracle:Kraum, Ludevic's Opus`
- **Contamination:** Thrull-fed lock that turns lands into black mana only. *strategic_judgment · high* — [grixistax-03](../interactions/grixistax-october-2026.md#grixistax-03-tevesh-thrulls-feed-every-sacrifice-outlet)
- **Helm of Obedience:** Compact win with Leyline or Dauthi. *strategic_judgment · high* — [grixistax-09](../interactions/grixistax-october-2026.md#grixistax-09-helm-of-obedience--leyline-of-the-void-or-dauthi-voidwalker)
- **Winter Orb:** Core untap lock broken by artifact mana. *strategic_judgment · high* — [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md)

## Anti-goals and thematic constraints

- ✗ Don't rebuild into stock Kraum/Tevesh turbo-combo (decisions L20).
- ✗ No hard one-spell caps (Arcane Laboratory) that make Kraum's trigger dead and block Breach (decisions L35).
  - *strategic_judgment · high* — [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Stax/prison resource deception; the deck is named for its archetype, not its commanders.
  - *strategic_judgment · high* — [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.124a:** Partner. *fact · verified* — `cr:702.124a`
- **CR 613.1d:** Blood Moon type-changing applies in layer 4. *fact · verified* — `cr:613.1d`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Thrull synergy", "sacrifice", "stealing / casting opponents' cards", "tokens"], "hooked_cards": 17, "role_counts": {"counter": 12, "draw": 8, "protection": 1, "ramp": 15, "removal": 6, "tutor": 8, "wipe": 1}, "lands": 26, "edhrec_pages": ["kraum-ludevics-opus-tevesh-szat-doom-of-fools"]}` *heuristic · low*

## Provenance

- Seeded from: [Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Grixistax_October_2026_Current_Cycle_Decisions_2026-10-14.md) · [Grixistax_October_2026_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Grixistax_October_2026_Approved_2026-10-14.md) · [Grixistax_October_2026_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Grixistax_October_2026_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
