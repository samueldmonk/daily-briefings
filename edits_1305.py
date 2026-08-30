# -*- coding: utf-8 -*-
import io,sys
def rd(p): return io.open(p,encoding='utf-8').read()
def wr(p,s): io.open(p,'w',encoding='utf-8').write(s)
fails=[]
def rep(s,old,new,label,count=1):
    if old not in s:
        fails.append('MISSING: '+label); return s
    return s.replace(old,new,count)

# ---------------- CYBER ----------------
c=rd('cyber-briefing.html')

# 1. KEV note -> append ninth check
old_eighth = u'a stalled run is exactly how a &ldquo;due today&rdquo; row becomes wrong.<br><br>'
new_eighth = old_eighth + (
 u'<b>A ninth check at 12:58 PM returned the same top of the catalogue &mdash; and a third hole in it.</b> '
 u'CISA&rsquo;s own alert pages came back for <b>August 11</b> (three), <b>August 18</b> (four), <b>August 20</b> (two), '
 u'<b>August 21</b> (one) and <b>August 26</b> (six), with <b>nothing dated later than August 27</b>, so the four rows '
 u'above stand unmoved. This run also named ids the board had only counted: the August 11 batch is '
 u'<b>CVE-2026-20349</b> (Cisco Secure Firewall ASA and FTD), <b>CVE-2026-68820</b> (Windows WinSock use-after-free) '
 u'and <b>CVE-2026-72898</b> (Metabase SQL injection); the August 18 batch is <b>CVE-2026-33824</b> (Microsoft IKE '
 u'double free), <b>CVE-2026-55040</b> (SharePoint weak authentication), <b>CVE-2026-59310</b> (Broadcom VMware '
 u'vCenter path traversal) and <b>CVE-2026-65400</b> (Apple macOS improper authentication); the August 20 pair is '
 u'<b>CVE-2026-72529</b> and <b>CVE-2026-72530</b>, both TrueConf Server. &#9888; <b>The single-vulnerability alert '
 u'this run is dated August 21, not August 24</b>, and it is <b>CVE-2026-73570</b>, a Zimbra Collaboration Suite OS '
 u'command injection. That is a <b>third</b> addition this board has never carried, after the August 24 Oracle alert '
 u'and the August 25 Gitea entry &mdash; and, like both of those, <b>no source fetched this run states a due date for '
 u'it, so it gets no row and no countdown</b>. Three known gaps in nine checks is the measure of how much of the '
 u'catalogue these searches actually see.<br><br>')
c = rep(c, old_eighth, new_eighth, 'cyber ninth check')

# 2. Two new incident cards, inserted at the top of Breaches & Incidents
anchor = u'<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">'
newcards = anchor + (
 u'<div class="card"><div class="tags"><span class="tag tnew">New</span><span class="tag">AI</span>'
 u'<span class="tag">Account takeover</span></div>'
 u'<h3>Anthropic is signing users out of Claude: infostealer malware on their own machines was hijacking live sessions to burn their usage.</h3>'
 u'<p><b>Anthropic has begun warning Claude users that infostealer malware running on their PCs stole active '
 u'Claude login sessions</b>, and that an attacker used those sessions to sign in to their accounts and consume '
 u'their usage. The company&rsquo;s notice to affected users describes a bad actor using <b>common infostealer '
 u'malware</b> to lift session tokens from people&rsquo;s computers and then reach the accounts with them.</p>'
 u'<p><b>The tell was a billing symptom, not a security alert.</b> Per the notice, if a user&rsquo;s usage limits '
 u'appeared to refill and then drain <b>while they were not using Claude</b>, that was the likely cause &mdash; which '
 u'is worth dwelling on, because the observable signature of this compromise is a quota that behaves oddly, not a '
 u'failed login or an unfamiliar device.</p>'
 u'<p><b>What Anthropic is doing about it.</b> The company is <b>signing affected users out of Claude</b>, '
 u'<b>removing saved payment methods</b>, and <b>refunding charges it identifies as unauthorised</b>.</p>'
 u'<p><b>The vector is the endpoint, and the company says so plainly.</b> Infostealers of this kind typically arrive '
 u'through downloads or malicious apps and take whatever is stored locally &mdash; <b>browser passwords, login '
 u'cookies and credentials belonging to other applications</b>. Anthropic stresses there is <b>no reason to believe '
 u'the malware is related to Claude, was installed through Claude, or is related to anything the user did with '
 u'Claude</b>. &#9888; <b>That framing matters for triage:</b> a stolen session cookie is not a product '
 u'vulnerability, and a user whose Claude session was taken should assume everything else in the same browser '
 u'profile went with it. <b>No number of affected accounts was stated by any source fetched this run, and none is '
 u'printed here.</b></p></div>'
 u'<div class="card"><div class="tags"><span class="tag tnew">New</span><span class="tag">Phishing</span>'
 u'<span class="tag">AI</span></div>'
 u'<h3>Phishing-as-a-service with a rented AI voice: AnonyMousKIT calls theft victims pretending to be Apple Support and asks for the passcode.</h3>'
 u'<p><b>Researchers disclosed on August 26 a phishing-as-a-service platform called AnonyMousKIT</b> that uses '
 u'<b>rented AI voice agents</b> to place calls to victims of phone theft, <b>posing as Apple Support</b> and '
 u'requesting the device passcode.</p>'
 u'<p><b>Why this one is worth a defender&rsquo;s attention even though it targets consumers.</b> The pattern is the '
 u'same one behind the McKesson item at the top of this page &mdash; a human being talked into handing over a '
 u'credential &mdash; with the labour cost of the call removed. <b>The kit is rented, not built</b>, and the voice is '
 u'a service. <b>No pricing, victim count or operator attribution was stated by any source fetched this run, and none '
 u'is printed.</b></p></div>')
