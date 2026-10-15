#!/usr/bin/env python3
"""Bracket calibration & pilot notes for every deck (Bot cycle 19, issue #68).

For each deck in decks/ and grixis/decks/ this writes a "Bracket calibration & pilot notes" block
(between CALIBRATION markers, right after the Bracket assessment section) and refreshes the stale
"Two-card infinite combos: not machine-checked" bullet in the core decks' Bracket assessment. It also
writes "EDH Bracket Calibration.md" (all decks in one table) and data/deck_calibration.json.
Facts (Scryfall Oracle bulk, Game Changer flags, the deck's Commander Spellbook block, hypergeometric odds)
are kept apart from **guidance** (pilot tips, which cuts lower the bracket), which is labeled as such.
Barometers follow EDH Standards → Power bracket assessment (official Commander Brackets, Oct 2025 update).
Usage: python3 scripts/deck_calibration.py [--check]
"""
import json
import re
import sys
from collections import Counter
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402
import evaluate_decklist as ev  # noqa: E402
import front_matter as fm  # noqa: E402

ROOT = ing.ROOT
DECK_DIRS = ["decks", "grixis/decks"]
START, END = "<!-- CALIBRATION:START -->", "<!-- CALIBRATION:END -->"
PAGE = ROOT / "EDH Bracket Calibration.md"
OUT = ROOT / "data" / "deck_calibration.json"
I = "https://github.com/corymstover/GrokBotMTGCompanion/issues/"
RX = {
    "ramp": re.compile(r"\{T\}[^.\n]*: Add|\bAdd \{|search your library for [^.\n]*land cards?[^.\n]*onto the battlefield|Treasure token", re.I),
    "draw": re.compile(r"\bdraws? (a|one|two|three|four|five|six|seven|X|that many) cards?\b|\bdraw cards equal\b", re.I),
    "counter": re.compile(r"\bcounter target\b", re.I),
    "removal": re.compile(r"\b(destroy|exile) (another |up to \w+ )?target\b|\bdeals? (\d+|X) damage to (any target|target creature)|\btarget (creature|player)[^.\n]*sacrifices?\b", re.I),
    "wipe": re.compile(r"\b(destroy|exile) all\b|\beach (creature|nonland permanent)\b[^.\n]*(destroy|exile|damage|-\d+/-\d+)|\breturn all (nonland|creatures?)\b", re.I),
    "protection": re.compile(r"\b(gains?|have|has) (hexproof|indestructible|shroud|protection)\b|\bphase out\b|\bcounter target spell or ability\b", re.I),
    "tutor": re.compile(r"search your library for (a|an|up to (one|two|three)) (?![^.\n]*\bland\b)[^.\n]*cards?", re.I),
}
ROLE_LABEL = {"ramp": "ramp", "draw": "card draw", "removal": "spot removal", "wipe": "board wipes", "counter": "counterspells", "protection": "protection", "tutor": "tutors"}


def text_of(c):
    return (c.get("oracle_text") or "\n".join(f.get("oracle_text", "") for f in c.get("card_faces") or []))


def front_type(c):
    return (c.get("card_faces") or [c])[0].get("type_line") or c.get("type_line", "")


def is_land(c):
    return "Land" in front_type(c).split("—")[0]


def deck_list(p):
    m = re.search(r"## Decklist[^\n]*\n.*?```[^\n]*\n(.*?)```", p.read_text(encoding="utf-8"), re.S)
    return m.group(1) if m else ""


def combos_of(body):
    """Complete combos from the deck's own Commander Spellbook block (cards, produces, link)."""
    blk = body.split("## Combos (Commander Spellbook)", 1)
    out = []
    if len(blk) < 2:
        return out
    for line in blk[1].splitlines():
        m = re.match(r"^\| (.+?) \| (.+?) \| (.+?) \| \[([^\]]+)\]\((https://commanderspellbook\.com/combo/[^)]+)\) \|$", line)
        if not m:
            continue
        cards = re.sub(r"^⚠️ \*\*two-card infinite\*\* · ", "", m.group(1)).split(" + ")
        out.append({"cards": cards, "produces": m.group(2), "requires": m.group(3), "id": m.group(4), "url": m.group(5),
                    "infinite": "infinite" in m.group(2).lower()})
    return out


