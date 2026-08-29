#!/usr/bin/env python3
"""Fix pass for the 10:20 AM edition.

Four stale-novelty errors caught by the validator and the read-through, all of the
same family CORRECTIONS.md has now recorded three editions running: a "this run"
claim is a DATED claim and expires. Every one of these was true at 9:40 and false
at 10:20.

  markets tldr   - "the September rate call has turned over since the last edition"
  markets movers - "the only figure that changed this run is the September rate pricing"
  markets movers - "Nothing on this board is new to the 9:40 edition"  (was this run's phrasing)
  markets Lead   - "What is new to this edition is the rate pricing"
  cyber          - "Context sourced this run" on the open-letter item (sourced at 9:40)

Also adds the sixth re-verification of Friday's closes, which the edit pass tried to
write against a phrase the markets page never contained -- a count=0 replacement that
reported success. That silent no-op is itself recorded.
"""
import io, os, sys

D = os.path.dirname(os.path.abspath(__file__))
NEW = "10:20 AM"
fails = []

def rd(p):
    with io.open(os.path.join(D, p), encoding="utf-8") as f:
        return f.read()

def wr(p, s):
    with io.open(os.path.join(D, p), "w", encoding="utf-8") as f:
        f.write(s)

def sub(s, old, new, label, count=1):
    n = s.count(old)
    if n != count or count == 0:
        fails.append("%s: expected %d, found %d" % (label, count, n))
        return s
    return s.replace(old, new)

# ---------------------------------------------------------------- markets
ws = rd("wallstreet-briefing.html")

WS_TLDR_OLD = ('Markets are closed for the weekend, so Friday&rsquo;s official closes stand &mdash; the '
 'S&amp;P 500 slipped 0.25% to 7,711.76 and still finished the week higher &mdash; and the September rate call '
 'has turned over since the last edition: a prediction market that had put nearly 70% odds on the Fed holding '
 'now prices a 48% chance of a quarter-point hike after Warsh&rsquo;s Jackson Hole speech, with Friday&rsquo;s '
 'payrolls report the next test.')
WS_TLDR_NEW = ('Markets are closed for the weekend, so Friday&rsquo;s official closes stand &mdash; the '
 'S&amp;P 500 slipped 0.25% to 7,711.76 and still finished the week higher &mdash; and the September rate call '
 'has turned over since Friday&rsquo;s bell: a prediction market that had put nearly 70% odds on the Fed holding '
 'now prices a 48% chance of a quarter-point hike after Warsh&rsquo;s Jackson Hole speech, with Friday&rsquo;s '
 'payrolls report the next test.')
ws = sub(ws, WS_TLDR_OLD, WS_TLDR_NEW, "ws tldr stale-novelty")

ws = sub(ws,
    '<b>Nothing on this board is new to the 9:40 edition, and none of it is tagged as though it were.</b> '
    'U.S. equity markets have been closed since Friday&rsquo;s bell, so no new single-stock move can exist. '
    'Every card below is carried from an earlier edition with its original sourcing intact; the only figure '
    'that changed this run is the September rate pricing, which is in <a href="#radar">On the Radar</a>.',
    '<b>Nothing on this board is new to this edition either, and none of it is tagged as though it were.</b> '
    'U.S. equity markets have been closed since Friday&rsquo;s bell, so no new single-stock move can exist. '
    'Every card below is carried from an earlier edition with its original sourcing intact. <b>No market figure '
    'on this page changed at ' + NEW + '</b>; the September rate pricing, which is in '
    '<a href="#radar">On the Radar</a>, turned over in the <b>9:40 AM</b> edition and is carried here.',
    "ws movers stale-novelty")

ws = sub(ws,
    '<b>What is new to this edition is the rate pricing</b>, which is in On the Radar below.',
    '<b>The rate pricing turned over in the 9:40 AM edition</b>, not this one; it is in On the Radar below.',
    "ws lead stale-novelty")

# the sixth re-verification of an unchanged weekend close, written against the
# sentence the page actually contains
ws = sub(ws,
    'and its official closes stand unchanged from the previous edition',
    'and its official closes stand unchanged, <b>re-verified a sixth time at ' + NEW + '</b> against a fresh '
    'search returning the same three figures',
    "ws sixth re-verification")

wr("wallstreet-briefing.html", ws)

# ---------------------------------------------------------------- index (must match tldr)
ix = rd("index.html")
ix = sub(ix, WS_TLDR_OLD, WS_TLDR_NEW, "index markets card")
wr("index.html", ix)

# ---------------------------------------------------------------- cyber
cy = rd("cyber-briefing.html")
cy = sub(cy,
    '<li><b>Context sourced this run &mdash; the industry has written down its own threat model',
    '<li><b>Context, sourced in the 9:40 AM edition and carried &mdash; the industry has written down its own '
    'threat model',
    "cyber open-letter stale-novelty")
wr("cyber-briefing.html", cy)

if fails:
    print("FIX FAILURES (%d):" % len(fails))
    for f in fails:
        print("  - " + f)
    sys.exit(1)
print("fix_1020.py: all fixes applied cleanly.")
