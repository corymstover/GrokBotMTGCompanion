# Ashad, the Lone Cyberman — M7 rules snapshot (2026-10-23, America/Chicago)

Source: Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`) and the candidate Oracle
snapshot `data/grixis/m6/oracle_snapshots/Ashad__the_Lone_Cyberman_M7_Scryfall_20261023.json`. Evidence only; not approval.

## Rules relied on
- **702.153a Casualty N**: an additional cost, "you may sacrifice a creature with power N or greater". When the spell is cast
  with the cost paid, it is copied. Ashad grants casualty 2 to the *first nonlegendary artifact spell* cast each turn,
  on any turn, so it works on opponents' turns with flash artifacts (Necron Deathmark) or Shimmer Myr. Power is checked
  when the cost is paid (601.2h). Tapped creatures can be sacrificed.
- **608.3f**: a copy of a permanent spell becomes a token as it resolves, but it is **not "created"**. Replacement effects
  that modify "create" (e.g. Worldwalker Helm) do not apply to Ashad's copy. The copy is not cast, so it never uses the
  first-artifact-spell slot.
- **707.10c**: the copy may choose new targets. A copied Necron Deathmark ETB is a separate trigger from the token
  permanent, so two creatures can be destroyed.
- Sequencing: the first nonlegendary artifact spell uses the slot whether or not casualty is paid. Cheap artifacts cast
  before a fodder body is available waste it.
- **702.84a Unearth** (Royal Warden): sorcery speed, haste, exiled at the next end step or if it would leave. An unearthed
  Warden sacrificed for casualty is exiled instead of dying (no Pitiless Plunderer Treasure). It was still sacrificed,
  so Ashad gets a counter, and its ETB still made two tapped 2/2 tokens.
- **Razorlash Transmogrant**: the graveyard ability is activated with no timing restriction (instant speed) and costs {B}{B}
  while an opponent controls four or more nonbasic lands. It returns with a +1/+1 counter as a new object.
- **Skullclamp**: +1/-1. A 1-toughness creature dies to state-based actions when equipped (draw two). A toughness-2+,
  1-power creature becomes power 2 and can pay casualty. Sacrificing it draws two.

## Combos (Commander Spellbook find-my-combos, 2026-10-23, research_challengers/*_CommanderSpellbook_20261023.json)
- Baseline and candidate: 66-457-5491 Urza, Lord High Artificer + Worldwalker Helm + Artificer Class (unchanged).
- **Candidate only: 4050-4871-6429 Razorlash Transmogrant + Pitiless Plunderer + Phyrexian Altar** (infinite creature
  death/ETB/sacrifice triggers). Condition: an opponent controls four or more nonbasic lands. Loop: sacrifice Razorlash to
  Altar for {B}, Plunderer makes a Treasure, sacrifice it for {B}, pay {B}{B} to return Razorlash. Net mana zero. Payoffs
  already in the deck: Mayhem Devil (2 damage per loop), Disciple of the Vault (2 life loss per loop) and Ashad
  (+1 counter per loop). It is a three-card conditional line, not a two-card infinite. No other new complete combo was
  reported. Infinite claims are limited to this Spellbook-listed line.
