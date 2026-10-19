# Loki, the Deceiver — M6 comprehensive commander-first review #28

**Authored review:** 2026-10-19. Tracker ID `Loki__the_Deceiver`, index 27. **Canonical:** `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json`, `APPROVED` / `LOCKED` (user October 14, 2026), exact approved SHA256 **`5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062`**, `refinement/decklists/Loki_the_Deceiver_Approved_2026-10-14.txt`. Engineering logical `lh1:1af6ee049bf73721081d3bed599d91b174e2487b42630b8b1c51827301e49c68`. Identity discrepancy NONE. No companion or project exception. **My own independent parsing of live approved export: 100 physical cards, 95 distinct names, 95 source rows, 34 lands, 66 nonland slots including commander, only Island ×3, Mountain ×2 and Swamp ×3 repeat.** UBR commander identity, approved Oct15 Oracle/official Commander legality and rules gate PASS with no reported errors; last gate's `approval_state=NOT_APPROVED` was an earlier pre-approval snapshot, superseded by live Oct14 manual `APPROVED/LOCKED` overrides. No current full-list external Oracle re-query in this review; targeted contemporary official WotC sources verified separately.

## Commander identity and natural ceiling

**Loki costs 1UBR, 4/4 God Sorcerer Villain.** When Loki is **declared** to attack, his trigger targets **another Villain you already control**; resolution creates a **tapped and attacking nonlegendary Illusion token** copied from that target's copiable values, with sacrifice at beginning of next end step. The token was **not declared as an attacker** and therefore does not trigger ordinary attack triggers. It **does** enter the battlefield, so ETB/as-enters, persistent static abilities and later damage triggers can work. Loki also draws **once per player damaged by one or more Villains in a combat-damage event**, not per Villain that hits the same player. Two Villains hit player A -> one Loki draw; hit A and B -> two draws.

**Protected strategic identity:** Villain density and early targets; Loki safely attacking through Cover of Darkness/Red Ghost and Lightning Greaves/Swiftfoot Boots; copy targets with ETB/static/combat damage; `The Master, Multiplied` and correctly timed Sundial to retain tokens; Roaming Throne/Hall/Kindred Discovery to turn combat into real card advantage; recurring Villain bodies that fight through removal. Natural ceiling **Bracket 4 Optimized** per Oct14 approved assessment. It is a combat- and board-presence-dependent commander without an inherent deterministic cEDH combo. Optimize that ceiling; don't inject Oracle/Consultation or Breach only because they are generically Grixis powerful.

**Fundamental separation:** the printed Loki-copy token can deal combat damage but its arrival does NOT trigger its own 'whenever this attacks' ability (Ultron/Killmonger counterexamples). Loki's Scepter granting Villain to a creature by a continuous type-changing effect qualifies that creature as a **target** at trigger resolution, but the new token copies only underlying copiable types; it isn't necessarily a Villain itself. Villain creature *spells* are cast, but Loki's created token is never cast (Madame Hydra does not trigger from token entry).

## Full 100-card role audit

Exact approved list, all **95 different source entries** individually accounted for by actual quantity, with the three basic-land repeats expanding to 100 physical cards. The role notes distinguish target quality, pressure, timing, and/or replacement risk.

