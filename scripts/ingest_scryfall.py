#!/usr/bin/env python3
"""Resumable, idempotent Scryfall ingestion for the MTG Companion knowledge base.

Source of truth: Scryfall `oracle_cards` bulk data (one object per Oracle ID).
Every run:
  1. Fetches bulk-data metadata from https://api.scryfall.com/bulk-data (polite
     User-Agent/Accept headers, >=100 ms between API requests) and downloads the
     oracle_cards file to a local cache (re-used if already downloaded).
  2. Builds the target universe: paper (non-digital) game cards, excluding tokens,
     emblems, art-series, planar/scheme/vanguard cards.
  3. Orders it by priority: data/priority_cards.txt first, then Commander-legal
     cards by ascending `edhrec_rank`, then other Commander-legal cards, then the
     rest (banned / not legal) alphabetically.
  4. Keeps every card already listed in data/card_index.csv and adds the next
     --batch cards (or up to --target total).
  5. Regenerates ALL shard files (cards/<L>/<LL>.md) from fresh Oracle data, the
     CSV index, Card Index.md, data/ingest_state.json, and the auto-generated
     sections of README.md and Progress Tracker.md.
Re-running with --batch 0 just refreshes existing entries (Oracle errata etc.).

Usage:
  python3 scripts/ingest_scryfall.py --batch 2000
  python3 scripts/ingest_scryfall.py --target 10000
  python3 scripts/ingest_scryfall.py --batch 0          # refresh only
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import json
import os
import re
import sys
import time
import unicodedata
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS_DIR = ROOT / "cards"
DATA_DIR = ROOT / "data"
INDEX_CSV = DATA_DIR / "card_index.csv"
STATE_FILE = DATA_DIR / "ingest_state.json"
PRIORITY_FILE = DATA_DIR / "priority_cards.txt"
CATEGORIES_FILE = DATA_DIR / "categories.json"
CARD_INDEX_MD = ROOT / "Card Index.md"
README = ROOT / "README.md"
TRACKER = ROOT / "Progress Tracker.md"
DEFAULT_CACHE = Path(os.environ.get("SCRYFALL_CACHE", ROOT / ".cache"))

API = "https://api.scryfall.com"
HEADERS = {
    "User-Agent": "GrokBotMTGCompanion/1.0 (+https://github.com/corymstover/GrokBotMTGCompanion; knowledge-base ingestion)",
    "Accept": "application/json;q=0.9,*/*;q=0.8",
}
REQUEST_DELAY = 0.1  # seconds between Scryfall requests (Scryfall asks for 50-100 ms)

EXCLUDED_LAYOUTS = {"token", "double_faced_token", "art_series", "emblem",
                    "vanguard", "scheme", "planar", "reversible_card"}
COLOR_NAMES = {"W": "White", "U": "Blue", "B": "Black", "R": "Red", "G": "Green"}
CSV_FIELDS = ["name", "oracle_id", "shard", "anchor", "edhrec_rank", "color_identity",
              "type_line", "commander_legality", "game_changer", "batch"]
UNIVERSE_TARGET_LABEL = "~33,000 (Grok working total)"

_last_request = 0.0


def http_get(url: str) -> bytes:
    global _last_request
    wait = REQUEST_DELAY - (time.time() - _last_request)
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = resp.read()
    _last_request = time.time()
    return data


def get_bulk(cache_dir: Path, bulk_file: str | None) -> tuple[list[dict], str]:
    """Return (cards, bulk_updated_at)."""
    if bulk_file:
        path = Path(bulk_file)
        updated = dt.datetime.fromtimestamp(path.stat().st_mtime, dt.timezone.utc).isoformat()
    else:
        meta = json.loads(http_get(f"{API}/bulk-data/oracle-cards"))
        updated = meta["updated_at"]
        uri = meta.get("jsonl_download_uri") or meta.get("download_uri")
        cache_dir.mkdir(parents=True, exist_ok=True)
        path = cache_dir / Path(uri.split("?")[0]).name
        if not path.exists():
            for old in cache_dir.glob("oracle-cards-*"):
                old.unlink()
            print(f"Downloading {uri} ...", file=sys.stderr)
            tmp = path.with_suffix(".part")
            tmp.write_bytes(http_get(uri))
            tmp.rename(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as fh:
        head = fh.read(1)
        fh.seek(0)
        if head == "[":
            cards = json.load(fh)
        else:
            cards = [json.loads(line) for line in fh if line.strip()]
    return cards, updated


# ---------------------------------------------------------------- helpers
def ascii_key(name: str) -> str:
    n = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    return "".join(ch for ch in n if ch.isalnum())


SHARD_MAX = 350  # max cards per shard file at FULL universe coverage (keeps files GitHub-renderable)
_PREFIX_COUNTS: Counter = Counter()


def configure_shards(universe: list[dict]) -> None:
    """Shard keys depend only on the full universe, so a card's shard never moves as ingestion grows."""
    _PREFIX_COUNTS.clear()
    for c in universe:
        k = ascii_key(c["name"])
        for n in range(2, 6):
            _PREFIX_COUNTS[k[:n]] += 1


