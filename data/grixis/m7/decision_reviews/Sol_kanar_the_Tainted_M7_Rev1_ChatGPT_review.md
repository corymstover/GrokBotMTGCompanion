# Deck #53 — Sol'Kanar the Tainted — M7 Rev1 exact owner review (2026-10-27)

**STATUS:** engineering review only; canonical Oct15 owner-approved/locked SHA `72a3b14e93d884d98397e000fe45df430beb538a106097a69dfc2491da8d7a58` remains untouched until Cory approves the new exact list.

- Candidate: `data/grixis/m7/candidate_lists/Sol_kanar_the_Tainted_M7_Rev1.txt`
- Proposed raw 100-card SHA-256: `c244b7c3e31b108a0730db37790de14dd167c9ee274259b3f18bbb5971a1ef20`.
- 100 physical / 93 distinct names / 35 lands / Island×3, Mountain×3, Swamp×4 only repeats, UBR, one commander and no companion.
- Natural ceiling: **Power Bracket 4 — Optimized**; tags **Donate / Blink / Giftable Curses**.

## Commander-first strategy and six actual upgrades

Sol'Kanar chooses one previously unchosen mode per battlefield object at **its controller's own end step**. It is not a fixed-order saga. End-step Thassa/Closet, instant Planar Incision and newly-added Displacer Kitten create a new object and reset the memory, while Homeward Path, Coveted Falcon, Planar Incision and Brand recover the **owned** commander when an opponent receives it. Pact, Coil, Illusions, Archfiend, Gambit, Plague Reaver and Audience stay as actual hazardous gifts. The strongest native finishes are Demonic Pact + permanent transfer after extracting safe modes and Immortal Coil + transfer + target-recipient graveyard exile.

| CUT | ADD | Real strategic gain and downside |
|---|---|---|
| Assault Suit | **Displacer Kitten** | Cast-triggered nonland blink enables multiple commander resets and ETB reuses. Kitten only blinks permanents **we control**; it cannot directly retrieve a stolen Sol and is removable. Suit's temporary opponent transfer does not reset the four chosen modes and requires high equip mana. |
| Perplexing Chimera | **Nightscape Familiar** | Earlier 2MV Zombie discounts Sol'Kanar's generic component and red/blue donor interaction. Critically: this is **one generic reduction** for a spell that is both red and blue, not two. Lose a quirky five-mana reactive spell exchange. |
| Reins of Power | **Brand** | One-red instant recovers all **owned permanents** including Sol after mode four; cycling {2} when inapplicable. It also reclaims dangerous **gifted** Pact/Coil, so using it indiscriminately can lose the game. Lose Reins's surprise temporary combat takeover. |
| Visions of Duplicity | **Alexios, Deimos of Kosmos** | Automatically transfers at every player's upkeep, grows, attacks and cannot be sacrificed or attack its owner; proactive opponent-against-opponent pressure. The creature can still threaten our planeswalkers and be removed. Lose a political opponent-opponent creature exchange with flashback. |
| The Trickster-God's Heist | **Sleeper Agent** | One-black immediate liability requiring no separate Donate: controller takes 2 at their upkeep. Cheap enough to pair with control and tutors. It gives an opponent a real 3/3 and is fragile; lose a slow but flexible two-step Saga exchange. |
| Propaganda | **Wishclaw Talisman** | Two-mana access to missing Pact, Offering, Coil or rescue, then the artifact passes to an opponent after tutoring. That opponent can tutor too; losing Propaganda's attack tax makes dedicated combat defense weaker. |

**Full 99-slot audit:** 93 KEEP/CUT-copy review from Oct20 M6, expanded to 99 individual physical lines in the companion CSV; **93 KEEP / 6 CUT**. All six material selected roles differ (repeatable mode reset, cheaper commander cast, owner recovery, self-transferring combat, direct curse creature, pact-finding tutor). There is no generic combo-shell conversion. We reviewed 15 material named candidates, challenged 11 incumbent roles, including the two additional post-floor checks below.

## What did not make the cut and why

- **Ghostly Flicker for Ertai Resurrected:** adds one-shot bounce of Sol plus a second artifact/land/creature. However Ertai's flash ETB answers *triggered abilities* as well as spells, vital to dangerous fourth-mode or Pact windows. Keep Ertai.
- **Jinxed Ring for Goblin Bombardment:** a cheap giftable death trigger, but free Bombardment sacrifices our controlled Sol **before** an unacceptable mode resolves, retaining a key pressure valve.
- **Goldnight Castigator for Kain:** doubles incoming damage to **us** until transferred; redundant fragile waiting period compared with Kain's built-in on-combat transfer.
- **Modify Memory / Order of Succession for Puca's Mischief:** one-shot exchange cannot replace ongoing nonland permanent swaps, including Pact and Coil.
- **Ebon Drake / Rust Elemental:** conditional liability and 3–4MV setup, weaker than immediate Sleeper Agent and proven existing curses against interactive or low-artifact pods.
- **Abyssal Persecutor:** can prevent a donated recipient from losing when Pact/Coil is trying to close, requiring further removal.
- **An Offer You Can't Refuse:** excellent one-mana protection but no replacement for Ertai's triggered-ability counter; two Treasure conceded can help remove our curse.
- **Generic cEDH Thoracle/Breach:** homogenizes away the four-mode gift identity.

The source-bound larger **eight-swap** variant adds Ghostly Flicker and Jinxed Ring by sacrificing Ertai and Goblin Bombardment. We physically staged and hashed all 100. This trades away distinct mandatory defensive roles for already represented effects, and so was rejected. A separate six-swap variant retains Propaganda but cuts Kain; chosen list keeps Kain's distinctive combat exchange at the expense of the nonwinning pillowfort tax. **Six is a quality result, neither a research cap nor padded to a quota.**

## Oracle/rules and test scope

The original all-93 Oct15 approved source and Oct20 Scryfall /collection Grok advisory were read as archive evidence; they are not automatically a same-day October27 certification. The exact-candidate Python verifier runs all-name current Scryfall Oracle identity, Commander legality and UBR checks in two batched requests in GitHub Actions. The 17 finite tests exercise the blueprint's C1, K1–K6, E1–E2, W1–W3, F1–F3 and three added-card interactions with normal/adversarial traces; these are deterministic constrained assertions **not** a full Magic rules engine or win-rate simulation. The M7 schema/source/99-slot/post-floor structural gate and exact-head GitHub workflow are also required.

**Historical I/J distinction:** `data/grixis/m6/ij/input_receipts/solkanar-the-tainted.json` attests M5/M6 input bytes with `phase_b_replayed=false` and `inputs_attested_downstream_incomplete`. We have checked the *candidate-specific* mechanics and the originally protected blueprint cases; this is not a reconstructed sealed I/J test, a historical M6.10 certification, Grok independence or aggregate milestone acceptance. Those older gaps remain accurately recorded.

## Owner authority

Review PR only. Do not merge or change canonical files, tracker or state until Cory explicitly approves exact new hash. On approval, run approved-exact-head and postmerge canonical readback; preserve Oct15 file and evidence.