| Source row | Approved card | Primary role | Tactical use / limitation |
|---:|---|---|---|
| 1 | Loki, the Deceiver | COMMANDER | Commander: 1UBR 4/4, target ANOTHER Villain on attack; token ETBs tapped/attacking and sacrifices at next end step; draw once per damaged player. |
| 2 | An Offer You Can't Refuse | Interaction | One-blue answer to noncreature spell, but feeds opponent two Treasures. |
| 3 | Arcane Signet | Mana/tempo | Reliable any-commander-color 2 mana rock. |
| 4 | Avengers: Under Siege | Tribal infrastructure | Multi-chapter Villain production, damage pressure, later Treasures; slow Plan scheduling but enables target density. |
| 5 | Badlands | Land | Untapped BR dual, helps Loki color density. |
| 6 | Baron Strucker, HYDRA Overlord | Villain | Cost reducer/connive from Villains entering; tokens from Loki create relevant entry but not cast triggers. |
| 7 | Black Cat, Cunning Thief | Villain | Opponent-resource theft on native Villain, value copy; vulnerable to attack blocking. |
| 8 | Black Market Connections | Value/access | Life for Treasure, draw, or Changeling Villain body; useful but top generic challenger cut. |
| 9 | Blasphemous Act | Interaction | Often cheap board reset but kills own Villain army; needs recovery. |
| 10 | Blood Crypt | Land | Typed BR shock, fetchable at life cost. |
| 11 | Bloodstained Mire | Land | Fetches typed duals for early Loki colors. |
| 12 | Carnage, Crimson Chaos | Villain | Reanimation and board pressure ETB makes a Loki token worth copying. |
| 13 | Cavern of Souls | Land | Naming Villain protects native Villain creature casts; does not necessarily fix non-Villain interaction mana. |
| 14 | Chameleon, Master of Disguise | Villain | Clone form becomes copiable: Loki copying it copies what it is now, not automatically new choice. |
| 15 | Chaos Warp | Interaction | Answers permanent, unpredictable replacement top deck. |
| 16 | Command Tower | Land | Untapped UBR; best three-color fixer. |
| 17 | Cover of Darkness | Tribal infrastructure | Fear makes Villains difficult to block, but shared color/artifacts block. |
| 18 | Crimson Cowl, Master of Evil | Villain | Villain board pressure; copy quality depends on ETB/static effects, not merely a combat keyword. |
| 19 | Crossbones, Malicious Mercenary | Villain | Villain damage pressure; test how many bodies to turn reach into actual lethal. |
| 20 | Cyclonic Rift | Interaction | 2 mana bounce or seven-mana overloaded asymmetric reset. |
| 21 | Dark Ritual | Mana/tempo | One-shot B acceleration; cannot alone supply U/R for Loki. |
| 22 | Deadly Rollick | Interaction | Free creature exile when Loki controlled, otherwise costs four; protects attacker. |
| 23 | Deflecting Swat | Interaction | Free target manipulation with commander; does not counter spells with no targets. |
| 24 | Demonic Tutor | Value/access | Universal 1B selection; identifies missing target/protection. |
| 25 | Doctor Doom | Villain | Native Villain clone target, but check current face/entry ability rather than assuming all attack triggers apply. |
| 26 | Doctor Doom, King of Latveria | Villain | Top-end native Villain engine, high mana; copied ETB can add resource advantage. |
| 27 | Doctor Octopus, Master Planner | Villain | Villain anthem persists during combat; temporary copy can still create value before delayed sacrifice. |
| 28 | Doom Reigns Supreme | Tribal infrastructure | Plan triggered by Villain entries and chapter scheduling; delayed value, no immediate pressure on empty board. |
| 29 | Dragonskull Summit | Land | Conditional untapped BR land; basis count matters. |
| 30 | Drowned Catacomb | Land | Conditional untapped UB land, two-pip sequencing. |
| 31 | Exotic Orchard | Land | Colors depend on opponents' land capabilities, not unconditional UBR. |
| 32 | Fierce Guardianship | Interaction | Free noncreature counter with commander controlled; unsafe to assume free if removed. |
| 33 | Hall of Echoes | Land | Colorless land: {5} precombat copy Loki; no ETB; attacks only if land held since start of turn. |
| 34 | Iron Monger, Sadistic Tycoon | Villain | Connive becomes +1/+1 counters on Villains; synergy with Prowler/M.O.D.O.K. |
| 35 | 3x Island | Land | Basic U, blue protection and Loki cast; copies legal basics. |
| 36 | Jeska's Will | Mana/tempo | 2R one-shot red mana and/or exiled card access when commander controlled; cannot supply missing U/B pips directly. |
| 37 | Kang Prime | Villain | Native Villain with value and type, but attack-copy impact should not be assumed without ETB. |
| 38 | Kang, Temporal Tyrant | Villain | High-mana Villain control/tempo, costly copy target; can win stalled games. |
| 39 | Killmonger, Ruthless Usurper | Villain | Strong genuine declared attack/combat effects, but Loki token entering attacking DOES NOT fire attack triggers. |
| 40 | Kindred Discovery | Tribal infrastructure | Choose Villain; Loki declared attack draws once, Loki token Villain entry draws once; token NOT declared an attacker. |
| 41 | Leader, Super-Genius | Villain | Beginning-of-combat connive occurs before declaration, can improve Prowler/board while digging for copy targets. |
| 42 | Lightning Greaves | Value/access | Gives immediate Loki haste and shroud; equip 0, shroud complicates targeting Loki with buffs/clone spells. |
| 43 | Loki's Scepter | Mana/tempo | Turns a target into Villain for Loki legality; added Villain type is NOT copiable by token unless in underlying copiable values. |
| 44 | Loki, God of Mischief | Villain | A permanent targeted by own Loki attack ability triggers this God once/turn to draw BEFORE clone creation. |
| 45 | Loki, Lord of Misrule | Villain | Repeatable board-copy effect; expensive and retains legendary/copy layering considerations. |
| 46 | Luxury Suite | Land | Conditional untapped BR in multiplayer. |
| 47 | M.O.D.O.K. | Villain | Connive engine on Villain; copies must be judged by actual current Oracle triggers. |
| 48 | Madame Hydra | Villain | Creates menace Villain tokens when Villain spells CAST; Loki tokens ENTER but are not cast. |
| 49 | Mana Confluence | Land | Any color but 1 life/tap. |
| 50 | Mana Drain | Interaction | UU counter plus delayed colorless ramp, useful protecting Loki. |
| 51 | Morphic Pool | Land | Conditional untapped UB multiplayer. |
| 52 | 2x Mountain | Land | Basic R supplies third color. |
| 53 | Mysterio, Master of Illusion | Villain | ETB builds 3/3 Illusion Villains based on nontoken Villain count; Loki copied Mysterio triggers ETB and creates more bodies. |
| 54 | Norman Osborn // Green Goblin | Villain | DFCreature Villain with transformation; copied form takes the actual face/characteristics, not arbitrary opposite face. |
| 55 | Oscorp Industries | Land | Thematic utility land; require source-paid comparison against untapped color source before cutting. |
| 56 | Otawara, Soaring City | Land | Channel bounce from hand still works even if nonbasic land hate; blue land otherwise. |
| 57 | Patchwork Banner | Mana/tempo | Mana + choose Villain anthem, strong two-role 3-mana artifact; does not accelerate first two turns well. |
| 58 | Path of Ancestry | Land | Fixing tapped land; casting Villain sharing subtype with Loki scries, but many generic spells do not. |
| 59 | Polluted Delta | Land | Fetches color dual/basic, contributes reliable U/B colored access. |
| 60 | Prowler, Clawed Thief | Villain | Whenever ANOTHER Villain enters, Prowler connives; original Prowler sees Loki's token ETB before blockers. |
| 61 | Reanimate | Value/access | Returns premium Villain to battlefield; ETB value works, but doesn't create an attack. |
| 62 | Red Ghost, Intangible Genius | Villain | Native unblockable Villain; second draw each turn creates hasty 3/3 Ape Villain, but combat-damage draw produces Ape AFTER attacker declaration. |
| 63 | Rhystic Study | Value/access | Generic fallback engine; does not increase Villain density. |
| 64 | Roaming Throne | Copy/preservation | Choose Villain; doubles Loki attack and combat-damage triggers (and other creature triggers), NOT Kindred Discovery enchantment trigger. |
| 65 | Scalding Tarn | Land | Fetches red/blue dual/basic, cast Loki on time. |
| 66 | Sol Ring | Mana/tempo | Accelerates generic mana but not UBR pips. |
| 67 | Spark Double | Copy/preservation | Copies a creature/planeswalker as nonlegendary; Loki copy of its form inherits copiable values; 4-mana investment. |
| 68 | Steam Vents | Land | Typed UR shock, life timing matters. |
| 69 | Stilt-Man, Towering Terror | Villain | Opponent creature theft on Villain combat damage; copy entering attacking may still hit for this trigger. |
| 70 | Sulfur Falls | Land | Conditional untapped UR. |
| 71 | Sundial of the Infinite | Copy/preservation | Activate on YOUR end step after sacrifice trigger goes onto stack; exiles that trigger and permanently preserves token; 1 mana plus tap. |
| 72 | 3x Swamp | Land | Basic B for Loki and tutors. |
| 73 | Swiftfoot Boots | Value/access | Haste and hexproof for Loki, equip 1 adds total cost. |
| 74 | Talisman of Creativity | Mana/tempo | UR fixer, colored damage tax. |
| 75 | Talisman of Dominance | Mana/tempo | UB fixer, colored damage tax. |
| 76 | Talisman of Indulgence | Mana/tempo | BR fixer, colored damage tax. |
| 77 | Taskmaster, Mercenary Mimic | Copy/preservation | Creature-based copy engine; check existing target and legend exceptions rather than assuming auto-copy of any creature. |
| 78 | The Master, Multiplied | Copy/preservation | Triggered abilities you control cannot force sacrifice/exile of creature tokens; prevents Loki delayed sacrifice while Master survives. |
| 79 | The Soul Stone | Mana/tempo | Black mana and later grave utility, slower than 2-mana rock; possible cut only with colored-source checks. |
| 80 | The Squadron Sinister | Tribal infrastructure | Villain combat-wide support/anthem, substantial with many bodies but payoff needs combat. |
| 81 | Thunderbolts Conspiracy | Tribal infrastructure | Returns nontoken Villains; cannot reanimate Loki tokens that ceased to exist. |
| 82 | Titan of Littjara | Copy/preservation | 6-mana Illusion, choose Villain as enters; Loki token copied Titan chooses type and gets ETB draw/loot, not attack trigger. |
| 83 | Tombstone, Career Criminal | Villain | Eligible Villain copy target; prioritize ETB, statics, or combat damage over plain attack triggers. |
| 84 | Toxic Deluge | Interaction | Scalable life-spend board reset; same own-board downside. |
| 85 | Training Center | Land | Multi-opponent untapped UR land, strong Loki fixing. |
| 86 | Ultron, Unlimited | Villain | Strong when Ultron itself is declared to attack; Loki-created Ultron copy does NOT gain an attack trigger. |
| 87 | Underground Sea | Land | Untapped UB typed dual, strong fixing. |
| 88 | Urborg, Tomb of Yawgmoth | Land | Makes all lands Swamps; benefits Black pips but supplies opponents black and dies to opposing Moon. |
| 89 | Urza's Incubator | Mana/tempo | Choose Villain, reduces cost of Villain creature spells; 3-mana future-value investment, tokens are not cast. |
| 90 | Vandalblast | Interaction | Single removal/overload artifact sweep; can't be cast overloaded without 5R. |
| 91 | Venom, Eddie Brock | Villain | Original Venom rewards sacrificed Loki token with counter+draw; saving tokens with Master reduces death triggers. |
| 92 | Villainous Hideout | Land | Thematic utility land; may enter tapped or need condition; not equate to untapped source. |
| 93 | Volcanic Island | Land | Untapped UR typed dual. |
| 94 | Watery Grave | Land | Typed UB shock, life timing matters. |
| 95 | Xander's Lounge | Land | Tapped triome fixes UBR and cycles late; tempo loss in four-mana commander deck. |

