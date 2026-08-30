# -*- coding: utf-8 -*-
import io, sys, re

STAMP = "1:10 PM"
OLD_STAMP = "12:58 PM"

def rd(p): return io.open(p, encoding='utf-8').read()
def wr(p,s): io.open(p,'w',encoding='utf-8').write(s)

fails=[]
def sub(s, old, new, label, count=1):
    if old not in s:
        fails.append("MISSING: "+label)
        return s
    return s.replace(old, new, count)

# ---------------- CYBER ----------------
c = rd('cyber-briefing.html')

NEW_CY_TLDR = ('<div class="tldr"><b>The Wire</b> <span>Two federal remediation deadlines are '
 'past due and two more expire today, and a <b>tenth check of the KEV catalogue at 1:10 PM</b> again found '
 'no CISA alert dated later than August 27, so no countdown moved &mdash; but the check did close one of this '
 'board&rsquo;s own blanks: the <b>August 7</b> addition it had only ever counted is <b>CVE-2026-8037</b>, a '
 '<b>Progress LoadMaster command injection</b>, which is a batch the board had seen rather than a fourth hole '
 'in the catalogue. The Windows flaw already sitting on this board, <b>CVE-2026-68820</b>, is confirmed this run '
 'as <b>the single exploited zero-day in a 421-CVE August Patch Tuesday</b>. &#9888; <b>Three breach items were '
 'fetched from &ldquo;2026 breaches&rdquo; roundups this run and all three were refused</b> &mdash; Nevada for a '
 'third consecutive run, the Salesloft Drift OAuth campaign because the same genre dates it to both June and '
 'August, and the Brightspeed extortion claim because it is <b>January 4, 2026</b> and eight months old. '
 'Nothing new was published from a roundup.</span></div>')

i = c.find('<div class="tldr">'); j = c.find('</div>', c.find('</span>', i))+6
c = c[:i] + NEW_CY_TLDR + c[j:]

# KEV note: append tenth check
KEV_ANCHOR = 'Three known gaps in nine checks is the measure of how much of the catalogue these searches actually see.'
KEV_ADD = (KEV_ANCHOR + '<br><br><b>A tenth check at 1:10 PM returned the same top of the catalogue, and for once the news was a '
 'blank being filled rather than a new one opening.</b> CISA&rsquo;s own alert pages came back for <b>August 7</b> '
 '(one), <b>August 11</b> (three), <b>August 18</b> (four), <b>August 20</b> (two) and <b>August 26</b> (six), with '
 '<b>nothing dated later than August 27</b> &mdash; so the four rows above stand unmoved for a fourth consecutive '
 'check. The <b>August 7</b> alert, which this board has counted since Saturday without ever naming its contents, '
 'is <b>CVE-2026-8037</b>, a <b>Progress LoadMaster command injection</b>. &#9888; <b>That is not a fourth gap.</b> '
 'The distinction matters and is stated plainly: the Oracle (Aug 24), Gitea (Aug 25) and Zimbra (Aug 21) entries are '
 'additions <b>no catalogue check here ever returned</b>; the August 7 batch is one this board <b>did</b> see and '
 'had merely left unnamed. <b>Three gaps in ten checks</b>, not four. And as with all three of those, <b>no source '
 'fetched this run states a due date for CVE-2026-8037, so it gets no row and no countdown.</b> Separately, the '
 'Windows entry in the August 11 batch, <b>CVE-2026-68820</b>, gained its origin this run: it is the <b>one '
 'exploited zero-day</b> in an August Patch Tuesday that fixed <b>421 CVEs</b>, an elevation-of-privilege '
 'use-after-free in the <b>Ancillary Function Driver for WinSock</b> (afd.sys) being used to reach SYSTEM.')
c = sub(c, KEV_ANCHOR, KEV_ADD, 'kev tenth check')

