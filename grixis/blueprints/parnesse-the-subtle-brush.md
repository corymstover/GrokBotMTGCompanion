# Blueprint — Parnesse, the Subtle Brush

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/parnesse-the-subtle-brush.md), state `SOURCE_BASELINE`, list `lh1:bb86ddd74054d4f5…`). Machine-readable source: [`data/grixis/blueprints/parnesse-the-subtle-brush.json`](../../data/grixis/blueprints/parnesse-the-subtle-brush.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Parnesse, the Subtle Brush** — Legendary Creature — Vampire Wizard

> Whenever you or a permanent you control becomes the target of a spell or ability an opponent controls, counter that spell or ability unless that player pays 4 life.  
> Whenever you copy a spell, up to one target opponent may also copy that spell. They may choose new targets for that copy.

## Plan and commander role

- **Primary plan:** Spellslinger copy: cast efficient instants and sorceries, copy them, and use Parnesse to hand selected opponents optional copies as political leverage. Her first ability taxes opposing targeting by 4 life. *strategic_judgment · high*
- **Secondary:** Commander-free copy infinites: Narset's Reversal or Reiterate/Reverberate/Increasing Vengeance/Return the Favor with a ritual/copy-mana engine (Alania, Pyromancer's Goggles, Prismari, Thousand-Year Storm, Storm-Kiln Artist, Mana Geyser, Jeska's Will).
  - Evidence: [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) · [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) · [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md)
- **Commander role: supporting.** Parnesse protects herself and your permanents with a 4-life targeting tax, and her copy-sharing is a political tool. *strategic_judgment · high*
- ⚠️ **Honest note:** None of the 25 Spellbook infinites in the list uses Parnesse; all are copy-spell pairs that work in any Grixis spellslinger deck. Her second ability gives opponents copies, which is optional politics and can be a liability. The source frames the deck as political conversion (blueprint L12), but mechanically she's a five-mana protection/politics commander on top of a strong generic copy-combo shell. The calibration floor is 3, below the source's 4; the 25 two-card infinites support 4. No M1 interaction review exists yet for this deck.
  - Evidence: [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) · `spellbook:11-3368` · `spellbook:3368-5959`
- **Dependency level:** low *strategic_judgment · high* — `spellbook:11-3368`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L8](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: 25 commander-free two- and three-card copy infinites support B4 despite the calibration floor of 3. Agrees with the source.) | *strategic_judgment · high* | [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) · `spellbook:11-3368` |
| Expected bracket (list as built) | 4 (computed floor 3) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Parnesse__the_Subtle_Brush` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 9, "2": 142, "3": 78, "4": 23}, "decks_with_bracket": 252, "share_b4_plus": 0.091, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__parnesse-the-subtle-brush.json`

## Win conditions

- **narset-reversal-loops** (combo): Narset's Reversal with Twinning Staff, Reiterate, Increasing Vengeance, Reverberate or Return the Favor; or with Primal Wellspring + Frantic Search, or Storm-Kiln Artist + Bonus Round/Thousand-Year Storm. Cards: Narset's Reversal, Twinning Staff, Reiterate, Increasing Vengeance, Reverberate, Return the Favor, Primal Amulet // Primal Wellspring, Frantic Search, Storm-Kiln Artist, Bonus Round, Thousand-Year Storm. *fact · verified* — `spellbook:11-2539` · `spellbook:11-3368` · `spellbook:11-4285` · `spellbook:11-5026` · `spellbook:11-5940` · `spellbook:11-1484-2196` · `spellbook:11-2492-5195` · `spellbook:11-3584-5195`
- **copy-mana-loops** (combo): Reiterate/Increasing Vengeance/Reverberate/Return the Favor with Alania, Pyromancer's Goggles, Prismari, Thousand-Year Storm, Mana Geyser or Jeska's Will: infinite mana/storm, finished with Grapeshot. Cards: Reiterate, Increasing Vengeance, Reverberate, Return the Favor, Alania, Divergent Storm, Pyromancer's Goggles, Prismari, the Inspiration, Thousand-Year Storm, Mana Geyser, Jeska's Will, Grapeshot. *fact · verified* — `spellbook:1878-3368` · `spellbook:2091-3368` · `spellbook:3368-3584` · `spellbook:3368-5959` · `spellbook:3368-6790` · `spellbook:3368-7683` · `spellbook:4285-5959` · `spellbook:4285-6790` · `spellbook:4285-7683` · `spellbook:5026-5959` · `spellbook:5026-6790` · `spellbook:5026-7683` · `spellbook:5940-5959` · `spellbook:5940-6790` · `spellbook:5940-7683` · `spellbook:1484-2196-3368`
- **dualcaster-tech** (combo): Dualcaster Mage + Replication Technique: infinite hasty tokens. Cards: Dualcaster Mage, Replication Technique. *fact · verified* — `spellbook:147-1883`

## Engines

