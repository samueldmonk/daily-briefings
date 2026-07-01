#!/usr/bin/env python3
import os
import re
from datetime import datetime
from collections import defaultdict

archive_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'archive')

# Collect files by date
files_by_date = defaultdict(lambda: defaultdict(list))

for fname in os.listdir(archive_dir):
    if not fname.endswith('.html'):
        continue
    
    # Parse filename: section-YYYY-MM-DD-HHMM.html
    match = re.match(r'(cyber|wallstreet|mma)-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.html', fname)
    if not match:
        continue
    
    section, year, month, day, hhmm = match.groups()
    date_key = f"{year}-{month}-{day}"
    hour = int(hhmm[:2])
    minute = int(hhmm[2:])
    ampm = 'AM' if hour < 12 else 'PM'
    if hour > 12:
        hour -= 12
    elif hour == 0:
        hour = 12
    time_str = f"{hour}:{minute:02d} {ampm} ET"
    
    section_name = {
        'cyber': 'The Cyber Wire',
        'wallstreet': 'The Closing Bell',
        'mma': 'The Octagon'
    }[section]
    
    files_by_date[date_key][section].append((time_str, fname))

# Sort dates descending
sorted_dates = sorted(files_by_date.keys(), reverse=True)

html = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Archive — Daily Briefings</title>
	<style>
		* { margin: 0; padding: 0; box-sizing: border-box; }
		:root {
			--bg: #0a0a0a;
			--fg: #e0e0e0;
			--panel: #161616;
			--line: #2a2a2a;
			--mono: 'Monaco', 'Courier New', monospace;
		}
		body {
			background: var(--bg);
			color: var(--fg);
			font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
			line-height: 1.6;
			padding: 20px;
		}
		.container { max-width: 900px; margin: 0 auto; }
		.masthead {
			display: flex;
			align-items: center;
			gap: 12px;
			margin-bottom: 20px;
			flex-wrap: wrap;
		}
		.masthead h1 {
			font-size: 28px;
			font-weight: 300;
			letter-spacing: 0.5px;
		}
		.pill {
			background: var(--panel);
			border: 1px solid var(--line);
			border-radius: 20px;
			padding: 6px 12px;
			font-family: var(--mono);
			font-size: 11px;
			letter-spacing: 0.12em;
			text-transform: uppercase;
			color: #999;
		}
		.nav {
			display: flex;
			gap: 8px;
			margin-bottom: 20px;
			border-bottom: 1px solid var(--line);
			padding-bottom: 12px;
			overflow-x: auto;
		}
		.nav a {
			font-family: var(--mono);
			font-size: 12px;
			letter-spacing: 0.1em;
			text-transform: uppercase;
			text-decoration: none;
			color: #666;
			padding: 8px 12px;
			border-radius: 6px;
			transition: all 0.2s;
			white-space: nowrap;
		}
		.nav a:hover { color: var(--fg); }
		.nav a.active {
			color: var(--fg);
			background: var(--panel);
		}
		.note {
			background: var(--panel);
			border: 1px solid var(--line);
			border-radius: 10px;
			padding: 15px;
			margin-bottom: 20px;
			font-size: 13px;
			color: #aaa;
			font-style: italic;
		}
		.date-section {
			margin-bottom: 30px;
		}
		.date-header {
			font-family: var(--mono);
			font-size: 13px;
			letter-spacing: 0.12em;
			text-transform: uppercase;
			color: #999;
			padding-bottom: 10px;
			border-bottom: 1px solid var(--line);
			margin-bottom: 12px;
		}
		.snapshot-row {
			display: grid;
			grid-template-columns: auto 1fr;
			gap: 16px;
			align-items: center;
			background: var(--panel);
			border: 1px solid var(--line);
			border-radius: 10px;
			padding: 12px;
			margin-bottom: 8px;
		}
		.time {
			font-family: var(--mono);
			font-size: 11px;
			color: #666;
			min-width: 140px;
		}
		.sections {
			display: flex;
			gap: 8px;
			flex-wrap: wrap;
		}
		.section-link {
			display: inline-block;
			padding: 6px 12px;
			background: linear-gradient(135deg, #1a1a1a, #222);
			border: 1px solid #333;
			border-radius: 6px;
			text-decoration: none;
			color: #aaa;
			font-size: 12px;
			transition: all 0.2s;
		}
		.section-link:hover {
			color: #fff;
			border-color: #555;
			transform: translateY(-1px);
		}
		footer {
			margin-top: 30px;
			padding-top: 20px;
			border-top: 1px solid var(--line);
			font-size: 12px;
			color: #666;
		}
	</style>
</head>
<body>
	<div class="container">
		<div class="masthead">
			<h1>Archive</h1>
			<span class="pill">🗄 Snapshots</span>
		</div>

		<div class="nav">
			<a href="index.html">★ Front Page</a>
			<a href="cyber-briefing.html">⛨ The Cyber Wire</a>
			<a href="wallstreet-briefing.html">▲ The Closing Bell</a>
			<a href="mma-briefing.html">⊘ The Octagon</a>
			<a href="archive.html" class="active">🗄 Archive</a>
		</div>

		<div class="note">
			📌 <strong>Point-in-Time Snapshots:</strong> Each edition below is a complete briefing captured at a specific date and time. Markets, events, and threat levels reflect conditions at that moment and are not updated retroactively. For current briefings, return to the <a href="index.html" style="color: inherit; text-decoration: underline;">Front Page</a>.
		</div>
'''

for date_key in sorted_dates:
    # Parse date for display
    year, month, day = date_key.split('-')
    date_obj = datetime(int(year), int(month), int(day))
    date_display = date_obj.strftime('%A, %B %d, %Y')
    
    html += f'\n\t\t<div class="date-section">\n\t\t\t<div class="date-header">{date_display}</div>\n'
    
    sections_dict = files_by_date[date_key]
    
    # Collect all unique times for this date
    times_set = set()
    for section in sections_dict:
        for time_str, _ in sections_dict[section]:
            times_set.add(time_str)
    
    sorted_times = sorted(times_set, reverse=True)
    
    for time_str in sorted_times:
        html += f'\t\t\t<div class="snapshot-row">\n\t\t\t\t<div class="time">{time_str}</div>\n\t\t\t\t<div class="sections">\n'
        
        for section in ['cyber', 'wallstreet', 'mma']:
            section_name = {
                'cyber': '⛨ The Cyber Wire',
                'wallstreet': '▲ The Closing Bell',
                'mma': '⊘ The Octagon'
            }[section]
            
            # Find matching file for this time
            found = False
            for s in sections_dict:
                if s == section:
                    for ts, fname in sections_dict[s]:
                        if ts == time_str:
                            html += f'\t\t\t\t\t<a href="archive/{fname}" class="section-link">{section_name}</a>\n'
                            found = True
                            break
            
            if not found:
                html += f'\t\t\t\t\t<span style="color: #444; padding: 6px 12px; font-size: 12px;">{section_name}</span>\n'
        
        html += '\t\t\t\t</div>\n\t\t\t</div>\n'
    
    html += '\t\t</div>\n'

html += '''
		<footer>
			<p>&copy; 2026 Daily Briefings. <a href="index.html" style="color: inherit;">Return to current editions</a>.</p>
		</footer>
	</div>
</body>
</html>
'''

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'archive.html'), 'w') as f:
    f.write(html)

print("✓ archive.html regenerated")
