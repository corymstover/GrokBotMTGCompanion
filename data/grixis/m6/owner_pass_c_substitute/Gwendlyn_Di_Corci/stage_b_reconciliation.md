# Josh-Lee-Kwai — Gwendlyn Di Corci — controlled Stage B

**Date:** 2026-10-21 America/Chicago | **Tracker:** #22 | **Source SHA-256:** `9a393cb7edf40f9bfb388d37dd657839cad851dc6a021440c7d1b239c1fd20a9`.  
**Immutable first-stage commit:** `6c381750b3dd20053c6d6f021087e04a634a46fd` | **Verified separate seal commit:** `a0e4ac5f8cf1dc239a0ca2140125716793646b3a`. Remote Stage A byte match and seal ancestry were verified before these other opinions were first opened.

## Exactly identified prior evidence

1. `data/grixis/m6/deep_reviews/Gwendlyn_Di_Corci.md`: comprehensive October 19 authored ChatGPT **KEEP**, 100/94 and 35 lands, many A–R finite rule/board-state traces; it separately proposed testing `+Aphetto Alchemist` with Illusionist's Bracers and several possible cuts. No measured wins, no swap approved.
2. `data/grixis/m6/grokbot_pass_c_advisory/Gwendlyn_Di_Corci.md`: GrokBot advisory **POSSIBLE UPGRADE `+Megrim/-Dream Salvage`**, no actual change; author stated no prior deep-review content exposure, while GrokBot's own history disqualified strict technical independence.
3. `data/grixis/m6/two_model_reconciliation/progress.json`, tracker index21 `KEEP`, evidence PR [#349](https://github.com/corymstover/GrokBotMTGCompanion/pull/349): explicitly **REJECT** GrokBot's exact `+Megrim/-Dream Salvage`, because Dream Salvage is a one-hybrid-mana instant drawing *each card one chosen opponent discarded that turn*; a wheel's full hand can make it a seven-card instant. Conditional `+Megrim/-Underworld Dreams` was left hypothetical, not authorized.
4. Current neutral Oracle: [Gwendlyn](https://scryfall.com/card/leg/228/gwendlyn-di-corci), [Aphetto Alchemist](https://scryfall.com/card/ons/64/aphetto-alchemist), [Illusionist's Bracers](https://scryfall.com/card/rvr/260/illusionists-bracers), plus exact owner locked source/override. Full latest 94-name legality sweep and actual randomized games were *not* run here.

## Agreements and materially distinct challenges

| Question | Sealed JLK Stage A | Existing review / reconciliation | Controlled disposition |
|---|---|---|---|
| Owner source; color and count | Exact raw source rehashed; 100 copies, 94 names, 35 lands; UBBR | All three exact SHA and count agree | **AGREEMENT**, no source conflict; note raw owner TXT has no terminal newline |
| Commander | On-your-turn tapped random discard; needs legal tap and opponent hand | All recognize own-turn rule and copied activations | **AGREEMENT**, correct restrictions |
| Graveyard / wheel hazards | Dauthi blocks Tergrid and grave-entry Ascension payoff; Chains/Notion complex | Authored independently identified same and Timetwister not discard | **AGREEMENT**; maintain explicit zone and draw replacement gates |
| First-look challenger | `+Rings of Brighthearth/-Mind Twist` NEEDS TESTING, alternate -Stone | Authored deep review KEEP; GrokBot proposed different payoff; reconciled KEEP | **NEW DISAGREEMENT**: Ring native ability copies but mana/per-opponent hand and redundant engine make no clear net gain |
| GrokBot challenger | Not read in Stage A | `+Megrim/-Dream Salvage` | **REJECT EXACT** pending new evidence. One-mana burst draw is much less replaceable than a redundant damage punishment at 3MV |
| Highest-risk omitted combo | Stage A did not propose Aphetto | Deep review found `Aphetto Alchemist+Illusionist's Bracers` self-untap route | **REAL NEW MECHANICAL PRIORITY**: validate effect/target/timing then compare meaningful cuts, not treat old author KEEP as conclusive |

## Specific interaction verified after Stage A seal

**Aphetto Alchemist `{1}{U}`** has `{T}: Untap target artifact or creature`. **Illusionist's Bracers** on the Alchemist copy its **nonmana activated** ability; we may change the copy's target. With a *ready* Alchemist, Gwendlyn and Bracers already equipped to Alchemist:

1. Activate Gwendlyn, target opponent with cards; Gwendlyn becomes tapped. That discard ability is on the stack, but Alchemist untapping Gwendlyn does not cancel it.
2. Activate Alchemist tapping it, targeting Gwendlyn. Bracers triggers and creates a copy. Change the **copy's target to Alchemist itself**.
3. The copied ability resolves first, untapping Alchemist. The original then resolves, untapping Gwendlyn. Both creatures are untapped (unless opponents changed the board in response).
4. Gwendlyn can activate again during our own turn and the sequence repeats without extra mana once set up. This is a **repeatable activation engine**, not an infinite discard win: finite available target hands, single-card random discard per tap, removal/counterplay, protection/timing and end-of-turn restriction constrain useful throughput. It yields zero additional discard from empty opponent hands. If Alchemist has summoning sickness and no haste/pseudo-haste, it cannot start tapping this turn; equip only at sorcery speed, costs real `{3}`, and a single instant removal can shut the ongoing line off.

**Potential exact test alternatives:** `+Aphetto Alchemist/-Magewright's Stone` trades a reliable colorless `{1},{T}` single untap and immediate noncreature operation for a summoning-sick, fragile blue creature with dramatic ceiling *only when Bracers is attached*. `+Aphetto/-Notion Thief` sacrifices near-asymmetric wheel draw denial and protection to power the native discard loop; likely not a prudent default. `+Aphetto/-Geth's Grimoire` loses card flow from multiple opponents' discards, and the commander engine easily starves on empty hands. The sealed first look's Ring versus Mind Twist remains an alternate **limited** test but is less promising than the fully source-checked Aphetto/Bracers mechanical synergy; preserve Stage A history unchanged.

**The owner approval and prior review may already have contemplated Alchemist**, but one old rejection referencing summoning sickness does not establish that the Bracers self-untap use was measured. Conversely, the authored deep review's discovery and A–R traces are not verified multiplayer performance; this reviewer does not claim independent discovery of it during Stage A.

## Opportunity-cost / opponent-response matrix (finite analytical traces, no win rates)

| Fixed matchup state | Approved untouched 100 | Hypothetical challenger and actual resource cost | Reason confidence is bounded |
|---|---|---|---|
| Gwendlyn + Bracers equipped and ready; Stone available; opponent hands [4,3,2] | Each Gwendlyn tap yields original+copy random discards: two per tap while hands remain. Stone `{1},{T}` allows **one** new commander tap this turn for up to four discarded cards across original/copy, assuming legal targets. | Aphetto replacing Stone has Bracers on **Alchemist** instead of Gwendlyn: each completed self-untap loop frees one new Gwendlyn tap for one discard; can remove all nine cards across nine successful loops at no extra mana after setup if unopposed. | Requires both bodies, equipment move and ready Alchemist. Strong native upside, worse setup and removal exposure; existing combo already disrupts multiple cards. |
| Opponent control with instant removal before Alchemist ability | Commander Bracers+Stone may lose Gwendlyn if kill lands before first tap, but counters may protect it; Stone not creature | Alchemist can be removed, so any already-on-stack untap abilities resolve if legal while next loops stop; protect with actual hand/counter resources | One compact loop description doesn't establish how many turns it stays alive in a pod |
| Turn-four UBBR unreliable; commander countered | Mind Twist can still discard X at random with just B and generic mana if present; Dream Salvage can draw after wheels, wheel engines work uncommanded | Rings needs surviving commander and `{2}` per copy after 3MV cast; Aphetto loop does **nothing** for hand denial without Gwendlyn | Commander-dependency is a real ceiling; don't optimize only an assembled board |
| Opponent hands already zero after wheel/Notion | Waste Not/Megrim/Caress may not trigger on further empty-hand activations, but some Empty-Hand Tinybones payoff persists | Rings/Aphetto repeat an ability whose effect has **no discarded card**, zero new triggers | Prior GrokBot assertion of unconditional Megrim damage is false for zero-card hands; another draw-refill strategy may be superior |
| Dauthi + Tergrid + Bloodchief active | Opponent discards nontoken permanent: discard triggers yes, but replacement exiles. Tergrid cannot retrieve from opponent grave; Bloodchief needs actual grave entry | Replacing these individually could remove anti-synergy but also lose opponent graveyard denial/theft; no exact alternative proven | Conditional coexistence is a sequencing decision, not a blanket rules blocker |
| Chains + Notion + own-turn wheel | Affected opponent's replacement effect choices and our replacement-modified card draws decide card totals | More copy/discard support cannot fix a miscounted replacement chain | Requires explicit per-player/per-card replacement order, not invented 7-card draw guarantee |

## Controlled Stage B decision

The prior reconciliation's **KEEP** of the exact `Megrim/Dream Salvage` swap is persuasive, and the sealed JLK `Rings/Mind Twist` hypothesis has no demonstrated advantage. The **Aphetto Alchemist + Bracers** engine is mechanically credible, strictly commander-first, and deserves a *higher-priority, narrow source-paid test* against `-Magewright's Stone` or another role-conscious cut. This is a potentially consequential native upgrade that the existing full list cannot reproduce at zero marginal mana, but a full pod can easily break its two-body-and-equipment setup. **Final disposition should remain `NEEDS TESTING`, canonical source untouched**, with no automatic increase of Phase B, I/J, M6 or owner-approval counters.
