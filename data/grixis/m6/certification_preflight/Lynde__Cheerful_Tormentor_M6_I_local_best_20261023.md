# Lynde__Cheerful_Tormentor (Lynde, Cheerful Tormentor) — M6 I local-best memo for the M7 research candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved, NOT M6 certified and NOT owner-presentable. Its readiness is `RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE` for two reasons:
- there are two genuine swaps, below the five-swap floor;
- the existing M6 Pass C Stage A seal does not match its file, so the shared J checker rejects any bundle for this deck. Expected `59f2dc10…`, actual `02adfb85…`, seal commit `c4c5fa5d` (Stage A commit `b4c98568`). The sealed value is exactly the SHA-256 of the committed `stage_a.md` without its final newline byte (the committed file is 13276 bytes and ends in `.\n\n`). See the adversarial packet.

The canonical list is unchanged.

Scope: the thirteen complete configurations in `data/grixis/m6/ij/tested_pools/Lynde__Cheerful_Tormentor_M7_tested_configurations_20261023.json`, plus the named single-card contenders. Each configuration is 100 cards (1 commander and a 99-card library). This is not a global or statistical optimum.

Identity:
- Tracker Deck 31 (index 30). Deck ID `Lynde__Cheerful_Tormentor`, commander Lynde, Cheerful Tormentor.
- The overrides (APPROVED / LOCKED, 2026-10-14) and the registry agree. Tracker row 30 detailed-gate sub-fields still read PENDING, and the decisions document header hashes are the pre-change source values. Both are disclosed, not changed.

Baseline:
- Canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, file `refinement/decklists/Lynde_Cheerful_Tormentor_Approved_2026-10-14.txt`.
- Git blob 5731e689, introduced by canonical commit 7258398 (2026-10-14). Registry source_commit 1836b97 has the same bytes.
- Raw SHA-256 05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166. It equals the overrides `approved_list_sha256` and the registry recorded hash, so no provenance exception is used.
- Logical hash lh1:7359723b…, the same as the registry Archidekt export.

## Commander text (frozen cache, identical on live Scryfall)
Lynde, Cheerful Tormentor ({1}{U}{B}{R} Legendary Creature — Human Warlock 2/4):
- deathtouch;
- whenever a Curse is put into your graveyard from the battlefield, return it to the battlefield attached to you at the beginning of the next end step;
- at the beginning of your upkeep, you may attach a Curse attached to you to one of your opponents; if you do, draw two cards.

Selection rule: a card earns a slot if it puts more Curses on you for Lynde to move, sends your own Curses to the graveyard, or gives Lynde more upkeeps, and a Curse is weakest when holding it for one turn hurts you.

## Result
The candidate (raw 435717e0…, lh1:a125b992…) is the canonical 100 with two swaps:

| # | Add | Cut | Confidence |
|---|---|---|---|
| 1 | Court of Vantress | Cruel Reality | MODERATE |
| 2 | Extravagant Replication | Curse of Death's Hold | MODERATE |

No owner keep or owner add is cut. Neither cut is in the protected core.

Local best within the pool, by measure:
- **Self-Curse upkeep stack (grid B1, 246 cells):** with Cruel Reality returned to you, Lynde is the forced sacrifice in 42/96 cells (0 without it); with Curse of Death's Hold returned to you, an X/1 dies in 32/96 cells (0 without it).
- **Copy-engine supply (grid B3, 180 cells):** Lynde draws 82 → 204 and Curse tokens 0 → 102 with Court (as monarch) or Replication; both together give 204 tokens. Court not monarch gives 82/0.
- **Cut versus add (grid B4, 72 cells):** Cruel Reality self-harm 6, Death's Hold 4; Court and Replication 0.
- **Deployment cost:** P(Lynde cast) by turn 4 0.629 and by turn 7 0.8681 for both baseline and candidate. P(Lynde with Court or Replication) by turn 7: 0 → 0.1381.
- **Staff of Compleation over Nightscape Familiar:** staged trade, outlet coverage 0.2716 → 0.3379 for a slower Lynde (turn 4 0.629 → 0.6179).
- **Single-swap alternatives:** alt A (Court only) and alt B (Replication only) are complete 100s for an owner who wants to keep one of the two table locks.
- **Rejected:** Curse of Chaos (owner removed), Strionic Resonator and Beseech the Mirror (owner rejected), Disturbing Mirth, Teferi's Ageless Insight, Thoughtrender Lamia and Curse of the Bloody Tome (each dominated by the incumbent they would cut).

## Not claimed
No win rate, no source-bound engine receipt and no M6 certification. The I/J certificate in this PR is `blocked`, not `pass`.
