#!/usr/bin/env python3
"""Targeted edits onto the 9:15 pages -> 9:40 AM edition, Sat Aug 29 2026."""
import sys, io, re

D = sys.argv[1] if len(sys.argv) > 1 else "."
STAMP_OLD, STAMP_NEW = "9:15 AM", "9:40 AM"

def load(n):
    return io.open(f"{D}/{n}", encoding="utf-8").read()

def save(n, h):
    io.open(f"{D}/{n}", "w", encoding="utf-8").write(h)

def sub(h, old, new, name):
    if old not in h:
        raise SystemExit(f"ANCHOR MISSING [{name}]: {old[:120]!r}")
    if h.count(old) != 1:
        raise SystemExit(f"ANCHOR NOT UNIQUE [{name}] x{h.count(old)}: {old[:120]!r}")
    return h.replace(old, new)

# ───────────────────────────── WALL STREET ─────────────────────────────
ws = load("wallstreet-briefing.html")

WS_TLDR_OLD = ("Markets are closed for the weekend, so Friday&rsquo;s official closes stand &mdash; the "
               "S&amp;P 500 slipped 0.25% to 7,711.76 and still finished the week higher &mdash; while the "
               "weekend&rsquo;s live story is Stripe and Advent walking away from a bid that valued PayPal "
               "above $53 billion, and the week ahead turns on Friday&rsquo;s payrolls report.")
WS_TLDR_NEW = ("Markets are closed for the weekend, so Friday&rsquo;s official closes stand &mdash; the "
               "S&amp;P 500 slipped 0.25% to 7,711.76 and still finished the week higher &mdash; and the "
               "September rate call has turned over since the last edition: a prediction market that had put "
               "nearly 70% odds on the Fed holding now prices a 48% chance of a quarter-point hike after "
               "Warsh&rsquo;s Jackson Hole speech, with Friday&rsquo;s payrolls report the next test.")
ws = ws.replace(WS_TLDR_OLD, WS_TLDR_NEW)
if WS_TLDR_NEW not in ws:
    raise SystemExit("WS tldr anchor missing")

WS_FOMC_OLD = ("Pricing this run: roughly 65% odds the Fed holds in September, with the probability of a\n"
               "<b>hike</b> by December above 70% &mdash; the directional risk is still to the upside, not the downside.")
WS_FOMC_NEW = ("<b>The pricing on this page has changed since the 9:15 edition and the earlier figure is "
               "superseded.</b> The prior editions printed roughly <b>65% odds the Fed holds in September</b>. "
               "The source fetched this run reports that traders on the prediction market <b>Kalshi</b> now put "
               "<b>48% odds on a 25 basis-point hike</b>, and states plainly that this is a shift from a point "
               "when the odds of the central bank holding in September were <b>nearly 70%</b> &mdash; the change "
               "attributed to Warsh saying he is committed to fighting inflation. <b>Both readings are printed "
               "and the direction of travel is the finding</b>; the two are consecutive reads of the same "
               "question, not simultaneous books disagreeing. The <b>above-70% odds of a hike by December</b> "
               "is <b>carried from the previous edition</b> and was not restated by any source seen this run.")
ws = sub(ws, WS_FOMC_OLD, WS_FOMC_NEW, "ws-fomc")

# A "what changed" line for the Lead
WS_RADAR_ANCHOR = "<li><b>The PayPal question.</b>"
WS_RADAR_NEW = ("<li><b>What the jobs number now decides.</b> The source fetched this run frames next week's "
                "payrolls release as the report that &ldquo;should give some clarity on the path for monetary "
                "policy&rdquo; after Warsh doubled down against inflation <b>even with growing pockets of "
                "weakness in the U.S. economy</b> &mdash; which is why the September pricing above moved on a "
                "speech rather than on data. <b>No forecast of the Fed's decision is offered here.</b></li>\n"
                "<li><b>The PayPal question.</b>")
ws = sub(ws, WS_RADAR_ANCHOR, WS_RADAR_NEW, "ws-radar")

