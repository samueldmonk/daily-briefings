#!/usr/bin/env python3
# Sixteenth run, 2026-09-12 ~3:35pm ET. Targeted edits to the four pages.
import io, sys, re

D = "/sessions/eloquent-loving-curie/mnt/outputs/"
n_edits = 0

def edit(path, old, new, label):
    global n_edits
    p = D + path
    s = io.open(p, encoding="utf-8").read()
    if s.count(old) != 1:
        print("FAIL [%s] %s -> occurrences=%d" % (path, label, s.count(old)))
        sys.exit(1)
    s = s.replace(old, new)
    io.open(p, "w", encoding="utf-8").write(s)
    n_edits += 1

# ───────────────────────────── SUMMARY STRIPS ─────────────────────────────
TLDR_CY = ("A CVSS 10.0 flaw in Adobe Commerce and Magento was exploited three days before a patch "
           "existed and its federal deadline was 11 September, which this page had been publishing as "
           "22 September until this edition; a second maximum-severity bypass, in Cisco's firewall "
           "manager, is due today.")
TLDR_WS = ("Markets are shut for the weekend so Friday's close stands, and the week ahead turns on "
           "Wednesday's Federal Reserve decision, where one futures read on Friday put the chance of a "
           "rate hike at about 90%.")
TLDR_MM = ("Noche UFC's prelims are under way in Glendale with two results now official: Regina Tarin's "
           "decision over a ranked flyweight, and Sean King III's 36-second slam knockout — the result "
           "this page refused last run.")

# ───────────────────────────── CYBER ─────────────────────────────
edit("cyber-briefing.html",
 "<div class=\"tldr\"><b>The Wire</b> <span>CISA's federal patch deadline for a maximum-severity Cisco firewall-manager bypass falls today, and a seven-flaw KEV batch shows AI infrastructure — LiteLLM, Kestra, Starlette — is now being exploited for ransomware staging and cryptomining.</span></div>",
 "<div class=\"tldr\"><b>The Wire</b> <span>" + TLDR_CY + "</span></div>", "cy tldr")

edit("cyber-briefing.html",
 "  <span class=\"why\">A CVSS 10.0 authentication bypass in Cisco Secure Firewall Management Center is under active exploitation and its federal remediation deadline is <strong>today</strong>; a second CVSS 10.0 flaw, in GitLab, is due in two days.</span>",
 "  <span class=\"why\">Two CVSS 10.0 flaws are under active exploitation with federal deadlines at or past the wire: <strong>Adobe Commerce CVE-2026-75650</strong> was due <strong>11 September</strong> and is now overdue, and <strong>Cisco CVE-2026-20079</strong> is due <strong>today</strong>. A third, in GitLab, is due in two days.</span>",
 "cy threat why")

edit("cyber-briefing.html",
 """  <div class="stat"><div class="n">966</div><div class="l">flaws in the September Patch Tuesday, including 2 actively exploited zero-days and 105 rated Critical</div></div>
  <div class="stat"><div class="n">11</div><div class="l">CVEs added to the CISA KEV catalog in the seven days to 11 September</div></div>
  <div class="stat"><div class="n">395</div><div class="l">organisations across 48 countries hit in the agent-driven PaperCut campaign</div></div>
  <div class="stat"><div class="n">4.1M</div><div class="l">people whose data AdaptHealth confirms was exposed in the July attack</div></div>""",
 """  <div class="stat"><div class="n">3 days</div><div class="l">that Adobe Commerce stores were attacked before a patch for CVE-2026-75650 existed — exploitation from 4 September, hotfix on 7 September</div></div>
  <div class="stat"><div class="n">966</div><div class="l">flaws in the September Patch Tuesday, including 2 actively exploited zero-days and 105 rated Critical</div></div>
  <div class="stat"><div class="n">178</div><div class="l">FortiGate devices infected with the PivotC2 RAT, from more than 3,000 IP addresses targeted</div></div>
  <div class="stat"><div class="n">56</div><div class="l">exploitation attempts against Citrix NetScaler honeypots since 3 September, 36 of them on 8 September alone</div></div>""",
 "cy stats")

