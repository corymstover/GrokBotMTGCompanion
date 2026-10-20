# M6 Comprehensive Commander-First Authored Review #55 — Tetsuo, Imperial Champion

**Exact ID:** `Tetsuo__Imperial_Champion` index54, #55/62; 2026-10-20. First-party ChatGPT authored deep review, NOT GrokBot independent Pass C. **Decision under final candidate/probe review: KEEP** exact locked canonical source; never apply a swap by engineering script.

## Source and test receipts

- Engineering authority `corymstover/GrokBotMTGCompanion` integration branch `chatgpt-cycle76-m6-refinement`: `AGENTS.md`, `grixis/M6 Commander-First Single-Deck Review Standard.md`, depth tracker `54/62` before review, registry, subtracker, [Commander-specific blueprint](../../blueprints/tetsuo-imperial-champion.json), Oct16 6 verified [rules interactions](../../../interactions/tetsuo-imperial-champion.md), [Stage C mana source](../../mana_base/tetsuo-imperial-champion.json), [M5 packet](../review_packets/tetsuo-imperial-champion.json) 44 paired candidate hypotheses.
- Canonical `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json#decks.Tetsuo__Imperial_Champion`: officially **APPROVED/LOCKED by owner Oct15 2026**. Source exact approved `refinement/decklists/Tetsuo_Imperial_Champion_Approved_2026-10-15.txt` git blob `1049ea399013f9633c0aeae998139f8218ce75a2`, source closeout `refinement/decisions/Tetsuo_Imperial_Champion_Candidate_Decisions_2026-10-15.md`, approval ready Oct15. **Exact approved SHA-256 `d6d7561f00cb56cfb86cd79024975130d718ddc7f3a1bddf0c62f61dc422822e`, engineering logical `lh1:fda37e991784a0844a31db1c357f33bd92f34894ab687b4bef444a97f8c976ee`**. No source identity discrepancy. The 12 owner-approved swaps include Leyline Axe, Oathkeeper, Savage Beating, World at War, and premium mana; not new swaps.
- Raw deck independently parsed: **100 physical including commander, 99 library, 91 distinct names, 35 lands**, no MDFCs, only **Island x5 / Mountain x4 / Swamp x3** repeated basic lands; singleton otherwise. No companion, no project exceptions. UBR official Commander legality and current Oracle PASS as recorded Oct15 canonical gate. Scryfall Oracle snapshot Oct16, rulings Oct15, WotC rules 2026-09-25. Targeted Oracle corroboration: [Tetsuo](https://mtg.wtf/card/2x2/235/Tetsuo-Imperial-Champion), [WotC ACR Excalibur notes](https://media.wizards.com/2024/downloads/ACR_Release_Notes_l743nDdwuot4/EN_MTGACR_ReleaseNotes_20240418.pdf), [World at War updated Oracle](https://mtg.wtf/card/roe/172/World-at-War), [Genji Glove](https://www.mtgaddict.net/oracle/en/sp-special-sets/ub-universes-beyond/fin--final-fantasy/258--genji-glove), [Leyline Axe](https://mtg.wtf/card/fdn/129/Leyline-Axe), [Buster Sword WotC FIN](https://media.wizards.com/2025/downloads/FIN_Release_Notes_3O87RLY5EO/EN_FIN_Release_Notes_2025_1_15.pdf), [Oathkeeper](https://mtg.wtf/card/chk/265/Oathkeeper-Takenos-Daisho). **No full new October20 Oracle/banned-list rescan claimed.**
- Source natural ceiling **Power Bracket 4 — Optimized**, Archidekt tags **Equipment / Free-Cast Spells / Extra Combats**. Original Tetsuo Umezawa #54 uses tapped-or-blocking kill; **different** Imperial Champion uses equipped attack free spell or damage, preserving both decks' uniqueness.

## Commander identity and natural ceiling

For {U}{B}{R} Samurai Tetsuo: when it **ATTACKS and is EQUIPPED**, choose ONE of damage mode (deals damage equal to the greatest Equipment mana value attached to it to ANY target, including a player/creature/PW) OR cast instant/sorcery from HAND with MV <= that equipment greatest mana value **without paying mana cost**. Condition is **intervening-if** both as it triggers and resolves: if no Equipment at declare attack, no trigger, and if unequipped before resolution it does nothing. Mode is chosen when triggering, but ceiling is recalculated with CURRENT Equipment attached on resolution. Noncombat damage mode is sourced by Tetsuo and Basilisk Collar adds deathtouch/lifelink to THAT damage. Equipment's printing MV is used; Excalibur printed12 even if cost-reduced to 2; no average/total MV sum. Equipment ability/Cost reduction don't make commander 12 mana.

**Protected commander-first:** at least 6 high-MV Equipment (Excalibur12, Kaldra7, Argentum6, Embercleave6, Genji5, Hexplate5, Leyline4, Hammer4), attach cheat (Brass Squire/Hammer/Gilgamesh/Blacksmith Talent), reliable attack haste/ward/indestructible (Boots/Coat/Oathkeeper/Winged), mana/draw (Signets/Talismans, Remora/Rhystic/Jhoira), **spells worth free-casting DURING COMBAT** (Ancestral Vision0, Profane Tutor0, Wheel of Fate0, Inevitable Betrayal0, Chandra Ignition5, Savage Beating5, World at War5), extra combat sources and two 2-card paid infinite-combat lines (Assault + Sword of Feast/Famine or Reaver Cleaver with enough mana/damage). Distinct from plain Grixis Voltron: high Equipment mana value has a **second independent spellcasting payoff** and determines damage even if equipped creature itself is small.

No generic breach/Oracle/Time Warp shell to force Bracket5: commander is combat-dependent and can be stopped by chump blockers, instant artifact removal, suppressing the Equipment, removing creature while attack trigger stacked, and running out of spells in hand. Most cEDH-style super-efficient combo packages would replace high MV gear and free-cast combat spells, destroying Tetsuo's own plan.

## Full 100-card role audit

A source-row-complete original audit of all 91 line identities and repeated basics. Roles are not category replacements; each entry has a concrete participation/cost/limit.

| TXT row | Qty | Approved card | Role | Commander-specific effect and failure mode |
|---:|---:|---|---|---|
| 1 | 1 | Tetsuo, Imperial Champion | CMD | 3 mana {U}{B}{R} Samurai: ATTACKS WHILE EQUIPPED -> choose damage to ANY target equal to greatest attached Equipment MV or cast instant/sorcery from HAND at/below same ceiling free; must remain equipped on resolution. |
| 2 | 1 | Academy Ruins | LAND | Untapped C land 1U,tap target artifact card from graveyard to top library, useful equipment recursion at tempo/card draw cost, not UBR source. |
| 3 | 1 | Aggravated Assault | EXTRA | 2R enchant 3RR activate only as sorcery -> untap own creatures, add combat then main; recurrent if Sword Feast untap or Reaver Cleaver Treasure yields 5+ repeatable mana. |
| 4 | 1 | Akki Battle Squad | EXTRA | 5R red Goblin Samurai grants extra combat first time modified creature attacks each turn, requires Tetsuo equipped/counters and surviving attack. |
| 5 | 1 | Ancestral Vision | FREE | Suspend-only U sorcery with NO printed mana cost, MV0: Tetsuo free-cast from hand draws3 without waiting suspend; cannot normally cast by paying no cost. |
| 6 | 1 | Anchor to Reality | TUTOR | 2U sorcery sacrifice artifact/creature cost then search artifact/Equipment and put onto battlefield under restrictions; can access gear but costs material. |
| 7 | 1 | Ancient Tomb | LAND | Untapped CC for equip/high-MV artifact with 2 life damage; cannot supply Tetsuo UBR. |
| 8 | 1 | Arcane Signet | RAMP | Two mana untapped UBR fix, indispensable three-color commander/Forge. |
| 9 | 1 | Argentum Armor | EQUIP | 6 MV Equipment equipped +6/+6 and attack destroy target permanent, raises commander free-cast ceiling6, EQUIP {6} costly without autoattach. |
| 10 | 1 | Badlands | LAND | BR untapped typed fetchable dual, no blue. |
| 11 | 1 | Basilisk Collar | EQUIP | MV1 deathtouch+lifelink on commander: Tetsuo triggered noncombat damage gains life and deathtouch lethality to target creature, but low free-cast ceiling if ONLY attachment. |
| 12 | 1 | Blacksmith's Talent | ATTACH | Red Class opens equipment and upgrades equip synergy and combat growth via later paid levels; must pay development mana before full value. |
| 13 | 1 | Blasphemous Act | SWEEP | 8R may cost R with enough creatures, does 13 to all creatures including Tetsuo; valuable rescue but conflicts with creature Voltron equipment board. |
| 14 | 1 | Blood Crypt | LAND | BR fetchable shock, untapped costs2 life. |
| 15 | 1 | Bloodstained Mire | LAND | Swamp/Mountain type fetch for one life, finds Badlands/Crypt/Xander typed triome for UBR reach. |
| 16 | 1 | Brainstorm | DRAW | U instant draw3 put2 cards back, fetch shuffles and Force pitch, incremental equipment/spell choice. |
| 17 | 1 | Brass Squire | ATTACH | 3 artifact creature tap attach target Equipment to target creature you control, bypasses six-mana equip cost but needs haste/turn to tap. |
| 18 | 1 | Buster Sword | EQUIP | MV3 equipped creature +3/+2; when equipped creature deals combat DAMAGE TO PLAYER draw1 then may free-cast spell from hand with MV <= combat DAMAGE, not equal to sword MV. |
| 19 | 1 | Chandra's Ignition | FREE | 3RR sorcery target creature YOU CONTROL deals damage equal its POWER to each OTHER creature and each opponent; Tetsuo attack free cast can target himself if no protection from instants/sorceries, boardwipe risk to other allies. |
| 20 | 1 | Chaos Warp | INTERACT | 2R instant permanent shuffle then opponent flips library top, answers enchant/artifact without destroying Tetsuo. |
| 21 | 1 | Command Tower | LAND | Untapped UBR. |
| 22 | 1 | Conqueror's Flail | EQUIP | MV2 equipment buffs based colors and restricts opponents casting spells during YOUR turn while attached to creature you control; small ceiling but meaningful combo protection. |
| 23 | 1 | Cyclonic Rift | INTERACT | 1U bounce one nonland or 6U overload opponent nonlands, clears blockers/hate for Attack. |
| 24 | 1 | Dalakos, Crafter of Wonders | ATTACH | UR legendary, Equipment spells cost? actual makes Equipment casting/equip mana via tap mana only artifacts, and equipped attacking creatures gain flying/haste; supports deployment and aerial attacks, slow three mana. |
| 25 | 1 | Deflecting Swat | PROTECT | 2R free when commander controlled, retarget target spells/abilities to protect Tetsuo/gear; no immunity from boardwipe. |
| 26 | 1 | Dimir Signet | RAMP | 2 rock activated 1,tap -> UB, supports initial UBR/blue draw. |
| 27 | 1 | Embercleave | EQUIP | MV6 Equipment double strike/trample and +1/+1, casting cost reduced per attacking creature and flash/autoattach on ETB, sets six-spell ceiling and Voltron burst. |
| 28 | 1 | Enthusiastic Mechanaut | RAMP | UR flying haste artifact creature reduces artifact spells by1 generic; supports equipment but many colored costs remain. |
| 29 | 1 | Etherium Sculptor | RAMP | 1U artifact creature reduces artifact spells by1 generic, accelerates gear and Arcane Signet, fragile. |
| 30 | 1 | Excalibur, Sword of Eden | EQUIP | Printed MV12 despite cast discount equal historic permanents' total MV; equipped legendary +10/+0 vigilance, equip legendary2, maximum Tetsuo free-cast ceiling and huge attack. |
| 31 | 1 | Exotic Orchard | LAND | Opponent colors UBR conditional, risky versus colorless pods. |
| 32 | 1 | Fabricate | TUTOR | 2U artifact tutor to hand, finds exact needed high-MV equipment, Squire, defense; not free itself unless Tetsuo equipment ceiling>=3. |
| 33 | 1 | Fierce Guardianship | PROTECT | 2U free noncreature counter while commander controlled, protects ability/extra combats from removal. |
| 34 | 1 | Flooded Strand | LAND | Island/Plains type fetch one life, finds Steam Vents/Volcanic/Underground Sea/Watery/triome. |
| 35 | 1 | Force of Will | PROTECT | 3UU or exile OTHER blue card from hand pay1 life, free stack protection when tapping out for equipments; 22 nonland other blues source. |
| 36 | 1 | Frantic Search | DRAW | 2U instant draw2 discard2 untap three lands, free from Tetsuo if equipment MV>=3, untap lands recoups casting tempo. |
| 37 | 1 | Genji Glove | EXTRA | MV5 equipment gives double strike; if equipped attacks in FIRST combat of turn, untap that creature and add additional combat immediately after this one; equip3, only first-combat trigger. |
| 38 | 1 | Gilgamesh, Master-at-Arms | ATTACH | 4RR Samurai ETB/attack look top6 put any number Equipment onto battlefield and attach ONE of them to Samurai, topdeck contingent but powerful high-end burst. |
| 39 | 1 | Godo, Bandit Warlord | EXTRA | 5R Samurai? Godo is Barbarian; ETB equipment tutor to field, first ATTACK each turn with Godo untap Samurai you control and add extra combat; requires Godo attack, not Tetsuo alone. |
| 40 | 1 | Hammer of Nazahn | ATTACH | MV4 legendary Equipment enters attach to your creature, equipped creature indestructible; whenever Equipment enters your control can attach it to creature you control, risk of removal before attachment. |
| 41 | 1 | Heiko Yamazaki, the General | VALUE | 3R Samurai with trample, modified creatures attack enabling casting artifact from own graveyard each turn; recur equipment but costs spells/mana and combat. |
| 42 | 1 | Hexplate Wallbreaker | EXTRA | MV5 Equipment from ONE, autoattach on ETB via For Mirrodin! token, first equipped creature attack each turn creates extra combat/untap per Oracle; token body not Tetsuo until equip paid. |
| 43 | 1 | Inevitable Betrayal | FREE | Suspend U sorcery with no mana cost, MV0; free-cast from hand through Tetsuo fetch target opponent creature from deck onto battlefield, not automatically win. |
| 44 | 5 | Island | LAND | Five blue basics, source of blue counter/artifact tutors; legal basic duplication. |
| 45 | 1 | Izzet Signet | RAMP | 2 rock generic input -> UR, supports three-color Tetsuo. |
| 46 | 1 | Jhoira, Weatherlight Captain | DRAW | 2UR historic spell casts (artifacts and legends) DRAW, gear-heavy list benefits, four-mana weak defensive standalone. |
| 47 | 1 | Kaldra Compleat | EQUIP | MV7 living-weapon legendary equipment grants huge +5/+5, first strike, trample, indestructible/haste/exile-on-damage; equipping Tetsuo costs7 if no attach cheating. |
| 48 | 1 | Kediss, Emberclaw Familiar | PAYOFF | 1R legend whenever commander you control deals COMBAT damage to opponent, deals same to EACH OTHER opponent; Tetsuo triggered damage is NONCOMBAT and doesn't trigger Kediss. |
| 49 | 1 | Leyline Axe | EQUIP | MV4 equipment may START on battlefield if in kept opening hand, but NOT automatically equipped; equip3 gives +1/+1 double strike trample, enabling free World at War? World at War MV5 thus needs >=5 equip. |
| 50 | 1 | Luxury Suite | LAND | BR multiplayer conditionally untapped. |
| 51 | 1 | Mana Confluence | LAND | Any UBR at one life activation cost, excellent three-color commander. |
| 52 | 1 | Marsh Flats | LAND | Swamp/Plains typed fetch, finds Badlands/Blood Crypt/Underground Sea/Watery etc. |
| 53 | 1 | Misty Rainforest | LAND | Island/Forest typed fetch, finds Island blue duals/triome. |
| 54 | 1 | Mithril Coat | EQUIP | MV3 flash equipment grants indestructible, can enter autoattach to LEGENDARY creature you control, emergency protection and low cast ceiling. |
| 55 | 1 | Morphic Pool | LAND | UB multiplayer conditional untapped dual. |
| 56 | 4 | Mountain | LAND | Four red basics, red pip payoff R-heavy (~55%) and equipment attach/extra combats, legal repeat. |
| 57 | 1 | Mystic Remora | DRAW | U cumulative upkeep taxes opponent noncreature spells draws, important during gear setup. |
| 58 | 1 | Oathkeeper, Takeno's Daisho | EQUIP | MV3 legendary Equipment +3/+1 equipped; if equipped Samurai dies return that SAMURAI CARD to battlefield under you; if Daisho goes graveyard equipped creature EXILED, so protection has sharp downside. |
| 59 | 1 | Padeem, Consul of Innovation | PROTECT | 3U gives artifacts you control hexproof, upkeep draw if you control highest MV artifact; Excalibur printed12 qualifies, no protection vs mass destroy. |
| 60 | 1 | Polluted Delta | LAND | Island/Swamp typed fetch, reaches all shock/dual variants by shared type. |
| 61 | 1 | Profane Tutor | FREE | Suspend 2B no mana cost MV0, Tetsuo cast directly from hand free (search any card into hand); slow if only suspend. |
| 62 | 1 | Rakdos Signet | RAMP | 2 rock 1,tap -> BR, crucial red double spells and black UBR. |
| 63 | 1 | Rhystic Study | DRAW | 2U tax/draw opponents' spell casts; long game gear card fuel. |
| 64 | 1 | Savage Beating | FREE | 3RR instant cast only during combat, either double strike until end turn or untap attackers/add extra combat; when cast free via Tetsuo attack trigger at equipment MV>=5 it is inside combat so works; entwine cost extra1R payable if chosen, free-cast does not waive extra. |
| 65 | 1 | Scalding Tarn | LAND | Island/Mountain typed fetch, instant dual access. |
| 66 | 1 | Smoldering Marsh | LAND | BR typed enters tapped unless 2 basics, fetchable Swamp Mountain for black and red. |
| 67 | 1 | Sol Ring | RAMP | 1 -> CC, efficient high-MV gear and equip costs, not UBR commander. |
| 68 | 1 | Steam Vents | LAND | UR shock typed Island Mountain for blue/red, pay2 life to untap. |
| 69 | 1 | Sunken Hollow | LAND | UB typed tapped until >=2 basics, fetchable black/blue. |
| 70 | 3 | Swamp | LAND | Three black basics, source needed Tetsuo cast & Withering Torment, minimal B demand for others. |
| 71 | 1 | Swiftfoot Boots | PROTECT | 2 equip1 gives haste+hexproof; allows Tetsuo attack as soon as it enters once equipped, protects and no own targeted spell conflict. |
| 72 | 1 | Sword of Feast and Famine | EQUIP | MV3 protection green/black, combat damage to player target? opponent discards and you UNTAP ALL LANDS, fuel Aggravated Assault extra combats if can produce {3}{R}{R} after. |
| 73 | 1 | Sword of Fire and Ice | EQUIP | MV3 protection red/blue, combat damage to player deals2 ANY target and DRAW1, excellent midrange velocity and direct removal, not uncommandered spell-copy swap. |
| 74 | 1 | Sword of the Animist | EQUIP | MV2 attacks search basic land tapped, fixes mana and historic artifacts, raises commander free-cast to2 only, noncombat targeting not removal. |
| 75 | 1 | Swordsman's Steel | EQUIP | Equipment linked to Samurai/equipped combat and additional trigger synergy, exact card-specific line should use source Oct16 Oracle; preserve role in multi-Equipment package, no generic combo without further proof. |
| 76 | 1 | Talisman of Creativity | RAMP | 2 UR colored at 1 damage cost, fast commander/extra red. |
| 77 | 1 | Talisman of Dominance | RAMP | 2 UB colored, handles Tetsuo cast. |
| 78 | 1 | Talisman of Indulgence | RAMP | 2 BR colored, handles commander and RR extra combat. |
| 79 | 1 | Terminate | INTERACT | BR instant destroy creature can't regenerate, independent of equipment trigger or combat. |
| 80 | 1 | The Reality Chip | DRAW | 1U artifact creature reconfigure 2U, equipped can look top card and play lands/cast spells top, sustained card velocity if top not stuck, low MV ceiling. |
| 81 | 1 | The Reaver Cleaver | EQUIP | MV3 Equipment gives +1/+1 and TRAMPLE; when equipped creature deals combat DAMAGE to player create that many TREASURES, can fuel Assault3RR if damage >=5 unblocked each combat. |
| 82 | 1 | Training Center | LAND | UR multiplayer dual often untapped. |
| 83 | 1 | Underground Sea | LAND | UB typed untapped dual fetchable. |
| 84 | 1 | Volcanic Island | LAND | UR typed untapped fetchable dual. |
| 85 | 1 | Vorpal Sword | EQUIP | B cost Equipment low MV1, equip BB; +2/+0 deathtouch and big BBB?? paid activation on combat damage can cause target player to lose game, high mana and threshold, not generic commander shot. |
| 86 | 1 | Watery Grave | LAND | UB typed shock, fetched. |
| 87 | 1 | Wheel of Fate | FREE | Suspend 1R zero-mana-cost MV0 sorcery, Tetsuo can cast directly from hand for free drawing 7 per player/discard all, symmetrical enemy refill. |
| 88 | 1 | Winged Boots | EQUIP | 2 Equipment grants flying+ward4, equip1, commander evasive attack and protects vs spells/abilities that target; low MV free-cast ceiling alone. |
| 89 | 1 | Withering Torment | INTERACT | 2B instant creature/enchantment destruction with 2 life loss upon resolution, indispensable vs Rest in Peace/stax and enemy kill spell; no free zero spell when countered. |
| 90 | 1 | World at War | FREE | 3RR sorcery cast from HAND through Tetsuo DURING combat still creates extra combat AFTER second main (if not already passed), rebound occurs next upkeep because cast from hand even for free; no additional alt cost required. |
| 91 | 1 | Xander's Lounge | LAND | Tapped UBR typed Swamp Island Mountain triome cycling, fetch target, sets back one tempo turn |

### Structural baseline: mana, creature/equipment ratios, access and tension

**Lands and fixing:** 35 lands, no MDFCs, 6 fetches (Bloodstained, Flooded, Marsh, Misty, Polluted, Scalding), one always-tapped land and 8 conditional taplands in Stage C audit. U20/R17/B18 land color source possibilities, incl nonland U25/R22/B23; source pips ~R55.3%, U38.3%, B6.4% excluding commander UBR. **This is a red equipment/extra-combat deck, not a double-black control shell.** Turn3 all-three-land-color *presence* .727 and turn3 third natural land drop ~.759 per source model; do not multiply independently or interpret as probability of actually casting Tetsuo (untapped mana, rock development and real hands not modeled). Commander tax recast 5 then 7 total mana. Excalibur artifact-historic cost discount depends on actual permanents and decreases its CAST COST, NOT MV for trigger; 12 is genuine ceiling at realistic late artifact board.

**Early turns and consistency:** T1 Sol Ring / T2 Signet or Mechanaut / T3 Tetsuo+protect may happen but attaching valuable equipment asks more mana/turns, with no false T3-equipped attack before haste. Leyline Axe in kept OPENING HAND may start on battlefield **unequipped**, but Tetsuo equip3 after cast plus haste from Boots can enable first combat line with correct mana. Kaldra Compleat living weapon ETB starts equipped on its own Germ token, not automatically Tetsuo; need equip7 or cheat attach. Argentum Armor equip6 is similarly prohibitive without Squire or Hammer. High Equipment MV alone without **attach** or **attack** produces no commander value. A bare Basilisk Collar/sword of Animist doesn't allow free Savage Beating MV5, and even with Excalibur on field but NOT attached, it doesn't raise cap.

**Card advantage and removal:** Jhoira draws when casting historic spells; tutors Fabricate, Profane Tutor, Anchor to Reality, top-view Reality Chip, Remora/Study and combat Buster/Sword F&I furnish access. Black is low density, but Withering Torment, Terminate and counters address enchantment/creature threats. Deflecting Swat/Force/Fierce protect when tapped out, Oathkeeper death trigger returns Samurai ONLY if equipped and destroyed, exile Equipment itself is a failure route. Swiftfoot Boots hexproof doesn't protect against sweepers, Mithril Coat protects destroy damage but not exile/bounce. The highest-variance slots include Gilgamesh six mana/uncertain top six, Godo six mana attack dependence, Heiko requiring modified attack to cast from grave, Akki six mana, Hexplate Wallbreaker high equip cost, Jhoira four-mana, Padeem four mana only protects artifacts, Vorpal Sword big activation. Yet all plausibly advance Tetsuo's identity better than a generic spell copier, and eliminating cheap Signets/Rhystic/Sword F&I is a high cut cost.

**Win conversion and limits:** Sword Feast and Famine + Aggravated Assault infinite combats ONLY if equipped carrier does combat damage to PLAYER and newly untapped lands can provide at least 3RR per turn cycle after damage. The Reaver Cleaver similarly needs at least five Treasure per successful damage event to fund 3RR (plus other appropriate resources), with trample helps. Extra combats via Godo, Genji, Hexplate, Savage Beating, World at War are generally finite and depend on timing and being re-untapped and combat survivors. Commander trigger direct damage can finish player from Excalibur MV12, but that's NONCOMBAT and doesn't count as commander damage for 21-damage rule; Basilisk Collar lifelink/deathtouch works on this damage. When equipment is removed in response to the trigger, ability fails even though attack was declared equipped.

## Candidate pool and competing cuts

M5 packet contains **44** pairs, **all P3 commander-fit-only**, no P0 independent agreement or P1 measured-performance confirmation. 15 fail, 15 inconclusive, 14 no detectable difference and **zero test passes**. Many candidates were completely effect-blank under paired v1.1 simulator, so NO implication of actual win rate. Main cut concentration Rakdos Signet (early colored UBR), Sword of Fire and Ice (draw+2 damage+MV3 Equipment), World at War (paid combat-compatible five-MV extra combat and rebound), Swordsman's Steel (Equipment density), Leyline Axe (four MV opening-hand free Equipment double strike/trample), Padeem (artifact hexproof/draw) and Remora (early card flow). All 44 route-specific add/cut decisions are below.

<!-- TETSUO55_CANDIDATES_ANCHOR -->

### Serious challengers and alternate cuts outside M5

- **Sword of Wealth and Power** equipment protected from instants/sorceries once attached: strong in abstract, but that PROTECTION disallows your own `Chandra's Ignition` targeting Tetsuo while equipped, a direct unforced contradiction. Would replace less synergy-rich Sword in different build, not here.
- **Time Warp / Temporal Manipulation** can yield an extra full turn through Tetsuo if Equipment MV≥5, very high generic power but not as focused as true extra combats, source keeps World at War/Savage.
- **Shadowspear** one-mana lifelink/trample recursion of utility, but duplicates Collar's lifelink and Leyline/Embercleave trample; would lower attach ceiling if replacing MV5 gear.
- **Komainu Battle Armor** and **Jhoira, Ageless Innovator** may add vehicles/goad/mana acceleration, but generic engines not better than direct Equipment attach/damage.
- **Full tutor/cEDH combo shell** would weaken high-MV equipment and forced free spells; violates natural ceiling and identity-first project standard.

## Oracle, legality and rules

Verified Oct15/16 source plus targeted official notes as above; project exceptions none. For approval changes outside source, rerun unexpected new/current legality, Oracle and color check, NOT silently auto-accept M5 candidate.

**Attack trigger and cap:** Tetsuo attacks equipped, chooses damage or CAST mode on stack, checks equipped condition on resolution. Greatest attached **printed MV** dynamically checked on resolution, e.g. Excalibur12 (even if cost0), Kaldra7, Argentum6, Embercleave6, Leyline4, Collar1. For damage choose target when triggering; it must be legal when resolving, and Tetsuo is damage source, affected by Collar. Sword F&I equipment MV3 grants nothing to `Savage Beating` MV5 unless other MV5+ attached. A new attached Equipment placed in response can increase cap on resolution if Tetsuo remains equipped; removing all attached Equipment fizzles intervening-if. `Sword of Wealth and Power` can make self-targeting instant/sorcery like Ignition illegal.

**Casting timing:** Free-cast mode uses spell from HAND with MV <= cap, normal timing restriction is bypassed because cast DURING trigger resolution. No-mana-cost suspend spell has MV0 and alternate-cost permission lets it cast, not "cast for {0}" ordinarily. `World at War` current Oracle after SECOND MAIN phase gives combat+main and untaps attackers at beginning; when cast in first attack combat there is still a second main upcoming, so it creates real extra combat. Rebound because it **was cast from hand** via Tetsuo, even without mana cost, exile after resolving and cast from exile next upkeep; no rebound after copy/cast from deck or exile. `Savage Beating` has **cast only during combat** and a first-combat timing-friendly extra combat; Tetsuo's attacking trigger meets restriction, but need equipment MV≥5; if choose entwine must PAY extra cost while main casting cost is free. `Relentless Assault` and `Seize the Day` extra-combat effects tied to "after this MAIN PHASE", and resolving during combat provides no current main phase for extra combat; both correctly absent.

**Combo/Voltron:** 3RR `Aggravated Assault` activate only as sorcery during main; Sword Feast/Famine combats deal player damage to untap ALL lands, funding another activation only if sufficient red & 5 mana. Reaver Cleaver creates Treasure equal to combat damage dealt to PLAYER and only if carrier connects, so 5+ damage suffices 3RR once treasures converted, enough again on each repeated unblocked combat. If opponent chumps without trample or removes equipment before combat damage, no mana and no loop. Aetherflux etc not in this list, so don't assign a fake generic win.

**Equipment and protections:** Leyline Axe from opener starts on battlefield not equipped. Excalibur cost reduction based total MV of HISTORIC permanents controlled, static equipment's own printed MV12 unchanged, equipped +10/+0 (WotC ACR text) vigilance (not +10 toughness). Kaldra Compleat Germ token holds equipment until move. Oathkeeper returns equipped creature card ONLY if it is a Samurai CARD in grave, when sword itself goes grave equipped creature is EXILED—plan both triggers correctly in boardwipe. Genji Glove first combat condition produces one additional combat even when cast already on field, not infinite itself. Hexplate/extra-combat mana must be evaluated per turn. Buster Sword free cast permission is triggered by combat damage and limited by actual DAMAGE, not Equipment MV. Kediss triggers on commander COMBAT damage to player, not the 12 NONCOMBAT direct target ping. The Reaver Cleaver triggers only from damage dealt to player by equipped creature, not Tetsuo attack trigger burn.

## Finite sequencing and adversarial scenarios

Explicit finite cast/equip/resolution/hand/target/priority sequences, not Monte Carlo. No assumed Equipment already equipped without paid equip or cheat effect.

<!-- TETSUO55_FINITE_ANCHOR -->

## Conclusions and unresolved evidence

**Final authored candidate decision pending scenario completion: KEEP** exact locked 100; the most tempting theoretical generic replacements (extra-turn cards, Time Sieve, Helm of the Host, spell-copy engines) have higher setup/time or remove genuine Gear+spell ceiling or early colored mana. The M5 packet produced NO modeled pass and cannot justify a swap; there are conditional off-packet improvements worth future tests, not owner-approved changes. Distinct Tetsuo attack-based optimized Bracket4 plan must remain separate from tap-target Tetsuo. No full new legality sync or live four-player match win samples claimed. No canonical artifact, approved SHA, lock status, project exception, independent Pass C, or milestone acceptance modified.

