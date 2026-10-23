# Lynde__Cheerful_Tormentor (Lynde, Cheerful Tormentor) — M7 rules snapshot (2026-10-23, America/Chicago)

Sources:
- Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only).
- Frozen Scryfall rulings file `rulings-20261015090033.jsonl.gz` (read-only). It has rulings for Lynde, Cheerful Tormentor (2), Court of Vantress (15), Cruel Reality (3), Curse of Thirst (1), Curse of Misfortunes (1), Torment of Scarabs (1), Copy Enchantment (8), Accursed Witch // Infectious Curse (3), Paradox Haze (5), Strionic Resonator (8), Beseech the Mirror (5) and Curse of Chaos (6). It has **no rulings** for Extravagant Replication, Curse of Death's Hold or Staff of Compleation, so those rest on Oracle text and the Comprehensive Rules only.
- Candidate Oracle snapshot `data/grixis/m6/oracle_snapshots/Lynde__Cheerful_Tormentor_M7_Scryfall_20261023.json` (live Scryfall `/cards/collection`, 2026-10-23). It has 0 oracle_id/text differences against the frozen 2026-10-16 oracle file for all 154 snapshot names, and 0 names missing. Live data was not written into the frozen cache.

This snapshot is evidence only. It is not owner approval.

## Deck ID, commander and legality
- Tracker deck #31 (index 30) `Lynde__Cheerful_Tormentor`; the commander is **Lynde, Cheerful Tormentor**. The tracker, registry, overrides (APPROVED/LOCKED 2026-10-14) and the canonical source file (canonical main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, `refinement/decklists/Lynde_Cheerful_Tormentor_Approved_2026-10-14.txt`, blob 5731e689, introduced by 7258398) agree on the raw SHA-256 05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166. Disclosed discrepancies, not changed: tracker row 30 detailed-gate sub-fields still read PENDING, and the decisions document header hashes (e72576fb…, aa021e79…) are the pre-change source values, not the approved list.
- **Lynde, Cheerful Tormentor** ({1}{U}{B}{R} Legendary Creature — Human Warlock 2/4) reads **commander: legal** on live Scryfall (2026-10-23) and is **not a Game Changer**. No preview caveat and no project exception applies.
- Every card in the baseline, the candidate and all staged alternatives reads commander-legal on live Scryfall and is within U/B/R. Evaluated and excluded: The Unluckiest Planeswalker and Jabs, Mistress of Mockery (both **not_legal** on live Scryfall, released 2026-10-19 in `mbc`; the owner also declined them on 2026-10-14). No unreleased or not-legal card is called legal.
- Game Changers (live): baseline and candidate both carry the same **8** (Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Imperial Seal, Jeska's Will, Rhystic Study, Vampiric Tutor). The deck is **Bracket 4** (owner Bracket 4 Optimized); none of the selected adds is a Game Changer.

## Commander text (current Oracle)
- "Deathtouch / Whenever a Curse is put into your graveyard from the battlefield, return it to the battlefield attached to you at the beginning of the next end step. / At the beginning of your upkeep, you may attach a Curse attached to you to one of your opponents. If you do, draw two cards."
- Rulings 2021-09-24: if a cursed player leaves the game, the Curse goes to your graveyard and Lynde triggers; the upkeep move does not target (hexproof players can receive it).
- CR 503.1a: Lynde's upkeep trigger and every Curse upkeep trigger go on the stack together and you order your own. A Curse trigger that has already triggered keeps the player it named when Lynde moves the Aura ("that player" is fixed; Curse of Thirst ruling 2011-01-22 counts Curses on resolution).
- CR 603.7c: the delayed return finds nothing if the Curse card left the graveyard (exiled) before the end step.
- CR 704.5d: a **token** Curse put into a graveyard ceases to exist, so Lynde cannot return token copies.

## Selected change 1: +Court of Vantress −Cruel Reality
- Court of Vantress ({2}{U}{U} enchantment): "When this enchantment enters, you become the monarch. At the beginning of your upkeep, choose up to one other target enchantment or artifact. If you're the monarch, you may create a token that's a copy of it. If you're not the monarch, you may have this enchantment become a copy of it, except it has this ability."
  - CR 303.4f: a token Aura created without being cast enters attached to a legal player **its controller chooses**. A Curse token can be attached to you, then moved by Lynde at the same or a later upkeep for two cards (order Court above Lynde, CR 503.1a), or attached straight to an opponent.
  - Ruling 2023-09-01: if Court (not monarch) becomes a copy of an Aura and is not attached, it goes to its owner's graveyard (CR 704.5m). That makes it a Curse put into your graveyard from the battlefield, so Lynde triggers and returns the card; in the graveyard the copy effect no longer applies, so it re-enters as Court of Vantress, a non-Aura, so it enters unattached (CR 303.4h) and its enters trigger makes you the monarch again. Classified moderate confidence and **not relied on** for the decision.
  - Monarch end-step draw is an extra card each turn while you keep it; combat damage to you passes it. Lynde (2/4 deathtouch) is a reasonable blocker.
- Cruel Reality ({5}{B}{B} Aura Curse): "At the beginning of enchanted player's upkeep, that player sacrifices a creature or planeswalker of their choice. If the player can't, they lose 5 life." Rulings 2017-04-18: the player can't choose to lose 5 life while they have a creature or planeswalker.
  - When Cruel Reality is destroyed or sacrificed, Lynde returns it **attached to you**. At your next upkeep its trigger and Lynde's trigger both go on the stack; moving the Aura does not cancel the already-triggered sacrifice for you. With Lynde as your only creature or planeswalker you must sacrifice Lynde (grid B1: 42 of 96 Cruel Reality cells).

## Selected change 2: +Extravagant Replication −Curse of Death's Hold
- Extravagant Replication ({4}{U}{U} enchantment): "At the beginning of your upkeep, create a token that's a copy of another target nonland permanent you control." A Curse you control (attached to you or to an opponent) is a legal target; the token Aura's attachment is chosen by you (CR 303.4f). It can instead copy a creature, artifact or another enchantment engine.
- Curse of Death's Hold ({3}{B}{B} Aura Curse): "Creatures enchanted player controls get -1/-1." When returned to you by Lynde it stays on you from the end step until your upkeep: Lynde is 1/3, and Nightscape Familiar (1/1) and every other X/1 dies (state-based action CR 704.5f; regeneration does not help against 0 toughness). Grid B1: an X/1 creature is killed in 32 of 96 Death's Hold cells.

## Staged and compare-only alternatives (not counted)
- Staff of Compleation ({3} artifact): "{T}, Pay 1 life: Destroy target permanent you own." A Curse you own attached to an opponent is a permanent you own, so this is a repeatable Lynde enabler (one activation per turn without the {5} untap). Staged against Nightscape Familiar; the cost reduction loss is measured.
- Strionic Resonator: copies a triggered ability on the stack (rulings 2018-03-16). Copying Lynde's upkeep trigger draws two more only if a second Curse is still attached to you. Owner rejected it on 2026-10-14; compare-only.
- Beseech the Mirror: bargain sacrifices one artifact, enchantment or token (rulings 2023-09-01); bargaining a Curse triggers Lynde. Owner rejected it on 2026-10-14; compare-only.
- Curse of Chaos: owner removed it on 2026-10-14 (replaced by Curse of Hospitality); compare-only, not re-added.

## Pass C requested mechanics (bounded tests)
- 1/2/3 self-Curse upkeep stacks with best ordering (Thirst, Bloodletting, Misfortunes, Torment of Scarabs, Cruel Reality, Death's Hold): grid B1 (246 cells). Without Cruel Reality, Lynde is never lost; maximum life lost in any cell is 2; a returned solo Thirst moved first deals 0.
- Curse of Misfortunes triggers on the Aura controller's upkeep (Stage B correction); with it above Lynde, it tutors a Curse onto you that Lynde then moves.
- Braids, Arisen Nightmare: sacrifice at the beginning of your end step returns at the **next** end step (CR 603.7), same one-turn latency before your upkeep.
- Accursed Witch // Infectious Curse: in the graveyard the card has only front-face characteristics (CR 712.8a); Lynde's return puts a creature onto the battlefield, which enters unattached (CR 303.4h). It returns as Accursed Witch, not as a Curse attached to you.
- Copy Enchantment / Mirrormade copying a Curse: Lynde triggers by look-back (CR 603.10a); on return the card may copy again as it enters (Copy Enchantment ruling 2023-09-01). Moderate confidence.
- Extra upkeeps: Paradox Haze ruling 2006-09-25 — "at the beginning of your upkeep" abilities trigger in each additional upkeep, so Court, Replication and Lynde each trigger again (grid B3).

## Combos
- Commander Spellbook find-my-combos (2026-10-23T17:44:24-0500): **0** included combos in the baseline, the candidate and every staged alternative. Almost-included: baseline 17, candidate 22. No combo is added or lost.
