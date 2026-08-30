#!/usr/bin/env python3
"""Targeted edits for the 2026-08-30 5:10 PM ET Afternoon Edition (TENTH run of the day).

Every string inserted below traces to a source fetched THIS run, or to a sourced
CORRECTIONS.md entry, per the FACT-CHECK GATE.
"""
import re, sys, os

D = sys.argv[1] if len(sys.argv) > 1 else "."
STAMP = "5:10 PM"

def rd(p):
    return open(os.path.join(D, p), encoding="utf-8").read()

def S(t):
    return t.replace("@@S@@", STAMP)


def wr(p, s):
    s = S(s)
    assert "@@S@@" not in s, p + ": unresolved stamp token"
    open(os.path.join(D, p), "w", encoding="utf-8").write(s)

def once(h, needle, new, label):
    """Replace exactly one occurrence; fail loudly otherwise."""
    n = h.count(needle)
    assert n == 1, "%s: expected 1 occurrence, found %d" % (label, n)
    return h.replace(needle, new)

def append_tldr(h, add, label):
    """Append to the .tldr span, anchored on its closing tags."""
    m = re.search(r'(<div class="tldr">.*?)(</span></div>)', h, re.S)
    assert m, label + ": no tldr found"
    assert "<p>" not in m.group(1), label + ": tldr swallowed a paragraph"
    return h[:m.start(2)] + " " + add + h[m.start(2):]


# ─────────────────────────────────────────────────────────────────────────────
# WALL STREET
# ─────────────────────────────────────────────────────────────────────────────
ws = rd("wallstreet-briefing.html")

# (1) THE HEADLINE OF THIS EDITION: PayPal's FRIDAY CLOSING move is finally sourced.
# Investing.com market-cap movers (-12.63%) + Seeking Alpha / CNBC midday ("fell 13%").
# Every prior edition could print only the premarket -16% and said so explicitly.
ws_tldr = (
    '<b>New at @@S@@:</b> <b>the number this page has refused for eleven editions finally '
    'has a source &mdash; PayPal&rsquo;s Friday <i>closing</i> move.</b> Every edition since '
    'Friday morning carried the buyout collapse with a <b>premarket</b> figure only, and said in '
    'three places that <b>no closing percentage had been stated by any source</b>. Two independent '
    'reads now give one: <b>&minus;12.63%</b> on a market-cap movers wrap and <b>&ldquo;fell '
    '13%&rdquo;</b> on a session recap &mdash; <b>the same move at two precisions, not two '
    'claims</b>, since 12.63 rounds to 13. The premarket &minus;16% stays on the page beside it, '
    'because the gap between the two is itself the story: <b>the sell-off narrowed by roughly a '
    'third between the open and the bell</b>. Also sharpened this run: <b>Marvell &minus;10.66%</b> '
    '(this page had carried &minus;10%), and a Friday gainer it had not carried at all, '
    '<b>Elastic</b>, which returned as <b>+20.34%</b> on one wrap and <b>&ldquo;surged 21%&rdquo;</b> '
    'on another &mdash; <b>recorded as two renderings, neither adopted</b>. <b>Nvidia finished the '
    'week higher by more than 1%</b> despite Friday&rsquo;s decline, on the strength of '
    'Thursday&rsquo;s <b>+8.7%</b>. And the September rate question drew a <b>thirteenth read</b>: '
    '<b>Polymarket at 49% for a hike</b>, a <b>third</b> rendering from that venue against the '
    '<b>52% hold</b> and <b>48% hike</b> already carried &mdash; <b>recorded, not adopted, for a '
    'thirteenth consecutive run</b>.'
)
ws = append_tldr(ws, S(ws_tldr), "ws tldr")

