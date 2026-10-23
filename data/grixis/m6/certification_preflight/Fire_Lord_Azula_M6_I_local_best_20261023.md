# Fire Lord Azula — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.

Scope: the ten complete configurations in
`data/grixis/m6/ij/tested_pools/Fire_Lord_Azula_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 = 1 commander + 99 library. This is not a global or statistical optimum.

Baseline: canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob 0aa3e809, introduced by 901face 2026-10-14; registry source_commit 1836b97 same bytes), `refinement/decklists/Fire_Lord_Azula_Approved_2026-10-14.txt`. Raw SHA-256 b6ef3966… equals the registry recorded digest and `state/current_deck_overrides.json` approved_list_sha256 (no provenance exception). Logical hash lh1:5647c4e9… equals registry baseline_hash and current_canonical_hash.

## Result
The preferred five (raw f4136ea0…, lh1:c3227754…) is the local best of the tested pool:
- Adds: +Turnabout, +Sink into Stupor // Soporific Springs, +Unexpected Windfall, +Flashback, +Mistrise Village.
- Cuts: −Samut, Tyrant of Naktamun, −Exotic Orchard, −Vivi Ornitier, −Swan Song, −Gemstone Caverns.

Five is the presentation floor, not a target. After the first five, ten more incumbents were challenged: Fellwar Stone by Mox Amber, Big Score by Storm-Kiln Artist, Wan Shi Tong by Storm-Kiln Artist, Talisman of Indulgence by Culling the Weak, Repeal by Dramatic Reversal, Strix Serenade by Mana Drain, Geist of Saint Thalia by Stingcaster Mage, Wooded Foothills by City of Traitors, Flusterstorm by Reiterate and Redirect Lightning by Lightning Bolt. All were kept, and no card was added just to reach a count.

## Why (commander-first)
Fire Lord Azula ({1}{U}{B}{R} 4/4 Legendary Creature — Human Noble): "Firebending 2 … Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell. You may choose new targets for the copy. (A copy of a permanent spell becomes a token.)"

- **Turnabout over Samut, Tyrant of Naktamun (FLAGGED: cuts an owner addition).**
  - Turnabout + Azula + Narset's Reversal is a complete Spellbook combo (11-4276-7089): net 2L − 6 mana per iteration from two land untaps.
  - Samut's split second (702.61a/b; Samut ruling 2026-08-21) blocks our own bargained Beseech free cast. It also stops Narset's Reversal being cast into Frantic Search or Turnabout, so both commander loops are off while Samut is out.
  - The owner's reason ("triggers still work") is true but does not cover this nonbo. Pass C Priority 1 raised the same issue.
- **Sink into Stupor // Soporific Springs over Exotic Orchard:** a land slot that is also a copied instant bounce. Orchard's colours depend on the opponents' lands.
- **Unexpected Windfall over Vivi Ornitier:** a 42.5% stats.cedh Azula staple.
  - Copied, it gives 4 cards and 4 Treasures for one discard (Azula ruling: paid additional costs carry to the copy).
  - Vivi's ping win is redundant with Brain Freeze and Thassa's Oracle.
- **Flashback over Swan Song (marginal, data-contrary: Swan Song 56.9% staple):** copied, it gives two spells flashback for {R}, and each recast during the attack is copied again.
- **Mistrise Village over Gemstone Caverns (most marginal, data-contrary: Gemstone 78% EDHREC cEDH):** makes the next spell uncounterable, including creature spells (Azula, Thassa's Oracle) that Samut never protected. It enters untapped from any of 13 Mountain-typed or fetch sources.
- Creatures 13 → 11; instants/sorceries 41 → 44; lands 26 → 25 plus one MDFC. Protection count net 0 (Samut and Swan Song out; Sink and Mistrise in).

## Owner direction
- **Cuts:** four are plain RETAIN lines in the owner's 2026-10-14 decisions (Exotic Orchard, Vivi Ornitier, Swan Song, Gemstone Caverns).
  - **One owner addition is overridden: Samut, Tyrant of Naktamun.** This is flagged, and the keep-Samut four-swap is staged as a complete 100.
- **Owner additions kept on their stated reasons:** Geist, Strix Serenade, Repeal, Quicken, Crimson Wisps, Expedite, Grinding Station, Beseech the Mirror, Mox Opal, Wan Shi Tong, Starting Town, Arena of Glory and Cavern of Souls.
- **Owner-removed cards are not re-added:** Storm-Kiln Artist, Spellseeker, Dualcaster Mage/Twinflame/Twinning Staff, Lightning Greaves, Seething Song, Snapcaster Mage, Brainstorm, Gitaxian Probe, Leyline of Anticipation, Veyran, Archmage Emeritus, The Last Agni Kai and Training Center. Spellseeker and Storm-Kiln appear only in the exact Pass C test lists.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Fire_Lord_Azula_bounded_measured_tests_20261023.json` and recomputed in `tests/test_m6_fire_lord_azula_m7_mechanics.py`. Pass C #19's final disposition was **NEEDS TESTING**. The Pass C receipt is a NON-INDEPENDENT owner-equivalent (actual technical third-model independence FALSE).

