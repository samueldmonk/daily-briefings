#!/usr/bin/env python3
# Daily Briefings generator — Thursday, August 27, 2026, Morning Edition (~8:06 AM ET)
import os
OUT = "/sessions/nice-ecstatic-thompson/mnt/outputs"

STAMP_JS = """<script>(function(){try{var n=new Date();var et=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'long',year:'numeric',month:'long',day:'numeric'}).format(n);var t=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',minute:'2-digit'}).format(n);var h=parseInt(new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',hour:'numeric',hour12:false}).format(n),10);var ed=h<11?'Morning Edition':(h<15?'Midday Edition':'Afternoon Edition');document.getElementById('datestamp').textContent=et;document.getElementById('updated').textContent=t+' ET';document.getElementById('edition').textContent=ed;var fl=document.getElementById('freshline');if(fl)fl.textContent='Data as of '+t+' ET · briefings refresh every 30 minutes, 8 AM–6 PM ET';}catch(e){}})();</script>"""

def base_css(bg, panel, line, acc, acc2, ink="#e9e6e1", mut="#9aa0a6"):
    return f""":root{{--bg:{bg};--panel:{panel};--line:{line};--acc:{acc};--acc2:{acc2};--ink:{ink};--mut:{mut};--up:#3fbf7f;--down:#ef5b5b;--warn:#e0a33a;--crit:#e0483a;--mono:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 -apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1060px;margin:0 auto;padding:26px 20px 70px}}
header.mast{{padding:6px 0 2px}}
.mast h1{{margin:0;font-size:33px;letter-spacing:-.02em}}
.mast .sub{{color:var(--mut);font-size:14.5px;margin-top:3px}}
.meta{{display:flex;flex-wrap:wrap;gap:8px;margin-top:13px}}
.pill{{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut);background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:5px 11px}}
.pill.live{{color:var(--up);border-color:var(--up)}}
.pill.live .dot{{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--up);margin-right:6px;vertical-align:1px}}
nav.tabs{{display:flex;flex-wrap:wrap;gap:7px;margin:16px 0 18px;border-bottom:1px solid var(--line);padding-bottom:12px}}
nav.tabs a{{text-decoration:none;color:var(--mut);font-family:var(--mono);font-size:11.5px;letter-spacing:.11em;text-transform:uppercase;border:1px solid var(--line);border-radius:999px;padding:7px 13px;background:var(--panel);transition:.16s}}
nav.tabs a:hover{{color:var(--ink);border-color:var(--acc)}}
nav.tabs a.on{{color:var(--bg);background:var(--acc);border-color:var(--acc);font-weight:700}}
.tldr{{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--acc);border-radius:10px;padding:11px 15px;margin:6px 0 2px;font-size:14.5px;line-height:1.5}}
.tldr b{{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--acc);margin-right:9px}}
.freshline{{font-family:var(--mono);font-size:11px;letter-spacing:.06em;color:var(--mut);margin:9px 2px 4px}}
h2.sec{{font-family:var(--mono);font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin:34px 0 12px;padding-bottom:7px;border-bottom:1px solid var(--line)}}
.panel{{background:var(--panel);border:1px solid var(--line);border-radius:13px;padding:17px 19px}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:13px}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:13px;padding:15px 17px;transition:transform .16s,border-color .16s}}
.card:hover{{transform:translateY(-3px);border-color:var(--acc)}}
.card h3{{margin:0 0 7px;font-size:16.5px;line-height:1.35}}
.card p{{margin:0;font-size:14.3px;color:#cdd3d6}}
.tag{{display:inline-block;font-family:var(--mono);font-size:10px;letter-spacing:.13em;text-transform:uppercase;border-radius:999px;padding:3px 9px;margin:0 6px 8px 0;border:1px solid var(--line);color:var(--mut)}}
.tag.new{{color:var(--up);border-color:var(--up)}}
.tag.acc{{color:var(--acc);border-color:var(--acc)}}
.tag.warn{{color:var(--warn);border-color:var(--warn)}}
.tag.crit{{color:var(--crit);border-color:var(--crit)}}
.callout{{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--warn);border-radius:11px;padding:14px 17px;margin-top:6px}}
.callout.crit{{border-left-color:var(--crit)}}
.callout h3{{margin:0 0 6px;font-size:16px}}
table{{width:100%;border-collapse:collapse;font-size:14.2px;background:var(--panel);border:1px solid var(--line);border-radius:13px;overflow:hidden}}
th{{text-align:left;font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);padding:11px 13px;border-bottom:1px solid var(--line);background:rgba(255,255,255,.02)}}
td{{padding:10px 13px;border-bottom:1px solid var(--line);vertical-align:top}}
tr:last-child td{{border-bottom:0}}
.up{{color:var(--up)}} .down{{color:var(--down)}} .mono{{font-family:var(--mono)}}
ul.bul{{margin:0;padding-left:19px}} ul.bul li{{margin:8px 0;font-size:14.5px}}
.note{{font-size:12.5px;color:var(--mut);margin-top:9px;line-height:1.55}}
footer{{margin-top:42px;border-top:1px solid var(--line);padding-top:16px;color:var(--mut);font-size:12.5px}}
footer a{{color:var(--acc2);text-decoration:none;word-break:break-all}} footer a:hover{{text-decoration:underline}}
footer li{{margin:5px 0}}
.disc{{margin-top:14px;font-size:12px;color:var(--mut);font-style:italic}}
.livebar{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}}
.livebar-label{{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);display:flex;align-items:center;gap:8px;padding:4px 8px 8px}}
.livebar-label .dot{{width:7px;height:7px;border-radius:50%;background:var(--up);display:inline-block}}
.tickers{{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px}}
.ticker{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}}
.cdn{{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--acc);border-radius:11px;padding:11px 15px;margin:2px 0 4px;font-size:14.2px;display:flex;flex-wrap:wrap;gap:10px;align-items:baseline}}
.cdn b{{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--acc)}}
.cdn #ufccdn{{font-family:var(--mono);color:var(--acc2);font-weight:700}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-top:4px}}
.stat{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:13px 15px}}
.stat .n{{font-family:var(--mono);font-size:22px;font-weight:700;color:var(--acc)}}
.stat .l{{font-size:12.3px;color:var(--mut);margin-top:3px;line-height:1.45}}
.banner{{border-radius:12px;padding:13px 16px;border:1px solid var(--line);background:var(--panel);border-left:4px solid var(--crit);margin-bottom:14px}}
.banner .lv{{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--crit);font-weight:700}}
@media(max-width:620px){{.mast h1{{font-size:26px}}}}"""

def nav(active):
    items = [("index.html","★ Front Page","index"),
             ("cyber-briefing.html","⛨ The Cyber Wire","cyber"),
             ("wallstreet-briefing.html","▲ The Closing Bell","ws"),
             ("mma-briefing.html","⊘ The Octagon","mma"),
             ("archive.html","\U0001f5c4 Archive","arch")]
    out = []
    for h, t, k in items:
        cls = ' class="on"' if k == active else ''
        out.append('<a href="%s"%s>%s</a>' % (h, cls, t))
    return '<nav class="tabs">' + "".join(out) + '</nav>'

