#!/usr/bin/env python3
"""Incremental edits — Wednesday Aug 26 2026, ~10:20 a.m. ET edition (Morning bucket).
Base: the 0942 pages pulled from the repo this run."""
import io, sys, re

FAIL = []

def sub(path, old, new, count=1):
    s = io.open(path, encoding='utf-8').read()
    n = s.count(old)
    if n != count:
        FAIL.append("%s: expected %d occurrence(s), found %d for: %s" % (path, count, n, old[:110]))
        return
    io.open(path, 'w', encoding='utf-8').write(s.replace(old, new))

WS = 'wallstreet-briefing.html'
CY = 'cyber-briefing.html'
MM = 'mma-briefing.html'
IX = 'index.html'

NEW = '<span class="tag new">New &middot; 10:20</span>'

# ---------------------------------------------------------------- WALL STREET
# 1. demote the 9:40 New tag
sub(WS, '<span class="tag new">New &middot; 9:40</span>',
        '<span class="tag">Carried &middot; 9:40 edition</span>')

# 2. summary strip
WS_TLDR_OLD = ('<div class="tldr"><b>The Tape</b> <span><b>The bell has rung on a sticky-inflation Wednesday</b> '
 '&mdash; July PCE landed <b>a tenth hot on the headline at 0.2% and 3.7%</b> and <b>exactly on forecast at the '
 'core, 0.2% and 3.3%</b>, and Yahoo Finance&rsquo;s live blog has re-titled from &ldquo;futures hold steady&rdquo; '
 'to <b>&ldquo;Dow, S&amp;P&nbsp;500, Nasdaq slip&rdquo;</b> as the tape marks time in front of <b>Nvidia&rsquo;s '
 'report after the close</b>.</span></div>')
WS_TLDR_NEW = ('<div class="tldr"><b>The Tape</b> <span><b>Meta has settled the states&rsquo; social-media '
 'addiction case for about $16.7&nbsp;billion</b> &mdash; the single-name story of an otherwise flat, '
 'sticky-inflation Wednesday in which July PCE ran <b>a tenth hot on the headline</b> and <b>exactly on forecast '
 'at the core</b>, and the tape marks time in front of <b>Nvidia&rsquo;s report at 4:20&nbsp;p.m. ET</b>.</span></div>')
sub(WS, WS_TLDR_OLD, WS_TLDR_NEW)

# 3. lead headline — restamp and re-lead on Meta
sub(WS, '<h2>Hot on the headline, steady at the core &mdash; and as of this <i>~9:40&nbsp;a.m. ET</i> edition the tape is slipping into Nvidia night</h2>',
        '<h2>Meta writes a $16.7&nbsp;billion cheque &mdash; and as of this <i>~10:20&nbsp;a.m. ET</i> edition the rest of the tape is marking time into Nvidia night</h2>\n'
 '<p><b>The session&rsquo;s lead is a legal settlement, not a data point.</b> Meta and a coalition of state '
 'attorneys general have <b>settled the federal trial</b> over allegations that the company misrepresented the '
 'extent of child-related mental-health harms caused by Facebook and Instagram. CNBC puts the figure at '
 '<b>$16.7&nbsp;billion</b>; Bloomberg&rsquo;s headline says Meta agreed to pay <b>&ldquo;up to&rdquo; '
 '$16.7&nbsp;billion</b>; NBC News frames it as <b>&ldquo;up to $16 billion&rdquo;</b>; and a separate read this '
 'run gives <b>$16.68&nbsp;billion</b>. <b>&#9888; Those are four different renderings of one number and they are '
 'published unmerged &mdash; nothing here is averaged or rounded into a single figure.</b> The case was brought by '
 '<b>29 states</b> and co-led by <b>California Attorney General Rob Bonta</b> with the attorneys general of '
 '<b>Colorado, New Jersey and Kentucky</b>; California could receive <b>$1.5&nbsp;billion to $2.1&nbsp;billion</b> '
 'if the court approves. The deal requires new guardrails &mdash; limits on how long young users can scroll, and a '
 'bar on switching off certain safety settings without parental consent. The filing states that Meta '
 '<b>&ldquo;denies the allegations against it and that it has any liability to the Plaintiffs,&rdquo;</b> and a '
 'judge still has to sign off.</p>')

