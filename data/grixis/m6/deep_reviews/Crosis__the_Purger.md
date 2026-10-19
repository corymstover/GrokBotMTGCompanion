# Crosis, the Purger — full commander-first authored deep review (#10)

**Date/role:** October 19 2026 primary ChatGPT engineering analysis, distinct from GrokBot independent Pass C and full M6 milestone. Nothing in this report authorizes modifying the approved canonical deck or its lock SHA.
**Exact approved source:** `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Crosis_the_Purger_Approval_Candidate_2026-10-14.txt`. Despite name `Approval_Candidate`, this EXACT file (not old `Crosis_the_Purger_Final_2026-10-13.txt`) is **user-approved and LOCKED Oct14** per `state/current_deck_overrides.json` and `refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md`. Its actual raw SHA-256 matches canonical recorded **`a59150c323aa1e21cbda65291a3b172d08ecc3b83266b708768f4e14f0b07ec1`**. File Git blob `f0e0db5fe3a9637b41b42c3ad90486bd2d8d992c`. Engineering logical `lh1:0cbe60a05298b70d73e20acd46eb164cb081b76da9401c69fbce41cf3b871f09`. Identity discrepancy NONE.

## Commander identity and natural ceiling

Crosis costs SIX mana `{3}{U}{B}{R}`, is a flying Dragon, and ONLY WHEN CROSIS deals COMBAT DAMAGE to a PLAYER can you pay `{2}{B}`; if you do, choose ONE COLOR as trigger RESOLVES, reveal that damaged player's HAND, discard ALL cards of that color. Without Painter's Servant, MonoColor-relevant target color depends on actual cards in hand; even an unblocked Dragon requires sufficient extra mana, enemy hand and protection. Hand disruption, protection/haste, combat evasion, and discard-to-value are essential commander-first elements.
**Painter's Servant** as enters chooses one COLOR globally added to every card not on battlefield including cards in hand and lands, plus spells and permanents. When Crosis connects, choosing Painter color while it survives makes ALL cards in opponent's hand share that color, turning 2B hit into COMPLETE hand purge; Liliana's Caress/Waste Not/Geth's Grimoire/Tinybones magnify it. Removing Crosis or Painter before resolution breaks plan; no forced generic Painter+Grindstone package. Natural ceiling **Bracket 4 optimized discard-control/combat damage**, not cEDH. The relevant finishers are handless-boards with Crosis commander combat clock, discard drain/theft and possible combat loop if extra card were added.

## Full 100-card role audit

Exact approved Oct14 source and fresh Complete Gate card CSV independently: **100 cards**, **92 distinct names**, **36 land cards**, **14 printed creature names**. Repeat basic lands Island×4, Mountain×3, Swamp×4 ONLY, singleton PASS. Commander identity exact Grixis B/R/U, official Commander legal on all 92 Oracle rows, zero exceptions and zero unresolved. No archival Oct13 final or prior-cycle approval substitute for current file. This 36-land structure plus Arcane/Dimir/Izzet/Rakdos Signet, three Talismans, Sol Ring, Mana Vault, Lotus Petal, fast Mox and fetches supports six-MV commander and extra paid 2B, but actual protected first hit turn-rate not measured.
User-authorized historical package changes from Oct14 include Painter's Servant, Brotherhood Regalia, Sword of Feast and Famine, Bandit's Talent, Tinybones Bauble Burglar, Mana Drain, Recoil, Swiftfoot Boots, plus untapped/fetch mana refinements (Shizo, Plaza of Heroes, City of Brass, Cavern of Souls, Marsh Flats, Misty Rainforest, Verdant Catacombs). Intentionally retained Blizzard/Sedraxis/Fell Specters, Tergrid, Kroxa, Tinybones package, Oppression/Bottomless Pit and wheels, not a generic alternate Grixis cEDH win shell.

### Every approved card: exact 100 copies, 92 unique source rows

