# -*- coding: utf-8 -*-
"""Validator, eighth run 2026-09-17 ~4:10pm ET."""
import re, datetime, os

OUT = "/sessions/sharp-pensive-ptolemy/mnt/outputs"
TODAY = datetime.date(2026, 9, 17)
P = {n: open(os.path.join(OUT, n)).read() for n in
     ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]}
n = 0
fail = []


def chk(cond, msg):
    global n
    n += 1
    if not cond:
        fail.append(msg)


# ---------- structural
for name, h in P.items():
    chk(h.count("<!DOCTYPE html>") == 1, "%s doctype" % name)
    chk(h.count("<body>") == 1, "%s one body" % name)
    chk(h.count("</body>") == 1, "%s one /body" % name)
    chk(h.count('<nav class="tabs">') == 1, "%s one nav" % name)
    chk(h.count("<footer>") == 1 and h.count("</footer>") == 1, "%s one footer" % name)
    chk(h.count('class="active"') == 1, "%s one active tab" % name)
    chk("@@" not in h, "%s unreplaced @@" % name)
    for href in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                 "mma-briefing.html", "archive.html"]:
        chk('href="%s"' % href in h, "%s nav link %s" % (name, href))
    for gl in ["&#9733;", "&#9960;", "&#9650;", "&#8856;", "&#128452;"]:
        chk(gl in h, "%s nav glyph %s" % (name, gl))
    chk("&#9924;" not in h, "%s snowman glyph blocked" % name)
    chk('id="edition"' in h and 'id="datestamp"' in h and 'id="updated"' in h, "%s meta pills" % name)
    chk('id="freshline"' in h, "%s freshline" % name)
    chk("America/New_York" in h, "%s stamp js" % name)

# ---------- TLDRs: on the three briefings, not the index
for name, label in [("cyber-briefing.html", "The Wire"), ("wallstreet-briefing.html", "The Tape"),
                    ("mma-briefing.html", "Tale of the Tape")]:
    chk(P[name].count('<div class="tldr">') == 1, "%s one tldr" % name)
    chk("<b>%s</b>" % label in P[name], "%s tldr label" % name)
chk('class="tldr"' not in P["index.html"], "index carries no tldr of its own")

# ---------- index cards string-match each briefing's own TLDR verbatim
for name in ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]:
    m = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', P[name], re.S)
    chk(m is not None, "%s tldr extractable" % name)
    if m:
        chk(m.group(1) in P["index.html"], "index card matches %s tldr verbatim" % name)

# ---------- TradingView: markets page only
TVB = ["ticker-tape", "single-quote", "timeline", "stock-heatmap", "mini-symbol-overview", "events"]
for b in TVB:
    chk(("embed-widget-%s.js" % b) in P["wallstreet-briefing.html"], "ws block %s" % b)
    for other in ["index.html", "cyber-briefing.html", "mma-briefing.html"]:
        chk("embed-widget-%s.js" % b not in P[other], "%s free of %s" % (other, b))
chk(P["wallstreet-briefing.html"].count("embed-widget-single-quote.js") == 3, "exactly 3 single-quote widgets")
ws = P["wallstreet-briefing.html"]
for keep in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    chk(keep in ws, "ticker retains %s" % keep)
chk('"symbol":"NASDAQ:MU"' in ws, "chart of the day pinned to MU")

# ---------- markets arithmetic, computed not typed
sp_prev, sp_chg = 7551.81, 87.21
dw_prev, dw_chg = 51461.90, 355.36
nd_prev, nd_chg = 28945.06, 480.96
chk("%.2f" % (sp_prev + sp_chg) == "7639.02", "S&P level computes")
chk("{:,.2f}".format(sp_prev + sp_chg) in ws, "S&P level on page")
chk("%.2f" % (dw_prev + dw_chg) == "51817.26", "Dow level computes")
chk("{:,.2f}".format(dw_prev + dw_chg) in ws, "Dow level on page")
chk("%.2f" % (nd_prev + nd_chg) == "29426.02", "Nasdaq 100 level computes")
chk("{:,.2f}".format(nd_prev + nd_chg) in ws, "Nasdaq 100 level on page")
chk(round(sp_chg / sp_prev * 100, 2) == 1.15, "S&P pct computes to 1.15")
chk(round(dw_chg / dw_prev * 100, 2) == 0.69, "Dow pct computes to 0.69")
chk(round(nd_chg / nd_prev * 100, 2) == 1.66, "Nasdaq 100 pct computes to 1.66")
# mover percentages reconcile last-minus-change
for last, chg, pct, who in [(977.36, 50.81, 5.48, "MU"), (348.66, 9.15, 2.70, "AVGO"),
                            (219.66, 5.76, 2.69, "NVDA"), (955.80, 17.82, 1.90, "GS")]:
    chk(round(chg / (last - chg) * 100, 2) == pct, "%s pct reconciles" % who)

