import io, sys
from canonrep import load, save, rep, slice_between

# ============================== CYBER ==============================
f = 'cyber-briefing.html'; t = load(f)

t = rep(t,
  "<b>The Wire</b> <span>A Metabase flaw already sitting past-due in CISA's KEV catalogue was used to breach logistics provider ShipMonk and expose 13,689 Trezor hardware-wallet owners by name and home address &mdash; while the federal deadline for the actively exploited Ray flaw lands Thursday.</span>",
  '<b>The Wire</b> <span>North Korea&rsquo;s Lazarus group ran a Windows kernel zero-day against defence and aerospace firms for roughly five weeks before Microsoft patched it on August 11 &mdash; and the federal deadline for the actively exploited Ray flaw now lands Thursday.</span>',
  f, 'tldr')

t = rep(t,
  '<div class="why">A past-due KEV flaw in Metabase has now been used in a real supply-chain breach; two CVSS 9.8 flaws &mdash; macOS Screen Sharing and VMware vCenter &mdash; are confirmed exploited in the wild; seven KEV remediation deadlines are due or overdue for federal agencies; and a 1.6-million-account leak at RingCentral has now been indexed by Have I Been Pwned.</div>',
  '<div class="why">A Windows kernel zero-day was run by a nation-state actor against defence and aerospace targets for weeks before it was patched; a past-due KEV flaw in Metabase has been used in a real supply-chain breach; two CVSS 9.8 flaws &mdash; macOS Screen Sharing and VMware vCenter &mdash; are confirmed exploited in the wild; and seven KEV remediation deadlines are due or overdue for federal agencies.</div>',
  f, 'threat why')

t = rep(t,
  '<div class="stat"><div class="n">9.8</div><div class="l">CVSS of CVE-2026-65400, the exploited macOS Screen Sharing flaw</div></div>',
  '<div class="stat"><div class="n">5 weeks</div><div class="l">Lazarus ran the Windows AFD zero-day before Microsoft patched it</div></div>',
  f, 'stat tile')

OLD_TOP = slice_between(t, '<h2 class="sec">Top story</h2>', '<h2 class="sec">Patch priority</h2>')
NEW_TOP = '''<h2 class="sec">Top story</h2>
<div class="panel top">
  <h3>A fake Lockheed Martin job advert, a Windows kernel zero-day, and five weeks of unpatched access to defence contractors</h3>
  <p><strong>Check Point Research</strong> has attributed the zero-day exploitation of <strong>CVE-2026-68820</strong> &mdash; an elevation-of-privilege flaw in the Windows Ancillary Function Driver for WinSock, <span class="cve">AFD.sys</span> &mdash; to the North Korea-linked <strong>Lazarus Group</strong>, running its long-standing <strong>Operation Dream Job</strong> campaign. Microsoft patched the flaw on <strong>August 11, 2026</strong> in the August Patch Tuesday. Check Point reports the group had been exploiting it since at least <strong>early July</strong>, which puts roughly five weeks of live use behind the fix.</p>
  <p>The targeting is specific: organisations in <strong>defence, aerospace, aviation, drone, robotics and military technology</strong>, with victims reported across <strong>France, Germany, Brazil and India</strong>. The lure is a job offer. A victim downloads an encrypted archive containing a legitimate signed PDF viewer and a malicious DLL; the DLL displays a convincing <strong>Lockheed Martin</strong> job description on screen while silently loading <strong>MISTPEN</strong>, a lightweight downloader that communicates through the <strong>Microsoft Graph API and OneDrive</strong> &mdash; traffic that looks unremarkable on a corporate network.</p>
  <p>Once persistence is established, MISTPEN loads an in-memory privilege-escalation module that exploits the AFD.sys bug. The flaw is a <strong>use-after-free</strong> reached by triggering a race condition, and it yields <strong>SYSTEM</strong>. That, in turn, is used to execute a new version of <strong>FudModule</strong>, Lazarus&rsquo; kernel-mode rootkit.</p>
  <p>The chain is the point. A social-engineering lure gets code on the box; a kernel bug gets that code into the kernel; a rootkit keeps it there. None of the individual stages is novel, and that is exactly why it worked for five weeks. The flaw is already in CISA&rsquo;s Known Exploited Vulnerabilities catalogue &mdash; added <strong>August 11</strong>, federal remediation due <strong>August 25</strong> &mdash; so for once the patch, the KEV listing and the attribution have all landed inside a week of each other. Applying August&rsquo;s Patch Tuesday is the whole remediation.</p>
</div>

'''
t = rep(t, OLD_TOP, NEW_TOP, f, 'top story swap')

