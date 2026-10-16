#!/usr/bin/env python3
"""Verbatim quote verification for lore pages (Bot cycle 31) and rules/FAQ/EDH pages (Bot cycle 32, #96).

Every double-quoted passage (>= 12 characters) on a lore page is checked against
  1. the official story pages cached in .cache/story/text22/ (fetched by build_primary_sources.py; gitignored), preferring
     the official URLs cited on the same line, then any cached page; and
  2. card text in the cached Scryfall default-cards bulk (flavor text of every printing, Oracle text, card names);
  3. (cycle 32) cited non-story Wizards pages in .cache/story/articles/ (rules articles, policy pages, the Commander format
     page), the cached Comprehensive Rules text and every Scryfall ruling comment (status "rules"); and
  4. for the two Grixis-derived method pages only, the read-only Grixis source checkout ($GRIXIS_SRC, default
     grixis/source-archive/grixis-commander-encyclopediaGPT since Bot cycle 45; status "grixis-repo"). Without that checkout the status is carried over from the ledger.
Normalization: curly quotes/dashes folded, whitespace collapsed, case-folded, markdown emphasis removed; "…" / "..." and
editorial [brackets] and " / " (between Oracle lines) split a quote into parts that must each appear.
Results per quote: verified (cited page) · verified-other (another cached official page) · card (card text) ·
uncached (a cited official page is not in the cache) · MISS.
The ledger data/lore_quotes.json stores per-page counts plus every non-verified quote with its documented reason
(data/lore_quote_exceptions.json). Without the cache (fresh clone) --check falls back to comparing quote fingerprints with
the ledger, so an edited or new quote still fails until it is re-verified on a machine that has the cache.

  python3 scripts/lore_quotes.py --build     verify and write data/lore_quotes.json (needs the cache)
  python3 scripts/lore_quotes.py --check     exit 1 on an unexplained MISS, or a stale ledger
  python3 scripts/lore_quotes.py --report    print every non-verified quote
"""
import atomic_io  # noqa: F401  atomic Path.write_text/write_bytes (Bot cycle 34)
import gzip
import os
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lore_lib as L  # noqa: E402

ROOT = L.ROOT
CACHE = ROOT / ".cache" / "story" / "text22"
ARTICLES = ROOT / ".cache" / "story" / "articles"  # Bot cycle 32: cited non-story Wizards pages (rules articles, policies), gitignored
GRIXIS_SRC = Path(os.environ.get("GRIXIS_SRC", str(ROOT / "grixis/source-archive/grixis-commander-encyclopediaGPT")))  # Bot cycle 45: archived Grixis source
OUT = ROOT / "data" / "lore_quotes.json"
EXC = ROOT / "data" / "lore_quote_exceptions.json"
PAGES = ["Planeswalker Dossiers.md", "Planes Index.md", "Items & Artifacts Index.md", "Contradictions & Retcons Log.md",
         "Characters Index.md", "Conflicts & Arcs.md", "Master Timeline.md", "Story Arc Summaries.md",
         "Omenpath & Multiverse Connections.md", "EDH Lore-Themed Deckbuilding.md", "Side-Media Index.md", "Lore Primary Sources.md",
         "Art & Flavor Story Links.md"]
RULES_PAGES = ["FAQ.md", "Rules Interactions.md", "Keyword Encyclopedia.md", "EDH Standards.md", "EDH Mulligans.md",
               "EDH Deck Evaluation Checklist.md", "EDH Deck Template.md", "Card Data Conventions.md", "Tokens, Emblems & Dungeons.md",
               "Format Legality Matrix.md", "Printing History.md", "EDH Win Conditions.md",
               "EDH Lift and Synergy.md", "EDH Commander-First Deckbuilding.md"]  # Bot cycle 32 (#96); 57.5
GRIXIS_PAGES = {"EDH Deck Evaluation Checklist.md", "EDH Deck Template.md"}
PAGES = PAGES + RULES_PAGES
REASONS = {"image-text": "text printed only on images (e.g. the IKO Story on Cards page), so it cannot be machine-verified",
           "other-source": "a cited non-Wizards official page (publisher/retailer listing, Netflix Tudum), not in the story cache",
           "not-a-quote": "quotation marks around a KB label, term, title or code snippet, not a quotation"}


def norm(s):
    s = unicodedata.normalize("NFKC", s)  # ﬁ/ﬂ ligatures in PDF-derived guides
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", "-").replace("–", "-")
    s = s.replace("\u00a0", " ").replace('"', "'")  # nested quotations: a page's "x" may be quoted here as 'x'
    return " ".join(s.split()).lower()


