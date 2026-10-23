# Evelyn, the Covetous — ChatGPT adversarial review packet (M7, 2026-10-23)

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
- File `refinement/decklists/Evelyn_the_Covetous_Approved_2026-10-14.txt`, git blob `03574140`, frozen by canonical commit `43c0ceca`.
- Canonical commit record: the bytes were fetched and verified at 9b26aa28. The registry's source commit field says `1836b97`, the import commit, which carries the same bytes.
- Raw SHA-256 `1d602b5d9b2a370d3448816f593198212b2b83da74e92ccc3232798641b2588a`. This equals `state/current_deck_overrides.json` `approved_list_sha256`, the tracker (Deck #18, index 17) and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Evelyn__the_Covetous_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:94c3b2c4114887f0c86ca2fed5df17408e2068537c475839f9fe7b502668d4db` (registry baseline_hash and current_canonical_hash).
- The registry export `exports/grixis-archidekt/evelyn-the-covetous.txt` (raw `e230c85b8254f533b0a8d6e2e5699e9eac000010f594a822892c3d74cd76390f`) is the same 100 in export format, with the same logical hash.

**Discrepancies.** None in the hashes. The canonical file is 100 lines, 100 distinct names, 26 lands. The candidate is written commander-first, then alphabetical.

**Count convention.** 100 = 1 commander + 99 library; no companion.

**Candidate.** `data/grixis/m7/candidate_lists/Evelyn__the_Covetous.txt`: commander first, then alphabetical; five substitutions.
- Raw SHA-256 `c3f6862c6f4498778069f45e7a5e5bc7efe92d70158b5e9b3f438c8c861b89ac`.
- Logical hash `lh1:7f36c397c95fb1f25c1477765b0ea27e3fdb80c476073d66146b02560eec075a`.

**Live data.** Live Scryfall `/cards/collection` was queried on 2026-10-23 for the 100 baseline rows and the evaluated names (discovery and legality only; the frozen cache was not written). EDHREC Evelyn pages (general, optimized, cEDH, upgraded) were retrieved at 10:23 CDT and the stats.cedh.events Evelyn summary at about 10:26 CDT. Commander Spellbook find-my-combos was queried for both lists.

**Legality.** Evelyn, the Covetous (Streets of New Capenna `snc`, released 2022-04-29) is Commander-legal on live Scryfall and is not a Game Changer. Every card in all eight configurations is legal and within UBR. **No project exception is used.**

**Game Changers.** 19 in the baseline and the candidate: Ad Nauseam, Ancient Tomb, Chrome Mox, Demonic Tutor, Force of Will, Gamble, Imperial Seal, Lion's Eye Diamond, Mana Vault, Mox Diamond, Mystical Tutor, Necropotence, Notion Thief, Opposition Agent, Orcish Bowmasters, Rhystic Study, Thassa's Oracle, Underworld Breach, Vampiric Tutor. **Power Bracket 5 (cEDH).**

**Archidekt tags.** cEDH, Worldgorger Combo, Thassa's Oracle.

## Commander model (attack this first)
**Evelyn, the Covetous** is a {2}{U/B}{B}{B/R} 2/5 Legendary Creature — Vampire Rogue with flash. Its Oracle text: "Whenever Evelyn or another Vampire you control enters, exile the top card of each player's library with a collection counter on it. Once each turn, you may play a card from exile with a collection counter on it if it was exiled by an ability you controlled, and you may spend mana as though it were mana of any color to cast it."
- The trigger is **Vampire-only** (no Rogue or Rat clause). In the baseline Evelyn is the only Vampire; Insolent Neonate makes two.
- In a four-player pod each trigger exiles four cards, ours included; we may play one per turn.
- Saw in Half on Evelyn: two Vampire tokens enter, each triggers for itself and the other (603.6a), up to 4 triggers / 16 cards; then the legend rule removes one token (704.5j) and the triggers still resolve.
- Worldgorger Dragon exiling Evelyn: we may decline the command zone (903.9a), so she returns with the loop and triggers again. Each iteration exiles our own top card too, so the repeats are finite.
- The deck wins with Thassa's Oracle + Demonic Consultation / Tainted Pact, Underworld Breach + LED / Lotus Petal + Brain Freeze, or Worldgorger + Animate Dead / Dance of the Dead / Necromancy. Evelyn is the flash value engine and theft outlet, not the combo.

## Swaps (5 — the floor; eight post-floor challenges, no sixth swap)
| Add | Cut | One-line reason |
|---|---|---|
| Marsh Flats | Thundering Falls | Untapped fetch (81% EDHREC cEDH) for the only always-tapped land (9%). |
| Insolent Neonate | Spellskite | Second Vampire for Evelyn's trigger and an instant-speed Worldgorger discard/exit outlet. Flagged against the owner's Vampire-package rejection. |
| Brainstorm | Redirect Lightning | Pass C's thesis card, added without cutting the owner-defended Ripples. |
| Burnt Offering | Wan Shi Tong, Librarian | 46% stats.cedh staple; sacrifices Evelyn (5) or Worldgorger (6) for B/R mana. |
| Verdant Catacombs | Blazemire Verge | Closest call: 9th fetch (76%) for a conditional dual (6%). |

**Net:**
- Lands 26 → 26; U/B/R land sources 19/19/19 → 20/20/19; always-tapped lands 1 → 0; fetches 7 → 9.
- Creatures 14 → 13; Vampires 1 → 2; instants/sorceries 36 → 37; average nonland MV 1.836 → 1.808.
- Game Changers 19 → 19; Spellbook complete combos 7 → 7.

**Owner direction.** No explicit owner keep is cut; all five cuts are plain RETAIN lines in the owner's 2026-10-14 decisions. Vexing Bauble, Ripples of Undeath, Saw in Half, Windfall/Notion Thief, Stifle and Mistrise Village stay.

**Losses:** the redirect pair (Spellskite, Redirect Lightning), Wan Shi Tong's search punishment, Thundering Falls' surveil, Blazemire Verge's non-fetch B/R.

## Pass C requested tests (bounded; `tests/test_m6_evelyn_the_covetous_m7_mechanics.py::PassCBoundedMeasuredTests`)
Pass C #18's provisional hypothesis was +Brainstorm / −Ripples of Undeath; its disposition was **NEEDS TESTING**. The bounded finite version (exact hypergeometric, no RNG):
- Brainstorm U source on turn 1, play/draw: baseline 0.8385/0.8771, candidate 0.8531/0.8899.
- Ripples castable on turn 2: 0.7852/0.8414 (baseline).
- Ripples mills Worldgorger (cast turn 2, given not drawn), play: 0.0333/0.0671/0.1012 over 1/2/3 triggers, at 3 life plus {1} per take.
- A fetch in the first 7 cards (reshuffles Brainstorm's put-backs): 0.4115 → 0.4981.
- Evelyn castable by turn 4 on the play: 0.1491 → 0.1491.

**Not done.** Pass C asked for matched opening hands and games. There is no validated Evelyn cEDH game or opponent model and no matched-shuffle or multiplayer simulation, so no success rates, kill turns or win rates are reported.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- The same 7 complete combos in baseline and candidate: 742-1295, 1295-3093, 1368-1414-4856, 1368-3518-4856, 4812-4846, 2896-4846, 3605-4846. Almost-included 103 → 117.
- Worldgorger loops are mandatory (104.4b / 732.4): they need another creature card in a graveyard or an instant-speed out, otherwise the game is a draw. Their mana is from lands tapped in response; they need a sink.
- **No new combo or infinite is claimed for any add.** Burnt Offering and Neonate support existing lines.

## Adversarial scenarios (please push here)
1. **Graveyard hate** (Rest in Peace, Dauthi, Bojuka Bog, Soul-Guide Lantern). Worldgorger and Breach lines stop; Oracle/Consultation/Pact remain. Neonate's discard role is weaker. Unchanged from baseline.
2. **Stax and Stifle on fetches.** Fetches 7 → 9; a Stifle or Trickbind on a fetch costs a land, and fetch punishers tax us more. Blazemire Verge (cut) was immune. The four-swap keeping Verge is staged. Should Verge stay?
3. **Targeted removal without the redirect pair.** Spellskite and Redirect Lightning are cut, so removal on Thassa's Oracle or a Breach turn is answered only by counters and Hexing Squelcher's ward. Is that loss bigger than the gains?
4. **Vexing Bauble self-counter.** The owner-kept Bauble counters any spell with no mana spent, including our own Force of Will, Pact of Negation, Mindbreak Trap and life-paid Gitaxian Probe. None of the adds is cast for free. Daze was rejected partly for this reason.
5. **Evelyn removed.** The wins do not need her. Burnt Offering can sacrifice her in response for 5 mana.
6. **Pass C exact swap.** Brainstorm over Ripples is staged as a complete 100, not selected, because Ripples is owner-defended and its mill also feeds Breach. Should it be selected?
7. **Neonate and the owner's Vampire rejection.** The owner rejected the optimized-tribal Vampire package. Neonate is one combo-relevant Vampire, not that package. If the reviewer reads it as a re-add of a rejected class, the swap should revert; Spellskite returns.
8. **Owner-removed classes.** Displacer Kitten, Otawara, Morphic Pool, Talisman of Creativity, Wheel of Fortune, The One Ring, Dragon's Rage Channeler, Cyclonic Rift, Deflecting Swat, Into the Flood Maw, Hoarding Broodlord and Beseech the Mirror are not re-added.
9. **Pass C disposition.** Pass C was owner-equivalent; a genuinely independent model was **NO** (actual technical third-model independence FALSE). It is NON-INDEPENDENT.

## Tested pool (8 configurations; `data/grixis/m6/ij/tested_pools/Evelyn__the_Covetous_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100) and CANONICAL_EXPORT (registry export, same logical hash).
- PREFERRED_FIVE (selected).
- PASS_C_BRAINSTORM_OVER_RIPPLES: RETAIN_ALTERNATIVE (Pass C exact one-swap on the baseline).
- FOUR_KEEP_BLAZEMIRE_VERGE: RETAIN_ALTERNATIVE (below the floor).
- FIVE_GRIM_MONOLITH_INSTEAD_OF_BURNT_OFFERING: RETAIN_ALTERNATIVE (Game Changers 19 → 20).
- FIVE_KEEP_WAN_SHI_TONG_CUT_NOTION_THIEF: RETAIN_ALTERNATIVE (cuts the owner-defended Windfall pair).
- SIX_SPELL_PIERCE_OVER_RIPPLES: RETAIN_ALTERNATIVE (the larger staged package).

**Other named rejections:** Intuition, Forbidden Orchard, Fierce Guardianship, Dispel, Daze, Grief, Vampire Hexmage, Changeling Outcast, Brazen Borrower, Lively Dirge, Starting Town, Gifts Ungiven, Snow-Covered Swamp, Bloodtithe Harvester; Displacer Kitten and Otawara (owner-removed).

**Post-floor challenges (all incumbents kept):**
- Ripples of Undeath vs Spell Pierce (RETAIN_ALTERNATIVE).
- Notion Thief vs Wan Shi Tong, Librarian (RETAIN_ALTERNATIVE).
- Mount Doom vs Starting Town.
- Praetor's Grasp vs Intuition.
- Dauthi Voidwalker vs Grief.
- Gitaxian Probe vs Lively Dirge.
- Hexing Squelcher vs Dispel.
- Final Fortune vs Gifts Ungiven.

## Distinctness (disclosed)
Nonbasic names shared with the most similar theft / cast-opponents'-cards decks (`exports/grixis-archidekt/`), baseline → candidate:
- Don Andres, the Renegade (#14) 27 → 29 (Marsh Flats, Verdant Catacombs).
- Cormela, Glamour Thief (#9) 67 → 69 (Marsh Flats, Brainstorm). Cormela is also a cEDH shell, so the fast-mana, free-interaction and Oracle core is shared.
- No Gonti deck is in the Grixis registry.

**Commander-first difference.** Neonate is the only add that triggers Evelyn's Vampire clause; Burnt Offering converts Evelyn or Worldgorger into mana. Neither appears in Don Andres or Cormela.

## Infra disclosure
**No new shared-infrastructure change in this PR.**
- The gate, the schema, the gate test, the Pass C corpus test and `scripts/grixis_m6_bundle_check.py` (SHA-256 `2962a640…`) are byte-identical to PR #665 head 5f5a3a0f (from the #651 → #665 chain), not modified here. They differ from base b6b40ac8 only because those PRs are not yet merged.

**Process notes.**
- The focused CI workflow step names contain no `#` characters.
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → #658 → #659 → #660 → #661 → #662 → #663 → #664 → #665 → this PR (#666).
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
