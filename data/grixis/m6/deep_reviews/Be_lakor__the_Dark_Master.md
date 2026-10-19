# Be'lakor, the Dark Master — 100-card commander-first deep review

**Status:** engineering-only authored analysis, October 19, 2026, distinct from independent GrokBot Pass C and formal M6 acceptance. NO deck changes, NO new approval or lock manipulation.
**Canonical approved authority:** `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json#Be_lakor_the_Dark_Master` and `refinement/decklists/Be_lakor_the_Dark_Master_Approved_2026-10-13.txt`. Raw approved SHA-256 **`3abc951606a6db2b17ea2aceb471fc2ef4c55e2ef082d49d9140a83b2491155e`**, equals recorded historical hash in registry. Engineering logical hash `lh1:ece0a3ce87a761d863499a0c6f443be756c6d2d43103b27c9d4b99023c303551` is a different format.
**Naming reconciliation:** engineering/tracker `Be_lakor__the_Dark_Master`, canonical `Be_lakor_the_Dark_Master`, both explicitly refer to identical commander `Be'lakor, the Dark Master` and same approved source hash. This is an **identifier alias**, not a second card, deck, or permitted hash overwrite; tracker field `IDENTIFIER_ALIAS_NEEDS_CONFIRMATION` is accurately documented here.

## Commander identity and natural ceiling

Be'lakor is a six-MV (`3UBR`) flying 6/5 Demon Noble. Prince of Chaos draws X and loses X life when Be'lakor ENTERS with X = **Demons you control when the trigger resolves**. Lord of Torment triggers when ANOTHER Demon enters and deals damage equal to **the ENTERING Demon's power**, not Be'lakor's power. Demons entering simultaneously see each other's triggering permanents. Demon density, entering power, cheapening high-MV Demon spells, repeat blink/clone/cheat, life-management and multiple damage receivers are the core identity.
Natural ceiling **optimized Bracket 4** based on a slower 6-MV commander; the deck has explosive Rite/Panharmonicon/Spark Double finite wins, but paying for six-mana commander plus keeping it in play under removal/graveyard hate reduces consistent high-end combo access. Not a justification to abandon Demon tribal for interchangeable Consultation/Thassa Grixis control.

## Full 100-card role audit

Independent approved TXT and Oct 16 canonical per-card Scryfall bulk audit: **100 cards**, **94 distinct card names**, **36 lands**, **28 creature names**, **25 printed Demon creature names** including Be'lakor. Only Island×3, Mountain×2, Swamp×4 are repeated; singleton PASS. All 94 current source names have B/R/U color identity, Commander legality PASS, zero unknown cards, and NO exception. Three approved swaps retained: `Raphael, Fiendish Savior → Dream Devourer`, `Reaper from the Abyss → Doom Whisperer`, `Demonlord Belzenlok → Spark Double`. Historic `Be_lakor_the_Dark_Master_Final_2026-10-13.txt` with Ardyn was superseded; DO NOT audit it as current approved.
36 lands include fetches, original duals, shocks, multiplayer duals, conditional/check duals, Xander's Lounge, tri-color tap lands and nine basics; several ETB-tapped color sources trade tempo for fixing. Sol Ring, Arcane/Fellwar, three Talismans, Rakdos Signet, Ancient Tomb, Dark Ritual, Urza's Incubator, Herald of Slaanesh, Heartless Summoning, Ancient Cellarspawn and Rakdos Lord of Riots make high-MV Demons more castable, though discount conditions vary. No measured turn-six UBR percentage or four-player game result is claimed.
25 printed Demons includes Dream Devourer and does NOT include non-Demon Ancient Cellarspawn, non-Demon Spark Double before ETB, or Roaming Throne before it chooses Demon; these conditional types become important for recursion, cast bonuses, Lord entries and Liliana's Contract.

### Every current approved card — 100 copies / 94 name rows

