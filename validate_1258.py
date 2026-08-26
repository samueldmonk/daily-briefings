#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fact-check gate for the 12:58 Midday Edition, Wed Aug 26 2026."""
import io, os, re, sys

D = sys.argv[1] if len(sys.argv) > 1 else "."
TAG = "12:58"
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
P = {p: io.open(os.path.join(D, p), encoding="utf-8").read() for p in PAGES}
fails, checks = [], 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond: fails.append(msg)

def has(page, s, label=None):
    ck(s in P[page], "%s: missing %r" % (page, label or s[:70]))

def hasnt(page, s, label=None):
    ck(s not in P[page], "%s: FORBIDDEN present %r" % (page, label or s[:70]))

# ---------- 1. ARITHMETIC: every published index number reconciles three ways ----------
SPX_PREV, DJI_PREV, IXIC_PREV, RUT_PREV = 7677.28, 53577.40, 26151.30, 3010.02
reads = [
    ("S&P 12:55a", 7667.22, 10.06, 0.13, SPX_PREV, 2),
    ("S&P 12:55b", 7668.63, 8.65, 0.11, SPX_PREV, 2),
    ("S&P 12:55c", 7668.89, 8.39, 0.1, SPX_PREV, 1),
    ("Dow 12:55a", 53433.49, 143.91, 0.27, DJI_PREV, 2),
    ("Dow 12:55b", 53433.99, 143.41, 0.3, DJI_PREV, 1),
    ("Nasdaq 12:55a", 26055.25, 96.05, 0.37, IXIC_PREV, 2),
    ("Nasdaq 12:55b", 26055.65, 95.65, 0.4, IXIC_PREV, 1),
    ("S&P 12:41:56", 7661.57, 15.71, 0.20, SPX_PREV, 2),
    ("S&P 12:39", 7662.54, 14.74, 0.19, SPX_PREV, 2),
    ("S&P 11:06", -7681.36, -4.08, 0.05, SPX_PREV, 2),
]
for name, lvl, pts, pct, prev, dp in reads:
    if lvl < 0:  # gain
        lvl, pts = -lvl, -pts
        ck(abs((lvl - pts) - prev) < 0.011, "%s: level-points != prev close" % name)
    else:
        ck(abs((lvl + pts) - prev) < 0.011, "%s: level+points != prev close" % name)
    ck(abs(round(pts / prev * 100, dp) - pct) < 1e-9,
       "%s: pct mismatch (%.4f vs %s)" % (name, pts / prev * 100, pct))

# 11:47 Fool read: two reconcile, the Nasdaq one does NOT and must be flagged
ck(abs(round((7678 - SPX_PREV) / SPX_PREV * 100, 2) - 0.01) < 1e-9, "11:47 S&P pct")
ck(abs(DJI_PREV * (1 - 0.0018) - 53481.03) < 0.5, "11:47 Dow implied level")
implied_ixic = (26117 - IXIC_PREV) / IXIC_PREV * 100
ck(abs(implied_ixic + 0.131) < 0.005, "11:47 Nasdaq implied pct should be -0.131")
has("wallstreet-briefing.html", "implies &minus;0.131%", "Nasdaq discrepancy flagged")
# 9:59 board still reconciles
for lvl, pts, prev in [(7686.64, 9.36, SPX_PREV), (53594.69, 17.29, DJI_PREV),
                       (26173.36, 22.06, IXIC_PREV)]:
    ck(abs((lvl - pts) - prev) < 0.011, "9:59 board reconcile %s" % lvl)
ck(abs((3007.66 + 2.36) - RUT_PREV) < 0.011, "9:59 Russell reconcile")
# single names carried
ck(abs((345.35 + 12.11) - 357.46) < 0.01, "INTU arithmetic")

# ---------- 2. WALL STREET content guards (each traces to a source this run) ----------
ws = "wallstreet-briefing.html"
for s in ["7,667.22", "53,433.49", "26,055.25", "&minus;10.06", "&minus;143.91", "&minus;96.05",
          "7,668.63", "7,668.89", "53,433.99", "26,055.65",
          "11:47", "7,678", "26,117", "53,480", "Emma Newbery", "12:27&nbsp;p.m. ET",
          "$80.78", "&minus;1.92%", "$4,608.72", "4.67%", "&plus;0.017", "4.65%", "4.629%",
          "$78,048.00", "$210.27", "$577.35", "$337.92",
          "Alibaba", "$10&nbsp;billion share placement", "&plus;40%", "eye-watering 40",
          "energy and industrial stocks", "basic materials and healthcare trail",
          "89.4", "90.2", "3.3% year over year", "over $100 billion",
          "UnitedHealth", "Travelers", "Goldman Sachs", "&minus;1.94%",
          "secondary sanctions", "20-month high of 4.75%"]:
    has(ws, s)
