# Cycle 114 — Inalla, The Rani, Nicol Bolas the Ravager: authored commander-first reviews

**Status:** source-bound strategic author review, NOT independently commissioned Pass C/I/J, complete multiplayer Phase B, current full-100-card legality certificate, all-candidates-zero-improvement proof, automatic swap or M6 milestone acceptance.

Preregistered first in `data/grixis/m6/phase_b_plans/cycle114_commander_reviews_01.json` (commit `8d7771487f0ffeb602a1912aa17d06ed14dfe76a`). The machine-verifiable authored judgments are in `data/grixis/m6/author_reviews/cycle114_three_commander_reviews_01.json`. CI will create a reproducible card-identity and Oracle receipt `data/grixis/m6/phase_b_bounded/cycle114_sourced_review_validation_01.json`.

## Inalla, Archmage Ritualist: Pitiless Plunderer for Blood Pet — HOLD

**Approved SHA-256:** `81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3`. **Exact M5 hypothesis:** `swap:inalla-archmage-ritualist:m5:217e55a1ecd0`.

Inalla's commander-defining Eminence works from the command zone or battlefield and copies **another nontoken Wizard** after an optional {1} payment. Her compact cEDH plan revolves around Spellseeker, Scholar of the Ages, Bloodline Necromancer, Ruthless Technomancer and reanimation/sacrifice rituals; the opponent-life tap mode is a possible mana-loop outlet.

Pitiless Plunderer, a **non-Wizard Human Pirate**, costs {3}{B} and creates a Treasure whenever another creature *you control* dies. It can support a token-death economy only after it is cast and other creatures die; it cannot be duplicated by Inalla's Eminence. Blood Pet, another non-Wizard, costs {B} and sacrifices itself for immediate {B}, preserving early ritual mana and creature sacrifice/graveyard access. The two cards have very different timing. The M5 mana/test-pass annotation proves neither an accessible commander-specific infinite line nor improved early cEDH speed.

**Decision:** retain Blood Pet for this exact candidate. If Plunderer is reconsidered, verify whether a Bloodline/Technomancer loop yields additional *useful* Treasure mana and wins measurably earlier, then compare it against a different truly weak noncore card.

## The Rani: Drafna, Founder of Lat-Nam for Curse of Opulence — HOLD

**Approved SHA-256:** `7220937ed5817b4ef9cacd2463a3434b98ae58690ffa1d7ef440881ba97d729c`. **Exact M5 hypothesis:** `swap:the-rani:m5:225ed1a7c9c4`.

The Rani marks and goads creatures on entering/attacking; goaded attackers that damage the controller's opponents create Clues through investigate. Academy Manufactor and Erdwal Illuminator multiply those Clues. Forced combat and Clue value—not generic artifact combo loops—define the deck.

Drafna has an ability for {1}{U} to return a controlled artifact to hand, and a {3}, {T} ability that copies an **artifact spell on the stack**, not an artifact token or Clue already on the battlefield. An artifact spell copy that resolves into a token is not automatically a token-creation event for token-created triggers. Returning a Clue token to hand makes it cease existing and does not provide a reusable Clue spell.

Curse of Opulence is a one-red-mana Aura Curse that creates **Gold** when the enchanted player is attacked, also rewarding other opponents attacking that player. It does not itself goad, nor do Gold tokens count as investigating, but it incentivizes the forced-combat economy in a way Drafna does not automatically replace. Its role should not be misrepresented as mere generic Treasure generation.

**Decision:** retain Curse of Opulence for this exact cut. Drafna warrants testing only if a complete legal artifact-spell-copy engine uses existing card slots and mana efficiently, preserving Clue and goad synergies.

## Nicol Bolas, the Ravager: Aetheric Amplifier for Mox Diamond — addition promising, proposed cut HOLD

**Approved SHA-256:** `5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e`. **Exact M5 hypothesis:** `swap:nicol-bolas-the-ravager:m5:14aef623f1e4`.

The approved deck is distinctively Bolas **superfriends**: Ravager's ETB discard, expensive sorcery-speed flip to Arisen planeswalker, loyalty activation/copy/proliferate with The Chain Veil, Ichormoon Gauntlet, Rings of Brighthearth, Deepglow Skate and Bolas planeswalkers.

Aetheric Amplifier has a real specialized payoff: as a three-mana artifact, it taps for colored mana; for an additional {4}, {T} at sorcery speed, it can **double all counter quantities on a target permanent**, including Arisen's loyalty counters. This accelerates the -12 ultimate and repeated loyalty plans once Arisen is already transformed and Amplifier can activate. It **does not** grant another legal loyalty activation, put an initial counter on a zero-counter permanent, or supply a zero-mana turn-one accelerant.

Mox Diamond can enter for {0} if its controller discards a land as it would enter; it can then tap for mana of any color. That early colored acceleration matters to cast Ravager, assemble protection and later activate the expensive flip. Replacing it with a costlier permanent that needs a separate four mana to double counters has serious tempo risk, even if the late-game ceiling is higher.

**Decision:** Aetheric Amplifier is **commander-identity positive but unproven**. Do not sacrifice Mox Diamond for it on current evidence. Assess real transform timing and extra planeswalker loyalty value; find an alternative lower-impact cut, then obtain independent strategic criticism and, if justified, owner approval.

Official primary external corroboration: <https://magic.wizards.com/en/news/feature/aetherdrift-release-notes> explains Aetheric Amplifier counter-doubling; card-specific Oracle/rulings are checked separately by archived Scryfall in the workflow. Current-day full-list legality must be independently validated prior to a final deck approval.

## Original state and unfinished M6

All three current approved main libraries and commander slots remain unchanged. Archived snapshot Oracle and listed cut/add presence/source list SHA are part of CI, not a current legality audit of every full deck card. The M5 exploratory candidate flags, even when source-agreed, do not equate to strategic optimization. This batch adds three meaningful candidate-specific author judgments but does **not** close out all possible candidates for any commander.

**Next research priority:** bounded verification of meaningful Aetheric Amplifier loyalty improvement against several genuinely weaker candidate cuts; independent Pass C review of the six Cycle112/113 and Cycle114 assessments; broader 62-commander coverage rather than excessive ad hoc simulator expansion.
