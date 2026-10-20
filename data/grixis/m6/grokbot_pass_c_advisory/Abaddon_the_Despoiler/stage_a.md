# GrokBot ADVISORY Pass C — Stage A (sealed first pass) — #1 Abaddon_the_Despoiler

**ADVISORY ONLY — NOT a qualified independent Pass C.** `formal_independent_pass_c=false`. No canonical deck, approval, exception or milestone was touched. Proposed swaps are for Cory's decision only.

Labels: **[M]** measured · **[F]** source-backed fact · **[J]** strategic judgment · **[H]** unresolved hypothesis.

## Reviewer provenance
- Reviewer: GrokBot (MTG Bot) advisory Pass C critic, executor subagent. Model/version: not exposed to the reviewer (unknown). Environment: shared Linux box, git + authenticated `gh`, Python 3, curl, live Scryfall API, Wizards CR text.
- Date/time: 2026-10-20 15:24–15:40 CDT (America/Chicago). Engineering branch `grokbot-passc-advisory-01-abaddon` from `origin/chatgpt-cycle76-m6-refinement` @ `efdafd4fe8d174273acec8ccc37984b1da4ea971`. Canonical repo `corymstover/grixis-commander-encyclopediaGPT` main @ `ceffdcceec19e51fa01e3cbe01cca99da0558b07` (read-only).
- Prior involvement (disqualifying): GrokBot wrote the M1 interaction reviews (likely including an Abaddon interaction review), the commander blueprints (cycles 50–55, including the Abaddon blueprint used here), the M2–M5 tooling, and the Cycle124 advisory critiques. The orchestrator read the handoff caveats (Zevlor, Tresserhorn, The Rani, Wick, Goben/Norman alias) and remembers earlier batch outcomes in general terms. It has not seen any comprehensive deep-review verdicts.
- **Exposure during Stage A (disclosed):** a keyword grep of `grixis/Grixis Authority Model.md` for "independen" showed one M5 line: *"Abaddon: Mystic Remora → Stormfist Crusader"* (a registered challenger). This is M5 candidate exposure. Anything below about Stormfist Crusader or Mystic Remora is therefore marked EXPOSED and does not count as an independent finding. The blueprint's EDHREC shortlist (Aurora Phoenix, Deny Reality, Poxwalkers, Blood for the Blood God!) was also seen, because the blueprint is an allowed input.
- Files opened (blob SHAs): engineering@efdafd4f — AGENTS.md e6fa62a4; Single-Deck Review Standard cd6a184e; Comprehensive 62 Pass C Handoff 3f15b71a; Authored 62 Pass C Handoff 10ddbf0c; I-J Contract a206e5dc; Authority Model 728432c1 (grep only); single_deck_depth_tracker.json 259d8c2a (only the queue/id/hash/authority fields were printed); .github/workflows/m6-single-deck-depth-check.yml 6030bfee; scripts/grixis_m6_single_deck_depth_check.py 9d4cc067 (grep only); pytest.ini 0f9b8f59. Canonical@ceffdcce — state/current_deck_overrides.json 81801b2f; refinement/Deck_Refinement_Tracker_2026-10-12.csv 7d3c80a3 (first rows only); refinement/decklists/Abaddon_the_Despoiler_Approved_2026-10-13.txt 1bbead6e; refinement/blueprints/Abaddon_the_Despoiler_v1.md a1a17c61 (GrokBot-authored). Also the directory and file *names* of data/grixis/m6/ and of the canonical repo's Abaddon files were listed, but their contents were not opened. Not opened: deep_reviews/*, critic_batches/*, refinement/decisions, CLOSEOUT_DECISION, rules/Interaction_Review, evidence/*, M5 rankings, PR/commit messages.
- External inputs: Scryfall collection, fetched 2026-10-20T20:25:12Z (= 15:25 CDT); raw sha256 c75afe8d…; slim snapshot in `stage_a_oracle_snapshot.json`. Scryfall returned 0 rulings for Abaddon [M]. Comprehensive Rules `MagicCompRules 20260925.txt`, sha256 8d860e45….

