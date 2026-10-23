# Edea, Possessed Sorceress — M7 rules snapshot (2026-10-23, America/Chicago)

Sources: the Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only), the frozen Scryfall rulings
file `rulings-20261015090033.jsonl.gz` (read-only), and the candidate Oracle snapshot
`data/grixis/m6/oracle_snapshots/Edea__Possessed_Sorceress_M7_Scryfall_20261023.json`. This snapshot is evidence only. It is not approval.

## Legality (recorded honestly)
- **Edea, Possessed Sorceress** (Final Fantasy Commander, set `fic`, released 2025-12-05, its only printing) reads **commander: legal** on
  live Scryfall (2026-10-23), colour identity U/B/R, **not a Game Changer**, oracle_id 7beb7505-b765-486d-a205-78325922a10f.
  **No future-release or pending-legality project exception applies to this deck.** Every card in the baseline, the candidate and all
  staged alternatives reads commander-legal on live Scryfall and is within U/B/R. Jabs, Mistress of Mockery (an owner-rejected discovery
  name) reads `not_legal` on live Scryfall and is excluded; no exception is applied.
- Game Changers (live): baseline and candidate both carry exactly **Ancient Tomb, Demonic Tutor, Fierce Guardianship** (3). No add is a
  Game Changer.

## Commander text (current Oracle)
- {2}{U}{B}{R} 2/5 Legendary Creature — Human Warlock. Ward {2}.
  - "At the beginning of combat on your turn, gain control of target creature an opponent controls until end of turn. Untap that
    creature. It gains haste until end of turn."
  - "Whenever a creature you control but don't own dies, return it to the battlefield under its owner's control and you draw a card."
- Identity: **borrow the best opposing creature every combat, use it, then sacrifice it for value; Edea gives it back and draws.**
  Stealing and sacrificing is therefore card advantage and outlet value, **not removal** (the creature comes back to its owner).

## Rules relied on
- **500.8 / 506.1**: each additional combat phase has its own beginning of combat step, so Edea's first ability triggers again in every
  extra combat (Karlach, Full Throttle, and the adds Combat Celebrant and Aggravated Assault). Aggravated Assault's ruling (2004-10-04):
  it may be activated more than once a turn with enough mana; it is sorcery-speed, so it is activated in each additional main phase.
  Combat Celebrant's rulings (2017-04-18): exert only as it is declared as an attacker; there is no main phase between the combats it adds.
- **603.2b**: an "at the beginning of" ability triggers only for permanents that have it when the step begins. **Irma timing caveat:**
  when Irma first becomes a copy of Edea at the beginning of combat, that copy does not trigger in that step; from the next combat on
  (this turn or later turns, since Irma's copy has no duration) she is a second Edea.
- **603.2d** (Roaming Throne naming Human or Warlock): Edea's triggers trigger an additional time; these are additional triggers, not
  copies (Roaming Throne ruling 2023-11-10). Combat Celebrant is a Human, so a Human Throne also doubles its "when you do" trigger. This
  doubling is disclosed but not used in the counts.
- **603.3b**: we put our simultaneous triggers on the stack in the order we choose. **Kaya's Ghostform**: order Ghostform's trigger to
  resolve before Edea's. Ghostform returns the card under our control (ruling 2019-05-03: a permanent we control but don't own returns
  under our control). Edea's trigger then finds a new object (**400.7**) and does as much as possible (**609.3**): no return, but **the
  draw still happens**, because the draw is not conditional on the return.
- **707.2**: Hall of Echoes and Irma copy Edea's printed abilities. Hall of Echoes ({5}: until end of turn) also turns the **legend rule
  (704.5j)** off for our permanents this turn. Activated in the first main phase, it gives a second beginning-of-combat theft and a
  second death trigger (one return, two draws). While it is a copy of Edea it is a creature, not a land. Hall rulings (2026-08-21)
  confirm the legend rule applies again in cleanup.
- **Lithoform Engine** ({2},{T}): it copies one triggered or activated ability we control, with new targets. Examples: Edea's combat
  trigger (a second theft), Edea's death trigger (an extra draw), Captivating Crew's steal, Karlach's or Celebrant's extra-combat
  trigger (one more combat), or a Kethek or Industrial Advancement end-step trigger. Rulings (2020-09-25): copies are not activated or
  triggered, so Roaming Throne does not apply to them.
- **Thassa, Deep-Dwelling**: blinking a stolen creature at end step returns it under our control, ending the until-end-of-turn
  control effect (the new object is ours). Conjurer's Closet does the same thing for {5} (owner rejection kept).

## Combos and bracket (disclosed)
- Commander Spellbook `find-my-combos` (2026-10-23): **0 complete combos** in baseline and candidate. Almost-included lines grow from
  126 to 175 with Aggravated Assault, all of them needing a card not in the 100. Some depend on an opponent's creature that Edea steals
  (for example Ancient Copper Dragon or The Reaver Cleaver with Aggravated Assault).
- **No infinite is claimed.** Repeated Aggravated Assault activations are finite: each needs {3}{R}{R}.
- Power Bracket **4**, unchanged: 3 Game Changers, fast mana, free interaction, tutors and mass theft (Insurrection, Mass Mutiny, Mob
  Rule).
