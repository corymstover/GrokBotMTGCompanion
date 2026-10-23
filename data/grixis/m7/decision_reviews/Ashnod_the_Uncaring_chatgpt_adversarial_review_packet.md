# Ashnod the Uncaring — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

Reviewer instruction: attack this list. Show any rules error, illegal card, unpayable line, unsupported combo claim, or a
candidate that clearly beats an incumbent. No win rates were measured; EDHREC prevalence is discovery evidence only.

## Provenance
- Canonical source (read-only): `corymstover/grixis-commander-encyclopediaGPT`
  `refinement/decklists/Ashnod_the_Uncaring_Approved_2026-10-13.txt` (commit 1836b97), raw SHA-256
  `f574e4fad4749603294f53d2fe5536a159f884a8f1a8a7b6b1a22b3a637cf1cf`, vendored byte-exact at
  `data/grixis/m7/baseline_sources/Ashnod_the_Uncaring_approved_source_2026-10-13.txt`.
- Registry `recorded_sha256` equals the raw bytes (`recorded_matches_raw: true`), so **no provenance exception** is used.
  Baseline logical hash equals the registry: `lh1:539266aa…9ecd`.
- Physical count: 95 rows = 100 cards (Island x3, Mountain x2, Swamp x3); 33 lands, 9 static rocks.
- Tracker discrepancies (disclosed, raw hash authoritative): the tracker's "once-per-turn" note on Ashnod is stale (current
  Oracle has no turn limit); `state/current_deck_overrides.json` mentions "three current-cycle swaps" while the tracker
  records one (Commander's Sphere → Trading Post). Overrides were not altered.
- Candidate: `data/grixis/m7/candidate_lists/Ashnod_the_Uncaring.txt`, raw
  `b1078f084c2fa53426910edb66f0a036978e06bd9c9a2061f460af397503143d`,
  `lh1:4ac4aed8ba1db6c913f19396e7d8a04645b3035bfe387cb8b04b694e5bfc862f`. Baseline order, five in-place substitutions.
- Live Scryfall data (2026-10-23) lives only in the candidate snapshot (102 cards; zero Oracle diffs vs the frozen cache).
  The frozen cache was not written. All cards are Commander-legal and within UBR.
  Game Changers (6, unchanged): Ancient Tomb, Bolas's Citadel, Cyclonic Rift, Demonic Tutor, Fierce Guardianship,
  Vampiric Tutor → **Power Bracket 4**.

## Commander model (attack this first)
- Ashnod: "Whenever you activate an ability of an artifact or creature that isn't a mana ability, if one or more permanents
  were sacrificed to activate it, you may copy that ability. You may choose new targets for the copy." No turn limit.
- Not copied: mana abilities (CR 605.1a: KCI, Ashnod's Altar, Lotus Petal, Treasure), land abilities (Buried Ruin,
  Inventors' Fair, fetches — but artifact lands like Treasure Vault are artifacts and are copied), and sacrifices made on
  resolution (Goblin Welder). Priest of Forgotten Gods targets, so it is not a mana ability and its BB is copied.
- Copies are not activated (CR 707.10): sorcery timing and {T}/summoning sickness apply only to the original.

## Swaps (5 — the floor, not padded)
| Add | Cut | Why |
|---|---|---|
| Corridor Monitor | Foundry Inspector | Completes Ashnod + Goblin Engineer + Monitor + Lotus Petal (Spellbook 1414-1649-2068-4404): copy returns Monitor, which untaps Engineer; mana-neutral, infinite artifact ETB/sacrifice (Disciple, Marionette Apprentice, Mayhem Devil, Fireweaver; Novelist → infinite R). Inspector is the third cost reducer; its two Spellbook variants survive via Sculptor/Mechanaut. |
| Aether Spellbomb | Fellwar Stone | Both modes sacrifice: copied bounce hits two creatures at instant speed, or draw two for {1}. EDHREC 62%. |
| Audacious Reshapers | Talisman of Indulgence | {T}, sacrifice an artifact: reveal until an artifact and put it onto the battlefield; copied = two free artifacts per activation. EDHREC 36%. |
| Priest of Forgotten Gods | Walking Ballista | Copied: each targeted opponent loses 4 and sacrifices two creatures, we add BBBB and draw two. Ballista's abilities never sacrifice, so Ashnod never copies them. EDHREC 21%. |
| Thopter Squadron | Esoteric Duplicator | Ashnod + Squadron + Crime Novelist + Ashnod's Altar or KCI (2034-2068-2762-5346 / 2068-2762-4659-5346): copied +1 counter nets +1 mana per two-Thopter cycle at sorcery speed. **Duplicator (EDHREC 43%) is the notable loss.** |

Net: lands 33 → 33, rocks 9 → 7 (42 → 40 static sources). Artifacts 43 → 41; noncommander creatures 25 → 27.
Pips U/B/R 18/13/14 → 18/14/15. Average nonland MV 2.212 → 2.258. P(≥5 lands-or-rocks in top 11, Ashnod turn 5 on the draw)
0.537 → 0.479.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline: 15 included combos, **none uses Ashnod**. Candidate: 16 (+3 Ashnod lines above, −2 Foundry Inspector
  variants 777-1020-2866-4659 and 777-1020-2034-2866, whose Trawler/Retriever lines remain with Sculptor/Mechanaut).
- All new lines are 3–4 cards including the commander; no two-card infinite. The baseline already had infinite combos, so
  the bracket is unchanged at 4. "Almost" combos are not counted.

## Weakest points (please push here)
1. **Mana:** two fewer rocks for a five-mana commander; about 5–6 points worse on-curve Ashnod odds before KCI/Altar/
   Novelist/Treasure Vault mana.
2. **Losses:** Esoteric Duplicator's token copies and draw, Walking Ballista's flexibility, Foundry Inspector, two rocks.
3. **Graveyard hate** blanks the Engineer/Monitor/Petal loop and the welders/Trawler/Retriever lines (Squadron's loop survives).
4. **Artifact hate** (Collector Ouphe, Null Rod) stops Spellbomb, Squadron and Engineer activations; Priest still works.
5. **Pass C argued against replacing the Ashnod-doubled Krark-Clan Shaman sweeper.** This candidate keeps Shaman; the same-count
   alternative that cut Shaman for Priest was rejected.

## Tested pool (6 full 100s; `data/grixis/m6/ij/tested_pools/Ashnod_the_Uncaring_M7_tested_configurations_20261023.json`)
BASELINE; PREFERRED_FIVE (selected); FIVE_ALT_PRIEST_OVER_KRARK_CLAN_SHAMAN (REJECT — Shaman is the copyable sweeper);
SIX_SAGE (Sage of Lat-Nam over Jhoira, RETAIN_ALTERNATIVE); SIX_SPIRE (Spire of Industry over Exotic Orchard,
RETAIN_ALTERNATIVE); SEVEN_SAGE_SPIRE (staged, not selected — padding).
Post-floor challenges also rejected: Mirkwood Bats, Marionette Master, Voltaic Key, Burnished Hart, Skullclamp, Fain,
Mindslaver, Commander's Sphere. Other named rejections: Manifold Key, Courier's Capsule. Excluded as invalid: Paradox Engine (banned).

## Infra disclosure
- Gate, schema and gate-test files are byte-identical to PR #653 head fee682f3.
- `scripts/grixis_m6_bundle_check.py` (after #653) gains two narrow, fail-closed additions, both pinned by
  `tests/test_m6_ashnod_the_uncaring_m7_ij.py`:
  1. A strict parenthetical pattern accepting only `technical third-model independence (… independent=FALSE …)`, vetoed by
     any `independent=TRUE/YES` or explicit TRUE/YES statement. Among all 62 receipts it newly accepts only Ashnod's.
  2. A one-to-one mapping for the legacy `A_SEAL` Stage A seal field names Ashnod's immutable seal uses
     (`canonical_approved_sha256`, `first_stage_git_commit_sha`, `formal_pass_c_classification`, `technical_independence`,
     `actual_model`). Values are never rewritten; seals with both names are rejected; every other seal is unchanged.
- **Forward note:** 57 of 62 Stage A seals use non-canonical field names, and many receipts (including Deck #7 Be'lakor)
  match none of the accepted disclosure wordings. Later decks will need their own narrow fixes.
- **Merge order:** #651 → #652 → #653 → this PR.
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
