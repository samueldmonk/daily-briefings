#!/usr/bin/env python3
"""12:35 PM ET Midday Edition edits — 2026-08-18."""
import io, sys, os

D = "/sessions/jolly-charming-keller/mnt/outputs"

def load(f):
    return io.open(os.path.join(D, f), encoding="utf-8").read()

def save(f, s):
    io.open(os.path.join(D, f), "w", encoding="utf-8").write(s)

def rep(s, old, new, label, count=1):
    assert s.count(old) >= 1, "MISSING: " + label
    return s.replace(old, new, count)

# ============================== WALL STREET ==============================
w = load("wallstreet-briefing.html")
if "NASDAQ:WDC" in w:
    print("WS already updated — skipping WS block"); SKIP_WS=True
else:
    SKIP_WS=False

# --- 1. tldr ---
w = rep(w,
  "<div class=\"tldr\"><b>The Tape</b> <span>Two hours in, the Nasdaq&rsquo;s loss has deepened to about 1.6% while the S&amp;P 500 holds at roughly &minus;0.5% and the Dow is down about 139 points &mdash; and the long end has quietly backed off, with the 10-year easing to 4.70% and the 30-year edging down to 5.30% after touching a 19-year high.</span></div>",
  "<div class=\"tldr\"><b>The Tape</b> <span>Three hours in, the Nasdaq has pared its loss to about 1.1%&ndash;1.3% and the Dow to about 0.2% &mdash; but the 30-year Treasury yield set a fresh 19-year high above 5.33% before easing back to 5.29%, and the memory-and-storage trade is the day&rsquo;s casualty, with Western Digital down 7%.</span></div>",
  "ws tldr")

# --- 2. lead heading + first two paragraphs ---
w = rep(w,
  "<h3>As of ~11:35 AM ET the Nasdaq is down about 1.6% &mdash; but the long end has eased, with the 30-year backing off its 19-year high</h3>",
  "<h3>As of ~12:35 PM ET the Nasdaq has pared its loss to about 1.1%&ndash;1.3% &mdash; after the 30-year set a fresh 19-year high above 5.33% and then eased back</h3>",
  "ws lead h3")

old_p1_start = "  <p><strong>The regular session is about two hours old as this edition is written, and the technology-led selling has deepened while the bond market that caused it has quietly relented.</strong> As of roughly <strong>11:36 AM ET</strong> the <strong>Nasdaq was down 1.6%</strong>, the <strong>S&amp;P 500 down 0.5%</strong> and the <strong>Dow Jones Industrial Average lower by about 139 points</strong>. The Nasdaq&rsquo;s loss has widened again &mdash; roughly 1.2% at 10:30, about 1.34% at 10:55, about 1.6% now &mdash; while the S&amp;P 500 has barely moved from where it opened the hour."
new_p1_start = "  <p><strong>The regular session is three hours old as this edition is written, and for the first time today the technology-led selling has eased rather than deepened.</strong> As of roughly <strong>12:35 PM ET</strong> the <strong>Nasdaq Composite was down 1.13%</strong>, the <strong>Dow Jones Industrial Average down 0.17%</strong> and the <strong>Russell 2000 down 0.96%</strong>, with the <strong>S&amp;P 500 off between 0.54% and 0.6%</strong> depending on the read. The Nasdaq&rsquo;s loss widened at every earlier check &mdash; roughly 1.2% at 10:30, about 1.34% at 10:55, about 1.6% at 11:36 &mdash; and has now narrowed to roughly <strong>1.1%&ndash;1.3%</strong>, the first improvement of the session; the Dow has all but closed its gap to unchanged."
w = rep(w, old_p1_start, new_p1_start, "ws lead p1")

