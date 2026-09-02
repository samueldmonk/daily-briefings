#!/usr/bin/env python3
"""Validator for the 2026-09-02 ~10:52 AM ET edition. Structural where possible, not string bans."""
import re, os, sys, datetime

OUT = "/sessions/wizardly-compassionate-cerf/mnt/outputs"
P = {k: open(os.path.join(OUT, f)).read() for k, f in
     [("ix", "index.html"), ("ws", "wallstreet-briefing.html"),
      ("cy", "cyber-briefing.html"), ("mma", "mma-briefing.html")]}
ALL = list(P.items())
raised, n = [], 0
def chk(cond, msg):
    global n
    n += 1
    if not cond:
        raised.append(msg)

# ---------- 1. universal furniture
for k, s in ALL:
    chk('id="edition"' in s, "%s: no edition pill" % k)
    chk('id="datestamp"' in s, "%s: no datestamp pill" % k)
    chk('id="updated"' in s, "%s: no updated pill" % k)
    chk('id="freshline"' in s, "%s: no freshline" % k)
    chk(s.count('<nav>') == 1, "%s: nav count != 1" % k)
    for href in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                 "mma-briefing.html", "archive.html"]:
        chk(('href="%s"' % href) in s, "%s: nav missing %s" % (k, href))
    nav = re.search(r'<nav>.*?</nav>', s, re.S).group(0)
    chk(nav.count('class="on"') == 1, "%s: active tab count != 1" % k)
    chk("Intl.DateTimeFormat" in s, "%s: no self-stamp JS" % k)
    chk("America/New_York" in s, "%s: stamp not ET" % k)

# ---------- 2. tldr strips (three briefings only, index uses cards)
for k, label in [("ws", "The Tape"), ("cy", "The Wire"), ("mma", "Tale of the Tape")]:
    m = re.search(r'<div class="tldr"><b>([^<]+)</b>', P[k])
    chk(m is not None and m.group(1).strip() == label,
        "%s: tldr label wrong (%s)" % (k, m.group(1) if m else None))
    chk(P[k].count('class="tldr"') == 1, "%s: tldr count != 1" % k)
chk('class="tldr"' not in P["ix"], "ix: index must use cards, not a tldr strip")
chk(P["ix"].count('class="more"') == 3, "ix: needs exactly three Read-the-briefing links")

# ---------- 3. Wall Street live widget blocks
ws = P["ws"]
chk(ws.count("embed-widget-ticker-tape.js") == 1, "ws: block A missing")
chk('class="livebar"' in ws, "ws: livebar wrapper missing")
for must in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    chk(must in ws.split("embed-widget-single-quote")[0], "ws: ticker tape missing %s" % must)
chk(ws.count("embed-widget-single-quote.js") == 3, "ws: block B needs exactly 3 single quotes")
chk(ws.count("embed-widget-timeline.js") == 1, "ws: block C missing")
chk(ws.count("embed-widget-stock-heatmap.js") == 1, "ws: block D missing")
chk(ws.count("embed-widget-mini-symbol-overview.js") == 1, "ws: block E missing")
chk(ws.count("embed-widget-events.js") == 1, "ws: block F missing")
chk("Quotes stream live" in ws, "ws: block B note line missing")

# ---------- 4. after-hours ban before 4 PM ET
# Narrowed: the page is allowed - required, in fact - to say WHY there is no after-hours block.
# Ban only an after-hours SECTION or an after-hours PRICE, not the sentence recording its absence.
chk("<h2>After-Hours" not in ws and "After-Hours Movers</h2>" not in ws,
    "ws: after-hours SECTION present before 4 PM ET")
for m in re.finditer(r"after[- ]hours", ws, re.I):
    w = ws[max(0, m.start() - 200):m.start() + 200]
    chk(("no after-hours section appears" in w) or ("return in the first edition published after" in w),
        "ws: after-hours mention outside the paragraph documenting its absence")

