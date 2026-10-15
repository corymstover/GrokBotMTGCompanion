"""Shared helpers for Bot cycle 6 EDH guide generators (Scryfall Oracle bulk + repo card index).
Every listed card is Commander-legal (Scryfall `legalities.commander == legal`) and links to its verified entry.
Prices: cheapest paper USD printing in Scryfall `default_cards` bulk (snapshot; prices change daily)."""
import csv, gzip, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402

WUBRG = "WUBRG"
NAMES = {"C": "Colorless", "W": "White", "U": "Blue", "B": "Black", "R": "Red", "G": "Green",
         "WU": "Azorius", "UB": "Dimir", "BR": "Rakdos", "RG": "Gruul", "WG": "Selesnya",
         "WB": "Orzhov", "UR": "Izzet", "BG": "Golgari", "WR": "Boros", "UG": "Simic",
         "WUG": "Bant", "WUB": "Esper", "UBR": "Grixis", "BRG": "Jund", "WRG": "Naya",
         "WBG": "Abzan", "WUR": "Jeskai", "UBG": "Sultai", "WBR": "Mardu", "URG": "Temur",
         "UBRG": "Glint (non-W)", "WBRG": "Dune (non-U)", "WURG": "Ink (non-B)", "WUBG": "Witch (non-R)",
         "WUBR": "Yore (non-G)", "WUBRG": "Five-color"}
ORDER = list(NAMES)


class Data:
    def __init__(self):
        cards, self.bulk = ing.get_bulk(ing.DEFAULT_CACHE, None)
        self.rows = {r["oracle_id"]: r for r in csv.DictReader(ing.INDEX_CSV.open(encoding="utf-8"))}
        pf = ing.DEFAULT_CACHE / "min_usd_20261015.json"
        self.price = json.loads(pf.read_text()) if pf.exists() else {}
        self._all = {c['name']: c for c in cards if c.get('layout') not in ing.EXCLUDED_LAYOUTS}
        self.pool = [c for c in cards if c.get("layout") not in ing.EXCLUDED_LAYOUTS and ing.in_universe(c)
                     and c.get("legalities", {}).get("commander") == "legal" and c["oracle_id"] in self.rows]
        self.pool.sort(key=lambda c: c.get("edhrec_rank") or 10**9)
        self.by_name = {c["name"]: c for c in self.pool}
        for c in self.pool:
            for f in c["name"].split(" // "):
                self.by_name.setdefault(f, c)

    def bulk_card(self, name):
        return self._all.get(name)

    @staticmethod
    def text(c):
        faces = c.get("card_faces") or []
        return (c.get("oracle_text") or " ".join(f.get("oracle_text", "") for f in faces)).replace("\n", " ")

    @staticmethod
    def ftype(c):
        return (c.get("card_faces") or [c])[0].get("type_line") or c.get("type_line", "")

    @staticmethod
    def ci(c):
        s = set(c.get("color_identity", []))
        return "".join(x for x in WUBRG if x in s) or "C"

    def usd(self, c):
        p = self.price.get(c["oracle_id"])
        return f"${p:,.2f}" if p is not None else "—"

    def link(self, c, rel=""):
        r = self.rows[c["oracle_id"]]
        return f"[{r['name']}]({rel}{r['shard'].replace(' ', '%20')}#{r['anchor']})"

    @staticmethod
    def gc(c):
        return "**GC**" if c.get("game_changer") else ""

    @staticmethod
    def mv(c):
        m = c.get("cmc", 0)
        return int(m) if float(m).is_integer() else m

    def find(self, pat, kind="nonland", types=None, excl=None, maxmv=None, ident=None, extra=None):
        rx = re.compile(pat, re.I); ex = re.compile(excl, re.I) if excl else None
        out = []
        for c in self.pool:
            t = self.ftype(c)
            if kind == "nonland" and "Land" in t.split("—")[0] and "Creature" not in t: continue
            if kind == "land" and "Land" not in t: continue
            if types and not re.search(types, t): continue
            if maxmv is not None and (c.get("cmc") or 0) > maxmv: continue
            if ident is not None and self.ci(c) != ident: continue
            tx = self.text(c)
            if not rx.search(tx) or (ex and ex.search(tx)): continue
            if extra and not extra(c): continue
            out.append(c)
        return out

    def table(self, cs, n=10, cols=("ci", "mv", "rank", "usd", "gc"), extra=None):
        hdr = {"ci": "Identity", "mv": "MV", "rank": "EDHREC rank", "usd": "Cheapest USD", "gc": "GC", "type": "Type"}
        h = ["Card"] + ([extra[0]] if extra else []) + [hdr[k] for k in cols]
        out = ["| " + " | ".join(h) + " |", "|" + "---|" * len(h)]
        for c in cs[:n]:
            v = {"ci": self.ci(c), "mv": str(self.mv(c)), "rank": f"{c['edhrec_rank']:,}" if c.get("edhrec_rank") else "—",
                 "usd": self.usd(c), "gc": self.gc(c), "type": self.ftype(c).replace("|", "/")}
            out.append("| " + " | ".join([self.link(c)] + ([extra[1](c)] if extra else []) + [v[k] for k in cols]) + " |")
        return out

    def header(self, title, gen, issue, extra=""):
        return [f"# {title}", "",
                f"> **Auto-generated** by `{gen}` (Bot cycle 6, issue [#{issue}](https://github.com/corymstover/GrokBotMTGCompanion/issues/{issue})) from Scryfall Oracle bulk {self.bulk[:10]}. Do not hand-edit.",
                "> **Data:** every card listed is **Commander-legal** per Scryfall. *Identity* is its color identity: it fits a deck only if that identity is a subset of the commander's ([CR 903.4](Rules%20Interactions.md#commander-color-identity)). Lists are ordered by Scryfall `edhrec_rank` (EDHREC popularity, lower = more played); popularity is not power. **GC** = official Game Changer, which affects the [Commander Brackets](EDH%20Standards.md#power-bracket-assessment). *Cheapest USD* is the lowest current paper price across printings in Scryfall's default-cards bulk (2026-10-15 snapshot; prices move daily). Categories are Oracle-text pattern matches; the patterns are listed in each section.",
                "> **Guidance** paragraphs are strategy advice (opinion), not rules or fact." + (" " + extra if extra else ""), ""]
