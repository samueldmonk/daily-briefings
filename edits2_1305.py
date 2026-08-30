# -*- coding: utf-8 -*-
import io,sys
def rd(p): return io.open(p,encoding='utf-8').read()
def wr(p,s): io.open(p,'w',encoding='utf-8').write(s)
fails=[]
def rep(s,old,new,label,count=1):
    if old not in s: fails.append('MISSING: '+label); return s
    return s.replace(old,new,count)

# ---------------- WALL STREET ----------------
w=rd('wallstreet-briefing.html')

old10 = u'<td><b>4.73%</b> at the close, on Warsh\'s remarks <span style="opacity:.75">(was &ldquo;~4.67%, after touching 4.73%&rdquo; &mdash; retired 5:15 PM)</span></td>'
new10 = (u'<td><b>4.73%</b> at the close, on Warsh\'s remarks <span style="opacity:.75">(was &ldquo;~4.67%, after touching '
 u'4.73%&rdquo; &mdash; retired 5:15 PM)</span> &#9888; <b>The retired figure came back at 1:00 PM, and it was refused a '
 u'second time.</b> A rates round-up fetched this run put the 10-year &ldquo;around <b>4.67%</b> on Friday&rdquo;; a '
 u'dedicated <b>Treasury-yields snapshot for August 28</b>, fetched in the same minute, states the 10-year '
 u'<b>finished at 4.73%</b> and the 2-year at <b>4.34%</b>. <b>A round-up&rsquo;s &ldquo;around&rdquo; does not '
 u'displace a close from a yields snapshot</b>, and 4.67% was already retired once on the same reasoning.</td>')
w = rep(w, old10, new10, 'ws 10yr row')

old_fed_tail = u'Neither is adopted &mdash; see On the Radar.</td>'
new_fed_tail = (u'Neither is adopted &mdash; see On the Radar. &#9888; <b>A sixth read at 1:00 PM, and it is the '
 u'widest spread yet.</b> One round-up states markets price <b>about a 65% chance the Fed holds</b> in September &mdash; '
 u'roughly <b>35% for a hike</b> &mdash; while the same run returned a wealth-management note saying strategists '
 u'<b>now expect a single quarter-point hike in September</b>, and a separate line putting the odds of a hike '
 u'<b>by December above 70%</b>. <b>35%, 48%, near 50% and 57% are four different answers to one question</b>, and '
 u'nothing fetched reconciles or co-dates them. <b>This page has now declined to adopt a September probability six '
 u'times</b>, which is the correct outcome rather than a failure of research: the spread is in the sources, not in '
 u'the reading of them.</td>')
w = rep(w, old_fed_tail, new_fed_tail, 'ws fed cell')
w = rep(w, u'<b>Four reads, all pointing the same way; none adopted.</b>',
           u'<b>Six reads now, spanning 35% to 57% on the same question; none adopted.</b>', 'ws fed header')

src_anchor = u'<b>Sources checked this run:</b><br>'
w = rep(w, src_anchor, src_anchor +
 u'<a href="https://www.advisorperspectives.com/dshort/updates/2026/08/28/treasury-yields-snapshot-august-28-2026">Advisor Perspectives &mdash; Treasury Yields Snapshot: August 28, 2026</a><br>'
 u'<a href="https://finance.yahoo.com/markets/live/stock-market-today-friday-august-28-dow-sp-500-nasdaq-dip-fed-warsh-jackson-hole-speech-081514091.html">Yahoo Finance &mdash; Dow, S&amp;P 500, Nasdaq end week on down note as rate-hike bets jump</a><br>'
 u'<a href="https://www.chase.com/personal/investments/learning-and-insights/article/september-2026-rate-hike-now-expected-amid-energy-shocks">Chase &mdash; Will the Fed hike rates in September? A 25bp move is now expected</a><br>'
 u'<a href="https://tradingeconomics.com/united-states/government-bond-yield">Trading Economics &mdash; US 10-year Treasury note yield</a><br>', 'ws sources')
wr('wallstreet-briefing.html', w)

# ---------------- MMA ----------------
m=rd('mma-briefing.html')

m = rep(m, u'for a fifty-eighth unchanged edition', u'for a fifty-ninth unchanged edition', 'mma champ counter tldr')
m = rep(m, u'fifty-eighth consecutive edition', u'fifty-ninth consecutive edition', 'mma champ counter body', count=99)

# Paris card: add the two newly sourced main-card bouts
old_paris = (u'<b>13 bouts</b>, with <b>Fares Ziam vs. Axel Sola</b>, <b>Michael Page vs.\n'
             u'Nursulton Ruziboev</b> and <b>Losene Keita vs. Muhammadjon Naimov</b> also listed.')
