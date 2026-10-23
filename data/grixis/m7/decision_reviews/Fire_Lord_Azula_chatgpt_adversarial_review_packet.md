# Fire Lord Azula — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

**Reviewer instruction:** attack this list. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a candidate that clearly beats an incumbent;
- an owner-direction contradiction we missed.

No win rates were measured, and EDHREC and stats.cedh.events prevalence are discovery evidence only.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Fire_Lord_Azula_Approved_2026-10-14.txt`, git blob `0aa3e809`, introduced by canonical commit `901face` (2026-10-14).
- Canonical commit record: 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob 0aa3e809, introduced by 901face 2026-10-14; registry source_commit 1836b97 same bytes).
- Raw SHA-256 `b6ef396641f2b5cfac0eb81fb494f21f3745e2a3fd47fa75d2eaadbdc34ddee5`. This equals `state/current_deck_overrides.json` `approved_list_sha256`, the tracker (Deck #19, index 18) and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Fire_Lord_Azula_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:5647c4e9260c54e4b8c54d35135829c656dadda546da03be62ce26113f1cd225` (registry baseline_hash and current_canonical_hash).
- The registry export `exports/grixis-archidekt/fire-lord-azula.txt` (raw `e52f1cbbf1b17f3e3cef0ef9d466e93bdf5e85bc4d32ac5f2856b4bd2b36fda4`) is the same 100 in export format, with the same logical hash.

**Discrepancies.** None in the hashes. The canonical file is 100 lines, 100 distinct names (Tainted Pact singleton names), 26 lands, no basics. The candidate is written commander-first, then alphabetical.

**Count convention.** 100 = 1 commander + 99 library; no companion.

**Candidate.** `data/grixis/m7/candidate_lists/Fire_Lord_Azula.txt`: commander first, then alphabetical; five substitutions.
- Raw SHA-256 `f4136ea0028ee787dddad379e12a7e34ccdaa6578a52d1c63ae953734e5806f2`.
- Logical hash `lh1:c322775496765320d1e9ccef49784108965afe28500d98e56ba70e6eb0b1ee7a`.

**Live data.**
- Live Scryfall `/cards/collection` was queried on 2026-10-23 for the 100 baseline rows and the evaluated names. This was for discovery and legality only; the frozen cache was not written.
- EDHREC Azula pages (general, optimized, cEDH, upgraded) were retrieved at 10:51 CDT, and the stats.cedh.events Azula summary at 10:58 CDT.
- Commander Spellbook find-my-combos was queried for both lists.

**Legality.** Fire Lord Azula (Avatar: The Last Airbender `tla`, released 2025-11-21) is Commander-legal on live Scryfall and is not a Game Changer. Every card in all ten configurations is legal and within UBR. **No project exception is used.**

**Game Changers.** 20 in the baseline and the candidate: Ad Nauseam, Ancient Tomb, Chrome Mox, Demonic Tutor, Fierce Guardianship, Force of Will, Gamble, Grim Monolith, Imperial Seal, Jeska's Will, Lion's Eye Diamond, Mana Vault, Mox Diamond, Mystical Tutor, Necropotence, Orcish Bowmasters, Rhystic Study, Thassa's Oracle, Underworld Breach, Vampiric Tutor. **Power Bracket 5 (cEDH).**

**Archidekt tags.** Combat-Flash, Spell Copy, Combo.

