#!/usr/bin/env python3
"""Edition edits for Sat 2026-08-22 ~6:35pm ET (Afternoon Edition, 4th run of Saturday)."""
import io, os, sys

SRC = "/tmp/db_1787438152"
OUT = "/sessions/epic-cool-pasteur/mnt/outputs"
FILES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]

fails = []

def load(p):
    with io.open(os.path.join(OUT, p), encoding="utf-8") as f:
        return f.read()

def save(p, s):
    with io.open(os.path.join(OUT, p), "w", encoding="utf-8") as f:
        f.write(s)

def rep(s, old, new, tag):
    if old not in s:
        fails.append("MISSING: " + tag)
        return s
    if s.count(old) != 1:
        fails.append("NOT-UNIQUE(%d): %s" % (s.count(old), tag))
        return s
    return s.replace(old, new)

# ---------------------------------------------------------------- copy sources
for f in FILES:
    with io.open(os.path.join(SRC, f), encoding="utf-8") as fh:
        save(f, fh.read())

# =============================================================== MMA
m = load("mma-briefing.html")

m = rep(m,
  '<div class="tldr"><b>Tale of the Tape</b> <span>UFC Sacramento\'s prelims are roughly an hour deep at the Golden 1 Center and the main card is still to come at 8 PM ET, but every primary source checked for this edition was still showing blank result fields, so no winners are published here.</span></div>',
  '<div class="tldr"><b>Tale of the Tape</b> <span>The first two UFC Sacramento prelim results are now confirmed &mdash; Shanelle Dyer stopped Elise Reed in the third round and Jackson McVey dropped Wes Schultz with a knee to the body in the first &mdash; while the rest of the card, including the 8 PM ET main event, is still unresolved.</span></div>',
  "mma tldr")

m = rep(m,
  '<h2 style="margin:0 0 10px;font-size:21px;line-height:1.3">Hernandez vs. Rodrigues headlines a live card in Sacramento — and no results exist yet</h2>',
  '<h2 style="margin:0 0 10px;font-size:21px;line-height:1.3">Hernandez vs. Rodrigues headlines a live card in Sacramento &mdash; and the first results are in</h2>',
  "mma headline")

OLD_NOTE = '<p class="note"><b>No results are published on this page.</b> Re-checked for this edition with the prelims about an hour old: UFC.com has now posted its dedicated <i>UFC Sacramento Prelim Results</i> page, but the page still carries only fight previews with no winners, methods or times; Sherdog\'s play-by-play shows an empty "The Official Result" heading under all thirteen bouts; and FightBook MMA reads "Result: TBD" on every line. Aggregated search summaries continue to assert prelim winners, and one of them mis-dated the event by a day, so none is treated as reliable. Winners will be published in the next edition once a primary source posts them.</p>'

NEW_NOTE = '''<div style="margin-top:14px;border-top:1px solid #322020;padding-top:12px">
<div style="font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#e84545;margin-bottom:8px">Confirmed so far tonight</div>
<div class="panel" style="padding:6px 8px;background:#150f0f">
<table>
<tr><th>Result</th><th>Bout</th><th>Method</th></tr>
<tr><td><span class="win">Jackson McVey</span></td><td>McVey def. Wes Schultz (185 lbs)</td><td>TKO, knee to the body &mdash; R1, 4:13</td></tr>
<tr><td><span class="win">Shanelle Dyer</span></td><td>Dyer def. Elise Reed (115 lbs)</td><td>Standing TKO, punches &mdash; R3, 1:42</td></tr>
</table>
</div>
<p class="note" style="margin-top:10px"><b>Only these two bouts are published.</b> They come from the MMA Mania / SB Nation live blog fetched for this edition, whose page body carries an explicit &ldquo;Official Decision&rdquo; line for each. Dyer out-landed Reed <b>116 significant strikes to 42</b> and is now <b>2-0</b> in the UFC. Every other bout on the 13-fight card is still listed without a result: UFC.com&rsquo;s <i>Prelim Results</i> page carries only previews, FightBook MMA reads &ldquo;Result: TBD&rdquo; on all thirteen lines, FIGHTMAG&rsquo;s live blog has posted nothing past media day, and Sports Illustrated&rsquo;s live page has no results either. Search summaries asserting further winners are not corroborated by any page fetched this run and are not published.</p>
<p class="note" style="margin-top:8px">Start times follow UFC.com and Sports Illustrated (prelims 5:00 PM ET, main card 8:00 PM ET). MMA Mania&rsquo;s own preamble lists the main card at 7 PM ET; that figure is not used.</p>
</div>'''

m = rep(m, OLD_NOTE, NEW_NOTE, "mma results note")

# footer source
m = rep(m,
  '<div class="lab">Sources</div>',
  '<div class="lab">Sources</div>',
  "mma sources lab")

save("mma-briefing.html", m)

# =============================================================== CYBER
c = load("cyber-briefing.html")

