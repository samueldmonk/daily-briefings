# -*- coding: utf-8 -*-
import io, re
def rd(f): return io.open(f,encoding="utf-8").read()
def wr(f,s): io.open(f,"w",encoding="utf-8").write(s)
def rep(s,o,n,c=1,l=""):
    k=s.count(o); assert k==c,"EXPECT %d got %d %s :: %s"%(c,k,l,o[:70]); return s.replace(o,n)

m = rd("mma-briefing.html")

# --- body note: two figures challenged and upheld ---
ANCH = 'Every weight class above is now sourced.'
NOTE = ('<b>Two rows were challenged at 6:20 PM and both were upheld.</b> An aggregated results listing '
 'fetched this run put the <b>Bilal Hasan</b> knockout of Nilson Rojas in <b>round one</b> and '
 '<b>Rei Tsuruya&rsquo;s</b> rear-naked choke at <b>4:03</b>. Neither figure was adopted. Targeted searches on '
 'each bout returned <b>round two, 2:28</b> for Hasan &mdash; stated independently by three separate write-ups, '
 'one of which headlines the finish as a <b>&ldquo;Round 2 walk-off shot&rdquo;</b> &mdash; and <b>4:14 of '
 'round one</b> for Tsuruya. <b>The table above is unchanged</b>, and the challenge is recorded rather than '
 'discarded, because an aggregate that gets one round wrong is a reason to distrust that aggregate, not a '
 'reason to pretend it never disagreed. Hasan&rsquo;s bout was the <b>main card opener</b> and his '
 '<b>UFC debut</b>, taking him to <b>10-0</b>; Rojas falls to <b>9-1</b>. '
 'Every weight class above is now sourced.')
m = rep(m, ANCH, NOTE, 1, "mma results note")

# --- Song's own words + the path, appended to the results-bonuses area ---
QANCH = 'Corroborated at 11:05 AM, and the arithmetic is the check.'
QNEW = ('<b>What Song actually asked for, in his own words, sourced at 6:20 PM.</b> Asked about what comes next, '
 'Song said: <b>&ldquo;I think the UFC should give me the title shot. I feel like I can finish everyone. I can '
 'finish Petr, I can finish Merab.&rdquo;</b> <b>The belt is not available to give.</b> '
 '<b>Petr Yan</b> defends the bantamweight title against <b>Merab Dvalishvili</b> in a trilogy bout at '
 '<b>UFC 333 on October 24</b>. Reporting fetched this run frames Song&rsquo;s realistic options as a '
 '<b>backup role for that fight, or a bout with its winner</b> &mdash; which is the same conclusion this page '
 'reached from the schedule, now attributable rather than inferred. '
 '&#9888; <b>One odds figure moved and is recorded, not replaced.</b> A report this run prices Nurmagomedov at '
 '<b>&minus;600</b>; this page has carried <b>&minus;625</b> from a different book. <b>Both are plausible '
 'simultaneously</b> &mdash; different books, and no source states which one it quotes as closing. The page '
 'keeps &minus;625 and notes the &minus;600 sighting; either way the description is the same, a heavy favourite '
 'who lost. One account this run also calls Song the <b>first man to knock out Umar Nurmagomedov</b>. '
 'Corroborated at 11:05 AM, and the arithmetic is the check.')
m = rep(m, QANCH, QNEW, 1, "mma song quote")

# --- footer sources ---
FA = '<a href="https://www.mmamania.com/ufc-results'
NEWSRC = ('<a href="https://sports.yahoo.com/articles/song-yadong-lands-unbelievable-knockout-130811359.html">'
 'Yahoo Sports &mdash; Song Yadong upsets Umar Nurmagomedov (Aug 29, 2026)</a><br>\n'
 '<a href="https://ca.sports.yahoo.com/news/song-yadong-wants-title-shot-160120772.html">'
 'Yahoo Sports &mdash; Song Yadong wants title shot: &ldquo;I can finish everyone&rdquo;</a><br>\n'
 '<a href="https://sports.yahoo.com/articles/why-bantamweight-contender-gives-petr-152015348.html">'
 'Yahoo Sports &mdash; Yan vs. Dvalishvili at UFC 333, Oct 24</a><br>\n'
 '<a href="https://boxingnews.com/news/bilal-hasan-vs-nilson-rojas-result-and-reaction">'
 'boxingnews.com &mdash; Hasan def. Rojas by KO in round 2</a><br>\n'
 '<a href="https://sports.yahoo.com/articles/ufc-shanghai-video-rei-tsuruya-093200676.html">'
 'Yahoo Sports &mdash; Tsuruya submits Borjas, 4:14 of round 1</a><br>\n'
 + FA)
m = rep(m, FA, NEWSRC, 1, "mma sources")
wr("mma-briefing.html", m)

c = rd("cyber-briefing.html")
j = c.find('<footer'); k = c.find('<a ', j)
CSRC = ('<a href="https://www.cnbc.com/2026/08/27/ai-cyber-defense-letter.html">'
 'CNBC &mdash; 116 companies and entities sign AI cyber defense letter (Aug 27, 2026)</a><br>\n'
 '<a href="https://www.securityweek.com/tech-cybersecurity-giants-unite-behind-openai-led-cyber-defense-pledge/">'
 'SecurityWeek &mdash; Tech and cybersecurity giants unite behind OpenAI-led cyber defense pledge</a><br>\n'
 '<a href="https://gizmodo.com/google-openai-and-over-100-companies-call-for-more-action-on-ai-driven-cyberattacks-2000804091">'
 'Gizmodo &mdash; Google, OpenAI and over 100 companies call for action on AI-driven cyberattacks</a><br>\n'
 '<a href="https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog">'
 'CISA &mdash; Adds three known exploited vulnerabilities to catalog (Aug 27, 2026)</a><br>\n'
 '<a href="https://www.cisa.gov/news-events/alerts/2026/08/24/cisa-adds-one-known-exploited-vulnerability-catalog">'
 'CISA &mdash; Adds one known exploited vulnerability to catalog (Aug 24, 2026)</a><br>\n')
c = c[:k] + CSRC + c[k:]
wr("cyber-briefing.html", c)

w = rd("wallstreet-briefing.html")
j = w.find('<footer'); k = w.find('<a ', j)
WSRC = ('<a href="https://www.cnbc.com/2026/08/27/stock-market-today-live-updates.html">'
 'CNBC &mdash; S&amp;P 500 falls Friday after Warsh highlights inflation worries, index posts positive week</a><br>\n')
w = w[:k] + WSRC + w[k:]
wr("wallstreet-briefing.html", w)
print("EDITS2 OK")
