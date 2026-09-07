# -*- coding: utf-8 -*-
import re, os, html, sys
R="/tmp/db_1788800764"; PAGES=["index","cyber-briefing","wallstreet-briefing","mma-briefing","archive"]
S={p:open(os.path.join(R,p+".html"),encoding="utf-8").read() for p in PAGES}
def txt(s): return html.unescape(re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',s))).replace('\xa0',' ')
T={p:txt(S[p]) for p in PAGES}
ok=[];bad=[]
def chk(c,why):
    (ok if c else bad).append(why)

# ---- structural: div balance AND first-open == last-close ----
for p in PAGES:
    s=S[p]; opens=len(re.findall(r'<div\b',s)); closes=len(re.findall(r'</div>',s))
    chk(opens==closes, "%s div balance %d/%d"%(p,opens,closes))
    stack=[]; pair_ok=True; first=None
    for m in re.finditer(r'<div\b|</div>', s):
        if m.group(0).startswith('</'):
            if not stack: pair_ok=False; break
            o=stack.pop()
            if not stack and first is None: first=o
        else: stack.append(m.start())
    chk(pair_ok and not stack, "%s div nesting well-formed"%p)
    chk(re.search(r'<div class="wrap"',s) is not None or p=="archive", "%s has wrap container"%p)

# ---- five-tab nav on every page ----
for p in PAGES:
    for href in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]:
        chk(href in S[p], "%s nav -> %s"%(p,href))
    chk(S[p].count('class="active"')>=1, "%s has an active tab"%p)

# ---- masthead ids + self-stamp JS on all four briefings ----
for p in PAGES[:4]:
    for i in ["edition","datestamp","updated","freshline"]:
        chk('id="%s"'%i in S[p], "%s has #%s"%(p,i))
    chk("America/New_York" in S[p], "%s self-stamp JS present"%p)

# ---- tldr strips with correct labels ----
for p,lab in [("cyber-briefing","The Wire"),("wallstreet-briefing","The Tape"),("mma-briefing","Tale of the Tape")]:
    m=re.search(r'<div class="tldr">.*?</div>',S[p],re.S)
    chk(m is not None,"%s has .tldr"%p)
    chk(m and lab in m.group(0), "%s tldr label = %s"%(p,lab))
chk('class="tldr"' not in S["index"], "index has no tldr strip (cards instead)")

# ---- NEW-TAG LEDGER: exactly 1, on cyber, on the Tengu card ----
tot=sum(S[p].count('class="t new"') for p in PAGES[:4])
chk(tot==1,"new-tag total is 1 (got %d)"%tot)
chk(S["cyber-briefing"].count('class="t new"')==1,"the 1 new tag is on cyber")
for p in ["wallstreet-briefing","mma-briefing","index"]:
    chk(S[p].count('class="t new"')==0,"%s carries 0 new tags"%p)
i=S["cyber-briefing"].find('class="t new"')
chk("Tengu" in S["cyber-briefing"][i:i+900],"the new tag sits on the Tengu card")
# and Tengu must be ABSENT from the previous archived snapshot
prev=open(os.path.join(R,"archive/cyber-2026-09-07-1245.html"),encoding="utf-8").read()
chk("Tengu" not in prev,"Tengu absent from archive/cyber-2026-09-07-1245.html (genuinely new)")
chk('class="t new"' in prev,"prev cyber snapshot had a new tag (ledger self-test non-trivial)")
for f in ["wallstreet","mma"]:
    pv=open(os.path.join(R,"archive/%s-2026-09-07-1245.html"%f),encoding="utf-8").read()
    chk('class="t new"' not in pv,"prev %s snapshot had 0 new tags, matching this edition's claim"%f)

# ---- stale-provenance sweep: no bare "this edition" outside the current run's own additions ----
for p in PAGES[:4]:
    n=T[p].count("this edition")
    chk(n>0,"%s labels its own additions 'this edition' (%d)"%(p,n))
chk("the 12:45 edition" in T["cyber-briefing"],"previous edition demoted to 'the 12:45 edition'")

# ---- MARKETS: Labor Day, closes, no fabricated single Brent level ----
ws=T["wallstreet-briefing"]
chk("Labor Day" in ws,"WS states Labor Day")
chk("closed all day" in ws or "shut all day" in ws,"WS states markets closed all day")
chk("8 September" in ws,"WS names Tuesday 8 September reopen")
for v in ["7,718.60","26,506.99","53,414.25"]:
    chk(v in ws,"WS carries verified Friday close %s"%v)
