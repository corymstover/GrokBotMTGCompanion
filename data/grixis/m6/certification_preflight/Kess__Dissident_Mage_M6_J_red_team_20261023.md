# Kess, Dissident Mage — M7 red-team memo (2026-10-23)

1. **Commander countered or removed.** Kess can be countered and strand four mana; recasting costs commander tax (CR 903.8). Removing Kess after a graveyard spell has been cast does not cancel that spell, but removal before the cast denies the permission for the turn.
   - Protection: the free counter suite (Force of Will, Force of Negation, Fierce Guardianship, Pact of Negation, Deflecting Swat, Mental Misstep) and the new Mana Drain.
   - Force of Negation's alternative cost works only when it is not your turn (Oracle), so it is not free when recast through Kess.
   - Kess gives **no** permission on opponents' turns. Graveyard counterspells (including Mana Drain) can be recast only against spells cast during your own turn.
2. **Stax and hate.** Graveyard exile (Rest in Peace, Bojuka Bog, Dauthi-style effects) removes Kess targets and Underworld Breach fuel. Rule of Law / Drannith Magistrate-style effects cap or deny the second cast. Thassa's Oracle with Demonic Consultation or Tainted Pact from hand remains.
3. **Mana Drain (the swap).**
   - Cast in your precombat main phase or during combat (including via Kess), the delayed trigger adds {C} at the beginning of the postcombat main phase of the same turn (ruling 2020-11-10; CR 505.1). The mana empties between steps and phases (CR 106.4), so it must be used in that phase.
   - Cast on an opponent's turn from hand, the mana arrives in your next precombat main phase.
   - Countering a zero-mana-value spell adds nothing. {U}{U} is the strictest blue cost among the counters: bounded P({U}{U}) turns 2–6 0.5028/0.6688/0.7442/0.7973/0.8395.
   - **Owner-direction flag:** the cut, Personal Tutor, is an owner addition from 2026-10-14. The fallback +Mana Drain −Deadly Rollick is staged as a complete 100.
   - **Data caveat:** EDHTop16 conversion with Mana Drain (0.125, 32 entries) is level with the field (0.1207); the case is adoption plus Kess fit, not a measured win-rate gain.
4. **Personal Tutor (the cut).** It finds a sorcery (Wheel of Fortune, Windfall, Reanimate, Demonic Tutor, Beseech the Mirror) to the top for {U}, and Kess can recast it. The losses are real but small: it cannot find the instant wins, it costs a draw step, and Mystical Tutor, Vampiric Tutor, Imperial Seal and Demonic Tutor cover the same targets.
5. **Pass C alternatives.** Jeska's Will is mana-negative below three cards in the target opponent's hand (net = hand size − 3) and lowers the blue pitch count 26 → 25. Frantic Search refunds only lands (P(three lands) on turn 3 0.4658). Both are owner-cut cards and stay owner decisions.
6. **Combo / bracket disclosure.**
   - Commander Spellbook find-my-combos: 6 → 6 complete combos:
     - Thassa's Oracle with Demonic Consultation (742-1295) or Tainted Pact (1295-3093).
     - Underworld Breach with Lotus Petal + Brain Freeze (1368-1414-4856), Lion's Eye Diamond + Brain Freeze (1368-3518-4856), Lion's Eye Diamond + Wheel of Fortune (1368-2706-3518), or Grinding Station + a zero-cost artifact (1368-3698--44).
     - Kess's own Consultation line (cast Consultation, then recast it from the graveyard in response to Oracle's trigger) is the commander's two-card variant of 742-1295.
   - Game Changers 21 → 21. **Bracket 5 (cEDH)**, unchanged.
7. **Exceptions:** none.
   - Kess, Dissident Mage (New Capenna Commander, `ncc`, released 2022-04-29) is Commander-legal per live Scryfall and is not a Game Changer.
   - All 100 cards are legal and inside U/B/R. Manamorphose and Silence were excluded as off-identity; there is no companion.
8. **Losses.** The candidate loses Personal Tutor: a one-mana sorcery tutor and one sorcery toward delirium (proxy turn 6 upper 0.401 → 0.3858). What the alternatives would lose:
   - Mana Drain over Deadly Rollick: a free exile spell for a creature threat (free again via Kess).
   - Grim Tutor over Demonic Counsel: an owner-accepted spine card.
   - Jeska's Will over Ledger Shredder: a blue pitch card and a grave-filling creature.
   - Frantic Search over Personal Tutor: the sorcery tutor, for land-only free card selection.
9. **Prior owner history.** The owner-removed and owner-rejected cards and classes in the 2026-10-14 decisions are not re-added (see the I memo).
10. **Distinctness.** Nonbasic names shared, candidate/baseline, from the registry Archidekt exports:
    - Kefka, Court Mage 80/80
    - Jeleva, Nephalia's Scourge 77/78
    - Inalla, Archmage Ritualist 71/71
    - Evelyn, the Covetous 71/71

    The swap lowers overlap: Personal Tutor is shared with Jeleva, and Mana Drain is in none of the four. The cards unique to Kess against all four are: Deadly Rollick, Dragon's Rage Channeler, Fiery Islet, Gifts Ungiven, Grinding Station, Ledger Shredder, Mana Drain, Snapcaster Mage and Training Center.
11. **Verdict:** RESEARCH_ONLY. One genuine swap; the five-swap floor is not met without padding. Not owner-presentable and NOT owner approved.
