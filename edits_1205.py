#!/usr/bin/env python3
"""Edition edits for the 2026-09-07 ~12:05 ET Midday run (Labor Day, markets closed)."""
import re, sys, io, os

REPO = "/tmp/db_1788797162"
OUT  = "/sessions/vibrant-gracious-wright/mnt/outputs"

def load(n): return io.open(os.path.join(REPO,n),encoding="utf-8").read()
def save(n,h): io.open(os.path.join(OUT,n),"w",encoding="utf-8").write(h)

fails=[]
def rep(h, old, new, label, count=1):
    global fails
    if old not in h:
        fails.append("MISSING ANCHOR: "+label); return h
    n = h.count(old)
    if count and n != count:
        fails.append("ANCHOR COUNT %d != %d: %s" % (n,count,label))
    return h.replace(old,new)

# ============================== PROVENANCE DEMOTION ==============================
# Only the Help Net Security ScreenConnect article was fetched first-hand THIS run.
# Every inherited "fetched directly this run" belongs to the 11:46 edition.
def demote(h):
    h = h.replace("fetched directly this run","fetched directly in the 11:46 edition")
    h = h.replace("fetched this run","fetched in the 11:46 edition")
    h = h.replace("newly sourced this edition","newly sourced in the 11:46 edition")
    h = h.replace("returned this run","returned in the 11:46 edition")
    h = h.replace("a fresh search this run","a fresh search in the 11:46 edition")
    h = h.replace("re-verified this run","re-verified in the 11:46 edition")
    h = h.replace("this run against an independent return","in the 11:46 edition against an independent return")
    h = h.replace("search this run","search in the 11:46 edition")
    h = h.replace("this run again returned","in the 11:46 edition again returned")
    h = h.replace("sourced this run","sourced in the 11:46 edition")
    h = h.replace("re-checked against a fresh CISA-alert search in the 11:46 edition and neither moved",
                  "re-checked against a fresh CISA-alert search this run and neither moved")
    return h

# ================================== CYBER ==================================
c = load("cyber-briefing.html")
c = demote(c)

# --- strip inherited New tag (Dropbox card was new at 11:46, is carried now) ---
c = rep(c, '<div class="tags"><span class="t new">New</span><span class="t hot">Identity</span></div>',
           '<div class="tags"><span class="t hot">Identity</span></div>',
           "cyber: strip Dropbox New tag")

# --- new card: ConnectWise ScreenConnect ---
SC_CARD = '''<div class="card">
<div class="tags"><span class="t new">New</span><span class="t crit">No patch</span><span class="t hot">RMM</span></div>
<h3>ConnectWise says a ScreenConnect file-transfer flaw is real, has no CVE and no fix &mdash; and the only thing defenders can do today is switch a permission off</h3>
<p><b>ConnectWise published an advisory on 3&nbsp;September confirming a security issue in file-transfer behaviour during ScreenConnect Remote Access Support and Access sessions, affecting both its own cloud-hosted deployments and customer on-premises installs.</b> &ldquo;A CVE identifier and an official fix will be issued within the week,&rdquo; the company wrote &mdash; which means that as of today there is <b>no CVE, no severity score, no affected-version list and no patched release</b>, and this page publishes none of those four things because none exists. <span class="mut">Reported by Help Net Security, 7&nbsp;September, quoting the ConnectWise advisory &mdash; <b>the one source fetched first-hand this run</b>.</span></p>
<p><b>The mitigation is a role permission, not an upgrade.</b> ConnectWise directs administrators to <b>Administration &rarr; Security &rarr; Roles</b>, edit each assigned role, review the permissions for each session group, and deselect <code>TransferFiles</code> &mdash; or <code>TransferFilesInSession</code> on legacy versions &mdash; applying the change to every applicable role. In the vendor&rsquo;s words the change &ldquo;does not require a version upgrade and can be applied immediately.&rdquo; <span class="mut">That is the whole of the vendor guidance available today; anything more specific would be invention.</span></p>
<p><b>What gives the advisory its urgency is the Huntress research it follows.</b> Huntress documented rogue ScreenConnect instances landing through social engineering &mdash; the firm calls RMM abuse a top attack vector it has tracked over the past year &mdash; after which the clients spawned repeated Windows Script Host processes to drop <b>four VBScript files named 1.vbs through 4.vbs</b>, and created a Windows registry Run key named <code>WindowsServiceHost</code> pointing at a matching script in the user&rsquo;s AppData directory. The researchers describe a staged chain built to profile hosts and conceal activity, and say the notable part is that <b>modified ScreenConnect clients propagated the VBScript chain to connected endpoints, &ldquo;creating worm-like spread across newly connected systems.&rdquo;</b> Documented payloads covered persistence, further ScreenConnect installations, tunnelling, security-control changes and cryptocurrency mining.</p>
<p><b>Two checks defenders can run now.</b> Huntress advises inspecting ScreenConnect audit logs for <code>RunFiles</code> or <code>RanFiles</code> entries tied to a guest process, and reimaging any machine already showing signs of compromise from known-good media; it adds that admins should apply extra scrutiny to on-premises ScreenConnect installations. <span class="mut">No victim count, no named victims, no attribution and no exploitation-in-the-wild claim for the file-transfer flaw itself: ConnectWise has not said whether it has seen the behaviour abused, and this page does not fill that gap. The Huntress campaign and the ConnectWise advisory are reported <b>adjacently</b> by Help Net Security, which says the advisory <em>follows</em> the research &mdash; a sequence, not a stated causal link, and it is carried here as a sequence.</span></p>
</div>
'''
c = rep(c, '<div class="card">\n<div class="tags"><span class="t hot">Identity</span></div>',
           SC_CARD + '<div class="card">\n<div class="tags"><span class="t hot">Identity</span></div>',
           "cyber: insert ScreenConnect card")

