"""Build "EDH Archetypes.md" (Bot cycle 4): one guide per archetype, assembled from repo data only —
validated deck skeletons, Oracle text (Scryfall bulk), EDH Staples role lists, rulings-backed synergy notes,
Rules Interactions topics, and Commander Spellbook combos (data/combos.json). Strategy text is labeled Opinion."""
import atomic_io  # noqa: F401  atomic Path.write_text/write_bytes (Bot cycle 34)
import csv, gzip, json, re, sys, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts")); import ingest_scryfall as ing
idx = {r["name"]: r for r in csv.DictReader(open(ROOT / "data/card_index.csv"))}
bulk = sorted((ROOT / ".cache").glob("oracle-cards-*.jsonl.gz"))[-1]
orc = {}
for l in gzip.open(bulk, "rt"):
    c = json.loads(l)
    if c["name"] in idx:
        orc[c["name"]] = (c.get("oracle_text") or " // ".join(f.get("oracle_text", "") for f in c.get("card_faces", [])))
combos = json.load(open(ROOT / "data/combos.json"))["decks"]
def slug(h): h = h.lower(); h = re.sub(r"[^\w\- ]", "", h); return h.replace(" ", "-")
def L(n): return ing.link(idx[n], "") if n in idx else n
def deck(stem):
    p = ROOT / "decks" / f"{stem}.md"; t = p.read_text()
    cmd = [m.group(1) for m in re.finditer(r"^1x (.+?) \[Commander", t, re.M)]
    cards = [m.group(1) for m in re.finditer(r"^1x (.+?) \[", t, re.M)]
    return cmd, cards
def staples(section):
    t = (ROOT / "EDH Staples.md").read_text(); i = t.index(f"### {section}\n"); j = t.find("\n### ", i + 5)
    return re.findall(r"\| \d+ \| \[([^\]]+)\]", t[i:j if j > 0 else None])
SYN = {m.group(1): slug(m.group(1)) for m in re.finditer(r"^### (.+)$", (ROOT / "EDH Standards.md").read_text(), re.M)}
def syn(word): return [f"[{h.split(' — ')[1].split(' (')[0]}](EDH%20Standards.md#{a})" for h, a in SYN.items() if " — " in h and word in h]
A = [
 ("Aristocrats (sacrifice & death triggers)", ["teysa-karlov","korvold-fae-cursed-king","edgar-markov"], "Sacrifice / aristocrats", r"sacrifice (a|another) creature|whenever (a|another) creature (you control )?dies|whenever you sacrifice", ["ETB / LTB & look-back triggers","Replacement effects vs. triggered abilities","State-based actions"], ["Teysa","Korvold"],
  "Make fodder, sacrifice it for value, and drain with death triggers."),
 ("Tokens / go-wide", ["krenko-mob-boss","edgar-markov","trostani-selesnyas-voice","giada-font-of-hope"], "Tokens / go-wide", r"create[^.]*token|tokens? you control", ["Copy effects","Replacement effects vs. triggered abilities"], ["Krenko","Teysa"],
  "Flood the board with creature tokens, then use anthems, mass pump or drain effects to finish."),
 ("Spellslinger (instants & sorceries)", ["talrand-sky-summoner","niv-mizzet-parun","feather-the-redeemed","kykar-winds-fury"], "Spellslinger (instants & sorceries matter)", r"instant or sorcery|noncreature spell|magecraft|copy target (instant|sorcery)", ["Stack & priority","Casting vs. copying a spell"], ["Talrand","Niv-Mizzet"],
  "Chain cheap instants and sorceries; payoffs turn each spell into bodies, cards or damage."),
 ("Lands matter / landfall", ["tatyova-benthic-druid","kynaios-and-tiro-of-meletis","selvala-heart-of-the-wilds"], "Landfall / lands matter", r"landfall|whenever a land (you control )?enters|play an additional land|lands? from your graveyard", ["ETB / LTB & look-back triggers","Replacement effects vs. triggered abilities"], ["Tatyova","Kynaios"],
  "Play extra lands every turn and convert each land drop into cards or bodies."),
 ("+1/+1 counters", ["atraxa-praetors-voice","giada-font-of-hope"], "+1/+1 counters", r"\+1/\+1 counter|proliferate", ["Layers & timestamps","Worked layer examples (official CR examples)","Replacement effects vs. triggered abilities"], [],
  "Spread and multiply counters (proliferate, doublers); counters apply in layer 7c."),
 ("Graveyard value / reanimator", ["muldrotha-the-gravetide","karador-ghost-chieftain","the-ur-dragon"], "Graveyard recursion", r"from your graveyard|mill|return target [^.]*card from your graveyard", ["Commander: returning to the command zone","ETB / LTB & look-back triggers"], ["Muldrotha","Karador"],
  "Fill the graveyard on purpose and replay permanents from it."),
 ("Blink / flicker", ["brago-king-eternal","chulane-teller-of-tales"], "Protection", r"exile [^.]*then return|return (it|them|those cards) to the battlefield|blink|flicker", ["ETB / LTB & look-back triggers","Commander: returning to the command zone"], ["Brago"],
  "Exile and return your own permanents to reuse enters-the-battlefield abilities."),
 ("Artifacts", ["breya-etherium-shaper","kozilek-the-great-distortion"], "Ramp (mana rocks & land ramp)", r"artifact (spell|creature|token)|whenever (an|another) artifact|sacrifice an artifact", ["Copy effects","State-based actions"], ["Breya"],
  "Generate artifacts and tokens; sacrifice outlets turn them into damage, mana or cards."),
 ("Combat / voltron & extra combats", ["saskia-the-unyielding","xenagos-god-of-revels","gishath-suns-avatar","yuriko-the-tigers-shadow"], "Protection", r"double strike|additional combat|extra combat|trample|deals combat damage to a player|ninjutsu|equipped creature", ["Combat damage assignment","Deathtouch + trample","Protection","Hexproof, shroud & ward","Commander tax"], ["Saskia","Yuriko"],
  "Win through combat damage: evasive or pumped attackers, extra combat steps, protection for the key creature."),
 ("Cascade & big spells", ["yidris-maelstrom-wielder","animar-soul-of-elements"], "Ramp (mana rocks & land ramp)", r"cascade|without paying its mana cost|costs? \{\d\} less", ["Casting vs. copying a spell","Stack & priority"], ["Yidris"],
  "Cheat or discount spells so each turn deploys more than its mana allows."),
 ("Group hug & group slug", ["kynaios-and-tiro-of-meletis","nekusar-the-mindrazer"], "Card draw & advantage", r"each player (draws|may)|each opponent|whenever an opponent draws", ["Stack & priority"], ["Kynaios"],
  "Give everyone resources (hug) or punish everyone for using them (slug, e.g. damage on draw)."),
 ("Life as a resource / lifedrain", ["krrik-son-of-yawgmoth","edgar-markov"], "Sacrifice / aristocrats", r"lose[s]? \d+ life|gain[s]? (\d+|that much) life|pay \d+ life|lifelink", ["State-based actions","Replacement effects vs. triggered abilities"], ["K'rrik"],
  "Use life totals as a resource — pay life for spells, drain opponents, and gain it back."),
]
o = ["# EDH Archetypes", "",
     "> **Bot cycle 4.** One guide per archetype, built only from data already in this repo: validated [deck skeletons](decks/), Oracle text (Scryfall bulk 2026-10-15), [EDH Staples](EDH%20Staples.md) role lists, rulings-backed [synergy notes](EDH%20Standards.md#synergy-notes), [Rules Interactions](Rules%20Interactions.md) (CR 2026-09-25), and [Commander Spellbook](https://commanderspellbook.com) combos (`data/combos.json`). The **Plan** line and the assignment of commanders to archetypes are **Opinion**; everything else is data. Generated by `scripts/build_archetypes.py`.", "",
     "## Contents"]
