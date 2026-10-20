# M6 comprehensive single-deck authored review #40 — Nekusar, the Mindrazer

**Deck ID:** `Nekusar__the_Mindrazer`; tracker index 39 / #40 of 62. **Author:** ChatGPT (not independent Pass C). **Date:** 2026-10-19 America/Chicago.

**Canonical state:** `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json#decks.Nekusar__the_Mindrazer`: **APPROVED / LOCKED**, SHA-256 `bc36908fb2f848dfd69407a317d7da5811532dba7e3b4e7be89a2905d901c6f1`. Approved TXT `refinement/decklists/Nekusar_the_Mindrazer_Approved_2026-10-15.txt` blob `8ee94e3e7d34d6ff7aa9bd28672a862756d002d9`. Engineering logical SHA `lh1:0b5079ca21d51e48d0d52464a7704059c3b4b4dd3685259af62b5b592222a886`, no source identity discrepancy.

## Source and test receipts

Read live `AGENTS.md`, the M6 comprehensive single-deck standard, depth tracker, registry and M6/M7 subtracker. Current tracker before review **39/62** complete, Nekusar first pending. Canonical Oct15 approved TXT, verification, whole-list audit, decision and approval override; engineering `grixis/blueprints/nekusar-the-mindrazer.md`, `grixis/interactions/nekusar-the-mindrazer.md` (nine cases, Scryfall bulk Oct16, rulings Oct15, CR Sep25), 69 hypotheses in `data/grixis/m6/review_packets/nekusar-the-mindrazer.json`, static mana `data/grixis/mana_base/nekusar-the-mindrazer.json`, M5 EDHREC 280 vectors (Oct17). External current [Wizards B&R Oct12](https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026) shows no tabletop Commander change; current [Commander Spellbook Breach/Will/Wheel](https://commanderspellbook.com/combo/1368-1878-2706/) confirms exact loop prerequisites. No Oct19 all-100 fresh Scryfall API sweep or new effect-aware simulation is claimed.

**Independent TXT arithmetic:** 100 physical cards, 97 distinct names, one commander and 99 library slots. Only Island x2, Mountain x2 and Swamp x2 repeat (basics). 35 lands, UBR, no project exception, Oct15 Commander legality checkpoint passed. The approved list includes 17 authorized swaps from a different 100-card FINAL baseline; this review evaluates the APPROVED list only.

## Commander identity and natural ceiling

Nekusar is {2}{U}{B}{R}, 2/4 Zombie Wizard. Beginning of EVERY player's draw step gives that player an EXTRA card; whenever an OPPONENT draws, Nekusar deals exactly 1 damage to that opponent. His draw trigger is separate from his damage trigger. Real draws matter; hand shuffles that do not draw are not damage. Strategy: wheels into opponent-draw punishment, stack Wizard/draw-trigger multipliers and keep protection for lethal wheels. Natural ceiling **Bracket 4 Optimized**: five-mana commander, high-cost payoffs and opponents refilled by wheels prevent claims of generic cEDH consistency. Win through wheels/Peer, Breach re-casting wheel with Jeska's Will, or optional Niv/Curiosity; no homogenizing into Oracle turbo.

Identity protection: prioritize true opponent draws, draw punishers, Nekusar Wizard triggers, exact-one-damage Ghyrson, cheap shields and self-life safety. A known internal hazard: Krang doubles your own Spiteful Visions/Phyrexian Tyranny draw-trigger penalties; careless wheels can kill their caster. `Ghyrson` needs exactly **one DAMAGE**, not loss of life; Solphim's former damage doubling conflicted with it.

