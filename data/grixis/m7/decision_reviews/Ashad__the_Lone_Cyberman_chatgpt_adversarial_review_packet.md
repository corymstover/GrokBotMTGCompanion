# Ashad, the Lone Cyberman — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

Reviewer instruction: attack this list. Show any rules error, illegal card, unpayable line, unsupported combo claim, or a
candidate that clearly beats an incumbent. No win rates were measured; EDHREC prevalence is discovery evidence only.

## Provenance
- Canonical source (read-only): `corymstover/grixis-commander-encyclopediaGPT`
  `refinement/decklists/Ashad_the_Lone_Cyberman_Approval_Ready_2026-10-13.txt`, raw SHA-256
  `087e34c2127859111fc08f8d9ec7d66cd3495537cc571d88e829fd27d2823e25`, vendored byte-exact at
  `data/grixis/m7/baseline_sources/Ashad_the_Lone_Cyberman_approved_source_2026-10-13.txt`.
- Registry `recorded_sha256` equals the raw bytes (`recorded_matches_raw: true`), so **no provenance exception** is used.
  Baseline logical hash equals the registry: `lh1:6d87a5e4…6f5b`.
- Physical count: 95 rows = 100 cards (Island x3, Mountain x2, Swamp x3); 30 lands, 9 static rocks.
- Candidate: `data/grixis/m7/candidate_lists/Ashad__the_Lone_Cyberman.txt`, raw
  `dfd1158c79668c2dcd85137219bd00bdc75cd855697cf31dfb9b5ff93552597d`,
  `lh1:672c3945d8fd2f44a7d03dce4672b9d4aa25391a26b8c1607b5242ca05cc946f`. Baseline order, five in-place substitutions.
- Live Scryfall data (2026-10-23) lives only in the candidate snapshot (112 cards; zero Oracle diffs vs the frozen cache).
  The frozen cache was not written. All cards are Commander-legal and within UBR.
  Game Changers (3, unchanged): Cyclonic Rift, Demonic Tutor, Fierce Guardianship → **Power Bracket 4**.

## Commander model (attack this first)
- Ashad: "The first nonlegendary artifact spell you cast each turn has casualty 2 … Whenever you sacrifice another
  creature, put a +1/+1 counter on Ashad." Casualty (CR 702.153a) is an optional additional cost: sacrifice a creature
  with power 2 or greater; the copy becomes a token (CR 608.3f) but is **not cast and not "created"** (no Helm doubling).
- The slot is consumed by the first nonlegendary artifact spell even with no fodder or if it is countered.
- Unearthed Royal Warden sacrificed for casualty is exiled instead, but Ashad still gets the counter.

## Swaps (5 — the floor, not padded)
| Add | Cut | Why |
|---|---|---|
| Skullclamp | Fellwar Stone | Ninth rock → repeatable draw. Lifts 1-power bodies (Emry, Etherium Sculptor, Padeem, Pitiless Plunderer, Urza) to casualty-legal power 2; kills 1-toughness bodies for two cards. |
| Piggy Bank | Reckless Fireweaver | 3/2 artifact for 2; fodder that leaves a Treasure. Fireweaver (1/3, nonartifact) can't pay casualty. |
| Razorlash Transmogrant | Thoughtcast | 3/1 artifact for 2, recursive fodder ({B}{B} if an opponent has ≥4 nonbasics, else {4}{B}{B}). |
| Necron Deathmark | Marionette Master | Flash 5/3 artifact: destroy a creature + mill 3, copyable on opponents' turns. Marionette (nonartifact, 1/1 Servos) can't be copied; **its drain is the biggest loss**. |
| Royal Warden | Thopter Spy Network | Three bodies (two 2/2 artifact tokens), six with a casualty copy; unearth. Spy Network's 1/1 Thopters can't pay casualty. |

Net: lands 30 → 30, rocks 9 → 8 (39 → 38 static sources). Nonlegendary artifacts 37 → 41; power-2+ creature cards 17 → 21.
Pips U/B/R 35/16/13 → 32/18/13. Average MV 3.406 → 3.348. P(≥4 sources in top 10) 0.610 → 0.583.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline complete combo kept: Urza + Worldwalker Helm + Artificer Class (66-457-5491).
- **New:** Razorlash Transmogrant + Pitiless Plunderer + Phyrexian Altar (4050-4871-6429). **Conditional** on an opponent
  controlling ≥4 nonbasic lands. Altar gives {B}, Plunderer's Treasure gives {B}: mana-neutral loop; payoffs Mayhem Devil,
  Disciple of the Vault, Ashad counters. Three cards, not two; disclosed for bracket. "Almost" combos are not counted.

## Weakest points (please push here)
1. **Mana:** one fewer rock and more black pips; colored land sources U/B/R 18/16/14 unchanged.
2. **Losses:** Marionette Master drain, Fireweaver pings, Spy Network card flow and post-wipe rebuild, Fellwar mana.
3. **Graveyard hate** blanks Razorlash recursion, the conditional loop, Warden unearth and the welders.
4. **Artifact hate** (Collector Ouphe, Stony Silence, Vandalblast) hits Skullclamp; bodies still pay casualty.

## Tested pool (6 full 100s; `data/grixis/m6/ij/tested_pools/Ashad__the_Lone_Cyberman_M7_tested_configurations_20261023.json`)
BASELINE; PREFERRED_FIVE (selected); FIVE_ALT_RAZORLASH_OVER_DISCIPLE (REJECT — Disciple is the drain payoff);
SIX_PATROL (Cyberman Patrol over Ichor Wellspring, RETAIN_ALTERNATIVE); SIX_KEEPER (Treasure Keeper over Auton Soldier,
off-ranked, RETAIN_ALTERNATIVE); SEVEN_PATROL_KEEPER (staged, not selected — padding).
Post-floor challenges also rejected: Three Steps Ahead over Artificer Class, Missy over Cybermen Squadron.
Named single-card rejections: Dalek Drone, Skorpekh Lord, Thran Dynamo, Spire of Industry, Ultron, Filigree Familiar.
Excluded as invalid: Golos, Bio-Asset Allocator.

## Infra disclosure
- Gate/schema/test files were reused byte-identical from PR #652 head a6798cf2 (themselves from PR #651).
- `scripts/grixis_m6_bundle_check.py` gains one **strict, case-insensitive** pattern accepting only an explicit
  FALSE/NO technical-independence statement (Ashad's preserved `technical independence FALSE`), vetoed by any
  explicit TRUE/YES statement. The four existing accepted substrings are unchanged (superset of #652). Tests show TRUE,
  ambiguous ("unknown", "not assessed", "no longer…", "NOT FALSE"), missing and contradictory wording still fail.
- **Pre-existing, not changed:** the legacy substring "Technically independent third model" is permissive on its own.
- **Merge order:** #651 → #652 → this PR.
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
