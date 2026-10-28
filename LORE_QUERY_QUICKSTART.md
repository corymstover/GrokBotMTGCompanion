# Lore-first retrieval quickstart (v1 in progress)

Run commands from the repository root. **No API key, web lookup, graph server, or local SQLite is required** for these commands because the compact English/default-language printing archive is committed under `data/printing_lore/`.

```bash
python3 scripts/lore_query.py set lea --limit 10
python3 scripts/lore_query.py card "Urza's Saga" --limit 12
python3 scripts/lore_query.py flavor "Urza" --set atq --limit 12
python3 scripts/lore_query.py lore "Golgothian Sylex" --limit 12
python3 scripts/lore_query.py timeline ar
python3 scripts/lore_query.py timeline invasion
python3 scripts/lore_query.py timeline omenpaths
python3 scripts/lore_query.py candidates "Karn" --limit 30
```

The default is compact JSON, intended for ChatGPT and other automation; add the **global** `--human` flag before the command for a readable view, e.g. `python3 scripts/lore_query.py --human timeline ar`.

### How to read evidence

- `literal_printing_text_match`: the **specific Scryfall printing** contains the searched words in its flavor text or Saga chapter rules text. Not proof of an event's depiction or an in-world relationship.
- `contextual_pointer`: a hand-curated lore entry links another lore entry or card page. Not a direct canon assertion.
- `official_citations`: Wizards URLs cited on the **lore entry**. An entry-level citation does not automatically substantiate each graph edge.
- Timeline `ar`: only the **eight specifically sourced numeric AR rows** in the existing Master Timeline. Do not interpolate missing years or claim every Magic event is exactly dated.
- Timeline `postmending`: editorial/publication sequence, **not** proven in-world temporal order; `invasion` is an editorial phase order; `omenpaths` gives explicit relative markers and is **not** a total chronological order.
- `candidates`: a starter pool for lore-deck design, ranked by **explicit card-page links → curated enrichment → printing-text mention**. It is neither a fully deduplicated decklist nor a canon timeline, and has not been checked for Commander legality yet.

The source printing snapshot is Scryfall `default-cards-20261028090549.jsonl.gz`. This is English/default-language Scryfall bulk coverage, **not** all foreign-language editions. Printing inventory counts differ from unique name/Oracle-card counts, as shown in `set` output.

### Integration notes

The canonical 62 approved Grixis decks and their frozen source snapshot stay **locked and separate**. This lore retrieval system does not edit them. For story-first deck construction, use the evidence output as candidates, then apply Commander legality/singleton/100-card checks before proposing a final list. Do not spend further engineering time merely to add popular cards to a theme; the story should lead the selections.

For the live readiness status, use [GitHub issue #758](https://github.com/corymstover/GrokBotMTGCompanion/issues/758). The repository is still undergoing the limited deck-builder and benchmark stages; this is a quickstart for the retrieval features already working.
