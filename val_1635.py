# -*- coding: utf-8 -*-
"""Validator for the 2026-09-11 1635 (post-close) edition."""
import io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_1635 import S_CY, S_WS, S_MMA

D = os.path.dirname(os.path.abspath(__file__))
P = {k: io.open(os.path.join(D, f), encoding="utf-8").read()
     for k, f in [("ix", "index.html"), ("cy", "cyber-briefing.html"),
                  ("ws", "wallstreet-briefing.html"), ("mma", "mma-briefing.html")]}
fails, checks = [], 0


def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)


def has(page, s, msg=None):
    ck(s in P[page], msg or "%s missing: %s" % (page, s[:70]))


def absent(page, s, msg=None):
    ck(s not in P[page], msg or "%s must NOT contain: %s" % (page, s[:70]))


# --- structure: tag balance -------------------------------------------------
for k, t in P.items():
    for tag in ("div", "p", "h2", "h3", "table", "thead", "tbody", "tr", "td", "th",
                "ul", "li", "span", "nav", "header", "a", "section"):
        o = len(re.findall(r"<%s[\s>]" % tag, t))
        c = len(re.findall(r"</%s>" % tag, t))
        ck(o == c, "%s unbalanced <%s>: %d open / %d close" % (k, tag, o, c))
    ck(t.count("<!DOCTYPE html>") == 1, "%s doctype" % k)
    ck(t.count("</html>") == 1, "%s html close" % k)

# --- masthead / nav / stamp -------------------------------------------------
for k in P:
    has(k, 'id="edition"')
    has(k, 'id="datestamp"')
    has(k, 'id="updated"')
    has(k, 'id="freshline"')
    has(k, "America/New_York")
    ck(P[k].count('class="active"') == 1, "%s must have exactly one active tab" % k)
    for href in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                 "mma-briefing.html", "archive.html"):
        has(k, 'href="%s"' % href)

# --- summary strips ---------------------------------------------------------
for k, s, lab in (("cy", S_CY, "The Wire"), ("ws", S_WS, "The Tape"), ("mma", S_MMA, "Tale of the Tape")):
    has(k, '<div class="tldr"><b>%s</b> <span>%s</span></div>' % (lab, s))
    ck(s in P["ix"], "index card sentence must be byte-identical to %s summary" % k)

# --- widgets: Wall Street only ---------------------------------------------
ck(P["ws"].count("s3.tradingview.com") == 8, "ws should carry 8 tradingview scripts, has %d"
   % P["ws"].count("s3.tradingview.com"))
ck(P["ws"].count("embed-widget-single-quote") == 3, "ws needs 3 single-quote widgets")
for k in ("ix", "cy", "mma"):
    ck(P[k].count("tradingview") == 0, "%s must carry no widgets" % k)
for w in ("ticker-tape", "timeline", "stock-heatmap", "mini-symbol-overview", "events"):
    has("ws", "embed-widget-%s" % w)
for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    has("ws", sym)
has("ws", '"symbol":"NASDAQ:VICR"', "Chart of the Day must be VICR")

# --- markets: closes reconcile and appear exactly once ----------------------
TH = {"S&P 500": (7591.70, 7656.98, 65.28), "Nasdaq": (26081.72, 26333.04, 251.32),
      "Dow": (52064.10, 52573.29, 509.19)}
for name, (prev, close, chg) in TH.items():
    ck(abs((prev + chg) - close) < 0.01, "%s close does not reconcile" % name)
for pct, (prev, close, _) in ((0.86, TH["S&P 500"]), (0.96, TH["Nasdaq"]), (0.98, TH["Dow"])):
    ck(abs(((close - prev) / prev * 100) - pct) < 0.02, "percent mismatch for %.2f" % pct)

score = P["ws"][P["ws"].index("Weekly Scorecard"):P["ws"].index("Rates, Bonds")]
for lvl in ("7,656.98", "26,333.04", "52,573.29"):
    ck(P["ws"].count(lvl) == 1, "%s must appear exactly once on ws" % lvl)
    ck(lvl in score, "%s must sit inside the Weekly Scorecard" % lvl)
for lvl in ("7,591.70", "26,081.72", "52,064.10"):
    ck(P["ws"].count(lvl) == 1, "Thursday close %s must appear exactly once" % lvl)

# intraday / junk levels that must never appear
for bad in ("7,672.34", "26,391.15", "52,643.72", "7,671.67", "26,391.88", "7,666.93",
            "52,627.00", "26,363.97", "7,674.54", "52,629.73", "7,718.60", "53,414.25",
            "29,432.84", "2,910.16"):
    absent("ws", bad, "ws must not print unverified level %s" % bad)
absent("ws", "+1.15%", "ws must not print the 9:34 AM opening-bell Dow figure")
absent("ws", "0.88%", "ws must not print the 9:34 AM opening-bell Nasdaq figure")
ck(P["ws"].count("+0.96%") == 1, "the one +0.96% on ws is the Nasdaq close, not the opening bell")

# sourced market figures that must be present
for s in ("509.19", "+0.86%", "+0.96%", "+0.98%", "$100.05", "$104.61", "3.4%", "2.4%",
          "$6.05", "85.6%", "15&ndash;16 September", "$62.06", "$14.25", "+11.84%",
          "&minus;7.10%", "$19.35 billion", "$664 billion"):
    has("ws", s)
