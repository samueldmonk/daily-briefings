# -*- coding: utf-8 -*-
import io, os
from common import head, masthead, nav, STAMP_JS, FOOT

OUT = os.path.dirname(os.path.abspath(__file__))

PAL = """
:root{
  --bg:#0a0a0b; --panel:#141414; --line:#262626;
  --accent:#d8d2c6; --accent2:#e8c766;
  --txt:#ece9e3; --muted:#9b9690;
  --up:#22c55e; --down:#ef4444; --warn:#f0b429; --crit:#ef4444;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
.big{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:16px;margin-top:6px}
.bigcard{background:var(--panel);border:1px solid var(--line);border-top:3px solid var(--c);
  border-radius:14px;padding:20px 21px;transition:.16s;display:flex;flex-direction:column}
.bigcard:hover{transform:translateY(-3px);box-shadow:0 10px 26px rgba(0,0,0,.4);border-color:var(--c)}
.bigcard .kicker{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--c)}
.bigcard h2{margin:8px 0 3px;font-size:23px;letter-spacing:-.3px}
.bigcard .strap{font-family:var(--mono);font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-bottom:11px}
.bigcard p{margin:0 0 16px;font-size:14.5px;color:#cfcbc6;flex:1}
.bigcard a.go{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--c)}
.serif h2{font-family:Georgia,'Times New Roman',serif}
"""

CARDS = [
    ("#22d3a8", "⛨ The Cyber Wire", "The Cyber Wire", "The Wire", "cyber-briefing.html", False,
     "Cisco shipped a firewall hardening release on 16 September carrying eight vulnerability classes up to "
     "CVSS 9.9 &mdash; two of them already exploited in the wild &mdash; while a separate Cisco email-gateway flaw "
     "hits its federal patch deadline today."),
    ("#caa64a", "▲ The Closing Bell", "The Closing Bell", "The Tape", "wallstreet-briefing.html", True,
     "Stocks rebounded broadly on Thursday &mdash; the S&amp;P 500 up 1.12% and the Dow up 0.73% on the latest read "
     "&mdash; as Treasury yields and oil both eased a day after the Federal Reserve&rsquo;s first rate rise since 2023."),
    ("#e84545", "⊘ The Octagon", "The Octagon", "Tale of the Tape", "mma-briefing.html", False,
     "UFC 331 lands Saturday in Los Angeles with Joshua Van defending the flyweight title against Alexandre Pantoja "
     "in a rematch, while the heavyweight belt sits vacant after Tom Aspinall gave it up on 14 September."),
]


def build():
    o = io.StringIO()
    o.write(head("Daily Briefings", PAL))
    o.write(masthead("Daily Briefings",
                     "Three desks, refreshed every 30 minutes &mdash; security, markets and the fight game"))
    o.write('<div class="freshline" id="freshline">&nbsp;</div>\n')
    o.write(nav("index"))
    o.write('<div class="big">')
    for colour, kicker, title, strap, href, serif, summary in CARDS:
        o.write('<div class="bigcard%s" style="--c:%s">'
                '<div class="kicker">%s</div>'
                '<h2>%s</h2><div class="strap">%s</div>'
                '<p>%s</p>'
                '<a class="go" href="%s">Read the briefing &rarr;</a>'
                "</div>" % (" serif" if serif else "", colour, kicker, title, strap, summary, href))
    o.write("</div>\n")
    o.write('<p class="disc">Each briefing is rebuilt from live sources every 30 minutes between 8 a.m. and 6 p.m. ET. '
            'Figures are stated with the hour they describe. Point-in-time snapshots of every edition are kept in the '
            '<a href="archive.html">Archive</a>. Markets coverage is for information only and is not investment advice.</p>\n')
    o.write(FOOT % STAMP_JS)
    return o.getvalue()


if __name__ == "__main__":
    html = build()
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(html)
    print("index ok", len(html))