**Development and curve:** 34 lands, 29 unique land names, including eight basic slots (Island three, Mountain two, Swamp three) and 26 nonbasic land names. Fetchlands (Bloodstained Mire/Polluted Delta/Scalding Tarn), ABUR duals/shocks, untapped three-color Command Tower/Mana Confluence, Cavern of Souls for Villains, and several conditions/tapped lands provide UBR fixing but **Path of Ancestry, Xander's Lounge, and conditional reveal lands can delay turn-four Loki**; utility colorless Hall requires substantial investment to turn into attacker. Acceleration consists of Sol Ring, Signet, three Talismans, Patchwork Banner, Urza's Incubator, Loki's Scepter, The Soul Stone, occasional Black Market Connections treasure and Dark Ritual/Jeska's Will. Incubator/Villain discounts do not help pay Loki's generic? His own creature type is Villain and may qualify after naming Villain, but only **generic** portion of 1UBR is discounted, never colored pips. The five-mana+ Villain cluster (Doom, King of Latveria; Kang; Titan; The Master; etc.) risks entering after opponents establish blockers/wipes; mana payability matters, not just card ranking.

**Access and interaction:** Demonic Tutor/Reanimate/Rhystic Study/Kindred Discovery supplement combat-dependent draw. There is premium permission (Mana Drain, Offer, Fierce, Swat) and sweeping (Blasphemous Act/Toxic Deluge/Cyclonic Rift) plus Chaos Warp/Deadly Rollick/Vandalblast; wraths also delete Loki's target board, and low instant count leaves some fast combo windows. No compact native win combo. Permanent package includes several slow typal plans/anthems; the commander needs enough live targets before it can produce value. Failure modes: no other Villain, Loki removed before combat, copy target removed in response, all enemies sharing evasion color, mass removal, delayed sacrifice when Master/Sundial unavailable, opponent life totals too high before stabilized. Hall copying Loki requires 5 mana and not-summoning-sick land; cannot assume two attacks for free.

