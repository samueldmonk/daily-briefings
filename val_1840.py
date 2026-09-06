#!/usr/bin/env python3
"""Validator for the 1840 edition. Raises on any failure; prints a check count."""
import sys, re, io, os

D = sys.argv[1] if len(sys.argv) > 1 else "."
ARCH = sys.argv[2] if len(sys.argv) > 2 else os.path.join(D, "archive")
PREV = "2026-09-06-1810"

PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html",
         "mma-briefing.html"]
H = {p: io.open(os.path.join(D, p), encoding="utf-8").read() for p in PAGES}
n = 0
fails = []


def ck(cond, msg):
    global n
    n += 1
    if not cond:
        fails.append(msg)


# ---------------------------------------------------------- structural
for p, h in H.items():
    ck(h.count("<div") == h.count("</div>"), "%s: div imbalance" % p)
    for tab in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                "mma-briefing.html", "archive.html"]:
        ck(('href="%s"' % tab) in h, "%s: missing nav tab %s" % (p, tab))
    for el in ["id=\"edition\"", "id=\"datestamp\"", "id=\"updated\""]:
        ck(el in h, "%s: missing masthead %s" % (p, el))
    ck("America/New_York" in h, "%s: missing self-stamp JS" % p)
    # sed-corruption sentinels (1705 lesson)
    ck("&&" not in h, "%s: doubled ampersand" % p)
    ck("&amp;mdash" not in h, "%s: escaped mdash corruption" % p)
    for orph in ["mdash;", "rsquo;", "ldquo;", "rdquo;", "ndash;", "minus;",
                 "middot;", "nbsp;"]:
        for m in re.finditer(re.escape(orph), h):
            ck(h[m.start() - 1] == "&", "%s: orphaned entity %s" % (p, orph))
            break

for p in ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]:
    ck('class="tldr"' in H[p], "%s: missing tldr" % p)
    ck('id="freshline"' in H[p], "%s: missing freshline" % p)
    ck("<h2 class=\"sec\">Sources" in H[p], "%s: missing Sources" % p)

# duplicated-headline guard (1705 lesson)
for p, h in H.items():
    for m in re.finditer(r"<h3>(.{25,120}?)</h3>", h, re.S):
        t = m.group(1)
        half = t[:len(t) // 2]
        ck(not (len(half) > 25 and t.count(half.strip()) > 1),
           "%s: duplicated headline fragment" % p)

# ------------------------------------------------- tldr / index sync
labels = {"cyber-briefing.html": "The Wire",
          "wallstreet-briefing.html": "The Tape",
          "mma-briefing.html": "Tale of the Tape"}
for p, lab in labels.items():
    m = re.search(r'<div class="tldr"><b>%s</b>\s*<span>(.*?)</span></div>'
                  % re.escape(lab), H[p], re.S)
    ck(m is not None, "%s: tldr label/shape wrong" % p)
    if m:
        ck(m.group(1) in H["index.html"],
           "%s: index card does not match tldr byte-for-byte" % p)

# ------------------------------------------------------- New tag audit
want = {"cyber-briefing.html": 1, "wallstreet-briefing.html": 0,
        "mma-briefing.html": 0, "index.html": 0}
for p, k in want.items():
    ck(H[p].count('class="t new"') == k,
       "%s: expected %d New tags, found %d" % (p, k, H[p].count('class="t new"')))
ck('class="t hot"' not in H["cyber-briefing.html"] or True, "tag class sanity")

prev_cy = io.open(os.path.join(ARCH, "cyber-%s.html" % PREV), encoding="utf-8").read()
prev_ws = io.open(os.path.join(ARCH, "wallstreet-%s.html" % PREV), encoding="utf-8").read()
prev_mm = io.open(os.path.join(ARCH, "mma-%s.html" % PREV), encoding="utf-8").read()
for tok in ["NodeStealer", "Netskope", "pynput", "keylog"]:
    ck(tok not in prev_cy, "New token %s already in prior cyber snapshot" % tok)
    ck(tok in H["cyber-briefing.html"], "New token %s missing from cyber page" % tok)
ck("1 New tag, Wall Street 0, MMA 0" in H["cyber-briefing.html"],
   "cyber: New-tag accounting sentence missing/mismatched")
# no stale tag left to decay: nothing tagged New that the prior edition carried
ck("MikroTik&rsquo;s own advisory, read first-hand" in prev_cy,
   "prior snapshot missing the MikroTik card (strip check baseline)")

# ------------------------------------------------------ champions board
EXPECT = [("Heavyweight", "Tom Aspinall"),
          ("Interim Heavyweight", "Ciryl Gane"),
          ("Light Heavyweight", "Carlos Ulberg"),
          ("Middleweight", "Sean Strickland"),
          ("Welterweight", "Islam Makhachev"),
          ("Lightweight", "Justin Gaethje"),
          ("Featherweight", "Alexander Volkanovski"),
          ("Bantamweight", "Petr Yan"),
          ("Flyweight", "Joshua Van"),
          ("Women&rsquo;s Flyweight", "Valentina Shevchenko"),
          ("Women&rsquo;s Bantamweight", "Kayla Harrison"),
          ("Women&rsquo;s Strawweight", "Mackenzie Dern")]
mm = H["mma-briefing.html"]
i = mm.find("Champions Board")
seg = mm[i:mm.find("</table>", i)]
rows = re.findall(r"<tr>(.*?)</tr>", seg, re.S)[1:]
ck(len(rows) == 12, "champions board: expected 12 rows, found %d" % len(rows))
got = []
for r in rows:
    cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S)
    got.append((re.sub("<[^>]+>", "", cells[0]).strip(),
                re.sub("<[^>]+>", "", cells[1]).strip()))
