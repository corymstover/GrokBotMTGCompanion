# Kess, Dissident Mage — M6 I local-best memo for the M7 research candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved, NOT M6 certified and NOT owner-presentable. It is RESEARCH_ONLY: one genuine swap, below the five-swap floor. The canonical list is unchanged.

Scope: the fourteen complete configurations in `data/grixis/m6/ij/tested_pools/Kess__Dissident_Mage_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 cards (1 commander + 99 library). This is not a global or statistical optimum.

Baseline:
- Source: canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, file `refinement/decklists/Kess_Dissident_Mage_Approved_2026-10-14.txt`.
- Blob 4e3feb62, the owner's 2026-10-14 approved rebuild. Registry source_commit 1836b97 has the same bytes.
- Raw SHA-256 93d27d60… equals the overrides approved_list_sha256 and the registry recorded_sha256, so no provenance exception is used. Logical hash lh1:d89d5778….
- Disclosed, not changed: the tracker row still reads PENDING while overrides record the deck APPROVED; the registry Archidekt export `exports/grixis-archidekt/kess-dissident-mage.txt` (raw 94dee35a…) is the same 100 in `1 Card` format and order, with the same logical hash, so it is current, not stale.

## Result
The research candidate (raw d8fc71c1…, lh1:066fc59a…) is the canonical 100 with **+Mana Drain −Personal Tutor**. It is the local best of the tested pool.

**One genuine improvement was found, so the deck is RESEARCH_ONLY.** Five is a floor, not a target. Twenty-five candidates were judged and fifteen incumbents were challenged. Apart from Mana Drain, every candidate failed for one of these reasons:
- **Dominated for the same slot:** Spell Pierce (soft counter; EDHREC cEDH 122/387 against Mana Drain's 234/387). The two-card package Mana Drain + Spell Pierce over Personal Tutor + Fellwar Stone is rejected because Fellwar Stone (cEDH 275/387) accelerates a four-mana commander.
- **Does not clearly beat an owner keep, spine card or addition:** Notion Thief, Narset, Parter of Veils and Hexing Squelcher (Ledger Shredder, owner spine), Undercity Sewers (City of Traitors).
- **Generic, colourless or anti-Kess:** Mnemonic Betrayal (exiles itself, so Kess cannot recast it), Urza's Saga and Exotic Orchard (City of Traitors; colourless or low synergy with a fetch-heavy base), Timetwister (shuffles your own graveyard away).
- **Marginal or no better:** Praetor's Grasp over Ponder (low confidence), Cyclonic Rift over Into the Flood Maw (equal cEDH events adoption, adds a Game Changer), Snap, Muddle the Mixture, Lim-Dûl's Vault, Dispel, Lightning Bolt.
- **Owner-rejected on 2026-10-14, inadmissible:** The One Ring, Opposition Agent, Dauthi Voidwalker.
- **Invalid:** Manamorphose (R/G hybrid) and Silence (W) are outside U/B/R.
- **Staged alternatives, not counted (RETAIN_ALTERNATIVE):** Grim Tutor over Demonic Counsel (overrides an explicitly accepted owner keep without clear evidence); Jeska's Will over Ledger Shredder and Frantic Search over Personal Tutor (both Pass C lines; the owner cut both cards on 2026-10-14). These are owner decisions only.

Challenged incumbents: Personal Tutor (cut), Deadly Rollick, Demonic Counsel, Ledger Shredder, Displacer Kitten, City of Traitors, Ponder, Into the Flood Maw, Fellwar Stone, Grinding Station, Final Fortune, Gitaxian Probe, Rite of Flame, Mental Misstep and Windfall. All except Personal Tutor were kept.

## Why (commander-first)
Kess, Dissident Mage ({1}{U}{B}{R} 3/4 flying Legendary Creature — Human Wizard): "Once during each of your turns, you may cast an instant or sorcery spell from your graveyard. If a spell cast this way would be put into your graveyard, exile it instead."

The deck's edge over a generic Grixis list is the second, paid, own-turn cast of every instant and sorcery: Demonic Consultation or Tainted Pact recast in response to Thassa's Oracle's trigger, a second tutor, ritual, wheel or Final Fortune, and Displacer Kitten blinking Kess for a fresh permission.

**The one swap: +Mana Drain −Personal Tutor (MODERATE confidence).**
- Mana Drain is the most-played non-incumbent card for Kess: EDHREC cEDH 234/387 (60.5%), stats.cedh.events 51.7% of 87 Kess decklists, repo EDHTop16 one-year 32 entries / 4 top cuts (conversion 0.125 against the commander's 0.1207: neutral, small sample).
- Kess fit: recast from the graveyard during your precombat main phase or combat, its colourless mana arrives in the postcombat main phase of the same turn (Mana Drain ruling 2020-11-10; CR 505.1, 106.4). From hand it is a hard counter on any turn. It is blue, so Force of Will / Force of Negation pitch count stays at 26.
- Personal Tutor is the least-adopted card in the 99: EDHREC cEDH 26/387 (6.7%), absent from the stats.cedh.events staple list. It puts a sorcery on top (not in hand), cannot find the instant win pieces (Demonic Consultation, Tainted Pact, Brain Freeze) and overlaps Mystical Tutor inside a 14-card tutor suite.
- Bounded cost: P({U}{U} available) turns 2–6 0.5028/0.6688/0.7442/0.7973/0.8395; the Demonic Counsel delirium proxy drops by at most about 1.5 points (turn 6 upper bound 0.401 → 0.3858). Commander Spellbook 6 → 6; Game Changers 21 → 21.
- **Data caveat:** EDHTop16 conversion for Mana Drain (0.125) is level with the field (0.1207) on 32 entries; the case rests on adoption and Kess's own-turn recast, not on a measured win-rate gain.
- **Owner-direction flag:** Personal Tutor is an owner addition from the 2026-10-14 rebuild (one of 41 adds; not in the adversarial second pass, not spine-named). The evidence is the clearest in the pool, so the override is proposed and flagged. The owner-respecting fallback **+Mana Drain −Deadly Rollick** (Rollick is retained from the pre-rebuild list, not an owner addition) is staged as a complete 100. The zero-swap baseline remains available.

## Owner direction
- Every incumbent is owner-directed (the 2026-10-14 rebuild). The one cut, Personal Tutor, is an owner addition, so **an owner addition is overridden**; it is flagged above with a staged owner-respecting fallback. No explicit keep or spine card (Demonic Counsel, Ledger Shredder, Displacer Kitten, Thassa's Oracle, Underworld Breach, Gifts Ungiven, Valley Floodcaller and the rest of the protected core) is cut.
- **Owner-removed cards and classes are not re-added:** Consider, Jeska's Will, Flame of Anor, Past in Flames, Yawgmoth's Will, Mizzix's Mastery, Thousand-Year Storm, Professor Onyx, Talrand, Guttersnipe, Young Pyromancer, the Hoarding Broodlord package, The One Ring, Opposition Agent, Dauthi Voidwalker, Frantic Search, Birgi, Chaos Warp, Sensei's Divining Top, Cursed Totem and the other 2026-10-14 cuts. Jeska's Will and Frantic Search appear only as staged owner-decision alternatives because Pass C asked for them.
- The staged alternatives are complete 100s on the baseline, so the owner can pick one directly.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Kess__Dissident_Mage_bounded_measured_tests_20261023.json` and recomputed or consistency-checked in `tests/test_m6_kess_dissident_mage_m7_mechanics.py`.

