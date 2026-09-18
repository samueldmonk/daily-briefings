# -*- coding: utf-8 -*-
"""Validator — Friday 18 Sep 2026, ~5:10 PM ET edition. Fails loudly."""
import io, os, re, sys, glob

OUT = os.path.dirname(os.path.abspath(__file__))
ARCH = sys.argv[1] if len(sys.argv) > 1 else None

P = {k: io.open(os.path.join(OUT, f), encoding="utf-8").read()
     for k, f in [("ix", "index.html"), ("cy", "cyber-briefing.html"),
                  ("ws", "wallstreet-briefing.html"), ("mma", "mma-briefing.html")]}

n = [0]
fail = []


def ck(cond, msg):
    n[0] += 1
    if not cond:
        fail.append(msg)


# ---------- structural, all four pages
for k, h in P.items():
    ck(h.count("<!DOCTYPE html>") == 1, "%s: doctype count" % k)
    ck(h.count("<body>") == 1, "%s: body count" % k)
    ck(h.count("<nav class=\"tabs\">") == 1, "%s: nav count" % k)
    ck(h.count("</nav>") == 1, "%s: nav close" % k)
    navblk = h[h.find('<nav class="tabs">'):h.find("</nav>")]
    ck(navblk.count("<a href=") == 5, "%s: five nav links (got %d)" % (k, navblk.count("<a href=")))
    ck(navblk.count('class="active"') == 1, "%s: exactly one active tab" % k)
    ck("@@" not in h, "%s: unreplaced @@" % k)
    ck('id="edition"' in h and 'id="datestamp"' in h and 'id="updated"' in h, "%s: masthead pills" % k)
    ck('id="freshline"' in h, "%s: freshline present" % k)
    ck("America/New_York" in h, "%s: stamp JS present" % k)
    ck('class="disc"' in h, "%s: disclaimer present" % k)
    # nav glyphs at entity/codepoint level
    for cp in (0x2605, 0x26E8, 0x25B2, 0x2298, 0x1F5C4):
        ck(chr(cp) in navblk, "%s: nav glyph U+%04X missing" % (k, cp))
    ck(chr(0x26C4) not in h, "%s: banned glyph U+26C4" % k)
    ck(chr(0x25E8) not in h, "%s: banned glyph U+25E8" % k)
    ck('class="warn"' not in h, "%s: undefined warn class" % k)

# ---------- TLDR / index card verbatim match
TL = {}
for k in ("cy", "ws", "mma"):
    m = re.search(r'<div class="tldr"[^>]*>.*?<span>(.*?)</span></div>', P[k], re.S)
    ck(m is not None, "%s: tldr present" % k)
    TL[k] = m.group(1) if m else ""
    ck(P[k].count('class="tldr"') == 1, "%s: exactly one tldr" % k)
ck('class="tldr"' not in P["ix"], "index: must carry no tldr of its own")
for k in ("cy", "ws", "mma"):
    ck(TL[k] and TL[k] in P["ix"], "index card does not verbatim-match %s tldr" % k)
# tailored labels
ck("The Wire" in P["cy"], "cy: tldr label 'The Wire'")
ck("The Tape" in P["ws"], "ws: tldr label 'The Tape'")
ck("Tale of the Tape" in P["mma"], "mma: tldr label 'Tale of the Tape'")

# ---------- TradingView blocks: markets only
TV = ["embed-widget-ticker-tape.js", "embed-widget-single-quote.js", "embed-widget-timeline.js",
      "embed-widget-stock-heatmap.js", "embed-widget-mini-symbol-overview.js", "embed-widget-events.js"]
for w in TV:
    ck(w in P["ws"], "ws: missing widget %s" % w)
    for k in ("ix", "cy", "mma"):
        ck(w not in P[k], "%s: widget %s must be absent" % (k, w))
ck(P["ws"].count("embed-widget-single-quote.js") == 3, "ws: exactly three single-quote widgets")
for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    ck(sym in P["ws"], "ws: tape/quotes must retain %s" % sym)
ck('"symbol":"NASDAQ:XENE"' in P["ws"], "ws: Chart of the Day pinned to NASDAQ:XENE")

# ---------- markets arithmetic (recompute every printed percentage)
def pct(chg, base, want, tol=0.006, label=""):
    got = abs(chg) / base * 100.0
    ck(abs(got - want) <= tol, "ws arithmetic %s: computed %.4f vs printed %.2f" % (label, got, want))