old_p2 = "  <p><strong>What is doing the damage is now precisely locatable: it is the chips.</strong> The <strong>Philadelphia semiconductor index fell roughly 3.7%</strong> in early trade, with <strong>Nvidia, Meta and other large technology names</strong> weakening &mdash; a sector-level move nearly three times the Nasdaq&rsquo;s own."
new_p2 = "  <p><strong>What is doing the damage is now precisely locatable: it is memory and storage.</strong> <strong>Western Digital fell about 7%</strong>, to <strong>$500.05</strong> &mdash; the single steepest move on the tape &mdash; with <strong>SanDisk</strong> lower alongside it (rendered at 6% in one headline and 8% in the body of the same report, so both are given), <strong>Marvell Technology and Seagate Technology each down about 8%</strong> and <strong>Micron down about 5%</strong>. The framing from the reporting is macro, not company-specific: rising Treasury yields are pressuring what had become the most extended trade in the semiconductor sector. The reversal is sharp &mdash; on Monday Western Digital <em>gained</em> 6.5% as the memory-storage complex rallied on SanDisk&rsquo;s investor day and its ninth-generation QLC flash. Wider out, the <strong>Philadelphia semiconductor index fell roughly 3.7%</strong> in early trade, with <strong>Nvidia, Meta and other large technology names</strong> weakening &mdash; a sector-level move nearly three times the Nasdaq&rsquo;s own."
w = rep(w, old_p2, new_p2, "ws lead p2")

# --- 3. movers: drop stale New tag, insert new memory card ---
w = rep(w,
  "    <div class=\"tags\"><span class=\"tag new\">New</span><span class=\"tag up\">30Y 5.30%</span></div>",
  "    <div class=\"tags\"><span class=\"tag up\">30Y 5.30%</span></div>",
  "ws remove old New tag")

anchor = "  <div class=\"card\">\n    <div class=\"tags\"><span class=\"tag down\">SOX &minus;3.7%</span></div>"
new_card = """  <div class="card">
    <div class="tags"><span class="tag new">New</span><span class="tag down">WDC &minus;7%</span></div>
    <h4>The memory trade cracked &mdash; and Western Digital is the day&rsquo;s worst print</h4>
    <p><strong>Western Digital is cratering about 7%, to $500.05</strong>, the steepest single-name move on the tape and the clearest expression of the session. It does not stand alone: <strong>Marvell Technology and Seagate Technology are each down around 8%</strong>, <strong>SanDisk</strong> is sharply lower (one report renders the move at 6% in its headline and 8% in its body, so both are given) and <strong>Micron is off about 5%</strong>. The stated cause is macro rather than company-specific &mdash; rising Treasury yields are pressuring what had become the most extended trade in the semiconductor sector, a trade built on AI-server demand and supply-chain policy expectations. What makes it striking is the turn: <strong>on Monday Western Digital rose 6.5%</strong> as the memory-storage group rallied on SanDisk&rsquo;s investor day and its ninth-generation QLC flash announcement. One day of higher long yields has taken back more than the good news gave.</p>
  </div>
"""
w = rep(w, anchor, new_card + anchor, "ws insert memory card")

# --- 4. Chart of the Day -> Western Digital ---
w = rep(w, "Chart of the day &mdash; Fabrinet", "Chart of the day &mdash; Western Digital", "ws chart heading") if "Chart of the day &mdash; Fabrinet" in w else rep(w, "Chart of the day — Fabrinet", "Chart of the day — Western Digital", "ws chart heading")
w = rep(w, '{"symbol":"NYSE:FN","width":"100%","height":240', '{"symbol":"NASDAQ:WDC","width":"100%","height":240', "ws chart symbol")

# --- 5. ticker tape: feature WDC ---
w = rep(w, '{"proName":"NYSE:FN","title":"Fabrinet"}', '{"proName":"NASDAQ:WDC","title":"Western Digital"}', "ws ticker WDC")

# --- 6. rates: 30Y and 10Y ---
old30 = "<tr><td>US 30-year Treasury yield</td><td class=\"num\">5.30%</td><td><strong>Easing intraday.</strong> Yahoo Finance&rsquo;s live Tuesday coverage, fetched at roughly 11:36 AM ET, has the 30-year <strong>edging down to 5.30% after hitting a 19-year high</strong>. The high itself stands: CNBC reports the yield topping <strong>5.31%</strong> &mdash; 5.311%, up more than four basis points, the highest since <strong>June 2007</strong>; Bloomberg's live Tuesday coverage puts it near <strong>5.32%</strong>, up about two basis points. Both are printed rather than one picked. CNBC published a follow-up this morning on three things that could push it higher.</td></tr>"
new30 = "<tr><td>US 30-year Treasury yield</td><td class=\"num\">5.29%</td><td><strong>A NEW 19-year high, then a reversal.</strong> CNBC&rsquo;s Tuesday rates report has the 30-year <strong>topping 5.33%</strong> intraday &mdash; a fresh 19-year high on inflation and federal spending concerns, above the 5.31% printed Monday &mdash; before it <strong>fell more than a basis point to 5.294%</strong>. That is the level carried here. Bloomberg&rsquo;s live Tuesday coverage had it near <strong>5.32%</strong>, up about two basis points, earlier in the day; Yahoo Finance had it <strong>edging down to 5.30%</strong> at roughly 11:36 AM ET. Cited drivers: July&rsquo;s federal deficit was the largest monthly total since March 2021 and inflation is still well above the Fed&rsquo;s 2% target while the Middle East conflict lifts crude.</td></tr>"
w = rep(w, old30, new30, "ws 30Y row")

