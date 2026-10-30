#!/usr/bin/env python3
"""Build an in-universe RELATIVE chronology (partial order) for Packs A, B and C.

Rules (Batch 13, owner instruction for Phase 4 L244):
* An ordering is admitted only if an official Wizards page in the story cache
  states it in a verbatim quote: "before/after/later/long ago...", or a span
  ("X years ago") relative to that page's own story present, or a printed
  in-universe year label (e.g. the "63 AR" scene headers in The Brothers' War).
* No absolute years are invented. AR numbers appear only where a page prints them.
* Different pages' "story presents" are separate nodes; they are never merged
  unless a quote ties them together.
* Derived orderings come only from (a) transitivity, and (b) numeric comparison
  of two AR labels printed in official text (kind DERIVED_FROM_PRINTED_AR).
  Spans are never subtracted from each other to make new edges.

Usage: build_relative_chronology.py [--check]
  default  rebuilds data/lore_research/relative_chronology_2026-10-30.json (needs story cache)
  --check  verifies the committed artifact; uses the cache for quote checks if present
"""
import hashlib, json, re, sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/lore_research/relative_chronology_2026-10-30.json"
LR = ROOT / "data/lore_research"
FAMILIES = {
    "A": ["pack_a_ugin_bolas_evidence", "pack_a_elder_dragon_war_extension", "pack_a_tarkir_card_scenes", "pack_a5_ugin_allies"],
    "B": ["pack_b_thran_yawgmoth_brothers_war"],
    "C": ["pack_c_weatherlight_invasion_new_phyrexia", "pack_c2_return_to_dominaria", "pack_c3_assault_on_new_phyrexia", "pack_c4_march_of_the_machine"],
}

