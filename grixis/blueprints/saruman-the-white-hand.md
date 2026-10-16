# Blueprint — Saruman, the White Hand

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/saruman-the-white-hand.md), state `SOURCE_BASELINE`, list `lh1:4710f5676592c6b8…`). Machine-readable source: [`data/grixis/blueprints/saruman-the-white-hand.json`](../../data/grixis/blueprints/saruman-the-white-hand.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Saruman, the White Hand** — Legendary Creature — Avatar Wizard

> Whenever you cast a noncreature spell, amass Orcs X, where X is that spell's mana value. (Put X +1/+1 counters on an Army you control. It's also an Orc. If you don't control an Army, create a 0/0 black Orc Army creature token first.)  
> Goblins and Orcs you control have ward {2}.

## Plan and commander role

- **Primary plan:** Spellslinger amass: each noncreature spell amasses Orcs equal to its mana value. Cost reducers, delve, alternate and free costs don't lower mana value, so cheap high-MV spells (Blasphemous Act, Dig Through Time, Blood for the Blood God!, Volcanic Salvo, Treasure Cruise, free spells) grow a huge Orc Army. *strategic_judgment · high*
- **Secondary:** Trigger multipliers (Harmonic Prodigy, Wizard's Staff, Veyran), Mauhúr and The Ozolith, and payoffs that turn the Army or its counters into damage (The Great Goblin, Soul's Fire, Chandra's Ignition, Widespread Brutality, Fall of Cair Andros).
  - Evidence: [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L39](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)
- **Commander role: central.** Saruman is the Army engine and gives Goblins and Orcs ward {2}. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native identity, but the only Spellbook combo in the list is Fall of Cair Andros + Blasphemous Act, which doesn't need him. He's a four-mana engine with no compact win; the source rejected commander-independent All Will Be One loops (decisions L40). Expect a mid Bracket 4 value/burn deck.
  - Evidence: [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · `spellbook:1823-2484`
- **Dependency level:** high *strategic_judgment · high* — [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: explosive Army turns and premium staples, no compact win. Agrees with the source.) | *strategic_judgment · high* | [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Saruman__the_White_Hand` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 42, "2": 1022, "3": 1252, "4": 305, "5": 22}, "decks_with_bracket": 2643, "share_b4_plus": 0.124, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__saruman-the-white-hand.json`

## Win conditions

- **cair-andros-act** (combo): Fall of Cair Andros + Blasphemous Act: excess damage amasses, which triggers more. Cards: Fall of Cair Andros, Blasphemous Act. Enablers: Saruman, the White Hand. *fact · verified* — `spellbook:1823-2484`
- **army-damage** (natural): A huge Orc Army attacks or is fired through Soul's Fire/Chandra's Ignition; The Great Goblin and All Will Be One ping per counter event. Cards: Saruman, the White Hand, Soul's Fire, Chandra's Ignition, The Great Goblin, All Will Be One, Widespread Brutality. Enablers: Mauhúr, Uruk-hai Captain, Harmonic Prodigy, Wizard's Staff, Veyran, Voice of Duality. *strategic_judgment · high* — [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)

## Engines

- **mv-amass:** Saruman, the White Hand, Blasphemous Act, Dig Through Time, Blood for the Blood God!, Deadly Rollick, Fierce Guardianship, Deflecting Swat, Volcanic Salvo, Treasure Cruise, Force of Will. Online when: Saruman in play; noncreature spells cast (copies don't trigger). *fact · high* — `oracle:Saruman, the White Hand` · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)
- **trigger-and-counter-multipliers:** Harmonic Prodigy, Wizard's Staff, Veyran, Voice of Duality, Mauhúr, Uruk-hai Captain, The Ozolith. Online when: Saruman in play. *fact · high* — [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L39](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:high-mv-cheap` | yes | 7 | High printed mana value for a low real cost. | 9: Blasphemous Act, Dig Through Time, Blood for the Blood God!, Deadly Rollick, Fierce Guardianship, Deflecting Swat, Volcanic Salvo, Treasure Cruise, Force of Will | — | *strategic_judgment · high* | [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) |
| `pkg:army-payoffs` | yes | 5 | Turn the Army or counter events into damage. | 6: The Great Goblin, All Will Be One, Soul's Fire, Chandra's Ignition, Widespread Brutality, Fall of Cair Andros | — | *strategic_judgment · high* | [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L41](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L43](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) |
| `pkg:mdfc-spells` | optional | 3 | Land-capable slots that are also noncreature spells. | 4: Kazuul's Fury // Kazuul's Cliffs, Sea Gate Restoration // Sea Gate, Reborn, Shatterskull Smashing // Shatterskull, the Hammer Pass, Sink into Stupor // Soporific Springs | — | *strategic_judgment · high* | [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) |

## Key interactions

- **alt-cost-keeps-mv:** Alternative costs, delve and cost reductions don't change mana value, so a pitched Force of Will still amasses 5. (Saruman, the White Hand, Force of Will, Dig Through Time, Treasure Cruise) *fact · high* — `oracle:Saruman, the White Hand` · `cr:118.9c` · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)
- **x-on-stack:** On the stack, an X spell's mana value includes the chosen X. (Saruman, the White Hand, Shatterskull Smashing // Shatterskull, the Hammer Pass) *fact · high* — `cr:202.3e` · [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)
- **fling-rejected:** Sacrificing the Army as an additional cost (Fling) happens before Saruman's trigger resolves; Soul's Fire keeps the Army. (Soul's Fire, Saruman, the White Hand) *fact · high* — [Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md)
- **copies-not-cast:** Copied spells aren't cast, so they don't trigger Saruman (why Storm of Saruman was cut). (Saruman, the White Hand) *fact · high* — [Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md)
- **mdfc-land-face:** Playing an MDFC's land face doesn't trigger Saruman; casting the spell face does. (Saruman, the White Hand, Kazuul's Fury // Kazuul's Cliffs) *fact · high* — [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L55](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)

## Tutors and recursion

- Tutor target **Blasphemous Act** via Demonic Tutor, Vampiric Tutor, Mystical Tutor *strategic_judgment · moderate* — `spellbook:1823-2484`
- Recursion: Mizzix's Mastery, Jeska's Will, Summons of Saruman *strategic_judgment · moderate* — [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Mana Drain, Counterspell, Swan Song, Deadly Rollick, Cyclonic Rift, Toxic Deluge, Feed the Swarm.
- **Protection:** Fierce Guardianship, Deflecting Swat; ward {2} on Orcs and Goblins.
- **Mana:** 35 land-capable slots including 4 MDFCs.
- *strategic_judgment · moderate* — [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)

## Failure modes

- **no-compact-win:** No compact win; the deck needs several spells after Saruman lands. Mitigations: Card draw and cost reduction. *strategic_judgment · high* — [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)
- **army-removal:** One removal spell on the Army resets most of the board. Mitigations: Ward {2}; The Ozolith. *strategic_judgment · high* — `oracle:Saruman, the White Hand`
- **saruman-removed:** Without Saruman the high-MV discount plan is just card quality. Mitigations: Fierce Guardianship; Deflecting Swat. *strategic_judgment · moderate* — `oracle:Saruman, the White Hand`

## Identity core

- **Saruman, the White Hand:** Amass by mana value on every noncreature spell. *fact · verified* — `oracle:Saruman, the White Hand`
- **Blasphemous Act:** MV 9 for one mana. *strategic_judgment · high* — [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)
- **Volcanic Salvo:** MV 12 with a power-based reduction. *strategic_judgment · high* — [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)
- **Soul's Fire:** Fires the grown Army without sacrificing it. *strategic_judgment · high* — [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)
- **Mauhúr, Uruk-hai Captain:** An extra counter per placement event. *strategic_judgment · high* — [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No commander-independent All Will Be One/Red Terror loops (decisions L40).
- ✗ No extra creatures that dilute noncreature density (decisions L37).
- ✗ No mana-spent payoffs like Uncover the Moon-Letters (L35).
  - *strategic_judgment · high* — [Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md#L40](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md) · [Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md) · [Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md)
- Theme: Spellslinger / amass / Orc Army (blueprint L59).
  - *strategic_judgment · high* — [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.47a:** Amass. *fact · verified* — `cr:701.47a`
- **CR 118.9c:** Alternative costs don't change mana cost. *fact · verified* — `cr:118.9c`
- **CR 202.3e:** X in mana value on the stack. *fact · verified* — `cr:202.3e`

## Supporting features (heuristic, not identity)

- `{"hooks": ["+1/+1 counters", "Army synergy", "Goblin synergy", "Orc synergy", "instants and sorceries", "tokens"], "hooked_cards": 58, "role_counts": {"counter": 6, "draw": 16, "protection": 2, "ramp": 14, "removal": 8, "tutor": 4, "wipe": 2}, "lands": 31, "edhrec_pages": ["saruman-the-white-hand"]}` *heuristic · low*

## Provenance

- Seeded from: [Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Saruman_the_White_Hand_Commander_Blueprint_2026-10-15.md) · [Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Saruman_the_White_Hand_Candidate_Decisions_2026-10-15.md) · [Saruman_the_White_Hand_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Saruman_the_White_Hand_Approved_2026-10-15.md) · [Saruman_the_White_Hand_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Saruman_the_White_Hand_Approval_Ready_Verification_2026-10-15.md) · [Saruman_the_White_Hand_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Saruman_the_White_Hand_Whole_List_Audit_2026-10-15.md) · [Saruman_the_White_Hand_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Saruman_the_White_Hand_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
