# -*- coding: utf-8 -*-
"""Edits for the 2026-09-08 ~11:40am ET (Midday) edition."""
import io, os, sys

D = sys.argv[1]
def rd(f): return io.open(os.path.join(D, f), encoding="utf-8").read()
def wr(f, s): io.open(os.path.join(D, f), "w", encoding="utf-8").write(s)

N = 0
def rep(h, old, new, label):
    global N
    assert old in h, "MISS: " + label
    assert h.count(old) == 1, "AMBIG: " + label
    N += 1
    return h.replace(old, new)

# ======================= CYBER =======================
c = rd("cyber-briefing.html")

c = rep(c,
 "A third maximum-severity flaw has joined the day &mdash; an actively exploited CVSS 10.0 pre-authentication RCE in N-able N-central, the remote monitoring platform managed service providers use to reach every endpoint they administer &mdash; alongside the exploited Adobe Commerce zero-day, SAP&#39;s Patch Day and three open federal deadlines, the nearest in six days.",
 "Two exploited maximum-severity RCEs still lead the day &mdash; N-able N-central and Adobe Commerce &mdash; and a third live campaign surfaced this run: &ldquo;MikroTrick&rdquo;, an exploited MikroTik RouterOS chain that has been taking over internet-exposed routers since 2 September, with Microsoft&#39;s September Patch Tuesday due at 1 PM ET today and three federal deadlines open, the nearest in six days.",
 "cyber tldr")

c = rep(c,
 "Three separate CVSS 10.0 flaws are now in play &mdash; N-able N-central and Adobe Commerce, both confirmed exploited in the wild; SAP Extended Passport Processing, patched today &mdash; with three CISA remediation deadlines still open and the nearest six days out.",
 "Three separate CVSS 10.0 flaws are in play &mdash; N-able N-central and Adobe Commerce, both confirmed exploited in the wild; SAP Extended Passport Processing, patched today &mdash; and a fourth active campaign joined this run: the MikroTik RouterOS &ldquo;MikroTrick&rdquo; chain, exploited against exposed routers since 2 September. Three CISA remediation deadlines remain open, the nearest six days out.",
 "cyber banner")

c = rep(c,
 '<div class="stat"><div class="n">7,551</div><div class="l">Ransomware victims counted in Black Kite&#39;s 2026 report, up 24.9%</div></div>',
 '<div class="stat"><div class="n">7,551</div><div class="l">Ransomware victims counted in Black Kite&#39;s 2026 report, up 24.9%</div></div>\n'
 '<div class="stat"><div class="n">2 Sep</div><div class="l">Date from which CERT Polska says the MikroTik &ldquo;MikroTrick&rdquo; chain has been actively used against internet-exposed routers</div></div>',
 "cyber stats")

# Patch Priority: add MikroTik as the third named item
c = rep(c,
 "Second in line: <b>CVE-2026-75650</b>, Adobe Commerce / Magento, also CVSS 10.0 and exploited since 4 September.",
 "Second in line: <b>CVE-2026-75650</b>, Adobe Commerce / Magento, also CVSS 10.0 and exploited since 4 September. Third: <b>MikroTik RouterOS</b> &mdash; <b>CVE-2026-67276</b> chained with <b>CVE-2026-86060</b>, exploited since 2 September, fixed on 3 September; neither is in KEV either.",
 "cyber patch priority")

