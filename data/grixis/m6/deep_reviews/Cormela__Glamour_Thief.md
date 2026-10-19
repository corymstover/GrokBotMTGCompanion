# Cormela, Glamour Thief — comprehensive commander-first deep review (#9)

**Reviewer/date:** ChatGPT primary engineering reviewer Oct 19, 2026. Authored evidence distinct from independent GrokBot Pass C. Full approved deck remains LOCKED; no unapproved list mutations.
**Authority:** `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json#Cormela__Glamour_Thief` and exact `refinement/decklists/Cormela_Glamour_Thief_Approved_2026-10-14.txt`. Raw approved SHA-256 **`80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b`**. Source blob `ee008725234c917af858de5a9c237fc2acf6781d`. Engineering logical hash `lh1:545b22caf5c71e44fe42483b7a737352e9e712db43d8289f03a82997269fa7b6`, by design independent format. `Cormela__Glamour_Thief` engineering+canonical identifier exact match, source discrepancy NONE.

## Commander identity and natural ceiling

Cormela 4-MV Grixis Vampire Rogue, haste, `{1}, {T}: Add {U}{B}{R}. Spend this mana only to CAST INSTANT and/or SORCERY spells.` Cormela's DEATH trigger returns up to one target instant or sorcery CARD from own graveyard to hand. Her mana helps rituals, Saw in Half, Goryo's Vengeance, Shallow Grave and recast chains, but CANNOT pay for Thassa's Oracle, other creature, enchantment/artifact spells, or activating her own `{1}` ability. Haste means a newly cast/reanimated Cormela can tap with one generic available unless it reenters TAPPED. Key action when physical commander dies for reanimation lines is choose **LEAVE in grave** rather than putting commander into command zone via SBAs.
Natural ceiling **Bracket 5 — cEDH**, justified by actual fast Cormela-specific spell recursions (Saw+ritual, altar/Goryo/Shallow, Birgi/Molten), compact alternate wins Oracle/Consultation/Pact, Underworld Breach/LED/Brain Freeze, Ad Nauseam and free stack interaction; not forced into a generic consultation-only commander shell. This deck's main Cormela death-and-tap engine remains strategically central, while fast failovers are natural to this commander at ceiling.

## Full 100-card role audit

**Fresh canonical source/complete gate:** exactly 100 cards and 100 UNIQUE names; 30 lands (including exactly 1 Island, 1 Mountain and 1 Swamp), 6 creatures including commander, remaining instants/sorceries/artifacts/enchantments. No name repeats, enabling Tainted Pact to process entire library without duplicate-name stop. B/R/U identity PASS for all, official Commander legality PASS for all, no project exceptions. Gate `refinement/verification/cormela_2026-10-14/gate_output/Cormela_Glamour_Thief_2026-10-14_Complete_Gate.md` and SHA-bound Oct14 full Oracle/rules certificate independently document user APPROVED/LOCKED.
30-land fast-mana posture supported by fetch/dual 3-color base, Chrome Mox/Mox Diamond/Mox Opal, Mana Vault, Sol Ring, Lotus Petal, Simian Spirit Guide, Gemstone Caverns, rituals, and 3 Talismans+Arcane Signet. Not all fast artifacts automatically produce U/B/R; Chrome Mox requires imprint, Mox Diamond land to discard, Mox Opal metalcraft, Mana Vault/Ancient Tomb colorless, and Cormela own mana restricts use. With only 30 lands, a card-advantage life-budget/speed balance against mulligans matters. Actual opening-hand mana simulations not run here.
Previously approved October14 fourteen swaps are locked: Goryo's Vengeance for Footsteps, Consultation for Electromancer, Pyroblast for Grapeshot, Mindbreak Trap for Mana Drain, Rite for Mizzix's Mastery, Arcane Signet for Mox Amber, Oracle for Nightscape Familiar, Shallow Grave for Presumed Dead, Tainted Pact for Storm-Kiln Artist, Molten Duplication for Twinflame, Orcish Bowmasters for Viscera Seer, Wishclaw for Bombardment, Phyrexian Tower for Urborg, Flooded Strand for Xander's Lounge. Source's approved list itself, not proposed baseline or prior October13 Final, is authoritative.

### Whole source 100/100 card name and functional audit