# ---------- 5. Weekly Scorecard is the ONLY place index levels appear
sc = ws.split("<h2>Weekly Scorecard</h2>")
chk(len(sc) == 2, "ws: Weekly Scorecard heading not found exactly once")
before, after = sc[0], sc[1]
after_table = after.split("</table>")[0]
# Tuesday closes may appear in the Lead's reconciliation sentence (disclosed arithmetic) - allow
# only inside the paragraph that names it as this desk's arithmetic.
for lvl in ["7,631.47", "26,099.77", "52,766.88"]:
    occ = [m.start() for m in re.finditer(re.escape(lvl), ws)]
    for o in occ:
        window = ws[max(0, o - 900):o + 400]
        # Permitted contexts: the scorecard itself; the disclosed reconciliation; and the paragraph
        # that documents a REFUSED figure - which must name the base it is refusing against.
        ok = ("Weekly Scorecard" in ws[o:o + 200]) or ("reconciles exactly" in window) or \
             ("official closes" in window) or (lvl in after_table and o > len(before)) or \
             ("base" in window and "refused" in window)
        chk(ok, "ws: level %s appears outside scorecard/reconciliation context" % lvl)
# banned: any implied intraday index level published as a figure
for banned in ["7,646.70", "7,647.61", "53,044.35", "53,060.57", "26,107.30", "26,110.72", "2,942.09"]:
    chk(banned not in ws, "ws: implied/unclocked intraday level %s published" % banned)

# ---------- 6. mover arithmetic must reconcile to Tuesday closes
movers = {"170.44": (206.63, -17.51), "451.21": (425.00, 6.17),
          "378.25": (434.21, -12.89), "328.22": (362.09, -9.35)}
for lvl, (prev, pct) in movers.items():
    v = float(lvl.replace(",", ""))
    implied = (v - prev) / prev * 100
    chk(abs(implied - pct) < 0.02,
        "ws: %s does not reconcile to %s at %s%% (got %.2f)" % (lvl, prev, pct, implied))
    chk(lvl in ws, "ws: mover level %s missing" % lvl)

# ---------- 7. chart of the day == largest single-name move on the page
chk('"symbol":"NASDAQ:CRDO"' in ws, "ws: chart of the day is not the largest mover (CRDO)")
mv = {"CRDO": 17.51, "MDB": 12.89, "PANW": 9.35, "DELL": 6.17}
chk(max(mv, key=mv.get) == "CRDO", "ws: CRDO is not the largest move by arithmetic")

# ---------- 8. cyber: KEV deadlines consistent between Patch Priority and KEV section
cy = P["cy"]
kevjs = re.findall(r"d\('(kev[0-9A-E]+)',(\d+),(\d+),(\d+)\)", cy)
kd = {a: (int(b), int(c), int(d)) for a, b, c, d in kevjs}
chk(kd.get("kev1") == kd.get("kevA"), "cy: Patch Priority date != KEV section date for MLflow")
chk(kd.get("kev2") == kd.get("kevB"), "cy: Patch Priority next-clock date != KEV section")
today = datetime.date(2026, 9, 2)
chk(kd.get("kevA") == (2026, 9, 2), "cy: MLflow due date is not Sept 2")
chk(datetime.date(*kd["kevA"]) == today, "cy: MLflow deadline is not today")
for cid in ["kev1", "kev2", "kevA", "kevB", "kevC", "kevD", "kevE"]:
    chk(('id="%s"' % cid) in cy, "cy: countdown span %s missing" % cid)
    chk(cid in kd, "cy: countdown %s has no JS date" % cid)
# every KEV bullet with a due date must have a countdown
bullets = re.findall(r"<li><b>CVE-[^<]*</b>.*?</li>", cy, re.S)
for b in bullets:
    if "due <b>September" in b or "remediation due <b>September" in b:
        chk('id="kev' in b, "cy: KEV bullet with a due date has no countdown: %s" % b[:70])
# Citrix must NOT carry a countdown or an adopted date
citrix = [b for b in re.findall(r"<li>.*?</li>", cy, re.S) if "8452" in b]
chk(len(citrix) == 1, "cy: expected exactly one Citrix bullet")
chk('id="kev' not in citrix[0], "cy: Citrix bullet must not carry a countdown")
chk("no Citrix countdown appears" in citrix[0], "cy: Citrix refusal not stated")

# ---------- 9. cyber: the banned blog CVSS must not appear anywhere
for k, s in ALL:
    chk("9.8" not in s, "%s: banned third-party CVSS 9.8 present" % k)
# CVSS column must never be blank
rows = re.findall(r"<tr><td>CVE-[^<]+</td><td[^>]*>([^<]*)</td>", cy)
for r in rows:
    chk(r.strip() != "", "cy: empty CVSS cell")