## Candidate pool and competing cuts

Reviewed `data/grixis/m6/optimizer/loki-the-deceiver.json`: Pass A contains **386 machine-projected add/cuts**, **0 Pass B**. No independent blinded Pass C from these. The Pass A pool systematically repeats `Loki, Lord of Misrule`, `Venom, Eddie Brock`, `Demonic Tutor`, `The Soul Stone` as cut targets; many additions are generic artifacts/creatures without a native Villain subtype or reliable ETB/damage payoff. Screening: actual copy target legality and effect on entry/after damage; slot efficiency vs other Villain bodies; interaction and mana density. All 386 are candidate DISCOVERY, not mechanically proven one-by-one. The Oct14 canonical three additions (Red Ghost, Titan, Hall) already exist in the approved list; do NOT propose them again.

| Serious new challenger | Competing cut | Alternative cut | Source-paid or commander-first trade-off | Decision |
|---|---|---|---|---|
| **Seize the Day** (4-mana extra combat, flashback 2R) | Black Market Connections | Urza's Incubator | After original combat, untap Loki in postcombat main for an extra declared attack and token copy, potentially repeat damage draws with evasive Villains. Extra combat alone doesn't untap all other attackers, loses steady card/treasure engine and needs protected Loki. | **KEEP**; top empirical challenger |
| **Aggravated Assault** | Kang Prime | Black Market Connections | Extra combat for 3RR repeatedly while mana available; pays 5 for each activation, slower than bodies/engine, and requires Loki survive attackers. | KEEP; test only |
| **Mysterio's Mirage** (discard-trigger 3/3 Villain) | Avengers: Under Siege | Black Market Connections | Prowler/M.O.D.O.K./Leader connive feeds discard, can create another Villain target by next turn, but requires prior discard and competes with Plan's broader bodies/damage/Treasures. | KEEP existing Plan |
| **Panharmonicon** | Urza's Incubator | The Soul Stone | Doubles some Villain ETBs and Kindred Discovery when a token enters; does NOT double Loki attack trigger itself. Cost four and does not make an independent Villain, while Incubator reduces costly Villain curve. | KEEP Incubator |
| **Strionic Resonator** | Loki, Lord of Misrule | The Squadron Sinister | 2 to cast then 2+tap per copied Loki triggered attack/damage ability, makes extra token when targeting valid Villain; low standalone board effect, less than broad copy/anthem payoff. | KEEP |
| **Reconnaissance Mission** | Rhystic Study | Black Market Connections | At 2UU it draws per individual creature dealing combat damage, whereas Loki draws per damaged opponent; useful but requires connection and provides no Villain bodies. Kindred Discovery already has entries and declared attacks. | KEEP Study |
| **Kindred Dominance / Raise the Palisade** | Blasphemous Act | Toxic Deluge | Less self-destruction but higher mana or temporary bounce; two current flexible board resets provide cost coverage. | KEEP |
| **Helm of the Host** | The Master, Multiplied | Sundial | Persistent extra copies but 4 equip 5 and token made in combat; far too expensive against established value engines. | KEEP |
| **Moonstone / attack-only Villain variants** | Venom or Loki, Lord of Misrule | Killmonger | Need precise current Oracle of each before crediting copy value; attack-only abilities never trigger on tapped-attacking token. Candidate rank not proof. | NO SWAP |
| **Generic Oracle/Consultation/Breach wins** | Villain creatures/typal infrastructure | Black Market Connections | Can raise generic Grixis win speed but falsifies the natural commander-centered strategy and consumes whole-package slots. | REJECT |

