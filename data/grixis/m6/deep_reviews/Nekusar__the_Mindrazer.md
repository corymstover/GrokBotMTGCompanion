# M6 comprehensive single-deck authored review #40 — Nekusar, the Mindrazer

**Deck ID:** `Nekusar__the_Mindrazer`; tracker index 39 / #40 of 62. **Author:** ChatGPT (not independent Pass C). **Date:** 2026-10-19 America/Chicago.

**Canonical state:** `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json#decks.Nekusar__the_Mindrazer`: **APPROVED / LOCKED**, SHA-256 `bc36908fb2f848dfd69407a317d7da5811532dba7e3b4e7be89a2905d901c6f1`. Approved TXT `refinement/decklists/Nekusar_the_Mindrazer_Approved_2026-10-15.txt` blob `8ee94e3e7d34d6ff7aa9bd28672a862756d002d9`. Engineering logical SHA `lh1:0b5079ca21d51e48d0d52464a7704059c3b4b4dd3685259af62b5b592222a886`, no source identity discrepancy.

## Source and test receipts

Read live `AGENTS.md`, the M6 comprehensive single-deck standard, depth tracker, registry and M6/M7 subtracker. Current tracker before review **39/62** complete, Nekusar first pending. Canonical Oct15 approved TXT, verification, whole-list audit, decision and approval override; engineering `grixis/blueprints/nekusar-the-mindrazer.md`, `grixis/interactions/nekusar-the-mindrazer.md` (nine cases, Scryfall bulk Oct16, rulings Oct15, CR Sep25), 69 hypotheses in `data/grixis/m6/review_packets/nekusar-the-mindrazer.json`, static mana `data/grixis/mana_base/nekusar-the-mindrazer.json`, M5 EDHREC 280 vectors (Oct17). External current [Wizards B&R Oct12](https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026) shows no tabletop Commander change; current [Commander Spellbook Breach/Will/Wheel](https://commanderspellbook.com/combo/1368-1878-2706/) confirms exact loop prerequisites. No Oct19 all-100 fresh Scryfall API sweep or new effect-aware simulation is claimed.

**Independent TXT arithmetic:** 100 physical cards, 97 distinct names, one commander and 99 library slots. Only Island x2, Mountain x2 and Swamp x2 repeat (basics). 35 lands, UBR, no project exception, Oct15 Commander legality checkpoint passed. The approved list includes 17 authorized swaps from a different 100-card FINAL baseline; this review evaluates the APPROVED list only.

## Commander identity and natural ceiling

Nekusar is {2}{U}{B}{R}, 2/4 Zombie Wizard. Beginning of EVERY player's draw step gives that player an EXTRA card; whenever an OPPONENT draws, Nekusar deals exactly 1 damage to that opponent. His draw trigger is separate from his damage trigger. Real draws matter; hand shuffles that do not draw are not damage. Strategy: wheels into opponent-draw punishment, stack Wizard/draw-trigger multipliers and keep protection for lethal wheels. Natural ceiling **Bracket 4 Optimized**: five-mana commander, high-cost payoffs and opponents refilled by wheels prevent claims of generic cEDH consistency. Win through wheels/Peer, Breach re-casting wheel with Jeska's Will, or optional Niv/Curiosity; no homogenizing into Oracle turbo.

Identity protection: prioritize true opponent draws, draw punishers, Nekusar Wizard triggers, exact-one-damage Ghyrson, cheap shields and self-life safety. A known internal hazard: Krang doubles your own Spiteful Visions/Phyrexian Tyranny draw-trigger penalties; careless wheels can kill their caster. `Ghyrson` needs exactly **one DAMAGE**, not loss of life; Solphim's former damage doubling conflicted with it.

## Whole-deck tactical role ledger — exact approved TXT order

Each row reflects one distinct approved card, with quantity; the ledger covers **97 names / 100 physical cards** including six basics in triples of two, and continues below without a second list. Source notes are canonical Oct15 audit context; tactical caveats are this author's review and not a renewed approval.

| Approved row | Qty | Exact card name | Commander-fit role, risk and source rationale |
|---:|---:|---|---|
| 1 | 1 | Nekusar, the Mindrazer | Commander; 5-mana Wizard extra-draw and exactly-one opponent damage trigger; source: Approved previously added or commander. |
| 2 | 1 | An Offer You Can't Refuse | one-mana noncreature counter protects expensive wheel; opponent gets two Treasures; source: efficient interaction/protection is necessary to resolve and preserve a five-mana commander and its wheel turns. |
| 3 | 1 | Ancient Tomb | fast colorless acceleration trades two life, fails UBR pips alone; source: efficient acceleration/fixing materially improves Nekusar deployment and multi-spell wheel turns. |
| 4 | 1 | Anvil of Bogardan | draw THEN discard triggers Nekusar plus Waste Not/Caress; source: rate/reciprocity is strong enough to sustain the draw-punishment engine without occupying a weaker slow group-hug slot. |
| 5 | 1 | Arcane Denial | 1U counter and delayed opponent draws can add Nekusar damage; source: efficient interaction/protection is necessary to resolve and preserve a five-mana commander and its wheel turns. |
| 6 | 1 | Arcane Signet | two-mana UBR fixing, important early colored development; source: efficient acceleration/fixing materially improves Nekusar deployment and multi-spell wheel turns. |
| 7 | 1 | Arid Mesa | land; fetchable/color/tapped constraint; source: Approved previously added or commander. |
| 8 | 1 | Badlands | land; fetchable/color/tapped constraint; source: current land contributes efficient color access or unique utility and survives the optimized mana-base comparison. |
| 9 | 1 | Blood Crypt | land; fetchable/color/tapped constraint; source: current land contributes efficient color access or unique utility and survives the optimized mana-base comparison. |
| 10 | 1 | Bloodchief Ascension | requires three quest counters before drains from opponent graveyard cards; source: high-impact engine/combo utility remains materially aligned with wheels, draw triggers, or recovery. |
| 11 | 1 | Bloodstained Mire | land; fetchable/color/tapped constraint; source: current land contributes efficient color access or unique utility and survives the optimized mana-base comparison. |
| 12 | 1 | Bojuka Bog | tapped B graveyard exile, anti-Breach defense for land tempo; source: current land contributes efficient color access or unique utility and survives the optimized mana-base comparison. |
| 13 | 1 | Burning Inquiry | R three actual draws then RANDOM discards, can harm own hand; source: efficient burst/repeatable wheel effect directly converts cards in opponents' hands into Nekusar draw triggers. |
| 14 | 1 | Chaos Warp | R-based permanent catch-all; opponent may flip dangerous permanent; source: efficient interaction/protection is necessary to resolve and preserve a five-mana commander and its wheel turns. |
| 15 | 1 | Chrome Mox | zero-mana colored accel needs imprint and costs a card; source: efficient acceleration/fixing materially improves Nekusar deployment and multi-spell wheel turns. |
| 16 | 1 | City of Brass | land; fetchable/color/tapped constraint; source: Approved previously added or commander. |
| 17 | 1 | Command Tower | land; fetchable/color/tapped constraint; source: current land contributes efficient color access or unique utility and survives the optimized mana-base comparison. |
| 18 | 1 | Consecrated Sphinx | optional draws off every opponent draw, six mana and self-damage risk; source: rate/reciprocity is strong enough to sustain the draw-punishment engine without occupying a weaker slow group-hug slot. |
| 19 | 1 | Curiosity | on Nekusar generates own value draws; on Niv loops optional pings; source: Approved previously added or commander. |
| 20 | 1 | Cyclonic Rift | 1U targeted bounce or 6U one-sided overloaded board reset; source: efficient interaction/protection is necessary to resolve and preserve a five-mana commander and its wheel turns. |
| 21 | 1 | Dark Deal | 2B each discards full hand then draws one fewer; feeds BOTH payoff kinds; source: efficient burst/repeatable wheel effect directly converts cards in opponents' hands into Nekusar draw triggers. |
| 22 | 1 | Dark Ritual | B into BBB but does not fix U and R for commander; source: efficient acceleration/fixing materially improves Nekusar deployment and multi-spell wheel turns. |
| 23 | 1 | Deflecting Swat | free targeted redirect only with commander; cannot protect vs untargeted effect; source: efficient interaction/protection is necessary to resolve and preserve a five-mana commander and its wheel turns. |
| 24 | 1 | Demonic Tutor | 2 mana finds lethal wheel, punisher or counter; precision matters; source: compact tutor for wheel, protection, trigger multiplier, or finisher at the deck's optimized ceiling. |
| 25 | 1 | Echo of Eons | shuffles HAND and GRAVEYARD, redraws 7; does not discard; source: efficient burst/repeatable wheel effect directly converts cards in opponents' hands into Nekusar draw triggers. |
