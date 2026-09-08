# -*- coding: utf-8 -*-
import io, os
D = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(D, "b_index.py")
s = io.open(p, encoding="utf-8").read()
n = 0

def rep(old, new):
    global s, n
    assert old in s, "MISSING: " + old[:90]
    s = s.replace(old, new, 1)
    n += 1

rep('''<h3>Routers are being taken over by attackers who got a head start on the patch</h3>
<p>An SSH authentication bypass in MikroTik RouterOS, chained for full administrative takeover and exploited in the wild since 2 September, is now the most urgent unpatched exposure on the internet-facing edge, with more than 122,000 devices showing exposed SSH interfaces.</p>''',
    '''<h3>The biggest Patch Tuesday ever shipped, and two of its flaws were already being used</h3>
<p>Microsoft&#39;s September release landed this afternoon with 973 CVEs, described as its largest to date, including two Windows elevation-of-privilege zero-days confirmed exploited in the wild &mdash; while the MikroTik router takeover chain runs on unpatched with more than 122,000 exposed devices.</p>''')

rep('''<h3>Two unrelated shocks, one lower market</h3>
<p>Stocks are lower across the board into Tuesday afternoon with the Dow much the weakest of the three, as Houthi strikes on Saudi energy facilities push Brent toward $100 and a failed Novartis heart-drug trial drags the health care sector down more than 2%.</p>''',
    '''<h3>The Dow gives up 500 points as two unrelated shocks bite</h3>
<p>A midday read has the Dow down around 500 points, the third successive worsening this briefing has logged today, as Houthi strikes on Saudi energy facilities push Brent toward $100 and a failed Novartis heart-drug trial drags health care down more than 2%.</p>''')

rep('''<h3>A win on Saturday, off the rankings by Monday</h3>
<p>Michael Page has been pulled from the UFC rankings less than two days after winning at UFC Paris with a release reportedly looming, while Valentina Shevchenko has been stripped of the women&#39;s flyweight title after telling the promotion she would be unable to compete for at least a year.</p>''',
    '''<h3>A win on Saturday, off the rankings Monday, off the roster by Tuesday</h3>
<p>Two outlets now report that Michael Page has actually been released by the UFC, three days after his win at UFC Paris and a day after being pulled from the rankings, though the promotion itself has announced nothing.</p>''')

io.open(p, "w", encoding="utf-8").write(s)
print("index edits:", n)
