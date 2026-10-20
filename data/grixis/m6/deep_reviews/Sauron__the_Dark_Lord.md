# M6 Comprehensive Commander-First Single-Deck Review #50 — Sauron, the Dark Lord

**Deck:** `Sauron__the_Dark_Lord`, canonical tracker index 49 of 62. **Author:** ChatGPT, 2026-10-20; first-party authored M6 deep pass, **NOT GrokBot's independent Pass C**. **Judgment:** `KEEP` the exact approved canonical list. No automatic swaps, unlocking, changes, or milestone acceptance.

## Authority and reproducibility

- Engineering: `corymstover/GrokBotMTGCompanion`, integration `chatgpt-cycle76-m6-refinement`; read `AGENTS.md`, single-deck standard, registry, M6/M7 subtracker, depth tracker (49 complete before this review), `data/grixis/m6/review_packets/sauron-the-dark-lord.json` (31 ranked candidate pairs), `data/grixis/blueprints/sauron-the-dark-lord.json`, `data/grixis/mana_base/sauron-the-dark-lord.json`, `grixis/interactions/sauron-the-dark-lord.md` (5 verified Oct16 interaction groups).
- Canonical: `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json#decks.Sauron__the_Dark_Lord`: approved and locked Oct15 2026; source `refinement/decklists/Sauron_the_Dark_Lord_Approved_2026-10-15.txt` Git blob `b714245307cf48d60a4a021e7e8f0815670f9c17`; canonical Oct15 candidate decision, 99-copy whole-list audit and approval-ready gate.
- **Immutable canonical SHA-256:** `fab194f69a6e15b83679c1419f88ba6fdd56cd9527946cb94a6d8efe23a7dfc8`; engineering logical fingerprint `lh1:bbac35497c11953c26540c28d14d51eb101a8ac86a915fe12b4c6aaba796594a`. Historical exported TXT in interaction doc has a different SHA, NOT the current approval source; do not conflate.
- Source Oracle/rules verification was against Scryfall bulk 2026-10-16, rulings 2026-10-15 and Commander CR effective 2026-09-25 as documented in the M1 interactions; canonical targeted October15 Oracle/legality gate passed. **No new live October20 bulk Oracle or banned-list execution claimed**, so any future unexpected legality change requires targeted refresh. Project exceptions: none; **Nazgûl x7 is officially permitted by the card's own nine-copy deck-construction rule**, not a house exception.
- Independent hand-executed parsing/recount of exact approved TXT: **100 physical cards, 99 library cards, 91 distinct names, 34 lands**. All repeated names exactly `Mountain x2; Nazgûl x7; Swamp x3`; Nazgûl's own construction exception + basic-land multiplicity only, no other duplicates; all included cards U/B/R or colorless on source audits, no explicit project exception. No MDFCs. Commander's cost {3}{U}{B}{R}, MV6, color identity UBR. Power ceiling Bracket 4 — Optimized. Archidekt tags Amass Orcs / Ring Temptation / Wraiths.

## Identity, engine and protection boundary

The commander turns **other players casting spells** into an expanding Orc Army. The Army deals **combat damage to a player** → the Ring tempts you → each temptation enables the commander to optionally **discard your entire hand to draw four** and triggers each Nazgûl's Wraith-wide +1/+1-counter effect. This is a multiplayer reactive growth engine, not spellslinger/self-cast amass like Saruman or the ETB/reanimation plan of the other Sauron. Opponent casts rather than resolves are sufficient for the amass; quiet/passive or creatureless opponents can suppress growth. The deck's small Nazgûl contingent, recurrent Ring temptations, and evasion work even if commander is temporarily unavailable; the commander is nevertheless essential to high card flow and repeated amass.

**Protected slots:** Sauron, Nazgûl x7, Call of the Ring, Minas Morgul shadow/Wraith bridge, Roaming Throne, Great Goblin trample, Mauhúr/The Great Goblin counter triggers, sufficient UBR fixing, and free protection for a six-drop. Do **not** silently substitute generic Oracle/Consult/Breach/Thoracle turbo goodstuff: a higher generic win-rate shell is not a stronger *Sauron* encyclopedia entry. The alternative lord-of-Rings named Sauron is deliberately a costly thematic redundancy, not evidence of turbo competitiveness.

## All 100 physical slots: individualized audit

This is an independently reconstructed per-approved-row accounting. `LAND` entries total 34; quantity lines explicitly preserve repeated basics and seven Nazgûl. Each audit line includes whether it directly advances identity, fills infrastructure, or presents an opportunity cost.

