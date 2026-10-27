# Deck #51 — Sedris, the Traitor King — M7 Rev1 decision review

Date: 2026-10-27 America/Chicago. Status: **NOT YET OWNER APPROVED**. Never alter canonical approval or claim a finished historical M6 I/J certificate.

- Canonical Oct15 source: `corymstover/grixis-commander-encyclopediaGPT/refinement/decklists/Sedris_the_Traitor_King_Approved_2026-10-15.txt`, raw SHA-256 `65fbfe3eb64551ad6f5723243fcd62a286610c360e24bd700b584252e1da6365`.
- Selected M7 exact list: `data/grixis/m7/candidate_lists/Sedris__the_Traitor_King_M7_Rev1.txt`, SHA-256 `b0aa141fe5d27b1e0d0bc804e692d56ae645c74de4bd6777c501b1ae057969da`.
- Physical candidate 100 including commander, 99 distinct names, only two Swamps, no companion and no project exception. Two more land faces: 31 → 33; bracket 4 Optimized.
- Audit inputs: the original M6 one-by-one 100-slot Sedris review, Pass C owner-equivalent Altar-versus-Panharmonicon dissent (no real independent-model certification), canonical exact source, EDHREC current Top and High Lift, off-ranked candidates and historic 15 blueprint P0/P1 case designs. This review is new comparative judgment, not gameplay win-rate inference.

## Commander-specific goal