# ---- curated nodes: id -> (family, label, [claim ids]) ----
NODES = {
    # Pack A
    "A:eldrazi_imprisoned": ("A", "Ugin, Sorin and Nahiri imprison the Eldrazi on Zendikar", ["U001"]),
    "A:nahiri_slumber": ("A", "Nahiri's slumber while warden of Zendikar", []),
    "A:eldrazi_near_escape": ("A", "The Eldrazi nearly escape; neither Sorin nor Ugin comes", ["U005"]),
    "A:sarkhan_change": ("A", "Sarkhan's change to Tarkir's history (saves Ugin in the past)", ["A006", "A025", "A028"]),
    "A:tarkir_duel": ("A", "Bolas and Ugin's duel in Tarkir's past", ["A005", "A026"]),
    "A:ugin_cocoon": ("A", "Sarkhan leaves Ugin slumbering in a hedron cocoon", ["A028", "U008"]),
    "A:sorin_wakes_ugin": ("A", "Sorin wakes Ugin (as Ugin recounts)", ["U007"]),
    "A:sarkhan_returns_present": ("A", "Sarkhan is ripped back to his (altered) present", []),
    "A:ugin_awakes_tdm": ("A", "Ugin awakes from hibernation and departs Tarkir", []),
    "A:elder_dragon_war": ("A", "The Elder Dragon War(s)", ["A017", "A016"]),
    "A:primeval_rule": ("A", "The five Primeval Dragons (incl. Rith) rule Dominaria", ["A024"]),
    "A:dihada_binds_piru": ("A", "Geyadrone Dihada binds Piru and Chromium against Dakkon", ["A020", "A021"]),
    "A:bolas_returns_madara": ("A", "Bolas falls back into Dominaria at Madara (Perspectives narration)", ["A003"]),
    "C:primevals_fall": ("C", "The fall of the Primeval Dragons", []),
    # Pack B
    "B:kroog_siege": ("B", "Kroog under siege (Brothers' War)", []),
    "B:trench_war": ("B", "Mechanized trench war near Tomakul", []),
    "B:last_battle_sylex": ("B", "Last Battle on Argoth; Urza activates the Golgothian Sylex", ["B007", "B008", "B009"]),
    "B:silence_terisiare": ("B", "'And there was silence in Terisiare'", []),
    "B:penregon_69": ("B", "Penregon, five years after the war ended", []),
    "B:kroog_flooded": ("B", "Kroog flooded; Teferi's first spirit visit lands here", []),
    "B:ice_age": ("B", "The Ice Age", ["B011"]),
    "B:shard_twelve_worlds": ("B", "The Shard of Twelve Worlds", []),
    "B:flood_age": ("B", "The Flood Age", []),
    "B:thran_rule": ("B", "The Thran Empire rules Dominaria", ["B014"]),
    "B:urza_youth": ("B", "Urza as a young man, obsessed with Thran history", ["B014"]),
    "B:urza_yawgmoth_perish": ("B", "Urza and Yawgmoth perish together", ["B013", "B015"]),
    "B:urza_tower_constructs": ("B", "Urza engineers constructs in his tower against Mishra", []),
    "B:war_ended": ("B", "The Brothers' War concludes", []),
    # Pack C
    "C:karn_created": ("C", "Urza creates Karn", ["C004"]),
    "C:mirrodin_created": ("C", "Karn creates Mirrodin", ["C005"]),
    "C:oil_takes_hold": ("C", "Phyrexian oil takes hold on Mirrodin over the centuries", ["C006", "C007"]),
    "C:green_sun": ("C", "The Green Sun bursts from Mirrodin's core", []),
    "C:new_phyrexia": ("C", "Mirrodin becomes New Phyrexia", ["C007"]),
    "C:jaya_born": ("C", "Jaya Ballard is born on Dominaria", []),
    "C:serra_dies": ("C", "Serra dies, dispersing her essence into Sursi", []),
    "C:phyrexian_invasion_1": ("C", "The (first) Phyrexian Invasion of Dominaria", ["C011", "C014"]),
    "C:primevals_wake": ("C", "Rith and the Primevals awake during the previous Phyrexian invasion", []),
    "C:jodah_born": ("C", "Jodah is born", ["C019"]),
    "C:josu_undead": ("C", "Liliana makes her brother Josu undead", ["RTD007"]),
    "C:jaya_first_visit": ("C", "Jaya's first visit to the people who later worship her", []),
    "C:jaya_religion_found": ("C", "Jaya returns and finds a religion based on her", ["RTD029"]),
    "C:teferi_away": ("C", "Teferi's homeland is away (phased out) for hundreds of years", ["RTD024"]),
}
# story-present nodes: one per source page (never merged)
PRESENTS = {
    "P:stone_and_blood": "stone-and-blood-2016-06-15",
    "P:lithomancer": "the-lithomancer",
    "P:tarkir_summary_ktk": "story-tarkir-block-2015-04-29",
    "P:unbroken": "unbroken-and-unbowed-2015-04-22",
    "P:tarkir_dragons_guide": "tarkir-dragons-2015-02-25",
    "P:tdm_guide1": "planeswalkers-guide-to-tarkir-dragonstorm-part-1",
    "P:rtd_ep3": "return-dominaria-episode-3-2018-03-28",
    "P:dmu_legends": "legends-youll-find-dominaria-united-2022-09-01",
    "P:karn_profile": "karn-planeswalker",
    "P:pwg_dominaria_2022": "planeswalkers-guide-dominaria-2022-08-31",
    "P:rtd_ep2": "return-dominaria-episode-2-2018-03-22",
    "P:bro_ep5": "the-brothers-war-episode-5-as-cruel-as-necessary",
    "P:bro_ch1": "the-brothers-war-chapter-1-stronghold",
    "P:mom_ep10": "episode-10-the-rhythms-of-life",
}