old10 = "<tr><td>US 10-year Treasury yield</td><td class=\"num\">4.70%</td><td><strong>First verified intraday Tuesday print.</strong> Yahoo Finance&rsquo;s live coverage at roughly 11:36 AM ET has the 10-year <strong>easing in morning trading but remaining elevated at 4.70%</strong>."
new10 = "<tr><td>US 10-year Treasury yield</td><td class=\"num\">4.71%</td><td><strong>Lower on the day, and off its morning level.</strong> CNBC&rsquo;s Tuesday rates report has the 10-year <strong>more than a basis point lower at 4.712%</strong> &mdash; the most recent verified print. Yahoo Finance&rsquo;s live coverage at roughly 11:36 AM ET had it <strong>easing in morning trading but remaining elevated at 4.70%</strong>."
w = rep(w, old10, new10, "ws 10Y row")

# --- 7. sector note: add Benzinga Aug 18 read ---
w = rep(w,
  "No verified percentage was carried for any other sector, so none is printed; the live heatmap above is the reference.",
  "Benzinga&rsquo;s own leading-and-lagging sectors piece for Tuesday, August 18 names <strong>XLE the day&rsquo;s top-gaining sector fund at $63.24, up 1.05%</strong> early on 201.7K shares, with <strong>XLP also among the gainers</strong> &mdash; a slightly smaller energy figure than the 1.30% above, so both reads are printed rather than one picked. No verified percentage was carried for any other sector, so none is printed; the live heatmap above is the reference.",
  "ws sector note")

# --- 8. sources ---
w = rep(w,
  '<li><a href="https://www.cnbc.com/2026/08/17/treasury-yields-federal-reserve-fomc-minutes.html">CNBC &mdash; 30-year Treasury yield tops 5.31%, the highest in 19 years</a></li>',
  '<li><a href="https://www.cnbc.com/2026/08/18/treasury-yields-.html">CNBC &mdash; 30-year Treasury yield tops 5.33%, new 19-year high on inflation, spending concerns (Aug 18)</a></li>\n    <li><a href="https://247wallst.com/investing/2026/08/18/micron-technology-falls-5-sandisk-sinks-6-western-digital-drops-7-as-higher-rates-test-the-memory-boom/">24/7 Wall St. &mdash; Micron Falls 5%, SanDisk Sinks 6%, Western Digital Drops 7% as Higher Rates Test the Memory Boom (Aug 18)</a></li>\n    <li><a href="https://www.benzinga.com/etfs/sector-etfs/26/08/61272272/leading-and-lagging-sectors-august-18-2026">Benzinga &mdash; Leading And Lagging Sectors For August 18, 2026</a></li>\n    <li><a href="https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-17-2026">TheStreet &mdash; Stock Market Today (Aug. 17, 2026): Western Digital +6.5% on the SanDisk investor day</a></li>\n    <li><a href="https://www.cnbc.com/2026/08/17/treasury-yields-federal-reserve-fomc-minutes.html">CNBC &mdash; 30-year Treasury yield tops 5.31%, the highest in 19 years (Aug 17)</a></li>',
  "ws sources")

save("wallstreet-briefing.html", w)

# ============================== CYBER ==============================
c = load("cyber-briefing.html")

# by-the-numbers: retire Heights tile, add Azure campaign tile
c = rep(c,
  '<div class="stat"><div class="n">1.2M</div><div class="l">People whose SSNs and account details were taken in the Heights Finance breach</div></div>',
  '<div class="stat"><div class="n">3.6M</div><div class="l">Azure/Entra directory records a single actor is offering from Fortune 500 tenants</div></div>',
  "cyber stat tile")

