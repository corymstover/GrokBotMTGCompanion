# Kess, Dissident Mage — M7 rules snapshot (2026-10-23, America/Chicago)

Sources:
- Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only).
- Frozen Scryfall rulings file `rulings-20261015090033.jsonl.gz` (read-only). Rulings are quoted for Kess, Dissident Mage, Mana Drain, Personal Tutor, Deadly Rollick, Displacer Kitten, Demonic Consultation, Thassa's Oracle, Jeska's Will, Frantic Search, Demonic Counsel, Underworld Breach, Ledger Shredder, Grim Tutor, Final Fortune and Gifts Ungiven. The frozen file has no rulings for Spell Pierce; its current Oracle text is used.
- Candidate Oracle snapshot `data/grixis/m6/oracle_snapshots/Kess__Dissident_Mage_M7_Scryfall_20261023.json` (live Scryfall `/cards/collection`, 2026-10-23). It has 0 oracle_id/text differences against the frozen 2026-10-16 oracle file for all 187 snapshot names, and 0 names missing.

This snapshot is evidence only. It is not owner approval.

## Legality (recorded honestly)
- **Kess, Dissident Mage** (New Capenna Commander, set `ncc`, released 2022-04-29; oracle_id f5092c14-eec4-472c-999c-ba96c36b2fbb) reads **commander: legal** on live Scryfall (2026-10-23).
  - Colour identity U/B/R; **not a Game Changer**. Released years ago; **no project exception applies to this deck.**
- Every card in the baseline, the candidate and all eleven staged alternatives reads commander-legal on live Scryfall and is within U/B/R.
  - Manamorphose (R/G hybrid), Orim's Chant (W), Sea of Clouds (W/U) and Silence (W) were evaluated and excluded as outside U/B/R. "Fire // Ice" did not resolve in the live batch and was dropped (fringe).
- Game Changers (live): the baseline and the candidate both carry the same **21** (neither Personal Tutor nor Mana Drain is a Game Changer):
  - Ad Nauseam, Ancient Tomb, Chrome Mox, Demonic Tutor, Fierce Guardianship, Force of Will, Gamble, Gifts Ungiven, Grim Monolith, Imperial Seal, Intuition, Lion's Eye Diamond, Mana Vault, Mox Diamond, Mystical Tutor, Necropotence, Orcish Bowmasters, Rhystic Study, Thassa's Oracle, Underworld Breach, Vampiric Tutor.
  - **Power Bracket 5 (fringe cEDH, owner-approved)**, unchanged.

