# Inalla, Archmage Ritualist — M7 rules snapshot (2026-10-23, America/Chicago)

Sources:
- Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only).
- Frozen Scryfall rulings file `rulings-20261015090033.jsonl.gz` (read-only). Rulings are quoted for Inalla, Archmage Ritualist, Dualcaster Mage, Saw in Half, Essence Flux, Kefka, Court Mage // Kefka, Ruler of Ruin, Thundertrap Trainer, Spellseeker, Finale of Promise, Samut, Tyrant of Naktamun, Micromancer, Snapcaster Mage, Defense Grid, Thassa's Oracle and Scholar of the Ages.
- Candidate Oracle snapshot `data/grixis/m6/oracle_snapshots/Inalla__Archmage_Ritualist_M7_Scryfall_20261023.json` (live Scryfall `/cards/collection`, 2026-10-23). It has 0 oracle_id/text differences against the frozen 2026-10-16 oracle file for all 204 snapshot names, and 0 names missing.

This snapshot is evidence only. It is not owner approval.

## Legality (recorded honestly)
- **Inalla, Archmage Ritualist** (Commander 2017, set `c17`, released 2017-08-25) reads **commander: legal** on live Scryfall (2026-10-23).
  - Colour identity U/B/R; **not a Game Changer**. Long-released card; **no project exception applies to this deck.**
- Every card in the baseline, the candidate and all staged alternatives reads commander-legal on live Scryfall and is within U/B/R.
  - Dockside Extortionist, Jeweled Lotus and Mana Crypt are **banned** and were excluded; Culling Ritual is outside U/B/R (B/G) and was excluded.
- Game Changers (live): the baseline and the candidate (same 100 cards) both carry the same **18**:
  - Ad Nauseam, Ancient Tomb, Chrome Mox, Demonic Tutor, Force of Will, Gamble, Grim Monolith, Imperial Seal, Intuition, Lion's Eye Diamond, Mana Vault, Mox Diamond, Mystical Tutor, Necropotence, Rhystic Study, Thassa's Oracle, Underworld Breach, Vampiric Tutor.
  - **Power Bracket 5 (cEDH)**, unchanged.

## Commander text (current Oracle)
- {2}{U}{B}{R} 4/5 Legendary Creature — Human Wizard.
  - "Eminence — Whenever another nontoken Wizard you control enters, if Inalla is in the command zone or on the battlefield, you may pay {1}. If you do, create a token that's a copy of that Wizard. The token gains haste. Exile it at the beginning of the next end step."
  - "Tap five untapped Wizards you control: Target player loses 7 life."
- Eminence is an intervening-if trigger (CR 603.4): Inalla must be in the command zone or on the battlefield when the Wizard enters and when the trigger resolves (2017-08-25 eminence rulings). If Inalla changes zones in between, the trigger does nothing.
- Only one {1} per trigger (2017-08-25). The token gains haste as part of the copy effect (CR 707.9a). Tokens never trigger Eminence (nontoken clause), so Twinflame/Molten Duplication-style token copies give no extra Inalla value.
- If the Wizard has left the battlefield before Eminence resolves, {1} still makes a token from last known copiable values (2017-08-25). This keeps the Spellseeker / Scholar of the Ages sacrifice lines (Burnt Offering, Culling the Weak, Sacrifice) working.
- The tap-five ability has no {T} symbol, so summoning-sick Wizards (including tokens) can be tapped for it (2017-08-25 ruling; CR 302.6 applies only to {T}/{Q} costs). An unbounded number of Wizard tokens therefore wins with Inalla on the battlefield (7 life per five Wizards).
- Copied legendary Wizards (Kefka, Court Mage) trigger their enters abilities before the legend rule removes one (2017-08-25).

## Pass C tested Wizards
- **Dualcaster Mage** ({1}{R}{R}, flash): "When this creature enters, copy target instant or sorcery spell." It can copy any instant or sorcery spell on the stack, whoever controls it (2016-06-08). Copies are not cast (2016-06-08).
  - With **Saw in Half** (already in the 99) targeting Dualcaster Mage, each pair of half-size token copies enters, and each token's enters trigger copies the original Saw in Half, which is still on the stack. That gives unbounded tokens (Commander Spellbook 147-500; Saw in Half 2025-09-19: the tokens' enters abilities trigger). With Inalla on the battlefield, the tap-five ability wins.
  - With **Essence Flux** (already in the 99), Dualcaster Mage can blink itself repeatedly (Commander Spellbook 147-4598). Each entry is a *nontoken* Wizard entering, so Eminence triggers each time (one {1} each).
  - Dualcaster Mage was **removed by the owner** in the 2026-10-14 rebuild (canonical decisions file, removed list). It is staged only as an owner decision.
- **Micromancer** ({3}{U}): it finds only instant or sorcery cards with mana value exactly 1; {X} counts as 0 in the library (2022-09-09). It misses Tainted Pact, Demonic Tutor, Pact of Negation (MV 0), Finale of Promise (MV 2 with X=0) and the other cards listed in the bounded tests. The owner rejected it by name.
- **Snapcaster Mage** ({1}{U}, flash): flashback still requires paying the card's mana cost and obeying timing (2025-06-06); a spell cast this way is exiled afterward. The owner removed it.
- **Thundertrap Trainer** ({1}{U}): looks at the top four for a noncreature, nonland card; the Inalla token's enters ability triggers separately (offspring rulings 2024-07-26 on token copies' enters abilities). Owner red-team addition replacing Samut.

## Owner red-team rejection re-verified
- **Samut, Tyrant of Naktamun** gives our instants and sorceries split second (live Oracle). Split second stops casting other spells while it is on the stack (CR 702.61a). Samut's 2026-08-21 ruling says a resolving ability that involves casting a spell can't cast it while a split-second spell is on the stack. Finale of Promise casts its targets during resolution, while Finale itself is still on the stack (Finale 2019-05-03). The owner's rejection is rules-correct, so Samut is not re-proposed.

## Other checked interactions
- **Defense Grid**: "Each spell costs {3} more to cast except during its controller's turn." The increase applies on top of alternative costs (CR 601.2f: the total cost is the mana cost or alternative cost plus cost increases; Defense Grid 2004-10-04: only cost reductions offset it), so on opponents' turns our own Force of Will (pitch) and Pact of Negation each cost {3}, and so do Flusterstorm, Swan Song, Red Elemental Blast, Mental Misstep, An Offer You Can't Refuse and off-turn Wizard flash plays. Rejected.
- **Spellseeker**: MV <= 2 instant or sorcery; {X} = 0 in the library (2018-06-08), so it finds Finale of Promise.
- **Thassa's Oracle**: wins if library is empty as the trigger resolves (2020-01-24). The Inalla copy gives a second Oracle trigger for {1}.
- **Scholar of the Ages** returns at most two cards total (2020-11-10).
