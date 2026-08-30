#!/usr/bin/env python3
"""Targeted edits onto the 5:48 PM pages -> 6:10 PM Afternoon Edition, Sun Aug 30 2026.
One job: content edits. Sources, restamp/sync and validation live in separate scripts."""
import io, sys, re

REPO = sys.argv[1]

def rd(f):
    return io.open(REPO + '/' + f, encoding='utf-8').read()

def wr(f, s):
    io.open(REPO + '/' + f, 'w', encoding='utf-8').write(s)

n = 0
def sub(h, old, new, label):
    global n
    assert h.count(old) == 1, ('ANCHOR %s: %d hits' % (label, h.count(old)))
    n += 1
    return h.replace(old, new)

# ---------------------------------------------------------------- WALL STREET
ws = rd('wallstreet-briefing.html')

WS_LEAD = (
'<h2 class="sec">The Lead</h2>\n'
'<p><span class="tag new">New &middot; 6:10 PM</span> <b>The week finally has numbers rather than adjectives '
'&mdash; and the fourth index that arrives with them is the one that will not reconcile.</b> '
'Every edition since Friday has described the week in words the sources supplied: a rotation into technology '
'and financials, health care flipping from leader to laggard, breadth thin on a daily advance&ndash;decline '
'basis. A weekly summary fetched this run puts figures on it. Against Friday&rsquo;s verified closes the three '
'indices this page publishes all close to the decimal: the <b>S&amp;P 500 rose 0.5% on the week, +37.39 points</b> '
'(7,711.76 &minus; 37.39 = 7,674.37), the <b>Dow rose 0.5%, +282.98 points</b> (53,559.99 &minus; 282.98 = '
'53,277.01), and the <b>Nasdaq Composite rose 0.8%, +221.97 points</b> (26,402.42 &minus; 221.97 = 26,180.45) '
'&mdash; and that last figure is independently corroborated, because the same source separately gives the '
'Composite&rsquo;s August 21 close as <b>26,180.45</b>. <b>Three weekly changes, three arithmetic checks, three '
'passes.</b></p>\n'
'<p>&#9888; <b>The Russell 2000 enters this page for the first time, and it fails the same check the other three '
'passed.</b> The small-cap index is the week&rsquo;s real story &mdash; it fell while the other three rose &mdash; '
'but three figures for it were returned this run and <b>no two of them close</b>. The source gives a Friday close '
'of <b>2,973.09, &minus;1.37%</b>; a weekly change of <b>&minus;1.5%, &minus;45.50 points</b>; and a prior-week '
'level of <b>3,017.87</b>. Take the prior week and subtract the point change and you get <b>2,972.37</b>, which is '
'<b>0.72 points below the close the same source states</b>. Take the prior week and the stated close instead and '
'the change is <b>&minus;44.78 points, &minus;1.48%</b> &mdash; close to &minus;1.5%, but not the &minus;45.50 '
'printed. <b>So the direction is published and the level is not.</b> The Russell 2000 fell roughly one and a half '
'percent on the week; the precise close is withheld under this page&rsquo;s standing rule that a level is printed '
'only when points, percent and level agree, and here they do not. <b>The rule exists for exactly this case, and '
'this is the first time it has bitten an index rather than a single stock.</b></p>\n'
'<p><b>What the small-cap number is worth is that it is the first hard figure under a read this page has been '
'carrying as attribution.</b> Since the 5:15 PM edition this page has printed, without adopting, a sourced view '
'that breadth had <b>stabilised on moving-average measures but stayed thin on a daily advance&ndash;decline '
'basis</b>. A week in which the S&amp;P 500 gains 0.5% while the Russell 2000 loses about 1.5% is that same '
'observation expressed as a spread of about two percentage points between large caps and small &mdash; a '
'concrete measurement where the page previously had only a characterisation. &#9888; <b>It corroborates the '
'description and not the forecast attached to it.</b> The read that came with the breadth line held that thin '
'participation precedes <b>either</b> a catch-up rally <b>or</b> a rougher stretch; a two-point divergence is '
'evidence that participation is in fact narrow, and it is <b>no evidence at all</b> about which of the two '
'branches follows. <b>The fork stays a fork.</b></p>\n'
)

