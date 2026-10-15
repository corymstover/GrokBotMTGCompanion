#!/usr/bin/env python3
"""Bot cycle 5 (issue #14): index the official Magic story archive beyond the sitemap.

Steps (each resumable):
  enumerate  - collect candidate URLs from the magic.wizards.com sitemap and from the
               Wayback Machine CDX index of the retired /en/articles/archive/uncharted-realms/
               and /en/articles/archive/magic-story/ paths -> .cache/story/candidates.txt
  fetch      - for each candidate slug try the live site (/en/news/feature/, /en/news/magic-story/),
               else the Internet Archive snapshot (flagged "archived"); page text is cached in
               .cache/story/text/ (gitignored; full text is never committed)
  index      - write data/story_index.csv (date, title, source, words, url) and
               "Story Archive Index.md" from one or more text directories (--dirs)

Usage:
  python3 scripts/crawl_story_index.py enumerate
  python3 scripts/crawl_story_index.py fetch
  python3 scripts/crawl_story_index.py index [--dirs DIR ...] [--dates dates.json]
"""
import argparse, csv, glob, json, os, re, sys, time, urllib.request
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/'
C = R + '.cache/story/'
UA = {'User-Agent': 'Mozilla/5.0 (GrokBotMTGCompanion lore research)'}
OLD = ['uncharted-realms', 'magic-story']

def get(u, t=90):
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t)
        return r.read().decode('utf-8', 'ignore')
    except Exception:
        return None

def enumerate_():
    os.makedirs(C, exist_ok=True); out = set()
    sm = get('https://magic.wizards.com/sitemap.xml') or ''
    for u in re.findall(r'<loc>([^<]+)</loc>', sm):
        if '/magic-story/' in u or '/story/' in u: out.add(('sitemap', u.rstrip('/').split('/')[-1]))
    for p in OLD:
        cdx = get(f'https://web.archive.org/cdx/search/cdx?url=magic.wizards.com/en/articles/archive/{p}/&matchType=prefix&fl=original&collapse=urlkey&filter=statuscode:200', 900) or ''
        for l in cdx.split('\n'):
            m = re.search(rf'/{p}/([a-z0-9-]+)/?(?:\?.*)?$', l.strip())
            if m: out.add((p, m.group(1)))
    with open(C + 'candidates.txt', 'w') as fh:
        for k, s in sorted(out): fh.write(f'{k}\t{s}\n')
    print('candidates', len(out))

def fetch():
    from bs4 import BeautifulSoup
    os.makedirs(C + 'text', exist_ok=True)
    for l in open(C + 'candidates.txt'):
        kind, s = l.rstrip('\n').split('\t'); fn = f'{C}text/{s}.txt'
        if os.path.exists(fn): continue
        tries = [('live', 'https://magic.wizards.com/en/news/feature/' + s), ('live', 'https://magic.wizards.com/en/news/magic-story/' + s)]
        if kind in OLD: tries.append(('archived', f'https://web.archive.org/web/2019id_/https://magic.wizards.com/en/articles/archive/{kind}/{s}'))
        for src, u in tries:
            h = get(u)
            if h and len(h) > 2000: break
        else:
            continue
        soup = BeautifulSoup(h, 'lxml'); title = (soup.title.string or '').strip() if soup.title else ''
        m = re.search(r'"datePublished":"([^"]+)"', h) or re.search(r'<time[^>]*datetime="([^"]+)"', h)
        for t in soup(['script', 'style', 'nav', 'header', 'footer', 'noscript']): t.decompose()
        main = soup.find('article') or soup.find(id='content') or soup.find('main') or soup.body
        txt = main.get_text('\n', strip=True) if main else ''
        open(fn, 'w').write(f'URL: {u}\nSOURCE: {src}\nTITLE: {title}\nDATE: {m.group(1) if m else ""}\n\n{txt}')
        time.sleep(0.5)

