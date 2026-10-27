# Deck 50 — M7 Rev1 executed P0/P1 case-level and scoped I/J transfer ledger

Date: 2026-10-27. Candidate-scoped tests executed locally; no historical M6/I-J acceptance or owner approval claimed.

- Baseline canonical raw SHA-256: `fab194f69a6e15b83679c1419f88ba6fdd56cd9527946cb94a6d8efe23a7dfc8`.
- Candidate raw SHA-256: `266660c6a3241c07a052da7624366be1f9617cb5db4c35c422b0e8f828977d9b`.
- Source blueprint: `data/grixis/m6/test_blueprints/Sauron__the_Dark_Lord.json`, 15 designed cases (P0 5 and P1 10). *All* original cases were recorded there as `DESIGN_ONLY_UNIMPLEMENTED_NOT_RUN`.
- Prior M6 I/J receipt: `data/grixis/m6/ij/input_receipts/sauron-the-dark-lord.json`, stage `M6_IJ_input_receipt`, downstream **incomplete**. It attests source inputs/hashes, NOT Phase B replay, actual model evaluation or complete candidate acceptance.
- Initial source-bound lightweight assertions: `sauron_dark_lord_verify.py`, local and GitHub CI PASS on PR #731.
- **New executable case transfer:** `tests/test_m6_sauron_dark_lord_m7_rev1_cases.py`, exact candidate SHA-bound, 16/16 local unittest PASS. Its fifteen named cases use explicit payment, zones, battlefield object IDs, separate LIFO spell/cast/tempt triggers, hand discard, opponent life, negative adversarial conditions; the sixteenth checks Bone Miser, Glint-Horn and Moonstone discard zones and payoffs. Full new exact-head CI is required. This is a bounded mini-fixture, *not* a universal rules engine or historical sealed I/J replay.

| Case | P | Preliminary new evidence / changed-card impact | Still required for formal M6 certification |
|---|---|---|---|
| C1 commander | P0 | Sauron's opponent CAST, Army player combat-damage and optional discard/draw triggers represented; neither Sauron identity nor name changed | Execute source-paid entire spell/trigger stack in a rules-faithful fixture with negative zones/countered spells |
| K1 ward legendary | P0 | Positive legendary creature/artifact sacrifice and no-permanent negative controls | Model targeting, ward-stack payment choices and untargeted sweeper |
| K2 amass on cast | P0 | One opponent spell countered still yields one amass; own casts produce none; Throne Avatar yields two | Stack order and changing Army creature objects after removal |
| K3 Mauhúr replacement | P0 | One counter per counter-placement event, not one per individual counter | Real zone/counter ledger with prior Army status |
| F1 compact win | P0 | Source-specific source-bound critique rejects unsupported deterministic compact wins; no automatic Breach/Oracle loop added | Exhaust relevant payable line candidates rather than treat the negative unit assertion as proof of absence |
| K4 The Great Goblin | P1 | One trigger per eligible counter event; amount increased by Mauhúr not extra trigger | Full positive/negative controller/event targets including no Army present |
| K5 Roaming Throne | P1 | **Correction:** Arcane Adaptation naming Wraith turns Sauron and The Great Goblin into Wraiths, so Throne choosing Wraith doubles their triggers alongside all Nazgûl | Exact K5 test now runs both with and without Adaptation |
| K6 seven Nazgûl | P1 | Seven legal copies; event wave and Sauron optional draw paths | Oracle card-name construction check (live CI) + token and replacement wave fixtures |
| K7 Minas Morgul | P1 | Army retains Army/Orc and gains Wraith under shadow counter | Pay {3}{B} and tap land; shadow evasion with actual blockers |
| E1 opponent-spell amass | P1 | Opponent casts, not resolving spell, drives Sauron | Three-opponent cast-turn ordering and priority |
| E2 Ring draw | P1 | Optional discard hand and only then draw 4 modeled | Multiple simultaneous Nazgûl/Throne triggers and changing hand |
| W1 Army combat | P1 | Only actual combat damage to a PLAYER by Army tempts; blocked and noncombat damage negative controls | Attacking/blocked/shadow/flying/trample state and lethal accounting |
| W2 The Great Goblin | P1 | Per event, not per counter, asserted | Opponent life/target damage and loss/prevention handling |
| F2 quiet opponents | P1 | Zero opponent casts yields no commander amass, Call/Nazgûl still relevant | Real 2-3-turn adversarial low-spell fixture |
| F3 sweepers | P1 | Loss of Ozolith noted; Army token disappears after destruction | Actual mass-removal resolution and recovery next turn |

