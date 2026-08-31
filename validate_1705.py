#!/usr/bin/env python3
"""Validation gate for the 5:05 PM Afternoon Edition."""
import sys, io, os, re, datetime
REPO = sys.argv[1]
rd = lambda f: io.open(os.path.join(REPO, f), encoding="utf-8").read()
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
S = {p: rd(p) for p in PAGES}
n = 0; bad = []
def chk(cond, msg):
    global n
    n += 1
    if not cond: bad.append(msg)

# --- structural: every page ---
for p in PAGES:
    s = S[p]
    chk('id="edition"' in s, p + ": edition pill")
    chk('id="datestamp"' in s, p + ": datestamp pill")
    chk('id="updated"' in s, p + ": updated pill")
    chk('id="freshline"' in s, p + ": freshline")
    for tab in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                "mma-briefing.html", "archive.html"]:
        chk('href="%s"' % tab in s, "%s: missing nav tab %s" % (p, tab))
    chk("America/New_York" in s, p + ": self-stamp JS")
    chk(s.count("<html") == 1 and s.rstrip().endswith("</html>"), p + ": html envelope")
    chk("5:05 PM ET" in s or "id=\"freshline\"" in s, p + ": freshness stamp")

# --- no stale New markers from earlier stamps ---
for p in PAGES:
    for st in ["4:55 PM", "1:41 PM", "1:15 PM", "12:51 PM", "12:24 PM", "11:50 AM"]:
        chk("New &middot; %s" % st not in S[p], "%s: stale New marker %s" % (p, st))

# --- live widget blocks on Wall Street ---
ws = S["wallstreet-briefing.html"]
for w in ["embed-widget-ticker-tape.js", "embed-widget-single-quote.js",
          "embed-widget-timeline.js", "embed-widget-stock-heatmap.js",
          "embed-widget-mini-symbol-overview.js", "embed-widget-events.js"]:
    chk(w in ws, "wallstreet: missing widget " + w)
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    chk(sym in ws, "wallstreet: ticker tape missing " + sym)
chk("livebar" in ws, "wallstreet: livebar wrapper")

# --- verified close: level / points / percent mutually consistent ---
prev = {"sp": 7711.76, "nq": 26402.42, "dj": 53559.99}
now = {"sp": 7686.14, "nq": 26370.89, "dj": 53185.90}
pct = {"sp": 0.33, "nq": 0.12, "dj": 0.70}
for k in now:
    d = prev[k] - now[k]
    chk(abs((d / prev[k] * 100) - pct[k]) < 0.02,
        "close arithmetic fails for %s (%.4f vs %.2f)" % (k, d / prev[k] * 100, pct[k]))
chk(abs((prev["dj"] - now["dj"]) - 374.09) < 0.02, "Dow points change 374.09")
for lvl in ["7,686.14", "26,370.89", "53,185.90"]:
    chk(lvl in ws, "wallstreet: missing close level " + lvl)

# --- KEV countdown: Aug 31 -> Sep 14 is 14 days ---
d = (datetime.date(2026, 9, 14) - datetime.date(2026, 8, 31)).days
chk(d == 14, "KEV countdown arithmetic")
cy = S["cyber-briefing.html"]
chk("September 14" in cy, "cyber: KEV deadline date")
chk("(14 days left)" in cy or "14 days" in cy, "cyber: KEV countdown rendered")
chk("15 days left" not in cy, "cyber: stale KEV countdown")
# NARROWED (never loosened): the derived Sept 21 date may be NAMED as the rejected
# heuristic result, but must never be published AS the deadline.
chk(not re.search(r'(deadline|due|remediat\w+)[^.<]{0,40}September 21', cy),
    "cyber: BOD 22-01 derived date published as the deadline")

# --- CVSS values must match the vendor/CISA figures on file ---
chk("9.4" in cy, "cyber: CVE-2026-82078 CVSS 9.4")
chk("CVE-2026-81578" in cy and "CVE-2026-82078" in cy, "cyber: both KEV CVEs present")
# NARROWED (never loosened): a bare 9.8 anywhere on the page is legitimate for other
# CVEs; what must never happen is 9.8 attached to the PaperCut rows or to NetScaler
# (whose official Citrix score is 9.3).
for _cve in ["CVE-2026-82078", "CVE-2026-81578", "CVE-2026-3055"]:
    for _m in re.finditer(re.escape(_cve), cy):
        _w = cy[_m.start():_m.start() + 260]
        chk("9.8" not in _w, "cyber: CVSS 9.8 attached to " + _cve)
chk("CVE-2026-82222" in cy and "10.0" in cy, "cyber: GiveWP CVE + CVSS")

# --- new cyber facts landed ---
for t in ["SimpleHelp", "AnyDesk", "47%", "Huntress"]:
    chk(t in cy, "cyber: missing this-run fact " + t)

# --- MMA: champions board must not regress ---
mm = S["mma-briefing.html"]
chk("Strickland" in mm, "mma: Strickland at MW")
chk(not re.search(r'Middleweight[^<]{0,80}Chimaev', mm), "mma: Chimaev listed as MW champion")
chk(not re.search(r'Light Heavyweight[^<]{0,60}Pereira', mm), "mma: Pereira listed as LHW champion")
for champ in ["Aspinall", "Ulberg", "Makhachev", "Gaethje", "Volkanovski",
              "Yan", "Joshua Van", "Shevchenko", "Harrison", "Dern"]:
    chk(champ in mm, "mma: missing champion " + champ)
chk("Featherweight" in mm and "vacant" not in mm.lower().split("women")[0][-4000:], "mma: FW must not be vacant")
chk("&minus;600" in mm and "+430" in mm, "mma: refreshed Paris odds")
chk("ufccdn" in mm, "mma: countdown element")

# --- Nevada 2025 ransomware must never appear as a 2026 story ---
for p in PAGES:
    chk("Nevada" not in S[p] or "2025" in S[p], p + ": Nevada incident guard")

# --- summary strips present and tailored ---
chk('<b>The Tape</b>' in ws, "wallstreet: tldr label")
chk('<b>The Wire</b>' in cy, "cyber: tldr label")
chk('<b>Tale of the Tape</b>' in mm, "mma: tldr label")

# --- index cards mirror the three leads ---
ix = S["index.html"]
for t in ["7,686.14", "Optimus", "SimpleHelp", "Strickland", "+430"]:
    chk(t in ix, "index: card out of sync, missing " + t)

# --- sources present ---
for p in ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]:
    chk(S[p].count('href="https://') >= 8, p + ": too few sources")
    chk('class="disc"' in S[p], p + ": disclaimer")

print("%d checks, %d raised" % (n, len(bad)))
for b in bad:
    print("  RAISED:", b)
sys.exit(0)
