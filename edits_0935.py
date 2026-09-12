#!/usr/bin/env python3
"""Morning Edition, Saturday 12 September 2026 (~9:35 AM ET) — fourth run of the day.
Patches the four pages with facts verified in THIS run's searches/fetches."""
import io, os, sys

SRC = sys.argv[1]
OUT = sys.argv[2]

def load(n):
    return io.open(os.path.join(SRC, n), encoding="utf-8").read()

def save(n, s):
    io.open(os.path.join(OUT, n), "w", encoding="utf-8").write(s)

N = 0
def rep(s, old, new, count=1, label=""):
    global N
    assert s.count(old) == count, "ANCHOR MISS (%d found, %d expected): %s | %.90s" % (
        s.count(old), count, label, old)
    N += count
    return s.replace(old, new)

# ───────────────────────── CYBER ─────────────────────────
cy = load("cyber-briefing.html")

# 1. Top story — GreyNoise attribution, campaign start date, escalation depth, patched builds.
cy = rep(cy,
  "The agents ran on OpenAI’s Codex harness paired with a DeepSeek model, alongside publicly available offensive security tools. Before going wide, the attacker built a private lab containing a vulnerable copy of PaperCut NG/MF and an Active Directory server in order to develop and test the exploits. The tempo that followed is the part defenders should sit with: <b>eleven organisations were compromised in 26 seconds</b>, and some individual servers fell in under thirty.",
  "The agents ran on OpenAI’s Codex harness paired with a DeepSeek model, alongside publicly available offensive security tools. <b>GreyNoise dates the campaign’s start to 31 August</b>, beginning from an empty workspace: the agents read the patches, replicated the code-execution path in a local virtual lab, wrote Go-based multi-threaded scanners and tuned their probes against live errors. Before going wide, the attacker built a private lab containing a vulnerable copy of PaperCut NG/MF and an Active Directory server in order to develop and test the exploits. The tempo that followed is the part defenders should sit with: <b>eleven organisations were compromised in 26 seconds</b>, some individual servers fell in under thirty, and one US high school went from initial access to <b>full domain administrative control in seven minutes</b>.",
  label="cyber top story para 2")

cy = rep(cy,
  "Education was by far the most affected sector, with <b>204 victims</b>. By country the United States recorded the most at <b>98</b>, followed by the United Kingdom, France, Spain and Canada.",
  "Education was by far the most affected sector, with <b>204 victims</b>. By country the United States recorded the most at <b>98</b>, followed by the United Kingdom, France, Spain and Canada. Depth matters as much as breadth here: credentials were harvested from <b>280 victims</b>, operating-system or domain secrets from <b>147</b>, and administrator privileges reached at <b>12 organisations</b> — so the great majority of the 440 were compromised without the attacker converting that into domain control.",
  label="cyber top story para 3")

cy = rep(cy,
  "Researchers described the anomaly as “agents gone wild”, a plain illustration that an autonomous offensive operation can drift from the intent of the person who launched it.",
  "Researchers described the anomaly as “agents gone wild”, a plain illustration that an autonomous offensive operation can drift from the intent of the person who launched it.</p><p>The two flaws were published on <b>28 August</b> — <b>CVE-2026-81578</b> an authentication bypass, <b>CVE-2026-82078</b> an unsafe-reflection remote code execution flaw — and chain to let an unauthenticated attacker alter configuration and run arbitrary Java bytecode as the PaperCut server. PaperCut has shipped maintenance releases <b>26.0.5, 25.0.13 and 24.1.10</b>; if you run an internet-facing print server, that is the build to be on.",
  label="cyber top story para 4")

# 2. New CVE row — the SECOND exploited V8 zero-day, added to KEV 9 September, due 23 September.
cy = rep(cy,
  "<tr><td class=\"mono\">CVE-2026-75650</td>",
  "<tr><td class=\"mono\">CVE-2026-87491</td><td class=\"mono\">Not stated in sources read</td><td>Google Chrome / Chromium V8</td><td>An <b>out-of-bounds write</b> in V8 — a second exploited V8 zero-day inside a week, distinct from CVE-2026-85046 above. A crafted HTML page can lead to arbitrary code execution inside the browser sandbox. Fixed in <b>Chrome 153.0.8010.36/.37</b> for Windows and macOS and 153.0.8010.36 for Linux, in the <b>8 September</b> Stable channel release. Google confirms an exploit exists in the wild but has not said who is using it or how it is delivered. Added to KEV 9 September, <b>due 23 September</b> — a 14-day window. No CVSS figure appeared in any source read, so none is published.</td></tr><tr><td class=\"mono\">CVE-2026-75650</td>",
  label="cyber new CVE row 87491")

