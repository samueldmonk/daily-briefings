#!/usr/bin/env python3
"""One job: carry the corrections found in the final read-through.

1. WS ordinal clash. The new lead called the Russell 2000 "the fourth index", but the 4:06 PM
   block on the SAME page already calls the Nasdaq 100 "a fourth Friday index figure". Two
   different fourths on one page is a contradiction the validator cannot see.
2. WS unverifiable page-history claim ("the first time it has bitten an index rather than a
   single stock") -- nothing fetched this run establishes what the rule has previously bitten.
3. MMA "four books". The four renderings are a named book (BetWay), a consensus line, the
   UFC's own listing and an odds aggregator's opener. A consensus is not a book and neither is
   a promotion's event page.
4. MMA overclaim of provenance. "Refuted by everything else fetched this run" listed the
   consensus line, which was NOT fetched this run -- it is carried from an earlier edition.
   Same error class as the "same search" slip logged at 5:48 PM: a true finding described more
   broadly than the evidence supports.
5. MMA "sits below" is ambiguous for negative odds (-357 is numerically above -400 but is the
   longer price). Stated as price length instead.
"""
import io, sys
REPO = sys.argv[1]
n = 0

def sub(f, old, new, label):
    global n
    p = REPO + '/' + f
    h = io.open(p, encoding='utf-8').read()
    assert h.count(old) == 1, ('ANCHOR %s: %d hits' % (label, h.count(old)))
    io.open(p, 'w', encoding='utf-8').write(h.replace(old, new))
    n += 1

# 1 + 2 -- wall street
sub('wallstreet-briefing.html',
    '<b>The week finally has numbers rather than adjectives &mdash; and the fourth index that '
    'arrives with them is the one that will not reconcile.</b>',
    '<b>The week finally has numbers rather than adjectives &mdash; and the small-cap index that '
    'arrives with them is the one that will not reconcile.</b> &#9888; <b>It is not the '
    '&ldquo;fourth index figure&rdquo; recorded at 4:06 PM below</b>, which was the Nasdaq 100; '
    'this is a different index arriving for a different reason, and the two are not the same '
    'item counted twice.',
    'ws-ordinal')

sub('wallstreet-briefing.html',
    '<b>The rule exists for exactly this case, and this is the first time it has bitten an index '
    'rather than a single stock.</b>',
    '<b>The rule exists for exactly this case.</b>',
    'ws-history-claim')

# 3 + 4 + 5 -- mma
sub('mma-briefing.html',
    'That is a price this page has not carried, and it sits <b>below all three of the lines '
    'already here</b> (&minus;400, &minus;428, &minus;500).',
    'That is a price this page has not carried, and it is the <b>longest of the four prices on '
    'Parnasse</b> &mdash; the shortest money he is asked for &mdash; against the <b>&minus;400, '
    '&minus;428 and &minus;500</b> already here.',
    'mma-below')

sub('mma-briefing.html',
    'If they are not, four books simply disagree by 143 points on the favourite.',
    'If they are not, four renderings simply disagree by <b>143 points</b> on the favourite '
    '(&minus;357 to &minus;500) &mdash; and &#9888; <b>they are four renderings and not four '
    'books</b>: one is a named sportsbook, one a consensus, one the promotion&rsquo;s own event '
    'listing and one an odds aggregator&rsquo;s opener. <b>Adding the opener widens the spread '
    'rather than narrowing it</b>, from the 100 points this page reported at 1:08 PM to 143.',
    'mma-four-books')

sub('mma-briefing.html',
    'It is refuted by everything else fetched this run: the BetWay line, the consensus line and '
    'the FightOdds.io opener all price <b>Parnasse</b> as the favourite,',
    'It is refuted by <b>both lines actually fetched this run</b> &mdash; the <b>BetWay</b> price '
    'and the <b>FightOdds.io</b> opener, which both make <b>Parnasse</b> the favourite &mdash; '
    'and it is inconsistent with the <b>consensus line this page already carried</b>, which is a '
    'weaker and separate thing, because that line was not re-fetched today;',
    'mma-provenance')

print('read-through corrections applied:', n)
