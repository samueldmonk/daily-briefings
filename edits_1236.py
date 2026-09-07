import io, re, sys

D = "/sessions/lucid-loving-wright/mnt/outputs/"
PAGES = ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "index.html"]
PREV = "12:16"

def rd(p): return io.open(D + p, encoding="utf-8").read()
def wr(p, s): io.open(D + p, "w", encoding="utf-8").write(s)

def sub1(s, old, new, label):
    n = s.count(old)
    assert n == 1, "EXPECTED 1 OCCURRENCE OF %s, GOT %d" % (label, n)
    return s.replace(old, new)

# ---------------------------------------------------------------- STEP 1
# Demote every inherited "this edition" / "this run" provenance claim to the
# previous edition's stamp, BEFORE any new text is inserted.
demoted = 0
for p in PAGES:
    s = rd(p); before = s
    s = s.replace("this edition", "the %s edition" % PREV)
    s = s.replace("this run", "the %s edition" % PREV)
    s = s.replace("this morning", "earlier this morning")
    # strip any stale New tags carried from the previous edition
    s = re.sub(r'<span class="t new">New</span>', '<span class="t">Carried</span>', s)
    s = re.sub(r'<span class="tag new">[^<]*</span>', '<span class="tag">Carried</span>', s)
    demoted += len(before) != len(s)
    wr(p, s)
print("demotion pass applied to", demoted, "pages")

# ---------------------------------------------------------------- STEP 2
# WALL STREET — the diesel record is STALE and is corrected.
s = rd("wallstreet-briefing.html")

s = sub1(s,
 "<b>the national average price of diesel has hit an all-time high of $5.820 a gallon</b>, one-tenth of a cent above the $5.819 set on 17&nbsp;June 2022 after Russia&rsquo;s invasion of Ukraine, while Brent trades at <b>$97.39, up 1.15%</b>",
 "<b>the national average price of diesel has hit an all-time high of $5.85 a gallon</b> &mdash; corrected upward this edition from the $5.820 print this page had been carrying, which was superseded the following day &mdash; while Brent trades at <b>$97.39, up 1.15%</b>",
 "WS tldr diesel")

old_diesel = "<p><b>The bigger energy story today is not crude at all &mdash; it is the barrel&rsquo;s middle.</b> The U.S. national average diesel price reached <b>$5.820 a gallon</b>, beating the previous record of <b>$5.819</b> set on <b>17 June 2022</b> in the aftermath of Russia&rsquo;s invasion of Ukraine, and 2026 is on track"
new_diesel = ("<p><b>The bigger energy story today is not crude at all &mdash; it is the barrel&rsquo;s middle, and the figure this page "
 "carried for it was three days out of date.</b> <b style=\"color:var(--accent)\">This edition corrects it.</b> The U.S. national average diesel price "
 "reached <b>$5.85 a gallon on Friday 4&nbsp;September</b>, an all-time high. This page had been printing <b>$5.820</b> &mdash; which was "
 "genuinely a record when it was set, on <b>3&nbsp;September</b>, one-tenth of a cent above the <b>$5.819</b> of <b>17 June 2022</b> &mdash; but "
 "the average kept climbing and <b>beat it again the very next day</b>. Both prints are GasBuddy readings of the same daily series, so this is "
 "not two sources disagreeing: it is one series moving, and the later, higher number is the current record. <span class=\"mut\">The correction "
 "has two independent routes. GasBuddy&rsquo;s own 4&nbsp;September release announces the $5.85 record and describes the figure it beat as "
 "&ldquo;$5.82 set in June 2022&rdquo; &mdash; its own 3&nbsp;September high, rounded. Separately, Associated Press copy carried by U.S. News, "
 "the Bangor Daily News and KSAT, and a Transport Topics report, all state <b>$5.85</b> for 4&nbsp;September without reference to GasBuddy&rsquo;s "
 "wire item. The Reuters/GasBuddy $5.820 story is left in the sources below rather than deleted, because a reader may have seen it and is "
 "entitled to know why the number on this page changed. &#9733; <b>A record is a moving statistic, and a page that prints one has to re-ask "
 "whether it is still the record &mdash; not merely whether it was correctly sourced.</b></span> AP adds two figures this page had not carried: "
 "diesel is up <b>58% in twelve months</b>, and roughly <b>10% of the world&rsquo;s seaborne diesel supply</b> transits the Strait of Hormuz &mdash; "
 "which is the mechanism connecting the crude story above to this one. The war it dates the disruption to began on <b>28 February 2026</b>. "
 "2026 is on track")
s = sub1(s, old_diesel, new_diesel, "WS diesel paragraph")

