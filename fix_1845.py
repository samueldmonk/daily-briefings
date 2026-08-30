#!/usr/bin/env python3
# One real page defect exposed by validate_1845.py: the Weekly Scorecard's Nasdaq weekly cell
# carried +0.9% while The Lead carried +0.8% / +221.97. Reconcile and explain on the page.
import re, sys, io
REPO = sys.argv[1]
p = REPO + '/wallstreet-briefing.html'
h = io.open(p, encoding='utf-8').read()

# 1. The scorecard cell: print the split, not one side of it.
old = '<td>+0.5%</td><td>+0.9%</td>'
if old in h:
    new = '<td>+0.5%</td><td>+0.8% &nbsp;<span style="opacity:.7">(+0.9% in one rendering &mdash; see note)</span></td>'
    h = h.replace(old, new, 1)
    print('scorecard cell rewritten (exact form)')
else:
    # tolerant form: locate the weekly row and rewrite its Nasdaq cell
    m = re.search(r'(<tr>[^<]*<td[^>]*>\s*Week \(5 sessions\).*?</tr>)', h, re.S)
    assert m, 'weekly scorecard row not found'
    row = m.group(1)
    assert row.count('+0.9%') == 1, 'unexpected +0.9% count in weekly row: %d' % row.count('+0.9%')
    row2 = row.replace('+0.9%', '+0.8% &nbsp;<span style="opacity:.7">(+0.9% in one rendering &mdash; see note)</span>', 1)
    h = h.replace(row, row2, 1)
    print('scorecard cell rewritten (tolerant form)')

NOTE = ('<div class="note" style="margin-top:12px"><span class="tag crit">Corrected &middot; 6:45 PM</span> '
        '<b>This table and The Lead have been printing two different Nasdaq weekly figures, and the validation gate '
        'caught it rather than a source did.</b> The Lead carries <b>+0.8%, +221.97 points</b>; this table&rsquo;s weekly '
        'row carried <b>+0.9%</b>. Both are sourced &mdash; and the arithmetic settles which one this page should lead '
        'with. Against Friday&rsquo;s verified close, <b>221.97 / 26,402.42 = 0.8407%</b>, and against the prior week&rsquo;s '
        'corroborated <b>26,180.45</b> it is <b>0.8478%</b>. <b>Either way it rounds to +0.8%</b>, so that is the figure '
        'this table now carries, with the <b>+0.9%</b> rendering printed beside it rather than deleted. '
        '&#9888; <b>The point worth keeping is not which rounding won.</b> It is that a page can hold a contradiction '
        'between its prose and its own table for a full edition without any source disagreeing with it &mdash; '
        '<b>this one was internal, and only an arithmetic check on the page against itself was going to find it.</b>'
        '</div>')
m = re.search(r'(<h2 class="sec">Weekly Scorecard.*?</table>)', h, re.S)
assert m, 'scorecard table not found'
h = h[:m.end()] + NOTE + h[m.end():]
io.open(p, 'w', encoding='utf-8').write(h)

# arithmetic assertions for the note's own figures
assert abs(221.97/26402.42*100 - 0.8407) < 5e-4
assert abs(221.97/26180.45*100 - 0.8478) < 5e-4
print('scorecard note added; both percentage identities asserted')
