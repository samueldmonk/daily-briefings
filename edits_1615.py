# -*- coding: utf-8 -*-
import io, sys, re
O='/sessions/relaxed-confident-goldberg/mnt/outputs/'
def rd(p): return io.open(O+p, encoding='utf-8').read()
def wr(p,s): io.open(O+p,'w',encoding='utf-8').write(s)
def sub(s, old, new, name):
    assert old in s, 'MISS: '+name
    return s.replace(old, new, 1)

fails=[]

# ---------------- CYBER ----------------
c = rd('cyber-briefing.html')
# 1. drop stale New tag (BTR.sys was in the 1548 snapshot)
c = sub(c, '<div class="tags"><span class="tag new">New</span><span class="tag hot">Endpoint</span></div>',
           '<div class="tags"><span class="tag hot">Endpoint</span></div>', 'cyber new tag')
# 2. refresh the vuln-watch note to reflect this run's re-fetch
c = sub(c,
 'The Hacker News front page was re-read this run and its newest item is still dated August 22, so the top story is unchanged.',
 'The Hacker News front page was re-read again for this edition and its newest item is still dated August 22 (the TikTok settlement), so the top story is unchanged and nothing on this page is tagged New. The CISA KEV catalog mirror was also re-fetched this edition: the board below is unchanged at twelve tracked entries.',
 'cyber note')
wr('cyber-briefing.html', c)

# ---------------- MMA ----------------
m = rd('mma-briefing.html')
# 1. drop stale New tag (Bilal Hasan was in the 1548 snapshot)
m = re.subn(r'<span class="tag new">New</span>', '', m, count=1)
assert m[1]==1, 'MISS: mma new tag'
m = m[0]
# 2. Shanghai card: add the full UFC.com bout list fetched this run
old_shanghai = '''<p>A bantamweight headliner between Nurmagomedov, a former UFC bantamweight title challenger, and Song, the division&rsquo;s No. 5-ranked contender. Main card 6:00 AM ET.</p>
<div class="odds">Odds: Nurmagomedov −450 / Song +350 (UFC.com). DraftKings has −470 / +360; BetOnline opened the line at −700 / +500.</div>'''
new_shanghai = '''<p>A bantamweight headliner between Nurmagomedov, a former UFC bantamweight title challenger, and Song, the division&rsquo;s No. 5-ranked contender. Main card 6:00 AM ET.</p>
<p><strong>Co-main (new here):</strong> No. 4-ranked strawweight Yan Xiaonan &mdash; China&rsquo;s first female UFC athlete and a former strawweight title challenger &mdash; meets No. 13-ranked Denise Gomes, who has won four straight. It is Yan&rsquo;s first appearance in China since 2018. Also announced: Junior Tafa vs kickboxing world champion Liu Ce at light heavyweight on Liu&rsquo;s UFC debut; a flyweight rematch between No. 11-ranked Alex Perez and Sumudaerji after their No Contest in Macau; and Rei Tsuruya vs Kevin Borjas at flyweight.</p>
<div class="odds">Odds: Nurmagomedov −450 / Song +350 (UFC.com). DraftKings has −470 / +360; BetOnline opened the line at −700 / +500. No odds published for the co-main in any source fetched this run.</div>'''
m = sub(m, old_shanghai, new_shanghai, 'shanghai card')
# tag the Shanghai card New-detail
m = sub(m, '<div class="dv">Sat, Aug 29 · Oriental Sports Center, Pudong District, China</div>',
           '<div class="dv">Sat, Aug 29 · Oriental Sports Center, Pudong District, China</div>\n<div class="tags"><span class="tag new">New</span><span class="tag">Full card announced</span></div>', 'shanghai tag')
wr('mma-briefing.html', m)
print('cyber + mma stage 1 OK')
