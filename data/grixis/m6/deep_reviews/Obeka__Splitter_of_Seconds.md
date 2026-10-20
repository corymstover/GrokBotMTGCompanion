# M6 Comprehensive Single-Deck Review #45 — Obeka, Splitter of Seconds

**Tracker deck ID:** `Obeka__Splitter_of_Seconds`, tracker index44 (#45/62). **Review author:** ChatGPT — not independent GrokBot Pass C. **Dated:** 2026-10-20. **Disposition:** Keep the 100 exact owner-approved cards unchanged. Conditional proposal only, no canonical swap.

## Source and test receipts

Recovered live engineering `corymstover/GrokBotMTGCompanion` active `chatgpt-cycle76-m6-refinement`; read `AGENTS.md`, `grixis/M6 Commander-First Single-Deck Review Standard.md`, tracker `data/grixis/m6/single_deck_depth_tracker.json` (44/62 before #45), `data/grixis/registry.json`, `data/grixis/milestone_m6_m7_subtracker.json`, `data/grixis/m6/review_packets/obeka-splitter-of-seconds.json`, `data/grixis/mana_base/obeka-splitter-of-seconds.json`, `grixis/interactions/obeka-splitter-of-seconds.md` (five source-verified cases). Canonical `corymstover/grixis-commander-encyclopediaGPT/main`: `state/current_deck_overrides.json#decks.Obeka__Splitter_of_Seconds`, [Oct15 approved TXT](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/decklists/Obeka_Splitter_of_Seconds_Approved_2026-10-15.txt) Git blob `3744ef1e8d127a6262abbfd8e064c475b8ee0654`, approval record, whole-list audit, candidate decisions and approval-ready verification.

**CANONICAL LOCK:** Oct15 2026 APPROVED/LOCKED SHA-256 **`c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63`**, engineering logical `lh1:95dc0a60266129426fa099fdb3188f143829ca9f23d5d65357f1a02a7cbf2912`; no identity discrepancy/project exception, official Commander UBR Oct16 Oracle snapshot compliant. Source explicitly corrected a *stale, wrong* prior reported hash `83062ff2dbc955c628f9a6df460cf72dd5d450b6685bc4b53f63894bc8c321fb` through GitHub Actions, with NO card membership changes; that obsolete hash must never supersede the source.

**Our independent exact TXT weighted arithmetic**: 100 cards / 96 distinct names / 35 lands / 99 library cards. ONLY basic repeats Island x3, Mountain x2 and Swamp x2, singleton PASS. Approved Oct15 source changed 19 physical slots from October12 historical FINAL (9 strategic, 10 lands), now fully incorporated. Do NOT reapply them.

**External Oracle evidence:** Wizards [Outlaws of Thunder Junction notes, Obeka](https://media.wizards.com/2024/downloads/OTJ_Release_Notes_nwYBwey2D91L/EN_MTGOTJ_ReleaseNotes_20240307.pdf), [Wizards The Hobbit notes, Wizard's Staff](https://magic.wizards.com/en/news/feature/the-hobbit-release-notes), [Wizards Paradox Haze Oracle ruling](https://media.wizards.com/2025/downloads/EOE_Release_Notes_R8Z03VaANE/EN_MTGEOE_ReleaseNotes_20250718.pdf), [Academy Manufactor Oracle](https://mtg.wtf/card/pmh2/219s/Academy-Manufactor), [Court of Vantress Oracle](https://media.wizards.com/2023/downloads/WOE_Release_Notes_9S5bvPQTjRwh/EN_MTGWOE_ReleaseNotes_20230518.pdf). Project-engineering Oct16 Scryfall Oracle bulk + Sep25 rules already checked five main interactions; no new full 100-card Oct20 live Scryfall API sweep was made.

**M5 screening:** 38 swap hypotheses, 2 model passes, 8 fails, 3 inconclusive and 25 undetected; P1 2/P3 36. Repeated false-cut targets Fellwar Stone, Ring of Valkas, Roaming Throne, Bonehoard Dracosaur, Deadly Rollick, Hatred, Paradox Haze. All 38 evaluated in relevant distinct families below, not as mandatory additions. Screening labels are effect-model results, not tournament/gameplay evidence.

## Commander identity and natural ceiling

Obeka is a {1}{U}{B}{R}, 2/5 menace legendary Ogre Warlock. On **actual combat damage to a player**, she produces an equal number of **added upkeep steps after the current combat phase**, implemented as extra beginning phases with **untap and draw omitted**; these are not extra whole turns. On a clean hit at power 2, two added upkeeps; a power 4 hit yields four. Damage prevention or blocking can reduce to zero; commander combat damage is not simply proportional to trigger duplication. Damage doubling from Mjölnir changes actual damage before Obeka's ability determines N; Roaming Throne and Wizard's Staff add triggers separately, so with both, **three** Obeka triggers per combat damage event, each independently creating N added upkeeps. Prowess and pump must apply *before* combat damage. Embercleave double strike can create distinct first-strike/normal damage events, if Obeka survives/gets through for both.

Each upkeep fires true `at beginning of upkeep` engines: monarch Courts; Super Intelligence; Tamiyo's Journal; Darksteel Reactor; Smaug; Phyrexian Arena; Ring +1/+1 counters; Twilight Prophet if City's Blessing; As Foretold/Replicating Ring counters; Clues/Treasure/Thopter production; time counters from suspended spells. **Important source nuance:** `Paradox Haze` adds exactly one extra upkeep after its enchanted player's **first** upkeep each turn — Obeka's additional upkeep steps later in that turn do not retrigger Haze. It gives strong autonomous value but only linear +1 per turn, unlike scalable Obeka combat engine.

**Target ceiling: Bracket 4 — Optimized** per owner source ranking and approved design, not demonstrated cEDH tournament consistency. The win pathway is Obeka contact + compounded upkeep output + Time Sieve/Mechanized Production/Reactor and drain/monarch clocks. Do not import generic Grixis Oracle/Breach as core. Distinct from previous Brute Chronologist end-the-turn commander, which has completely different timing.

## Full 100-card role audit

Each canonical source TXT line audited, quantity weighted; repeating basics indicated rather than silent deduplication.

| Original row | Qty | Approved card | Specific role, payoff and principal limitation |
|---:|---:|---|---|
| 1 | 1 | Obeka, Splitter of Seconds | COMMANDER {1}{U}{B}{R}, 2/5 menace; deals N combat damage to PLAYER -> N postcombat added upkeep-only beginning phases. |
| 2 | 1 | An Offer You Can't Refuse | U counter noncreature spell but opponent receives two Treasures, significant race cost. |
| 3 | 1 | Ancestral Vision | Suspended draw-three pays no mana after last time counter; each upkeep removes a counter; accelerates with Obeka. |
| 4 | 1 | Ancient Tomb | Land — Colorless CC and 2 damage to its controller, ramp generic component not UBR. |
| 5 | 1 | Aqueous Form | U Aura unblockable Obeka plus attack scry, critical contact reliability but weak to removal/shroud. |
| 6 | 1 | Arcane Signet | 2-mana UBR rock for four-mana commander and color-heavy protection. |
| 7 | 1 | Arena of Glory | Land — Untapped R / conditionally grants Obeka haste from mana used in her creature cast; haste helps first connection. |
| 8 | 1 | Arid Mesa | Land — 1-life fetch for typed UBR dual, shock, or triome; type-matching and tempo matter. |
| 9 | 1 | As Foretold | 2U upkeep time counters, allows casting spell each turn without paying cost if MV within counters; grows rapidly with extra upkeeps. |
| 10 | 1 | Badlands | Land — Untapped fetchable UBR dual/shock (shocks may cost two life); source of commander color pips. |
| 11 | 1 | Blood Crypt | Land — Untapped fetchable UBR dual/shock (shocks may cost two life); source of commander color pips. |
| 12 | 1 | Bloodstained Mire | Land — 1-life fetch for typed UBR dual, shock, or triome; type-matching and tempo matter. |
| 13 | 1 | Bonehoard Dracosaur | 5-mana creature with upkeep exile/treasure/card value, high output but 5-mana setup and creature vulnerability. |
| 14 | 1 | Brotherhood Regalia | Equipment evasion/protection enabling Obeka hits, setup/equip opportunity cost. |
| 15 | 1 | City of Brass | Land — Untapped any-color source with damage/life payment. |
| 16 | 1 | Combat Research | U Aura +1/+1 on legendary Obeka and combat-damage card draw, multiplies damage and card access. |
| 17 | 1 | Command Tower | Land — Unconditional untapped UBR source. |
| 18 | 1 | Court of Ambition | 4-mana monarch upkeep discard/life pressure, can multiply triggers; opponent taking monarchy via combat reduces payoffs. |
| 19 | 1 | Court of Cunning | 3-mana monarch upkeep mill engine and commander-specific repeated library pressure, does not itself win combat. |
| 20 | 1 | Court of Embereth | 4-mana monarch upkeep token/combat threat generation, slow against noncombat opponents. |
| 21 | 1 | Court of Ire | 5-mana monarch upkeep damage, repeat upkeeps can close games if monarchy maintained. |
| 22 | 1 | Court of Locthwain | Black monarch upkeep theft/cast-value, depends on availability of opponent cards, control of monarchy. |
| 23 | 1 | Court of Vantress | 2UU monarch upkeep token copies of another target artifact/enchantment if monarch; can copy Time Sieve or win artifact, but no token if monarch stolen. |
| 24 | 1 | Creeping Bloodsucker | 2-mana creature pings each opponent, gains life at each own upkeep; early drain multiplied by combat. |
| 25 | 1 | Cyclonic Rift | 1U targeted or 6U overloaded reset; clears blockers to connect Obeka. |
| 26 | 1 | Darksteel Reactor | 4-mana indestructible charge-counter one per upkeep, 20 charge counter win, slow without big Obeka damage. |
| 27 | 1 | Deadly Rollick | Creature exile free only while commander on battlefield, defensive and proactive evasion. |
| 28 | 1 | Deflecting Swat | Target-change shield for Obeka or payoff, free with commander present, not a generic counterspell. |
| 29 | 1 | Demonic Tutor | 1B arbitrary tutor to enabler, Sieve, pump or protection. |
| 30 | 1 | Dragonfire Blade | Equipment three-color Obeka equips at reduced {1}, gives +2/+2 & hexproof from mono-colored sources, no full hexproof. |
| 31 | 1 | Dragonmaster Outcast | One-drop upkeep Dragon creation requiring six lands; 35 lands and ramp can reach but needs many turns/land drops. |
| 32 | 1 | Embercleave | Equipment double strike and +1/+1, Obeka combat triggers separately on first-strike and regular damage if both connect. |
| 33 | 1 | Extravagant Replication | 5-mana enchantment upkeep copy permanent, high output with Obeka, but expensive and can copy noncreature payoff. |
| 34 | 1 | Fellwar Stone | Two-mana colored rock depending on opponent color production, no assured red pip. |
| 35 | 1 | Fierce Guardianship | Counter noncreature free with commander in play; protects charged-up combat and win engines. |
| 36 | 1 | Flooded Strand | Land — 1-life fetch for typed UBR dual, shock, or triome; type-matching and tempo matter. |
| 37 | 1 | Hatred | 3BB instant +X/+0 paying X life as additional cost, explosive extra upkeep count only when combat connects; life already lost if countered. |
| 38 | 1 | Inspiring Refrain | Suspend-counter draw; upkeep reduces counters, accelerates with extra upkeep phases. |
| 39 | 3 | Island | Land — Basic colored source; repeats only among the lawful basic set. |
| 40 | 1 | Jhoira of the Ghitu | Three-mana suspend card cheats big spells (rather than directly triggering upkeep), 2 mana tap activation and waiting counters. |
| 41 | 1 | Lightning Greaves | Haste/shroud equipment, 0 equip; shroud prevents own targeting auras/equipment later so order critical. |
| 42 | 1 | Luxury Suite | Land — Usually untapped 2-color multiplayer land, condition depends on opponents. |
| 43 | 1 | Mana Confluence | Land — Untapped any-color source with damage/life payment. |
| 44 | 1 | Mana Drain | UU counter, converts mana value of countered spell to next main phase COLORLESS, not UBR. |
| 45 | 1 | Marsh Flats | Land — 1-life fetch for typed UBR dual, shock, or triome; type-matching and tempo matter. |
| 46 | 1 | Mechanized Production | 2UU Aura on own artifact, at upkeep make copy then win if >=8 same-named artifacts, requires attached artifact/legal play. |
| 47 | 1 | Misty Rainforest | Land — 1-life fetch for typed UBR dual, shock, or triome; type-matching and tempo matter. |
| 48 | 1 | Mjölnir, Hammer of Thor | Legendary worthy equip {1} on non-Villain red Obeka, doubles damage dealt by equipped creature, doubles extra upkeeps from hit. |
| 49 | 1 | Morphic Pool | Land — Usually untapped 2-color multiplayer land, condition depends on opponents. |
| 50 | 2 | Mountain | Land — Basic colored source; repeats only among the lawful basic set. |
| 51 | 1 | Otawara, Soaring City | Land — Untapped U or channel interaction; spends resource. |
| 52 | 1 | Paradox Haze | 2U Aura enchanted player, only first upkeep EACH TURN grants ONE extra upkeep, not once for each newly added Obeka upkeep. |
| 53 | 1 | Phyrexian Arena | 1BB enchantment upkeep draw 1 lose 1, scales with every Obeka-created upkeep, dangerous if many and life low. |
| 54 | 1 | Plargg and Nassari | Upkeep reveal opponents' cards and cast one free, repeating can snowball but 5-mana high attack risk. |
| 55 | 1 | Polluted Delta | Land — 1-life fetch for typed UBR dual, shock, or triome; type-matching and tempo matter. |
| 56 | 1 | Profane Tutor | Suspend2 0-mana-cost tutor when cast from exile after upkeeps, not castable normally from hand. |
| 57 | 1 | Reflecting Pool | Land — Other lands needed to produce desired color; colorless with poor partners. |
| 58 | 1 | Replicating Ring | 3 mana snow any-color rock, counters each upkeep, at eight makes 8 tokens, large Obeka payoff but doesn't trigger if removed. |
| 59 | 1 | Rhystic Study | 2U opponent taxed-card draw, protects hand and shields high-investment commander. |
| 60 | 1 | Ring of Evos Isle | 2 mana equipment blue creature hexproof payment and grows +1/+1 each upkeep; equip expense; sources of protection can fail if mana unavailable. |
| 61 | 1 | Ring of Valkas | 2 mana red creature haste and +1/+1 upkeep counters, boosts Obeka and keeps triggering during many extra upkeeps. |
| 62 | 1 | Ring of Xathrid | 2 mana black creature regeneration payment and +1/+1 upkeep counters, pump but doesn't prevent exile/sacrifice. |
| 63 | 1 | Roaming Throne | 4-mana choose Ogre or Warlock, causes Obeka to trigger one additional time on damage; extra body must survive. |
| 64 | 1 | Rousing Refrain | Suspend/ritual income based on opponent hands; ticks each upkeep, red burst and further suspension. |
| 65 | 1 | Scalding Tarn | Land — 1-life fetch for typed UBR dual, shock, or triome; type-matching and tempo matter. |
| 66 | 1 | Shizo, Death's Storehouse | Land — Untapped B, paid fear to make Obeka hard to block except black/artifact blockers. |
| 67 | 1 | Silent Arbiter | 4-mana limits attackers/blockers; improves Obeka connecting one-on-one but can also restrict own offense. |
| 68 | 1 | Silver Shroud Costume | Equipment that helps evasion/protection, equip timing and mana cost matter. |
| 69 | 1 | Smaug the Magnificent | 2RR flying haste Dragon, creates Treasure each upkeep and attack deals damage equal Treasure count; multiplies Obeka upkeep output. |
| 70 | 1 | Sol Ring | 1->CC fast generic, can't satisfy UBR pips. |
| 71 | 1 | Steam Vents | Land — Untapped fetchable UBR dual/shock (shocks may cost two life); source of commander color pips. |
| 72 | 1 | Super Intelligence | One-mana Aura triggers draw at creature controller upkeep, on Obeka draws every added upkeep; shroud equipment order important. |
| 73 | 1 | Suspended Sentence | Suspend-linked recurring removal/exile effect advances via extra upkeep counter removals, interaction at pace but not universal answer. |
| 74 | 2 | Swamp | Land — Basic colored source; repeats only among the lawful basic set. |
| 75 | 1 | Swan Song | U counter instant/sorcery/enchantment; hands opponent 2/2 flier that may block Obeka. |
| 76 | 1 | Swiftfoot Boots | Equipment haste/hexproof helps connect and hold Aura targeting rights for controller. |
| 77 | 1 | Sword of Feast and Famine | Combat damage land untap and forced discard, can refuel extra turn mana but requires connection. |
| 78 | 1 | Talisman of Creativity | 2-mana UR/C rock, 1 life per colored output, helps three-color cast. |
| 79 | 1 | Talisman of Dominance | 2-mana UB/C rock, 1 life per colored output, helps three-color cast. |
| 80 | 1 | Talisman of Indulgence | 2-mana BR/C rock, 1 life per colored output, helps three-color cast. |
| 81 | 1 | Tamiyo's Journal | 5-mana upkeep investigate creates Clue token, 3 Clues sacrifice + tap tutor any card, tokens fuel Sieve separately. |
| 82 | 1 | Thassa, God of the Sea | 3-mana upkeep scry and unblockability activation, potent Obeka damage contact but costly if repeated. |
| 83 | 1 | Thopter Spy Network | 2UU upkeep create Thopter if already control artifact at both trigger and resolution, supplies Time Sieve fodder. |
| 84 | 1 | Time Sieve | UB artifact tap+sacrifice five artifacts, take extra turn; stable commander-damage 4+ with upkeep generators may replenish. |
| 85 | 1 | Toxic Deluge | 2B choose X pay life -X/-X wipe, may kill Obeka, control against wide blockers. |
| 86 | 1 | Training Center | Land — Usually untapped 2-color multiplayer land, condition depends on opponents. |
| 87 | 1 | Twilight Prophet | 2BB 2/4 ascending creature, City's Blessing condition for upkeep card reveal/drain, scales strongly with extra upkeep once blessed. |
| 88 | 1 | Underground Sea | Land — Untapped fetchable UBR dual/shock (shocks may cost two life); source of commander color pips. |
| 89 | 1 | Urborg, Tomb of Yawgmoth | Land — Untapped B and grants other lands Swamp typing; fixes B for Hatred and other costs. |
| 90 | 1 | Vampiric Tutor | B instant topdeck tutor for 2 life, finds pumping protection/timed alternate wins. |
| 91 | 1 | Verdant Catacombs | Land — 1-life fetch for typed UBR dual, shock, or triome; type-matching and tempo matter. |
| 92 | 1 | Volcanic Island | Land — Untapped fetchable UBR dual/shock (shocks may cost two life); source of commander color pips. |
| 93 | 1 | Watery Grave | Land — Untapped fetchable UBR dual/shock (shocks may cost two life); source of commander color pips. |
| 94 | 1 | Wizard's Staff | 1U equipment, normal equip3 because Obeka is WARLOCK not WIZARD; extra Obeka trigger on combat damage plus prowess. |
| 95 | 1 | Wooded Foothills | Land — 1-life fetch for typed UBR dual, shock, or triome; type-matching and tempo matter. |
| 96 | 1 | Xander's Lounge | Land — Always enters tapped but typed UBR triome with cycling; tempo vs fixing. |

**Role-level red team:** 35 lands provide mostly early untapped three-color access; 9 fetches, 3 original duals, 3 shock lands, 7 source-modeled repeated nonland mana sources, six nominal fast accelerants. Commander combat access: Menace, Aqueous Form, Brotherhood Regalia, Shizo, Thassa, Silver Shroud Costume; protection Greaves/Boots/Dragonfire Blade (only hexproof from monocolored), shields Fierce/Swat/Offer/Swan/Mana Drain, control Rift/Deluge/Rollick. Pump: Hatred, Dragonfire Blade, Mjölnir, Embercleave, Combat Research, Rings, Staff prowess, Sword. Untap/No draw in added beginning phases: must not assume naturally drawn cards from those phases except source card triggers.

**Internal weakness priority:** `Paradox Haze` one extra upkeep regardless of commander hits, same MV3 as Manufactor; `Jhoira of the Ghitu` requires time/cast mana and doesn't immediately exploit every damage-derived upkeep unless enough suspend cards, `Ring of Xathrid` regenerated Obeka can't stop exile or -X/-X and 2+2 setup; `Dragonmaster Outcast` needs six lands despite many artifact rocks; `Court of Embereth` and `Court of Ire` rely on retained monarchy and mana; `Bonehoard Dracosaur` slow 5-MV body but valuable upkeep trigger; `Plargg and Nassari` expensive but can yield multiple free spells. These are not automatically bad and must compete against genuine plan lift.

## Mana, sequencing and defense

**35 lands**: 9 fetches, 3 shocks, 3 original duals, basics 3U/2B/2R; lands often fix UBR at some fetch/shock life cost, Xander's Lounge always tapped. `Shizo` black + fear can connect Obeka versus nonblack, nonartifact blockers. `Arena of Glory` can give haste if its relevant mana is spent on creature cast, but its special use is NOT a second blue/black source. `Ancient Tomb` provides only two generic and hurts life. `Reflecting Pool` cannot make missing colors in isolation. `Hatred` costs 3BB plus **X life as additional cost**; castable only if current life available, cannot gamble X equal/exceeding life. The static source's nominal land color counts U19, B18, R18 and T4 59.2% four-land-drop no-mulligan probability are modeling **land drawing**, NOT a combined commander cast/equip/connection probability, nor a real game win rate.

**Opponent response**: risk of removal/redirect before Obeka deals combat; Hatred life already spent if countered; Mjölnir doubling is replacement on damage, not extra attack and not safe through fog; trample absent so defense and evasion mandatory. Free Fierce only with Obeka controlled; opponent can knock off commander in response to aura/equip/target. `Super Intelligence` is a targeted Aura, so attaching after Lightning Greaves shroud requires removing Greaves; Boots grants hexproof against opponents but permits owner's Auras. `Thopter Spy Network` checks artifact presence both at beginning and trigger resolution, not merely when it was cast.

**Artifacts**: `Time Sieve` {T} and sacrifice FIVE artifacts; sacrifice Time Sieve itself is possible but defeats automatic repeatability if no replacement. `Tamiyo's Journal` {T} sacrifice THREE Clues -> tutor, cannot spend same Clues toward Sieve. Court of Vantress, if still monarch, may create a new Sieve copy each upkeep; if not monarch, chooses to **become** a copy of target artifact/enchantment (and retain that ability) instead of generating token. `Mechanized Production` checks EIGHT artifacts you control sharing same name (not necessarily eight copies of the enchanted target), and requires a legal enchanted artifact. No auto infinite claim from incomplete board.

## Candidate pool and competing cuts

**All 38 M5 pairs triaged** by mechanism, with actual alternate cut rather than enforcing weak rank-suggested cuts. Two performance-pass outcomes are insufficient to prove metagame superiority.

| Challenger from M5/off-ranking | Source's proposed cut vs a credible alternative | Decision / opponent counterexample |
|---|---|---|
| **Academy Manufactor** (M5 #135, cut Fellwar Stone) | Bad modeled cut is 2-MV Fellwar Stone needed for three-color cast; **better compare Paradox Haze** (3 mana, only one extra upkeep/turn), or slow Ring of Xathrid. | **Best concrete commander-first proposal: Manufactor IN / Paradox Haze OUT**, owner approval only. Manufactor's **replacement** turns each Smaug upkeep Treasure or Journal upkeep Clue into **one Clue + one Food + one Treasure**, i.e. THREE artifacts *per original creation*. With both Smaug and Journal on board each upkeep yields 6 artifacts; one normal upkeep can already feed Time Sieve (five artifacts), independent of Obeka, but Obeka multiplies this dramatically. Fragile 1/3 artifact creature, 3-mana setup, needs source generators, Haze remains useful without commander and can still produce meaningful Court/As Foretold triggers. **Conditional recommendation, no applied swap**. |
| **Izzet Signet / Dimir Signet** (rank49/61) | Fellwar Stone | Guaranteed paired colors but costs one generic activation; often Fellwar taps for useful mana directly. Without color-starvation simulation, no automatic gain. |
| **Descent into Avernus** (rank6) | Fellwar Stone, prior intentionally removed for Darksteel Reactor | One extra upkeep multiplies symmetrical Treasure/damage to ALL players, can burn out deck quicker than opponents and gifts resources into counterspells. REJECT. |
| **The Reaver Cleaver / Ring of Valkas** | Fellwar Stone in M5, but more relevant compare Ring of Xathrid or Plargg | Extra Treasures from creature combat damage require equipped damage connection and initial equip expense; Manufactor/Journals/Smaug already provide greater upkeep-driven volume, no reason to lose fixing. HOLD. |
| **Aggravated Assault** (rank32) | Ring of Valkas | Extra combat allows more Obeka hits and Sword+Assault generic loop, but cutting Ring removes recurring haste and upkeep counter growth; Sword-Assault generic win functions without commander. Owner explicitly rejected earlier hybrid. HOLD. |
| **The Tenth Doctor / Timestream Navigator / Thopter Assembly** | Bonehoard Dracosaur, Roaming Throne | Doctor suspend engine needs attack and mana, competes with core; Navigator/Assembly can add extra turns or Thopter tokens, but removing Roaming Throne sacrifices direct multiple Obeka upkeep triggers; Bonehoard already reliable per-upkeep value when it survives. REJECT exact swaps. |
| **Hullbreaker Horror / Tidespout Tyrant / Olivia's Attendants** | Deadly Rollick | Expensive creature/infinite/treasure lines vs cheap conditional-free removal that clears blocker/protects Obeka; no justified loss of interaction. HOLD. |
| **Reiterate** | Hatred | Spell copier cannot replicate X-life→N-upkeep acceleration; removes commander's burst engine. REJECT. |
| **Wanderwine Prophets / Hellkite Charger / Cybermen Squadron / Myr Battlesphere / Timestream** | Ring of Valkas or Bonehoard | Standalone extra-turn or combat engines need extra bodies/resources and usually don't cause commander damage directly; no demonstrated gain over existing damage-upkeep equipment. HOLD. |
| **Second Chance** | Paradox Haze | Second Chance threshold life <=5, enchantment sacrifice extra turn on upkeep; lifesaving timing perhaps but requires dangerous life state and isn't a core Obeka payoff. HOLD. |
| **The Ninth Doctor / Shadow of Second Sun / Sphinx of Second Sun / Palace Siege / Ginger Queen Sweets** (historical near-misses) | Paradox Haze or Ring Xathrid | Additional upkeep/card drain effects can help, but 5-6MV payoff costs are heavy; Haze cheaper baseline. Against actual Manufactor token synergy, unsupported blanket additions. |
| **Robe of the Archmagi / Blackblade Reforged** (historical) | Combat Research or other pump | Robe equips cheaply to Warlock for draw proportional to damage, but doesn't itself improve damage; Blackblade huge pump yet redundant with Mjölnir/Blade/Hatred/Embercleave. Conditional high-meta alternatives only. |
| **Generic Oracle/Consult, unrelated Breach** | UBR engines | Strong raw efficiency but erases combat damage → extra upkeep strategy. Excluded from commander-first. |

**Critical cut comparison:** Haze with Reactor+Journal can add one extra noncombat upkeep every turn and actually helps when the commander is absent or indefinitely countered. Manufactor without Smaug/Journal produces nothing and can be destroyed by almost any removal. But when this **specific approved deck** already devotes four slots to artifact upkeep production, an ordinary one-per-turn Haze is less explosive, while Manufactor enables Time Sieve on **one normal upkeep** if both upkeep generators exist. In the expected slower optimized Bracket4 pod the 1/3 is vulnerable to board wipes, and producing five artifact tokens costs multiple other permanents; not enough objective performance evidence for an applied swap. Proposal may be stronger than exact M5 `Manufactor/Fellwar`, which must be rejected.

## Oracle, legality and rules

1. **Obeka's ability:** actual combat damage dealt to **player** gives N extra upkeep steps after **that combat phase**, placed in additional beginning phases skipping untap/draw. Combat damage to planeswalker/battle does not trigger.
2. **Damage and copy count:** +2/+2 Dragonfire Blade yields 4-power Obeka, if 4 player damage → 4 extra upkeeps. Mjölnir doubles actual combat damage to 8 → 8 extra upkeeps; Roaming Throne + Staff adds two triggers on that single damage event, each for 8 = **24 extra upkeeps** (not 8, not 32). Creature must remain enchanted/equipped on relevant event; trigger survives Obeka subsequent removal after triggering unless countered.
3. **Embercleave:** double strike results in separate first/normal damage events if eligible damage happens both steps; each leads to separate Obeka triggers and upkeeps, as long as combat not ended early. Staff prowess requires noncreature spell cast before combat damage to improve power.
4. **Roaming Throne:** choose Ogre or Warlock, two-card extra trigger with Staff additive original+1+1; does not itself give extra copies of upkeep triggers of Courts (unless creature-type source qualifies, Courts aren't creatures).
5. **Wizard's Staff:** equip Wizard {1} does **not** apply because Obeka is Warlock. Normal equip {3} and cards targeted cannot be shrouded by Greaves when trying to equip. Source [Wizards Hobbit notes](https://magic.wizards.com/en/news/feature/the-hobbit-release-notes).
6. **Paradox Haze:** triggers only at beginning of enchanted player's **first** upkeep each turn. Added postcombat upkeeps don't trigger Haze again on same turn. Source [WotC release notes](https://media.wizards.com/2025/downloads/EOE_Release_Notes_R8Z03VaANE/EN_MTGEOE_ReleaseNotes_20250718.pdf).
7. **Manufactor:** instead of creating any Clue/Food/Treasure token, creates one EACH per original creation. Journal investigation still counts once for any 'whenever you investigate' clause, not an additional three investigates. Source [card Oracle/rulings](https://mtg.wtf/card/pmh2/219s/Academy-Manufactor).
8. **Journal and Smaug upkeep:** EACH upkeep Smaug produces one Treasure, Journal produces a Clue; with Manufactor two separate effects produce SIX artifact tokens (Clue, Food, Treasure each) as long as all permanents survive. If one generator absent, THREE artifacts/upkeep. Token creations are separate triggers that opponents can respond to.
9. **Court of Vantress monarch:** target a different artifact/enchantment at EACH upkeep; if monarch make a token copy of it; if not monarch, may turn Court into copied permanent preserving ability, no token created. Court must keep monarchy for repeat artifact copies, opponent attacks can steal.
10. **Time Sieve:** requires 5 artifact sacrifices and tap each use, extra turn AFTER this one. A copied Sieve can activate after being created if not a creature and not tapped, but cannot pay activation of original and copy at same time using same artifacts.
11. **Mechanized Production:** win after creating token at upkeep if control 8 or more artifacts sharing name with one another, name needn't be that of Aura target. Control of same name checked on resolution; opponents may destroy Aura/artifact or remove tokens.
12. **Replicating Ring:** upkeep counter growth through 8 counters creates 8 ring copies, but only if ring survives and trigger resolves. Additional generated upkeep has no untap, so previously tapped ring stays tapped through them.
13. **Darksteel Reactor:** charge counter at each controller upkeep, 20+ triggers win condition; opponent removal by exile/bounce still possible despite indestructible, and artifact-hate threatens setup.
14. **Super Intelligence:** enchanted creature controller draws at upkeep, even if not Obeka if target selection changed; if Obeka equipped Greaves shroud, can't later attach own aura; plan order.
15. **Hatred:** X life PAID on cast; if blocked/countered you still lost life. Increase only power, not damage automatic. Life budget and opponent held removal determine whether safe.
16. **Ring of Evos/Xathrid/Valkas:** pump trigger at each controller upkeep if creature specific color condition; all apply to Obeka (UBR) and build counters quickly, but equipment equip to initially attach may cost large mana, counter growth isn't retroactive to already completed combat.
17. **Swan Song:** opponent gains 2/2 flying blocker, menace requires two blockers; flying is relevant if Obeka given evasion, tradeoff between shielding spell and future connection.
18. **Thopter Spy Network:** artifact required BOTH at trigger and resolution; Time Sieve itself can satisfy unless sacrificed in response. Generates 1 Thopter each extra upkeep; with normal upkeep + four extra, 5 artifact tokens if all trigger.
19. **Thassa unblockable:** Thassa's activation makes creature unblockable, costs mana; opponent can respond/removal; normal Menace doesn't guarantee unblocked.
20. **Official legality:** canon Oct15 verified UBR 100, engineering Oct16 Scryfall oracle bulk compliant, exceptions none. Academy Manufactor official Commander legal, colorless. Future owner-approved proposed swap needs fresh all-100 verification; no new current whole-list Oracle request claimed.

## Finite sequencing and adversarial scenarios

Deterministic card-paid thought tests, not stochastic gameplay, not assumed opponents pass priority.

| Trace | Exact source and initial state | Baseline/conditional challenger result |
|---|---|---|
| S1 | Obeka 2/5 menace unblocked, no pump, opponent takes 2 player combat | 2 postcombat added upkeeps, normal upkeep already occurred; no extra draws by rule. |
| S2 | Obeka Blade +2/+2, hits 4 | 4 added upkeeps; artifact engine triggers four times if survives, and base upkeep once. |
| S3 | Obeka 4 power, Mjölnir doubles all damage | 8 damage, eight extra upkeeps; commander combat damage counted as 8, no extra combat created. |
| S4 | S3 plus Throne (Ogre) and Wizard's Staff | Each of 3 triggered copies makes 8 upkeep steps = **24** upkeep steps after combat. |
| S5 | Obeka unblocked with both Staff and Throne but power2, no Mjölnir | 2 damage, 3 triggers ×2 = 6 extra upkeeps; not 8/12. |
| S6 | Obeka Embercleave, power3 double strike; 3 damage first step and 3 second | Two damage events each 3; six extra upkeeps total base, adjusted for other effects; losing attacker after first stops second. |
| S7 | 3 mana Paradox Haze on self, Obeka missed attack | Normal upkeep + exactly one added Haze upkeep, even with no commander; supports Court draw. |
| S8 | Paradox Haze plus Obeka 4 damage creates 4 more upkeeps after combat | Haze doesn't trigger again in extra beginning phases (already first upkeep passed); total upkeeps this turn 1 normal+1 Haze+4 Obeka =6. |
| S9 | Tamiyo Journal only, Manufactor on field, current normal upkeep | Journal triggers investigate: 1 Clue/Food/Treasure =3 artifacts; cannot produce 6 without second separate token event. |
| S10 | Journal + Smaug + Manufactor all present during normal upkeep | Each two token events produces 3 -> 6 artifacts; Time Sieve may sacrifice five when allowed and untapped, even without Obeka. |
| S11 | Time Sieve + Thopter Spy Network and Obeka 4 damage, no blockers | Normal upkeep Network produced 1 Thopter, each four Obeka-upkeeps yields 1; 5 Thopters support Sieve (requires tap and five sacrifices), next turn repeat conditional. |
| S12 | Network, but last artifact sacrificed before new upkeep trigger checks | No trigger (intervening if fails); not 1 free Thopter. |
| S13 | Sieve + 4 Clues + Journal | You may sacrifice Clues as artifacts to Sieve, need total five (one Sieve itself or 5 external), but sacrificing three Clues to Journal leaves just one and cannot count consumed Clues twice. |
| S14 | Court Vantress, monarch, existing Sieve, added 4 upkeeps | May copy Sieve at each upkeep, producing tokens if target remains legal and monarchy kept. Copies aren't legendary; all have tap ability that can be used after creation. |
| S15 | Same Court, monarchy lost before upkeep | Cannot make token; may have Court become copy and carry its granted upkeep ability, real strategic volatility. |
| S16 | Mechanized Production on one artifact, 7 Clues controlled, another arbitrary artifact | If at resolution you have 8 CLUES from previous token sources, alternate win independent of enchanted artifact name; if token removed before check, no win. |
| S17 | Replicating Ring with 7 night counters and Obeka makes multiple upkeeps | Next trigger adds eighth counter, creates 8 Ring tokens; do not count 9 new tokens without Oracle. |
| S18 | Hatred: life 20, pay X=15, Obeka original power2 unblocked | Obeka deals normally 17 combat, 17 added upkeeps (before other modifiers), controller at 5 life; countered Hatred still leaves 5 life but no bonus. |
| S19 | Three Rings on Obeka with extra 5 upkeeps, all colors UBR | Each Ring adds counter when its matched color upkeep trigger resolves; future attack bigger, does NOT increase damage event already done. |
| S20 | Darksteel Reactor at 18 counters, Obeka 2 damage creates 2 upkeeps | Two triggers can bring 18→20 and win as triggered condition permits, assuming no response. |
| S21 | Obeka blocked by two creatures (menace minimum 2), no trample | No player combat damage, no bonus upkeep; evasion/equipment is central, not decorative. |
| S22 | Academy Manufactor enters tapped? just cast as artifact creature; then opponent Toxic Deluge | 1/3 can die before future upkeeps, so no replacement; Paradox Haze Aura on player might have survived and kept one-upkeep value. |
| S23 | Mjölnir equipped, victim prevented all Obeka combat damage | No combat damage event, zero Obeka triggers despite damage multiplier. |
| S24 | Super Intelligence attached; Obeka creates eight upkeeps and Phyrexian Arena also present | Draw 8 from Aura plus 8 Arena draws and lose 8 life, not eight free draw steps; life budget matters. |

**Adversarial strongest-case** Manufactor yields exceptional artifact Sieve rates from a 3MV card **with existing** Smaug + Journal, unlike Haze's single upkeep-per-turn bonus; a removal-heavy pod kills the 1/3 before the next upkeep and nullifies it, while Haze on yourself survives ordinary sweeper and gives one upkeep even when commander inaccessible. The distinction is board state, not unconditional superiority. **Recommendation: present exact IN Manufactor / OUT Paradox Haze for owner consideration after downstream verification; DO NOT apply.**

## Conclusions and unresolved evidence

**KEEP approved 100 unchanged**, Bracket 4. **Primary unapplied proposal**: Academy Manufactor for Paradox Haze, commander-specific replacement effect trading broad unconditional one-upkeep support for artifact-token multiplication and faster Sieve/Mechanized Production opportunities. M5's `Manufactor -> Fellwar Stone` should be rejected because it cuts necessary mana stability. Secondary conditional challenge Ring of Xathrid (regen weaker than exile) or Jhoira (slow suspended setup), but no evidence better across full deck.

**Counted/checked:** 100 weighted cards / 96 names / 35 lands with basic-only repeats (3 Island, 2 Mountain, 2 Swamp), UBR and official legal Oct15/16 source, 38 M5 hypotheses grouped, rare Oracle equipment/cost/phase/source checks, 24 payable finite scenarios. Current legal snapshot is last full baseline check, not a newly executed comprehensive query. No blind ranking, canonical changes, approved hash/lock changes, project exception change, M6.4 62/62 reset or Pass C certification. Future proposed deck change demands owner approval and all full-list gates. This evidence artifact and tracker transition each require separate exact-head CI, source-bound and no-skip / tamper checks; only then progress 44→45.
