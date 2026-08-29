#!/usr/bin/env python3
"""Targeted edits for the 12:35 PM ET Saturday Aug 29 2026 run (onto the 12:12 pages)."""
import io, sys, os

O = os.path.dirname(os.path.abspath(__file__))
FAIL = []

def rd(n):
    return io.open(os.path.join(O, n), encoding='utf-8').read()

def wr(n, s):
    io.open(os.path.join(O, n), 'w', encoding='utf-8').write(s)

def sub(h, old, new, label, count=1):
    if old not in h:
        FAIL.append('MISSING: ' + label)
        return h
    n = h.count(old)
    if count and n != count:
        FAIL.append('COUNT %d != %d: %s' % (n, count, label))
    return h.replace(old, new)

# ---------------------------------------------------------------- WALL STREET
ws = rd('wallstreet-briefing.html')

OLD_TENTH = ('re-verified a tenth time at 12:05 PM</b>. &#9888; <b>What that tenth check actually '
             'returned is narrower than the phrase suggests, so it is stated exactly:</b> a fresh '
             'search this run returned the <b>Dow level (53,560, &minus;9 points, &minus;0.02%)</b> '
             'and the <b>S&amp;P 500 and Nasdaq moves as percentages</b> (&ldquo;slid nearly '
             '0.3%&rdquo;, &ldquo;declined by 0.5%&rdquo;) &mdash; it did <b>not</b> restate the '
             'S&amp;P and Nasdaq index levels. Those two levels are <b>carried</b> from the editions '
             'that sourced them and are consistent with every percentage returned since. The three '
             'figures &mdash; <b>S&amp;P 500 7,711.76, &minus;0.25%</b>; <b>Nasdaq Composite '
             '26,402.42, &minus;0.52%</b>;\n<b>Dow Jones Industrial Average 53,559.99, &minus;9.45 '
             'points, &minus;0.02%</b>.</p>')

NEW_ELEVENTH = ('re-verified an eleventh time at 12:35 PM &mdash; and this check was the broad one '
                'the tenth was not</b>. &#9888; <b>Stated exactly, because the previous edition had '
                'to state its own narrowness:</b> the search run this hour returned <b>all three '
                'index levels and all three percentage moves together</b> &mdash; <b>S&amp;P 500 '
                '7,711.76, &minus;0.25%</b>; <b>Nasdaq Composite 26,402.42, &minus;0.52%</b>;\n'
                '<b>Dow Jones Industrial Average 53,559.99, &minus;9.45 points, &minus;0.02%</b> '
                '&mdash; alongside the weekly figures (<b>S&amp;P +0.5%</b>, <b>Nasdaq +0.9%</b>, '
                '<b>Dow +0.5%</b>). The S&amp;P 500 and Nasdaq <b>levels</b> were flagged as '
                '<b>carried</b> at 12:05 PM only because that hour&rsquo;s search returned their '
                'percentages and not their levels; <b>they are carried no longer</b>. Nothing in the '
                'numbers changed between the two checks &mdash; what changed is <b>which fields the '
                'check itself returned</b>, which is the whole of what a verification claim is '
                'entitled to assert.</p>')
ws = sub(ws, OLD_TENTH, NEW_ELEVENTH, 'WS lead tenth->eleventh')

OLD_WS_TLDR = ('the S&amp;P 500 slipped 0.25% to 7,711.76 and still finished the week higher, '
               're-verified a tenth time this run &mdash; and the pre-speech September rate reading, '
               'which had rested on a single mid-August report, is now corroborated by a second and '
               'differently sourced one:')
NEW_WS_TLDR = ('the S&amp;P 500 slipped 0.25% to 7,711.76 and still finished the week higher, '
               're-verified an eleventh time this run by a search that returned all three index '
               'levels and all three percentage moves together, so the S&amp;P and Nasdaq levels the '
               'previous edition had to flag as carried are carried no longer &mdash; and the '
               'pre-speech September rate reading, which had rested on a single mid-August report, '
               'is corroborated by a second and differently sourced one:')
