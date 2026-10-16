# Blueprint — Gwendlyn Di Corci

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/gwendlyn-di-corci.md), state `SOURCE_BASELINE`, list `lh1:c2a52fd405d5eba4…`). Machine-readable source: [`data/grixis/blueprints/gwendlyn-di-corci.json`](../../data/grixis/blueprints/gwendlyn-di-corci.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Gwendlyn Di Corci** — Legendary Creature — Human Rogue

> {T}: Target player discards a card at random. Activate only during your turn.

## Plan and commander role

- **Primary plan:** Make Gwendlyn a repeatable random-discard engine: haste her, then untap her (Pemmin's Aura, Minamo, Magewright's Stone, Patriar's Seal) and copy her ability (Illusionist's Bracers) to strip hands while discard punishers (Waste Not, Liliana's Caress, Geth's Grimoire, Tinybones) pay off. *strategic_judgment · high*
- **Secondary:** Wheels refill opposing hands to strip again and punish draws (Sheoldred, Bowmasters, Underworld Dreams); Chains, Notion Thief and Opposition Agent deny resources; Breach + LED + Wheel of Fortune as a compact finish.
  - Evidence: [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md) · [gwendlyn-03](../interactions/gwendlyn-di-corci.md#gwendlyn-03-untappers-pemmins-aura-minamo-magewrights-stone-patriars-seal) · [gwendlyn-05](../interactions/gwendlyn-di-corci.md#gwendlyn-05-discard-payoffs-per-card-vs-per-event)
- **Commander role: central.** Every untapper and Bracers exists only to multiply Gwendlyn's activation. *strategic_judgment · high*
- ⚠️ **Honest note:** She is a four-mana tap ability that discards one random card, on your turn only and with summoning sickness (M1 gwendlyn-01). Without haste and untappers she's slow, and most of the damage comes from wheels plus punishers, which work without her.
  - Evidence: [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md) · [gwendlyn-01](../interactions/gwendlyn-di-corci.md#gwendlyn-01-tap-ability-your-turn-only-and-summoning-sickness-applies)
- **Dependency level:** medium *strategic_judgment · high* — [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Bracket 4 — Optimized (decisions natural ceiling).) | *fact · verified* | [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: oppressive discard-control with a premium card pool, but a four-mana one-card-per-tap commander and one compact combo. Agrees with the source.) | *strategic_judgment · high* | [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md) · [gwendlyn-01](../interactions/gwendlyn-di-corci.md#gwendlyn-01-tap-ability-your-turn-only-and-summoning-sickness-applies) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Gwendlyn_Di_Corci` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 15, "2": 20, "3": 25, "4": 31, "5": 3}, "decks_with_bracket": 94, "share_b4_plus": 0.362, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__gwendlyn-di-corci.json`

## Win conditions

- **punisher-wheels** (natural): Wheels and repeated discards trigger Waste Not, Caress, Tinybones, Sheoldred, Bowmasters and Underworld Dreams. Cards: Wheel of Fortune, Windfall, Timetwister, Waste Not, Liliana's Caress, Sheoldred, the Apocalypse, Underworld Dreams, Tinybones, Bauble Burglar. Enablers: Gwendlyn Di Corci. *strategic_judgment · high* — [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md) · [gwendlyn-05](../interactions/gwendlyn-di-corci.md#gwendlyn-05-discard-payoffs-per-card-vs-per-event)
- **breach-led-wheel** (combo): Underworld Breach + Lion's Eye Diamond + Wheel of Fortune. Cards: Underworld Breach, Lion's Eye Diamond, Wheel of Fortune. *fact · verified* — `spellbook:1368-2706-3518` · [gwendlyn-10](../interactions/gwendlyn-di-corci.md#gwendlyn-10-underworld-breach--led--wheel-of-fortune)
- **empty-hand-lock** (natural): Hellbent opponents locked by Oppression, Bottomless Pit and Chains lose to any pressure. Cards: Oppression, Bottomless Pit, Chains of Mephistopheles, Notion Thief. Enablers: Gwendlyn Di Corci. *strategic_judgment · moderate* — [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md)

## Engines

- **untap-discard:** Gwendlyn Di Corci, Illusionist's Bracers, Pemmin's Aura, Minamo, School at Water's Edge, Magewright's Stone, Patriar's Seal, Thousand-Year Elixir. Online when: Gwendlyn untapped, not summoning sick, on your turn. *fact · verified* — [gwendlyn-02](../interactions/gwendlyn-di-corci.md#gwendlyn-02-illusionists-bracers-copies-each-activation) · [gwendlyn-03](../interactions/gwendlyn-di-corci.md#gwendlyn-03-untappers-pemmins-aura-minamo-magewrights-stone-patriars-seal)
- **discard-payoffs:** Waste Not, Liliana's Caress, Geth's Grimoire, Tinybones, Pocket Nuisance, Tinybones, Bauble Burglar, Tinybones, Trinket Thief, Tergrid, God of Fright // Tergrid's Lantern. Online when: Opponents discard. *fact · verified* — [gwendlyn-05](../interactions/gwendlyn-di-corci.md#gwendlyn-05-discard-payoffs-per-card-vs-per-event) · [gwendlyn-08](../interactions/gwendlyn-di-corci.md#gwendlyn-08-tergrid-takes-discarded-permanent-cards)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:untap-copy` | yes | 6 | More activations per turn. | 7: Illusionist's Bracers, Pemmin's Aura, Minamo, School at Water's Edge, Magewright's Stone, Patriar's Seal, Thousand-Year Elixir, Lightning Greaves | — | *strategic_judgment · high* | [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md) · [gwendlyn-03](../interactions/gwendlyn-di-corci.md#gwendlyn-03-untappers-pemmins-aura-minamo-magewrights-stone-patriars-seal) |
| `pkg:wheels` | yes | 6 | Refill and strip opposing hands. | 8: Wheel of Fortune, Wheel of Misfortune, Windfall, Timetwister, Dark Deal, Reforge the Soul, Jace's Archivist, Magus of the Wheel | — | *strategic_judgment · high* | [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:punishers` | yes | 6 | Turn discards and draws into damage and value. | 9: Waste Not, Liliana's Caress, Geth's Grimoire, Tinybones, Pocket Nuisance, Tinybones, Bauble Burglar, Sheoldred, the Apocalypse, Orcish Bowmasters, Underworld Dreams, Tergrid, God of Fright // Tergrid's Lantern | — | *strategic_judgment · high* | [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md) · [gwendlyn-05](../interactions/gwendlyn-di-corci.md#gwendlyn-05-discard-payoffs-per-card-vs-per-event) |

## Key interactions

- **your-turn-sick:** Her tap ability is your turn only and needs haste the turn she lands. (Gwendlyn Di Corci, Lightning Greaves, Thousand-Year Elixir) *fact · verified* — [gwendlyn-01](../interactions/gwendlyn-di-corci.md#gwendlyn-01-tap-ability-your-turn-only-and-summoning-sickness-applies)
- **shroud-untappers:** Shroud on Gwendlyn blocks Minamo, Stone, Seal and Bracers' equip, but not Pemmin's own untap. (Lightning Greaves, Pemmin's Aura, Minamo, School at Water's Edge) *fact · verified* — [gwendlyn-04](../interactions/gwendlyn-di-corci.md#gwendlyn-04-shroud-on-gwendlyn-turns-off-the-targeted-untappers-but-not-pemmins-own-untap)
- **per-card-vs-event:** Caress and Grimoire trigger per card; Tinybones once per discard event. (Liliana's Caress, Geth's Grimoire, Tinybones, Pocket Nuisance) *fact · verified* — [gwendlyn-05](../interactions/gwendlyn-di-corci.md#gwendlyn-05-discard-payoffs-per-card-vs-per-event)
- **chains-wheels:** Chains turns wheel draws after an empty hand into mills, for you too. (Chains of Mephistopheles, Wheel of Fortune) *fact · verified* — [gwendlyn-06](../interactions/gwendlyn-di-corci.md#gwendlyn-06-chains-of-mephistopheles-hits-wheels-yours-included)
- **no-mindcrank:** Bloodchief Ascension has no Mindcrank loop in this list. (Bloodchief Ascension) *fact · verified* — [gwendlyn-09](../interactions/gwendlyn-di-corci.md#gwendlyn-09-bloodchief-ascension-has-no-mindcrank-loop-here)

## Tutors and recursion

- Tutor target **Illusionist's Bracers** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md)
- Tutor target **Underworld Breach** via Demonic Tutor, Gamble, Imperial Seal *strategic_judgment · moderate* — `spellbook:1368-2706-3518`
- Recursion: Kess, Dissident Mage, Underworld Breach, Yawgmoth's Will, Dream Salvage *strategic_judgment · moderate* — [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Free counters (Force of Will, Force of Negation, Fierce Guardianship), Mana Drain, Toxic Deluge, Cyclonic Rift.
- **Protection:** Lightning Greaves, Pemmin's Aura shroud, Deflecting Swat.
- **Mana:** Fast mana (Sol Ring, Chrome Mox, Lotus Petal, Ancient Tomb, Dark Ritual) for a four-mana commander.
- *strategic_judgment · moderate* — [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **slow-engine:** One random discard per tap is slow without untappers. Mitigations: Untap package; Wheels and punishers. *strategic_judgment · high* — [gwendlyn-01](../interactions/gwendlyn-di-corci.md#gwendlyn-01-tap-ability-your-turn-only-and-summoning-sickness-applies)
- **chains-self:** Chains mills you on your own wheels. Mitigations: Sequence wheels with Chains off. *strategic_judgment · moderate* — [gwendlyn-06](../interactions/gwendlyn-di-corci.md#gwendlyn-06-chains-of-mephistopheles-hits-wheels-yours-included)
- **empty-hands:** Opponents empty their hands fast, leaving Gwendlyn nothing to hit. Mitigations: Wheels refill; Oppression/Bottomless Pit lock. *strategic_judgment · moderate* — [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md)

## Identity core

- **Gwendlyn Di Corci:** Repeatable random discard on your turn. *fact · verified* — `oracle:Gwendlyn Di Corci`
- **Illusionist's Bracers:** Copies each activation: two discards per tap. *strategic_judgment · high* — [gwendlyn-02](../interactions/gwendlyn-di-corci.md#gwendlyn-02-illusionists-bracers-copies-each-activation)
- **Pemmin's Aura:** Untap per blue mana, plus shroud. *strategic_judgment · high* — [gwendlyn-03](../interactions/gwendlyn-di-corci.md#gwendlyn-03-untappers-pemmins-aura-minamo-magewrights-stone-patriars-seal)
- **Waste Not:** Turns every discard into mana, Zombies or cards. *strategic_judgment · high* — [gwendlyn-05](../interactions/gwendlyn-di-corci.md#gwendlyn-05-discard-payoffs-per-card-vs-per-event)
- **Mind Twist:** Scalable random discard that mirrors the commander. *strategic_judgment · moderate* — [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md)

## Anti-goals and thematic constraints

- ✗ No generic Grixis Thoracle/Breach turbo conversion (decisions L28).
- ✗ Prefer cards that raise Gwendlyn's activation rate over generic discard bodies (decisions swaps).
  - *strategic_judgment · high* — [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Random discard and hand denial: the Rogue who empties hands.
  - *strategic_judgment · moderate* — [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 302.6:** Summoning sickness stops a creature's {T} abilities. *fact · verified* — `cr:302.6`
- **CR 701.9b:** Random discard. *fact · verified* — `cr:701.9b`

## Supporting features (heuristic, not identity)

- `{"hooks": ["discard"], "hooked_cards": 24, "role_counts": {"counter": 6, "draw": 19, "protection": 3, "ramp": 10, "removal": 4, "tutor": 5, "wipe": 1}, "lands": 35, "edhrec_pages": ["gwendlyn-di-corci"]}` *heuristic · low*

## Provenance

- Seeded from: [Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Gwendlyn_Di_Corci_Current_Cycle_Decisions_2026-10-14.md) · [Gwendlyn_Di_Corci_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Gwendlyn_Di_Corci_Approved_2026-10-14.md) · [Gwendlyn_Di_Corci_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Gwendlyn_Di_Corci_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