NEW_CY_LEAD = """<h2>Top Story</h2>
<div class="lead">
  <h3>A maximum-severity Magento flaw was being exploited three days before Adobe had a patch — and its federal deadline passed yesterday, eleven days earlier than this page had been reporting</h3>
  <p><strong>CVE-2026-75650</strong>, which Sansec named <strong>StyleSmuggler</strong>, is an unauthenticated arbitrary-code-execution flaw in <strong>Adobe Commerce, Adobe Commerce B2B and Magento Open Source</strong>. Adobe rates it <strong>Critical at CVSS 10.0</strong>, classifies it <strong>Priority 1</strong>, and states it is being exploited in the wild. The weakness is an improper neutralization of special elements in a template engine (<strong>CWE-1336</strong>): attacker-controlled data reaches Magento's template system through <code>styles</code> properties and is executed during server-side rendering, on a path that can be triggered through the <strong>Payment Transaction Failed Reminder</strong> email. Code execution happens while the server renders the content — <strong>nobody has to open the email</strong>.</p>
  <p>The timeline is the reason this leads. Sansec observed the <strong>first confirmed exploitation on 4 September</strong>, published its analysis on <strong>5 September</strong> after reproducing the unauthenticated chain on clean Magento Open Source <strong>2.4.7, 2.4.8 and 2.4.9</strong> installs, and watched implant variants appear on the 6th and the 7th. Adobe's emergency bulletin <strong>APSB26-146</strong> and the <strong>VULN-39341</strong> hotfix did not arrive until <strong>7 September</strong>. Sansec's first identified victim was running <strong>2.4.6-p15 with the July and August 2026 security updates already installed</strong> — patched to the month, and still exploitable. A second, separate actor used the same flaw to drop a <strong>PHP web shell</strong> below Magento's media cache.</p>
  <p>There is a trap in the remediation that is worth stating plainly. Adobe published its regular September Commerce update, <strong>APSB26-138</strong>, on 8 September, and its installation guidance says explicitly that installations receiving APSB26-138 <strong>must also receive the VULN-39341 hotfix</strong>. A <code>2026-sep</code> build does not contain the fix. Adobe also instructs operators to rotate the Commerce encryption key, admin passwords, REST/SOAP/GraphQL integration tokens, OAuth secrets, payment-gateway credentials, database credentials and privileged service accounts — and notes that <strong>rotating the encryption key does not invalidate credentials an attacker has already taken</strong>; each secret has to be rotated at the system that issued it.</p>
  <p><strong>And this page had the deadline wrong.</strong> CISA added CVE-2026-75650 to the KEV catalog on <strong>8 September with a remediation due date of 11 September</strong> — a three-day window. Previous editions listed it in a four-CVE group all due <strong>22 September</strong>, which put it eleven days late and, worse, made it look like a routine fourteen-day item rather than an emergency one. This site's own standing corrections file already recorded that <em>"the 8 September batch of four split between 11 and 22 September"</em>; the page never applied the split. The entry is corrected below, the countdown now reads overdue, and the failure was one of carrying a batch as a single row instead of taking the date CISA states per CVE — which is the rule this page publishes two sections further down.</p>
</div>

<h2>Second Read — AI Infrastructure as a KEV Category</h2>
<div class="lead">
  <h3>AI infrastructure has become a KEV category of its own"""

edit("cyber-briefing.html",
 """<h2>Top Story</h2>
<div class="lead">
  <h3>AI infrastructure has become a KEV category of its own""",
 NEW_CY_LEAD, "cy lead")

edit("cyber-briefing.html",
 """  <p><strong>CVE-2026-20079 — Cisco Secure Firewall Management Center (FMC) Software, CVSS 10.0.</strong> An unauthenticated remote attacker can bypass authentication and execute script files to obtain <strong>root</strong>. It is in the KEV catalog as actively exploited and the federal remediation deadline is <strong>Saturday 12 September 2026 — today, <span class="cd now" data-due="2026-09-12">—</span></strong>. If an FMC instance is reachable and unpatched, it is the single thing to fix before anything else on this page. The same three-day alert carried <strong>CVE-2026-19490</strong> (Citrix NetScaler ADC and NetScaler Gateway, CVSS 9.3, authentication bypass when configured as an AAA virtual server or Gateway) and a Fortinet flaw, on the same deadline.</p>""",
 """  <p><strong>CVE-2026-20079 — Cisco Secure Firewall Management Center (FMC) Software, CVSS 10.0.</strong> An unauthenticated remote attacker can bypass authentication and execute script files to obtain <strong>root</strong>. It is in the KEV catalog as actively exploited and the federal remediation deadline is <strong>Saturday 12 September 2026 — today, <span class="cd now" data-due="2026-09-12">—</span></strong>. If an FMC instance is reachable and unpatched, it is the single thing to fix before anything else on this page. Cisco has since <strong>updated its own advisory</strong> to say it became aware of active exploitation in <strong>August 2026</strong>, and that it identified <strong>three clusters of post-compromise activity</strong> on FMC instances — tracked as <strong>UAT-12197, UAT-11823 and UAT-11988</strong> — deploying web shells and malware.</p>
  <p>The same 9 September alert carried two more flaws on the same deadline, and both now have exploitation figures attached. <strong>CVE-2026-19490</strong> (Citrix NetScaler ADC and NetScaler Gateway, CVSS 9.3, authentication bypass when the appliance is configured as an AAA virtual server or as a Gateway) has drawn <strong>56 attempts against Previdian's honeypots since 3 September, 36 of them on 8 September alone</strong>. <strong>CVE-2025-25249</strong> (Fortinet FortiOS, FortiSwitchManager and FortiSASE, CVSS 7.3, heap-based buffer overflow reachable by an unauthenticated attacker) is the flaw SOCRadar ties to a campaign delivering a Node.js remote access trojan called <strong>PivotC2</strong>: more than <strong>3,000 IP addresses targeted</strong> and <strong>178 devices infected</strong>, concentrated in the United States, assessed to a financially motivated Russian-speaking actor, with the earliest evidence of exploitation dating to <strong>July 2026</strong>.</p>""",
 "cy patch priority")

