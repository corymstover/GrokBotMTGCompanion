# Anhelo, the Painter — M7 rules snapshot (2026-10-23, America/Chicago)

Source: Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`) and the candidate Oracle
snapshot `data/grixis/m6/oracle_snapshots/Anhelo__the_Painter_M7_Scryfall_20261023.json`. Evidence only; not approval.

## Rules relied on
- **702.153a Casualty N**: additional cost "you may sacrifice a creature with power N or greater"; when cast, if the cost was
  paid, copy it (new targets allowed). Anhelo grants casualty 2 to the *first* instant or sorcery *cast* each turn (any
  turn, including opponents'). Copies are not cast, so they never consume the slot and never trigger "whenever you cast".
  Power is checked as the cost is paid (601.2h), so a 2/1 or 3/1 qualifies; a 1/1 Pest/Fractal-0 does not.
- Consequence: an instant/sorcery that *creates* the fodder (Startle, Rotten Reunion, Waste Management, Talrand's
  Invocation) is itself the first spell, so its token cannot pay that turn's casualty. Permanent or recursive bodies can.
- **702.152 Blitz**: cast for blitz cost -> haste, "When this creature dies, draw a card", sacrificed at next end step.
  Tenacious Underdog may be cast from the graveyard using blitz (sorcery timing, main phase, our turn). Sacrificing the
  blitzed Underdog to casualty draws the card and returns it to the graveyard for reuse.
- **702.62 Suspend**: Sinister Concierge's dies trigger exiles it with three time counters and gives suspend; also exiles up to
  one target creature with three counters (that creature gains suspend and its owner recasts it free, with haste, later).
  If Concierge left the graveyard before the trigger resolves, nothing is exiled from it (choose "may" = no).
- **Landfall cast permission (Skyclave Shade)**: only while the card is in the graveyard and it's our turn; the permission
  lasts that turn. Kicker remains payable when cast from the graveyard (702.33).
- **Dogged Detective**: returns to hand when an opponent draws their second card in a turn (checked per opponent).
- **Bedevil**: instant; as the first instant on an opponent's turn it gets casualty 2 and the copy may target a second
  artifact, creature or planeswalker.
- Ghoulish Procession triggers once per turn on nontoken creature deaths; the four new bodies are nontoken.

## Combo lines unchanged by the candidate
Reiterate + Mana Geyser/Jeska's Will (buyback loop), Narset's Reversal + Twinning Staff/Reiterate, Dualcaster Mage +
Twinflame, Primal Wellspring + Frantic Search; outlets Ral, Storm Conduit and Storm-Kiln Artist Treasures. No combo piece
is cut. Storm-Kiln Artist's static power drops by up to 3 (three fewer rocks); it still has >= 2 power with any one artifact.