# New cards: MikroTik, Mathspace, AI-run intrusion
newcards = (
'<div class="card">\n'
'<div class="tags"><span class="t new">New</span><span class="t hot">Exploited</span></div>\n'
'<h3>&ldquo;MikroTrick&rdquo;: a two-bug chain is taking full control of exposed MikroTik routers</h3>\n'
'<p><b>CVE-2026-67276</b>, rated <b>9.2</b>, lets an unauthenticated attacker bypass <b>RouterOS</b> SSH authentication by forging a valid signature with an <b>RSA key exponent of one</b> &mdash; authenticating as an existing RouterOS user without that user&#39;s private key. Chained with <b>CVE-2026-86060</b>, an argument-injection flaw that escalates the session to full administrative privileges through a crafted username, the result is total device takeover. <b>CERT Polska</b> says the chain, which it dubs <b>MikroTrick</b>, has been used against internet-exposed routers <b>since 2 September 2026</b>; observed attacks created an <b>&ldquo;ops&rdquo; account</b> and originated from the IP address <b>82.192.72.4</b>. A separate write-up read this run tells administrators to look for an SSH user named <b>&ldquo;-2&rdquo;</b> as an indicator of compromise. <b>MikroTik shipped fixes on 3 September</b> &mdash; RouterOS <b>7.25beta3, 7.24.2, 7.23.4 or 6.49.21</b> &mdash; and CERT Polska published the technical detail and the CVE assignments on <b>5 September</b>. <b>No CVSS figure was stated for CVE-2026-86060 in anything read this run, so none is printed</b>, and neither CVE appears in a KEV addition, the most recent of which is dated 4 September.</p>\n'
'</div>\n'
'<div class="card">\n'
'<div class="tags"><span class="t new">New</span><span class="t">Education</span></div>\n'
'<h3>Mathspace: a breach reaching more than a million students and parents</h3>\n'
'<p>A breach at <b>Mathspace</b> exposed data on <b>over a million students and parents</b>, dated <b>8 September 2026</b> in a running breach index read this run. <b>The index entry states the scale and the date and nothing else &mdash; no attacker, no intrusion vector and no data categories were given, so none are asserted here.</b></p>\n'
'</div>\n'
'<div class="card">\n'
'<div class="tags"><span class="t new">New</span><span class="t hot">Method</span></div>\n'
'<h3>An intrusion run end-to-end by AI agents, finished in under ten hours</h3>\n'
'<p>A human ransomware operator used frontier models and agentic attack frameworks to breach an enterprise network in <b>less than ten hours</b> &mdash; work that reporting read this run puts at roughly <b>two weeks</b> for human operators. The AI agents carried out each step of the intrusion, and the episode ended with the attacker leaving the victim an <b>80-page security audit</b>. Reported <b>2 September 2026</b>. It is carried here as a change in tempo rather than in technique: the defensive implication is that the window between initial access and impact is compressing.</p>\n'
'</div>\n'
)
c = rep(c,
 'Breaches &amp; Incidents</h2>\n<div class="cards">\n',
 'Breaches &amp; Incidents</h2>\n<div class="cards">\n' + newcards,
 "cyber new cards")

# Demote last edition's New tags on cards that are no longer new
for h3, lbl in [
  ("Boston Scientific says the August cyberattack will cost it the year&#39;s forecast", "bsx"),
  ("An Accenture claim, a confirmed DHS intrusion and Kodak&#39;s 2.2 million", "acn"),
]:
    i = c.find(h3)
    assert i > 0, "MISS demote " + lbl
    j = c.rfind('<span class="t new">New</span>', 0, i)
    assert j > 0 and i - j < 400, "demote anchor " + lbl
    c = c[:j] + '<span class="t">Carried</span>' + c[j + len('<span class="t new">New</span>'):]
    N += 1

# Rhysida spotlight: demote New -> Carried
i = c.find("Rhysida &mdash; and a captured state government")
j = c.rfind('<span class="t new">New</span>', 0, i)
assert j > 0 and i - j < 300
c = c[:j] + '<span class="t">Carried</span>' + c[j + len('<span class="t new">New</span>'):]
N += 1

# CVE table rows
c = rep(c,
 '<tr><td>CVE-2026-58240</td>',
 '<tr><td>CVE-2026-67276</td><td class="down">9.2</td><td>MikroTik RouterOS &mdash; fixed in 7.25beta3, 7.24.2, 7.23.4, 6.49.21</td><td>SSH authentication bypass by forging a signature with an RSA key exponent of one. Half of the &ldquo;MikroTrick&rdquo; chain; exploited since 2 Sep, fixes shipped 3 Sep. Not in KEV as of the 4 Sep addition.</td></tr>\n'
 '<tr><td>CVE-2026-86060</td><td class="mut">Not stated in any return read this run</td><td>MikroTik RouterOS</td><td>Argument injection via a crafted username; escalates a bypassed SSH session to full administrative privileges. The second half of the chain.</td></tr>\n'
 '<tr><td>CVE-2026-58240</td>',
 "cyber cve rows mikrotik")

