# Cormela, Glamour Thief — M7 rules snapshot (2026-10-23, America/Chicago)

Sources: the Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only) and the candidate Oracle
snapshot `data/grixis/m6/oracle_snapshots/Cormela__Glamour_Thief_M7_Scryfall_20261023.json`. This snapshot is evidence only. It is not approval.

## Commander text (current Oracle)
- **Cormela, Glamour Thief** {1}{U}{B}{R}, a 2/4 Legendary Creature — Vampire Rogue.
  - Haste.
  - "{1}, {T}: Add {U}{B}{R}. Spend this mana only to cast instant and/or sorcery spells."
  - "When Cormela dies, return up to one target instant or sorcery card from your graveyard to your hand."

## Rules relied on
- **605.1a**: Cormela's ability has no target and adds mana, so it is a mana ability. It can be activated while paying for a spell. Haste means it can be used the turn she (or a hasty token copy of her) enters.
- **106.6**: the restriction stays with the mana. Cormela's {U}{B}{R} can pay only for instants and sorceries. It cannot pay for artifacts, creatures, activations or her own {1} activation cost.
  - That makes the deck's **converters** important. These are instants or sorceries that, cast with restricted mana, produce unrestricted mana: Dark Ritual, Cabal Ritual, Culling the Weak, Seething Song, Jeska's Will and Rite of Flame.
  - The candidate adds **Frantic Search**, which untaps up to three lands. Cast with Cormela's three restricted mana, it turns them into up to three unrestricted land mana, and it loots two.
- **700.4 / 704.5j / 903.9a**: the legend rule puts the extra copies into the graveyard, so each one "dies".
  - A token copy of Cormela that dies triggers its own copy of her death ability.
  - The commander Cormela also triggers when she dies, even if her owner then moves her to the command zone. That move is a state-based action taken after she dies.
- **Twinflame** ({1}{R} sorcery, strive):
  1. Cast it on Cormela. It makes a token copy with haste.
  2. Keep the untapped token. The original goes to the graveyard and dies (legend rule), and its trigger returns Twinflame to hand.
  3. The token taps for {U}{B}{R}, which recasts Twinflame on the token.
  - Each loop nets 0 mana and adds 1 storm and 1 death trigger. It only becomes infinite with an outside +1, for example **Birgi** adding {R} per spell (Commander Spellbook 392-1235-4867).
  - **Dualcaster Mage + Twinflame** is a separate 2-card infinite of hasty tokens (Spellbook 147-1235).
  - Twinflame mirrors the incumbent Molten Duplication lines (Spellbook 147-5487, 392-4867-5487).
  - Twinflame + Cormela + an altar is **not** claimed as infinite. If you sacrifice the original in response, the death trigger cannot return Twinflame, because Twinflame is still on the stack. The copy then has no legal target.
- **Saw in Half on Cormela**: she dies (trigger 1) and two half-size token copies are created. The legend rule then sends one token to the graveyard (trigger 2). That is two death triggers per Saw in Half.
  - Spellbook lists Cormela + Saw in Half + Dark Ritual, Cabal Ritual or Seething Song as infinite (500-2701-4867, 500-4867-4923, 500-4036-4867). The second trigger returns the ritual.
  - **Frantic Search is not a converter there.** It nets 0 mana per loop where Dark Ritual nets +2, so the loop would net −1. No infinite is claimed for it.
- **Hexing Squelcher**: "Spells you control can't be countered." Per **101.2**, "can't" wins.
  - Opposing counterspells can still be cast at our spells, but they do not counter them.
  - Squelcher does **not** stop abilities from being countered: Stifle-type effects can still hit storm triggers, Cormela's death trigger or Breach escape. It also does not stop "can't cast" effects (Drannith Magistrate, Silence-type effects).
  - Ward—Pay 2 life (**702.21a**) taxes targeted removal on Squelcher and our other creatures, including Cormela.
- **Mistrise Village**: it enters untapped if we control a Mountain. The list has five Mountain-typed lands (Badlands, Blood Crypt, Steam Vents, Volcanic Island, basic Mountain), and all seven fetchlands can find one.
  - "{U}, {T}: The next spell you cast this turn can't be countered" protects one key spell (Ad Nauseam, Underworld Breach, Tendrils, or Thassa's Oracle via Consultation).
- **702.40a**: storm counts every spell cast before it this turn, including free spells and Twinflame recasts. Tendrils of Agony is a sorcery, so Cormela's restricted mana can cast it.

## Combos (Commander Spellbook find-my-combos, 2026-10-23, research_challengers/*_CommanderSpellbook_20261023.json)
- Baseline: 23 included combos. Candidate: 25 included combos. All 23 baseline combos remain, because every piece is kept.
  - Faithless Looting, Gitaxian Probe, Red Elemental Blast, Undercity Sewers and Exotic Orchard were in no included combo.
  - New in the candidate: **147-1235** (Dualcaster Mage + Twinflame) and **392-1235-4867** (Cormela + Birgi + Twinflame).
- Deterministic wins kept: Thassa's Oracle + Demonic Consultation/Tainted Pact (100 unique names, so Tainted Pact still exiles the whole library), Underworld Breach + LED/Lotus Petal + Brain Freeze, and the Cormela loops into Tendrils or Brain Freeze. Breach loops are graveyard-bounded (escape exiles three other cards).
- Power Bracket 5 (cEDH). The 20 Game Changers are unchanged, and none of the adds is a Game Changer.