Sedris grants sorcery-speed unearth {2}{B} to creature CARDS in the graveyard. It does not grant permanent recursion: unearthed bodies normally exile at next end step and exile instead if they would leave for another zone. Convergence reduces their generic two by two to {B} while Sedris is controlled. Preserve the timed stack rescue (Obeka, Sundial, Teferi's Veil, Deadeye), durable ETB duplication (Panharmonicon, Twilight Diviner), enters-from-grave rewards (River Kelpie/Flayer), and the paid Deadeye+Peregrine Drake engine. One Gyruda ETB can mill each player four; it has no companion restriction when played as an ordinary card in the 99.

## Nine exact selected swaps

| Cut | Addition | Commander-first advantage | Material cost |
|---|---|---|---|
| Ashnod's Altar | **Altar of Dementia** | Converts expendable Titans and unearthed creatures into self-mill immediately, seeding later Sedris targets or milling opponents with spare tokens. | Loses the sacrifice-for-two-colorless mana engine. Unearthed creatures sacrificed this way exile, so this is not a recursive sacrifice loop. |
| Chainer, Nightmare Adept | **Thassa, Deep-Dwelling** | At the beginning of our end step, blink an unearthed ETB creature before its delayed exile trigger resolves; return as a new object for durable repeated ETBs. | Four mana and an exposed enchantment; removes independent discard and cast-a-creature-from-graveyard backup when Sedris is unavailable. |
| Feldon of the Third Path | **Agadeem's Awakening // Agadeem, the Undercrypt** | Makes land drop 33 while retaining an expensive late-game reanimation spell as a land/spell choice, easing six-mana commander sequencing. | Loses Feldon's repeatable graveyard token copies and early-game power; Awakening has substantial black requirements and tapped or three-life land cost. |
| Gifts Ungiven | **Cephalid Coliseum** | Raises physical land density to 32-33 and retains a threshold looting land that draws three/discards three to bin payoffs after the graveyard develops. | Replaces a flexible instant that moves two chosen cards to grave. Coliseum only activates at threshold and sacrifices itself while paying blue. |
| Jin-Gitaxias, Core Augur | **Gyruda, Doom of Depths** | A six-mana creature ETB that mills four cards per player and converts one even-MV milled creature to our battlefield, doubled by Panharmonicon. | Gyruda may hit no eligible even-MV creature and fuels opposing graveyards; loses Jin's end-step draw-seven and rescued hand-size lockdown. |
| Likeness Looter | **Careful Study** | One blue mana draws two and deliberately discards two expensive creatures for Sedris, speeding the pre-commander graveyard assembly. | One-shot spell replaces a recurring tap looter and its graveyard-creature copying option; lower late-game standalone utility. |
| Sepulchral Primordial | **Agent of Treachery** | An unearthed Agent steals ANY target permanent immediately, and that change of control continues after Agent exiles; Panharmonicon doubles its ETB. | Seven mana and a fragile theft ETB; loses Primordial's potential three-opponent graveyard reanimation against stocked opponents. |
| Sheoldred, Whispering One | **Phyrexian Delver** | Five-mana ETB returns our best creature immediately without waiting for an upkeep that an unearthed Sheoldred normally never reaches. | Costs life equal to each target's mana value, especially sharp if Panharmonicon doubles it; forfeits Sheoldred's continuing sacrifice pressure when rescued. |
| Windfall | **Intuition** | Three-mana instant finds a three-creature pile, making two assured graveyard unearth targets and giving the third to hand; directly tutors Sedris plans. | Loses Windfall's mass hand reset/discard and potential seven-card refill, decreases generic card velocity in stalled hands. |

## Rescue and adversarial timing

- An unearthed creature is NOT recoverable merely by sacrificing it to Altar; it goes to exile under unearth replacement. Altar mills equal to last known creature power (e.g., Grave Titan 6), not mana value. Ashnod's colorless mana is genuinely lost.
- Sundial and Obeka end turn only profitably once the actual end-step exile trigger is on the stack. Ending too early simply permits a later beginning-of-end-step trigger. No Sundial cut; an earlier GrokBot argument was based on this false timing premise.
- Thassa and an unearth delayed-exile ability are both beginning-of-end-step triggers controlled by us. We can order Thassa's blink ABOVE the exile trigger, then exile and return that creature as a new object, making the old pending trigger inapplicable. Target invalidation and enchantment removal remain blockers.
- Teferi's Veil phases only actual attacking creatures at end of combat. It does not preserve creatures that did not attack.
- Deadeye Navigator plus Peregrine Drake can yield repeatable positive mana only if the Drake is legally paired, the 1U blink cost can be paid, and untapped lands produce enough mana above two. A creature reanimated normally can be blinked; avoid counting unearth grave reuse after sacrificing it.
- Agent of Treachery's target-permanent controller change is lasting, not contingent on Agent remaining in play. In multiplayer, Sepulchral could have reanimated three grave creatures and thus remains a credible lost ceiling.
- Gyruda's four-mill occurs per ETB trigger; Panharmonicon makes a second separate ETB. Its reanimated creature has to have EVEN mana value among the newly milled cards, which need not exist. Twilight Diviner token copying a legendary creature still faces state-based legend rule.
- Phyrexian Delver's reanimation costs life equal to the returned target's mana value. Panharmonicon may double the triggered reanimation but doubles possible life payment too, so choose targets consciously.

## Larger package and held candidates

An exact 11-swap list (SHA `229bd064dffb8948d187099fdc70b06ab246835597d18ddcb3646ff503589201`) adds **Ghostly Flicker** over Vile Entomber and **Mesmeric Orb** over Ripples of Undeath to the nine swaps. It is plausible for low-removal, slow pods where mass mill/blink repeats shine; rejected because Vile tutors a chosen threat into Sedris' yard and Ripples supplies hand selection while neither fuels the other graveyards.

An exact nine-swap rescue/sacrifice alternate (SHA `d3578c8735be29122156d08c9a6dfcb892cbe6d295b0e411bf1e3896f2f2b363`) retains Ashnod's Altar by cutting Panharmonicon instead. This is Pass C's strongest historical alternate cut. Rejected because losing second ETB tutors, Delver returns, theft and Titan tokens is worse than Ashnod's colorless creature-fed mana in this version. No guarantee from unmeasured pod win rates; it is a role/stack tradeoff.

Other explicit off-ranked/EDHREC challenges retained as alternatives or rejected: **Discontinuity** vs Veil (one-shot vs repeatable all-attacker rescue), **Ancient Brass Dragon** vs Etali (combat-damage variance vs immediate on-attack spell theft), **Incarnation Technique** vs Victimize (five-mana copy lets opponent reanimate, loses cheap deterministic two returns), **Conjurer's Closet** vs Obeka (higher setup and one blink each end step, lower timed control). **Kederekt Leviathan** was additionally checked as a mass bounce but bounces our Sedris, Panharmonicon and entire artifact/creature engine and was not promoted. **Gravebreaker Lamia** doesn't reduce unearth because its text discounts graveyard SPELL casts; **Embalmer's Tools** overlaps Convergence but cannot discount below one. No Oracle/Breach/Consultation homogenization.

## Verification boundary and owner authority

`sedris_rev1_verify.py` checks two exact raw SHA-256s, all 99 distinct physical names, nine changes, 33 land faces, protected pieces, and sixteen scoped finite source cases mapping all historic C1/K1–K7/E1–E2/W1–W2/F1–F3 plus new-card edge cases. GitHub CI performs a full fresh Scryfall card-collection Oracle/color identity/official Commander legality sweep and the repo M7 decision gate. These are bounded source-bound checks, NOT a Magic rules engine, hidden matchup tests, tournament win rates, new independent-model Pass C, or historical M6 I/J acceptance.

**Owner decision requested only after exact-head CI verifies the staged bytes:** This deck is complete. Do you approve it?
