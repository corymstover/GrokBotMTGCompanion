# Josh-Lee-Kwai formal Pass C — Final owner-equivalent review #53: Sol'Kanar the Tainted

**Final disposition: `NEEDS TESTING`** — preserve exact owner-approved `APPROVED/LOCKED` deck, no card changes. Bracket 4 Optimized and Archidekt identity **Donate / Blink / Giftable Curses** retained. This is a staged third *review* formally accepted under the owner's `FORMAL_PASS_C_OWNER_EQUIVALENT` independence waiver **only upon CI/merge**, NOT execution by an actual independent third model. Josh-Lee-Kwai alias is ChatGPT/OpenAI GPT-6 with prior project exposure disclosed. No measured wins, current full-card Oracle sweep, Phase B certificate, I/J, M6/M7 acceptance or M8 export claimed.

## Exact evidence receipts

| Field | Source |
|---|---|
| Deck/track order | `Sol_kanar_the_Tainted`, tracker index52, #53/62 |
| Canonical approved authority | `corymstover/grixis-commander-encyclopediaGPT@main/state/current_deck_overrides.json`, `APPROVED` and `LOCKED` |
| Canonical list | `refinement/decklists/Solkanar_the_Tainted_Approved_2026-10-15.txt`, Git blob `7ba29f9e4a855a446914566e29d2a67e93840ba0` |
| Independently computed raw TXT SHA-256 (exactly matches owner's approved hash) | **`72a3b14e93d884d98397e000fe45df430beb538a106097a69dfc2491da8d7a58`** |
| Structural | **100 physical; 93 names; 35 physical land cards; 3x Island, 3x Mountain, 4x Swamp** only repeats; one commander, no companion, UBR identity, zero project-specific legality exception |
| First Stage A MD commit | `2d261db41ed13031c87de404504023cb717d3016` |
| First complete Stage A MD+JSON commit | **`7e92e3f7922d59e1d98565b93aa998a896e7550b`** |
| Neutral Stage A Markdown SHA-256 / blob | `b354ef1248dc80bf4a52985f6032e7dd54e005294d9cbff3c78445c81508cf38` / `c8539dad0407a16a1a2875afc9daf80d0ecb9be9` |
| Neutral Stage A JSON SHA-256 / blob | `7fcc5637ee8958d2be641516c1ed8f5f9d22910dcdf9f95becdc2ab12dc53e0b` / `a4df41d77f9ef317bd68a0815f59d5656d771224` |
| **Separate cryptographic seal commit before historical unblinding** | **`7b04ed181916062da6f2bd0a4ea6962e474a5044`** |
| Controlled Stage B | `data/grixis/m6/owner_pass_c_substitute/Sol_kanar_the_Tainted/stage_b_reconciliation.md` |
| Historical authored full-review KEEP (opened after seal) | `data/grixis/m6/deep_reviews/Sol_kanar_the_Tainted.md`, blob `125dfc8821c03f26629224b933c0c8951c6df0d8` |
| Historical GrokBot advisory KEEP (opened after seal) | `data/grixis/m6/grokbot_pass_c_advisory/Sol_kanar_the_Tainted.md`, blob `e913e051a1ea0a9aca7571327075c7e8f27aeef7` |
| Historical 62/62 reconciliation | `two_model_reconciliation/KEEP_AGREEMENT_REGISTER_2026-10-20.md`, blob `9fa0d74d7426c4d1cd0dc6b5c7f0f9b4f1ffbf6a`; agreement **KEEP/KEEP documentary only** |

## Commander-first disposition

Sol'Kanar is a **five-mana four-mode END-STEP control-transfer commander**: draw one; opponents each lose 2/gain2; deal3 to another creature/planeswalker; exile/return under an opponent's control. Its fourth option is not a free fourth value mode: the newly entered opponent-controlled commander can then use its own three useful modes on its turns. The deck lives on carefully timing blink resets and the donation of **real downside permanents** (Demonic Pact, Greed's Gambit, Immortal Coil, Illusions of Grandeur, Archfiend of the Dross, other political liabilities), then policing who owns/controls them when liability resolves. Generic combo upgrades must not strip this of its strange theft-and-curses character.

**New, conditional Pass C challenge:** `ADD Displacer Kitten / CUT Conjurer's Closet`. The blue four-mana Kitten uses noncreature SPELL CAST triggers to blink our nonland permanents as new objects, opening faster or repeated Sol-mode and `Demonic Pact` resets and reusing owned ETB creatures. The original author did not explicitly screen Kitten in its comprehensive report, and GrokBot/ledger do not mention it. The card is technically compatible with UBR and currently not on the official ban list, but **compatibility is not superiority**.

**The strongest reason to KEEP the incumbent:** five-mana Closet triggers on our end step even when we have **no spells** to cast, letting the pilot reset Sol and capture a temporarily controlled **opponent-owned creature** indefinitely because Closet returns it under **our control**. Kitten's blink returns the card under its **owner's control** and may surrender the very creature we stole. Kitten can be killed as a 2/2 before any suitable cast and cannot trigger simply because a modal commander ability triggers; a crucial fourth-mode emergency in our end step specifically requires a legal instant/flash noncreature cast. We already possess `Thassa, Deep-Dwelling` for unconditional controller-return blinking, but removing the second repeatable blink reduces resilience and theft capture access. This is an unusually important owner-vs-controller distinction, requiring experimental case accounting rather than ranking the cheaper card automatically.

**Alternate cut search:** `Planar Incision` is one-shot, immediate blink/creature rescue and can retrieve our commander even when controlled by an opponent; it would trade reactive certainty for prospective Kitten chaining. `Perplexing Chimera` is a conditional 5MV political exchange engine that GrokBot listed as weak, but still provides a different opponent-cast interception/ownership challenge. `Spiteful Banditry` is NOT the easy cut: earlier author explicitly preserved its damage-to-creatures and once-turn Treasure leverage under combat pressure despite a biased ramp-only simulation comparing Fellwar Stone. `Assault Suit` has substantial equip cost but offers the distinctive donated-creature, no-sacrifice route. Do not force any exact swap into approved list without evidence.

## Key rules and counterplay

- The end-step mode is chosen when the original triggered ability is put on stack and its used-mode history belongs to that object; exiling and returning creates a **new object**. If Closet/Thassa blink the commander while an old fourth-mode trigger waits below them, the new Sol is not the old source to be exiled and given away. However, opponents can remove the blink target before the blink resolves or prevent the engine from surviving.
- Kitten's triggered nonland blink is **cast-based**, not activated or copied; if an appropriate spell is cast and trigger already put on stack, killing Kitten does not by itself counter that trigger. Removing the targeted Sol before resolution does. Returning other-owner permanents under owner control is not the same as Closet's return under our control.
- `Demonic Pact` remembers modes that were chosen even if the trigger is countered, and the lose-game mode eventually becomes mandatory unless it's removed, blinked, or donated in time. `Greed's Gambit` has **end-step**, not upkeep, liability; the old source-time wording error had already been corrected in original M6 and is not new Pass C discovery. Its leave-battlefield cost and controller determine actual risk.
- `Immortal Coil` no-cards-in-controller's-graveyard loss is a real state-triggered risk but must be evaluated with ability timing, opponent graveyard stock, interaction and handoff, not treated as unconditional victory on donation. `Homeward Path` only changes creatures and may undo stolen opponent creatures while recovering owned Sol.
- `Fierce Guardianship`/`Deflecting Swat` cost-free conditions depend on controlling the commander; counterspells can stop donation and blink assembly. A removal-heavy table, graveyard-hate, a destroyed blink engine and hard-to-cast {U}{B}{R} are real failure states in this 35-land suite.

**Primary current authoritative references:** [Dominaria United release notes (Sol'Kanar)](https://magic.wizards.com/en/news/feature/dominaria-united-release-notes-2022-08-26), [Commander Legends Baldur's Gate release notes (Displacer Kitten)](https://magic.wizards.com/en/news/feature/commander-legends-battle-baldurs-gate-release-notes-2022-06-01), [Innistrad Remastered release notes (Conjurer's Closet)](https://magic.wizards.com/en/news/feature/innistrad-remastered-release-notes), [Foundations release notes (Demonic Pact)](https://magic.wizards.com/en/news/feature/foundations-release-notes), [current Commander ban list](https://magic.wizards.com/en/banned-restricted-list). Historical owner whole-list gate and GrokBot October20 Scryfall legal collection remain documentary evidence; a NEW full-93-name current Oracle/legality recertification was NOT executed.

## Exact post-JLK test queue and owner boundary

**Targeted comparison** under the owner's risk-based Phase B, not another universal research sweep:

1. Source-correct copy-only hashes / 100-card, UBR, singleton checks for approved baseline and **+Displacer Kitten/-Conjurer's Closet**, then role-specific **-Planar Incision** or **-Perplexing Chimera** alternatives if context justifies; record future official legality/Oracle at actual test date. Original approved 100 untouched.
2. Source-paid T4 Kitten and T5 Closet lines including actual UBR Sol access, colored rocks, tapped lands, noncreature spell available or unavailable, Kitten surviving to cast trigger, opposing interrupt on spell/Kitten/target, and commander modes used before end step.
3. **Critical ownership case:** creature borrowed via `Reins of Power` or other time-limited transfer; Closet/Thassa return under OUR control versus Kitten owner-return. Include `Homeward Path`, a stolen native creature and opponent removal. Track who controls gifts and who suffers Pact/Gambit/Coil next upkeep or end step.
4. Existing documentary clean KEEP remains supported until this concrete challenger shows net commander-first improvement. A sourced KEEP is an acceptable final outcome. If actual superior swap emerges, Cory decides on the exact add/cut in M7 after re-count/rules/legal/full 100 checks. Do not auto-approve based on a plausible trace.

**Final:** `NEEDS TESTING` for the new Kitten/Closet tradeoff; old two-model KEEP/KEEP documentary agreement is not retroactively invalidated. Qualified **formal owner-equivalent Pass C** only after exact-head evidence CI/merge and separate correct ledger merge; actual technical independence = false, separate independent reviewer count 0, canonical mutations 0, Phase B completed 0, M6/I/J 0, M7/M8 unaccepted. Advance next to tracker #54 `Tetsuo_Umezawa` only on verified ledger completion.