| Card | Qty | Current Oracle type | Commander-centric analysis: value, sequencing and drawback |
|---|---:|---|---|
| Crosis, the Purger | 1 | Legendary Creature — Dragon | Commander 6MV flying UBR Dragon: combat damage TO PLAYER, optionally pay 2B, choose ONE COLOR on resolution, damaged player reveals hand/discards ALL cards of chosen color. Commander attack/combat needed. |
| Ancient Tomb | 1 | Land | MANABASE: colored source/timing support and commander connection resource cost. |
| Arcane Signet | 1 | Artifact | Fast 1-2MV rock improves 6MV Crosis cast and leaves 2B for on-hit trigger. |
| Badlands | 1 | Land — Swamp Mountain | Fetchable dual/shock: high tempo for UBR Crosis, shock sometimes costs2life. |
| Bandit's Talent | 1 | Enchantment — Class | On ETB each opponent may discard one NONLAND instead of two cards; level2 drains empty/<=1 hand opponents each upkeep; level3 draws for each empty/<=1 opponent at own draw step. |
| Black Market Connections | 1 | Enchantment | Upkeep first main choose Treasure (-1life), draw (-2life), 3/2 changeling (-3life) modes, reliable engine but life costs, 3/2 not Dragon by itself. |
| Blizzard Specter | 1 | Snow Creature — Specter | Creature combat damage to player makes opponent discard a card? Exact Oracle type matters; 4MV on-hit control, retained explicitly approved. |
| Blood Crypt | 1 | Land — Swamp Mountain | Fetchable dual/shock: high tempo for UBR Crosis, shock sometimes costs2life. |
| Bloodstained Mire | 1 | Land | FETCH: typed shock/dual access helps UBR 6MV commander and shuffles. |
| Bottomless Pit | 1 | Enchantment | On each player's UPKEEP each player randomly discards one, including you; anti-aggro long plan, synergizes Caress/Waste Not, symmetry is real. |
| Brotherhood Regalia | 1 | Artifact — Equipment | Ward2/evasion, equip LEGEND for1, Crosis on-hit dominant payoff. |
| Cavern of Souls | 1 | Land | Choose Dragon, makes Crosis uncounterable when mana used for Dragon spell, can't produce unrestricted noncreature colored mana. |
| Chaos Warp | 1 | Instant | Protection/interaction for Crosis, Painter, on-hit disruption; card slot justified by commander survival. |
| Chrome Mox | 1 | Artifact | Pitch imprint colored nonartifact nonland card, ongoing color, card disadvantage. |
| City of Brass | 1 | Land | MANABASE: colored source/timing support and commander connection resource cost. |
| Command Tower | 1 | Land | MANABASE: colored source/timing support and commander connection resource cost. |
| Cyclonic Rift | 1 | Instant | Protection/interaction for Crosis, Painter, on-hit disruption; card slot justified by commander survival. |
| Damnation | 1 | Sorcery | Board wipe all creatures; removes Crosis and discard engine pieces, preserves card advantage behind hand lock. |
| Dark Deal | 1 | Sorcery | All players DISCARDS their hands then draw cards equal discarded number minus1; improves hand denial but feeds opponents fresh cards, Notion Thief denies their draws. |
| Dark Ritual | 1 | Instant | Oracle support: Add {B}{B}{B}.; accepted role and potential tempo tradeoff. |
| Deflecting Swat | 1 | Instant | Free target redirection while commander controlled, can defend Dragon from spot removal but not full wipe. |
| Demonic Tutor | 1 | Sorcery | Tutor exact connect enabler, Painter, discard payoff or protection. |
| Dimir Signet | 1 | Artifact | Fast 1-2MV rock improves 6MV Crosis cast and leaves 2B for on-hit trigger. |
| Dream Salvage | 1 | Instant | 1 U/B? Draw count equal opponent discarded THIS TURN. Crosis+Painter can draw huge at cheap cost, but only after discards. |
| Drown in the Loch | 1 | Instant | Counter or destroy creature only while target MV<=cards in controller GY, grave hate reduces reach. |
| Exotic Orchard | 1 | Land | MANABASE: colored source/timing support and commander connection resource cost. |
| Feed the Swarm | 1 | Sorcery | Protection/interaction for Crosis, Painter, on-hit disruption; card slot justified by commander survival. |
| Fell Specter | 1 | Creature — Specter | Creature ETB discard and each opponent discard pings2 to their controller? repeatable punishment, source Commander plan. |
| Fierce Guardianship | 1 | Instant | Free counter NONcreature while controlling Crosis, protects core engine post-commander. |
| Force of Will | 1 | Instant | Free counter by exiling blue from hand and paying1 life, protects heavy commander and Painter but costs card. |
| Gamble | 1 | Sorcery | R tutor any card then discard random card, high chance to lose needed Crosis support if hand small. |
| Geier Reach Sanitarium | 1 | Legendary Land | 2/tap each player draws then DISCARD, one per player triggers opponent discard punish; combo with Notion may redirect opponent draw but discard still happens if cards. |
| Geth's Grimoire | 1 | Artifact — Book | Whenever opponent discards ONE CARD may DRAW one, N cards discarded yields N triggers; Crosis+Painter may fill or overdraw hand. |
| Hymn to Tourach | 1 | Sorcery | BB target opponent randomly discards TWO, low-cost noncombat pressure, strong with Caress/Grimoire. |
| Island | 4 | Basic Land — Island | BASIC ×4: 36-land stable colored source. |
| Izzet Signet | 1 | Artifact | Fast 1-2MV rock improves 6MV Crosis cast and leaves 2B for on-hit trigger. |
| Jet Medallion | 1 | Artifact | Cost reduction1 generic for black spells, Crosis multicolor not wholly black? Color identity multiple but it IS black, discount applies generic to black spells. |
| Kroxa, Titan of Death's Hunger | 1 | Legendary Creature — Elder Giant | ETB unless escaped gets sacrificed; its ETB/attack forces each opponent discard1 and if cannot discard nonland loses3. Strong independent discard-pressure engine, not auto-cut for Assault. |
| Lightning Greaves | 1 | Artifact — Equipment | Haste + shroud, equipped Crosis untargetable incl your further equip ability while shroud active; equip0 and move gear before other equips. |
| Liliana's Caress | 1 | Enchantment | Each opponent DISCARD CARD loses2 life PER discarded card. Crosis full-hand purge means N cards ->2N life loss. Life loss not DAMAGE. |
| Lotus Petal | 1 | Artifact | Sac for one colored mana, speeds Crosis but one-shot. |
| Luxury Suite | 1 | Land | MANABASE: colored source/timing support and commander connection resource cost. |
| Mana Confluence | 1 | Land | MANABASE: colored source/timing support and commander connection resource cost. |
| Mana Drain | 1 | Instant | Oracle support: Counter target spell. At the beginning of your next main phase, add an amount of {C} equal to that spell's mana value.; accepted role and potential tempo tradeoff. |
| Mana Vault | 1 | Artifact | One-MV CCC burst, six-MV commander acceleration but life/untap cost. |
| Marsh Flats | 1 | Land | FETCH: typed shock/dual access helps UBR 6MV commander and shuffles. |
| Mind Twist | 1 | Sorcery | XB targeted RANDOM discard X from one player's hand, potential color unrestricted utility. |
| Misty Rainforest | 1 | Land | FETCH: typed shock/dual access helps UBR 6MV commander and shuffles. |
| Morphic Pool | 1 | Land | MANABASE: colored source/timing support and commander connection resource cost. |
| Mountain | 3 | Basic Land — Mountain | BASIC ×3: 36-land stable colored source. |
| Mox Diamond | 1 | Artifact | Discard land or lose itself on ETB, turn1 fixing at land-resource opportunity cost. |
| Mystical Tutor | 1 | Instant | Tutor exact connect enabler, Painter, discard payoff or protection. |
| Notion Thief | 1 | Creature — Human Rogue | Opponent non-first draw-step draws replaced by YOU DRAWING. With Puzzle Box after opponent normal draw, redirects all Box draws and leaves opponent empty hand if no response. |
| Oppression | 1 | Enchantment | Each spell cast triggers that caster discarding one card, INCLUDING YOU; can punish combo opponents but self-hand risk, if no card cannot discard. |
| Orcish Bowmasters | 1 | Creature — Orc Archer | Flash draw-punish opponent draws outside first draw step and creature ping, supplies pressure while wheels operate; doesn't trigger from discard itself. |
| Painter's Servant | 1 | Artifact Creature — Scarecrow | Choose a color when enters, globally adds that color to all cards not on BF AND spells/permanents, permits whole-hand Crosis selection INCLUDING basic lands. |
| Plaza of Heroes | 1 | Land | Mana for legends and pay3/tap/exile from hand? Oracle source protective activated mode, protects commander at opportunity cost. |
| Polluted Delta | 1 | Land | FETCH: typed shock/dual access helps UBR 6MV commander and shuffles. |
| Rakdos Signet | 1 | Artifact | Fast 1-2MV rock improves 6MV Crosis cast and leaves 2B for on-hit trigger. |
| Reanimate | 1 | Sorcery | B return creature from GY any side, life loss MV; backup value/commander grave plan if user leaves commander GY. |
| Recoil | 1 | Instant | UB instant bounce ANY permanent then that player discards1, when hand otherwise empty may force bounced card to be discarded; if bounced token disappears, no card in hand. |
| Scalding Tarn | 1 | Land | FETCH: typed shock/dual access helps UBR 6MV commander and shuffles. |
| Sedraxis Specter | 1 | Creature — Specter | 3MV flying hand-hit discards, reanimate/Unearth utility and tempo pressure. |
| Shizo, Death's Storehouse | 1 | Legendary Land | Gives fear with B/tap, not true unblockability; black/artifact blockers exist. |
| Sol Ring | 1 | Artifact | Fast 1-2MV rock improves 6MV Crosis cast and leaves 2B for on-hit trigger. |
| Steam Vents | 1 | Land — Island Mountain | Fetchable dual/shock: high tempo for UBR Crosis, shock sometimes costs2life. |
| Swamp | 4 | Basic Land — Swamp | BASIC ×4: 36-land stable colored source. |
| Swan Song | 1 | Instant | Protection/interaction for Crosis, Painter, on-hit disruption; card slot justified by commander survival. |
| Swiftfoot Boots | 1 | Artifact — Equipment | Haste+hexproof, equip1, preserves your ability to equip additional gear and targeted spells. |
| Sword of Feast and Famine | 1 | Artifact — Equipment | On-hit extra DISCARD and land UNTAP can fund 2B after trigger; protection black/green gives evasion vs those blockers. |
| Syphon Mind | 1 | Sorcery | Each opponent discards1, you draw for each discarded this way, efficient multi-opponent 4MV. |
| Talisman of Creativity | 1 | Artifact | Fast 1-2MV rock improves 6MV Crosis cast and leaves 2B for on-hit trigger. |
| Talisman of Dominance | 1 | Artifact | Fast 1-2MV rock improves 6MV Crosis cast and leaves 2B for on-hit trigger. |
| Talisman of Indulgence | 1 | Artifact | Fast 1-2MV rock improves 6MV Crosis cast and leaves 2B for on-hit trigger. |
| Teferi's Puzzle Box | 1 | Artifact | At EACH player's draw step they put hand on library BOTTOM, then DRAW same number. This is NOT DISCARD, so Waste Not/Caress/Grimoire do not trigger! |
| Tergrid, God of Fright // Tergrid's Lantern | 1 | Legendary Creature — God // Legendary Artifact | Opponent DISCARD PERMANENT CARD or SAC nontoken permanent -> Tergrid may put that card from grave directly onto your battlefield; after Bauble Burglar exiles card no longer in grave, trigger ordering matters. |
| The Raven Man | 1 | Legendary Creature — Human Wizard | At END STEP if any player discarded during turn, creates 1/1 flying Bird that cannot block; activated sorcery-speed forces each opponent discard. |
| Tinybones, Bauble Burglar | 1 | Legendary Creature — Skeleton Rogue | Opponent discards card -> EXILE it from their grave with stash counter; during own turn may play exiled opponent cards with stash using any mana types; competes with Tergrid retrieving that same grave PERMANENT. |
| Tinybones, Pocket Nuisance | 1 | Legendary Creature — Skeleton Rogue | ETB all opponents discard ONE, whenever player discards ONE OR MORE CARDS it deals1 DAMAGE to each opponent (once per each discard EVENT/player, not once per card). |
| Tinybones, Trinket Thief | 1 | Legendary Creature — Skeleton Rogue | END STEP if opponent discarded this turn draw1 lose1; activated 4BB makes each empty-handed opponent lose10 life. |
| Tourach, Dread Cantor | 1 | Legendary Creature — Human Cleric | Kicked discard two, grows when opponent discards, pro-white evasion; commander-aligned creature. |
| Toxic Deluge | 1 | Sorcery | Board wipe shrinking X, loses X life as additional cost, can reset own Dragon and control shell. |
| Training Center | 1 | Land | MANABASE: colored source/timing support and commander connection resource cost. |
| Underground Sea | 1 | Land — Island Swamp | Fetchable dual/shock: high tempo for UBR Crosis, shock sometimes costs2life. |
| Vampiric Tutor | 1 | Instant | Tutor exact connect enabler, Painter, discard payoff or protection. |
| Verdant Catacombs | 1 | Land | FETCH: typed shock/dual access helps UBR 6MV commander and shuffles. |
| Volcanic Island | 1 | Land — Island Mountain | Fetchable dual/shock: high tempo for UBR Crosis, shock sometimes costs2life. |
| Waste Not | 1 | Enchantment | Each opponent discards CREATURE makes 2/2 Zombie, LAND makes BB, noncreature/nonland draws1; Painter gives extra color but doesn't change discarded card types. |
| Watery Grave | 1 | Land — Island Swamp | Fetchable dual/shock: high tempo for UBR Crosis, shock sometimes costs2life. |
| Wheel of Fortune | 1 | Sorcery | All discard hand then draw7; causes mass discard triggers but refills opponents; Notion Thief can steal their extra draw. |
| Windfall | 1 | Sorcery | All discard hands then draws MAX number any player discarded, can massively refill enemies without Notion; Caress/Grimoire value. |
| Xander's Lounge | 1 | Land — Island Swamp Mountain | Tapped UBR fixing with early tempo penalty. |

