"""Detect combos in every deck skeleton with Commander Spellbook's public API (Bot cycle 4).

POSTs each decklist to https://backend.commanderspellbook.com/find-my-combos and records the
combos whose cards are ALL in the deck ("included"). Writes:
  * a "Combos (Commander Spellbook)" block between <!-- COMBOS:START/END --> in each deck,
  * data/combos.json (raw summary, for reproducibility).
Facts only: combo pieces/results are Commander Spellbook community data (cited per combo);
the bracket implication uses the official Brackets barometer (no intentional two-card infinite
combos in Brackets 1-2). Anything else is Opinion and is not written here.
"""
import json, re, sys, time, urllib.request, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parent.parent
API = "https://backend.commanderspellbook.com/find-my-combos"
START, END = "<!-- COMBOS:START -->", "<!-- COMBOS:END -->"

def deck_cards(path):
    cmd, main = [], []
    for l in path.read_text().splitlines():
        m = re.match(r"^1x (.+?) \[(.*?)\]", l)
        if m: (cmd if m.group(2).startswith("Commander") else main).append(m.group(1))
    return cmd, main

def query(cmd, main):
    body = json.dumps({"commanders": [{"card": c} for c in cmd], "main": [{"card": c} for c in main]}).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json", "User-Agent": "GrokBotMTGCompanion/1.0"})
    for attempt in range(3):
        try:
            return json.load(urllib.request.urlopen(req, timeout=90))["results"]
        except Exception as e:
            if attempt == 2: raise
            time.sleep(3)

def infinite(v): return any("infinite" in p["feature"]["name"].lower() for p in v["produces"])

def main():
    today = datetime.date.today().isoformat()
    summary = {}
    for d in sorted((ROOT / "decks").glob("*.md")):
        cmd, mn = deck_cards(d)
        res = query(cmd, mn)
        inc = res["included"]
        rows = []
        for v in sorted(inc, key=lambda v: (len(v["uses"]), v["id"])):
            names = [u["card"]["name"] for u in v["uses"]]
            rows.append({"id": v["id"], "cards": names, "n": len(names), "infinite": infinite(v),
                         "produces": [p["feature"]["name"] for p in v["produces"]][:4],
                         "requires": [r["template"]["name"] for r in v.get("requires", [])],
                         "csb_bracket_tag": v.get("bracketTag")})
        two_inf = [r for r in rows if r["n"] == 2 and r["infinite"]]
        summary[d.stem] = {"commander": cmd, "combos": rows, "two_card_infinite": len(two_inf),
                           "almost": len(res.get("almostIncluded", []))}
        lines = [START, "## Combos (Commander Spellbook)", "",
                 f"> Auto-generated {today} by `scripts/detect_combos.py` from the [Commander Spellbook](https://commanderspellbook.com) public API (community-maintained combo database; each combo links to its page). "
                 "Only combos whose **every card is in this list** are shown. Bracket note uses the official barometer: *Brackets 1–2 — no intentional two-card infinite combos; Bracket 3 — no early-game two-card infinite combos*.", ""]
        if not rows:
            lines.append(f"**No complete combos found** ({summary[d.stem]['almost']} combos are one card away — not listed).")
        else:
            lines.append(f"**{len(rows)} complete combo(s); {len(two_inf)} two-card infinite.** {summary[d.stem]['almost']} more are one card away (not listed).")
            lines.append("")
            lines.append("| Cards | Produces (Spellbook) | Extra requirements | Link |")
            lines.append("|---|---|---|---|")
            for r in rows:
                flag = "⚠️ **two-card infinite** · " if r["n"] == 2 and r["infinite"] else ""
                req = "; ".join(r["requires"]) or "—"
                lines.append(f"| {flag}{' + '.join(r['cards'])} | {', '.join(r['produces'])} | {req} | [{r['id']}](https://commanderspellbook.com/combo/{r['id']}/) |")
            if two_inf:
                lines += ["", "**Bracket implication:** a two-card infinite combo is outside the Bracket 1–2 barometer, so this deck as listed sits at **Bracket 3+** unless the combo is cut; whether it is *early-game* (Bracket 3 vs 4) is **Opinion** and must be discussed at Rule 0."]
        lines.append(END)
        block = "\n".join(lines)
        txt = d.read_text()
        if START in txt:
            txt = re.sub(re.escape(START) + ".*?" + re.escape(END), block, txt, flags=re.S)
        else:
            txt = txt.rstrip("\n") + "\n\n" + block + "\n"
        if "- [Combos (Commander Spellbook)](#combos-commander-spellbook)" not in txt:
            txt = txt.replace("- [Commander rules & rulings](#commander-rules--rulings)", "- [Commander rules & rulings](#commander-rules--rulings)\n- [Combos (Commander Spellbook)](#combos-commander-spellbook)", 1)
        d.write_text(txt)
        print(f"{d.name}: {len(rows)} combos, {len(two_inf)} two-card infinite", flush=True)
        time.sleep(1)
    (ROOT / "data" / "combos.json").write_text(json.dumps({"generated": today, "source": API, "decks": summary}, indent=1))

if __name__ == "__main__":
    main()
