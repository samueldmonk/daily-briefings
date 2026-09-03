# -*- coding: utf-8 -*-
import re, sys, os, datetime
OUT="/sessions/nifty-sweet-cannon/mnt/outputs"
F={k:open(os.path.join(OUT,v)).read() for k,v in
   {"ix":"index.html","cy":"cyber-briefing.html","ws":"wallstreet-briefing.html","mma":"mma-briefing.html"}.items()}
ALL="\n".join(F.values())
raised=[]; n=0
def ck(cond,msg):
    global n; n+=1
    if not cond: raised.append(msg)

# ---- structural ----
for k,v in F.items():
    ck('id="edition"' in v, f"{k}: edition pill")
    ck('id="datestamp"' in v, f"{k}: datestamp pill")
    ck('id="updated"' in v, f"{k}: updated pill")
    ck('id="freshline"' in v, f"{k}: freshline")
    ck(v.count('nav class="tabs"')==1, f"{k}: one nav")
    for href in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]:
        ck(href in v, f"{k}: nav link {href}")
    ck("America/New_York" in v, f"{k}: stamp js")
    ck(v.strip().endswith("</html>"), f"{k}: closes html")
for k,act in [("ix",'<a href="index.html" class="on">'),("cy",'<a href="cyber-briefing.html" class="on">'),
              ("ws",'<a href="wallstreet-briefing.html" class="on">'),("mma",'<a href="mma-briefing.html" class="on">')]:
    ck(act in F[k], f"{k}: active tab")
for k,lbl in [("cy","The Wire"),("ws","The Tape"),("mma","Tale of the Tape")]:
    ck(f'<div class="tldr"><b>{lbl}</b>' in F[k], f"{k}: tldr label {lbl}")
ck('class="tldr"' not in F["ix"], "index: no tldr strip (uses cards)")

# ---- widgets (ws): 1 tape + 3 single-quote + 4 panels = 8 ----
ck(F["ws"].count("s3.tradingview.com")==8, "ws: 8 tradingview widgets, got %d"%F["ws"].count("s3.tradingview.com"))
for w in ["ticker-tape","single-quote","timeline","stock-heatmap","mini-symbol-overview","events"]:
    ck(w in F["ws"], f"ws: widget {w}")
ck('"symbol":"NYSE:CHPT"' in F["ws"], "ws: chart of the day = CHPT")
ck("tradingview" not in F["ix"] and "tradingview" not in F["cy"] and "tradingview" not in F["mma"], "no widgets outside ws")

# ---- calendar integrity: every "Weekday, Month D" must match the real 2026 calendar ----
MON={m:i+1 for i,m in enumerate(["January","February","March","April","May","June","July","August",
     "September","October","November","December"])}
WD=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for wd,mo,dy in re.findall(r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})", ALL):
    real=WD[datetime.date(2026,MON[mo],int(dy)).weekday()]
    ck(real==wd, f"CALENDAR: '{wd}, {mo} {dy}' is actually a {real}")
for wd,mo,dy in re.findall(r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun),\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec)\s+(\d{1,2})", ALL):
    full=[m for m in MON if m.startswith(mo.rstrip("t") if mo=="Sept" else mo)][0]
    real=WD[datetime.date(2026,MON[full],int(dy)).weekday()][:3]
    ck(real==wd, f"CALENDAR(short): '{wd}, {mo} {dy}' is actually a {real}")

# ---- KEV consistency ----
ck("Saturday, September 5" in F["cy"], "cy: KEV Sept 5 with weekday")
ck("Wednesday, September 16" in F["cy"], "cy: KEV Sept 16 with weekday")
ck("2 days left" in F["cy"] and "13 days left" in F["cy"], "cy: countdowns 2/13")
ck(F["cy"].index("2 days left") < F["cy"].index("13 days left"), "cy: countdowns chronological")
ck("BOD 26-04" in F["cy"] and "BOD 22-01" not in F["cy"], "cy: BOD 26-04 not 22-01")
ck("September 14" not in F["cy"], "cy: no unsourced Sept 14 deadline")
# tranche arithmetic: 2 SonicWall + 3 others = 5 of 7
ck("three others" in F["cy"], "cy: Sept 5 tranche = 2 SonicWall + three others")
ck("three other flaws" in F["cy"] and "three other flaws" in F["ix"], "cy/ix: 'three other flaws' matches")
ck("four other" not in ALL, "no 'four other flaws'")
for c in ["CVE-2026-83548","CVE-2026-83549","CVE-2026-9586","CVE-2026-82329","CVE-2026-49869","CVE-2026-48710","CVE-2026-59822"]:
    ck(c in F["cy"], f"cy: KEV cve {c}")
ck("7</div>" in F["cy"], "cy: by-the-numbers 7 CVEs")