| Source card | Qty | Verified Oracle type | Commander-specific function, weakness or retained tradeoff |
|---|---:|---|---|
| Be'lakor, the Dark Master | 1 | Legendary Creature — Demon Noble | Commander; six-mana flying Demon, ETB draws and loses life equal current Demon count at RESOLUTION. OTHER Demon entries deal that entering Demon's power as damage. Own ETB doesn't trigger its own Lord. |
| Abyssal Harvester | 1 | Creature — Demon Warlock | Demon grave-cloner; tap exiles grave creature card put there THIS turn, creates copy as Nightmare additional type, then exiles other Nightmare tokens. |
| Ancient Cellarspawn | 1 | Enchantment Creature — Horror | NONDEMON Horror cost-reducer 1 generic for Demon/Horror/Nightmare spells; discounted cast causes target life-loss, but own ETB doesn't trigger Lord. |
| Ancient Tomb | 1 | Land | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Arcane Signet | 1 | Artifact | Color fixing/acceleration for 6MV commander; not itself Demon trigger. |
| Archfiend of Depravity | 1 | Creature — Demon | Large flying Demon, opponents end steps reduce their creature boards to two, commander damage enabler. |
| Archfiend of Despair | 1 | Creature — Demon | Demon and life-gain prevention; at each end step each opponent loses additional life equal to life lost this turn, not another DAMAGE event. |
| Badlands | 1 | Land — Swamp Mountain | Fetchable dual/shock; fast UBR color with shock life tradeoff. |
| Balor | 1 | Creature — Demon | Demon trigger source: Flying Whenever this creature attacks or dies, choose one or more. Each mode must target a different player. • Target opponent draws three c |
| Bedevil | 1 | Instant | Board/stack interaction; key protection of expensive tribal engine. |
| Blasphemous Act | 1 | Sorcery | Board/stack interaction; key protection of expensive tribal engine. |
| Blood Crypt | 1 | Land — Swamp Mountain | Fetchable dual/shock; fast UBR color with shock life tradeoff. |
| Bloodletter of Aclazotz | 1 | Creature — Vampire Demon | Demon; during your turn opponents' LIFE LOSS is doubled as replacement, even if source deals normal damage. Doesn't deal damage again. |
| Bloodstained Mire | 1 | Land | Fetch typed dual/shock; fixing at life cost. |
| Bloodthirster | 1 | Creature — Demon | High-power Demon, extra combat after damage to PLAYER, cannot attack player it already attacked this turn, finite opponents. |
| Bojuka Bog | 1 | Land | Enters tapped black land, targeted opposing graveyard exile, source mana tempo cost. |
| Burning-Rune Demon | 1 | Creature — Demon Berserker | Large Demon, ETB selects two distinct cards to hand+grave as opponent chooses, fuels reanimation. |
| Cavern of Souls | 1 | Land | Chosen Demon offers uncounterable Demon creature spells and tribal colored mana, but pips restricted for noncreature. |
| Chaos Defiler | 1 | Artifact Creature — Demon Construct | Artifact Demon; enters OR dies each opponent nominates nonland permanent, random one destroyed; damage from its power when enters under Be'lakor. |
| Chaos Warp | 1 | Instant | Board/stack interaction; key protection of expensive tribal engine. |
| Command Tower | 1 | Land | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Crumbling Necropolis | 1 | Land | Tapped UBR fixing, costs one tempo turn, triome typed when Xander. |
| Cyclonic Rift | 1 | Instant | Board/stack interaction; key protection of expensive tribal engine. |
| Dark Ritual | 1 | Instant | B→BBB temporary acceleration, helps deploy big Demons but not permanent fixing. |
| Deadly Rollick | 1 | Instant | Board/stack interaction; key protection of expensive tribal engine. |
| Deflecting Swat | 1 | Instant | Board/stack interaction; key protection of expensive tribal engine. |
| Demon of Dark Schemes | 1 | Creature — Demon | Demon ETB -2/-2 to all OTHER creatures; can kill token support, energy from other creature deaths enables tapped creature reanimation. |
| Demonic Counsel | 1 | Sorcery | Non-Demon support: Search your library for a Demon card, reveal it, put it into your hand, then shuffle. Delirium — If there are four or more card types a |
| Demonic Tutor | 1 | Sorcery | Non-Demon support: Search your library for a card, put that card into your hand, then shuffle. |
| Spark Double | 1 | Creature — Illusion | Approved four-mana Illusion, copies OWN commander as NONLEGENDARY Be'lakor with +1/+1, triggers commander's Lord and own Prince; not a Demon in library/grave. |
| Dragonskull Summit | 1 | Land | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Drowned Catacomb | 1 | Land | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Exotic Orchard | 1 | Land | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Feed the Swarm | 1 | Sorcery | Board/stack interaction; key protection of expensive tribal engine. |
| Fellwar Stone | 1 | Artifact | Color fixing/acceleration for 6MV commander; not itself Demon trigger. |
| Fierce Guardianship | 1 | Instant | Board/stack interaction; key protection of expensive tribal engine. |
| Foreboding Ruins | 1 | Land | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Ghostly Flicker | 1 | Instant | Blinks TWO artifact/creatures/lands controlled, can create new Demon ETB/Lord and new Be'lakor Prince triggers, but can remove stolen/reanimated commitments. |
| Great Unclean One | 1 | Creature — Demon | Demon; end step opponents lose 2 and creates 1/3 Demon tokens for opponents with less life than you; each token creates Lord damage while commander present. |
| Gyruda, Doom of Depths | 1 | Legendary Creature — Demon Kraken | Demon Kraken ETB mill4 from each player and recover ONE even-MV creature; Companion restriction irrelevant as regular 99-card occupant. |
| Heartless Summoning | 1 | Enchantment | Creature spells cost 2 generic less; creatures -1/-1 continually, decreasing Be'lakor Lord power damage and sometimes killing 1/1 tokens. |
| Herald of Slaanesh | 1 | Creature — Demon | Demon cost reduction 2 generic and haste to other Demons, power-on-entry attack pressure; printed Demon eligible Lord. |
| Island | 3 | Basic Land — Island | BASIC ×3: colored mana and fetchable typed source. |
| Kardur, Doomscourge | 1 | Legendary Creature — Demon Berserker | Demon (despite body being Orc Warrior in some prints? audit check): ETB enemy compelled attacks and later death drain, party control. |
| Kindred Discovery | 1 | Enchantment | Demon-type ETB and attacks mandatory draw, burst can overdraw/deck-out; Demon type must be chosen. |
| Liliana's Contract | 1 | Enchantment | Etb draw4 lose4 and upkeep win with FOUR or more Demons of DIFFERENT names, not five Be'lakor tokens named alike. |
| Lord of Change | 1 | Creature — Demon | Demon ETB draw3, meaning multiple draw packages can deplete deck; ward3 and flying. |
| Luxury Suite | 1 | Land | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Mana Drain | 1 | Instant | Non-Demon support: Counter target spell. At the beginning of your next main phase, add an amount of {C} equal to that spell's mana value. |
| Molten Echoes | 1 | Enchantment | As enters choose Demon; NONtoken Demon ETB creates extra token copy exiled end step; legendary Demon copies subject legend rule. |
| Morphic Pool | 1 | Land | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Mountain | 2 | Basic Land — Mountain | BASIC ×2: colored mana and fetchable typed source. |
| Orcus, Prince of Undeath | 1 | Legendary Creature — Demon | Demon with X-modal recursion/creature board impact, needs red/black mana and variable payment. |
| Otawara, Soaring City | 1 | Legendary Land | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Panharmonicon | 1 | Artifact | ETB triggers generated by creature or artifact ETB happen an additional time, including Be'lakor Lord and Prince; doubling also doubles life loss. |
| Path of Ancestry | 1 | Land | Tapped UBR land; scry triggered when Demon creature SPELL cast with commander type (not cheated onto battlefield). |
| Patriarch's Bidding | 1 | Sorcery | EVERY player names creature type; all cards of all chosen types return simultaneously. Demon mass entries create many Lord triggers but opponents may recover. |
| Polluted Delta | 1 | Land | Fetch typed dual/shock; fixing at life cost. |
| Rakdos Signet | 1 | Artifact | Color fixing/acceleration for 6MV commander; not itself Demon trigger. |
| Rakdos, Lord of Riots | 1 | Legendary Creature — Demon | Demon spell-cost reducer requires prior opponent loss THIS turn to cast, can discount high-cost Demons in second main phase. |
| Rakdos, Patron of Chaos | 1 | Legendary Creature — Demon | Demon trigger source: Flying, trample At the beginning of your end step, target opponent may sacrifice two nonland, nontoken permanents of their choice. If they d |
| Rakdos, the Showstopper | 1 | Legendary Creature — Demon | Demon trigger source: Flying, trample When Rakdos enters, flip a coin for each creature that isn't a Demon, Devil, or Imp. Destroy each creature whose coin comes  |
| Dream Devourer | 1 | Creature — Demon Cleric | Approved cheap Demon/foretell staging; printed power zero means normally NO Lord damage on entry. Foretell costs 2 to exile from hand in own turn, cast on a later turn. |
| Reanimate | 1 | Sorcery | 1-mana reanimation from ANY graveyard, life loss equal CREATURE card's mana value, creates Demon entry Lord trigger if Be'lakor present. |
| Doom Whisperer | 1 | Creature — Nightmare Demon | Approved five-mana 6/6 Demon; contributes six entering damage, pays 2 life to surveil 2 for reanimation selection at risk to life budget. |
| Reflections of Littjara | 1 | Enchantment | Demon SPELL CAST copies spell; copy permanent resolves as token and may die to legend rule; not triggered from reanimation. |
| Rite of Replication | 1 | Sorcery | Kicked on Be'lakor creates five legendary 6/5 Be'lakor tokens simultaneously; 25 Lord triggers, 150 damage potential; five Prince triggers count SURVIVING Demons at resolution. |
| Roaming Throne | 1 | Artifact Creature — Golem | Choose Demon on ETB, becomes Demon, doubles triggers of OTHER Demon creatures, including Be'lakor Lord and Prince. Its entry itself gives Lord trigger. |
| Rune-Scarred Demon | 1 | Creature — Demon | Large Demon, ETB tutor any card to hand (Panharmonicon doubles), triggered Lord on entry. |
| Scalding Tarn | 1 | Land | Fetch typed dual/shock; fixing at life cost. |
| Sneak Attack | 1 | Enchantment | Pay red to cheat Demon from HAND with haste then end-step sacrifice; creates an immediate Lord trigger and attack at resource cost. |
| Sol Ring | 1 | Artifact | Color fixing/acceleration for 6MV commander; not itself Demon trigger. |
| Sower of Discord | 1 | Creature — Demon | Demon; choose two players on ETB, when one is dealt DAMAGE, the other loses that much LIFE; doesn't infinitely ping back. |
| Steam Vents | 1 | Land — Island Mountain | Fetchable dual/shock; fast UBR color with shock life tradeoff. |
| Sulfur Falls | 1 | Land | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Sunken Hollow | 1 | Land — Island Swamp | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Swamp | 4 | Basic Land — Swamp | BASIC ×4: colored mana and fetchable typed source. |
| Talisman of Creativity | 1 | Artifact | Color fixing/acceleration for 6MV commander; not itself Demon trigger. |
| Talisman of Dominance | 1 | Artifact | Color fixing/acceleration for 6MV commander; not itself Demon trigger. |
| Talisman of Indulgence | 1 | Artifact | Color fixing/acceleration for 6MV commander; not itself Demon trigger. |
| Toxic Deluge | 1 | Sorcery | Board/stack interaction; key protection of expensive tribal engine. |
| Training Center | 1 | Land | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Underground Sea | 1 | Land — Island Swamp | Fetchable dual/shock; fast UBR color with shock life tradeoff. |
| Unholy Annex // Ritual Chamber | 1 | Enchantment — Room // Enchantment — Room | Room end step draws, causes Demon-dependent opponent loss and life gain; unlocking Ritual Chamber creates 6/6 Demon token => 6 Lord damage. |
| Urborg, Tomb of Yawgmoth | 1 | Legendary Land | Mana/color-tempo slot supports six-MV commander and black heavy Demons. |
| Urza's Incubator | 1 | Artifact | Choose Demon: reduces generic 2 for Demon creature spells, mana intensive setup but scale. |
| Valgavoth, Terror Eater | 1 | Legendary Creature — Elder Demon | High-MV lifelink Demon; exiles would-be opponent graveyard cards, allows cast those on own turn by paying life instead of mana cost. |
| Vampiric Tutor | 1 | Instant | Non-Demon support: Search your library for a card, then shuffle and put that card on top. You lose 2 life. |
| Vilis, Broker of Blood | 1 | Legendary Creature — Demon | High-power Demon and life-payment conversion; draws cards WHEN YOU LOSE LIFE, potentially mandatory massive extra draws from Be'lakor and deck-out. |
| Volcanic Island | 1 | Land — Island Mountain | Fetchable dual/shock; fast UBR color with shock life tradeoff. |
| Warstorm Surge | 1 | Enchantment | Separate creature ETB power damage for every own creature including nonDemons; two sources if own Demon arrives with commander. |
| Watery Grave | 1 | Land — Island Swamp | Fetchable dual/shock; fast UBR color with shock life tradeoff. |
| Whip of Erebos | 1 | Legendary Enchantment Artifact | All own creatures lifelink to offset commander ETB life loss; activated sorcery-speed Demon reanimation exiles card on leaving/endstep. |
| Xander's Lounge | 1 | Land — Island Swamp Mountain | Tapped UBR fixing, costs one tempo turn, triome typed when Xander. |

