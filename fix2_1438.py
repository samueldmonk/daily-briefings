# -*- coding: utf-8 -*-
# MMA read-through fixes, 2026-09-08 ~2:38 PM ET.
import io, os
D = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(D, "b_mma.py")
s = io.open(p, encoding="utf-8").read()
n = 0
def rep(old, new):
    global s, n
    assert old in s, "MISSING: " + old[:80]
    s = s.replace(old, new, 1); n += 1

# (1) "documented in an artefact" overstated: the email is reported by a journalist, not published.
rep('''and the rankings removal remains the only action independently documented in an artefact, namely the email to voters.''',
    '''and the rankings removal remains the action with the most specific evidence behind it, namely an email sent to ranking voters and described by the journalist who received it.''')

# (2) "New this run" used twice in the same UFC 332 paragraph.
rep('''New this run: the UFC has said <b>Shevchenko gets a title shot when she is cleared</b>''',
    '''Also new this run: the UFC has said <b>Shevchenko gets a title shot when she is cleared</b>''')

# (3) Campbell holds a $25k finish cheque, so "no result stated" needed qualifying.
rep('''but no winner or method was stated for either, so neither is tabulated above.</p>''',
    '''but no winner or method was stated for either in anything read this run, so neither is tabulated above. <b>Kurtis Campbell</b> appears on the $25,000 finish-bonus list below, which is a bonus record rather than a sourced result, and it is not treated here as one.</p>''')

io.open(p, "w", encoding="utf-8").write(s)
print("mma fixes:", n)
