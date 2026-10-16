# Blueprint — Abaddon the Despoiler

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/abaddon-the-despoiler.md), state `SOURCE_BASELINE`, list `lh1:5a1e5e5bb86ba35d…`). Machine-readable source: [`data/grixis/blueprints/abaddon-the-despoiler.json`](../../data/grixis/blueprints/abaddon-the-despoiler.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Abaddon the Despoiler** — Legendary Creature — Astartes Warrior

> Trample  
> Mark of Chaos Ascendant — During your turn, spells you cast from your hand with mana value X or less have cascade, where X is the total amount of life your opponents have lost this turn.

## Plan and commander role

- **Primary plan:** Raise the same-turn opponent life-loss total with cheap damage and drain, then cast spells from hand at or under that total so Abaddon grants cascade; chain cascade hits and cast-from-exile payoffs into a large value or damage turn. *strategic_judgment · high*
- **Secondary:** Compact Underworld Breach loops (Lion's Eye Diamond or Lotus Petal + Brain Freeze, or Wheel of Fortune) backed by fast mana, tutors and free counters.
  - Evidence: [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) · [abaddon-01](../interactions/abaddon-the-despoiler.md#abaddon-01-abaddons-threshold-counts-life-opponents-actually-lost-this-turn) · [abaddon-02](../interactions/abaddon-the-despoiler.md#abaddon-02-only-spells-cast-from-your-hand-during-your-turn-get-cascade) · [abaddon-28](../interactions/abaddon-the-despoiler.md#abaddon-28-what-the-list-depends-on)
- **Commander role: central.** Abaddon is the cascade engine: without him, hand-cast spells get no cascade and the exile-cast payoffs (Prosper, Nalfeshnee, Keeper of Secrets, Passionate Archaeologist) mostly go quiet. The Breach line works without him. *strategic_judgment · high*
- ⚠️ **Honest note:** The threshold resets every turn and only counts life opponents actually lost this turn, so the engine is turn-local and five mana; the Breach combo is the faster kill and is commander-independent.
  - Evidence: [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) · [abaddon-01](../interactions/abaddon-the-despoiler.md#abaddon-01-abaddons-threshold-counts-life-opponents-actually-lost-this-turn) · [abaddon-03](../interactions/abaddon-the-despoiler.md#abaddon-03-eligibility-is-checked-as-the-spell-is-cast-later-life-loss-cant-add-cascade) · [abaddon-14](../interactions/abaddon-the-despoiler.md#abaddon-14-cast-from-exile-payoffs-see-cascade-hits-but-not-copies) · [abaddon-28](../interactions/abaddon-the-despoiler.md#abaddon-28-what-the-list-depends-on)
- **Dependency level:** high *strategic_judgment · high* — [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) · [abaddon-28](../interactions/abaddon-the-despoiler.md#abaddon-28-what-the-list-depends-on)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Bracket 4 — Optimized (provisional; compact combo can threaten higher)) | *fact · verified* | [Abaddon_the_Despoiler_v1.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) |
| GrokBot estimated ceiling | 4 (Bracket 4, high end: a cEDH-grade card pool (fast mana, free counters, Breach + LED) around a five-mana, turn-local engine. Agrees with the source.) | *strategic_judgment · high* | [Abaddon_the_Despoiler_v1.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) · [abaddon-20](../interactions/abaddon-the-despoiler.md#abaddon-20-underworld-breach--lions-eye-diamond--brain-freeze) · [abaddon-28](../interactions/abaddon-the-despoiler.md#abaddon-28-what-the-list-depends-on) · `spellbook:1368-3518-4856` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Abaddon_the_Despoiler` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 21, "2": 759, "3": 547, "4": 163, "5": 35}, "decks_with_bracket": 1525, "share_b4_plus": 0.13, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__abaddon-the-despoiler.json`

## Win conditions

- **cascade-value-turn** (natural): A turn of chained cascades and exile casts (Prosper Treasures, Nalfeshnee copies, Keeper of Secrets/Lost and the Damned bodies) that overwhelms on cards and damage. Cards: Abaddon the Despoiler, Prosper, Tome-Bound, Nalfeshnee, The Lost and the Damned, Keeper of Secrets. Enablers: Boltwave, Flame Rift, Thermo-Alchemist. *strategic_judgment · high* — [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) · [abaddon-14](../interactions/abaddon-the-despoiler.md#abaddon-14-cast-from-exile-payoffs-see-cascade-hits-but-not-copies) · [abaddon-24](../interactions/abaddon-the-despoiler.md#abaddon-24-storm-counts-cascade-hits-and-escapes-copies-count-for-magecraft-only)
- **amplified-burn** (natural): Solphim doubles damage and Bloodletter doubles the resulting life loss, so cheap burn becomes lethal table damage (Boltwave → 12 per opponent). Cards: Solphim, Mayhem Dominus, Bloodletter of Aclazotz, Boltwave, Flame Rift, Delayed Blast Fireball. Enablers: Kessig Flamebreather, Exalted Flamer of Tzeentch. *strategic_judgment · high* — [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) · [abaddon-10](../interactions/abaddon-the-despoiler.md#abaddon-10-bloodletter-and-solphim-modify-different-events)
- **breach-brain-freeze** (combo): Underworld Breach + Lion's Eye Diamond (or Lotus Petal) + Brain Freeze escape loop; milling alone doesn't win, a Wheel/Windfall finishes opponents. Cards: Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze. Enablers: Wheel of Fortune, Windfall. *fact · verified* — [abaddon-20](../interactions/abaddon-the-despoiler.md#abaddon-20-underworld-breach--lions-eye-diamond--brain-freeze) · [abaddon-21](../interactions/abaddon-the-despoiler.md#abaddon-21-breach--lotus-petal--brain-freeze) · `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856`
- **breach-wheel** (combo): Underworld Breach + Wheel of Fortune with Lion's Eye Diamond or Jeska's Will: repeated wheels deck the table. Cards: Underworld Breach, Wheel of Fortune, Lion's Eye Diamond, Jeska's Will. *fact · verified* — [abaddon-22](../interactions/abaddon-the-despoiler.md#abaddon-22-breach--wheel-of-fortune--led-or-jeskas-will) · `spellbook:1368-2706-3518` · `spellbook:1368-1878-2706`

## Engines

- **life-loss-threshold:** Thermo-Alchemist, Kessig Flamebreather, Exalted Flamer of Tzeentch, Loyal Subordinate, Noise Marine, Neheb, the Eternal. Online when: At least one opponent has lost life this turn before the key spell is cast from hand; X is the total lost. *strategic_judgment · high* — [abaddon-01](../interactions/abaddon-the-despoiler.md#abaddon-01-abaddons-threshold-counts-life-opponents-actually-lost-this-turn) · [abaddon-11](../interactions/abaddon-the-despoiler.md#abaddon-11-upkeep-and-combat-life-loss-open-the-threshold-early) · [abaddon-12](../interactions/abaddon-the-despoiler.md#abaddon-12-neheb-converts-the-turns-life-loss-into-post-combat-mana)
- **exile-cast-payoffs:** Prosper, Tome-Bound, Nalfeshnee, Wild-Magic Sorcerer, Passionate Archaeologist, The Lost and the Damned, Keeper of Secrets. Online when: Cascade hits are cast from exile; copies do not trigger them. *fact · verified* — [abaddon-14](../interactions/abaddon-the-despoiler.md#abaddon-14-cast-from-exile-payoffs-see-cascade-hits-but-not-copies) · [abaddon-16](../interactions/abaddon-the-despoiler.md#abaddon-16-wild-magic-sorcerer-only-the-first-exile-cast-each-turn-cascades) · [abaddon-17](../interactions/abaddon-the-despoiler.md#abaddon-17-nalfeshnee-copies-exile-casts-permanent-copies-are-hasty-temporary-tokens)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:threshold-enablers` | yes | 8 | Cheap damage/drain to open the cascade threshold early in the turn. | 9: Boltwave, Flame Rift, Thermo-Alchemist, Kessig Flamebreather, Exalted Flamer of Tzeentch, Loyal Subordinate, Noise Marine, Nightscape Familiar, Rakdos, Lord of Riots | Poxwalkers | *strategic_judgment · high* | [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) |
| `pkg:cascade-spells` | yes | 4 | Spells with printed cascade or cheap value that Abaddon's granted cascade stacks with. | 5: Ancestral Vision, Profane Tutor, Inevitable Betrayal, Bituminous Blast, Call Forth the Tempest | Aurora Phoenix, Deny Reality | *strategic_judgment · high* | [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) |
| `pkg:exile-payoffs` | yes | 5 | Turn cascade/exile casts into cards, mana and bodies. | 7: Prosper, Tome-Bound, Nalfeshnee, Wild-Magic Sorcerer, Passionate Archaeologist, The Lost and the Damned, Keeper of Secrets, The Ruinous Powers | — | *strategic_judgment · high* | [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) · [abaddon-14](../interactions/abaddon-the-despoiler.md#abaddon-14-cast-from-exile-payoffs-see-cascade-hits-but-not-copies) |
| `pkg:breach-combo` | optional | 3 | Commander-independent compact kill. | 6: Underworld Breach, Lion's Eye Diamond, Lotus Petal, Brain Freeze, Wheel of Fortune, Jeska's Will | — | *fact · verified* | [abaddon-20](../interactions/abaddon-the-despoiler.md#abaddon-20-underworld-breach--lions-eye-diamond--brain-freeze) · [abaddon-22](../interactions/abaddon-the-despoiler.md#abaddon-22-breach--wheel-of-fortune--led-or-jeskas-will) |
| `pkg:free-interaction` | yes | 5 | Protect the combo turn and the engine turn at no mana. | 8: Force of Will, Force of Negation, Fierce Guardianship, Pact of Negation, Deflecting Swat, Flusterstorm, Swan Song, Pyroblast | — | *strategic_judgment · high* | [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) |

## Key interactions

- **threshold-timing:** X counts life opponents lost this turn and is checked as the spell is cast; a spell's own damage can't give it cascade. (Abaddon the Despoiler) *fact · verified* — [abaddon-01](../interactions/abaddon-the-despoiler.md#abaddon-01-abaddons-threshold-counts-life-opponents-actually-lost-this-turn) · [abaddon-03](../interactions/abaddon-the-despoiler.md#abaddon-03-eligibility-is-checked-as-the-spell-is-cast-later-life-loss-cant-add-cascade)
- **hand-only:** Only spells cast from hand on your turn get cascade; exile, graveyard and command-zone casts never do. (Abaddon the Despoiler, Underworld Breach) *fact · verified* — [abaddon-02](../interactions/abaddon-the-despoiler.md#abaddon-02-only-spells-cast-from-your-hand-during-your-turn-get-cascade) · [abaddon-09](../interactions/abaddon-the-despoiler.md#abaddon-09-cards-without-a-mana-cost-cascade-hits-never-abaddon-casts)
- **zero-mv-randomizes:** 0-MV spells always qualify and their cascade randomizes the library, which can bury a tutored top card. (Lion's Eye Diamond, Lotus Petal, Chrome Mox, Pact of Negation, Vampiric Tutor, Mystical Tutor) *fact · verified* — [abaddon-06](../interactions/abaddon-the-despoiler.md#abaddon-06-a-stacked-top-card-is-exposed-to-every-later-cascade-on-your-turn) · [abaddon-07](../interactions/abaddon-the-despoiler.md#abaddon-07-mana-value-0-spells-always-qualify-and-their-cascade-randomizes-your-library)
- **double-cascade:** Granted cascade stacks with printed cascade (Bituminous Blast twice). (Bituminous Blast, Call Forth the Tempest) *fact · verified* — [abaddon-08](../interactions/abaddon-the-despoiler.md#abaddon-08-granted-cascade-stacks-with-printed-cascade)
- **solphim-bloodletter:** Solphim doubles damage, Bloodletter doubles the resulting life loss. (Solphim, Mayhem Dominus, Bloodletter of Aclazotz) *fact · verified* — [abaddon-10](../interactions/abaddon-the-despoiler.md#abaddon-10-bloodletter-and-solphim-modify-different-events)

## Tutors and recursion

- Tutor target **Underworld Breach** via Demonic Tutor, Vampiric Tutor, Gamble, Imperial Seal *strategic_judgment · high* — [abaddon-20](../interactions/abaddon-the-despoiler.md#abaddon-20-underworld-breach--lions-eye-diamond--brain-freeze) · [abaddon-06](../interactions/abaddon-the-despoiler.md#abaddon-06-a-stacked-top-card-is-exposed-to-every-later-cascade-on-your-turn)
- Tutor target **Lion's Eye Diamond** via Demonic Tutor, Vampiric Tutor, Profane Tutor *strategic_judgment · moderate* — [abaddon-20](../interactions/abaddon-the-despoiler.md#abaddon-20-underworld-breach--lions-eye-diamond--brain-freeze)
- Tutor target **Solphim, Mayhem Dominus** via Demonic Tutor, Profane Tutor *strategic_judgment · moderate* — [abaddon-10](../interactions/abaddon-the-despoiler.md#abaddon-10-bloodletter-and-solphim-modify-different-events)
- Recursion: Underworld Breach, Mind's Desire *strategic_judgment · moderate* — [abaddon-20](../interactions/abaddon-the-despoiler.md#abaddon-20-underworld-breach--lions-eye-diamond--brain-freeze) · [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md)

## Requirements

- **Interaction:** Heavy free/cheap stack interaction (8 counters/pitch spells) to force through the engine or the Breach turn; light board removal.
- **Protection:** Abaddon has no built-in protection; the free counters double as protection; recasting at 7+ mana is slow.
- **Mana:** Fast mana and rituals (Mana Vault, Chrome Mox, Dark Ritual, Lotus Petal, Ancient Tomb) to cast a five-drop early and still hold up spells; 30+ lands-equivalent with rocks.
- *strategic_judgment · high* — [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) · [abaddon-26](../interactions/abaddon-the-despoiler.md#abaddon-26-commander-tax-and-recasting-abaddon) · [abaddon-28](../interactions/abaddon-the-despoiler.md#abaddon-28-what-the-list-depends-on)

## Failure modes

- **no-commander:** Abaddon is not on the battlefield, so nothing cascades. Mitigations: Breach combo is commander-independent; Free counters protect him. *strategic_judgment · high* — [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md)
- **low-threshold:** Too little life loss this turn leaves high-MV spells without cascade. Mitigations: Cheap pingers and drains before the main spell; Neheb converts life loss into mana. *strategic_judgment · high* — [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) · [abaddon-03](../interactions/abaddon-the-despoiler.md#abaddon-03-eligibility-is-checked-as-the-spell-is-cast-later-life-loss-cant-add-cascade)
- **self-randomize:** A 0-MV cascade randomizes the library and can bottom a tutored card. Mitigations: Sequence top-of-library tutors after 0-MV casts. *fact · verified* — [abaddon-07](../interactions/abaddon-the-despoiler.md#abaddon-07-mana-value-0-spells-always-qualify-and-their-cascade-randomizes-your-library) · [abaddon-06](../interactions/abaddon-the-despoiler.md#abaddon-06-a-stacked-top-card-is-exposed-to-every-later-cascade-on-your-turn)
- **clunky-top-end:** Too many expensive cascade payoffs make hands slow and random. Mitigations: Keep the payoff count near the current 7. *strategic_judgment · moderate* — [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md)

## Identity core

- **Abaddon the Despoiler:** The commander is the cascade source; the deck has no other way to give hand-cast spells cascade. *fact · verified* — `oracle:Abaddon the Despoiler`
- **Solphim, Mayhem Dominus:** Doubles every point of noncombat damage, which doubles the threshold and the burn finish. *strategic_judgment · high* — [abaddon-10](../interactions/abaddon-the-despoiler.md#abaddon-10-bloodletter-and-solphim-modify-different-events)
- **Prosper, Tome-Bound:** Turns every cascade hit into Treasure, paying for the next spell in the chain. *strategic_judgment · high* — [abaddon-14](../interactions/abaddon-the-despoiler.md#abaddon-14-cast-from-exile-payoffs-see-cascade-hits-but-not-copies)
- **Nalfeshnee:** Copies exile casts, adding a second cascade-hit resolution per hit. *strategic_judgment · high* — [abaddon-17](../interactions/abaddon-the-despoiler.md#abaddon-17-nalfeshnee-copies-exile-casts-permanent-copies-are-hasty-temporary-tokens)
- **Thermo-Alchemist:** Repeatable cheap ping that opens the threshold every turn without spending a card. *strategic_judgment · moderate* — [abaddon-11](../interactions/abaddon-the-despoiler.md#abaddon-11-upkeep-and-combat-life-loss-open-the-threshold-early)

## Anti-goals and thematic constraints

- ✗ Don't turn the list into a generic Grixis turbo-Breach shell that ignores the cascade engine.
- ✗ Don't add expensive cascade hits that brick (Blood for the Blood God! deferred by the source).
- ✗ Don't label it cEDH just because it contains a cEDH-capable combo.
  - *strategic_judgment · high* — [Abaddon_the_Despoiler_v1.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) · [Abaddon_the_Despoiler_v1.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md)
- Theme: Warhammer 40,000 Chaos flavor (Tzeentch, Slaanesh, Khorne pieces) is welcome but not binding.
  - *strategic_judgment · low* — [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.85c:** Multiple instances of cascade trigger separately (granted + printed). *fact · verified* — `cr:702.85c`
- **CR 903.8:** Commander tax makes recasting a five-drop expensive; protect the first cast. *fact · verified* — `cr:903.8`

## Supporting features (heuristic, not identity)

- `{"hooks": ["cascade / cheap spells", "opponents losing life"], "hooked_cards": 15, "role_counts": {"counter": 7, "draw": 7, "protection": 1, "ramp": 16, "removal": 3, "tutor": 6, "wipe": 2}, "lands": 34, "edhrec_pages": ["abaddon-the-despoiler"]}` *heuristic · low*

## Provenance

- Seeded from: [Abaddon_the_Despoiler_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Abaddon_the_Despoiler_v1.md) · [Abaddon_the_Despoiler_Approved_2026-10-13.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Abaddon_the_Despoiler_Approved_2026-10-13.txt) · [Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) · [abaddon-28](../interactions/abaddon-the-despoiler.md#abaddon-28-what-the-list-depends-on)
- Reviewed by: — (not yet reviewed by Cory)