ws = sub(ws, OLD_WS_TLDR, NEW_WS_TLDR, 'WS tldr', count=1)

# first-winning-week-in-three detail, sourced this run
OLD_WEEK = ("The week still finished green.")
NEW_WEEK = ("The week still finished green, and for the Dow it was the first one in three.")
ws = sub(ws, OLD_WEEK, NEW_WEEK, 'WS week line')

# --------------------------------------------------------------------- CYBER
cy = rd('cyber-briefing.html')

OLD_CY_REVIEW = ('CISA\'s framing: attackers are exploiting simple, known flaws that persist in '
                 'exposed assets, and AI is being\nused to automate that exploitation. The four aged '
                 'CVEs above &mdash; two from 2015 &mdash; are the argument\nmade in list form.</div>')
NEW_CY_REVIEW = ('CISA\'s framing: attackers are exploiting simple, known flaws that persist in '
                 'exposed assets, and AI is being\nused to automate that exploitation. The four aged '
                 'CVEs above &mdash; two from 2015 &mdash; are the argument\nmade in list form. '
                 '<b>New at 12:35 PM &mdash; the same review, reported this week, puts an age on the '
                 'problem rather than a volume.</b> Across the 2024&ndash;2025 records the most '
                 'common weakness classes were <b>injection flaws &mdash; cross-site scripting, OS '
                 'command injection and SQL injection</b> &mdash; with <b>improper input '
                 'validation</b> named the <b>single most common weakness type</b> across both the '
                 'KEV catalogue and registered CVEs, and <b>seven of the top ten weakness types in '
                 '2025</b> were ones already classed as <b>&ldquo;unforgivable&rdquo; in 2007</b>. '
                 'CISA&rsquo;s own conclusion is that this is <b>not a problem of technical '
                 'difficulty</b> but of <b>organisational culture, developer workflow and gaps in '
                 'Secure by Design practice</b>. &#9888; Read against the deadline board directly '
                 'above, that is not an abstraction: the <b>2015, 2019, 2021 and 2022</b> CVEs '
                 'sitting on it with federal due dates <b>are</b> the finding.</div>')
cy = sub(cy, OLD_CY_REVIEW, NEW_CY_REVIEW, 'CY CISA review extension')

OLD_CY_KEV = ('<div class="note"><b>What changed at 10:50 AM: nothing on this board.</b> All four '
              'countdowns are\nunchanged at <b>0 / 1 / 11 / 12</b> days and no CVE was added to or '
              'removed from the deadline list.')
NEW_CY_KEV = ('<div class="note"><b>Re-checked at 12:35 PM: nothing on this board changed.</b> A '
              'fresh search for August 2026 KEV additions again returned <b>no CISA alert dated '
              'later than August 26</b>, and all four countdowns are\nunchanged at <b>0 / 1 / 11 / '
              '12</b> days with no CVE added to or removed from the deadline list. The same search '
              'independently returned <b>August 28</b> as a due date under <b>BOD 26-04</b> for '
              'other catalogue entries, which is consistent with the per-CVE windows described below '
              'and with none of the four rows here. &#9888; As before: <b>no later alert was '
              'returned</b> is not the same as <b>CISA published none</b>.')
cy = sub(cy, OLD_CY_KEV, NEW_CY_KEV, 'CY KEV recheck')

OLD_CY_TLDR = ('which is the practical consequence of a breach that took contact details and nothing '
               'that can be cancelled.')
NEW_CY_TLDR = ('which is the practical consequence of a breach that took contact details and nothing '
               'that can be cancelled; and CISA&rsquo;s own 2024&ndash;25 review, reported this week, '
               'finds that seven of 2025&rsquo;s ten most common weakness types were already called '
               '&ldquo;unforgivable&rdquo; in 2007 &mdash; which is exactly what the 2015, 2019, 2021 '
               'and 2022 CVEs on this page&rsquo;s federal deadline board are.')
