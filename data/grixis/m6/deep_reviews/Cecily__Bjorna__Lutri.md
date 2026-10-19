# Bjorna, Nightfall Alchemist // Cecily, Haunted Mage + Lutri — deep review #8

**Type of review:** ChatGPT authored engineering analysis on October 19, 2026, NOT independent GrokBot Pass C or formal M6 certification; canonical approval and owner locks unchanged.
**Canonical two-commanders main deck:** `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Cecily__Bjorna__Lutri_Approved_2026-10-13.txt` (source SHA-256 **`553838da88fe00974e74664633be5051c4f1a0879baa71de81ca9f880e5a6d28`**, source Git blob `543f7afafd0dc8a14ed28fb626c775716a685d64`). Both commanders count INSIDE the 100. Registered engineering logical hash `lh1:030933b552a9906fee98edf30961a5c57a8c40efd8971da3d37f7194ca8bf507`, not the same as RAW source hash by design.
**Companion:** `1x Lutri, the Spellchaser [Companion]` exists OUTSIDE the 100-card library+commanders, as an authorized project exception, and is in the engineering logical snapshot/Oracle audit but NOT the raw approved 100-card text. This creates 101 represented physical objects including companion, not a 101-card Commander deck.
**Exception authority:** project expressly permits Lutri companion, Trade Secrets and Yawgmoth's Bargain in this ONE designated deck. ALL THREE are officially banned in Commander in their specified uses, but approved as PROJECT exceptions. Do NOT represent resulting deck as officially Commander legal; do NOT remove/refit three cards or substitute the official-legal projection. Main state approval `APPROVED/LOCKED` Oct13 and retrospective `PASS_PROJECT_EXCEPTION` Oct14.

## Commander identity and natural ceiling

Cecily is UBR Human Wizard with max-hand-size eleven, and ATTACK trigger: draw one, lose one life, then IF you have eleven or more cards in HAND at that point, may CAST ONE instant or sorcery FROM HAND WITHOUT paying its mana cost. Maximum hand size is a CLEANUP restriction not a perpetual cap: hand can temporarily exceed 11. Hand engine must stock 10 before attack (11 after draw) or use Teferi draw replacement for extra. Cecily's free spell timing is during the attack trigger resolution, not combat damage and not before attackers.
Bjorna is UR Human with TAP+SAC ARTIFACT to deal exactly one DAMAGE to a target creature and goad it until your next turn. Goad causes attacks in subsequent combats if able toward another player where possible, but DOES NOT prevent creature from BLOCKING Cecily during your current turn. No use while summoning-sick unless haste; artifact token factory Clue/Treasure/Sai/Third Path/Anvil provides sacrificial fuel. These are PARTNER—FRIENDS FOREVER commanders, an authorized specific pairing. Lutri companion enhances spell copying from outside the 100, with mandatory extra three generic to move to hand then separately cast for 1UR, when CAST Lutri ETB can copy a spell YOU CONTROL (not when simply blinked).
Natural ceiling optimized Bracket 4: expensive high-MV spells cast for zero on Cecily attack and blowout hand-size combo; four-MV Cecily still needs to attack safely and accumulate 11 hand with actual copyable payload, and Bjorna's goad/tap needs fuel. Powerful generic spells are warranted as Cecily payloads but must preserve the hand-to-eleven and Bjorna artifact-politics axes rather than drift to generic cEDH storm.

## Full 100-card role audit

**Exact approved TXT:** 100 copies across 99 distinct names, **2 commanders + 98 other library cards**, 33 lands and 18 printed creature names in the 100. Island ×2 is the ONLY duplicate, every other card singleton, Commander identities combine exactly UBR. Separate Scryfall per-card audit has 100 distinct rows and 101 physical entries ONLY because it ALSO includes the outside-the-100 Lutri. Scryfall results for 97 normally legal main-deck unique names **PASS**, Trade Secrets and Yawgmoth's Bargain **PROJECT_EXCEPTION**, and Lutri **PROJECT_EXCEPTION**; zero unrecognized bans, zero off-identity cards, no wrong-count result. Already approved swap `Reckless Fireweaver → Robe of the Archmagi` retained.
Mana base 33 lands including Grixis dual/fetch/pathways, tapped Xander/Crumbling, utility Otawara/Sokenzan/Takenuma and basics, plus Arcane Signet/3 Signets/3 Talismans/Sol Ring/Thought Vessel, Goblin Electromancer, Seething Song, Storm-Kiln, Cormela, Jeska's Will and Mana Geyser. Colored UBR requirements are significant; no quantified turn-four Cecily protected attack cast rate. Big-cost spells Apex of Power, Cruel Ultimatum, Mnemonic Deluge and In Garruk's Wake are primarily free Cecily payloads; hard-casting those with rituals remains secondary and often inefficient.

