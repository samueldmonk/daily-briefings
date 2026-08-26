#!/usr/bin/env python3
# Incremental edits for the 12:58 Midday Edition, Wed Aug 26 2026.
import io, sys, re, os

D = sys.argv[1] if len(sys.argv) > 1 else "."
TAG = "12:58"

def rd(p):
    with io.open(os.path.join(D, p), encoding="utf-8") as f: return f.read()
def wr(p, s):
    with io.open(os.path.join(D, p), "w", encoding="utf-8") as f: f.write(s)

fails = []
def sub(s, old, new, label, count=1):
    if old not in s:
        fails.append("MISSING ANCHOR: " + label); return s
    return s.replace(old, new, count)

# ============================ WALL STREET ============================
ws = rd("wallstreet-briefing.html")

# --- demote previous edition's New tags ---
ws = ws.replace('New &middot; 12:50', 'Carried &middot; 12:50 edition')

# --- TLDR ---
old_tldr_start = ws.index('<div class="tldr"><b>The Tape</b>')
old_tldr_end = ws.index('</div>', ws.index('</span>', old_tldr_start))
new_tldr = ('<div class="tldr"><b>The Tape</b> <span>All three headline indices are now red on a '
  'single fully reconciled board: <b>S&amp;P&nbsp;500 7,667.22 (&minus;10.06, &minus;0.13%)</b>, '
  '<b>Dow 53,433.49 (&minus;143.91, &minus;0.27%)</b> and <b>Nasdaq Composite 26,055.25 '
  '(&minus;96.05, &minus;0.37%)</b>, each subtracting exactly to Tuesday&rsquo;s close &mdash; '
  'a clean reversal of the <b>11:47&nbsp;a.m. ET</b> read that still had the S&amp;P up 0.01% at '
  '7,678 &mdash; while <b>Abercrombie &amp; Fitch</b> is now rendered as high as <b>&plus;40%</b>, '
  '<b>Alibaba</b> is clawing back a plunge on a <b>$10&nbsp;billion share placement</b>, oil has a '
  'Wednesday print at <b>$80.78</b>, and the whole tape waits on <b>Nvidia after the close</b>.'
  '</span>')
ws = ws[:old_tldr_start] + new_tldr + ws[old_tldr_end:]

# --- ticker tape: INTU -> BABA (five mandatory symbols retained) ---
ws = sub(ws, '{"proName":"NASDAQ:INTU","title":"Intuit"}',
             '{"proName":"NYSE:BABA","title":"Alibaba"}', "tape INTU->BABA")

# --- Lead: new headline + new lead paragraph ---
ws = sub(ws,
  '<h2>The S&amp;P&nbsp;500 gives it all back and turns red, as of <i>~12:42&nbsp;p.m. ET</i></h2>',
  '<h2>Red across all three, and for once every number on the board reconciles</h2>',
  "ws lead h2")

