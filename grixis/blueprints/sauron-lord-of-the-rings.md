# Blueprint — Sauron, Lord of the Rings

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/sauron-lord-of-the-rings.md), state `SOURCE_BASELINE`, list `lh1:56944f00fbf608fa…`). Machine-readable source: [`data/grixis/blueprints/sauron-lord-of-the-rings.json`](../../data/grixis/blueprints/sauron-lord-of-the-rings.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Sauron, Lord of the Rings** — Legendary Creature — Avatar Horror

> When you cast this spell, amass Orcs 5, mill five cards, then return a creature card from your graveyard to the battlefield.  
> Trample  
> Whenever a commander an opponent controls dies, the Ring tempts you.

## Plan and commander role

- **Primary plan:** Cast-trigger reanimator: put premium creatures in the graveyard early (Entomb, Buried Alive, loots), accelerate the eight-mana commander, and cast Sauron to amass 5, mill 5 and return the best creature, even if Sauron is countered. *strategic_judgment · high*
- **Secondary:** Cheap secondary reanimation when Sauron isn't available, Anger/Wonder for haste and flying from the graveyard, and the Nazgûl/Ring/Orc package for pressure.
  - Evidence: [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md)
- **Commander role: central.** Sauron's cast trigger is the deck's best reanimation spell, and Command Beacon recasts it without tax. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native but expensive: eight mana, and Spellbook finds no combos. The source calls the engine value/reanimation rather than a compact win (blueprint L21). The deck can win without him through cheap reanimation of Archon, Valgavoth or Jin-Gitaxias. Expect mid Bracket 4. M1 review (sauronlotr-01..05, all verified) confirms the cast trigger and reanimation rules.
  - Evidence: [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md)
- **Dependency level:** medium *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: strong reanimator with fast mana and free protection, but no compact combo and an eight-mana commander. Agrees with the source.) | *strategic_judgment · high* | [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Sauron__Lord_of_the_Rings` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 15, "2": 469, "3": 588, "4": 107, "5": 3}, "decks_with_bracket": 1182, "share_b4_plus": 0.093, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__sauron-lord-of-the-rings.json`

## Win conditions

- **reanimated-threats** (natural): Reanimated Archon of Cruelty, Valgavoth, Jin-Gitaxias or Sheoldred plus the Orc Army, with haste/flying from Anger and Wonder. Cards: Sauron, Lord of the Rings, Archon of Cruelty, Valgavoth, Terror Eater, Jin-Gitaxias, Core Augur, Sheoldred, Whispering One, Anger, Wonder. Enablers: Reanimate, Animate Dead, Necromancy, Dance of the Dead, Victimize. *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md)
- **ring-orcs** (natural): Nazgûl, Call of the Ring and Army growth as pressure. Cards: Nazgûl, Call of the Ring, The Black Gate. Enablers: Sauron, Lord of the Rings. *strategic_judgment · moderate* — [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md)

## Engines