## Exact candidate changed-card follow-through

### New executable correspondence (16/16 local PASS)

Each original named blueprint case is explicitly linked to one actually
executed Python unittest method. These are independent **new** candidate
checks; the historical blueprint's design-only flags remain unchanged.

| Original cases | Executed `TestDeck50Cases.test_…` method |
|---|---|
| C1 | `C1_commander_zones_stack_and_optional_reset` |
| K1 | `K1_ward_sacrifice_paid_on_target_and_not_on_sweeper` |
| K2 | `K2_cast_even_if_countered_and_throne_priority` |
| K3 | `K3_mauhur_exactly_one_per_counter_event` |
| F1 | `F1_no_claimed_compact_infinite_win_and_counterspell_window` |
| K4 | `K4_great_goblin_event_and_adversarial_removal` |
| K5 | `K5_throne_wraith_bridge_vs_without_adaptation` |
| K6 | `K6_seven_nazgul_and_temptation_waves` |
| K7 | `K7_minas_morgul_cost_tap_shadow_and_army_identity` |
| E1 | `E1_three_opponent_casts_source_paid_nonloop` |
| E2 | `E2_paid_birthday_escape_vs_invalid_soothing_target` plus C1 reset |
| W1 | `W1_trample_and_shadow_need_actual_damage_to_player` |
| W2 | `W2_goblin_pings_source_changed_from_cut_widespread` |
| F2 | `F2_quiet_opponents_keep_call_and_ring_dependent_engine` |
| F3 | `F3_sweeper_loses_army_token_and_reanimates_nontoken_only` |
| Changed cards | `changed_discard_package_paid_zones_mana_damage_draw` |

P0 F1 is a **bounded named-line exclusion**, not mathematical proof that no
unknown infinite combo exists. Historical W2's Widespread Brutality and F3's
Ozolith were **cut** in this candidate; the test substitutes actual Lazotep
Plating and the revised no-Ozolith wipe state, without claiming those older
card-specific scenarios were executed unchanged.

- **Arcane Adaptation:** choosing Wraith affects all controlled creatures, including Orc Army, so the Nazgûl pump applies to Army only while Adaptation survives. Removing Adaptation in response can eliminate type before the trigger resolves. It does **not** itself trigger Ring temptation.
- **Lord of the Nazgûl:** creates Wraith tokens on *our* instant/sorcery spells, not opponents' casts. The nine-Wraith bonus requires controlling the threshold; no automatic nine Wraiths are assumed.
- **Bone Miser:** Sauron's one hand-discard choice creates one discard event per discarded card; Bone Miser's effects follow actual discarded card types. Sources cannot spend mana from a later trigger to pay earlier costs.
- **Moonstone, Harsh Mistress:** discard-to-exile is optional, cards remain subject to normal playing costs and timing, and choosing exile eliminates those cards as ordinary graveyard reanimation targets.
- **Glint-Horn Buccaneer:** discards each deal 1 to EACH opponent if Buccaneer survives while triggers resolve; no burn if commander draw trigger is declined or no cards discarded.
- **Herald of Secret Streams:** an amass counter makes Army unblockable while Herald persists; no false unblockable claim after Herald removal, or on zero-counter bodies.
- **Lazotep Plating:** two mana produces hexproof for player and permanents and amass Zombie 1, but does not counter untargeted destruction/exile or save a creature from damage.
- **Birthday Escape/Soothing of Sméagol:** actual spell resolution creates one Ring temptation; Soothing needs a legal nontoken creature target and can be fizzled if the only target becomes illegal.
- **Cavern of Souls:** Avatar chosen supports Sauron uncounterability and colored casting. It cannot be treated as a universal UBR source for other card types.

## Fail-closed status and next bounded action

The new verifier covers exact card identities/structure and finite tabletop
interactions; current whole-name Scryfall check is performed in PR CI.
The historical I/J receipt explicitly lacks downstream sealed replay and
global milestone acceptance; nothing here silently converts it into those.
The **fifteen case-level candidate checks now actually execute** as mapped
above, and the full-99 M7 decision packet passes the repository structural
gate locally. Before owner presentation, exact PR-head CI must pass these
new tests, the updated decision gate and current 91-name official legality.
Until then, this engineering branch is **PENDING EXACT-HEAD CI / NOT
APPROVED**, with the historical canonical source intact.
