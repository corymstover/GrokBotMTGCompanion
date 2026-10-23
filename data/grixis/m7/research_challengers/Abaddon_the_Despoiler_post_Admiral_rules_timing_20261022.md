# Abaddon post-Admiral M7 — source-bound life-loss timing and EDHREC mechanism triage

**Status:** RESEARCH_ONLY; not an approved proposed replacement, M6.10 mechanical certification, or proof of superiority.
**Authority:** Current approved Abaddon list is exactly `0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790` (100 cards), preserved canonically. Admiral is separately finally owner-approved. No deck #3 work is authorized until Abaddon's new revision is expressly approved.

## Primary sources now inspected

- Wizards of the Coast, *Magic: The Gathering Comprehensive Rules*, PDF dated 2026-08-07: https://media.wizards.com/2026/downloads/MagicCompRules%2020260807.pdf — 601.2f–i (casting steps), 605.1a and 605.3a–b (activated mana abilities).
- Scryfall: https://scryfall.com/card/emn/193/cryptolith-fragment-aurora-of-emrakul
- Scryfall: https://scryfall.com/card/rna/117/spear-spewer
- Scryfall: https://scryfall.com/card/otc/164/electrostatic-field
- Scryfall: https://scryfall.com/card/clb/778/aurora-phoenix
- Scryfall: https://scryfall.com/card/40k/108/blood-for-the-blood-god%21
- EDHREC: https://edhrec.com/commanders/abaddon-the-despoiler and https://edhrec.com/commanders/abaddon-the-despoiler/optimized/expensive

These are source-bound analytic rulings. The speculative complete-100 comparisons retain `RESEARCH_ONLY` while current full Oracle/legality and candidate-specific I/J remain outstanding.

## A genuine missed timing advantage: Cryptolith Fragment

Current Oracle effect as reviewed: enters tapped, and its tap ability adds one mana of any color **and** causes each player to lose one life. Under official rule 605.1a, its non-targeting mana-producing activated ability remains a mana ability despite the life-loss side effect. Rule 605.3b makes it resolve immediately without going on the stack. Rule 601.2g allows that mana ability to be used during payment for a spell from hand, and 601.2i says characteristic-modifying continuous effects apply and cast triggers happen **after** the payment steps.

Thus in an ordinary four-player game, if all three opponents had lost zero life that turn, activating an untapped Cryptolith Fragment during casting of a **2-mana-value spell from hand on your turn** both supplies one of the payable mana and causes each of three opponents to lose one life. Abaddon sees X=3 when the spell becomes cast, so that spell meets printed MV2 < X3 and gains cascade. At MV3 exactly, 3 < 3 is false and no Abaddon-granted cascade occurs. With a single opponent and no prior loss, X=1 and MV2 fails. With a Fragment already tapped, there is no ability activation to use. Other preexisting life loss and replacement effects must be computed individually.

This is not a simulated matchup win-rate claim. The timing conclusion follows directly from current card text plus rules 601/605; the material **strategic** question remains whether a three-mana rock entering tapped beats a two-mana Talisman or another on-theme role given Abaddon's five-mana casting curve. Challenge the complete mana plan, do not simply jam a 55x High Lift card.

## Trigger sequencing checks, not final optimization

1. **Spear Spewer** costs one red and taps to deal one damage to every player; with three opponents and no damage replacement, resolved activation yields X=3. Unlike Fragment it is a normal activated non-mana ability and goes on the stack; creature summoning sickness prevents immediate activation after casting.
2. **Electrostatic Field** damages each opponent upon casting an instant or sorcery, including a spell actually *cast* from exile via cascade. An ordinary copied spell is not cast. Field's trigger resolves *after* the instant or sorcery is cast: its new damage cannot retroactively give that same spell Abaddon cascade if it lacked cascade at cast completion. Trigger ordering matters when the spell already has cascade.
3. **Aurora Phoenix** can return to hand from graveyard when a spell with cascade is cast. An Abaddon-qualified hand spell is already endowed with cascade as it becomes cast, so it is a plausible trigger. This creates access to an expensive recur-and-recast threat, **not** an automatic free casting or doubled cascade line. Preserve graveyard position and the source's exact ability trigger in an explicit finite case before declaring a working engine.
4. **Blood for the Blood God!** has printed mana value eleven regardless of how much creature-death discount was applied; a hand-cast Blood only gets Abaddon cascade when opponents' already-lost total exceeds eleven by the time it becomes cast. Its resolution later discards the caster's hand, draws eight, and deals eight to each opponent; that damage cannot qualify its own earlier cast. Contrast the current eight-mana Call Forth the Tempest and demonstrate feasible creature deaths/payable remaining mana.

## Strategic guardrails

- Current original list already includes the powerful all-opponent **Boltwave**, **Flame Rift**, **Thermo-Alchemist**, and **Kessig Flamebreather**, plus **Orcish Bowmasters**, **Loyal Subordinate**, and **Noise Marine**. Redundant life loss must earn a slot through turn timing, resilience, and paid setup cost.
- The current approved replacement list has 34 lands and deliberate high-MV cascade, a proven 40K exile-cast identity, and a Breach/LED/Brain Freeze recovery route. Do not trade unique recovery and printed double cascade for generic pingers without proving the full 100 improves.
- The two newly staged alternative 100-card fixtures each use **two** trial replacements and remain strictly research-only. They explore the opportunity costs of `The Ruinous Powers` and `Call Forth the Tempest`; they are **not** a final recommendation, and do not count toward the required five genuinely justified NEW swaps.
- EDHREC overview displayed approximately 6,750 Abaddon lists; its optimized expensive subgroup contained only about 16. High Lift is correlated inclusion relative to general play, not win-rate proof and not a reason to add all nine omitted high-lift cards.
- Candidate-specific live Oracle full snapshots, additional challenged incumbent slots, coherent larger configurations, targeted effect fixtures, and fresh M6 I/J hash binding remain **UNVERIFIED** for any potential replacement. No owner approval should be requested now.

**Next decision-relevant engineering unit:** record a rules-faithful deterministic cast sequence for Cryptolith Fragment and a separate Aurora Phoenix cast-zone/trigger fixture, then analyze opportunity cost relative to the existing 100. Use one bounded experiment only if that analysis leaves a genuinely reversible decision.
