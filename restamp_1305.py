# -*- coding: utf-8 -*-
import io,re
STAMP=u"12:58 PM"
pages=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
for p in pages:
    s=io.open(p,encoding='utf-8').read()
    # masthead updated pill
    s2=re.sub(r'(<span id="updated">)[^<]*(</span>)', r'\g<1>'+STAMP+u' ET'+r'\g<2>', s)
    # freshline
    s2=re.sub(r'(<div class="freshline" id="freshline">)Data as of [^<]*(</div>)',
              r'\g<1>Data as of '+STAMP+u' ET &middot; briefings refresh every 30 minutes, 8 AM&ndash;6 PM ET'+r'\g<2>', s2)
    s2=re.sub(r'(<span class="pill" id="datestamp">)[^<]*(</span>)', r'\g<1>Sunday, August 30, 2026\g<2>', s2)
    s2=re.sub(r'(<span class="pill" id="edition">)[^<]*(</span>)', r'\g<1>Midday Edition\g<2>', s2)
    io.open(p,'w',encoding='utf-8').write(s2)
print('restamped to',STAMP)
