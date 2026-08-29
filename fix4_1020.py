# -*- coding: utf-8 -*-
"""Fourth fix pass, 10:20 AM edition.

FINAL-READ-THROUGH FINDING (validator missed it: it greps capital-U 'Undecided'):
the Champions Board note still ended "...none of the results above is affected by the
two undecided fights." There are ZERO undecided fights -- the co-main resolved at 8:46
and the main event at 9:15. It also duplicated the sentence immediately above it.

Plus: this run's source URLs added to all three footers (dedup-checked by the validator).
"""
import io, sys
fails = []
def edit(p, pairs):
    s = io.open(p, encoding='utf-8').read()
    for old, new, label in pairs:
        if s.count(old) != 1:
            fails.append("%s / %s: found %d" % (p, label, s.count(old))); continue
        s = s.replace(old, new)
    io.open(p, 'w', encoding='utf-8').write(s)

edit('mma-briefing.html', [(
    "\n<b>UFC Shanghai carries no title bout</b>, so no belt can move on it, and none of the results above is "
    "affected\nby the two undecided fights.",
    "\n<b>The card is complete at thirteen bouts with nothing left undecided</b>, and none of those results "
    "touches a belt.", "stale two-undecided-fights claim")])

SRC = {
 'mma-briefing.html': [
   ("https://www.sherdog.com/news/news/UFC-Shanghai-bonuses-Yadong-Song-3-others-earn-36100000-202571",
    "Sherdog &mdash; UFC Shanghai bonuses: Yadong Song, 3 others earn $100,000 (Aug 29, 2026)"),
 ],
 'cyber-briefing.html': [
   ("https://www.bleepingcomputer.com/news/security/atf-confirms-major-incident-after-recent-qilin-breach-claims/",
    "BleepingComputer &mdash; ATF confirms &ldquo;major incident&rdquo; after Qilin breach claims"),
   ("https://www.securityweek.com/atf-confirms-cyber-incident-after-ransomware-group-claims-attack/",
    "SecurityWeek &mdash; ATF confirms cyber incident after ransomware group claims attack"),
   ("https://cybernews.com/news/qilin-ransomware-bureau-alcohol-tobacco-firearms-atf-cyberattack/",
    "Cybernews &mdash; ATF confirms cyberattack; Qilin claims it"),
   ("https://www.bleepingcomputer.com/news/security/new-gputhor-attack-defeats-nvidia-ecc-protection-for-root-access/",
    "BleepingComputer &mdash; New GPUThor attack defeats NVIDIA ECC protection for root access"),
   ("https://thehackernews.com/2026/08/gputhor-rowhammer-defeats-ecc-on-nvidia.html",
    "The Hacker News &mdash; GPUThor Rowhammer defeats ECC on NVIDIA RTX A6000"),
   ("https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog",
    "CISA &mdash; Adds six Known Exploited Vulnerabilities to catalog, Aug 26 (fetched this run; empty body)"),
 ],
}
for p, items in SRC.items():
    s = io.open(p, encoding='utf-8').read()
    add = "".join('<a href="%s">%s</a><br>' % (u, t) for u, t in items if ('href="%s"' % u) not in s)
    key = '<b>Sources checked this run:</b><br>'
    if s.count(key) != 1:
        fails.append("%s: sources footer anchor not unique" % p); continue
    io.open(p, 'w', encoding='utf-8').write(s.replace(key, key + add))

if fails:
    print("FIX4 FAILURES:"); [print("  - "+f) for f in fails]; sys.exit(1)
print("fix4_1020.py: applied cleanly.")
