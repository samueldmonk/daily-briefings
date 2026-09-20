# -*- coding: utf-8 -*-
"""Read-through repairs, run 7 (2026-09-20 evening)."""
import io

R = {
 "mma-briefing.html": [
   # (a) article agreement in the top-story headline
   ("UFC 331 turns out to have been a $8.3 million night",
    "UFC 331 turns out to have been an $8.3 million night"),
   # (e) an unsourced descriptor for Rosas Jr.
   ("<p>Headlines his own Fight Night on 26 September as a <b>&minus;1011 favourite</b> over Raoni "
    "Barcelos &mdash; a price that puts a former youngest-fighter-on-the-roster curiosity squarely "
    "in main-event company on recent form.</p>",
    "<p>Headlines his own Fight Night on 26 September as a <b>&minus;1011 favourite</b> over Raoni "
    "Barcelos, with the source reporting the line describing <b>heavy money landing on Rosas</b> "
    "&mdash; a price gap it reads as the market siding with youth and recent wins over veteran "
    "form and experience.</p>"),
 ],
 "cyber-briefing.html": [
   # (b) the banner counted two overdue Cisco flaws while the KEV section lists three
   ("<span style=\"font-size:14.5px\">Two Cisco zero-days confirmed exploited in the wild are "
    "past their federal remediation deadlines &mdash; a CVSS 10.0 authentication bypass in "
    "Identity Services Engine by one day, and a CVSS 9.8 root-execution flaw in Secure Email "
    "Gateway by three &mdash; while",
    "<span style=\"font-size:14.5px\">Three Cisco flaws confirmed exploited in the wild are "
    "past their federal remediation deadlines &mdash; a CVSS 10.0 authentication bypass in "
    "Identity Services Engine by one day, a CVSS 9.8 root-execution flaw in Secure Email "
    "Gateway by three, and a CVSS 10.0 Secure Firewall Management Center bypass by eight "
    "&mdash; while"),
   # (c) miscount in the spotlight card
   ("<p>The extortion crew turns up three times in this briefing, which is the story in itself.",
    "<p>The extortion crew turns up twice in this briefing, which is the story in itself."),
 ],
 "wallstreet-briefing.html": [
   # (d) a fifth COIN reading surfaced this run and was not named
   ("Closing level: <b>$194.23</b> per the source that states it, against a <b>$194.25</b> "
    "reading carried from an earlier edition.</p>",
    "Closing level: <b>$194.23</b> per the source that states it, against a <b>$194.25</b> "
    "reading carried from an earlier edition. A <b>+6.55%</b> reading of the same session also "
    "surfaced this run; it sits far outside the cluster above and is not adopted.</p>"),
 ],
}

for path, subs in R.items():
    h = io.open(path, encoding="utf-8").read()
    for old, new in subs:
        assert h.count(old) == 1, (path, old[:70], h.count(old))
        h = h.replace(old, new)
    io.open(path, "w", encoding="utf-8").write(h)
    print("repaired", path, len(subs))