edit("cyber-briefing.html",
 """<h2>Threat Actor Spotlight</h2>
<div class="cards">
  <div class="card">
    <div class="tags"><span class="t new">New</span><span class="t crit">Ransomware</span></div>""",
 """<h2>Threat Actor Spotlight</h2>
<div class="cards">
  <div class="card">
    <div class="tags"><span class="t new">New</span><span class="t crit">Two actors</span></div>
    <h4>The StyleSmuggler operators — an implant crew, and someone else entirely</h4>
    <p>Sansec's reporting describes <strong>two separate actors</strong> working the same Adobe Commerce flaw, which is the detail that makes this more than one campaign. The first deploys implants that hide behind ordinary-looking process and path names — <code>[kworker/u:8:0]</code>, <code>fc-cache</code>, <code>chronyd</code>, and files under <code>~/.local/share/.gvfsd/</code>, <code>~/.cache/fontconfig/</code> and randomly suffixed directories in <code>/tmp</code> — with variants appearing on 6 and 7 September as the campaign matured. The second simply drops a <strong>PHP web shell</strong> beneath Magento's media cache; unexpected executable PHP under <code>pub/media</code> is the check for it. Neither is named, and no ransomware brand is attached to either in anything read this run. Sansec also published network indicators for correlation, including hosts that typosquat legitimate services — <code>time.microsft.run</code>, <code>ntp.timesysnc.net</code>, <code>windwsecurity.run</code>.</p>
  </div>
  <div class="card">
    <div class="tags"><span class="t carry">Carried</span><span class="t crit">Ransomware</span></div>""",
 "cy spotlight new card")

edit("cyber-briefing.html",
 """    <h4>Qilin (also tracked as Agenda) — now tied to the AI-gateway exploitation chain</h4>""",
 """    <h4>Qilin (also tracked as Agenda) — tied to the AI-gateway exploitation chain</h4>""",
 "cy qilin heading")

# CVE table: correct the Adobe row and add two rows
edit("cyber-briefing.html",
 """  <tr><td class="mono">CVE-2026-75650</td><td class="mono" style="text-align:right">not stated</td><td>Adobe Commerce / Magento</td><td>KEV add 8 September, due 22 September</td></tr>""",
 """  <tr><td class="mono">CVE-2025-25249</td><td class="mono" style="text-align:right">7.3</td><td>Fortinet FortiOS / FortiSwitchManager / FortiSASE</td><td>Heap-based buffer overflow; unauthenticated code execution via crafted requests. Delivered the PivotC2 RAT. KEV; deadline today</td></tr>
  <tr><td class="mono">CVE-2026-87491</td><td class="mono" style="text-align:right">not stated</td><td>Google Chromium V8</td><td>Out-of-bounds write, exploited. Fixed in Chrome 153.0.8010.36. KEV add 9 September, due 23 September</td></tr>""",
 "cy table swap adobe row out")

edit("cyber-briefing.html",
 """  <tr><td class="mono">CVE-2026-20079</td><td class="mono" style="text-align:right">10.0</td><td>Cisco Secure Firewall Management Center</td><td>Authentication bypass, script execution as root, unauthenticated. KEV; deadline today</td></tr>""",
 """  <tr><td class="mono">CVE-2026-75650</td><td class="mono" style="text-align:right">10.0</td><td>Adobe Commerce / Commerce B2B / Magento Open Source</td><td>Template-engine injection (CWE-1336) to unauthenticated RCE. Adobe hotfix VULN-39341; a September build alone does not fix it. KEV add 8 September, due <strong>11 September — overdue</strong></td></tr>
  <tr><td class="mono">CVE-2026-20079</td><td class="mono" style="text-align:right">10.0</td><td>Cisco Secure Firewall Management Center</td><td>Authentication bypass, script execution as root, unauthenticated. Exploited since August 2026; three post-compromise clusters. KEV; deadline today</td></tr>""",
 "cy table adobe row in")

edit("cyber-briefing.html",
 """<div class="note">Every CVSS figure above comes from the vendor advisory, CISA or The Hacker News's reporting of the CISA alert, not from a blog's restatement. Where no score appears in a source read this run, the cell says <strong>not stated</strong> rather than carrying a number this page cannot attribute.</div>""",
 """<div class="note">Twenty-three rows. Every CVSS figure above comes from the vendor advisory, CISA or The Hacker News's reporting of the CISA alert, not from a blog's restatement. Where no score appears in a source read this run, the cell says <strong>not stated</strong> rather than carrying a number this page cannot attribute. Two rows changed this edition: <strong>CVE-2026-75650</strong> gains Adobe's own <strong>10.0</strong> and its corrected 11 September deadline, and <strong>CVE-2025-25249</strong> gains Fortinet's <strong>7.3</strong> — a flaw this page had been carrying only as "a Fortinet flaw" on the Cisco/Citrix deadline.</div>""",
 "cy table note")

