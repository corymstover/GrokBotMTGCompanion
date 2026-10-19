# M6 #35 — Marchesa, the Black Rose: single-deck commander-first review

**Source binding:** canonical `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json#decks.Marchesa__the_Black_Rose`, `APPROVED / LOCKED` since October 15, 2026, SHA-256 `627b07f6466c0a48f16daea58ee9c01bba02c2b7fb4de76a37b14a7f75ad7f9b`. Approved export `refinement/decklists/Marchesa_the_Black_Rose_Approved_2026-10-15.txt` Git blob `e21039369a86dc2160dcf92155a5fbe0fa847bef`. Engineering registry logical `lh1:ff7464ce79627be5de1b49504c69dc40a9e01dd24e33f9e3abffeffb5784166f`; no source discrepancy. Review author ChatGPT October19 2026. **No canonical edits.**

## Source and test receipts

Read live tracker index34 (first PENDING, 34/62 completed), `AGENTS.md`, M6 single-deck standard, registry, milestone subtracker, `grixis/blueprints/marchesa-the-black-rose.md`, `grixis/interactions/marchesa-the-black-rose.md` (11 verified interaction entries; CR Sep25, Oracle Oct16, rulings Oct15), `data/grixis/m6/review_packets/marchesa-the-black-rose.json` (129 source M5 candidate comparisons), `data/grixis/mana_base/marchesa-the-black-rose.json`, `data/grixis/birthday_m5/evidence/marchesa-the-black-rose.json` (260 EDHREC inclusion vectors), canonical Oct15 decision/approval-ready source and actual approved list. The canonical Oct15 official Commander legality gate and engineering Oct16 Scryfall Oracle bulk mark **COMPLIANT**, no project exceptions; these are **dated checkpoints**, not a newly run Oct19 complete Scryfall/banlist check. Project 62 narrow M6.4 authored reviews ≠ these comprehensive reviews; independent Pass C remains incomplete.

**Independent current source TXT parse:** 98 named rows, quantities sum to exactly **100** including one commander; **98 distinct names**, duplicate `Island ×2` and `Swamp ×2` ONLY (both legal basic land repeats), **34 lands**, **66 nonlands** including commander, no companion, color identity U/B/R by approved dated Oracle gate. Bracket **4 — Optimized**, not forced cEDH. The Oct15 approval-ready verification's historical “not yet approved” status is superseded by the later explicit Oct15 locked approval record and live overrides.

## Commander identity and natural ceiling

**Marchesa, the Black Rose** costs {1}{U}{B}{R}, is a Human Wizard with **dethrone**, grants other creatures you control dethrone, and returns any creature you control that DIED with a +1/+1 counter to battlefield under your control **at the beginning of the next end step**. Counter must be present as it dies; merely gaining one after dying is impossible. Marchesa must be on battlefield as that death occurs for the death trigger to exist; the delayed return then survives Marchesa leaving. A Marchesa with her own counter also triggers on her death. Dethrone triggers on attacking the player with most/tied life, not their planeswalker; counters occur before blocks. Marchesa's primary gameplay is **protecting sacrifice/ETB creature resources**, not a generic Grixis spellslinger win. Sacrifice engines (Ashnod's/Phyrexian Altars, Bombardment, Dementia, Seer, Feeder, Yahenni, Tower, Yawgmoth), counter sources (Unspeakable Symbol, Forge, Gev, Mimic, Thran Vigil, Uncivil Unrest, Cauldron, Danny, dethrone), persist/undying bodies (Redcap, Glen, Clique, Kelpie, Flayer, Mikaeus) and death/ETB payoffs (Blood Artist, Zulaport, Syr Konrad, Gary, Flayer, Mayhem Devil, River Kelpie, Satoru, Twilight) form a coherent recursion economy.

**Natural ceiling Bracket4:** Compact persist/undying infinites and premium tutors/interaction are real, but the battlefield, commander-return end-step and counter-placement dependence are genuine weaknesses. Source blueprint honestly notes **48 Commander Spellbook enumerated infinite lines do not require Marchesa**; they are usually persist reset+free outlet combos. They are **not** 48 independent strategic win plans, and shouldn't be used to inflate to cEDH or imply commander required for the kill. Marchesa improves resilience, repetition and value while backup loops finish. The exact 21 Oct15 source changes are ALREADY incorporated in this approved deck; do not re-propose Sneak Attack, Sage, Gev, Spark Double, Danny, Cauldron, Satoru or Altar as new additions.

