# -*- coding: utf-8 -*-
"""Third fix pass -- the two replacements fix2 could not match because the source
strings wrap across newlines. Same two findings, matched against the real markup."""
import io, sys
fails = []
def edit(p, pairs):
    s = io.open(p, encoding='utf-8').read()
    for old, new, label in pairs:
        if s.count(old) != 1:
            fails.append("%s / %s: found %d" % (p, label, s.count(old))); continue
        s = s.replace(old, new)
    io.open(p, 'w', encoding='utf-8').write(s)

edit('wallstreet-briefing.html', [(
    " Those figures were re-confirmed\nagainst a fresh search this morning rather than carried on trust.",
    "", "redundant re-confirmation sentence")])

edit('mma-briefing.html', [(
    " The same report puts the card at <b>ten finishes</b>, which is the count this page has carried, "
    "and calls it the promotion&rsquo;s <b>third visit to the venue</b>.",
    " The same report independently puts the card at <b>ten finishes</b>, which is the count this page "
    "has carried.", "third-visit claim dropped")])

if fails:
    print("FIX3 FAILURES:"); [print("  - "+f) for f in fails]; sys.exit(1)
print("fix3_1020.py: applied cleanly.")
