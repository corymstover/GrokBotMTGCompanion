# Blueprint — Mishra, Artificer Prodigy

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/mishra-artificer-prodigy.md), state `SOURCE_BASELINE`, list `lh1:c5f0c3e61664642e…`). Machine-readable source: [`data/grixis/blueprints/mishra-artificer-prodigy.json`](../../data/grixis/blueprints/mishra-artificer-prodigy.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Mishra, Artificer Prodigy** — Legendary Creature — Human Artificer

> Whenever you cast an artifact spell, you may search your graveyard, hand, and/or library for a card with the same name as that spell and put it onto the battlefield. If you search your library this way, shuffle.

## Plan and commander role

- **Primary plan:** Artifact stax-combo: run symmetrical artifact-spell counters (Void Mirror, Chalice of the Void, Blood Funnel, Nether Void, Nullstone Gargoyle, Possibility Storm, Vexing Bauble, Planar Chaos) that only Mishra breaks. His cast trigger can put the countered or exiled card back onto the battlefield from graveyard or library, so the stax hurts opponents only. *strategic_judgment · high*
- **Secondary:** Fast artifact mana and tutors assemble commander-free artifact kills: Sensei's Divining Top with Mystic Forge or The Reality Chip, KCI + Scrap Trawler + Myr Retriever, Karn + Aetherflux, or the Karn/Vandalblast + Mycosynth Lattice lock.
  - Evidence: [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md) · [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)
- **Commander role: central.** Mishra turns the deck's own symmetrical counters into one-sided stax: with both triggers ordered, a countered artifact still reaches the battlefield from the graveyard (or from the library after Possibility Storm). *strategic_judgment · high*
- ⚠️ **Honest note:** Mishra is central to the stax half, but none of the 20 Spellbook combos in the list uses him. The kills are generic artifact engines, so without Mishra the deck is a weaker, self-locking artifact pile. His trigger finds only same-name cards; in singleton that means the spell he just cast, after it has left the stack. The cycle 51 M1 review (mishraap-01..10) flags two anti-synergies: the stax hits your own non-artifact spells (mishraap-04), and Void Mirror/Bauble break your own loops without Mishra (mishraap-05). That raises his real importance to the kills too.
  - Evidence: [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md) · [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)
- **Dependency level:** high *strategic_judgment · high* — [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md) · [mishraap-05](../interactions/mishra-artificer-prodigy.md#mishraap-05-without-mishra-void-mirror-and-vexing-bauble-break-your-own-top-and-kci-loops)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (Power Bracket 5 — cEDH (fringe / commander-centric artifact stax-combo).) | *fact · verified* | [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md) |
| GrokBot estimated ceiling | 5 (Bracket 5 ceiling, fringe: Workshop/Moxen speed, Force suite, Lattice lock and several compact artifact infinites, with a commander-specific stax edge. Agrees with the source; expect it to sit at the low end of cEDH.) | *strategic_judgment · moderate* | [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md) · `spellbook:1976-5078-5243` |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Mishra__Artificer_Prodigy` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 6, "2": 29, "3": 70, "4": 63, "5": 15}, "decks_with_bracket": 183, "share_b4_plus": 0.426, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__mishra-artificer-prodigy.json`

## Win conditions

- **top-loops** (combo): Sensei's Divining Top with a cost reducer or untapper (Etherium Sculptor, Foundry Inspector, Cloud Key, Enthusiastic Mechanaut) plus The Reality Chip or Mystic Forge draws the library. Cards: Sensei's Divining Top, The Reality Chip, Mystic Forge, Etherium Sculptor, Foundry Inspector, Cloud Key, Enthusiastic Mechanaut. *fact · verified* — `spellbook:1976-5078-5243` · `spellbook:2146-5078-5243` · `spellbook:777-5078-5243` · `spellbook:4908-5078-5243` · `spellbook:777-985-5078` · `spellbook:985-1976-5078` · `spellbook:985-2146-5078` · `spellbook:985-4908-5078`
- **aetherflux** (combo): Aetherflux Reservoir with Top + Bolas's Citadel, or with Karn, the Great Creator. Cards: Aetherflux Reservoir, Sensei's Divining Top, Bolas's Citadel, Karn, the Great Creator. *fact · verified* — `spellbook:2173-4740-5078` · `spellbook:4740-5089`
- **kci-loop** (combo): Krark-Clan Ironworks + Scrap Trawler + Myr Retriever with a cost reducer or untapper. Cards: Krark-Clan Ironworks, Scrap Trawler, Myr Retriever, Etherium Sculptor, Foundry Inspector, Cloud Key, Enthusiastic Mechanaut. *fact · verified* — `spellbook:1020-1976-2866-4659` · `spellbook:1020-2146-2866-4659` · `spellbook:777-1020-2866-4659` · `spellbook:1020-2866-4659-4908`
- **lattice-lock** (alternate): Lock rather than kill: Mycosynth Lattice with Karn, the Great Creator (lock) or Vandalblast (wipe), then win at leisure. Cards: Mycosynth Lattice, Karn, the Great Creator, Vandalblast. *fact · high* — `spellbook:3263-5089` · `spellbook:2552-3263`

## Engines

- **self-counter-recovery:** Mishra, Artificer Prodigy, Void Mirror, Chalice of the Void, Blood Funnel, Nether Void, Nullstone Gargoyle, Possibility Storm. Online when: Mishra in play, an artifact spell cast, and the counter trigger ordered to resolve before Mishra's. *fact · high* — `oracle:Mishra, Artificer Prodigy` · [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)
- **artifact-mana:** Mishra's Workshop, Mana Vault, Grim Monolith, Sol Ring, Chrome Mox, Mox Opal, Mox Amber, Mox Diamond, Metalworker, Urza, Lord High Artificer. Online when: Opening hand. *strategic_judgment · high* — [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:parity-stax` | yes | 6 | Symmetrical counters that Mishra breaks. | 8: Void Mirror, Chalice of the Void, Blood Funnel, Nether Void, Nullstone Gargoyle, Possibility Storm, Vexing Bauble, Planar Chaos | — | *strategic_judgment · high* | [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md) |
| `pkg:artifact-tutors` | yes | 6 | Find engine pieces. | 12: Fabricate, Whir of Invention, Transmute Artifact, Tezzeret the Seeker, Goblin Engineer, Demonic Tutor, Vampiric Tutor, Praetor's Grasp, Gamble, Wishclaw Talisman, Urza's Saga, Inventors' Fair | — | *strategic_judgment · high* | [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md) |
| `pkg:stack-protection` | yes | 4 | Protect the combo turn. | 5: Force of Will, Force of Negation, Fierce Guardianship, Swan Song, Mana Drain | — | *strategic_judgment · high* | [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md) |

## Key interactions

- **trigger-ordering:** Mishra's cast trigger and the counter trigger from my own Void Mirror, Chalice, Blood Funnel or Nether Void are both mine, so I order them. If the counter resolves first, the card is in the graveyard when Mishra searches. (Mishra, Artificer Prodigy, Void Mirror, Chalice of the Void, Blood Funnel, Nether Void) *fact · verified* — [mishraap-02](../interactions/mishra-artificer-prodigy.md#mishraap-02-self-counters-as-parity-breakers-blood-funnel-nether-void-nullstone-gargoyle-chalice-void-mirror-vexing-bauble-planar-chaos) · `oracle:Mishra, Artificer Prodigy` · `cr:603.3b`
- **possibility-storm:** Possibility Storm can move the original card through exile to the bottom of the library; Mishra's trigger then finds it there. (Mishra, Artificer Prodigy, Possibility Storm) *fact · verified* — [mishraap-03](../interactions/mishra-artificer-prodigy.md#mishraap-03-possibility-storm--void-mirror--vexing-bauble-lock-mishra-recovers-the-tucked-artifact) · [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)
- **bauble-mirror-lock:** Vexing Bauble/Void Mirror + Possibility Storm is a lock on opponents' spells from hand, not an unconditional lock. (Vexing Bauble, Void Mirror, Possibility Storm) *fact · verified* — [mishraap-03](../interactions/mishra-artificer-prodigy.md#mishraap-03-possibility-storm--void-mirror--vexing-bauble-lock-mishra-recovers-the-tucked-artifact) · [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)
- **same-name-only:** Mishra only finds a card with the same name; in singleton that's the original spell once it has left the stack. (Mishra, Artificer Prodigy) *fact · verified* — [mishraap-01](../interactions/mishra-artificer-prodigy.md#mishraap-01-in-singleton-mishra-only-finds-the-spell-itself-after-its-countered-or-moved) · `oracle:Mishra, Artificer Prodigy`
- **chalice-x0:** A Chalice of the Void that Mishra puts onto the battlefield has X = 0. (Chalice of the Void, Mishra, Artificer Prodigy) *fact · verified* — [mishraap-06](../interactions/mishra-artificer-prodigy.md#mishraap-06-chalice-of-the-void-returned-by-mishra-has-x--0)
- **own-stax-hits-spells:** M1 flag: Blood Funnel, Nether Void, Nullstone, Planar Chaos and Possibility Storm also hit your own instants and sorceries, and Possibility Storm stops the Lattice + overloaded Vandalblast kill. (Blood Funnel, Nether Void, Nullstone Gargoyle, Planar Chaos, Possibility Storm, Vandalblast) *strategic_judgment · moderate* — [mishraap-04](../interactions/mishra-artificer-prodigy.md#mishraap-04-your-own-stax-hits-your-non-artifact-spells-and-possibility-storm-breaks-overloaded-vandalblast)
- **mirror-breaks-own-loops:** M1 flag: with Void Mirror or Vexing Bauble out, the Top/Forge/Reality Chip and KCI loops only work while Mishra is on the battlefield. (Void Mirror, Vexing Bauble, Sensei's Divining Top, Krark-Clan Ironworks, Mishra, Artificer Prodigy) *strategic_judgment · moderate* — [mishraap-05](../interactions/mishra-artificer-prodigy.md#mishraap-05-without-mishra-void-mirror-and-vexing-bauble-break-your-own-top-and-kci-loops)

## Tutors and recursion

- Tutor target **Sensei's Divining Top** via Whir of Invention, Fabricate, Tezzeret the Seeker, Goblin Engineer *strategic_judgment · high* — `spellbook:1976-5078-5243`
- Tutor target **Karn, the Great Creator** via Demonic Tutor, Vampiric Tutor *strategic_judgment · high* — `spellbook:4740-5089`
- Recursion: Academy Ruins, Goblin Welder, Emry, Lurker of the Loch, Scrap Trawler, Myr Retriever, Junk Diver, Mishra, Artificer Prodigy *strategic_judgment · high* — [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Force of Negation, Mana Drain, Swan Song, Cyclonic Rift, Toxic Deluge, Vandalblast.
- **Protection:** Fierce Guardianship, Lightning Greaves.
- **Mana:** Workshop, Monoliths, Moxen, Signets.
- *strategic_judgment · high* — [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)

## Failure modes

- **mishra-removed:** Without Mishra, the parity stax locks the pilot too. Mitigations: Lightning Greaves; commander tax affordable with fast mana. *strategic_judgment · high* — `oracle:Mishra, Artificer Prodigy`
- **artifact-hate:** Artifact removal or stax (Collector Ouphe, Stony Silence) shuts off engines and kills. Mitigations: Counterspells; Karn lock. *strategic_judgment · high* — [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)
- **lock-gaps:** The lock doesn't stop uncounterable effects, abilities or spells not cast from hand. Mitigations: Fast combo. *strategic_judgment · moderate* — [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)

## Identity core

- **Mishra, Artificer Prodigy:** Turns countered artifact spells into free permanents. *fact · verified* — `oracle:Mishra, Artificer Prodigy`
- **Void Mirror:** Counters opponents' colorless spells; Mishra recovers his own. *strategic_judgment · high* — [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)
- **Possibility Storm:** The strongest identity card according to the source. *strategic_judgment · high* — [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)
- **Sensei's Divining Top:** Hub of the main kill. *strategic_judgment · high* — `spellbook:1976-5078-5243`
- **Karn, the Great Creator:** Lattice lock and Aetherflux access. *strategic_judgment · high* — `spellbook:4740-5089`

## Anti-goals and thematic constraints

- ✗ Don't replace the stax package with generic Grixis Oracle/Breach; the asymmetry is the identity (decisions L18).
- ✗ Slower value artifacts (Darksteel Forge, Sai, Padeem) were cut at this ceiling (decisions L48).
  - *strategic_judgment · high* — [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md) · [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)
- Theme: Mishra breaks the artifact counter effects that also hit opponents.
  - *strategic_judgment · high* — [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 603.3b:** APNAP ordering of simultaneous triggers. *fact · verified* — `cr:603.3b`
- **CR 601.2i:** Cast triggers trigger when the spell becomes cast. *fact · verified* — `cr:601.2i`

## Supporting features (heuristic, not identity)

- `{"hooks": ["artifacts"], "hooked_cards": 53, "role_counts": {"counter": 12, "draw": 8, "protection": 1, "ramp": 17, "removal": 3, "tutor": 10, "wipe": 1}, "lands": 29, "edhrec_pages": ["mishra-artificer-prodigy"]}` *heuristic · low*

## Provenance

- Seeded from: [Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Current_Cycle_Decisions_2026-10-15.md) · [Mishra_Artificer_Prodigy_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Mishra_Artificer_Prodigy_Approved_2026-10-15.md) · [Mishra_Artificer_Prodigy_Whole_List_Audit_2026-10-15.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Mishra_Artificer_Prodigy_Whole_List_Audit_2026-10-15.csv) · [Mishra_Artificer_Prodigy_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Mishra_Artificer_Prodigy_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