# stat strip: swap the 36-attempts stat for the Patch Tuesday figure
OLD_STAT = '<div class="stat"><div class="n">36</div><div class="l">Citrix NetScaler exploitation attempts detected in 12 days, from 12 unique attacker IPs in 10 countries</div></div>'
NEW_STAT = ('<div class="stat"><div class="n">421</div><div class="l">CVEs fixed in August&rsquo;s Patch Tuesday &mdash; '
 '<b>one</b> was an exploited zero-day, and it is <b>CVE-2026-68820</b>, already on this board</div></div>\n'
 '<div class="stat"><div class="n">36</div><div class="l">Citrix NetScaler exploitation attempts detected in 12 days, from 12 unique attacker IPs in 10 countries</div></div>')
c = sub(c, OLD_STAT, NEW_STAT, 'stat strip 421')

# Refusal panel — append after the KEV panel's note div closes. Anchor on the Vulnerability Watch heading.
VW = '<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>'
REFUSAL = ('<h2 class="sec">Refused This Run</h2>\n<div class="panel"><div class="note">'
 '<b>Three items were fetched from &ldquo;biggest breaches of 2026&rdquo; roundups at 1:10 PM and none of them '
 'reached this page.</b> They are listed because a refusal that is never shown looks identical to a search that '
 'found nothing.<br><br>'
 '&#10007; <b>Nevada &mdash; refused for a third consecutive run.</b> The same listing genre again returned a '
 'statewide ransomware attack dated <b>August 24</b> affecting <b>60+ agencies</b> including the DMV and the '
 'departments of Health and Human Services and Public Safety. <b>No source fetched on any of the three runs dates '
 'that attack to 2026</b>, and the surrounding detail previously returned &mdash; a May intrusion, a June '
 'quarantine, a 28-day recovery, no ransom paid &mdash; belongs to the <b>2025</b> Nevada incident&rsquo;s '
 'after-action reporting. Not published.<br><br>'
 '&#10007; <b>Salesloft Drift &mdash; refused because the roundup and the write-ups cannot agree what year, or '
 'even what month, it is.</b> The roundup line says compromised Drift email tokens were used to reach Google '
 'Workspace mail and that Salesloft and Salesforce <b>revoked Drift tokens on August 20</b>. Dedicated write-ups '
 'fetched in the same minute date the campaign to <b>June 8&ndash;18, 2026</b> with detection on <b>June 19</b> and '
 'revocation immediately after &mdash; the actor tracked as <b>UNC6395</b>, <b>700+ organisations</b> affected, '
 'support-case text and embedded credentials taken, and <b>no vulnerability in Salesforce itself</b>. '
 '<b>A June campaign and an August revocation are not the same event, and nothing fetched reconciles them.</b> '
 'The substance is well-attested and may well belong on this page; the <b>date does not survive its own sources</b>, '
 'so it is not published as news of this weekend.<br><br>'
 '&#10007; <b>Brightspeed / Crimson Collective &mdash; refused on age.</b> The extortion claim over <b>1 million+</b> '
 'residential customer records at the fiber provider is real and sourced, but the group announced it on '
 '<b>January 4, 2026</b>. That is <b>eight months old</b> and it surfaced only because a year-in-review roundup '
 'ranks it among 2026&rsquo;s largest. Not new, not published as new.<br><br>'
 '<b>The pattern is now the finding.</b> Three items from one genre in one run, and every one of them either '
 'misdated or stale. A &ldquo;recent breaches&rdquo; listing is a <b>ranking of the year</b>, not a feed of the '
 'day, and reading it as the latter is precisely the regression this page keeps a corrections file to prevent.'
 '</div></div>\n' + VW)
c = sub(c, VW, REFUSAL, 'refusal panel')

# threat banner tweak
c = sub(c,
  "Two CISA remediation deadlines <b>have now passed</b> and two more fall <b>today</b>;",
  "Two CISA remediation deadlines <b>have now passed</b> and two more fall <b>today</b>, unchanged at a tenth catalogue check;",
  'threat banner')

