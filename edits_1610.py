# -*- coding: utf-8 -*-
"""Targeted edits onto the 1540 pages. Run: python3 edits_1610.py <repodir>"""
import sys, io, os
R = sys.argv[1]

def rd(f):
    return io.open(os.path.join(R, f), encoding='utf-8').read()

def wr(f, s):
    io.open(os.path.join(R, f), 'w', encoding='utf-8').write(s)

def sub(s, old, new, label):
    if old not in s:
        raise SystemExit('MISS: ' + label)
    if s.count(old) != 1:
        raise SystemExit('AMBIGUOUS (%d): %s' % (s.count(old), label))
    return s.replace(old, new)

# ---------------------------------------------------------------- MMA
m = rd('mma-briefing.html')
m = sub(m,
  u'the <b>fifth consecutive edition</b> in which the two have failed to converge',
  u'the <b>sixth consecutive edition</b> in which the two have failed to converge',
  'mma run count')
m = sub(m,
  u'byte-for-byte the timestamp recorded two runs ago',
  u'byte-for-byte the timestamp recorded three runs ago',
  'mma modified_time age')
wr('mma-briefing.html', m)

# ---------------------------------------------------------------- CYBER
c = rd('cyber-briefing.html')
old = (u'source IPs <b>82.192.72.4</b> (active since at least 2 September) and '
       u'<b>103.102.31.18</b>.</p>')
new = (u'source IPs <b>82.192.72.4</b> (active since at least 2 September) and '
       u'<b>103.102.31.18</b>. CERT Polska’s advisory was fetched directly from '
       u'cert.pl this run rather than read through a summary, and every figure in this '
       u'paragraph and in the three RouterOS rows above matches that page. '
       u'<span class="mut">One provenance detail from the same advisory, printed because '
       u'CERT Polska states it plainly: the six RouterOS bugs were found by its researchers '
       u'using the <b>GPT-5.5-cyber</b> and <b>GPT-5.6-sol</b> models under the team’s '
       u'access to the OpenAI Government and Trust Agency Collaboration (GTAC) programme, in '
       u'a supervised agent-based laboratory. CERT Polska is explicit that this was not a '
       u'single prompt — every hypothesis was confirmed on real hardware with negative '
       u'controls, and the impact of each bug was assessed by the researchers. It also says '
       u'it is publishing early because the patched packages are already public and the '
       u'community has begun reconstructing the fixes by diffing them. This is a newly-sourced '
       u'detail about an item already on this page, not a new development, so it carries no '
       u'New tag.</span></p>')
c = sub(c, old, new, 'cyber mikrotik note')
wr('cyber-briefing.html', c)

# ---------------------------------------------------------------- WALL STREET
w = rd('wallstreet-briefing.html')
old = (u'<li><b>Friday 11 September &mdash; CPI</b>, 8:30 AM ET. The week&rsquo;s main event '
       u'for the rate path; officials may weight the CPI and PPI reports more heavily than the '
       u'jobs report in shaping the mid-month decision.</li>')
new = (u'<li><b>Friday 11 September &mdash; CPI</b>, 8:30 AM ET. The week&rsquo;s main event '
       u'for the rate path; officials may weight the CPI and PPI reports more heavily than the '
       u'jobs report in shaping the mid-month decision. <span class="t new" style="margin-left:4px">New</span> '
       u'<b>Consensus is now sourced.</b> Morningstar’s survey has August headline CPI at '
       u'<b>+0.3% m/m</b> and <b>2.9% y/y</b> (from 2.7% in July), with <b>core</b> also at '
       u'<b>+0.3% m/m</b> and <b>3.1% y/y</b>, unchanged from July — an inflation rate '
       u'still running above target with core above headline. Ameriprise chief economist '
       u'<b>Russell Price</b> is above consensus at <b>+0.4% m/m</b>, on the view that '
       u'“tariff costs are going to flow through, plus a further increase in food '
       u'prices.” <span class="mut">A competing set of figures was returned this run and '
       u'is <b>refused</b>: an “Inflation Nowcasting” reading dated 4 September put '
       u'headline CPI at 3.38% y/y and core at 2.38% y/y. Those cannot be reconciled with the '
       u'survey — they disagree on the headline by roughly half a point and they invert '
       u'the core-versus-headline relationship — so only the attributed consensus is '
       u'printed. Note also that one return dated the release &ldquo;Thursday, September '
       u'11&rdquo;; 11 September 2026 is a Friday, and the day-of-week above is the one that '
       u'checks out.</span></li>')
w = sub(w, old, new, 'ws cpi consensus')

w = sub(w,
  u'decision Wednesday 2:00 PM ET. The pre-meeting quiet period began',
  u'decision Wednesday 2:00 PM ET, followed by the Chair’s press conference at 2:30 PM ET. '
  u'The pre-meeting quiet period began',
  'ws presser time')
wr('wallstreet-briefing.html', w)
print('edits ok')
