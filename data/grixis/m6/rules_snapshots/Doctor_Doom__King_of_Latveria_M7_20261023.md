# Doctor Doom, King of Latveria — M7 rules snapshot (2026-10-23, America/Chicago)

Sources: the Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only) and the candidate Oracle
snapshot `data/grixis/m6/oracle_snapshots/Doctor_Doom__King_of_Latveria_M7_Scryfall_20261023.json`. This snapshot is evidence only. It is not approval.

## Legality (recorded honestly)
- **Doctor Doom, King of Latveria** was first released in Marvel Super Heroes Commander (`msc`, 2026-06-26) and reads **commander: legal**
  on live Scryfall (2026-10-23). The later `pmei` 2026-12-18 printing is a promotional print, not a legality date. **No future-release or
  pending-legality project exception applies to this deck**, in line with the two-model reconciliation and the Pass C #13 final disposition.
  The paused Nov 13 legality-activation plan covers other (MBC) cards and is not used here. Every card in the baseline, the candidate and
  all staged alternatives reads commander-legal on live Scryfall and is within U/B/R.

## Commander text (current Oracle)
- {1}{U}{B}{R} 3/3 Legendary Creature — Human Noble **Villain**.
  - "Whenever you discard one or more land cards, each opponent loses 2 life."
  - "At the beginning of combat on your turn, target Villain you control gains menace until end of turn. It connives."
- The commander's identity: **separate land-discard events** (each = 2 life from every opponent) plus a free **Villain connive** every turn.

## Rules relied on
- **603.2c** + Oracle "one or more": one discard event containing several lands triggers Doom **once** (a wheel is one trigger, not seven).
  Separate events (each cycling activation, each Seismic Assault / Trade Routes / Psychic Frog activation, Lightning Axe's additional
  cost, Mox Diamond's replacement discard) each trigger it.
- **701.50a**: connive = draw, then discard; a +1/+1 counter only if a **nonland** card was discarded. A land discarded to connive is a
  land-discard event (Doom drains 2) but gives no counter (Pass C note kept).
- **608.2b / 115**: Doom's combat ability targets a Villain we control (Doom himself is legal). If the target is illegal on resolution,
  there is no menace and no connive.
- **702.11b vs 702.18a**: **Swiftfoot Boots** gives hexproof ("can't be the target of spells or abilities your **opponents** control"),
  so Doom can still target himself with his own connive. Lightning Greaves' shroud would stop Doom targeting himself; that is why Boots,
  not Greaves, is the candidate's protection card.
- **601.2h**: Lightning Axe's and Big Score's "discard a card" is an additional cost paid while casting; discarding a land that way is a
  land-discard event and Doom triggers even if the spell is later countered.
- **614.1a / Mox Diamond**: "If this artifact would enter, you may discard a land card instead." The replacement discards a land, so Doom
  (and Bone Miser, Surly Badgersaur, Green Goblin Nemesis, Cool but Rude level 2, Monument, Glint-Horn Buccaneer) trigger.
- **702.29a**: cycling = "[Cost], Discard this card: Draw a card." Cycling **Coastal Peak**, Canyon Slough, Fetid Pools, Xander's Lounge,
  or any land under **Tectonic Reformation** is a land-discard event. Coastal Peak is an Island Mountain (fetchable by Scalding Tarn,
  Polluted Delta and Bloodstained Mire) and **Crucible of Worlds** lets it be replayed from the graveyard and cycled again later.
- **702.52a / 702.52b / 121.6**: dredge 2 replaces a draw only while the library has at least 2 cards. The Dakmor Salvage loop
  (Tectonic Reformation's cycling {R} on Dakmor; Surly Badgersaur's Treasure from the land discard pays the next {R}; the cycling draw is
  replaced by dredge 2) is therefore **bounded by library size**: n iterations need 2n library cards. Commander Spellbook labels it
  "near-infinite"; this project calls it **finite** and claims no infinite.
- **603.3b**: the discard triggers (Doom, Badgersaur, Glint-Horn Buccaneer, Monument, Cool but Rude) are put on the stack above the cycling
  ability's draw and resolve first, so the Treasure exists before the dredge choice.
- **Monument to Endurance**: each of its three modes can be chosen at most once per turn; after three discards it stops adding anything.
- **Containment Construct / Moonstone / Currency Converter**: "you may exile that card"; exiling Dakmor Salvage breaks the loop (it must be
  in the graveyard for dredge), so those choices are declined during the loop (Containment Construct can instead exile a cycled
  non-Dakmor land to play it this turn).
- **Villainous Hideout**'s coloured mana only pays for Villain spells or abilities of Villain sources; it cannot pay Tectonic
  Reformation's granted cycling {R} (the cycling ability's source is the land card, not a Villain).
- **120.3a**: **Glint-Horn Buccaneer**'s "Whenever you discard a card" triggers once **per card** (a seven-card wheel is seven
  triggers, 1 damage each, to each opponent); damage to a player causes that much life loss. Its loot ("{1}{R}, Discard a card: Draw a
  card") can be activated only while it is attacking; it has haste. Doom's own trigger is once per event (603.2c).
- **Red Ghost, Intangible Genius**: "Whenever you draw your second card each turn" — the draw step plus Doom's connive reaches the second
  card on our turn; the 3/3 Ape token is a **Villain**, so it triggers Prowler, Baron Strucker (once per turn) and Doom Reigns Supreme.
- **Loki, the Deceiver (cut)**: its attack-created copies enter after the beginning of combat has passed, so they never get Doom's
  connive that turn (Pass C rules note kept).

## Combo disclosure
Commander Spellbook find-my-combos (2026-10-23): **1 included combo in both the baseline and the candidate** (Surly Badgersaur +
Tectonic Reformation + Dakmor Salvage, "infinite self-mill / near-infinite self-discard triggers"); in this deck it is bounded by
library size and graveyard access, as above. Almost-included: 16 (baseline) and 22 (candidate; the new near-misses pair Glint-Horn Buccaneer with Curiosity, Ophidian Eye, Tandem Lookout, Malcolm or Kefka, none of which is in the list, and Kefka is an owner-removed opponent-discard card that is not re-added). No infinite is claimed.
