# Don Andres, the Renegade — M7 rules snapshot (2026-10-23, America/Chicago)

Sources: the Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only) and the candidate Oracle
snapshot `data/grixis/m6/oracle_snapshots/Don_Andres__the_Renegade_M7_Scryfall_20261023.json`. This snapshot is evidence only. It is not approval.

## Legality (recorded honestly)
- **Don Andres, the Renegade** (Lost Caverns of Ixalan Commander, 2023) reads **commander: legal** on live Scryfall (2026-10-23).
  **No future-release or pending-legality project exception applies to this deck.** Every card in the baseline, the candidate and all
  staged alternatives reads commander-legal on live Scryfall and is within U/B/R. Five evaluated discovery names were rejected on
  legality or identity before judgment and are not in the snapshot: Jabs, Mistress of Mockery, Mirror Universe Intrusion and The Madcap
  Jester (not commander-legal), Bootleggers' Stash (green) and Gonti, Canny Acquisitor (Sultai).

## Commander text (current Oracle)
- {1}{U}{B}{R} 3/3 Legendary Creature — Vampire Pirate.
  - "Each creature you control but don't own gets +2/+2, has menace and deathtouch, and is a Pirate in addition to its other types."
  - "Whenever you cast a noncreature spell you don't own, create two tapped Treasure tokens."
- The commander's identity: **ownership, not control**. Stolen creatures become 4-toughness-plus menace/deathtouch Pirates; casting an
  opponent's noncreature card pays two Treasures that arrive **tapped**.

## Rules relied on
- **108.3 / 110.2 / 111.2**: a card's owner is the player who started the game with it; a permanent's owner is its card's owner; a
  token's owner is the player who created it. So Don's static ability never touches our own tokens (including Black Market Connections'
  changeling token and Treasures) and always applies to an opponent's permanent we control (Gilded Drake, Treachery, Hostage Taker,
  Jhoira, Insurrection, Coercive Recruiter) or a manifest of an opponent's card (Thieving Amalgam).
- **707.10**: a copy of a spell is not cast. Copies we create are not cards we don't own being cast, so they never trigger Don. Arcane
  Heist's cipher "cast a copy of the encoded card" casts a copy of our own card; the opponent's instant or sorcery that the copy then
  lets us cast **is** an opponent-owned card being cast, and triggers Don.
- **Tapped Treasures (Oracle) / 111.10a**: Don's Treasures enter tapped and cannot be sacrificed for mana until they untap during our next
  untap step (their mana ability has {T} in its cost). They never fund the spell that created them or a same-turn chain. Pass C #14's
  rejection of the Mnemonic Betrayal line (which assumed same-turn Treasure mana) is kept; the mechanics test checks it.
- **613.1b / 613.4c**: control changes apply in layer 2, Don's +2/+2 in layer 7c, so a creature is buffed the moment we control it.
- **608.2h**: **Mob Rule** checks power once, when it resolves, before Don's +2/+2 applies; a 3-power creature we take with "power 3 or
  less" becomes a 5-power creature afterwards. **Insurrection** untaps and steals every creature (ours included, a no-op).
- **701.40a / 701.40b / 701.40g**: a **Thieving Amalgam** manifest is the opponent's card, face down as a 2/2 — with Don a 4/4 menace
  deathtouch Pirate — and only a creature card can be turned face up. Each manifest entering under our control is a Pirate (Don), so it
  triggers **Coercive Recruiter**.
- **702.49a / 702.49c**: **Fallen Shinobi**'s ninjutsu returns an unblocked attacker "to its owner's hand": returning a creature stolen
  only until end of turn (Insurrection, Coercive Recruiter) or a dashed creature costs nothing permanent. Its combat-damage trigger lets
  us play the two exiled cards free this turn: each noncreature spell cast that way triggers Don; each creature cast that way is
  opponent-owned and gets Don's static ability; a land needs an available land play.
- **Gríma, Saruman's Footman**: can't be blocked; each combat-damage trigger exiles until an instant or sorcery, which we may cast free —
  always an opponent-owned noncreature spell, so exactly two tapped Treasures per connection when one is found. Gríma is not a Pirate, so
  Roaming Throne naming Pirate does not double Gríma's own trigger (it doubles Don's Treasure trigger, a creature's triggered ability).
- **Treachery**: "untap up to five lands" — with five or more lands tapped to cast it, the steal is mana-neutral this turn. The Aura is
  ours (303.4e) while the creature stays the opponent's, so it keeps Don's static ability as long as Treachery remains attached.
- **702.2b / 702.111b**: Don's deathtouch and menace on stolen attackers mean each needs two blockers and kills any creature that blocks it.
- **Gloomlake Verge / Blazemire Verge**: always untapped; the second colour needs an Island or Swamp (9 names in the candidate) or a
  Swamp or Mountain (9 names). The cut **Smoldering Marsh** entered tapped unless we controlled two basic lands (the list has four
  basics), and **Shipwreck Marsh** entered tapped as the first or second land.
- **Lightning Greaves (kept)**: shroud stops our own targeting of the equipped creature; Don has no targeted ability of his own, so Greaves
  costs Don nothing.

## Combo disclosure
Commander Spellbook find-my-combos (2026-10-23): **0 included combos in both the baseline and the candidate** (almost-included: 23
baseline, 19 candidate). No infinite or game-winning combo is claimed.