| Approved card | Qty | Oracle type | Cormela-specific role, sequencing, or liability |
|---|---:|---|---|
| Cormela, Glamour Thief | 1 | Legendary Creature — Vampire Rogue | Commander: haste; pay1 and TAP to make UBR usable ONLY TO CAST INSTANT/SORCERY. Dies (including legend rule, altar, destruction) -> return up to 1 inst/sorc from OWN grave to HAND. Leave card in GY for Goryo/Shallow loops. |
| Ad Nauseam | 1 | Instant | 3BB instant may reveal/draw then lose card's MV repeatedly, cEDH deck low average MV but high life risk, not deterministic. |
| An Offer You Can't Refuse | 1 | Instant | U counter target noncreature, opponent gets 2 Treasures, can protect pivotal lines but supplies opponent mana. |
| Ancient Tomb | 1 | Land | Tap CC at 2 damage, accelerates Cormela but life matters for Ad Nauseam. |
| Ashnod's Altar | 1 | Artifact | Sac CREATURE to gain CC as MANA ability, key to reanimate loop; Cormela dies trigger. No cast restriction on CC, fuels Cormela {1} tap activation. |
| Badlands | 1 | Land — Swamp Mountain | Fetchable dual Grixis mana, optional shock life where relevant. |
| Birgi, God of Storytelling // Harnfel, Horn of Bounty | 1 | Legendary Creature — God // Legendary Artifact | Birgi face spell CAST -> unrestricted R, survives turn stages; combined with Cormela+Molten spell-cast legend death loop. Harnfel discard to exile impulse alternative. |
| Blood Crypt | 1 | Land — Swamp Mountain | Fetchable dual Grixis mana, optional shock life where relevant. |
| Bloodstained Mire | 1 | Land | FETCH: typed Grixis dual access and shuffle Brainstorm; life cost/colored tempo. |
| Borne Upon a Wind | 1 | Instant | Spell / utility: You may cast spells this turn as though they had flash. Draw a card. |
| Brain Freeze | 1 | Instant | 1U target player mills3 with STORM spell copy per prior CAST this turn, can target SELF to refuel Underworld Breach escape or opponent for win. |
| Brainstorm | 1 | Instant | U draw3 then place 2 from hand on top, card selection, shuffle with fetches. |
| Cabal Ritual | 1 | Instant | 1B->BBB (BBBBB threshold seven grave) powerful spell mana; exact threshold matters. |
| Chain of Vapor | 1 | Instant | Spell / utility: Return target nonland permanent to its owner's hand. Then that permanent's controller may sacrifice a land of their choice. If the player does, they may co |
| Chrome Mox | 1 | Artifact | Imprint nonartifact nonland from HAND to tap colored mana in imprinted color, permanent card disadvantage for speed. |
| City of Brass | 1 | Land | Untapped any color at 1 damage, Ad Nauseam life budget risk. |
| Command Tower | 1 | Land | UNTAPPED/UTILITY land: exact colored count and Tainted Pact singleton considered. |
| Culling the Weak | 1 | Instant | B instant sacrificial creature as additional CAST COST -> BBBB, triggers Cormela death; body sacrifice cost already paid before responses. |
| Dark Ritual | 1 | Instant | B->BBB mana-positive instant; recast via Saw death triggers; BB net supports many iterations. |
| Deflecting Swat | 1 | Instant | 2R target reassign, alternative free while commander controlled; not blanket counterspell. |
| Demonic Gifts | 1 | Instant | Instant target creature +2/+0 and death-trigger reanimation untapped? Oracle returns creature to battlefield under owner, new object; recursion support, not a free mana source. |
| Demonic Tutor | 1 | Sorcery | 1B sorcery find ANY card to hand; direct fast combo assembly. |
| Diabolic Intent | 1 | Sorcery | Spell / utility: As an additional cost to cast this spell, sacrifice a creature. Search your library for a card, put that card into your hand, then shuffle. |
| Dualcaster Mage | 1 | Creature — Human Wizard | FLASH ETB copy an INSTANT/SORC spell on stack; with Molten Duplication pending targets creature you control, can retarget copy to Dualcaster and loop hasty tokens. |
| Entomb | 1 | Instant | B instant put card in grave; seeds commander legendary for Goryo/Shallow, or Breach spell fuel. |
| Exotic Orchard | 1 | Land | UNTAPPED/UTILITY land: exact colored count and Tainted Pact singleton considered. |
| Faithless Looting | 1 | Sorcery | R draw2 discard2, flashback2R, fuels grave Cormela/reanimation at card-negative hand rate. |
| Fierce Guardianship | 1 | Instant | 1UU counter noncreature, alternative free only if commander CONTROLS at cast; Cormela survives tempo; essential. |
| Flusterstorm | 1 | Instant | U counter inst/sorc unless pay1, STORM, defend fights in cEDH. |
| Goryo's Vengeance | 1 | Instant — Arcane | 1B instant returns LEGENDARY creature from grave with haste then exile next endstep; if Cormela left in GY enables altar loop, requires Commander owner not moving it to CZ. |
| Force of Negation | 1 | Instant | 1UU counter NONcreature, pitch blue option free only if NOT your turn, and counters exiled spell; protect/interaction asymmetric. |
| Force of Will | 1 | Instant | 3UU counter ANY spell, pitch blue card+1life alternative, card disadvantage needed in cEDH. |
| Gamble | 1 | Sorcery | R any card to hand then RANDOM discard; grave-friendly for Breach/Goryo, not guaranteed searched card remains. |
| Gemstone Caverns | 1 | Legendary Land | Pregame preturn luck of being non-starting player + exile hand for luck counter, otherwise colorless land. |
| Gitaxian Probe | 1 | Sorcery | Spell / utility: ({U/P} can be paid with either {U} or 2 life.) Look at target player's hand. Draw a card. |
| Wishclaw Talisman | 1 | Artifact | 1 mana tap remove wish counter tutor ANY card, then an OPPONENT gains control. One-shot combo consistency but risk passing tutor. |
| Demonic Consultation | 1 | Instant | Black instant name card, exile top six then until name found; name card ABSENT to exile whole library then resolve Oracle ETB. DO NOT allow opponents to counter/kill Oracle before. |
| Pyroblast | 1 | Instant | R counter blue spell or destroy blue permanent, modal roles; strong versus cEDH blue. |
| Imperial Seal | 1 | Sorcery | B sorcery search any card to library TOP and lose2 life; doesn't tutor to hand. |
| Intuition | 1 | Instant | 2U choose 3 cards from library, opponent selects one to hand rest GY. Construct grave lines; not guaranteed first-choice into hand. |
| Island | 1 | Basic Land — Island | SINGLE BASIC: 100 unique names ensure Tainted Pact never repeats. |
| Jeska's Will | 1 | Sorcery | 2R choose mana based on target opponent hand and/or exile top3 IF commander controlled when CAST; mana mode can be underpowered if few opponent cards. |
| Lion's Eye Diamond | 1 | Artifact | Sac LED + DISCARD ENTIRE HAND to make three one color; instant timing only. LED escape with Breach can generate mana while discarding important spells/grave sequencing. |
| Lotus Petal | 1 | Artifact | 0-sac for 1 colored mana, efficient storm/Breach, one-shot. |
| Luxury Suite | 1 | Land | UNTAPPED/UTILITY land: exact colored count and Tainted Pact singleton considered. |
| Mana Confluence | 1 | Land | Untapped any color pays1 life on tap, correct interaction with restricted Cormela mana. |
| Mindbreak Trap | 1 | Instant — Trap | 2UU exiles any number target SPELLS, can free if opponent cast 3+ this turn; handles uncounterable/storm. |
| Mana Vault | 1 | Artifact | 1 tap to add CCC, doesn't untap normally each untap step, drains life upkeep, commander acceleration not stable colored. |
| Marsh Flats | 1 | Land | FETCH: typed Grixis dual access and shuffle Brainstorm; life cost/colored tempo. |
| Mental Misstep | 1 | Instant | Phyrexian blue counter MV1, pay2 life or U, can stop opposing tutors/stack pieces. |
| Misty Rainforest | 1 | Land | FETCH: typed Grixis dual access and shuffle Brainstorm; life cost/colored tempo. |
| Rite of Flame | 1 | Sorcery | R→RR, +R per Rite of Flame card in ALL graveyards, one-shot ritual but Breach loops can repeat. |
| Morphic Pool | 1 | Land | UNTAPPED/UTILITY land: exact colored count and Tainted Pact singleton considered. |
| Mountain | 1 | Basic Land — Mountain | SINGLE BASIC: 100 unique names ensure Tainted Pact never repeats. |
| Arcane Signet | 1 | Artifact | Early artifact fixing/ramp; not Cormela's restricted instant/sorcery ritual itself. |
| Mox Diamond | 1 | Artifact | 0 discard LAND on ETB or sacrifice Mox, tap any colored mana, opportunity with only 30 lands. |
| Mox Opal | 1 | Legendary Artifact | 0 artifact metalcraft need 3 artifacts, zero early if threshold not reached. |
| Mystic Remora | 1 | Enchantment | U enchantment cumulative upkeep card draw versus opponent noncreature spells (unless pay4); accelerates interaction-rich tables. |
| Mystical Tutor | 1 | Instant | U instant seek instant/sorcery to TOP of library, not creature Oracle or artifact mana piece. |
| Necropotence | 1 | Enchantment | Bargain LOOKALIKE but not same! Pay1 LIFE exile top card facedown, only put into hand at BEGINNING NEXT END STEP. SKIP draw step; discards exiled replacement. |
| Thassa's Oracle | 1 | Creature — Merfolk Wizard | 2MV creature win trigger when own BLUE devotion >= remaining library cards. Consult/Pact on trigger stack with empty library, not an intrinsic win without setup. |
| Otawara, Soaring City | 1 | Legendary Land | UNTAPPED/UTILITY land: exact colored count and Tainted Pact singleton considered. |
| Pact of Negation | 1 | Instant | 0 counter spell but pay 3UU at NEXT upkeep or lose game; not unconditional free. |
| Phyrexian Altar | 1 | Artifact | Sac CREATURE to gain ONE of any color, also death loops but resource calculations differ from CC altar. |
| Polluted Delta | 1 | Land | FETCH: typed Grixis dual access and shuffle Brainstorm; life cost/colored tempo. |
| Ponder | 1 | Sorcery | U dig top3 reorder/shuffle, draw1, protects fast combo hands. |
| Preordain | 1 | Sorcery | U scry2 draw1, inexpensive selection/instant-sorcery count. |
| Shallow Grave | 1 | Instant | 1B instant reanimates TOP CREATURE card of your GY with haste, exile at next end step; grave order matters! Leaves Cormela in grave, sacrifice and reuse with altar. |
| Reanimate | 1 | Sorcery | B sorcery return any creature from any grave, lose life equal MV; Cormela reanimates without haste? Cormela PRINTED haste, so ready after return. |
| Red Elemental Blast | 1 | Instant | R counter blue spell or destroy blue permanent, different targeting rules from Pyroblast; redundancy. |
| Rhystic Study | 1 | Enchantment | 2U enchantment conditioned opponent spell draw; card advantage, vulnerable to tax paid. |
| Saw in Half | 1 | Instant | CORE: destroys Cormela, creates TWO legendary half-power/toughness token Cormelas. Legend rule removes one; original+token die triggers can return Saw and a mana-positive ritual from GY AFTER Saw resolves. |
| Scalding Tarn | 1 | Land | FETCH: typed Grixis dual access and shuffle Brainstorm; life cost/colored tempo. |
| Seething Song | 1 | Instant | 2R→RRRRR ritual for Saw/Corp; mana positive on recasts, requires red spells. |
| Shivan Reef | 1 | Land | UNTAPPED/UTILITY land: exact colored count and Tainted Pact singleton considered. |
| Simian Spirit Guide | 1 | Creature — Ape Spirit | Red pitch from hand for R, exiles card, not a cast or death trigger. |
| Sol Ring | 1 | Artifact | 1 generic rock accelerates, cannot itself make UBR mana; cEDH speed. |
| Steam Vents | 1 | Land — Island Mountain | Fetchable dual Grixis mana, optional shock life where relevant. |
| Tainted Pact | 1 | Instant | {1}{B} instant: exile from top until choose card or two duplicate NAMES; list has exactly 100 unique names so can exile all with none chosen for Oracle if no disruption. |
| Sulfurous Springs | 1 | Land | UNTAPPED/UTILITY land: exact colored count and Tainted Pact singleton considered. |
| Swamp | 1 | Basic Land — Swamp | SINGLE BASIC: 100 unique names ensure Tainted Pact never repeats. |
| Swan Song | 1 | Instant | U counter enchantment/inst/sorc and gives opponent 2/2 Bird, cheap protection. |
| Talisman of Creativity | 1 | Artifact | Early artifact fixing/ramp; not Cormela's restricted instant/sorcery ritual itself. |
| Talisman of Dominance | 1 | Artifact | Early artifact fixing/ramp; not Cormela's restricted instant/sorcery ritual itself. |
| Talisman of Indulgence | 1 | Artifact | Early artifact fixing/ramp; not Cormela's restricted instant/sorcery ritual itself. |
| Tendrils of Agony | 1 | Sorcery | 2BB target player loses2 life/gain2, STORM copies per prior spell CAST this turn; loops with Saw/Breach generate lethal spell count. |
| Training Center | 1 | Land | UNTAPPED/UTILITY land: exact colored count and Tainted Pact singleton considered. |
| Molten Duplication | 1 | Sorcery | Copy your artifact or creature as ARTIFACT in addition to other types, haste, end-step sac. Copying legendary Cormela forces legend-rule death, returns duplication with Cormela trigger; Birgi contributes R on CAST to supply activations. |
| Undercity Sewers | 1 | Land — Island Swamp | Surveil typed tapped UB land, fetchable but slower than untapped duals. |
| Underground Sea | 1 | Land — Island Swamp | Fetchable dual Grixis mana, optional shock life where relevant. |
| Underworld Breach | 1 | Enchantment | Nonland in own GY gets ESCAPE for printed mana plus exile three OTHER GY cards; LED + Brain Freeze refuels, must produce sufficient colored mana and grave count; sacrifice Breach at EOT. |
| Phyrexian Tower | 1 | Legendary Land | Land sac creature + tap for BB, commander death trigger; land sac source once per untap, not repeat unlimited. |
| Vampiric Tutor | 1 | Instant | B instant any card on TOP, life2; must draw/reach it before combo. |
| Orcish Bowmasters | 1 | Creature — Orc Archer | B1 creatures flash damage on extra card draw opponent, makes/or grows Orc Army; protects vs wheels/draw but not core spell loop. |
| Volcanic Island | 1 | Land — Island Mountain | Fetchable dual Grixis mana, optional shock life where relevant. |
| Watery Grave | 1 | Land — Island Swamp | Fetchable dual Grixis mana, optional shock life where relevant. |
| Wheel of Fortune | 1 | Sorcery | 2R discards hands then all draw7, fuels Breach GY, wheel could hand opponent interaction. Existing approved, do not cut for a nonidentical counter. |
| Windfall | 1 | Sorcery | 2U discards hands then everyone draws MAX discarded; increases storm/grave but feeds opponents. |
| Wooded Foothills | 1 | Land | FETCH: typed Grixis dual access and shuffle Brainstorm; life cost/colored tempo. |
| Flooded Strand | 1 | Land | FETCH: typed Grixis dual access and shuffle Brainstorm; life cost/colored tempo. |

