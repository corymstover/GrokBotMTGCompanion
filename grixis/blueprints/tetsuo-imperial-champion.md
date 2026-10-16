# Blueprint — Tetsuo, Imperial Champion

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/tetsuo-imperial-champion.md), state `SOURCE_BASELINE`, list `lh1:fda37e991784a084…`). Machine-readable source: [`data/grixis/blueprints/tetsuo-imperial-champion.json`](../../data/grixis/blueprints/tetsuo-imperial-champion.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Tetsuo, Imperial Champion** — Legendary Creature — Human Samurai

> Whenever Tetsuo attacks, if it's equipped, choose one —  
> • Tetsuo deals damage equal to the greatest mana value among Equipment attached to it to any target.  
> • You may cast an instant or sorcery spell from your hand with mana value less than or equal to the greatest mana value among Equipment attached to Tetsuo without paying its mana cost.

## Plan and commander role

- **Primary plan:** Equipment free-cast: keep high-mana-value Equipment on Tetsuo, then each equipped attack either deals damage equal to the highest Equipment MV or casts an instant/sorcery from hand for free, ideally an extra combat (Savage Beating, World at War) or a suspend card (Ancestral Vision, Profane Tutor, Wheel of Fate). *strategic_judgment · high*
- **Secondary:** Voltron damage as a real second win, with the extra-combat package (Genji Glove, Hexplate Wallbreaker, Akki Battle Squad, Godo, Aggravated Assault + Sword of Feast and Famine).
  - Evidence: [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L9](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md)
- **Commander role: central.** Tetsuo's attack trigger is the deck's spell engine and burn. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native. Both Spellbook combos (900-3750, Sword of Feast and Famine + Aggravated Assault; 3750-5039, The Reaver Cleaver + Aggravated Assault) need an attacking creature, but not Tetsuo; he is the natural carrier. The source corrected a false Relentless Assault / Seize the Day interaction (blueprint L33).
  - Evidence: [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L9](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · `spellbook:900-3750`
- **Dependency level:** high *strategic_judgment · high* — [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L9](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: two-card infinite combat lines and fast Equipment tutoring, but a combat-dependent commander. Agrees with the source.) | *strategic_judgment · high* | `spellbook:900-3750` · [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Tetsuo__Imperial_Champion` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 9, "2": 227, "3": 228, "4": 93, "5": 5}, "decks_with_bracket": 562, "share_b4_plus": 0.174, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__tetsuo-imperial-champion.json`

## Win conditions

- **assault-loop** (combo): Aggravated Assault with Sword of Feast and Famine's untap or The Reaver Cleaver's Treasure for infinite combats. Cards: Aggravated Assault, Sword of Feast and Famine, The Reaver Cleaver. Enablers: Tetsuo, Imperial Champion. *strategic_judgment · high* — `spellbook:900-3750` · `spellbook:3750-5039` · [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L28](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md)
- **voltron** (natural): Equipped Tetsuo with double strike/extra combats, plus trigger damage at any target. Cards: Tetsuo, Imperial Champion, Embercleave, Leyline Axe, Kaldra Compleat, Basilisk Collar. Enablers: Savage Beating, World at War. *strategic_judgment · high* — [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md)

## Engines

- **attack-trigger:** Tetsuo, Imperial Champion, Excalibur, Sword of Eden, Kaldra Compleat, Argentum Armor, Embercleave, Genji Glove, Hexplate Wallbreaker. Online when: Tetsuo attacks while equipped. *fact · high* — `oracle:Tetsuo, Imperial Champion` · [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L9](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md)
- **attach-cheat:** Brass Squire, Hammer of Nazahn, Blacksmith's Talent, Dalakos, Crafter of Wonders, Fabricate, Sword of the Animist, Enthusiastic Mechanaut. Online when: Equipment in play or hand. *strategic_judgment · high* — [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:high-mv-equipment` | yes | 6 | Raise the trigger's ceiling. | 9: Excalibur, Sword of Eden, Kaldra Compleat, Argentum Armor, Embercleave, Genji Glove, Hexplate Wallbreaker, Leyline Axe, Buster Sword, The Reaver Cleaver | — | *strategic_judgment · high* | [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) |
| `pkg:attach` | yes | 4 | Cheap attaching and Equipment tutors. | 7: Brass Squire, Hammer of Nazahn, Blacksmith's Talent, Dalakos, Crafter of Wonders, Fabricate, Sword of the Animist, Enthusiastic Mechanaut | — | *strategic_judgment · high* | [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L14](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) |
| `pkg:free-cast` | yes | 5 | Spells worth casting free. | 7: Ancestral Vision, Profane Tutor, Wheel of Fate, Inevitable Betrayal, Savage Beating, World at War, Chandra's Ignition | — | *strategic_judgment · high* | [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md) · [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md) |
| `pkg:protection` | yes | 3 | Haste and protection. | 6: Swiftfoot Boots, Oathkeeper, Takeno's Daisho, Mithril Coat, Winged Boots, Deflecting Swat, Fierce Guardianship | — | *strategic_judgment · high* | [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md) · [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md) |

## Key interactions

- **main-phase-only:** Relentless Assault / Seize the Day only add combats if cast in a main phase; Tetsuo casts in combat, so they were cut. (Savage Beating, World at War) *fact · high* — [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L46](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md) · `cr:505.1`
- **savage-beating:** Savage Beating works at combat timing when the Equipment ceiling is at least five. (Savage Beating) *fact · high* — [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L31](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md) · `cr:500.8`
- **world-at-war-rebound:** World at War cast in combat still adds a later combat, and rebound works because it was cast from hand. (World at War) *fact · high* — [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L32](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md)
- **suspend-free-cast:** Suspend cards with no mana cost can be cast through Tetsuo because his ability supplies the alternative cost. (Ancestral Vision, Profane Tutor, Wheel of Fate) *fact · high* — [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · `cr:118.9`
- **collar-damage:** Tetsuo deals the trigger damage himself, so Basilisk Collar gives it deathtouch and lifelink. (Basilisk Collar) *fact · high* — [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L29](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md)
- **no-wealth-power:** Sword of Wealth and Power was rejected: protection from instants/sorceries blocks Tetsuo's own targeted spells. (Chandra's Ignition) *fact · high* — [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md)

## Tutors and recursion

- Tutor target **Embercleave** via Fabricate, Sword of the Animist, Enthusiastic Mechanaut, Profane Tutor *strategic_judgment · high* — [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md)
- Recursion: Academy Ruins, Oathkeeper, Takeno's Daisho *strategic_judgment · moderate* — [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L30](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Fierce Guardianship, Terminate, Withering Torment, Chaos Warp, Blasphemous Act, Cyclonic Rift.
- **Protection:** Swiftfoot Boots, Oathkeeper, Mithril Coat, Deflecting Swat.
- **Mana:** 35 lands with Sol Ring, Ancient Tomb, Signets and Talismans.
- *strategic_judgment · moderate* — [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md) · [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md)

## Failure modes

- **equipment-hate:** Artifact removal or an unequipped Tetsuo turns the trigger off. Mitigations: Equipment density; Academy Ruins. *strategic_judgment · high* — `oracle:Tetsuo, Imperial Champion`
- **blockers-and-removal:** Tetsuo has to attack and survive. Mitigations: Boots; Oathkeeper; Winged Boots. *strategic_judgment · high* — [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L16](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md)
- **empty-hand:** The free-cast mode needs a good spell in hand. Mitigations: Rhystic Study; Mystic Remora; Wheel of Fate. *strategic_judgment · moderate* — `oracle:Tetsuo, Imperial Champion`

## Identity core

- **Tetsuo, Imperial Champion:** Equipped attack: burn or free spell. *fact · verified* — `oracle:Tetsuo, Imperial Champion`
- **Aggravated Assault:** Infinite-combat outlet. *strategic_judgment · high* — `spellbook:900-3750`
- **Sword of Feast and Famine:** Untaps lands for Assault. *strategic_judgment · high* — `spellbook:900-3750`
- **Excalibur, Sword of Eden:** Very high MV for the trigger. *strategic_judgment · high* — [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L25](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md)
- **Brass Squire:** Free attaching. *strategic_judgment · high* — [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No generic cEDH conversion (decisions L42).
- ✗ No Time Warp effects over extra combats (L38).
  - *strategic_judgment · high* — [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L42](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md) · [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md#L38](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md)
- Theme: Equipment / free-cast spells / extra combats (blueprint L21).
  - *strategic_judgment · high* — [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 118.9:** Alternative costs. *fact · verified* — `cr:118.9`
- **CR 500.8:** Extra phases. *fact · verified* — `cr:500.8`
- **CR 702.6a:** Equip. *fact · verified* — `cr:702.6a`

## Supporting features (heuristic, not identity)

- `{"hooks": ["combat damage / attack triggers", "instants and sorceries"], "hooked_cards": 41, "role_counts": {"counter": 2, "draw": 11, "protection": 7, "ramp": 11, "removal": 6, "tutor": 4, "wipe": 1}, "lands": 35, "edhrec_pages": ["tetsuo-imperial-champion"]}` *heuristic · low*

## Provenance

- Seeded from: [Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Tetsuo_Imperial_Champion_Commander_Blueprint_2026-10-15.md) · [Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md) · [Tetsuo_Imperial_Champion_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Tetsuo_Imperial_Champion_Approved_2026-10-15.md) · [Tetsuo_Imperial_Champion_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tetsuo_Imperial_Champion_Approval_Ready_Verification_2026-10-15.md) · [Tetsuo_Imperial_Champion_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tetsuo_Imperial_Champion_Whole_List_Audit_2026-10-15.md) · [Tetsuo_Imperial_Champion_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Tetsuo_Imperial_Champion_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
