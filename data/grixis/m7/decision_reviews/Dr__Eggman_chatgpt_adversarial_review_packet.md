# Dr. Eggman — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

**Reviewer instruction:** attack this list. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a candidate that clearly beats an incumbent;
- an owner-direction contradiction we missed.

No win rates were measured, and EDHREC prevalence is discovery evidence only.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Dr_Eggman_Approved_2026-10-14.txt`, git blob `86119caf033b605bf0d30017c8bd06b6a63a3c0c`, frozen by canonical commit `8883de3`.
- Canonical commit record: the bytes were fetched and verified at 9b26aa28. The registry's source commit field says `1836b97`, the import commit, which carries the same bytes.
- Raw SHA-256 `ef34986253f71043e10c852b5f9f3ce79594fdfc1086b105f6744c3f639199c3`. This equals `state/current_deck_overrides.json` `approved_list_sha256`, the tracker (index 14) and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Dr__Eggman_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:04e4d973c9055eda049e943fc333e8642f24a11a20b61c77437127c6cf1b9e95`.
- The registry export `exports/grixis-archidekt/dr-eggman.txt` (raw `7110223f41570f87c3e5aa879cb46f2727ab94c43f96163cd861f2561882744a`) is the same 100 in export format ("1 " instead of "1x ", sorted), with the same logical hash.

**Discrepancies.** None in the hashes. The candidate is written commander-first, then alphabetical.

**Count convention.** 100 = 1 commander + 99 library; no companion.
- 31 lands: Island, Mountain and Swamp ×2 each, plus 25 nonbasic (97 rows).
- Rocks: Sol Ring, Arcane Signet, Fellwar Stone, Mox Opal and three Talismans in both lists.

**Candidate.** `data/grixis/m7/candidate_lists/Dr__Eggman.txt`: commander first, then alphabetical; five substitutions.
- Raw `85bcd5a250c097a8b94322416c85272a8550728a43edc9a257b7fbd39823f792`.
- Logical `lh1:c092a5e2…` (full value in the tested pool).

**Live data.** Live Scryfall `/cards/collection` was queried on 2026-10-23 for the 97 baseline rows and 150 evaluated names. An off-ranking type search (Construct/Robot/Vehicle within UBR, 458 hits) was also run.
- The live results are stored only in the candidate snapshot and the research files; the frozen cache was not written.
- Oracle text and oracle_id show zero differences against the frozen `oracle-cards-20261016090200` snapshot for all 239 snapshot names (double-faced cards compared face by face).
- Tri-Sentinel and Ravage, Bomber of Tiamat did not resolve on live Scryfall and were dropped.

**Legality.** Dr. Eggman (Secret Lair `sld`, released 2025-07-14) is Commander-legal on live Scryfall, and so is every card in all nine configurations, all within UBR. **No project exception is used.**

**Game Changers.** 3 in the baseline and the candidate: Ancient Tomb, Cyclonic Rift, Fierce Guardianship. **Power Bracket 4.**

**Archidekt tags.** Villainous Choice, Robots, Artifact Cheat.

## Commander model (attack this first)
**Dr. Eggman** is a {2}{U}{B}{R} 3/6 flying Legendary Creature — Human Scientist. Its Oracle text: "At the beginning of your end step, draw a card. Then each opponent faces a villainous choice — That player discards a card, or you may put a Construct, Robot, or Vehicle card from your hand onto the battlefield."

Rules points:
- **701.55a–d.** Each opponent chooses in turn; an impossible option can be chosen (an empty hand "discards" nothing), and The Valeyard adds choices, not draws.
- **Put is not cast** (601.2). Cast triggers and cost reductions don't apply; Cityscape Leveler is the only cast-only payload.
- **603.6a.** Enters triggers fire on a put: Possession Engine, Skysovereign, Interceptor Mechan and Behemoth all work.
- **301.7a / 702.122a.** Put Vehicles are not crewed; Eggman's 3 power meets Crew 3 alone.
- **500.9 and trigger multipliers.** Roaming Throne, Spark Double, Strionic Resonator and Y'shtola's extra end step allow at most 9 Eggman resolutions per turn (finite).

## Swaps (5 — the floor; no post-floor swap)
| Add | Cut | Why |
|---|---|---|
| Possession Engine | Blasphemous Act | A Vehicle payload whose enters trigger steals an opponent's creature for as long as we control it. Act is a sweeper that also kills Eggman and our artifact creatures. **FLAG: the owner named Act as retained interaction.** |
| Skysovereign, Consul Flagship | Cybermen Squadron | A Vehicle payload that deals 3 to a creature or planeswalker on entering and on attacking. The Squadron is a Cyberman, not a payload, and its myriad needs attacking nonlegendary artifact creatures. |
| Interceptor Mechan | Cryptothrall | A Robot payload that returns an artifact or creature card to hand, stocking the next Eggman trigger. Cryptothrall's hexproof grant overlaps Padeem. |
| Su-Chi Cave Guard | Unwinding Clock | An 8/8 vigilance Construct with ward {4} that adds eight {C} when it dies. The Clock is not a payload. |
| Behemoth of Vault 0 | Foundry Inspector | A 6/6 trample Robot payload; on death, energy pays to destroy a nonland permanent. Inspector's discount is cast-only. **FLAG: the owner named Inspector as retained infrastructure.** |

**Net:**
- Lands 31 → 31. Payloads 28 → 31; P(no payload among 7) 0.0893 → 0.0651.
- Creatures 33 → 33; instants/sorceries 13 → 12.
- Curve by MV 0/1/2/3/4/5/6/7+: 1/1/15/12/14/7/8/10 → 1/1/15/11/13/9/9/9. Average nonland MV 4.206 → 4.221.