t = rep(t,
  '''<div class="tags"><span class="tag new">New</span><span class="tag">Pharma</span><span class="tag crit">Ransomware</span></div>''',
  '''<div class="tags"><span class="tag">Pharma</span><span class="tag crit">Ransomware</span></div>''',
  f, 'inotiv New off')

t = rep(t,
  '''    <tr>
      <td class="cve">CVE-2026-65400</td><td class="score s-crit">9.8</td>''',
  '''    <tr>
      <td class="cve">CVE-2026-68820</td><td class="score s-crit">7.0</td>
      <td>Windows Ancillary Function Driver for WinSock (AFD.sys)</td>
      <td>Use-after-free reached via a race condition, giving local escalation to SYSTEM. Exploited as a <strong>zero-day since at least early July</strong> by the Lazarus Group in Operation Dream Job, per Check Point Research, to load the FudModule kernel rootkit. Patched August 11, 2026; in CISA KEV the same day, federal deadline August 25.</td>
    </tr>
    <tr>
      <td class="cve">CVE-2026-65400</td><td class="score s-crit">9.8</td>''',
  f, 'cve 68820 row')

t = rep(t,
  '<span class="p">CVE-2026-68820</span> &mdash; Microsoft Windows Ancillary Function Driver for WinSock use-after-free. Added Aug 11, 2026. Due <strong>Aug 25, 2026</strong>. <span class="cd ok">(7 days left)</span>',
  '<span class="p">CVE-2026-68820</span> &mdash; Microsoft Windows Ancillary Function Driver for WinSock use-after-free. Added Aug 11, 2026. Due <strong>Aug 25, 2026</strong>. <span class="cd ok">(7 days left)</span> &mdash; the zero-day Lazarus ran against defence and aerospace firms before the August 11 patch.',
  f, 'kev 68820 note')

t = rep(t,
  '''<li><a href="https://www.bleepingcomputer.com/news/security/ringcentral-data-breach-exposed-info-of-16-million-accounts/">BleepingComputer &mdash; RingCentral data breach exposed info of 1.6 million accounts</a></li>''',
  '''<li><a href="https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/">Check Point Research &mdash; Shattering the Dream: when a job offer becomes a zero-day attack</a></li>
    <li><a href="https://www.bleepingcomputer.com/news/security/lazarus-hackers-exploited-windows-zero-day-to-target-defense-firms/">BleepingComputer &mdash; Lazarus hackers exploited Windows zero-day to target defense firms</a></li>
    <li><a href="https://www.securityweek.com/fresh-windows-zero-day-exploited-in-north-korean-cyberattacks/">SecurityWeek &mdash; Fresh Windows zero-day exploited in North Korean cyberattacks</a></li>
    <li><a href="https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html">The Hacker News &mdash; Lazarus exploits Windows zero-day to gain SYSTEM access and deploy backdoor</a></li>
    <li><a href="https://www.helpnetsecurity.com/2026/08/12/north-korea-lazarus-fake-job-offers/">Help Net Security &mdash; Lazarus hackers pair fake job offers with Windows zero-day exploit</a></li>
    <li><a href="https://www.bleepingcomputer.com/news/security/ringcentral-data-breach-exposed-info-of-16-million-accounts/">BleepingComputer &mdash; RingCentral data breach exposed info of 1.6 million accounts</a></li>''',
  f, 'cyber sources')

save(f, t)

# ============================ WALL STREET ==========================
f = 'wallstreet-briefing.html'; t = load(f)

t = rep(t,
  '<b>The Tape</b> <span>An hour into trade the tape has split &mdash; the Nasdaq Composite is down about 1.2% and the memory names are being marked down hard, while the Dow has nearly clawed back to flat behind J&amp;J, IBM and Chevron &mdash; with an expired US&ndash;Iran ceasefire keeping crude bid and the 30-year Treasury yield at 5.32%, its highest since 2007.</span>',
  '<b>The Tape</b> <span>Ninety minutes in, the split has widened rather than closed &mdash; the Nasdaq Composite is now off about 1.34% with the Philadelphia semiconductor index down roughly 3.7%, while the Dow sits all but flat at &minus;0.06% as health care, energy and staples absorb the rotation, and the 30-year Treasury yield holds a 19-year high.</span>',
  f, 'tldr')

