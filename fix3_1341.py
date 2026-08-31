#!/usr/bin/env python3
"""Third pass. Two real page defects:
(a) the Paris odds paragraph written this run called two prices 'more renderings'
    when this page already carries both -- they are re-confirmations, and the
    carried set is five prices, not four;
(b) edition references with no AM/PM ('the 8:19 edition', '(11:05)') survived the
    stamp scrub, which keys on AM/PM, and still read as this morning."""
import io, re

# ---------------------------------------------------------------- (a) odds
p = 'mma-briefing.html'
h = io.open(p, encoding='utf-8').read()
OLD = ('&#9888; <b>Paris odds refreshed, and for the first time this session nothing lands outside the band '
'already carried.</b> Two more renderings for <b>September 5, Accor Arena</b>: <b>BetWay at Parnasse &minus;400 / '
'Hooker +300</b>, and a <b>consensus line at Parnasse &minus;428 / Hooker +292</b>. '
'<b>Both sit inside the carried range of Parnasse &minus;400 to &minus;550 and Hooker +292 to +400</b>; '
'<b>the range is unchanged and no figure is adopted as the line.</b>')
NEW = ('&#9888; <b>Paris odds came back and not one number in them is new, which is the finding.</b> The sweep for '
'<b>September 5, Accor Arena</b> returned <b>BetWay at Parnasse &minus;400 / Hooker +300</b> and a '
'<b>consensus line at Parnasse &minus;428 / Hooker +292</b>. <b>This page already carries both pairs</b>, alongside '
'the promotion&rsquo;s own <b>&minus;500 / +375</b>, the opener at <b>&minus;357 / +275</b> and the '
'<b>&minus;550 / +400</b> recorded earlier. <b>Five prices on the favourite &mdash; &minus;357, &minus;400, '
'&minus;428, &minus;500, &minus;550 &mdash; and a re-return of two of them is a re-confirmation, not a sixth.</b> '
'&#9888; <b>The spread is why none is adopted:</b> &minus;357 and &minus;550 are not the same bet, and a price that '
'keeps being republished is not thereby the price. <b>The published range is unchanged.</b>')
assert OLD in h, 'odds paragraph not found'
h = h.replace(OLD, NEW, 1)

# ---------------------------------------------------------------- (b) stamps
h = h.replace('stale names (10:50), full agreement (11:05), agreement plus a false vacancy (11:35), '
              'and agreement plus a self-contradicting two-division claim (12:05)',
              'stale names, then full agreement, then agreement plus a false vacancy, then agreement '
              'plus a self-contradicting two-division claim')
h = re.sub(r'the 8:19 and 8:46 editions', 'earlier editions', h)
h = re.sub(r'(?:in |since )?the (\d{1,2}:\d{2}) edition',
           lambda m: 'an earlier edition', h)
io.open(p, 'w', encoding='utf-8').write(h)
print('mma fixed')

for q in ['wallstreet-briefing.html', 'cyber-briefing.html']:
    g = io.open(q, encoding='utf-8').read()
    g = re.sub(r'the (\d{1,2}:\d{2}) edition', 'an earlier edition', g)
    g = re.sub(r'the (\d{1,2}:\d{2}) and (\d{1,2}:\d{2}) editions', 'earlier editions', g)
    g = g.replace('since an earlier edition and is repeated', 'in an earlier edition and is repeated')
    io.open(q, 'w', encoding='utf-8').write(g)
    print('stamps fixed', q)
