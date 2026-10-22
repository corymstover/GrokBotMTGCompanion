# Abaddon M7 second-pass — six substantive replacements, physical portfolios, and remaining exact verification

**Status: RESEARCH-ONLY.** This is a genuine revised, source-bound whole-deck recommendation following Cory's rejection of the earlier two-swap presentation. It is **not** a final owner approval packet, a canonical mutation, new M6 certification, or proof of gameplay win-rate superiority. The historical two-swap list, historical M6 I/J receipts and source hashes remain immutable.

## Source, scope, and reproducible lists

- Current canonical approved/locked raw SHA-256: `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`; 100 cards including commander, 34 lands, no Abaddon project exception.
- Actual source: `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Abaddon_the_Despoiler_Approved_2026-10-13.txt`; independently read and reconciled with canonical override, and original imported source baseline.
- Selected **six-swap physical research list**: `Abaddon_the_Despoiler_rev2_six_swap_research.txt`; raw SHA-256 `0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790`. The list is newly staged *outside* the withdrawn historical two-swap packet.
- Competing **five-swap clone-focused physical 100**: `Abaddon_the_Despoiler_rev2_clone_focused_alternative.txt`; SHA-256 `752930337e0810afae2b5328c33b20447ce63c70c6f464f87536162172e94ba2`.
- Competing **five-swap combat-focused physical 100**: `Abaddon_the_Despoiler_rev2_combat_focused_alternative.txt`; SHA-256 `d1b91dece69b3d82c839cc65c88bacde40b8b3cfdae0e54db052fca9e64eb304`.
- Machine-readable exact add/cut comparison, ten weakest slot names and twelve candidate judgments: `Abaddon_the_Despoiler_rev2_six_swap_manifest.json`.
- Existing dated 97-card source-bound baseline Oracle snapshot covers original 94 distinct names plus Chaos Warp, Grinning Ignus and Aggravated Assault. A fresh Scryfall named-card check on October 22 also confirmed Spark Double, Orcish Bowmasters and Cyclonic Rift are officially Commander-legal, Grixis color identity compatible, and have the Oracle text and IDs recorded in the manifest. The final revised 100-card exact-current Oracle gate **has not yet passed**.

## Final selected research package: six real improvements

| Add | Cut | Concrete gain | Honest opportunity cost |
| --- | --- | --- | --- |
| **Grinning Ignus** | Rakdos, Lord of Riots | Birgi plus payable repeated hand-casts, with Abaddon X>=3 generating distinct cascade triggers; Nightscape Familiar can improve mana efficiency. | Rakdos is a flying trampling threat and can discount later creature spells; Ignus without Birgi/threshold/outlets has low independent floor. |
| **Chaos Warp** | Inevitable Betrayal | Instant answer to resolved enchantments, artifacts or hate permanents that the original list scarcely answers; hand-cast 3-MV spell can itself cascade after X>=3. | Betrayal is a premium free MV0 cascade hit stealing an opponent's creature from library. Warp can reveal another permanent. |
| **Spark Double** | Bituminous Blast | A *nonlegendary second Abaddon* grants qualifying paid hand-casts **an additional independent cascade**, directly multiplying the commander rather than generic spellslinging. Also flexibly copies a controlled alternative creature/planeswalker. | Loses 5-MV printed-cascade instant creature removal, which with original Abaddon can produce two cascade triggers; Spark requires suitable battlefield target and initial four-mana setup. |
| **Orcish Bowmasters** | Cabal Ritual | 2-MV flash ETB damage or creature interaction; Wheel of Fortune/Windfall with Bowmasters on the battlefield yields one trigger per opponent card drawn outside the exempt first draw-step draw, potentially very large *same-turn* X. | Cabal is a paid black ritual, net +1 B below threshold or +3 B with seven cards in grave; reduced ritual burst can slow some Breach/tutor turns. Bowmasters without wheel has a smaller same-turn loss floor than Kessig/Thermo. |
| **Cyclonic Rift** | Force of Negation | Answers already resolved nonland stax with an inexpensive bounce mode and offers a paid seven-mana overloaded asymmetrical reset; its **printed MV is 2 even when overloaded**, so X>=2 grants hand-cast cascade. | Force of Negation provides free exile-counter on opponents' turns and helps prevent fast opposing combos; Rift is not a hard answer to re-castable stax and cannot be overloaded for free via cascade. |
| **Aggravated Assault** | Exalted Flamer of Tzeentch | Converts protected on-list **Loyal Subordinate + Neheb, the Eternal + controlled Abaddon** into repeat combats/postcombat mains with source-payable recurring opponent life loss; one-on-theme independent win route alongside hand-cast cascade. | Flamer is a meaningful 40K card: delayed random upkeep instant/sorcery recursion plus 1 loss to each opponent for each instant/sorcery cast. Assault without Neheb and a repeat damage/loss outlet can be a dead enchantment. |

These six are **not quota padding**: they address separately identified mechanical deficiencies—too little multiplication of Abaddon's *actual cascade grant*, resolved-permanent stax, suboptimal black-only burst for a tri-color strategy, insufficient independent combo reach through Neheb/Loyal, and reliance on opponent actions instead of wheel-turn threshold injection. Nonetheless, confirmation of the exact full 100 remains mandatory.