# 4. the bell paragraph — an hour old now
sub(WS, '<p><b>U.S. markets are open.</b> The bell rang at 9:30, minutes before this edition went out, and the first of Wednesday&rsquo;s two events is behind us with the number confirmed.',
        '<p><b>U.S. markets are open, and roughly an hour into the session.</b> The first of Wednesday&rsquo;s two set-piece events is behind us with the number confirmed; the second does not arrive until after the close.')

# 5. new mover card — Meta, with the share reaction published unmerged
META_CARD = ('<div class="card">\n'
 '<div class="tags">' + NEW + '<span class="tag">Legal</span><span class="tag">Reaction disputed</span></div>\n'
 '<h3>Meta settles for about $16.7 billion &mdash; and the three reads of its share reaction do not agree</h3>\n'
 '<p>Three separate reads of Meta&rsquo;s move surfaced this run and <b>they point in different directions</b>. A '
 'Yahoo Finance summary says <b>Meta stock jumped in early trading</b> after the settlement. A TipRanks summary '
 'has <b>Meta shares falling 1.1% to $563.84 in early trading</b>. A third read has <b>Meta surging 3.9% in '
 'pre-open trading</b>. <b>&#9888; None of the three carries a clock time on the page it came from, and they cannot '
 'all describe the same instant.</b> All three are published as they were found; this page asserts <b>no</b> '
 'percentage move for META in this edition, and no level. The live widgets above and below carry the actual tape.</p>\n'
 '<p class="note">What <i>is</i> firm is the settlement itself and its structure &mdash; the amount, the '
 '29&nbsp;states, the California share, the scroll limits and parental-consent guardrails, and Meta&rsquo;s denial '
 'of liability &mdash; all of which appear in the CNBC, Bloomberg, NBC News and ABC News accounts read this run. '
 'See The Lead above.</p>\n'
 '</div>\n')
sub(WS, '<div class="card">\n<div class="tags"><span class="tag">Carried &middot; 9:16 edition</span><span class="tag">Macro</span><span class="tag crit">Confirmed print</span></div>',
        META_CARD + '<div class="card">\n<div class="tags"><span class="tag">Carried &middot; 9:16 edition</span><span class="tag">Macro</span><span class="tag crit">Confirmed print</span></div>')

# 6. ticker tape — drop Tuesday's DKS, add META, remove the duplicated US10Y
sub(WS, '{"proName":"NYSE:DKS","title":"DICK\'S"},', '{"proName":"NASDAQ:META","title":"Meta"},')
sub(WS, '{"proName":"TVC:US10Y","title":"US 10Y"},{"proName":"TVC:US10Y","title":"US 10Y"}',
        '{"proName":"TVC:US10Y","title":"US 10Y"}')

# 7. Chart of the day — the session is open now; chart the largest sourced move
sub(WS, '{"symbol":"NASDAQ:NVDA","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}',
        '{"symbol":"NASDAQ:INTU","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}')
sub(WS, '<div class="note">Wednesday&rsquo;s session has not opened, so there is no biggest mover yet to chart. The chart tracks <b>NVDA</b> &mdash; the name reporting after tonight&rsquo;s close and, on Yahoo Finance&rsquo;s framing, the quarterly yardstick for the AI trade. The largest move on the most recent completed session was <b>DICK&rsquo;S Sporting Goods, &minus;30.68%</b>, and the largest premarket move on the board this morning is <b>Intuit, &minus;11.8%</b> &mdash; both covered in Movers &amp; drivers above.</div>',
        '<div class="note">The session is open, and <b>the largest single-name move any source fetched this run puts a number on is Intuit</b> &mdash; <b>&minus;11.8% in premarket trading to $315.30</b> on its fiscal-2027 guidance, per Investing.com&rsquo;s 7:10&nbsp;a.m. ET wire. The chart tracks <b>INTU</b> accordingly. <b>&#9888; No source read this run states a regular-session percentage move for any individual stock</b>, so nothing here claims to be the biggest <i>intraday</i> mover; the heatmap below and the tape above carry the live picture. The largest move on the most recent <i>completed</i> session was DICK&rsquo;S Sporting Goods at <b>&minus;30.68%</b> &mdash; that was <b>Tuesday</b>, and it is not a Wednesday mover.</div>')

