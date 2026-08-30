# -*- coding: utf-8 -*-
import io, sys

STAMP = "6:35 PM"
FILES = ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]
def rd(f): return io.open(f,encoding="utf-8").read()
def wr(f,s): io.open(f,"w",encoding="utf-8").write(s)

def rep(s, old, new, n=1, label=""):
    c = s.count(old)
    assert c == n, "EXPECTED %d got %d for %s :: %s" % (n, c, label, old[:70])
    return s.replace(old, new)

# ---------- 1. STAMPS on all four pages ----------
for f in FILES:
    s = rd(f)
    s = rep(s, 'id="edition">Midday Edition', 'id="edition">Afternoon Edition', 1, f+" edition")
    s = rep(s, 'id="updated">5:15 PM ET', 'id="updated">%s ET' % STAMP, 1, f+" updated")
    s = rep(s, 'id="freshline">Data as of 5:15 PM ET',
               'id="freshline">Data as of %s ET' % STAMP, 1, f+" freshline")
    wr(f, s)

# ---------- 2. CYBER: new collective-defense letter card ----------
NEWCARD = (
'<div class="card"><div class="tags"><span class="tag new">New &middot; 6:35 PM</span>'
'<span class="tag warn">Signatory count disputed</span><span class="tag">Industry</span></div>\n'
'<h4>Most of the security industry signed one letter about AI-enabled attacks &mdash; and the reports cannot agree on how many signed it</h4>\n'
'<p><b>What was published.</b> On <b>August 27, 2026</b>, OpenAI published an open letter titled '
'<b>&ldquo;A call for collective action on cyber defense&rdquo;</b> and organised the industry behind it. '
'The letter sets out <b>three principles</b>: that current security practices <b>will not be enough</b>; that '
'more defenders should be <b>empowered with cyber-capable AI</b>; and that the response must be '
'<b>collective</b>. It also calls for a <b>coordinated government effort to fund cyber defense</b> and to make '
'it reachable for <b>under-resourced critical infrastructure</b> &mdash; naming <b>hospitals</b> and '
'<b>water treatment plants</b>, alongside internet infrastructure, as what is at risk. The stated warning is '
'about timing: that AI-enabled attacks become <b>significantly more capable in the coming months</b>.</p>\n'
'<p>&#9888; <b>The number is not settled, and this page will not pick one.</b> Four reports fetched this run '
'give four different counts of who signed. <b>CNBC</b> says <b>116 companies and entities</b>. A second report '
'puts <b>128 organisations</b> behind it. A third headline says <b>&ldquo;over 100 companies.&rdquo;</b> A '
'fourth renders it as <b>&ldquo;130 other companies&rdquo;</b> alongside four named firms. <b>The honest range '
'is 116 to roughly 130</b>, and the spread is printed rather than averaged, because the difference between '
'&ldquo;companies&rdquo; and &ldquo;organisations and entities&rdquo; is very likely what is being counted '
'differently &mdash; no source fetched this run defines its own unit. <b>The signatory names, unlike the '
'count, agree across reports:</b> <b>Anthropic</b>, <b>Google</b>, <b>Microsoft</b>, <b>AWS</b>, <b>IBM</b>, '
'<b>Oracle</b>, <b>Cisco</b>, <b>Check Point</b>, <b>Cloudflare</b> and <b>CrowdStrike</b>, with <b>OpenAI</b> '
'leading the effort.</p>\n'
'<p><b>Why it sits next to the rest of this page rather than above it.</b> A letter is not an incident. It is '
'here because the thing it describes is already on this page in concrete form &mdash; the '
'<b>OpenAI sandbox-escape post-mortem</b> below, and <b>CVE-2026-53362</b> in the table above, KEV-listed on '
'<b>August 27</b>, the same day the letter published, and exploited by AI agents that found a public exploit '
'and adapted it. <b>The letter is the industry saying in general what those two items show in particular.</b></p>'
'</div>\n'
)
s = rd("cyber-briefing.html")
ANCH = '<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">\n'
s = rep(s, ANCH, ANCH + NEWCARD, 1, "cyber breaches anchor")

# KEV note: fifth check
KOLD = ('Re-checked again at 1:35 PM, and nothing moved.')
KNEW = ('A fifth check at 6:20 PM returned CISA&rsquo;s own August 27 alert page for the first time.</b> '
 'Until this edition the <b>August 27 batch</b> &mdash; the 1-day and 12-day rows above &mdash; had been carried '
 'from reporting <i>about</i> the catalogue rather than from CISA. The search run this hour returned '
 '<b>CISA&rsquo;s alert page titled &ldquo;CISA Adds Three Known Exploited Vulnerabilities to Catalog,&rdquo; '
 'dated August 27, 2026</b>, and <b>three</b> is exactly the number of August 27 ids this board carries '
 '(<b>CVE-2026-53362</b>, <b>CVE-2023-49105</b>, <b>CVE-2026-66384</b>). <b>That row is now anchored on the '
 'issuing authority rather than on secondary reporting.</b> The same search also surfaced a <b>CISA alert dated '
 'August 24 adding one vulnerability</b>, which none of the four earlier checks had returned &mdash; it '
 '<b>predates</b> the August 26 batch, so it changes no countdown above, and it is recorded here as evidence '
 'that <b>these searches do not see the whole catalogue</b>, which is the caveat this section has carried all '
 'day and now has a concrete instance of. <b>No alert dated later than August 27 was returned.</b> Countdowns '
 'stay at <b>0 / 1 / 11 / 12</b>. '
 '<b>Re-checked earlier at 1:35 PM, and nothing moved then either.</b>')