1. **Samut/Beseech nonbo (Priority 1; +Spellseeker / −Samut):**
   - Exact co-occurrence by turn 4 on the play (10 cards): Samut 0.101; Samut and Beseech 0.0093; Samut with Reversal and Frantic Search 0.0008.
   - A rules trace of split second (Beseech free cast blocked; Reversal not castable in response; triggers still copy).
   - Spellseeker reach: 30 instants/sorceries with MV ≤ 2 in every list. The exact Spellseeker list is staged.
2. **Storm-Kiln vs Big Score (Priority 2) and Storm-Kiln vs Wan Shi Tong (optional):** a finite Treasure ledger for k = 0..6 spells cast while Azula attacks.
   - A pre-combat Artist nets 2k − 4 mana. (The Artist has no flash, so the ledger's in-combat column is hypothetical only.)
   - A copied Big Score nets 0 mana (4 Treasures for its {3}{R}) and 4 cards for one discard, whatever k is. The Artist repays itself at k = 2, out-produces Big Score's net mana from k = 3, matches its 4 gross Treasures at k = 4, and never draws.
   - Both lists are staged.
3. **Azula castability** (exact enumeration; lands plus Sol Ring, Mana Vault, Grim Monolith, Fellwar Stone (as colourless), Arcane Signet, Lotus Petal and Talismans counted; moxen, rituals, Spirit Guide and Treasures excluded):

   | Seat | Baseline T3 / T4 / T5 | Candidate, MDFC as land | Candidate, MDFC never a land |
   |---|---|---|---|
   | Play | 0.2857 / 0.4920 / 0.5861 | 0.2846 / 0.4905 / 0.5845 | 0.2691 / 0.4632 / 0.5565 |
   | Draw | 0.3654 / 0.5855 / 0.6697 | 0.3642 / 0.5839 / 0.6680 | — |

Not done, stated plainly: Pass C's speed test (Lightning Greaves) and any matched-hand games were not run. There is no validated Azula cEDH game or opponent model, so no matched-shuffle playtest, win rate or kill-turn distribution is reported.

## Self-challenge
- **Four-swap keeping Samut (no Turnabout):** staged, RETAIN_ALTERNATIVE (the owner-keep alternative).
- **Four-swap keeping Swan Song (no Flashback):** staged, RETAIN_ALTERNATIVE.
- **Five-swap keeping Gemstone Caverns, cutting Wooded Foothills:** staged, RETAIN_ALTERNATIVE.
- **Six-swap with Mox Amber over Fellwar Stone:** staged, RETAIN_ALTERNATIVE (turn-4 Azula 0.4905 → 0.4638).
- **Pass C exact lists:** +Spellseeker/−Samut, +Storm-Kiln/−Big Score and +Storm-Kiln/−Wan Shi Tong are staged, RETAIN_ALTERNATIVE (owner-removed adds).
- **Rejected singles:** Culling the Weak, Dramatic Reversal, Mana Drain, Opposition Agent, Lightning Bolt, Samut, Hazoret's Champion, Stingcaster Mage, Gush, The One Ring, City of Traitors, Reiterate, Flare of Duplication, Sea Gate Stormcaller, Lightning Greaves and Brainstorm (the last two are owner-removed).

## Limits
Only finite rules cases and exact enumerations are tested.

Main losses:
- Samut's split-second protection;
- Swan Song's one-mana counter;
- Vivi's ping win and mana;
- Gemstone Caverns' opening-hand acceleration;
- Exotic Orchard's rainbow mana.

Game Changers 20 → 20 (Bracket 5). Average nonland MV 1.849 → 1.905.

Castability model caveats:
- Each fetch is counted as a source of any one Grixis colour, Exotic Orchard is counted as rainbow, and Gemstone Caverns as colourless.
- Fetch and shock life is ignored.
- Turn 2 reads 0 for every list (at most T − 1 rocks are deployed by turn T, and moxen are excluded).
