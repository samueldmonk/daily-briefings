#!/usr/bin/env python3
"""Prepend this run's new sources to each briefing's Sources footer."""
import io, sys

FAIL = []
ANCHOR = '<footer>\n<div class="lab">Sources</div>\n<ul>\n'

def add(path, items):
    s = io.open(path, encoding='utf-8').read()
    if s.count(ANCHOR) != 1:
        FAIL.append("%s: sources anchor not found exactly once" % path)
        return
    io.open(path, 'w', encoding='utf-8').write(s.replace(ANCHOR, ANCHOR + items))

add('wallstreet-briefing.html',
 '<li><b>CNBC &mdash; <a href="https://www.cnbc.com/2026/08/26/meta-social-media-trial-settlement.html">'
 '&ldquo;Meta settles social media addiction case with California, other states for $16.7 billion&rdquo;</a></b>, '
 'with <b>Bloomberg</b> (<a href="https://www.bloomberg.com/news/articles/2026-08-26/meta-states-agree-to-settle-teen-social-media-harm-case">'
 '&ldquo;Meta Agrees to Pay Up to $16.7 Billion in Social Media Case&rdquo;</a>), <b>NBC News</b> '
 '(<a href="https://www.nbcnews.com/tech/social-media/meta-settles-social-media-addiction-suit-16-billion-rcna594492">'
 '&ldquo;Meta settles social media addiction suit for up to $16 billion&rdquo;</a>) and <b>ABC News</b> '
 '(<a href="https://abcnews.com/Business/meta-settles-states-landmark-social-media-addiction-trial/story?id=135967095">'
 '&ldquo;Meta settles with states in landmark social media addiction trial&rdquo;</a>) &mdash; the four headlines '
 'behind The Lead: the settlement, the four different renderings of the amount, the <b>29 states</b>, the co-leading '
 'attorneys general, California&rsquo;s <b>$1.5&ndash;2.1&nbsp;billion</b> share, the scroll and parental-consent '
 'guardrails, and Meta&rsquo;s denial of liability. <b>&#9888; Read as search summaries and headlines, not full '
 'fetches</b> &mdash; the CNBC article body would not return on fetch this run.</li>\n'
 '<li><b>TipRanks &mdash; <a href="https://www.tipranks.com/news/stock-market-news-today-8-26-2026-futures-mixed-ahead-of-nvidia-results-inflation-data">'
 '&ldquo;Stock Market News Today, 8/26/2026&rdquo;</a></b> &mdash; source for <b>Nvidia reporting at 4:20&nbsp;p.m. '
 'ET with the call at 5&nbsp;p.m.</b>, for the <b>5:27&nbsp;a.m. EDT</b> futures snapshot, and for the '
 '<b>Meta &minus;1.1% to $563.84</b> read published unmerged in Movers &amp; drivers. Search summary.</li>\n'
 '<li><b>Benzinga &mdash; <a href="https://www.benzinga.com/markets/equities/26/08/61427410/stock-market-today-dow-jones-futures-rise-sp-500-slips-ahead-of-nvda-q2-earnings-and-feds-preferred-inflation-data-zoom-intuit-datavault-ai-in-focus">'
 '&ldquo;Dow Jones Futures Rise, S&amp;P 500 Slips Ahead of NVDA Q2 Earnings&rdquo;</a></b> &mdash; re-confirms '
 'Tuesday&rsquo;s closes exactly as carried in the Weekly Scorecard: <b>S&amp;P 500 +0.32% to 7,677.28</b>, '
 '<b>Nasdaq Composite +0.66% to 26,151.30</b>, <b>Dow +0.3% to 53,577.40</b>. Each reconciles against Monday&rsquo;s '
 'closes on level, points and percent.</li>\n'
 '<li><b>Charles Schwab &mdash; <a href="https://www.schwab.com/learn/story/stock-market-update-open">Schwab Market '
 'Update</a>, fetched in full this run</b> &mdash; <b>&#9888; the page served is still stamped &ldquo;Published as '
 'of: August 25, 2026, 9:08 a.m. ET&rdquo;</b>, i.e. Tuesday&rsquo;s open. Nothing from its quote table or its '
 '&ldquo;On the move&rdquo; list is published here as Wednesday data. Only its forward calendar for '
 '<b>August&nbsp;26</b> &mdash; PCE, personal income and spending, the second estimate of Q2 GDP, July durable '
 'orders and the earnings slate &mdash; is used.</li>\n')