## Commander model (attack this first)
**Fire Lord Azula** is a {1}{U}{B}{R} 4/4 Legendary Creature — Human Noble. Its Oracle text: "Firebending 2 … Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell. You may choose new targets for the copy. (A copy of a permanent spell becomes a token.)"
- **What a copy carries.** The copies are not cast, so they add no storm count and no cast triggers. Additional costs paid for the original count for the copy (Azula ruling 2025-10-02), so Big Score, Unexpected Windfall, Demand Answers and a bargained Beseech each double without a second payment.
- **Combat timing.** Spells have to be cast during combat, from Azula's attack trigger to end of combat. Borne Upon a Wind, High Fae Trickster, Valley Floodcaller, Emergence Zone and Quicken grant flash or sorcery timing. Arena of Glory, Crimson Wisps and Expedite give her haste.
- **Loops** (they need Azula attacking):
  - Narset's Reversal + Frantic Search (11-2196-7089).
  - Narset's Reversal + Turnabout (11-4276-7089, new). Each iteration has two Turnabout resolutions, and we tap the lands for mana in between, so the net is 2L − 6 per iteration. That gives unbounded storm at L ≥ 3 and unbounded mana at L ≥ 4. It wins through a tutor to Brain Freeze, or with Frantic Search drawing the deck for Thassa's Oracle.
- **Wins that need no commander:** Thassa's Oracle + Demonic Consultation or Tainted Pact; Underworld Breach + LED, Lotus Petal, Wheel of Fortune or Grinding Station.
- **Split second (702.61a/b; Samut ruling 2026-08-21).** While a spell with split second is on the stack, players can't cast spells, including our own bargained Beseech free cast and Narset's Reversal into Frantic Search or Turnabout. Triggers still work.

## Swaps (5 — the floor; ten post-floor challenges, no sixth swap)
| Add | Cut | One-line reason |
|---|---|---|
| Turnabout | Samut, Tyrant of Naktamun | Completes the Azula + Reversal + Turnabout loop. Samut's split second disables our Beseech free cast and both Reversal loops. **FLAGGED: cuts an owner addition**; the keep-Samut alternative is staged. |
| Sink into Stupor // Soporific Springs | Exotic Orchard | A land slot that is also a copied instant bounce (opponent's spell or nonland permanent). |
| Unexpected Windfall | Vivi Ornitier | 42.5% stats.cedh Azula staple. Copied, it gives 4 cards and 4 Treasures for one discard; Vivi's win is redundant. |
| Flashback | Swan Song | Copied, it gives two spells flashback for {R}, and the recasts are copied again. Marginal and data-contrary (Swan Song 56.9%); the keep-Swan alternative is staged. |
| Mistrise Village | Gemstone Caverns | Makes the next spell uncounterable, creature spells included. Most marginal and data-contrary (Gemstone 439/566 cEDH); the alternative cuts Wooded Foothills instead. |

**Net:**
- Lands 26 → 25 + 1 MDFC; R/U/B land sources 21/21/20 → 19/20/18 (U 21 with the MDFC); fetches 9 → 9.
- Creatures 13 → 11; instants/sorceries 41 → 44; average nonland MV 1.849 → 1.905.
- Game Changers 20 → 20; Spellbook complete combos 9 → 10 (none lost); almost-included 98 → 105.

**Owner direction.**
- Four cuts are plain RETAIN lines in the owner's 2026-10-14 decisions.
- **Samut, Tyrant of Naktamun is an owner addition**, kept on the reason "Azula's triggered copy ability still functions through split second". That reason is true, but it does not cover our own free-cast and Reversal lines. The override is **flagged** and the keep-Samut four-swap is a complete staged 100.
- Owner-removed cards and classes are not re-added.

**Losses:**
- Samut's split-second protection for our instants and sorceries.
- Swan Song.
- Vivi's ping win and mana.
- Gemstone Caverns' turn-0 rainbow mana on the draw.
- Exotic Orchard's rainbow mana.

## Pass C requested tests (bounded; `tests/test_m6_fire_lord_azula_m7_mechanics.py::PassCBoundedMeasuredTests`)
Pass C #19's priorities were:
1. The Samut/Beseech nonbo, testing +Spellseeker / −Samut.
2. +Storm-Kiln Artist / −Big Score.
3. (Optional) +Storm-Kiln Artist / −Wan Shi Tong.