| TXT line | Qty | Exact approved card | Role | Reason and limitation |
|---:|---:|---|---|---|
| 1 | 1 | Sauron, the Dark Lord | CMD | 3UBR commander; opponent casts grow Army, Army combat connects tempt Ring, every temptation optional discard hand/draw four; ward sacrificing legendary creature/artifact |
| 2 | 1 | Ancient Tomb | LAND | Untapped CC at cost two life; accelerates six-mana commander but produces zero UBR pips |
| 3 | 1 | Anger | RECUR | Graveyard haste with Mountain; Entomb/looting useful; hard-casting without grave outlet inefficient |
| 4 | 1 | Animate Dead | RECUR | Cheap reanimation for Nazgûl/large support creature; weak to graveyard or enchantment hate |
| 5 | 1 | Arcane Signet | RAMP | Two-mana untapped rainbow mana constrained to identity; excellent triple-colored casting support |
| 6 | 1 | Archfiend of Ifnir | PAYOFF | Own hand discard puts -1/-1 counters on opposing board; 5-mana setup but converts commander wheel into control |
| 7 | 1 | Badlands | LAND | Untapped Swamp Mountain typed BR; fetch target and Anger source, no U |
| 8 | 1 | Barad-dûr | LAND | B utility, creature-death-gated amass activation; activation is not opponent spell cast and requires tempo |
| 9 | 1 | Bilbo, Retired Burglar | VALUE | Combat/Ring flavor piece with lower direct impact than Nazgûl/Army engines; candidate soft cut only when tested |
| 10 | 1 | Black Market Connections | ENGINE | Upkeep modes draw/Treasure/changeling with life payment; flexible resource-and-creature engine, NOT empty simulator slot |
| 11 | 1 | Blasphemous Act | SWEEP | Cheap if creature count high; hits own Sauron, Nazgûl and Army, important board reset liability |
| 12 | 1 | Blood Crypt | LAND | BR typed shock, fetched for black/red; Mountain enables Anger; untapped two-life cost |
| 13 | 1 | Bloodstained Mire | LAND | Fetch Swamp or Mountain type for one life, including typed multicolor duals |
| 14 | 1 | Call of the Ring | CORE | At each upkeep Ring tempts independent of Army hit; feeds all Nazgûl and Sauron draw option; two-mana indispensable trigger redundancy |
| 15 | 1 | City of Brass | LAND | Flexible untapped UBR fixing at life/damage cost |
| 16 | 1 | Claim the Precious | INTERACT | Targeted kill plus Ring temptation on resolution; mana three, stronger than generic kill when source survives |
| 17 | 1 | Command Tower | LAND | Untapped perfect UBR colored source |
| 18 | 1 | Force of Will | PROTECT | Pitch another blue card plus one life or hard pay; free stack interaction preserves six-mana investment |
| 19 | 1 | Cyclonic Rift | INTERACT | 1U bounce or 6U overload to clear opponent blockers/hate; seven-mana mode slow |
| 20 | 1 | Dark Ritual | RAMP | Single B -> BBB burst; accelerates commander only if U and R otherwise available |
| 21 | 1 | Deadly Rollick | INTERACT | Creature exile free with commander, 3B otherwise; critical protection against blockers and creature combo |
| 22 | 1 | Deflecting Swat | PROTECT | Free with commander for targeted stack spells/abilities; no protection from untargeted wipes |
| 23 | 1 | Demonic Tutor | TUTOR | 1B fetch any needed engine or answer into hand, strong flexibility not thematic replacement |
| 24 | 1 | Minas Morgul, Dark Fortress | LAND | Tapped B with 3B,T shadow-counter to give Army shadow plus Wraith status, uniquely converts Nazgûl growth into connection |
| 25 | 1 | Entomb | TUTOR | Instant tutor directly graveyard: Wonder/Anger/reanimation; not a card-to-hand tutor |
| 26 | 1 | Exotic Orchard | LAND | Opponents' land colors conditionally permit any UBR, poor reliability versus atypical mana |
| 27 | 1 | Feed the Swarm | INTERACT | Creature/enchantment removal, pays life; key answer to problem enchantments in black |
| 28 | 1 | Mana Vault | RAMP | One-mana CCC burst, permits faster Sauron, no colored pips; upkeep/life and untap tax |
| 29 | 1 | Fierce Guardianship | PROTECT | Noncreature counter free while commander controlled; protects engine from wipe/combo |
| 30 | 1 | In the Darkness Bind Them | THEME | High-mana saga, Ring/Army storyline and ongoing value; weak when already behind and no accessible clock |
| 31 | 1 | Island | LAND | One blue basic, Island condition for Wonder and basic-land resilience |
| 32 | 1 | Misty Rainforest | LAND | Fetch Island/Forest types for one life, including Island-typed Grixis duals |
| 33 | 1 | Jeska's Will | RAMP | Mana red / exile access with commander, opponent hand size variable; cannot supply U/B alone |
| 34 | 1 | Living Death | RECUR | Board grave exchange; reanimates Nazgûl but destroys existing Sauron board and revives enemy threats |
| 35 | 1 | Luxury Suite | LAND | BR partner land untapped at ordinary 4-player table; conditional smaller pods |
| 36 | 1 | Mana Confluence | LAND | Any color on demand at one life cost per colored mana |
| 37 | 1 | Mana Drain | PROTECT | UU answer, later adds generic mana in main phase; colored challenge vs UBR |
| 38 | 1 | March from the Black Gate | THEME | Army attack-enhancing thematic payoff; payoff dependent on connecting and board state |
| 39 | 1 | Marsh Flats | LAND | Fetch Plains/Swamp typed lands, including black-producing duals and typed triome |
| 40 | 1 | Mauhúr, Uruk-hai Captain | CORE | Adds ONE counter to each eligible counter-placement event on Army/Orc/Goblin, not per counter |
| 41 | 1 | Moria Scavenger | VALUE | Orc combat and card/graveyard value; weaker versus no-block/combo but supports army identity |
| 42 | 1 | Morphic Pool | LAND | UB multiplayer untapped conditional dual |
| 43 | 1 | Mount Doom | LAND | BR and legend-sacrifice/destructive utility modes; ability has real resource cost |
| 44 | 2 | Mountain | LAND | Two red basics, enable Anger and resist nonbasic denial; physical qty counted |
| 45 | 1 | Mystic Remora | DRAW | Upkeep cumulative-cost tax engine when opponents cast noncreature spells; strong in stack-heavy pods |
| 46 | 1 | Mystical Tutor | TUTOR | Instant/sorcery to top, NOT an artifact/creature finder for Roaming Throne |
| 47 | 7 | Nazgûl | CORE | Seven legally repeatable Wraiths: ETB Ring temptation; each creature independently puts +1/+1 on each Wraith for each Ring temptation |
| 48 | 1 | Roaming Throne | CORE | Choose Avatar to double Sauron triggers OR Wraith to double Nazgûl triggers; one chosen type, not both |
| 49 | 1 | Orcish Bowmasters | INTERACT | Draw punishment and independent Army creation when Sauron absent; needs draw events |
| 50 | 1 | Orcish Siegemaster | THEME | Orc/Army combat enhancement, backup to shadow/trample, variable against pillow-fort |
| 51 | 1 | Otawara, Soaring City | LAND | U or channel to bounce threat; channel is not casting |
| 52 | 1 | Polluted Delta | LAND | Fetch Island/Swamp type, often U/B plus colored typed dual |
| 53 | 1 | Reanimate | RECUR | B resurrect creature with MV life cost, own or opponents' graveyard; Army token never grave card |
| 54 | 1 | Relic of Sauron | RAMP | Four-mana rock plus filtering thematic, comparatively slow, but offers UBR and discard enabling Anger/Wonder |
| 55 | 1 | Rhystic Study | DRAW | Three-mana opponent-tax draw engine supports hand fuel and interaction; not independently Ring engine |
| 56 | 1 | Ringsight | TUTOR | Ring tempts then conditional shared-color tutor with legendary creature; cannot tutor colorless Roaming Throne even with Sauron UBR |
| 57 | 1 | Rogue's Passage | LAND | Colorless mana; four plus tap to make Army unblockable, helps Army hit at material tempo cost |
| 58 | 1 | Saruman, the White Hand | THEME | Amass on own noncreature spells based on stack MV; partial independent Army generator, four-mana setup |
| 59 | 1 | Saruman's Trickery | PROTECT | Themed countermagic with targeting and costs that must be respected; role redundant with other stack answers |
| 60 | 1 | Sauron, Lord of the Rings | THEME | Eight-mana alternative Sauron/Army + graveyard payoff, flavorful but expensive compared with commander |
| 61 | 1 | Sauron's Ransom | DRAW | Instant political opponent choice and card selection, non-guaranteed best cards; draw-support tempo |
| 62 | 1 | Scalding Tarn | LAND | Fetch Island/Mountain types; color reaches typed duals |
| 63 | 1 | Sheoldred, the Apocalypse | PAYOFF | Own Sauron draw4 gains life / opponents' draws penalized; generic but helps long game and pressure |
| 64 | 1 | Sol Ring | RAMP | One-mana CC acceleration, no UBR pip |
| 65 | 1 | Steam Vents | LAND | Typed UR shock, Wonder/Anger support, two-life optional untapped |
| 66 | 1 | Volcanic Island | LAND | Untapped Island Mountain dual fetched by many and supports both Wonder and Anger |
| 67 | 1 | Summons of Saruman | THEME | Variable X-cost amass / graveyard spell access; chosen X and timing require real paid mana |
| 68 | 3 | Swamp | LAND | Three black basics, support early black Ring/recursion and resist nonbasic hate |
| 69 | 1 | Swan Song | PROTECT | U instant counter for enchantment/instant/sorcery, leaves 2/2 bird, cannot counter creature |
| 70 | 1 | Talisman of Creativity | RAMP | Two-mana UR fixation; colored activations cost one life |
| 71 | 1 | Talisman of Dominance | RAMP | Two-mana UB fixation; vital black-heavy early turns |
| 72 | 1 | Talisman of Indulgence | RAMP | Two-mana BR fixation; supports Mauhúr and commander |
| 73 | 1 | The Black Gate | LAND | Color/utility land provides targeted anti-blocker opponent route if conditions met; not blanket unblockability |
| 74 | 1 | The Great Goblin | PAYOFF | Deals two on each qualifying counters-being-placed event, NOT two per counter; damage scales with trigger frequency |
| 75 | 1 | The One Ring | DRAW | Legendary artifact protection if cast and compounding draw from burden counters, life costs and anti-legend ward resource |
| 76 | 1 | The Ozolith | PROTECT | Stores +1/+1 counters when creature leaves, NOT its body; moves counters at combat start |
| 77 | 1 | Toxic Deluge | SWEEP | Life-paid scalable board wipe can selectively spare larger Army, kills Nazgûl if X≥toughness |
| 78 | 1 | Training Center | LAND | UR multiplayer dual, conditionally untapped |
| 79 | 1 | Flooded Strand | LAND | Fetch Plains/Island type including Island duals, not arbitrary UBR land |
| 80 | 1 | Underground Sea | LAND | Untapped Island Swamp dual for blue/black, Wonder support and fetching |
| 81 | 1 | Urborg, Tomb of Yawgmoth | LAND | Each land is Swamp additionally, black fixes otherwise colorless lands, also helps opponents |
| 82 | 1 | Vampiric Tutor | TUTOR | B and two life any-card to deck top, find missing combat bridge with draw delay |
| 83 | 1 | Victimize | RECUR | Sac creature then return two creatures tapped; small creature as sacrifice preferable to active Army/Nazgûl |
| 84 | 1 | Great Goblin, Foul-Hearted | CORE | Five-mana enters and attacks to amass Goblins3 onto Army, adds trample to all Armies, commander-tempts when Army damages player |
| 85 | 1 | Watery Grave | LAND | Typed UB shock, supports Wonder and early black requirements |
| 86 | 1 | Wheel of Fortune | DRAW | Two R + discard hand/draw seven symmetrical to opponents, triggers hand-discard payoffs at card cost |
| 87 | 1 | Widespread Brutality | SWEEP | Amass Zombies2 then Army deals its power to all NON-Army creatures, INCLUDING own Sauron and Nazgûl |
| 88 | 1 | Windfall | DRAW | All players discard then draw largest discarded size, strong with Archfiend/Sheoldred/Bowmasters but helps opponents |
| 89 | 1 | Witch-king of Angmar | CORE | Nazgûl-scaling Wraith legend with combat tax and menace-like evasion, high MV threat |
| 90 | 1 | Wonder | RECUR | Graveyard flying to creatures only when control Island; must enter graveyard via Entomb/discard |
| 91 | 1 | Xander's Lounge | LAND | Tapped typed UBR cycling triome, excellent fetch target but tempo cost |

