# Cult of Skaro — M7 rules snapshot (2026-10-23, America/Chicago)

Sources: the Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only) and the candidate Oracle
snapshot `data/grixis/m6/oracle_snapshots/Cult_of_Skaro_M7_Scryfall_20261023.json`. This snapshot is evidence only. It is not approval.

## Commander text (current Oracle)
- **Cult of Skaro** {1}{U}{B}{R}, a 4/4 Legendary Artifact Creature — Dalek. No haste.
  - "Whenever Cult of Skaro attacks, choose one at random — Thay (+1/+1 counter on each artifact creature you control);
    Caan (draw two cards); Sec (create a 3/3 black Dalek artifact creature token with menace); Jast (each opponent loses 4 life)."
  - Each mode has probability 1/4. Expected value of one trigger: 1/2 card, 1/4 Dalek token, 1 life per opponent, plus 1/4 of a
    team-wide counter.

## Rules relied on
- **603.3c / 707.10**: the random mode is chosen as the trigger goes on the stack. **Strionic Resonator** and **Scientist Supreme
  of A.I.M.** copy the trigger *with* that mode (707.10 copies modes). **Roaming Throne** naming Dalek makes the trigger trigger an
  additional time; that is a separate trigger with its own random mode (Pass C correction kept).
- **508.3a / 508.4**: "Whenever ... attacks" triggers only when a creature is *declared* as an attacker. Tokens put onto the battlefield
  tapped and attacking (myriad from **Dalek Squadron**, **Auton Soldier**, the cut **Cybermen Squadron**; **Shaun, Father of Synths**'
  Synth token) never "attacked", so they do not trigger Cult that combat.
- **"Whenever you attack"** (Karlach, Shaun) triggers once when we declare one or more attackers.
  - **Karlach, Fury of Avernus**: "if it's the first combat phase of the turn, untap all attacking creatures. They gain first strike ...
    After this phase, there is an additional combat phase." In the extra combat (500.8), Cult and every untapped legal Cult copy can be
    declared again, so **each gets a second attack trigger**. Karlach's own trigger needs no attack by Karlach, so it works the turn it
    is cast if anything attacks.
  - **Shaun + Karlach ordering (603.3b)**: both are ours and trigger together. Put Karlach's trigger on the stack first and Shaun's on
    top. Shaun resolves first: the Synth copy of Cult enters tapped and attacking. Karlach then untaps all attacking creatures, including
    the Synth, which can be declared as an attacker in the extra combat and triggers Cult there.
  - The Synth token is not exiled at end of combat; it stays until Shaun leaves the battlefield ("exile all Synth tokens"). On later turns
    it is a normal non-legendary Cult copy that attacks and triggers.
- **707.9b / 704.5j**: Shaun's, **Quantum Misalignment**'s, **Spark Double**'s, **Irenicus's Vile Duplication**'s, **Auton Soldier**'s and
  **Helm of the Host**'s copies are not legendary, so the legend rule does not apply. **Phyrexian Metamorph**'s copy of Cult stays
  legendary (legend rule applies unless **Sakashima** is on the battlefield).
- **302.6 / 702.10b**: Cult and fresh copies need haste to attack the turn they arrive. Baseline haste: Lightning Greaves, Swiftfoot Boots,
  Helm token, The Dalek Emperor (other Daleks), Arena of Glory (exerted, creature spells). **Hammer of Purphoros** gives every creature haste,
  including Cult cast from the command zone and every clone the turn it enters.
- **702.88a (Rebound)**: Quantum Misalignment cast from hand is exiled and recast free next upkeep, so it makes two non-legendary Cult copies
  over two turns (the second one in upkeep, able to attack that turn only with haste or if Hammer is out — tokens created in upkeep are
  still summoning sick without haste).
- **Kindred Discovery** naming Dalek: "Whenever a creature you control of the chosen type enters or attacks, draw a card." Mandatory;
  **121.2** draws are individual and **704.5b** a player who drew from an empty library loses. Large Dalek token turns (Genesis of the Daleks
  chapter III = 3 tokens) draw several cards. Overdraw/deck-out risk is disclosed, not modeled.
- **Research Thief / Thopter Spy Network** draw on combat **damage** (post-blocks); **Kindred Discovery** draws on **entry / declared attack**
  (pre-blocks). **Canoptek Spyder** (cut) draws only when another **nontoken** artifact creature or Vehicle enters.
- **702.116a (Myriad)**: in a four-player game, a myriad attacker creates up to two tapped-and-attacking copies that are exiled at end of combat.
  **The Master, Multiplied** (cut) stops our triggered abilities from exiling those tokens.
- **Skorpekh Lord**: other artifact creatures get +1/+0 and menace; Cult, Dalek tokens (already menace), Cybermen, Necrons and Thopters gain evasion.
- **Combo disclosure**: Commander Spellbook lists **Sword of Feast and Famine + Aggravated Assault** (900-3750, "Infinite combat phases"),
  unchanged from the baseline. It needs the equipped creature to connect every combat and at least five usable lands with two red after
  each untap. It is disclosed as conditional and is not claimed as an unconditional or deterministic infinite. No new combo is added.