### Each approved source card (exact 100 / 99 rows)

| Main deck card | Qty | Audit card type | Commander-first role, sequencing or weakness |
|---|---:|---|---|
| Bjorna, Nightfall Alchemist | 1 | Legendary Creature — Human | Commander UR Human; tap+sac ARTIFACT to deal1 damage to TARGET CREATURE and goad it. Can't tap first turn under summoning sickness; goad does not prevent that creature BLOCKING Cecily. |
| Cecily, Haunted Mage | 1 | Legendary Creature — Human Wizard | Commander UBR Wizard: max hand size 11 (not absolute cap), attack draw1 lose1 THEN if hand >=11 MAY CAST one instant/sorcery from HAND at zero mana cost. |
| Academy Manufactor | 1 | Artifact Creature — Assembly-Worker | Replacement for creating Clue/Food/Treasure creates one EACH for each original; Bjorna sacrificial options but not free extra triggers from replacement. |
| Apex of Power | 1 | Sorcery | Enabler/payload: Exile the top seven cards of your library. Until end of turn, you may cast spells from among them. If this spell was cast from your hand, add ten |
| Arcane Signet | 1 | Artifact | 2MV (or 1MV Sol Ring) acceleration, essential for fast Cecily/equipment/instants. |
| Archmage Emeritus | 1 | Creature — Human Wizard | Whenever CAST/COPY instant/sorc draw card; engine combines free Cecily casts with storm copies. |
| Big Score | 1 | Instant | INSTANT discard as additional COST, draws2 and creates TWO Treasures, Manufactor makes two each Clue/Food/Treasure, 2 potential Bjorna activations. |
| Blightstep Pathway // Searstep Pathway | 1 | Land // Land | Pathway land: choose ONE side on entry, cannot generate both colors later. |
| Blood Crypt | 1 | Land — Swamp Mountain | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Bloodstained Mire | 1 | Land | FETCH: typed dual/basic land fix, some enters tapped at lower land count. |
| Bojuka Bog | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Brainstorm | 1 | Instant | Enabler/payload: Draw three cards, then put two cards from your hand on top of your library in any order. |
| Brass's Bounty | 1 | Sorcery | Land count -> Treasure and Bjorna fuel, free Cecilys spell possible. |
| Chaos Warp | 1 | Instant | Stack/board removal keeps Cecily attack trigger/large hand engine alive. |
| Clearwater Pathway // Murkwater Pathway | 1 | Land // Land | Pathway land: choose ONE side on entry, cannot generate both colors later. |
| Command Tower | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Cormela, Glamour Thief | 1 | Legendary Creature — Vampire Rogue | Tap for 3-color inst/sorc mana; on death return inst/sorc card from grave, maintains free-spell quality. |
| Counterspell | 1 | Instant | Stack/board removal keeps Cecily attack trigger/large hand engine alive. |
| Cruel Ultimatum | 1 | Sorcery | Enabler/payload: Target opponent sacrifices a creature of their choice, discards three cards, then loses 5 life. You return a creature card from your graveyard to |
| Crumbling Necropolis | 1 | Land | TAPPED UBR fixer, colored requirements versus tempo. |
| Cyclonic Rift | 1 | Instant | Stack/board removal keeps Cecily attack trigger/large hand engine alive. |
| Dark Deal | 1 | Sorcery | Each discards all cards then draws that many minus one, lowers your hand size absent draw multipliers; supports Breach grave fuel. |
| Deadly Dispute | 1 | Instant | Instant sacrifice artifact or creature as additional COST, draw2 and create Treasure; trading off Bjorna fodder for current cards. |
| Demonic Tutor | 1 | Sorcery | Tutors wheel/Peer/interaction to hand or top; Cecily only casts instant/sorcery FROM HAND. |
| Dimir Signet | 1 | Artifact | 2MV (or 1MV Sol Ring) acceleration, essential for fast Cecily/equipment/instants. |
| Dragonskull Summit | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Drowned Catacomb | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Echo of Eons | 1 | Sorcery | Each player shuffles hand/grave into library and draws7; flashback2U and exile, refill opponents too. |
| Emry, Lurker of the Loch | 1 | Legendary Creature — Merfolk Wizard | Tap lets cast artifact from grave this turn; can re-use Wellspring/fodder, does not directly add a card without mana. |
| Fabled Passage | 1 | Land | FETCH: typed dual/basic land fix, some enters tapped at lower land count. |
| Feed the Swarm | 1 | Sorcery | Stack/board removal keeps Cecily attack trigger/large hand engine alive. |
| Fierce Guardianship | 1 | Instant | Stack/board removal keeps Cecily attack trigger/large hand engine alive. |
| Frantic Search | 1 | Instant | Enabler/payload: Draw two cards, then discard two cards. Untap up to three lands. |
| Goblin Electromancer | 1 | Creature — Goblin Wizard | Creature body/payoff: Instant and sorcery spells you cast cost {1} less to cast. |
| Goblin Engineer | 1 | Creature — Goblin Artificer | ETB puts artifact from library into grave; tap/sac artifact reanimates artifact MV<=3, Bjorna has competing sac cost. |
| Harmonic Prodigy | 1 | Creature — Human Wizard | Cecily is another Wizard, so its attack triggered ability triggers ADDITIONAL time; each independent hand threshold, can cast two spells if both conditions met. Does not double Bjorna's ACTIVATED ability. |
| Haunted Ridge | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Hexing Squelcher | 1 | Creature — Goblin Sorcerer | Creature anti-counter/punish interaction as current Oracle, supports expensive free casts. |
| Ichor Wellspring | 1 | Artifact | Artifact draws one on ETB and when grave from battlefield, 2 cards if sacrificed to Bjorna after entering. |
| In Garruk's Wake | 1 | Sorcery | Enabler/payload: Destroy all creatures you don't control and all planeswalkers you don't control. |
| Island | 2 | Basic Land — Island | BASIC ×2: Grixis mana, reliable, repeated only singleton exception. |
| Izzet Signet | 1 | Artifact | 2MV (or 1MV Sol Ring) acceleration, essential for fast Cecily/equipment/instants. |
| Jeska's Will | 1 | Sorcery | When commander controlled as CAST choose both produce R equal target opponent hand and 3-card impulse; repeated escape can be profitable only with appropriate resource setup. |
| Kess, Dissident Mage | 1 | Legendary Creature — Human Wizard | Once each OWN turn casts inst/sorc in grave, then exiles when leaving stack, combo/wheel/interaction redundancy. |
| Lightning Greaves | 1 | Artifact — Equipment | Equip0 haste shroud Cecily; shroud protects but interferes with targeted equips/abilities, moving equipment requires correct order. |
| Luxury Suite | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Mana Geyser | 1 | Sorcery | Red for opponent tapped lands, high explosive X spell fuel but only sorcery and conditional table. |
| Mnemonic Deluge | 1 | Sorcery | Exile inst/sorc from ANY graveyard then COPY it three times, cast the copies; all three COPIES CAST (printed), exception vs ordinary copied spells. |
| Morphic Pool | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Mountain | 1 | Basic Land — Mountain | BASIC ×1: Grixis mana, reliable, repeated only singleton exception. |
| Mystic Remora | 1 | Enchantment | Cumulative upkeep and conditional opponent noncreature spell draws help hand, not an unconditional free draw. |
| Mystical Tutor | 1 | Instant | Tutors wheel/Peer/interaction to hand or top; Cecily only casts instant/sorcery FROM HAND. |
| Niv-Mizzet, Parun | 1 | Legendary Creature — Dragon Wizard | Whenever any player CASTS inst/sorc you draw; when YOU DRAW Niv deals 1 DAMAGE to any target; direct win converter and works off wheel and Teferi doubling. |
| Notion Thief | 1 | Creature — Human Rogue | Flash, opponents' extra (outside first draw step) draws replaced by YOU drawing; turns wheels into enormous your-hand payoff but may deck yourself with Teferi. |
| Oni-Cult Anvil | 1 | Artifact | Artifact sacrificed leaves during YOUR turn generates 1/1 Construct artifact token once/turn; tap/sac itself another artifact drains each opponent/gains life. On OPPONENT turn Bjorna artifact sacrifice does NOT trigger its own-turn token-maker. |
| Otawara, Soaring City | 1 | Legendary Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Peer into the Abyss | 1 | Sorcery | Target player draws ceil(library/2) cards and loses ceil(life/2). On SELF plus Teferi doubles draw count; if odd library, attempt to draw too many, lose at SBA. |
| Polluted Delta | 1 | Land | FETCH: typed dual/basic land fix, some enters tapped at lower land count. |
| Psychosis Crawler | 1 | Artifact Creature — Phyrexian Horror | Power/toughness = own hand size and whenever YOU DRAW card each opponent loses1. Pure life LOSS not creature damage, and drawing an empty library can make YOU lose first. |
| Rakdos Signet | 1 | Artifact | 2MV (or 1MV Sol Ring) acceleration, essential for fast Cecily/equipment/instants. |
| Reforge the Soul | 1 | Sorcery | Miracle can reduce cost if first card drawn in own turn; all players discard draw7. |
| Rhystic Study | 1 | Enchantment | Taxed spell cast draws at opponent discretion, helps fill up to 11; opponents can pay. |
| Riverglide Pathway // Lavaglide Pathway | 1 | Land // Land | Pathway land: choose ONE side on entry, cannot generate both colors later. |
| Robe of the Archmagi | 1 | Artifact — Equipment | Draw damage-based equal to Cecily power. Attack-trigger free spell happens BEFORE damage. |
| Sai, Master Thopterist | 1 | Legendary Creature — Human Artificer | Casting artifacts creates 1/1 Thopter ARTIFACT tokens (not spell-copy entry); Bjorna can sacrifice them; 1U sac2 artifacts to DRAW. |
| Scalding Tarn | 1 | Land | FETCH: typed dual/basic land fix, some enters tapped at lower land count. |
| Seething Song | 1 | Instant | Enabler/payload: Add {R}{R}{R}{R}{R}. |
| Shipwreck Marsh | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Shivan Reef | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Sokenzan, Crucible of Defiance | 1 | Legendary Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Sol Ring | 1 | Artifact | 2MV (or 1MV Sol Ring) acceleration, essential for fast Cecily/equipment/instants. |
| Steam Vents | 1 | Land — Island Mountain | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Storm-Kiln Artist | 1 | Creature — Dwarf Shaman | Magecraft cast OR copy instant/sorcery creates Treasure, feeds Bjorna and big spell mana. |
| Stormcarved Coast | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Sulfur Falls | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Sulfurous Springs | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Swamp | 1 | Basic Land — Swamp | BASIC ×1: Grixis mana, reliable, repeated only singleton exception. |
| Takenuma, Abandoned Mire | 1 | Legendary Land | FETCH: typed dual/basic land fix, some enters tapped at lower land count. |
| Talisman of Creativity | 1 | Artifact | 2MV (or 1MV Sol Ring) acceleration, essential for fast Cecily/equipment/instants. |
| Talisman of Dominance | 1 | Artifact | 2MV (or 1MV Sol Ring) acceleration, essential for fast Cecily/equipment/instants. |
| Talisman of Indulgence | 1 | Artifact | 2MV (or 1MV Sol Ring) acceleration, essential for fast Cecily/equipment/instants. |
| Teferi's Ageless Insight | 1 | Legendary Enchantment | During time other than FIRST draw in each of YOUR draw steps, EVERY card draw doubled. Peer self-target with odd library tries to overdraw: dangerous! |
| The One Ring | 1 | Legendary Artifact | Cast ETB gives protection from everything until next turn; repeated tap burden draw with escalating upkeep life loss; hand engine but life danger. |
| Third Path Iconoclast | 1 | Creature — Human Monk | Every NONCREATURE spell cast creates 1/1 artifact Soldier, direct Bjorna feed; copies are not casts. |
| Thought Vessel | 1 | Artifact | Rock and no maximum hand size; removes Cecily cleanup 11 ceiling enabling long holds, does not change 11-cards trigger. |
| Toxic Deluge | 1 | Sorcery | Stack/board removal keeps Cecily attack trigger/large hand engine alive. |
| Trade Secrets | 1 | Sorcery | OFFICIALLY BANNED but designated project-authorized. Opponent draws2 then caster draws up to4, then TARGET OPPONENT (not you) chooses repeat cycles. |
| Training Center | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Triskaidekaphile | 1 | Creature — Human Wizard | Wins at upkeep with exactly 13 (not 11) and no max hand; expensive ability draws. |
| Underground River | 1 | Land | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Underworld Breach | 1 | Enchantment | Escape inst/sorc from GY for regular mana and exiling three other cards, after EOT sac; Wheel/Jeska's Will loops NEED grave fuel and sufficient mana per iteration. |
| Vampiric Tutor | 1 | Instant | Tutors wheel/Peer/interaction to hand or top; Cecily only casts instant/sorcery FROM HAND. |
| Watery Grave | 1 | Land — Island Swamp | Mana base: UBR fixing and 4MV Cecily/high-cost free spell tempo. |
| Wheel of Fortune | 1 | Sorcery | Discard all players' hands then draw seven, supports Breach/Notion Thief, can RESET Cecily hand if no refill. |
| Wheel of Misfortune | 1 | Sorcery | Each secretly choose >=0; highest number chooser takes highest damage, non-lowest discard draw7. No simple repeatable unconditional wheel. |
| Whispering Madness | 1 | Sorcery | Each discards then draws equal greatest discarded hand size; cipher when encoded allows optional free COPY CAST on creature damage. Casting cipher copies is CAST; timing. |
| Windfall | 1 | Sorcery | All players discard then draw MAX number any player discarded; can fill to 11 only if discarded largest hand >=11. |
| Xander's Lounge | 1 | Land — Island Swamp Mountain | TAPPED UBR fixer, colored requirements versus tempo. |
| Yawgmoth's Bargain | 1 | Enchantment | OFFICIALLY BANNED project exception. SKIP draw step; pay1 LIFE draw1 repeatedly, can build 11-card hand, low-life danger; replacements with lifegain/card draw payoffs. |

