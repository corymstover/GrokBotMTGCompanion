# Evelyn, the Covetous — M7 rules snapshot (2026-10-23, America/Chicago)

Sources:
- Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only).
- Frozen Scryfall rulings file `rulings-20261015090033.jsonl.gz` (read-only). It holds no Evelyn rulings. Rulings are quoted for Burnt Offering, Worldgorger Dragon and Saw in Half.
- Candidate Oracle snapshot `data/grixis/m6/oracle_snapshots/Evelyn__the_Covetous_M7_Scryfall_20261023.json` (live Scryfall `/cards/collection`, 2026-10-23). It has 0 oracle_id/text differences against the frozen 2026-10-16 oracle file for all 191 snapshot names.

This snapshot is evidence only. It is not owner approval.

## Legality (recorded honestly)
- **Evelyn, the Covetous** (Streets of New Capenna, set `snc`, released 2022-04-29) reads **commander: legal** on live Scryfall (2026-10-23).
  - Colour identity U/B/R; **not a Game Changer**.
  - **No future-release or pending-legality project exception applies to this deck.**
- Every card in the baseline, the candidate and all staged alternatives reads commander-legal on live Scryfall and is within U/B/R.
  - Evaluated discovery names outside U/B/R were excluded from the snapshot and are listed there: Archivist of Oghma, Drannith Magistrate, Esper Sentinel, Silence, Silent Clearing, Tymna.
- Game Changers (live): the baseline and the candidate both carry the same **19**:
  - Ad Nauseam, Ancient Tomb, Chrome Mox, Demonic Tutor, Force of Will, Gamble, Imperial Seal, Lion's Eye Diamond, Mana Vault, Mox Diamond, Mystical Tutor, Necropotence, Notion Thief, Opposition Agent, Orcish Bowmasters, Rhystic Study, Thassa's Oracle, Underworld Breach, Vampiric Tutor.
  - No primary add is a Game Changer. Grim Monolith, in a staged alternative only, is one.
  - **Power Bracket 5 (cEDH)**, unchanged.

## Commander text (current Oracle)
- {2}{U/B}{B}{B/R} Legendary Creature — Vampire Rogue, Flash.
  - "Whenever Evelyn or another **Vampire** you control enters, exile the top card of each player's library with a collection counter on it."
  - "Once each turn, you may play a card from exile with a collection counter on it if it was exiled by an ability you controlled, and you may spend mana as though it were mana of any color to cast it."
- The trigger is **Vampire-only**. Rogues and Rats do not trigger it.
  - In the baseline, Evelyn herself is the **only Vampire**. In the candidate, **Insolent Neonate** ({R} Vampire) is a second trigger source.
- Identity:
  - Flash in a cEDH Grixis combo shell.
  - Each Vampire entering exiles four cards (one per player in a 4-player pod), and Evelyn plays one per turn with any-colour mana.
  - Her re-entries during a Worldgorger loop each exile four more.

## Rules relied on
- **603.6a**: the trigger fires for each Vampire entering, so a Saw in Half on Evelyn makes two token copies, each a Vampire entering.
  - Each token triggers itself and the other, so up to 4 triggers. Saw in Half ruling (2025-09-19): enters abilities of the copied creature trigger for the tokens.
- **704.5j (legend rule)**: the two Evelyn tokens are legendary with the same name, so after their triggers are put on the stack, one token is put into the graveyard (where it ceases to exist, 704.5d). The triggers still resolve.
- **406.6 / 607.2a** and Evelyn's own text: only cards exiled by an ability we controlled with a collection counter are playable, once each turn.
- **903.9a**: when Worldgorger Dragon exiles Evelyn, we may **decline** to move her to the command zone, so she returns with the other exiled permanents and her enter trigger fires again.
- **104.4b / 732.4**: Worldgorger plus Animate Dead/Dance of the Dead/Necromancy is a mandatory loop.
  - It needs an optional exit: another creature card in a graveyard for the returning Aura to enchant, or an instant-speed win/out during the loop. Otherwise the game is a draw.
  - **Insolent Neonate** discarding a second creature card adds such an exit.
  - Worldgorger ruling (2022-12-08): the Aura's controller chooses what it enchants when it returns, without targeting.
- **Evelyn in the loop**: each iteration exiles the top card of **each** library, ours included, with a collection counter. Our library shrinks by one per loop.
  - The loop therefore mills itself finitely. It is not used as an unbounded engine; the deck wins with Thassa's Oracle/Consultation/Pact or Breach/Brain Freeze lines.
- **Burnt Offering** ruling (2013-04-15): exactly one creature is sacrificed as a cost, and no one can respond to the sacrifice.
  - Sacrificing Evelyn (MV 5) gives 5 mana; Worldgorger (MV 6) gives 6; Thassa's Oracle (MV 2) after its trigger gives 2. The mana is B and/or R.
- **701.21a / Insolent Neonate**: "Discard a card, Sacrifice this creature: Draw a card" is an instant-speed outlet. It puts Worldgorger or a second loop-exit creature into the graveyard and refills by one card.
- **702.8a (flash)**: Evelyn and the deck's instants are cast in response, so Brainstorm's stack-time selection is live at instant speed.
- **Fetchlands**: Marsh Flats and Verdant Catacombs find the Swamp-typed duals/shocks (Underground Sea, Badlands, Watery Grave, Blood Crypt) or the basic Swamp.
  - Each fetch shuffles, which turns Brainstorm's two replaced cards back into fresh draws.

## Combo and infinite boundaries (no unsupported claims)
- Commander Spellbook find-my-combos (2026-10-23): baseline and candidate have the **same 7** complete combos (ids 742-1295, 1295-3093, 1368-1414-4856, 1368-3518-4856, 4812-4846, 2896-4846, 3605-4846). No combo is lost and none is added.
  - They cover Thassa's Oracle + Demonic Consultation / Tainted Pact; Underworld Breach + Lion's Eye Diamond / Lotus Petal + Brain Freeze; and Worldgorger Dragon + Animate Dead / Dance of the Dead / Necromancy.
- **Worldgorger lines** yield arbitrarily large **mana from lands tapped in response** and repeated Evelyn enter triggers.
  - They are **not** a win alone and need a mana sink or an exit. Each Evelyn iteration also exiles our own top card, so the repeats are finite.
- **Saw in Half on Evelyn** is finite: 2 tokens, up to 4 triggers, 16 cards exiled across a 4-player table.
- No new combo or infinite is claimed for any add.