## Candidate pool and competing cuts

Exact engineering candidate source `data/grixis/m6/optimizer/cormela-glamour-thief.json`: 142 pass-A commander-first candidate pairs, 108 pass-B technical candidates, **32** overlapping exact-swap agreements. Strong overlap is not a substitute for card text and fully paid cEDH opportunity cost. Named comparisons:

| Ranked addition → named cut | What improves and what is sacrificed | Disposition |
|---|---|---|
| **Archaeomancer → Faithless Looting** (A/B agreement) | 4MV creature ETB returns one inst/sorc from grave to HAND, but Cormela ALREADY recurs spells via its death trigger, and this creature costs four and has no haste/ritual ability. Faithless is one-mana early dig/discard for Cormela-in-grave, Breach and combo density with flashback. | REJECT exact cut (slow redundant body). |
| **Ardent Elementalist → Faithless Looting** (A/B) | Similar four-mana creature ETB spell recursion, does not supply combo mana or Cormela deaths. | REJECT. |
| **Altar of Dementia → Lion's Eye Diamond** (ranked) | Sac creature to mill its power can exploit repeated Cormela tokens, and Cormela death triggers (sac outlet) without paying mana; but LED is pivotal zero-mana red/black/blue source for Breach loop, Ad Nauseam and storm, not expendable. | REJECT LED cut. |
| **Blasting Station → Pyroblast** (A) | A nonmana sac outlet with infinite token ETB ping potential, but Cormela's primary loops need MANA-producing outlets; Pyroblast `{R}` saves against blue combo and more aligned with cEDH interaction. | REJECT. |
| **Arcane Denial → Wheel of Fortune** (B) | More two-mana counter coverage versus a seven-card refill and Breach grave dump; Wheel creates multiple grave and spell triggers, helps failover but also opponent draws. Removing Wheel has substantial combo and velocity cost. | HOLD no conclusive swap. |
| **Archmage Emeritus → Wheel of Fortune** (B) | Magecraft on cast/copy draws but four-mana exposed creature and Thoracle fast deck already has multiple draw/selection choices. | REJECT wheel cut. |
| **Big Score → Culling the Weak / Lotus Petal** (B) | Four-mana discard to draw2+2 Treasures slow even at strong payoff; Culling cheaply sacrifices Cormela as CAST COST to trigger recursion while creating BBBB, Petal zero-cost colored burst and Breach storm. | REJECT either cut. |
| **Abnormal Endurance → Borne Upon a Wind** (A) | Two-mana instant temporary resurrection supports altar deaths; Borne grants flash to ALL spells for turn and draws, enabling responsive cEDH combo on another player's turn and protecting timing. Under original approved package Demonic Gifts already gives similar death revival and Borne provides unique reactive mode. | HOLD, not clean upgrade. |
| **Heat Shimmer → Birgi, God of Storytelling** (B) | Second clone sorcery could combo with Dualcaster and Cormela, but losing Birgi breaks commander-specific Molten Duplication loop and generic spell-chain mana. | REJECT. |
| **Mystic Remora / Rhystic Study → secondary generic body** | Card-flow critical for mulligans, 30-land ritual synergy and protective stack fights. Candidate score alone cannot remove card-velocity support. | KEEP. |

