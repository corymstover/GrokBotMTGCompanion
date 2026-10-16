# Blueprint — The Madcap Jester

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/the-madcap-jester.md), state `PENDING_RELEASE`, list `lh1:5c53783a710fc838…`). Machine-readable source: [`data/grixis/blueprints/the-madcap-jester.json`](../../data/grixis/blueprints/the-madcap-jester.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**The Madcap Jester** — Legendary Creature — Clown Wizard

> Whenever The Madcap Jester attacks, each opponent exiles the top card of their library.  
> Whenever a spell or ability you control causes one or more cards to be exiled from an opponent's library, you may play those cards until the end of your next turn. Mana of any type can be spent to cast spells this way.

## Plan and commander role

- **Primary plan:** Exile theft into compact Grixis wins: library-exile effects (Extract, Tasha's Hideous Laughter, Ashiok, Jester's Cap) become tutors and card draw under the Jester's play permission, protected by free counters, and the deck closes with Thassa's Oracle + Demonic Consultation / Tainted Pact or Underworld Breach + Brain Freeze. *strategic_judgment · high*
- **Secondary:** Cast-from-exile payoffs (Dragon's Smile, Prosper, Gonti, Laughing Jasper Flint) and the Jester's attack trigger (hasty with Greaves) for incremental stolen resources.
  - Evidence: [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) · [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)
- **Commander role: significant.** The Jester turns every library exile into card access, and its attack trigger is a built-in exile burst. *strategic_judgment · high*
- ⚠️ **Honest note:** Honest call: significant. None of the four Spellbook combos uses the Jester; the kills are generic Grixis cEDH lines (Oracle/Consult, Oracle/Tainted Pact, Breach + LED/Petal + Brain Freeze). The source added Consultation and Tainted Pact explicitly to complete them (decisions L27, L28). The Jester is a future-release card (project exception, legal from 2026-11-13 per decisions L57) and is not officially Commander-legal today.
  - Evidence: [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) · [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) · [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) · `spellbook:742-1295`
- **Dependency level:** low *strategic_judgment · high* — `spellbook:742-1295`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 5 (Power Bracket 5 — cEDH (decisions).) | *fact · verified* | [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L65](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) |
| GrokBot estimated ceiling | 5 (Bracket 5: Oracle/Consult, Tainted Pact and Breach/Brain Freeze with Moxen, LED and free counters is a real cEDH shell, though the identity payoffs make it slower than turbo lists. Agrees with the source.) | *strategic_judgment · moderate* | [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) · [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) · `spellbook:742-1295` |
| Expected bracket (list as built) | 5 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#The_Madcap_Jester` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 5, "2": 59, "3": 101, "4": 27, "5": 50}, "decks_with_bracket": 242, "share_b4_plus": 0.318, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__the-madcap-jester.json`

## Win conditions

- **oracle** (combo): Thassa's Oracle with Demonic Consultation or Tainted Pact. Cards: Thassa's Oracle, Demonic Consultation, Tainted Pact. Enablers: Demonic Tutor, Vampiric Tutor, Imperial Seal, Mystical Tutor. *strategic_judgment · high* — `spellbook:742-1295` · `spellbook:1295-3093`
- **breach-freeze** (combo): Underworld Breach with Lion's Eye Diamond or Lotus Petal and Brain Freeze mills the table. Cards: Underworld Breach, Brain Freeze, Lion's Eye Diamond, Lotus Petal. Enablers: Gamble, Beseech the Mirror. *strategic_judgment · high* — `spellbook:1368-3518-4856` · `spellbook:1368-1414-4856`
- **exile-theft-value** (natural): Out-resource opponents by casting their cards. Cards: The Madcap Jester, Extract, Sadistic Sacrament, Bitter Ordeal, Tasha's Hideous Laughter, Dragon's Smile. Enablers: Dragon's Smile, Don Andres, the Renegade, Gonti, Night Minister. *strategic_judgment · moderate* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) · [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)

## Engines

- **exile-play-permission:** The Madcap Jester, Extract, Sadistic Sacrament, Bitter Ordeal, Tasha's Hideous Laughter, Psychic Surgery, Inside Information, Jester's Cap, Jester's Scepter, Ensnared by the Mara, Ashiok, Nightmare Weaver, Praetor's Grasp. Online when: A spell or ability you control exiles cards from an opponent's library. *fact · high* — `oracle:The Madcap Jester` · [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)
- **hasty-attack:** The Madcap Jester, Lightning Greaves. Online when: The Jester can attack. *strategic_judgment · high* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:library-exile` | yes | 8 | Exile effects that turn into card access. | 11: Extract, Sadistic Sacrament, Bitter Ordeal, Tasha's Hideous Laughter, Psychic Surgery, Inside Information, Jester's Cap, Jester's Scepter, Ensnared by the Mara, Ashiok, Nightmare Weaver, Praetor's Grasp | — | *strategic_judgment · high* | [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) |
| `pkg:exile-payoffs` | yes | 8 | Cast-from-exile payoffs and theft. | 13: Dragon's Smile, Don Andres, the Renegade, Gonti, Night Minister, Prosper, Tome-Bound, Party Thrasher, Passionate Archaeologist, Nalfeshnee, Plargg and Nassari, Sire of Stagnation, Circu, Dimir Lobotomist, Laughing Jasper Flint, Wild-Magic Sorcerer, Dauthi Voidwalker | — | *strategic_judgment · high* | [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) |
| `pkg:compact-wins` | yes | 5 | Compact Grixis kills. | 6: Thassa's Oracle, Demonic Consultation, Tainted Pact, Underworld Breach, Brain Freeze, Lion's Eye Diamond | — | *strategic_judgment · high* | `spellbook:742-1295` · `spellbook:1368-3518-4856` |
| `pkg:free-protection` | yes | 6 | Free and cheap protection. | 8: Force of Will, Force of Negation, Fierce Guardianship, Pact of Negation, Mana Drain, Swan Song, Deadly Rollick, Deflecting Swat | — | *strategic_judgment · high* | [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) |

## Key interactions

- **any-mana-type:** The Jester lets you spend mana of any type on stolen spells, so off-color cards are castable. (The Madcap Jester) *fact · high* — `oracle:The Madcap Jester` · `cr:601.3`
- **dauthi-replacement:** Dauthi Voidwalker exiles cards that would be milled from an opponent's library, which the Jester then lets you play. (Dauthi Voidwalker, The Madcap Jester) *fact · high* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)
- **uba-mask-no:** Uba Mask's replacement effect doesn't trigger the Jester by itself and replaces your own draws; rejected. (The Madcap Jester) *fact · high* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)
- **tainted-pact-singleton:** With 100 distinct names, Tainted Pact never stops on a duplicate. (Tainted Pact, Thassa's Oracle) *fact · high* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)
- **brain-freeze-storm:** Brain Freeze's storm copies scale with Breach loops. (Brain Freeze, Underworld Breach) *fact · high* — `spellbook:1368-3518-4856` · `cr:702.40a`
- **future-release:** The Jester and Dragon's Smile are project exceptions until 2026-11-13; not officially legal today. (The Madcap Jester, Dragon's Smile) *fact · high* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)

## Tutors and recursion

- Tutor target **Thassa's Oracle** via Demonic Tutor, Vampiric Tutor, Imperial Seal, Mystical Tutor, Tainted Pact *strategic_judgment · high* — `spellbook:742-1295`
- Tutor target **Underworld Breach** via Gamble, Beseech the Mirror, Demonic Tutor *strategic_judgment · high* — `spellbook:1368-3518-4856`
- Recursion: Underworld Breach *strategic_judgment · moderate* — `spellbook:1368-3518-4856`

## Requirements

- **Interaction:** Force of Will, Force of Negation, Fierce Guardianship, Pact of Negation, Mana Drain, Swan Song, Deadly Rollick, Toxic Deluge.
- **Protection:** Deflecting Swat, Lightning Greaves, free counters.
- **Mana:** 34 lands plus Moxen, Lotus Petal, LED, Dark/Cabal Ritual, Sol Ring, Mana Vault.
- *strategic_judgment · moderate* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) · [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)

## Failure modes

- **slow-payoffs:** The source kept several four-to-seven-mana exile payoffs over generic cEDH staples; slower than a pure turbo shell. Mitigations: Tasha's Hideous Laughter burst; Compact kills. *strategic_judgment · high* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)
- **oracle-hate:** Stax and graveyard hate stop the Oracle and Breach lines. Mitigations: Two separate lines; Free counters. *strategic_judgment · high* — `spellbook:742-1295`
- **future-release-status:** Not officially legal before 2026-11-13; registry status PENDING_RELEASE. Mitigations: Project exception. *strategic_judgment · high* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)

## Identity core

- **The Madcap Jester:** Plays cards exiled from opponents' libraries. *fact · verified* — `oracle:The Madcap Jester`
- **Thassa's Oracle:** Compact win. *strategic_judgment · high* — `spellbook:742-1295`
- **Underworld Breach:** Second compact win. *strategic_judgment · high* — `spellbook:1368-3518-4856`
- **Tasha's Hideous Laughter:** Burst exile under the Jester. *strategic_judgment · high* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)
- **Dauthi Voidwalker:** Mill-to-exile replacement plus hate. *strategic_judgment · high* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No Uba Mask (decisions L45) or Memory Vessel (L46).
- ✗ No more generic cEDH staples over commander-specific exile engines (L53).
  - *strategic_judgment · high* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) · [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) · [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)
- Theme: Exile theft / library control / Grixis combo (decisions L67).
  - *strategic_judgment · high* — [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md#L67](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 601.3:** Permission to cast. *fact · verified* — `cr:601.3`
- **CR 702.40a:** Storm. *fact · verified* — `cr:702.40a`
- **CR 702.138a:** Escape (Breach). *fact · verified* — `cr:702.138a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["combat damage / attack triggers", "exiling and playing opponents' library cards"], "hooked_cards": 16, "role_counts": {"counter": 7, "draw": 3, "protection": 2, "ramp": 18, "removal": 1, "tutor": 6, "wipe": 3}, "lands": 34, "edhrec_pages": ["the-madcap-jester"]}` *heuristic · low*

## Provenance

- Seeded from: [The_Madcap_Jester_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Madcap_Jester_Candidate_Decisions_2026-10-15.md) · [The_Madcap_Jester_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/The_Madcap_Jester_Approved_2026-10-15.md) · [The_Madcap_Jester_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Madcap_Jester_Approval_Ready_Verification_2026-10-15.md) · [The_Madcap_Jester_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Madcap_Jester_Whole_List_Audit_2026-10-15.md) · [The_Madcap_Jester_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/The_Madcap_Jester_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
