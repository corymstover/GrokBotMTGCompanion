# Blueprint — Sol'Kanar the Tainted

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/solkanar-the-tainted.md), state `SOURCE_BASELINE`, list `lh1:3dac16383746b8fa…`). Machine-readable source: [`data/grixis/blueprints/solkanar-the-tainted.json`](../../data/grixis/blueprints/solkanar-the-tainted.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Sol'Kanar the Tainted** — Legendary Creature — Elemental Demon

> At the beginning of your end step, choose one that hasn't been chosen —  
> • Draw a card.  
> • Each opponent loses 2 life and you gain 2 life.  
> • Sol'Kanar deals 3 damage to up to one other target creature or planeswalker.  
> • Exile Sol'Kanar, then return it to the battlefield under an opponent's control.

## Plan and commander role

- **Primary plan:** Political control with cursed gifts: take value from Demonic Pact, Greed's Gambit or Illusions of Grandeur, then give the liability to an opponent with Donate-style effects; Demonic Pact + a donate effect is the compact kill. *strategic_judgment · high*
- **Secondary:** Recycle Sol'Kanar's once-per-object end-step modes (draw, drain 2, 3 damage, give him away) by blinking him with Thassa, Conjurer's Closet or Planar Incision; Homeward Path and Coveted Falcon recover ownership.
  - Evidence: [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md)
- **Commander role: significant.** Sol'Kanar is repeatable end-step value, and his fourth mode is a political gift. *strategic_judgment · high*
- ⚠️ **Honest note:** Honest call: significant, not central. All four Spellbook combos (Demonic Pact + Donate / Harmless Offering / Blim / Coveted Falcon) work without him. He adds value through blink resets but the kills are the cursed-gift package. The source calls the plan slower and more board-dependent than cEDH (blueprint L22).
  - Evidence: [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) · `spellbook:2770-6676`
- **Dependency level:** medium *strategic_judgment · high* — `spellbook:2770-6676`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: compact two-card Pact kills and premium interaction, but a slower political shell. Agrees with the source.) | *strategic_judgment · high* | [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) · `spellbook:2770-6676` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Sol_kanar_the_Tainted` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 5, "2": 101, "3": 21, "4": 2}, "decks_with_bracket": 129, "share_b4_plus": 0.016, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__solkanar-the-tainted.json`

## Win conditions

- **pact-donate** (combo): After safe Demonic Pact modes, transfer it; the recipient loses on the lose-the-game mode. Cards: Demonic Pact, Donate, Harmless Offering, Blim, Comedic Genius, Coveted Falcon. Enablers: Demonic Tutor, Vampiric Tutor. *strategic_judgment · high* — `spellbook:2770-6676` · `spellbook:3090-6676` · `spellbook:3769-6676` · `spellbook:6676-6922` · [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md)
- **coil-bog** (combo): Give Immortal Coil away, then empty that player's graveyard with Bojuka Bog or Rakdos Charm. Cards: Immortal Coil, Bojuka Bog, Rakdos Charm. Enablers: Donate, Harmless Offering, Bazaar Trader. *strategic_judgment · high* — [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md) · [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md)
- **audience-and-drain** (alternate): Captive Audience enters under an opponent's control; Sol'Kanar drains and Goblin Bombardment finishes. Cards: Captive Audience, Sol'Kanar the Tainted, Goblin Bombardment. *strategic_judgment · moderate* — [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md) · [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L38](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md)

## Engines

- **mode-reset:** Sol'Kanar the Tainted, Thassa, Deep-Dwelling, Conjurer's Closet, Planar Incision. Online when: Sol'Kanar plus a blink effect. *fact · high* — `oracle:Sol'Kanar the Tainted` · [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md) · `cr:400.7`
- **cursed-gift:** Donate, Harmless Offering, Bazaar Trader, Blim, Comedic Genius, Coveted Falcon, Role Reversal, Shifting Grift, Puca's Mischief, Fateful Handoff, Sudden Substitution, Demonic Pact, Archfiend of the Dross, Greed's Gambit, Illusions of Grandeur, Plague Reaver, Immortal Coil, Captive Audience. Online when: A liability permanent plus a transfer effect. *strategic_judgment · high* — [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:transfer` | yes | 7 | Control-transfer effects. | 10: Donate, Harmless Offering, Bazaar Trader, Blim, Comedic Genius, Coveted Falcon, Role Reversal, Shifting Grift, Puca's Mischief, Fateful Handoff, Sudden Substitution | — | *strategic_judgment · high* | [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) |
| `pkg:curses` | yes | 5 | Giftable liabilities. | 7: Demonic Pact, Archfiend of the Dross, Greed's Gambit, Illusions of Grandeur, Plague Reaver, Immortal Coil, Captive Audience | — | *strategic_judgment · high* | [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md) · [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md) |
| `pkg:reset` | yes | 3 | Reset Sol'Kanar's modes. | 3: Thassa, Deep-Dwelling, Conjurer's Closet, Planar Incision | — | *strategic_judgment · high* | [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md) |
| `pkg:ownership` | optional | 2 | Recover owned permanents. | 3: Homeward Path, Coveted Falcon, Planar Incision | — | *strategic_judgment · moderate* | [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) |