## Candidate pool and competing cuts

Source pool from `data/grixis/m6/optimizer/belakor-the-dark-master.json`: 267 Pass A candidate pairs, 3 Pass B technical pairs, zero identical agreements; earlier approved dossier independently screened 100 named candidates. EDHREC optimized/Demons distribution provides **observed community inclusion**, not evidence any proposed replacement wins. Significant named competing cuts:

| Candidate → exact cut | Value and failure mode | Determination |
|---|---|---|
| **Varragoth, Bloodsky Sire → Archfiend of Despair** (M5 A) | Varragoth is a cheap Demon tutoring card to library TOP via attack/boast at sorcery-speed offensive exposure; power is low so entering Lord damage small. Archfiend stops life gain and doubles each opponent's total turn life loss at end step, multiplying core commander damage. | **REJECT**: cannot remove a Demon damage multiplier for a slower topdeck tutor without proof. |
| **Varragoth → Sower of Discord** (M5 A) | Cheap Demon and repeatable tutor, but Sower is a Demon amplifier linking player life losses to selected combat/ETB damage and immediate Be'lakor power damage. | HOLD only in poor-search metagames; no provable net improvement. |
| **Abhorrent Overlord → Sower of Discord** (M5 A) | Overlord is a high-MV Demon with devotion-based Harpy token army, but Harpies aren't Demons (no Lord triggers) and upkeep sacrifice can consume creatures. Sower provides immediate copy-sensitive damage propagation at lower mana. | REJECT ranked exact swap. |
| **Abyssal Persecutor → Sower of Discord** (M5 A) | Cheap big Demon increases damage ceiling but prevents controller from winning until removed; not enough built-in sacrifice outlets to guarantee safe exit. Sower has no loss-lock. | REJECT risk. |
| **Bloodcrusher of Khorne → Archfiend of Despair** (M5 A) | Large Demon/combat payoff, but expensive and must reach combat; Archfiend converts Be'lakor ETB direct damage without attacking and prevents life gain. | REJECT pair. |
| **Ancestral Statue → Roaming Throne** (M5 A) | Bounce/loop potential with another ETB effect but Statue is NOT Demon, while Throne named Demon doubles commander triggers and itself triggers Lord on entering. | REJECT loss of central trigger multiplier. |
| **Brainstorm → Unholy Annex // Ritual Chamber** (M5 B) | Cheap card selection is efficient but doesn't generate recurring end-step card flow/lifegain or a 6/6 Demon token; that Demon generates six Lord damage. | REJECT. |
| **Dimir Signet → Fellwar Stone** (M5 B) | Signet offers deterministic UB after paying1; Fellwar usually produces needed UBR in four-player game at no activation mana, enabling six-MV commander. Neither creates Demon ETB. | HOLD conditional on opponent lands; no compelling default swap. |
| **Temple of the False God → Otawara, Soaring City** (M5 B) | Temple dead without five lands, adds only colorless on an already six-MV triple-colored commander; Otawara supplies blue earlier and versatile Channel bounce. | REJECT. |
| **Sakashima of a Thousand Faces / more Be'lakor clones → generic interaction or Demon slots** (off-ranking context) | Additional stable nonlegendary commander copy can dramatically raise next Demon entry burn, but is NOT a Demon from hand, requires commander to survive and overconcentrates clone package already containing Spark Double, Rite, Molten Echoes and Reflections. | HOLD until named objectively weakest cut and removal-heavy tests. |
| **Curse-Marred Demon → costly marginal Demon** (EDHREC new inclusion) | Appears in current observational commander cohorts, but Oracle/interaction, legality and exactly superior approved cut not independently established here; DO NOT manufacture card text. | UNRESOLVED, not recommended. |

