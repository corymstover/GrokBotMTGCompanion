# Garza Zol, Plague Queen — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** RESEARCH ONLY — NOT APPROVED, NOT CANONICAL, NOT OWNER-PRESENTABLE. Readiness `RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE`.
- Blocker: only four genuine swaps were found, and the five-swap floor was not met without padding.
- Only Cory can approve.

**Reviewer instruction:** attack this list. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a candidate that clearly beats an incumbent, including a genuine fifth swap we missed;
- an owner-direction contradiction we missed.

No win rates were measured, and EDHREC prevalence is discovery evidence only.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Garza_Zol_Plague_Queen_Approved_2026-10-14.txt`, git blob `e3e43c53d9c52224566fe392de92f05e75face4d`, introduced by canonical commit `3e2c89d998d17f709d54f40a4d52acfd6840ee11` (2026-10-14).
- Canonical commit record: 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob e3e43c53, introduced by 3e2c89d998d17f709d54f40a4d52acfd6840ee11 2026-10-14; registry source_commit 1836b97 same bytes).
- Raw SHA-256 `32c0e8049a9c8a5d238048b4f774f0457908d724f23d4597b7da93a6cba0c16f`. This equals the tracker (Deck #20, index 19) and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Garza_Zol__Plague_Queen_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:f5190339a7e9ccc3e5331a401e13f79d1d8dbabed8c81bcb917f6f24d04c3b74`.
- The registry export `exports/grixis-archidekt/garza-zol-plague-queen.txt` (raw `b0dfe1fc5ad19d3d8b3eeb350b1abc42f0de3e32526032a558b5717df32e5fda`) is the same 100 in export format, with the same logical hash.

**Discrepancies.** None. The canonical file is 100 lines, every card 1x, 38 lands.

**Count convention.** 100 = 1 commander + 99 library; no companion.

**Research candidate.** `data/grixis/m7/candidate_lists/Garza_Zol__Plague_Queen.txt`: commander first, then alphabetical; four substitutions.
- Raw SHA-256 `48b6a7dbdb2dac5d591d93cb6f7f7efea634c0663acab9b6a1812661e559317f`.
- Logical hash `lh1:cd76780100cbe9d1ada853684a2093d097a3cf3c8fdae459728fe618821ce4f5`.

**Live data.**
- Live Scryfall `/cards/collection` was queried on 2026-10-23 for the baseline, the candidate and the evaluated names. This was for discovery and legality only; the frozen cache was not written.
- EDHREC Garza pages were retrieved at 11:27 CDT: general (128 decks), upgraded (9), optimized (6), and cEDH (no card data).
- Commander Spellbook find-my-combos was queried for both lists.

**Legality.** Garza Zol, Plague Queen (Coldsnap `csp`, released 2006-07-21) is Commander-legal on live Scryfall and is not a Game Changer. Every card in all ten configurations is legal and within UBR. **No project exception is used.**

**Game Changers.** 9 in the baseline and the candidate: Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Grim Monolith, Jeska's Will, Mana Vault, Rhystic Study, Vampiric Tutor. **Power Bracket 4 (Optimized).**

**Archidekt tags.** Voltron, Commander Damage, Deathtouch-Control.

## Commander model (attack this first)
**Garza Zol, Plague Queen** is a {4}{U}{B}{R} 5/5 Legendary Creature — Vampire Noble. Its Oracle text: "Flying, haste / Whenever a creature dealt damage by Garza Zol this turn dies, put a +1/+1 counter on Garza Zol. / Whenever Garza Zol deals combat damage to a player, you may draw a card."
- **Per-hit payoffs.** Garza's draw, Curiosity, Kediss, Emberclaw Familiar, Quietus Spike, Robe of the Archmagi, Sword of Feast and Famine and Sword of Fire and Ice all trigger per damage event. Double strike gives two events per combat (510.4, 702.4b).
- **Garza-sourced damage.** Fall of the Hammer, Soul's Fire, Chandra's Ignition and Nova Flame (and now Giantfall) make Garza the damage source. With deathtouch from Basilisk Collar or Quietus Spike, each damaged creature dies and gives her a counter.
- **Wins.**
  - 21 commander damage (903.10a).
  - Grafted Exoskeleton poison: Kediss copies it to each other opponent (Spellbook 2822-3681).
  - Extra combats: Aggravated Assault with The Reaver Cleaver (3750-5039) or Sword of Feast and Famine (900-3750).