# ---- champions board: standing record ----
CH={"Tom Aspinall":"Heavyweight","Ciryl Gane":"interim","Carlos Ulberg":"LHW","Sean Strickland":"MW",
    "Islam Makhachev":"WW","Justin Gaethje":"LW","Alexander Volkanovski":"FW","Petr Yan":"BW",
    "Joshua Van":"FLW","Valentina Shevchenko":"WFLW","Kayla Harrison":"WBW","Mackenzie Dern":"WSW"}
board=F["mma"][F["mma"].index("Champions Board"):]
for name in CH: ck(name in board, f"mma: champion {name} on board")
ck("<td>Light Heavyweight</td><td>Carlos Ulberg</td>" in board, "mma: LHW cell = Ulberg")
ck("<td>Middleweight</td><td>Sean Strickland</td>" in board, "mma: MW cell = Strickland")
ck("<td>Lightweight</td><td>Justin Gaethje</td>" in board, "mma: LW cell = Gaethje")
ck("<td>Featherweight</td><td>Alexander Volkanovski</td>" in board, "mma: FW cell = Volkanovski")
rows=re.findall(r"<tr><td>[^<]*</td><td>([^<]+)</td>", board)
for bad in ["Alex Pereira","Khamzat Chimaev","Ilia Topuria"]:
    ck(bad not in rows, f"mma: {bad} must NOT be a champion cell")
ck("Featherweight</td><td>Vacant" not in board and "featherweight is vacant" not in F["mma"].lower(), "mma: FW not vacant")

# ---- Parnasse provenance (both directions) ----
seg=F["mma"]
i=seg.find("Parnasse")
ck("Contender Series" not in seg[max(0,seg.index("On Salahdine Parnasse")):seg.index("On Salahdine Parnasse")+700]
   or "not a Contender Series signee" in seg, "mma: Parnasse not attributed to Contender Series")
ck("two-time KSW featherweight" in seg, "mma: Parnasse KSW provenance")
ck("Saladhine" not in ALL, "spelling: Salahdine not Saladhine")
ck("Tsarukyan vs. Ruffy" in seg and "Rebecki" not in ALL, "mma: co-main surnames only, no invented names")

# ---- MMA results table: no placeholder opponents ----
res=seg[seg.index("Last Event"):seg.index("Prospect Watch")]
ck("not named" not in res and "TBD" not in res, "mma: no placeholder in results table")
ck("Aoriqileng" in res, "mma: Asakura opponent named")
ck(res.count("<tr>")==7, "mma: 6 result rows + header, got %d"%res.count("<tr>"))
ck("Levi Rodrigues Jr." in res, "mma: Rodrigues named")
# Asakura must NOT be paired with Rodrigues (refused aggregation)
ck("Kai Asakura</td><td>def. Levi" not in res, "mma: refuse Asakura-vs-Rodrigues conflation")

# ---- markets arithmetic consistency: level = prior + change ----
def close_ok(lvl, chg, prior):
    return abs((lvl-chg)-prior) < 0.02
ck(close_ok(53686.11, 624.16, 53061.95), "ws: Dow close reconciles to Wed close")
ck(abs(7747.71/7666.60-1.0106)<0.0002, "ws: S&P +1.06% reconciles")
ck(abs(26584.06/26217.83-1.014)<0.0005, "ws: Nasdaq +1.4% reconciles")
ck(close_ok(53061.95,295.07,52766.88), "ws: Wed Dow reconciles")
ck(close_ok(26217.83,118.05,26099.78), "ws: Wed Nasdaq reconciles")
ck(close_ok(355.96,-11.28,367.24), "ws: Broadcom quote reconciles")
ck(close_ok(382.09,25.08,357.01), "ws: Tesla quote reconciles")
ck("7,747.71" in F["ws"] and "53,686.11" in F["ws"] and "26,584.06" in F["ws"], "ws: official Thu closes printed")
ck("No official Thursday closing print" not in F["ws"], "ws: stale no-close language removed")
ck("7,748.36" not in F["ws"] and "53,695.80" not in F["ws"], "ws: superseded intraday panel figures dropped")
ck("Weekly Scorecard" in F["ws"] and "Thu, Sept 3" in F["ws"], "ws: scorecard has Thursday")
ck("After-Hours Movers" in F["ws"], "ws: after-hours section present post-close")
ck("Wednesday" not in F["ws"][F["ws"].index("Movers &amp; Drivers"):F["ws"].index("Chart of the Day")].replace("Wednesday's $367.24 close","").replace("Wednesday's report",""), "ws: no unlabelled Wednesday figures in movers")

# ---- refused / excluded items ----
for bad,why in [("Pennsylvania Attorney General","standing exclusion"),("INC Ransom","standing exclusion"),
                ("IDMerit","standing exclusion"),("Tilly","unpinnable session"),
                ("Principal Financial","standing exclusion")]:
    ck(bad not in ALL, f"excluded: {bad} ({why})")
