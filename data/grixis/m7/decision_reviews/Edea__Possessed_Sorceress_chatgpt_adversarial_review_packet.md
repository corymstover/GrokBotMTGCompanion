# Edea, Possessed Sorceress — ChatGPT adversarial review packet (M7, 2026-10-23)

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
- File `refinement/decklists/Edea_Possessed_Sorceress_Approved_2026-10-14.txt`, git blob `e3651060`, frozen by canonical commit `c0dd52a4`.
- Canonical commit record: the bytes were fetched and verified at 9b26aa28. The registry's source commit field says `1836b97`, the import commit, which carries the same bytes.
- Raw SHA-256 `fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4`. This equals `state/current_deck_overrides.json` `approved_list_sha256`, the tracker (Deck #16, index 15) and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Edea__Possessed_Sorceress_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:d6ca08555bc66faf2d6a1884feda86b3d5bad055b6279f78920af5a33d6cb5ea`.
- The registry export `exports/grixis-archidekt/edea-possessed-sorceress.txt` (raw `d41924a6b09c4232b438aa863c833a28f67bdd6598c9bba470ae66f23428acd6`) is the same 100 in export format, with the same logical hash.

**Discrepancies.** None in the hashes. The candidate is written commander-first, then alphabetical.

**Count convention.** 100 = 1 commander + 99 library; no companion.
- 35 lands: Island, Mountain and Swamp ×3 each, plus 26 nonbasic (94 rows).
- Rocks: Sol Ring, Arcane Signet, Fellwar Stone and three Talismans in both lists.

**Candidate.** `data/grixis/m7/candidate_lists/Edea__Possessed_Sorceress.txt`: commander first, then alphabetical; five substitutions.
- Raw `e8680cafc7b7500b6106677e1aaafce6d5035893ea9f0cd335cd1fa1ff5227a2`.
- Logical `lh1:60df43495ea457255e5e1f03cfbdd29975d420a6622bb9f38c4d92a704e685b2`.

**Live data.** Live Scryfall `/cards/collection` was queried on 2026-10-23 for the 94 baseline rows and 178 evaluated names.
- The live results are stored only in the candidate snapshot and the research files; the frozen cache was not written.
- Oracle text and oracle_id show zero differences against the frozen `oracle-cards-20261016090200` snapshot for all 260 snapshot names.
- Jabs, Mistress of Mockery reads `not_legal` on live Scryfall and is EXCLUDE_INVALID. Off-colour names were dropped.

**Legality.** Edea, Possessed Sorceress (Final Fantasy Commander `fic`, released 2025-12-05) is Commander-legal on live Scryfall and is not a Game Changer. Every card in all eight configurations is legal and within UBR. **No project exception is used.**

**Game Changers.** 3 in the baseline and the candidate: Ancient Tomb, Demonic Tutor, Fierce Guardianship. **Power Bracket 4.**

**Archidekt tags.** Theft, Extra Combats, Aristocrats.

## Commander model (attack this first)
**Edea, Possessed Sorceress** is a {2}{U}{B}{R} 2/5 Legendary Creature — Human Warlock with ward {2}. Its Oracle text: "At the beginning of combat on your turn, gain control of target creature an opponent controls until end of turn. Untap it. It gains haste until end of turn. Whenever a creature you control but don't own dies, return it to the battlefield under its owner's control and you draw a card."

Rules points:
- **500.8 / 506.1.** Each additional combat phase has its own beginning of combat step, so each one is another Edea theft.
- **603.2d.** Roaming Throne naming Human or Warlock doubles Edea's triggers.
- **603.3b / 400.7 / 609.3.** With Kaya's Ghostform on a stolen creature, we order Ghostform's trigger first. It returns the card under our control; Edea's trigger then finds a new object, does as much as possible, and we still draw. This is not a delayed trigger, unlike the owner-rejected Marchesa route.
- **707.2 / 704.5j.** Hall of Echoes ({5}) becomes a copy of Edea until end of turn, and the legend rule doesn't apply to our permanents that turn: two thefts per combat.
- **701.43a.** Combat Celebrant exerts, so it gives an extra combat on alternate turns unless Aggravated Assault or Full Throttle untaps it.
- **603.2b (Irma).** Irma can't target the creature Edea is stealing in the same combat.

## Swaps (5 — the floor; eight post-floor challenges, no sixth swap)
| Add | Cut | Why |
|---|---|---|
| Aggravated Assault | Evereth, Viceroy of Plunder | A repeatable extra combat ({3}{R}{R}): another Edea theft each time, and it untaps the stolen creature. **FLAG: the owner challenged Evereth on 2026-10-14 and kept it.** A keep-Evereth four-swap is staged. |
| Kaya's Ghostform | Zara, Renegade Recruiter | For {B}, one theft becomes permanent and Edea still draws. Zara borrows a creature card from a hand and returns it to hand. |
| Hall of Echoes | High Market | A colourless land that copies Edea for a second theft. **FLAG: the owner retained High Market as a "land-based sacrifice outlet".** Phyrexian Tower remains. |
| Geyadrone Dihada | Ayara, Widow of the Realm | −3 steals a creature or planeswalker, and −7 permanently steals every corrupted permanent: theft density, the owner's priority. Ayara is an outlet. |
| Combat Celebrant | Seize the Spotlight | OFF-RANKING (absent from all Edea EDHREC pages): a repeatable extra combat that also untaps the stolen creature. Spotlight is a one-shot where each opponent chooses; it is in 54% of EDHREC Edea decks, a notable loss. |

**Net:**
- Lands 35 → 35; coloured sources U19 B19 R18 unchanged.
- Extra-combat sources 2 → 4; Edea copy and trigger effects 6 → 7.
- Repeatable outlets 10 → 7 (P(at least one in 12 cards) 0.7432 → 0.6075).
- Creatures 24 → 22; instants/sorceries 24 → 23. Average nonland MV 3.203 → 3.156.

**Losses:** Evereth (owner keep), High Market (owner keep), Ayara, Zara and Seize the Spotlight.

## Pass C requested tests (bounded; `tests/test_m6_edea_possessed_sorceress_m7_mechanics.py::PassCBoundedMeasuredTests`)
- **Closet vs Irma (32 cells):** Irma 216 vs Closet 120 steal triggers, with Irma ahead in 28 cells. Closet keeps 48 vs 16, but Thassa keeps one in half the cells. KEEP Irma.
- **Closet vs Impostor Syndrome (8 cells):** Impostor ties or beats Closet in 6 cells and beats it in 4. KEEP.
- **Closet vs Industrial Advancement (28 cells, exact):** Advancement finds a creature 0.4936–0.8834 of the time, on top of Edea's draw. KEEP.
- **Combat Celebrant vs Grim Haruspex (32 cells):** Celebrant gives 48 extra steals, Haruspex 144 draws. Both stay (Pass C DEFER honoured; Celebrant replaces Spotlight).
- **Mana, turns 3–7 (exact DP, on the play):** P(Edea castable) 0.0456/0.2304/0.4878/0.588/0.6772, the same in both lists.

**Not done.** Pass C asked for identical shuffles and interaction sequences against legal opponent boards and blockers. There is no opponent model and no matched-shuffle or multiplayer simulation, so no success or win rates are reported.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline: **0 included combos**. Candidate: **0 included combos**.
- Almost-included lines: 126 → 167. Aggravated Assault adds near-combos with The Reaver Cleaver, Sword of Feast and Famine or Ancient Copper Dragon. None of these is in the 100, but a stolen opposing Ancient Copper Dragon could make Assault repeat combats. This is disclosed as opponent-dependent. **No infinite is claimed.**

## Adversarial scenarios (please push here)
1. **Edea removed.** The fallbacks are ward {2}, Lightning Greaves, the counter suite, the copy effects (Hall, Irma, Spark Double, Sakashima, Gogo) and Dihada as a theft source that isn't a creature.
2. **Creature-light tables.** Extra combats and Dihada need opposing creatures; Evereth's drain didn't. Is the keep-Evereth four-swap better there?
3. **Outlet surplus spent.** The owner said "no sacrifice-outlet shortage remains"; this candidate cuts three outlets. Is 7 enough?
4. **Owner retention conflicts.** Evereth and High Market were kept by the owner. The staged keep-Evereth four-swap answers the first.
5. **Owner four-mana-multiplier direction.** The owner wrote "Another four-mana clone had lower marginal value than theft density or extra combats". So Lithoform Engine is a staged five-swap, not selected, and Dihada (theft) is selected.
6. **Owner-removed class.** Conjurer's Closet, Marchesa, Nasty End, Rhystic Study and the extra clones are not re-added.
7. **Pass C disposition.** Pass C was owner-equivalent; a genuinely independent model was **NO** (not technically independent). Its final disposition was **NEEDS TESTING, KEEP**. Its three Closet hypotheses are staged as complete 100s and rejected.

## Tested pool (8 configurations; `data/grixis/m6/ij/tested_pools/Edea__Possessed_Sorceress_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100) and CANONICAL_EXPORT (registry export, same logical hash).
- PREFERRED_FIVE (selected).
- FOUR_KEEP_EVERETH_ASSAULT_OVER_SPOTLIGHT_NO_CELEBRANT: RETAIN_ALTERNATIVE.
- FIVE_LITHOFORM_ENGINE_INSTEAD_OF_DIHADA: RETAIN_ALTERNATIVE.
- SIX_PASS_C_CLOSET_OVER_IRMA / _OVER_IMPOSTOR_SYNDROME / _OVER_INDUSTRIAL_ADVANCEMENT: REJECT as configurations. Conjurer's Closet itself stays a card-level RETAIN_ALTERNATIVE (post-floor challenges) in case the owner revisits it.

**Other named rejections:** Sephiroth, Bribery, Agent of Treachery, Treachery, Helm of the Host, Sakashima the Impostor, Nasty End, Rhystic Study, Cyclonic Rift, Dark Ritual, Jeska's Will, Nightscape Familiar, Relentless Assault, Hellkite Charger, Laughing Jasper Flint, Susur Secundi and Swiftfoot Boots.

**Post-floor challenges (all kept):** Irma, Impostor Syndrome, Industrial Advancement, Kethek, Lightning Greaves, Victimize, Mob Rule and Disciple of Bolas.

## Distinctness (disclosed)
Nonbasic names shared with the most similar Grixis decks (`exports/grixis-archidekt/`), baseline → candidate:
- Marchesa, the Black Rose 50 → 49; Missy 46 → 46; Wick 45 → 45.
- Tresserhorns 44 → 43; Thraximundar 43 → 43; Lord Xander 41 → 43.
- Don Andres, the closest theft deck, 39 → 38.

**Commander-first difference.** Every add multiplies, repeats or keeps Edea's own two triggers (combat theft and death draw).

## Infra disclosure
**No shared-infrastructure change in this PR.**
- The gate, the schema, the gate test, the Pass C corpus test and `scripts/grixis_m6_bundle_check.py` (SHA-256 `2962a640…`) are byte-identical to PR #663 head 3b67994a, not modified here.

**Process notes.**
- The focused CI workflow step names contain no `#` characters.
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → #658 → #659 → #660 → #661 → #662 → #663 → this PR (#664).
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
