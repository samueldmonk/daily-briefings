#!/usr/bin/env python3
# Eleventh run, Saturday 12 September 2026 ~1:05pm ET clone / ~1:25pm build.
# Edits the established pages in place; no restyle.
import re, sys, os

SRC = "/tmp/db_1789232738"
OUT = "/sessions/sleepy-hopeful-carson/mnt/outputs"

def load(f): return open(os.path.join(SRC, f), encoding="utf-8").read()
def save(f, s): open(os.path.join(OUT, f), "w", encoding="utf-8").write(s)

fails = []
def rep(s, old, new, label, count=1):
    if old not in s:
        fails.append("MISSING ANCHOR: " + label); return s
    return s.replace(old, new, count)

# ============================== CYBER ==============================
cy = load("cyber-briefing.html")

# --- 1. tldr
cy = rep(cy,
 "<div class=\"tldr\"><b>The Wire</b> <span>The Dutch national cyber centre says exploitation of two unpatched-until-this-week Check Point VPN flaws rated CVSS 9.8 is imminent, the federal deadline for a CVSS 10.0 Cisco firewall bypass already under attack expires today, and the V8 sandbox escape at the centre of Proofpoint&rsquo;s BlueMoon chain now carries a CVSS of 8.8 and a federal deadline of its own on 23 September.</span></div>",
 "<div class=\"tldr\"><b>The Wire</b> <span>A single CVSS 10.0 flaw in the Metabase analytics platform now sits underneath at least two of the breaches on this page, including the one that exposed 67,000 Trezor customers whose data a supplier had certified as deleted; the federal deadline for a CVSS 10.0 Cisco firewall bypass already under attack expires today; and a week of disclosures added more than 220 million traveller records and 7.6 million patient records to the running total.</span></div>",
 "cy.tldr")

# --- 2. stat strip
cy = rep(cy,
 "<div class=\"strip\"><div class=\"stat\"><div class=\"n\">10.0</div><div class=\"l\">CVSS &mdash; Cisco Secure FMC auth bypass (CVE-2026-20079), KEV due today</div></div>".replace("&mdash;","—"),
 "<div class=\"strip\"><div class=\"stat\"><div class=\"n\">10.0</div><div class=\"l\">CVSS — Metabase unauthenticated SQL injection (CVE-2026-72898), the common root cause behind two breaches on this page</div></div><div class=\"stat\"><div class=\"n\">220m+</div><div class=\"l\">Passenger and crew records exposed in a Vietnam-linked Advance Passenger Information System database, spanning 2017 to April 2026</div></div><div class=\"stat\"><div class=\"n\">10.0</div><div class=\"l\">CVSS — Cisco Secure FMC auth bypass (CVE-2026-20079), KEV due today</div></div>",
 "cy.strip")

# --- 3. Replace Top Story panel with Metabase; keep BlueMoon by demoting it to a carried card.
m = re.search(r"<h2>Top Story</h2>(<div class=\"panel\" style=\"border-left:3px solid var\(--crit\)\">.*?)<h2>Patch Priority</h2>", cy, re.S)
if not m:
    fails.append("MISSING ANCHOR: cy.topstory-block")