pct(95.40, 51682.64, 0.18, label="Dow close")
pct(104.25, 26522.55 - 104.25, 0.39, label="Nasdaq close vs prior")
pct(7650.50 - 7637.72, 7637.72, 0.17, label="S&P close vs prior")
# the disclosed Dow prior-close gap
ck(abs((51682.64 + 95.40) - 51778.04) < 0.005, "ws: Dow implied prior close figure")
ck(abs(51779.85 - 51778.04 - 1.81) < 0.005, "ws: stated 1.81 pt Dow gap")
for s in ("51,778.04", "1.81", "7,637.72", "26,418.30", "51,779.85"):
    ck(s in P["ws"], "ws: reconciliation figure %s must appear" % s)
for s in ("7,650.50", "26,522.55", "51,682.64", "+0.17%", "+0.39%"):
    ck(s in P["ws"], "ws: close figure %s must appear" % s)
# withheld / refused items named on page
for s in ("No after-hours moves are published", "17 September", "No same-session sector percentages",
          "No VIX reading is published"):
    ck(s in P["ws"], "ws: refusal text missing: %s" % s)
ck("Not re-verified this run" in P["ws"], "ws: scorecard blanks")
ck(P["ws"].count("Not re-verified this run") == 9, "ws: expected 9 not-re-verified cells, got %d"
   % P["ws"].count("Not re-verified this run"))
# oil / rates divergence both printed
for s in ("$100.30", "$103.87", "5.00%", "4.996%", "$99.5"):
    ck(s in P["ws"], "ws: rates/oil figure %s must appear" % s)
ck("+0.07 pp" in P["ws"], "ws: 10y change carries pp unit")

# ---------- cyber KEV invariants
ck(P["cy"].count("18 September 2026") == 3, "cy: deadline must appear exactly 3x, got %d"
   % P["cy"].count("18 September 2026"))
for i in ("cd1", "cd2", "cd3"):
    ck('id="%s"' % i in P["cy"], "cy: countdown slot %s" % i)
ck("days left" in P["cy"] and "due today" in P["cy"], "cy: countdown computed in JS, not written")
ck(not re.search(r"\(\s*\d+\s+days?\s+left\s*\)", P["cy"].replace("d+", "")) or "Math.floor" in P["cy"],
   "cy: countdown must be computed")
ck("BOD 22-01" not in P["cy"], "cy: BOD 22-01 must not be named by number")
ck("BOD 26-04" in P["cy"], "cy: BOD 26-04 named")
ck(P["cy"].count("19 September 2026") == 1, "cy: Cisco date once, got %d" % P["cy"].count("19 September 2026"))
ck("No due date has been confirmed for it and none is asserted" in P["cy"], "cy: Acronis no-due-date sentence")
ck("empty body for a fifth consecutive run" in P["cy"], "cy: cisa.gov empty-body disclosure")
ck("eight new exploited flaws or ten" in P["cy"] or "8 new exploited CVEs" in P["cy"], "cy: both counts printed")
ck("10 newly exploited vulnerabilities" in P["cy"], "cy: body count printed")
ck("sixth" in P["cy"] and "seventh" in P["cy"], "cy: chrome zero-day count dispute printed")
cverows = re.findall(r'<tr><td class="mono">(CVE-\d{4}-\d+)</td>', P["cy"])
ck(len(cverows) == 13, "cy: expected 13 CVE rows, got %d" % len(cverows))
ck(len(set(cverows)) == len(cverows), "cy: duplicate CVE rows")
_cytbl = P["cy"][P["cy"].find("<table><tr><th>CVE</th>"):P["cy"].find("</table>", P["cy"].find("<table><tr><th>CVE</th>"))]
ck(_cytbl.count('class="mono">not stated<') == 2,
   "cy: exactly two 'not stated' CVSS cells in the table, got %d" % _cytbl.count('class="mono">not stated<'))
ck("not stated" in P["cy"][P["cy"].find("</table>", P["cy"].find("<table><tr><th>CVE</th>")):],
   "cy: note must explain the 'not stated' cells")
ck("CVE-2026-85046" in P["cy"] and "CVSS 8.8" in P["cy"], "cy: patch-priority CVE + score")
ck("152.0.7977.82" in P["cy"], "cy: fixed build string")