# ---- curated stated orderings: (earlier, later, kind, page-key, quote, note) ----
# kind: STATED_BEFORE | SPAN_BEFORE_PRESENT(span) | PRINTED_AR(value)
EDGES = [
    ("A:eldrazi_imprisoned", "A:nahiri_slumber", "STATED_BEFORE", "stone-and-blood-2016-06-15",
     "It was Zendikar as she remembered it—after the Eldrazi, but before her slumber had allowed the world to drift out of control.", ""),
    ("A:eldrazi_imprisoned", "P:stone_and_blood", "SPAN_BEFORE_PRESENT:five thousand years ago", "stone-and-blood-2016-06-15",
     "forty years of mild effort, five thousand years ago, in exchange for millennia of peace of mind", "Sorin's point of view; conflicts with 'more than 6,000 years ago' (Lithomancer)."),
    ("A:eldrazi_near_escape", "P:stone_and_blood", "SPAN_BEFORE_PRESENT:over a thousand years ago", "stone-and-blood-2016-06-15",
     "But the Eldrazi nearly escaped over a thousand years ago, and neither Sorin nor Ugin came.", "Open lower bound only; not orderable against the imprisonment by span arithmetic."),
    ("A:eldrazi_imprisoned", "P:lithomancer", "SPAN_BEFORE_PRESENT:more than 6,000 years ago", "the-lithomancer",
     "Today, we look back in time, more than 6,000 years ago, to a plane whose name is lost to history.", "Editorial frame; 'today' is the 2014 publication present, not a dated in-universe scene."),
    ("A:eldrazi_imprisoned", "A:sarkhan_change", "STATED_BEFORE", "story-tarkir-block-2015-04-29",
     "it was a flashback that takes place long before Sarkhan's change to history", "The Lithomancer flashback (Eldrazi imprisonment) precedes Sarkhan's change."),
    ("A:tarkir_duel", "P:tarkir_summary_ktk", "SPAN_BEFORE_PRESENT:1,280 years", "story-tarkir-block-2015-04-29",
     "he has traveled into Tarkir's past—1,280 years, though Sarkhan doesn't know the exact span", "Span is from Sarkhan's Khans of Tarkir present."),
    ("A:tarkir_duel", "A:ugin_cocoon", "STATED_BEFORE", "unbroken-and-unbowed-2015-04-22",
     "is you and your hedron shard, after Bolas cast me down. Then I slumbered.", "Ugin speaking."),
    ("A:ugin_cocoon", "A:sorin_wakes_ugin", "STATED_BEFORE", "unbroken-and-unbowed-2015-04-22",
     "Then I slumbered. Time passed, but how much I could not say. I slept…and I healed. An ally of mine, a vampire and a Planeswalker, woke me up", "Ugin speaking; the ally is Sorin (U007)."),
    ("A:ugin_cocoon", "A:sarkhan_returns_present", "STATED_BEFORE", "tarkir-dragons-2015-02-25",
     "After he created a magical, protective hedron cocoon around the fallen Ugin, Sarkhan was ripped back through time to his present.", ""),
    ("A:tarkir_duel", "P:tarkir_dragons_guide", "SPAN_BEFORE_PRESENT:more than 1,200 years", "tarkir-dragons-2015-02-25",
     "left his time to travel back more than 1,200 years into Tarkir's past and save Ugin", "Compatible with, but less precise than, '1,280 years' (Tarkir story summary)."),
    ("A:ugin_cocoon", "P:unbroken", "SPAN_BEFORE_PRESENT:over a thousand years ago", "unbroken-and-unbowed-2015-04-22",
     "Ugin, the Spirit Dragon, whom he left slumbering in a hedron cocoon over a thousand years ago", ""),
    ("A:ugin_cocoon", "A:ugin_awakes_tdm", "STATED_BEFORE", "unbroken-and-unbowed-2015-04-22",
     "Ugin, the Spirit Dragon, whom he left slumbering in a hedron cocoon", "Awakening presupposes the slumber; paired with the TDM guide quote below."),
    ("A:ugin_awakes_tdm", "P:tdm_guide1", "SPAN_BEFORE_PRESENT:Five years ago", "planeswalkers-guide-to-tarkir-dragonstorm-part-1",
     "Five years ago, Ugin awoke from his hibernation and departed Tarkir.", ""),
    ("A:elder_dragon_war", "A:primeval_rule", "STATED_BEFORE", "legends-youll-find-dominaria-united-2022-09-01",
     "was one of the five ancient Primeval Dragons who ruled Dominaria sometime after the Elder Dragon War", ""),
    ("A:elder_dragon_war", "A:dihada_binds_piru", "STATED_BEFORE", "returning-legends-modern-horizons-2-2021-06-10",
     "Millennia later, Piru and Chromium were bound to the service of the planeswalker Geyadrone Dihada", "'Later' relative to the Elder Dragon War in the same biography."),
    ("A:elder_dragon_war", "A:bolas_returns_madara", "STATED_BEFORE", "chronicle-bolas-perspectives-2018-08-08",
     "at a time when the memory of the Elder Dragon Wars had faded into legend", "Bolas's own narration (Pack A A003 is CANON_DISPUTED for its roster, not for this ordering)."),
    ("A:primeval_rule", "C:primevals_fall", "STATED_BEFORE", "return-dominaria-episode-3-2018-03-28",
     "all the way back to the fall of the Primeval Dragons twenty thousand years ago", "A fall presupposes the rule; see span edge."),
    ("C:primevals_fall", "P:rtd_ep3", "SPAN_BEFORE_PRESENT:twenty thousand years ago", "return-dominaria-episode-3-2018-03-28",
     "all the way back to the fall of the Primeval Dragons twenty thousand years ago", "Stated within a description of Belzenlok's rewritten history."),
    ("C:phyrexian_invasion_1", "C:primevals_wake", "STATED_DURING", "legends-youll-find-dominaria-united-2022-09-01",
     "She and her kin awoke during the previous Phyrexian invasion", "'During' is a containment, not a strict ordering; excluded from the partial order."),
    ("C:primevals_fall", "C:primevals_wake", "STATED_BEFORE", "legends-youll-find-dominaria-united-2022-09-01",
     "She and her kin awoke during the previous Phyrexian invasion, but with Darigaaz's death, they were sealed away once more.", "'Sealed away once more' states a prior sealing (the fall)."),
    # Pack B — printed AR scene headers (bro_ep5 / bro_ep1 / bro_ep4)
    ("B:kroog_siege", "AR:28", "PRINTED_AR:28", "the-brothers-war-episode-5-as-cruel-as-necessary",
     "He was back in Kroog. He recognized it immediately from the towers: during his first visit they were crumbled ruins. Now, they stood proud above a city under siege.", "Scene under the '28 AR' header."),
    ("B:trench_war", "AR:44", "PRINTED_AR:44", "the-brothers-war-episode-5-as-cruel-as-necessary",
     "This was the same war as the one he saw days prior, now decades later.", "Scene under the '44 AR' header."),
    ("B:last_battle_sylex", "AR:63", "PRINTED_AR:63", "the-brothers-war-episode-5-as-cruel-as-necessary",
     "Urza sat cross-legged with the bowl in his lap.", "Scene under the '63 AR' header."),
    ("B:silence_terisiare", "AR:64", "PRINTED_AR:64", "the-brothers-war-episode-5-as-cruel-as-necessary",
     "And there was silence in Terisiare.", "Line under the '64 AR' header."),
    ("B:penregon_69", "AR:69", "PRINTED_AR:69", "the-brothers-war-episode-1-the-end",
     "It was snowing in Penregon. Five years after the war that ended the world concluded", "Scene under the '69 AR' header."),
    ("B:kroog_flooded", "AR:85", "PRINTED_AR:85", "the-brothers-war-episode-5-as-cruel-as-necessary",
     "Teferi arrived in a dark room in a flooded city that he would later learn to be Kroog.", "Scene under the '85 AR' header."),
    ("P:bro_ep5", "AR:4562", "PRINTED_AR:4562", "the-brothers-war-episode-5-as-cruel-as-necessary",
     "Teferi lay shirtless in a cold metal coffin, counting his breath.", "Teferi's present, under the '4562 AR' header."),
    ("B:war_ended", "B:penregon_69", "STATED_BEFORE", "the-brothers-war-episode-1-the-end",
     "Five years after the war that ended the world concluded, the survivors found that nothing truly ended", ""),
    ("B:last_battle_sylex", "B:shard_twelve_worlds", "STATED_BEFORE", "the-brothers-war-episode-5-as-cruel-as-necessary",
     "the Shard of Twelve Worlds, the Ice Age, every important event over the last four millennia—everything came after this moment", ""),
    ("B:last_battle_sylex", "B:ice_age", "STATED_BEFORE", "the-brothers-war-episode-5-as-cruel-as-necessary",
     "the Shard of Twelve Worlds, the Ice Age, every important event over the last four millennia—everything came after this moment", ""),
    ("B:last_battle_sylex", "P:bro_ep5", "SPAN_BEFORE_PRESENT:the last four millennia", "the-brothers-war-episode-5-as-cruel-as-necessary",
     "every important event over the last four millennia—everything came after this moment", "Consistent with the printed 63 AR / 4562 AR labels."),
    ("B:last_battle_sylex", "B:ice_age", "STATED_BEFORE", "planeswalkers-guide-dominaria-2022-08-31",
     "Urza's Sylex blast at the end of the Brothers' War shattered it, carved up by glaciers during the Ice Age, and ﬁnally inundated during the Flood Age", "Terisiare sequence."),
    ("B:ice_age", "B:flood_age", "STATED_BEFORE", "planeswalkers-guide-dominaria-2022-08-31",
     "carved up by glaciers during the Ice Age, and ﬁnally inundated during the Flood Age", ""),
    ("B:thran_rule", "B:urza_youth", "STATED_BEFORE", "urza-planeswalker",
     "As a young man, Urza was obsessed with the history of Dominaria and the Thran Empire that once ruled the plane.", "'History'/'once ruled' places the Thran before Urza's youth."),
    ("B:urza_youth", "B:urza_yawgmoth_perish", "STATED_BEFORE", "urza-planeswalker",
     "This led to a millennia-long vendetta against Yawgmoth and the plane of Phyrexia. After countless years of conflict, both subtle and overt, Urza and Yawgmoth perished together.", ""),
    ("B:urza_tower_constructs", "P:bro_ch1", "SPAN_BEFORE_PRESENT:millennia before", "the-brothers-war-chapter-1-stronghold",
     "the tower where, millennia before, Urza engineered mechanical constructs to fight a bitter struggle against his brother, Mishra", ""),
    # Pack C
    ("C:karn_created", "P:karn_profile", "SPAN_BEFORE_PRESENT:over 1200 years ago", "karn-planeswalker",
     "Created over 1200 years ago by the Planeswalker Urza", "Profile present (undated)."),
    ("C:karn_created", "C:mirrodin_created", "STATED_BEFORE", "mirrodin-plane",
     "Long ago, this metal plane was created by Karn, the silver golem built by the Planeswalker Urza.", "Karn existed (built by Urza) before creating Mirrodin."),
    ("C:mirrodin_created", "C:oil_takes_hold", "STATED_BEFORE", "mirrodin-plane",
     "He unwittingly introduced a dark contagion: Phyrexian oil. Over the centuries, this oil has taken hold", ""),
    ("C:green_sun", "C:new_phyrexia", "STATED_BEFORE", "returning-legends-modern-horizons-2-2021-06-10",
     "when the Green Sun, a gigantic ball of mana, burst forth from Mirrodin's core. Years later, Mirrodin succumbed to an infectious agent and became New Phyrexia.", ""),
    ("C:jaya_born", "P:dmu_legends", "SPAN_BEFORE_PRESENT:more than 1,500 years ago", "legends-youll-find-dominaria-united-2022-09-01",
     "Born on Dominaria more than 1,500 years ago", ""),
    ("C:jodah_born", "P:dmu_legends", "SPAN_BEFORE_PRESENT:over 4,000 years", "legends-youll-find-dominaria-united-2022-09-01",
     "At over 4,000 years of age, Jodah is an archmage blessed with prodigious talent and eternal youth.", "Age, i.e. born over 4,000 years before the DMU present."),
    ("C:serra_dies", "P:pwg_dominaria_2022", "SPAN_BEFORE_PRESENT:almost eight hundred years ago", "planeswalkers-guide-dominaria-2022-08-31",
     "Serra died almost eight hundred years ago when she dispersed her essence into the land of Sursi.", ""),
    ("C:phyrexian_invasion_1", "P:pwg_dominaria_2022", "SPAN_BEFORE_PRESENT:centuries ago", "planeswalkers-guide-dominaria-2022-08-31",
     "They first appeared during the Phyrexian Invasion centuries ago", ""),
    ("C:josu_undead", "P:rtd_ep2", "SPAN_BEFORE_PRESENT:many years ago", "return-dominaria-episode-2-2018-03-22",
     "I made Josu undead, many years ago.", "Liliana speaking."),
    ("C:jaya_first_visit", "C:jaya_religion_found", "STATED_BEFORE", "return-dominaria-episode-9-2018-05-09",
     "Two hundred years later, I went back and found they'd started a religion based on me.", "Jaya speaking; interval two hundred years."),
    ("C:teferi_away", "P:mom_ep10", "SPAN_BEFORE_PRESENT:hundreds of years", "episode-10-the-rhythms-of-life",
     "why Teferi spent hundreds of years trying to restore his home", ""),
]