# --- rewrite the ledger paragraph ---
old_ledger_start = '<p class="note" style="margin:-4px 0 12px"><b>Two items are tagged New this edition'
i = c.find(old_ledger_start)
if i < 0:
    fails.append("MISSING ANCHOR: cyber ledger paragraph")
else:
    j = c.find('</p>', i) + 4
    NEW_LEDGER = '''<p class="note" style="margin:-4px 0 12px"><b>Two items are tagged New this edition &mdash; one here and one on the MMA page &mdash; and both tags carried over from 11:46 have been stripped.</b> <span class="mut">Measured against <code>archive/cyber-2026-09-07-1146.html</code> and <code>archive/mma-2026-09-07-1146.html</code> with the corrected check, which counts the markup these pages actually emit (<code>class=&quot;t new&quot;</code>) and asserts <b>placement per page</b> rather than a bare total &mdash; the failure that let a wrong sentence pass a right count last edition. The 11:46 snapshots carried <b>one</b> New tag on this page (the Dropbox account takeovers) and <b>one</b> on the MMA page (Roberto Soldi&#263;&rsquo;s signing); both items are still on their pages and still correct, but they were in the previous archived edition, so their tags are removed here.</span> <b>What is genuinely new this edition: on this page, the ConnectWise ScreenConnect file-transfer advisory immediately below &mdash; and on the MMA page, the Edmonton card on 17&nbsp;October.</b> <span class="mut">Two new items, two tags, one on each of two pages; the count, the placement and this sentence agree, and all three are asserted separately.</span></p>'''
    c = c[:i] + NEW_LEDGER + c[j:]

# --- tldr ---
i = c.find('<div class="tldr">'); j = c.find('</div>', i)+6
if i<0: fails.append("MISSING ANCHOR: cyber tldr")
else:
    c = c[:i] + '''<div class="tldr"><b>The Wire</b> <span>A print server is still today&rsquo;s most urgent box &mdash; PaperCut NG/MF is under hands-on human intrusion and carries the only federal deadline on this page that has not elapsed, 14&nbsp;September &mdash; but new this edition is a flaw with no deadline at all, because it has nothing to attach one to: ConnectWise confirmed on 3&nbsp;September that ScreenConnect file transfers are affected in both cloud and on-premises deployments, with <b>no CVE, no score and no patch yet</b>, and the only action available today is switching the <code>TransferFiles</code> role permission off.</span></div>''' + c[j:]