new_lead = ('<p><b>&#9679; New at ' + TAG + ' &mdash; the first fully reconciled three-index intraday board '
 'of the afternoon, and every index is negative.</b> A live quote board carried on The Motley Fool&rsquo;s '
 'midday report and fetched in full this run reads <b>S&amp;P&nbsp;500 7,667.22, &minus;10.06, &minus;0.13%</b>; '
 '<b>Dow Jones Industrial Average 53,433.49, &minus;143.91, &minus;0.27%</b>; <b>Nasdaq Composite 26,055.25, '
 '&minus;96.05, &minus;0.37%</b>. All three pass this page&rsquo;s three-way test simultaneously, which no '
 'board has done since the 9:59 snapshot: <b>7,667.22 &plus; 10.06 = 7,677.28</b>, <b>53,433.49 &plus; 143.91 '
 '= 53,577.40</b> and <b>26,055.25 &plus; 96.05 = 26,151.30</b> &mdash; the three Tuesday closes published in '
 'the Weekly Scorecard below, to the cent &mdash; and each percentage matches its own points-over-prior-close '
 'arithmetic (0.131%, 0.269%, 0.367%). <b>&#9888; The board is a streaming widget and carries no clock stamp '
 'of its own</b>; it was fetched at approximately <b>12:55&nbsp;p.m. ET</b> and is published as a read at the '
 'moment of fetch, not as a stamped quotation. <b>&#9888; The same page rendered the same three quotes twice '
 'more, moments apart</b> &mdash; <b>S&amp;P 7,668.63 (&minus;8.65, &minus;0.11%)</b> and <b>7,668.89 '
 '(&minus;8.39, &minus;0.1%)</b>, <b>Dow 53,433.99 (&minus;143.41, &minus;0.3%)</b>, <b>Nasdaq 26,055.65 '
 '(&minus;95.65, &minus;0.4%)</b>. Every one of those reconciles to the same three prior closes as well. They '
 'are printed as successive ticks of a live feed, not averaged and not merged.</p>\n'
 '<p><b>&#9679; New at ' + TAG + ' &mdash; and here is where the session was an hour earlier.</b> The same '
 'Motley Fool report, bylined <b>Emma Newbery</b> and published <b>12:27&nbsp;p.m. ET</b>, states in its own '
 'text: <b>&ldquo;As of 11:47 AM ET, the S&amp;P 500 is up 0.01% to 7,678, while the Nasdaq Composite has '
 'fallen 0.12% to 26,117, and the Dow Jones Industrial Average is trading 0.18% lower at 53,480.&rdquo;</b> '
 'Two of those three reconcile cleanly: <b>7,678 against a 7,677.28 close is &plus;0.72 points, or '
 '&plus;0.009%</b>, which rounds to the stated 0.01%; and <b>53,577.40 less 0.18% is 53,481.0</b>, which is '
 'the stated 53,480 to the rounding. <b>&#9888; The Nasdaq pair does not: a level of 26,117 against a '
 '26,151.30 close implies &minus;0.131%, not the stated 0.12%.</b> Both figures are printed exactly as the '
 'outlet gives them and neither is corrected here. Set against the board above, the <b>S&amp;P has gone from '
 'fractionally green at 11:47 to roughly ten points red by 12:55</b>, and the Dow and Nasdaq have each '
 'roughly doubled their losses over the same hour.</p>\n')

ws = sub(ws, '<p><b>&#9679; Carried &middot; 12:50 edition at 12:50 &mdash;',
             new_lead + '<p><b>&#9679; Carried from the 12:50 edition &mdash;', "ws lead insert (variant A)")
if "ws lead insert (variant A)" in " ".join(fails):
    fails.remove("MISSING ANCHOR: ws lead insert (variant A)")
    ws = sub(ws, '<p><b>&#9679; New at 12:50 &mdash;',
                 new_lead + '<p><b>&#9679; Carried from the 12:50 edition &mdash;', "ws lead insert (variant B)")

# --- Movers: new Alibaba card + ANF 40% rendering ---
movers_anchor = '<div class="lab">Movers &amp; drivers</div>\n<div class="cards">'
if movers_anchor not in ws:
    m = re.search(r'<div class="lab">Movers &amp; drivers</div>\s*<div class="cards">', ws)
    movers_anchor = m.group(0) if m else None

