# Gwendlyn Di Corci — M7 rules snapshot (2026-10-23, America/Chicago)

Sources:
- Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only).
- Frozen Scryfall rulings file `rulings-20261015090033.jsonl.gz` (read-only). Rulings are quoted for Dauthi Voidwalker, Tergrid, God of Fright // Tergrid's Lantern, Tinybones, Bauble Burglar, Bloodchief Ascension, Illusionist's Bracers, Magewright's Stone, Rings of Brighthearth, Chains of Mephistopheles, Notion Thief and Anvil of Bogardan. The frozen file has no rulings for Gwendlyn Di Corci, Hymn to Tourach, Aphetto Alchemist or Pemmin's Aura.
- Candidate Oracle snapshot `data/grixis/m6/oracle_snapshots/Gwendlyn_Di_Corci_M7_Scryfall_20261023.json` (live Scryfall `/cards/collection`, 2026-10-23). It has 0 oracle_id/text differences against the frozen 2026-10-16 oracle file for all 208 snapshot names, and 0 names missing.

This snapshot is evidence only. It is not owner approval.

## Legality (recorded honestly)
- **Gwendlyn Di Corci** (Legends, set `leg`, released 1994-06-01; reprinted in Masters Edition III, `me3`, 2009-09-07; Reserved List) reads **commander: legal** on live Scryfall (2026-10-23).
  - Colour identity U/B/R; **not a Game Changer**. Long-released card; **no project exception applies to this deck.**
- Every card in the baseline, the candidate and all staged alternatives reads commander-legal on live Scryfall and is within U/B/R.
  - Jeweled Lotus is **banned** and was excluded.
- Game Changers (live): the baseline and the candidate both carry the same **17**:
  - Ancient Tomb, Chrome Mox, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Force of Will, Gamble, Imperial Seal, Lion's Eye Diamond, Mystical Tutor, Notion Thief, Opposition Agent, Orcish Bowmasters, Rhystic Study, Tergrid, God of Fright // Tergrid's Lantern, Underworld Breach, Vampiric Tutor.
  - Neither Hymn to Tourach nor Dauthi Voidwalker is a Game Changer.
  - **Power Bracket 4 (Optimized)**, unchanged.

## Commander text (current Oracle)
- {U}{B}{B}{R} 3/5 Legendary Creature — Human Rogue.
  - "{T}: Target player discards a card at random. Activate only during your turn."
- The ability is not a mana ability (it targets; CR 605.1a), so Illusionist's Bracers copies it and Magewright's Stone or Pemmin's Aura can untap her for another activation.
- "Activate only during your turn" is not sorcery timing (CR 602.5d contrast), so she can be activated in response, in combat and with the stack non-empty on our turn.

## Rules relied on
- **Random discard (CR 701.9a/b)**: the discarded card moves from hand to its owner's graveyard; Gwendlyn, Hymn to Tourach and Mind Twist choose at random.
- **Dauthi Voidwalker is a replacement effect (CR 614.1a, "instead")**: while it is on the battlefield, a card that would be put into an opponent's graveyard from anywhere is exiled with a void counter instead.
  - Ruling (2021-06-18): "If your opponent discards a card while you control Dauthi Voidwalker, abilities that function when that card is discarded still work, even though that card never reaches that player's graveyard." So Liliana's Caress, Waste Not, Geth's Grimoire, Tourach, Dread Cantor and Tinybones, Trinket Thief still work.
  - Ruling (2021-06-18): nontoken creatures opponents control are exiled instead of dying; die-triggers do not trigger.
  - **Tergrid, God of Fright** triggers on the discard or sacrifice, but must "put that card **from a graveyard** onto the battlefield". Ruling (2021-02-05): "If the card leaves the graveyard before Tergrid's ability resolves, you can't put it onto the battlefield". Under Dauthi the card never reaches a graveyard, so Tergrid gets nothing. This covers both Gwendlyn's discards and Tergrid's Lantern edicts.
  - **Tinybones, Bauble Burglar** triggers on the discard but must "exile it **from their graveyard** with a stash counter". Under Dauthi the card is already in exile with a void counter and not a stash counter, so it cannot be played with Tinybones.
  - **Bloodchief Ascension**'s payoff ("Whenever a card is put into an opponent's graveyard from anywhere") never triggers under Dauthi. Its quest-counter ability still works because it checks life loss.
  - Dauthi's own payoff: once, {T} and sacrifice it to play one void-countered card without paying its mana cost (X = 0; ruling 2021-06-18).
- **Hymn to Tourach** ({B}{B} sorcery, "Target player discards two cards at random."): uses the same BB as Dauthi. It adds two random discards that feed every discard trigger in the deck, and all of them reach the graveyard for Tergrid, Burglar and Ascension.
- **Illusionist's Bracers** (rulings 2013-01-24): copies non-mana activated abilities of the equipped creature, and new targets may be chosen.
  - Aphetto Alchemist ("{T}: Untap target artifact or creature.") is not a mana ability (it targets), so with Bracers the ability untaps a target and the copy untaps the Alchemist.
  - That is unbounded untaps. Repeated on a mana rock it gives unbounded mana; repeated on Gwendlyn it gives unbounded random discards on our turn (Commander Spellbook 283-4091).
  - This is a generic two-card engine, the class the owner rejected (Mindcrank + Bloodchief Ascension), so it is staged as an owner decision only.
- **Magewright's Stone** ruling (2006-05-01): it untaps a creature that has an activated ability with {T} in its cost. Gwendlyn and Jace's Archivist qualify.
- **Pemmin's Aura**: {U} untap; the shroud mode is optional, and Gwendlyn's ability targets a player, not herself.
- **Rings of Brighthearth** rulings (2020-11-10): pay {2} to copy a non-mana activated ability once per activation. It copies Gwendlyn's ability for {2}, at the cost of a slot.
- **Chains of Mephistopheles** rulings (2007-09-16): each extra draw is replaced. With an empty hand the player mills instead. Our own wheel draws are also replaced, and draw triggers (Orcish Bowmasters, Sheoldred, Underworld Dreams) do not fire on replaced draws.
- **Notion Thief** ruling (2018-03-16): the opponent "still discards a card" when a draw-then-discard has its draw replaced. Anvil of Bogardan's ruling (2004-10-04) agrees: "If the draw part of the effect is skipped due to a replacement effect, the discard part of the effect is not skipped." So with Notion Thief, Anvil makes each opponent discard without drawing, and we draw.

## Combo and infinite boundaries (no unsupported claims)
- Commander Spellbook find-my-combos (2026-10-23):
  - The baseline and the candidate each contain one complete combo, 1368-2706-3518: Underworld Breach + Lion's Eye Diamond + Wheel of Fortune.
  - Almost-included counts are 52 for the baseline and 50 for the candidate. The Dauthi lines are one card short and not decision-relevant.
- The Pass C Aphetto variant adds 283-4091 (Illusionist's Bracers + Aphetto Alchemist), with 60 almost-included. This is a new generic two-card infinite and the reason the variant is not a first-pass swap.
- The candidate swap creates and removes no complete combo.
