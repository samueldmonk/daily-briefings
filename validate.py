#!/usr/bin/env python3
import re, os
OUT="/sessions/nice-ecstatic-thompson/mnt/outputs"
P={f:open(os.path.join(OUT,f)).read() for f in
   ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]}
fails=[]; n=0
def ck(cond,msg):
    global n; n+=1
    if not cond: fails.append(msg)

for f,h in P.items():
    for tab in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]:
        ck('href="%s"'%tab in h, "%s: missing nav tab %s"%(f,tab))
    for pid in ["edition","datestamp","updated","freshline"]:
        ck('id="%s"'%pid in h, "%s: missing #%s"%(f,pid))
    ck("Intl.DateTimeFormat" in h and "Morning Edition" in h, "%s: missing self-stamp JS"%f)
    ck(h.count("<div")==h.count("</div>"), "%s: unbalanced divs %d/%d"%(f,h.count("<div"),h.count("</div>")))
    ck('class="pill live"' in h, "%s: missing LIVE pill"%f)
    ck(h.count("<table>")==h.count("</table>"), "%s: unbalanced tables"%f)
    ck("<html" in h and "</html>" in h, "%s: html tags"%f)

# tldr labels
ck('<b>The Wire</b>' in P["cyber-briefing.html"], "cyber: tldr label")
ck('<b>The Tape</b>' in P["wallstreet-briefing.html"], "ws: tldr label")
ck('<b>Tale of the Tape</b>' in P["mma-briefing.html"], "mma: tldr label")
for f in ["cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]:
    ck('class="tldr"' in P[f], "%s: missing tldr strip"%f)
ck('class="tldr"' not in P["index.html"], "index: should use cards not tldr")

# active tabs
ck('<a href="cyber-briefing.html" class="on">' in P["cyber-briefing.html"], "cyber: active tab")
ck('<a href="wallstreet-briefing.html" class="on">' in P["wallstreet-briefing.html"], "ws: active tab")
ck('<a href="mma-briefing.html" class="on">' in P["mma-briefing.html"], "mma: active tab")
ck('<a href="index.html" class="on">' in P["index.html"], "index: active tab")

# TradingView blocks on WS
w=P["wallstreet-briefing.html"]
for widget in ["ticker-tape","single-quote","timeline","stock-heatmap","mini-symbol-overview","events"]:
    ck("embed-widget-%s.js"%widget in w, "ws: missing widget %s"%widget)
ck(w.count("embed-widget-single-quote.js")==3, "ws: single-quote count %d"%w.count("embed-widget-single-quote.js"))
for sym in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    ck(sym in w, "ws: tape missing %s"%sym)
ck('class="livebar"' in w and "LIVE QUOTES" in w, "ws: livebar")
ck("Quotes stream live" in w, "ws: note line")
for other in ["index.html","cyber-briefing.html","mma-briefing.html"]:
    ck("tradingview.com" not in P[other], "%s: should have no live widgets"%other)

# MMA countdown
m=P["mma-briefing.html"]
ck('id="ufccdn"' in m and "Fight week — live/completed" in m, "mma: countdown")

# champions regressions
ch=m[m.find("Champions Board"):]
ck("Carlos Ulberg" in ch and "Light Heavyweight</td><td><b>Carlos Ulberg" in ch.replace("\n",""), "mma: LHW must be Ulberg")
ck(not re.search(r"Light Heavyweight</td><td><b>Alex Pereira", ch), "mma: Pereira must not be LHW champ")
ck("Middleweight</td><td><b>Sean Strickland" in ch, "mma: MW must be Strickland")
ck(not re.search(r"Middleweight</td><td><b>Khamzat", ch), "mma: Chimaev must not be MW champ")
ck("Featherweight</td><td><b>Alexander Volkanovski" in ch, "mma: FW must be Volkanovski")
# HARNESS FIX: "vacant" is legitimate in a historical note ("won the VACANT belt").
# Only the champion CELL may never say vacant.
champ_cells = re.findall(r"<tr><td>[^<]+</td><td>(.*?)</td>", ch)
ck(len(champ_cells) == 11, "mma: champion cells parsed %d" % len(champ_cells))
ck(all("vacant" not in x.lower() for x in champ_cells), "mma: a champion cell says vacant")
ck("Lightweight</td><td><b>Justin Gaethje" in ch, "mma: LW must be Gaethje")
ck("Ciryl Gane" in ch, "mma: interim HW Gane")
ck(ch.count("<tr><td>")==11, "mma: champions rows %d"%ch.count("<tr><td>"))

# trap greps
traps=["Cody Salkilld","Shamil Yakhyaev","Abdul-Rakhman","Fight Night 286","7,677.24 / 53,577.40 / 26,151.30 is the close"]
for f,h in P.items():
    for t in traps[:4]:
        ck(t not in h, "%s: trap string present: %s"%(f,t))
# rejected close set must appear only inside the rejection note
ck("7,677.24" in w and "mislabelled" in w, "ws: rejected set must be framed as rejected")
ck("7,675.70" in w, "ws: verified S&P close missing")

# cyber checks
c=P["cyber-briefing.html"]
ck("CVE-2026-21962" in c and "10.0" in c, "cyber: top CVE")
ck('class="callout crit"' in c, "cyber: patch priority crit border")
ck(c.count("August 27")>=2, "cyber: deadline date")
ck("kev1" in c and "kev2" in c and "kev3" in c, "cyber: kev countdowns")
ck("Threat level · High" in c, "cyber: threat banner")
ck(c.count('class="stat"')==4, "cyber: stat strip count")
# patch priority must match KEV nearest deadline
ck("due today, August 27" in c, "cyber: patch priority deadline wording")

# index cards match page leads
i=P["index.html"]
ck("CVE-2026-21962" in i, "index: cyber card lead")
ck("Nvidia" in i and "96.2" in i, "index: markets card lead")
ck("Nurmagomedov" in i and "Song" in i, "index: mma card lead")
for cls in ["c-cy","c-ws","c-mm"]:
    ck('class="card %s"'%cls in i, "index: card %s"%cls)
ck(i.count("Read the briefing →")==3, "index: three read links")

# no invented CVEs outside the verified list
verified={"CVE-2026-21962","CVE-2026-12569","CVE-2026-69836","CVE-2026-68820","CVE-2026-62815",
          "CVE-2026-62893","CVE-2026-60004","CVE-2026-73570","CVE-2026-20349","CVE-2026-72898"}
found=set(re.findall(r"CVE-\d{4}-\d{4,6}", c))
ck(found<=verified, "cyber: unverified CVE ids %s"%(found-verified))

# sources footers
for f in ["cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]:
    ck("<footer>" in P[f] and P[f].count("<a href=\"http")>=10, "%s: sources footer thin"%f)
    ck('class="disc"' in P[f], "%s: disclaimer"%f)
# HARNESS FIX: the page's wording is "Nothing here is investment advice" — accept the real phrasing.
ck("investment advice" in w.lower() and "for information only" in w.lower(), "ws: investment disclaimer")
ck("subject to change" in m, "mma: cards disclaimer")

print("checks:", n, "failures:", len(fails))
for x in fails: print("  FAIL:", x)