# ---------- markets honesty guards
chk("no index-level source had published official thursday closing figures" in ws.lower(),
    "post-close caveat present")
chk(ws.lower().count("official thursday closing figures") >= 1, "post-close caveat phrasing")
chk("4:12 PM ET" in ws, "as-of time stamped")
chk("Weekly scorecard" in ws or "Weekly Scorecard" in ws, "weekly scorecard present")
chk("After-hours movers" in ws, "after-hours section present (post 4pm)")
chk("nothing was sourced" in ws, "after-hours emptiness stated")
chk("7,596" in ws and "0.59%" in ws, "superseded snapshot named as refused")
chk("downward pressure" in ws, "bad-summary refusal named")
chk("5.01%" in ws, "10-yr 5.01% refusal named")
chk("15.49" in ws and "fourth consecutive edition" in ws, "VIX refusal named")
chk("Nasdaq\nComposite percentage is published" not in ws, "no stray")
chk("No Nasdaq " in ws and "Composite percentage is published" in ws, "Nasdaq Composite refusal named")
chk("7635" in ws and "1.10%" in ws, "TE self-divergence printed")
chk("14%" in ws, "barchart wrong-session refusal named")
chk("4.94%" in ws, "10-yr level published")
chk("$101.44" in ws and "$4,354.47" in ws, "commodities published")
chk("not investment advice" in ws, "ws disclaimer")

# ---------- cyber
cy = P["cyber-briefing.html"]
chk("Threat level &mdash; High" in cy, "threat banner")
chk(cy.count('<div class="stat">') == 4, "four stat cards")
chk("CVE-2026-76461" in cy and "CVE-2026-76460" in cy, "both Cisco CVEs")
chk("BOD 26-04" in cy, "new directive named")
chk("three days" in cy, "three-day window stated")
chk(cy.count("BOD 22-01") == 1, "superseded directive named exactly once")
chk("not the three-week window of the older BOD 22-01" in cy,
    "BOD 22-01 appears only inside the supersession clause")
chk(cy.count("three-week") == 1 and "three weeks" not in cy,
    "three-week window mentioned only as the superseded one")
# KEV countdowns computed
for due, expect in [(datetime.date(2026, 9, 17), "0 days &mdash; due TODAY"),
                    (datetime.date(2026, 9, 19), "2 days left"),
                    (datetime.date(2026, 9, 13), "OVERDUE by 4 days"),
                    (datetime.date(2026, 9, 14), "OVERDUE by 3 days"),
                    (datetime.date(2026, 8, 21), "OVERDUE by 27 days")]:
    d = (due - TODAY).days
    if d > 1:
        s = "%d days left" % d
    elif d == 1:
        s = "1 day left"
    elif d == 0:
        s = "0 days &mdash; due TODAY"
    else:
        s = "OVERDUE by %d days" % (-d)
    chk(s == expect, "countdown arithmetic %s" % due)
    chk(s in cy, "countdown on page %s" % due)
chk("19 September 2026" in cy, "Saturday deadline date printed")
chk(datetime.date(2026, 9, 19).strftime("%A") == "Saturday", "19 Sep is a Saturday")
chk("Revolut" in cy and "$3 million" in cy, "Revolut top story")
chk("IAmNotAVillain" in cy, "spotlight actor named")
chk("680" in cy and "147GB" in cy, "Revolut figures")
chk("has not received any direct contact" in cy, "Revolut denial quoted")
chk("No CVE asserted" in cy, "City Relay CVE deliberately unmapped")
chk("not stated" in cy, "Acronis no-CVSS stated")
chk("no usable content on direct fetch" in cy, "cisa.gov failure named")
chk("1,183" in cy and "5,237" in cy and "412" in cy, "Black Kite figures")
chk("Patch priority" in cy, "patch priority section")
chk('class="callout crit"' in cy, "patch priority is crit-bordered (deadline today)")
chk(cy.count('class="tag new"') == 0, "cyber carries zero New tags")
chk("No card above is tagged" in cy, "cyber states the zero-New result in prose")
chk("756 archived snapshots" in cy, "cyber names the snapshot corpus searched")
chk("development, not a debut" in cy, "top story novelty honestly framed")
chk("attributed secondary characterisation" in cy, "BOD 26-04 history stated")
chk(P["wallstreet-briefing.html"].count('class="tag new"') == 0, "markets carries zero New tags")
chk("Zero &ldquo;New&rdquo; tags in this section" in ws, "markets states the zero-New result")
chk(P["mma-briefing.html"].count('class="tag new"') == 1, "mma carries exactly one New tag")