def strip_md(s):
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    return s.replace("**", "").replace("*", "").replace("_", " ").replace("`", "")


def parts(q):
    q = strip_md(q)
    ps = re.split(r"\s*(?:…|\.\.\.|\[[^\]]*\]| / )\s*", q)  # " / " joins Oracle lines (Bot cycle 32)
    return [norm(p).strip(" .,;:!?'\"-") for p in ps if len(p.strip(" .,;:!?'\"-")) >= 8]


_story = _cards = None


def story():
    global _story
    if _story is None:
        _story = {}
        for f in list(CACHE.glob("*.txt")) + list(ARTICLES.glob("*.txt")):
            t = f.read_text(encoding="utf-8")
            url = t.split("\n", 1)[0][4:].strip().rstrip("/")
            _story[url] = norm(re.sub(r"\s*\|\s*Art by:[^\n]*", "", t))
    return _story


def cards():
    global _cards
    if _cards is None:
        import glob
        fs = sorted(glob.glob(str(ROOT / ".cache" / "default-cards-*.jsonl.gz")))
        buf = []
        if fs:
            with gzip.open(fs[-1], "rt", encoding="utf-8") as f:
                for line in f:
                    c = json.loads(line)
                    for face in [c] + c.get("card_faces", []):
                        for k in ("flavor_text", "oracle_text", "name", "flavor_name"):
                            if face.get(k):
                                buf.append(face[k])
        _cards = norm("\n".join(dict.fromkeys(buf)).replace("*", ""))  # Scryfall marks italics in flavor text with *
    return _cards


def pair_quotes(line):
    """Quoted passages on one line. Straight quotes are paired in order (1st with 2nd, 3rd with 4th, …) so a short
    quoted name such as "Ashiok" cannot swallow the text between two quotations; curly quotes pair by direction."""
    out = []
    line = re.sub(r"\]\([^)]*\)", "]", line)  # link targets never hold quotations
    pos = [i for i, ch in enumerate(line) if ch == '"']
    out += [line[a + 1:b] for a, b in zip(pos[::2], pos[1::2])]
    out += re.findall(r"“([^”]*)”", line)
    return [q for q in out if len(q) >= 12]


_rules = _grixis = None


def rules():
    """Comprehensive Rules text + every Scryfall ruling comment (Bot cycle 32: rules/FAQ pages quote both)."""
    global _rules
    if _rules is None:
        import glob
        buf = []
        cr = sorted(glob.glob(str(ROOT / ".cache" / "MagicCompRules-*.txt")))
        if cr:
            buf.append(Path(cr[-1]).read_text(encoding="utf-8", errors="ignore"))
        rl = sorted(glob.glob(str(ROOT / ".cache" / "rulings-*.jsonl.gz")))
        if rl:
            with gzip.open(rl[-1], "rt", encoding="utf-8") as f:
                buf += [json.loads(line).get("comment", "") for line in f]
        _rules = norm("\n".join(buf))
    return _rules


