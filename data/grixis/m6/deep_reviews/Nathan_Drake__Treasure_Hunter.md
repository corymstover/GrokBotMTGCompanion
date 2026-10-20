# M6 comprehensive single-deck authored review #39 — Nathan Drake, Treasure Hunter

**Deck ID:** `Nathan_Drake__Treasure_Hunter`; tracker index 38 (39th of 62). **Author:** ChatGPT (not independent GrokBot Pass C). **Date:** 2026-10-19 America/Chicago.

**Authority:** Canonical `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json#decks.Nathan_Drake__Treasure_Hunter` records **APPROVED / LOCKED** with approved TXT SHA-256 `a5d59afc3a78d7ff6454b1d011c82c2f732e11f4d4dd03256df1195a3abe9ba0`; engineering logical identity `lh1:ac167a53ea77215d7eb148ea2eb814c2596d8da1943a971a8ee077c6d35ceb00`, no discrepancy. Historical FINAL baseline had 94 distinct names/33 lands; current approved version has 97 names/34 lands. This review does not reopen the historical 12-for-12 approval.

## Source and test receipts

Read current engineering `AGENTS.md`, `grixis/M6 Commander-First Single-Deck Review Standard.md`, depth tracker, registry and M6/M7 subtracker; canonical override, approved TXT, whole-list audit, approval-ready verification and candidate decisions (2026-10-15). Engineering `grixis/blueprints/nathan-drake-treasure-hunter.md`, `grixis/interactions/nathan-drake-treasure-hunter.md` (8 rules cases; Scryfall Oracle bulk 2026-10-16, rulings 2026-10-15, CR 2026-09-25), `data/grixis/m6/review_packets/nathan-drake-treasure-hunter.json` (249 candidate-cut hypotheses, 245 distinct candidate adds), `data/grixis/mana_base/nathan-drake-treasure-hunter.json` and `data/grixis/birthday_m5/evidence/nathan-drake-treasure-hunter.json`. Dated sources are NOT a fresh Oct19 all-card Scryfall lookup.

**Independent approved TXT arithmetic:** 97 distinct name rows, 100 total physical cards, exactly one commander, 99 library cards; only Island x2, Mountain x2 and Swamp x2 repeat, all basic lands; no nonbasic singleton violations; 34 lands by current static mana report, UBR color identity. Card role audit below covers every name in approved TXT order; quantity-weighted coverage 100/100. Project exception: **none**. Official Commander legality is supported by canonical 2026-10-15 verification and 2026-10-16 engineering Oracle; no new Oct19 complete card-by-card recheck claimed.

## Commander identity and natural ceiling

Nathan is **{U}{B}{R} 3/2 Human Rogue with first strike**. When Nathan ATTACKS, exile the top card of EACH player's library, then **cast at most one spell** from those exiled cards **during trigger resolution** and pay its costs. A land is not a spell. Uncast cards stay exiled. Nathan's static mana color flexibility applies to spells **you do not own** and abilities of permanents you control but don't own, **not your own exiled card**. The commander is a three-mana, repeatable four-library heist with unusual payment timing, NOT combat-damage theft and NOT free Etali. The deck wins by repeated heists, tempo and stolen opponent threats rather than a generic Oracle/Breach combo. **Natural ceiling: low-to-mid Bracket 4 Optimized**; very strong card quality and commander-driven value, but variable hits and no compact deterministic kill.

Identity protection: prioritize (1) attacking with Nathan promptly and repeatedly, (2) mana held or produced during his attack trigger to cast an opponent's spell, (3) trigger multiplication, extra combats and stolen-spell/exile payoffs, (4) protection of 3/2 commander, (5) resilience when Nathan is removed. Reject upgrades that merely substitute a stronger generic Grixis control/Oracle shell, replace cheap interaction with six-mana theft bodies, or optimize generic goldfish resources while omitting attack-window casting.