def norm(s: str) -> str:
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def load_pages():
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_card_lore_links as b
    return b.load_pages()


def find_page(pages, key):
    hits = [p for p in pages.values() if p["url"].rstrip("/").endswith(key)]
    if len(hits) != 1:
        raise SystemExit(f"page key {key!r} matched {len(hits)} cached pages")
    return hits[0]


def pack_claims():
    out = {}
    for fam, packs in FAMILIES.items():
        for p in packs:
            for c in json.loads((LR / f"{p}_2026-10-30.json").read_text())["claims"]:
                out[c["id"]] = (fam, p, c["grade"])
    return out


def closure(nodes, edges):
    succ = {n: set() for n in nodes}
    for e in edges:
        succ[e["earlier"]].add(e["later"])
    reach = {}
    for n in nodes:
        seen, stack = set(), list(succ[n])
        while stack:
            m = stack.pop()
            if m not in seen:
                seen.add(m); stack.extend(succ[m])
        reach[n] = seen
    return reach


def build(pages):
    claims = pack_claims()
    nodes = {}
    for nid, (fam, label, cids) in NODES.items():
        for c in cids:
            if c not in claims:
                raise SystemExit(f"{nid}: unknown claim {c}")
        nodes[nid] = {"id": nid, "kind": "EVENT", "family": fam, "label": label,
                      "claims": [{"id": c, "pack": claims[c][1], "grade": claims[c][2]} for c in cids]}
    for pid, key in PRESENTS.items():
        pg = find_page(pages, key)
        nodes[pid] = {"id": pid, "kind": "STORY_PRESENT", "family": None,
                      "label": f"Story present of {key}", "url": pg["url"]}
    edges = []
    for (a, b, kind, key, quote, note) in EDGES:
        pg = find_page(pages, key)
        if norm(quote) not in norm(pg["text"]):
            raise SystemExit(f"quote not verbatim on {key}: {quote[:60]}")
        if kind.startswith("PRINTED_AR:"):
            v = kind.split(":", 1)[1]
            if not re.search(rf"(?m)^\s*{v} AR\s*$", pg["text"]):
                raise SystemExit(f"{v} AR header not printed on {key}")
            nodes.setdefault(b, {"id": b, "kind": "PRINTED_AR_LABEL", "family": "B",
                                 "label": f"{v} AR (printed scene header)", "ar": int(v)})
        for n in (a, b):
            if n not in nodes:
                raise SystemExit(f"unknown node {n}")
        rel = "SAME_TIME_AS_LABEL" if kind.startswith("PRINTED_AR") else ("DURING" if kind == "STATED_DURING" else "BEFORE")
        edges.append({"earlier": a, "later": b, "relation": rel, "kind": kind.split(":")[0],
                      "value": kind.split(":", 1)[1] if ":" in kind else None,
                      "source_url": pg["url"], "quote": quote,
                      "quote_sha256": hashlib.sha256(norm(quote).encode()).hexdigest(), "note": note})
    return assemble(nodes, edges)


