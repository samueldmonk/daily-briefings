#!/usr/bin/env python3
"""Page fixes found by validate_1505.py: index cards written into the wrong card,
a stale 'Dooho Choi' spelling carried from an earlier edition, and an undisclosed
percent truncation on the 3:00 INTU line."""
import re, io, sys
D = "/sessions/festive-upbeat-carson/mnt/outputs/"
def rd(f): return io.open(D+f, encoding="utf-8").read()
fails = []
def must(c, m):
    if not c: fails.append(m)

# ---------------------------------------------------------------- index.html
ix = rd("index.html")
CARDS = {
 "c-sec": ("A tenth straight edition with a frozen KEV board &mdash; and one new CISA ransomware advisory",
   '<p>No CISA KEV alert page later than <b>Aug.&nbsp;24</b> for a <b>tenth consecutive edition</b>: the board holds at '
   '<b>14 deadlines, 10 past due</b>, with <b>Oracle due tomorrow</b> and <b>Gitea on Friday</b>. The only item not '
   'already carried is <b>CISA&rsquo;s #StopRansomware advisory AA26-222A for Gunra ransomware</b> &mdash; published with '
   'a caveat, because the advisory page returned an empty body when fetched.</p>'),
 "c-mkt": ("Three boards, three clocks &mdash; a session that opened green and turned red",
   '<p>Three Yahoo index boards self-stamped <b>~9:59&nbsp;a.m.</b>, <b>~11:59&nbsp;a.m.</b> and <b>~12:29&nbsp;p.m.</b> '
   'reconcile on all eight lines each and show a session that <b>opened green and turned red</b> &mdash; the S&amp;P '
   '<b>&plus;0.12%</b> then <b>&minus;0.15%</b>, with the Nasdaq worst of the four. Latest strip: <b>ANF &plus;40.43%</b>, '
   '<b>XPON &plus;71.16%</b>. <b>&#9888; Bitcoin&rsquo;s implied prior close differs on all three boards.</b></p>'),
 "c-mma": ("The full UFC 331 card lands, and Shanghai is three days out",
   '<p>The <b>full twelve-bout UFC&nbsp;331 line-up</b> for <b>Sept.&nbsp;19</b> at Crypto.com Arena is now on the page, '
   'with prelims at <b>6&nbsp;p.m. ET</b> and the main card at <b>9&nbsp;p.m. ET</b> on Paramount+. Shanghai is three days '
   'out with the line read five ways, all pointing at <b>Umar Nurmagomedov</b>. The champions board is unchanged for a '
   '<b>twenty-fifth</b> consecutive edition.</p>'),
}
for cls, (h2, p) in CARDS.items():
    i = ix.find('class="bcard %s"' % cls)
    must(i > 0, "index: bcard %s missing" % cls)
    if i <= 0: continue
    end = ix.find('</a>', i)
    blk = ix[i:end]
    blk = re.sub(r'<h2>.*?</h2>', '<h2>' + h2 + '</h2>', blk, count=1, flags=re.S)
    blk2 = re.sub(r'<p>.*?</p>', p, blk, count=1, flags=re.S)
    must(blk2 != blk or '<p>' in blk, "index: %s paragraph not replaced" % cls)
    ix = ix[:i] + blk2 + ix[end:]

# ---------------------------------------------------------------- mma: stale spelling
mm = rd("mma-briefing.html")
must("Dooho Choi" in mm, "mma: expected the stale 'Dooho Choi' spelling to be present")
mm = mm.replace("Dooho Choi", "Doo Ho Choi")
must("Dooho Choi" not in mm, "mma: stale spelling survived")
old = "<b>Renato Moicano vs. Brian Ortega</b> and <b>Alonzo Menifield vs. Iwo Baraniewski</b>."
must(old in mm, "mma: main-card sentence anchor missing")
mm = mm.replace(old,
  "<b>Renato Moicano vs. Brian Ortega</b> and <b>Alonzo Menifield vs. Iwo Baraniewski</b>. "
  "<b>&#9888; Corrected at 3:05:</b> this page previously rendered the featherweight as <b>&ldquo;Dooho Choi&rdquo;</b>; "
  "the MMA Mania card listing fetched this run spells him <b>Doo Ho Choi</b>, and that spelling is now used throughout. "
  "<b>&#9888; The same listing also gives the Moicano bout as <em>Ortega 2</em>, a rematch, and does not split its twelve "
  "bouts into a main card and prelims &mdash; so the five-fight main-card composition above and the listing below are "
  "printed side by side and neither is adopted as definitive.</b>", 1)

# ---------------------------------------------------------------- ws: disclose the INTU truncation
ws = rd("wallstreet-briefing.html")
old = "though the percent (18.29 &divide; 357.46 = 5.1166%) lands on the stated 5.11."
must(old in ws, "ws: INTU percent sentence anchor missing")
ws = ws.replace(old,
  "and the percent is <b>truncated rather than rounded</b>: 18.29 &divide; 357.46 = 5.1166%, which rounds to <b>5.12</b> "
  "but is printed as <b>5.11</b>. Both the one-cent base gap and the truncation are disclosed here rather than smoothed.", 1)

if fails:
    print("FAILURES — nothing written:")
    for f in fails: print(" -", f)
    sys.exit(1)
io.open(D+"index.html", "w", encoding="utf-8").write(ix)
io.open(D+"mma-briefing.html", "w", encoding="utf-8").write(mm)
io.open(D+"wallstreet-briefing.html", "w", encoding="utf-8").write(ws)
print("fixes_1505: OK — 3 pages corrected")