def grixis():
    """Markdown of the read-only Grixis source checkout (EDH Deck Template / Checklist quote its protocols)."""
    global _grixis
    if _grixis is None:
        _grixis = norm("\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in GRIXIS_SRC.rglob("*.md"))) if GRIXIS_SRC.exists() else ""
    return _grixis


def fp(q):
    return hashlib.sha1(norm(q).encode()).hexdigest()[:12]


def quotes(page):
    """(quote, context) pairs. The context is the quote's own line plus, when that line cites no official page, the
    official URLs cited elsewhere in the same ##/### section (a bullet often cites its source once per entry)."""
    text = L.body(ROOT / page)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    secs = re.split(r"\n(?=#{2,3} )", text)
    for sec in secs:
        sec_urls = " ".join(L.official_urls(sec))
        for line in sec.splitlines():
            ctx = line if L.official_urls(line) else line + " " + sec_urls
            for q in pair_quotes(line):
                if "http" in q or ".md" in q or not parts(q):
                    continue
                yield q, ctx


GRIXIS = False  # set per page: only the Grixis-derived method pages may verify against the Grixis source


def classify(q, line):
    ps = parts(q)
    S = story()
    cited = [u.rstrip("/") for u in L.official_urls(line)]
    for u in cited:
        if u in S and all(p in S[u] for p in ps):
            return "verified"
    allc = "\n".join(S.values()) if not hasattr(classify, "allc") else classify.allc
    classify.allc = allc
    if all(p in allc for p in ps):
        return "verified-other"
    C = cards()
    if all(p in C or p in allc for p in ps):
        return "card"
    Rr = rules()
    if all(p in Rr or p in C for p in ps):
        return "rules"
    if GRIXIS and all(p in grixis() for p in ps):
        return "grixis-repo"
    if any(u not in S for u in cited):
        return "uncached"
    return "MISS"


def build():
    global GRIXIS
    exc = json.loads(EXC.read_text(encoding="utf-8")) if EXC.exists() else {}
    led = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {"pages": {}}
    res = {"generated_by": "scripts/lore_quotes.py --build", "story_pages_cached": len(story()), "pages": {}}
    for page in PAGES:
        cnt, rows = {}, []
        GRIXIS = page in GRIXIS_PAGES and GRIXIS_SRC.exists()
        prev = {r["fp"]: r.get("status") for r in led["pages"].get(page, {}).get("quotes", [])}
        for q, line in quotes(page):
            k = classify(q, line)
            f = fp(q)
            if k == "MISS" and page in GRIXIS_PAGES and not GRIXIS_SRC.exists() and prev.get(f) == "grixis-repo":
                k = "grixis-repo"  # verified earlier against the Grixis checkout, which this machine lacks
            if k in ("MISS", "uncached") and f in exc.get(page, {}):
                k = "excepted:" + exc[page][f]["reason"]
            cnt[k.split(":")[0]] = cnt.get(k.split(":")[0], 0) + 1
            rows.append({"fp": f, "status": k, **({"quote": q[:160]} if not k.startswith("verified") and k not in ("card", "rules") else {})})
        res["pages"][page] = {"counts": dict(sorted(cnt.items())), "quotes": rows}
    return res


def dump(d):
    return json.dumps(d, ensure_ascii=False, indent=1) + "\n"


def main(argv):
    if "--build" in argv or "--report" in argv:
        if not CACHE.exists():
            print("lore quotes: story cache missing (.cache/story/text22) — run scripts/build_primary_sources.py first")
            return 1
        d = build()
        if "--report" in argv:
            for page, v in d["pages"].items():
                for r in v["quotes"]:
                    if "quote" in r:
                        print(f"{r['status']:<28} {page} | {r['quote'][:120]}")
            return 0
        OUT.write_text(dump(d), encoding="utf-8")
        tot = sum(sum(v["counts"].values()) for v in d["pages"].values())
        print(f"lore quotes: wrote {OUT.relative_to(ROOT)} ({tot} quotes)")
        return 0
    if not OUT.exists():
        print("lore quotes: data/lore_quotes.json missing — run python3 scripts/lore_quotes.py --build")
        return 1
    led = json.loads(OUT.read_text(encoding="utf-8"))
    bad = []
    if CACHE.exists():
        now = build()
        mode = f"re-verified against {now['story_pages_cached']} cached official pages + Scryfall card text + CR/rulings"
        if dump(now) != dump(led):
            bad.append("ledger stale — run python3 scripts/lore_quotes.py --build")
    else:
        mode = "story cache absent: compared quote fingerprints with the ledger"
        now = {"pages": {p: {"quotes": [{"fp": fp(q)} for q, _ in quotes(p)]} for p in PAGES}}
        for p in PAGES:
            if [r["fp"] for r in now["pages"][p]["quotes"]] != [r["fp"] for r in led["pages"].get(p, {}).get("quotes", [])]:
                bad.append(f"{p}: quotes changed since the ledger was verified (re-run --build where the cache exists)")
    exc = json.loads(EXC.read_text(encoding="utf-8")) if EXC.exists() else {}
    live = {(p, r["fp"]) for p, v in now["pages"].items() for r in v["quotes"]}
    for p, v in exc.items():
        if p.startswith("_"):
            continue
        for f, e in v.items():
            if e.get("reason") not in REASONS:
                bad.append(f"exception {p} {f}: unknown reason {e.get('reason')!r} (allowed: {', '.join(REASONS)})")
            if (p, f) not in live:
                bad.append(f"exception {p} {f}: quote no longer on the page — remove it from data/lore_quote_exceptions.json")
    tot, kinds = 0, {}
    for p, v in now["pages"].items():
        for r in v["quotes"]:
            tot += 1
            s = r.get("status", "ledger")
            kinds[s.split(":")[0]] = kinds.get(s.split(":")[0], 0) + 1
            if s in ("MISS", "uncached"):
                bad.append(f"{p}: {s} — \"{r.get('quote', '')[:100]}\" (fix the quote, or document it in data/lore_quote_exceptions.json)")
    print(f"lore quotes: {tot} quotes on {len(PAGES)} pages ({mode}); " + ", ".join(f"{k} {n}" for k, n in sorted(kinds.items())) + f"; {len(bad)} problems")
    for b in bad[:30]:
        print("  " + b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