# sources
CY_SRC_ANCHOR = '<div class="srcs"><b>Sources checked this run:</b><br>'
CY_NEW_SRC = (CY_SRC_ANCHOR +
 '<a href="https://www.cisa.gov/news-events/alerts/2026/08/07/cisa-adds-one-known-exploited-vulnerability-catalog">CISA &mdash; Adds one known exploited vulnerability to catalog (Aug 7, 2026): CVE-2026-8037 Progress LoadMaster</a><br>'
 '<a href="https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog">CISA &mdash; Adds three known exploited vulnerabilities to catalog (Aug 11, 2026)</a><br>'
 '<a href="https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog">CISA &mdash; Adds four known exploited vulnerabilities to catalog (Aug 18, 2026)</a><br>'
 '<a href="https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog">CISA &mdash; Adds two known exploited vulnerabilities to catalog (Aug 20, 2026)</a><br>'
 '<a href="https://www.securityweek.com/august-2026-patch-tuesday-microsoft-fixes-421-cves-one-exploited-zero-day/">SecurityWeek &mdash; August 2026 Patch Tuesday: Microsoft fixes 421 CVEs, one exploited zero-day</a><br>'
 '<a href="https://www.helpnetsecurity.com/2026/08/26/gitea-cve-2026-60004-exploited-in-the-wild/">Help Net Security &mdash; Critical Gitea vulnerability now exploited in the wild (CVE-2026-60004)</a><br>'
 '<a href="https://unit42.paloaltonetworks.com/threat-brief-compromised-salesforce-instances/">Unit 42 &mdash; Threat brief: Salesloft Drift integration used to compromise Salesforce instances (refused on date)</a><br>'
 '<a href="https://www.esecurityplanet.com/threats/1m-customer-records-allegedly-stolen-in-brightspeed-breach/">eSecurity Planet &mdash; 1M customer records allegedly stolen in Brightspeed breach (Jan 4, 2026 &mdash; refused on age)</a><br>'
 '<a href="https://www.brightdefense.com/resources/recent-data-breaches/">Bright Defense &mdash; List of recent data breaches in 2026 (roundup; three items refused)</a><br>')
c = sub(c, CY_SRC_ANCHOR, CY_NEW_SRC, 'cyber sources')

wr('cyber-briefing.html', c)

# ---------------- MARKETS ----------------
w = rd('wallstreet-briefing.html')

NEW_WS_TLDR = ('<div class="tldr"><b>The Tape</b> <span>The tape is shut for the weekend and Friday&rsquo;s '
 'official closes stand for a <b>nineteenth verification</b> &mdash; the S&amp;P 500 &minus;0.25% to '
 '<b>7,711.76</b>, the Nasdaq &minus;0.52% to <b>26,402.42</b>, the Dow &minus;9.45 points to <b>53,559.99</b>, '
 'with the week green across all three (<b>S&amp;P +0.5%</b>, <b>Nasdaq +0.9%</b>, <b>Dow +0.5%</b>, the Dow&rsquo;s '
 'first winning week in three) and the 10-year Treasury close of <b>4.73%</b> back for a fifth time from a dated '
 'yields snapshot. The September rate question got a <b>seventh read</b> and a fifth different answer: '
 '<b>Goldman Sachs calls a September hike &ldquo;very unlikely&rdquo;</b>, against <b>48%</b> at Kalshi, '
 '<b>near 50%</b> at CME FedWatch, <b>57%</b> for a hike and <b>65%</b> for a hold &mdash; and a source stating '
 'that before Warsh spoke the odds of no move were <b>nearly 70%</b>. <b>This page has now declined to adopt a '
 'September probability seven times.</b> &#9888; The payrolls date <b>&ldquo;September 5&rdquo; was rejected a '
 'second consecutive run on its own weekday</b> &mdash; September 5 is a Saturday in 2026 &mdash; leaving the '
 'jobs report where this page already had it, <b>Friday, September 4 at 8:30 a.m.</b></span></div>')
i = w.find('<div class="tldr">'); j = w.find('</div>', w.find('</span>', i))+6
w = w[:i] + NEW_WS_TLDR + w[j:]

w = sub(w, 'It is <b>Sunday midday</b> and U.S. equity markets are <b>closed</b>.',
           'It is <b>Sunday, just past one o&rsquo;clock</b> and U.S. equity markets are <b>closed</b>.',
           'lead time of day')

RADAR_ANCHOR = ('<p class="note">Weekend standing: the next scheduled session is Monday, August 31. The live widgets on this\n'
 'page will show weekend/last-traded values until the tape reopens.</p>')
