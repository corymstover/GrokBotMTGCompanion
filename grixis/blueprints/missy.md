# Blueprint — Missy

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/missy.md), state `SOURCE_BASELINE`, list `lh1:f8f18bbca5711b52…`). Machine-readable source: [`data/grixis/blueprints/missy.json`](../../data/grixis/blueprints/missy.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Missy** — Legendary Creature — Time Lord Rogue

> Whenever another nonartifact creature dies, return it to the battlefield under your control face down and tapped. It's a 2/2 Cyberman artifact creature.  
> At the beginning of your end step, each opponent faces a villainous choice — Each artifact creature you control deals 1 damage to that opponent, or you draw a card and chaos ensues.

## Plan and commander role

- **Primary plan:** Nonartifact death → Missy returns it face down as a 2/2 Cyberman artifact → turn it face up → the printed nonartifact creature can die again. Free sacrifice outlets plus zero-cost-reveal morphs make this a commander-native infinite. *strategic_judgment · high*
- **Secondary:** Steal opponents' dead nonartifact creatures through edicts and nonartifact sweepers, build a Cyberman army for the villainous-choice end step, and drain with aristocrats.
  - Evidence: [Missy_Commander_Blueprint_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) · [Missy_Commander_Blueprint_2026-10-15.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md)
- **Commander role: central.** Missy is the recursion engine and a piece in every one of the 17 Spellbook infinites in the list. *strategic_judgment · high*
- ⚠️ **Honest note:** This is genuinely commander-native: Missy + free outlet + Ruthless Ripper/Dragon's Eye Savants/Horde Ambusher is three cards, two of them tutorable. The cost is a six-mana commander, which the source names as the main reason for Bracket 4 (blueprint L42). No M1 interaction review exists yet for this deck.
  - Evidence: [Missy_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) · [Missy_Commander_Blueprint_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) · `spellbook:1794-2292-4424`
- **Dependency level:** high *strategic_judgment · high* — `spellbook:1794-2292-4424`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Missy_Commander_Blueprint_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: commander-native three-card loops with tutors, held back by a six-mana commander. Agrees with the source.) | *strategic_judgment · high* | [Missy_Commander_Blueprint_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) · `spellbook:1794-2292-4424` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Missy` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 12, "2": 305, "3": 191, "4": 39, "5": 10}, "decks_with_bracket": 557, "share_b4_plus": 0.088, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__missy.json`

## Win conditions

- **missy-morph-loop** (combo): Missy + a free sacrifice outlet + Ruthless Ripper, Dragon's Eye Savants or Horde Ambusher (reveal-a-card morph costs): unbounded deaths, damage via Bombardment or drain, mill via Altar of Dementia. Cards: Missy, Ruthless Ripper, Dragon's Eye Savants, Horde Ambusher, Ashnod's Altar, Viscera Seer, Phyrexian Altar, Goblin Bombardment, Altar of Dementia. Enablers: Blood Artist, Zulaport Cutthroat, Mayhem Devil. *fact · verified* — `spellbook:1794-2034-4424` · `spellbook:1794-2292-4424` · `spellbook:1794-4050-4424` · `spellbook:1794-4424-5147` · `spellbook:1794-4424-5256` · `spellbook:2034-3565-4424` · `spellbook:2292-3565-4424` · `spellbook:3565-4050-4424` · `spellbook:3565-4424-5147` · `spellbook:3565-4424-5256` · `spellbook:1045-2034-4424` · `spellbook:1045-2292-4424` · `spellbook:1045-4050-4424` · `spellbook:1045-4424-5147` · `spellbook:1045-4424-5256`
- **haruspex-ixidor** (combo): Missy + Phyrexian Altar + Grim Haruspex; Missy + Ixidor + Pitiless Plunderer + Ashnod's Altar. Cards: Missy, Phyrexian Altar, Grim Haruspex, Ixidor, Reality Sculptor, Pitiless Plunderer, Ashnod's Altar. *fact · verified* — `spellbook:631-4050-4424` · `spellbook:419-2034-4424-4871`
- **villainous-choice** (natural): End-step villainous choice: each artifact creature deals 1 damage, scaled by Cybermen and The Valeyard. Cards: Missy, The Valeyard. Enablers: Cyberman Patrol, Cybermen Squadron, Ashad, the Lone Cyberman, The Cyber-Controller. *fact · high* — `oracle:Missy` · [Missy_Commander_Blueprint_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md)

## Engines

