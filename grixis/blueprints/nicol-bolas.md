# Blueprint — Nicol Bolas

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/nicol-bolas.md), state `SOURCE_BASELINE`, list `lh1:f26970666b991249…`). Machine-readable source: [`data/grixis/blueprints/nicol-bolas.json`](../../data/grixis/blueprints/nicol-bolas.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Nicol Bolas** — Legendary Creature — Elder Dragon

> Flying  
> At the beginning of your upkeep, sacrifice Nicol Bolas unless you pay {U}{B}{R}.  
> Whenever Nicol Bolas deals damage to an opponent, that player discards their hand.

## Plan and commander role

- **Primary plan:** Ramp to an eight-mana UUBBRR commander, protect it, and have Bolas deal damage (combat or noncombat) to empty opponents' hands. Discard payoffs turn each hand wipe into cards, mana, permanents and life loss. *strategic_judgment · high*
- **Secondary:** Aggravated Assault + Sword of Feast and Famine as a repeatable extra-combat finisher; Torment of Hailfire and attrition with an emptied table.
  - Evidence: [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L24](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)
- **Commander role: central.** Bolas's damage-triggered hand wipe is the engine every damage enabler and discard payoff is built around. *strategic_judgment · high*
- ⚠️ **Honest note:** The identity is real but the commander is weak: 8 mana with UUBBRR, an {U}{B}{R} upkeep tax, and no command-zone combo (blueprint L57). The only Spellbook combo in the list is Sword of Feast and Famine + Aggravated Assault, which doesn't need him. Expect a slow, low-end Bracket 4 control deck. The cycle 51 M1 review (bolas-01..09) verifies the damage-source lines and flags Ignition hitting your own creatures (bolas-04).
  - Evidence: [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · `spellbook:900-3750`
- **Dependency level:** total *strategic_judgment · high* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L55](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling, low end: high-quality staples around a slow eight-drop with no commander combo. Agrees with the source.) | *strategic_judgment · high* | [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Nicol_Bolas` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 42, "2": 91, "3": 107, "4": 59, "5": 1}, "decks_with_bracket": 300, "share_b4_plus": 0.2, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__nicol-bolas.json`

## Win conditions

- **sword-assault** (combo): Sword of Feast and Famine + Aggravated Assault: infinite combats once a creature connects. Cards: Sword of Feast and Famine, Aggravated Assault. Enablers: Nicol Bolas. *fact · verified* — `spellbook:900-3750` · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)
- **discard-lock** (natural): Repeated whole-hand discard, then Bolas beats or Liliana's Caress, Raiders' Wake and Torment of Hailfire drain. Cards: Nicol Bolas, Liliana's Caress, Raiders' Wake, Torment of Hailfire. Enablers: Dragon Tempest, Ingris Stingerquill, Kediss, Emberclaw Familiar, Chandra's Ignition, Pain for All, Quicksilver Dagger, Viridian Longbow. *strategic_judgment · moderate* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L47](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)

## Engines

- **bolas-damage:** Nicol Bolas, Dragon Tempest, Ingris Stingerquill, Kediss, Emberclaw Familiar, Chandra's Ignition, Pain for All, Quicksilver Dagger, Viridian Longbow. Online when: Bolas in play and survives upkeep. *fact · high* — `oracle:Nicol Bolas` · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)
- **discard-payoffs:** Waste Not, Geth's Grimoire, Tergrid, God of Fright // Tergrid's Lantern, Tinybones, Bauble Burglar, Tinybones, Trinket Thief, Sangromancer, Liliana's Caress, Raiders' Wake. Online when: Opponents discard. *strategic_judgment · high* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:bolas-sourced-damage` | yes | 5 | Make Bolas himself deal damage, ideally outside combat. | 7: Dragon Tempest, Ingris Stingerquill, Kediss, Emberclaw Familiar, Chandra's Ignition, Pain for All, Quicksilver Dagger, Viridian Longbow | — | *strategic_judgment · high* | [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) |
| `pkg:discard-payoffs` | yes | 6 | Turn hand wipes into advantage. | 8: Waste Not, Geth's Grimoire, Tergrid, God of Fright // Tergrid's Lantern, Tinybones, Bauble Burglar, Tinybones, Trinket Thief, Sangromancer, Liliana's Caress, Raiders' Wake | — | *strategic_judgment · high* | [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L39](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) |
| `pkg:mana` | yes | 10 | Accelerate an eight-mana, triple-color commander. | 13: Sol Ring, Mana Vault, Grim Monolith, Chrome Mox, Mox Diamond, Dark Ritual, Cabal Ritual, Seething Song, Ancient Tomb, Arcane Signet, Talisman of Creativity, Talisman of Dominance, Talisman of Indulgence | — | *strategic_judgment · high* | [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) |
| `pkg:protection` | yes | 5 | Protect the eight-drop. | 8: Lightning Greaves, Swiftfoot Boots, Brotherhood Regalia, Cavern of Souls, Command Beacon, Fierce Guardianship, Deflecting Swat, Force of Will | — | *strategic_judgment · high* | [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) |

## Key interactions

- **any-damage:** The discard trigger fires on damage of any kind, not only combat damage. (Nicol Bolas) *fact · verified* — [bolas-01](../interactions/nicol-bolas.md#bolas-01-nicol-bolas-any-damage-to-an-opponent-empties-that-hand-the-upkeep-tax-and-command-beacon) · `oracle:Nicol Bolas` · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)
- **ingris-pre-blocks:** Ingris makes Nicol deal 1 to each opponent when he attacks, so they discard before blockers. (Ingris Stingerquill, Nicol Bolas) *fact · verified* — [bolas-02](../interactions/nicol-bolas.md#bolas-02-ingris-kediss-and-dragon-tempest-make-nicol-the-source-of-table-wide-damage) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)
- **tergrid-tinybones-order:** Tergrid and Tinybones, Bauble Burglar both trigger on a discarded permanent; their controller chooses the order. (Tergrid, God of Fright // Tergrid's Lantern, Tinybones, Bauble Burglar) *fact · verified* — [bolas-06](../interactions/nicol-bolas.md#bolas-06-tinybones-bauble-burglar-vs-tergrid-on-the-same-discarded-permanent) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)
- **upkeep-tax:** Pay {U}{B}{R} each upkeep or sacrifice Bolas. (Nicol Bolas) *fact · verified* — [bolas-01](../interactions/nicol-bolas.md#bolas-01-nicol-bolas-any-damage-to-an-opponent-empties-that-hand-the-upkeep-tax-and-command-beacon) · `oracle:Nicol Bolas` · `cr:603.3b`
- **ignition-self-sweep:** M1 flag: Chandra's Ignition also hits your own creatures, including Ingris, Kediss and Sangromancer. (Chandra's Ignition, Ingris Stingerquill, Kediss, Emberclaw Familiar, Sangromancer) *strategic_judgment · moderate* — [bolas-04](../interactions/nicol-bolas.md#bolas-04-chandras-ignition-also-hits-your-own-creatures)
- **creature-is-source:** With Ignition, Pain for All, Quicksilver Dagger, Viridian Longbow and Curiosity, Nicol is the damage source, so the discard triggers. (Nicol Bolas, Chandra's Ignition, Pain for All, Quicksilver Dagger, Viridian Longbow) *fact · verified* — [bolas-03](../interactions/nicol-bolas.md#bolas-03-chandras-ignition-pain-for-all-quicksilver-dagger-viridian-longbow-and-curiosity-the-creature-is-the-source)
- **no-mercy-symmetric:** No Mercy is symmetric toward your own creatures. (No Mercy) *fact · verified* — [bolas-09](../interactions/nicol-bolas.md#bolas-09-no-mercy-is-symmetric-toward-your-own-creatures-canonical-list-keeps-no-mercy-not-megrim)

## Tutors and recursion

- Tutor target **Dragon Tempest** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)
- Tutor target **Aggravated Assault** via Demonic Tutor *strategic_judgment · moderate* — `spellbook:900-3750`
- Recursion: Jeska's Will, Tergrid, God of Fright // Tergrid's Lantern, Shizo, Death's Storehouse *strategic_judgment · low* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Mana Drain, Counterspell, Terminate, Sheoldred's Edict, Chaos Warp, Toxic Deluge, Cyclonic Rift.
- **Protection:** Boots, Greaves, Regalia, Cavern, Command Beacon.
- **Mana:** High-quality UUBBRR mana plus rituals.
- *strategic_judgment · high* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)

## Failure modes

- **eight-drop-removed:** Losing an eight-mana commander before it deals damage is catastrophic. Mitigations: Protection package; Command Beacon. *strategic_judgment · high* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)
- **upkeep-cost:** The upkeep tax delays the rest of the game plan. Mitigations: Mana density. *strategic_judgment · high* — `oracle:Nicol Bolas`
- **no-combo:** No deterministic commander win; fast combo tables outrace it. Mitigations: Free counters. *strategic_judgment · moderate* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)

## Identity core

- **Nicol Bolas:** Damage → whole-hand discard. *fact · verified* — `oracle:Nicol Bolas`
- **Dragon Tempest:** Haste plus immediate damage on entry. *strategic_judgment · high* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)
- **Kediss, Emberclaw Familiar:** One hit spreads to the whole table. *strategic_judgment · high* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)
- **Chandra's Ignition:** 7 to each opponent and a creature sweep. *strategic_judgment · high* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)
- **Waste Not:** Each discard becomes value. *strategic_judgment · high* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ Don't import Bolas planeswalkers; they belong to deck #42 (blueprint L61).
- ✗ Not a generic Grixis combo shell.
  - *strategic_judgment · high* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L61](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)
- Theme: Discard / commander damage / control (blueprint L63).
  - *strategic_judgment · high* — [Nicol_Bolas_Commander_Blueprint_2026-10-15.md#L63](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 120.3:** Results of damage dealt; damage from any source triggers Bolas. *fact · verified* — `cr:120.3`
- **CR 603.3b:** Ordering Tergrid/Tinybones triggers. *fact · verified* — `cr:603.3b`

## Supporting features (heuristic, not identity)

- `{"hooks": ["combat damage / attack triggers", "discard", "sacrifice"], "hooked_cards": 25, "role_counts": {"counter": 4, "draw": 9, "protection": 4, "ramp": 18, "removal": 8, "tutor": 2, "wipe": 2}, "lands": 37, "edhrec_pages": ["nicol-bolas"]}` *heuristic · low*

## Provenance

- Seeded from: [Nicol_Bolas_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Nicol_Bolas_Commander_Blueprint_2026-10-15.md) · [Nicol_Bolas_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Nicol_Bolas_Candidate_Decisions_2026-10-15.md) · [Nicol_Bolas_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Nicol_Bolas_Approved_2026-10-15.md) · [Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Approval_Ready_Verification_2026-10-15.md) · [Nicol_Bolas_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Nicol_Bolas_Whole_List_Audit_2026-10-15.md) · [Nicol_Bolas_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Nicol_Bolas_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