## Source binding
- [M] Canonical list: 100 cards, 94 unique lines. Plain `sha256` of the deck TXT = `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`. This matches the override `approved_list_sha256` and the tracker `baseline_approved_sha256`. Tracker index 0 = Abaddon_the_Despoiler; source_identity_discrepancy NONE.
- [M] Every card is Commander-legal (official). Colour identity ⊆ UBR. No project exceptions apply to this deck. 14 Scryfall Game Changers: Ancient Tomb, Chrome Mox, Demonic Tutor, Fierce Guardianship, Force of Will, Gamble, Imperial Seal, Jeska's Will, LED, Mana Vault, Mystical Tutor, Rhystic Study, Underworld Breach, Vampiric Tutor.

## Commander mechanics (what Abaddon actually rewards)
- [F] Abaddon is {2}{U}{B}{R}, a trample creature. *During your turn, spells you cast from your hand with MV ≤ X have cascade, where X = total life your opponents have lost this turn.*
- [F] X is a sum over **all** opponents. In a 4-player game, Boltwave gives X=9, Flame Rift X=12, Loyal Subordinate X=9, and one Thermo-Alchemist tap X=3. X counts life *lost*, not net change (Rakdos/Neheb rulings on the same wording). Opponents paying life on your turn also adds to X.
- [F] Only **hand** casts get cascade. Free alternative costs still count as hand casts: Fierce Guardianship, Deadly Rollick and Deflecting Swat free on your turn, FoW pitch, and Pact. So free Rollick with X≥4 = exile a creature plus a free cascade. Cascade, suspend, foretell, escape, Prosper and Jeska's Will casts are from exile or graveyard. They do not chain Abaddon cascades, but they do trigger the exile-cast payoffs: Wild-Magic Sorcerer, Keeper of Secrets, Passionate Archaeologist (on Abaddon), Nalfeshnee, The Lost and the Damned, and Prosper. Copies (storm, Nalfeshnee) are not cast.
- [F] Cascade (CR 702.85a) finds a nonland card with **strictly lower** MV. Printed cascade plus Abaddon's cascade trigger separately (702.85c): Bituminous Blast or Noise Marine at X≥5 cascade twice, and Call Forth the Tempest at X≥8 cascades three times.
- [M]/[J] **MV-1 casts are the key lever.** The 99 has 15 MV-1 spells, and each one cast from hand with X≥1 cascades into an **MV-0** card. That pool is exactly 7 cards: Ancestral Vision, Inevitable Betrayal, Profane Tutor (premium hits), Chrome Mox, Lotus Petal, LED (minor), and Pact of Negation (usually a dead hit). A cascaded Delayed Blast Fireball is cast from exile, so it deals 5 to each opponent and each of their creatures (ruling).
- [F] A card with no mana cost cannot use an alternative cost equal to its mana cost (Lotus Bloom/Mox Tantalite ruling). So Breach escape most likely can't recast the deck's no-cost suspend cards [H].

## Power ceiling and game plan
- [J] **Bracket 4 (Optimized), upper end; fringe cEDH at most.** It has fast mana, 6 tutors, 7 counters and a compact Breach line, but a 5-MV commander whose engine depends on life lost this turn. Do not push it toward generic turbo cEDH.
- [J] The plan: fast mana into Abaddon on turns 3–4. Each turn, front-load life loss (Thermo tap, Boltwave, Flame Rift, Loyal Subordinate at combat, Ruinous Powers at upkeep, Vivi/Kessig/Flamer triggers, doubled by Bloodletter or Solphim). Then chain hand casts with cascade and convert the exile casts into damage, tokens and cards. Close with burn, Breach mill, or combat.

