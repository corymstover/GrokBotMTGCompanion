#!/usr/bin/env python3
"""Grixis interaction reviews (Bot cycle 46, phase 2): one detailed, cited rules review per deck.

Data:    data/grixis_interactions/<slug>.json   (schema: grixis/interactions/README.md#data-format)
         data/grixis_interactions/_batches.json  (batch plan: A–F, alphabetical, ~12 decks each; status per batch)
Renders: grixis/interactions/<slug>.md          (full review)
         data/grixis_interactions/edges/<slug>.json (machine-readable edges for the M4 graph, Bot cycle 58;
                                                    schema data/grixis/schemas/interaction_edges.schema.json)
         grixis/decks/<slug>.md                  <!-- INTERACTIONS --> "Rules notes" block (key rulings + flags)
         grixis/interactions/README.md           status table between <!-- INTERACTIONS-STATUS --> markers

Every citation is machine-checked (`--check`, a validate_all step):
  * deck_sha256 = SHA-256 of the deck's canonical project list: the M0 registry's canonical_project_list.export
    (data/grixis/registry.json), which is exports/grixis-archidekt/<slug>.txt except for the decks whose canonical
    list is a source baseline (exports/grixis-archidekt/source-baseline/<slug>.txt); list_source must name it;
  * every interaction has an evidence_class from the seven M0 authority classes;
  * every card named in an interaction is in that list (or listed in `absent` / the companion);
  * every CR rule number exists in the cached Comprehensive Rules (version must match `cr_version`);
  * every Oracle quote is verbatim in the card's current Oracle text (Scryfall oracle bulk);
  * every ruling quote is verbatim in the card's current Scryfall rulings (rulings bulk);
  * every source reference points at an archived file (grixis/source-archive/...) and, for attestation JSON,
    at an interaction name that exists there; for Markdown sources the quoted text must be in the file;
  * decks in batches marked done all have a review; rendered pages and deck-page blocks are current;
  * (Bot cycle 58) each review's edge file is current, schema-valid, has a hub per ruling and >= 1 pair edge;
  * (Bot cycle 58) every archived Rules_Attestation item is cited by a review or dispositioned with a reason
    in data/grixis_interactions/_attestation_dispositions.json.
Usage:
  python3 scripts/grixis_interactions.py                 render all reviews, deck-page blocks, README status
  python3 scripts/grixis_interactions.py --check         validate (no writes)
  python3 scripts/grixis_interactions.py --dossier SLUG  print a working dossier (Oracle text, rulings, combos,
                                                          source attestations) for writing a review
"""
import atomic_io  # noqa: F401
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402
from evaluate_decklist import Resolver, oracle as oracle_text  # noqa: E402
import grixis_archive  # noqa: E402
from check_links import anchor  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "grixis_interactions"
OUT = ROOT / "grixis" / "interactions"
DECKS = ROOT / "grixis" / "decks"
EXPORTS = ROOT / "exports" / "grixis-archidekt"
ARCH = grixis_archive.TREE
CR_URL = "https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt"
START, END = "<!-- INTERACTIONS:START -->", "<!-- INTERACTIONS:END -->"
SSTART, SEND = "<!-- INTERACTIONS-STATUS:START -->", "<!-- INTERACTIONS-STATUS:END -->"
CATS = [("commander", "Commander rules text and edge cases"), ("combo", "Combos and engine lines"),
        ("engine", "Engines and payoffs"), ("pair", "Key card-pair interactions"),
        ("layers", "Layers and continuous effects"), ("timing", "Timing and priority"),
        ("replacement", "Replacement and prevention effects"), ("trigger-order", "Trigger ordering"),
        ("zone", "Zones, commander tax and the command zone"), ("dependency", "What the list depends on"),
        ("legality", "Legality and project exceptions")]
CAT_IDS = [c for c, _ in CATS]
STATUS = {"verified": "✅ verified", "uncertain": "⚠️ uncertain", "flag": "🚩 list flag"}
SPELLBOOK = ROOT / "data" / "grixis_spellbook_steps.json"
# Evidence classes (M0 authority foundation). Required on every interaction since Bot cycle 49 (M0 on main).
EVIDENCE = {"fact", "derived_metric", "heuristic", "hypothesis", "test_result", "strategic_judgment", "approved_decision"}
FLAG_KINDS = {"non-bo", "anti-synergy", "misunderstood-combo", "dead-card", "dependency-risk", "documentation", "other"}


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("−", "-").replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip()


