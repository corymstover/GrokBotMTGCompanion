# Cecily, Haunted Mage + Bjorna, Nightfall Alchemist (companion Lutri) — M7 rules snapshot (2026-10-23, America/Chicago)

Sources: the Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only) and the candidate Oracle
snapshot `data/grixis/m6/oracle_snapshots/Cecily__Bjorna__Lutri_M7_Scryfall_20261023.json`. This snapshot is evidence only. It is not approval.

## Commander and companion text (current Oracle)
- **Cecily, Haunted Mage** {1}{U}{B}{R}, a 3/5 Legendary Creature — Human Wizard.
  - "Your maximum hand size is eleven."
  - "Whenever Cecily, Haunted Mage attacks, you draw a card and you lose 1 life. Then if you have eleven or more cards in your hand, you may cast an instant or sorcery spell from your hand without paying its mana cost."
  - Partner—Friends forever.
- **Bjorna, Nightfall Alchemist** {U}{R}, a 1/3 Legendary Creature — Human.
  - "{T}, Sacrifice an artifact: Bjorna deals 1 damage to target creature. Goad that creature."
  - Partner—Friends forever.
- **Lutri, the Spellchaser** {1}{U/R}{U/R} (companion, outside the 100).
  - Flash.
  - "When Lutri enters, if you cast it, copy target instant or sorcery spell you control."

## Rules relied on
- **402.2 / 514.1**: maximum hand size is checked only in the cleanup step. Holding 11+ cards during combat is legal at any maximum hand size.
- **613.11**: maximum hand size effects modify game rules and are applied in timestamp order. Twenty-Toed Toad ("twenty") versus Cecily ("eleven") versus Thought Vessel or Sea Gate Restoration ("no maximum") is therefore resolved by timestamps:
  - The newest effect wins.
  - Recasting Cecily gives her a new timestamp, which resets the maximum to eleven.
  - Sea Gate Restoration's "for the rest of the game" effect is newer than any permanent already on the battlefield when it resolves.
- **Cecily's "Then if"**: this clause is inside the effect. It is not an intervening-if trigger condition (603.4), so it is checked as the trigger resolves, after the draw. Ten cards before the attack become eleven after the draw, which turns the free cast on. With nine cards, it stays off unless a copy of the trigger resolves first.
- **707.10 / 707.10b**: Strionic Resonator ({2},{T}) and Echo, Perceptive Prodigy ({1},{T}; creature sources only) put a copy of a triggered ability on the stack. The copy has the same source.
  - A copied Cecily trigger draws, drains 1 life and offers its own free cast. Each copy checks the hand size separately when it resolves.
  - The copy of a spell made by Lutri is **not cast** (707.10), so it does not trigger "cast" abilities. Magecraft (Archmage Emeritus) also sees copies.
  - Lutri is a creature source, so Echo may legally target Lutri's ETB trigger while the target spell is still on the stack. No line in this review relies on that interaction; the Lutri-copy case is credited to Strionic Resonator only.
  - Resonator copies any triggered ability we control. That includes Lutri's ETB and Mana Drain's delayed mana trigger.
  - Echo and Resonator need {T}, so they must be untapped. Echo is a creature, so it must also be free of summoning sickness. Resonator is a noncreature artifact and can be activated the turn it is cast.
- **Harmonic Prodigy**: it doubles triggered abilities of Shamans and other Wizards we control. Cecily, Twenty-Toed Toad, Archmage Emeritus and Gogo are Wizards; Echo (Human Hero) is not.
- **Twenty-Toed Toad**: "Whenever this creature attacks, you win the game if … you have twenty or more cards in hand." This is checked on resolution, not as an intervening-if. Order the triggers (603.3b) so that Cecily's attack trigger resolves first (draw, then free-cast Peer into the Abyss or Sea Gate Restoration), and the Toad trigger resolves last.
- **104.3c / 121.4**: drawing from an empty library makes the drawer lose at the next state-based check. Peer into the Abyss targeting ourselves draws half our library, rounded up, so it cannot deck us by itself. Teferi's Ageless Insight doubles those draws, which can overdraw.
- **702.139a (companion)**: once per game, at sorcery speed with an empty stack, pay {3} to put Lutri into hand. Lutri is then cast normally for {1}{U/R}{U/R}, with flash.

## Combos (Commander Spellbook find-my-combos, 2026-10-23, research_challengers/*_CommanderSpellbook_20261023.json)
- Baseline included combos (all kept in the candidate):
  - **1368-1878-2706**: Underworld Breach + Wheel of Fortune + Jeska's Will. Spellbook lists this as infinite draw/loot for all players. Hand-verified:
    - Escape requires exiling **three** other graveyard cards per cast, so the loop's length is bounded by the graveyard.
    - Every wheel also refills the opponents, and we draw too, which risks decking ourselves.
    - It needs a payoff to win: Psychosis Crawler damage, Storm-Kiln Treasure, or Toad holding 20 cards.
    - We do not claim this as a deterministic infinite.
  - **1561-2384**: Psychosis Crawler + Peer into the Abyss on ourselves. The burst is about half our library in damage to each opponent. It is finite.
  - **1561-5042**: Peer into the Abyss + Teferi's Ageless Insight. This doubles the draws to about our whole library, so it is a **self-decking risk** unless we win the same turn.
- Candidate-only included combo:
  - **1561-5850**: Twenty-Toed Toad + Peer into the Abyss. Spellbook lists it as "Win the game".
  - It needs Toad to attack (no summoning sickness) with Peer cast first, for example via Cecily's free cast during the attack.
  - This is a deterministic alternate win only if Peer resolves while the Toad trigger is still on the stack.
- No unsupported infinite claim. Yawgmoth's Bargain and Trade Secrets are project-exception card draw. They are not combos.
- **Bracket 4**. The deck has ten Game Changers: Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Mystical Tutor, Notion Thief, Rhystic Study, The One Ring, Underworld Breach and Vampiric Tutor. These are unchanged, and none of the six adds is a Game Changer.

## Legality truth (never "officially legal")
- Live Scryfall reports Trade Secrets and Yawgmoth's Bargain as **banned** in Commander.
- Lutri, the Spellchaser reads `legal` on Scryfall only because the Commander **companion** ban is not encoded there. Lutri is banned as a Commander companion.
- All three are owner project exceptions for **this deck only**. They are never described as officially legal and never applied to any other deck.