ws = sub(ws, '<h2 class="sec">The Lead</h2>\n', WS_LEAD, 'ws-lead')

WS_TLDR_OLD = re.search(r'<div class="tldr">.*?</div>', ws, re.S).group(0)
WS_TLDR_NEW = (
'<div class="tldr"><b>The Tape</b> <span>The week stops being described and starts being counted: against '
'Friday&rsquo;s closes the <b>S&amp;P 500 rose 0.5% (+37.39)</b>, the <b>Dow 0.5% (+282.98)</b> and the '
'<b>Nasdaq Composite 0.8% (+221.97)</b>, all three reconciling to the decimal and the Composite&rsquo;s '
'prior-week level independently corroborated at <b>26,180.45</b> &mdash; while the <b>Russell 2000, arriving on '
'this page for the first time, fails that same check</b>: its stated close (<b>2,973.09</b>), its stated weekly '
'change (<b>&minus;45.50 points</b>) and its stated prior week (<b>3,017.87</b>) are mutually inconsistent by '
'<b>0.72 points</b>, so the direction is published (<b>down about 1.5%</b>) and <b>the level is withheld</b>; the '
'gap that survives is the useful part &mdash; a <b>two-percentage-point large-cap-over-small-cap spread</b> is the '
'first hard number under the <b>thin-breadth</b> read this page has carried as attribution since 5:15 PM, and it '
'corroborates <b>the description without settling the fork attached to it</b>. Friday&rsquo;s closes stand for a '
'<b>twenty-eighth verification</b> (<b>S&amp;P 500 7,711.76 &minus;0.25%</b>, <b>Nasdaq Composite 26,402.42 '
'&minus;0.52%</b>, <b>Dow 53,559.99 &minus;0.02%</b>).</span></div>'
)
ws = sub(ws, WS_TLDR_OLD, WS_TLDR_NEW, 'ws-tldr')
wr('wallstreet-briefing.html', ws)

# ---------------------------------------------------------------------- CYBER
cy = rd('cyber-briefing.html')

CY_CARDS = (
'<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">\n'
'<div class="card"><div class="tags"><span class="tag new">New &middot; 6:10 PM</span>'
'<span class="tag warn">Leak-site claims &mdash; unconfirmed</span><span class="tag">Extortion</span></div>'
'<h3>Three fresh listings, one tracker, and not one of them confirmed by the company named</h3>'
'<p><b>What was returned.</b> A leak-site tracker fetched this run lists three victims posted in the last days of '
'August. <b>Questal</b>, a <b>Paris-based IT services provider</b>, is claimed by <b>ShinyHunters</b>, which says '
'it took <b>more than 21 million Salesforce records</b> including personal data plus <b>147 GB of internal '
'corporate data</b>. <b>Hyundai Motor T&uuml;rkiye</b> is claimed by <b>CRPx0</b>, which says it took <b>more than '
'1.5 GB of recruitment and personnel data</b>. <b>ProHealth Medical Group</b> is claimed by <b>Krybit</b>, which '
'says it took <b>more than 114 GB</b>.</p>'
'<p>&#9888; <b>Every number in the paragraph above is the attacker&rsquo;s.</b> These are entries on extortion '
'leak sites, which are <b>advertisements</b>: the group chooses what to claim, when to post it, and whether the '
'victim is named accurately. <b>No statement from Questal, Hyundai Motor T&uuml;rkiye or ProHealth Medical Group '
'was returned by anything fetched this run</b>, and none of the three claims has been corroborated by a second '
'source. They are carried because a listing is itself a fact &mdash; the posting happened &mdash; and they are '
'carried at that weight and no more. <b>A leak-site count is a count of claims, not of breaches</b>, which is the '
'same caveat this page attached to TITAN&rsquo;s 24-victim tally below, and it applies here for the same '
'reason.</p>'
'<p><b>One of the three is worth a second look for a reason that has nothing to do with the tracker.</b> The '
'Questal listing attributes a <b>Salesforce-record</b> theft to <b>ShinyHunters</b> &mdash; a group and a target '
'platform this page has already been carrying in another context. That does not make the claim true, and this '
'page does not treat consistency with a story it already tells as corroboration; <b>a claim that fits the pattern '
'is exactly the claim easiest to make</b>. It is flagged as a thread to check when a named source appears, not '
'as a confirmed extension of the campaign.</p></div>\n'
)
cy = sub(cy, '<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">\n', CY_CARDS, 'cy-breach')