if movers_anchor:
    baba_card = (movers_anchor + '\n'
      '<div class="card"><div class="tags"><span class="tag new">New &middot; ' + TAG + '</span>'
      '<span class="tag">$10bn placement</span><span class="tag">AI capex</span></div>'
      '<h3>Alibaba plunges on a $10&nbsp;billion share placement &mdash; then claws part of it back</h3>'
      '<p>The Motley Fool&rsquo;s midday report, fetched in full this run, has <b>Alibaba Group Holding</b> '
      'having <b>&ldquo;erased some losses after plunging on news of a $10 billion share placement to fund '
      'artificial intelligence (AI) development.&rdquo;</b> A placement of that size is dilution taken '
      'deliberately to fund capital expenditure, which is why the tape reads it in two directions inside one '
      'session.</p>'
      '<p class="note"><b>&#9888; No percentage move, no level and no clock time is stated for Alibaba in any '
      'source fetched this run</b> &mdash; direction and the $10&nbsp;billion figure are all that is published, '
      'and the $10&nbsp;billion is the placement size as the outlet states it, not a market-value change.</p>'
      '</div>\n'
      '<div class="card"><div class="tags"><span class="tag new">New &middot; ' + TAG + '</span>'
      '<span class="tag">Sixth rendering</span><span class="tag">&plus;40%</span></div>'
      '<h3>Abercrombie gets a sixth number, and it is the biggest one yet</h3>'
      '<p>The Motley Fool has <b>Abercrombie &amp; Fitch</b> having <b>&ldquo;soared an eye-watering 40% after '
      'beating earnings estimates and raising its full-year guidance.&rdquo;</b> That is now the <b>sixth '
      'distinct rendering</b> of the same reaction this page has carried today, after 8.3%, 11.9%, &ldquo;over '
      '11%&rdquo; premarket, 17% and the reconciled Yahoo board figure of <b>&plus;30.85% at $142.50</b>.</p>'
      '<p class="note"><b>&#9888; The 40% is a narrative figure with no level and no clock time attached, so it '
      'does not displace the board reading in the Chart of the Day note below</b> &mdash; the +30.85% remains '
      'the only ANF number that reconciles against a stated prior close. All six are printed, none is merged '
      'into another, and nothing is averaged.</p></div>\n'
      '<div class="card"><div class="tags"><span class="tag new">New &middot; ' + TAG + '</span>'
      '<span class="tag">Whipsaw</span><span class="tag">Settlement</span></div>'
      '<h3>Meta whipsawed on its own settlement &mdash; and the quote board disagrees with the wire</h3>'
      '<p>The Motley Fool describes <b>Meta Platforms</b> as having <b>&ldquo;whipsawed this morning following '
      'a $17 billion legal settlement,&rdquo;</b> with the stock <b>initially popping before paring gains as '
      'markets digested the news.</b> The same page&rsquo;s live quote strip, read at the moment of fetch, puts '
      '<b>META at $577.35, &plus;1.3%, &plus;$7.30</b>.</p>'
      '<p class="note"><b>&#9888; Three figures for one stock, all printed unmerged.</b> The settlement is '
      'rendered as <b>$17&nbsp;billion</b> here and as <b>$16.7&nbsp;billion</b> in the CNBC account carried in '
      'The Lead; and the <b>&plus;$577.35 / &plus;1.3%</b> quote sits directly against the earlier TipRanks '
      'read of <b>Meta &minus;1.1% to $563.84</b>. Neither pair is adjudicated on this page.</p></div>')
    ws = sub(ws, movers_anchor, baba_card, "ws movers cards")

# --- Sector heat editorial line ---
ws = sub(ws,
  '<div class="note">Tuesday&rsquo;s sector leadership, for reference until Wednesday&rsquo;s own board fills in:',
  '<div class="note"><b>&#9679; New at ' + TAG + ' &mdash; Wednesday finally has its own sector line.</b> The '
  'Motley Fool&rsquo;s midday report, fetched in full this run, states that <b>energy and industrial stocks '
  'lead the sector gainers, and basic materials and healthcare trail.</b> <b>&#9888; That is a leadership '
  'ranking only &mdash; no sector percentage, no count of advancing sectors and no clock time is stated, so '
  'none is printed.</b> It is the first Wednesday sector read this page has been able to publish, and it does '
  'not agree with Tuesday&rsquo;s board below, where health care led. Both are printed at their own dates. '
  '&mdash; Tuesday&rsquo;s sector leadership, for reference:',
  "ws sector line")

wr("wallstreet-briefing.html", ws)

# ============================ CYBER ============================
cy = rd("cyber-briefing.html")
cy = cy.replace('New &middot; 12:50', 'Carried &middot; 12:50 edition')

# TLDR
s0 = cy.index('<div class="tldr"><b>The Wire</b>')
s1 = cy.index('</span>', s0) + len('</span>')
new_cy_tldr = ('<div class="tldr"><b>The Wire</b> <span>The KEV-listed Gitea remote code execution flaw '
 '<b>CVE-2026-60004</b> now has a severity attached &mdash; <b>CVSS&nbsp;9.8</b> &mdash; and its federal '
 'remediation deadline of <b>Friday, August&nbsp;28</b> is independently confirmed by three outlets this run, '
 'putting it two days out and directly behind the <b>CVSS&nbsp;10.0</b> Oracle flaw due <b>tomorrow</b>; '
 'meanwhile CERT/CC has published <b>two unpatched, unauthenticated flaws in Kaltura&rsquo;s mwEmbed video '
 'player</b> that it could not get the vendor to answer for, the <b>Los Angeles County Museum of Art</b> has '
 'disclosed a 2025 intrusion that reached Social Security numbers and medical records, and the federal board '
 'still holds <b>14 tracked KEV deadlines with 10 already past due</b>.</span>')
cy = cy[:s0] + new_cy_tldr + cy[s1:]