# drop stale New tag from Heights card
c = rep(c,
  '<div class="tags"><span class="tag new">New</span><span class="tag crit">1.2M people</span><span class="tag">Third-party cloud</span></div>',
  '<div class="tags"><span class="tag crit">1.2M people</span><span class="tag">Third-party cloud</span></div>',
  "cyber remove Heights New")

# insert new Azure card at top of Breaches
c = rep(c, 'Breaches &amp; incidents</h2>\n<div class="cards">\n',
  """Breaches &amp; incidents</h2>
<div class="cards">

  <div class="card">
    <div class="tags"><span class="tag new">New</span><span class="tag crit">3.6M records</span><span class="tag">Credential theft</span></div>
    <h4>&lsquo;TheHatman&rsquo; is selling the employee directories of nine household-name companies</h4>
    <p>A single actor using the moniker <strong>TheHatman</strong> is offering roughly <strong>3.6 million records</strong> said to have been pulled straight out of corporate <strong>Azure and Entra</strong> tenants. The named victims are not obscure: <strong>McDonald&rsquo;s Corporation tops the list with more than 1.7 million records</strong>, followed by <strong>Tata Consultancy Services at roughly 800,000</strong>, <strong>Vodafone at about 425,000</strong> and <strong>HCL Technologies at around 250,000</strong>, with <strong>InterContinental Hotels Group, Kyndryl, Gap Inc., Hexaware Technologies and Wyndham Hotels</strong> also listed. The contents are what make this different from a marketing-list dump: full names, corporate email addresses including active domains and tenant-specific <span class="cve">.onmicrosoft.com</span> structures, phone numbers, physical addresses, employee IDs, job titles, departments, manager details and direct reports, plus user group memberships, service accounts and <strong>Global Administrator listings</strong>. That is an org chart and a privileged-account map handed to whoever buys it &mdash; the ideal starting material for targeted vishing and business email compromise. <strong>Hudson Rock</strong> assesses with high confidence that the data is authentic but could <em>not</em> establish the initial access vector; the actor claims compromised credentials, and researchers float infostealer-harvested credentials or session cookies, phishing, weak or absent MFA and over-permissive third-party applications as the candidates. No software vulnerability is implicated. Treat the exposure as identity-layer, and the mitigation accordingly: conditional access, phishing-resistant MFA on privileged accounts, and a review of what third-party apps can read from the directory.</p>
  </div>
""",
  "cyber azure card")

# sources
c = rep(c, '<ul style="padding-left:18px;margin-top:10px">',
  '<ul style="padding-left:18px;margin-top:10px">\n    <li><a href="https://www.bleepingcomputer.com/news/security/hacker-claims-36-million-azure-account-records-stolen-from-major-companies/">BleepingComputer &mdash; Hacker claims 3.6 million Azure account records stolen from major companies</a></li>\n    <li><a href="https://www.securityweek.com/fortune-500-companies-hit-in-azure-data-theft-campaign/">SecurityWeek &mdash; Fortune 500 Companies Hit in Azure Data Theft Campaign</a></li>\n    <li><a href="https://www.theregister.com/security/2026/08/17/crook-hawks-millions-of-records-allegedly-plundered-from-corporate-azure-tenants/5288305">The Register &mdash; Crook hawks millions of records allegedly plundered from corporate Azure tenants (Aug 17)</a></li>\n    <li><a href="https://www.itpro.com/security/data-breaches/hacker-claims-to-have-stolen-millions-of-azure-customer-records-from-mcdonalds-vodafone-kyndryl-and-others-heres-what-we-know-so-far">IT Pro &mdash; Hacker claims to have stolen millions of Azure customer records from McDonald&rsquo;s, Vodafone, Kyndryl and others</a></li>\n    <li><a href="https://www.theregister.com/security/2026/08/18/cisa-gives-feds-3-days-to-fix-actively-exploited-ray-rce-bug/5289007">The Register &mdash; CISA gives feds 3 days to fix actively exploited Ray RCE bug (Aug 18)</a></li>\n    <li><a href="https://www.cisa.gov/news-events/alerts/2026/08/17/cisa-adds-one-known-exploited-vulnerability-catalog">CISA &mdash; CISA Adds One Known Exploited Vulnerability to Catalog (Aug 17, 2026)</a></li>',
  "cyber sources")