### Companion audit (NOT a main-deck row)

`Lutri, the Spellchaser` — banned_as_companion in official Commander, specifically project permitted; Companion condition (each nonland name distinct in starting deck) satisfied by singleton main deck. In Companion role it is an additional OUTSIDE-deck card, not third commander nor part of 100. Pay {3} as sorcery to put Lutri into hand (companion action, not casting it). Later cast `{1}{U}{R}`, with Flash, and its ETB copies target **INSTANT OR SORCERY SPELL YOU CONTROL** only if it was CAST; not on flicker. Original spell must remain on stack as a legal target. Use exactly one card in outside companion zone; don't invent a ban waiver for ordinary Commander play.

## Candidate pool and competing cuts

Source M5 optimizer 58 Pass-A, 23 Pass-B technical candidate pairs, ZERO exact-overlap agreements, and earlier Oct13 approved dossier candidate decisions. M5 raw scores are NOT player-tested superiority. Named alternatives:

| Addition → named cut | Positive and negative expected outcomes | Current disposition |
|---|---|---|
| **Alhammarret's Archive → Dark Deal** (M5 A) | Artifact Archive doubles most your card-draw outside draw step and lifegain, increasing odds eleven and triggering Crawler/Niv; BUT five-mana setup, doesn't directly provide the same wheel discard engine and can cause catastrophic overdraw with Peer/Teferi. Dark Deal itself also fuels graveyard/Breach and shrinks hands. | CONDITIONAL high-risk study, not automatic improvement; retain Dark Deal. |
| **Aether Syphon → Dark Deal** (M5 A) | New candidate ranked but card Oracle/legality and hand-synergy not independently verified in this review; cannot assert an effect, legality or clear superior cut. | UNRESOLVED, no swap. |
| **Ophidian Eye → Wheel of Fortune** (M5 B) | Eye can be attached to Niv-Mizzet to create a repeat draw→damage chain in suitable stack, adding another compact combo. But removing Wheel of Fortune cuts a premier seven-card reset, Notion Thief burst, graveyard load, and core Cecily 11-hand refueling. | REJECT exact cut; no forced generic combo. |
| **Orcish Bowmasters → Wheel of Fortune** (M5 B) | Powerful opponents-draw punishment and token body, but Wheel contributes direct hand-size/wheel strategy while Bowmasters is a payoff only. | REJECT cut. |
| **Nekusar, the Mindrazer → Wheel of Fortune** (M5 B) | Grixis wheel payoff punishes draws but wheel availability is prerequisite; cutting premier wheel to add wheel payoff reduces enablers. | REJECT pair. |
| **Kefka, Court Mage → Wheel of Fortune** (M5 B) | Off-command brand-name alternative demands independent Oracle and payoff fit; Wheel is a pillar for Cecily and Notion Thief. | NO supported superiority. |
| **Darkwater Catacombs → Takenuma, Abandoned Mire** (M5 B) | Filters U/B at cost of colored activation and loses Takenuma's late channel grave creature recursion utility. Replacing legendary utility source with conditional filter changes ceiling/tempo, not guaranteed higher UBR. | HOLD. |
| **Izzet Boilerworks → Takenuma, Abandoned Mire** (M5 B) | Bounce land reuses ETBs but enters tapped and risks 2-for-1 land removal, while Takenuma usually enters untapped and recovers creature. | REJECT. |
| **Heat Shimmer → Underworld Breach** (M5 B) | Copying creature temporarily can duplicate magecraft/ETB and combo, but Breach is core graveyard replay of WHEELS, Jeska's Will, high-value free spells. Losing Breach hurts actual combo axis. | REJECT. |
| **Robe of the Archmagi → Reckless Fireweaver** (historical) | Fireweaver triggers on artifact creation but was explicitly removed to give WIZARD Cecily a 1-mana-equip on-hit draw engine for 11-card attack turns. Reversing swaps breaks already approved identity work. | KEEP approved Robe. |