# Stat strip: swap the Iran designations stat for the AnonyMousKIT scale
cy = sub(cy,
  '<div class="stat"><div class="n">~60</div><div class="l">Iran-linked entities, individuals and vessels newly designated by the U.S. Treasury</div></div>',
  '<div class="stat"><div class="n">506</div><div class="l">Domains SOCRadar links to the <b>AnonyMousKIT</b> Apple-phishing service, feeding <b>168</b> reseller storefronts</div></div>',
  "cy stat swap")

# Patch priority: Gitea now has a CVSS
cy = sub(cy,
  '<p><b>New on the board this run &mdash; Gitea CVE-2026-60004, due Friday.</b>',
  '<p><b>&#9679; New at ' + TAG + ' &mdash; the Gitea flaw finally has a severity, and the deadline is now '
  'triple-sourced.</b> <b>CVE-2026-60004 is rated CVSS&nbsp;9.8</b>, per reporting read this run from '
  '<b>SecurityWeek</b>, <b>Help Net Security</b> and <b>BleepingComputer</b>; the same accounts put the '
  'mechanism plainly &mdash; <b>&ldquo;an attacker with ordinary repository write access&rdquo;</b> can '
  '<b>&ldquo;plant an executable Git hook and run arbitrary shell commands with the privileges of the Gitea '
  'service account.&rdquo;</b> All three independently state the <b>federal remediation deadline of '
  'August&nbsp;28, 2026</b>, and all three place the <b>KEV addition on August&nbsp;25</b>. The standing note '
  'that no CVSS had been stated for this CVE is <b>retired</b>, and the score is now carried in the '
  'Vulnerability Watch table and on the KEV board below. <b>&#9888; The score is a reported figure from '
  'security press, not read off a Gitea advisory or an NVD page by this desk</b> &mdash; it is published on '
  'that attribution, and on the agreement of three independent outlets, rather than as a vendor number.</p>\n'
  '<p><b>&#9679; New at ' + TAG + ' &mdash; and one thing you cannot patch at all today.</b> <b>CERT/CC has '
  'published VU#308749</b>, covering <b>CVE-2026-19913</b> and <b>CVE-2026-19912</b> in <b>Kaltura&rsquo;s '
  'mwEmbed HTML5 video player library</b> (also distributed as <b>html5lib</b>). Both stem from the same '
  '<b>unsafe deserialization in the mwEmbedLoader.php endpoint</b>, and <b>neither requires authentication or '
  'a Kaltura session token</b> &mdash; network access to the endpoint is the only precondition CERT/CC states. '
  '<b>There is no patch.</b> CERT/CC says it was <b>&ldquo;unable to reach Kaltura to coordinate these '
  'vulnerabilities.&rdquo;</b> The interim guidance is to <b>restrict or disable external access to the '
  'endpoint</b> and to <b>enforce a strict allow-list for the ServiceUrl parameter</b> permitting only '
  'legitimate backend API URLs. <b>&#9888; No CVSS score is stated for either CVE in any source fetched this '
  'run, and neither is in KEV, so neither carries a federal deadline</b> &mdash; they sit above the Oracle and '
  'Gitea clocks in urgency only in the sense that no vendor fix exists to apply.</p>\n'
  '<p><b>Carried &middot; 8:46 edition &mdash; Gitea CVE-2026-60004, due Friday.</b>',
  "cy patch priority gitea+kaltura")

# Vulnerability watch: give Gitea its 9.8 and add the two Kaltura rows
cy = sub(cy,
  '<tr><td>CVE-2026-60004</td><td>&mdash;</td><td>Gitea before 1.27.1',
  '<tr><td>CVE-2026-19913</td><td>&mdash;</td><td>Kaltura mwEmbed / html5lib HTML5 player (<b>no patch available</b>)</td>'
  '<td>Unsafe deserialization in <i>mwEmbedLoader.php</i> &rarr; <b>arbitrary file read</b>: a <i>file://</i> path '
  'supplied to <b>ServiceUrl</b> is reflected back in the deserialization error, exposing database credentials, '
  'administrative secrets and API keys. Unauthenticated; no Kaltura session token needed. CERT/CC <b>VU#308749</b> '
  '&mdash; vendor unreachable. Not in KEV. No CVSS stated in any source fetched this run.</td></tr>\n'
  '<tr><td>CVE-2026-19912</td><td>&mdash;</td><td>Kaltura mwEmbed / html5lib HTML5 player (<b>no patch available</b>)</td>'
  '<td>Same unsafe deserialization &rarr; <b>remote code execution</b>, enabling modification or exfiltration of '
  'platform data and deployment of tooling for persistence and lateral movement. Unauthenticated. Mitigation is '
  'network restriction plus a strict <b>ServiceUrl</b> allow-list. Not in KEV. No CVSS stated in any source fetched '
  'this run.</td></tr>\n'
  '<tr><td>CVE-2026-60004</td><td>9.8</td><td>Gitea before 1.27.1',
  "cy vw gitea 9.8 + kaltura rows")