# Refusals appended to the NetScaler paragraph in Vulnerability Watch
CY_ANCHOR = 'Verify against Citrix advisory <b>CTX696604</b> before you act on either.'
CY_NEW = (
CY_ANCHOR +
'</div><div class="note" style="margin-top:12px"><b>New at 6:10 PM &mdash; a second CVE ships in the same fix, '
'and it does not belong on the deadline board.</b> The advisory coverage fetched this run states that the '
'recommended builds <b>14.1-73.32 and later</b> and <b>13.1-63.21 and later</b> carry the fix for <b>CVE-2026-8452 '
'as well as a companion authentication-bypass flaw, CVE-2026-19490</b>. &#9888; <b>Nothing fetched this run states '
'that CVE-2026-19490 is exploited, and it is not in the KEV catalogue</b>, so it is recorded here and <b>not</b> '
'added to the federal-deadline list below &mdash; the same line this page drew for the Splunk flaw and for the '
'NVIDIA GPU issue. It matters operationally rather than for the countdown: if you are patching for 8452 you are '
'already patching for this, and if you have applied a mitigation instead of the build, <b>you have not</b>. '
'<b>Also newly stated: the exposure precondition.</b> The flaw is reachable when the appliance is configured as a '
'<b>Gateway</b> &mdash; covering <b>SSL VPN, ICA Proxy, CVPN or RDP Proxy</b> &mdash; <b>or as an AAA virtual '
'server</b>. An appliance in neither role is not in scope for this one, which is the first statement on this page '
'that lets a reader rule themselves <i>out</i> rather than only in.</div>'
)
assert cy.count(CY_ANCHOR) == 1
cy = sub(cy, CY_ANCHOR + '</div>', CY_NEW, 'cy-netscaler')

CY_TLDR_OLD = re.search(r'<div class="tldr">.*?</div>', cy, re.S).group(0)
CY_TLDR_NEW = (
'<div class="tldr"><b>The Wire</b> <span>Three fresh extortion listings arrive and all three are published at the '
'weight of a claim rather than a breach: <b>ShinyHunters</b> says it took <b>21 million Salesforce records and '
'147 GB</b> from the Paris IT provider <b>Questal</b>, <b>CRPx0</b> says <b>1.5 GB</b> of personnel data from '
'<b>Hyundai Motor T&uuml;rkiye</b>, and <b>Krybit</b> says <b>114 GB</b> from <b>ProHealth Medical Group</b> '
'&mdash; <b>every figure the attacker&rsquo;s own, none confirmed by the company named</b>, and the Questal entry '
'flagged rather than folded into a campaign this page already tracks, because <b>a claim that fits the pattern is '
'the easiest claim to make</b>; separately the NetScaler fix is now known to close <b>a second flaw, '
'CVE-2026-19490</b>, which is <b>recorded and deliberately kept off the deadline board</b> since nothing fetched '
'calls it exploited, and the newly stated exposure precondition &mdash; <b>Gateway (SSL VPN, ICA Proxy, CVPN, RDP '
'Proxy) or an AAA virtual server</b> &mdash; is the first line here that lets a reader rule themselves <i>out</i>. '
'<b>Nevada was refused an eleventh time and an uncorroborated Iran-linked infrastructure claim a first.</b></span></div>'
)
cy = sub(cy, CY_TLDR_OLD, CY_TLDR_NEW, 'cy-tldr')
wr('cyber-briefing.html', cy)

# ------------------------------------------------------------------------ MMA
mma = rd('mma-briefing.html')