Overall HOLD pending tested, named beneficial cut. No blanket exclusion of future candidate, but every named contender must increase actual Cecily free-spell probability and/or Bjorna artifact/goat control without net dilution. Avoid automatic proposed upgrade from zero-exact-agreement optimizer.

## Oracle, legality and rules

1. Two `partner—friends forever` commanders count IN the 100. Their color identities U/R + U/B/R combine UBR, both official Commander legal by themselves. Outside companion Lutri is officially BANNED as Commander/companion and allowed only by this project, not a normal Commander legality pass. Trade Secrets and Yawgmoth's Bargain official Commander banned, project authorized. Official-legal derived projection substitutes cards but is NOT CANONICAL.
2. Cecily max hand eleven operates only at cleanup; it doesn't prevent 12/13 cards between draws. Check eleven or more AFTER drawing one and LOSING one life in ATTACK trigger; may CAST an instant/sorc from HAND only then, without mana cost. Alternative costs cannot also be paid if casting without paying mana cost (additional mandatory costs still apply). Subsequent cleanup discards down to current maximum unless Thought Vessel/Triskaidekaphile change it.
3. Harmonic Prodigy doubles Cecily's ATTACK triggered ability because Cecily is another Wizard you control; two independent draws/life-loss/eleven-checks, possibly two distinct instant/sorc free spells if each check satisfied. It never doubles Bjorna TAP/sac activated ability, Bjorna is not Wizard and its ability isn't triggered.
4. Robe equipped to Cecily (Wizard) costs 1 to equip at sorcery speed vs four normal; drawing from combat DAMAGE is LATER THAN attack-trigger eleven check, so it improves future attacks, not the same initial trigger. Bjorna as Human, not Wizard, would need normal equip4. Robe combat damage draw with Teferi replaces each normal draw with two, but increases overdraw risk.
5. Bjorna TAP and sacrifice artifact are COST; opponent cannot remove sacrificed Clue/Treasure 'in response' after cost paid. Bjorna deals 1 to creature on resolution then GOADS it; if creature dies from that damage, goad doesn't create future attacks. Goad doesn't eliminate/blocking rights on same turn. Oni-Cult Anvil creates Construct only once each YOUR turn when own artifact leaves; opponent-turn Bjorna activations don't create Anvil 1/1.
6. Academy Manufactor changes creation of one Clue/Food/Treasure into one of EACH; Big Score two Treasures becomes two Treasures plus two Clues plus two Foods if Manufactor survives. Trigger doesn't recurse infinitely from its own replacement. Artifacts then split among Bjorna ping/goad, Deadly Dispute, Sai, Oni Anvil and mana/draw.
7. Lutri: singleton eligible as companion, pay THREE generic as SORCERY to put into hand from outside game, then separately CAST for 1UR. On ENTERS only IF CAST copies a targeted inst/sorc spell YOU CONTROL that remains on stack. Paying 3 is not alternate to printed mana cost, nor a life payment, and blink/reanimate doesn't generate its cast-only ETB copying effect.
8. Peer into the Abyss: target draws ceil(L/2) cards, loses ceil(HP/2) life. With Teferi's Ageless Insight while resolving Peer OUTSIDE your draw step, EACH Peer draw becomes two. For library L even, 2*ceil(L/2)=L, empty library is legal until another draw attempt. For L odd, result L+1 attempts, so the player LOSES for attempted draw from empty library as soon as state-based actions are checked (before queued Psychosis Crawler draw triggers can save them). The source blueprint flagged this parity; never call it unconditional safe combo. During own draw step special first-draw exception would change count only if Peer actually resolves there.
9. Psychosis Crawler: for every completed draw each OPPONENT loses one LIFE (not damage). Can convert large safe Peer draw into lethal, but if drawing player decks themselves, they lose at SBA before waiting Crawler triggers resolve. Niv-Mizzet Parun draw trigger deals DAMAGE to target, likewise queues until after spell/ability resolves.
10. Teferi's Ageless Insight doubles each of your draws except first one during EACH of your draw steps; NOT a triggered effect and NOT optional. Notion Thief replaces opponents' noninitial-step draws with YOU drawing, so with Wheel/Windfall you could draw several opponents' wheels, then Teferi doubles, possibly decking yourself. Don't state a fixed 28 cards without number of players/current hand-size/wheel considered.
11. Trade Secrets banned/project permitted: target opponent draws TWO then caster draws UP TO FOUR; TARGET OPPONENT may decide to repeat, not caster. With Notion Thief, opponent's two non-drawstep cards may become YOUR draws; they will likely refuse further iteration, so no guaranteed arbitrary cards.
12. Yawgmoth's Bargain banned/project permitted: skips your draw step, activated pay ONE LIFE for one card; the cards received enable eleven only while enough life. Paying last remaining life can cause a game loss at next SBA before further benefits.
13. Triskaidekaphile wants EXACTLY THIRTEEN cards at upkeep, removes maximum hand size; eleven Cecily free-spell threshold remains only eleven, so not automatically win at eleven. Thought Vessel similarly has no maximum but does not change free spell requirement.
14. Underworld Breach gives inst/sorc/grave escape at normal mana plus exiling three other grave cards; Wheel of Fortune plus Jeska's Will isn't intrinsically infinite without all required red mana, grave fuel and enough spell events. Source blueprint marks a candidate win line, not a fully paid universal guarantee.
15. Extra copies of SPELLS are generally NOT cast. Lutri only copies if Lutri CAST and its ETB resolves; Mnemonic Deluge uniquely instructs the controller to COPY then CAST the copies; spell-copy magecraft interactions depend on these exact terms.

