#!/usr/bin/env python3
# MMA + index edits, run 2026-09-09 ~1:45pm ET (Midday Edition, third run of the day)
import io
D = "/sessions/sharp-bold-tesla/mnt/outputs/"
n = 0
def rep(s, old, new):
    global n
    assert s.count(old) == 1, ("NOT-UNIQUE/MISSING: " + old[:110])
    n += 1
    return s.replace(old, new)

# ================= MMA =================
P = D + "mma-briefing.html"
s = io.open(P, encoding="utf-8").read()

# 1. The withdrawing fighter is now named.
s = rep(s, '<p>The fourth annual Noche UFC lands on Mexican Independence Day weekend with a featherweight main event. <b>Delgado stepped in on late notice</b> after an injury in camp removed the original opponent, and gets the first headline slot of his UFC career.',
    '<p>The fourth annual Noche UFC lands on Mexican Independence Day weekend with a featherweight main event. <b>The fighter Delgado replaced is now named: Yair Rodr&iacute;guez</b>, who withdrew with an injury. Delgado &mdash; who is from Arizona &mdash; stepped in on late notice and gets the first headline slot of his UFC career.')

s = rep(s, '<div class="card"><span class="t carried">Carried</span><div class="kv">Sat 12 September &middot; Desert Diamond Arena, Glendale, AZ</div>',
    '<div class="card"><span class="t new">New</span><div class="kv">Sat 12 September &middot; Desert Diamond Arena, Glendale, AZ</div>')

# 2. TL;DR — lead with the newly closed detail alongside Aspinall.
s = rep(s, '<div class="tldr"><b>Tale of the Tape</b> <span>Dana White says heavyweight champion Tom Aspinall is still hurt with no return date &mdash; &ldquo;the heavyweight division will just keep rolling&rdquo; &mdash; three days out from Noche UFC in Glendale.</span></div>',
    '<div class="tldr"><b>Tale of the Tape</b> <span>Dana White says heavyweight champion Tom Aspinall is still hurt with no return date &mdash; &ldquo;the heavyweight division will just keep rolling&rdquo; &mdash; three days out from Noche UFC in Glendale, where the late replacement in the main event is now confirmed to have come in for an injured Yair Rodr&iacute;guez.</span></div>')

# 3. Around the Sport — add the Rodriguez line.
s = rep(s, '<li><b>Roster churn cuts both ways.</b>',
    '<li><b>A blank on this page is now filled.</b> Previous editions said only that Jose Miguel Delgado &ldquo;stepped in on late notice&rdquo; and declined to name who had withdrawn, because a single read gave only a surname. Two further reads this run identify him as <b>Yair Rodr&iacute;guez</b>, out with an injury. That turns Saturday&rsquo;s headliner from a routine short-notice booking into a local fighter replacing one of the division&rsquo;s most recognisable names on a Mexican Independence Day card.</li>\n<li><b>Roster churn cuts both ways.</b>')

# 4. Champions board — record this run's re-verification.
s = rep(s, '<b>How this board was checked this run.</b> Six belts &mdash; heavyweight, light heavyweight, middleweight, welterweight, lightweight and featherweight &mdash; were read directly off ESPN&rsquo;s current-champions article with their title dates and defence counts.',
    '<b>How this board was checked this run.</b> Six belts &mdash; heavyweight, light heavyweight, middleweight, welterweight, lightweight and featherweight &mdash; were re-read off ESPN&rsquo;s current-champions article <b>again this run</b>, and all six matched the board exactly on champion, date, method and defence count: Aspinall 21 Jun 2025 (0), Ulberg KO1 Proch&aacute;zka 11 Apr 2026 (0), Strickland split decision over Chimaev 9 May 2026 (0), Makhachev UD Della Maddalena 15 Nov 2025 (1), Gaethje TKO4 Topuria 14 Jun 2026 (0), Volkanovski UD Lopes 12 Apr 2025 (1). <b>No Pereira-at-205 regression and no Chimaev-at-185 regression</b>, and featherweight is not vacant.')

