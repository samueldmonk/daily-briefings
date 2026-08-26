import io, os, sys
O=os.path.dirname(os.path.abspath(__file__)); fails=[]
def rep(h,o,n,l):
    if h.count(o)!=1: fails.append(l); return h
    return h.replace(o,n)
A='<div class="lab">Sources</div>\n'
w=io.open(os.path.join(O,'wallstreet-briefing.html'),encoding='utf-8').read()
NEW=(A+'<p class="note"><b>Added 5:36:</b> <a href="https://ca.investing.com/news/stock-market-news/afterhours-movers-nvda-crm-snps-crwd-okta-ntnx-432SI-4818239">Investing.com &mdash; After-hours movers: NVDA, CRM, SNPS, CRWD, OKTA, NTNX</a> &middot; '
 '<a href="https://ca.investing.com/news/earnings/hp-earnings-beat-expectations-but-shares-tumble-4818200">Investing.com &mdash; HP earnings beat expectations but shares tumble</a> &middot; '
 '<a href="https://www.kiplinger.com/investing/live/nvidia-earnings-live-updates-and-commentary-august-2026">Kiplinger &mdash; Nvidia earnings live updates, August 2026</a> &middot; '
 '<a href="https://stockstory.org/us/stocks/nyse/anf/news/earnings/abercrombie-and-fitchs-nyseanf-q2-cy2026-beats-on-revenue-stock-jumps-119percent">StockStory &mdash; Abercrombie &amp; Fitch Q2 CY2026 (11:39 a.m. read)</a> &middot; '
 '<a href="https://markets.financialcontent.com/stocks/article/stockstory-2026-8-26-williams-sonoma-nysewsm-exceeds-q2-cy2026-expectations">StockStory &mdash; Williams-Sonoma exceeds Q2 CY2026 expectations</a> &middot; '
 '<a href="https://www.investing.com/news/transcripts/earnings-call-transcript-williamssonoma-tops-q2-2026-estimates-shares-slip-93CH-4877547">Investing.com &mdash; Williams-Sonoma Q2 2026 earnings call transcript</a> &middot; '
 '<a href="https://news.alphastreet.com/hp-q3-2026-earnings-preview-august-26-street-expects-0-72-eps/">AlphaStreet &mdash; HP Q3 2026 preview ($0.72 street estimate)</a> &middot; '
 '<a href="https://www.tradingview.com/news/tradingview:998e11fa59a6e:0-hpq-q3-26-earnings-eps-estimate-is-0-69-usd/">TradingView &mdash; HPQ Q3&rsquo;26 EPS estimate $0.69</a></p>\n')
w=rep(w,A,NEW,'ws sources')
io.open(os.path.join(O,'wallstreet-briefing.html'),'w',encoding='utf-8').write(w)
c=io.open(os.path.join(O,'cyber-briefing.html'),encoding='utf-8').read()
NEWC=(A+'<p class="note"><b>Added 5:36:</b> <a href="https://www.securityweek.com/adobe-and-nvidia-patch-dozens-of-vulnerabilities/">SecurityWeek &mdash; Adobe and Nvidia patch dozens of vulnerabilities</a> &middot; '
 '<a href="https://www.securityweek.com/wordpress-websites-targeted-via-miniorange-plugin-vulnerabilities/">SecurityWeek &mdash; WordPress sites targeted via MiniOrange plugin flaws</a> &middot; '
 '<a href="https://patchstack.com/articles/one-slug-seven-editions-the-miniorange-saml-sso-bug-that-let-anyone-log-in-as-your-wordpress-admin/">Patchstack &mdash; MiniOrange SAML SSO authentication bypass analysis</a> &middot; '
 '<a href="https://www.securityweek.com/sensitive-information-exposed-in-nutex-health-data-breach/">SecurityWeek &mdash; Nutex Health data breach</a> &middot; '
 '<a href="https://www.securityweek.com/reliaquest-confirms-shinyhunters-hack-but-says-impact-was-limited/">SecurityWeek &mdash; ReliaQuest confirms ShinyHunters hack</a> &middot; '
 '<a href="https://www.securityweek.com/cisa-over-100-internet-exposed-water-systems-targeted-in-july-cyberattacks/">SecurityWeek &mdash; CISA: 100+ internet-exposed water systems targeted in July</a> &middot; '
 '<a href="https://www.securityweek.com/chrome-152-patches-over-300-vulnerabilities/">SecurityWeek &mdash; Chrome 152 patches over 300 vulnerabilities</a> &middot; '
 '<a href="https://www.securityweek.com/first-malware-built-specifically-for-car-head-units-fuels-botnet/">SecurityWeek &mdash; First malware built for car head units</a> &middot; '
 '<a href="https://www.cyera.com/research/nemoclaw-one-website-visit-to-hijack-your-ai-agent">Cyera &mdash; NemoClaw AI-agent hijack research</a></p>\n')
c=rep(c,A,NEWC,'cy sources')
io.open(os.path.join(O,'cyber-briefing.html'),'w',encoding='utf-8').write(c)
if fails: print("FAILED",fails); sys.exit(1)
print("sources OK")
