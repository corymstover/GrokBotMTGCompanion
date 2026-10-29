# Cory's approval: Story-First Lore Deck #10 — Yawgmoth

**Decision:** APPROVED and archived on 2026-10-29 (America/Chicago).

**Owner authority:** Cory explicitly replied **“Approved”** immediately after being presented with the complete final 100-card Yawgmoth biography decklist, the four final story-first swaps, and raw decklist SHA-256 below. This is a specific approval of the exact displayed list, not approval of future substitutions.

**Approved deck title:** *Yawgmoth: Father of Machines — A Biography of the Thran Tyrant and His Posthumous Shadow*.

## Immutable approved artifact

- Original proposal and owner approval: [PR #777](https://github.com/corymstover/GrokBotMTGCompanion/pull/777).
- Source branch: `chatgpt-lore-yawgmoth-biography-deck10-20261028`.
- Exact approved source head: `a27cd17b1a42d01f852c81e08ad71f032efea150`.
- Squash merge commit on `main`: `010fc989461d45ad52a637fe4d7bd17c5ad952ad`.
- Approved raw decklist SHA-256: `d77fb2e2976c01c18db233a3e39816241f46e891c696b9a301a85bbd75b9812f`.
- Count: exactly **100 cards**, **30 lands**, **WUBRG** identity, **90 distinct commander/nonbasic names and 10 basic land copies**.
- Actual printed flavor found on **58** of the selected 90 nonbasic/commander printings.
- Importable decklist: `data/lore_decks/drafts/yawgmoth_complete_biography_decklist.txt`.
- Chronological story/source/printing dossier: `data/lore_decks/drafts/yawgmoth_complete_biography_proposal.md`.
- Machine-readable story evidence: `data/lore_decks/drafts/yawgmoth_complete_biography_proposal.json`.
- Exact printing evidence: `data/lore_decks/drafts/yawgmoth_complete_biography_printing_evidence.json`.

## Final exact four-for-four narrative revision approved

| Removed | Added | Exact printed edition |
|---|---|---|
| Dark Ritual | Phyrexian Reclamation | Urza's Legacy ULG #63 |
| Gixian Infiltrator | Phyrexian Broodlings | Urza's Legacy ULG #58 |
| Yawgmoth's Vile Offering | Phyrexian Tyranny | Planeshift PLS #118 |
| Phyrexian Vivisector | Phyrexian Slayer | Invasion INV #118 |

The earlier five Bones of Ramos and Henge of Ramos were also intentionally removed from the 99. **Ramos, Dragon Engine remains the commander only** as a five-color framing device, not a claim he personally witnessed ancient Thran history.

## Explicit interpretive and Rule 0 exceptions approved

1. **Yawgmoth's Bargain**, **Sundering Titan**, and **Tolarian Academy** are banned in sanctioned Commander. Cory intentionally retains all three for story accuracy under **Rule 0**; do **not** claim sanctioned-Commander legality.
2. **Ramos, Dragon Engine** is a lore-connected WUBRG framing commander. The 99 tells Yawgmoth's antagonist-centered story, including the Thran, Gix, K'rrik, Rath, Invasion/Apocalypse, and the posthumous New Phyrexian legacy.
3. Specific printings carry critical flavor or art evidence. In addition to the final four editions, select **Toxic Deluge CC2 #6**, **Corrupt USG #124**, **Retaliation USG #272**, **Planar Portal INV #308**, **Warped Devotion PLS #57**, **Great Furnace BRC #187**, and other pinned evidence listed in the source dossier. Plain-name imports may lose intended editions.
4. **Yawgmoth died at the end of the original Invasion.** New Phyrexia is his later legacy, not a resurrection or evidence that he personally ruled the posthumous regime.
5. The research dossier did **not** claim to have read the full 1999 novel *The Thran*. It distinguishes official Wizards narrative, original card printings, and contextual or secondary research.
6. Story-first selection deliberately overrides card power, optimization, and ordinary ban-list restrictions. No independently certified power bracket or full gameplay-combo audit is asserted.
7. This approval **locks the raw decklist SHA above** against unapproved card substitutions.

## Validation and post-merge verification

- Offline Scryfall snapshot rules evaluation found exactly **100 cards, 30 lands, WUBRG color identity** and **only the three deliberate banned-card Rule 0 issues**; therefore its automated sanctioned-legality status is correctly failed, not misrepresented as a clean rules pass.
- The exact PR head had a successful *Focused Grixis mechanics validation* GitHub Actions run. That general-purpose workflow is **not** falsely described as a dedicated certification of this lore list.
- After PR #777 was merged, **all four** files were re-fetched from `main` and compared **character-for-character** to the approved local source files: **4/4 exact matches**.

**Preservation:** This approval applies only to Story-First Lore Deck #10. The 62 previously approved Grixis Encyclopedia decks and other approved lore decks remain untouched. Pending unrelated lore proposals are not approved by this record.
