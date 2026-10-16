# Blueprint — Sedris, the Traitor King

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/sedris-the-traitor-king.md), state `SOURCE_BASELINE`, list `lh1:8b145ace962d556a…`). Machine-readable source: [`data/grixis/blueprints/sedris-the-traitor-king.json`](../../data/grixis/blueprints/sedris-the-traitor-king.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Sedris, the Traitor King** — Legendary Creature — Zombie Warrior

> Each creature card in your graveyard has unearth {2}{B}. ({2}{B}: Return the card to the battlefield. The creature gains haste. Exile it at the beginning of the next end step or if it would leave the battlefield. Unearth only as a sorcery.)

## Plan and commander role

- **Primary plan:** Unearth reanimator: self-mill and discard creatures, then use Sedris's granted unearth {2}{B} (down to {B} with Convergence of Dominion) to return ETB creatures each turn, with Panharmonicon doubling their ETBs. *strategic_judgment · high*
- **Secondary:** Keep unearthed creatures by ending the turn with Obeka or Sundial, or phasing them with Teferi's Veil; Deadeye Navigator + Peregrine Drake is the combo package.
  - Evidence: [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)
- **Commander role: central.** Sedris gives every creature card in the graveyard unearth, which makes the whole graveyard reusable. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native. The one Spellbook combo (1409-3821, Deadeye Navigator + Peregrine Drake) doesn't need Sedris, but Sedris can unearth either half. The deck has backup reanimation (Reanimate, Animate Dead, Necromancy, Living Death) but is far weaker without him. There is no source blueprint file; the closeout and verification are the evidence. M1 review (sedris-01..06, all verified) confirms the unearth and rescue rules.
  - Evidence: [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · `spellbook:1409-3821`
- **Dependency level:** high *strategic_judgment · high* — [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions).) | *fact · verified* | [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L58](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: deep reanimator with a two-card combo and premium staples; a graveyard deck with a six-mana commander, not cEDH. Agrees with the source.) | *strategic_judgment · high* | [Sedris_the_Traitor_King_Approval_Ready_Verification_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Sedris_the_Traitor_King_Approval_Ready_Verification_2026-10-15.md) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Sedris__the_Traitor_King` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 6, "2": 178, "3": 181, "4": 66, "5": 5}, "decks_with_bracket": 436, "share_b4_plus": 0.163, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__sedris-the-traitor-king.json`

## Win conditions

- **etb-value-beats** (natural): Repeated hasty unearth of Archon, Grave Titan, Massacre Wurm or Terror of the Peaks. Cards: Sedris, the Traitor King, Archon of Cruelty, Grave Titan, Massacre Wurm, Sepulchral Primordial, Terror of the Peaks. Enablers: Panharmonicon, Convergence of Dominion. *strategic_judgment · high* — [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)
- **drake-navigator** (combo): Peregrine Drake + Deadeye Navigator for infinite mana, then sinks such as Goblin Bombardment or repeated unearth. Cards: Peregrine Drake, Deadeye Navigator. Enablers: Goblin Bombardment. *strategic_judgment · high* — `spellbook:1409-3821` · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)

## Engines

- **granted-unearth:** Sedris, the Traitor King, Convergence of Dominion. Online when: Sedris on the battlefield; creature cards in the graveyard. *fact · high* — `oracle:Sedris, the Traitor King` · `cr:702.84a`
- **unearth-rescue:** Obeka, Brute Chronologist, Sundial of the Infinite, Teferi's Veil, Deadeye Navigator. Online when: An unearthed creature with its exile trigger pending. *strategic_judgment · high* — [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:etb-targets` | yes | 7 | ETB creatures worth unearthing. | 10: Archon of Cruelty, Grave Titan, Massacre Wurm, Sepulchral Primordial, Sheoldred, Whispering One, Jin-Gitaxias, Core Augur, Rune-Scarred Demon, Terror of the Peaks, Etali, Primal Storm, Burning-Rune Demon | — | *strategic_judgment · high* | [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) |
| `pkg:self-mill` | yes | 6 | Fill the graveyard. | 9: Entomb, Buried Alive, Faithless Looting, Frantic Search, Gifts Ungiven, Ripples of Undeath, Likeness Looter, Corpse Connoisseur, Convergence of Dominion | — | *strategic_judgment · high* | [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) |
| `pkg:rescue` | yes | 4 | Keep unearthed creatures. | 4: Obeka, Brute Chronologist, Sundial of the Infinite, Teferi's Veil, Deadeye Navigator | — | *strategic_judgment · high* | [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) |

## Key interactions