edit("cyber-briefing.html",
 """  <li><strong>Added 8 September, due 22 September — CVE-2026-85880, CVE-2026-81963, CVE-2026-75650, CVE-2026-86218.</strong> <span class="cd" data-due="2026-09-22">—</span> Fourteen days, including the two Windows zero-days fixed in the 8 September Patch Tuesday.</li>
  <li><strong>Added 9 September, due 23 September — Chromium V8.</strong> <span class="cd" data-due="2026-09-23">—</span> Fourteen days, from the <em>same alert</em> as the three-day group above.</li>""",
 """  <li><strong>Added 8 September, due 11 September — Adobe Commerce CVE-2026-75650 (CVSS 10.0).</strong> <span class="cd now" data-due="2026-09-11">—</span> Three days, and <strong>the correction this edition makes</strong>: earlier editions of this page put this CVE in the fourteen-day group below. It was never in it.</li>
  <li><strong>Added 8 September, due 22 September — CVE-2026-85880, CVE-2026-81963, CVE-2026-86218.</strong> <span class="cd" data-due="2026-09-22">—</span> Fourteen days, including the two Windows zero-days fixed in the 8 September Patch Tuesday. The <em>same</em> four-CVE bulletin therefore carries both a three-day and a fourteen-day clock.</li>
  <li><strong>Added 9 September, due 23 September — Chromium V8 CVE-2026-87491.</strong> <span class="cd" data-due="2026-09-23">—</span> Fourteen days, from the <em>same alert</em> as the three-day group above. Fixed in Chrome 153.0.8010.36.</li>""",
 "cy kev split")

edit("cyber-briefing.html",
 """Across six add dates this site has now logged both three-day and fourteen-day windows, and once — the 9 September alert — both intervals appeared in a single alert.</li>""",
 """Across six add dates this site has now logged both three-day and fourteen-day windows, and <strong>twice</strong> — the 8 September and 9 September alerts — both intervals appeared within a single alert. The second of those two was only visible to this page once the Adobe row above was corrected.</li>""",
 "cy kev pattern")

edit("cyber-briefing.html",
 """  <p><strong>Summit Pathology (1,813,538 patients)</strong> remains refused""",
 """  <p><strong>A Texas water-treatment ransomware attack and a Siemens SIMATIC S7 flaw tracked as CVE-2026-12345</strong> were returned together this run by a daily OT-security roundup. Both are refused. <strong>CVE-2026-12345</strong> is a sequence this site has refused before as an obvious placeholder identifier, and this is its second sighting in an aggregator; the water-treatment incident appears in the same summary with no utility named, no state or federal advisory, and no corroboration in anything else read. An aggregator paragraph is where a claim starts, not where it is established.</p>
  <p><strong>Summit Pathology (1,813,538 patients)</strong> remains refused""",
 "cy refusals add")

edit("cyber-briefing.html",
 """    <a href="https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html">""",
 """    <a href="https://aicybr.com/blog/stylesmuggler-magento-adobe-commerce-zero-day-rce">AiCybr — "StyleSmuggler CVE-2026-75650: Adobe Hotfix, CISA KEV Deadline and September Update" (fetched in full; Adobe's 10.0 and Priority 1 ratings, APSB26-146 / APSB26-138 / VULN-39341, the 8 September KEV add with an 11 September due date, Sansec's timeline, affected trains, indicators and the credential-rotation sequence)</a><br>
    <a href="https://sansec.io/research/stylesmuggler-0day">Sansec — "StyleSmuggler: Magento and Adobe Commerce 0-day RCE under active attack" (cited by the above as the origin of the exploitation timeline and indicators)</a><br>
    <a href="https://helpx.adobe.com/security/products/magento/apsb26-146.html">Adobe — APSB26-146, emergency security update for Adobe Commerce</a><br>
    <a href="https://www.securityweek.com/adobe-patches-over-170-vulnerabilities-including-commerce-zero-day/">SecurityWeek — "Adobe Patches Over 170 Vulnerabilities, Including Commerce Zero-Day"</a><br>
    <a href="https://aicybr.com/blog/chrome-153-cve-2026-87491">AiCybr — "Chrome 153 Fixes Exploited CVE-2026-87491" (the Chromium V8 CVE identifier and its 23 September deadline)</a><br>
    <a href="https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html">""",
 "cy sources")