class Ctx:
    def __init__(self):
        self.R = Resolver()
        rulings, self.rdate = ing.get_bulk(ing.DEFAULT_CACHE, None, kind="rulings")
        self.rul = {}
        for r in rulings:
            self.rul.setdefault(r["oracle_id"], []).append(r)
        crf = sorted((ROOT / ".cache").glob("MagicCompRules-*.txt"))[-1]
        self.cr_version = f"{crf.stem[-8:-4]}-{crf.stem[-4:-2]}-{crf.stem[-2:]}"
        self.cr = {}
        for line in crf.read_text(encoding="utf-8-sig").splitlines():
            m = re.match(r"^(\d{3}(?:\.\d+[a-z]?)?)\.? (.*)$", line.strip())
            if m and m.group(1) not in self.cr:
                self.cr[m.group(1)] = m.group(2)

    def card(self, name):
        c, _ = self.R.get(name)
        return c

    def rulings(self, name):
        c = self.card(name)
        return self.rul.get(c["oracle_id"], []) if c else []


REGISTRY = ROOT / "data" / "grixis" / "registry.json"
_REG = None


def list_path(slug):
    """Repo-relative path of the list a review must hash (Bot cycle 49, M1 on M0): the deck's
    `canonical_project_list.export` from the M0 authority registry (read-only here), else the legacy export."""
    global _REG
    if _REG is None:
        _REG = {}
        if REGISTRY.exists():
            for d in json.loads(REGISTRY.read_text(encoding="utf-8")).get("decks", {}).values():
                exp = (d.get("canonical_project_list") or {}).get("export")
                if d.get("slug") and exp:
                    _REG[d["slug"]] = exp
    return _REG.get(slug, f"exports/grixis-archidekt/{slug}.txt")


def deck_list(slug, with_companion=False):
    p = ROOT / list_path(slug)
    raw = p.read_bytes()
    cmd, main, comp = [], [], []
    for line in raw.decode("utf-8").splitlines():
        m = re.match(r"^(\d+) (.+?)(?: \[(Commander|Companion)\])?$", line.strip())
        if not m:
            continue
        {"Commander": cmd, "Companion": comp}.get(m.group(3), main).append(m.group(2))
    if with_companion:
        return cmd, main, comp, hashlib.sha256(raw).hexdigest()
    return cmd, main, hashlib.sha256(raw).hexdigest()


def summary():
    return json.loads((ROOT / "data" / "grixis_summary.json").read_text(encoding="utf-8"))


def slug_to_id():
    return {v["slug"]: k for k, v in summary().items()}