# sources
anchor = '<h2 class="sec">Sources</h2><div class="panel srcs">'
ws_src = "".join([
 '<b>Search return, 12:36 PM ET edition</b> &mdash; GasBuddy newsroom, <a href="https://www.gasbuddy.com/newsroom/pressrelease/2026/09/04/1174">Diesel Prices Reach New All-Time High, Surpassing 2022 Record</a> (4 Sep 2026) &mdash; national average $5.85/gal, above the $5.82 June 2022 record. &nbsp;&middot;&nbsp; ',
 '<b>Search return, 12:36 PM ET edition</b> &mdash; U.S. News / Associated Press, <a href="https://www.usnews.com/news/business/articles/2026-09-04/us-diesel-prices-hit-a-record-high-of-5-85-on-average-as-the-iran-war-disrupts-the-flow-of-fuel">US diesel prices hit a record high of $5.85 on average as the Iran war disrupts the flow of fuel</a> (4 Sep 2026). &nbsp;&middot;&nbsp; ',
 '<b>Search return, 12:36 PM ET edition</b> &mdash; Transport Topics, <a href="https://www.ttnews.com/articles/diesel-hits-record-price">Diesel hits record price at an average of $5.85 a gallon</a>. &nbsp;&middot;&nbsp; ',
 '<b>Search return, 12:36 PM ET edition</b> &mdash; Reuters via TradingView, <a href="https://www.tradingview.com/news/reuters.com,2026:newsml_L6N44V1CG:0-us-diesel-hits-record-5-820-a-gallon-gasbuddy-says/">US diesel hits record $5.820 a gallon, GasBuddy says</a> (3 Sep 2026) &mdash; the superseded print, retained for the correction trail. &nbsp;&middot;&nbsp; ',
 '<b>Search return, 12:36 PM ET edition</b> &mdash; Trading Economics, <a href="https://tradingeconomics.com/commodity/brent-crude-oil">Brent crude oil</a> &mdash; $97.39, +1.15%, 7 September; +11.02% on the month, +47.51% on the year. Re-confirmed unchanged. &nbsp;&middot;&nbsp; ',
])
s = sub1(s, anchor, anchor + ws_src, "WS sources anchor")
wr("wallstreet-briefing.html", s)
print("wallstreet: diesel correction + 5 sources")

# ---------------------------------------------------------------- STEP 3
# MMA — day-of-week error, plus new odds route and UFC 332 detail.
s = rd("mma-briefing.html")

s = sub1(s,
 "and Friday&rsquo;s Paris card leaves Dan Hooker on the longest losing run of his career.",
 "and Saturday&rsquo;s Paris card &mdash; this page&rsquo;s own heading dates it Saturday 5&nbsp;September, and the summary above said Friday until this edition &mdash; leaves Dan Hooker on the longest losing run of his career.",
 "MMA tldr Friday->Saturday")

old_odds = "<b>Odds: Silva &minus;425 / Delgado +355</b>"
assert s.count(old_odds) == 1, "odds line"
s = s.replace(old_odds,
 "<b>Odds: Silva &minus;425 / Delgado +355</b> <span class=\"mut\">(FightOdds.io). A second route this edition, from an aggregate across "
 "<b>20 sportsbooks</b>, has the line at <b>Silva &minus;428 / Delgado +324</b> &mdash; the favourite&rsquo;s side agrees to within three points "
 "and the dog&rsquo;s does not, which is what a spread across twenty books looks like rather than a conflict, so both are printed and neither is "
 "called the line. Silva&rsquo;s implied win probability sits at <b>81%</b>, held between 80 and 82 across the market. Records, newly sourced: "
 "<b>Silva 17&ndash;3</b>, <b>6&ndash;1</b> in the UFC with <b>five finishes</b>; <b>Delgado 12&ndash;2</b>, <b>4&ndash;1</b> with two knockouts. "
 "Both came through Dana White&rsquo;s Contender Series &mdash; Silva in late 2023, Delgado in summer 2024 &mdash; and that is stated by the "
 "returns for these two men specifically, not inferred.</span>")

# UFC 332 detail — append to the Top Story block
old_332 = "The promotion is reported to have said Shevchenko will receive a title shot on her return."
new_332 = (old_332 + " <b>The vacant-title fight itself gained detail this edition.</b> <b>Nat&aacute;lia Silva</b> carries a "
 "<b>14-fight win streak</b> into it, with wins over former champions <b>Rose Namajunas</b>, <b>Alexa Grasso</b> and <b>Jessica Andrade</b> in her "
 "last three outings; <b>Wang Cong</b> has won <b>four straight</b> in the Octagon, most recently beating <b>Tracy Cortez at UFC 329 in July</b>. "
 "The card is the <b>UFC&rsquo;s fifth visit to Salt Lake City</b> and its first since <b>UFC 307 in October 2024</b>, and its main card is the "
 "<b>first for a numbered event to air on CBS</b>. <span class=\"mut\">Corroborated this edition across UFC.com&rsquo;s own announcement, CBS Sports, "
 "FIGHTMAG and the Wikipedia event page; none was fetched first-hand. One framing difference is noted rather than adopted: MMA Mania&rsquo;s headline "
 "says Shevchenko was <i>stripped</i> of the title, while UFC.com, CBS Sports and Yahoo Sports describe her as having <b>vacated</b> it after telling "
 "the promotion she would be unable to compete for at least a year. This page follows the promotion&rsquo;s own wording.</span>")