# forbidden: unsupported / previously-rejected strings
for s in ["slipped 0.12%", "Cody Salkilld", "No opening level for any index",
          "$1.4 trillion", "Suno", "Fight Night 286"]:
    hasnt(ws, s)
# the +30.85% board figure must remain the Chart of the Day basis, not be replaced by 40%
has(ws, "+30.85%")
ck(P[ws].count("NYSE:ANF") >= 1, "ws: Chart of the Day symbol")
m = re.search(r'embed-widget-mini-symbol-overview\.js" async>\{"symbol":"([^"]+)"', P[ws])
ck(m and m.group(1) == "NYSE:ANF", "ws: Chart of the Day is NYSE:ANF")

# ---------- 3. WALL STREET structure ----------
ck(P[ws].count("embed-widget-single-quote.js") == 3, "ws: exactly three single-quote widgets")
for w in ["ticker-tape", "timeline", "stock-heatmap", "mini-symbol-overview", "events"]:
    ck(P[ws].count("embed-widget-%s.js" % w) == 1, "ws: one %s widget" % w)
tape = re.search(r'embed-widget-ticker-tape\.js" async>(\{.*?\})</script>', P[ws], re.S).group(1)
syms = re.findall(r'"proName":"([^"]+)"', tape)
ck(len(syms) == len(set(syms)), "ws: duplicate tape symbols %s" % syms)
for mand in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    ck(mand in syms, "ws: tape missing mandatory %s" % mand)
ck("NYSE:BABA" in syms, "ws: tape features Alibaba")
ck("NASDAQ:INTU" not in syms, "ws: INTU rotated off tape")

# ---------- 4. CYBER content guards ----------
cy = "cyber-briefing.html"
for s in ["CVE-2026-60004", "CVSS&nbsp;9.8", "August&nbsp;28", "SecurityWeek", "Help Net Security",
          "BleepingComputer", "ordinary repository write access", "Gitea service account", "1.27.1",
          "CVE-2026-19913", "CVE-2026-19912", "VU#308749", "mwEmbedLoader.php", "ServiceUrl",
          "unable to reach Kaltura", "html5lib",
          "Los Angeles County Museum of Art", "July&nbsp;11, 2025", "late February&nbsp;2026",
          "August&nbsp;24, 2026", "treatment dates", "one year",
          "AnonyMousKIT", "SOCRadar", "506", "168", "179 of the\n200",
          "Alice from Apple Support", "five personas", "CVE-2026-21962", "August&nbsp;27"]:
    has(cy, s.replace("\n", " ")) if "\n" not in s else has(cy, "179 of the\n200")
has(cy, "179 of the\n200") if "179 of the\n200" in P[cy] else has(cy, "179 of the 200")
# the retired "no CVSS" note must be gone
hasnt(cy, "No CVSS score was stated in any source fetched this run, so none is published.",
      "retired Gitea no-CVSS note")
hasnt(cy, "no CVSS published", "retired KEV no-CVSS marker")
# Patch Priority deadline must agree with the KEV board
ck("Added Aug 25, due Aug 28" in P[cy], "cy: Gitea KEV row deadline")
ck("Added Aug 24, due Aug 27" in P[cy], "cy: Oracle KEV row deadline")
# KEV countdown spans: colour must agree with the words
spans = re.findall(r'<span class="kevdue([^"]*)">([^<]+)</span>', P[cy])
ck(len(spans) == 14, "cy: expected 14 kevdue spans, got %d" % len(spans))
nok = sum(1 for c, t in spans if "ok" in c)
ncrit = sum(1 for c, t in spans if "crit" in c)
ck(nok == 4 and ncrit == 10, "cy: kevdue split expected 4 ok / 10 crit, got %d/%d" % (nok, ncrit))
for c, t in spans:
    tl = t.lower()
    if "ok" in c: ck("left" in tl, "cy: ok span not 'left': %r" % t)
    if "crit" in c: ck(("past due" in tl) or ("due today" in tl), "cy: crit span wrong text: %r" % t)
# Gitea 2 days left (Aug 26 -> Aug 28)
ck("2 days left" in P[cy], "cy: Gitea countdown 2 days left")
ck("1 day left" in P[cy], "cy: Oracle countdown 1 day left")

# ---------- 5. MMA: champions board integrity ----------
mm = "mma-briefing.html"
champ_tbl = re.search(r'<div class="lab">Champions board</div>(.*?)</table>', P[mm], re.S).group(1)
rows = re.findall(r'<tr>(.*?)</tr>', champ_tbl, re.S)
ck(len(rows) == 12, "mma: expected 12 champion rows incl. header, got %d" % len(rows))
champ_col = " ".join(re.sub(r'<[^>]*>', ' ', r).split("  ")[0] for r in rows[1:])
champ_cells = []
for r in rows[1:]:
    tds = re.findall(r'<td>(.*?)</td>', r, re.S)
    if len(tds) >= 2: champ_cells.append(re.sub(r'<[^>]*>', '', tds[1]))