**Actual weakest/changeable incumbents considered:** Black Market Connections is generic but provides early Treasure, draw and Changeling Villain targets; The Soul Stone is a higher-mana rock but resilient and graveyard useful; Urza's Incubator is mediocre without many Villain spells but this list meets density; Avengers: Under Siege is slow but three different chapters make bodies/reach/Treasure; Kang Prime is not necessarily top clone target yet fills native high-value Villain threat slot; `Loki, Lord of Misrule` is situationally expensive but copies whole Villain board; `Venom` converts temporary sacrifice into cards and combat size, uniquely synergistic with Loki's downside; `Hall of Echoes` costs five to activate but is also a land and can become second Loki. `Titan of Littjara` six mana exposes tempo but genuine ETB copy payoff is large. Distinctive core outweighs speculative 4th/5th swap.

## Oracle, legality and rules

- **Current commander Oracle and legitimacy:** WotC `https://magic.wizards.com/en/news/feature/marvel-super-heroes-release-notes` (Loki item in Marvel Commander release notes), and Scryfall-reproduced Loki 1UBR/4-4 and Commander legal `https://mtg.wtf/card/msc/86/Loki-the-Deceiver`. Approved Oct15 gate `refinement/verification/loki_the_deceiver_2026-10-14/gate_output/Loki_the_Deceiver_2026-10-14_Complete_Gate.json` records 100/95, UBR, official legality PASS, rules PASS, zero exceptions. Does not mean fresh bulk 2026-10-19 legality reread.
- **Attack timing:** Loki trigger on DECLARATION of Loki as attacker, choose target other Villain then. Target removed/responds with control change = spell/ability loses legal target, copy doesn't appear. The created token ENTERS attacking but does not 'attack' for trigger conditions. Its ETB/choices still happen. `Kindred Discovery` naming Villain triggers from original Loki being declared attacking and (separately) from the Villain token **entering**, not because that token attacks. This distinction is independently confirmed by WotC Loki rulings.
- **Once-per-opponent draw:** Multiple Villains connect to one opponent simultaneously -> Loki draws once for that opponent; damage across players A and B -> two separate triggers. Roaming Throne naming Villain gives an extra trigger for Loki's second ability when it triggers; it doesn't double Kindred Discovery because source is enchantment rather than Villain creature.
- **God of Mischief:** Loki's attack ability targets a Villain, so `Loki, God of Mischief` (separate printed Villain creature) sees a permanent targeted by our ability and draws once that turn *before* token creation; WotC release notes confirm this God effect and timing.
- **Red Ghost:** Unblockable. Draw second card per turn while Ghost controlled creates 3/3 Ape Villain with haste; if the second draw is caused by Loki's **combat damage**, Ape arrives after declare attackers and cannot retroactively attack. Copy of Ghost is nonlegendary Illusion Villain and unblocked; if it triggers on second draw later, token's trigger works while Ghost copy still exists.
- **Titan of Littjara:** As enters choose Villain; subsequent ETB trigger lets draw for EACH other creature sharing chosen type, then discard one, rather than drawing only one. A Loki copy gets its own as-enters choice and ETB; the copy was not declared to attack, so Titan's 'attacks' trigger does not additionally fire.
- **Hall of Echoes:** {5} precombat causes Hall to become Loki while the legend rule is suppressed for turn. Hall did not enter when it changed, so no ETB; since Hall originally a noncreature land, summoning sickness **still checks continuous controller since start of turn** when it becomes a creature. If established from prior turn and untapped to attack, it can generate a separate Loki attack/copy trigger. No assumption that activating Hall on same turn land entered permits attacking.
- **Master and Sundial:** `The Master, Multiplied` says triggered abilities controlled by you can't make you sacrifice/exile creature tokens: prevents Loki's delayed end-step sacrifice while Master remains on field. `Sundial of the Infinite` must be activated **after** Loki's delayed sacrifice trigger has triggered and is on stack during **your end step** to exile it permanently; activating in combat skips end step that turn and can merely postpone trigger to next end step, not necessarily save it.
- **Scepter copy-layer:** Loki's Scepter can make a creature Villain to be a valid target, but Loki copying it does **not** carry noncopy type modification to token. Token is Illusion in addition to types copied, not automatically Villain. An unmodified non-Villain copy will not contribute to Loki combat-draw type count.
- **Venom and token death:** `Venom, Eddie Brock` triggers when another creature dies; a sacrificed Villain clone dying supplies counter+draw. Preserving a token via Master/Sundial naturally means it does NOT produce this death event, creating genuine sequencing choice. Token ceasing to exist later cannot be reanimated by Thunderbolts Conspiracy.
- **Type/ramp:** Urza's Incubator discount applies only to **Villain creature spells** cast, not Loki-created tokens. `Madame Hydra` triggers when Villain spells cast, not on copy tokens entering. `Path of Ancestry` cares about casting appropriate creature spells, not token creation. Cover of Darkness grants fear when naming Villain, **not** unblockability against all boards. Commander color identity UBR; no authorized exception needed or new legality problem established.