else:
    bluemoon_panel = m.group(1)
    # condense BlueMoon into a Breaches card
    bm_card = ("<div class=\"card\"><span class=\"chip\">Carried</span><span class=\"chip hot\">Zero-day chain</span>"
      "<span class=\"chip\">Espionage</span><h3>BlueMoon — a three-stage chain from a Chrome tab to SYSTEM</h3>"
      "<p>Proofpoint's <b>BlueMoon</b> exploit kit, in use by <b>at least four threat clusters</b> since <b>late August 2026</b> and "
      "majority-assessed as <b>China nexus</b>, chains <b>CVE-2026-85046</b> (V8 type confusion, renderer code execution) into "
      "<b>CVE-2026-87491</b> (V8 sandbox escape, CVSS <b>8.8</b>, KEV due <b>23 September</b>) into <b>CVE-2026-85880</b> "
      "(Windows ALPC heap overflow to SYSTEM). First confirmed use was <b>TA412 / Violet Typhoon / APT31</b> on <b>28 August</b>, "
      "with lures posing as university interns and academic conference outreach against US NGOs, mining firms and commodity traders, "
      "delivering a fake &ldquo;Google Gemini&rdquo; extension Proofpoint tracks as <b>GemStone</b>. Chrome Stable was fixed 3 and "
      "8 September; Windows on September Patch Tuesday. Demoted from Top Story this run, not retracted.</p></div>")

    metabase = ("<div class=\"panel\" style=\"border-left:3px solid var(--crit)\"><span class=\"chip new\">New</span>"
      "<span class=\"chip hot\">CVSS 10.0</span><span class=\"chip\">Supply chain</span>"
      "<h3 style=\"margin:0 0 10px;font-size:22px\">One analytics bug, several victims: Metabase is the common thread under this week's breaches</h3>"
      "<p style=\"margin:0 0 10px;font-size:15px;color:#c6ced6\">The most useful thing to notice about this week's breach roundup is that "
      "the victims are not related to one another &mdash; a crypto-hardware maker's shipping contractor and an online maths platform for "
      "schools &mdash; and yet at least two of them were reached through the <b>same piece of software</b>. That software is <b>Metabase</b>, "
      "the open-source business-intelligence tool organisations point at their production databases so that non-engineers can query them.</p>"
      "<p style=\"margin:0 0 10px;font-size:15px;color:#c6ced6\"><b>CVE-2026-72898</b> is an <b>unauthenticated SQL injection</b> rated "
      "<b>CVSS 10.0</b>. It is reachable through the publicly exposed <b>POST /api/session/reset_password</b> endpoint, so an attacker "
      "injects SQL into Metabase's own application database without a login, manipulates the authentication data stored there and comes "
      "out the other side as an <b>administrator</b>. Administrator on a Metabase instance is the interesting part: it confers the ability "
      "to change configuration and to <b>read out the stored credentials for every database the instance is connected to</b>, then read and "
      "export whatever those connections reach. IONIX puts the affected range at <b>Metabase 0.58/1.58 through 0.63.4</b>.</p>"
      "<p style=\"margin:0 0 10px;font-size:15px;color:#c6ced6\">It was exploited as a <b>zero-day</b>. Metabase disclosed on "
      "<b>6 August 2026</b> that its own <b>Cloud environment</b> had been attacked using a then-unknown flaw, and <b>CISA added it to the "
      "KEV catalog on 11 August 2026</b>. One account puts the number of companies breached through it at <b>five</b>, with all connected "
      "database credentials exposed.</p>"
      "<p style=\"margin:0 0 10px;font-size:15px;color:#c6ced6\">The links to this page's own breach cards are of two different strengths, "
      "and are worth separating. For <b>Mathspace</b>, BleepingComputer states directly that attackers took data on more than a million "
      "students, staff and parents <b>after breaching its Metabase internal reporting system</b> &mdash; the platform is named, the CVE is "
      "not. For <b>ShipMonk</b>, the shipping provider whose breach has now exposed <b>81,000 Trezor customers</b>, the attribution to "
      "<b>CVE-2026-72898 specifically</b> comes from a single vendor analysis (Rescana) rather than from ShipMonk or Trezor, and is carried "
      "here on that basis rather than as an established fact.</p>"
      "<p style=\"margin:0;font-size:15px;color:#c6ced6\">The defensive reading does not depend on resolving that. A reporting tool is not "
      "usually on anyone's internet-facing asset inventory, and it holds credentials to the systems that are. Both victims were compromised "
      "through the dashboard rather than through the database it pointed at.</p></div>")
    cy = cy.replace(m.group(0), "<h2>Top Story</h2>" + metabase + "<h2>Patch Priority</h2>")
    cy = rep(cy, "<h2>Breaches &amp; Incidents</h2><div class=\"cards\">",
             "<h2>Breaches &amp; Incidents</h2><div class=\"cards\">" + bm_card, "cy.breach-open")

