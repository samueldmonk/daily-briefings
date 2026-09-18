# -*- coding: utf-8 -*-
"""Daily Briefings build — Friday 18 September 2026, Afternoon Edition (~5:10 PM ET).
Sixth run of the day. Markets CLOSED at 4:00 PM.
Every string below traces to a source fetched THIS run or a sourced CORRECTIONS.md entry.
"""
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import BASE_CSS, nav, masthead, STAMP_JS, head, FOOT

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- palettes
PAL_CY = """:root{--bg:#080c0c;--panel:#101717;--line:#1d2a2a;--txt:#e7f2f0;--muted:#7d918f;
--accent:#22d3a8;--accent2:#36c6ff;--up:#22c55e;--down:#ef4444;--crit:#ef4444;--warn:#f0b429;
--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}"""

PAL_WS = """:root{--bg:#0d0c09;--panel:#171511;--line:#2e2920;--txt:#f0ece3;--muted:#8d8677;
--accent:#caa64a;--accent2:#e8c766;--up:#4ecb7d;--down:#ff5f56;--crit:#ff5f56;--warn:#e8b64c;
--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
.masthead h1,h2.sec+*.panel h3,.panel h3,.card h3,.lead h3{font-family:Georgia,'Times New Roman',serif}
.masthead h1{font-family:Georgia,'Times New Roman',serif}
.livebar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 8px 4px;margin-bottom:18px}
.livebar-label{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--up);display:flex;align-items:center;gap:8px;padding:4px 8px 8px}
.livebar-label .dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--up)}
.tickers{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:12px;margin-bottom:8px}
.ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 10px}"""

PAL_MMA = """:root{--bg:#100c0c;--panel:#1a1313;--line:#322020;--txt:#f5ecea;--muted:#9a8480;
--accent:#e84545;--accent2:#ff8a5c;--up:#4ecb7d;--down:#ef4444;--crit:#e84545;--warn:#f0b429;
--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
.cdbar{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);
border-radius:10px;padding:11px 15px;margin-bottom:16px;display:flex;flex-wrap:wrap;gap:11px;align-items:baseline}
.cdbar b{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.cdbar .cd{font-family:var(--mono);font-size:15px;color:var(--accent2)}
.cdbar .w{color:var(--muted);font-size:13.5px}"""

PAL_IX = """:root{--bg:#0b0b0d;--panel:#141418;--line:#26262e;--txt:#eceaf0;--muted:#8a8898;
--accent:#9aa0ff;--accent2:#c3b6ff;--up:#22c55e;--down:#ef4444;--crit:#ef4444;--warn:#f0b429;
--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:16px}
.big .card{padding:20px 21px;border-top:3px solid var(--line)}
.big .card.cy{border-top-color:#22d3a8}
.big .card.ws{border-top-color:#caa64a}
.big .card.mm{border-top-color:#e84545}
.big .card .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:9px}
.big .card.cy .k{color:#22d3a8}
.big .card.ws .k{color:#caa64a}
.big .card.mm .k{color:#e84545}
.big .card h3{font-size:21px;margin-bottom:10px}
.big .card.ws h3{font-family:Georgia,'Times New Roman',serif}
.big .card p{font-size:14.5px;line-height:1.55;margin-bottom:13px}
.big .card a.rd{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase}
.big .card.cy a.rd{color:#22d3a8}
.big .card.ws a.rd{color:#caa64a}
.big .card.mm a.rd{color:#e84545}"""

# ---------------------------------------------------------------- summaries
TLDR_CY = ("Two federal patch deadlines land inside twenty-four hours &mdash; the actively exploited "
           "Chrome V8 zero-day CVE-2026-85046 is due today and the CVSS&nbsp;10.0 Cisco ISE bypass "
           "CVE-2026-76460 is due tomorrow &mdash; while the KEV tracker still cannot agree with itself "
           "on whether this week brought eight new exploited flaws or ten.")

TLDR_WS = ("Wall Street closed a volatile, triple-witching week split &mdash; the Nasdaq up 0.39%, the "
           "S&amp;P&nbsp;500 up 0.17% and the Dow down 0.18% &mdash; with the 10-year yield back at 5.00% "
           "and Warren Buffett stepping down as Berkshire chairman.")

TLDR_MMA = ("UFC&nbsp;331 is tomorrow night in Los Angeles with all twenty-four fighters on weight and "
            "Joshua Van a narrow favourite to keep the flyweight belt against Alexandre Pantoja, whose "
            "first meeting ended in twenty-six seconds.")

FRESH = '<div class="freshline" id="freshline">&nbsp;</div>\n'


def meta_block(tldr, accent):
    return ('<div class="tldr" style="border-left-color:%s"><b style="color:%s">%s</b>'
            '<span>%s</span></div>\n' % (accent[0], accent[0], accent[1], tldr))


