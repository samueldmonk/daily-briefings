#!/usr/bin/env python3
"""A carried odds block still said 'this run', so a price fetched days ago read as
fetched now, and its '(three books)' summary predates two later prices."""
import io
p = 'mma-briefing.html'
h = io.open(p, encoding='utf-8').read()
old = 'A sportsbook quoted in reporting this run has <b>Parnasse &minus;400, Hooker +300</b>'
new = ('A sportsbook quoted in the reporting of an earlier edition had <b>Parnasse &minus;400, Hooker +300</b>')
assert old in h, 'odds sentence not found'
h = h.replace(old, new, 1)
old2 = '<b>Odds: Parnasse &minus;400 to &minus;500 / Hooker +292 to +375 (three books).</b>'
new2 = ('<b>Odds: Parnasse &minus;400 to &minus;500 / Hooker +292 to +375 (three books at the time).</b> '
        '&#9888; <b>Two further prices, &minus;357 and &minus;550, have been recorded since; no line is adopted.</b>')
assert old2 in h, 'odds range line not found'
h = h.replace(old2, new2, 1)
io.open(p, 'w', encoding='utf-8').write(h)
print('carried odds block de-staled')