# ---------- 10. cyber: threat banner + stat strip present and above the top story
chk(cy.index('class="banner"') < cy.index("<h2>Top Story</h2>"), "cy: banner not above Top Story")
chk(cy.index('class="stats"') < cy.index("<h2>Top Story</h2>"), "cy: stat strip not above Top Story")
chk(cy.count('class="stat"') == 4, "cy: stat strip should carry 4 figures")
chk(cy.index("<h2>Top Story</h2>") < cy.index("Patch Priority &mdash;"), "cy: Patch Priority not after Top Story")
chk("callout crit" in cy, "cy: Patch Priority not in crit colour despite a deadline today")

# ---------- 11. mma: champions board parsed structurally, all cells asserted
mma = P["mma"]
tbl = mma.split("<h2>Champions Board</h2>")[1].split("</table>")[0]
cells = dict((re.sub(r"<[^>]+>", "", a).strip(), re.sub(r"<[^>]+>", "", b).strip())
             for a, b in re.findall(r"<tr><td>(.*?)</td><td>(.*?)</td>", tbl))
EXPECT = {"Heavyweight": "Tom Aspinall", "Heavyweight (interim)": "Ciryl Gane",
          "Light Heavyweight": "Carlos Ulberg", "Middleweight": "Sean Strickland",
          "Welterweight": "Islam Makhachev", "Lightweight": "Justin Gaethje",
          "Featherweight": "Alexander Volkanovski", "Bantamweight": "Petr Yan",
          "Flyweight": "Joshua Van", "Women’s Bantamweight": "Kayla Harrison",
          "Women’s Flyweight": "Valentina Shevchenko",
          "Women’s Strawweight": "Mackenzie Dern"}
for div, champ in EXPECT.items():
    chk(cells.get(div) == champ,
        "mma: champions cell %s = %r, expected %r" % (div, cells.get(div), champ))
chk(len(cells) == len(EXPECT), "mma: champions board has %d rows, expected %d" % (len(cells), len(EXPECT)))
chk("Women’s Featherweight" not in tbl, "mma: unsourced Women's Featherweight row added")
# Chimaev may only appear as the man Strickland beat, or in the stale-list narrative - never as an
# affirmative present-tense champion assertion.
for m in re.finditer(r"Chimaev", mma):
    w = mma[max(0, m.start() - 260):m.start() + 120]
    chk(("Strickland" in w) or ("superseded" in w) or ("stale" in w) or ("returned" in w),
        "mma: Chimaev mention without corrective context")

# ---------- 12. mma: countdown + next card
chk('id="ufccdn"' in mma, "mma: no countdown element")
chk("2026-09-05T15:00:00-04:00" in mma, "mma: countdown target missing/wrong")
chk(mma.index('class="cdn"') < mma.index("<h2>Top Story</h2>"), "mma: countdown bar not under nav")

# ---------- 13. mma: nothing 'upcoming' that has already happened
for d in re.findall(r"SEPT (\d+)", mma):
    chk(int(d) >= 2, "mma: upcoming card dated before today (Sept %s)" % d)
chk("August 29, 2026" in mma and "most recent <b>completed</b>" in mma,
    "mma: last-completed-event framing missing")
# Parnasse must never be attributed to the Contender Series
for m in re.finditer(r"Parnasse", mma):
    w = mma[max(0, m.start() - 300):m.start() + 300]
    chk("Contender Series" not in w, "mma: Parnasse near a Contender Series attribution")

# ---------- 14. summaries on index must match each page's own tldr
def tldr_text(k):
    return re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', P[k], re.S).group(1)
for k, marker in [("cy", "Cyber Wire"), ("ws", "Closing Bell"), ("mma", "Octagon")]:
    card = [c for c in re.findall(r'<div class="card c-\w+">.*?</div>', P["ix"], re.S) if marker in c]
    chk(len(card) == 1, "ix: expected one card for %s" % marker)
    chk(tldr_text(k) in P["ix"], "ix: card summary does not match %s page tldr" % k)

# ---------- 15. no novelty marker may survive from the previous edition
prev = "/tmp/db_1788359757/archive"
import glob
for k, fn in [("ws", "wallstreet"), ("cy", "cyber"), ("mma", "mma")]:
    snaps = sorted(glob.glob(os.path.join(prev, "%s-2026-09-02-*.html" % fn)))
    if not snaps:
        continue
    old = open(snaps[-1]).read()
    for card in re.findall(r'<div class="card".*?</div>\s*</div>', P[k], re.S):
        if "t-new" not in card:
            continue
        h3 = re.search(r"<h3>(.*?)</h3>", card, re.S)
        if not h3:
            continue
        term = re.sub(r"<[^>]+>", "", h3.group(1))
        key = None
        for cand in ["Credo", "Palo Alto", "Uber", "McKesson", "Boston Scientific",
                     "JFrog", "Exchange"]:
            if cand in term:
                key = cand
        if key:
            chk(key not in old, "%s: 'New' tag on %s but it was in the previous edition" % (k, key))

