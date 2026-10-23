# Cecily, Haunted Mage + Bjorna, Nightfall Alchemist (companion Lutri) — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

**Reviewer instruction:** attack this list. Show any rules error, illegal card, unpayable line, unsupported combo claim, or a
candidate that clearly beats an incumbent. No win rates were measured, and EDHREC prevalence is discovery evidence only.

## Provenance
- **Canonical source (read-only):** `corymstover/grixis-commander-encyclopediaGPT`,
  `refinement/decklists/Cecily__Bjorna__Lutri_Approved_2026-10-13.txt` (commit 1836b97).
  - Raw SHA-256: `553838da88fe00974e74664633be5051c4f1a0879baa71de81ca9f880e5a6d28`.
  - Vendored byte-exact at `data/grixis/m7/baseline_sources/Cecily__Bjorna__Lutri_approved_source_2026-10-13.txt`.
- **Hashes:** the registry's `recorded_sha256` equals the raw bytes (`recorded_matches_raw: true`), so **no provenance exception** is used.
  - The raw 100 has no Lutri line: logical `lh1:f1a44d6b…dac5` = registry `baseline_hash`.
  - The registry's canonical project list adds `1 Lutri, the Spellchaser [Companion]` (the source approval record designates
    Lutri as companion outside the 100). Logical `lh1:030933b5…f507` = registry `current_canonical_hash` = sealed A/B list hash.
    Bound via `exports/grixis-archidekt/source-baseline/bjorna-nightfall-alchemist-cecily.txt`.
- **Count convention:** 100 = 2 commanders + 98 library; 1x Lutri, the Spellchaser [Companion] outside the 100. Island x2 is the only
  repeated name. 33 lands, 9 rocks.
- **Candidate:** `data/grixis/m7/candidate_lists/Cecily__Bjorna__Lutri.txt` (baseline order, six in-place substitutions, companion line kept).
  - Raw: `2cc7227f954e728e0b37949b74f9575128b2c82250f53e211289aa60e4fa1717`.
  - Logical: `lh1:514596aaf599116e15083596021e97a0dc24b1c03b2b51f341ed6f927576e5e3`.
- **Live data:** live Scryfall (2026-10-23, /cards/collection) is only in the candidate snapshot and research files. The frozen cache was not written.
- **Legality truth:** live Scryfall lists Trade Secrets and Yawgmoth's Bargain as **banned** in Commander, and Lutri as "legal" only
  because Scryfall does not encode the Commander companion ban. All three are **documented project exceptions for this deck only**,
  never officially legal, never applied elsewhere. Every other card is Commander-legal and within UBR.
- **Game Changers (10, unchanged):** Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Mystical Tutor, Notion Thief,
  Rhystic Study, The One Ring, Underworld Breach, Vampiric Tutor → **Power Bracket 4**.

## Commander model (attack this first)
- **Cecily, Haunted Mage:** maximum hand size eleven. Whenever she attacks, draw a card and lose 1 life; *then*, if we have eleven or
  more cards in hand, we may cast an instant or sorcery spell from hand without paying its mana cost. The hand check is part of the
  resolving effect, not an intervening-if (603.4), so a ten-card hand reaches eleven with the draw.
