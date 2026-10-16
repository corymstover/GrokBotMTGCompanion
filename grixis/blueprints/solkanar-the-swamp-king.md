# Blueprint — Sol'kanar the Swamp King

> **Commander Blueprint v1** (cory_reviewed, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/solkanar-the-swamp-king.md), state `SOURCE_BASELINE`, list `lh1:33b7d4dad6f4db82…`). Machine-readable source: [`data/grixis/blueprints/solkanar-the-swamp-king.json`](../../data/grixis/blueprints/solkanar-the-swamp-king.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Sol'kanar the Swamp King** — Legendary Creature — Demon

> Swampwalk (This creature can't be blocked as long as defending player controls a Swamp.)  
> Whenever a player casts a black spell, you gain 1 life.

## Plan and commander role

- **Primary plan:** Black-spell lifegain: Sol'kanar and Demon's Horn trigger on every black spell (on every spell with Painter's Servant naming black), and the gains feed Exquisite Blood / Bloodthirsty Conqueror loops with Vito, Blight-Priest, Enduring Tenacity or Starscape Cleric. *strategic_judgment · high*
- **Secondary:** Swamp matters (Blanket of Night, Urborg, Cabal Coffers, Crypt Ghast) for swampwalk and mana; Painter + Grindstone; wheels with Sheoldred and Underworld Dreams.
  - Evidence: [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md)
- **Commander role: supporting.** Sol'kanar gains 1 life per black spell, which starts the life loops, and has swampwalk once Blanket of Night or Urborg is out. *strategic_judgment · high*
- ⚠️ **Honest note:** Honest call: supporting. None of the 13 Spellbook combos uses Sol'kanar; the loops start from any lifegain, and Demon's Horn duplicates the trigger. The source itself calls him a five-mana incremental trigger engine (blueprint L26). The deck is a strong two-card life-loop deck built around a modest commander. M1 review (solkanar-01..06, all verified) confirms the trigger and loop rules.
  - Evidence: [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md) · `spellbook:110-3966` · `registry:data/grixis/blueprint_reviews.json#solkanar-the-swamp-king`
- **Dependency level:** low *strategic_judgment · high* — `spellbook:110-3966` · `registry:data/grixis/blueprint_reviews.json#solkanar-the-swamp-king`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: many two-card loops and premium tutors/fast mana; the commander adds little speed. High Bracket 4; agrees with the source.) | *strategic_judgment · high* | [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) · `spellbook:110-3966` · `registry:data/grixis/blueprint_reviews.json#solkanar-the-swamp-king` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Sol_kanar_the_Swamp_King` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 32, "2": 83, "3": 46, "4": 22, "5": 2}, "decks_with_bracket": 185, "share_b4_plus": 0.13, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__solkanar-the-swamp-king.json`

## Win conditions

- **life-loops** (combo): Exquisite Blood or Bloodthirsty Conqueror plus a drain-on-gain payoff (Vito, Marauding Blight-Priest, Enduring Tenacity, Starscape Cleric) loops until opponents die. Cards: Exquisite Blood, Bloodthirsty Conqueror, Vito, Thorn of the Dusk Rose, Marauding Blight-Priest, Enduring Tenacity, Starscape Cleric. Enablers: Sol'kanar the Swamp King, Demon's Horn. *strategic_judgment · high* — `spellbook:110-3966` · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md)
- **reservoir-activation** (combo): Aetherflux Reservoir is a lifegain enabler and an independent payoff, not a drain-on-gain loop half. With Exquisite Blood or Bloodthirsty Conqueror at 51+ life, each 'pay 50 life: 50 damage' activation gives the 50 life back (Spellbook 3966-4740), which is a repeated-activation kill, not a Vito-style loop. Cards: Aetherflux Reservoir, Exquisite Blood, Bloodthirsty Conqueror. Enablers: Sol'kanar the Swamp King, Demon's Horn. *strategic_judgment · high* — `spellbook:3966-4740` · `oracle:Aetherflux Reservoir` · `registry:data/grixis/blueprint_reviews.json#solkanar-the-swamp-king`
- **painter-grindstone** (combo): Painter's Servant + Grindstone mills each library. Cards: Painter's Servant, Grindstone. Enablers: Demonic Tutor. *strategic_judgment · high* — `spellbook:1078-2302` · [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md)
- **citadel-top-reservoir** (combo): Sensei's Top + Bolas's Citadel + Aetherflux Reservoir. Cards: Sensei's Divining Top, Bolas's Citadel, Aetherflux Reservoir. *strategic_judgment · moderate* — `spellbook:2173-4740-5078` · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md)
- **wheel-pressure** (natural): Wheels with Sheoldred / Underworld Dreams, plus Gray Merchant and Exsanguinate drains. Cards: Wheel of Fortune, Windfall, Sheoldred, the Apocalypse, Underworld Dreams, Gray Merchant of Asphodel, Exsanguinate. *strategic_judgment · moderate* — [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md)