## Finite sequencing and adversarial scenarios

All cases are manually traceable **conditional game states**, not simulation observations, measured win-rates or proof of deterministic optimization. Define opponent reactions and source-paid costs where concrete:

1. **Development t1–t4:** land, Sol Ring/Signet and untapped UR/B sources can pay 1UBR Loki by turn 3/4; the five-colorless Hall ability is unrelated to casting Loki. An opener with Cavern + tapped Path + Xander's Lounge may be too slow to safely deploy Loki on curve; test land sequencing before trusting color total.
2. **No other Villain:** Loki alone attacks, but cannot legally target **another** Villain, hence no copy. It can still draw if it hits a player as a Villain. Adding extra combat without another Villain yields no additional token engine.
3. **Removal in response:** Loki declared attacking, trigger targets Doctor Octopus; opponent kills target before trigger resolution: no token. If opponent instead kills Loki after trigger is on stack while target stays valid, clone can still appear, but Loki's later draw ability won't be present at damage unless another Loki-effect remains.
4. **Original attack versus token attack:** Ultron is declared attacker -> his printed 'attacks' ability can trigger; Loki creates tapped-attacking copy of Ultron -> that copy does NOT trigger Ultron's attack ability. Replacing Venom with an attack-only Villain is therefore weaker than rank suggests.
5. **Prowler and Kindred Discovery:** Loki and Prowler declared attackers with Kindred Discovery Villain, Loki targets Prowler. Kindred Discovery triggers from declared Loki and Prowler attacks, not new token attack; copy Prowler entering triggers Discovery and ORIGINAL Prowler's 'another Villain enters' connive. Draw/discard resolves in attacker-declaration step BEFORE blockers if triggers resolve; then damage may trigger Loki draw once per player hit.
6. **Targeting God of Mischief:** God of Mischief on field, Loki attacks targeting another Villain; the target selection triggers God once (if unused), draw can be second card this turn; Red Ghost then spawns haste Ape Villain before combat damage if present. New Ape created in attackers step isn't attacking; haste doesn't put it into combat.
7. **Roaming Throne:** choose Villain. Loki attack trigger becomes two separate triggers, can target two *different* Villains if available, or same legal target twice; tokens enter separately. Original Loki damage-draw triggers twice per damaged player. But enchantment Kindred Discovery draws only on its own triggers, not multiplied by Throne's static.
8. **Red Ghost copy:** Loki targets Red Ghost, makes token tapped and attacking unblockable; it can connect with an opponent even with a crowded ground board (assuming no prevention effects). Draw at damage step may make additional Ape, but Ape cannot retroactively attack.
9. **Master removal:** Master Multiplied on battlefield prevents Loki end-step sacrifice. Opponent kills Master **before sacrifice trigger resolves**, tokens can be sacrificed, even if Master was there when they were created. Protect Master or use Sundial with timing.
10. **Sundial timing:** On YOUR end step sacrifice trigger is on stack, pay 1 and tap Sundial, end turn -> trigger exiled; token survives. Activate Sundial during combat instead -> sacrifice trigger has not triggered, may happen next end step, so 'I end turn early' alone not a permanent save.
11. **Hall of Echoes cost:** Have land Hall since previous turn and total 5 mana available in first main; activate, Hall becomes Loki and legend rule suppressed, then attack with original and Hall (unless tapped). Each declared Loki produces a clone on a legal Villain target, yielding extra Kindred triggers. Hall played this turn is summoning sick; no second attacker.
12. **Seize the Day challenger:** With Loki and another Villain active, first declare Loki attacking in the normal combat; then cast 3R sorcery Seize the Day in the **postcombat main phase**, targeting tapped Loki to untap it. Seize adds an additional combat **after that main phase**, so the newly untapped Loki can be declared attacking again and create a second copy; other creatures do NOT automatically untap, limiting damage. Casting Seize in the precombat main instead creates an extra combat **before** the normal one and does not untap Loki again between them, so it does not by itself grant two Loki attacks. Removal of Loki before the extra combat prevents the second attack. `Black Market Connections` yields value even when combat fails. Needs paired test.
13. **Aggravated Assault challenger:** Activation 3RR only at sorcery speed pays for untap all creatures and additional combat. If player has 5 free mana after first combat, can repeat, but no infinite mana assumed; opponents' blockers can still trade with attackers.
14. **Villain death versus preservation:** Copy Venom, sacrifice it at end step without Master -> original Venom can trigger as another Villain dies; Master stops that value but leaves a lasting combat body. Both branches require actual permanent presence and cannot be simultaneously counted.
15. **Board wipe:** Own Blasphemous Act may clear blockers but also kills Villain targets and Loki; sequencing recovery (Reanimate, Thunderbolts Conspiracy) needed before attack copy resumes. A proposed one-sided Kindred Dominance costs substantially more and can be dead before combat.
16. **Three-opponent distribution:** Loki + Villains connecting to A/B/C in the same combat deal at least one Villain hit per player -> baseline Loki draws three, not number of hits; group attacking only A draws one. Roaming Throne doubles Loki creature triggers if present; no fabricated probability of actually connecting.