# (2) New Lead paragraph.
lead_anchor = '</p>\n</div><h2 class="sec">Movers &amp; Drivers</h2>'
if lead_anchor not in ws:
    # fall back: insert immediately before the Movers heading
    lead_anchor = '<h2 class="sec">Movers &amp; Drivers</h2>'
    lead_new = (
        '<p><span class="tag new">New &middot; @@S@@</span> <b>A refusal ends: PayPal&rsquo;s Friday '
        'close is on the page, and the premarket figure stays next to it.</b> This page has said, '
        'edition after edition, that the only PayPal number anyone had published for Friday was a '
        '<b>premarket</b> one &mdash; shares down as much as <b>16%</b> before the open after '
        'Stripe and Advent walked away from a bid worth more than <b>$50 billion</b>. Two wraps '
        'fetched this run close the gap: PayPal ended the session <b>&minus;12.63%</b>, described '
        'elsewhere as having <b>&ldquo;fell 13%&rdquo;</b>. Those are not competing claims &mdash; '
        'they are the same move quoted to two decimal places and to none. What the pair makes '
        'visible is something neither number shows alone: <b>the decline that opened near 16% '
        'closed near 13%</b>, so roughly a third of the premarket damage was bought back during '
        'the day. Both figures now sit on the mover card, each labelled with the moment it '
        'describes.</p>\n')
    ws = once(ws, lead_anchor, S(lead_new) + lead_anchor, "ws lead")
else:
    lead_new = (
        '</p>\n<p><span class="tag new">New &middot; @@S@@</span> <b>A refusal ends: PayPal&rsquo;s '
        'Friday close is on the page, and the premarket figure stays next to it.</b> This page has '
        'said, edition after edition, that the only PayPal number anyone had published for Friday '
        'was a <b>premarket</b> one &mdash; shares down as much as <b>16%</b> before the open '
        'after Stripe and Advent walked away from a bid worth more than <b>$50 billion</b>. Two '
        'wraps fetched this run close the gap: PayPal ended the session <b>&minus;12.63%</b>, '
        'described elsewhere as having <b>&ldquo;fell 13%&rdquo;</b>. Those are not competing '
        'claims &mdash; they are the same move quoted to two decimal places and to none. What the '
        'pair makes visible is something neither number shows alone: <b>the decline that opened '
        'near 16% closed near 13%</b>, so roughly a third of the premarket damage was bought '
        'back during the day. Both figures now sit on the mover card, each labelled with the '
        'moment it describes.</p>\n</div><h2 class="sec">Movers &amp; Drivers</h2>')
    ws = once(ws, lead_anchor, S(lead_new), "ws lead")

# (3) Rewrite the PayPal mover card: premarket + close, both labelled.
pypl_old = ('<div class="card"><div class="tags"><span class="tag">Carried</span>'
            '<span class="tag">Premarket</span></div>')
pypl_new = ('<div class="card"><div class="tags"><span class="tag new">New &middot; @@S@@</span>'
            '<span class="tag">Close</span></div>')
ws = once(ws, pypl_old, S(pypl_new), "pypl card tags")

ws = once(
    ws,
    'Shares fell as much as\n<span class="down">16% in premarket trading</span> Friday. '
    'No closing move was stated; none printed.',
    'Shares fell as much as <span class="down">16% in premarket trading</span> Friday, and '
    '<b>closed the session <span class="down">&minus;12.63%</span></b> &mdash; a figure this page '
    'had been unable to print until this run, reported elsewhere as having '
    '<b>&ldquo;fell 13%&rdquo;</b> (the same move at two precisions). &#9888; The two figures '
    'describe <b>different moments</b>, not different sessions: the premarket low and the closing '
    'bell. Roughly a third of the premarket decline was recovered by the close.',
    "pypl card body")

# (4) Marvell: -10% sharpened to -10.66%.
ws = once(ws, 'Marvell &minus;10%',
          'Marvell <b>&minus;10.66%</b> (sharpened this run from the &minus;10% this page carried)',
          "marvell pct")