def shard_for(name: str) -> str:
    k = ascii_key(name)
    if not k:
        return "_/__.md"
    if not k[0].isalpha():
        return "0-9/0-9.md"
    n = 2
    while n < 5 and _PREFIX_COUNTS.get(k[:n], 0) > SHARD_MAX and len(k) > n:
        n += 1
    pre = k[:n] if len(k) >= 2 else k + "_"
    return f"{k[0].upper()}/{pre}.md"


def gh_anchor(text: str) -> str:
    """Approximate GitHub's heading-anchor algorithm."""
    t = text.strip().lower()
    t = re.sub(r"[^\w\- ]", "", t, flags=re.UNICODE)
    return t.replace(" ", "-")


def ci_label(ci: list[str]) -> str:
    if not ci:
        return "Colorless"
    return "".join(ci) + " (" + ", ".join(COLOR_NAMES[c] for c in ci) + ")"


def quote(text: str) -> str:
    if not text:
        return "  > *(no rules text)*"
    return "\n".join("  > " + (ln.replace("<", "&lt;") if ln else "") for ln in text.split("\n"))


def flavor(text: str) -> str:
    return "\n".join("  > *" + ln.replace("*", "\\*").replace("<", "&lt;").strip() + "*" if ln.strip() else "  >"
                     for ln in text.split("\n"))


def commander_eligibility(c: dict) -> str:
    faces = c.get("card_faces") or [c]
    front_type = faces[0].get("type_line") or c.get("type_line", "")
    text = c.get("oracle_text") or " ".join(f.get("oracle_text", "") for f in faces)
    if "can be your commander" in text.lower():
        return "Yes (Oracle text: \"can be your commander\")"
    if "Legendary" in front_type and "Creature" in front_type:
        return "Yes (legendary creature)"
    if "Background" in front_type and "Legendary" in front_type:
        return "Only alongside a commander with *Choose a Background*"
    return "No"


def pairing_notes(c: dict) -> list[str]:
    kws = set(c.get("keywords") or [])
    out = []
    for kw in ("Partner", "Partner with", "Friends forever", "Choose a Background", "Doctor's companion", "Companion"):
        if kw in kws:
            out.append(kw)
    txt = (c.get("oracle_text") or "")
    if not out and re.search(r"^Partner\b", txt, re.M):
        out.append("Partner")
    return out


def stat_line(obj: dict) -> str:
    parts = []
    if "power" in obj:
        parts.append(f"**P/T:** {obj['power']}/{obj['toughness']}")
    if "loyalty" in obj:
        parts.append(f"**Loyalty:** {obj['loyalty']}")
    if "defense" in obj:
        parts.append(f"**Defense:** {obj['defense']}")
    return " · ".join(parts)


