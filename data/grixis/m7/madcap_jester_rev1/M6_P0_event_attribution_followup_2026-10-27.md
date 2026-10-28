# Deck 56 M6 P0 follow-up — modified-event attribution, not new deck selection

**Exact already owner-approved M7 Rev1 100-card raw SHA-256:**
`643eb1cc4827c1dd95485e9922506b514746e6bbc5b4b8a4cfff0f44b1007e43`.
The list's seven swaps, owner approval and original 24-test conservative
review are preserved. This follow-up neither reopens nor changes a card.

## Source and rule boundary

- [Wizards current Comprehensive Rules](https://magic.wizards.com/en/rules),
  especially **614.6**: a replaced event does not happen; the modified
  event happens instead and may trigger other abilities; and **109.5**,
  **113.7–113.8** concerning control and sources.
- [Wizards MBC release notes — The Madcap Jester](https://magic.wizards.com/en/news/feature/mystery-booster-commander-edition-release-notes):
  play permissions grant neither free casting nor a timing exception.
- Exact gzip SHA-256 of public Scryfall Oracle Cards downloaded
  2026-10-27T21:02 UTC:
  `2f8afacba1b8f5375723cdeec3bc00adb3c6b97d038acc6406fa774129d7cf0a`.
  The new tests resolve Oracle text for **Jester, Dauthi Voidwalker, Uba
  Mask, Brain Freeze, Wheel of Fortune, Opposition Agent and Sire of
  Stagnation** locally, without a decklist API upload.

`m6_p0_followup.py` is an explicit small event-state model: source
controller/kind, opponent library, original destination, replacement,
changed destination and surviving Jester. It is **not** a complete Magic
game engine and does not purport to be an independent judge, a new sealed
M6 J result, or an empirical multiplayer study.

## Actual finite case results

| Original M6 P0 | Positive, payable/source-bound branch | Adversarial branch and limitation |
|---|---|---|
| `C1` Jester | Three actual opponent library top-card objects; attack ability under our control exiles one each with Jester live | Jester absent when exile occurs means no newly granted permission; no damage trigger assumed |
| `K1` any mana type | Stolen hypothetical `{2}{G}` spell costs **three** mana and can use two R plus one C through Jester | Only two mana is insufficient; sorcery timing and land quota remain normal |
| `K2` Dauthi replacement | Our **Brain Freeze** supplies the causing spell. Dauthi changes opponent mill-to-graveyard into library-to-exile with void counters; CR 614.6 modified event is tracked to original controlled spell | Opponent-controlled milling spell is not made ours merely because our Dauthi changes the destination; no Dauthi-only permission claimed |
| `K3` Uba Mask | With a hypothetical Wheel of Fortune **we** control, the replaced opponent draw exiles opponent cards; original causing spell is still ours | An ordinary turn-based draw is a game action, not our spell/ability, so Uba Mask by itself does not confer Jester access. Symmetric replacement of our own draws remains a strategic downside; Uba Mask stays excluded |
| `F1` slow payoffs | Opposition Agent costs three versus Sire of Stagnation six; available 3-mana opponent-search window compared with 6-mana unavailability | Opponent search exiled under Agent's control takeover is **not** automatically credited to our own causing spell/ability for Jester permission |

The old 24-case source intentionally refrained from claiming Dauthi/Brain
Freeze causation. Its unchanged historical receipt remains visible. This
new separately versioned fixture makes the cause-attribution assumption
explicit and tests both source-controlled and opponent-controlled branches,
rather than retrospectively relabeling the old caution as a pass.

**Scope of PASS:** five executable finite case models with exact candidate
SHA and pinned Oracle source. **Not included:** complete game simulation,
exhaustive replacement dependency interactions, independent card-specific
Wizards judge ruling, original I/J Phase B completion, other decks'
missing P0/P1 evidence, or total M7 milestone certification.
