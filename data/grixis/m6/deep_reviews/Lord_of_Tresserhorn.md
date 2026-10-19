# Lord of Tresserhorn — M6 comprehensive commander-first deep review #29

**2026-10-19, single-deck original author analysis.** Tracker `Lord_of_Tresserhorn`, tracker index28. Canonical authority `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json`: **APPROVED/LOCKED** since Cory's explicit 2026-10-14 approval, approved 100-card SHA256 **`95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e`**, `refinement/decklists/Lord_of_Tresserhorn_Approved_2026-10-14.txt`. Engineering logical `lh1:eae4578c6338f3c2caf25f7359154e851b6f51f179c2ddb3ac2883f95489aafa`, source-identity conflict NONE. Historical October CSV/TXT source hashes differ from approved list intentionally due prior authorized changes; do not revert to historical snapshot.

**Independent physical count:** 100 cards; 98 distinct names; 98 export rows; 35 lands, 64 nonland library cards, 1 commander. Only **Swamp ×3** repeats (Commander basics permitted). UBR color identity, no companion/project legality exception. 2026-10-14/15 exact approval gate reports official Commander legality/rules/identity PASS, zero errors. This review independently evaluates focal Oracle via canonical pinned blueprint and WotC 2026 Reality Fracture Karn release notes; no wholesale contemporaneous Scryfall query was rerun, so record that limit rather than claiming fully fresh certification.

## Commander identity and natural ceiling

**Lord of Tresserhorn costs 1UBR, a 10/4 legendary Zombie.** Its ENTIRE ETB ability is one targeted trigger: **you lose 2 life, sacrifice two creatures, and TARGET OPPONENT draws two**; Lord itself can have to be sacrificed if too few other creatures remain when the ability resolves. {B}: regenerate Lord cannot regenerate from sacrifice, lethal toughness reduction or exile. Lord's four-mana ten power with costly drawback defines the puzzle, not merely another sacrifice general.