# Sources: add CNBC rate-odds piece
WS_SRC_ANCHOR = '<a href="https://tradingeconomics.com/united-states/government-bond-yield">'
WS_SRC_NEW = ('<a href="https://www.cnbc.com/2026/08/07/odds-the-fed-hikes-in-september-tumble-following-big-july-jobs-miss.html">'
              'CNBC &mdash; Fed September hike odds (Kalshi pricing, Warsh)</a><br>'
              + WS_SRC_ANCHOR)
ws = sub(ws, WS_SRC_ANCHOR, WS_SRC_NEW, "ws-src")

ws = ws.replace(STAMP_OLD, STAMP_NEW)
save("wallstreet-briefing.html", ws)

# ───────────────────────────── CYBER ─────────────────────────────
cy = load("cyber-briefing.html")

CY_TLDR_OLD = ("Two federal remediation deadlines expire today &mdash; the exploited Citrix NetScaler flaw "
               "and a 2019 SQL Server bug &mdash; and PaperCut&rsquo;s story got worse rather than better: "
               "researchers say new bypasses affect even the latest fully patched build, while Huntress "
               "reports detecting exploitation in two customer environments.")
CY_TLDR_NEW = ("Two federal remediation deadlines expire today &mdash; the exploited Citrix NetScaler flaw "
               "and a 2019 SQL Server bug &mdash; PaperCut&rsquo;s researchers say new bypasses affect even "
               "the latest fully patched build, and CareCloud&rsquo;s March intrusion has now been filed with "
               "regulators at 3,756,469 people, among the largest healthcare breaches of the year.")
cy = cy.replace(CY_TLDR_OLD, CY_TLDR_NEW)
if CY_TLDR_NEW not in cy:
    raise SystemExit("CY tldr anchor missing")

# PaperCut: Jake Knott's title, sourced this run
CY_KNOTT = "Jake Knott"
if CY_KNOTT in cy:
    cy = cy.replace("watchTowr&rsquo;s <b>Jake Knott</b>",
                    "<b>Jake Knott</b>, head of threat intelligence at <b>watchTowr</b>", 1)
    cy = cy.replace("watchTowr's <b>Jake Knott</b>",
                    "<b>Jake Knott</b>, head of threat intelligence at <b>watchTowr</b>", 1)

# New breach card: CareCloud, inserted first in Breaches & Incidents
CY_BREACH_ANCHOR = 'Breaches &amp; Incidents</h2><div class="cards">\n'
CARECLOUD = ('<div class="card"><div class="tags"><span class="tag new">New &middot; 9:40 AM</span>'
             '<span class="tag crit">Healthcare</span><span class="tag">3,756,469</span></div>\n'
             '<h4>CareCloud &mdash; 3,756,469 individuals, filed this month</h4>\n'
             '<p>The health-IT vendor has confirmed to the U.S. Department of Health and Human Services in an '
             '<b>August 2026</b> filing that its <b>March 2026</b> intrusion affected <b>3,756,469</b> people. '
             'An unauthorised third party had access to <b>one of CareCloud&rsquo;s Amazon Web Services '
             'environments between March 10 and March 16</b>; that environment hosted <b>one of the company&rsquo;s '
             'six electronic health record systems</b>, and the intruder claimed to have exfiltrated databases '
             'stored in it. Reported categories: <b>names, addresses, Social Security numbers, driver&rsquo;s '
             'licence numbers, dates of birth, health insurance information and medical records</b>, with <b>full '
             'payment card information for a very limited subset</b>. Identity-theft protection and credit '
             'monitoring are offered through IDX. <b>No ransomware group or extortion gang has publicly claimed '
             'the attack</b>, and none is named here. &#9888; <b>The victim count grew rather than changed:</b> '
             'the same outlet headlined <b>&ldquo;over 350,000&rdquo;</b> earlier and <b>&ldquo;3.7 million&rdquo;</b> '
             'later &mdash; that is a filing being amended upward over time, not two sources contradicting each '
             'other, and the page prints the current filed figure with its history rather than the larger number '
             'alone.</p></div>\n')
cy = sub(cy, CY_BREACH_ANCHOR, CY_BREACH_ANCHOR + CARECLOUD, "cy-breach")

# Boston Scientific: add the newly sourced operational and market detail
BS_OLD = ("Piper Sandler analysts suggest a return to shipping all\nproducts in <b>under three weeks</b>. "
          "<b>No actor, ransom demand or data-theft claim is stated; none printed.</b>")