add('cyber-briefing.html',
 '<li><b>Reuters, via <a href="https://www.insurancejournal.com/news/east/2026/08/26/882928.htm">Insurance '
 'Journal</a>, <a href="https://www.thestar.com.my/tech/tech-news/2026/08/26/boston-scientific-hit-by-cyberattack-global-operations-affected">'
 'The Star</a> and <a href="https://www.unionleader.com/news/business/boston-scientific-hit-by-cyberattack-global-operations-affected/article_e16f04fb-3224-565c-ba1c-2c53506446ca.html">'
 'the Union Leader</a></b> &mdash; source for the share reaction published this run, <b>&minus;5.03% at $46.90, a '
 'fresh 20-day low</b>, and for the restatement of the 8-K facts (August&nbsp;25 detection, incident-response '
 'procedures, third-party specialists, no restoration timeline, materiality undetermined) and the list of recently '
 'hit healthcare names. <b>&#9888; Search summaries and headlines, not full fetches; no common actor or linkage '
 'between those companies is asserted anywhere on this page.</b></li>\n'
 '<li><b>Fierce Biotech &mdash; <a href="https://www.fiercebiotech.com/medtech/boston-scientific-hit-cyberattack-causing-disruptions-parts-its-business">'
 '&ldquo;Boston Scientific hit by cyberattack causing &lsquo;disruptions&rsquo; to parts of its business&rdquo;</a></b> '
 'and <b>MarketScreener</b>, <b>Echo</b> (Cork) &mdash; corroborating trade and regional coverage of the same '
 'incident. Headlines only.</li>\n'
 '<li><b>CISA &mdash; <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">Known Exploited '
 'Vulnerabilities Catalog</a></b>, searched again this run. The most recent alerts returned remain '
 '<a href="https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog">Aug&nbsp;18 (four)</a>, '
 '<a href="https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog">Aug&nbsp;20 (two, TrueConf)</a> '
 'and <a href="https://www.cisa.gov/news-events/alerts/2026/08/21/cisa-adds-one-known-exploited-vulnerability-catalog">Aug&nbsp;21 (one, Zimbra CVE-2026-73570)</a>. '
 '<b>No alert page dated August&nbsp;25 or 26 was seen this run</b> &mdash; which is a statement about what this '
 'desk saw, not a claim that CISA added nothing. The board below is unchanged.</li>\n')

add('mma-briefing.html',
 '<li><b>UFC.com &mdash; <a href="https://www.ufc.com/video/159548">&ldquo;Song Yadong: &lsquo;With This Fight I '
 'Will Get A Title Shot&rsquo; | UFC Shanghai&rdquo;</a></b> &mdash; the official video title carrying Song&rsquo;s '
 'claim, published ahead of Saturday&rsquo;s main event.</li>\n'
 '<li><b>The Body Lock &mdash; <a href="https://thebodylockmma.com/ufc/news-ufc/song-yadong-goes-shirtless-at-ufc-shanghai-faceoff-as-title-shot-looms/">'
 '&ldquo;Song Yadong Goes Shirtless at UFC Shanghai Faceoff as Title Shot Looms&rdquo;</a></b> and <b>MiddleEasy</b> '
 '(<a href="https://middleeasy.com/mma-news/song-yadong-umar-nurmagomedov-ufc-shanghai-faceoff-title-shot">&ldquo;Song '
 'Yadong Rips Shirt Off In Umar Nurmagomedov UFC Shanghai Faceoff&rdquo;</a>) &mdash; source for the '
 '<b>Wednesday media-day faceoff</b>, the shirt, and the quoted line <b>&ldquo;If I win this fight, I will get a '
 'title shot.&rdquo;</b> Search summaries and headlines. <b>&#9888; This is a separate occasion from the Tuesday '
 'faceoff in front of the host arena</b> reported by Yahoo Sports and carried since the 9:40 edition.</li>\n'
 '<li><b>ESPN &mdash; <a href="https://www.espn.com/mma/fightcenter/_/id/600060620/league/ufc">UFC Fight Night: '
 'Nurmagomedov vs. Song fight centre</a></b> &mdash; consulted this run; no results exist yet, the card is three '
 'days out. <b>&#9888; A Wikipedia entry for the event carries an event number in its URL; no source fetched this '
 'run from UFC.com or ESPN states one, so this page continues to use the official event title only.</b></li>\n')

if FAIL:
    print("FAILED:")
    for f in FAIL:
        print(" -", f)
    sys.exit(1)
print("sources added")
