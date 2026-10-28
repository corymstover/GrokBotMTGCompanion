# Deck #60 — M6/IJ scope transfer against M7 Rev1 100 (non-certifying)

**Status: `SOURCE_BOUND_CASE_MAPPING_PASS__IJ_PHASE_B_UNATTESTED`.** This is an
audit of which original M6 commander-effect cases have actually been exercised
under the October 15 baseline and the new research 100. It is NOT a new
independent I/J verdict, an M7 acceptance or a replacement for Phase B.

- Original canonical raw SHA: `8c802586a4742156fb96246f4f23331eb51d1a77d6717da63ceed2446e98adf8`.
- Current research raw SHA: `9a9d2f7a344e2491444c0a0e4c48525dfe8faa37032eaf8e22a94082f6fbf60e`.
- Original `data/grixis/m6/test_blueprints/Tresserhorn_s_Lord__Returned.json`: five P0, ten P1 case IDs. The execution scripts bind the exact old and new 100s by raw SHA and use named frozen Oracle sections; live Scryfall checks bind the proposed new 100.
- Original `data/grixis/m6/ij/input_receipts/tresserhorns-lord-returned.json`: only M6 I/J **input integrity** (`inputs_attested_downstream_incomplete`); `phase_b_replayed: false`, `positive_simulator_verdicts_decisive: false`, `can_decide: false`, and `can_approve_or_lock: false`. The receipt's own `required_next` list includes independent A/B commits, Pass C critique, validated Phase B, judgment review, final receipt bundle and local-optimum certificate.
- Subsequent `data/grixis/m6/sealed/A` and `sealed/B` source artifacts and the `owner_pass_c_substitute/Tresserhorn_s_Lord__Returned/final_disposition.md` **do exist**. The October 21 owner-equivalent Pass C decided **KEEP** of the *old exact 100*, expressly identified itself as not genuinely independent, and said measured Phase B was not performed. These prior materials neither authorize our seven additions nor certify a new 100.

| Original M6 ID | Executed test and proposed-list scope | Changed-card transfer / adversarial risk |
|---|---|---|
| C1 P0 | `m6_p0_followup.py::test_C1*` PASS: exact commander, UBR cast identity, official future-release exception | Commander constant; current Scryfall still not officially legal before Nov 13 |
| K1 P0 | `test_K1*` PASS: exactly 3 other sacrifices + 3 paid life + opponent draws 3 yield 3 Lord draws; Lord self-sac yields one | Remains valid for changed fodder makers; does not grant magical extra creatures |
| K2 P0 | `test_K2*` PASS: Plumb additional sacrifice copies, 2N+1 combined draws and N+1 life lost, finite library/life | Plumb retained; revised token economy can amplify deck-out risk, not false infinite |
| K3 P0 | `test_K3*` PASS: Nightscape reduces Lord generic by one, never both U and R | Nightscape retained in Rev1; the *Alt9* that cuts it needs fresh castability comparison |
| F1 P0 | `test_F1*` PASS: three available bodies, three life, opponent gift; failure with only two | Rev1 adds Genesis/Autocrat and cuts Endrek; source case covers 3-Serf payable and one-body removal adversary |
| K4 P1 | `m6_p1_followup.py::test_K4*` PASS: Not of This World free only if proper power-7+ target | Retained; free-mode does not stop untargeted wrath/edict |
| K5 P1 | `test_K5*` PASS: outgoing 13-sacrifice Edict vs incoming Meathook -X/-X | **Changed wipe:** X=4 kills even the indestructible Lord; X=3 leaves its 4 toughness intact |
| K6 P1 | `test_K6*` PASS: Torpor Orb style ETB suppression blocks native Lord-sacrifice draws | No ETB-hoser introduced; lower-opponent-gift shortcut rejected |
| E1 P1 | `test_E1*` PASS: only creature sacrifices with Lord present trigger its draws | Genesis Myr and Autocrat Serfs are real creature fodder; Treasures alone don't count |
| E2 P1 | `test_E2*` PASS: Fabricate/Mogg, symmetric Chamber, selected Autocrat and rejected Stairwell | **Changed fodder:** Autocrat leaves => exiles all Serfs. No guaranteed fodder against removal; four comparative traces added |
| W1 P1 | `test_W1*` PASS: Locust God/Altar loop bounded by library, not an infinite win | Locust kept; no unsupported table-kill claim |
| W2 P1 | `test_W2*` PASS: Crawler needs a Zombie, Altar mana is spent, Soultrader spends life | Existing central engine retained; opposing graveyard hate/board disruption still effective |
| W3 P1 | `test_W3*` PASS: 10 printed power produces 10 mobilized Warriors; Wand checks actual player damage | Infantry Shield and Wand kept; removal/blocking/trample affect quantity, not deterministic win |
| F2 P1 | `test_F2*` PASS: indestructible doesn't beat exile, edicts or 0 toughness | Meathook's own X≥4 downside now explicit |
| F3 P1 | `test_F3*` PASS: mandatory end-step sacrifice of 10 tokens causes 10 Lord draws | Revised engine must preserve room in library; no unbounded guaranteed win |

Additional Rev1-vs-Alt5 named-state comparisons: `same_start_compare.py`
(4/4 finite PASS): Autocrat turn-four setup can pay Lord turn five; Endrek
turn-five into Lord turn six provides five Thrulls on cast, while removal of
Autocrat can exile Serfs; Village Rites remains castable with one black source
when precommander Swat is not.

## What is and is not transferred

**Transferred:** 15 planned *case names* have new source-bound finite
positive/adversarial executions against the exact proposed 100, and the two
material changed-case families (K5 board wipe, E2/F1 fodder) are explicitly
remapped. These tests and current Oracle do not imply a whole-game engine.

**NOT transferred:** the original I/J receipt never contained a Phase B
decision, independent tested local optimum, validation of alternative whole
deck matched hands, or final judgment receipt; no such attestation exists to
carry over. The new 100 also differs from the old 100 and cannot inherit a
hypothetical old-list result without proof. Do not declare M6/IJ complete,
`READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED`, or owner approval based on
this file. This is a documented certification blocker to be resolved in the
actual approved evidence process, not a request for Cory to rerun tests.
