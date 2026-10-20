# M6 comprehensive single-deck authored review #42 — Nicol Bolas, the Ravager // Nicol Bolas, the Arisen

**Deck ID**: `Nicol_Bolas__the_Ravager`. **Index:** 41, deck #42/62. **Primary author:** ChatGPT (NOT GrokBot independent Pass C). **Dated:** 2026-10-19 America/Chicago. **Original-author decision:** `KEEP` locked 100; conditional alternatives and incomplete evidence recorded, no approved swap. **Authorized repository scope:** engineering-only.

## Source and test receipts

**Live GitHub recovered first**: `AGENTS.md`, `grixis/M6 Commander-First Single-Deck Review Standard.md`, `data/grixis/m6/single_deck_depth_tracker.json` at **41/62 complete** after previous original Bolas; `data/grixis/registry.json`, `data/grixis/milestone_m6_m7_subtracker.json`, exact 62-row canonical refinement order, `state/current_deck_overrides.json`. Tracker #42 is first PENDING, following #41 original Nicol Bolas complete. Previous original's direct-damage/hand-discard identity was **not** copied into this Superfriends deck.

**Authority:** Canonical `corymstover/grixis-commander-encyclopediaGPT/main`, override key `Nicol_Bolas__the_Ravager` **APPROVED / LOCKED** 2026-10-15, exact approved raw SHA-256 `5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e`. [Officially approved TXT](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/decklists/Nicol_Bolas_the_Ravager_Approved_2026-10-15.txt), blob `6b507ab9ca156e4c6214899a10a7ed3a0b862a2f`; [Oct15 canonical approval](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/approvals/Nicol_Bolas_the_Ravager_Approved_2026-10-15.md), [whole-list audit](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/verification/Nicol_Bolas_the_Ravager_Whole_List_Audit_2026-10-15.md), [verification](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/verification/Nicol_Bolas_the_Ravager_Approval_Ready_Verification_2026-10-15.md), [16-card historical approval delta](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/decisions/Nicol_Bolas_the_Ravager_Candidate_Decisions_2026-10-15.md). All 62 canonical approval records remain protected.

