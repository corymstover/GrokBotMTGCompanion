# Deck #45 — Obeka, Splitter of Seconds — M7 Rev1 owner candidate

Date: October 26, 2026 (America/Chicago). **REVIEW ONLY — NOT OWNER APPROVED.**

## Authority and exact bytes

- Canonical October 15 approved/locked list: `refinement/decklists/Obeka_Splitter_of_Seconds_Approved_2026-10-15.txt` in `corymstover/grixis-commander-encyclopediaGPT`, raw SHA-256 `c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63`.
- This M7 candidate: `data/grixis/m7/candidate_lists/Obeka__Splitter_of_Seconds_chatgpt_rev1.txt`, raw UTF-8 LF SHA-256 `f80d882944d5e39f3c6661da4dcdce3ec6eead577cd981dc54f7dc522be50859`.
- **Exactly 100 cards / 96 distinct names / 35 lands.** Repeated names only Island 3, Mountain 2, Swamp 2; no companion and no project exception. UBR identity unchanged; six new cards are red or colorless. Commander remains Obeka.
- The October 15 canonical list, all existing locks, state registry and approval tracker must stay unchanged. An explicit single Cory approval of this exact candidate SHA is necessary for a new canonical version.

## Commander-first result

The deck deliberately converts *real combat damage by Obeka to a player* into additional **postcombat upkeep-only beginning phases**, then uses the six existing Courts, Smaug, Journal, Thopter Spy Network, Replicating Ring, suspend/time effects and Time Sieve. Rev1 concentrates more slots on **getting the first hit earlier, increasing that hit's actual damage, and connecting in additional combats**, then converting the ensuing upkeeps into artifacts and wins. It remains **Power Bracket 4 — Optimized**, not an Oracle/Consultation or generic Breach shell.

## Six exact 1:1 changes, without a fixed-swap stop rule

| Cut | Addition | Stronger net role and acknowledged trade-off |
| --- | --- | --- |
| Rousing Refrain | Jeska, Thrice Reborn | Jeska's 0 triples Obeka's actual *player combat damage*, e.g. 2 → 6 extra upkeeps; Refrain cast by suspend in an upkeep produces red mana that normally empties before the next main phase. Jeska must be cast after a command-zone commander cast to survive entering with loyalty, and the target must connect. |
| Ring of Xathrid | Blackblade Reforged | Legendary equip {3} grants Obeka +1/+1 per land immediately, e.g. +5/+5 on five lands, before the **first** connection. The Ring can grow explosively after multiple upkeeps and regenerate, so the trade is pre-hit velocity against later growth/protection. |
| Jhoira of the Ghitu | Academy Manufactor | Smaug's Treasures and Tamiyo's Journal's Clues become one Clue, one Food and one Treasure per creation event. This produces Time Sieve fodder and same-name tokens for Mechanized Production. Jhoira's {2} activation and four-counter suspense is mana- and board-intensive, though playable in the prior shell. Manufactor relies on finding token engines and surviving removal. |
| Ring of Valkas | Rising of the Day | Gives teamwide haste and Obeka +1/+0 the moment she attacks, increasing the initial number of additional upkeeps without waiting for Ring counters. Ring's color-matched counters produce better long-run growth if it stays attached; we retain Ring of Evos Isle as upkeep-growing protection. |
| Paradox Haze | Karlach, Fury of Avernus | An attacked-first-combat Karlach produces a free additional combat and untaps attackers. If Obeka connects both times, there are two Obeka damage triggers and two batches of added upkeeps. Haze's single precombat upkeep each turn is safer if Obeka cannot attack; it does not repeat on every Obeka-created upkeep. Karlach is five mana and vulnerable to creature interaction. |
| Darksteel Reactor | Aggravated Assault | {3}{R}{R} each postcombat main phase can generate another combat/main sequence. Smaug plus Obeka dealing five or more player combat damage can make five Treasures from the ensuing upkeeps to fuel another activation; repeatability requires connection, a surviving board and real mana. Retained Sword of Feast and Famine offers a second combat-mana engine. Reactor is indestructible and commander-native, but needs twenty separate upkeep counter placements; cutting it reduces win-condition diversification in favor of active combat lines. |

This was not a five-card quota. Each candidate was assessed against all 99 existing noncommander copies and the Oct15 hybrid M7 source, then against newer Pass C questions.

## Comparative non-inclusions after challenge