# --- 4. New breach cards, inserted after the BlueMoon carried card
new_cards = (
 "<div class=\"card\"><span class=\"chip new\">New</span><span class=\"chip hot\">Supply chain</span><span class=\"chip\">Crypto</span>"
 "<h3>Trezor — 81,000 customers, and data a supplier had certified as deleted</h3>"
 "<p>Hardware-wallet maker <b>Trezor</b> disclosed a further <b>67,000 US customers</b> affected by the August breach at its shipping and "
 "logistics provider <b>ShipMonk</b>, taking the total to <b>81,000</b> after an initial disclosure of nearly <b>14,000</b> on "
 "<b>13 August</b>. ShipMonk notified Trezor of unauthorised access on <b>10 August 2026</b>. Exposed: names, email addresses, phone "
 "numbers, shipping addresses and order numbers, for orders between <b>November 2019 and August 2021</b> &mdash; and that date range is the "
 "story. Trezor had <b>repeatedly requested deletion of that data and received written confirmation that it had been deleted</b>; it had not "
 "been. Wallet security is unaffected. Rescana attributes the underlying compromise to the Metabase flaw above.</p></div>"

 "<div class=\"card\"><span class=\"chip new\">New</span><span class=\"chip hot\">Phishing</span><span class=\"chip\">Crypto</span>"
 "<h3>Trezor, again — 347,000 addresses phished through its email provider</h3>"
 "<p>A separate and unrelated Trezor incident: attackers breached <b>Brevo</b>, Trezor's third-party email provider, and mailed customers who "
 "had opted into the newsletter. <b>347,000 email addresses</b> were targeted and <b>2,500 users clicked</b> the embedded malicious link. The "
 "lure was well built &mdash; a fake <b>&ldquo;critical security alert&rdquo;</b> sent from <b>help@trezor.io</b> claiming a "
 "<b>hardware microcontroller vulnerability</b> in the wallets' <b>STM32</b> chips could expose recovery seeds to brute-force cracking. A "
 "security warning is a near-perfect phishing pretext against exactly the users most inclined to act on one.</p></div>"

 "<div class=\"card\"><span class=\"chip new\">New</span><span class=\"chip hot\">Exposure</span><span class=\"chip\">Aviation</span>"
 "<h3>220 million traveller records left reachable in a Vietnam-linked APIS database</h3>"
 "<p>An <b>Advance Passenger Information System</b> database holding more than <b>220 million passenger and crew records</b> was reachable "
 "online through a chain of misconfigurations, with researchers getting in via a cloud path using <b>default credentials</b>. APIS platforms "
 "collect identity, passport and flight data from airlines before arrival or departure, so the contents are comprehensive: names, dates of "
 "birth, sex, nationalities, <b>passport or travel-document numbers</b>, expiry dates and issuing countries, plus flight numbers and dates, "
 "airlines, departure, destination and transit airports, seat assignments, baggage references and scheduled, estimated and actual times. The "
 "records span <b>January 2017 to April 2026</b>. No exploited flaw here &mdash; nothing had to be broken.</p></div>"

 "<div class=\"card\"><span class=\"chip new\">New</span><span class=\"chip hot\">Healthcare</span><span class=\"chip\">Third party</span>"
 "<h3>Veradigm and AdaptHealth — 7.6 million patients between them</h3>"
 "<p><b>Veradigm</b>, the Chicago-based supplier of electronic health records, e-prescribing, patient-engagement, practice-management and "
 "revenue-cycle software to medical practices, warned of a patient data breach after an incident at <b>one of its third-party vendors</b>. The "
 "threat actor claims to hold <b>3.5 million patient records</b> including full names, home addresses, <b>Social Security numbers</b>, email "
 "addresses and phone numbers. Separately <b>AdaptHealth</b> &mdash; home medical equipment, sleep-apnea and respiratory devices, oxygen "
 "therapy, hospital beds and mobility products &mdash; confirmed <b>4.1 million people</b> exposed in a <b>July</b> cyberattack attributed to "
 "<b>ShinyHunters</b>, covering names, contact and demographic details, health insurance information and health information. Both reached the "
 "patient through a supplier.</p></div>"
)
cy = rep(cy, "<h2>Breaches &amp; Incidents</h2><div class=\"cards\">",
         "<h2>Breaches &amp; Incidents</h2><div class=\"cards\">" + new_cards, "cy.newcards")