edit("cyber-briefing.html",
 """    <a href="https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html">The Hacker News — "CISA Flags Exploited Cisco, Citrix, Fortinet Flaws, Sets Sept. 12 Federal Patch Deadline"</a><br>""",
 """    <a href="https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html">The Hacker News — "CISA Flags Exploited Cisco, Citrix, Fortinet Flaws, Sets Sept. 12 Federal Patch Deadline" (fetched in full; the Fortinet CVSS 7.3, Cisco's advisory update and its three post-compromise clusters, the Previdian honeypot counts and the SOCRadar PivotC2 figures)</a><br>
    <a href="https://socradar.io/blog/cve-2025-25249-pivotc2-fortigate-rat/">SOCRadar — CVE-2025-25249 and the PivotC2 FortiGate RAT campaign (cited by the above)</a><br>
    <a href="https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2">Cisco — security advisory for CVE-2026-20079, updated for active exploitation</a><br>
    <a href="https://www.cisa.gov/news-events/alerts/2026/09/08/cisa-adds-four-known-exploited-vulnerabilities-catalog">CISA alert — four known exploited vulnerabilities added, 8 September 2026 (requested this run; the page returned no content, so the deadline split is sourced to AiCybr's reading of the KEV record)</a><br>""",
 "cy sources 2")

# ───────────────────────────── WALL STREET ─────────────────────────────
edit("wallstreet-briefing.html",
 "<div class=\"tldr\"><b>The Tape</b> <span>Wall Street snapped a four-session losing streak on Friday with all three indexes up about 1%, but the week still closed lower — and the Dow's weekly loss is 840.96 points, or 1.6%, retiring two smaller figures this site had carried.</span></div>",
 "<div class=\"tldr\"><b>The Tape</b> <span>" + TLDR_WS + "</span></div>", "ws tldr")

edit("wallstreet-briefing.html",
 """  <h3>Markets are closed for the weekend. Friday's rebound broke a four-day losing streak — and a corrected wire figure makes the week's damage larger than this site had been reporting.</h3>""",
 """  <h3>Markets are closed for the weekend. Friday's rebound broke what one week-ahead piece calls the S&amp;P 500's deepest four-day decline since June — and the week ahead is a Federal Reserve week.</h3>""",
 "ws lead h3")

edit("wallstreet-briefing.html",
 """  <p>The correction: earlier editions of this page carried a weekly Dow move of <strong>−1.51%</strong>,""",
 """  <p>Two things are newly sourced this run. First, the Friday percentages now have a second decimal that reconciles with the AP wire's rounded ones: <strong>S&amp;P 500 +0.86%</strong>, <strong>Dow +0.98%</strong>, <strong>Nasdaq composite +0.96%</strong> — each consistent with the points figures above and with AP's "0.9%" and "1%". Second, the context for that rebound: a week-ahead piece describes the index as having been on track for its <strong>deepest four-day decline since June</strong>, with <strong>WTI crude above $100</strong> and the <strong>10-year yield closing in on 5%</strong>, before buyers stepped in on Friday to halt the slide. The same piece attributes the losing week to a <strong>warmer-than-expected producer price index</strong>, surging energy prices and higher bond yields.</p>
  <p>The correction, carried forward: earlier editions of this page carried a weekly Dow move of <strong>−1.51%</strong>,""",
 "ws lead new para")

edit("wallstreet-briefing.html",
 """Friday's three headline closes are now re-confirmed for a <strong>sixteenth</strong> consecutive edition.""",
 """Friday's three headline closes are now re-confirmed for a <strong>seventeenth</strong> consecutive edition, this time against a wire summary carrying the percentages to two decimals.""",
 "ws scorecard note")

edit("wallstreet-briefing.html",
 """  <li><strong>Federal Reserve decision — Wednesday 16 September, 2 PM ET.</strong>""",
 """  <li><strong>Who is deciding, and what the expectation is.</strong> The week-ahead source read this run names <strong>Federal Reserve Chairman Kevin Warsh</strong> and says he will "likely deliver a hike" on Wednesday after the latest inflation data failed to settle fears about pricing pressure. It also describes a crucial week for global markets with the <strong>Fed, Bank of England and Bank of Japan</strong> all deciding against a backdrop of rising oil prices — three central banks in four days.</li>
  <li><strong>Federal Reserve decision — Wednesday 16 September, 2 PM ET.</strong>""",
 "ws radar warsh")

edit("wallstreet-briefing.html",
 """a carried CME FedWatch read gives <strong>~90%</strong>. Two of the three now cluster near 70%.</li>""",
 """a <strong>CME FedWatch</strong> read, now re-sourced this run and explicitly dated to <strong>11 September</strong>, gives roughly <strong>90%</strong>. Two of the three cluster near 70% and the third does not; all three are printed because the dispute is real.</li>""",
 "ws radar odds")

edit("wallstreet-briefing.html",
 """  <p>And the figure this site itself got wrong: <strong>−426 points</strong> for the Dow's week.""",
 """  <p>Nothing new was refused this run: no figure surfaced that had to be turned away, and the weekend means no new session to misread. The two items above stand from the previous edition, as does the figure this site itself got wrong: <strong>−426 points</strong> for the Dow's week.""",
 "ws refusals")