## Commander text (current Oracle)
- {1}{U}{B}{R} 3/4 Legendary Creature — Human Wizard. Flying. "Once during each of your turns, you may cast an instant or sorcery spell from your graveyard. If a spell cast this way would be put into your graveyard, exile it instead."
- Rulings (2019-06-14): "You must pay the costs to cast that card. If it has an alternative cost, you may cast it for that cost instead." / "You must follow the normal timing permissions and restrictions of the card you cast from your graveyard." / "If you cast one instant or sorcery card from your graveyard and then have a new Kess come under your control in the same turn, you may cast another instant or sorcery card from your graveyard that turn." / "If you cast a card from your graveyard using another permission (such as that of flashback), Kess's effect doesn't apply."
- CR 117.1a: A player may cast an instant spell any time they have priority. A player may cast a noninstant spell during their main phase any time they have priority and the stack is empty.
- CR 608.2n: As the final part of an instant or sorcery spell’s resolution, the spell is put into its owner’s graveyard. As the final part of an ability’s resolution, the ability is removed from the stack and ceases to exist. (Kess replaces this with exile for the recast spell.)
- CR 400.7: An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions. A blinked Kess (Displacer Kitten) is a new object, so it grants a fresh permission (ruling above).
- CR 118.9: Some spells have alternative costs. An alternative cost is a cost listed in a spell’s text, or applied to it from another effect, that its controller may pay rather than paying the spell’s mana cost. Alternative costs are usually phrased, “You may [action] rather than pay [this object’s] mana cost,” or “You may cast [t... Alternative costs (Force of Will, Fierce Guardianship, Pact of Negation, Deadly Rollick, Mindbreak Trap, Deflecting Swat, Force of Negation) may be used for the Kess recast on your turn; Force of Negation's free cost only works on an opponent's turn, so it is not free via Kess.
- CR 903.8: A player may cast a commander they own from the command zone. A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game. This additional cost is informally known as the “commander tax.”
- Kess gives **no** permission on opponents' turns: graveyard counterspells are only recastable during your own turn.

## Selected change: +Mana Drain −Personal Tutor
- Mana Drain ({U}{U} instant): "Counter target spell. At the beginning of your next main phase, add an amount of {C} equal to that spell's mana value."
  - Ruling (2020-11-10): "Mana Drain's delayed triggered ability will usually trigger at the beginning of your precombat main phase. However, if you cast Mana Drain during your precombat main phase or during your combat phase, its delayed triggered ability will trigger at the beginning of that turn's postcombat main phase."
  - CR 505.1: There are two main phases in a turn. In each turn, the first main phase (also known as the precombat main phase) and the second main phase (also known as the postcombat main phase) are separated by the combat phase (see rule 506, “Combat Phase”). The precombat and postcombat main phases are individually and collectivel...
  - CR 106.4: When an effect instructs a player to add mana, that mana goes into a player’s mana pool. From there, it can be used to pay costs immediately, or it can stay in the player’s mana pool as unspent mana. Each player’s mana pool empties at the end of each step and phase, and the player is said to lose this mana. Cards with ...
  - Consequence for Kess: recast from the graveyard during your precombat main phase (for example against an opponent's response to your combo, or their instant), the colourless mana arrives in your postcombat main phase of the same turn. From hand on an opponent's turn it is a hard counter plus mana on your next turn. Not a Game Changer.
- Cut: Personal Tutor ({U} sorcery): "Search your library for a sorcery card, reveal it, then shuffle and put that card on top." Ruling (2004-10-04): "Because the “search” requires you to find a card with certain characteristics, you don’t have to find the card if you don’t want to." It cannot find the instant wincons (Demonic Consultation, Tainted Pact, Brain Freeze) and puts the card on top, not in hand; Mystical Tutor (instant) overlaps it.
- Staged owner-respecting fallback cut: Deadly Rollick ({3}{B} instant, free with a commander; exile target creature). Rulings (2020-04-17): "It doesn't matter whose commander you control. Any one will do." Recast via Kess it is free again (alternative cost, CR 118.9), which is why it is retained in the main candidate.

## Combo rules (unchanged by the swap)
- Demonic Consultation: "If you don't reveal the named card (perhaps because it was in the top six cards of your library), you'll end up exiling your entire library. You don't lose the game at that point, but will lose the next time you're instructed to draw a card." (2008-10-01)
- Thassa's Oracle: "If your devotion to blue is zero at the time the triggered ability of Thassa's Oracle resolves, you don't look at or move any cards in your library. If you have no cards in your library, you win the game." (2020-01-24). Kess line: Consultation from hand finds Oracle; cast Oracle; with the enter trigger on the stack, recast Consultation from the graveyard via Kess naming a card not in the library.
- Underworld Breach: "If a card has multiple abilities giving you permission to cast it, such as two escape abilities or an escape ability and a flashback ability, you choose which one to apply." (2020-01-24). Escape casts do not use Kess's permission.
- Gifts Ungiven: "If you find one or two cards, your opponent must choose for them to be put into your graveyard, even if they don't want to." (2017-03-14)
- Displacer Kitten: "When the card returns to the battlefield, it will be a new object with no connection to the card that was exiled." (2022-06-10)

## Pass C tested cards
- **Jeska's Will** ({2}{R} sorcery; owner-cut 2026-10-14): "Use the number of cards in the target opponent's hand as Jeska's Will resolves to determine how much {R} to add." (2026-03-20). With Kess (a commander) both modes are chosen; net mana = hand size − 3. Red only.
- **Ledger Shredder** ({1}{U}, owner spine): "Spells that were cast before Ledger Shredder entered the battlefield count." (2022-04-29). Connives on every player's second spell each turn; a blue pitch card for Force of Will / Force of Negation.
- **Frantic Search** ({2}{U} instant; owner-cut): "You choose which lands to untap as the spell resolves. They aren't targeted, and they don't have to be lands that you control." (2022-12-08). Free only with three untapped lands (not rocks).
- **Demonic Counsel** ({1}{B} sorcery; owner addition): "In the case where Demonic Counsel's delirium ability allows you to search your library for any card, you won't have to reveal that card." (2024-09-20). No Demon in the 99, so delirium is required.
- **Grim Tutor**: "You don't reveal the card you search for." (2020-06-23); 3 mana, 3 life.
- **Final Fortune**: "If you end up skipping the extra turn that is gained, you do not lose the game." (2004-10-04). The extra turn is another of your turns, so Kess grants another graveyard cast.
