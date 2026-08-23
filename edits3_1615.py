# -*- coding: utf-8 -*-
import io, re
O='/sessions/relaxed-confident-goldberg/mnt/outputs/'
def rd(p): return io.open(O+p, encoding='utf-8').read()
def wr(p,s): io.open(O+p,'w',encoding='utf-8').write(s)
def sub(s, old, new, name):
    assert old in s, 'MISS: '+name
    return s.replace(old, new, 1)

w = rd('wallstreet-briefing.html')

# 1. Drop all three stale New tags (all three were in the 1548 snapshot; no new session since)
n = w.count('<span class="tag new">New</span>')
assert n==3, 'expected 3 new tags, got %d' % n
w = w.replace('<span class="tag new">New</span>', '')

# 2. Lead: add a fourth paragraph on the Fed/Treasury tension, sourced this run
old_tail = '''<em>Correction to earlier editions: July PCE is released Wednesday, August 26 &mdash; not Friday alongside Warsh.</em></p>'''
new_tail = '''<em>Correction to earlier editions: July PCE is released Wednesday, August 26 &mdash; not Friday alongside Warsh.</em></p>
<p>The subplot into Jackson Hole is an unusual one: the Fed and the Treasury are pulling in opposite directions. Warsh has suggested he welcomes higher yields as a way to raise borrowing costs and tighten policy without the Fed moving rates; the point of Bessent&rsquo;s buyback expansion was to push long yields down. &ldquo;We have the Fed and the Treasury basically working in sort of opposite directions,&rdquo; Wilmington Trust senior bond portfolio manager Wil Stith told Yahoo Finance. &ldquo;I think that&rsquo;s just going to require the Fed, which has the larger sandbox, to sort of adjust the target fed funds rate more so than it would have.&rdquo; The consolation for policymakers is that the bond market largely shrugged the maneuver off. The Fed&rsquo;s next policy meeting is in September.</p>'''
w = sub(w, old_tail, new_tail, 'ws lead tail')

# 3. On the radar: enrich Wednesday and add a Fed-watch bullet
w = sub(w,
 'alongside the second estimate of Q2 GDP and July durable goods orders. Nvidia then reports fiscal Q2 after the bell',
 'alongside the second estimate of Q2 GDP (+1.5% annualized on the first estimate) and July durable goods orders (+0.5% previously). Nvidia then reports fiscal Q2 after the bell',
 'ws wed gdp')
w = sub(w,
 'the last of the Magnificent Seven and the next major test of the AI trade.',
 'the last of the Magnificent Seven and the next major test of the AI trade. CrowdStrike, Okta, Synopsys, Agilent, Veeva, Williams-Sonoma and Nutanix also report Wednesday.',
 'ws wed earnings')
w = sub(w,
 '''<li><strong>Friday, August 28 — Warsh at Jackson Hole.</strong>''',
 '''<li><strong>What the Fed is weighing.</strong> Goldman Sachs Research chief economist Jan Hatzius holds the view that price pressures have improved over recent months and that temporary drivers such as tariffs and energy are likely to subside; a hotter-than-expected PCE print would rekindle calls for a September <em>hike</em>. On the crypto side, Bernstein strategist Gautam Chhugani noted that &ldquo;bitcoin historically has had a positive reaction to liquidity expansion.&rdquo;</li>
<li><strong>Friday, August 28 — Warsh at Jackson Hole.</strong>''',
 'ws fed bullet')

# 4. Freshen the TLDR to include the Fed/Treasury tension
w = sub(w,
 'and the next catalysts are Bessent&rsquo;s Iran plan Monday, then July PCE <em>and</em> Nvidia together on Wednesday before Warsh&rsquo;s Jackson Hole keynote Friday.',
 'and the next catalysts are Bessent&rsquo;s Iran plan Monday, then July PCE <em>and</em> Nvidia together on Wednesday before Warsh&rsquo;s Jackson Hole keynote Friday &mdash; with the Fed and the Treasury now visibly pulling in opposite directions on yields.',
 'ws tldr')
wr('wallstreet-briefing.html', w)
print('wallstreet OK; new tags now:', w.count('tag new'))