cy = sub(cy, OLD_CY_TLDR, NEW_CY_TLDR, 'CY tldr', count=1)

# ----------------------------------------------------------------------- MMA
mma = rd('mma-briefing.html')

OLD_MMA_PUNCH = ('the official method, <b>knockout (punch)</b>, remains the only description with a '
                 'primary source behind it.')
NEW_MMA_PUNCH = ('the official method, <b>knockout (punch)</b>, remains the only description with a '
                 'primary source behind it. <b>New at 12:35 PM &mdash; the outlet that supplied the '
                 'third name has now supplied a fourth, and it is its own.</b> A search run this hour '
                 'returns the <b>same national outlet</b> describing the finish as a <b>right-hand '
                 'uppercut</b>, where the report read at 11:35 AM from that outlet called it a '
                 '<b>short right hand</b>; a second outlet&rsquo;s headline this hour also calls it '
                 'an <b>uppercut</b>. &#9888; The point is not that the count has moved to two-two. '
                 'It is that <b>one publication renders the same punch two ways</b>, which is the '
                 'clearest evidence yet that these are <b>descriptions rather than findings</b>. '
                 'This page had already stopped counting; this is the reason it was right to.')
mma = sub(mma, OLD_MMA_PUNCH, NEW_MMA_PUNCH, 'MMA punch fourth name')

OLD_MMA_TLDR = ('which was rejected on its own wording before any source was consulted.')
NEW_MMA_TLDR = ('which was rejected on its own wording before any source was consulted; newly sourced '
                'this run, Song ran straight to <b>Jon Jones</b> at cageside to celebrate, and the '
                'outlet that gave the finishing punch a third name now gives it a fourth &mdash; the '
                'same publication calls it both a short right hand and a right-hand uppercut, which '
                'is why this page stopped counting names rather than tallying them.')
mma = sub(mma, OLD_MMA_TLDR, NEW_MMA_TLDR, 'MMA tldr', count=1)

# Jon Jones celebration detail into the post-fight item
OLD_MMA_LAP = ('Two accounts of the same moments are on the record and this page prints both. In one, '
               'Song ran a victory lap\ninside the cage and')
NEW_MMA_LAP = ('Two accounts of the same moments are on the record and this page prints both. '
               '<b>Newly sourced at 12:35 PM, and not in dispute:</b> the first thing Song did after '
               'the finish was <b>run straight to Jon Jones at cageside to celebrate</b> &mdash; '
               'stated by the national outlet\'s own report of the upset and echoed in a second '
               'account. In one, Song ran a victory lap\ninside the cage and')
mma = sub(mma, OLD_MMA_LAP, NEW_MMA_LAP, 'MMA Jon Jones detail')

wr('wallstreet-briefing.html', ws)
wr('cyber-briefing.html', cy)
wr('mma-briefing.html', mma)

# --------------------------------------------------------------- index mirror
ix = rd('index.html')
ix = sub(ix, OLD_WS_TLDR, NEW_WS_TLDR, 'INDEX ws mirror', count=1)
ix = sub(ix, OLD_CY_TLDR, NEW_CY_TLDR, 'INDEX cy mirror', count=1)
ix = sub(ix, OLD_MMA_TLDR, NEW_MMA_TLDR, 'INDEX mma mirror', count=1)
wr('index.html', ix)

# ---------------------------------------------------- static timestamp fallbacks
for name in ('index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html'):
    h = rd(name)
    if '12:05 PM ET' not in h:
        FAIL.append('MISSING timestamp fallback: ' + name)
    h = h.replace('12:05 PM ET', '12:35 PM ET')
    wr(name, h)

if FAIL:
    print('FAILURES:')
    for f in FAIL:
        print('  ' + f)
    sys.exit(1)
print('edits_1235.py OK')