def render_entry(c: dict, bulk_date: str) -> str:
    L = [f"### {c['name']}", ""]
    faces = c.get("card_faces")
    mv = c.get("cmc", 0)
    mv = int(mv) if float(mv).is_integer() else mv
    if faces and any("oracle_text" in f for f in faces):
        L.append(f"- **Layout:** {c['layout']} · **MV:** {mv} · **Color identity:** {ci_label(c.get('color_identity', []))}")
        for i, f in enumerate(faces, 1):
            cost = f.get("mana_cost") or "—"
            L.append(f"- **Face {i}: {f.get('name')}** — {cost} — {f.get('type_line', '')}")
            st = stat_line(f)
            if st:
                L.append(f"  - {st}")
            L.append(quote(f.get("oracle_text", "")))
            if f.get("flavor_text"):
                L.append(f"  - *Flavor text ({c.get('set', '').upper()} printing):*")
                L.append(flavor(f["flavor_text"]))
    else:
        cost = c.get("mana_cost") or "—"
        L.append(f"- **Mana cost:** {cost} · **MV:** {mv} · **Color identity:** {ci_label(c.get('color_identity', []))}")
        L.append(f"- **Type:** {c.get('type_line', '')}")
        st = stat_line(c)
        if st:
            L.append(f"- {st}")
        L.append("- **Oracle text:**")
        L.append(quote(c.get("oracle_text", "")))
    if c.get("flavor_text"):
        L.append(f"- **Flavor text** ({c.get('set', '').upper()} printing):")
        L.append(flavor(c["flavor_text"]))
    if c.get("keywords"):
        L.append(f"- **Keywords:** {', '.join(c['keywords'])}")
    leg = c.get("legalities", {}).get("commander", "not_legal").replace("_", " ")
    rank = f"#{c['edhrec_rank']}" if c.get("edhrec_rank") else "unranked"
    notes = [f"Commander format: **{leg}**", f"EDHREC rank: {rank}",
             f"Game Changer: {'**yes**' if c.get('game_changer') else 'no'}",
             f"Can be commander: {commander_eligibility(c)}"]
    pn = pairing_notes(c)
    if pn:
        notes.append("Pairing: " + ", ".join(pn))
    if c.get("reserved"):
        notes.append("Reserved List")
    L.append("- **Commander notes:** " + " · ".join(notes))
    flags = [f"[Scryfall]({c['scryfall_uri'].split('?')[0]})",
             f"oracle_id `{c['oracle_id']}`",
             f"printing: {c.get('set', '').upper()} #{c.get('collector_number', '')} ({c.get('released_at', '')})",
             f"[rulings]({c.get('rulings_uri', '')})",
             f"source: Scryfall oracle_cards bulk {bulk_date[:10]}", "status: ✅ verified (Scryfall Oracle)"]
    L.append("- **Source flags:** " + " · ".join(flags))
    L.append("")
    return "\n".join(L)


def in_universe(c: dict) -> bool:
    """Paper Magic cards. The printing Scryfall picks may be digital (e.g. Strip Mine -> VMA),
    so a card also qualifies if it is legal/banned/restricted in a paper eternal format."""
    if "paper" in (c.get("games") or []) and not c.get("digital"):
        return True
    leg = c.get("legalities") or {}
    return any(leg.get(f, "not_legal") != "not_legal" for f in ("vintage", "legacy", "commander"))


# ---------------------------------------------------------------- main logic
def load_index() -> dict[str, dict]:
    if not INDEX_CSV.exists():
        return {}
    with INDEX_CSV.open(encoding="utf-8", newline="") as fh:
        return {r["oracle_id"]: r for r in csv.DictReader(fh)}


def priority_names() -> list[str]:
    if not PRIORITY_FILE.exists():
        return []
    out = []
    for ln in PRIORITY_FILE.read_text(encoding="utf-8").splitlines():
        ln = ln.split("#", 1)[0].strip()
        if ln:
            out.append(ln)
    return out