def mast(title, sub):
    return f"""<header class="mast"><h1>{title}</h1><div class="sub">{sub}</div>
<div class="meta"><span class="pill live"><span class="dot"></span>Live</span><span class="pill" id="edition">&nbsp;</span><span class="pill" id="datestamp">&nbsp;</span><span class="pill">Updated <span id="updated">&nbsp;</span></span></div></header>"""

def page(title, css, body, extra_js=""):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{css}</style></head><body><div class="wrap">
{body}
</div>{STAMP_JS}{extra_js}</body></html>"""

# ---------------------------------------------------------------- summaries
S_CY = "CISA's federal deadline to patch the maximum-severity Oracle WebLogic Proxy flaw CVE-2026-21962 — CVSS 10.0 and confirmed under active exploitation — expires today, August 27."
S_WS = "Nvidia's $96.2 billion quarter and a $108 billion third-quarter forecast sent the chipmaker up sharply in premarket trade and lifted S&P 500 and Nasdaq 100 futures, while Dow futures slipped."
S_MM = "It is fight week in Shanghai: bantamweight contenders Umar Nurmagomedov and Song Yadong headline Saturday's card at the Oriental Sports Center, with Nurmagomedov roughly a −500 favourite."

SRC_COMMON = []

# ================================================================= CYBER
cy_css = base_css("#0b0f0f","#121a19","#1e2a29","#22d3a8","#36c6ff")
cy_sources = [
 ("CISA — Adds One Known Exploited Vulnerability to Catalog (Aug 24, 2026)","https://www.cisa.gov/news-events/alerts/2026/08/24/cisa-adds-one-known-exploited-vulnerability-catalog"),
 ("SecurityWeek — CISA Warns of Exploited Oracle WebLogic Vulnerability","https://www.securityweek.com/cisa-warns-of-exploited-oracle-weblogic-vulnerability/"),
 ("The Hacker News — Actively Exploited Oracle WebLogic Flaw Lets Unauthenticated Attackers Access Critical Data","https://thehackernews.com/2026/08/actively-exploited-oracle-weblogic-flaw.html"),
 ("Global Security Mag — CISA orders federal agencies to patch actively exploited Oracle flaw by August 27","https://www.globalsecuritymag.com/cisa-orders-federal-agencies-to-patch-actively-exploited-oracle-flaw-by-august.html"),
 ("The Stack — CISA spots Oracle bug exploitation seven months after patch","https://www.thestack.technology/cisa-spots-oracle-bug-exploitation-seven-months-after-patch/"),
 ("SecurityWeek — Cl0p Ransomware Group Names Over 40 Victims of PTC Windchill Campaign","https://www.securityweek.com/cl0p-ransomware-group-names-over-40-victims-of-ptc-windchill-campaign/"),
 ("BleepingComputer — Clop ransomware targets Windchill, FlexPLM in data theft attacks","https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/"),
 ("The Hacker News — Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE","https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html"),
 ("The Hacker News — front page (Aug 26, 2026 stories: Kaltura, AnonyMousKIT, Nimbus Manticore)","https://thehackernews.com/"),
 ("SecurityWeek — August 2026 Patch Tuesday: Microsoft Fixes 421 CVEs, One Exploited Zero-Day","https://www.securityweek.com/august-2026-patch-tuesday-microsoft-fixes-421-cves-one-exploited-zero-day/"),
 ("Help Net Security — Microsoft patches 400+ vulnerabilities, one zero-day under attack (CVE-2026-68820)","https://www.helpnetsecurity.com/2026/08/12/august-2026-patch-tuesday-cve-2026-68820/"),
 ("CISA — Adds One Known Exploited Vulnerability to Catalog (Aug 21, 2026 — Zimbra CVE-2026-73570)","https://www.cisa.gov/news-events/alerts/2026/08/21/cisa-adds-one-known-exploited-vulnerability-catalog"),
 ("CISA — Adds Three Known Exploited Vulnerabilities to Catalog (Aug 11, 2026)","https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog"),
 ("Cybersecurity News — Weekly bulletin (ReliaQuest phishing, Entra ID CVE-2026-69836)","https://cybersecuritynews.com/cyber-security-newsletter-bulletin-august/"),
]
cy_body = f"""{mast("The Cyber Wire","Your daily cybersecurity briefing — breaches, exploits &amp; federal deadlines")}
<div class="tldr"><b>The Wire</b> <span>{S_CY}</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
{nav("cyber")}

<div class="banner"><div class="lv">Threat level · High</div>
<div style="margin-top:5px;font-size:14.6px">A CVSS 10.0, unauthenticated Oracle flaw is being exploited in the wild and the federal remediation deadline lands today — while Cl0p continues to publish victims from its PTC Windchill data-theft campaign.</div></div>

<div class="stats">
<div class="stat"><div class="n">10.0</div><div class="l">Oracle's own CVSS score for CVE-2026-21962 — the maximum (SecurityWeek)</div></div>
<div class="stat"><div class="n">40+</div><div class="l">Organisations named on Cl0p's leak site in the PTC Windchill / FlexPLM campaign (SecurityWeek)</div></div>
<div class="stat"><div class="n">421</div><div class="l">CVEs fixed in Microsoft's August 2026 Patch Tuesday, including one exploited zero-day (SecurityWeek)</div></div>
<div class="stat"><div class="n">7 mo</div><div class="l">Between Oracle's January patch and CISA spotting exploitation (The Stack)</div></div>
</div>

<h2 class="sec">Top Story</h2>
<div class="panel">
<span class="tag new">New · 8:06</span><span class="tag crit">Deadline today</span><span class="tag acc">KEV</span>
<h3 style="margin:2px 0 8px;font-size:20px">Federal agencies have until today to patch a maximum-severity Oracle WebLogic proxy flaw</h3>
<p style="margin:0 0 10px">CISA added <span class="mono">CVE-2026-21962</span> to its Known Exploited Vulnerabilities catalog on <b>August 24</b>, confirming that attackers are using the flaw against <b>Oracle HTTP Server</b> and the <b>Oracle WebLogic Server Proxy Plug-in</b>, and instructed federal agencies to remediate it by <b>August 27</b> — today.</p>
<p style="margin:0 0 10px">Oracle rates the vulnerability <b>CVSS 10.0</b>. The attack arrives over HTTP with <b>no authentication, no user interaction and no existing privileges</b>, and lets an attacker access or modify critical data through crafted HTTP requests. The vulnerable components are the WebLogic Server Proxy Plug-in for <b>Apache HTTP Server</b> and for <b>Microsoft IIS</b>, including deployments bundled with Oracle HTTP Server.</p>
<p style="margin:0">A fix has existed since <b>January 20, 2026</b>, when Oracle disclosed and patched the issue in its January Critical Patch Update — roughly seven months before CISA flagged exploitation.</p>
</div>