- **cyberman-conversion:** Missy, Grave Pact, Plaguecrafter, Feed the Swarm, Toxic Deluge, Their Name Is Death, Death in Heaven. Online when: Missy in play while nonartifact creatures die. *fact · high* — `oracle:Missy` · [Missy_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) · [Missy_Commander_Blueprint_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md)
- **aristocrats:** Blood Artist, Zulaport Cutthroat, Mayhem Devil, Reckless Fireweaver, Pitiless Plunderer, Grim Haruspex. Online when: Sacrifice outlet available. *strategic_judgment · high* — [Missy_Commander_Blueprint_2026-10-15.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:zero-cost-morphs` | yes | 3 | Reveal-cost morphs that turn the loop on. | 3: Ruthless Ripper, Dragon's Eye Savants, Horde Ambusher | — | *strategic_judgment · high* | [Missy_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) |
| `pkg:morph-utility` | optional | 4 | Hidden interaction that Missy later recycles. | 8: Willbender, Boltbender, Stratus Dancer, Kadena's Silencer, Bane of the Living, Pyrotechnic Performer, Aphetto Runecaster, Ixidor, Reality Sculptor | — | *strategic_judgment · high* | [Missy_Commander_Blueprint_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) |
| `pkg:free-outlets` | yes | 4 | Free sacrifice outlets. | 6: Ashnod's Altar, Viscera Seer, Phyrexian Altar, Goblin Bombardment, Altar of Dementia, Phyrexian Tower | — | *strategic_judgment · high* | [Missy_Commander_Blueprint_2026-10-15.md#L61](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) |
| `pkg:cybermen` | optional | 3 | Cyberman artifact creatures for villainous-choice damage. | 4: Ashad, the Lone Cyberman, Cyberman Patrol, Cybermen Squadron, The Cyber-Controller | — | *strategic_judgment · moderate* | [Missy_Commander_Blueprint_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) |

## Key interactions

- **face-down-colorless:** A Missy-returned card is a colorless face-down 2/2 Cyberman artifact creature; if it has morph, it can be turned face up for its morph cost. (Missy) *fact · high* — `oracle:Missy` · [Missy_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) · `cr:708.2`
- **turn-up-reset:** Turning the card face up restores its printed nonartifact characteristics, so its next death triggers Missy again. (Missy, Ruthless Ripper, Dragon's Eye Savants, Horde Ambusher) *fact · high* — `cr:702.37e` · `cr:708.8`
- **opponent-creatures:** Missy returns any nonartifact creature, including opponents', under your control. (Missy) *fact · high* — `oracle:Missy` · [Missy_Commander_Blueprint_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md)
- **villainous-choice-rules:** Each opponent picks an option; they may choose one that does nothing. (Missy) *fact · high* — `cr:701.55a` · `cr:701.55b`

## Tutors and recursion

- Tutor target **Ruthless Ripper** via Demonic Tutor, Vampiric Tutor, Diabolic Intent *strategic_judgment · high* — `spellbook:1794-2292-4424`
- Tutor target **Goblin Bombardment** via Demonic Tutor *strategic_judgment · moderate* — `spellbook:1794-4424-5147`
- Recursion: Missy *strategic_judgment · moderate* — [Missy_Commander_Blueprint_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md)

## Requirements

- **Interaction:** Terminate, Delete, An Offer You Can't Refuse, Chaos Warp, Cyclonic Rift, Toxic Deluge, Swan Song.
- **Protection:** Lightning Greaves, Willbender, Boltbender.
- **Mana:** 35 lands, Sol Ring, Mana Vault, Ancient Tomb, Talismans.
- *strategic_judgment · moderate* — [Missy_Commander_Blueprint_2026-10-15.md#L58](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) · [Missy_Commander_Blueprint_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md)

## Failure modes

- **six-mana-commander:** Missy costs six; losing her twice is very expensive. Mitigations: Fast mana; Lightning Greaves. *strategic_judgment · high* — [Missy_Commander_Blueprint_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md)
- **graveyard-exile:** Exile-on-death effects (Rest in Peace, Leyline) stop the loop. Mitigations: Removal. *strategic_judgment · high* — `oracle:Missy`
- **nonartifact-only:** Artifact creatures don't return; Cybermen and Missy's own returns can't loop until turned face up. Mitigations: Morph density. *strategic_judgment · moderate* — `oracle:Missy`

## Identity core

- **Missy:** The loop engine. *fact · verified* — `oracle:Missy`
- **Ruthless Ripper:** Free reveal-cost morph. *strategic_judgment · high* — `spellbook:1794-2292-4424`
- **Dragon's Eye Savants:** Second free morph (reveal a blue card). *strategic_judgment · high* — `spellbook:2292-3565-4424`
- **Horde Ambusher:** Third free morph (reveal a red card); its face-up trigger also stops blockers. *strategic_judgment · high* — `spellbook:1045-2292-4424`
- **Goblin Bombardment:** Outlet that is also the kill. *strategic_judgment · high* — `spellbook:1794-4424-5147`

## Anti-goals and thematic constraints

- ✗ Not generic Grixis artifacts/aristocrats/theft/morph (blueprint L46).
- ✗ Cut self-disabling or Dalek-specific high-cost cards (blueprint L63).
  - *strategic_judgment · high* — [Missy_Commander_Blueprint_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) · [Missy_Commander_Blueprint_2026-10-15.md#L63](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md)
- Theme: Doctor Who Cybermen conversion; the Master and Valeyard support.
  - *strategic_judgment · moderate* — [Missy_Commander_Blueprint_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 708.2:** Face-down characteristics. *fact · verified* — `cr:708.2`
- **CR 702.37e:** Turning a morph face up. *fact · verified* — `cr:702.37e`
- **CR 701.55a:** Villainous choice. *fact · verified* — `cr:701.55a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Cyberman synergy", "artifacts", "graveyard as a resource", "villainous choices / voting"], "hooked_cards": 30, "role_counts": {"counter": 4, "draw": 7, "protection": 1, "ramp": 10, "removal": 6, "tutor": 3, "wipe": 3}, "lands": 35, "edhrec_pages": ["missy"]}` *heuristic · low*

## Provenance

- Seeded from: [Missy_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Missy_Commander_Blueprint_2026-10-15.md) · [Missy_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Missy_Candidate_Decisions_2026-10-15.md) · [Missy_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Missy_Approved_2026-10-15.md) · [Missy_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Missy_Approval_Ready_Verification_2026-10-15.md) · [Missy_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Missy_Whole_List_Audit_2026-10-15.md) · [Missy_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Missy_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
