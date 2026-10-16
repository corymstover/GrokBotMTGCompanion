# Blueprint — The Rani

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/the-rani.md), state `SOURCE_BASELINE`, list `lh1:f740437f9975b3bb…`). Machine-readable source: [`data/grixis/blueprints/the-rani.json`](../../data/grixis/blueprints/the-rani.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**The Rani** — Legendary Creature — Time Lord Scientist

> Whenever The Rani enters or attacks, create a red Aura enchantment token named Mark of the Rani attached to another target creature. That token has enchant creature and "Enchanted creature gets +2/+2 and is goaded."  
> Whenever a goaded creature deals combat damage to one of your opponents, investigate.

## Plan and commander role

- **Primary plan:** Forced combat into Clues: each Rani ETB or attack puts Mark of the Rani (+2/+2 and goaded) on a creature, goaded creatures hitting opponents investigate, and the goad Aura suite makes more goaded attackers. Academy Manufactor and Erdwal Illuminator multiply the Clues. *strategic_judgment · high*
- **Secondary:** Blink The Rani for more Marks (Thassa, Displacer Kitten), turn artifact tokens into mana, damage and extra turns (Urza, Bjorna, Time Sieve), and use mass goad (Disrupt Decorum, Kardur, Spectacular Showdown).
  - Evidence: [The_Rani_Candidate_Decisions_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- **Commander role: central.** The Rani makes the goad and is the main Clue trigger for opposing creatures' combat damage. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native forced combat. Spellbook finds no combos; Time Sieve is kept as a payoff, not a deterministic loop (decisions L48). Source note: the decisions file still says 'working decision closeout; not user approval' (L7), but the approval record (approvals L8) shows APPROVED / LOCKED on 2026-10-15; the approval record is the authority.
  - Evidence: [The_Rani_Candidate_Decisions_2026-10-15.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L7](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Approved_2026-10-15.md#L8](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/The_Rani_Approved_2026-10-15.md)
- **Dependency level:** high *strategic_judgment · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions).) | *fact · verified* | [The_Rani_Candidate_Decisions_2026-10-15.md#L71](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: tuned forced-combat value with premium protection, but no compact kill. Agrees with the source.) | *strategic_judgment · high* | [The_Rani_Approval_Ready_Verification_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Rani_Approval_Ready_Verification_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L63](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#The_Rani` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 15, "2": 344, "3": 212, "4": 21, "5": 9}, "decks_with_bracket": 601, "share_b4_plus": 0.05, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__the-rani.json`

## Win conditions

- **forced-combat** (natural): Goaded opponents attack each other while Clues build up; Kardur, Karazikar and Firkraag add pressure. Cards: The Rani, Ghoulish Impetus, Psychic Impetus, Shiny Impetus, Coercive Impetus, Incriminating Impetus, Eye of Nidhogg. Enablers: Disrupt Decorum, Kardur, Doomscourge. *strategic_judgment · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- **artifact-payoffs** (natural): Bjorna turns artifacts into damage; Time Sieve converts tokens into extra turns. Cards: Bjorna, Nightfall Alchemist, Time Sieve, Academy Manufactor. Enablers: Erdwal Illuminator. *strategic_judgment · moderate* — [The_Rani_Candidate_Decisions_2026-10-15.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)

## Engines

- **mark-and-investigate:** The Rani. Online when: The Rani enters or attacks; goaded creatures deal combat damage to opponents. *fact · high* — `oracle:The Rani` · [The_Rani_Candidate_Decisions_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- **token-multiplier:** Academy Manufactor, Erdwal Illuminator. Online when: Any investigate. *fact · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L47](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- **rani-blink:** Thassa, Deep-Dwelling, Displacer Kitten, The Rani. Online when: The Rani on the battlefield. *strategic_judgment · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:goad` | yes | 10 | Repeatable and mass goad. | 16: Ghoulish Impetus, Psychic Impetus, Shiny Impetus, Coercive Impetus, Incriminating Impetus, Eye of Nidhogg, Bloodthirsty Blade, The Master, Mesmerist, Baeloth Barrityl, Entertainer, Disrupt Decorum, Spectacular Showdown, Maestros Confluence, Kardur, Doomscourge, Karazikar, the Eye Tyrant, Firkraag, Cunning Instigator, Grenzo, Havoc Raiser | — | *strategic_judgment · high* | [The_Rani_Candidate_Decisions_2026-10-15.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) |
| `pkg:artifact-payoff` | yes | 6 | Turn Clues into value. | 10: Academy Manufactor, Erdwal Illuminator, Time Sieve, Bjorna, Nightfall Alchemist, Five Hundred Year Diary, Forensic Gadgeteer, Inspiring Statuary, Urza, Lord High Artificer, Tangletrove Kelp, Entity Tracker | — | *strategic_judgment · high* | [The_Rani_Candidate_Decisions_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) |

## Key interactions

- **manufactor-illuminator:** Manufactor + Illuminator: the first investigate each turn makes six artifact tokens. (Academy Manufactor, Erdwal Illuminator) *fact · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L47](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- **thassa-new-object:** Thassa returns The Rani as a new object, so her ETB makes another Mark. (Thassa, Deep-Dwelling, The Rani) *fact · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · `cr:400.7`
- **baeloth-mark:** A Mark on Baeloth makes him 4/7, so he goads more opposing creatures. (Baeloth Barrityl, Entertainer) *fact · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- **sieve-not-infinite:** Time Sieve is a payoff, not a deterministic infinite. (Time Sieve) *fact · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- **goad-investigate:** Goaded creatures must attack; damage to opponents investigates. (The Rani) *fact · high* — `cr:701.15a` · `cr:701.16a`

## Tutors and recursion

- Tutor target **Academy Manufactor** via Demonic Tutor, Vampiric Tutor, Mystical Tutor *strategic_judgment · moderate* — [The_Rani_Candidate_Decisions_2026-10-15.md#L47](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- Recursion: Reanimate *strategic_judgment · low* — [The_Rani_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Fierce Guardianship, Mana Drain, Swan Song, Deadly Rollick, Chaos Warp, Cyclonic Rift, Toxic Deluge, Blasphemous Act.
- **Protection:** Deflecting Swat, Lightning Greaves, Force of Will.
- **Mana:** 33 lands with City of Brass, Mana Confluence and fetches.
- *strategic_judgment · moderate* — [The_Rani_Candidate_Decisions_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)

## Failure modes

- **no-creatures:** Creature-light combo opponents give no goad targets. Mitigations: Counterspells; Own pressure. *strategic_judgment · high* — `oracle:The Rani`
- **no-compact-win:** No compact kill. Mitigations: Time Sieve; Bjorna. *strategic_judgment · moderate* — [The_Rani_Candidate_Decisions_2026-10-15.md#L63](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- **colored-mana:** Needs U/B/R; Mana Vault and Chrome Mox were rejected. Mitigations: Signets; Talismans. *strategic_judgment · moderate* — [The_Rani_Candidate_Decisions_2026-10-15.md#L62](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)

## Identity core

- **The Rani:** Mark of the Rani and goad-damage Clues. *fact · verified* — `oracle:The Rani`
- **Academy Manufactor:** Each Clue becomes three tokens. *strategic_judgment · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- **Erdwal Illuminator:** Extra investigate each turn. *strategic_judgment · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- **Thassa, Deep-Dwelling:** Repeat ETB Marks. *strategic_judgment · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- **The Master, Mesmerist:** Targeted goad with skulk. *strategic_judgment · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No generic Oracle/Breach (decisions L63).
- ✗ No Propaganda / No Mercy (L61).
  - *strategic_judgment · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L63](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Candidate_Decisions_2026-10-15.md#L61](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)
- Theme: Goad / Clues / forced combat (decisions L73).
  - *strategic_judgment · high* — [The_Rani_Candidate_Decisions_2026-10-15.md#L73](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.15a:** Goad. *fact · verified* — `cr:701.15a`
- **CR 701.16a:** Investigate. *fact · verified* — `cr:701.16a`
- **CR 400.7:** New object after blink. *fact · verified* — `cr:400.7`

## Supporting features (heuristic, not identity)

- `{"hooks": ["combat damage / attack triggers", "goad / forced attacks", "tokens"], "hooked_cards": 32, "role_counts": {"counter": 4, "draw": 12, "protection": 2, "ramp": 15, "removal": 5, "tutor": 3, "wipe": 3}, "lands": 33, "edhrec_pages": ["the-rani"]}` *heuristic · low*

## Provenance

- Seeded from: [The_Rani_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Rani_Candidate_Decisions_2026-10-15.md) · [The_Rani_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/The_Rani_Approved_2026-10-15.md) · [The_Rani_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Rani_Approval_Ready_Verification_2026-10-15.md) · [The_Rani_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Rani_Whole_List_Audit_2026-10-15.md) · [The_Rani_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/The_Rani_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