# (5) New Elastic mover card, inserted before the Chart of the Day heading.
estc_card = (
    '<div class="card"><div class="tags"><span class="tag new">New &middot; @@S@@</span>'
    '<span class="tag">Earnings</span></div>\n'
    '<h4>Elastic &mdash; Friday&rsquo;s largest named gain</h4>\n'
    '<p>A Friday mover wrap fetched this run names <b>Elastic</b> as the session&rsquo;s biggest '
    'named advance, <span class="up">+20.34%</span>, after the company beat earnings estimates, '
    'raised guidance for <b>FY2027</b> and pointed to improving profitability. &#9888; A second '
    'account of the same session says the stock <b>&ldquo;surged 21%&rdquo;</b>. <b>20.34 does not '
    'round to 21</b>, so unlike the PayPal pair these two are <b>not</b> the same figure at two '
    'precisions &mdash; <b>both are recorded and neither is adopted</b>. The stock is <b>not</b> '
    'the Chart of the Day: no source seen this run stated its listing venue, and this page does '
    'not guess an exchange prefix to fill a widget.</p></div>\n'
)
ws = once(ws, '</div><h2 class="sec">Chart of the Day',
          S(estc_card) + '</div><h2 class="sec">Chart of the Day', "estc card")

# (6) Rates: record the WTI open alongside the carried close. An open is not a close.
m = re.search(r'\$83\.44', ws)
if m:
    ws = ws.replace(
        '$83.44',
        '$83.44 <span class="note-inline">(a separate snapshot puts the Friday <i>open</i> at '
        '<b>$83.54</b> &mdash; an open is not a close, and it is recorded rather than substituted)</span>',
        1)

# (7) Fed pricing: add Polymarket's third rendering.
ws = once(
    ws,
    'Polymarket puts a hold at 52% against 48% for a 25 basis-point hike',
    'Polymarket puts a hold at 52% against 48% for a 25 basis-point hike &mdash; and a read fetched at @@S@@ returns <b>Polymarket at 49% for a hike</b>, a <b>third</b> figure from the '
    'same venue, <b>recorded and not adopted</b>',
    "polymarket third read")

# (8) Footer sources.
ws_srcs = (
    '<a href="https://www.investing.com/news/stock-market-news/marvell-and-paypal-among-market-cap-stock-movers-on-friday-93CH-4881729">'
    'Investing.com &mdash; Marvell and PayPal among market-cap movers Friday (PYPL &minus;12.63%, MRVL &minus;10.66%, ESTC +20.34%)</a><br>'
    '<a href="https://seekingalpha.com/news/4637776-biggest-stock-movers-friday-pypl-mrvl-and-more">'
    'Seeking Alpha &mdash; Biggest stock movers Friday: PYPL, MRVL, GAP and more</a><br>'
    '<a href="https://www.cnbc.com/2026/08/28/stocks-making-the-biggest-moves-midday-amzn-mrvl-pypl-crm.html">'
    'CNBC &mdash; Biggest midday movers, Aug 28 (Amazon, Marvell, PayPal, Salesforce)</a><br>'
    '<a href="https://www.etftrends.com/fixed-income-content-hub/treasury-yields-snapshot-august-28-2026/">'
    'ETF Trends &mdash; Treasury yields snapshot, August 28 2026</a><br>'
    '<a href="https://polymarket.com/event/fed-decision-in-september-762">'
    'Polymarket &mdash; September Fed decision odds (49% hike, read this run)</a><br>'
)
ws = once(ws, '<footer><div class="srcs">', '<footer><div class="srcs">' + ws_srcs, "ws srcs")

wr("wallstreet-briefing.html", ws)


# ─────────────────────────────────────────────────────────────────────────────
# CYBER
# ─────────────────────────────────────────────────────────────────────────────
cy = rd("cyber-briefing.html")