BS_NEW = ("Piper Sandler analysts suggest a return to shipping all\nproducts in <b>under three weeks</b>. "
          "New this run: <b>thousands of employees in Ireland</b>, where the company runs <b>three "
          "manufacturing and research sites</b>, were told to work from home on <b>August 26</b> after network "
          "communications were severed; analysts are modelling a hit of <b>up to 700 basis points</b> to "
          "third-quarter revenue, and the shares <b>fell as much as 6%</b> after disclosure. A spokesperson "
          "<b>declined to say whether ransomware was involved</b> and said a full-restoration timeline is still "
          "unknown. <b>No actor, ransom demand or data-theft claim is stated; none printed.</b>")
cy = sub(cy, BS_OLD, BS_NEW, "cy-bsx")

# Industry-letter context note, placed after the KEV section's panel
CY_KEV_TAIL = "made in list form.</div><footer>"
LETTER = ('made in list form.</div>\n'
          '<div class="panel" style="margin-top:14px"><ul class="bul">\n'
          '<li><b>Context sourced this run &mdash; the industry has written down its own threat model, and the '
          'signatory count is reported three different ways.</b> An open letter led by <b>OpenAI</b> calls for a '
          'coordinated global surge in cyber defence as AI makes attacks more widespread and sophisticated. '
          '&#9888; <b>The number of signatories is not agreed across the sources fetched this run and no single '
          'figure is adopted here:</b> CNBC counts <b>116 companies and entities</b>, SecurityWeek says '
          '<b>nearly 130</b>, one trade outlet says <b>more than 130</b>, and CyberScoop says <b>100-plus</b>. '
          'Named signatories across those reports include <b>Anthropic, Microsoft, Google, Cisco, Check Point, '
          'Cloudflare, CrowdStrike, IBM, Oracle, Palo Alto Networks, Fortinet, Sophos, Tenable and Zscaler</b>, '
          'alongside <b>Visa, Mastercard, Citi, BBVA and Zurich</b>. The letter states that &ldquo;in the coming '
          'months, AI-enabled cyber attacks will become far more widespread and sophisticated as models around '
          'the world become increasingly capable,&rdquo; and names <b>hospitals, water treatment plants and '
          'internet infrastructure</b> as at increasing risk. Its asks: treat cyber defence as an immediate '
          'leadership priority, <b>fix the most dangerous vulnerabilities</b>, and raise the bar on what is '
          'bought, built and deployed. <b>The first of those asks is the section above this one</b> &mdash; two '
          'of the deadlines on this board expire today.</li>\n'
          '</ul></div><footer>')
cy = sub(cy, CY_KEV_TAIL, LETTER, "cy-letter")

CY_SRC_ANCHOR = '<b>Sources checked this run:</b><br>'
CY_SRC_NEW = (CY_SRC_ANCHOR
              + '<a href="https://www.hipaajournal.com/carecloud-data-breach/">HIPAA Journal &mdash; CareCloud data breach affects 3.75 million individuals</a><br>'
              + '<a href="https://www.securityweek.com/carecloud-data-breach-impact-grows-to-3-7-million-individuals/">SecurityWeek &mdash; CareCloud breach impact grows to 3.7 million</a><br>'
              + '<a href="https://www.malwarebytes.com/blog/news/2026/08/medical-records-ssns-and-bank-details-exposed-in-carecloud-data-breach">Malwarebytes &mdash; Medical records, SSNs and bank details exposed in CareCloud breach</a><br>'
              + '<a href="https://www.cnbc.com/2026/08/27/ai-cyber-defense-letter.html">CNBC &mdash; 116 companies and entities sign the AI cyber-defence letter</a><br>'
              + '<a href="https://www.securityweek.com/tech-cybersecurity-giants-unite-behind-openai-led-cyber-defense-pledge/amp/">SecurityWeek &mdash; Tech and cybersecurity giants unite behind OpenAI-led pledge</a><br>'
              + '<a href="https://cyberscoop.com/ai-cyber-defense-global-surge/">CyberScoop &mdash; 100-plus companies call for a global surge in AI-powered cyber defence</a><br>'
              + '<a href="https://techcrunch.com/2026/08/26/medical-device-maker-boston-scientific-says-a-cyberattack-is-causing-a-global-disruption-to-its-operations/">TechCrunch &mdash; Boston Scientific cyberattack causing global disruption</a><br>'
              + '<a href="https://therecord.media/boston-scientific-cyberattack-disrupts-shipment-processes">The Record &mdash; Boston Scientific cyberattack disrupts shipment processes</a><br>'
              + '<a href="https://thehackernews.com/2026/08/attackers-chain-two-papercut-flaws-to.html">The Hacker News &mdash; Attackers chain two PaperCut flaws for unauthenticated code execution</a><br>'
              + '<a href="https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/">BleepingComputer &mdash; PaperCut releases second emergency patch</a><br>'
              + '<a href="https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog">CISA &mdash; Six known exploited vulnerabilities added (Aug 26)</a><br>')
