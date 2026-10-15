#!/usr/bin/env python3
"""Bot cycle 21 (issues #79-#81): build story-first lore-themed Commander decks.

Input: data/lore_decks/lore_decks.json (hand-curated lists, packages, cited story summaries).
For every card the script adds machine-found evidence of its story link, all of it facts from
Scryfall bulk in .cache/: name keyword hits, flavor-text quotes containing an arc keyword (any paper
printing, default-cards bulk), printings in the arc's story sets, and type-line echoes (Kor, Construct…).
A card with no evidence and no cited note is labeled "playability slot (guidance)", and the page
reports the story-linked share. Bot cycle 23: >= 85% of ALL non-basic cards (commander, non-land cards and non-basic lands);
only name / flavor / story-set printing / official-story-page notes count; type and mechanical echoes are guidance.
Hard checks come from scripts/evaluate_decklist.py: names, eligibility, 100 cards, singleton,
identity, Commander legality, Game Changers, plus Commander Spellbook combos (--online, cached
in data/lore_decks/combos.json otherwise).
Output: decks/<slug>.md in the shared deck layout (Commander / Validation / Bracket assessment /
Decklist / Card breakdown / Combos), so front_matter, deck_calibration and build_crossrefs pick them up.
Usage: python3 scripts/build_lore_decks.py [--online] [--check]
"""
import glob, gzip, json, re, sys, csv, urllib.request, datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402
import evaluate_decklist as ev  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
import lore_lib as _LL  # noqa: E402  (Bot cycle 32: names of lore entries for the story map)
ENTRY_NAMES = {f"{e['page']}#{e['anchor']}": e["name"] for e in _LL.all_entries()}
SPEC = ROOT / "data/lore_decks/lore_decks.json"
COMBOS = ROOT / "data/lore_decks/combos.json"
API = "https://backend.commanderspellbook.com/find-my-combos"
I = "https://github.com/corymstover/GrokBotMTGCompanion/issues/"
THRESHOLD = 85  # Bot cycle 23: % of ALL non-basic cards (commander + non-land + non-basic lands)
OFFICIAL = re.compile(r"https://magic\.wizards\.com/en/(story|news)/")
TYPE_ECHO = re.compile(r"\b(Kor|Construct|Thopter|Golem|Artificer|Eldrazi|Equipment|Soldier|Angel|Powerstone)\b")
C_START, C_END = "<!-- COMBOS:START -->", "<!-- COMBOS:END -->"


