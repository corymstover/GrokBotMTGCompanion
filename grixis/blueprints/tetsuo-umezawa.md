# Blueprint — Tetsuo Umezawa

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/tetsuo-umezawa.md), state `SOURCE_BASELINE`, list `lh1:da8056ed35918860…`). Machine-readable source: [`data/grixis/blueprints/tetsuo-umezawa.json`](../../data/grixis/blueprints/tetsuo-umezawa.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Tetsuo Umezawa** — Legendary Creature — Human Archer

> Tetsuo Umezawa can't be the target of Aura spells.  
> {U}{B}{B}{R}, {T}: Destroy target tapped or blocking creature.

## Plan and commander role

- **Primary plan:** Tap/untap creature control: make targets with goad, forced attacks and tap effects, then use Tetsuo's {U}{B}{B}{R}, {T} to destroy tapped or blocking creatures, untapping him again and again (Minamo, Magewright's Stone, Thousand-Year Elixir, Alchemist, Fatestitcher, Puppeteer, Patriar's Seal, Retreat, Sting). *strategic_judgment · high*
- **Secondary:** Turn the tapped board into cards and pressure with Verity Circle, Borrowing 100,000 Arrows, Firkraag, Karazikar and Grenzo; Rings of Brighthearth and Illusionist's Bracers copy activations.
  - Evidence: [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)
- **Commander role: central.** Tetsuo's activation is the deck's repeatable removal, and the untap suite exists to reuse it. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native control. The one Spellbook combo (283-4091, Illusionist's Bracers + Aphetto Alchemist) gives infinite untaps but no mana, so Tetsuo still pays {U}{B}{B}{R} per activation. There is no compact kill; the deck wins by grinding and combat. The source calls Tetsuo mana-intensive and board-dependent (blueprint L43).
  - Evidence: [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) · `spellbook:283-4091`
- **Dependency level:** high *strategic_judgment · high* — [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Low-to-mid Bracket 4: tuned and well protected, but no compact kill and a narrow commander. Agrees with the source; it plays below most batch-4 decks.) | *strategic_judgment · moderate* | [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Umezawa_Whole_List_Audit_2026-10-15.md#L64](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tetsuo_Umezawa_Whole_List_Audit_2026-10-15.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Tetsuo_Umezawa` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 4, "2": 13, "3": 10, "4": 4}, "decks_with_bracket": 31, "share_b4_plus": 0.129, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__tetsuo-umezawa.json`

## Win conditions

- **grind-and-goad** (natural): Repeated removal plus goad and forced combat until opponents are out of creatures; Kardur, Firkraag and Karazikar push damage. Cards: Tetsuo Umezawa, Kardur, Doomscourge, Firkraag, Cunning Instigator, Karazikar, the Eye Tyrant, Red Death, Shipwrecker. Enablers: Flood, Blustersquall, Puppeteer, Disrupt Decorum. *strategic_judgment · moderate* — [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)
- **bracers-alchemist** (combo): Illusionist's Bracers + Aphetto Alchemist gives infinite untaps; with enough mana it gives repeated Tetsuo activations. Cards: Illusionist's Bracers, Aphetto Alchemist. Enablers: Tetsuo Umezawa. *strategic_judgment · moderate* — `spellbook:283-4091`

## Engines

- **destroy-tapped-or-blocking:** Tetsuo Umezawa. Online when: {U}{B}{B}{R}; target tapped or blocking. *fact · high* — `oracle:Tetsuo Umezawa` · [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)
- **untap-suite:** Minamo, School at Water's Edge, Magewright's Stone, Thousand-Year Elixir, Aphetto Alchemist, Fatestitcher, Puppeteer, Patriar's Seal, Retreat to Coralhelm, Sting, the Glinting Dagger. Online when: Tetsuo tapped after an activation. *strategic_judgment · high* — [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)
- **copy-activation:** Rings of Brighthearth, Illusionist's Bracers. Online when: Extra mana for the copy. *strategic_judgment · high* — [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:untap` | yes | 7 | Reuse Tetsuo. | 9: Minamo, School at Water's Edge, Magewright's Stone, Thousand-Year Elixir, Aphetto Alchemist, Fatestitcher, Puppeteer, Patriar's Seal, Retreat to Coralhelm, Sting, the Glinting Dagger | — | *strategic_judgment · high* | [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) |
| `pkg:target-makers` | yes | 8 | Make tapped or blocking targets. | 12: Flood, Blustersquall, Puppeteer, Disrupt Decorum, Fumiko the Lowblood, Kardur, Doomscourge, Firkraag, Cunning Instigator, Karazikar, the Eye Tyrant, Bloodthirsty Blade, Shiny Impetus, Sly Instigator, Grenzo, Havoc Raiser | — | *strategic_judgment · high* | [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) |
| `pkg:payoffs` | optional | 3 | Convert the tapped board. | 5: Verity Circle, Borrowing 100,000 Arrows, Firkraag, Cunning Instigator, Karazikar, the Eye Tyrant, Grenzo, Havoc Raiser | — | *strategic_judgment · moderate* | [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) |

## Key interactions

- **two-conditions:** Tapped or blocking are independent: an untapped blocker is still a legal target. (Tetsuo Umezawa) *fact · high* — `oracle:Tetsuo Umezawa` · [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)
- **sting-reset:** Sting untaps Tetsuo at the beginning of each combat, every player's turn. (Sting, the Glinting Dagger, Tetsuo Umezawa) *fact · high* — [Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md) · [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)
- **no-mana-vault:** Mana Vault was rejected: Tetsuo's cost and activation have no generic mana. (Patriar's Seal) *fact · high* — [Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md)
- **retreat-fetch:** A fetchland gives Retreat to Coralhelm two landfall triggers. (Retreat to Coralhelm) *fact · high* — [Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md#L44](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md)
- **goad-targets:** Goaded creatures must attack, so they become tapped targets. (Disrupt Decorum, Bloodthirsty Blade, Shiny Impetus) *fact · high* — `cr:701.15a`

## Tutors and recursion

- Tutor target **Illusionist's Bracers** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — `spellbook:283-4091`
- Recursion: — *strategic_judgment · moderate* — [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Mana Drain, Counterspell, Terminate, Withering Torment, Chaos Warp, Damnation, Blasphemous Act, Cyclonic Rift, Vandalblast.
- **Protection:** Lightning Greaves, Swiftfoot Boots, Force of Will.
- **Mana:** 36 land-capable slots with heavy colored sources for {U}{B}{B}{R}.
- *strategic_judgment · moderate* — [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md)

## Failure modes

- **colored-mana-hungry:** Each activation costs four colored mana. Mitigations: Patriar's Seal; Premium duals. *strategic_judgment · high* — [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)
- **creatureless-opponents:** Spell-based combo opponents give no targets. Mitigations: Force of Will; Mana Drain. *strategic_judgment · high* — `oracle:Tetsuo Umezawa`
- **removal-on-tetsuo:** Removal on Tetsuo shuts off the deck. Mitigations: Greaves; Boots. *strategic_judgment · moderate* — `oracle:Tetsuo Umezawa`

## Identity core

- **Tetsuo Umezawa:** Repeatable destroy-tapped-or-blocking. *fact · verified* — `oracle:Tetsuo Umezawa`
- **Sting, the Glinting Dagger:** Untaps Tetsuo each combat. *strategic_judgment · high* — [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)
- **Minamo, School at Water's Edge:** Land that untaps Tetsuo. *strategic_judgment · high* — [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)
- **Illusionist's Bracers:** Copies activations. *strategic_judgment · high* — `spellbook:283-4091`
- **Flood:** Repeatable target maker. *strategic_judgment · high* — [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No generic cEDH packages (decisions L68).
- ✗ No Mana Vault (L60).
  - *strategic_judgment · high* — [Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md#L68](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md) · [Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md)
- Theme: Tap/untap / forced combat / activated abilities (blueprint L45).
  - *strategic_judgment · high* — [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.15a:** Goad. *fact · verified* — `cr:701.15a`
- **CR 602.2:** Activating abilities. *fact · verified* — `cr:602.2`
- **CR 509.1a:** Declaring blockers. *fact · verified* — `cr:509.1a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["tapping / blocking creatures"], "hooked_cards": 24, "role_counts": {"counter": 3, "draw": 10, "protection": 2, "ramp": 14, "removal": 9, "tutor": 2, "wipe": 3}, "lands": 35, "edhrec_pages": ["tetsuo-umezawa"]}` *heuristic · low*

## Provenance

- Seeded from: [Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Umezawa_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Umezawa_Candidate_Decisions_2026-10-15.md) · [Tetsuo_Umezawa_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Tetsuo_Umezawa_Approved_2026-10-15.md) · [Tetsuo_Umezawa_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tetsuo_Umezawa_Approval_Ready_Verification_2026-10-15.md) · [Tetsuo_Umezawa_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tetsuo_Umezawa_Whole_List_Audit_2026-10-15.md) · [Tetsuo_Umezawa_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Tetsuo_Umezawa_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
