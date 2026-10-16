# Blueprint — Sauron, the Dark Lord

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/sauron-the-dark-lord.md), state `SOURCE_BASELINE`, list `lh1:bbac35497c11953c…`). Machine-readable source: [`data/grixis/blueprints/sauron-the-dark-lord.json`](../../data/grixis/blueprints/sauron-the-dark-lord.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Sauron, the Dark Lord** — Legendary Creature — Avatar Horror

> Ward—Sacrifice a legendary artifact or legendary creature.  
> Whenever an opponent casts a spell, amass Orcs 1.  
> Whenever an Army you control deals combat damage to a player, the Ring tempts you.  
> Whenever the Ring tempts you, you may discard your hand. If you do, draw four cards.

## Plan and commander role

- **Primary plan:** Amass and the Ring: every opponent spell amasses Orcs 1, the Army's combat damage makes the Ring tempt you, and each temptation offers Sauron's discard-hand/draw-four and pumps every Nazgûl (7 copies). *strategic_judgment · high*
- **Secondary:** Army support (Great Goblin, Foul-Hearted; Mauhúr; The Great Goblin; Widespread Brutality), evasion (Minas Morgul, Rogue's Passage, The Black Gate, Orcish Siegemaster) and Roaming Throne to double Sauron or Nazgûl triggers.
  - Evidence: [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L39](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- **Commander role: central.** Sauron makes the Army, turns its hits into Ring temptations and card draw, and is protected by a legendary-sacrifice ward. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native, with no compact win: Spellbook finds no combos, and the source rejected Oracle/Breach conversion (decisions L34). The deck wins by Army/Nazgûl combat and card flow. There is no source blueprint file; the closeout and verification are the evidence. M1 review (saurondl-01..05, all verified) confirms the Army/Ring loop.
  - Evidence: [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- **Dependency level:** high *strategic_judgment · high* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions).) | *fact · verified* | [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: strong typal/Ring engine with premium staples, no compact combo. Agrees with the source.) | *strategic_judgment · high* | [Sauron_the_Dark_Lord_Approval_Ready_Verification_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Sauron_the_Dark_Lord_Approval_Ready_Verification_2026-10-15.md) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Sauron__the_Dark_Lord` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 79, "2": 2024, "3": 5123, "4": 1955, "5": 215}, "decks_with_bracket": 9396, "share_b4_plus": 0.231, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__sauron-the-dark-lord.json`

## Win conditions

- **army-nazgul-combat** (natural): A growing Orc Army plus seven Nazgûl that each get a counter whenever the Ring tempts you. Cards: Sauron, the Dark Lord, Nazgûl, Great Goblin, Foul-Hearted, Mauhúr, Uruk-hai Captain, Minas Morgul, Dark Fortress. Enablers: Roaming Throne, Call of the Ring. *strategic_judgment · high* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- **great-goblin-pings** (natural): The Great Goblin and Widespread Brutality turn counter events into damage. Cards: The Great Goblin, Widespread Brutality. Enablers: Sauron, the Dark Lord. *strategic_judgment · moderate* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)

## Engines

- **opponent-spell-amass:** Sauron, the Dark Lord. Online when: Opponents cast spells. *fact · high* — `oracle:Sauron, the Dark Lord` · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L39](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- **ring-draw:** Sauron, the Dark Lord, Call of the Ring, Nazgûl, Ringsight, Claim the Precious. Online when: Army connects or the Ring tempts you another way. *fact · high* — `oracle:Sauron, the Dark Lord` · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · `cr:701.54a`

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:nazgul` | yes | 3 | Wraiths that grow on each temptation (Nazgûl counts as one name with 7 copies). | 3: Nazgûl, Witch-king of Angmar, Minas Morgul, Dark Fortress | — | *strategic_judgment · high* | [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) |
| `pkg:army-support` | yes | 5 | Grow and arm the Army. | 7: Great Goblin, Foul-Hearted, Mauhúr, Uruk-hai Captain, The Great Goblin, Saruman, the White Hand, March from the Black Gate, Orcish Siegemaster, The Ozolith | — | *strategic_judgment · high* | [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) |
| `pkg:evasion` | yes | 4 | Army connection. | 5: Minas Morgul, Dark Fortress, Rogue's Passage, The Black Gate, Orcish Siegemaster, Wonder | — | *strategic_judgment · high* | [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) |

## Key interactions

- **ward-legendary:** Sauron's ward cost is sacrificing a legendary artifact or creature. (Sauron, the Dark Lord) *fact · high* — `oracle:Sauron, the Dark Lord` · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L38](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · `cr:702.21a`
- **amass-on-cast:** Each opponent spell triggers separately; countering it doesn't remove the trigger. (Sauron, the Dark Lord) *fact · verified* — [saurondl-01](../interactions/sauron-the-dark-lord.md#saurondl-01-saurons-loop-opponents-spells-feed-the-army-army-hits-tempt-the-ring-each-temptation-offers-discard-hand--draw-four) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L39](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- **mauhur-per-event:** Mauhúr adds one counter per event, not per counter. (Mauhúr, Uruk-hai Captain) *fact · verified* — [saurondl-05](../interactions/sauron-the-dark-lord.md#saurondl-05-army-counter-support-mauhúr-the-great-goblin-great-goblin-foul-hearted-widespread-brutality) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- **great-goblin-per-event:** The Great Goblin triggers once per counter event. (The Great Goblin) *fact · verified* — [saurondl-05](../interactions/sauron-the-dark-lord.md#saurondl-05-army-counter-support-mauhúr-the-great-goblin-great-goblin-foul-hearted-widespread-brutality) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- **throne-avatar-wraith:** Roaming Throne naming Avatar doubles Sauron's triggers; Wraith doubles each Nazgûl's. (Roaming Throne, Sauron, the Dark Lord, Nazgûl) *fact · verified* — [saurondl-04](../interactions/sauron-the-dark-lord.md#saurondl-04-roaming-throne-name-avatar-to-double-sauron-or-wraith-to-double-nazgûl-not-both) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- **seven-nazgul:** Seven Nazgûl are legal; each temptation is a counter wave plus a Sauron draw. (Nazgûl) *fact · verified* — [saurondl-02](../interactions/sauron-the-dark-lord.md#saurondl-02-seven-nazgûl-legal-and-every-temptation-is-a-counter-wave-plus-a-sauron-draw)
- **morgul-wraith-army:** Minas Morgul makes the Army a Wraith with shadow, and it stays an Army. (Minas Morgul, Dark Fortress) *fact · verified* — [saurondl-03](../interactions/sauron-the-dark-lord.md#saurondl-03-minas-morgul-turns-the-army-into-a-wraith-with-shadow-so-it-stays-an-army-for-sauron)

## Tutors and recursion

- Tutor target **Roaming Throne** via Demonic Tutor, Vampiric Tutor, Mystical Tutor *strategic_judgment · moderate* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- Recursion: Reanimate, Animate Dead, Victimize, Living Death, Summons of Saruman, Jeska's Will *strategic_judgment · moderate* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Mana Drain, Swan Song, Deadly Rollick, Feed the Swarm, Cyclonic Rift, Toxic Deluge, Blasphemous Act.
- **Protection:** Ward, Fierce Guardianship, Deflecting Swat.
- **Mana:** 34 lands, Sol Ring, Mana Vault, Talismans.
- *strategic_judgment · moderate* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)

## Failure modes

- **no-compact-win:** No compact kill; fast combo tables outrace it. Mitigations: Counterspells. *strategic_judgment · high* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- **quiet-opponents:** Opponents who cast few spells starve the amass engine. Mitigations: Nazgûl and other Army sources. *strategic_judgment · high* — `oracle:Sauron, the Dark Lord`
- **sweepers:** Sweepers reset the Army and Nazgûl. Mitigations: The Ozolith; Reanimation. *strategic_judgment · moderate* — `oracle:Sauron, the Dark Lord`

## Identity core

- **Sauron, the Dark Lord:** Amass on opponent spells; Ring temptations draw four. *fact · verified* — `oracle:Sauron, the Dark Lord`
- **Nazgûl:** Seven Wraiths that grow on each temptation. *strategic_judgment · high* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- **Great Goblin, Foul-Hearted:** Amass, repeat amass and Army trample. *strategic_judgment · high* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- **Minas Morgul, Dark Fortress:** Shadow for the Army and Wraith synergy. *strategic_judgment · high* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- **Roaming Throne:** Doubles Sauron or the Nazgûl. *strategic_judgment · high* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No generic Oracle/Breach/turbo conversion (decisions L34).
- ✗ No Chandra's Ignition / All Will Be One drift (L32).
  - *strategic_judgment · high* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)
- Theme: Amass Orcs / Ring temptation / Wraiths (decisions L60).
  - *strategic_judgment · high* — [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.54a:** The Ring tempts you. *fact · verified* — `cr:701.54a`
- **CR 701.47a:** Amass. *fact · verified* — `cr:701.47a`
- **CR 702.21a:** Ward. *fact · verified* — `cr:702.21a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Army synergy", "Orc synergy", "artifacts", "combat damage / attack triggers", "discard", "sacrifice"], "hooked_cards": 35, "role_counts": {"counter": 5, "draw": 11, "protection": 1, "ramp": 11, "removal": 5, "tutor": 5, "wipe": 2}, "lands": 34, "edhrec_pages": ["sauron-the-dark-lord"]}` *heuristic · low*

## Provenance

- Seeded from: [Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_the_Dark_Lord_Candidate_Decisions_2026-10-15.md) · [Sauron_the_Dark_Lord_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Sauron_the_Dark_Lord_Approved_2026-10-15.md) · [Sauron_the_Dark_Lord_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Sauron_the_Dark_Lord_Approval_Ready_Verification_2026-10-15.md) · [Sauron_the_Dark_Lord_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Sauron_the_Dark_Lord_Whole_List_Audit_2026-10-15.md) · [Sauron_the_Dark_Lord_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Sauron_the_Dark_Lord_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