# ---------- mma
mm = P["mma-briefing.html"]
chk("UFC 331" in mm and "Van vs. Pantoja 2" in mm, "UFC 331 present")
chk("boxingnews.com" in mm and "refused" in mm, "withdrawal claim refused and source named")
chk("Anthony Joshua" in mm, "aggregator tell cited")
chk("&minus;135" in mm, "CBS/DraftKings main-event line")
chk("&minus;2100" in mm and "+130" in mm and "+154" in mm, "further sourced lines")
chk("id=\"ufccdn\"" in mm and "2026-09-19T21:00:00-04:00" in mm, "countdown target")
chk("Proch&aacute;zka" in mm, "accented Prochazka")
chk("Prochazka" not in mm.replace("Proch&aacute;zka", ""), "no bare Prochazka")
# champions board: 12 rows, exactly 2 VACANT
rows = re.findall(r"<tr><td>([^<]+)</td><td[^>]*><b>([^<]+)</b></td>", mm)
champ_rows = [r for r in rows if "weight" in r[0].lower()]
chk(len(champ_rows) == 12, "champions board 12 rows (got %d)" % len(champ_rows))
chk(sum(1 for r in champ_rows if r[1] == "VACANT") == 2, "exactly 2 vacant")
cells = " | ".join(r[1] for r in champ_rows)
for banned in ["Pereira", "Chimaev", "Shevchenko", "Aspinall", "Topuria", "Ankalaev", "Pantoja",
               "Prochazka", "Proch&aacute;zka", "Dvalishvili", "Nunes"]:
    chk(banned not in cells, "%s absent from champion cells" % banned)
chk(("Light Heavyweight", "Carlos Ulberg") in champ_rows, "Ulberg pinned to LHW")
chk(sum(1 for r in champ_rows if r[1] == "Carlos Ulberg") == 1, "Ulberg appears once")
chk(("Interim Heavyweight", "Ciryl Gane") in champ_rows, "Gane pinned to interim HW")
for div, who in [("Middleweight", "Sean Strickland"), ("Welterweight", "Islam Makhachev"),
                 ("Lightweight", "Justin Gaethje"), ("Featherweight", "Alexander Volkanovski"),
                 ("Bantamweight", "Petr Yan"), ("Flyweight", "Joshua Van"),
                 ("Women&rsquo;s Bantamweight", "Kayla Harrison"),
                 ("Women&rsquo;s Strawweight", "Mackenzie Dern")]:
    chk((div, who) in champ_rows, "%s = %s" % (div, who))
chk(("Heavyweight", "VACANT") in champ_rows, "HW vacant")
chk(("Women&rsquo;s Flyweight", "VACANT") in champ_rows, "W-FLW vacant")
# ESPN regression named
chk("Carlos Ulberg at HEAVYWEIGHT" in mm or "Ulberg at HEAVYWEIGHT" in mm, "ESPN HW regression named")
chk("LIGHT HEAVYWEIGHT" in mm, "ESPN LHW regression named")
# dates chronological
chk("19 September" in mm and "3 Oct 2026" in mm and "24 Oct 2026" in mm, "three future cards")
for d in [datetime.date(2026, 9, 19), datetime.date(2026, 10, 3), datetime.date(2026, 10, 24),
          datetime.date(2026, 9, 24)]:
    chk(d > TODAY, "%s is future" % d)
chk(datetime.date(2026, 9, 12) < TODAY, "last event is past")
chk(mm.count("0:36") == 1 and mm.count("0:33") == 1, "King timings each named once")
chk("timed the King finish at <b>0:36</b> and refused a competing <b>0:33</b>" in mm,
    "both King timings appear only inside the refusal clause")
chk("round one" in mm, "only 'round one' is asserted for the King finish")
chk("subject to change" in mm, "mma disclaimer")
chk("No viewership, gate or TKO Group figure is published" in mm, "no invented business figures")

print("checks:", n, "failures:", len(fail))
for f in fail:
    print("  FAIL:", f)
