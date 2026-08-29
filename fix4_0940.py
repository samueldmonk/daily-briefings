#!/usr/bin/env python3
"""Fourth fix pass — read-through of the MMA results and Around the Sport sections.

(11) The results note still said bonuses were unannounced "since the main event has not been
     resulted" — stale from the 8:46 edition, and it contradicts the Around the Sport bullet
     on the same page, which correctly says the main event ended hours ago.
(12) A bullet headed "Two fighters missed weight" sits two bullets above one that says three
     fighters missed. Three is correct (Lima 127, Xiong 117, Polastri 118.5).
(13) "Three of thirteen fighters missed" — thirteen is the BOUT count, not the fighter count.
(14) The strawweight limit was asserted as 115 lb; no source seen this run stated the limit.
"""
import io, sys

D = sys.argv[1] if len(sys.argv) > 1 else "."
p = f"{D}/mma-briefing.html"
h = io.open(p, encoding="utf-8").read()

def sub(old, new, tag):
    global h
    if old not in h:
        raise SystemExit(f"fix4 ANCHOR MISSING [{tag}]: {old[:110]!r}")
    if h.count(old) != 1:
        raise SystemExit(f"fix4 ANCHOR x{h.count(old)} [{tag}]")
    h = h.replace(old, new)

# (11) stale reason for the absent bonuses
sub("<b>Performance bonuses: still none announced in any source seen this run</b> &mdash; expected, since the main\nevent has not been resulted.",
    "<b>Performance bonuses: still none announced in any source seen this run</b> &mdash; and the main event "
    "is now <b>resolved</b>, so the earlier explanation for the silence no longer applies. This is the "
    "<b>fifth</b> consecutive check with nothing announced.",
    "mma-bonus-stale")

# (12) the count in the heading disagreed with the count two bullets down
sub("<li><b>Two fighters missed weight on the same card.</b> <b>Andre Lima</b> missed for the second time in his UFC",
    "<li><b>Three fighters missed weight on the same card; two of them are covered here.</b> "
    "<b>Andre Lima</b> missed for the second time in his UFC",
    "mma-weight-count")

# (13) thirteen is the number of bouts, not of fighters
sub("Three of thirteen fighters\nmissed.",
    "Three fighters missed across <b>thirteen bouts</b> &mdash; thirteen is the number of contests on the\n"
    "card, not the number of competitors on it.",
    "mma-thirteen")

# (14) an unsourced limit figure
sub("because <b>both</b> women missed the 115-pound strawweight limit (117 and 118.5)",
    "because <b>both</b> women missed the contracted strawweight limit &mdash; <b>Xiong at 117</b> and "
    "<b>Polastri at 118.5</b>, the weights themselves sourced, the limit figure not asserted",
    "mma-limit")

io.open(p, "w", encoding="utf-8").write(h)
print("fix4_0940: OK — 4 further read-through corrections")