cy_tldr = (
    '<b>New at @@S@@:</b> <b>the Oracle deadline this page dropped for three consecutive editions is '
    'back, and it is overdue.</b> `CVE-2026-21962` (Oracle HTTP Server / WebLogic Server proxy '
    'plug-in, improper access control) was stood down on Aug 27 because no source restated it; '
    '<b>CISA&rsquo;s own dated alert page for August 24 returned it this run</b>, and separate '
    'reporting states federal agencies were ordered to patch it <b>by August 27</b> &mdash; a date '
    'that has passed, so it goes back on the board <b>marked OVERDUE rather than quietly '
    'restored</b>. &#9888; <b>A due-date conflict is recorded and resolved toward the earlier '
    'date:</b> one aggregate read placed <b>CVE-2026-53362</b> (Linux kernel) at <b>September '
    '10</b>, while a dedicated report citing CISA gives <b>August 30 &mdash; today</b>, with '
    '<b>forensic triage</b> required under <b>BOD 26-04</b>. <b>The earlier date is published</b>, '
    'because treating a deadline as later than it may be is the costlier error. Newly sourced '
    'mechanism for that flaw: an <b>incorrect parameter length calculation in the IPv6 '
    'subsystem</b> lets anyone who can <b>create a UDP socket</b> overwrite kernel memory. The '
    '<b>seventeenth KEV check returns nothing later than August 27</b>, an <b>eleventh</b> '
    'consecutive time. Cl0p&rsquo;s PTC campaign gained three details and one sharp caveat: '
    '<b>Fiserv</b> joins the claimed-victim list, a <b>Ransom-ISAC notice dated July 22</b> warned '
    'of the exploitation before the naming, the group deployed <b>JSP web shells</b> to take '
    'backups, project plans and blueprints &mdash; and <b>none of the four named companies has '
    'confirmed data was taken, and Cl0p has published no samples</b>.'
)
cy = append_tldr(cy, S(cy_tldr), "cy tldr")

# Restore Oracle CVE-2026-21962 to the KEV section, marked overdue.
kev_anchor = '<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>'
oracle_li = (
    '<div class="note" style="margin-bottom:12px"><span class="tag new">New &middot; @@S@@</span> '
    '<b>Restored after three editions off the board, and overdue.</b> '
    '<b>CVE-2026-21962</b> &mdash; Oracle HTTP Server and Oracle WebLogic Server proxy plug-in, '
    '<b>improper access control</b>. <b>Added to KEV August 24</b> (CISA&rsquo;s own dated alert '
    'page, &ldquo;CISA Adds One Known Exploited Vulnerability to Catalog&rdquo;), with separate '
    'reporting stating federal agencies were ordered to remediate <b>by August 27</b>. '
    '<span class="crit">That date has passed &mdash; OVERDUE.</span> This page stood the CVE down '
    'on Aug 27 and Aug 28 because no source restated it, and said so on the page each time; '
    '<b>the absence was a sourcing gap, not a closed deadline</b>, and this run closes it the '
    'other way. &#9888; The deadline is reported by a secondary outlet rather than read off the '
    'KEV row itself, and is labelled as such.</div>\n'
)
oracle_li = S(oracle_li)
cy = once(cy, kev_anchor, kev_anchor + oracle_li, "oracle kev restore")

# Record the 53362 due-date conflict inside the KEV section.
cy = once(
    cy, oracle_li,
    oracle_li + S(
    '<div class="note" style="margin-bottom:12px"><span class="tag new">New &middot; @@S@@</span> '
    '<b>A due-date conflict on the Linux kernel entry, resolved toward the earlier date.</b> '
    'An aggregate KEV read this run placed <b>CVE-2026-53362</b> at <b>September 10</b> and '
    '<b>CVE-2023-49105</b> at <b>August 30</b>; a dedicated report citing CISA directly gives '
    '<b>CVE-2026-53362 added August 27, due August 30</b>, flagged for <b>forensic triage</b> '
    'under <b>BOD 26-04</b>. <b>Both readings are printed; August 30 is the one this page acts '
    'on</b>, on the same asymmetric-cost reasoning it applied to the Citrix fixed builds &mdash; '
    'if the earlier date is right, treating it as September 10 leaves an agency out of compliance '
    'for eleven days; if the later date is right, patching today costs nothing. Newly sourced '
    'mechanism: an <b>incorrect parameter length calculation in the kernel&rsquo;s IPv6 '
    'subsystem</b> allows an attacker able to <b>create UDP sockets</b> to trigger kernel-memory '
    'overwrites &mdash; privilege escalation, data corruption or a crash.</div>\n',
    ), "kev conflict note")

