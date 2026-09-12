import io, re, datetime
D = "/sessions/lucid-funny-planck/mnt/outputs/"
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
raw = {p: io.open(D + p, encoding="utf-8").read() for p in PAGES}
# rendered body = file with <script> blocks stripped (the "0 days left" trap, 4 prior recurrences)
body = {p: re.sub(r"<script.*?</script>", "", raw[p], flags=re.S) for p in PAGES}
ok = fail = 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1; print("FAIL:", label)

# ---------- structural ----------
for p in PAGES:
    r = raw[p]
    chk(p + " doctype", r.startswith("<!DOCTYPE html>"))
    chk(p + " tail", r.rstrip().endswith("</html>"))
    for t in ["div", "span", "p", "h2", "h3", "table", "tr", "td", "th", "ul", "li", "a", "footer"]:
        chk("%s <%s> balance" % (p, t),
            len(re.findall(r"<%s[ >]" % t, r)) == len(re.findall(r"</%s>" % t, r)))
    for i in ["edition", "datestamp", "updated", "freshline"]:
        chk("%s id=%s" % (p, i), r.count('id="%s"' % i) == 1)
    chk(p + " ET timezone refs", r.count("America/New_York") >= 3)
    # five-tab nav, exactly one active, matching own filename
    nav = re.search(r"<nav>.*?</nav>", r, re.S).group(0)
    chk(p + " nav 5 tabs", len(re.findall(r"<a ", nav)) == 5)
    act = re.findall(r'<a class="on" href="([^"]+)"', nav)
    chk(p + " nav one active = self", act == [p])
    for tab in PAGES + ["archive.html"]:
        chk("%s nav links %s" % (p, tab), ('href="%s"' % tab) in nav)

# ---------- TradingView: Wall Street only ----------
for p in PAGES:
    c = raw[p].count("s3.tradingview.com")
    chk(p + " tradingview count", c == 8 if p == "wallstreet-briefing.html" else c == 0)
ws = raw["wallstreet-briefing.html"]
chk("ws single-quote widgets = 3", ws.count("embed-widget-single-quote.js") == 3)
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    chk("ws symbol " + sym, sym in ws)
chk("ws chart-of-day = HPE", '"symbol":"NYSE:HPE"' in ws)
for w in ["ticker-tape", "timeline", "stock-heatmap", "mini-symbol-overview", "events"]:
    chk("ws widget " + w, ("embed-widget-%s.js" % w) in ws)

# ---------- index levels: exactly once, inside the Scorecard, reconciled ----------
wsb = body["wallstreet-briefing.html"]
sc = wsb[wsb.index("Weekly Scorecard"):wsb.index("Rates, Bonds")]
# 7,656.98 legitimately occurs twice: once in the Scorecard, once inside the 7,666
# refusal clause that names what it is refusing. Pin both, do not ban the second.
for lvl in ["26,333.04", "52,573.29"]:
    chk("level %s once on page" % lvl, wsb.count(lvl) == 1)
    chk("level %s inside scorecard" % lvl, lvl in sc)
chk("7,656.98 total = 2", wsb.count("7,656.98") == 2)
# Both occurrences fall inside the Scorecard SECTION - one in the table, one in the
# explanatory note beneath it. Split the section rather than the page.
sc_table = sc[sc.index("<table>"):sc.index("</table>")]
sc_note = sc[sc.index("</table>"):]
chk("7,656.98 once in the Scorecard TABLE", sc_table.count("7,656.98") == 1)
chk("7,656.98 once in the refusal note", sc_note.count("7,656.98") == 1)
chk("7,656.98 nowhere after the Scorecard", wsb[wsb.index("Rates, Bonds"):].count("7,656.98") == 0)
for lvl, pts, pct in [("7,656.98", 65.28, 0.86), ("26,333.04", 251.31, 0.96), ("52,573.29", 509.19, 0.98)]:
    close = float(lvl.replace(",", "")); implied = (pts / (close - pts)) * 100
    chk("reconcile %s (%.3f%% vs %.2f%%)" % (lvl, implied, pct), abs(implied - pct) < 0.03)
    chk("scorecard pts %s" % pts, ("+%s" % pts) in sc)
chk("7,666 refusal guard: appears only in refusal clause",
    wsb.count("7,666") == 1 and "not</b> published here" in wsb)