Its disposition was **NEEDS TESTING**. Bounded finite versions (exact enumeration, no RNG):
- **Samut co-occurrence, by turn 4 on the play (10 cards seen):** Samut 0.101; Samut and Beseech 0.0093; Samut with Reversal and Frantic Search 0.0008.
- **Split-second rules trace:** blocked are the Beseech free cast and Reversal in response; allowed are triggers and mana abilities.
- **Spellseeker reach:** 30 instants/sorceries with MV ≤ 2 in every list.
- **Storm-Kiln vs Big Score Treasure ledger** for k = 0..6 spells cast while Azula attacks:
  - A pre-combat Artist nets 2k − 4 mana and no cards.
  - A copied Big Score nets 0 mana and +2 cards (4 drawn, 1 discarded), whatever k is. So the Artist repays itself at k = 2, out-produces Big Score from k = 3 and matches its 4 gross Treasures at k = 4.
- **Azula castable by turn 4 on the play:**
  - Baseline 0.4920.
  - Candidate 0.4905 with the MDFC played as a land, or 0.4632 if it is never played as a land.
  - Each Pass C exact list 0.4920.

**Not done.** Pass C asked for matched opening hands and games and a speed test. There is no validated Azula cEDH game or opponent model, so there was no matched-shuffle or multiplayer simulation, and no success rates, kill turns or win rates are reported. The exact Pass C lists (+Spellseeker/−Samut, +Storm-Kiln/−Big Score, +Storm-Kiln/−Wan Shi Tong) are staged as complete 100s, not selected, because Storm-Kiln Artist and Spellseeker are owner-removed.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- **Baseline (9):** 742-1295, 1295-3093, 1368-1414-4856, 1368-3518-4856, 1368-1878-2706, 1368-2706-3518, 1368-3698--44, 11-2196-7089, 1368-2196-7089.
- **Candidate:** all nine kept, plus **11-4276-7089** (Azula + Narset's Reversal + Turnabout).
- The loop needs Azula attacking, at least 3–4 lands that untap, and a payoff (Brain Freeze via a tutor, or the Frantic Search loop into Thassa's Oracle). Every iteration is optional and finite.
- No other new combo or infinite is claimed. Storm-Kiln Artist + Azula + Reversal (11-5195-7089) is real but owner-removed, and is staged only in a Pass C list.

## Adversarial scenarios (please push here)
1. **Samut override.** Is the split-second nonbo (Beseech free cast; Reversal into Frantic Search or Turnabout) worse than Samut's protection for our instants and sorceries? The co-occurrence numbers are small (0.0093 for Samut + Beseech by turn 4). If the reviewer weighs the owner's addition higher, select FOUR_KEEP_SAMUT_NO_TURNABOUT.
2. **Counter-heavy tables without Swan Song.** Mistrise Village and Cavern of Souls also protect creature spells. Force of Will, Force of Negation, Fierce Guardianship, Pact, Mindbreak Trap, Flusterstorm, Pyroblast, Red Elemental Blast, Strix Serenade, Mental Misstep and Hexing Squelcher remain. Is Flashback really better than a 1-mana counter?
3. **Mana base.** Gemstone Caverns and Exotic Orchard are cut. B and R land sources each drop by 2, and the MDFC costs 3 life to enter untapped. Is Gemstone's turn-0 mana on the draw worth more than Mistrise Village?
4. **Graveyard hate** (Rest in Peace, Dauthi, Bojuka Bog). This stops Breach and Flashback, but the Turnabout and Frantic loops still work.
5. **Azula removed.** The wins do not need her (Oracle, Breach). Deflecting Swat and Redirect Lightning stay as redirection.
6. **Turnabout outside the loop.** Copied, it can tap two opponents' lands, or untap our own for a second mana pass, at upkeep or end of turn. It is weak without Azula attacking.
7. **Owner-removed classes.** Storm-Kiln Artist, Spellseeker, Dualcaster Mage/Twinflame/Twinning Staff, Lightning Greaves, Seething Song, Snapcaster Mage, Brainstorm, Gitaxian Probe, Leyline of Anticipation, Veyran, Archmage Emeritus, The Last Agni Kai, Training Center and Final Fortune are not re-added.
8. **Pass C disposition.** Pass C was owner-equivalent; a genuinely independent model was **NO** (actual technical third-model independence FALSE). It is NON-INDEPENDENT.

## Tested pool (10 configurations; `data/grixis/m6/ij/tested_pools/Fire_Lord_Azula_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100) and CANONICAL_EXPORT (registry export, same logical hash).
- PREFERRED_FIVE (selected).
- FOUR_KEEP_SAMUT_NO_TURNABOUT: RETAIN_ALTERNATIVE (the owner-keep alternative).
- FOUR_KEEP_SWAN_SONG_NO_FLASHBACK: RETAIN_ALTERNATIVE (below the floor).
- FIVE_KEEP_GEMSTONE_CAVERNS_CUT_WOODED_FOOTHILLS: RETAIN_ALTERNATIVE.
- SIX_MOX_AMBER_OVER_FELLWAR_STONE: RETAIN_ALTERNATIVE (the larger staged package; turn-4 Azula 0.4905 → 0.4638).
- PASS_C_SPELLSEEKER_OVER_SAMUT_BASELINE, PASS_C_STORMKILN_OVER_BIGSCORE_BASELINE and PASS_C_STORMKILN_OVER_WANSHITONG_BASELINE: RETAIN_ALTERNATIVE (Pass C exact one-swaps on the baseline).

**Other named rejections:** Culling the Weak, Dramatic Reversal, Mana Drain, Opposition Agent (a Game Changer), Lightning Bolt, Samut, Hazoret's Champion, Stingcaster Mage, Gush (only 4 Island-typed lands), The One Ring, City of Traitors, Reiterate, Flare of Duplication, Sea Gate Stormcaller; Lightning Greaves and Brainstorm (owner-removed). Manamorphose and Silence are outside UBR.

**Post-floor challenges (all incumbents kept):**
- Fellwar Stone vs Mox Amber (RETAIN_ALTERNATIVE).
- Big Score vs Storm-Kiln Artist (RETAIN_ALTERNATIVE).
- Wan Shi Tong, Librarian vs Storm-Kiln Artist (RETAIN_ALTERNATIVE).
- Talisman of Indulgence vs Culling the Weak.
- Repeal vs Dramatic Reversal.
- Strix Serenade vs Mana Drain.
- Geist of Saint Thalia vs Stingcaster Mage.
- Wooded Foothills vs City of Traitors.
- Flusterstorm vs Reiterate.
- Redirect Lightning vs Lightning Bolt.

## Distinctness (disclosed)
Nonbasic names shared with the most similar Grixis turbo/storm decks (`exports/grixis-archidekt/`), baseline → candidate:

| Deck | Shared names |
|---|---|
| Norman Osborn | 76 → 74 |
| Kefka, Court Mage | 76 → 74 |
| Kess, Dissident Mage | 74 → 73 |
| Rograkh/Silas Renn | 74 → 71 |
| Jeleva, Nephalia's Scourge | 73 → 70 |
| Evelyn, the Covetous | 68 → 66 |

These are cEDH shells, so the fast-mana, free-interaction, Oracle and Breach core is shared.

**Commander-first difference.**
- Turnabout and Flashback appear in no other Grixis export.
- Unexpected Windfall appears only in Doctor Doom, and Sink into Stupor only in Saruman and Tetsuo.
- Each add is chosen for being copied by Azula's attack trigger.

## Infra disclosure
**No new shared-infrastructure change in this PR.**
- The gate, the schema, the gate test, the Pass C corpus test and `scripts/grixis_m6_bundle_check.py` (SHA-256 `2962a640…`) are byte-identical to PR #666 head 8150b968 (from the #651 → #666 chain), not modified here. They differ from base b6b40ac8 only because those PRs are not yet merged.

**Process notes.**
- The focused CI workflow step names contain no `#` characters.
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → #658 → #659 → #660 → #661 → #662 → #663 → #664 → #665 → #666 → this PR (#667).
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