# Cl0p spotlight additions.
cl0p_add = (
    '<p><span class="tag new">New &middot; @@S@@</span> <b>Three additions and one caveat that cuts '
    'against the whole campaign.</b> <b>Fiserv</b> is named alongside Shell, General Electric and '
    'Philips in the claimed-victim list. The exploitation was flagged <b>before</b> the naming: '
    '<b>Ransom-ISAC issued a notice on July 22</b> warning that the group was exploiting PTC '
    'Windchill and FlexPLM, software used in engineering and manufacturing. Tradecraft is now '
    'specific &mdash; <b>JSP web shells</b> deployed to exfiltrate <b>backups, project plans and '
    'blueprints</b>. &#9888; And the caveat, which belongs at the top of any account of this '
    'campaign: <b>none of the four named companies has confirmed that data was taken, and Cl0p has '
    'published no samples.</b> Philips says it identified and contained an attempted compromise of '
    '<b>one enterprise server</b> holding internal data and that <b>customer environments are not '
    'affected</b>; Shell acknowledges only a <b>&ldquo;possible incident&rdquo;</b>. The victim '
    'count still returns as <b>43</b>, <b>&ldquo;more than 40&rdquo;</b> and <b>&ldquo;nearly '
    '50&rdquo;</b> and <b>none is adopted</b>.</p>\n'
)
sp = '<h2 class="sec">Breaches &amp; Incidents</h2>'
cl0p_add = S(cl0p_add)
cy = once(cy, sp, cl0p_add + sp, "cl0p additions")

# Leak-site listings + the industry letter, as claims with the caveat travelling with them.
cy = once(
    cy, cl0p_add,
    cl0p_add + S(
    '<p><span class="tag new">New &middot; @@S@@</span> <b>Fresh leak-site listings, printed as '
    'claims and nothing more.</b> A breach tracker records <b>three organisations listed on the '
    '<i>ZaWoo</i> ransomware leak site on August 30</b> &mdash; <b>esopartnerscpa</b>, '
    '<b>Afsard</b> and <b>hoerburger</b> &mdash; with the group claiming to have stolen internal '
    'data. &#9888; <b>These are the attacker&rsquo;s claims.</b> No victim count, data category, '
    'vendor statement, regulator filing or newsroom report accompanies any of the three, and '
    '<b>a leak-site listing is not confirmation of a breach</b>. They appear here only because '
    'that caveat travels with them. Separately and unrelated to those listings: <b>close to 130 '
    'technology and cybersecurity companies</b> have backed a collective call to strengthen cyber '
    'defences as AI-enabled attacks grow more capable. <b>Nevada&rsquo;s statewide ransomware '
    'incident was refused on sight for a ninth consecutive run</b> &mdash; it is an <b>August '
    '2025</b> event, and the &ldquo;2026 breaches&rdquo; listings that keep surfacing it are '
    'mis-shelving last year&rsquo;s incident.</p>\n',
    ), "leak-site listings")

# ServiceNow fourth-CVE identifier: a second read arrives; the refusal is narrowed, not lifted.
sn_note = (
    '<p><span class="tag new">New &middot; @@S@@</span> <b>The ServiceNow set returned again, and the '
    'fourth identifier is still not adopted &mdash; but the refusal is now narrower.</b> A source '
    'this run lists the August 27 advisory as covering <b>CVE-2026-6876</b>, CVE-2026-18885, '
    'CVE-2026-18886 and CVE-2026-74820, which is <b>unambiguous within that source</b>. The '
    'previous edition, however, saw <b>CVE-2026-6875</b> and <b>CVE-2026-6876</b> returned for the '
    'same flaw inside one result set. <b>One clean read does not settle a conflict recorded in '
    'another</b>, so the fourth CVE stays out of the table below and is described without an '
    'identifier; <b>CVE-2026-6876 is recorded here as the likelier form</b>. The three critical '
    'flaws are re-confirmed at <b>CVSS 10.0</b> and unauthenticated, and ServiceNow states it is '
    '<b>not aware of exploitation</b>.</p>\n'
)
vw = '<h2 class="sec">Vulnerability Watch</h2>'
cy = once(cy, vw, S(sn_note) + vw, "servicenow note")