### Why this is commander-first

Preserves **The Ruinous Powers, The Lost and the Damned, Keeper of Secrets, Call Forth the Tempest, Noise Marine, Loyal Subordinate, Neheb, The Lost/Archaeologist exile cast payoffs, Nalfeshnee, Prosper, Birgi, Vivi, the compact Breach/LED/Brain Freeze backup**, and all 34 approved lands. The main upgraded engines use Abaddon's own spell-granting static ability, or the protected Warhammer life-loss combat package. It retains printed cascade through Call Forth and Noise Marine after weighing the loss of Bituminous Blast. Bracket 4 — Optimized remains the **provisional** ceiling, not certified.

## Rules-critical, bounded direct reasoning

1. **Two Abaddons:** with original Abaddon plus a Spark Double entering as a copy of Abaddon and remaining nonlegendary, a new qualifying spell **actually cast from hand on your turn** has two cascade abilities. An individual cascade resolution can cast a new spell from exile, which is **not itself a hand spell** and does not gain Abaddon's cascade from either static effect. On-turn opponent loss X and the cast spell's printed MV must be checked before claiming either grant.
2. **Bowmasters/Wheel:** Wheel and Windfall cause opponents to draw during your turn. With Bowmasters present as each draw actually occurs, every opponent draw except the exempt first draw-step draw yields a *separate* 1-damage trigger, each with a legal target. Damage/life loss contributes to X **only when dealt**, not when triggers are pending. For three opponents drawing seven each outside their draw steps, 21 triggers may be generated; assuming each targets an opponent and resolves without mitigation, X rises by 21. Not an unconditional combo or 21 damage to each opponent.
3. **Rift:** Its overloaded seven-mana payment does not change MV 2; a **hand cast on Abaddon's turn** with X>=2 earns one Abaddon-granted cascade. Rift cannot be cast for both overload and cascade's 'without paying mana cost' alternative cost simultaneously, and bouncing a permanent does not permanently remove its future recast.
4. **Assault/Neheb/Loyal:** In the normal combat, with original Abaddon controlled and Loyal present, each of three opponents loses 3 on the lieutenant trigger resolving. With Neheb, the next postcombat main produces 9 red from cumulative opponent life loss. A preexisting Assault permits spending five on its sorcery-timing ability, then the added combat triggers Loyal again and the extra postcombat main produces 18 red. Repeat while the permanents survive and relevant triggers resolve. Casting Assault from hand first costs three red, which can also be paid out of the nine; it receives Abaddon cascade only if X>=3. Extra-combat availability and postcombat sequencing require actual legal priority/payment; this is a conditional loop, not guaranteed through interaction.
5. **Ignus/Birgi:** Ignus's legal ability returns it to hand as part of paying {R}; making {C}{C}{R} and subsequently casting the creature for {2}{R} creates another **real cast** and a Birgi spell-cast mana trigger. Do not confuse repeated creature casts with Kessig Flamebreather's noncreature ability or with mana-positive infinite combo in isolation. An Abaddon cascade trigger from each paid hand cast requires X>=3 and Abaddon to remain controlled.
6. **Breach competition:** Preserve its mana and graveyard resources. Dig Through Time/Treasure Cruise delve removes potential Breach escape fuel; do not add those simply for their nominal printed MV8 and discount. Existing wheel access and source/cast count matter more than raw draw slots.

Source: actual retrieved Scryfall named Oracle records, permanent `data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Scryfall_20261022.json`, and the repository's paid physical P0/P1 mechanics receipts. This text describes direct reasoning, **not new simulated multiplayer wins**.

## At least eight genuinely plausible incumbent slots challenged

1. **Rakdos, Lord of Riots:** BBRR creature-specific discount; replace with direct hand-cast loop engine.
2. **Inevitable Betrayal:** premium free cascade theft, but does not answer a resolved Rule of Law or Rest in Peace; exchange for Warp.
3. **Bituminous Blast:** five-mana required creature target and printed cascade; replace for an additional Abaddon static ability, recognizing double-cascade loss.
4. **Cabal Ritual:** black-only threshold ramp and Breach fuel vs a 2-MV on-turn wheel payoff.
5. **Force of Negation:** free only on opponents' turns; actual own-turn Abaddon-cascade value limited vs a versatile reset/bounce.
6. **Exalted Flamer of Tzeentch:** on-theme but four-mana delayed random recursion and narrow instant/sorcery pings vs recurring Loyal/Neheb win route.
7. **The Ruinous Powers:** opponent random-library card exile four-mana upkeep exposure; **RETAIN** because it feeds nonhand cast engine and correctly causes card owner (often opponent) life loss.
8. **Profane Tutor:** suspend timing and zero MV, but **RETAIN** because low-MV cascades can turn it into an exceptionally valuable immediate unrestricted tutor.
9. **Pact of Negation:** a potentially dead MV0 unopposed cascade hit; **RETAIN** because unconditional free stack protection on the combo turn is not covered by Rift.
10. **Xander's Lounge:** tapped land as real first-turn tempo cost; **RETAIN** for fetchable three-color fixing in a 34-land five-MV commander deck.

