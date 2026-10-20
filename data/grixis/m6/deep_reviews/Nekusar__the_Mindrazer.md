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
| 26 | 1 | Exotic Orchard | Multiplayer opponent-land conditional fixer; opponents need corresponding colors to supply UBR. |
| 27 | 1 | Fate Unraveler | Independent 1 damage for every opponent draw; triggers Ghyrson and Krang without Nekusar. |
| 28 | 1 | Fevered Visions | 2UR end-step each draws plus conditional 2 damage; feeds opposing answers and delays payoff. |
| 29 | 1 | Fierce Guardianship | Free noncreature counter only while Nekusar controlled, key to protect five-mana setup. |
| 30 | 1 | Flooded Strand | Pay1 life, fetch Island-typed original duals/shocks/triome, fixes colors but not a Plains-free arbitrary target. |
| 31 | 1 | Force of Negation | Pitching blue free only on OPPONENT turn, never assume free during your wheel turn. |
| 32 | 1 | Force of Will | Blue pitch and 1 life to counter any spell, including creatures, enables protected wheel turn. |
| 33 | 1 | Geier Reach Sanitarium | Colorless utility land: 2 and tap everyone draws then discards, independent Nekusar/Waste Not engine. |
| 34 | 1 | Ghyrson Starn, Kelermorph | Adds 2 damage only after another your source does exactly 1; Phyrexian Tyranny's life loss doesn't qualify. |
| 35 | 1 | Grim Monolith | Taps CCC, four to untap; fast generic but not UBR colored; Power Artifact optional unapproved challenger. |
| 36 | 1 | Harmonic Prodigy | Two-mana Wizard (Nekusar is another Wizard) adds one to both Nekusar triggered abilities. |
| 37 | 2 | Island | 2 basics, fetchable and immune to nonbasic hate; low count forces fetch-target discipline. |
| 38 | 1 | Jace's Archivist | 1UU tap wheel; summoning sickness, removal and no immediate activation without haste. |
| 39 | 1 | Jeska's Will | 2R adds red equal opponent hand; requires >=6 in hand for recurring Breach/Will/Wheel cost cycle. |
| 40 | 1 | Kami of the Crescent Moon | UU adds draw each draw step, inexpensive but symmetrical until a Nekusar/punisher resolves. |
| 41 | 1 | Kederekt Parasite | B one-damage opponent draw punisher requiring a controlled red permanent, easy to remove. |
| 42 | 1 | Krang, the All-Powerful | Adds draw-CAUSED triggers only, not Nekusar's beginning draw-step; also doubles your Tyranny/Spiteful risk. |
| 43 | 1 | Liliana's Caress | Opponent DISCARD creates two LIFE LOSS, not damage, so not Ghyrson and not shuffle wheels. |
| 44 | 1 | Luxury Suite | BR multiplayer untapped dual in 4-player; neither typed nor always untapped heads-up. |
| 45 | 1 | Magus of the Wheel | 3-mana 3/3 wheel-on-activated tap/sac with additional mana; vulnerable and summoning sick. |
| 46 | 1 | Mana Confluence | Untapped UBR at 1 life each tap, improves Niv/commander cast but life cost compounds. |
| 47 | 1 | Mana Drain | UU hard counter generates COLORLESS next main; doesn't fix Niv's triple U/R requirements. |
| 48 | 1 | Mana Vault | 1-mana artifact CCC burst; upkeep damage/untap costs, not fully repeatable Mana Crypt analogue. |
| 49 | 1 | Marsh Flats | Fetches Swamp-typed UBR lands, not arbitrary colored land; improves black source density. |
| 50 | 1 | Mikokoro, Center of the Sea | Colorless land, 2 tap everyone draws at instant speed, Nekusar engine at opportunity cost. |
| 51 | 1 | Misty Rainforest | Pay1 life fetch Island-typed blue sources or typed Xander's Lounge; nine-fetchtarget package. |
| 52 | 1 | Molten Psyche | 1RR shuffles then redraws, NO discard triggers; metalcraft >=3 artifacts damages for all cards drawn this turn. |
| 53 | 1 | Morphic Pool | UB multiplayer untapped fixer, nonfetchable and may enter tapped in duel. |
| 54 | 2 | Mountain | 2 fetchable basic red sources; supports wheels, only two total versus several RR spells. |
| 55 | 1 | Mystical Tutor | U instant puts instant/sorcery on library TOP; fetched wheel can be disrupted or lost to opponent wheel. |
| 56 | 1 | Niv-Mizzet, Parun | UUURRR demanding 6-mana 5/5; Curiosity creates optional draw/ping loop, not guaranteed without protection. |
| 57 | 1 | Orcish Bowmasters | 1B flash, pings on ETB and each opposing draw besides first draw-step card; Ghyrson boosts exact 1. |
| 58 | 1 | Otawara, Soaring City | U untapped channel removal spell-adjacent but ability, costs 3U reduced by legendaries. |
| 59 | 1 | Peer into the Abyss | 4BBB target one player loses half life and draws half library (round up); lethal with enough draw-punish. |
| 60 | 1 | Phyrexian Tyranny | 1UB makes ALL draws trigger pay2 or lose2; Krang doubles OWN life-loss trigger count, dangerous to wheel. |
| 61 | 1 | Polluted Delta | Pay1 fetch Island/Swamp typed UBR duals; near-optimal fixing, life cost matters. |
| 62 | 1 | Razorkin Needlehead | Damage on opponent draw from independent body; increases punisher density but dies to removal. |
| 63 | 1 | Reforge the Soul | 3RR normal wheel seven or 1R miracle, discard/draw true triggers and may refill opponent defenses. |
| 64 | 1 | Reliquary Tower | Colorless no maximum hand size; useful with Sphinx, colorless competes with tight commander/Niv pips. |
| 65 | 1 | Rhystic Study | 2U generic value and interactive tax; lets pilot draw counter/wheel but opponents may pay. |
| 66 | 1 | Scalding Tarn | Pay1 fetch Island/Mountain typed original/shock/triome; efficient U/R choice. |
| 67 | 1 | Scrawling Crawler | Artifact creature on-plan draw punishment; double exposed to creature and artifact sweeps. |
| 68 | 1 | Sheoldred, the Apocalypse | Own draw gains 2 life, opponent draw loses 2 life; life LOSS is not Ghyrson damage. |
| 69 | 1 | Sol Ring | Turn-one CC acceleration, doesn't pay U/B/R, tempo high but color sequencing critical. |
| 70 | 1 | Spiteful Visions | Each player draws extra and takes 1 DAMAGE per draw, YOU included; Krang creates extra own pings. |
| 71 | 1 | Steam Vents | Fetchable UR shock, untapped costs 2 life; valuable for Niv UUU/RRR demands. |
| 72 | 1 | Stormfist Crusader | BR 2/2 menace, each upkeep everyone draws and loses 1 life; may feed enemies before Nekusar online. |
| 73 | 2 | Swamp | 2 basics, supply BBB Underworld Dreams/Peer and recovery vs nonbasic hate. |
| 74 | 1 | Swan Song | U counters instant/enchantment/sorcery only, provides Bird; cannot stop Oracle or other creatures. |
| 75 | 1 | Talisman of Creativity | 2-mana UR/C rock, colored taps cost 1 life; essential to Niv/commander colored requirements. |
| 76 | 1 | Talisman of Dominance | 2-mana UB/C rock, colored taps cause 1 life; smoother Nekusar and BBB/UUU. |
| 77 | 1 | Talisman of Indulgence | 2-mana BR/C rock, colored taps cause 1 life; supports Wheel RR, Peer BBB. |
| 78 | 1 | Teferi's Puzzle Box | 4-mana at draw step bottoms hand then draws that many, not DISCARD; orders after extra-draw triggers for maximal impact. |
| 79 | 1 | Toxic Deluge | 2B plus X life, all creatures -X/-X including Nekusar; answers attackers but sacrifices life budget. |
| 80 | 1 | Training Center | UR multiplayer untapped land, typed? no, good Niv colored without pain. |
| 81 | 1 | Underground Sea | Fetchable UB original dual enters untapped, ideal for Nekusar and underworld dreams. |
| 82 | 1 | Underworld Breach | 1R all nonland GY cards escape for printed cost + exile3 other grave cards; with Wheel/Jeska hand/grave fuel. |
| 83 | 1 | Underworld Dreams | BBB each opponent draw deals 1 damage; Ghyrson and Krang synergy but severe black source constraint. |
| 84 | 1 | Vampiric Tutor | B instant unrestricted tutor to top for 2 life; plan draw timing and Wheel shuffle disruption. |
| 85 | 1 | Verdant Catacombs | Pay1 fetch Swamp-type original/shock/triome, improves black without Forest in deck. |
| 86 | 1 | Volcanic Island | Fetchable UR original dual enters untapped, exceptional Niv triple-color reliability. |
| 87 | 1 | Waste Not | 1B opponent DISCARD yields BB/Zombie/card by type; shuffles do not trigger, can replenish wheel mana. |
| 88 | 1 | Watery Grave | Fetchable UB shock entering untapped costs 2 life; underworld dreams/Blue counter coverage. |
| 89 | 1 | Wheel and Deal | 3U instant OPPONENTS discard and draw7, you draw1; asymmetric Nekusar finisher. |
| 90 | 1 | Wheel of Fortune | 2R discard all hands then draw7, core wheel plus Breach fuel and own self-damage risk. |
| 91 | 1 | Wheel of Misfortune | 2R choice wheel that some opponents can avoid with 0; not a guaranteed symmetric seven. |
| 92 | 1 | Whispering Madness | 2UB each discard then draw to largest discarded, cipher can recast on damage; expensive/situational. |
| 93 | 1 | Windfall | 2U discard hands then draw max discarded among players; powerful under big opposing hands. |
| 94 | 1 | Winds of Change | R SHUFFLE hands into libraries and redraw same sizes, no discard, cheapest mass damage burst. |
| 95 | 1 | Wizard's Staff | 1U Equipment equip Wizard 1, adds one of both Nekusar triggers (step and damage); best commander-specific slot. |
| 96 | 1 | Wooded Foothills | Pay1 fetch Mountain typed shock/original/triome, not any color as typed fetch targets require Mountain. |
| 97 | 1 | Xander's Lounge | UBR typed triome enters tapped, fetchable, can cycle late instead of land. |

**Role-reconciliation checksum:** 97 consecutive ledger rows, quantity sum 100 (including commander), exactly 35 land cards; no nonbasic duplication. Every library slot evaluated for card draw generation, punisher relevance, protection, combo, color access, self-damage or opportunity cost. The role ledger identifies vulnerability rather than treating the Oct15 KEEP votes as independent evidence.

