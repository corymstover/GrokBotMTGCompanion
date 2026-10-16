# Blueprint — Nicol Bolas, the Ravager // Nicol Bolas, the Arisen

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/nicol-bolas-the-ravager.md), state `SOURCE_BASELINE`, list `lh1:c2b4559a1e5f0415…`). Machine-readable source: [`data/grixis/blueprints/nicol-bolas-the-ravager.json`](../../data/grixis/blueprints/nicol-bolas-the-ravager.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Nicol Bolas, the Ravager // Nicol Bolas, the Arisen** — Legendary Creature — Elder Dragon // Legendary Planeswalker — Bolas

> Flying  
> When Nicol Bolas enters, each opponent discards a card.  
> {4}{U}{B}{R}: Exile Nicol Bolas, then return him to the battlefield transformed under his owner's control. Activate only as a sorcery.  
> +2: Draw two cards.  
> −3: Nicol Bolas deals 10 damage to target creature or planeswalker.  
> −4: Put target creature or planeswalker card from a graveyard onto the battlefield under your control.  
> −12: Exile all but the bottom card of target player's library.

## Plan and commander role

- **Primary plan:** Bolas superfriends: cast Ravager for ETB discard, transform him into the Arisen (Training Grounds helps), then proliferate, copy and repeat loyalty abilities across Bolas and other planeswalkers. *strategic_judgment · high*
- **Secondary:** Chain Veil infrastructure with Teferi gives deterministic loops; the Arisen's -4 reanimates discarded creatures and planeswalkers.
  - Evidence: [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md) · [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)
- **Commander role: significant.** The Arisen is the centrepiece planeswalker and Ravager's ETB gives discard. *strategic_judgment · high*
- ⚠️ **Honest note:** All three Spellbook infinites (Teferi + Chain Veil, Teferi + Ichormoon Gauntlet + Chain Veil or Rowan's Talent) are commander-free. Bolas's transform costs seven mana at sorcery speed. He is the deck's best planeswalker rather than its engine, and a superfriends shell would work under another Grixis walker commander. The cycle 51 M1 review (bolasrav-01..08, all verified) confirms the transform and loyalty rules.
  - Evidence: [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md) · `spellbook:787-1124`
- **Dependency level:** low *strategic_judgment · high* — `spellbook:787-1124`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: fast mana and Teferi/Chain Veil loops, but a slow superfriends core. Agrees with the source.) | *strategic_judgment · high* | [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md) · `spellbook:787-1124` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Nicol_Bolas__the_Ravager` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 64, "2": 339, "3": 941, "4": 629, "5": 67}, "decks_with_bracket": 2040, "share_b4_plus": 0.341, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__nicol-bolas-the-ravager.json`

## Win conditions

- **teferi-veil** (combo): Teferi, Temporal Archmage + The Chain Veil; Teferi, Master of Time + Ichormoon Gauntlet + The Chain Veil or Rowan's Talent: infinite loyalty activations. Cards: Teferi, Temporal Archmage, Teferi, Master of Time, The Chain Veil, Ichormoon Gauntlet, Rowan's Talent. *fact · verified* — `spellbook:787-1124` · `spellbook:1124-1543-2247` · `spellbook:652-1543-2247`
- **arisen-ultimate** (alternate): The Arisen's -12 exiles all but one card of a library; extra activations and proliferate get there quickly. Cards: Nicol Bolas, the Ravager // Nicol Bolas, the Arisen, Rings of Brighthearth, Spark Double. Enablers: Deepglow Skate, Flux Channeler, Tekuthal, Inquiry Dominus, Karn's Bastion. *strategic_judgment · moderate* — `oracle:Nicol Bolas, the Ravager // Nicol Bolas, the Arisen` · [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)
- **superfriends-value** (natural): Planeswalker advantage and ultimates. Cards: Nicol Bolas, Dragon-God, Nicol Bolas, God-Pharaoh, Nicol Bolas, Planeswalker, Liliana, Dreadhorde General. Enablers: Deepglow Skate, Flux Channeler, Tekuthal, Inquiry Dominus, Karn's Bastion, Inexorable Tide, Ripples of Potential, Dreamtide Whale, Tezzeret's Gambit. *strategic_judgment · moderate* — [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)

## Engines

- **transform:** Nicol Bolas, the Ravager // Nicol Bolas, the Arisen, Training Grounds. Online when: Seven mana at sorcery speed (less with Training Grounds). *fact · high* — `oracle:Nicol Bolas, the Ravager // Nicol Bolas, the Arisen` · [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md) · [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)
- **loyalty-multiplication:** The Chain Veil, Ichormoon Gauntlet, Rings of Brighthearth, Sanctum Lurker, Spark Double, Deepglow Skate, Flux Channeler, Tekuthal, Inquiry Dominus. Online when: Planeswalkers in play. *strategic_judgment · high* — [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md) · [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:planeswalkers` | yes | 8 | Bolas and supporting planeswalkers. | 10: Nicol Bolas, Dragon-God, Nicol Bolas, God-Pharaoh, Nicol Bolas, Planeswalker, Liliana, Dreadhorde General, Teferi, Master of Time, Teferi, Temporal Archmage, Tezzeret the Seeker, The Theorist, Jace Beleren, Narset, Parter of Veils, Vraska, Betrayal's Sting | — | *strategic_judgment · high* | [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md) |
| `pkg:proliferate` | yes | 5 | Proliferate and loyalty copying. | 8: Deepglow Skate, Flux Channeler, Tekuthal, Inquiry Dominus, Karn's Bastion, Inexorable Tide, Ripples of Potential, Dreamtide Whale, Tezzeret's Gambit | — | *strategic_judgment · high* | [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md) |
| `pkg:etb-reset` | optional | 1 | Reset Ravager's ETB. | 2: Displacer Kitten, Deepglow Skate | — | *strategic_judgment · high* | [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md) |

## Key interactions

- **transform-exile-return:** Ravager's ability exiles him and returns him transformed: a new object with summoning sickness that doesn't matter for loyalty abilities. (Nicol Bolas, the Ravager // Nicol Bolas, the Arisen) *fact · verified* — [bolasrav-01](../interactions/nicol-bolas-the-ravager.md#bolasrav-01-transform-by-exile-and-return-the-arisen-is-a-new-object-and-can-use-loyalty-right-away) · `oracle:Nicol Bolas, the Ravager // Nicol Bolas, the Arisen` · `cr:701.27a`
- **one-loyalty-activation:** Normally one loyalty activation per planeswalker per turn; Chain Veil, Gauntlet and Rings break this. (The Chain Veil, Ichormoon Gauntlet, Rings of Brighthearth) *fact · verified* — [bolasrav-03](../interactions/nicol-bolas-the-ravager.md#bolasrav-03-copied-loyalty-abilities-dont-cost-loyalty-rowans-talent-rings-of-brighthearth-jayas-phoenix) · [bolasrav-04](../interactions/nicol-bolas-the-ravager.md#bolasrav-04-teferi-temporal-archmage--the-chain-veil--rings) · `cr:606.3`
- **proliferate:** Proliferate adds loyalty to every chosen planeswalker. (Deepglow Skate, Flux Channeler, Tekuthal, Inquiry Dominus) *fact · verified* — [bolasrav-08](../interactions/nicol-bolas-the-ravager.md#bolasrav-08-loyalty-support-proliferate-tekuthal-doubles-sanctum-lurker-at-0-ripples-phase-out) · `cr:701.34a`
- **kitten-reset:** Displacer Kitten flickers Ravager for repeated ETB discard. Flickering the Arisen returns the front face and strips Talents attached to him. (Displacer Kitten, Nicol Bolas, the Ravager // Nicol Bolas, the Arisen) *fact · verified* — [bolasrav-02](../interactions/nicol-bolas-the-ravager.md#bolasrav-02-displacer-kitten-resets-to-ravager-front-face--and-strips-talents) · [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)
- **bolas-walker-checks:** Deliver Unto Evil sees the Bolas planeswalkers; Dark Intimations' Bolas clause doesn't apply here. (Deliver Unto Evil, Dark Intimations) *fact · verified* — [bolasrav-06](../interactions/nicol-bolas-the-ravager.md#bolasrav-06-bolas-planeswalker-checks-and-casts-deliver-unto-evil-yes-dark-intimations-no)
- **spark-dragon-god:** Spark Double copies the Arisen; Nicol Bolas, Dragon-God borrows every planeswalker's loyalty abilities. (Spark Double, Nicol Bolas, Dragon-God, Nicol Bolas, the Ravager // Nicol Bolas, the Arisen) *fact · verified* — [bolasrav-07](../interactions/nicol-bolas-the-ravager.md#bolasrav-07-spark-double-copies-the-arisen-nicol-bolas-dragon-god-borrows-every-walkers-loyalty-abilities)

## Tutors and recursion

- Tutor target **The Chain Veil** via Tezzeret the Seeker, Demonic Tutor, Vampiric Tutor, Gamble *strategic_judgment · high* — `spellbook:787-1124`
- Tutor target **Teferi, Temporal Archmage** via Demonic Tutor, Dark Intimations *strategic_judgment · moderate* — `spellbook:787-1124`
- Recursion: Nicol Bolas, the Ravager // Nicol Bolas, the Arisen, Jeska's Will, Jaya's Phoenix, Liliana's Talent, Deliver Unto Evil, The Eldest Reborn *strategic_judgment · moderate* — [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Mana Drain, Swan Song, An Offer You Can't Refuse, Deadly Rollick, Damnation, Toxic Deluge, Cyclonic Rift, The Elderspell.
- **Protection:** Fierce Guardianship, Cavern of Souls.
- **Mana:** 34 lands, fast mana, Signets/Talismans.
- *strategic_judgment · moderate* — [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)

## Failure modes

- **sorcery-transform:** The transform is slow and telegraphed. Mitigations: Training Grounds. *strategic_judgment · high* — `oracle:Nicol Bolas, the Ravager // Nicol Bolas, the Arisen`
- **walker-pressure:** Combat pressure and walker removal punish a superfriends board. Mitigations: Sweepers; Vraska/-3 removal. *strategic_judgment · high* — [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)
- **veil-hate:** Artifact removal answers the Veil/Gauntlet. Mitigations: Redundant loyalty multipliers. *strategic_judgment · moderate* — `spellbook:787-1124`

## Identity core

- **Nicol Bolas, the Ravager // Nicol Bolas, the Arisen:** ETB discard and the Arisen planeswalker. *fact · verified* — `oracle:Nicol Bolas, the Ravager // Nicol Bolas, the Arisen`
- **Training Grounds:** Cheaper transform. *strategic_judgment · high* — [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)
- **The Chain Veil:** Extra loyalty activations and the combo. *strategic_judgment · high* — `spellbook:787-1124`
- **Ichormoon Gauntlet:** Loyalty multiplier and combo piece. *strategic_judgment · high* — `spellbook:1124-1543-2247`
- **Nicol Bolas, Planeswalker:** High-synergy Bolas walker re-added after review. *strategic_judgment · high* — [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ Owns superfriends/transform/proliferate; leave discard-damage to deck #41 (blueprint L37–L44).
- ✗ No generic wheel locks or draw-punishment (blueprint L44).
  - *strategic_judgment · high* — [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L39](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md) · [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L44](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)
- Theme: Bolas-flavoured planeswalkers (blueprint L43).
  - *strategic_judgment · high* — [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.27a:** Transform. *fact · verified* — `cr:701.27a`
- **CR 606.3:** Loyalty ability timing. *fact · verified* — `cr:606.3`

## Supporting features (heuristic, not identity)

- `{"hooks": ["discard"], "hooked_cards": 9, "role_counts": {"counter": 5, "draw": 10, "protection": 2, "ramp": 17, "removal": 7, "tutor": 5, "wipe": 2}, "lands": 34, "edhrec_pages": ["nicol-bolas-the-ravager"]}` *heuristic · low*

## Provenance

- Seeded from: [Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_the_Ravager_Commander_First_Blueprint_2026-10-15.md) · [Nicol_Bolas_the_Ravager_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Nicol_Bolas_the_Ravager_Candidate_Decisions_2026-10-15.md) · [Nicol_Bolas_the_Ravager_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Nicol_Bolas_the_Ravager_Approved_2026-10-15.md) · [Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md) · [Nicol_Bolas_the_Ravager_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_the_Ravager_Whole_List_Audit_2026-10-15.md) · [Nicol_Bolas_the_Ravager_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Nicol_Bolas_the_Ravager_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