## Full 100-card role audit

Every **98 distinct approved name** explicitly inspected in approved list order; basic Island/Swamp quantities recorded. 100 physical cards reconciled, no omitted slots.

| # | Quantity and card | Principal role | Commander-specific contribution and failure mode |
|---:|---|---|---|
| 1 | 1x Marchesa, the Black Rose | Commander, dethrone + end-step recurrence | Four mana UBR, other creatures get dethrone; creature with +1/+1 counter dying while Marchesa present gets delayed end-step return. Commander is resilience engine, not required for most persist infinites. |
| 2 | 1x Agatha's Soul Cauldron | Counter placement, GY hate, activated-ability sharing | One countered creature can acquire activated abilities of exiled creature cards; needs target card in graveyard; cannot share altar's noncreature ability. |
| 3 | 1x Altar of Dementia | Free sacrifice outlet, mill win | Sacrifice creature to mill target player equal to power, can self-mill for recursion or mill opponents in repeatable persist loop. |
| 4 | 1x An Offer You Can't Refuse | One-mana noncreature counter | Answers opposing noncreature spell, gives controller two Treasures; protection cost for proactive combo. |
| 5 | 1x Ancient Tomb | Fast generic land | Two colorless at 2 life, helps 4-mana Marchesa and altars but not UBR pips. |
| 6 | 1x Arcane Signet | Color fixing rock | Two mana investment, any UBR on tap; supports commander and later multiple activation costs. |
| 7 | 1x Ashnod's Altar | Free sacrifice, 2 colorless per body | Loop outlet and mana generator; sac is cost, creature returns later by Marchesa unless immediate persist/undying. |
| 8 | 1x Badlands | Untapped fetchable BR | Typed original dual supporting black-heavy creature suite and R for Sneak Attack/Bombardment. |
| 9 | 1x Baleful Strix | Cheap artifact creature ETB draw | Sac/return with +1 counter makes repeatable card advantage and flying deathtouch blocker; without counter doesn't return. |
| 10 | 1x Blasphemous Act | Board wipe and sacrifice-enabler | Costs less with creature density, kills countered Marchesa board to return later; opponents can exile in response. |
| 11 | 1x Blood Artist | Death-trigger drain payoff | Whenever any creature dies targets one player to lose1, gain1; kills with repeatable deaths, vulnerable to removal. |
| 12 | 1x Blood Crypt | BR fetchable shock | Untapped for 2 life or tapped, relevant early black+red source. |
| 13 | 1x Bloodstained Mire | Fetchland fixing | Gets typed Swamp/Mountain duals, 1 life, feeds graveyard. |
| 14 | 1x Braids, Arisen Nightmare | End-step sac-to-draw pressure | Sacrifice artifact/creature/enchantment/land; each opponent sacrifices same type or loses2 and you draw; commander recurrence offsets creature sacrifice only if countered. |
| 15 | 1x Carrion Feeder | Free creature sac outlet | One-mana Zombie can sac any creature to grow +1 counters; cannot block, protected loop outlet. |
| 16 | 1x Chaos Warp | Broad permanent answer | 2R shuffles target permanent into owner's library, opponent may get permanent; essential enchantment/stax answer. |
| 17 | 1x City of Brass | Any-color land | Untapped rainbow but repeated taps cost damage, life resource with Unspeakable Symbol. |
| 18 | 1x Command Tower | Any-color land | No life loss, casts UBR commander and varied pips. |
| 19 | 1x Cyclonic Rift | Flexible bounce / emergency reset | 1U single opposing nonland permanent; overload 6U clears opponents, does not itself sacrifice or counter creatures. |
| 20 | 1x Danny Pink | Counter placement draw engine | Mentor counter placement and each creature draws first time counters put on it each turn; interacts with dethrone and persist reentry. |
| 21 | 1x Deadly Dispute | Instant sac, cards and Treasure | 1B sac artifact/creature as additional cost, draw2 and tapped? Treasure enters untapped; one-shot sacrifice can trigger Marchesa if +1 counter. |
| 22 | 1x Demonic Tutor | Universal 2-mana tutor | Finds combo enabler/outlet/protection; generic but supports identity. |
| 23 | 1x Diabolic Intent | Sac-to-tutor | 1B additional creature sacrifice; with Marchesa countered creature returns at next end step, find missing loop part. |
| 24 | 1x Exotic Orchard | Conditional rainbow land | Only colors opponents' lands could produce; cannot guarantee all three. |
| 25 | 1x Feed the Swarm | Black enchantment/creature removal | Sorcery, destroy target creature or enchantment opponent controls, lose life equal MV; covers Rule of Law effects. |
| 26 | 1x Fellwar Stone | Conditional 2-mana rock | Adds opponent land colors, may lack needed UBR in narrow tables. |
| 27 | 1x Fierce Guardianship | Free noncreature stack protection | Free only with commander controlled; counter target noncreature spell, protect engine from board hate. |
| 28 | 1x Flare of Denial | Free alternate counter via blue creature sac | Sacrifice nontoken blue creature as alternate cost, counters spell; countered blue creature may return via Marchesa if it had +1 counter. |
| 29 | 1x Flayer of the Hatebound | Undying damage payoff | When creature enters from own graveyard, that creature damages any target equal to power; with Sage + Ashnod mana neutral repeat. |
| 30 | 1x Fleshbag Marauder | ETB each-player creature sacrifice | Recurs with Marchesa if countered, bypasses hexproof/indestructible, own sacrifice can include Fleshbag itself. |
| 31 | 1x Flooded Strand | Fetchland U access | Finds Island-typed duals and Xander's Lounge? Lounge is Island Swamp Mountain so yes, feeds fixing. |
| 32 | 1x Forge of Heroes | Commander counter utility land | {T} colorless or target commander that entered this turn for +1/+1; does not produce colored mana. |
| 33 | 1x Gev, Scaled Scorch | Conditional counter-on-ETB reset | After opponent lost life this turn, other creatures enter with +1 counter; supports Redcap persist and death loops. |
| 34 | 1x Glen Elendra Archmage | Persist blue counter engine | 1U sacrifice self to counter noncreature spell; +1 reset (Sage/Mimic etc) can repeat if mana available. |
| 35 | 1x Goblin Bombardment | Free sacrifice outlet and damage | Sac creature deal1 any target, direct payoff; doesn't require tapping, lethal from persist loops. |
| 36 | 1x Grave Pact | Sac/death board control | Whenever own creature dies each opponent sacrifices creature; powerful but BBB in 34 land B-heavy list. |
| 37 | 1x Gray Merchant of Asphodel | ETB black devotion drain | Drains each opponent and gains life; recurring ETB via Marchesa or Mikaeus/Yawgmoth loop. |
| 38 | 1x Grim Haruspex | Death-trigger card draw | Nontoken own creatures dying draw, can deck self in infinite loop unless control trigger source. |
| 39 | 1x High Market | Land + life sacrifice | {T} C or {T},sac creature gain1 life, protects countered body and returns end step; colorless hurts UBR. |
| 40 | 1x Imperial Recruiter | Creature tutor | 2R search power≤2 creature to hand; fetches several outlets/reset creatures, not all big finishers. |
| 41 | 1x Iron Apprentice | One-mana modular counter donor | Dies and moves +1 counters to artifact creature or creature? modular targets artifact creature; verify before assuming unrestricted; cheap counter resource. |
| 42 | 2x Island | Basic U land | Two copies legally repeated, support UU Flare/Glen/interaction, low basic count. |
| 43 | 1x Lightning Greaves | Haste/shroud protection | Equip0; shroud prevents own targeting Unspeakable Symbol/Forge while equipped; no counter by itself. |
| 44 | 1x Luxury Suite | Multiplayer BR | Untapped with 2+ opponents, conditional tapped in 1v1. |
| 45 | 1x Mana Confluence | Rainbow land with life | Pay1 life per tap, colored reliability, life pressure. |
| 46 | 1x Marionette Apprentice | ETB fabricate and artifact/creature loss drain | Artifact/creature death drain opponents depending Oracle; synergizes with Altar and token lines, creature counters optional. |
| 47 | 1x Mayhem Devil | Sacrifice ping payoff | Any player sacrifices permanent, deal1 any target; own altars/fetches trigger, not limited to creatures. |
| 48 | 1x Metallic Mimic | Type-specific counter-on-entry | Choose creature type on entry, other matching creatures enter with +1 counter, resets persist if appropriate type. |
| 49 | 1x Mikaeus, the Unhallowed | Non-Human undying combo engine | BBB high-cost, gives other non-Humans undying, works with persist and Yawgmoth; humans excluded. |
| 50 | 1x Misty Rainforest | Fetchland U | Gets Island-typed duals or Xander Lounge, life cost. |
| 51 | 1x Morphic Pool | Multiplayer UB | Untapped with 2+ opponents, UB helps Glen and black pips. |
| 52 | 1x Mountain | Basic R land | Single copy, red for Bombardment/Sneak Attack, not black for triple black cards. |
| 53 | 1x Murderous Redcap | Persist damage win creature | ETB damage equal power any target; persist reset + self-targeting or outlet produces lethal loops. |
| 54 | 1x Otawara, Soaring City | U legendary land / channel bounce | Channel can return artifact, creature, enchantment or planeswalker; not an on-board sac or counter source. |
| 55 | 1x Phyrexian Altar | Free sacrifice, any-color mana | Core sac outlet converts bodies into colored mana; recur via persist for infinite colored resources. |
| 56 | 1x Phyrexian Tower | Land sac for BB | Legendary sac creature for BB vs colorless baseline, sacrifice outlet with land activation constraints. |
| 57 | 1x Pitiless Plunderer | Death treasure engine | Nontoken own creature death creates Treasure, can fuel repeated costs, not a free sac outlet. |
| 58 | 1x Polluted Delta | Fetchland UB | Finds Swamp/Island duals, helps BB/UU and graveyard. |
| 59 | 1x Puppeteer Clique | Persist opponent GY ETB theft | Reanimate opponent creature until EOT, can sacrifice it; +1 reset gives repeated reanimation; graveyard target conditional. |
| 60 | 1x Reanimate | One-mana creature recursion | Gets any creature from GY, lose life equal MV, may reanimate own discarded/removed pieces; not commander delayed return. |
| 61 | 1x River Kelpie | Persist graveyard ETB draw | Draws when permanent enters from graveyard, recurring engine, can draw too many cards in infinite loops. |
| 62 | 1x Sage of Fables | Wizard counter reset, pay2 draw | Wizards enter with +1 counter; 2 remove counter draw, supports Glen/Kelpie/ Clique depending types and Flayer loop. |
| 63 | 1x Satoru, the Infiltrator | Free-enter creature draw | Nontoken creatures entering without being cast draw; Marchesa/persist/undying turns generate value. |
| 64 | 1x Scalding Tarn | Fetchland UR | Finds Island/Mountain typed duals, mana fixing, graveyard fuel. |
| 65 | 1x Scorn-Blade Berserker | Sac-to-draw with counter support | Backup gives +1/+1 and sacrifice another creature for draw, self-contained enabler but limited activation. |
| 66 | 1x Shivan Reef | Painland UR | Colorless no life, U/R costs life; black-heavy spells need separate source. |
| 67 | 1x Skullclamp | Sacrifice/card draw equipment | Equip1 -1 toughness and death draw2, may kill 1-toughness before counter; repeatable with returning creatures. |
| 68 | 1x Sneak Attack | Haste/ETB cheating | R activate put creature from hand onto field with haste; end-step sacrifice trigger, Marchesa return next end step if +1 counter before death. |
| 69 | 1x Sol Ring | Fast colorless mana | One mana→two generic, accelerates altars/commander generic but cannot pay UBR alone. |
| 70 | 1x Spark Double | Copy with +1 counter | Copies own creature (not legendary copy) enters with counter, persist copied body can loop with free sac and reset. |
| 71 | 1x Steam Vents | Fetchable UR shock | Pay2 untapped or ETB tapped, needed for double blue and red. |
| 72 | 1x Sulfurous Springs | BR painland | Untapped colored source at 1 damage each colored tap, key BBB requirement. |
| 73 | 2x Swamp | Basic B land | Two copies legally repeated, black-heavy devotion and Yawgmoth/Mikaeus. |
| 74 | 1x Syr Konrad, the Grim | Graveyard movement damage | Triggers on creature dies or creature leaves graveyard, pings each opponent; high mana but direct finisher. |
| 75 | 1x Takenuma, Abandoned Mire | B legendary land / channel recursion | Channel mills three and returns creature or planeswalker from GY to hand, land slot utility. |
| 76 | 1x Talisman of Creativity | UR rock | 2 cost, colorless or U/R at 1 damage, supports protection and red. |
| 77 | 1x Talisman of Dominance | UB rock | 2 cost, colorless or U/B life, supports BB and UU. |
| 78 | 1x Talisman of Indulgence | BR rock | 2 cost, colorless or B/R life, supports black-heavy and red. |
| 79 | 1x The Ozolith | Counter preservation | When countered creature leaves battlefield, counters stored then move to combat creature; counters not retained on returning body by default. |
| 80 | 1x Thran Vigil | Graveyard-exit counter placement | When cards leave your graveyard during YOUR turn put +1 counter on target creature; crucial for persist resetting, only own turn. |
| 81 | 1x Toxic Deluge | Life-paid board wipe | 2B all creatures -X/-X until EOT; may kill own countered board, returns at next end step if Marchesa present. |
| 82 | 1x Training Center | Multiplayer UR | Untapped with 2+ opponents, tapped 1v1. |
| 83 | 1x Twilight Diviner | Once/turn token copy on GY return | Creates token copy of creature that enters from graveyard; copied token lacks original counters, fragile without support. |
| 84 | 1x Uncivil Unrest | Riot and damage doubling | Creatures you control have riot and modified creatures deal double damage; +1 counter mode supports Marchesa and persist reset. |
| 85 | 1x Underground River | UB painland | Untapped U/B at 1 damage, key color source. |
| 86 | 1x Underground Sea | Fetchable UB dual | Best U/B typed untapped land for triple black / blue counters. |
| 87 | 1x Unspeakable Symbol | Instant-speed +1 counter for life | Pay3 life put +1 counter on creature; can rescue own board from removal if enough life, not free. |
| 88 | 1x Vampiric Tutor | One-mana topdeck tutor | Any card top at 2 life, instant speed, not sac/ETB synergy directly. |
| 89 | 1x Verdant Catacombs | Fetchland B | Fetch Swamp-typed duals or Xander Lounge, life cost. |
| 90 | 1x Victimize | Two creature reanimation | 2B sac creature and target two GY creatures to battlefield tapped, strong if countered sac creature Marchesa later. |
| 91 | 1x Viscera Seer | Free sacrifice and scry | One mana sac any creature, scry1, setup Marchesa loops and filter. |
| 92 | 1x Volcanic Island | Fetchable UR dual | No life tax, U/R access. |
| 93 | 1x Warren Soultrader | Sac outlet, treasure at life cost | Pay1 life sac another creature, make Treasure, can fund repeated persist loops at life cost; careful not assume free infinite. |
| 94 | 1x Watery Grave | Fetchable UB shock | Pay2 untapped, important blue/black. |
| 95 | 1x Xander's Lounge | Tapped fetchable tri-land | UBR typed Island Swamp Mountain enters tapped, cycle later; one slower slot for stable 3-color. |
| 96 | 1x Yahenni, Undying Partisan | Free creature sac outlet | Sac another creature to give indestructible until EOT, grows on opposing deaths; free repeatable outlet. |
| 97 | 1x Yawgmoth, Thran Physician | Sac-to-draw and -1 counter | Pay1 life sac another creature put -1/-1 counter on up to one target creature and draw; proliferate discard at BB, enables Mikaeus loops. |
| 98 | 1x Zulaport Cutthroat | Creature death drain | Own creatures die each opponent loses1 and gain1, no target; primary table-wide aristocrats kill. |