## Engines

- **black-spell-gain:** Sol'kanar the Swamp King, Demon's Horn, Painter's Servant, Bontu's Monument, Jet Medallion, K'rrik, Son of Yawgmoth. Online when: Black spells are cast (all spells with Painter naming black). *fact · high* — `oracle:Sol'kanar the Swamp King` · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md) · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md)
- **swamp-mana:** Blanket of Night, Urborg, Tomb of Yawgmoth, Cabal Coffers, Crypt Ghast, Dread Presence, Consuming Corruption. Online when: Swamps on the battlefield. *strategic_judgment · high* — [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md) · [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:life-loop` | yes | 5 | Redundant two-card drain-on-gain loops (Aetherflux Reservoir is modelled separately as an enabler/payoff). | 6: Exquisite Blood, Bloodthirsty Conqueror, Vito, Thorn of the Dusk Rose, Marauding Blight-Priest, Enduring Tenacity, Starscape Cleric | — | *strategic_judgment · high* | [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md) |
| `pkg:swamp` | yes | 5 | Swamp infrastructure. | 6: Blanket of Night, Urborg, Tomb of Yawgmoth, Cabal Coffers, Crypt Ghast, Dread Presence, Consuming Corruption | — | *strategic_judgment · high* | [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) |
| `pkg:black-spells` | optional | 4 | Black versions of removal and ramp. | 5: Withering Torment, The Soul Stone, Fell the Profane // Fell Mire, Toxic Deluge, Dark Ritual | — | *strategic_judgment · high* | [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md) · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md) |

## Key interactions