**Core:** Roaming Throne (Rogue), Firebender Ascension, Karlach, Fire Lord Azula, Fire Nation Palace, Arena of Glory, Brotherhood Regalia, Greaves/Boots, Interdimensional Web Watch, Nalfeshnee, Wild-Magic Sorcerer, Passionate Archaeologist, Don Andres/Gonti/Tasha/Vaan. Independent theft from Etali, Plargg and Nassari, Stolen Strategy and others retains function through commander removal. Important self-conflict: Dauthi Voidwalker's exile replacement reduces Tinybones the Pickpocket's opponent-graveyard targets; don't hide this.

## Full 100-card role audit

Rows are exact canonical order, all distinct names with quantities. A land's strategic role includes untapped/typed color access and the cost of not casting a payoff; each nonland is evaluated for Nathan's attack timing, theft identity, engine payoff, interaction or opportunity cost.

| # | Qty | Approved card | Role | Commander-specific evaluation / limitation |
|---:|---:|---|---|---|
| 1 | 1 | Nathan Drake, Treasure Hunter | Commander / attack heist | UBR 3/2 first-strike Human Rogue; attacks exile four top cards, allows exactly one spell cast during trigger resolution with its costs paid; not damage-triggered |
| 2 | 1 | An Offer You Can't Refuse | Counterspell / stack protection | U noncreature counter gives opponent two Treasures, real tempo liability |
| 3 | 1 | Ancient Tomb | Mana land / attack utility | two colorless for 2 life; accelerates engine but doesn't pay UBR commander alone |
| 4 | 1 | Arcane Signet | Cheap mana / exile casting | 2-mana rock any color in UBR, strongest generic fixing for commander |
| 5 | 1 | Arena of Glory | Mana land / attack utility | red exert mana grants haste to creature spell paid with it; color source but needs R upfront and Mountain to enter untapped |
| 6 | 1 | Arid Mesa | Fetch land / typed-dual selection | Sacrifice and pay 1 life for matching basic land TYPE (including appropriate dual/shock/triome), not an unrestricted any-color fetch. |
| 7 | 1 | Badlands | Typed dual/shock/triome | Typed UBR fixing and fetch target; shock enters untapped only by paying 2 life, triome enters tapped. |
| 8 | 1 | Black Cat, Cunning Thief | Opponents' cards / theft access | nine-card selection plus Rogue body, significant synergy with Throne |
| 9 | 1 | Black Market Connections | Additional resource/recursion | reliable upkeep options card/Treasure/body at life cost; protects ability to pay Nathan's combat spells |
| 10 | 1 | Blasphemous Act | Removal, hate, disruption | scales down to R in creature-heavy tables; kills Nathan absent protection |
| 11 | 1 | Blood Crypt | Typed dual/shock/triome | Typed UBR fixing and fetch target; shock enters untapped only by paying 2 life, triome enters tapped. |
| 12 | 1 | Bloodstained Mire | Fetch land / typed-dual selection | Sacrifice and pay 1 life for matching basic land TYPE (including appropriate dual/shock/triome), not an unrestricted any-color fetch. |
| 13 | 1 | Brotherhood Regalia | Haste, evasion, attack protection | equip legendary for {1}, ward2 and unblockable; protects repeat attacks but trigger doesn't need combat damage |
| 14 | 1 | Chaos Warp | Removal, hate, disruption | one of few Grixis permanent-type catchalls, opponent may reveal dangerous permanent |
| 15 | 1 | City of Brass | Untapped/flexible multiplayer fixing | Flexible colored source; multiplayer conditions, pain or opponent land dependency must be considered. |
| 16 | 1 | Command Tower | Untapped/flexible multiplayer fixing | Flexible colored source; multiplayer conditions, pain or opponent land dependency must be considered. |
| 17 | 1 | Court of Locthwain | Opponents' cards / theft access | monarch-based recurring theft; can lose monarch after combat damage |
| 18 | 1 | Cyclonic Rift | Removal, hate, disruption | versatile instant bounce, overload seven mana; better emergency reset than costly bounce creature |
| 19 | 1 | Dark Ritual | Cheap mana / exile casting | BBB one-shot acceleration; triple black cannot supply U or R commander pips without other sources |
| 20 | 1 | Dauthi Voidwalker | Removal, hate, disruption | replacement exiles opponents' graveyard cards, offering a powerful free cast but depriving Tinybones of graveyard targets |
| 21 | 1 | Deadly Rollick | Removal, hate, disruption | exile creature, free while commander controlled; not noncreature/artifact removal |
| 22 | 1 | Deflecting Swat | Removal, hate, disruption | redirect targets if any; free only with commander controlled; cannot redirect overloaded Vandalblast |
| 23 | 1 | Demonic Tutor | Tutor / sustained card draw | 2-mana precise search for trigger doubling, haste, or protection |
| 24 | 1 | Don Andres, the Renegade | Exile/unowned cast payoff | unowned noncreature cast makes two tapped Treasures, unavailable to fund the spell already being cast; stolen creatures receive combat boost |
| 25 | 1 | Dream-Thief's Bandana | Haste, evasion, attack protection | theft/evasion support; must check exact triggered condition before asserting extra Nathan trigger |
| 26 | 1 | Etali, Primal Storm | Opponents' cards / theft access | attack-trigger multiopponent free spell casting, but six mana and no haste by default; can trigger even if Nathan absent |
| 27 | 1 | Exotic Orchard | Untapped/flexible multiplayer fixing | Flexible colored source; multiplayer conditions, pain or opponent land dependency must be considered. |
| 28 | 1 | Fellwar Stone | Cheap mana / exile casting | color depends on opponent lands, not guaranteed to produce any chosen color |
| 29 | 1 | Fierce Guardianship | Counterspell / stack protection | free noncreature counter only while controlling commander; does not counter Oracle creature |
| 30 | 1 | Fire Lord Azula | Attack triggers / extra combat | combat mana and copy of cast spell while attacking; copied spell not cast |
| 31 | 1 | Fire Nation Palace | Mana land / attack utility | firebending 4 before combat for attack-window mana; activation costs 1R and tap |
| 32 | 1 | Firebender Ascension | Attack triggers / extra combat | two-mana Soldier/firebending setup; quest-counter engine eventually copies attacking creature's own trigger, including Nathan's |
| 33 | 1 | Flooded Strand | Fetch land / typed-dual selection | Sacrifice and pay 1 life for matching basic land TYPE (including appropriate dual/shock/triome), not an unrestricted any-color fetch. |
| 34 | 1 | Force of Negation | Counterspell / stack protection | free only on opponent's turn with blue pitch; Nathan attacks on own turn, cannot assume free in combat |
| 35 | 1 | Gonti, Night Minister | Opponents' cards / theft access | Treasure on unowned spell cast; stolen-spell infrastructure |
| 36 | 1 | Grenzo, Havoc Raiser | Opponents' cards / theft access | combat-damage triggers from your creatures, choice goad or exile opponent top; needs connections |
| 37 | 1 | Gríma, Saruman's Footman | Opponents' cards / theft access | opponent-card access tied to creature trigger, interaction exposure |
| 38 | 1 | Hostage Taker | Opponents' cards / theft access | exiles creature/artifact while on battlefield; stolen cast costs paid and depends on source survival |
| 39 | 1 | Interdimensional Web Watch | Exile/unowned cast payoff | restricted exile-spell mana directly funds Nathan's unusual cast-during-resolution payment |
| 40 | 2 | Island | Basic land | Untapped basic fetch target; repeated basic copies are permitted; preserves resilience to nonbasic hate. |
| 41 | 1 | Jeska's Will | Cheap mana / exile casting | mana or exile access, both with commander controlled; timing is main-phase sorcery, cannot wait until Nathan trigger |
| 42 | 1 | Karlach, Fury of Avernus | Attack triggers / extra combat | first-combat attack grants extra combat and untaps attackers; no extra main phase; Nathan must survive and attack again |
| 43 | 1 | Laughing Jasper Flint | Opponents' cards / theft access | opponent-library theft when conditions met, can function without Nathan |
| 44 | 1 | Lightning Greaves | Haste, evasion, attack protection | zero equip shroud/haste; shroud blocks your own targeted buffs until unequipped |
| 45 | 1 | Locke, Treasure Hunter | Opponents' cards / theft access | theft/value support; exact Oracle interactions source-dated and should not be overstated |
| 46 | 1 | Lotus Petal | Cheap mana / exile casting | free one-time any-color mana held for attack trigger, real cost is consumed card |
| 47 | 1 | Luxury Suite | Untapped/flexible multiplayer fixing | Flexible colored source; multiplayer conditions, pain or opponent land dependency must be considered. |
| 48 | 1 | Mana Confluence | Untapped/flexible multiplayer fixing | Flexible colored source; multiplayer conditions, pain or opponent land dependency must be considered. |
| 49 | 1 | Mana Drain | Counterspell / stack protection | UU unconditional spell counter; requires blue source and priority, later colorless mana cannot pay colored commander pips |
| 50 | 1 | Marsh Flats | Fetch land / typed-dual selection | Sacrifice and pay 1 life for matching basic land TYPE (including appropriate dual/shock/triome), not an unrestricted any-color fetch. |
| 51 | 1 | Misty Rainforest | Fetch land / typed-dual selection | Sacrifice and pay 1 life for matching basic land TYPE (including appropriate dual/shock/triome), not an unrestricted any-color fetch. |
| 52 | 1 | Morphic Pool | Untapped/flexible multiplayer fixing | Flexible colored source; multiplayer conditions, pain or opponent land dependency must be considered. |
| 53 | 2 | Mountain | Basic land | Untapped basic fetch target; repeated basic copies are permitted; preserves resilience to nonbasic hate. |
| 54 | 1 | Mystic Remora | Tutor / sustained card draw | early multi-opponent noncreature-spell draw, upkeep cumulative cost makes it temporary |
| 55 | 1 | Nalfeshnee | Exile/unowned cast payoff | copies cast-from-exile spell, copy isn't cast; permanent spell copy becomes temporary token |
| 56 | 1 | Notion Thief | Removal, hate, disruption | flash draw replacement, can backfire with symmetric draw and is not native Nathan attack trigger |
| 57 | 1 | Opposition Agent | Removal, hate, disruption | flash controls opponents' searches, steals tutor outcomes; adversarial stack interaction |
| 58 | 1 | Otawara, Soaring City | Mana land / attack utility | untapped blue source with channel interaction; channel not counterable as spell |
| 59 | 1 | Passionate Archaeologist | Exile/unowned cast payoff | Background in library still grants commander creature exile-cast damage trigger; must control Nathan when casting |
| 60 | 1 | Plargg and Nassari | Opponents' cards / theft access | upkeep exile opponent-library access; opponents select one each, you cast one; no attack trigger requirement |
| 61 | 1 | Polluted Delta | Fetch land / typed-dual selection | Sacrifice and pay 1 life for matching basic land TYPE (including appropriate dual/shock/triome), not an unrestricted any-color fetch. |
| 62 | 1 | Praetor's Grasp | Opponents' cards / theft access | searches opponent library and exiles a card face down for casting later, can steal answer/win card |
| 63 | 1 | Professional Face-Breaker | Exile/unowned cast payoff | Treasure from combat damage and sacrifice to exile own cards; requires damage unlike Nathan's attack trigger |
| 64 | 1 | Prosper, Tome-Bound | Exile/unowned cast payoff | end-step exile access plus Treasure from playing exile cards; mana often arrives after spell is cast |
| 65 | 1 | Ragavan, Nimble Pilferer | Opponents' cards / theft access | one-mana treasure and theft on combat damage; needs actual damage and may not connect |
| 66 | 1 | Reanimate | Additional resource/recursion | cheap creature recursion, including stolen opponent graveyard creatures when available; life loss equals MV |
| 67 | 1 | Rev, Tithe Extractor | Opponents' cards / theft access | theft/treasure value requiring board and sequencing; not interchangeable with direct attack-trigger copies |
| 68 | 1 | Rhystic Study | Tutor / sustained card draw | repeatable tax/draw, powerful but commander-independent and three mana |
| 69 | 1 | Roaming Throne | Attack triggers / extra combat | choose Rogue to double Nathan attack trigger; each instance separately exiles four cards and permits one cast, mana not waived |
| 70 | 1 | Robber of the Rich | Opponents' cards / theft access | early attack-driven exile access conditional on hand sizes; spells have limited timing and mana costs |
| 71 | 1 | Scalding Tarn | Fetch land / typed-dual selection | Sacrifice and pay 1 life for matching basic land TYPE (including appropriate dual/shock/triome), not an unrestricted any-color fetch. |
| 72 | 1 | Shizo, Death's Storehouse | Mana land / attack utility | black utility mana; {B},tap gives legendary creature fear, survival rather than trigger enablement |
| 73 | 1 | Siphon Insight | Opponents' cards / theft access | instant look at top two of opponent library, exile one; flashback allows two cast opportunities |
| 74 | 1 | Sol Ring | Cheap mana / exile casting | fast generic acceleration; can't satisfy UBR commander colored requirements |
| 75 | 1 | Steam Vents | Typed dual/shock/triome | Typed UBR fixing and fetch target; shock enters untapped only by paying 2 life, triome enters tapped. |
| 76 | 1 | Stolen Strategy | Opponents' cards / theft access | each upkeep exiles opponent top cards for later casting; persistent advantage but costs five and doesn't solve combat mana |
| 77 | 2 | Swamp | Basic land | Untapped basic fetch target; repeated basic copies are permitted; preserves resilience to nonbasic hate. |
| 78 | 1 | Swan Song | Counterspell / stack protection | U counters enchantment/instant/sorcery, not creature spells |
| 79 | 1 | Swiftfoot Boots | Haste, evasion, attack protection | {1} equip hexproof/haste, preserves ability to target Nathan with Fire Nation Palace |
| 80 | 1 | Talisman of Creativity | Cheap mana / exile casting | UR mana at 1 life per colored activation, fixes two commander colors |
| 81 | 1 | Talisman of Dominance | Cheap mana / exile casting | UB mana at 1 life per colored activation, fixes two commander colors |
| 82 | 1 | Talisman of Indulgence | Cheap mana / exile casting | BR mana at 1 life per colored activation, fixes two commander colors |
| 83 | 1 | Tasha, the Witch Queen | Opponents' cards / theft access | Demon creation when you cast a spell you don't own; a planeswalker that must survive to benefit |
| 84 | 1 | Thief of Sanity | Opponents' cards / theft access | requires combat damage; opponent-top-three theft, slow if blockers dominate |
| 85 | 1 | Thieving Varmint | Cheap mana / exile casting | two mana of one color only for spells not owned; doesn't help cast Nathan or your own exiled spell |
| 86 | 1 | Tinybones, the Pickpocket | Opponents' cards / theft access | needs opponent graveyard card on combat damage; Voidwalker replacement can leave no targets |
| 87 | 1 | Training Center | Untapped/flexible multiplayer fixing | Flexible colored source; multiplayer conditions, pain or opponent land dependency must be considered. |
| 88 | 1 | Underground Sea | Typed dual/shock/triome | Typed UBR fixing and fetch target; shock enters untapped only by paying 2 life, triome enters tapped. |
| 89 | 1 | Vaan, Street Thief | Opponents' cards / theft access | unowned spells grow relevant Scouts/Pirates/Rogues, including Nathan; combat pressure rather than guaranteed kill |
| 90 | 1 | Vampiric Tutor | Tutor / sustained card draw | B instant tutor puts card on top at 2 life, card not directly to hand; can arrange next draw |
| 91 | 1 | Verdant Catacombs | Fetch land / typed-dual selection | Sacrifice and pay 1 life for matching basic land TYPE (including appropriate dual/shock/triome), not an unrestricted any-color fetch. |
| 92 | 1 | Volcanic Island | Typed dual/shock/triome | Typed UBR fixing and fetch target; shock enters untapped only by paying 2 life, triome enters tapped. |
| 93 | 1 | Watery Grave | Typed dual/shock/triome | Typed UBR fixing and fetch target; shock enters untapped only by paying 2 life, triome enters tapped. |
| 94 | 1 | Wild-Magic Sorcerer | Exile/unowned cast payoff | first spell cast from exile each turn has cascade; cascade spell cast from exile can trigger additional payoffs |
| 95 | 1 | Wooded Foothills | Fetch land / typed-dual selection | Sacrifice and pay 1 life for matching basic land TYPE (including appropriate dual/shock/triome), not an unrestricted any-color fetch. |
| 96 | 1 | Xander's Lounge | Typed dual/shock/triome | Typed UBR fixing and fetch target; shock enters untapped only by paying 2 life, triome enters tapped. |
| 97 | 1 | You Find Some Prisoners | Opponents' cards / theft access | modal artifact destruction or temporary top-three theft from opponent library |