def assemble(nodes, edges):
    # derived: numeric comparison of printed AR labels only
    ars = sorted((n["ar"], n["id"]) for n in nodes.values() if n["kind"] == "PRINTED_AR_LABEL")
    derived = [{"earlier": x[1], "later": y[1], "relation": "BEFORE", "kind": "DERIVED_FROM_PRINTED_AR",
                "value": f"{y[0]-x[0]} years", "source_url": None, "quote": None, "quote_sha256": None,
                "note": "Arithmetic on two AR labels printed in official text."}
               for x, y in zip(ars, ars[1:])]
    # an event labelled with an AR is collapsed to the label for ordering purposes
    alias = {e["earlier"]: e["later"] for e in edges if e["relation"] == "SAME_TIME_AS_LABEL"}
    order_edges = [dict(e, earlier=alias.get(e["earlier"], e["earlier"]), later=alias.get(e["later"], e["later"]))
                   for e in edges + derived if e["relation"] == "BEFORE"]
    reach = closure(nodes, order_edges)
    canon = lambda n: alias.get(n, n)
    cycles = sorted(n for n in nodes if canon(n) in reach[canon(n)])
    ids = sorted(nodes)
    pairs = [(a, b) for a, b in combinations(ids, 2) if canon(a) != canon(b)]
    comparable = sum(1 for a, b in pairs if canon(b) in reach[canon(a)] or canon(a) in reach[canon(b)])
    # weakly connected components
    parent = {n: n for n in ids}
    def f(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for e in edges + derived:
        parent[f(e["earlier"])] = f(e["later"])
    comps = {}
    for n in ids:
        comps.setdefault(f(n), []).append(n)
    components = sorted((sorted(v) for v in comps.values()), key=lambda v: (-len(v), v[0]))
    precedes = {n: sorted(m for m in ids if canon(m) in reach[canon(n)]) for n in ids}
    fam_stats = {}
    for fam in FAMILIES:
        ev = [n for n in ids if nodes[n].get("family") == fam and nodes[n]["kind"] == "EVENT"]
        fe = [e for e in edges if nodes[e["earlier"]].get("family") == fam or nodes[e["later"]].get("family") == fam]
        fam_stats[fam] = {"event_nodes": len(ev), "stated_edges": len(fe),
                          "claims_placed": sorted({c["id"] for n in ev for c in nodes[n]["claims"]}),
                          "claims_total": len(pack_claims_by_family(fam))}
    return {
        "schema": "relative-chronology/v1", "status": "PRELIMINARY_RESEARCH", "as_of": "2026-10-30",
        "basis": "Only orderings stated verbatim on cached official Wizards pages; printed AR scene headers; transitivity. No invented years; story presents are never merged.",
        "counts": {"nodes": len(nodes), "event_nodes": sum(n["kind"] == "EVENT" for n in nodes.values()),
                   "story_present_nodes": sum(n["kind"] == "STORY_PRESENT" for n in nodes.values()),
                   "printed_ar_labels": len(ars), "stated_edges": len(edges), "derived_edges": len(derived),
                   "comparable_pairs": comparable, "total_pairs": len(pairs), "components": len(components),
                   "cycles": len(cycles)},
        "families": fam_stats, "nodes": [nodes[n] for n in ids], "stated_edges": edges, "derived_edges": derived,
        "components": components, "precedes": precedes, "cycles": cycles,
        "l244_closure": {"closes_l244": False, "missing": MISSING},
    }


def pack_claims_by_family(fam):
    return [c for c, v in pack_claims().items() if v[0] == fam]


MISSING = [
    "Story presents are unanchored to each other: no official quote states how the KTK, EMN, DOM, DMU, BRO, ONE or MOM 'present' relate, so spans measured from different pages cannot be compared (e.g. Jaya 'more than 1,500 years ago' vs Karn 'over 1200 years ago').",
    "Pack A's primordial and early-lives claims (A001, A002, A004, A013) and the Meditation Realm/War of the Spark/Dragonstorm sequence (A007-A012, U010-U016) have no ordering quote in the cached pages beyond publication order.",
    "Many spans are open-ended ('over a thousand', 'centuries', 'many years', 'hundreds of years'), so they cannot order events even against the same present; e.g. the Eldrazi near-escape vs the imprisonment is not orderable from spans alone.",
    "Conflicting spans for the Eldrazi imprisonment: 'five thousand years ago' (Stone and Blood, Sorin's view) vs 'more than 6,000 years ago' (The Lithomancer) vs 'Six thousand years ago'/'over 6,000 years ago' elsewhere; both are recorded, none chosen.",
    "Pack B: The Thran, Yawgmoth's origin and the Mishra corruption sequence lack stated orderings beyond 'once ruled' and 'millennia-long vendetta'; the three B-pack card-story/product pages are not in the cache.",
    "Pack C: C2/C3/C4 episodes print no AR dates; the Weatherlight Saga (novels) is not ingested, so Invasion → Yawgmoth's end → Old Phyrexia destroyed has no ordering quote; the cross-reference 'Karn built by Urza' links C to B only by identity, not by a dated edge.",
    "Seven Pack A/B source pages (reforged_chain, nexus_design, journey_nexus, war_games, m19/dmu notes, bro_card_stories_1/2, bro_product_page) are not in the story cache, so their orderings were not checked.",
]


def main():
    check = "--check" in sys.argv
    if check:
        doc = json.loads(OUT.read_text())
        try:
            pages = load_pages()
        except SystemExit:
            pages = None
        if pages is not None:
            fresh = build(pages)
            if fresh != doc:
                raise SystemExit("relative chronology is stale; rebuild")
        else:
            for e in doc["stated_edges"]:
                assert hashlib.sha256(norm(e["quote"]).encode()).hexdigest() == e["quote_sha256"]
        assert doc["counts"]["cycles"] == 0
        print("relative chronology OK", doc["counts"])
        return
    doc = build(load_pages())
    OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(doc["counts"]), json.dumps({k: (v["event_nodes"], v["stated_edges"], len(v["claims_placed"]), v["claims_total"]) for k, v in doc["families"].items()}))


if __name__ == "__main__":
    main()
