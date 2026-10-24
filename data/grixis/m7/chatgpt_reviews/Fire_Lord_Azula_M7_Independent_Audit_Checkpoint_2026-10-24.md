# Deck #19 Fire Lord Azula — ChatGPT independent M7 adversarial checkpoint (2026-10-24)

**STATUS: RESEARCH_ONLY / NOT OWNER-APPROVED / NOT CANONICAL / NO FINAL CANDIDATE YET.**

This review is stacked on GrokBot PR #667 head `1946a316e457f5751dbd8bca2f3e67bdf0530cd7` for provenance. It does **not** revise the approved canonical October 14 source `refinement/decklists/Fire_Lord_Azula_Approved_2026-10-14.txt` (raw SHA-256 `b6ef396641f2b5cfac0eb81fb494f21f3745e2a3fd47fa75d2eaadbdc34ddee5`). GrokBot's proposed candidate `f4136ea0028ee787dddad379e12a7e34ccdaa6578a52d1c63ae953734e5806f2` is first-pass research, **not** an owner-approved M7 deck.

## Commander-first and fast mana

Azula must attack for her copy trigger. Her firebending 2 generates {R}{R} until end of combat. Copies are not cast, but preserve additional-cost status. Strongest realistic strategy still uses quick Azula deployment, haste/timing support, combat-window duplicated spells, the Narset's Reversal + Frantic Search loop, Oracle/Consultation/Pact and Breach engines, compact fast mana and protection. Bracket 5 cEDH; no exception.

## Critical independent correction: Big Score versus Unexpected Windfall

My initial comment on PR #667 incorrectly said Big Score consumes three additional mana while Azula attacks. **Retracted.** Both spells cost four total:
- Big Score {3}{R}: pay one firebending {R} for colored {R}, the other firebending {R} toward {3}; **{2} remains**.
- Unexpected Windfall {2}{R}{R}: pay both firebending {R}{R} toward colored pips; **{2} remains**.
- Both require one discard; copied by Azula, each draws four cards and produces four Treasure tokens if both resolves.

