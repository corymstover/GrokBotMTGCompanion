# Jeleva, Nephalia's Scourge — M6 I local-best memo for the M7 research candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved, NOT M6 certified and NOT owner-presentable. It is RESEARCH_ONLY: zero genuine swaps, below the five-swap floor. The canonical list is unchanged.

Scope: the eleven complete configurations in `data/grixis/m6/ij/tested_pools/Jeleva__Nephalia_s_Scourge_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 cards (1 commander + 99 library). This is not a global or statistical optimum.

Baseline:
- Source: canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, file `refinement/decklists/Jeleva_Nephalia_s_Scourge_Approved_2026-10-14.txt`.
- Blob 8cdc5b5a, introduced by d53789d1. Registry source_commit 1836b97 has the same bytes.
- Raw SHA-256 00e3f521… equals the overrides approved_list_sha256, the tracker final_list_hash and the registry recorded_sha256, so no provenance exception is used.

## Result
The research candidate (raw 4818b32a…, lh1:21c3ebbd…) is the canonical 100 re-serialized, with the same logical hash. It is the local best of the tested pool among configurations that respect owner direction.

**Zero genuine improvements were found, so the deck is RESEARCH_ONLY.** Five is a floor, not a target. Twenty-two candidates were judged (21 cards, Intuition against two cuts) and fifteen incumbents were challenged. Every candidate failed for one of these reasons:
- **Measured worse in the Pass C tests:** Intuition (over Long-Term Plans or Scheming Symmetry) and Galvanic Iteration (over Borne Upon a Wind).
- **Generic or homogenizing:** Dramatic Reversal + Isochron Scepter, Reanimate.
- **Marginal or no better:** Spellseeker, Forbidden Orchard, Starting Town, Mox Amber, Merchant Scroll, Cruel Tutor, Insidious Dreams, Goblin Bushwhacker, Snapback.
- **Loses colour:** Hanweir Battlements, Hall of the Bandit Lord.
- **No Jeleva value:** Twinflame and Conjurer's Closet (an uncast Jeleva has X=0), Savage Beating (dead in hand).
- **Invalid:** Dockside Extortionist is banned; Manamorphose is off-identity (R/G hybrid).
- **Staged alternative, not counted:** Snap over Gitaxian Probe (RETAIN_ALTERNATIVE).

All fifteen challenged incumbents were kept: Long-Term Plans, Scheming Symmetry, Borne Upon a Wind, Gitaxian Probe, Mental Misstep, Exotic Orchard, Arena of Glory, Scroll Rack, Personal Tutor, Torch Courier, Final Fortune, Mox Opal, Wishclaw Talisman, Fellwar Stone and Gemstone Caverns.

## Why (commander-first)
Jeleva, Nephalia's Scourge ({1}{U}{B}{R} 1/3 flying Legendary Creature — Vampire Wizard):
- "When Jeleva enters, each player exiles the top X cards of their library, where X is the amount of mana spent to cast Jeleva."
- "Whenever Jeleva attacks, you may cast an instant or sorcery spell from among cards exiled with Jeleva without paying its mana cost."

The deck's edge over a generic Grixis list is staging a spell on top, then haste, then a free cast. The two low-data incumbents (Scroll Rack 2/30, Scheming Symmetry 5/30, Arena of Glory 5/30, Personal Tutor 6/30) are exactly those blueprint pieces. The high-data challengers (Snap, Dramatic Reversal and Reanimate, 11/30 each, in a 30-deck sample) are either generic or don't clearly beat their slot.

**Closest call: +Snap −Gitaxian Probe.**
- Snap is mana-neutral with two untapped lands; it protects Jeleva and resets her to a larger X on recast (commander tax raises X).
- But Probe is 17/30 against Snap's 11/30. Probe is free on turn 1 and is Breach/LED fuel.
- It stays RETAIN_ALTERNATIVE as an owner decision and is not counted.

## Owner direction
- Every incumbent is owner-directed: 37 retained baseline cards plus 62 owner additions.
- Long-Term Plans, Scroll Rack, Opposition Agent and Hexing Squelcher are explicit adversarial-pass keeps.
- No cut was clearly better on evidence, so **no owner keep or addition is overridden**.
- **Owner-removed cards and classes are not re-added:** Mana Drain, Cyclonic Rift, Mizzix's Mastery, Time Stretch, Nexus of Fate, Swiftfoot Boots, Frantic Search, the signets, Mountain and the 7–10-mana haymaker class.
- **Owner-rejected cards are not re-added:** The One Ring, Beseech the Mirror, Praetor's Grasp, Notion Thief, Dauthi Voidwalker, Orcish Bowmasters, Valley Floodcaller, Roaming Throne, Strionic Resonator, Burnt Offering and Rain of Filth.
- The staged alternatives are complete 100s on the baseline, so the owner can pick one directly.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Jeleva__Nephalia_s_Scourge_bounded_measured_tests_20261023.json` and recomputed in `tests/test_m6_jeleva_nephalias_scourge_m7_mechanics.py`.