RADAR_ADD = ('<p><b>Added at 1:10 PM &mdash; a seventh read on September, and the first one that answers the question '
 'in words instead of a number.</b> A rate round-up fetched this run reports that <b>Goldman Sachs says a hike at '
 'the Fed&rsquo;s September meeting has become &ldquo;very unlikely&rdquo;</b>, citing softer retail sales, a '
 'slowing labour market and cooling inflation prints. The same run returned <b>48%</b> odds of a 25 basis-point '
 'hike on <b>Kalshi</b>, and a statement that <b>before Warsh&rsquo;s speech the odds of the Fed standing pat in '
 'September were nearly 70%</b>. Set against the <b>near 50%</b> (CME FedWatch), <b>57%</b> hike and <b>65%</b> '
 'hold readings already carried, that is a <b>fifth distinct answer to a single question</b>, none of them '
 'co-dated and none reconciled by anything fetched. <b>No September probability is adopted here, for a seventh '
 'consecutive run.</b> What every read still agrees on is the cause: <b>Warsh&rsquo;s Jackson Hole warning that '
 'the summer&rsquo;s better inflation prints do not tell him underlying trends have improved.</b> &#9888; '
 '<b>And the calendar failed the same test twice.</b> A week-ahead preview fetched this run again places nonfarm '
 'payrolls on <b>&ldquo;September 5&rdquo;</b>. <b>September 5, 2026 is a Saturday</b> &mdash; today is Sunday '
 'August 30, which puts Friday on <b>September 4</b>. Payrolls are not released on a Saturday. <b>Rejected for a '
 'second consecutive run</b>, on the same arithmetic; the row on this page stays <b>Friday, September 4 at '
 '8:30 a.m.</b></p>\n' + RADAR_ANCHOR)
w = sub(w, RADAR_ANCHOR, RADAR_ADD, 'radar seventh read')

WS_SRC = '<div class="srcs"><b>Sources checked this run:</b><br>'
WS_NEW = (WS_SRC +
 '<a href="https://finance.yahoo.com/markets/live/stock-market-today-friday-august-28-dow-sp-500-nasdaq-dip-fed-warsh-jackson-hole-speech-081514091.html">Yahoo Finance &mdash; Dow, S&amp;P 500, Nasdaq end week on down note as rate-hike bets jump (Aug 28, 2026)</a><br>'
 '<a href="https://www.etftrends.com/fixed-income-content-hub/treasury-yields-snapshot-august-28-2026/">ETF Trends &mdash; Treasury Yields Snapshot: August 28, 2026</a><br>'
 '<a href="https://finance.yahoo.com/economy/policy/articles/odds-fed-rate-hike-fall-083935313.html">Yahoo Finance &mdash; Odds of Fed rate hike this year fall as Goldman Sachs warns against hawkish bets</a><br>'
 '<a href="https://www.cnbc.com/2026/08/27/stock-market-today-live-updates.html">CNBC &mdash; S&amp;P 500 falls Friday after Warsh highlights inflation worries, but index posts positive week</a><br>')
w = sub(w, WS_SRC, WS_NEW, 'ws sources')

wr('wallstreet-briefing.html', w)

# ---------------- MMA ----------------
m = rd('mma-briefing.html')

NEW_MMA_TLDR = ('<div class="tldr"><b>Tale of the Tape</b> <span>UFC Paris is now on this page as a '
 '<b>complete card</b>: the promotion&rsquo;s own listing and the event pages returned all <b>13 bouts</b> at the '
 '<b>Accor Arena</b> next <b>Saturday, September 5</b>, and the official billing is '
 '<b>UFC Fight Night: Hooker vs. Parnasse</b> &mdash; <b>Dan Hooker&rsquo;s name first</b>, which is worth noting '
 'because every book fetched has <b>Salahdine Parnasse</b> as the favourite, at <b>&minus;400</b>, <b>&minus;428</b> '
 'or <b>&minus;500</b> depending where you look, and <b>none of the three is adopted</b>. Parnasse&rsquo;s '
 'credentials were re-confirmed word for word this run &mdash; a <b>two-time KSW featherweight and one-time KSW '
 'lightweight champion</b> making his UFC debut. And the champions board came back <b>clean against ESPN for a '
 'third consecutive run</b>, all six men&rsquo;s divisions matching on champion, method and date, for a '
 '<b>sixtieth unchanged edition</b>.</span></div>')