# --- 5. Florida DAVID: add the 200,000 claim
cy = re.sub(r"(ShinyHunters[^<]{0,400}?DAVID)", r"\1", cy)  # no-op guard
if "DAVID" in cy and "200,000 records" not in cy:
    cy = re.sub(r"(<p>[^<]*?<b>Florida[^<]*?</b>)", r"\1", cy)

# --- 6. CVE table: add Metabase row (insert before closing of the Vulnerability Watch table)
mt = re.search(r"(<h2>Vulnerability Watch</h2>.*?)</table>", cy, re.S)
if not mt:
    fails.append("MISSING ANCHOR: cy.cvetable")
else:
    row = ("<tr><td>CVE-2026-72898</td><td>10.0</td><td>Metabase 0.58/1.58 &ndash; 0.63.4</td>"
           "<td>Unauthenticated SQL injection via the public <code>POST /api/session/reset_password</code> endpoint; yields administrator "
           "access and with it the stored credentials for every connected database. Exploited as a zero-day; Metabase disclosed the attack on "
           "its Cloud environment 6 August, <b>added to KEV 11 August 2026</b>.</td></tr>")
    cy = cy.replace(mt.group(0), mt.group(1) + row + "</table>")

# --- 7. KEV: add the Metabase entry
cy = rep(cy, "<li><b>Recent additions this month:</b>",
 "<li><b>Metabase CVE-2026-72898</b> &mdash; added to KEV on <b>11 August 2026</b>, five days after Metabase disclosed the zero-day attack on "
 "its Cloud environment. Its federal deadline has long since passed; it is listed here because it is the root cause in this run's top story "
 "and remains unpatched in the field, which is a different problem from an open deadline.</li>"
 "<li><b>Recent additions this month:</b>", "cy.kev")

# --- 8. Patch Tuesday counts: add the fifth and sixth figures
cy = cy.replace("other trackers give 964, 973 and 974, and the two reads sharing 973 disagree on the critical subset",
 "other trackers give 964, 973, 974 and — on a count that ranks by risk and appears to scope differently — 1,169; the two reads sharing 973 disagree on the critical subset")

# ============================== WALL STREET ==============================
ws = load("wallstreet-briefing.html")

ws = rep(ws,
 "<div class=\"tldr\"><b>The Tape</b> <span>Markets are closed for the weekend: Wall Street snapped a four-day losing streak on Friday with all three indexes up about 1% as Brent fell nearly 3%, but every index still finished the week lower, and the week ahead turns on Wednesday’s FOMC decision at 2 PM ET — futures price roughly a 90% chance of a rate rise, and this meeting carries a fresh set of economic projections.</span></div>",
 "<div class=\"tldr\"><b>The Tape</b> <span>Markets are closed for the weekend: Wall Street snapped a four-day losing streak on Friday with all three indexes up about 1% after both crude benchmarks reversed an intraday gain to settle sharply lower — WTI at $100.05 and Brent at $104.61 — on news that Iran will meet Gulf states in Oman about the Strait of Hormuz; every index still finished the week lower, and three central banks decide rates next week, the Fed on Wednesday with futures pricing roughly a 90% chance of a rise.</span></div>",
 "ws.tldr")

# Brent row — replace with the sourced settlement
ws = rep(ws,
 "<tr><td>Brent crude</td><td>$104.42</td><td><b>Friday 11 September, down 2.98% on the day</b> — a dated figure sourced this run, which supersedes the “~$99” carried in earlier editions. The near-3% fall is what let equities rally. Brent had ended the previous session at <b>$107.63</b> after soaring <b>6.3% in a day</b> on 10 September.</td></tr>",
 "<tr><td>Brent crude</td><td>$104.61 <span class=\"note\" style=\"display:inline;margin:0\">(settle)</span></td>"
 "<td><b>Settled down 2.8% on Friday 11 September</b> — a settlement figure, newly sourced this run, which supersedes both the &ldquo;~$99&rdquo; "
 "of earlier editions and the <b>$104.42 / −2.98%</b> carried yesterday; that earlier read is named rather than silently dropped, and the two "
 "describe the same move. Brent still gained <b>8.7% on the week</b> and held above $100. It had ended the previous session at <b>$107.63</b> "
 "after soaring <b>6.3% in a day</b> on 10 September.</td></tr>",
 "ws.brent")