## Key interactions

- **object-modes:** Mode history belongs to the battlefield object; blinking creates a new object and resets it. (Sol'Kanar the Tainted) *fact · high* — `oracle:Sol'Kanar the Tainted` · [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md) · `cr:400.7`
- **stack-before-blink:** Order Thassa/Closet with the end-step trigger so a mode resolves before the reset. (Thassa, Deep-Dwelling, Conjurer's Closet, Sol'Kanar the Tainted) *fact · high* — [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md) · `cr:603.3b`
- **incision-owner:** Planar Incision returns Sol'Kanar under its owner's control. (Planar Incision, Sol'Kanar the Tainted) *fact · high* — [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md)
- **pact-modes-follow:** Demonic Pact's chosen modes stay with the permanent through control changes. (Demonic Pact) *fact · high* — [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md)
- **coil-controller:** Immortal Coil's empty-graveyard loss applies to its current controller. (Immortal Coil) *fact · high* — [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md)
- **no-greaves:** Lightning Greaves was cut because shroud blocks the blink targets. (Deflecting Swat) *fact · high* — [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md)

## Tutors and recursion

- Tutor target **Demonic Pact** via Demonic Tutor, Vampiric Tutor *strategic_judgment · high* — `spellbook:2770-6676`
- Recursion: — *strategic_judgment · moderate* — [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Fierce Guardianship, Mana Drain, Swan Song, Withering Torment, Deadly Rollick, Chaos Warp, Toxic Deluge, Blasphemous Act, Cyclonic Rift, Vandalblast.
- **Protection:** Deflecting Swat.
- **Mana:** 35 lands including Forbidden Orchard and Homeward Path; Sol Ring, Mana Vault, Signets, Talismans.
- *strategic_judgment · moderate* — [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md)

## Failure modes

- **slow-board:** Sequence-dependent; fast combo outpaces it. Mitigations: Force of Will; Fierce Guardianship. *strategic_judgment · high* — [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md)
- **pact-removed:** Opponents remove a gifted Demonic Pact or Coil before it kills. Mitigations: Redundant curses; Tutors. *strategic_judgment · high* — [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md)
- **mode-four-loss:** Mode four gives Sol'Kanar away. Mitigations: Homeward Path; Planar Incision; Coveted Falcon. *strategic_judgment · moderate* — `oracle:Sol'Kanar the Tainted`

## Identity core

- **Sol'Kanar the Tainted:** Four once-per-object end-step modes. *fact · verified* — `oracle:Sol'Kanar the Tainted`
- **Demonic Pact:** Main cursed gift. *strategic_judgment · high* — `spellbook:2770-6676`
- **Harmless Offering:** Transfers the Pact. *strategic_judgment · high* — `spellbook:3090-6676`
- **Thassa, Deep-Dwelling:** Resets Sol'Kanar every end step. *strategic_judgment · high* — [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md)
- **Immortal Coil:** Second giftable kill. *strategic_judgment · high* — [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No generic Thoracle/Breach (decisions L54).
- ✗ No Alicia Masters: her reset would undo intentional gifts (L47).
  - *strategic_judgment · high* — [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md) · [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md#L47](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md)
- Theme: Donate / blink / giftable curses (blueprint L35).
  - *strategic_judgment · high* — [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 400.7:** A new object after a zone change. *fact · verified* — `cr:400.7`
- **CR 603.3b:** Ordering triggers. *fact · verified* — `cr:603.3b`
- **CR 700.2:** Modal choices. *fact · verified* — `cr:700.2`

## Supporting features (heuristic, not identity)

- `{"hooks": ["life gain", "opponents losing life"], "hooked_cards": 12, "role_counts": {"counter": 5, "draw": 13, "protection": 1, "ramp": 12, "removal": 12, "tutor": 2, "wipe": 4}, "lands": 35, "edhrec_pages": ["solkanar-the-tainted"]}` *heuristic · low*

## Provenance

- Seeded from: [Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Tainted_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Tainted_Candidate_Decisions_2026-10-15.md) · [Solkanar_the_Tainted_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Solkanar_the_Tainted_Approved_2026-10-15.md) · [Solkanar_the_Tainted_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Solkanar_the_Tainted_Approval_Ready_Verification_2026-10-15.md) · [Solkanar_the_Tainted_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Solkanar_the_Tainted_Whole_List_Audit_2026-10-15.md) · [Solkanar_the_Tainted_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Solkanar_the_Tainted_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