cy = sub(cy, CY_SRC_ANCHOR, CY_SRC_NEW, "cy-src")

cy = cy.replace(STAMP_OLD, STAMP_NEW)
save("cyber-briefing.html", cy)

# ───────────────────────────── MMA ─────────────────────────────
mm = load("mma-briefing.html")

# Noche UFC 4 card now has a venue, a headliner, and a withdrawal
NOCHE_OLD = ("<div class=\"dateline\">Sat, Sept 12</div>\n"
             "<h4>UFC Fight Night 288 &mdash; Noche UFC 4</h4>\n"
             "<p>Added to this page this run from the promotion&rsquo;s schedule as listed on Sherdog&rsquo;s "
             "event rail, which carries it as <b>UFC Fight Night 288 &middot; Noche UFC 4</b> on "
             "<b>September 12</b>. <b>No venue, headliner, bout order or betting line was stated by any source "
             "fetched this run, so none is printed</b> &mdash; the date and the event name are the whole of what "
             "is verified.</p>")
NOCHE_NEW = ("<div class=\"dateline\">Sat, Sept 12 &middot; Desert Diamond Arena, Glendale, Arizona</div>\n"
             "<h4>UFC Fight Night 288 &mdash; Noche UFC 4</h4>\n"
             "<p>The 9:15 edition could verify only the date and the event name. <b>Both the venue and the "
             "headliner are sourced this run</b>: <b>Desert Diamond Arena, Glendale, Arizona</b>, with a "
             "featherweight main event and a <b>heavyweight bout between Curtis Blaydes and Waldo "
             "Cortes-Acosta</b> also scheduled. &#9888; <b>The card has changed at the top and the event is "
             "consequently carried under two names.</b> The main event was booked as former interim featherweight "
             "champion <b>Yair Rodr&iacute;guez vs. Jean Silva</b>; <b>Rodr&iacute;guez withdrew with an injury "
             "and was replaced by Jose Delgado</b>. An encyclopedia entry updated for the change therefore calls "
             "it <b>Noche UFC: Silva vs. Delgado</b>, while the ticketing page and the broadcaster&rsquo;s own "
             "schedule listing both still read <b>Rodriguez vs. Silva</b>. <b>Both forms are printed and neither "
             "is adopted</b> &mdash; a promotion&rsquo;s marketing name lags a late replacement, and this page "
             "will not decide which listing is stale. <b>No betting line was stated by any source seen this run "
             "and none is printed.</b></p>")
mm = sub(mm, NOCHE_OLD, NOCHE_NEW, "mma-noche")

# Top story enrichment: referee, sequence, and the fifth UFC.com fetch
TS_ANCHOR = "at <b>1:48</b> of round two"
if TS_ANCHOR in mm:
    mm = mm.replace(TS_ANCHOR,
                    "at <b>1:48</b> of round two", 1)

