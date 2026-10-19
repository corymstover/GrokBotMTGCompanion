# Abaddon the Despoiler — comprehensive commander-first authored deep review

**Authored:** 2026-10-19, ChatGPT primary engineering reviewer (NOT independent Pass C)  
**Tracker ID:** `Abaddon_the_Despoiler` (0 of 61); no companion, one commander.  
**Canonical authority:** `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json`. APPROVED / LOCKED.  
**EXACT APPROVED RAW SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`.  
**Canonical approved file:** `refinement/decklists/Abaddon_the_Despoiler_Approved_2026-10-13.txt` (Git blob `1bbead6e8a7973bd7eb1982147e917d39e217492`).  
**Engineering source logical hash:** `lh1:5a1e5e5bb86ba35d7dbf712fbc3a7d29c3e05a17569c05e8a11976321699b793`; logical hash is not a replacement for approved raw file SHA.  
**Review posture:** evidence-only; all proposed adds/cuts are UNAPPLIED; no approval, locks, exceptions, raw hashes or decklists changed.  
**Review finding:** materially overlooked **Neheb, the Eternal + Aggravated Assault** line, with **Loyal Subordinate** as an on-identity combat-step life-loss outlet. Current recommendation is a **proposal for owner consideration**, not an applied swap.  
**Sources:** canonical deck export + October 16 fresh 100-card gate, original full 60-candidate ledger, M5 98-item packet, historical narrow Cycle131 author review, 2026-09-25 Comprehensive Rules, current Commander banned list checked October 19, 2026, direct rules/card references below.

## Commander identity and natural ceiling

Abaddon the Despoiler is a 5/5 trampler costing {2}{U}{B}{R}; **during your turn**, hand-cast spells with mana value ≤ total life all opponents have lost **that turn** have cascade. The threshold is **not** individual damage dealt, hand cost paid, damage to permanents or life loss from prior turns. Abaddon must be on the battlefield when a qualifying hand spell is cast. Nonhand casts caused by cascade do not automatically receive Abaddon's cascade. Printed cascades can coexist with Abaddon's granted cascade and trigger independently.

Protected identity: **cheap early opponent loss → increasing same-turn cascade threshold → hand-cast cascade → free exile casts → more damage, card/mana advantage and repeatable payoffs.** Non-negotiable engine includes Boltwave, Flame Rift, Loyal Subordinate, Thermo-Alchemist, Kessig Flamebreather, Solphim, Bloodletter, printed cascade spells, Wild-Magic Sorcerer, Prosper, Nalfeshnee, Keeper of Secrets and Passionate Archaeologist. Breach/LED/Brain Freeze is an important *secondary* compact finish but must not become the exclusive identity. The commander does not merely lend colors to turbo-Grixis.

Natural ceiling: **optimized/Bracket 4 provisional**; free interaction and a potent Breach package supply high spike potential, but a five-MV commander plus requirement to produce opponent life loss **before** casting the hand spell limits default cEDH-level consistency. Do not change the bracket on an unmeasured proxy score.

## Full 100-card role audit

Independent parsing of the actual approved source and 94 Oracle audit rows: **100 total cards = 1 commander + 99 library**, **94 distinct names**, only Island ×3, Mountain ×3 and Swamp ×3 repeat; singleton **PASS**. Exactly 34 lands, 19 source-tagged ramp, 11 tagged draw, six tutors, nine tagged removal, four counters and one labeled protection. These **single-source tags underestimate overlap** and **19 ramp does not mean 19 unconditional turn-two sources**. No Abaddon project-exception card.

**Mana sources:** 34 land slots, with nine basics (3 U / 3 R / 3 B); seven on-color fetches (Bloodstained, Flooded, Marsh, Misty, Polluted, Scalding, Verdant); six fetchable shocks/ABUR duals (Badlands, Underground Sea, Volcanic Island, Blood Crypt, Steam Vents, Watery Grave); three multiplayer duals (Luxury Suite, Morphic Pool, Training Center); rainbow/tri group (City of Brass, Command Tower, Exotic Orchard, Mana Confluence, Xander's Lounge); Otawara, Takenuma, Urborg; and Ancient Tomb. Xander's Lounge always enters tapped, shocks pay life or enter tapped, Exotic Orchard depends on opponents and Ancient Tomb/Mana Vault don't supply colored pips. Urborg helps black but not nonblack pips. The seven fetches have multiple dual/basic targets but exact turn-five U+B+R access was **not** measured with a color-aware source simulator. **Do not treat the raw 34/19 summary as a proved commander-cast rate.**

**Mana development:** Arcane Signet, Sol Ring, Talismans, Chrome Mox, Mana Vault, Lotus Petal, Dark Ritual, Cabal Ritual, Rite of Flame, Jeska's Will provide very different burst/sustainable mana; LED discards the whole hand and is mainly a Breach combo card; Nightscape Familiar reduces U/R spells only; Neheb needs a postcombat main and *that turn's* opponent life loss; Rakdos discounts creature spells only after an opponent lost life; Birgi adds R per actual spell cast (not copies); Vivi makes mana once per your turn; Storm-Kiln generates Treasures from instant/sorcery casts *and copies*. Some tagged ramp pays no mana until later setup.

**Tempo, cascade quality, curve:** Commander costs five; multiple MV 5–6 payoffs and **Call Forth the Tempest at MV 11** create expensive draws. Blasphemous Act has **MV 9 even when reduced to R**, valuable as a high-threshold cast but not a cheap-MV cascade trigger. Suspend-only cards (Ancestral Vision, Profane Tutor, Inevitable Betrayal) are **MV 0** and premium cascade hits but cannot normally be hand-cast. Zero/one-MV counterspells (Pact, Swan Song, Flusterstorm) can be ineffective cascade hits with no opposing target. Cascade does not guarantee the next target or improve counterspell availability. These are *real* opportunity costs of early interaction but not proof those interaction slots should be cut.

**Interaction gap:** Good stack control against blue/noncreature spells: Force of Will, Force of Negation, Pact, Fierce Guardianship, Flusterstorm, Swan Song, Pyroblast, Deflecting Swat. Creature control: Deadly Rollick, Bituminous Blast, Blasphemous Act, Delayed Blast Fireball, Noise Marine and damage lines. **Resolved nonblue artifacts/enchantments** are notably harder to remove: Otawara offers only temporary bounce; counterspells require preventing them first. Chaos Warp or Rakdos Charm merit targeted reassessment versus the strongest engine slots rather than automatically cutting Pyroblast. A restrictive Rule of Law effect / Rest in Peace is genuinely threatening.

**Card access and recursion:** Remora, Rhystic, Wheel/Windfall, Brainstorm/Ponder, suspend-zero cascade hits and nonhand payoffs provide abundant access. Demonic/Imperial/Vampiric/Mystical/Gamble/Profane tutors serve Breach or Abaddon routes but must not all be counted as literal card draw. Underworld Breach and Exalted Flamer provide uneven recursion; Harnfel and Ruinous Powers play from exile, and Prosper rewards this with Treasure. Losing Remora meaningfully harms pre-Abaddon card volume in blue-heavy pods.

**Damage and converting value:** Boltwave at one red gives 3 loss per opponent, **X=9** if three opponents all lose 3. Flame Rift gives 4 damage to each player, **X=12** from opponents in a three-opponent game; your own four damage does not count in X. Thermo-Alchemist repeatedly pings; Solphim doubles **controlled noncombat damage**, whereas Bloodletter doubles **opponent life loss** (including Loyal Subordinate's non-damage drain). Casting from exile triggers Keeper of Secrets and, if Abaddon remains controlled with Passionate Archaeologist, the granted commander trigger. The Lost and the Damned converts nonhand casts into 3/3s but is an expensive setup card.

**Protection/failure cases:** Countering/stealing Abaddon before hand casting turns off its static grant; spot removal of pingers before threshold can stop the chain; graveyard hate stops Breach; Rule of Law and Drannith Magistrate can strand cascade hits; hostile permanents that already resolved may be difficult to remove; free counters do not guarantee all combats/combos are protected. No multiplayer resilience win rate was measured.

### Complete card-by-card audit (every approved distinct name)

This matrix is an independent functional review of the **entire approved quantity map**, with the source audit's role tag and an authored retain/challenge note for each of the 94 distinct names, totaling 100 cards. 'Keep' is a role judgment **for this review**, not a reapproval or declaration of local optimum.

| Approved card | Qty | Source tag | Audited role, dependency or weakest-slot question |
|---|---:|---|---|
| Abaddon the Despoiler | 1 | Commander{top} | Hold: source-audited role, no individually demonstrated replacement. |
| Ancestral Vision | 1 | Draw | Keep: zero-MV free-draw cascade target; unusable as normal hand cast, suspend costs time. |
| Ancient Tomb | 1 | Land | Keep: early colorless acceleration; cannot itself supply U/B/R and costs life. |
| Arcane Signet | 1 | Ramp | Keep: reliable tri-color fixer for turn-five Abaddon. |
| Badlands | 1 | Land | Keep: fetchable B/R dual, red+black early threshold engines. |
| Birgi, God of Storytelling // Harnfel, Horn of Bounty | 1 | Ramp | KEEP CORE: cast-trigger red mana/Harnfel discard-to-exile two; alternate faces never together. Ignus loop candidate. |
| Bituminous Blast | 1 | Removal | Keep: printed cascade plus instant-speed creature damage; noncreature permanents remain weakness. |
| Blasphemous Act | 1 | Removal | Keep: efficient creature reset; printed mana value NINE even if cast for {R}. |
| Blood Crypt | 1 | Land | Keep: fetchable B/R dual; listed TRK future reprint is not new card legality. |
| Bloodletter of Aclazotz | 1 | Drain | Keep: doubles opponents' life LOSS, including Loyal Subordinate; restrictive BBB casting. |
| Bloodstained Mire | 1 | Land | Keep: fetches typed Grixis duals. |
| Boltwave | 1 | Burn | CORE: {R}, 3 each opponent => threshold 9 at three-player table (assuming all lose life). |
| Brain Freeze | 1 | Mill | KEEP COMBO: storm and Breach fuel/finisher; storm copies are not cast. |
| Brainstorm | 1 | Draw | Keep: early selection and Abaddon-trigger cascade hit. |
| Cabal Ritual | 1 | Ramp | Keep: one-shot black burst; threshold condition needs seven grave cards. |
| Call Forth the Tempest | 1 | Removal | IDENTITY KEEP: eleven-MV double printed cascade; expensive and high variance. |
| Chrome Mox | 1 | Ramp | Keep: colored early mana at real hand-card imprint cost. |
| City of Brass | 1 | Land | Keep: 3-color rainbow, self-damage is not opponent life loss. |
| Command Tower | 1 | Land | Keep: color fixing. |
| Dark Ritual | 1 | Ramp | Keep: accelerates black cards, doesn't alone cast tri-color Abaddon. |
| Deadly Rollick | 1 | Removal | Keep: free conditional spot exile with commander; protection vs creature threats. |
| Deflecting Swat | 1 | Protection | Keep: free conditional protection; cannot redirect every spell. |
| Delayed Blast Fireball | 1 | Removal | KEEP: high exile-cast sweep/damage, hand-cast mode lower damage. |
| Demonic Tutor | 1 | Tutor | Keep: unrestricted paid tutor, improves finding coherent engines. |
| Exalted Flamer of Tzeentch | 1 | Recursion | KEEP: instant/sorcery recursion at random; spell-cast opponent pings. |
| Exotic Orchard | 1 | Land | Keep: multiplayer conditional rainbow, source depends on opponents. |
| Fierce Guardianship | 1 | Removal | Keep: commander-dependent interaction; may be awkward cascade hit. |
| Flame Rift | 1 | Burn | CORE: 4 damage each player => opponent loss 12 in three-player scenario; hurts you too. |
| Flooded Strand | 1 | Land | Keep: fetch typed blue Grixis duals. |
| Flusterstorm | 1 | Counters | Keep: efficient stack fight, generally not productive mid-turn cascade hit. |
| Force of Negation | 1 | Counters | Keep: stack defense; free exile cost specifically opponents' turns, cascade cast still normal legality. |
| Force of Will | 1 | Counters | Keep: free stack protection by exiling a blue card and life; poor unopposed cascade hit. |
| Gamble | 1 | Tutor | Keep: cheap tutor with discard variance, can load graveyard for Breach. |
| Imperial Seal | 1 | Tutor | Keep: top-deck tutor at sorcery speed, does not draw directly. |
| Inevitable Betrayal | 1 | Theft | Keep: MV0 cascade theft target or slow suspend; not normal hand-cast. |
| Island | 3 | Land | Keep x3: basic untapped blue, fetchable. |
| Jeska's Will | 1 | Ramp | KEEP: commander conditional red mana/exile, supports hand-to-exile velocity. |
| Keeper of Secrets | 1 | Burn | Keep: nonhand cast damage payoff, six MV and creature removal exposure. |
| Kessig Flamebreather | 1 | Burn | KEEP: low-curve noncreature pinger fuels Abaddon on spell chains. |
| Lion's Eye Diamond | 1 | Ramp | KEEP COMBO: Breach loop; sacrifices and discards entire hand for three mana. |
| Lotus Petal | 1 | Ramp | Keep: early free one-shot any-color mana; critical early commander source. |
| Loyal Subordinate | 1 | Pingers | KEEP CORE: 3 each opponent at every combat when commander remains controlled; Neheb/Assault outlet. |
| Luxury Suite | 1 | Land | Keep: multiplayer typically untapped B/R source. |
| Mana Confluence | 1 | Land | Keep: any color at personal life cost. |
| Mana Vault | 1 | Ramp | Keep: colorless 3 burst, upkeep debt; not fixing. |
| Marsh Flats | 1 | Land | Keep: fetch typed black Grixis duals. |
| Mind's Desire | 1 | Draw | Keep pending qualified test: 6-MV storm plus possible Abaddon-granted cascade, 2 U pips. |
| Misty Rainforest | 1 | Land | Keep: fetch typed blue Grixis duals. |
| Morphic Pool | 1 | Land | Keep: multiplayer typically untapped U/B source. |
| Mountain | 3 | Land | Keep x3: basic red for thresholds and red mana intensive finishes. |
| Mystic Remora | 1 | Draw | KEEP: 1-MV early card draw and interaction fuel; poor Assault cut. |
| Mystical Tutor | 1 | Tutor | Keep: puts instant/sorcery atop library, pairs with cheap drawing/cascade sequencing. |
| Nalfeshnee | 1 | Copy | IDENTITY KEEP: non-hand spells are copied; permanent spell-copy enters as token. |
| Neheb, the Eternal | 1 | Ramp | KEEP CORE: each postcombat MAIN adds R for cumulative opponent life lost that turn; establishes Assault loop. |
| Nightscape Familiar | 1 | Ramp | Keep: reductions for U/R spells; regeneration cost nontrivial. |
| Noise Marine | 1 | Removal | KEEP: printed cascade and ETB damage scaled by spells cast in turn. |
| Otawara, Soaring City | 1 | Land | Keep: untapped U land or discard-channel bounce on limited permanent types. |
| Pact of Negation | 1 | Counters | Keep: zero-mana stack protection with next-upkeep mana debt; blank when cascade hits without valid spell target. |
| Passionate Archaeologist | 1 | Burn | IDENTITY KEEP: Abaddon gains triggered damage upon exile-cast spells; not independent global burn. |
| Polluted Delta | 1 | Land | Keep: fetch typed blue/black Grixis duals. |
| Ponder | 1 | Draw | Keep: topdeck smoothing, cascade setup. |
| Profane Tutor | 1 | Tutor | KEEP: MV0 cascade-to-tutor or suspend; cannot normally hand-cast. |
| Prosper, Tome-Bound | 1 | Draw | IDENTITY KEEP: exile-impulse supply and Treasure on exile cast. |
| Pyroblast | 1 | Removal | KEEP: cheap blue-counter/permanent answer, not generic permanent removal. |
| Rakdos, Lord of Riots | 1 | Ramp | CHALLENGED CUT: demanding BBRR creature-only cost reduction competes with spell/exile emphasis. |
| Rhystic Study | 1 | Draw | Keep: high-volume opposing-turn card advantage; tax pressure at optimized tables. |
| Rite of Flame | 1 | Ramp | Keep: cheap ritual; helps early red and cast count. |
| Scalding Tarn | 1 | Land | Keep: fetch typed red/blue Grixis duals. |
| Sol Ring | 1 | Ramp | Keep: core colorless acceleration. |
| Solphim, Mayhem Dominus | 1 | Burn | KEEP CORE: doubles controlled noncombat damage, not effects that directly say 'loses life'. |
| Steam Vents | 1 | Land | Keep: fetchable U/R dual, potential future printing code independent from card legality. |
| Storm-Kiln Artist | 1 | Ramp | KEEP: instant/sorcery cast OR copy generates Treasure, including storm copies. |
| Swamp | 3 | Land | Keep x3: basic untapped black, fetchable. |
| Swan Song | 1 | Removal | Keep: cheap blue stack answer with opponent creature drawback. |
| Takenuma, Abandoned Mire | 1 | Land | Keep: untapped black or channel recursion and self-mill. |
| Talisman of Creativity | 1 | Ramp | Keep: early U/R access at self-damage cost. |
| Talisman of Dominance | 1 | Ramp | Keep: early U/B access at self-damage cost. |
| Talisman of Indulgence | 1 | Ramp | Keep: early B/R access at self-damage cost. |
| The Lost and the Damned | 1 | Tokens | CONDITIONAL KEEP: repeated 3/3 token production from nonhand casts; five-mana setup payoff. |
| The Ruinous Powers | 1 | Draw | CONDITIONAL KEEP: random opponent-card theft from upkeep; casting card causes OWNER life loss; five-ish mana setup. |
| Thermo-Alchemist | 1 | Pingers | KEEP CORE: tap pings all opponents, untaps on instant/sorcery casts (not spell copies). |
| Training Center | 1 | Land | Keep: multiplayer typically untapped U/R source. |
| Underground Sea | 1 | Land | Keep: fetchable U/B dual. |
| Underworld Breach | 1 | Recursion | KEEP COMBO: escape requires card fuel and mana; graveyard answer vulnerability. |
| Urborg, Tomb of Yawgmoth | 1 | Land | Keep: all lands gain Swamp type, supports heavy black requirements. |
| Vampiric Tutor | 1 | Tutor | Keep: instant-speed unrestricted topdeck tutor at personal life cost. |
| Verdant Catacombs | 1 | Land | Keep: fetch typed black Grixis duals. |
| Vivi Ornitier | 1 | Ramp | KEEP: once-per-turn {0} mana from power and noncreature-spell all-opponent damage. |
| Volcanic Island | 1 | Land | Keep: fetchable U/R dual. |
| Watery Grave | 1 | Land | Keep: fetchable U/B dual, potential future printing code independent from card legality. |
| Wheel of Fortune | 1 | Draw | KEEP: seven-card hand refill, feeds Breach graveyard and storm; opponent benefit. |
| Wild-Magic Sorcerer | 1 | Draw | IDENTITY KEEP: first exile-cast spell of turn gains cascade; not every exile cast. |
| Windfall | 1 | Draw | Keep: hand refill and graveyard fuel; opponent hand-size dependent. |
| Xander's Lounge | 1 | Land | Keep: fetchable U/B/R tri-land but enters tapped. |

## Candidate pool and competing cuts

**Pool actually examined:** all **98 M5 Abaddon single-swap review-packet rows** (mixed objective-specific projections, many repeated candidate names and suspect cuts) and the prior **60 Abaddon individual candidate decisions**, including the commander-centric cards Aurora Phoenix, Deny Reality, Poxwalkers, Descent into Avernus, Spear Spewer, Blood for the Blood God!, Chaos Warp, Grinning Ignus, Past in Flames, Stormfist Crusader and others. These 158 *records* do not represent 158 independently playable and distinct upgrades. The M5 'pass' often counts a Spellbook combo proxy while not modeling actual combat, cast sequencing, creature abilities, opponent interaction or casting costs. The benchmark that suggests e.g. **Chromatic Lantern > Lotus Petal** or **Temple of the False God > Flooded Strand** relies strongly on popularity/proxy and is not a valid reason to mutilate the fast Grixis mana base.

| Candidate | Authentic advantage | Named candidate cut(s) and cost | Authored decision |
|---|---|---|---|
| **Aggravated Assault {2}{R}** | **NEW key discovery:** Neheb's repeated postcombat mana converts ≥5 prior opponent life loss into another combat and postcombat main. Existing Loyal Subordinate + controlled Abaddon can deal 3 to each opponent EVERY additional combat with no attacks; Bloodletter can amplify direct life loss. An Assault hand-cast with threshold ≥3 itself gains Abaddon's cascade. | **Preferred cut: Rakdos, Lord of Riots** — loses flying/trampling Demon and discount on hand-cast creatures, but Rakdos needs BBRR and scales only creature casts; the list concentrates on noncreature spells, exile and cast chains. **Alternative cut: The Lost and the Damned** — sacrifices major exile-cast 3/3 payoff (more damaging to identity). **Rejected cut: Mystic Remora** — removes early card-access lifeline. **Rejected cut: Neheb or Loyal** — removes the deterministic line itself. | **PROPOSE_SWAP_FOR_CORY_APPROVAL: Rakdos → Aggravated Assault**, no canonical mutation. |
| **Grinning Ignus {2}{R}** | Birgi front face + Ignus makes repeatable creature casts/ETBs (net zero red per loop); Nightscape Familiar can make colorless mana positive. With Abaddon out and X≥3, every Ignus hand cast gets cascade; a subsequent Brain Freeze benefits from the acquired storm count. | Candidate cut Rakdos or high-MV payoff; removing Birgi is **invalid** to this hypothesis. More creature-loop/combo focus, fewer independent threshold enablers; cannot say this immediately deals damage or draws cards without outlet. | **KEEP BASELINE / RESEARCH PRIORITY 2**: strong off-standard interaction, not a demonstrated better slot than Assault/other cascade engine. |
| **Chaos Warp {2}{R}** | Instant-speed way to address a resolved permanent, particularly nonblue enchantment/artifact stax that this 99 otherwise struggles to remove; permanent replacement risks are real. A qualified hand cast can itself cascade at X≥3. | Pyroblast is the M5 suggested cut but loses low-cost blue stack defense and another 1-MV cascade hit; weaker situational alternatives are high-MV threat packages, but their distinctive payoffs matter. | **HOLD / targeted table-dependent upgrade**: real gap; no unilateral cut authorized. |
| **Stormfist Crusader {B}{R}** | On your own upkeep makes each of three opponents lose 1 ⇒ X≥3, plus an extra card for you even before combat. | It draws **each opponent** too, gives away cards into the three-opponent table and is fragile. M5 Wheel of Fortune cut is especially bad for Breach and hand refills. | **KEEP BASELINE**, next priority if insufficient turn-level threshold reported. |
| **Aurora Phoenix** | Printed cascade; grants a **second** cascade trigger when hand-cast with Abaddon X≥6; returns from your graveyard after other cascade casts. | Mind's Desire, unlike Phoenix, retains unique storm/chain ceiling and one Abaddon-granted cascade at X≥6. Pilot cast neither candidate, so no comparison. Cutting Call Forth erases two printed cascades. | **KEEP Mind's Desire**; former 3-v-3 game experiment **inconclusive**, never claim performance win. |
| **Deny Reality** | Printed cascade at MV5; any-permanent bounce can partly address a resolved permanent. | Bituminous Blast's instant-speed 4 damage and printed cascade matter; Pyroblast cut loses blue interaction. Sorcery bounce doesn't permanently solve stax. | **KEEP BASELINE** against both registered cuts; compare Chaos Warp first for the genuine gap. |
| **Poxwalkers** | Repeated tapped graveyard return when a spell cast from outside hand, including cascade exile casts. | Cutting Thermo-Alchemist or Kessig Flamebreather reduces fast reusable threshold output; replacing Birgi removes high-impact cast mana/exile face. | **KEEP BASELINE** unless creature resiliency becomes the actual failure mode. |
| **Hullbreaker Horror / Tidespout Tyrant** | Strong spell-triggered bounce engines and possible zero-cost artifact loops. | M5 proposed **Pyroblast** cut; moving from one-mana stack protection to 7–8 MV spell-centric bouncer is a large tempo loss, not merely a Spellbook 'completion'. Heroic loops require source-payable spells and legal targets. | **REJECT exact ranked swaps**, protect fast interaction and Abaddon identity. |
| **Descent into Avernus** | Upkeep mana + group damage reliably increases same-turn X before main if it survives. | Group also receives Treasures; helps opponents deploy interaction; self-damage/time investment. | **HOLD**; metagame sensitive, not universally above conditional engine slots. |
| **Spear Spewer / Guttersnipe / Ancient Cellarspawn** | Redundant life-loss/instant-spell threshold engines. | Spewer requires untapping; Guttersnipe depends on instant/sorcery cast instead of all noncreatures; higher-cost Cellarspawn requires relevant discounted spells. | **KEEP BASELINE** pending evidence cheap threshold density inadequate. |
| **Blood for the Blood God! / Lord of Change / Be'lakor** | High ceiling refill or Demon ETB payoffs. | Greater top-end/creature-count dependency, inefficient hands; current already has large 6- and 11-MV payoffs and draw. | **KEEP BASELINE**, no superior cut established. |
| **Reiterate / Grinding Station / Time Warp / Past in Flames** | Combo and spell recursion diversity. | Existing LED/Breach/Brain Freeze and tutors; forced cut of LED/Breach, Rite, Wheel or other compact enabler is actively adverse. M5 Spellbook proximity isn't a payable infinite or multiplayer result. | **KEEP BASELINE** against proposed swaps, not proof these cards are categorically weak. |
| **Chromatic Lantern / Commander's Sphere / Temple of the False God** | Generic fixing/colorless ramp. | Worse at accelerating a five-MV tri-color commander than premium fetch/rainbow/zero-mana ramp and offers no threshold engine. | **REJECT**; popularity-sorted false positives. |

The most promising challenger is thus not the top-ranked M5 Hullbreaker result, but the **on-list Neheb + Loyal Subordinate → Assault** interaction. If Cory accepts the proposal in a later authorized cycle, the new 100-card list must be separately recomputed, Oracle-verified, legality-cleared and approved. **No change is preapproved by this report.**

## Oracle, legality and rules

**Baseline provenance:** canonical raw approved TXT SHA is recorded both by canonical override and October 14 raw-source reconciliation, and current October 16 verification attested **100/100, singleton, B/R/U, official legal** using then-current Scryfall bulk updated October 15; the earlier 94-name per-card audit is recorded in the source repo. On October 19 the Wizards **Commander** banned/restricted list was checked; no current approved card is unexpectedly banned. Scryfall's list of printings can contain upcoming TRK dual-land reprints; an upcoming *specific printing* does not make the already-existing card name illegal. The actual future printing's physical availability is separate; no project exception is invoked or changed. All candidates discussed are proposals and receive independent legality checks before any potential list modification.

**Verified current candidate Oracle (external):**
- Aggravated Assault: {2}{R} enchantment, {3}{R}{R} sorcery-speed activation: untap your creatures and create **an extra combat followed by an extra main phase after this main phase**, officially Commander-legal. https://mtg.wtf/card?q=%21Aggravated+Assault
- Neheb, the Eternal: at beginning of **each** of your postcombat main phases add R per 1 opponent life lost **during this turn**; if multiple postcombat main phases occur, it triggers at each beginning; not a mana ability and can be responded to. https://mtg.wtf/card/mkc/158/Neheb-the-Eternal and https://www.mtgassist.com/cards/Commander-Masters/Neheb-the-Eternal/rulings/
- Loyal Subordinate: lieutenant checks controlling a commander **on resolution**; each opponent loses 3 at beginning of each combat on your turn. https://mtg.wtf/card/cmm/172/Loyal-Subordinate
- Stormfist Crusader: each player draws and loses 1 on **your upkeep**, including each opponent. https://mtg.wtf/card/eld/203/Stormfist-Crusader
- Grinning Ignus: {R} and return to hand as activation cost for {C}{C}{R}; sorcery-speed mana ability, legal. https://www-.mtg.wtf/card/stx/104/Grinning-Ignus
- WotC official current format list: https://magic.wizards.com/en/banned-restricted-list ; October 12 announcement https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026 .
- Current Abaddon/exile and other baseline printed ability words: checked against the exact-recorded audit file `refinement/tests/Abaddon_Current_Card_Audit_2026-10-13.csv`, with source metadata and 2026-09-25 rules. Reference rules (effective Sept. 25, 2026): https://magic.wizards.com/en/rules.

**Critical interaction boundaries:**
1. **Neheb/Assault** creates the extra postcombat main even if no one attacked; Neheb checks life lost during turn cumulatively. The first Neheb trigger must actually **resolve** and net at least five R for a repeat activation without other mana. At exactly five, loop nets zero mana; if over five, it accumulates R. Declaring 'infinite red' when only five was lost is false. More combat steps without repeated loss **do not automatically win**: require Loyal Subordinate + controlled commander, unblocked attackers, or another actual outlet.
2. **Loyal Subordinate** says lose life, not deal damage. Solphim does **not** double it; Bloodletter does during your turn. Removal of Abaddon before Loyal resolves stops the lieutenant trigger from producing life loss. Removal of Neheb before postcombat main stops the mana trigger; targeted answers can interrupt at numerous priority windows.
3. **Birgi/Ignus** cycle at baseline cost: pay R to bounce Ignus and make 2C+R; recast costs 2C+R; Birgi gives R ⇒ **red pool net 0**, creature casts accumulate. With Nightscape Familiar reducing R spells generic mana by one, one C can remain per cycle. This is not a direct life-loss trigger, nor does Kessig Flamebreather trigger on creature casts. A storm spell or Abaddon-granted cascading exile-hit is a *separate* outlet/precondition.
4. **Breach/LED/Brain Freeze** prior worked state: ten cycles starting with LED+Breach on battlefield, Brain Freeze+Wheel plus SIX fuel cards in grave, 70 self-library and 90 each opponent, using twice each cycle's total Brain Freeze self-target resolutions to mill six replacement fuel, 10U floating after ten iterations; red land + 2 blue pays for escaped Wheel to force opponents to draw from empty libraries. Correctly distinguish **storm copies (not cast)** from future storm count, LED discards and six fuel per iteration; opponent responses or insufficient graveyard/remaining cards can interrupt. Never call unconditional infinite.
5. **Cascade and timing:** Abaddon grants on hand-cast during its controller's own turn, and spells cost even when alternate cost paid retain printed MV; suspended no-cost cards MV0 are valid cascade hits. Printed cascade + Abaddon grants separate triggers, e.g. Bituminous Blast (MV5) or Noise Marine (MV5) get 2 when X≥5; Call Forth (MV11) has two printed + one granted at X≥11. Wild-Magic Sorcerer grants cascade ONLY to first spell cast from exile in the turn. No permanent-free casts without matching permissions.
6. **Nalfeshnee** copies spells cast from exile; permanent copies enter as tokens as they resolve, spell copies aren't cast for cast-triggered pingers. **Storm-Kiln Artist** has 'cast or copy' on instant/sorcery so can trigger from spell copies. **Solphim** doubles noncombat damage, **Bloodletter** doubles life loss, and 3-opponent aggregate X is the sum of each opponent's actual loss.

No current card or interaction is knowingly represented as officially legal solely due to a project exception.

## Finite sequencing and adversarial scenarios

**Scenario A — tested by exact rules/mana arithmetic (not simulated matches):** Three opponents; control Abaddon, Loyal Subordinate, Neheb at start of normal combat; have Aggravated Assault in **hand** and no preexisting R floating. With no blockers/attacks needed, Loyal Subordinate trigger resolves in regular combat and opponents each lose 3 ⇒ X=9. In the following postcombat main, Neheb adds **9R**. Cast Assault from hand for **2R paid using 3 of those R**, leaving 6R; it gains cascade because X≥3 (optional cascade hit may change resources, not needed). Once Assault resolves, activate for **3RR (5R)**, leaving 1R. In extra combat Loyal again drains each for 3 if Abaddon still present ⇒ X=18. Next postcombat main Neheb adds **18R**, enough to reactivate and repeat. At each extra combat, opponents again lose 3, so with no responses finite repeated drains kill players from finite life totals. **Necessities:** 4 permanents/commander before combat, enough prior opponent life loss, postcombat Neheb trigger resolution, Assault resolving and remaining for future activations, no prevention/loss-redirection or relevant removal. If an opponent responds with removal, repeat is not guaranteed.

**Scenario B — shorter mana access:** Neheb and Assault on battlefield; before initial postcombat main, all opponents collectively lost **at least 5** that turn (for example Boltwave with three opponents creates total 9). Neheb produces ≥5R, Assault can be activated. Further postcombat main phases each grant at least the same R as **cumulative life loss persists this turn**. Without Loyal, repeated combats need a valid damage outlet: untapped attack-capable creatures with paths through blockers, or a cast/trigger that uses additional phases. This is an infinite phase loop, not automatically lethal.

**Scenario C — pilot counterfactual:** With a raw un-mulliganed 99-card library, two named one-of cards are co-seen among 7 cards at probability **7×6/(99×98)=0.433%**, among 12 cards **12×11/(99×98)=1.361%**. This does **not** model six tutors, draw, mulligans, conditional mana, or whether the commander and remaining outlets are cast/available; it shows the combo must be evaluated as an *additional* value line, not claimed turn-4 deterministic. Legacy baseline probabilities: 7-card chance ≥2 lands 76.46%, ≥3 lands 45.33%; 7-card ≥2 lands + 1 of 12 tagged early accelerators 43.49%. These are *descriptive card-density facts*, NOT commander-cast probabilities or win rates. Authority: `refinement/tests/Abaddon_Baseline_Consistency_Report_2026-10-13.md`.

**Adversarial Table 1 — Rule of Law/Rest in Peace:** Restricting the number of spells per turn can suppress both baseline cascade followthrough and proposed Assault's cascade trigger; Rip stops the compact Breach win. With no Chaos Warp present, play may depend on advance stack answers/Otawara bounce. A single Assault swap does not fix this. **Adversarial Table 2 — creature board attrition:** Exile Neheb/Loyal/Subordinate before main; the Assault alternate line collapses and becomes sorcery-speed three-mana value-light extra-combat mana sink. Protected baseline Rakdos can still threaten discounted creatures if enabled, so there is tangible downside to cutting it. **Adversarial Table 3 — wide blockers/pillowfort:** Assault extra combats do not guarantee combat damage; Loyal's beginning-of-combat life loss *bypasses blockers but not removal of the lieutenant or commander*. **Adversarial Table 4 — blue interaction:** Replacing Mystic Remora (M5 initial suggested cut) reduces the ability to find answers after opponents cast stack interaction; keeping it preserves counterplay.

**What was NOT tested:** no qualified matched-opening-hand Monte Carlo accounting for Assault, no Forge effect-aware multiplayer match, no real opponent priority/effect engine, no external card cache downloaded in this execution environment, no measured performance delta or win-rate claim. Existing M5 'pass' labels do not qualify because the model treated candidates as castable or counted Spellbook completion without effect resolution. Here the rule trace is source-backed and finite; the merits of one card cut are strategic authored judgment, not empirically established dominance.

## Conclusions and unresolved evidence

1. **PROPOSE_SWAP_FOR_CORY_APPROVAL:** `-1 Rakdos, Lord of Riots / +1 Aggravated Assault`. Strongest available *commander-identity-preserving* challenger due to actual Neheb/Assault repeat-combat resource line and Loyal/Subordinate finish, with Assault also hand-cast cascade-eligible after early damage. Rakdos is the structurally most contestable current four-MV creature-only cost-reducer because of BBRR cost and narrow function; preserve Neheb, Loyal, Birgi, Thermo, Remora, Wheel, LED, Breach, Call Forth. Caveat: Rakdos is a large flying trampler and discounts future creature casts if life loss is achieved; it might outperform the enchantment without Neheb. **Proposal, NOT applied or owner-approved.**
2. **KEEP pending new evidence:** Mind's Desire over Aurora Phoenix; Bituminous Blast over Deny Reality; Thermo-Alchemist over Poxwalkers; Mystic Remora over M5 Assault suggested cut; protect mana-fastening Chrome Mox, fetches, Lotus Petal, Wheel, LED/Breach.
3. **HOLD / ranked followups:** (a) Chaos Warp or Rakdos Charm for real stax/artifact/enchantment-heavy tables with an appropriate cut, (b) Birgi + Grinning Ignus looping only with named payoff and exact mana proof, (c) Stormfist Crusader if repeated tests show threshold insufficient on your own turn, (d) possible five-MV The Lost and the Damned attrition/cast-from-exile efficiency vs high-end alternatives. None by itself authorizes a card edit.
4. **No hard blocker to authored review evidence**: verified current baseline source, finite line accounting, source-linked 98 M5 and 60 legacy decisions, explicit opponent responses, quantified mana/card density and non-modeled uncertainty. **No canonical changes were made.** Retain source raw hash exactly. This reviewer is **NOT** an independent Pass C. No Phase B/M6 certificate or milestone acceptance claimed.

## Source and test receipts

- Live canonical deck authority `https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/state/current_deck_overrides.json`
- Exactly approved raw deck `https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/decklists/Abaddon_the_Despoiler_Approved_2026-10-13.txt` raw SHA `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`
- Canonical 94-row oracle/print/legality audit `refinement/tests/Abaddon_Current_Card_Audit_2026-10-13.csv` blob `5a1025c0ccc1738c32beaf4ea940d7da7065482f`; 2026-10-16 fresh verification `refinement/verification/retrospective_1_to_8/Verification_Gate_Abaddon_the_Despoiler_2026-10-14.md`; canonical 2026-10-13 exhaustive interaction note `refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md`
- 60 Abaddon decisions `refinement/decisions/Abaddon_the_Despoiler_Candidate_Decisions_2026-10-12.csv`; 98 M5 case packet `https://github.com/corymstover/GrokBotMTGCompanion/blob/chatgpt-cycle76-m6-refinement/data/grixis/m6/review_packets/abaddon-the-despoiler.json`; narrow original `data/grixis/m6/author_reviews/cycle131_batch_a_01.json`; prior stats `refinement/tests/Abaddon_Baseline_Consistency_Report_2026-10-13.md`
- Previous qualified **rules-coherent bounded** Breach sequence `refinement/tests/Abaddon_Breach_Sequence_Audit_2026-10-13.md`. Prior three-paired-games Aurora vs Desire Forge trial inconclusive (neither candidate cast, unmatched actual libraries, decision_use_allowed=false) `refinement/decisions/Abaddon_the_Despoiler_Candidate_Decisions_2026-10-12.csv`.
- Rules https://magic.wizards.com/en/rules ; official October 19 bans https://magic.wizards.com/en/banned-restricted-list ; https://mtg.wtf/card?q=%21Aggravated+Assault ; https://mtg.wtf/card/mkc/158/Neheb-the-Eternal ; https://mtg.wtf/card/cmm/172/Loyal-Subordinate ; independent Neheb/Assault interaction https://edh-combos.com/combo/3750-4945/ .
- EDHREC conditional cascade archetype page https://edhrec.com/commanders/abaddon-the-despoiler/cascade ; historical legacy EDHREC lift and counts are observational only, not exchangeable with current filtered sample sizes.
- New deep-review ledger entry: `data/grixis/m6/single_deck_depth_tracker.json` must be moved to `DEEP_REVIEW_COMPLETE` **only after** review evidence and exact-head GitHub CI. Before that keep `IN_PROGRESS`. Review artifact alone proves no independent Pass C or performance superiority. 
