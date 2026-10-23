# Be'lakor, the Dark Master — M7 rules snapshot (2026-10-23, America/Chicago)

Sources: Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only) and the candidate Oracle
snapshot `data/grixis/m6/oracle_snapshots/Be_lakor__the_Dark_Master_M7_Scryfall_20261023.json`. This is evidence only, not approval.

## Commander text (current Oracle)
Be'lakor, the Dark Master {3}{U}{B}{R}, a 6/5 flying Legendary Creature — Demon Noble.
- "Prince of Chaos — When Be'lakor enters, you draw X cards and you lose X life, where X is the number of Demons you control."
- "Lord of Torment — Whenever another Demon you control enters, it deals damage equal to its power to any target."

## Rules relied on
- **603.6a**: every permanent on the battlefield, including newcomers, checks an enters event. Demons that enter at the same time see each other.
  Be'lakor entering alongside Demons triggers Lord for each of them, but never for itself ("another").
- **608.2h**: Prince's X is counted when the trigger resolves, not when it triggers. Lord's "its power" uses the entering Demon's
  current power. If that Demon has left the battlefield, last-known information applies (**113.7a**: the trigger exists independently of its source).
- **704.5j (legend rule)**: Rite of Replication or Molten Echoes copies of a legendary Demon (Be'lakor, Belzenlok, Kardur, Gyruda,
  Valgavoth, Rakdos the Showstopper, Vilis) go to the graveyard as a state-based action after they enter. Their ETB and Lord triggers
  are still put on the stack. Spark Double's copy is not legendary.
- **614.1a**: Bloodletter of Aclazotz doubles opponents' life loss during our turn as a replacement effect. It does not double our own
  Prince life loss.
- **702.143a**: Dream Devourer grants foretell (pay {2} during our turn, then cast on a later turn at the reduced cost). This is the value lost by the cut.
- Morbid (ability word): Reaper from the Abyss checks at the start of every end step whether any creature died this turn. Its target must be a non-Demon creature.
- Kindred Dominance destroys every creature that isn't of the chosen type. With Demon named, Roaming Throne (chosen type Demon), Spark Double
  copying a Demon survive. Ancient Cellarspawn (Horror) and opponents' non-Demons die.
- Herald's Horn and Urza's Incubator each choose a creature type as they enter. Cost reductions apply only to generic mana (Horn {1}, Incubator {2},
  Herald of Slaanesh {2}, Heartless Summoning {2}, Cellarspawn {1}).

## Combos (Commander Spellbook find-my-combos, 2026-10-23, research_challengers/*_CommanderSpellbook_20261023.json)
- The baseline and the candidate each report exactly one included combo: **Be'lakor + Rite of Replication**, listed by Spellbook as "near-infinite"
  damage/draw. Hand-verified as **finite**. With Be'lakor on the battlefield, a kicked Rite targeting him makes five legendary token copies at once.
  The original sees five other Demons enter and each token sees four, so 5 + 5×4 = **25 Lord triggers**, each dealing 6 damage (up to 150).
  The legend rule leaves one Be'lakor. The five token Prince triggers each draw X and lose X life, with X counted live at resolution. With about 5 Demons left, that is roughly 25 cards and 25 life, a real self-kill risk. The controller should stack all Prince triggers under the Lord triggers (603.3b ordering) so the damage resolves first. Roaming Throne naming Demon doubles each Lord trigger, so the burst is at most 50 triggers; that is still finite. No new combos are introduced by the five adds.
  The deck has **no infinite combo**. Liliana's Contract is an alternate win at upkeep with four or more differently named Demons.
- Abyssal Persecutor was rejected because "You can't win the game" would block Liliana's Contract.
- Bracket 4: five Game Changers (Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Vampiric Tutor), unchanged. None of the adds is a Game Changer.