for a in A: o.append(f"- [{a[0]}](#{slug(a[0])})")
o.append("")
for name, decks, stap, pat, rules, synw, plan in A:
    o.append(f"## {name}\n")
    o.append(f"**Plan (Opinion):** {plan}\n")
    dl = []
    for d in decks:
        cmd, cards = deck(d); c = combos.get(d, {})
        dl.append(f"[{' & '.join(cmd)}](decks/{d}.md) ({len(c.get('combos', []))} Spellbook combos, {c.get('two_card_infinite', 0)} two-card infinite)")
    o.append("**Example skeletons (validated, 100 cards):** " + " · ".join(dl) + "\n")
    st = staples(stap); seen = collections.Counter()
    for d in decks:
        _, cards = deck(d)
        for n in cards:
            if n in orc and re.search(pat, orc[n], re.I): seen[n] += 1
    shared = [n for n, k in seen.most_common() if k >= 2][:12]
    top = [n for n, _ in seen.most_common(12)] if not shared else shared
    o.append(f"**Archetype cards in these skeletons** (Oracle text matches `{pat}`; {'in ≥2 of the example decks' if shared else 'most common'}): " + ", ".join(L(n) for n in top) + "\n")
    o.append(f"**Staples list:** [EDH Staples → {stap}](EDH%20Staples.md#{slug(stap)}) — top picks there: " + ", ".join(L(n) for n in st[:6]) + "\n")
    s = [x for w in synw for x in syn(w)]
    if s: o.append("**Rulings-backed synergy notes:** " + " · ".join(s) + "\n")
    o.append("**Rules to know:** " + " · ".join(f"[{r}](Rules%20Interactions.md#{slug(r)})" for r in rules) + "\n")
    tc = [(d, r) for d in decks for r in combos.get(d, {}).get("combos", []) if r["n"] == 2 and r["infinite"]]
    if tc:
        o.append("**Two-card infinite combos present in these skeletons** (Commander Spellbook; ⚠️ Bracket 3+ — see [Power bracket assessment](EDH%20Standards.md#power-bracket-assessment)):\n")
        for d, r in tc[:6]:
            o.append(f"- {' + '.join(L(n) for n in r['cards'])} — {', '.join(r['produces'][:2])} ([{r['id']}](https://commanderspellbook.com/combo/{r['id']}/))")
        if len(tc) > 6: o.append(f"- … {len(tc)-6} more in the deck files.")
        o.append("")
(ROOT / "EDH Archetypes.md").write_text("\n".join(o) + "\n")
print("archetypes", len(A))