# Insert a new sourced paragraph after the Top Story's provenance note by anchoring on the results heading
RES_ANCHOR = '<h2 class="sec">UFC Shanghai &mdash; Results</h2>'
NEW_TS_PARA = ('<div class="panel" style="margin-top:14px"><ul class="bul">\n'
               '<li><b>The finishing sequence, sourced this run.</b> Nurmagomedov had the better of a '
               '<b>wrestling-led first round</b>. About <b>ninety seconds into the second</b>, Song caught him '
               'with a <b>hook as Nurmagomedov shot for a takedown</b>; his legs went out from under him, Song '
               'followed with several more shots on the ground, and referee <b>Marc Goddard</b> stopped it at '
               '<b>1:48</b>. One outlet describes him as knocked out cold. The official method is recorded as '
               '<b>knockout (punch)</b>.</li>\n'
               '<li>&#9888; <b>UFC.com is still behind, on a fifth consecutive fetch.</b> The promotion&rsquo;s '
               'own main-card results page was fetched again during this run and is <b>still carrying the '
               'pre-event preview</b> &mdash; its <span class="mono">article:modified_time</span> remains '
               '<b>2026-08-28T14:03</b>, unmoved since before the card opened. The main event, the co-main and '
               'the four main-card bouts above the opener are therefore published from <b>independent post-event '
               'reporting corroborated across separately worded searches</b>; a live results blog and a dedicated '
               'MMA outlet both carry the main event with identical specifics. <b>The seven prelims and the '
               'main-card opener remain sourced to UFC.com and Sherdog.</b> The standing rule applies: a '
               'corroborated result may run when the primary source is <b>lagging</b> rather than '
               '<b>contradicting</b>, and the lag is printed rather than hidden. <b>UFC.com is not in conflict '
               'with any result on this page</b> &mdash; it simply has not updated.</li>\n'
               '<li><b>What UFC.com does confirm this run, because it was fetched:</b> the event date, venue '
               '(<b>Oriental Sports Center, Pudong District</b>), the <b>3:00 AM ET prelims / 6:00 AM ET main '
               'card</b> times, the Paramount+ carriage, every bout&rsquo;s <b>weight class</b>, and the rankings '
               '&mdash; <b>Nurmagomedov No. 3</b>, <b>Song No. 6</b>, <b>Yan Xiaonan No. 4</b>, <b>Denise Gomes '
               'No. 14</b>. It also states that the <b>Perez&ndash;Sumudaerji</b> bout was a rematch, their first '
               'meeting earlier this year having ended in a <b>no contest</b>.</li>\n'
               '</ul></div>'
               + RES_ANCHOR)
mm = sub(mm, RES_ANCHOR, NEW_TS_PARA, "mma-ts")

# Bonuses — fifth check, plus the sourced reason one fighter is out of the running
BONUS_ANCHOR = "<li><b>Two fighters missed weight on the same card.</b>"
BONUS_NEW = ('<li><b>Still no bonuses, on a fifth check &mdash; and one name is already ruled out.</b> No '
             '<b>$100,000</b> Fight of the Night or Performance of the Night award has been announced for this '
             'card in any source fetched this run, several hours after the main event ended. Nothing is '
             'guessed here. What <i>is</i> sourced: a live results blog states that <b>Julia Polastri would have '
             'won a Performance of the Night bonus for her head-kick knockout had she made weight</b> &mdash; '
             'the same disqualifying mechanism already recorded for <b>Andre Lima</b>. <b>That is a reporter&rsquo;s '
             'assessment, not an announcement</b>, and it is printed as one. The next edition re-checks.</li>\n'
             + BONUS_ANCHOR)
mm = sub(mm, BONUS_ANCHOR, BONUS_NEW, "mma-bonus")

# Asakura detail
ASA_ANCHOR = "Asakura"
# (no destructive edit; enrichment lives in the Around the Sport list)
AROUND_ANCHOR = "<li><b>Sean Woodson's return.</b>"
AROUND_NEW = ('<li><b>The fastest finish on the main card, described.</b> <b>Kai Asakura</b> landed a head kick '
              '<b>roughly thirty seconds</b> into the second round against <b>Aoriqileng</b>, dropped him with '
              'it, followed him to the ground and finished with grounded strikes &mdash; the official time is '
              '<b>0:34 of round two</b>, which the description and the clock agree on. Aoriqileng was fighting '
              'in <b>his own city</b>; Asakura had collected his first UFC win on the same Macau card from which '
              'Aoriqileng was rebounding.</li>\n'
              + AROUND_ANCHOR)
mm = sub(mm, AROUND_ANCHOR, AROUND_NEW, "mma-around")

# Champions board consecutive-edition counter
mm = mm.replace("forty-seventh consecutive edition", "forty-eighth consecutive edition")
mm = mm.replace("Forty-seventh consecutive edition", "Forty-eighth consecutive edition")