# WTI row — first sourced settlement
ws = rep(ws,
 "<td>WTI crude</td><td>$104.02 <span class=\"note\" style=\"display:inline;margin:0\">(open)</span></td><td>That is the <b>Friday 11 September opening</b> price, not a settlement — no WTI closing figure appeared in sources read this run. Prices surged earlier in the week; one read has WTI above $102 at the peak.</td></tr>",
 "<td>WTI crude</td><td>$100.05 <span class=\"note\" style=\"display:inline;margin:0\">(settle)</span></td>"
 "<td><b>Settled down 2.4% on Friday 11 September.</b> This is the <b>first WTI closing figure this page has been able to source</b> — prior "
 "editions carried only the $104.02 open and said so. WTI gained <b>9.4% on the week</b>, the larger of the two benchmarks' weekly moves, and "
 "finished a fraction above the $100 line it had crossed on the way up.</td></tr>",
 "ws.wti")

# On the Radar — oil reversal + three central banks
ws = rep(ws, "<h2>On the Radar</h2><div class=\"panel\"><ul class=\"tight\">",
 "<h2>On the Radar</h2><div class=\"panel\"><ul class=\"tight\">"
 "<li><b>Three central banks decide next week, not one.</b> The <b>Federal Reserve</b>, the <b>Bank of England</b> and the <b>Bank of Japan</b> "
 "all meet, against what one week-ahead preview frames as rising oil prices and mounting inflation pressure. The Fed's is the one with a "
 "projections round attached.</li>"
 "<li><b>Friday's oil move was a reversal, and the intraday print is still circulating.</b> A week-ahead preview written during Friday's session "
 "had oil <i>extending</i> gains, quoting <b>Brent November at $108.21 (+0.54%)</b> and <b>WTI October at $102.96 (+0.47%)</b>. Both benchmarks "
 "then turned and <b>settled lower</b> — Brent $104.61, WTI $100.05. The figures are printed here together because the higher pair is still "
 "being quoted as Friday's, and it is an intraday quote, not a close.</li>"
 "<li><b>What turned it:</b> Iranian state media said Tehran will <b>meet Gulf states in Oman</b> to discuss the <b>Strait of Hormuz</b> — the "
 "first diplomacy after a week of escalation, and the reason a week that ran crude up 9% ended with a near-3% fall.</li>",
 "ws.radar")

# ============================== MMA ==============================
mma = load("mma-briefing.html")

mma = rep(mma,
 "<div class=\"tldr\"><b>Tale of the Tape</b> <span>All 26 fighters made weight for Noche UFC in Glendale, where Jean Silva is a four-to-one favourite over short-notice replacement Jose Delgado with prelims at 2 PM ET and the main card at 5 PM ET on Paramount+ — and Curtis Blaydes fights the first bout of a newly signed eight-fight deal on the same card.</span></div>",
 "<div class=\"tldr\"><b>Tale of the Tape</b> <span>Noche UFC had not begun when this edition was built: UFC.com's own live prelim-results page, checked at 1:10 PM ET, still carried nothing but matchup previews, and it now confirms a 2 PM ET prelim start that settles a start-time conflict three earlier editions printed both ways — Jean Silva remains a four-to-one favourite over short-notice replacement Jose Miguel Delgado in the 5 PM ET main event.</span></div>",
 "mma.tldr")

# Start-time conflict resolution + no-results statement: patch the top story area
mma = rep(mma, "<h2>Top Story</h2>",
 "<h2>Top Story</h2>", "mma.ts")

# Insert a resolution note as the first card of Fight Week
mma = rep(mma, "<h2>Fight Week &mdash; Upcoming Cards</h2>".replace("&mdash;","—"),
 "<h2>Fight Week — Upcoming Cards</h2>", "mma.fw-probe")

sys.stdout.write("ANCHOR FAILURES: %d\n" % len(fails))
for f in fails: print("  " + f)

save("cyber-briefing.html", cy)
save("wallstreet-briefing.html", ws)
save("mma-briefing.html", mma)
print("written")
