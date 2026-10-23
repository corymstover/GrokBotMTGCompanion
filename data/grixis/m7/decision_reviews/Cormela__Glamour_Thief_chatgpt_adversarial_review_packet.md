# Cormela, Glamour Thief — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

**Reviewer instruction:** attack this list. Show any rules error, illegal card, unpayable line, unsupported combo claim, or a
candidate that clearly beats an incumbent. No win rates were measured, and EDHREC prevalence is discovery evidence only.

## Provenance
- **Canonical source (read-only):** `corymstover/grixis-commander-encyclopediaGPT`,
  `refinement/decklists/Cormela_Glamour_Thief_Approved_2026-10-14.txt` (commit 1836b97).
  - Raw SHA-256: `80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b`.
  - Vendored byte-exact at `data/grixis/m7/baseline_sources/Cormela__Glamour_Thief_approved_source_2026-10-14.txt`.
- **Hashes:** the registry's `recorded_sha256` equals the raw bytes (`recorded_matches_raw: true`), so **no provenance exception** is used.
  - Logical `lh1:545b22ca…7b6` = registry `baseline_hash` = `current_canonical_hash` = canonical project list hash.
  - The registry export `exports/grixis-archidekt/cormela-glamour-thief.txt` is the same 100 with a `1 ` quantity prefix
    (different raw bytes, same logical hash).
- **Count convention:** 100 = 1 commander + 99 library; no companion; every name is a single copy. 30 lands, 13 mana artifacts.
- **Candidate:** `data/grixis/m7/candidate_lists/Cormela__Glamour_Thief.txt` (baseline order, five in-place substitutions).
  - Raw: `1cb098f4d1089f6989dfdb79b4abcd149000dfa5f90b923bda72ffa36aa2c8b1`.
  - Logical: `lh1:ed41bb16fe9c22a42cc13f9084b0feb192cb5937878049e89417c155110219a7`.
- **Live data:** live Scryfall (2026-10-23, /cards/collection) is only in the candidate snapshot and research files. The frozen cache was not written.
- **Legality:** every card is Commander-legal on live Scryfall and within UBR. No project exception is used.
- **Game Changers (20, unchanged):** Ad Nauseam, Ancient Tomb, Chrome Mox, Demonic Tutor, Fierce Guardianship, Force of Will, Gamble,
  Imperial Seal, Intuition, Jeska's Will, Lion's Eye Diamond, Mana Vault, Mox Diamond, Mystical Tutor, Necropotence, Orcish Bowmasters,
  Rhystic Study, Thassa's Oracle, Underworld Breach, Vampiric Tutor → **Power Bracket 5** (cEDH).

## Commander model (attack this first)
- **Cormela, Glamour Thief** ({1}{U}{B}{R}, 2/4 haste): "{1}, {T}: Add {U}{B}{R}. Spend this mana only to cast instant and/or sorcery
  spells." When she dies, return up to one target instant or sorcery card from our graveyard to hand.
- **The restriction is the design problem.** Her mana cannot pay for activations, artifacts or creatures. This list adds cards that
  turn it back into unrestricted mana or reuse her death trigger.
- **Frantic Search ({2}{U}):** paid entirely with Cormela's UBR, it untaps three lands, a net gain of +2 unrestricted mana plus a loot.
  In the Saw in Half loop it is net −1, so it is **not** an infinite piece.
- **Twinflame loop:** Twinflame makes a hasty token copy of Cormela. The legend rule (704.5j) puts one Cormela in the graveyard, and its
  dies trigger returns Twinflame. The token taps for UBR, which recasts Twinflame. Each iteration costs −1 unrestricted (the {1}) and nets
  +1 restricted mana. It is **finite alone**. With Birgi it is infinite (Spellbook 392-1235-4867), and Dualcaster Mage + Twinflame is
  infinite (147-1235). Twinflame + an altar is **not** claimed as infinite.
- If Cormela is in exile or the library, her dies trigger is lost (903.9a lets the commander go to the command zone instead).