# ---------- mma champions board
mm = P["mma"]
i = mm.find("Champions board")
tbl = mm[i:mm.find("</table>", i)]
rows = re.findall(r"<tr><td>(.*?)</td><td[^>]*><b>(.*?)</b></td>", tbl)
ck(len(rows) == 11, "mma: 11 champion rows, got %d" % len(rows))
vac = [d for d, c in rows if c == "VACANT"]
ck(len(vac) == 2, "mma: exactly 2 VACANT, got %d" % len(vac))
ck("Heavyweight" in vac, "mma: Heavyweight must be vacant")
ck(any("Flyweight" in v and "Women" in v for v in vac), "mma: Women's Flyweight must be vacant")
champ_cells = " | ".join(c for _, c in rows)
for banned in ("Pereira", "Chimaev", "Shevchenko", "Aspinall", "Topuria", "Ankalaev",
               "Pantoja", "Dvalishvili", "Nunes", "Proch", "Gane"):
    ck(banned not in champ_cells, "mma: banned name %s in a champion cell" % banned)
pins = {"Light Heavyweight": "Carlos Ulberg", "Middleweight": "Sean Strickland",
        "Welterweight": "Islam Makhachev", "Lightweight": "Justin Gaethje",
        "Featherweight": "Alexander Volkanovski", "Bantamweight": "Petr Yan",
        "Flyweight": "Joshua Van", "Women&rsquo;s Bantamweight": "Kayla Harrison",
        "Women&rsquo;s Strawweight": "Mackenzie Dern"}
d2c = dict(rows)
for d, c in pins.items():
    ck(d2c.get(d) == c, "mma: %s must be %s, got %r" % (d, c, d2c.get(d)))
ck(mm.count("Carlos Ulberg") == 2, "mma: Ulberg exactly twice, got %d" % mm.count("Carlos Ulberg"))
ck("Ciryl Gane" in tbl, "mma: Gane named as interim in the HW row")
ck("sixth consecutive run" in mm, "mma: ESPN regression named")
ck("Chimaev vs. Gilbert Burns" in mm and "Not published in any form" in mm, "mma: Fox Nation item refused by name")
ck("0:36" in mm and "33-second" in mm, "mma: King finish time + refusal of 0:33")
ck("2026-09-19T21:00:00-04:00" in mm, "mma: countdown target")
ck('id="ufccdn"' in mm, "mma: countdown slot")
ck("Fight week" in mm, "mma: countdown elapsed branch")
# dates: upcoming future, last event past
for s in ("19 September", "3 October", "24 October"):
    ck(s in mm, "mma: upcoming date %s" % s)
ck("12 September" in mm, "mma: last event date")
ck("tomorrow" in mm.lower(), "mma: 331 framed as tomorrow")
# odds carry book/date attribution
ck("Covers, read this run" in mm and "dated 15 September" in mm, "mma: odds attribution")

# ---------- New tags vs prior snapshots
tags = {k: P[k].count('class="t new"') for k in ("cy", "ws", "mma")}
tags["ws"] += P["ws"].count('class="t new"')
newcounts = {"cy": P["cy"].count('class="t new"'), "ws": P["ws"].count('class="t new"'),
             "mma": P["mma"].count('class="t new"')}
if ARCH and os.path.isdir(ARCH):
    snaps = glob.glob(os.path.join(ARCH, "*.html"))
    blob = ""
    for s in snaps:
        try:
            blob += io.open(s, encoding="utf-8", errors="ignore").read()
        except Exception:
            pass
    for term in ("Vite", "7,650.50", "51,682.64", "CVE-2026-39364", "CVE-2026-85046"):
        print("  grep %-18s -> %d prior snapshots contain it"
              % (term, sum(1 for s in snaps
                           if term in io.open(s, encoding="utf-8", errors="ignore").read())))
    ck(len(snaps) > 0, "archive: snapshots found")
ck(newcounts == {"cy": 0, "ws": 2, "mma": 0},
   "New-tag counts must be cy=0 ws=2 mma=0, got %r" % newcounts)
ck("zero New tags" in P["cy"], "cy: must state its New count in prose")
ck("Two New tags" in P["ws"], "ws: must state its New count in prose")
ck("zero New tags" in P["mma"], "mma: must state its New count in prose")
print("New-tag counts:", newcounts)

print("\nchecks run: %d   failures: %d" % (n[0], len(fail)))
for f in fail:
    print("  FAIL:", f)
sys.exit(1 if fail else 0)