- **Copies:** a copied trigger (Strionic Resonator, Echo, Harmonic Prodigy's extra trigger for a Wizard) resolves separately: draw, lose
  1, re-check, free cast. The free-cast spell is cast (magecraft, Lutri apply); a copy of a spell is not cast (707.10).
- **Bjorna, Nightfall Alchemist:** {T}, sacrifice an artifact: 1 damage to target creature and goad it. Echo can copy this activation
  (creature source) for {1}; the sacrifice is a cost and is not repeated.
- **Lutri:** pay {3} at sorcery speed to put it into hand (companion special action, 116.2g; 702.139a), then cast for {1}{U/R}{U/R}; its ETB copies a spell we cast.

## Swaps (6 — the five-swap floor plus one post-floor swap, not padded)
| Add | Cut | Why |
|---|---|---|
| Strionic Resonator | Emry, Lurker of the Loch | Copies Cecily's attack trigger: two free casts from a ten-card hand. Pass C's own challenger, but cutting Emry keeps In Garruk's Wake. |
| Echo, Perceptive Prodigy (OFF-RANKING) | Goblin Engineer | {1},{T} with vigilance copies Cecily's trigger while attacking, and Bjorna's ping/goad. Engineer has few artifact targets. |
| Twenty-Toed Toad (OFF-RANKING) | Sai, Master Thopterist | Turns the big hand into a win (Spellbook 1561-5850 with Peer). Sai's Thopters are low impact here. |
| Sea Gate Restoration // Sea Gate, Reborn | Dark Deal | Land in bad hands, free-cast hand-plus-one draw in good ones. Dark Deal shrinks our own hand. |
| Deflecting Swat | Mana Geyser | Free (commander out) redirect that protects the attack turn. Geyser is a one-shot ritual. |
| Mana Drain | Seething Song | Counter plus delayed mana for Lutri or post-combat spells. Song is a one-shot ritual. |

**Net:** lands 33 → 33 (+ Sea Gate MDFC); rocks 9 → 9; creatures 16 → 15; artifacts 16 → 17; instants/sorceries 30 → 30.
Pips U/B/R 36/21/29 → 41/20/26. Average nonland MV 3.338 → 3.369. P(2–5 lands in 7) 0.747 → 0.764.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline: 1368-1878-2706 (Underworld Breach + Wheel of Fortune + Jeska's Will; finite — Breach exiles three other cards per escape),
  1561-2384 (Psychosis Crawler + Peer into the Abyss), 1561-5042 (Peer + Teferi's Ageless Insight; self-deck risk).
- Candidate adds one: **1561-5850, Twenty-Toed Toad + Peer into the Abyss ("Win the game")**. Deterministic attack-trigger alternate
  win, not an infinite. No infinite combo is claimed anywhere.

## Weakest points (please push here)
1. **Two copiers plus Harmonic Prodigy:** is a fourth Cecily trigger ever needed? Each copy needs another castable spell in hand.
2. **Echo is a creature:** it dies to every wipe and must not be summoning sick to activate.
3. **Toad + Peer needs the free cast or seven mana,** and Peer costs half our life. Toad must survive a turn cycle.
4. **Rituals cut:** Apex of Power / Mnemonic Deluge cast by hand gets harder without Geyser and Song.
5. **Pass C** (owner-equivalent, NOT technically independent) disposition NEEDS TESTING for Resonator over In Garruk's Wake. This
   candidate tests Resonator with a different cut (Emry) and keeps Wake; the Pass C pairing itself is staged and rejected.

## Tested pool (7 configurations; `data/grixis/m6/ij/tested_pools/Cecily__Bjorna__Lutri_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100, no companion line) and CANONICAL_WITH_COMPANION (registry export).
- PREFERRED_SIX (selected).
- FIVE_FLOOR_WITHOUT_MANA_DRAIN (REJECT: Song's burst is one-shot).
- SIX_PASS_C_RESONATOR_OVER_WAKE (REJECT: keeps Emry, loses the one-sided wipe Pass C defended).
- SEVEN_ENTER_THE_INFINITE (RETAIN_ALTERNATIVE, staged, not selected).
- SEVEN_PETER_PARKERS_CAMERA (RETAIN_ALTERNATIVE, staged, not selected).

Other named rejections: Arcane Denial, Reliquary Tower, Gogo, Spellbook, Lithoform Engine, Double Vision, Veyran, Necrodominance,
Fevered Suspicion, Hit the Mother Lode, Swan Song, Wizard Class, Time Stretch, Library of Leng, Galvanic Iteration, Whispersilk Cloak.

## Infra disclosure
- No shared-infrastructure change in this PR. The gate, schema, gate test and `scripts/grixis_m6_bundle_check.py` (SHA-256 `2962a640…`)
  are byte-identical to PR #655 head ce713a71. The checker already enumerates this deck's preserved Pass C wording
  ("Technical independent model FALSE").
- **Merge order:** #651 → #652 → #653 → #654 → #655 → this PR.
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