# --- stat strip: add two ScreenConnect figures at the front ---
c = rep(c, '<div class="stats">\n<div class="stat">',
           '<div class="stats">\n<div class="stat"><div class="n">0</div><div class="l">CVE identifiers, severity scores and patched releases ConnectWise had published for the ScreenConnect file-transfer flaw as of today &mdash; the advisory promises a CVE and a fix &ldquo;within the week&rdquo; &mdash; per Help Net Security, 7 September, fetched first-hand this run</div></div><div class="stat"><div class="n">1.vbs&ndash;4.vbs</div><div class="l">VBScript files dropped by rogue ScreenConnect clients in the Huntress-documented campaign, propagated to connected endpoints for worm-like spread</div></div><div class="stat">',
           "cyber: prepend stats")

# --- sources ---
c = rep(c, '<h2 class="sec">Sources</h2><div class="panel srcs">',
           '<h2 class="sec">Sources</h2><div class="panel srcs"><a href="https://www.helpnetsecurity.com/2026/09/07/connectwise-screenconnect-file-transfer-flaw/">Help Net Security &mdash; attackers spread malware through ScreenConnect file transfers (ConnectWise 3 September advisory, TransferFiles mitigation, Huntress rogue-client campaign; Sinisa Markovic, 7 September 2026 &mdash; <b>fetched directly this run</b>)</a> &nbsp;&middot;&nbsp; <a href="https://www.connectwise.com/company/trust/advisories">ConnectWise &mdash; Trust Center advisories (vendor primary for the 3 September notice, cited by the above)</a> &nbsp;&middot;&nbsp; <a href="https://www.huntress.com/blog/rogue-screenconnect-installations">Huntress &mdash; rogue ScreenConnect installations (the research the advisory follows, cited by the above)</a> &nbsp;&middot;&nbsp; ',
           "cyber: sources")

save("cyber-briefing.html", c)

# ================================ WALL STREET ================================
w = load("wallstreet-briefing.html")
w = demote(w)

# --- tldr ---
i = w.find('<div class="tldr">'); j = w.find('</div>', i)+6
if i<0: fails.append("MISSING ANCHOR: ws tldr")
else:
    w = w[:i] + '''<div class="tldr"><b>The Tape</b> <span>U.S. stock and bond markets are shut all day for Labor Day and reopen at 9:30&nbsp;AM ET Tuesday, so the only markets with news in them today are energy ones &mdash; and both are at extremes: <b>the national average price of diesel has hit an all-time high of $5.820 a gallon</b>, one-tenth of a cent above the $5.819 set on 17&nbsp;June 2022 after Russia&rsquo;s invasion of Ukraine, while Brent trades at <b>$97.39, up 1.15%</b>, as the U.S. and Iran exchange strikes around Hormuz.</span></div>''' + w[j:]

# --- retire the Brent single-level refusal, everywhere ---
if "twenty-sixth" not in w: fails.append("ws: expected 'twenty-sixth' counter not found")

BRENT_PARA = '''<p><b>The Brent single-level refusal is retired this edition, after twenty-six consecutive runs.</b> It was never a judgement that no price existed &mdash; it was a statement that no return this desk had read stated one. A Trading Economics return this run does: <b>Brent crude at $97.39 a barrel on Monday 7 September, up 1.15% on the previous day</b>, which is the same series and the same day as the &ldquo;rose toward $97&rdquo; direction this page has carried since 11:46, now with the print attached. <span class="mut">It is published with the source named rather than as a bare number, and the direction and the level agree, which is the condition this desk set for lifting the refusal. The VIX refusal is untouched and stands at <b>twenty-seventh</b> consecutive edition &mdash; no level has been sourced.</span> The driver is unchanged and re-confirmed this run: the U.S. struck three Iranian oil tankers over the weekend in retaliation for ballistic-missile attacks on U.S. Navy warships; Tehran answered by attacking tankers and other U.S.-linked vessels and threatening a &ldquo;restricted&rdquo; maritime zone beyond the Strait of Hormuz in the coming days. The U.S. Energy Secretary said the naval presence and the blockade on Iranian oil exports will be maintained; Vice President JD Vance said there will be no peace talks until Iran stops attacking ships in Hormuz.</p>
<p><b>The bigger energy story today is not crude at all &mdash; it is the barrel&rsquo;s middle.</b> The U.S. national average diesel price reached <b>$5.820 a gallon</b>, beating the previous record of <b>$5.819</b> set on <b>17 June 2022</b> in the aftermath of Russia&rsquo;s invasion of Ukraine, and 2026 is on track to be the most expensive year for diesel in U.S. history. Two supply shocks are stacked: Middle Eastern refineries damaged during the Iran conflict and disrupted around Hormuz, and Russian refining and exports repeatedly set back by Ukrainian drone attacks. <b>Distillate stocks &mdash; diesel and heating oil &mdash; averaged their lowest August level for the time of year since 1982</b>, per Energy Information Administration data, and the U.S. diesel refining margin, the crack spread, <b>rose above $106 a barrel in early September, a record for that benchmark</b>. <span class="mut">The seasonal risk is stated by the reporting rather than by this desk: farmers and truckers use more diesel in autumn, which raises the stakes of the lowest early-September inventories on record. Reuters via Hydrocarbon Processing and Investing.com, NPR (4 September) and RBN Energy, search returns this run &mdash; none fetched first-hand.</span></p>
'''