edit("wallstreet-briefing.html",
 """    <a href="https://www.cnbc.com/2026/09/10/stock-market-today-live-updates.html">CNBC — Stock market news for Sept. 11, 2026</a><br>""",
 """    <a href="https://www.cnbc.com/2026/09/10/stock-market-today-live-updates.html">CNBC — Stock market news for Sept. 11, 2026</a><br>
    <a href="https://www.ig.com/ae/news-and-trade-ideas/week-ahead--14-september-2026-260911">IG — "Week Ahead: 14 September 2026" (the Fed, BoE and BoJ schedule, the four-day decline framing, WTI above $100 and the 10-year approaching 5%)</a><br>
    <a href="https://www.cnbc.com/2026/09/11/stock-market-next-week-outlook-for-sept-14-18-2026.html">CNBC — "Stock market next week: Outlook for Sept. 14-18, 2026"</a><br>
    <a href="https://wtop.com/national/2026/09/how-major-us-stock-indexes-fared-friday-9-11-2026">WTOP / Associated Press — "How major US stock indexes fared Friday 9/11/2026" (Friday percentages to two decimals)</a><br>""",
 "ws sources")

# ───────────────────────────── MMA ─────────────────────────────
edit("mma-briefing.html",
 "<div class=\"tldr\"><b>Tale of the Tape</b> <span>Noche UFC is under way in Glendale and exactly one result is official: 21-year-old Regina Tarin beat the No. 15-ranked JJ Aldrich by unanimous decision, 29-28 on all three cards.</span></div>",
 "<div class=\"tldr\"><b>Tale of the Tape</b> <span>" + TLDR_MM + "</span></div>", "mm tldr")

NEW_MM_LEAD = """<h2>Top Story</h2>
<div class="lead">
  <h3>Sean King III ends it in 36 seconds with a slam — and the result this page refused last run is now official, while three others returned by the same search still are not</h3>
  <p>The second bout of the Noche UFC prelims lasted barely half a minute. <strong>Sean King III def. Jessie Rosas by KO (slam), round 1, 0:36</strong>, in a meeting of featherweight newcomers. The round-by-round account: King ducked under, picked Rosas up and drove him into the canvas — the reporter's comparison is to the Rock Bottom, professional wrestling's slam finisher — and Rosas was out on impact, before King could follow with punches. King came in <strong>6-0</strong> per UFC.com, which makes him <strong>7-0</strong>; the derivation is stated rather than implied. He was a <strong>−200</strong> favourite. Rosas came in <strong>8-1</strong>.</p>
  <p>That is the second official result of the card, after <strong>Regina Tarin def. JJ Aldrich by unanimous decision, 29-28 on all three scorecards</strong>, in the opener. Tarin arrived <strong>8-0</strong> off a February debut win and leaves <strong>9-0</strong>; Aldrich is <strong>15-7</strong> and the division's <strong>No. 15</strong> ranked flyweight. Both are published because a live blog carries them under a filled <strong>"Official decision"</strong> heading with a round-by-round account attached — not because a search returned them.</p>
  <p><strong>The King result is the one this page refused last run</strong>, and the refusal was correct at the time: the only live page then available listed the bout as "Next Up". What has changed is not the strength of the search result but the existence of a filled result field. That distinction is the whole method, and this run it cut in the other direction too — the same search that produced King also produced <strong>three more prelim winners that remain unconfirmed</strong>, and tracing them this time identified the mechanism. See the refusal block below: the culprit is a <em>betting-picks list written in "def." syntax</em>, sitting inside the very same live blog that carries the real results.</p>
</div>"""

edit("mma-briefing.html",
 """<h2>Top Story</h2>
<div class="lead">
  <h3>Regina Tarin opens Noche UFC by beating a ranked flyweight — and the result this page refused last run turns out to be the one that happened</h3>
  <p>The card opener at Desert Diamond Arena went the distance and to the 21-year-old. <strong>Regina Tarin def. JJ Aldrich by unanimous decision, 29-28 on all three scorecards</strong>, taking her professional record to <strong>9-0</strong> from the <strong>8-0</strong> she carried in, in only her second UFC appearance after a debut win in February. Aldrich, <strong>15-7</strong> and the <strong>No. 15 ranked</strong> women's flyweight, came in as a <strong>+240 underdog</strong> against Tarin at <strong>−300</strong>. Round-by-round coverage has the two trading elbows in the pocket late in the first, with Tarin edging it and growing more animated in the second.</p>
  <p>That is the only official result on this card as of the time stamped at the top of this page. Six more prelims and the six-bout main card were still to come or still unsettled: UFC.com's own prelim-results page and its official-scorecards page were both fetched during this run and <strong>both still carry every bout as a matchup with no result and no scorecard</strong>, and the live blog that did report Tarin's win lists the next bout, Sean King III vs Jessie Rosas, as "Next Up".</p>
  <p>The part worth recording is what it says about the previous edition. Last run this page <strong>refused</strong> a set of seven prelim winners returned by a search, after tracing them to an Athlon Sports page headlined "What AI Predicted and What Happened?" that contained a prediction table and no results at all — including <em>Regina Tarin, unanimous decision, 55% winner confidence</em>, annotated as "a coin-flip tier call". The prediction was correct. The refusal was still right: at the time there was no filled result field anywhere, and a forecast that later comes true was never evidence of anything. The model picked the <strong>−300 favourite</strong>, and the −300 favourite won. The six other predictions from that same table remain unpublished here, because they remain unconfirmed.</p>
</div>""",
 NEW_MM_LEAD, "mm lead")