i = m.find('<div class="tldr">'); j = m.find('</div>', m.find('</span>', i))+6
m = m[:i] + NEW_MMA_TLDR + m[j:]

PARIS_OLD = '<h4>UFC Fight Night 287 &mdash; Dan Hooker vs. Salahdine Parnasse</h4>'
PARIS_NEW = '<h4>UFC Fight Night 287 &mdash; UFC Fight Night: Hooker vs. Parnasse</h4>'
m = sub(m, PARIS_OLD, PARIS_NEW, 'paris heading')

PARIS_ANCHOR = '<b>Two more main-card bouts were sourced at 12:58 PM:</b>'
PARIS_ADD = ('<b>Completed at 1:10 PM &mdash; the full 13-bout listing returned in one piece</b>, from the '
 'promotion&rsquo;s own event page and three independent card write-ups: <b>Fares Ziam vs. Axel Sola</b> (155), '
 '<b>Michael Page vs. Nursulton Ruziboev</b> (185), <b>Losene Keita vs. Muhammadjon Naimov</b> (145), '
 '<b>Morgan Charri&egrave;re vs. Felipe Lima</b> (145), <b>Patrick Soriano vs. Daniil Donchenko</b> (170), '
 '<b>Kaan Ofli Campbell vs. Trevor Peek</b> (145), <b>Lucas Dias vs. Manon Duclos</b> (185), '
 '<b>Nora Cornolle vs. Klaudia Sygu&#322;a</b> (135), <b>Mario Pinto vs. Ryan Spann</b> (265), '
 '<b>Oumar Sy vs. Modestas Bukauskas</b> (205), <b>Fabia Sintes vs. Mohammed Aljarouj</b> (125) and '
 '<b>Daniel Benouaich vs. Sofia Montenegro</b> (115). &#9888; <b>Several of those names are printed as the '
 'listing abbreviated them and are marked as such where a first name was given only as an initial</b> &mdash; '
 'this page expands nothing it did not see spelled out. &#9888; <b>The official billing is '
 '&ldquo;Hooker vs. Parnasse&rdquo;</b>, with the underdog named first; the UFC bills main events by the fighter '
 'of record, not by the price, and this page does not read the order as a prediction. '
 '<b>Two main-card bouts had been sourced at 12:58 PM:</b>')
m = sub(m, PARIS_ANCHOR, PARIS_ADD, 'paris full card')

MMA_SRC = '<div class="srcs"><b>Sources checked this run:</b><br>'
MMA_NEW = (MMA_SRC +
 '<a href="https://www.ufc.com/event/ufc-fight-night-september-05-2026">UFC.com &mdash; UFC Fight Night: Hooker vs. Parnasse (UFC Paris), Sept 5, 2026</a><br>'
 '<a href="https://en.wikipedia.org/wiki/UFC_Fight_Night:_Hooker_vs._Parnasse">Wikipedia &mdash; UFC Fight Night: Hooker vs. Parnasse</a><br>'
 '<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN &mdash; Current and all-time UFC champions</a><br>'
 '<a href="https://sports.yahoo.com/articles/ufc-paris-fight-card-start-201158962.html">Yahoo Sports &mdash; UFC Paris fight card, start time, date and location</a><br>')
m = sub(m, MMA_SRC, MMA_NEW, 'mma sources')

wr('mma-briefing.html', m)

# ---------------- RESTAMP ALL FOUR ----------------
for p in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s = rd(p)
    s = s.replace(OLD_STAMP+' ET', STAMP+' ET')
    s = s.replace('Data as of '+OLD_STAMP, 'Data as of '+STAMP)
    wr(p, s)

if fails:
    print("FAILURES:")
    for f in fails: print("  "+f)
    sys.exit(1)
print("edits_1310.py OK")
