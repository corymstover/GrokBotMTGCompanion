# Ashnod the Uncaring — M7 rules snapshot (2026-10-23, America/Chicago)

Source: Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only) and the candidate Oracle
snapshot `data/grixis/m6/oracle_snapshots/Ashnod_the_Uncaring_M7_Scryfall_20261023.json`. Evidence only; not approval.

## Commander text (current Oracle)
"Deathtouch. Whenever you activate an ability of an artifact or creature that isn't a mana ability, if one or more permanents
were sacrificed to activate it, you may copy that ability. You may choose new targets for the copy." There is **no
once-per-turn limit**; the tracker's "once-per-turn" wording is stale.

## Rules relied on
- **602.2b / 601.2c / 601.2h**: an activated ability's targets are chosen before costs are paid; sacrifices that are part of
  the cost happen during activation, so Ashnod's trigger sees "permanents were sacrificed to activate it". Effects that
  sacrifice on resolution (Goblin Welder's swap, Toxic Deluge, Priest's opponents' edicts) do not qualify.
- **605.1a**: abilities that could add mana, have no target and are not loyalty abilities are mana abilities and are never
  copied (Krark-Clan Ironworks, Ashnod's Altar, Lotus Petal, Treasure, Mox Opal, Crime Novelist's trigger is a trigger).
  Priest of Forgotten Gods' ability targets players, so it is **not** a mana ability and is copied (its BB is added again).
- **Lands**: Ashnod only sees abilities of artifacts or creatures. Buried Ruin, Inventors' Fair and fetches are not copied;
  artifact lands (Treasure Vault, Seat of the Synod, Vault of Whispers, Great Furnace) are artifacts and are copied when a
  sacrifice is in the cost (Treasure Vault X=2 -> 4 Treasures).
- **707.10**: a copy of an activated ability is not activated; activation restrictions ("activate only as a sorcery",
  tap symbols, 302.6 summoning sickness) apply only to the original. **707.10c**: the copy may choose new targets; the copy
  is put on the stack above the original and resolves first.
- **302.6**: Goblin Engineer, Audacious Reshapers, Sage of Lat-Nam, Priest of Forgotten Gods need to have been controlled
  since the start of our turn to use {T} abilities.

## Combos (Commander Spellbook find-my-combos, 2026-10-23, research_challengers/*_CommanderSpellbook_20261023.json)
- Baseline 15 included combos, none uses Ashnod. Candidate 16: two Foundry Inspector variants (777-1020-2866-4659,
  777-1020-2034-2866) leave; the same Trawler/Retriever lines remain through Etherium Sculptor / Enthusiastic Mechanaut.
- **New 1414-1649-2068-4404 Ashnod + Goblin Engineer + Corridor Monitor + Lotus Petal** (hand-verified): Petal in the
  graveyard after tapping it for R; activate non-sick Engineer ({R}, {T}, sacrifice Monitor) targeting Petal; Ashnod copies,
  copy targets Monitor; copy resolves: Monitor returns, ETB untaps Engineer; original resolves: Petal returns; tap Petal
  for R, repeat. Net mana zero, any number of loops, stop at will. Each loop: two artifacts sacrificed, two artifact ETBs,
  one creature death. Payoffs in deck: Disciple (2 life/loop), Marionette Apprentice (2), Mayhem Devil (2 damage),
  Reckless Fireweaver (2), Crime Novelist (+RR per loop -> infinite red mana). Requires graveyard access (Rest in Peace stops it).
- **New 2034-2068-2762-5346 / 2068-2762-4659-5346 Ashnod + Thopter Squadron + Crime Novelist + Ashnod's Altar or KCI**
  (hand-verified, sorcery speed): remove a counter ({1}) -> Thopter A; pay {1} and sacrifice A to Squadron (copied: +2
  counters; Novelist +R); remove a counter ({1}) -> Thopter B; sacrifice B to Altar/KCI (+CC, Novelist +R). Per cycle:
  counters +0, mana +1, two Thopter ETB/deaths. Without Novelist the cycle is -1 mana (not infinite).
- No other new complete combo was reported; infinite claims are limited to these Spellbook-listed lines. Bracket stays 4.
