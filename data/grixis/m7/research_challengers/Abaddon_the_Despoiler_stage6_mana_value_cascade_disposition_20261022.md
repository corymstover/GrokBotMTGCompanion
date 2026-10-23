# Abaddon Stage 6: printed mana-value and free-cast reachability adjudication

**Status:** RESEARCH_ONLY. Canonical Abaddon M7 approved SHA `0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790` remains locked and unchanged. No new exact-list owner approval, no formal M6.10 acceptance, and deck #3 stays on hold.

## A decision-relevant top-end distinction

The source-approved 100's largest printed mana value for an existing library spell is **9**, `Blasphemous Act`, whose printed cost remains 9 even when paid for a single red mana after creature-count reduction. `Call Forth the Tempest` is printed **8** with **two independent printed cascade abilities**, while `Blood for the Blood God!` is printed **11**, with no printed cascade.

Cascade can exile and offer a spell only with strictly lesser mana value than the spell carrying cascade (plus the post-2021 check on the resulting cast spell). Consequently:

1. **Existing in-deck cascade sources cannot cascade into Blood for the Blood God! at all.** Its MV11 exceeds Blasphemous Act's existing maximum MV9; discounts from creature deaths do not change Blood's printed MV.
2. **A cascading Blasphemous Act (MV9) can legally hit Call Forth (MV8)** if the library order makes it the first eligible hit. The result is NOT guaranteed, but a successful free cast of Call from exile produces its two printed cascade triggers without requiring Abaddon to grant it anything.
3. When Call is actually cast from **hand** with Abaddon present on your turn and opponents have already lost total **X≥8**, Call gains Abaddon's cascade *in addition to* its two printed cascades (three separate triggers). If Call is instead cascade-cast **from exile**, Abaddon's hand-only clause does not add another instance. Other effects such as Wild-Magic Sorcerer may separately change this setup; do not silently assume them.
4. Blood can itself earn **one Abaddon-granted cascade** when hand-cast with X≥11, despite a smaller paid cost; its eight damage to each opponent occurs only on later resolution and cannot qualify its own earlier cast. It discards the current hand, draws eight, and **exiles itself** on resolution.
5. Crucial exception: `Mind's Desire` is not cascade and can offer a library-exiled Blood **without paying its mana cost regardless of MV11**. That specific high ceiling remains, but a one-card random hit from Mind's Desire is not reliable broad cascade access and the discard-eight/draw-eight effect may alter chained-resource sequencing.

**Sources:** 
- current Scryfall card identities, Oracle and Commander legality: `data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json` and `data/grixis/m7/research_challengers/Abaddon_the_Despoiler_post_Admiral_39_card_Scryfall_20261022.json`;
- Scryfall: https://scryfall.com/card/ltc/509/call-forth-the-tempest ; https://scryfall.com/card/40k/108/blood-for-the-blood-god%21 ; https://scryfall.com/card/msc/163/blasphemous-act ; https://scryfall.com/card/c21/123/minds-desire ;
- Wizards Comprehensive Rules (2026-08-07 PDF): https://media.wizards.com/2026/downloads/MagicCompRules%2020260807.pdf

## Strategic consequence, not a forced inclusion

`Blood for the Blood God!` must overcome a **much larger practical free-cast-reachability loss** than the earlier six-swap stress-test packets made explicit. Compared with protected Call Forth, it requires a large death-discount event to be realistically paid, gets at most a single Abaddon cascade from hand, cannot be cascade-hit by existing cards, and consumes its user's hand before refill. It has an extraordinary payoff in creature-dense matchups and can be hit by unrestricted Mind's Desire, so it remains a *table-conditioned alternative*, but the provisional default should **retain Call Forth** until a specific credible game-state/payment/floor analysis overturns that conclusion.

The prior Stage4 six/eight and Stage5 Harmonic six physical packets are **adversarial research portfolios**, not proofs. They intentionally cut Call Forth, so this new source-bound finding is an argument *against adopting them unchanged*. The permanent five-swap floor remains only eligibility and must never pressure us to cut a protected double-cascade card merely to increase change count.

**Next:** design a Harmonic/Ob/Kederekt/Ghyrson/land package that keeps Call Forth and sufficient stack protection if viable, then compare the exact 100 against the approved source and alternative cuts. No ownership or certificate claim until source/full mechanics/I-J are actually reverified.
