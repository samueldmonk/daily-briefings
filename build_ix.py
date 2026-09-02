# -*- coding: utf-8 -*-
import css as C
import build_ws, build_cy, build_mma

CSS = C.base_css("#8a94a6", "#b9c2d0", "#0b0c0e", "#14161a", "#252932") + """
.big{display:grid;gap:16px}
@media(min-width:760px){.big{grid-template-columns:1fr}}
.bigcard{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 22px;
  border-left:4px solid var(--c);transition:.16s}
.bigcard:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(0,0,0,.35)}
.bigcard .k{font-family:var(--mono);font-size:11px;letter-spacing:.17em;text-transform:uppercase;color:var(--c)}
.bigcard h3{margin:8px 0 9px;font-size:22px;color:var(--c)}
.bigcard p{font-size:15px;color:#cfd3d9;margin:0 0 13px}
.bigcard a.rd{font-family:var(--mono);font-size:11.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--c)}
.serif h3{font-family:Georgia,'Times New Roman',serif}
"""

CARDS = [
    ("#22d3a8", "&#9960; The Cyber Wire", "The Wire", build_cy.TLDR, "cyber-briefing.html", ""),
    ("#caa64a", "&#9650; The Closing Bell", "The Tape", build_ws.TLDR, "wallstreet-briefing.html", "serif"),
    ("#e84545", "&#8856; The Octagon", "Tale of the Tape", build_mma.TLDR, "mma-briefing.html", ""),
]


def build():
    p = []
    p.append(C.head("Daily Briefings", CSS))
    p.append('<div class="masthead"><h1>Daily Briefings</h1>'
             '<p class="tag">Three desks, refreshed every 30 minutes — security, markets and mixed martial arts</p>'
             + C.meta_row() + "</div>")
    p.append('<div class="freshline" id="freshline">&nbsp;</div>')
    p.append(C.nav("index"))

    p.append('<div class="big">')
    for color, title, label, tldr, href, cls in CARDS:
        p.append('<div class="bigcard %s" style="--c:%s"><div class="k">%s &middot; %s</div>'
                 '<h3>%s</h3><p>%s</p><a class="rd" href="%s">Read the briefing &rarr;</a></div>'
                 % (cls, color, title, label, title, tldr, href))
    p.append("</div>")

    p.append('<div class="note" style="margin-top:26px">Every figure on these pages is checked against a '
             'source fetched during the run that published it, or against this desk\'s standing corrections '
             'file. Where sources disagree, the disagreement is printed rather than resolved by preference; '
             'where a number could not be verified, it is left off the page and the omission is stated.</div>')

    p.append(C.STAMP_JS)
    p.append("</div></body></html>")
    return "".join(p)


if __name__ == "__main__":
    open("index.html", "w").write(build())
    print("index ok")
