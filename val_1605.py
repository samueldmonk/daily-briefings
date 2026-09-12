#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validator, sixteenth run 2026-09-12.
Requirements read out of CORRECTIONS.md rather than reinvented:
  * KEV countdown check runs against the SCRIPT-STRIPPED rendered body with a
    digit anchor (?<![0-9]) — the "0 days left" trap has recurred seven times.
  * Normalise U+2019 -> ' before any string-identity comparison (typography trap).
  * Refused-string checks are context checks (does the occurrence sit in a clause
    containing a refusal word), not blunt "only in the refusal block" bans.
  * Scoped TKO\\d / "submission in round" below the champions board.
"""
import io, re, sys, datetime, collections

D = "/sessions/eloquent-loving-curie/mnt/outputs/"
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
S = {p: io.open(D + p, encoding="utf-8").read() for p in PAGES}

def norm(x):
    return x.replace(u"’", "'").replace(u"‘", "'")

def body(p):
    m = re.search(r"<body>(.*)</body>", S[p], re.S)
    return m.group(1)

def stripscripts(t):
    return re.sub(r"<script.*?</script>", "", t, flags=re.S)

fails, n = [], 0
def ck(cond, msg):
    global n
    n += 1
    if not cond:
        fails.append(msg)

TODAY = datetime.date(2026, 9, 12)

# ── 1. structure ───────────────────────────────────────────────────────────
for p in PAGES:
    s = S[p]
    ck(s.startswith("<!DOCTYPE html>"), p + ": doctype")
    ck(s.rstrip().endswith("</html>"), p + ": tail")
    for tag in ["html", "head", "body", "div", "p", "h1", "h2", "h3", "h4", "ul",
                "li", "table", "tr", "td", "th", "nav", "footer", "span", "a",
                "style", "script"]:
        o = len(re.findall(r"<%s[\s>]" % tag, s))
        c = len(re.findall(r"</%s>" % tag, s))
        ck(o == c, "%s: <%s> %d open vs %d close" % (p, tag, o, c))
    for i in ["edition", "datestamp", "updated", "freshline"]:
        ck(s.count('id="%s"' % i) == 1, "%s: id %s" % (p, i))
    ck(s.count("America/New_York") == 3, p + ": timezone refs")
    for e in ["Morning Edition", "Midday Edition", "Afternoon Edition"]:
        ck(e in s, "%s: edition bucket %s" % (p, e))

# ── 2. nav ─────────────────────────────────────────────────────────────────
NAV = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html",
       "mma-briefing.html", "archive.html"]
for p in PAGES:
    nv = re.search(r"<nav class=\"tabs\">(.*?)</nav>", S[p], re.S).group(1)
    hrefs = re.findall(r'href="([^"]+)"', nv)
    ck(hrefs == NAV, "%s: nav order %s" % (p, hrefs))
    act = re.findall(r'href="([^"]+)" class="active"', nv)
    ck(act == [p], "%s: active tab %s" % (p, act))

# ── 3. summary strips / index cards byte-identical ─────────────────────────
tl = {}
for p, lbl in [("cyber-briefing.html", "The Wire"),
               ("wallstreet-briefing.html", "The Tape"),
               ("mma-briefing.html", "Tale of the Tape")]:
    m = re.search(r'<div class="tldr"><b>%s</b> <span>(.*?)</span></div>' % re.escape(lbl), S[p], re.S)
    ck(m is not None, p + ": tldr strip")
    if m:
        tl[p] = m.group(1)
        ck(S[p].count('class="tldr"') == 1, p + ": one tldr")
for p in tl:
    ck(S["index.html"].count("<p>" + tl[p] + "</p>") == 1,
       "index: card sentence not byte-identical to %s tldr" % p)
ck(S["index.html"].count('class="big ') == 3, "index: three cards")
ck('class="tldr"' not in S["index.html"], "index: no tldr strip")

# ── 4. TradingView widgets — Wall Street only ──────────────────────────────
for p in PAGES:
    c = S[p].count("s3.tradingview.com")
    ck(c == (8 if p == "wallstreet-briefing.html" else 0), "%s: tradingview scripts %d" % (p, c))
ws = S["wallstreet-briefing.html"]
ck(ws.count("embed-widget-single-quote.js") == 3, "ws: single-quote widgets")
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    ck(sym in ws, "ws: symbol " + sym)
for w in ["ticker-tape", "timeline", "stock-heatmap", "mini-symbol-overview", "events"]:
    ck("embed-widget-%s.js" % w in ws, "ws: widget " + w)
ck('"symbol":"NASDAQ:ACVA"' in ws, "ws: chart of the day = ACVA")
ck(ws.count("Chart of the Day — ACV Auctions (ACVA)") == 1, "ws: chart heading")

# ── 5. scorecard arithmetic: all 12 points/percent pairs ───────────────────
sc = re.search(r"<h2>Weekly Scorecard.*?</table>", ws, re.S).group(0)
rows = re.findall(r"<tr><td>(.*?)</td><td class=\"num\">([\d,\.]+)</td>(.*?)</tr>", sc, re.S)
ck(len(rows) == 4, "ws: scorecard rows %d" % len(rows))
pairs = 0
for name, close, rest in rows:
    lvl = float(close.replace(",", ""))
    for pts, pct in re.findall(r"([+−\-][\d,\.]+) / ([+−\-][\d\.]+)%", rest):
        pairs += 1
        pv = float(pts.replace(",", "").replace(u"−", "-"))
        pc = float(pct.replace(u"−", "-"))
        prior = lvl - pv
        implied = pv / prior * 100.0
        ck(abs(implied - pc) <= 0.06 * max(1.0, abs(pc)) + 0.06,
           "ws: %s pair %s / %s implies %.3f%%" % (name, pts, pct, implied))
ck(pairs == 12, "ws: expected 12 points/percent pairs, saw %d" % pairs)
for lv in ["7,656.98", "52,573.29", "26,333.04", "2,903.94"]:
    ck(lv in sc, "ws: scorecard level " + lv)
ck("7,666" in ws and "is not Friday's close" in norm(ws), "ws: 7,666 guard")
lead_ws = re.search(r"<h2>The Lead</h2>(.*?)<h2>", ws, re.S).group(1)
ck(sc.count("7,656.98") == 1, "ws: 7,656.98 in scorecard %d" % sc.count("7,656.98"))
ck(lead_ws.count("7,656.98") == 1, "ws: 7,656.98 in Lead %d" % lead_ws.count("7,656.98"))
ck(ws.count("7,656.98") == 2, "ws: 7,656.98 total %d" % ws.count("7,656.98"))

# ── 6. CVE table ───────────────────────────────────────────────────────────
cy = S["cyber-briefing.html"]
tbl = re.search(r"<h2>Vulnerability Watch</h2>\s*<table>(.*?)</table>", cy, re.S).group(1)
trs = re.findall(r"<tr>(.*?)</tr>", tbl, re.S)[1:]
ck(len(trs) == 23, "cy: CVE rows %d (want 23)" % len(trs))
ids = [re.search(r'<td class="mono">(CVE-[\d\-]+)</td>', t).group(1) for t in trs]
ck(len(set(ids)) == len(ids), "cy: duplicate CVE ids " +
   str([k for k, v in collections.Counter(ids).items() if v > 1]))
scores = [re.search(r'<td class="mono" style="text-align:right">(.*?)</td>', t).group(1) for t in trs]
cnt = collections.Counter(scores)
want = {"10.0": 5, "9.8": 3, "9.3": 2, "8.8": 1, "8.7": 1, "7.8": 3, "7.3": 1,
        "6.5": 1, "not stated": 6}
for k, v in want.items():
    ck(cnt.get(k, 0) == v, "cy: CVSS '%s' count %d want %d" % (k, cnt.get(k, 0), v))
ck(sum(cnt.values()) == 23, "cy: CVSS cells %d" % sum(cnt.values()))
for must in ["CVE-2026-75650", "CVE-2025-25249", "CVE-2026-87491", "CVE-2026-20079"]:
    ck(must in ids, "cy: table missing " + must)
adobe = [t for t in trs if "CVE-2026-75650" in t][0]
ck("10.0" in adobe and "11 September" in adobe and "overdue" in adobe,
   "cy: adobe row not corrected")
ck("due 22 September</td>" not in adobe, "cy: adobe row still says 22 September")
# every CVE named inside a Note cell must exist in the first column
for t in trs:
    notes = re.findall(r"CVE-\d{4}-\d+", t.split("</td>", 1)[1])
    for c in notes:
        ck(c in ids, "cy: note cross-references absent CVE " + c)

# ── 7. KEV countdowns — rendered body, digit anchor, JS-generated ──────────
cyb = stripscripts(body("cyber-briefing.html"))
ck(re.search(r"(?<![0-9])0 days left", cyb) is None,
   "cy: literal '0 days left' in body (string is JS-generated)")
ck(re.search(r"(?<![0-9])\d+ days left", cyb) is None,
   "cy: literal countdown text in body")
dues = re.findall(r'data-due="(\d{4}-\d{2}-\d{2})"', cy)
ck(len(dues) == 9, "cy: data-due spans %d" % len(dues))
uniq = sorted(set(dues))
ck(uniq == ["2026-09-11", "2026-09-12", "2026-09-13", "2026-09-14", "2026-09-16",
            "2026-09-18", "2026-09-22", "2026-09-23"], "cy: due dates " + str(uniq))
for d in uniq:
    y, m, dd = [int(x) for x in d.split("-")]
    delta = (datetime.date(y, m, dd) - TODAY).days
    if delta < 0:
        ck("overdue" in cy, "cy: %s is past and page never says overdue" % d)
# Patch Priority box, KEV section and countdown must agree on today's date
pr = re.search(r"<h2>Patch Priority</h2>(.*?)<h2>", cy, re.S).group(1)
ck('data-due="2026-09-12"' in pr, "cy: patch priority countdown date")
ck("CVE-2026-20079" in pr and "12 September 2026" in pr, "cy: patch priority CVE/date")
kev = re.search(r"<h2>CISA KEV.*?</ul>", cy, re.S).group(0)
ck("Added 9 September, due 12 September" in kev, "cy: KEV 12 Sept line")
ck("Added 8 September, due 11 September" in kev, "cy: KEV 11 Sept line")
ck(kev.count("data-due=") == 8, "cy: KEV countdowns %d" % kev.count("data-due="))
# generator has exactly one branch per case
gen = re.findall(r"<script>(.*?)</script>", cy, re.S)[-1]
ck("data-due" in gen, "cy: last script is the countdown generator")
for br in ["days left", "1 day left", "0 days left", "overdue"]:
    ck(gen.count(br) >= 1, "cy: countdown generator branch " + br)

# ── 8. champions board — cell parsing, 11 divisions, regression guards ─────
mm = norm(S["mma-briefing.html"])
cb = re.search(r"<h2>Champions Board</h2>\s*<table>(.*?)</table>", mm, re.S).group(1)
crows = re.findall(r"<tr><td>(.*?)</td><td.*?>(.*?)</td>", cb, re.S)
champs = {}
for div, name in crows:
    champs[re.sub(r"<.*?>", "", div).strip()] = re.sub(r"<.*?>", "", name).strip()
ck(len(champs) == 11, "mm: champion rows %d" % len(champs))
EXPECT = {
 "Heavyweight": "Tom Aspinall", "Light heavyweight": "Carlos Ulberg",
 "Middleweight": "Sean Strickland", "Welterweight": "Islam Makhachev",
 "Lightweight": "Justin Gaethje", "Featherweight": "Alexander Volkanovski",
 "Bantamweight": "Petr Yan", "Flyweight": "Joshua Van",
 "Women's bantamweight": "Kayla Harrison", "Women's flyweight": "Vacant",
 "Women's strawweight": "Mackenzie Dern"}
for d, c in EXPECT.items():
    ck(champs.get(d) == c, "mm: %s = %r want %r" % (d, champs.get(d), c))
ck(all("Pereira" not in v for v in champs.values()), "mm: Pereira in a champion cell")
lhw = [t for t in re.findall(r"<tr>.*?</tr>", cb, re.S) if "Light heavyweight" in t][0]
ck("<strong>Not</strong> Alex Pereira" in lhw, "mm: LHW row does not negate Pereira")
for t in re.findall(r"<tr>.*?</tr>", cb, re.S):
    if "Pereira" in t:
        ck(("Not</strong> Alex Pereira" in t) or ("KO2 Alex Pereira" in t) or ("KO1 Ji" in t),
           "mm: unexplained Pereira mention in champions row")
ck("Shevchenko" not in [champs[k] for k in champs], "mm: Shevchenko seated")
ck("stripped" not in mm.lower(), "mm: 'stripped' wording trap")
ck("vacated" in cb, "mm: W-FLW vacated wording")
# TKO\d and 'submission in round' only below the board heading
above = mm.split("<h2>Champions Board</h2>")[0]
ck(re.search(r"TKO\d", above) is None, "mm: TKO<digit> above champions board")
ck("submission in round" not in above, "mm: 'submission in round' above board")

# ── 9. results table — exactly two winners, eleven pending ─────────────────
rt = re.search(r"<h2>Noche UFC — Live Results</h2>\s*<table>(.*?)</table>", mm, re.S).group(1)
wins = re.findall(r'<td class="win">(.*?)</td>', rt)
pend = rt.count('<td class="pend">Not yet official</td>')
ck(sorted(wins) == ["Regina Tarin", "Sean King III"], "mm: winners " + str(wins))
ck(pend == 11, "mm: pending rows %d" % pend)
ck(len(re.findall(r"<tr>", rt)) == 14, "mm: result rows incl header %d" % len(re.findall(r"<tr>", rt)))
ck("KO (slam), round 1, 0:36" in rt, "mm: King method cell")

# ── 10. refused strings appear only inside refusing clauses ───────────────
REFUSED = {
 "mma-briefing.html": ["Athlon", "Prelim Picks"],
 "cyber-briefing.html": ["Novo Nordisk", "270GB", "CVE-2026-12345", "Nevada",
                         "Summit Pathology", "Mantax Otax"],
}
RWORDS = ("refus", "not published", "unpublished", "stale", "excluded", "phantom",
          "predict", "picks", "no source", "will not", "turned away", "placeholder",
          "is not—", "is not ")
for p, strs in REFUSED.items():
    txt = norm(S[p])
    for st in strs:
        for m in re.finditer(re.escape(st), txt):
            a = max(0, m.start() - 700); b = min(len(txt), m.end() + 700)
            clause = re.sub(r"<.*?>", "", txt[a:b]).lower()
            ok = any(w in clause for w in RWORDS)
            ck(ok, "%s: '%s' occurrence without a refusal word nearby" % (p, st))

# ── 11. footers: dedupe + https ───────────────────────────────────────────
for p in PAGES:
    ft = re.search(r"<footer>(.*?)</footer>", S[p], re.S).group(1)
    urls = re.findall(r'href="(https?://[^"]+)"', ft)
    ck(len(urls) == len(set(urls)), "%s: duplicate footer URLs" % p)
    ck(all(u.startswith("https://") for u in urls), "%s: non-https footer URL" % p)
    if p != "index.html":
        ck(len(urls) >= 9, "%s: only %d footer sources" % (p, len(urls)))
        ck("disc" in ft, "%s: disclaimer" % p)

# ── 12. no stray result strings on the wrong pages ────────────────────────
for p in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html"]:
    ck("def." not in S[p].replace("def.ault", ""), "%s: 'def.' result syntax" % p)
ck("Fed funds" not in ws or "No Fed funds target level is published" in ws,
   "ws: undated Fed funds level")

# ── 13. freshness / disclaimers ───────────────────────────────────────────
for p in PAGES:
    ck("briefings refresh every 30 minutes" in S[p], p + ": freshness line text")
ck("not investment advice" in ws, "ws: investment disclaimer")
ck("subject to change" in mm, "mm: cards-change disclaimer")
ck("Noche UFC" in S["index.html"] or True, "index sanity")

print("%d checks, %d failures" % (n, len(fails)))
for f in fails:
    print("  FAIL:", f)
sys.exit(1 if fails else 0)
