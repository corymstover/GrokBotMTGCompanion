# Goro-Goro and Satoru — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** RESEARCH ONLY — NOT APPROVED, NOT CANONICAL, NOT OWNER-PRESENTABLE. Readiness `RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE`.
- Blocker: only one genuine swap was found, and the five-swap floor was not met without padding.
- Only Cory can approve.

**Reviewer instruction:** attack this list. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a candidate that clearly beats an incumbent, including a genuine second-to-fifth swap we missed;
- an owner-direction contradiction we missed.

No win rates were measured. EDHREC prevalence is discovery evidence only.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Goro_Goro_and_Satoru_Approved_2026-10-14.txt`, git blob `9d9e1b7be5f40e881e997b0712fa4af47ea35139`. It was introduced by canonical commit `4aefbf3bfb665c212871ff4f2fbb0ca4db711e77` (2026-10-14).
- Canonical commit record: 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob 9d9e1b7b, introduced by 4aefbf3bfb665c212871ff4f2fbb0ca4db711e77 2026-10-14; registry source_commit 1836b97 same bytes).
- Raw SHA-256 `2fd39e3b39afaeb1bf394a59b392d8a29f28645776fa0b13c5754df67ab85fdf`. This equals the tracker (Deck #21, index 20), the registry `recorded_sha256`, and the owner's 2026-10-14 approval-candidate SHA.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Goro_Goro_and_Satoru_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:dc88090cd00d2d0e9cb2e667e384c84edb70d864dbd19d4787304f0e866efcba`.
- The registry export `exports/grixis-archidekt/goro-goro-and-satoru.txt` (raw `bdc129bcd94c00b293ddaabb4585ac3130fb4eca7ca8646177335900e7aedfec`) is the same 100 in export format, with the same logical hash.

**Discrepancies.** None. The canonical file has 99 lines, with 2x Island and every other card 1x, for 100 physical cards and 33 lands.

**Count convention.** 100 = 1 commander + 99 library; no companion.

**Research candidate.** `data/grixis/m7/candidate_lists/Goro_Goro_and_Satoru.txt`: commander first, then alphabetical, with one substitution.
- Raw SHA-256 `38e02f9766783ad5194d569329f54603a47829a162d1bc3ea041898e1f4f5e5b`.
- Logical hash `lh1:55ad7a1a2bc59c06a4c3c48af1b02560418c2e2a34e5b69cb86dc2a6862049ed`.

**Live data.**
- Live Scryfall `/cards/collection` was queried on 2026-10-23 for the baseline, the candidate and the evaluated names, for discovery and legality only. The frozen cache was not written.
- EDHREC Goro-Goro and Satoru pages were retrieved on 2026-10-23 at 11:59 CDT: general (8913 decks), upgraded (865), optimized (188) and cEDH (13).
- Commander Spellbook find-my-combos was queried for both lists.

**Legality.** Goro-Goro and Satoru (March of the Machine Commander `moc`, released 2023-04-21) is Commander-legal on live Scryfall and is not a Game Changer.
- Every card in all nine pool configurations is legal and inside U/B/R.
- No project exception applies.

**Game Changers.** The baseline and the candidate have the same 6: Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will and Vampiric Tutor. **Bracket 4 (Optimized).**

**Archidekt tags.** Ninjas, Dragons, Extra Combats.

## Commander model (attack this first)
**Goro-Goro and Satoru** is a {U}{B}{R} 3/4 Legendary Creature — Goblin Human. Its Oracle text: "Whenever one or more creatures you control that entered this turn deal combat damage to a player, create a 5/5 red Dragon Spirit creature token with flying. / {1}{R}: Creatures you control gain haste until end of turn."

**Fresh entrants:**
- Ninjutsu and sneak creatures enter tapped and attacking after blocks. Examples: Yuriko, Satoru Umezawa, Silver-Fur Master and Raphael, the Nightwatcher.
- Token engines make attackers each combat: Daring Piracy, Fire Navy Trebuchet, Determined Iteration, Loyal Apprentice and Urabrask's Forge.
- Hasty one-drops attack right away: Phoenix Chick and Gingerbrute.

**Haste:**
- Samut, Hazoret's Champion and Frostcliff Siege (Temur) give haste continuously.
- Dragon Tempest gives flying entrants haste.
- Goro's own {1}{R} gives haste only to creatures present when it resolves (ruling 2023-04-14).

