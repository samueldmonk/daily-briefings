#!/usr/bin/env python3
"""Sync index.html cards to the three tldrs, then restamp all four pages from the clock."""
import re, datetime, zoneinfo

D = "/sessions/serene-vigilant-hypatia/mnt/outputs/"
FILES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
NOW = datetime.datetime.now(zoneinfo.ZoneInfo("America/New_York"))
STAMP = NOW.strftime("%-I:%M %p")
h = NOW.hour
EDITION = "Morning Edition" if h < 11 else ("Midday Edition" if h < 15 else "Afternoon Edition")
DATESTR = NOW.strftime("%A, %B %-d, %Y")
fails = []

# 1. pull the three tldr sentences
tldr = {}
for f, label in [("cyber-briefing.html", "The Wire"),
                 ("wallstreet-briefing.html", "The Tape"),
                 ("mma-briefing.html", "Tale of the Tape")]:
    s = open(D + f, encoding="utf-8").read()
    m = re.search(r'<div class="tldr"><b>' + re.escape(label) + r'</b>\s*<span>(.*?)</span></div>', s, re.S)
    if m:
        tldr[f] = m.group(1).strip()
    else:
        fails.append("tldr not found: " + f)

# 2. write them into the index cards (each card links to its page)
idx = open(D + "index.html", encoding="utf-8").read()
for f in ("cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    if f not in tldr:
        continue
    # find the card containing the href and replace its <p class="cardsum"> / summary <p>
    pat = re.compile(r'(<a[^>]*href="' + re.escape(f) + r'"[^>]*class="card[^"]*"[^>]*>.*?<p[^>]*>)(.*?)(</p>)', re.S)
    m = pat.search(idx)
    if not m:
        pat = re.compile(r'(<div class="card[^"]*"[^>]*>(?:(?!</div>).)*?<p[^>]*>)(.*?)(</p>(?:(?!<div class="card).)*?href="' + re.escape(f) + r'")', re.S)
        m = pat.search(idx)
    if m:
        idx = idx[:m.start(2)] + tldr[f] + idx[m.end(2):]
    else:
        fails.append("index card not matched: " + f)
open(D + "index.html", "w", encoding="utf-8").write(idx)

# 3. restamp every page: masthead fallbacks + freshline
STALE = ["2:47 PM", "2:39 PM ET", "2:14 PM", "2:11 PM", "1:09 PM", "1:08 PM"]
for f in FILES:
    s = open(D + f, encoding="utf-8").read()
    s = re.sub(r'(id="updated"[^>]*>)[^<]*(</span>)', r'\g<1>' + STAMP + ' ET\g<2>', s)
    s = re.sub(r'(id="datestamp"[^>]*>)[^<]*(</span>)', r'\g<1>' + DATESTR + r'\g<2>', s)
    s = re.sub(r'(id="edition"[^>]*>)[^<]*(</span>)', r'\g<1>' + EDITION + r'\g<2>', s)
    s = re.sub(r'(id="freshline"[^>]*>).*?(</div>)',
               r'\g<1>Data as of ' + STAMP +
               ' ET &middot; briefings refresh every 30 minutes, 8 AM&ndash;6 PM ET\g<2>', s, flags=re.S)
    open(D + f, "w", encoding="utf-8").write(s)

print("STAMP:", STAMP, "| EDITION:", EDITION, "|", DATESTR)
print("FAILURES:", fails if fails else "none")
