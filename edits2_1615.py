# -*- coding: utf-8 -*-
import io, re
O='/sessions/relaxed-confident-goldberg/mnt/outputs/'
def rd(p): return io.open(O+p, encoding='utf-8').read()
def wr(p,s): io.open(O+p,'w',encoding='utf-8').write(s)
def sub(s, old, new, name):
    assert old in s, 'MISS: '+name
    return s.replace(old, new, 1)

# ---------------- MMA part 2 ----------------
m = rd('mma-briefing.html')

# Prospect watch: add Lucia Szabova
szabova = '''<div class="card">
<div class="tags"><span class="tag new">New</span><span class="tag prospect">Prospect</span></div>
<h3>Lucia Szabova &mdash; a two-weight OKTAGON champion, reportedly UFC-bound</h3>
<p>Bloody Elbow reported on Saturday that the UFC has signed Szabova, whom it bills as an undefeated two-weight world champion. She holds belts at bantamweight and flyweight and has spent the majority of her professional career in OKTAGON at 135 pounds. Her promotional debut is <em>reported</em> to be set for October, against Tainara Lisboa. The UFC has not published a bout announcement, so treat the date and the opponent as reporting rather than confirmed booking.</p>
</div>

<div class="card">
<div class="tags"><span class="tag prospect">Prospect</span></div>
<h3>Anthony Wint'''
m = sub(m, '''<div class="card">
<div class="tags"><span class="tag prospect">Prospect</span></div>
<h3>Anthony Wint''', szabova, 'szabova card')

# Around the sport: add Road to UFC + Shanghai fight-week detail
old_next = '''<li><strong>Next up.</strong> The promotion heads to Shanghai on Saturday, August 29 for Umar Nurmagomedov vs Song Yadong, then Paris on September 5.</li>'''
new_next = '''<li><strong>Road to UFC returns Friday.</strong> Shanghai fight week is a back-to-back double: the <strong>Road to UFC Season 5 semifinals</strong> run Friday, August 28 (5 PM China time), with the 16 surviving Asia-Pacific prospects fighting for a place in the finals and a multi-fight UFC contract. UFC.com says the opening round produced <strong>10 finishes</strong>.</li>
<li><strong>A Shanghai homecoming.</strong> UFC.com describes the card as the promotion&rsquo;s return to Shanghai for a second consecutive year and its first event in the Pudong District since it sold out Mercedes-Benz Arena in 2017. The event is hosted by the Shanghai Municipal Sports Bureau and the Pudong District Government, with China Mobile subsidiary Migu and Orange Lion Sports (formerly Alisports) as co-organizers.</li>
<li><strong>Next up.</strong> The promotion heads to Shanghai on Saturday, August 29 for Umar Nurmagomedov vs Song Yadong, then Paris on September 5.</li>'''
m = sub(m, old_next, new_next, 'around the sport')

# TLDR refresh — lead with the same verified lead, note the week ahead
m = sub(m,
 '<div class="tldr"><b>Tale of the Tape</b> <span>Gregory Rodrigues outlasted Anthony Hernandez over five rounds in Sacramento for his fourth straight win, split Fight of the Night with him, and called out No. 2-ranked Dricus du Plessis.</span></div>',
 '<div class="tldr"><b>Tale of the Tape</b> <span>Gregory Rodrigues outlasted Anthony Hernandez over five rounds in Sacramento for his fourth straight win, split Fight of the Night with him, and called out No. 2-ranked Dricus du Plessis &mdash; and attention now turns to Shanghai, where the full Nurmagomedov vs Song card is set behind a Yan Xiaonan co-main.</span></div>',
 'mma tldr')
wr('mma-briefing.html', m)
print('mma part 2 OK')
