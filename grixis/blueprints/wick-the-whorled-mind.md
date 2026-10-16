# Blueprint — Wick, the Whorled Mind

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/wick-the-whorled-mind.md), state `SOURCE_BASELINE`, list `lh1:8209700d366bf1d1…`). Machine-readable source: [`data/grixis/blueprints/wick-the-whorled-mind.json`](../../data/grixis/blueprints/wick-the-whorled-mind.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Wick, the Whorled Mind** — Legendary Creature — Rat Warlock

> Whenever Wick or another Rat you control enters, create a 1/1 black Snail creature token if you don't control a Snail. Otherwise, put a +1/+1 counter on a Snail you control.  
> {U}{B}{R}, Sacrifice a Snail: Wick deals damage equal to the sacrificed creature's power to each opponent. Then draw cards equal to the sacrificed creature's power.

## Plan and commander role

- **Primary plan:** Rats into a Snail: every Rat entering creates or grows one Snail, and Wick's {U}{B}{R}, sacrifice a Snail deals its power to each opponent and draws that many. Type-changers (Arcane Adaptation, Leyline of Transformation, Maskwood Nexus) make the Snail a Rat, so it loops with free outlets. *strategic_judgment · high*
- **Secondary:** Grow the Snail with Bulk Up, Lich's Relic and Blade of the Bloodchief, keep counters with The Ozolith, and run Marrow-Gnawer + Intruder Alarm; Tainted Strike turns Wick's damage into poison.
  - Evidence: [Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md#L9](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md) · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L56](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)
- **Commander role: central.** Wick is the Snail factory and the damage-and-draw outlet. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native combo: 12 of the 13 Spellbook combos name Wick (Wick + a type-changer + a free outlet); the 13th (1636-3126, Marrow-Gnawer + Intruder Alarm) doesn't. Wick costs {3}{B}, but the activation needs {U}{B}{R}, and Cavern of Souls mana can't pay it (verification L64).
  - Evidence: [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L56](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L64](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · `spellbook:4050-5853-5929`
- **Dependency level:** total *strategic_judgment · high* — `spellbook:4050-5853-5929`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions).) | *fact · verified* | [Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (High Bracket 4: 12 commander-native three-card loops and tutors, but they're three-card enchantment lines with a three-color activation, and protection is moderate. Agrees with the source.) | *strategic_judgment · high* | [Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md#L139](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md) · `spellbook:803-4050-5853` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Wick__the_Whorled_Mind` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 46, "2": 1770, "3": 805, "4": 167, "5": 29}, "decks_with_bracket": 2817, "share_b4_plus": 0.07, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__wick-the-whorled-mind.json`

## Win conditions

- **snail-rat-loop** (combo): Wick + Arcane Adaptation or Leyline of Transformation (Rat) + a free outlet: the Snail-Rat re-enters as the next Snail, and with Goblin Bombardment, Altar of Dementia or Phyrexian Altar the loop wins. Cards: Wick, the Whorled Mind, Arcane Adaptation, Leyline of Transformation, Viscera Seer, Carrion Feeder, Phyrexian Altar, Ashnod's Altar, Altar of Dementia, Goblin Bombardment. Enablers: Diabolic Intent, Demonic Tutor, Vampiric Tutor. *strategic_judgment · high* — `spellbook:4050-5853-5929` · `spellbook:803-4050-5853` · `spellbook:803-5147-5853` · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L56](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)
- **gnawer-alarm** (combo): Marrow-Gnawer + Intruder Alarm makes unbounded Rats; each one grows the Snail through Wick. Cards: Marrow-Gnawer, Intruder Alarm. Enablers: Wick, the Whorled Mind. *strategic_judgment · high* — `spellbook:1636-3126` · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)
- **big-snail** (natural): Grow one Snail, then sacrifice it to hit every opponent and draw the same amount. Cards: Wick, the Whorled Mind, Bulk Up, Lich's Relic, Blade of the Bloodchief, Song of Totentanz. Enablers: Pack Rat, Marrow-Gnawer, Lord Skitter, Sewer King, Lord Skitter's Butcher, Karumonix, the Rat King. *strategic_judgment · high* — [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)
- **tainted-strike** (alternate): Tainted Strike on Wick turns the activation damage into poison counters. Cards: Tainted Strike, Wick, the Whorled Mind. *strategic_judgment · moderate* — [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L58](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)

## Engines

- **snail-engine:** Wick, the Whorled Mind. Online when: Rats entering; {U}{B}{R} to cash in. *fact · high* — `oracle:Wick, the Whorled Mind` · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)
- **type-change:** Arcane Adaptation, Leyline of Transformation, Maskwood Nexus. Online when: A type-changer naming Rat. *fact · high* — [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L56](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:rats` | yes | 12 | Cheap and multi-body Rat entries. | 18: Pack Rat, Marrow-Gnawer, Lord Skitter, Sewer King, Lord Skitter's Butcher, Karumonix, the Rat King, Rat King, Pale Piper, Rat King, Verminister, Piper of the Swarm, Persistent Marshstalker, Redcap Gutter-Dweller, Tangled Colony, Voracious Vermin, Vren, the Relentless, Totentanz, Swarm Piper, Valley Rotcaller, Song of Totentanz, Ashcoat of the Shadow Swarm, Roaming Throne | — | *strategic_judgment · high* | [Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md#L9](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md) |
| `pkg:type-changers` | yes | 3 | Make the Snail a Rat without losing Snail. | 3: Arcane Adaptation, Leyline of Transformation, Maskwood Nexus | — | *strategic_judgment · high* | [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) |
| `pkg:outlets` | yes | 5 | Free sacrifice outlets. | 7: Viscera Seer, Carrion Feeder, Phyrexian Altar, Ashnod's Altar, Altar of Dementia, Goblin Bombardment, Phyrexian Tower | — | *strategic_judgment · high* | [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L56](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) |
| `pkg:snail-growth` | yes | 4 | Grow and keep Snail power. | 4: Bulk Up, Blade of the Bloodchief, The Ozolith, Lich's Relic | — | *strategic_judgment · high* | [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L61](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L62](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) |

## Key interactions

- **last-known-power:** Damage and cards use the Snail's power as it last existed on the battlefield. (Wick, the Whorled Mind) *fact · high* — [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · `cr:608.2h`
- **add-not-replace:** Arcane Adaptation, Leyline and Maskwood add Rat and keep Snail; Conspiracy replaces types and was rejected. (Arcane Adaptation, Leyline of Transformation, Maskwood Nexus) *fact · high* — [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L55](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · `cr:205.1b`
- **wick-is-source:** Wick, not the Snail, is the damage source, so Tainted Strike on Wick makes it poison. (Tainted Strike, Wick, the Whorled Mind) *fact · high* — [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L58](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)
- **cavern-mana:** Cavern of Souls' restricted mana can't pay Wick's activation. (Cavern of Souls, Wick, the Whorled Mind) *fact · high* — [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L64](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)
- **ozolith-keep:** The Ozolith stores a sacrificed Snail's counters for later. (The Ozolith) *fact · high* — [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L61](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)

## Tutors and recursion

- Tutor target **Arcane Adaptation** via Demonic Tutor, Vampiric Tutor, Diabolic Intent *strategic_judgment · high* — `spellbook:803-4050-5853`
- Recursion: Persistent Marshstalker, Pack Rat, The Ozolith *strategic_judgment · moderate* — [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L61](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)

## Requirements

- **Interaction:** Mana Drain, Fierce Guardianship, Swan Song, An Offer You Can't Refuse, Deadly Rollick, Feed the Swarm, Chaos Warp, Toxic Deluge, Blasphemous Act, Cyclonic Rift.
- **Protection:** Deflecting Swat, Fierce Guardianship, An Offer You Can't Refuse, Cavern of Souls.
- **Mana:** U/B/R sources for the activation; Mana Confluence and fetches; Cavern is restricted.
- *strategic_judgment · moderate* — [Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md) · [Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md)

## Failure modes

- **three-color-activation:** The activation needs all three colors. Mitigations: Mana Confluence; Typed duals. *strategic_judgment · high* — [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L64](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)
- **snail-removal:** Removing the Snail in response wastes the stored power. Mitigations: The Ozolith; Instant-speed activation. *strategic_judgment · high* — `oracle:Wick, the Whorled Mind`
- **enchantment-hate:** Enchantment removal on the type-changer breaks the loop. Mitigations: Three type-changers; Tutors. *strategic_judgment · moderate* — `spellbook:803-4050-5853`

## Identity core

- **Wick, the Whorled Mind:** Snail factory and damage-draw outlet. *fact · verified* — `oracle:Wick, the Whorled Mind`
- **Arcane Adaptation:** Makes the Snail a Rat. *strategic_judgment · high* — `spellbook:803-4050-5853`
- **Leyline of Transformation:** Second type-changer, free from the opening hand. *strategic_judgment · high* — `spellbook:4050-5853-5929`
- **Intruder Alarm:** Unbounded Rats with Marrow-Gnawer. *strategic_judgment · high* — `spellbook:1636-3126`
- **Bulk Up:** Doubles the Snail's payload. *strategic_judgment · high* — [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No generic Oracle/Consultation/Breach (decisions L139).
- ✗ No Conspiracy (L138) or Panharmonicon (L133).
  - *strategic_judgment · high* — [Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md#L139](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md) · [Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md#L138](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md) · [Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md#L133](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md)
- Theme: Rats / Snail counters / combo (decisions L12).
  - *strategic_judgment · high* — [Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md#L12](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 608.2h:** Last known information. *fact · verified* — `cr:608.2h`
- **CR 205.1b:** Adding types versus replacing them. *fact · verified* — `cr:205.1b`
- **CR 701.21a:** Sacrifice. *fact · verified* — `cr:701.21a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["+1/+1 counters", "Rat synergy", "Snail synergy", "enters triggers", "sacrifice", "tokens"], "hooked_cards": 35, "role_counts": {"counter": 4, "draw": 5, "protection": 1, "ramp": 13, "removal": 7, "tutor": 3, "wipe": 2}, "lands": 35, "edhrec_pages": ["wick-the-whorled-mind"]}` *heuristic · low*

## Provenance

- Seeded from: [Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Wick_the_Whorled_Mind_Candidate_Decisions_2026-10-15.md) · [Wick_the_Whorled_Mind_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Wick_the_Whorled_Mind_Approved_2026-10-15.md) · [Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Wick_the_Whorled_Mind_Approval_Ready_Verification_2026-10-15.md) · [Wick_the_Whorled_Mind_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Wick_the_Whorled_Mind_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