**Primary plan: Voltron/infect + drawback suppression.** Preposition Torpor Orb or Karn, Argent Defender (creatures/artifacts entering don't trigger abilities), flash Dress Down before Lord enters, or hold Stifle/Tale's End to counter its triggered ability on stack. Give Lord haste/unblockability while preserving your right to target it with Tainted Strike/Phyresis/Chandra's Ignition: Greaves SHROUD is a real limitation, Brotherhood Regalia ward/unblockable is not. A single 10-damage infect hit eliminates one player, and Kediss can spread Lord-source noncombat infect damage to the other opponents. Uncaged Fury gives +1/+1 and double strike, 22 commander combat damage in an unblocked combat, versus unboosted double strike only 20. Pain for All and Chandra's Ignition capitalize on exactly Lord's ten power. This is **Bracket 4 — Optimized**, not artificially cEDH, per canonical decision.

**Secondary support:** disposable/recursive Zombies and creatures pay Lord's ETB without catastrophic attrition and form compact Gravecrawler + Phyrexian Altar or Rooftop Storm/Ashnod's Altar loops with Blood Artist/Zulaport/Commander-sourced Zombie presence. If suppressors already make Lord ETB free, these are a backup not an excuse to make the whole deck another aristocrats shell. Protect two suppression axes, haste/evasion, and poison-to-ten payoff; don't cut these for generic engine rankings.

## Full 100-card role audit

Every source row including all repeated basic Swamps independently reconciled; each distinct card's tactical role and major limitation explicitly noted. **98 source rows = 100 cards**, not 98-card deck.

| # | Current approved card | Main role | Commander-specific interaction / liability |
|---:|---|---|---|
| 1 | Lord of Tresserhorn | Commander | 10/4 1UBR Zombie; on entry lose 2 life, sacrifice two creatures, target opponent draws two; B regenerates only against destruction. |
| 2 | Anger | Haste/evasion/protection | Sac by Lord's drawback without ability suppression is legitimate way to grant haste with Mountain, but need second creature. |
| 3 | Arcane Signet | Mana/fixing | 2 mana all commander colors, safest turn2 rock. |
| 4 | Arena of Glory | Land | Red-source haste utility; activations/exert sequencing for commander cast, not unconditional every-color source. |
| 5 | Ashnod's Altar | Sac outlets/combo | Free creature sac makes CC, but CC alone cannot recast B-cost Gravecrawler absent Rooftop Storm. |
| 6 | Badlands | Land | Untapped typed BR dual. |
| 7 | Bitterblossom | Fodder/recursion | One flying Faerie every upkeep for life; predeploy for Lord's two-sac cost, not Zombie for Gravecrawler. |
| 8 | Blasphemous Act | Answers | 8R minus 1 per battlefield creature, deals 13 to all creatures; with Pain on Lord, 13 reflected to opponents if triggers. |
| 9 | Blood Artist | Death payoffs | Creature-death drain single target + life gain, closes Gravecrawler/Altar loops; source is 0/1 vulnerable. |
| 10 | Blood Crypt | Land | Fetchable BR shock, choose pay life for untap. |
| 11 | Bloodghast | Fodder/recursion | Landfall recurring fodder, not self-suppressed by Karn since land isn't creature. |
| 12 | Bloodstained Mire | Land | Fetch typed red/black dual or triome; triggers Bloodghast landfall twice including fetched land. |
| 13 | Bojuka Bog | Land | Tapped black land GY disruption, can slow a four-mana commander. |
| 14 | Brotherhood Regalia | Haste/evasion/protection | Equip legendary creature {1}, ward {2}, cannot be blocked; targeted Lord spells still function. |
| 15 | Carrion Feeder | Sac outlets/combo | One-mana Zombie sac outlet, grows, can't block; feeds recursion/payoffs. |
| 16 | Cavern of Souls | Land | Naming Zombie makes Lord and zombie fodder spells uncounterable, not counterspell colored pips. |
| 17 | Chandra's Ignition | Kill conversion | At 3RR, Lord deals own power to other creatures and each opponent; infect applies to Lord as source. |
| 18 | Chaos Warp | Answers | Kills blocker, protects Lord, or prevents opponent's win; role contested versus main combo. |
| 19 | Command Tower | Land | Untapped unconditional commander colors. |
| 20 | Cover of Darkness | Haste/evasion/protection | Choose Zombie; fear means black/artifact blockers still block; not generic unblockable. |
| 21 | Deadly Rollick | Answers | Free creature exile while Lord controlled, otherwise paid mana; protects offensive window. |
| 22 | Deflecting Swat | Haste/evasion/protection | Redirects a spell/ability target while Lord controlled, not a generic counterspell. |
| 23 | Demonic Tutor | Card access | 1B put selected answer/finisher to hand, not a direct win. |
| 24 | Dimir Signet | Mana/fixing | 1 & tap produces UB; likewise input mana. |
| 25 | Diregraf Captain | Death payoffs | Zombie anthem and loss-life when Zombie you control dies; note Lord is Zombie. |
| 26 | Dress Down | Drawback suppression | Flash 1U draw and creatures lose abilities through end step; must resolve before Lord ETB, then removes Lord regeneration temporarily. |
| 27 | Exotic Orchard | Land | Mana/color choice, life cost, tapped timing or utility opportunity must be tested in turn-two-four hands. |
| 28 | Feed the Swarm | Answers | Kills blocker, protects Lord, or prevents opponent's win; role contested versus main combo. |
| 29 | Fellwar Stone | Mana/fixing | May produce opponents' land colors, variable in three-color pods. |
| 30 | Goblin Bombardment | Sac outlets/combo | Sac outlet deals 1 noninfect damage per creature; payoff for Gravecrawler loops independent of commander damage. |
| 31 | Gravecrawler | Fodder/recursion | B cast from grave if controlling another Zombie; Lord itself qualifies while on battlefield. |
| 32 | Headless Rider | Fodder/recursion | Nontoken Zombies dying make tapped 2/2 Zombie tokens; helps feed Lord and recursive engine. |
| 33 | High Market | Land | Sac Lord as alternative response? Avoid sacrificing Lord when no backup; sac own token for 1 life. |
| 34 | Island | Land | Basic U protects against Moon, Stifle/NOW and other blue requirements. |
| 35 | Jadar, Ghoulcaller of Nephalia | Fodder/recursion | End step produces decayed Zombie if none; upkeep sac fodder, but timed and only one at time. |
| 36 | Karn, Argent Defender | Drawback suppression | 2 mana 1/3 artifact creature; artifacts and creatures entering do not cause abilities to trigger, globally including opponents. |
| 37 | Kediss, Emberclaw Familiar | Kill conversion | After commander combat damage to opponent, Lord deals SAME amount as noncombat damage to every other opponent; infect carries, commander damage does NOT. |
| 38 | Lightning Greaves | Haste/evasion/protection | Haste, shroud, equip0; blocks YOUR Tainted Strike/other targeting when equipped. |
| 39 | Luxury Suite | Land | Mana/color choice, life cost, tapped timing or utility opportunity must be tested in turn-two-four hands. |
| 40 | Mana Confluence | Land | Any color 1 life cost; life management matters when using Warren Soultrader. |
| 41 | Marsh Flats | Land | Fetch Swamp typed dual/triome, helps Bloodghast landfall and pre-deployment black. |
| 42 | Misty Rainforest | Land | Fetch Island typed dual/triome, helps U mana for Stifle. |
| 43 | Morphic Pool | Land | Mana/color choice, life cost, tapped timing or utility opportunity must be tested in turn-two-four hands. |
| 44 | Mountain | Land | Basic R and Anger condition. |
| 45 | Muddle the Mixture | Answers | UU instant counter instant/sorcery; 1UU transmute at sorcery speed tutors MV2 Torpor Orb/Phyresis/Regalia. |
| 46 | Mystic Remora | Card access | Find suppression/poison/protection pieces; not a win by itself. |
| 47 | Nether Traitor | Fodder/recursion | One-mana-ish recurring shadow creature, costs B after another creature dies; needs mana and creature death. |
| 48 | Nightscape Familiar | Fodder/recursion | Zombie, discounts blue/red spells by generic 1 but Lord has colored B/U/R so only 1 generic saved, and can regenerate itself. |
| 49 | Not of This World | Haste/evasion/protection | 7 mana Eldrazi spell becomes free only when countering a spell/ability that targets Lord with power >=7; NOT universal free protection. |
| 50 | Ophiomancer | Fodder/recursion | Makes 1/1 deathtouch Snake if no Snake at each upkeep; reusable sacrifice fodder with correct timing. |
| 51 | Otawara, Soaring City | Land | Mana/color choice, life cost, tapped timing or utility opportunity must be tested in turn-two-four hands. |
| 52 | Pain for All | Kill conversion | 2R Aura: on enter Lord deals power damage to target other object/player; if Lord dealt damage, it deals that much to every opponent. |
| 53 | Phyresis | Kill conversion | Aura permanent infect; opponent can remove aura before damage/ability resolution. |
| 54 | Phyrexian Altar | Sac outlets/combo | Sac creature for 1 mana of chosen color; one Gravecrawler + another Zombie forms repeatable death/recast chain. |
| 55 | Phyrexian Tower | Land | Land taps+sacs one creature to add BB, strong fodder converter but not repeatable untapped. |
| 56 | Pitiless Plunderer | Sac outlets/combo | Whenever another creature you control dies creates Treasure; Gravecrawler recursion but four-mana setup. |
| 57 | Polluted Delta | Land | Fetch Island/Swamp typed dual and triome, best color fixing. |
| 58 | Rakdos Signet | Mana/fixing | 1 & tap produces BR; must have input mana unlike Talisman. |
| 59 | Reassembling Skeleton | Fodder/recursion | 1B return from grave tapped; mana-positive only with additional payoff engines. |
| 60 | Rogue's Passage | Land | Colorless land, expensive evasion adds colored pip strain. |
| 61 | Rooftop Storm | Sac outlets/combo | Six mana pays 0 instead of Zombie creature mana costs (additional commander tax still applies); with Ashnod + Gravecrawler makes colorless loops. |
| 62 | Scalding Tarn | Land | Fetch Island/Mountain typed lands; blue and red. |
| 63 | Shadowspear | Haste/evasion/protection | Equip 2, +1/+1 trample/lifelink; elevates Lord to 11 power; can remove opponents' hexproof/indestructibility with paid ability. |
| 64 | Shambling Ghast | Fodder/recursion | Cheap Zombie fodder; dies to give -1/-1 to creature or Treasure. |
| 65 | Sheoldred's Edict | Answers | Two mana instant sacrifice opponent creature or planeswalker; strong versus indestructible/hexproof threats. |
| 66 | Shivan Reef | Land | Mana/color choice, life cost, tapped timing or utility opportunity must be tested in turn-two-four hands. |
| 67 | Shizo, Death's Storehouse | Land | Untapped black source; 1B/tap grant fear to legendary Lord, not guarantee against black/artifacts. |
| 68 | Slip Out the Back | Haste/evasion/protection | U instant phase out Lord and put +1/+1 counter; phased out Lord cannot deal damage until next turn. |
| 69 | Sol Ring | Mana/fixing | 1 mana artifact adds CC; does not produce commander UBR colored pips. |
| 70 | Steam Vents | Land | Fetchable UR shock, can cost life for untap. |
| 71 | Stifle | Drawback suppression | U instant counters Lord's ETB triggered ability on stack in its entirety; must hold mana during entry. |
| 72 | Stubborn Denial | Haste/evasion/protection | U counter noncreature spell unless payer pays 1, but Lord's 10 power turns ferocious into hard counter. |
| 73 | Sulfurous Springs | Land | Mana/color choice, life cost, tapped timing or utility opportunity must be tested in turn-two-four hands. |
| 74 | 3x Swamp | Land | Basic B for infect, tutors, regeneration. |
| 75 | Swiftfoot Boots | Haste/evasion/protection | Haste and hexproof, equip1; unlike Greaves does not block own targeting. |
| 76 | Tainted Strike | Kill conversion | B instant +1 power and infect until EOT; Lord now 11 power and injects 11 poison if unblocked. |
| 77 | Takenuma, Abandoned Mire | Land | Black source channel mills/returns creature or planeswalker (not targeted from your GY as simple tutor). |
| 78 | Tale's End | Drawback suppression | 1U counter triggered/activated ability (Lord ETB) or legendary spell; flexible timing. |
| 79 | Talisman of Creativity | Mana/fixing | UR source under land pressure, damage for colored mana. |
| 80 | Talisman of Dominance | Mana/fixing | UB source under land pressure, damage for colored mana. |
| 81 | Talisman of Indulgence | Mana/fixing | BR source under land pressure, damage for colored mana. |
| 82 | Terminate | Answers | Kills blocker, protects Lord, or prevents opponent's win; role contested versus main combo. |
| 83 | Torpor Orb | Drawback suppression | 2 artifact stops entering creature triggered abilities globally, also blanks some backup ETB value. |
| 84 | Toxic Deluge | Answers | Kills blocker, protects Lord, or prevents opponent's win; role contested versus main combo. |
| 85 | Training Center | Land | Mana/color choice, life cost, tapped timing or utility opportunity must be tested in turn-two-four hands. |
| 86 | Uncaged Fury | Kill conversion | 2R instant +1/+1 double strike, Lord 11/5 deals 22 commander COMBAT damage if both hits player. |
| 87 | Undead Augur | Fodder/recursion | Death of Zombie you control draws and loses 1 life; Grave loops can kill self unless drain gain offsets. |
| 88 | Underground River | Land | Mana/color choice, life cost, tapped timing or utility opportunity must be tested in turn-two-four hands. |
| 89 | Underground Sea | Land | Untapped typed UB dual. |
| 90 | Vampiric Tutor | Card access | B instant life 2 topdeck any, find protection, suppressor or poison package. |
| 91 | Viscera Seer | Sac outlets/combo | One-mana free sac for scry1 per creature; tutor/control in loops. |
| 92 | Volcanic Island | Land | Untapped typed UR dual, counters/haste colored access. |
| 93 | Warren Soultrader | Sac outlets/combo | Sac creature pay1 life create Treasure; recast Gravecrawler for B via Treasure, needs death payoff/life sustain. |
| 94 | Watery Grave | Land | Fetchable UB shock, can cost life for untap. |
| 95 | Wilhelt, the Rotcleaver | Fodder/recursion | Nontoken Zombie death creates decayed token, endstep token sacrifice can draw; Lord is a Zombie. |
| 96 | Wonder | Haste/evasion/protection | From grave with Island controlled gives all your creatures flying; Lord's ETB may sacrifice it. |
| 97 | Xander's Lounge | Land | Always tapped UBR fetchable land, cycling late. |
| 98 | Zulaport Cutthroat | Death payoffs | On your creature death each opponent loses life and you gain 1, makes Warren life-neutral. |

**Structure, mana and role tension:** 35 lands (33 distinct land names; basics Island ×1, Mountain ×1, Swamp ×3) and eight dedicated artifact mana accelerants. **Exact verified mana permanents:** Arcane Signet, Dimir Signet, Rakdos Signet, Sol Ring, Fellwar Stone, Talisman of Creativity/Dominance/Indulgence; with Nightscape Familiar as generic cost reducer, Phyrexian Tower as land-sac BB. NOTE this source does not include Dark Ritual, Mana Vault, etc.; do not import Grixistax shortcuts. Undercounted protection makes turn-four commander with {U}{B}{R} a reasonable but not automatic payoff; some utility lands produce colorless and Bojuka Bog/Xander's Lounge enter tapped. Shizo grants fear but Lord, itself black, is blockable by any black or artifact creature. Arena can grant haste for the commander with appropriate paid mana; Anger needs actual graveyard + Mountain.

**Functional density:** 5 ETB suppression pieces (Torpor Orb, Karn, Dress Down, Stifle, Tale's End); roughly 11 evasion/haste/protection pieces and 6 ten-power conversion cards (some function in both); recursive fodder from Bloodghast/Skeleton/Nether Traitor/Bitterblossom/Ophiomancer/Jadar/Headless Rider; Gravecrawler as backup recursion engine; removal and permission covering creature and combo. Several other sacrifice bodies increase consistency of the two-creature tax. Disadvantage under opener with no suppression and no fodder: casting Lord sacrifices Lord itself and gives an opponent two cards. The Zombie loop is compact but needs persistent Zombie to cast Gravecrawler and a net-zero-mana route; Ashnod's Altar alone produces colorless, not B to recast Gravecrawler.

## Candidate pool and competing cuts

Engineering `data/grixis/m6/optimizer/lord-of-tresserhorn.json`: 120 Pass A commander-fidelity *projections*, 1 Pass B technical projection; neither is a blind independent critic. The B suggestion `Tribute Mage → Vampiric Tutor` has weak cost and instant-speed coverage, and Tribute Mage's ETB is shut off by Torpor Orb/Karn; reject. Pass A includes many aristocrat substitutions for Sheoldred's Edict, Nether Traitor, Talisman of Creativity and Deadly Rollick. Significant on-plan opportunities were examined against off-ranking alternatives instead of treating rank as mandatory.

| Challenger | Primary cut | Alternative cut | Strategic/payable comparison | Decision |
|---|---|---|---|---|
| **Soul's Fire** (2R instant; your creature deals power to target) | Sheoldred's Edict | Muddle the Mixture | Lord with infect deals 10+ noncombat poison to one opponent through blockers, at instant speed, without sacrificing Lord; with no infect simply 10 life damage. Edict is cheap removal against indestructible/hexproof/hatebears and Muddle tutors Torpor/Phyresis. | **KEEP**, best focused test challenger |
| **Assault Strobe** (R sorcery double strike) | Goblin Bombardment | Uncaged Fury | Under unpumped Lord deals 20 commander damage, **not lethal 21**; if Shadowspear/Slip counter boosts to 11, makes 22 at much lower mana than Fury, but depends on second card or counter and sorcery timing. Bombardment preserves recursion outlet/backup. | KEEP Uncaged Fury and Bombardment |
| **Mask of Memory** | Undead Augur | Mystic Remora | Equip2, triggers on combat-damage to player, draws2 discards1, helping locate poison/protection; but only after Lord connects and lacks immediate kill. Augur feeds Zombie backup and Remora draws under interaction. | KEEP |
| **Fling / Kazuul's Fury** | Sheoldred's Edict | Goblin Bombardment | Sacrifices 10/4 to deal 10 **from the spell**; Fling source lacks infect even if sacrificed Lord had infect. Increases commander tax / risks self-sabotage. | REJECT |
| **Altar of Dementia** | Sheoldred's Edict | Viscera Seer | Free sacrifice for milling equal to power (Lord 10); can supplement Gravecrawler loop mill, but does not kill as reliably as existing blood-drain outlets, and sacrificing Lord disrupts primary kill. | KEEP |
| **Bastion of Remembrance / Chthonian Nightmare** | Sheoldred's Edict | Nether Traitor | Recurrent fodder/life pressure; Bastion tokens and drain useful, but more redundant aristocrat weight displaces instant answer and ETB suppressant plan. Nightmare recursion competes with Torpor/Karn suppression of reentry ETBs. | KEEP |
| **Bloodsoaked Champion / Cult Conscript** | Nether Traitor | Jadar | Recurring one-drops, but don't supply Zombie subtype for Gravecrawler and may require raid/another creature died conditions; Shadow of Nether Traitor offers evasion/fodder upside. | KEEP |
| **Tribute Mage** | Vampiric Tutor | Muddle the Mixture | 3-mana ETB searches MV2 artifact suppression, but Torpor/Karn intentionally blank its own ETB; instant Tutor finds any poison/evasion/land. | REJECT |
| **Aetherflux Reservoir / Aether-artifact combos** | Deadly Rollick | Pitiless Plunderer | Rank outputs push non-Lord spellslinger/alt-win package; four-mana payoff + large storm count, poor fit for Voltron/infect. | REJECT |
| **Whispersilk Cloak / Grafted Exoskeleton** | Brotherhood Regalia / Phyresis | Swiftfoot Boots | Cloak shroud blocks targeting by own Tainted Strike/Igni­tion/Pain; Exoskeleton is expensive to equip and creates sacrifice liability when detached. Approved Regalia and Phyresis much more reliable. | REJECT |
| **Bontu's Monument / Blasting Station** | Talisman of Creativity / Deadly Rollick | Goblin Bombardment | Can help a dedicated Gravecrawler loop but sacrifice-core infrastructure already sufficient and loses early three-color fixing/answer. | KEEP |

**Material weak slots explicitly challenged:** Sheoldred's Edict is the closest movable noncore interaction but premium protection-independent answer; Muddle might appear redundant with Stifle/Tale's End but uniquely transmute-finds two-mana Torpor Orb, Phyresis, Regalia and other MV2 cards; Nether Traitor can demand continuous black mana but is reusable evasive fodder and pairs with sacrifice outlets; Shambling Ghast modest baseline but one mana, Zombie and Treasure on death; Wilhelt is four-mana side engine but turns deaths into fodder; Nightscape Familiar is narrow generic reduction but Zombie and regenerating ETB fodder; Xander's Lounge tapped source and Bojuka Bog tapped disrupt tempo, yet fetchable three-color/trade-off and graveyard interaction respectively; Rogue's Passage expensive colorless but can directly force a 10-poison connection. All deserve role-justified KEEP rather than automatic cutting.

## Oracle, legality and rules

- **Lord 10/4 ETB:** Single trigger `When Lord of Tresserhorn enters...` targeting opponent, not three independent effects. Can respond with Stifle/Tale's End before resolution to avoid **all** three costs. If you have fewer than two other creatures, Lord itself can be sacrificed during resolution. Regeneration does not stop sacrifice. Official Commander legality and UBR recorded PASS in canonical Oct15 full gate; no exceptions.
- **Karn, Argent Defender:** Official WotC *Reality Fracture Release Notes* (`https://magic.wizards.com/en/news/feature/reality-fracture-release-notes`) explicitly states `Artifacts and creatures entering the battlefield don't cause abilities to trigger.` It blanks Lord's trigger if present **as he enters**; as a global effect it also blanks your own artifact/creature-enter-triggered effects, but **not** Shambling Ghast's death trigger or Ophiomancer's beginning-of-upkeep trigger. `Dress Down` removes creature abilities only while in effect; cast it and let resolve **before** Lord enters. Torpor Orb similarly preinstalled. A creature entering while Karn or Torpor active didn't have an ETB trigger put on stack later just because suppressor removed.
- **Combat versus poison:** Infect from Phyresis/Tainted Strike is relevant when Lord DEALS damage, not merely from being controlled. Lord 10 unblocked -> 10 poison lethal. Tainted Strike buffs to 11; Kediss only triggers off Lord's COMBAT damage to one opponent, then **Lord** deals that much NONCOMBAT damage to every *other* opponent. Infect on Lord applies to this damage; **Kediss damage does not increase commander-damage totals against the other opponents** because noncombat.
- **Ignition and Pain:** `Chandra's Ignition` Lord deals power damage to each other creature/each opponent, so infect yields ≥10 poison each if spell resolves with Lord infect and the chosen target remains legal. `Pain for All` costs 2R, enchants a controlled creature, ETB causes it to deal power damage to any *other* target, and second ability when enchanted creature is dealt damage has Lord deal that much to each opponent. Official 2025-07-25 ruling: last ability triggers even if Lord receives lethal damage, and simultaneous multi-source damage triggers once for total damage. Source: `https://mtg.wtf/card/eoe/151/Pain-for-All`; if Lord has infect at time it deals reflected damage, poison is dealt.
- **Damage timing and regeneration:** Regeneration creates replacement shield preventing next destruction and tapping/removing damage/combat; it does not prevent the damage event itself for Pain's trigger. `Blasphemous Act` deals 13 to Lord; can lead Pain to deal 13 to each opponent on a later trigger even if Lord would die, but precise last-known-information/ infect state must be protected at resolution and opponent removal matters.
- **Uncaged Fury:** +1/+1 and double strike gives 11 power and (assuming both damage steps reach player) **22 commander combat damage** for one-shot 21 threshold. Base 10 with simple double strike yields only 20. `Shadowspear` adds +1/+1 and trample/lifelink as separate route for a cheap double-strike candidate.
- **Not of This World:** Counter targets a spell or ability that targets your permanent; **free only if it targets a spell/ability that targets your 7+ power CREATURE** such as Lord; won't free-counter spells not targeting Lord or mass wipes (no targets). Oracle `https://mtg.wtf/card?q=%21Not+of+this+World`.
- **Gravecrawler loop:** With Lord or another Zombie on board, Gravecrawler can be cast from grave for B. `Phyrexian Altar` sacrifice produces B; pay B to recast indefinitely under no disruption, with Blood Artist/Zulaport/Diregraf Captain/Bombardment payoff (Bombardment as outlet changes mana requirements). `Ashnod's Altar` produces CC, not B; to loop by itself requires `Rooftop Storm` making Gravecrawler cost 0, or other colored converter. `Warren Soultrader` costs 1 life and sacrifices Gravecrawler to create Treasure for B recast; with Zulaport each death returns 1 life, so life-neutral; opponent interaction can break any loop. No fake infinite loop without Zombie/outlet/payoff.
- **Anger and Wonder:** Need in YOUR graveyard with Mountain or Island respectively; can be sacrificed during Lord ETB but that simultaneously imposes another required sacrifice. If suppressing Lord ETB, have to discard/sac them via a different route. `Shizo` fear is weaker versus black/artifact blockers; `Brotherhood Regalia` can be stronger, while `Lightning Greaves` shroud blocks your own Lord-targeted finishers unless moved.
- **Mana/legal:** 35 lands 33 unique land names, one commander, no banned exceptions in canonical gate. No wholesale fresh 100-name legality query on Oct19; do not claim current official legality stronger than verified gate and spot Oracle research.

## Finite sequencing and adversarial scenarios

All conditional **manual stack/payment/board-state traces** (not simulated win percentages). Each scenario records a relevant opponent disruption or low-ceiling state.

1. **Turn-four Lord without suppression/fodder:** pay 1UBR for 10/4, trigger on stack; when it resolves with no other two creatures, sacrifice Lord itself and lose two life while targeted opponent draws two. This makes an unprepared fast Lord actively negative.
2. **Turn-two Torpor into Lord:** cast 2-mana Orb before 1UBR Lord, if still in play as Lord enters ETB does not trigger. Opponent destroying Orb in response to Lord on stack removes prevention; drawback triggers as Lord resolves. Cannot wait until after trigger to flash Orb to erase existing trigger.
3. **Stifle versus counterspell:** cast 1UBR Lord with U held open; triggered ability on stack, target opponent chosen. Cast U Stifle, it counters entire ETB cost if resolves. Opponent countering Stifle still leaves obligation; regenerating Lord doesn't prevent sacrifice.
4. **Karn parity:** two-mana Karn in play blanks Lord ETB but also opponent ETBs; removing Karn while Lord spell on stack reinstates trigger when Lord enters. Karn does not prevent token creation at beginning-of-upkeep since these aren't creatures entering triggers? `Ophiomancer` triggers at beginning of upkeep, not because a creature ENTERS; its trigger can create a Snake normally.
5. **Unsuppressed fodder:** with Bitterblossom Faerie and Gravecrawler field as two OTHER creatures, Lord ETB sacrifices both, loses2 and feeds two opponent draws; Gravecrawler from grave can be recast if Lord survived Zombie source with B. Lord's presence enables secondary recovery; poor plan if opponent benefits from draw.
6. **Anger haste:** with Anger and another body on field, Lord ETB makes you sac Anger and the other; if Mountain controlled, haste applies once Anger in grave when trigger ends. Without other body Lord sacrificed too; if Torpor prevents trigger Anger remains on battlefield and doesn't grant haste automatically.
7. **Basic infect:** Lord 10/4 + Phyresis (1B), evade via Regalia/Shizo, unblocked combat gives target opponent ten poison. Opponent can remove Phyresis or Lord before damage; poison is not commander damage (though combat damage would also qualify as combat commander damage tracking), so win derives from poison.
8. **Instant Tainted Strike:** declare 10/4 attack, blockers declared none, cast B Tainted Strike, Lord becomes 11/4 infect, damage 11 poison lethal. If Greaves equipped shroud, can't target Lord; moving Greaves to different creature before window might restore targetability but costs suitable target.
9. **Kediss table kill:** Lord infect hits opponent A for10, Kediss trigger uses Lord to deal 10 NONCOMBAT poison to B and C. If Kediss is removed in response to damage? Its trigger already on stack persists; if Lord removed before resolution, Lord's last known traits as source may apply, but this detailed contingency needs judge-grade verification and should not be overstated. Noncombat propagation is NOT 21 commander damage.
10. **Chandra's Ignition:** pay 3RR targeting Lord with infect, Lord survives until resolution, deals10 infect to all opponents and all other creatures. Opponent kills Lord in response -> spell's only target invalid, no spell resolution. The active attack shell must reserve protection.
11. **Pain for All ETB:** pay 2R Aura, attach Lord; ETB triggers targeting opponent; response cast B Tainted Strike before ETB resolves, Lord now 11 power infect, deals 11 noncombat infect to targeted player. Target must still be legal and Lord must remain attached. If target is removed or hexproof granted to target, ETB can fail.
12. **Pain + Blasphemous Act:** with Aura on Lord and Act costing appropriately reduced 8R, Act deals13 to Lord, Pain reflects13 to each opponent via trigger; Lord may die absent regenerate but damage event still triggers. With infect prior to reflection, can give13 poison subject to source/last-known ruling; do not claim Lord survives without B regeneration.
13. **Uncaged Fury unblocked:** Lord 10/4, cast 2R Fury before first-strike damage, gains +1/+1 and double strike; 11 first-strike commander damage plus 11 normal =22, lethal. Opponent can remove Lord after first strike and before normal, leaving just 11, so must defend both damage steps.
14. **Assault Strobe challenger:** base Lord gets double strike from R sorcery, only 20 commander damage. With Shadowspear equipped Lord 11/5 then 22. If no secondary buff available, Fury has better solo-one-card lethality in 10-power plan.
15. **Soul's Fire challenger:** with Lord 10 and Phyresis, pay 2R instant and target opponent, Lord deals10 noncombat infect (no combat needed); can respond after blocks. If only Soul's Fire with normal Lord, deals10 normal life damage, cannot independently kill typical 40-life opponent. Opponent can remove Lord in response (the source creature targeted), so downside similar to Ignition but cheaper.
16. **Gravecrawler+Altar:** Lord Zombie on board; Phyrexian Altar + Gravecrawler from grave, sacrifice Gravecrawler for B, spend B recast, repeat; with Zulaport/Blood Artist drain, finite arbitrarily many legal iterations if every opponent can't disrupt. Lord in grave instead -> no controlling Zombie unless other Zombie present; loop not live.
17. **Ashnod alone failure:** sacrifice Gravecrawler produces CC, but colored B needed to recast; without Rooftop Storm or colored converter, no loop. Projection ranking of generic sacrifice mana is misleading if costs not actually paid.
18. **Warren Soultrader life budget:** pay1life and sac Gravecrawler for Treasure B; cast from grave for B and repeat, costs 1 life every iteration. Zulaport gain1 makes life-neutral; without life gain can only repeat fewer times than remaining life permits, Blood Artist typically heals you for 1 but targets a single player, so sequencing matters.
19. **Torpor negative:** Karn/Torpor also suppress some own ETB creatures; source package heavily relies on death/on-upkeep/landfall more than ETB to break parity. Grave recursion still works with Gravecrawler cast and Jadar end-step.
20. **Removal timing:** opponent casts exile on Lord in response to Phyresis or Ignition; Not of This World may be FREE if spell targets Lord with power >=7, but doesn't counter an opponent's untargeted Toxic Deluge; Slip Out the Back phases Lord, saves him but also fizzles your current Ignition/attachment plan.
21. **Mana source adversary:** hands with Rogue's Passage, Bojuka Bog and one Signet may be short U/R for Lord by t4; removal of single mana rock can strand Stifle shield. Compare replacing colorless utility rather than assuming 35 lands means early UBR guaranteed.

## Conclusions and unresolved evidence

**KEEP current exact 100-card approved and locked baseline unchanged.** Strongest challenger **Soul's Fire vs Sheoldred's Edict** merits focused paid mana/board interaction tests because it extends infect lethal damage through blockers at only 2R while keeping Lord alive; key downside is loss of cheap reliable edict answer and requirement to draw or maintain infect Lord. Second challenger **Assault Strobe** becomes effective only with separate +1 power (Shadowspear/Slip Out counter), whereas Fury supplies self-contained +1. Neither presently establishes a strict net improvement across meaningful pods. No upgrade automatically applied; no final deck modification/authorization.

**Open evidence:** effect-aware paired tests of ready-to-cast suppressor+Lord and poison conversion, critical-mana source hands, survival through removal, opponent response to Aura/stack, and Soul's Fire frequency. Most M5 Pass A candidates overweight sacrifice engines at expense of Voltron identity; Pass B lone Tribute Mage fails suppression conflict. Manual scenarios above are not simulations or measured performance, and no broad 2026-10-19 Scryfall bulk pass was executed. This authored review does not qualify independent GrokBot Pass C, complete M6, approve proposed swaps, or overwrite canonical locks.

## Source and test receipts

- Canonical approved state and exact approved list `state/current_deck_overrides.json`, `refinement/decklists/Lord_of_Tresserhorn_Approved_2026-10-14.txt`, SHA256 `95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e`.
- Historic complete gate `refinement/verification/lord_of_tresserhorn_2026-10-14/gate_output/Lord_of_Tresserhorn_2026-10-14_Complete_Gate.json` and decisions `refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md`; spot 2026 WotC Karn text `https://magic.wizards.com/en/news/feature/reality-fracture-release-notes`.
- Engineering `AGENTS.md`, `grixis/M6 Commander-First Single-Deck Review Standard.md`, `data/grixis/m6/single_deck_depth_tracker.json`, `data/grixis/blueprints/lord-of-tresserhorn.json` and `data/grixis/m6/optimizer/lord-of-tresserhorn.json` with Pass A 120, Pass B 1.
- Focal Oracle sources `https://mtg.wtf/card/eoe/151/Pain-for-All`, `https://mtg.wtf/card?q=%21Not+of+this+World`, `https://mtg.wtf/card/sld/2364/Kediss-Emberclaw-Familiar` and 2025/2020 rulings; official Karn 2026 release notes, all interpreted separately from 2026 approved legality cache.
- Independent source-row recount: 98 export rows, 100 physical cards, 98 unique names, 35 lands, only Swamp ×3 repeats, one commander; name-by-name audit above.
- Cases 1–21 are authored/manual adversarial sequencing only; no new stochastic trials, measured win-rate, effect-aware paid simulation, reviewer certification or deck mutation. CI must succeed on review and tracker exact commits before ledger advancement.
