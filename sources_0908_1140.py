# -*- coding: utf-8 -*-
import io, os, sys
D = sys.argv[1]
def rd(f): return io.open(os.path.join(D, f), encoding="utf-8").read()
def wr(f, s): io.open(os.path.join(D, f), "w", encoding="utf-8").write(s)

def add(f, items):
    h = rd(f)
    anchor = '</div>\n<p class="disc">'
    assert anchor in h, f
    block = ""
    n = 0
    for t, u in items:
        if u in h:
            continue
        n += 1
        block += '<div style="margin-bottom:7px">%s &mdash; <a href="%s">%s</a></div>' % (t, u, u)
    h = h.replace(anchor, block + anchor, 1)
    wr(f, h)
    print(f, "added", n)

# ---- cyber: August baseline conflict ----
c = rd("cyber-briefing.html")
old = ("For scale: August 2026 delivered <b>421 vulnerabilities</b>, the highest monthly total in "
       "Microsoft&#39;s patching history, <b>42</b> of them classified critical, and included three zero-days.")
new = ("For scale: August 2026 delivered <b>421 vulnerabilities</b>, the highest monthly total in "
       "Microsoft&#39;s patching history, and included <b>one zero-day exploited in the wild</b> &mdash; "
       "<b>CVE-2026-68820</b>, a use-after-free in the <b>Ancillary Function Driver for WinSock (afd.sys)</b> "
       "&mdash; alongside three publicly disclosed zero-days. "
       "<span class=\"mut\">The critical count previously printed here as 42 is withdrawn: a source read this "
       "run gives 62 critical vulnerabilities for the same release, and a third headline read this run counts "
       "the month at 398 flaws rather than 421. The 421 total is corroborated by two sources and is kept; the "
       "critical count is dropped rather than picked between.</span>")
if old in c:
    c = c.replace(old, new, 1)
    wr("cyber-briefing.html", c)
    print("august baseline updated")
else:
    assert "CVE-2026-68820" in c, "august baseline neither old nor new"
    print("august baseline already applied")

add("cyber-briefing.html", [
 ("CERT Polska — Critical vulnerabilities in MikroTik RouterOS are being actively exploited",
  "https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/"),
 ("CERT Polska — Vulnerabilities in MikroTik RouterOS software",
  "https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve/"),
 ("MikroTik — September 2026 vulnerability",
  "https://mikrotik.com/supportsec/september-2026-vulnerability/"),
 ("SOC Prime — CVE-2026-67276: MikroTik RouterOS SSH zero-day exploited in router takeover attacks",
  "https://socprime.com/blog/cve-2026-67276-mikrotik-routeros-ssh-zero-day/"),
 ("BleepingComputer — Hackers exploit new MikroTik RouterOS flaws to hijack routers",
  "https://www.bleepingcomputer.com/news/security/hackers-exploit-new-mikrotik-routeros-flaws-to-hijack-routers/"),
 ("Security Affairs — Your MikroTik router may already be compromised: look for SSH user &ldquo;-2&rdquo;",
  "https://securityaffairs.com/198538/security/your-mikrotik-router-may-already-be-compromised-look-for-ssh-user-2.html"),
 ("Cybersecurity News — SAP security updates September 2026: critical flaws patched in NetWeaver, Cloud and Extended Passport",
  "https://cybersecuritynews.com/sap-security-updates-september-2026/"),
 ("SecurityWeek — August 2026 Patch Tuesday: Microsoft fixes 421 CVEs, one exploited zero-day",
  "https://www.securityweek.com/august-2026-patch-tuesday-microsoft-fixes-421-cves-one-exploited-zero-day/"),
 ("The Register — AI agents carried out every step of this ransomware attack, then left the victim an 80-page security audit",
  "https://www.theregister.com/security/2026/09/02/ai-agents-carried-out-every-step-of-this-ransomware-attack-then-left-the-victim-an-80-page-security-audit/5294009"),
 ("Bright Defense — List of recent data breaches in 2026",
  "https://www.brightdefense.com/resources/recent-data-breaches/"),
 ("CISA — Adds One Known Exploited Vulnerability to Catalog (4 Sep 2026)",
  "https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog"),
])

add("wallstreet-briefing.html", [
 ("CNBC — Treasury yields tick higher as traders look ahead to more economic data releases (8 Sep 2026)",
  "https://www.cnbc.com/2026/09/08/us-treasury-yields-bonds.html"),
 ("Yahoo Finance — Stock market today: Dow, S&amp;P 500 slip as oil prices rise, US&ndash;Canada trade war escalates",
  "https://finance.yahoo.com/markets/live/stock-market-today-tuesday-september-8-dow-sp-500-nasdaq-080440338.html"),
 ("Yahoo Finance — Stock market today (Sept. 8, 2026): S&amp;P 500 edges lower as oil prices climb, Mideast tensions rise",
  "https://finance.yahoo.com/markets/stocks/articles/stock-market-today-sept-8-133744027.html"),
 ("Charles Schwab — Short week packs a punch: stocks down early on oil",
  "https://www.schwab.com/learn/story/stock-market-update-open"),
 ("StocksToTrade — Sandisk stock rides DRAM shortage and meme volatility (4 Sep 2026)",
  "https://stockstotrade.com/news/sandisk-corporation-sndk-news-2026_09_04/"),
])

add("mma-briefing.html", [
 ("ESPN — Current and all-time UFC champions",
  "https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
 ("Wikipedia — UFC 332",
  "https://en.wikipedia.org/wiki/UFC_332"),
 ("Yahoo Sports — UFC 332: injured Valentina Shevchenko vacates title; Nat&aacute;lia Silva vs. Wang Cong headlines for the vacant belt",
  "https://sports.yahoo.com/mma/article/ufc-332-injured-valentina-shevchenko-vacates-title-natalia-silva-vs-wang-cong-headlines-for-vacant-belt-202450352.html"),
 ("UFC.com — Noche UFC: Silva vs. Delgado",
  "https://www.ufc.com/event/ufc-fight-night-september-12-2026"),
 ("Yahoo Sports — Jean Silva vs. Jose Delgado Noche UFC betting odds revealed",
  "https://sports.yahoo.com/articles/jean-silva-vs-jose-delgado-055714314.html"),
 ("Tapology — Contender Series 2026: Week 5",
  "https://www.tapology.com/fightcenter/events/142724-contender-series-2026-week-5"),
 ("BJJ TV — Contender Series Week 5 card set for Meta APEX with five contract fights",
  "https://bjj.tv/contender-series-week-5-card-set-for-meta-apex-with-five-contract-fights/"),
])