### Structural implications and weakest-slot adversarial audit

**Early mana.** Exact approved list has 34 lands, zero MDFCs, six fetches (Bloodstained Mire, Flooded Strand, Marsh Flats, Misty Rainforest, Polluted Delta, Scalding Tarn), Sol Ring, Mana Vault, Signet, three Talismans and a single ritual Dark Ritual. Colored-source evidence in `data/grixis/mana_base/sauron-the-dark-lord.json`: nominal land U17/B21/R16; incl repeatable rocks U21/B25/R20. Black pips dominate early spell demand (~52% raw colored pip equivalents). 3UBR costs SIX total and all three colors; a turn-three Sauron requires exceptional Vault/Ritual opening and does not imply turn-three consistent casting. Source no-mulligan chance of four natural land drops by turn4 ~0.563, and all-three-color land-source *presence* by turn4 ~0.767; they are not joint probabilities of castability. T5 fifth land drop ~0.394. Nine conditional-tapped and one unconditional tapped land can cause an additional tempo loss not represented by source-presence proxies.

**Weak/conditional candidates, not automatically cuts:** Bilbo (combat-only contribution vs Nazgûl density), In the Darkness Bind Them (multi-turn saga at high mana cost), Relic of Sauron (four-mana rock), Sauron, Lord of the Rings (eight-mana redundant top end), Moria Scavenger (conditional combat recursion), Witch-king of Angmar (large but protective Wraith), Archfiend of Ifnir (five-mana discard payoff), Saruman the White Hand (requires own noncreature spell casts), Sauron's Ransom (opponent-choice access), and Rogue's Passage (colorless + high activation). Their strongest keep-side arguments are meaningful thematic redundancy, Ring/Army bridge, broader game-state coverage or UBR consistency. The correct comparison is **candidate vs particular cut**, not candidate card quality in isolation.

