# M6 Comprehensive Single-Deck Review #44 — Obeka, Brute Chronologist

**Author** ChatGPT, NOT independent GrokBot Pass C. **Tracker key** `Obeka__Brute_Chronologist` index 43, deck #44 of 62. **Date** 2026-10-20. **Authored decision** HOLD original approved 100 unchanged; challenger(s) recorded only, no applied swaps.

## Source and test receipts

Live engineering repository `corymstover/GrokBotMTGCompanion`, integration `chatgpt-cycle76-m6-refinement`: read `AGENTS.md`, `grixis/M6 Commander-First Single-Deck Review Standard.md`, `data/grixis/m6/single_deck_depth_tracker.json` (43/62 done at review initiation), `data/grixis/registry.json`, `data/grixis/milestone_m6_m7_subtracker.json`; read Obeka's `grixis/interactions/obeka-brute-chronologist.md` (2026-10-16 Oracle/CR cases), `data/grixis/mana_base/obeka-brute-chronologist.json`, and `data/grixis/m6/review_packets/obeka-brute-chronologist.json`. Canonical source `corymstover/grixis-commander-encyclopediaGPT/main`, `state/current_deck_overrides.json#decks.Obeka__Brute_Chronologist`; [approved 100-card TXT](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/decklists/Obeka_Brute_Chronologist_Approved_2026-10-15.txt) (Git blob `af530761f649e2b40f1baecdbabb08d726fce1ae`), [approval and Oct15 verification](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/verification/Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md), historical [candidate decisions](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/decisions/Obeka_Brute_Chronologist_Candidate_Decisions_2026-10-15.md).

**Authority binding:** APPROVED/LOCKED 2026-10-15, exact raw approved SHA-256 `31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8`; engineering logical `lh1:958f40565c66c18bf18f1451bac9e933497046c04dc54e58811bfac18d794e66`. No identity discrepancy, no project exceptions, UBR official Commander compliance per 2026-10-16 Scryfall Oracle bulk + canonical Oct15 check. **Independent canonical TXT recount**: 100 physical cards, 100 names, 34 lands, 99 library cards, zero repeated names (including basics). This is the approved list, NOT historical 34-land FINAL pre-approval baseline; 19 historical swaps already owner-approved. No claimed new all-100 live legality/Oracle API sweep.