cy = sub(cy,
  'Advisory shipped with a PoC. Patched in 1.27.1 in late July. No CVSS score was stated in any source fetched this run, so none is published.',
  'Advisory shipped with a PoC. Patched in <b>1.27.1</b> in late July. <b>CVSS&nbsp;9.8 as reported by SecurityWeek, '
  'Help Net Security and BleepingComputer this run</b> &mdash; a press figure agreed by three outlets, not a vendor '
  'or NVD page read by this desk.',
  "cy vw gitea note")

# KEV board line for Gitea
cy = sub(cy,
  '<b>CVE-2026-60004</b> &mdash; Gitea, code injection via the <i>diffpatch</i> endpoint &rarr; RCE ',
  '<b>CVE-2026-60004</b> &mdash; Gitea, code injection via the <i>diffpatch</i> endpoint &rarr; RCE ',
  "cy kev gitea (noop check)")
cy = cy.replace('as the Gitea OS user (no CVSS published).',
                'as the Gitea OS user (CVSS&nbsp;9.8, as reported).')

# Breaches & incidents: two new cards
cy = sub(cy, '<div class="lab">Breaches &amp; incidents</div>',
 '<div class="lab">Breaches &amp; incidents</div>\n'
 '<div class="cards">\n'
 '<div class="card"><div class="tags"><span class="tag new">New &middot; ' + TAG + '</span>'
 '<span class="tag">Breach</span><span class="tag crit">Medical data</span></div>'
 '<h3>LACMA took thirteen months to work out what a 2025 intrusion had reached &mdash; and it reached medical records</h3>'
 '<p>The <b>Los Angeles County Museum of Art</b>, one of the largest art museums in the western United States, '
 'has disclosed a breach of customer and employee data. The timeline is the part worth reading twice: LACMA '
 '<b>detected suspicious activity on its systems on July&nbsp;11, 2025</b>, confirmed a network compromise '
 '<b>roughly a month later</b>, did not identify the <b>full extent of the exposed data until late '
 'February&nbsp;2026</b>, and <b>reported the breach on August&nbsp;24, 2026</b> &mdash; more than thirteen '
 'months after detection.</p>'
 '<p>The exposed categories run well past a mailing list: <b>full names, dates of birth, Social Security '
 'numbers, driver&rsquo;s licence or government-issued identification numbers, partial financial account '
 'numbers, partial payment-card information, health insurance information</b>, and <b>medical details '
 'including provider names, diagnoses and treatment dates</b>. LACMA says it has notified law enforcement, has '
 'sent personalised notifications to affected individuals, and is offering <b>one year of identity-theft and '
 'fraud protection</b>.</p>'
 '<p class="note"><b>&#9888; The attack method and the number of individuals affected have not been disclosed</b>, '
 'and no threat actor, ransomware family, CVE or intrusion vector is stated in the reporting read this run &mdash; '
 'none is asserted here. This item is carried from security-press summaries, not from a notification letter fetched '
 'in full.</p></div>\n'
 '<div class="card"><div class="tags"><span class="tag new">New &middot; ' + TAG + '</span>'
 '<span class="tag">Phishing-as-a-service</span><span class="tag">Voice AI</span></div>'
 '<h3>A rented AI voice agent called 200 phone-theft victims pretending to be &ldquo;Alice from Apple Support&rdquo;</h3>'
 '<p>Researchers at <b>SOCRadar</b> have documented <b>AnonyMousKIT</b>, a phishing-as-a-service platform built '
 'for one specific job: harvesting the Apple ID credentials needed to <b>strip Activation Lock from stolen '
 'iPhones</b>. It has been <b>active since early 2024</b> and sits inside a structured resale ecosystem &mdash; '
 '<b>506 connected domains</b> feeding <b>168 storefront brands</b> acting as resellers, alongside access to '
 '<b>iCloud backups and Keychain credentials</b>. Delivery is a credit-based mix of phishing email, SMS, '
 'WhatsApp, recorded calls and <b>AI-powered voice agents</b>.</p>'
 '<p>The call records are the striking part. Researchers recovered <b>200 calls placed to victims between '
 'August&nbsp;31, 2025 and May&nbsp;30, 2026</b>, with <b>55 distinct interaction transcripts</b> handled by a '
 'voice AI agent operating under <b>five personas</b> &mdash; all five carrying the same translated identity, '
 '<b>&ldquo;Alice from Apple Support,&rdquo;</b> across <b>English, Spanish and Portuguese</b>. <b>179 of the '
 '200 calls went to numbers in Brazil.</b> In the recovered transcript the agent asks the victim to confirm '
 'ownership, requests the <b>four- or six-digit passcode</b> and <b>reads the digits back to confirm them</b>, '
 'then explains that someone visited an Apple Store to remove the Activation Lock and asks whether a recovery '
 'link has arrived by text.</p>'
 '<p class="note">The defensive point is not technical. There is no CVE, no patch and no federal deadline here &mdash; '
 'the control that fails is a human one, and the attacker&rsquo;s marginal cost of a fluent, patient, trilingual '
 'support call has collapsed. <b>&#9888; No dollar figure, no victim-loss total and no arrest or takedown is stated '
 'in the reporting read this run.</b></p></div>\n'
 '</div>\n<div class="cards">',
 "cy breach cards")