# 3. KEV ladder — the 9 September batch was FOUR, not three; add the Chromium entry with its own window.
cy = rep(cy,
  "— added 9 September, due <b>12 September</b> <b class=\"critc\">(0 days left — today)</b>.</li>",
  "— added 9 September, due <b>12 September</b> <b class=\"critc\">(0 days left — today)</b>. CISA’s 9 September bulletin catalogued <b>four</b> CVEs, not the three that carry today’s date; the fourth is the Chromium entry below, which was given a longer window.</li>",
  label="cyber KEV 9 Sep batch")

cy = rep(cy,
  "<li><b>Google Chromium <span class=\"mono\">CVE-2026-85046</span></b> — added 4 September, due <b>18 September</b> (6 days left).</li>",
  "<li><b>Google Chromium <span class=\"mono\">CVE-2026-85046</span></b> — added 4 September, due <b>18 September</b> (6 days left).</li>"
  "<li><span class=\"tag new\">New</span> <b>Google Chromium <span class=\"mono\">CVE-2026-87491</span></b> — added 9 September, due <b>23 September</b> (11 days left). The fourth CVE in the same bulletin as the Cisco, Citrix and Fortinet entries above, and the clearest illustration on this page that BOD 26-04 assigns its window per CVE rather than per batch: same bulletin, same day, deadlines eleven days apart.</li>",
  label="cyber KEV chromium new bullet")

# 4. Summary strip + threat banner reflect the added entry.
cy = rep(cy,
  "CISA has set Monday as the federal deadline for a CVSS 10.0 file-read flaw in GitLab, and the maximum-severity N-able N-central bug is now a day past its own.",
  "CISA has set Monday as the federal deadline for a CVSS 10.0 file-read flaw in GitLab, and a second exploited Chrome V8 zero-day has joined the catalogue inside a week.",
  label="cyber tldr")

# 5. Threat-level banner: the catalogue grew again today.
cy = rep(cy,
  "five CVSS 10.0 flaws in the table below are under active exploitation, and four federal remediation deadlines fall today or have already passed.",
  "five CVSS 10.0 flaws in the table below are under active exploitation, four federal remediation deadlines fall today or have already passed, and a second exploited Chrome V8 zero-day entered the catalogue this week.",
  label="cyber threat banner")

# 6. Sources added this run.
cy = rep(cy,
  "<footer><h4>Sources</h4><ul>",
  "<footer><h4>Sources</h4><ul>"
  "<li><a href=\"https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-one-known-exploited-vulnerability-catalog\">CISA — CISA Adds One Known Exploited Vulnerability to Catalog (11 September 2026)</a></li>"
  "<li><a href=\"https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog\">CISA — CISA Adds Four Known Exploited Vulnerabilities to Catalog (9 September 2026)</a></li>"
  "<li><a href=\"https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html\">The Hacker News — Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox</a></li>"
  "<li><a href=\"https://securityonline.info/chrome-zero-day-cve-2026-87491/\">securityonline.info — Chrome 153 Patches Zero-Day CVE-2026-87491 Exploited in the Wild</a></li>"
  "<li><a href=\"https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html\">The Hacker News — CISA Flags Exploited Cisco, Citrix, Fortinet Flaws, Sets Sept. 12 Federal Patch Deadline</a></li>"
  "<li><a href=\"https://www.techrepublic.com/article/news-papercut-ai-agents-compromise-440-servers/\">TechRepublic — AI Agents Help Hackers Compromise 440 PaperCut Servers</a></li>",
  label="cyber sources")

save("cyber-briefing.html", cy)

# ───────────────────────── MMA ─────────────────────────
mm = load("mma-briefing.html")