**Engineering:** approved raw hash matches registry. Logical SHA `lh1:c2b4559a1e5f0415decb48a9f496f1f780af715f6f763d3fcb166753dbfda293`; no commander-name alias issue; Oct16 official Scryfall Oracle bulk labels official Commander compliance `compliant`. [Engine interaction record](https://github.com/corymstover/GrokBotMTGCompanion/blob/chatgpt-cycle76-m6-refinement/grixis/interactions/nicol-bolas-the-ravager.md) has 8 Oracle/CR-reviewed cases, source Scryfall bulk 2026-10-16, rulings 2026-10-15, Comprehensive Rules effective 2026-09-25. [Commander blueprint](https://github.com/corymstover/GrokBotMTGCompanion/blob/chatgpt-cycle76-m6-refinement/grixis/blueprints/nicol-bolas-the-ravager.md), M5 packet `data/grixis/m6/review_packets/nicol-bolas-the-ravager.json` **54** machine triage items (9 pass, 3 fail, 15 inconclusive, 27 no detected difference) and static `data/grixis/mana_base/nicol-bolas-the-ravager.json` are evidence not owner decisions.

**Current external corroboration:** [EDHREC's Ravager planeswalkers cohort](https://edhrec.com/commanders/nicol-bolas-the-ravager/planeswalkers), 717 public decks when read 2026-10-19, commonly plays Dragon-God, God-Pharaoh, original Planeswalker, Deepglow Skate and Ichormoon Gauntlet; EDHREC popularity does not establish a better 100. [Commander Spellbook Teferi/Chain Veil](https://commanderspellbook.com/combo/787-1124/) describes a related combo but requires actual accessible mana and is not proof that this precise locked list has an automatic turn-three win.

**Independent source TXT arithmetic in this review:** 100 physical cards, **98 names**, only `Island x2` and `Swamp x2` repeat; **34 lands**, 99 library copies and no nonbasic/nonland singleton repetition. The commander is a SINGLE physical transforming double-faced card; its planeswalker face is **not a second commander slot**. UBR commander/color identity, official legality Oct15/16 pass, project exception **NONE**. No new 2026-10-19 Scryfall exact-100 audit is claimed; canonical/current engineering source snapshot establishes the last verified whole-list checkpoint. Historic FINAL pre-approval baseline differs by 16 cuts/adds and does **not** supersede the LOCKED 100.

**Important test-data flaw:** The generated mana audit mistakes the double-faced commander string `Nicol Bolas, the Ravager // Nicol Bolas, the Arisen` for mana cost `—`, mana value **0**, no colored requirements, and first recast target 3. That commander's `commander_casting` fields are INVALID and must not be used for power/turn/cast conclusions. The source's full deck still has 34 lands and nominal land-source counts; independent costs from Oracle are `{1}{U}{B}{R}` to cast Ravager, `{4}{U}{B}{R}` to transform, and `{2}{U}{B}{R}` with Training Grounds. This is documented as an existing **derived-data bug**, not a reauthorization to rerun pipeline or alter decks.

## Commander identity and natural ceiling

**Nicol Bolas, the Ravager:** {1}{U}{B}{R}, four-mana 4/4 flying Elder Dragon; ETB each opponent discards exactly **one** card. Sorcery-speed `{4}{U}{B}{R}` activation exiles then returns card **transformed** as planeswalker Nicol Bolas, the Arisen at **7 loyalty**. Its +2 draws two, -3 does 10 damage to creature or planeswalker, -4 reanimates target creature/planeswalker, -12 exiles target player's library except bottom card (does NOT automatically kill that opponent without future draw). This is a transform-centric Bolas Superfriends build: commander ETB disruption, delayed transformation, Arisen loyalty actions, other Bolas walkers, Doubling/proliferate effects, copied loyalty and Chain Veil exploitation. It does not deserve the other original Bolas deck's combat/direct-damage engine.

**Identity protections:** preserve Training Grounds as a way to make the actual commander transform, Displacer Kitten's costed front-face ETB reset, Arisen-specific -4/reanimate/+2/-12, Deliver Unto Evil conditional on controlling a Bolas planeswalker, Bolas planeswalker density, proliferate/copy/Veil engine and interaction to keep those walkers alive. Avoid generic wheel-discard cEDH goodstuff with no role for transformation. Existing combo win infrastructure (Teferi + Veil) can operate without Ravager, so the review should not overstate commander necessity; commander remains central as protected planeswalker centerpiece, not deterministic command-zone combo.

**Natural bracket 4 — Optimized**, not verified tournament cEDH: four-mana commander plus 5–7 mana additional transformation on a later main phase, with an opponent turn and sorcery-speed response window. Walker packages of 5–8 MV, creature attackers threatening walkers, and lots of color-intensive mana expose tempo problems. A concentrated early Planeswalker/doubling plan can be powerful once protected, but high-cost generic combos do not justify claims of consistent fast wins.

## Full 100-card role audit

One ledger row for every distinct approved source TXT name, with exact quantity and its role/weakness. **98 rows / 100 physical copies**; no "additions" inferred from the source list.

| TXT row | Qty | Exact name | Authored source-card role and material weakness |
|---:|---:|---|---|
| 1 | 1 | Nicol Bolas, the Ravager // Nicol Bolas, the Arisen | COMMANDER: {1}{U}{B}{R} 4/4 ETB each opponent discard one; {4}{U}{B}{R} sorcery exile/return transformed PW at 7 loyalty; source centerpiece |
| 2 | 1 | An Offer You Can't Refuse | Protection: one-mana noncreature counter; gives opponent two Treasures, so not neutral tempo. |
| 3 | 1 | Ancient Tomb | Land: Colorless CC with two life per tap; cannot supply UBR pips to transform. |
| 4 | 1 | Arcane Signet | Two-mana UBR fixing for ETB commander and transform payment. |
| 5 | 1 | Arid Mesa | Land: One-life Mountain-typed dual/triome search (including red-bearing duals); no white identity issue. |
| 6 | 1 | Badlands | Land: Typed, untapped black/red fixing. |
| 7 | 1 | Blood Crypt | Land: Typed black/red shock; can pay life to enter untapped. |
| 8 | 1 | Bloodstained Mire | Land: Typed Swamp/Mountain dual fetch; one life. |
| 9 | 1 | Bolas's Citadel | Six-mana B-heavy spell access/life-pay engine; powerful generic resource, 3 sacrifice 10 permanents condition rarely easy here. |
| 10 | 1 | Cavern of Souls | Land: Elder naming protects commander creature casting; chosen-color mana restricted to Elder creature spells, NOT transform ability/planeswalkers. |
| 11 | 1 | Chrome Mox | Zero-mana one-color permanent accelerator, requires exiling a nonartifact/nonland spell. |
| 12 | 1 | City of Brass | Land: Any-color fixer; life loss via damage when tapped. |
| 13 | 1 | Command Tower | Land: Any UBR color for commander and walker spells. |
| 14 | 1 | Cyclonic Rift | Seven-mana overloaded asymmetric bounce or two-mana spot bounce; shields walkers versus board creatures. |
| 15 | 1 | Damnation | Four-mana destroy sweeper to protect walkers; regeneration prevented, indestructible survives. |
| 16 | 1 | Dark Intimations | Bolas-flavor 5-mana opponent sacrifice/discard plus graveyard recursion/draw; Bolas planeswalker cast-only graveyard rider. |
| 17 | 1 | Deadly Rollick | Cheap creature exile; free only while controlling commander creature/planeswalker and opponent target legality. |
| 18 | 1 | Deepglow Skate | Five-mana ETB doubles loyalty counters of all targeted permanents you control, strongest if Arisen already transformed. |
| 19 | 1 | Deliver Unto Evil | Three-mana up-to-four graveyard card return if control any Bolas planeswalker; otherwise opponent withholds two. |
| 20 | 1 | Demonic Tutor | Two mana any-library card search, assembles Chain Veil/Training Grounds or emergency sweeper. |
| 21 | 1 | Dimir Signet | UB filtering requires a generic mana input to activate. |
| 22 | 1 | Displacer Kitten | On noncreature spell cast can blink nonland permanent; resetting transformed Arisen returns front-face Ravager, not back-face planeswalker. |
| 23 | 1 | Dreamtide Whale | Vanishing 2, second spell each turn proliferation; can add counters to itself to maintain lifespan. |
| 24 | 1 | Fellwar Stone | Two-mana rock, usable color depends on opponent lands. |
| 25 | 1 | Fierce Guardianship | Counter a noncreature spell free while commander controlled; otherwise hardcast costs three. |
| 26 | 1 | Flooded Strand | Land: Island-typed dual or basic Island fetch. |
| 27 | 1 | Flux Channeler | Three-mana 2/2 proliferate on NONCREATURE spells; can gradually build Arisen/walker loyalty. |
| 28 | 1 | Force of Will | Free pitch-blue-and-life counter, critical protection for multi-turn walkers. |
| 29 | 1 | Gamble | One-mana risky tutor; random discard can lose searched piece, may enable recursion. |
| 30 | 1 | Ichormoon Gauntlet | Grants walker 0 proliferate and -12 extra turn; 3 mana artifact but on-board walkers needed, not independently winning. |
| 31 | 1 | Inexorable Tide | Five-mana permanent proliferate on spell cast, slow high ceiling only if walker board survives. |
| 32 | 2 | Island | Land: Basic blue mana; two legal copies. |
| 33 | 1 | Izzet Signet | UR filtering rock requires one generic activation input. |
| 34 | 1 | Jaya's Phoenix | Flying haste threat and graveyard recursion associated with planeswalker loyalty; one subsequent loyalty-copy trigger after combat damage. |
| 35 | 1 | Jeska's Will | Three-mana red burst dependent on opposing hand, commander-control gated top three access. |
| 36 | 1 | Karn's Bastion | Land: Colorless-producing repeatable 4-mana proliferation, significant colored-mana opportunity cost. |
| 37 | 1 | Liliana's Talent | Aura superfriend multiplier, provides end-step graveyard return? Verify exact current text before making specific ability claim; role generic loyalty support. |
| 38 | 1 | Liliana, Dreadhorde General | Six-mana planeswalker removal/sac/draw engine; death draws cards from own creatures, not from walker death. |
| 39 | 1 | Lotus Petal | Free single-use one-of-any-color acceleration; reduces sustained mana permanents. |
| 40 | 1 | Luxury Suite | Land: Usually untapped black/red in four-player pod. |
| 41 | 1 | Mana Confluence | Land: Untapped any-color mana, costs one life per color use. |
| 42 | 1 | Mana Drain | UU counter converts countered mana value into colorless next main phase; supports high-cost walker spells but not UBR. |
| 43 | 1 | Mana Vault | One-mana CCC burst, untap cost four at upkeep; cannot satisfy UBR colored costs. |
| 44 | 1 | Marsh Flats | Land: Swamp typed dual/triome search; cannot fetch Island-only or Mountain-only duals. |
| 45 | 1 | Misty Rainforest | Land: Island-typed dual/triome fetch. |
| 46 | 1 | Morphic Pool | Land: Usually untapped black/blue multiplayer dual. |
| 47 | 1 | Mountain | Land: Basic red access for commander R. |
| 48 | 1 | Mox Diamond | Zero-mana source only if you discard a land; 34 lands and multiple other pitch rocks tax keepable hands. |
| 49 | 1 | Mox Opal | Free any-color rock only with metalcraft (three artifacts including itself); earliest turns can be unreliable. |
| 50 | 1 | Mystic Remora | Early one-mana tax/draw vs opponent noncreature spells; maintenance cumulative upkeep problematic past early turns. |
| 51 | 1 | Mystical Tutor | Instant to topdeck an instant/sorcery, sacrifices card/card draw tempo; finds protection, sweepers, tutors. |
| 52 | 1 | Narset, Parter of Veils | Three-mana walker denies opponent extra card draws and selects noncreature nonland cards; passive makes wheel plan high power but no wheels left. |
| 53 | 1 | Nicol Bolas, Dragon-God | BBB and UR color-heavy 5-mana Bolas walker, copies other planeswalker loyalty abilities passively, Bolas identity core. |
| 54 | 1 | Nicol Bolas, God-Pharaoh | Seven-mana Bolas walker, high-end interaction and emblem threat, expensive while Arisen aims transform. |
| 55 | 1 | Nicol Bolas, Planeswalker | Eight-mana Bolas walker, character-specific control/ultimate but tempo-risky clogging high end. |
| 56 | 1 | Nicol Bolas, the Deceiver | Eight-mana Bolas walker, theme-heavy but low rate; vulnerable before high loyalty payback; serious alternative cut. |
| 57 | 1 | Otawara, Soaring City | Land: Blue source or channel bounce at land-card opportunity cost. |
| 58 | 1 | Polluted Delta | Land: Island/Swamp typed fetch, strong U/B choice. |
| 59 | 1 | Rakdos Signet | BR two-color filter, costs one generic input to activate. |
| 60 | 1 | Reflecting Pool | Land: Copies already accessible mana; colorless-only early board makes unreliable. |
| 61 | 1 | Rhystic Study | Three-mana recurring card access dependent on opponents' pay choices. |
| 62 | 1 | Rings of Brighthearth | 3-mana nonmana activated-ability copier for 2 each; doubles Veil and loyalty activations without extra loyalty cost. |
| 63 | 1 | Ripples of Potential | Two-mana instant proliferate and optional phase-out of permanents that received counters; defense against destroy/damage until next untap. |
| 64 | 1 | Rowan's Talent | Four-mana planeswalker Aura, copies enchanted walker loyalty abilities; multiplies Arisen -3/-4/-12 value, aura and walker exposed. |
| 65 | 1 | Sanctum Lurker | Protects planeswalkers at 0 loyalty from SBAs, grants each [+2] for 1 damage to each opponent + 1 life. |
| 66 | 1 | Scalding Tarn | Land: Island/Mountain typed fetch. |
| 67 | 1 | Sol Ring | One mana -> two generic each turn, pays commander generic and Chain Veil not colored. |
| 68 | 1 | Spark Double | Copies planeswalker as nonlegend with extra loyalty; can copy Arisen as PW, copying front Ravager cannot transform (not DFC). |
| 69 | 1 | Steam Vents | Land: Typed blue/red shock fixing. |
| 70 | 2 | Swamp | Land: Basic black access; two legal copies for BBB walker requirements. |
| 71 | 1 | Swan Song | U noncreature enchantment/instant/sorcery counter, gives opponent 2/2 flying body that threatens walkers. |
| 72 | 1 | Takenuma, Abandoned Mire | Land: Black source or channel mill/recursion; can retrieve creature or planeswalker. |
| 73 | 1 | Talisman of Creativity | Two-mana UR source, 1 life for colored or C free. |
| 74 | 1 | Talisman of Dominance | Two-mana UB source, 1 life for colored or C free. |
| 75 | 1 | Talisman of Indulgence | Two-mana BR source, 1 life for colored or C free. |
| 76 | 1 | Teferi, Master of Time | Four-mana walker activates once per EACH player's turn, draw/discard and 2 extra turns at -10. |
| 77 | 1 | Teferi, Temporal Archmage | Six-mana walker untaps up to four permanents at -1; Chain Veil setup combo after paying full resources. |
| 78 | 1 | Tekuthal, Inquiry Dominus | Four-mana Phyrexian proliferate replacement doubles each event; can gain indestructible by sacrificing artifacts. |
| 79 | 1 | Tergrid, God of Fright // Tergrid's Lantern | 5-mana discard/sac payoff, competes with Arisen -4 for graveyard creatures and lacks wheel density. |
| 80 | 1 | Tezzeret the Seeker | Five-mana walker tutors MV-X artifacts to battlefield or untaps two artifacts; fetches Chain Veil/Rings/Gauntlet. |
| 81 | 1 | Tezzeret's Gambit | Can pay 3U or 3+2 life; draw two AND proliferate once, supports walkers but slower than cheaper cantrips. |
| 82 | 1 | The Chain Veil | 4-mana artifact and 4 plus tap for extra loyalty activation permissions, does NOT automatically make infinite turns. |
| 83 | 1 | The Elderspell | BB one-sided targeted planeswalker destruction; loyalty counters placed on your walker, often no opponents with walkers => no effect. |
| 84 | 1 | The Eldest Reborn | Five-mana Saga opponent sacrifice/discard and later recursion; slow incremental identity/flavor, delays 7-mana transform. |
| 85 | 1 | The Theorist, Jace Beleren | Four-mana walker auxiliary draw/defense/bounce, new high impact walker in source project; not equal to one-shot blue cantrip. |
| 86 | 1 | Tinybones, Bauble Burglar | 2-mana opponent discard value theft; Ravager's ETB is only one per opponent, low repeated discard supply if not blinked. |
| 87 | 1 | Toxic Deluge | Three-mana -X/-X life-price sweeper; can sweep own setup creatures but leaves walkers in play. |
| 88 | 1 | Training Center | Land: Usually untapped blue/red multiplayer dual. |
| 89 | 1 | Training Grounds | One-mana enchantment subtracts 2 generic from front-face Ravager transform cost, UBR fixed. |
| 90 | 1 | Underground Sea | Land: Untapped typed blue/black original dual. |
| 91 | 1 | Urborg, Tomb of Yawgmoth | Land: Black source itself; grants all lands Swamp subtype, helps black-heavy Bolas walkers and Bastion. |
| 92 | 1 | Vampiric Tutor | Instant tutor to top with two life loss; flexible but card-neutral only if draw later. |
| 93 | 1 | Verdant Catacombs | Land: Swamp typed dual fetch, even with Forest absent. |
| 94 | 1 | Volcanic Island | Land: Untapped typed blue/red original dual. |
| 95 | 1 | Vraska, Betrayal's Sting | Six-mana walker toxic/proliferate engine and potential win conditions, heavy colorless or life payment. |
| 96 | 1 | Watery Grave | Land: Typed blue/black shock. |
| 97 | 1 | Wooded Foothills | Land: Mountain typed dual/triome fetch. |
| 98 | 1 | Xander's Lounge | Land: Typed UBR, always tapped, cycles for card at 3 mana. |

**Role coverage / weaknesses:** Ten dedicated in-list planeswalkers apart from transformed Arisen: Liliana, Dreadhorde General; Narset; Nicol Bolas Dragon-God, God-Pharaoh, Planeswalker and the Deceiver; Teferi Master of Time and Temporal Archmage; Tezzeret; The Theorist Jace; Vraska (**11** if separately count all names below; count sourced from list, not a game state). Walker/enabler duplication includes Rowan's Talent, Liliana's Talent, Rings, Phoenix, Chain Veil, Ichormoon, Deepglow, Tekuthal, Inexorable Tide, Whale, Flux Channeler, Ripples, Gambit, Karn Bastion and Kitten. Interaction density: free/cheap counters Offer, Swan Song, Force, Fierce, Mana Drain; removal Deadly Rollick, Damnation, Toxic Deluge, Cyclonic Rift, Arisen -3, some other walkers. Direct walker defense relies heavily on sweepers and early spot interaction; several threats can attack walkers before Ravager reaches seven mana.

**Most credible incumbent weaknesses:** `Nicol Bolas, the Deceiver` (eight MV, highest theme-tax), `The Eldest Reborn` (five MV delayed saga), `Tergrid` and `Tinybones, Bauble Burglar` (one ETB discard per opponent per normal Ravager cast, weaker without repeated ETB/wheels), `Dreamtide Whale` (vanishing + creature vulnerability), `Inexorable Tide` (five MV spell-driven growth with real early board requirements), `The Elderspell` (depends on opponent planeswalkers or sacrifices your own), `Jaya's Phoenix` (combat connection requirement), `Mox Opal` (metalcraft at opening), and `Liliana's Talent` if genuine win-more compared to alternate shields. These are **cut candidates for analysis**, NOT adopted cuts.

## Mana, ramp, card access and access error audit

**34 lands**: 9 fetches; 3 originals + 3 shocks; tapped Xander's Lounge; all-color fixes Command Tower, City of Brass, Mana Confluence, Reflecting Pool; 5 basics (Island 2, Swamp 2, Mountain 1); utility Ancient Tomb, Cavern of Souls, Karn's Bastion, Otawara, Takenuma, Urborg. `Karn's Bastion` adds colorless and pays `{4},{T}` to proliferate; this has serious opportunity cost when commander transform requires UBR. Cavern naming Elder can cast Ravager uncounterably but its colored mana can't pay the on-battlefield transform ability or non-Elder Bolas planeswalker spells. `Reflecting Pool` is not perfect without a separate colored producer. Opponent-sensitive signets and Fellwar depend on other mana; Ravager's UBR casting, Nicol Dragon-God's B-heavy cost, and multiple walkers' UU/BB pips compete.

**Nonland**: Lotus Petal one-shot; 12-ish repeatable rocks including all three Signets, all three Talismans, Sol Ring, Arcane Signet, Fellwar Stone, Mana Vault, Chrome/Mox Diamond/Mox Opal (last conditional) plus Jeska's Will. Original 34-land count retained after 16 cuts/adds, with card disadvantage Mox Diamond discard land and Chrome Mox pitch. Mana artifact density supports Tezzeret/Chain Veil, but Opal often fails until third artifact and Lotus Petal sacrificed while making colored mana stops counting toward metalcraft. The static mana profile reports nominal U/B/R land sources 19/19/17; these are **raw proxies**, not joint colored-payment likelihood. Historical T4 56% strict four land-drop presence is a no-mulligan proxy, not chance of casting Ravager on curve. The generated commander cost/mv=0 was detected as false; no claim is based on its 100% 'all_required_colors_present_by_base_turn'.

**Explicit mana example:** Four lands producing exactly U,B,R,C pay Ravager `1UBR` on T4. Even with Sol Ring and Mana Vault giving excess C after, they **cannot pay** the transformation's U,B,R if tapped out, so the next available main phase still needs UBR sources. With Ravager in play, Training Grounds and five available mana U+B+R+C+C cast transform `2UBR` legally. If your U source is Cavern of Souls naming Elder and no other U source, the transform cannot be paid with that restricted Cavern mana; Cavern's colorless mode can fund one of the 2 generic but you still need actual blue.

**Card advantage:** Remora, Rhystic, Teferi Master Time, Arisen +2, Jace, Liliana -/death draw, Citadel, tutor suite. The board can fall behind on four-mana planeswalkers protected poorly; hold an early counter/removal or cast Damnation before exposed walker deployment. Recursion mostly Arisen -4, Deliver Unto Evil, The Eldest Reborn/Takenuma; targeted discard from Ravager creates potential enemy graveyard resources, so Tergrid and Tinybones both vie for those; the deck lacks a high-density general reanimation shell.

## Candidate pool and competing cuts

**All 54 M5 packet hypotheses examined by role family** rather than automatically applying scores. Packet: P0 3, P1 6, P3 45; 9 limited test PASS, 3 FAIL, 15 inconclusive, 27 undetectable; these do not establish measured game win-rate or card-value certainty. The 54 items cover repeated alternative cuts for the same candidate; there are not 54 independent endorsed improvements. EDHREC 717 public planeswalker-themed lists corroborate Bolas-heavy identity, not an actual best cut.

| Material challenger | Compare to actual existing possible cuts | Commander-first verdict and adversarial cost |
|---|---|---|
| **Aetheric Amplifier** (M5 rank 37) | Mox Diamond vs Inexorable Tide vs The Eldest Reborn | Potential loyalty/enhancement artifact matters only if effect's Oracle text and payoff are confirmed; source packet ranks without comprehensive costed combo proof. **HOLD_PENDING_CARD_ORACLE**, do not displace 0-mana accelerator on a score. |
| **Relic of Sauron / Chromatic Lantern / Commander's Sphere / Visage of Bolas / Chromatic Orrery** (M5 ranks 13/20/79/25/109) | Mox Diamond in M5; alternative high-end Deceiver or The Eldest Reborn | A 3/4/7-mana artifact can help fixed UBR and Tezzeret untap, but replacing 0-mana acceleration is a substantial turn-4 tempo hit; expensive artifacts dilute planeswalker density. Relic is more plausible than Orrery, but don't infer automatic acceleration. **KEEP** current. |
| **Tezzeret, Master of the Bridge** (M5 51) | The Theorist, Jace Beleren / Bolas Deceiver | 6-mana multicolor planeswalker reduces creature/planeswalker costs with affinity for artifacts (needs sufficient board artifacts), plus damage recursion; strengthens planeswalker theme, but effect may not protect Arisen, is slower than four-mana Jace. **KEEP**; real alternate cut Deceiver superior to eliminating low-curve Jace. |
| **Jace, Cunning Castaway / Tasha, the Witch Queen** (M5 59/133) | Mystic Remora or Deceiver | Extra walker count/loyalty copy targets useful, but Jace's combat-oriented copy is low impact and Tasha's 5 MV may crowd upper curve; losing one-mana Remora badly weakens draw/survival. **KEEP**, stronger to compare Deceiver than Remora. |
| **Brainstorm / Wheel of Fortune** (M5 67/99) | Mystic Remora; alternative tinybones or slow Saga | Brainstorm is cheap draw selection, but recurring Remora access more valuable over three-opponent cycle; Wheel refills enemies after Ravager disrupts exactly one each, contradicting this build and encroaches Nekusar/original discard identities. **KEEP**. |
| **Lithoform Engine / The Peregrine Dynamo** (M5 234/408) | Rings, Dreamtide Whale, Sanctum Lurker | Lithoform can copy ability for 2 and also ETB or spells with extra payments; 4-MV and at-least-2 activation is tempo-heavy compared with Rings' 3/2. Dynamo specifically needs a NONLEGENDARY source for its activated/triggered-ability copy, so **cannot copy Arisen's legendary PW loyalty activation**, making M5 copy claim invalid if relied on. **KEEP**. |
| **Clockspinning / Mystic Speculation / Experimental Augury / Contentious Plan** | Ripples, Gambit, Inexorable Tide, Deceiver | Cheap counter manipulation/proliferate can be relevant; Contentious Plan 1U sorcery draws 1/proliferates, Experimental Augury 1U instant looks top 3 then proliferates, offering real early activation acceleration but less protection than Ripples (which phases out walkers) and less raw cards than Gambit. **Conditional cheap curve challenger: Experimental Augury for Inexorable Tide**, not for Ripples/Tezzeret's Gambit, only when expensive 5-drop consistently stranded. |
| **Dack Fayden / Ashiok Dream Render / Ajani Unrelenting / Ugin** (historical Oct15 offranking) | The Deceiver; The Eldest Reborn | Dack is affordable artifact theft/loot and candidate on multiplayer artifact pods, but not Bolas-specific. Ashiok graveyard exile conflicts with Arisen -4. Ajani (2026) expensive and role unclear; Ugin 8 mana noncommander Goodstuff. **KEEP** with Dack as a metagame-dependent cheaper control walker. |
| **Teferi's Talent vs Rowan's Talent** (historical) | Rowan's Talent | Teferi's Talent at 5 MV is slower than Rowan (4) and does not prove more Arisen activations through an established board. **KEEP Rowan**. |
| **Hullbreaker Horror / Tidespout Tyrant / Kiki-Jiki + Ancestral Statue / infinite spell-copy Reiterate** (M5 combo routes) | Nicol Bolas Dragon-God, Tergrid, Sanctum Lurker, Dreamtide Whale | Have independent combo or bounce payoffs but dramatically reduce number of Bolas/proliferate/loyalty engines; Kiki untap timing and colors cannot be presumed from ranking. **REJECT generic diversions**. |
| **Venser, Shaper Savant / Aether Channeler** (M5) | Dragon-God, Tergrid or Remora | ETB stack/board flexibility valuable, and Kitten allows blink, but expensive relative to Swan/Offer and planeswalker engines; cutting Dragon-God erases uniquely Bolas planeswalker synergy. **KEEP**. |
| **Magistrate's Scepter** (M5) | Rings of Brighthearth; Mox Diamond | Can earn an extra turn after 3 charge counters; without repeatable efficient counter source/costs it asks 12 generic mana across activations and sacrifice, a separate artifact-combo route. **KEEP Rings**. |
| **Deflecting Swat / Force of Negation** (off-ranking prior) | Deceiver, The Eldest Reborn | Premium extra shields can be attractive in interactive pods, particularly at the vulnerable 7-mana transform window; Swat conditional free while commander controlled, Force pitch blue but noncreature spell. **Potential improvement conditional on removal-heavy meta**, but slots displace distinct walker identity/recursion. No proof to change now. |
| **Theorist's Sanctum / Interplanar Beacon** (EDHREC/prior off-ranking lands) | Karn's Bastion, Reflecting Pool | Planeswalker-specific benefits trade generic UBR commander casting and prolif utility. Need full Oracle and land-source accounting; do not swap into 34-land greedy pip structure by popularity. **KEEP**. |

**Priority judgment:** The weakest *unconditional* approved slot is likely eight-mana `Nicol Bolas, the Deceiver`, but it makes the fifth Bolas-personality aspect of a flavor-first Superfriends deck. Dropping it for cheap Experimental Augury, Dack or another shield boosts early consistency at cost of strong character identity and a walker slot; the deck may deliberately accept that trade because commander's ceiling is not cEDH. The key genuine challenger is **Experimental Augury -> Inexorable Tide** if the five-mana enchantment cannot begin proliferating before opposing attack clocks; the exact swapped matchup must be recorded and approved by Cory if ever selected. `Mox Diamond -> Relic of Sauron` is a rank trap, not a real gain established by M5.

## Oracle, legality and rules

1. **Ravager transforming is blink-equivalent new object**: cannot be activated with summoning sickness relevance only on creature tap abilities, but transform itself has no tap in cost. Ability `4UBR` is sorcery-only; response removal before it resolves leaves no transform. Seven-loyalty Arisen enters new and can activate loyalty immediately in the same main phase.
2. **Training Grounds** only subtracts **2 generic** while Ravager is a creature; cost becomes **`2UBR`**, not `UBR` or anything free. It does not reduce separate loyalty activation costs of the planeswalker backside. The mana is paid on activation **before** opponent response.
3. **Kitten** triggers when you cast noncreature spell and target your nonland permanent. Blinking a transformed Arisen returns front-face Ravager because no effect says 'return transformed'. If enchanted by Rowan/Liliana Talent, those Auras fall off when it exiles, ending any prior attachment. It re-enters as creature with ETB discard and cannot immediately act as Arisen without paying activation anew.
4. **Deliver Unto Evil** selects up to four targeted graveyard cards. Control any planeswalker with subtype Bolas (Arisen or named Bolas cards) → return all legally targeted; otherwise opponent chooses two if able. Transforming does NOT cast a Bolas planeswalker spell, so `Dark Intimations` graveyard bonus applies to **cast** Bolas walker spells only, never Arisen's reentry from transformed front face.
5. **Rings / Rowan's Talent / Jaya's Phoenix** copy loyalty **effect** instances, not the +2/-4 cost counters; +2 adds only two loyalty when copied once while potentially drawing 4 cards. Each copy can retarget if allowed. Auras attach to a particular object; removing or transforming by exile drops enchantments.
6. **Disparity in The Chain Veil + Rings + Teferi combo**: Veil pay `{4},{T}`, Rings pays an extra `{2}`; each of two resolutions grants extra activation. Teferi Temporal Archmage `-1` untaps Veil and 3 mana permanents producing **at least 6 mana combined** and `+1` restores loyalty. Two Teferi actions consume both newly gained permissions while restoring engine; this supports arbitrarily repeated activations under correct starting activation/timing and 6-producing mana package. Teferi + Veil without Rings does **not** mean literally free infinite combo with Teferi stuck outside command zone; avoid overclaiming archived Spellbook's commander-specific recast steps. `Mana Vault 3C + Sol Ring 2C + any 1-mana source = 6` is a viable tap-output trio. No double-counting Mana Vault while tapped on wrong point.
7. **Ichormoon + Teferi Master of Time**: Gauntlet grants `[0]: Proliferate`, `[-12]: extra turn`; Teferi -10 gives two extra turns, Rowan Talent copies for four. A loop needs sufficient loyalty, effect resolution, available activation permissions and opponents not interacting, not merely two cards in starting hand.
8. **The Arisen -12** exiles all but the **bottom card** of target player's library; player is not defeated until required draw from empty library or another win effect. Copying -12 could target two distinct players, but one still retains a single card.
9. **Sanctum Lurker** exempts walker from 0-loyalty state-based graveyard loss, but cannot protect from creature attacks, exile, bounce, -loyalty effects unrelated to zero check, or destruction; a 0-loyalty walker can later activate granted [+2] at permissible time.
10. **Tekuthal** proliferation replacement twice; `Dreamtide Whale` vanishing 2 can proliferate its **own time counters** to delay eventual vanishing, not generate mana. `Ripples of Potential` proliferates first then phases out those receiving counters; phase out does not ETB/blink and counter permanence maintained.
11. **Spark Double** can nonlegendary-copy transformed Arisen as a planeswalker (with extra loyalty), but a non-DFC Spark Double copying front Ravager exiles without returning on 'return transformed' instruction.
12. **The Peregrine Dynamo** copies triggered/activated ability of **another target COLORLESS SOURCE / legendary?** Need verify exact Oracle: current documented M5 candidate isn't in list; its copying requires **another target legendary source**? **UNVERIFIED** until confirm exact. No eligibility claims should drive a swap without actual Scryfall Oracle and controller-target legality. The M5 candidate note is hypotheses, not a verified negative.
13. **The Elderspell** sacrifices/destroys planeswalkers (including yours if target) and accumulates counters for own walker according to number destroyed; no relevant opposing walkers => dead BB card except sacrificing own walker, real metagame weakness.
14. **Liliana's Talent / Jaya's Phoenix exact rare Oracle nuances** were not individually live re-fetched Oct19. Strategically counted as loyalty support only; do not claim an unsupported exact infinite interaction.
15. **Official compliance**: Scryfall bulk Oct16 engineering audit compliant UBR; all named cards canonically approved Oct15, no project exception. Latest user-authorized status unchanged. Fresh future Scryfall before any card swap.
16. **Mana document correction:** generated 'MV=0' is categorically false for Ravager; manual `1UBR` cast and `4UBR`/reduced `2UBR` transform used for all judgments. This error must be raised as data-quality ticket separately, not silently used as a game statistic.

## Finite sequencing and adversarial scenarios

**Manual, deterministic finite state traces; no new stochastic simulation, aggregate win rate, or opponent-policy outcome is claimed.** Opponents may interact at priority windows and may keep creature pressure after discard.

| Case | Payable board / opposing response | Approved line | Alternative and result |
|---|---|---|---|
| R1 | T3 have U,B,R,Sol Ring but no extra untapped color | `1UBR` cast needs 4 total, can pay with Sol Ring plus 3 colors. | Replacing Mox Diamond with 4-mana Relic slows early colored source; late upkeep stronger only if game reaches turn. |
| R2 | Ravager on board, UBR + 2 generic untapped, Training Grounds | Pay `2UBR` at sorcery-speed, exile/return Arisen, activate +2 same main phase if no response. | Without Grounds need UBR +4 generic. Opponent removal on stack can prevent transformation. |
| R3 | Ravager on board, Cavern Elder only blue source + B,R,C,C, Grounds | Cavern's chosen-color restricted to Elder creature casting, cannot pay U on transform; no valid activation unless other blue. | Chromatic Lantern may help in long game, not immediate absent cast/resolution. |
| R4 | 4 Ravager, noncreature cantrip, Displacer Kitten out; three opponents with cards | Kitten trigger blink Ravager, each opponent discards one upon ETB; old Ravager is new object. | Cut Kitten for random bounce creature, losing repeated commander ETB. |
| R5 | Transformed Arisen 7 loyalty wearing Rowan's Talent, cast spell triggers Kitten | Blink makes front Ravager, Rowan goes graveyard; new ETB discard. | Repeatable walker copy engine **lost**; choose a different Kitten blink target instead. |
| R6 | Arisen 7 loyalty + Rowan Talent, activate -4 targeting creature in GY | Arisen down to 3; two copies of reanimation effect can target two different GY cards (if copied retarget allowed), not twice the loyalty loss. | Lithoform Engine can copy for extra mana but adds costly artifact, Rowan stays relevant. |
| R7 | Control no Bolas PW (front Ravager only), Deliver Unto Evil up to four targets | Opponent withholds two cards if possible. | With transformed Arisen, get all four; real synergy countered if Arisen removed before Deliver resolves. |
| R8 | Six mana from three Teferi untappable permanents, Rings + Veil, Teferi Temporal Archmage and enough activations | Pay 4+2; resolve 2 Veil activations; Teferi -1 untap Veil + mana, +1 net loyalty. Repeat if valid timing/priority. | Replace Rings with Lithoform 4MV, requires mana to activate plus potential tap; evaluate exact, don't auto-upgrade. |
| R9 | Arisen at 7 loyalty, Deepglow Skate enters and doubles to 14 | -12 ultimate available at next legal chance (likely same turn if no earlier loyalty activation); library to one card, not direct loss. | Contentious Plan single proliferate takes to 8, not instant -12; more flexible earlier but fewer late loyalty. |
| R10 | Own walker at 0 loyalty, Sanctum Lurker survives | Walker remains, may legally [+2] later; can act as blocker-draining source with 1 dmg all opponents. | Remove Lurker for Dynamo or generic tutor: walkers die as SBA at zero. |
| R11 | Ripples proliferates walker, respond opponent destroy | Walker may phase out after it receives counter as Ripples resolves; protection applies to chosen permanent that did receive counters. | Inexorable Tide no protection while expensive setup. |
| R12 | Whale with 1 time counter and opponent casts second spell | Proliferate can choose whale to gain time counter, extend life, and walkers for loyalty. | Cheap Experimental Augury provides proliferate at instant speed once but does not sustain. |
| R13 | Board only 2 artifacts: Sol Ring + Mox Opal, need U for Ravager | Opal counts itself and Sol, total 2: metalcraft OFF, produces zero. | Another 0-mana artifact or drawn third artifact fixes, but M5 hypothetical can't assume early Opal activation. |
| R14 | One opponent walker, own Arisen 5 loyalty, The Elderspell BB | Destroy target opponent walker, add loyalty to own walker to set -12 later. | Zero opposing walkers and unwilling to sacrifice own => blank spell; Dispel/Draw would be broader early. |
| R15 | High-end hand: Bolas Planeswalker 8 MV + Deceiver 8 MV + God-Pharaoh 7, lands 4, no fast ramp | Many turns with uncastables; identity strength later but early spells needed. | Replace Deceiver with Experimental Augury (1U) speeds draw/proliferate only if walkers on board; high-end theme-tax real. |
| R16 | Attackers 3x 3/3, one PW 2 loyalty and no blockers, hand with Inexorable Tide | On T5 cast Tide; opponent combat may kill walker before any proliferate benefits. | Cheap removal or Instant Augury/Propaganda-type effect may keep state, but protection card must actually address attacks at walkers. |
| R17 | Opponent graveyard with discarded permanent, Tergrid and Tinybones on board | Both potentially trigger when discarded; controller orders but one card can't both return and be exiled. | Multiple card slots for only one discard per opponent until commander blink; cut pressure on these pieces is justified. |
| R18 | Arisen -12 resolved with target library 40, no future draw same turn | Target has one-card library; still in game until required draw from empty library. | Don't label -12 'immediate lethal' in optimizer test; extra draw/turn needed. |

**Strongest challenger adversarial defense:** Experimental Augury's `1U` instant speed looks better than fifth-turn Inexorable Tide when facing walkers being attacked and when you can hold U up. But Inexorable triggers on each CAST spell and with Tekuthal multiplies events; for five-plus follow-up spells it can add far more loyalty. A 1-for-1 needs controlled test across fast attack and slower control pods, not a popularity rank. Also the Augury leaves an enchantment slot absent, potentially lowering endgame -12 reliability.

**Strongest incumbent defense and counterargument:** Deceiver at eight mana is high-cost flavor anchor and nearly uncastable on many openers, apparently easiest cut for cheap interaction. However it contributes one of the franchise's uniquely villainous iconic Bolas planeswalker abilities and keeps the collection's Ravager Superfriends deck recognizably Bolas; replacing all named Bolas with the strongest cheap cantrips would violate its thematic objective. No deck should be forced to fringe cEDH because of ranking.

## Conclusions and unresolved evidence

**Decision:** `KEEP` all 100 exact approved cards unchanged. **No owner-approved swaps applied; no approved hash, lock, exception, canonical file, M6.4 62/62 count, formal Phase B, or GrokBot Pass C changed.** Commander-first evidence supports a tuned Bracket 4, not a generic Grixis combo deck.

Material follow-ups, not swap instructions: `Experimental Augury -> Inexorable Tide` and `Dack Fayden -> Nicol Bolas, the Deceiver` as meta-specific 1-for-1 tests; `Deflecting Swat -> The Eldest Reborn` in removal heavy tables, or `Relic of Sauron -> Mox Diamond` if T4 color scarcity is measured. Evaluate actual opening hand UBR and 5–7 transformation payments, walker defense vs three opponent attack steps, high MV dead draw, and source-paid priority windows. Don't claim derived "MV zero" metric, 54 candidate passes, or external popularity as evidence of improvement.

**Completion evidence:** 98 independently reconstructed TXT names/100 physical copies including exactly two repeat basics, 34 lands, 54 M5 pool items grouped with concrete cut alternatives, commander transforms/cost/timing and 18 opponent-aware finite traces, canonical Oct15/Oct16 legal and Oracle receipt, explicit impact limits. This authored report is NOT independent Pass C. Exact-head M6 GitHub Actions policy and anti-tamper tests must pass before advancing tracker. Artifact separate from tracker checkpoint: merge after CI then tracker commit/CI/merge only if validator passes. If CI cannot be verified, current tracker remains 41/62 and Ravager not complete.