# ---------------------------------------------------------------- dossier (authoring aid, prints only)
def dossier(slug, ctx):
    did = slug_to_id()[slug]
    cmd, main, h = deck_list(slug)
    out = [f"# {slug}  ({did})  sha256 {h}", f"CR {ctx.cr_version} · rulings bulk {ctx.rdate[:10]}", ""]
    for n in cmd:
        c = ctx.card(n)
        out += [f"## COMMANDER {n}  {c.get('mana_cost') or ''}  {c['type_line']}", oracle_text(c), ""]
        out += ["  R: " + r["comment"] for r in ctx.rulings(n)] + [""]
    combos = json.loads((ROOT / "data" / "grixis_combos.json").read_text(encoding="utf-8"))["decks"].get(did, {})
    have = set(cmd) | set(main)
    out.append("## COMBOS (Spellbook, source list; [x] = all pieces in final list)")
    for k in combos.get("combos", []):
        ok = all(any(x == y or y.startswith(x + " //") for y in have) for x in k["cards"])
        out.append(f"  [{'x' if ok else ' '}] {k['id']}: {' + '.join(k['cards'])} → {', '.join(k['produces'][:4])}")
        v = spellbook().get(k["id"], {})
        if ok and v.get("steps"):
            out.append("      prereq: " + " | ".join(x for x in (v.get("easy_prerequisites", ""), v.get("notable_prerequisites", "")) if x).replace("\n", " | "))
            out.append("      steps: " + v["steps"].replace("\n", " | "))
    out.append("")
    out.append("## CARDS")
    for n in sorted(set(main)):
        c = ctx.card(n)
        if not c or "Basic Land" in c["type_line"]:
            continue
        t = oracle_text(c).replace("\n", " / ")
        out.append(f"- **{n}** {c.get('mana_cost') or ''} · {c['type_line']} · {t}")
    out.append("")
    out.append("## SOURCE ATTESTATIONS")
    for f in sorted(ARCH.rglob("*Rules_Attestation*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        ids = [x.get("deck_id") for x in d.get("decks", [])]
        if did in ids or (d.get("interactions") and did.split("_")[0].lower() in f.name.lower()):
            out.append(f"### {f.relative_to(ARCH)}")
            for it in d.get("interactions", []):
                out.append(f"  - [{it.get('status')}] {it['name']}: {it.get('note', '')}")
            for x in d.get("decks", []):
                if x.get("deck_id") == did:
                    out.append(f"  - deck entry: {x}")
    print("\n".join(out))


_SB = None


def spellbook():
    """Cached Commander Spellbook variants (data/grixis_spellbook_steps.json), keyed by id."""
    global _SB
    if _SB is None:
        _SB = json.loads(SPELLBOOK.read_text(encoding="utf-8"))["variants"] if SPELLBOOK.exists() else {}
    return _SB


# ---------------------------------------------------------------- validation
def validate(slug, d, ctx):
    bad = []
    cmd, main, comp, h = deck_list(slug, with_companion=True)
    have = set(cmd) | set(main) | set(d.get("companion", []))
    if d.get("list_source") != list_path(slug):
        bad.append(f"list_source {d.get('list_source')} ≠ canonical project list {list_path(slug)} (M0 registry)")
    if comp and sorted(d.get("companion", [])) != sorted(comp):
        bad.append(f"companion {d.get('companion')} ≠ list companion {comp}")
    absent = set(d.get("absent", []))
    if d.get("deck_sha256") != h:
        bad.append(f"deck_sha256 {str(d.get('deck_sha256'))[:12]} ≠ current list {h[:12]} (re-review the changed cards)")
    if d.get("cr_version") != ctx.cr_version:
        bad.append(f"cr_version {d.get('cr_version')} ≠ cached CR {ctx.cr_version}")
    if d.get("commanders") != cmd:
        bad.append(f"commanders {d.get('commanders')} ≠ list {cmd}")
    seen = set()
    for it in d.get("interactions", []):
        i = it.get("id", "?")
        if i in seen:
            bad.append(f"{i}: duplicate id")
        seen.add(i)
        for k in ("title", "category", "cards", "ruling", "status"):
            if not it.get(k):
                bad.append(f"{i}: missing {k}")
        if it.get("category") not in CAT_IDS:
            bad.append(f"{i}: unknown category {it.get('category')}")
        if it.get("status") not in STATUS:
            bad.append(f"{i}: unknown status {it.get('status')}")
        if it.get("status") == "flag" and (not it.get("flag") or it["flag"].get("kind") not in FLAG_KINDS):
            bad.append(f"{i}: flag needs flag.kind in {sorted(FLAG_KINDS)} and flag.note")
        if it.get("status") == "uncertain" and not it.get("uncertainty"):
            bad.append(f"{i}: uncertain needs an `uncertainty` note")
        if not (it.get("cr") or it.get("oracle") or it.get("rulings") or it.get("spellbook")):
            bad.append(f"{i}: no citation (cr / oracle / rulings)")
        for n in it.get("cards", []):
            if n not in have and n not in absent and not any(x.startswith(n + " //") for x in have):
                bad.append(f"{i}: card not in current list: {n}")
        for r in it.get("cr", []):
            if r not in ctx.cr:
                bad.append(f"{i}: CR {r} does not exist in CR {ctx.cr_version}")
        for q in it.get("oracle", []):
            c = ctx.card(q["card"])
            if not c:
                bad.append(f"{i}: unknown card {q['card']}")
            elif norm(q["quote"]) not in norm(oracle_text(c)):
                bad.append(f"{i}: Oracle quote not verbatim for {q['card']}: {q['quote'][:60]}")
        for q in it.get("rulings", []):
            if not any(norm(q["quote"]) in norm(r["comment"]) for r in ctx.rulings(q["card"])):
                bad.append(f"{i}: ruling quote not found for {q['card']}: {q['quote'][:60]}")
        if it.get("evidence_class") not in EVIDENCE:
            bad.append(f"{i}: evidence_class {it.get('evidence_class')!r} not in {sorted(EVIDENCE)} (required since M0)")
        for q in it.get("spellbook", []):
            v = spellbook().get(q.get("id"))
            if not v or not v.get("steps"):
                bad.append(f"{i}: Spellbook variant {q.get('id')} not cached (run scripts/spellbook_steps.py --ids {q.get('id')})")
            elif q.get("quote") and norm(q["quote"]) not in norm("\n".join([v.get("steps", ""), v.get("notable_prerequisites", ""), v.get("easy_prerequisites", "")])):
                bad.append(f"{i}: Spellbook step quote not in {q['id']}: {q['quote'][:60]}")
        for s in it.get("source", []):
            p = ARCH / s["path"]
            if not p.exists():
                bad.append(f"{i}: source file missing: {s['path']}")
            elif p.suffix == ".json" and s.get("item"):
                names = [x.get("name") for x in json.loads(p.read_text(encoding="utf-8")).get("interactions", [])]
                if s["item"] not in names:
                    bad.append(f"{i}: source interaction not in {p.name}: {s['item'][:50]}")
            elif s.get("quote") and norm(s["quote"]) not in norm(p.read_text(encoding="utf-8")):
                bad.append(f"{i}: source quote not in {p.name}: {s['quote'][:50]}")
    return bad


# ---------------------------------------------------------------- edges (Bot cycle 58, M1 → M4)
EDGES = DATA / "edges"
EDGE_SCHEMA = "interaction_edges.schema.json"
EDGE_RULE = "edges-v1"
# Relation kinds. Those that are also graph.schema.json edge kinds map 1:1 (graph_kind); the review-layer relations
# (combo_with, interacts_with, conflicts_with) have graph_kind null and are kept by M4 as annotations / evidence.
GRAPH_KINDS = {"piece_of", "member_of", "enables", "tutors_for", "protects", "recurs", "fuels", "payoff_of", "fixes", "redundant_with"}
REVIEW_KINDS = {"combo_with", "interacts_with", "conflicts_with"}
SYMMETRIC = {"combo_with", "interacts_with", "conflicts_with", "redundant_with"}


def _canon(name, listed):
    """List spelling of a card the review names (a front-face name maps to its full `A // B` list entry)."""
    if name in listed:
        return name, True
    for x in listed:
        if x.startswith(name + " //"):
            return x, True
    return name, False


def build_edges(slug, d, review_bytes):
    """Deterministic edge document for one review (rule edges-v1; see grixis/interactions/README.md#edges).

    * every ruling → one hub node: combo:<slug>/<id> for combo rulings, interaction:<slug>/<id> otherwise;
    * membership: each card the ruling names → hub (piece_of for combos, member_of otherwise), graph-native kinds;
    * pair: each other card → the ruling's anchor (the commander if the ruling names one, else its first card):
      conflicts_with for anti-synergy flags, else combo_with for combos, else interacts_with (symmetric, derived);
    * a ruling may carry authored `edges` ([{from, to, kind}], card names) that replace its pair edges.
    """
    cmd, main, comp, h = deck_list(slug, with_companion=True)
    listed = list(cmd) + list(main) + list(comp)
    cmds = set(cmd)
    nodes, seen, edges = [], set(), []
    rel = f"data/grixis_interactions/{slug}.json"

    def nid(name):
        n, ok = _canon(name, listed)
        i = ("commander:" if n in cmds else "card:") + n
        if i not in seen:
            seen.add(i)
            nodes.append({"id": i, "kind": "commander" if n in cmds else "card", "name": n, "in_list": ok})
        return i

    def edge(eid, a, b, kind, layer, x, ev):
        return {"id": eid, "from": a, "to": b, "kind": kind, "graph_kind": kind if kind in GRAPH_KINDS else None,
                "layer": layer, "symmetric": kind in SYMMETRIC, "interaction": x["id"], "topic": x["category"],
                "status": x["status"], "flag_kind": (x.get("flag") or {}).get("kind"),
                "evidence_class": ev, "cr": list(x.get("cr", [])), "evidence": refs(x)}

    def refs(x):
        r = [f"review:{rel}#{x['id']}"] + [f"cr:{c}" for c in x.get("cr", [])]
        r += [f"spellbook:{q['id']}" for q in x.get("spellbook", [])]
        return r

    for x in d["interactions"]:
        combo = x["category"] == "combo"
        names = list(dict.fromkeys(x["cards"]))
        hub = ("combo:" if combo else "interaction:") + f"{slug}/{x['id']}"
        ids = [nid(n) for n in names]
        hn = {"id": hub, "kind": "combo" if combo else "interaction", "interaction": x["id"], "topic": x["category"],
              "status": x["status"], "flag_kind": (x.get("flag") or {}).get("kind"), "evidence_class": x["evidence_class"]}
        if x.get("spellbook"):
            hn["spellbook"] = [q["id"] for q in x["spellbook"]]
        nodes.append(hn)
        for k, i in enumerate(ids, 1):
            edges.append(edge(f"{x['id']}:m{k}", i, hub, "piece_of" if combo else "member_of", "membership", x, x["evidence_class"]))
        if x.get("edges"):
            for k, e in enumerate(x["edges"], 1):
                edges.append(edge(f"{x['id']}:a{k}", nid(e["from"]), nid(e["to"]), e["kind"], "authored", x, x["evidence_class"]))
            continue
        if len(ids) < 2:
            continue
        anchor = next((i for i in ids if i.startswith("commander:")), ids[0])
        kind = ("conflicts_with" if (x.get("flag") or {}).get("kind") == "anti-synergy"
                else "combo_with" if combo else "interacts_with")
        for k, i in enumerate([i for i in ids if i != anchor], 1):
            edges.append(edge(f"{x['id']}:p{k}", i, anchor, kind, "pair", x, "derived_metric"))
    return {"schema_version": 1, "generated_by": "scripts/grixis_interactions.py", "rule_version": EDGE_RULE,
            "deck_id": d["deck_id"], "slug": slug, "deck_sha256": d["deck_sha256"], "review": rel,
            "review_sha256": hashlib.sha256(review_bytes).hexdigest(), "cr_version": d["cr_version"],
            "counts": {"interactions": len(d["interactions"]), "nodes": len(nodes),
                       "membership_edges": sum(1 for e in edges if e["layer"] == "membership"),
                       "pair_edges": sum(1 for e in edges if e["layer"] != "membership")},
            "nodes": nodes, "edges": edges}


def edges_text(doc):
    return json.dumps(doc, indent=1, ensure_ascii=False) + "\n"


def validate_edges(slug, d, doc):
    """Schema + semantic checks of one edge document (the stale check separately enforces regeneration)."""
    import grixis_authority as ga
    bad = [f"edges: {e}" for e in ga.validate(doc, ga.load_schema(EDGE_SCHEMA), EDGE_SCHEMA)]
    ids = {n["id"] for n in doc["nodes"]}
    ints = {x["id"] for x in d["interactions"]}
    hubbed = {n["interaction"] for n in doc["nodes"] if n["kind"] in ("combo", "interaction")}
    if hubbed != ints:
        bad.append(f"edges: rulings without a hub node: {sorted(ints - hubbed)}")
    for e in doc["edges"]:
        if e["from"] not in ids or e["to"] not in ids:
            bad.append(f"edges: {e['id']} points at an unknown node")
        if e["interaction"] not in ints:
            bad.append(f"edges: {e['id']} names unknown ruling {e['interaction']}")
    for x in d["interactions"]:
        for e in x.get("edges", []):
            if e.get("kind") not in GRAPH_KINDS | REVIEW_KINDS:
                bad.append(f"{x['id']}: authored edge kind {e.get('kind')!r} not in {sorted(GRAPH_KINDS | REVIEW_KINDS)}")
            for n in (e.get("from"), e.get("to")):
                if n not in x["cards"]:
                    bad.append(f"{x['id']}: authored edge card {n!r} is not one of the ruling's cards")
    if not any(e["layer"] != "membership" for e in doc["edges"]):
        bad.append("edges: no pair edges (every review needs at least one card → card/commander edge)")
    return bad


# ---------------------------------------------------------------- source attestation coverage (M1 criterion)
DISPOSITIONS = DATA / "_attestation_dispositions.json"
DISPOSITION_KINDS = {"not_applicable", "covered_elsewhere"}


def attestation_coverage(reviews):
    """Every interaction in every archived *Rules_Attestation*.json must be cited by a review (`source` → item,
    i.e. folded in) or carry an explicit disposition with a reason in _attestation_dispositions.json."""
    items = []
    for f in sorted(ARCH.rglob("*Rules_Attestation*.json")):
        rp = str(f.relative_to(ARCH))
        for it in json.loads(f.read_text(encoding="utf-8")).get("interactions", []):
            items.append((rp, it["name"]))
    cited = {(s["path"], s["item"]) for r in reviews.values() for x in r["interactions"] for s in x.get("source", []) if s.get("item")}
    disp = json.loads(DISPOSITIONS.read_text(encoding="utf-8"))["dispositions"] if DISPOSITIONS.exists() else []
    dk = {(x["path"], x["item"]): x for x in disp}
    bad = []
    for x in disp:
        k = (x["path"], x["item"])
        if k not in set(items):
            bad.append(f"attestations: disposition for unknown item {x['path']} → {x['item']}")
        if k in cited:
            bad.append(f"attestations: {x['item']} is both cited and dispositioned ({x['path']})")
        if x.get("disposition") not in DISPOSITION_KINDS or not x.get("reason"):
            bad.append(f"attestations: {x['item']} needs disposition in {sorted(DISPOSITION_KINDS)} and a reason")
    missing = [k for k in items if k not in cited and k not in dk]
    bad += [f"attestations: not folded in or dispositioned: {p} → {n}" for p, n in missing]
    n_cited = sum(1 for k in set(items) if k in cited)
    return {"files": len({p for p, _ in items}), "items": len(items), "cited": n_cited,
            "dispositioned": sum(1 for k in set(items) if k in dk and k not in cited), "missing": len(missing)}, bad


# ---------------------------------------------------------------- rendering
def eid(x):
    """Heading anchor of an interaction entry (matches check_links.anchor)."""
    return anchor(f"{x['id']}: {x['title']}")


def crid(r):
    return anchor(f"CR {r}")


def render(slug, d, ctx):
    cmd, main, h = deck_list(slug)
    its = d["interactions"]
    n_flag = sum(1 for x in its if x["status"] == "flag")
    n_unc = sum(1 for x in its if x["status"] == "uncertain")
    name = " + ".join(cmd)
    L = ["---", f'title: "{name} — Interaction Review"', "category: rules", "tags: [grixis, interactions, rulings]",
         "generated_by: scripts/grixis_interactions.py", "sources: [cr, scryfall, grixis-repo]", "schema: 2", "---", "",
         f"# {name} — Interaction Review", "",
         f"> Bot cycle {d['cycle']} · batch {d['batch']} · reviewed {d['reviewed']}. Deck: [{name}](../decks/{slug}.md) · method and format: [Interaction reviews](README.md). "
         f"Every ruling below was checked against current Oracle text (Scryfall oracle bulk {ctx.R.bulk[:10]}), Scryfall rulings (bulk {ctx.rdate[:10]}) and the "
         f"[Comprehensive Rules]({CR_URL}) effective {ctx.cr_version}; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. "
         "Source attestations from the archived source repo were re-verified, not copied.", "",
         "| | |", "|---|---|",
         f"| Canonical project list | [`{list_path(slug)}`](../../{list_path(slug)}) · SHA-256 `{h}` |",
         f"| Rulings | **{len(its)}** ({len(its) - n_flag - n_unc} verified · {n_unc} uncertain · {n_flag} flags) |",
         f"| CR / Oracle / rulings | CR {ctx.cr_version} · Oracle {ctx.R.bulk[:10]} · rulings {ctx.rdate[:10]} |"]
    if d.get("source_attestations"):
        L.append("| Source attestations | " + " · ".join(f"[`{s['path'].rsplit('/', 1)[-1]}`](../source-archive/grixis-commander-encyclopediaGPT/{s['path']}) ({s['note']})" for s in d["source_attestations"]) + " |")
    L += ["", "## Contents", "- [Summary](#summary)"]
    flags = [x for x in its if x["status"] in ("flag", "uncertain")]
    if flags:
        L.append("- [Flags and open questions](#flags-and-open-questions)")
    cats = [c for c in CATS if any(x["category"] == c[0] for x in its)]
    L += [f"- [{t}](#{anchor(t)})" for _, t in cats]
    L += ["- [Rules cited](#rules-cited)", "", "## Summary", "", d["summary"], ""]
    if flags:
        L += ["## Flags and open questions", "", "Input for later refinement. **No decklist was changed in this phase.**", "",
              "| # | Status | Interaction | Note |", "|---|---|---|---|"]
        for x in flags:
            note = x["flag"]["note"] if x["status"] == "flag" else x["uncertainty"]
            kind = f" ({x['flag']['kind']})" if x["status"] == "flag" else ""
            L.append(f"| [{x['id']}](#{eid(x)}) | {STATUS[x['status']]}{kind} | {x['title']} | {note} |")
        L.append("")
    for cid, t in cats:
        L += [f"## {t}", ""]
        for x in [y for y in its if y["category"] == cid]:
            L += [f"### {x['id']}: {x['title']}", "",
                  f"**Status:** {STATUS[x['status']]}" + (f" · **Evidence:** {x['evidence_class']}" if x.get("evidence_class") else "") + " · **Cards:** " + ", ".join(x["cards"]), ""]
            if x.get("question"):
                L += [f"**Question.** {x['question']}", ""]
            L += [f"**Ruling.** {x['ruling']}", ""]
            if x.get("uncertainty"):
                L += [f"**Uncertain.** {x['uncertainty']}", ""]
            if x.get("flag"):
                L += [f"**List flag ({x['flag']['kind']}).** {x['flag']['note']}", ""]
            cit = []
            for q in x.get("oracle", []):
                cit.append(f"- Oracle, *{q['card']}*: “{q['quote']}”")
            for q in x.get("rulings", []):
                cit.append(f"- Scryfall ruling, *{q['card']}*: “{q['quote']}”")
            if x.get("cr"):
                cit.append("- " + ", ".join(f"[CR {r}](#{crid(r)})" for r in x["cr"]))
            for q in x.get("spellbook", []):
                v = spellbook().get(q["id"], {})
                cit.append(f"- Commander Spellbook [{q['id']}]({v.get('url', 'https://commanderspellbook.com/combo/' + q['id'] + '/')}) (community-maintained, retrieved {v.get('retrieved', '?')})"
                           + (f": “{q['quote']}”" if q.get("quote") else ""))
            for s in x.get("source", []):
                cit.append(f"- Source (re-verified): [`{s['path'].rsplit('/', 1)[-1]}`](../source-archive/grixis-commander-encyclopediaGPT/{s['path']})"
                           + (f" → “{s['item']}”" if s.get("item") else "") + (f" → “{s['quote']}”" if s.get("quote") else ""))
            L += ["**Citations**", ""] + cit + [""]
    rules = sorted({r for x in its for r in x.get("cr", [])}, key=lambda r: [int(p) if p.isdigit() else p for p in re.findall(r"\d+|[a-z]", r)])
    L += ["## Rules cited", "", f"Verbatim from the [Comprehensive Rules]({CR_URL}) effective {ctx.cr_version} (long rules shortened with …).", ""]
    for r in rules:
        t = ctx.cr[r]
        t = t if len(t) <= 600 else t[:600].rsplit(" ", 1)[0] + " …"
        L += [f"#### CR {r}", "", t, ""]
    return "\n".join(L) + "\n"


def deck_block(slug, d):
    its = d["interactions"]
    key = [x for x in its if x.get("key")]
    fl = [x for x in its if x["status"] in ("flag", "uncertain")]
    L = [START, "## Rules notes", "",
         f"> Bot cycle {d['cycle']} interaction review: **{len(its)} rulings** checked against current Oracle text, Scryfall rulings and the Comprehensive Rules. "
         f"Full review with citations: [{' + '.join(d['commanders'])} — Interaction Review](../interactions/{slug}.md).", ""]
    for x in key:
        L.append(f"- **{x['title']}** — {x.get('short') or x['ruling']} ([{x['id']}](../interactions/{slug}.md#{eid(x)}))")
    if fl:
        L += ["", "**Flags for later refinement** (no list change in this phase):"]
        for x in fl:
            L.append(f"- {STATUS[x['status']]} {x['title']}: {x['flag']['note'] if x['status'] == 'flag' else x['uncertainty']} ([{x['id']}](../interactions/{slug}.md#{eid(x)}))")
    L.append(END)
    return "\n".join(L)


def inject(text, blk):
    text = re.sub(r"\n*" + re.escape(START) + r".*?" + re.escape(END) + r"\n*", "\n\n", text, flags=re.S)
    toc = "- [Rules notes](#rules-notes)\n"
    if blk:
        assert "\n\n<!-- COMBOS:START -->" in text
        text = text.replace("\n\n<!-- COMBOS:START -->", "\n\n" + blk + "\n\n<!-- COMBOS:START -->", 1)
        if toc not in text:
            text = text.replace("- [Combos (Commander Spellbook)](#combos-commander-spellbook)\n", toc + "- [Combos (Commander Spellbook)](#combos-commander-spellbook)\n", 1)
    else:
        text = text.replace(toc, "")
    return text


def status_table(reviews, batches):
    summ = summary()
    order = sorted(summ.items(), key=lambda kv: kv[1]["slug"])
    done = sum(1 for _, v in order if v["slug"] in reviews)
    n = sum(len(r["interactions"]) for r in reviews.values())
    nf = sum(1 for r in reviews.values() for x in r["interactions"] if x["status"] == "flag")
    nu = sum(1 for r in reviews.values() for x in r["interactions"] if x["status"] == "uncertain")
    L = [SSTART, f"**{done}/{len(order)} decks reviewed · {n} rulings ({nu} uncertain, {nf} flags).**", "",
         "| Batch | Status | Decks |", "|---|---|---|"]
    for b, x in batches["batches"].items():
        L.append(f"| {b} | {x['status']}{' (Bot cycle ' + str(x['cycle']) + ')' if x.get('cycle') else ''} | " +
                 " · ".join((f"[{s}]({s}.md) ({len(reviews[s]['interactions'])})" if s in reviews else s) for s in x["decks"]) + " |")
    L.append(SEND)
    return "\n".join(L)


def load_reviews():
    return {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(DATA.glob("*.json")) if not p.name.startswith("_")}


def main(argv):
    ctx = Ctx()
    if "--dossier" in argv:
        dossier(argv[argv.index("--dossier") + 1], ctx)
        return 0
    check = "--check" in argv
    reviews = load_reviews()
    batches = json.loads((DATA / "_batches.json").read_text(encoding="utf-8"))
    slugs = {v["slug"] for v in summary().values()}
    problems, writes, n_edges = [], [], 0
    planned = [s for b in batches["batches"].values() for s in b["decks"]]
    if sorted(planned) != sorted(slugs):
        problems.append(f"_batches.json must list each of the {len(slugs)} decks exactly once")
    for b, x in batches["batches"].items():
        if x["status"] == "done":
            problems += [f"batch {b} is done but {s} has no review" for s in x["decks"] if s not in reviews]
    for slug, d in reviews.items():
        if slug not in slugs:
            problems.append(f"{slug}: not a Grixis deck slug")
            continue
        problems += [f"{slug}: {p}" for p in validate(slug, d, ctx)]
        writes.append((OUT / f"{slug}.md", render(slug, d, ctx)))
        try:
            doc = build_edges(slug, d, (DATA / f"{slug}.json").read_bytes())
            problems += [f"{slug}: {p}" for p in validate_edges(slug, d, doc)]
            writes.append((EDGES / f"{slug}.json", edges_text(doc)))
            n_edges += len(doc["edges"])
        except (KeyError, TypeError) as e:
            problems.append(f"{slug}: edges could not be built ({e!r})")
    for p in sorted(EDGES.glob("*.json")) if EDGES.exists() else []:
        if p.stem not in reviews:
            problems.append(f"edges/{p.name}: no review with that slug")
    cov, cbad = attestation_coverage(reviews)
    problems += cbad
    for slug in sorted(slugs):
        p = DECKS / f"{slug}.md"
        t = p.read_text(encoding="utf-8")
        writes.append((p, inject(t, deck_block(slug, reviews[slug]) if slug in reviews else None)))
    rp = OUT / "README.md"
    rt = rp.read_text(encoding="utf-8")
    rt = re.sub(re.escape(SSTART) + r".*?" + re.escape(SEND), lambda m: status_table(reviews, batches), rt, flags=re.S)
    writes.append((rp, rt))
    stale = [str(p.relative_to(ROOT)) for p, t in writes if not p.exists() or p.read_text(encoding="utf-8") != t]
    n = sum(len(r["interactions"]) for r in reviews.values())
    if check:
        problems += [f"stale (run scripts/grixis_interactions.py): {s}" for s in stale]
    else:
        for p, t in writes:
            if not p.exists() or p.read_text(encoding="utf-8") != t:
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(t, encoding="utf-8")
    print(f"grixis interactions: {len(reviews)}/{len(slugs)} decks reviewed, {n} rulings; "
          f"batches done {sum(1 for x in batches['batches'].values() if x['status'] == 'done')}/{len(batches['batches'])}; "
          f"{n_edges} edges; attestations {cov['cited']} folded + {cov['dispositioned']} dispositioned / {cov['items']} "
          f"({cov['files']} files); {len(problems)} problem(s)")
    for p in problems[:40]:
        print("  - " + p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
