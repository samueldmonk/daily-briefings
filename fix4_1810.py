#!/usr/bin/env python3
"""One job: make the defence-count claim true rather than approximately true.

The 6:10 PM champions note said ESPN's defence counts "matched what this board carries,
including ... Van at one". The board's flyweight and bantamweight rows carried NO defence count
at all, so there was nothing there to match -- the claim was about cells that did not exist.
Two fixes, in this order: put the counts ESPN returned into the two rows that lacked them
(both corroborated by the standing corrections file), then narrow the sentence to say what was
actually compared.
"""
import io, sys
REPO = sys.argv[1]
p = REPO + '/mma-briefing.html'
h = io.open(p, encoding='utf-8').read()
n = 0

def sub(old, new, label):
    global h, n
    assert h.count(old) == 1, ('ANCHOR %s: %d hits' % (label, h.count(old)))
    h = h.replace(old, new)
    n += 1

# 1. bantamweight row gains the count ESPN returned (0 defences)
sub('UD over Merab Dvalishvili, UFC 323, Dec 6, 2025',
    'UD over Merab Dvalishvili, UFC 323, Dec 6, 2025; 0 defences',
    'yan-row')

# 2. flyweight row gains the defence it has always had in the corrections file but never showed
sub('TKO1 (0:26) Alexandre Pantoja, UFC 323, Dec 2025; defends in the rematch at UFC 331',
    'TKO1 (0:26) Alexandre Pantoja, UFC 323, Dec 2025; 1 defence '
    '(TKO5 Tatsuro Taira, UFC 328, May 9, 2026); defends in the rematch at UFC 331',
    'van-row')

# 3. narrow the claim in the note
sub('<b>Title dates and defence counts both matched</b> what this '
    'board carries, including the two counts this page has had to defend before &mdash; '
    'Makhachev at <b>one</b> defence and Van at <b>one</b>.',
    '<b>Every title date matched</b> what this board carries. On defences the comparison was '
    'narrower than that sentence would suggest in an earlier draft, and the difference is worth '
    'stating: six of the eight rows already carried a count and <b>all six agreed</b> &mdash; '
    'including <b>Makhachev at one</b>, which this page has had to defend before. &#9888; <b>The '
    'bantamweight and flyweight rows carried no defence count at all</b>, so there was nothing in '
    'them to match; ESPN returned <b>Yan at 0</b> and <b>Van at 1</b>, both of which agree with '
    'the standing record (Van&rsquo;s being the TKO5 of Tatsuro Taira at UFC 328), and <b>both '
    'have now been written into the two rows</b>. The board is more complete than it was an hour '
    'ago because a claim about it turned out to be checking cells that did not exist.',
    'note-defences')

io.open(p, 'w', encoding='utf-8').write(h)
print('champions defence-count fixes:', n)