# ================================================================ CYBER
def build_cyber():
    h = [head("The Cyber Wire &mdash; Daily Briefings", PAL_CY)]
    h.append(masthead("The Cyber Wire",
                      "Your daily cybersecurity briefing &mdash; breaches, exploits &amp; federal deadlines"))
    h.append(meta_block(TLDR_CY, ("#22d3a8", "The Wire")))
    h.append(FRESH)
    h.append(nav("cyber"))

    h.append('<div class="banner"><span class="lvl">Threat level: High</span>'
             '<span>Two CISA-tracked, actively exploited flaws carry federal remediation dates inside a '
             'single day &mdash; the Chrome V8 zero-day <span class="mono">CVE-2026-85046</span>, due '
             '<b id="kevdue">18 September 2026</b>, and the Cisco ISE authentication bypass '
             '<span class="mono">CVE-2026-76460</span> on 19 September &mdash; and a further batch of '
             'newly exploited vulnerabilities landed this week across six vendors.</span></div>\n')

    h.append('<div class="stats">'
             '<div class="stat"><div class="n">8 &rarr; 10</div><div class="l">CVEs added to CISA KEV in the last 7 days &mdash; the tracker&rsquo;s title says eight, its body says ten</div></div>'
             '<div class="stat"><div class="n">47</div><div class="l">New KEV entries in 30 days, one of them tied to ransomware campaigns</div></div>'
             '<div class="stat"><div class="n">12%</div><div class="l">FIRST.org EPSS on GitLab CVE-2026-85706, the highest of this week&rsquo;s batch</div></div>'
             '<div class="stat"><div class="n">6*</div><div class="l">Vendors, by the tracker&rsquo;s own count &mdash; though the ten identifiers it lists span seven distinct vendors</div></div>'
             '</div>\n')

    h.append('<h2 class="sec">Top story</h2>\n')
    h.append('<div class="panel"><h3>A week of KEV additions that the tracker itself cannot count</h3>'
             '<p>Senserva&rsquo;s live exploited-this-week page, fetched in full this run and stamped '
             '<b>updated September 18, 2026</b>, titles itself &ldquo;<b>8 new exploited CVEs</b>&rdquo; and '
             'repeats that figure in its meta description and its opening line &mdash; &ldquo;8 vulnerabilities '
             'crossed from theoretical to confirmed exploited in the wild in the last 7 days, across 6 '
             'vendors.&rdquo; Its own body prose, a few paragraphs down, says CISA &ldquo;confirmed '
             '<b>10 newly exploited vulnerabilities in the last 7 days</b>, after 9 the week before and 23 '
             'across the two weeks before that.&rdquo; It then lists <b>ten identifiers</b>. '
             'This is the <b>third consecutive day</b> this desk has read the page and the contradiction has '
             'not self-corrected.</p>'
             '<p>Both counts are printed here and neither is adopted. What is not in dispute is the shape of '
             'the batch: Google Pixel, two Cisco products, Acronis Backup, two JFrog Artifactory flaws, '
             'ConnectWise ScreenConnect, GitLab and two MikroTik RouterOS bugs. The page names GitLab '
             '<span class="mono">CVE-2026-85706</span> as the likeliest to be attacked next, at a FIRST.org '
             'EPSS of 12% over the next thirty days.</p>'
             '<p class="note">The page carries its own data notice disclaiming accuracy and directing readers '
             'to the authoritative vendor advisory. Where a vendor score was available it is used below; where '
             'none appeared, the cell says so.</p></div>\n')

    h.append('<h2 class="sec">Patch priority</h2>\n')
    h.append('<div class="callout crit"><h3>Patch today &mdash; deadline expires</h3>'
             '<p><b><span class="mono">CVE-2026-85046</span> &mdash; Google Chrome, V8 JavaScript and '
             'WebAssembly engine.</b> A high-severity <b>type confusion</b> flaw: crafted HTML or JavaScript '
             'makes V8 mishandle memory object types, yielding arbitrary read/write and, ultimately, '
             'attacker-controlled code execution inside the browser sandbox. <b>CVSS 8.8</b>, exploited in the '
             'wild before the fix. Patched in the 3 September stable-channel update &mdash; <b>Chrome '
             '152.0.7977.82/.83</b> on Windows and macOS, <b>152.0.7977.82</b> on Linux. CISA added it to the '
             'Known Exploited Vulnerabilities catalog within hours of Google&rsquo;s advisory and set federal '
             'civilian agencies a remediation date of <b>18 September 2026</b> &mdash; '
             '<span id="cd1" class="mono">&nbsp;</span>. The Cisco date shown in the KEV section below is a '
             'separate, later deadline and is labelled as such.</p>'
             '<p class="note">Provenance, stated plainly: the CVSS score, the exploited-in-the-wild status, the '
             'fixed build strings and the 18 September federal date all come from <i>secondary</i> reporting '
             'read this run (Help Net Security, SOC Prime, tech-insider.org, Security Affairs). '
             '<b>cisa.gov&rsquo;s own alert page returned an empty body for a fifth consecutive run</b>, so the '
             'date has not been read from the catalog itself. Sources also disagree on whether this is the '
             '<b>sixth</b> or the <b>seventh</b> actively exploited Chrome zero-day of 2026 &mdash; both counts '
             'appear in results read this run and neither is adopted here.</p></div>\n')

    h.append('<h2 class="sec">Threat actor spotlight</h2>\n')
    h.append('<div class="panel"><h3>Settra</h3>'
             '<p>The Settra ransomware crew accounts for four separate victim listings surfaced this run, '
             'spread across three countries and three unrelated sectors: <b>Hansler Smith Limited</b> '
             '(Canada, 4 September), <b>Teletek Structures Inc.</b> (Canadian cell-tower construction), '
             '<b>MedEvolve</b> (US medical billing) and <b>DiaSorin S.p.A.</b> (Italian biotechnology). In each '
             'case the group threatens to leak stolen data unless a settlement is reached, and in each case '
             'negotiations are described as unresolved.</p>'
             '<p>Every one of those four is an <b>attacker claim on a leak site</b>, not a confirmed or '
             'victim-acknowledged breach, and is labelled that way here. No record counts, ransom demands or '
             'dollar figures were stated in anything read this run, so none are published. This desk&rsquo;s '
             'standing ledger separately records Settra abusing the legitimate <b>MeshAgent</b> remote-monitoring '
             'agent for persistence.</p></div>\n')

    h.append('<h2 class="sec">Breaches &amp; incidents</h2>\n')
    h.append('<div class="cards">'
             '<div class="card"><div class="tags"><span class="t hot">Public sector</span><span class="t">Data theft</span></div>'
             '<h3>Florida DMV breach disclosed by ShinyHunters</h3>'
             '<p>A data breach involving the State of Florida DMV was disclosed by ShinyHunters on '
             '<b>16 September 2026</b>. No record count appeared in anything read this run and none is published.</p></div>'
             '<div class="card"><div class="tags"><span class="t">Law enforcement</span><span class="t hot">Scattered Spider</span></div>'
             '<h3>Scattered Spider member pleads guilty</h3>'
             '<p><b>Ahmed Elbadawy</b> of Texas, an accused Scattered Spider member, pleaded guilty to wire fraud '
             'conspiracy and identity theft charges tied to attacks against dozens of organisations, resulting in '
             'the sale of stolen sensitive data and the theft of cryptocurrency worth millions.</p></div>'
             '<div class="card"><div class="tags"><span class="t">Cloud credentials</span></div>'
             '<h3>Mass scanning of exposed Vite dev servers</h3>'
             '<p>A mass-scanning campaign is targeting <b>Vite</b> deployments to extract cloud credentials from '
             'exposed development servers, disclosed <b>15 September 2026</b>. Separately, credential-harvesting '
             'activity observed in <b>August 2026</b> leveraged <span class="mono">CVE-2026-39364</span> '
             '(<b>CVSS 8.2</b>) in Vite, which lets an unauthenticated attacker bypass security restrictions via '
             'query-parameter manipulation and leak sensitive data.</p></div>'
             '<div class="card"><div class="tags"><span class="t">Fraud</span><span class="t">Identity</span></div>'
             '<h3>Microsoft on abused email infrastructure and passkey lures</h3>'
             '<p>Microsoft disclosed details of campaigns in which threat actors abuse <b>third-party email '
             'delivery infrastructure</b> to blast financial-fraud scam messages, and use '
             '<b>passkey-themed social engineering</b> to breach cloud environments.</p></div>'
             '<div class="card"><div class="tags"><span class="t">Container escape</span><span class="t">macOS</span></div>'
             '<h3>Docker Sandboxes guest escape on macOS</h3>'
             '<p>Docker warned that malicious code running inside a <b>Docker Sandboxes</b> virtual machine on '
             'macOS could escape the shared project directory and read or change files on the host.</p></div>'
             '</div>\n')
    h.append('<p class="note"><b>This desk carries zero New tags this edition.</b> The tag is drafted last and only '
             'survives if the string returns zero hits when grepped against every prior archived snapshot on this '
             'site &mdash; and every candidate had prior hits: <span class="mono">Vite</span> 9, '
             '<span class="mono">CVE-2026-39364</span> 7, <span class="mono">CVE-2026-85046</span> 89, '
             '<span class="mono">152.0.7977</span> 46, &ldquo;Salvatore Gulizia&rdquo; 39, '
             '&ldquo;passkey-themed&rdquo; 14, &ldquo;Settra&rdquo; 4, &ldquo;MedEvolve&rdquo; 3, '
             '&ldquo;Elbadawy&rdquo; 2. Zero is a publishable answer.</p>\n')

    h.append('<h2 class="sec">Vulnerability watch</h2>\n')
    rows = [
        ("CVE-2026-85046", "8.8", "Google Chrome (V8 engine)",
         "Type confusion; exploited in the wild before the fix. Chrome 152.0.7977.82/.83 Win/macOS, 152.0.7977.82 Linux."),
        ("CVE-2026-76460", "10.0", "Cisco Identity Services Engine / ISE-PIC",
         "Incorrect use of privileged APIs &rarr; authentication bypass. Exploited in the wild; emergency fixes issued."),
        ("CVE-2026-85706", "10.0", "GitLab Community &amp; Enterprise Edition",
         "Path traversal. EPSS 12% &mdash; the highest of this week&rsquo;s batch."),
        ("CVE-2026-84869", "9.9", "ConnectWise ScreenConnect",
         "Improper privilege management and missing authorisation."),
        ("CVE-2026-76461", "9.8", "Cisco Secure Email Gateway (AsyncOS)",
         "SQL injection; unauthenticated remote attacker can run commands as root on the underlying OS."),
        ("CVE-2026-91843", "9.8", "Check Point Security Management &amp; Log Servers",
         "Pre-auth stack overflow in login &rarr; code execution as root. Check Point&rsquo;s own rating."),
        ("CVE-2026-42016", "8.8", "JFrog Artifactory", "Incorrect authorisation."),
        ("CVE-2026-58704", "8.8", "Google Pixel", "Improper authorisation."),
        ("CVE-2026-39364", "8.2", "Vite",
         "Security-restriction bypass via query-parameter manipulation; used in August 2026 credential harvesting."),
        ("CVE-2026-42018", "7.5", "JFrog Artifactory", "Improper authentication."),
        ("CVE-2026-87886", "7.8", "Acronis Backup", "Incorrect default permissions."),
        ("CVE-2026-67277", "not stated", "MikroTik RouterOS",
         "Missing authentication for critical function. No CVSS appeared on the tracker."),
        ("CVE-2026-86060", "not stated", "MikroTik RouterOS",
         "Improper neutralisation of argument delimiters in a command. No CVSS appeared on the tracker."),
    ]
    h.append('<div class="panel" style="padding:4px 6px"><table><tr><th>CVE</th><th>CVSS</th>'
             '<th>Affected</th><th>Note</th></tr>')
    for c, s, a, n in rows:
        cls = ' class="down"' if s not in ("not stated",) and float(s) >= 9.8 else ""
        sv = s if s == "not stated" else s
        h.append('<tr><td class="mono">%s</td><td%s class="mono">%s</td><td>%s</td><td>%s</td></tr>'
                 % (c, cls, sv, a, n))
    h.append('</table></div>\n')
    h.append('<p class="note">Scores are the vendor&rsquo;s or CISA&rsquo;s where one was published. Two MikroTik '
             'rows carry &ldquo;not stated&rdquo; because no score appeared anywhere read this run, and a blank is '
             'more honest than a borrowed number. Two rows sit <i>outside</i> this week&rsquo;s KEV batch and are '
             'included because they are live and unpatched in many estates rather than because CISA added them: '
             '<span class="mono">CVE-2026-91843</span> (Check Point) and <span class="mono">CVE-2026-39364</span> '
             '(Vite). Neither carries a federal deadline here.</p>\n')

    h.append('<h2 class="sec">CISA KEV &amp; federal deadlines</h2>\n')
    h.append('<ul class="bul">'
             '<li><b class="mono">CVE-2026-85046</b> &mdash; Google Chrome V8 zero-day. Added to KEV within hours '
             'of Google&rsquo;s 3 September advisory; federal remediation date <b>18 September 2026</b> '
             '<span id="cd2" class="mono"></span>. <b>This is the deadline used by the Patch Priority box and the '
             'threat banner above</b>, and it is the same date in all three places.</li>'
             '<li><b class="mono">CVE-2026-76460</b> &mdash; Cisco Identity Services Engine / ISE-PIC, CVSS 10.0, '
             'exploited in the wild. Added to KEV <b>16 September</b> (confirmed from CISA&rsquo;s own alert index '
             'in a prior run), with a remediation date of <b>19 September 2026</b> '
             '<span id="cd3" class="mono"></span>. That date is <i>carried from this desk&rsquo;s standing ledger</i> '
             'and was not re-fetched: cisa.gov returned an empty body again. A later deadline than the Chrome one, '
             'and deliberately kept distinct from it.</li>'
             '<li><b class="mono">CVE-2026-87886</b> &mdash; Acronis Backup, incorrect default permissions, CVSS 7.8. '
             'Added the same day as the Cisco flaw. <b>No due date has been confirmed for it and none is asserted here.</b></li>'
             '<li>Earlier additions in the chain included: <b>11 September</b> &mdash; GitLab '
             '<span class="mono">CVE-2026-85706</span> and ConnectWise ScreenConnect '
             '<span class="mono">CVE-2026-84869</span>, whose 14 September deadline has already passed. '
             '<b>8 September</b> &mdash; four flaws: Adobe Commerce/Magento '
             '<span class="mono">CVE-2026-75650</span>, two Windows bugs '
             '<span class="mono">CVE-2026-81963</span> and <span class="mono">CVE-2026-85880</span>, and N-able '
             'N-central <span class="mono">CVE-2026-86218</span>. <b>2 September</b> &mdash; seven flaws.</li>'
             '<li>The governing directive for these dates is <b>BOD 26-04</b>, &ldquo;Prioritizing Security Updates '
             'Based on Risk&rdquo;, which sets per-vulnerability remediation dates rather than the flat three-week '
             'window of the older directive it replaced.</li>'
             '</ul>\n')

    h.append('<h2 class="sec">Sources</h2>\n')
    h.append('<div class="panel"><p class="srcs">'
             '<a href="https://senserva.com/exploited-this-week.html">senserva.com/exploited-this-week.html</a> &middot; '
             '<a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">cisa.gov/known-exploited-vulnerabilities-catalog</a> &middot; '
             '<a href="https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog">cisa.gov &mdash; 16 Sep KEV additions (empty body on fetch)</a> &middot; '
             '<a href="https://www.cisa.gov/news-events/alerts/2026/09/08/cisa-adds-four-known-exploited-vulnerabilities-catalog">cisa.gov &mdash; 8 Sep KEV additions</a> &middot; '
             '<a href="https://www.helpnetsecurity.com/2026/09/04/google-chrome-zero-day-cve-2026-85046/">helpnetsecurity.com &mdash; Chrome zero-day CVE-2026-85046</a> &middot; '
             '<a href="https://socprime.com/blog/cve-2026-85046-analysis/">socprime.com &mdash; CVE-2026-85046 analysis</a> &middot; '
             '<a href="https://securityaffairs.com/198757/security/google-fixes-the-seventh-actively-exploited-chrome-zero-day-of-2026.html">securityaffairs.com &mdash; Chrome zero-day count</a> &middot; '
             '<a href="https://thehackernews.com/">thehackernews.com</a> &middot; '
             '<a href="https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html">thehackernews.com &mdash; Chrome V8 update</a> &middot; '
             '<a href="https://www.cyfirma.com/news/weekly-intelligence-report-04-sep-2026/">cyfirma.com &mdash; weekly intelligence report, 4 Sep</a> &middot; '
             '<a href="https://www.wiu.edu/cybersecuritycenter/cybernews.php">wiu.edu &mdash; cybersecurity news roll-up</a>'
             '</p></div>\n')

    h.append('<p class="disc">Information only. Severity scores, affected versions and remediation dates change; '
             'verify against the vendor advisory and the CISA KEV catalog before acting. Where a figure could not '
             'be confirmed from a source read this run, it has been omitted or the gap stated in place.</p>\n')

    h.append("""<script>(function(){try{
var due=new Date('2026-09-18T23:59:59-04:00');var cis=new Date('2026-09-19T23:59:59-04:00');
function lbl(d){var ms=d-new Date();if(ms<=0)return'(overdue)';var days=Math.floor(ms/86400000);
if(days<=0)return'(due today)';return'('+days+(days===1?' day left)':' days left)');}
function paint(id,d){var e=document.getElementById(id);if(!e)return;var s=lbl(d);e.textContent=s;
if(s==='(overdue)'||s==='(due today)'){e.style.color='var(--crit)';}}
paint('cd1',due);paint('cd2',due);paint('cd3',cis);
}catch(e){}})();</script>\n""")
    h.append(FOOT % STAMP_JS)
    io.open(os.path.join(OUT, "cyber-briefing.html"), "w", encoding="utf-8").write("".join(h))