**Losses:**
- Blasphemous Act (Toxic Deluge, Their Name Is Death and Cyclonic Rift remain).
- Foundry Inspector's cast discount.
- Cybermen Squadron, Cryptothrall and Unwinding Clock.

## Pass C requested tests (bounded; `tests/test_m6_dr_eggman_m7_mechanics.py::PassCBoundedMeasuredTests`)
**Goblin Welder vs Liliana's Caress (Pass C item 1): 192-cell grid.**
- Caress is live in 72 cells and drains 12 per trigger at hand 3 with The Valeyard (6 without).
- Welder is live in 64 cells, needs an artifact card already in our graveyard, and never adds a card to hand.
- Pass C KEEP stands.

**31 vs 32/33 lands (Pass C item 2):** exact DP.
- P(Eggman castable by card 11/12) is 0.3751/0.4696 at 31 lands, 0.404/0.5009 at 32 and 0.4333/0.532 at 33.
- The 32-land six-swap is staged and rejected (owner's 31-land choice).

**Cast vs put / multipliers (Pass C item 3):** a 64-cell villainous grid.
- In 40 of 64 cells at least one opponent has a free answer.
- The multipliers allow at most 9 triggers.

**Not done.** There were no fixed legal hands or mulligans, no rational-opponent model, no artifact-removal or graveyard-hate model and no multiplayer simulation. No win rates are reported.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline: **0 included combos**. Candidate: **0 included combos**.
- Almost-included lines: 36 → 30. They need cards that are not in the list. **No infinite is claimed.**

## Adversarial scenarios (please push here)
1. **Eggman removed.** Payloads must be hardcast; Lightning Greaves and the counter suite are the protection.
2. **Empty-hand opponents.** They answer every choice for free. Is 31 payloads enough to make the put branch real?
3. **Removal density.** The owner rejected Tri-Sentinel on 2026-10-14 for "substantial removal density". Possession Engine, Skysovereign and Behemoth carry removal, but Blasphemous Act is cut. Does the owner see this as the same class?
4. **Owner retention conflicts.** Act and Inspector were named as retained. The staged keep-Act four-swap and keep-Inspector five-swap are the answers if so.
5. **Possession Engine answered.** Artifact removal returns the creature.
6. **Owner-removed class.** The owner's 2026-10-14 closeout removed or rejected Megrim, Steel Overseer, Etherium Sculptor, Mirrorworks, Torrential Gearhulk, Imposter Mech, Scrawling Crawler, Damocles Base, Chief of the Foundry, Raiders' Wake and Tri-Sentinel. Those evaluated here were rejected; none is re-added. Midnight Crusader Shuttle was demoted for the Damocles critique.
7. **Pass C disposition.** Pass C was owner-equivalent; a genuinely independent model was **NO** (not technically independent). Its final disposition was **NEEDS TESTING, KEEP**. Its Welder hypothesis and the 32-land question are staged as complete 100s and rejected.

## Tested pool (9 configurations; `data/grixis/m6/ij/tested_pools/Dr__Eggman_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100) and CANONICAL_EXPORT (registry export, same logical hash).
- PREFERRED_FIVE (selected).
- FOUR_KEEP_BLASPHEMOUS_ACT_NO_POSSESSION_ENGINE: RETAIN_ALTERNATIVE.
- FIVE_KEEP_FOUNDRY_INSPECTOR_CUT_WEAPONS_MANUFACTURING: RETAIN_ALTERNATIVE.
- FIVE_MIDNIGHT_CRUSADER_SHUTTLE_INSTEAD_OF_SU_CHI: REJECT.
- SIX_PASS_C_GOBLIN_WELDER_OVER_LILIANAS_CARESS: REJECT.
- SIX_TERGRID_OVER_LILIANAS_CARESS: REJECT (Tergrid would be Game Changer #4).
- SIX_PASS_C_32_LANDS_SILVERBLUFF_BRIDGE_OVER_THOUGHTCAST: REJECT.

Other named rejections: Drossforge Bridge, Relentless X-ATM092, Bygone Colossus, Thought Vessel, This Is How It Ends, Ensnared by the Mara, Starscream, Power Hungry, Krang, the All-Powerful, Craterclaw Colossus, and the owner-removed Imposter Mech, Torrential Gearhulk, Scrawling Crawler, Raiders' Wake, Chief of the Foundry and Steel Overseer.

## Distinctness (disclosed)
Nonbasic names shared with the most similar Grixis decks (`exports/grixis-archidekt/`), baseline → candidate:
- Davros, Dalek Creator 45 → 43.
- Mishra, Eminent One 41 → 41; Mishra, Artificer Prodigy 40 → 39.
- Ashnod the Uncaring 38 → 37; Mai and Zuko 37 → 35; The Valeyard 35 → 34.

Overlap with the artifact decks falls by 0–2 names; it is disclosed, not repaired.

**Commander-first difference.** Eggman rewards a hand full of Constructs, Robots and Vehicles that are worth putting at end step, and punishes actual discards. Every add is a payload with enters or dies value; no generic Grixis staple was added.

## Infra disclosure
**No shared-infrastructure change in this PR.**
- These files are byte-identical to PR #662 head bc4b9d53 (vendored from the #651–#662 stack; not modified here):
  - the gate;
  - the schema;
  - the gate test;
  - the Pass C corpus test;
  - `scripts/grixis_m6_bundle_check.py` (SHA-256 `2962a640…`).

**Process notes.**
- The focused CI workflow step names contain no `#` characters.
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → #658 → #659 → #660 → #661 → #662 → this PR.
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