Other M5 proposal pairs remain proposals, not accepted automatically. Some A/B overlaps favor high-cost creatures or remove Wheel/LED/interaction, harming natural cEDH tempo; approved deck is exceptionally low creature count by intention. No new net-positive substitution established from current source evidence. Official source approval and user lock outrank candidate-swap rankings.

## Oracle, legality and rules

1. Cormela is HASTE and 4MV, tap requires paying `{1}` from **other unrestricted mana**, because Cormela's own UBR can be spent only TO CAST instant/sorcery spells. These three mana may pay normal/mandatory additional casting costs of such spells, but NOT Thassa's Oracle (creature), Ashnod/Phyrexian Altars (artifact/ability), Wishclaw activation, or Cormela's own tap activation. The ability is a MANA ability (does not use stack under ordinary circumstances).
2. When Cormela DIES (sacrifice, destruction, legend rule), return up to ONE legal instant/sorcery card from own GY to hand. A spell whose resolution causes Cormela to die, such as Saw in Half, finishes resolving and goes to GY before the triggered ability is placed on stack; hence Saw can be retrieved by that death trigger. To reanimate *the original physical commander card* with Goryo/Shallow, do NOT elect to put that card in command zone; leave it in grave.
3. **Saw in Half** destroys target Cormela and makes TWO legendary token copies with rounded-half POWER/TOUGHNESS (original 2/4 -> tokens 1/2 in absence of other modifications). Legend rule retains one token, the other dies; original Cormela dies and one token dies, making two distinct Cormela death triggers. After Saw resolves, use death triggers to recover Saw plus Dark Ritual/Seething Song/Jeska's Will from GY if two legal cards available. Surviving token retains HASTE and usable tap mana after you supply `{1}`. Requires mana-positive ritual and valid targets/payments; 'Saw by itself with no ritual' does NOT automatically make infinite mana.
4. **Ashnod's Altar** sac Cormela for TWO colorless and Cormela returns Shallow Grave or Goryo from GY, paying spell from colored Cormela mana plus altar output and then using recurred Cormela's haste for next activation. **Phyrexian Altar** sac creature for ONE any-color mana and requires separate resource accounting, not interchangeable CC. Both sacrifice Cormela as COST so opponents cannot prevent paid sacrifice by killing it 'in response'.
5. **Shallow Grave** returns TOP creature CARD of graveyard, no target, grants haste and exile at end step. If another creature lies above Cormela in grave (after creature removal, discarded Bowmasters/Oracle), Shallow returns THAT creature, breaking advertised commander loop. **Goryo's Vengeance** instead targets LEGENDARY creature CARD and doesn't care about grave order, but Cormela must remain in grave; exile next endstep.
6. **Molten Duplication** casts spell copying own Cormela as an ARTIFACT as well as creature; original and token are same legendary name, one is put to grave via legend rule and death trigger recovers Molten, while Birgi gains R on EACH spell CAST. A new token with haste may tap after paying generic1 using unrestricted Birgi mana; Cormela's restricted UBR pays Molten itself. Without Birgi/other paid mana, cannot claim self-sustaining repetition.
7. **Dualcaster Mage + Molten Duplication**: first cast Molten targeting another own creature, respond with flash Dualcaster; its ETB copies Molten and retarget to Dualcaster, create hasty Dualcaster token with ETB that copies pending Molten again, repeat chosen finite times. Damage conversion normally via combat; opponents' responses to original/copy targets may disrupt. Dualcaster copies aren't CAST.
8. **Underworld Breach + LED + Brain Freeze**: escape needs original mana plus exile THREE OTHER GY cards per cast; each recast LED has zero mana cost, can sac/discard hand for 3 colored; cast Brain Freeze with sufficiently high spell-count and target SELF to refill grave for repeat and stack storm. In absence of grave-filling or required colored mana this is NOT a standalone infinite from two pieces. Deck has Brain Freeze, Wheel, LED and Petal alternatives.
9. **Thassa's Oracle + Demonic Consultation**: cast Oracle, its ETB trigger on stack; respond with Consultation naming card ABSENT from library (exiles library), after resolution let Oracle ETB win with devotion blue >=0 cards remaining. If Oracle leaves BF before its ETB resolves, last known info/devotion nuance matters; interaction can spoil combo; cannot skip stack windows. **Tainted Pact** can exile the entire source deck with no duplicate names (verified 100/100 unique) before Oracle ETB resolves; when exiled all, oracle wins as appropriate.
10. **Necropotence** isn't Yawgmoth's Bargain. Activated pay1 life exiles top facedown and moves it to HAND only at beginning of NEXT END STEP; its discard replacement exiles discarded cards instead of GY. Cannot use Necropotence payments to immediately fill hand or Breach grave and should not mislabel instant draw.
11. **Ad Nauseam** adds revealed card to hand and loses life equal mana value repeatedly if controller chooses; at low life a revealed high MV can kill during spell resolution. With low curve many 0/1 cards it is powerful but not certain.
12. **Force of Negation** zero-mana pitch option only on an OPPONENT's turn; free interaction on your own combo turn requires other cards e.g Force of Will/Guardianship/Swat conditions. **Pact of Negation** must pay `{3}{U}{U}` NEXT upkeep or lose if it was cast; don't describe without drawback.
13. **Mox Diamond** requires discarding a LAND or sacrifices itself, notable with 30-land source; Mox Opal requires three artifacts for metalcraft, Chrome Mox imprint requires nonartifact nonland card, Lion's Eye Diamond sacrifices and discards entire hand. Fast mana is not free of setup.
14. **Wishclaw Talisman** tutoring gives artifact control to an opponent (after activation) and has own-turn-only timing; cannot blindly plan second tutor from same source. **Tainted Pact** unique names ensure no duplicate stop, but if choosing a card during resolution, must not accidentally take a card when trying to exile full library.
15. All 100 unique audited Oracle names Commander-legal UBR as of Oct14 source gate, no registered project exceptions. All proposed noncanonical alternatives require fresh Oracle/color/ban check and explicit user approval before any list mutation.

