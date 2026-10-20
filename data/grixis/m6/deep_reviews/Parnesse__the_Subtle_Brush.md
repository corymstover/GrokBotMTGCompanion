# M6 Comprehensive Single-Deck Authored Review #46 — Parnesse, the Subtle Brush

**ID:** `Parnesse__the_Subtle_Brush`, tracker index45, deck #46/62. **Author:** ChatGPT (NOT GrokBot independent Pass C), **2026-10-20**. **Disposition:** KEEP all 100 canonical cards unchanged; narrowly scoped challengers documented as owner-facing proposals ONLY.

## Source and test receipts

Read live `AGENTS.md`, `grixis/M6 Commander-First Single-Deck Review Standard.md`, `data/grixis/m6/single_deck_depth_tracker.json` (45/62 complete prior to review), `data/grixis/registry.json`, `data/grixis/milestone_m6_m7_subtracker.json`, 2026-Oct16 Oracle/CR [Parnesse interaction review](https://github.com/corymstover/GrokBotMTGCompanion/blob/chatgpt-cycle76-m6-refinement/grixis/interactions/parnesse-the-subtle-brush.md), `data/grixis/m6/review_packets/parnesse-the-subtle-brush.json` **126 M5 hypothesis routes** and mana source model. Canonical `corymstover/grixis-commander-encyclopediaGPT/main`, `state/current_deck_overrides.json#decks.Parnesse__the_Subtle_Brush`, Oct15 approval, whole-list audit, decision closeout, targeted verification and complete gate. Approved TXT [here](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/decklists/Parnesse_the_Subtle_Brush_Approved_2026-10-15.txt) (blob `c99244e17b3a36c654b54b2abddc2e82047d7d04`).

**Approved LOCKED SHA** `8ff8c101d98e7de997c1de29973db2dd6a51ffdd7b44e4f34145bb1abf2d9e7c`, 2026-10-15; engineering logical `lh1:bb86ddd74054d4f5dbec9ed997501ca1731a398a728fda18d0d430f94d0a9839`. No commander ID discrepancy, no special project exception. Canonical Oct15 legality verified, engineering Oct16 bulk Scryfall official Commander compliant. **Independently recount actual TXT:** 100 physical, 96 distinct names, 35 lands, singleton PASS with only lawful repeats Island x2, Mountain x3, Swamp x2; commander one. Approved historical change count ten (9 mana lands + Arcane Bombardment→Tempt with Mayhem) is already built into these approved exact bytes.

**Source test limitations:** generated M5 packet has 126 proposed add/cut routes in seven batches (P1 performance-only 4, P3 fit-only 122); reported 4 passes, 8 failures, 71 inconclusive, 34 no-difference, with remaining per-route classification limitations. The Oracle/CR review of ten special interactions reports **eight verified, one uncertain, one flagged** (Bonus Round symmetry). Do not incorrectly call all ten exact scenarios universally solved. This authored review independently checks the principal uncertainty and risk; no executed fully effect-aware new tournament/meta simulation or all-100 Oct20 Scryfall refetch claimed.

**External rules:** [Parnesse Oracle](https://www.mtg.wtf/card/ncc/106/Parnesse-the-Subtle-Brush), [Tempt with Mayhem official release notes](https://magic.wizards.com/en/news/feature/modern-horizons-3-release-notes), [Sunken Palace official release notes](https://media.wizards.com/2024/downloads/MH3_Release_Notes_9d01wihakukg/EN_MTGMH3_ReleaseNotes_20240515.pdf), [2026-09-25 CR](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt), original Oct15 attestation gate.

## Commander identity and natural ceiling

Parnesse {2}{U}{B}{R} 4/4 legendary Vampire Wizard has two distinct triggered abilities: (1) whenever an opponent-controlled spell/ability TARGETS you or a permanent you control, counter that spell/ability unless that opponent **pays 4 life**. This protects your BOARD and controller, not generic every player and not untargeted sweepers; taxed spell copies count as opponent-controlled spells if opponent controls them. (2) whenever **YOU COPY A SPELL**, up to one TARGET opponent may ALSO copy that spell, choosing new targets for their copy. This second effect is **optional to you** (choose zero targets); an opponent-copy created under the opponent's control does NOT itself generate another Parnesse trigger for you. Commander politics matter by deciding when giving another player resources advances your own objective and avoids retaliation.

Crucial Oracle distinction: COPYING an **instant/sorcery SPELL already on stack** triggers Parnesse; **copying a card in another zone then casting that copy** (Mizzix's Mastery, Arcane Bombardment) does NOT trigger Parnesse merely from that effect, although CAST and magecraft triggers may still happen separately. You can create Parnesse instances via Reverberate/Reiterate/Narset's Reversal, Tempt with Mayhem, Alania, Thunderclap, Twinning Staff, Primal Wellspring, Goggles, Ral, Prismari storm, Double Vision, replication/demonstrate; create enough copies to trigger Ral or Professor Onyx lethal. Parnesse's grant can let opponents copy useful nonlethal spells, but giving an opponent a copied counterspell can be dangerous.

**Ceiling Bracket 4 — Optimized**, not asserted cEDH: five-mana commander with ongoing responsive protection and copy/political storm, tutor/card access but mana-heavy copy engines. Win lines include true Reiterate buyback mana positive with Mana Geyser/Jeska's Will under actual resources; other spell copier interaction/storm with Ral/Professor Onyx; possible Dualcaster spell-copy value; not generic Consult/Breach default. Multiple shared staples are valid if they feed cast/copy plan without replacing signature politics. Critical vulnerabilities are sudden board wipe not targeted, too few copied spells before high-end engines, and opponent responses benefiting from Bonus Round.

## Full 100-card role audit

Exact owner-approved TXT in original source order; one distinct card name per ledger row and quantity shown.

| TXT | Qty | Exact source name | Distinct role, real commander synergy and limitation |
|---:|---:|---|---|
| 1 | 1 | Parnesse, the Subtle Brush | COMMANDER — {2}{U}{B}{R} 4/4 Vampire Wizard; any opponent target against you/permanent taxed 4 life; when YOU copy spell may allow one opponent copy |
| 2 | 1 | Alania, Divergent Storm | First relevant instant/sorcery can be copied if giving an opponent a card; triggers Parnesse when YOU make copy, political opponent-benefit cost. |
| 3 | 1 | An Offer You Can't Refuse | U counter noncreature spell at cost of giving two Treasures to its controller; protection for combo turn with tempo downside. |
| 4 | 1 | Arcane Signet | 2-mana stable UBR fixing, Parnesse needs {2}UBR and later UU/RR. |
| 5 | 1 | Archmage Emeritus | Magecraft cards drawn for instant/sorcery casts or spell copies, enables engine but 4-mana vulnerable body. |
| 6 | 1 | Arid Mesa | Land — Fetchland for appropriate land subtype among shocks/original duals/triome, 1 life. |
| 7 | 1 | Badlands | Land — Fetchable typed dual/shock that pays UBR pair; shock untapped needs 2 life. |
| 8 | 1 | Big Score | 3R instant additional discard then draw2+two Treasures, pays setup in storm chains; copying spells does not pay original extra discard again. |
| 9 | 1 | Blasphemous Act | 1R often cheap board wipe in multiplayer, can kill own Parnesse/payoff creatures; stops creature assault. |
| 10 | 1 | Blood Crypt | Land — Fetchable typed dual/shock that pays UBR pair; shock untapped needs 2 life. |
| 11 | 1 | Bloodstained Mire | Land — Fetchland for appropriate land subtype among shocks/original duals/triome, 1 life. |
| 12 | 1 | Bonus Round | 1RR copies EVERY player's instant/sorcery casts that turn, including opponent response counterspells; symmetric major exposure. |
| 13 | 1 | Brainstorm | U top-three card selection with fetch shuffle, cheap spell velocity for storm and tutors. |
| 14 | 1 | Chaos Warp | 2R instant catch-all permanent disruption, opponent reveals possible replacement. |
| 15 | 1 | Chef's Kiss | 1RR instant copies/retargets an opponent-controlled spell, political but randomized target selection; can be unsafe vs targeted removal. |
| 16 | 1 | City of Brass | Land — Untapped any-color fixer costing damage/life. |
| 17 | 1 | Command Tower | Land — Untapped guaranteed UBR fixing. |
| 18 | 1 | Cormela, Glamour Thief | UBR haste mana dork for instant/sorcery casting and death recursion for spells, turns copy storms into more casts. |
| 19 | 1 | Counterspell | UU unconditional counter, shields expensive Parnesse and win pieces; double blue requirement. |
| 20 | 1 | Dark Ritual | B to BBB one-shot, helps black generic spending but does not directly pay Parnesse blue/red. |
| 21 | 1 | Deflecting Swat | 3R retarget free if commander controlled, can shield win stack, not general counter or turn-ending protection. |
| 22 | 1 | Demonic Tutor | 1B unrestricted tutor for Reiterate, Ral, Onyx, mana/combo shields. |
| 23 | 1 | Display of Power | 1RR? Instant copy an arbitrary number of instant/sorceries on stack; exact current Oracle/cost must be rechecked before paid line, mostly high-ceiling stack copier. |
| 24 | 1 | Double Vision | 3RR first instant/sorcery each turn is copied, slow engine but repeated commander triggers if board survives. |
| 25 | 1 | Dualcaster Mage | 1RR flash ETB copy instant/sorcery on stack, body+value, potential combos if paired properly; also creature vulnerable. |
| 26 | 1 | Errant, Street Artist | U legendary tap + 1U copy SPELL you control that wasn't cast, so needs another copy first; commander synergy after setup. |
| 27 | 1 | Exotic Orchard | Land — Mana color conditional on opponents' lands, usually available in multiplayer but not guaranteed. |
| 28 | 1 | Feed the Swarm | 1B sorcery destroys creature/enchantment controlled by opponent for life equal MV, scarce black enchantment answer. |
| 29 | 1 | Fellwar Stone | Two-mana color rock depending on lands controlled by opponents, quick mana progression. |
| 30 | 1 | Flooded Strand | Land — Fetchland for appropriate land subtype among shocks/original duals/triome, 1 life. |
| 31 | 1 | Frantic Search | 2U draw2/discard2/untap 3 lands, can be mana-neutral or better with land multipliers. |
| 32 | 1 | Galvanic Iteration | UR instant sets next instant/sorcery copy that turn, flashback later; conditional Parnesse trigger. |
| 33 | 1 | Goblin Electromancer | UR discounts generic instants/sorceries, doesn't reduce colored RR/UU. |
| 34 | 1 | Grapeshot | 1R storm burn finisher, each storm COPY triggers Parnesse and magecraft, but each target must be legal and storm count matters. |
| 35 | 1 | Harmonic Prodigy | 1R Shaman Wizard, increases relevant Wizard/ Shaman triggered abilities including Parnesse and Storm-Kiln; fragile. |
| 36 | 1 | Hexing Squelcher | Red spell protection/rate piece, source-approved Oracle snapshot, exact rare rules need separate live check before combo claim. |
| 37 | 1 | Increasing Vengeance | RR copy instant/sorcery controlled by you, flashback for more; graveyard cost and stack setup. |
| 38 | 2 | Island | Land — Basic colored source with lawful repeated copies, mitigates nonbasic hate. |
| 39 | 1 | Izzet Signet | Two-mana UR filter requiring {1} input, helps copy spell RR. |
| 40 | 1 | Jeska's Will | 2R red burst depending opponent hand; top-three access if commander present, scaling Reiterate seed. |
| 41 | 1 | Kess, Dissident Mage | 2UBR once on your turn instant/sorcery cast from graveyard, spell recursion, not copying herself. |
| 42 | 1 | Luxury Suite | Land — Conditional multiplayer untapped dual, colored pips. |
| 43 | 1 | Mana Confluence | Land — Untapped any-color fixer costing damage/life. |
| 44 | 1 | Mana Drain | UU counter then colorless equal countered MV next main phase, cannot substitute fixed colors. |
| 45 | 1 | Mana Geyser | 3RR red mana equal tapped lands opponents control; Reiterate buyback needs enough red output. |
| 46 | 1 | Marsh Flats | Land — Fetchland for appropriate land subtype among shocks/original duals/triome, 1 life. |
| 47 | 1 | Misty Rainforest | Land — Fetchland for appropriate land subtype among shocks/original duals/triome, 1 life. |
| 48 | 1 | Mizzix's Mastery | 3R card copy in exile CAST as spell, not directly a spell copy that triggers Parnesse; recursion still powerful. |
| 49 | 1 | Morphic Pool | Land — Conditional multiplayer untapped dual, colored pips. |
| 50 | 3 | Mountain | Land — Basic colored source with lawful repeated copies, mitigates nonbasic hate. |
| 51 | 1 | Narset's Reversal | UU copies target instant/sorcery spell and returns it to hand; timing and copy target choices central. |
| 52 | 1 | Nightscape Familiar | 1B reduces generic cost of blue and red spells only, not colored pips; blocks/remains on table. |
| 53 | 1 | Otawara, Soaring City | Land — Untapped U or channel bounce at resource cost. |
| 54 | 1 | Polluted Delta | Land — Fetchland for appropriate land subtype among shocks/original duals/triome, 1 life. |
| 55 | 1 | Ponder | U look3 manipulate top/shuffle then draw, selection. |
| 56 | 1 | Preordain | U scry2/draw, smooth combo/protection draws. |
| 57 | 1 | Primal Amulet // Primal Wellspring | 4MV discount then transforms with spell casts, Wellspring mana used to cast instant/sorcery copies it; slow in fast game. |
| 58 | 1 | Prismari, the Inspiration | Commander-specific spell-copy/storm synergy (own instant/sorcery), multiple stack copies trigger Parnesse; high MV setup. |
| 59 | 1 | Professor Onyx | 4BB planeswalker magecraft each opponent loses2/controller gains2 per spell cast/copy, primary win without combat. |
| 60 | 1 | Pyromancer's Goggles | 5MV mana rock red plus copy red instant/sorcery when used to cast, big setup; copies on stack trigger. |
| 61 | 1 | Rakdos Signet | Two mana BR filtering with generic input; fixes R/B cast. |
| 62 | 1 | Ral, Storm Conduit | 2UR magecraft deals1 to target opponent/walker per cast/copy, win with Reiterate storm loop; fragile. |
| 63 | 1 | Reflecting Pool | Land — Mana color conditioned by other producible land mana; not guaranteed solo. |
| 64 | 1 | Reiterate | 1RR instant copy instant/sorcery, buyback {3} allows same card re-cast; needs 4RR total and sufficiently productive spell. |
| 65 | 1 | Replication Technique | 4U sorcery demonstrate copy target permanent, own SPELL copy triggers Parnesse but opponent's copy does not. |
| 66 | 1 | Return the Favor | RRR instant modal copy spell/retarget or redirection; genuine stack copying, not all choices equally safe. |
| 67 | 1 | Reverberate | RR copy target instant/sorcery on stack, triggers Parnesse and magecraft on resolution. |
| 68 | 1 | Rhystic Study | 2U taxation card draw in multiplayer, vital sustained refill. |
| 69 | 1 | Scalding Tarn | Land — Fetchland for appropriate land subtype among shocks/original duals/triome, 1 life. |
| 70 | 1 | Sedgemoor Witch | 2B magecraft produces Pest for casts/copied instant/sorcery, blocker defense and sacrifice material. |
| 71 | 1 | Shivan Reef | Land — Untapped painland paired colors and generic, life cost when colored. |
| 72 | 1 | Sol Ring | 1 CC each turn, helps generic commander but not UBR. |
| 73 | 1 | Steam Vents | Land — Fetchable typed dual/shock that pays UBR pair; shock untapped needs 2 life. |
| 74 | 1 | Storm-Kiln Artist | 3R magecraft creates Treasure per spell cast OR copied, scalable mana for Reiterate/Bonus Round; body can die. |
| 75 | 1 | Sulfurous Springs | Land — Untapped painland paired colors and generic, life cost when colored. |
| 76 | 1 | Sunken Palace | Land — Enters tapped U; special {1}{U},tap,EXILE SEVEN from GY makes U which when spent on casting spell/activating ability creates copy, not cheap/free. |
| 77 | 2 | Swamp | Land — Basic colored source with lawful repeated copies, mitigates nonbasic hate. |
| 78 | 1 | Talisman of Creativity | 2UR/C rock, life on colored mana, sustains RR/UU. |
| 79 | 1 | Talisman of Dominance | 2UB/C rock, life on colored mana, sustains commander. |
| 80 | 1 | Talisman of Indulgence | 2BR/C rock, life on colored mana, sustains red copy spells. |
| 81 | 1 | Tempt with Mayhem | 1RR instant targeting instant/sorcery; opponents MAY copy first, you copy once+one per accepting opponent, direct Parnesse political core, copies not cast. |
| 82 | 1 | Thousand-Year Storm | 4UR copies your instant/sorcery by number of prior spells cast this turn, spell copies produce magecraft/Parnesse but are not cast. |
| 83 | 1 | Thunderclap Drake | Blue creature with spell-copy enhancement/discount, source Oracle needed for exact trigger/cost; role spell-multiplication redundancy. |
| 84 | 1 | Training Center | Land — Conditional multiplayer untapped dual, colored pips. |
| 85 | 1 | Twinning Staff | 3 artifact replacement gives extra copy for events copying instant/sorcery one or more, 7 tap itself copy; high ceiling but 7 activation slow. |
| 86 | 1 | Underground Sea | Land — Fetchable typed dual/shock that pays UBR pair; shock untapped needs 2 life. |
| 87 | 1 | Urborg, Tomb of Yawgmoth | Land — Untapped B and all lands are Swamps, helps BB and mana filters. |
| 88 | 1 | Verdant Catacombs | Land — Fetchland for appropriate land subtype among shocks/original duals/triome, 1 life. |
| 89 | 1 | Veyran, Voice of Duality | 1UR Magecraft multiplier on instant/sorcery cast/copy, also grows with them; can double Parnesse triggered ability because Parnesse triggers from copying instant/sorcery. |
| 90 | 1 | Volcanic Island | Land — Fetchable typed dual/shock that pays UBR pair; shock untapped needs 2 life. |
| 91 | 1 | Wandering Archaic // Explore the Vastlands | 5-mana reactive opponent instant/sorcery copy unless they pay2; OUR copies trigger Parnesse but opponent controls rate and spell choice. |
| 92 | 1 | Watery Grave | Land — Fetchable typed dual/shock that pays UBR pair; shock untapped needs 2 life. |
| 93 | 1 | Windfall | 2U each discards and draws equal largest hand discarded, reload but gives enemies fresh interaction. |
| 94 | 1 | Wizard's Staff | 1U equipment equip Wizard {1} valid for Parnesse Vampire WIZARD, grants prowess and one extra trigger from equipped creature, including its copy-gift. |
| 95 | 1 | Xander's Lounge | Land — Typed tapped UBR triome/cycle, first-turn tempo expense. |
| 96 | 1 | Zevlor, Elturel Exile | 1UBR tap ability, next target spell single-opponent spreads spell copies to other opponents when cast; needs tap-ready commander support. |

**Role aggregation:** 35 lands / 8 fetches / 3 original duals / 3 shocks / basics 2U,3R,2B, one tapped triome and Sunken Palace; 10-ish repeatable nonland mana sources, 1 ritual source (static model), defensive counter/retarget package (Offer, Counterspell, Mana Drain, Deflecting, Chaos Warp, Feed), Demonic Tutor and quality cantrips/draw, copy spells and spell-copy triggers, repeated game-end magecraft payoffs (Ral, Onyx), 3+ mana high-setup engines, politics. Weakest potential slots are `Wandering Archaic` (reactive 5-MV opponent pays two), `Double Vision` (5-MV first-copy per turn only), `Primal Amulet` (4-MV setup before transform), `Pyromancer's Goggles` (5-MV red-only), `Chef's Kiss` (opponent target/risk), or `Display of Power` (stack-dependent); do NOT cut life saving removal, protection, cheap ramp or actual kill payoffs to satisfy a raw score.

## Mana, interaction and combo viability

**Cost** Parnesse {2}UBR requires three colors + two other mana, not just five mixed. 35 lands and 10 repeatable mana nonlands support slower 5-MV leader. Static model nominal land source U21, B19, R20; T5 42.54% five land drops and 86.1% at least some U/B/R source presence are **no-mulligan presence estimates**, not joint cast probability and not copy-combo win rate. Sunken Palace ETB tapped and produces U normally; its special mode is `{1}{U},{T}, exile SEVEN cards from GY: Add {U}`, and **only spending that particular mana to cast a spell or activate an ability** causes a delayed copy trigger. For a spell copying, Parnesse triggers; for ONLY an activated ability copied, she does NOT. Seven GY cards are real cost; not free late-game color fixer. Mana Geyser makes R for opponents' TAPped lands not cards in hands; Jeska's Will counts target opponent's hand for mana and different modes depending on commander while casting.

**Red-team copy-engine cost**: Reiterate costs {1}{R}{R}, buyback {3}, total {4}{R}{R} = SIX mana for reusable copy. If target Mana Geyser is on stack and a Reiterate copy makes **at least six R**, using Reiterate on that spell can be maintained with available resources, and at SEVEN+ red mana per cycle it generates net mana. A copy of the original spell itself is placed on stack and resolves separately, and the original stays until copy loops end. Must initially have enough mana for original Geyser (3RR) AND buyback Reiterate (4RR) unless other source pays; can't claim "six mana total" from nothing. Opponents can counter either target or the repeated copy spell.

**Protection cadence**: Parnesse's four-life tax is a triggered ability and may be countered itself, only fires when actual targeting occurs. Paying life is not damage and cannot be prevented via damage prevention; a player who lacks four life may not pay if doing so would take them below zero. A copy belonging to opponent that retargets Parnesse or your permanent triggers protection because it is opponent-controlled; opponents instead can retarget each other. On a COPY GIFT you choose up to one target opponent, NOT all opponents by default. Stacking additional Parnesse triggers from Harmonic Prodigy, Veyran and Wizard Staff can create more optional gifts; some trigger sources grant extra copy to YOU (Twinning Staff), not automatic grants to all opponents.

## Candidate pool and competing cuts

**126 M5 routes considered by distinct function and actual suggested slot cost, including 122 commander-synergy P3 and 4 performance-only**, but a model PASS doesn't override timing/control. These repeatedly suggest cutting Wandering Archaic, Wizard's Staff, Rhystic Study, Jeska's Will, Mana Drain, Talisman, protection and generic draw; many also recommend creature-token loops unrelated to Parnesse's instant/sorcery copy signature.

| Challenger(s) | Exact modeled cut / better alternate | Authored judgment |
|---|---|---|
| **Twincast** (M5 #3) | Model cuts **Wandering Archaic**. Twincast {U}{U} directly copies any instant/sorcery spell; Parnesse trigger is guaranteed if target resolves. | **Best conditional improvement proposal**: Twincast IN / Wandering Archaic OUT, if pod is fast and opponents always pay Archaic tax. Converts five-mana fragile reactive copier into reliable two-mana spell-copy/stack interaction. BUT Archaic can copy **opponent** spells repeatedly on turns they decline to pay, and its back face adds option. No forced change without evidence. |
| **Swarm Intelligence** (M5 #1) | Wandering Archaic | {6}{U} enchantment doubles every instant/sorcery YOU cast once on stack, produces Parnesse triggers, but seven mana beats five-MV Archaic and only after additional casts; vulnerable to removal, copy overload may be win-more. HOLD. |
| **Wild Ricochet** (#2) | Deflecting Swat | Retarget+copy spell gives commander trigger but costs 4, unlike Swat's conditional FREE protective line. Reject loss of core shields. |
| **Expansion // Explosion, Insidious Will, Three Steps Ahead, Sublime Epiphany** | M5 cuts Rhystic Study/Mana Drain | Strong value and stack-copy potential, but can't remove early repeated card advantage and UU hard counter without profiling opponent disruption. HOLD. |
| **Resonating Lute / Seething Song / Brass's Bounty / Dragon's Desire** (M5 #8/#12 etc) | Jeska's Will or Talisman Indulgence | Big resource ceiling but Lute four-mana ramp and Song/Brass one-color bursts compete with Grixis mana permanence and Ral/Onyx turn. Lute may be excellent on longer game but cannot replace cheap mana burst unconditionally. HOLD. |
| **Naru Meha / Radiant Performer / Rootha / Echo Mage / Melek / Krark** | Model cuts Veyran or Wizard's Staff | Many genuinely copy spells, some impose creatures, levels, target-specific costs, and Kark coin flips. Replacing Veyran/Staff sacrifices doubled commander trigger at 3/2 MV; opponent-value/politics and instant timing degraded. HOLD. |
| **Fury Storm / Flare of Duplication / Storm King's Thunder** | Wandering Archaic or Wizard Staff, previous rejection | Fury scales commander casts but Parnesse five mana; Flare may use sacrifice red creature free (which may mean sacrificing Parnesse), then loses source; Storm Thunder {X} wants RRRed mana at late stage. CONDITIONAL. |
| **Fork / Twinferno / Teach by Example / See Double / Dual Strike** | Wandering Archaic / weaker copier | Cheap spell copies direct Parnesse lift, but redundant with current Reverberate, Return the Favor, Iteration, Reiterate, Tempt; spells need appropriate target on stack or next cast. Sidegrade absent removal-heavy/proactive-timing evidence. HOLD. |
| **Saw in Half / Blue Sun's Twilight / Ghostly Flicker / creature cloning routes** | Model cuts Feed the Swarm, Grapeshot, or Wandering Archaic | Creature copy ≠ copying spell; if instant/sorcery effect creates token copy of creature, Parnesse doesn't trigger unless the **spell itself** was copied. Cutting Grapeshot storm finisher or rare black enchantment removal is strategic regression. REJECT exact swaps. |
| **Hive Mind / Curse of Echoes / Bonus Round** (historical) | Bonus Round or Wandering Archaic | Opponent spells copied under OPPONENT controllers don't trigger our Parnesse; these can hand enemies a stronger storm/combo than own deck. Bonus Round already in list: specific hazard, not universally safe. HOLD. |
| **Venser, Fervent Forger / Chandra, Hope's Beacon / Arcane Bombardment** | Double Vision/Archaic | Venser six and reactive but opponent spell copy x2; Chandra 6 once-per-turn, Arcane Bombardment 6 copies *cards* then casts them (not direct Parnesse copy trigger). Don't re-add prior cut under incorrect trigger assumptions. |
| **Underworld Breach / generic Oracle+Consultation and Kiki loops** | Rhystic/Mana Drain/Wizard Staff | High power independent wins that don't enhance Parnesse copying-spells/politics, risk homogenization and require other pieces. REJECT. |
| **Darkwater Catacombs / Arid Mesa; Dimir Signet / Talisman Indulgence** | Colored mana changes | Darkwater conditional filter cannot replace premium fetch reliability; Dimir Signet requires generic input and shifts red pip access away from RR copy package. HOLD approved lands. |

**Strongest challenger costed both ways:** If an opponent casts a 2MV instant they value protecting and has two unused mana, Wandering Archaic {5} in play gives no Parnesse copy after they pay {2}. Twincast {U}{U} in hand can copy that spell immediately if controller has UU and opportunity, trigger commander, with independent target choice. But if opponents cast four spells across a round while tapped out, Archaic can copy EACH spell for no extra mana while Twincast copies only one and costs a card+UU; a noncommander flavor-driven deck should not make unconditional claims absent meta. Unchanged approval remains defensible.

## Oracle, legality and rules

1. Parnesse first ability is triggered 4-life counter tax on opposing targeting (you or PERMANENT you control), not shield for untargeted sweepers nor generic Ward keyword; copies of spell/ability under opponents can trigger it.
2. Second ability triggers when **you copy a spell** (CR707.10), chooses up to one target opponent. They may copy but YOU are not required to choose anyone and can refrain to avoid helping opponents.
3. Copying CARD and then CASTING that copy (Mizzix's Mastery, Arcane Bombardment) is **not** copy a spell. Cast can trigger magecraft, but not Parnesse copying trigger merely for that action.
4. Tempt with Mayhem official Oracle: target instant/sorcery, each opponent may copy in turn order, THEN you copy once + once for EACH opponent who accepted. If three opponents all accept, you create FOUR copies, each triggers Parnesse separately; 3 opponent copies do not trigger Parnesse for you; our four copies resolve before opponents' copies (absent stack responses). [Wizards MH3 notes](https://magic.wizards.com/en/news/feature/modern-horizons-3-release-notes).
5. Tempt original target spell remains on stack; spell copies are **not cast**, don't trigger "when CAST" abilities; can choose new legal targets, copied mode/X stays as original.
6. Harmonic Prodigy targets Wizards/Shamans and Parnesse is Wizard; Wizard Staff equip Wizard {1} valid (contrast Obeka Warlock required {3}). Veyran duplicates triggers caused by casting or copying instant/sorcery, conditionally adds +1 trigger.
7. Each separate Parnesse gift may trigger additional gifts if Parnesse triggered twice, but it's optional. **Opponent creates copies controlled by them** → Parnesse on YOUR board does not recursively trigger on those.
8. **Bonus Round** copies opponents' instants and sorceries as well as ours when cast that turn, including opponent counterspell over a combo. Cannot label all copies "ours", opponent threat can double.
9. Sunken Palace ETB tapped and its special ability requires **{1}{U},tap,exile7 GY** to produce U with copy delayed trigger; if spent for an activated ability instead of spell, copy ability not trigger Parnesse. No automatic infinite without resource.
10. Reiterate buyback costs 6 total (4RR), original Mana Geyser 5 mana. Reiterate/Mana Geyser copies producing >=6R can sustain; >=7R gives net R if repeatedly copied, while base cast costs initially real mana.
11. Jeska's Will mode copying keeps same chosen modes; if commander control condition met when **casting original**, both modes selected, copy of it retains both; target opponent hand size observed per resolution.
12. Ral's cast/copy triggers ping target opponent/planeswalker (can redirect targets), Professor Onyx's magecraft drains each opponent 2 and gains you 2; fully paid repeated copier can win but opponent responds between stack objects.
13. Twinning Staff replacement gives *one additional copy* when would copy instant/sorcery spell one or more times; those new copies trigger Parnesse if YOU make them, doesn't automatically cast extra spells.
14. Prismari's storm copies spell on stack; counts spells CAST before it this turn (not copies) for storm number, but storm COPIES do count for Parnesse/Onyx/Ral triggers.
15. Replication Technique demonstrate YOU copy spell; target opponent copy of spell belongs opponent, not triggering own Parnesse. Demonstrate may give opponent a free permanent and political bargaining matters.
16. Wandering Archaic opponent may PAY {2} to prevent your copy; each declined payment creates YOUR instant/sorcery spell copy, triggering Parnesse; opponent copy/stack windows matter.
17. Thassa's Oracle / Breach generic combos not needed to maximize natural ceiling, no project exceptions. Snapshot Oct15/16 official Commander legality UBR PASS. Any later swap requires all-100 fresh Oracle/checkpoints; no unapproved changes.

## Finite sequencing and adversarial scenarios

Manually costed states with realistic opponent intervention; not randomized games or asserted win-rate.

| Test | Input and action | Verified result / downside |
|---|---|---|
| P1 | Five total mana U,B,R,C,C, Parnesse in zone | Can cast {2}UBR exactly; five mana U,B,C,C,C cannot pay R. |
| P2 | Opponent targets our Parnesse with removal, keeps 4 life and mana available | Tax trigger resolves, may pay four life to let spell resolve; Parnesse not indestructible. |
| P3 | Opponent uses untargeted board wipe | No tax from first ability; all creatures may die unless other answer. |
| P4 | Our Reverberate RR copies a target opponent instant in stack, Parnesse active | YOU create one copy; Parnesse up to one opponent may be given copy; opponent's extra copy doesn't itself retrigger YOU. |
| P5 | Tempt with Mayhem targeting own spell, all three opponents decline | You still copy it ONCE; one Parnesse trigger. |
| P6 | Tempt with Mayhem all three opponents accept | Opponents each get one copy, you copy spell FOUR times, four Parnesse triggers; our copies resolve first under standard stacking. |
| P7 | Mizzix's Mastery targets GY instant/sorc, creates copy of card then casts it | You CAST copy, triggering magecraft but not Parnesse direct copy-spell condition. |
| P8 | Mizzix's Mastery overload and 4 GY instants, no other copy engines | Those casts alone give 4 cast triggers for Onyx/Ral; Parnesse gets zero from them absent actual spell copying. |
| P9 | Bonus Round resolved, opponent casts Counterspell against our key spell | Bonus Round copies opponent Counterspell under their control; our Parnesse does not protect against untargeted spell only targeted own permanent/player cases, so counter copy dangerous. |
| P10 | Wizard Staff on Parnesse, Harmonic Prodigy on table, Parnesse copies one spell | Original + Staff + Prodigy extra Parnesse triggers, each optional; not an infinite by itself. |
| P11 | Veyran also on board, instantaneous magecraft event | Each applicable replacement/additional-trigger effect leads an extra Parnesse trigger; additions not geometric absent effects that explicitly compound, evaluate source timing. |
| P12 | Mana Geyser 3RR cast, opponents have 5 tapped lands | Makes 5R, Reiterate with buyback 6 mana cannot break even from copied Geyser; loops fail without other mana. |
| P13 | Mana Geyser cast, opponents have 7 tapped lands, Reiterate with buyback paid 4RR | Reiterate copied Geyser makes 7R per iteration, pay 6 to recast, net 1R plus copy triggers, contingent spell remaining legal and cards protected. |
| P14 | Jeska's Will targeted opponent 3 hand cards, Reiterate buyback 6 | Just 3R per copy, cannot sustain absent alternate mana; don't label unlimited. |
| P15 | Sunken Palace special activation with fewer than 7 GY cards | Cannot pay activation, only normal tap for U remains. |
| P16 | Special Palace U spent on a creature activated ability rather than spell | Copy activated ability but not Parnesse's copied-SPELL trigger. |
| P17 | Wandering Archaic in play, opponent casts instant and pays 2 | No copy from Archaic, so no Parnesse trigger; five mana setup potentially zero payoff. |
| P18 | Wandering Archaic in play, opponent casts three instants no spare mana | We can get 3 copied spells (one each) and Parnesse 3 triggers, outscores one Twincast. |
| P19 | Twincast UU in hand and one spell on stack | Direct copy spell under our control, Parnesse triggers, but Twincast is single-use card. |
| P20 | Ral Storm Conduit in play, one copy spell created with Onyx also | Ral triggers one 1-damage target event and Onyx drains all opponents 2; not automatically lethal unless repetition. |
| P21 | Parnesse gives opponent copy and opponent retargets our commander | Because opponent controls copy targeting our permanent, Parnesse first 4-life tax triggers; opponent can pay, other target choices matter. |
| P22 | Twin Staff copies a spell once with replacement | Two copies created under our control, 2 Parnesse triggers, not two casts. |
| P23 | Replication Technique demonstrate chosen opponent gets spell copy | Their copy under their control does not satisfy Parnesse YOU copy; our demonstrate copy does. |
| P24 | Mana Drain resolves targeting opponent spell MV6; next main phase gains CCCCCC | Colorless cannot pay RR for Reiterate or UU counter on its own. |
| P25 | Rhystic Study in play, opponent casts multiple low-cost spells | Repeated tax opportunities, unless opponents pay; cut for high-MV copy enchantment can starve protection. |

**Adversarial dynamic:** Against fast blue players with spare mana, five-mana Wandering Archaic is a fragile generic obstacle whose copy option they can buy off. Two-mana Twincast produces exactly one immediate Parnesse-native spell copy and one magecraft set at crucial priority window. Conversely in grind pods tapped down by previous spells, Archaic generates multiple copy events without consuming hand cards, and back-face Explore option is relevant. This context-sensitive comparison is MATERIAL but insufficient to apply automatically to locked deck.

## Conclusions and unresolved evidence

**Verdict KEEP canonical 100** unchanged, with one **unapplied conditional proposal** `Twincast IN / Wandering Archaic // Explore the Vastlands OUT` for fast interactive opponents who routinely pay Archaic {2} tax; existing approved list already tuned and duplicate copy spells can be redundant, so no universal improvement shown. 100 cards/96 names/35 lands/basic repeats only, UBR Commander legality per approved Oct15 and engineering Oct16, no exceptions. No material new legality concern. Original M6.4 62/62 distinct from comprehensive new count and independent GrokBot Pass C remains undone.

**Coverage** all 96 names with weighted 100 cards and role/weakness ledger; 126 M5 pair routes categorized, true alternate cuts identified; 25 paid/opponent-aware finite examples, explicit preexisting unresolved 1 rules question / Bonus Round warning, externally checked Parnesse/Tempt/Palace Oracle. No fresh whole 100-card 2026-10-20 Oracle API pass or stochastic four-player results. Engineering-only exact-head CI mandatory before PR merge; sequential tracker 45→46 only after artifact merged + own tracker exact-head CI. No owner reapproval/milestone certification.
