# Deck #27 — Grixistax (Kraum // Tevesh Szat) — independent M7 Rev1 owner review

**Status: OWNER REVIEW READY; NOT OWNER APPROVED OR CANONICAL.** 2026-10-25 (America/Chicago). No canonical list, lock, registry, or other deck is modified by this research artifact. The owner must explicitly approve the complete exact 100-card candidate and raw hash before a separate canonical PR.

- Canonical approved source: `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Grixistax_October_2026_Approved_2026-10-14.txt`
- Canonical source SHA-256: `f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c` (byte-for-byte preserved in this PR)
- Proposed source: `data/grixis/m7/candidate_lists/Grixistax___October_2026_ChatGPT_Rev1.txt`
- Proposed raw SHA-256, terminal LF: `70b48148409e849e38d7189bcda032d1c98d74329302563a005f86a86b81279e`
- Prior Grok first pass: [research-only PR #675](https://github.com/corymstover/GrokBotMTGCompanion/pull/675), two-swap recommendation, **not adopted**.
- This independent review uses the owner's October 14 full-deck decisions and the Oct 23 214-name Scryfall source archive as evidence, not as automatic approvals.

## Commander-first thesis

This is a Grixis **prison-resource** deck, not a generic Thassa's Oracle / Consultation turbo conversion. Kraum's second-spell trigger draws through opposing interaction; Tevesh creates Thrulls and converts bodies into cards. Thrulls should independently maintain Contamination, absorb Tangle Wire, feed Skullclamp/Diabolic Intent/Culling the Weak/Phyrexian Tower, and now provide tap or sacrifice resources. The candidate retains the Helm + exile win and Breach/LED/Brain Freeze win packages, together with Wheel of Fortune and Windfall for Narset/Notion Thief. Natural ceiling remains Bracket 5, fringe/rogue cEDH.

## Five one-for-one swaps, with costs

| Add | Cut | Improvement, and the real loss |
|---|---|---|
| **Arcane Signet** | Mox Amber | A guaranteed Grixis-colored artifact mana source once cast, especially under Contamination or Moon effects; gives up a conditional zero-mana accelerant that can be live with Ragavan, Narset, Sheoldred, or a commander in the old list. Grok's 40,000-sample-per-cell goldfish found turn-4 mean sources 3.138 → 3.193 for the isolated rock swap; not a win-rate estimate. |
| **Bitterblossom** | Magus of the Moon | Independent 1/1 flying token each upkeep for Tevesh, Contamination, Skullclamp, Opposition, and Phyrexian Altar. Magus was a fragile redundant Moon and triggers our own Overburden; loses a second Blood Moon effect and a turn-three proactive land lock. Blood Moon and Back to Basics remain. Bitterblossom's mandatory one life each upkeep matters alongside Necropotence. |
| **Opposition** | Ashiok, Dream Render | Turns Tevesh Thrulls, Faeries, and Snakes into repeatable taps of opposing lands, creatures or artifacts. Its enchantment ability survives Cursed Totem; at the previous player's end step it can tap our own Winter/Static Orb, disabling its restriction for our untap, then the artifact untaps and re-enables its restriction for opponents. This is a new way to break prison parity, but costs 2UU, is harder to resolve through Contamination, and drops one tutor/graveyard denial card. Opposition Agent, Dauthi Voidwalker and Leyline remain. |
| **Phyrexian Altar** | Damping Sphere | Free sacrifice of Thrulls/Faeries/Snakes to produce **any** color, giving Tevesh genuine colored-mana parity under Contamination, Blood Moon and Back to Basics. The sacrifice ability is on an artifact, so Cursed Totem does not stop it. **Important owner-priority override:** Damping Sphere was an express October 14 KEEP. Removing it weakens anti-storm and big-mana coverage and gives up a cheap turn-two tax; Trinisphere, Chalice, Narset and stack protection remain. Approval of Rev1 would deliberately supersede this one specific KEEP. |
| **Ophiomancer** | Sheoldred, the Apocalypse | A Snake whenever an upkeep begins with no Snake in play; using Skullclamp, Altar or Tevesh +1 can replenish it across turns, allowing reliable Contamination payments and deterring attacks on Tevesh. Its upkeep trigger is not a creature activated ability and works under Cursed Totem. Losing Sheoldred means giving up a formidable standalone win clock, draw punishment, and life replenishment for Necropotence/Bitterblossom; this is the sharpest late-game cost of the revision. |

This is a **quality-argued five**, not a count padded with cosmetic swaps. The two contested cuts (Damping Sphere and Sheoldred) remain open for owner judgment; neither is silently treated as weak.

## Why the prior research-only two-swap result changed

Grok's +Bitterblossom / −Windfall line undervalued Windfall in a shell already containing Narset, Notion Thief, Orcish Bowmasters and formerly Sheoldred. Windfall remains as the second wheel to back up Wheel of Fortune, with a strong opposing-resource-denial ceiling when paired with draw restriction or draw theft. The revised Bitterblossom cut is the third Moon effect instead. The previous research rejected Opposition primarily by turn-four raw castability; this packet explicitly recognizes its tap-our-own-Orb parity line and its compounding value with two independent creature-token engines. This is a strategic inference from Oracle interactions, **not** an observed match win-rate improvement.

Urza, Lord High Artificer was reconsidered but is not chosen: our own Cursed Totem shuts off Urza's creature activated mana ability, and Torpor Orb suppresses his Construct-producing entry trigger. Opposition/Altar are enchantment/artifact activated abilities instead, preserving the hate package.

## Exact mechanics and sequencing caveats

1. If Bitterblossom and Contamination trigger on the same upkeep, put Contamination's trigger on the stack **first**, then Bitterblossom on top; the Faerie enters before Contamination's sacrifice trigger resolves. If Ophiomancer also triggers (you have no Snake at upkeep start), you can likewise stack it to create a Snake before the sacrifice.
2. Ophiomancer checks for Snakes both at trigger time and at resolution; keeping a Snake across upkeeps prevents additional Snakes until it is sacrificed. It does not independently make a creature every upkeep when an existing Snake remains.
3. To turn off Winter Orb or Static Orb for **our** untap, activate Opposition to tap the Orb *before our untap step*, e.g. at the end of the preceding opponent's turn. Tapping it after untap has begun does not retroactively free our permanents.
4. Opposition costs 2UU and can be difficult to cast while our own Contamination is active; colored artifact sources and Phyrexian Altar can help, but the candidate does not presume unrestricted mana.
5. Chalice of the Void, Trinisphere, Blood Moon, Back to Basics, Contamination and Necropotence still create meaningful self-lock and Breach/graveyard tensions. Sequence or remove locks as appropriate; no automatic deterministic win is claimed.
6. Karn's outside-the-game -2 is not counted as a normal Commander sideboard tutor; the static ability is its reason to stay.
7. Both partner commanders retain separate commander tax; the text's two [Commander] rows represent two cards in the 100.

## Source and validation status

- **Structural exact source audit:** 100 physical cards = two partner commanders plus 98 library cards, 100 distinct names, 26 lands, 0 companion, 5 adds/5 cuts. Every candidate name stays within Grixis color identity; no project exceptions. Blue noncommander Force-pitch source count remains 22, since Ashiok (blue) is replaced by Opposition (blue). Recorded Game Changers remain 22.
- **Oracle/legality:** 98 of these 100 names appear in the 2026-10-23 214-name Scryfall `Grixistax___October_2026_M7_Scryfall_20261023.json` archive attached to prior PR #675, with `commander_legality=legal` and identity within UBR. The two missing names are Ophiomancer (Scryfall MH3 #276, 2B, black) and Phyrexian Altar (Scryfall 2X2 #311, 3, colorless); their Oracle functionality was independently checked against Scryfall and the current official Wizards Commander banned list. Official October 12, 2026 B&R announcement has no Commander changes. There is no banned card in this 100.
- **Focused reproducible tests:** hash binding, exact source set delta, unique cards, 26 lands, protected engines and wheel package, singleton and partner commander text. These are structural tests, **not** automated gameplay/rules or live 100-card Scryfall pulls. No matched-hand games or tournament win rates were measured. The prior M6 I/J two-swap certificate **does not** certify this different five-swap proposal.

## Owner-review disposition

**PROPOSE Rev1 as a deliberate stax-parity redesign for Cory's approval.** No canonical replacement, merge into canonical `main`, tracker approval, or unlock is authorized by research alone. If accepted, require an exact-source canonical approval PR, canonical CI, post-merge hash and lock verification. If either disputed cut is rejected, return for a new exact Rev2 and preserve the old lock.

**Power Bracket:** 5 — fringe/rogue cEDH.

**Archidekt tags:** Grixis Stax / Thrull Sacrifice / Helm–Breach Combo.