# ================================================================ WALL STREET
TAPE = ('<script src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>'
        '{"symbols":[{"proName":"FOREXCOM:SPXUSD","title":"S&P 500"},{"proName":"FOREXCOM:NSXUSD","title":"Nasdaq 100"},'
        '{"proName":"FOREXCOM:DJI","title":"Dow 30"},{"proName":"NASDAQ:XENE","title":"Xenon"},'
        '{"proName":"NASDAQ:NFLX","title":"Netflix"},{"proName":"NYSE:BRK.A","title":"Berkshire"},'
        '{"proName":"NASDAQ:COIN","title":"Coinbase"},{"proName":"NASDAQ:MSTR","title":"Strategy"},'
        '{"proName":"TVC:USOIL","title":"WTI Crude"},{"proName":"TVC:US10Y","title":"US 10Y"}],'
        '"colorTheme":"dark","isTransparent":true,"showSymbolLogo":true,"displayMode":"adaptive","locale":"en"}</script>')


def sq(sym):
    return ('<div class="ticker"><script src="https://s3.tradingview.com/external-embedding/'
            'embed-widget-single-quote.js" async>{"symbol":"%s","width":"100%%","colorTheme":"dark",'
            '"isTransparent":true,"locale":"en"}</script></div>' % sym)


def build_ws():
    h = [head("The Closing Bell &mdash; Daily Briefings", PAL_WS)]
    h.append(masthead("The Closing Bell",
                      "Your daily markets briefing &mdash; the tape, the drivers &amp; what&rsquo;s next"))
    h.append(meta_block(TLDR_WS, ("#caa64a", "The Tape")))
    h.append(FRESH)
    h.append(nav("ws"))

    h.append('<div class="livebar"><div class="livebar-label"><span class="dot"></span> LIVE QUOTES</div>%s</div>\n' % TAPE)

    h.append('<h2 class="sec">Live index quotes &mdash; updates in real time</h2>\n')
    h.append('<div class="tickers">%s%s%s</div>\n'
             % (sq("FOREXCOM:SPXUSD"), sq("FOREXCOM:NSXUSD"), sq("FOREXCOM:DJI")))
    h.append('<div class="note">Quotes stream live (some feeds ~15-min delayed). Editorial below reflects the '
             'latest edition; official closes are in the Weekly Scorecard.</div>\n')

    h.append('<h2 class="sec">The lead</h2>\n')
    h.append('<div class="panel"><h3>A split close to a triple-witching week, and Buffett hands over the chair</h3>'
             '<p>Wall Street finished Friday divided. The <b>Nasdaq Composite closed up 0.39% at 26,522.55</b>, a '
             'gain of 104.25 points; the <b>S&amp;P 500 rose 0.17% to 7,650.50</b>; and the '
             '<b>Dow Jones Industrial Average shed 95.40 points, or 0.18%, to 51,682.64</b>. The session wrapped a '
             'volatile week in which traders absorbed the Federal Reserve&rsquo;s first rate increase in three '
             'years, a 10-year Treasury yield back at the 5% line, and elevated oil.</p>'
             '<p>It was also <b>triple witching</b> &mdash; the quarterly simultaneous expiry of index futures, '
             'index options and single-stock options. Citadel Securities data as of 16 September, cited by EBC '
             'Financial Group, put roughly <b>$7 trillion</b> of US equity options notional exposure expiring on '
             'the day, about <b>25% of total US options exposure</b> and, on that reckoning, the '
             '<b>second-largest expiration on record</b>. TheStreet Pro&rsquo;s James &ldquo;Rev Shark&rdquo; '
             'DePorre had flagged it in advance: expirations of that size &ldquo;tend to produce heavy volume and '
             'sharp swings, particularly in the final hour.&rdquo;</p>'
             '<p>The day&rsquo;s other story came from Omaha. <b>Warren Buffett, 96, stepped down as chairman of '
             'Berkshire Hathaway</b>, becoming chairman emeritus while remaining a director. <b>Howard Buffett</b> '
             'takes the chair and <b>Susan Decker</b> becomes lead independent director, a little more than nine '
             'months after <b>Greg Abel, 64</b>, became chief executive. &ldquo;Father Time always wins,&rdquo; '
             'Buffett said. &ldquo;He has, however, been generous with me.&rdquo; No verified percentage move for '
             'Berkshire stock appeared in anything read this run, so none is published.</p>'
             '<p class="note">The closing levels are admitted because all three reconcile against independently '
             'sourced prior closes. S&amp;P: 7,650.50 against Thursday&rsquo;s 7,637.72 is +12.78, or +0.167%. '
             'Nasdaq: 26,522.55 against 26,418.30 is +104.25, or +0.395%. Dow: &minus;95.40 on 51,682.64 is '
             '&minus;0.184%. One unsmoothed wrinkle &mdash; the Dow&rsquo;s implied prior close of <b>51,778.04</b> '
             'sits <b>1.81 points</b> below the 51,779.85 this desk recorded for Thursday. The gap is printed '
             'rather than split, and it is far too small to move the direction or the percentage.</p></div>\n')

    h.append('<h2 class="sec">Movers &amp; drivers</h2>\n')
    h.append('<div class="cards">'
             '<div class="card"><div class="tags"><span class="t hot">Biggest decliner</span><span class="t new">New</span></div>'
             '<h3>Xenon Pharmaceuticals &mdash; good news buried by a safety pause</h3>'
             '<p>Xenon submitted a <b>New Drug Application to the FDA for azetukalner</b> in focal seizures, '
             'resting on the Phase 2b <b>X-TOLE</b> and Phase 3 <b>X-TOLE2</b> studies, in which all four '
             'evaluated doses cut monthly seizure frequency significantly against placebo. It was overwhelmed by '
             'the second announcement: a <b>voluntary pause on new patient enrolment in the ongoing depression '
             'studies</b> after reports of <b>neuropsychiatric adverse events</b>. Shares fell about <b>26% in '
             'premarket trade, to $42.30</b>. This desk separately logged the stock down about <b>29.1%</b> at '
             '<b>11:44 AM ET</b>; no verified closing percentage for it appeared in anything read this run.</p></div>'
             '<div class="card"><div class="tags"><span class="t gold">Analyst moves</span><span class="t new">New</span></div>'
             '<h3>Three price targets cut on the same name</h3>'
             '<p>Deutsche Bank&rsquo;s <b>David Hoang</b> downgraded Xenon from Buy to Hold and cut the target '
             'from <b>$90 to $46</b>. Baird&rsquo;s <b>Brian Skorney</b> kept Outperform but trimmed from '
             '<b>$97 to $90</b>. Needham&rsquo;s <b>Serge Belanger</b> kept Buy and moved from <b>$78 to $60</b>. '
             'A separate Benzinga analyst note argued the share reaction was overblown.</p></div>'
             '<div class="card"><div class="tags"><span class="t hot">Decliner</span></div>'
             '<h3>Netflix slid at the open</h3>'
             '<p>Netflix fell about <b>5%</b> as the Dow opened roughly <b>90 points lower</b>. Both figures are '
             '<b>opening-bell prints</b>, explicitly labelled as such, not closing moves &mdash; no verified '
             'closing percentage for the stock appeared in anything read this run.</p></div>'
             '<div class="card"><div class="tags"><span class="t pro">Advancers</span></div>'
             '<h3>Crypto-linked equities rose across the board</h3>'
             '<p>Cryptocurrency-related shares gained broadly after the <b>SEC announced an innovation exemption '
             'for tokenized securities</b>. Intraday winners logged by this desk at 12:26 PM ET included '
             '<b>ALMR +15.87%, MSTR +13.14%, COIN +11.58%, MARA +10.22%, BitMine +7.92%, HOOD +7.87%</b> and '
             '<b>Galaxy +7.59%</b>. Three different causal framings for the same rally appeared in one live blog '
             '&mdash; the SEC exemption, the Senate <i>failing</i> to pass crypto legislation, and '
             '&ldquo;legislative progress in the U.S. House&rdquo; &mdash; and none is adjudicated here.</p></div>'
             '</div>\n')
    h.append('<p class="note"><b>Two New tags on this desk, both on the Xenon block.</b> Grepped against every '
             'prior archived snapshot on this site, &ldquo;X-TOLE2&rdquo;, &ldquo;neuropsychiatric&rdquo;, '
             '&ldquo;New Drug Application&rdquo;, &ldquo;$42.30&rdquo; and the three analyst names Hoang, Skorney '
             'and Belanger all return <b>zero</b> hits, so the NDA filing, the safety pause and the target cuts are '
             'genuinely first-published here. &ldquo;Citadel Securities&rdquo; also returns zero, but it sits inside '
             'The Lead rather than on a taggable card. The Weekly Scorecard is <b>not</b> tagged: '
             '&ldquo;7,650.50&rdquo; and &ldquo;51,682.64&rdquo; each return one prior hit &mdash; this '
             'afternoon&rsquo;s earlier edition, which published the same close.</p>\n')

    h.append('<h2 class="sec">Chart of the day &mdash; Xenon Pharmaceuticals</h2>\n')
    h.append('<div class="panel" style="padding:8px">'
             '<script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>'
             '{"symbol":"NASDAQ:XENE","width":"100%","height":240,"locale":"en","dateRange":"1D",'
             '"colorTheme":"dark","isTransparent":true,"autosize":false}</script></div>\n')

    h.append('<h2 class="sec">Sector heat &mdash; live</h2>\n')
    h.append('<div class="panel" style="padding:8px">'
             '<script src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>'
             '{"dataSource":"SPX500","blockSize":"market_cap_basic","blockColor":"change","grouping":"sector",'
             '"locale":"en","colorTheme":"dark","hasTopBar":false,"isDataSetEnabled":false,"isZoomEnabled":true,'
             '"hasSymbolTooltip":true,"isMonoSize":false,"width":"100%","height":420}</script></div>\n')
    h.append('<p class="note"><b>No same-session sector percentages are published this run.</b> The sector figures '
             'that surfaced were year-to-date and trailing-month returns (energy leading the year, technology and '
             'financial sector ETFs quoted without a session stamp), not 18 September moves. Rather than relabel a '
             'monthly number as a daily one &mdash; the exact failure this desk caught on the index close earlier '
             'today &mdash; the live heatmap above is left to speak for itself. No VIX reading is published either: '
             'none was re-fetched this run.</p>\n')

    h.append('<h2 class="sec">The calendar &mdash; live</h2>\n')
    h.append('<div class="panel" style="padding:8px">'
             '<script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>'
             '{"colorTheme":"dark","isTransparent":true,"width":"100%","height":420,"locale":"en",'
             '"importanceFilter":"0,1","countryFilter":"us"}</script></div>\n')

    h.append('<h2 class="sec">Live market headlines &mdash; updates in real time</h2>\n')
    h.append('<div class="panel" style="padding:8px">'
             '<script src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>'
             '{"feedMode":"market","market":"stock","colorTheme":"dark","isTransparent":true,'
             '"displayMode":"regular","width":"100%","height":420,"locale":"en"}</script></div>\n')

    h.append('<h2 class="sec">After-hours movers</h2>\n')
    h.append('<div class="panel"><p><b>No after-hours moves are published this evening.</b> No after-hours board '
             'carrying an 18 September stamp was sourced this run.</p>'
             '<p class="note">One trap is worth naming because it would have fitted the day&rsquo;s lead too '
             'neatly. A Benzinga headline reading &ldquo;Xenon Pharmaceuticals shares fall 25% after hours&rdquo; '
             'describes the <b>17 September</b> after-hours session, when the company&rsquo;s announcements first '
             'landed &mdash; the same 25%-ish figure that a stale after-hours board has been showing this desk for '
             'two consecutive runs. It is not tonight&rsquo;s move, and publishing it beside today&rsquo;s '
             'Xenon story would have read as confirmation of something never verified.</p></div>\n')

    h.append('<h2 class="sec">Weekly scorecard</h2>\n')
    h.append('<div class="panel" style="padding:4px 6px"><table>'
             '<tr><th>Session</th><th>S&amp;P 500</th><th>Nasdaq Composite</th><th>Dow 30</th></tr>'
             '<tr><td>Mon 14 Sep</td><td class="mut">Not re-verified this run</td><td class="mut">Not re-verified this run</td><td class="mut">Not re-verified this run</td></tr>'
             '<tr><td>Tue 15 Sep</td><td class="mut">Not re-verified this run</td><td class="mut">Not re-verified this run</td><td class="mut">Not re-verified this run</td></tr>'
             '<tr><td>Wed 16 Sep</td><td class="mut">Not re-verified this run</td><td class="mut">Not re-verified this run</td><td class="mut">Not re-verified this run</td></tr>'
             '<tr><td>Thu 17 Sep</td><td class="mono">7,637.72</td><td class="mono">26,418.30</td><td class="mono">51,779.85</td></tr>'
             '<tr><td><b>Fri 18 Sep</b></td>'
             '<td class="mono up"><b>7,650.50</b> &nbsp;+0.17%</td>'
             '<td class="mono up"><b>26,522.55</b> &nbsp;+104.25 &nbsp;+0.39%</td>'
             '<td class="mono down"><b>51,682.64</b> &nbsp;&minus;95.40 &nbsp;&minus;0.18%</td></tr>'
             '</table></div>\n')
    h.append('<p class="note">Monday through Wednesday were not re-fetched this run and are left blank rather than '
             'carried forward from memory. Thursday&rsquo;s three levels come from this desk&rsquo;s standing ledger, '
             'where each was sourced separately; they are shown because they are the denominators that make '
             'Friday&rsquo;s percentages checkable, and the 1.81-point Dow discrepancy they expose is described in '
             'The Lead above rather than hidden. Friday&rsquo;s close was refused by four consecutive editions '
             'earlier today &mdash; a search summary kept presenting the 9:32 AM opening-bell print as the close '
             '&mdash; and was first published by this afternoon&rsquo;s fifth edition once a third independent '
             'prior close made the arithmetic a real check. It is re-verified here.</p>\n')

    h.append('<h2 class="sec">Rates, bonds &amp; commodities</h2>\n')
    h.append('<div class="panel" style="padding:4px 6px"><table>'
             '<tr><th>Instrument</th><th>Level</th><th>Change</th><th>Note</th></tr>'
             '<tr><td>US 10-year Treasury yield</td><td class="mono">5.00%</td><td class="mono up">+0.07 pp (~7 bp)</td>'
             '<td>Trading Economics, dated 18 September. Up 0.35 pp on the month and 0.87 pp on the year; near its '
             'highest since July 2007.</td></tr>'
             '<tr><td>Fed funds target</td><td class="mono">3.75% &ndash; 4.00%</td><td class="mono">+25 bp</td>'
             '<td>Raised in mid-September &mdash; the first increase in three years. Chair Kevin Warsh has said '
             'inflation remains elevated; FOMC projections point to one or two further hikes by next year.</td></tr>'
             '<tr><td>WTI crude</td><td class="mono">$100.30</td><td class="mono down">&minus;1.6%</td>'
             '<td>Settlement, per CNBC&rsquo;s 18 September oil report.</td></tr>'
             '<tr><td>Brent crude</td><td class="mono">$103.87</td><td class="mono down">&minus;0.9%</td>'
             '<td>Settlement, same report.</td></tr>'
             '</table></div>\n')
    h.append('<p class="note">Two divergences are printed rather than reconciled. <b>Oil:</b> the settlement figures '
             'above disagree with a Trading Economics board this desk read at about 4:07 PM ET, which showed WTI near '
             '$99.5 and down about 2.3&ndash;2.4%. Oil reversed more than once during the session &mdash; down on '
             'Saudi loading via Oman and product builds in the morning, up after a tanker was struck in the Strait of '
             'Hormuz in the afternoon &mdash; and the two reads are consistent with a whipsaw, but they are not the '
             'same number and neither is presented as the other. <b>The 10-year:</b> Trading Economics prints 5.00% '
             'while a second write-up of the same session printed <b>4.996%</b>. Both appear here; the difference is '
             'four-thousandths of a point and nothing on this page turns on it. Where a change is coloured, the colour '
             'follows the sign of that change &mdash; green for up, red for down &mdash; for yields and commodities '
             'alike; the policy-rate row is left uncoloured because a target range is not a market move.</p>\n')

    h.append('<h2 class="sec">On the radar</h2>\n')
    h.append('<ul class="bul">'
             '<li><b>Monday&rsquo;s index reshuffles take effect.</b> SpaceX&rsquo;s Nasdaq-100 weighting moves to '
             'roughly <b>2.82%</b> from about <b>1.28%</b> at Friday&rsquo;s close, with <b>$15.5&ndash;22 billion</b> '
             'of programmatic buying attributed to Investing.com, effective <b>Monday 21 September</b>. '
             '<b>SanDisk (SNDK)</b> joins the S&amp;P 100 the same day.</li>'
             '<li><b>The rate path.</b> With the funds target at 3.75&ndash;4.00% after the first hike in three years '
             'and FOMC projections pointing to one or two more, the 10-year&rsquo;s behaviour around the 5% line is '
             'the number to watch next week.</li>'
             '<li><b>Oil as the inflation input.</b> Yields climbed this week on speculation that elevated energy '
             'costs feed inflation and therefore further tightening. Friday&rsquo;s two-way action in crude, and the '
             'Strait of Hormuz tanker strike behind the afternoon bounce, keep that channel open.</li>'
             '<li><b>Post-expiry positioning.</b> Roughly a quarter of total US options exposure rolled off on '
             'Friday. Where dealers re-hedge into the new cycle is the first thing Monday&rsquo;s tape will show.</li>'
             '</ul>\n')

    h.append('<h2 class="sec">Sources</h2>\n')
    h.append('<div class="panel"><p class="srcs">'
             '<a href="https://www.cnbc.com/2026/09/17/stock-market-today-live-updates.html">cnbc.com &mdash; stock market news for Sept. 18, 2026</a> &middot; '
             '<a href="https://www.cnbc.com/2026/09/18/oil-prices-today-brent-wti-saudi-arabia-houthi.html">cnbc.com &mdash; oil prices today</a> &middot; '
             '<a href="https://tradingeconomics.com/united-states/government-bond-yield">tradingeconomics.com &mdash; US 10-year yield</a> &middot; '
             '<a href="https://tradingeconomics.com/commodity/crude-oil">tradingeconomics.com &mdash; crude oil</a> &middot; '
             '<a href="https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-18-2026">thestreet.com &mdash; market live blog, 18 Sep</a> &middot; '
             '<a href="https://www.ebc.com/forex/september-triple-witching-2026-fed-boj-expiry">ebc.com &mdash; September triple witching 2026</a> &middot; '
             '<a href="https://invezz.com/news/2026/09/18/dow-opens-90-pts-lower-as-buffett-steps-down-netflix-stock-slides-5/">invezz.com &mdash; Buffett steps down, Netflix slides</a> &middot; '
             '<a href="https://news.futunn.com/en/post/79481545/us-stock-market-preview-triple-witching-day-is-upon-us">futunn.com &mdash; US stock market preview</a> &middot; '
             '<a href="https://www.benzinga.com/analyst-stock-ratings/analyst-color/26/09/61872335/xenon-stock-reaction-is-overblown-analyst">benzinga.com &mdash; Xenon reaction overblown</a> &middot; '
             '<a href="https://www.gurufocus.com/news/9087886/xenon-pharmaceuticals-xene-faces-market-selloff-despite-nda-filing-for-seizure-treatment">gurufocus.com &mdash; Xenon selloff and NDA filing</a> &middot; '
             '<a href="https://finimize.com/content/wall-street-ends-a-choppy-week-with-triple-witching-jitters">finimize.com &mdash; choppy week, triple-witching jitters</a>'
             '</p></div>\n')

    h.append('<p class="disc">For information only. Nothing on this page is investment advice, a recommendation, or '
             'an offer to buy or sell any security. Levels and percentages are as reported by the sources named '
             'above at the times stated; figures that could not be reconciled have been withheld or printed '
             'side by side rather than smoothed.</p>\n')
    h.append(FOOT % STAMP_JS)
    io.open(os.path.join(OUT, "wallstreet-briefing.html"), "w", encoding="utf-8").write("".join(h))