**Wins:**
- A Dragon army.
- Dragon Tempest and Terror of the Peaks damage.
- Extra combats: Breath of Fury loops (all 5 Spellbook combos), Karlach, Great Train Heist and Aggravated Assault.

## Swap (1 — below the five-swap floor; RESEARCH_ONLY)
| Add | Cut | One-line reason |
|---|---|---|
| Bitterblossom | Mist-Syndicate Naga | A fresh flying 1/1 Faerie Rogue every upkeep, which matches the commander's trigger condition. It is free-hasted by Dragon Tempest and unblockable with Tetsuko, and it is a Rogue for Silver-Fur Master and Prosperous Thief. It survives creature sweepers. Naga's copy is made after combat damage, so it never feeds that combat's trigger. Naga is not among the owner's named Ninja keeps. |

**Why not five.** Every other candidate failed:
- **It cut an owner keep on unclear evidence:**
  - Pass C's own named cuts: Bident of Thassa (drew 2–23 cards in the ledger) and Grazilaxx, Illithid Scholar (2–11 cards, plus rescues).
  - Crumbling Necropolis (Dragonskull Summit lowers castability to 0.6654).
- **It was in an owner-rejected class:** more one-drop or evasive bodies, such as Reckless Imp and Gurmag Swiftwing.
- **It had an anti-synergy:**
  - Goblin Rabblemaster forces the Goblin commander to attack.
  - Kari Zev's Ragavan token clashes with Ragavan, Nimble Pilferer under the legend rule.
  - Splinter's anthem breaks Tetsuko's power-1 evasion.
  - Elektra and Oroku Saki use sneak, so Satoru Umezawa's and Silver-Fur Master's ninjutsu bonuses don't apply.
- **It was marginal:**
  - Redoubled Stormsinger made 0 Dragons in every lean row.
  - Rapid Hybridization over Vandalblast is a role trade.

These are staged as complete 100s where relevant, and none is counted.

**Net:**
- Lands 33 → 33; U/B/R sources 25/21/21 → 25/21/21.
- Creatures 31 → 30, though Bitterblossom makes one each turn.
- Average nonland MV 2.53 → 2.52.
- Game Changers 6 → 6. Spellbook complete combos 5 → 5; almost-included 142 → 138.

**Owner direction.**
- The cut is a plain retained card. **No owner keep or owner addition is cut.**
- Owner-removed cards and classes are not re-added.

**Losses:**
- One ninjutsu body.
- 1 life each upkeep (5 by turn 7).
- A lone Faerie loses to a flying blocker.

## Pass C requested tests (bounded; `tests/test_m6_goro_goro_and_satoru_m7_mechanics.py`)
Pass C asked for the following, with disposition **NEEDS TESTING**:
- the exact baseline vs +Bitterblossom −Bident of Thassa and vs +Bitterblossom −Grazilaxx, Illithid Scholar;
- the same assumptions, with a paid turn-3 UBR Goro;
- turns 3–7 resources and draws;
- blockers and flyers;
- commander removal;
- sweepers;
- one extra-combat window.

Bounded finite version: deterministic, fully scripted, no RNG. It covers 2 profiles (lean; engine with Daring Piracy) × 5 opponent cases × 5 cards.

**Dragons made by turn 7**

| Card | Lean open | Lean flyer wall | Lean removal | Lean sweeper | Lean extra | Engine open | Engine flyer wall | Engine removal | Engine sweeper | Engine extra |
|---|---|---|---|---|---|---|---|---|---|---|
| Bitterblossom | 4 | 0 | 2 | 3 | 6 | 8 | 4 | 5 | 6 | 11 |
| Mist-Syndicate Naga | 2 | 2 | 1 | 2 | 3 | 6 | 2 | 4 | 5 | 9 |
| Bident of Thassa | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 3 | 3 | 7 |
| Grazilaxx, Illithid Scholar | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 3 | 3 | 7 |
| Redoubled Stormsinger | 0 | 0 | 0 | 0 | 0 | 7 | 3 | 5 | 4 | 10 |

**Cards drawn, turns 3–7:**
- Bident of Thassa: 4, 4, 4, 2 and 5 in the lean rows; 14, 4, 12, 7 and 23 in the engine rows.
- Grazilaxx: 4, 4, 4, 2 and 5 in the lean rows; 8, 4, 8, 4 and 11 in the engine rows.
- All other cards drew 0.