**Interaction and protection:** Free Force of Will (requires OTHER blue card and 1 life), Fierce Guardianship, Deflecting Swat, Deadly Rollick preserve tapping out for Sauron. Mana Drain, Swan Song, Saruman's Trickery, Cyclonic Rift, Feed the Swarm, Claim the Precious, Bowmasters, Toxic Deluge and Blasphemous Act address diverse vectors. Sweepers can reset **own** Nazgûl/commander; Widespread Brutality specifically hits ALL non-Army creatures on both sides, not all enemy creatures only. Omitting free exile removal for an eight-mana engine is an asymmetric downside. Graveyard recursion Reanimate, Animate Dead, Victimize, Living Death and Entomb makes repeat creatures resilient but does not retrieve Army token and suffers graveyard exile. The Ozolith preserves counters but cannot retain an Army body. Protection from a targeted spell/ability is not immunity to combat or sacrifice-boardwipe effects.

**Card velocity and win conversion:** Sauron's optional discard-to-four, Call's Ring temptation, Wheel, Windfall, Connections, Rhystic, Remora, The One Ring, Ransom and tutors supply access; players should frequently decline Sauron's trigger with a hand of four+ good cards or to preserve timed counterspells. Nazgûl x7 converts each fresh Ring event into **up to seven separate Wraith counter placements** only when all seven are on battlefield; the list starts with none. Evasion across shadow, unblockability, trample, flying and The Black Gate converts large Army into damage/temptations, but blockers, pillowfort, exile and graveyard hate change the clock. True deck power is strong optimized multiplayer engine (Bracket4) but lacks a source-proven compact deterministic victory; not cEDH by assertion.

## All 31 M5 candidate routes: add/cut adjudication

The paired M5 screening packet is evidence of **test coverage**, NOT owner-approved changes or an oracle-correct multiplayer evaluator. Its 31 candidates span 2 independent-agreement P0, 6 performance-only P1 and 23 commander-fit-only P3 hypotheses: 8 test passes, 6 fails, 9 inconclusive, 7 no-detectable-difference and 1 without a test. Most test artifacts only simulate whether a swapped card is castable; many incumbent cards (Call, Deadly Rollick, Connections, Remora) have **no effect modeled**, while a replacement mana source/draw action is modeled. Positive sign can invert after modeling Ring and opponents.