## Mana, curve, interaction and identity protection

Current static mana evidence: **34 lands, nine fetches, six basics** (2 each Island/Mountain/Swamp), seven repeatable nonland mana sources, nine `fast_mana` flags (including rituals and Varmint), one Lotus Petal one-shot, one Dark Ritual. Colored **land sources B18/R19/U18**, unconditional B17/R18/U17; land plus repeatable nonland B23/R24/U23. Spell pip shares **B 41.33%, R 34.67%, U 24%**. Double-pip counts B5/R3/U2. The three-mana UBR commander needs all three distinct colors, not merely three mana. The source proxy estimates three-color land-source presence by base turn3 **0.733327**, with no mulligans and without joint land-drop/cast timing; it is **not** the probability of casting Nathan T3. Conditional/tapped sources, opponent colors for Fellwar, land-fetch choices and a 3/2 commander's repeated tax are meaningful. Arena of Glory is a real tempo upgrade but needs {R} upfront and its exerted red; Fire Nation Palace costs {1}{R}, tap before attack and can enter tapped without basic. Nine fetches with seven typed duals make the land package strong, but a fetch cannot find an off-type original dual merely because it makes a desired color.

**Early turns:** T1 one-mana theft creature or Remora; T2 rock, Greaves/Regalia, or protection; T3 Nathan if UBR and safe haste access, otherwise delay for protection. After Nathan attacks, spell permission exists only while his trigger resolves. A tapped-out attacker cannot later spend sorcery-speed mana to cast a chosen stolen spell. Firebending resolves before Nathan if its trigger stacked above, and the mana lasts through combat. Treasure triggers from Don Andres/Gonti/Prosper happen **after** a stolen spell has been cast and cannot retroactively pay its costs. The deck's chief bottleneck is not generic card draw but **mana at the trigger-resolution window**, plus keeping Nathan alive to attack.

**Interaction:** Force of Negation's alternative pitch cost is only available on opponent turns, not your Nathan attack; Guardianship and Swat need commander controlled to be free; Swan Song and An Offer are noncreature counters, so an opposing Oracle creature requires Mana Drain or Force of Will (not in approved list) or other creature-specific interaction. Deadly Rollick handles a creature; Chaos Warp handles diverse permanents; Cyclonic Rift is an asymmetric reset at seven; Blasphemous Act kills your 3/2 Nathan unless protected. Opposition Agent, Dauthi and Notion Thief are disruptive but have commander-independent opportunity cost. Protection/evasion is abundant enough that another evasion aura should not displace trigger doubling.