- **convergence-floor:** Convergence makes unearth {B}; it can't go below one mana. (Convergence of Dominion, Sedris, the Traitor King) *fact · verified* — [sedris-02](../interactions/sedris-the-traitor-king.md#sedris-02-convergence-of-dominion-makes-unearth-cost-b) · `oracle:Convergence of Dominion` · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)
- **end-turn-exile:** Ending the turn with Obeka or Sundial while the exile trigger is on the stack removes it. (Obeka, Brute Chronologist, Sundial of the Infinite) *fact · verified* — [sedris-03](../interactions/sedris-the-traitor-king.md#sedris-03-keeping-unearthed-creatures-obeka--sundial-on-the-exile-trigger-teferis-veil-phase-out-deadeye-blink) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · `cr:723.1`
- **veil-phase:** Teferi's Veil phases attackers out at end of combat, so the end-step exile trigger can't find them. (Teferi's Veil) *fact · verified* — [sedris-03](../interactions/sedris-the-traitor-king.md#sedris-03-keeping-unearthed-creatures-obeka--sundial-on-the-exile-trigger-teferis-veil-phase-out-deadeye-blink) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)
- **navigator-reset:** Deadeye resets an unearthed creature as a new object; the unearth replacement doesn't replace an exile already happening. (Deadeye Navigator) *fact · verified* — [sedris-03](../interactions/sedris-the-traitor-king.md#sedris-03-keeping-unearthed-creatures-obeka--sundial-on-the-exile-trigger-teferis-veil-phase-out-deadeye-blink) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)
- **kelpie-draw:** Unearthed creatures enter from a graveyard and trigger River Kelpie. (River Kelpie) *fact · verified* — [sedris-04](../interactions/sedris-the-traitor-king.md#sedris-04-enter-from-graveyard-payoffs-river-kelpie-twilight-diviner-panharmonicon) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)
- **granted-unearth-rules:** Sedris-granted unearth is each card's own sorcery-speed activated ability with both exile clauses. (Sedris, the Traitor King) *fact · verified* — [sedris-01](../interactions/sedris-the-traitor-king.md#sedris-01-sedris-granted-unearth-an-activated-ability-of-each-card-sorcery-speed-with-two-exile-clauses)
- **drake-navigator-m1:** Peregrine Drake + Deadeye Navigator is infinite mana and blinks. (Peregrine Drake, Deadeye Navigator) *fact · verified* — [sedris-05](../interactions/sedris-the-traitor-king.md#sedris-05-peregrine-drake--deadeye-navigator-infinite-mana-and-blinks)

## Tutors and recursion

- Tutor target **Archon of Cruelty** via Entomb, Buried Alive, Demonic Tutor, Rune-Scarred Demon *strategic_judgment · high* — [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L44](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)
- Recursion: Reanimate, Animate Dead, Necromancy, Dread Return, Living Death, Chainer, Nightmare Adept, Sedris, the Traitor King *strategic_judgment · high* — [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Fierce Guardianship, Mana Drain, Deadly Rollick, Feed the Swarm, Cyclonic Rift, Toxic Deluge.
- **Protection:** Force of Will, Deflecting Swat, Lightning Greaves.
- **Mana:** 31 lands, fast mana and Signets for a six-mana commander.
- *strategic_judgment · moderate* — [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)

## Failure modes

- **graveyard-hate:** Graveyard hate shuts off unearth and the backup reanimation. Mitigations: Fresh self-mill; Hard casts. *strategic_judgment · high* — `oracle:Sedris, the Traitor King`
- **six-drop:** Sedris costs six; slow without fast mana. Mitigations: Grim Monolith; Mana Vault. *strategic_judgment · high* — [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)
- **unearth-exile:** Unearthed creatures are exiled without rescue. Mitigations: Obeka; Sundial; Teferi's Veil. *strategic_judgment · moderate* — `cr:702.84a`

## Identity core

- **Sedris, the Traitor King:** Unearth {2}{B} for every creature card in the graveyard. *fact · verified* — `oracle:Sedris, the Traitor King`
- **Convergence of Dominion:** Cuts unearth to {B}. *strategic_judgment · high* — [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)
- **Obeka, Brute Chronologist:** Ends the turn to keep unearthed creatures. *strategic_judgment · high* — [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)
- **Panharmonicon:** Doubles ETBs of unearthed creatures. *strategic_judgment · high* — [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)
- **Deadeye Navigator:** Rescue piece and half of the combo. *strategic_judgment · high* — `spellbook:1409-3821`

## Anti-goals and thematic constraints

- ✗ No generic Thassa's Oracle / Underworld Breach conversion (decisions L46).
- ✗ No Hela (future release, no exception; L45).
  - *strategic_judgment · high* — [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)
- Theme: Unearth / reanimator / end-step control (decisions L59).
  - *strategic_judgment · high* — [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.84a:** Unearth. *fact · verified* — `cr:702.84a`
- **CR 723.1:** Ending the turn. *fact · verified* — `cr:723.1`
- **CR 702.26a:** Phasing. *fact · verified* — `cr:702.26a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["unearth / creature cards in your graveyard"], "hooked_cards": 21, "role_counts": {"counter": 3, "draw": 9, "protection": 2, "ramp": 12, "removal": 4, "tutor": 9, "wipe": 1}, "lands": 31, "edhrec_pages": ["sedris-the-traitor-king"]}` *heuristic · low*

## Provenance

- Seeded from: [Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sedris_the_Traitor_King_Candidate_Decisions_2026-10-15.md) · [Sedris_the_Traitor_King_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Sedris_the_Traitor_King_Approved_2026-10-15.md) · [Sedris_the_Traitor_King_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Sedris_the_Traitor_King_Approval_Ready_Verification_2026-10-15.md) · [Sedris_the_Traitor_King_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Sedris_the_Traitor_King_Whole_List_Audit_2026-10-15.md) · [Sedris_the_Traitor_King_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Sedris_the_Traitor_King_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