def hyper_at_least(k, K, N=99, n=7):
    return sum(comb(K, i) * comb(N - K, n - i) for i in range(k, min(K, n) + 1)) / comb(N, n)


def hyper_between(lo, hi, K, N=99, n=7):
    return sum(comb(K, i) * comb(N - K, n - i) for i in range(lo, min(hi, K, n) + 1)) / comb(N, n)


def rel(from_p, to):
    return "../" * (len(from_p.relative_to(ROOT).parts) - 1) + to.replace(" ", "%20").replace("&", "%26").replace(",", "%2C")


def analyse(p, R):
    text = p.read_text(encoding="utf-8")
    body = fm.body_of(text)
    res = ev.check(deck_list(p), R)
    rows = [r for r in res["cards"] if r["zone"] != "companion"]
    cards = {r["name"]: R.by_oid[r["oracle_id"]] for r in rows}
    cmdrs = [r["name"] for r in rows if r["zone"] == "commander"]
    main = [r for r in rows if r["zone"] == "main"]
    lands = sum(r["qty"] for r in main if is_land(cards[r["name"]]))
    nonland = [r for r in main if not is_land(cards[r["name"]])]
    avg = sum(cards[r["name"]].get("cmc", 0) for r in nonland) / max(1, len(nonland))
    roles = {k: [] for k in RX}
    for r in nonland + [r for r in rows if r["zone"] == "commander"]:
        t = text_of(cards[r["name"]])
        for k, rx in RX.items():
            if rx.search(t):
                roles[k].append(r["name"])
    combos = combos_of(body)
    two = [c for c in combos if c["infinite"] and len(c["cards"]) == 2]
    gcs = [r["name"] for r in rows if r["gc"]]
    mld = [r["name"] for r in rows if r["mld"]]
    xt = [r["name"] for r in rows if r["xturn"]]
    gc_floor = 4 if len(gcs) > 3 else 3 if gcs else 2
    floor = max(gc_floor, 4 if mld else 2, 3 if two else 2)
    setby = []
    if len(gcs) > 3:
        setby.append(f"{len(gcs)} Game Changers (more than three → Bracket 4)")
    elif gcs:
        setby.append(f"{len(gcs)} Game Changer{'s' if len(gcs) > 1 else ''} (one to three → Bracket 3)")
    if mld:
        setby.append("mass land denial (Brackets 1–3 allow none → Bracket 4)")
    if two:
        setby.append(f"{len(two)} two-card infinite combo{'s' if len(two) > 1 else ''} (none in Brackets 1–2 → at least Bracket 3)")
    if not setby:
        setby.append("no Game Changers, mass land denial or two-card infinites (Bracket 2 floor; Bracket 1 is a matter of intent)")
    tgt = re.search(r"Source's stated target \(guidance\): \*\*Bracket (\d)", body)
    edhrec = re.search(r"bracket distribution reported by EDHREC: (B1: [\d,]+, B2: [\d,]+, B3: [\d,]+, B4: [\d,]+, B5: [\d,]+)", body)
    dist = None
    if edhrec:
        dist = {int(k[1]): int(v.replace(",", "")) for k, v in re.findall(r"(B\d): ([\d,]+)", edhrec.group(1))}
    meta = fm.deck_fields(p, body)
    return {"path": str(p.relative_to(ROOT)), "title": meta["title"], "kind": meta["kind"], "commanders": cmdrs,
            "identity": meta["color_identity"], "floor": floor, "set_by": setby, "gcs": gcs, "mld": mld, "extra_turns": xt,
            "combos": combos, "two": two, "lands": lands, "avg_mv": round(avg, 2), "roles": roles,
            "target": int(tgt.group(1)) if tgt else None, "edhrec": dist, "body": body, "text": text,
            "one_card_away": (re.search(r"(\d+) more are one card away", body) or [None, None])[1]}


def cut_set(two, cmdrs):
    """Greedy minimal set of cards whose removal breaks every two-card infinite (never the commander)."""
    left = [set(c["cards"]) for c in two]
    cuts = []
    while left:
        cnt = Counter(x for s in left for x in s if x not in cmdrs)
        if not cnt:
            break
        best = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[0][0]
        cuts.append(best)
        left = [s for s in left if best not in s]
    return cuts