anchor = '<h2 class="sec">On the Radar'
if anchor not in w: fails.append("MISSING ANCHOR: ws On the Radar heading")
else:
    k = w.find(anchor); k = w.find('>', w.find('</h2>', k))+1
    w = w[:k] + BRENT_PARA + w[k:]

w = w.replace("the twenty-sixth consecutive run without one","the twenty-seventh consecutive run without one")
w = w.replace("twenty-sixth","twenty-seventh")

# --- week ahead block, appended into On the Radar ---
WEEK = '''<p><b>The week the market reopens into is short, and three dated events carry it.</b> <b>Wednesday 9 September</b> &mdash; Apple&rsquo;s &ldquo;Surprise and shine&rdquo; keynote at Apple Park, 10&nbsp;AM PT / 1&nbsp;PM ET, the first as CEO for <b>John Ternus</b>, who took the job on <b>1 September</b>; the iPhone&nbsp;18 Pro and Pro Max are expected, along with a foldable iPhone. <span class="mut">The foldable&rsquo;s name (&ldquo;iPhone Ultra&rdquo;), its rumoured $2,099&ndash;$2,299 starting price and the Apple Watch Series&nbsp;12 / Ultra&nbsp;4 are all carried by the returns as <b>rumoured</b>, and are printed here with that word attached rather than as announcements.</span> <b>Thursday 10 September</b> &mdash; <b>Oracle</b> reports fiscal Q1 2027 <b>after the close</b>, with a 4:00&nbsp;PM Central call; consensus in the returns is revenue of <b>$19.13&nbsp;billion</b> and EPS of <b>$1.299</b>. <span class="mut">One week-ahead aggregator placed Oracle on <b>Tuesday</b>; Oracle&rsquo;s own earnings-date release says Thursday 10 September, and the company date is followed. The aggregator is noted rather than silently dropped, because a reader may have seen it.</span> <b>Friday 11 September</b> &mdash; <b>August CPI at 8:30&nbsp;AM ET</b>, the print Fed governor Christopher Waller said on 3 September would largely determine his vote.</p>
<p><b>No CPI consensus figure is published here, and the reason is a direct contradiction between two returns this run.</b> A week-ahead aggregator gave headline <b>3.4%</b> and core <b>2.4%</b>; a second return this run gave August CPI at <b>2.9%</b> headline and core at <b>3.1%</b> &mdash; and presented them as <em>reported</em> figures for a release that does not land until Friday, which cannot be right today. Neither pair can be checked against the other and one of them describes a report that has not happened. <span class="mut">Under this desk&rsquo;s rule &mdash; publish a number only when a return states it and nothing contradicts it &mdash; all four figures are withheld. What survives is the date and time, which both returns agree on and which the BLS release schedule fixes. <b>A forecast that two sources cannot agree on is not a forecast, it is a coin flip with a decimal point.</b></span></p>
'''
if anchor in w:
    k = w.find(anchor); k = w.find('>', w.find('</h2>', k))+1
    w = w[:k] + WEEK + w[k:]

# --- Brent row into the rates/commodities table ---
m = re.search(r'<h2 class="sec">Rates, Bonds[^<]*</h2>\s*<table>\s*<tr><th>Instrument</th><th>Level</th><th>Note</th></tr>', w, re.S)
if not m:
    fails.append("MISSING ANCHOR: ws commodities table")
