#!/usr/bin/env python3
"""Bot cycle 22 (#73): index of primary story sources ingested for Phase 6 lore deepening.

Reads fetched page text from .cache/story/text22/ (gitignored; full text is never committed) and
writes data/primary_sources.csv (date, title, kind, arc, words, url) and "Lore Primary Sources.md".
If the cache is missing, the page is rebuilt from the committed CSV.

Usage: python3 scripts/build_primary_sources.py [--check]
"""
import atomic_io  # noqa: F401  atomic Path.write_text/write_bytes (Bot cycle 34)
import csv, re, sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent
C = R / '.cache/story/text22'
CSV = R / 'data/primary_sources.csv'
OUT = R / 'Lore Primary Sources.md'

# arc code -> (Conflicts & Arcs anchor title, slug patterns)
ARCS = [
 ('KHM', 'Kaldheim (2021)', r'kaldheim|travelers-2021|awaken-trolls|saga-tibalt|demons-realm|battle-kaldheim'),
 ('STX', 'Strixhaven (2021)', r'strixhaven-2021|class-session|lessons-2021|extracurriculars|put-test|final-exam'),
 ('MID/VOW', 'Innistrad: Midnight Hunt & Crimson Vow (2021)', r'midnight-hunt|witch-woods|motives-wolf|betzold|harvesttide|night-closes|tithes|dolorous|forever-hold|wedding-crashers|till-death'),
 ('NEO', 'Kamigawa: Neon Dynasty (2022)', r'neon-dynasty|eiganjo|neon-flames|unexpected-alliance|episode-4-break|threads-war'),
 ('SNC', 'Streets of New Capenna (2022)', r'new-capenna|homecoming-2022-03|dirty-laundry|tests-2022|font-2022|hymn-angels'),
 ('DMU', 'Dominaria United (2022)', r'dominaria-2022|echoes-dark|sand-hourglass|locked-tower|brutal-blow|whisper-wind'),
 ('ONE', 'Phyrexia: All Will Be One (2023)', r'assault-on-new-phyrexia|all-will-be-one'),
 ('MOM', 'March of the Machine (2023)', r'march-of-the-machine|fleshless|holding-your-breath|mother-son|eyes-unblinking|cathartic|last-to-leave|divine-intervention|wrenn-and-eight|old-sins|rhythms-of-life'),
 ('WOE', 'Wilds of Eldraine (2023)', r'pure-of-heart|wandering-knight|two-great-banquets|frozen-heart|broken-oaths'),
 ('MKM', 'Murders at Karlov Manor (2024)', r'karlov|ghosts-of-our-past|monsters-we-became|shadows-of-regret|justice-before-mercy|chains-of-expectation|explosions-of-genius|rot-before|gods-of-chaos|beauty-in-destruction|roots-of-decay'),
 ('OTJ', 'Outlaws of Thunder Junction (2024)', r'offer-of-revenge|the-jailbreak|train-to-prosperity|finding-tarnation|high-moon|thieves-and-thunderslingers|epilogue-[12]'),
 ('BLB', 'Bloomburrow (2024)', r'bloomburrow|calamity-comes|expected-party|lost-and-the-found|soothsaying|fountainport'),
 ('DSK', 'Duskmourn: House of Horror (2024)', r'duskmourn|dont-go-past|dont-split|dont-look-back|dont-give-up|dont-give-in|dont-die'),
 ('DFT', 'Aetherdrift (2025)', r'aetherdrift'),
 ('TDM', 'Tarkir: Dragonstorm (2025)', r'tarkir-dragonstorm'),
 ('EOE', 'Edge of Eternities (2025)', r'edge-of-eternities'),
 ('ECL', 'Lorwyn Eclipsed (2025–26)', r'lorwyn-eclipsed'),
 ('SOS', 'Secrets of Strixhaven (2026)', r'secrets-of-strixhaven'),
 ('RF', "Jace's Echoverse (Reality Fracture)", r'reality-fracture'),
 # Bot cycle 24: pre-2019 arcs upgraded from fetched web fiction / guides
 ('THS', "Theros: Xenagos's ascension & Elspeth's fall", r'planeswalkers-guide-theros-part|planeswalkers-guide-born-gods|planeswalkers-guide-journey-nyx|^theros-plane$'),
 ('KLD/AER', 'Kaladesh revolt', r'torch-defiance|renegade-prime|born-aether|bottled-2016|release-2016|very-arena|grateful-consulate|quiet-moments|breakthrough-2016|revolution-begins|skies-over-ghirapur|breaking-points|puppets-2017|renewal-2017|planeswalkers-guide-kaladesh|homesick-2016|time-innovation'),
 ('AKH/HOU', 'Amonkhet & the God-Pharaoh', r'^trust-2017|writing-wall|servants-2017|hand-moves|brazen-2017|trespass-2017|judgment-2017|^hour-(revelation|glory|promise|eternity|devastation)|^amonkhet-plane$|feast-2017|favor-2017|endure-2017'),
 ('XLN/RIX', 'Ixalan & the Immortal Sun', r'jace-alone|question-confidence|talented-captain|shapers-2017|something-else-entirely|race-part|flood-2018|glimpse-far-side|arbiter-law|sabotage-2018|who-tells-stories|wool-over-eyes|planeswalkers-guide-ixalan-part|^ixalan-plane$|rivals-ixalan'),
 # Bot cycle 25: last six arcs to full format + 2015–19 episode upgrades
 ('ELD', 'Throne of Eldraine (2019)', r'planeswalkers-guide-eldraine'),
 ('THB', 'Theros Beyond Death (2020)', r'theros-beyond-death|journeys-end-2014'),
 ('IKO', 'Ikoria: Lair of Behemoths (2020)', r'ikoria'),
 ('BRO', "The Brothers' War frame story (2022)", r'the-brothers-war-(chapter|episode)'),
 ('MAT', 'March of the Machine: The Aftermath (2023)', r'she-who-breaks-the-world|beyond-repair'),
 ('LCI', 'The Lost Caverns of Ixalan (2023)', r'lost-caverns-of-ixalan|rivals-ixalan-magic-story-alternate'),
 ('BFZ/OGW', 'Eldrazi Awaken / Battle for Zendikar / Gatewatch', r'battle-zendikar-story|oath-gatewatch|zendikars-last-stand|zendikar-resurgent|brink-extinction|rise-kozilek|hedron-alignment|promises-keep|retaliation-ob-nixilis|blight-we-were-born|flames-2016|beneath-surface|revelation-eye|shaping-army|liberation-sea-gate|any-cost-2015|family-values-2015|battle-of-fort-keff|believers-pilgrimage'),
 ('SOI/EMN', 'Innistrad & Emrakul', r'under-silver-moon|gaze-blank|unwelcome-2016|sacrifice-2016|mystery-markov|drownyard|promises-old-and-new|lilianas-indignation|games-2016|lunarch-inquisition|stories-and-endings|i-am-avacyn|prodigal-sorcerers|archmage-goldnight|stone-and-blood|innistrads-last-hope|campaign-vengeance|saint-traft|battle-thraben|promised-end|emrakul-rises'),
 ('DOM/WAR', 'Return to Dominaria & War of the Spark', r'return-dominaria-episode|war-spark-ravnica'),
]
DEEPENED = {'KHM','STX','MID/VOW','NEO','SNC','DMU','ONE','MOM','WOE','MKM','OTJ','BLB','DSK','DFT','TDM','EOE','ECL','SOS','RF','THS','KLD/AER','AKH/HOU','XLN/RIX','ELD','THB','IKO','BRO','MAT','LCI','BFZ/OGW','SOI/EMN','DOM/WAR'}  # +9 in Bot cycle 24, +10 in Bot cycle 25

