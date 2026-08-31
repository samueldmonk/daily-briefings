# -*- coding: utf-8 -*-
import re, io
STAMP='12:51 PM'
for f in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s=io.open(f,encoding='utf-8').read()
    s=re.sub(r'(<div class="freshline" id="freshline">)Data as of [^<]*(</div>)',
             r'\g<1>Data as of '+STAMP+' ET &middot; briefings refresh every 30 minutes, 8 AM&ndash;6 PM ET\g<2>',s)
    io.open(f,'w',encoding='utf-8').write(s)
    print('restamped',f)

# index.html: mirror the three summary sentences + refresh source links
idx=io.open('index.html',encoding='utf-8').read()
cards={
 'cyber':'<b>LockBit 5 listed U.S. Bank on August 20 with a September 3 publication deadline &mdash; and U.S. Bancorp disputes it</b>, saying it traced the activity to &ldquo;a potential cyber incident&hellip;related to a fourth party event that occurred outside&rdquo; its environment, with <b>no evidence its own systems, networks or data repositories were compromised</b>. A denial about your own network is not a denial that the data is real, and the deadline runs regardless.',
 'markets':'<b>The recap this page has refused three times came back under a different question, and its sector figures contradict its own headline</b> &mdash; a wrap dated August 31 reporting a <b>3.2% gain in the technology sector ETF</b> in a session it also calls <b>weak on AI stocks</b>, alongside two of Friday&rsquo;s closes. The live session has the <b>S&amp;P 500 down about half a percent at midday</b>, <b>energy the only sector higher</b>, and a <b>utilities decline that is really two stocks</b>.',
 'mma':'<b>UFC Paris finally has a price and it inverts the billing</b> &mdash; <b>Salahdine Parnasse &minus;550, Dan Hooker +400</b> for Saturday&rsquo;s five-round main event at the Accor Arena, the first refreshed odds line this page has published in several editions. <b>Noche UFC joins the calendar for September 12 in Glendale, Arizona</b>, and the champions board is unchanged for a <b>seventy-fourth consecutive edition</b>.',
}
print('index cards prepared')
io.open('index_cards.txt','w',encoding='utf-8').write(repr(cards))