## Oracle, legality and rules

1. **Prince/Lord** are distinct triggers. Own Be'lakor entering causes only its Prince (except OTHER Be'lakor already present can see it). X Demon count checked when Prince RESOLVES. Lord of Torment needs another Demon entering; the source is Be'lakor but DAMAGE is dealt by entering Demon, even if that entering Demon later leaves, using last-known power.
2. **Kicked Rite** when target is your original 6-power Be'lakor: five legendary Be'lakor copies enter simultaneously. Original sees five others -> FIVE Lord triggers. Each of five incoming copies sees four of the other incoming copies -> 5×4 = TWENTY additional Lord triggers. **25 Lord triggers × 6 power = 150 damage** before pumps, replacement effects, protection or target changes, allocated among LEGAL targets as triggering events are put on stack. State-based legend rule removes all but one of six legendary Be'lakors before those triggers are put on stack; dies/leaves afterward doesn't erase existing triggers, and power via last known info remains six absent modifiers.
3. There are FIVE additional Prince triggers (one per entering copy); if Be'lakor is the ONLY Demon survivor after legend cleanup and no other Demons, each Prince draws **one** card and loses **one** life, total five cards/life. Do NOT claim 30 cards drawn just because six Demons briefly entered. If two other distinct Demons survive, X becomes three, etc. Panharmonicon/Roaming Throne can add Prince triggers and forced life loss; be careful with Vilis mandatory draw and decking.
4. **Spark Double** only copies a creature you control when entering, normally as NONLEGENDARY Be'lakor with +1/+1 counter: original Lord sees an additional Demon (new 7/6 assuming no other modifiers), while copied Be'lakor Prince counts all Demons on resolution. A nonlegendary copy survives alongside original, allowing both Lords on future Demon entries. Spark Double itself is Illusion card in grave; cannot be returned by `Patriarch's Bidding` if only Demon chosen unless an effect changes types in grave.
5. **Panharmonicon** doubles Lord due to creature/artifact ENTER and Prince due to creature ENTER; it also duplicates the attached life-loss. **Roaming Throne** choosing Demon becomes that creature type on battlefield and doubles OTHER Demon creature triggered abilities; does not double its OWN abilities from self. Throne's ETB as Demon can trigger already-existing Lords.
6. **Molten Echoes** triggers only from NONtoken Demon entry; generated Demon TOKEN enters and causes Lords, but does NOT generate another Molten Echoes token by itself. Legendary-copy tokens from Molten Echoes encounter legend rule but still trigger enter effects. **Reflections of Littjara** copies DEMON spell when cast, not reanimation or Token-entry; permanent spell copy becomes token on resolution.
7. **Liliana's Contract** wins at beginning own upkeep only with FOUR+ Demons having different names; multiple tokens named Be'lakor don't independently count, even if legend rule waived. A single Roaming Throne named Demon contributes one distinct Golem name while on battlefield. Deck risk: Prince draw/life loss and Liliana ETB draw four are not optional.
8. **Whip of Erebos** grants creature lifelink. Damage dealt by ENTERING Demon through Lord is creature-source damage and gains life for controller if creature has lifelink on battlefield or last-known information preserves lifelink; can offset life cost. Whip resurrected creature exiles at next end step or on leaving, so cannot simply recycle in grave. **Reanimate** costs life equal to printed mana value, regardless of discounts from Incubator/Heartless.
9. **Archfiend of Despair** is end-step life-loss trigger based on opponent life lost that turn (not damage), can close game after Demon ETB. **Bloodletter of Aclazotz** replaces opponent life loss on YOUR turn with twice as much. **Sower of Discord** propagates damage as LIFE LOSS to other player, not secondary damage, preventing an infinite mirror of two Sow-players.
10. **Heartless Summoning** makes each creature -1/-1, including 1/3 Plaguebearer Demon tokens (become 0/2), still Demon and may have zero Lord damage. It reduces cost of cast creatures including nonDemons and affects current power continuously. **Dream Devourer** starts 0 base power, so unless foretell granted +2/+0 or other pump on entry, Lord damage zero, despite being Demon.
11. **Abyssal Harvester** targets a grave creature CARD put there THIS turn; token copies retain Demon type ONLY if original copy's creature types include Demon, plus Nightmare. Other Nightmare tokens are exiled, limiting persistent Demon multiplication. **Ancient Cellarspawn** is Horror, not Demon, although discounts Demon and triggers life-loss from spell mana discounts.
12. **Patriarch's Bidding** returns creature cards of each player's chosen type for EVERY PLAYER, not only controller's Demons; mass Demon ETBs trigger multiple Lords (simultaneous event sees all Demons). Can revive enemy threats, and graveyard hate/countermagic can prevent payoff.
13. **Gyruda** printed Companion wording has restriction only if Gyruda chosen as outside-deck companion; as a normal Demon in 99, no even-cost deck-building constraint. Its ETB mines FOUR cards from EACH library but only one chosen even-MV creature enters.
14. Printed Demon type, copied type, legend rule, last known power and card legal targets are material. No newly identified Commander color or ban violation from Oct15 audit. This report uses archived 94-row per-card Oracle evidence, not a claim of 94 new Scryfall network queries. No project-authorized exceptions used.