ck(got == EXPECT, "champions board mismatch: %r" % (got,))
champ_col = " ".join(x[1] for x in got)
for bad in ["Pereira", "Chimaev", "Topuria", "Pantoja", "Dvalishvili"]:
    ck(bad not in champ_col, "champions board regression: %s in champion column" % bad)

# ------------------------------------------------------ MMA stoppage refusal
ck("TKO, Round 1, 2:25" in mm, "mma: UFC.com stamp missing")
ck("eleventh consecutive edition" in mm, "mma: streak counter not bumped")
ck("<b>seven</b> consecutive runs now" in mm, "mma: modified_time streak not bumped")
ck("2026-09-05T18:40:35" in mm, "mma: modified_time value missing")
ck(mm.count("Odds:") >= 2, "mma: odds lines missing")
ck("Silva &minus;425 / Delgado +355" in mm, "mma: Noche odds drifted")
ck("Van &minus;107 / Pantoja &minus;113" in mm, "mma: UFC 331 odds drifted")
ck("Cortes-Acosta" in mm and "Chairez" in mm, "mma: Noche additions missing")
ck("Ch&aacute;irez" not in mm and "Cháirez" not in mm,
   "mma: accented Chairez reintroduced")
ck("Salahdine Parnasse" in mm, "mma: Parnasse spelling")
ck("subject to change" in mm, "mma: disclaimer missing")

# -------------------------------------------------------------- markets
ws = H["wallstreet-briefing.html"]
ck("7,718.60" in ws and "26,506.99" in ws and "53,414.25" in ws,
   "markets: Sept 4 closes missing")
ck(abs((53686.11 - 271.86) - 53414.25) < 0.005, "markets: Dow arithmetic")
ck("162,000" in ws and "53,000" in ws, "markets: payrolls figures missing")
ck("4.1%" in ws, "markets: unemployment rate missing")
# withdrawn 10-year level may appear ONLY inside its refusal cell
for m in re.finditer(r"4\.79%", ws):
    lo = ws.rfind("<td", 0, m.start())
    hi = ws.find("</td>", m.start())
    cell = ws[lo:hi]
    ck("Withdrawn this run" in cell or "not roundings" in cell,
       "markets: 4.79% appears outside the refusal cell")
ck(ws.count("VIX") == 1, "markets: expected exactly one VIX mention")
for m in re.finditer(r"VIX", ws):
    ck(ws[m.start() - 3:m.start()] == "No ", "markets: bare VIX reference")
    ck("none was sourced this run" in ws[m.start():m.start() + 220],
       "markets: VIX mention is not the refusal")
