# Blueprint — Zevlor, Elturel Exile

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/zevlor-elturel-exile.md), state `SOURCE_BASELINE`, list `lh1:f4342af184fe4a9e…`). Machine-readable source: [`data/grixis/blueprints/zevlor-elturel-exile.json`](../../data/grixis/blueprints/zevlor-elturel-exile.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Zevlor, Elturel Exile** — Legendary Creature — Tiefling Warrior

> Haste  
> {2}, {T}: When you next cast an instant or sorcery spell that targets only a single opponent or a single permanent an opponent controls this turn, for each other opponent, choose that player or a permanent they control, copy that spell, and the copy targets the chosen player or permanent.

## Plan and commander role

- **Primary plan:** Target-copy payloads: activate Zevlor ({2}, {T}), then cast an instant or sorcery that targets one opponent or their permanent, and it's copied for each other opponent. The deck runs single-target theft, draw and control spells (Cruel Ultimatum, Praetor's Grasp, Bribery, Acquire, River's Rebuke, Leadership Vacuum) that become table-wide. *strategic_judgment · high*
- **Secondary:** Activation support (Training Grounds, Omen Hawker, Illusionist's Bracers, Pemmin's Aura, Patriar's Seal, Minamo, Twinning Staff) and magecraft engines that trigger on copies (Sedgemoor Witch, Storm-Kiln Artist).
  - Evidence: [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)
- **Commander role: central.** Zevlor turns every single-target spell into one per opponent. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native. The only Spellbook combo (3525-3772, Omen Hawker + Pemmin's Aura) doesn't need Zevlor. The deck has no compact kill; it wins on multiplied value and theft. The source says a generic Oracle/Breach shell can hold Zevlor but its wins don't need him, so it was rejected (verification L23; decisions L120).
  - Evidence: [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md#L120](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md) · `spellbook:3525-3772`
- **Dependency level:** high *strategic_judgment · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (verification).) | *fact · verified* | [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: strong multiplied value with premium protection, but no compact kill. Agrees with the source.) | *strategic_judgment · high* | [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md#L121](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Zevlor__Elturel_Exile` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 27, "2": 464, "3": 357, "4": 95, "5": 15}, "decks_with_bracket": 958, "share_b4_plus": 0.115, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__zevlor-elturel-exile.json`

## Win conditions

- **multiplied-payloads** (natural): Copied Cruel Ultimatum, Praetor's Grasp, Bribery and Acquire strip and steal from every opponent. Cards: Zevlor, Elturel Exile, Cruel Ultimatum, Praetor's Grasp, Acquire, Bribery, River's Rebuke, Leadership Vacuum. Enablers: Training Grounds, Omen Hawker, Illusionist's Bracers, Pemmin's Aura. *strategic_judgment · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md)
- **magecraft-tokens** (natural): Sedgemoor Witch and Storm-Kiln Artist trigger on each copy. Cards: Sedgemoor Witch, Storm-Kiln Artist. Enablers: Zevlor, Elturel Exile. *strategic_judgment · moderate* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)
- **hawker-pemmin** (combo): Omen Hawker + Pemmin's Aura gives infinite untaps and ability-only mana. Cards: Omen Hawker, Pemmin's Aura. *strategic_judgment · moderate* — `spellbook:3525-3772`

## Engines

- **single-target-copy:** Zevlor, Elturel Exile. Online when: {2}, {T}, then a spell with exactly one target that's an opponent or their permanent. *fact · high* — `oracle:Zevlor, Elturel Exile` · [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)
- **activation-support:** Training Grounds, Omen Hawker, Illusionist's Bracers, Pemmin's Aura, Patriar's Seal, Minamo, School at Water's Edge, Twinning Staff. Online when: Zevlor on the battlefield. *strategic_judgment · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L64](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L65](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L66](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L67](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L68](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:payloads` | yes | 12 | Single-target spells worth copying. | 16: Cruel Ultimatum, Praetor's Grasp, Acquire, Bribery, River's Rebuke, Leadership Vacuum, Peek, Portent, Pilfered Plans, Great Intelligence's Plan, Worst Fears, Rakdos's Return, Talent of the Telepath, Hell to Pay, Siphon Insight, Electrodominance | — | *strategic_judgment · high* | [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) |
| `pkg:activation` | yes | 5 | Pay, reduce, copy or repeat the activation. | 7: Training Grounds, Omen Hawker, Illusionist's Bracers, Pemmin's Aura, Patriar's Seal, Minamo, School at Water's Edge, Twinning Staff | — | *strategic_judgment · high* | [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) |
| `pkg:magecraft` | optional | 2 | Copy payoffs. | 3: Sedgemoor Witch, Storm-Kiln Artist, Archmage Emeritus | — | *strategic_judgment · moderate* | [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md) |

## Key interactions

- **only-one-target:** Zevlor's Oracle says 'targets only a single': spells with multiple chosen targets don't qualify. (Zevlor, Elturel Exile) *fact · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · `oracle:Zevlor, Elturel Exile`
- **copies-not-cast:** Copies aren't cast: cast triggers miss; 'cast or copy' magecraft works. (Sedgemoor Witch, Storm-Kiln Artist) *fact · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · `cr:707.10`
- **countered-original:** The delayed trigger copies the spell even if the original was countered. (Zevlor, Elturel Exile) *fact · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L61](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)
- **copy-keeps-choices:** Copies keep modes, X and paid additional costs. (Cruel Ultimatum) *fact · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L62](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)
- **multiple-delayed:** Several activations (or Bracers copies) all trigger on the same next spell. (Illusionist's Bracers, Zevlor, Elturel Exile) *fact · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L63](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L64](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)
- **twinning-staff:** Twinning Staff adds one copy per copy event, not recursively. (Twinning Staff) *fact · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L65](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)
- **boots-not-greaves:** Swiftfoot Boots instead of Greaves, because shroud blocks your own Minamo/Seal untaps. (Swiftfoot Boots, Minamo, School at Water's Edge, Patriar's Seal) *fact · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L69](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)

## Tutors and recursion

- Tutor target **Cruel Ultimatum** via Demonic Tutor, Mystical Tutor, Gamble *strategic_judgment · moderate* — [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md)
- Recursion: Snapcaster Mage, Kess, Dissident Mage, Jeska's Will *strategic_judgment · moderate* — [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Fierce Guardianship, Mana Drain, Counterspell, Swan Song, Deadly Rollick, Terminate, Chaos Warp, Feed the Swarm, Cyclonic Rift, Blasphemous Act.
- **Protection:** Swiftfoot Boots, Pemmin's Aura shroud, Deflecting Swat.
- **Mana:** 34 lands with fetches and true duals; Sol Ring, Mana Vault, Ancient Tomb.
- *strategic_judgment · moderate* — [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md#L112](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md) · [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md#L115](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md)

## Failure modes

- **no-compact-win:** No compact kill; combo tables outrace it. Mitigations: Counterspells; Theft. *strategic_judgment · high* — [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md#L120](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md)
- **sorcery-window:** Zevlor must activate then cast in the same turn; two pieces of mana each time. Mitigations: Training Grounds; Omen Hawker. *strategic_judgment · high* — `oracle:Zevlor, Elturel Exile`
- **target-rules:** Multi-target spells don't qualify. Mitigations: Card selection by exact Oracle. *strategic_judgment · moderate* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)

## Identity core

- **Zevlor, Elturel Exile:** Copies single-target spells for each opponent. *fact · verified* — `oracle:Zevlor, Elturel Exile`
- **Cruel Ultimatum:** Premier multiplied payload. *strategic_judgment · high* — [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md)
- **Illusionist's Bracers:** Copies the activation for free. *strategic_judgment · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L64](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)
- **Training Grounds:** Cuts the activation to {1}. *strategic_judgment · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L66](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)
- **Pemmin's Aura:** Repeat untaps and shroud. *strategic_judgment · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L68](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No Oracle/Consultation/Tainted Pact/Breach (decisions L120).
- ✗ No Thousand-Year Storm generic copying (L74).
  - *strategic_judgment · high* — [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md#L120](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md) · [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md#L74](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md)
- Theme: Targeted spells / spell copy / theft-control (verification L25).
  - *strategic_judgment · high* — [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 707.10:** Copying spells. *fact · verified* — `cr:707.10`
- **CR 707.10c:** New targets for copies. *fact · verified* — `cr:707.10c`
- **CR 603.7a:** Delayed triggers. *fact · verified* — `cr:603.7a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["copying", "instants and sorceries"], "hooked_cards": 56, "role_counts": {"counter": 5, "draw": 15, "protection": 3, "ramp": 11, "removal": 13, "tutor": 4, "wipe": 3}, "lands": 34, "edhrec_pages": ["zevlor-elturel-exile"]}` *heuristic · low*

## Provenance

- Seeded from: [Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Zevlor_Elturel_Exile_Candidate_Decisions_2026-10-15.md) · [Zevlor_Elturel_Exile_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Zevlor_Elturel_Exile_Approved_2026-10-15.md) · [Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Zevlor_Elturel_Exile_Approval_Ready_Verification_2026-10-15.md) · [Zevlor_Elturel_Exile_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Zevlor_Elturel_Exile_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