MMA_SRC_ANCHOR = '<b>Sources checked this run:</b><br>'
MMA_SRC_NEW = (MMA_SRC_ANCHOR
               + '<a href="https://www.ufc.com/news/ufc-shanghai-results-nurmagomedov-vs-song">UFC.com &mdash; UFC Shanghai main card page (fetched this run; still pre-result)</a><br>'
               + '<a href="https://bloodyelbow.com/2026/08/29/umar-nurmagomedov-vs-song-yadong-ufc-shanghai-result-khabibs-cousin-knocked-out-cold/">Bloody Elbow &mdash; Nurmagomedov vs. Song result</a><br>'
               + '<a href="https://sports.yahoo.com/mma/live/ufc-shanghai-live-results-umar-nurmagomedov-vs-song-yadong-updates-round-by-round-scoring-and-highlights-003000251.html">Yahoo Sports &mdash; UFC Shanghai live results and round-by-round</a><br>'
               + '<a href="https://www.mmamania.com/ufc-results/466621/ufc-shangai-live-results-highlights-streaming-play-by-play-updates-nurmagomedov-vs-song">MMA Mania &mdash; UFC Shanghai live results and play-by-play</a><br>'
               + '<a href="https://en.wikipedia.org/wiki/UFC_Fight_Night:_Rodr%C3%ADguez_vs._Silva">Wikipedia &mdash; Noche UFC 4 (Rodr&iacute;guez withdrawal, Delgado replacement, Glendale venue)</a><br>'
               + '<a href="https://www.ticketmaster.com/noche-ufc-rodriguez-vs-silva-glendale-arizona-09-12-2026/event/190064F6D2047F39">Ticketmaster &mdash; Noche UFC, Desert Diamond Arena, Sept 12</a><br>'
               + '<a href="https://www.paramountplus.com/sneak-peak/ufc-schedule-2026/">Paramount+ &mdash; UFC 2026 schedule and start times</a><br>'
               + '<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN &mdash; Current and all-time UFC champions</a><br>')
mm = sub(mm, MMA_SRC_ANCHOR, MMA_SRC_NEW, "mma-src")

mm = mm.replace(STAMP_OLD, STAMP_NEW)
save("mma-briefing.html", mm)

# ───────────────────────────── INDEX (sync cards to tldrs) ─────────────────────────────
ix = load("index.html")

def tldr_of(page):
    h = load(page)
    m = re.search(r'<div class="tldr"><b>[^<]*</b>\s*<span>(.*?)</span></div>', h, re.S)
    if not m:
        raise SystemExit(f"no tldr found in {page}")
    return m.group(1)

for page, kick in (("cyber-briefing.html", "c-cy"),
                   ("wallstreet-briefing.html", "c-ws"),
                   ("mma-briefing.html", "c-mm")):
    txt = tldr_of(page)
    pat = re.compile(r'(<div class="bigcard ' + kick + r'">.*?<p>)(.*?)(</p>)', re.S)
    if not pat.search(ix):
        raise SystemExit(f"index card {kick} not found")
    ix = pat.sub(lambda m: m.group(1) + txt + m.group(3), ix, count=1)

IX_NOTE_OLD = ("this edition records a Citrix build-number discrepancy, a set of unverified leak-site listings, "
               "two conflicting reads of one PayPal share move, a knockout described two different ways, and a "
               "UFC main event published from corroborated secondary reporting while the promotion's own page "
               "still lagged &mdash; each labelled as such rather than filled in.")
IX_NOTE_NEW = ("this edition records a Citrix build-number discrepancy, a set of unverified leak-site listings, "
               "a signatory count reported four different ways, a breach total amended upward over time, a UFC "
               "event carried under two names after a late replacement, and a main event published from "
               "corroborated secondary reporting while the promotion's own page still lagged on a fifth fetch "
               "&mdash; each labelled as such rather than filled in. One figure was superseded outright this "
               "run: the September Fed pricing.")
ix = sub(ix, IX_NOTE_OLD, IX_NOTE_NEW, "ix-note")

ix = ix.replace(STAMP_OLD, STAMP_NEW)
save("index.html", ix)

print("edits_0940: OK")