# 8. On the radar — Nvidia's exact release time
sub(WS, '<li><b>Jensen Huang on CNBC&rsquo;s &ldquo;Mad Money,&rdquo; 6&nbsp;p.m. ET.</b>',
        '<li><b>Nvidia reports at 4:20&nbsp;p.m. ET, with the earnings call at 5&nbsp;p.m.</b> Those times come from a '
 'TipRanks market-news summary read this run. Also on today&rsquo;s macro slate, per Schwab&rsquo;s calendar: the '
 '<b>second estimate of second-quarter GDP</b>, <b>July durable goods orders</b>, and <b>July personal income and '
 'spending</b> alongside the PCE print.</li>\n'
 '<li><b>Jensen Huang on CNBC&rsquo;s &ldquo;Mad Money,&rdquo; 6&nbsp;p.m. ET.</b>')

# ---------------------------------------------------------------------- CYBER
CY_TLDR_OLD = ('<div class="tldr"><b>The Wire</b> <span><b>Boston Scientific&rsquo;s 8-K is now on file</b>: an '
 'incident identified <b>August&nbsp;25</b> has caused <b>&ldquo;a global disruption to the Company&rsquo;s '
 'operations,&rdquo;</b> reaching <b>its ability to process and ship customer orders</b>, with no restoration '
 'timeline yet &mdash; wires now add that <b>Cork staff have been told to work from home</b>, while the federal '
 'board holds at <b>14 tracked KEV deadlines, 10 already past due</b> and the Oracle CVSS&nbsp;10.0 flaw due '
 'tomorrow.</span></div>')
CY_TLDR_NEW = ('<div class="tldr"><b>The Wire</b> <span><b>Boston Scientific&rsquo;s outage has now moved the '
 'stock</b>: the 8-K describes an incident identified <b>August&nbsp;25</b> causing <b>&ldquo;a global disruption '
 'to the Company&rsquo;s operations&rdquo;</b> that reaches <b>its ability to process and ship customer orders</b>, '
 'and Reuters reports the shares <b>down 5.03% at $46.90, a fresh 20-day low</b> &mdash; while the federal board '
 'holds at <b>14 tracked KEV deadlines, 10 already past due</b> and the Oracle CVSS&nbsp;10.0 flaw due '
 'tomorrow.</span></div>')
sub(CY, CY_TLDR_OLD, CY_TLDR_NEW)

BSX_CARD = ('<div class="card">\n'
 '<div class="tags">' + NEW + '<span class="tag crit">&minus;5.03%</span><span class="tag">Market impact</span></div>\n'
 '<h3>The Boston Scientific outage reaches the share price: a 20-day low, per Reuters</h3>\n'
 '<p>With the session open, the premarket band this desk carried through the morning has resolved into a '
 'regular-session figure. <b>Reuters reports Boston Scientific shares down 5.03% at $46.90, a fresh 20-day '
 'low.</b> <b>&#9888; That read is untimestamped on the page it was found on</b>, and it sits alongside &mdash; '
 'and is not merged into &mdash; the premarket snapshots already published here: <b>&minus;3.2%</b> '
 '(Investing.com, 7:10&nbsp;a.m. ET), then untimestamped reads of <b>3.5%&ndash;4%</b> and <b>5.8%</b>. '
 'Four snapshots of a moving quote, not four claims about one moment. Nothing is averaged.</p>\n'
 '<p>The wire accounts add nothing that contradicts the 8-K: detection on <b>August&nbsp;25</b>, incident-response '
 'procedures activated, third-party cybersecurity specialists engaged, no restoration timeline, and no '
 'determination yet of material impact. <b>Still no threat actor, no ransomware family, no CVE, no intrusion '
 'vector, and no assertion of data exfiltration or patient-safety impact</b> &mdash; not in the filing and not in '
 'the wires. This page asserts none of those things.</p>\n'
 '</div>\n')
sub(CY, '<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">\n',
        '<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">\n' + BSX_CARD)