# patch priority: corroborate the 3-day window
c = rep(c,
  "federal remediation deadline is <strong>Thursday, August 20, 2026 \u2014 two days away</strong>.",
  "federal remediation deadline is <strong>Thursday, August 20, 2026 \u2014 two days away</strong> \u2014 a three-day window from Monday's KEV listing, as <em>The Register</em> put it this morning.",
  "cyber patch priority register")

save("cyber-briefing.html", c)

# ============================== INDEX ==============================
x = load("index.html")

x = rep(x,
  "<p>As of roughly 11:36 AM ET the Nasdaq was down 1.6%, the S&amp;P 500 down 0.5% and the Dow lower by about 139 points. The Nasdaq&rsquo;s loss has widened through the morning &mdash; about 1.2% at 10:30, 1.34% at 10:55, 1.6% now &mdash; even as the bond market that caused it relented: the 10-year has eased to 4.70% and the 30-year edged down to 5.30% after touching a 19-year high. The concentrated damage is in semiconductors: the Philadelphia semiconductor index fell roughly 3.7% in early trade, with Nvidia, Meta and other large technology names weakening together. The cause is unchanged &mdash; President Trump rejected extending the 60-day Iran ceasefire that expired Monday, crude stayed bid with Brent near a three-week high and US crude topping $85, and the 30-year Treasury yield hit a 19-year high earlier, CNBC putting it above 5.31% and Bloomberg near 5.32%. The money went to defensives: health care led sectors at +1.59%, energy +1.30% and staples +1.11%. Home Depot beat on both lines and reaffirmed guidance, then gave the gain back and spent the morning among the Dow&rsquo;s worst.</p>",
  "<p>As of roughly 12:35 PM ET the Nasdaq Composite was down 1.13%, the Dow 0.17% and the Russell 2000 0.96%, with the S&amp;P 500 off between 0.54% and 0.6% &mdash; the Nasdaq&rsquo;s first improvement of a session in which its loss had widened at every earlier check (about 1.2% at 10:30, 1.34% at 10:55, 1.6% at 11:36). The damage is concentrated in memory and storage: Western Digital is down about 7% to $500.05, Marvell and Seagate about 8% each, Micron about 5%, with rising long yields cited as the cause rather than anything company-specific &mdash; a hard turn from Monday, when Western Digital rose 6.5% on SanDisk&rsquo;s investor day. The long end made a new high and then reversed: CNBC has the 30-year topping 5.33%, a fresh 19-year high on inflation and deficit concerns, before falling to 5.294%, with the 10-year at 4.712%. The cause behind it is unchanged &mdash; President Trump rejected extending the 60-day Iran ceasefire that expired Monday and crude stayed bid, with Brent near a three-week high and US crude topping $85. The money went to defensives: health care led sectors at +1.59%, energy +1.30% (Benzinga has XLE +1.05%) and staples +1.11%.</p>",
  "index ws card")

x = rep(x,
  "Elsewhere on the page: consumer lender Heights Finance is notifying more than 1.2 million people that names, Social Security numbers, financial account details and government ID numbers were taken from a third-party cloud platform &mdash; a breach discovered on May 7 and notified only on August 11 &mdash; and CISA&rsquo;s deadline for the actively exploited Ray flaw falls Thursday.",
  "Elsewhere on the page: an actor calling himself TheHatman is offering roughly 3.6 million records pulled from corporate Azure and Entra tenants &mdash; more than 1.7 million from McDonald&rsquo;s, about 800,000 from Tata Consultancy Services, 425,000 from Vodafone &mdash; including job titles, manager chains and Global Administrator listings, with Hudson Rock calling the data authentic but the access vector unknown; consumer lender Heights Finance is notifying more than 1.2 million people whose Social Security numbers and account details were taken from a third-party cloud platform; and CISA&rsquo;s deadline for the actively exploited Ray flaw falls Thursday, a three-day window from Monday&rsquo;s KEV listing.",
  "index cyber card")

save("index.html", x)
print("OK — edits applied")
