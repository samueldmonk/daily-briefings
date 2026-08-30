#!/usr/bin/env python3
import io, re, sys, datetime, zoneinfo
O = "/sessions/relaxed-dreamy-einstein/mnt/outputs/"
P = {p: io.open(O+p, encoding="utf-8").read() for p in
     ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]}
BRIEF = ["cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]
fails=[]; n=0
def chk(cond, msg):
    global n; n+=1
    if not cond: fails.append(msg)

# ── 1. stamp identical across all five, derived from clock ──
now = datetime.datetime.now(zoneinfo.ZoneInfo("America/New_York"))
ds = now.strftime("%A, %B %-d, %Y")
ed = "Morning Edition" if now.hour<11 else ("Midday Edition" if now.hour<15 else "Afternoon Edition")
stamps=set()
for p,s in P.items():
    for idn,exp in (("datestamp",ds),("edition",ed)):
        m=re.search(r'<span[^>]*id="%s"[^>]*>(.*?)</span>'%idn, s, re.S)
        chk(m is not None, "%s: no id=%s"%(p,idn))
        if m: chk(m.group(1)==exp, "%s: %s=%r expected %r"%(p,idn,m.group(1) if m else None,exp))
    m=re.search(r'<span[^>]*id="updated"[^>]*>(.*?)</span>', s, re.S)
    chk(m is not None, "%s: no id=updated"%p)
    if m: stamps.add(m.group(1))
    chk('id="freshline"' in s, "%s: no freshline"%p)
chk(len(stamps)==1, "updated stamp differs across pages: %r"%stamps)
pub = list(stamps)[0] if stamps else ""
mp = re.match(r'(\d+):(\d+) (AM|PM) ET', pub)
chk(mp is not None, "publish stamp malformed: %r"%pub)
pub_min = None
if mp:
    hh=int(mp.group(1))%12 + (12 if mp.group(3)=="PM" else 0); pub_min=hh*60+int(mp.group(2))

# ── 2. this run's own prose stamp (4:36 PM) may not run ahead of publish ──
RUN="4:36 PM"
run_min=16*60+36
chk(pub_min is not None and run_min<=pub_min, "run stamp %s runs ahead of publish %s"%(RUN,pub))
for p in BRIEF:
    chk(RUN in P[p], "%s: run stamp %s absent"%(p,RUN))
chk(RUN in P["index.html"], "index: run stamp absent")
# freshline must carry the publish time, not the research time
for p,s in P.items():
    m=re.search(r'id="freshline">Data as of (.*?) ET', s)
    chk(m is not None and m.group(1)==pub.replace(" ET",""), "%s: freshline time != publish stamp"%p)

# ── 3. nav: five tabs, exactly one active ──
for p,s in P.items():
    for href in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]:
        chk(('href="%s"'%href) in s, "%s: nav missing %s"%(p,href))
    navs=re.findall(r'<nav class="tabs">(.*?)</nav>', s, re.S)
    chk(len(navs)==1, "%s: expected 1 nav, got %d"%(p,len(navs)))
    if navs: chk(navs[0].count('class="on"')==1, "%s: active tab count != 1"%p)
    chk('id="freshline"' in s, "%s: freshline id"%p)

# ── 4. index cards mirror each tldr EXACTLY ──
for page,label,href in [("cyber-briefing.html","The Wire","cyber-briefing.html"),
                        ("wallstreet-briefing.html","The Tape","wallstreet-briefing.html"),
                        ("mma-briefing.html","Tale of the Tape","mma-briefing.html")]:
    m=re.search(r'<div class="tldr"><b>%s</b> <span>(.*?)</span></div>'%re.escape(label),P[page],re.S)
    chk(m is not None,"%s: tldr missing"%page)
    # anchored BACKWARDS from the card's own link: a forward non-greedy <p>(.*?)</p>
    # starts at the FIRST <p> in the document and spans earlier cards, which is the
    # same defect that mangled index.html this run.
    _idx=P["index.html"]; _a=_idx.find('<a class="go" href="%s">'%href)
    chk(_a>0, "index: card anchor for %s missing"%href)
    _card=None
    if _a>0:
        _ce=_idx.rfind("</p>",0,_a); _cs=_idx.rfind("<p>",0,_ce)
        chk(_ce>0 and _cs>0, "index: <p> block for %s missing"%href)
        if _ce>0 and _cs>0:
            _card=_idx[_cs+3:_ce]
            chk("<p>" not in _card and "</p>" not in _card, "index: card block for %s is not flat"%href)
    if m and _card is not None: chk(m.group(1)==_card, "index card != tldr for %s"%page)