## Finite sequencing and adversarial scenarios

**A — base Rite proof:** Have exactly original Be'lakor on battlefield and 5UUUU? (Rite base 2UU + kicker 5 = **7UU?** Correct payment is `{2}{U}{U}` plus `{5}` = **{7}{U}{U}**, total 9 mana). Cast kicked Rite targeting own Be'lakor. Five 6/5 token copies enter; 25 Lord damage triggers and 5 Prince triggers occur. Choose one legendary to remain; five original/copies total die to legend. Assign legal damage targets as abilities go on stack, usually all opposing players (each 40 starting life) can be killed by 150 total damage if no responses, protection or prevention. Need distribute enough across each opponent; not one forced player target. If only one Demon remains before Prince resolution, five separate draws and five life lost. No benefit from token bodies staying once legend cleanup happens.
**B — commander removal and protection:** Opponent destroys Be'lakor in response to kicked Rite before resolution: Rite targeted object becomes illegal and fizzles unless target is still legal; no five token copies. If opponents destroy source Be'lakor AFTER all five copy tokens entered, already-queued Lord triggers persist, using appropriate last-known info. If opponent controls hexproof or damage prevention, legal targets and actual kills change.
**C — nonlegendary clone:** With Be'lakor already in play, cast Spark Double and choose Be'lakor to enter as its nonlegendary copy. Original Be'lakor sees another Demon enter and deals copied 7-power Spark damage if plus-one counter applies; copied Be'lakor Prince triggers and draws/loses life based on at least two Demons, absent other changes. Next Demon entry triggers BOTH Lords, each causing entering Demon power damage. Opponent removing source before it enters may prevent copying the planned card; no card type shortcut in grave.
**D — graveyard-revival burst:** With Be'lakor plus two distinct large Demon creature cards in YOUR grave, cast Patriarch's Bidding selecting Demon. Opponents may choose Goblin/Elf/other types and recover their own cards. On resolving, two Demons simultaneously enter, Be'lakor generates two Lord triggers to valid targets, then any Demon ETB additional benefits; Roaming Throne/Panharmonicon can duplicate conditional triggers. If Rest in Peace/Cage is active, plan fails; if Be'lakor isn't present, returning Demons provides bodies but no Be'lakor damage.
**E — life/deck overdraw:** Be'lakor enters with five other Demons under your control. Prince draws six cards and you lose six life, unless doubled by Panharmonicon for twelve cards/life. With Vilis on battlefield, loss-life trigger can draw an additional six per event, reaching 12 or 24 total draws; at low life total or low library count this can kill you. Whip lifelink benefits DAMAGE from your Demon but cannot negate life-loss-only Prince. Sequencing Whip/Archfiend/Bloodletter matters.
**F — Demon density vs rank:** Replace Sower of Discord with top-ranked Varragoth: four-mana/tutor timing? Varragoth costs 2B and needs attack and boast to tutor top; if removed before combat, no card. Existing Sower immediately triggers Be'lakor on its Demon entry and subsequent damage propagation to second player; it also promotes table-wide lethal targeting. No evidence from heuristic alone that extra topdeck access outweighs Demon burn.
**G — adversarial artifact/blink/counterplay:** Vandalblast can destroy Incubator/Panharmonicon/Sol Ring, severely delaying six-MV commander. Torpor Orb stops Be'lakor Prince and Lord triggered by Demon entering (since triggered by creature ETBs) and Doom/Rune-Scarred ETBs, so protection/removal matters. Rest in Peace/Cage stops recursion, not Demons cast from hand. Arcane Denial/Mana Drain can stop Rite; killing original target in response fizzles it. A conventional Wrath after board establishment wipes the ability sources; prioritize retaining appropriate counter/reanimation interaction.