- **copy-politics:** Parnesse, the Subtle Brush, Harmonic Prodigy, Veyran, Voice of Duality, Wizard's Staff. Online when: You copy a spell on the stack. *fact · high* — `oracle:Parnesse, the Subtle Brush` · [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) · [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md)
- **cast-copy-payoffs:** Archmage Emeritus, Storm-Kiln Artist, Sedgemoor Witch, Ral, Storm Conduit, Professor Onyx, Grapeshot, Goblin Electromancer. Online when: High spell volume. *strategic_judgment · high* — [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:spell-copy` | yes | 10 | Actual spell copies, each triggering Parnesse. | 17: Reverberate, Galvanic Iteration, Increasing Vengeance, Reiterate, Double Vision, Pyromancer's Goggles, Primal Amulet // Primal Wellspring, Twinning Staff, Zevlor, Elturel Exile, Thunderclap Drake, Bonus Round, Narset's Reversal, Return the Favor, Tempt with Mayhem, Replication Technique, Dualcaster Mage, Sunken Palace | — | *strategic_judgment · high* | [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) |
| `pkg:trigger-multipliers` | optional | 2 | Multiply Parnesse's triggers. | 3: Harmonic Prodigy, Veyran, Voice of Duality, Wizard's Staff | — | *strategic_judgment · high* | [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) |
| `pkg:cantrips-rituals` | yes | 6 | Spell volume and mana. | 9: Brainstorm, Ponder, Preordain, Frantic Search, Dark Ritual, Big Score, Windfall, Mana Geyser, Jeska's Will | — | *strategic_judgment · high* | [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L55](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) |

## Key interactions

- **copy-not-cast-copy:** Parnesse only triggers on copying a spell. Arcane Bombardment/Mizzix's Mastery copy cards in other zones and cast them, a different event. (Parnesse, the Subtle Brush, Mizzix's Mastery) *fact · high* — `oracle:Parnesse, the Subtle Brush` · [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) · `cr:707.10`
- **opponent-copy:** Opponents' copies may choose new targets; pick a recipient whose copy helps you or is harmless. (Parnesse, the Subtle Brush) *fact · high* — `oracle:Parnesse, the Subtle Brush` · `cr:707.10c`
- **targeting-tax:** Opposing spells and abilities that target you or your permanents are countered unless they pay 4 life. (Parnesse, the Subtle Brush) *fact · high* — `oracle:Parnesse, the Subtle Brush`
- **tempt-copies:** Tempt with Mayhem copies an instant or sorcery at least once under your control, plus more if opponents accept. (Tempt with Mayhem, Parnesse, the Subtle Brush) *fact · high* — [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md)

## Tutors and recursion

- Tutor target **Narset's Reversal** via Demonic Tutor *strategic_judgment · high* — `spellbook:11-3368`
- Tutor target **Reiterate** via Demonic Tutor *strategic_judgment · moderate* — `spellbook:3368-5959`
- Recursion: Mizzix's Mastery, Jeska's Will, Sedgemoor Witch *strategic_judgment · moderate* — [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md)

## Requirements

- **Interaction:** Counterspell, Mana Drain, Narset's Reversal, An Offer You Can't Refuse, Chaos Warp, Feed the Swarm, Blasphemous Act.
- **Protection:** Parnesse's tax, Deflecting Swat.
- **Mana:** 35 lands, nine fetches, Sol Ring, Dark Ritual, Signets/Talismans.
- *strategic_judgment · moderate* — [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) · [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L55](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md)

## Failure modes

- **gifted-copies:** Opponents' copies can backfire, e.g. a copied tutor or wipe. Mitigations: Choose copy recipients carefully; 'up to one' lets you give none. *strategic_judgment · high* — `oracle:Parnesse, the Subtle Brush`
- **expensive-engines:** Five-mana commander plus five- to seven-mana copy engines. Mitigations: Rituals and cantrips. *strategic_judgment · moderate* — [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L55](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md)
- **stack-interaction:** Counters on the key copy spell break the combos. Mitigations: Redundant copy pairs. *strategic_judgment · moderate* — [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md)

## Identity core

- **Parnesse, the Subtle Brush:** Targeting tax and copy politics. *fact · verified* — `oracle:Parnesse, the Subtle Brush`
- **Narset's Reversal:** Hub of the copy infinites. *strategic_judgment · high* — `spellbook:11-3368`
- **Reiterate:** Buyback copy for mana loops. *strategic_judgment · high* — `spellbook:3368-5959`
- **Tempt with Mayhem:** Copy spell with political upside. *strategic_judgment · high* — [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md)
- **Veyran, Voice of Duality:** Doubles Parnesse's triggers. *strategic_judgment · high* — [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No Oracle/Consultation or Breach cEDH shell (blueprint L53).
- ✗ Don't overfill two-mana copy spells (L54).
  - *strategic_judgment · high* — [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) · [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md)
- Theme: Spell copy / politics / spellslinger (blueprint L10).
  - *strategic_judgment · high* — [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md#L10](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 707.10:** Copying a spell. *fact · verified* — `cr:707.10`
- **CR 707.10c:** New targets for copies. *fact · verified* — `cr:707.10c`

## Supporting features (heuristic, not identity)

- `{"hooks": ["copying"], "hooked_cards": 31, "role_counts": {"counter": 3, "draw": 9, "protection": 2, "ramp": 17, "removal": 4, "tutor": 1, "wipe": 1}, "lands": 35, "edhrec_pages": ["parnesse-the-subtle-brush"]}` *heuristic · low*

## Provenance

- Seeded from: [Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Parnesse_the_Subtle_Brush_Commander_Blueprint_2026-10-15.md) · [Parnesse_the_Subtle_Brush_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Parnesse_the_Subtle_Brush_Candidate_Decisions_2026-10-15.md) · [Parnesse_the_Subtle_Brush_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Parnesse_the_Subtle_Brush_Approved_2026-10-15.md) · [Parnesse_the_Subtle_Brush_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Parnesse_the_Subtle_Brush_Approval_Ready_Verification_2026-10-15.md) · [Parnesse_the_Subtle_Brush_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Parnesse_the_Subtle_Brush_Whole_List_Audit_2026-10-15.md) · [Parnesse_the_Subtle_Brush_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Parnesse_the_Subtle_Brush_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