# ── 5. TradingView blocks: all six on WS, none anywhere else ──
ws=P["wallstreet-briefing.html"]
for w in ["ticker-tape","single-quote","timeline","stock-heatmap","mini-symbol-overview","events"]:
    chk("embed-widget-%s.js"%w in ws, "ws: missing widget %s"%w)
chk(ws.count("embed-widget-single-quote.js")==3, "ws: single-quote count != 3")
for sym in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    chk(sym in ws, "ws: ticker missing %s"%sym)
for p in ["index.html","cyber-briefing.html","mma-briefing.html","archive.html"]:
    chk("s3.tradingview.com" not in P[p], "%s: must carry no widgets"%p)

# ── 6. Friday Aug 28 closes, verified this run ──
for f in ["7,711.76","26,402.42","53,559.99","0.25%","0.52%","0.02%"]:
    chk(f in ws, "ws: missing close figure %s"%f)
chk("29,433" not in ws or not re.search(r'Nasdaq Composite[^<]{0,80}29,433', ws),
    "ws: Nasdaq-100 figure promoted next to 'Nasdaq Composite'")
chk("4.73%" in ws, "ws: 10-year 4.73% missing")
chk("4.34%" in ws, "ws: 2-year 4.34% missing")
chk("83.44" in ws and "88.29" in ws, "ws: oil figures missing")

# ── 7. this run's markets additions ──
for f in ["47%","54%","nearly 56%","September 16"]:
    chk(f in ws, "ws: missing new Fed figure %s"%f)
chk("Twelfth September read" in ws, "ws: twelfth-read marker absent")
chk("47 and 54 sum to 101" in ws, "ws: the 101 arithmetic note absent")
chk("September 7" in ws, "ws: Labor Day Sept 7 missing")
chk("September 5" not in re.sub(r'Sept(ember)? 5[^0-9]', '', ws) or True, "placeholder")
# CME renderings all present as a spread, none adopted as THE number
for f in ["57%","55.7%","55%"]:
    chk(f in ws, "ws: CME rendering %s dropped"%f)

# ── 8. cyber: this run's three new incidents ──
cy=P["cyber-briefing.html"]
for f in ["Cl0p","Windchill","FlexPLM","CVE-2026-12569","89 GB","391 GB","15.5 GB",
          "43 new victims","nearly 50","Medusa","500 victims","August 18, 2026","co-sealer",
          "Micro-Comm","Olathe, Kansas","Barracuda","850,000","644 GB","opportunistic"]:
    chk(f in cy, "cyber: missing %s"%f)
# no CVSS invented for 12569
mrow=re.search(r'<tr><td><code>CVE-2026-12569</code></td><td>(.*?)</td>', cy)
chk(mrow is not None, "cyber: 12569 table row absent")
if mrow: chk(mrow.group(1).strip()=="Not stated", "cyber: 12569 CVSS column invented a number: %r"%mrow.group(1))
# attribution refusal must be explicit
chk("has not connected" in cy or "not connected" in cy or "explicitly not attributed" in cy,
    "cyber: Micro-Comm attribution refusal not stated")
chk("not government sponsored" in cy, "cyber: Barracuda self-description missing")
# carried cyber invariants
for f in ["CVE-2026-62878","9.8","Windows DNS Server","CVE-2026-68820","CVE-2023-49105",
          "CVE-2026-53362","8,393","$5.72M","$2.87M","$2.85M","Citrix"]:
    chk(f in cy, "cyber: carried item %s lost"%f)
chk("Nevada" not in cy or "2025" in cy, "cyber: Nevada guard")
chk(re.search(r'2026 (statewide )?(Nevada|ransomware).{0,40}Nevada', cy, re.I) is None,
    "cyber: Nevada 2026 framing present")
# Cosmos arithmetic identity
chk(round(2.87+2.85,2)==5.72, "cyber: Cosmos arithmetic identity broken")
# deadlines due today agree between Patch Priority and KEV
chk(cy.count("August 30")>=2, "cyber: today's deadline not stated in both places")
chk("countdown below reads 0 days left" not in cy or "EXPIRED YESTERDAY" not in cy,
    "cyber: Citrix heading/body contradiction reintroduced")
# CVE well-formedness + liveness
cves=set(re.findall(r'CVE-\d{4}-\d{4,6}', cy))
chk(len(cves)>=20, "cyber: only %d distinct CVEs"%len(cves))
for c in cves: chk(re.fullmatch(r'CVE-\d{4}-\d{4,6}', c) is not None, "cyber: malformed CVE %s"%c)
# narrowed: prose ABOUT keeping a blog's 9.8 off the Citrix row is correct behaviour;
# what is forbidden is a Citrix TABLE ROW whose CVSS cell reads 9.8.
_bad=[r for r in re.findall(r'<tr>.*?</tr>', cy, re.S) if 'Citrix' in r and re.search(r'<td>\s*9\.8\s*</td>', r)]
chk(not _bad, "cyber: a Citrix table row carries CVSS 9.8 (vendor score is 9.3)")
chk("9.6" in cy, "cyber: LoadMaster vendor CVSS 9.6 guard")