| # | Add | Proposed cut | Source priority | M5 result | Authored verdict, alternative cut and mechanism |
|---:|---|---|---|---|---|
| 1 | Marina Vendrell's Grimoire | Call of the Ring | independent_agreement | pass | HOLD. P0 draw candidate appears to pass only when its draws are modeled and Call's automatic temptations + Sauron draw4 are modeled as blank. Do not cut Call. Alternative Wheel cut loses cheap refill, check tempo before any future proposal. |
| 2 | Tidespout Tyrant | Deadly Rollick | independent_agreement | pass | HOLD. P0 expensive bounce engine has nontrivial payoff after spell casts, but deleting free exile Deadly Rollick worsens protected commander deployment. M5 models neither effect. Alternate large Sauron cut sacrifices flavorful backup and may still not fund Tyrant. |
| 3 | Inherited Envelope | Black Market Connections | measured_performance_only | pass | HOLD. Ring-centric mana piece playable, but three-mana ramp costs entire setup turn, while Black Market Connections produces cards/Treasure/changeling; alternative Relic of Sauron cut compromises on-theme red/blue/black fixing. |
| 4 | Worn Powerstone | Black Market Connections | measured_performance_only | pass | HOLD. Enters tapped and generates only CC from subsequent turns, losing Connections modal draw/colored Treasure; goldfish pass not tactical. |
| 5 | Dimir Signet | Black Market Connections | measured_performance_only | pass | HOLD. Attractive two-mana UB rock, but Connections repeatable black-heavy selection and Treasure dominates longer; alternative Relic cut might lower curve yet trades late filtering. |
| 6 | Rakdos Signet | Black Market Connections | measured_performance_only | pass | HOLD. BR fixing only, insufficient alone for commander U; loses Connections engine. Requires better-colored-mana evidence. |
| 7 | Phial of Galadriel | Black Market Connections | measured_performance_only | pass | HOLD. Flavorful hand-size/mana utility, but slower 3-mana than two-mana rocks; Connections has independent card selection. Modeled pass is biased. |
| 8 | Izzet Signet | Black Market Connections | measured_performance_only | pass | HOLD. UR two-mana fixing can help Sauron but does not fulfill black demand and displaces flexible Connections; not established. |
| 9 | Underworld Breach | Mystic Remora | commander_fit_only | fail | REJECT both proposed cuts Remora/Brutality. Escape recursion is powerful but no payable deterministic kill here; card exile consumption and generic combo drift; Remora's pressure and Army-native wipe matter. |
| 10 | Underworld Breach | Widespread Brutality | commander_fit_only | fail | REJECT both proposed cuts Remora/Brutality. Escape recursion is powerful but no payable deterministic kill here; card exile consumption and generic combo drift; Remora's pressure and Army-native wipe matter. |
| 11 | Lich | Wheel of Fortune | commander_fit_only | fail | REJECT replacing Wheel/Call. BBBB and life-total setting build a risky alternative shell, worsens Ring throughput and commander draw synergy. |
| 12 | Peer into the Abyss | Wheel of Fortune | commander_fit_only | fail | REJECT replacing Wheel/Call. Seven-mana halved-life giant burst competes with six-mana commander, loses consistent Ring triggers or wheel; not source-paid early. |
| 13 | Reiterate | Sauron's Ransom | commander_fit_only | fail | REJECT Ransom cut. Buyback spell-copy does not itself generate mana and no demonstrated profitable target engine; Ransom gives immediate access. |
| 14 | Nefarious Lich | Wheel of Fortune | commander_fit_only | fail | REJECT replacing Wheel/Call. Extremely fragile life/exile replacement and lost-game downside when leaves battlefield, disconnected from Army/Ring. |
| 15 | Lord of the Nazgûl | Deflecting Swat | commander_fit_only | not run | HOLD thematic alternative, NOT replacing free commander-protecting Deflecting Swat. Triggers on own instants/sorceries vs Sauron's opponents' casts; possible Bilbo cut worth future combat-speed test. |
| 16 | Fall of Cair Andros | Deadly Rollick | commander_fit_only | inconclusive | HOLD, NOT replacing Deadly Rollick. More on-theme board damage-to-amass in creature tables; requires excess noncombat damage and expensive activation; alternate slow saga cut more comparable. |
| 17 | Witch-king, Bringer of Ruin | Witch-king of Angmar | commander_fit_only | inconclusive | HOLD. Compare to Witch-king of Angmar only with known table attacker/blocker environment; one-for-one Wraith slot changes deterrence and scaling, no proven upgrade. |
| 18 | Toralf, God of Fury // Toralf's Hammer | Deadly Rollick | commander_fit_only | inconclusive | REJECT Rollick cut. Excess noncombat damage payoff demands expensive damage spells and board targets, loses free exile removal and protection. |
| 19 | Requiem Monolith | Call of the Ring | commander_fit_only | inconclusive | BLOCKED pending authoritative Oracle/current legality and representative activations; its cuts Call or Wheel dismantle immediate engine, not justified by model. |
| 20 | Requiem Monolith | Wheel of Fortune | commander_fit_only | no_detectable_difference | BLOCKED pending authoritative Oracle/current legality and representative activations; its cuts Call or Wheel dismantle immediate engine, not justified by model. |
| 21 | Marina Vendrell's Grimoire | Wheel of Fortune | commander_fit_only | no_detectable_difference | HOLD. P0 draw candidate appears to pass only when its draws are modeled and Call's automatic temptations + Sauron draw4 are modeled as blank. Do not cut Call. Alternative Wheel cut loses cheap refill, check tempo before any future proposal. |
| 22 | Mind Over Matter | Black Market Connections | commander_fit_only | no_detectable_difference | REJECT Connections cut. UUUU + discard-to-untap engine with no documented finite profitable untap loop, loses black modal value. |
| 23 | Lich | Call of the Ring | commander_fit_only | no_detectable_difference | REJECT replacing Wheel/Call. BBBB and life-total setting build a risky alternative shell, worsens Ring throughput and commander draw synergy. |
| 24 | Worldgorger Dragon | Toxic Deluge | commander_fit_only | inconclusive | REJECT Toxic Deluge cut. Animate Dead + Dragon can produce an unbounded exile/return loop and repeated mana if lands profitably tap, but without accessible instant-speed win outlet can force a draw; removes vital wipe, generic combo drift. |
| 25 | Hullbreaker Horror | Deadly Rollick | commander_fit_only | inconclusive | HOLD, not Rollick cut. Flash/protection + cast-to-bounce can dominate with rocks, but eight-mana creature and multiple spells needed; shouldn't sacrifice zero-mana removal. |
| 26 | Peer into the Abyss | Call of the Ring | commander_fit_only | inconclusive | REJECT replacing Wheel/Call. Seven-mana halved-life giant burst competes with six-mana commander, loses consistent Ring triggers or wheel; not source-paid early. |
| 27 | Repercussion | Call of the Ring | commander_fit_only | no_detectable_difference | REJECT proposed cuts Call/Remora. Can combine with mass-damage wipe for huge damage but symmetric harm and board-state dependency, less direct than Sauron's combat engine. |
| 28 | Repercussion | Mystic Remora | commander_fit_only | inconclusive | REJECT proposed cuts Call/Remora. Can combine with mass-damage wipe for huge damage but symmetric harm and board-state dependency, less direct than Sauron's combat engine. |
| 29 | Lich's Mastery | Call of the Ring | commander_fit_only | inconclusive | REJECT Call/Wheel. Six-mana BBB/black-heavy life-draw replacement demands dedicated lifegain engine; loses identity source and introduces lose-game risk. |
| 30 | Lich's Mastery | Wheel of Fortune | commander_fit_only | no_detectable_difference | REJECT Call/Wheel. Six-mana BBB/black-heavy life-draw replacement demands dedicated lifegain engine; loses identity source and introduces lose-game risk. |
| 31 | Nefarious Lich | Call of the Ring | commander_fit_only | no_detectable_difference | REJECT replacing Wheel/Call. Extremely fragile life/exile replacement and lost-game downside when leaves battlefield, disconnected from Army/Ring. |

