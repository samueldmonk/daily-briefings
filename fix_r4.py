# -*- coding: utf-8 -*-
import io
B="/sessions/youthful-bold-tesla/mnt/outputs/"
def ed(fn, pairs):
    p=B+fn; s=io.open(p,encoding="utf-8").read()
    for a,b in pairs:
        assert s.count(a)==1, (fn, a[:70], s.count(a))
        s=s.replace(a,b)
    io.open(p,"w",encoding="utf-8").write(s); print("patched",fn,len(pairs))

# --- WALL STREET ---
ed("wallstreet-briefing.html", [
 # (a) sector-heat note no longer repeats the lead verbatim
 ('<p class="note">Editorial line, sourced this run: most sectors were in the green, led by technology and '
  'financial stocks, while oil and gas shares retreated. The <b>VIX</b> was <b>14.85, +0.27%</b> on '
  'Yahoo&rsquo;s ~9:05&nbsp;AM strip.</p>',
  '<p class="note">The sourced sector line for today is given in The Lead above and is not repeated here. One '
  'figure to add: the <b>VIX</b> was <b>14.85, +0.27%</b> on Yahoo&rsquo;s ~9:05&nbsp;AM strip.</p>'),
 # (b) bitcoin row earns its CoinDesk source
 ('and a third account simply saying bitcoin <b>topped $85,000</b>.',
  'and a third account simply saying bitcoin <b>topped $85,000</b>. The driver is the same in each: the '
  '<b>CLARITY Act</b> stalled in the Senate on a <b>49&ndash;50</b> cloture vote, short of the 60 required, and '
  'CoinDesk, citing CoinGlass, puts just over <b>$300 million of the roughly $313 million</b> in crypto positions '
  'recently liquidated on <b>short sellers &mdash; about 96%</b>.'),
 # (c) name the headline IPO figure in the bullet that carries the Bloomberg link
 ('Oura is going public.</b> The Finnish smart-ring maker and some backers are marketing',
  'Oura is going public.</b> The Finnish smart-ring maker and some backers are seeking to raise as much as '
  '<b>$2.2 billion</b>, marketing'),
])

# --- CYBER ---
ed("cyber-briefing.html", [
 ('<h3 class="critc">Patch Priority &mdash; deadline is today</h3>', '<h3 class="critc">Deadline is today</h3>'),
 ('per a <b>18 September</b> entry', 'per an <b>18 September</b> entry'),
 ('<a href="https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog">CISA &mdash; adds seven KEVs, 2 September</a>',
  '<a href="https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog">CISA &mdash; adds seven KEVs, 2 September</a> &middot; '
  '<a href="https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog">CISA &mdash; adds four KEVs, 9 September</a> &middot; '
  '<a href="https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-one-known-exploited-vulnerability-catalog">CISA &mdash; adds one KEV, 11 September</a>'),
])

# --- MMA ---
ed("mma-briefing.html", [
 # (g) Rogan appears once, in Around the Sport
 (' <b>Joe Rogan</b> has publicly backed Tsarukyan for the shot.</p>', '</p>'),
 # (h) cross-reference points at the right section
 ('See the odds refusal below the cards.', 'The odds refusal is in Around the Sport, below.'),
 # (i) the 790 figure stated the way the source states it
 ('<b>UFC 331 was the promotion&rsquo;s 790th event</b>, per the running list of UFC events read this run.',
  '<b>790 UFC events had been held as of UFC 331</b>, per the running list of UFC events read this run.'),
 # (j) UFC 334 gets a source link
 ('<a href="https://en.wikipedia.org/wiki/UFC_333">Wikipedia &mdash; UFC 333: Volkanovski vs. Evloev</a>',
  '<a href="https://en.wikipedia.org/wiki/UFC_333">Wikipedia &mdash; UFC 333: Volkanovski vs. Evloev</a> &middot; '
  '<a href="https://en.wikipedia.org/wiki/UFC_334">Wikipedia &mdash; UFC 334: Gane vs. Hokit</a>'),
])
