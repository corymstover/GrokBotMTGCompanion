#!/usr/bin/env python3
"""Generate "EDH Mulligans.md" (Bot cycle 6, #31): mulligan rules (CR 103.5 quoted from the cached CR), exact
hypergeometric opening-hand odds for 99-card libraries, opening-hand cards (CR 103.6) from Scryfall, plus labeled guidance.
Usage: python3 scripts/build_mulligans.py"""
import re
from math import comb
from edh_lib import Data
import ingest_scryfall as ing

CR = sorted((ing.ROOT / ".cache").glob("MagicCompRules-*.txt"))[-1]


def rule(n):
    for l in CR.read_text(encoding="utf-8", errors="replace").splitlines():
        if l.startswith(n + " "):
            return l[len(n) + 1:].strip()
    raise SystemExit(f"rule {n} not found")


def p_atleast(N, K, n, k):  # P(X >= k), X ~ Hypergeom(N, K, n)
    return sum(comb(K, i) * comb(N - K, n - i) for i in range(k, min(K, n) + 1)) / comb(N, n)


def p_between(N, K, n, lo, hi):
    return sum(comb(K, i) * comb(N - K, n - i) for i in range(lo, min(hi, K, n) + 1)) / comb(N, n)


def main():
    d = Data()
    L = d.header("EDH Mulligans", "scripts/build_mulligans.py", 31,
                 f"Rules are quoted from the cached Comprehensive Rules (`{CR.name}`). The odds are exact hypergeometric math for a 99-card library (one commander; with two commanders it's 98, and the numbers barely change).")
    L += ["## Rules (fact)", ""]
    for n in ("103.5.", "103.5c", "103.6.", "103.6a", "103.6b"):
        L += [f"> **CR {n.rstrip('.')}** — {rule(n)}", ""]
    L += ["**In practice (fact, from the rules above):** in a multiplayer Commander game your **first mulligan is free**. You draw a fresh 7 and bottom 0. The second mulligan bottoms 1, the third bottoms 2, and so on. Players decide in turn order, starting with the starting player, and then everyone who chose to mulligan does so at the same time (103.5).", "",
          "> **Note:** some tables play house rules, such as extra free mulligans or the older \"Partial Paris\" style. Those aren't in the CR, so agree on them in the pre-game talk.", ""]
    N, n = 99, 7
    L += ["## Opening-hand land odds (math)", "", f"P(the opening 7 has the given number of lands), drawn from {N} cards:", "",
          "| Lands in deck | 0–1 lands | 2 lands | 3–4 lands | 5+ lands | ≥ 2 lands | ≥ 3 lands |", "|---|---|---|---|---|---|---|"]
    for K in (33, 34, 35, 36, 37, 38, 40):
        f = lambda x: f"{x*100:.1f}%"
        L.append(f"| {K} | {f(p_between(N,K,n,0,1))} | {f(p_between(N,K,n,2,2))} | {f(p_between(N,K,n,3,4))} | {f(p_atleast(N,K,n,5))} | {f(p_atleast(N,K,n,2))} | {f(p_atleast(N,K,n,3))} |")
    L += ["", "## Odds of seeing a key piece (math)", "",
          "P(at least one copy of a card group, such as ramp, removal or your combo pieces), by group size and cards seen. 7 is the opening hand; 8, 10 and 12 are by your turns 1, 3 and 5 on the draw, drawing one card a turn with no other card draw.", "",
          "| Copies in deck | 7 cards | 8 cards | 10 cards | 12 cards |", "|---|---|---|---|---|"]
    for K in (1, 3, 5, 8, 10, 12, 15):
        L.append(f"| {K} | " + " | ".join(f"{p_atleast(N,K,s,1)*100:.1f}%" for s in (7, 8, 10, 12)) + " |")
    L += ["", "## Opening-hand cards (CR 103.6)", "",
          "Cards that act from your opening hand. They're Commander-legal and sorted by EDHREC rank. Pattern: `in your opening hand`.", ""]
    oh = d.find(r"in your opening hand", kind="any")
    L += d.table(oh, 25) + ["", f"{len(oh)} matches in total.", ""]
    L += ["## Keep or mulligan? (guidance)", "",
          "*Strategy opinion, not rules or fact. Adjust it to your deck and bracket.*", "",
          "**Usually keep:**",
          "- 3–4 lands plus at least one early play (ramp, card draw or interaction).",
          "- 2 lands plus 2+ cheap ramp pieces or cantrips, especially on the draw.",
          "- Any hand that executes your deck's plan by turn 3–4.", "",
          "**Usually mulligan (the first one is free):**",
          "- 0–1 lands, unless it's a cEDH hand with heavy fast mana and you've weighed the risk.",
          "- 6–7 lands with no card draw.",
          "- Hands where every spell costs 5 or more mana.",
          "- Hands missing the colors your spells need, with no fixing.", "",
          "**Mulligan to a plan:**",
          "- After the free mulligan, keep a functional 6 rather than chasing a perfect hand.",
          "- In competitive play (Bracket 5) you may mulligan more aggressively for fast mana, tutors or a protected win. See the [cEDH Primer](cEDH%20Primer.md).",
          "- Use the land odds above to set your deck's land count. The [EDH Mana Bases](EDH%20Mana%20Bases.md) guide recommends 36–38 lands plus about 10 ramp pieces for casual decks.", ""]
    A = [("Aristocrats", "aristocrats-sacrifice--death-triggers", "A sac outlet or a death-trigger payoff, plus fodder", "Turns 2–4: assemble an outlet, a payoff and fodder; keep a recursion piece in reserve"),
         ("Tokens / go-wide", "tokens--go-wide", "A token maker by turn 3 and ramp", "Build the board, then hold the anthem or overrun until it's lethal or close"),
         ("Spellslinger", "spellslinger-instants--sorceries", "Cheap cantrips or rituals plus a payoff, or the commander castable on time", "Get the engine (commander or payoff) down first; keep a counterspell up afterwards"),
         ("Lands / landfall", "lands-matter--landfall", "4+ lands or land-ramp; extra-land-drop effects", "Ramp every turn; get landfall payoffs down before fetches and extra drops"),
         ("+1/+1 counters", "11-counters", "2-drop counter creatures or a proliferate engine", "Curve out; get doublers (Hardened Scales effects) down before the payoffs"),
         ("Graveyard / reanimator", "graveyard-value--reanimator", "A self-mill or discard outlet plus a reanimation spell", "Fill the graveyard early; be wary of opposing graveyard hate before going all in"),
         ("Blink / flicker", "blink--flicker", "ETB creatures plus ramp to reach the blink engine", "Value ETBs first; land the repeatable blink engine when it can be protected"),
         ("Artifacts", "artifacts", "Mana rocks or cheap artifacts plus a payoff", "Use rocks to reach the payoffs fast; spread artifacts out in case of a board wipe"),
         ("Voltron / extra combats", "combat--voltron--extra-combats", "Protection plus equipment or auras, or a fast commander", "Commander out by turn 2–3; hold protection up instead of overcommitting auras"),
         ("Cascade & big spells", "cascade--big-spells", "Heavy ramp: 2+ ramp pieces or 4+ lands", "Ramp turns 1–3, then cast the cascade engine or the commander"),
         ("Group hug / slug", "group-hug--group-slug", "Lands and the commander castable on time", "Develop quietly; let the table spread its aggression around"),
         ("Life as a resource", "life-as-a-resource--lifedrain", "A lifegain or drain engine and cheap card advantage", "Get engines down early; pay life aggressively only when it's safe")]
    L += ["## Priorities by archetype (guidance)", "",
          "*Strategy opinion, not rules or fact.* Archetype names link to the [EDH Archetypes](EDH%20Archetypes.md) guides.", "",
          "| Archetype | Opening hand wants | Early-game priorities |", "|---|---|---|"]
    L += [f"| [{a}](EDH%20Archetypes.md#{anc}) | {w} | {e} |" for a, anc, w, e in A] + [""]
    (ing.ROOT / "EDH Mulligans.md").write_text("\n".join(L) + "\n")
    print("opening-hand cards", len(oh))


if __name__ == "__main__":
    main()