**Additional off-packet challenge:** `One Ring to Rule Them All` competes with mass temptation but its chapter II potentially destroys the deck's own nonlegendary Nazgûl, Orc Army support and Archfiend; do not cut Call. `Bothersome Noisemaker` supports own noncreature spell casts rather than the commander's opponents-cast engine, directly competes with Saruman without solving evasion. `The Mouth of Sauron` is slower amass redundancy. `Shadowspear` supplies lifelink/trample at equipment cost but clashes with included shadow, trample, Wonder and nonland unblockability; replacing Bilbo is defensible but currently no evidence of higher consistent Army-hit probability. `Moonstone, Harsh Mistress` converts hand discards but Sauron's discard is optional and draw4 is powerful without it. `All Will Be One` is a strong counter placement finisher; as long as cheaper The Great Goblin can turn amass *events* into damage while supporting Orc narrative, use a creature-heavy pilot test before converting toward generic enchantment damage. `Chandra's Ignition` targets one friendly creature and can burn all other creatures and opponents; Army can be removed in response, own other creatures suffer, and it overlaps Widespread Brutality. `Command Beacon` helps commander tax but trades colored land source/evasion; `Phyrexian Tower` requires sacrifice and is not more identity-relevant than Minas Morgul. The Oct15 owner-closeout independently rejected these; reassessment here includes explicit card-specific failure modes rather than assuming rank = approval.

## Actual finite source-paid sequence checks (analytical stack and game-state probes, NOT Monte Carlo)

These probes adjudicate critical interactions using the documented October Oracle/CR text; costs assume all stated sources are already controlled and capable of producing indicated mana. No unstated fetch targets, commander discounts, mana-positive loops, or guaranteed draw lines; opponents can respond where appropriate. These are *deterministic rule-state analyses*, not executed sample-based performance tests.

| # | Setup/cost, step, and adversarial response | Verified consequence and relevance |
|---:|---|---|
| 1 | Sauron on field; opponent casts a 1-mana spell then you Swan Song it for U. | Sauron amass1 goes onto stack from original CAST; countering spell cannot untrigger. Your Swan Song does not create a second Sauron trigger. |
| 2 | Sauron plus a 0/0 Orc Army with 2 counters; opposing creature attacks Sauron and opponent targets with removal. | Ward requires opponent to sacrifice a legendary artifact or creature to resolve target; Army survival does not grant Sauron hexproof or protect from untargeted sweep. |
| 3 | Army 4/4 connects opponent for four combat damage with Sauron. | One Ring temptation, one optional discard-whole-hand/draw4 trigger. Does NOT draw4 simply for attacking or damaging creature blocker. |
| 4 | Sauron + Nazgûl x2, Call of the Ring on your field; your upkeep begins. | Call triggers one Ring temptation; both Nazgûl each place one +1/+1 on each Wraith, then Sauron offers discard/draw4. Ring-bearer change need not result in a creature if none exists. |
| 5 | You control Sauron and four good cards; one Ring temptation occurs. | Declining optional discard leaves entire hand intact and draws zero; may be strategically superior to drawing four. |
| 6 | Sauron + Throne choosing Avatar; opponent casts a spell. | Two Sauron amass Orcs1 triggered events, each independent; Throne does not increase amass N within a single trigger. |
| 7 | Sauron + Throne Avatar; one Army damages one player. | Two Sauron Ring temptations occur, each creates a potential separate Sauron draw4 trigger (possibly more if Avatar doubling applies to draw trigger). No free draw8 absent a paid choice and hand discards. |
| 8 | Throne chooses Wraith; one Ring temptation with three Nazgûl on battlefield. | Six total Nazgûl pump triggered abilities, each giving +1/+1 to each Wraith (3 Nazgûl ×2); Sauron draw trigger unmultiplied unless he has Wraith type. |
| 9 | Throne choosing Wraith on battlefield plus Nazgûl ETB. | That Nazgûl is Wraith and its ETB Ring temptation triggers twice; resulting temptations each also trigger live Nazgûl pumps twice; every resolution separate. |
| 10 | Minas Morgul untapped, 3B available and Army legal target. | Pay 3B and tap the land to install shadow counter; Army stays Army/Orc, becomes Wraith, gains shadow; pumping Nazgûl now affects that Army. Not free/instant evasion without mana. |
| 11 | Army already has shadow counter, opponent has no shadow blockers; Army attacks. | Army damage is likely if opponent cannot remove Army, create shadow blocker, or prevent damage; it triggers Sauron when combat damage to PLAYER is dealt, regardless Army's extra Wraith type. |
| 12 | Sauron+Mauhúr, opponent casts spell. | One amass Orcs1 becomes 2 +1/+1 counters on selected Army due to Mauhúr replacement; does not become exponential or two amass events. |
| 13 | Sauron+Mauhúr+The Great Goblin, opponent casts spell. | One amass counter event adds 2 counters total and The Great Goblin event payoff happens **once** for two damage to its configured target, not four damage due to counters. |
| 14 | Same setup + Throne Avatar; opponent casts spell. | Two separate amass events, 2 counters each (with Mauhúr), and TWO qualifying Great Goblin triggers, two damage each; if Throne naming Avatar doesn't include Great Goblin its triggers aren't doubled. |
| 15 | Great Goblin, Foul-Hearted ETBs when you have Orc Army. | Amass Goblins3 adds 3 counters to existing Army, makes Army Goblin additionally, trample supplied, no second token required; can generate single The Great Goblin counter event. |
| 16 | Great Goblin attacks, opponent removes him in response to attack trigger. | Amass-on-attack already triggered and resolves even if Goblin removed; loss of static trample may let chump blocker prevent Army combat damage. |
| 17 | You cast Widespread Brutality for 1BR with 5/5 Army and 2 Nazgûl. | Amass Zombies2 makes existing Army 7/7 Zombie/Orc Army, then Army deals its power to EACH non-Army creature including Nazgûl and Sauron; generally wipes allies, not a one-sided sweep. |
| 18 | With no Army, you cast Widespread Brutality and opponent has 3/3. | Spell creates a 0/0 black Zombie Army token and adds two counters, then 2/2 Army deals two to each non-Army: 3/3 survives absent modifiers; boardwipe overstatement false. |
| 19 | Your Army dies in destroy-wipe with 8 +1/+1 counters and Ozolith. | Ozolith gets 8 counters; Army token ceases in nonbattlefield zone. Must subsequently have a creature to accept Ozolith counters at beginning of combat; Ozolith does not preserve token. |
| 20 | Wonder in own graveyard and control typed Island (Watery Grave/Steam Vents/Volcanic Island, etc.). | Your creatures have flying regardless whether Wonder was cast; without controlled Island, no flying. |
| 21 | Anger in graveyard and control typed Mountain (Badlands/Blood Crypt/Steam Vents/Volcanic Island). | Your creatures gain haste while conditions hold; Anger on battlefield does NOT grant its graveyard-static bonus. |
| 22 | You cast Wheel of Fortune for 2R with Archfiend and Sheoldred on field, opponent each have large hands. | All players discard then each draw 7; Archfiend discard-trigger effects occur from own discarded cards, Sheoldred's per-card draw lifegain/damage can occur; opponents also refill. |
| 23 | Sauron + Call of the Ring, no creatures or Army; upkeep temptation. | The Ring still tempts, Sauron optional hand-to-four can fire even though no Ring-bearer creature; differentiates from combat-only support. |
| 24 | Sauron + Relic of Sauron + Mana Vault + Island/Swamp/Mountain. | Relic needs four mana spent earlier and taps later for one U/B/R; Vault provides CCC but zero colored; six-mana command cast requires available UBR plus 3 generic; cannot claim reliable T3 without paying setup turns. |
| 25 | Commander on field, Rollick in hand; opponent attacks with high-value creature, no mana left. | Free Deadly Rollick (when control commander) exiles threat; Tyrant eight-mana card as swap cannot answer this timing/board-state. |
| 26 | Sauron+Call, replace Call with Grimoire in hypothetical, opponent casts zero spells and Army blocked. | Baseline upkeep gives one Ring temptation and Nazgûl pump/Sauron wheel option every upkeep. Challenger must supply *independent* Ring events from elsewhere; draw-only proxy lacks these effects. |
| 27 | Opponent casts spell into Remora and Sauron. | Sauron amass triggers even if spell countered; Remora draw depends on opponent paying {4} for a qualifying noncreature spell; Breach replacement loses Remora's taxation. |
| 28 | Animate Dead enchants Worldgorger Dragon hypothetically in graveyard with two untapped lands and no instant-speed sink. | Dragon ETB exiles all own other permanents incl Aura; Aura LTB sacrifices Dragon; LTB returns permanents incl Aura. This can repeat and float land mana if available, but without a legally finite stopping condition/opponent action may force a draw. Not a clean win just because Spellbook records loop. |
| 29 | Cast Tidespout Tyrant for 6UU with no free mana and a single 1 mana spell in hand, Sauron threatened. | Tyrant survives only if allowed to resolve; another SPELL cast gives one bounce trigger, which can be responded to. Cannot provide Rollick's immediate free exile at zero mana. |
| 30 | Attempt to use Ringsight to find Roaming Throne with UBR Sauron controlled. | Ringsight's shared COLOR tutor finds cards sharing color with Sauron; Throne colorless shares no color and is ineligible. Similarly Mystical Tutor cannot find creature Throne. |
| 31 | Cast Reiterate with buyback on an ordinary 2R Wheel of Fortune and no other mana engine. | Requires paying Reiterate 1RR + buyback 3 plus legal spell to copy; original wheel plus copy refill opponents and selves, no automatic mana or finite win. |
| 32 | Repercussion plus Blasphemous Act hypothetical, each side has 10 creatures. | Each creature being dealt 13 would trigger Repercussion separately for its controller; includes your own creature damage to you, so not automatically safe kill, player totals and prevention matter. |
| 33 | You play Lord of the Nazgûl with Sauron on battlefield but cast no instants/sorceries this turn. | Lord's own spell-cast payoffs cannot trigger merely from opponents casting creature spells; Sauron's opponent-spell Army still works, so packet 'commander fit' overstates synergy. |
| 34 | Quiet opponent pod (one opposing spell/round) with Call, 3 Nazgûl and Throne Wraith vs disconnected Army. | One upkeep temptation generates 6 Nazgûl pump trigger events regardless opponent casts/Army damage; removing Call fundamentally reduces own inevitable clock. |
| 35 | Attack with trample Army 10/10 blocked by opponent 1/1 and no prevention; Sauron present. | Assign lethal damage to blocker and rest to opponent, barring other effects, so an Army actually damaging player triggers Ring; trample is meaningful, not guaranteed vs full damage prevention or enough toughness. |

### Baseline-versus-challenger adversarial matrix

| Opposing environment | Canonical 100 expected play and limit | Strongest challenger and why **not approved** |
|---|---|---|
| Fast noncreature spells | Remora/Study/Sauron amass, free Swat/Fierce/Force; reliance on one six-drop remains | Underworld Breach can recover spells but no shown compact source-paid kill; cutting Remora sacrifices exactly this coverage |
| Quiet creature boards | Call supplies upkeep Ring, Nazgûl grow; army slower, Widespread Brutality clears non-Army creatures but is self-damaging | Fall of Cair Andros adds damage-driven amass, but losing Rollick makes fast creature threats worse; alternative saga slot needs board tests |
| Pillowfort / flying blockers | Shadow from Minas Morgul, Rogue Passage unblockable, Great Goblin trample, Wonder fly; land activation taxes turn | Shadowspear or other unblockable item may help but duplicates other routes; check specific taxes and resource timeline |
| Removal-rich table | Sauron ward, free protection, Wheel/Reanimate/Victimize, Ozolith retain counters; non-target sweepers remain a weakness | Tidespout/Hullbreaker do not replace instant zero-mana targeted removal without waiting many turns |
| Artifact/enchantment suppression | Feed the Swarm, Rift, counters and mana rocks; fragile Call/Connections/The One Ring risk | Replacing Call with artifact Grimoire *increases* exposure to artifact disruption and removes native Ring source |
| Commander tax >8 | 34 lands + mana rocks, backup Saruman/Army and seven Nazgûl; recovery may be slow | More 2-mana colored rocks can lower bottleneck but cut must be genuine weak card rather than Connections; test opening source+pips |
| Opposing graveyard hate | Fair Army/Nazgûl plan remains; Entomb/Anger/Wonder/recursion weaken | Underworld Breach and Worldgorger less robust; generic combo conversions increase GY exposure |

**Strongest positive-case counterargument (Grimoire):** a draw apparatus independent of having Sauron or a Ring-bearer could improve topdeck recovery, particularly if Army cannot connect. **Why KEEP remains:** Call already tempts on upkeep independent of combat/Army, and even in no-creature case Commander draw4 is optional whenever tempted; Nazgûl ETB and buffs generate persistent engine. Removing Call for unmodeled draw is especially damaging in the exact no-connection states used to argue for Grimoire. If fresh Oracle for Grimoire reveals a way to generate repeated temptation or a payable immediate win, reopen this specific test rather than treating M5 `pass` as approval.

**Second positive-case counterargument (Tyrant):** resolving high-impact 8-drop can interact with multiple permanents and convert fast spells to bounce. **Why KEEP:** this commander already costs six; secondary eight-mana payoff has severe tempo and does not trigger from opponents' spell casts. Rollick is free immediate exile on attack/combo threat. The M5 test made both cards effect-blank; a performance `pass` there cannot verify combat/stack function.

### Test coverage and disclosure

Evidence actually reviewed: exact approved 100 TXT with deterministic weighted recount and 91-name audit; October15 canonical whole-list and approval-ready gate; Oct16 Oracle/CR documented five interaction groups; source Stage C mana proxy; all **31** M5 proposed add/cut pairs and their test status. Fresh work: **35** explicit finite state/cost/trigger analytical probes above, and a seven-environment adversarial comparative matrix. **No new executable goldfish/paired Monte Carlo run was performed**; no invented test receipt or quantitative improvement claimed. Existing M5 simulator v1.1 cannot model opponents, combat, Ring temptation and numerous actual candidate effects. This is the reason the prior automated evidence does not authorize any card replacement.

### Final per-issue judgment and handoff

**KEEP**, exact locked approved 100, no unauthorized swaps. Major P0 options Marina Vendrell's Grimoire (vs Call/alt Wheel) and Tidespout Tyrant (vs Rollick/alt top-end) considered and declined; mana P1 engines versus Connections declined on incomplete modeling; thematic Lord of the Nazgûl versus Bilbo and Fall of Cair Andros versus the slow saga are the most reasonable *unapproved* conditional comparisons if owner requests changes later. **Requiem Monolith Oracle effect was not freshly checked here**; don't represent its failed/no-effect v1.1 proxy as rules verification or insert without a new factual audit. No open issue is strong enough to mandate a canonical update or invalidate the source Oct15 legality gate.

**No approved decklist, canonical repository file, approval status, SHA, project exception or completed milestone was modified.** Only engineering authored review and later sequential tracker checkpoint may be merged after exact-head CI. All Pass C independent review and owner authority remain pending as before.
