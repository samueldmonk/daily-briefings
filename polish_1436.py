# -*- coding: utf-8 -*-
"""Edition 2026-09-07-1436: read-through corrections found by hand."""
import sys, os, re
REPO = sys.argv[1]
P = lambda n: os.path.join(REPO, n)
rep = []
def fix(f, old, new, tag):
    h = open(P(f), encoding="utf-8").read()
    if old not in h:
        rep.append("MISS  " + tag); return
    rep.append("ok    %s (x%d)" % (tag, h.count(old)))
    open(P(f), "w", encoding="utf-8").write(h.replace(old, new))

# (a) MMA: stale per-page New-tag sentence naming the 10 October card.
fix("mma-briefing.html",
 'This page does carry one New tag the 1:45 edition, and it is on the 10&nbsp;October Las Vegas card below, '
 'which was absent from <code>archive/mma-2026-09-07-1313.html</code>.',
 'This page carries <b>two</b> New tags this edition and neither is a schedule change: the <b>Roberto Soldic signing</b> and the '
 '<b>first bout booked for UFC&nbsp;334</b>, both above. Each was absent from <code>archive/mma-2026-09-07-1419.html</code>. '
 'The 10&nbsp;October Las Vegas card, tagged New in the 1:45 edition, now reads <b>Carried</b>.',
 "mma stale new-tag sentence")

# (b) MMA: the two new cards are roster news, not fight-week cards; say so where
#     the Fight Week section opens so the ordering is not read as a schedule claim.
fix("mma-briefing.html",
 '<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>',
 '<h2 class="sec">Fight Week &mdash; Upcoming Cards</h2>'
 '<p class="note" style="margin:-4px 0 12px"><b>The first two entries below are roster news carrying a date, not new cards.</b> '
 '<span class="mut">Soldic&rsquo;s debut attaches a name to <b>UFC&nbsp;332 on 3 October</b>, a card this page has carried for weeks; the '
 '<b>UFC&nbsp;334</b> entry is the <b>first and so far only</b> bout announced for that date, which is why it appears here without an '
 'undercard and without a headliner. Neither is presented as a newly announced event.</span></p>',
 "mma fight-week framing note")

# (c) Wall Street: the tldr's own "as of this edition" must not outlive the halt
#     framing the way the 1:00 PM sentence did on the last two runs. Anchor it to
#     clock times rather than to "as of this edition".
fix("wallstreet-briefing.html",
 'and as of this edition <b>the oil futures that were still trading have halted as well',
 'and <b>by early afternoon the oil futures that were still trading had halted as well',
 "ws tldr clock-anchored")

fix("wallstreet-briefing.html",
 'ICE Brent at about 1:30 PM ET and CME crude at about 2:30 PM ET on a relayed schedule &mdash; so every symbol on the live ticker at the top of this page is now showing a last matched price rather than a live market</b>;',
 'ICE Brent at about 1:30 PM ET and CME crude at about 2:30 PM ET on a relayed schedule, both of them before this edition went out &mdash; so every symbol on the live ticker at the top of this page is showing a last matched price rather than a live market</b>;',
 "ws tldr halt tense")

print("\n".join(rep))