def block(a, p):
    std = rel(p, "EDH Standards.md") + "#power-bracket-assessment"
    L = [START, "## Bracket calibration & pilot notes", "",
         f"> Generated by `scripts/deck_calibration.py` (Bot cycle 19, [#68]({I}68)). **Facts:** Scryfall Oracle bulk and Game Changer flags, this page's Commander Spellbook block, exact hypergeometric odds. "
         f"**Guidance** lines are strategy opinion and are labeled. Barometers: [EDH Standards → Power bracket assessment]({std}). Brackets are a pregame-conversation tool, not a hard rule.", "",
         "### Floor rationale", "", "| Barometer | In this list | Effect on the floor |", "|---|---|---|"]
    g = a["gcs"]
    L.append(f"| Game Changers | {len(g)}{': ' + ', '.join(g) if g else ''} | " + ("Bracket 4 (more than three)" if len(g) > 3 else "Bracket 3 (one to three)" if g else "none (Bracket 1–2 allow 0)") + " |")
    L.append(f"| Mass land denial | {', '.join(a['mld']) or 'none'} | " + ("Bracket 4 (none allowed in 1–3)" if a["mld"] else "—") + " |")
    L.append(f"| Extra-turn cards | {', '.join(a['extra_turns']) or 'none'} | " + ("informational: Bracket 1 has none; Brackets 2–3 only in low quantity, not chained" if a["extra_turns"] else "—") + " |")
    tw = "; ".join(f"[{' + '.join(c['cards'])}]({c['url']})" for c in a["two"])
    L.append(f"| Two-card infinite combos (Spellbook) | {len(a['two'])}{': ' + tw if tw else ''} | " + ("at least Bracket 3 (none in 1–2); *early-game* or not (3 vs 4) is opinion" if a["two"] else "—") + " |")
    tu = a["roles"]["tutor"]
    L.append(f"| Tutors (non-land) | {len(tu)}{': ' + ', '.join(tu[:8]) + (' …' if len(tu) > 8 else '') if tu else ''} | informational: the Oct 2025 update removed tutor limits (efficient tutors are Game Changers) |")
    L += ["", f"**Calibrated floor: Bracket {a['floor']}** — set by {'; '.join(a['set_by'])}.", ""]
    ctx = []
    if a["target"]:
        ok = a["target"] >= a["floor"]
        ctx.append(f"- Source's stated target (guidance): Bracket {a['target']} — " + ("consistent with the floor." if ok else f"⚠️ **below the floor** (Bracket {a['floor']}): the list as written cannot be played at its stated target without the cuts below."))
        if a["target"] == 5:
            ctx.append("- Bracket 5 means built for the cEDH metagame; that is intent and meta fit, which the list alone cannot show (opinion). See [cEDH Primer](" + rel(p, "cEDH Primer.md") + ").")
    if a["edhrec"]:
        tot = sum(a["edhrec"].values())
        mode = max(a["edhrec"], key=a["edhrec"].get)
        share = ", ".join(f"B{k} {100 * v / tot:.0f}%" for k, v in sorted(a["edhrec"].items()))
        ctx.append(f"- Community data (EDHREC, all decks for this commander, not this list): {share}; most reported **Bracket {mode}**. "
                   + ("This list's floor is above the most-reported bracket — it is stronger than the typical deck for this commander." if a["floor"] > mode else "The floor is at or below the most-reported bracket."))
    if a["one_card_away"]:
        ctx.append(f"- Spellbook also lists {a['one_card_away']} combos one card away (not counted): adding a single card can raise the floor.")
    if ctx:
        L += ["### Calibration context", ""] + ctx + [""]
    # lower-bracket paths
    L += ["### Playing at a lower bracket (guidance)", ""]
    cuts = cut_set(a["two"], a["commanders"])
    if a["floor"] >= 4:
        need = []
        if len(g) > 3:
            need.append(f"cut {len(g) - 3} of the {len(g)} Game Changers")
        if a["mld"]:
            need.append(f"cut the mass land denial ({', '.join(a['mld'])})")
        L.append(f"- **To reach Bracket 3:** {' and '.join(need)}" + ("; keep the two-card infinite for the late game only, or cut it (Bracket 3 allows no *early-game* two-card infinites)." if a["two"] else "."))
    if a["floor"] >= 3:
        need = []
        if g:
            need.append(f"cut all {len(g)} Game Changers")
        if cuts:
            need.append(f"break every two-card infinite (minimum cut: {', '.join(cuts)})")
        if a["mld"]:
            need.append("cut the mass land denial")
        L.append(f"- **To reach Bracket 2:** {'; '.join(need)}; keep extra turns to a low count.")
    if a["floor"] <= 2:
        L.append("- Already at the Bracket 2 floor. Bracket 1 is about theme and intent (and pod agreement), not a card count.")
    L.append("- Which replacements to add is opinion; every replacement must still fit the commander's identity and be Commander-legal.")
    L.append("")
    # pilot notes
    r = a["roles"]
    p3 = hyper_between(3, 5, a["lands"])
    p2 = hyper_at_least(2, a["lands"])
    pr = 1 - hyper_at_least(1, len(r["ramp"])) if r["ramp"] else 1.0
    L += ["### Pilot notes (guidance)", "",
          f"- **Mana (fact):** {a['lands']} lands, {len(r['ramp'])} ramp pieces, average nonland mana value {a['avg_mv']}. "
          f"A 7-card opening hand has 3–5 lands {100 * p3:.0f}% of the time and at least 2 lands {100 * p2:.0f}%"
          + (f"; it has no ramp piece {100 * pr:.0f}% of the time." if r["ramp"] else ".")
          + f" **Guidance:** keep 3–4 landers, or 2 lands plus ramp; see [EDH Mulligans]({rel(p, 'EDH Mulligans.md')}#keep-or-mulligan-guidance).",
          "- **Interaction budget (fact):** " + " · ".join(f"{len(r[k])} {ROLE_LABEL[k]}" for k in ("removal", "wipe", "counter", "protection", "draw")) +
          ". **Guidance:** " + ("hold protection or a counterspell on the turn you commit the commander or a combo." if (r["protection"] or r["counter"]) else
                                "with no protection or counterspells, sequence threats so a single removal spell does not end the plan.")]
    if a["two"] or a["combos"]:
        lines = a["two"] or [c for c in a["combos"] if c["infinite"]][:3] or a["combos"][:2]
        ex = "; ".join(f"[{' + '.join(c['cards'])}]({c['url']}) → {c['produces'].split(',')[0]}" for c in lines[:3])
        L.append(f"- **Combo lines (fact, Spellbook):** {ex}" + (f" (+{len(a['combos']) - len(lines[:3])} more in the Combos block)" if len(a["combos"]) > len(lines[:3]) else "") + ". "
                 + (f"**Guidance:** the {len(tu)} tutor{'s' if len(tu) != 1 else ''} ({', '.join(tu[:4])}{' …' if len(tu) > 4 else ''}) can fetch a missing piece; announce the combo in the pregame talk." if tu else
                    "**Guidance:** with no tutors, treat the combo as a bonus line and announce it in the pregame talk."))
    else:
        L.append(f"- **Win plan:** no complete Spellbook combo in the list. **Guidance:** it wins through board presence and the commander; see [EDH Win Conditions]({rel(p, 'EDH Win Conditions.md')}) for finishers that fit the identity.")
    L.append(f"- **Pregame talk (guidance):** say the floor (Bracket {a['floor']}), the Game Changers ({len(g)}), and any two-card infinite or extra-turn cards before the game, as the Brackets intend.")
    if a["kind"] == "grixis":
        L.append("- **Source author's own pilot reasoning:** see [Source commentary (verbatim)](#source-commentary-verbatim) below (guidance from the Grixis repo).")
    L.append(END)
    return "\n".join(L)