def printings():
    f = sorted(glob.glob(str(ROOT / ".cache/default-cards-*.jsonl.gz")))[-1]
    sets, flav = {}, {}
    with gzip.open(f, "rt", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip().rstrip(",")
            if not line or line in "[]":
                continue
            c = json.loads(line)
            if "paper" not in c.get("games", []):
                continue
            n = c["name"]
            sets.setdefault(n, set()).add(c["set"])
            ft = c.get("flavor_text") or " ".join((x.get("flavor_text") or "") for x in c.get("card_faces") or [])
            if ft:
                flav.setdefault(n, set()).add(" ".join(ft.split()))
    return sets, flav


def spellbook(cmd, main, online, cache, slug):
    if not online:
        return cache.get(slug)
    body = json.dumps({"commanders": [{"card": cmd}], "main": [{"card": c} for c in main]}).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json", "User-Agent": "GrokBotMTGCompanion/1.0"})
    res = json.load(urllib.request.urlopen(req, timeout=90))["results"]
    rows = []
    for v in sorted(res["included"], key=lambda v: (len(v["uses"]), v["id"])):
        names = [u["card"]["name"] for u in v["uses"]]
        rows.append({"id": v["id"], "cards": names, "infinite": any("infinite" in p["feature"]["name"].lower() for p in v["produces"]),
                     "produces": [p["feature"]["name"] for p in v["produces"]][:4], "requires": [r["template"]["name"] for r in v.get("requires", [])]})
    out = {"date": datetime.date.today().isoformat(), "combos": rows, "almost": len(res.get("almostIncluded", []))}
    cache[slug] = out
    return out


def build(d, by, idx, sets, flav, R, combos):
    kw = re.compile(d["keywords"], re.I)
    story_sets = set(d["story_sets"])
    lk = lambda n: f"[{n}](../{idx[n]['shard']}#{idx[n]['anchor']})"
    names = [c["name"] for c in d["cards"]]
    text = "\n".join([f"1x {d['commander']} [Commander{{top}}]"] + [f"1x {n} [{c['package'].split(' (')[0]}]" for n, c in zip(names, d["cards"])]
                     + [f"{d['basics']}x {d['basic']} [Land]"]) + "\n"
    res = R and ev.check(text, R)
    hard = [i for i in res["issues"] if i["type"] in ev.HARD]
    cmd = by[d["commander"]]
    ci = "".join(x for x in "WUBRG" if x in (cmd.get("color_identity") or [])) or "C"
    gcs = [c["name"] for c in res["cards"] if c.get("gc")]
    xt = [c["name"] for c in res["cards"] if c.get("xturn")]
    mld = res.get("mass_land_denial") or []
    cb = spellbook(d["commander"], names, "--online" in sys.argv, combos, d["slug"]) or {"combos": [], "almost": 0, "date": "—"}
    two = [r for r in cb["combos"] if len(r["cards"]) == 2 and r["infinite"]]
    floor = 4 if (len(gcs) > 3 or mld) else 3 if (gcs or two) else 2
    rows, story_n, play_n = [], 0, 0
    entries = [{"name": d["commander"], "package": "Commander", "note": d.get("commander_note", "")}] + d["cards"]
    for c in entries:
        n, card = c["name"], by[c["name"]]
        ev_, counted = [], False
        if kw.search(n):
            ev_.append("named for the story"); counted = True
        fl = sorted(x for x in flav.get(n, ()) if kw.search(x))
        if fl:
            fl.sort(key=lambda x: (not re.search(r"—\s*\w", x), len(x)))
            q = fl[0] if len(fl[0]) <= 160 else fl[0][:157] + "…"
            ev_.append(f"flavor: “{q}”"); counted = True
        ss = sorted(sets.get(n, set()) & story_sets)
        if ss:
            ev_.append("printed in " + ", ".join(f"`{s}`" for s in ss)); counted = True
        note = c.get("note") or ""
        if note:
            ev_.insert(0, note)
            if OFFICIAL.search(note) and "mechanical echo" not in note.lower():
                counted = True
        te = sorted(set(TYPE_ECHO.findall(card.get("type_line", ""))))
        if te and not counted:
            ev_.append("type echo (guidance, not counted): " + ", ".join(te))
        if counted:
            story_n += 1
            why = "; ".join(ev_)
        else:
            play_n += 1
            why = "**Not story-linked under the 85% tests (guidance slot)**" + (": " + "; ".join(ev_) if ev_ else " — kept for mana, interaction or a win path.")
        land = "Land" in card.get("type_line", "")
        rows.append(f"| {lk(n)} | {c['package']}{' (land)' if land else ''} | {why} | {''.join(x for x in 'WUBRG' if x in (card.get('color_identity') or [])) or 'C'} |")
    share = round(100 * story_n / max(1, story_n + play_n), 1)
    nb_lands = sum(1 for r in rows if "(land)" in r.split(" | ")[1])
    nb_lands_linked = sum(1 for r in rows if "(land)" in r.split(" | ")[1] and "Not story-linked" not in r)
    pk = {}
    for c in d["cards"]:
        pk.setdefault(c["package"], []).append(c["name"])
    front = lambda c: (c.get("card_faces") or [c])[0].get("type_line", c.get("type_line", ""))
    lands = sum(1 for n in names if "Land" in front(by[n]).split("—")[0]) + int(d["basics"])  # Bot cycle 32: front face, as deck_calibration.py
    mdfc = sorted(n for n in names if "Land" in by[n]["type_line"] and "Land" not in front(by[n]).split("—")[0])
    L = [f"# {d['title']}", "",
         f"> **Lore-themed deck (story-first, not power-first).** Built by `scripts/build_lore_decks.py` (Bot cycle 21, [#80]({I}80); 85% standard Bot cycle 23) under [EDH Lore-Themed Deckbuilding](../EDH%20Lore-Themed%20Deckbuilding.md). Card data and legality are facts from Scryfall bulk; story claims cite official magic.wizards.com pages; package choices, pilot notes and *How the deck tells it* are **guidance**. ✅ sourced · ⚠️ uncertain · 🚫 non-canonical.",
         "", "## Contents", "- [Story the deck tells](#story-the-deck-tells)", "- [Commander](#commander)", "- [Validation](#validation)", "- [Bracket assessment](#bracket-assessment)",
         "- [Lore score](#lore-score)", "- [Packages](#packages)", "- [Decklist (Archidekt import)](#decklist-archidekt-import)", "- [Card breakdown](#card-breakdown)",
         "- [Story pilot notes (guidance)](#story-pilot-notes-guidance)", "- [Combos (Commander Spellbook)](#combos-commander-spellbook)", "",
         "## Story the deck tells", "", d["story"], "",
         f"Lore links: [Conflicts & Arcs](../Conflicts%20%26%20Arcs.md#{d['arc_anchor']}) · [Characters Index](../Characters%20Index.md#{d['character_anchor']}) · [Planes Index → {d['plane']}](../Planes%20Index.md#{d.get('plane_anchor', 'planes-with-official-profiles')}) · [Master Timeline](../Master%20Timeline.md)", "",
         "## Commander", "", f"- **{lk(d['commander'])}** — {cmd.get('mana_cost','')} — {cmd['type_line']}",
         f"- Color identity: **{ci}**", "- Eligibility: Yes (" + ("its Oracle text says it can be your commander" if "can be your commander" in (cmd.get("oracle_text") or "") else "legendary creature") + ")", "",
         "## Validation", "", f"- Total cards: **{res['total']}** ({lands} lands incl. {d['basics']} basics" + (f"; plus {len(mdfc)} modal double-faced spell/land: {', '.join(mdfc)}" if mdfc else "") + ")",
         "- Strict color identity (CR 903.5c), singleton (903.5b), Commander-legal, size (903.5a): " + ("✅ **all checks pass**" if not hard else "❌ " + "; ".join(i['detail'] for i in hard)),
         f"- Checked with `scripts/evaluate_decklist.py` against Scryfall bulk {R.bulk[:10]}.", "",
         "## Bracket assessment", "", (f"- Game Changers ({len(gcs)}): " + ", ".join(gcs)) if gcs else "- Game Changers: no Game Changers",
         "- Extra-turn cards: " + (", ".join(xt) or "none"), "- Mass land denial: " + (", ".join(mld) if mld else "none"),
         f"- Two-card infinite combos (Commander Spellbook): {len(two)}" + (" — " + "; ".join(" + ".join(r["cards"]) for r in two) if two else ""),
         f"- **Minimum bracket by the published barometers: {floor}**. Lore decks aim for Bracket 2–3 by design (guidance); see [EDH Standards](../EDH%20Standards.md#power-bracket-assessment).", "",
         "## Lore score", "", f"- **Story-linked: {story_n} / {story_n + play_n} non-basic cards ({share}%)** — {'✅ meets' if share >= THRESHOLD else '❌ below'} the ≥ {THRESHOLD}% standard. Counted over the commander, every non-land card and every non-basic land ({nb_lands} non-basic lands, {nb_lands_linked} of them story-linked); basics excluded. Not linked (guidance slots): {play_n}.",
         f"- Counting tests (facts): card **name**, **flavor text** of any paper printing, **printing in the story's sets**, or a note citing an **official story page**. Type and mechanical echoes are shown as guidance and **do not count**. Story sets: " + ", ".join(f"`{s}`" for s in d["story_sets"]) + ".", "",
         "## Packages", "", "| Package | Cards |", "|---|---|"]
    L += [f"| {p} | {len(v)} |" for p, v in pk.items()]
    L += ["", "## Decklist (Archidekt import)", "", "```text", text.rstrip(), "```", "",
          "## Card breakdown", "", "*Why this card belongs:* evidence first, then package. Quotes are flavor text from a paper printing (Scryfall).", "",
          "| Card | Package | Why it belongs | Identity |", "|---|---|---|---|"] + rows
    sm = d.get("story_map", {})
    L += ["", "## Story pilot notes (guidance)", "",
          "> Bot cycle 32 ([#95](" + I + "95)). Opening-hand odds, interaction counts and the floor are in [Bracket calibration & pilot notes](#bracket-calibration--pilot-notes) (generated, same as every deck). This section adds the lore side: which story each package plays out, linked to the [lore entries](../Lore%20Entry%20Index.md) that cite it. Package-to-entry pointers are curated in `data/lore_decks/lore_decks.json` (`story_map`); `scripts/check_lore.py` checks that every pointer resolves, and each entry links back.", "",
          f"- **Mana (fact):** {lands} lands" + (f" (front face; +{len(mdfc)} modal double-faced spell/land)" if mdfc else "") + ". **Guidance:** keep hands with 3+ lands or 2 lands plus a mana rock; the deck is slower than a tuned list by design.",
          "- **Win path (guidance):** " + d.get("win_path", "combat with the commander's package; the story finale card is a fun closer, not a guaranteed one."),
          "- **Interaction (guidance):** the list keeps a small removal/counter suite so the story can reach its ending; hold it for threats that end the game.",
          f"- **Pregame talk (guidance):** say it is a lore deck at Bracket {floor}, {len(gcs)} Game Changers, {len(two)} two-card infinites.",
          "- **Telling the story at the table (guidance):** name the package when you cast its first card. The table below is the cheat sheet.", ""]
    if sm:
        def ent(k):
            pg, _, a = k.partition("#")
            lab = {"Conflicts & Arcs.md": "Arc", "Planes Index.md": "Plane", "Items & Artifacts Index.md": "Item", "Planeswalker Dossiers.md": "Dossier",
                   "Characters Index.md": "Character", "Contradictions & Retcons Log.md": "Retcon", "Master Timeline.md": "Era"}[pg]
            return f"{lab}: [{ENTRY_NAMES.get(k, a)}](../{pg.replace(' ', '%20').replace('&', '%26')}#{a})"
        L += ["### Story map", "", "| Package | Cards | Story it plays out (lore entries) |", "|---|---|---|"]
        for pkg in sorted(pk, key=lambda x: (-len(pk[x]), x)):
            ks = sm.get(pkg, [])
            L.append(f"| {pkg} | {len(pk[pkg])} | " + (" · ".join(ent(k) for k in ks) if ks else ("— (playability slots)" if pkg.startswith("Playability") else "— ⚠️ no lore entry covers this yet")) + " |")
        L.append("")
    blk = [C_START, "## Combos (Commander Spellbook)", "", f"> From the [Commander Spellbook](https://commanderspellbook.com) API ({cb['date']}); only combos complete in this list."]
    if not cb["combos"]:
        blk += ["", f"**No complete combos found** ({cb['almost']} combos are one card away — not listed)."]
    else:
        blk += ["", f"**{len(cb['combos'])} complete combo(s); {len(two)} two-card infinite.** {cb['almost']} more are one card away (not listed).", "",
                "| Cards | Produces (Spellbook) | Extra requirements | Link |", "|---|---|---|---|"]
        blk += [f"| {' + '.join(r['cards'])} | {', '.join(r['produces'])} | {'; '.join(r['requires']) or '—'} | [{r['id']}](https://commanderspellbook.com/combo/{r['id']}/) |" for r in cb["combos"]]
    blk.append(C_END)
    return "\n".join(L + blk) + "\n", {"slug": d["slug"], "type": d["type"], "commander": d["commander"], "identity": ci, "floor": floor, "gc": len(gcs),
                                       "story": story_n, "playability": play_n, "share": share, "valid": not hard, "lands": lands, "nonbasic_lands": nb_lands, "nonbasic_lands_linked": nb_lands_linked, "threshold": THRESHOLD}


def main():
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    cards, _ = ing.get_bulk(ing.DEFAULT_CACHE, None)
    by = {c["name"]: c for c in cards}
    idx = {r["name"]: r for r in csv.DictReader(ing.INDEX_CSV.open(encoding="utf-8"))}
    sets, flav = printings()
    R = ev.Resolver()
    combos = json.loads(COMBOS.read_text()) if COMBOS.exists() else {}
    stale, summary = [], []
    for d in spec["decks"]:
        page, s = build(d, by, idx, sets, flav, R, combos)
        summary.append(s)
        p = ROOT / "decks" / f"{d['slug']}.md"
        old = p.read_text(encoding="utf-8") if p.exists() else ""
        # keep front-matter and generated blocks (calibration, cross-refs) written by other scripts
        body_old = re.sub(r"^---\n.*?\n---\n\n?", "", old, flags=re.S)
        keep = {k: re.search(re.escape(a) + ".*?" + re.escape(b), body_old, re.S) for k, a, b in
                (("cal", "<!-- CALIBRATION:START -->", "<!-- CALIBRATION:END -->"), ("xr", "<!-- CROSSREFS:START -->", "<!-- CROSSREFS:END -->"))}
        new = page
        if keep["cal"]:
            new = new.replace("\n## Lore score", "\n" + keep["cal"].group(0) + "\n\n## Lore score", 1)
        if keep["xr"]:
            new = new.rstrip("\n") + "\n\n" + keep["xr"].group(0) + "\n"
        fm_ = re.match(r"^---\n.*?\n---\n\n?", old, re.S)
        new = (fm_.group(0) if fm_ else "") + new
        # --check compares only the sections this script owns (other scripts post-edit TOC, combo and calibration text)
        own = lambda t: [m.group(0) for m in re.finditer(r"^## (Lore score|Packages|Decklist \(Archidekt import\)|Card breakdown)\n.*?(?=^## |\Z)", t, re.S | re.M)]
        if ("--check" in sys.argv and own(new) != own(old)) or ("--check" not in sys.argv and new != old):
            stale.append(p.name)
            if "--check" not in sys.argv:
                p.write_text(new, encoding="utf-8")
    if "--check" not in sys.argv:
        COMBOS.write_text(json.dumps(combos, indent=1))
        (ROOT / "data/lore_decks/summary.json").write_text(json.dumps(summary, indent=1))
    for s in summary:
        print(f"{s['slug']}: valid={s['valid']} floor={s['floor']} GC={s['gc']} lands={s['lands']} story {s['story']}/{s['story'] + s['playability']} ({s['share']}%) nonbasic lands linked {s['nonbasic_lands_linked']}/{s['nonbasic_lands']}")
    if "--check" in sys.argv:
        print(f"lore decks: {len(summary)} decks; {len(stale)} stale")
        low = [s["slug"] for s in summary if s["share"] < THRESHOLD]
        if low:
            print(f"lore decks below {THRESHOLD}%: " + ", ".join(low))
        return 1 if stale or low or not all(s["valid"] for s in summary) else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
