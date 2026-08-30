# -*- coding: utf-8 -*-
import io, re
def rd(f): return io.open(f,encoding="utf-8").read()
def wr(f,s): io.open(f,"w",encoding="utf-8").write(s)

# remove ONLY the duplicate <a> blocks I added this run, keeping the pre-existing ones
DUPS = {
 "cyber-briefing.html": ["https://www.cnbc.com/2026/08/27/ai-cyber-defense-letter.html",
   "https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog"],
 "wallstreet-briefing.html": ["https://www.cnbc.com/2026/08/27/stock-market-today-live-updates.html"],
 "mma-briefing.html": ["https://sports.yahoo.com/articles/song-yadong-lands-unbelievable-knockout-130811359.html"],
}
for f, urls in DUPS.items():
    s = rd(f); j = s.find("<footer"); head, foot = s[:j], s[j:]
    for u in urls:
        # drop the FIRST occurrence's whole anchor (+ trailing <br>), keep the later original
        pat = re.compile(r'<a href="%s">.*?</a>(<br>)?\s*' % re.escape(u), re.S)
        ms = list(pat.finditer(foot))
        assert len(ms) == 2, "%s expected 2 anchors for %s, got %d" % (f, u, len(ms))
        foot = foot[:ms[0].start()] + foot[ms[0].end():]
    s = head + foot
    hrefs = re.findall(r'href="(http[^"]+)"', s[s.find("<footer"):])
    assert len(hrefs) == len(set(hrefs)), "%s still duplicated" % f
    wr(f, s)
print("DEDUPE OK")