## Finite sequencing and adversarial scenarios

**A — Saw + Ritual finite first cycle.** Required Cormela untapped on battlefield, Saw in Half AND Dark Ritual in hand, at least one `{B}` usable. Cast Dark Ritual for B, add BBB; pay generic1 and tap hasty Cormela to add restricted UBR. Cast Saw ({2}{B}) targeting Cormela, paying from remaining unrestricted B and Cormela restricted spell mana. Saw destroys Cormela; original goes grave, two legendary token copies enter with haste, legend rule kills one; two death triggers recover Dark Ritual and Saw once both in grave. Surviving token hasty and untapped can tap on further turns/iterations with unrestricted generic from recast ritual, copied spells continue to raise storm. IMPORTANT: exact stack legal targets and mana payment matter, no second free sacrifice generated by mere copying a spell.
**B — Cormela Shallow/Altar loops with grave order.** Control untapped Cormela, Ashnod's Altar, Cormela topmost creature card once it dies, Shallow Grave in own grave, one generic mana available. Activate Cormela pay1 tap -> restricted UBR, sacrifice her to Altar -> CC, death trigger returns Shallow to hand. Use one C + restricted B to cast Shallow 1B (the exact allocation of remaining C/UBR varies), return Cormela (top creature) with haste. Use remaining colorless for next activation, iterate and accumulate restricted U/R and colorless as appropriate. If Cormela was moved to CZ, or another creature card becomes top GY, fails. Official indexed loop references https://commanderspellbook.com/combo/1893-2034-4867/.
**C — two-phase Molten/Birgi legend.** Control Birgi and Cormela, pay for first Molten Duplication targeting Cormela. Birgi generates R UNRESTRICTED on spell CAST. Molten creates an artifact-legendary token Cormela with haste, choose one legendary to retain, one Cormela dies and triggers return Molten from grave after spell resolves. Use Birgi R to pay generic1 to tap surviving hasty Cormela -> restricted UBR; use U as Molten generic and R as red to recast, Birgi refunds another R, repeat if no disruption; leftover restricted B can accumulate. Beware exact legend choice and multiple Cormela objects; if opponent removes Cormela at critical priority window no repeat.
**D — compact Oracle + Pact.** List has 100/100 distinct names, including one each basic land, so cast Thassa's Oracle first and respond to its ETB with Tainted Pact. If uninterrupted, exile 99 or fewer cards until entire library exhausted, no duplicate-name stop and never choose to put card in hand; Oracle ETB resolves with cards in library=0, devotion may be any >=0 and win. This is commander-independent failover, kept SECONDARY rather than basis for cutting Cormela engines.
**E — Breach/LED paid throughput.** LED is an artifact activation at instant timing with discard all hand and sac LED for triple one-color mana. With Breach out, cast escaped Brain Freeze by paying 1U and exiling three other GY cards, use storm to target yourself for enough milling to replenish; escaped LED can be recast from grave at 0 using further escape costs. Sequence needs GY at each step and BLUE mana for Brain Freeze; if opponent exiles graveyard mid-loop, stops. Excess spell count converted to opposing library mill or Tendrils storm.
**F — adversarial Cormela disruption.** Silence/Rule of Law suppress multi-spell chains even with Cormela restricted UBR; graveyard exile stops death-return targets if removed in response, Cage/Dauthi/RIP can interrupt recursion, but not direct free stack counters. Targeted removal of Cormela after a paid death trigger already on stack cannot undo prior trigger, but exile replacing death prevents it. Opponent can counter Saw before it resolves, protect the target with indestructible (destroy fails -> NO copies), or remove target before Saw resolves. Shallow fails if wrong top creature; Goryo fails if Cormela in CZ.
**G — colored mana split:** Cormela generates UBR restricted, **not** unrestricted triple-colored source. To cast Thassa's Oracle (UU creature) need TWO other blue sources; one generic activation payment for tap also external. With 30 land and many colorless fast artifacts, initial conditions may be hard, despite source combo labels; colored-pip and sacrifice triggers must be shown in every proof.