## Conclusions and unresolved evidence

**STRATEGIC HOLD**: the exact approved 100 concentrates 25 printed Demons, high-impact power-dependent Lord triggers, Rite/clone/ETB multipliers, life/recursion and adequate UBR land count. The top M5 alternatives mostly cut key Demon burn multipliers or core Roaming Throne, damaging Be'lakor identity. Varragoth is plausible if tutors are needed but weaker immediate commander damage; Curse-Marred Demon is observed in community list but unverified as a specific net-positive replacement and therefore is NOT a recommendation. All proposed differences remain UNAPPLIED. Neither historical approvals nor independent Pass C altered.
**Unresolved evidence:** no paired multiplayer match-seed tests, no turn-four/six colored mana source rate, no real opponent-response deck-win estimate, no complete authenticated Oracle for new 2026 Curse-Marred Demon in this review, no separate exact-card external match simulation. M5 rank is not deck optimization proof. Historical Ardyn version remains superseded. Keep user approval/lock authority intact.

## Source and test receipts

- Approved source `refinement/decklists/Be_lakor_the_Dark_Master_Approved_2026-10-13.txt` on `corymstover/grixis-commander-encyclopediaGPT/main`, SHA-256 `3abc951606a6db2b17ea2aceb471fc2ef4c55e2ef082d49d9140a83b2491155e`, original lock `refinement/approvals/Be_lakor_the_Dark_Master_Approved_2026-10-13.md` and state overrides.
- October 16 per-card source `refinement/verification/retrospective_1_to_8/Card_Verification_Be_lakor_the_Dark_Master_2026-10-14.csv` (Scryfall bulk updated Oct15), 94 current legal Oracle records and zero unexplained identity failures. Original `refinement/evidence/Be_lakor_the_Dark_Master_Approval_Gate_Dossier_2026-10-13.md` and `data/grixis/blueprints/belakor-the-dark-master.json`.
- M5 optimizer `data/grixis/m6/optimizer/belakor-the-dark-master.json`: 267 A, 3 B, 0 exact agreements; EDHREC optimized Demon observational evidence https://edhrec.com/commanders/belakor-the-dark-master/optimized/demons ; source is inclusion not gameplay accuracy.
- Rules for simultaneous ETBs, legend rule and LKI https://blogs.magicjudges.org/rules/comprehensive-rules/ ; targeted independently discussed Be'lakor kicked Rite 25-trigger/5-draw baseline https://www.reddit.com/r/mtgrules/comments/y43wua/ . Original Oracle reference https://mtg.wtf/card/40k/6/Be-lakor-the-Dark-Master.
- CI must pass at authored review and final exact PR head with source/queue tests; no independent GrokBot Pass C, no M6 acceptance and no user-owned canonical edit.
