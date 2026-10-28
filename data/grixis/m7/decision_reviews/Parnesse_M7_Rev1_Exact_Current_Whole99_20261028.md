# Parnesse, the Subtle Brush (#46) — M8 whole-99 current-source commander-first decision

2026-10-28. **Author recommendation: KEEP exact owner-approved October 27 Rev1 100**. This is a new substantive whole-deck role challenge on the already-approved bytes, not a new M7 replacement proposal or milestone seal.

- Current physical 100: `data/grixis/m7/candidate_lists/Parnesse_the_Subtle_Brush_M7_Rev1_Approved_2026-10-27.txt`, exact SHA-256 `63b605a2c36ec81ab7a5a48770ac2b96b7994daf38546aba7b6bc6bd7597928c`. Commander first, 99 library copies, 96 distinct names, 35 lands; basic Island x2, Mountain x3, Swamp x2; color identity U/B/R, no project exceptions. Owner's approved canonical path is `refinement/decklists/Parnesse_the_Subtle_Brush_M7_Rev1_2026-10-27.txt`; no change to either source or approval.
- Previous Oct15 full-99 author audit: `refinement/verification/Parnesse_the_Subtle_Brush_Whole_List_Audit_2026-10-15.md` (99/99, before seven replacements); Oct27 approved seven-swap record `refinement/approvals/Parnesse_the_Subtle_Brush_M7_Rev1_Approved_2026-10-27.md`; exact-list Oracle/legality source-composite check `refinement/verification/Parnesse_the_Subtle_Brush_M7_Rev1_Oracle_Certification_2026-10-27.md`. It was **not** a fresh successful 100-card Scryfall collection response; do not relabel it as one.
- M6 original five P0 executed against this SHA in engineering [PR #747](https://github.com/corymstover/GrokBotMTGCompanion/pull/747). Five specific P1 K5/K6/K7/E1/F3 bounded cases executed under exact current SHA in [PR #756](https://github.com/corymstover/GrokBotMTGCompanion/pull/756), [CI #40658115383 success](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40658115383); original W3 was retired because Replication Technique is absent. **The other five original P1 cases remain deferred**, and no old M6 I/J or independent third-model verdict is fabricated.

## Commander-first core and 99-copy ledger

Parnesse `{2}{U}{B}{R}` taxes opponents' spells/abilities *targeting us or our permanents* by **four life** or countering, and whenever **we copy a spell**, we **may** let one targeted opponent make their own copy (new targets permitted). Opponents' copies are their own; they do not re-trigger *our* Parnesse. Spells copied in exile and then cast are different from copying a spell on the stack. The goal is real copy-value/optional gifts, blue-red spell-payoff density and paid storm/magecraft finishers, not a generic noncommander turbo combo shell or forced benefits to opponents. Card classification below accounts for **all 99 current physical noncommander copies** exactly once; a dedicated SHA-bound test independently verifies the quantities and names.

### 35 lands — KEEP (U/B/R five-mana commander plus expensive copy engines)

- 1x Arid Mesa
- 1x Badlands
- 1x Blood Crypt
- 1x Bloodstained Mire
- 1x City of Brass
- 1x Command Tower
- 1x Exotic Orchard
- 1x Flooded Strand
- 2x Island
- 1x Luxury Suite
- 1x Mana Confluence
- 1x Marsh Flats
- 1x Misty Rainforest
- 1x Morphic Pool
- 3x Mountain
- 1x Otawara, Soaring City
- 1x Polluted Delta
- 1x Reflecting Pool
- 1x Scalding Tarn
- 1x Shivan Reef
- 1x Steam Vents
- 1x Sulfurous Springs
- 1x Sunken Palace
- 2x Swamp
- 1x Training Center
- 1x Underground Sea
- 1x Urborg, Tomb of Yawgmoth
- 1x Verdant Catacombs
- 1x Volcanic Island
- 1x Watery Grave
- 1x Xander's Lounge

Eight fetch lands search **typed** duals/shocks/basic lands (not utility spells); two life-paying any-color lands and Reflecting Pool mitigate painful U/B/R source constraints, while Sunken Palace can supply on-theme late spell-copy utility at its actual mana cost. No blanket source-is-always-untapped claim: shock lands, Xander's Lounge and other specific lands may enter tapped, and the pain lands tax life. **35 lands are retained** because Parnesse costs five, Double Vision costs five, Thousand-Year Storm costs six and copies are often additional mana payments; shaving lands for one more narrow copier worsens source-paid reliability.

### 15 mana/access accelerants or reducers — KEEP

- 1x Arcane Signet
- 1x Big Score
- 1x Fellwar Stone
- 1x Frantic Search
- 1x Goblin Electromancer
- 1x Izzet Signet
- 1x Jeska's Will
- 1x Mana Geyser
- 1x Nightscape Familiar
- 1x Rakdos Signet
- 1x Sol Ring
- 1x Storm-Kiln Artist
- 1x Talisman of Creativity
- 1x Talisman of Dominance
- 1x Talisman of Indulgence

Big Score's discarded card makes its two Treasures/draw-two **not free**; Frantic Search untaps up to three lands only when actually resolved; Storm-Kiln Artist rewards real instant/sorcery cast **or copied** events with Treasures and can support Mica's artifact-sacrifice demand. Familiar/Electromancer reduce only the appropriate spell costs, not every payment; Jeska's Will red mana depends on chosen opponent hand size, Mana Geyser on opponents' **tapped lands**. They are conditional ritual ceilings, not unconditional loops. The original Dark Ritual would supply one-time BBB but doesn't by itself fund the U/R commander pips or repeated copy spells; the chosen longer-game slot is not a risk-free speed upgrade.

### 25 substantive direct-copy/copy-permission engines — KEEP

- 1x Alania, Divergent Storm
- 1x Bonus Round
- 1x Chef's Kiss
- 1x Display of Power
- 1x Double Vision
- 1x Dualcaster Mage
- 1x Errant, Street Artist
- 1x Galvanic Iteration
- 1x Increasing Vengeance
- 1x Loki Laufeyson
- 1x Mica, Reader of Ruins
- 1x Narset's Reversal
- 1x Primal Amulet // Primal Wellspring
- 1x Prismari, the Inspiration
- 1x Reiterate
- 1x Return the Favor
- 1x Reverberate
- 1x Spinerock Tyrant
- 1x Storm King's Thunder
- 1x Tempt with Mayhem
- 1x Thousand-Year Storm
- 1x Thunderclap Drake
- 1x Twinning Staff
- 1x Wandering Archaic // Explore the Vastlands
- 1x Zevlor, Elturel Exile

This is intentionally high **real-copy** density. Bonus Round is symmetric and opponents also copy *their own* spells; it cannot be scored as unilateral protection. Tempt/Alania/Wandering Archaic trade opponent resources or decisions for copies and are politics, not automatic always-favorable copies. Reiterate's `{4}{R}{R}` buyback repetition is *mana-positive only when the copied live ritual actually yields at least seven red and RR/initial six mana can be paid*; a generated six is mana-neutral, five is a resource loss. Other one-shot copiers—Reverberate, Return the Favor, Increasing Vengeance—are **not** automatically infinite merely because mana rituals exist. Mica sacrifices a real artifact; Big Score/Storm-Kiln Treasures help but are not guaranteed. Spinerock Tyrant copies only applicable **single-target** spells; Loki's delayed spell-copy is restricted by mana value/power; Prismari, Zevlor, Wandering Archaic and their permitted copies depend on specific activation/target/payment facts. Double Vision/Thousand-Year Storm are expensive and vulnerable to removal; increasing their density is weaker than getting them onto a stable board with colored mana and protection. Kess and Mizzix's Mastery belong in spell-recovery group below because **casting** a copied card isn't by itself Parnesse's copy-spell trigger. The removed Replication Technique/Dualcaster token loop is no longer in the physical 100 and must not inflate win-line counts.

### 8 Parnesse trigger multipliers or cast/copy payoff finishers — KEEP

- 1x Archmage Emeritus
- 1x Grapeshot
- 1x Harmonic Prodigy
- 1x Professor Onyx
- 1x Ral, Storm Conduit
- 1x Tendrils of Agony
- 1x Veyran, Voice of Duality
- 1x Wizard's Staff

Archmage/Magecraft/Ral/Onyx/Storm-Kiln convert **actual cast/copy events**, while Tendrils and Grapeshot create storm copies that **are not cast** and do not themselves increment storm count. Parnesse receives an optional politics trigger for each copy **we control**. Staff equipped to Parnesse plus Harmonic and Veyran yields **four** Parnesse triggers for a copied instant/sorcery (native + three additive increases), **not eight**; Veyran does not amplify a non-instant/sorcery copy. All gifted spell copies remain optional and can backfire if offered indiscriminately. The seven-swap Tendrils addition provides a real black storm life-drain finish absent from the prior Witch token package, but only when sufficient actual storm exists and the spell/copies resolve.

### 8 conditional answers and protection cards — KEEP

- 1x Blasphemous Act
- 1x Chaos Warp
- 1x Deflecting Swat
- 1x Feed the Swarm
- 1x Fierce Guardianship
- 1x Flusterstorm
- 1x Hexing Squelcher
- 1x Mana Drain

This coverage favors protecting an engine and stopping interaction: Fierce/Swat free modes need commander control, Flusterstorm copies only target instant/sorcery spells and opponents can pay its taxes, Hexing Squelcher's protection is bounded, Feed/Chaos handle resolved enchantment/nonland permanents and Blasphemous Act handles creatures. Swapping unconditional Counterspell for Fierce loses some creature-spell counter coverage; swapping An Offer You Can't Refuse for Flusterstorm loses coverage against non-instant/sorcery noncreature stack spells but avoids the opponent's two Treasures and can counter multiple actual spells. Those tradeoffs are substantial, not ignored. Eight answers are a deliberately lean optimized build: pressure from creature-heavy or enchantment-heavy pods remains matchup-dependent.

### 8 card-selection, tutor, recursion and spell-recast support — KEEP

- 1x Brainstorm
- 1x Demonic Tutor
- 1x Kess, Dissident Mage
- 1x Mizzix's Mastery
- 1x Ponder
- 1x Preordain
- 1x Rhystic Study
- 1x Windfall

These turn mana and copied turns into future spells. Kess casts a graveyard instant/sorcery on our own turn only once and obeys replacement exile; Mizzix's Mastery copies *cards* then casts copies, not an automatic Parnesse trigger at the copy-a-card step. Windfall is symmetrical and can supply opponents cards; tutoring and filtering cost time/spells rather than solving every game. Cutting one for a thirtieth copier loses consistency or actual draws, especially with five-to-seven-mana engines.

## Post-seven-swap opportunity audit and physically complete alternatives

The exact seven swaps already approved are Cormela→Mica, Pyromancer's Goggles→Spinerock Tyrant, Sedgemoor Witch→Tendrils of Agony, Replication Technique→Storm King's Thunder, Counterspell→Fierce Guardianship, An Offer You Can't Refuse→Flusterstorm, Dark Ritual→Loki Laufeyson. Explicitly accepted losses: Cormela death recursion, Goggles fixing, Witch defense, Dualcaster-Replication Technique loop, two broad counters and black one-shot speed. The gains are more repeatable direct spell copies, a direct storm kill, no symmetry-giving Treasure on protection, and higher copy payoff for Parnesse. A material risk is that eliminating several colored/resource cards for engines makes the source/mana protection decisions more critical, not mechanically guaranteed better in every pod.

| Fully specified legal **100-card** alternative to the exact seven-swap approved deck | Strongest argument | Counterargument and decision |
|---|---|---|
| Add **Twincast**; cut **Display of Power** | `{U}{U}` is earlier/cost-cheaper to copy one spell | Display can copy multiple eligible spells from a real contested stack and cannot itself be copied; losing flexibility/multi-copy leverage for another narrow copier is not enough. **REJECT**. |
| Add **Teach by Example** and **Chandra, Hope's Beacon**; cut **Galvanic Iteration** and **Double Vision** | Two cheaper/sometimes repeatable copy supports with planeswalker utility and flash-style sequencing | Galvanic can flashback for a later copy; replacing a stable five-mana enchantment with an even more expensive vulnerable six-mana walker weakens an already high curve. **REJECT**. |
| Add **Counterspell** and **Dark Ritual** back; cut **Flusterstorm** and **Loki Laufeyson** | Reclaims early unconditional stack counter and black burst to deploy a five-mana commander | More rigid UU and one-shot BBB with no guaranteed U/R pip conversion; loses low-U stack-storm copies and delayed on-theme spell duplication. Real metagame alternative, not demonstrated general improvement. **REJECT**, monitor actual failures. |
| Add **See Double**; cut **Mica, Reader of Ruins** | Broad response copy without sacrificing artifacts | Four-mana one-shot spell loses repeatable source-supported copy engine, while Mica has actual Treasury feed from Storm-Kiln/Big Score. **REJECT** unless those artifacts consistently fail to materialize in real games. |

Additional incumbent positions independently challenged after seven selections: **Mica**, **Double Vision**, **Display of Power**, **Galvanic Iteration**, **Bonus Round**, **Kess**, **Windfall**, **Fellwar Stone**, **Sunken Palace** and **Blasphemous Act**. Relevant off-ranking alternatives already considered in the preceding October 15 candidate research include Twincast, Teach by Example, Twinferno, See Double, Chandra Hope's Beacon, Radiant Performer and generic tutor/Oracle packages. EDHREC Oct15 commander-specific inclusion/relevant synergy was used to discover candidates but not to certify their strength; no new High Lift metric or fresh 2026 live page is fabricated here. Shortlisted new seven-replacement cards have an explicit October 27 source-composite Oracle check; remaining uncertainties are counted as uncertainty, not as a mechanical all-card API success.

**Quality stop criterion:** Current commander text + 35-land/64-spell real copy economy + all 99 physical noncommanders individually assigned; every approved cut's lost role assessed; current weak slots, specific alternate cuts and two distinct multi-card 100-card portfolios challenged; core copy/cast, target, symmetry, mana and payoff boundaries adversarially reviewed. The approved seven-swap configuration better preserves Parnesse's political-copy density, defensive mana, tutor access and storm finishing opportunities than the above alternatives. No genuinely material new card swap is supported by the current evidence. This is an authored local-best conclusion, **not** an independent measured win-rate claim, literal complete game-engine test, completion of five remaining P1 cases, new owner approval or global M8 acceptance. **KEEP EXACT CURRENT 100**.
