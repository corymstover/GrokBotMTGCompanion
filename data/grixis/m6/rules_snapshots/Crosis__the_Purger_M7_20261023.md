# Crosis, the Purger — M7 rules snapshot (2026-10-23, America/Chicago)

Sources: the Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only) and the candidate Oracle
snapshot `data/grixis/m6/oracle_snapshots/Crosis__the_Purger_M7_Scryfall_20261023.json`. This snapshot is evidence only. It is not approval.

## Commander text (current Oracle)
- **Crosis, the Purger** {3}{U}{B}{R}, a 6/6 Legendary Creature — Dragon.
  - Flying.
  - "Whenever Crosis deals combat damage to a player, you may pay {2}{B}. If you do, choose a color, then that player reveals their hand and discards all cards of that color."

## Rules relied on
- **510.2 / 603.2c**: combat damage is dealt simultaneously. Each "whenever ... deals combat damage to a player" ability then triggers once per player damaged.
  - When Crosis's trigger makes a player discard several cards, that is one event with several occurrences. So "whenever an opponent discards a card" triggers once per card discarded: **Megrim** (2 damage), **Liliana's Caress** (lose 2 life) and **Raiders' Wake** (lose 2 life).
- **105.2 / 105.4**: Crosis's chosen color must be one of the five colors. **Painter's Servant** makes every card outside the battlefield the chosen color in addition to its other colors. Naming the Servant's color with Crosis empties the hand, including colorless cards and lands.
- **701.9a/b**: a discard moves the card from hand to graveyard. Crosis's and Sword's discards are chosen by the effect or the player, not at random. Bottomless Pit is random. Tergrid, God of Fright returns discarded permanent cards under our control.
- **603.3b (stack order)**: with **Sword of Feast and Famine** on Crosis, both "deals combat damage to a player" triggers are ours and we choose their order.
  - Put Crosis's trigger on the stack first and Sword's on top. Sword resolves first: the player discards a card and we untap all lands. Crosis's trigger then resolves, and the {2}{B} can be paid from the untapped lands.
  - The payment is made on resolution ("you may pay"), so the untapped lands are available for it.
- **500.8 / Aggravated Assault** ({2}{R} enchantment; "{3}{R}{R}: Untap all creatures you control. After this main phase, there is an additional combat phase followed by an additional main phase. Activate only as a sorcery").
  - It is activated in a main phase (a postcombat main phase counts). Each activation adds one combat phase plus one main phase.
  - **Finite mana math with Sword:**
    1. Crosis with Sword connects. Sword untaps the lands, then {2}{B} from lands pays for Crosis.
    2. In the next main phase, {3}{R}{R} from lands activates Assault again, which needs at least five usable lands, two of them making red.
  - A full loop (Assault + Crosis payment) needs at least 8 land mana after each untap. The loop continues only while the equipped creature connects with a player each combat. Blockers, removal, fog effects or a lost Sword end it.
  - Commander Spellbook lists **Sword of Feast and Famine + Aggravated Assault** as "Infinite combat phases" (900-3750). This packet discloses that as a two-card combo **conditional on connecting each combat**. It is not claimed as an unconditional or deterministic infinite win.
- **Rankle, Master of Pranks** (3/3 flying, **haste**): on combat damage to a player, choose any number of the three modes. The modes are symmetric ("each player"), so we choose which to apply.
  - Discard mode: each opponent's discard triggers Megrim, Caress and Wake. We discard too, and Waste Not and Tergrid do not trigger on our own discards.
- **Deadly Rollick**: "If you control a commander, you may cast this spell without paying its mana cost." Per **903.3d**, controlling a commander means a commander permanent on the battlefield, so it is free only while Crosis (or another commander we control) is on the battlefield. Otherwise it costs {3}{B}.
  - Per **118.9**, an alternative cost does not change its mana value (4).
- **Blizzard Specter** (cut) has **no haste** (Pass C correction kept). **Teferi's Puzzle Box** puts cards on the bottom and redraws; it is **not** a discard (Pass C correction kept), so it does not trigger Megrim, Caress or Wake.
- **702.16b/e**: Sword gives protection from black and green, so black or green blockers and removal cannot stop the equipped creature. **702.21a**: Brotherhood Regalia's ward {2} taxes targeted removal on Crosis, and it makes him unblockable.
- **Oppression** (cut): "Whenever a player casts a spell, that player discards a card." It is symmetric. It taxes our own spells and empties opponents' hands before Crosis can purge them.

## Damage math (finite, illustrative; see tests/test_m6_crosis_the_purger_m7_mechanics.py)
- With Liliana's Caress + Megrim + Raiders' Wake out, each opponent card discarded costs that opponent 6 life.
  - A Painter's Servant purge of a 5-card hand: 30 life, plus 6 (8 with Sword) combat damage.
  - A Wheel of Fortune or Windfall with 7-card hands: 42 life per opponent.
- These are bounded totals. No infinite damage loop is claimed.

## Combos (Commander Spellbook find-my-combos, 2026-10-23, research_challengers/*_CommanderSpellbook_20261023.json)
- Baseline: 1 included combo (2286-3221 Notion Thief + Teferi's Puzzle Box lock). Candidate: 2 included combos.
  - The baseline combo is kept.
  - New: **900-3750** (Sword of Feast and Famine + Aggravated Assault, infinite combat phases; conditional on connecting each combat).
- **Power Bracket 4** (registry ceiling 4). The 14 Game Changers are unchanged, and none of the five adds is a Game Changer.
  - The new two-card combo is disclosed. Bracket 4 permits it, and it requires a 3-mana enchantment, a 3-mana Equipment plus equip, and five or more lands.