ck("31.8%" not in ALL, "excluded: unpinnable ChargePoint 31.8% figure")

# ---- desk jargon scan ----
JARG=["this run","fetched this run","in the sources fetched","from the same fetch","an aggregated return",
      "carried from this desk","carried from the verified record","in an earlier fetch","a fresh fetch",
      "Not re-sourced","returned this run","previous edition","prior snapshot","the guards","read-through"]
for j in JARG: ck(j.lower() not in ALL.lower(), f"jargon: '{j}'")

# ---- disclaimers ----
ck("not investment advice" in F["ws"] or "Nothing here is investment advice" in F["ws"], "ws: disclaimer")
ck("subject to change" in F["mma"], "mma: disclaimer")
ck("vendor advisories" in F["cy"], "cy: disclaimer")
for k in ["cy","ws","mma"]:
    ck("<footer>" in F[k] and "Sources" in F[k], f"{k}: sources footer")
    ck(F[k].count("<li>")>=6, f"{k}: >=6 sources")

# ---- summary strips faithful to leads ----
ck("best day" in F["ws"] and "624" in F["ws"], "ws: summary matches lead (best day / 624)")
ck("Falcon" in F["cy"] and "two days" in F["cy"], "cy: summary matches lead")
ck("UFC 332" in F["mma"] and "Shevchenko" in F["mma"], "mma: summary matches lead")
# index cards must match page summaries verbatim
for k,f in [("cy",F["cy"]),("ws",F["ws"]),("mma",F["mma"])]:
    m=re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', f, re.S)
    ck(m is not None, f"{k}: tldr parse")
    if m: ck(m.group(1).strip() in F["ix"], f"index card matches {k} summary verbatim")

print("checks:", n, "raised:", len(raised))
for r in raised: print("  !!", r)

# ===== guards added from this edition's read-through =====
F2={k:open(os.path.join(OUT,v)).read() for k,v in
   {"ix":"index.html","cy":"cyber-briefing.html","ws":"wallstreet-briefing.html","mma":"mma-briefing.html"}.items()}
r2=[]; m=0
def ck2(c,msg):
    global m; m+=1
    if not c: r2.append(msg)
# 1 glyph
ck2("&#9960; Security" in F2["ix"] and "&#9880;" not in F2["ix"], "index: shield glyph U+26E8, not U+2698")
# 2 New-tag comparator vs the prior snapshot
import re as _re
PREV={"ws":open("/tmp/db_1788465063/archive/wallstreet-2026-09-03-1547.html").read(),
      "cy":open("/tmp/db_1788465063/archive/cyber-2026-09-03-1547.html").read(),
      "mma":open("/tmp/db_1788465063/archive/mma-2026-09-03-1547.html").read()}
for k in PREV:
    for blk in F2[k].split('<div class="card"')[1:]:
        blk=blk[:blk.find('</p>')]
        if 't new">New' not in blk: continue
        t=_re.sub(r'<[^>]+>','',(_re.search(r'<h3>(.*?)</h3>',blk,_re.S) or _re.match('','')).group(1))
        for tok in [w for w in _re.findall(r"[A-Z][A-Za-z’'\-]{4,}",t)
                    if w not in ("Series","Contender","Every")]:
            ck2(tok not in PREV[k], f"{k}: New tag on '{t[:40]}' but '{tok}' was on the 1547 page")
for k,names in [("ws",["Broadcom falls","Robinhood rises","Megacaps and crypto"]),
                ("mma",["Bilal Hasan, 25","Liu Ce &mdash; a debut"])]:
    for nm in names:
        i=F2[k].index("<h3>"+nm); s=F2[k].rfind('<div class="card"',0,i)
        ck2('t new">New' not in F2[k][s:i], f"{k}: '{nm}' must NOT carry a New tag")
# 3 unsupported framing
ck2("second day of AI-demand" not in F2["ws"], "ws: Snowflake 'second day' framing was unsupported")
ck2("Snowflake soars on a blowout quarter" in F2["ws"], "ws: Snowflake retitled")
# 4 champions board provenance
ck2("taken from the individual event result" in F2["mma"], "mma: board provenance stated")
ck2("Freedom 250 on June 14, 2026" in F2["mma"], "mma: supersession dates kept")
# 5 post-close integrity
ck2("last traded around <strong>4.75%</strong> after the remarks" in F2["ws"], "ws: yield reading time-anchored")
ck2("Thu, Sept 3" in F2["ws"] and F2["ws"].index("Thu, Sept 3")<F2["ws"].index("Wed, Sept 2"), "ws: Thursday rows first")
# 6 no source-omission claims written from memory
for bad in ["is not on that listing","does not appear on ESPN","ESPN does not list"]:
    ck2(bad not in "\n".join(F2.values()), f"no source-omission claim: '{bad}'")
print("added checks:", m, "raised:", len(r2))
for x in r2: print("  !!", x)