if old_paris not in m:
    old_paris = old_paris.replace('\n',' ')
new_paris = (u'<b>13 bouts</b>, with <b>Fares Ziam vs. Axel Sola</b>, <b>Michael Page vs. '
 u'Nursulton Ruziboev</b> and <b>Losene Keita vs. Muhammadjon Naimov</b> also listed. '
 u'<b>Two more main-card bouts were sourced at 1:00 PM:</b> <b>Mario Pinto vs. Ryan Spann</b> at heavyweight and '
 u'<b>Oumar Sy vs. Modestas Bukauskas</b> at light heavyweight. &#9888; <b>One spelling is left as carried:</b> the '
 u'same listing renders Naimov&rsquo;s first name <b>Muhammad</b> where this page carries <b>Muhammadjon</b>; both '
 u'forms are in circulation, the page keeps the fuller form it sourced first, and the variant is recorded rather '
 u'than silently swapped.')
m = rep(m, old_paris, new_paris, 'mma paris card')

# Bonuses: seventh-check corroboration
old_bon = u'this page does not read a round number as evidence of an extra recipient.'
new_bon = (old_bon + u' <b>Re-confirmed at 1:00 PM, and this time both tiers and the total arrived in one place.</b> '
 u'A report fetched this run states the <b>$400,000</b> total, names <b>Fight of the Night: Liu Ce vs. Levi Rodrigues '
 u'Jr.</b> and <b>Performance of the Night: Song Yadong and Bilal Hasan</b>, and separately lists the five '
 u'<b>$25,000</b> recipients &mdash; <b>Hector Santiago, Francesco Nuzzi, Rei Tsuruya, Kai Asakura and Denise '
 u'Gomes</b> &mdash; exactly as carried above. <b>It also re-states the card&rsquo;s ten finishes.</b> Nothing '
 u'changed; the point of recording it is that the two tiers, which reached this page a day apart and from different '
 u'outlets, now sit in a single account that agrees with both.')
m = rep(m, old_bon, new_bon, 'mma bonuses corroboration')

src_anchor_m = u'<b>Sources checked this run:</b><br>'
m = rep(m, src_anchor_m, src_anchor_m +
 u'<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN &mdash; Current and all-time UFC champions</a><br>'
 u'<a href="https://www.ufc.com/news/ufc-fight-night-shanghai-2026-bonus-coverage">UFC.com &mdash; Bonus coverage, UFC Shanghai</a><br>'
 u'<a href="https://sports.yahoo.com/articles/ufc-shanghai-bonuses-yadong-song-150010453.html">Yahoo Sports &mdash; UFC Shanghai bonuses: Yadong Song, 3 others earn $100,000</a><br>'
 u'<a href="https://www.ufc.com/event/ufc-fight-night-september-05-2026">UFC.com &mdash; UFC Fight Night: Hooker vs. Parnasse (UFC Paris)</a><br>'
 u'<a href="https://en.wikipedia.org/wiki/UFC_Fight_Night:_Hooker_vs._Parnasse">Wikipedia &mdash; UFC Fight Night: Hooker vs. Parnasse</a><br>', 'mma sources')

# tldr
s=m.find(u'class="tldr"><b>Tale of the Tape</b> <span>')
e=m.find(u'</span></div>', s)
if s<0 or e<0: fails.append('MISSING: mma tldr')
else:
    new_tl=(u'class="tldr"><b>Tale of the Tape</b> <span>The Shanghai bonus picture finally arrived in one piece '
      u'&mdash; a single report this run carries the <b>$400,000</b> total, <b>Fight of the Night to Liu Ce vs. Levi '
      u'Rodrigues Jr.</b>, <b>Performance of the Night to Song Yadong and Bilal Hasan</b> and the five '
      u'<b>$25,000</b> finish bonuses, tiers that reached this page a day apart and from different outlets now '
      u'agreeing in a single account, along with the card&rsquo;s <b>ten finishes</b>; UFC Paris gained two more '
      u'main-card bouts, <b>Mario Pinto vs. Ryan Spann</b> and <b>Oumar Sy vs. Modestas Bukauskas</b>, while the '
      u'headline price stays a <b>range</b> &mdash; Salahdine Parnasse is favoured over Dan Hooker at <b>&minus;400</b>, '
      u'<b>&minus;428</b> and <b>&minus;500</b> depending on the book, and none of the three is adopted; and the '
      u'champions board was re-verified against ESPN&rsquo;s own page for a <b>fifty-ninth unchanged edition</b>, '
      u'clean again on the three belts this project has historically got wrong.')
    m = m[:s]+new_tl+m[e:]
wr('mma-briefing.html', m)

if fails:
    print('FAILURES:'); [print(' ',f) for f in fails]; sys.exit(1)
print('OK stage 2')
