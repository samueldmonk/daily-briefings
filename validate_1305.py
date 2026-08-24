#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Programmatic validation for the 2026-08-24 ~1:05pm ET Midday Edition."""
import io, re, json, sys
from html.parser import HTMLParser

D = "/sessions/amazing-bold-curie/mnt/outputs/"
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
BRIEFS = PAGES[1:]
fails, checks = [], [0]

def ck(cond, msg):
    checks[0] += 1
    if not cond: fails.append(msg)

def load(f): return io.open(D+f, encoding="utf-8").read()
S = {f: load(f) for f in PAGES}

VOID = {"br","img","hr","meta","link","input","source","col","area","base","embed","param","track","wbr"}
class Bal(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.st=[]; self.stray=0
    def handle_starttag(self,t,a):
        if t not in VOID: self.st.append(t)
    def handle_endtag(self,t):
        if t in VOID: return
        if self.st and self.st[-1]==t: self.st.pop()
        elif t in self.st:
            while self.st and self.st.pop()!=t: pass
        else: self.stray+=1

# 1. structural balance
for f in PAGES:
    p = Bal(); p.feed(S[f])
    ck(len(p.st)==0, "%s: %d unclosed tags %s" % (f, len(p.st), p.st[:6]))
    ck(p.stray==0, "%s: %d stray end tags" % (f, p.stray))

# 2. five-tab nav, exactly one active
for f in PAGES:
    nav = re.search(r'<nav class="tabs">(.*?)</nav>', S[f], re.S)
    ck(nav is not None, "%s: no nav" % f)
    if nav:
        body = nav.group(1)
        for href in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]:
            ck(('href="%s"' % href) in body, "%s: nav missing %s" % (f, href))
        ck(body.count('class="on"')==1, "%s: active tab count %d" % (f, body.count('class="on"')))

# 3. stamp ids + freshline
for f in PAGES:
    for i in ["edition","datestamp","updated","freshline"]:
        ck(('id="%s"' % i) in S[f], "%s: missing id %s" % (f, i))
    ck("America/New_York" in S[f], "%s: missing stamp JS" % f)

# 4. tldr on briefings only, correct labels
LAB = {"cyber-briefing.html":"The Wire","wallstreet-briefing.html":"The Tape","mma-briefing.html":"Tale of the Tape"}
for f in BRIEFS:
    ck(S[f].count('class="tldr"')==1, "%s: tldr count %d" % (f, S[f].count('class="tldr"')))
    ck('<b>%s</b>' % LAB[f] in S[f], "%s: wrong tldr label" % f)
ck('class="tldr"' not in S["index.html"], "index.html: has a .tldr (should not)")

# 5. index cards each contain their page's tldr sentence verbatim
for f in BRIEFS:
    t = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', S[f], re.S)
    ck(t is not None, "%s: cannot parse tldr" % f)
    if t: ck(t.group(1) in S["index.html"], "index.html: missing verbatim tldr of %s" % f)

# 6. TradingView widget JSON blocks all parse
blocks = re.findall(r'embed-widget-[a-z\-]+\.js" async>(\{.*?\})</script>', S["wallstreet-briefing.html"], re.S)
ck(len(blocks)==8, "WS: expected 8 widget blocks, found %d" % len(blocks))
for b in blocks:
    try: json.loads(b)
    except Exception as e: fails.append("WS: widget JSON parse error %s" % e)
    checks[0]+=1

# 7. ticker keeps the mandated symbols
tick = [b for b in blocks if '"symbols"' in b][0]
for sym in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    ck(sym in tick, "WS ticker missing %s" % sym)

# 8. Chart of the Day == AAOI, SNDK absent as a widget symbol
ck('"symbol":"NASDAQ:AAOI"' in S["wallstreet-briefing.html"], "WS: Chart of the Day is not NASDAQ:AAOI")
ck('"symbol":"NASDAQ:SNDK"' not in S["wallstreet-briefing.html"], "WS: NASDAQ:SNDK still a widget symbol")

