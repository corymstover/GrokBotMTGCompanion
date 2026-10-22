# Admiral Beckett Brass — M7 stage 6 targeted real-cost threshold adjudication (2026-10-22)

**RESEARCH_ONLY / NOT OWNER-READY.** Retain Admiral's approved canonical 100 and raw SHA-256 `4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414`. The full card-by-card source records and EDHREC discovery capture are in stage-3/4 artifacts. None of the 7/8/9-swap variants has an adopted new M6 I/J certificate.

## One discriminating question

**Does exchanging Open into Wonder for Dreamcaller Siren—or Kari Zev for Storm Fleet Aerialist—materially increase reliable *three separate Pirate hits to the same player* at payable timing once relevant opposing blockers and the incumbent payoffs are modeled?**

This bounded analysis does not assert multiplayer win-rate, and does not rerun large inconclusive simulations.

| Game state, known resources | Seven-swap Regalia/Wave retains Open into Wonder + Kari Zev | Eight-swap Dreamcaller / Nine-swap both | Decision-relevant difference |
| --- | --- | --- | --- |
| Three Pirate attackers, four eligible blockers, Regalia makes one attacker unblockable, at least 5 mana for X=3 Open | Open into Wonder targets three; assuming it resolves and hits are not prevented, all three get through and each hits draw a card | Dreamcaller at UU + two generic taps only two blockers; two remaining can block other Pirates, so only protected one is assured | **Open dominates this multi-blocker threshold and card-replenishment state** |
| Three pre-existing Pirate attackers, exactly two eligible blockers, four payable mana including UU, another Pirate already controlled | Open into Wonder at X=3 costs 5, one more than available; Wave at 4 mana may still unblock all, if held | Flash Dreamcaller can tap both before blocks and allow all three to connect; its body is an extra Pirate for later combats | **Dreamcaller creates one legitimate earlier-payable window**, but Wave may offer a similar window and Siren cannot attack immediately without haste |
| Defender with instant Fog or removal of one of exactly three unblocked Pirates | Three-hit Admiral threshold can fail despite Open, Wave, Dreamcaller or Regalia | Same failure; adding an evasive card doesn't make the exact-three-source trigger inevitable | Additional Pirate density/resilience and opponent response modeling remain important |
| Aerialist vs Kari Zev, defender has two ground blockers but no flying blockers | Kari Zev's menace can be jointly blocked, even though her Ragavan token adds separate Monkey combat damage | Aerialist's flying has an unblocked line as an actual Pirate; Raid counter only helps after a turn's attack, not retroactively | **Aerialist improves this Pirate-specific connection state** |
| Aerialist vs Kari Zev, defender has exactly one flying-capable blocker | Kari Zev's menace cannot be blocked by a lone creature | Aerialist can be blocked by the flying creature | **Kari Zev is better in the reverse state**; neither is universally dominant |

**Qualitative, nonfinal disposition:** Storm Fleet Aerialist is a credible **RETAIN_ALTERNATIVE** for a true Pirate-density upgrade over Kari Zev in the seven-swap Regalia/Wave shell. Dreamcaller Siren remains a **RETAIN_ALTERNATIVE** for early two-blocker boards but is not justified as an automatic replacement of Open into Wonder: the repeatable Pirate body is attractive, yet Open is more reliable for the targeted theft trigger against wide defenses and immediately draws cards. The combined nine-swap variant is **not automatically superior** to either eight-swap list or the original seven-swap source. More changes are welcome when better, not because nine looks more thorough.

The retained seven-swap source itself remains research-only: replacing Bident of Thassa loses repeatable combat card draw; replacing Fiery Cannonade loses cheaper instant-speed mass interaction. Stage-3 Oracle snapshots establish their actual costs/timing. Regalia + Wave has synergy but requires two distinct cards, whereas Open into Wonder at X=3 uses one five-mana spell to get three hits and three draws. No forced package selection.

## Verification scope and next step

The deterministic regression `tests/test_m7_admiral_stage6_decision_bound.py` asserts the 7/8/9 source integrity, payable source costs, four- and two-blocker cases, an adverse Fog/removal example, and reciprocal Aerialist/Kari evasion examples. It has **no whole-game magic state engine** and treats ward, priority, response cards and mana colors separately. Any current CI receipt certifies only those assertions.

**Next substantive comparison:** Compare the best surviving Regalia/Wave + Aerialist route against the previously staged seven-swap Storm/Shizo and other six-swap Bident-preserving packages, explicitly valuing persistent draw, recursion, mana color and instant-speed defense alongside three-hit frequency. Choose and source-bind the single best full 100; then rerun only invalidated P0/P1 fixtures and formal candidate-specific M6 I/J before owner presentation.
