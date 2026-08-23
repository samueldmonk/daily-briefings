# -*- coding: utf-8 -*-
import io
O='/sessions/relaxed-confident-goldberg/mnt/outputs/'
def rd(p): return io.open(O+p, encoding='utf-8').read()
def wr(p,s): io.open(O+p,'w',encoding='utf-8').write(s)
def sub(s, old, new, name):
    assert old in s, 'MISS: '+name
    return s.replace(old, new, 1)

# --- MMA sources: add the two URLs fetched/found this run ---
m = rd('mma-briefing.html')
m = sub(m,
 '<li><a href="https://www.ufc.com/events">UFC.com — Events (upcoming cards, venues and start times)</a></li>',
 '<li><a href="https://www.ufc.com/events">UFC.com — Events (upcoming cards, venues and start times)</a></li>\n'
 '<li><a href="https://www.ufc.com/news/ufc-returns-shanghai-pivotal-bantamweight-clash-between-3-umar-nurmagomedov-and-5-song-yadong">UFC.com — UFC returns to Shanghai with a pivotal bantamweight clash between #3 Umar Nurmagomedov and #5 Song Yadong (full card, co-main and Road to UFC semifinals)</a></li>\n'
 '<li><a href="https://bloodyelbow.com/2026/08/22/ufc-signs-undefeated-two-weight-world-champion-with-debut-reportedly-set-for-october/">Bloody Elbow — UFC signs undefeated two-weight world champion, debut reportedly set for October (Aug 22, 2026)</a></li>\n'
 '<li><a href="https://en.wikipedia.org/wiki/UFC_Fight_Night:_Nurmagomedov_vs._Song">UFC Fight Night: Nurmagomedov vs. Song — event page (Aug 29, 2026, SPD Bank Oriental Sports Center)</a></li>',
 'mma sources')
wr('mma-briefing.html', m)

# --- INDEX: refresh the three summaries to match each page's verified lead ---
i = rd('index.html')
i = sub(i,
 'Gregory Rodrigues took a unanimous decision over Anthony Hernandez in Sacramento to win his fourth straight, split Fight of the Night with him, and call out No. 2-ranked Dricus du Plessis. Ten of the card&rsquo;s 13 bouts ended in a stoppage.',
 'Gregory Rodrigues took a unanimous decision over Anthony Hernandez in Sacramento to win his fourth straight, split Fight of the Night with him, and call out No. 2-ranked Dricus du Plessis. Attention now shifts to Shanghai on Saturday, where the full Nurmagomedov vs Song card is set behind a Yan Xiaonan co-main.',
 'index mma')
i = sub(i,
 'Bessent details the plan to economically isolate Iran on Monday, and July PCE lands the same day Nvidia reports, Wednesday.',
 'Bessent details the plan to economically isolate Iran on Monday, July PCE lands the same day Nvidia reports on Wednesday, and Warsh keynotes Jackson Hole on Friday with the Fed and the Treasury pulling opposite ways on yields.',
 'index ws')
i = sub(i,
 'lands today, while seven other entries in the Known Exploited Vulnerabilities catalog are already past due, the oldest by nine days.',
 'lands today, while seven other entries in the Known Exploited Vulnerabilities catalog are already past due, the oldest by nine days. The catalog was re-checked for this edition and the board is unchanged.',
 'index cyber')
wr('index.html', i)
print('OK')
