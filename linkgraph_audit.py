#!/usr/bin/env python3
"""Solar link-graph audit: dead-end pages, orphans, buyer-intent readiness."""
import os, re, collections

BASE = "/mnt/ai-shared/cluster/websites/adsense-portfolio/solarpoweredproject/content"
pages = {}  # rel path -> set of outbound internal links
inbound = collections.defaultdict(set)

for root, dirs, files in os.walk(BASE):
    for fn in files:
        if not fn.endswith(".md"):
            continue
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, BASE)
        src = open(p, errors="replace").read()
        links = set()
        # markdown links + href in raw html
        for m in re.finditer(r'\]\((/[^)#\s]+)[^)]*\)', src):
            links.add(m.group(1))
        for m in re.finditer(r'href="(/[^"]+)"', src):
            links.add(m.group(1))
        pages[rel] = links
        for l in links:
            inbound[l].add(rel)

deadends = {p for p, ls in pages.items() if len(ls) == 0}
# orphan = article nobody links to (approximate: check both /pages/x.html and /pages/x/ forms)
orphans = []
for p in pages:
    stem = p[:-3]
    candidates = [f"/{stem}.html", f"/{stem}/", f"/{stem}"]
    hits = sum(len(inbound[c]) for c in candidates)
    if hits == 0:
        orphans.append(p)

print(f"pages: {len(pages)}")
print(f"dead-end pages (0 outbound): {len(deadends)}")
for p in sorted(deadends)[:12]:
    print("  ", p)
print(f"orphan pages (0 inbound): {len(orphans)}")
for p in sorted(orphans)[:12]:
    print("  ", p)

# buyer-intent pages link readiness
buyer = [p for p in pages if re.search(r'(best|vs|compare|cost|cheap|kit|review|diy-vs)', p)]
print(f"\nbuyer-intent pages: {len(buyer)}")
withlinks = [p for p in buyer if any('amazon' in l or 'aff' in l or 'tag=' in l for l in pages[p])]
print(f"  with affiliate-style outbound links: {len(withlinks)}")
