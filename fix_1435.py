# -*- coding: utf-8 -*-
# Read-through fixes, 2026-09-08 ~2:35 PM ET.
# (1) 500 Dow points on a ~53,400 index is ~0.9%, NOT worse than the carried -1%.
#     The "third successive worsening" claim was arithmetically false. Rewritten.
# (2) A midday wire read is not a current 2:35 PM read; headline softened.
# (3) The lead said "two reads" and then listed three.
import io, os
D = os.path.dirname(os.path.abspath(__file__))
n = 0
def rep(path, old, new):
    global n
    p = os.path.join(D, path)
    s = io.open(p, encoding="utf-8").read()
    assert old in s, "MISSING in %s: %s" % (path, old[:80])
    io.open(p, "w", encoding="utf-8").write(s.replace(old, new, 1))
    n += 1

rep("b_ws.py",
    '''<h3 style="margin:0 0 8px;font-size:20px">As of reads taken ~2:23&ndash;2:35 PM ET: the Dow is down about 500 points, and the two shocks driving it &mdash; oil and a failed drug trial &mdash; are still unrelated to each other</h3>''',
    '''<h3 style="margin:0 0 8px;font-size:20px">As of reads taken ~2:23&ndash;2:35 PM ET: a midday wire puts the Dow down about 500 points, and the two shocks driving the session &mdash; oil and a failed drug trial &mdash; are still unrelated to each other</h3>''')

rep("b_ws.py",
    '''Two reads of it were available at the time of this edition and both are printed here rather than smoothed into one:''',
    '''Three reads of it were available at the time of this edition and all three are printed here rather than smoothed into one:''')

rep("b_ws.py",
    '''<li><b>New this edition:</b> a midday market wire dated today reports the <b>Dow down 500 points</b> with stocks sliding and oil moving higher. <span class="mut">That is a headline figure from a single outlet and is printed as such, in points rather than converted to a percentage. It is the third successive worsening this briefing has recorded today: &minus;0.8% on the Dow at 10:48 a.m., &minus;1% at 1:50 p.m., and roughly 500 points now.</span></li>''',
    '''<li><b>New this edition:</b> a <b>midday</b> market wire dated today reports the <b>Dow down 500 points</b>, with stocks sliding and oil moving higher. <span class="mut">That is a headline figure from a single outlet, stated in points rather than as a percentage, and it is a midday read rather than a 2:35 p.m. one. On a Dow that closed Friday at 53,414.25, 500 points is roughly 0.9% &mdash; so this read <b>corroborates</b> the &minus;1% carried below rather than showing further deterioration. The two agree; they are not a sequence.</span></li>''')

rep("b_ws.py",
    '''<span class="mut">Re-confirmed rather than re-dated this run; the 500-point read above is the newer one.</span></li>''',
    '''<span class="mut">Re-confirmed rather than re-dated this run. Taken together with the 500-point read above, the Dow has been sitting near a one-percent decline since the middle of the session; the earlier &minus;0.8% read at 10:48 a.m. is the only materially lighter figure this briefing has recorded today.</span></li>''')

rep("b_ws.py",
    '''<div class="tldr"><b>The Tape</b> <span>The Dow is now down around 500 points on a midday read as Houthi''',
    '''<div class="tldr"><b>The Tape</b> <span>A midday read has the Dow down around 500 points, roughly a one-percent decline, as Houthi''')

rep("b_index.py",
    '''<h3>The Dow gives up 500 points as two unrelated shocks bite</h3>
<p>A midday read has the Dow down around 500 points, the third successive worsening this briefing has logged today, as Houthi strikes on Saudi energy facilities push Brent toward $100 and a failed Novartis heart-drug trial drags health care down more than 2%.</p>''',
    '''<h3>The Dow gives up 500 points as two unrelated shocks bite</h3>
<p>A midday read has the Dow down around 500 points &mdash; roughly one percent, and consistent with the other reads of this session &mdash; as Houthi strikes on Saudi energy facilities push Brent toward $100 and a failed Novartis heart-drug trial drags health care down more than 2%.</p>''')

print("fixes:", n)