wr("cyber-briefing.html", cy)

# ============================ MMA ============================
mma = rd("mma-briefing.html")
mma = mma.replace('New &middot; 12:50', 'Carried &middot; 12:50 edition')
wr("mma-briefing.html", mma)

# ============================ INDEX ============================
ix = rd("index.html")

def card_swap(html, kicker_marker, new_h2, new_p):
    i = html.index(kicker_marker)
    h2s = html.index('<h2>', i); h2e = html.index('</h2>', h2s)
    html = html[:h2s] + '<h2>' + new_h2 + html[h2e:]
    ps = html.index('<p>', i); pe = html.index('</p>', ps)
    return html[:ps] + '<p>' + new_p + html[pe:]

ix = card_swap(ix, 'The Closing Bell',
  'All three indices red, on the first board of the day that reconciles on every line',
  'A live quote board fetched this run reads <b>S&amp;P&nbsp;500 7,667.22 (&minus;10.06, &minus;0.13%)</b>, '
  '<b>Dow 53,433.49 (&minus;143.91, &minus;0.27%)</b> and <b>Nasdaq Composite 26,055.25 (&minus;96.05, '
  '&minus;0.37%)</b> &mdash; all three subtracting exactly to Tuesday&rsquo;s closes &mdash; reversing an '
  '<b>11:47&nbsp;a.m. ET</b> read that still had the S&amp;P fractionally green at 7,678, while '
  '<b>Abercrombie &amp; Fitch</b> picks up a sixth rendering at <b>&plus;40%</b>, <b>Alibaba</b> claws back a '
  'plunge on a <b>$10&nbsp;billion share placement</b> for AI, energy and industrials lead the sectors, oil '
  'has a Wednesday print at <b>$80.78</b>, and the tape waits on <b>Nvidia after the close</b>.')

ix = card_swap(ix, 'The Cyber Wire',
  'The Gitea flaw gets a 9.8 &mdash; and CERT/CC ships two Kaltura bugs with no vendor to patch them',
  'The KEV-listed Gitea RCE <b>CVE-2026-60004</b> now carries <b>CVSS&nbsp;9.8</b> and a federal deadline of '
  '<b>Friday, August&nbsp;28</b>, confirmed independently by three outlets this run and sitting right behind '
  'the <b>CVSS&nbsp;10.0</b> Oracle flaw due <b>tomorrow</b>; separately CERT/CC published <b>VU#308749</b> '
  'covering two <b>unpatched, unauthenticated</b> flaws in <b>Kaltura&rsquo;s mwEmbed player</b> after being '
  '<b>&ldquo;unable to reach Kaltura,&rdquo;</b> the <b>Los Angeles County Museum of Art</b> disclosed a 2025 '
  'intrusion reaching <b>Social Security numbers and medical records</b>, and the federal board still holds '
  '<b>14 KEV deadlines with 10 past due</b>.')

wr("index.html", ix)

print("FAILS:" if fails else "OK - all anchors matched")
for f in fails: print("  " + f)