# ================================================================ MMA
def build_mma():
    h = [head("The Octagon &mdash; Daily Briefings", PAL_MMA)]
    h.append(masthead("The Octagon",
                      "Your daily MMA briefing &mdash; UFC, prospects &amp; the business of fighting"))
    h.append(meta_block(TLDR_MMA, ("#e84545", "Tale of the Tape")))
    h.append(FRESH)
    h.append(nav("mma"))

    h.append('<div class="cdbar"><b>Next card</b>'
             '<span class="cd" id="ufccdn">&nbsp;</span>'
             '<span class="w">UFC 331: Van vs. Pantoja 2 &mdash; Saturday 19 September, Crypto.com Arena, '
             'Los Angeles. Main card 9 PM ET on Paramount+.</span></div>\n')

    h.append('<h2 class="sec">Top story</h2>\n')
    h.append('<div class="panel" style="border-left:3px solid var(--accent)">'
             '<h3>Twenty-four fighters on weight, and a flyweight title rematch nine months in the making</h3>'
             '<p><b>UFC 331</b> is tomorrow night &mdash; <b>Saturday 19 September</b> &mdash; at '
             '<b>Crypto.com Arena in Los Angeles</b>, and it cleared its last administrative hurdle this morning. '
             'All <b>24 scheduled athletes made weight</b>, with champion <b>Joshua Van at 125</b> and challenger '
             '<b>Alexandre Pantoja at 125</b>. Ceremonial weigh-ins follow on the evening of <b>Friday 18 September, '
             '5:00 PM PT / 8:00 PM ET</b>, '
             'at the arena, streaming on the UFC&rsquo;s YouTube, Kick, TikTok, Facebook and Instagram channels.</p>'
             '<p>The rematch exists because the first fight barely happened. Van and Pantoja met at '
             '<b>UFC 323</b> and it <b>ended in twenty-six seconds</b> when Pantoja suffered a freak arm injury &mdash; '
             'a result that left Van with the belt and the open question of whether he had really won it. Van goes in '
             'the narrow favourite; Pantoja is trying to become the third fighter to hold the flyweight title twice.</p>'
             '<p class="note"><b>Refused, and named:</b> a &ldquo;this weekend in combat sports&rdquo; round-up '
             'surfaced this run asserting a <b>Khamzat Chimaev vs. Gilbert Burns</b> bout on Fox Nation tonight, '
             'Friday 18 September. Nothing else read this run corroborates it, no such card appears on any UFC '
             'schedule this desk has verified, and Chimaev&rsquo;s last confirmed bout is his middleweight title '
             'loss to Sean Strickland at UFC 328 on 9 May 2026. Not published in any form.</p></div>\n')

    h.append('<h2 class="sec">Fight week &mdash; upcoming cards</h2>\n')
    h.append('<div class="cards">'
             '<div class="card"><div class="tags"><span class="t gold">Title fight</span></div>'
             '<p class="mono" style="color:var(--accent2);font-size:12px;letter-spacing:.09em;margin-bottom:7px">'
             'SAT 19 SEP &middot; CRYPTO.COM ARENA, LOS ANGELES</p>'
             '<h3>UFC 331: Joshua Van vs. Alexandre Pantoja 2</h3>'
             '<p>Flyweight title rematch. Early prelims 5 PM ET, prelims 7 PM ET, main card 9 PM ET on Paramount+. '
             'Co-main: No. 2 contender <b>Arman Tsarukyan (156)</b> vs. No. 7 contender '
             '<b>Mauricio Ruffy (155)</b> at lightweight.<br>'
             '<b>Odds:</b> Van &minus;130 / Pantoja +110 (Covers, read this run &mdash; 56% implied for Van); an '
             'earlier fight-week board dated 15 September had Van &minus;138 / Pantoja +108 and Tsarukyan '
             '&minus;360 / Ruffy +260.</p></div>'
             '<div class="card"><div class="tags"><span class="t gold">Vacant title</span></div>'
             '<p class="mono" style="color:var(--accent2);font-size:12px;letter-spacing:.09em;margin-bottom:7px">'
             'SAT 3 OCT &middot; DELTA CENTER, SALT LAKE CITY</p>'
             '<h3>UFC 332: Nat&aacute;lia Silva vs. Wang Cong</h3>'
             '<p>For the <b>vacant women&rsquo;s flyweight title</b>, and the promotion&rsquo;s first numbered-event '
             'main card on CBS. No odds are published for this card &mdash; none were stated in anything read this run.</p></div>'
             '<div class="card"><div class="tags"><span class="t gold">Two title-picture bouts</span></div>'
             '<p class="mono" style="color:var(--accent2);font-size:12px;letter-spacing:.09em;margin-bottom:7px">'
             'SAT 24 OCT &middot; ETIHAD ARENA, ABU DHABI</p>'
             '<h3>UFC 333: Volkanovski vs. Evloev</h3>'
             '<p>Alexander Volkanovski defends the featherweight belt against <b>Movsar Evloev</b>, with the '
             'bantamweight trilogy bout between champion <b>Petr Yan</b> and <b>Merab Dvalishvili</b> as co-main. '
             'No odds published &mdash; none stated.</p></div>'
             '</div>\n')

    h.append('<h2 class="sec">Last event &mdash; results</h2>\n')
    h.append('<div class="panel" style="padding:4px 6px"><table>'
             '<tr><th>Result</th><th>Bout</th><th>Method</th></tr>'
             '<tr><td class="up">Jean Silva</td><td>def. Jose Miguel Delgado</td><td>Submission (rear-naked choke), R3 at 2:57</td></tr>'
             '<tr><td class="up">Brandon Moreno</td><td>def. Joseph Morales</td><td>Split decision</td></tr>'
             '<tr><td class="up">Tommy McMillen</td><td>def. Marwan Rahiki</td><td>Unanimous decision (29-28, 29-28, 29-27)</td></tr>'
             '<tr><td class="up">Alexa Grasso</td><td>def. Manon Fiorot</td><td>Unanimous decision (29-28 &times;3)</td></tr>'
             '<tr><td class="up">Curtis Blaydes</td><td>def. Waldo Cortes Acosta</td><td>Unanimous decision (29-28 &times;3)</td></tr>'
             '<tr><td class="up">David Martinez</td><td>def. Dan Ige</td><td>Unanimous decision (30-27, 30-27, 29-28)</td></tr>'
             '<tr><td class="up">Sean King III</td><td>def. Jessie Rosas</td><td>KO (slam), R1 at 0:36 &mdash; UFC debut</td></tr>'
             '</table></div>\n')
    h.append('<p class="note"><b>Noche UFC, Saturday 12 September, Desert Diamond Arena, Glendale, Arizona.</b> '
             'Results verified against UFC.com&rsquo;s own main-card report and bonus page. Bonuses: '
             '<b>Performance of the Night &mdash; Jean Silva and Sean King III; Fight of the Night &mdash; '
             'McMillen vs. Rahiki.</b> UFC.com names exactly those three awards and prints no dollar figures, so '
             'no bonus amounts are published. King&rsquo;s finishing time is <b>0:36</b>, per UFC.com&rsquo;s own '
             'headline and copy; the 33-second figure that circulates in secondary summaries is refused. '
             'Silva moves to 7-1 in the Octagon with six finishes; Martinez to 4-0 in the UFC on an eleven-fight '
             'overall streak; McMillen to 12-0; King to 7-0.</p>\n')

    h.append('<h2 class="sec">Prospect watch</h2>\n')
    h.append('<div class="cards">'
             '<div class="card"><div class="tags"><span class="t pro">Prospect</span></div>'
             '<h3>Sean King III &mdash; 7-0</h3>'
             '<p>Caught Jessie Rosas on a takedown attempt 36 seconds into his UFC debut, lifted him and slammed him '
             'for an instant knockout, and walked out with a Performance of the Night award.</p></div>'
             '<div class="card"><div class="tags"><span class="t pro">Prospect</span></div>'
             '<h3>Tommy McMillen &mdash; 12-0</h3>'
             '<p>Took a unanimous decision over Marwan Rahiki (29-28, 29-28, 29-27) in the Fight of the Night, and '
             'is still unbeaten.</p></div>'
             '<div class="card"><div class="tags"><span class="t pro">Prospect</span></div>'
             '<h3>David Martinez &mdash; 4-0 in the UFC</h3>'
             '<p>Swept Dan Ige on two cards (30-27, 30-27, 29-28) to extend an eleven-fight overall winning '
             'streak.</p></div>'
             '</div>\n')

    h.append('<h2 class="sec">Around the sport</h2>\n')
    h.append('<ul class="bul">'
             '<li><b>Mauricio Ruffy has left Fighting Nerds</b> ahead of the UFC 331 co-main, and a teammate of '
             'Arman Tsarukyan conceded this week that the move does not stop Ruffy having a chance (Bloody Elbow, '
             '18 September).</li>'
             '<li>Tsarukyan, asked about the possibility of an accidental headbutt against Ruffy, addressed it '
             'directly in fight-week media.</li>'
             '<li>Friday&rsquo;s scale session was <b>drama-free</b>: twenty-four fighters, twenty-four made weight, no '
             'misses and no late withdrawals &mdash; which also disposes of a withdrawal rumour about the champion '
             'that circulated earlier in the week, since Van stood on the scale.</li>'
             '<li>A previously-reported release of <b>Michael &ldquo;Venom&rdquo; Page</b> is <b>not carried on this '
             'page</b>: this desk&rsquo;s ledger dates the report to 7 September while placing the bout it follows on '
             '12 September, and that ordering could not be resolved against any source read this run.</li>'
             '<li>The <b>heavyweight title is vacant</b>: Tom Aspinall vacated on 14 September over ongoing eye '
             'complications and is <i>not</i> retiring. <b>Ciryl Gane</b> holds the interim belt.</li>'
             '</ul>\n')

    h.append('<h2 class="sec">Rankings &amp; business</h2>\n')
    h.append('<div class="cards">'
             '<div class="card"><h3>Rankings movement</h3>'
             '<p>The UFC 331 co-main pairs the lightweight division&rsquo;s <b>No. 2 contender</b>, Arman Tsarukyan, '
             'against its <b>No. 7</b>, Mauricio Ruffy, over five rounds &mdash; the one bout on the card that can '
             'reorder the top of a division without a belt on the line. No other ranking changes were stated in '
             'anything read this run, and none are inferred.</p></div>'
             '<div class="card"><h3>Business &amp; broadcast</h3>'
             '<p>Paramount is in <b>year one of a seven-year, $7.7 billion</b> UFC media-rights deal. '
             '<b>16 million subscriber households</b> have watched <b>180 million-plus hours</b> of UFC on '
             'Paramount+ since the start of the year. UFC 331 is a Paramount+ card; UFC 332 on 3 October will be the '
             'first numbered-event main card on CBS.</p></div>'
             '</div>\n')
    h.append('<p class="note">No viewership, gate or TKO Group figures for this weekend are published: none appeared '
             'in any source read this run, and this desk does not estimate them.<br>'
             '<b>This desk carries zero New tags this edition.</b> Grepped against every prior archived snapshot on '
             'this site, every candidate had prior hits: &ldquo;Ruffy&rdquo; 236, &ldquo;ceremonial&rdquo; 14, '
             '&ldquo;Fighting Nerds&rdquo; 1. Nothing on the page is being published here for the first time.</p>\n')

    h.append('<h2 class="sec">Champions board</h2>\n')
    champs = [
        ("Heavyweight", "VACANT", "&mdash;",
         "Tom Aspinall vacated on 14 September over ongoing eye complications; he is not retiring. <b>Interim champion: Ciryl Gane</b> (KO2 Pereira, 14 Jun 2026)"),
        ("Light Heavyweight", "Carlos Ulberg", "UFC 327, 11 Apr 2026",
         "KO1 over Ji&#345;&iacute; Proch&aacute;zka for the vacant belt"),
        ("Middleweight", "Sean Strickland", "UFC 328, 9 May 2026",
         "Split decision over Khamzat Chimaev; two-time champion"),
        ("Welterweight", "Islam Makhachev", "UFC 322, 15 Nov 2025",
         "1 defence &mdash; UD over Ian Machado Garry, UFC 330, 15 Aug 2026 (17th straight UFC win, a record)"),
        ("Lightweight", "Justin Gaethje", "14 Jun 2026", "TKO4 over Ilia Topuria"),
        ("Featherweight", "Alexander Volkanovski", "UFC 314, 12 Apr 2025",
         "Defends against Movsar Evloev at UFC 333 on 24 October"),
        ("Bantamweight", "Petr Yan", "UFC 323, 6 Dec 2025",
         "Faces Merab Dvalishvili in a trilogy bout at UFC 333 on 24 October"),
        ("Flyweight", "Joshua Van", "UFC 323, 6 Dec 2025",
         "1 defence &mdash; TKO5 Tatsuro Taira, UFC 328. Defends against Pantoja on 19 September"),
        ("Women&rsquo;s Flyweight", "VACANT", "&mdash;",
         "Valentina Shevchenko vacated while injured; Nat&aacute;lia Silva vs. Wang Cong contest it at UFC 332 on 3 October"),
        ("Women&rsquo;s Bantamweight", "Kayla Harrison", "UFC 316, 7 Jun 2025",
         "0 defences &mdash; the scheduled UFC 324 defence was cancelled after she withdrew for neck surgery"),
        ("Women&rsquo;s Strawweight", "Mackenzie Dern", "UFC 321, 25 Oct 2025",
         "1 defence &mdash; UD over Gillian Robertson, UFC 330, 15 Aug 2026"),
    ]
    h.append('<div class="panel" style="padding:4px 6px"><table>'
             '<tr><th>Division</th><th>Champion</th><th>Won</th><th>Note</th></tr>')
    for d, c, w, n in champs:
        cc = ' class="mut"' if c == "VACANT" else ""
        h.append('<tr><td>%s</td><td%s><b>%s</b></td><td class="mono">%s</td><td>%s</td></tr>' % (d, cc, c, w, n))
    h.append('</table></div>\n')
    h.append('<p class="note"><b>Why this board is current.</b> The last title bout anywhere was <b>UFC 330 on '
             '15 August</b>. Shanghai on 29 August, and both Paris and Noche UFC on 12 September, were non-title '
             'cards. Nothing since 15 August could have changed a belt, and the two vacancies are documented '
             'vacatings rather than results. The next belt that can move is the flyweight one, on 19 September.<br>'
             '<b>Refused, and named:</b> the ESPN current-champions page regressed for a <b>sixth consecutive run</b>. '
             'The rendering read this run seats <b>Carlos Ulberg at heavyweight</b> and <b>Sean Strickland at light '
             'heavyweight</b> &mdash; each shifted up exactly one row from his real division, with the correct win '
             'details still attached. The names are current; the division labels are not. Its other rows agree with '
             'the board above. Nothing was taken from it.</p>\n')

    h.append('<h2 class="sec">Sources</h2>\n')
    h.append('<div class="panel"><p class="srcs">'
             '<a href="https://www.covers.com/ufc/331-odds-saturday-sept-19-2026">covers.com &mdash; UFC 331 odds &amp; fight card</a> &middot; '
             '<a href="https://sports.yahoo.com/articles/ufc-331-official-weigh-results-150028870.html">sports.yahoo.com &mdash; UFC 331 official weigh-in results</a> &middot; '
             '<a href="https://sports.yahoo.com/articles/ufc-331-full-card-date-045924305.html">sports.yahoo.com &mdash; UFC 331 full card, date and time</a> &middot; '
             '<a href="https://dknetwork.draftkings.com/2026/09/17/ufc-331-van-vs-pantoja-2-ceremonial-weigh-in-date-start-time-location-how-to-watch/">dknetwork.draftkings.com &mdash; ceremonial weigh-in details</a> &middot; '
             '<a href="https://www.ufc.com/video/160224">ufc.com &mdash; Tsarukyan vs. Ruffy co-main feature</a> &middot; '
             '<a href="https://www.tapology.com/fightcenter/events/145652-ufc-331">tapology.com &mdash; UFC 331 event page</a> &middot; '
             '<a href="https://bloodyelbow.com/2026/09/18/arman-tsarukyans-teammate-admits-mauricio-ruffy-has-a-chance-at-ufc-331-after-leaving-fighting-nerds/">bloodyelbow.com &mdash; Ruffy leaves Fighting Nerds</a> &middot; '
             '<a href="https://mmasucka.com/news/ufc-331-weigh-ins-drama-free-friday-on-scales-in-southern-california/">mmasucka.com &mdash; weigh-in report</a> &middot; '
             '<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">espn.com &mdash; current and all-time UFC champions (refused this run, see note)</a>'
             '</p></div>\n')

    h.append('<p class="disc">Cards and bouts are subject to change. Odds move constantly and are shown with the '
             'book and the date on which they were read; they are not a recommendation to bet. Records, methods and '
             'finishing times are as stated by the sources named above &mdash; where a source could not be confirmed '
             'this run, the item has been dropped or the gap stated in place.</p>\n')

    h.append("""<script>(function(){try{
var t=new Date('2026-09-19T21:00:00-04:00');var e=document.getElementById('ufccdn');if(!e)return;
function tick(){var ms=t-new Date();if(ms<=0){e.textContent='Fight week \\u2014 live/completed';return;}
var d=Math.floor(ms/86400000),h=Math.floor(ms%86400000/3600000),m=Math.floor(ms%3600000/60000);
e.textContent=d+'d '+h+'h '+m+'m';}
tick();setInterval(tick,30000);}catch(e){}})();</script>\n""")
    h.append(FOOT % STAMP_JS)
    io.open(os.path.join(OUT, "mma-briefing.html"), "w", encoding="utf-8").write("".join(h))


