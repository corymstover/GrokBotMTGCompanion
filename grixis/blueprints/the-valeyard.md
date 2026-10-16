# Blueprint — The Valeyard

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/the-valeyard.md), state `SOURCE_BASELINE`, list `lh1:1724d3640badd976…`). Machine-readable source: [`data/grixis/blueprints/the-valeyard.json`](../../data/grixis/blueprints/the-valeyard.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**The Valeyard** — Legendary Creature — Time Lord Noble

> If an opponent would face a villainous choice, they face that choice an additional time. (They can make the same or different choices.)  
> While voting, you may vote an additional time.

## Plan and commander role

- **Primary plan:** Villainous Choice and voting: The Valeyard makes opponents face each Villainous Choice twice and gives you an extra vote, so the deck runs Villainous Choice sources and real vote cards (Capital Punishment, Plea for Power, Split Decision, Tyrant's Choice, Messenger Jays) and copies the Valeyard to stack the effects. *strategic_judgment · high*
- **Secondary:** Premium protection, tutors and interaction around a five-mana commander; Doctor Who villain support.
  - Evidence: [The_Valeyard_Candidate_Decisions_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)
- **Commander role: central.** The Valeyard doubles every Villainous Choice and adds a vote; nonlegendary copies add more. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native but narrow: two static modifiers, no body-based engine, and no Spellbook combos; the source asserts no infinite (decisions L76). Copies stack additively, not exponentially (L74). The source rejected Prisoner's Dilemma and Seize the Spotlight because 'choose' isn't 'vote' (CR 701.38c). The deck's power comes from its staples more than the commander; expect low Bracket 4.
  - Evidence: [The_Valeyard_Candidate_Decisions_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L74](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L76](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)
- **Dependency level:** high *strategic_judgment · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions).) | *fact · verified* | [The_Valeyard_Candidate_Decisions_2026-10-15.md#L86](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Low Bracket 4: premium staples set the floor, but the commander's mechanic is slow and opponent-chosen. Agrees with the source on the bracket; it likely plays below most Bracket 4 decks.) | *strategic_judgment · moderate* | [The_Valeyard_Candidate_Decisions_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Approval_Ready_Verification_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Valeyard_Approval_Ready_Verification_2026-10-15.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#The_Valeyard` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 14, "2": 130, "3": 124, "4": 20, "5": 1}, "decks_with_bracket": 289, "share_b4_plus": 0.073, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__the-valeyard.json`

## Win conditions

- **political-attrition** (natural): Doubled Villainous Choices and weighted votes grind opponents out of resources and life. Cards: The Valeyard, Damocles Base, Sword of Kang, Davros, Dalek Creator, Dr. Eggman, Ensnared by the Mara, Genesis of the Daleks, Messenger Jays, Capital Punishment, Plea for Power. Enablers: Spark Double, Quantum Misalignment, Sakashima of a Thousand Faces, Auton Soldier. *strategic_judgment · moderate* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)
- **villain-beats** (natural): Doctor Who villain threats (Davros, The Dalek Emperor, Cult of Skaro) close the game. Cards: Davros, Dalek Creator, The Dalek Emperor, Cult of Skaro. *strategic_judgment · moderate* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)

## Engines