- **cast-trigger:** Sauron, Lord of the Rings, Command Beacon. Online when: Eight mana (less tax with Command Beacon); the trigger survives a counter. *fact · high* — `oracle:Sauron, Lord of the Rings` · [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L44](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md)
- **setup-and-reanimate:** Entomb, Buried Alive, Faithless Looting, Frantic Search, Forbidden Alchemy, Thrill of Possibility, Reanimate, Animate Dead, Necromancy, Dance of the Dead, Victimize. Online when: A target in the graveyard. *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:targets` | yes | 7 | High-impact ETB/static creatures. | 10: Archon of Cruelty, Valgavoth, Terror Eater, Jin-Gitaxias, Core Augur, Sheoldred, Whispering One, Ancient Brass Dragon, Cavern-Hoard Dragon, The Balrog of Moria, Metamorphosis Fanatic, Troll of Khazad-dûm, Voracious Fell Beast | — | *strategic_judgment · high* | [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) |
| `pkg:reanimation` | yes | 8 | Secondary reanimation so the deck works without Sauron. | 11: Reanimate, Animate Dead, Necromancy, Dance of the Dead, Victimize, Living Death, Persist, Grave Researcher // Reanimate, Too Greedily, Too Deep, Ripples of Undeath, Sneak Attack | — | *strategic_judgment · high* | [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) |
| `pkg:fast-mana` | yes | 8 | Solve the eight-mana bottleneck. | 12: Sol Ring, Mana Vault, Grim Monolith, Ancient Tomb, Dark Ritual, Arcane Signet, Talisman of Creativity, Talisman of Dominance, Talisman of Indulgence, Relic of Sauron, Phyrexian Tower, Command Beacon | — | *strategic_judgment · high* | [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) |
| `pkg:ring-orc` | optional | 3 | LOTR/Ring/Orc identity. | 7: Nazgûl, Call of the Ring, The Mouth of Sauron, Sauron, the Dark Lord, Saruman, the White Hand, Barad-dûr, Mount Doom | — | *strategic_judgment · moderate* | [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) |

## Key interactions

- **cast-not-enter:** The trigger is on cast; countering Sauron doesn't stop it. (Sauron, Lord of the Rings) *fact · verified* — [sauronlotr-01](../interactions/sauron-lord-of-the-rings.md#sauronlotr-01-cast-trigger-amass-5-mill-5-then-reanimate-resolves-even-if-sauron-is-countered) · `oracle:Sauron, Lord of the Rings` · [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md)
- **mill-then-return:** Amass 5, mill five, then return: the five milled cards can be the target. (Sauron, Lord of the Rings) *fact · verified* — [sauronlotr-01](../interactions/sauron-lord-of-the-rings.md#sauronlotr-01-cast-trigger-amass-5-mill-5-then-reanimate-resolves-even-if-sauron-is-countered) · [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L44](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md)
- **beacon-tax:** Command Beacon puts Sauron in hand, so the next cast avoids commander tax and still triggers. (Command Beacon, Sauron, Lord of the Rings) *fact · high* — [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md) · `cr:903.8`
- **fanatic-chain:** A Metamorphosis Fanatic returned by Sauron triggers its own reanimation for a second creature. (Metamorphosis Fanatic, Sauron, Lord of the Rings) *fact · verified* — [sauronlotr-02](../interactions/sauron-lord-of-the-rings.md#sauronlotr-02-reanimation-chains-metamorphosis-fanatic-dance-of-the-dead-animate-dead-necromancy-reanimate) · [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md)
- **nazgul-nine:** Nazgûl allows up to nine copies; four is legal (registry exception row is official_card_rule, NOT_REQUIRED). (Nazgûl) *fact · verified* — [sauronlotr-04](../interactions/sauron-lord-of-the-rings.md#sauronlotr-04-four-nazgûl-are-legal-each-temptation-grows-every-wraith-once-per-nazgûl) · [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md)
- **anger-wonder-types:** Anger needs a Mountain and Wonder an Island while in the graveyard; the mana base keeps both types. (Anger, Wonder) *fact · verified* — [sauronlotr-05](../interactions/sauron-lord-of-the-rings.md#sauronlotr-05-anger-and-wonder-work-from-the-graveyard-if-you-control-a-mountain-or-island) · [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md)
- **living-death-order:** Living Death exiles, then sacrifices, then returns; tokens and Sauron don't come back. (Living Death) *fact · verified* — [sauronlotr-03](../interactions/sauron-lord-of-the-rings.md#sauronlotr-03-living-death-exile-sacrifice-return-tokens-and-sauron-dont-come-back)

## Tutors and recursion

- Tutor target **Archon of Cruelty** via Entomb, Buried Alive, Demonic Tutor, Vampiric Tutor *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md)
- Recursion: Reanimate, Animate Dead, Necromancy, Dance of the Dead, Victimize, Living Death, Persist, Grave Researcher // Reanimate, Too Greedily, Too Deep, Ripples of Undeath, Sneak Attack, Sauron, Lord of the Rings *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Mana Drain, Swan Song, Deadly Rollick, Feed the Swarm, Cyclonic Rift, Toxic Deluge, Blasphemous Act.
- **Protection:** Deflecting Swat, Lightning Greaves, Force of Will.
- **Mana:** 32 lands with Mountain and Island types for Anger/Wonder; fast mana.
- *strategic_judgment · moderate* — [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md)

## Failure modes

- **eight-drop:** Sauron costs eight; slow without fast mana. Mitigations: Mana Vault; Grim Monolith; Command Beacon. *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md)
- **graveyard-hate:** Graveyard hate stops the trigger's best mode and the backup reanimation. Mitigations: Sneak Attack; Hard-casting. *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md)
- **living-death-symmetry:** Living Death is symmetric. Mitigations: Set up the graveyard first. *strategic_judgment · moderate* — [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md)

## Identity core

- **Sauron, Lord of the Rings:** Cast trigger: amass, mill, reanimate. *fact · verified* — `oracle:Sauron, Lord of the Rings`
- **Command Beacon:** Avoids commander tax on an eight-drop. *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md)
- **Metamorphosis Fanatic:** Second reanimation off the trigger. *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md)
- **Entomb:** Sets up a target for one mana. *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md)
- **Anger:** Haste from the graveyard. *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No generic Oracle/Breach conversion (decisions L39).
- ✗ No Heartless Summoning (L38) or slow recursion engines (L36).
  - *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L39](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L38](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md)
- Theme: Reanimator / graveyard setup / amass Orcs (decisions L66).
  - *strategic_judgment · high* — [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md#L66](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 601.2i:** Cast triggers. *fact · verified* — `cr:601.2i`
- **CR 903.8:** Commander tax. *fact · verified* — `cr:903.8`
- **CR 701.54a:** The Ring tempts you. *fact · verified* — `cr:701.54a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Orc synergy", "graveyard as a resource"], "hooked_cards": 23, "role_counts": {"counter": 3, "draw": 14, "protection": 2, "ramp": 13, "removal": 5, "tutor": 4, "wipe": 2}, "lands": 32, "edhrec_pages": ["sauron-lord-of-the-rings"]}` *heuristic · low*

## Provenance

- Seeded from: [Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Sauron_Lord_of_the_Rings_Commander_Blueprint_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Sauron_Lord_of_the_Rings_Candidate_Decisions_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Sauron_Lord_of_the_Rings_Approved_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Sauron_Lord_of_the_Rings_Approval_Ready_Verification_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Sauron_Lord_of_the_Rings_Whole_List_Audit_2026-10-15.md) · [Sauron_Lord_of_the_Rings_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Sauron_Lord_of_the_Rings_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