chk("162,000" in ws,"WS carries the verified 162,000 payroll print")
chk("53,000" in ws,"WS carries the 53,000 consensus")
chk("55,000" not in ws or "revision" in ws,"WS does not assert 55,000 as consensus")
chk("4.1%" in ws,"WS carries the 4.1% unemployment rate")
chk("$5.85" in ws,"WS carries the CURRENT diesel record $5.85")
for m_ in re.finditer(r'\$5\.820', ws):
    seg=ws[max(0,m_.start()-400):m_.start()+400]
    chk(any(w in seg for w in ["supersed","corrected","corrects","retained","correction trail",
                               "beat it again","3 September","had been printing","had been carrying"]),
        "every $5.820 occurrence sits in superseding context")
chk("all-time high of $5.820" not in ws,"banned string 'all-time high of $5.820' absent")
# the tldr must NOT assert a single Brent level while the body refuses one
tl=txt(re.search(r'<div class="tldr">.*?</div>',S["wallstreet-briefing"],re.S).group(0))
chk("No single Brent level is asserted" in ws,"WS body keeps the no-single-level refusal")
chk(not re.search(r'Brent trades at \$9\d\.\d\d', tl),"WS tldr does not assert a single Brent level")
chk("97.27" in tl and "97.50" in tl,"WS tldr gives the range instead")
chk("$97.50" in ws and "2:34" in ws,"WS carries the sixth reading with its timestamp")
chk("lowest since May" in ws,"WS carries the second route to the Hormuz traffic low")
chk("four-month low" in ws,"WS still carries the four-month-low framing it corroborates")

# ---- CYBER: countdowns arithmetic against 7 September ----
cy=T["cyber-briefing"]
for due,days in [("14 September",7),("16 September",9),("18 September",11)]:
    m_=re.search(re.escape(due)+r'[^.]{0,40}?\((\d+) days left\)',cy)
    chk(m_ is not None and int(m_.group(1))==days,"KEV %s = %d days left"%(due,days))
chk("overdue by 2 days" in cy,"5 September KEV group overdue by 2 days")
chk("14 September" in cy,"PaperCut 14 September deadline present")
# patch priority and KEV must name the SAME deadline
i=cy.find("Patch Priority"); chk(i>=0,"Patch Priority box present")
chk("14 September" in cy[i:i+2500],"Patch Priority uses the same 14 September deadline")
# ScreenConnect card: no CVE / CVSS / countdown inside it
m_=re.search(r'<div class="card">(?:(?!</div>\s*<div class="card">).)*?ScreenConnect(?:(?!<div class="card">).)*?</div>\s*(?=<h2|<div class="card")',S["cyber-briefing"],re.S)
sc = txt(m_.group(0)) if m_ else ""
chk(sc!="","ScreenConnect card isolated")
chk(not re.search(r'CVE-20\d\d-\d+',sc),"no CVE id inside the ScreenConnect card")
chk("days left" not in sc,"no KEV countdown inside the ScreenConnect card")
chk("no CVE" in sc,"ScreenConnect card says there is no CVE")
# Tengu card: malware, so no CVE / CVSS / countdown, and no exploitation-of-a-flaw claim
i0=S["cyber-briefing"].find('class="t new"')
i1=S["cyber-briefing"].find('<div class="card">', i0)
tg=txt(S["cyber-briefing"][i0:i1]) if (i0>=0 and i1>i0) else ""
chk("Tengu" in tg,"Tengu card isolated")
chk(not re.search(r'CVE-20\d\d-\d+',tg),"no CVE id inside the Tengu card")
import re as _re
chk(not _re.search(r'CVSS\s*(?:v\d(?:\.\d)?\s*)?\d', tg),"no CVSS SCORE asserted inside the Tengu card")
chk("no CVE and no CVSS" in tg,"Tengu card explicitly negates CVE and CVSS")
chk("days left" not in tg,"no KEV countdown inside the Tengu card")
chk("not in the CISA KEV" in tg,"Tengu card states it is not in KEV")
chk("no victim count" in tg and "no attribution" in tg,"Tengu card states what it does not know")
chk("464 functions" in tg and "kworker" in tg and "ELFOOD" in tg,"Tengu card carries the sourced specifics")
chk("late July 2026" in tg,"Tengu card dates the original research, not just today's analysis")
chk("7 September 2026" in tg,"Tengu card dates today's analysis")
# 84147 stays disclosed-not-exploited
chk("84147" in cy,"CVE-2026-84147 still on the page")
hits=[m.start() for m in re.finditer(r'CVE-2026-84147',cy)]
chk(any("10.0" in cy[h:h+220] for h in hits),"84147 carries CVSS 10.0 at its table row")
chk(any("not exploited" in cy[max(0,h-500):h+1400] for h in hits),
    "84147 still labelled disclosed, not exploited")