c = rep(c,
  'and 7 entries in CISA&#39;s Known Exploited Vulnerabilities catalog are already past their deadline.'
    if 'and 7 entries in CISA&#39;s' in c else
  "and 7 entries in CISA's Known Exploited Vulnerabilities catalog are already past their deadline.",
  "and 8 entries in CISA's Known Exploited Vulnerabilities catalog are already past their deadline — the oldest being an actively exploited flaw in the Ray AI computing framework, due two days ago.",
  "cyber tldr")

c = rep(c,
  '<span style="font-size:14.3px;color:#c6d2dd">7 KEV entries sit past their federal due date, a GitLab flaw is under active exploitation days after disclosure, and five freshly patched Cisco vulnerabilities carry the maximum CVSS 10.0 score.</span>',
  '<span style="font-size:14.3px;color:#c6d2dd">8 KEV entries sit past their federal due date, a GitLab flaw is under active exploitation days after disclosure, and five freshly patched Cisco vulnerabilities carry the maximum CVSS 10.0 score.</span>',
  "cyber banner")

c = rep(c,
  '<div class="stat"><div class="n">7</div><div class="l">KEV entries past due</div></div>',
  '<div class="stat"><div class="n">8</div><div class="l">KEV entries past due</div></div>',
  "cyber stat")

# Patch Priority: add Ray sentence
c = rep(c,
  'It is one of four August 18 additions that all came due yesterday. The nearest deadline still ahead is <b>CVE-2026-72529</b> in <b>TrueConf Server</b> &mdash; <b>CVSS 9.3</b>, due <b>August 23, tomorrow</b>.'
    if 'came due yesterday. The nearest deadline still ahead is <b>CVE-2026-72529</b> in <b>TrueConf Server</b> &mdash;' in c else
  'It is one of four August 18 additions that all came due yesterday. The nearest deadline still ahead is <b>CVE-2026-72529</b> in <b>TrueConf Server</b> — <b>CVSS 9.3</b>, due <b>August 23, tomorrow</b>.',
  'It is one of four August 18 additions that all came due yesterday. The <b>longest-overdue</b> entry is now <b>CVE-2025-62593</b> in the <b>Ray</b> distributed-computing framework &mdash; CVSS 9.4, added August 17, due <b>August 20</b> and <b>2 days past due</b>. The nearest deadline still ahead is <b>CVE-2026-72529</b> in <b>TrueConf Server</b> &mdash; <b>CVSS 9.3</b>, due <b>August 23, tomorrow</b>.',
  "cyber patch priority")

# CVE table: insert Ray row before the vCenter row
c = rep(c,
  '<tr><td><b>CVE-2026-59310</b></td><td>9.8</td><td>Broadcom VMware vCenter</td>',
  '<tr><td><b>CVE-2025-62593</b></td><td>9.4</td><td>Ray (all versions before 2.52.0)</td><td><span class="down">Exploited in the wild</span> per CISA. Code injection reachable from a browser via DNS rebinding on unauthenticated endpoints such as /api/jobs; the RondoDox DDoS botnet adopted it. Fixed in 2.52.0. KEV deadline was <b>Aug 20</b> &mdash; passed.</td></tr>\n<tr><td><b>CVE-2026-59310</b></td><td>9.8</td><td>Broadcom VMware vCenter</td>',
  "cyber cve table ray row")

# KEV list: insert Ray row after the four Aug-18 rows
c = rep(c,
  '<li><b>CVE-2026-20349</b> — Cisco Secure Firewall ASA / FTD — heap inspection. Added Aug 11 <span class="kev-crit">(remediation window elapsed — past due)</span></li>'
    if '<li><b>CVE-2026-20349</b> — Cisco Secure Firewall ASA / FTD' in c else
  '<li><b>CVE-2026-20349</b> — Cisco Secure Firewall ASA / FTD — heap inspection. Added Aug 11 <span class="kev-crit">(remediation window elapsed — past due)</span></li>',
  '<li><b>CVE-2025-62593</b> &mdash; Ray distributed-computing framework &mdash; code injection, CVSS 9.4. Added Aug 17, due <b>2026-08-20</b> <span class="kev-crit">(2 days PAST DUE)</span></li>\n<li><b>CVE-2026-20349</b> &mdash; Cisco Secure Firewall ASA / FTD &mdash; heap inspection. Added Aug 11 <span class="kev-crit">(remediation window elapsed &mdash; past due)</span></li>',
  "cyber kev ray row")

c = rep(c,
  'Of the 10 entries tracked here, <b>7 are past due</b>.',
  'Of the 11 entries tracked here, <b>8 are past due</b>.',
  "cyber kev note count")