<h2 class="sec">Patch Priority</h2>
<div class="callout crit">
<h3>Patch <span class="mono">CVE-2026-21962</span> — Oracle HTTP Server / WebLogic Server Proxy Plug-in — <span style="color:var(--crit)">due today, August 27</span></h3>
<p style="margin:0;font-size:14.4px">This is the single most urgent item on the board: maximum severity (CVSS 10.0 per Oracle), unauthenticated and remotely reachable over HTTP, confirmed exploited by CISA, and the BOD-assigned federal remediation date expires today. Inventory every Apache HTTP Server and Microsoft IIS instance running the WebLogic proxy plug-in — including the copies bundled inside Oracle HTTP Server — and apply the January 2026 Critical Patch Update.</p>
</div>

<h2 class="sec">Threat Actor Spotlight</h2>
<div class="cards"><div class="card" style="grid-column:1/-1">
<span class="tag crit">Cl0p</span><span class="tag">Data-theft extortion</span><span class="tag">Carried</span>
<h3>Cl0p is still publishing victims from its PTC Windchill campaign</h3>
<p>The Cl0p ransomware group has been exploiting <span class="mono">CVE-2026-12569</span>, a critical improper-input-validation flaw in PTC's product lifecycle management platforms <b>Windchill</b> and <b>FlexPLM</b>. The bug carries a <b>CVSS 9.8</b>, stems from deserialisation of untrusted data, and affects releases <b>prior to 11.0 M030</b>. Operators deploy <b>JSP webshells</b> to exfiltrate data rather than encrypt it.<br><br>
As of <b>August 19</b>, the group had named <b>more than 40 organisations</b> on its leak site, including <b>Shell, Philips, Fiserv, Zebra, Mindray and Largan Precision</b>. Extortion emails are sent from randomly compromised accounts to hundreds of users inside each victim. Targeted sectors include manufacturing, automotive, aerospace and retail. <span style="color:var(--mut)">(SecurityWeek, BleepingComputer, The Hacker News)</span></p>
</div></div>

<h2 class="sec">Breaches &amp; Incidents</h2>
<div class="cards">
<div class="card"><span class="tag crit">Extortion</span><span class="tag">Manufacturing</span><span class="tag">Carried</span>
<h3>Cl0p names 40+ Windchill victims</h3><p>Shell, Philips, Fiserv, Zebra, Mindray and Largan Precision are among the organisations listed on Cl0p's leak site as of August 19 in the PTC Windchill / FlexPLM data-theft campaign. <span style="color:var(--mut)">(SecurityWeek)</span></p></div>

<div class="card"><span class="tag warn">Phishing</span><span class="tag">Security vendor</span><span class="tag">Carried</span>
<h3>ReliaQuest employee phished</h3><p>A ReliaQuest employee fell victim to a phishing attack and the attackers gained access to a dashboard, in an incident reported around August 24–25. <span style="color:var(--mut)">(Cybersecurity News weekly bulletin)</span></p></div>

<div class="card"><span class="tag crit">Nation-state</span><span class="tag">Espionage</span><span class="tag">Carried</span>
<h3>Nimbus Manticore infrastructure surfaces</h3><p>Researchers uncovered additional infrastructure and previously undocumented malware tied to <b>Nimbus Manticore</b>, an Iranian state-sponsored group affiliated with the IRGC that Group-IB describes as among the most active Iranian APT groups of 2026. <span style="color:var(--mut)">(The Hacker News)</span></p></div>

<div class="card"><span class="tag warn">Fraud</span><span class="tag">Phishing-as-a-service</span><span class="tag">Carried</span>
<h3>AnonyMousKIT strips Apple Activation Lock</h3><p>A phishing-as-a-service platform built to remove Apple's Activation Lock from stolen devices uses <b>rented AI voice agents</b> that call theft victims posing as Apple Support and ask for the device passcode. <span style="color:var(--mut)">(The Hacker News)</span></p></div>

<div class="card"><span class="tag warn">Unpatched</span><span class="tag">Supply chain</span><span class="tag">Carried</span>
<h3>Kaltura video player flaws disclosed unpatched</h3><p>CERT/CC disclosed two unpatched vulnerabilities in Kaltura's HTML5 video player library that let a remote, unauthenticated attacker read arbitrary files from a server and execute code on it. <span style="color:var(--mut)">(The Hacker News / CERT/CC)</span></p></div>
</div>

<h2 class="sec">Vulnerability Watch</h2>
<table><thead><tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr></thead><tbody>
<tr><td class="mono">CVE-2026-21962</td><td class="mono" style="color:var(--crit)">10.0</td><td>Oracle HTTP Server; WebLogic Server Proxy Plug-in (Apache HTTP Server, Microsoft IIS)</td><td>Unauthenticated over HTTP; in KEV since Aug 24, federal due date <b>Aug 27</b>. Patched by Oracle Jan 20, 2026 CPU.</td></tr>
<tr><td class="mono">CVE-2026-12569</td><td class="mono">9.8</td><td>PTC Windchill / FlexPLM prior to 11.0 M030</td><td>Deserialisation of untrusted data → RCE. Exploited by Cl0p affiliates with JSP webshells.</td></tr>
<tr><td class="mono">CVE-2026-69836</td><td class="mono">Max severity (Microsoft)</td><td>Microsoft Entra ID</td><td>Critical remote code execution, disclosed Aug 20, 2026. Numeric CVSS not confirmed this run.</td></tr>
<tr><td class="mono">CVE-2026-68820</td><td class="mono">Not confirmed</td><td>Windows Ancillary Function Driver for WinSock (afd.sys)</td><td>Use-after-free elevation of privilege to SYSTEM; the exploited zero-day in August Patch Tuesday. KEV due date <b>Aug 25 — lapsed</b>.</td></tr>
<tr><td class="mono">CVE-2026-62815</td><td class="mono">9.8</td><td>Microsoft QUIC</td><td>Critical RCE fixed in the August 2026 Patch Tuesday.</td></tr>
<tr><td class="mono">CVE-2026-62893</td><td class="mono">9.8</td><td>Windows Deployment Services</td><td>Critical RCE fixed in the August 2026 Patch Tuesday.</td></tr>
<tr><td class="mono">CVE-2026-60004</td><td class="mono">Not confirmed</td><td>Gitea (fixed in 1.27.1)</td><td>Remote code execution; on the KEV board with a federal due date of <b>Aug 28</b>.</td></tr>
<tr><td class="mono">CVE-2026-73570</td><td class="mono">Not confirmed</td><td>Zimbra Collaboration Suite</td><td>OS command injection; added to KEV Aug 21, 2026.</td></tr>
</tbody></table>
<div class="note">Scores are printed only where a source seen this run states them. "Not confirmed" means no vendor or CISA figure was verified this run — no number is inferred.</div>

