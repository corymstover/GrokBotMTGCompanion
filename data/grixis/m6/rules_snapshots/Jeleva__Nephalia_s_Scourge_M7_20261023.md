# Jeleva, Nephalia's Scourge — M7 rules snapshot (2026-10-23, America/Chicago)

Sources:
- Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only).
- Frozen Scryfall rulings file `rulings-20261015090033.jsonl.gz` (read-only). Rulings are quoted for Jeleva, Nephalia's Scourge, Long-Term Plans, Intuition, Galvanic Iteration, Borne Upon a Wind, Snap, Spellseeker, Final Fortune, Mind's Desire, Isochron Scepter, Arena of Glory, Exotic Orchard, Hanweir Battlements, Underworld Breach, Gemstone Caverns and Mox Opal. The frozen file has no rulings for Harmonic Prodigy, Scheming Symmetry, Torch Courier, Dramatic Reversal or Forbidden Orchard; their current Oracle text is used.
- Candidate Oracle snapshot `data/grixis/m6/oracle_snapshots/Jeleva__Nephalia_s_Scourge_M7_Scryfall_20261023.json` (live Scryfall `/cards/collection`, 2026-10-23). It has 0 oracle_id/text differences against the frozen 2026-10-16 oracle file for all 204 snapshot names, and 0 names missing.

This snapshot is evidence only. It is not owner approval.

## Legality (recorded honestly)
- **Jeleva, Nephalia's Scourge** (Commander 2013, set `c13`, released 2013-11-01) reads **commander: legal** on live Scryfall (2026-10-23).
  - Colour identity U/B/R; **not a Game Changer**. Long-released card; **no project exception applies to this deck.**
- Every card in the baseline, the candidate and all staged alternatives reads commander-legal on live Scryfall and is within U/B/R.
  - Dockside Extortionist, Jeweled Lotus and Mana Crypt are **banned** and were excluded; Manamorphose (R/G hybrid identity) and Silence (W) are outside U/B/R and were excluded.
- Game Changers (live): the baseline and the candidate (same 100 cards) both carry the same **20**:
  - Ad Nauseam, Ancient Tomb, Chrome Mox, Demonic Tutor, Fierce Guardianship, Force of Will, Gamble, Grim Monolith, Imperial Seal, Jeska's Will, Lion's Eye Diamond, Mana Vault, Mox Diamond, Mystical Tutor, Necropotence, Opposition Agent, Rhystic Study, Thassa's Oracle, Underworld Breach, Vampiric Tutor.
  - **Power Bracket 5 (cEDH)**, unchanged. Intuition (staged Pass C alternative) is also a Game Changer; the Intuition alternatives would carry 21.

## Commander text (current Oracle)
- {1}{U}{B}{R} 1/3 Legendary Creature — Vampire Wizard. Flying.
  - "When Jeleva enters, each player exiles the top X cards of their library, where X is the amount of mana spent to cast Jeleva."
  - "Whenever Jeleva attacks, you may cast an instant or sorcery spell from among cards exiled with Jeleva without paying its mana cost."
- X counts all mana actually spent, including commander tax (CR 903.8; Jeleva 2014-02-01 ruling) and extra mana from additional costs; you can't choose to overpay (2014-02-01). So the first cast is normally X=4, the second X=6.
- The two abilities are linked (CR 607.2a). If Jeleva leaves the battlefield, her exiled cards stay exiled and a new Jeleva can't use them (2013-10-17). A blink or flicker returns her uncast, so X=0 and nothing is exiled. Snap, Chain of Vapor or Otawara on Jeleva therefore resets her pool. The next cast costs two more and exiles a larger new pool.
- The free cast happens while the attack trigger resolves, before blockers are declared. If you don't cast then, you can't later (2013-10-17). Card-type timing is ignored (2013-10-17). {X} must be 0 (2013-10-17). Additional costs may be paid, but alternative costs may not (2013-10-17).
- Jeleva needs haste or to have been under control since the start of the turn to attack (CR 302.6, 702.10b). The deck's enablers are Torch Courier, Lightning Greaves, Arena of Glory (Arena mana spent on Jeleva gives her haste; 2024-06-07) and Borne Upon a Wind (cast Jeleva with flash in an opponent's end step).
- **Harmonic Prodigy**: "If a triggered ability of a Shaman or another Wizard you control triggers, that ability triggers an additional time" (CR 603.2d). Jeleva is a Wizard, so both her ETB (two exiles of X each) and her attack trigger (two free casts) double.