- **double-villainous:** The Valeyard, Damocles Base, Sword of Kang, Davros, Dalek Creator, Dr. Eggman, Ensnared by the Mara, Genesis of the Daleks, Great Intelligence's Plan, Hunted by The Family, Midnight Crusader Shuttle, Missy, Sycorax Commander, The Dalek Emperor, The Master, Gallifrey's End, This Is How It Ends. Online when: An opponent faces a Villainous Choice. *fact · high* — `oracle:The Valeyard` · `cr:701.55c`
- **extra-vote:** The Valeyard, Messenger Jays, Capital Punishment, Plea for Power, Split Decision, Truth or Consequences, Tyrant's Choice, Coercive Portal, Model of Unity, Illusion of Choice, Grudge Keeper, Expropriate, Fateful Tempest, Mob Verdict, Trap the Trespassers, Path of the Enigma, Path of the Pyromancer, Path of the Schemer. Online when: A vote happens. *fact · high* — `oracle:The Valeyard` · `cr:701.38a`
- **valeyard-copies:** Spark Double, Quantum Misalignment, Sakashima of a Thousand Faces, Auton Soldier. Online when: The Valeyard on the battlefield. *strategic_judgment · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:villainous` | yes | 10 | Villainous Choice sources. | 13: Damocles Base, Sword of Kang, Davros, Dalek Creator, Dr. Eggman, Ensnared by the Mara, Genesis of the Daleks, Great Intelligence's Plan, Hunted by The Family, Midnight Crusader Shuttle, Missy, Sycorax Commander, The Dalek Emperor, The Master, Gallifrey's End, This Is How It Ends | — | *strategic_judgment · high* | [The_Valeyard_Candidate_Decisions_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) |
| `pkg:vote` | yes | 6 | Actual vote cards. | 17: Messenger Jays, Capital Punishment, Plea for Power, Split Decision, Truth or Consequences, Tyrant's Choice, Coercive Portal, Model of Unity, Illusion of Choice, Grudge Keeper, Expropriate, Fateful Tempest, Mob Verdict, Trap the Trespassers, Path of the Enigma, Path of the Pyromancer, Path of the Schemer | — | *strategic_judgment · high* | [The_Valeyard_Candidate_Decisions_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) |
| `pkg:copy` | yes | 3 | Nonlegendary Valeyard copies. | 4: Spark Double, Quantum Misalignment, Sakashima of a Thousand Faces, Auton Soldier | — | *strategic_judgment · high* | [The_Valeyard_Candidate_Decisions_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) |

## Key interactions

- **vote-means-vote:** Only cards that say 'vote' use the extra vote; Prisoner's Dilemma and Seize the Spotlight don't. (The Valeyard) *fact · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L72](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · `cr:701.38c`
- **one-at-a-time:** Extra Villainous Choices resolve one at a time. (The Valeyard) *fact · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L73](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · `cr:701.55c`
- **additive:** Each extra Valeyard adds one more choice and one more vote; additive, not exponential. (Spark Double, Quantum Misalignment, Sakashima of a Thousand Faces, Auton Soldier) *fact · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L74](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)
- **auton-myriad:** Auton Soldier as a Valeyard copy makes nonlegendary myriad Valeyard tokens. (Auton Soldier) *fact · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L75](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)
- **paradox-haze-no:** Paradox Haze adds an upkeep, not a copy of either ability; cut. (The Valeyard) *fact · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)

## Tutors and recursion

- Tutor target **Spark Double** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [The_Valeyard_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)
- Recursion: — *strategic_judgment · moderate* — [The_Valeyard_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Fierce Guardianship, Mana Drain, Arcane Denial, Deadly Rollick, Feed the Swarm, Chaos Warp, Cyclonic Rift, Blasphemous Act.
- **Protection:** Deflecting Swat, Lightning Greaves, Force of Will.
- **Mana:** 36 lands; Arid Mesa replaced a dead Windswept Heath.
- *strategic_judgment · moderate* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)

## Failure modes

- **five-mana-static:** Five mana for two static modifiers; little happens without the cards they modify. Mitigations: Copies; Tutors. *strategic_judgment · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)
- **opponent-choice:** Villainous Choices and votes let opponents pick the least bad option. Mitigations: Doubled choices; Extra votes. *strategic_judgment · high* — `oracle:The Valeyard`
- **no-compact-win:** No compact kill. Mitigations: Villain threats. *strategic_judgment · moderate* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L76](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)

## Identity core

- **The Valeyard:** Double Villainous Choices; an extra vote. *fact · verified* — `oracle:The Valeyard`
- **Spark Double:** Permanent nonlegendary Valeyard. *strategic_judgment · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)
- **Sakashima of a Thousand Faces:** Copy without the legend rule. *strategic_judgment · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)
- **Messenger Jays:** Vote card with direct commander text. *strategic_judgment · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)
- **Davros, Dalek Creator:** Villainous Choice threat. *strategic_judgment · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No 'choose' cards that aren't votes (decisions L43, L45).
- ✗ No Tempt with Reflections without a legend-rule workaround (L65).
  - *strategic_judgment · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L45](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Candidate_Decisions_2026-10-15.md#L65](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)
- Theme: Villainous Choice / voting / political control (decisions L88).
  - *strategic_judgment · high* — [The_Valeyard_Candidate_Decisions_2026-10-15.md#L88](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.38c:** Voting means an actual vote. *fact · verified* — `cr:701.38c`
- **CR 701.55c:** Extra Villainous Choices. *fact · verified* — `cr:701.55c`
- **CR 701.38a:** Voting. *fact · verified* — `cr:701.38a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["villainous choices / voting"], "hooked_cards": 30, "role_counts": {"counter": 4, "draw": 19, "protection": 2, "ramp": 12, "removal": 4, "tutor": 2, "wipe": 3}, "lands": 36, "edhrec_pages": ["the-valeyard"]}` *heuristic · low*

## Provenance

- Seeded from: [The_Valeyard_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/The_Valeyard_Candidate_Decisions_2026-10-15.md) · [The_Valeyard_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/The_Valeyard_Approved_2026-10-15.md) · [The_Valeyard_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Valeyard_Approval_Ready_Verification_2026-10-15.md) · [The_Valeyard_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/The_Valeyard_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