s = sub1(s, old_332, new_332, "MMA UFC 332 detail")

mma_src = "".join([
 '<b>Search return, 12:36 PM ET edition</b> &mdash; Yahoo Sports, <a href="https://sports.yahoo.com/articles/noche-ufc-4-odds-betting-171123912.html">Noche UFC 4 odds: Betting line opens for Jean Silva vs. Jose Delgado</a> &mdash; Silva &minus;428 / Delgado +324 across 20 sportsbooks; 81% implied; Silva 17&ndash;3 (6&ndash;1 UFC), Delgado 12&ndash;2 (4&ndash;1). &nbsp;&middot;&nbsp; ',
 '<b>Search return, 12:36 PM ET edition</b> &mdash; UFC.com, <a href="https://www.ufc.com/news/undisputed-flyweight-title-grabs-ufc-332-salt-lake-city">Undisputed Flyweight Title Up For Grabs At UFC 332 In Salt Lake City</a>. &nbsp;&middot;&nbsp; ',
 '<b>Search return, 12:36 PM ET edition</b> &mdash; CBS Sports, <a href="https://www.cbssports.com/ufc/news/ufc-332-fight-card-natalia-silva-wang-cong-women-flyweight-title/">UFC 332 fight card: Natalia Silva vs. Wang Cong to main event in Salt Lake City</a> &mdash; Silva&rsquo;s 14-fight streak; Wang Cong four straight, beat Tracy Cortez at UFC 329 in July; first numbered-event main card on CBS. &nbsp;&middot;&nbsp; ',
 '<b>Search return, 12:36 PM ET edition</b> &mdash; UFC.com, <a href="https://www.ufc.com/news/bonus-coverage-ufc-fight-night-paris-2026">Bonus Coverage: UFC Paris</a> &mdash; re-confirmed unchanged. &nbsp;&middot;&nbsp; ',
 '<b>Search return, 12:36 PM ET edition</b> &mdash; ESPN, <a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">Current and all-time UFC champions</a> &mdash; six of six returned belts match the board below (Aspinall, Ulberg, Strickland, Makhachev, Gaethje, Volkanovski). &nbsp;&middot;&nbsp; ',
])
s = sub1(s, anchor, anchor + mma_src, "MMA sources anchor")
wr("mma-briefing.html", s)
print("mma: Friday->Saturday fix + odds route + UFC 332 detail + 5 sources")

# ---------------------------------------------------------------- STEP 4
# CYBER — new disclosure, refreshed ConnectWise status, daily CVE volume.
s = rd("cyber-briefing.html")

old_row = "<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>"
new_row = old_row + ("\n<tr><td><span class=\"t new\">New</span> CVE-2026-84147</td><td class=\"down\"><b>10.0 (Critical)</b></td>"
 "<td>Manacle Technologies <b>Multi-tenant ERP System</b></td>"
 "<td><b>Unauthenticated arbitrary file upload leading to remote code execution (CWE-434).</b> An API endpoint neither authenticates the request "
 "nor validates the type of the uploaded file, so an attacker with nothing but network reach to that endpoint can write executable content into a "
 "web-accessible directory and take the system. Confidentiality, integrity and availability are all rated at the maximum, which is how a score "
 "reaches 10.0. Disclosed alongside <b>CVE-2026-84148</b> (authorisation bypass through a user-controlled key &mdash; an IDOR reaching other "
 "tenants&rsquo; data, CWE-639) and <b>CVE-2026-84149</b> (a publicly exposed <code>.git</code> directory allowing the source tree to be "
 "reconstructed, CWE-527). <span class=\"mut\"><b>Disclosed, not exploited.</b> No public exploitation, no proof-of-concept and <b>no CISA KEV "
 "entry</b> was stated in any return, so no deadline is attached and none should be inferred. Score and CWE taken from the CVE record as published "
 "by IONIX&rsquo;s threat center and OffSeq&rsquo;s Threat Radar, with an Indian CERT-In advisory (CIVN-2026-0430) covering the same three flaws "
 "&mdash; three independent routes to one description. Neither a fixed version nor a vendor bulletin was stated in any return, so none is printed: "
 "the mitigation available today is to keep the ERP&rsquo;s API off the public internet.</span></td></tr>")