## Finite sequencing and adversarial scenarios

**A — attack threshold, no Robe retroactivity:** Cecily ready to attack with TEN cards in hand, including Peer and another spell. Declare Cecily attacking; its ability draws one card and you lose1 life, hand now ELEVEN. During trigger resolution cast Peer for zero mana from your hand and resolve later. Robe's possible combat-damage draw has not happened yet and cannot fill hand for this attack. If Cecily has only nine before trigger and no Teferi/Harmonic extra draw, ends at ten and cannot cast a free spell.
**B — doubled trigger:** Cecily + Harmonic Prodigy on BF, attack while hand nine and Teferi's Ageless Insight on BF. First Cecily trigger draws 2 (outside draw step) to eleven, lose1, can cast inst/sorc from hand. Second trigger draws two more, loses1, independently checks threshold. If second free spell not in hand or first reduced hand too low the second may fail; triggers aren't automatic two casts. Important: casting first instant sorcery may modify board and hand before second resolves.
**C — Bjorna token route:** With Bjorna untapped (no summoning sickness), Academy Manufactor, one Big Score casting and a spare card to discard as cast-cost, Big Score resolves to draw2 then create two Treasures, replaced with two each Treasure/Clue/Food. Activate Bjorna pay tap+sac one Food or Clue to target opponent 4/4, Bjorna deals1 and goads it. It REMAINS able to block Cecily this turn; on opponent turn it must attack a different player if legal. Sac second Treasure can pay mana later; Bjorna cannot activate twice without untap.
**D — Peer parity and fatal risk:** L=41 cards library, Teferi in play, cast Peer on SELF outside draw step. Peer instructs draw21; Teferi replacement demands 42 draws, attempt 42nd from empty library -> you LOSE as SBAs checked before Psychosis triggers. If L=40, Peer instructs draw20 -> 40 draws leaves library EMPTY, no immediate decking loss just from zero cards remaining; Psychosis Crawler draws trigger 40 opponent life-loss pings on stack and may kill before future draw. However any additional compulsory draw can kill you. Low self life may also kill from Peer losing half life rounded up.
**E — Trade Secrets exception political:** Cast Trade Secrets targeting opponent during your turn, possibly with Notion Thief. Opponent's two draw events can be replaced by you drawing two, then you may choose up to4 draws, giving up to6 cards before the opponent decides whether to repeat. Opponent may choose NO repeats, so cannot force loop; Teferi may double the replacements and threaten deckout. Trade Secrets is approved only by project exception.
**F — wheel+Notion Thief and resource abuse:** Suppose four players and Windfall where maximum discard is ten. Everyone DISCARDs hands, then each would draw ten. Notion Thief redirects the three opponents' draws to you (30 cards) in addition to your own ten, so normally you draw 40 cards; with Teferi Insight you attempt 80 card draws. This may win via Crawler/Niv if library survives or can immediately deck YOU. Risk shows why more draw replacement power isn't automatic upgrade.
**G — counterplay:** Opponent's Ghostly Prison effects might require attack mana, creature removal can stop Cecily before attack, Stifle-type effects counter a trigger, an instant killing Cecily AFTER trigger on stack won't counter that trigger by itself, but needed hand/payload and creature still matter. Rule of Law may permit one cast per turn, and Cecily's free cast is CAST so cannot bypass Rule of Law limit. Grave hate stops Breach/Wheel loops, not cast-free from hand. With No Mercy hostile body or damage prevention, Robe may not connect; Bjorna's goad doesn't stop blocks. With life under three, Yawgmoth's Bargain/Peer and Cecily loss are material.