Pass C's final disposition was **NEEDS TESTING**: retain the canonical deck, and compare it against +Jeska's Will −Ledger Shredder (priority 1) and +Frantic Search −Personal Tutor (priority 2), counting real coloured sources, land-versus-rock payment, first Kess deployment, usable own-turn graveyard casts, four-type delirium, blue Force-pitch availability and opponents' hand sizes. The Pass C receipt is a NON-INDEPENDENT owner-equivalent review (alias Josh-Lee-Kwai, ChatGPT/OpenAI GPT-6, with a technical-independence waiver).

1. **Blue Force-pitch availability (exact hypergeometric).** P(another blue card in hand, given a Force in hand), turns 1–6:

   | List (blue cards in 99) | T1 | T2 | T3 | T4 | T5 | T6 |
   |---|---|---|---|---|---|---|
   | Baseline (26) | 0.8383 | 0.8822 | 0.9146 | 0.9383 | 0.9556 | 0.9682 |
   | +Jeska's Will −Ledger Shredder (25) | 0.824 | 0.8699 | 0.9042 | 0.9298 | 0.9487 | 0.9627 |
   | Candidate +Mana Drain −Personal Tutor (26) | 0.8383 | 0.8822 | 0.9146 | 0.9383 | 0.9556 | 0.9682 |

2. **Jeska's Will by opponent hand size (exact).** Net mana after paying {2}{R} = hand size − 3 (−3 at 0 cards, +4 at 7). No hand-size logs exist in the repo, so no distribution is claimed.
3. **Frantic Search three-land access (seeded Monte Carlo, seed 26, N=200000).** P(three lands in play) turns 3–6: 0.4658/0.5485/0.6236/0.6912; rocks and fast mana are not refunded.
4. **First Kess deployment (seeded Monte Carlo; conservative, rocks beyond Signet/Talismans ignored).** P(four mana including U, B and R) turns 3–6: 0.1215/0.3577/0.4488/0.5328. Identical for baseline and candidate (no land or rock changes).
5. **Demonic Counsel delirium proxy (seeded Monte Carlo).** No Demon in the 99. Turn 6: baseline 0.0922 lower / 0.401 upper; candidate 0.0868 / 0.3858; +Frantic −Personal 0.086 / 0.4013.
6. **Usable own-turn graveyard casts / matched-hand win outcomes.** Not run: the repo has no validated Kess game engine and no opponent model.

Commander Spellbook: the baseline has 6 complete combos and the candidate 6. Jeska's Will adds 1368-1878-2706 and Frantic Search adds 1368-2196-3766 (7 each); every other alternative is 6.

Not done, stated plainly: there were no matched-hand games, no opponent model and no win rates. The bounded tests show the Pass C alternatives trade a measurable cost (one fewer blue pitch card; land-only refunds) for situational gains, which is why both stay owner-decision alternatives.

## Limits
Only finite scripted rules cases, exact enumerations and seeded proxies are tested.

- Game Changers 21 → 21 (Bracket 5).
- Average nonland MV 1.85 → 1.86.
- Commander Spellbook 6 → 6 complete combos.
