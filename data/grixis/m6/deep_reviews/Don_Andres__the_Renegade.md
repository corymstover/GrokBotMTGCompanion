# Don Andres, the Renegade — authored comprehensive deep review #14

**Date:** 2026-10-19. **Authorship:** primary ChatGPT engineering review; NOT independent GrokBot Pass C, NOT final M6 phase certification, NOT user authorization to revise a locked deck.

## 1. Authority and no-mutation boundary
- **Source identity receipt:** `Don_Andres__the_Renegade` is the same exact canonical deck ID and engineering registry ID at tracker index 13 (human review #14). Approved SHA is bound to this exact ID; source_identity_discrepancy = NONE.
- Canonical approved/locked file: `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Don_Andres_the_Renegade_Approved_2026-10-14.txt`. Canonical `main` SHA at start `a7c73533ac864eccabd591fae7cd805746bfbfe0`; Git blob `1d20d4887565d2765f914ea0a9c33a14d9df03f2`; approval/complete-gate SHA-256 `a6022fddd295d7c671690fbce5e25dc6fed47ca7fa77bf1d8a86ebadb2d927bb` (sourced, not newly independently recomputed from GitHub HTTP bytes).
- `state/current_deck_overrides.json` currently records APPROVED/LOCKED, explicitly approved Oct14. The October 14 gate `refinement/verification/don_andres_the_renegade_2026-10-14/gate_output/Don_Andres_the_Renegade_2026-10-14_Complete_Gate.json` PASSED current Commander legality, Oracle/rules/color identity, count, and zero exceptions. Prior baseline SHA `5013e0b0b035880e74f5395e55115a58eb3f60ad922cd4bd29670d5f45d0ed2e` is NOT the locked approved deck. Engineering logical hash `lh1:012d9c8c9f3127dbfc1ed86dbd8db88ac5f00ee810f841c90a74e5d385faff48`.
- Independent strict TXT quantity/name parser now confirms **100 physical cards, 99 distinct names, 35 land copies across 34 different land names (only Island×2 repeats), 65 nonland cards including commander**. Table below gives a named commander-role evaluation for all 99 entries. This is a fresh structural count; no new live all-card Scryfall cache/Oracle sweep was run, so full legality support is the dated exact-SHA gate. Source-identity discrepancy NONE; no companion or project exception.

## Commander identity and natural ceiling
**Don Andres, the Renegade** is `{1}{U}{B}{R}` 4/3 Vampire Pirate. His static ability makes a creature **controlled by you but OWNED by another player** +2/+2, menace, deathtouch and Pirate in addition to other types. His trigger gives TWO **TAPPED** Treasures whenever YOU CAST a **NONCREATURE** spell you do **NOT OWN**. Separate mechanisms: creatures you steal as permanents get the buff, spells actually cast from enemy cards provide Treasure if noncreature. Merely exiling a card, directly putting a permanent into play, casting an opponent-owned CREATURE, casting your OWN card from exile, or putting a copy of a spell you own on the stack does **not** cause that triggered Treasure production. The owner of a spell COPY you create is you, even if it copies an opponent's card, per the commander card rulings.
**Natural realistic power ceiling: Bracket 4 — Optimized**, Archidekt tags **Theft / Pirates / Treasure**. Strength hinges on the opposing decks' creature quality, permission windows, stolen mana payments and combat connection. On-theme engine intentionally includes Ragavan/Breeches/Black Cat/Court/Gonti/Jhoira/Thief, stolen Pirates fueling Kindred Discovery/Malcolm/Beckett, and mass-theft Insurrection. No pivot to generic Grixis goodstuff or deterministic unrelated cEDH win.
**Important caveats:** Don is 4MV with three distinct colored pips and only 35 lands; tapped Treasures are not an immediate recast refund. Several theft engines cost 5–8 MV or need an opponent upkeep/attacker contact. Opponents may remove Don before borrowed creatures connect or steal monarchy. Avoid blanket claims of turn-four setup or measured win percentages.

## Full 100-card role audit

| Exact approved card | Quantity | Individual role and specific strategic cost |
|---|---:|---|
| Don Andres, the Renegade | 1 | Commander. Controlled opponent-owned creatures get +2/+2, menace, deathtouch and Pirate type. Casting opponent-owned NONCREATURE spells makes TWO TAPPED Treasure; never triggers on stolen creature casts or own spells. |
| Admiral Beckett Brass | 1 | Counts THREE Pirates dealing combat damage to the same player for an end-step steal; Don makes stolen creatures Pirates, so multi-source connections are the gate. |
| Ancient Tomb | 1 | 2 generic mana for self 2 damage; accelerates expensive engines but not UBR |
| Animate Dead | 1 | Reanimate opponent-owned creature from their graveyard and it receives Don buff; own Aura spell casting is not a stolen-card cast. |
| Arcane Heist | 1 | Instant/sorcery theft pathway; Don triggers only upon actually casting a spell owned by opponent, not copying a spell you own. |
| Arcane Signet | 1 | Reliable early UBR fixing; key to casting 1UBR commander. |
| Badlands | 1 | Untapped BR dual fetchable by black/red fetches |
| Black Market Connections | 1 | Card/Treasure/Changeling each upkeep at own life cost; independent repeatable resource access, not itself opponent-card ownership. |
| Blasphemous Act | 1 | Very efficient sweeping damage when crowded; can destroy your stolen army and Don. |
| Blood Crypt | 1 | BR shock; untapped costs 2 life |
| Bloodstained Mire | 1 | Fetches typed Swamp/Mountain duals or triome |
| Brainstealer Dragon | 1 | Seven-mana recurring opponent-deck exile theft, payoff delayed until end step; major top-end congestion. |
| Breeches, Brazen Plunderer | 1 | Pirate combat-damage exiled-card access; requires Pirate connecting with player. |
| Breeches, Eager Pillager | 1 | Pirate attack modes provide Treasure/goad/discard-value tempo; relevant attack density, not arbitrary Pirate body. |
| Mana Drain | 1 | UU counterspell, next main phase colorless for Etali/Insurrection; good strategic interaction. |
| Cavern of Souls | 1 | Pirate colored creature casts/cannot counter; color not freely usable for stolen noncreature |
| Chaos Warp | 1 | Red universal permanent answer with opponent reveal/put-into-play downside. |
| Coercive Recruiter | 1 | Pirate ETB grants temporary control/haste to target opposing creature; opponent-owned creature gets Don buff while controlled. |
| Command Tower | 1 | Unconditional untapped UBR |
| City of Brass | 1 | Untapped UBR; 1 self damage on tap |
| Roaming Throne | 1 | Choose Pirate to duplicate Don's cast trigger: FOUR tapped Treasure, while STATIC creature bonus stays +2/+2 once. |
| Cyclonic Rift | 1 | Overload clears opponents' nonlands while maintaining captured army; significant seven-mana investment. |
| Dauthi Voidwalker | 1 | Opponent graveyard replacement/exile and stolen free cast; can prevent Thieving Amalgam owned-creature death triggers. |
| Deadly Rollick | 1 | Commander-conditioned free creature exile keeps Don/Pirates safe and wins tempo. |
| Deflecting Swat | 1 | Free targeted protection with Don; no answer to nontargeting sweeper. |
| Dimir Signet | 1 | 2-mana color fixer, needs 1 input to add UB. |
| Dire Fleet Daredevil | 1 | Casts opponent-owned instant/sorcery from graveyard, so each noncreature cast makes Don tapped Treasure. |
| Misty Rainforest | 1 | Fetches Island-typed duals/triome; one life |
| Etali, Primal Storm | 1 | Attack generates cast opportunities from all libraries; OWN spell casts give no Don Treasure, opponents' NONCREATURE ones do. |
| Exotic Orchard | 1 | Opponents' colors determine available fixing, not guaranteed |
| Feed the Swarm | 1 | Black enchantment/creature answer despite life loss, difficult to replace in Grixis. |
| Fellwar Stone | 1 | Two-mana opponent-dependent fixing, important versus high-curve theft threats. |
| Fierce Guardianship | 1 | Free noncreature counter with commander, protects stolen board. |
| Gilded Drake | 1 | Exchanges control of itself and target opposing creature for 1U; permanently owned-by-opponent stolen creature gains Don buff. |
| Black Cat, Cunning Thief | 1 | Five-mana ETB looks at top nine opponent cards and exiles two face down indefinitely; need cast/play later, not automatically free. |
| Gonti, Night Minister | 1 | Opponent library/card access and theft; independent permission/cost gates, requires actual cast for Don Treasure. |
| Grenzo, Havoc Raiser | 1 | Player damage via your creatures gets goad or opponent-card exile access; must connect and cast within allowed window. |
| Marsh Flats | 1 | Swamp-typed dual/triome fetch, one life |
| Hostage Taker | 1 | Exiles artifact/creature until permission; stolen CREATURE cast does not make Don Treasure, but entering gains buff. |
| Hurl Through Hell | 1 | Removal-exile and later casting of stolen creature; Don boosts creature, no Treasure for casting creature. |
| Insurrection | 1 | 5RRR mass theft untaps creatures, gives haste until end turn; Don boosts all opponent-owned stolen bodies for a lethal Pirate attack. |
| Island | 2 | 2 copies basic U, pays UU Mana Drain; only basic duplicate |
| Izzet Signet | 1 | 2-mana rock, input1 outputs UR; casts commander/counters. |
| Kindred Discovery | 1 | Name Pirate; draws for entering/attacking Pirates, including Don-transformed stolen creature board. |
| Laughing Jasper Flint | 1 | Outlaw count fuels opponent-library exile during upkeep; stolen Pirates are outlaws if Don live. |
| Lightning Greaves | 1 | Shroud/haste protects Don, but shroud prevents own targeting until moved. |
| Thieving Amalgam | 1 | 5BB manifest top card of EACH opponent's library on their upkeep under your control; 2/2 manifests become 4/4 menace/deathtouch Pirates, dying owned-other creatures drains owner2/gains2 if death not replaced. |
| Locke, Treasure Hunter | 1 | Opponent-card access with Treasure/theft synergy; exact text-specific cast payment must be consulted before modeling. |
| Luxury Suite | 1 | Multiplayer usually untapped BR |
| Malcolm, Keen-Eyed Navigator | 1 | Pirate combat damage to players generates Treasure; Don turns borrowed creatures into additional Pirate hits. |
| Mana Confluence | 1 | Untapped UBR costing own life for color |
| Morphic Pool | 1 | Multiplayer UB dual |
| Mountain | 1 | Singleton basic R, limits basics under nonbasic hate |
| Opposition Agent | 1 | Opponents' search becomes card acquisition; stolen noncreature needs actual cast to trigger Don. |
| Otawara, Soaring City | 1 | Blue mana or channel bounce, channel is separate ability |
| Outrageous Robbery | 1 | XBB exiles many cards from one opponent; exile alone provides no Treasure, still need casting permissions/payment. |
| Path of Ancestry | 1 | Always enters tapped UBR, Pirate casts may scry |
| Plargg and Nassari | 1 | Delayed upkeep free spell casting; opponents' noncreature spell cast gives tapped Treasure, random access. |
| Polluted Delta | 1 | Island/Swamp typed dual fetch |
| Praetor's Grasp | 1 | Search opponent library and exile one card for yourself; ownership remains opponent's if cast. |
| Professional Face-Breaker | 1 | Own creatures dealing damage make Treasure; own library exiled cards remain OWN so never qualify Don. |
| Ragavan, Nimble Pilferer | 1 | Cheap player-damage Treasure and opponent-card theft; high upside but must connect. |
| Rakdos Signet | 1 | 2-mana rock input1 adds BR to pay colored requirements. |
| Ramirez DePietro, Pillager | 1 | Pirate combat hit can recover opponent-owned cards from exile/GY; improves with stolen Pirate swarm. |
| Reanimate | 1 | B returns opposing-grave creature under your control, buffed Pirate; Reanimate is OWN spell and no Don Treasure. |
| Thieving Varmint | 1 | Tap pay1 life add 2 mana ONE COLOR restricted to casting spells you don't own; can't pay your own counter or Don. |
| Scalding Tarn | 1 | Island/Mountain typed dual fetch |
| Seize the Spotlight | 1 | Each opponent chooses permanent theft or Treasures; can't guarantee stolen body. |
| Court of Locthwain | 1 | 2BB monarch, upkeep exiles opponent card with enduring play permission; one free exiled spell if you are monarch that turn; stolen noncreature cast creates Treasure. |
| Shipwreck Marsh | 1 | UB needs two other lands to enter untapped |
| Shivan Reef | 1 | Untapped UR pain mana |
| Siphon Insight | 1 | UB opponent-card face-down exiled play permission and flashback; needs actually CAST stolen spell. |
| Smoldering Marsh | 1 | BR typed but tapped absent two basics; only four basics in 100 |
| Sol Ring | 1 | Fast two generic, does not provide UBR pips. |
| Steam Vents | 1 | Fetchable UR shock |
| Stolen Strategy | 1 | Five-mana upkeep exiles top card from EACH opponent; casts not free by default, limited duration. |
| Verdant Catacombs | 1 | Fetches Swamp-typed duals/triome |
| Sulfur Falls | 1 | UR conditional Island/Mountain check |
| Sulfurous Springs | 1 | Untapped BR pain mana |
| Swamp | 1 | Singleton basic B |
| Takenuma, Abandoned Mire | 1 | Black mana/channel self-mill and creature/planeswalker recovery |
| Talisman of Creativity | 1 | 2-mana UR fixing with 1 self-damage for colored. |
| Talisman of Dominance | 1 | 2-mana UB fixing with self-damage, UU counters. |
| Talisman of Indulgence | 1 | 2-mana BR fixing with self-damage. |
| Tasha, the Witch Queen | 1 | Any stolen spell cast gets Demon token, but Don only generates Treasure for NONCREATURE stolen spells; complementary payoff. |
| Wand of Wonder | 1 | 4 mana to deploy + activation, d20 resolves casts of 1–3 exiled opponent instant/sorcery free; each actual cast can make tapped Treasure with Don. |
| Thief of Sanity | 1 | Evasive UB/R attack creature hits player, exiles one of top three and may cast later with any colored mana; must connect. |
| Toxic Deluge | 1 | Sweeper -X/-X at own life, kills stolen Pirates as well as opponents. |
| Training Center | 1 | Multiplayer UR dual |
| Underground River | 1 | UB pain mana |
| Underground Sea | 1 | Fetchable untapped UB dual |
| Vaan, Street Thief | 1 | Thematic theft engine with combat/access timing; source-specific cast steps required for certainty. |
| Vampiric Tutor | 1 | B and 2 life places selected theft/finisher on library, needs draw later. |
| Decadent Dragon // Expensive Taste | 1 | Adventure banks top two opponent cards, Dragon later flies and makes Treasure; opponent-owned noncreature casts trigger Don. |
| Volcanic Island | 1 | Fetchable untapped UR dual |
| Watery Grave | 1 | Fetchable UB shock |
| Xander's Lounge | 1 | Always tapped UBR typed triome; cycling useful flood relief |
| You Find Some Prisoners | 1 | R instant modal artifact removal or temporary exile-card theft; if cast stolen noncreature later, Don makes Treasure. |
| Jhoira, Weatherlight Corsair | 1 | 4BB 4/5 Pirate, ETB/attack puts opponent HISTORIC permanent directly battlefield, you lose its MV in life. Not casting, zero Don Treasure; stolen creature is buffed. |

### Mana, cards, protection, recursion and victory
- **Mana:** 35 lands include Cavern of Souls (Pirate restricted colored mana), Ancient Tomb (colorless only), Path of Ancestry/Xander's Lounge (guaranteed tapped), Smoldering Marsh (only four basics across deck) and multiple typed fetchable duals/shocks; mana acceleration comprises Sol Ring, Arcane Signet, Fellwar Stone, Dimir/Izzet/Rakdos Signets, three Talismans, Varmint (opponent-spell restricted), and the commander's conditional tapped Treasure from opponent noncreature casts. UU Mana Drain and eight-mana Insurrection cannot be assumed from generic-rock count.
- **Card advantage/theft:** Cheap exiling Ragavan, Siphon Insight, Grenzo, Daredevil, Gonti and Thief feed early spells; mid-game Cat, Court, Wand, Outrageous Robbery, Stolen Strategy, Etali, Brainstealer supply fuel at very different costs/timing. Kindred Discovery rewards Pirate attacks and bodies; Black Market Connections and monarch draw provide independent, non-stolen resilience. Spell casting from an opponent is NOT synonymous with controlling a permanent the opponent owns.
- **Interaction:** Free countermagic/deflection and exile (Fierce Guardianship, Deflecting Swat, Deadly Rollick), Mana Drain, Chaos Warp, Feed the Swarm, Cyclonic Rift, two global board wipes. Hostage Taker/Gilded Drake theft may neutralize creatures but are interaction-substitutes only with valid targets and proper response windows. Greaves keeps Don protected but shroud interferes with friendly targeting.
- **Recursion:** Reanimate and Animate Dead specifically have added commander value by taking **other players' graveyard creatures**, unlike returning own stuff. Dauthi Voidwalker can exile graveyard resources before they are reanimated, so source interaction is not uniformly positive.
- **Victory:** Regular stolen+2/+2 menace/deathtouch Pirate combat; Pirate damage-to-Treasure and 3-Pirate Beckett theft; Tasha/other cast payoffs; explosive `{5}{R}{R}{R}` Insurrection steals all available opponent creatures and grants haste, making them Pirates while Don lives. Existing 7MV Dragon/Amalgam and 6MV Jhoira create ceiling but also top-heavy failure states.

## Candidate pool and competing cuts
- M5-derived engineering `data/grixis/m6/optimizer/don-andres-the-renegade.json`: **109 Pass A recommended add/cut pair projections plus 3 Pass B**. Rankings are *discovery*, not measured win-rate lift. Historic October14 author audit already incorporated swaps to Roaming Throne, Mana Drain, Thieving Amalgam, Thieving Varmint, Court of Locthwain, Wand of Wonder, Black Cat, Jhoira and Dragon; all are in NOW-approved 100. Compare against current list, not initial baseline.
- **Bribery → Thieving Amalgam** is the most interesting honest A/B test. `{3}{U}{U}` searches an opponent's entire library for BEST creature, PUTS it under our control (not cast), so Don boosts it immediately. Stronger low-mana certainty at five versus Amalgam's seven. But Amalgam produces an opponent-owned manifested 2/2 on **each opponent upkeep** (with Don, each 4/4 menace/deathtouch Pirate), potentially three per opponent-round and added death drain. Amalgam is an actual recurring theft engine. Do not declare one universally superior. **EVIDENCE-REQUIRED**.
- **Bribery → Jhoira, Weatherlight Corsair** alternative: five-mana searched BEST creature vs six-mana ETB revealing until first **historic permanent**, potentially artifact/legendary/Saga but not necessarily creature, and life lost equal to MV. Jhoira is 4/5 Pirate and repeats on EACH subsequent attack, can gain noncreature historic utility; Bribery only one searched creature. The right slot is opponent-deck dependent. **HOLD AND TEST**.
- **Fallen Shinobi → Thief of Sanity / Thieving Amalgam** (candidate): Ninjutsu onto unblocked creature, if creature deals combat damage to player cast two exiled opponent cards without paying costs; stolen noncreatures trigger Don. Requires unblocked attack, available ninjutsu colored mana and contact; non-Pirate 5MV, competes with more stable 3MV evasive Thief and 7MV repeated manifests. **CONDITIONAL TEST**, not accepted.
- **Xanathar, Guild Kingpin → Brainstealer Dragon / Jhoira:** repeated opponent-top casting each upkeep, shuts chosen opponent casting your turn; six mana and one upkeep delay versus Jhoira immediate historic capture. **HOLD**.
- **Agent of Treachery → Amalgam:** 7MV theft ANY permanent at ETB, potentially draws at 3 stolen permanents, versus Amalgam multiple opponent-owned manifestations each opponent upkeep. One ETB doesn't settle multi-turn result. **HOLD**.
- **Mind's Dilation → Brainstealer Dragon / Stolen Strategy:** 7MV repeat free top opponent casts from opposing first spells each turn; more spell-ownership payoff if opponent noncreatures, but delayed/high-CMC and controlled by opposing casting. **HOLD**.
- **Memory Plunder → You Find Some Prisoners / Hurl Through Hell:** 4MV instant can cast targeted opponent grave instant/sorcery for free, triggers Don on actual cast. Existing one-shot/removal options may cover more board states and one is R-mana artifact interaction. **NOT CLEAR UPGRADE**.
- **Mob Rule → Insurrection** (M5): 2 mana cheaper but captures only creatures on chosen POWER half of board. Don's +2/+2 finisher maximizes total stolen creatures; **KEEP Insurrection**.
- **Captivating Crew → Coercive Recruiter:** repeat temporary stealing costs activation {4} each time vs Recruiter generating steals off Pirates entering; Pirate construction already extensive, so 4-mana activation is significant. **KEEP Recruiter**.
- **Broadside Bombardiers / Captain Storm / Captain Howler → Roaming Throne or Breeches** (M5): decent Pirate standalone cards but cuts erase Don's real doubled Treasure/other Pirate triggers or sources of stolen spells. **REJECT named cuts**.
- **Deadly Dispute → Decadent Dragon // Expensive Taste** (M5 B): generic own-card draw+Treasure vs durable 2 opponent-card bank and flying Dragon treasure body. **REJECT**.
- **Discreet Retreat → Decadent Dragon** (M5 B): four-mana Aura restricted double mana for OUTLAW spells (mostly Pirate creatures, not stolen noncreature instant/sorcery) and extra outlaw draw, versus Dragon's actual opponent-card access. **REJECT**.
- **Tidespout Tyrant → Deadly Rollick** (M5 B): eight-mana unrelated universal bounce threat replacing free exile when commander live is a serious safety/tempo loss, **REJECT**.
- **Generic Bracket-5 tutors/combo or Pirate-only goodstuff → existing theft engine**: not a commander-first lift absent source-paid proof; prevent homogenization.

**Alternative cut priority:** High top-end Thieving Amalgam or Jhoira is defendable testing because high-cost engines compete for mana, but removing either costs a distinct class of theft (recurrent opponent manifests vs recurrent historic permanent). Brainstealer Dragon and Stolen Strategy are also top-end competitors, yet each supplies ongoing opponent noncreature casts; a better cut must have clear model of rate and protection cost. **Don't cut early rocks, Don multiplier Throne, actual stolen spells or theft-enabling Pirates solely because a ranked candidate scores highly.**

## Oracle, legality and rules
1. [Don oracle and rules](https://mtg.wtf/card/lcc/28/Don-Andres-the-Renegade): your spell COPY is owned by you; tokens created by you are your OWN tokens. Opponent-owned creature controlled by you gets buff; opponent-owned NONCREATURE spell you cast gives two **tapped** Treasures. Cast trigger occurs before resolution, doesn't require stolen spell resolving. Creature you cast from opponent library gets static buff on entering, NOT Treasure.
2. [Thieving Amalgam text/rulings](https://mtg.wtf/card/c19/21/Thieving-Amalgam): opponent library is manifested under your control as their owned card, becoming 4/4 menace/deathtouch Pirate under Don. Death (battlefield to grave) triggers owner life loss2/controller gain2. Dauthi Voidwalker's exile replacement of opponent-owned cards entering opponent GY can STOP dies trigger; tokens you created are owned by you and don't count as opponent-owned cards.
3. [Jhoira official printing](https://mtg.wtf/card/frc/8/Jhoira-Weatherlight-Corsair): 2026-10-02 `{4}{B}{B}` 4/5 Human Pirate, ETB/attack reveals until **historic PERMANENT**, puts it directly under our control, we lose life equal MV. Directly put is NOT cast; not necessarily creature, cannot claim unconditional Don boost/Treasure. Opponent's historic target may be low-value and lifeloss painful.
4. [Court of Locthwain](https://mtg.wtf/card/woc/31/Court-of-Locthwain): monarchy grants extra draw at monarch end step and player combat damage can steal it. Upkeep target opponent top card exile, may play card while remains exiled even if court leaves, spend any mana colors. While YOU monarch you may CAST one spell among its exiled cards for free THIS turn. Opponent land may be played as land under rules, not cast, gives no Treasure; noncreature actual cast does.
5. [Black Cat](https://mtg.wtf/card/spm/52/Black-Cat-Cunning-Thief) {3}{B}{B} looks top nine opponent library and exiles two cards facedown (not drawn); play while exiled, any type mana to cast. Casting cost/timing required. [Thieving Varmint](https://mtg.wtf/card/otc/23/Thieving-Varmint) 1B taps/pay1 life for 2 of ONE color only to cast spells NOT owned; can't pay your own counter or activate own Wand.
6. **Roaming Throne/Pirate** doubles Don's triggered NONCREATURE cast Treasure (to FOUR tapped Treasures) not +2/+2 static bonus. `Kindred Discovery` named Pirate sees stolen creatures enter while Don makes them Pirates, if Don is present at relevant timestamp. `Admiral Beckett Brass` demands three Pirate creatures that actually dealt combat damage to SAME player; three total combat damage by one Pirate doesn't suffice.
7. **Insurrection** owns its own red sorcery card; does not trigger Don treasure. Borrows all others' creatures, untaps, grants haste; Don adds +2/+2 menace/deathtouch Pirate statically to only opponent-owned captured bodies. Killing Don before damage strips buff but does not reverse Insurrection's temporary control/haste. Opponents can respond with Fog, commander removal, or untargeted wipes.
8. **Mana realism**: `Cavern of Souls` colored source only cast chosen TYPE creature; UBR from Ancient Tomb/only Cavern cannot cast opponent stolen noncreature. 35 land sources include two always-tapped lands and only four basic copies (Island×2, Mountain, Swamp), and multiple checklands. `Mana Drain` UU, `Insurrection` RRR, `Bribery` UU, `Jhoira` BB; evaluate actual source payment.
9. **Opposing exile/copies:** Own `Professional Face-Breaker` exiles OWN library cards; even though CAST from exile, no Don treasure. `Siphon Insight` exiles OPPONENT card; cast noncreature yields Treasures. `Wand` can cast opponent instants/sorceries free upon resolving activated ability, but not all cards it reveals are automatically cast, and `4,T` activation plus artifact turn timing matter. `Dauthi Voidwalker` ability permits casting selected opponent-owned exiled card at no mana cost, still normal timing restrictions and possible extra costs.

## Finite sequencing and adversarial scenarios
**A — one actual stolen spell.** Don + Throne (named Pirate) already controlled. Cast a real opponent-owned noncreature Siphon Insight card and pay its mana cost. Don triggers TWICE (one normal + one from Throne), each gives 2 tapped Treasure: FOUR tapped Treasure after triggers resolve. Spell can be countered after that; cannot spend those treasures on original cast. If opponent-owned creature instead, no Treasure on cast; later creature becomes boosted Pirate if resolves.
**B — own exile nonbo.** Own Professional Face-Breaker exiles own instant, controller CASTS from exile: zero Don trigger. Opponent-owned instant exiled via Praetor's Grasp and ACTUALLY CAST: Don triggers, two tapped Treasures. Only ownership, not source zone or mana spent, changes result.
**C — manifest round.** Seven-mana Amalgam survives three opposing upkeeps and manifests top card of each opponent (opponent owns card, we control face-down 2/2). With Don alive each is 4/4 menace/deathtouch Pirate. No spell was cast, no Treasure. Killing one by normal destruction sends opponent-owned card to grave, owner loses2/we gain2. With Dauthi Voidwalker exile replacement active, card never dies into grave -> drain doesn't trigger. Removing Don strips 4/4 buffs.
**D — mass borrow finish.** Pay `5RRR` for Insurrection with Don alive, after spell resolves untap opposing creatures, take them, haste, attack; all opponent-owned bodies gain Pirate menace deathtouch and +2/+2. Opponent can remove Don before damage so static bonus disappears, and own Insurrection itself never generated Treasure. Not guaranteed against fog/wipe.
**E — Jhoira vs Bribery opponent shape.** Opponent library contains a high MV NONHISTORIC creature (best theft), a cheaper historic noncreature artifact and assorted other cards. Jhoira at ETB reveals FIRST historic, takes artifact and loses its MV life, producing no Don Treasure or stolen creature buff. Five-mana Bribery can choose nonhistoric creature in that library and directly put it under our control; Don boosts, no Treasure. But Jhoira can repeat on attack, remain Pirate, and steal multiple artifacts/legends beyond creatures; one-shot Bribery can't. Conditional not categorical upgrade.
**F — Pirate combat gate.** Attacking player hits A with two Pirates and a stolen non-Pirate owned by us. Only two Pirates connected => no Admiral Brass qualifying 3, even if 8 total damage. If the third was stolen opponent-owned and Don made Pirate, then three qualify and Beckett can steal a nonland at end step if defending opponent still eligible. Paying only first two Pirate sources can't suffice.
**G — source-paid high-end.** Your available permanents Ancient Tomb, Cavern of Souls named Pirate, Path of Ancestry, Island, Sol Ring have ample generic mana but may lack exact B/U/R for all necessary actions. Thieving Varmint's 2 mana restricted to casting opponent spells can't fund your own Mana Drain, Insurrection or commander; a hypothetical Bribery UU needs actual two blue sources and 5 total. No fabricated on-curve probability.
**H — adversarial sweeper.** Opponent overloaded Vandalblast removes Wand and Sol Ring, Signets, Talismans, all your tapped Treasures but not Don creature; stealing/casting cards next turn may become inaccessible despite a large exiled pool. Opponent Toxic Deluge also removes stolen Pirates and Don at sufficiently high X; commander's static buff is absent after he dies. Reanimate can rebuild stolen creature only if card remains in a graveyard and is legal target.
**I — cast window denial.** Court not monarch, exiles opponent noncreature; controller still has permission for as long as exiled but not free cast until reobtaining monarch. If no actual mana, no spell and no Don Treasure. If opponent casts an instant, that doesn't trigger Don even when opponent owns it; only you casting an unowned spell counts.

**Empirical limit:** nine authored finite rules states are NOT statistically controlled matched gameplay or simulation. No claimed win-rate delta. A follow-up comparing `Bribery→Thieving Amalgam`, `Bribery→Jhoira`, `Fallen Shinobi→Thief of Sanity` would need exact 35-land mana, 3 different opponent threat densities, removal/stack interaction, number of actual opponent noncreature casts, actual Treasure available next turn, permanents controlled per turn, and ownership. Do not automatically apply any proposed cut.

## Conclusions and unresolved evidence
**Verdict: KEEP approved 100 unchanged; evidence-qualified candidate follow-up only.** The deck is commander-first and its two axes remain coherent. Strongest omitted alternative **Bribery** has credible lower-mana immediate top creature theft, but losing three opponent-upkeep manifests each round (Amalgam) or historic permanent ETB+attack repeat (Jhoira) can be an expensive mistake. Falling for automatic `Deadly Dispute` / `Tidespout Tyrant` projected swaps or Pirate-only bodies for Roaming Throne dilutes Don. No evidence establishes a net improvement while retaining power bracket and deck identity.
**Most forceful counterargument:** Against high-end creature decks with substantial removal, Bribery at {3}{U}{U} may be better than Amalgam because it delivers the highest-value opponent creature immediately and avoids a seven-mana permanent needing multiple upkeep laps. The prior review's "zero further changes" is therefore NOT proof of global optimum. Require source-aware controlled test and owner approval before any swap; no edits.
**Integrity:** Exact approved state, hashes, exceptions and locks unchanged; 62/62 historical M6.4 narrow count separate; no independent Pass C or M6 certification. Reviewer evidence does not claim full Oracle recertification beyond Oct14 dated gate.

## Source and test receipts
- [Canonical approved Don Andres deck](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/a7c73533ac864eccabd591fae7cd805746bfbfe0/refinement/decklists/Don_Andres_the_Renegade_Approved_2026-10-14.txt), Git blob `1d20d4887565d2765f914ea0a9c33a14d9df03f2`, source recorded SHA `a6022fddd295d7c671690fbce5e25dc6fed47ca7fa77bf1d8a86ebadb2d927bb`. Independently parsed all 99 card names / 100 cards / 35 lands, 1 duplicate basic (Island).
- Canonical [current-cycle decision record](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/decisions/Don_Andres_the_Renegade_Current_Cycle_Decisions_2026-10-14.md), [current approved-state registry](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/state/current_deck_overrides.json), 2026-10-14 exact SHA-bound deck gate 100/99 UBR legal/rules PASS, no exceptions.
- M5 evidence `data/grixis/m6/optimizer/don-andres-the-renegade.json` Pass A 109, Pass B 3, candidate ranking not proof. Public [Don oracle](https://mtg.wtf/card/lcc/28/Don-Andres-the-Renegade), [Thieving Amalgam](https://mtg.wtf/card/c19/21/Thieving-Amalgam), [Black Cat](https://mtg.wtf/card/spm/52/Black-Cat-Cunning-Thief), [Jhoira](https://mtg.wtf/card/frc/8/Jhoira-Weatherlight-Corsair), [Court](https://mtg.wtf/card/woc/31/Court-of-Locthwain), [Varmint](https://mtg.wtf/card/otc/23/Thieving-Varmint), [EDHREC optimized theft](https://edhrec.com/commanders/don-andres-the-renegade/optimized/theft) — sample popularity not power measurement.
- Case analysis A–I authored by ChatGPT, not claimed as model wins. GitHub exact-head validation receipt to be linked in tracker only after actual CI success and no-skip guard.