def fix_bracket_bullet(body, a):
    old = "- Two-card infinite combos: ⚠️ not machine-checked — review manually."
    if old in body or "- Two-card infinite combos (Commander Spellbook):" in body:
        new = (f"- Two-card infinite combos (Commander Spellbook): {len(a['two'])}" + (f" — {'; '.join(' + '.join(c['cards']) for c in a['two'])}" if a["two"] else "")
               + " (see [Combos](#combos-commander-spellbook) and [calibration](#bracket-calibration--pilot-notes))")
        body = re.sub(r"^- Two-card infinite combos(?::| \(Commander Spellbook\):).*$", lambda _m: new, body, count=1, flags=re.M)
    return body


def insert(text, a, p):
    head = fm.FM.match(text)
    pre = head.group(0) if head else ""
    body = text[len(pre):]
    body = fix_bracket_bullet(body, a)
    blk = block(a, p)
    if START in body:
        i, j = body.index(START), body.index(END) + len(END)
        body = body[:i] + blk + body[j:]
    else:
        m = re.search(r"^## Bracket assessment\n.*?(?=^## )", body, re.S | re.M)
        body = body[:m.end()] + blk + "\n\n" + body[m.end():]
    line = "- [Bracket calibration & pilot notes](#bracket-calibration--pilot-notes)"
    if line not in body:
        body = body.replace("- [Bracket assessment](#bracket-assessment)\n", "- [Bracket assessment](#bracket-assessment)\n" + line + "\n", 1)
    return pre + body