c = rep(c,
 '<tr><td>CVE-2026-76969</td>',
 '<tr><td>CVE-2026-66768</td><td class="down">9.0</td><td>SAP GUI for Java</td><td>Improper access control. Part of today&#39;s SAP Security Patch Day.</td></tr>\n'
 '<tr><td>CVE-2026-76969</td>',
 "cyber cve row sapgui")

wr("cyber-briefing.html", c)

# ======================= WALL STREET =======================
w = rd("wallstreet-briefing.html")

w = rep(w,
 "Stocks are lower across the board in late Tuesday morning trade with the Dow much the weakest of the three, as Houthi strikes on southern Saudi Arabia push crude higher and put energy at the top of the board, while single names swing hard on drug-trial results, an index addition and a downgrade.",
 "Stocks are lower across the board in late Tuesday morning trade with the Dow much the weakest of the three, as Houthi strikes on southern Saudi Arabia push crude higher, energy leads the board and the 10-year Treasury yield tops 4.8% for the first time since October 2023.",
 "ws tldr")

w = rep(w,
 "As of ~11:05 AM ET: stocks slip on all three indices, the Dow much the hardest hit, as strikes on Saudi oil installations lift crude",
 "As of ~11:35 AM ET: stocks slip on all three indices, the Dow much the hardest hit, as strikes on Saudi oil installations lift crude and the 10-year yield tops 4.8%",
 "ws lead head")

w = rep(w,
 "All three reads returned again in this run unchanged from the previous edition, so they are re-confirmed rather than refreshed; the movement since the last edition is in single names, below, not in the index prints.",
 "All three reads returned again in this run unchanged from the previous edition, so they are re-confirmed rather than refreshed; the movement since the last edition is in rates and single names, not in the index prints. <b>What is new at this hour is the bond market:</b> the <b>10-year Treasury yield topped 4.8% on Tuesday, its highest since October 2023</b>, while the <b>2-year was flat at 4.3810%</b> &mdash; the first 8 September curve reads to appear in returns, the bond market having been shut on Monday for Labor Day. Rate-hike pricing firmed with it: markets are putting roughly a <b>58% probability on a 25 basis point increase</b> at the <b>15&ndash;16 September FOMC meeting</b>.",
 "ws lead rates")

# Semiconductor list: refused, with reason
w = rep(w,
 "Semiconductors more broadly are providing the cushion under the Nasdaq: the <b>VanEck Semiconductor ETF (SMH) is trading 1% higher</b>, with <b>Micron (MU) up 2.0%</b> and <b>Nvidia (NVDA) up 1.2%</b>.",
 "Semiconductors more broadly are providing the cushion under the Nasdaq: the <b>VanEck Semiconductor ETF (SMH) is trading 1% higher</b>, with <b>Micron (MU) up 2.0%</b> and <b>Nvidia (NVDA) up 1.2%</b>. <span class=\"mut\">A mid-morning list of larger semiconductor moves was returned this run &mdash; and refused. One of its figures, <b>Sandisk up 11.9%</b>, matches exactly a move independently verified this run as having happened on <b>Friday 4 September</b>, on the news that Sandisk joins the S&amp;P 100 later this month. Because a session-dating error is the likeliest explanation for the whole list, none of its percentages are printed and the earlier, separately sourced figures above are carried instead. The qualitative point that both reads agree on is printed: technology is showing intraday resilience, supported by strength in semiconductor equities.</span>",
 "ws semis refusal")

# Rates table updates
w = rep(w,
 "Markets price a roughly <b>52%</b> chance of a <b>25 basis point increase</b> this month; a CME FedWatch reading returned this run puts the probability of a hike at the September meeting at <b>60.4%</b>. Readings across sources this week span <b>50&ndash;63%</b>, so the range is printed rather than averaged.",
 "The <b>FOMC meets 15&ndash;16 September</b>. Markets price a roughly <b>52%</b> chance of a <b>25 basis point increase</b> this month; a CME FedWatch reading returned in an earlier edition put it at <b>60.4%</b>, and a read taken this run puts it at <b>58%</b>. Readings across sources this week span <b>50&ndash;63%</b>, so the range is printed rather than averaged.",
 "ws fed row")