# ================================================================ INDEX
def build_index():
    h = [head("Daily Briefings", PAL_IX)]
    h.append(masthead("Daily Briefings",
                      "Three desks, rebuilt from live sources every thirty minutes, 8 AM&ndash;6 PM ET"))
    h.append(FRESH)
    h.append(nav("index"))
    h.append('<div class="big">'
             '<div class="card cy"><div class="k">&#9960; The Cyber Wire &middot; The Wire</div>'
             '<h3>Two federal patch deadlines inside a day</h3>'
             '<p>%s</p><a class="rd" href="cyber-briefing.html">Read the briefing &rarr;</a></div>'
             '<div class="card ws"><div class="k">&#9650; The Closing Bell &middot; The Tape</div>'
             '<h3>A split close to a triple-witching week</h3>'
             '<p>%s</p><a class="rd" href="wallstreet-briefing.html">Read the briefing &rarr;</a></div>'
             '<div class="card mm"><div class="k">&#8856; The Octagon &middot; Tale of the Tape</div>'
             '<h3>UFC 331 is tomorrow, and everyone made weight</h3>'
             '<p>%s</p><a class="rd" href="mma-briefing.html">Read the briefing &rarr;</a></div>'
             '</div>\n' % (TLDR_CY, TLDR_WS, TLDR_MMA))
    h.append('<h2 class="sec">About this edition</h2>\n')
    h.append('<div class="panel"><p>Each desk is rebuilt from live web sources on every run. Nothing is published '
             'unless a source read during that run states it, or a standing correction in this site&rsquo;s ledger '
             'records it with a source. Figures that could not be reconciled are printed side by side or withheld, '
             'and the refusal is named on the page rather than quietly dropped. Point-in-time snapshots of every '
             'edition are kept in the <a href="archive.html">archive</a>.</p></div>\n')
    h.append('<p class="disc">Information only. The markets desk is not investment advice; the security desk is not '
             'a substitute for vendor advisories; fight cards are subject to change.</p>\n')
    h.append(FOOT % STAMP_JS)
    io.open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write("".join(h))


build_cyber()
build_ws()
build_mma()
build_index()
print("built:", sorted(f for f in os.listdir(OUT) if f.endswith(".html")))