## Conclusions and unresolved evidence

**Per-material-issue result: KEEP** current locked and approved canonical 100 unchanged. This is **not** a conclusion that no improvement exists; it means strongest plausible challengers presently lack tested evidence to displace existing identity-important or indispensable interaction pieces at natural Bracket 4 ceiling. `Seize the Day vs Black Market Connections` is strongest research challenger: extra combat specifically repeats Loki's copy trigger, but payoff is board-dependent and cannot replace the Connections treasure/card/access with established positive net value. `Mysterio's Mirage vs Avengers: Under Siege` is secondary, gated on how many discard/connive triggers naturally occur. Compare Panharmonicon vs Incubator only on paid high-Villain ETB game states. Source rank positions alone do not authorize changes.

**Unresolved:** No freshly run 100-name Oracle/banlist query after canonical Oct15 clean gate; candidate draw, pressure and mana outcomes are unmeasured; unresolved real table attack/survival distribution, source-paid turn-4 Loki + haste enabling, copied target availability, sweep recovery. No qualified independent Pass C. Explicitly **no deck mutation, no new approval, no milestone acceptance, no project exception change, no asserted simulator measurements**.

## Source and test receipts

- Canonical lock SHA `5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062` verified in `state/current_deck_overrides.json`, `refinement/decklists/Loki_the_Deceiver_Approved_2026-10-14.txt`. Canonical decision `refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md`, full historical audit `refinement/decisions/Loki_the_Deceiver_Whole_List_Audit_2026-10-14.csv`, complete approval gate `refinement/verification/loki_the_deceiver_2026-10-14/gate_output/Loki_the_Deceiver_2026-10-14_Complete_Gate.json`.
- Engineering branch authority `AGENTS.md`, `grixis/M6 Commander-First Single-Deck Review Standard.md`, `data/grixis/m6/single_deck_depth_tracker.json`; blueprint `data/grixis/blueprints/loki-the-deceiver.json` and `data/grixis/m6/optimizer/loki-the-deceiver.json` candidate evidence, not auto-approval.
- Contemporary primary rules WotC `https://magic.wizards.com/en/news/feature/marvel-super-heroes-release-notes` supports Loki attack/copy/ETB and Loki God of Mischief, Red Ghost, and Roaming Throne rulings. MTG card Oracle `https://mtg.wtf/card/msc/86/Loki-the-Deceiver`, `https://mtg.wtf/card/msc/335/Titan-of-Littjara`, `https://mtg.wtf/card/who/146/The-Master-Multiplied`, `https://mtg.wtf/card/pfra/179p/Hall-of-Echoes`.
- Independent physical-card accounting: 100 cards, 95 distinct names, 34 land slots, commander singleton, only basics repeat; exact table above reconciles 95 source rows. Manual case analysis only, no claimed opponent AI, probability model, paid simulator or Monte Carlo runs.
- CI: new immutable review commit must pass exact-head GitHub Actions; only then fill tracker receipt with successful run and update next ID.