def replace_block(path: Path, tag: str, content: str) -> None:
    start, end = f"<!-- {tag}:START -->", f"<!-- {tag}:END -->"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    if start not in text:
        return
    pre, rest = text.split(start, 1)
    _, post = rest.split(end, 1)
    path.write_text(pre + start + "\n" + content.rstrip() + "\n" + end + post, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--batch", type=int, default=None, help="number of NEW cards to add (default: state next_batch_size)")
    ap.add_argument("--target", type=int, default=None, help="grow the ingested total up to this number")
    ap.add_argument("--bulk-file", default=None, help="use a local oracle_cards .json/.jsonl(.gz) instead of downloading")
    ap.add_argument("--cache-dir", default=str(DEFAULT_CACHE))
    ap.add_argument("--batch-label", default=None, help="label stored in the CSV for newly added cards")
    args = ap.parse_args()

    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}
    cards, bulk_updated = get_bulk(Path(args.cache_dir), args.bulk_file)

    universe = [c for c in cards if c.get("layout") not in EXCLUDED_LAYOUTS and in_universe(c)]
    configure_shards(universe)
    by_id = {c["oracle_id"]: c for c in universe}
    by_name = {c["name"].lower(): c for c in universe}
    for c in universe:  # allow face names (e.g. "Fire") to resolve
        for f in c.get("card_faces") or []:
            by_name.setdefault(f["name"].lower(), c)

    def is_legal(c):
        return c.get("legalities", {}).get("commander") == "legal"

    ordered: list[dict] = []
    missing_priority = []
    for n in priority_names():
        c = by_name.get(n.lower())
        if c:
            ordered.append(c)
        else:
            missing_priority.append(n)
    ordered += sorted([c for c in universe if is_legal(c) and c.get("edhrec_rank")], key=lambda c: c["edhrec_rank"])
    ordered += sorted([c for c in universe if is_legal(c) and not c.get("edhrec_rank")], key=lambda c: ascii_key(c["name"]))
    ordered += sorted([c for c in universe if not is_legal(c)], key=lambda c: ascii_key(c["name"]))
    seen, queue = set(), []
    for c in ordered:
        if c["oracle_id"] not in seen:
            seen.add(c["oracle_id"])
            queue.append(c)

    index = load_index()
    dropped = [oid for oid in index if oid not in by_id]  # e.g. Oracle ID merged/removed upstream
    for oid in dropped:
        index.pop(oid)
    n_before = len(index)

    batch = args.batch if args.batch is not None else state.get("next_batch_size", 2000)
    if args.target is not None:
        batch = max(0, args.target - n_before)
    today = dt.date.today().isoformat()
    label = args.batch_label or f"{today}-b{state.get('batches_run', 0) + 1}"
    added = []
    for c in queue:
        if len(added) >= batch:
            break
        if c["oracle_id"] not in index:
            index[c["oracle_id"]] = {"batch": label}
            added.append(c)

    # ---- render shards
    shards: dict[str, list[dict]] = defaultdict(list)
    for oid in index:
        c = by_id[oid]
        shards[shard_for(c["name"])].append(c)
    if CARDS_DIR.exists():
        for old in CARDS_DIR.rglob("*.md"):
            if old.name != "README.md":
                old.unlink()
    rows = []
    for shard, cs in sorted(shards.items()):
        cs.sort(key=lambda c: (ascii_key(c["name"]), c["name"]))
        p = CARDS_DIR / shard
        p.parent.mkdir(parents=True, exist_ok=True)
        prefix = shard.split("/")[1][:-3]
        head = [f"# Cards — `{prefix}`", "",
                f"> Auto-generated by `scripts/ingest_scryfall.py` from Scryfall Oracle bulk data ({bulk_updated[:10]}). "
                "Do not hand-edit entries; edit the script or `data/` inputs and re-run. "
                "Format: see [Card Data Conventions](../../Card%20Data%20Conventions.md). "
                "Index: [Card Index](../../Card%20Index.md).", "",
                f"**{len(cs)} cards in this shard.**", "", "## Contents", ""]
        anchors = Counter()
        body = []
        for c in cs:
            a = gh_anchor(c["name"])
            if anchors[a]:
                a2 = f"{a}-{anchors[a]}"
            else:
                a2 = a
            anchors[a] += 1
            head.append(f"- [{c['name']}](#{a2})")
            body.append(render_entry(c, bulk_updated))
            r = index[c["oracle_id"]]
            rows.append({"name": c["name"], "oracle_id": c["oracle_id"], "shard": f"cards/{shard}",
                         "anchor": a2, "edhrec_rank": c.get("edhrec_rank") or "",
                         "color_identity": "".join(c.get("color_identity", [])) or "C",
                         "type_line": c.get("type_line", ""),
                         "commander_legality": c.get("legalities", {}).get("commander", ""),
                         "game_changer": "1" if c.get("game_changer") else "0",
                         "batch": r.get("batch", label)})
        p.write_text("\n".join(head) + "\n\n## Entries\n\n" + "\n".join(body), encoding="utf-8")

    rows.sort(key=lambda r: (ascii_key(r["name"]), r["name"]))
    DATA_DIR.mkdir(exist_ok=True)
    with INDEX_CSV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CSV_FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    total = len(rows)
    remaining = [c for c in queue if c["oracle_id"] not in index]
    next_target = remaining[0] if remaining else None
    ranks = [int(r["edhrec_rank"]) for r in rows if r["edhrec_rank"]]
    contiguous = 0  # highest N such that all ranked+legal cards with rank <= N are ingested
    for c in queue:
        if not (is_legal(c) and c.get("edhrec_rank")):
            continue
        if c["oracle_id"] in index:
            contiguous = c["edhrec_rank"]
        else:
            break
    hist = state.get("history", [])
    if added or not hist:
        hist.append({"date": today, "label": label, "added": len(added), "total": total})
    state.update({
        "schema": 1,
        "source": "scryfall oracle_cards bulk",
        "bulk_updated_at": bulk_updated,
        "universe_size": len(queue),
        "universe_definition": "Scryfall oracle_cards that exist in paper (paper printing, or legal/banned/restricted in Vintage/Legacy/Commander); excludes Arena/Alchemy-only cards and token/emblem/art_series/planar/scheme/vanguard/reversible layouts",
        "ingested_total": total,
        "batches_run": state.get("batches_run", 0) + (1 if added else 0),
        "next_batch_size": state.get("next_batch_size", 2000),
        "last_run": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "last_added": len(added),
        "ingested_edhrec_rank_contiguous_through": contiguous,
        "max_ingested_edhrec_rank": max(ranks) if ranks else None,
        "next_target": ({"name": next_target["name"], "oracle_id": next_target["oracle_id"],
                         "edhrec_rank": next_target.get("edhrec_rank"),
                         "commander_legality": next_target["legalities"].get("commander")} if next_target else None),
        "missing_priority_names": missing_priority,
        "dropped_oracle_ids": dropped,
        "shards": len(shards),
        "history": hist[-50:],
    })
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    write_card_index(rows, by_id, state, shards)
    write_dashboard(state)
    print(json.dumps({k: state[k] for k in ("ingested_total", "last_added", "universe_size",
                                             "ingested_edhrec_rank_contiguous_through", "next_target",
                                             "missing_priority_names", "shards")}, indent=2))
    return 0


