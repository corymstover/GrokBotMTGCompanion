"""Build "Rules Interactions.md": verbatim Comprehensive Rules (2026-09-25; download the official .txt to .cache/MagicCompRules-20260925.txt or set CR_TXT) + official WotC rulings from the Scryfall rulings bulk. Bot cycles 3–5. CR "Example:" paragraphs (official) are attached to the rule they follow."""
import atomic_io  # noqa: F401  atomic Path.write_text/write_bytes (Bot cycle 34)
import sys,csv,json,gzip,re,os,pathlib
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import ingest_scryfall as ing
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')+'/'
CRURL="https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt"
cr={}; crex={}; last=None; body=False
for l in open(os.environ.get('CR_TXT','.cache/MagicCompRules-20260925.txt'),encoding='utf-8'):
    s=l.strip()
    if s=='Glossary' and len(cr)>2000: break
    m=re.match(r'^(\d{3}\.\d+[a-z]*)\.? (.*)',s)
    if m:
        if m.group(1) not in cr: cr[m.group(1)]=m.group(2)
        last=m.group(1)
    elif s.startswith('Example:') and last: crex.setdefault(last,[]).append(s[len('Example:'):].strip())
idx=list(csv.DictReader(open(R+'data/card_index.csv')))
byoid={r['oracle_id']:r for r in idx}
def rank(r):
    try: return int(r['edhrec_rank'])
    except: return 10**9
rul={}
for l in gzip.open(R+'.cache/rulings-20261015090033.jsonl.gz','rt'):
    x=json.loads(l)
    if x['oracle_id'] in byoid and x.get('source')=='wotc': rul.setdefault(x['oracle_id'],[]).append(x)
def examples(pat,n=6,excl=None):
    out=[]
    for oid,rs in rul.items():
        for x in rs:
            if re.search(pat,x['comment'],re.I) and not (excl and re.search(excl,x['comment'],re.I)):
                out.append((rank(byoid[oid]),byoid[oid],x)); break
    out.sort(key=lambda t:t[0]); seen=set(); res=[]
    for e in out:
        k=e[2]['comment'][-60:]
        if k in seen: continue
        seen.add(k); res.append(e)
    return res[:n]
def q(num,full=False):
    t=cr[num]
    if not full and len(t)>420: t=t[:420].rsplit(' ',1)[0]+' …'
    return f"> **CR {num}** — {t}"
