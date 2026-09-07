# -*- coding: utf-8 -*-
import sys
O='/sessions/gracious-zealous-maxwell/mnt/outputs/'
def rd(f): return open(O+f,encoding='utf-8').read()
def wr(f,s): open(O+f,'w',encoding='utf-8').write(s)
def sub1(s,a,b,label):
    if a not in s: print('!! MISS',label); sys.exit(1)
    return s.replace(a,b,1)

m=rd('mma-briefing.html')

# 1. tldr: fourth consecutive zero-tag edition
m=sub1(m,'There is no new development in the 5:38&nbsp;PM edition either &mdash; a third consecutive sweep returned only material this page already carries</b>, so <b>no New tag is attached anywhere on it</b>',
 'There is no new development in this 6:05&nbsp;PM edition either &mdash; a <b>fourth</b> consecutive sweep returned only material this page already carries</b>, so <b>no New tag is attached anywhere on it</b>',
 'mma tldr count')

# 2. the vacate/stripped conflict gains its first corroborating return
old=('A second return read in the 5:05&nbsp;PM edition repeats <b>&ldquo;stripped&rdquo;</b> and adds a reason &mdash; <b>&ldquo;due to injury&rdquo;</b> &mdash; '
 'which <b>agrees with this page on the cause and still disagrees on the mechanism</b>, so the conflict is now two returns deep and is still not resolved here.')
new=('A second return read in the 5:05&nbsp;PM edition repeated <b>&ldquo;stripped&rdquo;</b> and added a reason &mdash; <b>&ldquo;due to injury&rdquo;</b> &mdash; '
 'which agreed with this page on the cause and still disagreed on the mechanism. <b>A third return, read in this 6:05&nbsp;PM edition, is the first to come down on this page&rsquo;s side of it:</b> '
 'a UFC&nbsp;332 preview says the vacant belt is at stake because Shevchenko <b>&ldquo;was forced to vacate the title due to injury&rdquo;</b> &mdash; <b>vacate, not strip</b> &mdash; '
 'and adds that the injury <b>&ldquo;will sideline her for up to a year&rdquo;</b>, which matches the <b>about a year</b> absence this page already carries. '
 '<b>The count is now three returns deep and split 2&ndash;1 for &ldquo;stripped&rdquo; by volume</b>, but the single return using <b>vacated</b> agrees with the promotion&rsquo;s own <b>5 September</b> wording, '
 'which is the source this page has followed throughout and follows still. <b>The conflict is narrowed, not closed</b>, and it stays printed. '
 '<b>&#9733; A tally of outlets is not evidence; the one that matches the primary announcement outweighs the two that paraphrase it.</b>')
m=sub1(m,old,new,'mma vacate corroboration')

# 3. champions refusal -- a stale board came back this edition
kk='Champions Board</h2>\n<p class="note" style="margin:-4px 0 12px">'
add=('<b>The stale-champions trap fired again in this 6:05&nbsp;PM edition, and this time it took three belts at once.</b> A champions-list return read at this desk gave '
 '<b>Alex Pereira at light heavyweight</b> (&ldquo;won title Oct.&nbsp;4, 2025&rdquo;), <b>Khamzat Chimaev at middleweight</b> (&ldquo;won title Aug.&nbsp;16, 2025&rdquo;) and '
 '<b>Valentina Shevchenko at women&rsquo;s flyweight</b> (&ldquo;won title Sept.&nbsp;14, 2024&rdquo;). <b>All three are refused.</b> This desk carries '
 '<b>Carlos Ulberg</b> at light heavyweight and <b>Sean Strickland</b> at middleweight, and the women&rsquo;s flyweight belt is <b>vacant</b> &mdash; Shevchenko gave it up on <b>5 September</b>, '
 'which is <i>why</i> Nat&aacute;lia Silva and Wang Cong are fighting for it at UFC&nbsp;332, a fight the same desk&rsquo;s own page carries two sections above. '
 '<span class="mut">The tell is internal: <b>a list that still seats Shevchenko cannot also be current for a card built on her vacating</b>, and the three &ldquo;won title&rdquo; dates it attaches '
 '&mdash; October 2025, August 2025, September 2024 &mdash; are all older than the events that moved those belts. <b>The other eight lines in the same return matched this board exactly</b> and are noted as corroboration: '
 'Aspinall, Makhachev, <b>Gaethje (&ldquo;won title June&nbsp;14, 2026&rdquo;)</b>, Volkanovski, Yan, Van, Harrison and Dern. '
 '&#9733; <b>A champions list is the one document on this beat that is wrong by default &mdash; it is a snapshot, and every event since it was taken is a chance for it to have gone stale. '
 'Eight right lines do not make the other three right.</b></span></p>\n<p class="note" style="margin:-4px 0 12px">')
m=sub1(m,kk,kk.replace('<p class="note" style="margin:-4px 0 12px">','')+add,'mma champs refusal')
wr('mma-briefing.html',m)
print('mma done; new tags',m.count('class="t new"'))