s = sub1(s, old_row, new_row, "cyber vuln table header")

# Daily volume note under the KEV section's opening line
old_vol = "<b>The week&rsquo;s volume, newly sourced in the 11:17 edition:</b>"
new_vol = ("<b>Today&rsquo;s volume, newly sourced this edition:</b> <span class=\"mut\">a daily CVE brief dated <b>7 September 2026</b> counts "
 "<b>10 actively exploited vulnerabilities and 20 further critical issues</b> in its 24-hour window, and its ten exploited entries are the same "
 "estate this page already tracks &mdash; SonicWall SMA1000, PaperCut MF/NG, JFrog Artifactory, Kestra, Sangoma Switchvox, and the Python web stack "
 "(Starlette, LiteLLM) &mdash; which is corroboration of this page&rsquo;s KEV list rather than new work for defenders. It also flags three critical "
 "Chrome CVEs scored 9.1&ndash;9.6 plus the one actively exploited flaw already covered below, and a CVSS 9.8 issue in Firefox and Thunderbird. "
 "<b>Those Chrome and Mozilla scores are carried as an aggregator&rsquo;s count and no individual score is asserted from it</b> &mdash; this desk "
 "takes CVSS from the vendor or NVD, and only CVE-2026-84147 was independently confirmed at the record level this edition, which is why it and not "
 "the others appears in the table above.</span> <b>The week&rsquo;s volume, sourced in the 11:17 edition:</b>")
s = sub1(s, old_vol, new_vol, "cyber KEV volume line")

cy_src = "".join([
 '<b>Search return, 12:36 PM ET edition</b> &mdash; IONIX Threat Center, <a href="https://www.ionix.io/threat-center/cve-2026-84147/">CVE-2026-84147 &mdash; Unauthenticated Arbitrary File Upload leading to RCE, Manacle Technologies Multi-tenant ERP</a> &mdash; CVSS 10. &nbsp;&middot;&nbsp; ',
 '<b>Search return, 12:36 PM ET edition</b> &mdash; OffSeq Threat Radar, <a href="https://radar.offseq.com/threat/cve-2026-84147-cwe-434-unrestricted-upload-of-file-with-dangerous-type-in-manacle-technologies-multi-23a2e431cceddaba">CVE-2026-84147 (CWE-434)</a>, with <a href="https://radar.offseq.com/threat/cve-2026-84148-cwe-639-authorization-bypass-through-user-controlled-key-in-manacle-technologies-multi-94fce7c7e97f2e6f">CVE-2026-84148 (CWE-639)</a> and <a href="https://radar.offseq.com/threat/cve-2026-84149-cwe-527-exposure-of-version-control-repository-to-an-unauthorized-control-sphere-in-2b5ea390721f99c7">CVE-2026-84149 (CWE-527)</a>. &nbsp;&middot;&nbsp; ',
 '<b>Search return, 12:36 PM ET edition</b> &mdash; CVE Brief, <a href="https://cvebrief.com/archive/2026/09/07/">CVE Brief &mdash; September 7, 2026</a> &mdash; 10 actively exploited, 20 further critical; counted, not scored. &nbsp;&middot;&nbsp; ',
 '<b>Search return, 12:36 PM ET edition</b> &mdash; BleepingComputer, <a href="https://www.bleepingcomputer.com/news/security/connectwise-warns-of-new-screenconnect-flaw-without-patch/">ConnectWise warns of new ScreenConnect flaw without patch</a> &mdash; CVE and patched release expected within the week, after cloud rollout. &nbsp;&middot;&nbsp; ',
 '<b>Search return, 12:36 PM ET edition</b> &mdash; CISA, <a href="https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog">CISA Adds Seven Known Exploited Vulnerabilities to Catalog</a> (2 Sep 2026) &mdash; the seven re-confirmed unchanged. &nbsp;&middot;&nbsp; ',
])
s = sub1(s, anchor, anchor + cy_src, "cyber sources anchor")

# ConnectWise status refresh in the tldr
s = sub1(s,
 "with <b>no CVE, no score and no patch yet</b>, and the only action available today is switching the <code>TransferFiles</code> role permission off.",
 "with <b>no CVE, no score and no patch yet</b> &mdash; re-checked this edition and still true, with the vendor saying a CVE and a fixed release "
 "are expected <b>within the week</b>, after the cloud rollout &mdash; and the only action available today is switching the <code>TransferFiles</code> "
 "role permission off.",
 "cyber tldr connectwise")
wr("cyber-briefing.html", s)
print("cyber: CVE-2026-84147 row + daily volume + ConnectWise refresh + 5 sources")
print("OK")
