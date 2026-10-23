# Lynde__Cheerful_Tormentor (Lynde, Cheerful Tormentor) — M7 red-team memo (2026-10-23)

1. **Seal blocker (stated first).**
   - The existing Pass C Stage A seal (`seal.json`, commit `c4c5fa5d`) records `stage_a.md` SHA-256 `59f2dc10…4829c12e`.
   - The committed file (commit `b4c98568`, blob `b253ed9c`, unchanged since) hashes to `02adfb85db19aa42d5dfe36b96906874ea1abd232b6f8bfc3861c1108035b72a`.
   - Exact cause: the sealed value is the SHA-256 of the file without its final byte. The committed file is 13276 bytes and ends `.\n\n`; the seal was computed over the text with one trailing newline. The seal's own `git_blob_sha` matches the committed bytes, so the seal record is internally inconsistent.
   - The shared checker therefore rejects the bundle. This PR does not edit the seal, the Stage A files or the checker; the owner must decide on a re-seal or a documented hash-correction exception.
2. **Commander text: attack this first.**
   - Lynde returns a Curse to you only at the next end step, and only if the card is still in your graveyard (CR 603.7c). Exile in response leaves nothing to return.
   - Token Curses (from Court or Replication) cease to exist in the graveyard (CR 704.5d), so Lynde never returns them. Each token is a one-shot Curse for one move.
   - The upkeep move does not target, so hexproof players can receive it.
3. **Court of Vantress over Cruel Reality (swap 1).**
   - Court as monarch copies a Curse each upkeep; the token Aura enters attached to the player you choose (CR 303.4f). Ordered above Lynde (CR 503.1a), you put it on yourself and Lynde moves one for two cards.
   - Risk: lose the monarchy to combat damage and Court only becomes a copy of something; Court is four mana with no immediate board effect except the monarch draw.
   - Cruel Reality returned to you still makes you sacrifice at your upkeep even after Lynde moves it (the trigger already named you). Grid B1: Lynde is lost in 42/96 cells.
   - Cost: Cruel Reality is the deck's strongest table lock and is more popular on EDHREC.
4. **Extravagant Replication over Curse of Death's Hold (swap 2).**
   - Unconditional upkeep copy of any nonland permanent you control: a Curse, Paradox Haze or a creature engine. Six mana, nothing the turn it lands.
   - Curse of Death's Hold returned to you shrinks your own creatures until your upkeep; Nightscape Familiar and any X/1 die (CR 704.5f). Grid B1: 32/96 cells.
   - Cost: loses the anti-token lock; more popular on EDHREC.
5. **Pass C items (bounded).**
   - 1/2/3 self-Curse stacks, Braids and Accursed Witch return timing, extra upkeeps: grids B1–B3 and the 12 rules cases in B2.
   - Curse of Chaos over Curse of Echoes: rejected (owner removed Curse of Chaos; Echoes is an owner add).
   - Strionic Resonator and Beseech the Mirror: rejected (owner rejected both on 2026-10-14).
6. **Combo / bracket.**
   - Spellbook included combos 0 → 0. Almost-included 17 → 22. No infinite is claimed for any add.
   - Game Changers 8 → 8. Bracket 4.
7. **Owner direction.**
   - No owner keep or owner add is cut, so no override is flagged.
   - No removed card or rejected class is re-added (Curse of Chaos, Strionic Resonator and Beseech the Mirror stay compare-only).
8. **Non-independence.** The Pass C reviewer (alias Josh-Lee-Kwai) is `technically_independent=false` under `OWNER_WAIVED_FOR_FORMAL_PASS_C`.