These challenges are not synonymous with ten cuts. The selected six do not remove Commander/40K protected core cards other than the deliberately assessed Flamer role.

## Twelve nonduplicated material candidate judgments

- **SELECT_ADD — Grinning Ignus:** strongest direct paid repeated hand-cast synergy; cut Rakdos.
- **SELECT_ADD — Chaos Warp:** best flexible resolved-permanent answer alongside Rift; cut Inevitable Betrayal.
- **SELECT_ADD — Spark Double:** second Abaddon grant has irreplaceable commander-specific multiplier; cut Bituminous Blast.
- **SELECT_ADD — Orcish Bowmasters:** wheel-reliable burst at only 1B, with flash interaction; cut Cabal Ritual.
- **SELECT_ADD — Cyclonic Rift:** resilient large reset and cheap emergency out to nonland hate; cut Force of Negation.
- **SELECT_ADD — Aggravated Assault:** Neheb/Loyal naturally supports a second win path; cut Exalted Flamer.
- **RETAIN_ALTERNATIVE — Sheoldred, the Apocalypse:** Wheel/Windfall X ceiling can be even higher, but 2BB, removal fragility and less early flexibility than Bowmasters; perhaps choose for a sustained draw-heavy opponent table.
- **RETAIN_ALTERNATIVE — Irenicus's Vile Duplication:** nonlegendary flying Abaddon copy at 3U, but target-based sorcery interaction adds counterplay and cannot flex-copy a planeswalker; Spark is the preferred clone.
- **RETAIN_ALTERNATIVE — Sakashima of a Thousand Faces:** also copies Abaddon while preserving legend-rule exemption; its legend-rule-wide effect and original legendary characteristics introduce more dependence than Spark's standalone nonlegendary entry; best if additional legendary synergies are later found.
- **RETAIN_ALTERNATIVE — Dig Through Time:** instant-speed select-two-of-seven with nominal MV8 despite delve, but double blue, significant grave fuel competition with Breach, and no independent threshold enabler; revisit if access rather than payoff is observed to be the weakness.
- **REJECT — Treasure Cruise:** MV8 delve draw-three has weaker selection/timing than Dig and sacrifices Breach resources; no case for both on top of existing wheels, Remora and Rhystic.
- **REJECT — Stormfist Crusader:** 2-MV every-upkeep all-player draw/loss produces X>=3 at a normal three-opponent table, but gifts three cards to opponents on each trigger and contributes nothing immediately when deployed after upkeep; Bowmasters better exploits the actual wheel package.

## Three actually coherent 100-card portfolios and explicit selection

1. **Six-swap combined:** the selected research candidate; retains original 34 lands and core. Adds both an independent recurring combat route and Abaddon duplication while adding permanent answers and wheel burst. Favored strategically, subject to certification.
2. **Five-swap clone-focused:** omit Assault and retain Exalted Flamer; best at preserving Warhammer spell-burn redundancy and decreasing reliance on a three-permanent combat loop, but gives up an immediate potentially repeating Neheb/Loyal conversion.
3. **Five-swap combat-focused:** omit Spark and retain Exalted Flamer; better at using the existing Neheb combat board, but misses the highest-impact direct multiplication of Abaddon's printed static cascade grant across almost every qualifying hand cast.

All alternatives name exact adds and cuts in the manifest and exist as complete physical 100-card TXT files. Comparisons are authored marginal-role decisions, not simulated objective win-rate differences. No additional expensive simulator is justified **until a genuinely unresolved, decision-changing question is specified**.

## Hard blockers before any owner-final M7 packet

1. Re-run **entire revised 100-card current live Scryfall** name/identity/text/Commander-legality gate, including 3 new selected names, and preserve exact Oracle provenance. Existing 97-name snapshot only proves its historical named scope.
2. Add and **execute** rules-faithful deterministic checks for double independent hand-cast cascade, Bowmasters/Wheel distinct resolution/target/damage windows, overloaded Rift's payment and MV, and Neheb/Loyal/Assault source-paid step sequencing. Record exact-head CI, not just a JSON check.
3. Reconcile the changed 100-card list against M6.6–M6.9 source-hash and candidate-bound I/J requirements; previous two-swap certificate does not certify the new six-swap list. Extend the tested physical pool and publish new strict, reproducible receipts when earned.
4. Reconcile all 10 challenged incumbents and 12 decisions into the final M7 machine schema, with heightened audit and live canonical SHA. Only set **READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED** after substantive and executable hard evidence passes. Do **not** alter the old withdrawn M7 decision record or historical staged candidate until successor evidence is ready.
5. Finally present all 100 cards, six actual adds/cuts with substantive reasons, provisional Bracket 4 and three accurate tags to Cory for his **exact owner decision**. No canonical replacement or milestone acceptance by inference.

**Immediate next technical work is the finite revised-candidate Oracle/mechanics and updated I/J binding—not another unrestricted 20,000-game research campaign.**
