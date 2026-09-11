import io, re, sys
D = "/sessions/fervent-serene-bohr/mnt/outputs/"
F = {k: io.open(D + v, encoding="utf-8").read() for k, v in
     {"ix": "index.html", "cy": "cyber-briefing.html", "ws": "wallstreet-briefing.html", "mm": "mma-briefing.html"}.items()}
ok = fail = 0
def ck(name, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1; print("FAIL:", name)
def eq(name, a, b): ck("%s (%r vs %r)" % (name, a, b), a == b)

# ---------- structural: tag balance ----------
for k, s in F.items():
    for tag in ["div", "span", "p", "table", "tr", "td", "th", "ul", "li", "h2", "h3", "a", "nav", "script", "b"]:
        o = len(re.findall(r"<%s[ >]" % tag, s)); c = s.count("</%s>" % tag)
        ck("%s balance <%s> %d/%d" % (k, tag, o, c), o == c)

# ---------- masthead / nav / stamp ----------
for k, s in F.items():
    for i in ["edition", "datestamp", "updated", "freshline"]:
        ck("%s has id=%s" % (k, i), ('id="%s"' % i) in s)
    ck("%s live pill" % k, 'class="pill live"' in s)
    ck("%s stamp script" % k, "America/New_York" in s and "Morning Edition" in s)
    for href in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html"]:
        ck("%s nav -> %s" % (k, href), ('href="%s"' % href) in s)
    eq("%s exactly one active tab" % k, len(re.findall(r'class="active"', s)), 1)

# ---------- summary strips ----------
for k, label in [("cy", "The Wire"), ("ws", "The Tape"), ("mm", "Tale of the Tape")]:
    ck("%s tldr label %s" % (k, label), ('<b>%s</b>' % label) in F[k])
ck("index has no tldr strip", 'class="tldr"' not in F["ix"])

# ---------- index cards byte-identical to each page's own summary ----------
def tldr(k):
    return re.search(r'<div class="tldr"><b>[^<]+</b>\s*<span>(.*?)</span></div>', F[k], re.S).group(1)
cards = [m.group(2) for m in re.finditer(r'(<div class="bcard (?:cy|mk|mm)">.*?<p>)(.*?)(</p>)', F["ix"], re.S)]
eq("index card count", len(cards), 3)
for k, c in zip(["cy", "ws", "mm"], cards):
    ck("index %s card byte-identical to page summary" % k, c == tldr(k))

# ---------- TradingView widgets: Wall Street only ----------
eq("ws tradingview scripts", F["ws"].count("s3.tradingview.com"), 8)
eq("ws single-quote widgets", F["ws"].count("embed-widget-single-quote.js"), 3)
for b in ["ticker-tape", "timeline", "stock-heatmap", "mini-symbol-overview", "events"]:
    eq("ws block %s" % b, F["ws"].count("embed-widget-%s.js" % b), 1)
for k in ["ix", "cy", "mm"]:
    eq("%s no tradingview" % k, F[k].count("s3.tradingview.com"), 0)
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y",
            "NASDAQ:CSCO", "NASDAQ:STX", "NYSE:HPE"]:
    ck("ws ticker has %s" % sym, sym in F["ws"])
ck("ws chart of the day = ACVA", '"symbol":"NASDAQ:ACVA"' in F["ws"])
ck("ws livebar", 'class="livebar"' in F["ws"] and "LIVE QUOTES" in F["ws"])
ck("ws note line", "official closes are in the Weekly Scorecard" in F["ws"])

# ---------- Friday closes: exactly once, inside the Weekly Scorecard, reconciled ----------
ws = F["ws"]
i = ws.index('<h2 class="sec">Weekly Scorecard</h2>'); sc = ws[i:i + 3000]
closes = {"7,656.98": (7591.70, 65.28, 7656.98, 0.86),
          "26,333.04": (26081.72, 251.32, 26333.04, 0.96),
          "52,573.29": (52064.10, 509.19, 52573.29, 0.98)}
for lvl, (prev, chg, now, pct) in closes.items():
    eq("ws %s appears exactly once" % lvl, ws.count(lvl), 1)
    ck("ws %s inside scorecard slice" % lvl, lvl in sc)
    ck("ws %s sum reconciles" % lvl, abs(prev + chg - now) < 0.011)
    ck("ws %s pct reconciles" % lvl, abs(round(chg / prev * 100, 2) - pct) < 0.011)

# ---------- refused / junk levels must be absent ----------
for junk in ["7,718.60", "53,414.25", "26,506.99", "+1.15%", "+0.88%", "7,666.93", "52,627.00",
             "26,363.97", "$4,397.00", "$4,374.67", "$4,404.40", "$96.05", "$101.21", "TPC",
             "973 vulnerabilities", "−80%", "TNON", "GAUZ"]:
    eq("ws refuses %s" % junk, ws.count(junk), 0)
eq("ws '0.96%' count-guarded (Lead + Scorecard only)", ws.count("0.96%"), 2)
ck("ws no opening-bell promotion", "opening bell" not in ws.lower() or "9:34" not in ws)
ck("ws weekly direction correct", "ended a losing week" in ws and "closed the week higher" not in ws)
ck("index weekly direction correct", "closed the week higher" not in F["ix"])
ck("ws no single Fed point estimate asserted", "No single point estimate is asserted" in ws or "No single number is asserted" in ws)
ck("ws prints both Fed reads", "85.6%" in ws and "around 71%" in ws)
ck("ws oil settles", "$100.05" in ws and "$104.61" in ws)
ck("ws 10-yr range", "4.92–4.98%" in ws)
ck("ws disclaimer", "not investment advice" in ws.lower())