## Conclusions and unresolved evidence

**STRATEGIC HOLD** on the APPROVED 100 plus separate project exception companion. The library and command zone explicitly remain 100, the companion is outside. Central gameplay genuinely emphasizes Cecily eleven-hand threshold, massive free instants/sorceries, Bjorna artifact-sacrifice politics, synergistic wizard/card draw and Lutri copying; replacement by generic Grixis value/wheel payoffs without increasing eleven-card attack probability would homogenize. No source-backed improvement displaced Robe, wheel density, Breach or token fuel. The biggest real risk discovered is self-deck with Peer + Teferi and overly large Notion wheel; this is a PILOTING/COMBO documentation issue, not a Commander deck structural defect or invitation to remove documented exceptions.
**Not measured:** colored Cecily cast chance on turn4, eleven-card hand by protected turn5 attack, win rate against multiple opponents, artifact fodder turns per Bjorna activation, Breach mana/payment loop in real Forge games, and new candidate Aether Syphon's actual Oracle/legality. These remain explicitly unresolved, not falsified experimental results. No independent Pass C or formal M6 certification claimed.

## Source and test receipts

- Exact approved source https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/decklists/Cecily__Bjorna__Lutri_Approved_2026-10-13.txt ; raw SHA-256 `553838da88fe00974e74664633be5051c4f1a0879baa71de81ca9f880e5a6d28`, explicit October13 companion count and project exception record `refinement/approvals/Cecily__Bjorna__Lutri_Approved_2026-10-13.md`.
- Per-card October16 Scryfall audit `refinement/verification/retrospective_1_to_8/Card_Verification_Cecily__Bjorna__Lutri_2026-10-14.csv`: 99 main-deck NAME rows, 100 main-deck copies, plus separate outside-deck Lutri row => 100 source names, 101 total physical entries; 3 `PROJECT_EXCEPTION` and others official Commander legal. Engineering exception registry preserves all three. Canonical approval state remains `APPROVED/LOCKED`, retrospective `PASS_PROJECT_EXCEPTION`.
- Engineering blueprint `data/grixis/blueprints/bjorna-nightfall-alchemist-cecily.json`, historical source `refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md`, M5 optimizer `data/grixis/m6/optimizer/bjorna-nightfall-alchemist-cecily.json` with 58+23 projections and no A/B agreement.
- Current Oracle reference https://mtg.wtf/card/slx/3/Cecily-Haunted-Mage and draw replacement https://mtg.wtf/card/m21/294/Teferis-Ageless-Insight . Rules parity support https://www.reddit.com/r/mtg/comments/1ldcorc/peer_into_the_abyss_teferis_ageless_insight/ . Current comprehensive rules https://magic.wizards.com/en/rules and official format banned-list https://mtgcommander.net/index.php/banned-list/ ; project overrides clearly separate from official compliance.
- Final review validation via GitHub M6 exact-head source/queue no-skip and adversarial CI must pass before tracker completion. No canonical decklist/hash, exception, official-legal projection, GrokBot Pass C or formal M6 acceptance changed.
