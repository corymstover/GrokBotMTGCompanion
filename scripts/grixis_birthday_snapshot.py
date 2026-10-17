#!/usr/bin/env python3
"""Fresh Birthday authority snapshot (ChatGPT cycle 74).

This is intentionally separate from data/grixis/dev_snapshot_lock.json.  The frozen
snap-20261016 development inputs remain immutable for A-F reproduction; this script
collects current authority/evidence into data/grixis/birthday_authority and computes
explicit deltas against the frozen snapshot immediately before M5 acceptance.

Hard authority inputs: Scryfall oracle/default/rulings, Wizards Comprehensive Rules,
and Wizards' Banned & Restricted page.  Evidence feeds: EDHREC, Commander Spellbook,
and EDHTop16.  Evidence-feed absence is recorded, never fabricated.  Any unexpected
Commander-legality failure in the 62 canonical project lists is a hard blocker.

Usage:
  SCRYFALL_BIRTHDAY_SNAPSHOT=1 SCRYFALL_CACHE=.cache/birthday \
    python scripts/grixis_birthday_snapshot.py --build
  python scripts/grixis_birthday_snapshot.py --check
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402

VERSION = 1
OUT = ROOT / "data" / "grixis" / "birthday_authority"
CACHE = Path(os.environ.get("BIRTHDAY_CACHE", ROOT / ".cache" / "birthday"))
FROZEN = Path(os.environ.get("FROZEN_CACHE", ROOT / ".cache" / "frozen"))
LOCK = ROOT / "data" / "grixis" / "dev_snapshot_lock.json"
RULES_LOCK = ROOT / "data" / "grixis" / "dev_rules_lock.json"
PENDING = ROOT / "data" / "grixis_pending.json"
EXCEPTIONS = ROOT / "data" / "grixis" / "exceptions.json"
HIST_EVID = ROOT / "data" / "grixis" / "evidence"
OLD_SPELLBOOK = ROOT / "data" / "grixis" / "candidates" / "spellbook_almost.json"
OLD_TOUR = ROOT / "data" / "grixis" / "candidates" / "tournament"

SCRYFALL_API = "https://api.scryfall.com"
RULES_PAGE = "https://magic.wizards.com/en/rules"
BANNED_PAGE = "https://magic.wizards.com/en/banned-restricted-list"
EDHREC_BASE = "https://json.edhrec.com/pages/commanders/{}.json"
UA = "GrokBotMTGCompanion/1.0 (+https://github.com/corymstover/GrokBotMTGCompanion; Birthday authority snapshot)"
HEADERS = {"User-Agent": UA, "Accept": "application/json,text/html;q=0.9,*/*;q=0.8"}
SKIP_EDHREC_LISTS = {"newcards", "topcommanders", "newcommanders"}


def sha_bytes(b: bytes) -> str:
    return "sha256:" + hashlib.sha256(b).hexdigest()


def sha_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


def canonical_json_hash(obj) -> str:
    return sha_bytes(json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())


def get_bytes(url: str, timeout=120) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def download(url: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers=HEADERS)
    tmp = path.with_suffix(path.suffix + ".part")
    with urllib.request.urlopen(req, timeout=300) as r, tmp.open("wb") as f:
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            f.write(b)
    tmp.replace(path)


def source_record(url: str, path: Path, **extra):
    return {"status": "collected", "url": url, "file": path.name,
            "sha256": sha_file(path), "bytes": path.stat().st_size, **extra}


def fetch_bulk(kind: str):
    meta_url = f"{SCRYFALL_API}/bulk-data/{kind}"
    meta_raw = get_bytes(meta_url)
    meta = json.loads(meta_raw)
    uri = meta.get("jsonl_download_uri") or meta.get("download_uri")
    if not uri:
        raise RuntimeError(f"Scryfall {kind}: no download URI")
    name = Path(urllib.parse.urlsplit(uri).path).name
    path = CACHE / name
    download(uri, path)
    rec = source_record(uri, path, kind=kind, metadata_url=meta_url,
                        metadata_sha256=sha_bytes(meta_raw), updated_at=meta.get("updated_at"),
                        scryfall_id=meta.get("id"), content_type=meta.get("content_type"))
    return rec, path


def _open_text(path: Path):
    return gzip.open(path, "rt", encoding="utf-8") if path.suffix == ".gz" else path.open("rt", encoding="utf-8")


def iter_objects(path: Path):
    with _open_text(path) as f:
        first = f.read(1)
        f.seek(0)
        if first == "[":
            for x in json.load(f):
                yield x
        else:
            for line in f:
                line = line.strip().rstrip(",")
                if line.startswith("{"):
                    yield json.loads(line)


def oracle_sig(c: dict):
    faces = []
    for f in c.get("card_faces") or []:
        faces.append({k: f.get(k) for k in ("name", "mana_cost", "type_line", "oracle_text", "color_indicator", "colors")})
    return {
        "name": c.get("name"), "layout": c.get("layout"), "mana_cost": c.get("mana_cost"),
        "cmc": c.get("cmc"), "type_line": c.get("type_line"), "oracle_text": c.get("oracle_text"),
        "color_identity": c.get("color_identity"), "keywords": c.get("keywords"),
        "commander_legality": (c.get("legalities") or {}).get("commander"),
        "released_at": c.get("released_at"), "set": c.get("set"), "faces": faces,
    }


def oracle_index(path: Path):
    out = {}
    for c in iter_objects(path):
        oid = c.get("oracle_id")
        if oid:
            out[oid] = oracle_sig(c)
    return out


def oracle_delta(old_path: Path, new_path: Path):
    old, new = oracle_index(old_path), oracle_index(new_path)
    old_ids, new_ids = set(old), set(new)
    added = sorted(new_ids - old_ids, key=lambda x: (new[x].get("name") or "").lower())
    removed = sorted(old_ids - new_ids, key=lambda x: (old[x].get("name") or "").lower())
    changed, legal = [], []
    for oid in sorted(old_ids & new_ids):
        if old[oid] == new[oid]:
            continue
        fields = sorted(k for k in new[oid] if old[oid].get(k) != new[oid].get(k))
        row = {"oracle_id": oid, "name": new[oid].get("name"), "fields": fields}
        changed.append(row)
        if old[oid].get("commander_legality") != new[oid].get("commander_legality"):
            legal.append({"oracle_id": oid, "name": new[oid].get("name"),
                          "from": old[oid].get("commander_legality"), "to": new[oid].get("commander_legality")})
    return {
        "old_count": len(old), "new_count": len(new),
        "added": [{"oracle_id": x, **new[x]} for x in added],
        "removed": [{"oracle_id": x, **old[x]} for x in removed],
        "changed": changed, "commander_legality_changes": legal,
        "counts": {"added": len(added), "removed": len(removed), "changed": len(changed),
                   "commander_legality_changes": len(legal)},
    }, new


def rulings_delta(old_path: Path, new_path: Path, oracle_by_id: dict):
    def rows(path):
        out = set()
        for r in iter_objects(path):
            out.add((r.get("oracle_id"), r.get("published_at"), r.get("comment")))
        return out
    a, b = rows(old_path), rows(new_path)
    add, rem = b - a, a - b
    affected = sorted({x[0] for x in add | rem if x[0]})
    return {"old_count": len(a), "new_count": len(b), "added": len(add), "removed": len(rem),
            "affected_cards": [{"oracle_id": oid, "name": (oracle_by_id.get(oid) or {}).get("name")} for oid in affected]}


def strip_html(raw: bytes) -> str:
    t = raw.decode("utf-8", errors="replace")
    t = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", t, flags=re.I | re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def fetch_rules():
    page = get_bytes(RULES_PAGE)
    page_path = CACHE / "wizards-rules-page.html"
    page_path.write_bytes(page)
    text = page.decode("utf-8", errors="replace")
    links = re.findall(r'href=["\']([^"\']+\.txt(?:\?[^"\']*)?)["\']', text, flags=re.I)
    links += re.findall(r'https://[^"\'<> ]*MagicCompRules[^"\'<> ]*\.txt', text, flags=re.I)
    links = [urllib.parse.urljoin(RULES_PAGE, html.unescape(x)) for x in links]
    links = list(dict.fromkeys(links))
    if not links:
        return {"status": "blocked", "page_url": RULES_PAGE, "page_sha256": sha_file(page_path),
                "reason": "official Rules page exposed no Comprehensive Rules TXT link"}, None
    url = urllib.parse.quote(next((x for x in links if "MagicCompRules" in x), links[0]), safe=":/?=&%")
    path = CACHE / Path(urllib.parse.urlsplit(url).path).name
    download(url, path)
    raw = path.read_bytes()
    body = raw.decode("utf-8-sig", errors="replace")
    m = re.search(r"These rules are effective as of ([^.]+)\.", body[:5000], flags=re.I)
    rec = source_record(url, path, page_url=RULES_PAGE, page_sha256=sha_file(page_path),
                        effective_date=m.group(1).strip() if m else None)
    return rec, path


def fetch_official_banned():
    raw = get_bytes(BANNED_PAGE)
    path = CACHE / "wizards-banned-restricted.html"
    path.write_bytes(raw)
    txt = strip_html(raw)
    has_commander = "Commander Banned Cards" in txt and "Lutri, the Spellchaser" in txt
    return source_record(BANNED_PAGE, path, commander_section_detected=has_commander,
                         normalized_text_sha256=sha_bytes(txt.encode()))


def eslug(name: str) -> str:
    s = name.split(" // ")[0].lower().replace("'", "").replace(",", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def normalize_edhrec_page(d: dict):
    rows = {}
    for cl in (d.get("container") or {}).get("json_dict", {}).get("cardlists", []):
        if cl.get("tag") in SKIP_EDHREC_LISTS:
            continue
        for v in cl.get("cardviews", []):
            if not v.get("name"):
                continue
            rows.setdefault(v["name"], {k: v.get(k) for k in ("num_decks", "potential_decks", "synergy", "lift", "trend_zscore")})
    return rows


def fetch_edhrec():
    cache = CACHE / "edhrec"
    cache.mkdir(parents=True, exist_ok=True)
    pend = json.loads(PENDING.read_text(encoding="utf-8"))["decks"]
    decks, compact = {}, {}
    for did, v in sorted(ga.summary().items(), key=lambda kv: kv[1]["slug"]):
        slug, cmds = v["slug"], v["commanders"]
        candidates = []
        if len(cmds) > 1:
            candidates.append(("combined_page", "-".join(sorted(eslug(c) for c in cmds))))
        candidates += [("single_page", eslug(c)) for c in cmds]
        got, errs = [], []
        for method, pslug in candidates:
            if got and got[0]["method"] == "combined_page":
                break
            url = EDHREC_BASE.format(pslug)
            try:
                raw = get_bytes(url, timeout=60)
                d = json.loads(raw)
                if not (d.get("container") or {}).get("json_dict"):
                    raise ValueError("missing container.json_dict")
                path = cache / f"commanders__{pslug}.json"
                path.write_bytes(raw)
                got.append({"method": method, "page": pslug, "url": url, "sha256": sha_file(path),
                            "bytes": len(raw), "rows": len(normalize_edhrec_page(d)), "data": normalize_edhrec_page(d)})
                if method == "combined_page":
                    break
            except Exception as e:
                errs.append({"page": pslug, "error": f"{type(e).__name__}: {e}"[:300]})
        if got and got[0]["method"] == "combined_page":
            got = got[:1]
            method = "combined_page"
        elif got:
            method = "pooled" if len(got) > 1 else "single_page"
        else:
            method = "none"
        rid = ga.registry_id(did)
        expected = did in pend or rid in pend
        status = "collected" if got else ("expected_unavailable" if expected else "unavailable")
        old_path = HIST_EVID / f"{slug}.json"
        old_names = set()
        if old_path.exists():
            old = json.loads(old_path.read_text(encoding="utf-8"))
            old_names = {x["card"] for x in old.get("vectors", []) if x.get("edhrec") is not None}
        now_names = set().union(*(set(x["data"]) for x in got)) if got else set()
        decks[slug] = {"status": status, "deck_id": rid, "method": method,
                       "pages": [{k: x[k] for k in ("page", "url", "sha256", "bytes", "rows")} for x in got],
                       "errors": errs, "historical_raw_available": False,
                       "historical_comparison": "committed derived M3 evidence only; exact 2026-10-16 EDHREC raw pages are lost",
                       "cardview_names": len(now_names), "derived_added_names": sorted(now_names - old_names),
                       "derived_removed_names": sorted(old_names - now_names)}
        compact[slug] = {"deck_id": rid, "method": method,
                         "pages": [{"page": x["page"], "sha256": x["sha256"], "rows": x["data"]} for x in got]}
        time.sleep(0.12)
    blob = json.dumps({"schema_version": 1, "retrieved": dt.date.today().isoformat(), "decks": compact},
                      ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    cp = OUT / "edhrec_current.json.gz"
    cp.write_bytes(gzip.compress(blob, compresslevel=9, mtime=0))
    return {"source": EDHREC_BASE.format("<commander-slug>"), "status": "collected",
            "decks": decks, "artifact": str(cp.relative_to(ROOT)), "artifact_sha256": sha_file(cp),
            "counts": {"collected": sum(x["status"] == "collected" for x in decks.values()),
                       "expected_unavailable": sum(x["status"] == "expected_unavailable" for x in decks.values()),
                       "unavailable": sum(x["status"] == "unavailable" for x in decks.values())}}


def preferred_name_index(oracle_by_id: dict):
    """Resolve duplicate Scryfall names to the actual game card, not a same-name token/emblem.

    Oracle bulk can contain separate Oracle IDs with identical English names (for example
    Thundertrap Trainer and its offspring token).  Canonical deck legality must resolve the
    playable object.  Non-game layouts/type lines therefore sort after ordinary cards;
    legality is only a secondary tie-breaker and never overrides project exceptions.
    """
    out = {}
    non_game_layouts = {"token", "double_faced_token", "emblem", "art_series", "vanguard", "scheme", "planar"}
    def rank(c):
        t = c.get("type_line") or ""
        nongame = c.get("layout") in non_game_layouts or t.startswith(("Token ", "Emblem"))
        ordinary_legality = c.get("commander_legality") in ("legal", "banned", "restricted")
        return (1 if nongame else 0, 0 if ordinary_legality else 1, c.get("set") or "")
    for oid, c in oracle_by_id.items():
        name = c.get("name")
        if not name:
            continue
        if name not in out or rank(c) < rank(out[name][1]):
            out[name] = (oid, c)
    return out


def fresh_deck_legality(oracle_by_id: dict):
    by_name = preferred_name_index(oracle_by_id)
    exc_rows = json.loads(EXCEPTIONS.read_text(encoding="utf-8"))["exceptions"]
    exc = {(x["deck_id"], x["card"]): x for x in exc_rows}
    rows, blockers = {}, []
    for did, v in sorted(ga.summary().items(), key=lambda kv: kv[1]["slug"]):
        rid, slug = ga.registry_id(did), v["slug"]
        text = ga.deck_block_text(slug)
        cards = []
        for line in text.splitlines():
            m = re.match(r"^\s*(\d+)x?\s+(.+?)(?:\s+\[[^]]+\])?\s*$", line)
            if m:
                cards.append((int(m.group(1)), m.group(2).strip()))
        issues, authorized = [], []
        for qty, name in cards:
            got = by_name.get(name)
            if not got:
                issues.append({"card": name, "type": "unresolved_current_oracle"})
                continue
            oid, c = got
            lg = c.get("commander_legality")
            er = exc.get((did, name)) or exc.get((rid, name))
            # Companion-only Lutri restriction is not expressible in Scryfall legalities; preserve official registry fact.
            if er and er.get("official_commander_legality") == "banned_as_companion":
                authorized.append({"card": name, "official": "banned_as_companion",
                                   "authorization": er.get("project_authorization_status")})
            elif lg != "legal":
                if er and er.get("project_authorization_status") in ("AUTHORIZED_EXCEPTION", "AUTHORIZED_FUTURE_RELEASE"):
                    authorized.append({"card": name, "official": lg, "authorization": er["project_authorization_status"],
                                       "legal_from": er.get("legal_from")})
                else:
                    issues.append({"card": name, "type": "unexpected_commander_legality", "official": lg})
        rows[slug] = {"deck_id": rid, "unexpected_issues": issues, "authorized_nonlegal": authorized,
                      "status": "pass_with_authorized_exception" if authorized and not issues else "pass" if not issues else "blocked"}
        blockers += [f"{slug}: {x}" for x in issues]
    return {"source": "Scryfall current legalities.commander + data/grixis/exceptions.json companion/future overlays",
            "decks": rows, "blockers": blockers,
            "counts": {"decks": len(rows), "blocked": sum(x["status"] == "blocked" for x in rows.values()),
                       "with_authorized_nonlegal": sum(bool(x["authorized_nonlegal"]) for x in rows.values())}}


def refresh_spellbook():
    import grixis_spellbook_almost as sp
    target = OUT / "spellbook_almost.json"
    sp.OUT = target
    sp.fetch()
    if sp.check():
        raise RuntimeError("fresh Commander Spellbook snapshot failed its existing check")
    cur = json.loads(target.read_text(encoding="utf-8"))
    old = json.loads(OLD_SPELLBOOK.read_text(encoding="utf-8")) if OLD_SPELLBOOK.exists() and OLD_SPELLBOOK.stat().st_size else {"decks": {}}
    changes = {}
    for slug in sorted(set(old.get("decks", {})) | set(cur.get("decks", {}))):
        a = {x["id"] for x in old.get("decks", {}).get(slug, {}).get("variants", [])}
        b = {x["id"] for x in cur.get("decks", {}).get(slug, {}).get("variants", [])}
        if a != b:
            changes[slug] = {"added_variant_ids": sorted(b - a), "removed_variant_ids": sorted(a - b)}
    return {"status": "collected", "source": cur.get("source"), "retrieved": cur.get("retrieved"),
            "artifact": str(target.relative_to(ROOT)), "sha256": sha_file(target),
            "decks": len(cur.get("decks", {})), "near_miss_variants": sum(len(x.get("variants", [])) for x in cur.get("decks", {}).values()),
            "delta_vs_frozen_candidate_snapshot": {"decks_changed": len(changes), "decks": changes}}


def refresh_tournament():
    import grixis_birthday_tournament as bt
    return bt.refresh(OUT)


def build():
    if os.environ.get("SCRYFALL_BIRTHDAY_SNAPSHOT") != "1":
        raise SystemExit("refusing fresh authority fetch without SCRYFALL_BIRTHDAY_SNAPSHOT=1")
    OUT.mkdir(parents=True, exist_ok=True)
    CACHE.mkdir(parents=True, exist_ok=True)
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    rules_lock = json.loads(RULES_LOCK.read_text(encoding="utf-8"))
    if lock.get("snapshot") != "snap-20261016":
        raise SystemExit(f"unexpected development snapshot {lock.get('snapshot')}")
    frozen_paths = {k: FROZEN / v for k, v in lock["files"].items()}
    for k, p in frozen_paths.items():
        if not p.exists() or sha_file(p) != lock["sha256"][k]:
            raise SystemExit(f"frozen input missing/hash mismatch: {k} {p}")
    frozen_rules = FROZEN / rules_lock["file"]
    if not frozen_rules.exists() or sha_file(frozen_rules) != rules_lock["sha256"]:
        raise SystemExit("frozen Comprehensive Rules missing/hash mismatch")

    scry = {}; fresh_paths = {}
    for kind in ("oracle-cards", "rulings", "default-cards"):
        scry[kind], fresh_paths[kind] = fetch_bulk(kind)
    odelta, oracle_now = oracle_delta(frozen_paths["oracle-cards"], fresh_paths["oracle-cards"])
    rdelta = rulings_delta(frozen_paths["rulings"], fresh_paths["rulings"], oracle_now)

    rules, rules_path = fetch_rules()
    if rules_path:
        rules["frozen_sha256"] = rules_lock["sha256"]
        rules["changed_vs_frozen"] = rules["sha256"] != rules_lock["sha256"]
    banned = fetch_official_banned()
    edhrec = fetch_edhrec()
    spellbook = refresh_spellbook()
    tournament = refresh_tournament()
    legality = fresh_deck_legality(oracle_now)

    pending = json.loads(PENDING.read_text(encoding="utf-8"))["decks"]
    names = {name: pair[1] for name, pair in preferred_name_index(oracle_now).items()}
    pending_now = {}
    for did, x in pending.items():
        pending_now[did] = {"legal_from": x["legal_from"], "cards": {n: {"present": n in names,
            "commander_legality": (names.get(n) or {}).get("commander_legality"),
            "released_at": (names.get(n) or {}).get("released_at")} for n in x["cards"]}}

    provenance_seed = {"frozen": lock["sha256"], "scryfall": {k: v["sha256"] for k, v in scry.items()},
                       "rules": rules.get("sha256"), "banned": banned.get("sha256"),
                       "edhrec": edhrec["artifact_sha256"], "spellbook": spellbook["sha256"],
                       "tournament": {k: v["sha256"] for k, v in tournament["decks"].items()}}
    sid = f"birthday-{dt.date.today().strftime('%Y%m%d')}-{canonical_json_hash(provenance_seed).split(':',1)[1][:12]}"
    hard_blockers = list(legality["blockers"])
    if rules.get("status") != "collected": hard_blockers.append("current Comprehensive Rules not collected")
    if not banned.get("commander_section_detected"): hard_blockers.append("official Commander banned-list section not detected")
    if edhrec["counts"]["unavailable"]:
        hard_blockers.append(f"EDHREC unavailable for {edhrec['counts']['unavailable']} non-pending deck(s)")
    if spellbook.get("decks") != 62:
        hard_blockers.append(f"Commander Spellbook covered {spellbook.get('decks')} decks, expected 62")
    if tournament["status"] != "collected":
        hard_blockers += ["tournament evidence: " + x for x in tournament.get("problems", [])] or ["tournament evidence blocked"]

    manifest = {
        "schema_version": 1, "kind": "birthday_authority_snapshot", "snapshot_id": sid,
        "generated_by": f"scripts/grixis_birthday_snapshot.py v{VERSION}",
        "retrieved_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "frozen_baseline": {"snapshot_id": lock["snapshot"], "lock": "data/grixis/dev_snapshot_lock.json",
                            "sha256": lock["sha256"], "rules_sha256": rules_lock["sha256"],
                            "preserved": True, "note": "Fresh data is isolated; A-F continue to reproduce against snap-20261016."},
        "sources": {"scryfall": scry, "comprehensive_rules": rules,
                    "official_commander_legality": banned, "edhrec": {k: v for k, v in edhrec.items() if k != "decks"},
                    "commander_spellbook": {k: v for k, v in spellbook.items() if k != "delta_vs_frozen_candidate_snapshot"},
                    "edhtop16": {k: v for k, v in tournament.items() if k != "decks"}},
        "canonical_deck_legality": legality, "pending_release_status": pending_now,
        "hard_blockers": hard_blockers, "status": "ready" if not hard_blockers else "blocked",
        "authority_note": "This snapshot supplies facts/derived evidence. It cannot approve a deck or decide an M5 swap; only Cory can accept M5 and approve/lock decks."
    }
    delta = {
        "schema_version": 1, "snapshot_id": sid, "baseline": lock["snapshot"],
        "scryfall_oracle": odelta, "scryfall_rulings": rdelta,
        "comprehensive_rules": {"changed_vs_frozen": rules.get("changed_vs_frozen"),
                                "frozen_sha256": rules_lock["sha256"], "fresh_sha256": rules.get("sha256"),
                                "fresh_effective_date": rules.get("effective_date")},
        "edhrec": {"counts": edhrec["counts"], "decks": edhrec["decks"]},
        "commander_spellbook": spellbook["delta_vs_frozen_candidate_snapshot"],
        "edhtop16": tournament["decks"], "pending_release": pending_now,
        "limitations": [
            "Exact historical EDHREC raw pages are unavailable; EDHREC delta compares fresh page names/hashes to committed derived M3 evidence, not to missing raw bytes.",
            "EDHREC, Commander Spellbook and EDHTop16 are community/observational evidence and never independently decide swaps.",
            "The official Wizards banned-list page is freshly hashed; no byte-identical 2026-10-16 raw page was retained, so its byte delta is unavailable.",
        ]
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    (OUT / "delta_vs_snap-20261016.json").write_text(json.dumps(delta, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"snapshot_id": sid, "status": manifest["status"], "hard_blockers": hard_blockers,
                      "oracle_delta": odelta["counts"], "rulings_delta": {k: rdelta[k] for k in ("added", "removed")},
                      "edhrec": edhrec["counts"], "spellbook_decks": spellbook["decks"],
                      "tournament": tournament["counts"], "legality": legality["counts"]}, indent=2))
    return 0 if not hard_blockers else 2


def check():
    mp = OUT / "manifest.json"; dp = OUT / "delta_vs_snap-20261016.json"; ep = OUT / "edhrec_current.json.gz"
    p = []
    for x in (mp, dp, ep, OUT / "spellbook_almost.json"):
        if not x.exists() or not x.stat().st_size:
            p.append(f"missing/empty {x.relative_to(ROOT)}")
    if p:
        print("birthday snapshot:", len(p), "problem(s)")
        print("\n".join("  - " + x for x in p)); return 1
    d = json.loads(mp.read_text(encoding="utf-8"))
    if d.get("frozen_baseline", {}).get("snapshot_id") != "snap-20261016" or not d.get("frozen_baseline", {}).get("preserved"):
        p.append("frozen snap-20261016 binding missing")
    if d.get("status") != "ready" or d.get("hard_blockers"):
        p.append(f"snapshot not ready: {d.get('hard_blockers')}")
    if d.get("canonical_deck_legality", {}).get("counts", {}).get("decks") != 62:
        p.append("canonical fresh-legality check did not cover 62 decks")
    if d.get("canonical_deck_legality", {}).get("counts", {}).get("blocked"):
        p.append("canonical fresh-legality check has blocked deck(s)")
    ed = (d.get("sources", {}).get("edhrec") or {}).get("counts", {})
    if ed.get("collected", 0) + ed.get("expected_unavailable", 0) != 62 or ed.get("unavailable", 0):
        p.append(f"EDHREC coverage not closed: {ed}")
    sp = d.get("sources", {}).get("commander_spellbook") or {}
    if sp.get("decks") != 62:
        p.append(f"Spellbook coverage {sp.get('decks')}/62")
    tr = d.get("sources", {}).get("edhtop16") or {}
    if tr.get("status") != "collected" or tr.get("counts", {}).get("collected_files") != tr.get("counts", {}).get("expected_cedh"):
        p.append(f"EDHTop16 coverage not closed: {tr.get('counts')} {tr.get('problems')}")
    for k, v in (d.get("sources", {}).get("scryfall") or {}).items():
        if v.get("status") != "collected" or not str(v.get("sha256", "")).startswith("sha256:"):
            p.append(f"Scryfall {k} not collected/hashed")
    if (d.get("sources", {}).get("comprehensive_rules") or {}).get("status") != "collected":
        p.append("current Comprehensive Rules not collected")
    if not (d.get("sources", {}).get("official_commander_legality") or {}).get("commander_section_detected"):
        p.append("official Commander banned-list section not detected")
    print(f"birthday snapshot {d.get('snapshot_id')}: {'PASS' if not p else 'FAIL'}; {len(p)} problem(s)")
    for x in p: print("  -", x)
    return 1 if p else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if not a.build and not a.check:
        ap.error("choose --build or --check")
    rc = 0
    if a.build: rc = build()
    if a.check: rc = max(rc, check())
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