def link(r: dict, rel: str = "") -> str:
    path = rel + r["shard"].replace(" ", "%20")
    return f"[{r['name']}]({path}#{r['anchor']})"


def write_card_index(rows, by_id, state, shards):
    total = state["ingested_total"]
    uni = state["universe_size"]
    by_letter = Counter(r["shard"].split("/")[1] for r in rows)
    ci = Counter(r["color_identity"] for r in rows)
    legal = Counter(r["commander_legality"] for r in rows)
    gc = [r for r in rows if r["game_changer"] == "1"]
    cats = json.loads(CATEGORIES_FILE.read_text()) if CATEGORIES_FILE.exists() else {}
    name_map = {r["name"].lower(): r for r in rows}
    L = ["# Card Index", "",
         "> **Auto-generated** by `scripts/ingest_scryfall.py` — do not hand-edit. "
         "Tracks which cards have full entries. Machine-readable index: [`data/card_index.csv`](data/card_index.csv). "
         "State: [`data/ingest_state.json`](data/ingest_state.json).", "",
         "## Contents", "- [Totals](#totals)", "- [Shards by letter](#shards-by-letter)",
         "- [Category trackers](#category-trackers)", "- [Game Changers ingested](#game-changers-ingested)",
         "- [Top 100 by EDHREC rank](#top-100-by-edhrec-rank)", "- [How to find a card](#how-to-find-a-card)", "",
         "## Totals", "",
         f"| Metric | Value |", "|---|---|",
         f"| Cards with full entries | **{total:,}** |",
         f"| Target universe (paper cards, Scryfall Oracle) | {uni:,} ({total / uni:.1%} complete) |",
         f"| EDHREC-rank coverage (all Commander-legal cards ranked ≤ N ingested) | N = {state['ingested_edhrec_rank_contiguous_through']:,} |",
         f"| Commander legality of ingested | " + ", ".join(f"{k}: {v:,}" for k, v in sorted(legal.items())) + " |",
         f"| Game Changers ingested | {len(gc)} |",
         f"| Shard files | {state['shards']} |",
         f"| Scryfall bulk data timestamp | {state['bulk_updated_at']} |", "",
         "### By color identity", "", "| Identity | Cards |", "|---|---|"]
    for k, v in sorted(ci.items(), key=lambda kv: (len(kv[0]) if kv[0] != 'C' else 0, kv[0])):
        L.append(f"| {k} | {v:,} |")
    L += ["", "## Shards by letter", "",
          "Cards are stored in `cards/<LETTER>/<prefix>.md` (accents stripped, punctuation ignored; 2-letter prefix, deepened to 3–5 letters "
          f"where the full universe would exceed {SHARD_MAX} cards in one file).", "",
          "| Letter | Cards | Shard files |", "|---|---|---|"]
    letter_files = defaultdict(list)
    for s in sorted(shards):
        letter_files[s.split("/")[0]].append(s)
    for letter in sorted(letter_files):
        files = ", ".join(f"[{s.split('/')[1][:-3]}](cards/{s})" for s in letter_files[letter])
        cnt = sum(len(shards[s]) for s in letter_files[letter])
        L.append(f"| {letter} | {cnt:,} | {files} |")
    L += ["", "## Category trackers", "",
          "Curated in [`data/categories.json`](data/categories.json) (mirrors the categories of the original Grok project). "
          "✅ = full entry present; ⬜ = not yet ingested.", ""]
    for cat, names in cats.items():
        have = sum(1 for n in names if n.lower() in name_map)
        L += [f"### {cat} ({have}/{len(names)})", ""]
        L.append(" · ".join(("✅ " + link(name_map[n.lower()])) if n.lower() in name_map else f"⬜ {n}" for n in names))
        L.append("")
    L += ["## Game Changers ingested", "",
          "Cards Scryfall flags as `game_changer` (used by the official Commander Brackets system). See [EDH Standards](EDH%20Standards.md).", ""]
    L.append(" · ".join(link(r) for r in sorted(gc, key=lambda r: r["name"])) or "*(none yet)*")
    L += ["", "## Top 100 by EDHREC rank", "", "| Rank | Card | Identity | Type |", "|---|---|---|---|"]
    for r in sorted([r for r in rows if r["edhrec_rank"]], key=lambda r: int(r["edhrec_rank"]))[:100]:
        L.append(f"| {r['edhrec_rank']} | {link(r)} | {r['color_identity']} | {r['type_line']} |")
    L += ["", "## How to find a card", "",
          "1. Strip accents and punctuation from the name and lower-case it → take the first two letters → `cards/<FIRST>/<first two>.md`; "
          "very common prefixes are split one letter deeper (e.g. `cards/T/the.md`, `cards/M/mag.md`) — see the shard table above. "
          "Names starting with a digit live in `cards/0-9/0-9.md`.",
          "2. Or search [`data/card_index.csv`](data/card_index.csv) (columns: " + ", ".join(CSV_FIELDS) + ").", ""]
    CARD_INDEX_MD.write_text("\n".join(L), encoding="utf-8")


def bar(frac: float, width: int = 30) -> str:
    n = round(frac * width)
    return "█" * n + "░" * (width - n)


def write_dashboard(state):
    total, uni = state["ingested_total"], state["universe_size"]
    nt = state.get("next_target") or {}
    block = "\n".join([
        f"**Cards with full Scryfall-verified entries: {total:,} / {uni:,}** ({total / uni:.1%}) — working target {UNIVERSE_TARGET_LABEL}",
        "",
        f"`{bar(total / uni)}`",
        "",
        f"- EDHREC coverage: every Commander-legal card ranked ≤ **{state['ingested_edhrec_rank_contiguous_through']:,}** has an entry",
        f"- Last batch: `{state['history'][-1]['label']}` (+{state['history'][-1]['added']:,} cards) · last run {state['last_run']} · Scryfall bulk {state['bulk_updated_at'][:10]}",
        f"- Next card target: **{nt.get('name', '—')}** (EDHREC rank {nt.get('edhrec_rank', '—')}) · default batch {state['next_batch_size']:,}",
    ])
    replace_block(README, "CARD-STATS", block)
    replace_block(TRACKER, "CARD-STATS", block)


if __name__ == "__main__":
    sys.exit(main())
