# Lore-first MTG Companion — v1 READY (2026-10-28)

**Purpose:** Help Cory begin making story-exhibit, funny, epoch-based, character-based, and plane-based Commander decks **now**. This is an operational first version, **not** a claim that all future MTG fiction or all printed languages have been exhausted. Stop infrastructure work unless a real deck or research question demonstrates a blocker.

## ChatGPT's first step on a new request

1. Ask for a theme if Cory hasn't already named one. Commander/color identity are optional at first. Story significance, printed flavor, and honest lore links take priority over EDHREC popularity or power.
2. Query the committed knowledge source:

   ```bash
   python3 scripts/lore_query.py beats "Ugin vs Nicol Bolas"
   python3 scripts/lore_query.py lore "Karn" --limit 20
   python3 scripts/lore_query.py flavor "Urza" --set atq --limit 40
   python3 scripts/lore_query.py set lea --limit 15
   python3 scripts/lore_query.py card "Strip Mine" --limit 15
   python3 scripts/lore_query.py timeline ar
   python3 scripts/lore_query.py candidates "Phyrexian Invasion" --limit 40
   ```

   Commands default to compact JSON. A locally installed repo is ideal, but a GitHub-only assistant can fetch `data/printing_lore/manifest.json` then the indicated small shard(s), `data/lore_graph.json`, and individual indexed lore pages. Use [LORE_QUERY_QUICKSTART.md](LORE_QUERY_QUICKSTART.md) for field meanings and commands.
3. Build a chronological *reading sequence* with explicit source and uncertainty for each beat. Only claim an exact date from a specific official citation, not from release order or graph co-occurrence. A retcon remains a retcon. If a silly theme has no entry, match literal card text first and label the creative interpretation.
4. Choose cards **because they depict, quote, name, or evoke** the story; include basic lands and nonbasics with relevant printings when possible. Every card gets a short reason. Name-match, same-set printing, and mechanical echo are **different kinds of evidence**.
5. Pick a Commander-legal commander/identity and present a **proposed** 100-card list, preferably with choices for weak narrative links. Do not force incompatible colors into a deck. The example composer is `scripts/story_deck_planner.py`; the hard-rules evaluator is `scripts/evaluate_decklist.py`.
6. Validate 100 count, commander eligibility, color identity, singleton, bans, land mix, Game Changers, mass land denial, and relevant combo/bracket concerns. **The user approves or locks decks—not a script.** Do not modify Cory's 62 approved Grixis lists.

## Evidence boundaries (non-negotiable)

- **Literal printing text**: the specific Scryfall card/face/set/collector displays an exact flavor phrase or Saga chapter. This proves words are on a printing, **not** that the scene happened as described.
- **Official story citation**: a relevant `magic.wizards.com` page supports the claim actually expressed in that passage. An entry's list of citations is not blanket proof for all its graph edges.
- **Contextual pointer**: a curated lore entry links a character, era, object, plane or card. The relationship is navigational, not automatically causal or chronological.
- **Creative/thematic inference**: a deliberate aesthetic choice; label as inference or playability. Never promote it to canon by repeating it.
- **Canon uncertainty**: distinguish retcons, altered histories, universes beyond, missing sources, published-story order and exact AR dates. Do not invent events or claim a unique canon timeline where sources disagree.

## Accepted v1 footprint and limitations

| Resource | Verified footprint | Limitation |
|---|---|---|
| Committed printing/flavor archive | 105 small JSONL shards; 1,062 set codes; 119,509 printing objects in the 2026-10-28 Scryfall `default-cards` snapshot | English/default-language coverage; not every foreign-language edition |
| Lore graph | 280 curated lore entries, 422 nodes and 1,062 directional typed pointers | Pointers are not direct proof; official URL/printing matching is queried on demand |
| Timeline | Eight source-cited numeric AR events; five invasion phases; 12 Omenpath relative markers | Omenpaths and post-Mending publication order are not a total absolute chronology |
| Queries | `set`, `card`, `flavor`, `lore`, `timeline`, `candidates`, `beats` | Literal-text retrieval can miss implicit/art-only symbolism; use official story research when needed |
| Story deck example | [Karn's life: 100-card colorless prototype](data/lore_decks/examples/karn_life_story_draft.md) | **Unapproved**. Rules pass on supplied Scryfall bulk; per-card lore claims still require judgment; combo/bracket assessment is provisional |

Source provenance: Scryfall `default-cards-20261028090549.jsonl.gz`, SHA-256 `c7c6d738cae2a9419e2120afedba460c4afeaa026bf74ca60e6451d14486d1e2`. Existing Grixis development lock `data/grixis/dev_snapshot_lock.json` is separate and unchanged. The locally indexed SQLite file is a speed cache, not a GitHub binary asset. The 105 committed shards are sufficient for offline/repo-only lookups.

### Repeatable acceptance gate

```bash
python3 scripts/check_lore_ready.py
python3 scripts/check_lore_ready.py --bulk-file /path/to/explicit-lore-Scryfall-default-cards.jsonl.gz
```

The first runs completely offline against committed data: Alpha = **295 printings / 290 names**; Strip Mine = **2** different flavor texts; Evolving Wilds = **27**; The Antiquities War has Saga chapters; `Karn Dogs` hits Concession Stand; eight official-dated AR events; Ugin/Bolas has four beats; Phyrexian Invasion has five; a short *March of the Machine* title resolves; and the Karn 100-card spec has provenance and no Mycosynth Lattice lock. The optional second command checks the Karn example through the existing hard-rules evaluator using a specifically named local Scryfall snapshot; this was **PASS** (100 cards, colorless identity, 35 lands, zero hard issues). Its Bracket 2 minimum estimate is not a guarantee until combos and individual gameplay are reviewed.

## Updating the knowledge safely later

1. **Don't refresh the frozen Grixis source or touch its 62 approved decks.** New lore-only printings should live in a separate `.cache/lore-printings/` source, selected explicitly via `scripts/printing_lore_index.py --source ...` and re-exported through `scripts/export_printing_lore.py` only when needed. Preserve source filename and SHA-256.
2. Rebuild/check the compact printing export and the lore graph only if their actual inputs change. Keep their evidence semantics explicit; add a new official page/retcon record when it resolves a real deck question.
3. Rerun focused tests and `scripts/check_lore_ready.py`. A new MTG release may require new citations or a fresh snapshot; no nightly rebuild or heavyweight graph service is needed to start building decks.

## Stop-engineering gate

**READY means:** This repo can already take a character, era, plane, set, event, or joke and return meaningful evidence-linked deck candidates, a source-qualified story arc, and a Commander-checkable 100-card draft. It does **not** mean all lore claims are preverified or every conceivable card automatically belongs in a specific deck. The next normal action is to **ask Cory which deck to build**.

The live readiness ledger is [GitHub issue #758](https://github.com/corymstover/GrokBotMTGCompanion/issues/758). No infrastructure work is scheduled after this v1 gate unless a concrete question demonstrates a material gap.
