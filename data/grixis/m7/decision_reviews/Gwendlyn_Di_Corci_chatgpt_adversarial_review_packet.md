# Gwendlyn Di Corci — ChatGPT adversarial review packet (M7, 2026-10-23)

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
- File `refinement/decklists/Gwendlyn_Di_Corci_Approved_2026-10-14.txt`, git blob `4ef2c267314322be9793a1e5490613b98520a24e`. It was introduced by canonical commit `111f903e` (2026-10-14).
- Canonical commit record: 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob 4ef2c267, introduced by 111f903e 2026-10-14; registry source_commit 1836b97 same bytes).
- Raw SHA-256 `9a393cb7edf40f9bfb388d37dd657839cad851dc6a021440c7d1b239c1fd20a9`. This equals the tracker (Deck #22, index 21) and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Gwendlyn_Di_Corci_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:c2a52fd405d5eba4d4216c5852e7bf09604502a13ec215c7bf3c9ca55016911c`.
- The registry export `exports/grixis-archidekt/gwendlyn-di-corci.txt` (raw `4120c13480a4daa65cfd672e720c9e8a7bc83b7964730aaf342bf1da44589ca4`) is the same 100 in export format, with the same logical hash.

**Discrepancies.** None. The canonical file has no terminal newline (hashed as-is). It holds 2x Island, 2x Mountain, 5x Swamp and every other card 1x: 100 physical cards and 35 lands.

**Count convention.** 100 = 1 commander + 99 library; no companion.

**Research candidate.** `data/grixis/m7/candidate_lists/Gwendlyn_Di_Corci.txt`: commander first, then alphabetical, with one substitution.
- Raw SHA-256 `f5f26b78a09f9247be2e311dd76b6e1ff3ed012cd2eaa66692cb33b68fc38197`.
- Logical hash `lh1:0540cd42…` (full value in the tested pool).

**Live data.**
- Live Scryfall `/cards/collection` was queried on 2026-10-23 at 12:34 CDT for the baseline and 115 candidates, for discovery and legality only. The frozen cache was not written.
- EDHREC Gwendlyn Di Corci pages were retrieved on 2026-10-23 at 12:31 CDT: general (380 decks), upgraded (26), optimized (31) and cEDH.
- Commander Spellbook find-my-combos was queried for both lists.

**Legality.** Gwendlyn Di Corci (first printed in Legends; snapshot printing Masters Edition III `me3`, released 2009-09-07) is Commander-legal on live Scryfall and is not a Game Changer.
- Every card in all nine pool configurations is legal and inside U/B/R.
- Jeweled Lotus (banned) was excluded.
- No project exception applies.

**Game Changers.** The baseline and the candidate have the same 17. **Bracket 4 (Optimized).**

**Archidekt tags.** Discard, Wheels, Untap.

## Commander model (attack this first)
**Gwendlyn Di Corci** is a {U}{B}{B}{R} 3/5 Legendary Creature — Human Rogue. Its Oracle text: "{T}: Target player discards a card at random. Activate only during your turn."

**Untaps** (the owner's keeps):
- Magewright's Stone works the turn it lands.
- Pemmin's Aura.
- Patriar's Seal.
- Thousand-Year Elixir removes summoning sickness.
- Illusionist's Bracers copies the activated ability (CR 605.1a: it is not a mana ability).

**Payoffs:**
- On discard: Waste Not, Liliana's Caress, Tinybones, Trinket Thief.
- On the graveyard: Tergrid, God of Fright, Tinybones, Bauble Burglar and Bloodchief Ascension.
- Lock and refill pieces: Bottomless Pit, Oppression, Chains of Mephistopheles and Notion Thief, plus the wheels (Wheel of Fortune, Reforge the Soul, Windfall and others).

## Swap (1 — below the five-swap floor; RESEARCH_ONLY)
| Add | Cut | One-line reason |
|---|---|---|
| Hymn to Tourach | Dauthi Voidwalker | Same {B}{B}, two more random discards in Gwendlyn's idiom. Dauthi's exile replacement (CR 614.1a) switches off three owner keeps: Tergrid, Tinybones, Bauble Burglar and Bloodchief Ascension. Flagged owner-blueprint override (Dauthi is named in the owner's blueprint, not the explicit keep list). |

**Why not five.** Every other candidate failed:
- **It cut an owner keep or addition without clearly better evidence:**
  - Pass C exact: +Aphetto Alchemist −Magewright's Stone. The Stone is an owner keep, and the Alchemist is owner-removed and makes a generic infinite with Bracers (283-4091). OWNER DECISION.
  - Pass C fallback: +Rings of Brighthearth −Mind Twist (Mind Twist is an owner addition).
  - Sulfurous Springs over Crumbling Necropolis measured worse: play T4 0.5094 vs 0.511.
- **It was owner-removed or in a rejected class:**
  - Megrim (owner-removed).
  - Whispering Madness and Drown in the Loch are generic redundancy.
  - Kederekt Parasite and Lavaborn Muse are punishment bodies, a class the owner trimmed.
- **It was marginal or off-plan:**
  - Swiftfoot Boots, Rankle, Master of Pranks, Tinybones, the Pickpocket, Davriel, Rogue Shadowmage, Vizier of Tumbling Sands and Retreat to Coralhelm.
  - Mana Vault would be an 18th Game Changer, and its colourless mana cannot pay Gwendlyn.

These are staged as complete 100s where relevant, and none is counted.

**Net:**
- Lands 35 → 35; U/B/R sources 21/24/17 → 21/24/17.
- Creatures 14 → 13.
- Average nonland MV 2.328 → 2.328.
- Game Changers 17 → 17. Spellbook complete combos 1 → 1; almost-included 52 → 50.

**Owner direction.**
- The flagged override is above. **No explicit owner keep or owner addition is cut.**
- Owner-removed cards and classes are not re-added.

**Losses:**
- Continuous graveyard hate (Bojuka Bog remains).
- A 3-power shadow clock.
- Dauthi's one free void card.
- Hymn is blank against empty hands.

## Pass C requested tests (bounded; `tests/test_m6_gwendlyn_di_corci_m7_mechanics.py`)
Pass C asked for the following, with disposition **NEEDS TESTING**:
- the untouched locked 100 vs +Aphetto Alchemist −Magewright's Stone, with +Rings of Brighthearth −Mind Twist only if it mattered;
- source-paid UBBR by turns 3–5;
- useful discards;
- the Dauthi/Tergrid interaction resolved.

Bounded finite version: deterministic, no RNG. It covers 9 fixed states, exact hypergeometric castability, and a 36-row Hymn vs Dauthi ledger plus 5 adversarial rows.

**Useful random discards, Stone vs Alchemist:**

| State | Stone | Alchemist |
|---|---|---|
| A1 | 4 | 4 |
| A2 | 4 | 9 |
| A3 | 2 | 1 |
| A4 | 2 | 2 |
| A5 | 4 | 3 |
| A6 | 0 | 0 |
| A7 | 0 | 0 |
| A8 | 4 | 21 |
| A9 | 4 | 5 |

The Alchemist's gains need its Bracers loop. Exact no-tutor chance of assembling two specific cards: 0.0093 in 10 cards seen, 0.0188 in 14.

**Castability (source-paid UBBR):** play T3 0.1439; play T4 0.511; draw T4 0.6035; play T5 0.6035. The two lists are identical. The colour-agnostic bound is 0.555 on the play at T4.

**Rings arithmetic.** In a single turn, Rings beats Hymn's two discards only with 6+ spare mana.

**Not done:** there were no matched-hand games and no win rates, because no validated Gwendlyn game model exists.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- The baseline and the candidate have the same 1: 1368-2706-3518 (Underworld Breach + Lion's Eye Diamond + Wheel of Fortune).
- No new combo is claimed. The Aphetto alternative would add 283-4091.

## Adversarial scenarios (please push here)
1. **Graveyard decks.** This is the CANDIDATE_LOSS row. Is Bojuka Bog plus interaction enough without Dauthi?
2. **Hellbent tables.** Hymn is blank (CANDIDATE_LOSS). How often are opponents hellbent on Gwendlyn's turns?
3. **Dauthi's void card.** This one-time free spell is lost (CANDIDATE_LOSS).
4. **Tergrid with an edict, and wheels with Bloodchief Ascension.** These are CANDIDATE_GAIN rows. Is the replacement-effect reading (CR 614.1a) right?
5. **Pass C exact.** Should Aphetto Alchemist replace Magewright's Stone despite the owner's keep and rejection? It is staged as an OWNER DECISION.
6. **Missed swaps.** Is there a genuine second swap that is not an owner keep or addition and not an owner-removed class? Every rejected candidate is listed above.
7. **Pass C disposition.** Pass C was owner-equivalent, and technical independence is **false**. It is NON-INDEPENDENT.

## Tested pool (9 configurations; `data/grixis/m6/ij/tested_pools/Gwendlyn_Di_Corci_M7_tested_configurations_20261023.json`)
- **BASELINE** (raw 100) and **CANONICAL_EXPORT** (registry export, same logical hash).
- **RESEARCH_ONE:** the research local best; not owner-presentable.
- **PASS_C_EXACT_APHETTO_MINUS_STONE_ON_BASELINE** and **CANDIDATE_PLUS_APHETTO_MINUS_STONE:** RETAIN_ALTERNATIVE (OWNER DECISION).
- **PASS_C_FALLBACK_RINGS_MINUS_MIND_TWIST:** REJECT (it cuts an owner addition).
- **ONE_RINGS_OVER_DAUTHI:** RETAIN_ALTERNATIVE.
- **TWO_WHISPERING_MADNESS_OVER_REFORGE:** REJECT.
- **CHALLENGE_SULFUROUS_SPRINGS_OVER_NECROPOLIS:** REJECT (measured worse).

## Distinctness (disclosed)
Nonbasic names shared with the most similar Grixis decks (`exports/grixis-archidekt/`), baseline → candidate:

| Deck | Shared names |
|---|---|
| Crosis, the Purger | 55 → 56 (Crosis also runs Hymn to Tourach) |
| Nekusar, the Mindrazer | 54 → 54 |
| Lord Xander, the Collector | 50 → 50 |
| Nicol Bolas | 46 → 46 |
| The Madcap Jester | 45 → 44 |
| Grixistax October 2026 | 45 → 44 |

**Commander-first difference.**
- Dauthi Voidwalker is in seven other Grixis exports.
- Gwendlyn remains a tap-to-discard untap deck, unlike Nekusar's draw punishment.

## Infra disclosure
**No new shared-infrastructure change in this PR.**
- The gate, the schema, the gate test, the Pass C corpus test and `scripts/grixis_m6_bundle_check.py` (SHA-256 `2962a640…`) are byte-identical to PR #669 head 3d550c79 (from the #651 → #669 chain) and are not modified here.
- They differ from base b6b40ac8 only because those PRs are not yet merged.

**Checker limitation (disclosed, not fixed).** On the explicit-false disclosure path, the bundle checker does not veto an appended "independent third model: yes"-style phrase, because its explicit-true pattern is narrower than its any-true pattern. This is shared infra, so it is left unchanged here.

**Process notes.**
- The focused CI workflow step names contain no `#` characters.
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → #658 → #659 → #660 → #661 → #662 → #663 → #664 → #665 → #666 → #667 → #668 → #669 → this PR (#670).
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