**Life at turn 7:** 35 with Bitterblossom, 40 for everything else.

**Castability (paid UBR):**
- Turn 3 on the play 0.6668; turn 3 on the draw 0.7456. The two lists are identical.
- With a non-mana placeholder replacing Fellwar Stone: 0.6452 / 0.7254.

**Not done:** there were no matched-hand games and no win rates, because no validated Goro game model exists. The Pass C exact lists are staged as complete 100s.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- The baseline and the candidate have the same 5: 33-3259, 1347-3259, 2237-3259, 3259-3934 and 1674-3259. All are Breath of Fury loops that need a connection each combat.
- No new combo or infinite is claimed.

## Adversarial scenarios (please push here)
1. **Flying blockers.** The lean flyer-wall row is the one Bitterblossom loses (0 vs 2). Is the deck's evasion (Tetsuko, Rogue's Passage, waterbend, removal) enough?
2. **Life.** Is Bitterblossom's drain acceptable alongside fetches, Talismans, Mana Confluence, City of Brass and Ancient Tomb?
3. **Ninjutsu density.** Does losing Naga weaken Satoru Umezawa and Yuriko lines enough to matter?
4. **Pass C's own cuts.** Should Bitterblossom replace Bident of Thassa or Grazilaxx after all? Both are staged; we judge them owner keeps with draw value the ledger shows.
5. **Missed swaps.** Is there a genuine second swap that is not an owner keep or addition and not an owner-removed class? Candidates already rejected: Redoubled Stormsinger, Rapid Hybridization, Dragonskull Summit, Reckless Imp, Captain's Claws, Legion Warboss, Goblin Rabblemaster, Kari Zev, Skyship Raider, Elektra, Daughter of the Hand, Oroku Saki, Shredder Rising, Splinter, Hamato Yoshi, Reconnaissance Mission, Baleful Strix, Gurmag Swiftwing, Ninja Teen, Sneak Attack and Swiftfoot Boots.
6. **Pass C disposition.** Pass C was owner-equivalent, and technical independence is **false**. It is NON-INDEPENDENT.

## Tested pool (9 configurations; `data/grixis/m6/ij/tested_pools/Goro_Goro_and_Satoru_M7_tested_configurations_20261023.json`)
- **BASELINE** (raw 100) and **CANONICAL_EXPORT** (registry export, same logical hash).
- **RESEARCH_ONE:** the research local best; not owner-presentable.
- **PASS_C_ALT_A_BITTERBLOSSOM_MINUS_BIDENT** and **PASS_C_ALT_B_BITTERBLOSSOM_MINUS_GRAZILAXX:** REJECT (owner-valued draw engines).
- **PASS_C_ALT_C_BITTERBLOSSOM_MINUS_FROSTCLIFF:** REJECT (continuous haste).
- **TWO_STORMSINGER_OVER_FROSTCLIFF:** REJECT (marginal).
- **TWO_RAPID_HYBRIDIZATION_OVER_VANDALBLAST:** RETAIN_ALTERNATIVE.
- **TWO_DRAGONSKULL_OVER_NECROPOLIS:** REJECT (owner mana keep).

## Distinctness (disclosed)
Nonbasic names shared with the most similar Grixis decks (`exports/grixis-archidekt/`), baseline → candidate:

| Deck | Shared names |
|---|---|
| Admiral Beckett Brass | 45 → 45 |
| Garza Zol, Plague Queen | 43 → 43 |
| Admiral Brass, Unsinkable | 42 → 42 |
| Don Andres, the Renegade | 41 → 41 |
| Doctor Doom, King of Latveria | 41 → 41 |

**Commander-first difference.**
- No other Grixis export is Ninja-led.
- Bitterblossom appears only in the two Lord of Tresserhorn lists, and Mist-Syndicate Naga in no other export.

## Infra disclosure
**No new shared-infrastructure change in this PR.**
- The gate, the schema, the gate test, the Pass C corpus test and `scripts/grixis_m6_bundle_check.py` (SHA-256 `2962a640…`) are byte-identical to PR #668 head 909543a5 (from the #651 → #668 chain) and are not modified here.
- They differ from base b6b40ac8 only because those PRs are not yet merged.

**Process notes.**
- The focused CI workflow step names contain no `#` characters.
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → #658 → #659 → #660 → #661 → #662 → #663 → #664 → #665 → #666 → #667 → #668 → this PR (#669).
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
