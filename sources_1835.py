#!/usr/bin/env python3
import io, os, sys
OUT = "/sessions/epic-cool-pasteur/mnt/outputs"
fails = []

def edit(fn, old, new, tag):
    p = os.path.join(OUT, fn)
    s = io.open(p, encoding="utf-8").read()
    if s.count(old) != 1:
        fails.append("%s: %s (count=%d)" % (fn, tag, s.count(old)))
        return
    io.open(p, "w", encoding="utf-8").write(s.replace(old, new, 1))

# --- MMA: add the live-blog source that carries the two official decisions
edit("mma-briefing.html",
 '<li><a href="https://sports.yahoo.com/articles/ufc-sacramento-results-hernandez-vs-100000198.html">Yahoo Sports / MMA Fighting — UFC Sacramento results: Hernandez vs. Rodrigues</a></li>',
 '<li><a href="https://sports.yahoo.com/articles/ufc-sacramento-results-hernandez-vs-100000198.html">Yahoo Sports / MMA Fighting — UFC Sacramento results: Hernandez vs. Rodrigues</a></li>\n'
 '<li><a href="https://sports.yahoo.com/articles/ufc-sacramento-live-results-highlights-204500063.html">MMA Mania / SB Nation via Yahoo Sports — UFC Sacramento live results, highlights and play-by-play (source of the two official decisions)</a></li>\n'
 '<li><a href="https://www.ufc.com/news/ufc-sacramento-hernandez-vs-rodrigues-prelim-results">UFC.com — Prelim Results | UFC Sacramento</a></li>\n'
 '<li><a href="https://www.si.com/fannation/mma/news/ufc-sacramento-free-live-stream-results-highlights-for-hernandez-vs-rodrigues">Sports Illustrated / MMA Knockout — UFC Sacramento live results &amp; highlights</a></li>',
 "mma sources")

# --- CYBER: Ray KEV + Baxter
edit("cyber-briefing.html",
 '<li><a href="https://thehackernews.com/2026/08/gitlab-cve-2026-19478-comes-under.html">The Hacker News — GitLab CVE-2026-19478 comes under active exploitation</a></li>',
 '<li><a href="https://thehackernews.com/2026/08/gitlab-cve-2026-19478-comes-under.html">The Hacker News — GitLab CVE-2026-19478 comes under active exploitation</a></li>\n'
 '<li><a href="https://thehackernews.com/2026/08/cisa-flags-actively-exploited-ray-flaw.html">The Hacker News — CISA flags actively exploited Ray flaw that can trigger browser-based RCE</a></li>\n'
 '<li><a href="https://www.cisa.gov/news-events/alerts/2026/08/17/cisa-adds-one-known-exploited-vulnerability-catalog">CISA — Adds one known exploited vulnerability to catalog (Aug 17, 2026)</a></li>\n'
 '<li><a href="https://www.govinfosecurity.com/shinyhunters-leaks-71-million-baxter-international-records-a-32630">GovInfoSecurity — ShinyHunters leaks 7.1 million Baxter International records</a></li>',
 "cyber sources")

# --- WALL STREET: CNBC yields
p = os.path.join(OUT, "wallstreet-briefing.html")
s = io.open(p, encoding="utf-8").read()
if 'cnbc.com/2026/08/20/stock-market-today-live-updates.html' not in s:
    marker = '<div class="lab">Sources</div>\n<ul>\n'
    if s.count(marker) == 1:
        s = s.replace(marker, marker +
            '<li><a href="https://www.cnbc.com/2026/08/20/stock-market-today-live-updates.html">CNBC — Stock market news for Aug. 21, 2026 (10-year 4.737%, 30-year 5.276%)</a></li>\n', 1)
        io.open(p, "w", encoding="utf-8").write(s)
    else:
        fails.append("ws sources marker count=%d" % s.count(marker))

if fails:
    print("FAILURES:"); [print("  " + f) for f in fails]; sys.exit(1)
print("sources added")
