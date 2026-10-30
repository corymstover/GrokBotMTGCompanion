# Pack B — Thran → Yawgmoth → Old Phyrexia → The Brothers' War (v1, preliminary)

Status: **PRELIMINARY RESEARCH** — tests passing; not owner approved; not certified.
Data: `data/lore_research/pack_b_thran_yawgmoth_brothers_war_2026-10-30.json` (schema `multiverse-claim-pack/v1`),
ingested by the Phase 3 claim graph through `data/multiverse_graph/manifest.json`.

## Sources (all Wizards of the Coast official; fetched 2026-10-30)
| id | source |
|---|---|
| bro_ep1 | [The Brothers' War, Episode 1: The End](https://magic.wizards.com/en/news/magic-story/the-brothers-war-episode-1-the-end) |
| bro_ep4 | [Episode 4: The Ink of Empires](https://magic.wizards.com/en/news/magic-story/the-brothers-war-episode-4-the-ink-of-empires) |
| bro_ep5 | [Episode 5: As Cruel, As Necessary](https://magic.wizards.com/en/news/magic-story/the-brothers-war-episode-5-as-cruel-as-necessary) |
| bro_ch1 | [Chapter 1: Stronghold](https://magic.wizards.com/en/news/magic-story/the-brothers-war-chapter-1-stronghold) |
| bro_card_stories_1/2 | Making Magic: The Brothers' War Card Stories, [Part 1](https://magic.wizards.com/en/news/making-magic/the-brothers-war-card-stories-part-1) and [Part 2](https://magic.wizards.com/en/news/making-magic/the-brothers-war-card-stories-part-2) |
| urza_profile | [Urza, Planeswalker](https://magic.wizards.com/en/story/urza-planeswalker) |
| bro_product_page | [The Brothers' War product page](https://magic.wizards.com/en/products/the-brothers-war) |

## Claims (18): 17 CANON_CONFIRMED, 1 CANON_DISPUTED
B001 Urza–Mishra brothers · B002 Kayla bin-Kroog is Urza's wife · B003 Harbin is their son · B004 Tawnos was Urza's assistant ·
B005 Ashnod worked for Mishra (the rumor that she was his lover is kept out of the claim) · B006 Mishra was corrupted by Phyrexia/Gix ·
B007 Urza activated the Golgothian Sylex on Argoth · B008 the blast shattered Argoth · B009 Urza became a Planeswalker in the blast ·
B010 the Mightstone and Weakstone became his eyes · B011 the Ice Age followed the blast · **B012 the sylex's origin is DISPUTED** (Episode 5 deliberately gives competing legends) ·
B013 Urza's vendetta against Yawgmoth and Phyrexia · B014 Urza's obsession with the Thran · B015 Urza and Yawgmoth perished together ·
B016 Teferi witnessed the blast by time travel · B017 Ajani (a sleeper agent) destroyed the sylex · B018 Saheeli made a replica.

Graph effect: 247 nodes, 366 edges, 50 claims, 31 sources (all official), 20 curated bridges (Urza, Mishra, Yawgmoth, Karn, Teferi, Golgothian Sylex, The Brothers' War, and others). Query example: `python3 scripts/query_multiverse_graph.py path mishra yawgmoth`.

## Not yet covered (see `remaining` in the pack)
- The Thran civilization and Yawgmoth's Thran-era origin. No official web source fetched yet; the novel *The Thran* has **not** been read.
- Koilos, Tocasia, and the splitting of the powerstone (novel-era).
- Gix and the Brotherhood of Gix chronology; Old Phyrexia's spheres and the shift to New Phyrexia (the Planeswalker's Guides to ONE and MOM are not yet ingested).
- Episodes 2–3 and Chapters 2–5 were fetched but only keyword-searched.
- BRO card anchors are not attached yet.