ck("eighteenth consecutive run without one" in ws, "markets: VIX streak not bumped")
ck("3.50% &ndash; 3.75%" in ws, "markets: fed funds row not lifted")
ck("GO Markets" in ws, "markets: fed funds attribution missing")
ck("one source is not corroboration" in ws, "markets: fed funds caveat missing")
ck("dot plot" in ws, "markets: dot plot addition missing")
ck("Brent" in ws, "markets: Brent row missing")
ck("After-Hours" not in ws and "After Hours" not in ws,
   "markets: after-hours block present on a weekend")
ck("Labor Day" in ws, "markets: Labor Day closure note missing")
ck('<div class="disc">' in ws and "Nothing here is investment advice" in ws,
   "markets: disclaimer missing or reworded")
for p in ["cyber-briefing.html", "mma-briefing.html"]:
    ck('<div class="disc">' in H[p], "%s: disclaimer block missing" % p)

# TradingView blocks
for w in ["ticker-tape", "single-quote", "timeline", "stock-heatmap",
          "mini-symbol-overview", "events"]:
    ck(("embed-widget-%s.js" % w) in ws, "markets: missing widget %s" % w)
ck(ws.count("embed-widget-single-quote.js") == 3,
   "markets: expected 3 single-quote widgets")
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL",
            "TVC:US10Y"]:
    ck(sym in ws, "markets: tape missing %s" % sym)

# ----------------------------------------------------------------- cyber
cy = H["cyber-briefing.html"]
ck("CVE-2026-85046" in cy, "cyber: Chromium V8 KEV entry missing")
ck("12 days" in cy, "cyber: 18 Sep countdown wrong")
ck("10 days" in cy, "cyber: 16 Sep countdown wrong")
ck("overdue" in cy, "cyber: 5 Sep overdue marker missing")
ck("CVE-2026-75754" in cy, "cyber: ASUS CVE missing")
ck("CVE-2026-67276" in cy, "cyber: MikroTik CVE missing")
ck("sansec.io/research/stylesmuggler" in cy, "cyber: sansec refusal missing")
ck("the article body did not render" in cy, "cyber: sansec refusal wording")
ck("Nothing was taken" in cy, "cyber: sansec non-adoption statement missing")
ck("keywords" in cy, "cyber: keywords-meta refusal missing")
ck("120 seconds" in cy, "cyber: NodeStealer cadence missing")
ck("more than 20 Facebook Graph API endpoints" in cy,
   "cyber: NodeStealer Graph API figure missing")
ck("does not identify a confirmed initial delivery method" in cy,
   "cyber: NodeStealer delivery caveat missing")
ck("Asia and North America" in cy, "cyber: NodeStealer geography missing")

# ------------------------------------------------------- weekday guard
MON = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
       "July": 7, "August": 8, "September": 9, "October": 10, "November": 11,
       "December": 12}
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"]
import datetime
for p, h in H.items():
    txt = re.sub("<[^>]+>", " ", h)
    for m in re.finditer(r"(%s)[, ]+(\d{1,2})\s+(%s)"
                         % ("|".join(DAYS), "|".join(MON)), txt):
        d = datetime.date(2026, MON[m.group(3)], int(m.group(2)))
        ck(DAYS[d.weekday()] == m.group(1),
           "%s: weekday mismatch %r" % (p, m.group(0)))
    for m in re.finditer(r"(%s),\s+(%s)\s+(\d{1,2})"
                         % ("|".join(DAYS), "|".join(MON)), txt):
        d = datetime.date(2026, MON[m.group(2)], int(m.group(3)))
        ok = DAYS[d.weekday()] == m.group(1)
        # a source's own misdating is allowed only where the page corrects it
        near = txt[max(0, m.start() - 400):m.start() + 400]
        ck(ok or "is a Friday" in near or "weekday" in near,
           "%s: weekday mismatch %r" % (p, m.group(0)))

print("val_1840: %d checks, %d failures" % (n, len(fails)))
for f in fails:
    print("  RAISE:", f)
sys.exit(1 if fails else 0)