# ---------- 16. no relative edition pointers that go stale
for k, s in ALL:
    for bad in ["this morning's edition", "the previous edition said", "as we said earlier"]:
        chk(bad not in s.lower(), "%s: relative edition pointer %r" % (k, bad))

# ---------- 17. sources + disclaimers
for k in ["ws", "cy", "mma"]:
    chk("<h2>Sources</h2>" in P[k], "%s: no sources footer" % k)
    chk(P[k].count('class="disc"') == 1, "%s: disclaimer count != 1" % k)
    blk = re.findall(r'class="[^"]*srcs[^"]*">(.*?)</div>', P[k], re.S)
    chk(len(blk) == 1, "%s: sources block not found exactly once" % k)
    chk(len(blk[0].split("<br>")) >= 8, "%s: fewer than 8 sources listed" % k)
disc_ws = re.findall(r'class="disc">(.*?)</div>', P["ws"], re.S)[0]
chk("investment advice" in disc_ws, "ws: missing investment-advice disclaimer")
chk("information only" in disc_ws.lower(), "ws: missing information-only disclaimer")
chk("subject to change" in P["mma"], "mma: missing cards-subject-to-change disclaimer")

# ---------- 18. no unattributed superlatives (rewritten to catch ANY 'largest ... move/swing')
for k, s in ALL:
    for m in re.finditer(r"largest (?:<b>[^<]*</b> )?(?:index |single-name |post-open )*(?:move|swing)", s):
        w = s[max(0, m.start() - 500):m.start() + 900]
        chk(("this desk" in w) or ("arithmetic" in w) or ("subtraction" in w),
            "%s: superlative %r without showing the working" % (k, m.group(0)))

# ---------- 19. a magnitude superlative must not be falsified by a bigger number on the same page
# Collect every percentage attached to a named ticker on the markets page.
mags = [float(x) for x in re.findall(r"[−-](\d+\.\d+)%", ws)] + \
       [float(x) for x in re.findall(r"\+(\d+)%", ws)]
biggest = max(mags)
if "largest <b>post-open</b> single-name move" in ws:
    # the qualifier is only honest if the page NAMES the bigger, differently-windowed number
    chk("premarket +21%" in ws and "is a larger magnitude" in ws,
        "ws: post-open qualifier used without naming the larger premarket magnitude")
    chk(biggest >= 21, "ws: expected the GitLab premarket magnitude to be the page maximum")

# ---------- 20. ordinal inferences must not be asserted about unnamed people
for k, s in ALL:
    for m in re.finditer(r"\bA (sixth|seventh|eighth) \w+", s):
        w = s[max(0, m.start() - 200):m.start() + 400]
        chk("that was an inference" in w, "%s: ordinal inference %r asserted" % (k, m.group(0)))

# ---------- 21. days-until arithmetic on the MMA page must match the countdown target
for m in re.finditer(r"(Three|Four|Five|Two) days out from a main event", mma):
    words = {"Two": 2, "Three": 3, "Four": 4, "Five": 5}
    d = (datetime.date(2026, 9, 5) - today).days
    chk(words[m.group(1)] == d, "mma: 'days out' says %s, actual is %d" % (m.group(1), d))

# ---------- 22. UFC 331 must not be billed a title fight without a source
chk("Title fight" not in mma, "mma: UFC 331 billed a title fight with no source")
chk("explicitly bills the bout as a title fight" in mma, "mma: title-fight refusal not stated")

# ---------- 23. carried-not-refetched items must be labelled as such
for k, needle in [("cy", "were not re-fetched in this run"), ("mma", "not</b> re-verified in this run")]:
    chk(needle in P[k].replace("<b>", "").replace("</b>", "") or needle in P[k],
        "%s: carried item lacks a not-refetched label" % k)

# ---------- 24. provenance note must not point 'below' from the foot of the page
for k, s in ALL:
    chk("says &ldquo;this run,&rdquo;" not in s or "item on this page says" in s,
        "%s: provenance note uses a directional pointer that is wrong at the page foot" % k)

print("%d checks, %d raised" % (n, len(raised)))
for r in raised:
    print("  RAISED:", r)
sys.exit(1 if raised else 0)