## Pass C tested cards
- **Long-Term Plans** ({2}{U} instant): the card goes third from the top, or to the bottom if the library has fewer than three cards (2004-10-04). Jeleva's ETB exiles the top X >= 4 immediately, so the staged card is captured **without waiting for draws**. The GrokBot advisory's "waits two draws" premise is false for the Jeleva line; it applies only to drawing the card.
- **Intuition** ({2}{U} instant, Game Changer): it targets an opponent, and that opponent chooses which revealed card goes to your hand (2006-07-15); the other two go to the graveyard. It never puts a card into the library, so Jeleva's ETB can't capture it. The exhaustive hostile-choice enumeration is in the bounded measured tests (T2). Underworld Breach is stranded in the graveyard because escape is granted only while Breach is on the battlefield (Underworld Breach 2020-01-24 rulings and Oracle).
- **Scheming Symmetry** ({B} sorcery): "Choose two target players." That is one instance of "target", so it needs two different players (CR 115.3), and some other player always tutors too. The card it stages goes on top, where Jeleva's ETB captures it.
- **Galvanic Iteration** ({U}{R} instant, flashback {1}{U}{R}): it copies the next instant or sorcery you cast this turn. The copy is created on the stack and is not cast (CR 707.10; Galvanic Iteration 2021-09-24), so it adds no storm count and no prowess or cast trigger. A copy of a storm spell (Mind's Desire, Brain Freeze) gives one more resolution only (Mind's Desire 2022-12-08). A copied Final Fortune gives a second extra turn, but you take the most recent first (Final Fortune 2022-12-08) and lose at that turn's end step, so it adds nothing.
- **Borne Upon a Wind** ({1}{U} instant): it gives flash only to *spells* you cast this turn (2023-06-16). Jeleva is a spell from the command zone, so she can be cast in an opponent's end step and attack on your turn without a haste source (CR 302.6).

## Other checked interactions
- **Snap** ({1}{U} instant): it returns target creature to its owner's hand and untaps up to two lands; you choose the lands on resolution, and they need not be yours (2022-12-08). On Jeleva it is free protection plus a reset to a larger X. It answers creature hate pieces at tempo.
- **Spellseeker**: it finds an instant or sorcery with MV <= 2; {X} counts as 0 in the library (2018-06-08). It is a Wizard, so Harmonic Prodigy doubles its ETB.
- **Dramatic Reversal + Isochron Scepter**: the copy is cast while the Scepter ability resolves (2020-08-07), so storm counts it. With at least {3} of nonland mana permanents (for example Sol Ring plus a Talisman) it makes unbounded mana and storm (Commander Spellbook 4821-5261). It is a generic two-card Grixis package with no Jeleva text; the owner blueprint does not contain it.
- **Arena of Glory**: it enters tapped unless you control a Mountain, and that Mountain must already be there (2024-06-07). Its RR exert mana can be spent on anything (2024-06-07). **Hanweir Battlements** gives haste for {R} plus tap but makes only {C}. **Exotic Orchard** produces only colours an opponent's lands could produce (2009-02-01), so it gives nothing on turn 1 on the play. **Forbidden Orchard** gives any colour and an opponent a 1/1 Spirit; the Spirit can't block flying Jeleva.
- **Gemstone Caverns**: "opening hand" means the hand after mulligans (2021-03-19). It gives any colour only with a luck counter, which needs it in the opening hand while you are not the starting player.
- **Mox Opal**: legend-rule interaction (2020-08-07). Metalcraft needs three artifacts. Given Opal, P(>= 2 other artifacts among the 6 other opening cards) = 0.2277 over the actual 99 (bounded test T4).