t = rep(t,
  '<h3>A split tape as of ~10:30 AM ET: the Nasdaq is carrying the losses, the Dow has nearly recovered, and the 30-year sits at a 2007 high</h3>',
  '<h3>As of ~10:55 AM ET the split has widened: the Nasdaq is down about 1.34%, the chip index roughly 3.7%, and the Dow is all but flat</h3>',
  f, 'lead h3')

t = rep(t,
  '''<strong>The regular session is roughly an hour old as this edition is written.</strong> As of about 10:30 AM ET the <strong>Nasdaq Composite was down about 1.2%</strong>, the <strong>S&amp;P 500 about 0.6%</strong> and the <strong>Dow Jones Industrial Average about 0.3%</strong>, per <em>Yahoo Finance</em>'s and <em>TheStreet</em>'s live Tuesday coverage. That extends Monday's losses and puts the S&amp;P 500 on course for a third straight down day.</p>''',
  '''<strong>The regular session is about ninety minutes old as this edition is written, and the divergence has widened.</strong> As of roughly <strong>10:55 AM ET</strong> the <strong>Nasdaq Composite was down about 1.34%</strong>, the <strong>S&amp;P 500 about 0.57%</strong> and the <strong>Dow Jones Industrial Average about 0.06%</strong> &mdash; the Dow is now within a rounding error of unchanged while the Nasdaq&rsquo;s loss has deepened from the roughly 1.2% carried at 10:30. Earlier in the session the moves read <strong>Nasdaq &minus;1.2%, S&amp;P 500 &minus;0.6%, Dow &minus;0.3%</strong> on <em>Yahoo Finance</em>&rsquo;s and <em>TheStreet</em>&rsquo;s live Tuesday coverage; both reads are given, each stamped with its time. That extends Monday&rsquo;s losses and puts the S&amp;P 500 on course for a third straight down day.</p>''',
  f, 'lead p1')

t = rep(t,
  '''<strong>But the tape is splitting as the morning goes on, and that is the change since the open.</strong> A later intraday snapshot fetched this run had the <strong>Nasdaq 100 down 1.58%</strong> and the <strong>Russell 2000 down 0.68%</strong> while the <strong>Dow had pared to &minus;0.07%</strong> and the S&amp;P 500 sat at &minus;0.53% &mdash; the index carrying the least technology is the index taking the least damage.''',
  '''<strong>What is doing the damage is now precisely locatable: it is the chips.</strong> The <strong>Philadelphia semiconductor index fell roughly 3.7%</strong> in early trade, with <strong>Nvidia, Meta and other large technology names</strong> weakening &mdash; a sector-level move nearly three times the Nasdaq&rsquo;s own. An earlier intraday snapshot this run had the <strong>Nasdaq 100 down 1.58%</strong> and the <strong>Russell 2000 down 0.68%</strong> while the <strong>Dow had pared to &minus;0.07%</strong> and the S&amp;P 500 sat at &minus;0.53% &mdash; the index carrying the least technology is the index taking the least damage.''',
  f, 'lead p2')

t = rep(t,
  '''the US 30-year rose about two basis points to <strong>5.32%, the highest since 2007</strong>.''',
  '''the US 30-year sits at a <strong>19-year high</strong>. CNBC has it topping <strong>5.31%</strong> &mdash; 5.311%, up more than four basis points, the highest since <strong>June 2007</strong> &mdash; and Bloomberg&rsquo;s live coverage puts it around 5.32%, up about two basis points on Tuesday. CNBC followed up this morning with a piece on three things that could drive it higher still.''',
  f, 'lead 30yr')

# --- movers: drop the two prior New tags, add the semis card
t = rep(t,
  '''<div class="tags"><span class="tag new">New</span><span class="tag down">Reversed to &minus;1.24%</span></div>''',
  '''<div class="tags"><span class="tag down">Reversed to &minus;1.24%</span></div>''',
  f, 'HD New off')

t = rep(t,
  '''<div class="tags"><span class="tag new">New</span><span class="tag up">Defensives bid</span></div>''',
  '''<div class="tags"><span class="tag up">Defensives bid</span></div>''',
  f, 'rotation New off')