else:
    w = w[:m.end()] + '\n<tr><td>Brent crude</td><td><b>$97.39 / bbl</b></td><td class="mut"><b>Up 1.15% on the day</b>, Monday 7 September, per a Trading Economics return this run &mdash; the print that retires this page&rsquo;s twenty-six-edition refusal to publish a single Brent level. The direction this page has carried since 11:46 (&ldquo;rose toward $97&rdquo;) and this level are the same series on the same day and agree, which is the condition the desk set for lifting the refusal. <b>No Brent settlement is asserted</b> &mdash; there is no U.S. settlement to reference today.</td></tr>' + w[m.end():]

save("wallstreet-briefing.html", w)

# =================================== MMA ===================================
m_ = load("mma-briefing.html")
m_ = demote(m_)

# strip inherited New tag
n_before = m_.count('<span class="t new">New</span>')
m_ = m_.replace('<span class="t new">New</span>','',1)
if n_before != 1: fails.append("mma: expected exactly 1 inherited New tag, found %d" % n_before)

# tldr
i = m_.find('<div class="tldr">'); j = m_.find('</div>', i)+6
if i<0: fails.append("MISSING ANCHOR: mma tldr")
else:
    m_ = m_[:i] + '''<div class="tldr"><b>Tale of the Tape</b> <span>Valentina Shevchenko&rsquo;s vacated women&rsquo;s flyweight title still leads the page &mdash; Natalia Silva meets Wang Cong for the vacant belt at UFC&nbsp;332 on 3&nbsp;October &mdash; while new this edition the October schedule gains a second Canadian date, <b>UFC Fight Night: Buckley vs. Malott at Rogers Place in Edmonton on Saturday 17 October</b>, with Erin Blanchfield vs. Jasmine Jasudavicius in the co-main; and Friday&rsquo;s Paris card leaves Dan Hooker on the longest losing run of his career.</span></div>''' + m_[j:]

# new card in Upcoming Cards
i = m_.find('<h2 class="sec">Fight Week')
if i < 0: i = m_.find('Upcoming Cards')
if i < 0:
    fails.append("MISSING ANCHOR: mma upcoming cards heading")
else:
    k = m_.find('<div class="card"', i)
    EDM = '''<div class="card">
<div class="tags"><span class="t new">New</span></div>
<div class="dt">Sat 17 Oct &middot; Rogers Place, Edmonton, Alberta</div>
<h3>UFC Fight Night: Buckley vs. Malott</h3>
<p><b>A welterweight main event between Joaquin Buckley and Mike Malott headlines the UFC&rsquo;s return to Edmonton</b> &mdash; billed in the returns as UFC Fight Night&nbsp;291. The co-main is a women&rsquo;s flyweight bout between <b>Erin Blanchfield and Jasmine Jasudavicius</b>. Main card at <b>8&nbsp;PM ET</b>, prelims at <b>6&nbsp;PM ET</b>. <span class="mut">Corroborated across the UFC.com event page, the Rogers Place listing, Wikipedia and Tapology in returns this run; none was fetched first-hand and the card says so. <b>No odds are printed &mdash; no return stated one.</b> Descriptors are held to the standing discipline: Buckley and Malott are named as the headliners, nothing more, because nothing more was sourced &mdash; neither is called ranked, a contender or a challenger.</span></p>
</div>
'''
    m_ = m_[:k] + EDM + m_[k:]

# Hooker post-event facts into the Last Event section
i = m_.find('<h2 class="sec">Last Event')
if i < 0:
    fails.append("MISSING ANCHOR: mma last event heading")
else:
    k = m_.find('>', m_.find('</h2>', i))+1
    HOOK = '''<p><b>New this edition, and it is the sourced arithmetic of Friday&rsquo;s main event rather than a fresh result.</b> Post-event facts published after UFC Fight Night&nbsp;287 put <b>Dan Hooker</b> on the longest losing run of his career: <b>three straight defeats</b>, and <b>no win since August 2024</b>. Salahdine Parnasse&rsquo;s finish &mdash; a body kick and a left hand at <b>2:35 of round one</b> &mdash; was the <b>fifth knockout loss</b> of Hooker&rsquo;s career and the <b>third time he has been finished in three consecutive appearances</b>, the other two coming against <b>Benoit Saint-Denis</b> and <b>Arman Tsarukyan</b>. Hooker drops to <b>24&ndash;15</b> and is <b>4&ndash;8 in his last twelve</b>. <span class="mut">Yahoo Sports post-event facts, 6&ndash;7 September, a search return this run &mdash; not fetched first-hand. Hooker is described as a veteran and nothing else; no retirement, release or matchmaking claim is made, because none was stated.</span></p>
'''
    m_ = m_[:k] + HOOK + m_[k:]