c = rep(c, anchor, newcards, 'cyber new cards')

# 3. tldr
old_tl_start = c.find(u'class="tldr"><b>The Wire</b> <span>')
old_tl_end = c.find(u'</span></div>', old_tl_start)
if old_tl_start<0 or old_tl_end<0:
    fails.append('MISSING: cyber tldr')
else:
    new_tl = (u'class="tldr"><b>The Wire</b> <span>Two federal remediation deadlines expired at midnight and two more '
      u'fall today, and a <b>ninth check of the KEV catalogue at 12:58 PM</b> found no batch newer than August 27 but '
      u'did find a <b>third addition this board has never carried</b> &mdash; the single-vulnerability alert came back '
      u'dated <b>August 21</b>, not August 24, and it is a <b>Zimbra</b> command-injection flaw with no CISA-stated due '
      u'date, so it gets no row; three gaps in nine checks is now the honest measure of how much of the catalogue these '
      u'searches see. The Citrix flaw that ran out yesterday was <b>patched in June as a denial-of-service bug</b> and '
      u'only later understood to allow unauthenticated remote code execution. &#9888; <b>New this run:</b> '
      u'<b>Anthropic is signing Claude users out</b> after infostealer malware on their own machines stole live '
      u'sessions and an attacker used them to drain the accounts&rsquo; usage &mdash; the symptom was a quota that '
      u'refilled and emptied while nobody was working &mdash; and a phishing-as-a-service kit called '
      u'<b>AnonyMousKIT</b> is renting <b>AI voice agents</b> to call phone-theft victims as Apple Support and ask for '
      u'the passcode.')
    c = c[:old_tl_start] + new_tl + c[old_tl_end:]

# 4. sources
src_anchor = u'<footer><div class="srcs"><b>Sources checked this run:</b><br>'
c = rep(c, src_anchor, src_anchor +
 u'<a href="https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-warns-infostealer-malware-is-hijacking-claude-sessions-to-drain-usage/">BleepingComputer &mdash; Anthropic warns infostealer malware is hijacking Claude sessions to drain usage</a><br>'
 u'<a href="https://www.cisa.gov/news-events/alerts/2026/08/21/cisa-adds-one-known-exploited-vulnerability-catalog">CISA &mdash; Adds one known exploited vulnerability to catalog (Aug 21, 2026)</a><br>'
 u'<a href="https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog">CISA &mdash; Adds six known exploited vulnerabilities to catalog (Aug 26, 2026)</a><br>'
 u'<a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA &mdash; Known Exploited Vulnerabilities Catalog</a><br>'
 u'<a href="https://thehackernews.com/2026/08/critical-macos-sharepoint-vcenter-and.html">The Hacker News &mdash; Critical macOS, SharePoint, vCenter and Microsoft IKE flaws under active exploitation</a><br>'
 u'<a href="https://www.bitdefender.com/en-us/blog/businessinsights/bitdefender-threat-debrief-august-2026">Bitdefender &mdash; Threat Debrief, August 2026</a><br>', 'cyber sources')

wr('cyber-briefing.html', c)

# ---------------- WALL STREET ----------------
w=rd('wallstreet-briefing.html')
w = rep(w, u'Sunday morning', u'Sunday midday', 'ws sunday midday', count=99)
w = rep(w, u'a seventeenth verification', u'an eighteenth verification', 'ws counter')
w = rep(w, u'came back a third time', u'came back a fourth time, against a fifth source that put the 10-year at 4.67% and was not adopted', 'ws rates tldr')
w = rep(w, u'a <b>fifth read</b> arrived this run', u'a <b>sixth read</b> arrived this run', 'ws sixth read')

# add a paragraph to the rates/September discussion
sept_anchor = c.find('x')  # noop
if u'no single probability' in w:
    w = rep(w, u'no single probability',
      u'no single probability', 'ws noop', count=1)
wr('wallstreet-briefing.html', w)

if fails:
    print('FAILURES:'); [print(' ',f) for f in fails]; sys.exit(1)
print('OK stage 1')