w = rep(w,
 "Full curve as of Friday 4 September. The 10-year rose nearly 3 basis points to 4.79% on Friday following a stronger-than-expected jobs report. The bond market was closed Monday for Labor Day; no 8 September curve was published in returns read this run.",
 "Levels are the full curve as of Friday 4 September; the bond market was shut Monday for Labor Day. <b>Two 8 September reads arrived this run:</b> the <b>10-year topped 4.8%, its highest since October 2023</b>, and the <b>2-year was flat at 4.3810%</b>. No full 8 September curve was published in returns read this run, so the Friday levels stay in this column and the intraday reads are noted here.",
 "ws curve note")

w = rep(w,
 "<td>Brent crude</td>",
 "<td>Brent crude</td>", "ws brent anchor")

w = rep(w,
 "Two reads from different moments this morning. Both have Brent up on the day; they do not agree on the level.",
 "Three reads from different moments this morning &mdash; a third this run has Brent <b>up 1.76% at $98.71</b>, described as heading towards $100. All have Brent higher on the day; they do not agree on the level.",
 "ws brent note")

w = rep(w,
 "Same two reads. Crude is at a six-week high as investors assess the impact of the U.S.&ndash;Iran conflict on global supply.",
 "Same reads; a third this run has WTI <b>up more than 3% in early trade at $94.20</b>. Crude is at a six-week high as investors assess the impact of the U.S.&ndash;Iran conflict on global supply.",
 "ws wti note")

wr("wallstreet-briefing.html", w)

# ======================= MMA =======================
m = rd("mma-briefing.html")

m = rep(m,
 '<span class="mut">Odds: none returned this run for this card.</span>',
 '<span class="mut">Odds: none returned this run for this card.</span> New detail this run: <b>Nat&aacute;lia Silva is 20-5-1</b> and <b>29</b>, and has <b>won all eight of her UFC appearances</b>, including wins over former champions <b>J&eacute;ssica Andrade, Alexa Grasso and Rose Namajunas</b>; <b>Wang Cong is 10-1</b> and <b>34</b>, has won <b>five of her six UFC outings</b>, and most recently beat <b>Tracy Cortez by decision at UFC 329 in July</b>. Both are ranked inside the top six of the division.',
 "mma 332 records")

m = rep(m,
 "One source read this run renders the venue &ldquo;Diamond Desert Arena&rdquo;;",
 "Also on the card: former flyweight champion <b>Brandon Moreno</b> against <b>Joseph Morales</b>, the winner of <i>The Ultimate Fighter</i> season 33, and <b>Manon Fiorot</b> against former women&#39;s flyweight champion <b>Alexa Grasso</b>. One source read this run renders the venue &ldquo;Diamond Desert Arena&rdquo;;",
 "mma noche undercard")

# New prospect card: DWCS Week 5 tonight
m = rep(m,
 'Prospect Watch</h2>',
 'Prospect Watch</h2>', "mma prospect anchor")

pw = (
'<div class="card">\n'
'<div class="tags"><span class="t new">New</span><span class="t pro">Tonight</span></div>\n'
'<h3>Contender Series Week 5 runs tonight, five contract fights</h3>\n'
'<p><b>Dana White&#39;s Contender Series season 10, Week 5</b> takes place <b>tonight, Tuesday 8 September</b>, at the <b>Meta APEX in Las Vegas</b>, with <b>five bouts</b>: <b>Arlind Berisha vs. Quentin Pasley</b> at 205 pounds, <b>Isaac Moreno vs. R. Junior</b> at 170, <b>Mart&iacute;n Koz&aacute;k vs. C. Echols</b>, <b>Won Il Kwon vs. Apollo Gomes</b> at 135 and <b>Colton Loud vs. C. Natividad</b> at 125. <b>Two opponents are given only by initial and surname in the listing read this run, and one bout&#39;s weight was returned as a figure that is not a standard division, so it is not printed.</b> Contracts are announced live at the end of the night by Dana White and the matchmakers; <b>no Week 5 results or contract offers had been published in anything read this run</b>, so none are reported.</p>\n'
'</div>\n'
)
i = m.find('Prospect Watch</h2>')
j = m.find('<div class="cards">', i)
assert j > 0
k = j + len('<div class="cards">\n')
m = m[:k] + pw + m[k:]
N += 1