Pass C's final disposition was **NEEDS TESTING**. It asked for a targeted Phase B: the baseline against +Intuition −Long-Term Plans and +Intuition −Scheming Symmetry, with Jeleva top-stage success, haste access and hostile Breach-pile castability; and +Galvanic Iteration −Borne Upon a Wind, distinguishing casts from copies. The Pass C receipt is a NON-INDEPENDENT owner-equivalent review (alias Josh-Lee-Kwai, ChatGPT/OpenAI GPT-6, with a technical-independence waiver).

1. **T1 stager access.** There are 11 direct Jeleva stagers in the 99. Exact P(at least one):

   | Cards seen | Baseline | Minus one stager (either Intuition swap) |
   |---|---|---|
   | 7 | 0.5736 | 0.5372 |
   | 8 | 0.6246 | 0.5875 |
   | 9 | 0.6699 | 0.6328 |
   | 10 | 0.7103 | 0.6736 |

   Long-Term Plans' third-from-top card is captured at once by X≥4, so the GrokBot "waits two draws" premise is false. Intuition never puts a card into the library.
2. **T2 Intuition hostile piles.** Exhaustive enumeration of the opponent's choice: the Breach/LED/Brain Freeze pile and the Oracle pile both fail early (the opponent hands over the dead piece and strands Breach in the graveyard). The triple-tutor pile is a slower stager.
3. **T3 Galvanic Iteration vs Borne Upon a Wind.**
   - The copy is not cast (CR 707.10), so it adds no storm count.
   - Eight key targets gain nothing or are harmed: Demonic Consultation, Doomsday, Final Fortune, Mnemonic Betrayal, Peer into the Abyss, Tainted Pact, Toxic Deluge and Yawgmoth's Will.
   - Jeleva haste/flash enablers go from 4 to 3. P(at least one) falls from 0.2577–0.3514 to 0.1994–0.2760 over 7–10 cards.
4. **T4 Mox Opal.** With 16 artifacts, P(at least 2 other artifacts | Opal) is 0.2277, 0.2906, 0.3536 and 0.4152 with 6, 7, 8 and 9 other cards.
5. **T5 Spellseeker reach.** 29 instants and sorceries with MV≤2.
6. **T6 colour sources.** U/B/R 21/20/19. Forbidden Orchard leaves this unchanged; Hanweir Battlements drops R to 18.

Commander Spellbook: the baseline has 7 complete combos. Every alternative is 7, except Dramatic Reversal + Isochron Scepter, which is 8 (4821-5261).

Not done, stated plainly: there were no matched-hand games, no opponent model and no win rates. The repo has no validated Jeleva game engine.

## Limits
Only finite scripted rules cases and exact enumerations are tested.

- Game Changers 20 → 20 (Bracket 5).
- Average nonland MV 1.9 → 1.9.
- Commander Spellbook 7 → 7 complete combos.