<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>
<div class="panel"><ul class="bul">
<li><b class="mono">CVE-2026-21962</b> — Oracle HTTP Server / WebLogic Server Proxy Plug-in. Added <b>Aug 24</b>, due <b>Aug 27</b> — <span style="color:var(--crit);font-weight:700" id="kev1">(0 days left)</span>.</li>
<li><b class="mono">CVE-2026-60004</b> — Gitea remote code execution, fixed in 1.27.1. Due <b>Aug 28</b> — <span class="mono" id="kev2">(1 day left)</span>.</li>
<li><b class="mono">CVE-2026-68820</b> — Windows AFD for WinSock zero-day. Due <b>Aug 25</b> — <span style="color:var(--crit);font-weight:700" id="kev3">(overdue)</span>.</li>
<li><b class="mono">CVE-2026-73570</b> — Zimbra Collaboration OS command injection, added <b>Aug 21</b>. No due date verified this run.</li>
<li><b>Aug 18 batch</b> — four vulnerabilities added spanning <b>Apple macOS, Microsoft SharePoint, VMware vCenter and Windows</b>. No due dates verified this run.</li>
<li><b>Aug 11 batch</b> — three vulnerabilities added: <span class="mono">CVE-2026-20349</span> (Cisco Secure Firewall ASA / FTD), <span class="mono">CVE-2026-68820</span> (Microsoft Windows) and <span class="mono">CVE-2026-72898</span> (Metabase SQL injection).</li>
</ul>
<div class="note">Countdowns are computed from today's date to the due date published by CISA. Remediation windows are assigned per-CVE under CISA's risk-based directive — no fixed three-week window is assumed.</div></div>

<footer><b style="color:var(--ink)">Sources</b><ul class="bul">
{"".join(f'<li><a href="{u}">{t}</a></li>' for t,u in cy_sources)}
</ul>
<div class="disc">Compiled from public reporting fetched this run. Vulnerability details change quickly — verify against the vendor advisory before acting. This briefing is informational and is not a substitute for your own security review.</div></footer>"""

CY_KEV_JS = """<script>(function(){try{function d(y,m,dd){return new Date(Date.UTC(y,m-1,dd));}
var now=new Date();var s=new Intl.DateTimeFormat('en-CA',{timeZone:'America/New_York',year:'numeric',month:'2-digit',day:'2-digit'}).format(now).split('-');
var today=d(+s[0],+s[1],+s[2]);
function set(id,due){var el=document.getElementById(id);if(!el)return;var n=Math.round((due-today)/86400000);
if(n>1)el.textContent='('+n+' days left)';else if(n===1)el.textContent='(1 day left)';else if(n===0)el.textContent='(0 days left — due today)';else el.textContent='('+Math.abs(n)+' day'+(Math.abs(n)===1?'':'s')+' overdue)';}
set('kev1',d(2026,8,27));set('kev2',d(2026,8,28));set('kev3',d(2026,8,25));}catch(e){}})();</script>"""

# ================================================================= WALL STREET
ws_css = base_css("#0d0c0a","#171410","#2a2418","#caa64a","#e8c766") + """
.mast h1{font-family:Georgia,'Times New Roman',serif;font-weight:700}
h2.sec{font-family:var(--mono)}
.card h3,.callout h3,.panel h3{font-family:Georgia,'Times New Roman',serif}
.lead h3{font-family:Georgia,'Times New Roman',serif;font-size:22px;line-height:1.3;margin:2px 0 10px}"""

ws_sources = [
 ("Benzinga — Stock Market Today: S&P 500, Nasdaq 100 Futures Gain, While Dow Slips Following NVDA Blockbuster Q2 Report","https://www.benzinga.com/markets/equities/26/08/61454942/stock-market-today-sp-500-nasdaq-100-futures-gain-while-dow-slips-following-nvda-blockbuster-q2-report-crm-crwd-hpq-in-focus"),
 ("Bloomberg — Stock Market Today: Dow, S&P Live Updates for August 27","https://www.bloomberg.com/news/articles/2026-08-26/nasdaq-futures-rise-on-bullish-nvidia-sales-growth-markets-wrap"),
 ("CNBC — Stock futures rise as Nvidia shares gain over 4% after earnings","https://www.cnbc.com/2026/08/26/stock-market-today-live-updates.html"),
 ("Yahoo Finance — Stock market today: Dow, S&P 500, Nasdaq close lower, Nvidia stock jumps after earnings (Wed Aug 26)","https://finance.yahoo.com/markets/live/stock-market-today-wednesday-august-26-dow-sp-500-nasdaq-081834782.html"),
 ("NVIDIA — Q2 FY2027 results, SEC filing (revenue, Data Center, EPS, Q3 outlook)","https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm"),
 ("CNBC — Nvidia earnings takeaways: Huang forecasts 70% fiscal 2028 revenue growth","https://www.cnbc.com/2026/08/26/nvidia-nvda-earnings-report-q2-2027-live-updates.html"),
 ("Benzinga — NVDA, CRM, CRWD, OKTA, ANF: 5 Trending Stocks Today","https://www.benzinga.com/markets/equities/26/08/61452319/nvidia-salesforce-crowdstrike-okta-and-abercrombie-fitch-why-these-5-stocks-are-on-investors-radars-today"),
 ("SiliconANGLE — Salesforce scoffs at SaaSpocalypse fears with a crushing earnings beat","https://siliconangle.com/2026/08/26/salesforce-scoffs-at-saaspocalypse-fears-with-a-crushing-earnings-beat/"),
 ("Quartz — Salesforce earnings, revenue forecast, AI/Agentforce","https://qz.com/salesforce-earnings-revenue-forecast-ai-agentforce-082626"),
 ("TheStreet — Stock Market Today (Aug. 26, 2026)","https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-26-2026"),
 ("Trading Economics — US 10 Year Treasury Note Yield","https://tradingeconomics.com/united-states/government-bond-yield"),
 ("Trading Economics — Crude Oil (WTI)","https://tradingeconomics.com/commodity/crude-oil"),
 ("Trading Economics — Federal Funds Target Range, Upper Limit","https://tradingeconomics.com/united-states/federal-funds-target-range--upper-limit-percent-d-na-fed-data.html"),
 ("Federal Reserve — H.15 Selected Interest Rates (Daily), August 26, 2026","https://www.federalreserve.gov/releases/h15/"),
]

ws_body = f"""{mast("The Closing Bell","Your daily markets briefing — the tape, the movers &amp; what moves next")}
<div class="tldr"><b>The Tape</b> <span>{S_WS}</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
{nav("ws")}

