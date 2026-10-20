# M6 comprehensive authored single-deck review #47 — Rograkh, Son of Rohgahh // Silas Renn, Seeker Adept

**Tracker key** `RogSi` index46, deck #47/62. **Review author ChatGPT** (not independent GrokBot Pass C), **2026-10-20**. **Owner action** NONE. **Disposition** KEEP exactly approved 100; conditional objections/candidate proposals captured without changing cards.

## Source and test receipts

Recovered live `corymstover/GrokBotMTGCompanion` integration `chatgpt-cycle76-m6-refinement`: `AGENTS.md`, `grixis/M6 Commander-First Single-Deck Review Standard.md`, depth tracker (46/62 complete before #47), registry, `data/grixis/milestone_m6_m7_subtracker.json`, `data/grixis/m6/review_packets/rograkh-son-of-rohgahh-silas-renn.json`, `data/grixis/mana_base/rograkh-son-of-rohgahh-silas-renn.json`, `grixis/interactions/rograkh-son-of-rohgahh-silas-renn.md`. Canonical `corymstover/grixis-commander-encyclopediaGPT/main`: `state/current_deck_overrides.json#decks.RogSi`, [approved TXT](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/decklists/RogSi_Approved_2026-10-15.txt) Git blob `6b7827592ff0f2eaca004b4b02a9867ed49a0879`, Oct15 approval, targeted verification, 98-slot audit, rules gate and candidate closeout.

**Immutable source:** `APPROVED / LOCKED` Oct15 2026, authoritative exact SHA-256 `06c9e22b5afc46bd58bbbfdef5c42a796d2a986a2972456107c29aee1b5f905c`, engineering logical `lh1:2f1326f4b41ecefd086deec69eb25dd097886b4903115d5f060ea4db5df35fa1`. No canonical changes or source identity discrepancies, **no project exception**. Official Commander legality Oct15 and engineering 2026-10-16 Scryfall bulk `compliant`. Rograkh & Silas both have PARTNER and together UBR color identity, independent separate commander taxes. **Independent TXT recount**: 100 physical 1x cards, **2 commanders**, **98 library** cards, **24 lands**, 100 distinct names, zero repeated names, full singleton compliance. This approved 100 supersedes prior Oct12 FINAL, whose 7 swaps were adopted/approved Oct15; do not reapply.

**Source evidence:** Original partner approval documented classic turbo-Naus/Breach vs Monolith artifact-branch, final 7 replacements: Timetwister→Final Fortune; Retraction Helix→Mnemonic Betrayal; Orcish Bowmasters→Vexing Bauble; Talisman Indulgence→Talisman Dominance; Training Center→Demonic Counsel; Luxury Suite→Wooded Foothills; Morphic Pool→Undercity Sewers. M5 `51` candidate/cut hypotheses, 13 test pass, 9 fail, 18 inconclusive, 11 undetected; P0=3 P1=10 P3=38. Those are limited engine screening outcomes, not audited cEDH win percentages. Engineering interactions verified 7 of 8 Oracle/CR cases, with **one explicit Vexing Bauble dependency warning**. [Wizards Vexing Bauble official MH3 ruling](https://magic.wizards.com/en/news/feature/modern-horizons-3-release-notes), [Necrodominance text](https://mtg.wtf/card/pmh3/102s/Necrodominance), [Demonic Counsel](https://mtg.wtf/card/dsk/92/Demonic-Counsel), [Silas Renn](https://mtg.wtf/card/brc/129/Silas-Renn-Seeker-Adept), [Hexing Squelcher current WotC Jan2026](https://media.wizards.com/2026/downloads/ECL_Release_Notes_06HVqa76yI/AIuLLXK62r_EN_MTGECL_ReleaseNotes_20260106.pdf), [Samut current Oct2 2026](https://mtg.wtf/card/fra/302/Samut-Tyrant-of-Naktamun). EDHREC [RogSi Ad Nauseam cohort](https://edhrec.com/commanders/rograkh-son-of-rohgahh-silas-renn-seeker-adept/ad-nauseam) retains high inclusion for Breach, Oracle, Consultation and fast mana; community deck counts aren't controlled performance proof.

**Test scope:** manually checked every approved name and source cost, all material M5 route families and offranking Brainstorm/last-chance/Monolith/review alternatives, explicit costed finite traces below. No fresh full Oct20 Scryfall API 100-card dump or actual 4-player randomized gameplay is claimed; no pipeline rerun, current source Oracle snapshot cited.

## Commander identity and natural ceiling

**Rograkh {0}**: red (red color indicator) 0/1 legendary Kobold Warrior with first strike, menace and trample; supplies a free commander on first cast, immediate battlefield material, legendary-red Mox Amber, Springleaf Drum, sacrifice for Culling the Weak/Infernal Plunge/Diabolic Intent/Flare of Duplication, and commander presence for free Fierce Guardianship/Deadly Rollick/Deflecting Swat and Jeska's Will's both-mode cast. Each *commander's* command tax is separately +{2} per previous cast from command zone. Second Rograkh after dying costs {2}, not {0}, so infinite free sac/recast never follows from having a 0 printed cost. Rograkh is **NOT artifact**, so his presence doesn't turn on Mox Opal metalcraft or Grinding Station artifact-ETB untap.

**Silas Renn {1}{U}{B}**: blue/black 2/2 legendary **artifact** creature with deathtouch; on combat damage to **player**, choose target **artifact CARD** in your graveyard and you may CAST it that turn. Must pay normal costs, follow normal timing (artifact sorcery speed usually), and target be in GY when triggered/permission applies. Silas provides blue/black in identity, a legend for Amber, a second commander for protection, real salvage of Lotus Petal, zero-cost rocks, Station or LED if it connected, and is an artifact itself for metalcraft when fielded. However 3 mana plus combat survival/connection is much slower than Rograkh's turn-one mana plan: cannot pretend both partners are always on the field. Combining them gives **UBR**.

**Commander-first cEDH identity:** 24-land turbo Ad Nauseam/ritual and Breach-LED-Brain Freeze and compact Oracle+Consultation/Pact. Fast mana is amplified by zero commander, fast untapped colored land sources, free-mana/pitch counterspells, oppressive first-turn mana, fast draw, tutors; artifact-value Silas undergrinds if early storm fails. Natural **Bracket 5 — cEDH** is warranted by density and known competitive shell, not unverified actual current event win rate. Must preserve creature-sacrifice/free-commander payoff, artifact recurrence fallback, not migrate to unrelated slower generic Hullbreaker/Monolith purely for extra card ranking.

## Full 100-card role audit

**100 exact source TXT singleton name rows, including BOTH commander rows, 24 independent lands, 74 other noncommander slots.** The library has 98 cards, not 99. One row per source name in original order, with non-generic costs/risk and role.

| Row | Exact approved card name | Commander-specific role and main caveat |
|---:|---|---|
| 1 | Rograkh, Son of Rohgahh | COMMANDER Rograkh {0} 0/1 legendary RED Kobold, first strike/menace/trample; sacrifice/tap/legend/free commander engine, not itself artifact. |
| 2 | Silas Renn, Seeker Adept | COMMANDER Silas {1}{U}{B} artifact 2/2 deathtouch, player-combat-damage trigger targets GY artifact permitting CAST this turn with timing/mana. |
| 3 | Ad Nauseam | 3BB instant repeated top reveal/pick life payment per MV; 0/1-cost density strongly supports turbo plan but life budget and counter-window matter. |
| 4 | An Offer You Can't Refuse | U noncreature counter costing opponent two Treasure tokens; excellent early shield with meaningful resource downside. |
| 5 | Ancient Tomb | Land: CC and 2 life loss, speeds setup but not colored pips, worsens Ad Nauseam life. |
| 6 | Arcane Signet | 2-mana UBR fixer, slower than pitch/ritual burst but supports card turns and UB Silas. |
| 7 | Arid Mesa | Land: Fetch land for subtype-matched UBR dual/shock/surveil land; life plus potential tapped target. |
| 8 | Badlands | Land: Fetchable untapped typed original dual/shock (life cost if shocking), essential UBR and Silas {1}UB. |
| 9 | Beseech the Mirror | 1BBB tutor can cast selected MV4-or-less spell free ONLY after bargain additional sacrifice; colored BBB real. |
| 10 | Birgi, God of Storytelling // Harnfel, Horn of Bounty | Ritual refund {R} per spell cast on creature face; Harnfel hand-discard into exile cards, converts dead draws into storm velocity; enormous Rograkh zero-spell payoff. |
| 11 | Blood Crypt | Land: Fetchable untapped typed original dual/shock (life cost if shocking), essential UBR and Silas {1}UB. |
| 12 | Bloodstained Mire | Land: Fetch land for subtype-matched UBR dual/shock/surveil land; life plus potential tapped target. |
| 13 | Borne Upon a Wind | 1U instant to cast spells as though flash this turn, enables end-step refill/stack combo but not mana itself. |
| 14 | Brain Freeze | 1U storm mills chosen library; self-mill Breach/LED fuel and opponent mill win after adequate storm; storm counts spells CAST, not copies. |
| 15 | Cabal Ritual | 1B adds BBB or BBBBB with threshold seven graveyard cards; critical timing with Breach escape exiles. |
| 16 | Chain of Vapor | U bounce nonland permanent; copied via sacrificing land can produce interaction or replay own LED/Mox but gives opponent choices. |
| 17 | Chrome Mox | Zero-mana imprint nonartifact nonland card for one selected color; hand loss may matter under Ad Nauseam and fast turn. |
| 18 | City of Brass | Land: Untapped any-color fixer costing life/damage, vital 24-land UBR pacing. |
| 19 | City of Traitors | Land: CC, sacrifices itself upon playing another land; turbo generic, bad longer-game land stability. |
| 20 | Command Tower | Land: Untapped UBR source for color requirements, 0 commander first cast doesn't demand colored. |
| 21 | Culling the Weak | B + sacrifice creature as additional COST -> BBBB, Rograkh native, cannot respond before creature was sacrificed. |
| 22 | Dark Ritual | B -> BBB, turbo black for Ad Naus/Necropotence but not U/B split. |
| 23 | Daze | 1U or return Island to hand alternate cost, countermagic tempo; blue pitch/Island present as typed duals, source return weakens land board. |
| 24 | Deadly Rollick | 3B creature exile, free if any commander controlled (Rograkh immediately), not answer to spell or noncreature hate. |
| 25 | Defense Grid | Two-mana artifact taxes each spell cast outside its controller's turn by 3; enemies' turn responses to our win cost more, our own offturn instant protection also taxed. |
| 26 | Deflecting Swat | 2R redirect target(s), free if Rograkh or Silas in play, cannot protect against untargeted wipe. |
| 27 | Demonic Consultation | B instant dig/exile many cards (naming absent card empties remaining library), high danger if Oracle absent in hand and incorrectly chosen. |
| 28 | Demonic Counsel | 1B sorcery tutor Demon ONLY until delirium 4 card types in GY; THIS LIST HAS NO DEMON, so pre-delirium it finds zero cards. |
| 29 | Demonic Tutor | 1B unconditional search to hand, premium tutor. |
| 30 | Diabolic Intent | 1B sacrifice creature additional cost, Rograkh native search; if Rograkh from command zone recast tax grows. |
| 31 | Fierce Guardianship | 2U counter noncreature free while one of two commanders controlled, but Vexing Bauble on field may counter free cast. |
| 32 | Final Fortune | RR instant take next extra turn; lose at beginning of that extra turn's end step, no Obeka to clear it, requires win before trigger resolves. |
| 33 | Flare of Duplication | 1RR instant copy target instant/sorcery, alternative sacrifice NONTOKEN RED creature, Rograkh offers free native copy with risk of free spell being Baubled. |
| 34 | Flooded Strand | Land: Fetch land for subtype-matched UBR dual/shock/surveil land; life plus potential tapped target. |
| 35 | Flusterstorm | U storm instant/sorcery counters; targets each separate stack copy, storm copies are not CAST. |
| 36 | Force of Negation | 1UU or pitch blue in opponent's turn, counters noncreature exile; free only on opponent turn so not general free self-turn shield. |
| 37 | Force of Will | 3UU or pitch blue+one life, hard counter critical fast-game protection. |
| 38 | Gamble | R tutor then RANDOM discard from hand, graveyard salvage through Breach if piece lost and fuel remains. |
| 39 | Gemstone Caverns | Land: Only pregame color source with luck counter on draw after exile hand card; otherwise colorless; exiling not discard. |
| 40 | Gitaxian Probe | U or 2 life draw and reveal opponent hand, inexpensive storm/hand intelligence, supports active win timing. |
| 41 | Grim Monolith | 2 artifact CCC burst with 4-mana untap, colorless only, not automatic infinite without Power Artifact. |
| 42 | Grinding Station | 2 artifact tap/sac artifact mill 3, untap when ARTIFACT enters, Breach recursion fuel loop with zero rocks; target availability and exile three matter. |
| 43 | Hexing Squelcher | 1R Goblin Sorcerer uncounterable and own spells uncounterable; other creatures ward—pay two life. Shields zero spells from Bauble without stopping its trigger. |
| 44 | Imperial Seal | B sorcery topdeck tutor, 2 life, delays card access until next draw unless another draw available. |
| 45 | Infernal Plunge | R sorcery sacrifice creature additional cost -> RRR, Rograkh turns low-resource spell into turbo red. |
| 46 | Into the Flood Maw | U bounce nonland permanent, low-cost interaction against hatebear/stax/target artifact, fewer mana than giant Hullbreaker. |
| 47 | Jeska's Will | 2R two modes red mana based on target opponent hand; extra exile-top-three if commander controlled when cast, high burst with 0-mana Rograkh. |
| 48 | Lion's Eye Diamond | 0 artifact sac + discard entire hand add 3 ONE color at instant-speed activation only, pivotal Breach escape and draw sequencing; doesn't split UBR. |
| 49 | Lotus Petal | 0 sac any ONE mana, fast start/Breach replay fodder, Vexing Bauble trigger if no mana spent on cast. |
| 50 | Mana Confluence | Land: Untapped any-color fixer costing life/damage, vital 24-land UBR pacing. |
| 51 | Mana Vault | 1 taps CCC burst with expensive untap and tapped upkeep damage; cannot alone provide UBR. |
| 52 | Marsh Flats | Land: Fetch land for subtype-matched UBR dual/shock/surveil land; life plus potential tapped target. |
| 53 | Mental Misstep | U or two life counter one-mana-value spell; protects T0–T2 on stack, opponent trap/counter targets. |
| 54 | Mindbreak Trap | 2UUU or no-cost when opponent cast 3+ spells this turn; EXILES any number target spells on stack, cost conditions matter and Bauble stops free. |
| 55 | Misty Rainforest | Land: Fetch land for subtype-matched UBR dual/shock/surveil land; life plus potential tapped target. |
| 56 | Mnemonic Betrayal | 1UB exiles opponent graveyards, casts nonland cards from exile that turn (pay costs/timing), return uncast at end step, exiles itself; unlike Breach uses enemy resources. |
| 57 | Mox Amber | 0 taps for one color among LEGENDARY creatures/PWs controlled: with Rograkh alone RED, with Silas as well U/B/R any one, not 3 mana. |
| 58 | Mox Diamond | 0 discard LAND as it enters or sacrifice it, any-color steady ramp but 24-land deck increases dead draws/hand attrition. |
| 59 | Mox Opal | 0 mana source any color only at METALCRAFT >=3 artifacts counting itself; Rograkh NOT artifact, Silas is. |
| 60 | Mystic Remora | U cumulative upkeep taxed draw on opponents' noncreature spells, crucial turbo multiplayer card flow. |
| 61 | Mystical Tutor | U instant place instant/sorcery on top, supports Ad Naus/Consultation/protection but loses card tempo. |
| 62 | Necrodominance | BBB draw massive at own END STEP, max hand 5, skips draw steps and REPLACES ANY CARD/TOKEN to own GY with EXILE; Breach and delirium anti-synergy until enchantment leaves. |
| 63 | Necropotence | BBB pay life exile face-down then collect at own NEXT end step, draws high velocity; discard-to-GY creates subsequent exile trigger, not global replacement. |
| 64 | Otawara, Soaring City | Land: U mana or channel bounce, important zero-mana-risk hate removal. |
| 65 | Pact of Negation | 0 free counter, pay 3UU NEXT upkeep or lose, Vexing Bauble counters if zero spent; win turn or upkeep mana vital. |
| 66 | Paradise Mantle | 0 Equipment equip 1 gives creature tap any-color mana; newly summoned Rograkh cannot tap through sickness because ability belongs to him. |
| 67 | Phyrexian Tower | Land: Colorless or tap sacrifice creature for BB, Rograkh-native sacrifice source, opportunity cost of killing commander and subsequent command tax. |
| 68 | Polluted Delta | Land: Fetch land for subtype-matched UBR dual/shock/surveil land; life plus potential tapped target. |
| 69 | Praetor's Grasp | 1BB exile select card from opponent library face down; permits playing; politics/opponent deck condition, stax/combo theft. |
| 70 | Pyroblast | R blue spell counter/blue permanent destroy, cEDH stack tool. |
| 71 | Ragavan, Nimble Pilferer | R haste? 2/1 with Dash; on combat damage treasure/exile top opponent card; conditional unblocked fast ramp compared with 2-mana stones. |
| 72 | Rain of Filth | B instant all lands gain 'sacrifice this land: add B' until end of turn, converts future land drops into one-shot black; cannot reverse sacrifices. |
| 73 | Red Elemental Blast | R blue spell counter/blue permanent destroy, key blue mirror card. |
| 74 | Rhystic Study | 2U continuous opponent pay1 tax or draw, maintains resources post failed burst; slower than turbo rituals. |
| 75 | Rite of Flame | R -> RR in singleton starting state, graveyard other copies normally absent; spell count for Breach. |
| 76 | Samut, Tyrant of Naktamun | 1U creature grants our instants/sorceries SPLIT SECOND while on stack; triggered Vexing Bauble remains valid, and WE cannot cast spell/add nonmana activated responses while our split-second spell on stack. |
| 77 | Scalding Tarn | Land: Fetch land for subtype-matched UBR dual/shock/surveil land; life plus potential tapped target. |
| 78 | Simian Spirit Guide | Exile from hand for R one time, exile is not discard or GY fuel; relevant Ad Naus 3MV life reveal. |
| 79 | Sol Ring | 1 taps CC for cast/recast tax and artifacts, can't pay fixed U/B/R. |
| 80 | Springleaf Drum | 1 artifact mana of any color by tapping its OWN ability and an untapped creature as cost; can tap newly cast summoning-sick Rograkh this way. |
| 81 | Steam Vents | Land: Fetchable untapped typed original dual/shock (life cost if shocking), essential UBR and Silas {1}UB. |
| 82 | Swan Song | U counter instant/sorcery/enchantment, opponent gets a 2/2 flyer, protects stack. |
| 83 | Tainted Pact | 1B instant reveal/exile until select card or duplicate name; 100 unique names avoids duplicate stop, critical Oracle win after empty library. |
| 84 | Talisman of Dominance | 2-mana UB/C permanent fixing, paid 1 life for colored; helpful Oracle UU and B tutor, slower than zero rocks. |
| 85 | Thassa's Oracle | UU creature ETB win if devotion to blue >= cards remaining in library; Consultation/Pact compact competitive endline. |
| 86 | Undercity Sewers | Land: Enters tapped UB surveil1; typed Island Swamp fetch target, adds GY card types/topdeck selection but tempo cost. |
| 87 | Underground Sea | Land: Fetchable untapped typed original dual/shock (life cost if shocking), essential UBR and Silas {1}UB. |
| 88 | Underworld Breach | 1R enchant gives nonland GY cards ESCAPE: normal mana + exile THREE other graveyard cards per recast; Vexing Bauble stops zero-cost artifacts if no mana spent. |
| 89 | Valley Floodcaller | 1U creature grants instant-speed noncreature spell permissions/untap trigger, relevant with Mana rocks but fragile. |
| 90 | Vampiric Tutor | B instant 2 life topdeck any, draw access needed before payoff. |
| 91 | Verdant Catacombs | Land: Fetch land for subtype-matched UBR dual/shock/surveil land; life plus potential tapped target. |
| 92 | Vexing Bauble | 1 artifact counter EACH spell cast with NO MANA SPENT (including our first Rograkh, LED, Mox), can sacrifice for {1},{T} to draw; must be sequenced before free-spell turns. |
| 93 | Volcanic Island | Land: Fetchable untapped typed original dual/shock (life cost if shocking), essential UBR and Silas {1}UB. |
| 94 | Warrior's Oath | RR sorcery extra turn then loss at that extra turn's end step; not time-independent free advantage. |
| 95 | Watery Grave | Land: Fetchable untapped typed original dual/shock (life cost if shocking), essential UBR and Silas {1}UB. |
| 96 | Wheel of Fortune | 2R discard all and draw seven, turbo refill but gives opponents 7 counterspells and may conflict Necropotence. |
| 97 | Windfall | 2U symmetrical discard/reload based on largest hand, may fill opponent graveyards for Betrayal but also improve their shields. |
| 98 | Wishclaw Talisman | 2 artifact {1},{T} tutor and give to opponent; best used win turn to avoid giving opponent own tutor. |
| 99 | Wooded Foothills | Land: Fetch land for subtype-matched UBR dual/shock/surveil land; life plus potential tapped target. |
| 100 | Yawgmoth's Will | 2B play cards from graveyard this turn; all cards put into GY from anywhere exiled instead for duration, overlaps Breach core but stops newly generated feed. |

**Role balance:** 24 land incl. nine fetches, dual/shock typing, two city double-colorless lands, conditional Caverns, sacrifice Tower and tapped Undercity Sewers. 16 source-labeled fast mana items, five rituals plus artifact acceleration, 9 repeatable nonland sources, card advantage Remora/Rhystic/Ad Naus/Necropotence/Necrodominance/wheels/Jeska/Birgi, tutors multiple B, protection >10 pitch or low-cost counters/redirect/bounce, compact Oracle+Pact and Breach+LED+Freeze/Station. **Weakest real incumbents** Demonic Counsel before delirium, Necrodominance/Breach conflict, Grim Monolith without two-card support, and own Vexing Bauble anti-synergy, not blindly "highest M5 cut Birgi". Silas's slow combat permission is fallback, not a free second infinite combo.

## Mana, turns, card advantage and protected combo lines

**Sources:** 24 lands / no basics / nine fetches; source model nominal land colored counts B14/U14/R12, repeatable-inclusive B20/U20/R17. Mox Amber with **Rograkh alone makes RED only**; to make blue/black need Silas (which also adds artifact count), while Mox Opal requires 3 artifacts including itself. Talisman Dominance provides UB but not red; Phyrexian Tower sacrifice Rograkh makes BB not R; Chrome Mox imprint consumes card and color determined by exiled card; Mana Vault/Sol/Grim/Ancient Tomb/City of Traitors create colorless, cannot fund BBB Necropotence or UU Oracle alone. On no-mulligan T2 two-land presence 0.70 and T4 four-land presence 0.264, **not real cast probabilities under cEDH mulligans**. Keep 24 lands intentional because 0/1 rocks + rituals; aggressively mulligan uncastable colors rather than trust static source count.

**Turn examples:** T1 Rograkh costs {0}, Springleaf Drum {1} can tap Rograkh as an additional cost of Drum's own activated mana ability even if newly summoned; Paradise Mantle {0} equip{1} gives Rograkh a tapped mana ability and THEN he needs haste/next turn, summoning sickness applies. Culling the Weak costs B + sac Rograkh -> BBBB, Net BBB after B paid and taxes Rograkh next zone cast. Infernal Plunge costs R + sac Rograkh -> RRR, net RR. Rograkh + Mox Amber gives single red; need artifact support for Opal. `Necrodominance` requires BBB and begins draw at END STEP, so if going off on main phase before its trigger it has produced ZERO extra cards yet.

**Breach-LED-Freeze:** Underworld Breach 1R grants escape normal cost + EXILE 3 other GY cards. LED artifact {0} escapes with three OTHER cards exiled, activate/sac/discard hand for BBB/UUU/RRR all one chosen color. Brain Freeze 1U from graveyard costs 1U plus 3 other GY exiles; storm counts spells cast *this turn*, not copies, so self-mill adds GY fuel each copy and can replenish escape while loop remains legal. Grinding Station plus recast 0-MV artifacts (LED, Lotus Petal, Amber, Moxen) can feed 3 GY cards with artifact ETB untap; must pay all escape exiles and maintain target/legend/metalcraft requirements. **Vexing Bauble** counter-trigger fires on EVERY spell cast if **zero mana spent**, including own LED escape and first 0 Rograkh; ritual-paid colored spells normally unaffected. If Bauble on battlefield **sacrifice with {1},{T} to draw** first (but not if tapped newly cast artifact? artifact's {T} abilities usable even newly cast as noncreature), or have **Hexing Squelcher** so spells cannot be countered (triggers still occur). Even Samut split second does **not** silence Bauble's trigger. [Wizards official rules](https://magic.wizards.com/en/news/feature/modern-horizons-3-release-notes).

**Oracle+Consultation / Pact:** Thassa's Oracle costs UU, ETB victory when devotion to blue >= remaining cards (empty library always satisfies); DConsult B naming card no longer present in library can remove remainder. Tainted Pact 1B never stops on repeated names because source 100 unique; choose no card until exile rest. Opponents can respond to Oracle trigger and spells, and remove Oracle to change devotion if library not empty (with 0 cards, 0 devotion is enough). Bauble on field won't counter normal mana-paid Oracle/Consult; free response shields may be baubled. Removing Necrodominance before Breach if its global GY-exile effect active is a real sequencing dependency; don't combine mutually antagonistic engines as though synergistic.

**Reload risk:** Necropotence BBB lets pay 1 life per card into delayed next-end-step hand, discard GY exile trigger; Necrodominance BBB skip draw, END STEP life/draw and replacement *all cards/tokens to own graveyard instead exiled*, five maximum hand; Breach requires populated GY, Demonic Counsel requires 4 card types IN GY. Necrodominance **stops new delirium development and GY fuel** while it remains, unlike Necropotence's narrow discard-trigger exile. Yawgmoth's Will creates GY replacement for turn and is a separate replay engine, not Breach feeder for spells cast/discarded after resolution. These are high-ceiling but incompatible simultaneous modes, which cEDH tuner should handle by sequencing line based on state.

## Candidate pool and competing cuts

**51 actual M5 candidate/cut hypotheses, not 51 independently proved winners.** 13 limited test pass, 9 fail, 18 inconclusive, 11 undetected. Three independent agreement routes assess Enigma Jewel vs Birgi and Hullbreaker/Tidespout vs Into the Flood Maw; ten performance-only routes have no commander-specific burden proof. Ranked off-branch alternatives, real weak cuts and source paid opportunity-cost judgments:

| Challenger(s) and M5 source | What is cut vs alternate weaker candidate | Decision and commander-specific trade |
|---|---|---|
| **The Enigma Jewel // Locus of Enlightenment** (P0 rank21) | M5 proposes **Birgi/Harnfel**; alternative `Grim Monolith` (no Power Artifact) | **REJECT Birgi cut**: Jewel U, enters tapped, tap CC **only usable to activate abilities**, cannot cast Ad Nauseam/Oracle/commander, nor generally enable Breach. Craft 8U plus 4 nonland activated-ability cards is hugely expensive in 24-land turbo. Grim is more plausibly replaceable but still CCC burst relevant to fast Ad Naus; without measured upside, no swap. [Oracle](https://www.mtg.wtf/card/lci/362a/The-Enigma-Jewel). |
| **Hullbreaker Horror / Tidespout Tyrant** (P0 #109/#481) | M5 removes `Into the Flood Maw` (U instant bounce); alternate expensive slot `Grim Monolith` | 7–8 MV independent noncreature/creature bounce combo branches can be effective off artifact Mox/LED, but Ad Nauseam revealing 7–8 costs life and cannot simply replace T1 one-mana hate bounce. Still commander flavor less direct than turbo sac+fast resources. **Reject direct swap** without established event-based better branch. |
| **Fellwar Stone / Talisman of Creativity** (#8/#13) | M5 removes Birgi. Alternative `Demonic Counsel` conditional dead pre-delirium | 2-MV repeatable colored source can make 24-land deck more resilient to mulligan, but replacing Birgi's one-red rebate per cast/Harnfel discard-through weakens burst. `Fellwar IN / Demonic Counsel OUT` is a **conditional slower/colored-starved pod challenger**, no proven turn-1 speed lift. |
| **Brainstorm** (off-ranking; M5 #24 cuts Bauble) | Auto model removes `Vexing Bauble`; **better alternative cut Demonic Counsel** | Brainstorm {U} live turn one with fetch shuffles and allows pitch spell/top sorting even before four graveyard types. Counsel {1}{B} finds NO card until delirium (zero Demon targets here), but once active it is an unrestricted tutor, stronger than Brainstorm. **Strongest evidence-based conditional proposal: Brainstorm IN / Demonic Counsel OUT IF pre-delirium dead draws repeatedly lose windows.** Keep Bauble because opponents' free spells matter. No owner approval applied. |
| **Wheel of Misfortune / Burning Inquiry** (#15/#440) | M5 removes Bauble/Necrodominance | Adds card velocity or discard but symmetrical opponents get resources and Inquiry random; neither protects turn 1/2 from opposing zero spells. Necessarily verify 2026 list and role of own Necro. **KEEP**. |
| **Narset's Reversal / Reiterate / Retraction Helix / Banishing Knack** (#198,371,29,729) | M5 cuts `Final Fortune` or `Into the Flood Maw`; original Oct15 cut Helix already owner-approved | Countercopy/replay or artifact bounce combos can be valid under Valley Floodcaller but require extra specific creature/mana and often need opponents casting spell. Final Fortune is strong immediate extra-turn protected win conversion. Generic stack combo cannot replace a 1-mana universal bounce answer or turbo turn on rank only. **KEEP**. |
| **Stitcher's Supplier / Grinning Ignus / Cool but Rude / Alania** | M5 pushes cutting Oracle, Jeska's Will, Rain of Filth or Necrodominance | Supplier fills GY but gives opponent window and one creature slot to activate; Grinning Ignus loops need cost rebates; all worse than existing compact Oracle finish/mana enabling a real T2–T3 kill unless context proven. **REJECT essential slot swaps**. |
| **Power Artifact + Grim Monolith / full artifact branch** | Could swap Birgi, Grim counterpart? | Power Artifact enchanted Grim reduces its {4} untap to {2}, tap adds CCC and costs CC to untap -> unbounded COLORLESS; still needs payoff and correct blue/red/black mana. Needs at least one more card for legitimate win and weakens T1 reload/storm if missing. A coherent alternate *different build* not automatically superior RogSi encyclopedia classic turbo. **NO conversion authorized**. |
| **Memnite, Adaptive Training Post, Saheeli, Pyromancer's Goggles** | Replace Birgi in M5 | More artifacts to turn on Opal/Station, but Memnite no Rograkh free-commander significance, 3+/5-mana engines too slow versus Birgi spell refund/Harnfel. HOLD. |
| **Platinum Angel/Emperion/Enter the Infinite/Lich** | M5 removes Birgi, Necrodominance, Bauble | Large MV crushes Ad Naus life flips; Angel/Emperion do not protect from nonlife instant wins or disenchant removal. No commander-first win gain. **REJECT**. |
| **Noxious Revival / Brainstorm, off-ranking cheap optimization** | `Demonic Counsel` or `Grim Monolith` | Noxious Revival can topdeck key graveyard card (cost 2 life or green hybrid paid as life), break opposing graveyard target at instant speed, but card disadvantage and graveyard interference to our Breach; Brainstorm more generic velocity. **Conditional only**. |

**Three material structural debates:**
(A) `Demonic Counsel` is unlike Demonic Tutor: without 4 types (e.g. *artifact* Lotus Petal, *instant* Dark Ritual, *sorcery* Wheel, *land* fetch) it finds **zero** because no Demon; trading out a land for it was knowingly aggressive. Brainstorm improves early draw but tutor late is a strong answer to combo lock/hate—decision requires opening-hand T2–T3 dead-draw data.
(B) Vexing Bauble is a real dependency problem but has powerful asymmetrical timing windows because we can sacrifice once prepared. Never pretend Samut stops triggered counter; Hexing Squelcher does as actual uncounterability; do not remove Bauble merely for safe-feeling card draw.
(C) Necrodominance can massively refill late at price of turning off Breach/Delirium and shrinking hand five. It serves a **different combo mode** (go for immediate Oracle/Naus/hand combo next turn). Question how many game states require it vs another permanent color fixer, but do not reject a cEDH reload engine because of that managed tension alone.

## Oracle, legality and rules

1. **Partner tax** tracked separately: first Rograkh {0}, second costs {2}, first Silas {1}UB, second Silas {3}UB; commander presence qualifies if either controlled. Both on board also maintain 2 legendary sources for Amber; Rograkh color red alone, Silas blue/black artifact.
2. **Rograkh ZERO mana but RED identity.** Not a colorless creature just because printed cost {0}. Culling/Plunge/Intent sacrifice as CAST COST before opponent priority, no preemptive removal to fizzle the sacrifice payment.
3. **Silas player-combat damage** ability chooses *target artifact card in GY* on trigger and lets you CAST it this turn following actual card timing/mana. No free cast or permanent permission, no access to land cards or enemy graveyards.
4. **Springleaf Drum** artifact's own tap ability can tap newly summoned Rograkh for mana; **Paradise Mantle** grants ability to equipped creature and thus summoning sickness applies to creature. No phantom haste.
5. **Mox Amber** red only with Rograkh; with Silas U,B,R **one choice**, metalcraft Mox Opal counts ARTIFACTS (Rograkh not artifact, Silas is), Chrome Mox imprint must be paid; LED gives three same-color once and discards whole hand.
6. **Vexing Bauble** counter-trigger when NO MANA spent to cast any spell, including first Rograkh, free pitch spells, zero artifacts and escape LED. The trigger is not prevented by Samut's split second. Pay {1}, tap and SAC Bauble to draw before free-spell turn, or control Hexing Squelcher's "spells you control can't be countered". Paying genuine mana for commander tax or an additional mana cost avoids trigger; note alternative free costs with sacrifice/pitch but zero mana still trigger. [WotC rules](https://magic.wizards.com/en/news/feature/modern-horizons-3-release-notes).
7. **Samut 2026** instants/sorceries YOU CONTROL have split second while stack; nobody can cast spells or activate NONMANA abilities, **including you**; opponents still resolve triggered Bauble and activate mana; it does not make card uncounterable against trigger or already-cast counterspell. [Oracle](https://mtg.wtf/card/fra/302/Samut-Tyrant-of-Naktamun).
8. **Hexing Squelcher** {1}{R}, this spell uncounterable, other own spells uncounterable and own other creatures ward pay2life; prevents actual Bauble counter effect while leaving its trigger stack interactions intact. [Wizards Jan2026](https://media.wizards.com/2026/downloads/ECL_Release_Notes_06HVqa76yI/AIuLLXK62r_EN_MTGECL_ReleaseNotes_20260106.pdf).
9. **Demonic Counsel** {1}{B} no Demon target until delirium 4 DISTINCT GY card types; if active search ANY card without revealing, not a general tutor T1. Fetch land + artifact + instant + sorcery is sufficient, but not if Necrodominance replacement exiled them.
10. **Necrodominance** replacement ALL cards/tokens going to YOUR GY instead EXILE, no draw step, max hand5; it blocks Breach fuel/Delirium from new cards, unlike `Necropotence` whose *discard* GY exile is triggered and can potentially respond to it. Necrodominance 3 black pips tough under 24 land.
11. **Yawgmoth's Will** similar GY exile replacement while turn lasts; existing cards can be played once, new cards can't refill GY, while Breach escape needs three other existing cards. Do not claim perpetual replay.
12. **Tainted Pact** exactly 100 unique names, can exile whole library choosing no card; if no repeated name stop, then Oracle ETB win with empty library provided resolves. Consultation naming a nonexisting-library card can empty library; Oracle in hand/stack not named in library is a valid target name.
13. **Underworld Breach** escape spell mana cost plus exile three other GY cards; LED/Brain Freeze repeated storm/mill loops require PAYABLE fuel, and Bauble must be disabled/prevented first if casting 0 mana LED.
14. **Necropotence** pay life add card to hand on own next end step, no immediately drawn cards or free sorcery casts during resolution; early main burst requires other card access before end step.
15. **Silas with Mox Opal and Grinding Station** counts as artifact for metalcraft and can return Station if combat connects, but opponent can block 2/2 deathtouch if life threat manageable; no automatic recursion before attack step.
16. **Final Fortune/Warrior's Oath** cause lose-game trigger at beginning extra turn's end step; unlike Obeka Brute deck, RogSi has no automatic end-turn safety. Must win/protect by then or lose; Flare/Pact may be countered by own Bauble while attempting shields.
17. **Mana base** 24 lands 100 names 2 commanders, all in UBR, official Commander compliant at Oct15/16; project exception NONE. Any proposed addition requires exact new Oracle/card identity plus independently recount and new owner approval.

## Finite sequencing and adversarial scenarios

Deterministic source-paid samples, NO invented 4-player win-rate model. All alternatives preserve 100 if ever accepted.

| Probe | Exact state / opponent window | Outcome |
|---|---|---|
| R1 | T1 land produces R, zero Rograkh, Mox Amber in hand | Cast Rograkh free, Mox Amber free if Bauble absent, Amber now taps R (not U/B). |
| R2 | T1 Rograkh and Springleaf Drum, Drum untapped, Rograkh summoned now | Drum may tap newly cast Rograkh for ONE chosen color; activation is artifact's, not Rograkh's own ability. |
| R3 | T1 Rograkh plus Paradise Mantle equip1, no haste | Mantle gives Rograkh own tap ability, cannot use until turn next due summoning sickness. |
| R4 | Rograkh + B mana + Culling Weak in hand | Sac Rograkh as additional COST, B spent, receive BBBB; Rograkh next command-zone cast 2 generic (unless dies elsewhere), not free loop. |
| R5 | Rograkh + R mana + Infernal Plunge | Sac creature as casting cost, receive RRR; first recast Rograkh 2 after zone decision. |
| R6 | Rograkh only and Mox Amber with zero artifact other than Amber, Mox Opal | Amber taps R; Opal has only two artifacts? Amber + Opal =2; metalcraft OFF. |
| R7 | Rogue alone, Vexing Bauble already present, cast Rograkh first time no mana | Bauble triggered, counter Rograkh if Squelcher absent; having printed {0} does not exempt. |
| R8 | Bauble and LED/Chrome/Mox Opal/Petal on win turn, no mana paid | Each artifact spell with no mana spent gets Bauble trigger; sacrifice Bauble {1},tap first or have Squelcher. |
| R9 | Bauble + Samut and cast 0-MV instant? (e.g. Pact free) | Bauble counter-trigger STILL triggers despite split second; Samut doesn't override it. |
| R10 | Bauble + Hexing Squelcher and zero Lotus Petal | Bauble triggers, cannot counter our Petal due Squelcher's uncounterable static; opponent may remove Squelcher earlier. |
| R11 | Rograkh commander previously cast once, Bauble present, paying 2 command tax | Rograkh cast has mana spent, Bauble no trigger; actual mana paid prevents self-hate. |
| R12 | Silas attacks hits opponent, own GY has LED | Silas trigger targets LED; at your main phase after damage (if GY unchanged) may cast LED for 0, Bauble may counter if still up, no exemption from mana. |
| R13 | Demonic Counsel on turn2; GY artifact Lotus Petal and land fetch only | TWO types (<4), can only find Demon; none in deck -> no card to hand. |
| R14 | Counsel later with GY land, artifact, instant, sorcery | FOUR types, {1}B Demonic Counsel gets ANY card; fails if Necrodominance exiled prospective GY cards. |
| R15 | 24 land / 16 fast mana no U source, Oracle + Pact available | UU is still mandatory to CAST Oracle, not just more CC; generic artifacts don't substitute. |
| R16 | LED/Breach/Feeze GY fuel 3 other cards, Bauble present | Zero-cost LED escaped would be countered; escaping consumes cards as costs even if countered, catastrophic if unprepared. |
| R17 | Breach on board, 3 other GY cards and Brain Freeze in GY, no LED | Can pay 1U + exile3 for ONE Brain Freeze, not a repeatable free loop from empty GY. |
| R18 | Grinding Station + zero artifact + Breach + GY feed | Station sacrifices artifact and mills three, then exiled3 to escape zero artifact; entering artifact untaps Station; upkeep/payoff requires additional mana/targets as applicable. |
| R19 | Necrodominance and Breach simultaneously, self-mill three via Station | Would-be GY cards EXILED instead, Breach cannot use newly milled cards; must remove Dominance or win different line. |
| R20 | Necropotence in play, discard card via Wheel | Card enters graveyard then Necro discard exile triggered ability will exile later; unlike Necrodominance global replacement, there may be stack response window. |
| R21 | Samut on field and cast Brain Freeze with split second | Triggered storm copies still stack, opponents can't cast counterspells while Brain Freeze on stack, but can respond after it leaves and before next unresolved objects; cannot cast own protection either while still on stack. |
| R22 | Final Fortune RR, extra turn, commander only Rograkh and tapped out | You lose at beginning extra turn end step unless win first; RogSi has no end-turn commander ability, unlike other Obeka deck. |
| R23 | Force of Negation alternative pitch during YOUR main win turn | Cannot use free alternate cost unless opponent turn; needs 1UU now; Vexing Bauble would counter no-mana cast anyway. |
| R24 | Original Rograkh free, Silas hand zone first time, sources U/B/C | Silas costs 1UB => cast, but no built-in haste; artifact recursion must wait for successful player combat. |
| R25 | Opponent only one tapped land, M5 Hullbreaker in hand and Into Flood Maw proposed cut | Can't cast seven-mana payoff in hand, one-mana bounce can clear hatebear; model large creature score fails tempo. |
| R26 | Grim Monolith taps CCC, no Power Artifact | Untap {4}, cannot endlessly net mana; adding Power Artifact still only produces COLORLESS unbounded, requires payoff. |
| R27 | Opponent casts zero mana Force into your open Vexing Bauble | Counter trigger stops no-mana Force, protects own combo *unless* your own Rograkh/LED free spells also await casting; sequencing choice. |
| R28 | Opponent fast combo, own T1 Demonic Counsel vs proposed Brainstorm | Before four GY types Counsel blank, Brainstorm sees three and replaces itself after reshuffle with fetch; late-game delirium Counsel tutors ANY required singleton where Brainstorm only finds in top3. |
| R29 | Early hand 1 land, Gemstone Caverns in hand on the PLAY, no luck counter | Caverns normally only C, not free any-color; conditional pregame exile on draw required; 24-land turbo opening fragile. |
| R30 | Necrodominance with 5 cards max hand, attempt Wheel to feed graveyard | Wheel discards hand into EXILE, no graveyard feed; draws seven then must discard to max 5 in cleanup, again exile. |
| R31 | Rograkh free commander + Culling/Intent after already sacrificed and recast twice | Next recast costs {4}, cannot treat sacrificed commander as reusable unlimited free mana; each other spell requires colored/pitch resources. |

**Strongest counterargument to Brainstorm challenger:** early unconditional blue cantrip + fetch is better than pre-delirium totally blank Counsel. However turbo RogSi can create delirium by late T2 through land fetch + artifact Petal + instant Dark Ritual + sorcery Infernal Plunge, giving **unconditional any-card tutor** for {1}B. Brainstorm often is card selection not arbitrary tutor; the difference matters in a deterministic cEDH race and additional card on top can be locked without fetch. The choice requires tracked opening-hand/dead-draw rates and opponent turn pressure, not a raw popular-cantrip ranking. Conditional proposal only, no swap.

## Conclusions and unresolved evidence

**Final authored disposition: KEEP exact approved 100 unchanged (Bracket 5 cEDH)**, with conditional candidate `Brainstorm IN / Demonic Counsel OUT` if timing audits show 4-type delirium too slow and weak early Counsel draws costing opportunities; off-ranking `Fellwar Stone IN / Demonic Counsel OUT` in mana denial/grind pods. Candidate `Enigma Jewel -> Birgi` categorically mismatched resource costs; `Hullbreaker -> Into the Flood Maw` raises lethal speed curve/AdNaus penalty. Structural Vexing Bauble risk is real but manageable; do not hide it or count Bauble as a costless unilateral shield. Necrodominance active with Breach/Delirium is a serious mutually exclusive mode to document, not proof of mandatory removal.

**Coverage and boundaries**: all 100 approved names audited incl partner identities, 24 lands, 98 library cards, no repeat, 51 M5 routes by family + offranking, 31 finite payable adversarial probes, current Oct20 official WotC and Oracle evidence, Oct15/16 full-list UBR legality snapshot, zero project exceptions. No actual empirical stochastic 4-player tournament win-rate test or new 100-card Oracle refetch; no current user approval for changes; source approved hash and 62 canonical locks intact, 62/62 narrow M6.4 separate, independent GrokBot Pass C and Phase B remain unaccepted. Exact-head CI for THIS evidence and tracker checkpoint separately required before marking complete. 