## Mana, development, draw, interaction and vulnerabilities

**Mana inventory:** 34 lands, 6 fetchlands, 6 repeatable nonland mana sources (Sol Ring, Arcane Signet, Fellwar Stone, three Talismans), no ritual or one-shot mana inventory; 4 utility lands, 1 unconditional ETB tapped land (Xander's Lounge), six conditionally tapped land flags. Source colored land access potential **B20 / U20 / R16**, unconditional **B19 / U19 / R15**; including repeatable nonland **B24 / U24 / R20** (not simultaneous usable resources). Spell pip demand **B44 (65.67%) / U13 (19.4%) / R10 (14.93%)** and 8 double-black spells vs 2 double-blue spells; BBB Grave Pact and Mikaeus are hard colored commitments. Turn3 10-card no-mulligan proxy: **74.1852%** “all UBR potential land source presence” and **73.6993%** strict 3 land drops; neither means Marchesa T3 is castable (requires four total mana, one of each color, with tapped-land/rocks constraints). Turn4 strict 4 land drops **56.2728%** without ramp. Life payments on Unspeakable Symbol, City, Confluence, painlands, Yawgmoth and Deluge compete with combat life totals and ability to dethrone. `Forge of Heroes` and `High Market` are colorless until utility; `Phyrexian Tower` produces BB by sacrificing creature but may cost a board resource.

**Game plan:** T1 black sac outlet or cheap counter enabler, T2 rock/Strix/engine, T3 draw/counter source, T4 Marchesa with held-up protection or immediate Forge/Unspeakable Symbol counter, then sacrifice countered ETB creatures to reuse at next end step and assemble a repeatable persist reset + outlet + drain/Redcap payoff. Against opponents with higher life, dethrone supplies counters before combat damage; against opponents who lower life intentionally, no reliable dethrone trigger, so independent counter sources are essential. Attack is NOT required to combo, but timing around end step matters.

**Protection / interaction:** An Offer, Fierce Guardianship, Flare of Denial, Chaos Warp, Cyclonic Rift, Feed the Swarm, Otawara, Blasphemous Act, Toxic Deluge, Fleshbag, Glen Elendra Archmage; Grave Pact is repeatable sacrifice control. The deck has only a small permission suite vs turbo Grixis, and several answers are sorcery speed; unlike Marchesa, Dealer of Death, this commander is NOT optimized as cEDH counterspell turbo. `Lightning Greaves` shroud can block our own targeted Unspeakable Symbol/Forge if equipped; equip0 move it before placing counters if timing permits. No graveyard-return protection against Rest in Peace/Leyline/targeted exile; persist, Marchesa and reanimation all need card to visit/return from GY, whereas `Agatha's Soul Cauldron` exiles creatures for ability sharing (can conflict with later reanimation). `Skullclamp`, Satoru, Kelpie, Danny, Haruspex, Braids and tutors cover access, but each has board/setup constraints and excessive draw in a mandatory infinite loop can lose to empty library.

**Opportunity-cost pressure:** 5+ mana engines Flayer, Syr Konrad, Gary, Mikaeus, Uncivil Unrest, River Kelpie and 4-mana Grave Pact can clog a 34-land draw. `Twilight Diviner` once each turn is only good if graveyard returns already happen; `Braids` asks for a disposable permanent at own end step; `Grim Haruspex` risks mandatory overdraw on loop; `Sneak Attack` is high-output but needs creature IN HAND and a counter before end-step sacrifice; `The Ozolith` conserves counters but doesn't independently put a counter on a freshly returned creature until beginning of combat. `Iron Apprentice` modular only moves to artifact creature, so its use as a universal counter donor requires other wording (the card's “when dies” counter-moving ability if present) and should not be assumed without Oracle. `Uncivil Unrest` five mana may be slow but is a mass entry-counter reset and modified-damage closer, not generic anthem. `Gray Merchant` has an actual Mikaeus/Yawgmoth engine role and should not be dismissed as an overcosted aristocrat alone.