topics=[
("Layers & timestamps","613",["613.1","613.1a","613.1b","613.1c","613.1d","613.1e","613.1f","613.1g","613.4","613.4a","613.4b","613.4c","613.4d","613.7"],r'\blayer \d|layers? system|in layer|apply in (the )?(applicable|appropriate) layer',r'wearing|garment',"Continuous effects are applied in seven layers (and sublayers for 1 and 7); within a layer, timestamp order decides unless a dependency exists.",[]),
("Dependency","613.8",["613.8","613.8a","613.8b","613.8c"],r'Humility and Opalescence|Urborg[^.]{0,120}Blood Moon|Blood Moon[^.]{0,120}Urborg|Opalescence[^.]{0,80}Humility',None,"A dependency overrides timestamp order inside the same layer/sublayer. Official card rulings rarely use the word \"dependency\"; the rulings below are the ones in the bulk that settle classic dependency/layer cases (Humility + Opalescence; Blood Moon + Urborg). ⚠️ Any card pair not listed here should be worked through CR 613.8 directly.",[]),
("Replacement effects vs. triggered abilities","614",["614.1","614.1a","603.1","616.1","616.1e","616.1f"],r'replacement effect',None,"A replacement effect modifies an event as it happens (often \"instead\") and never uses the stack; a triggered ability (\"when/whenever/at\") goes on the stack after the event. When several replacement effects apply, the affected object's controller (or the affected player) picks the order.",[]),
("State-based actions","704",["704.3","704.5a"],r'state-based action',None,"SBAs are checked whenever a player would get priority and all applicable ones happen simultaneously; they don't use the stack.",[]),
("Copy effects","707",["707.2","707.2a","707.2b","707.2c"],r'copiable values?|copy effect|enters? (the battlefield )?as a copy|becomes? a copy',None,"Copies take only copiable values (printed values as modified by other copy effects), not counters, Auras, or other effects.",[]),
("Commander: color identity","903.4",["903.4","903.4a","903.4b","903.4c","903.4d","903.4e","903.4f"],r'color identity',r'two commanders|partner',"Color identity is mana symbols in the cost and rules text (plus color indicators/characteristic-defining abilities), including back faces; reminder text is ignored.",[]),
("Commander: returning to the command zone","903.9",["903.9","903.9a","903.9b","903.9c"],r'(put|move|return)[^.]{0,60}(in)?to the command zone|command zone instead|state-based action[^.]*command zone',r'partner|two commanders|dungeon|Undercity',"From graveyard or exile, the owner *may* move the commander to the command zone as a state-based action (so \"dies\"/\"leaves\" triggers still see it go to the graveyard first); from hand or library it's a replacement effect.",[]),
("Worked layer examples (official CR examples)","613",[],r'Humility and Opalescence|layer 7[a-d]|layer 1|layer 4',None,"Every example below is an **official Example paragraph from the CR**, printed under the rule it illustrates; they are the safest worked layer cases because Wizards wrote them.",["613.4c","613.4d","613.5","613.6","613.7a","613.8a","613.9"]),
("Stack & priority","117 / 405 / 608",["117.1a","117.3a","117.3b","117.3c","117.3d","117.4","405.1","405.2","405.5","405.6","608.2b"],r'in response|holds? priority|while (it|that ability|the ability) is on the stack',None,"The active player gets priority first; a player who casts a spell or activates an ability gets priority again afterward (117.3c). The top object of the stack resolves only when all players pass in succession (117.4, 405.5). Some things don't use the stack (405.6). On resolution a spell or ability rechecks its targets; if all are illegal it doesn't resolve (608.2b).",[]),
("Casting vs. copying a spell","601 / 707.10 / 707.12",["601.2","601.2a","601.2f","601.2h","601.2i","707.10","707.10a","707.10c","707.12"],r"(isn't|wasn't|aren't|is not) cast|cast a copy|copy of (a|the|that) spell",None,"A copy of a spell put onto the stack **isn't cast** (707.10), so \"whenever you cast\" triggers don't see it; it copies modes, targets, X and costs paid. An effect that says **cast a copy** follows casting steps 601.2a–h and the copy **is** cast (707.12).",["707.10"]),
("Combat damage assignment","510",["510.1","510.1a","510.1b","510.1c","510.1d","510.1e","510.2","510.4","702.7b"],r'assigns? (its )?combat damage|combat damage step',None,"Each creature assigns combat damage equal to its power; a blocked creature divides damage among its blockers as its controller chooses (510.1c), and all combat damage is dealt simultaneously (510.2). First or double strike creates an extra combat damage step (510.4).",["510.1c"]),
("Deathtouch + trample","702.2 / 702.19",["702.2b","702.2c","702.19b","702.19c"],r'deathtouch[^.]*trample|trample[^.]*deathtouch',None,"With deathtouch, any nonzero combat damage assigned to a creature counts as lethal for assigning excess (702.2c), so a deathtouch + trample attacker needs to assign only 1 damage to each blocker and can assign the rest to the player, planeswalker or battle (702.19b).",["702.19b","702.19c"]),
("Protection","702.16",["702.16a","702.16b","702.16c","702.16d","702.16e","702.16f","702.16j","702.16k"],r'protection from',r'phas',"Protection from a quality means: can't be targeted by spells/abilities with that quality, enchanted or equipped by such Auras/Equipment, blocked by such creatures (when attacking), and damage from such sources is prevented (702.16b–f).",[]),
("Hexproof, shroud & ward","702.11 / 702.18 / 702.21",["702.11b","702.11c","702.11d","702.11e","702.18a","702.21a","702.21b"],r'\bward\b|hexproof|shroud',None,"Hexproof stops targeting by spells/abilities **opponents** control (702.11b); shroud stops targeting by **any** player (702.18a); ward is a **triggered ability** that counters an opponent's spell or ability targeting the permanent unless they pay the cost (702.21a) — so it uses the stack and can be responded to.",[]),
("ETB / LTB & look-back triggers","603.6 / 603.10",["603.2","603.6a","603.6c","603.6d","603.10","603.10a"],r'leaves the battlefield|look(s)? back in time|last known information',None,"Enters-the-battlefield triggers check the battlefield after the event, including the newcomers (603.6a). Leaves-the-battlefield triggers \"look back in time\" (603.10a), so they see the game as it was just before the permanent left. \"Enters with …\" / \"enters tapped\" text is a static ability, not a triggered ability; its effect happens as part of the event (603.6d).",["603.10a"]),
("Mutate & merged permanents","702.140 / 730",["702.140a","702.140b","702.140c","702.140d","702.140e","730.2","730.2a","730.2b","730.2c","730.3"],r'\\bmutates?\\b|mutating|merged (creature|permanent)',None,"A mutating creature spell with a legal target doesn't enter the battlefield; it merges with the target (702.140c). The merged permanent is the **same object** it was before — it hasn't just come under your control and existing effects keep applying (730.2c) — and uses the characteristics of its topmost component (730.2a) plus all abilities of every component (702.140e).",[]),
("Commander tax","903.8",["903.8"],r'commander tax|additional \{2\}|cast (it )?from the command zone',r'partner|two commanders',"Casting your commander from the command zone costs {2} more for each previous time **you** cast it from the command zone this game (903.8); casts from anywhere else don't count.",[]),
("Sagas","714",["714.2","714.2b","714.2d","714.3a","714.3c","714.4"],r'lore counters?|chapter abilit',None,"A Saga enters with a lore counter (714.3a). As your precombat main phase begins you add another lore counter as a turn-based action that doesn't use the stack (714.3c). Each chapter is a **triggered ability** that triggers when the count reaches its number (714.2b). Once the counters are at least the final chapter number and no chapter ability from it is still on the stack, the Saga is sacrificed as a state-based action (714.4).",[]),
("Classes","716",["716.1","716.2","716.2a","716.2b","716.2d","716.3","716.4"],r'level ability of a Class|Class becomes level|class level bar|Each Class (starts|has)|gain a level',r'level up|level counter',"Gaining a Class level is an **activated ability, sorcery speed only**, and you can level only from N-1 to N, so you can't skip levels (716.2a). Abilities from earlier levels stay. A level is not a copiable value (716.2b). Class levels are not level counters (716.4).",[]),
("Phasing","702.26",["702.26a","702.26b","702.26d","702.26g","702.26k","702.26m"],r'phas(e|es|ed|ing) (out|in)\b',r'main phase|combat phase|beginning phase|ending phase',"A phased-out permanent is treated as though it doesn't exist and is removed from combat (702.26b). It **doesn't change zones**, so no enter/leave triggers fire and its counters stay (702.26d). Attached Auras and Equipment phase out with it (702.26g). It phases back in during its controller's next untap step (702.26a).",["702.26b"]),
("Double-faced cards & transform","712 / 701.27",["712.8a","712.8d","712.8e","712.11","712.14","712.18","701.27a","701.27c","701.27f"],r'transforms?\b|double-faced|back face',r'meld',"Outside the battlefield and stack a DFC has only its front face's characteristics (712.8a), so for example its mana value is the front face's. A transforming permanent is the **same object**, so effects on it keep applying (712.18). An ability that would transform a permanent does nothing if the permanent already transformed since that ability went on the stack (701.27f).",["712.9","712.13a","712.18"]),
("The legend rule","704.5j",["704.5j","306.4"],r'legend rule',None,"If you control two or more legendary permanents with the same name, you choose one and the rest go to their owners' graveyards as a state-based action (704.5j). Different players can each control one with the same name. Planeswalkers follow the same rule (306.4).",[]),
("\"Can't\" beats \"can\" (and impossible instructions)","101.2 / 101.3",["101.1","101.2","101.3","101.4"],r"“can.t” (effect|wins)|can.t[^.]{0,60}takes precedence|takes precedence over[^.]{0,60}can",None,"When one effect allows something and another says it **can't** happen, the \"can't\" wins (101.2). The parts of an instruction that are impossible are ignored (101.3). Simultaneous choices are made in APNAP order (101.4).",["101.2","101.4"]),
("Ordering replacement effects (worked examples)","616",["616.1","616.1a","616.1b","616.1c","616.1d","616.1e","616.1f","616.1g","614.15"],r'self-replacement|replacement effects?[^.]{0,80}(order|choose which)|(order|which order)[^.]{0,80}replacement',None,"The affected player, or the controller of the affected object, chooses the order. Self-replacement effects come first (616.1a, 614.15), then effects that change who controls an entering object (616.1b), then copy-as-it-enters effects (616.1c) and back-face-up effects (616.1d), then any others (616.1e). After each one is applied, re-check which effects still apply (616.1f).",["616.1f","616.1g","616.2"]),
("Commander damage","903.10a / 704.6c",["903.10a","704.6c","702.124d"],r'21 or more combat damage|commander damage|combat damage[^.]{0,60}(that|the same|a) commander',None,"A player who has been dealt **21 or more combat damage by the same commander** over the game loses. This is a state-based action (903.10a, 704.6c). Only **combat** damage counts. Partner commanders are tracked separately (702.124d).",[]),
("Partner & Backgrounds","702.124",["702.124a","702.124b","702.124c","702.124d","702.124f","702.124h","702.124j","702.124k"],r'\bpartner\b|choose a background',None,"Partner variants let you have two commanders (100 cards total, 702.124b). Your color identity is the combined identity of both (702.124c). Each commander has its own commander tax and its own commander-damage count (702.124d). Different partner abilities can't be combined (702.124f).",[]),
("When a player leaves a multiplayer game","800.4",["800.4a","800.4b","800.4d","800.4e","800.4j","800.4m"],r'leaves? the game|left the game',r'attacking creature',"When a player leaves a multiplayer game, everything they **own** leaves with them, and effects that gave them control of something end. Anything they still control after that is exiled (800.4a). Damage that would be assigned to a player who has left isn't assigned (800.4e).",["800.4a","800.4d"]),
]
def slug(h): h=h.lower(); h=re.sub(r'[^\w\- ]','',h); return h.replace(' ','-')
o=["# Rules Interactions\n",
f"> **Source of truth:** Magic: The Gathering **Comprehensive Rules, effective 2026-09-25** ([official text]({CRURL}), Wizards of the Coast). Rule text below is **quoted verbatim** (long rules trimmed with \"…\"); card rulings are **official WotC rulings** from the Scryfall rulings bulk (2026-10-15), quoted verbatim and linked to the card entries that carry them. Plain-language summaries are labeled **Summary** and are paraphrase, not rules text. Started Bot cycle 3, extended Bot cycles 4–5 (issue [#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9)).\n",
"## Contents"]
for t in topics: o.append(f"- [{t[0]}](#{slug(t[0])}) — CR {t[1]}")
o.append("- [Open questions / next topics](#open-questions--next-topics)\n")
total=0; crx=[0]
for name,num,rules,pat,excl,summ,exr in topics:
    o.append(f"## {name}\n")
    o.append(f"**Summary:** {summ}\n")
    for r_ in rules:
        if r_ in cr: o.append(q(r_)); o.append(">")
    if o and o[-1]==">": o.pop()
    exs=[(r_,e) for r_ in exr for e in crex.get(r_,[])]
    if exs:
        o.append(f"\n**Official CR examples** ({len(exs)}):\n")
        for r_,e in exs: o.append(f"- *CR {r_} example* — {e}")
        crx[0]+=len(exs)
    ex=examples(pat,6,excl); total+=len(ex)
    o.append(f"\n**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):\n")
    if not ex: o.append("- ⚠️ No official card ruling in the bulk matched this topic; rely on the quoted CR text.")
    for _,row,x in ex:
        o.append(f"- {ing.link(row,'')} — *{x['published_at']}* — \"{x['comment']}\"")
    o.append("")
o.append("## Open questions / next topics\n- Possible further topics: morph/disguise & face-down (708), split/adventure/omen cards (709, 715), the monarch & initiative (724, 725), day/night (726), dungeons (309), banding (702.22).\n- ❓ Any rule summary here that disagrees with the quoted text is an error: the quoted CR text wins.")
pathlib.Path(R+'Rules Interactions.md').write_text("\n".join(o)+"\n")
print('topics',len(topics),'rulings quoted',total,'CR examples',crx[0])