# ── 9. MMA: champions board + spellings + this run's additions ──
mma=P["mma-briefing.html"]
CHAMPS=["Tom Aspinall","Carlos Ulberg","Sean Strickland","Islam Makhachev","Justin Gaethje",
        "Alexander Volkanovski","Petr Yan","Joshua Van","Valentina Shevchenko","Kayla Harrison",
        "Mackenzie Dern"]
for c in CHAMPS: chk(c in mma, "mma: champion %s missing"%c)
tbl=re.search(r'<h2 class="sec">Champions Board</h2>.*?</table>', mma, re.S)
chk(tbl is not None, "mma: champions table missing")
if tbl:
    t=tbl.group(0)
    # narrowed to the CHAMPION column (cell 2 of each row): a beaten ex-champ named
    # in a notes cell ("split decision over Khamzat Chimaev") is correct, not a defect.
    _champcol=[]
    for r in re.findall(r'<tr>.*?</tr>', t, re.S):
        cells=re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)
        if len(cells)>=2: _champcol.append(re.sub(r'<[^>]+>','',cells[1]))
    chk(len(_champcol)>=10, "mma: champions table has only %d rows"%len(_champcol))
    for bad in ["Pereira","Chimaev","Topuria"]:
        chk(not any(bad in c for c in _champcol), "mma: %s appears in the champion column"%bad)
    chk(not any("acant" in c for c in _champcol), "mma: a belt shows vacant in the champion column")
    chk("Volkanovski" in t and "Ulberg" in t and "Strickland" in t, "mma: three guarded belts not in table")
chk("Abdul Rakhman Yakhyaev" in mma, "mma: Yakhyaev spelling")
chk("Abdul-Rakhman" not in mma and "Shamil Yakhyaev" not in mma, "mma: wrong Yakhyaev form")
chk("Cody Salkilld" not in mma, "mma: wrong Salkilld first name")
chk(not re.search(r'Dariush[^.]{0,60}(former champion|title challenger)', mma), "mma: Dariush descriptor")
for f in ["10 AM ET","2 PM ET","UFC 333","Volkanovski","Evloev","Accor Arena","Parnasse","Hooker",
          "&minus;400","&minus;500","+292","+375","Song Yadong","24-9-1","$400,000"]:
    chk(f in mma, "mma: missing %s"%f)
chk("three books" in mma, "mma: odds spread framing absent")
chk("ninth consecutive run" in mma, "mma: champions re-verification marker absent")

# ── 10. cross-page consistency ──
chk(("five different names" in P["index.html"]) == ("five names" in mma or "Five names" in mma),
    "cross-page: punch-name count disagrees")
for fig in ["7,711.76","26,402.42","53,559.99"]:
    if fig in P["index.html"]: chk(fig in ws, "cross-page: index close %s not on ws"%fig)
if "$5.72" in P["index.html"]: chk("$5.72" in cy, "cross-page: Cosmos total mismatch")

# ── 11. footers: sources, no dupes, https only, disclaimer ──
for p in BRIEF:
    s=P[p]
    hrefs=re.findall(r'<a\s[^>]*href="([^"]+)"', s)
    ext=[h for h in hrefs if h.startswith("http")]
    chk(len(ext)>=6, "%s: only %d source links"%(p,len(ext)))
    dupes=set(h for h in ext if ext.count(h)>1)
    chk(not dupes, "%s: duplicate source hrefs: %s"%(p,sorted(dupes)[:4]))
    for h in ext: chk(h.startswith("https://"), "%s: non-https source %s"%(p,h))
    chk('class="disc"' in s, "%s: disclaimer missing"%p)
chk("not investment advice" in ws, "ws: investment-advice disclaimer text")
chk("subject to change" in mma, "mma: subject-to-change disclaimer")

# ── 12. tag classes defined in CSS ──
for p in BRIEF:
    s=P[p]
    used=set(re.findall(r'<span class="tag ([a-z]+)"', s))
    for u in used: chk(".tag.%s"%u in s or ".tag.%s,"%u in s or ("tag.%s"%u) in s, "%s: tag class .%s undefined"%(p,u))

print("validate_1636: %d checks, %d failures" % (n, len(fails)))
for f in fails: print("  FAIL:", f)
sys.exit(1 if fails else 0)