## Candidate pool and competing cuts

Engineering M5 source `data/grixis/m6/optimizer/crosis-the-purger.json` has **14 Pass A candidate projections + 3 Pass B** (17 total) and 0 identical exact add/cut agreements, considerably smaller candidate coverage than other decks. Neither rank score nor prior community popularity substitutes card-by-card fit. Primary explicit challenger:

| Add → possible named cut | Actual advantage and complete opportunity cost | Disposition |
|---|---|---|
| **Aggravated Assault → Blizzard Specter** (NEW alternative cut, not the ranked proposal) | Existing Sword of Feast and Famine equipped to UNBLOCKABLE Crosis provides land untaps on hit. With ≥5 land mana INCLUDING two red, Aggravated Assault `{3}{R}{R}` at sorcery timing in postcombat main gives another combat followed by main; Crosis attacks/hits again and Sword untaps lands. Repeat can produce arbitrarily many commander attacks/combat damage and multiple Crosis purge opportunities (hand usually empties after first). Strong identity-aligned combat conversion. | **HIGH-VALUE EXPERIMENT ONLY**, not applied: extra 3MV enchantment + 5-mana activation, Sword and evasive live Crosis needed, and Blizzard Specter was deliberately retained as discard damage support. No paired survival/tempo test establishing that replacement improves realistic game outcomes. |
| **Aggravated Assault → Kroxa, Titan of Death's Hunger** (M5 A) | Same Sword extra-combat opportunity, but Kroxa is efficient recurring ALL-opponent discard and 3life penalty, reinforcing denial even when Crosis unavailable. | REJECT cutting Kroxa without sustained evidence. |
| **Aggravated Assault → Tergrid, God of Fright** (M5 A) | Tergrid converts opponent-discarded PERMANENT cards into YOUR battlefield and works even without Sword, one of strongest Crosis hand-purge payoffs. | REJECT ranked exact cut. |
| **Cephalid Aristocrat / Cephalid Illusionist → Kroxa or Orcish Bowmasters** (M5 A) | New alternate blue support may be synergistic in other shells, but exact Oracle and commander-specific discard connection not independently verified here; swapping away Kroxa or fast Bowmasters loses actual hand-pressure/interaction. | UNSUPPORTED at this evidence level, no swap. |
| **Crackdown Construct → Kroxa / Bowmasters** (M5 A) | Construct loops can be strong generically but would compete with core Crosis-oriented discard engine; no approved loop from this exact source shows gain. | REJECT ungrounded pair. |
| **Burning Inquiry → Black Market Connections** (M5 B) | One-R random three-card discard/draw EACH player makes discard payoffs immediate, but refills each opponent while Connections gives ongoing Treasure/draw and 3/2 blocker at life cost. | Metagame contender only, no demonstrated net gain. |
| **Reforge the Soul → Black Market Connections** (M5 B) | Additional 7-card wheel can be cheap with miracle if correctly drawn, good Notion Thief/Waste Not synergy, but slower full-price and refills opponents without Thief; removes recurring mana/card draw. | HOLD, no evidence outweighing card-engine loss. |
| **Relic of Sauron → Black Market Connections** (M5 B) | Mana fixing/reduction utility but at high mana with already abundant rocks, Connections supports commander beyond raw mana. | REJECT on curve/identity. |
| **Painter's Servant → any generic discard payoff** | Painter creates all-color unified hand enabling actual Crosis full purge, unlike most generic discard cards. Its source/type interactions are uniquely commander-scaling and come with hate risks, but no replacement improves this identity. | NEVER AUTOCUT. |

