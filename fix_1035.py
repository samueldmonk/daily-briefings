#!/usr/bin/env python3
"""Read-through fixes for the 2026-09-02 ~10:52 AM edition. Every edit below corrects a defect
the line-by-line read found, not a guard raise."""
import os, sys
OUT = "/sessions/wizardly-compassionate-cerf/mnt/outputs"

def ed(fn, pairs):
    p = os.path.join(OUT, fn)
    s = open(p).read()
    for old, new in pairs:
        if old not in s:
            print("MISS in %s: %r" % (fn, old[:80])); sys.exit(1)
        if s.count(old) != 1:
            print("AMBIG in %s (%d): %r" % (fn, s.count(old), old[:80])); sys.exit(1)
        s = s.replace(old, new)
    open(p, "w").write(s)
    print("patched", fn, len(pairs))

PROV_OLD = 'Provenance: where an item below says &ldquo;this run,&rdquo;'
PROV_NEW = 'Provenance: where an item on this page says &ldquo;this run,&rdquo;'

# ---------------------------------------------------------------- WALL STREET
ed("wallstreet-briefing.html", [
    # W7: the Dow does not lead the board - the Russell does. Headline narrowed to the big three.
    ('as of ~10:35 AM ET, '
     'the Dow leads a narrowly positive open while the 10-year touches its highest since November 2023',
     'as of ~10:35 AM ET, '
     'the Dow leads the big three while the Russell 2000 swings hardest and the 10-year touches its '
     'highest since November 2023'),

    # W1 + W2: "a fifth of that" was wrong arithmetic (0.16 is a twelfth of 1.98, not a fifth), and
    # the superlative was asserted rather than shown.
    ('<b>The Russell is the largest index swing on this page and nothing '
     'fetched explains it.</b> It was down 1.23% at 9:35 and up 0.75% an hour later &mdash; a roughly '
     'two-percentage-point reversal inside one hour, while the Dow moved a fifth of that. No source '
     'offers a cause and none is invented here; the divergence is recorded as an observation, not a '
     'causal claim.',
     '<b>The Russell 2000 is the largest index swing on this page and nothing fetched explains it.</b> '
     'It was down 1.23% at 9:35 and up 0.75% an hour later. Set against the other three across the same '
     'two reads &mdash; Dow +0.37% to +0.53%, S&amp;P 500 +0.06% to +0.20%, Nasdaq Composite −0.06% to '
     '+0.03% &mdash; the small-cap index travelled about 1.98 percentage points while the widest of the '
     'other three moved 0.16. That is roughly twelve times the Dow’s distance, and it is this desk’s '
     'subtraction across two clocked reads, not a claim any source makes. No source offers a cause and '
     'none is invented here; the divergence is recorded as an observation, not a causal claim.'),

    # W5: single-name and commodity levels for Wednesday DO appear on this page. Only INDEX levels do not.
    ('so no Wednesday level appears anywhere on this page as a completed figure',
     'so no Wednesday <b>index</b> level appears anywhere on this page as a completed figure '
     '(single-name and commodity reads do appear, each with its clock attached)'),

    # W3: only the post-open pair backs out to a close; the premarket figure is a bare percentage.
    ('<p class="note" style="margin-bottom:0">Both reads back out to a Tuesday close of $434.21; the gap '
     'between them is a clock, not a dispute.</p>',
     '<p class="note" style="margin-bottom:0">The post-open pair backs out to a Tuesday close of $434.21. '
     'The premarket figure is a bare percentage with no level attached, so it cannot be reconciled the '
     'same way &mdash; the two are printed side by side as different windows, not cross-checked against '
     'each other.</p>'),

    # W4: the superlative was falsified by a number elsewhere on the same page - GitLab's premarket +21%.
    ('Credo holds this slot on the arithmetic, not on the story: at −17.51% it is the '
     'largest single-name move on this page, ahead of MongoDB (−12.89%), Palo Alto Networks (−9.35%) and Dell '
     '(+6.17%). That ranking is this desk’s comparison across figures from one quote board read at one time, not a claim '
     'any source makes.',
     'Credo holds this slot on the arithmetic, not on the story: at −17.51% it is the largest '
     '<b>post-open</b> single-name move on this page, ahead of MongoDB (−12.89%), Palo Alto Networks '
     '(−9.35%) and Dell (+6.17%) on the same quote board at the same time. <b>The qualifier is load-bearing: '
     'GitLab’s premarket +21% is a larger magnitude than Credo’s −17.51%</b>, and this slot is not '
     'awarded to it, because a premarket print and a post-open print are not the same measurement and no '
     'post-open GitLab quote was fetched this run. The ranking is this desk’s comparison across one '
     'board read at one time, not a claim any source makes.'),

    (PROV_OLD, PROV_NEW),
])