cy_srcs = (
    '<a href="https://www.cisa.gov/news-events/alerts/2026/08/24/cisa-adds-one-known-exploited-vulnerability-catalog">'
    'CISA &mdash; Adds One Known Exploited Vulnerability to Catalog (Aug 24: CVE-2026-21962, Oracle)</a><br>'
    '<a href="https://cybersecuritynews.com/linux-kernel-privilege-escalation-vulnerability-exploited/">'
    'Cybersecurity News &mdash; CVE-2026-53362 Linux kernel IPv6 priv-esc, KEV Aug 27, due Aug 30, BOD 26-04 forensic triage</a><br>'
    '<a href="https://www.techtimes.com/articles/324578/20260815/clop-hacks-shell-ge-philips-43-victim-ptc-windchill-zero-day-campaign.htm">'
    'TechTimes &mdash; Cl0p PTC Windchill campaign, 43 claimed victims</a><br>'
    '<a href="https://www.claimsjournal.com/news/national/2026/08/14/339563.htm">'
    'Claims Journal &mdash; Cl0p claims data theft from Shell, Philips, GE and Fiserv (unverified; no samples published)</a><br>'
    '<a href="https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html">'
    'The Hacker News &mdash; Three CVSS 10.0 ServiceNow flaws</a><br>'
)
cy = once(cy, '<footer><div class="srcs">', '<footer><div class="srcs">' + cy_srcs, "cy srcs")

wr("cyber-briefing.html", cy)


# ─────────────────────────────────────────────────────────────────────────────
# MMA
# ─────────────────────────────────────────────────────────────────────────────
mma = rd("mma-briefing.html")

mma_tldr = (
    '<b>New at @@S@@:</b> <b>a stale champions list surfaced in this run&rsquo;s own search results '
    'and was refused on sight &mdash; it is the exact regression this page has guarded against for '
    'sixty-seven editions.</b> A blended result returned <b>Chimaev</b> at middleweight, '
    '<b>Topuria</b> at featherweight, <b>Dvalishvili</b> at bantamweight, <b>Pantoja</b> at '
    'flyweight and <b>Zhang Weili</b> at women&rsquo;s strawweight &mdash; <b>five belts wrong in '
    'one paragraph</b>, every one of them a champion who has since been beaten. A second, dated '
    'search re-confirmed the correct holders independently: <b>Strickland</b> took the middleweight '
    'title from Chimaev at UFC 328, <b>Volkanovski</b> is a two-time featherweight champion after '
    'beating Diego Lopes again at UFC 325, and <b>Yan</b> took the bantamweight belt back from '
    'Dvalishvili at UFC 323. <b>The board is unchanged for a sixty-seventh consecutive edition.</b> '
    '&#9888; Also recorded: a <b>third rendering of the UFC 331 start times</b> &mdash; early '
    'prelims about <b>5 PM ET</b>, prelims <b>7 PM ET</b>, main card <b>9 PM ET</b>, against the '
    '<b>prelims 6 PM / main card 9 PM</b> this page carries. <b>The 9 PM main card is the one '
    'point all readings agree on</b>; the prelim windows are not resolved and are not presented as '
    'though they were. Three more UFC 331 bouts are sourced: <b>Moicano vs. Ortega 2</b>, '
    '<b>Patricio Pitbull vs. Doo Ho Choi</b> and <b>Jourdain vs. Vera</b>.'
)
mma = append_tldr(mma, S(mma_tldr), "mma tldr")