No explicit owner request to reopen a locked deck: no source modification and no proposed swap applied. A possible alternative can be rigorously recorded as a future controlled study, not adopted because an M5 heuristic favors it.

## Oracle, legality and rules

1. On damage to PLAYER (not planeswalker), Crosis COMBAT hit creates triggered ability, choose whether pay 2B DURING RESOLUTION. Color chosen during resolution, then damaged opponent reveals hand/discards every card matching selected color; opponents can respond before ability resolves but NOT after hearing chosen color before discarding. Hexproof player doesn't stop this because Crosis's triggered ability doesn't target the player.
2. Painter's Servant chooses color AS it enters. Every CARD in HAND or library or grave, including normally COLORLESS artifacts and LAND CARDS, gains chosen color, so the chosen-color Crosis purge hits ENTIRE victim hand regardless of printed color. If Painter leaves battlefield before Crosis trigger resolution, blanket coloring ceases; hit still may purge one naturally colored set.
3. Brotherhood Regalia equipped to LEGENDARY Crosis costs ONE to equip at sorcery speed, grants ward2 and UNBLOCKABLE (no blockers can legally block). Swiftfoot Boots grants haste/hexproof and still allows your own equips. Lightning Greaves grants shroud, which can obstruct your subsequent targeted equipment equip abilities until moved. Shizo fear only excludes nonblack/nonartifact creatures and is NOT fully unblockable.
4. Sword of Feast and Famine and Crosis triggers both on same COMBAT DAMAGE event. You choose their stack order. If Sword RESOLVES FIRST, lands untap and you can then pay 2B for Crosis, but opponent already DISCARDs one before the color purge. If Crosis resolves FIRST, you may purge larger hand but need 2B already available. If opponent's hand empty before Sword, no Sword discard effect but lands still untap.
5. Waste Not distinguishes discarded CREATURE card→2/2 Zombie, LAND card→BB, noncreature/nonland→DRAW; Painter makes cards extra color but doesn't change their types. Liliana's Caress and Geth's Grimoire trigger separately PER opponent card discarded. Tinybones Pocket Nuisance triggers ONCE per a player discarding one or more in a simultaneous event, not for N cards from Crosis.
6. Tergrid triggers on OPPONENT discarding PERMANENT card; Tinybones Bauble Burglar exiles every discarded opponent card with stash counter. If BOTH you control, their effects compete for same physical card in grave: choose order of simultaneous trigger placement to select stealing by Tergrid or exiling with Tinybones; if card already moved, later trigger can't retrieve it. Bauble Burglar's stolen cards can be played on your turn for mana of any type but normal land-play/timing restrictions still apply.
7. Teferi's Puzzle Box trigger puts hand cards on BOTTOM of library, not GRAVE and not DISCARDED; Waste Not/Caress/Grimoire/Thief discard payoffs NEVER trigger directly from bottoming. Notion Thief replaces draws opponent would make from Box AFTER their normal draw-step first draw; those draws become YOUR draws, opponent ends with empty hand if none of their original draw replacement/draw effects interfere. Opponents may cast instants in draw step in response to Box. It's a restrictive draw lock, not an instant damage-based win.
8. Bandit's Talent on entering: each opponent may choose to discard ONE nonland card INSTEAD of two arbitrary cards. At level2 opponent upkeep if hand <=1 loses2 life; at level3 your draw step draw for each opponent with <=1 card. Those payoff triggers can occur even without Crosis if hand denial already works.
9. Recoil bounces target permanent to OWNER'S hand then that player discards one. If hand otherwise empty before Recoil, bounced regular permanent is sole card and must be discarded, effectively 3MV UB all-permanent answer with delayed discard triggers; if target token goes to hand it ceases to exist, so cannot be discarded as a card.
10. Aggravated Assault's sorcery-speed activation pays 3RR to untap your creatures and insert one additional COMBAT followed by MAIN after present main. With Sword-equipped evasive attacker connecting, lands untap each combat; if ≥3RR from lands in subsequent MAIN, you can repeat finite N times, producing arbitrarily many combat steps and potentially lethal COMMANDER damage. Not auto-infinite if Sword fails to connect, Sword unequipped, mana insufficient, no combat-capable body, enemy Fog/removal, or activations restricted. Does not produce stored 'infinite mana' across phase boundaries.
11. Oppression triggers after ANY player cast spell, including yourself; cast spell remains on stack even if triggered discard empties caster hand. Bottomless Pit discards randomly on EACH player's upkeep, not one-sided. Both can damage your own protection/search resources, but preserve scarce long-game lock effects.
12. All current approved 92 Oracle rows officially legal B/R/U, all 100 copies correct, zero project exception; checker Oct14 SHA binding. No one-step ranked candidate automatically legal/meaningful without independent specific card Oracle verification and owner approval.