# ---------------------------------------------------------------- CYBER
ed("cyber-briefing.html", [
    # C10 + C11: two details carried from an earlier sourced edition were reading as fresh confirmations.
    ('The September pair’s '
     'fixes are hotfix 12.4.3-03526 / 12.5.0-02952 or higher, and SSL-VPN on firewalls and the SMA100 line are not affected.',
     'For the September pair, an <b>earlier edition today</b> recorded the fixes as hotfix '
     '12.4.3-03526 / 12.5.0-02952 or higher, with SSL-VPN on firewalls and the SMA100 line unaffected; '
     '<b>those two details were not re-fetched in this run’s searches</b> and are carried with that label '
     'rather than presented as fresh confirmation. The July fixed versions above <i>were</i> read from the '
     'vendor-linked advisory this run.'),

    (PROV_OLD, PROV_NEW),
])

# ---------------------------------------------------------------- MMA
ed("mma-briefing.html", [
    # M2: Sept 2 to Sept 5 is three days, not four.
    ('Four days out from a main event in which he is a substantial underdog.',
     'Three days out from a main event in which he is a substantial underdog.'),

    # M4: no source fetched this run calls UFC 331 a title fight; the tag asserted it.
    ('<div class="tags"><span class="tag t-a">Title fight</span></div>',
     '<div class="tags"><span class="tag t-a">Main event</span></div>'),
    ('Flyweight champion Joshua Van rematches Alexandre Pantoja, the man he took the belt from. Main card at 9 PM ET / '
     '6 PM PT on Paramount+.',
     'Flyweight champion Joshua Van rematches Alexandre Pantoja, the man he took the belt from. Main card '
     'at 9 PM ET / 6 PM PT on Paramount+. <b>Nothing fetched this run explicitly bills the bout as a title '
     'fight</b>, so this page does not call it one &mdash; the reigning champion meeting the former champion '
     'in the main event of a numbered card is what the listings support, and the inference beyond that is '
     'left to the reader.'),

    # M6: "a sixth contract" was an inference; the 22-year-old may well be one of the five named above.
    ('<li><b>A sixth contract, separately reported.</b> Sherdog, September 2: &ldquo;Dana White hands UFC deal to 22-year-old '
     'following controversial 15-second KO.&rdquo; The fighter is not named in the headline and the card is not identified, '
     'so neither is supplied here.</li>',
     '<li><b>Another contract, and this desk will not number it.</b> Sherdog, September 2: &ldquo;Dana White '
     'hands UFC deal to 22-year-old following controversial 15-second KO.&rdquo; The fighter is not named in '
     'the headline and the card is not identified. An earlier draft of this item called it &ldquo;a sixth '
     'contract&rdquo; &mdash; <b>that was an inference, and a bad one</b>: the 22-year-old could perfectly '
     'well be one of the five named under Prospect Watch above, and nothing fetched this run says otherwise.</li>'),

    # M7: label the count as derived from the list printed directly above it.
    ('<h3>Adam Livingston</h3><p>Split decision over Hunter Smith &mdash; the only bout of the five to reach the scorecards.</p>',
     '<h3>Adam Livingston</h3><p>Split decision over Hunter Smith &mdash; the only one of the five results '
     'printed here to reach the scorecards, which is this desk’s reading of the four cards beside it rather '
     'than a claim any source makes.</p>'),

    (PROV_OLD, PROV_NEW),
])
