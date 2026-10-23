# Anhelo, the Painter — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

Reviewer instruction: attack this list. Show any rules error, illegal card, unpayable line, or a candidate that clearly
beats an incumbent. No win rates were measured, and EDHREC prevalence is discovery evidence only.

## Provenance
- Canonical source (read-only): `corymstover/grixis-commander-encyclopediaGPT`
  `refinement/decklists/Anhelo_the_Painter_Approval_Ready_2026-10-13.txt` (blob 0f5f55ea…), physical raw SHA-256
  `8d5f8a9bd4fcdcd164aab63150c14dc69a814a4d9fd764876de3214d3adf9972`, vendored byte-exact at
  `data/grixis/m7/baseline_sources/Anhelo_the_Painter_approved_source_2026-10-13.txt`.
- **Discrepancy:** the historical approved digest `d19d94b8…9839e` (state/progress) does not match those bytes
  (registry `recorded_matches_raw: false`). Both values are kept, nothing is re-approved, and the baseline is bound
  through the provenance exception. The baseline logical hash equals the registry: `lh1:627cae66…0132`.
- **Closeout count error:** "31 lands" counts rows. The list has 34 physical lands, plus 3 each of Island, Mountain and Swamp.
- Candidate: `data/grixis/m7/candidate_lists/Anhelo__the_Painter.txt`, raw
  `2c696db8013b90459b23495f8c6a94426ca86ba180a163a8a941d5c285950a58`, `lh1:284c4e096696838efbcc8cd69e694c8339cc9eb926f218d21bf805934497ed39`.
- Live Scryfall data (2026-10-23, 115 names) lives only in the candidate snapshot. The frozen cache was not written.
  - All cards are Commander-legal and within UBR.
  - Game Changers (7, unchanged): Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Mystical Tutor,
    Underworld Breach, Vampiric Tutor → **Power Bracket 4**.

## Commander model (attack this first)
- Anhelo: "The first instant or sorcery spell you cast each turn has casualty 2" (every turn, including opponents' turns).
- Casualty (CR 702.153a) is an optional extra cost paid while casting: you sacrifice a creature with power 2 or greater.
- Copies are not cast, so a copy can't use the casualty slot again.
- Tokens created by the instant itself (Startle, Rotten Reunion, Waste Management, Talrand's Invocation) arrive too late
  to pay that spell's casualty, so they can't fuel the copy they come from.
- The bottleneck is having a power-2 body on board before the first spell of each turn.

## Swaps (5 — the floor, not padded)
| Add | Cut | Why |
|---|---|---|
| Skyclave Shade | Fellwar Stone | A 3/1 casualty body. A landfall turn lets you cast it again from the graveyard. |
| Sinister Concierge | Talisman of Indulgence | A 2/1 for 2. When it dies it suspends itself (and can exile/suspend a creature), so it returns later. |
| Dogged Detective | Exotic Orchard | A 2/1 for 2 with surveil 2, and it returns to hand when an opponent draws their second card. |
| Tenacious Underdog | Talisman of Dominance | A 3/2 for 2 that draws when it dies and blitzes back from the graveyard. Chosen off the popularity ranking. |
| Bedevil | Feed the Swarm | An instant, so it gets a casualty copy on an opponent's turn. It hits artifacts and planeswalkers. Enchantment removal is lost. |

Net: 34 lands + 9 rocks → 33 + 6 (43 → 39 static sources). Creatures go 17 → 21 and artifacts 11 → 8.
Average nonland MV goes 2.831 → 2.833. No combo piece is cut: Reiterate+Geyser/Jeska's Will, Narset's Reversal+Staff/Reiterate,
Dualcaster+Twinflame, Wellspring+Frantic Search, and the Ral / Storm-Kiln outlets all stay.

## Weakest points (please push here)
1. **Mana.** P(≥3 lands-or-rocks in the top 9) drops 0.839 → 0.768, and on the play (top 8) 0.762 → 0.680.
   P(2–5 lands in 7) drops 0.758 → 0.741. A same-count full 100 keeps Talisman of Dominance and cuts Primal Amulet instead
   (`…_five_alt_Underdog_over_PrimalAmulet_20261023.txt`). It was rejected at MODERATE confidence because it loses the Wellspring copy engine.
2. **Feed the Swarm** was the only cheap enchantment answer.
3. **Storm-Kiln Artist** is weaker with three fewer artifacts.
4. **Graveyard hate** shuts off Shade and Underdog recursion.

## Tested pool (6 full 100s; `data/grixis/m6/ij/tested_pools/Anhelo__the_Painter_M7_tested_configurations_20261023.json`)
BASELINE; PREFERRED_FIVE (selected); FIVE_ALT_AMULET (RETAIN_ALTERNATIVE); SIX_WIZARDS (Wizards of Thay over Thunderclap
Drake, RETAIN_ALTERNATIVE); SIX_SANCTUARY (REJECT); SEVEN_GRAVECRAWLER_WINDFALL (REJECT, breaks Reiterate+Geyser).
Named single-card rejections: Cult Conscript, Sedgemoor Witch, Rotten Reunion, Waste Management, Talrand's Invocation,
Double Vision, Reverberate, Make an Example, Metallurgic Summonings, Exsanguinate.

## Infra disclosure
- The four gate/schema/checker/test files were copied byte-identical from PR #651 head 447d9d69, which is unmerged and needed for the
  provenance exception.
- One added line in `scripts/grixis_m6_bundle_check.py` accepts Anhelo's preserved Pass C wording
  `**Technically independent:** FALSE.`. It is exact and case-sensitive. Tests show that TRUE or a missing disclosure still fails.
- Most other decks' final dispositions use other wordings, so they will need the same review.
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