# ------------------------------------------------------------------------ MMA
MM_TLDR_OLD = ('<div class="tldr"><b>Tale of the Tape</b> <span>Fight week is under way in Shanghai, where '
 '<b>Umar Nurmagomedov (20-1)</b> and <b>Song Yadong (23-9-1)</b> have had their first faceoff ahead of a '
 '<b>6:00 a.m. EDT Saturday</b> main event that UFC.com says will leave the winner <b>&ldquo;first in line to face '
 'the winner of Yan-Dvalishvili 3&rdquo;</b> &mdash; with Nurmagomedov a <b>&minus;470 favourite</b> at DraftKings '
 'and <b>Yan Xiaonan vs Denise Gomes</b> in the co-main.</span></div>')
MM_TLDR_NEW = ('<div class="tldr"><b>Tale of the Tape</b> <span>Media day in Shanghai turned theatrical &mdash; '
 '<b>Song Yadong (23-9-1) pulled his shirt off in front of Umar Nurmagomedov (20-1)</b> at Wednesday&rsquo;s '
 'faceoff and said <b>&ldquo;If I win this fight, I will get a title shot&rdquo;</b> &mdash; three days out from a '
 '<b>6:00 a.m. EDT Saturday</b> main event UFC.com says will leave the winner <b>&ldquo;first in line to face the '
 'winner of Yan-Dvalishvili 3,&rdquo;</b> with Nurmagomedov a <b>&minus;470 favourite</b> at DraftKings.</span></div>')
sub(MM, MM_TLDR_OLD, MM_TLDR_NEW)

sub(MM, '<h2>Fight week in Shanghai: Umar Nurmagomedov and Song Yadong come face to face</h2>',
        '<h2>Media day in Shanghai: Song Yadong rips his shirt off, and says the winner gets the title shot</h2>\n'
 '<p><b>The second faceoff of the week was the loud one.</b> Song Yadong and Umar Nurmagomedov came face to face '
 'again on <b>Wednesday, at UFC Shanghai media day</b>, and <b>Song pulled his shirt off in front of '
 'Nurmagomedov</b>. Song&rsquo;s line, as reported: <b>&ldquo;If I win this fight, I will get a title shot.&rdquo;</b> '
 'UFC.com has published the exchange under the title <b>&ldquo;Song Yadong: &lsquo;With This Fight I Will Get A '
 'Title Shot&rsquo;&rdquo;</b>. <b>&#9888; This is a distinct event from the Tuesday faceoff in front of the host '
 'arena reported by Yahoo Sports</b> and already carried below &mdash; two faceoffs, two days, both published. '
 '<span class="tag new">New &middot; 10:20</span></p>')

# --------------------------------------------------------------------- INDEX
sub(IX, '<h2>Boston Scientific&rsquo;s 8-K: a cyber incident that has reached its ability to ship customer orders</h2>',
        '<h2>The Boston Scientific outage reaches the share price &mdash; a 20-day low, per Reuters</h2>')
sub(IX, '<p>' + CY_TLDR_OLD.split('<span>')[1].rsplit('</span>')[0] + '</p>',
        '<p>' + CY_TLDR_NEW.split('<span>')[1].rsplit('</span>')[0] + '</p>')

sub(IX, '<h2>Hot on the headline, steady at the core &mdash; July PCE lands, and the September <i>hike</i> stays on the table</h2>',
        '<h2>Meta writes a $16.7 billion cheque, and the rest of the tape marks time into Nvidia night</h2>')
sub(IX, '<p>' + WS_TLDR_OLD.split('<span>')[1].rsplit('</span>')[0] + '</p>',
        '<p>' + WS_TLDR_NEW.split('<span>')[1].rsplit('</span>')[0] + '</p>')

sub(IX, '<h2>Fight week in Shanghai: the winner is first in line for the title</h2>',
        '<h2>Shanghai media day: Song rips his shirt off, and calls his shot</h2>')
sub(IX, '<p>' + MM_TLDR_OLD.split('<span>')[1].rsplit('</span>')[0] + '</p>',
        '<p>' + MM_TLDR_NEW.split('<span>')[1].rsplit('</span>')[0] + '</p>')

if FAIL:
    print("FAILED EDITS:")
    for f in FAIL:
        print(" -", f)
    sys.exit(1)
print("all edits applied")