**Outside Oracle correction:** Wizards' [Sep 2, 2022 Oracle changes](https://magic.wizards.com/en/news/announcements/oracle-changes-2022-09-02) explicitly states that **Delina, Wild Mage's token exile is NOT a delayed triggered ability**; the token instead has a **normal triggered ability** reading "At end of combat, exile this creature." Therefore a token whose one end-of-combat trigger is exiled with Obeka will trigger **again at a future end of combat**, unlike Sneak Attack/Feldon/Hate Mirage one-shot delayed triggers. This **material discovery contradicts shallow claims that Delina tokens become permanently safe after one Obeka end turn**. Source [Footsteps of the Goryo Oracle](https://mtg.wtf/card/plst/SOK-68/Footsteps-of-the-Goryo): {2}{B} sorcery returns creature from YOUR GY and sacrifices at beginning of **next end step**, no haste; its delayed trigger, once stacked then exiled, does not return.

**M5 pool accounting:** 181 generated pairwise candidate/cut hypotheses from 10 batches; P0=1, P1=24, P3=156; effect-limited labels: 25 pass, 22 fail, 92 inconclusive, 42 no-difference. Many entries vary only cut among Dualcaster Mage, Reanimate, Cyclonic Rift, Glorious End, Discontinuity, Mystic Remora, Jaxis, Purphoros, Fellwar, or Toxic Deluge. They do NOT equal 181 independent, tested superior swaps; no effect-aware real four-player competitive win rate is evidenced. Historical whole-list audit reviewed all 99 noncommander slots; this report independently audits approved source rows and alternate cuts, not just a highest-ranked candidate.

## Commander identity and natural ceiling

Obeka, Brute Chronologist costs {1}{U}{B}{R} and is a 3/4 legendary Ogre Wizard. `{T}: The player whose turn it is may end the turn.` Thus current active player **may decline** if it is their turn; it is on OWN turn that Obeka's controller can compel the intended outcome by choosing to end. Ending a turn exiles everything currently on stack and proceeds to cleanup; "until end of turn" durations still expire. One-shot `beginning of the next end step` delayed triggers must be put **on the stack first**, then removed by Obeka; ending turn before they trigger shifts the liability to the next end step. These are mandatory timing semantics, not flavor.

Game plan: low-cost RR extra-turn spells with lose-game liability (Final Fortune, Last Chance, Warrior's Oath, un-cleaved Alchemist's Gambit); temporary creature/clone/sneak/reanimation effects whose next-end-step sacrifice/exile/return triggers Obeka can erase; use haste, Thousand-Year Elixir, Minamo and Sundial/Discontinuity to ensure action. Scepter imprinted with Final Fortune plus Obeka provides repeatable extra-turn engine if mana/tap and interaction constraints met. Distinct from Obeka, Splitter of Seconds (upkeep multiplication). Natural ceiling **Bracket 4 — Optimized**: commander-specific setup, mana/haste cost, vulnerable trigger windows and some fast compact wins; cannot label unstoppable turbo-cEDH. Protect commander's agency; do not supplant with generic Oracle/Consult or unrelated huge mana loops.

## Full 100-card role audit

Individual physical-row audit, in exact approved TXT order, one row per singleton.

| Row | Exact approved card | Concrete role and strategic liability |
|---:|---|---|
| 1 | Obeka, Brute Chronologist | COMMANDER — {1}{U}{B}{R}, tap: ACTIVE PLAYER MAY end the turn; must survive/tap on own triggered end step |
| 2 | Alchemist's Gambit | Risky extra turn; penalty tied to that extra turn, not a generic next-end-step token trigger; cleave removes penalty at higher cost. |
| 3 | Ancient Tomb | Land — CC with two life cost, funds generic commander but not UBR or RR turn spells. |
| 4 | Animate Dead | Cheap ongoing Aura recursion; Obeka does not negate losing creature when Aura leaves. |
| 5 | Apprentice Necromancer | Tap/sacrifice reanimates creature; one-shot next-end-step sacrifice can be erased; requires tap access and valid graveyard target. |
| 6 | Arcane Signet | Two-mana all-UBR fixing; enables Obeka's three specific pips. |
| 7 | Arena of Glory | Land — Red mana; specialty creature-spell haste that makes Obeka's tap live immediately, requires exact mana mode. |
| 8 | Arid Mesa | Land — Fetchland for typed dual/shock/triome, costs life and thins typed fixing; correct land type matters. |
| 9 | Avaricious Dragon | Extra draw but intrinsic discard of hand every own end step; recurring trigger every turn, not a one-shot delayed drawback. |
| 10 | Badlands | Land — Untapped/fetchable dual or shock color fixing (shock may require two life); funds UBR activation. |
| 11 | Blood Crypt | Land — Untapped/fetchable dual or shock color fixing (shock may require two life); funds UBR activation. |
| 12 | Bloodstained Mire | Land — Fetchland for typed dual/shock/triome, costs life and thins typed fixing; correct land type matters. |
| 13 | Bojuka Bog | Land — Enters tapped, utility GY exile or three-color typed fixing/cycling, early tempo cost. |
| 14 | Chaos Warp | Broad emergency removal; red instant can reveal dangerous replacement. |
| 15 | Chrome Mox | Zero-mana colored ramp needs imprint of nonartifact nonland hand card; card disadvantage. |
| 16 | City of Brass | Land — Any-color untapped fixing with life expense. |
| 17 | Come Back Wrong | Removal/theft; next-end-step sacrifice delayed trigger is directly Obeka-clearable. |
| 18 | Command Tower | Land — Untapped unconditional UBR fixing. |
| 19 | Counterspell | UU protection; colored demand competes with Obeka. |
| 20 | Cyclonic Rift | Flexible bounce, 7-mana overloaded defensive reset; not end-turn synergy but protects fragile engine. |
| 21 | Deflecting Swat | Conditional free red target redirection with commander present; cannot defeat untargeted effects. |
| 22 | Delina, Wild Mage | Attack produces token with REGULAR granted end-of-combat exile trigger, recurring at every later end of combat; not a permanently savable one-shot delay. |
| 23 | Demonic Tutor | Tutors Scepter/Final Fortune/haste/protection; not identity payoff alone. |
| 24 | Discontinuity | Noncommander end-turn backup; cheaper during own turn; protects from a missed Obeka end step. |
| 25 | Dualcaster Mage | Flash spell-copy protection and Twinflame token engine; important independent backup win, not a gratuitous cut. |
| 26 | Fable of the Mirror-Breaker // Reflection of Kiki-Jiki | Treasures/loot then creature copier; clone has a one-shot next-end-step sacrifice; Obeka makes token last. |
| 27 | Feldon of the Third Path | Tap-based graveyard token copy with haste and delayed next-end-step sacrifice; commander native. |
| 28 | Fellwar Stone | Two-mana rock, opponents must provide desired colored land abilities; useful but not unconditional UBR. |
| 29 | Fierce Guardianship | Noncreature counter, conditional zero mana while commander controlled; shields liability stack. |
| 30 | Final Fortune | RR instant extra turn with that extra turn's end-step lose trigger; Scepter imprint (MV2) central. |
| 31 | Flameshadow Conjuring | Extra R on nontoken ETB for haste token copy, one-shot next-end-step exile; direct Obeka conversion. |
| 32 | Flooded Strand | Land — Fetchland for typed dual/shock/triome, costs life and thins typed fixing; correct land type matters. |
| 33 | Force of Will | Pitch-blue protection or costly full counter; saves Obeka/turn-ending setup. |
| 34 | Frantic Search | Instant draw-discard and three-land untap; fuels reanimation and colored mana sequencing. |
| 35 | Gamble | R tutor with random discard; costly failure if key piece dropped without recursion. |
| 36 | Glorious End | End the turn on resolution but creates its own future lose-game trigger; backup with exposure. |
| 37 | Hate Mirage | Copies up to two opposing creature targets with haste; next-end-step exile trigger is clearable; opponent board dependence. |
| 38 | Hellkite Courser | Six-mana ETB puts own Obeka from command zone onto field with haste without casting/tax; end-step return trigger clearable. |
| 39 | Ideas Unbound | UU draw three now, NEXT end-step discard three one-shot delayed trigger; Obeka saves cards after it triggers. |
| 40 | Identity Thief | Attacker exiles nontoken creature, copies it only until cleanup; delayed return trigger can be removed after stack placement. |
| 41 | Ilharg, the Raze-Boar | Five-mana creature cheat on attack; next-end-step return-to-hand trigger is Obeka-clearable. |
| 42 | Island | Land — Basic colored source, supports necessary UBR pip and resilience against nonbasic hate. |
| 43 | Isochron Scepter | Imprints MV2-or-less instant such as Final Fortune; {2},tap casts copy for repeatable extra turns with Obeka. |
| 44 | Izzet Signet | Two-mana UR filtering with one generic input, fixing rather than free acceleration. |
| 45 | Jaxis, the Troublemaker | Hasty token copier paying discard and tap; one-time end-step sacrifice erased by Obeka. |
| 46 | Jeska's Will | Three-mana red burst/card access conditional on controlling commander; timing risk. |
| 47 | Kiki-Jiki, Mirror Breaker | Hasty tap copied nonlegend creature, red triple-pip cost; next-end-step sacrifice one-shot. |
| 48 | Last Chance | RR sorcery extra turn with specific-turn end-step lose trigger, Obeka protective. |
| 49 | Lightning Greaves | Zero equip haste/shroud protection; removes targeting option for owner's targeted auras later. |
| 50 | Lotus Petal | Zero-color single-shot mana, not sustained fixing. |
| 51 | Luxury Suite | Land — Conditionally untapped multiplayer dual, vital paired UBR pips. |
| 52 | Mana Confluence | Land — Any-color untapped fixing with life expense. |
| 53 | Mana Drain | UU hard counter producing colorless next main phase; no guaranteed colored UBR boost. |
| 54 | Mana Vault | One-mana colorless triple burst with untap expense; doesn't pay Obeka's fixed pips. |
| 55 | Marsh Flats | Land — Fetchland for typed dual/shock/triome, costs life and thins typed fixing; correct land type matters. |
| 56 | Minamo, School at Water's Edge | Land — Blue source and legendary-permanent untap for Obeka; does not remove summoning sickness. |
| 57 | Misty Rainforest | Land — Fetchland for typed dual/shock/triome, costs life and thins typed fixing; correct land type matters. |
| 58 | Morphic Pool | Land — Conditionally untapped multiplayer dual, vital paired UBR pips. |
| 59 | Mountain | Land — Basic colored source, supports necessary UBR pip and resilience against nonbasic hate. |
| 60 | Mystic Remora | One-mana opponent noncreature tax draw engine, cumulative upkeep; critical early card flow. |
| 61 | Mystical Tutor | U top-deck instant/sorcery tutor, finds extra turn/end turn/protection. |
| 62 | Necromancy | Aura reanimator; flash-mode timed sacrifice can be erased, but Aura removal still loses reanimated creature. |
| 63 | Otawara, Soaring City | Land — Untapped mono-colored source or channeled interaction/recursion at land-card opportunity cost. |
| 64 | Polluted Delta | Land — Fetchland for typed dual/shock/triome, costs life and thins typed fixing; correct land type matters. |
| 65 | Psychic Vortex | Draws more over turns with cumulative upkeep and hand discard each own end step; both recurring burdens. |
| 66 | Puppeteer Clique | Opponent-GY creature theft with end-step exile once; Obeka can retain; persist offers replay. |
| 67 | Purphoros, Bronze-Blooded | High-cost haste plus red creature cheating, timed sacrifice next end step; noncommander identity support. |
| 68 | Reanimate | B permanent fast reanimation with life payment; less Obeka-specific but uniquely efficient. |
| 69 | Reflecting Pool | Land — Only produces colors other lands could produce, conditional early. |
| 70 | Rhystic Study | Three-mana ongoing card tax; adds shields, not a delayed trigger. |
| 71 | Rionya, Fire Dancer | Attack copies another creature based on instants/sorceries cast, one-shot next-end-step exile; strong token scale. |
| 72 | Saheeli, the Sun's Brilliance | Two-mana legendary artifact/creature temporary copier with next-end-step sacrifice; Obeka-ready but tap requirement. |
| 73 | Scalding Tarn | Land — Fetchland for typed dual/shock/triome, costs life and thins typed fixing; correct land type matters. |
| 74 | Shivan Reef | Land — Untapped color-pair painland, costs life on colored activation. |
| 75 | Sneak Attack | R hand-to-battlefield haste creature from enchantment, one-shot next-end-step sacrifice; major Obeka synergy. |
| 76 | Sol Ring | One->CC repeated, cannot alone pay UBR or RR. |
| 77 | Steam Vents | Land — Untapped/fetchable dual or shock color fixing (shock may require two life); funds UBR activation. |
| 78 | Sulfurous Springs | Land — Untapped color-pair painland, costs life on colored activation. |
| 79 | Sundial of the Infinite | End-own-turn activated artifact backup; must be your turn and untapped/payable. |
| 80 | Swamp | Land — Basic colored source, supports necessary UBR pip and resilience against nonbasic hate. |
| 81 | Swiftfoot Boots | Haste and hexproof for Obeka at equip cost; essential activation reliability. |
| 82 | Takenuma, Abandoned Mire | Land — Untapped mono-colored source or channeled interaction/recursion at land-card opportunity cost. |
| 83 | Talisman of Creativity | Untapped UR/C rock, life cost for colored; helps activation. |
| 84 | Talisman of Dominance | Untapped UB/C rock, life cost for colored; helps activation. |
| 85 | Talisman of Indulgence | Untapped BR/C rock, life cost for colored; helps RR extra turns. |
| 86 | Thousand-Year Elixir | Creatures tap as though hasty and untap target creature for {1},tap; does not confer haste for attacking. |
| 87 | Toxic Deluge | Three-mana -X/-X board clear, life cost can kill own commander. |
| 88 | Training Center | Land — Conditionally untapped multiplayer dual, vital paired UBR pips. |
| 89 | Twinflame | Red short-duration clone spell with next-end-step exile, Dualcaster copying can create unbounded hasty tokens if untouched. |
| 90 | Underground Sea | Land — Untapped/fetchable dual or shock color fixing (shock may require two life); funds UBR activation. |
| 91 | Underworld Breach | Graveyard escape-value engine, exiles three other GY cards per escape; distinct from Obeka's central plan. |
| 92 | Vampiric Tutor | B topdeck any card, 2 life cost, protection/engine access. |
| 93 | Venser, Fervent Forger | Six-mana flash modal copies of opponent spells or temporary permanent copies with one-shot timed sacrifice. |
| 94 | Verdant Catacombs | Land — Fetchland for typed dual/shock/triome, costs life and thins typed fixing; correct land type matters. |
| 95 | Volcanic Island | Land — Untapped/fetchable dual or shock color fixing (shock may require two life); funds UBR activation. |
| 96 | Warrior's Oath | RR sorcery extra turn; lose-trigger on that turn's end step, Obeka can erase. |
| 97 | Watery Grave | Land — Untapped/fetchable dual or shock color fixing (shock may require two life); funds UBR activation. |
| 98 | Windfall | Three-mana all-player discard/draw; refill and reanimation fodder but grants opponents answers. |
| 99 | Wooded Foothills | Land — Fetchland for typed dual/shock/triome, costs life and thins typed fixing; correct land type matters. |
| 100 | Xander's Lounge | Land — Enters tapped, utility GY exile or three-color typed fixing/cycling, early tempo cost. |

**Engine density:** temporary/token copies (Reflection, Feldon, Flameshadow, Jaxis, Kiki, Saheeli, Rionya, Twinflame, Hate Mirage, Venser, Delina), reanimation/theft (Animate Dead, Apprentice, Necromancy, Reanimate, Clique, Come Back Wrong), sneak/cheat (Hellkite Courser, Sneak Attack, Purphoros, Ilharg); RR risky turns/Scepter; commander tap infrastructure (Boots, Greaves, Thousand-Year Elixir, Arena of Glory, Minamo). Every category has incumbent opportunities: excess expensive top end and repeating self-discard vs needed card access; extra turn speed vs conditional commander protection; Delina's NORMAL recurring trigger is non-permanent payoff and timing conflict. The deck does not have deterministic access to Obeka merely because it draws 34 lands.

## Candidate pool and competing cuts

| Actual candidate vs current cut | Positive case | Adversarial counter-case / disposition |
|---|---|---|
| **Footsteps of the Goryo IN / Delina, Wild Mage OUT** | {2}{B} one-shot reanimation of any creature from own GY, turns temporary next-end-step sacrifice into lasting creature with Obeka. Replaces a four-mana attack/d20 copier whose granted exile trigger occurs at **EVERY future end of combat**, so Obeka cannot make Delina tokens last permanently by clearing it once. This is the **strongest strategic upgrade proposal** after source verification, distinct from earlier weak-slot Avaricious Dragon suggestion. | Footsteps requires supplied GY target and does **not grant haste**; Delina can generate immediate attacking token ETBs/combat and sometimes multiple high-roll copies. This list has limited giant creature payoff density and already four reanimation slots; may have low early Footsteps hit rate. Recommend **owner consideration**, NOT apply; need actual creature target/attacker matchup testing and detailed opponent response. |
| **Footsteps IN / Avaricious Dragon OUT** | Four-mana Dragon gives cards at cost of recurring end-step discard; Footsteps enables one-shot lasting reanimation with Obeka. | Reduces proactive ongoing draw and still doesn't fix Delina recurring-exile rule trap; second-best alternate cut if Dragon underperforms. HOLD for matchup evidence. |
| **Goryo's Vengeance / Apprentice Necromancer** | B1 instant grants haste and next-end-step exile for a target legendary creature, which Obeka can cancel. | Only legend targets, compared to Necromancer ANY creature, may lose broad coverage. No proof of upgrade. |
| **Mulldrifter / Mystic Remora** (M5 rank 3) | Immediate two cards, evoked at 2U or main creature 5; some graveyard recursion. | Removing Remora sacrifices uniquely potent one-mana three-opponent draw taxation for slow body. Reject exact swap. |
| **Rakdos Signet / Fellwar Stone** | More guaranteed BR colors than opposing-land-dependent Fellwar Stone. | Costs a generic input to activate; slower immediate mana. Meta-dependent only. |
| **Lotus Field / Arid Mesa** | Rainbow triple mana land with hexproof and untap synergy. | Enters tapped and sacrifices two lands; disastrous in early 34-land commander/haste curve. Reject. |
| **Auton Soldier / Terror of the Peaks / Zealous Conscripts / Godo / Duelcaster Mage** (many M5 routes) | Copy/ETB threats can exploit temporary cheats or provide extra-combat wins. | Replacing Dualcaster breaks efficient Twinflame combo and stack-copy control; most are 5–6 MV, may require survival/attack. Test only against redundant pricey copier rather than core Twinflame piece. |
| **Molten Duplication / Heat Shimmer / Electroduplicate / Irenicus's Vile Duplication / Hate Mirage** | A cloned creature with a one-shot next-end-step exile/sacrifice can be retained via Obeka; some clones have better own-creature targeting than opponent-dependent Hate Mirage. | Need exact Oracle, color/mana, timing, targeted copies and available payoff. Certain replacement clones lack end-step liability and thus offer no commander lift. Candidate swap to Hate Mirage conditionally plausible, not forced. |
| **Generic extra turns (Nexus of Fate, Time Warp) / Scepter, Discontinuity** | Low drawback, no Obeka dependence. | Seven/five mana and generic win condition weaken Obeka's RR risky-turn signature, already owner decided. Reject. |
| **Dramatic Reversal / Discontinuity or Glorious End** | Untap artifacts and Obeka in an Isochron shell. | Without positive nonland mana, not a self-sustaining loop; losing unconditional stack exiling increases risk of Final Fortune self-loss. Reject exact swaps. |
| **Worldgorger Dragon+Animate Dead, Power Artifact+Grim, Intruder Alarm, Hullbreaker Horror** | Independently explosive with correct pieces/mana. | Commander may be irrelevant; Worldgorger loop has exile/target risks and insufficient guaranteed win exit; colored pips remain. Do not homogenize. |
| **The Master, Multiplied / Delina or Purphoros** | Turns off own token sacrifice/exile and renders token strategy independent of a ready Obeka; particularly addresses Delina NORMAL recurrent exile ability. | Removing mandatory commander end-turn involvement is a real identity loss; if deck wants a redundant protection line, conditional, no evidence broad enough. |
| **Time Stop / Sundial or Glorious End** | True other-player end-turn capability without Obeka vote; six-mana spell. | Worse than existing one-mana Sundial and cheaper own-turn Discontinuity; don't replace. |
| **Brainstorm, Wheel of Fortune / Jaxis, Mystic Remora** | Improves selection/hand size. | Generic draw needs to outperform recurring draw and one-shot token engines; wheel refills opponent hands and can lose combo shields. HOLD. |

**Weak-slot analysis:** `Delina` is most clearly **rules-discounted** in approved list; `Avaricious Dragon` and `Psychic Vortex` put recurring self-discard triggers on each own end step and risk hand/protection, and `Venser` is six-mana interactive payoff. `Hate Mirage` is high utility only when opposing creatures worth cloning. `Ilharg` and `Purphoros` are setup-heavy yet directly Obeka-synergistic. Good protection `Counterspell`, `Force`, `Fierce`, `Deflecting Swat` shouldn't be replaced with expensive dragons on score. Highest scoring model swap != best identity strategy.

## Oracle, legality and rules

1. Obeka's active-player choice: opponent can decline own turn; a ready Obeka on your own end step can clean triggers while you choose yes.
2. Ending turn exiles STACK, skips directly to cleanup; duration `until end of turn` still ends in cleanup. End-turn effect does not prevent sacrifice that's a COST or an ability already RESOLVED.
3. Delayed `at beginning of next end step`: skipping before it triggers merely shifts it to a later end step; stack it then end the turn and it is gone permanently (for that instance). This is why timing identical across Sneak Attack, Kiki, Hellkite Courser, Come Back Wrong and Footsteps.
4. Delina's generated tokens **have** a regular triggered "At end of combat, exile this creature" ability, not a one-shot delayed trigger. It triggers at each later combat end until token disappears, including opponents' turns; Obeka-cleared single iteration doesn't permanently retain those tokens. [Official Sep 2022 oracle correction](https://magic.wizards.com/en/news/announcements/oracle-changes-2022-09-02).
5. Dualcaster/Twinflame: cast Twinflame with legal own creature target, flash Dualcaster in response, copy Twinflame selecting Dualcaster, new hasty Dualcaster token repeats ETB copy; interruptible loop yields arbitrarily many temporary tokens; their one-shot delayed exile can be cleared at own end step, though attacking/lethal damage may have other blockers and priority windows. Requires spell on stack and correct retarget.
6. Scepter + Final Fortune: Final Fortune MV2 imprinted, {2},tap Scepter copies casts it for repeatable extra turns; on EXTRA turn's end step its lose-game trigger is stacked then Obeka tapped to end. Must leave Obeka available EACH extra turn and pay 2/tap Scepter EACH cycle; artifact/creature counterplay remains. Final Fortune's trigger refers to that turn, so an early end of specifically that turn can avoid it, unlike "next end step" generic token liability.
7. Glorious End ends turn immediately on resolution, creates delayed future loss if unmanaged; it alone cannot indefinitely dodge own loss. Discontinuity is cheaper on your own turn, regular standalone ability.
8. Avaricious Dragon / Psychic Vortex ongoing printed `at beginning of YOUR end step` abilities aren't one-shot delayed triggers: each subsequent own end step generates a fresh trigger. Obeka must answer repeatedly, costs activation and saves no upkeep.
9. Delina vs other copiers: Delina's trigger may be caught at end of combat (not next end step), requiring end turn before postcombat main. Fable's cloned token / Hate Mirage copies have delayed NEXT end-step liability which can be permanently erased.
10. Identity Thief attacks, exiles creature, gains copy **until end of turn**; next-end-step delayed return can be exiled on stack, original remains exiled even when copy wears off at cleanup.
11. Hellkite Courser commander enters directly from zone without CAST and with haste; does not add command-zone tax, and Obeka can erase delayed end-step return if active player agrees.
12. Thousand-Year Elixir enables tap ability as though haste without actually granting combat haste; Minamo can untap Obeka but doesn't solve summoning sickness. Lightning Greaves grants shroud and can complicate allied targeting.
13. Necromancy Aura removal still causes reanimated creature to be lost despite timing trick; Obeka only deletes a temporary delayed sacrifice stack object, not a durable Aura attachment rule.
14. Footsteps {2}{B} **does not give haste**, reanimates target creature from own GY, next-end-step sacrifice one-shot; opponent can kill Obeka or creature before trigger and reduce lift. Different from instant Goryo's Vengeance (1B, legend-only, gives haste).
15. Ideas Unbound UU draw3 and delayed next-end-step discard3, Obeka clears after it triggers; ending main phase prematurely transfers trigger to next player's end step.
16. Venser, Fervent Forger's temporary copied permanents are genuine next-end-step sacrificial copies that can remain if Obeka clears delayed triggers. But six mana, opponent permanent quality and counterspell vulnerability mean it isn't automatic value.
17. `Puppeteer Clique` steals opposing graveyard creature and triggers exile at next end step; persist ETB recurrences can value, but controlling opponent GY cards matters.
18. RR extra turns and {1}UBR Obeka cast require actual red/UB mana, not Ancient Tomb/Mana Vault CC; raw resource >=4 isn't sufficient without UBR. Source static mana report correctly values Obeka MV4, unlike DFC false-MV bug observed in prior deck reviews.
19. 34 lands/100 unique, UBR Commander legality official Oct15/16 source snapshot with NO authorized exceptions. Outside add Footsteps Oracle legal Commander as documented. New Scryfall full 100 check required if owner explicitly approves any swap.
20. Risky turn stack example: opponent removes Obeka before end-step lose trigger on stack; any free Fierce Guardianship still requires commander controlled to be free, or may need actual 2U; Sundial can save own turn if untapped and paid.
21. Ending an opponent's turn with Sundial isn't possible (own turn only); activating Obeka on their turn gives THEM choice and is not reliable protection for their combo.

## Finite sequencing and adversarial scenarios

Manual deterministic tests with actual paid mana, timing and active-player decisions. **Not** a newly executed stochastic simulator or win-rate measurement.

| Case | State and opponent counterplay | Valid result |
|---|---|---|
| O1 mana | Have Obeka, sources U, B, C, C (no R) | Cannot cast Obeka despite 4 mana; conditional Rakdos Signet could fix later with input. |
| O2 haste | Obeka entered this turn without haste/Elixir | Can't tap for end-step protection; Minamo untap alone doesn't waive summoning sickness. |
| O3 ready | Obeka has Swiftfoot/Greaves and on own end step Hate Mirage sacrifice/exile is STACKED | Tap Obeka, choose yes, exile triggered ability, copied creature remains. |
| O4 premature | End own main phase after Hate Mirage token but before next-end-step trigger | Trigger waits and fires at opponent's next end step; Obeka on their turn isn't reliable. |
| O5 vote | Activate Obeka during opponent turn over their lethal spell | Active opponent may decline, spell will still resolve if nothing else intervenes. |
| O6 Delina | Token created in combat, at end of combat token's own exile ability triggers | Obeka clears one instance; token triggers again next end of combat. No permanent Delina token engine. |
| O7 Delina with next-end liabilities | Obeka tapped end-of-combat to rescue Delina this turn | Cannot also clear Fable/Hate Mirage next-end-step liability unless Obeka untapped/reset; mixed engines conflict. |
| O8 Footsteps | Obeka already able to tap, valid reanimation target in graveyard, spend 2B on Footsteps on own main | Creature returns WITHOUT haste; next own end-step sacrifice stacked and Obeka exiles it; permanent after cleanup, if not removed. |
| O9 counter | Obeka removed in response to its already activated tap ability | Ability generally still resolves; if removed before activation, cannot activate; Stifle can counter ability. |
| O10 risky | Final Fortune RR grants extra turn, Obeka untapped at its end step | When losing trigger on stack, Obeka choose end, survives; without Obeka/Sundial/backup may lose. |
| O11 repeat | Scepter (Final Fortune imprinted) plus untapped Obeka and 2 generic source on each own turn | Activate Scepter, extra turn, clear specific-turn loss; untap Scepter and Obeka on extra turn, repeat; opposing removal breaks. |
| O12 Twinflame | Own creature, 1R cast Twinflame targeting it; 1RR flash Dualcaster in response | Copy Twinflame for Dualcaster, create token whose ETB copies again, potentially many hasty Dualcasters; opponent counterspell interrupts. |
| O13 Hellkite | Hellkite Courser ETB puts Obeka in from zone with haste | No cast/tax added; Obeka can clear return trigger on own end step and stay. |
| O14 Dragon | Avaricious Dragon gained draw but triggered hand discard at own end step | Obeka clears one occurrence; triggers again next own end step, including when commander tapped or unavailable. |
| O15 Vortex | Psychic Vortex's upkeep cost grows each turn and end-step discard keeps returning | Obeka can't erase cumulative upkeep or future recurring end-step costs; high attrition risk. |
| O16 Identity | Identity Thief attacks, exiles opposing nontoken creature, becomes copy until EOT | End turn after delayed return trigger on stack, original remains exiled; thief stops copying at cleanup. |
| O17 reanimate aura | Necromancy reanimates creature, Obeka erases temporary trigger, opponent destroys Necromancy | Creature leaves from Aura lifecycle; Obeka never made that ongoing attachment permanent. |
| O18 Ilharg | Attack and put creature from hand tapped attacking, return next-end-step delayed trigger on stack | Obeka ending at that point keeps creature beyond turn instead of returning to hand. |
| O19 two colors | Three lands produce U,B,R; Sol Ring generic CC available | Obeka costs one generic + UBR and can be cast, but counterspell UU may be unavailable afterward, protect sequencing. |
| O20 extra turn tax | With Scepter paying 2 per extra turn, opponent destroys artifact before next activation | Infinite-turn route stalls, extra-turn schedule finite; cannot claim unconditional victory. |
| O21 Phantom generic combo | Replace Twinflame with unrelated creature and add Power Artifact+Grim | Can make colorless if assembled but no UBR guaranteed; turns away from Obeka with slot loss. |
| O22 other end turn | Sundial in play, opponent's combat active | Sundial ability prohibited (only your turn); Obeka activation gives that opponent a choice, not guaranteed defense. |

## Conclusions and unresolved evidence

**Authored decision:** HOLD **approved 100** exactly, **strongest potential improvement for OWNER CONSIDERATION** = **Footsteps of the Goryo IN / Delina, Wild Mage OUT**, as Delina's recurring NORMAL triggered exile prevents permanent saves and conflicts with the rest of next-end-step architecture. **This is NOT an applied swap** and gains depend on creature graveyard availability, no haste from Footsteps, and opponents' interaction. Secondary Avaricious Dragon or Psychic Vortex as alternate cuts to improve live protection reliability remain unproven. No pointless generic cEDH homogenization.

**Risks pending additional evidence:** actual graveyard creature hit rate for Footsteps, target creature ETBs versus Delina immediate attacking copies, percent of turns 4–6 with Obeka haste/untap/UBR, multi-engine end-combat versus end-step scheduling, board wipe/defense, real controlled multi-opponent games. Earlier October15 approved review overlooked Delina's recurrent-trigger difference and needs annotation here, **not** a canonical reopen or previous deck alteration.

**Verification boundary:** approved TXT independently 100 cards, 100 names, 34 lands, 99 library slots, UBR official Oct15/16 source snapshot PASS, project exception none; 181 M5 machine hypotheses triaged by role/cut, 22 payable opponent-aware deterministic traces, WotC official Oracle ruling, alternative-cost and priority reasoning. No fresh 2026-10-20 full Scryfall bulk pass or empirical matchwin testing. No owner approval changed; historical original 62/62 narrow M6.4 and canonical locks untouched, no GrokBot Pass C or Phase B/M6 final claim. Exact-head CI on THIS artifact and sequential tracker checkpoint required before count changes.