edit("mma-briefing.html",
 """  <tr><td class="pend">Not yet official</td><td>Sean King III vs Jessie Rosas — featherweight <em>(prelim)</em></td><td class="pend">—</td></tr>""",
 """  <tr><td class="win">Sean King III</td><td>Sean King III vs Jessie Rosas — featherweight <em>(prelim)</em></td><td>KO (slam), round 1, 0:36</td></tr>""",
 "mm results king")

edit("mma-briefing.html",
 """<div class="note">Thirteen bouts: seven prelims and six on the main card. That count is now enumerated bout-by-bout by <strong>three independent sources</strong>""",
 """<div class="note"><strong>Two of thirteen decided</strong> at the time stamped at the top of this page, both of them prelims, both taken from filled result fields. UFC.com's own prelim-results page was fetched again this run and <strong>still carries all seven prelims as matchups</strong>, as does Sherdog's play-by-play, whose "The Official Result" headings are all empty — which is why neither is the source for the two results above. Thirteen bouts: seven prelims and six on the main card. That count is enumerated bout-by-bout by <strong>three independent sources</strong>""",
 "mm results note")

edit("mma-briefing.html",
 """    <h4>Sean King III — 6-0 featherweight, New Orleans</h4>
    <p>Undefeated and matched against <strong>Jessie Rosas</strong> (8-1) in a meeting of featherweight newcomers. King opened as a <strong>−200</strong> favourite. The bout had not been decided at the time of this edition.</p>""",
 """    <h4>Sean King III — 7-0 after 36 seconds</h4>
    <p>The New Orleans featherweight arrived <strong>6-0</strong> per UFC.com and leaves <strong>7-0</strong>, having slammed <strong>Jessie Rosas</strong> (8-1) unconscious at <strong>0:36 of the first round</strong> in a meeting of newcomers. He was a <strong>−200</strong> favourite. A knockout that fast, on a card built for highlights, is the kind of debut-tier win that gets a fighter booked again quickly — though no next booking is announced in anything read.</p>""",
 "mm prospect king")

edit("mma-briefing.html",
 """  <p><strong>"Sean King III def. Jessie Rosas via KO (slam) at 0:36 of R1".</strong> A results search returned this alongside the Tarin decision. It is not published: the round-by-round live blog that <em>did</em> carry Tarin's official result, timestamped minutes earlier, lists the King–Rosas bout as <strong>"Next Up"</strong>, and UFC.com's prelim-results and scorecards pages carry it as a matchup with no result. A specific method and a specific time do not make a result real. The standing rule from the previous run applies unchanged: during a live event, refuse every result that does not come from a filled result field, however specific and however many outlets appear to carry it.</p>""",
 """  <p><strong>Three prelim winners — Bahamondes over Salikhov, Gantt over Klose, and Rongzhu over Rafa García "by unanimous decision (29-28, 29-28, 29-28)".</strong> All three came back from the same search that produced the two real results above, and none is published. The live blog carrying the two official decisions lists <strong>Rafa Garcia vs Rongzhu, Drakkar Klose vs Tommy Gantt and Ignacio Bahamondes vs Muslim Salikhov as matchups</strong> in the same quick-results list where King and Tarin appear in bold as results.</p>
  <p><strong>And this run finally identifies where those phantom results come from.</strong> The Yahoo/Uncrowned live blog contains a block headed <strong>"Prelim Picks"</strong>, posted before the card started, and every line in it is written in exactly the syntax of a result: <em>"Thomas Gantt (−450) def. Drakkar Klose (+350)"</em>, <em>"Rong Zhu (−180) def. Rafa García (+145)"</em>, <em>"Ignacio Bahamondes (−600) def. Muslim Salikhov (+425)"</em>. Those are <strong>predictions with betting odds attached</strong>. Every "result" refused above is a line from that list, and the "29-28, 29-28, 29-28" bolted onto the Rongzhu line is Tarin's real scoreline, borrowed from a different fight. ⭐ <strong>The lesson: a picks list uses the same verb as a results list.</strong> "Def." is not evidence, favourites winning is not confirmation, and a correctly ordered set is what a picks list looks like by construction. Last run this page traced a fabricated set to a prediction table on an outside site; this run the same thing was sitting inside the source that carries the genuine results.</p>""",
 "mm refusals")

