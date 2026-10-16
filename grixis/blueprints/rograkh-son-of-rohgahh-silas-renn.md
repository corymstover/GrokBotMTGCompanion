# Blueprint — Rograkh, Son of Rohgahh + Silas Renn, Seeker Adept

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/rograkh-son-of-rohgahh-silas-renn.md), state `SOURCE_BASELINE`, list `lh1:2f1326f4b41ecefd…`). Machine-readable source: [`data/grixis/blueprints/rograkh-son-of-rohgahh-silas-renn.json`](../../data/grixis/blueprints/rograkh-son-of-rohgahh-silas-renn.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Rograkh, Son of Rohgahh** — Legendary Creature — Kobold Warrior

> First strike, menace, trample  
> Partner (You can have two commanders if both have partner.)

**Silas Renn, Seeker Adept** — Legendary Artifact Creature — Human

> Deathtouch  
> Whenever Silas Renn deals combat damage to a player, choose target artifact card in your graveyard. You may cast that card this turn.  
> Partner (You can have two commanders if both have partner.)

## Plan and commander role

- **Primary plan:** RogSi turbo-naus: a zero-mana commander plus Moxen, rituals and zero-mana artifacts make early mana, then Ad Nauseam, Necropotence, Necrodominance or a wheel reloads the hand. Protection (Defense Grid, Hexing Squelcher, Samut, Vexing Bauble) pushes through a compact win. *strategic_judgment · high*
- **Secondary:** Final Fortune and Warrior's Oath turn an end-step reload or an unsafe window into an extra turn to finish. Mnemonic Betrayal and Yawgmoth's Will recover resources.
  - Evidence: [RogSi_Commander_Blueprint_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · [RogSi_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · [RogSi_Commander_Blueprint_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · [RogSi_Commander_Blueprint_2026-10-15.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md)
- **Commander role: significant.** Rograkh is a free creature on turn 0 that turns on Mox Amber, Springleaf Drum, Paradise Mantle, the free sacrifice tutors (Culling the Weak, Infernal Plunge, Diabolic Intent) and the commander-conditional free spells (Fierce Guardianship, Deflecting Swat, Deadly Rollick, Jeska's Will, Flare of Duplication). *strategic_judgment · high*
- ⚠️ **Honest note:** The pair is deliberately asymmetric (blueprint L11): Rograkh is a cost-free enabler, and Silas Renn is mostly color identity; the strongest games often never cast Silas (L14). None of the 7 Spellbook combos uses either commander; the wins are the generic cEDH Oracle and Breach lines. The commanders make those lines cheaper, not possible. M1 review (rogsi-01..08) verifies the partner and Silas rules and flags Vexing Bauble as a self-counter risk (rogsi-04).
  - Evidence: [RogSi_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · [RogSi_Commander_Blueprint_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · `spellbook:1295-3093`
- **Dependency level:** low *strategic_judgment · high* — `spellbook:1295-3093`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (Power Bracket 5 — cEDH (blueprint).) | *fact · verified* | [RogSi_Commander_Blueprint_2026-10-15.md#L9](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 5 (Bracket 5: the classic RogSi turbo-naus list, tournament-dominant (1,767 parsed lists). Agrees with the source.) | *strategic_judgment · high* | [RogSi_Commander_Blueprint_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · `spellbook:1295-3093` |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#RogSi` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 12, "2": 22, "3": 63, "4": 163, "5": 3378}, "decks_with_bracket": 3638, "share_b4_plus": 0.973, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__rograkh-son-of-rohgahh-silas-renn-seeker-adept.json`

## Win conditions

- **oracle** (combo): Thassa's Oracle + Demonic Consultation or Tainted Pact. Cards: Thassa's Oracle, Demonic Consultation, Tainted Pact. *fact · verified* — `spellbook:1295-3093` · `spellbook:742-1295`
- **breach** (combo): Underworld Breach + LED/Lotus Petal + Brain Freeze, + Wheel of Fortune (LED or Jeska's Will), or + Grinding Station with a zero-mana artifact. Cards: Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze, Wheel of Fortune, Jeska's Will, Grinding Station, Mox Amber. *fact · verified* — `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856` · `spellbook:1368-2706-3518` · `spellbook:1368-1878-2706` · `spellbook:1368-3698--44`
- **extra-turn-finish** (alternate): Final Fortune / Warrior's Oath: an extra turn to finish after a reload; the delayed loss trigger must be beaten. Cards: Final Fortune, Warrior's Oath. Enablers: Ad Nauseam, Necrodominance. *strategic_judgment · high* — [RogSi_Commander_Blueprint_2026-10-15.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · [RogSi_Candidate_Decisions_2026-10-15.md#L38](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md)

## Engines

- **zero-mana-commander:** Rograkh, Son of Rohgahh, Mox Amber, Springleaf Drum, Paradise Mantle, Culling the Weak, Infernal Plunge, Diabolic Intent. Online when: Rograkh cast for {0} from the command zone. *fact · high* — `oracle:Rograkh, Son of Rohgahh` · [RogSi_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · [RogSi_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md)
- **reloads:** Ad Nauseam, Necropotence, Necrodominance, Rhystic Study, Mystic Remora, Wheel of Fortune, Windfall. Online when: Mana from the fast-mana spine. *strategic_judgment · high* — [RogSi_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:commander-native` | yes | 8 | Cards that get much better with a free creature commander in play. | 11: Mox Amber, Springleaf Drum, Paradise Mantle, Culling the Weak, Infernal Plunge, Diabolic Intent, Deflecting Swat, Fierce Guardianship, Deadly Rollick, Jeska's Will, Flare of Duplication | — | *strategic_judgment · high* | [RogSi_Commander_Blueprint_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · [RogSi_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · [RogSi_Commander_Blueprint_2026-10-15.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · [RogSi_Commander_Blueprint_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · [RogSi_Commander_Blueprint_2026-10-15.md#L38](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) |
| `pkg:protection` | yes | 10 | Proactive and free protection for the win turn. | 14: Defense Grid, Hexing Squelcher, Samut, Tyrant of Naktamun, Vexing Bauble, Force of Will, Force of Negation, Pact of Negation, Mental Misstep, Flusterstorm, Mindbreak Trap, Swan Song, Pyroblast, Red Elemental Blast, Daze | — | *strategic_judgment · high* | [RogSi_Commander_Blueprint_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) |
| `pkg:tutors` | yes | 8 | Find a win. | 10: Demonic Tutor, Vampiric Tutor, Imperial Seal, Mystical Tutor, Demonic Counsel, Beseech the Mirror, Wishclaw Talisman, Gamble, Praetor's Grasp, Diabolic Intent | — | *strategic_judgment · high* | [RogSi_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md) |

## Key interactions

- **silas-permission:** Silas's combat-damage trigger lets you cast the targeted artifact that turn; normal timing still applies. (Silas Renn, Seeker Adept) *fact · verified* — [rogsi-03](../interactions/rograkh-son-of-rohgahh-silas-renn.md#rogsi-03-silas-renn-cast-one-artifact-card-from-your-graveyard-this-turn-at-normal-timing) · [RogSi_Candidate_Decisions_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md) · `oracle:Silas Renn, Seeker Adept`
- **bauble-symmetry:** Vexing Bauble also counters your own no-mana spells; sequence or sacrifice it first. Hexing Squelcher makes your spells uncounterable. (Vexing Bauble, Hexing Squelcher) *fact · high* — [RogSi_Candidate_Decisions_2026-10-15.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md)
- **samut-split-second:** Samut gives your instants and sorceries split second; triggered abilities like Vexing Bauble still happen. (Samut, Tyrant of Naktamun, Vexing Bauble) *fact · verified* — [rogsi-05](../interactions/rograkh-son-of-rohgahh-silas-renn.md#rogsi-05-samut-gives-your-instants-and-sorceries-split-second-but-triggers-still-happen) · [RogSi_Candidate_Decisions_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md) · `cr:702.61a`
- **extra-turn-loss:** Final Fortune and Warrior's Oath each create a lose-the-game trigger at that extra turn's end step. (Final Fortune, Warrior's Oath) *fact · verified* — [rogsi-07](../interactions/rograkh-son-of-rohgahh-silas-renn.md#rogsi-07-final-fortune--warriors-oath-the-lose-trigger-is-real-here) · [RogSi_Candidate_Decisions_2026-10-15.md#L38](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md)
- **demonic-counsel:** Before delirium, Demonic Counsel can only find a Demon card. (Demonic Counsel) *fact · verified* — [rogsi-08](../interactions/rograkh-son-of-rohgahh-silas-renn.md#rogsi-08-demonic-counsel-needs-delirium-mnemonic-betrayal-casts-but-never-plays-lands-undercity-sewers-is-fetchable) · [RogSi_Candidate_Decisions_2026-10-15.md#L39](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md)
- **bauble-m1-flag:** M1 dependency-risk flag: Vexing Bauble counters the deck's own free spells and {0} escapes; have Hexing Squelcher out or sacrifice Bauble first. (Vexing Bauble, Hexing Squelcher) *fact · high* — [rogsi-04](../interactions/rograkh-son-of-rohgahh-silas-renn.md#rogsi-04-vexing-bauble-counters-your-own-free-spells-rograkh-moxen-led-fierce-guardianship-flare-breach-escapes-for-0)
- **partner-tax:** Rograkh and Silas have separate commander tax; Rograkh is a free red legendary body. (Rograkh, Son of Rohgahh, Silas Renn, Seeker Adept) *fact · verified* — [rogsi-01](../interactions/rograkh-son-of-rohgahh-silas-renn.md#rogsi-01-partners-ubr-identity-separate-commander-tax-a-free-red-legendary-body) · [rogsi-02](../interactions/rograkh-son-of-rohgahh-silas-renn.md#rogsi-02-rograkh-as-a-resource-mox-amber-springleaf-drum-paradise-mantle-culling-the-weak-infernal-plunge-flare-of-duplication)

## Tutors and recursion

- Tutor target **Thassa's Oracle** via Demonic Tutor, Vampiric Tutor, Imperial Seal, Mystical Tutor, Diabolic Intent *strategic_judgment · high* — `spellbook:1295-3093`
- Tutor target **Lion's Eye Diamond** via Beseech the Mirror, Wishclaw Talisman, Gamble *strategic_judgment · high* — `spellbook:1368-3518-4856`
- Recursion: Underworld Breach, Yawgmoth's Will, Mnemonic Betrayal, Silas Renn, Seeker Adept *strategic_judgment · high* — [RogSi_Candidate_Decisions_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Full free-counter suite.
- **Protection:** Defense Grid, Hexing Squelcher, Samut, Vexing Bauble.
- **Mana:** 24 lands plus Moxen, rituals, LED, Lotus Petal and zero-mana artifacts.
- *strategic_judgment · high* — [RogSi_Candidate_Decisions_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md)

## Failure modes

- **graveyard-hate:** Graveyard hate stops Breach and Mnemonic Betrayal. Mitigations: Oracle lines. *strategic_judgment · high* — [RogSi_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md)
- **self-bauble:** Vexing Bauble can counter your own free spells. Mitigations: Sequencing; Hexing Squelcher. *strategic_judgment · high* — [RogSi_Candidate_Decisions_2026-10-15.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md)
- **naus-life:** Ad Nauseam and Necropotence cost a lot of life against fast tables. Mitigations: Low curve. *strategic_judgment · moderate* — [RogSi_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md)

## Identity core

- **Rograkh, Son of Rohgahh:** Free creature commander that turns on the free-spell and Mox suite. *fact · verified* — `oracle:Rograkh, Son of Rohgahh`
- **Mox Amber:** Zero-mana mana with Rograkh out. *strategic_judgment · high* — [RogSi_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md)
- **Culling the Weak:** Sacrifices Rograkh for BBBB. *strategic_judgment · high* — [RogSi_Commander_Blueprint_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md)
- **Ad Nauseam:** The main reload. *strategic_judgment · high* — [RogSi_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md)
- **Underworld Breach:** Primary combo engine. *strategic_judgment · high* — `spellbook:1368-3518-4856`

## Anti-goals and thematic constraints

- ✗ Not a full artifact/Monolith conversion (decisions L30).
- ✗ No Commandeer/Misdirection (L29); no Chromatic Star filler.
  - *strategic_judgment · high* — [RogSi_Candidate_Decisions_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md) · [RogSi_Candidate_Decisions_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md)
- Theme: Turbo Naus / Underworld Breach / Fast Mana (blueprint L43).
  - *strategic_judgment · high* — [RogSi_Commander_Blueprint_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.124a:** Partner. *fact · verified* — `cr:702.124a`
- **CR 702.61a:** Split second. *fact · verified* — `cr:702.61a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["artifacts", "combat damage / attack triggers"], "hooked_cards": 21, "role_counts": {"counter": 12, "draw": 8, "protection": 1, "ramp": 23, "removal": 5, "tutor": 9, "wipe": 2}, "lands": 24, "edhrec_pages": ["rograkh-son-of-rohgahh-silas-renn-seeker-adept"]}` *heuristic · low*

## Provenance

- Seeded from: [RogSi_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/RogSi_Commander_Blueprint_2026-10-15.md) · [RogSi_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/RogSi_Candidate_Decisions_2026-10-15.md) · [RogSi_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/RogSi_Approved_2026-10-15.md) · [RogSi_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/RogSi_Approval_Ready_Verification_2026-10-15.md) · [RogSi_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/RogSi_Whole_List_Audit_2026-10-15.md) · [RogSi_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/RogSi_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