# 1. Full first names from UFC.com's official main-card results page.
mm = rep(mm, "Sola def. Farès Ziam", "Axel Sola def. Farès Ziam", label="mma Sola name")
mm = rep(mm, "Keita def. Muhammad Naimov", "Losene Keita def. Muhammad Naimov", label="mma Keita name")
mm = rep(mm, "Donchenko def. Punahele Soriano", "Daniil Donchenko def. Punahele Soriano", label="mma Donchenko name")

# 2. Parnasse record and the competing stoppage time.
mm = rep(mm,
  "A former two-time KSW featherweight champion and one-time KSW lightweight champion, 14-2 inside KSW, who signed with the UFC in late July 2026 having previously turned the promotion down. He did <b>not</b> come through the Contender Series.",
  "The 28-year-old is now <b>24-2</b> and has <b>won six straight, all by stoppage</b>. A former two-time KSW featherweight champion and one-time KSW lightweight champion, 14-2 inside KSW, who signed with the UFC in late July 2026 having previously turned the promotion down. He did <b>not</b> come through the Contender Series.",
  label="mma parnasse record")

# 3. Odds range widens on a fresh read.
mm = rep(mm,
  "The books make it lopsided. Silva runs from <b>−425 to −455</b> across the six books read, with Delgado between <b>+310 and +355</b>.",
  "The books make it lopsided. Silva runs from <b>−410 to −455</b> across the seven reads taken, with Delgado between <b>+310 and +355</b>; the shortest price this run, −410, carries an implied win probability of <b>77%</b>, and the same read gives Silva a <b>63%</b> chance of winning by knockout or TKO.",
  label="mma odds range")

# 4. UFC 331 start times re-read.
mm = rep(mm,
  "Thirteen fights; prelims 6 PM ET, main card 9 PM ET.",
  "Thirteen fights; Al Jazeera’s card breakdown gives early prelims about 5 PM ET, prelims 7 PM ET and the main card 9 PM ET (an earlier edition today read the prelims as 6 PM ET, and both are printed).",
  label="mma 331 times")

# 5. Champions-board warning: ESPN returned THREE stale rows this run, not two.
mm = rep(mm,
  "returned <b>two stale belts</b>: Alex Pereira at light heavyweight (dated 4 October 2025, which predates Ulberg’s April 2026 win outright) and Valentina Shevchenko at women’s flyweight.",
  "returned <b>three stale belts</b> this time, one worse than the previous run: Alex Pereira at light heavyweight (dated 4 October 2025, which predates Ulberg’s April 2026 win outright), <b>Khamzat Chimaev at middleweight</b> (dated 16 August 2025, which predates Strickland’s May 2026 upset) and Valentina Shevchenko at women’s flyweight (dated 14 September 2024).",
  label="mma espn stale note")

save("mma-briefing.html", mm)

# ───────────────────────── WALL STREET ─────────────────────────
ws = load("wallstreet-briefing.html")

# 1. Breadth and the small-cap read.
ws = rep(ws,
  "and the session review is carried here as the later measurement.",
  "and the session review is carried here as the later measurement. Breadth backed the move: advancing issues beat decliners inside the index by roughly <b>2.1 to 1</b>, and the <b>Russell 2000 added 0.45%</b> — a narrower gain than the large-cap averages.",
  label="ws sector breadth")

# 2. Oracle card — the quarter that started it, and the disagreement about Friday's close.
ws = rep(ws,
  "The company whose spending plan moved its suppliers <b>rose as much as 10.3% intraday and finished about +0.3%</b>.",
  "The quarter underneath it beat: adjusted <b>$1.92 a share on revenue of $19.35 billion</b> in the fiscal first quarter, against the <b>$1.74 and $19.14 billion</b> analysts polled by LSEG had sought, on cloud and AI-infrastructure growth. The Friday move is where reads diverge. One set has the company that moved its suppliers <b>rising as much as 10.3% intraday and finishing about +0.3%</b>; a movers roundup read this run instead puts it up <b>6%</b>. Both are printed rather than reconciled, because no source read this run states an official closing change.",
  label="ws oracle card")

save("wallstreet-briefing.html", ws)

print("OK  replacements=%d" % N)