- **Protection Racket:** scales during every extra upkeep and can exert life/card pressure, but opponents choose the payment and even zero-cost land reveals can be denied for zero life; existing Courts, Super Intelligence, Arena, Prophet and Journal provide more predictable advantages. No replacement with higher commander-specific net return was identified.
- **Endless Evil / Followed Footsteps:** repeated nonlegend creature copies are attractive on Smaug? Smaug is legendary, so token copies of it would not survive state-based actions without legend-rule circumvention. Better nonlegend targets (Bonehoard Dracosaur, Creeping Bloodsucker, Dragonmaster Outcast, Twilight Prophet) require a second creature and a surviving Aura; keeping the deck's existing flexible six-mana Extravagant Replication remains defensible.
- **Unleash Fury / Temur Battle Rage:** efficient damage amplification/double strike, but one-use pump is timing-vulnerable and adds a weaker long-game engine than Jeska/Blackblade/Assault in this exact 100. Embercleave and Hatred already cover combat surprise/double strike.
- **Rogue's Passage over Swamp:** preserve the Pass C reject; four mana plus the land tap for evasion and one fewer black source are poor versus Aqueous Form, Brotherhood Regalia, Thassa, Shizo and Silent Arbiter+menace.
- **Generic Oracle/Consultation/Breach:** inappropriate homogenization and a different deck plan.

## Rules and bounded mechanical cases

1. Wizards' Outlaws of Thunder Junction release notes establish that each extra upkeep is in a new beginning phase after combat without untap or draw. If Obeka is blocked/prevented/removed before dealing **player** combat damage, no trigger occurs.
2. Jeska's **0** ability produces a damage replacement, not an extra trigger. With 2-power Obeka and unprevented player damage, six actual combat damage creates six extra upkeeps. With Mjölnir doubling and Jeska tripling 4 power and two separate additional-trigger effects (Wizard's Staff + Ogre/Warlock Roaming Throne), one successful damage event can produce `4 × 2 × 3 × 3 = 72` extra upkeeps; these independent effects should not be assumed to require or achieve any uncontested board state. Check decking, life loss and opponents' priority windows.
3. Karlach must see an attack in the first combat phase, then untaps creatures and adds another combat. The extra phase and Obeka-added upkeeps obey the game’s most-recently-added-phase ordering; neither provides another untap/draw step by itself.
4. Academy Manufactor changes each individual Clue/Treasure creation event into three different token types, **not three copies of each type**. Smaug plus Journal give six total artifacts per upkeep with Manufactor. Time Sieve consumes five expendable artifacts and **taps**; only a new turn or another untap lets it activate again.
5. Aggravated Assault is activated **as a sorcery** for {3}{R}{R}. Its combo with Smaug assumes at least five controller upkeeps' worth of usable Treasures (or equivalent sources) and repeated combat hits, not a guaranteed infinite loop from an empty board. Sword of Feast and Famine lands must actually untap enough usable mana if that is the chosen payment line.
6. Rings trigger at the beginning of the *controller's* upkeeps and grow Obeka for later hits, not the hit that caused those extra upkeeps. Replacing two of three does forfeit some potential post-hit scaling in favor of increasing initial contact and extra-combat frequency.
7. Rousing Refrain's red mana is generated while the suspended spell resolves, often during an upkeep. Mana normally empties at the end of that step. Obeka-created upkeep steps do not allow that mana to be saved to a later main phase.

## Verification status and limits

- Exact-file script at `data/grixis/m7/obeka_splitter_rev1/verify_obeka_splitter_rev1.py` (local working filename `obeka_splitter_m7_rev1_verify.py`) passed: raw SHA; weighted 100; 96 names; 35 lands; basic-only repeats; six exact additions/cuts; bounded conditional damage and artifact-count cases. Run in the engineering repository with `python3 data/grixis/m7/obeka_splitter_rev1/verify_obeka_splitter_rev1.py`.
- Existing October 15 baseline had a full 99-slot and official Commander legality review. All 90 retained distinct names are unchanged from that officially audited list. All six new additions are historical printed colorless or mono-red Commander cards; checked against October 2026 WotC Commander banned list and card-specific Oracle/Scryfall sources. No banned or off-color addition found.
- No new 100/100 live external Oracle batch, performance simulation, tournament win rate, or full cross-deck M6 transfer-certification pass is claimed by these checks. Inherited historical gates and newer checks are distinguished.
- Owner action: approve the **complete exact 100** with raw SHA `f80d882944d5e39f3c6661da4dcdce3ec6eead577cd981dc54f7dc522be50859` once. Only then versioned canonical locking may happen.

## Sources

- WotC Outlaws of Thunder Junction release notes: https://magic.wizards.com/en/news/feature/outlaws-of-thunder-junction-release-notes
- WotC banned/restricted list: https://magic.wizards.com/en/banned-restricted-list
- Scryfall Jeska: https://scryfall.com/card/cmr/186/jeska-thrice-reborn
- Scryfall Blackblade: https://scryfall.com/card/dom/211/blackblade-reforged
- Scryfall Academy Manufactor: https://scryfall.com/card/mh2/219/academy-manufactor
- Scryfall Rising of the Day: https://scryfall.com/card/ltr/145/rising-of-the-day
- Scryfall Karlach: https://scryfall.com/card/clb/186/karlach-fury-of-avernus
- Scryfall Aggravated Assault: https://scryfall.com/card/wot/96/aggravated-assault
