# Phase 4 — source-linked Dominaria/Kamigawa, Urza and Karn historical order

**Checkpoint:** 2026-10-31
**Status:** PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED; NOT_RELEASE_READY.

## Primary evidence and exact scope

1. Wizards' [Dominaria plane profile](https://magic.wizards.com/en/story/dominaria-plane)
   describes Urza and Mishra, their Caves of Koilos powerstones, the Brothers'
   War, resulting Ice Age, Urza finding Phyrexia, the subsequent Phyrexian
   threat and the Weatherlight/Legacy response. A *separate branch* records
   Dominaria's temporal fractures, outward damage, Planeswalker Mending and
   later profile-era rebuilding.
2. Wizards' [The Known Mutliverse](https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19)
   gives the specific cross-plane causal link: Dominarian planar-temporal rifts
   weaken the barrier between Kamigawa's two realms, enabling Konda's theft
   and the subsequent Kami War. These are *not* the same event as every other
   Dominarian disaster, and their exact AR dates are not supplied.
3. Wizards' [Karn profile](https://magic.wizards.com/en/story/karn-planeswalker)
   recounts the Urza-built silver golem, his independent Planeswalker legacy,
   creation of a world, its Phyrexian corruption and his determination to
   prevent Phyrexian domination. Only the *creation by Urza* is marked as
   the same historical event as existing ledger node `C:karn_created`, whose
   source already quotes the **same official Karn profile**.

The new `R` history strand adds **14 events / 12 strict edges**; the `U` Karn
strand adds **5 events / 4 strict edges**. The committed chronology artifact
now has **11 strands / 107 events / 87 strict BEFORE edges / 354 of 5,671
source-local ordered event pairs**. There are now **eight** source-corroborated
cross-ledger `SAME_EVENT` bridges, up from seven, with no strict cycles. The
56-event legacy chronology is unchanged and its separate 177 ordered pairs
must not be summed with the local counts.

## Provenance and boundaries

- The Dominaria profile's Brothers' War and Ice Age references do **not** order
  ice-age onset relative to Urza finding Phyrexia at war's end.
- The Kamigawa source ties Dominarian rifts to Konda's kidnapping, but does
  **not** date the Kami War against the Mending or first invasion.
- The Karn profile's corruption of his world is not automatically an identity
  bridge to the separate 2008 account of an unnamed contagion on Argentum;
  cross-strand queries without explicit proof remain `UNKNOWN`.
- A profile's historical “today” is not the actual status of Dominaria on
  2026-10-31. Neither a current census nor full-source chronology is claimed.
- The source-limited Phase 4/5 history and L244 requirements remain open.
  No owner approval, deckbuilding, relative AR date, new canon retcon
  resolution or certified release is inferred.

## Reproducible safety checks

```sh
python3 scripts/source_event_sequences.py --check
python3 scripts/source_event_sequences.py --live
python3 scripts/query_lore_chronology.py --check
python3 scripts/build_foundation_acceptance_packet.py --check
python3 -m unittest tests.test_phase4_dominaria_karn_chronology tests.test_source_event_sequences tests.test_foundation_acceptance_packet -q
```

The live source verifier passed **98 exact quote excerpts over nine Wizards
pages**. A new regression suite checks the explicit cross-plane path, the
Karn `SAME_EVENT` proof, Q&A citation flags, unconnected negative cases, and
rejection of duplicate source-local strand IDs. Six representative acceptance
questions include both proven and unresolved relations, bringing the
knowledge-only Phase 8 review packet to **59 cases**; that packet remains
**NOT CERTIFIED**. The 62 approved Grixis lists, three parked unapproved
pilots and all Scryfall snapshot/owner approvals are untouched. Checklist
stays **89/137 checked, 48 open**.
