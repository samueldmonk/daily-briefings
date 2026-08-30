#!/usr/bin/env python3
"""Regenerate archive.html from the snapshot files in archive/.

Never hand-curated: the page is built entirely by listing archive/<section>-YYYY-MM-DD-HHMM.html.
Reuses the existing archive.html's <style> block so the design carries forward unchanged.
"""
import os, re, sys, collections

D = sys.argv[1] if len(sys.argv) > 1 else "."
ARC = os.path.join(D, "archive")
OUT = os.path.join(D, "archive.html")

SECTIONS = [("cyber", "The Cyber Wire"), ("wallstreet", "The Closing Bell"), ("mma", "The Octagon")]
SECNAME = dict(SECTIONS)
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

# ── collect snapshots ───────────────────────────────────────────────────────
pat = re.compile(r"^(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html$")
by_day = collections.defaultdict(lambda: collections.defaultdict(dict))
total = 0
for fn in os.listdir(ARC):
    m = pat.match(fn)
    if not m:
        continue
    sec, y, mo, d, hhmm = m.groups()
    by_day[(int(y), int(mo), int(d))][hhmm][sec] = fn
    total += 1

def ampm(hhmm):
    h, mi = int(hhmm[:2]), hhmm[2:]
    suffix = "AM" if h < 12 else "PM"
    h12 = h % 12 or 12
    return "%d:%s %s ET" % (h12, mi, suffix)

# ── carry the existing style block forward ──────────────────────────────────
style = ""
if os.path.exists(OUT):
    old = open(OUT, encoding="utf-8").read()
    m = re.search(r"<style>.*?</style>", old, re.S)
    if m:
        style = m.group(0)
assert style, "archive.html: could not read the existing <style> block to carry forward"
assert "s3.tradingview.com" not in style, "archive: style block must carry no live widgets"

NAV = ('<nav class="tabs">'
       '<a href="index.html">&#9733; Front Page</a>'
       '<a href="cyber-briefing.html">&#9880; The Cyber Wire</a>'
       '<a href="wallstreet-briefing.html">&#9650; The Closing Bell</a>'
       '<a href="mma-briefing.html">&#8856; The Octagon</a>'
       '<a href="archive.html" class="on">&#128451; Archive</a></nav>')

STAMPJS = ("<script>(function(){try{var n=new Date();"
           "var et=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'long',"
           "year:'numeric',month:'long',day:'numeric'}).format(n);"
           "var t=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',"
           "minute:'2-digit'}).format(n);"
           "var h=parseInt(new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',"
           "hour:'numeric',hour12:false}).format(n),10);"
           "var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');"
           "document.getElementById('datestamp').textContent=et;"
           "document.getElementById('updated').textContent=t+' ET';"
           "document.getElementById('edition').textContent=ed;"
           "var fl=document.getElementById('freshline');"
           "if(fl)fl.textContent='Data as of '+t+' ET \\u00b7 briefings refresh every 30 minutes, "
           "8 AM\\u20136 PM ET';}catch(e){}})();</script>")

body = []
days = sorted(by_day.keys(), reverse=True)
for (y, mo, d) in days:
    body.append('<h2 class="sec">%s %d, %d</h2>' % (MONTHS[mo - 1], d, y))
    body.append('<div class="panel" style="padding:6px 14px">')
    for hhmm in sorted(by_day[(y, mo, d)].keys(), reverse=True):
        files = by_day[(y, mo, d)][hhmm]
        links = []
        for sec, label in SECTIONS:
            if sec in files:
                links.append('<a href="archive/%s">%s</a>' % (files[sec], label))
            else:
                links.append('<span class="mut">%s &mdash;</span>' % label)
        body.append(
            '<div class="arow"><span class="atime">%s</span>'
            '<span class="alinks">%s</span></div>' % (ampm(hhmm), " &middot; ".join(links)))
    body.append("</div>")

extra = ("<style>.arow{display:flex;flex-wrap:wrap;gap:10px;align-items:baseline;"
         "padding:7px 0;border-bottom:1px solid var(--line)}"
         ".arow:last-child{border-bottom:none}"
         ".atime{font-family:var(--mono);font-size:11.5px;letter-spacing:.08em;"
         "color:var(--mut);min-width:104px}"
         ".alinks{font-size:14px}.mut{color:var(--mut)}</style>")

html = (
    '<!doctype html><html lang="en"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1">'
    '<title>Archive &mdash; Daily Briefings</title>' + style + extra + '</head><body><div class="wrap">'
    '<header class="masthead"><h1 class="brand">Archive</h1>'
    '<p class="tagline">Every published edition of the three briefings, newest first.</p>'
    '<div class="meta"><span class="pill live"><span class="dot"></span>Live</span>'
    '<span class="pill" id="edition">&mdash;</span>'
    '<span class="pill" id="datestamp">&mdash;</span>'
    '<span class="pill">Updated <span id="updated">&mdash;</span></span></div></header>'
    '<div class="freshline" id="freshline">&mdash;</div>' + NAV +
    '<div class="note" style="margin-bottom:18px">These are <b>point-in-time snapshots</b>. '
    'Each captures a briefing exactly as it was published at that moment and is '
    '<b>never updated afterwards</b>, so an older snapshot may contain figures that later '
    'editions corrected or withdrew &mdash; that is the point of keeping them. Live quote widgets '
    'do not appear on archived pages. Snapshots older than 21 days are pruned automatically. '
    '<b>%d snapshots across %d days.</b></div>' % (total, len(days)) +
    "".join(body) +
    '<footer><div class="disc">Archived editions are retained for reference only. Figures in an '
    'archived briefing were accurate to the sources available at the moment of publication.</div>'
    '</footer></div>' + STAMPJS + '</body></html>')

open(OUT, "w", encoding="utf-8").write(html)
print("gen_archive_1715: %d snapshots, %d days" % (total, len(days)))