# UFC 331 start-time third rendering + newly sourced bouts.
u331 = (
    '<p><span class="tag new">New &middot; @@S@@</span> <b>UFC 331 &mdash; a third start-time '
    'rendering, and three more bouts.</b> A listing fetched this run puts <b>early prelims at '
    'about 5 PM ET, prelims at 7 PM ET and the main card at 9 PM ET</b>. This page carries '
    '<b>prelims 6 PM ET / main card 9 PM ET</b>. &#9888; <b>The main card time is the same in '
    'every reading and is the only one stated as settled</b>; the undercard windows differ and '
    '<b>neither is adopted</b> &mdash; a three-tier card (early prelims, prelims, main) and a '
    'two-tier one may simply be two ways of describing the same schedule, which is a reason to '
    'record both rather than pick. Newly sourced additions to the card: <b>Renato Moicano vs. '
    'Brian Ortega 2</b>, <b>Patricio Pitbull vs. Doo Ho Choi</b> and <b>Charles Jourdain vs. '
    'Marlon Vera</b>, under the <b>Van vs. Pantoja 2</b> flyweight title headliner and the '
    '<b>Tsarukyan vs. Ruffy</b> co-main.</p>\n'
)
pw = '<h2 class="sec">Prospect Watch</h2>'
mma = once(mma, pw, S(u331) + pw, "ufc331 note")

# Champions board: the refusal, recorded above the table.
champ_note = (
    '<div class="note" style="margin-bottom:12px"><span class="tag new">New &middot; @@S@@</span> '
    '<b>This run&rsquo;s search results contained a five-belt regression, and it was refused.</b> '
    'A blended current-champions summary returned <b>Khamzat Chimaev</b> (middleweight), '
    '<b>Ilia Topuria</b> (featherweight), <b>Merab Dvalishvili</b> (bantamweight), '
    '<b>Alexandre Pantoja</b> (flyweight) and <b>Zhang Weili</b> (women&rsquo;s strawweight) as '
    'reigning champions. <b>All five lost those belts</b> &mdash; to Strickland, Volkanovski, Yan, '
    'Van and Dern respectively. The blend is what this page&rsquo;s standing rule describes '
    'exactly: <b>a heavily-covered older reign outranking the newer result that ended it</b>. '
    'Correct holders re-confirmed independently this run for middleweight, featherweight and '
    'bantamweight; the remaining belts are carried from the verified board. '
    '<b>Sixty-seventh consecutive unchanged edition.</b></div>\n'
)
cb = '<h2 class="sec">Champions Board</h2>'
mma = once(mma, cb, cb + S(champ_note), "champions refusal note")

mma_srcs = (
    '<a href="https://www.cbssports.com/ufc/news/ufc-pound-for-pound-fighter-rankings-sean-strickland-khamzat-chimaev/">'
    'CBS Sports &mdash; Strickland&rsquo;s upset of Chimaev at UFC 328 (middleweight title)</a><br>'
    '<a href="https://www.aljazeera.com/sports/2026/8/6/ufc-331-van-pantoja-rematch-tsarukyan-returns-and-full-fight-card">'
    'Al Jazeera &mdash; UFC 331 full card (Moicano&ndash;Ortega 2, Pitbull&ndash;Choi, Jourdain&ndash;Vera)</a><br>'
    '<a href="https://www.ufc.com/event/ufc-fight-night-september-05-2026">'
    'UFC.com &mdash; UFC Paris, Hooker vs Parnasse, September 5</a><br>'
    '<a href="https://sports.yahoo.com/articles/ufc-shanghai-video-denise-gomes-123030574.html">'
    'Yahoo Sports &mdash; Denise Gomes KOs Yan Xiaonan, UFC Shanghai co-main</a><br>'
)
mma = once(mma, '<footer><div class="srcs">', '<footer><div class="srcs">' + mma_srcs, "mma srcs")

wr("mma-briefing.html", mma)

print("edits_1710: all edits applied")