## Swaps (5 — the floor, not padded)
| Add | Cut | Why |
|---|---|---|
| Mistrise Village | Undercity Sewers | Untapped with any of 5 Mountain-typed lands (all 7 fetches find one). {U},{T} makes the key spell uncounterable. Sewers is the only always-tapped land. |
| Underground River | Exotic Orchard | Guaranteed untapped U/B. Orchard depends on what opponents' lands make. |
| Frantic Search | Faithless Looting | Pays with Cormela's restricted mana and nets +2 unrestricted mana. Looting is card disadvantage at sorcery speed. |
| Twinflame | Gitaxian Probe | Commander-centric loop with Birgi or Dualcaster (two new Spellbook combos). Probe has no Cormela synergy. |
| Hexing Squelcher | Red Elemental Blast | Spells we control can't be countered on the combo turn, and Cormela gets ward (pay 2 life). REB duplicates Pyroblast. |

**Net:** lands 30 → 30 (always tapped 1 → 0); rocks 13 → 13; library creatures 5 → 6; instants/sorceries 46 → 45.
Curve by MV 0/1/2/3/4/5: 6/25/18/16/2/2 → 6/22/20/17/2/2. Average nonland MV 1.841 → 1.899.
Heuristic U/B/R sources 19/18/17 → 19/17/16. P(2–5 lands in 7) 0.683 → 0.683.
**Losses:** Sewers' surveil, Orchard's off-color reach, Looting's flashback, Probe's free storm count and peek, and the second blue hoser.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline: 23 included combos, all kept, including Thassa's Oracle + Demonic Consultation or Tainted Pact; Breach + Brain Freeze with
  Lotus Petal or LED; Breach + Wheel of Fortune lines; Cormela + Saw in Half + Dark Ritual / Cabal Ritual / Seething Song / Jeska's Will;
  Cormela + Demonic Gifts, Goryo's Vengeance or Shallow Grave + an altar; Dualcaster lines; and Cormela + Birgi + Molten Duplication.
- The candidate has 25: **+147-1235 (Dualcaster Mage + Twinflame)** and **+392-1235-4867 (Cormela + Birgi + Twinflame)**.
  Infinite claims are limited to Spellbook-listed lines. Every line can be interrupted (removal, Stifle effects, graveyard hate).

## Weakest points (please push here)
1. **Hexing Squelcher is a 2-mana creature** in a deck whose commander's mana can't cast it. It dies to Bowmasters-style pings and wipes.
   The staged four-swap (keep REB) is the fallback.
2. **Twinflame requires Cormela on the battlefield**, and the token needs haste to tap (Twinflame grants it). It is dead alone without Birgi or Dualcaster.
3. **Mistrise Village enters tapped** without a Mountain. It is untapped with 5 Mountain-typed lands in play, and all 7 fetches can find one, but opening hands without either exist.
4. **Underground River** costs life, and the deck already takes damage from Mana Confluence, shocks, Ancient Tomb and fetches.
5. **Pass C** (owner-equivalent, NOT technically independent) final disposition was **KEEP, no swap**. Its own challenger, Muddle the
   Mixture over Seething Song, is staged and **rejected** here (Song is a converter and an infinite piece). This candidate disagrees with
   the KEEP on five different slots, so it needs owner review.

## Tested pool (7 configurations; `data/grixis/m6/ij/tested_pools/Cormela__Glamour_Thief_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100) and CANONICAL_EXPORT (registry export, same logical hash).
- PREFERRED_FIVE (selected).
- FOUR_WITHOUT_HEXING_SQUELCHER (REJECT: REB duplicates Pyroblast).
- SIX_PASS_C_MUDDLE_OVER_SONG (REJECT: Song is a converter and an infinite piece).
- SIX_ABRADE_OVER_PREORDAIN (RETAIN_ALTERNATIVE, staged, not selected).
- SEVEN_BURNT_OFFERING_OVER_WINDFALL (RETAIN_ALTERNATIVE, staged, not selected).

Other named rejections: Verdant Catacombs, Arid Mesa, Lim-Dûl's Vault, Grim Monolith, Mana Drain, Mox Amber, Defense Grid,
Galvanic Iteration, Spellseeker, Ragavan, The One Ring, Culling Ritual.

## Distinctness
This is different from Anhelo (the first instant or sorcery each turn gets casualty 2, a copy engine) and Cecily (an eleven-card-hand attack trigger). Cormela's
plan is converting restricted instant/sorcery mana and recurring spells through her death trigger.

## Infra disclosure
- No shared-infrastructure change in this PR. The gate, schema, gate test, Pass C corpus test and `scripts/grixis_m6_bundle_check.py`
  (SHA-256 `2962a640…`) are byte-identical to PR #656 head 14f33de8. The checker already enumerates this deck's preserved Pass C wording
  ("**not a technically independent third model**").
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → this PR.
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