# ---- MMA: champions board vs the six verified this run; regressions absent ----
mm=T["mma-briefing"]
for name in ["Aspinall","Ulberg","Strickland","Makhachev","Gaethje","Volkanovski","Yan","Van","Shevchenko","Harrison","Dern"]:
    chk(name in mm,"champions board names %s"%name)
for m_ in re.finditer(r'Pereira',mm):
    seg=mm[max(0,m_.start()-260):m_.start()+260]
    chk("Light Heavyweight champion" not in seg,"Pereira never called LHW champion")
BEAT=r'(?:decision over|UD over|SD |Split decision|TKO|KO\d|Sub\d|Submission|defeat|beat|over |defends against|rematch|vs\.? )'
for div_,wrong in [("Middleweight","Chimaev"),("Lightweight","Topuria"),
                   ("Light Heavyweight","Pereira"),("Flyweight","Pantoja"),("Bantamweight","Dvalishvili")]:
    bad_=False
    for m_ in re.finditer(re.escape(div_)+r'(.{0,90}?)'+re.escape(wrong),mm):
        if not re.search(BEAT,m_.group(1)): bad_=True
    chk(not bad_,"%s champion is not %s (defeat-token aware)"%(div_,wrong))
# Parnasse guard
for m_ in re.finditer(r'Contender Series',mm):
    seg=mm[max(0,m_.start()-300):m_.start()+300]
    chk(("Parnasse" not in seg) or ("not a" in seg) or ("NOT" in seg),"Contender Series never attributed to Parnasse")
chk("KSW" in mm,"Parnasse's actual pedigree (KSW) is on the page")
# Paris weekday: 5 September 2026 is a Saturday
for m_ in re.finditer(r'Friday',mm):
    seg=mm[max(0,m_.start()-160):m_.start()+160]
    chk("Paris" not in seg,"no 'Friday' within 160 chars of 'Paris'")
chk("Saturday 5 September" in mm or "Saturday&nbsp;5" in S["mma-briefing"],"Paris card dated as a Saturday")
# bonuses + odds only as sourced
chk("$100,000" in mm and "$25,000" in mm,"Paris bonus tiers carried")
chk("425" in mm and "355" in mm,"Noche UFC odds carried as sourced")
# countdown bar
chk('id="ufccdn"' in S["mma-briefing"],"MMA countdown element present")
# no event described as upcoming that has already happened
chk(not re.search(r'[Uu]pcoming[^.]{0,120}5 September',mm),"Paris (5 Sep) not described as upcoming")

# ---- widgets on wall street ----
for w in ["ticker-tape","single-quote","timeline","stock-heatmap","mini-symbol-overview","events"]:
    chk("embed-widget-"+w in S["wallstreet-briefing"],"WS widget block %s"%w)
chk(S["wallstreet-briefing"].count("embed-widget-single-quote")==3,"three single-quote widgets")
chk('class="livebar"' in S["wallstreet-briefing"],"livebar wrapper present")
for sym in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    chk(sym in S["wallstreet-briefing"],"ticker keeps %s"%sym)
chk("investment advice" in ws and ("Nothing here is" in ws or "not investment advice" in ws),
    "WS disclaimer present")
chk("subject to change" in mm,"MMA disclaimer present")

# ---- sources footers ----
for p in PAGES[:4]:
    if p=="index": continue
    chk(T[p].count("Sources")>=1,"%s has a Sources footer"%p)
    chk(S[p].count("https://")>=8,"%s footer carries real URLs"%p)

print("PASS %d   FAIL %d"%(len(ok),len(bad)))
for b in bad: print("  FAIL:",b)
sys.exit(1 if bad else 0)