# 9. KEV countdowns: 12 rows, 8 past due / 1 due today / 3 ahead
kev = re.findall(r'<span class="kevdue[^"]*">([^<]+)</span>', S["cyber-briefing.html"])
ck(len(kev)==12, "CY: KEV countdown count %d (want 12)" % len(kev))
past = len([k for k in kev if "PAST DUE" in k])
today = len([k for k in kev if "DUE TODAY" in k])
ahead = len(kev) - past - today
ck(past==8, "CY: past-due count %d (want 8)" % past)
ck(today==1, "CY: due-today count %d (want 1)" % today)
ck(ahead==3, "CY: ahead count %d (want 3)" % ahead)

# 10. Zimbra deadline consistent across Patch Priority and KEV board
c = S["cyber-briefing.html"]
ck(c.count("CVE-2026-73570")>=3, "CY: Zimbra CVE referenced %d times" % c.count("CVE-2026-73570"))
ck("10.1.20" in c, "CY: missing Zimbra fixed version 10.1.20")
ck("August 21" in c and "August 24" in c, "CY: missing Zimbra add/due dates")
ck("8.9" in c, "CY: missing Zimbra CVSS 8.9")

# 11. champions board: 12 <tr>, 8 names asserted, 3 stale cells absent
m = S["mma-briefing.html"]
champ = m[m.find("Champions board"):]
champ = champ[:champ.find("</section>")]
ck(champ.count("<tr>")==12, "MMA: champions rows %d (want 12)" % champ.count("<tr>"))
for name in ["Aspinall","Ulberg","Strickland","Makhachev","Gaethje","Volkanovski","Yan","Shevchenko"]:
    ck(name in champ, "MMA: champions board missing %s" % name)
# the CHAMPION column only (2nd <td> of each row) — defeated opponents legitimately
# appear in the "Won the title" column, so scope the stale-name test to column 2.
col2 = re.findall(r'<tr><td>[^<]*</td><td>([^<]*)</td>', champ)
ck(len(col2)==11, "MMA: parsed %d champion cells (want 11)" % len(col2))
for stale in ["Pereira","Chimaev","Topuria"]:
    ck(not any(stale in x for x in col2), "MMA: stale name %s in a CHAMPION cell" % stale)
ck(not any("vacant" in x.lower() or not x.strip() for x in col2), "MMA: a division has an empty/vacant champion cell")
ck("Eleven belts, none vacant" in champ, "MMA: champions note does not assert 11 belts, none vacant")

# 12. cached / stale figure blacklist absent from editorial lead + movers
w = S["wallstreet-briefing.html"]
lead = w[w.find('<div class="lab">The lead</div>'):w.find('<div class="lab">Chart of the day')]
BLACK = ["7,652.36","53,441.18","25,971.85","53,506.48","26,090.11","7,645.21","53,391.49","25,935.17"]
for b in BLACK:
    ck(b not in lead, "WS lead: cached figure %s present" % b)
# Friday closes must NOT appear in the lead block (they belong in the Weekly Scorecard)
for b in ["7,674.37","53,277.01","26,180.46"]:
    ck(b not in lead, "WS lead: Friday close %s present in lead" % b)
    ck(b in w, "WS: Friday close %s missing from Weekly Scorecard" % b)

# 13. this run's fresh, sourced figures are present
for fig in ["0.07%","0.24%","0.63%","0.56%","917.23","802.10","436.19","8.62%","4.69%","4,671.09","79,716.00",
            "$600&nbsp;million","392%","1.55&nbsp;billion","5.187%","5.337%","4.651%","5.247%",
            "$100&nbsp;billion to $200&nbsp;billion","November&nbsp;4"]:
    ck(fig in w, "WS: fresh figure missing: %s" % fig)