# ---------- markets: retired / disputed items named, not silently dropped ----------
chk("ws Thursday-FOMC retired clause", "Thursday 17 September" in wsb and "only to retire it" in wsb)
chk("ws FOMC published date", "Wednesday 16 September at 2 PM ET" in wsb)
chk("ws 4.396 retired explicitly", "4.396%" in wsb and "is <b>retired</b>" in wsb)
chk("ws 2-year published 4.63", "<td>4.63%</td>" in wsb)
chk("ws 30y 5.36 not presented as Friday", "5.36%" in wsb and "not</b> published as a Friday figure" in wsb)
chk("ws Gauzy named but refused", "Gauzy" in wsb and "not published as a price move" in wsb)
chk("ws hike odds both printed", "71%" in wsb and "90%" in wsb)
chk("ws oil settles", "$104.61" in wsb and "$100.05" in wsb)
chk("ws weekly oil", "8.7%" in wsb and "9.4%" in wsb)
chk("ws sector line retired", "retired" in wsb and "nine of eleven" in wsb)
chk("ws carried labelled", wsb.count("carried") + wsb.count("Carried") >= 3)
# negation-tolerant disclaimer check (recurred twice before)
chk("ws not-investment-advice", re.search(r"(not investment advice|Nothing here is investment advice)", wsb) is not None)

# ---------- cyber ----------
cy = body["cyber-briefing.html"]
rows = re.findall(r"<tr><td><b>CVE-", cy)
chk("cyber CVE rows = 14", len(rows) == 14)
chk("cyber two CVSS 10.0 cells", cy.count('class="critc">10.0<') == 2)
chk("cyber two 7.8 cells", cy.count('class="warnc">7.8<') == 2)
chk("cyber 5.3 cell", cy.count('class="warnc">5.3<') == 1)
# KEV deadline consistency: 12 Sept must agree in banner, patch priority, KEV list
chk("KEV 12 Sept in patch priority", 'data-due="2026-09-12"' in cy)
chk("KEV 12 Sept count = 2 anchors", cy.count('data-due="2026-09-12"') == 2)
chk("KEV 22 Sept anchor", 'data-due="2026-09-22"' in cy)
today = datetime.date(2026, 9, 12)
for due, txt in [("2026-09-12", "0 days left"), ("2026-09-18", "6 days left"),
                 ("2026-09-23", "11 days left"), ("2026-09-22", "10 days left")]:
    y, m, d = map(int, due.split("-"))
    chk("countdown %s = %s" % (due, txt), (datetime.date(y, m, d) - today).days == int(txt.split()[0]))
    chk("countdown %s rendered" % due, txt in cy)
# the four-times-recurring substring trap: pin raw AND rendered counts
chk("'0 days left' rendered exactly once", len(re.findall(r"(?<![0-9])0 days left", cy)) == 1)
# 5th recurrence of the documented trap: the KEV countdown <script> contains the
# string literal '0 days left'. Pin BOTH numbers - raw 2, rendered 1 - per the
# previous ledger's prescription. Rendered-body counting is the actual fix.
chk("'0 days left' raw count pinned at 2", len(re.findall(r"(?<![0-9])0 days left", raw["cyber-briefing.html"])) == 2)
chk("'0 days left' script-literal is the only extra",
    len(re.findall(r"(?<![0-9])0 days left", raw["cyber-briefing.html"]))
    - len(re.findall(r"(?<![0-9])0 days left", cy)) == 1)
chk("'10 days left' not counted as '0 days left'", "10 days left" in cy)
chk("threat level High", "Threat Level: High" in cy)
chk("patch priority is crit border", 'class="callout crit"' in cy)
# refusals must be present and the refused strings must appear ONLY inside the refusal block
refblk = cy[cy.index("Refused This Run"):cy.index("Vulnerability Watch")]
cyfoot = cy[cy.index("<footer>"):]
cyed = cy[:cy.index("Refused This Run")] + cy[cy.index("Vulnerability Watch"):cy.index("<footer>")]
for bad in ["Summit Pathology", "Imperial Healthcare Solutions", "DiamondLease", "NightSpire"]:
    chk("refused '%s' named in refusal block" % bad, refblk.count(bad) >= 1)
    # must NOT appear in editorial (top story, breach cards, CVE table, KEV list)
    chk("refused '%s' absent from editorial" % bad, cyed.count(bad) == 0)
chk("Summit footer links are citations for the refusal, not coverage",
    cyfoot.count("Summit Pathology") == 2 and "refused above" in cyfoot)
chk("refused Summit dated 2024", "2024" in refblk and "18 April 2024" in refblk)
# standing refusal from CORRECTIONS: placeholder CVE must never appear
for bad in ["CVE-2026-12345", "Mantax Otax"]:
    chk("standing refusal absent: " + bad, bad not in cy)
chk("cyber patch tuesday range", "966&ndash;997" in cy or "966–997" in cy)
chk("cyber BOD 26-04 not 22-01", "BOD 26-04" in cy and "BOD 22-01" in cy and "not</b> the old BOD 22-01" in cy)