# sources
m_ = rep(m_, '<h2 class="sec">Sources</h2><div class="panel srcs">',
             '<h2 class="sec">Sources</h2><div class="panel srcs"><a href="https://www.ufc.com/event/ufc-fight-night-october-17-2026">UFC.com &mdash; UFC Fight Night: Buckley vs Malott, 17 October 2026 (event page; search return this run)</a> &nbsp;&middot;&nbsp; <a href="https://www.rogersplace.com/ufc-fight-night-october-17-2026/">Rogers Place &mdash; UFC Fight Night, 17 October 2026 (venue listing; search return this run)</a> &nbsp;&middot;&nbsp; <a href="https://sports.yahoo.com/articles/ufc-fight-night-287-post-161026018.html">Yahoo Sports &mdash; UFC Fight Night 287 post-event facts: Dan Hooker hits career-worst skid (search return this run)</a> &nbsp;&middot;&nbsp; <a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN &mdash; current and all-time UFC champions (champions board cross-check, re-run this run)</a> &nbsp;&middot;&nbsp; ',
             "mma: sources")

save("mma-briefing.html", m_)

# ================================== INDEX ==================================
x = load("index.html")
x = demote(x)

CARDS = {
 "c-sec": ("A ScreenConnect flaw with no CVE and no patch &mdash; and a print server that still owns the only live federal deadline",
   "ConnectWise confirmed on 3 September that file transfers in ScreenConnect Remote Access sessions are affected in both cloud and on-premises deployments, with no CVE, no severity score and no patched release yet &mdash; the only action available today is deselecting the <code>TransferFiles</code> role permission &mdash; while PaperCut NG/MF remains the page&rsquo;s Patch Priority on a 14 September federal deadline."),
 "c-mkt": ("Diesel sets an all-time high on a day nothing trades",
   "U.S. stock and bond markets are shut for Labor Day and reopen at 9:30 AM ET Tuesday, leaving energy as the only market with news in it: the national average diesel price hit a record $5.820 a gallon, one-tenth of a cent above the June 2022 peak, while Brent traded at $97.39, up 1.15%, on renewed U.S.&ndash;Iran strikes around Hormuz."),
 "c-mma": ("October gains a second Canadian date, and Dan Hooker gains a career-worst skid",
   "UFC Fight Night: Buckley vs. Malott lands at Rogers Place in Edmonton on Saturday 17 October, with Erin Blanchfield vs. Jasmine Jasudavicius in the co-main; Valentina Shevchenko&rsquo;s vacated flyweight belt still leads the briefing, and Friday&rsquo;s Paris card left Hooker on three straight losses, his longest run of defeats."),
}

for cls,(h3,p) in CARDS.items():
    m2 = re.search(r'(<div class="card[^"]*\b'+cls+r'\b[^"]*">)(.*?)(?=<a class="read")', x, re.S)
    if not m2:
        fails.append("MISSING ANCHOR: index card "+cls); continue
    block = m2.group(2)
    if "<h3" not in block or "<p" not in block:
        fails.append("EMPTY BLOCK: index card "+cls+" (no h3/p inside)"); continue
    nb = re.sub(r'(<h3[^>]*>).*?(</h3>)', lambda mm: mm.group(1)+h3+mm.group(2), block, count=1, flags=re.S)
    nb = re.sub(r'(<p[^>]*>).*?(</p>)', lambda mm: mm.group(1)+p+mm.group(2), nb, count=1, flags=re.S)
    if nb == block:
        fails.append("NO-OP REPLACE: index card "+cls); continue
    x = x[:m2.start(2)] + nb + x[m2.end(2):]

save("index.html", x)

print("FAILURES:" if fails else "ALL EDITS APPLIED CLEANLY")
for f in fails: print("  -", f)
sys.exit(1 if fails else 0)