## Finite sequencing and adversarial scenarios

**A — one Crosis+Painter whole hand purge:** Control Beholder? Actually CROSIS (6MV) with haste or a prior-turn ready attack, Painter's Servant choosing RED and Brotherhood Regalia equipped, leave 2B available. Damaged opponent has six cards: an Island, a colorless artifact, three black spells and a green land. All six are also RED in hand by Painter. Crosis deals combat damage; its trigger resolves, pay 2B, choose RED; opponent reveals and discards ALL six, Liliana's Caress would trigger six times -> lose12 life, Geth's Grimoire offers six card draws, Waste Not identifies each original TYPE for its own effect. If Painter removed in response to Crosis trigger before color selection, there may be zero naturally red cards; no automatic full-hand purge.
**B — Sword stack choice:** Crosis with Sword, Regalia equipped, player holds two blue and two red cards, no Painter. On hit Crosis and Sword triggers. Choosing stack Sword TOP causes Sword player DISCARD1 and you untap all lands, then with now-ready 2B pay Crosis and choose likely remaining color, discard all of that color. Choosing Crosis TOP instead lets 2B be paid before Sword mana if already floated or untapped, maximizing color discard count but no Sword refund until after. This is strategic resource/sequence decision, not an automatic order.
**C — lock isn't discard damage:** Opponent's draw step begins with zero cards in hand and Notion Thief+Puzzle Box in play under Crosis controller. Opponent draws NORMAL first card (exempt from Thief), Box later bottoms 1 card, instructs draw1, Thief redirects that non-first draw to you; opponent starts main with zero cards. No card was DISCARDED as part of Box, so Caress/Waste Not/Grimoire do not fire. Opponent could cast drawn instant before Box resolves if legal, or remove Notion in response.
**D — Tergrid vs Tinybones stash:** On Crosis full purge two land cards and one instant discarded, both Tergrid and Tinybones trigger for lands. Resolve Tergrid first: land returned to your BF (if legal), Tinybones sees land no longer in grave and can't stash it. Or resolve Tinybones first to exile/stash land, Tergrid can't take it. Instant only Tinybones stash qualifies (not Tergrid which requires PERMANENT). Damage/discard triggers otherwise independent.
**E — Sword + candidate Assault finite three turns:** With Crosis+Sword equipped and regalia active, 5+ untapped lands producing 3RR, and Aggravated Assault on BF (NOT CURRENTLY APPROVED). Crosis connects, Sword untaps all lands. In postcombat main tap lands to pay3RR, activate Assault, untap Crosis, extra combat and extra main. Repeat if Crosis connects again. Each loop adds six commander damage (or eight with Sword's +2/+2) to victim, quickly lethal via commander damage. If any combat step fails to hit, subsequent iteration cannot refund 5 land mana; refrain from unbounded claim under disruption. This is a new high-interest contender to test; not an approved edit.
**F — adverse matchup:** An opponent removes Painter before Crosis's color trigger, blanks entire-hand purge, even if Crosis still connects. Regalia equipped ward2 taxes target removal but does not prevent global board wipes or artifact destruction. Notion Thief wheel combo may draw you many cards and deck out if massive; protective Counter/Force resources must defend. Bottomless Pit/Oppression tax YOUR casts/hand too. Enemy with no cards in hand makes Crosis purge negligible; rely on commander damage or Bandit's Talent/Tinybones empty-hand damage.

## Conclusions and unresolved evidence

**STRATEGIC HOLD** on locked current approved 100. The deck is an actual Crosis combat-hit/color-purge identity build, not generic Grixis discard goodstuff: Painter makes whole-hand purge, Regalia makes hit reliably unblockable, Sword sequences 2B mana, and Waste Not/Geth/Tinybones/Tergrid convert hit to value. Rank-pushed Aggravated Assault is a legitimate synergistic 2-card infinite-combat partner of EXISTING Sword, but it introduces a combo identity shift and still requires 5 land mana/board survival. Against the intentionally approved Kroxa, Tergrid or Blizzard Specter, no independently simulated net improvement or owner authorization to reopen. Keep canonical list frozen; document high-priority comparison rather than altering it.
**Evidence not yet obtained:** Turn-six protected Crosis with open 2B castability, live ability to keep Painter, proportion opponents have colored/nonempty hands, Notion Puzzle Box response distribution, Sword+Assault tested across 4-player enemy removal, new candidate Oracle for obscure Cephalid cards. No actual matched multiplayer result, no regenerated pipeline or Google Colab, and no independent GrokBot Pass C. Natural ceiling remains Bracket 4 — Optimized.

## Source and test receipts

- Canonical approved Oct14 file `refinement/decklists/Crosis_the_Purger_Approval_Candidate_2026-10-14.txt` (approved notwithstanding filename), SHA-256 `a59150c323aa1e21cbda65291a3b172d08ecc3b83266b708768f4e14f0b07ec1`, authority `state/current_deck_overrides.json#Crosis__the_Purger`, explicit approval `refinement/decisions/Crosis_the_Purger_Current_Cycle_Decisions_2026-10-14.md`.
- Complete gate exact current per-card Oracle `refinement/verification/crosis_2026-10-14/gate_output/Crosis_the_Purger_2026-10-14_Card_Verification.csv` blob `3a06e23bc0a0e4ba866f2ff486fd55c8ce35b676`; 92 distinct records all B/R/U Commander legal PASS; 100 copies. No new individual 92 live Scryfall API claims.
- Engineering blueprint `data/grixis/blueprints/crosis-the-purger.json`, M5 projections `data/grixis/m6/optimizer/crosis-the-purger.json`: 14+3 candidate pairs, zero exact add/cut agreements, past Oct14 approved whole-deck decision package.
- External combo verification Sword of Feast and Famine + Aggravated Assault prerequisites/steps https://edh-combos.com/combo/900-3750/ and https://www.ccgforge.com/en/combo/900-3750; these do not establish that it beats a named APPROVED cut, and no copy is currently in 100.
- Current comprehensive rules https://magic.wizards.com/en/rules and official ban list https://mtgcommander.net/index.php/banned-list/ ; legal evidence based on canonical fresh Oct14 gate with zero project exceptions. M6 single-deck CI required on exact head prior tracker advancement, not independent GrokBot Pass C.