## Swaps (4 — below the five-swap floor; RESEARCH_ONLY)
| Add | Cut | One-line reason |
|---|---|---|
| Lizard Blades | Fellwar Stone | Permanent double strike: twice the draws and per-hit triggers, and a first-strike kill of most blockers. This is Pass C's requested test, run finitely. Cost: turn-6 Garza 0.4724 → 0.4451; the keep-Fellwar alternative is staged. |
| Giantfall | Rapid Hybridization | Garza-sourced removal that grows her (the owner's stated direction), is lethal with deathtouch and has an artifact mode. It needs a creature. |
| Sink into Stupor // Soporific Springs | Exotic Orchard | A land that is also a bounce, and it works against uncounterable spells. Orchard has EDHREC synergy −0.15. |
| Fell the Profane // Fell Mire | Takenuma, Abandoned Mire | A land that is also creature or planeswalker removal. **FLAGGED: generic removal**, accepted only because it uses a land slot. |

**Why not five.** Every fifth candidate failed:
- Nibelheim Aflame over Nova Flame: cuts the owner's explicit addition on evidence that does not clearly beat the owner's reason.
- Nibelheim Aflame over Toxic Deluge: no better than an owner-kept answer.
- Fire Whip over Pongify: re-adds the owner-removed pinger class.
- Hammer of Nazahn over Talisman of Indulgence: castability drops for an unclear gain.

All four are staged as complete 100s and none is counted.

**Net:**
- Lands 38 → 36 + 2 MDFCs; U/B/R land sources 25/27/24 → 25/26/23.
- Creatures besides Garza 1 → 2 (Lizard Blades when unattached); Equipment 20 → 21; average nonland MV 2.213 → 2.270.
- Game Changers 9 → 9; Spellbook complete combos 3 → 3; almost-included 86 → 86.

**Owner direction.**
- All four cuts are plain RETAIN lines in the owner's 2026-10-14 decisions. **No owner keep or owner addition is cut.**
- Owner-removed cards and classes are not re-added.

**Losses:**
- One 2-mana rock.
- One-mana removal that works without a creature.
- Exotic Orchard's rainbow mana.
- Takenuma's channel recursion.
- 3 life per MDFC played untapped.

## Pass C requested tests (bounded; `tests/test_m6_garza_zol_plague_queen_m7_mechanics.py`)
Pass C's primary challenger was +Fireshrieker / −Inquisitor's Flail; the alternate cuts were Robe of the Archmagi and Quietus Spike. It also asked for:
- removal between strike steps;
- ordinary and deathtouch blockers;
- infect, Kediss and Curiosity;
- 7-mana access and commander tax.

Its disposition was **NEEDS TESTING**. Bounded finite versions (deterministic, no RNG; 5 equipment states × 8 blockers × 3 configurations, plus special rows):

**Unblocked commander damage**

| Equipment | Commander damage | Note |
|---|---|---|
| None | 5 | |
| Inquisitor's Flail | 10 | |
| Double strike (Fireshrieker or Lizard Blades) | 10 | 2 Garza draws |
| Inquisitor's Flail + Lizard Blades | 20 | 24 at power 6, lethal |

**Blockers.**
- Double strike kills and survives a 5/5 vanilla, a 3/3 deathtouch and a 4/4 double-strike blocker. Bare or Flail Garza dies to all three.
- Double strike trades with a 5/5 first striker and dies to an 8/8 or a 5/5 indestructible blocker. Flail + Lizard Blades survives the 8/8.

**Removal after first-strike damage:** double strike 5, Flail 10.

**Per-hit payoffs**

| Test | Double strike | Inquisitor's Flail |
|---|---|---|
| Curiosity + Kediss draws (3 opponents) | 6 | 3 |
| Quietus Spike, opponent starting at 40 | ends at 6 | ends at 15 |
| Grafted Exoskeleton at 7 power | 14 poison (lethal) | 14 poison (lethal) |

**Castability, by turn 4/5/6 on the play**

| List | Turn 4 | Turn 5 | Turn 6 |
|---|---|---|---|
| Baseline | 0.1876 | 0.3093 | 0.4724 |
| Candidate, MDFCs as lands | 0.1769 | 0.2882 | 0.4451 |
| Candidate, MDFCs never as lands | 0.1649 | 0.2669 | 0.4073 |

**Not done:** there were no matched-hand games and no win rates, because no validated Garza game model exists. The Pass C exact list is staged as a complete 100. Robe of the Archmagi and Quietus Spike are not cut, because both multiply with double strike.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline and candidate have the same 3: 3750-5039, 900-3750 and 2822-3681.
- No new combo or infinite is claimed for any add.

## Adversarial scenarios (please push here)
1. **Rock for double strike.** Is Lizard Blades worth losing Fellwar Stone in a deck whose commander costs 7 (turn-6 access −2.7 points)? If not, select FOUR_LIZARD_BLADES_CUT_INQUISITORS_FLAIL_KEEP_FELLWAR. Its cost is the 4× one-hit kill.
2. **Removal between strike steps.** That is the one row where Flail beats double strike (10 vs 5). The research four keeps Flail for that reason.
3. **Giantfall without a creature.** Garza is often the only creature. Rapid Hybridization works with none but gives the opponent a 3/3.
4. **Fell the Profane as generic removal.** The owner trimmed Go for the Throat and Soul Shatter. Does an MDFC land slot really avoid that objection?
5. **Missed fifth swap.** Is there a genuine fifth swap that is not an owner keep or addition and not an owner-removed class? Candidates already rejected: Nibelheim Aflame, Fire Whip, Hammer of Nazahn, Cranial Plating, Sword of War and Peace, Sword of Sinew and Steel, Withering Torment, Bedevil, Temur Battle Rage, Mask of Riddles, Psionic Gift, Rabid Gnaw, The Last Agni Kai, Pain for All, Mox Amber, Thran Dynamo, Relic of Sauron and Shore Up. Jeweled Lotus is banned.
6. **Sweepers and edicts.** Attached Lizard Blades is not a creature. Unattached, it can be sacrificed to an edict instead of Garza.
7. **Pass C disposition.** Pass C was owner-equivalent; technical independence is **false**. It is NON-INDEPENDENT.

## Tested pool (10 configurations; `data/grixis/m6/ij/tested_pools/Garza_Zol__Plague_Queen_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100) and CANONICAL_EXPORT (registry export, same logical hash).
- RESEARCH_FOUR: the research local best, not owner-presentable.
- FIVE_NIBELHEIM_OVER_NOVA_FLAME and FIVE_NIBELHEIM_OVER_TOXIC_DELUGE: REJECT (owner addition and owner keep).
- FIVE_FIRE_WHIP_OVER_PONGIFY: REJECT (owner-removed pinger class).
- FIVE_HAMMER_OF_NAZAHN_OVER_TALISMAN_OF_INDULGENCE: REJECT (turn-6 Garza 0.4451 → 0.4179).
- FOUR_FIRESHRIEKER_INSTEAD_OF_LIZARD_BLADES: RETAIN_ALTERNATIVE.
- FOUR_LIZARD_BLADES_CUT_INQUISITORS_FLAIL_KEEP_FELLWAR: RETAIN_ALTERNATIVE.
- PASS_C_BASELINE_PLUS_FIRESHRIEKER_MINUS_INQUISITORS_FLAIL: RETAIN_ALTERNATIVE (the Pass C exact one-swap).

## Distinctness (disclosed)
Nonbasic names shared with the most similar Grixis decks (`exports/grixis-archidekt/`), baseline → candidate:

| Deck | Shared names |
|---|---|
| Nicol Bolas | 61 → 58 |
| Lord of Tresserhorn | 50 → 47 |
| Obeka, Brute Chronologist | 48 → 46 |
| Nicol Bolas, the Ravager | 46 → 44 |
| Edward Kenway | 46 → 44 |

**Commander-first difference.**
- Lizard Blades, Giantfall and Fireshrieker appear in no other Grixis export.
- Sink into Stupor appears only in Saruman and Tetsuo, and Fell the Profane only in Solkanar.

## Infra disclosure
**No new shared-infrastructure change in this PR.**
- The gate, the schema, the gate test, the Pass C corpus test and `scripts/grixis_m6_bundle_check.py` (SHA-256 `2962a640…`) are byte-identical to PR #667 head 1946a316 (from the #651 → #667 chain), not modified here. They differ from base b6b40ac8 only because those PRs are not yet merged.

**Process notes.**
- The focused CI workflow step names contain no `#` characters.
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → #658 → #659 → #660 → #661 → #662 → #663 → #664 → #665 → #666 → #667 → this PR (#668).
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