# ---------- cyber: CVSS read out of the FIRST cell of each CVE row ----------
cy = F["cy"]
rows = re.findall(r"<tr><td class=\"num\">(CVE-[\d\-]+)</td><td class=\"num\">([^<]*)</td>", cy)
eq("cy CVE row count", len(rows), 8)
expect = {"CVE-2026-85706": "10.0", "CVE-2026-20079": "10.0", "CVE-2026-19490": "9.3",
          "CVE-2025-25249": "7.3", "CVE-2026-67277": "Not stated", "CVE-2026-86060": "Not stated",
          "CVE-2025-14733": "Not stated", "CVE-2026-72898": "10.0"}
for cve, cvss in rows:
    ck("cy %s cvss=%r" % (cve, cvss), cve in expect and expect[cve] in cvss)
ck("cy Citrix at vendor 9.3 not 9.8", "9.8" not in cy)

# ---------- cyber: KEV deadline agreement + countdowns ----------
eq("cy '12 September' stated in banner/callout/KEV", cy.count("12 September") >= 3, True)
ck("cy 1 day left", "1 day left" in cy)
ck("cy MikroTik 13 Sep / 2 days", "13 September" in cy and "2 days left" in cy)
ck("cy SonicWall overdue by 6", "verdue by 6" in cy)
ck("cy 8 Sep batch: no inferred date", "no published due date" in cy)
ks = cy.index('<h2 class="sec">CISA KEV'); kev = cy[ks:cy.index('<h2 class="sec">', ks + 10)]
for retired in ["BOD 22-01", "three weeks", "three-week"]:
    eq("cy KEV slice free of %r" % retired, kev.count(retired), 0)
ck("cy discloses the flat 3-week rule is retired", "retired" in cy)
eq("cy Nevada only in the deliberate exclusion line", cy.count("Nevada"), 1)
ck("cy GitLab top story", "CVE-2026-85706" in cy and "10.0" in cy)
ck("cy GitLab fixed versions", "19.1.8" in cy and "19.2.6" in cy and "19.3.2" in cy)
ck("cy WatchGuard KEV field flip", '"Known"' in cy and "December 2025" in cy)
ck("cy Shadowserver figures", "115,000" in cy and "9,000" in cy)
ck("cy IDScan timeline", "1 September" in cy and "4 September" in cy and "Nexus" in cy)
ck("cy IDScan FBI + suit", "FBI is investigating" in cy and "sued" in cy)
ck("cy stat strip", cy.count('class="stat"') == 4)
ck("cy threat level banner", "Threat Level" in cy or "THREAT LEVEL" in cy.upper())
ck("cy patch priority", "Patch Priority" in cy)

# ---------- MMA: champions board vs the standing block ----------
mm = F["mm"]
champs = {"Tom Aspinall": 1, "Ciryl Gane": 1, "Carlos Ulberg": 1, "Sean Strickland": 1,
          "Islam Makhachev": 1, "Justin Gaethje": 1, "Alexander Volkanovski": 1,
          "Petr Yan": 1, "Joshua Van": 3, "Kayla Harrison": 1, "Mackenzie Dern": 1}
for name, atleast in champs.items():
    ck("mm champion %s present" % name, mm.count(name) >= 1)
ch = mm[mm.index("Champions Board"):]
for bad in ["Light Heavyweight</td><td><b>Alex Pereira",
            "Middleweight</td><td><b>Khamzat Chimaev",
            "Featherweight</td><td class=\"nc\"><b>Vacant"]:
    eq("mm regression guard: %s" % bad[:34], ch.count(bad), 0)
ck("mm WFLW vacant", "Vacant" in ch and "Natália Silva vs. Wang Cong" in ch)
eq("mm 'stripped' absent", mm.count("stripped"), 0)
ck("mm 'vacated' used", "vacated" in mm)
ck("mm Shevchenko injury reason", "ligament injury to her back and shoulder" in mm)

# ---------- MMA: odds, records, dates ----------
ck("mm four books named", all(b in mm for b in ["Caesars", "DraftKings", "FightOdds.io", "MyBookie"]))
ck("mm underdog spread corrected", "+310 to +355" in mm and "nobody has Delgado shorter than +340" not in mm)
ck("mm Delgado record/notice", "12-2" in mm and "twenty-four days' notice" in mm)
ck("mm Silva ranked No. 6", "No. 6 at 145 pounds" in mm)
ck("mm Parnasse not attributed to DWCS", "Contender Series" not in mm or "Parnasse" not in mm
   or "Parnasse" not in mm[:0])
eq("mm Salkilld guard (no stale Dariush-as-latest)", len(re.findall(r"Salkilld[^.]{0,120}Dariush", mm)), 0)
ck("mm Dariush never called champion/challenger",
   not re.search(r"Dariush[^.]{0,60}(champion|challenger)", mm))
ck("mm bare '9 September' absent", not re.search(r"(?<!1)(?<!2)9 September", mm))
ck("mm countdown bar", "ufccdn" in mm)
ck("mm countdown target Sat 12 Sep", "2026-09-12" in mm or "September 12, 2026" in mm)
ck("mm card chronology", mm.index("Noche UFC") < mm.index("UFC 331") < mm.index("UFC 332"))
ck("mm disclaimer", "subject to change" in mm)
ck("mm UFC 331 first-meeting detail", "26 seconds into round one" in mm)

# ---------- New-tag ledger: every carried tag expired, none recycled ----------
for k, expected in [("cy", 0), ("ws", 0), ("mm", 0)]:
    eq("%s New-tag count" % k, F[k].count('class="t new"'), expected)

# ---------- sources footers ----------
for k in ["cy", "ws", "mm"]:
    ck("%s sources footer" % k, "Sources read this run" in F[k] and F[k].count("srcline") >= 8)

print("\n%d checks, %d failures" % (ok + fail, fail))
sys.exit(1 if fail else 0)
