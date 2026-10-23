# Davros, Dalek Creator — M7 rules snapshot (2026-10-23, America/Chicago)

Sources: the Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only) and the candidate Oracle
snapshot `data/grixis/m6/oracle_snapshots/Davros__Dalek_Creator_M7_Scryfall_20261023.json`. This snapshot is evidence only. It is not approval.

## Commander text (current Oracle)
- **Davros, Dalek Creator** {1}{U}{B}{R}, a 3/4 Legendary Artifact Creature — Alien Scientist with menace. **Davros is not a Dalek**
  (Pass C rules note kept), so Dalek-type effects (Roaming Throne naming Dalek, The Dalek Emperor's haste) do not apply to him;
  Roaming Throne must name Alien or Scientist to copy his trigger.
  - "At the beginning of your end step, create a 3/3 black Dalek artifact creature token with menace if an opponent lost 3 or more life
    this turn. Then each opponent who lost 3 or more life this turn faces a villainous choice — You draw a card, or that player discards a card."
- The commander's identity is therefore: **make every opponent lose 3+ life on our turn**, then cash it in (one Dalek per resolution,
  one villainous choice per qualified opponent per resolution).

## Rules relied on
- **603.4**: the condition is *not* written as an intervening "if" clause ("At ..., if ..., ..."). It is a condition in the effect, so it
  is checked on resolution. Other "at the beginning of your end step" triggers we control can be ordered to resolve first (**603.3b**):
  **Wound Reflection** (each opponent loses life equal to the life they lost this turn), **Perforating Artist** (raid: each opponent
  loses 3 unless they sacrifice/discard), **Missy**. Those losses count for Davros.
- **603.3 / 603.2**: the Dalek token's entering triggers (Purphoros 2 to each opponent; Ingenious Artillerist 1 per artifact) trigger
  during Davros's resolution but go on the stack only after it has finished, i.e. after that resolution's villainous choices. They can
  qualify opponents only for a *later* Davros resolution (Roaming Throne naming Alien/Scientist, Strionic Resonator, Scientist Supreme
  of A.I.M., a second Davros from Auton Soldier). The first token never creates the original qualification.
- **701.55a / 701.55d**: each qualified opponent chooses an option, one at a time in APNAP order. **701.55b**: they may choose an
  impossible option — an empty-handed opponent can "discard a card" and lose nothing. This is the main weakness of the villainous choice
  and is disclosed (Tinybones, Sygg, Court of Ambition and Torment of Hailfire keep pressure on such opponents; Tergrid only gains
  from permanent cards actually discarded or nontoken permanents sacrificed).
- **701.55c**: **The Valeyard** makes each villainous choice be faced an additional time; it doubles the choices, not the Dalek token.
- **614 / 616.1**: **Bloodletter of Aclazotz** "If an opponent would lose life during your turn, they lose twice that much life
  instead." Damage to a player causes life loss (**120.3**), so it doubles combat damage, Boltwave, Fiery Confluence, Purphoros, Tectonic
  Giant, Torment of Hailfire, Wound Reflection's loss etc. on our turn only. The effective threshold becomes 2 points on our turn.
  Bloodletter + Wound Reflection is a finite doubling, not a loop.
- **608.2b**: a spell whose targets are all illegal on resolution does not resolve. **Unlicensed Disintegration** with an illegal target
  does nothing (no destroy, no 3 damage). **Fiery Confluence**'s "destroy target artifact" mode is its only targeted mode; if every chosen
  artifact target is illegal, the whole spell does not resolve and its "2 damage to each opponent" modes are lost too (Pass C failure case).
  With only untargeted modes chosen (2-2-2) it cannot be fizzled by target loss.
- **Unlicensed Disintegration**: "Destroy target creature. If you control an artifact, Unlicensed Disintegration deals 3 damage to that
  creature's controller." It qualifies at most one opponent, and only for our end step if cast on our turn.
- **Purphoros, God of the Forge**: indestructible; "Whenever another creature you control enters, Purphoros deals 2 damage to each
  opponent." Each Dalek token, each myriad token (**702.116a**: one per opponent other than the defending player; Dalek Squadron,
  Cybermen Squadron's granted myriad, Auton Soldier), Genesis of the Daleks chapter tokens and each creature spell triggers it separately.
  Not a creature below devotion 5, so creature wipes and artifact wipes miss it.
- **Tectonic Giant**: "Whenever this creature attacks or becomes the target of a spell an opponent controls, choose one — This creature
  deals 3 damage to each opponent; or exile the top two cards ...". The attack trigger resolves in the declare-attackers step, before
  blocks, so it qualifies the whole table even if Tectonic Giant is blocked.
- **Tergrid, God of Fright** (Game Changer): "Whenever an opponent sacrifices a nontoken permanent or discards a permanent card, you may
  put that card from a graveyard onto the battlefield under your control." Hits Court of Ambition, Torment of Hailfire, Perforating
  Artist, Davros's discard option, Sycorax Commander, Labyrinth Raptor, The Dalek Emperor's and Doomsday Confluence's edicts.
  **Anti-synergy disclosed:** Dauthi Voidwalker exiles cards that would go to opponents' graveyards, so Tergrid gets nothing while
  Voidwalker is out (choose which to deploy).
- **702.111 (menace)**: Davros, every Dalek token and Tergrid have menace; Swan Song (cut) gives the opponent a 2/2 flying blocker.
- **704.5j / 707.9b**: Auton Soldier's copy of Davros is not legendary, so it gives a second Davros end-step trigger.

## Combo disclosure
Commander Spellbook find-my-combos (2026-10-23): **0 included combos** for both the baseline and the candidate. Almost-included rises
from 39 to 51; new near-misses involve Bloodletter with cards not in the list (Peer into the Abyss, Unstoppable Slasher, Blood Tribute,
Tree of Perdition). No infinite is claimed.