def lore_section(all_a):
    """Bot cycle 32 (#95): lore decks get the same calibration row plus their lore score and story-map coverage."""
    spec = json.loads((ROOT / "data" / "lore_decks" / "lore_decks.json").read_text(encoding="utf-8"))
    sm = {f"decks/{d['slug']}.md": d.get("story_map", {}) for d in spec["decks"]}
    L = ["", "## Lore decks", "",
         "Story-first decks ([EDH Lore-Themed Deckbuilding](EDH%20Lore-Themed%20Deckbuilding.md)). They are calibrated like every other deck. "
         "*Lore score* = story-linked share of non-basic cards (≥ 85% standard, `scripts/build_lore_decks.py --check`). "
         "*Story map* = non-playability packages that point at a [lore entry](Lore%20Entry%20Index.md) (each entry links the deck back; `scripts/check_lore.py`).", "",
         "| Deck | Floor | GC | 2-card ∞ | Lands | Avg MV | Lore score | Story map | Pilot & story notes |", "|---|---|---|---|---|---|---|---|---|"]
    for a in sorted((a for a in all_a if a["kind"] == "lore"), key=lambda a: a["title"]):
        m = re.search(r"^lore_score: ([\d.]+)", a["text"], re.M)
        pk = {k: v for k, v in sm.get(a["path"], {}).items() if not k.startswith("Playability")}
        cov = f"{sum(1 for v in pk.values() if v)}/{len(pk)} packages" if pk else "—"
        path = a["path"].replace(" ", "%20")
        L.append(f"| [{a['title'].replace('Lore Deck — ', '')}]({path}#bracket-calibration--pilot-notes) | **{a['floor']}** | {len(a['gcs'])} | {len(a['two'])} | {a['lands']} | {a['avg_mv']} | "
                 f"{m.group(1) + '%' if m else '—'} | {cov} | [calibration]({path}#pilot-notes-guidance) · [story map]({path}#story-map) |")
    return L


