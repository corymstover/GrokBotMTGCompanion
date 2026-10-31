# Phase 5 — Four underdocumented plane histories, source-graded (v2.65)

**Status:** PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED. No lore decks, current-world-state guarantees or foundation certification.

The named-plane dossier index has **33 registered planes**. This pass adds **11 directly incident `CANON_CONFIRMED` claims** to four planes that previously had fewer than five such claims. Consequently **12**, rather than 16, registered planes still have fewer than five distinct direct claims. This is a *threshold for auditing coverage*, not a definition of a complete history.

| Plane | Direct claims before → after | Official evidence and bounded historical content |
| --- | ---: | --- |
| **Eldraine** | 3 → 5 | [2019 Planeswalker's Guide](https://magic.wizards.com/en/news/feature/planeswalkers-guide-eldraine-2019-10-31): five courts govern **the Realm**, and human ascendancy displaced elves there eight or nine generations before the guide's narrative present. The Realm is **not** the whole plane. |
| **Ikoria** | 4 → 6 | [2020 Planeswalker's Guide](https://magic.wizards.com/en/news/feature/planeswalkers-guide-ikoria-2020-04-02): Drannith and the mobile Skysail sanctuary. This does **not** establish their condition after later invasions. |
| **New Capenna** | 2 → 5 | [2022 Planeswalker's Guide](https://magic.wizards.com/en/news/feature/planeswalkers-guide-to-streets-of-new-capenna): the refuge-city's founding, the archangels' early defense and the invasion of Old Capenna. The guide describes the invaders as **forgotten**; this pack does **not** silently name them. The city and the plane are distinct entities. |
| **Argentum** | 1 → 5 | [New Phyrexia overview](https://magic.wizards.com/en/story/new-phyrexia-plane), [From the Vault: Lore](https://magic.wizards.com/en/news/feature/vault-lore-2016-08-01) and [The Known Multiverse (2008)](https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19): Karn's artificial world, Memnarch as its watcher, the early oil contagion and the historical renaming to Mirrodin. These are **past-era names**, not claims about post-March of the Machine politics. |

The 11 claims and six primary-source URLs are recorded in `data/lore_research/pack_p5_thin_plane_history_2026-10-31.json`. Each stores the excerpt, source metadata, a grade and an explicit caveat. No release date or narration-relative span is converted into an absolute in-universe timestamp.

## Reproducibility and Q&A

```
python3 scripts/build_multiverse_graph.py --check
python3 scripts/build_plane_history_dossiers.py --check
python3 scripts/audit_p5_thin_plane_history.py --check
python3 -m unittest discover -s tests -p 'test_p5_thin_plane_history.py' -q
python3 scripts/build_foundation_acceptance_packet.py --check
python3 scripts/mv_ask.py ask 'What is the history of Argentum?'
python3 scripts/mv_ask.py ask 'What is the history of New Capenna?'
```

The auditor's optional `--live` mode fetches all six source pages and checks quoted text in their HTML; the offline CI test gates graph incidence, source records, the four five-plus dossier counts and the route's `complete_history: false` / `verified_total_chronology: false` safeguards.

The deterministic foundation acceptance packet now contains **26 representative Q&A cases**, including one cited history answer for each of the four expanded planes. Registered character/faction coverage also updates automatically from 629/629 to **630/630**: the historical Old Capenna archangels correctly reuse their existing entity ID, and only the unidentified invaders are a new registered faction. This does **not** certify all factions in canon. Current graph: **1,222 claims, 5,209 nodes, 8,324 edges**. All 33 planes have some direct evidence, yet 12 remain thin by the five-claim audit threshold. The original 62 approved Grixis decks and three unapproved pilots are untouched.

**Open work:** deeper plane histories and cross-plane consequences, the unresolved L244 total chronology, primary-source gaps, rule and set qualification gaps, exact-head release CI and Cory's documented owner review. The existing **83/137** engineering checklist stays unchanged, and foundation readiness remains **NOT_RELEASE_READY**.