<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>
<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{{"symbols":[{{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"}},{{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"}},{{"proName":"FOREXCOM:DJI","title":"Dow 30"}},{{"proName":"NASDAQ:NVDA","title":"NVIDIA"}},{{"proName":"NYSE:CRM","title":"Salesforce"}},{{"proName":"NASDAQ:CRWD","title":"CrowdStrike"}},{{"proName":"NASDAQ:AMD","title":"AMD"}},{{"proName":"NASDAQ:MU","title":"Micron"}},{{"proName":"TVC:USOIL","title":"WTI Crude"}},{{"proName":"TVC:US10Y","title":"US 10Y"}}],"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}}</script></div>

<h2 class="sec">Live Index Quotes — updates in real time</h2>
<div class="tickers">
<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>{{"symbol":"FOREXCOM:SPXUSD","width":"100%","colorTheme":"dark","isTransparent":true,"locale":"en"}}</script></div>
<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>{{"symbol":"FOREXCOM:NSXUSD","width":"100%","colorTheme":"dark","isTransparent":true,"locale":"en"}}</script></div>
<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>{{"symbol":"FOREXCOM:DJI","width":"100%","colorTheme":"dark","isTransparent":true,"locale":"en"}}</script></div>
</div>
<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the latest edition; official closes are in the Weekly Scorecard.</div>

<h2 class="sec">The Lead</h2>
<div class="panel lead">
<span class="tag new">New · 8:06 AM ET</span><span class="tag acc">Pre-open</span>
<h3>Nvidia's blowout quarter puts a bid under tech futures before the open</h3>
<p style="margin:0 0 10px">As of roughly <b>8:06 AM ET</b>, ahead of Thursday's open, <b>S&amp;P 500 and Nasdaq 100 futures were higher while Dow futures slipped</b> after Nvidia's second-quarter report landed Wednesday evening. Bloomberg reported Nasdaq 100 contracts up about <b>1%</b> in early Thursday trade after CFO <b>Colette Kress</b> signalled strong sales growth into fiscal 2028.</p>
<p style="margin:0 0 10px">The quarter itself, from Nvidia's own filing: revenue of <b>$96.2 billion</b>, up <b>106%</b> year over year and <b>18%</b> from the prior quarter; <b>Data Center revenue of $89.0 billion</b>, up <b>117%</b>; GAAP and non-GAAP gross margins both <b>75.0%</b>; and diluted EPS of <b>$2.46 GAAP / $2.22 non-GAAP</b>. Management guided third-quarter revenue to <b>$108 billion, plus or minus 2%</b>, with non-GAAP gross margin near <b>74%</b> — a figure that <b>excludes any Data Center compute revenue from China</b>, where Hopper shipments were under 1% of Data Center revenue in the quarter. CNBC reported CEO <b>Jensen Huang</b> forecasting roughly <b>70% revenue growth in fiscal 2028</b>, well above estimates.</p>
<p style="margin:0">That follows a flat-to-lower Wednesday session: the <b>S&amp;P 500 closed at 7,675.70, down 0.02%</b>, with the <b>Dow off 0.08%</b> and the <b>Nasdaq Composite down 0.16%</b>.</p>
</div>

<h2 class="sec">Movers &amp; Drivers</h2>
<div class="cards">
<div class="card"><span class="tag new">New</span><span class="tag acc">Semis</span>
<h3>Nvidia (NVDA) — up sharply pre-market</h3><p>Two reads this morning, both printed and neither averaged: <b>CNBC has NVDA up 6%</b> in premarket trade, while <b>Benzinga has it up 7.32%</b>. Wednesday evening's first post-call read was "more than 4%" in extended trading. The driver is the $108 billion third-quarter guide and Huang's fiscal-2028 growth comment.</p></div>

<div class="card"><span class="tag new">New</span><span class="tag acc">Software</span>
<h3>Salesforce (CRM) — double-digit after-hours pop</h3><p>Revenue of <b>$11.35 billion</b>, up <b>11%</b> year over year and ahead of a <b>$11.32 billion</b> consensus. Full-year fiscal 2027 revenue guidance was raised to <b>$46.1–$46.4 billion</b> from <b>$45.9–$46.2 billion</b>. Agentforce and Data 360 annual recurring revenue reached nearly <b>$3.9 billion</b>, up more than <b>210%</b>; Agentforce ARR alone topped <b>$1.5 billion</b>, up more than <b>240%</b>. The stock traded to <b>$231.70</b> after hours, <b>+$26.08 / +12.68%</b>; a separate tally put the move at <b>+11.8%</b>.</p></div>

<div class="card"><span class="tag new">New</span><span class="tag acc">Cybersecurity</span>
<h3>CrowdStrike (CRWD) — sharply higher after hours</h3><p>CrowdStrike closed Wednesday at <b>$189.18, up 2.05%</b>, then rose <b>10.49% to $209.02</b> in after-hours trading following its results. HP (HPQ) is also on the earnings watchlist this morning.</p></div>
</div>

<h2 class="sec">Chart of the Day</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{{"symbol":"NASDAQ:NVDA","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}}</script>
</div>
<div class="note">Nvidia is the session's dominant single-stock story after Wednesday evening's report.</div>

<h2 class="sec">Sector Heat — live</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>{{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector","locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}}</script>
</div>
<div class="note">Pre-market activity leaned decisively toward technology and semiconductors on Thursday, on a resurgence in semiconductor demand. No numeric sector or breadth figure is asserted — none was stated in sources seen this run.</div>

<h2 class="sec">The Calendar — live</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en","importanceFilter":"0,1","countryFilter":"us"}}</script>
</div>

<h2 class="sec">Live Market Headlines — updates in real time</h2>
<div class="panel" style="padding:8px">
<script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>{{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":420,"locale":"en"}}</script>
</div>

<h2 class="sec">Weekly Scorecard</h2>
<table><thead><tr><th>Index</th><th>Latest official close</th><th>Change</th><th>Session</th></tr></thead><tbody>
<tr><td>S&amp;P 500</td><td class="mono">7,675.70</td><td class="mono down">−0.02%</td><td>Wed, Aug 26</td></tr>
<tr><td>Dow Jones Industrial Average</td><td class="mono" style="color:var(--mut)">level not corroborated this run</td><td class="mono down">−0.08%</td><td>Wed, Aug 26</td></tr>
<tr><td>Nasdaq Composite</td><td class="mono" style="color:var(--mut)">level not corroborated this run</td><td class="mono down">−0.16%</td><td>Wed, Aug 26</td></tr>
</tbody></table>
<div class="note">A closing set of 7,677.24 / 53,577.40 / 26,151.30 circulated again this run labelled "the August 26 close." It is <b>Tuesday, August 25's</b> close, mislabelled, and is not published here as Wednesday's. Dow and Nasdaq closing <i>levels</i> for August 26 were not corroborated this run, so only the percentage moves are shown.</div>

<h2 class="sec">Rates, Bonds &amp; Commodities</h2>
<table><thead><tr><th>Instrument</th><th>Level</th><th>Context</th></tr></thead><tbody>
<tr><td>US 10-year Treasury yield</td><td class="mono">4.66%</td><td>Thursday pre-market read (Benzinga). It sat at 4.64–4.65% around Aug 25, after a 20-month high of 4.75% on Aug 21 (Trading Economics).</td></tr>
<tr><td>US 2-year Treasury yield</td><td class="mono">4.22%</td><td>Thursday pre-market read (Benzinga).</td></tr>
<tr><td>US 30-year Treasury yield</td><td class="mono" style="color:var(--mut)">not verified this run</td><td>No figure seen in sources fetched this run — none asserted.</td></tr>
<tr><td>Federal funds target range</td><td class="mono">3.50%–3.75%</td><td>Upper limit of 3.75% in August 2026; the range was left unchanged at the July meeting (Trading Economics).</td></tr>
<tr><td>WTI crude</td><td class="mono">$81.36</td><td>Down 1.06% from the previous day on Aug 27 (Trading Economics). Investing.com showed a WTI futures range of $81.44–$82.15.</td></tr>
</tbody></table>

<h2 class="sec">On the Radar</h2>
<div class="panel"><ul class="bul">
<li><b>8:30 AM ET — second-quarter GDP (second estimate), weekly initial jobless claims and second-quarter corporate profits.</b> Consensus figures were not corroborated this run and are not printed.</li>
<li><b>11:00 AM ET — Kansas City Fed manufacturing index for August.</b></li>
<li><b>HP (HPQ)</b> joins Nvidia, Salesforce and CrowdStrike on this week's earnings watchlist.</li>
<li><b>Fed policy.</b> Chair <b>Kevin Warsh</b>'s address at the Jackson Hole symposium was not expected to give clear guidance on the September decision; the target range currently stands at 3.50%–3.75%.</li>
<li><b>Energy and the Gulf.</b> Oil eased after the US tightened sanctions on Iran while refraining from further military threats, and after Iran and Oman reached an agreement over their shares of the Strait of Hormuz's waters and related revenues.</li>
</ul></div>

<footer><b style="color:var(--ink)">Sources</b><ul class="bul">
{"".join(f'<li><a href="{u}">{t}</a></li>' for t,u in ws_sources)}
</ul>
<div class="disc">For information only. Nothing here is investment advice, a recommendation, or an offer to buy or sell any security. Market data shown in live widgets may be delayed.</div></footer>"""

# ================================================================= MMA
mma_css = base_css("#100c0c","#1a1313","#322020","#e84545","#ff8a5c")
mma_sources = [
 ("UFC.com — UFC Fight Night: Nurmagomedov vs Song (UFC Shanghai), Aug 29, 2026","https://www.ufc.com/event/ufc-fight-night-august-29-2026"),
 ("UFC.com — UFC returns to Shanghai with a pivotal bantamweight clash between #3 Umar Nurmagomedov and #5 Song Yadong","https://www.ufc.com/news/ufc-returns-shanghai-pivotal-bantamweight-clash-between-3-umar-nurmagomedov-and-5-song-yadong"),
 ("UFC.com — Fight By Fight Preview | UFC Shanghai","https://www.ufc.com/news/fight-fight-preview-ufc-shanghai-umar-nurmagomedov-vs-song-yadong"),
 ("Yahoo Sports — UFC Shanghai video: Umar Nurmagomedov, Song Yadong have first fight week faceoff","https://sports.yahoo.com/articles/ufc-shanghai-video-umar-nurmagomedov-134031506.html"),
 ("LowKick MMA — Umar Nurmagomedov heavy favourite over Song Yadong ahead of UFC Shanghai","https://www.lowkickmma.com/umar-nurmagomedov-favourite-song-yadong-ufc-shanghai/"),
 ("MMA Odds Breaker — Opening betting odds for UFC Shanghai: Nurmagomedov vs. Song","https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161241-opening-betting-odds-for-ufc-shanghai-nurmagomedov-vs-song/"),
 ("UFC.com — Bonus Coverage | UFC Sacramento","https://www.ufc.com/news/bonus-coverage-ufc-sacramento"),
 ("MMA Mania — Bonuses! Gregory Rodrigues banks bonus $100k for upsetting Anthony Hernandez","https://www.mmamania.com/ufc-bonuses-and-awards/466591/bonuses-gregory-rodrigues-banks-bonus-100k-for-upsetting-anthony-hernandez-ufc-sacramento"),
 ("Yahoo Sports — UFC Fight Of The Night winners hit with 6-month suspension after main event brawl","https://sports.yahoo.com/articles/ufc-results-rodrigues-hernandez-6-231554581.html"),
 ("Wikipedia — UFC 331","https://en.wikipedia.org/wiki/UFC_331"),
 ("Yahoo Sports — UFC 331 fight card revealed, Van vs. Pantoja 2 leads loaded lineup","https://sports.yahoo.com/articles/ufc-331-fight-card-revealed-235537467.html"),
 ("CBS Sports — Dana White's Contender Series 2026 Week 1 results","https://www.cbssports.com/ufc/news/dana-whites-contender-series-2026-week-1-results-winners-contracts-anthony-wint-bilal-hasan/"),
 ("CBS Sports — Dana White's Contender Series 2026 Week 2 results","https://www.cbssports.com/ufc/news/dana-whites-contender-series-2026-week-2-results-winners-contracts-knockouts-highlights/"),
 ("Wikipedia — Dana White's Contender Series season 10","https://en.wikipedia.org/wiki/Dana_White's_Contender_Series_season_10"),
 ("Bloody Elbow — Ex-UFC title challenger survives trend of surprise roster removals by signing new 8-fight deal","https://bloodyelbow.com/2026/08/21/ex-ufc-title-challenger-survives-trend-of-surprise-roster-removals-by-signing-new-8-fight-deal/"),
 ("ESPN — Current and all-time UFC champions","https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions"),
]

mma_body = f"""{mast("The Octagon","Your daily MMA briefing — UFC, prospects &amp; the business of fighting")}
<div class="tldr"><b>Tale of the Tape</b> <span>{S_MM}</span></div>
<div class="freshline" id="freshline">&nbsp;</div>
{nav("mma")}

<div class="cdn"><b>Next card</b> <span>UFC Shanghai · Nurmagomedov vs. Song · Sat, Aug 29 · Shanghai Oriental Sports Center</span> <span id="ufccdn">—</span></div>

<h2 class="sec">Top Story</h2>
<div class="panel" style="border-left:4px solid var(--acc)">
<span class="tag">Carried</span><span class="tag acc">Fight week</span><span class="tag">Bantamweight</span>
<h3 style="margin:2px 0 9px;font-size:20px">Fight week in Shanghai: Umar Nurmagomedov and Song Yadong meet with the next title shot on the line</h3>
<p style="margin:0 0 10px">UFC Fight Night: Nurmagomedov vs. Song takes place <b>Saturday, August 29</b> at the <b>Shanghai Oriental Sports Center</b>, streaming exclusively on <b>Paramount+</b> in the United States. UFC.com frames it as a critical matchup for both men, each looking to head into the final quarter of the year as the clubhouse leader in the chase for the next title opportunity.</p>
<p style="margin:0 0 10px"><b>Umar Nurmagomedov (20-1</b>, fighting out of Dagestan, Russia<b>)</b> is on a two-fight win streak since challenging for the bantamweight title. <b>Song Yadong "The Kung Fu Kid" (23-9-1</b>, fighting out of Heilongjiang, China<b>)</b> makes his sixth main-event appearance following a submission win over former UFC flyweight champion <b>Deiveson Figueiredo</b> at UFC Fight Night Macau in May. The two came face to face on Wednesday at media day.</p>
<p style="margin:0;color:var(--mut);font-size:13.6px"><b>Rankings, unresolved:</b> UFC.com's own preview headline bills the fight as "#3 Umar Nurmagomedov and #5 Song Yadong," while a summary of the same coverage describes them as ranked No. 2 and No. 6 at 135 pounds. Both readings are printed; neither is adopted, and no numeric rank is asserted here for either man.</p>
</div>

<h2 class="sec">Fight Week — Upcoming Cards</h2>
<div class="cards">
<div class="card"><span class="tag acc">Fight week</span><span class="tag">Carried</span>
<div class="mono" style="color:var(--acc2);font-size:12px;letter-spacing:.08em;margin-bottom:6px">SAT AUG 29 · SHANGHAI ORIENTAL SPORTS CENTER</div>
<h3>UFC Fight Night: Nurmagomedov vs. Song</h3>
<p>Bantamweight main event with title-eliminator stakes; Paramount+ exclusive in the US.<br><b>Odds:</b> Nurmagomedov −500 / Song +380 consensus (roughly 80% / 20% implied); DraftKings opened the fight at −470 / +360.</p></div>

<div class="card"><span class="tag">Carried</span><span class="tag acc">Title fight</span>
<div class="mono" style="color:var(--acc2);font-size:12px;letter-spacing:.08em;margin-bottom:6px">SAT SEP 19 · CRYPTO.COM ARENA, LOS ANGELES</div>
<h3>UFC 331: Van vs. Pantoja 2</h3>
<p>Flyweight title rematch between champion <b>Joshua Van</b> and former champion <b>Alexandre Pantoja</b>, whom Van beat by TKO 26 seconds into round one at UFC 323 after Pantoja suffered an arm injury. Co-main: <b>Arman Tsarukyan vs. Mauricio Ruffy</b> over five rounds. Also booked: <b>Marlon Vera vs. Charles Jourdain</b>. Thirteen fights; the UFC's first Los Angeles event since UFC 227 in August 2018.<br><span style="color:var(--mut)">No odds stated in sources seen this run.</span></p></div>

<div class="card"><span class="tag">Carried</span><span class="tag acc">Developmental</span>
<div class="mono" style="color:var(--acc2);font-size:12px;letter-spacing:.08em;margin-bottom:6px">TUESDAYS THROUGH OCTOBER · LAS VEGAS</div>
<h3>Dana White's Contender Series, season 10</h3>
<p>Ten weekly episodes running August through October 2026, airing Tuesday nights exclusively on Paramount+. Week 3's main event paired <b>Bella Mir</b> — daughter of former UFC heavyweight champion Frank Mir — with <b>Alex Apodaca</b> at women's bantamweight.</p></div>
</div>

<h2 class="sec">Last Event — Results</h2>
<div class="note" style="margin:0 0 10px">UFC Fight Night: Hernandez vs. Rodrigues — Saturday, August 22, 2026, Sacramento.</div>
<table><thead><tr><th>Result</th><th>Bout</th><th>Method</th></tr></thead><tbody>
<tr><td class="up"><b>Gregory Rodrigues</b></td><td>def. Anthony Hernandez (main event)</td><td>Unanimous decision (48-47, 49-46, 48-47)</td></tr>
</tbody></table>
<div class="note">Only the main event result was corroborated with scorecards in sources fetched this run; no other bout result is asserted.</div>

<div class="panel" style="margin-top:14px">
<h3 style="margin:0 0 8px;font-size:16px">Performance bonuses — UFC Sacramento</h3>
<ul class="bul">
<li><b>Fight of the Night ($100,000 each):</b> Gregory Rodrigues and Anthony Hernandez.</li>
<li><b>Performance of the Night ($100,000 each):</b> MarQuel Mederos and Carli Judice.</li>
<li><b>$25,000 finish bonuses:</b> Jamall Emmers, Shanelle Dyer, Jackson McVey, Marcio Barbosa, Chris Padilla, Anthony Wint and Reinier de Ridder — fighters who finished their bouts without taking one of the $100,000 awards.</li>
</ul></div>

<h2 class="sec">Prospect Watch</h2>
<div class="cards">
<div class="card"><span class="tag new" style="color:var(--up);border-color:var(--up)">prospect</span><span class="tag">Carried</span>
<h3>Contender Series week 1 — four contracts</h3><p>Live from Las Vegas on <b>August 11</b>: <b>Anthony Wint</b>, <b>Bilal Hasan</b>, <b>Tom Pagliarulo</b> and <b>Joseph Kropschot</b> were awarded UFC contracts. Wint stopped Matt Adams at heavyweight in <b>34 seconds</b>; Hasan finished Mridul Saikia at bantamweight in <b>under a minute</b>.</p></div>

<div class="card"><span class="tag new" style="color:var(--up);border-color:var(--up)">prospect</span><span class="tag">Carried</span>
<h3>Contender Series week 2 — six contracts</h3><p><b>Kaik Brito</b>, <b>Trent Miller</b>, <b>Cristian Pérez</b>, <b>Alik Lorenz</b>, <b>Roman Puga</b> and <b>Taner Trembley</b> earned deals. Lorenz's was the headline result: a stunning upset knockout at light heavyweight.</p></div>

<div class="card"><span class="tag new" style="color:var(--up);border-color:var(--up)">prospect</span><span class="tag">Carried</span>
<h3>Bella Mir headlines week 3</h3><p>The daughter of former UFC heavyweight champion <b>Frank Mir</b> met <b>Alex Apodaca</b> in the women's bantamweight main event of the season's third episode. No result is asserted here — none was stated in sources seen this run.</p></div>
</div>

<h2 class="sec">Around the Sport</h2>
<div class="panel"><ul class="bul">
<li><b>Sacramento's main event ended in a brawl.</b> The Fight of the Night winners were hit with six-month suspensions afterward (Yahoo Sports).</li>
<li><b>Roster churn.</b> Bloody Elbow reported on August 21 that a former UFC title challenger has survived a run of surprise roster removals by signing a new <b>eight-fight deal</b>. No name is asserted here — none appeared in the source text seen this run.</li>
<li><b>Broadcast.</b> Both UFC Shanghai and Contender Series season 10 stream exclusively on <b>Paramount+</b> in the United States.</li>
</ul></div>

<h2 class="sec">Rankings &amp; Business</h2>
<div class="panel">
<p style="margin:0 0 9px"><b>Rankings movement.</b> The only ranking dispute live this run is the Shanghai main event itself: UFC.com bills the fighters as <b>#3 and #5</b> at bantamweight, while a summary of the same coverage puts them at <b>No. 2 and No. 6</b>. Both are recorded; neither is adopted.</p>
<p style="margin:0"><b>Business &amp; broadcast.</b> No viewership, gate or TKO Group financial figure was stated in any source fetched this run, so none is published. UFC Shanghai and Dana White's Contender Series both run on Paramount+ in the US; UFC 331 fills the Crypto.com Arena in Los Angeles on September 19 with a 13-fight card.</p>
</div>

<h2 class="sec">Champions Board</h2>
<table><thead><tr><th>Division</th><th>Champion</th><th>Notes</th></tr></thead><tbody>
<tr><td>Heavyweight</td><td><b>Tom Aspinall</b></td><td>Undisputed since June 21, 2025. <b>Interim:</b> Ciryl Gane (KO2 Alex Pereira, Freedom 250, Jun 14, 2026).</td></tr>
<tr><td>Light Heavyweight</td><td><b>Carlos Ulberg</b></td><td>KO1 Jiří Procházka for the vacant belt, UFC 327, Apr 11, 2026.</td></tr>
<tr><td>Middleweight</td><td><b>Sean Strickland</b></td><td>Split-decision upset of Khamzat Chimaev, UFC 328, May 9, 2026. Two-time champion.</td></tr>
<tr><td>Welterweight</td><td><b>Islam Makhachev</b></td><td>UD Jack Della Maddalena, UFC 322, Nov 15, 2025. One defence — UD Ian Machado Garry, UFC 330, Aug 15, 2026.</td></tr>
<tr><td>Lightweight</td><td><b>Justin Gaethje</b></td><td>TKO4 Ilia Topuria, Freedom 250, Jun 14, 2026.</td></tr>
<tr><td>Featherweight</td><td><b>Alexander Volkanovski</b></td><td>Reclaimed the belt UFC 314, Apr 12, 2025; defended UD over Diego Lopes, UFC 325, Jan 31, 2026.</td></tr>
<tr><td>Bantamweight</td><td><b>Petr Yan</b></td><td>UD Merab Dvalishvili, UFC 323, Dec 6, 2025.</td></tr>
<tr><td>Flyweight</td><td><b>Joshua Van</b></td><td>TKO1 Alexandre Pantoja, UFC 323, Dec 6, 2025; defended TKO5 Tatsuro Taira, UFC 328, May 9, 2026. Rematches Pantoja at UFC 331.</td></tr>
<tr><td>Women's Flyweight</td><td><b>Valentina Shevchenko</b></td><td>&mdash;</td></tr>
<tr><td>Women's Bantamweight</td><td><b>Kayla Harrison</b></td><td>Sub2 Julianna Peña, UFC 316, Jun 7, 2025. Zero defences.</td></tr>
<tr><td>Women's Strawweight</td><td><b>Mackenzie Dern</b></td><td>UD Virna Jandiroba, UFC 321, Oct 25, 2025. One defence — UD Gillian Robertson, UFC 330, Aug 15, 2026.</td></tr>
</tbody></table>
<div class="note">Cross-checked against ESPN's current-champions listing this run and against the most recent completed event (UFC Sacramento, August 22) — no title bout has taken place since, and UFC Shanghai is not a title fight.</div>

<footer><b style="color:var(--ink)">Sources</b><ul class="bul">
{"".join(f'<li><a href="{u}">{t}</a></li>' for t,u in mma_sources)}
</ul>
<div class="disc">Cards and bouts are subject to change. Odds move constantly and are shown as recorded at the time of the source snippet.</div></footer>"""

MMA_JS = """<script>(function(){var el=document.getElementById('ufccdn');if(!el)return;var target=new Date('2026-08-29T00:00:00-04:00');
function tick(){var d=target-new Date();if(d<=0){el.textContent='Fight week — live/completed';return;}
var days=Math.floor(d/86400000),h=Math.floor(d%86400000/3600000),m=Math.floor(d%3600000/60000);
el.textContent=days+'d '+h+'h '+m+'m to fight day (ET)';}
tick();setInterval(tick,30000);})();</script>"""

# ================================================================= INDEX
ix_css = base_css("#0b0c0e","#14161a","#242830","#8ea6c0","#b9cde0") + """
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.big .card{padding:20px 21px;border-radius:15px}
.big .card .lbl{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;font-weight:700}
.big .card h3{font-size:21px;margin:8px 0 9px}
.big .card a.read{display:inline-block;margin-top:12px;font-family:var(--mono);font-size:11.5px;letter-spacing:.11em;text-transform:uppercase;text-decoration:none}
.c-cy{border-left:4px solid #22d3a8} .c-cy .lbl,.c-cy a.read{color:#22d3a8} .c-cy:hover{border-color:#22d3a8}
.c-ws{border-left:4px solid #caa64a} .c-ws .lbl,.c-ws a.read{color:#caa64a} .c-ws:hover{border-color:#caa64a} .c-ws h3{font-family:Georgia,'Times New Roman',serif}
.c-mm{border-left:4px solid #e84545} .c-mm .lbl,.c-mm a.read{color:#ff8a5c} .c-mm:hover{border-color:#e84545}"""

ix_body = f"""{mast("Daily Briefings","Security, markets and the fight game — rebuilt from live sources every 30 minutes")}
<div class="freshline" id="freshline">&nbsp;</div>
{nav("index")}

<div class="big">
<div class="card c-cy"><div class="lbl">⛨ The Cyber Wire · The Wire</div>
<h3>Oracle's CVSS 10.0 WebLogic proxy flaw hits its federal deadline today</h3>
<p>{S_CY}</p>
<a class="read" href="cyber-briefing.html">Read the briefing →</a></div>

<div class="card c-ws"><div class="lbl">▲ The Closing Bell · The Tape</div>
<h3>Nvidia's $96.2bn quarter lifts tech futures before the open</h3>
<p>{S_WS}</p>
<a class="read" href="wallstreet-briefing.html">Read the briefing →</a></div>

<div class="card c-mm"><div class="lbl">⊘ The Octagon · Tale of the Tape</div>
<h3>Shanghai fight week: Nurmagomedov vs. Song for the next title shot</h3>
<p>{S_MM}</p>
<a class="read" href="mma-briefing.html">Read the briefing →</a></div>
</div>

<h2 class="sec">About this page</h2>
<div class="panel"><p style="margin:0;font-size:14.5px">Four pages are rebuilt from scratch on every run: this dashboard and three briefings. Every figure on them is checked against a source fetched during that run, or against a standing sourced correction — anything that cannot be verified is dropped rather than carried. Point-in-time snapshots of each edition are kept in the <a href="archive.html" style="color:var(--acc2)">Archive</a>.</p></div>

<footer><b style="color:var(--ink)">Sources</b> — each briefing carries its own full source list in its footer.
<div class="disc">Informational only. Not investment, legal or security advice.</div></footer>"""

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT,"cyber-briefing.html"),"w").write(page("The Cyber Wire — Daily Briefings", cy_css, cy_body, CY_KEV_JS))
open(os.path.join(OUT,"wallstreet-briefing.html"),"w").write(page("The Closing Bell — Daily Briefings", ws_css, ws_body))
open(os.path.join(OUT,"mma-briefing.html"),"w").write(page("The Octagon — Daily Briefings", mma_css, mma_body, MMA_JS))
open(os.path.join(OUT,"index.html"),"w").write(page("Daily Briefings", ix_css, ix_body))
print("wrote 4 pages")
for f in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]:
    p=os.path.join(OUT,f); print(f, os.path.getsize(p))
