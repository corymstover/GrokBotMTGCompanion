# Fire Lord Azula — M7 rules snapshot (2026-10-23, America/Chicago)

Sources:
- Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only).
- Frozen Scryfall rulings file `rulings-20261015090033.jsonl.gz` (read-only). Rulings are quoted for Fire Lord Azula, Samut, Tyrant of Naktamun, Beseech the Mirror, Narset's Reversal, Turnabout, Flashback and Mistrise Village.
- Candidate Oracle snapshot `data/grixis/m6/oracle_snapshots/Fire_Lord_Azula_M7_Scryfall_20261023.json` (live Scryfall `/cards/collection`, 2026-10-23). It has 0 oracle_id/text differences against the frozen 2026-10-16 oracle file for all 205 snapshot names.

This snapshot is evidence only. It is not owner approval.

## Legality (recorded honestly)
- **Fire Lord Azula** (Avatar: The Last Airbender, set `tla`, released 2025-11-21) reads **commander: legal** on live Scryfall (2026-10-23).
  - Colour identity U/B/R; **not a Game Changer**. The set is released; no preview or pre-release caveat applies.
  - **No future-release or pending-legality project exception applies to this deck.**
- Every card in the baseline, the candidate and all staged alternatives reads commander-legal on live Scryfall and is within U/B/R.
  - Evaluated discovery names outside U/B/R were excluded from the snapshot and are listed there (Manamorphose, Silence).
- Game Changers (live): the baseline and the candidate both carry the same **20**:
  - Ad Nauseam, Ancient Tomb, Chrome Mox, Demonic Tutor, Fierce Guardianship, Force of Will, Gamble, Grim Monolith, Imperial Seal, Jeska's Will, Lion's Eye Diamond, Mana Vault, Mox Diamond, Mystical Tutor, Necropotence, Orcish Bowmasters, Rhystic Study, Thassa's Oracle, Underworld Breach, Vampiric Tutor.
  - No primary add and no cut is a Game Changer.
  - **Power Bracket 5 (cEDH)**, unchanged.

## Commander text (current Oracle)
- {1}{U}{B}{R} 4/4 Legendary Creature — Human Noble.
  - "Firebending 2 (Whenever this creature attacks, add {R}{R}. This mana lasts until end of combat.)"
  - "Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell. You may choose new targets for the copy. (A copy of a permanent spell becomes a token.)"
- Azula rulings (2025-10-02): the copy is not cast; additional costs paid for the original are treated as paid for the copy; X is copied; the copy resolves even if the original is countered; firebending is not a mana ability; a permanent-spell copy becomes a token (legendary copies then meet the legend rule, 704.5j).

## Rules relied on
- **702.61a / 702.61b (split second)**: "As long as this spell is on the stack, players can't cast other spells or activate abilities that aren't mana abilities." Triggered abilities still trigger (Azula's copy still happens, as the owner noted).
  - Samut ruling (2026-08-21): "If the resolution of a triggered ability involves casting a spell, that spell can't be cast if a spell with split second is on the stack." The same restriction applies to a resolving spell: a bargained **Beseech the Mirror** with split second is still on the stack while it resolves, so its free cast is impossible and the card goes to hand.
  - Under Samut, **Narset's Reversal cannot be cast** while our Frantic Search or Turnabout is on the stack (each has split second). Both commander loops (Spellbook 11-2196-7089 and 11-4276-7089) therefore require Samut to be absent. Breach lines that cast spells one at a time still work.
  - Upside of Samut: opponents can't counter our instants/sorceries; it does not protect creature spells (Thassa's Oracle) or triggers.
- **Narset's Reversal** rulings (2019-05-03): copy any instant/sorcery spell, then return it to hand; returning works on uncounterable spells; copies returned to hand cease to exist.
- **Turnabout** ruling (2022-12-08): tap/untap and the permanent type are chosen on resolution, so Azula's copy and the original can each choose separately (for example untap our lands, or tap two different opponents' lands).
- **Turnabout loop (Spellbook 11-4276-7089)**: with Azula attacking, cast Turnabout ({2}{U}{U}); Azula copies it. Cast Narset's Reversal ({U}{U}) targeting Turnabout; Azula copies Reversal, the copy retargets the original Reversal, so a further Turnabout copy is made and both cards return to hand. Two Turnabout resolutions (the Azula copy and the Reversal copy) each untap all our lands, and we tap the lands for mana between the two resolutions (mana abilities while holding priority; the pool empties only at the end of the step): net mana per iteration 2L - 6, where L is our untapped-able lands. Unbounded storm when L >= 3, unbounded mana when L >= 4 (colour limited by lands). Win routes in the candidate (Vivi Ornitier is cut): unbounded mana pays for a tutor to Brain Freeze, whose storm copies mill every opponent; the Frantic Search loop also draws the deck for Thassa's Oracle. Each iteration is a finite, optional sequence; we stop when we choose.
- **Flashback** rulings (2026-03-20): the granted flashback cost equals the card's mana cost; a card cast this way is exiled; timing rules still apply. Azula copies Flashback, so two instants/sorceries gain flashback; each recast while she is attacking is copied again.
- **Unexpected Windfall**: discard is an additional cost; per the Azula ruling the copy also draws two and makes two Treasures without a second discard (4 cards, 4 Treasures total).
- **Sink into Stupor // Soporific Springs** (MDFC, 712): played as an untapped U land for 3 life, or cast ({1}{U}{U} instant) to return a spell or nonland permanent an opponent controls to its owner's hand; Azula's copy can bounce a second opponent target.
- **Mistrise Village** ruling (2025-04-04): enters untapped only if we already control a Mountain or Forest (Badlands, Volcanic Island, Steam Vents and the Mountain-typed fetch targets qualify). {U},{T}: the next spell this turn can't be countered.
- **Gemstone Caverns**: rainbow only if in the opening hand when not the starting player (luck counter); otherwise {C}.

## Combo and infinite boundaries (no unsupported claims)
- Commander Spellbook find-my-combos (2026-10-23): baseline 9 complete combos, candidate 10. None is lost; the candidate gains 11-4276-7089 (Azula + Narset's Reversal + Turnabout).
  - Kept: Oracle + Demonic Consultation / Tainted Pact; Breach + Lotus Petal / LED + Brain Freeze; Breach + Wheel of Fortune + Jeska's Will; Breach + LED + Wheel of Fortune; Breach + Grinding Station; Azula + Narset's Reversal + Frantic Search; Azula + Breach + Frantic Search.
- With Samut cut, the two Azula + Reversal loops and the bargained-Beseech free cast are no longer self-disabled.
- No other new combo or infinite is claimed for any add. Storm-Kiln Artist + Azula + Narset's Reversal (11-5195-7089) is real but the Artist is owner-removed and only appears in a staged Pass C test list.