t = rep(t,
  '''  <div class="card">
    <div class="tags"><span class="tag down">MU, SK Hynix &minus;4%+</span></div>''',
  '''  <div class="card">
    <div class="tags"><span class="tag new">New</span><span class="tag down">SOX &minus;3.7%</span></div>
    <h4>The chip index, not the Nasdaq, is the real move</h4>
    <p>The <strong>Philadelphia semiconductor index fell roughly 3.7%</strong> in early trade, against the Nasdaq Composite&rsquo;s own decline of about 1%&ndash;1.34% &mdash; the sector is falling roughly three times as fast as the index it dominates. <strong>Nvidia, Meta and other large technology names</strong> weakened together. This is the cleanest read on the session: it is not a broad de-rating of equities but a concentrated markdown of long-duration semiconductor risk as the long end of the curve prints a 19-year high, with the rest of the market largely absorbing it.</p>
  </div>
  <div class="card">
    <div class="tags"><span class="tag down">MU, SK Hynix &minus;4%+</span></div>''',
  f, 'semis card')

t = rep(t,
  '''The <strong>Energy Select Sector SPDR ETF (XLE) was up 1.30%</strong> and among the top-performing sector funds &mdash; the rotation is the story the index-level numbers hide.</p>''',
  '''At the sector level the leadership is now legible: <strong>Health Care (XLV) is the top performer, up 1.59%</strong>, followed by <strong>Energy (XLE) at 1.30%</strong> and <strong>Consumer Staples (XLP) at 1.11%</strong> &mdash; defensives and value, in that order. The rotation is the story the index-level numbers hide.</p>''',
  f, 'rotation card sectors')

t = rep(t,
  '''One sector figure was corroborated this run &mdash; the <strong>Energy Select Sector SPDR ETF (XLE) up 1.30%</strong>, among the session's top-performing sector funds. No verified percentage was carried for any other sector, so none is printed; the live heatmap above is the reference.</div>''',
  '''Three sector figures were corroborated this run: <strong>Health Care (XLV) up 1.59%</strong>, the session&rsquo;s top-performing sector fund, <strong>Energy (XLE) up 1.30%</strong> and <strong>Consumer Staples (XLP) up 1.11%</strong> &mdash; a defensive-and-value leadership board. Against that, the <strong>Philadelphia semiconductor index is down roughly 3.7%</strong>. No verified percentage was carried for any other sector, so none is printed; the live heatmap above is the reference.</div>''',
  f, 'sector note')

t = rep(t,
  '''<td class="num">5.32%</td><td>Up about two basis points on Tuesday and the <strong>highest since 2007</strong>, per Bloomberg's live coverage. CNBC's Monday close was 5.311%.</td>''',
  '''<td class="num">5.31%&ndash;5.32%</td><td>A <strong>19-year high</strong>. CNBC reports the yield topping <strong>5.31%</strong> &mdash; 5.311%, up more than four basis points, the highest since <strong>June 2007</strong>; Bloomberg's live Tuesday coverage puts it near <strong>5.32%</strong>, up about two basis points. Both are printed rather than one picked. CNBC published a follow-up this morning on three things that could push it higher.</td>''',
  f, 'rates 30yr')

t = rep(t,
  '''<li><a href="https://www.cnbc.com/2026/08/18/stocks-making-the-biggest-moves-premarket-hd-tsla-fn-duol.html">''',
  '''<li><a href="https://www.cnbc.com/2026/08/18/30-year-treasury-yield-three-things-that-could-drive-it-even-higher.html">CNBC &mdash; The 30-year Treasury yield just hit a 19-year high (Aug 18)</a></li>
    <li><a href="https://www.cnbc.com/2026/08/17/treasury-yields-federal-reserve-fomc-minutes.html">CNBC &mdash; 30-year Treasury yield tops 5.31%, the highest in 19 years</a></li>
    <li><a href="https://stockmarketwatch.com/live/stock-market-today">StockMarketWatch &mdash; live sector performance (XLV, XLE, XLP), Aug 18</a></li>
    <li><a href="https://www.cnbc.com/2026/08/18/stocks-making-the-biggest-moves-premarket-hd-tsla-fn-duol.html">''',
  f, 'ws sources')

save(f, t)

# =============================== MMA ===============================
f = 'mma-briefing.html'; t = load(f)

t = rep(t,
  '''    <div class="tags"><span class="tag new">New</span></div>
    <h4>UFC Fight Night 285: Hernandez vs. Rodrigues</h4>''',
  '''    <h4>UFC Fight Night 285: Hernandez vs. Rodrigues</h4>''',
  f, 'sacramento New off')