ck(len(champ_cells) == 11, "mma: 11 champion cells, got %d" % len(champ_cells))
joined = " | ".join(champ_cells)
for bad in ["Pereira", "Chimaev", "Topuria", "vacant", "Vacant"]:
    ck(bad not in joined, "mma: STALE NAME in champion column: %s" % bad)
for good in ["Tom Aspinall", "Carlos Ulberg", "Sean Strickland", "Islam Makhachev",
             "Justin Gaethje", "Alexander Volkanovski", "Petr Yan", "Joshua Van",
             "Valentina Shevchenko", "Kayla Harrison", "Mackenzie Dern"]:
    ck(good in joined, "mma: missing incumbent %s" % good)
# no card since Sacramento -> board cannot have changed
has(mm, "August&nbsp;22")
has(mm, "no title fight")
# named-fighter traps
for bad in ["Cody Salkilld", "Shamil Yakhyaev", "Abdul-Rakhman", "Shanghai Indoor Stadium"]:
    if bad == "Shanghai Indoor Stadium":
        # allowed ONLY inside an explicit rejection
        for mt in re.finditer(re.escape(bad), P[mm]):
            ctx = P[mm][max(0, mt.start() - 400): mt.end() + 400]
            ck(("not" in ctx) or ("rejected" in ctx) or ("Oriental" in ctx),
               "mma: bare 'Shanghai Indoor Stadium' without rejection context")
    else:
        hasnt(mm, bad)
has(mm, "Oriental Sports Center")
# stale PFL item must NOT be published as news
ck(("PFL" not in P[mm]) or ("June&nbsp;24, 2026" in P[mm]),
   "mma: PFL mentioned without its real June date")

# ---------- 6. New-tag hygiene: no 'New' marker from a prior edition ----------
for p in PAGES:
    for mt in re.finditer(r'New (?:&middot;|at) (\d{1,2}:\d{2})', P[p]):
        ck(mt.group(1) == TAG, "%s: stale New marker %r" % (p, mt.group(0)))

# ---------- 7. Every page: mandatory furniture ----------
for p in PAGES:
    for req in ['id="edition"', 'id="datestamp"', 'id="updated"', 'class="pill live"',
                'index.html', 'cyber-briefing.html', 'wallstreet-briefing.html',
                'mma-briefing.html', 'archive.html', "America/New_York"]:
        has(p, req)
    ck(P[p].count('nav.tabs') >= 1 or 'class="tabs"' in P[p], "%s: nav present" % p)
    tabs = re.search(r'<nav class="tabs">(.*?)</nav>', P[p], re.S)
    ck(tabs is not None and len(re.findall(r'<a ', tabs.group(1))) == 5,
       "%s: five nav tabs" % p)
    ck(P[p].count('class="on"') == 1, "%s: exactly one active tab" % p)
for p in ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]:
    has(p, 'class="tldr"')
    has(p, 'id="freshline"')
for p, lab in [("cyber-briefing.html", "The Wire"), ("wallstreet-briefing.html", "The Tape"),
               ("mma-briefing.html", "Tale of the Tape")]:
    has(p, "<b>%s</b>" % lab, "tldr label %s" % lab)
ck('id="ufccdn"' in P["mma-briefing.html"], "mma: countdown element")
ck("tradingview" not in P["index.html"], "index: no live widgets")

# ---------- 8. index.html cards must match each page's own lead ----------
ix = P["index.html"]
for s in ["7,667.22", "53,433.49", "26,055.25", "11:47", "7,678", "$10&nbsp;billion share placement",
          "&plus;40%", "$80.78", "Nvidia after the close"]:
    has("index.html", s, "index markets card: %s" % s)
for s in ["CVE-2026-60004", "CVSS&nbsp;9.8", "August&nbsp;28", "Kaltura", "VU#308749",
          "Los Angeles County Museum of Art", "14 KEV deadlines with 10 past due"]:
    has("index.html", s, "index cyber card: %s" % s)
ck(ix.count("Read the briefing") == 3, "index: three briefing cards")

# ---------- 9. no unclosed obvious tags / gross corruption ----------
for p in PAGES:
    ck(P[p].count("<div") == P[p].count("</div>"), "%s: div balance (%d open / %d close)"
       % (p, P[p].count("<div"), P[p].count("</div>")))
    ck(P[p].count("<script") == P[p].count("</script>"), "%s: script balance" % p)
    ck(P[p].count("<tr>") == P[p].count("</tr>"), "%s: tr balance" % p)

print("=" * 62)
print("CHECKS RUN: %d   FAILURES: %d" % (checks, len(fails)))
for f in fails: print("  FAIL: " + f)
print("=" * 62)
sys.exit(1 if fails else 0)