## Role counts (my classification of the actual 99) [M]
- Lands: 34. Effective sources U18/B19/R15 counting basic types only; fetches reach the duals (and Xander's Lounge), so all three colours are effectively ≈20+.
- Curve of the 65 nonlands: MV0 ×7, MV1 ×15, MV2 ×13, MV3 ×12, MV4 ×9, MV5 ×4, MV6 ×3, MV8 ×1, MV9 ×1. Average MV 2.58.
- Ramp/acceleration: 19 (9 artifacts, 4 rituals including Jeska's Will, Birgi, Neheb, Storm-Kiln, Vivi, and the reducers Nightscape Familiar and Rakdos), plus Ancient Tomb.
- Draw/selection: about 11 (AV, Brainstorm, Ponder, Rhystic, Remora, Wheel, Windfall, Mind's Desire, Prosper, Ruinous Powers, Jeska's Will), plus recursion from Exalted Flamer and Wild-Magic chains.
- Tutors: 6.
- Stack interaction: 7 counters (FoW, FoN, Fierce Guardianship, Pact, Flusterstorm, Swan Song, Pyroblast) plus Deflecting Swat.
- Creature removal: Bituminous Blast, Deadly Rollick, Noise Marine, Inevitable Betrayal (theft), plus sweepers Call Forth and Delayed Blast (both one-sided) and Blasphemous Act (symmetric).
- **Noncreature permanent removal: 2, both conditional** (Otawara bounce, Pyroblast on blue only).
- Threshold enablers: about 10. Amplifiers: Bloodletter, Solphim. Exile payoffs: 6.

## Strongest synergies [J]
1. The MV-1 to MV-0 cascade pipeline, explained above.
2. Bloodletter + Solphim: Boltwave becomes 6 damage, then 12 life lost per opponent.
3. Free commander-spells (Rollick, Fierce Guardianship, Swat) gaining cascade on your own turn.
4. Delayed Blast Fireball from exile (foretold or cascaded).
5. Passionate Archaeologist on Abaddon + Wild-Magic Sorcerer + Lost and the Damned, all converting cascades into damage and bodies.
6. Neheb after a high-X turn gives a large burst of red mana.

## Combo trace — Underworld Breach + LED + Brain Freeze [F mechanics / J feasibility; not simulated]
- **Entry:** Breach (1R), LED, and Brain Freeze reachable, plus about 6 cards in the graveyard after discarding to LED. Total entry is 2 mana plus LED; the LED mana pays for the first Brain Freeze.
- **Loop:** sacrifice LED for 3 of one colour → escape Brain Freeze (1U, exile 3). Point enough copies at yourself to mill at least 6, and the rest at opponents → escape LED (0, exile 3) → repeat. Each cycle nets +1 mana and +2 storm.
- **Feasibility estimate:** cumulative opponent mill is roughly 3k² after k cycles. About 10 cycles mills three 85-card libraries, and your own library (~80 at turn 3) is enough to sustain that.
- **The win is not immediate.** Opponents lose at their next draw (CR 704.5b) unless pingers are on the board. With Vivi or Kessig out, each noncreature spell in the loop hits every opponent, Exalted Flamer adds hits for instants/sorceries, and Solphim/Bloodletter double all of it. That can make the kill immediate.
- **Interruption points:** a counter on Breach; Stifle-type effects on the storm trigger; instant-speed graveyard hate (Tormod's Crypt, Soul-Guide Lantern); Rest in Peace or Grafdigger's Cage; Drannith Magistrate (blocks all non-hand casts — also shuts off cascade, suspend and foretell); a reshuffle effect after the mill.
- **Protection:** 7 counters plus Swat, and Pact at 0 mana. Abaddon adds nothing to this line.

## Opponent responses [J]
- Removing Abaddon in response to the first setup spell turns off cascade for the rest of the turn. Cascade is checked at cast, and he costs 7 on recast.
- Drannith Magistrate and Rest in Peace are the worst stax pieces. The deck has no clean answer to an artifact or enchantment once it resolves.
- Lifegain does not reduce X. Prevention effects do (damage prevented = no life lost).

## Weakest slots (ranked) [J]
1. **Blasphemous Act.** Symmetric: it kills Abaddon and the pinger/amplifier board. Two one-sided sweepers already exist. At MV9 it is almost never a cascade hit.
2. **Nightscape Familiar.** A 2-mana 1/1 that only reduces U/R costs; it does nothing for Bloodletter or the free spells. Fragile.
3. **Rakdos, Lord of Riots.** Reduces creatures only (16 others), and the BBRR cost is hard. Redundant threat.
4. **Kessig Flamebreather.** 3 life loss per trigger. Its saving grace is that it pings during the combo loop.
5. **Keeper of Secrets.** A 6-MV body that duplicates Archaeologist's effect.
6. **Mind's Desire.** MV6 and storm-dependent, though on-theme with the exile payoffs. Borderline keep.
7. **Flame Rift.** 4 to yourself, in a list with 7 fetches, 3 shocks, City of Brass, Mana Confluence, Ancient Tomb, Talismans, Imperial Seal/Vampiric and FoW. Your own life budget is real. Keep, but watch it.
8. **Mystic Remora.** Its cumulative upkeep taxes the mana you need on Abaddon turns. EXPOSED; no independent conclusion.

## Missing opportunities and candidates (Scryfall-verified legal, inside UBR)
- **MV-0 pool upgrades** (each one turns an MV-1 cascade into real value):
  - **Lotus Bloom:** a free 3 mana when cascaded; suspend {0} when drawn.
  - **Slaughter Pact:** free instant removal that kills Drannith; pay 2B next upkeep.
  - **Wheel of Fate:** a free full wheel when cascaded, which refills your hand with fresh hand-casts while X stays high.
  - **Mox Tantalite:** a permanent any-colour mox.
- **Noncreature answers:** Chaos Warp (any permanent, instant), Abrade, Feed the Swarm.
- **Cascade cards:** Into the Time Vortex (cascade plus rebound, and the rebound cast from exile hits every exile payoff), Deny Reality (cascade bounce of any permanent).
- **Enablers:** Guttersnipe (6 total per instant/sorcery), Glint-Horn Buccaneer (wheels and LED discards turn into damage), Torbran.
- **Considered and weaker:** Aurora Phoenix (6-MV body), Blood for the Blood God! (MV11; cost keyed to creatures dying), Poxwalkers (needs discard setup), Fiery Emancipation (6 MV), Fireblast (needs two Mountains).

## Stage A disposition — **PROPOSE SWAPS FOR CORY'S CONSIDERATION (advisory)**, the rest KEEP
| # | IN | OUT | Confidence | One-line evidence |
|---|---|---|---|---|
| 1 | Slaughter Pact | Blasphemous Act | moderate | Removal for removal. The new card is instant, one-sided, an MV-0 cascade hit and a Drannith answer; the cut card is symmetric and kills your own engine. |
| 2 | Lotus Bloom | Nightscape Familiar | moderate | Mana for mana. Bloom is a free +3 when cascaded and suspends for {0}; Familiar is a fragile 2-mana reducer. |
| 3 | Wheel of Fate | Rakdos, Lord of Riots | low–moderate | A free wheel off MV-1 cascades replaces a narrow creature reducer. Risk: the wheel is symmetric, and suspend 4 is slow when drawn. |
| 4 | Chaos Warp | Kessig Flamebreather | low (meta-dependent) | Fills the zero-hard-noncreature-answer gap. Risk: loses a combo-loop pinger. |
- [J] KEEP everything else, including the full Breach/LED/Brain Freeze package, the free counters, Bloodletter/Solphim, and the exile payoffs.
- [J] Strongest counterarguments: the Pacts add upkeep-loss risk; adding MV-0 cards slightly dilutes hits from high-MV cascades; Blasphemous Act is the only answer to a huge go-wide board when Call Forth isn't drawn.

## Tests required [H]
1. **Exact enumeration** of MV-1 and MV-5 cascade hit distributions, baseline vs. swaps 1–3. Cheap and deterministic.
2. **Opening-hand / turn-to-Abaddon** comparison: Lotus Bloom vs. Nightscape Familiar.
3. **Effect-aware multiplayer scenarios.** Opposing Drannith or RIP: does Slaughter Pact or Chaos Warp change outcomes? A wide-board scenario: is Blasphemous Act's loss material?
4. **Breach loop resource check:** does library/graveyard sustain hold with no pingers on board?

Goldfish results are not multiplayer evidence.