edit("mma-briefing.html",
 """  <p><strong>The six remaining Athlon Sports predictions</strong> — a page titled "Noche UFC Prediction, Results and Highlights", written in the past tense and containing no results — stay unpublished. One of its seven calls has now been vindicated; that changes nothing about the other six, which remain forecasts.</p>""",
 """  <p><strong>The remaining Athlon Sports predictions</strong> — a page titled "Noche UFC Prediction, Results and Highlights", written in the past tense and containing no results — stay unpublished. Two of its seven calls have now been vindicated by real results; that changes nothing about the other five, which remain forecasts.</p>""",
 "mm refusals athlon")

edit("mma-briefing.html",
 """<div class="note"><strong>Verification note, and it is a better one than the last two runs could give.</strong> ESPN's "Current and all-time UFC champions" page returned content this run after two consecutive runs of returning nothing, and it <strong>agrees with all eight men's divisions above, light heavyweight included</strong> — which resolves the light-heavyweight regression this site logged on 12 September, when that page was seating Alex Pereira on a result predating UFC 327. Two discrepancies remain and are resolved against this board, not against ESPN. First, the page <strong>still seats Valentina Shevchenko at women's flyweight</strong> on a September 2024 win over Alexa Grasso — a <strong>fourth consecutive</strong> run with that regression, refused here, and contradicted by UFC.com's own Noche UFC copy calling Grasso a <em>former</em> champion. Second, its defence counts lag: it lists <strong>0</strong> for both Mackenzie Dern and Joshua Van where each has a sourced UFC 330 or UFC 328 defence. The rule this site works to stands: treat that page as a cross-check, never as the source of truth, and re-derive every belt from the most recent title-changing card.</div>""",
 """<div class="note"><strong>Verification note.</strong> ESPN's "Current and all-time UFC champions" page was requested again this run and <strong>returned no content</strong> — so, unlike the previous edition, there is no cross-check to report either way, and this board stands on the derivation rather than on agreement with that page. What the previous run established is carried forward and unchanged: ESPN agreed on all eight men's divisions including light heavyweight, resolving a regression logged earlier on 12 September; it still seated <strong>Valentina Shevchenko</strong> at women's flyweight on a September 2024 win, which is refused here and is contradicted by UFC.com's own Noche UFC copy calling Alexa Grasso a <em>former</em> champion; and its defence counts lagged at <strong>0</strong> for both Mackenzie Dern and Joshua Van, each of whom has a sourced defence. Nothing on tonight's card can change a belt: <strong>no title is contested at Noche UFC</strong>, and the one bout with championship consequences, Fiorot–Grasso, is an eliminator. The rule stands: treat that page as a cross-check, never as the source of truth, and re-derive every belt from the most recent title-changing card.</div>""",
 "mm champ note")

edit("mma-briefing.html",
 """    <a href="https://sports.yahoo.com/mma/live/noche-ufc-live-results-jean-silva-vs-jose-delgado-updates-round-by-round-scoring-for-todays-fights-063000680.html">""",
 """    <a href="https://sports.yahoo.com/articles/noche-ufc-4-live-results-171500767.html">Yahoo Sports / MMA Mania — "Noche UFC 4 live results, highlights and play-by-play" (fetched in full; both official decisions under filled "Official decision" headings, with the round-by-round account of the King slam, and the remaining eleven bouts still listed as matchups)</a><br>
    <a href="https://www.ufc.com/news/noche-ufc-results-silva-vs-delgado">UFC.com — Main Card Results, Noche UFC (fetched this run; all six main-card bouts still carried as matchups, with fighter records, rankings and hometowns)</a><br>
    <a href="https://www.sherdog.com/news/news/UFC-Noche-4-Silva-vs-Delgado-playbyplay-results-round-scoring-202770">Sherdog — Noche UFC 4 play-by-play and round scoring (fetched this run; all thirteen "The Official Result" headings empty, and the weigh-in weights for every bout)</a><br>
    <a href="https://sports.yahoo.com/mma/live/noche-ufc-live-results-jean-silva-vs-jose-delgado-updates-round-by-round-scoring-for-todays-fights-063000680.html">""",
 "mm sources")

# ───────────────────────────── INDEX ─────────────────────────────
edit("index.html",
 "    <p>CISA's federal patch deadline for a maximum-severity Cisco firewall-manager bypass falls today, and a seven-flaw KEV batch shows AI infrastructure — LiteLLM, Kestra, Starlette — is now being exploited for ransomware staging and cryptomining.</p>",
 "    <p>" + TLDR_CY + "</p>", "ix cy")
edit("index.html",
 "    <p>Wall Street snapped a four-session losing streak on Friday with all three indexes up about 1%, but the week still closed lower — and the Dow's weekly loss is 840.96 points, or 1.6%, retiring two smaller figures this site had carried.</p>",
 "    <p>" + TLDR_WS + "</p>", "ix ws")
edit("index.html",
 "    <p>Noche UFC is under way in Glendale and exactly one result is official: 21-year-old Regina Tarin beat the No. 15-ranked JJ Aldrich by unanimous decision, 29-28 on all three cards.</p>",
 "    <p>" + TLDR_MM + "</p>", "ix mm")

print("OK — %d edits applied" % n_edits)