assert s.count(KOLD) == 1, "KEV anchor count %d" % s.count(KOLD)
s = s.replace(KOLD, '<b>' + KNEW)

# cyber tldr + index card share this opener
CY_OLD = 'ServiceNow has patched <b>three separate CVSS 10.0 flaws</b>'
CY_NEW = ('Most of the technology and security industry has put its name to a single document &mdash; OpenAI '
 'published an open letter, <b>&ldquo;A call for collective action on cyber defense,&rdquo;</b> on '
 '<b>August 27</b>, signed by <b>Anthropic, Google, Microsoft, AWS, IBM, Oracle, Cisco, Check Point, Cloudflare '
 'and CrowdStrike</b> among others, warning that AI-enabled attacks get materially more capable within months '
 'and that hospitals, water treatment plants and internet infrastructure are the under-resourced edge, though '
 'the reports fetched this run put the signatory count anywhere from <b>116 to roughly 130</b> and this page '
 'prints the range rather than choose; a fifth check of the federal deadline board also returned '
 '<b>CISA&rsquo;s own August 27 alert page</b> for the first time, anchoring the three August 27 ids on the '
 'issuing authority, while surfacing an <b>August 24 alert none of the four earlier checks had seen</b> &mdash; '
 'it predates the August 26 batch and moves no countdown, but it is the concrete instance of the caveat this '
 'page has carried all day, that these searches do not see the whole catalogue; separately '
 'ServiceNow has patched <b>three separate CVSS 10.0 flaws</b>')
s = rep(s, CY_OLD, CY_NEW, 1, "cyber tldr")
wr("cyber-briefing.html", s)

s = rd("index.html")
s = rep(s, CY_OLD, CY_NEW, 1, "index cyber card")

# ---------- 3. MARKETS: fourteenth verification ----------
WS_OLD = ('re-verified a thirteenth time this run by a search that returned all three index levels, all three '
 'percentage moves and the three weekly figures together &mdash; the third consecutive check of that breadth')
WS_NEW = ('re-verified a <b>fourteenth</b> time this run by a search that again returned all three index levels, '
 'all three percentage moves and the three weekly figures together &mdash; the <b>fourth consecutive</b> check '
 'of that breadth, and on a tape that has been shut since Friday afternoon <b>nothing else on this page moved '
 'either</b>')
s = rep(s, WS_OLD, WS_NEW, 1, "index markets card")
wr("index.html", s)

w = rd("wallstreet-briefing.html")
w = rep(w, WS_OLD, WS_NEW, 1, "ws tldr")
LEAD_OLD = ('its official closes stand unchanged, re-verified an eleventh time at 12:35 PM')
LEAD_NEW = ('its official closes stand unchanged, re-verified a <b>fourteenth</b> time at <b>6:20 PM</b> and an '
 'eleventh time at 12:35 PM')
w = rep(w, LEAD_OLD, LEAD_NEW, 1, "ws lead")
wr("wallstreet-briefing.html", w)

# ---------- 4. MMA: Song quote, path, and two conflicts resolved ----------
m = rd("mma-briefing.html")
MM_OLD = ('though the $400,000 figure still stands as the total of the four and no source states a combined '
 'total for the card.</span></div>')
MM_NEW = ('though the $400,000 figure still stands as the total of the four and no source states a combined '
 'total for the card; and at <b>6:35 PM</b> Song&rsquo;s own words arrived &mdash; &ldquo;I think the UFC '
 'should give me the title shot. I feel like I can finish everyone. I can finish Petr, I can finish '
 'Merab&rdquo; &mdash; alongside sourced framing that with the belt booked for October his realistic next step '
 'is a <b>backup role or a fight with the Yan&ndash;Dvalishvili winner</b>, and two figures in the results '
 'table above were challenged by an aggregated listing this hour and <b>both survived</b>: the Bilal Hasan '
 'knockout is <b>round two at 2:28</b>, not round one, and Rei Tsuruya&rsquo;s choke is at <b>4:14</b>, not '
 '4:03.</span></div>')
m = rep(m, MM_OLD, MM_NEW, 1, "mma tldr")
wr("mma-briefing.html", m)

s = rd("index.html")
s = rep(s, MM_OLD.replace('</span></div>','</p>'), MM_NEW.replace('</span></div>','</p>'), 1, "index mma card")
wr("index.html", s)

print("EDITS OK")