- **painter-black:** Painter naming black makes every spell black in addition to its colors, so opponents' spells trigger Sol'kanar and Horn. (Painter's Servant, Sol'kanar the Swamp King, Demon's Horn) *fact · verified* — [solkanar-02](../interactions/solkanar-the-swamp-king.md#solkanar-02-painters-servant-naming-black-every-spell-is-black-and-grindstone-mills-forever) · `oracle:Painter's Servant` · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md) · `cr:105.3`
- **blanket-swampwalk:** Blanket of Night / Urborg make every land a Swamp, which turns on swampwalk and widens Coffers/Crypt Ghast. (Blanket of Night, Urborg, Tomb of Yawgmoth, Sol'kanar the Swamp King) *fact · verified* — [solkanar-05](../interactions/solkanar-the-swamp-king.md#solkanar-05-blanket-of-night--urborg-every-land-is-a-swamp-swampwalk-coffers-crypt-ghast) · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md) · `cr:702.14c`
- **separate-triggers:** Sol'kanar and Demon's Horn trigger separately for each black spell. (Sol'kanar the Swamp King, Demon's Horn) *fact · verified* — [solkanar-01](../interactions/solkanar-the-swamp-king.md#solkanar-01-solkanar-and-demons-horn-any-players-black-spell-gains-life-one-event-per-spell) · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md)
- **life-loops-m1:** Exquisite Blood / Bloodthirsty Conqueror plus a gain-to-loss payoff is an infinite drain. (Exquisite Blood, Bloodthirsty Conqueror) *fact · verified* — [solkanar-03](../interactions/solkanar-the-swamp-king.md#solkanar-03-exquisite-blood--bloodthirsty-conqueror--a-lifegain-to-loss-payoff-infinite-drain)
- **top-citadel:** Sensei's Top + Bolas's Citadel + Sheoldred or Aetherflux Reservoir. (Sensei's Divining Top, Bolas's Citadel, Aetherflux Reservoir) *fact · verified* — [solkanar-04](../interactions/solkanar-the-swamp-king.md#solkanar-04-senseis-divining-top--bolass-citadel--sheoldred-or-aetherflux-reservoir)

## Tutors and recursion

- Tutor target **Exquisite Blood** via Demonic Tutor, Vampiric Tutor, Imperial Seal, Beseech the Mirror *strategic_judgment · high* — `spellbook:110-3966`
- Recursion: The Soul Stone, Witch of the Moors *strategic_judgment · moderate* — [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md) · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Counterspell, Mana Drain, Swan Song, Fierce Guardianship, Withering Torment, Deadly Rollick, Toxic Deluge, Cyclonic Rift.
- **Protection:** Deflecting Swat, Fierce Guardianship.
- **Mana:** 36 land-capable slots (Swamp-typed duals, Coffers) plus Mox Diamond, Chrome Mox and Lotus Petal.
- *strategic_judgment · moderate* — [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md) · [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md)

## Failure modes

- **loop-hate:** Enchantment or creature removal on loop pieces; the deck needs both halves. Mitigations: Redundant loop halves; Tutors. *strategic_judgment · high* — `spellbook:3966-5755`
- **weak-commander:** Sol'kanar alone is slow incremental value. Mitigations: Demon's Horn; Other lifegain sources. *strategic_judgment · moderate* — [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md)
- **no-force:** Too few blue cards to pitch to Force of Will. Mitigations: Counterspell; Fierce Guardianship. *strategic_judgment · moderate* — [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md)

## Identity core

- **Sol'kanar the Swamp King:** Lifegain per black spell; swampwalk. *fact · verified* — `oracle:Sol'kanar the Swamp King`
- **Painter's Servant:** Makes every spell black; half of Grindstone. *strategic_judgment · high* — [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md)
- **Exquisite Blood:** Loop half. *strategic_judgment · high* — `spellbook:3966-4740`
- **Bloodthirsty Conqueror:** Second loop half. *strategic_judgment · high* — `spellbook:4740-6191`
- **Demon's Horn:** Second black-spell trigger. *strategic_judgment · high* — [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No generic Thoracle/Breach (blueprint L36).
- ✗ No redundant low-impact lifegain artifacts from EDHREC (L35).
  - *strategic_judgment · high* — [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md)
- Theme: Black spells / lifegain / Swamp matters (blueprint L42).
  - *strategic_judgment · high* — [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.14c:** Landwalk. *fact · verified* — `cr:702.14c`
- **CR 105.3:** Changing an object's color. *fact · verified* — `cr:105.3`
- **CR 119.9:** Life gain events. *fact · verified* — `cr:119.9`

## Supporting features (heuristic, not identity)

- `{"hooks": ["black spells / Swamps", "life gain"], "hooked_cards": 19, "role_counts": {"counter": 4, "draw": 12, "protection": 1, "ramp": 16, "removal": 8, "tutor": 4, "wipe": 2}, "lands": 35, "edhrec_pages": ["solkanar-the-swamp-king"]}` *heuristic · low*

## Provenance

- Seeded from: [Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Solkanar_the_Swamp_King_Commander_Blueprint_2026-10-15.md) · [Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Solkanar_the_Swamp_King_Candidate_Decisions_2026-10-15.md) · [Solkanar_the_Swamp_King_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Solkanar_the_Swamp_King_Approved_2026-10-15.md) · [Solkanar_the_Swamp_King_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Solkanar_the_Swamp_King_Approval_Ready_Verification_2026-10-15.md) · [Solkanar_the_Swamp_King_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Solkanar_the_Swamp_King_Whole_List_Audit_2026-10-15.md) · [Solkanar_the_Swamp_King_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Solkanar_the_Swamp_King_Approved_2026-10-15.txt)
- Reviewed by: corymstover
- **Cory's review (2026-10-16, chat t50u (2026-10-16T17:47Z, relayed)):** ceiling B4, commander role supporting, dependency low. Resolves this blueprint's ceiling and commander role. Not M2 acceptance; no list change. *approved_decision · verified*
- **Correction (Bot cycle 62):** retracted Aetherflux Reservoir listed as a drain-on-gain half of the Exquisite Blood / Bloodthirsty Conqueror loops (win_conditions life-loops, pkg:life-loop) → Reservoir gains life on cast and pays 50 life for 50 damage; it is a lifegain enabler and an independent payoff (win_conditions reservoir-activation), not a Vito-style loop half.