# ---------- MMA ----------
mm = body["mma-briefing.html"]
champs = re.findall(r"<tr><td>([^<]+)</td><td[^>]*>(.*?)</td><td>", mm)
cmap = {}
for div, cell in champs:
    cmap[div.replace("&rsquo;", "'").strip()] = re.sub(r"<[^>]+>", "", cell).strip()
expect = {"Heavyweight": "Tom Aspinall", "Light Heavyweight": "Carlos Ulberg",
          "Middleweight": "Sean Strickland", "Welterweight": "Islam Makhachev",
          "Lightweight": "Justin Gaethje", "Featherweight": "Alexander Volkanovski",
          "Bantamweight": "Petr Yan", "Flyweight": "Joshua Van",
          "Women's Bantamweight": "Kayla Harrison", "Women's Flyweight": "VACANT",
          "Women's Strawweight": "Mackenzie Dern"}
chk("champions board has 11 divisions", len([d for d in expect if d in cmap]) == 11)
for div, who in expect.items():
    chk("champion cell %s = %s (got %r)" % (div, who, cmap.get(div)), cmap.get(div) == who)
# regression guards: check the CELL, not the page (blunt checks fired falsely 2 runs running)
for div, banned in [("Light Heavyweight", "Pereira"), ("Middleweight", "Chimaev"),
                    ("Women's Flyweight", "Shevchenko"), ("Featherweight", "vacant")]:
    chk("guard: %s cell excludes %s" % (div, banned), banned.lower() not in cmap.get(div, "").lower())
chk("guard: 'stripped' trap", "stripped" not in mm.lower())
chk("mma 13 'Not yet contested' rows", mm.count("Not yet contested") == 13)
# no result strings anywhere on any page while the card is live
# Scope result-string checks to the Noche card's own sections. The champions board
# legitimately contains "Submission (round 2)" for Kayla Harrison's 2025 title win;
# a page-wide absence check fires on it every time. Check the region, not the page.
for p in PAGES:
    b = body[p]
    if p == "mma-briefing.html":
        b = b[:b.index("Champions Board")]
    for pat in [r"\bdef\.\s", r"\bsubmission \(round", r"\bby (KO|TKO|unanimous decision|split decision)\b",
                r"Noche.{0,60}\bwins\b", r"\bwins by\b", r"\bfinishes\b.{0,30}\bround\b"]:
        chk("%s no Noche result string %r" % (p, pat), re.search(pat, b, re.I) is None)
# and assert the champions board really is where that phrase lives
chk("champions board holds the only 'Submission (round' on the MMA page",
    mm.count("ubmission (round") == 1 and "ubmission (round" in mm[mm.index("Champions Board"):])
chk("mma build note present", "prelims underway" in mm.lower() or "prelims <b>underway</b>" in mm)
chk("mma two-source verification", "UFC.com" in mm and "Sherdog" in mm and "2:08 PM ET" in mm)
chk("mma ESPN no-content reported", "no content at all" in mm)
chk("mma 16-bout figure retired", "sixteen" in mm and "is retired" in mm.replace("<b>", "").replace("</b>", ""))
chk("mma UFC 331 odds both books", "+100" in mm and "&minus;120" in mm and "&minus;105" in mm and "&minus;115" in mm)
chk("mma countdown script", "ufccdn" in raw["mma-briefing.html"])
chk("mma disclaimer", "subject to change" in mm)

# ---------- index cards byte-identical to each page's own summary ----------
ix = raw["index.html"]
for p, cls in [("cyber-briefing.html", "c1"), ("wallstreet-briefing.html", "c2"), ("mma-briefing.html", "c3")]:
    t = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', raw[p], re.S).group(1)
    card = re.search(r'<div class="bcard ' + cls + r'">.*?<p>(.*?)</p>', ix, re.S).group(1)
    chk("index %s byte-identical to %s summary" % (cls, p), card == t)
chk("index no live widgets", "tradingview" not in ix.lower())

# ---------- summary-strip labels ----------
for p, lab in [("cyber-briefing.html", "The Wire"), ("wallstreet-briefing.html", "The Tape"),
               ("mma-briefing.html", "Tale of the Tape")]:
    chk("%s tldr label %s" % (p, lab), ('<b>%s</b>' % lab) in raw[p])

# ---------- footer source URLs ----------
for p in PAGES[1:]:
    urls = re.findall(r'<footer>.*?</footer>', raw[p], re.S)
    hrefs = re.findall(r'href="(https?://[^"]+)"', urls[0])
    chk(p + " has >=8 sources", len(hrefs) >= 8)
    chk(p + " no duplicate source URLs", len(hrefs) == len(set(hrefs)))

print("\n%d checks, %d failures" % (ok + fail, fail))
