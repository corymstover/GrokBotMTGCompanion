#!/usr/bin/env python3
"""Build the Grixis section (grixis/) from the read-only source repo (Bot cycle 16).

Source: corymstover/grixis-commander-encyclopediaGPT, archived byte-identically in grixis/source-archive/ (Bot cycle 45; never modified). A clone path may be passed as SRC.
Steps: run scripts/grixis_eval.py checks → apply logged corrections → write
  grixis/decks/<slug>.md (one page per integrated list: commander block, validation, bracket floor,
      corrections, Archidekt list, card breakdown, source commentary verbatim with attribution,
      Commander Spellbook combos),
  grixis/Grixis Evaluation.md (all 62 source lists), grixis/Grixis Corrections.md,
  grixis/Grixis Packages.md (cross-deck package library), data/grixis_combos.json.
Usage: python3 scripts/build_grixis.py [--refresh-combos] [SRC]
Facts come from Scryfall bulk (.cache/) and Commander Spellbook; source commentary is the
source author's guidance and is quoted, not re-asserted.
"""
import atomic_io  # noqa: F401  atomic Path.write_text/write_bytes (Bot cycle 34)
import csv, datetime as dt, glob, json, os, re, subprocess, sys, time
from collections import Counter, defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402
import detect_combos as dc  # noqa: E402
from grixis_eval import norm  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
args = [a for a in sys.argv[1:] if not a.startswith("--")]
SRC = Path(args[0] if args else ROOT / "grixis/source-archive/grixis-commander-encyclopediaGPT")  # Bot cycle 45: companion archive by default
REPO = "https://github.com/corymstover/grixis-commander-encyclopediaGPT"
OUT = ROOT / "grixis"
DECKS = OUT / "decks"
TODAY = dt.date.today().isoformat()
import grixis_archive  # noqa: E402
# the archive is not its own git repo (git -C would answer with the companion's HEAD), so read its recorded commit
SRC_SHA = (grixis_archive.source_commit() if SRC.resolve() == grixis_archive.TREE.resolve() else
           subprocess.run(["git", "-C", str(SRC), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip())
BLOB = f"{REPO}/blob/{SRC_SHA or 'main'}/"

# ---- Bot cycle 47 (M0, Cory decision 1): ONE canonical project list per commander. Registered project exceptions
# (data/grixis/exceptions.json) stay in the canonical list, labeled and never called legal; the officially legal variant
# is a derived compliance projection (data/grixis/projections.json), never canonical. The Bot cycle 16 import had
# replaced Trade Secrets / Yawgmoth's Bargain and dropped the Lutri companion; those replacements now live only in the projection.
import grixis_authority as ga  # noqa: E402
EXC = ga.load_json(ga.EXCEPTIONS, {"exceptions": []})["exceptions"]
PROJ = ga.load_json(ga.PROJECTIONS, {"decks": {}})
EXC_AUTH = {(x["deck_id"], x["card"]): x for x in EXC if x["project_authorization_status"] == "AUTHORIZED_EXCEPTION"}
# Bot cycle 38: decks published with legality_status: pending (data/grixis_pending.json; flipped by scripts/activate_pending_grixis.py)
PENDING = {k: v for k, v in json.loads((ROOT / "data" / "grixis_pending.json").read_text(encoding="utf-8"))["decks"].items()
           if v.get("status") == "pending"} if (ROOT / "data" / "grixis_pending.json").exists() else {}
LEFT_OUT = {}
# Bot cycle 37 re-import: the 40 lists integrated in Bot cycle 16 (unchanged in the source since then).
C16 = set(json.loads((ROOT / "data" / "grixis_c16_ids.json").read_text())) if (ROOT / "data" / "grixis_c16_ids.json").exists() else set()
EVIDENCE_LABELS = ("VERIFIED", "HIGH_CONFIDENCE", "PROVISIONAL", "TEST_REQUIRED", "BLOCKED")


_RES = []


def resolver_check(text):
    import evaluate_decklist as ev_
    if not _RES:
        _RES.append(ev_.Resolver())
    return ev_.check(text, _RES[0])


def slugify(s):
    s = re.sub(r"[^\w\s-]", "", norm_keep(s)).strip().lower()
    return re.sub(r"[\s_]+", "-", s)


def norm_keep(s):
    import unicodedata
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().replace("'", "")


def rel_link(row, up="../../"):
    return f"[{row['name']}]({up}{row['shard'].replace(' ', '%20')}#{row['anchor']})" if row.get("shard") else row["name"]


def type_tag(t):
    front = t.split(" // ")[0]
    for k in ("Land", "Creature", "Planeswalker", "Battle", "Instant", "Sorcery", "Artifact", "Enchantment"):
        if k in front:
            return k
    return "Other"


def src_files(did):
    """Per-deck source records: files whose name starts with the deck id, plus every `*_artifact` path the source's
    state/current_deck_overrides.json records for the deck (Bot cycle 37: some ids no longer prefix their files,
    e.g. `Goben__Gene_Splice_Savant` holds the Norman Osborn // Green Goblin list)."""
    key = norm(did).replace("the", "")
    out = defaultdict(list)
    st = json.loads((SRC / "state/current_deck_overrides.json").read_text())["decks"].get(did, {})
    for k, v in sorted(st.items()):
        if k.endswith("_artifact") and isinstance(v, str) and (SRC / v).is_file():
            out[(SRC / v).parent.name].append(SRC / v)
    for f in sorted(glob.glob(str(SRC / "refinement/**/*"), recursive=True)):
        p = Path(f)
        if p.is_file() and norm(p.name).replace("the", "").startswith(key):
            if p not in out[p.parent.name]:
                out[p.parent.name].append(p)
    return {k: sorted(v) for k, v in out.items()}


def demote(md, rel_dir):
    """Quote a source markdown file: headings demoted under ####, relative links → absolute source URLs."""
    def fix(m):
        t = m.group(2)
        if re.match(r"^[a-z]+:", t) or t.startswith("#"):
            return m.group(0) if not t.startswith("#") else m.group(1)
        return f"{m.group(1)}({BLOB}{os.path.normpath(os.path.join(rel_dir, t))})"
    md = re.sub(r"(\[[^\]]*\])\(([^)\s]+)\)", fix, md)
    lines = []
    infence = False
    for l in md.splitlines():
        if l.startswith("```"):
            infence = not infence
        if not infence and re.match(r"^#{1,6} ", l):
            l = "**" + l.lstrip("#").strip() + "**"
        lines.append(l)
    return "\n".join(lines).strip()


def decisions_csv_table(p):
    rows = list(csv.DictReader(open(p, encoding="utf-8")))
    out = ["| ID | Candidate | Proposed cut | Decision | Source reasoning (abridged) |", "|---|---|---|---|---|"]
    for r in rows:
        why = (r.get("reviewer_notes") or r.get("expected_benefit") or "").replace("|", "/").replace("\n", " ")
        out.append(f"| {r.get('review_id','')} | {r.get('candidate_card','')} | {r.get('proposed_cut','')} | {r.get('decision_status','')[:60]} | {why[:400]}{'…' if len(why) > 400 else ''} |")
    return "\n".join(out)


def combos(decks, refresh):
    cache = ROOT / "data" / "grixis_combos.json"
    have = json.loads(cache.read_text())["decks"] if cache.exists() and not refresh else {}
    for did, d in decks.items():
        sig = sorted(c["name"] for c in d["final"])
        if did in have and have[did].get("sig") == sig:
            continue
        cmd = [c["name"] for c in d["final"] if c["zone"] == "commander"]
        mn = [c["name"] for c in d["final"] if c["zone"] == "main"]
        res = dc.query(cmd, mn)
        rows = []
        for v in sorted(res["included"], key=lambda v: (len(v["uses"]), v["id"])):
            names = [u["card"]["name"] for u in v["uses"]]
            rows.append({"id": v["id"], "cards": names, "n": len(names), "infinite": dc.infinite(v),
                         "produces": [p["feature"]["name"] for p in v["produces"]][:4],
                         "requires": [r["template"]["name"] for r in v.get("requires", [])], "csb_bracket_tag": v.get("bracketTag")})
        have[did] = {"sig": sig, "combos": rows, "almost": len(res.get("almostIncluded", [])), "queried": TODAY}
        print(f"  spellbook {did}: {len(rows)} combos", flush=True)
        time.sleep(1)
    cache.write_text(json.dumps({"source": dc.API, "decks": have}, indent=1, ensure_ascii=False))
    return have


def main():
    subprocess.run([sys.executable, str(ROOT / "scripts/grixis_eval.py"), str(SRC)], check=True, stdout=subprocess.DEVNULL)
    ev = json.loads((ROOT / "data/grixis_eval.json").read_text())
    cards, bulk = ing.get_bulk(ing.DEFAULT_CACHE, None)
    by_name = {}
    for c in cards:
        if c.get("layout") not in ing.EXCLUDED_LAYOUTS and ing.in_universe(c):
            by_name.setdefault(c["name"], c)
    index = {r["oracle_id"]: r for r in csv.DictReader(ing.INDEX_CSV.open(encoding="utf-8"))}
    DECKS.mkdir(parents=True, exist_ok=True)
    import tarfile
    from grixis_eval import parse
    tar = tarfile.open(SRC / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz")
    base_tags, any_tags = {}, defaultdict(Counter)
    for m in tar.getmembers():
        if m.isfile() and m.name.endswith(".txt"):
            for e in parse(tar.extractfile(m).read().decode("utf-8-sig")):
                if not e.get("bad") and e["tags"] and "commander" not in e["tags"].lower():
                    base_tags[(Path(m.name).stem, e["name"])] = e["tags"]
                    any_tags[e["name"]][e["tags"]] += 1
    corrections, integrated, evaluation = [], {}, []
    for did, d in ev["decks"].items():
        approved = d["source_state"]["approval_status"] == "APPROVED"
        hard = [i for i in d["issues"] if i["type"] in ("banned", "not Commander-legal", "color identity", "deck size", "singleton", "unresolved name", "commander eligibility", "commander pairing")]
        unfixed, accepted = ga.accepted_hard_issues(did, hard)
        pend = PENDING.get(did)
        if pend:  # Bot cycle 38: only the registered not-yet-legal cards may fail, and only on Commander legality
            unfixed = [i for i in unfixed if not (i["type"] == "not Commander-legal" and i["card"] in pend["cards"])]
        if did in LEFT_OUT:
            why = "future-release: " + LEFT_OUT[did]
        elif not approved:
            why = "not integrated: the source repo marks this list UNREFINED (its whole-list audit has not run yet). Validation results are kept here for a later import."
        elif unfixed:
            why = "not integrated: unresolved " + "; ".join(i["type"] for i in unfixed)
        else:
            why = None
        evaluation.append((did, d, hard, why))
        if why:
            continue
        final = [dict(r) for r in d["cards"] if r["zone"] != "companion"]
        fixes = []
        mine = [x for (dd, _), x in EXC_AUTH.items() if dd == did]
        for x in mine:
            if x["zone"] == "companion" and not any(r["name"] == x["card"] for r in final):
                row = resolver_check(f"1x {x['card']} [Companion]")["cards"][0]
                row["tags"] = "Companion"
                final.append(row)
        for r in final:
            x = EXC_AUTH.get((did, r["name"]))
            if x:
                r["exception"] = x
        for x in mine:
            fixes.append(("project exception (Bot cycle 47)", f"{x['card']}{' (companion)' if x['zone'] == 'companion' else ''} kept in the canonical project list",
                          f"{x['render_label']}. Authorized: {x['authorized_by']}. Registry: `data/grixis/exceptions.json` ({x['id']}). "
                          + ("The Bot cycle 16 import had replaced it; since Bot cycle 47 that replacement lives only in the deck page's derived compliance projection (not canonical)." if x["zone"] != "companion" else
                             "The source's approval record designates Lutri as companion (its approved 100-card file has no companion line, so the line is added from that record). The Bot cycle 16 import had dropped it.")))
        d["exceptions"] = mine
        # mechanical normalization log
        restored = [0, 0]
        for r in final:
            if r["zone"] == "commander" or r["tags"]:
                continue
            key = r.get("src_name") or r["name"]
            if (did, key) in base_tags:
                r["tags"], restored[0] = base_tags[(did, key)], restored[0] + 1
            elif any_tags.get(key):
                r["tags"], restored[1] = any_tags[key].most_common(1)[0][0], restored[1] + 1
        untagged = [r for r in final if not r["tags"] or r["tags"].lower() in ("commander",)]
        cmd_plain = [r for r in final if r["zone"] == "commander" and "{top}" not in r["tags"]]
        pins = sum(1 for r in final if r.get("set"))
        mech = []
        if cmd_plain:
            mech.append(f"`[Commander]` → `[Commander{{top}}]` ({len(cmd_plain)} line(s))")
        n_unt = len([r for r in untagged if r["zone"] != "commander"])
        if restored[0] or restored[1]:
            mech.append(f"role tags restored on {sum(restored)} untagged line(s): {restored[0]} from this deck's FINAL baseline, {restored[1]} from the tag the source uses most for that card in other decks")
        if n_unt:
            mech.append(f"{n_unt} untagged line(s) given a type tag (e.g. `[Land]`)")
        if pins:
            mech.append(f"{pins} pinned printings `(set) number` moved from the import block to the card breakdown, as in our 46 decks")
        if mech:
            fixes.append(("format", "Archidekt list normalized to [EDH Standards](../../EDH%20Standards.md#list-format-archidekt)", "; ".join(mech) + "."))
        sh = d.get("selection", "")
        if "card-for-card" in sh:
            fixes.append(("provenance", "approved list located by content", f"The SHA-256 recorded in the source's `state/current_deck_overrides.json` matches none of its files. We used `{d['source_path']}`, which matches the deck's Card_Verification CSV card for card."))
        if pend:
            fixes.insert(0, ("pending legality", f"published as **PENDING LEGALITY** (legal from {pend['legal_from']})",
                             pend["note"] + f" Not yet Commander-legal: {', '.join(pend['cards'])}. Activation: `python3 scripts/activate_pending_grixis.py`."))
        d["final"], d["fixes"], d["pending"] = final, fixes, pend
        integrated[did] = d
        for kind, what, reason in fixes:
            corrections.append((did, d, kind, what, reason))
    combo = combos(integrated, "--refresh-combos" in sys.argv)

    # ---------------- per-deck pages
    names_ix = {}
    for did, d in integrated.items():
        final = d["final"]
        cmdrs = [r for r in final if r["zone"] == "commander"]
        title = " + ".join(r["name"] for r in cmdrs)
        slug = slugify(did.replace("__", " ").replace("_", " ")) if did.startswith("Grixistax") else slugify(cmdrs[0]["name"].split(" // ")[0]) + (("-" + slugify(cmdrs[1]["name"].split(",")[0])) if len(cmdrs) > 1 else "")
        d["slug"] = slug
        names_ix[did] = slug
        gcs = [r["name"] for r in final if r["gc"]]
        xt = [r["name"] for r in final if r["xturn"]]
        mld = [r["name"] for r in final if r["mld"]]
        floor = 4 if (mld or len(gcs) > 3) else 3 if gcs else 2
        co = combo[did]["combos"]
        two_inf = [x for x in co if x["n"] == 2 and x["infinite"]]
        cfloor = max(floor, 3) if two_inf else floor
        d.update(gcs=gcs, floor=floor, cfloor=cfloor, n_combos=len(co), n_two=len(two_inf))
        total = sum(r["qty"] for r in final if r["zone"] != "companion")
        n_comp = sum(1 for r in final if r["zone"] == "companion")
        lands = sum(r["qty"] for r in final if type_tag(r["type"]) == "Land")
        basics = sum(r["qty"] for r in final if "Basic" in r["type"])
        avg = sum(r["mv"] * r["qty"] for r in final if type_tag(r["type"]) != "Land" and r["zone"] == "main") / max(1, sum(r["qty"] for r in final if type_tag(r["type"]) != "Land" and r["zone"] == "main"))
        d.update(lands=lands, avg_mv=avg)
        src_claim = None
        fl = src_files(did)
        texts = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for k in ("approvals", "decisions", "blueprints") for p in fl.get(k, []) if p.suffix == ".md")
        m = re.search(r"Bracket[^0-9\n]{0,6}([1-5])\s*(?:[—/-]|\(|)\s*`?\**\s*([A-Za-z][A-Za-z /()-]*?)\s*(?:[`*\n.,;)]|$)", texts)
        if m:
            src_claim = f"{m.group(1)} — {m.group(2).strip()}"
        d["src_claim"] = src_claim
        mt = re.search(r"Archidekt tags:?\**:?\s*\**\s*([A-Za-z0-9+/&' ,-]{3,80}?)\s*(?:\*\*|\.|\n)", texts)
        d["themes"] = mt.group(1).strip() if mt else ""
        fx = (f"The source records no Game Changer count and does not check the official Game Changers list anywhere in its approval records. We added it: **{len(gcs)} Game Changers**, so the minimum bracket is **{floor}**"
              + (f", and **{cfloor}** once its two-card infinite combos are counted" if cfloor > floor else "") + f". Commander Spellbook finds {len(co)} complete combos ({len(two_inf)} two-card infinite)."
              + (f" This is consistent with the source's stated Bracket {src_claim.split(' ')[0]}." if src_claim and int(src_claim[0]) >= cfloor else (f" ⚠️ The source states Bracket {src_claim.split(' ')[0]}, which is **below** this floor." if src_claim else "")))
        d["fixes"].append(("bracket", "Game Changers and combo floor added", fx))
        corrections.append((did, d, "bracket", "Game Changers and combo floor added", fx))
        if lands < 32 and avg > 3.0:
            note = f"{lands} lands with an average nonland MV of {avg:.2f}. That is below the community-convention range (~36 lands; see [EDH Standards](../../EDH%20Standards.md#deck-building-checklist)) for a curve this high. **Guidance:** review the mana base. The list is unchanged, because the source approved it."
            d["fixes"].append(("structure (flag)", "low land count for curve", note))
            corrections.append((did, d, "structure (flag)", "low land count for curve", note))
        ci = d["ci"]
        pend = d.get("pending")
        L = [f"# Grixis Deck — {title}", ""]
        if pend:
            L += [f"> ⏳ **PENDING LEGALITY — not Commander-legal yet.** Legal from **{pend['legal_from']}** ([Wizards]({pend['legal_from_source']['url']}): \"{pend['legal_from_source']['quote']}\"; Scryfall set `{pend['set']}`). "
                  f"Not-yet-legal cards: {', '.join('**' + c + '**' for c in pend['cards'])}. This page is published so all 62 source decks are in the companion, "
                  "but it is **excluded from every legal-deck count** (Grixis index, packages, summaries). `validate_all` accepts these cards only while "
                  "`legality_status: pending` and the date is still ahead. Activation: `python3 scripts/activate_pending_grixis.py` "
                  "(refreshes the Scryfall bulk, re-checks the cards, flips the deck to active once they are legal).", ""]
        exc = d.get("exceptions") or []
        if exc:
            L += [f"> 🚩 **PROJECT EXCEPTIONS — not Commander-legal.** This deck's canonical project list carries {len(exc)} project-authorized exception(s): "
                  + "; ".join(f"**{x['card']}**{' (companion)' if x['zone'] == 'companion' else ''} ({x['render_label'].split(': ', 1)[-1]})" for x in exc)
                  + ". Official Commander compliance: **not compliant**. They are authorized by Cory for this project (registry `data/grixis/exceptions.json`, "
                  "[Grixis Authority Model](../Grixis%20Authority%20Model.md#legality-model)); they are never reported as legal. "
                  "An officially legal version is shown below as a [derived compliance projection (not canonical)](#official-legal-projection-derived-not-canonical).", ""]
        L += [
             f"> **From [grixis-commander-encyclopediaGPT]({REPO}), path [`{d['source_path']}`]({BLOB}{d['source_path'].split(' → ')[0]})** "
             f"({d['source_state'].get('approval_status')} / {d['source_state'].get('lock_status')} in the source, user approval {d['source_state'].get('user_approval_date')}; source commit `{SRC_SHA}`). "
             f"{'Imported in Bot cycle 16; re-validated in Bot cycle 37' if did in C16 else 'Imported in Bot cycle 38 as a pending-legality page' if pend else 'Imported in Bot cycle 37 (newly approved in the source)'} against Scryfall Oracle bulk {bulk[:10]}. The card choices and all commentary are **the source author's guidance**. Corrections we made are listed below. Facts (Oracle text, legality, identity, Game Changers, combos) come from our card DB and Commander Spellbook. Section index: [Grixis](../README.md).", "",
             "## Contents", "- [Commander](#commander)", "- [Validation](#validation)", "- [Bracket assessment](#bracket-assessment)",
             "- [Corrections applied](#corrections-applied)", "- [Decklist (Archidekt import)](#decklist-archidekt-import)"] + (
             ["- [Official-legal projection (derived, not canonical)](#official-legal-projection-derived-not-canonical)"] if exc else []) + ["- [Card breakdown](#card-breakdown)",
             "- [Source commentary (verbatim)](#source-commentary-verbatim)", "- [Combos (Commander Spellbook)](#combos-commander-spellbook)", "",
             "## Commander", ""]
        for r in cmdrs:
            c = by_name.get(r["name"]) or {}
            L.append(f"- **{rel_link(r)}** — {c.get('mana_cost') or ' // '.join(f.get('mana_cost','') for f in c.get('card_faces') or [])} — {r['type']}")
        L.append(f"- Color identity: **{ing.ci_label(list(ci))}**")
        for r in cmdrs:
            c = by_name.get(r["name"]) or {}
            pn = ing.pairing_notes(c) if c else []
            L.append(f"- Eligibility ({r['name']}): {ing.commander_eligibility(c)}" + (f" · pairing: {', '.join(pn)}" if pn else ""))
        L += ["", "## Validation", "",
              f"- Total cards: **{total}** ({len(cmdrs)} commander(s) + {total - len(cmdrs) - lands} nonland + {lands - basics} nonbasic lands + {basics} basics)" + (f" + {n_comp} companion outside the 100" if n_comp else "") + f" · average nonland MV {avg:.2f}",
              (f"- Strict color identity (CR 903.5c), singleton (903.5b), size (903.5a): pass. **Official Commander compliance: ❌ not compliant** — {len(exc)} project-authorized exception(s), not Commander-legal: "
               + "; ".join(f"{x['card']} ({x['official_commander_legality'].replace('_', ' ')})" for x in exc) + ". `validate_all` accepts them only because they are registered project exceptions; every other card is Commander-legal.") if exc else
              ("- Strict color identity (CR 903.5c), singleton (903.5b), Commander-legal, size (903.5a): ✅ **all checks pass**" + (" (after the corrections below)" if any(f[0] == "legality" for f in d["fixes"]) else "")) if not pend else
              (f"- Strict color identity (CR 903.5c), singleton (903.5b), size (903.5a): pass. **Commander legality: ⏳ pending.** {', '.join(pend['cards'])} "
               f"{'is' if len(pend['cards']) == 1 else 'are'} `not_legal` on Scryfall until their official Commander-legal date ({pend['legal_from']}, per Wizards); every other card is Commander-legal."),
              f"- Every card resolves to an entry in our card DB ({len(final)}/{len(final)} lines linked).", "",
              "## Bracket assessment", "",
              f"- Game Changers ({len(gcs)}): " + (", ".join(gcs) or "none"),
              "- Extra-turn cards: " + (", ".join(xt) or "none"),
              "- Mass land denial: " + (", ".join(mld) or "none"),
              f"- Commander Spellbook: {len(co)} complete combo(s), {len(two_inf)} two-card infinite (see [Combos](#combos-commander-spellbook)).",
              f"- **Minimum bracket by the published barometers: {floor}** ({'more than three Game Changers' if len(gcs) > 3 else '1–3 Game Changers' if gcs else 'no Game Changers'}{'; mass land denial' if mld else ''})."
              + (f" **Bracket implication:** a two-card infinite combo raises the floor to **Bracket {cfloor}+**." if cfloor > floor else ""),
              f"- Source's stated target (guidance): **Bracket {src_claim}**." if src_claim else "- Source's stated target: not stated in the imported records.",
              "- (Brackets are a pregame-conversation tool. See [EDH Standards](../../EDH%20Standards.md#power-bracket-assessment).)", "",
              "## Corrections applied", ""]
        if d["fixes"]:
            L += ["| Type | Change | Reason |", "|---|---|---|"] + [f"| {k} | {w} | {r} |" for k, w, r in d["fixes"]]
        else:
            L.append("None needed.")
        L += ["", f"Full log for all decks: [Grixis Corrections](../Grixis%20Corrections.md).", "", "## Decklist (Archidekt import)", "", "```text"]
        for r in final:
            if r["zone"] == "commander":
                tag = "Commander{top}"
            else:
                tag = r["tags"] or type_tag(r["type"])
            L.append(f"{r['qty']}x {r['name']} [{tag}]")
        if pend:
            for r in final:
                if r["name"] in pend["cards"]:
                    r["pending_mark"] = True
        L += ["```", ""]
        if exc:
            pt = ga.projection_text(did, "\n".join(L[L.index("## Decklist (Archidekt import)") + 3:-2]) + "\n", PROJ)
            pj = PROJ["decks"][did]
            L += ["## Official-legal projection (derived, not canonical)", "",
                  f"> **{ga.PROJECTION_LABEL}.** Derived from the canonical project list above by the substitutions below, so the deck can be played under official Commander rules. "
                  "It never competes for authority: it is not canonical, never enters an approval state, and changes whenever the canonical list changes. "
                  f"Registry: `data/grixis/projections.json`; export: `exports/grixis-archidekt/projections/{slug}.official-legal-projection.txt`.", "",
                  "| Canonical card | Projection | Why |", "|---|---|---|"]
            L += [f"| {x['from']} | {x['to']} | {x['why']} |" for x in pj["substitutions"]]
            if pj.get("drop_companion"):
                L.append(f"| {pj['drop_companion']} (companion) | — (no companion) | {pj['drop_companion_why']} |")
            L += ["", "```text", pt.strip(), "```", ""]
        L += ["## Card breakdown", "",
              "Role tags are the source author's (untagged lines show the card type). *Printing* is the source's pinned printing, if it pinned one.", "",
              "| Card | Role (source tag) | Type | MV | Identity | GC | Printing |", "|---|---|---|---|---|---|---|"]
        for r in sorted(final, key=lambda r: (r["zone"] != "commander", (r["tags"] or type_tag(r["type"])).lower(), r["name"])):
            role = "Commander" if r["zone"] == "commander" else (r["tags"] or type_tag(r["type"]))
            L.append(f"| {('**' + rel_link(r) + '**') if r.get('fixed') else rel_link(r)}{' (×' + str(r['qty']) + ')' if r['qty'] > 1 else ''} | {role}{' · ⏳ not legal until ' + pend['legal_from'] if r.get('pending_mark') else ''}{' · ' + r['exception']['render_label'] if r.get('exception') else ''} | {r['type']} | {int(r['mv'])} | {r['ci']} | {'✅' if r['gc'] else ''} | {(r['set'] or '') + (' ' + r['cn'] if r.get('cn') else '') if r.get('set') else '—'} |")
        L += ["", "## Source commentary (verbatim)", "",
              f"> Quoted from the source repo with headings turned into bold text. This is **the source author's analysis and opinion (guidance)**, from `{REPO.split('/')[-1]}`, path shown above each block. Relative links point back to the source. Rules statements here were not re-verified card by card (see [Grixis Corrections](../Grixis%20Corrections.md#oracle-text-check) for the Oracle check). Where the source mentions Lutri, Trade Secrets or Yawgmoth's Bargain as approved exceptions: since Bot cycle 47 the canonical project list above carries them as labeled project exceptions (not Commander-legal); the officially legal version is the derived compliance projection.", ""]
        shown = 0
        for k in ("blueprints", "decisions", "approvals", "evidence"):
            for p in fl.get(k, []):
                rp = str(p.relative_to(SRC))
                if p.suffix == ".md":
                    L += [f"### From `{rp}`", "", f"Source: [{rp}]({BLOB}{rp})", "", demote(p.read_text(encoding="utf-8"), str(p.parent.relative_to(SRC))), ""]
                    shown += 1
                elif p.suffix == ".csv" and k == "decisions" and not any(q.suffix == ".md" for q in fl.get("decisions", [])):
                    L += [f"### From `{rp}` (candidate decision ledger)", "", f"Source: [{rp}]({BLOB}{rp})", "", decisions_csv_table(p), ""]
                    shown += 1
        other = [p for k in ("verification", "audits", "rules", "tests", "tracker_reconciliation") for p in fl.get(k, [])]
        if other:
            L += ["### Further source evidence (linked, not copied)", ""] + [f"- [{p.relative_to(SRC)}]({BLOB}{p.relative_to(SRC)})" for p in other][:40] + [""]
        L += [dc.START, "## Combos (Commander Spellbook)", "",
              f"> Generated {combo[did]['queried']} by `scripts/build_grixis.py` from the [Commander Spellbook](https://commanderspellbook.com) public API (community-maintained). Shows only combos whose **every card is in this list**. Bracket barometer: *Brackets 1–2: no intentional two-card infinite combos. Bracket 3: no early-game two-card infinite combos.*", ""]
        if not co:
            L.append(f"**No complete combos found** ({combo[did]['almost']} more are one card away; not listed).")
        else:
            L += [f"**{len(co)} complete combo(s); {len(two_inf)} two-card infinite.** {combo[did]['almost']} more are one card away (not listed).", "",
                  "| Cards | Produces (Spellbook) | Extra requirements | Link |", "|---|---|---|---|"]
            for x in co:
                flag = "⚠️ **two-card infinite** · " if x["n"] == 2 and x["infinite"] else ""
                L.append(f"| {flag}{' + '.join(x['cards'])} | {', '.join(x['produces'])} | {'; '.join(x['requires']) or '—'} | [{x['id']}](https://commanderspellbook.com/combo/{x['id']}/) |")
        L.append(dc.END)
        (DECKS / f"{slug}.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    # ---------------- evaluation page (all 62)
    E = ["# Grixis Evaluation — all 62 source lists", "",
         f"> Bot cycle 16; re-run in Bot cycle 37. Every decklist in [grixis-commander-encyclopediaGPT]({REPO}) (commit `{SRC_SHA}`), checked by `scripts/grixis_eval.py` against Scryfall Oracle bulk {bulk[:10]}. Checks: name resolution, commander eligibility and pairing, 100 cards, singleton (with Oracle copy exceptions such as Nazgûl), color identity, Commander legality and bans, companion, Game Changers. Oracle text recorded in the source's audit CSVs is compared with current Oracle. Back to [Grixis](README.md).", "",
         "## Contents", "- [Summary](#summary)", "- [Per-list results](#per-list-results)", "- [How the current list was chosen](#how-the-current-list-was-chosen)", "",
         "## Summary", ""]
    legal = {k: v for k, v in integrated.items() if not v.get("pending") and not v.get("exceptions")}
    pending = {k: v for k, v in integrated.items() if v.get("pending")}
    excd = {k: v for k, v in integrated.items() if v.get("exceptions")}
    n_int = len(legal)
    E += [f"- Source lists: **{len(evaluation)}** (62 baseline FINAL lists; {sum(1 for _, d, _, _ in evaluation if d['source_state']['approval_status'] == 'APPROVED')} have a newer user-approved list).",
          f"- **Deck pages: {len(integrated)}/{len(evaluation)}** ({n_int} legal + {len(excd)} 🚩 with project exceptions + {len(pending)} ⏳ pending legality). **Integrated as legal: {n_int}**, i.e. every approved list that passes or could be corrected to pass. **With project exceptions: {len(excd)}** (" + (", ".join(' + '.join(v['commanders']) for v in excd.values()) or "none") + "; canonical project list keeps Cory-authorized exceptions, not Commander-legal, see [Grixis Authority Model](Grixis%20Authority%20Model.md#legality-model)). **Pending legality: {len(pending)}** (" + (", ".join(f"{' + '.join(v['commanders'])}, legal from {v['pending']['legal_from']}" for v in pending.values()) or "none") + f"). **Left out: {len(evaluation) - len(integrated)}**.",
          f"- Hard problems found across all 62: " + (", ".join(f"{v}× {k}" for k, v in Counter(i['type'] for _, _, h, _ in evaluation for i in h).most_common()) or "none") + ".",
          f"- Oracle check: {ev['oracle_check']['rows_checked']:,} Oracle-text rows in {ev['oracle_check']['files']} source audit files; **{len(ev['oracle_check']['stale'])} differ** from current Oracle.", "",
          "## Per-list results", "",
          "| # | Source deck | Commander(s) | Source status | Cards | Hard issues | GC | Result |", "|---|---|---|---|---|---|---|---|"]
    for i, (did, d, hard, why) in enumerate(evaluation, 1):
        gc = sum(1 for r in d["cards"] if r["gc"])
        res = (f"⏳ [pending legality](decks/{names_ix[did]}.md) (legal from {integrated[did]['pending']['legal_from']})" if did in pending
               else f"🚩 [integrated with project exceptions](decks/{names_ix[did]}.md) (not Commander-legal: {', '.join(x['card'] for x in integrated[did]['exceptions'])})" if did in excd
               else f"✅ [integrated](decks/{names_ix[did]}.md)" if did in integrated else "⏸ " + why)
        E.append(f"| {i} | `{did}` | {' + '.join(d['commanders'])} | {d['source_state']['approval_status']} | {d['total']} | {'; '.join(x['type'] + ': ' + x['card'] for x in hard) or '—'} | {gc} | {res} |")
    E += ["", "## How the current list was chosen", "",
          "- If `state/current_deck_overrides.json` marks the deck APPROVED/LOCKED, we use the approved list: the `approved_list_artifact`, or the `refinement/decklists/*.txt` file whose SHA-256 matches `approved_list_sha256`. If no file matches, we use the file that matches the deck's Card_Verification CSV card for card.",
          "- Otherwise we use the frozen baseline `source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz → TXT/<deck>.txt`.", ""]
    (OUT / "Grixis Evaluation.md").write_text("\n".join(E) + "\n", encoding="utf-8")

    # ---------------- corrections page
    kinds = Counter(c[2] for c in corrections)
    C = ["# Grixis Corrections", "",
         f"> Bot cycles 16 and 37. Every change made to a source list on import from [grixis-commander-encyclopediaGPT]({REPO}), with its reason. The source repo was not modified. Back to [Grixis](README.md).", "",
         "## Contents", "- [Summary](#summary)", "- [Corrections table](#corrections-table)", "- [Oracle text check](#oracle-text-check)", "- [Source-repo structural findings](#source-repo-structural-findings)", "",
         "## Summary", "", f"**{len(corrections)} corrections** across {len({c[0] for c in corrections})} decks: " + ", ".join(f"{v} {k}" for k, v in kinds.most_common()) + ".", "",
         "## Corrections table", "", "| Deck | Type | Issue → fix | Reason |", "|---|---|---|---|"]
    for did, d, kind, what, reason in corrections:
        C.append(f"| [{' + '.join(d['commanders'])}](decks/{d['slug']}.md) | {kind} | {what.replace('../../', '../')} | {reason.replace('../../', '../')} |")
    st = ev["oracle_check"]["stale"]
    C += ["", "## Oracle text check", "",
          f"- **{ev['oracle_check']['rows_checked']:,} Oracle-text rows** checked, from {ev['oracle_check']['files']} source files: per-deck `Card_Verification` CSVs, the Abaddon card audit, the Scryfall metadata overlays and the Oracle cache. Each was compared with our current Oracle text (Scryfall bulk {bulk[:10]}), ignoring punctuation and case.",
          f"- **{len(st)} rows are outdated.** The source refreshed Scryfall data on 2026-10-12 to 2026-10-15, so its recorded Oracle text is current." if not st else f"- **{len(st)} outdated:** " + ", ".join(st),
          "- Quotes inside the source's Markdown notes were also checked against all Oracle text. One is **abridged** rather than outdated: `refinement/verification/Anhelo_the_Painter_Proposed_Final_Verification_2026-10-13.md` labels Cryptic Pursuit's text as \"Current Oracle text\" but leaves out the manifest reminder text. The rules wording matches the [card entry](../cards/C/cr.md#cryptic-pursuit), so no fix was needed.",
          "- The source's notes contain no pre-2024 \"enters the battlefield\" wording.", "",
          "## Source-repo structural findings", "",
          "These are process notes, not deck changes. We did not modify the source.",
          "- Two approved lists (Admiral Brass, Unsinkable; Anhelo, the Painter) have an `approved_list_sha256` that matches no file in the repo. Their content matches the Card_Verification CSVs. The source's own 2026-10-15 Archidekt export (`exports/archidekt_2026-10-15/README.txt`) confirms it: their \"state canonical digests are logical/list digests rather than raw TXT file SHA-256 values\".",
          "- Bot cycle 37 cross-check: all 62 lists we selected match the source's `exports/archidekt_2026-10-15/` package (its `manifest.csv` and per-deck TXT files) card for card.",
          "- Deck id `Goben__Gene_Splice_Savant` (#21) holds the **Norman Osborn // Green Goblin** list (already so in the frozen FINAL baseline). Its files are named for Norman Osborn, so we locate them through the artifact paths in the source state.",
          "- One state artifact path does not exist: Thraximundar's `whole_list_audit_artifact` points to `refinement/decisions/Thraximundar_Whole_List_Audit_v2_2026-10-15.csv`, but the file in the repo is `refinement/audits/Thraximundar_Whole_List_Audit_2026-10-15.csv` (linked from the deck page).",
          "- ⚠️ The Tresserhorn's Lord, Returned approval record (2026-10-15) reports \"current official Commander legality PASS, no project exception required\". Scryfall lists the card as `not_legal`, and Wizards says new MBC cards are Commander-legal on 2026-11-13 (\"New-to-Magic MBC cards will be legal in Commander on November 13, 2026.\", [What's Inside Mystery Booster Commander Edition?](https://magic.wizards.com/en/news/feature/whats-inside-mystery-booster-commander-edition)), so the deck page is published as ⏳ *pending legality* (Bot cycle 38; date corrected in Bot cycle 44).",
          "- Decklist files use mixed formats: some lines have `(set) number` printings and role tags, some only `Nx Name`. Commanders are tagged `[Commander]` or `[Commander{top}]`.",
          "- The Lutri companion is recorded in the approval record but missing from the approved 100-card file. The two disagree. The source's Archidekt export README still says to set \"the intended commanders/companion manually\" for this deck, and its retrospective gate keeps Trade Secrets, Yawgmoth's Bargain (banned) and Lutri (banned as a companion) as *project exceptions*. **Bot cycle 47 (Cory decision 1):** the canonical project list carries all three as labeled project exceptions (not Commander-legal; registry `data/grixis/exceptions.json`); the cycle 16 replacements live on only as the derived compliance projection.",
          "- Per-deck evidence is spread across 5–8 folders (blueprints, decisions, approvals, evidence, verification, rules, tests), and one blueprint exists twice (`Be_lakor__the_Dark_Master_v1.md` / `Belakor_the_Dark_Master_v1.md`). On import, each deck's records are gathered into a single page.",
          "- The approval record for deck #8 says `state/current_deck_overrides.json` was stale at that time. In Bot cycle 16 the state file listed 40 decks. By commit `" + SRC_SHA + "` (Bot cycle 37) it lists all 62 as APPROVED/LOCKED, and it now records per-deck artifact paths (approved list, whole-list audit, decision closeout, verification, approval record).",
          "- New in the source since Bot cycle 16: a mandatory **99-slot whole-list audit** per deck (KEEP/CUT for every non-commander slot), *approval-ready verification* and *candidate decision closeout* records, a \"zero-new-material-improvement\" closure before approval, and one-shot GitHub Actions finalizers that write the approval and lock. We adopted the audit and closure steps as guidance in the [EDH Deck Evaluation Checklist](../EDH%20Deck%20Evaluation%20Checklist.md).", ""]
    (OUT / "Grixis Corrections.md").write_text("\n".join(C) + "\n", encoding="utf-8")

    # ---------------- package library
    cnt, roles, rows = Counter(), defaultdict(Counter), {}
    for did, d in legal.items():  # Bot cycle 38: pending-legality decks are not counted
        for r in d["final"]:
            if r["zone"] == "commander" or "Basic" in r["type"]:
                continue
            cnt[r["name"]] += 1
            roles[r["name"]][(r["tags"] or type_tag(r["type"])).split(",")[0].strip()] += 1
            rows[r["name"]] = r
    N = len(legal)
    groups = defaultdict(list)
    for n, k in cnt.items():
        role = roles[n].most_common(1)[0][0]
        if type_tag(rows[n]["type"]) == "Land":
            role = "Land"
        groups[role].append((k, n))
    P = ["# Grixis Packages", "",
         f"> Bot cycle 16; rebuilt in Bot cycle 37. Cross-deck package library built from the **{N} integrated Grixis lists** (source: [grixis-commander-encyclopediaGPT]({REPO}); role tags are the source author's). For each role, the cards that appear in at least 4 lists, with how many lists use them. Facts: Commander-legal, identity from Scryfall, **GC** = Game Changer. *Which package to run is guidance: start from the commander blueprint ([EDH Deck Template](../EDH%20Deck%20Template.md)), not from popularity.* The general, identity-wide version is [EDH Packages](../EDH%20Packages.md). Back to [Grixis](README.md).", "",
         "## Contents"]
    order = sorted(groups, key=lambda g: (g != "Land", -sum(k for k, _ in groups[g])))
    P += [f"- [{g}](#{re.sub(r'[^a-z0-9 -]', '', g.lower()).replace(' ', '-')})" for g in order] + ["- [Grixis rules insights (from the source)](#grixis-rules-insights-from-the-source)", ""]
    for g in order:
        items = sorted([x for x in groups[g] if x[0] >= 4], key=lambda x: (-x[0], x[1]))
        P += [f"## {g}", "", f"{len(groups[g])} distinct cards carry this role across the {N} lists; {len(items)} appear in 4 or more.", ""]
        if items:
            P += ["| Card | Lists | Identity | MV | GC |", "|---|---|---|---|---|"]
            P += [f"| {rel_link(rows[n], '../')} | {k}/{N} | {rows[n]['ci']} | {int(rows[n]['mv'])} | {'✅' if rows[n]['gc'] else ''} |" for k, n in items[:40]]
        P.append("")
    P += ["## Grixis rules insights (from the source)", "",
          "> Rules interactions the source author worked out and relied on. Each one is quoted with its source path and checked against the Oracle text in our card entries (quoted below). How to *use* them is guidance.", ""]
    def ot(n):
        c = by_name[n]
        return (c.get("oracle_text") or " // ".join(f.get("oracle_text", "") for f in c.get("card_faces") or [])).replace("\n", " ")
    def lk(n):
        r = index[by_name[n]["oracle_id"]]
        return f"[{n}](../{r['shard']}#{r['anchor']})"
    staff = "Wizard's Staff"
    staff_line = next(x for x in by_name[staff]["oracle_text"].split("\n") if "additional time" in x)
    ghy_line = next(x for x in by_name["Ghyrson Starn, Kelermorph"]["oracle_text"].split("\n") if "exactly 1" in x)
    cec_line = next(x for x in by_name["Cecily, Haunted Mage"]["oracle_text"].split("\n") if "attacks" in x)
    P += [f"- **Trigger multipliers are additive, not multiplicative.** In the Nekusar build the source found that {lk(staff)} (\"{staff_line}\") and {lk('Harmonic Prodigy')} add instances of *both* Nekusar triggers, while {lk('Krang, the All-Powerful')} (\"{ot('Krang, the All-Powerful').split('. ')[0]}.\") adds one only to the draw-caused damage trigger, not to the draw-step trigger. Source: `refinement/decisions/Nekusar_the_Mindrazer_Candidate_Decisions_2026-10-15.md`.",
          f"- **Damage replacement can break exact-damage payoffs.** The same source file cuts Solphim, Mayhem Dominus because doubling Nekusar's 1 damage stops {lk('Ghyrson Starn, Kelermorph')} from seeing an event of exactly 1 damage. Oracle: \"{ghy_line.rstrip('.')}.\"",
          f"- **Attack triggers come before combat-damage draws.** For {lk('Cecily, Haunted Mage')} (\"{cec_line}\") the source notes that a combat-damage draw such as {lk('Robe of the Archmagi')} resolves *after* her attack trigger. So it cannot meet the eleven-card check on the same attack. Source: `refinement/evidence/Cecily__Bjorna__Lutri_Approval_Gate_Dossier_2026-10-13.md`.",
          f"- **\"Cast from hand\" clauses still work with free casts.** {lk('Apex of Power')} cast for free through Cecily's trigger is still cast from hand, so its hand clause applies. \"Without paying its mana cost\" bars alternative costs but allows additional costs (CR 118.9a, 118.9d). Same source file.", ""]
    (OUT / "Grixis Packages.md").write_text("\n".join(P) + "\n", encoding="utf-8")
    # ---------------- section index
    R = ["# Grixis (U/B/R) Commander", "",
         "> 🎯 **Mission (Cory, Bot cycle 39):** every one of the 62 decks must be the definitive, maximally optimized version of *that commander's* deck, "
         "not a strong Grixis shell. Commander identity first, optimization up to the commander's natural ceiling, no homogenization, complete verification. "
         "Full text: [Grixis Mission](Grixis%20Mission.md) · progress: [Grixis Refinement Cycle](Grixis%20Refinement%20Cycle.md) · "
         "Archidekt files: [exports/grixis-archidekt/](../exports/grixis-archidekt/README.md).", "",
         f"> **Bot cycle 16 import, refreshed in Bot cycle 37** (all 62 source lists are now APPROVED/LOCKED in the source). This section brings in the user's Grixis Commander work from [grixis-commander-encyclopediaGPT]({REPO}) (commit `{SRC_SHA}`, read-only): the user-approved, refined decklists, each with its commander-first blueprint, swap decisions and approval record quoted verbatim. Each list was re-validated against our card DB, corrected where needed, and given Game Changer counts, bracket floors and Commander Spellbook combos. Source analysis is **the source author's guidance**. Our facts come from Scryfall and Commander Spellbook. Built by `scripts/build_grixis.py`. Related: [EDH Standards](../EDH%20Standards.md) · [EDH Deck Template](../EDH%20Deck%20Template.md) · [EDH Deck Evaluation Checklist](../EDH%20Deck%20Evaluation%20Checklist.md) · [Grixis mana base](../EDH%20Mana%20Bases.md) · [data-derived Nekusar skeleton](../decks/nekusar-the-mindrazer.md)", "",
         "> 🏛️ **Authority layer (Bot cycle 47, M0):** every deck has **one canonical project list** and a state in the "
         "[authority registry](../data/grixis/registry.json). All 62 start at `SOURCE_BASELINE` (2 at `PENDING_RELEASE`); the source's approvals and our "
         "cycle 39–44 refinements are evidence and *GrokBot challengers (unapproved)*, not approvals. Nothing becomes APPROVED or CANONICAL_LOCKED without "
         "Cory's explicit sign-off. Model and rules: [Grixis Authority Model](Grixis%20Authority%20Model.md).", "",
         "> 🗄️ **Single source of truth (Bot cycle 45):** the companion now holds the **complete source repository** in "
         "[source-archive/](source-archive/README.md): every file at commit `" + SRC_SHA + "`, byte-identical (SHA-256 manifest, checked by "
         "`validate_all`), plus a git bundle with all branches and history. The archive is inert data; generators read it instead of a separate "
         "clone. The original GitHub repo stays untouched.", "",
         "## Contents", "- [Pages](#pages)", "- [Decks](#decks)", "- [Project exceptions](#project-exceptions)", "- [Pending legality](#pending-legality)", "- [What was left out](#what-was-left-out)", "",
         "## Pages", "",
         "| Page | What it holds |", "|---|---|",
         "| [Grixis Integration Summary](Grixis%20Integration%20Summary.md) | What was integrated, what was generalized, and follow-ups |",
         "| [Grixis Mission](Grixis%20Mission.md) | Cory's commander-first mission and principles (Bot cycle 39) |",
         "| [Grixis Authority Model](Grixis%20Authority%20Model.md) | Bot cycle 47 (M0): authority hierarchy, deck states, evidence classes, legality vs project authorization, Cory's binding rules, milestone acceptance criteria |",
         "| [Grixis Authority Gap Analysis](Grixis%20Authority%20Gap%20Analysis.md) | The approved gap analysis of Cory's authority brief (24 sections) and the M0–M8 plan |",
         "| [Grixis Refinement Cycle](Grixis%20Refinement%20Cycle.md) | Commander-dependence and homogenization metrics for all 62 decks, batch log, per-deck swaps |",
         "| [exports/grixis-archidekt/](../exports/grixis-archidekt/README.md) | Archidekt import files, each labeled: source baseline (canonical) or GrokBot challenger (unapproved); derived compliance projections; `index.json` manifest |",
         "| [source-archive/](source-archive/README.md) | Full byte-identical archive of the source repo (Bot cycle 45): area map, SHA-256 manifest, history bundle |",
         f"| [Grixis Evaluation](Grixis%20Evaluation.md) | Check results for all {len(evaluation)} source lists, and how each current list was chosen |",
         f"| [Grixis Corrections](Grixis%20Corrections.md) | All {len(corrections)} corrections (deck, issue, fix), the Oracle-text check, source-repo structural findings |",
         f"| [Grixis Packages](Grixis%20Packages.md) | Cross-deck package library (cards shared by 4 or more of the {N} lists, by role) and verified rules insights |",
         f"| [decks/](decks/) | {len(integrated)} deck pages: {N} validated (legal) + {len(excd)} 🚩 with project exceptions + {len(pending)} ⏳ pending legality |", "",
         "## Decks", "",
         "*Themes* are the source's Archidekt tags where it recorded them. *Source bracket* is the source author's stated target (guidance). *Floor* is the minimum by the official barometers (Game Changers, mass land denial, two-card infinites).", "",
         "| Deck | Themes (source) | GC | Floor | Source bracket | Spellbook combos / 2-card ∞ | Lands | Avg MV | Fixes |", "|---|---|---|---|---|---|---|---|---|"]
    for did, d in sorted(legal.items(), key=lambda kv: kv[1]["commanders"][0]):
        R.append(f"| [{' + '.join(d['commanders'])}](decks/{d['slug']}.md) | {d['themes'] or '—'} | {len(d['gcs'])} | {d['cfloor']} | {d['src_claim'] or '—'} | {d['n_combos']} / {d['n_two']} | {d['lands']} | {d['avg_mv']:.2f} | {len(d['fixes'])} |")
    R += ["", "## Project exceptions", "",
          f"{len(excd)} deck(s) keep Cory-authorized project exceptions in their canonical project list. They are **not Commander-legal** and are not counted among the {N} legal decks above or in [Grixis Packages](Grixis%20Packages.md). Registry: `data/grixis/exceptions.json`; officially legal version: the deck page's derived compliance projection (not canonical).", "",
          "| Deck | Exceptions (not Commander-legal) | GC | Floor | Source bracket | Lands |", "|---|---|---|---|---|---|"]
    for did, d in sorted(excd.items(), key=lambda kv: kv[1]["commanders"][0]):
        R.append(f"| 🚩 [{' + '.join(d['commanders'])}](decks/{d['slug']}.md) | {'; '.join(x['card'] + ' (' + x['official_commander_legality'].replace('_', ' ') + ')' for x in d['exceptions'])} | {len(d['gcs'])} | {d['cfloor']} | {d['src_claim'] or '—'} | {d['lands']} |")
    R += ["", "## Pending legality", "",
          f"{len(pending)} deck page(s) are published with `legality_status: pending`. They are **not counted** among the {N} legal decks above or in [Grixis Packages](Grixis%20Packages.md). Each lists the cards that are not Commander-legal yet. Activation: `python3 scripts/activate_pending_grixis.py` (Bot cycle 38).", "",
          "| Deck | Not yet legal | Legal from | GC | Floor | Source bracket | Lands |", "|---|---|---|---|---|---|---|"]
    for did, d in sorted(pending.items(), key=lambda kv: kv[1]["commanders"][0]):
        R.append(f"| ⏳ [{' + '.join(d['commanders'])}](decks/{d['slug']}.md) | {', '.join(d['pending']['cards'])} | {d['pending']['legal_from']} | {len(d['gcs'])} | {d['cfloor']} | {d['src_claim'] or '—'} | {d['lands']} |")
    R += ["", "## What was left out", "",
          f"{len(evaluation) - len(integrated)} of {len(evaluation)} source lists are left out. Their check results are in [Grixis Evaluation](Grixis%20Evaluation.md#per-list-results).", ""]
    for did, d, hard, why in evaluation:
        if why:
            R.append(f"- **{' + '.join(d['commanders'])}** (`{did}`): {why}")
    R.append("")
    (OUT / "README.md").write_text("\n".join(R) + "\n", encoding="utf-8")
    with atomic_io.atomic_open(ROOT / "data/grixis_summary.json", "w") as fh:
        json.dump({did: {k: d[k] for k in ("slug", "themes", "commanders", "ci", "gcs", "floor", "cfloor", "n_combos", "n_two", "src_claim", "lands", "avg_mv", "source_path")} | {"fixes": len(d["fixes"]), "legality_status": "pending" if d.get("pending") else "project_exception" if d.get("exceptions") else "legal"}
                   for did, d in integrated.items()}, fh, indent=1, ensure_ascii=False)
    print(json.dumps({"pages": len(integrated), "legal": len(legal), "pending": len(pending), "integrated": len(integrated), "left_out": len(evaluation) - len(integrated), "corrections": len(corrections), "kinds": kinds}, default=str))


if __name__ == "__main__":
    main()