# 5. The "Carried" note — update for this run.
s = rep(s, '<b>On the &ldquo;Carried&rdquo; tags.</b> The previous edition of this page published at 12:57 p.m. ET today. Nothing on the MMA beat has changed in the interval beyond the Aspinall update at the top, so every card on this page is honestly marked <i>Carried</i> rather than re-tagged New.',
    '<b>On the &ldquo;Carried&rdquo; tags.</b> Three editions of this page have published today, at 12:57, 1:15 and now. The only MMA fact that changed in the latest interval is the identification of <b>Yair Rodr&iacute;guez</b> as the fighter Delgado replaced, so exactly one card is tagged <i>New</i> and every other card on the page is honestly marked <i>Carried</i>. Tagging an unchanged card &ldquo;New&rdquo; because the page was rebuilt would be a lie about the news, not about the build.')

io.open(P, "w", encoding="utf-8").write(s)

# ================= INDEX =================
P = D + "index.html"
s = io.open(P, encoding="utf-8").read()

s = rep(s, '<p>CISA has given federal agencies until 11 September to patch CVE-2026-86218, a CVSS 10.0 pre-authentication remote-code-execution flaw in N-able N-central that is being exploited in the wild against the platforms managed service providers use to reach every one of their customers.</p>',
    '<p>CISA has given federal agencies until 11 September to patch CVE-2026-86218, a CVSS 10.0 pre-authentication remote-code-execution flaw in the N-able N-central platform managed service providers use to reach every one of their customers &mdash; and N-able&rsquo;s own release notes and incident notice flatly contradict each other on whether it has been exploited yet.</p>')

s = rep(s, '<p>Brent crude broke back above $100 a barrel for the first time since July after U.S.&ndash;Iran strikes escalated, and selling broadened through the late morning &mdash; the Dow down 413 points, or 0.8%, as of 12:07 p.m. ET, with 78% of the S&amp;P 500 in the red.</p>',
    '<p>Brent crude broke back above $100 a barrel for the first time since July after U.S.&ndash;Iran strikes escalated, and all three major indexes were lower into the early afternoon &mdash; the Dow off 321.52 points (&minus;0.61%), the Nasdaq Composite &minus;0.60% and the S&amp;P 500 &minus;0.42% on a live quote board read at about 1:35 p.m. ET.</p>')

s = rep(s, '<p>Dana White says heavyweight champion Tom Aspinall is still hurt with no return date &mdash; &ldquo;the heavyweight division will just keep rolling&rdquo; &mdash; three days out from Noche UFC in Glendale.</p>',
    '<p>Dana White says heavyweight champion Tom Aspinall is still hurt with no return date &mdash; &ldquo;the heavyweight division will just keep rolling&rdquo; &mdash; three days out from Noche UFC in Glendale, where the late replacement in the main event is now confirmed to have come in for an injured Yair Rodr&iacute;guez.</p>')

s = rep(s, '<div class="disc">Each card summarises',
    '<div><a href="https://www.fool.com/coverage/stock-market-today/2026/09/09/stock-market-midday-sept-9-stocks-slide-as-oil-surges-past-usd100-while-meta-gains/">https://www.fool.com/coverage/stock-market-today/2026/09/09/stock-market-midday-sept-9-stocks-slide-as-oil-surges-past-usd100-while-meta-gains/</a></div>'
    '<div><a href="https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html">https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html</a></div>'
    '<div><a href="https://en.wikipedia.org/wiki/UFC_Fight_Night:_Silva_vs._Delgado">https://en.wikipedia.org/wiki/UFC_Fight_Night:_Silva_vs._Delgado</a></div>'
    '<div class="disc">Each card summarises')

io.open(P, "w", encoding="utf-8").write(s)
print("mma + index OK, %d edits" % n)
