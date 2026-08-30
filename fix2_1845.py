#!/usr/bin/env python3
# Final read-through catch: the cross-check write-up described ESPN's return more narrowly than
# the return actually was ("six men's divisions it covered"), when it covered ten cells -- and the
# two stale ones were men's divisions printed under a "Women's Divisions" heading. Same error class
# the corrections file logs three times: a true finding described inaccurately.
import re, sys, io
REPO = sys.argv[1]
p = REPO + '/mma-briefing.html'
h = io.open(p, encoding='utf-8').read()

# --- tldr
old = ('ESPN&rsquo;s list matched on all <b>six men&rsquo;s divisions it covered</b> &mdash; Aspinall, Ulberg, '
       'Strickland, Makhachev, Gaethje, Volkanovski &mdash; but the same return carried <b>bantamweight as Merab '
       'Dvalishvili</b> and <b>flyweight as Alexandre Pantoja</b>, both superseded at <b>UFC 323 on December 6, 2025</b>. ')
new = ('ESPN&rsquo;s return covered <b>ten cells</b>: the <b>six under its own &ldquo;Men&rsquo;s Divisions&rdquo; '
       'heading</b> all matched &mdash; Aspinall, Ulberg, Strickland, Makhachev, Gaethje, Volkanovski &mdash; and so did '
       '<b>Harrison and Shevchenko</b>, but <b>two more, listed under a &ldquo;Women&rsquo;s Divisions&rdquo; heading that '
       'does not fit them, were the men&rsquo;s bantamweight and flyweight rows carrying Merab Dvalishvili and Alexandre '
       'Pantoja</b> &mdash; both superseded at <b>UFC 323 on December 6, 2025</b>. ')
assert h.count(old) == 1, 'tldr anchor'
h = h.replace(old, new, 1)

# --- body: "What matched"
old2 = 'Six cells, six matches.<br><br>'
new2 = ('Six cells, six matches. Two more matched as well, under the return&rsquo;s &ldquo;Women&rsquo;s Divisions&rdquo; '
        'heading and correctly placed there: <b>Kayla Harrison</b> (women&rsquo;s bantamweight, June 7 2025, submission in '
        'round two over Juliana Pe&ntilde;a at UFC 316, <b>0 defences</b> &mdash; the count this board carries) and '
        '<b>Valentina Shevchenko</b> (women&rsquo;s flyweight). <b>Eight of the ten cells the return contained were '
        'right.</b><br><br>')
assert h.count(old2) == 1, 'body anchor 1'
h = h.replace(old2, new2, 1)

# --- body: "What did not match"
old3 = ('&#9888; <b>What did not match, and why the board did not move.</b> The same return carried '
        '<b>bantamweight as Merab Dvalishvili</b> (September 14 2024, three defences) and <b>flyweight as Alexandre '
        'Pantoja</b> (July 8 2023, four defences).')
new3 = ('&#9888; <b>What did not match &mdash; and the mislabel is part of why it was easy to miss.</b> The same return '
        'carried <b>bantamweight as Merab Dvalishvili</b> (September 14 2024, three defences) and <b>flyweight as '
        'Alexandre Pantoja</b> (July 8 2023, four defences), <b>both printed under the &ldquo;Women&rsquo;s Divisions&rdquo; '
        'heading</b> &mdash; which they are not. A men&rsquo;s row filed under a women&rsquo;s heading is the kind of '
        'defect that makes a reader skim past the cell rather than compare it, and this page nearly did.')
assert h.count(old3) == 1, 'body anchor 2'
h = h.replace(old3, new3, 1)

# --- body: the uncovered-cells sentence was wrong (women's flyweight WAS covered)
old4 = ('The three cells ESPN did not cover this run &mdash; women&rsquo;s strawweight, and the interim '
        'heavyweight and women&rsquo;s flyweight notes &mdash; rest on the checks recorded beneath, as they have.')
new4 = ('&#9888; Corrected in the read-through: a first draft of this note said the return covered six cells and that '
        '<b>women&rsquo;s flyweight</b> was among those it did not. Both were wrong &mdash; it covered <b>ten</b>, and '
        'Shevchenko was in it. The cell it genuinely did not reach is <b>women&rsquo;s strawweight</b> '
        '(<b>Mackenzie Dern</b>, one defence), together with the <b>interim heavyweight</b> note '
        '(<b>Ciryl Gane</b>), and those rest on the checks recorded beneath as they have. '
        '<b>Describing a finding more narrowly than it is, is the same defect as describing it more broadly</b>, and this '
        'file has now logged the second direction as well as the first.')
assert h.count(old4) == 1, 'body anchor 3'
h = h.replace(old4, new4, 1)

io.open(p, 'w', encoding='utf-8').write(h)
print('cross-check write-up corrected: ten cells, eight matches, two stale men\'s rows mislabelled')
