# M6 two-model reconciliation — Obeka, Splitter of Seconds (#45 / tracker index 44)

**Date:** 2026-10-20. **Class:** engineering-only ChatGPT reconciliation, **NOT formally independent Pass C**. GrokBot first pass is ADVISORY (prior blueprint/engineering exposure); ChatGPT already authored original comprehensive review. No canonical mutation/approval, no milestone credit for independence.

## Authority and exact source

- Canonical: `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json#Obeka__Splitter_of_Seconds`; APPROVED and LOCKED.
- **Exact live approved raw SHA-256** `c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63`; approved TXT `refinement/decklists/Obeka_Splitter_of_Seconds_Approved_2026-10-15.txt`, blob `3744ef1e8d127a6262abbfd8e064c475b8ee0654`.
- Separately recorded engineering logical hash `lh1:95dc0a60266129426fa099fdb3188f143829ca9f23d5d65357f1a02a7cbf2912`. The obsolete Oct12 reported SHA beginning `83062...` must NOT be reused; old source-hash error was already fixed without membership edits.
- Canonical TXT read from live main and independently recounted: **100 copies, 96 unique card names, only Island x3 / Mountain x2 / Swamp x2 repeated**, commander+99 library, **35 land copies**. Rogue's Passage ABSENT, Swamp x2 PRESENT. Aqueous Form, Brotherhood Regalia, Thassa, Silent Arbiter, Shizo, Silver Shroud Costume and haste/protection suites PRESENT. Legal UBR official checkpoint Oct15–16, zero project exceptions. Current spot Oracle checked commander, Rogue's Passage, Silent Arbiter and Thassa; this is NOT an all-96 fresh Scryfall legality sweep.
- [ChatGPT original authored review](https://github.com/corymstover/GrokBotMTGCompanion/blob/chatgpt-cycle76-m6-refinement/data/grixis/m6/deep_reviews/Obeka__Splitter_of_Seconds.md) Git blob `1a00170172258f6f88a8fa2f8760d479437849da`, concluded KEEP with **separate hypothetical Academy Manufactor / Paradox Haze** challenger for owner consideration. Prior original review is not independently authoritative.
- [GrokBot advisory](https://github.com/corymstover/GrokBotMTGCompanion/blob/chatgpt-cycle76-m6-refinement/data/grixis/m6/grokbot_pass_c_advisory/Obeka__Splitter_of_Seconds.md) blob `53b7c43fdc0d0451615bd33cbe7fdb9419f4e2f2`, POSSIBLE UPGRADE `+Rogue's Passage / -Swamp`, sealed in batch 43–62 with prior engineering exposure disclosures.

## Commander-first payoff and actual rules

**Obeka, Splitter of Seconds** is 2/5 menace {1}{U}{B}{R}. If she DEALS actual **combat damage to a PLAYER**, her triggered ability grants that many **additional upkeep steps after the current combat phase**. Each is in an extra beginning phase with **untap and draw steps skipped**, so a hit for 2 = two additional upkeeps; power modification prior to damage changes the number. Each additional upkeep triggers Courts/monarch, Phyrexian Arena, Darksteel Reactor, Tamiyo's Journal, Smaug, rings, Time Sieve and related setup, with actual timing and survival restrictions. Pump+double strike/copies must account for damage events and independent triggers. Obeka's menace requires **two or more blockers** to block her.

**Rogue's Passage**: Commander-legal COLORLESS land; `{T}: add {C}`; `{4},{T}: target creature can't be blocked this turn.` It works if activated **before blockers are declared** (even if after attack declaration, when priority is available); can't retroactively unblock a creature once blocked. It requires **four other available mana plus tapping the Passage**, an opportunity cost equivalent to five land/mana resources this turn. It's repeatable, cannot be used both for {C} and its own activation in the same untap without an additional untap, and activation can be answered with creature removal, land destruction or other targeted effects. It is fully legal in Obeka's UBR identity; that's NOT enough to prove improvement.

**Swamp** is a black-producing basic untapped land, also a fetchable basic Swamp-type target. Cutting one reduces approved 2 Swamps → 1, constraining untapped black, shroud-proof base sources and basic search under nonbasic hate; UBR commander cast and life-costed `Hatred` ({3}{B}{B}) both require real black pips. Although fetchable typed duals and `Urborg, Tomb of Yawgmoth` cushion that loss, Urborg is only a singleton and cannot be assumed on board. Rogue's Passage gives no U/B/R without Urborg or another actual color-changing effect.

### Existing evasion (not merely hypothetical)

1. **Aqueous Form** ({U}) attaches to Obeka to make it **unblockable**, also scry when attacks. Low mana, immediately works on subsequent attack, but Aura can expose two-for-one removal/shroud targeting complications.
2. **Brotherhood Regalia** is on-list and supplies unblocked connection for a legendary creature, plus protection/ward at equip/timing cost.
3. **Thassa, God of the Sea** ({2}{U}) has **{1}{U}: target creature you control can't be blocked this turn**. Cheaper REPEATABLE active unblockability (2 mana vs Rogue's 4+tap), and at beginning of **your upkeep** scry 1 — meaning Obeka's many extra upkeeps produce repeated scry value even independent of activated unblockability. It is an extremely Commander-first and strictly distinct multi-role land-vs-spell comparison.
4. **Silent Arbiter** permits **no more than one creature to block each combat**. Since Obeka has menace (requires at least two creatures to block), if Arbiter remains on the battlefield through blockers, an attacking Obeka cannot legally be blocked by creatures. Arbiter is a *standalone evasion piece* for Obeka, not generic one-blocker defense.
5. **Shizo, Death's Storehouse** provides B mana and can give target legend fear as source-paid activation, restricting who may block; not full unblockability versus black/artifact blockers. It protects colored access unlike Rogue. **Silver Shroud Costume** provides its own commander-protection/evasion package; do not treat every protection item as another copy of Rogue's Passage without Oracle checks.
6. Natural **menace**, equipment/haste and commander-specific targeted counterspells increase connection chances. This is not a zero-evasion approved 99.

## Adjudication of exact GrokBot pair

**Decision: REJECT EXACT SWAP / KEEP BASIC SWAMP.** The candidate is *technically valid* and on-theme but the specific land substitution does **not** establish net improved connection probability or faster, protected Obeka upkeeps.

**Benefit acknowledged:** Land-slot repeatable unblockability is difficult to counter and gives a late-game guaranteed connection against a board with multiple blockers even if opponent removed Aqueous Form/Regalia/Thassa/Arbiter. Unlike nonland evasion, it consumes a land rather than a spell slot. In an unusually slow creature-stalled pod with abundant mana and reliable colored sources, passage could be a good meta choice, and activated unblockability can convert one power-boosted Obeka hit into 5–20 upkeeps.

**Key cost overlooked by GrokBot:** Obeka is four colored pips? **No: its actual cost is {1}{U}{B}{R}**, requiring **three specific colors plus one generic**, so a colorless early land can strand commander despite total mana seeming adequate. Rogue's {4}+tap is a major commitment on the very combat turn when mana is needed for `Hatred` (X life plus B), protection (An Offer/Fierce with proper condition), equipment and upkeep artifact setup. Thassa's 1U activates at half the generic outlay and grants scry on EVERY resulting extra upkeep. Redundant unblockability has falling marginal value when Aqueous/Regalia/Thassa/Arbiter already exist; the missing black on a T1–T4 land can matter before any unblockable source is relevant.

**Competing cuts examined:**
- **Shizo → Rogue's Passage:** both utility lands but Shizo produces black and gives conditional evasion at low mana; replacing it exacerbates rather than solves color constraint. **Worse cut**.
- **Arena of Glory → Rogue's Passage:** Arena provides original combat haste synergy and red-related mana; loss of commander attack timing/power undermines Obeka far more than another unblockable source helps.
- **Reflecting Pool → Passage:** Pool is colored only when another source supports; still stronger early UBR access in the current nonbasic-rich mana base. Loss worsens color consistency.
- **Ancient Tomb → Passage:** sacrifices turn-two/t3 generic mana acceleration for an expensive activated effect. Tomb can pay initial setup/protection; better to retain.
- **Thassa → Passage:** gains a land slot only if compensated by a spell slot elsewhere and sacrifices repeated **extra-upkeep scrys** and cheaper unblockability, a directly commander-specific loss. **Do not replace**.
- **Aqueous Form or Brotherhood Regalia → Passage** is not a direct 1:1 mana-neutral swap: to remain at 100, must replace a spell with a land and now increase lands to 36/100; it can be explored only if changing the deck's land/spell proportions is justified. Aqueous cheap evasion and Regalia legendary equip plus protection are both strong; no better exchange established.
- **Basic Swamp (GrokBot's cut)** is particularly expensive when only two basic Swamps exist and the commander needs B; check meta nonbasic hate and black availability before revisiting.

### Finite source-paid scenarios

**A: early colored turn.** Lands Island, Badlands, Swamp, Rogue Passage rather than second Swamp. The current exact colors U/B/R are available if Badlands survives; but if opponent destroys a dual or `Back to Basics`/Blood Moon-type effect constrains nonbasics, two black basics keep `Hatred` and future commander recast more feasible. A first-three-lands hand Island, Mountain, Passage with no other black source cannot cast Obeka even if total 3+ rocks later produce C.
  
**B: cost of unblockability.** Obeka on field with 4 other mana and untapped Passage. Tap all other four, tap Passage; target Obeka, gain unblockable for turn; attack for 2 yields 2 extra upkeep triggers. With Thassa already in approved 100, pay {1}{U} (2 mana) and still have more mana to equip/counter/pump and protect combat; the outcome is the same unblockable Obeka, plus Thassa scries during each extra upkeep.
  
**C: Silent Arbiter.** Control 2/5 menace Obeka and Arbiter. Declare Obeka attacking; blocker declaration legally allows at most ONE creature to block, but menace means at least TWO needed, so no blocks allowed while both effects apply. Rogue passage activation is unnecessary. If Arbiter leaves before blocks, blockers may now block; Passage is an additional safety if mana available and unactivated prior blockers. The value is conditional redundancy, not distinct baseline absence.
  
**D: high-mana stalled field.** Opponents have several creatures and have removed every other evasion source, board 9 lands incl Passage with sources for UBR and 4 available. Rogue is powerful here: connect for pumped 5–10 damage, generate that many upkeeps, possibly win off ring/Court/Sieve setup. This is the best argument to test the swap in prolonged games; early-game color penalty remains unmeasured.

## Other meaningful challenger from ChatGPT deep review — separate pending hypothesis

Original ChatGPT authored review identified **Academy Manufactor / Paradox Haze** as a potentially stronger commander-first upgrade than rank-suggested swaps. With **Tamiyo's Journal** producing a Clue each upkeep and **Smaug the Magnificent** producing a Treasure each upkeep, Manufactor's replacement would produce **three artifact tokens for each original event**, six total with both sources in play. Extra Obeka upkeeps increase the volume; five artifacts can fuel **Time Sieve** for additional turn at true mana/tap/sacrifice costs. But Manufactor (1/3) is fragile, cannot help WITHOUT token creation, and losing Paradox Haze removes one guaranteed extra upkeep each own turn even with Obeka unavailable. This is **NEEDS TESTING / NOT an independently accepted owner proposal here**; no measure of how often both generators + Manufactor + Sieve coexist or survive interaction. Do not silently promote the author's separate proposal just because it has higher ceiling.

## Final decision and gates

- **GrokBot `+Rogue's Passage / -Swamp`: REJECT EXACT, KEEP canonical source**.
- **Owner action:** none for this exact proposal; reconsider only if colored early source simulation and evasion-failure matchup support it.
- **Open alternate**: Manufactor for Paradox Haze merits targeted uptime/board token/survival analysis, not an automatic replacement.
- **Legality/rules:** both Rogue and current Swamp are officially legal in UBR; Obeka's postcombat extra upkeep steps verified against Wizards OTJ rulings; no unexpected legality blocker. 100/96 baseline singleton checked, power remains **Bracket 4 — Optimized**.
- **Evidence remaining:** early UBR cast timing with Passage vs Swamp, share of games all existing evasion removed and Passage activation available, actual protected connection; and token engine survivability if testing Manufactor.
- **Certification boundary:** no canonical changes, no approval/lock SHA updates, no formal independent Pass C, no claimed effect-aware Phase B, no M6 certificate; same-model ChatGPT reconciliation transparently disclosed.

**Sources:** [exact canonical approved 100](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/decklists/Obeka_Splitter_of_Seconds_Approved_2026-10-15.txt), [GrokBot advisory](https://github.com/corymstover/GrokBotMTGCompanion/blob/chatgpt-cycle76-m6-refinement/data/grixis/m6/grokbot_pass_c_advisory/Obeka__Splitter_of_Seconds.md), [original ChatGPT review](https://github.com/corymstover/GrokBotMTGCompanion/blob/chatgpt-cycle76-m6-refinement/data/grixis/m6/deep_reviews/Obeka__Splitter_of_Seconds.md), [Obeka + official extra-phase rulings](https://mtg.wtf/card/otj/222/Obeka-Splitter-of-Seconds), [Rogue's Passage](https://mtg.wtf/card/fic/415/Rogues-Passage), [Thassa](https://mtg.wtf/card/pio/288/Thassa-God-of-the-Sea), [Silent Arbiter](https://mtg.wtf/card/cmm/972/Silent-Arbiter), [Wizards Comprehensive Rules](https://magic.wizards.com/en/rules).
