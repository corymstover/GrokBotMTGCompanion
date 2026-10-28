# Nekusar M6 P1 closeout — exact current M7 Rev1, bounded tests

**Approved raw SHA-256:** `043d2521cec1e82d7ba8ff899b96920249e16ae32e73e2759f02044b41f94e53`.
**Source:** `nekusar_m7_candidate_rev1.txt`, same exact 100 as current canonical approved Nekusar.
**Test:** `python3 data/grixis/m7/nekusar_rev1/test_nekusar_m6_p1_closeout.py`.
**Oracle source:** current Scryfall cache (bulk updated 2026-10-27), plus the live 97-name Nekusar M7 checks in PR #721/#722.

This packet is a source-specific micro-model for **original P1 case triage**. It is not a rules-engine simulation, full priority resolution, M6 local-zero-improvement proof, or J certification. Do not upgrade the canonical M7 transfer statuses without a separate evidence review and exact SHA reconciliation.

| Original M6 P1 | What source-bounded cases now establish | Honest residual status |
| --- | --- | --- |
| K4 Curiosity / Nekusar | Opponent draw produces Nekusar damage, then optional Curiosity self-draw; drawing yourself does not recursively trigger Nekusar | Bounded positive/adversarial trace, not total stack proof |
| K5 Krang self-punishment | `Spiteful Visions` and `Phyrexian Tyranny` have both been cut in the exact current 100 | **Historical source case inapplicable; needs formal disposition, NOT passed** |
| K6 discard vs shuffle | `Wheel of Fortune` feeds Waste Not/Caress; `Winds of Change` and Molten Psyche shuffle, not discard; Molten Psyche requires 3 artifacts for damage rider | Bounded positive/adversarial trace |
| E1/E2 engine | Nekusar and qualifying punisher must be active when the draw occurs; Krang duplicates Nekusar triggers, and Ghyrson follows each exact-one damage event | Bounded source-specific trace |
| W1 Peer kill | `Peer into the Abyss` was removed from this exact 100 | **Historical source case inapplicable; needs formal disposition, NOT passed** |
| W2 Breach/Wheel/Will | One two-spell escape needs six other graveyard cards, actual initial mana, and usable Jeska's Will mana; examples with five cards, two starting mana, or zero-card opponent hand fail | **Deferred:** no proof of all stack/priority windows, repeatability, draw-outs, or guaranteed kill |
| W3 Niv/Curiosity | Niv damage to opponent permits optional draw, triggering a further Niv damage; stopping, no target, finite library and life are concrete stopping conditions | Bounded trace only; opponent counterplay unmodeled |
| F2 Narset/Notion Thief | **Correction:** opposing Narset only limits *its controller's opponents*, not its controller. With players A=Nekusar and B=Narset, a seven-card wheel gives B seven draws and other opposing players one each (9 Nekusar triggers total, assuming no earlier draws). With B controlling Notion Thief, B can receive all 28 draws in a four-player wheel and be hit by Nekusar for each; this is not a universal shutdown. | Meaningful rules/strategy correction; stack responses remain outside fixture |
| F3 lifegain | Seven Nekusar pings against 25 life plus ten lifegain cannot be called lethal | Bounded negative counterexample |

**Commander-first judgment:** keep Nekusar's damage-on-opponent-draw identity. The old F2 blanket warning should be amended in future strategy documentation, not turned into a random new inclusion/cut. This evidence identifies **no independently justified card swap**. All cards remain locked; no milestone counters or canonical state are altered by this file.