absent("ws", "Gold futures", "gold line must stay off the page (feeds disagreed)")

# --- cyber: CVSS read from the FIRST cell of each row ----------------------
rows = re.findall(r"<tr><td><b>(CVE-[\d-]+)</b></td><td>([^<]*)</td>", P["cy"])
got = dict(rows)
for cve, cvss in (("CVE-2026-85706", "10.0 (GitLab)"), ("CVE-2026-20079", "10.0"),
                  ("CVE-2026-19490", "9.3"), ("CVE-2025-25249", "7.3"),
                  ("CVE-2026-67277", "Not stated"), ("CVE-2026-86060", "Not stated")):
    ck(got.get(cve) == cvss, "%s CVSS cell should be %r, got %r" % (cve, cvss, got.get(cve)))
ck(len(rows) == 6, "cyber CVE table should have 6 rows, has %d" % len(rows))

# KEV date agreement across callout, list and top story
ck(P["cy"].count("12 September") >= 3, "12 September must appear in callout, KEV list and table")
ck(P["cy"].count("(1 day left)") >= 2, "the 12 September countdown must read 1 day left")
ck(P["cy"].count("(2 days left)") >= 2, "the 13 September countdown must read 2 days left")
has("cy", "overdue by 6 days")
has("cy", "(5 days left)")
has("cy", 'class="callout crit"')
for s in ("220 million", "3.5 million", "153 million", "4.1 million", "347,000", "395 organisations",
          "19.1.8, 19.2.6 and 19.3.2", "06:00 UTC on 11 September", "BOD 26-04", "GentleKiller",
          "SystemBC", "The Gentlemen", "Viettel", "Veradigm"):
    has("cy", s)
for bad in ("Nevada", "Novo Nordisk", "FulcrumSec", "BOD 22-01", "three-week", "three weeks"):
    absent("cy", bad, "cyber must not contain %s" % bad)

# --- MMA: champions positively asserted, regressions guarded ---------------
for div, champ in (("Heavyweight", "Tom Aspinall"), ("Light Heavyweight", "Carlos Ulberg"),
                   ("Middleweight", "Sean Strickland"), ("Welterweight", "Islam Makhachev"),
                   ("Lightweight", "Justin Gaethje"), ("Featherweight", "Alexander Volkanovski"),
                   ("Bantamweight", "Petr Yan"), ("Flyweight", "Joshua Van"),
                   ("Women&rsquo;s Bantamweight", "Kayla Harrison"),
                   ("Women&rsquo;s Strawweight", "Mackenzie Dern")):
    has("mma", "<td class=\"mut\">%s</td><td><b>%s</b></td>" % (div, champ))
has("mma", "<td class=\"mut\">Women&rsquo;s Flyweight</td><td><b><span class='mut'>Vacant</span></b></td>")
for bad in ("<b>Alex Pereira</b></td>", "<b>Khamzat Chimaev</b></td>", "<b>Ilia Topuria</b></td>",
            "<b>Valentina Shevchenko</b></td>", "<b>Merab Dvalishvili</b></td>",
            "<b>Alexandre Pantoja</b></td>", "Featherweight</td><td><b>Vacant"):
    absent("mma", bad, "stale champion regression: %s" % bad)
ck("stripped" not in P["mma"], "women's flyweight wording must be 'vacated', never 'stripped'")

# odds must name their book; no invented UFC 331 moneyline
has("mma", "&minus;450 / Delgado +350 (Caesars)")
has("mma", "&minus;440 / +340 (DraftKings)")
ck(P["mma"].count("(Caesars)") + P["mma"].count("(DraftKings)") == 2, "each odds quote names one book")
has("mma", "No moneyline for the main event appeared in any source read this run")
absent("mma", "Contender Series earlier in 2026")
has("mma", "he did not come through the Contender Series")
has("mma", "Salahdine Parnasse")
absent("mma", "Saladhine")
absent("mma", "Cody Salkilld")
has("mma", "Waldo Cortes Acosta")
absent("mma", "Cortes-Acosta")
has("mma", 'id="ufccdn"')
has("mma", "2026-09-12T17:00:00-04:00")

# chronology: nothing "upcoming" that already happened
for d in ("12 September 2026", "19 September 2026", "3 October 2026", "24 October 2026"):
    has("mma", d)

# --- new tags reflect a real diff against the 1615 snapshot ----------------
ARCH = os.path.join("/tmp/db_1789158933/archive")
if os.path.isdir(ARCH):
    prev = {}
    for k, f in (("cy", "cyber-2026-09-11-1615.html"), ("ws", "wallstreet-2026-09-11-1615.html"),
                 ("mma", "mma-2026-09-11-1615.html")):
        p = os.path.join(ARCH, f)
        prev[k] = io.open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    for k, token in (("cy", "Veradigm"), ("cy", "Viettel"), ("mma", "CBS</b>")):
        ck(token not in prev[k], "%s tagged New but appears in the 1615 snapshot: %s" % (k, token))

print("checks: %d   failures: %d" % (checks, len(fails)))
for f in fails:
    print("  FAIL", f)
sys.exit(1 if fails else 0)