def summary_page(all_a):
    by_floor = Counter(a["floor"] for a in all_a)
    L = ["# EDH Bracket Calibration", "",
         f"> **Auto-generated** by `scripts/deck_calibration.py` (Bot cycle 19, issue [#68]({I}68)). One row per deck in [decks/](decks/) and [grixis/decks/](grixis/README.md). "
         "Floors are facts from the official barometers ([EDH Standards → Power bracket assessment](EDH%20Standards.md#power-bracket-assessment)); stated targets and community data are context; every deck page carries the full rationale and pilot notes (guidance).", "",
         "## Contents", "- [Summary](#summary)", "- [All decks](#all-decks)", "- [Targets below the floor](#targets-below-the-floor)", "- [Lore decks](#lore-decks)", "- [Method](#method)", "",
         "## Summary", "",
         f"- **{len(all_a)} decks**: floor Bracket 2: **{by_floor[2]}** · Bracket 3: **{by_floor[3]}** · Bracket 4: **{by_floor[4]}**.",
         f"- Set by Game Changers (> 3): {sum(1 for a in all_a if len(a['gcs']) > 3)} · mass land denial: {sum(1 for a in all_a if a['mld'])} · two-card infinites: {sum(1 for a in all_a if a['two'])} decks ({sum(len(a['two']) for a in all_a)} combos).",
         f"- Decks with extra-turn cards: {sum(1 for a in all_a if a['extra_turns'])} · median tutors per deck: {sorted(len(a['roles']['tutor']) for a in all_a)[len(all_a) // 2]}.",
         f"- Grixis source targets: {sum(1 for a in all_a if a['target'])} stated; {sum(1 for a in all_a if a['target'] and a['target'] < a['floor'])} below the floor.", "",
         "## All decks", "", "| Deck | Kind | Identity | Floor | GC | 2-card ∞ | MLD | Extra turns | Tutors | Lands | Avg MV | Stated target | EDHREC mode |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for a in sorted(all_a, key=lambda a: (-a["floor"], a["kind"], a["title"])):
        name = a["title"].replace("Deck Skeleton — ", "").replace("Grixis Deck — ", "")
        mode = max(a["edhrec"], key=a["edhrec"].get) if a["edhrec"] else "—"
        L.append(f"| [{name}]({a['path'].replace(' ', '%20')}#bracket-calibration--pilot-notes) | {a['kind']} | {a['identity']} | **{a['floor']}** | {len(a['gcs'])} | {len(a['two'])} | {len(a['mld'])} | {len(a['extra_turns'])} | {len(a['roles']['tutor'])} | {a['lands']} | {a['avg_mv']} | {a['target'] or '—'} | {mode} |")
    below = [a for a in all_a if a["target"] and a["target"] < a["floor"]]
    L += ["", "## Targets below the floor", ""]
    L += [f"- [{a['title']}]({a['path'].replace(' ', '%20')}#bracket-calibration--pilot-notes): target {a['target']}, floor {a['floor']}" for a in below] or ["None: every stated target is at or above the deck's floor."]
    L += lore_section(all_a)
    L += ["", "## Method", "",
          "- **Floor (fact):** 0 Game Changers → 2 · 1–3 → 3 · 4+ → 4; any mass land denial → 4; any two-card infinite (Commander Spellbook, complete in the list) → at least 3. The highest applies. Game Changer and Oracle data: Scryfall bulk; combos: each deck's Spellbook block.",
          "- **Not a floor input:** tutors (the Oct 2025 update removed tutor limits) and extra turns beyond Bracket 1 (\"low quantity\" is a judgment). Both are shown.",
          "- **Bracket 5** (cEDH) depends on intent and metagame, so no list is floored at 5; see [cEDH Primer](cEDH%20Primer.md).",
          "- **Role counts** are Oracle-text pattern matches (ramp, draw, removal, wipes, counterspells, protection, tutors), so a card can count in several roles or fit loosely.",
          "- **Pilot notes** are guidance built from those counts and the hypergeometric opening-hand odds (99-card library, 7-card hand)."]
    return "\n".join(L) + "\n"


def main(argv):
    check = "--check" in argv
    R = ev.Resolver()
    all_a, stale = [], []
    for d in DECK_DIRS:
        for p in sorted((ROOT / d).glob("*.md")):
            a = analyse(p, R)
            new = insert(a["text"], a, p)
            if new != a["text"]:
                stale.append(str(p.relative_to(ROOT)))
                if not check:
                    p.write_text(new, encoding="utf-8")
            all_a.append(a)
    page = summary_page(all_a)
    if fm.body_of(PAGE.read_text(encoding="utf-8")).strip() != page.strip() if PAGE.exists() else True:
        stale.append(PAGE.name)
        if not check:
            PAGE.write_text(page, encoding="utf-8")
    data = {"generated_by": "scripts/deck_calibration.py", "decks": [{k: v for k, v in a.items() if k not in ("body", "text", "combos")} |
                                                                     {"two": [c["cards"] for c in a["two"]], "roles": {k: len(v) for k, v in a["roles"].items()}} for a in all_a]}
    js = json.dumps(data, ensure_ascii=False, indent=1) + "\n"
    if not OUT.exists() or OUT.read_text(encoding="utf-8") != js:
        stale.append(str(OUT.relative_to(ROOT)))
        if not check:
            OUT.write_text(js, encoding="utf-8")
    print(f"calibration: {len(all_a)} decks; floors {dict(sorted(Counter(a['floor'] for a in all_a).items()))}; {len(stale)} {'stale' if check else 'updated'}")
    return 1 if check and stale else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