for fig in ["CVE-2026-58231","10.0","Defused Cyber","KEVIntel","Onapsis","July 6 and July 10","August 12","August 21"]:
    ck(fig in c, "CY: fresh figure missing: %s" % fig)
for fig in ["Natália Silva","Shevchenko","ESPN Brasil","Payton Talbott","Ateba Gautier","UFC 307"]:
    ck(fig in m, "MMA: fresh item missing: %s" % fig)

# 14. New-tag accounting: WS 2, CY 2, MMA 0
nw = {f: S[f].count('class="tag new"') for f in BRIEFS}
ck(nw["wallstreet-briefing.html"]==2, "WS New tags %d (want 2)" % nw["wallstreet-briefing.html"])
ck(nw["cyber-briefing.html"]==2, "CY New tags %d (want 2)" % nw["cyber-briefing.html"])
ck(nw["mma-briefing.html"]==0, "MMA New tags %d (want 0)" % nw["mma-briefing.html"])
# last edition's New tags gone by exact markup
ck('<span class="tag down">SNDK −9%</span><span class="tag">Apple / CXMT / YMTC</span><span class="tag new">New</span>' not in w, "WS: old New tag (CXMT) still present")
ck('<span class="tag down">F, STLA −4%</span><span class="tag">Auto tariffs</span><span class="tag new">New</span>' not in w, "WS: old New tag (auto tariffs) still present")
ck('<span class="tag">4 &times; CVSS 9.8</span><span class="tag new">New</span>' not in c, "CY: old New tag (Apple cluster) still present")
# this edition's New tags present by exact markup
ck('<span class="tag down">MRNA −7%</span><span class="tag">Profit-taking</span><span class="tag new">New</span>' in w, "WS: Moderna New tag missing")
ck('<span class="tag down">Drones, quantum</span><span class="tag">Risk appetite</span><span class="tag new">New</span>' in w, "WS: speculative-complex New tag missing")
ck('<span class="tag crit">CVSS 10.0</span><span class="tag">SAP Commerce Cloud</span><span class="tag new">New</span>' in c, "CY: SAP New tag missing")
ck('<span class="tag">Social engineering</span><span class="tag new">New</span>' in c, "CY: Apollo New tag missing")

# 15. trap greps: no "2 p.m." on WS/CY (Bessent is 1 p.m. ET); no three-week KEV rule
for f in ["wallstreet-briefing.html","cyber-briefing.html"]:
    ck("2 p.m." not in S[f], "%s: contains '2 p.m.'" % f)
    ck("1 p.m. ET" in S[f], "%s: missing '1 p.m. ET'" % f)
ck("three-week" not in c or "not on a fixed three-week schedule" in c, "CY: unqualified three-week KEV rule")
ck("Beneil Dariush" not in m or "challenger" not in m[max(0,m.find("Beneil Dariush")-300):m.find("Beneil Dariush")+300], "MMA: Dariush mislabelled")
ck("Cody Salkilld" not in m, "MMA: wrong Salkilld first name")
ck("Abdul-Rakhman" not in m, "MMA: hyphenated Yakhyaev spelling")
ck("Shamil Yakhyaev" not in m, "MMA: wrong Yakhyaev first name")

# 16. no After-Hours SECTION (regular session under way). The phrase legitimately appears
# in the Weekly Scorecard note explaining its absence, so test for a section label.
ck('<div class="lab">After-hours movers' not in w.lower(), "WS: after-hours section present mid-session")
ck("No After-Hours Movers section appears in this edition" in w, "WS: missing the note explaining no after-hours block")

# 17. every page carries a Sources footer
for f in BRIEFS:
    ck('<div class="lab">Sources</div>' in S[f], "%s: no Sources footer" % f)

print("CHECKS: %d   FAILURES: %d" % (checks[0], len(fails)))
for x in fails: print("  FAIL: " + x)
sys.exit(1 if fails else 0)