# Champions board: this run's list corroborates Ulberg
m = rep(m,
 "<b>The ESPN-attributed list read this run seats Alex Pereira here; that is refused</b> &mdash; a list that predates UFC 327 cannot be current.",
 "<b>The ESPN-attributed list read this run seats Ulberg here, dated to 11 April 2026 &mdash; the first edition in which that list agrees with this board at light heavyweight.</b> Earlier editions were read a version of the same list that seated Alex Pereira, which was refused each time; the refusal stands as a record, but it does not apply to this run&#39;s read.",
 "mma lhw note")

m = rep(m,
 "Nine of the eleven champions on the list read this run matched this board by name; two are refused above.",
 "Ten of the eleven champions on the list read this run matched this board by name; one &mdash; women&#39;s flyweight &mdash; is refused above, an eighth consecutive edition in which that entry has come back stale.",
 "mma board note")

m = rep(m,
 "and this run independently confirmed Silva vs. Wang Cong as a fight for the vacant title.",
 "and this run independently confirmed, for an eighth consecutive edition, that <b>Shevchenko vacated the belt after an undisclosed injury expected to keep her out for about a year</b>, and that Silva vs. Wang Cong is a fight for the vacant title.",
 "mma wflw note")

wr("mma-briefing.html", m)

# ======================= INDEX =======================
x = rd("index.html")
x = rep(x,
 "<h2>A third CVSS 10.0 flaw, exploited in the wild</h2>",
 "<h2>A third exploited campaign: MikroTik routers</h2>", "ix cy head")
x = rep(x,
 "A third maximum-severity flaw has joined the day &mdash; an actively exploited CVSS 10.0 pre-authentication RCE in N-able N-central, the remote monitoring platform managed service providers use to reach every endpoint they administer &mdash; alongside the exploited Adobe Commerce zero-day, SAP&#39;s Patch Day and three open federal deadlines, the nearest in six days.",
 "Two exploited maximum-severity RCEs still lead the day &mdash; N-able N-central and Adobe Commerce &mdash; and a third live campaign surfaced this run: &ldquo;MikroTrick&rdquo;, an exploited MikroTik RouterOS chain that has been taking over internet-exposed routers since 2 September, with Microsoft&#39;s September Patch Tuesday due at 1 PM ET today and three federal deadlines open, the nearest in six days.",
 "ix cy body")
x = rep(x,
 "<h2>Oil strikes lift crude, the Dow lags again</h2>",
 "<h2>Crude climbs and the 10-year tops 4.8%</h2>", "ix mk head")
x = rep(x,
 "Stocks are lower across the board in late Tuesday morning trade with the Dow much the weakest of the three, as Houthi strikes on southern Saudi Arabia push crude higher and put energy at the top of the board, while single names swing hard on drug-trial results, an index addition and a downgrade.",
 "Stocks are lower across the board in late Tuesday morning trade with the Dow much the weakest of the three, as Houthi strikes on southern Saudi Arabia push crude higher, energy leads the board and the 10-year Treasury yield tops 4.8% for the first time since October 2023.",
 "ix mk body")
x = rep(x,
 "UFC 332 on 3 October will put its entire main card live and free on CBS for the first time ever, headlined by Nat&aacute;lia Silva against Wang Cong for the vacant women&#39;s flyweight title &mdash; one of twelve events left on the 2026 calendar, which runs through UFC 335 in Las Vegas on 12 December.",
 "UFC 332 on 3 October will put its entire main card live and free on CBS for the first time ever, headlined by Nat&aacute;lia Silva (20-5-1) against Wang Cong (10-1) for the vacant women&#39;s flyweight title, while Contender Series Week 5 puts five more contract fights on at the Meta APEX tonight.",
 "ix mm body")
wr("index.html", x)

print("edits applied:", N)