t = rep(t,
  '''At middleweight, Gregory Rodrigues is given as <strong>No. 10</strong> in this run's fight-preview sourcing ahead of Saturday's main event, against the No. 11 an earlier edition carried &mdash; a one-place move, and the newer figure is the one used above.''',
  '''At middleweight, <strong>Gregory Rodrigues&rsquo; ranking is genuinely disputed across sources and this page will not pick one</strong>: fight-preview sourcing yesterday gave him <strong>No. 10</strong>, an earlier edition carried <strong>No. 11</strong>, and this run's event previews (MMA Mania, Yahoo Sports) give <strong>No. 12</strong>. All three were seen in sourcing within two days of each other, so no rank is printed on the card above &mdash; only Hernandez's No. 6, which every source agrees on.''',
  f, 'rodrigues rank')

save(f, t)

# ============================== INDEX ==============================
f = 'index.html'; t = load(f)

OLD_CY = slice_between(t, '<h2>A past-due KEV bug', '<span class="more">Read the briefing')
NEW_CY = '''    <h2>A fake Lockheed Martin job advert, a Windows kernel zero-day, and five weeks inside defence contractors</h2>
    <p>Check Point Research has attributed zero-day exploitation of CVE-2026-68820 &mdash; an elevation-of-privilege flaw in the Windows AFD.sys driver &mdash; to North Korea&rsquo;s Lazarus Group, running its long-standing Operation Dream Job campaign. Microsoft patched it on August 11; Check Point says the group had been using it since at least early July, roughly five weeks earlier. Targets were defence, aerospace, aviation, drone, robotics and military-technology organisations in France, Germany, Brazil and India. The lure is a job offer: a malicious DLL displays a convincing Lockheed Martin job description while loading MISTPEN, a downloader that talks through the Microsoft Graph API and OneDrive, which then escalates to SYSTEM through the AFD.sys use-after-free and executes the FudModule kernel rootkit. The flaw entered CISA&rsquo;s KEV catalogue on August 11 with a federal deadline of August 25. Elsewhere on the page: the ShipMonk breach that exposed 13,689 Trezor customers by name and address is attributed to a Metabase flaw whose own KEV deadline passed on August 14, and CISA&rsquo;s deadline for the actively exploited Ray flaw falls Thursday.</p>
    '''
t = rep(t, OLD_CY, NEW_CY, f, 'index cyber card')

OLD_MK = slice_between(t, '<h2>A split tape: the Nasdaq', '<span class="more">Read the briefing')
NEW_MK = '''    <h2>The split widened: the Nasdaq is off 1.34%, the chip index roughly 3.7%, and the Dow is all but flat</h2>
    <p>As of roughly 10:55 AM ET the Nasdaq Composite was down about 1.34%, the S&amp;P 500 about 0.57% and the Dow about 0.06% &mdash; the Nasdaq&rsquo;s loss has deepened since the 10:30 read while the Dow has closed almost the whole gap to unchanged. The concentrated damage is in semiconductors: the Philadelphia semiconductor index fell roughly 3.7% in early trade, with Nvidia, Meta and other large technology names weakening together. The cause is unchanged &mdash; President Trump rejected extending the 60-day Iran ceasefire that expired Monday, crude stayed bid with Brent near a three-week high and US crude topping $85, and the 30-year Treasury yield sits at a 19-year high, CNBC putting it above 5.31% and Bloomberg near 5.32%. The money went to defensives: health care led sectors at +1.59%, energy +1.30% and staples +1.11%. Home Depot beat on both lines and reaffirmed guidance, then gave the gain back and spent the morning among the Dow&rsquo;s worst.</p>
    '''
t = rep(t, OLD_MK, NEW_MK, f, 'index markets card')

t = rep(t,
  '''The next UFC card is Sacramento on Saturday, with Anthony Hernandez against Gregory Rodrigues at middleweight &mdash; Hernandez &minus;166 to &minus;176 across books after opening near &minus;147, with Rodrigues 19-6 and on a three-fight winning streak.</p>''',
  '''The next UFC card is Sacramento on Saturday, with No. 6 Anthony Hernandez against Gregory Rodrigues at middleweight &mdash; Hernandez &minus;166 to &minus;176 across books after opening near &minus;147, with Rodrigues 19-6 and on a three-fight winning streak. Rodrigues&rsquo; own ranking is given as No. 10, No. 11 and No. 12 by different sources within two days, so none is printed.</p>''',
  f, 'index mma card')

save(f, t)
print('\nALL EDITS APPLIED')