def index(dirs, dates_file):
    dates = json.load(open(dates_file)) if dates_file and os.path.exists(dates_file) else {}
    eng = lambda t: len(re.findall(r'\b(the|and|of|to)\b', t)) >= 25
    rows = []
    for d in dirs:
        for f in glob.glob(f'{d}/*.txt'):
            t = open(f, encoding='utf-8', errors='ignore').read()
            h = dict(re.findall(r'^(URL|SOURCE|TITLE|DATE): ?(.*)$', t[:1500], re.M)); body = t.split('\n\n', 1)[-1]
            if not eng(body) or len(body) < 1500: continue
            slug = os.path.basename(f)[:-4]
            title = re.sub(r'\s*\|\s*MAGIC: THE GATHERING.*$|\s*\|\s*Magic: The Gathering.*$', '', h.get('TITLE', '')).strip() or slug
            if title.lower().startswith(('article archives', 'page not found')) or title.lower() == 'magic: the gathering': continue
            date = (dates.get(slug) or h.get('DATE') or '')[:10]
            if not date:
                m = re.search(r'(\d{4})-(\d{2})-(\d{2})(?:-\d)?$', slug); date = '-'.join(m.groups()) if m else ''
            rows.append(dict(date=date, title=title, url=h.get('URL', ''), source=h.get('SOURCE', 'live'), words=len(body.split())))
    seen = set(); out = []
    for r in sorted(rows, key=lambda r: (r['date'] or '0000', r['title'])):
        k = (r['title'].lower(), r['date'])
        if k in seen: continue
        seen.add(k); out.append(r)
    with open(R + 'data/story_index.csv', 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=['date', 'title', 'source', 'words', 'url']); w.writeheader(); w.writerows(out)
    by = {}
    for r in out: by.setdefault(r['date'][:4] or 'undated', []).append(r)
    nl = sum(r['source'] == 'live' for r in out); na = len(out) - nl
    o = ["# Story Archive Index\n",
         f"> This index lists every official Wizards of the Coast story or lore page in the project's research corpus: **{len(out)} pages**. Of these, {nl} are live on magic.wizards.com and **{na} are archived** copies read from the Internet Archive. Built by `scripts/crawl_story_index.py` (Bot cycle 5, issue [#14](https://github.com/corymstover/GrokBotMTGCompanion/issues/14)).",
         "> Where the list comes from: the magic.wizards.com sitemap, the Wayback Machine CDX index of the retired `/en/articles/archive/uncharted-realms/` and `/en/articles/archive/magic-story/` paths, and the feature pages cited in the lore files.",
         "> Legend: **live** means fetched from magic.wizards.com in 2026-10. **🗄️ archived** means the page no longer resolves on the live site and was read from a web.archive.org snapshot. Treat archived pages as official but historical. Dates come from page metadata or the URL slug. Full text is never committed; the machine-readable list is [data/story_index.csv](data/story_index.csv).\n",
         "## Contents"]
    ys = sorted(by, key=lambda y: (y == 'undated', y))
    o.append(" · ".join(f"[{y}](#{y}) ({len(by[y])})" for y in ys) + "\n")
    for y in ys:
        o.append(f"## {y}\n\n| Date | Title | Source |\n|---|---|---|")
        for r in by[y]:
            o.append(f"| {r['date'] or '—'} | [{r['title'].replace('|', chr(92) + '|')}]({r['url']}) | {'live' if r['source'] == 'live' else '🗄️ archived'} |")
        o.append("")
    open(R + 'Story Archive Index.md', 'w').write("\n".join(o) + "\n")
    print('indexed', len(out), 'live', nl, 'archived', na)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('step', choices=['enumerate', 'fetch', 'index'])
    ap.add_argument('--dirs', nargs='*', default=[C + 'text'])
    ap.add_argument('--dates', default=None)
    a = ap.parse_args()
    {'enumerate': enumerate_, 'fetch': fetch}.get(a.step, lambda: index(a.dirs, a.dates))()