# Breach card: Baxter, inserted ahead of the US Bank card
c = rep(c,
  '<div class="cards">\n<div class="card">\n<div class="tags"><span class="tag new">New</span><span class="tag hot">Extortion</span><span class="tag">Financial services</span></div>',
  '''<div class="cards">
<div class="card">
<div class="tags"><span class="tag new">New</span><span class="tag hot">Extortion</span><span class="tag">Healthcare</span></div>
<h3>ShinyHunters claims 7.1 million Baxter International records</h3>
<p>The extortion crew <b>ShinyHunters</b> claims on its dark-web leak site to have published <b>7.1 million Salesforce records</b> taken from medical-products maker <b>Baxter International</b>, according to Information Security Media Group&rsquo;s GovInfoSecurity. It is the group&rsquo;s latest move against the healthcare sector after earlier claims involving DentaQuest.</p>
<p class="note">This is an <b>unverified attacker claim</b>. No Baxter statement confirming or denying a breach, and no regulatory filing, was found in the sources fetched for this edition, so no data categories, affected-individual count or incident date are asserted here beyond the number the group itself published.</p>
</div>
<div class="card">
<div class="tags"><span class="tag hot">Extortion</span><span class="tag">Financial services</span></div>''',
  "cyber baxter card")

save("cyber-briefing.html", c)

# =============================================================== WALL STREET
w = load("wallstreet-briefing.html")

w = rep(w,
  '<tr><td><b>US 10-year Treasury yield</b></td><td>&asymp; 4.7%</td><td>Per Trading Economics. Snapped back to earlier highs after a brief post-Bessent decline.</td></tr>'
    if '&asymp; 4.7%' in w else
  '<tr><td><b>US 10-year Treasury yield</b></td><td>≈ 4.7%</td><td>Per Trading Economics. Snapped back to earlier highs after a brief post-Bessent decline.</td></tr>',
  '<tr><td><b>US 10-year Treasury yield</b></td><td>4.737%</td><td>Friday&rsquo;s finish per CNBC&rsquo;s Aug 21 market report. Snapped back to earlier highs after a brief post-Bessent decline. Trading Economics&rsquo; rounded read of &asymp;4.7% agrees.</td></tr>',
  "ws 10yr")

w = rep(w,
  '<tr><td><b>US 30-year Treasury yield</b></td><td>&asymp; 5.25%</td><td>Per Trading Economics. Long-dated yields rebounded Friday on doubts about the debt-reduction plan.</td></tr>'
    if '&asymp; 5.25%' in w else
  '<tr><td><b>US 30-year Treasury yield</b></td><td>≈ 5.25%</td><td>Per Trading Economics. Long-dated yields rebounded Friday on doubts about the debt-reduction plan.</td></tr>',
  '<tr><td><b>US 30-year Treasury yield</b></td><td>5.276%</td><td>Friday&rsquo;s finish per CNBC&rsquo;s Aug 21 market report. Long-dated yields rebounded Friday on doubts about the debt-reduction plan; Trading Economics&rsquo; &asymp;5.25% agrees.</td></tr>',
  "ws 30yr")

save("wallstreet-briefing.html", w)

# =============================================================== INDEX
i = load("index.html")

i = rep(i,
  '<h2>A named group is behind tomorrow&#39;s federal patch deadline</h2>'
    if '<h2>A named group is behind tomorrow&#39;s federal patch deadline</h2>' in i else
  "<h2>A named group is behind tomorrow's federal patch deadline</h2>",
  '<h2>Eight federal patch deadlines have already passed</h2>',
  "index cyber h2")

i = rep(i,
  '<p>The TrueConf Server flaw federal agencies must fix by tomorrow now carries a CVSS of 9.3 and an attacker — the Head Mare group, which used it to swap client downloads for malware. A GitLab flaw rated 9.4 remains under active exploitation, and seven KEV entries are already past due.</p>',
  '<p>Eight entries in CISA&rsquo;s Known Exploited Vulnerabilities catalog now sit past their federal due date, the oldest an actively exploited flaw in the Ray AI computing framework that came due two days ago. A GitLab flaw rated 9.4 remains under exploitation, and the TrueConf Server bug is due tomorrow.</p>',
  "index cyber p")

i = rep(i,
  '<h2>Sacramento is live, and the scorecards are blank</h2>',
  '<h2>The first Sacramento results are in</h2>',
  "index mma h2")

i = rep(i,
  '<p>UFC Sacramento&#39;s prelims are roughly an hour deep at the Golden 1 Center and the main card is still to come at 8 PM ET, but every primary source checked for this edition was still showing blank result fields, so no winners are published.</p>'
    if 'UFC Sacramento&#39;s prelims are roughly an hour deep' in i else
  "<p>UFC Sacramento's prelims are roughly an hour deep at the Golden 1 Center and the main card is still to come at 8 PM ET, but every primary source checked for this edition was still showing blank result fields, so no winners are published.</p>",
  '<p>Two UFC Sacramento prelim results are now confirmed &mdash; Shanelle Dyer stopped Elise Reed in the third and Jackson McVey folded Wes Schultz with a first-round knee to the body. The rest of the 13-fight card, including the 8 PM ET main event, is still unresolved.</p>',
  "index mma p")

save("index.html", i)

if fails:
    print("FAILURES:")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("all edits applied cleanly")