MMA_ANCHOR = 'Parnasse&rsquo;s record returned again as <b>23-2</b>'
MMA_NEW = (
'<b>New at 6:10 PM &mdash; a fourth rendering arrives, and it is the first one whose <i>stage</i> is stated.</b> '
'<b>FightOdds.io</b> gives what it labels the <b>opening odds</b> for UFC Fight Night 287: <b>Parnasse &minus;357 '
'/ Hooker +275</b>. That is a price this page has not carried, and it sits <b>below all three of the lines already '
'here</b> (&minus;400, &minus;428, &minus;500). <b>The reason it matters is that it is dated by kind rather than '
'by clock.</b> An opener is by definition the first number a book posts, so a set of later quotes that are all '
'shorter on the same fighter is what a line looks like when money arrives on the favourite &mdash; which would '
'explain a spread this page has twice called unusually wide as <b>partly a spread across time rather than across '
'books</b>. &#9888; <b>That explanation is offered and not adopted, and the gap in it is precise:</b> none of the '
'other three lines is dated by its source, so <b>this page cannot establish that they are later than the opener</b>. '
'If they are, the spread narrows to a normal story about a line moving. If they are not, four books simply '
'disagree by 143 points on the favourite. <b>The opener is printed as a fourth line, not as the key to the other '
'three.</b> '
'&#9888; <b>And one listing this run got the pair right and the fighters wrong.</b> An aggregated card summary '
'fetched this run reported <b>&ldquo;Hooker &minus;500, Parnasse +375&rdquo;</b> &mdash; the <b>same two numbers</b> '
'this page carries from the UFC&rsquo;s own listing, <b>assigned to the opposite men</b>, making the promotional '
'debutant the underdog and Hooker a heavy favourite. It is refuted by everything else fetched this run: the '
'BetWay line, the consensus line and the FightOdds.io opener all price <b>Parnasse</b> as the favourite, and this '
'page had already reasoned from the official billing that the underdog is named first. <b>This is a new failure '
'mode for this page to log</b> &mdash; not a wrong number and not a stale one, but a correctly transcribed pair '
'attached to the wrong names, which no arithmetic check would catch and only a second source can. '
'Parnasse&rsquo;s record returned again as <b>23-2</b>'
)
mma = sub(mma, MMA_ANCHOR, MMA_NEW, 'mma-odds')

MMA_TLDR_OLD = re.search(r'<div class="tldr">.*?</div>', mma, re.S).group(0)
MMA_TLDR_NEW = (
'<div class="tldr"><b>Tale of the Tape</b> <span><b>A fourth UFC Paris line arrives and it is the first whose '
'<i>stage</i> is stated:</b> FightOdds.io&rsquo;s <b>opening</b> price of <b>Parnasse &minus;357 / Hooker +275</b> '
'sits below all three quotes already carried (&minus;400, &minus;428, &minus;500), which is what a line looks like '
'when money lands on the favourite &mdash; <b>offered as an explanation for a spread twice called unusually wide, '
'and not adopted</b>, because <b>none of the other three is dated</b> and so cannot be shown to be later than the '
'opener. &#9888; <b>Separately, one listing this run got the numbers right and the fighters wrong</b>, reporting '
'<b>&ldquo;Hooker &minus;500, Parnasse +375&rdquo;</b> &mdash; the same pair this page carries, <b>assigned to the '
'opposite men</b> &mdash; refuted by every other return; <b>a correctly transcribed pair attached to the wrong '
'names is a failure no arithmetic check catches and only a second source can</b>. The <b>champions board is '
'unchanged for a sixty-ninth consecutive edition</b> after a <b>twelfth cross-check against ESPN</b>, which this '
'time returned <b>eight</b> of the eleven cells &mdash; <b>Aspinall, Ulberg, Strickland, Makhachev, Gaethje, '
'Volkanovski, Yan and Van</b> &mdash; with title dates <b>and defence counts</b> matching this page; the other '
'three rest on the checks recorded beneath it.</span></div>'
)
mma = sub(mma, MMA_TLDR_OLD, MMA_TLDR_NEW, 'mma-tldr')
wr('mma-briefing.html', mma)

print('edits applied:', n)