def anchor(t):
    a = re.sub(r'[^\w\- ]', '', t.lower()).replace(' ', '-')
    return a

def arc_of(slug):
    for code, _, pat in ARCS:
        if re.search(pat, slug): return code
    return ''

def scan():
    rows = []
    for f in sorted(C.glob('*.txt')):
        head = f.read_text(errors='ignore').split('\n', 4)
        url = head[0].replace('URL: ', '').strip()
        title = re.sub(r'\s*\|\s*(MAGIC: THE GATHERING|Magic: The Gathering)\s*$', '', head[1].replace('TITLE: ', '').strip())
        date = head[2].replace('DATE: ', '').strip()
        words = len(head[-1].split())
        kind = 'planeswalkers-guide' if 'planeswalkers-guide' in url else ('feature' if '/feature/' in url else 'story')
        rows.append(dict(date=date, title=title, kind=kind, arc=arc_of(f.stem), words=words, url=url))
    rows.sort(key=lambda r: (r['date'], r['url']))
    return rows

def page(rows):
    by = {}
    for r in rows: by.setdefault(r['arc'], []).append(r)
    guides = [r for r in rows if r['kind'] == 'planeswalkers-guide']
    total_words = sum(int(r['words']) for r in rows)
    L = ['---', 'title: "Lore Primary Sources"', 'category: lore', 'tags: [sources, primary, planeswalkers-guide, story-episodes]',
         'issues: [73]', 'generated_by: scripts/build_primary_sources.py', 'sources: [wizards-story]',
         'related: ["Conflicts & Arcs.md", "Side-Media Index.md", "Contradictions & Retcons Log.md"]', 'schema: 2', '---', '',
         '# Lore Primary Sources', '',
         f'> **Generated (Bot cycle 22, [#73](https://github.com/corymstover/GrokBotMTGCompanion/issues/73)).** Official Wizards pages fetched for the Phase 6 primary-source pass: **{len(rows)} pages** ({total_words:,} words), incl. **{len(guides)} Planeswalker\'s Guides**. Page text is cached locally (`.cache/story/text22/`, gitignored) and is never committed; this page lists titles, dates and URLs only. Quotes added to [Conflicts & Arcs](Conflicts%20%26%20Arcs.md), the [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md) and [Planeswalker Dossiers](Planeswalker%20Dossiers.md) in cycles 22, 24 and 25 were matched against this text (cycle 24 added pre-2019 web fiction for Kaladesh, Amonkhet, Ixalan and Theros; cycle 25 added ELD/THB/IKO/BRO-frame/MAT/LCI and the BFZ, SOI/EMN, Dominaria and WAR episodes).',
         '', '**Flags:** ✅ deepened this cycle (Cause · Key beats · Outcome · Lasting consequences, primary quotes) · 📚 fetched, deepening queued · ⚠️ secondary material (novels / e-books / comics) is **not** in this list — see [Side-Media Index](Side-Media%20Index.md).', '',
         '## Contents', '- [Coverage by arc](#coverage-by-arc)', "- [Planeswalker's Guides](#planeswalkers-guides)", '- [Secondary material (not ingested)](#secondary-material-not-ingested)', '- [Rebuild](#rebuild)', '',
         '## Coverage by arc', '| Arc | Status | Pages | Words | Conflicts & Arcs |', '|---|---|---|---|---|']
    for code, title, _ in ARCS:
        rs = by.get(code, [])
        if not rs: continue
        st = '✅' if code in DEEPENED else '📚'
        L.append(f"| {code} | {st} | {len(rs)} | {sum(int(r['words']) for r in rs):,} | [{title}](Conflicts%20%26%20Arcs.md#{anchor(title)}) |")
    other = by.get('', [])
    L.append(f"| other (older arcs, profiles, features) | 📚 | {len(other)} | {sum(int(r['words']) for r in other):,} | — |")
    L += ['', "## Planeswalker's Guides", '| Date | Title | Words |', '|---|---|---|']
    for r in guides:
        L.append(f"| {r['date']} | [{r['title']}]({r['url']}) | {int(r['words']):,} |")
    L += ['', '## Secondary material (not ingested)',
          '- ⚠️ Novels and e-books (e.g. *The Wildered Quest*, Invasion-block novels) were **not** fetched; claims that rest only on them stay flagged in [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) and [Side-Media Index](Side-Media%20Index.md).',
          '- ⚠️ Bloomburrow episodes after Ep. 5 and some side stories are absent from the magic.wizards.com sitemap snapshot used here (2026-10-15); they are queued, not assumed.',
          '- 🚫 Universes Beyond fiction is non-canonical to Multiverse continuity and is not indexed here.',
          '', '## Rebuild', '```bash', 'python3 scripts/build_primary_sources.py   # needs .cache/story/text22 (else rebuilds from data/primary_sources.csv)', '```', '']
    return '\n'.join(L)

def main():
    if C.exists() and any(C.glob('*.txt')):
        rows = scan()
        if '--check' not in sys.argv:
            with atomic_io.atomic_open(CSV, 'w', newline='') as fh:
                w = csv.DictWriter(fh, fieldnames=['date', 'title', 'kind', 'arc', 'words', 'url']); w.writeheader(); w.writerows(rows)
    else:
        rows = list(csv.DictReader(CSV.open()))
    txt = page(rows)
    if '--check' in sys.argv:
        body = lambda x: x.split('\n---\n', 1)[-1]
        ok = OUT.exists() and body(OUT.read_text()) == body(txt)
        print('primary sources:', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    if OUT.exists():
        fm = OUT.read_text().split('\n---\n', 1)[0]
        txt = fm + '\n---\n' + txt.split('\n---\n', 1)[-1]
    OUT.write_text(txt)
    print(f'primary sources: {len(rows)} pages, {sum(1 for r in rows if r["kind"]=="planeswalkers-guide")} guides -> {OUT.name}')

if __name__ == '__main__':
    main()