## Conclusions and unresolved evidence

**STRATEGIC HOLD** on the exact approved Bracket 5 cEDH commander-first list. 100 unique/30 lands/6 creature slots; Cormela physical/reanimated death/tap is actually integral to at least three optimized loops, while compact Oracle/Breach alternatives improve realistic table ceiling rather than replace Cormela. No candidate matched a proven named weak cut under full combo + interaction constraints; rankings repeatedly propose losing Faithless Looting, LED, Birgi, Wheel or free counters for slower generic recursion cards, a likely strategic downgrade.
**Unresolved for future optional research:** Source-based Cormela turn 2/3 availability against colored-pip/0 land hands, exact Saw pool accounting in opponents-responses, combo survival through grave hate, active counter-protection/mulligan policies, empirical 4-player cEDH win rates. No new simulation/Colab pipeline run; no unsupported performance claim. No independent GrokBot Pass C or formal M6 certified deck implied by authored review.

## Source and test receipts

- Canonical source GitHub `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Cormela_Glamour_Thief_Approved_2026-10-14.txt`, raw SHA `80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b` and approved state; Source complete gate `refinement/verification/cormela_2026-10-14/gate_output/Cormela_Glamour_Thief_2026-10-14_Card_Verification.csv` git blob `44d3a42414abe9d420649db23ddc2c620fc8cbf0`, all 100 Oracle/legality PASS. Finalization certificate `refinement/verification/cormela_2026-10-14/Cormela_Glamour_Thief_Finalization_Certificate_2026-10-14.md` and separate rules `refinement/verification/cormela_2026-10-14/Cormela_Rules_Attestation.json`.
- Original 14 explicitly approved swaps and costs `refinement/verification/cormela_2026-10-14/Cormela_Optimization_Decision_Ledger.md`, primary engineering blueprint `data/grixis/blueprints/cormela-glamour-thief.json`, candidate source `data/grixis/m6/optimizer/cormela-glamour-thief.json`: 142 Pass A, 108 Pass B, 32 identical overlap projections.
- Independent combo source https://commanderspellbook.com/combo/500-2701-4867/ Saw+Dark Ritual, https://commanderspellbook.com/combo/1893-2034-4867/ Cormela+Shallow Grave+Ashnod's Altar, https://commanderspellbook.com/combo/742-1295/ Oracle+Consultation and https://commanderspellbook.com/combo/1295-3093/ Pact. Need preserve explicit initial zones/paid mana, not just cite combo names.
- Official rules checkpoint source recorded September25 2026 by `Cormela_Rules_Attestation.json`, full-Commander legality Oct14; current WotC comprehensive rules entry https://magic.wizards.com/en/rules and Commander banned list https://mtgcommander.net/index.php/banned-list/ .
- Exact-head CI to pass per engineering M6 depth workflow before marking this review `DEEP_REVIEW_COMPLETE`; review not user permission to edit canonical deck.