Big Score is *more flexible outside combat* because it needs only one red mana. It is **not quality-positive** to call Windfall a strict replacement for Big Score. Windfall is still a valid *additional redundant copy payoff* worth testing against a different cut; the Grok PR pairs it with Vivi Ornitier, a separate 3-MV mana/ping engine. Redundancy versus losing Vivi remains a real decision, not proven by adoption percentages (Windfall 42.5% in Grok's stats.cedh.events snapshot).

## Protection / mana stress tests before any five-swap floor

1. **Swan Song must be protected by default.** One-mana live counter to instant/sorcery/enchantment, 56.9% stats.cedh.events adoption. +Flashback/-Swan sacrifices essential cEDH stack interaction. `Repeal` is a better-tested possible nonland cut for Flashback, but losing Repeal's bounce-cantrip must be costed.
2. **Gemstone Caverns must be protected by default.** Turn-zero any-color acceleration on the draw when it has a luck counter, high cEDH inclusion. +Mistrise Village/-Caverns is not an acceptable automatic upgrade; challenge -Wooded Foothills if Village really belongs. Mistrise is U-only, enters tapped unless a Mountain/Forest is controlled, and grants uncounterability for the next spell at {U}+{T}; there are four Mountain-typed duals and fetch access, not a guaranteed untapped source.
3. **Samut, Tyrant of Naktamun is an explicit October 14 owner addition.** Split second on our spells powerfully protects spells, and Azula's triggered copy still happens. However Samut prevents our own Narset's Reversal from being cast in response to Frantic Search/Turnabout and prevents the free cast from a bargained Beseech. Do not simply delete Samut because a new loop exists: compare interaction-heavy wins versus 4-MV Turnabout, including Hexing Squelcher's redundant can't-be-countered protection. Any proposed cut is flagged for explicit owner scrutiny.
4. **Sink into Stupor // Soporific Springs versus Exotic Orchard** is not pure value. The MDFC offers a copied instant bounce, but its U-only land face costs 3 life to enter untapped; as a *front-faced 3-MV card* it also increases Ad Nauseam life loss if revealed versus Orchard's 0 MV. Orchard's multicolor fixing is especially relevant to Azula's {U}{B}{R} and double-blue Reversal/Turnabout. Quantify both costs before selection.
5. **Samut, Hazoret's Champion** ({1}{R}, 2/2, other abilities: creatures you control have haste) is a current legal new contender *not* among October 14 owner-removed cards. It gives Azula same-turn attack access with no equip/target conflict. The baseline's independently named haste access is Arena of Glory / Crimson Wisps / Expedite (3); adding Champion makes 4. In a raw 99-card library, ten draws find >=1 of three in 27.60% versus four in 35.14% (7.54 percentage point increase), **not** a playable-turn or match win-rate estimate. Compare directly with Vivi, an independent repeatable mana engine and ping payoff, before any cut.
6. **Turnabout** is an important Azula-specific addition: while Azula attacks it can untap lands twice, and alongside Narset's Reversal it forms Commander Spellbook combo `11-4276-7089`. The loop needs Azula attacking, enough lands producing mana, timing and a finishing spell. Four mana and duplicate loop redundancy are opportunity costs.
7. **Flashback** {R} gains one graveyard instant/sorcery flashback until end of turn, with Azula copying the targeting instant to grant another. Flashback is not itself free casting: the graveyard spell requires its mana-cost-equivalent flashback payment, appropriate timing, and is exiled afterward. Graveyard hate is an important failure mode.
8. **Electrodominance**, **Leyline of Anticipation**, **Storm-Kiln Artist**, **Spellseeker**, **Lightning Greaves**, **Twinning Staff** and other October 14 explicitly rejected/removed choices are not automatically reintroduced to reach the five-swap minimum. Electrodominance's instructed cast also clashes with Samut's split second while the spell is resolving. EDHREC high lift is discovery, not deckbuilding proof.

## Active full-100 comparisons (not selected, not verified for approval)

- **Grok first-pass:** +Turnabout/-Samut, +Sink/-Orchard, +Windfall/-Vivi, +Flashback/-Swan, +Mistrise/-Caverns. Five swaps but sacrifices both cEDH interaction and turn-zero mana, so reject as an automatic final.
- **Defense-preserving five-under-challenge:** +Turnabout/-Samut; +Sink/-Orchard; +Windfall/-Vivi; +Flashback/-Repeal; +Mistrise/-Wooded Foothills. Keeps Swan Song, Gemstone Caverns, Big Score; still needs mana/Ad Nauseam and duplicate-four-mana-draw tradeoff proof.
- **Haste alternative:** In the prior full-100 comparison, consider +Samut, Hazoret's Champion/-Vivi instead of +Windfall/-Vivi. This favors access to Azula's same-turn attack over duplicated four-mana value. Neither is automatically selected.
- **Keep-Samut variant:** Avoid replacing explicit owner-protected split second unless scenario analysis proves the new combo worth its loss.

**Stopping rule:** Five owner-presentation swaps is a **minimum floor, not target or cap**. Continue looking past five and reject gratuitous replacements. If fewer than five honest quality-positive swaps survive, report RESEARCH_ONLY and preserve the canonical baseline. Do not invent a SHA-bound approval candidate prematurely.

## Evidence and next gate

- Frozen October 23 Scryfall 205-name oracle snapshot and 100-list corpus: `data/grixis/m6/oracle_snapshots/Fire_Lord_Azula_M7_Scryfall_20261023.json`.
- EDHREC general / optimized / cEDH and stats.cedh.events dated October 23: `data/grixis/m7/research_challengers/Fire_Lord_Azula_EDHREC_discovery_20261023.json`.
- Commander Spellbook source-backed baseline 9 combos / Grok candidate 10: `data/grixis/m7/research_challengers/Fire_Lord_Azula_CommanderSpellbook_20261023.json`.
- Current official/rules texts are staged, but **no validated multiplayer goldfish or win-rate model** exists. The previous finite turn-four castability proxy omits several fast-mana lines and is not a success-rate claim.
- Need exact 100, full interactions and mana tests, selected current Oracle/rules and card legality, SHA, staged focused tests and exact-head CI **before** owner presentation. No canonical write or approval now.

## Exact research-only 100-card alternative seals and bounded comparison

Three **complete 100-card, singleton, official-Commander-legal, UBR** alternatives have been added as noncanonical evidence (each with 26 land faces including the Sink MDFC and 20 Game Changers). Each raw source was independently SHA-256 hashed before staging; all are named `Under_Review`, and **none is presented to Cory for approval**.

| Staged alternative | Raw SHA-256 | Swaps | Protected current staples |
|---|---|---:|---|
| Defense-preserving five | `390d09cd01672fb30b4f6d758db9562c04b453d11bcf9d434808c61bde4b3f7c` | 5 | Swan Song, Gemstone Caverns, Big Score |
| Haste five | `76f298c328d5ce76e43dba32c04d4f3dc4d8e57d2ff3827e681563da254d2ec3` | 5 | Swan Song, Gemstone Caverns, Big Score, Samut Hazoret's Champion |
| Keep-Samut four | `2e3deb60bce700d5a59478c4ca65c8c84b18c37c576a54bc54a3a5af9d4a91bb` | 4 | Swan Song, Gemstone Caverns, Samut Tyrant and Big Score |

**Finite castability proxy, Azula by turn four on the play:** frozen baseline 0.4920; each alternative 0.4874 when the Sink MDFC may be played as a land, 0.4604 when it is never a land. This is a **0.0046 (0.46 percentage-point) decline** compared with the baseline when the MDFC provides mana; it does not count the MDFC's three-life untapped cost, Mistrise tapped timing, fetch/shock life, moxen, rituals, haste, or actual opponent interaction. These proxy values are **not win rates** and do not settle the strategic value of any alternative.

The matching independent test `tests/test_m7_fire_lord_azula_chatgpt_alternatives.py` checks raw SHA, complete count, singleton, UBR, current stored Commander legality, exact diffs, Swan/Caverns keeps, Big Score/Windfall correct payment, Ad Nauseam/MDFC life tradeoffs, haste raw-draw proxy and these bounded castability values. CI on the exact alternate branch must pass; it does not certify a final owner-ready deck.

**Next strategic decision:** whether a fifth quality-positive change exists beyond the clear commander-synergy opportunities, given the genuine costs of replacing an any-color fetch/Orchard with conditional blue lands and the tension between duplicate four-mana draw and immediate haste access. If not, mark RESEARCH_ONLY, never pad merely to reach five.
